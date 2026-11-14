"""Робот pools 14.11 (14 UTC), шаг 2: карточки Яндекс Карт новых кандидатов (ключ po<N>=1114p) → auto/fetch-queue.txt,
справка OSM (pl34-*) → auto/osm-queries.json.   python3 tools/pools_1114p_cardq.py"""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q = [
 "Акулёнок, Москва, 3-я Хорошёвская ул., 19А",
 "Акулёнок детский бассейн, Коммунарка, Севильский бульвар, 3",
 "Kido детское плавание, Коммунарка, Скандинавский бульвар, 23, корп. 1",
 "Морепользы, Коммунарка, проспект Куприна, 30, корп. 1",
 "ГрудничОк, Бутово, жилой комплекс Бутово Парк, 20, корп. 1",
 "Грудничковое плавание, посёлок Газопровод, 101А",
 "Start Swim, Москва, Большой Строченовский пер., 10",
 "Start Swim, Москва, ул. Земляной Вал, 71, стр. 2",
 "Mevis, Москва, Большой Строченовский пер., 10",
 "Strong Swim, Москва, Чертановская ул., 45Б",
 "SwimRocket, Москва, Чертановская ул., 45Б",
 "Золотые рыбки обучение плаванию, Москва, Рабочая ул., 53, стр. 1",
 "Бассейн дворца детского спорта, Москва, Рабочая ул., 53, стр. 1",
 "Swimaquarel, Москва, ул. Тёплый Стан, 9, корп. 9",
 "Буду Плыть, Москва, ул. Тёплый Стан, 9, корп. 9",
 "Плавать Умеем, Москва, ул. Генерала Глаголева, 10, корп. 3, стр. 2",
 "Школа плавания № 1, Москва, ул. Земляной Вал, 71, стр. 2",
 "Школа плавания № 1 Еврейский центр, Москва, ул. Образцова, 11, стр. 4",
 "Дворец творчества детей и молодёжи Преображенский бассейн, Москва, Большая Черкизовская ул., 15",
 "Ohana фитнес детский бассейн, Московский, ул. Хабарова, 2",
 "Aquastar детское плавание, Москва, Партийный пер., 1, корп. 57, стр. 3",
 "Юна Aqua Life, Москва, Кировоградская ул., 15",
 "Центр образования и спорта Москва-98 бассейн, Москва, ул. Удальцова, 87",
 "РезиДетство, Троицк, Центральная ул., 15",
 "Бассейн Мосрентген Видное-4 спортивная школа",
 "Территория Фитнеса школа плавания, Москва, ул. Академика Понтрягина, 14",
 "Палестра Спорт детский бассейн, Москва, 2-я Песчаная ул., 4А, стр. 2",
 "Акулёнок детский бассейн Москва",
 "Морепользы детский бассейн",
 "Start Swim школа плавания Москва",
]
EXTRA = ["https://startswim.ru/", "https://mevis.ru/pools", "https://mevis.ru/detyam", "https://strongswim.ru/", "https://kidopool.ru/",
         "https://akulenok.ru/", "https://swimaquarel.ru/", "https://grudnichok.ru/", "https://dtdm-preobr.mskobr.ru/"]
OSM = [
 {"id": "pl34-morepolzy-kuprina", "lat": 55.5880, "lon": 37.4330, "radius": 2500, "name": "Морепользы", "street": "Куприна"},
 {"id": "pl34-grudnichok-butovo-park", "lat": 55.5250, "lon": 37.6050, "radius": 2500, "name": "ГрудничОк"},
 {"id": "pl34-grudnichkovoe-gazoprovod", "lat": 55.5850, "lon": 37.4860, "radius": 1500, "name": "бассейн"},
 {"id": "pl34-obraztsova-11", "lat": 55.7935, "lon": 37.6100, "radius": 500, "name": "бассейн", "street": "Образцова"},
 {"id": "pl34-rabochaya-53", "lat": 55.7395, "lon": 37.6830, "radius": 700, "name": "Дворец детского спорта", "street": "Рабочая"},
 {"id": "pl34-udaltsova-87", "lat": 55.6790, "lon": 37.4850, "radius": 1200, "name": "Москва-98", "street": "Удальцова"},
 {"id": "pl34-troitsk-tsentralnaya-15", "lat": 55.4850, "lon": 37.3050, "radius": 2500, "name": "РезиДетство", "street": "Центральная"},
 {"id": "pl34-pontryagina-14", "lat": 55.5440, "lon": 37.5300, "radius": 1500, "name": "Территория Фитнеса", "street": "Понтрягина"},
 {"id": "pl34-neptun-federativny", "lat": 55.7560, "lon": 37.8090, "radius": 500, "name": "Нептун"},
 {"id": "pl34-khoroshevskaya-19a", "lat": 55.7850, "lon": 37.4965, "radius": 250, "name": "Акулёнок"},
]
if __name__ == "__main__":
    lines = list(EXTRA)
    for i, q in enumerate(Q):
        lines.append("https://yandex.ru/maps/1/moscow-and-moscow-oblast/?po%d=1114p&text=%s" % (i, urllib.parse.quote(q)))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in lines if l not in old]) + "\n")
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = json.load(open(p)); have = {x["id"] for x in old}
    json.dump(old + [q for q in OSM if q["id"] not in have], open(p, "w"), ensure_ascii=False, indent=1)
    print(len(lines), len(OSM))
