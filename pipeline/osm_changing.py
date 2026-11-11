"""Пеленальные столы и комнаты из OSM (Вадим 11.11: «карапузам важны тишина, прогулки на свежем воздухе, пеленальные
комнаты — будем добавлять их на карту»).
Вход: ch.geojsonseq — osmium export объектов с тегом changing_table и торговых центров (shop=mall), см. osm-local.yml.
Выход: auto/osm-changing.json
  points — все пеленальные места OSM: osm, lat, lon, name, amenity, level, where (changing_table:location), mall (ТЦ, внутри
           которого стоит точка), mall_osm;
  places — {id места: osm} — наши места, у которых сам объект OSM (то же название, ≤150 м) отмечен changing_table=yes;
           сборка ставит им «Пеленальный стол = да».
Новые места «Пеленальная комната — ТЦ …» по списку points добавляет робот fun (с проверкой и своей иконкой)."""
import json, math, os, re, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SRC = sys.argv[1] if len(sys.argv) > 1 else "ch.geojsonseq"


def norm(s):
    s = (s or "").lower().replace("ё", "е")
    return re.sub(r"[^a-zа-я0-9]+", "", s)


def dist(a, b, c, d):
    return math.hypot((a - c) * 111320, (b - d) * 111320 * math.cos(math.radians(a)))


def rings(g):
    if g["type"] == "Polygon":
        return [g["coordinates"][0]]
    if g["type"] == "MultiPolygon":
        return [p[0] for p in g["coordinates"]]
    return []


def center(g):
    if g["type"] == "Point":
        return g["coordinates"][1], g["coordinates"][0]
    pts = [p for r in rings(g) for p in r] or (g.get("coordinates") or [])
    if not pts:
        return None
    return sum(p[1] for p in pts) / len(pts), sum(p[0] for p in pts) / len(pts)


def inside(lat, lon, ring):
    c = False
    for i in range(len(ring)):
        x1, y1 = ring[i - 1]; x2, y2 = ring[i]
        if (y1 > lat) != (y2 > lat) and lon < (x2 - x1) * (lat - y1) / ((y2 - y1) or 1e-12) + x1:
            c = not c
    return c


def main():
    malls, pts = [], []
    for line in open(SRC, encoding="utf-8"):
        line = line.strip().lstrip("\x1e")
        if not line:
            continue
        f = json.loads(line)
        t, g = f.get("properties") or {}, f.get("geometry")
        if not g:
            continue
        osm = f"{t.get('@type', '')}/{t.get('@id', '')}"
        if t.get("shop") == "mall" and t.get("name") and rings(g):
            malls.append((t["name"], osm, rings(g)))
        if t.get("changing_table") in ("yes", "limited"):
            c = center(g)
            if c:
                pts.append({"osm": osm, "lat": round(c[0], 7), "lon": round(c[1], 7), "name": t.get("name"),
                            "amenity": t.get("amenity") or t.get("shop") or t.get("leisure") or t.get("tourism"),
                            "level": t.get("level") or t.get("addr:floor"), "where": t.get("changing_table:location"),
                            "fee": t.get("changing_table:fee") or t.get("fee")})
    for p in pts:
        for name, osm, rs in malls:
            if any(inside(p["lat"], p["lon"], r) for r in rs):
                p["mall"], p["mall_osm"] = name, osm
                break
    places = {}
    allp = json.load(open(os.path.join(ROOT, "places-all.json")))["places"]
    named = [p for p in pts if p.get("name")]
    for pl in allp:
        if pl.get("lat") is None:
            continue
        n = norm(pl["name"].split("(")[0])
        for p in named:
            pn = norm(p["name"])
            if pn and (pn == n or (len(pn) > 4 and pn in n)) and dist(pl["lat"], pl["lon"], p["lat"], p["lon"]) <= 150:
                places[pl["id"]] = p["osm"]; break
    out = {"points": pts, "places": places}
    json.dump(out, open(os.path.join(ROOT, "auto", "osm-changing.json"), "w"), ensure_ascii=False, indent=0)
    print(f"пеленальных мест в OSM: {len(pts)}, в ТЦ: {sum(1 for p in pts if p.get('mall'))}, совпало с нашими местами: {len(places)}")


if __name__ == "__main__":
    main()
