"""Робот creative, 13.11 (запуск 1113b): места из выдач Яндекс Карт по 15 районам (Панфиловская … Коломна, 7 тем,
auto/pages *-cv<N>-1113b*), карточки организаций (*-cc<N>-1113b*: рубрика, адрес, этаж/вход, телефон, сайт, услуги с
возрастом групп) и сайты мест из кэша auto/pages. Возраст — только по источнику; «с N лет» без верхней границы → до 17.
Точки — справка OSM crs-* (объект OSM места → «объект»; иначе дом строго по адресу — место скрыто, пока сверка не найдёт вход).
WebFetch не использовался. Запуск: KP_PART=creative python3 tools/add_creative_1113b.py [--dry|deals|verify]"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DT = "2026-11-13"
YA = "https://yandex.ru/maps/org/"
OBJ = "объект"
# id: (название, тип, категории, от, до, метро, до метро, адрес, (lat, lon, уровень, osm), телефон, сайт, часы, как найти,
#      плюс, источник возраста/услуг, карточка Яндекса, cat_ages|None)
D = {
 "skazka-ballet-khodynsky": ("Академия балета «Сказка» (Ходынский бульвар)", "школа балета", "ballet", 3, 16,
    "ЦСКА", "270 м", "Ходынский бул., 10Б", (55.786966, 37.529834, "дом", None),
    "+7 (965) 103-44-40", "https://baletskazka.ru", None, None,
    "Балет для малышей 3–5 лет — игровые уроки с ритмикой, гимнастикой и азбукой танца; группы школьников 7–16 лет; абонемент раз в неделю для 3–5 лет — 5 500 ₽",
    "карточка Яндекс Карт («Абонемент 1 раз в неделю (1 час) 3-5 лет — 5500 ₽», «Абонемент 2 раза в неделю (1,5 часа) 7-16 лет»)", "ballet_academy_skazka/203679252450", None),
 "ya-tantsuyu-parkovaya": ("Школа танцев «Я Танцую» (Первомайская)", "школа танцев", "dance,ballet", 5, 16,
    "Первомайская", "290 м", "10-я Парковая ул., 3", (55.794386, 37.801907, "дом", None),
    "+7 (925) 173-09-03", "https://idance.su", None, "Этаж: 1",
    "Детские группы хип-хопа 5–8, 10–13 и 14–16 лет и балета 6–8, 10–14 и 14–16 лет",
    "карточка Яндекс Карт («Хип-хоп: группы 5-8 лет; 10-13 лет; 14-16 лет», «Балет: 6-8 лет; 10-14 лет; 14-16 лет», этаж 1)", "i_am_dancing/1319753898",
    {"dance": [5, 16], "ballet": [6, 16]}),
 "true-dance-parkovaya": ("True Dance Studio (Первомайская)", "студия танцев", "dance", 4, 16,
    "Первомайская", "610 м", "11-я Парковая ул., 24", (55.794735, 37.806847, "дом", None),
    "+7 (909) 649-62-92", "https://true-dance.ru", None, None,
    "Современные танцы для детей 4–16 лет, K-pop и хип-хоп для подростков; абонемент — от 7 200 ₽",
    "карточка Яндекс Карт («Современные танцы (4-16 лет)», «K-Pop для детей и подростков», «Хип-Хоп для подростков», «Танцы Измайлово — 7200 ₽»)", "true_dance_studio/104904232059", None),
 "milgrad-vladimirskaya": ("Детский центр «Милград» (Перово)", "детский развивающий центр", "singing,dance,drawing,languages,robotics,early", 1, 12,
    "Перово", "400 м", "1-я Владимирская ул., 33, корп. 1", (55.751472, 37.77935, "дом", None),
    "+7 (968) 436-23-58", "https://milgrad.moscow", None, None,
    "Вокал и хореография для детей 4–12 лет, рисование 4–10 лет, английский и робототехника 4–12 лет, «Мама и малыш» с года до трёх; вокальная группа, 8 занятий — 9 600 ₽",
    "карточка Яндекс Карт («Вокал для детей 4-12 лет», «Хореография для детей 4-12 лет», «Рисование для детей 4-10 лет», «Английский для детей 4-12 лет», «Робототехника для детей 4-12 лет», «Раннее развитие 1-3 года», «Вокальная группа, от 4 до 12 лет, 8 занятий — 9600 ₽»)", "milgrad/16135583026",
    {"singing": [4, 12], "dance": [4, 12], "drawing": [4, 10], "languages": [4, 12], "robotics": [4, 12], "early": [1, 3]}),
 "ballet-elion-balashikha": ("Школа танцев «Балет Элион» (Балашиха)", "школа танцев", "ballet,dance", 3, 17,
    "Балашиха", None, "Балашиха, Заречная ул., 31", (55.830068, 37.963729, "дом", None),
    "+7 (966) 982-23-38", None, None, "Этаж: 1",
    "Хореография, балет, джаз, модерн и контемпорари для дошкольников с 3 лет и школьников; абонемент на 8 занятий — от 5 900 ₽, пробное занятие — 500 ₽",
    "карточка Яндекс Карт («ПРОБНОЕ ЗАНЯТИЕ для детей от 3х лет», абонементы «дошкольники 3-4 года», «дошкольники и школьники», «Базовый абонемент 8 занятий — 5900 рублей», «Пробное занятие — 500 ₽», обновлено представителем 6 октября)", "ballet_elion/67612244013", None),
 "tvoy-golos-perovskaya": ("Студия вокала «Твой голос» (Новогиреево)", "студия вокала", "singing", 3, 17,
    "Новогиреево", "1,5 км", "Перовская ул., 66, корп. 7", (55.743466, 37.804233, "дом", None),
    "+7 (926) 777-99-19", "https://tvoi-golos.ru", None, None,
    "Уроки вокала для детей с 3 лет и любого уровня голоса, есть хор; пробный урок на час — 1 500 ₽",
    "карточка Яндекс Карт («Пробные занятия по длительности ЧАС. Мы занимаемся с разным возрастом от 3+» — 1500 ₽)", "tvoy_golos/52392700280", None),
 "vremena-goda-tekstilshchikov": ("Творческий центр «Времена года» (Текстильщики)", "творческий центр", "dance,singing", 3, 17,
    "Текстильщики", "1,3 км", "8-я ул. Текстильщиков, 12, корп. 2", (55.702637, 37.744325, "дом", None),
    "+7 (916) 674-89-57", "https://www.teatrvg.ru", None, None,
    "Хореография для малышей 3–4 лет, группы с 5 и с 12 лет — эстрадный, народный и современный танец; вокал для детей с 5 лет; абонемент 2 раза в неделю — 6 000 ₽ в месяц",
    "карточка Яндекс Карт («Хореография для малышей 3-4 лет — 6000 ₽», «Хореография для детей с 5 лет», «с 12 лет», «Вокал для детей с 5 лет — 6000 ₽»)", "tvorchesky_tsentr_vremena_goda/1058881334",
    {"dance": [3, 17], "singing": [5, 17]}),
 "krylatye-kacheli-krasnogorsk": ("Творческая академия «Крылатые качели» (Красногорск)", "творческая академия", "singing,dance", 5, 17,
    "Красногорск", None, "Красногорск, Вокзальная ул., 17А", (55.813668, 37.338996, "дом", None),
    "+7 (495) 975-94-13", "https://ka4elimusic.ru", None, "Этаж: 1",
    "Вокал для детей с 5 лет в мини-группах и индивидуально, своя студия звукозаписи; хореография для подростков 15–18 лет; пробное занятие на 30 минут — бесплатно",
    "карточка Яндекс Карт («Групповые занятия вокалом для детей от 5 лет. Занятия проходят в мини группах», «Хореография 15-18 лет», «Пробное занятие. Длительность 30 минут - Бесплатно», «Студия звукозаписи!»)", "tvorcheskaya_akademiya_krylatye_kacheli/14002104298",
    {"singing": [5, 17], "dance": [15, 17]}),
 "maximus-elektrostal": ("Танцевальный коллектив «Максимус» (Электросталь)", "школа танцев", "dance", 2, 17,
    "Электросталь", None, "Электросталь, Западная ул., 1Б", (55.771272, 38.431527, "дом", None),
    "+7 (926) 354-52-49", "https://www.maximusdance.ru", None, None,
    "Группы 2–6 и 7–18 лет: детский танец, ритмика, партерная гимнастика, современная хореография, модерн и джаз; занятие — от 600 ₽",
    "карточка Яндекс Карт (возрастные группы «2-6 лет», «7-18 лет», «Детский танец, развитие данных — 600 ₽», «Современная хореография — 700 ₽»)", "maximus/39195066558", None),
 "rykova-dance-kolomna": ("Танцевальная студия Марии Рыковой (Коломна)", "танцевальная студия", "dance", 7, 17,
    "Коломна", None, "Коломна, Уманская ул., 3А", (55.099768, 38.765233, "дом", None),
    "+7 (909) 983-94-15", None, None, "Этаж: 3, зал 319",
    "Детские группы 7–10 лет, Dancehall для 10–13 лет, Girly Hip-Hop с 14 лет; абонемент — 4 000 ₽, пробное занятие — 700 ₽",
    "карточка Яндекс Карт («Возраст: 7-10 лет», «Dancehall Choreo - группа для детей 10-13 лет», «Girly Hip-Hop 14+ — 4000 ₽», «Пробное занятие 700₽», зал 319, этаж 3)", "tantsevalnaya_studiya_marii_rykovoy/193897897988", None),
 "muzykalka-kolomna": ("Музыкальная школа «Музыкалка» (Коломна)", "музыкальная школа", "music,singing", 4, 17,
    "Коломна", None, "Коломна, ул. Октябрьской Революции, 366/2", (55.082869, 38.80095, "дом", None),
    "+7 (925) 485-57-47", "https://muzkolomna.ru", None, None,
    "Вокал, гитара и укулеле для детей, учеников берут с 4 лет; на укулеле с нуля обещают 50 песен за 2 месяца, инструменты дают на занятия",
    "карточка Яндекс Карт («ВОКАЛ ДЛЯ ДЕТЕЙ», «ГИТАРА ДЛЯ ДЕТЕЙ», «УКУЛЕЛЕ ДЛЯ ДЕТЕЙ», «Возраст учеников от 4 до 80 лет», «Инструменты на занятия»)", "muzykalka/177112492117", None),
}

PTP = os.path.join(ROOT, "tools", "creative_1113b_points.json")
ENTR = json.load(open(PTP)) if os.path.exists(PTP) else {}
TAGS = {"dance": "спорт и активность, музыка", "ballet": "спорт и активность, музыка", "singing": "музыка",
        "music": "музыка", "theaterstudio": "сказки и театр, творчество", "drawing": "творчество", "ceramics": "творчество"}


def point(pid):
    """Точка из справки OSM crz-* (tools/creative_1113b_points.json): объект OSM этого места или вход здания;
    иначе — дом по адресу (координаты Яндекс Карт), место скрыто, пока сверка не найдёт вход."""
    v = D[pid]
    lat, lon, lvl, osm = v[8]
    if pid in ENTR:
        e = ENTR[pid]
        if e["level"] == OBJ:
            return e["lat"], e["lon"], f'точно (объект: {e["osm"]}), {e["why"]}, 13.11', OBJ, e
        return e["lat"], e["lon"], f'точно (вход: {e["osm"]}), OSM вход здания {v[7]} — {e["why"]}, 13.11', "вход", e
    return lat, lon, f"точно (дом по адресу {v[7]}, координаты здания — Яндекс Карты); подъезд уточнит сверка", "дом", None


def row(pid):
    name, typ, cats, a0, a1, met, dist, addr, pt, phone, site, hours, how, plus, asrc, ya, ca = D[pid]
    lat, lon, acc, lvl, _ = point(pid)
    first = cats.split(",")[0]
    active = first in ("dance", "ballet")
    r = P(pid, name, typ, met, addr, lat, lon, a0, a1, 45, 90, "активно" if active else "спокойно", TAGS[first],
          None, None, hours, "да", plus, None, adult=1,
          src=(f"Яндекс Карты: карточка организации yandex.ru/maps/org/{ya} (адрес, этаж/вход, телефон, сайт, услуги), 13.11.2026; " if ya else "Яндекс Карты: карточка организации (поиск по названию и адресу), 13.11.2026; ") + f"возраст — {asrc}",
          acc=acc, adult_price=None, booking="обязательна", loud="частично" if active or first in ("music", "singing") else "нет",
          sit="нет" if active else "частично", crowd="нет", food="нет", stroller="частично")
    r["Взрослый билет, ₽"] = None
    r["Сайт"] = site
    r["Категории"] = cats
    r["Как найти"] = how
    r["Проверено (дата)"] = DT
    return r


ROWS = [row(k) for k in D]
TRIAL = {"krylatye-kacheli-krasnogorsk": ("Бесплатное пробное занятие", "Пробное занятие вокалом или хореографией — 30 минут, бесплатно", "https://yandex.ru/maps/org/tvorcheskaya_akademiya_krylatye_kacheli/14002104298")}

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "deals":
        p = os.path.join(ROOT, "deals.json")
        d = json.load(open(p))
        have = {x["id"] for x in d["deals"]}
        n = 0
        for pid, (t, det, url) in TRIAL.items():
            did = pid + "-trial"
            if did not in have:
                d["deals"].append({"id": did, "place_id": pid, "kind": "trial", "title": t, "details": det, "code": "",
                                   "until": "", "url": url, "checked": DT}); n += 1
        json.dump(d, open(p, "w"), ensure_ascii=False, indent=1)
        print("акций", n); sys.exit()
    if mode == "verify":
        out = {}
        for pid in D:
            r = next(x for x in ROWS if x["id"] == pid)
            f = {"address": r["Адрес"], "type": r["Тип"], "cats": r["Категории"], "age_min": r["Возраст от"],
                 "age_max": r["Возраст до"], "booking": "обязательна", "phone": D[pid][9]}
            if r["Сайт"]:
                f["url"] = r["Сайт"]
            if r["Как найти"]:
                f["how"] = r["Как найти"]
            if r["Часы работы"]:
                f["hours"] = r["Часы работы"]
            lat, lon, acc, lvl, _ = point(pid)
            if lvl in (OBJ, "вход"):
                f["point"] = {"lat": lat, "lon": lon, "level": lvl, "how": acc}
            out[pid] = {"fields": f, "src": r["Источник"]}
        print(json.dumps(out, ensure_ascii=False, indent=1)); sys.exit()
    pa = json.load(open(os.path.join(ROOT, "places-all.json")))
    PL = {p["id"] for p in (pa["places"] if isinstance(pa, dict) else pa)}
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    bad = [r["id"] for r in ROWS if r["id"] in existing or r["id"] in PL]
    assert not bad, bad
    if mode == "--dry":
        for r in ROWS:
            print(r["id"], "|", r["Адрес"], "|", r["Широта"], r["Долгота"], "|", r["Точность координат"][:70], "|", r["Сайт"])
        print([k for k in ROWS[0] if k not in hdr]); sys.exit()
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    r0 = ws.max_row + 1
    for n, row_ in enumerate(ROWS):
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=r0 + n, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    cp = os.path.join(ROOT, "auto", "cat-ages.json")
    ca = json.load(open(cp)) if os.path.exists(cp) else {}
    for pid, v in D.items():
        if v[16]:
            ca[pid] = dict(v[16], src=f"{v[14]} (13.11.2026)")
    json.dump(ca, open(cp, "w"), ensure_ascii=False, indent=1)
    print("rows", len(ROWS))
