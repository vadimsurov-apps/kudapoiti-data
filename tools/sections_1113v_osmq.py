"""Робот sections 13.11 (18 UTC, 1113v): запросы OSM sec13v-* (здания по улице из адреса источника около станции,
объект по названию) → auto/osm-queries.json. python3 tools/sections_1113v_osmq.py"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_batch14 import MET
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ST = {n: (a, b) for n, a, b in MET}
ST["Химки"] = (55.8887, 37.4300)
ST["Новоподрезково"] = (55.9375, 37.3370)
# id: (станция, улица в OSM, название для совпадения)
Q = {
 "dovmont-kostromskaya": ("Бибирево", "Костромская", "Довмонт"),
 "vdokhnovenie-gym-miklukho": ("Беляево", "Миклухо-Маклая", "Вдохновение"),
 "first-step-basket-sholokhova": ("Боровское шоссе", "Шолохова", "Первый шаг"),
 "first-step-basket-fedosyino": ("Рассказовка", "Федосьино", "Первый шаг"),
 "first-step-basket-ramenki": ("Раменки", "Раменки", "Первый шаг"),
 "first-step-basket-kozhinoy": ("Багратионовская", "Василисы Кожиной", "Первый шаг"),
 "first-step-basket-myachkovsky": ("Марьино", "Мячковский", "Первый шаг"),
 "first-step-basket-krasnogo-mayaka": ("Пражская", "Красного Маяка", "Первый шаг"),
 "grizzly-judo-vnukovo": ("Аэропорт Внуково", "квартал", "Гризли"),
 "roshchin-team-ulyanina": ("Рассказовка", "Ульянина", "Roshchin"),
 "sk-nevsky-gritsevtsa": ("Рассказовка", "Грицевца", "Невского"),
 "agatsukan-9-maya": ("Химки", "9 Мая", "Агацукан"),
 "agatsukan-podrezkovo": ("Новоподрезково", "Железнодорожная", "Агацукан"),
 "specnaz21-altufyevskoe": ("Алтуфьево", "Алтуфьевское", "Спецназ"),
 "voronin-sambo-moskovsky": ("Саларьево", "Хабарова", "Я чемпион"),
 "glissada-proizvodstvennaya": ("Солнцево", "Производственная", "Глиссада"),
 "mosgimnastika-rimskogo-korsakova": ("Отрадное", "Римского-Корсакова", "Мосгимнастика"),
}
if __name__ == "__main__":
    out = []
    for k, (st, street, nm) in Q.items():
        if st not in ST: print("нет станции", st); continue
        a, b = ST[st]
        out.append({"id": "sec13v-" + k, "lat": a, "lon": b, "radius": 4000, "name": nm, "street": street})
    p = os.path.join(ROOT, "auto/osm-queries.json")
    ids = {x["id"] for x in out}
    old = [x for x in json.load(open(p)) if x["id"] not in ids]
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(out))
