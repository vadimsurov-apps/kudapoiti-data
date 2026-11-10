"""Робот fun, 2026-11-10 (дневной проход). Источник — объекты OpenStreetMap из auto/candidates.json (детские библиотеки
и музей), адрес и часы — из тегов OSM и дома по адресу (справка auto/osm-answers.json, запрос fun-*), у музея — сайт
sgm.ru (кэш auto/pages/osm-way-31482144). Яндекс и jsprav попали в auto/spam-domains.txt — их не использовали.
Иконки — tools/icons_fun_1110e.py. Запуск: KP_PART=fun python3 tools/add_fun_1110e.py"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC
from add_batch14 import metro

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DAY = "2026-11-10"
EX = "точно (OpenStreetMap)"
ROWS = []


def lib(pid, osm, name, addr, ll, hours=None, site="", phone=None, plus=None, minus=""):
    lat, lon = ll
    r = P(pid, name, "детская библиотека", metro(lat, lon), addr, lat, lon, 1, 14, 30, 120, "спокойно", "творчество",
          0, "вход свободный", hours, "да",
          plus or "Районная детская библиотека: книги для малышей и школьников, можно посидеть и почитать вместе",
          minus, adult=1, src=f"OpenStreetMap {osm}" + (f"; {site}" if site else ""), acc=EX, adult_price=0,
          booking="не нужна", food="нет", crowd="нет")
    r["Сайт"] = site
    r["Категории"] = "museums"
    r["Проверено (дата)"] = DAY
    if phone:
        r["Телефон"] = phone
    ROWS.append(r)


H1 = "Вт–Сб 12:00–21:00, Вс 12:00–20:00, Пн — выходной"
lib("lib34-kuryanovskaya", "node/541418275", "Детская библиотека №34 (Курьяново)", "Москва, 1-я Курьяновская ул., 31",
    (55.654118, 37.70303), phone="+7 495 356-00-62")
lib("kids-library-domodedovskaya-1", "node/707038993", "Детская библиотека (Домодедовская ул., 1)",
    "Москва, Домодедовская ул., 1, корп. 1", (55.615071, 37.707215),
    hours="Вт–Сб 12:00–21:00, Вс 12:00–20:00; последний вторник месяца — выходной")
lib("lib141-chertanovskaya", "way/60268187", "Детская библиотека №141 (Чертановская ул.)",
    "Москва, Чертановская ул., 41, корп. 3", (55.608476, 37.59559))
lib("lib206-zabelin-kremenchugskaya", "node/3944274081", "Детская библиотека №206 им. И. Е. Забелина",
    "Москва, Кременчугская ул., 6, корп. 1", (55.723963, 37.460318), hours=H1, phone="+7 495 449-05-84")
lib("lib130-guryevsky", "way/98244518", "Детская библиотека №130 (Гурьевский пр-д)",
    "Москва, Гурьевский пр-д, 15, корп. 2, стр. 2", (55.607177, 37.746705))
lib("lib161-ussuriyskaya", "node/740599593", "Детская библиотека №161 (Уссурийская ул.)",
    "Москва, Уссурийская ул., 9", (55.823783, 37.819671), hours="Пн–Сб 12:00–21:00, Вс 12:00–20:00")
lib("lib163-bogdanova", "node/666977870", "Детская библиотека №163 (Солнцево)", "Москва, ул. Богданова, 14",
    (55.657528, 37.407725), hours="Пн–Пт 11:00–19:00, Сб 11:00–18:00")
lib("lib58-rimskogo-korsakova", "node/2451289456", "Детская библиотека №58 (Отрадное)",
    "Москва, ул. Римского-Корсакова, 16", (55.87392, 37.606827), phone="+7 499 202-46-13")
lib("lib65-prishvin-severnaya", "way/88379051", "Детская библиотека №65 им. М. М. Пришвина (Северный)",
    "Москва, 6-я Северная линия, 1", (55.937668, 37.552327), hours=H1, site="https://vk.com/biblioteka65",
    phone="+7 499 767-77-63")
lib("lib14-dubininskaya", "node/5056154809", "Центральная детская библиотека №14 (Дубининская ул.)",
    "Москва, Дубининская ул., 20, стр. 1", (55.726284, 37.636628),
    plus="Центральная детская библиотека у Павелецкой с отделом семейного чтения — книги для детей и родителей")
lib("lib27-bochvara", "way/105733232", "Центральная детская библиотека №27 (Щукино)",
    "Москва, ул. Академика Бочвара, 3, стр. 1", (55.80712, 37.463174), hours=H1, phone="+7 499 190-05-63")
lib("lib250-zelenograd", "node/4811525321", "Детская библиотека №250 (Зеленоград)", "Зеленоград, корп. 607А",
    (55.988617, 37.230364), hours="Вт–Сб 10:00–22:00, Вс 10:00–20:00",
    site="http://www.zelbiblio.ru/biblioteki/biblioteka-250/", phone="+7 499 735-85-10")
lib("chekhov-kids-library", "node/12079512766", "Детская библиотека (Чехов, ул. Чехова)", "Чехов, ул. Чехова, 2",
    (55.147053, 37.484166), hours="Пн–Пт 9:30–18:00, Сб 9:30–17:00", site="http://www.chehovcbs.ru")
lib("ramenskoe-kids-library1", "node/1893359434", "Раменская детская библиотека №1", "Раменское, Коммунистическая ул., 7",
    (55.589556, 38.208242), phone="+7 496 463-53-54")
lib("zhukovsky-kids-library3", "node/2960900734", "Детская библиотека №3 (Жуковский)", "Жуковский, ул. Гагарина, 56",
    (55.608657, 38.093357), hours="Пн–Пт 10:00–17:00", phone="+7 498 482-12-19")
lib("naro-fominsk-kids-library", "way/170075533", "Центральная детская и юношеская библиотека (Наро-Фоминск)",
    "Наро-Фоминск, Латышская ул., 15Б", (55.376259, 36.731992),
    hours="Вт–Вс 10:00–18:30, перерыв 13:30–14:00", phone="+7 496 346-24-29", minus="Понедельник — выходной")

SGM = "сайт sgm.ru (10.11.2026); OpenStreetMap way/31482144"
r = P("geology-museum-vernadsky", "Государственный геологический музей им. В. И. Вернадского", "музей",
      metro(55.755957, 37.612582), "Москва, Моховая ул., 11, стр. 11", 55.755957, 37.612582, 6, 14, 60, 120, "средне",
      "история и наука", None, None,
      "Вт–Пт 11:00–19:00, Сб–Вс 12:00–19:00 (касса до 18:00), Пн — выходной", "да",
      "Минералы, камни и окаменелости в старинном особняке напротив Кремля; можно спуститься в шахту «Академическая». По карте «Москвёнок» (проект «Музей детям») — бесплатно",
      "Шахта «Академическая» — по отдельному билету (400 ₽)", adult=3, src=SGM, acc=EX, adult_price=500,
      booking="не нужна", food="нет")
r["Сайт"] = "https://www.sgm.ru/"
r["Категории"] = "museums,science"
r["Проверено (дата)"] = DAY
r["Телефон"] = "+7 495 692-09-43"
ROWS.append(r)

if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=i, column=1).value for i in range(2, ws.max_row + 1)}
    allids = {x["id"] for x in json.load(open(os.path.join(ROOT, "places.json")))["places"]}
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    ids = [x["id"] for x in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    assert not [i for i in ids if i in existing or i in allids], [i for i in ids if i in existing or i in allids]
    for row_ in ROWS:
        bad = set(row_) - set(hdr)
        for b in bad:
            row_.pop(b) if b == "Телефон" else None
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        rr = ws.max_row + 1
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=rr, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    print("rows", len(ROWS), "total", ws.max_row - 1)
