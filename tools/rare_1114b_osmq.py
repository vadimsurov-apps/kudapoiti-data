"""Робот rare 14.11 (1114b): справка OSM (rare14b-*) по свежим кандидатам — катки «Зима в Москве» в парках, ледовые арены
Подмосковья, хоккей/фигурное → auto/osm-queries.json.  Координаты центра — грубо по району (только для поиска объекта по
названию в радиусе), в таблицу не идут.  python3 tools/rare_1114b_osmq.py"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q = {  # id: (lat, lon, radius, имя, улица)
 "rink-mikhalkovo": (55.8340, 37.5150, 1300, "Каток", ""),
 "rink-rechnoy": (55.8550, 37.4770, 1100, "Каток", ""),
 "rink-pionersky": (55.7350, 37.4700, 900, "Каток", ""),
 "rink-nikulino": (55.6650, 37.4800, 1000, "Каток", ""),
 "rink-ogonek": (55.5920, 37.6750, 2500, "Огон", ""),
 "rink-sosenki": (55.6180, 37.6650, 1500, "Каток", ""),
 "rink-ashkhabad": (55.6270, 37.6030, 1500, "Каток", ""),
 "rink-iskra-rostokino": (55.8370, 37.6650, 1800, "Искра", ""),
 "rink-molostovykh": (55.7720, 37.8250, 1500, "Каток", "Молостовых"),
 "strela-zhukovsky": (55.5980, 38.1180, 2500, "Стрела", "Кирова"),
 "kristall-shakhovskaya": (56.0330, 35.5050, 2500, "Кристалл", "Шамонина"),
 "meteor-chechersky": (55.5120, 37.5480, 2500, "Метеор", "Чечёрский"),
 "fetisov-domodedovo": (55.4380, 37.7650, 3000, "", "Кирова"),
 "rink-degeninskaya": (55.8650, 37.5420, 700, "", "Дегунинская"),
 "rink-dorogobuzhskaya": (55.7210, 37.4040, 700, "", "Дорогобужская"),
 "rink-matushkino": (55.9990, 37.2110, 900, "", ""),
 "rink-bitsa-ksk": (55.6380, 37.5850, 1200, "Битца", "Балаклавский"),
 "rink-nagatinsky-zaton": (55.6880, 37.6950, 1500, "Каток", ""),
 "rink-druzhba-levoberezhny": (55.8650, 37.4730, 900, "Дружба", ""),
 "fungrad-sokolniki": (55.7960, 37.6750, 1500, "Fun", ""),
 "lider-volokolamsk": (56.0300, 35.9550, 3000, "Лидер", "Рижское"),
 "fk-nakhabino-parkovaya25": (55.8336, 37.1595, 500, "", "Парковая"),
 "fk-vypolzov-7": (55.7810, 37.6290, 400, "", "Выползов"),
}
p = os.path.join(ROOT, "auto/osm-queries.json")
q = [x for x in json.load(open(p)) if not x["id"].startswith("rare14b-")]
for k, (la, lo, r, nm, st) in Q.items():
    x = {"id": "rare14b-" + k, "lat": la, "lon": lo, "radius": r, "name": nm}
    if st: x["street"] = st
    q.append(x)
json.dump(q, open(p, "w"), ensure_ascii=False, indent=1)
print(len(Q), len(q))
