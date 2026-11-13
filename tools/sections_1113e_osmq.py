"""Робот sections 13.11 (03 UTC, 1113e): запросы OSM sec13f-* (здание по улице из адреса карточки Яндекс Карт) → auto/osm-queries.json.
python3 tools/sections_1113c_osmq.py"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q = {
 "zolotye-zvezdochki-pyatnitskoe": (55.8455, 37.3618, "Пятницкое", "Звезд"),
 "mosrusscvet-beskudnikovsky": (55.866, 37.556, "Бескудниковский", "Russ"),
 "impuls-korchagina": (55.811, 37.650, "Павла Корчагина", "Импульс"),
 "akro-miks-chongarsky": (55.652, 37.620, "Чонгарский", "Акро"),
 "tornado-kirovogradskaya": (55.5977, 37.6017, "Кировоградская", "Торнадо"),
}
if __name__ == "__main__":
    out = [{"id": "sec13f-" + k, "lat": a, "lon": b, "radius": 5000, "name": nm, "street": st} for k, (a, b, st, nm) in Q.items()]
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("sec13f-")]
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(out))
