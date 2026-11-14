"""Пачка set_verified по местам rare 1114c: подтверждённые поля (адрес/телефон/сайт/возраст — карточка организации в Яндекс
Картах и сайт места; точка — объект OSM, где найден). Полных часов в источниках нет — не пишем.
python3 tools/rare_1114c_verify.py > batch.json"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PTS = json.load(open(os.path.join(ROOT, "tools", "rare_1114c_points.json")))
D = "проверено 2026-11-14"
YA = "карточка организации в Яндекс Картах (auto/pages)"
B = {
 "deinega-skating-bitsa": ({"address": "Москва, Балаклавский просп., 33 (КСК «Битца», ЛД «ЧемпиОн»), 1 этаж", "phone": "+7 (993) 370-02-15",
     "url": "https://deinega-team.ru/", "age_min": 4, "age_max": 17, "cats": "figureskating"},
     "deinega-team.ru (набор с 4 лет, арена ЛД «ЧемпиОн Битца»); " + YA + " «Школа фигурного катания Дейнеги Сергея»"),
 "ice-fenix-sokolniki": ({"address": "Москва, ул. Сокольнический Вал, 1Б", "phone": "+7 (926) 288-21-42", "url": "https://icefenixclub.ru/",
     "age_min": 3, "cats": "figureskating"}, YA + " «Клуб фигурного катания Ice Fenix» (группа с 3 лет)"),
 "led-noginsk": ({"address": "Ногинск, ул. Климова, 48А", "phone": "+7 (925) 110-10-60", "url": "https://na-ldu.ru/", "price_child": 2000,
     "age_min": 3, "age_max": 17, "cats": "figureskating"}, YA + " «Лёд» (Ногинск; от 3,5 лет, подростки до 17 лет, занятие 2000 ₽)"),
 "monster-hockey-bitsa": ({"address": "Москва, Балаклавский просп., 33 (КСК «Битца»)", "phone": "+7 (913) 687-01-01", "price_child": 2900,
     "age_min": 6, "age_max": 13, "cats": "hockey"}, YA + " «Монстр хоккея» (группы 2020–2018 / 2017–2013 г. р., занятие 2900 ₽)"),
 "pro-hockey-soloslovo": ({"address": "Одинцовский г. о., д. Солослово, КП «Резиденции Берёзки», 314", "phone": "+7 (909) 108-60-06",
     "url": "https://pro-hockey.ru/", "age_min": 3, "cats": "hockey"}, YA + " «Хоккейная школа Pro Hockey» (дети от 3 лет)"),
 "sokol-tt-leningradsky": ({"address": "Москва, Ленинградский просп., 80, корп. 4А", "phone": "+7 (985) 035-33-22", "url": "https://gosokol.ru/",
     "age_min": 6, "cats": "tabletennis"}, YA + " «Сокол — Территория спорта» (тренировки для детей от 6 лет)"),
 "arenaplay-yug-kommunarka": ({"address": "Москва, пос. Коммунарка, ул. Александры Монаховой, 21Б", "phone": "+7 (495) 147-44-43",
     "url": "https://arenaplay.ru/", "cats": "rinks,hockey,figureskating"}, YA + " «Арена Плей Юг»; arenaplay.ru"),
 "mayak-rink-krasny-mayak": ({"address": "Москва, ул. Красного Маяка, вл. 28", "phone": "+7 (495) 532-00-17", "url": "https://sportvsegda.ru/",
     "cats": "rinks"}, YA + " «Маяк» (каток); sportvsegda.ru (адрес)"),
 "luch-rink-volokolamskoe": ({"address": "Москва, Волоколамское ш., 88, корп. 9, стр. 3", "phone": "+7 (980) 194-87-34", "url": "https://lkluch.ru/",
     "cats": "rinks"}, YA + " «Луч» (каток)"),
 "petruseva-rink-pposad": ({"address": "Павловский Посад, Большая Покровская ул., 60В", "phone": "+7 (929) 945-05-23", "cats": "rinks"},
     YA + " «Ледовая арена имени Н.А. Петрусевой»"),
 "chernevskaya-gorka-krasnogorsk": ({"address": "Красногорск, ул. Карбышева", "phone": "+7 (916) 395-34-64", "url": "https://moon-village.club/",
     "cats": "ski"}, YA + " «Черневская горка»"),
}
out = {}
for pid, (f, src) in B.items():
    s = f"{src} ({D})"
    if pid in PTS:
        lat, lon, _, how = PTS[pid]
        f = dict(f, point={"lat": lat, "lon": lon, "level": "объект", "how": "OSM " + how})
        s = f"{src}; OSM {how.split(' ')[0]} ({D})"
    out[pid] = {"fields": f, "src": s}
print(json.dumps(out, ensure_ascii=False, indent=1))
