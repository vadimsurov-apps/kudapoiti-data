"""Робот pools 14.11 (14 UTC), шаг 3: сайты кандидатов и уточняющие карточки Яндекс Карт (ключ pc<N>=1114p) → auto/fetch-queue.txt,
справка OSM (pl34-*) → auto/osm-queries.json.   python3 tools/pools_1114p_siteq.py"""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Y = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?pc%d=1114p&text=%s"
LINES = ["https://kido.center/", "https://ohanamoskovsky.ru/", "https://pav.aquastar.club/", "https://varshavka.juna-life.ru/",
         "https://palestrasport.ru/", "https://www.swimrocket.ru/plavanie-dlya-detey/", "https://www.swimrocket.ru/bassein-sk-volna/",
         "https://terfit.ru/t-swim-school/butovo/", "https://terfit.ru/t-swim-school/yuzhnoe-butovo/", "https://terfit.ru/t-swim-school/hovrino/",
         "https://terfit.ru/t-swim-school/reutov/", "https://terfit.ru/t-swim-school/mitino/", "https://terfit.ru/t-swim-school/pechatniki/",
         "https://zolotye-ribki.ru/raspisanie", "https://strongswim.ru/contacts", "https://iwillswim.ru/soyuz", "https://iwillswim.ru/pools"]
for i, q in enumerate(["Московская детская школа плавания, Москва, ул. Образцова, 11, стр. 4",
                       "Школа плавания Романа Смольского, Москва, ул. Образцова, 11, стр. 4",
                       "Плыви с Алисой, Московский, Солнечная ул., 9",
                       "Школа Плавания Территория Фитнеса, Москва, ул. Академика Понтрягина, 14",
                       "Aqua клуб Морской львёнок, Раменское, Бронницкая ул., 6",
                       "Школа плавания Территория Фитнеса, Москва, ул. Марьинский Парк, 29А",
                       "Школа плавания Территория Фитнеса, Люберцы, 3-е Почтовое отделение, 102",
                       "Школа плавания Территория Фитнеса, Москва, Ландышевая ул., 3",
                       "Акулёнок бассейн Коммунарка Севильский бульвар 3 грудничковое плавание возраст",
                       "Start Swim, Москва, 2-я Песчаная ул., 4А, стр. 2",
                       "Грудничковое плавание Газопровод 101А оздоровительный комплекс",
                       "детский бассейн Мосрентген",
                       "обучение плаванию детей Мосрентген",
                       "детский бассейн Сосенское Коммунарка грудничковое плавание"]):
    LINES.append(Y % (i, urllib.parse.quote(q)))
OSM = [
 {"id": "pl34-tswim-lyublino", "lat": 55.6670, "lon": 37.7520, "radius": 1800, "name": "Территория Фитнеса", "street": "Марьинский"},
 {"id": "pl34-tswim-zhulebino", "lat": 55.6880, "lon": 37.8720, "radius": 1800, "name": "Территория Фитнеса", "street": "Почтовое"},
 {"id": "pl34-tswim-kurkino", "lat": 55.8930, "lon": 37.3890, "radius": 1500, "name": "Территория Фитнеса", "street": "Ландышевая"},
 {"id": "pl34-alisa-moskovsky-solnechnaya", "lat": 55.5990, "lon": 37.3560, "radius": 2000, "name": "Плыви с Алисой", "street": "Солнечная"},
 {"id": "pl34-lvenok-ramenskoe", "lat": 55.5700, "lon": 38.2300, "radius": 3000, "name": "львёнок", "street": "Бронницкая"},
]
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in LINES if l not in old]) + "\n")
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = json.load(open(p)); have = {x["id"] for x in old}
    json.dump(old + [q for q in OSM if q["id"] not in have], open(p, "w"), ensure_ascii=False, indent=1)
    print(len(LINES))
