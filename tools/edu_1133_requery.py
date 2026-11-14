"""Робот edu 14.11 (двадцать четвёртый запуск): повторная справка OSM для 1133-мест без точки — фильтр улицы без «ё»
(Панфёрова, Тёплый Стан, Семёновская) и центр у ближайшего по номеру дома (ответ обрезается до 120 зданий) → edu39r-<id>."""
import json, os, re, sys, io, contextlib
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.join(ROOT, "tools"))
ANS = json.load(open(os.path.join(ROOT, "auto/osm-answers.json")))
QS = {q["id"]: q for q in json.load(open(os.path.join(ROOT, "auto/osm-queries.json")))}
# pid: (запрос 1-й волны, подстрока улицы, номер дома)
R = {"kulikova-mishina": ("edu39-185", "Мишина", 26), "quantum-panferova": ("edu39-17", "Панф", 4),
     "discovery-profsoyuznaya-68": ("edu39-28", "Профсоюзная", 68), "iq007-teply-stan": ("edu39-94", "плый Стан", 5),
     "rybakov-playschool-gzhatskaya": (None, "Гжатская", 5), "discovery-shmitovsky": (None, "Шмитовский", 20),
     "filippok-panfilovtsev": (None, "Героев Панфиловцев", 18), "yamir-domodedovskaya": (None, "Домодедовская", 33),
     "kiberone-kolomna-oktyabrskoy": (None, "Октябрьской Революции", 362), "premier-shipilovskaya": (None, "Шипиловская", 40),
     "neokids-semenovskaya": (None, "Малая Сем", 5), "semitsvetik-kolomna": (None, "Дачная", 2),
     "yarkie-deti-krasnogorsk-zvereva": (None, "Зверева", 4), "smartykids-zelenograd": (None, "Юности", 2)}
with contextlib.redirect_stdout(io.StringIO()):
    import edu_1133_pick as P
OUT = []
for pid, (_, st, hn) in R.items():
    qid = P.JOBS[pid][1]; q = QS[qid]; a = ANS.get(qid, {"buildings": []})
    lat, lon, rad = q["lat"], q["lon"], q["radius"]
    best = None
    for b in a["buildings"]:
        m = re.match(r"(\d+)", b.get("addr:housenumber") or "")
        if m and st.lower() in (b.get("addr:street") or "").lower() and int(m.group(1)) % 2 == hn % 2:
            d = abs(int(m.group(1)) - hn)
            if best is None or d < best[0]: best = (d, b)
    if best and best[0] <= 30:
        lat, lon, rad = best[1]["lat"], best[1]["lon"], 350 + 25 * best[0]
    OUT.append({"id": "edu39r-" + pid, "lat": lat, "lon": lon, "radius": min(rad, 2500), "name": q["name"], "street": st})
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("edu39r-")]
    json.dump(old + OUT, open(p, "w"), ensure_ascii=False, indent=1)
    for o in OUT: print(o)
