"""Робот cafes, 2026-11-14 (02 UTC): районы Площадь Ильича…Пятницкое шоссе. Поиск Яндекс Карт (кэш kcz*-1114b),
карточки kcn*-1114b, координаты kcg*-1114b. Детская подтверждена карточкой Яндекса этого заведения: аспект отзывов
«Детская комната» (≥ 60% положительных, не меньше 12 отзывов) / подборка «Заведения с детским уголком». Координаты — здание
по адресу (Яндекс Карты); объект/вход уточнит сверка. Часы — подставит робот yandex-entrances (в карточке только «открыто до»).
Средний чек — только из карточки («Средний счёт»); lo–hi → середина, если hi ≤ 2·lo.
Запуск: KP_PART=cafes python3 tools/add_cafes_1114b.py"""


import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PLACES = {p["id"]: p for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
COORD = json.load(open(os.path.join(ROOT, "tools", "cafes_1114b_coords.json")))
DAY = "2026-11-14"
A1 = "дом по адресу (Яндекс Карты, координаты здания)"
YA = "Яндекс Карты (карточка заведения 14.11: рубрика, адрес, отзывы"
# id, название, тип, адрес, плюс, минус, средний чек, сайт, источник, как найти
DATA = [
 ('cafe-dodo-vernadskogo-29', 'Додо Пицца (пр-т Вернадского, 29)', 'пиццерия с детской комнатой', 'просп. Вернадского, 29, БЦ «Лето»',
  'Пиццерия в бизнес-центре «Лето» на проспекте Вернадского: пицца, додстеры, закуски и десерты. Есть детская комната, родители её хвалят', None, 500,
  'https://dodopizza.ru',
  YA + ': пиццерия, кафе, 940 оценок; аспекты «Детская комната» 81% (45 отз.), «С детьми» 79% (61 отз.); в подборке «Кафе и пиццерии с детской комнатой в Ломоносовском районе Москвы»; средний счёт 500 ₽)', 'В бизнес-центре «Лето»'),
 ('cafe-vash-gogis-potapovskaya', 'Ваш Гогис (Коммунарка)', 'ресторан грузинской кухни с детским уголком', 'пос. Коммунарка, ул. Потаповская Роща, 24, корп. 2',
  'Ресторан грузинской кухни у метро Потапово: хинкали, хачапури, пхали, чашушули, медовик. Бывает живая музыка, есть детский уголок и детское меню', None, None,
  'https://vashgogis.ru',
  YA + ': ресторан, 605 оценок; в подборках «Заведения с детским уголком в Новой Москве», «Заведения с детским меню в Новой Москве», «Заведения с грузинской кухней в Новой Москве», «Семейные кафе в Москве», «Рестораны и кафе с живой музыкой в Новой Москве»; аспект «С детьми» 96% (28 отз.); меню в карточке)', None),
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
