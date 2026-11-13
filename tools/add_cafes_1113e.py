"""Робот cafes, 2026-11-13 (07–09 UTC): 30 районов (Лесопарковая…Нижегородская). Поиск Яндекс Карт (кэш kcz*-1113e/1113f),
карточки kcn*-1113e/1113f, координаты kcg*-1113e. Детская подтверждена карточкой Яндекса этого заведения: аспект отзывов
«Детская комната» (≥ 60% положительных, не меньше 12 отзывов) / подборка «Заведения с детским уголком». Координаты — здание
по адресу (Яндекс Карты); объект/вход уточнит сверка. Часы — подставит робот yandex-entrances (в карточке только «открыто до»).
Средний чек — только из карточки («Средний счёт»); lo–hi → середина, если hi ≤ 2·lo.
Запуск: KP_PART=cafes python3 tools/add_cafes_1113e.py"""


import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PLACES = {p["id"]: p for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
COORD = json.load(open(os.path.join(ROOT, "tools", "cafes_1113e_coords.json")))
DAY = "2026-11-13"
A1 = "дом по адресу (Яндекс Карты, координаты здания)"
YA = "Яндекс Карты (карточка заведения 13.11: рубрика, адрес, отзывы"
# id, название, тип, адрес, плюс, минус, средний чек, сайт, источник, как найти
DATA = [
 ('cafe-gud-stori-lyublinskaya', 'Гуд Стори (Люблинская ул., 64)', 'ресторан-паб с детским уголком', 'Люблинская ул., 64',
  'Ресторан-паб в Люблине: стейки и большая кухня. Есть детский уголок — в отзывах его хвалят', None, 2000, 'https://goodstorypub.ru',
  YA + ': ресторан, бар; аспект «Детская комната» 90% (18 отз.); входит в подборку «Заведения с детским уголком в районе Люблино»; средний счёт 1500–2500 ₽; телефон +7 (968) 910-30-00)', None),
 ('cafe-chayka-lyubertsy-vesennyaya', 'Чайка (Люберцы, Весенняя ул.)', 'кафе-ресторан с детской комнатой', 'Люберцы, Весенняя ул., 12',
  'Кафе-ресторан в Люберцах: завтраки, выпечка, десерты. Есть детская комната', 'Про детскую комнату отзывы разные', None, None,
  YA + ': кафе, ресторан; аспект «Детская комната» 60% (17 отз.), «С детьми» 68% (28 отз.), «Завтраки» 88%, «Выпечка» 100%; телефон +7 (926) 250-21-11)', None),
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
