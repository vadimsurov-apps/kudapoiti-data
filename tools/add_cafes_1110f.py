"""Робот cafes, 2026-11-10 (20:30 UTC): районы Авиамоторная…Беговая (15). Поиск Яндекс Карт (кэш *-kcz*-1110z, карточки *-kcc*-1110y).
Детская подтверждена карточкой Яндекса (аспект отзывов «Детская комната», подборка «с детской комнатой»).
Координаты приблизительные (соседнее здание/тот же дом) — точку уточнит сверка с OSM (osm-local.yml); до этого место скрыто.
Запуск: KP_PART=cafes python3 tools/add_cafes_1110f.py"""

import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PLACES = {p["id"]: p for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
DAY = "2026-11-10"
YA2 = "Яндекс Карты (карточка: «Кафе, организация детских праздников», отзывы «Детская комната» 327 и «Детская анимация», ср. счёт 1200–1500 ₽, новость сети о бесплатной игровой с аниматором)"
YA3 = "Яндекс Карты (выдача и карточка: подборка «Рестораны и кафе с детской комнатой в Москве (Новая Москва)», адрес и вход)"
YA = "Яндекс Карты (карточка заведения: «Особенности» — детская комната, рубрика, адрес)"
RC = "restoran.cafe (карточка заведения в подборке: адрес, формат, средний чек, детская/аниматор)"
A1 = "приблизительно, ±1 км (по адресу, уточнить)"
# id, название, тип, адрес, lat, lon, плюс, минус, средний чек, сайт, источник
DATA = [
 ("cafe-anderson-taganskaya", "АндерСон (Таганская)", "семейное кафе-кондитерская с детской игровой",
  "Таганская ул., 36, стр. 1", 55.738401, 37.666043,
  "Семейное кафе-кондитерская сети «АндерСон» рядом с Детским театром эстрады: сырники, супы, торты. Бесплатная игровая с аниматором, здесь устраивают детские праздники; родители хвалят детскую комнату и анимацию",
  None, 1350, "https://cafe-anderson.ru/", YA2),
 ("cafe-sinergiya-vnukovo", "Синергия Кафе (Внуково)", "семейное кафе с детской комнатой",
  "ул. Анны Ахматовой, 11, корп. 3 (вход со двора, первый)", 55.633484, 37.328468,
  "Семейное кафе во Внукове, в том же доме, что и Академия хореографии «Синергия». Есть детская комната",
  None, None, None, YA3),
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
