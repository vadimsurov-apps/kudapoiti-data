"""Робот rare 14.11 (1114e): справка OSM (rare14e-*) по кандидатам → auto/osm-queries.json. Центры — по соседним местам базы
или грубо по городу (только для поиска объекта/входа, в таблицу не идут).   python3 tools/rare_1114e_osmq.py"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q = {  # id: (lat, lon, radius, имя, улица)
 "krasny-kit": (55.9165, 37.7588, 400, "Красный", "Шараповский"),
 "tomilino-krylova": (55.6600, 37.9450, 1500, "", "Крылова"),
 "nekrasovka-ds": (55.7038, 37.9294, 250, "Некрасовка", ""),
 "psb-patriot": (55.5700, 36.8150, 3500, "Ледов", ""),
 "orion-zheldor": (55.7441, 38.0193, 600, "Орион", ""),
 "salyut-dolgoprudny": (55.9330, 37.5150, 2500, "Салют", "Ракетостроителей"),
 "molokovo-shkolnaya": (55.5660, 37.8300, 2500, "", "Школьная"),
 "aysberg-khimki": (55.8905, 37.4862, 400, "Айсберг", ""),
 "technopolis-zelenograd": (55.9900, 37.1500, 3000, "Arena", ""),
 "arena-legend-ozery": (54.8550, 38.5500, 3000, "Легенд", "Парковая"),
}
p = os.path.join(ROOT, "auto/osm-queries.json")
q = [x for x in json.load(open(p)) if not x["id"].startswith("rare14e-")]
for k, (la, lo, r, nm, st) in Q.items():
    x = {"id": "rare14e-" + k, "lat": la, "lon": lo, "radius": r, "name": nm, "geom": True}
    if st: x["street"] = st
    q.append(x)
json.dump(q, open(p, "w"), ensure_ascii=False, indent=1)
print(len(Q), len(q))
