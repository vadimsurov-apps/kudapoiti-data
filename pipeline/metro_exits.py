"""Выходы метро Москвы для карты (Вадим 13.11: «разместим на карте все выходы из метро… крайне точными,
приблизительность исключена»).

Источник — OpenStreetMap: точки railway=subway_entrance (ставятся на сам вход/лестницу). Станция — по отношению
stop_area, в которое входит точка; иначе по имени точки; иначе ближайшая станция метро ≤ 350 м.
В metro-exits.json попадают только выходы с однозначной станцией; остальные — в auto/metro-exits-skipped.json.
Если рядом лежит mos.json (официальный набор data.mos.ru «Входы и выходы вестибюлей»), у выхода ставится
"mos": расстояние до ближайшей официальной точки в метрах.

Вход: metro.osm (osmium tags-filter -R … n/railway=subway_entrance n/railway=station,stop r/public_transport=stop_area)
"""
import json, math, re, sys, os, datetime
import xml.etree.ElementTree as ET

def dist(a, b, c, d):
    k = math.cos(math.radians((a + c) / 2))
    return math.hypot((a - c) * 111320, (b - d) * 111320 * k)

def clean(name):
    n = (name or "").strip()
    n = re.sub(r"^(станция метро|станция|метро|м\.)\s+", "", n, flags=re.I)
    return n.strip(" «»\"")

def main(src="metro.osm"):
    nodes, exits, stations, areas = {}, {}, {}, []
    for ev, el in ET.iterparse(src):
        if el.tag == "node":
            t = {x.get("k"): x.get("v") for x in el.findall("tag")}
            nid = el.get("id"); lat = float(el.get("lat")); lon = float(el.get("lon"))
            if t.get("railway") == "subway_entrance":
                exits[nid] = (lat, lon, t)
            elif t.get("railway") == "station" and (t.get("station") in ("subway", "light_rail", "monorail") or t.get("subway") == "yes"
                                                    or "МЦК" in (t.get("network") or "") or "метрополитен" in (t.get("network") or "").lower()):
                if t.get("name") and not t["name"].startswith("Москва-"):
                    stations[nid] = (lat, lon, t)
            el.clear()
        elif el.tag == "relation":
            t = {x.get("k"): x.get("v") for x in el.findall("tag")}
            if t.get("public_transport") == "stop_area":
                mem = [m.get("ref") for m in el.findall("member") if m.get("type") == "node"]
                areas.append((t, mem))
            el.clear()
    # станция и линия по stop_area
    by_area = {}
    for t, mem in areas:
        st = [stations[m] for m in mem if m in stations]
        name = clean(st[0][2].get("name") if st else t.get("name"))
        colour = (st[0][2].get("colour") if st else None) or t.get("colour")
        if not name:
            continue
        for m in mem:
            if m in exits:
                by_area.setdefault(m, []).append((name, colour))
    good, skipped = [], []
    for nid, (lat, lon, t) in sorted(exits.items(), key=lambda x: int(x[0])):
        if t.get("access") in ("no", "private") or t.get("disused") == "yes" or any(k.startswith(("disused:", "abandoned:", "construction:", "proposed:")) for k in t):
            skipped.append({"osm": nid, "lat": lat, "lon": lon, "why": "закрыт/не действует", "tags": t}); continue
        near = sorted((dist(lat, lon, s[0], s[1]), clean(s[2].get("name")), s[2].get("colour")) for s in stations.values())
        near = [x for x in near if x[0] <= 350]
        names = []; how = None
        if nid in by_area:
            names = sorted({n for n, _ in by_area[nid]}); how = "stop_area"
        elif clean(t.get("name")) and any(clean(t.get("name")).lower().replace("ё", "е") == n[1].lower().replace("ё", "е") for n in near):
            names = [clean(t.get("name"))]; how = "name"
        elif near:
            # ближайшая станция; пересадочный узел — все станции не дальше +120 м от ближайшей
            names = sorted({n[1] for n in near if n[0] <= near[0][0] + 120}); how = "near"
        if not names:
            skipped.append({"osm": nid, "lat": lat, "lon": lon, "why": "станция не определена", "tags": t}); continue
        if how != "stop_area" and (not near or near[0][0] > 350):
            skipped.append({"osm": nid, "lat": lat, "lon": lon, "why": "дальше 350 м от станции", "tags": t}); continue
        if "МЦК" in (t.get("network") or ""):
            names = [n if "МЦК" in n else n + " (МЦК)" for n in names]
        e = {"id": "n" + nid, "lat": round(lat, 7), "lon": round(lon, 7), "station": " / ".join(names), "by": how}
        ref = (t.get("ref") or "").strip()
        if ref: e["ref"] = ref
        if t.get("wheelchair") in ("yes", "no", "limited"): e["wheelchair"] = t["wheelchair"]
        if t.get("elevator") == "yes" or t.get("highway") == "elevator": e["lift"] = True
        good.append(e)
    # сверка с официальным набором, если удалось скачать
    mos = []
    if os.path.exists("mos.json"):
        try:
            for r in json.load(open("mos.json")):
                c = r.get("Cells", r)
                la, lo = c.get("Latitude_WGS84") or c.get("LatitudeWGS84"), c.get("Longitude_WGS84") or c.get("LongitudeWGS84")
                if la and lo: mos.append((float(la), float(lo), c.get("Name") or ""))
        except Exception as ex:
            print("mos.json не разобран:", ex)
    if mos:
        for e in good:
            e["mos"] = round(min(dist(e["lat"], e["lon"], m[0], m[1]) for m in mos))
    out = {"version": datetime.date.today().isoformat(), "source": "OpenStreetMap (railway=subway_entrance)",
           "mos_checked": bool(mos), "exits": good}
    json.dump(out, open("metro-exits.json", "w"), ensure_ascii=False, separators=(",", ":"))
    json.dump(skipped, open("auto/metro-exits-skipped.json", "w"), ensure_ascii=False, indent=0)
    st = {e["station"] for e in good}
    have = {x.replace(" (МЦК)", "") for e in good for x in e["station"].split(" / ")}
    none = sorted({clean(s[2].get("name")) for s in stations.values()} - have)
    json.dump({"date": out["version"], "exits": len(good), "skipped": len(skipped), "stations_without_exits": none},
              open("auto/metro-exits-report.json", "w"), ensure_ascii=False, indent=1)
    print("станции без выходов:", none)
    print(f"выходов: {len(good)}, станций: {len(st)}, станций метро в OSM: {len({clean(s[2].get('name')) for s in stations.values()})}, "
          f"с номером: {sum(1 for e in good if e.get('ref'))}, пропущено: {len(skipped)}, официальных точек: {len(mos)}")
    if mos:
        for lim in (10, 20, 40):
            print(f"  совпало с mos.ru ≤{lim} м:", sum(1 for e in good if e["mos"] <= lim))

if __name__ == "__main__":
    main(*sys.argv[1:])
