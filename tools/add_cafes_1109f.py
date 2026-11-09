"""Робот cafes, 2026-11-09 (20 UTC): районы Первомайская…Проспект Вернадского (поиск Яндекс Карт, кэш auto/pages,
ключи yandex-com-am …tcafx*-1109x и карточки …tcafy*-1109y) + каталог Restoran.cafe (кэш auto/pages/restoran-cafe-*).
Детская подтверждена аспектом отзывов Яндекса «Детская комната · N%» / подборками или каталогом с адресом (аниматор, часы).
Координаты приблизительные — точку уточнит сверка с OSM по адресу (osm-local.yml).
Запуск: KP_PART=cafes python3 tools/add_cafes_1109f.py"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PLACES = {p["id"]: p for p in json.load(open(os.path.join(ROOT, "places.json")))["places"]}
DAY = "2026-11-09"
YM = "Яндекс Карты (поиск по району и карточка заведения)"
RC = "Restoran.cafe (каталог «с аниматором»)"
A1 = "приблизительно, ±1 км (по адресу, уточнить)"
# id, название, тип, адрес, lat, lon, плюс, минус, средний чек, сайт, источник
DATA = [
 ("cafe-klevoe-bistro-cheremushkinsky", "Клёвое бистро (Черёмушкинский рынок)", "рыбный ресторан с аниматором по воскресеньям",
  "ул. Вавилова, 64/1, стр. 1 (Черёмушкинский рынок)", 55.6943, 37.5458,
  "Рыбный ресторан Аркадия Новикова на Черёмушкинском рынке: средиземноморская кухня, есть детское меню. По воскресеньям с 13:00 до 19:00 аниматор играет с детьми, рисует и делает с ними поделки",
  "Аниматор только по воскресеньям", 2500, None, RC + ": аниматор по вс 13:00–19:00, детское меню, средний чек 2500 ₽"),
 ("cafe-bochka-1905", "Бочка (ул. 1905 года)", "мясной ресторан с аниматором по выходным",
  "ул. 1905 года, 2", 55.7631, 37.5616,
  "Мясной ресторан в стиле альпийского шале у метро «Улица 1905 года»: русская и европейская кухня, детское меню, детские стульчики и игры. По субботам и воскресеньям с 13:00 до 18:00 с детьми занимается аниматор. Есть своя парковка",
  "Аниматор только по выходным; бывают спортивные трансляции", 5000, None, RC + ": аниматор сб–вс 13:00–18:00, детское меню, средний чек 5000 ₽"),
 ("cafe-casa-famiglia-perovo", "Casa di Famiglia (Перово, 2-я Владимирская)", "ресторан-пиццерия с детской комнатой",
  "2-я Владимирская ул., 18/7", 55.7535, 37.7855,
  "Итальянский ресторан-пиццерия в Перове: паста, пицца, детское меню; есть детская комната, проходит детская анимация",
  None, 2150, "https://casadifamiglia.ru/", YM + ": отзывы — детская комната 81%, детская анимация 86%, детское меню 87%; подборка «Рестораны Москвы с аниматорами для детей»; средний счёт 1800–2500 ₽"),
 ("cafe-shikari-columbus", "Шикари (ТРЦ «Columbus»)", "ресторан паназиатской кухни с детской комнатой",
  "Кировоградская ул., 13А, ТРЦ «Columbus», 4 этаж", 55.6115, 37.6070,
  "Ресторан паназиатской кухни на 4 этаже ТРЦ «Columbus»: роллы, том-ям, удон, фо-бо; есть детское меню и детская комната",
  None, 2800, "https://shikary.ru/", YM + ": отзывы — детская комната 94%, детское меню 84%; подборки «Рестораны и кафе Москвы с детской комнатой», «…с детской зоной в районе Чертаново»"),
 ("cafe-legenda-tushino", "Легенда (Северное Тушино)", "семейное кафе с детской комнатой",
  "ул. Свободы, 71, корп. 3, 1 этаж", 55.8635, 37.4365,
  "Семейное кафе в Северном Тушине: пицца, роллы, салаты и десерты, есть детское меню и детская комната",
  "В отзывах о детской комнате мнения расходятся", None, "https://cafelegenda.ru/", YM + ": отзывы — детская комната 65%, детское меню 87%; подборка «Семейные кафе и рестораны в районе Северное Тушино»"),
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
