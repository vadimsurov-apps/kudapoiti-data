"""Робот sections 13.11 (1113b): запросы OSM sec13b-* (здание по улице из адреса карточки Яндекс Карт) → auto/osm-queries.json.
python3 tools/sections_1113b_osmq.py"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q = {
 "blok-mosfilmovskaya": (55.70706, 37.51607, "Мосфильмовская", "Блок"),
 "krylya-khimki-sovkhoznaya": (55.8925, 37.4400, "Совхозная", "Крылья"),
 "vityaz-mma-perovskaya": (55.7570, 37.7550, "Перовская", "Витязь"),
 "legion-kudo-sokol": (55.80556, 37.51525, "Ленинградский", "Легион"),
 "mosrusscvet-khodynsky": (55.7865, 37.534, "Ходынский", "Russ"),
 "chg1-olofa-palme": (55.72395, 37.49788, "Улофа Пальме", "гимнаст"),
 "grace-gym-latsisa": (55.85968, 37.43681, "Вилиса Лациса", "Grace"),
 "sofia-rg-mkad73": (55.85363, 37.35311, "МКАД", "Sofia"),
 "ready-fight-khimki": (55.8940, 37.4300, "Кирова", "Ready"),
}
if __name__ == "__main__":
    out = [{"id": "sec13b-" + k, "lat": a, "lon": b, "radius": 5000, "name": nm, "street": st} for k, (a, b, st, nm) in Q.items()]
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("sec13b-")]
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(out))
