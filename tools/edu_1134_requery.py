"""Робот edu 14.11 (24-й запуск): повторная справка OSM для мест 1134 без точки — точная улица (без «ё», без «микрорайон»),
центр ближе к дому (ответ обрезается до 120 зданий) → edu40r-<id>."""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = [
 {"id": "edu40r-bayt-lyubertsy-pochtovoe-102", "lat": 55.6790, "lon": 37.9380, "radius": 3000, "name": "Байт", "street": "Почтовое"},
 {"id": "edu40r-bukhta-znaniy-novocheremushkinskaya", "lat": 55.6620, "lon": 37.5530, "radius": 1500, "name": "Бухта", "street": "Новоч"},
 {"id": "edu40r-alternativa-reutov", "lat": 55.7499, "lon": 37.8704, "radius": 1200, "name": "Альтернат", "street": "Юбилейный"},
 {"id": "edu40r-abvgdeika-reutov-chelomeya", "lat": 55.7550, "lon": 37.8650, "radius": 3000, "name": "АБВГДейка", "street": "Челомея"},
 {"id": "edu40r-ptitsa-govorun-zhukovsky", "lat": 55.5990, "lon": 38.1170, "radius": 2500, "name": "Птица Гов", "street": "Гагарина"},
 {"id": "edu40r-neposedy-mamontovka", "lat": 55.9990, "lon": 37.8200, "radius": 3500, "name": "Непоседы", "street": "Ленточка"},
 {"id": "edu40r-garmoniya-razvitiya-bratislavskaya", "lat": 55.6588, "lon": 37.7484, "radius": 900, "name": "Гармония", "street": "Братиславская"},
]
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("edu40r-")]
    json.dump(old + OUT, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(OUT))
