"""Робот edu, 13.11 (двадцать первый запуск): запросы OSM edu36-<N> по карточкам кандидатов (ключи ev<N>-1131e)."""
import json, os, re, sys, glob, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_batch14 import MET
with contextlib.redirect_stdout(io.StringIO()):
    import edu_1120_q as Q20
from edu_1131_sel import SEL, ADDR_FIX
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
E = {"31:" + k: v for k, v in json.load(open(os.path.join(ROOT, "tools/edu_1131_ext.json"))).items()}
D = {n.lower().replace("ё", "е"): (a, b) for n, a, b in MET}
TOWN = {"Краснознаменск": (55.5980, 37.0390), "Монино": (55.8400, 38.1930), "Свердловский": (55.8650, 38.2050), "Тучково": (55.6030, 36.4750),
        "Солнечногорск": (56.1850, 36.9770), "Талдом": (56.7310, 37.5280), "Шатура": (55.5770, 39.5400), "Луховицы": (54.9660, 39.0250), "Дрожжино": (55.5660, 37.6350),
        "Бутово Парк": (55.5510, 37.5840), "Битца": (55.5630, 37.5820), "Зеленоград": (55.9850, 37.1800), "Коммунарка": (55.5690, 37.4870),
        "Сосенки": (55.5720, 37.4480), "Внуково": (55.6360, 37.3350), "Мосрентген": (55.6160, 37.4660), "Московский": (55.6000, 37.3520), "Химки": (55.8890, 37.4450), "Долгопрудный": (55.9380, 37.5100)}
def near_station(key):
    n = key.split(":")[1]
    f = glob.glob(os.path.join(ROOT, f"auto/pages/*-ev{n}-1131e-*.txt"))[0]
    L = [l.strip() for l in open(f).read().split("\n### ")[0].splitlines() if l.strip()]
    if "Как добраться" not in L: return None, None
    i = L.index("Как добраться")
    st, d = L[i + 1], L[i + 2]
    try: m = float(d.split()[0].replace(",", ".")) * (1000 if "км" in d else 1)
    except ValueError: return None, None
    return st.lower().replace("ё", "е"), m
MAN = {"gppc-tverskoe": (55.7650, 37.5620), "gppc-severnoe-chelobitevskoe": (55.9030, 37.5450), "gppc-lyublino": (55.6560, 37.7440),
       "gppc-chertanovo": (55.6430, 37.6060), "gppc-sokol": (55.7965, 37.5160), "dostizhenie-lugovoy": (55.6590, 37.7570), "chernyak-izyumskaya": (55.5400, 37.5550)}
def qid(key): return "edu36-" + key.split(":")[1]
Q = []
for pid, v in SEL.items():
    o = E.get(v[0])
    a = ADDR_FIX.get(pid) or o["addr"][0]
    if pid.startswith("gppc-"): from edu_1131_gppc import G; a = ADDR_FIX.get(pid) or G[pid][1]
    t = next((t for t in TOWN if t in a or ("Бутово Парк" == t and "Бутово Парк" in a)), None)
    st = next((p.strip() for p in a.split(",") if re.search(Q20.KW, p)), None)
    if t:
        (lat, lon), rad = TOWN[t], 4000
    else:
        if pid in MAN: (lat, lon), rad = MAN[pid], 2500
        else:
          stn, dist = near_station(v[0])
          if stn not in D: print("нет станции", pid, stn); continue
          (lat, lon), rad = D[stn], int(min(dist or 1500, 3000)) + 700
    q = {"id": qid(v[0]), "lat": lat, "lon": lon, "radius": rad, "name": o["name"][:9]}
    if st:
        c = Q20.core(st); q["street"] = c.split(" ")[-1] if re.match(r"^(\d-|Больш|Мал|Стар|Нов|Верхн|Нижн|Средн|Маршала|Генерала|Академика)", c) else c
    Q.append(q)
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("edu34")]
    json.dump(old + Q, open(p, "w"), ensure_ascii=False, indent=1)
    for q in Q: print(q)
