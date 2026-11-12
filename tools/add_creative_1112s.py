"""Робот creative, 12.11 (запуск 1112s): места из выдач Яндекс Карт по 14 районам (Каховская … Котельники, 7 тем,
auto/pages *-crs<N>-1112s*), карточки организаций (*-cpy<N>-1112s*: рубрика, адрес, этаж/вход, телефон, сайт, услуги с
возрастом групп) и сайты мест из кэша auto/pages. Возраст — только по источнику; «с N лет» без верхней границы → до 17.
Точки — справка OSM crs-* (объект OSM места → «объект»; иначе дом строго по адресу — место скрыто, пока сверка не найдёт вход).
WebFetch не использовался. Запуск: KP_PART=creative python3 tools/add_creative_1112s.py [--dry|deals|verify]"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DT = "2026-11-12"
YA = "https://yandex.ru/maps/org/"
OBJ = "объект"
# id: (название, тип, категории, от, до, метро, до метро, адрес, (lat, lon, уровень, osm), телефон, сайт, часы, как найти,
#      плюс, источник возраста/услуг, карточка Яндекса, cat_ages|None)
D = {
 "elainz-kantemirovskaya": ("Школа танцев «Элайнз»", "школа танцев", "dance", 3, 16,
    "Кантемировская", "450 м", "Кантемировская ул., 39", (55.637459, 37.660584, "дом", None),
    "+7 (903) 183-61-44", "https://www.elainz.ru", None, None,
    "Танцы для детей 3–16 лет: современные стили с 6 лет, брейк-данс, акробатика, группы PRO; первое занятие — пробное, без предварительной оплаты",
    "сайт elainz.ru («занятия для детей 3-16 лет», «ЗАНЯТИЯ ДЛЯ ДЕТЕЙ ОТ 3 ЛЕТ»), карточка Яндекс Карт («для детей от 6 лет»)", "elainz/101991082087", None),
 "tancpol-elektrolitny": ("Студия танцев «ТанцПол»", "школа танцев", "dance", 8, 17,
    "Нагорная", "210 м", "Электролитный пр., 10", (55.672448, 37.61388, "дом", None),
    "+7 (994) 506-34-65", "https://www.dancepole.moscow", None, "Этаж: 3",
    "Детские группы: хип-хоп и спортивный пилон для детей от 8 лет, полотна для детей и подростков",
    "карточка Яндекс Карт («Хип-хоп для детей от 8 лет», «Спортивный пилон для детей от 8 лет»)", "tancpole/1752205179", None),
 "belaya-goncharnaya-nagatinskaya": ("Гончарная мастерская «Белая гончарная»", "гончарная мастерская", "ceramics", 8, 17,
    "Нагатинская", "410 м", "Нагатинская ул., 2", (55.68125, 37.625478, "дом", None),
    "+7 (916) 000-11-17", "https://www.belaya.moscow", "ежедневно 11:00–21:00", "Этаж: 1\nПарковка: бесплатная для автомобилей",
    "Детский керамический курс для 8–12 лет и детский коворкинг для 12–18 лет: гончарный круг, лепка, роспись ангобами",
    "карточка Яндекс Карт («Детский керамический курс», «Возраст набора ‐ от 8 до 12 лет», «детский коворкинг для детей от 12 до 18 лет»), сайт belaya.moscow (часы, парковка)", "white_pottery/140012202449", None),
 "art-pushkin-starosadsky": ("Арт-студия «Пушкин»", "художественная студия", "drawing", 4, 16,
    "Китай-город", "650 м", "Старосадский пер., вл. 7/10", (55.756715, 37.64153, "дом", None),
    "+7 (916) 092-36-52", "https://art-pushkin.ru", None, None,
    "Рисунок и живопись по возрастам: «Малыши» 4–6 лет, «Дети» 7–12, «Подростки» 12–16 и подготовка в художественные вузы; на пробное занятие материалы дают",
    "сайт art-pushkin.ru («4-6 группа Малыши», «7-12 группа Дети», «12-16 группа Подростки»)", "art_studiya_pushkin/7465476372", None),
 "kolibri-andropova": ("Студия «Колибри» (проспект Андропова)", "школа танцев", "dance,ballet", 4, 17,
    "Коломенская", "350 м", "просп. Андропова, 22", (55.68264, 37.661787, "дом", None),
    "+7 (925) 755-99-12", None, None, "Этаж: 3",
    "Балет и танцевальный спорт с 4 лет, хип-хоп и шаффл с 5 лет, K-pop и брейк-данс с 7 лет; занятие — 1 600 ₽",
    "карточка Яндекс Карт («Балет 4+», «Танцевальный спорт 4+», «Hip-hop 5+», «Shuffle 5+», «K-pop 7+», «Breakdance 7+»)", "kolibri/140118361666", None),
 "step-family-kommunarka": ("Школа танцев The Step Family", "школа уличных танцев", "dance", 5, 17,
    "Коммунарка", "920 м", "пос. Коммунарка, ул. Александры Монаховой, 21, стр. 1", (55.570579, 37.476609, "дом", None),
    "+7 (925) 165-36-95", "https://thestepfamily.ru", None, None,
    "Уличные современные танцы для детей от 5 лет: группы 8–10, 10–12, 11–13, 12–15 лет и 13+, по воскресеньям ОФП с акробатикой и растяжка для 7–10 и 11+",
    "сайт thestepfamily.ru («Группы для детей от 5 лет», расписание групп 8-10 … 16+ лет)", None, None),
 "ballet-romanova-kommunarka": ("Студия балета Софии Романовой", "студия балета", "ballet", 2, 12,
    "Коммунарка", "1,96 км", "пос. Коммунарка, ул. Липовый Парк, 4, корп. 3", (55.571423, 37.491045, "дом", None),
    "+7 (993) 363-75-17", "https://balletromanova.ru", None, None,
    "Балет для детей с 2 лет: группы 3–4, 5–6, 7–8, 7–9 и 10–12 лет; первое пробное занятие бесплатно",
    "сайт balletromanova.ru («для детей с 2-х лет», группы «3-4 года» … «10-12 лет», «Первое пробное занятие - БЕСПЛАТНО»)", "ballet_danse_school/89233859762", None),
 "music-star-kommunarka": ("Музыкальная школа Music Star (Коммунарка)", "музыкальная школа", "music,singing", 3, 17,
    "Новомосковская", "1,89 км", "пос. Коммунарка, ул. Липовый Парк, 5, корп. 2", (55.568695, 37.492716, "дом", None),
    "+7 (999) 999-61-74", "https://music-star-school.ru", None, None,
    "Раннее музыкальное развитие для детей 3–6 лет, вокал, гитара, фортепиано, барабаны, саксофон и укулеле для детей; пробный урок 30 минут — 700 ₽",
    "карточка Яндекс Карт («Раннее музыкальное развитие для детей от 3 до 6 лет»), сайт music-star-school.ru («С 3 лет — на направлении «Раннее развитие»», пробный 700 ₽)", "music_star/113373973040", None),
 "polet-kommunarka": ("Детская театральная студия «Полёт»", "детская театральная студия", "theaterstudio", 5, 17,
    "Коммунарка", "1,82 км", "пос. Коммунарка, ул. Липовый Парк, 6А", (55.569988, 37.489248, "дом", None),
    "+7 (993) 703-70-10", "https://www.studiopolet.ru", None, None,
    "Группы 5–6, 7–9 и 10–15 лет («Театр на подоконнике» для 5–6 лет); в конце сезона дети играют в большом спектакле на настоящей сцене",
    "сайт studiopolet.ru («Ребята 5-6 лет», «7-9 лет», «10-15 лет», «Для детей 6 - 17 лет»), карточка Яндекс Карт («Группа для детей от 7 до 17 лет»)", "polet/88914121887", None),
 "la-prima-davydkovskaya": ("Студия балета La Prima (Давыдковская)", "студия балета", "ballet,dance", 3, 17,
    "Славянский бульвар", "700 м", "Давыдковская ул., 3, стр. 2", (55.726446, 37.480543, "дом", None),
    "+7 (965) 230-04-38", "https://laprima-moscow.ru", None, None,
    "Детская хореография для 3–5 лет, балет для детей 4–12 лет и балет для подростков, современный танец и K-pop с 6 лет; пробное занятие бесплатно",
    "карточка Яндекс Карт («Детская хореография 3-5 лет», «Балет для детей 4–12 лет», «Современный танец 6+», «K-pop для детей от 6 лет»), сайт laprima-moscow.ru («Пробное занятие — бесплатно!»)", "ballet_studio_la_prima/9179941233",
    {"ballet": [4, 17], "dance": [3, 17]}),
 "dmsh-98-kronshtadtsky": ("Детская музыкальная школа № 98", "детская музыкальная школа", "music,singing", 1, 17,
    "Коптево", "1,81 км", "Кронштадтский бул., 49А", (55.853016, 37.510942, "дом", None),
    "+7 (495) 456-55-46", "https://98.music.mos.ru", None, None,
    "Городская музыкальная школа: подготовительный класс для детей 5,5–7 лет, вокал, курс «Музыка с мамой» для малышей 1,5–2,5 лет",
    "карточка Яндекс Карт («Подготовительный класс … Возраст: от 5,5 до 7 лет», «ждёт малышей 1,5—2,5 лет», «Возрастная категория: дети, малыши, подростки»)", "detskaya_muzykalnaya_shkola_98/8572084631", None),
 "artkids-kommunarka-skandinavsky": ("Актёрская школа Art Kids Community (Коммунарка)", "актёрская школа", "theaterstudio", 4, 16,
    "Потапово", "1,52 км", "Коммунарка, Скандинавский бул., 9", (55.563824, 37.503307, "дом", None),
    "+7 (916) 744-64-79", "https://artkidscommunity.com", None, None,
    "Актёрское мастерство, сценическая речь и движение для детей 4–7, 7–10 и 10–16 лет; первое полноценное занятие бесплатно",
    "карточка Яндекс Карт (курсы «для детей 4-7 лет», «7-10 лет», «10-16 лет»), сайт artkidscommunity.com («для детей 4-16 лет»)", "art_kids_community/50269620086", None),
}
PTP = os.path.join(ROOT, "tools", "creative_1112s_points.json")
ENTR = json.load(open(PTP)) if os.path.exists(PTP) else {}
TAGS = {"dance": "спорт и активность, музыка", "ballet": "спорт и активность, музыка", "singing": "музыка",
        "music": "музыка", "theaterstudio": "сказки и театр, творчество", "drawing": "творчество", "ceramics": "творчество"}


def point(pid):
    """Точка из справки OSM crs-* (tools/creative_1112s_points.json): объект OSM этого места или вход здания;
    иначе — дом по адресу (координаты Яндекс Карт), место скрыто, пока сверка не найдёт вход."""
    v = D[pid]
    lat, lon, lvl, osm = v[8]
    if pid in ENTR:
        e = ENTR[pid]
        if e["level"] == OBJ:
            return e["lat"], e["lon"], f'точно (объект: {e["osm"]}), OSM по названию, 12.11', OBJ, e
        return e["lat"], e["lon"], f'точно (вход: {e["osm"]}), OSM вход здания {v[7]} — {e["why"]}, 12.11', "вход", e
    return lat, lon, f"точно (дом по адресу {v[7]}, координаты здания — Яндекс Карты); подъезд уточнит сверка", "дом", None


def row(pid):
    name, typ, cats, a0, a1, met, dist, addr, pt, phone, site, hours, how, plus, asrc, ya, ca = D[pid]
    lat, lon, acc, lvl, _ = point(pid)
    first = cats.split(",")[0]
    active = first in ("dance", "ballet")
    r = P(pid, name, typ, met, addr, lat, lon, a0, a1, 45, 90, "активно" if active else "спокойно", TAGS[first],
          None, None, hours, "да", plus, None, adult=1,
          src=(f"Яндекс Карты: карточка организации yandex.ru/maps/org/{ya} (адрес, этаж/вход, телефон, сайт, услуги), 12.11.2026; " if ya else "Яндекс Карты: карточка организации (поиск по названию и адресу), 12.11.2026; ") + f"возраст — {asrc}",
          acc=acc, adult_price=None, booking="обязательна", loud="частично" if active or first in ("music", "singing") else "нет",
          sit="нет" if active else "частично", crowd="нет", food="нет", stroller="частично")
    r["Взрослый билет, ₽"] = None
    r["Сайт"] = site
    r["Категории"] = cats
    r["Как найти"] = how
    r["Проверено (дата)"] = DT
    return r


ROWS = [row(k) for k in D]
TRIAL = {"ballet-romanova-kommunarka": ("Бесплатное пробное занятие балетом", "Первое пробное занятие для ребёнка с 2 лет — бесплатно.", "https://balletromanova.ru"),
         "la-prima-davydkovskaya": ("Бесплатное пробное занятие балетом", "Пробное занятие для детей (хореография с 3 лет, балет 4–12 лет) — бесплатно.", "https://laprima-moscow.ru"),
         "artkids-kommunarka-skandinavsky": ("Первое занятие в актёрской школе — бесплатно", "Полноценный пробный урок актёрского мастерства для детей 4–16 лет — бесплатно.", YA + "art_kids_community/50269620086/")}

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
            ca[pid] = dict(v[16], src=f"{v[14]} (12.11.2026)")
    json.dump(ca, open(cp, "w"), ensure_ascii=False, indent=1)
    print("rows", len(ROWS))
