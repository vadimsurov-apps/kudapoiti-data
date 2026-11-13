"""Робот edu, 2026-11-13 (двадцать первый запуск): новые места — карточки Яндекс Карт *-ev<N>-1131e* (tools/edu_1131_sel.py), точка — справка OSM edu36-*.
Строка таблицы — функция row() из add_edu_1121.py. Запуск: KP_PART=edu python3 tools/add_edu_1131.py [--dry]"""
import json, os, sys, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
with contextlib.redirect_stdout(io.StringIO()):
    import add_edu_1126 as A26
A = A26.A
from batch_helpers import SRC
from edu_1131_sel import SEL as SEL30, SITE_SRC as SS30, HOW_FIX as HF30, ADDR_FIX
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
HERE = os.path.dirname(os.path.abspath(__file__))
A.E.update({"31:" + k: v for k, v in json.load(open(os.path.join(HERE, "edu_1131_ext.json"))).items()})
_pp = os.path.join(HERE, "edu_1131_points.json")
P30 = json.load(open(_pp)) if os.path.exists(_pp) else {}
A.PTS.update(P30)
A.TOWNS = A.TOWNS + tuple(t for t in ("Одинцово", "Видное", "Московский", "Балашиха", "Мытищи", "Краснознаменск", "Звенигород", "Дедовск", "Троицк", "Павловский Посад", "Красногорск", "Талдом", "Шатура", "Луховицы", "Ленинский г. о.", "Лосино-Петровский", "Щёлково", "Руза") if t not in A.TOWNS)
A.YA = "Яндекс Карты: карточка организации (рубрика, адрес, этаж/вход, телефон, сайт, услуги, цены и возраст групп, доступность), выдача «{q}», 13.11.2026"
A.TOWNS = A.TOWNS + tuple(t for t in ("Солнечногорск", "Химки", "Долгопрудный") if t not in A.TOWNS)
A.SEL.update(SEL30); A.SITE_SRC.update(SS30); A.HOW_FIX.update(HF30)
IDS = [p for p in SEL30 if p in P30]
ROWS = []
for p in IDS:
    A.DT = "2026-11-13"
    r = A.row(p)
    if p in ADDR_FIX:
        r["Адрес"] = ADDR_FIX[p]
    if p.startswith("gppc-"):
        r["Сайт"] = "https://gppc.ru/"
    if not r.get("Как найти"):
        r["Как найти"] = None
    ROWS.append(r)

if __name__ == "__main__":
    pa = json.load(open(os.path.join(ROOT, "places-all.json")))
    PL = {p["id"] for p in (pa["places"] if isinstance(pa, dict) else pa)}
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    ids = [r["id"] for r in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    ROWS = [r for r in ROWS if r["id"] not in existing and r["id"] not in PL]
    if "--dry" in sys.argv:
        for r in ROWS: print(r["id"], "|", r["Адрес"], "|", (r["Как найти"] or "").replace("\n", " / "), "|", r["Метро"], "|", r["Сайт"], "|", r["Категории"], r["Возраст от"], r["Возраст до"], "|", r["Точность координат"][:40])
        print(len(ROWS)); sys.exit()
    r0 = ws.max_row + 1
    while r0 > 2 and ws.cell(row=r0 - 1, column=1).value is None: r0 -= 1
    for k, row_ in enumerate(ROWS):
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=r0 + k, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    print("rows", len(ROWS))
