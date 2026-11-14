"""Точки мест робота edu (14.11, двадцать четвёртый запуск) из справки OSM auto/osm-answers.json (запросы edu40-<N>, edu40g-<N>).
1) объект OSM с тем же названием и номером дома → «точно (объект: …)»; 2) иначе здание строго по адресу карточки.
Нет совпадения — место не добавляется. python3 tools/edu_1134_pick.py → tools/edu_1134_points.json"""
import json, os, re, sys, io, contextlib
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.join(ROOT, "tools"))
with contextlib.redirect_stdout(io.StringIO()):
    import edu_1125_pick as P25
    import add_edu_1121 as A21
from edu_1134_sel import SEL as SEL29, ADDR_FIX
A21.E.update({"34:" + k: v for k, v in json.load(open(os.path.join(ROOT, "tools/edu_1134_ext.json"))).items()})
_e2 = os.path.join(ROOT, "tools/edu_1134_ext2.json")
if os.path.exists(_e2): A21.E.update({"34g:" + k: v for k, v in json.load(open(_e2)).items()})
A21.TOWNS = A21.TOWNS + tuple(t for t in ("Одинцово", "Видное", "Московский", "Балашиха", "Мытищи", "Краснознаменск", "Звенигород", "Дедовск", "Троицк", "Павловский Посад", "Красногорск", "Талдом", "Шатура", "Луховицы", "Ленинский г. о.", "Лосино-Петровский", "Щёлково", "Руза", "Подольск", "Королёв", "Люберцы", "Раменское", "Электросталь", "Химки", "Долгопрудный", "Жуковский", "Пушкино", "Реутов", "посёлок Поведники", "Люберцы") if t not in A21.TOWNS)
ANS = json.load(open(os.path.join(ROOT, "auto", "osm-answers.json")))
HN_FIX = {}
norm, house, osm_hn = P25.norm, P25.house, P25.osm_hn
JOBS = {}
REQ = {}
for pid, v in SEL29.items():
    JOBS[pid] = (v[0], ("edu40g-" if v[0].startswith("34g") else "edu40-") + v[0].split(":")[1])
_pp = os.path.join(ROOT, "tools", "edu_1134_points.json")
PT, MISS = (json.load(open(_pp)) if os.path.exists(_pp) else {}), []
def street_ok(addr, osm_street):
    w = None
    for part in addr.split(","):
        if re.search(r"(ул\.|ш\.|просп|бул\.|пер\.|наб\.|проезд)", part):
            w = [x for x in re.split(r"[ .]", part.replace("ё", "е")) if len(x) > 2 and x not in ("ул", "просп", "бул", "пер", "наб", "проезд")]
    if not w or not osm_street:
        return bool(not w)
    st = osm_street.replace("ё", "е").lower()
    return all(x.lower() in st for x in w)
for pid, (key, qid) in JOBS.items():  # точки, поправленные вручную, — в edu_1134_points.json (Солнышко: OSM-объект по названию — государственный сад №1342, взято здание 8с1)
    if pid in PT: continue
    addr = ADDR_FIX.get(pid) or A21.addr_how(key)[0]
    hn = HN_FIX.get(pid) or house(addr)
    got = None
    for q in (qid, "edu40r-" + pid):  # повторная справка edu40r
        ans = ANS.get(q)
        if not ans or got: continue
        if pid.startswith("gppc-"):
            gp = [p for p in ans["pois"] if "психолого-педагогический центр" in (p.get("name") or "").lower()]
            gp = [p for p in gp if not p.get("addr:housenumber") or osm_hn(p["addr:housenumber"]) == hn]
            if len(gp) == 1:
                p = gp[0]; got = (p["lat"], p["lon"], f'точно (объект: {p["osm"]}), OSM по названию, 14.11'); break
        if not hn: continue
        bld = next((b for b in ans["buildings"] if osm_hn(b.get("addr:housenumber")) == hn and street_ok(addr, b.get("addr:street"))), None)
        for p in ans["pois"]:
            if not p.get("match") or pid.startswith("gppc-"): continue
            same_hn = p.get("addr:housenumber") and osm_hn(p["addr:housenumber"]) == hn and street_ok(addr, p.get("addr:street"))
            near = bld and abs(p["lat"] - bld["lat"]) * 111000 < 120 and abs(p["lon"] - bld["lon"]) * 63000 < 120
            if same_hn or (near and not p.get("addr:housenumber")):
                got = (p["lat"], p["lon"], f'точно (объект: {p["osm"]}), OSM по названию, 14.11'); break
        if not got and bld:
            got = (bld["lat"], bld["lon"], f'точно (OpenStreetMap), здание {bld["osm"]} по адресу {bld.get("addr:street")}, {bld.get("addr:housenumber")}')
    if got:
        PT[pid] = got
    else:
        MISS.append((pid, hn, addr))
json.dump(PT, open(_pp, "w"), ensure_ascii=False, indent=1)
if __name__ == "__main__":
    print("точек:", len(PT), "нет:", len(MISS))
    for m in MISS: print(" ", m)
    for k, v in PT.items(): print(k, v)
