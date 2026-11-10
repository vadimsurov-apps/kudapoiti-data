"""Робот cafes, 2026-11-10 (16:40 UTC): районы Алма-Атинская…Одинцово (14). WebSearch отдаёт только заголовки,
yandex.* в спам-списке (очередь не скачается), кэш restoran.cafe уже разобран. Источник новых мест — кэш карточек
Яндекс Карт (auto/pages/yandex-*): в «Особенностях» заведения отмечена «Детская комната», рубрика, адрес, средний счёт.
Координаты приблизительные — точку уточнит сверка с OSM (osm-local.yml); до этого место скрыто.
Запуск: KP_PART=cafes python3 tools/add_cafes_1110e.py"""

import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PLACES = {p["id"]: p for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
DAY = "2026-11-10"
YA = "Яндекс Карты (карточка заведения: «Особенности» — детская комната, рубрика, адрес)"
RC = "restoran.cafe (карточка заведения в подборке: адрес, формат, средний чек, детская/аниматор)"
A1 = "приблизительно, ±1 км (по адресу, уточнить)"
# id, название, тип, адрес, lat, lon, плюс, минус, средний чек, сайт, источник
DATA = [
 ("cafe-village-house-stupino", "Village House (Ступино)", "ресторан с детской игровой комнатой",
  "Ступино, ул. Горького, вл. 20, стр. 2", 54.8925, 38.0640,
  "Ресторан в Ступине с авторской и классической кухней: бургеры, стейки, чизкейки. Есть детская игровая комната",
  None, None, None, YA),
 ("cafe-piponi-svyatoozerskaya", "Пипони (Святоозёрская)", "пиццерия с детской комнатой",
  "Святоозёрская ул., 18, 1 этаж", 55.7155, 37.8700,
  "Пиццерия в Косине: римская пепперони и другая пицца, доставка по Кожухову, Некрасовке и Люберцам. В зале есть детская комната",
  None, None, "https://pizzapiponi.ru/", YA + "; https://pizzapiponi.ru/"),
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
