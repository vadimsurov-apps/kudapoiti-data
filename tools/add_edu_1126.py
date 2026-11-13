"""Робот edu, 2026-11-13 (шестнадцатый запуск): 1) места, отложенные запуском 1125 (иконки готовы, точка — повторная справка OSM
edu26-*, улицы с «ё»); 2) новые — карточки Яндекс Карт *-ev<N>-1126e* (tools/edu_1126_sel.py), точка — справка OSM edu27-*.
Строка таблицы — функция row() из add_edu_1121.py. Запуск: KP_PART=edu python3 tools/add_edu_1126.py [--dry]"""
import json, os, sys, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
with contextlib.redirect_stdout(io.StringIO()):
    import add_edu_1125 as A25
A = A25.A
from batch_helpers import SRC
from edu_1126_sel import SEL as SEL26, SITE_SRC as SS26, HOW_FIX as HF26, ADDR_FIX
from edu_1125_sel import SEL as SEL25
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
HERE = os.path.dirname(os.path.abspath(__file__))
A.E.update({"26:" + k: v for k, v in json.load(open(os.path.join(HERE, "edu_1126_ext.json"))).items()})
_pp = os.path.join(HERE, "edu_1126_points.json")
P26 = json.load(open(_pp)) if os.path.exists(_pp) else {}
A.PTS.update(P26)
A.TOWNS = A.TOWNS + tuple(t for t in ("Одинцово", "Видное", "Московский", "Балашиха", "Мытищи") if t not in A.TOWNS)
A.SEL.update(SEL26); A.SITE_SRC.update(SS26); A.HOW_FIX.update(HF26)
DEF = [p for p in SEL25 if p in P26]
NEW = [p for p in SEL26 if p in P26]
IDS = DEF + NEW
ROWS = []
for p in IDS:
    A.DT = "2026-11-13"
    r = A.row(p)
    if p in ADDR_FIX:
        r["Адрес"] = ADDR_FIX[p]
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
