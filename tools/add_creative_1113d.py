"""Робот creative, 13.11 (запуск 1113d): места из выдач Яндекс Карт по 15 районам (Пушкинская … Долгопрудный, 7 тем,
auto/pages *-cv<N>-1113d*), карточки организаций (*-cc<N>-1113d*: рубрика, адрес, этаж/вход, телефон, сайт, услуги с
возрастом групп) и сайты мест из кэша auto/pages. Возраст — только по источнику; «с N лет» без верхней границы → до 17.
Точки — справка OSM crs-* (объект OSM места → «объект»; иначе дом строго по адресу — место скрыто, пока сверка не найдёт вход).
WebFetch не использовался. Запуск: KP_PART=creative python3 tools/add_creative_1113d.py [--dry|deals|verify]"""
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
 "keydance-mitino": ("Студия танцев KeyDance (Митино)", "школа танцев", "dance", 4, 17,
    "Пятницкое шоссе", "640 м", "Митинская ул., 45, корп. 2", (55.850449, 37.350782, "дом", None),
    "+7 (965) 229-62-19", "https://keydance.ru", None, None,
    "Хип-хоп для детей 4–15 лет и брейк-данс с 4 лет, контемпорари и шаффл для 6–14 лет, хаус с 7 лет; абонемент на месяц — 7 200 ₽; пробное занятие — бесплатно",
    "карточка Яндекс Карт («Хип-хоп 4-15 лет», «Брейк-данс для детей от 4х лет», «Контемп 6-14 лет», «Шаффл 6-14 лет», «Хаус 7+», «7200 ₽ 30 д», «Пробное занятие БЕСПЛАТНО», обновлено представителем 28 августа) и сайт keydance.ru («Направлений для детей от 4 лет»)", "keydance_studio/75557718179", None),
 "dmsh-molchanova-klinskaya": ("Детская музыкальная школа им. К. В. Молчанова (Ховрино)", "детская музыкальная школа", "music,singing,drawing,theaterstudio", 3, 17,
    "Ховрино", "1,6 км", "Клинская ул., 8А", (55.869612, 37.497917, "дом", None),
    "+7 (495) 451-31-65", "https://molchanov.music.mos.ru", None, "Этаж: 1",
    "Фортепиано, скрипка, виолончель, флейта, саксофон, гитара, баян, домра и вокал — индивидуально (8 занятий — 10 000–12 000 ₽), ИЗО-студия — 7 500 ₽ в месяц, театр и сценическая речь — 8 600 ₽; музыкальные группы с 3 лет вместе с мамой и для 4–6 лет",
    "карточка Яндекс Карт (платные услуги школы: «Группы для детей от 3 х лет (с мамами)», «Групповые занятия для детей 4-6 лет», «Изо-студия для детей — 7500 ₽», «Театр, сценическая речь — 8600 ₽», инструменты и вокал «для детей и взрослых»; обновлено представителем 3 сентября)", "gosudarstvennoye_byudzhetnoye_uchrezhdeniye_dopolnitelnogo_obrazovaniya_goroda_moskvy_detskaya_muzykalnaya_shkola_im_k_v_molchanova/1015228544", None),
 "artpozitiv-mira": ("Школа искусств «Artпозитив» (просп. Мира)", "детская школа искусств", "drawing", 4, 14,
    "Ростокино", "680 м", "просп. Мира, 198, корп. 2", (55.837414, 37.66229, "дом", None),
    "+7 (980) 469-55-20", None, None, "Этаж: 1",
    "ИЗО в группах 4–6, 6–9 и 10–14 лет, основы дизайна и графической композиции; занятие 2 академических часа — 1 000 ₽",
    "карточка Яндекс Карт («ИЗО для детей 4-6 лет», «ИЗО для детей 6-9 лет», «ИЗО для детей 10-14 лет», «2 ак.час — 1000 ₽», обновлено 2 октября)", "artpozitiv/143575906153", None),
 "zhdanova-ballet-salarevo": ("Студия балета Ирины Ждановой (Саларьево)", "студия балета", "ballet,dance", 2, 17,
    "Саларьево", "1,2 км", "Саларьевская ул., 16, корп. 4", (55.618207, 37.407519, "дом", None),
    "+7 (978) 792-03-25", "https://baletsalarevo.tb.ru", None, None,
    "Классический балет для детей с 3 лет с отчётным концертом на большой сцене (12 ак. часов — 9 600 ₽), современный танец с 3 лет (8 ак. часов — 7 600 ₽) и «Танец с мамой» для малышей с 2 лет",
    "карточка Яндекс Карт («Балет для детей 3+ — 9600 ₽», «Современный танец для детей 3+ — 7600 ₽», «Танец с мамой 2+», обновлено 24 августа)", "irina_zhdanova_ballet_studio/238006209579",
    {"ballet": [3, 17], "dance": [2, 17]}),
 "splash-sensaciya-dolgoprudny": ("Хореографический коллектив «Splash-Сенсация» (Долгопрудный)", "школа танцев", "dance", 4, 15,
    "Физтех", "3,1 км", "Долгопрудный, пл. Собина, 3", (55.934059, 37.514212, "дом", None),
    "+7 (916) 081-62-56", "https://splash-dance.ru", None, None,
    "Эстрадный и современный танец, джаз, хип-хоп, классическая хореография, партерная гимнастика и акробатика; группы 4–5, 4–6, 6–7, 7–9, 9–11 и 13–15 лет; абонемент на месяц (8 часов) — 5 500 ₽; пробное занятие — бесплатно",
    "карточка Яндекс Карт («Наша школа танцев приглашает детей с 4-х лет», «5500 ₽ 8 ч») и сайт splash-dance.ru (расписание групп «Первогодки (4-5 лет)», «Новички (4-6 лет)», «Подготовишки (6-7 лет)», «Младшие (7-9 лет)», «Средние (9-11 лет)», «Взрослые (13-15 лет)», «Бесплатное пробное занятие»)", "dance_school_splash_sensaciya/1063955262", None),
 "chunikhin-musical-dolgoprudny": ("Школа мюзикла Стаса Чунихина (Долгопрудный)", "школа мюзикла", "theaterstudio,singing", 3, 15,
    "Физтех", "4,1 км", "Долгопрудный, просп. Ракетостроителей, 5, корп. 1", (55.932969, 37.500639, "дом", None),
    "+7 (931) 899-78-14", "https://musical-school.ru", None, "Этаж: 1",
    "Мюзикл, актёрское мастерство и вокал: группы 3,5–5, 5–7 и 8–11 лет, подростковый мюзикл 12–15 лет; месяц в группе 3,5–5 лет — от 3 900 ₽, в группах 5–7 и 8–11 лет — 8 200 ₽",
    "карточка Яндекс Карт («Начинающая группа 3,5-5 лет — 3900/5500 ₽», «Младшая группа 5-7 лет — 8200 ₽», «Старшая группа 8-11 лет — 8200 ₽», «детская вокальная студия, группы 5-7 и 8-11 лет») и сайт musical-school.ru («принимаем детей в возрасте от 3,5 до 15 лет», «Подростки Мюзикл 12-15 лет»)", "shkola_myuzikla_stasa_chunikhina/4328303986",
    {"theaterstudio": [3, 15], "singing": [5, 11]}),
 "artdom-ramenskoe": ("Художественная студия «Артдом» (Раменское)", "художественная студия", "drawing", 5, 15,
    "ДК Орбита", "320 м", "Раменское, ул. Гурьева, 1Д, корп. 1", (55.576559, 38.24377, "дом", None),
    "+7 (916) 836-18-52", "https://artdomram.ru", "Пн, Пт 12:00–19:00; Сб 11:00–17:30; Вс 12:00–19:00", None,
    "Рисование для детей 5–15 лет в мастерской до 6–7 человек, по индивидуальной программе; детские занятия — пн и пт 12:00–15:00, сб 11:00–17:30; разовое занятие — 700 ₽ за час, 1 100 ₽ за 3 часа, абонементы на 4 занятия — от 2 200 ₽",
    "сайт artdomram.ru («Занятия для детей от 5 - 15 лет», расписание и цены «Разовое посещение для детей от 5-15 лет: 700 руб. - 1 час … 1100 руб. - 3 часа», «4 занятия по 1 часу - 2200 рублей»)", None, None),
}

PTP = os.path.join(ROOT, "tools", "creative_1113d_points.json")
ENTR = json.load(open(PTP)) if os.path.exists(PTP) else {}
TAGS = {"dance": "спорт и активность, музыка", "ballet": "спорт и активность, музыка", "singing": "музыка",
        "music": "музыка", "theaterstudio": "сказки и театр, творчество", "drawing": "творчество", "ceramics": "творчество"}


def point(pid):
    """Точка из справки OSM crz-* (tools/creative_1113d_points.json): объект OSM этого места или вход здания;
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
TRIAL = {"keydance-mitino": ("Бесплатное пробное занятие танцами", "Студия KeyDance в Митино: первое пробное занятие для детей от 4 лет — бесплатно (хип-хоп, брейк-данс, контемпорари)", "https://yandex.ru/maps/org/keydance_studio/75557718179/"),
         "splash-sensaciya-dolgoprudny": ("Бесплатное пробное занятие в «Splash-Сенсации»", "Хореографический коллектив в Долгопрудном приглашает детей с 4 лет на бесплатное пробное занятие", "https://splash-dance.ru/")}

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
