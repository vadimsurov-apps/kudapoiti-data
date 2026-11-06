"""Робот акций 06.11 (тема: квесты, картинг, скалодромы): два детских картинга с живыми акциями.
Координаты приблизительные (по адресу с сайта, без OSM)."""
import os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import SRC
from add_batch14 import base

SRCN = "сайт места; акция проверена 2026-11-06"


def kart(pid, name, lat, lon, addr, site, a0, a1, price, plus, minus, hours):
    r = base(pid, name, "картинг", lat, lon, a0, a1, 60, 90, "активно", "транспорт, спорт и активность", price,
             "цена «от» за занятие школы", hours, "да", plus, minus, site, "karting", addr=addr,
             booking="обязательна", loud="да", food="нет", stroller="нет", adult=2)
    r["Точность координат"] = "приблизительно, ±1 км"
    r["Источник"] = SRCN
    r["Проверено (дата)"] = "2026-11-06"
    return r


ROWS = [
    kart("miks-karting-academy", "MIKS Karting Academy — детская школа картинга", 55.7175, 37.6825,
         "Шарикоподшипниковская ул., 13, стр. 41", "https://miks-karting.ru/children/", 6, 16, 3000,
         "Школа картинга для детей 6–16 лет: младшая группа с роста 123 см, свой крытый трек",
         "Пробное занятие платное; абонементы без переносов дешевле",
         "пн 14:00–00:00, вт–пт 12:00–00:00, сб–вс 13:00–00:00"),
    kart("dozari-kart", "Dozari Kart — детская школа картинга (ТЦ «Шоколад»)", 55.7598, 37.8430,
         "Реутов, МКАД 2-й км, ТЦ «Шоколад», крытый паркинг, уровень E", "https://школа-картинга.рф/школа", 6, 15, 5000,
         "Крытый картинг на парковке ТЦ, группы для юных картингистов 6–15 лет",
         "Трасса на подземном паркинге — шумно, тёплая одежда не помешает", "ежедневно 12:00–23:00"),
]

if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    for row in ROWS:
        assert row["id"] not in existing, row["id"]
        assert not (set(row) - set(hdr)), (row["id"], set(row) - set(hdr))
        r = ws.max_row + 1
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=r, column=i, value=row.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    for r in ROWS: print(r["id"], "|", r["Метро"])
