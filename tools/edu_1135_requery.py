"""Робот edu 14.11 (25-й запуск): повторная справка OSM для мест 1135 без точки (центр ближе к дому) → edu41r-<id>."""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = [
 {"id": "edu41r-dom-dlya-detey-s-ras-rybalko", "lat": 55.7955, "lon": 37.4985, "radius": 500, "name": "Дом для", "street": "Рыбалко"},
 {"id": "edu41r-moy-sadik-ideya-vertolyotchikov", "lat": 55.7040, "lon": 37.9250, "radius": 1500, "name": "ИдеЯ", "street": "Вертолётчиков"},
 {"id": "edu41r-pixel-nagatinsky-6a", "lat": 55.6800, "lon": 37.6740, "radius": 1200, "name": "Пиксель", "street": "Нагатинский"},
 {"id": "edu41r-iq007-nagatinskaya-16", "lat": 55.6830, "lon": 37.6450, "radius": 1300, "name": "IQ", "street": "Нагатинская"},
 {"id": "edu41r-kindergarden-zhulebinsky-5", "lat": 55.7000, "lon": 37.8480, "radius": 800, "name": "Киндер", "street": "Жулебинский"},
]
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("edu41r-")]
    json.dump(old + OUT, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(OUT))
