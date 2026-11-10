"""Как попасть в место — подсказки из выгрузки OSM (07.11, Вадим: «подъезд, этаж, номер помещения, домофон,
шлагбаум, платная или бесплатная парковка — максимально точно и полезно»).

Для каждого места с точкой собирает то, что знает OSM:
- объект места (если найден по названию, auto/geocode-report.json): этаж (level, addr:floor), помещение (addr:unit,
  addr:door, addr:flats), вход (entrance), доступность для колясок (wheelchair);
- здание по адресу (auto/osm-address.json): входы с номерами подъездов/названиями;
- шлагбаумы и ворота в радиусе 60 м;
- парковки в радиусе 300 м: платная/бесплатная (fee), тип (наземная/подземная/многоуровневая), для кого (access),
  вместимость, название.
Это сырьё: итоговый текст «Как найти» и поле «Парковка» пишет робот «навигатор», сверяя с сайтом места.
Нужны файлы из osm-local.yml: named.geojsonseq, entr.geojsonseq, bld.geojsonseq, park.geojsonseq.
Выход: auto/osm-access.json"""
import json, math, os
from collections import defaultdict

CELL = 0.01
POI_KEYS = ("level", "addr:floor", "addr:unit", "addr:door", "addr:flats", "entrance", "wheelchair", "level:ref",
            "access", "fee", "description", "note", "phone", "contact:phone", "website",
            "contact:website", "url", "opening_hours")


def dist(a, b, c, d):
    R = 6371000
    p1, p2 = math.radians(a), math.radians(c)
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(math.radians(d - b) / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


def read(path):
    if not os.path.exists(path):
        return
    with open(path) as f:
        for line in f:
            line = line.strip().lstrip("\x1e")
            if line:
                yield json.loads(line)


def center(g):
    t = g.get("type")
    if t == "Point":
        return g["coordinates"][1], g["coordinates"][0]
    pts = []
    if t == "LineString":
        pts = g["coordinates"]
    elif t == "Polygon":
        pts = g["coordinates"][0]
    elif t == "MultiPolygon":
        pts = [p for poly in g["coordinates"] for p in poly[0]]
    if not pts:
        return None
    return sum(p[1] for p in pts) / len(pts), sum(p[0] for p in pts) / len(pts)


def cell(lat, lon):
    return int(lat / CELL), int(lon / CELL)


def around(grid, lat, lon):
    i, j = cell(lat, lon)
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            yield from grid.get((i + di, j + dj), [])


def main():
    places = [p for p in json.load(open("places-all.json" if __import__("os").path.exists("places-all.json") else "places.json"))["places"] if p.get("lat") is not None]
    poi = json.load(open("auto/geocode-report.json")) if os.path.exists("auto/geocode-report.json") else {}
    addr = json.load(open("auto/osm-address.json")) if os.path.exists("auto/osm-address.json") else {}

    # 1) теги объектов мест (только нужные id, файл большой — читаем потоком)
    want = {}
    for pid, q in poi.items():
        if q.get("status") == "high" and q.get("osm"):
            want.setdefault(q["osm"], []).append(pid)
    poi_tags = {}
    for f in read("named.geojsonseq"):
        t = f.get("properties", {})
        key = f'{t.get("@type")}/{t.get("@id")}'
        if key in want:
            tags = {k: t[k] for k in POI_KEYS if k in t}
            for pid in want[key]:
                poi_tags[pid] = tags
    print("объекты мест с тегами:", len(poi_tags), flush=True)

    # 2) входы и шлагбаумы
    ent = defaultdict(list)
    for f in read("entr.geojsonseq"):
        g = f.get("geometry") or {}
        if g.get("type") != "Point":
            continue
        t = f.get("properties", {})
        lon, lat = g["coordinates"]
        ent[cell(lat, lon)].append((lat, lon, {k: v for k, v in t.items() if not k.startswith("@")}))

    # 3) здания (для входов здания места)
    bld_ids = {r["building"] for r in addr.values() if r.get("building")}
    bld = {}
    for f in read("bld.geojsonseq"):
        t = f.get("properties", {})
        key = f'{t.get("@type")}/{t.get("@id")}'
        if key in bld_ids:
            g = f["geometry"]
            rings = [g["coordinates"][0]] if g["type"] == "Polygon" else [p[0] for p in g["coordinates"]]
            bld[key] = rings

    # 4) парковки
    park = defaultdict(list)
    n = 0
    for f in read("park.geojsonseq"):
        c = center(f.get("geometry") or {})
        if not c:
            continue
        t = f.get("properties", {})
        info = {k: t[k] for k in ("fee", "parking", "access", "capacity", "name", "operator", "maxstay", "charge",
                                  "supervised", "capacity:disabled", "zone") if k in t}
        park[cell(*c)].append((c[0], c[1], info))
        n += 1
    print("парковок:", n, flush=True)

    out = {}
    for p in places:
        lat, lon, rec = p["lat"], p["lon"], {}
        if p["id"] in poi_tags and poi_tags[p["id"]]:
            rec["poi"] = poi_tags[p["id"]]
        a = addr.get(p["id"], {})
        if a.get("building") in bld:
            rings = bld[a["building"]]
            es = []
            for e in around(ent, lat, lon):
                if min(dist(e[0], e[1], y, x) for r in rings for x, y in r) < 2.5 and (e[2].get("entrance") or e[2].get("ref")):
                    es.append({"d": round(dist(lat, lon, e[0], e[1])), **{k: e[2][k] for k in ("entrance", "ref", "name", "addr:flats", "level", "access", "door") if k in e[2]}})
            if es:
                rec["building_entrances"] = sorted(es, key=lambda x: x["d"])[:8]
            rec["building_addr"] = a.get("addr")
        gates = sorted(({"d": round(dist(lat, lon, e[0], e[1])), "barrier": e[2]["barrier"],
                         **({"access": e[2]["access"]} if "access" in e[2] else {})}
                        for e in around(ent, lat, lon) if e[2].get("barrier") in ("lift_gate", "gate")
                        and dist(lat, lon, e[0], e[1]) <= 60), key=lambda x: x["d"])
        if gates:
            rec["gates"] = gates[:4]
        ps = sorted(({"d": round(dist(lat, lon, q[0], q[1])), **q[2]} for q in around(park, lat, lon)
                     if dist(lat, lon, q[0], q[1]) <= 300 and q[2].get("access") not in ("private", "no")),
                    key=lambda x: x["d"])
        if ps:
            rec["parking"] = ps[:4]
        if rec:
            out[p["id"]] = rec
    json.dump(out, open("auto/osm-access.json", "w"), ensure_ascii=False, indent=0, sort_keys=True)
    print("мест с подсказками OSM:", len(out),
          "| этаж/помещение:", sum(1 for r in out.values() if any(k in r.get("poi", {}) for k in ("level", "addr:floor", "addr:unit", "addr:door"))),
          "| входы здания:", sum(1 for r in out.values() if "building_entrances" in r),
          "| шлагбаум/ворота рядом:", sum(1 for r in out.values() if "gates" in r),
          "| парковка ≤300 м:", sum(1 for r in out.values() if "parking" in r),
          "из них с указанием платная/бесплатная:", sum(1 for r in out.values() if any("fee" in x for x in r.get("parking", []))))


if __name__ == "__main__":
    main()
