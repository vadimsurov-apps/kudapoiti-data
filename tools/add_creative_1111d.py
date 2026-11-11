"""Робот creative, 2026-11-11 (второй запуск). Поиск по районам Багратионовская … Боровское шоссе (14 станций метро) —
выдачи Яндекс Карт по 7 темам (auto/pages *-cr3<N>-1111d*), карточки организаций (*-cw<N>-1111d*: рубрика, адрес, этаж,
телефон, сайт, услуги с ценами и возрастом групп) и сайты мест из кэша auto/pages (возраст групп набора).
Взяты только места с возрастом групп в источнике и без дубля в places-all.json и data/parts (по названию в городе).
Справка OSM (cr3-*) в этот запуск не пришла: GitHub Actions стояли в очереди больше часа. Точка — станция метро из
карточки («Как добраться»), «примерно»: место скрыто, пока osm-local не поставит его на дом/вход по адресу
(pipeline/osm_address.py) или подтверждатель скрытых не найдёт объект OSM. WebFetch не использовался.
Запуск: KP_PART=creative python3 tools/add_creative_1111d.py [--dry]"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DT = "2026-11-11"
MET = {}
for m in re.finditer(r'"([^"]+)": \("([^"]+)", ([\d.]+), ([\d.]+)\)', open(os.path.join(ROOT, "tools", "MetroStations.swift")).read()):
    MET[m.group(2)] = (float(m.group(3)), float(m.group(4)))

TAGS = {"dance": "спорт и активность, музыка", "ballet": "спорт и активность, музыка", "singing": "музыка",
        "music": "музыка", "theaterstudio": "сказки и театр, творчество", "drawing": "творчество", "ceramics": "творчество"}

# id: (название, тип, категории, возраст от, до, адрес, «как найти», телефон, сайт, метро (из карточки, расстояние),
#      плюс, выдача Яндекс Карт, источник возраста)
D = {
    "adm-miklukho-maklaya": ("Академия детского мюзикла (Беляево)", "студия мюзикла", "theaterstudio,singing,dance", 4, 16,
        "ул. Миклухо-Маклая, 18, корп. 1", "Этаж: 3", "+7 (495) 624-88-88", "https://www.musicalacademy.ru",
        ("Беляево", "650 м"),
        "Программа для детей 4–16 лет: вокал, хореография и актёрское мастерство вместе — ставят настоящий мюзикл и выходят на большую сцену",
        "вокал для детей метро Беляево", "сайт musicalacademy.ru («для детей от 4 до 16 лет»)"),
    "guitar-school-1-miklukho": ("Гитарная школа № 1 (Беляево)", "гитарная школа", "music", 8, 16,
        "ул. Миклухо-Маклая, 22", None, "+7 (931) 521-44-63", "https://guitar-studio.ru",
        ("Беляево", "430 м"),
        "Гитара и укулеле для детей 8–16 лет, раз в неделю в небольших группах; инструмент дают на занятие; пробный урок укулеле — 990 ₽",
        "музыкальная школа метро Беляево", "сайт guitar-studio.ru («для детей 8–16 лет»), цена пробного — карточка Яндекс Карт"),
    "buff-kastanaevskaya": ("Театральная студия «Буфф» (Пионерская)", "театральная студия", "theaterstudio", 4, 16,
        "Кастанаевская ул., 52, стр. 2", None, "+7 (964) 575-63-36", "https://ctbuff.ru",
        ("Пионерская", "360 м"),
        "Группы 4–8 лет («Театр и школа»), 7–12 и 12–16 лет, до 12 детей в группе; абонемент на 8 занятий для 4–8 лет — 8 600 ₽",
        "театральная студия для детей метро Багратионовская", "сайт ctbuff.ru (4–16 лет, филиал на Пионерской), цена — карточка Яндекс Карт"),
    "krb-yamskogo-polya": ("Академия талантов KRB (Белорусская)", "детская творческая академия", "singing,theaterstudio", 8, 17,
        "3-я ул. Ямского Поля, 9", None, "+7 (968) 510-80-86", "https://academykrb.ru",
        ("Белорусская", "750 м"),
        "Творческий комплекс для 8–17 лет: вокал, хор, хореография, актёрское мастерство и сольфеджио; есть «Медиа» — школа юных теле- и радиоведущих",
        "вокал для детей метро Белорусская", "карточка Яндекс Карт, «Товары и услуги» (программы «от 8 до 17 лет»)"),
    "bcballet-baumanskaya": ("Балетная студия «Балет в большом городе» (Бауманская)", "балетная студия", "ballet", 5, 15,
        "Бауманская ул., 53/2", None, "+7 (903) 571-73-31", "https://bcballet.ru",
        ("Бауманская", "490 м"),
        "Балет для детей 5–15 лет любого уровня; два раза в год выступают на большой сцене",
        "балетная школа для детей метро Бауманская", "карточка Яндекс Карт («Занятия балетом для детей от 5 до 15 лет»)"),
    "le-petit-ballerine-yamskogo": ("Школа балета «Ле Пти балерин» (Белорусская)", "школа балета", "ballet", 3, 17,
        "3-я ул. Ямского Поля, 24", None, "+7 (985) 056-27-05", None,
        ("Белорусская", "900 м"),
        "Балет для малышей с 3 лет и для детей постарше; разовое занятие — 875 ₽",
        "балетная школа для детей метро Белорусская", "карточка Яндекс Карт («для малышей от 3 лет», «балет для детей»)"),
    "risovanie-novoperedelkinskaya": ("Студия «Рисование» (Новопеределкино)", "студия рисования", "drawing", 3, 17,
        "Новопеределкинская ул., 16, корп. 1", None, "+7 (965) 230-07-27", "https://newppaint.ru",
        ("Боровское шоссе", "590 м"),
        "Рисование и лепка для детей с 3 лет, отдельные группы для школьников и ИЗО для старшеклассников",
        "рисование для детей метро Баррикадная", "карточка Яндекс Карт (услуги «для детей от 3 лет», «для учеников старшей школы»)"),
    "vdokhnovenie-litovsky": ("Центр творчества «Вдохновение» (Ясенево)", "школа искусств", "dance,drawing,ceramics", 4, 17,
        "Литовский бул., 7", None, "+7 (495) 197-71-70", "https://v-v-v.ru",
        ("Ясенево", "880 м"),
        "Балет, хип-хоп, брейк и бальные танцы — с 4 лет; рисунок, живопись и керамика — с 6 лет; пробное занятие в любой студии — 500 ₽",
        "вокал для детей метро Битцевский Парк", "карточка Яндекс Карт (возраст по направлениям: танцы с 4 лет, хип-хоп 7–18, брейк 5–16, ИЗО и керамика с 6 лет)"),
}
CAT_AGES = {"vdokhnovenie-litovsky": {"dance": [4, 17], "drawing": [6, 17], "ceramics": [6, 17],
                                      "src": "Яндекс Карты, карточка «Вдохновение», Литовский бул., 7: «Балет, хип-хоп, брейк-данс, бальные для детей с 4 лет», «Рисунок, живопись, керамика, анимация для детей с 6 лет» (11.11.2026)"},
            "adm-miklukho-maklaya": None}


def row(pid):
    name, typ, cats, a0, a1, addr, how, phone, url, (st, dist), plus, q, asrc = D[pid]
    lat, lon = MET[st]
    first = cats.split(",")[0]
    active = first in ("dance", "ballet")
    r = P(pid, name, typ, st, addr, lat, lon, a0, a1, 45, 90, "активно" if active else "спокойно", TAGS[first],
          None, None, None, "да", plus, None, adult=1,
          src=f"Яндекс Карты: выдача «{q}» и карточка организации (адрес, этаж, телефон, сайт, услуги), 11.11.2026; возраст — {asrc}",
          acc=f"примерно: станция метро {st} (по карточке до места {dist}); дом и вход уточнит сверка с OSM по адресу",
          adult_price=None, booking="обязательна", loud="частично" if active or first in ("music", "singing") else "нет",
          sit="нет" if active else "частично", crowd="нет", food="нет", stroller="частично")
    r["Взрослый билет, ₽"] = None
    r["Сайт"] = url
    r["Категории"] = cats
    r["Как найти"] = how
    r["Проверено (дата)"] = DT
    return r


ROWS = [row(pid) for pid in D]

if __name__ == "__main__":
    pa = json.load(open(os.path.join(ROOT, "places-all.json")))
    PL = {p["id"] for p in (pa["places"] if isinstance(pa, dict) else pa)}
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    ids = [r["id"] for r in ROWS]
    assert not [i for i in ids if i in existing or i in PL], [i for i in ids if i in existing or i in PL]
    if "--dry" in sys.argv:
        for r in ROWS:
            print(r["id"], "|", r["Адрес"], "|", r["Метро"], r["Широта"], r["Долгота"])
        sys.exit()
    r0 = ws.max_row + 1
    for n, row_ in enumerate(ROWS):
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=r0 + n, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    # возраст по направлениям (урок 8)
    cp = os.path.join(ROOT, "auto", "cat-ages.json")
    ca = json.load(open(cp)) if os.path.exists(cp) else {}
    for pid, v in CAT_AGES.items():
        if v:
            ca[pid] = v
    json.dump(ca, open(cp, "w"), ensure_ascii=False, indent=1)
    print("rows", len(ROWS))
