"""Робот edu, 12.11 (одиннадцатый запуск): запросы OSM edu21d-<N> по отложенным карточкам прошлого запуска (ключи ev<N>-1120e)."""
import json, os, re, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_batch14 import MET
import edu_1120_q as Q20
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
E = json.load(open(os.path.join(ROOT, "tools/edu_1120_ext.json")))
D = {n: (a, b) for n, a, b in MET}
TOWN = {**Q20.TOWN, "Реутов": (55.7600, 37.8600)}
KW = Q20.KW
NS = [1, 21, 233, 108, 182, 31, 79, 80, 82, 85, 87, 103, 105, 111, 147, 148, 150, 177, 178, 188, 205, 207, 217, 60, 40, 46, 35, 23,
      58, 129, 143, 155, 171, 197, 208, 0, 43, 138, 158, 163, 164, 89, 102, 170, 93, 187, 189, 180]
NAME = {1: "IQ007", 21: "IQ007", 233: "IQ007", 108: "IQ007", 182: "IQ007", 60: "ПослушАЙ", 40: "Келлер", 155: "ДетУм", 85: "Клёво"}
Q = []
for n in NS:
    o = E[str(n)]
    a = o["addr"][0]
    st = next((p.strip() for p in a.split(",") if re.search(KW, p)), None)
    t = next((t for t in TOWN if t in a), None)
    if t:
        (lat, lon), rad = TOWN[t], (5000 if t == "Зеленоград" else 3500)
    else:
        stn, dist = Q20.near_station(n)
        if stn not in D: print("нет станции", n, o["name"], stn); continue
        (lat, lon), rad = D[stn], int(min(dist, 3000)) + 700
    ws = [w for w in re.findall(r"[A-Za-zА-Яа-яЁё0-9\-]{3,}", o["name"]) if w.lower() not in
          {"центр", "детский", "детская", "школа", "студия", "логопедическая", "клуб", "развития", "умных", "деток", "английского", "академия", "игровой", "кабинет"}]
    nm = NAME.get(n) or (ws[0] if ws else o["name"])[:9]
    q = {"id": f"edu21d-{n}", "lat": lat, "lon": lon, "radius": rad, "name": nm}
    if st:
        c = Q20.core(st); q["street"] = c.split(" ")[-1] if re.match(r"^(\d-|Больш|Мал|Стар|Нов|Верхн|Нижн)", c) else c
    Q.append(q)
D2 = {d["n"]: d for d in []}
Q += [{"id": "edu21d-21", "lat": 55.7905, "lon": 37.4720, "radius": 1800, "name": "IQ007", "street": "Маршала Тухачевского"},
      {"id": "edu21d-147", "lat": 55.6713, "lon": 37.5528, "radius": 900, "name": "Дениум", "street": "Профсоюзная"},
      {"id": "edu21d-148", "lat": 55.6760, "lon": 37.5660, "radius": 1200, "name": "Букварён", "street": "Новочерёмушкинская"},
      {"id": "edu21d-143", "lat": 55.6713, "lon": 37.5528, "radius": 1500, "name": "Лицеист", "street": "Гарибальди"},
      {"id": "edu21d-40", "lat": 55.7413, "lon": 37.4157, "radius": 1800, "name": "Келлер", "street": "Партизанская"},
      {"id": "edu21d-35", "lat": 55.7413, "lon": 37.4157, "radius": 2000, "name": "ДокторНейро", "street": "Рублёвское"},
      {"id": "edu21d-23", "lat": 55.7735, "lon": 37.4710, "radius": 1600, "name": "Лингва", "street": "Маршала Жукова"}]
for q in Q:
    if q["id"] == "edu21d-163": q["street"] = "Молодёжная"
    if q["id"] == "edu21d-105": q["street"] = "Челомея"
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith(("edu20", "edu21d-"))]
    json.dump(old + Q, open(p, "w"), ensure_ascii=False, indent=1)
    for q in Q: print(q["id"], q["name"], q.get("street"), q["radius"])
