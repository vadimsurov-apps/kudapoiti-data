"""Точки мест робота edu (13.11, пятнадцатый запуск) из справки OSM auto/osm-answers.json (запросы edu25-*):
1) объект OSM с тем же названием и тем же номером дома (если номер у объекта есть) → «точно (объект: node/…)»;
2) иначе здание строго по адресу карточки (улица из запроса + номер дома/корпус/строение) → «точно (OpenStreetMap), здание way/…»;
нет совпадения — место не добавляется (осталось бы скрытым).
python3 tools/edu_1123_pick.py → tools/edu_1125_points.json"""
import json, os, re
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
import sys
sys.path.insert(0, os.path.join(ROOT, "tools"))
from edu_1125_sel import SEL
import add_edu_1121 as A21
A21.E.update({"25:" + k: v for k, v in json.load(open(os.path.join(ROOT, "tools/edu_1125_ext.json"))).items()})
A21.TOWNS = A21.TOWNS + ("Одинцово", "Видное")
addr_how = A21.addr_how
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import edu_1125_q as edu_1123_q
QN = {q["id"]: q["name"] for q in edu_1123_q.Q}
def qid(k):
    a, b = k.split(":")
    return f"edu25-{b}"
A = {pid: {"addr": addr_how(v[0])[0], "qid": qid(v[0]), "name": QN.get(qid(v[0]), "")} for pid, v in SEL.items()}
ANS = json.load(open(os.path.join(ROOT, "auto", "osm-answers.json")))
FIX = {}  # повторный запрос: центр у дома 32к2 (точка IQ007 в том же доме), радиус 500 м  # повторный запрос с меньшим радиусом (у первого ответа — лимит 120 зданий)


def norm(s):
    return re.sub(r"[^a-zа-я0-9]", "", (s or "").lower().replace("ё", "е"))


def house(addr):
    parts = [p.strip() for p in addr.split(",")]
    hn = None; extra = ""
    for i, p in enumerate(parts):
        if re.match(r"^\d+[А-Яа-я]?(/\d+)?([кс]\d+)?$", p.replace(" ", "")) and hn is None:
            hn = p.replace(" ", "").lower()
            for q in parts[i + 1:i + 2]:
                m = re.match(r"(корп\.|стр\.)\s*(\S+)", q)
                if m:
                    extra = ("к" if m.group(1) == "корп." else "с") + m.group(2).lower()
    return (hn or "") + extra


def osm_hn(t):
    return (t or "").lower().replace(" ", "").replace("корпус", "к").replace("строение", "с").replace("стр.", "с").replace("к.", "к")


_pp = os.path.join(ROOT, "tools", "edu_1125_points.json")
PT, MISS = (json.load(open(_pp)) if os.path.exists(_pp) else {}), []  # точки прошлого прохода (запросы edu25-*) сохраняются
for pid, a in A.items():
    if pid in PT:
        continue
    ans = ANS.get(FIX.get(pid, a["qid"]))
    if not ans:
        MISS.append((pid, "нет ответа")); continue
    hn = house(a["addr"])
    if not hn:
        MISS.append((pid, "нет номера дома в адресе")); continue
    name = norm(a.get("name") or "")
    got = None
    bld = next((b for b in ans["buildings"] if osm_hn(b.get("addr:housenumber")) == hn), None)
    for p in ans["pois"]:
        if not p.get("match"):
            continue
        same_hn = p.get("addr:housenumber") and osm_hn(p["addr:housenumber"]) == hn
        near = bld and abs(p["lat"] - bld["lat"]) * 111000 < 120 and abs(p["lon"] - bld["lon"]) * 63000 < 120
        if same_hn or (near and not p.get("addr:housenumber")):
            got = (p["lat"], p["lon"], f'точно (объект: {p["osm"]}), OSM по названию, 13.11'); break
    if not got and bld:
        got = (bld["lat"], bld["lon"], f'точно (OpenStreetMap), здание {bld["osm"]} по адресу {bld.get("addr:street")}, {bld.get("addr:housenumber")}')
    if got:
        PT[pid] = got
    else:
        MISS.append((pid, hn, [osm_hn(b.get("addr:housenumber")) for b in ans["buildings"][:12]]))
PT = {k: v for k, v in PT.items() if k in A}
json.dump(PT, open(os.path.join(ROOT, "tools", "edu_1125_points.json"), "w"), ensure_ascii=False, indent=1)
print("точек:", len(PT), "нет:", len(MISS))
for m in MISS:
    print(" ", m)
