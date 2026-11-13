"""Робот cafes, 2026-11-13 (17–18 UTC): 15 районов (Бауманская…Бульвар Дмитрия Донского). Поиск Яндекс Карт (кэш kcz*-1113q),
карточки kcn*-1113q, координаты kcg*-1113q. Детская подтверждена карточкой Яндекса этого заведения: аспект отзывов
«Детская комната» (≥ 60% положительных, не меньше 12 отзывов) / подборка «Заведения с детским уголком». Координаты — здание
по адресу (Яндекс Карты); объект/вход уточнит сверка. Часы — подставит робот yandex-entrances (в карточке только «открыто до»).
Средний чек — только из карточки («Средний счёт»); lo–hi → середина, если hi ≤ 2·lo.
Запуск: KP_PART=cafes python3 tools/add_cafes_1113q.py"""


import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PLACES = {p["id"]: p for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
COORD = json.load(open(os.path.join(ROOT, "tools", "cafes_1113q_coords.json")))
DAY = "2026-11-13"
A1 = "дом по адресу (Яндекс Карты, координаты здания)"
YA = "Яндекс Карты (карточка заведения 13.11: рубрика, адрес, отзывы"
# id, название, тип, адрес, плюс, минус, средний чек, сайт, источник, как найти
DATA = [
 ('cafe-allo-pizza-borovskoe-50', 'Алло! Пицца (Боровское ш., 50)', 'пиццерия с детской комнатой', 'Боровское ш., 50',
  'Пиццерия «Алло! Пицца» в Ново-Переделкине: пицца, закуски, морсы. Есть детская комната', 'Детскую комнату в отзывах хвалят не все', 600,
  'https://allopizza.su',
  YA + ': пиццерия, быстрое питание; аспект «Детская комната» (27 отз., 33% отрицательных), «С детьми» 76% (90 отз.); входит в подборки «Заведения с детской комнатой в районе Ново-Переделкино, Москва», «Заведения для семейного отдыха с детьми в районе Ново-Переделкино»; средний счёт 500–700 ₽; телефон +7 (495) 374-60-97)', None),
 ('cafe-ersh-pererva-58', 'Ёрш (ул. Перерва, 58)', 'рыбный ресторан с детской зоной', 'ул. Перерва, 58',
  'Рыбный ресторан семьи «Тануки» в Марьине: уха, рыба, шашлык. Есть детская зона и детское меню, его хвалят в отзывах', 'По вечерам живая музыка и спортивные трансляции — бывает шумно', 2000,
  'https://tanukifamily.ru',
  YA + ': ресторан; входит в подборки «Заведения с детской зоной: где поесть с детьми в районе Марьино (Москва)», «Рестораны и бары с живой музыкой в районе Марьино», «Рестораны и бары Москвы со спортивными трансляциями»; аспекты «С детьми» 79% (102 отз.), «Детское меню» 88% (39 отз.); средний счёт 1500–2500 ₽; телефон +7 (499) 649-22-23)', None),
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
