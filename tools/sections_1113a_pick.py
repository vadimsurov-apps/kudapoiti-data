"""Точки мест робота sections 12.11 (21 UTC, 1113a): справка OSM (auto/osm-answers.json, sec13a-*) — объект места
или здание строго по адресу карточки Яндекс Карт.
Не нашлось (места не добавлены): «Воздушная гимнастика» (Восточная ул., 4А, стр. 4 — в OSM есть только стр. 1 и 3),
FD (Каширское ш., 67, стр. 16 — нет здания).
python3 tools/sections_1113a_pick.py → tools/sections_1113a_points.json"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
A = json.load(open(os.path.join(ROOT, "auto", "osm-answers.json")))
PT = {}


def bld(pid, osm, adr):
    p = next(p for p in A["sec13a-" + pid]["buildings"] if p["osm"] == osm)
    PT[pid] = [p["lat"], p["lon"], f"по адресу: здание из OpenStreetMap {osm}", "дом", adr]


def obj(pid, osm, what):
    q = A["sec13a-" + pid]
    p = next(p for p in q["pois"] + q["buildings"] if p["osm"] == osm)
    PT[pid] = [p["lat"], p["lon"], f"точно (объект: {osm} {what}), OSM", "объект", what]


bld("effekt-vidnoe", "way/105762540", "Видное, Ольховая улица 9")
bld("tsvetkov-karate-oktyabrsky", "way/445081150", "Октябрьский переулок 23")
bld("orlenok-judo-yubileyny", "way/37651282", "Королёв, Лесная улица 22")
bld("fight-zone-korolev", "way/184467721", "Королёв, Октябрьский бульвар 22")
bld("altis-tkd-korolev", "way/31649449", "Королёв, Октябрьский бульвар 10 (бассейн «Вымпел», стадион «Вымпел»)")
obj("shindo-tkd-korolev", "way/31425755", "«ШинДо», Стадионная ул., 7")
bld("jungle-korolev-grabina", "way/193152503", "Королёв, улица Грабина 8Б (ТЦ «Каньон»)")
obj("bryksina-rg-opalikha", "way/1038369401", "«Старт Арена», ул. Ахматовой, 26")
bld("attitude-koneva", "way/95406695", "улица Маршала Конева 10")
bld("chg1-khoroshevskaya", "way/882050161", "3-я Хорошёвская улица 27А")
json.dump(PT, open(os.path.join(ROOT, "tools", "sections_1113a_points.json"), "w"), ensure_ascii=False, indent=1)
print(len(PT))
