"""Робот creative, 12.11 (запуск 1112q): места из выдач Яндекс Карт по 15 районам (Нахимовский проспект … Новоясеневская,
Балашиха, Химки, Подольск; ключи cv<N>-1112q), карточки организаций (cc<N>-1112q: рубрика, адрес, этаж/вход, телефон,
сайт, услуги с возрастом групп и ценой), адресные страницы Яндекс Карт (ca<N>-1112q: координаты здания) и сайты мест
из кэша auto/pages. Возраст — только по источнику; «с N лет» без верхней границы → до 17.
Точки — справка OSM crq-* (объект OSM места → «объект»; вход здания по адресу → «вход»; иначе дом по адресу — место
скрыто, пока сверка не найдёт вход). WebFetch не использовался.
Запуск: KP_PART=creative python3 tools/add_creative_1112q.py [--dry|deals|verify|points]"""
import json, os, re, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC
from creative_1112q_sel import SEL
from add_batch14 import MET
STATIONS = {n.lower().replace("ё", "е") for n, a, b in MET}

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DT = "2026-11-12"
YA = "https://yandex.ru/maps/org/"
E = json.load(open(os.path.join(ROOT, "tools/creative_1112q_ext.json")))
N = {v: k for k, v in SEL.items()}
# id: (название, тип, категории, от, до, сайт|None, как найти|None, плюс, источник возраста/услуг, cat_ages|None)
D = {
 "musicclasses-lipchanskogo": ("Музыкальные классы (Некрасовка)", "музыкальная школа", "music,singing", 5, 17, "https://musicclasses.ru", None,
    "Раннее музыкальное развитие для детей 5–6 лет и общеразвивающая программа с 7 лет; фортепиано, гитара, укулеле, вокал — индивидуальное занятие 45 минут — 2 000 ₽",
    "сайт musicclasses.ru («Раннее музыкальное развитие детей 5-6 лет», «Общеразвивающая программа с 7 лет»), карточка Яндекс Карт (услуги и цены)", None),
 "active-style-zeleny": ("Школа танцев Active Style (Новогиреево)", "школа танцев", "dance", 4, 15, None,
    "Вход: Окружной общественный центр им. Моссовета",
    "Хип-хоп для детей: группы 4–6, 6–8, 7–11, 9–12 лет и юниоры 12–15 лет; абонемент 2 раза в неделю — 6 600 ₽, 3 раза — 7 800 ₽ в месяц",
    "карточка Яндекс Карт («HIP-HOP для детей 4-6 лет», «6-8 лет», «7-11 лет», «9-12 лет», «HIP-HOP для юниоров 12-15 лет», цены 6600/7800 ₽, адрес «Зелёный просп., 59А, Окружной общественный центр им. Моссовета»)", None),
 "zhete-novokosino-gorodetskaya": ("Школа балета «Жете» (Новокосино)", "школа балета", "ballet,dance", 3, 17, "https://jete-school.ru", None,
    "Детский танец для малышей 3–6 лет, классический танец с пуантами с 10 лет, современная хореография и народно-характерный танец с 9 лет",
    "сайт jete-school.ru («Детский танец (3-6 лет)», «станок, экзерсис, пуанты (с 10 лет)», «современная хореография для детей от 9 лет», «характерный танец для детей с 9 лет», филиал «Новокосино», «Городецкая, 10Б»), карточка Яндекс Карт", None),
 "first-dance-academy-reutov": ("Первая танцевальная академия (Реутов)", "школа танцев", "dance", 3, 17, "https://fdacademy.ru",
    "Вход: через лицей № 4",
    "Бальные танцы для детей с нуля (группы 5–8 лет, 8 занятий — 6 400 ₽) и продолжающие группы с 6 лет с выступлениями на соревнованиях (12 занятий — 7 800 ₽), хореография; берут детей с 3 лет",
    "сайт fdacademy.ru («мы принимаем детей от 3 лет», адрес «Котовского, 13»), карточка Яндекс Карт («Группы для детей 5-8 лет», «Бальные танцы для детей с 6 лет», цены, «вход в лицей №4»)", None),
 "viartfam-suzdalskaya": ("Студия танцев ViArtfam (Новокосино)", "студия танцев", "dance", 3, 17, "https://www.viartdance.com",
    "Вход: со стороны парковки\nЭтаж: цокольный",
    "Детский танец 3–5 лет, хип-хоп, брейк-данс и современный танец для детей 5–17 лет; детский хип-хоп 2 раза в неделю — 6 000 ₽ в месяц, пробное занятие — 500 ₽",
    "сайт viartdance.com («Дети 3–5 лет», «Группы для детей 5–17 лет», «Дети 6–16 лет», адрес «Суздальская»), карточка Яндекс Карт (цены, «Вход со стороны парковки, этаж цокольный»)", None),
 "raduga-hor-reutov": ("Музыкальная хоровая школа «Радуга» (Реутов)", "хоровая школа", "singing", 5, 17, "https://radugahor.ru", None,
    "Хоровая школа: в подготовительные группы принимают детей 5–7 лет, в основное отделение — 6,5–9 лет; от метро «Новокосино» пешком около 5 минут",
    "сайт radugahor.ru («принимаются дети 5-7 лет», «принимаются дети 6,5-9 лет», «От станции метро \"Новокосино\" … пешком 5 мин.»), карточка Яндекс Карт", None),
 "ramos-vocal-reutov": ("Школа вокала Юлии Рамос (Реутов)", "школа вокала", "singing", 5, 11, "https://shkola-vokala-ramos.clients.site",
    "Этаж: цокольный (-1)",
    "Вокал для детей 5–11 лет: индивидуальные уроки постановки голоса, подготовка в музыкальную школу; урок — 3 000 ₽, детский абонемент на 8 занятий — 24 000 ₽",
    "карточка Яндекс Карт («Дети вокал 5-11 лет», «Абонемент дети от 5-11 лет», «Уроки вокала для детей от 6 лет — 3000 ₽», «Абонемент Дети на 8 занятий — 24000 ₽», «этаж -1»)", None),
 "testa-dance-pavlovsky": ("Школа танцев Testa Dance Show (Серпуховская)", "школа танцев", "dance", 3, 17, "https://school.testa-dance.ru",
    "Вход: напротив 2-го Павловского переулка",
    "Детская хореография, брейк-данс, современные и афро-танцы для детей и подростков 3–17 лет, отчётные концерты; у школы 13 филиалов",
    "сайт school.testa-dance.ru («20 лет · 13 филиалов · 3–17 лет», «Дети от 3 до 17 лет»), карточка Яндекс Карт (направления, «Вход напротив 2-го Павловского переулка»)", None),
 "dshi-rimsky-korsakov-novogireevo": ("ДШИ им. Н. А. Римского-Корсакова (Новогиреевская ул.)", "детская школа искусств", "music", 4, 17, None, None,
    "Программа раннего эстетического развития «Ладушки» для 4–5 лет (музыкальная грамота, хор, ритмика, рисование) — 5 600 ₽, подготовка к поступлению для 5–6 лет — 7 500 ₽, фортепиано для 6–17 лет — 6 000 ₽",
    "карточка Яндекс Карт (услуги: «Ладушки … Возраст: 4-5 лет», «Подготовка к школе … Возраст: 5-6 лет», «Уроки игры на фортепиано … Возраст: 6-17 лет», цены)", None),
 "istok-art-lukinskaya": ("Арт-студия «Исток» (Новопеределкино)", "арт-студия", "drawing", 6, 14, "https://art-studio-eu.ru", None,
    "Рисование для детей 6–14 лет в группах 6–8 и 9–14 лет; проводят детские дни рождения с росписью и картиной акрилом",
    "сайт art-studio-eu.ru («Дети от 6 до 14 лет», «Группы от 6 до 8 лет и группы от 9 до 14 лет», адрес «Лукинская»), карточка Яндекс Карт", None),
 "planeta-vocal-melnikova": ("Школа вокала и барабанов Planeta (Пролетарская)", "музыкальная школа", "singing,music", 4, 17, "https://planeta-vocal.ru", None,
    "Вокал и барабаны для детей от 4 лет, абонементы на 4 занятия; пробное занятие по вокалу или барабанам — 1 000 ₽",
    "сайт planeta-vocal.ru («по вокалу и барабанам со взрослыми и детьми от 4 лет», адрес «Мельникова»), карточка Яндекс Карт («Абонемент на 4 занятия по вокалу для детей», «по барабанам для детей», пробное 1000 ₽)", None),
 "x-temp-saltykovskaya": ("Студия танцев X-temp (Новокосино)", "студия танцев", "dance", 2, 17, "https://x-temp.ru", "Вход: через ТЦ «Авалон»\nЭтаж: 2",
    "Baby dance для малышей от 2,5 лет (можно с родителями), хип-хоп для детей 4–6 и 7–10 лет и юниоров 11–17, K-pop 8–17 лет; занятие baby dance — 800 ₽, пробное детское — бесплатно",
    "сайт x-temp.ru («Хип-хоп ДЕТИ 4 – 6 лет», «7 – 10 лет», «ЮНИОРЫ 11 – 17 лет», «K-POP 8-17 лет», адрес «Салтыковская»), карточка Яндекс Карт («Baby dance … от 2,5 лет», «Ритмика (2,5 - 4 года)», «Бесплатное пробное занятие», «этаж 2»)", None),
 "impulse-dance-korolev": ("Танцевальная студия Impulse (Королёв, просп. Космонавтов, 37Б)", "танцевальная студия", "dance", 7, 17, "https://impulsedsc.ru", None,
    "Хип-хоп, брейкинг, K-pop, джаз-фанк и современная хореография; в этом зале — группы для детей 7+ (младшие 3+ занимаются в соседнем филиале на Космонавтов, 34Б)",
    "сайт impulsedsc.ru («Королёв, пр-кт Космонавтов 37 Б ( 7+ )», «пр-кт Космонавтов 34 Б ( 3+ )»), карточка Яндекс Карт (направления)", None),
 "sinergiya-music-balashikha": ("Школа музыки «Синергия» (Балашиха)", "школа музыки", "music,singing", 5, 17, "https://synergymusicschool.ru",
    "Вход: через ТРЦ «Галион»\nЭтаж: 3",
    "Фортепиано, музыка и пение для детей с 5 лет, группы 5–10 и 11–17 лет",
    "сайт synergymusicschool.ru («У нас можно заниматься детям с 5 лет», «5-10 лет», «11-17 лет»), карточка Яндекс Карт («Занятия для детей: музыка, фортепиано, пение», «этаж 3»)", None),
 "dom-khudozhnikov-khimki": ("Школа живописи «Дом художников» (Химки)", "школа живописи", "drawing", 5, 16, "https://www.art-ris.ru", None,
    "Живопись и ИЗО для детей 5–6 лет (45 минут — 600 ₽), живопись и рисунок 7–10 лет (60 минут — 800 ₽), группа 11–16 лет и архитектурные курсы",
    "карточка Яндекс Карт («Живопись, ИЗО для 5-6 лет — 600 ₽», «Живопись, рисунок 7-10 лет — 800 ₽», «Группа 11-16 лет», «Архитектурные курсы для детей»), сайт art-ris.ru («Школа живописи \"Дом художников\" в Химках»)", None),
 "bely-slon-khimki": ("Арт-студия «Белый слон» (Химки)", "арт-студия", "drawing,ceramics", 5, 12, "https://www.bely-slon.ru",
    "Этаж: 2, офис 33",
    "ИЗО и керамика для детей 5–12 лет: ИЗО — 900 ₽ за час, абонемент ИЗО + керамика на 8 занятий — 6 800 ₽; бывают мастер-классы на гончарном круге",
    "сайт bely-slon.ru («от 5 до 12 лет», «(5-12 лет)», адрес «Совхозная»), карточка Яндекс Карт (цены «Дети: ИЗО разовый 1 час — 900 ₽», «ИЗО+Керамика абонемент 8 занятий — 6800 ₽», «офис 33, этаж 2»)", None),
 "starlight-podolsk": ("Детский музыкальный театр-студия StarLight (Подольск)", "театр-студия", "theaterstudio,singing", 3, 17, None, None,
    "Детский музыкальный театр Андрея Гаркунова: группы Star Kids Lab для малышей 3–5 лет, кастинг в театр для детей постарше, киношкола и блогинг 8+",
    "карточка Яндекс Карт («Набор в группы Star Kids Lab для детей 3–5 лет», «STAR.KIDS.LAB 3+», «КиноШкола и Блогинг 8+», «детский музыкальный театр»)", None),
}
TAGS = {"dance": "спорт и активность, музыка", "ballet": "спорт и активность, музыка", "singing": "музыка",
        "music": "музыка", "theaterstudio": "сказки и театр, творчество", "drawing": "творчество", "ceramics": "творчество"}
PTP = os.path.join(ROOT, "tools", "creative_1112q_points.json")
PT = json.load(open(PTP)) if os.path.exists(PTP) else {}


def info(pid):
    return E[str(N[pid])]


def addr(pid):
    o = info(pid)
    a = o["addr"].replace(", Москва", "").replace("Москва, ", "")
    if a.endswith(", Москва"): a = a[:-8]
    if a.endswith(", Химки"): a = "Химки, " + a[:-7]
    return a


def point(pid):
    o = info(pid)
    lat, lon = o["ll"]
    if pid in PT:
        e = PT[pid]
        if e["level"] == "объект":
            return e["lat"], e["lon"], f'точно (объект: {e["osm"]}), {e["why"]}, 12.11', "объект"
        return e["lat"], e["lon"], f'точно (вход: {e["osm"]}), {e["why"]}, 12.11', "вход"
    return lat, lon, f"точно (дом по адресу {addr(pid)}, координаты здания — Яндекс Карты); вход уточнит сверка", "дом"


def row(pid):
    name, typ, cats, a0, a1, site, how, plus, asrc, ca = D[pid]
    o = info(pid)
    lat, lon, acc, lvl = point(pid)
    first = cats.split(",")[0]
    active = first in ("dance", "ballet")
    metro = o.get("metro") if (o.get("metro") or "").lower().replace("ё", "е") in STATIONS else None
    r = P(pid, name, typ, metro, addr(pid), lat, lon, a0, a1, 45, 90, "активно" if active else "спокойно", TAGS[first],
          None, None, None, "да", plus, None, adult=1,
          src=f"Яндекс Карты: карточка организации {('yandex.ru/maps/org/' + o['org']) if o.get('org') else '(поиск по названию и адресу)'} (адрес, этаж/вход, телефон, сайт, услуги), 12.11.2026; возраст — {asrc}",
          acc=acc, adult_price=None, booking="обязательна", loud="частично" if active or first in ("music", "singing") else "нет",
          sit="нет" if active else "частично", crowd="нет", food="нет", stroller="частично")
    r["Взрослый билет, ₽"] = None
    r["Сайт"] = site
    r["Категории"] = cats
    r["Как найти"] = how
    r["Проверено (дата)"] = DT
    return r


TRIAL = {"x-temp-saltykovskaya": ("Бесплатное пробное занятие танцами", "Пробное занятие в детских группах (танцы для детей и подростков) — бесплатно.", YA + "x_temp/53822336192/prices/")}

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    ROWS = [row(k) for k in D]
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
        for r in ROWS:
            pid = r["id"]
            f = {"address": r["Адрес"], "type": r["Тип"], "cats": r["Категории"], "age_min": r["Возраст от"],
                 "age_max": r["Возраст до"], "booking": "обязательна"}
            if info(pid).get("phone"): f["phone"] = info(pid)["phone"]
            if r["Сайт"]: f["url"] = r["Сайт"]
            if r["Как найти"]: f["how"] = r["Как найти"]
            lat, lon, acc, lvl = point(pid)
            if lvl in ("объект", "вход"):
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
            print(r["id"], "|", r["Адрес"], "|", r["Метро"], "|", r["Широта"], r["Долгота"], "|", r["Точность координат"][:80], "|", r["Сайт"])
        print([k for k in ROWS[0] if k not in hdr]); sys.exit()
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    r0 = ws.max_row + 1
    for n, row_ in enumerate(ROWS):
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=r0 + n, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    cp = os.path.join(ROOT, "auto", "cat-ages.json")
    ca = json.load(open(cp)) if os.path.exists(cp) else {}
    for pid, v in D.items():
        if v[9]:
            ca[pid] = dict(v[9], src=f"{v[8]} (12.11.2026)")
    json.dump(ca, open(cp, "w"), ensure_ascii=False, indent=1)
    print("rows", len(ROWS))
