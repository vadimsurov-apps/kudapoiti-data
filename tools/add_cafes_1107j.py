"""Робот cafes, 2026-11-07 (22 UTC): 24 кафе и ресторанов с детской комнатой.
Данные — tools/cafes_1107j_data.py. Детская комната — по справочникам jsprav.ru (кэш auto/pages).
Координаты приблизительные (уточнит geocode-address.yml). Запуск: KP_PART=cafes python3 tools/add_cafes_1107j.py"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC
from cafes_1107j_data import DATA

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PLACES = {p["id"]: p for p in json.load(open(os.path.join(ROOT, "places.json")))["places"]}
DAY = "2026-11-07"


def row(d):
    pid, name, addr, lat, lon, src, plus, acc = d
    hours = None
    where = "справочнику jsprav.ru (метка «Кафе с детской комнатой»)"
    minus = f"Детская комната — по {where}; что в ней есть, часы работы и аниматоров уточняйте по телефону"
    r = P(pid, name, "кафе", metro(lat, lon), addr, lat, lon, 0, 12, 60, 150, "спокойно", "творчество", None,
          "средний чек — уточняйте", hours, "да", plus, minus, adult=3, src=src, acc=acc,
          booking="желательна", loud="частично", food="да", stroller="да")
    r["Сайт"] = None
    r["Категории"] = "food"
    r["Проверено (дата)"] = DAY
    return r


ROWS = [row(d) for d in DATA]

if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    ids = [r["id"] for r in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    assert not [i for i in ids if i in existing or i in PLACES], [i for i in ids if i in existing or i in PLACES]
    for row_ in ROWS:
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        r = ws.max_row + 1
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=r, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    print("rows", len(ROWS), "total", ws.max_row - 1)
