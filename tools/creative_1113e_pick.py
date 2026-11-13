"""Точки мест робота creative (запуск 1113e) из справки OSM auto/osm-answers.json (запросы crf-<id>, центр — здание по
адресу из Яндекс Карт, радиус 150 м).
1) объект OSM с тем же названием (match) не дальше 80 м от здания по адресу → уровень «объект»;
2) иначе здание строго по номеру дома и улице: если у его контура ровно один вход/главный вход (entrance=main|yes, не
   подъезд жилого дома) в 3 м от контура → уровень «вход» (вход здания);
3) иначе — точки нет (место останется скрытым, координаты здания из Яндекс Карт).
python3 tools/creative_1113e_pick.py → tools/creative_1113e_points.json"""
import json, math, os, re, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("KP_PART", "creative")
from add_creative_1113e import D, YLL
ANS = json.load(open(os.path.join(ROOT, "auto", "osm-answers.json")))


def dist(a, b, c, d):
    return 6371000 * 2 * math.asin(math.sqrt(math.sin(math.radians(c - a) / 2) ** 2 + math.cos(math.radians(a)) *
                                              math.cos(math.radians(c)) * math.sin(math.radians(d - b) / 2) ** 2))


def hn(t):
    t = (t or "").lower().replace("ё", "е").replace(" ", "")
    for a, b in (("строение", "с"), ("стр.", "с"), ("корпус", "к"), ("корп.", "к"), ("к.", "к")):
        t = t.replace(a, b)
    return t


def want(addr):
    a = re.sub(r"^(Москва|Пушкино|Видное|Сергиев Посад|Реутов|Жуковский),\s*", "", addr)
    m = re.match(r"([^,]+),\s*([^,]+)((?:,\s*(?:корп\.|стр\.)\s*[^,]+)*)", a)
    if not m:
        return None, None
    street = re.sub(r"\b(ул|пр|пер|наб|пл|ш|просп|бул)\.?", "", m.group(1).lower().replace("ё", "е")).strip()
    return street.split()[0] if street.split() else "", hn(m.group(2) + (m.group(3) or "").replace(",", ""))


def seg_d(lat, lon, coords):
    best = 1e9
    for (x1, y1), (x2, y2) in zip(coords, coords[1:]):
        for k in range(11):
            x = x1 + (x2 - x1) * k / 10; y = y1 + (y2 - y1) * k / 10
            best = min(best, dist(lat, lon, y, x))
    return best


def ring(g):
    t = g.get("type")
    if t == "LineString": return g["coordinates"]
    if t == "Polygon": return g["coordinates"][0]
    if t == "MultiPolygon": return g["coordinates"][0][0]
    return []


PT, MISS = {}, []
for pid, v in D.items():
    a = ANS.get("crf-" + pid)
    if not a:
        MISS.append((pid, "нет ответа")); continue
    st, w = want(v[7])
    bs = [b for b in a.get("buildings", []) if hn(b.get("addr:housenumber")) == w and st and st[:5] in (b.get("addr:street") or "").lower().replace("ё", "е")]
    got = None
    for p in a.get("pois", []):
        if p.get("match") and (not bs or min(dist(p["lat"], p["lon"], b["lat"], b["lon"]) for b in bs) <= 80):
            got = {"lat": p["lat"], "lon": p["lon"], "level": "объект", "osm": p["osm"],
                   "why": f'объект OSM «{p.get("name")}» ({p.get("amenity") or p.get("leisure") or p.get("shop") or "место"})'}
            break
    if not got and bs:
        b = bs[0]
        g = ANS.get("crg-" + pid, {})
        outl = [o for o in g.get("outlines", []) + g.get("buildings", []) + a.get("outlines", []) if o["osm"] == b["osm"] and o.get("geom")]
        coords = ring(outl[0]["geom"]) if outl else []
        if coords:
            ens = [e for e in a.get("entrances", []) + g.get("entrances", []) if e.get("entrance") in ("main", "yes") and seg_d(e["lat"], e["lon"], coords) <= 3]
            ens = list({e["osm"]: e for e in ens}.values())
            if len(ens) == 1:
                e = ens[0]
                got = {"lat": e["lat"], "lon": e["lon"], "level": "вход", "osm": e["osm"],
                       "why": f'{"главный вход (entrance=main)" if e["entrance"] == "main" else "вход (entrance=yes)"} здания {b.get("addr:street")}, {b.get("addr:housenumber")} ({b["osm"]})'}
    if got:
        PT[pid] = got
    else:
        MISS.append((pid, w, "здание найдено" if bs else "здания нет"))
json.dump(PT, open(os.path.join(ROOT, "tools", "creative_1113e_points.json"), "w"), ensure_ascii=False, indent=1)
print("точек:", len(PT), {k: v["level"] for k, v in PT.items()})
for m in MISS:
    print("  нет:", m)

if "--debug" in sys.argv:
    for pid, v in D.items():
        a = ANS.get("crf-" + pid)
        if not a: continue
        st, w = want(v[7])
        bs = [b for b in a.get("buildings", []) if hn(b.get("addr:housenumber")) == w and st and st[:5] in (b.get("addr:street") or "").lower().replace("ё", "е")]
        print("\n##", pid, v[0], "|", [ (b["osm"], b.get("building"), b["d"]) for b in bs][:3])
        print("  pois:", [(p.get("name"), p["osm"], p["d"], p.get("match")) for p in a.get("pois", [])[:8]])
        for b in bs[:1]:
            g = ANS.get("crg-" + pid, {})
            outl = [o for o in g.get("outlines", []) + g.get("buildings", []) if o["osm"] == b["osm"] and o.get("geom")]
            c = ring(outl[0]["geom"]) if outl else []
            print("  outline:", bool(c), "entr:", [(e["osm"], e.get("entrance") or e.get("barrier"), e.get("ref"), round(seg_d(e["lat"], e["lon"], c), 1) if c else None) for e in {x["osm"]: x for x in a.get("entrances", []) + g.get("entrances", [])}.values() if not c or seg_d(e["lat"], e["lon"], c) <= 4])
