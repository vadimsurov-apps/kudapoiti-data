"""Робот cafes, 2026-11-08 (13 UTC): 1 ресторан с детской комнатой (Коммунарка).
Источник — подборка restorating.ru «Рестораны с детской комнатой в Москве» (кэш auto/pages); детские праздники и
мастер-классы — по новостям заведения (заголовки restoclub в WebSearch). Остальные кэшированные каталоги уже выбраны.
Координаты приблизительные (уточнит сверка с OSM по адресу). Запуск: KP_PART=cafes python3 tools/add_cafes_1108e.py"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PLACES = {p["id"]: p for p in json.load(open(os.path.join(ROOT, "places.json")))["places"]}
DAY = "2026-11-08"
RC = "https://restoran.cafe/moskva/"
A = "приблизительно, ±1 км (по адресу, уточнить)"
A5 = "приблизительно, ±500 м (по адресу, уточнить)"

# id, название, адрес, lat, lon, источник, плюс, что в детской (или None), средний чек, точность
DATA = [
 ("cafe-taverna-robina-kommunarka", "Таверна Робина (Коммунарка)", "Скандинавский б-р, 3, корп. 2 (Коммунарка)", 55.5700, 37.4830,
  "https://www.restorating.ru/msk/best/child?page=2",
  "Семейный рестобар европейской кухни в стиле английской таверны Робина Гуда, детские праздники и мастер-классы · детская комната",
  None, 2500, A),
]


def row(d):
    pid, name, addr, lat, lon, src, plus, room, check, acc = d
    what = f"по подборке restorating.ru: {room}" if room else "по подборке restorating.ru «Рестораны с детской комнатой»"
    minus = f"Детская — {what}; часы работы детской и аниматоров уточняйте по телефону"
    note = f"средний чек ~{check} ₽" if check else "средний чек — уточняйте"
    r = P(pid, name, "кафе", metro(lat, lon), addr, lat, lon, 0, 12, 60, 150, "спокойно", "творчество", None,
          note, None, "да", plus, minus, adult=3, src=src, acc=acc,
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
