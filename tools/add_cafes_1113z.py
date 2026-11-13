"""Робот cafes, 2026-11-13 (23 UTC): районы Воронцовская…Орехово. Поиск Яндекс Карт (кэш kcz*-1113z),
карточки kcn*-1113z, координаты kcg*-1113z. Детская подтверждена карточкой Яндекса этого заведения: аспект отзывов
«Детская комната» (≥ 60% положительных, не меньше 12 отзывов) / подборка «Заведения с детским уголком». Координаты — здание
по адресу (Яндекс Карты); объект/вход уточнит сверка. Часы — подставит робот yandex-entrances (в карточке только «открыто до»).
Средний чек — только из карточки («Средний счёт»); lo–hi → середина, если hi ≤ 2·lo.
Запуск: KP_PART=cafes python3 tools/add_cafes_1113z.py"""


import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PLACES = {p["id"]: p for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
COORD = json.load(open(os.path.join(ROOT, "tools", "cafes_1113z_coords.json")))
DAY = "2026-11-13"
A1 = "дом по адресу (Яндекс Карты, координаты здания)"
YA = "Яндекс Карты (карточка заведения 13.11: рубрика, адрес, отзывы"
# id, название, тип, адрес, плюс, минус, средний чек, сайт, источник, как найти
DATA = [
 ('cafe-dodo-nametkina-13b', 'Додо Пицца (ул. Намёткина, 13Б)', 'пиццерия с детской комнатой', 'ул. Намёткина, 13Б, этаж 2',
  'Пиццерия на втором этаже на Намёткина: пицца, додстеры, закуски и десерты. Есть детская комната, родители её хвалят', None, 500,
  'https://dodopizza.ru',
  YA + ': пиццерия, кафе, 1443 оценки; аспекты «Детская комната» 89% (70 отз.), «С детьми» 88% (92 отз.); средний счёт 500 ₽)', 'Пиццерия на 2 этаже'),
 ('cafe-yellowfin-zilart', 'Yellowfin by Bluefin (ЗИЛАРТ)', 'ресторан и суши-бар с детским уголком', 'бул. Братьев Весниных, 1, помещение 10Н',
  'Суши-бар в ЗИЛАРТе: роллы, суши и японская кухня. Есть детский уголок', None, None,
  None,
  YA + ': ресторан, суши-бар, бар, 247 оценок; в подборке «Заведения с детским уголком в Даниловском районе»; средний счёт 1000–2500 ₽)', None),
 ('cafe-esse-nikitinskaya-13', 'Эссе (Никитинская ул., 13)', 'кафе-кофейня с детской комнатой', 'Никитинская ул., 13',
  'Кафе-кофейня в Измайлове: завтраки, горячее, десерты и кофе. Есть детская комната и детское меню', None, 900,
  None,
  YA + ': кафе, кофейня, 1937 оценок; аспекты «Детская комната» 91% (210 отз.), «С детьми» 92% (265 отз.), «Детское меню» 85% (28 отз.); в подборках «Рестораны Москвы с аниматорами для детей», «Рестораны и кафе с детской комнатой в районе Измайлово»; средний счёт 800–1000 ₽)', None),
 ('cafe-dodo-turistskaya-23', 'Додо Пицца (Туристская ул., 23)', 'пиццерия с детской комнатой', 'Туристская ул., 23',
  'Пиццерия в Северном Тушине: пицца, закуски и десерты, на кухню можно посмотреть вживую. Есть детская комната', None, None,
  'https://dodopizza.ru',
  YA + ': пиццерия, 2174 оценки; аспекты «Детская комната» 84% (102 отз.), «С детьми» 87% (139 отз.); в отзыве: «Детская комната… Можно наблюдать как готовят»)', None),
]



def row(d):
    pid, name, typ, addr, plus, minus, check, site, src, how = d
    lat, lon = COORD[pid]
    r = P(pid, name, typ, metro(lat, lon), addr, lat, lon, 0, 12, 60, 150, "спокойно", "творчество", None,
          None, None, "да", plus, minus, adult=3, src=src, acc=A1,
          booking=None, loud=None, food="да", stroller=None)
    r["Взрослый билет, ₽"] = check
    r["Бесплатно до (лет / см)"] = None
    r["Сайт"] = site
    r["Категории"] = "food"
    r["Как найти"] = how
    r["Проверено (дата)"] = DAY
    r["Источник"] += "; качество 2026-11"
    return r


if __name__ == "__main__":
    ROWS = [row(d) for d in DATA if d[0] in COORD]
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    ids = [r["id"] for r in ROWS]
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
