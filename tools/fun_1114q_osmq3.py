"""Робот fun 1114q: справки OSM по зданиям двух мест из поиска по районам (fun-1114q-d<N>) → auto/osm-queries.json."""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q = [{"id": "fun-1114q-d9", "lat": 55.8508, "lon": 37.4393, "radius": 1500, "name": "Галерея", "street": "Яна Райниса", "geom": False},
     {"id": "fun-1114q-d14", "lat": 55.6905, "lon": 37.5870, "radius": 1500, "name": "Музей", "street": "Шверника", "geom": False}]
if __name__ == "__main__":
    q = json.load(open(os.path.join(ROOT, "auto/osm-queries.json")))
    q = [x for x in q if x["id"] not in {y["id"] for y in Q}] + Q
    json.dump(q, open(os.path.join(ROOT, "auto/osm-queries.json"), "w"), ensure_ascii=False, indent=1)
