"""Точки мест робота rare 12.11 (09:45 UTC) из справки OSM (auto/osm-answers.json, запросы rare12j-*):
1) объект OSM с тем же названием → «точно (объект: …)»; 2) иначе здание строго по адресу (улица + дом/корпус/строение) —
вход этого здания (≤ 60 м), иначе центр здания (уровень «дом», место останется скрытым до подтверждения).
python3 tools/rare_1112j_pick.py → tools/rare_1112j_points.json"""
import json, os, re, math, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rare_1112j_cands import C, C2
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ANS = json.load(open(os.path.join(ROOT, "auto", "osm-answers.json")))
NM = {"rink-solntsevo-aviatorov": "Ледовая Арена Солнцево", "rink-ld-sokolniki": "Ледовый дворец Сокольники", "rink-cska-arena": "ЦСКА Арена",
      "rink-legenda77-danilovskaya": "Легенда", "rink-montreal-butovo": "Монтреал", "rink-alyaska-nizhnelikhoborsky": "Аляска", "rink-vershina-tsaritsyno": "Вершина", "rink-snegir-arena": "Снегирь"}
Q = {c[0]: ("rare12j-" + c[0], c[2].split(", ", 1)[1] if c[2].startswith(("Москва, ", "Видное, ", "Воскресенск, ", "Мытищи, ", "Подольск, ", "Долгопрудный, ")) else c[2], NM.get(c[0])) for c in C + C2}
QK = {c[0]: "rare12k-" + c[0] for c in C2}


def hn_of(addr):
    m = re.search(r",\s*(?:вл\.?\s*)?(\d+[А-Яа-я]?(?:/\d+)?)(?:,\s*(корп|стр)\.\s*(\w+))?", addr)
    if not m:
        return None
    h = m.group(1).lower()
    if m.group(2):
        h += ("к" if m.group(2) == "корп" else "с") + m.group(3).lower()
    return h


def osm_hn(t):
    t = (t or "").lower().replace(" ", "")
    for a, b in (("корпус", "к"), ("строение", "с"), ("стр.", "с"), ("стр", "с"), ("к.", "к"), ("с.", "с")):
        t = t.replace(a, b)
    return t


def d(a, b, c, e):
    return math.hypot((a - c) * 111320, (b - e) * 111320 * math.cos(math.radians(a)))


PT, MISS = {}, []
for pid, (qid, addr, nm) in Q.items():
    if len(sys.argv) > 1 and pid not in sys.argv[1:]: continue
    v = ANS.get(QK.get(pid, qid))
    if not v:
        MISS.append((pid, "нет ответа")); continue
    hn = hn_of(addr)
    bld = next((b for b in v["buildings"] if hn and osm_hn(b.get("addr:housenumber")) == hn), None)
    got = None
    if nm:
        for p in v["pois"]:
            if nm.lower() in (p.get("name") or "").lower():
                if not p.get("addr:housenumber") or osm_hn(p["addr:housenumber"]) == (hn or "").split("с")[0].split("к")[0] or osm_hn(p["addr:housenumber"]) == hn:
                    got = (p["lat"], p["lon"], f'точно (объект: {p["osm"]} «{p.get("name")}»), OSM по названию, 12.11'); break
    if not got and bld:
        ent = [e for e in v.get("entrances", []) if d(e["lat"], e["lon"], bld["lat"], bld["lon"]) <= 60]
        if ent:
            e = min(ent, key=lambda e: d(e["lat"], e["lon"], bld["lat"], bld["lon"]))
            got = (e["lat"], e["lon"], f'точно (OpenStreetMap), вход {e["osm"]} здания {bld["osm"]} по адресу {bld.get("addr:street")}, {bld.get("addr:housenumber")}')
        else:
            got = (bld["lat"], bld["lon"], f'точно (OpenStreetMap), здание {bld["osm"]} по адресу {bld.get("addr:street")}, {bld.get("addr:housenumber")}')
    if got:
        PT[pid] = got
    else:
        MISS.append((pid, hn, sorted({osm_hn(b.get("addr:housenumber")) for b in v["buildings"]})[:30]))
json.dump(PT, open(os.path.join(ROOT, "tools", "rare_1112j_points.json"), "w"), ensure_ascii=False, indent=1)
print("точек:", len(PT), "нет:", len(MISS))
for k, v in PT.items():
    print(" ", k, v[2])
for m in MISS:
    print(" НЕТ", m)
# 12.11: Снегирь Арена — здание по «2» нашлось на другой улице (Заводское ш.) — место не добавлено.
# Точки переименованы под id мест: rink-montreal-butovo → hockey-montreal-butovo, fk-salto-nagatinskaya → salto-batut-nagatinskaya.
