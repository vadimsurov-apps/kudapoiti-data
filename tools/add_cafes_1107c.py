"""Робот cafes, 2026-11-07 (утро): 32 кафе и ресторанов с детской комнатой/игровой зоной.
Данные — tools/cafes_1107c_data.json. Детская комната/игровая зона — по каталогам zoon.ru (фильтр «С детской комнатой», Химки/Мытищи/Москва) и restoran.cafe
(раздел «Детская комната» с описанием игровой). Координаты: «M:<метро>» — по станции, числа — приблизительно
по городу/адресу (уточнит geocode-address.yml).
Запуск: KP_PART=cafes python3 tools/add_cafes_1107c.py"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro, MET
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PLACES = {p["id"]: p for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
DATA = json.load(open(os.path.join(ROOT, "tools", "cafes_1107c_data.json")))
STN = {n.lower().replace("ё", "е"): (a, b) for n, a, b in MET}
DAY = "2026-11-07"


def loc(c):
    if isinstance(c, str) and c.startswith("P:"):
        p = PLACES[c[2:]]
        return p["lat"], p["lon"], "приблизительно, ±300 м (по соседнему месту в том же ТЦ)"
    if isinstance(c, str) and c.startswith("M:"):
        a, b = STN[c[2:].lower().replace("ё", "е")]
        return a, b, "приблизительно, ±1 км (по метро, уточнить)"
    if len(c) == 3:
        return c[0], c[1], c[2]
    return c[0], c[1], "приблизительно, ±1 км (по адресу, уточнить)"


def row(d):
    lat, lon, acc = loc(d["coord"])
    plus = d["plus"].replace(", бесплатные мастер-классы для детей 3–12 лет по выходным", ", бесплатные мастер-классы по выходным")
    mt = d.get("metro") or metro(lat, lon)
    note = f"средний чек ~{d['check']} ₽ на взрослого" if d["check"] else "средний чек — уточняйте"
    r = P(d["id"], d["name"], "кафе", mt, d["addr"], lat, lon, 0, 12, 60, 150, "спокойно", "творчество", None,
          note, d.get("hours"), "да", plus, d.get("minus") or "Детская — по описанию в каталоге ресторанов (restoran.cafe); часы работы детской и аниматоров уточняйте по телефону", adult=3, src=d["url"], acc=acc, adult_price=d["check"],
          booking="желательна", loud="частично", food="да", stroller="да")
    r["Сайт"] = d["url"]
    r["Категории"] = "food"
    r["День рождения"] = d.get("bday")
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
