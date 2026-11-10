"""Робот cafes, 2026-11-10 (22:40 UTC): районы Белокаменная…Верхние Котлы (15). Поиск Яндекс Карт (кэш *-kcz*-1111a, карточки *-kcn*-1111b).
Детская подтверждена карточкой Яндекса (рубрика / аспекты отзывов «Детская комната», «Детская анимация», отзывы, подборки «кафе с игровыми»).
Координаты — здание по адресу (Яндекс Карты); вход/объект уточнит сверка с OSM (osm-local.yml), до этого место скрыто.
Запуск: KP_PART=cafes python3 tools/add_cafes_1110g.py"""

import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PLACES = {p["id"]: p for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
DAY = "2026-11-10"
YA = "Яндекс Карты (карточка заведения 10.11: рубрика, адрес, отзывы о детской комнате)"
A1 = "дом по адресу (Яндекс Карты, координаты здания)"
# id, название, тип, адрес, lat, lon, плюс, минус, средний чек, сайт, источник
DATA = [
 ("cafe-trolli-kids-krasnobogatyrskaya", "Тролли Кидс", "семейный ресторан с детской игровой",
  "Краснобогатырская ул., 90, стр. 2", 55.800428, 37.710063,
  "Детский ресторан на Краснобогатырской улице: в зале игровая зона, с детьми занимаются аниматоры и няни",
  None, None, None, "Яндекс Карты (карточка: рубрика «Ресторан», подборки «Кафе с игровыми», «Рестораны Москвы с услугами няни и детскими игровыми зонами», «Рестораны с аниматорами для детей», адрес)"),
 ("cafe-maxlevel-novodanilovskaya", "МаксЛевел", "ресторан с детской комнатой",
  "Новоданиловская наб., 6, корп. 2", 55.697711, 37.625262,
  "Ресторан на Новоданиловской набережной. На первом этаже — огромная трёхэтажная детская комната с горками и сухим бассейном, с детьми играет аниматор; родители хвалят и комнату, и аниматора",
  None, None, None, "Яндекс Карты (карточка: «Ресторан, кафе, бар», аспекты «Детская комната» 80%, «Детская анимация» 92%, отзывы, адрес)"),
 ("cafe-yug-novodmitrovskaya", "Yug (Большая Новодмитровская)", "кафе-ресторан с детской комнатой",
  "Большая Новодмитровская ул., 36, стр. 9", 55.805528, 37.584460,
  "Кафе-ресторан на Большой Новодмитровской: пицца, рыба, десерты. Есть детская игровая комната, детям нравится",
  None, None, None,
  "Яндекс Карты (карточка: «Кафе, ресторан, быстрое питание», «Детская комната» в особенностях, аспект «Детская комната» 83%, отзывы, адрес)"),
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
