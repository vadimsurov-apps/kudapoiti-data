"""Робот sections 13.11 (21 UTC, 1113s): запросы OSM sec13s-* (здания по улице из адреса источника около станции,
объект по названию) → auto/osm-queries.json. python3 tools/sections_1113s_osmq.py"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_batch14 import MET
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ST = {n: (a, b) for n, a, b in MET}
ST["Химки"] = (55.8887, 37.4300)
ST["Новоподрезково"] = (55.9375, 37.3370)
# id: (станция, улица в OSM, название для совпадения)
Q = {
 "flamingo-club-verkhnie-polya": ("Братиславская", "Верхние Поля", "Flamingo"),
 "flamingo-club-starokashirskoe": ("Каширская", "Старокаширское", "Flamingo"),
 "flamingo-club-vavilova-5": ("Ленинский проспект", "Вавилова", "Flamingo"),
 "iskusstvo-dvizheniya-tyumensky": ("Черкизовская", "Тюменский", "Искусство движения"),
 "rhythm-club-buninskaya": ("Бунинская аллея", "Бунинская", "Ритм"),
 "lime-rg-bartenevskaya": ("Улица Горчакова", "Бартеневская", "Лайм"),
 "arsenal-kids-pilyugina": ("Калужская", "Академика Пилюгина", "Арсенал"),
 "arsenal-kids-krylatskie": ("Крылатское", "Крылатские Холмы", "Арсенал"),
 "arsenal-kids-orekhovy": ("Домодедовская", "Ореховый", "Арсенал"),
 "taekwon-pro-novorossiyskaya": ("Люблино", "Новороссийская", "тхэквондо"),
 "taekwon-pro-karibia": ("Перово", "Зелёный", "Карибия"),
 "taekwon-pro-samory-mashela": ("Коньково", "Саморы Машела", "Гармония"),
}
if __name__ == "__main__":
    out = []
    for k, (st, street, nm) in Q.items():
        if st not in ST: print("нет станции", st); continue
        a, b = ST[st]
        out.append({"id": "sec13s-" + k, "lat": a, "lon": b, "radius": 4000, "name": nm, "street": street})
    p = os.path.join(ROOT, "auto/osm-queries.json")
    ids = {x["id"] for x in out}
    old = [x for x in json.load(open(p)) if x["id"] not in ids]
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(out))
