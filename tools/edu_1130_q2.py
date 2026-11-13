"""Робот edu, 13.11 (двадцатый запуск): повторная справка OSM edu35-* для мест без точки после edu34 (улицы с «ё», шире радиус)."""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q = [
 {"id": "edu35-304", "lat": 55.8205, "lon": 37.6290, "radius": 2500, "name": "психолого", "street": "Королёва"},
 {"id": "edu35-306", "lat": 55.8950, "lon": 37.5450, "radius": 3000, "name": "психолого", "street": "Дмитровское"},
 {"id": "edu35-309", "lat": 55.8000, "lon": 37.7960, "radius": 2500, "name": "психолого", "street": "Парковая"},
 {"id": "edu35-312", "lat": 55.6580, "lon": 37.7480, "radius": 2500, "name": "психолого", "street": "Кожедуба"},
 {"id": "edu35-315", "lat": 55.6780, "lon": 37.5320, "radius": 2500, "name": "психолого", "street": "Ленинский"},
 {"id": "edu35-316", "lat": 55.7600, "lon": 37.4100, "radius": 2500, "name": "психолого", "street": "Осенний"},
 {"id": "edu35-317", "lat": 55.7560, "lon": 37.4850, "radius": 2500, "name": "психолого", "street": "Филёвский"},
 {"id": "edu35-323", "lat": 55.9900, "lon": 37.2100, "radius": 3000, "name": "психолого"},
 {"id": "edu35-104", "lat": 55.7040, "lon": 37.7350, "radius": 2500, "name": "АВС", "street": "Волжский"},
 {"id": "edu35-8", "lat": 55.7060, "lon": 37.6280, "radius": 2500, "name": "Василис", "street": "Даниловская"},
 {"id": "edu35-177", "lat": 55.7430, "lon": 37.4950, "radius": 2500, "name": "Логос", "street": "Филёвская"},
 {"id": "edu35-69", "lat": 55.6590, "lon": 37.7550, "radius": 2500, "name": "Гармония", "street": "Братиславская"},
 {"id": "edu35-29", "lat": 55.6830, "lon": 37.5730, "radius": 2500, "name": "Космо", "street": "Новочерёмушкинская"},
 {"id": "edu35-184", "lat": 55.7460, "lon": 37.4900, "radius": 2500, "name": "Sun School", "street": "Филёвская"},
]
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("edu35")]
    json.dump(old + Q, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(Q))
