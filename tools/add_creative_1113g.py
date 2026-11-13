"""Робот creative, 13.11 (запуск 1113g): места из выдач Яндекс Карт по 15 районам (Текстильщики … Чехов, 7 тем,
auto/pages *-cv<N>-1113g*), карточки организаций (*-cc<N>-1113g*: рубрика, адрес, этаж/вход, телефон, сайт, услуги с
возрастом групп) и сайты мест из кэша auto/pages. Возраст — только по источнику; «с N лет» без верхней границы → до 17.
Точки — справка OSM crs-* (объект OSM места → «объект»; иначе дом строго по адресу — место скрыто, пока сверка не найдёт вход).
WebFetch не использовался. Запуск: KP_PART=creative python3 tools/add_creative_1113g.py [--dry|deals|verify]"""
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
 "etual-dmitrovskoe": ("Балетная школа «Этуаль» (Дмитровское шоссе)", "балетная школа", "ballet", 3, 17,
    "Петровско-Разумовская", "790 м", "Дмитровское ш., 33, стр. 5", None,
    "+7 (977) 508-74-51", "https://etual-balet.ru", None, "Ориентир: здание Дома культуры «Нега» (Дмитровское ш., 33, стр. 5)",
    "Классический балет для детей: группы от 3 лет и от 7 лет, занятие — 1 000 ₽; есть уроки классического танца для взрослых",
    "карточка Яндекс Карт («Балет для детей от 3-х лет — 1000 ₽»; здание по адресу в OSM — Дом культуры «Нега», relation/1842766, «Балет для детей от 7 лет — 1000 ₽», «Урок классического танца для взрослых — 1375 ₽»)", "etoile/199287945881", None),
 "dmtya-studio-tsvetnoy": ("Театральная студия ДМТЮА (Цветной бульвар)", "детская театральная студия", "theaterstudio", 4, 17,
    "Цветной бульвар", "490 м", "Цветной бул., 30, стр. 1", None,
    "+7 (495) 625-19-59", "https://dmtya.ru", None, "Вход: через бизнес-центр\nЭтаж: 3, офис 302",
    "Студия Детского музыкального театра юного актёра: актёрское мастерство, вокал, хоровое пение и хореография. Группа 4–6 лет — пн и ср 11:00–13:15 (15 000 ₽), группа 7–17 лет — дважды в неделю, зачисление по прослушиванию (18 000 ₽); первые 2 занятия — бесплатно",
    "карточка Яндекс Карт («Театральная студия ДМТЮА 4–6 лет — Цветной бульвар … Занятия по понедельникам и средам, 11:00–13:15: актёрское мастерство, вокал, хоровое пение и хореография — 15000 ₽», «7–17 лет … Первые 2 занятия — бесплатно … зачисление — по прослушиванию — 18000 ₽», «Вход через Бизнес-центр, этаж 3, офис 302», обновлено 6 октября)", "teatralnaya_studiya_dmtyua/224500555361", None),
 "domik-hudozhnika-fabritsiusa": ("Студия «Домик художника» (Южное Тушино)", "художественная студия", "drawing,ceramics", 4, 12,
    "Сходненская", "670 м", "ул. Фабрициуса, 22", None,
    "+7 (985) 604-29-84", "https://domikhudoznika.ru", None, "Этаж: 1",
    "Рисование для детей: курс «От сказки к шедевру» для 4–6 лет и «Искусство и художники» для 7–12 лет; каллиграфия для 5–9 лет (1 800 ₽); керамика — дети лепят из глины и расписывают ангобами, обжиг в студии (2 500 ₽); первое пробное занятие — 1 500 ₽",
    "сайт domikhudoznika.ru («От сказки к шедевру» — рисование для детей от 4 до 6 лет», «Искусство и художники» — рисование для детей от 7 до 12 лет», «Сказочная каллиграфия 5-6 лет», «Игра в каллиграфию 7-9 лет», «первое пробное 1500Р», «студия переехала в новое помещение по адресу: ул.Фабрициуса, д.22») и карточка Яндекс Карт («Керамика детям и взрослым — 2500 ₽», «Каллиграфия — 1800 ₽», этаж 1)", "domik_hudozhnika/80818882621", None),
 "chudo-tsveta-dmitrov": ("Творческая студия «Чудо цвета» (Дмитров)", "творческая студия", "ceramics", 3, 7,
    "Выставочный центр (остановка)", "540 м", "Дмитров, ул. Подлипичье, 6", None,
    "+7 (916) 255-57-74", None, None, "Этаж: 1",
    "Лепка для дошкольников: курс «Пластилиновые открытия» для детей от 3,7 до 6 лет (1 050 ₽) и кружок «Глиняные открытия» для 4–7 лет — фигурки, игрушки и посуда из природной глины (900 ₽)",
    "карточка Яндекс Карт («Пластилиновые открытия. Развивающий курс для детей от 3,7 до 6 лет — 1050 ₽», «Глиняные открытия. Развивающий кружок для детей от 4 до 7 лет — 900 ₽», этаж 1, обновлено 26 октября)", "studiya_chudo_tsveta/223751830739", None),
 "dinamo-dance-chekhov": ("Школа танцев «Динамо» (Чехов)", "школа танцев", "dance", 6, 17,
    "Полиграфический комбинат (остановка)", "280 м", "Чехов, ул. Полиграфистов, 1, стр. 2", None,
    "+7 (977) 380-76-17", "https://dancechekhov.clients.site", None, None,
    "Набор детей в школу танцев с 6 лет, занятие — 700 ₽; есть занятия актёрским мастерством (800 ₽)",
    "карточка Яндекс Карт («Школа Танцев — Набор детей от 6 лет — 700 ₽», «Актерское Мастерство — 800 ₽»)", "dynamo_chekhov/46358571270", None),
 "sing-play-khoroshevskoe": ("Музыкальная школа Sing & Play (Хорошёвское шоссе)", "музыкальная школа", "music,singing", 4, 17,
    "Полежаевская", "550 м", "Хорошёвское ш., 23, корп. 2", None,
    "+7 (499) 715-30-41", "https://singplay.ru", None, None,
    "Для детей от 4 лет: вокал, фортепиано, гитара, укулеле, барабаны, скрипка, флейта, саксофон, труба — урок 2 100 ₽; есть пробное занятие",
    "сайт singplay.ru («Музыкальная школа для взрослых и детей», «Для любого возраста (от 4 лет)», «Вокал для детей», «Скрипка для детей» и др.) и карточка Яндекс Карт («Вокал — 2100 ₽», «Фортепиано — 2100 ₽», «Пробное занятие»)", "sing_play/18705930566", None),
 "em-dance-volokolamskoe": ("Школа танцев E.M. Dance (Волоколамское шоссе)", "школа танцев", "dance", 3, 17,
    "Спартак", "700 м", "Волоколамское ш., 71, корп. 2", None,
    "+7 (985) 977-41-55", "https://em-dance.ru", None, None,
    "Эстрадный, классический танец, современная хореография и акробатика для детей 3–18 лет, своя программа для каждого возраста; абонемент 3 раза в неделю по 90 минут — 12 800 ₽, акробатика раз в неделю по 120 минут — 6 600 ₽",
    "сайт em-dance.ru («Мы принимаем учеников от 3 до 18 лет. Для каждого возраста — своя программа») и карточка Яндекс Карт («Абонемент 3 раз в неделю по 90 мин. — 12800 ₽», «Акробатика 1 раз в неделю по 120 мин. — 6600 ₽», «Эстрадный танец / Классический танец / Современная хореография / Акробатика»)", "e_m_dance/166635854070", None),
 "starset-klin": ("Студия музыки Starset (Клин)", "музыкальная студия", "singing,music", 6, 17,
    "Бородинский проезд (остановка)", "20 м", "Клин, Бородинский пр., 17А", None,
    "+7 (916) 000-41-81", "https://starsetschool.ru", None, "Помещение: офис 6",
    "Детские вокальные группы с 6 лет и индивидуальный вокал; гитара, фортепиано и скрипка для детей с 6 лет; 8 индивидуальных уроков в месяц — 11 000 ₽; первый урок — бесплатно; отчётные концерты каждые 3 месяца",
    "сайт starsetschool.ru («Детские вокальные группы — с 6 лет, взрослые — с 16 лет», «гитара, фортепиано и скрипка для детей с 6 лет и взрослых», «Первый урок — бесплатно», «отчётный концерт каждые 3 месяца») и карточка Яндекс Карт («Индивидуальные уроки Вокала для взрослых и детей. 8 занятий в месяц … Первый пробный урок - БЕСПЛАТНО! — 11000 ₽», офис 6)", "starset/196129996446", None),

}
PTP = os.path.join(ROOT, "tools", "creative_1113g_points.json")
ENTR = json.load(open(PTP)) if os.path.exists(PTP) else {}
_X = json.load(open(os.path.join(ROOT, 'tools', 'creative_1113g_ext.json')))
_IDS = json.load(open(os.path.join(ROOT, 'tools', 'creative_1113g_ids.json')))
YLL = {v: _X[k]['ll'] for k, v in _IDS.items() if k in _X and _X[k].get('ll')}
TAGS = {"dance": "спорт и активность, музыка", "ballet": "спорт и активность, музыка", "singing": "музыка",
        "music": "музыка", "theaterstudio": "сказки и театр, творчество", "drawing": "творчество", "ceramics": "творчество"}


def point(pid):
    """Точка из справки OSM crz-* (tools/creative_1113g_points.json): объект OSM этого места или вход здания;
    иначе — дом по адресу (координаты Яндекс Карт), место скрыто, пока сверка не найдёт вход."""
    v = D[pid]
    if pid in ENTR:
        e = ENTR[pid]
        if e["level"] == OBJ:
            return e["lat"], e["lon"], f'точно (объект: {e["osm"]}), {e["why"]}, 13.11', OBJ, e
        return e["lat"], e["lon"], f'точно (вход: {e["osm"]}), OSM вход здания {v[7]} — {e["why"]}, 13.11', "вход", e
    lat, lon = YLL[pid]
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
TRIAL = {"dmtya-studio-tsvetnoy": ("Первые 2 занятия бесплатно в театральной студии ДМТЮА", "Театральная студия Детского музыкального театра юного актёра на Цветном бульваре: для детей 7–17 лет первые 2 занятия (актёрское мастерство, вокал, хор, хореография) — бесплатно; зачисление по прослушиванию", "https://yandex.ru/maps/org/teatralnaya_studiya_dmtyua/224500555361/"),
         "starset-klin": ("Бесплатный первый урок в студии Starset", "Студия музыки Starset в Клину: первый урок вокала, гитары, фортепиано или скрипки — бесплатно; детские группы с 6 лет", "https://starsetschool.ru/")}

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
