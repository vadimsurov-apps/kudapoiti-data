"""Справка из выгрузки OSM по запросам роботов/людей (09.11, Вадим: «проверь точно, какой дом, какой подъезд, сколько
входов — а не наугад»).
Вход: auto/osm-queries.json  [{"id": "<id места или метка>", "lat": .., "lon": .., "radius": 250, "name": "Muu"}, …]
Выход: auto/osm-answers.json {id: {"pois": [...], "buildings": [...], "entrances": [...]}} — объекты в радиусе:
 - pois: объекты с названием (name, тип, адрес, телефон, сайт, часы, этаж, координаты; совпадение с name — первыми);
 - buildings: здания с адресом (адрес, центр, расстояние);
 - entrances: входы/ворота/шлагбаумы (тип, номер подъезда ref, имя, координаты).
Запускается Action osm-query.yml при пуше auto/osm-queries.json."""
import json, math, os, re

def dist(a, b, c, d):
    R = 6371000; p1, p2 = math.radians(a), math.radians(c)
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(math.radians(d - b) / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))

def read(path):
    if os.path.exists(path):
        for line in open(path):
            line = line.strip().lstrip("\x1e")
            if line: yield json.loads(line)

def center(g):
    t = g.get("type"); pts = []
    if t == "Point": return g["coordinates"][1], g["coordinates"][0]
    if t == "LineString": pts = g["coordinates"]
    elif t == "Polygon": pts = g["coordinates"][0]
    elif t == "MultiPolygon": pts = [p for poly in g["coordinates"] for p in poly[0]]
    return (sum(p[1] for p in pts) / len(pts), sum(p[0] for p in pts) / len(pts)) if pts else None

KEEP = ("name", "amenity", "shop", "leisure", "tourism", "building", "addr:street", "addr:housenumber", "addr:floor",
        "level", "phone", "contact:phone", "website", "contact:website", "opening_hours", "entrance", "ref", "barrier",
        "access", "addr:flats", "description")

def norm(s): return re.sub(r"[^a-zа-я0-9]", "", (s or "").lower().replace("ё", "е"))

def main():
    qs = json.load(open("auto/osm-queries.json"))
    out = {q["id"]: {"query": q, "pois": [], "buildings": [], "entrances": []} for q in qs}
    # 12.11: сетка вместо перебора всех запросов на каждый объект (700+ запросов → прогон не укладывался в 40 мин)
    CELL = 0.02
    grid = {}
    for q in qs:
        r = q.get("radius", 250)
        dla = r / 111000 + 0.001
        dlo = r / (111000 * max(0.2, math.cos(math.radians(q["lat"])))) + 0.001
        for i in range(math.floor((q["lat"] - dla) / CELL), math.floor((q["lat"] + dla) / CELL) + 1):
            for j in range(math.floor((q["lon"] - dlo) / CELL), math.floor((q["lon"] + dlo) / CELL) + 1):
                grid.setdefault((i, j), []).append(q)
    def near(lat, lon):
        for q in grid.get((math.floor(lat / CELL), math.floor(lon / CELL)), ()):
            d = dist(q["lat"], q["lon"], lat, lon)
            if d <= q.get("radius", 250): yield q, round(d)
    srcs = [("named.geojsonseq", "pois"), ("bld.geojsonseq", "buildings"), ("entr.geojsonseq", "entrances")]
    if any(q.get("geom") for q in qs):
        srcs.append(("allbld.geojsonseq", "outlines"))
        for v in out.values(): v["outlines"] = []
    for src, key in srcs:
        for f in read(src):
            c = center(f.get("geometry") or {})
            if not c: continue
            for q, d in near(*c):
                t = f.get("properties", {})
                rec = {"d": d, "lat": round(c[0], 6), "lon": round(c[1], 6), "osm": f'{t.get("@type")}/{t.get("@id")}',
                       **{k: t[k] for k in KEEP if k in t}}
                if q.get("geom") and (f.get("geometry") or {}).get("type") in ("Polygon", "MultiPolygon", "LineString"):
                    rec["geom"] = f["geometry"]
                if key == "buildings" and q.get("street") and q["street"].lower() not in str(t.get("addr:street", "")).lower():
                    continue
                if key == "pois" and q.get("name") and norm(q["name"]) and norm(q["name"]) in norm(t.get("name")):
                    rec["match"] = True
                out[q["id"]][key].append(rec)
    for v in out.values():
        v["pois"].sort(key=lambda r: (not r.get("match"), r["d"])); v["pois"] = v["pois"][:100 if v["query"].get("geom") else 60]
        v["buildings"].sort(key=lambda r: r["d"]); v["buildings"] = v["buildings"][:120]
        v["entrances"].sort(key=lambda r: r["d"]); v["entrances"] = v["entrances"][:40]
        if "outlines" in v: v["outlines"].sort(key=lambda r: r["d"]); v["outlines"] = v["outlines"][:100]
    # 12.11 16 UTC (rare): ответ снова перевалил за 100 МБ (outlines 55 МБ) — пуш молча отклонялся с 15:56; outlines 300→100,
    # pois у geom-запросов 200→100 (ближайшие объекты сохраняются).
    # 12.11 (rare): с indent=1 ответ на 700+ запросов перевалил за 100 МБ и GitHub отклонял пуш (GH001), а одной строкой
    # любые два параллельных прогона конфликтуют при git pull --rebase. Поэтому: один запрос — одна компактная строка.
    with open("auto/osm-answers.json", "w") as fo:
        fo.write("{\n" + ",\n".join(json.dumps(k, ensure_ascii=False) + ":" + json.dumps(v, ensure_ascii=False, separators=(",", ":"))
                                     for k, v in out.items()) + "\n}\n")
    print({k: (len(v["pois"]), len(v["buildings"]), len(v["entrances"])) for k, v in out.items()})

if __name__ == "__main__":
    main()
