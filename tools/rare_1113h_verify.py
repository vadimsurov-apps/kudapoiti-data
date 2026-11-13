"""Пачка set_verified по местам rare 1113h: подтверждённые поля (точка — объект OSM; адрес/телефон/сайт/цена/возраст — сайт
места и карточка Яндекс Карт). Часов в источниках нет (Яндекс показывает лишь «закрыто до …», сайты не публикуют) — не пишем.
python3 tools/rare_1113h_verify.py > batch.json"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PTS = json.load(open(os.path.join(ROOT, "tools", "rare_1113h_points.json")))
D = "проверено 2026-11-13"
B = {
 "rink-icepark-zhukovsky": ({"address": "Жуковский, Молодёжная ул., 9", "type": "крытый каток", "cats": "rinks",
     "phone": "+7 (905) 500-99-98", "url": "https://ice-park.org/", "price_child": 600, "price_adult": 600,
     "how": "Въезд со стороны ул. Дугина, 20; парковка для посетителей бесплатная"},
     "ice-park.org (арена 56×28 м, массовое катание 600 ₽/час взрослым и детям, прокат, въезд с ул. Дугина, 20, телефон); карточка Яндекс Карт «АйсПарк»"),
 "fk-led-khimki": ({"address": "Химки, ул. Мичурина, стр. 24, корп. 1", "type": "школа фигурного катания", "cats": "figureskating",
     "phone": "+7 (925) 110-10-60", "url": "https://na-ldu.ru/", "age_min": 3, "age_max": 17, "price_child": 2000},
     "na-ldu.ru (дети 3,5–17 лет, адрес стр. 24 корп. 1, абонемент от 1 100 ₽); карточка Яндекс Карт «Лёд» (занятие для детей от 3,5 лет — 2000 ₽, телефон)"),
 "fk-pegas-domodedovo": ({"address": "Домодедово, мкр Центральный, ул. Кирова, 30", "type": "школа фигурного катания",
     "cats": "figureskating", "url": "https://figskating.ru/", "age_min": 3, "age_max": 17},
     "figskating.ru (группы 3,5 / 5–7 / 7–14 / 15–17 лет, адрес ул. Кирова, 30); карточка Яндекс Карт «Школа фигурного катания Пегас»"),
 "squash-sport-lines-ivanteevskaya": ({"address": "Москва, Ивантеевская ул., 13, корп. 1, 4 этаж", "type": "сквош-клуб",
     "cats": "squash,tabletennis", "phone": "+7 (977) 349-62-72", "url": "https://slsquash.ru/", "age_min": 6, "age_max": 16},
     "slsquash.ru (детские группы, подготовка с 6–7 лет, адрес); t-j.ru (детские группы 8–16 лет); карточка Яндекс Карт «Спортивные Линии» (телефон, этаж 4)"),
}
out = {}
for pid, (f, src) in B.items():
    if pid not in PTS:
        continue
    lat, lon, how = PTS[pid]
    f = dict(f, point={"lat": lat, "lon": lon, "level": "объект", "how": "OSM " + how})
    out[pid] = {"fields": f, "src": f"{src}; OSM {how.split(' ')[0]} ({D})"}
print(json.dumps(out, ensure_ascii=False, indent=1))
