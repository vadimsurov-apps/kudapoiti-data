"""Робот edu, 2026-11-11 (пятый запуск): поиск по районам Выставочная, Выставочный центр, Давыдково, Деловой центр, Динамо,
Дмитровская, Добрынинская, Домодедовская, Достоевская, Дубровка, Жулебино, ЗИЛ, Электросталь, Коломна, Домодедово.
Выдачи Яндекс Карт (auto/pages *-eu<N>-1115e*), каждое место сверено с карточкой организации (*-ev<N>-1115e*).
Точка — справка OSM (edu15-*), tools/edu_1115_pick.py. WebFetch не использовался.
Запуск: KP_PART=edu python3 tools/add_edu_1115.py [--dry]"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC
from edu_1115_sel import SEL

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
HERE = os.path.dirname(os.path.abspath(__file__))
DT = "2026-11-11"
PTS = json.load(open(os.path.join(HERE, "edu_1115_points.json")))
ADDR = json.load(open(os.path.join(HERE, "edu_1115_addr.json")))
YA = "Яндекс Карты: карточка организации (рубрика, адрес, этаж/вход, телефон, сайт, услуги, цены и возраст групп), выдача «{q}», 11.11.2026"
HOW = {k: v.get("how") for k, v in ADDR.items()}


def row(n):
    pid, name, typ, cats, a0, a1, price, note, plus, tags, trial = SEL[n]
    a = ADDR[pid]
    lat, lon, acc = PTS[pid]
    addr = a["addr"]
    if addr.endswith(", Москва"):
        addr = "Москва, " + addr[:-8]
    elif not addr.startswith(("Москва", "Реутов", "Долгопрудный", "Жуковский", "Видное", "Пушкино", "Красногорск", "Мытищи", "Люберцы", "Электросталь", "Домодедово", "Коломна", "Дубна", "Клин", "Ивантеевка")):
        addr = "Москва, " + addr
    r = P(pid, name, typ, metro(lat, lon), addr, lat, lon, a0, a1, 45, 60, "спокойно", tags, price, note, None, "да",
          plus, None, adult=1, src=YA.format(q=a["q"].replace(" | ", " метро ")), acc=acc, adult_price=None,
          booking="обязательна", loud="нет", sit="частично", crowd="нет", food="нет", stroller="частично")
    r["Взрослый билет, ₽"] = None
    r["Сайт"] = a["site"]
    r["Категории"] = cats
    r["Как найти"] = HOW.get(pid)
    r["Проверено (дата)"] = DT
    r["Коляска"] = None   # правило 9: только по источнику — в карточке нет
    r["Громко"] = None    # правило 7: «Шумно» только по источнику
    return r


ROWS = [row(n) for n in SEL if SEL[n][0] in PTS]

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
    ROWS = [r for r in ROWS if r["id"] not in existing and r["id"] not in PL]   # повторный запуск: только новые
    if "--dry" in sys.argv:
        print(len(ROWS)); sys.exit()
    r0 = 2 if ws.max_row == 1 or ws.cell(row=2, column=1).value is None else ws.max_row + 1
    for n, row_ in enumerate(ROWS):
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        r = r0 + n
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=r, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    print("rows", len(ROWS))

