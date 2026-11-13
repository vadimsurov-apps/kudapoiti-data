"""Робот rare, 13.11 (16 UTC; 1113f): выдача Яндекс Карт по 15 районам второго круга (фигурное/настольный теннис/волейбол,
ключи rr13k*) + зимние/редкие виды по области → auto/fetch-queue.txt; справка OSM (rare13h-*) для кандидатов без точки.
python3 tools/rare_1113f_queue.py"""
import json, os, urllib.parse as u
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
AREAS = ["Арбатская", "Библиотека им.Ленина", "Боровицкая", "Вавиловская", "Варшавская", "Верхние Котлы",
         "Верхние Лихоборы", "Владыкино", "Водный стадион", "Войковская", "Волгоградский проспект", "Волжская",
         "Волоколамская", "Воробьевы горы", "Воронцовская"]
Q = ["фигурное катание для детей {} метро", "настольный теннис для детей {} метро", "волейбол для детей {} метро"]
EXTRA = ["тюбинг Московская область", "горнолыжная школа для детей Московская область", "театр зверей Московская область",
         "цирк шапито Московская область", "сквош для детей Московская область", "памп-трек Московская область",
         "каток в парке Московская область", "ледовый дворец массовое катание Московская область"]
qs = [q.format(a) for a in AREAS for q in Q] + EXTRA
fq = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?rr13k{i:03d}=1113f&text=" + u.quote(t) for i, t in enumerate(qs)]
OSMQ = [
 {"id": "rare13h-sled-chernevskaya-gorka", "lat": 55.5405, "lon": 37.5265, "radius": 1500, "name": "горк"},
]
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in fq if l not in old]) + "\n")
    p = os.path.join(ROOT, "auto/osm-queries.json")
    q = [x for x in json.load(open(p)) if not x["id"].startswith("rare13h-")]
    json.dump(q + OSMQ, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(fq), len(OSMQ))
