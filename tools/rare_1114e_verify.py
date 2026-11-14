"""Пачка set_verified по местам rare 1114e: подтверждённые поля (адрес/телефон/сайт/возраст/цена — карточка организации
в Яндекс Картах и сайт места; точка — объект OSM, где найден; доступность — только где карточка прямо пишет).
Полных часов в источниках нет — не пишем.   python3 tools/rare_1114e_verify.py > batch.json"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PTS = json.load(open(os.path.join(ROOT, "tools", "rare_1114e_points.json")))
D = "проверено 2026-11-14"
YA = "карточка организации в Яндекс Картах (auto/pages)"
B = {
 "lyapkin-hockey-tomilino": ({"address": "Люберецкий г. о., пгт Томилино, ул. Крылова, 6", "phone": "+7 (925) 476-77-31",
     "url": "https://lyapkin-hockey.ru/", "age_min": 3, "age_max": 17, "cats": "hockey"},
     "сайт lyapkin-hockey.ru (дети от 3 лет, площадка Томилино, ул. Крылова, 6, расписание); " + YA + " «Хоккейная академия Юрия Ляпкина»",
     {"wheelchair": "yes", "toilet": "yes", "parking": "yes",
      "note": "по карточке в Яндекс Картах: пандус, вход доступен на коляске, туалет и парковка для людей с инвалидностью"}),
 "lyapkin-hockey-nekrasovka": ({"address": "Москва, Покровская ул., 22 (Дворец спорта «Некрасовка»)", "phone": "+7 (965) 230-09-79",
     "url": "https://lyapkin-hockey.ru/", "age_min": 3, "age_max": 17, "price_child": 1250, "cats": "hockey"},
     "сайт lyapkin-hockey.ru (площадка Некрасовка, Покровская ул., 22; дети от 3 лет); " + YA + " (тренировка ОФП + лёд — 1250 ₽)", None),
 "fk-motorin-dolgoprudny": ({"address": "Долгопрудный, просп. Ракетостроителей, 4 (ФОК «Салют»)", "phone": "+7 (999) 277-49-95",
     "url": "https://motorinschool.ru/", "age_min": 3, "age_max": 17, "cats": "figureskating"},
     YA + " «Школа фигурного катания Алексея Моторина» (группы 3–6, 7–9 лет и старше)", None),
 "liga-fskate-zelenograd": ({"address": "Зеленоград, Проектируемый пр-д № 684 (Arena Play Технополис)", "phone": "+7 (925) 685-21-03",
     "url": "https://ligafskate.ru/", "age_min": 3, "age_max": 17, "cats": "figureskating"},
     "сайт ligafskate.ru (адрес филиала, группы с 3 лет); " + YA + " «Лига фигурного катания» (телефон)", None),
 "golden-star-zheleznodorozhny": ({"address": "Балашиха, мкр Железнодорожный, Пионерская ул., 1А", "phone": "+7 (977) 726-34-27",
     "url": "https://goldenstar-skating.ru/", "age_min": 3, "age_max": 17, "cats": "figureskating"},
     "сайт goldenstar-skating.ru (филиал Железнодорожный, Пионерская, 1А; дети с 3 лет); " + YA + " «Школа фигурного катания Golden Star» (телефон)", None),
 "golden-star-molokovo": ({"address": "Ленинский г. о., пгт Молоково, Школьная ул., 6А", "url": "https://goldenstar-skating.ru/",
     "age_min": 3, "age_max": 17, "cats": "figureskating"},
     "сайт goldenstar-skating.ru (филиал Молоково, ул. Школьная, 6А; дети с 3 лет)", None),
 "golden-star-khimki-aysberg": ({"address": "Химки, ул. Пожарского, вл. 22А (каток «Айсберг»)", "url": "https://goldenstar-skating.ru/",
     "age_min": 3, "age_max": 17, "cats": "figureskating"},
     "сайт goldenstar-skating.ru (филиал Химки «Айсберг», ул. Пожарского, вл22А; дети с 3 лет)", None),
 "rink-psb-patriot-kubinka": ({"phone": "+7 (495) 995-10-85", "url": "https://psbpatriot.cosmosgroup.ru/", "price_child": 400,
     "cats": "rinks"}, YA + " «Ледовая арена ПСБ Патриот» (массовое катание 1 ч — 400 ₽, хоккейное — 500 ₽, прокат)",
     {"wheelchair": "limited", "toilet": "yes", "parking": "yes",
      "note": "по карточке в Яндекс Картах: вход доступен на коляске, помещение — частично; туалет и парковка для людей с инвалидностью, кнопка вызова персонала"}),
 "rink-orion-technopool-zheldor": ({"phone": "+7 (925) 500-04-78", "cats": "rinks"},
     YA + " «Орион-Технопул» (крытый каток, билеты 200–500 ₽, прокат 300 ₽)",
     {"wheelchair": "limited", "parking": "yes",
      "note": "по карточке в Яндекс Картах: пандус, вход доступен на коляске, помещение — частично; парковка для людей с инвалидностью"}),
 "rink-salyut-dolgoprudny": ({"address": "Долгопрудный, просп. Ракетостроителей, 4 (ФОК «Салют»)", "phone": "+7 (495) 576-02-92",
     "url": "https://www.stadion-salut.ru/", "cats": "rinks"},
     "сайт stadion-salut.ru (каток: спортивное и массовое катание, прокат); " + YA + " «Салют» (адрес, телефон)",
     {"wheelchair": "yes", "toilet": "yes", "lift": "yes", "parking": "yes",
      "note": "по карточке в Яндекс Картах: пандус, лифт, туалет и парковка для людей с инвалидностью, вход и помещение доступны на коляске"}),
 "rink-arena-legend-ozery": ({"address": "Озёры, Парковая ул., 2Г", "phone": "+7 (985) 473-03-43", "url": "https://arenaleg.ru/",
     "cats": "rinks"}, "сайт arenaleg.ru (адрес, телефон, сеансы массового катания); " + YA + " «Арена Легенд»", None),
}
out = {}
for pid, (f, src, acc) in B.items():
    s = f"{src} ({D})"
    if pid in PTS:
        lat, lon, _, how = PTS[pid]
        f = dict(f, point={"lat": lat, "lon": lon, "level": "объект", "how": "OSM " + how})
        s = f"{src}; OSM {how.split(' ')[0]} ({D})"
    if acc:
        f = dict(f, access=acc)
    out[pid] = {"fields": f, "src": s}
print(json.dumps(out, ensure_ascii=False, indent=1))
