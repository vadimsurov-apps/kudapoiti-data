"""Робот sections 13.11 (09 UTC, 1113i): запросы OSM sec13i-* (здание по улице из адреса источника, объект по названию) → auto/osm-queries.json.
python3 tools/sections_1113i_osmq.py [набор]"""
import json, os, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q1 = {
 "rg-prosport-festivalnaya": (55.8556, 37.4766, "Фестивальная", "Pro спорт"),
 "sambo-goncharov-leninsky": (55.7075, 37.5850, "Ленинский", "Самбо"),
 "kanrit-malaya-tulskaya": (55.7060, 37.6200, "Малая Тульская", "Канрит"),
 "akro-miks-gazoprovod": (55.5900, 37.6050, "Газопровод", "Акро"),
 "valset-chertanovskaya": (55.6160, 37.6000, "Чертановская", "Вальсет"),
 "mir-edinoborstv-starokachalovskaya": (55.5700, 37.5770, "Старокачаловская", "Мир единоборств"),
}
Q2 = {
 "corsair-barklaya": (55.7417, 37.5040, "Барклая", "Корсар"),
 "flamingo-club-luzhniki": (55.7150, 37.5580, "Лужнецкая", "Дружба"),
 "shingitay-khoroshevskoe": (55.7765, 37.5350, "Хорошёвское", "Сингитай"),
 "salto-style-komarova": (55.8240, 37.5980, "Академика Комарова", "Salto"),
 "rhythm-club-moskovsky": (55.6010, 37.3530, "микрорайон", "Ритм"),
 "zapad-sport-novozavodskaya": (55.7468, 37.5140, "Новозаводская", "Zapad"),
}
SETS = {"1": Q1, "2": Q2}
if __name__ == "__main__":
    Q = SETS[sys.argv[1] if len(sys.argv) > 1 else "1"]
    out = [{"id": "sec13i-" + k, "lat": a, "lon": b, "radius": 4000, "name": nm, "street": st} for k, (a, b, st, nm) in Q.items()]
    p = os.path.join(ROOT, "auto/osm-queries.json")
    ids = {x["id"] for x in out}
    old = [x for x in json.load(open(p)) if x["id"] not in ids]
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(out))
