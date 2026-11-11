"""Точки мест робота creative (11.11) из справки OSM auto/osm-answers.json (запросы cr2-<id>, центр — дом по адресу из Яндекс Карт):
1) объект OSM с тем же названием (match) в 120 м → «точно (объект: node/…)»;
2) иначе здание строго по номеру дома из Яндекса (улица — фильтр запроса) → «точно (OpenStreetMap), здание way/… по адресу …».
Нет совпадения — место не добавляется. python3 tools/creative_1111_pick.py → tools/creative_1111_points.json"""
import json, os, re, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from creative_1111_sel import SEL
ANS = json.load(open(os.path.join(ROOT, "auto", "osm-answers.json")))
YA = json.load(open(os.path.join(ROOT, "tools", "creative_1111_ya.json")))   # {id: [lat, lon, «улица, дом» по Яндексу]}


def hn(t):
    t = (t or "").lower().replace("ё", "е").replace(" ", "")
    for a, b in (("строение", "с"), ("стр.", "с"), ("корпус", "к"), ("корп.", "к"), ("к.", "к")):
        t = t.replace(a, b)
    return t


PT, MISS = {}, []
for v in SEL.values():
    pid = v[0]
    a = ANS.get("cr2-" + pid)
    if not a:
        MISS.append((pid, "нет ответа")); continue
    want = hn(YA[pid][2].rsplit(", ", 1)[-1])
    got = None
    for p in a["pois"]:
        if p.get("match") and p["d"] <= 120 and (not p.get("addr:housenumber") or hn(p["addr:housenumber"]) == want):
            got = (p["lat"], p["lon"], f'точно (объект: {p["osm"]}), OSM по названию, 11.11'); break
    if not got:
        b = next((b for b in a["buildings"] if hn(b.get("addr:housenumber")) == want), None)
        if b:
            got = (b["lat"], b["lon"], f'точно (OpenStreetMap), здание {b["osm"]} по адресу {b.get("addr:street")}, {b.get("addr:housenumber")}')
    if got:
        PT[pid] = got
    else:
        MISS.append((pid, want, [hn(b.get("addr:housenumber")) for b in a["buildings"][:10]]))
json.dump(PT, open(os.path.join(ROOT, "tools", "creative_1111_points.json"), "w"), ensure_ascii=False, indent=1)
print("точек:", len(PT), "нет:", len(MISS))
for m in MISS:
    print(" ", m)
