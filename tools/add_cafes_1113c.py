"""Робот cafes, 2026-11-13 (04–06 UTC): 30 районов (Выхино…Лермонтовский проспект). Поиск Яндекс Карт (кэш kcz*-1113c/1113d), карточки kcn*-1113c/1113d, координаты kcg*-1113c.
Старый текст шаблона:: 29 районов (Зябликово…Ивантеевка). Поиск Яндекс Карт
«кафе с детской комнатой / ресторан с детской игровой <район>» (кэш kcz*-1113a/1113b), карточки kcn*-1113a/1113b,
координаты kcg*-1113a/1113b.
Детская подтверждена карточкой Яндекса этого заведения: аспект отзывов «Детская комната» (≥ 60% положительных,
не меньше 12 отзывов) и отзывы посетителей о детской комнате/уголке. Координаты — здание по адресу (Яндекс Карты);
объект/вход уточнит сверка. Средний чек — только из карточки («Средний счёт»); lo–hi → середина, если hi ≤ 2·lo.
Запуск: KP_PART=cafes python3 tools/add_cafes_1113a.py"""

import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PLACES = {p["id"]: p for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
COORD = json.load(open(os.path.join(ROOT, "tools", "cafes_1113c_coords.json")))
DAY = "2026-11-13"
A1 = "дом по адресу (Яндекс Карты, координаты здания)"
YA = "Яндекс Карты (карточка заведения 13.11: рубрика, адрес, отзывы"
# id, название, тип, адрес, плюс, минус, средний чек, сайт, источник, как найти
DATA = [
 ('cafe-dodo-davydkovskaya-8', 'Додо Пицца (Давыдковская ул., 8к1)', 'пиццерия с детской комнатой', 'Давыдковская ул., 8, корп. 1',
  'Пиццерия «Додо» в Давыдкове. Есть небольшая игровая комната — дети играют, пока готовят заказ', 'Игрушек в детской комнате немного', 500, 'https://dodopizza.ru',
  YA + ': пиццерия, кафе; аспекты «С детьми» 85% (65 отз.), «Детская комната» 74% (48 отз.); в отзывах «есть небольшая игровая комната, где дети проводят время в ожидании заказа», «в детской комнате не хватает игрушек»; ср. чек 500 ₽)', None),
 ('cafe-osteria-mario-kotelniki', 'Osteria Mario (Котельники, 1-й Покровский пр.)', 'итальянский ресторан с детской комнатой', 'Котельники, 1-й Покровский пр., 5',
  'Итальянский ресторан сети Osteria Mario в Котельниках. Есть игровая комната для детей', None, 3000, 'https://osteriamario.ru',
  YA + ': ресторан, пиццерия; особенность «детская комната»; в отзывах «в ресторане есть игровая комната для детей», «детский уголок»; средний счёт 2000–4000 ₽; телефон +7 (964) 508-39-60; адрес — этаж 1)', 'Этаж: 1'),
 ('cafe-batono-jonny-lyubertsy-8marta', 'Батоно Джонни (Люберцы, ул. 8 Марта)', 'ресторан грузинской кухни с детской комнатой', 'Люберцы, ул. 8 Марта, 6',
  'Ресторан грузинской кухни в Люберцах: хинкали и хачапури. Есть детская комната и детское меню', None, None, 'https://batono-jonny.ru',
  YA + ': ресторан, кафе, бар; аспект «Детская комната» 70% (41 отз.); подборка «Рестораны и кафе в Люберцах с детским меню»; средний счёт 500–1500 ₽; телефон +7 (925) 333-38-28)', None),
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
