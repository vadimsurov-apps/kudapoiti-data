"""Сверка всех мест с OpenStreetMap ЛОКАЛЬНО (без Overpass — он перегружен: 26 мест за 4 часа).
Вход: named.geojsonseq (все объекты OSM с названием в Москве и области, osmium export)
      entr.geojsonseq (входы и ворота).
Выход: auto/geocode-report.json (как у geocode.py) и auto/entrances.json (входы парков/усадеб/ТЦ)."""
import json, math, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geocode import TYPE_TAGS, tokens, sim, dist, norm

BIG = {"парк", "ботанический сад", "усадьба", "зоопарк", "кремль", "монастырь", "парк развлечений", "ферма",
       "контактный зоопарк", "пляж", "горнолыжный курорт", "железная дорога", "аквапарк"}
CELL = 0.02   # ~2 км


def read(path):
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip().lstrip("\x1e")
            if line:
                yield json.loads(line)


def rings(geom):
    t, c = geom["type"], geom["coordinates"]
    if t == "Point": return [[c]]
    if t == "LineString": return [c]
    if t == "Polygon": return c[:1]
    if t == "MultiPolygon": return [p[0] for p in c]
    return []


def centroid(geom):
    pts = [pt for r in rings(geom) for pt in r]
    if not pts: return None
    return sum(p[1] for p in pts) / len(pts), sum(p[0] for p in pts) / len(pts)


def inside(lat, lon, ring):
    x, y, ins = lon, lat, False
    for i in range(len(ring) - 1):
        (x1, y1), (x2, y2) = ring[i][:2], ring[i + 1][:2]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1 + 1e-12) + x1: ins = not ins
    return ins


def main():
    grid = {}
    objs = []
    for f in read("named.geojsonseq"):
        g = f.get("geometry")
        if not g: continue
        c = centroid(g)
        if not c: continue
        t = f.get("properties", {})
        if t.get("railway") or t.get("highway"): continue
        names = " ".join(t.get(k, "") for k in ("name", "name:ru", "alt_name", "official_name", "short_name"))
        o = {"lat": c[0], "lon": c[1], "tags": t, "names": names, "norm": set(norm(names).split()),
             "osm": f'{t.get("@type", "?")}/{t.get("@id", "?")}', "geom": g if g["type"] != "Point" else None}
        objs.append(o)
        grid.setdefault((int(c[0] / CELL), int(c[1] / CELL)), []).append(o)
    print("объектов OSM с названием:", len(objs), flush=True)

    places = json.load(open("places-all.json" if __import__("os").path.exists("places-all.json") else "places.json"))["places"]
    if os.path.exists("auto/table-coords.json"):     # сверяем от точек из таблиц, без уже применённых уточнений
        tc = json.load(open("auto/table-coords.json"))
        for p in places:
            if p["id"] in tc: p["lat"], p["lon"] = tc[p["id"]]
    out = {}
    for p in places:
        if p.get("lat") is None: continue
        best = None
        R = 4000 if p["type"][0] != "прогулка" else 2500
        cands = []
        gi, gj = int(p["lat"] / CELL), int(p["lon"] / CELL)
        for di in range(-2, 3):
            for dj in range(-4, 5):
                cands += grid.get((gi + di, gj + dj), [])
        names_to_try = [(p["name"], False)]
        aq = re.findall(r"[«\"]([^»\"]+)[»\"]", p.get("address") or "")
        if aq: names_to_try.append((aq[0], True))
        for name, via_addr in names_to_try:
            toks = tokens(name)
            if not toks: continue
            want = TYPE_TAGS.get(p["type"][0], [])
            for o in cands:
                d = dist(o["lat"], o["lon"], p["lat"], p["lon"])
                if d > R: continue
                if o["tags"].get("public_transport") == "station" and p["type"][0] != "прогулка": continue
                s = sim(name, o["names"])
                if s < 0.5: continue
                tg = o["tags"]
                tag_ok = any(k in tg and re.search(v, str(tg[k])) for k, v in want) if want and not via_addr else None
                score = s + (0.35 if tag_ok else 0) - (0.3 if want and not tag_ok else 0) - d / 20000
                if best is None or score > best["score"]:
                    best = {"score": round(score, 3), "sim": round(s, 2), "tag_ok": tag_ok, "lat": round(o["lat"], 6),
                            "lon": round(o["lon"], 6), "osm": o["osm"], "osm_name": tg.get("name"),
                            "kind": o["osm"].split("/")[0], "moved_m": round(d), "_o": o,
                            "via": ("адрес: " + name) if via_addr else None}
            if best and best["sim"] >= 0.99: break
        if not best:
            out[p["id"]] = {"status": "not-found", "src": [p["lat"], p["lon"]], "name": p["name"], "type": p["type"][0]}
            continue
        st = "high" if best["sim"] >= 0.99 and best["tag_ok"] is not False else ("medium" if best["sim"] >= 0.66 else "low")
        if best["via"] and st == "high": st = "medium"
        best["status"] = st
        o = best.pop("_o")
        best.update({"src": [p["lat"], p["lon"]], "name": p["name"], "type": p["type"][0]})
        if o["geom"] and (p["type"][0] in BIG or re.search(r"ТЦ|ТРЦ|ТРК", p.get("address") or "")):
            best["_ring"] = rings(o["geom"])
        out[p["id"]] = best

    # входы для больших территорий и ТЦ
    ents = [(f["geometry"]["coordinates"][1], f["geometry"]["coordinates"][0], f.get("properties", {}))
            for f in read("entr.geojsonseq") if f.get("geometry", {}).get("type") == "Point"]
    eg = {}
    for e in ents: eg.setdefault((int(e[0] / CELL), int(e[1] / CELL)), []).append(e)
    MET = [(n, float(a), float(b)) for n, a, b in
           re.findall(r'": \("([^"]+)", ([\d.]+), ([\d.]+)\)', open("tools/MetroStations.swift").read())]
    entrances = {}
    for pid, r in out.items():
        ring_list = r.pop("_ring", None)
        if not ring_list or r["status"] not in ("high", "medium"): continue
        pts = [pt for rg in ring_list for pt in rg]
        lat0, lon0 = r["lat"], r["lon"]
        near = []
        span = max(dist(lat0, lon0, pt[1], pt[0]) for pt in pts) + 100
        k = int(span / 2000) + 1
        gi, gj = int(lat0 / CELL), int(lon0 / CELL)
        for di in range(-k, k + 1):
            for dj in range(-2 * k, 2 * k + 1):
                for e in eg.get((gi + di, gj + dj), []):
                    tg = e[2]
                    if tg.get("access") in ("private", "no") or tg.get("entrance") in ("service", "emergency", "exit"): continue
                    # на контуре (≤ 40 м до ближайшей вершины) или внутри
                    dmin = min(dist(e[0], e[1], pt[1], pt[0]) for pt in pts[::max(1, len(pts) // 400)])
                    if dmin <= 40 or any(inside(e[0], e[1], rg) for rg in ring_list):
                        near.append(e)
        if not near: continue
        dm, mn, ma, mb = min((dist(lat0, lon0, a, b), n, a, b) for n, a, b in MET)
        def score(e):
            bonus = -600 if e[2].get("entrance") == "main" else (-150 if e[2].get("name") else 0)
            return (dist(e[0], e[1], ma, mb) if dm < 3000 else dist(e[0], e[1], lat0, lon0)) + bonus
        e = min(near, key=score)
        entrances[pid] = {"lat": round(e[0], 6), "lon": round(e[1], 6), "name": e[2].get("name") or e[2].get("ref"),
                          "kind": e[2].get("entrance") or e[2].get("barrier"), "osm": f'node/{e[2].get("@id")}',
                          "metro": mn if dm < 3000 else None, "dist_metro_m": round(dist(e[0], e[1], ma, mb)),
                          "entrances_found": len(near)}
    os.makedirs("auto", exist_ok=True)
    json.dump(out, open("auto/geocode-report.json", "w"), ensure_ascii=False, indent=0)
    json.dump(entrances, open("auto/entrances.json", "w"), ensure_ascii=False, indent=0)
    from collections import Counter
    print("Итого:", Counter(r["status"] for r in out.values()), "входов:", len(entrances))


if __name__ == "__main__":
    main()
