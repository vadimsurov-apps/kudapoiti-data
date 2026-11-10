"""Робот fun, 2026-11-10 (дневной проход 3). Источник — объекты OpenStreetMap из auto/candidates.json (детские библиотеки
Москвы и музей-подлодка в Северном Тушине): название, точка, часы, телефон — из тегов объекта OSM; адрес — дом, в котором
стоит объект (справка auto/osm-answers.json, запросы fun-*; дом с адресом ≤ 30 м). Музей ВМФ — цены и часы с его
страницы (кэш auto/pages/osm-way-118989786). Иконки — tools/icons_fun_1110g.py.
Запуск: KP_PART=fun python3 tools/add_fun_1110g.py"""
import json, os, sys
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC
from add_batch14 import metro

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DAY = "2026-11-10"
EX = "точно (OpenStreetMap)"
ROWS = []
PLUS = "Районная детская библиотека: книги для малышей и школьников, можно посидеть и почитать вместе"


def lib(pid, osm, name, addr, ll, hours=None, site="", phone=None, plus=None, minus=""):
    lat, lon = ll
    r = P(pid, name, "детская библиотека", metro(lat, lon), addr, lat, lon, 1, 14, 30, 120, "спокойно", "творчество",
          0, "вход свободный", hours, "да", plus or PLUS, minus, adult=1,
          src=f"OpenStreetMap {osm} (адрес — дом объекта в OSM)" + (f"; {site}" if site else ""), acc=EX, adult_price=0,
          booking="не нужна", food="нет", crowd="нет")
    r["Сайт"] = site
    r["Категории"] = "museums"
    r["Проверено (дата)"] = DAY
    if phone:
        r["Телефон"] = phone
    ROWS.append(r)


H = "Вт–Сб 12:00–21:00, Вс 12:00–20:00"
lib("lib-kids-mira-198", "node/1321969348", "Детская библиотека (пр-т Мира, 198)", "Москва, пр-т Мира, 198, корп. 2",
    (55.837285, 37.661832))
lib("lib153-zadonsky", "node/6279105291", "Детская библиотека №153 (Задонский пр-д)", "Москва, Задонский пр-д, 24, корп. 3",
    (55.621728, 37.753618), hours="Пн–Сб 12:00–21:00, Вс 12:00–20:00")
lib("lib60-goncharova", "node/7658402641", "Детская библиотека №60 (ул. Гончарова)", "Москва, ул. Гончарова, 17, корп. 4",
    (55.81596, 37.590376), hours=H)
lib("lib122-andropova", "node/1711851904", "Детская библиотека №122 (пр-т Андропова)", "Москва, пр-т Андропова, 17, корп. 1",
    (55.682892, 37.667091))
lib("lib31-baltiyskaya", "node/3912636549", "Детская библиотека №31 (Балтийская ул.)", "Москва, Балтийская ул., 4А, стр. 2",
    (55.807729, 37.512966), hours=H, phone="+7 499 152-48-81")
lib("lib40-vyatskaya", "node/6453204185", "Детская библиотека №40 (Вятская ул.)", "Москва, Вятская ул., 3",
    (55.793657, 37.581344), hours=H + ", Пн — выходной")
lib("lib74-sayanskaya", "node/1803669976", "Детская библиотека №74 (Саянская ул.)", "Москва, Саянская ул., 7А",
    (55.767992, 37.832253))
lib("lib226-khimkinsky", "node/1370762390", "Центральная детская библиотека №226 (Химкинский б-р)",
    "Москва, Химкинский б-р, 16, корп. 1", (55.851874, 37.442478),
    hours=H + "; 4-е воскресенье месяца — выходной", site="https://szao-cbs.ru/226-2/", phone="+7 499 492-37-15",
    plus="Центральная детская библиотека района: младший и старший абонемент, читальный зал, компьютерный класс, "
         "сенсорная комната и игровой отдел «Игромир»")
lib("lib-kids-domodedovskaya-44", "node/6486134931", "Детская библиотека (Домодедовская ул., 44)",
    "Москва, Домодедовская ул., 44", (55.601182, 37.714851))

# Музей-подводная лодка Б-396 (Северное Тушино)
lat, lon = 55.852304, 37.455071
r = P("vmf-museum-tushino", "Музейный комплекс истории ВМФ — подводная лодка Б-396 (Северное Тушино)", "музей",
      metro(lat, lon), "Москва, ул. Свободы, 56 (парк «Северное Тушино»)", lat, lon, 5, 14, 60, 120, "средне",
      "техника, история, вода", 550,
      "до 6 лет включительно — бесплатно; школьникам Москвы по «Москвёнку» (проект «Музеи — детям») — бесплатно",
      "Пн–Ср, Пт–Вс 11:00–19:00; Чт 13:00–21:00; последний четверг месяца — санитарный день", "да",
      "Можно пройти внутри настоящей дизельной подводной лодки Б-396, посмотреть снаружи экраноплан «Орлёнок»; "
      "есть выставка «Величие и глубина» и выставка об истории водолазного дела",
      "", adult=3,
      src="OpenStreetMap way/118989786; https://mosparks.ru/places/severnoe-tushino/vmf-museum (цены, часы)",
      acc=EX, adult_price=550, booking="не нужна", food="нет")
r["Сайт"] = "https://mosparks.ru/places/severnoe-tushino/vmf-museum"
r["Категории"] = "museums, transport"
r["Проверено (дата)"] = DAY
r["Телефон"] = "+7 495 640-73-55"
ROWS.append(r)

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
        for b in set(row_) - set(hdr):
            row_.pop(b) if b == "Телефон" else None
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        rr = ws.max_row + 1
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=rr, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    print("rows", len(ROWS), "total", ws.max_row - 1)
