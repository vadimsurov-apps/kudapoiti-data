"""Робот fun, 2026-11-10 (утренний проход). Источник — список «Детские музеи» Афиши (auto/pages/www-afisha-ru-msk-museum-kids):
название, адрес, метро и описание из карточки списка. Карты Яндекса в этот запуск не использовались (домены yandex.* в
auto/spam-domains.txt), kudago отвечает 403 — поэтому партия маленькая. Координаты приблизительные, точку по адресу
поправит сверка с OSM. Иконки — tools/icons_fun_1110d.py.
Запуск: KP_PART=fun python3 tools/add_fun_1110d.py"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC
from add_batch14 import metro

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DAY = "2026-11-10"
AF = "Афиша, раздел «Детские музеи» (afisha.ru/msk/museum/kids, 10.11.2026)"
ROWS = []


def add(pid, name, typ, cats, tags, addr, ll, a0, a1, d0, d1, energy, plus, acc, adult=2, how=None, stroller="частично"):
    lat, lon = ll
    r = P(pid, name, typ, metro(lat, lon), addr, lat, lon, a0, a1, d0, d1, energy, tags, None, None, None, "да",
          plus, "", adult=adult, src=AF, acc=acc, booking="желательна", food="нет", stroller=stroller)
    r["Сайт"] = ""
    r["Категории"] = cats
    r["Проверено (дата)"] = DAY
    if how:
        r["Как найти"] = how
    ROWS.append(r)


add("fso-garage-museum-vdnh", "Музей гаража особого назначения ФСО России (ВДНХ)", "музей", "museums,transport",
    "техника, история и наука", "пр-т Мира, 119, стр. 53, 54, ВДНХ", (55.8300, 37.6310), 5, 16, 60, 120, "средне",
    "Музей гаража особого назначения в павильонах 53 и 54 на ВДНХ",
    "приблизительно, ±1 км (ВДНХ)", adult=3, how="Павильоны 53 и 54 на ВДНХ")
add("pokrovsky-sobor-red-square", "Покровский собор (храм Василия Блаженного)", "музей-храм", "museums,tours",
    "история и наука", "Красная пл., 7", (55.752523, 37.623087), 6, 16, 45, 90, "спокойно",
    "Традиционный символ Москвы, который можно рассмотреть снаружи и изнутри: музей на Красной площади",
    "приблизительно, ±300 м", adult=3, stroller="нет")
add("mamm-ostozhenka", "Мультимедиа Арт Музей (МАММ)", "музей", "museums",
    "творчество", "ул. Остоженка, 16", (55.7413, 37.6000), 7, 16, 60, 90, "спокойно",
    "Пространство мультимедийных технологий и искусства фотографии у метро «Кропоткинская»",
    "приблизительно, ±300 м", adult=3)

if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    allids = {x["id"] for x in json.load(open(os.path.join(ROOT, "places.json")))["places"]}
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    ids = [r["id"] for r in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    assert not [i for i in ids if i in existing or i in allids], [i for i in ids if i in existing or i in allids]
    for row_ in ROWS:
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        r = ws.max_row + 1
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=r, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    print("rows", len(ROWS), "total", ws.max_row - 1)
