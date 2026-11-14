"""Пачка set_verified по местам rare 1114f: подтверждённые поля (адрес/телефон/сайт/возраст/цена/часы — сайт места и карточка
организации в Яндекс Картах из auto/pages). Точки приблизительные — не пишем.   python3 tools/rare_1114f_verify.py > batch.json"""
import json
D = "проверено 2026-11-14"
YA = "карточка организации в Яндекс Картах (auto/pages)"
B = {
 "icezubrus-cska": ({"address": "Москва, Ленинградский пр-т, 39, стр. 1 (крытый легкоатлетическо-футбольный комплекс ЦСКА)",
     "phone": "+7 (903) 681-79-25", "url": "https://academy-ice-zubrus.ru/", "age_min": 4, "age_max": 11, "price_child": 2500,
     "cats": "hockey"}, "сайт academy-ice-zubrus.ru (группа 4–11 лет, 2500 ₽, адрес); " + YA + " «Хоккейная академия IceZubrus» (телефон)"),
 "nevsky-bears-nagatinskaya": ({"address": "Москва, Нагатинская ул., 16", "phone": "+7 (499) 877-46-81",
     "url": "https://nevsky-bears.ru/", "age_min": 9, "age_max": 17, "cats": "volleyball"},
     YA + " «Невские медведи» (Нагатинская ул., 16; дети и подростки 9–17 лет; телефон; сайт nevsky-bears.ru)"),
 "rink-polyus-arena-gorki2": ({"address": "Одинцовский г. о., пос. Горки-2, 23", "phone": "+7 (925) 677-39-55",
     "url": "https://polyus-arena.ru/", "hours": "пн–вс 06:00–00:00", "parking": "бесплатная", "cats": "rinks"},
     "сайт polyus-arena.ru (часы пн–вс 06:00–00:00, как добраться); " + YA + " «Полюс Арена» (адрес, телефон, бесплатная парковка)"),
 "ski-zavadovskaya-krylatskoe": ({"address": "Москва, Крылатская ул., 1, стр. 3", "phone": "+7 (995) 501-64-62",
     "url": "https://zavadovskaya.club/", "hours": "ежедневно 08:00–00:00", "age_min": 3, "age_max": 17, "cats": "ski"},
     "сайт zavadovskaya.club (адрес Крылатская, 1с3; дети с 2,5–3 лет; тренажёр 8:00–00:00 круглый год; телефон); " + YA + " «Zavadovskaya. club»"),
 "karting-dixxodrom-izmailovo": ({"address": "Москва, Измайловское ш., 73, стр. 3", "phone": "+7 (925) 900-79-00",
     "url": "https://dixxodrom.ru/", "age_min": 5, "price_child": 1300, "cats": "karting"},
     "сайт dixxodrom.ru («дети с 5 лет», детские карты 5,5 л. с.); " + YA + " «Диксодром» (адрес, телефон, заезд 5,5 л. с. в будни 1300 ₽)"),
}
print(json.dumps({pid: {"fields": f, "src": f"{s} ({D})"} for pid, (f, s) in B.items()}, ensure_ascii=False, indent=1))
