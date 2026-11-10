"""Сплошная проверка координат: для каждого места ищем в OpenStreetMap сам объект (по названию и типу)
рядом с текущей точкой и берём его точные координаты (вход, если отмечен).
Пишет auto/geocode-report.json. В places.json ничего не меняет — применяет tools/apply_geocode.py."""
import json, math, os, re, sys, time, urllib.parse, urllib.request

SERVERS = ["https://overpass-api.de/api/interpreter", "https://overpass.kumi.systems/api/interpreter",
           "https://maps.mail.ru/osm/tools/overpass/api/interpreter"]
UA = {"User-Agent": "kudapoiti-geocode/1.0 (github.com/vadimsurov-apps/kudapoiti-data)"}

# какие OSM-теги подходят к нашему типу места
TYPE_TAGS = {
    "музей": [("tourism", "museum|gallery")], "музей науки": [("tourism", "museum")], "музей-макет": [("tourism", "museum")],
    "театр": [("amenity", "theatre|arts_centre")], "цирк": [("amenity", "theatre|circus|arts_centre")],
    "кинотеатр": [("amenity", "cinema")], "концертный зал": [("amenity", "theatre|concert_hall|arts_centre")],
    "парк": [("leisure", "park|garden")], "ботанический сад": [("leisure", "garden|park")],
    "усадьба": [("tourism", "museum|attraction"), ("historic", ".")], "кремль": [("historic", "."), ("tourism", ".")],
    "монастырь": [("amenity", "place_of_worship"), ("historic", ".")],
    "кафе": [("amenity", "cafe|restaurant|fast_food|ice_cream")],
    "прогулка": [("amenity", "ferry_terminal"), ("man_made", "pier"), ("public_transport", "platform|stop_position|station")],
    "аквапарк": [("leisure", "water_park|sports_centre|swimming_pool")],
    "бассейн": [("leisure", "sports_centre|swimming_pool|water_park")], "детский бассейн": [("leisure", "sports_centre|swimming_pool")],
    "зоопарк": [("tourism", "zoo|attraction")], "контактный зоопарк": [("tourism", "zoo|attraction"), ("shop", ".")],
    "ферма": [("tourism", "zoo|attraction"), ("place", "farm|hamlet"), ("landuse", "farmyard")],
    "библиотека": [("amenity", "library")], "каток": [("leisure", "ice_rink|sports_centre")],
    "скалодром": [("leisure", "sports_centre|climbing")], "картинг": [("sport", "karting"), ("leisure", "sports_centre")],
    "конный клуб": [("leisure", "horse_riding|sports_centre"), ("sport", "equestrian")],
}
GENERIC = set("""музей музея парк театр детский детская детское центр центра кафе ресторан кинотеатр клуб студия школа
бассейн аквапарк каток зоопарк контактный ферма усадьба москва москвы московский московская государственный
им имени и в на по для с от у дом мастерская мастер класс игровой развлекательный батутный верёвочный веревочный
парк-отель семейный экскурсия прогулка тц трц мц""".split())


def norm(s):
    return re.sub(r"[^a-zа-я0-9 ]", " ", s.lower().replace("ё", "е"))


def tokens(name):
    q = re.findall(r"[«\"]([^»\"]+)[»\"]", name)
    base = q[0] if q else re.sub(r"\(.*?\)", "", name)
    toks = [t for t in norm(base).split() if len(t) > 2 and t not in GENERIC]
    return toks or [t for t in norm(name).split() if len(t) > 2][:2]


def sim(a, b):
    ta, tb = set(tokens(a)), set(norm(b).split())
    if not ta: return 0
    hit = sum(1 for t in ta if any(x.startswith(t[:max(4, len(t) - 2)]) for x in tb))
    return hit / len(ta)


def dist(a, b, c, d):
    return math.hypot((a - c) * 111320, (b - d) * 111320 * math.cos(math.radians(a)))


def overpass(q):
    data = urllib.parse.urlencode({"data": q}).encode()
    for url in SERVERS:
        for _ in range(2):
            try:
                with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=UA), timeout=90) as r:
                    return json.load(r)["elements"]
            except Exception as e:
                print("  overpass:", url, e, file=sys.stderr); time.sleep(8)
    return None


def find(p):
    r = find_by(p, p["name"])
    # причалы, ТЦ и т.п.: название объекта часто в адресе — «причал «Киевский вокзал»», «ТРЦ «Ривьера»»
    addr_q = re.findall(r"[«\"]([^»\"]+)[»\"]", p.get("address") or "")
    if r.get("status") in ("not-found", "low", "no-name") and addr_q:
        r2 = find_by(p, addr_q[0], via_address=True)
        if r2.get("status") in ("high", "medium"):
            r2["status"] = "medium"; r2["via"] = "адрес: " + addr_q[0]
            return r2
    return r


def find_by(p, name, via_address=False):
    toks = tokens(name)
    if not toks or p.get("lat") is None: return {"status": "no-name"}
    rx = "|".join(re.escape(t[:max(4, len(t) - 2)]) for t in toks)
    R = 4000 if p["type"][0] not in ("прогулка",) else 2500
    q = (f'[out:json][timeout:60];(nwr(around:{R},{p["lat"]},{p["lon"]})["name"~"{rx}",i];'
         f'nwr(around:{R},{p["lat"]},{p["lon"]})["name:ru"~"{rx}",i];'
         f'nwr(around:{R},{p["lat"]},{p["lon"]})["alt_name"~"{rx}",i];);out center tags;')
    els = overpass(q)
    if els is None: return {"status": "error"}
    want = TYPE_TAGS.get(p["type"][0], [])
    best = None
    for e in els:
        t = e.get("tags", {})
        if t.get("railway") or t.get("highway"): continue
        if t.get("public_transport") == "station" and p["type"][0] != "прогулка": continue
        lat = e.get("lat") or e.get("center", {}).get("lat"); lon = e.get("lon") or e.get("center", {}).get("lon")
        if lat is None: continue
        names = " ".join(t.get(k, "") for k in ("name", "name:ru", "alt_name", "official_name"))
        s = sim(name, names)
        tag_ok = any(k in t and re.search(v, t[k]) for k, v in want) if want and not via_address else None
        score = s + (0.35 if tag_ok else 0) - (0.3 if want and not tag_ok else 0) - dist(lat, lon, p["lat"], p["lon"]) / 20000
        if s >= 0.5 and (best is None or score > best["score"]):
            best = {"score": round(score, 3), "sim": round(s, 2), "tag_ok": tag_ok, "lat": round(lat, 6), "lon": round(lon, 6),
                    "osm": f'{e["type"]}/{e["id"]}', "osm_name": t.get("name"), "kind": e["type"]}
    if not best: return {"status": "not-found", "found": len(els)}
    best["moved_m"] = round(dist(best["lat"], best["lon"], p["lat"], p["lon"]))
    best["status"] = "high" if best["sim"] >= 0.99 and best["tag_ok"] is not False else ("medium" if best["sim"] >= 0.66 else "low")
    return best


def main():
    places = json.load(open("places-all.json" if __import__("os").path.exists("places-all.json") else "places.json"))["places"]
    path = "auto/geocode-report.json"
    old = json.load(open(path)) if os.path.exists(path) else {}
    only = set(sys.argv[1:])
    out = {}
    for i, p in enumerate(places):
        if only and p["id"] not in only: continue
        if not only and p["id"] in old and old[p["id"]].get("status") not in ("error",) and \
                old[p["id"]].get("src") == [p.get("lat"), p.get("lon")]:
            out[p["id"]] = old[p["id"]]; continue
        r = find(p); r["src"] = [p.get("lat"), p.get("lon")]; r["name"] = p["name"]; r["type"] = p["type"][0]
        out[p["id"]] = r
        print(i, p["id"], r["status"], r.get("moved_m"), r.get("osm_name"), flush=True)
        if len(out) % 20 == 0:   # сохраняем по ходу: если прогон прервётся по времени, результаты не пропадут
            os.makedirs("auto", exist_ok=True)
            json.dump({**old, **out}, open(path, "w"), ensure_ascii=False, indent=0)
        time.sleep(1.2)
    os.makedirs("auto", exist_ok=True)
    json.dump(out if not only else {**old, **out}, open(path, "w"), ensure_ascii=False, indent=0)
    from collections import Counter
    print("Итого:", Counter(r["status"] for r in out.values()))


if __name__ == "__main__":
    main()
