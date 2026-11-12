"""Робот edu, 2026-11-12 (двенадцатый запуск): 1) места, отложенные одиннадцатым запуском (карточки, точки и иконки готовы:
tools/edu_1121_sel.py, edu_1121_points.json, icons_edu_1121.py); 2) новые — карточки Яндекс Карт *-ev<N>-1122e* (tools/edu_1122_sel.py).
Строка таблицы — та же функция row(), что в add_edu_1121.py. Запуск: KP_PART=edu python3 tools/add_edu_1122.py [--dry]"""
import json, os, sys, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
import add_edu_1121 as A
from batch_helpers import SRC
from edu_1122_sel import SEL as SEL22, SITE_SRC as SS22, HOW_FIX as HF22, TAKE as TAKE22
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
HERE = os.path.dirname(os.path.abspath(__file__))
DEFERRED = open(os.path.join(HERE, "edu_1122_deferred.txt")).read().split()
A.E.update({"22:" + k: v for k, v in json.load(open(os.path.join(HERE, "edu_1122_ext.json"))).items()})
_pp = os.path.join(HERE, "edu_1122_points.json")
A.PTS.update(json.load(open(_pp)) if os.path.exists(_pp) else {})
A.TOWNS = A.TOWNS + ("Балашиха", "Дмитров", "Подольск")
A.SEL.update(SEL22); A.SITE_SRC.update(SS22); A.HOW_FIX.update(HF22)
SEL = A.SEL
IDS = [p for p in DEFERRED if p in A.PTS] + [p for p in SEL22 if p in A.PTS and p in TAKE22]
ROWS = [A.row(p) for p in IDS]

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
        for r in ROWS: print(r["id"], "|", r["Адрес"], "|", (r["Как найти"] or "").replace("\n", " / "), "|", r["Метро"], "|", r["Сайт"])
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
