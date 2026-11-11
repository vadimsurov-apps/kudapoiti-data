"""Робот cafes, 2026-11-11 (07 UTC): 15 районов (Выставочный центр…Крымская). Поиск Яндекс Карт
(кэш *-kfz/kfr*-1111g), карточки *-kfn*-1111g, координаты здания по адресу *-kfa*-1111g.
Детская подтверждена карточкой Яндекса (аспект отзывов «Детская комната», подборки «с детской/игровой комнатой»).
Координаты — здание по адресу (Яндекс Карты); вход/объект уточнит сверка с OSM (osm-local.yml), до этого место скрыто.
Запуск: KP_PART=cafes python3 tools/add_cafes_1111d.py"""

import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PLACES = {p["id"]: p for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
DAY = "2026-11-11"
YA = "Яндекс Карты (карточка заведения 11.11: рубрика, адрес, отзывы о детской комнате)"
A1 = "дом по адресу (Яндекс Карты, координаты здания)"
# id, название, тип, адрес, lat, lon, плюс, минус, средний чек, сайт, источник
DATA = [
 ("cafe-tanuki-profsoyuznaya-126", "Тануки (Профсоюзная, 126)", "ресторан японской кухни с детской комнатой",
  "Профсоюзная ул., 126, корп. 3", 55.630370, 37.516853,
  "Ресторан-суши-бар «Тануки» на Профсоюзной у метро «Коньково»: роллы, суши, рамен, том ям, десерты. Есть детская комната и детское меню — родители в отзывах их хвалят",
  None, 1250, "https://tanukifamily.ru/", "Яндекс Карты (карточка: «Ресторан, суши-бар», средний счёт 1000–1500, аспекты «Детская комната» 82%, «Детское меню» 89%, адрес, телефон +7 (499) 649-22-23)"),
 ("cafe-la-piola-profsoyuznaya-109", "Ла Пиола (Профсоюзная, 109)", "итальянский ресторан-пиццерия с детской комнатой",
  "Профсоюзная ул., 109, корп. 2, 1 этаж", 55.632382, 37.519557,
  "Итальянский ресторан «Ла Пиола» на первом этаже дома на Профсоюзной, рядом с метро «Коньково»: пицца, паста, десерты, летом веранда. Есть детская комната — в отзывах её хвалят",
  None, 2000, "https://www.la-piola.ru/", "Яндекс Карты (карточка: «Ресторан», средний счёт 1500–2500, аспект «Детская комната» 88%, адрес, этаж, телефон +7 (915) 040-86-99); сайт la-piola.ru"),
]

def row(d):
    pid, name, typ, addr, lat, lon, plus, minus, check, site, src = d
    r = P(pid, name, typ, metro(lat, lon), addr, lat, lon, 0, 12, 60, 150, "спокойно", "творчество", None,
          None, None, "да", plus, minus, adult=3, src=src, acc=A1,
          booking="желательна", loud="частично", food="да", stroller="да")
    r["Взрослый билет, ₽"] = check
    r["Сайт"] = site
    r["Категории"] = "food"
    r["Проверено (дата)"] = DAY
    r["Источник"] += "; качество 2026-11"
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
