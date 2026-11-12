"""Точки мест робота rare 12.11 (16 UTC): справка OSM (auto/osm-answers.json, rare12u-*) — объект места или здание строго по
адресу; для школ в здании, где у базы уже есть место с точкой «вход», — та же точка (то же здание OSM).
Не нашлось (места не добавлены): каток «Космолёд» (Октябрьская ул., 6, стр. 1 в OSM — в 3 км от ЦДК, а не рядом),
каток «Фаворит» (Варшавское ш., 1, стр. 1 — нет здания), «Арена Пехорка» (Парковая ул., 2А — нет здания; д. 2 — «Балашиха Арена»),
«Спартак-СпортТех» (Вилиса Лациса, вл. 26 — нет здания), «Шарк Скилс» (Ленинградский пр-т, 39, стр. 1 — нет здания).
Школа «Лёд» в Королёве — уже в базе (fk-led-korolev), не дублируем.
python3 tools/rare_1112u_pick.py → tools/rare_1112u_points.json"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
A = json.load(open(os.path.join(ROOT, "auto", "osm-answers.json")))
PT = {
 "fk-klub-lider-lefortovo": [55.74796, 37.704888, "точно (вход: node/1642862887 entrance=main ТРЦ «Город Лефортово»), OSM; та же точка, что у rink-grad-lefortovo (каток, где занимается клуб)"],
}


def obj(q, osm, what):
    p = next(p for p in A[q]["pois"] + A[q]["buildings"] if p["osm"] == osm)
    return [p["lat"], p["lon"], f"точно (объект: {osm} {what}), OSM"]


def bld(q, osm, adr):
    p = next(p for p in A[q]["buildings"] if p["osm"] == osm)
    return [p["lat"], p["lon"], f"точно (OpenStreetMap), здание {osm} по адресу {adr}"]


PT["rink-lytkarino-lsk"] = obj("rare12u-rink-lytkarino-lsk", "way/647838903", "«Ледовый спортивный комплекс \"Лыткарино\"», Советская ул., 9А")
PT["fk-ledovaya-feeriya-mytishchi"] = obj("rare12u-fk-ledovaya-feeriya-mytishchi", "way/91742617", "«Арена Мытищи», Лётная ул., 17")
PT["fk-led-mytishchi"] = obj("rare12u-fk-led-mytishchi", "way/91742617", "«Арена Мытищи», Лётная ул., 17")
PT["fk-led-balashikha"] = obj("rare12u-rink-pekhorka-arena", "way/87517195", "«Балашиха Арена», Парковая ул., 2")
PT["fk-v-ritme-sporta"] = obj("rare12u-fk-v-ritme-sporta", "way/37735427", "Ледовый дворец «Центральный», ул. Талалихина, 28 с4")
PT["hockey-red-machine-junior-opalikha"] = obj("rare12u-hockey-krasnaya-mashina-opalikha", "way/1038369401", "«Старт Арена», ул. Ахматовой, 26")
PT["hockey-star-entuziastov"] = bld("rare12u-hockey-star-entuziastov", "way/307158980", "ш. Энтузиастов, 33 (та же точка, что у figurist-vao-sporttekh)")
PT["hockeychance-magistralnaya"] = bld("rare12u-hockeychance-magistralnaya", "way/84610284", "2-я Магистральная ул., 10 с2")
json.dump(PT, open(os.path.join(ROOT, "tools", "rare_1112u_points.json"), "w"), ensure_ascii=False, indent=1)
for k, v in PT.items():
    print(k, v)
