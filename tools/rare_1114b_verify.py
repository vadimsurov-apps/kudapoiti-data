"""Пачка set_verified по местам rare 1114b: подтверждённые поля (адрес/телефон/сайт/цена/часы/категории — сайт места и карточка
Яндекс Карт; точка — только объект OSM). Точки из справки OSM — tools/rare_1114b_points.json (если пришла).
python3 tools/rare_1114b_verify.py > batch.json"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
pp = os.path.join(ROOT, "tools", "rare_1114b_points.json")
PTS = json.load(open(pp)) if os.path.exists(pp) else {}
PTS.setdefault("rink-iskra-rostokino", [55.838868, 37.638444, "relation/12225117 «Учебно-спортивный комплекс «Искра»» (leisure=sports_centre)"])
PTS.setdefault("rink-vershina-tsaritsyno", [55.600623, 37.706399, "way/313260854 «Центр развития детского и массового спорта «Вершина» им. Сергея Макарова» (leisure=sports_centre)"])
D = "проверено 2026-11-14"
YA = "карточка Яндекс Карт"
B = {
 "rink-iskra-rostokino": ({"address": "Москва, ул. Вильгельма Пика, стадион «Искра»", "type": "каток", "cats": "rinks",
     "phone": "+7 (499) 181-54-03", "url": "https://www.katokmoscow.ru/", "hours": "пн-пт 16:00-23:00; сб-вс 12:00-23:00",
     "parking": "бесплатная"},
     "сайт katokmoscow.ru (адрес, часы в сезон, бесплатная парковка, телефоны); " + YA + " «Каток Искра» (телефон)"),
 "rink-mikhalkovo-park": ({"address": "Москва, парк Петра Алексеева (усадьба Михалково)", "type": "каток", "cats": "rinks",
     "phone": "+7 (495) 663-55-33", "url": "https://kulturasao.ru/"},
     YA + " «Каток в парке-усадьбе Михалково» (адрес, телефон, сайт)"),
 "rink-pionersky-park": ({"address": "Москва, Кастанаевская ул., 62", "type": "каток", "cats": "rinks",
     "phone": "+7 (495) 927-67-65", "url": "https://культуразао.рф/"},
     YA + " «ОКЦ ЗАО, Каток с искусственным покрытием в парке Пионерский» (адрес, телефон, сайт)"),
 "rink-nikulino-park": ({"address": "Москва, просп. Вернадского, 100А", "type": "каток", "cats": "rinks",
     "phone": "+7 (495) 927-67-65", "url": "https://культуразао.рф/"},
     YA + " «ОКЦ ЗАО, Каток с искусственным покрытием в парке Никулино» (адрес, телефон, сайт)"),
 "rink-sosenki-tsaritsyno": ({"address": "Москва, район Царицыно, парк «Сосенки»", "type": "каток", "cats": "rinks"},
     YA + " «Каток в районе Царицыно» (парк Сосенки)"),
 "rink-bitsa-ksk": ({"address": "Москва, Чертаново Северное, конноспортивный комплекс «Битца»", "type": "каток", "cats": "rinks"},
     YA + " «Каток в конноспортивном комплексе Битца»"),
 "rink-vershina-tsaritsyno": ({"address": "Москва, Шипиловский пр-д, парк «Царицыно»", "type": "ледовая арена", "cats": "rinks",
     "phone": "+7 (495) 744-68-14", "url": "https://katok.top/", "price_adult": 500},
     "сайт katok.top (телефон, массовое катание); " + YA + " «Вершина» (адрес, массовое катание 1 ч — 500 ₽)"),
 "rink-lider-volokolamsk": ({"address": "Волоколамск, Рижское ш., 40", "type": "ледовый каток", "cats": "rinks",
     "phone": "+7 (49636) 2-96-09", "url": "https://lama-sport.ru/", "hours": "ежедневно 09:00-21:00"},
     "сайт lama-sport.ru (режим работы ФОК «Лидер»); " + YA + " «ФОК Лидер» (адрес, телефон, крытый каток)"),
 "rink-patriot-kubinka": ({"address": "Московская обл., Одинцовский г. о., парк «Патриот», у Соборной площади", "type": "каток",
     "cats": "rinks,sledding", "phone": "8 (800) 511-14-18", "url": "https://katokvpatriote.ru/", "hours": "ежедневно 10:00-22:00"},
     "сайт katokvpatriote.ru (сеансы 10:00–22:00, тюбинговые горки); " + YA + " «Каток в парке Патриот» (телефон)"),
 "fungrad-sokolniki": ({"address": "Москва, парк «Сокольники»", "type": "верёвочный парк", "cats": "ropes,trampolines",
     "phone": "+7 (905) 529-99-61", "url": "https://fungrad.ru/", "price_child": 1500, "age_min": 2, "age_max": 10},
     "сайт fungrad.ru; " + YA + " «FunГрад» (Сокольники: 4–10 лет — 1500 ₽/60 мин в будни, батут 2–5 лет, телефон)"),
 "fetisov-hockey-domodedovo": ({"address": "Домодедово, мкр Центральный, ул. Кирова, 30 (ЛСК «Легенда»)", "type": "хоккейная школа",
     "cats": "hockey", "phone": "+7 (906) 799-05-55", "url": "https://fetisovhockeyacademy.com/", "age_min": 5, "age_max": 14},
     "сайт fetisovhockeyacademy.com (набор 2021 г. р., команды 2012–2021 г. р., телефон); " + YA + " (адрес)"),
}
out = {}
for pid, (f, src) in B.items():
    if pid in PTS:
        lat, lon, how = PTS[pid]
        f = dict(f, point={"lat": lat, "lon": lon, "level": "объект", "how": "OSM " + how})
        src = f"{src}; OSM {how.split(' ')[0]}"
    out[pid] = {"fields": f, "src": f"{src} ({D})"}
print(json.dumps(out, ensure_ascii=False, indent=1))
