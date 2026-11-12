"""Робот edu, 12.11 (двенадцатый запуск): запросы OSM edu22-<N> по карточкам новых кандидатов (ключи ev<N>-1122e / ey<N>-1122e)."""
import json, os, re, sys, glob, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_batch14 import MET
with contextlib.redirect_stdout(io.StringIO()):
    import edu_1120_q as Q20
from edu_1122_sel import SEL
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
E = {**{"22:" + k: v for k, v in json.load(open(os.path.join(ROOT, "tools/edu_1122_ext.json"))).items()}}
if os.path.exists(os.path.join(ROOT, "tools/edu_1122_ext2.json")):
    E.update({"22y:" + k: v for k, v in json.load(open(os.path.join(ROOT, "tools/edu_1122_ext2.json"))).items()})
D = {n.lower().replace("ё", "е"): (a, b) for n, a, b in MET}
TOWN = {"Дмитров": (56.3440, 37.5200), "Мытищи": (55.9116, 37.7300), "Балашиха": (55.7800, 37.9500), "Подольск": (55.4310, 37.5450)}
def near_station(key):
    a, n = key.split(":")
    f = glob.glob(os.path.join(ROOT, f"auto/pages/*-{'ey' if a.endswith('y') else 'ev'}{n}-1122e-*.txt"))[0]
    L = [l.strip() for l in open(f).read().splitlines() if l.strip()]
    if "Как добраться" not in L: return None, None
    i = L.index("Как добраться")
    st, d = L[i + 1], L[i + 2]
    try: m = float(d.split()[0].replace(",", ".")) * (1000 if "км" in d else 1)
    except ValueError: return None, None
    return st.lower().replace("ё", "е"), m
NAME = {"dom-dlya-detey-s-ras-rybalko": "РАС", "semeyny-centr-orientir-pervomayskaya": "семейный", "minakova-kosmodemyanskikh": "Минаков", "podsolnukh-balashikha": "Подсолнух", "kosmos-montessori-novorogozhskaya": "Космос", "uh-ty-kub-mikhaylova": "Куб"}
SKIPW = {"центр", "детский", "детская", "школа", "студия", "клуб", "развития", "сад", "мой", "семейный", "логоцентр", "дом", "для", "детей"}
def qid(key):
    a, n = key.split(":"); return f"edu22{'y' if a.endswith('y') else ''}-{n}"
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
        if stn == "бульвар генерала карбышева": stn = "октябрьское поле"
        if stn not in D: print("нет станции", pid, stn); continue
        (lat, lon), rad = D[stn], int(min(dist or 1500, 3000)) + 700
    ws = [w for w in re.findall(r"[A-Za-zА-Яа-яЁё0-9\-]{3,}", o["name"]) if w.lower() not in SKIPW]
    q = {"id": qid(v[0]), "lat": lat, "lon": lon, "radius": rad, "name": NAME.get(pid) or (ws[0] if ws else o["name"])[:9]}
    if st:
        c = Q20.core(st); q["street"] = c.split(" ")[-1] if re.match(r"^(\d-|Больш|Мал|Стар|Нов|Верхн|Нижн|Средн)", c) else c
    if pid == "ladushki-kuchino": q["street"] = "Смельчак"
    Q.append(q)
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith(("edu21", "edu22"))]
    have = {x["id"] for x in old}
    json.dump(old + [q for q in Q if q["id"] not in have], open(p, "w"), ensure_ascii=False, indent=1)
    for q in Q: print(q["id"], q["name"], q.get("street"), q["radius"], q["lat"], q["lon"])
