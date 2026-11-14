"""Робот rare 14.11 (1114d): справка OSM (rare14d-*) по кандидатам → auto/osm-queries.json. Центры — по соседним местам базы
с тем же адресом или грубо по району (только для поиска объекта/входа, в таблицу не идут).
python3 tools/rare_1114d_osmq.py [id:lat:lon:radius:имя:улица ...]"""
import json, os, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q = {  # id: (lat, lon, radius, имя, улица)
 "hurricane-tt": (55.794991, 37.593458, 400, "Харрикейн", "Сущёвский Вал"),
 "pingpoint": (55.7935, 37.5870, 700, "Ping", "Квесисская"),
 "pushkino-tt": (55.9905, 37.846, 2000, "теннис", "Холмогоры"),
 "samolet-arena": (55.555, 37.47, 3500, "Самолёт", ""),
 "soloslovo-rink": (55.699131, 37.162978, 2500, "Ледов", ""),
 "bauma-arena": (55.834111, 37.160237, 600, "Баума", "Парковая"),
 "pogranichny-4v": (54.925147, 37.467051, 2500, "Ледов", ""),
 "legenda-domodedovo": (55.431534, 37.7513399, 700, "Легенда", "Кирова"),
 "myshenskoe-squash": (54.93, 38.15, 8000, "Squash", "Озёрная"),
}
for a in sys.argv[1:]:
    k, la, lo, r, nm, st = a.split(":")
    Q[k] = (float(la), float(lo), int(r), nm, st)
p = os.path.join(ROOT, "auto/osm-queries.json")
q = [x for x in json.load(open(p)) if not x["id"].startswith("rare14d-")]
for k, (la, lo, r, nm, st) in Q.items():
    x = {"id": "rare14d-" + k, "lat": la, "lon": lo, "radius": r, "name": nm}
    if st: x["street"] = st
    q.append(x)
json.dump(q, open(p, "w"), ensure_ascii=False, indent=1)
print(len(Q), len(q))
