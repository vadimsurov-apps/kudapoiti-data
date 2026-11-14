"""Робот edu, 2026-11-14 (двадцать третий запуск): новые места — карточки Яндекс Карт *-ev<N>-1133e* и *-ev<N>-1133g* (tools/edu_1133_sel.py), точка — справка OSM edu38-*.
Строка таблицы — функция row() из add_edu_1121.py. Запуск: KP_PART=edu python3 tools/add_edu_1131.py [--dry]"""
import json, os, sys, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
with contextlib.redirect_stdout(io.StringIO()):
    import add_edu_1132 as A31
A = A31.A
from batch_helpers import SRC
from edu_1133_sel import SEL as SEL30, SITE_SRC as SS30, HOW_FIX as HF30, ADDR_FIX
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
HERE = os.path.dirname(os.path.abspath(__file__))
A.E.update({"33:" + k: v for k, v in json.load(open(os.path.join(HERE, "edu_1133_ext.json"))).items()})
_e2 = os.path.join(HERE, "edu_1133_ext2.json")
if os.path.exists(_e2): A.E.update({"33g:" + k: v for k, v in json.load(open(_e2)).items()})
_pp = os.path.join(HERE, "edu_1133_points.json")
P30 = json.load(open(_pp)) if os.path.exists(_pp) else {}
A.PTS.update(P30)
A.TOWNS = A.TOWNS + tuple(t for t in ("Одинцово", "Видное", "Московский", "Балашиха", "Мытищи", "Краснознаменск", "Звенигород", "Дедовск", "Троицк", "Павловский Посад", "Красногорск", "Талдом", "Шатура", "Луховицы", "Ленинский г. о.", "Лосино-Петровский", "Щёлково", "Руза") if t not in A.TOWNS)
A.YA = "Яндекс Карты: карточка организации (рубрика, адрес, этаж/вход, телефон, сайт, услуги, цены и возраст групп, доступность), выдача «{q}», 14.11.2026"
A.TOWNS = A.TOWNS + tuple(t for t in ("Солнечногорск", "Химки", "Долгопрудный", "Подольск", "Королёв", "Люберцы", "Раменское", "Электросталь") if t not in A.TOWNS)
A.SEL.update(SEL30); A.SITE_SRC.update(SS30); A.HOW_FIX.update(HF30)
_old_page = A.page
def _page(n):
    a, b = n.split(":")
    if a == "33g":
        import glob as _g
        f = _g.glob(os.path.join(ROOT, f"auto/pages/*-ev{b}-1133g-*.txt"))[0]
        secs = open(f).read().split("\n### ")
        return [l.strip() for l in "\n".join([secs[0]] + [s for s in secs[1:] if s.startswith("https://yandex.ru/maps/org/")]).splitlines() if l.strip()]
    return _old_page(n)
A.page = _page
IDS = [p for p in SEL30 if p in P30]
ROWS = []
for p in IDS:
    A.DT = "2026-11-14"
    r = A.row(p)
    if p in ADDR_FIX:
        r["Адрес"] = ADDR_FIX[p]
    import re as _re  # 14.11 (24-й запуск): «Москва, Коломна, …» из карточки Яндекса — Коломна/Домодедово не Москва
    if r.get("Адрес"): r["Адрес"] = _re.sub(r"^Москва, (?=(Коломна|Домодедово|Химки|Красногорск|Электросталь|Одинцово|Балашиха|Мытищи|Подольск),)", "", r["Адрес"])
    if r.get("Метро") and r["Метро"].startswith("—"):
        r["Метро"] = None
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
