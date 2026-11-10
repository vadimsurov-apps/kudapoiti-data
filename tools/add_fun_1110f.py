"""Робот fun, 2026-11-10 (дневной проход 2). Источник — объекты OpenStreetMap из auto/candidates.json (детские
библиотеки): название, точка, часы и телефон — из тегов объекта OSM; адрес — дом, в котором стоит объект
(справка auto/osm-answers.json, запросы fun-*). Брали только те, у которых дом с адресом найден рядом (≤ 26 м),
а город однозначен. Иконки — tools/icons_fun_1110f.py. Запуск: KP_PART=fun python3 tools/add_fun_1110f.py"""
import json, os
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
lib("lib85-izmaylovsky", "node/4114707592", "Детская библиотека №85 (Измайлово)", "Москва, 3-я Парковая ул., 26/2",
    (55.795923, 37.783205))
lib("lib97-suzdalskaya", "node/2389493010", "Библиотека №97 — фонд детской литературы (Новокосино)",
    "Москва, Суздальская ул., 38, корп. 2", (55.745399, 37.872473), hours="Вт–Вс 12:00–21:00",
    site="https://cbs-vao.ru/lib97-fond-detskoj-literatury")
lib("cbs1-kids-volgogradsky-91", "node/529601587", "Детская библиотека ЦБС №1 (Волгоградский пр-т, 91)",
    "Москва, Волгоградский пр-т, 91", (55.708212, 37.74959), hours="Вт–Сб 12:00–20:00, Вс и Пн — выходные",
    phone="+7 499 173-13-94")
lib("lib11-tolstoy-novatorov", "node/2313211953", "Детская библиотека №11 им. Л. Н. Толстого",
    "Москва, ул. Новаторов, 14, корп. 2", (55.66712, 37.523112))
lib("lib117-vesennyaya", "node/3959209467", "Детская библиотека №117 (Весенняя ул.)", "Москва, Весенняя ул., 8",
    (55.872918, 37.517144))
lib("lib22-kassil-leningradskoe", "node/5341564476", "Детская библиотека №22 им. Л. Кассиля",
    "Москва, Ленинградское ш., 120", (55.867543, 37.462885), hours=H)
lib("lib32-supruna", "node/3560736442", "Детская библиотека №32 (ул. Степана Супруна)",
    "Москва, ул. Степана Супруна, 12, корп. 3", (55.797488, 37.545622), hours=H)
lib("lib43-kuusinena", "node/9029258029", "Детская библиотека №43 (ул. Куусинена)", "Москва, ул. Куусинена, 17, корп. 2",
    (55.785705, 37.51185))
lib("lib98-narodnogo-opolcheniya", "way/52584106", "Детская библиотека №98 (ул. Народного Ополчения)",
    "Москва, ул. Народного Ополчения, 37, корп. 1", (55.790709, 37.488035))
lib("lib57-krasnobogatyrskaya", "node/2013361399", "Детская библиотека №57 (Краснобогатырская ул.)",
    "Москва, Краснобогатырская ул., 75, корп. 2", (55.80861, 37.707338), phone="+7 499 162-43-68")
lib("lib71-baykalskaya", "node/663722977", "Детская библиотека №71 (Байкальская ул.)",
    "Москва, Байкальская ул., 46, корп. 1", (55.817098, 37.819214))
lib("lib72-storozhevaya", "node/1635663350", "Детская библиотека №72 (Сторожевая ул.)",
    "Москва, Сторожевая ул., 22, корп. 1", (55.765586, 37.711503))
lib("lib77-shaturskaya", "node/1801649526", "Детская библиотека №77 (Шатурская ул.)", "Москва, Шатурская ул., 49, корп. 1",
    (55.726882, 37.774047))
lib("lib80-sholokhov", "node/3504855619", "Центральная детская библиотека №80 им. М. А. Шолохова",
    "Москва, 8-я ул. Текстильщиков, 14", (55.702131, 37.745731),
    hours="Пн–Пт 12:00–19:00, Сб–Вс — выходные; последняя пятница месяца — санитарный день",
    site="http://www.infokniga.ru/centralnaya-detskaya-biblioteka-80-im-masholoxova", phone="+7 499 179-11-01")
lib("lib91-altufyevskoe", "node/6942530074", "Детская библиотека №91 (Алтуфьевское ш.)", "Москва, Алтуфьевское ш., 34А",
    (55.867546, 37.587564))
lib("zhukovsky-kids-library4", "node/2057021998", "Детская библиотека №4 (Жуковский)", "Жуковский, ул. Гудкова, 7А",
    (55.595623, 38.092697), hours="Пн–Пт 10:00–18:00 (перерыв 13:00–14:00), Вс 10:00–14:00", phone="+7 498 482-49-67")
lib("zhukovsky-kids-library6", "node/2960912634", "Детская библиотека №6 (Жуковский)", "Жуковский, ул. Макаревского, 3",
    (55.608791, 38.074064), hours="Пн–Пт 10:00–17:00, Сб 10:00–16:00", phone="+7 498 482-55-12")
lib("klin-kids-library-krasnaya", "node/5213077850", "Детская библиотека (Клин, Красная ул.)", "Клин, Красная ул., 6",
    (56.33678, 36.730371))
lib("ruza-kids-library", "node/4789698823", "Детская библиотека (Руза)", "Руза, Федеративная ул., 4", (55.705204, 36.19507))
lib("dubna-kids-library-volga", "node/4331385264", "Детская городская библиотека (Дубна, Большая Волга)",
    "Дубна, пр-т Боголюбова, 35", (56.730871, 37.149092))
lib("skhodnya-kids-library", "node/1217962449", "Сходненская детская библиотека (Химки)", "Химки, мкр Сходня, Вишнёвая ул., 10",
    (55.949033, 37.293839))
lib("voskresensk-central-kids-library", "node/3380833442", "Центральная детская библиотека (Воскресенск)",
    "Воскресенск, Пионерская ул., 7", (55.321042, 38.676127))

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
