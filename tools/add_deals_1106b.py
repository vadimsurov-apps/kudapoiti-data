"""Робот акций 06.11 вечер (тема: дни рождения): батутный центр «Высота» (Митино) с живыми акциями.
Координаты — точка ТРЦ «Митино Парк» (Дубравная, 51с1), приблизительно."""
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import SRC
from add_batch14 import play

ROWS = []
r = play("vysota-mitino", "Батутный центр «Высота» (Митино)", "батутный центр", 55.85363, 37.35311,
         "https://vysota-park.ru/", 3, 1150,
         "37 батутов, поролоновая яма, верёвочный парк, лабиринт и детский городок 0+ в одном месте",
         "Детям 3–6 лет на батутной арене — только со взрослым; в выходные дороже",
         "trampolines", hours="ежедневно 10:00–22:00", addr="Дубравная ул., 51, стр. 1")
r["Точность координат"] = "приблизительно, ±500 м"
r["Источник"] = "сайт места; акции проверены 2026-11-06"
r["Проверено (дата)"] = "2026-11-06"
ROWS.append(r)

if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=i, column=1).value for i in range(2, ws.max_row + 1)}
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    for row in ROWS:
        assert row["id"] not in existing, row["id"]
        assert not (set(row) - set(hdr)), (row["id"], set(row) - set(hdr))
        n = ws.max_row + 1
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=n, column=i, value=row.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    for x in ROWS: print(x["id"], "|", x["Метро"])
