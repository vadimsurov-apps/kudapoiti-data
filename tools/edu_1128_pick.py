"""Точки мест робота edu (13.11, восемнадцатый запуск) из справки OSM auto/osm-answers.json (запросы edu31-<N>).
1) объект OSM с тем же названием и номером дома → «точно (объект: …)»; 2) иначе здание строго по адресу карточки.
Нет совпадения — место не добавляется. python3 tools/edu_1128_pick.py → tools/edu_1128_points.json"""
import json, os, re, sys, io, contextlib
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.join(ROOT, "tools"))
with contextlib.redirect_stdout(io.StringIO()):
    import edu_1125_pick as P25
    import add_edu_1121 as A21
from edu_1128_sel import SEL as SEL28, ADDR_FIX
A21.E.update({"28:" + k: v for k, v in json.load(open(os.path.join(ROOT, "tools/edu_1128_ext.json"))).items()})
A21.TOWNS = A21.TOWNS + tuple(t for t in ("Одинцово", "Видное", "Московский", "Балашиха", "Мытищи", "Краснознаменск", "Звенигород", "Дедовск", "Троицк", "Павловский Посад", "Красногорск") if t not in A21.TOWNS)
ANS = json.load(open(os.path.join(ROOT, "auto", "osm-answers.json")))
HN_FIX = {}
norm, house, osm_hn = P25.norm, P25.house, P25.osm_hn
JOBS = {}
REQ = {}
for pid, v in SEL28.items():
    JOBS[pid] = (v[0], REQ.get(pid, "edu31-" + v[0].split(":")[1]))
_pp = os.path.join(ROOT, "tools", "edu_1128_points.json")
PT, MISS = (json.load(open(_pp)) if os.path.exists(_pp) else {}), []
for pid, (key, qid) in JOBS.items():
    if pid in PT: continue
    ans = ANS.get(qid)
    if not ans:
        MISS.append((pid, "нет ответа")); continue
    addr = ADDR_FIX.get(pid) or A21.addr_how(key)[0]
    hn = HN_FIX.get(pid) or house(addr)
    if not hn:
        MISS.append((pid, "нет номера дома", addr)); continue
    got = None
    bld = next((b for b in ans["buildings"] if osm_hn(b.get("addr:housenumber")) == hn), None)
    for p in ans["pois"]:
        if not p.get("match"): continue
        same_hn = p.get("addr:housenumber") and osm_hn(p["addr:housenumber"]) == hn
        near = bld and abs(p["lat"] - bld["lat"]) * 111000 < 120 and abs(p["lon"] - bld["lon"]) * 63000 < 120
        if same_hn or (near and not p.get("addr:housenumber")):
            got = (p["lat"], p["lon"], f'точно (объект: {p["osm"]}), OSM по названию, 13.11'); break
    if not got and bld:
        got = (bld["lat"], bld["lon"], f'точно (OpenStreetMap), здание {bld["osm"]} по адресу {bld.get("addr:street")}, {bld.get("addr:housenumber")}')
    if got:
        PT[pid] = got
    else:
        MISS.append((pid, hn, addr, [p.get("name") for p in ans["pois"] if p.get("match")][:3], sorted({osm_hn(b.get("addr:housenumber")) for b in ans["buildings"]})[:25]))
json.dump(PT, open(_pp, "w"), ensure_ascii=False, indent=1)
if __name__ == "__main__":
    print("точек:", len(PT), "нет:", len(MISS))
    for m in MISS: print(" ", m)
    for k, v in PT.items(): print(k, v)
