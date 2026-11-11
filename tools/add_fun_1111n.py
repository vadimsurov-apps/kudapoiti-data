"""Робот fun, 2026-11-11 (проход n).
1) Пеленальные комнаты (урок 7): точки osm-changing.json исчерпаны (остались набережные/трассы без объекта),
   поэтому — комнаты матери и ребёнка в ТЦ и парке по сайтам ТЦ и карточкам Яндекс Карт (кэш auto/pages/*fqv*-1111n*,
   *fqy30*), точка — объект OSM самого ТЦ/комнаты (auto/osm-answers.json, запросы fq-*).
2) Поиск по районам (Яндекс Карты, кэш auto/pages/*fqz*-1111n* — поиск, *fqy* — карточки, *fqx*/*fqu* — адреса):
   Воскресенск, Дзержинский, Дмитров, Дубна, Звенигород, Зеленоград, Истра, Кашира, Крылатское, Кузьминки,
   Лефортово, Люблино, Марьино. Только места с возрастом в источнике (урок 7); остальные пропущены.
Точки — tools/fun_1111n_points.json (объект/вход OSM). Иконки — tools/icons_fun_1111n.py.
Запуск: KP_PART=fun python3 tools/add_fun_1111n.py"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC
from add_batch14 import metro

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DAY = "2026-11-11"
PTS = json.load(open(os.path.join(ROOT, "tools", "fun_1111n_points.json")))
ROWS, VER = [], {}


def row(r, f, src):
    r["Проверено (дата)"] = DAY
    ROWS.append(r)
    VER[r["id"]] = {"fields": f, "src": src}


def pt(pid):
    lat, lon, osm, level = PTS[pid]
    if not osm:  # объект/вход OSM не нашли — дом по адресу (Яндекс Карты), место скрыто до подтверждения входа
        return (lat, lon, "приблизительно — здание по адресу (Яндекс Карты, координаты дома)",
                {"lat": lat, "lon": lon, "level": "дом", "how": "Яндекс Карты, координаты дома по адресу"})
    return lat, lon, f"точно (OSM {osm})", {"lat": lat, "lon": lon, "level": level, "how": f"OSM {osm}"}


def changing(pid, name, addr, plus, how, src, hours=None, minus=""):
    if pid not in PTS:
        return
    lat, lon, acc, point = pt(pid)
    r = P(pid, name, "пеленальная комната", metro(lat, lon), addr, lat, lon, 0, 3, 10, 20, "спокойно", "малыши",
          None, None, hours, "да", plus, minus, adult=1, src=src, acc=acc, adult_price="",
          booking="не нужна", sit="частично", loud="нет", dark="нет", stroller="да", crowd="нет", food="нет")
    r["Категории"] = "changing"
    r["Пеленальный стол"] = "да"
    if how:
        r["Как найти"] = how
    f = {"point": point, "address": addr}
    if hours:
        f["hours"] = hours
    row(r, f, src)


def place(pid, name, typ, cats, tags, addr, a0, a1, d0, d1, energy, plus, phone, site, src, how=None, minus="",
          loud="частично", sit="частично", booking="обязательна", adult=1, price=None, hours=None, empty=()):
    if pid not in PTS:
        return
    lat, lon, acc, point = pt(pid)
    r = P(pid, name, typ, metro(lat, lon), addr, lat, lon, a0, a1, d0, d1, energy, tags, price, None, hours, "да",
          plus, minus, adult=adult, src=src, acc=acc, adult_price="", booking=booking, sit=sit, loud=loud,
          dark="нет", stroller="нет", crowd="нет", food="нет")
    r["Сайт"] = site
    r["Категории"] = cats
    if how:
        r["Как найти"] = how
    f = {"point": point, "address": addr, "phone": phone, "age_min": a0, "age_max": a1}
    if site:
        f["url"] = site
    if hours:
        f["hours"] = hours
    if price is not None:
        f["price_child"] = price
    row(r, f, src)


YAV = "Яндекс Карты, карточка «Комната матери и ребёнка» (поиск 11.11.2026)"
# --- пеленальные ---
changing("chg-park-50-let-oktyabrya", "Комната матери и ребёнка — парк 50-летия Октября",
         "Москва, парк 50-летия Октября", "Отдельная комната матери и ребёнка прямо в парке — покормить и переодеть малыша",
         "Ориентир: на территории парка 50-летия Октября (район Проспект Вернадского)",
         "OpenStreetMap way/982171847 «Комната матери и ребёнка» (opening_hours Mo-Su 10:00-22:00); Яндекс Карты, карточка организации",
         hours="ежедневно 10:00–22:00")
changing("chg-trc-orbita", "Комната матери и ребёнка — ТЦ «Орбита» (Люберцы)", "Люберцы, Октябрьский просп., 366, ТЦ «Орбита», 4 этаж",
         "Бесплатная комната матери и ребёнка, на 4 этаж можно подняться на лифте или эскалаторе",
         "Этаж: 4 (лифт или эскалатор)",
         "Яндекс Карты, карточка ТЦ «Орбита» → услуги «Комната матери и ребенка» (11.11.2026); OpenStreetMap way/306454849",
         hours="пн–пт 12:00–22:00; сб, вс и праздники 11:00–22:00")
changing("chg-trc-botanica", "Комната матери и ребёнка — ТРЦ «Ботаника»", "Москва, ул. Вильгельма Пика, 11, ТРЦ «Ботаника», 2 этаж",
         "Комната матери и ребёнка на 2 этаже, рядом в ТРЦ — «Детский мир» и семейный парк TeikaBoom", "Этаж: 2",
         "сайт botanicamall.ru (раздел «Веселое время для всей семьи»); " + YAV)
changing("chg-trk-evropeisky", "Комната матери и ребёнка — ТРК «Европейский»",
         "Москва, площадь Киевского Вокзала, 2, ТРК «Европейский»",
         "Комната матери и ребёнка в ТРК у Киевского вокзала — удобно перед поездом", None,
         "сайт europe-tc.ru (каталог «Все для детей» → «Комната матери и ребенка»); " + YAV)
changing("chg-vegas-kuntsevo", "Комната матери и ребёнка — ТРК «Vegas Кунцево»", "Одинцовский г.о., Хорошёвский пр-д, 14, ТРК «Vegas Кунцево» (56-й км МКАД)",
         "Комната матери и ребёнка, гардероб и браслеты-«непотеряшки» для детей", None,
         "сайт kuntsevo.vegas-city.ru: «Во всех ТРК VEGAS есть комнаты матери и ребенка, гардероб и браслеты «непотеряшки»»")
changing("chg-vegas-crocus", "Комната матери и ребёнка — ТРК «Vegas Крокус Сити»", "Красногорск, Международная ул., 12, ТРК «Vegas Крокус Сити»",
         "Комната матери и ребёнка, гардероб и браслеты-«непотеряшки» для детей", None,
         "сайт kuntsevo.vegas-city.ru: «Во всех ТРК VEGAS есть комнаты матери и ребенка…»")
changing("chg-vegas-kashirskoe", "Комната матери и ребёнка — ТРК «Vegas» (24-й км МКАД)", "Москва, МКАД, 24-й километр, 1, ТРК «Vegas»",
         "Комната матери и ребёнка, гардероб и браслеты-«непотеряшки» для детей", None,
         YAV + "; сайт kuntsevo.vegas-city.ru: «Во всех ТРК VEGAS есть комнаты матери и ребенка…»")

# --- новые места по районам ---
place("fun-shkola-fokusov-baumanskaya", "Московская школа фокусов", "школа фокусов", "masterclass", "фокусы, творчество",
      "Москва, Бауманская ул., 58/25, стр. 10", 5, 15, 60, 90, "спокойно",
      "Каждый день шоу-мастер-класс: выступление иллюзиониста и урок фокусов, которые ребёнок унесёт с собой — 2500 ₽; "
      "группы обучения фокусам для 5–7, 8–10 и 11–15 лет — 3000 ₽ за час", "+7 993 350-20-40", "https://magician.center",
      "Яндекс Карты, карточка организации (11.11.2026); сайт magician.center (группы 5–7, 8–10, 11–15 лет)",
      how="Вход: главный вход строения 10 (по OSM)", sit="да", price=2500)
place("fun-quest-center-zelenograd", "Квест центр (Зеленоград, Крюково)", "квест-центр", "quests", "загадки, приключения",
      "Зеленоград, корп. 1462", 5, 17, 60, 120, "активно",
      "Квесты, квест-игры и интерактивы для детей от 5 лет и взрослых; детские праздники с программами на 2, 3 и 4 часа "
      "для 7–12 лет", "+7 999 999-66-19", "https://quest.center",
      "сайт quest.center (возраст, часы «ежедневно с 11.00 до 21.00»); Яндекс Карты, карточка организации (11.11.2026)",
      hours="ежедневно 11:00–21:00", loud="да", sit="нет")
place("fun-vkusnaya-studiya-zelenograd", "Кулинарная «Вкусная студия» (Зеленоград)", "кулинарная студия мастер-классов",
      "masterclass", "кулинария, творчество", "Зеленоград, корп. 2308Б", 8, 17, 120, 180, "спокойно",
      "Детские кондитерские мастер-классы для 8+ — пряничный домик, новогодняя ёлочка, 3000 ₽; есть семейные мастер-классы "
      "и дни рождения с готовкой", "+7 919 997-40-56", "https://tastystudio.ru",
      "сайт tastystudio.ru (расписание: «Дети 8+», 3000 ₽); Яндекс Карты, карточка организации (11.11.2026)",
      sit="да", price=3000, loud="нет")
place("fun-malenky-ostrov-zelenograd", "Игровая «Маленький остров» (Зеленоград, Савёлки)", "игровая комната и студия праздников",
      "playcenters", "игры, праздники", "Зеленоград, корп. 353", 0, 10, 60, 240, "активно",
      "Игровая комната: в будни — безлимит под присмотром родителей 750 ₽, в выходные и праздники — безлимит под присмотром "
      "няни 1500 ₽; устраивают дни рождения с аниматором, бумажной дискотекой и шоу мыльных пузырей",
      "+7 916 734-02-37", "https://small-island.ru", "Яндекс Карты, карточка организации, цены (11.11.2026)",
      minus="Не больше 21 ребёнка одновременно; дети до 3 лет — только с родителями", loud="да", sit="нет",
      booking="желательна", price=750)

if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=i, column=1).value for i in range(2, ws.max_row + 1)}
    allids = {x["id"] for x in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    ids = [x["id"] for x in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    assert not [i for i in ids if i in existing or i in allids], [i for i in ids if i in existing or i in allids]
    for row_ in ROWS:
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        rr = ws.max_row + 1
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=rr, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    json.dump(VER, open("/tmp/claude-0/ver_fun_1111n.json", "w"), ensure_ascii=False, indent=1)
    print("rows", len(ROWS), "total", ws.max_row - 1, ids)
