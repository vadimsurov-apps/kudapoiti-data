"""Пачка set_verified по местам rare 1114a: подтверждённые поля (точка — объект OSM; адрес/телефон/сайт/цена/возраст — сайт
места и карточка Яндекс Карт). Часов в источниках нет (Яндекс показывает лишь «закрыто до …»/«открыто до …») — не пишем,
кроме памп-трека «Фукусима» (открытая территория, «круглосуточно» в карточке).
python3 tools/rare_1114a_verify.py > batch.json"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PTS = json.load(open(os.path.join(ROOT, "tools", "rare_1114a_points.json")))
D = "проверено 2026-11-14"
YA = "карточка Яндекс Карт"
B = {
 "rink-borisoglebsky-ramenskoe": ({"address": "Раменское, ул. Махова, 18/1", "type": "ледовый дворец", "cats": "rinks",
     "phone": "+7 (926) 216-80-60", "url": "https://dsbg.ru/", "price_adult": 300},
     YA + " «Дворец спорта Борисоглебский» (адрес, телефон, сайт, массовое катание 1 ч — 300 ₽ старше 14 лет)", None, "объект"),
 "hockey-masters-mosfilmovskaya": ({"address": "Москва, Мосфильмовская ул., 41, корп. 3", "type": "хоккейная школа", "cats": "hockey",
     "phone": "+7 (985) 293-29-82", "url": "https://hockeymasters.ru/", "age_min": 4, "age_max": 12},
     "hockeymasters.ru (группы 4–7 и 7–12 лет, телефон); " + YA + " «Мастера Хоккея» (адрес)", None, None),
 "pumptrack-chertanovo-severnoe": ({"address": "Москва, район Чертаново Северное", "type": "скейт-парк", "cats": "skate,pumptrack",
     "hours": "круглосуточно", "price_child": 0},
     YA + " «Памп-трек» (Чертаново Северное, круглосуточно, телефона нет)", None, "объект"),
}
out = {}
for pid, (f, src, acc, level) in B.items():
    if pid not in PTS:
        continue
    lat, lon, how = PTS[pid]
    if level:  # точка — объект OSM самого места; у «Мастеров хоккея» точка приблизительная — в реестр не пишем
        f = dict(f, point={"lat": lat, "lon": lon, "level": level, "how": "OSM " + how})
    out[pid] = {"fields": f, "src": f"{src}; OSM {how.split(' ')[0]} ({D})" if level else f"{src} ({D})"}
    if acc:
        out[pid]["access"] = acc
print(json.dumps(out, ensure_ascii=False, indent=1))
