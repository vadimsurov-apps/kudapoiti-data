"""Точки мест робота creative (третий запуск 11.11–12.11) из справки OSM auto/osm-answers.json (запросы crq-<k>: центр — станция
метро из карточки, радиус 3 км, фильтр зданий по улице).
1) объект OSM с тем же названием (match) и тем же номером дома (или без номера, но ≤60 м от здания по адресу) → «точно (объект: node/…)»;
2) иначе здание строго по номеру дома → «точно (OpenStreetMap), дом по адресу …» (уровень «дом»: место скрыто, пока вход не уточнится).
python3 tools/creative_1111f_pick.py → tools/creative_1111f_points.json"""
import json, math, os, re, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from creative_1111f_data import D
ANS = json.load(open(os.path.join(ROOT, "auto", "osm-answers.json")))
CARDS = json.load(open(os.path.join(ROOT, "tools", "creative_1111f_cards.json")))


def hn(t):
    t = (t or "").lower().replace("ё", "е").replace(" ", "")
    for a, b in (("строение", "с"), ("стр.", "с"), ("корпус", "к"), ("корп.", "к"), ("к.", "к")):
        t = t.replace(a, b)
    return t


def want(addr):
    a = re.sub(r"^(Москва|Пушкино),\s*", "", addr)
    m = re.match(r"[^,]+,\s*([^,]+)((?:,\s*(?:корп\.|стр\.)\s*[^,]+)*)", a)
    return hn(m.group(1) + (m.group(2) or "").replace(",", "")) if m else None


def dist(a, b, c, d):
    return 6371000 * 2 * math.asin(math.sqrt(math.sin(math.radians(c - a) / 2) ** 2 + math.cos(math.radians(a)) *
                                              math.cos(math.radians(c)) * math.sin(math.radians(d - b) / 2) ** 2))


PT, MISS = {}, []
for k, v in D.items():
    pid = v[0]
    a = ANS.get(f"crq-{k}")
    if not a:
        MISS.append((pid, "нет ответа")); continue
    w = want(CARDS[str(k)]["addr"])
    bs = [b for b in a.get("buildings", []) if hn(b.get("addr:housenumber")) == w]
    got = None
    for p in a.get("pois", []):
        if not p.get("match"):
            continue
        if p.get("addr:housenumber"):
            ok = hn(p["addr:housenumber"]) == w
        else:
            ok = any(dist(p["lat"], p["lon"], b["lat"], b["lon"]) <= 60 for b in bs)
        if ok:
            got = (p["lat"], p["lon"], f'точно (объект: {p["osm"]}), OSM по названию «{p.get("name")}», 12.11'); break
    if not got and bs:
        b = bs[0]
        got = (b["lat"], b["lon"], f'точно (OpenStreetMap), дом по адресу {b.get("addr:street")}, {b.get("addr:housenumber")}; вход уточнит сверка')
    if got:
        PT[pid] = got
    else:
        MISS.append((pid, w, sorted({hn(b.get("addr:housenumber")) for b in a.get("buildings", [])})[:12]))
json.dump(PT, open(os.path.join(ROOT, "tools", "creative_1111f_points.json"), "w"), ensure_ascii=False, indent=1)
print("точек:", len(PT), "объект:", sum("объект" in v[2] for v in PT.values()), "нет:", len(MISS))
for m in MISS:
    print(" ", m)
