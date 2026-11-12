"""Робот creative, 12.11 (запуск 1112z): места из выдач Яндекс Карт по 14 районам (Лесопарковая … Марьино, 7 тем,
auto/pages *-cv<N>-1112z*), карточки организаций (*-cc<N>-1112z*: рубрика, адрес, этаж/вход, телефон, сайт, услуги с
возрастом групп) и сайты мест из кэша auto/pages. Возраст — только по источнику; «с N лет» без верхней границы → до 17.
Точки — справка OSM crs-* (объект OSM места → «объект»; иначе дом строго по адресу — место скрыто, пока сверка не найдёт вход).
WebFetch не использовался. Запуск: KP_PART=creative python3 tools/add_creative_1112z.py [--dry|deals|verify]"""
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
 "b-major-nekrasovka": ("Музыкальная студия B-Major (Некрасовка)", "музыкальная студия", "singing,dance,theaterstudio", 3, 17,
    "Некрасовка", "510 м", "Рождественская ул., 27, корп. 1", (55.707284, 37.924203, "дом", None),
    "+7 (916) 708-30-89", "https://nekrasovka.b-major.ru", None, None,
    "Вокал в группах 3–4, 5–6, 7–8 и 9–12 лет, актёрское мастерство 4–17 лет, эстрадный танец 3–6 лет и dance mix с 7 лет, «Школа мюзикла» для 8–14 лет; абонемент раз в неделю — от 4 900 ₽ в месяц; три пробных групповых занятия бесплатно",
    "сайт nekrasovka.b-major.ru (тарифы: «Вокал, 3-4 и 5-6 лет», «Вокал, 7-8 и 9-12 лет», «Актерское мастерство, 4-5 лет», «5-17 лет», «Эстрадный танец, 3-4 года», «5-6 лет», «Dance mix, 7+», «Школа мюзикла 8-11 и 12-14 лет», «3 пробных занятия бесплатно»), карточка Яндекс Карт", "b_major/198967828318",
    {"singing": [3, 12], "dance": [3, 17], "theaterstudio": [4, 17]}),
 "belaya-studio-komsomolsky": ("Хореографическая студия Ксении Белой", "хореографическая студия", "dance,ballet,theaterstudio", 2, 16,
    "Фрунзенская", "170 м", "Комсомольский просп., 24, стр. 2", (55.728256, 37.58031, "дом", None),
    "+7 (926) 476-73-93", "https://belayastudia.ru", None, None,
    "Хореография для малышей с 2 лет, классический танец с 5 лет, современный танец 7–15 лет и актёрское мастерство 4–16 лет; студия работает с 1999 года, дети выступают на театральных площадках Москвы",
    "сайт belayastudia.ru («детей с 2-х до 16 лет», «Хореография для малышей с 2-х лет», «Классический танец с 5-ти лет», «Актерское мастерство с 4 до 16 лет», «Современный танец с 7-ми до 15 лет»; адрес «Комсомольский проспект, д.24, стр.2»), карточка Яндекс Карт", None,
    {"dance": [2, 15], "ballet": [5, 16], "theaterstudio": [4, 16]}),
 "maleeva-ballet-vysotny": ("Студия балета Ксении Малеевой", "студия балета", "ballet", 2, 17,
    "Люблино", "640 м", "Высотный пр., 2/5", (55.680042, 37.757278, "дом", None),
    "+7 (963) 922-88-33", "https://balet-studio-km.ru", None, "Этаж: 2, зал 4",
    "Балет для детей с 2 лет, группы 2–4, 4–6, 6–8 лет и 8+; 8 занятий в месяц — 6 500 ₽, разовое — 1 000 ₽; первое пробное занятие бесплатно",
    "сайт balet-studio-km.ru («группы разных возрастов: 2-4 года; 4-6 лет, 6-8 лет, 8+ лет», адрес «Высотный проезд д.2/5»), карточка Яндекс Карт (цены, «Бесплатное пробное занятие», «4 зал, этаж 2»)", "ksenia_maleeva_ballet_studio/66285876824", None),
 "makarov-dance-marksistsky": ("Школа танцев Александра Макарова (Таганская)", "школа танцев", "dance", 4, 17,
    "Марксистская", "680 м", "Марксистский пер., 3", (55.738475, 37.664617, "дом", None),
    "+7 (916) 494-31-69", "https://makarovdance.ru", None, None,
    "Современные уличные стили для детей от 4 лет: хип-хоп, брейк-данс, K-pop, Girls Style; пробное занятие — 700 ₽, абонемент на 4 занятия — 6 000 ₽",
    "сайт makarovdance.ru («Дети от 4 лет и взрослые», филиал «Таганская Марксистский переулок 3», цены филиала), карточка Яндекс Карт", "shkola_tantsev_aleksandra_makarova/218069637541", None),
 "deti-rayka-michurinsky": ("Театральная студия «Дети райка» (Раменки)", "театральная студия", "theaterstudio", 6, 17,
    "Раменки", "420 м", "Мичуринский просп., 26", (55.699903, 37.500764, "дом", None),
    "+7 (495) 220-84-00", "https://www.detiraika.com", None, None,
    "Группы 6–7, 7–10, 11–13 лет и подростки 14–17: актёрское мастерство, сценическая речь и движение, спектакли и фестивали; раз в неделю по 2 часа, абонемент — 13 990 ₽ в месяц",
    "сайт detiraika.com («от 6 до 17 лет», «Для детей 6-7 лет», «7–10 и 11-13 лет», «Для подростков 14–17 лет», филиал «Мичуринский пр-т, 26»), карточка Яндекс Карт (цена)", "deti_raika/219235052229", None),
 "act-place-leninsky": ("Театральная студия «Акт Плэйс» (Ленинский проспект)", "театральная студия", "theaterstudio", 3, 11,
    "Ленинский проспект", "610 м", "Ленинский просп., 30", (55.710641, 37.58385, "дом", None),
    "+7 (926) 266-95-58", "https://www.act-place.com", None, None,
    "Группы 3–4, 4–6 и 7–11 лет: актёрское мастерство, ораторское искусство, вокал и сценическое движение; раз в неделю по 2 часа, абонемент — 9 000 ₽ в месяц, пробный урок — 1 400 ₽",
    "карточка Яндекс Карт («Театральная студия для детей 3-4 года», «4-6 лет», «7-11 лет», пробный урок 1400 ₽), сайт act-place.com (филиал «Ленинский проспект, 30»)", "act_place/96543064559", None),
 "act-place-lyublinskaya": ("Театральная студия «Акт Плэйс» (Люблинская)", "театральная студия", "theaterstudio", 3, 11,
    "Братиславская", "1,8 км", "Люблинская ул., 78, корп. 3", (55.661796, 37.729592, "дом", None),
    "+7 (903) 008-01-64", "https://www.act-place.com", None, None,
    "Группы 3,5–6 и 7–11 лет: актёрское мастерство, ораторское искусство, вокал и сценическое движение; раз в неделю по 2 часа, абонемент — 9 000 ₽ в месяц, пробный урок — 1 400 ₽",
    "карточка Яндекс Карт («Театральная студия для детей 3,5-6 лет», «7-11 лет», пробный урок 1400 ₽), сайт act-place.com (филиал «ул.Люблинская, 78к3»)", "act_place/171244657655", None),
 "zerno-lyublinskaya": ("Театральная лаборатория «Зерно»", "театральная студия", "theaterstudio", 7, 17,
    "Братиславская", "1 км", "Люблинская ул., 149", (55.663217, 37.742771, "дом", None),
    "+7 (495) 351-59-02", None, None, None,
    "Группы 7–11, 12–14 и 14–17 лет: актёрское мастерство, сценическая речь, импровизация и спектакли; абонемент — 7 000 ₽",
    "карточка Яндекс Карт («студия для детей и подростков 7–17 лет», группы 7-11, 12-14, 14-17 лет, 7000 ₽)", "teatralnaya_laboratoriya_zerno/91638442646", None),
 "prorisunok-tyumensky": ("Художественная школа «Прорисунок»", "художественная школа", "drawing", 4, 17,
    "Бульвар Рокоссовского", "560 м", "Тюменский пр., 3, корп. 7", (55.810799, 37.741684, "дом", None),
    "+7 (916) 404-92-60", "https://proricynok.ru", None, None,
    "Занятия для дошкольников с 4 лет и полный курс для 7–18 лет: живопись, рисунок, композиция и скульптура, 2 раза в неделю — 12 000 ₽ в месяц",
    "сайт proricynok.ru («Занятия для дошкольников от 4 лет», «для детей от 7 до 18 лет»), карточка Яндекс Карт (абонемент 12000 ₽)", "prorisunok/67708617225", None),
 "art-libre-mosfilmovskaya": ("Русско-французская школа живописи Art Libre", "школа живописи", "drawing", 5, 14,
    "Ломоносовский проспект", "660 м", "Мосфильмовская ул., 43/40", (55.710707, 37.50778, "дом", None),
    "+7 (917) 535-19-23", "https://artlibre.ru", None, None,
    "Детские классы для 5–7 и 7–14 лет по будням с 17:00 до 19:00, занятие — 2 000 ₽",
    "сайт artlibre.ru («Детские классы дети 5-7 лет», «Дети 7-14 лет», 17.00-19.00), карточка Яндекс Карт (адрес, «Детские классы для детей и подростков 2 000 ₽»)", "russian_french_school_of_painting_art_libre/74730756059", None),
}
PTP = os.path.join(ROOT, "tools", "creative_1112z_points.json")
ENTR = json.load(open(PTP)) if os.path.exists(PTP) else {}
TAGS = {"dance": "спорт и активность, музыка", "ballet": "спорт и активность, музыка", "singing": "музыка",
        "music": "музыка", "theaterstudio": "сказки и театр, творчество", "drawing": "творчество", "ceramics": "творчество"}


def point(pid):
    """Точка из справки OSM crz-* (tools/creative_1112z_points.json): объект OSM этого места или вход здания;
    иначе — дом по адресу (координаты Яндекс Карт), место скрыто, пока сверка не найдёт вход."""
    v = D[pid]
    lat, lon, lvl, osm = v[8]
    if pid in ENTR:
        e = ENTR[pid]
        if e["level"] == OBJ:
            return e["lat"], e["lon"], f'точно (объект: {e["osm"]}), {e["why"]}, 12.11', OBJ, e
        return e["lat"], e["lon"], f'точно (вход: {e["osm"]}), OSM вход здания {v[7]} — {e["why"]}, 12.11', "вход", e
    if pid == "belaya-studio-komsomolsky":
        return lat, lon, "приблизительно (координаты Яндекс Карт для Комсомольского просп., 24, стр. 1; на сайте студии — стр. 2); вход уточнит сверка", "дом", None
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
TRIAL = {"b-major-nekrasovka": ("Три бесплатных пробных занятия", "Три пробных групповых занятия (вокал, актёрское мастерство, танец для детей с 3 лет) — бесплатно.", "https://nekrasovka.b-major.ru"),
         "maleeva-ballet-vysotny": ("Бесплатное пробное занятие балетом", "Первое пробное занятие в студии балета для детей с 2 лет — бесплатно.", YA + "ksenia_maleeva_ballet_studio/66285876824/")}

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
