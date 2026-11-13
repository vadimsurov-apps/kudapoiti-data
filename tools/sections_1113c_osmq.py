"""Робот sections 13.11 (03 UTC, 1113c): запросы OSM sec13d-* (здание по улице из адреса карточки Яндекс Карт) → auto/osm-queries.json.
python3 tools/sections_1113c_osmq.py"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q = {
 "alenichev-belyaninovo": (55.973, 37.735, "Зелёный", "Аленичев"),
 "aleksandrov-box-kirovogradskaya": (55.5977, 37.6017, "Кировоградская", "Александров"),
 "artgymnastik-stromynka": (55.791, 37.693, "Стромынка", "Арт"),
 "fc-young-9park": (55.807, 37.800, "9-я Парковая", "Young"),
 "cska-basket-aviatorov": (55.650, 37.402, "Авиаторов", "ЦСКА"),
 "polet-gym-festivalnaya": (55.858, 37.476, "Фестивальная", "Полёт"),
 "okinawa-snezhnaya": (55.852, 37.648, "Снежная", "Окинава"),
 "alatar-snezhnaya": (55.852, 37.648, "Снежная", "Alatar"),
 "zalomsky-vyatskaya": (55.800, 37.578, "Вятская", "Заломск"),
 "khaski-ordzhonikidze": (55.707, 37.596, "Орджоникидзе", "Хаски"),
 "dzyudokan-matrosskaya": (55.795, 37.705, "Матросская Тишина", "Дзюдокан"),
 "vityaz-vernadskogo86": (55.663, 37.481, "Вернадского", "Витязь"),
 "pirouette-maklaya": (55.651, 37.507, "Миклухо-Маклая", "Pirouette"),
 "grace-3mytishchinskaya": (55.817, 37.648, "3-я Мытищинская", "Grace"),
}
if __name__ == "__main__":
    out = [{"id": "sec13d-" + k, "lat": a, "lon": b, "radius": 5000, "name": nm, "street": st} for k, (a, b, st, nm) in Q.items()]
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("sec13d-")]
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(out))
