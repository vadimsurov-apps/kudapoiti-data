"""Робот sections 12.11 (09 UTC): запросы OSM sec12w-* (дом по улице из адреса) → auto/osm-queries.json.
python3 tools/sections_1112w_q.py"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_batch14 import MET
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
M = {n: (a, b) for n, a, b in MET}
TOWN = {"Лобня": (56.0129, 37.4745), "Одинцово": (55.6789, 37.2636), "Реутов": (55.7604, 37.8613), "Заречье": (55.6905, 37.3988)}
# id: (центр поиска, улица (как в OSM addr:street, часть), дом, имя для сверки)
Q = {
 "molodaya-gvardiya-lobnya": ("Лобня", "Пушкина", "4", "Молодая Гвардия"),
 "smolsky-swim-novoorlovskaya": ("Новопеределкино", "Новоорловская", "7В", "Смольск"),
 "m-profi-musorgskogo": ("Отрадное", "Мусоргского", "3", "M-PROFI"),
 "karate-yasenevo-yasnogorskaya": ("Новоясеневская", "Ясногорская", "5", "Ясенево"),
 "makarov-team-odintsovo": ("Одинцово", "Маковского", "20", "Makarov"),
 "zapad-vostok-odintsovo": ("Одинцово", "Триумфальная", "14", "Запад"),
 "nikuchadze-tushinskaya": ("Тушинская", "Тушинская", "17", "Праздник"),
 "akro-miks-kastanaevskaya": ("Багратионовская", "Кастанаевская", "4", "Акро"),
 "pirouette-zarechye": ("Заречье", "Берёзовая", "1", "Pirouette"),
 "brain-sport-ostrovnaya": ("Крылатское", "Островная", "1", "Brain"),
 "sk-salto-nagatinskaya": ("Нагатинская", "Нагатинская", "16", "Сальто"),
 "yarkova-gym-fryazevskaya": ("Новогиреево", "Фрязевская", "5", "Ярков"),
 "yarkova-gym-napolny": ("Новогиреево", "Напольный", "3", "Ярков"),
 "olimp-boevye-reutov": ("Реутов", "Октября", "52", "Олимп"),
 "tkd-centr-vostok-saltykovskaya": ("Новокосино", "Салтыковская", "13Г", "Тхэквондо"),
 "zarinyan-karate-suzdalskaya": ("Новокосино", "Суздальская", "25", "карате"),
}
if __name__ == "__main__":
    out = []
    for pid, (c, st, h, nm) in Q.items():
        lat, lon = TOWN.get(c) or M[c]
        out.append({"id": "sec12w-" + pid, "lat": lat, "lon": lon, "radius": 5000, "name": nm, "street": st})
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("sec12w-")]
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(out))
