"""Робот edu 12.11 (десятый запуск): запросы OSM edu20-<N> по карточкам кандидатов → auto/osm-queries.json.
Центр — ближайшая станция метро из блока «Как добраться» карточки (радиус = расстояние + 700 м) или центр города (3,5 км);
здания фильтруются по улице, объекты — по первому слову названия."""
import json, os, re, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_batch14 import MET
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
E = json.load(open(os.path.join(ROOT, "tools/edu_1120_ext.json")))
D = {n: (a, b) for n, a, b in MET}
TOWN = {"Солнечногорск": (56.1850, 36.9770), "Фрязино": (55.9600, 38.0450), "Лыткарино": (55.5780, 37.9050), "Реутов": (55.7600, 37.8600),
        "Лобня": (56.0120, 37.4800), "Зеленоград": (55.9900, 37.2000), "Островцы": (55.5920, 37.9850)}
KW = r"(ул\.|улица|пр-т|просп\.|проспект|ш\.|шоссе|пер\.|бул\.|бульвар|наб\.|пр\.|проезд|микрорайон)"
NAME = {}  # ручные подсказки названия для поиска объекта OSM
def core(st):
    return re.sub(r"\s*\b(ул\.|улица|пр-т|просп\.|проспект|ш\.|шоссе|пер\.|бул\.|бульвар|наб\.|пр\.|проезд)\s*", " ", st).strip().replace("ё", "е")
def near_station(n):
    f = glob.glob(os.path.join(ROOT, f"auto/pages/*-ev{n}-1120e-*.txt"))[0]
    L = [l.strip() for l in open(f).read().splitlines() if l.strip()]
    if "Как добраться" not in L: return None, None
    i = L.index("Как добраться")
    st, d = L[i + 1], L[i + 2]
    try: m = float(d.split()[0].replace(",", ".")) * (1000 if "км" in d else 1)
    except ValueError: return None, None
    return st, m
def town(a):
    return next((t for t in TOWN if t in a), None)
C = json.load(open(os.path.join(ROOT, "tools/edu_1120_broad.json")))
Q = []
for n in C:
    o = E[str(n)]
    if not o.get("addr"): continue
    a = o["addr"][0]
    st = next((p.strip() for p in a.split(",") if re.search(KW, p)), None)
    t = town(a)
    if t:
        (lat, lon), rad = TOWN[t], (5000 if t == "Зеленоград" else 3500)
    else:
        stn, dist = near_station(n)
        if stn not in D: print("нет станции", n, o["name"], stn); continue
        (lat, lon), rad = D[stn], int(min(dist, 3000)) + 700
    GEN = {"центр", "детский", "детская", "школа", "студия", "логопедический", "логопедическая", "кабинет", "развития", "ребенка",
           "городской", "психологический", "мастерская", "клуб", "семейный", "монтессори", "монтессори-центр", "гбоу", "дворец",
           "логопед", "логопед-дефектолог", "нейропсихологический", "скорочтения", "курсы", "детей", "молодежи", "молодёжи", "дом", "окц", "зао"}
    ws = [w for w in re.findall(r"[A-Za-zА-Яа-яЁё0-9\-]{3,}", o["name"]) if w.lower() not in GEN]
    nm = NAME.get(n) or (ws[0] if ws else o["name"])[:9]
    q = {"id": f"edu20-{n}", "lat": lat, "lon": lon, "radius": rad, "name": nm}
    if st:
        c = core(st); q["street"] = c.split(" ")[-1] if re.match(r"^(\d-|Больш|Мал|Стар|Нов|Верхн|Нижн)", c) else c
    Q.append(q)
Q += [{"id": "edu20-21", "lat": 55.7905, "lon": 37.4720, "radius": 1800, "name": "IQ007", "street": "Маршала Тухачевского"},
      {"id": "edu20-147", "lat": 55.6713, "lon": 37.5528, "radius": 900, "name": "Дениум", "street": "Профсоюзная"},
      {"id": "edu20-148", "lat": 55.6760, "lon": 37.5660, "radius": 1200, "name": "Букварён", "street": "Новочерёмушкинская"}]
for q in Q:
    if q["id"] in ("edu20-105", "edu20-113"): q["street"] = "Челомея"
    if q["id"] == "edu20-190": q["street"] = "Баулинская"
    if q["id"] == "edu20-0": q["name"] = "Академия речи"
    if q["id"] == "edu20-1": q["name"] = "IQ007"
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith(("edu20-",))]
    json.dump(old + Q, open(p, "w"), ensure_ascii=False, indent=1)
    for q in Q: print(q["id"], q["name"], q.get("street"), q["radius"])
