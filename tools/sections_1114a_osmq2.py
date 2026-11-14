"""Робот sections 14.11 (1114a), второй круг справки OSM: филиалы сетей с сайтов (не из выдачи Яндекса) → auto/osm-queries.json.
python3 tools/sections_1114a_osmq2.py"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_batch14 import MET
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ST = {n: (a, b) for n, a, b in MET}
# slug: (lat, lon, radius, улица в OSM, название)
Q = {
 "wa-moskovskaya": (55.938, 37.510, 5000, "Московская", "Зарядка"),
 "wa-serebrova": (55.938, 37.510, 5000, "Сереброва", "Школа"),
 "wa-mayakovskogo": (55.889, 37.430, 6000, "Маяковского", "Школа"),
 "wa-planernaya": (55.889, 37.430, 8000, "Планерная", "Планерная"),
 "fortuna-krestyanskaya": (55.910, 37.736, 7000, "Крестьянская", "Фортуна"),
 "fortuna-parkovaya": (55.910, 37.736, 7000, "Парковая", "Фортуна"),
 "flamingo-pervomayskaya": (55.784, 38.445, 6000, "Первомайская", "Гимназия"),
 "nika-makhova": (55.567, 38.230, 7000, "Махова", "Ника"),
 "tochka-imenie": (55.567, 38.230, 7000, "Народное имение", "Атриум"),
 "perhod-stroiteley": (55.437, 37.766, 9000, "Строителей", "Первый ход"),
 "perhod-mezentseva": (55.437, 37.766, 9000, "Мезенцева", "Первый ход"),
 "perhod-belova": (ST["Домодедовская"][0], ST["Домодедовская"][1], 3000, "Генерала Белова", "Первый ход"),
 "progym-8marta-6b": (55.676, 37.893, 6000, "8 Марта", "Искра"),
 "acrostars-gagarina-24": (55.676, 37.893, 6000, "Гагарина", "Гимназия"),
 "futbiki-kashira": (54.834, 38.151, 6000, "Садовая", "Футбики"),
 "futbiki-voskresensk": (55.317, 38.673, 7000, "Кагана", "Школа"),
 "futbiki-stupino": (54.886, 38.078, 7000, "Победы", "Ока"),
}
if __name__ == "__main__":
    out = [{"id": "sec14a-" + k, "lat": a, "lon": b, "radius": r, "name": nm, "street": s} for k, (a, b, r, s, nm) in Q.items()]
    p = os.path.join(ROOT, "auto/osm-queries.json")
    ids = {x["id"] for x in out}
    old = [x for x in json.load(open(p)) if x["id"] not in ids]
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(out))
