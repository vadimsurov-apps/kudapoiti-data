"""Робот sections 13.11 (12 UTC, 1113j): запросы OSM sec13j-* (здание по улице из адреса источника, объект по названию) → auto/osm-queries.json.
python3 tools/sections_1113j_osmq.py"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q = {
 "mosrascvet-khodynsky": (55.7880, 37.5330, "Ходынский", "Mos Russ"),
 "mosrascvet-yunnatov": (55.7935, 37.5690, "Юннатов", "Mos Russ"),
 "aurum-azovskaya": (55.6476, 37.5966, "Азовская", "Аурум"),
 "shturm-azovskaya": (55.6500, 37.5900, "Азовская", "Штурм"),
 "benz-wrestling-shchuseva": (55.6990, 37.6420, "Архитектора Щусева", "Бенц"),
 "grusha-shmitovsky": (55.7550, 37.5560, "Шмитовский", "Груша"),
 "vimpelsport-shipilovskaya": (55.6215, 37.7440, "Шипиловская", "Вымпел"),
 "first-step-basket-artekovskaya": (55.6520, 37.6150, "Артековская", "Первый шаг"),
}
if __name__ == "__main__":
    out = [{"id": "sec13j-" + k, "lat": a, "lon": b, "radius": 4000, "name": nm, "street": st} for k, (a, b, st, nm) in Q.items()]
    p = os.path.join(ROOT, "auto/osm-queries.json")
    ids = {x["id"] for x in out}
    old = [x for x in json.load(open(p)) if x["id"] not in ids]
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(out))
