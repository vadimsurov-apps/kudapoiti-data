"""Робот fun, 2026-11-10 (дневной проход 3, часть 2). Литературные музеи и детский театр. Точка — объект OSM места
(auto/candidates.json), адрес — дом объекта в OSM (справка auto/osm-answers.json, запросы fun-*), часы — тег OSM или
сайт, цены — страница goslitmuz.ru/visitors/ticket_price (кэш auto/pages/osm-node-3466483914), у музея Есенина — его
сайт (кэш auto/pages/osm-node-4118442289), у театра — его сайт (кэш auto/pages/osm-node-2196651653).
Иконки — tools/icons_fun_1110h.py. Запуск: KP_PART=fun python3 tools/add_fun_1110h.py"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC
from add_batch14 import metro

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DAY = "2026-11-10"
EX = "точно (OpenStreetMap)"
ROWS = []
GL = "https://goslitmuz.ru/visitors/ticket_price/"
FREE16 = "до 16 лет — бесплатно; последняя пятница месяца — бесплатно для всех"


def mus(pid, osm, name, addr, ll, adult_price, hours, plus, site, a0=7, src_extra="", note=FREE16, cats="museums"):
    lat, lon = ll
    r = P(pid, name, "литературный музей", metro(lat, lon), addr, lat, lon, a0, 14, 60, 120, "спокойно",
          "история, творчество", 0 if note == FREE16 else None, note, hours, "да", plus, "", adult=3,
          src=f"OpenStreetMap {osm} (адрес — дом объекта в OSM); {site}" + src_extra, acc=EX,
          adult_price=adult_price, booking="не нужна", food="нет", crowd="нет")
    r["Сайт"] = site
    r["Категории"] = cats
    r["Проверено (дата)"] = DAY
    ROWS.append(r)


mus("ostroukhov-house-trubniki", "node/3466483914", "Дом И. С. Остроухова в Трубниках (Гослитмузей)",
    "Москва, Трубниковский пер., 17, стр. 1", (55.754835, 37.586672), 200,
    "Вт–Вс 11:00–18:00, Чт 14:00–20:00",
    "Выставки Гослитмузея в старом особняке; для детей 8–12 лет бывают занятия «Загадки и премудрости русского языка» "
    "и «Символы и знаки»",
    "https://goslitmuz.ru/museums/dom-i-s-ostroukhova-v-trubnikakh", src_extra=f"; цены — {GL}")
mus("silver-age-museum-mira", "node/7824274685", "Музей Серебряного века (дом Брюсова)",
    "Москва, пр-т Мира, 30, стр. 1", (55.778369, 37.633016), 400,
    "Вт, Пт–Вс 11:00–18:00, Ср–Чт 11:00–21:00",
    "Дом, где с 1910 по 1924 год жил поэт Валерий Брюсов, — музей поэзии Серебряного века",
    "https://goslitmuz.ru/museums/muzey-serebryanogo-veka/", src_extra=f"; цены — {GL}")
mus("dostoevsky-house-moscow", "node/1396324038", "Музейный центр «Московский дом Достоевского»",
    "Москва, ул. Достоевского, 2", (55.783497, 37.610357), 500,
    "Вт–Вс 11:00–18:00, Ср–Чт 11:00–21:00",
    "Квартира, где прошло детство Фёдора Достоевского, восстановлена по описанию и чертежам его брата; есть экскурсия "
    "«Достоевский. Московское детство писателя»",
    "https://goslitmuz.ru/museums/moskovskij-dom-dostoevskogo/", src_extra=f"; цены — {GL}")
mus("herzen-house-museum", "node/3500729458", "Дом-музей А. И. Герцена", "Москва, пер. Сивцев Вражек, 27",
    (55.747126, 37.591898), 300, "Вт, Пт–Вс 11:00–18:00, Ср–Чт 11:00–21:00",
    "Дом-музей Александра Герцена в переулке у Старого Арбата", "https://goslitmuz.ru/museums/dom-muzey-a-i-gertsena/",
    src_extra=f"; цены — {GL}")
mus("esenin-house-strochenovsky", "node/4118442289", "Дом-музей С. А. Есенина (Замоскворечье)",
    "Москва, Большой Строченовский пер., 24, стр. 2", (55.726629, 37.630778), None,
    "Вт, Ср, Пт 10:00–18:00; Чт 13:00–21:00; Сб–Вс 12:00–20:00; Пн — выходной",
    "Мемориальный дом-музей Сергея Есенина в Замоскворечье", "https://esenin-museum.ru/",
    note="дети до 7 лет — бесплатно")

lat, lon = 55.763472, 37.655146
r = P("theatre-na-pokrovke", "Театр на Покровке", "театр", metro(lat, lon), "Москва, ул. Покровка, 50/2, стр. 1",
      lat, lon, 6, 14, 60, 150, "спокойно", "театр", None, None, None, "да",
      "В репертуаре есть мюзикл для детей «Буратино» и сказка для всех «Дракон» по Шварцу", "", adult=3,
      src="OpenStreetMap node/2196651653 (адрес — дом объекта в OSM); http://www.napokrovke.ru/ (репертуар)", acc=EX,
      booking="обязательна", dark="частично", sit="да", food="нет", stroller="нет")
r["Сайт"] = "http://www.napokrovke.ru/"
r["Категории"] = "shows"
r["Проверено (дата)"] = DAY
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
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        rr = ws.max_row + 1
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=rr, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    print("rows", len(ROWS), "total", ws.max_row - 1)
