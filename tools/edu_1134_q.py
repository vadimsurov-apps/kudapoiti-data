"""Робот edu, 14.11 (двадцать четвёртый запуск): запросы OSM edu40-<N> (волна 1, ключи 32:N) и edu40g-<N> (волна 2, 32g:N) → auto/osm-queries.json."""
import json, os, re, sys, glob, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_batch14 import MET
with contextlib.redirect_stdout(io.StringIO()):
    import edu_1120_q as Q20
from edu_1134_sel import SEL, ADDR_FIX
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
E = {"34:" + k: v for k, v in json.load(open(os.path.join(ROOT, "tools/edu_1134_ext.json"))).items()}
_e2 = os.path.join(ROOT, "tools/edu_1134_ext2.json")
if os.path.exists(_e2): E.update({"34g:" + k: v for k, v in json.load(open(_e2)).items()})
D = {n.lower().replace("ё", "е"): (a, b) for n, a, b in MET}
TOWN = {"Коммунарка": (55.5690, 37.4870), "Московский": (55.6000, 37.3520), "Химки": (55.8890, 37.4450), "Мытищи": (55.9116, 37.7308),
        "Красногорск": (55.8310, 37.3300), "Подольск": (55.4310, 37.5450), "Зеленоград": (55.9850, 37.1800), "Балашиха": (55.7960, 37.9380),
        "Королёв": (55.9160, 37.8270), "Одинцово": (55.6780, 37.2630), "Люберцы": (55.6780, 37.8930), "Раменское": (55.5670, 38.2250),
        "Щёлково": (55.9200, 37.9900), "Видное": (55.5510, 37.7080), "Долгопрудный": (55.9380, 37.5100), "Электросталь": (55.7840, 38.4450),
        "Троицк": (55.4850, 37.3050), "Пушкино": (56.0110, 37.8470), "Реутов": (55.7600, 37.8600), "Домодедово": (55.4400, 37.7700), "Коломна": (55.0900, 38.7800), "Жуковский": (55.5990, 38.1170), "Ивантеевка": (55.9710, 37.9210), "Фрязино": (55.9590, 38.0450), "Лобня": (56.0130, 37.4740), "Котельники": (55.6600, 37.8640), "Дзержинский": (55.6300, 37.8500), "Поведники": (55.9560, 37.6600)}
def near_station(key):
    w, n = key.split(":")
    f = glob.glob(os.path.join(ROOT, f"auto/pages/*-ev{n}-{'1134g' if w == '34g' else '1134e'}-*.txt"))[0]
    L = [l.strip() for l in open(f).read().split("\n### ")[0].splitlines() if l.strip()]
    if "Как добраться" not in L: return None, None
    i = L.index("Как добраться"); st, d = L[i + 1], L[i + 2]
    try: m = float(d.split()[0].replace(",", ".")) * (1000 if "км" in d else 1)
    except ValueError: return None, None
    return st.lower().replace("ё", "е"), m
MAN = {}
def qid(key): w, n = key.split(":"); return ("edu40g-" if w == "34g" else "edu40-") + n
Q, MISS = [], []
for pid, v in SEL.items():
    o = E.get(v[0])
    a = ADDR_FIX.get(pid) or o["addr"][0]
    t = next((t for t in TOWN if t in a), None)
    st = next((p.strip() for p in a.split(",") if re.search(Q20.KW, p)), None)
    if pid in MAN:
        (lat, lon), rad = MAN[pid], 2500
    elif t:
        (lat, lon), rad = TOWN[t], 6000
    else:
        stn, dist = near_station(v[0])
        if stn not in D: MISS.append((pid, stn)); continue
        (lat, lon), rad = D[stn], int(min(dist or 1500, 3000)) + 700
    q = {"id": qid(v[0]), "lat": lat, "lon": lon, "radius": rad, "name": o["name"][:9]}
    if st:
        c = Q20.core(st); q["street"] = c.split(" ")[-1] if re.match(r"^(\d-|Больш|Мал|Стар|Нов|Верхн|Нижн|Средн|Маршала|Генерала|Академика|Архитектора|Адмирала)", c) else c
    Q.append(q)
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("edu40")]
    json.dump(old + Q, open(p, "w"), ensure_ascii=False, indent=1)
    for q in Q: print(q)
    print("нет станции:", MISS)
