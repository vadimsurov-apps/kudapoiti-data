"""Пачка set_verified по местам rare 1114d: подтверждённые поля (адрес/телефон/сайт/возраст/цена — карточка организации
в Яндекс Картах и сайт места; точка — объект OSM, где найден; доступность — только где карточка прямо пишет).
Полных часов в источниках нет — не пишем.   python3 tools/rare_1114d_verify.py > batch.json"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PTS = json.load(open(os.path.join(ROOT, "tools", "rare_1114d_points.json")))
D = "проверено 2026-11-14"
YA = "карточка организации в Яндекс Картах (auto/pages)"
B = {
 "bulldozer-hockey-megasport": ({"address": "Москва, Ходынский бул., 3 (Дворец спорта «Мегаспорт»)", "phone": "+7 (901) 591-67-41",
     "age_min": 3, "age_max": 17, "price_child": 4000, "cats": "hockey"},
     YA + " «Bulldozer» (групповая тренировка для детей от 3 до 17 лет — 4000 ₽ без учёта льда)", None),
 "crazy-snowflakes-soloslovo": ({"address": "Одинцовский г. о., д. Солослово, КП «Резиденции Берёзки Ривер Вилладж», 314",
     "phone": "+7 (925) 183-22-02", "url": "https://crazyflakes.ru/", "age_min": 3, "age_max": 12, "price_child": 4150,
     "cats": "figureskating"}, YA + " «Безумные снежинки» (групповое занятие для детей от 3 до 12 лет — 4150 ₽)",
     {"wheelchair": "yes", "toilet": "yes", "lift": "yes", "parking": "yes",
      "note": "по карточке в Яндекс Картах: пандус, лифт, туалет и парковка для людей с инвалидностью, вход доступен на коляске"}),
 "pingpoint-tt-savelovskaya": ({"address": "Москва, 1-я Квесисская ул., 9", "phone": "+7 (495) 150-55-43", "url": "https://pingpoint.ru/",
     "age_max": 13, "price_child": 1500, "cats": "tabletennis"},
     "сайт pingpoint.ru (дети до 14 лет — сб и вс 11:00, 60 мин, 1500 ₽; адрес, телефон); " + YA + " «Ping Point»", None),
 "squash-time-myshenskoe": ({"address": "Ступино (г. о.), ТСН Мышенское, Озёрная ул., 4 (КП Green Forest)", "phone": "+7 (985) 700-93-33",
     "url": "https://squashtime.ru/", "age_max": 15, "cats": "squash"},
     "сайт squashtime.ru (адрес, абонемент для детей до 16 лет); " + YA + " «Сквош Тайм» (телефон)", None),
 "samolet-arena-rink-kommunarka": ({"address": "Москва, пос. Коммунарка, квартал № 195, 16к1вл1", "phone": "+7 (985) 042-46-19",
     "url": "https://micarena.ru/", "price_child": 500, "cats": "rinks"},
     YA + " «Самолёт Арена» (массовое катание 1 ч — 500 ₽, прокат 600 ₽, пингвин 350 ₽)",
     {"wheelchair": "yes", "toilet": "yes", "parking": "yes",
      "note": "по карточке в Яндекс Картах: вход и помещение доступны на коляске, туалет и парковка для людей с инвалидностью"}),
 "legenda-rink-domodedovo": ({"address": "Домодедово, мкр Центральный, ул. Кирова, 30 (СК «Легенда»)", "phone": "+7 (495) 120-11-36",
     "url": "https://sklegenda.ru/rink/skating/", "price_child": 450, "cats": "rinks",
     "free_note": "дети до 7 лет — на лёд только со взрослым; сеанс 1 ч — 450 ₽, вечерний 1,5 ч — 650 ₽; прокат коньков — 450 ₽ (залог 2000 ₽ или документ)"},
     "сайт sklegenda.ru (сезон массового катания с 06.11.2026, цены сеансов и проката, дети младше 7 лет — только в сопровождении); "
     + YA + " «Легенда» (адрес, телефон)", None),
 "krylatskoe-ld-rink": ({"address": "Москва, Крылатская ул., 16", "phone": "+7 (906) 740-66-35", "url": "https://megasport.mossport.ru/",
     "cats": "rinks"}, YA + " «Ледовый дворец Крылатское» (адрес, телефон справочной, сайт, массовые катания)",
     {"wheelchair": "limited", "toilet": "yes", "lift": "yes", "parking": "yes",
      "note": "по карточке в Яндекс Картах: вход доступен на коляске, помещение — частично; есть пандус, лифт, туалет и парковка для людей с инвалидностью"}),
 "kosmoled-rink-korolev": ({"address": "Королёв, Октябрьская ул., 6, стр. 1", "phone": "+7 (926) 263-33-36", "cats": "rinks",
     "parking": "бесплатная"}, YA + " «Каток Космолёд» (открытый каток, билеты 200–800 ₽, прокат 500 ₽, бесплатная парковка)", None),
 "malevich-rink-odintsovo": ({"cats": "rinks"}, "выдача Яндекс Карт «Каток Малевича» (каток в парке Малевича, Одинцовский г. о.)", None),
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
