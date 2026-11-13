"""Робот edu, 13.11 (семнадцатый запуск): запросы OSM edu29-<N> по карточкам кандидатов (ключи ev<N>-1127e)."""
import json, os, re, sys, glob, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_batch14 import MET
with contextlib.redirect_stdout(io.StringIO()):
    import edu_1120_q as Q20
from edu_1127_sel import SEL
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
E = {"27:" + k: v for k, v in json.load(open(os.path.join(ROOT, "tools/edu_1127_ext.json"))).items()}
D = {n.lower().replace("ё", "е"): (a, b) for n, a, b in MET}
TOWN = {"Краснознаменск": (55.5970, 37.0390), "Звенигород": (55.7290, 36.8550), "Балашиха": (55.7480, 38.0100)}
NAME = {"mostik-marfinskaya": "Мостик", "smelost-mechtat-pudovkina": "Смелость", "dom-ras-rybalko": "РАС", "akademiya-rechi-chernomorsky": "речи", "sema-zarevy": "Сёма", "iq007-volzhsky": "IQ", "logoped-v-dele-krasnoznamensk": "Логопед", "cns-neiro-zlatoustinsky": "нейропсих", "raido-budennogo": "Райдо", "amakids-kuskovskaya": "AMA", "zhiraf-zvenigorod": "Жираф", "art-kaleydoskop-balashikha": "Калейдоскоп", "eco-elli-budennogo": "Elli", "premier-musy-dzhalilya": "Премьер", "eroshka-shabolovka": "Ерошка", "medalist-dubki": "Медалист", "algoritmika-usacheva": "Алгоритм", "coddy-leninsky-15": "Coddy", "kiberone-grizodubovoy": "Kiber", "eclit-izmaylovsky": "Эклит", "mshp-izmaylovsky": "программист", "kventin-gorodskaya": "Квентин", "cyber-class-magistralnaya": "Кибер", "vse-vmeste-serp-i-molot": "Вместе"}
def near_station(key):
    n = key.split(":")[1]
    f = glob.glob(os.path.join(ROOT, f"auto/pages/*-ev{n}-1127e-*.txt"))[0]
    L = [l.strip() for l in open(f).read().split("\n### ")[0].splitlines() if l.strip()]
    if "Как добраться" not in L: return None, None
    i = L.index("Как добраться")
    st, d = L[i + 1], L[i + 2]
    try: m = float(d.split()[0].replace(",", ".")) * (1000 if "км" in d else 1)
    except ValueError: return None, None
    return st.lower().replace("ё", "е"), m
def qid(key): return "edu29-" + key.split(":")[1]
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
FIXQ = {"edu29-237": {"street": "Буд"}, "edu29-229": {"street": "Буд"}, "edu29-27": {"street": "Усач"}}
Q.append({"id": "edu29-130", "lat": 55.640, "lon": 37.605, "radius": 2500, "name": "речи", "street": "Черноморский"})
for q in Q: q.update(FIXQ.get(q["id"], {}))
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("edu29")]
    have = {x["id"] for x in old}
    json.dump(old + [q for q in Q if q["id"] not in have], open(p, "w"), ensure_ascii=False, indent=1)
    for q in Q: print(q)
