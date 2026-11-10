"""Входы для больших объектов (парки, усадьбы, зоопарки, музеи-комплексы, ТЦ).
Для мест, у которых в auto/geocode-report.json найден OSM-объект-контур (way/relation), ищем узлы-входы:
entrance=*, barrier=gate/entrance на контуре или в 40 м от него. Выбираем вход, ближайший к станции метро места
(или главный, если отмечен entrance=main). Пишет auto/entrances.json: {id: {lat, lon, name, kind, dist_metro_m}}."""
import json, math, re, sys, time, urllib.parse, urllib.request

SERVERS = ["https://overpass-api.de/api/interpreter", "https://overpass.kumi.systems/api/interpreter",
           "https://maps.mail.ru/osm/tools/overpass/api/interpreter"]
UA = {"User-Agent": "kudapoiti-entrances/1.0 (github.com/vadimsurov-apps/kudapoiti-data)"}
BIG = {"парк", "ботанический сад", "усадьба", "зоопарк", "кремль", "монастырь", "парк развлечений", "ферма",
       "контактный зоопарк", "пляж", "горнолыжный курорт", "железная дорога", "аквапарк"}
MET = [(n, float(a), float(b)) for n, a, b in
       re.findall(r'": \("([^"]+)", ([\d.]+), ([\d.]+)\)', open("tools/MetroStations.swift").read())]


def dist(a, b, c, d):
    return math.hypot((a - c) * 111320, (b - d) * 111320 * math.cos(math.radians(a)))


def overpass(q):
    data = urllib.parse.urlencode({"data": q}).encode()
    for url in SERVERS:
        for _ in range(2):
            try:
                with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=UA), timeout=120) as r:
                    return json.load(r)["elements"]
            except Exception as e:
                print("  overpass:", url, e, file=sys.stderr); time.sleep(8)
    return None


def main():
    places = {p["id"]: p for p in json.load(open("places-all.json" if __import__("os").path.exists("places-all.json") else "places.json"))["places"]}
    rep = json.load(open("auto/geocode-report.json"))
    out = {}
    for pid, r in rep.items():
        p = places.get(pid)
        if not p or r.get("status") not in ("high", "medium") or r.get("kind") not in ("way", "relation"): continue
        if p["type"][0] not in BIG and not re.search(r"ТЦ|ТРЦ|ТРК", p.get("address") or ""): continue
        t, i = r["osm"].split("/")
        sel = f"{t}({i})" if t == "way" else f"relation({i});way(r)"
        q = (f'[out:json][timeout:90];{sel}->.a;(node(w.a)["entrance"];node(w.a)["barrier"~"gate|entrance|turnstile"];'
             f'node(w.a)["highway"="footway"]["entrance"];);out tags;'
             f'({sel};)->.b;node(around.b:40)["entrance"];out tags;')
        els = overpass(q)
        if not els:
            continue
        seen = {}
        for e in els:
            if "lat" in e: seen[e["id"]] = e
        if not seen: continue
        # ближайшее метро к центру объекта
        mlat, mlon = r["lat"], r["lon"]
        dm, mn, ma, mb = min((dist(mlat, mlon, a, b), n, a, b) for n, a, b in MET)
        best = None
        for e in seen.values():
            tg = e.get("tags", {})
            main_bonus = -400 if tg.get("entrance") == "main" else 0
            if tg.get("access") in ("private", "no") or tg.get("entrance") in ("service", "emergency", "exit"): continue
            score = (dist(e["lat"], e["lon"], ma, mb) if dm < 2500 else dist(e["lat"], e["lon"], p["lat"], p["lon"])) + main_bonus
            if best is None or score < best[0]: best = (score, e)
        if not best: continue
        e = best[1]; tg = e.get("tags", {})
        out[pid] = {"lat": round(e["lat"], 6), "lon": round(e["lon"], 6), "name": tg.get("name") or tg.get("ref"),
                    "kind": tg.get("entrance") or tg.get("barrier"), "osm": f"node/{e['id']}",
                    "metro": mn if dm < 2500 else None, "dist_metro_m": round(dist(e["lat"], e["lon"], ma, mb)),
                    "entrances_found": len(seen)}
        print(pid, out[pid], flush=True)
        time.sleep(1.2)
    json.dump(out, open("auto/entrances.json", "w"), ensure_ascii=False, indent=0)
    print("Итого входов:", len(out))


main()
