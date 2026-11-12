"""Робот edu, 12.11 (одиннадцатый запуск): запросы OSM edu21-<N> по карточкам новых кандидатов (ключи ev<N>-1121e) и
уточняющие edu21x-<N> (дом не попал в первые 120 зданий)."""
import json, os, re, sys, glob, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_batch14 import MET
with contextlib.redirect_stdout(io.StringIO()):
    import edu_1120_q as Q20
from edu_1121_sel import SEL
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
E = json.load(open(os.path.join(ROOT, "tools/edu_1121_ext.json")))
D = {n.lower().replace("ё", "е"): (a, b) for n, a, b in MET}
TOWN = {"Красногорск": (55.8250, 37.3300), "Истра": (55.9150, 36.8600), "Дубна": (56.7400, 37.1700), "Воскресенск": (55.3200, 38.6700),
        "Люберцы": (55.6800, 37.8930)}
def near_station(n):
    f = glob.glob(os.path.join(ROOT, f"auto/pages/*-ev{n}-1121e-*.txt"))[0]
    L = [l.strip() for l in open(f).read().splitlines() if l.strip()]
    if "Как добраться" not in L: return None, None
    i = L.index("Как добраться")
    st, d = L[i + 1], L[i + 2]
    try: m = float(d.split()[0].replace(",", ".")) * (1000 if "км" in d else 1)
    except ValueError: return None, None
    return st.lower().replace("ё", "е"), m
NAME = {24: "Академия развития", 90: "Свой", 94: "нейропсихолог", 154: "Остров", 168: "Солнечный", 141: "Сила", 177: "Ментор",
        113: "Инжинириум", 42: "Coddy", 63: "Coddy", 36: "Монтессори", 51: "Бэби", 31: "арифметик"}
Q = []
for pid, v in SEL.items():
    a_, b_ = v[0].split(":")
    if a_ != "21": continue
    n = int(b_); o = E[str(n)]; a = o["addr"][0]
    st = next((p.strip() for p in a.split(",") if re.search(Q20.KW, p)), None)
    t = next((t for t in TOWN if t in a), None)
    if t:
        (lat, lon), rad = TOWN[t], 4000
    else:
        stn, dist = near_station(n)
        if stn not in D: print("нет станции", n, o["name"], stn); continue
        (lat, lon), rad = D[stn], int(min(dist or 1500, 3000)) + 700
    ws = [w for w in re.findall(r"[A-Za-zА-Яа-яЁё0-9\\-]{3,}", o["name"]) if w.lower() not in
          {"центр", "детский", "детская", "школа", "студия", "клуб", "развития", "сад"}]
    q = {"id": f"edu21-{n}", "lat": lat, "lon": lon, "radius": rad, "name": NAME.get(n) or (ws[0] if ws else o["name"])[:9]}
    if st:
        c = Q20.core(st); q["street"] = c.split(" ")[-1] if re.match(r"^(\\d-|Больш|Мал|Стар|Нов|Верхн|Нижн)", c) else c
    Q.append(q)
for q in Q:
    if q["id"] == "edu21-31": q["street"] = "Гагарина"
    if q["id"] == "edu21-191": q["street"] = "Кагана"
Q += [{"id": "edu21x-111", "lat": 55.737954, "lon": 37.859584, "radius": 450, "name": "Космос", "street": "Новокосинская"},
      {"id": "edu21x-58", "lat": 55.682428, "lon": 37.650354, "radius": 300, "name": "Яркие", "street": "Нагатинская"}]
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith(("edu21-", "edu21x-", "edu21d-"))]
    json.dump(old + Q, open(p, "w"), ensure_ascii=False, indent=1)
    for q in Q: print(q["id"], q["name"], q.get("street"), q["radius"])
