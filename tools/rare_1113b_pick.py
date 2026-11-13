"""Точки мест робота rare 13.11 (04 UTC; 1113b): справка OSM (auto/osm-answers.json, rare13b-*/rare13c-*) — объект места
(ледовый дворец, спорткомплекс, ледовая арена, ТЦ по адресу). Не нашлось объекта по адресу (места НЕ добавлены): школа Дейнеги
(Балаклавский пр-т, 33 — в OSM только безымянное здание, «Чемпион» — 33А), Hockey Star (Профсоюзная, 93А — только здание),
школа Бобровой (Волоколамское ш., 88к9с3 — здание помечено детским садом), тюбинг «Горыныч», ЛА «ПСБ Патриот».
python3 tools/rare_1113b_pick.py → tools/rare_1113b_points.json"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
A = json.load(open(os.path.join(ROOT, "auto", "osm-answers.json")))
PT = {}


def obj(q, osm, what, pre="rare13b-"):
    a = A[pre + q]
    p = next(p for p in a["pois"] + a["buildings"] + a["outlines"] if p["osm"] == osm)
    return [p["lat"], p["lon"], f"точно (объект: {osm} {what}), OSM"]


PT["hockey-star-yuzhnoportovy"] = obj("hockey-star-yuzhnoportovy", "node/11435533050", "каток «Чемпион» (ice_rink), 2-й Южнопортовый пр., 2")
PT["tt-oskar-miklukho"] = obj("tt-oskar-miklukho", "way/1215606759", "ТЦ «Витязь. Место встречи», ул. Миклухо-Маклая, 27А")
PT["rink-snezhkom-stroitelny"] = obj("rink-snezhkom-stroitelny", "way/43027044", "«Центр хоккейного мастерства», Строительный пр., 7А к18")
PT["rink-lsk-zaraysk"] = obj("rink-lsk-zaraysk", "way/983818102", "«Зарайский Ледовый спортивный комплекс», ул. Академика Виноградова, 20")
PT["rink-shalimova-naro-fominsk"] = obj("rink-shalimova-naro-fominsk", "way/758897877", "«Ледовый Дворец», Профсоюзная ул., 36Б", "rare13c-")
PT["rink-kasatonova-aprelevka"] = obj("rink-kasatonova-aprelevka", "way/1121157531", "«Апрель клуб» (sports_centre), Апрелевская ул., 91А", "rare13c-")
PT["rink-bagration-mozhaisk"] = obj("rink-bagration-mozhaisk", "node/5752013227", "«Можайский Дворец спорта «Багратион»», ул. Мира, 15", "rare13c-")
json.dump(PT, open(os.path.join(ROOT, "tools", "rare_1113b_points.json"), "w"), ensure_ascii=False, indent=1)
for k, v in PT.items():
    print(k, v)
