"""Робот pools 13.11 (11 UTC), шаг 3: уточнённые справки OSM (pl21-*) для мест, у которых первая справка не нашла дом —
к следующему запуску (места и иконки для них описаны в tools/add_pools_1113k.py и tools/icons_pools_1113k.py).
python3 tools/pools_1113k_osmq2.py"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q = [
 {"id": "pl21-malenkiy-plovets-balashikha-e", "lat": 55.803, "lon": 37.975, "radius": 1800, "name": "пловец", "street": "Ленина"},
 {"id": "pl21-malenkiy-plovets-balashikha-w", "lat": 55.794, "lon": 37.905, "radius": 1800, "name": "пловец", "street": "Ленина"},
 {"id": "pl21-volna-balashikha-olgino", "lat": 55.737, "lon": 38.045, "radius": 3000, "name": "Волна", "street": "4-я"},
 {"id": "pl21-rannee-plavanie-khimki-yunnatov", "lat": 55.89765, "lon": 37.460581, "radius": 500, "name": "плавани"},
 {"id": "pl21-spn-khimki-michurina", "lat": 55.886, "lon": 37.455, "radius": 900, "name": "бассейн", "street": "Мичурина"},
 {"id": "pl21-aqua-baby-corp-podolsk", "lat": 55.4145, "lon": 37.551, "radius": 700, "name": "Baby", "street": "Серпуховская"},
 {"id": "pl21-lyagushonok-lyubertsy", "lat": 55.689227, "lon": 37.906085, "radius": 150, "name": "Лягуш"},
]
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("pl21-")]
    json.dump(old + Q, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(Q))
