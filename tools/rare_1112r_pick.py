"""Точки мест робота rare 12.11 (12:47 UTC): справка OSM (auto/osm-answers.json, rare12r-*) — здание строго по адресу;
для площадок в зданиях, где у базы уже есть место с точкой «объект/вход», — та же точка (то же здание OSM).
Не нашлось: Hockey Star ул. Юных Ленинцев, 52, стр. 2 (в OSM только д. 52 — ТЦ «Высота»), «Самолёт Арена» (квартал 195 — объекта
и здания в OSM нет). python3 tools/rare_1112r_pick.py → tools/rare_1112r_points.json"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PT = {
 "hockey-star-krasnogo-mayaka": [55.605885, 37.57848, "точно (OpenStreetMap), здание way/80575125 по адресу ул. Красного Маяка, вл. 28 (каток «Маяк»; та же точка, что у sport-katok-mayak)"],
 "hockey-star-nizhnelikhoborsky": [55.848424, 37.564191, "точно (объект: node/13004572621 «Аляска арена»), OSM по названию; та же точка, что у rink-alyaska-nizhnelikhoborsky"],
 "hockey-star-aviapark": [55.789967, 37.531024, "точно (объект: relation/3789959 ТРЦ «Авиапарк»), OSM; та же точка, что у rfhockey-aviapark"],
 "hockey-star-novoyasenevsky26": [55.604433, 37.532481, "точно (OpenStreetMap), здание way/1367964348 по адресу Новоясеневский пр-т, 26 (та же точка, что у ms-tutberidze-center)"],
}
A = json.load(open(os.path.join(ROOT, "auto", "osm-answers.json")))
for pid, q, st, hn in [("hockey-star-danilovskaya", "rare12r-hockey-star-danilovskaya", "Даниловская набережная", "8А"),
                       ("hockey-chance-danilovskaya", "rare12r-hockey-chance-danilovskaya", "Даниловская набережная", "8А"),
                       ("fk-led-tenisty", "rare12r-fk-led-tenisty", "Тенистый проезд", "8 с1"),
                       ("tt-tenix-novocheremushkinskaya", "rare12r-tt-tenix-novocheremushkinskaya", "Новочерёмушкинская улица", "25")]:
    b = next(b for b in A[q]["buildings"] if b.get("addr:street") == st and b.get("addr:housenumber") == hn)
    PT[pid] = [b["lat"], b["lon"], f'точно (OpenStreetMap), здание {b["osm"]} по адресу {st}, {hn}']
json.dump(PT, open(os.path.join(ROOT, "tools", "rare_1112r_points.json"), "w"), ensure_ascii=False, indent=1)
for k, v in PT.items():
    print(k, v)
