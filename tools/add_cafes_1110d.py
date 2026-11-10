"""Робот cafes, 2026-11-10 (08:00 UTC): районы Терехово…Университет (14 станций). Поиск Яндекс Карт недоступен (все домены yandex.* в
auto/spam-domains.txt — очередь 1110j не скачается), WebSearch отдаёт только заголовки подборок. Источник — каталог
restoran.cafe (кэш auto/pages/restoran-cafe-*): карточка заведения с адресом, форматом, средним чеком и описанием
детской/аниматора. Взяты только места, где детская или аниматор описаны конкретно (дни и часы), и которых нет в базе.
Координаты приблизительные — точку уточнит сверка с OSM (osm-local.yml); до этого место скрыто.
Запуск: KP_PART=cafes python3 tools/add_cafes_1110d.py"""

import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PLACES = {p["id"]: p for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
DAY = "2026-11-10"
RC = "restoran.cafe (карточка заведения в подборке: адрес, формат, средний чек, детская/аниматор)"
A1 = "приблизительно, ±1 км (по адресу, уточнить)"
# id, название, тип, адрес, lat, lon, плюс, минус, средний чек, сайт, источник
DATA = [
 ("cafe-klevo-usacheva", "Клёво (Усачёвский рынок)", "рыбный ресторан с аниматором по выходным",
  "ул. Усачёва, 26, Усачёвский рынок", 55.7283, 37.5673,
  "Ресторан Аркадия Новикова на Усачёвском рынке: средиземноморская кухня, свежие черноморские морепродукты. По субботам и воскресеньям аниматор играет с детьми, рисует и мастерит поделки",
  "Аниматор только по выходным, 15:00–19:00", 3000, None, RC),
 ("cafe-prokhinkali-butyrskaya", "PRO.Хинкали (Бутырская)", "грузинская хинкальная с аниматором по выходным",
  "Бутырская ул., 69–71, стр. 1", 55.8060, 37.5830,
  "Хинкальная и ресторан грузинской кухни у метро Дмитровская: хинкали и известные блюда разных регионов Грузии. По выходным с детьми занимается аниматор",
  "Аниматор только по субботам и воскресеньям, 14:00–20:00", 3500, None, RC),
 ("cafe-bereg-strogino", "Берег (Строгино)", "ресторан с аниматором по воскресеньям",
  "ул. Исаковского, 37, корп. 2, стр. 1", 55.7935, 37.4125,
  "Ресторан в Строгинском лесопарке с видом на залив и открытой террасой, интерьер из натуральных материалов. Есть детское меню, устраивают детские праздники, по воскресеньям аниматор мастерит с детьми поделки",
  "Аниматор только по воскресеньям, 14:00–19:00", 3000, None, RC),
 ("cafe-uspenskie-vstrechi", "Успенские встречи (Успенское)", "загородный ресторан с аниматором и няней",
  "Одинцовский г.о., с. Успенское, стр. 72", 55.7270, 37.1200,
  "Загородный ресторан на Рублёвке: авторская итальянская и восточная кухня, халяльные блюда, летняя терраса. С детьми занимаются аниматор и няня",
  "Без машины добираться неудобно", 3000, None, RC),
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
