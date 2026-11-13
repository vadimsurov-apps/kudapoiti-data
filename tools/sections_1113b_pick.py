"""Точки мест робота sections 13.11 (00 UTC, 1113b): справка OSM (auto/osm-answers.json, sec13b-*/sec13c-*) — объект места,
вход здания или здание строго по адресу карточки Яндекс Карт.
python3 tools/sections_1113b_pick.py → tools/sections_1113b_points.json"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
A = json.load(open(os.path.join(ROOT, "auto", "osm-answers.json")))
PT = {}


def find(pid, osm):
    for pre in ("sec13b-", "sec13c-"):
        q = A.get(pre + pid)
        if q:
            for p in q["pois"] + q["buildings"] + q.get("entrances", []):
                if p["osm"] == osm:
                    return p
    raise KeyError(pid + " " + osm)


def bld(pid, osm, adr):
    p = find(pid, osm)
    PT[pid] = [p["lat"], p["lon"], f"по адресу: здание из OpenStreetMap {osm}", "дом", adr]


def obj(pid, osm, what):
    p = find(pid, osm)
    PT[pid] = [p["lat"], p["lon"], f"точно (объект: {osm} {what}), OSM", "объект", what]


bld("blok-mosfilmovskaya", "way/28987234", "Мосфильмовская улица 19 к2")
bld("krylya-khimki-sovkhoznaya", "way/1050974512", "Химки, Совхозная улица 15 с3")
bld("vityaz-mma-perovskaya", "way/301819343", "Перовская улица 1 с7")
bld("chg1-olofa-palme", "way/153390870", "улица Улофа Пальме 5 с1")
bld("sofia-rg-mkad73", "way/48869971", "МКАД, 73-й километр 7 (ТЦ «Арфа»)")
# Не нашлось (места не добавлены): Легион Кудо (Ленинградский пр-т, 80, корп. 1 — корпуса 1 в OSM нет), «Мос Расцвет»
# (в OSM только Ходынский б-р, 10Б, стр. 3 — не уверен, что это он), Ready Fight Club (ул. Кирова, «с24» — рядом и дом 24,
# и стадион «Арена Химки» вл24, какой именно — непонятно).
# ул. Вилиса Лациса, 26 — СК «Лазурный»: вход node/3594583870 (тот же, что у «Про.Плыть» в этом здании)
PT["grace-gym-latsisa"] = [55.861933, 37.412843, "точно (вход: OSM node/3594583870, вход СК «Лазурный» relation/8248360, ул. Вилиса Лациса, 26)",
                           "вход", "ул. Вилиса Лациса, 26 (СК «Лазурный»)"]
json.dump(PT, open(os.path.join(ROOT, "tools", "sections_1113b_points.json"), "w"), ensure_ascii=False, indent=1)
print(len(PT))
