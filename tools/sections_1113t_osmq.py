"""Робот sections 13.11 (15 UTC, 1113t): запросы OSM sec13t-* (здания по улице из адреса карточки Яндекс Карт около станции района,
объект по названию) → auto/osm-queries.json. python3 tools/sections_1113t_osmq.py"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_batch14 import MET
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ST = {n: (a, b) for n, a, b in MET}
# id: (станция, улица в OSM, название для совпадения)
Q = {
 "mfteam-polyarnaya": ("Медведково", "Полярная", "Moscow Fight"),
 "upgrade-molodtsova": ("Бабушкинская", "Молодцова", "Upgrade"),
 "musa-tkd-leninsky": ("Юго-Западная", "Ленинский", "Муса"),
 "white-lotus-vernadskogo": ("Университет", "Вернадского", "Лотос"),
 "tornado-fc-kirovogradskaya": ("Южная", "Кировоградская", "Торнадо"),
 "sinitsa-dnepropetrovskaya": ("Южная", "Днепропетровская", "Синица"),
 "acroarena-novoyasenevsky": ("Ясенево", "Новоясеневский", "Акро"),
 "reguzov-tkd-novoyasenevsky": ("Ясенево", "Новоясеневский", "Регузов"),
 "yarkova-gym-aviamotornaya": ("Авиамоторная", "Авиамоторная", "Ярков"),
 "cobra-dojo-paveletskaya": ("Павелецкая", "Павелецкая", "Cobra"),
 "torpedo-boxing-vostochnaya": ("Автозаводская", "Восточная", "Торпедо"),
 "aerial-vostochnaya": ("Автозаводская", "Восточная", "Воздушная"),
 "sfera-chess-tulskaya": ("Тульская", "Малая Тульская", "Сфера"),
 "ibasket-vavilova": ("Академическая", "Вавилова", "basket"),
 "football-lab-panferova": ("Университет", "Панфёрова", "Футбол"),
 "botvinnik-kosygina": ("Воробьевы горы", "Косыгина", "Ботвинник"),
 "shakhmatoriya-rizhsky": ("Алексеевская", "Рижский", "Шахмат"),
 "bekhoev-team-borisovskie": ("Борисово", "Борисовские Пруды", "Bekhoev"),
 "soyuz-karate-altufyevskoe102": ("Алтуфьево", "Алтуфьевское", "Каратэ"),
 "soyuz-karate-altufyevskoe70": ("Алтуфьево", "Алтуфьевское", "Каратэ"),
 "tigris-altufyevskoe": ("Алтуфьево", "Алтуфьевское", "Tigris"),
 "facultet-pro-altufyevskoe": ("Алтуфьево", "Алтуфьевское", "Факультет"),
 "facultet-pro-babushkina": ("Бабушкинская", "Лётчика Бабушкина", "Факультет"),
 "chesstogo-cherepovetskaya": ("Алтуфьево", "Череповецкая", "Chess"),
 "bern-leninskaya-sloboda": ("Автозаводская", "Ленинская Слобода", "Берн"),
 "fiet-nezhinskaya": ("Славянский бульвар", "Нежинская", "Fiet"),
 "golotsutskov-lobachevskogo": ("Озёрная", "Лобачевского", "Голоцуцков"),
 "chess-zao-ozernaya": ("Озёрная", "Озёрная", "Шахмат"),
 "imperia-starobitsevskaya": ("Аннино", "Старобитцевская", "Империя"),
 "karate1-babushkina": ("Бабушкинская", "Лётчика Бабушкина", "Каратэ"),
 "novy-orion-babushkina": ("Бабушкинская", "Лётчика Бабушкина", "Орион"),
 "first-step-basket-kozhinoy": ("Багратионовская", "Василисы Кожиной", "Первый"),
 "first-step-basket-ramenki": ("Раменки", "Раменки", "Первый"),
 "sovershenstvo-bagrationovsky": ("Багратионовская", "Багратионовский", "Совершенство"),
}
if __name__ == "__main__":
    out = []
    for k, (st, street, nm) in Q.items():
        if st not in ST: print("нет станции", st); continue
        a, b = ST[st]
        out.append({"id": "sec13t-" + k, "lat": a, "lon": b, "radius": 4000, "name": nm, "street": street})
    p = os.path.join(ROOT, "auto/osm-queries.json")
    ids = {x["id"] for x in out}
    old = [x for x in json.load(open(p)) if x["id"] not in ids]
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(out))
