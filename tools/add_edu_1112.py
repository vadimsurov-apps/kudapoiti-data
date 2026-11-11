"""Робот edu, 2026-11-11 (второй запуск): поиск по районам Арбатская, Аэропорт, Аэропорт Внуково, Бабушкинская,
Багратионовская, Балтийская, Баррикадная, Бауманская, Беговая, Белокаменная, Белорусская, Мытищи, Люберцы, Красногорск.
Запросы Яндекс Карт по 8 темам (Action sites.yml → auto/pages, ключи *-eu<N>-1112a*), карточки организаций
(*-ev<N>-1112a*): рубрика, адрес, телефон, сайт, услуги с ценами и возрастами. WebFetch не использовался.
Точка — справка OSM (auto/osm-answers.json, edu12-*): объект OSM места или здание строго по адресу.
Отброшены: Санкт-Петербург в выдаче, взрослые клиники, частные школы и сады без детских курсов, дубли (Притяжение,
Семейная академия, Траектория взлёта, Polycent, Лисёнок Монтессори), карточки-списки без телефона/сайта (на следующий запуск).
Запуск: KP_PART=edu python3 tools/add_edu_1112.py [--dry]"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC
from edu_1112_data import D
from edu_1112_sel import SEL

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DT = "2026-11-11"
PTS = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "edu_1112_points.json")))
ADDR = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "edu_1112_addr.json")))
YA = "Яндекс Карты: выдача «{q}» и карточка организации (рубрика, адрес, телефон, сайт, услуги и цены), 11.11.2026"


def row(n):
    key, cats, a0, a1, price, note = SEL[n]
    name, typ, plus, minus, how, tags = D[n]
    site = ADDR[key].get("site")
    lat, lon, acc = PTS[key]
    r = P(key, name, typ, metro(lat, lon), ADDR[key]["addr"], lat, lon, a0, a1, 45, 60, "спокойно",
          tags or "творчество", price, note, None, "да", plus, minus, adult=1,
          src=YA.format(q=ADDR[key]["q"]), acc=acc, adult_price=0 if price else None, booking="обязательна",
          loud="нет", sit="частично", crowd="нет", food="нет", stroller="частично")
    r["Сайт"] = site
    r["Категории"] = cats
    r["Как найти"] = how
    r["Проверено (дата)"] = DT
    return r


ROWS = [row(n) for n in SEL if SEL[n][0] in PTS]

if __name__ == "__main__":
    PL = {p["id"] for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    ids = [r["id"] for r in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    assert not [i for i in ids if i in existing or i in PL], [i for i in ids if i in existing or i in PL]
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
