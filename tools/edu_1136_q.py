"""Робот edu, 14.11 (двадцать шестой запуск): запросы OSM edu42-<N> (волна 1, ключи 36:N), edu42g-<N> (36g:N), edu42i-<N> (36i:N) → auto/osm-queries.json."""
import json, os, re, sys, glob, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_batch14 import MET
with contextlib.redirect_stdout(io.StringIO()):
    import edu_1120_q as Q20
    import edu_1135_q as Q35
from edu_1136_sel import SEL, ADDR_FIX
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
TAG = {"36": ("1136e", "", "edu_1136_ext.json"), "36g": ("1136g", "g", "edu_1136_ext2.json"), "36i": ("1136i", "i", "edu_1136_ext3.json")}
E = {}
for w, (tag, suf, fn) in TAG.items():
    p = os.path.join(ROOT, "tools", fn)
    if os.path.exists(p): E.update({w + ":" + k: v for k, v in json.load(open(p)).items()})
D = {n.lower().replace("ё", "е"): (a, b) for n, a, b in MET}
TOWN = dict(Q35.TOWN, **{"Балашиха": (55.7960, 37.9380), "Мытищи": (55.9116, 37.7308), "Люберцы": (55.6780, 37.8930), "Сергиев Посад": (56.3150, 38.1350),
        "Ногинск": (55.8530, 38.4400), "Наро-Фоминск": (55.3860, 36.7330), "Щёлково": (55.9200, 37.9900), "Пушкино": (56.0110, 37.8470)})
def near_station(key):
    w, n = key.split(":")
    f = glob.glob(os.path.join(ROOT, f"auto/pages/*-ev{n}-{TAG[w][0]}-*.txt"))[0]
    L = [l.strip() for l in open(f).read().split("\n### ")[0].splitlines() if l.strip()]
    if "Как добраться" not in L: return None, None
    i = L.index("Как добраться"); st, d = L[i + 1], L[i + 2]
    try: m = float(d.split()[0].replace(",", ".")) * (1000 if "км" in d else 1)
    except ValueError: return None, None
    return st.lower().replace("ё", "е"), m
MAN = {"uniqum-filimonki": (55.5560, 37.3600), "art-kaleydoskop-balashikha": (55.7960, 37.9380), "cdkrn-mozhayskoe-4": (55.7225, 37.4600), "kids-land-basmannaya-14": (55.7685, 37.6478), "alfa-kurkino": (55.8930, 37.3900)}
def qid(key): w, n = key.split(":"); return "edu42" + TAG[w][1] + "-" + n
Q, MISS = [], []
for pid, v in SEL.items():
    o = E.get(v[0])
    if not o: MISS.append((pid, "нет карточки")); continue
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
    old = [x for x in json.load(open(p)) if not x["id"].startswith("edu42")]
    json.dump(old + Q, open(p, "w"), ensure_ascii=False, indent=1)
    for q in Q: print(q)
    print("нет станции:", MISS)
