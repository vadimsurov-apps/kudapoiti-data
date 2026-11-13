"""Робот edu, 13.11 (шестнадцатый запуск): запросы OSM edu27-<N> по карточкам кандидатов (ключи ev<N>-1126e)."""
import json, os, re, sys, glob, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_batch14 import MET
with contextlib.redirect_stdout(io.StringIO()):
    import edu_1120_q as Q20
from edu_1126_sel import SEL
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
E = {"26:" + k: v for k, v in json.load(open(os.path.join(ROOT, "tools/edu_1126_ext.json"))).items()}
D = {n.lower().replace("ё", "е"): (a, b) for n, a, b in MET}
TOWN = {"Одинцово": (55.6780, 37.2770), "Московский": (55.6000, 37.3550), "Балашиха": (55.7480, 38.0100), "Мытищи": (55.9150, 37.7400), "Зеленоград": (55.9900, 37.2000), "посёлок Дрожжино": (55.5640, 37.6300)}
NAME = {"discovery-profsoyuznaya": "Discovery", "discovery-kozhinoy": "Discovery", "discovery-bolshaya-filevskaya": "Discovery", "kiberone-kastanaevskaya-10": "Kiber", "iq007-grad-moskovsky": "IQ007", "chudo-zelenograd-2016": "Чудо", "umka-zelenograd-354": "Умка", "akademiya-znaniy-zelenograd": "Академия", "clp-stroiteley": "лечебной", "sport-adaptive-school-korneychuka": "адаптив", "logo-neuro-yuzhnobutovskaya": "логопед", "neuropsy-izyumskaya": "ейропсихолог", "kvantum-panferova": "Quant"}
def near_station(key):
    n = key.split(":")[1]
    f = glob.glob(os.path.join(ROOT, f"auto/pages/*-ev{n}-1126e-*.txt"))[0]
    L = [l.strip() for l in open(f).read().split("\n### ")[0].splitlines() if l.strip()]
    if "Как добраться" not in L: return None, None
    i = L.index("Как добраться")
    st, d = L[i + 1], L[i + 2]
    try: m = float(d.split()[0].replace(",", ".")) * (1000 if "км" in d else 1)
    except ValueError: return None, None
    return st.lower().replace("ё", "е"), m
def qid(key): return "edu27-" + key.split(":")[1]
Q = []
for pid, v in SEL.items():
    o = E.get(v[0])
    if not o or not o.get("addr"): print("нет карточки", pid); continue
    a = o["addr"][0]
    st = next((p.strip() for p in a.split(",") if re.search(Q20.KW, p)), None)
    t = next((t for t in TOWN if a.startswith(t) or (", " + t) in a), None)
    if t:
        (lat, lon), rad = TOWN[t], 5000
    else:
        stn, dist = near_station(v[0])
        if stn not in D: print("нет станции", pid, stn); continue
        (lat, lon), rad = D[stn], int(min(dist or 1500, 3000)) + 700
    q = {"id": qid(v[0]), "lat": lat, "lon": lon, "radius": rad, "name": NAME.get(pid, o["name"][:9])}
    if st:
        c = Q20.core(st); q["street"] = c.split(" ")[-1] if re.match(r"^(\d-|Больш|Мал|Стар|Нов|Верхн|Нижн|Средн|Маршала)", c) else c
    Q.append(q)
FIXQ = {"edu27-72": {"street": "Кашёнкин"}, "edu27-133": {"street": "Панфёрова"}, "edu27-213": {"street": "Филёвская"},
        "edu27-182": {"street": "Московская"}, "edu27-122": {"lat": 55.5600, "lon": 37.6300, "radius": 2500, "street": "Южная"}}
for q in Q: q.update(FIXQ.get(q["id"], {}))
Q += [{"id": "edu27-41", "lat": 55.5422, "lon": 37.5323, "radius": 2000, "name": "логопед", "street": "Южнобутовская"},
      {"id": "edu27-65", "lat": 55.7935, "lon": 37.6125, "radius": 1300, "name": "Андрахан", "street": "Полковая"},
      {"id": "edu27-90", "lat": 55.5481, "lon": 37.55272, "radius": 1300, "name": "Талалаев", "street": "Скобелевская"}]
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("edu27")]
    have = {x["id"] for x in old}
    json.dump(old + [q for q in Q if q["id"] not in have], open(p, "w"), ensure_ascii=False, indent=1)
    for q in Q: print(q)
