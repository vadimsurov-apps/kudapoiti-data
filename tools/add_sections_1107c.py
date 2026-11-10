"""Робот sections, 2026-11-07 (03 UTC): бадминтон (НаТен, «Высшая лига», «Развитие», «Мастер+», NLBC на Турчаниновом,
Badminton club Сколково, «Мир бадминтона», сквош-клуб «Москва», «Градиор»), баскетбол (новые залы «Хаски», «Стремление»,
IBASKET Тропарёво, ОЦ «Протон», СК «Восход»), шахматы (Chess First, EduChess, Шахматная школа №1 — Озёрная).
Источники (кэш auto/pages, скачан 2026-11-07 через auto/fetch-queue.txt): sportschools.ru (карточки бадминтона и
баскетбола ЗАО — возраст детских групп и адрес), trenera.ru и inring.ru (залы «Хаски», цена «от»), posleurokov.ru
(шахматы — адрес, возраст, цена), официальные сайты сетей s-basket.ru, i-basket.ru, bc-newliga.ru, chessfirst.ru,
educhess.ru, chess1school.com (цены, возраст). Не брали: только взрослые (Newton Arena, «Искра», BAD), спа-клуб Rodina,
залы Khimki Badminton Club без подтверждённых детских групп, карточки с сайтом-перепродажей без детских групп.
Координаты — по метро («приблизительно»), уточнит geocode-address.yml.
Запуск: KP_PART=sections python3 tools/add_sections_1107c.py [--dry]"""
import json, os, re, sys, math, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
import add_sections_1106 as A
from add_sections_1106 import at, near, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
D = "проверено 2026-11-07"
SEC, CH = "спортивная секция", "шахматный клуб"
SP = LOG = "спорт и активность"
SS_B = "sportschools.ru/gorod-Moscow/sport-Badminton"
SS_Z = "sportschools.ru/gorod-Moscow/region-ZAO/sport-Basketball"
PL = "posleurokov.ru/moscow/chess"

R = []


def add(pid, name, typ, loc, addr, a0, a1, d, tags, price, note, plus, minus, site, cat, src):
    r = A.row(pid, name, typ, loc, addr, a0, a1, d[0], d[1], tags, price, note, None, plus, minus, site, cat,
              src=f"{src} ({D})")
    r["Детский билет, ₽"] = price
    r["Взрослый билет, ₽"] = None
    r["Проверено (дата)"] = "2026-11-07"
    R.append(r)


# ---------------- Бадминтон ----------------
B = (60, 90)
add("naten-badminton-vernadskogo", "Клуб «НаТен» — бадминтон для детей (пр-т Вернадского)", SEC, at("Юго-Западная"),
    "пр-т Вернадского, 78, стр. 5", 3, 17, B, SP, None, "цены — у администратора клуба",
    "Бадминтон и настольный теннис: детские группы с 3 лет, ОФП, соревнования и спортлагерь",
    "Цены на сайте каталога не указаны — уточняйте по телефону", None, "badminton", SS_B)
add("naten-badminton-shchipkovsky", "Клуб «НаТен» — бадминтон для детей (1-й Щипковский пер.)", SEC, at("Серпуховская"),
    "1-й Щипковский пер., 23", 5, 17, B, SP, None, "цены — у администратора клуба",
    "Бадминтон и настольный теннис в центре: детские группы с 5 лет, индивидуальные занятия и турниры",
    "Цены не опубликованы — уточняйте при записи", None, "badminton", SS_B)
add("vysshaya-liga-badminton", "Центр игровых видов спорта «Высшая лига» — детский бадминтон", SEC, at("Нагорная"),
    "Электролитный пр-д, 3, стр. 5", 7, 17, B, SP, None, "цены — у администратора",
    "Большой спорткомплекс игровых видов: бадминтон для детей с 7 лет, рядом — футбол, волейбол и теннис",
    "Группы с 7 лет; уточняйте расписание детских тренировок", None, "badminton", SS_B)
add("razvitie-badminton-kozhukhovo", "Спортклуб «Развитие» — бадминтон для детей (Кожуховская)", SEC, at("Кожуховская"),
    "2-й Южнопортовый пр-д, 19, корп. 1", 3, 17, B, SP, None, "цены — у администратора",
    "Детские секции с 3 лет: бадминтон, мини-футбол, гимнастика и волейбол в одном зале",
    "Цены не опубликованы", None, "badminton", SS_B)
add("master-plus-badminton", "Бадминтонный клуб «Мастер+» — детские группы", SEC, at("Шаболовская"),
    "ул. Малая Калужская, 1", 5, 17, B, SP, None, "цены — у администратора",
    "Профессиональные корты и групповые тренировки для детей с 5 лет и взрослых — можно заниматься всей семьёй",
    "Цены на сайте не указаны", None, "badminton", SS_B)
add("nlbc-badminton-turchaninov", "Центр бадминтона «Новая Лига» (NLBC) — дети (Турчанинов пер.)", SEC, at("Парк культуры"),
    "Турчанинов пер., 3, стр. 1", 5, 17, B, SP, None, "цены — на сайте клуба bc-newliga.ru",
    "Детская академия бадминтона: тренеры — призёры первенств Европы, группы с 5 лет, рядом с м. Парк культуры",
    "Детские группы быстро заполняются — записывайтесь заранее", "https://bc-newliga.ru/", "badminton",
    f"{SS_B}, bc-newliga.ru")
add("badminton-club-skolkovo", "Badminton club Сколково — детские группы", SEC, near(55.6992, 37.3585),
    "ул. Зворыкина, 21 (Сколково)", 5, 17, B, SP, None, "цены — у администратора",
    "9 профессиональных площадок, детские и взрослые группы с 5 лет", "Далеко от метро — удобнее на машине",
    None, "badminton", SS_B)
add("mir-badmintona-leningradka", "«Мир бадминтона» — тренировки для детей (Ленинградское ш.)", SEC, at("Войковская"),
    "Ленинградское ш., 25А, стр. 2", 7, 17, B, SP, None, "цены — у администратора",
    "Групповые и игровые тренировки с мастерами спорта, дети с 7 лет", "Цены не опубликованы", None, "badminton", SS_B)
add("squash-moskva-badminton", "Сквош-клуб «Москва» — детский бадминтон", SEC, at("Дубровка"),
    "Шарикоподшипниковская ул., 13, стр. 46", 7, 17, B, SP, None, "цены — у администратора",
    "6 бадминтонных кортов и 9 сквош-кортов: групповые тренировки для детей с 7 лет", "Цены не опубликованы", None,
    "badminton", SS_B)
add("gradior-pokryshkina", "Спортклуб «Градиор» — бадминтон и секции (Покрышкина)", SEC, at("Юго-Западная"),
    "ул. Покрышкина, 3", 7, 17, B, SP, None, "цены — у администратора",
    "Бадминтон с 7 лет и ещё много секций в одном месте: ритмика с 3 лет, хореография, самбо, брейк-данс",
    "Цены не опубликованы", None, "badminton", SS_B)

# ---------------- Баскетбол ----------------
H = "https://husbasket.ru/"
HS = "trenera.ru/kluby/basketbol/dlya-detej, inring.ru (возраст 5–15, цена «от»)"
for slug, addr, loc in [("zeleny-10", "Зелёный пр-т, 10Б", at("Перово")),
                        ("aviamotornaya", "ул. Авиамоторная, 55, корп. 8", at("Авиамоторная")),
                        ("ryazansky", "Рязанский пр-т, 99, корп. 7", at("Рязанский проспект")),
                        ("pravoberezhnaya", "ул. Правобережная, 1Б", near(55.8665, 37.4770)),
                        ("novodmitrovskaya", "ул. Большая Новодмитровская, 63, стр. 1", at("Дмитровская")),
                        ("khimki-mashkinskoe", "Химки, Машкинское ш., 19, стр. 1", near(55.8905, 37.4300)),
                        ("smolnaya", "ул. Смольная, 12", at("Водный стадион")),
                        ("yaroslavskoe", "Ярославское ш., 26, стр. 4", at("ВДНХ")),
                        ("novoyasenevsky", "Новоясеневский пр-т, 1В, стр. 1", at("Тёплый Стан")),
                        ("profsoyuznaya-96", "Профсоюзная ул., 96Б (школа № 170)", at("Беляево"))]:
    add(f"husky-basket-{slug}", f"Баскетбольная школа «Хаски» ({addr.split(' (')[0]})", SEC, loc, addr, 5, 15, (60, 90),
        SP, 563, "цена «от» за занятие в абонементе; пробное — по записи",
        "Детский баскетбол с 5 лет рядом с домом: группы по возрасту, своя лига и турниры",
        "Цена «от» — для длинного абонемента; уточняйте расписание зала", H, "ballgames", HS)
SB = "https://s-basket.ru/moscow"
for slug, addr, st, a0, a1 in [("novye-sady", "6-я ул. Новые Сады, 2, корп. 1", "Новопеределкино", 7, 17),
                               ("molodezhnaya", "Молодогвардейская ул., 15", "Молодёжная", 9, 16),
                               ("kutuzovskaya", "Кутузовский пр-т, 28", "Кутузовская", 7, 17)]:
    add(f"stremlenie-basket-{slug}", f"Баскетбольный клуб «Стремление» ({addr.split(',')[0]})", SEC, at(st), addr,
        a0, a1, (60, 90), SP, 750, "пробная тренировка 750 ₽ (вместо 1500), абонемент от 5800 ₽ / 4 тренировки",
        "Крупнейший любительский баскетбольный клуб: берут без отбора, своя детская лига и сборы круглый год",
        "Цены по абонементу выше разовой пробной", SB, "ballgames", f"{SS_Z}, s-basket.ru/moscow")
add("ibasket-troparevo", "Баскетбольная академия IBASKET (Никулинская ул.)", SEC, at("Юго-Западная"),
    "Никулинская ул., 5", 5, 12, (60, 90), SP, None, "цены — на сайте i-basket.ru",
    "Детские группы 6–12 лет, ученики играют во внутренней лиге IBASKET и летних лагерях",
    "Уточняйте расписание конкретного зала", "https://i-basket.ru/", "ballgames", f"{SS_Z}, i-basket.ru")
add("proton-basket-fili", "Секция баскетбола в ОЦ «Протон» (Фили)", SEC, at("Багратионовская"),
    "Большая Филёвская ул., 15", 4, 17, (60, 90), SP, None, "цены — у администратора",
    "Баскетбол для детей с 4 лет: групповые и индивидуальные тренировки", "Цены не опубликованы", None,
    "ballgames", SS_Z)
add("voskhod-basket-fili", "Спортклуб «Восход» — баскетбол для детей (Новозаводская ул.)", SEC, at("Багратионовская"),
    "Новозаводская ул., 27А, стр. 1 (СК «Фили»)", 5, 14, (60, 90), SP, None, "цены — у администратора",
    "Баскетбол и настольный теннис для детей с 5 лет", "Цены не опубликованы", None, "ballgames", SS_Z)

# ---------------- Шахматы ----------------
C = (45, 60)
add("chessfirst-landyshevaya", "Детский шахматный клуб Chess First (Ландышевая ул., Куркино)", CH, near(55.8968, 37.3895),
    "ул. Ландышевая, 12 (IQ-Школа)", 3, 17, C, LOG, 100, "пробное занятие от 100 ₽",
    "Шахматы с 3,5 лет в игровой форме: маленькие группы, первые турниры через несколько месяцев",
    "Занятия в помещении школы — расписание уточняйте", "https://chessfirst.ru/", "chess", f"{PL}, chessfirst.ru")
add("chessfirst-lobachevskogo", "Детский шахматный клуб Chess First (ул. Лобачевского)", CH, at("Тропарёво"),
    "ул. Лобачевского, 92 (детский сад № 1953)", 3, 17, C, LOG, 100, "пробное занятие от 100 ₽",
    "Шахматы для малышей с 3,5 лет: авторская игровая методика, удобно после детского сада",
    "Занятия на территории детского сада — уточняйте вход", "https://chessfirst.ru/", "chess", f"{PL}, chessfirst.ru")
for slug, addr, st in [("mosfilmovskaya", "ул. Мосфильмовская, 1Б (Discovery English Preschool)", "Воробьёвы горы"),
                       ("krylatskaya", "Крылатская ул., 45, корп. 1 (Discovery English Preschool)", "Крылатское"),
                       ("initsiativnaya", "ул. Инициативная, 1 (школа № 1589)", "Озёрная"),
                       ("udaltsova", "ул. Удальцова, 31 (школа № 1541)", "Проспект Вернадского")]:
    add(f"educhess-{slug}", f"Школа шахмат EduChess ({addr.split(',')[0]})", CH, at(st), addr, 3, 16, C, LOG, 1000,
        "занятие от 1000 ₽; группы и индивидуально",
        "Шахматы с 3 лет по методике EduChess: мышление и концентрация через игру, турниры и шахматные лагеря",
        "Занятия на базе детского сада/школы — расписание по записи", "https://educhess.ru/", "chess",
        f"{PL}, educhess.ru")
add("chess1-ozernaya", "Шахматная школа №1 (библиотека на Озёрной)", CH, at("Озёрная"), "ул. Озёрная, 13 (библиотека)",
    4, 14, C, LOG, 4800, "4800 ₽ в месяц (4 занятия); пробный урок по записи",
    "Шахматы для детей с 4 лет в библиотеке у метро: тренеры — кандидаты в мастера спорта и выше",
    "Группы небольшие — нужна запись", "https://chess1school.com/", "chess", f"{PL}, chess1school.com")

ROWS = R

if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    allp = json.load(open(os.path.join(ROOT, "places-all.json")))["places"]
    allids = {x["id"] for x in allp}
    ids = [r["id"] for r in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    assert not [i for i in ids if i in existing or i in allids], [i for i in ids if i in existing or i in allids]
    pts = [(p["name"], p["lat"], p["lon"]) for p in allp]
    for f in glob.glob(os.path.join(ROOT, "data", "parts", "*.xlsx")):
        rr = list(openpyxl.load_workbook(f, read_only=True)["Места"].values); h = rr[0]
        pts += [(r[h.index("Название")], r[h.index("Широта")], r[h.index("Долгота")]) for r in rr[1:] if r[h.index("Широта")]]
    key = lambda n: re.sub(r"[«»\"()—,.-]", " ", str(n).lower()).split()[:2]
    for r in ROWS:
        for n, a, b in pts:
            if a and math.hypot((r["Широта"] - a) * 111000, (r["Долгота"] - b) * 63000) < 300 and key(n) == key(r["Название"]):
                print("ДУБЛЬ?", r["id"], "~", n)
    if "--dry" in sys.argv:
        for r in ROWS: print(r["id"], "|", r["Метро"], "|", r["Категории"], "|", r["Широта"], r["Долгота"])
        from collections import Counter
        print("rows", len(ROWS), Counter(r["Категории"] for r in ROWS)); sys.exit()
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    for row_ in ROWS:
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        r = ws.max_row + 1
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=r, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    print("rows", len(ROWS), "total", ws.max_row - 1)
