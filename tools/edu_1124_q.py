"""Робот edu, 13.11 (четырнадцатый запуск): запросы OSM edu24-<N> по карточкам кандидатов (ключи ev<N>-1124e)."""
import json, os, re, sys, glob, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_batch14 import MET
with contextlib.redirect_stdout(io.StringIO()):
    import edu_1120_q as Q20
from edu_1124_sel import SEL
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
E = {"24:" + k: v for k, v in json.load(open(os.path.join(ROOT, "tools/edu_1124_ext.json"))).items()}
E.update({"24x:" + k: v for k, v in json.load(open(os.path.join(ROOT, "tools/edu_1124_ext2.json"))).items()})
D = {n.lower().replace("ё", "е"): (a, b) for n, a, b in MET}
TOWN = {"Одинцово": (55.6780, 37.2770), "Мытищи": (55.9116, 37.7300), "Подольск": (55.4310, 37.5450), "Балашиха": (55.7800, 37.9500)}
FIXST = {"бульвар генерала карбышева": "октябрьское поле"}
MANUAL = {"24:163": ("партизанская", 2000)}
NAME = {"dom-ras-rybalko": "РАС", "akademiya-rechi-stroginsky": "академия", "chernyak-mironovskaya": "Черняк", "zdorovy-rebenok-novatorov": "Здоровый", "popova-neuro-kommunarka": "Попов",
        "vernoe-reshenie-kravchenko": "Верное", "akademiya-rechi-zelenodolskaya": "академия", "akademiya-rechi-tukhachevskogo": "академия"}
def near_station(key):
    if key in MANUAL: return MANUAL[key]
    a, n = key.split(":")
    f = glob.glob(os.path.join(ROOT, f"auto/pages/*-{'ex' if a == '24x' else 'ev'}{n}-1124e-*.txt"))[0]
    L = [l.strip() for l in open(f).read().split("\n### ")[0].splitlines() if l.strip()]
    if "Как добраться" not in L: return None, None
    i = L.index("Как добраться")
    st, d = L[i + 1], L[i + 2]
    try: m = float(d.split()[0].replace(",", ".")) * (1000 if "км" in d else 1)
    except ValueError: return None, None
    st = st.lower().replace("ё", "е")
    return FIXST.get(st, st), m
def qid(key): a, b = key.split(":"); return f"edu{a}-{b}"
Q = []
for pid, v in SEL.items():
    o = E.get(v[0])
    if not o or not o.get("addr"): continue
    a = o["addr"][0]
    st = next((p.strip() for p in a.split(",") if re.search(Q20.KW, p)), None)
    t = next((t for t in TOWN if t in a), None)
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
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("edu24")]
    have = {x["id"] for x in old}
    json.dump(old + [q for q in Q if q["id"] not in have], open(p, "w"), ensure_ascii=False, indent=1)
    for q in Q: print(q)
