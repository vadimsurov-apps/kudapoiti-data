"""Точки мест робота rare 13.11 (01 UTC): справка OSM (auto/osm-answers.json, rare13a-*) — объект места (ледовый дворец,
спорткомплекс, школа по названию/адресу); для секций в здании, где у базы уже есть место с точкой «вход»/«объект», — та же точка.
Не нашлось объекта/здания по адресу (места НЕ добавлены): «Шарк Скилс» и IceZubrus (Ленинградский пр-т, 39 с1 — в OSM нет),
RusVolley (Авиамоторная, 1; Ленинградское ш., 13А), «Невские медведи» (Новорогожская, 5 — в OSM только жилой дом в 440 м),
RusVolley (Ткацкая, 1) и «Невские медведи» (Рязанский пр-т, 4) — точка только по зданию/соседям, VolleyCrab (2-я Лыковская, 73А), «Арена Плей Технополис» (в OSM нет объекта).
python3 tools/rare_1113a_pick.py → tools/rare_1113a_points.json"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
A = json.load(open(os.path.join(ROOT, "auto", "osm-answers.json")))
PT = {}


def obj(q, osm, what):
    a = A["rare13a-" + q]
    p = next(p for p in a["pois"] + a["buildings"] if p["osm"] == osm)
    return [p["lat"], p["lon"], f"точно (объект: {osm} {what}), OSM"]


PT["hockey-volki-plyushchikha"] = obj("hockey-volki-plyushchikha", "way/132678407", "спорткомплекс, ул. Плющиха, 59 с11")
PT["hockey-magiya-yantar"] = obj("hockey-magiya-yantar", "relation/8041903", "«Дворец Спорта «Янтарь»», ул. Маршала Катукова, 22")
PT["hockey-snaiper-radiatorskaya"] = obj("hockey-snaiper-radiatorskaya", "node/14108259422", "«Снайпер-select», 3-я Радиаторская ул., 11")
PT["hockey-star-stroitelny"] = obj("hockey-star-stroitelny", "way/43027044", "«Центр хоккейного мастерства», Строительный пр., 7А к18")
PT["fk-volosozhar-sokolniki"] = obj("fk-volosozhar-sokolniki", "relation/12563387", "«Ледовый дворец Сокольники», Сокольнический Вал, 1Б")
PT["fk-magical-ice-nemchinovka"] = obj("fk-magical-ice-nemchinovka", "way/493757713", "ТРК «Vegas Кунцево», Хорошёвский пр., 14")
PT["fk-magical-ice-plyushchikha"] = obj("fk-magical-ice-plyushchikha", "node/10683919940", "стадион «Буревестник», ул. Плющиха, 57")
PT["volley-rusvolley-aeroporta"] = obj("volley-rusvolley-aeroporta", "way/24968357", "школа № 1287, пр. Аэропорта, 10")
PT["volley-rusvolley-planernaya"] = obj("volley-rusvolley-planernaya", "relation/8248365", "«ФОК детско-юношеской школы №101», ул. Вилиса Лациса, вл20")
PT["rink-ld-bobrova-stupino"] = obj("rink-ld-bobrova-stupino", "way/435675370", "«Ледовый дворец спорта им. В. М. Боброва», просп. Победы, вл8 с1")
PT["rink-ld-kharlamova-klin"] = obj("rink-ld-kharlamova-klin", "way/69652301", "«Ледовый дворец им. В. Харламова», ул. Карла Маркса, 99")
json.dump(PT, open(os.path.join(ROOT, "tools", "rare_1113a_points.json"), "w"), ensure_ascii=False, indent=1)
for k, v in PT.items():
    print(k, v)
