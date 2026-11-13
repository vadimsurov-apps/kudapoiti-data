"""Точки мест робота sections 13.11 (03 UTC, 1113c/1113e): справка OSM (auto/osm-answers.json, sec13d-*/sec13f-*) —
здание строго по адресу карточки Яндекс Карт (улица + номер дома/корпуса/строения совпадают).
python3 tools/sections_1113c_pick.py → tools/sections_1113c_points.json"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
A = json.load(open(os.path.join(ROOT, "auto", "osm-answers.json")))
PT = {}


def find(pid, osm):
    for pre in ("sec13d-", "sec13f-"):
        q = A.get(pre + pid)
        if q:
            for p in q["pois"] + q["buildings"] + q.get("entrances", []):
                if p["osm"] == osm:
                    return p
    raise KeyError(pid + " " + osm)


def bld(pid, osm, adr):
    p = find(pid, osm)
    PT[pid] = [p["lat"], p["lon"], f"по адресу: здание из OpenStreetMap {osm}", "дом", adr]


bld("fc-young-9park", "way/30131252", "9-я Парковая улица 60")
bld("okinawa-snezhnaya", "way/43420247", "Снежная улица 13 к1")
bld("alatar-snezhnaya", "way/43420247", "Снежная улица 13 к1")
bld("zalomsky-vyatskaya", "way/165814760", "Вятская улица 27 с12")
bld("khaski-ordzhonikidze", "way/111243126", "улица Орджоникидзе 11 с8")
bld("dzyudokan-matrosskaya", "way/85929967", "улица Матросская Тишина 23 с1")
bld("vityaz-vernadskogo86", "way/312258864", "проспект Вернадского 86А (ТРЦ Avenue Southwest)")
bld("grace-3mytishchinskaya", "way/140563394", "3-я Мытищинская улица 16 с3")
bld("zolotye-zvezdochki-pyatnitskoe", "way/27736489", "Пятницкое шоссе 25 к3 (школа № 1190)")
bld("impuls-korchagina", "way/52476377", "улица Павла Корчагина 17")
bld("akro-miks-chongarsky", "way/745705993", "Чонгарский бульвар 7 (ТЦ «Место встречи Ангара»)")
# Не нашлось / неоднозначно (места не добавлены): Академия Аленичева (Беляниново — в OSM нет здания по адресу),
# клуб Ю. Александрова (Кировоградская, 23, стр. 2 — строения 2 в OSM нет), «Полёт» (Фестивальная, 29 — два здания с этим
# номером, какое из них — непонятно), «Мос Расцвет» (Бескудниковский б-р, 52А) и ФК «Торнадо» (Кировоградская, 23) —
# зданий с такими номерами в OSM нет.
json.dump(PT, open(os.path.join(ROOT, "tools", "sections_1113c_points.json"), "w"), ensure_ascii=False, indent=1)
print(len(PT))
