"""Робот edu, 2026-11-12/13 (тринадцатый запуск): 1) места, отложенные запусками 1120–1122 (карточки и точки готовы,
иконки — tools/icons_edu_1123.py); 2) новые — карточки Яндекс Карт *-ev<N>-1123e* (tools/edu_1123_sel.py).
Строка таблицы — та же функция row(), что в add_edu_1121.py. Запуск: KP_PART=edu python3 tools/add_edu_1123.py [--dry]"""
import json, os, sys, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
with contextlib.redirect_stdout(io.StringIO()):
    import add_edu_1122 as A22
A = A22.A
from batch_helpers import SRC
from edu_1123_sel import SEL as SEL23, SITE_SRC as SS23, HOW_FIX as HF23, TAKE as TAKE23, DEFERRED, TAKE_DEF
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
HERE = os.path.dirname(os.path.abspath(__file__))
for suf, fn in (("22y:", "edu_1122_ext2.json"), ("23:", "edu_1123_ext.json"), ("23y:", "edu_1123_ext2.json")):
    if os.path.exists(os.path.join(HERE, fn)):
        A.E.update({suf + k: v for k, v in json.load(open(os.path.join(HERE, fn))).items()})
_pp = os.path.join(HERE, "edu_1123_points.json")
A.PTS.update(json.load(open(_pp)) if os.path.exists(_pp) else {})
A.TOWNS = A.TOWNS + ("Балашиха", "Дмитров", "Подольск", "Королёв", "Ивантеевка", "Одинцово", "Домодедово", "Щёлково")
_page = A.page
def _page23(n):
    """второй заход тринадцатого запуска: «23y:N» — страницы *-ex<N>-1123e*"""
    if n.startswith("23y:"):
        import glob
        f = glob.glob(os.path.join(ROOT, f"auto/pages/*-ex{n[4:]}-1123e-*.txt"))[0]
        secs = open(f).read().split("\n### ")
        return [l.strip() for l in "\n".join([secs[0]] + [s for s in secs[1:] if s.startswith("https://yandex.ru/maps/org/")]).splitlines() if l.strip()]
    return _page(n)
A.page = _page23
A.SEL.update(SEL23); A.SITE_SRC.update(SS23); A.HOW_FIX.update(HF23)
SEL = A.SEL
IDS = [p for p in DEFERRED if p in A.PTS and p in TAKE_DEF] + [p for p in SEL23 if p in A.PTS and p in TAKE23]
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
        for r in ROWS: print(r["id"], "|", r["Адрес"], "|", (r["Как найти"] or "").replace("\n", " / "), "|", r["Метро"], "|", r["Сайт"], "|", r["Категории"], r["Возраст от"], r["Возраст до"])
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
