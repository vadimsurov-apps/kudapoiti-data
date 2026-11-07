"""Точный дом по адресу из выгрузки OSM (07.11, Вадим: «точки часто совсем не на том доме»).

Раньше адрес искали через Nominatim/Photon — они угадывают по похожести и часто ставят точку на соседний дом.
Здесь сопоставление СТРОГОЕ: улица (без учёта порядка слов и сокращений) + номер дома + корпус/строение
по зданиям из локальной выгрузки OSM (в Москве у зданий почти везде есть адреса).

Для каждого места с адресом:
- нашли здание, и текущая точка уже внутри него — ничего не меняем (status ok);
- текущая точка вне этого здания (стоит на другом доме) — переносим: на главный вход здания (entrance=main) или на
  единственный вход; если входов несколько и главный не отмечен — в центр здания (status moved);
- здание не нашли — status not-found (ничего не меняем).
Нужны файлы из osm-local.yml: bld.geojsonseq (здания с адресом) и entr.geojsonseq (входы).
Выход: auto/osm-address.json — его применяет сборка (tools/xlsx_to_json.py), если в таблице точку не правили вручную."""
import json, math, os, re
from collections import defaultdict

CELL = 0.01
TYPES = {"ул": "улица", "улица": "улица", "пр-т": "проспект", "просп": "проспект", "проспект": "проспект",
         "пр-д": "проезд", "проезд": "проезд", "ш": "шоссе", "шоссе": "шоссе", "наб": "набережная",
         "набережная": "набережная", "пер": "переулок", "переулок": "переулок", "б-р": "бульвар", "бул": "бульвар",
         "бульвар": "бульвар", "пл": "площадь", "площадь": "площадь", "туп": "тупик", "пр": "проспект", "тупик": "тупик",
         "аллея": "аллея", "линия": "линия", "мкр": "микрорайон", "микрорайон": "микрорайон", "кв-л": "квартал",
         "квартал": "квартал", "тракт": "тракт", "спуск": "спуск", "просек": "просек", "дорога": "дорога"}
CITY_WORDS = {"москва", "г", "город", "россия", "московская", "область", "обл", "мо", "пос", "поселение", "пгт",
              "деревня", "д", "село", "с", "рп", "городской", "округ", "го"}


def dist(a, b, c, d):
    R = 6371000
    p1, p2 = math.radians(a), math.radians(c)
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(math.radians(d - b) / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


def street_key(s):
    s = s.lower().replace("ё", "е").replace(".", " ")
    w = [TYPES.get(x, x) for x in re.findall(r"[а-яa-z0-9-]+", s)]
    return " ".join(sorted(x for x in w if x))


def house_key(s):
    s = s.lower().replace("ё", "е").replace(" ", "")
    s = re.sub(r"^(д|дом|вл|влад|владение)\.?", "", s)
    s = re.sub(r"(корпус|корп\.?|к\.)", "к", s)
    s = re.sub(r"(строение|стр\.?|с\.)", "с", s)
    s = s.replace(",", "")
    return s


def parse(addr):
    """адрес места → (street_key, house_key) или None"""
    if not addr:
        return None
    a = re.sub(r"[«\"][^»\"]*[»\"]", " ", addr)          # названия ТЦ в кавычках
    a = re.sub(r"\(.*?\)", " ", a)
    parts = [x.strip() for x in a.split(",") if x.strip()]
    for i, part in enumerate(parts):
        words = re.findall(r"[а-яёa-z-]+\.?", part.lower())
        if any(w.rstrip(".") in TYPES for w in words) and not re.search(r"\d+\s*(этаж|эт)", part.lower()):
            num = None
            m = re.search(r"\s(\d+[а-я]?(?:\s*(?:к|корп\.?|с|стр\.?)\s*\d+)*)$", part)   # «ул. Ленина 5»
            rest = parts[i + 1:]
            if m:
                num, street = m.group(1), part[:m.start()]
            else:
                street = part
                if rest and re.match(r"^(д\.?\s*|вл\.?\s*|влад\.?\s*)?\d", rest[0].lower()):
                    num, rest = rest[0], rest[1:]
            if not num:
                continue                                   # «мкр Сходня» без номера — улица дальше
            for r in rest[:2]:                            # «корп. 2», «стр. 1»
                if re.match(r"^(к|корп|корпус|с|стр|строение)\.?\s*\d", r.lower()):
                    num += " " + r
            sk = street_key(street)
            if not sk or all(w in CITY_WORDS for w in sk.split()):
                continue
            return sk, house_key(num)
    # без слова «улица»: «Знаменские Садки, 5Б»
    for i, part in enumerate(parts[:-1]):
        if re.search(r"\d", part) or not re.search(r"[а-яё]{3}", part.lower()):
            continue
        if re.match(r"^(д\.?\s*|вл\.?\s*)?\d+[а-я]?(\s*(к|с|корп|стр)\.?\s*\d+)?$", parts[i + 1].lower()):
            sk = street_key(part)
            if sk and not all(w in CITY_WORDS for w in sk.split()):
                return sk, house_key(parts[i + 1])
    return None


def read(path):
    with open(path) as f:
        for line in f:
            line = line.strip().lstrip("\x1e")
            if line:
                yield json.loads(line)


def rings(g):
    if g["type"] == "Polygon":
        return [g["coordinates"][0]]
    if g["type"] == "MultiPolygon":
        return [p[0] for p in g["coordinates"]]
    return []


def inside(lat, lon, ring):
    c = False
    j = len(ring) - 1
    for i in range(len(ring)):
        xi, yi = ring[i]; xj, yj = ring[j]
        if (yi > lat) != (yj > lat) and lon < (xj - xi) * (lat - yi) / (yj - yi + 1e-12) + xi:
            c = not c
        j = i
    return c


def edge_dist(lat, lon, ring):
    return min(dist(lat, lon, y, x) for x, y in ring)


def main():
    idx = defaultdict(list)          # (street_key, house_key) → здания
    n = 0
    for f in read("bld.geojsonseq"):
        t, g = f.get("properties", {}), f.get("geometry")
        if not g or not t.get("addr:street") or not t.get("addr:housenumber"):
            continue
        rs = rings(g)
        if not rs:
            continue
        pts = [p for r in rs for p in r]
        lat = sum(p[1] for p in pts) / len(pts); lon = sum(p[0] for p in pts) / len(pts)
        b = {"lat": lat, "lon": lon, "rings": rs, "osm": f'{t.get("@type")}/{t.get("@id")}',
             "city": (t.get("addr:city") or t.get("addr:place") or "").lower().replace("ё", "е"),
             "addr": f'{t["addr:street"]}, {t["addr:housenumber"]}'}
        idx[(street_key(t["addr:street"]), house_key(t["addr:housenumber"]))].append(b)
        n += 1
    print("зданий с адресом:", n, flush=True)

    eg = defaultdict(list)
    for f in read("entr.geojsonseq"):
        g = f.get("geometry") or {}
        if g.get("type") != "Point": continue
        t = f.get("properties", {})
        if t.get("access") in ("private", "no") or t.get("entrance") in ("service", "emergency", "exit"): continue
        lon, lat = g["coordinates"]
        eg[(int(lat / CELL), int(lon / CELL))].append((lat, lon, t))

    places = json.load(open("places.json"))["places"]
    poi = json.load(open("auto/geocode-report.json")) if os.path.exists("auto/geocode-report.json") else {}
    BIG = {"парк", "усадьба", "прогулка", "зоопарк", "ботанический сад", "пляж", "детская площадка", "экопарк",
           "парк развлечений", "лесопарк", "музей-заповедник", "ферма", "конный клуб"}
    out = {}
    for p in places:
        if p.get("lat") is None: continue
        if (p.get("type") or [""])[0] in BIG:          # территории: адрес — это контора, а не вход (входы — osm_local)
            out[p["id"]] = {"status": "territory"}; continue
        q = poi.get(p["id"], {})
        if q.get("status") == "high" and dist(q["lat"], q["lon"], p["lat"], p["lon"]) < 60:
            out[p["id"]] = {"status": "poi"}; continue   # точка уже на объекте OSM с тем же названием
        key = parse(p.get("address"))
        if not key:
            out[p["id"]] = {"status": "no-address"}; continue
        cands = idx.get(key, [])
        cands = [b for b in cands if dist(b["lat"], b["lon"], p["lat"], p["lon"]) < 8000]   # тот же город/район
        if not cands:
            out[p["id"]] = {"status": "not-found", "key": " | ".join(key)}; continue
        b = min(cands, key=lambda b: dist(b["lat"], b["lon"], p["lat"], p["lon"]))
        rec = {"src": [p["lat"], p["lon"]], "building": b["osm"], "addr": b["addr"]}
        if any(inside(p["lat"], p["lon"], r) for r in b["rings"]) or min(edge_dist(p["lat"], p["lon"], r) for r in b["rings"]) < 4:
            rec["status"] = "ok"; out[p["id"]] = rec; continue
        gi, gj = int(b["lat"] / CELL), int(b["lon"] / CELL)
        ents = [e for di in (-1, 0, 1) for dj in (-1, 0, 1) for e in eg.get((gi + di, gj + dj), [])
                if min(edge_dist(e[0], e[1], r) for r in b["rings"]) < 2.5]
        main_e = [e for e in ents if e[2].get("entrance") == "main"]
        pick = main_e[0] if len(main_e) == 1 else (ents[0] if len(ents) == 1 else None)
        if pick:
            rec.update(lat=round(pick[0], 6), lon=round(pick[1], 6), method="osm-entrance",
                       entrance=pick[2].get("name") or pick[2].get("ref") or pick[2].get("entrance"))
        else:
            rec.update(lat=round(b["lat"], 6), lon=round(b["lon"], 6), method="osm-building", entrances=len(ents))
        rec["moved_m"] = round(dist(p["lat"], p["lon"], rec["lat"], rec["lon"]))
        rec["status"] = "moved"
        if rec["moved_m"] > 2000:
            # далеко: в Подмосковье одинаковые улицы в соседних городах — переносим, только если город сходится
            first = (p.get("address") or "").split(",")[0].lower().replace("ё", "е")
            town = re.sub(r"^(г\.?|город|пос\.?|пгт|д\.?|деревня|с\.?|рп)\s+", "", first).strip()
            if not (b["city"] and town and (town in b["city"] or b["city"] in town)) and not (not b["city"] and p.get("coord_exact") is None and "москва" in (p.get("address") or "").lower()):
                rec["status"] = "far-unsure"
        out[p["id"]] = rec
    os.makedirs("auto", exist_ok=True)
    json.dump(out, open("auto/osm-address.json", "w"), ensure_ascii=False, indent=0, sort_keys=True)
    from collections import Counter
    print("Итого:", Counter(r["status"] for r in out.values()),
          "перенос: на вход", sum(1 for r in out.values() if r.get("method") == "osm-entrance"))


if __name__ == "__main__":
    main()
