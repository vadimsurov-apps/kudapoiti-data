"""Робот cafes, 2026-11-13 (10–12 UTC): 30 районов (Новаторская…Октябрьская, Дзержинский, Солнечногорск…Павловский Посад). Поиск Яндекс Карт (кэш kcz*-1113g/1113h),
карточки kcn*-1113g/1113h, координаты kcg*-1113g/1113h. Детская подтверждена карточкой Яндекса этого заведения: аспект отзывов
«Детская комната» (≥ 60% положительных, не меньше 12 отзывов) / подборка «Заведения с детским уголком». Координаты — здание
по адресу (Яндекс Карты); объект/вход уточнит сверка. Часы — подставит робот yandex-entrances (в карточке только «открыто до»).
Средний чек — только из карточки («Средний счёт»); lo–hi → середина, если hi ≤ 2·lo.
Запуск: KP_PART=cafes python3 tools/add_cafes_1113g.py"""


import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PLACES = {p["id"]: p for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
COORD = json.load(open(os.path.join(ROOT, "tools", "cafes_1113g_coords.json")))
DAY = "2026-11-13"
A1 = "дом по адресу (Яндекс Карты, координаты здания)"
YA = "Яндекс Карты (карточка заведения 13.11: рубрика, адрес, отзывы"
# id, название, тип, адрес, плюс, минус, средний чек, сайт, источник, как найти
DATA = [
 ('cafe-osteria-zeleny-81', 'Osteria Mario (Зелёный просп., 81)', 'итальянский ресторан-пиццерия с детской комнатой', 'Москва, Зелёный просп., 81',
  'Итальянский ресторан сети Osteria Mario в Новогирееве: паста, пицца, десерты. Есть детская комната — в отзывах её хвалят, есть детское меню', None, 2500, 'https://osteriamario.ru',
  YA + ': ресторан, пиццерия; аспект «Детская комната» 94% (39 отз.), «С детьми» 84% (94 отз.), «Детское меню» 80% (10 отз.); входит в подборку «Рестораны с детским уголком в районе Новогиреево»; средний счёт 2000–3000 ₽; этаж 1; телефон +7 (968) 369-65-04)', 'Этаж: 1'),
 ('cafe-osteria-pyatnitskaya-25a', 'Osteria Mario (Пятницкая ул., 25А)', 'итальянский ресторан-пиццерия с детской комнатой', 'Москва, Пятницкая ул., 25А',
  'Итальянский ресторан сети Osteria Mario в Замоскворечье: паста, пицца, рыба и морепродукты. Есть детская комната — в отзывах её хвалят', 'Средний чек высокий — 4 000–4 500 ₽', 4250, 'https://osteriamario.ru',
  YA + ': ресторан, пиццерия; аспект «Детская комната» 91% (13 отз.), «С детьми» 77% (60 отз.); средний счёт 4000–4500 ₽; телефон +7 (964) 508-24-95)', None),
 ('cafe-festival-fryazino-60-let-sssr', 'Фестиваль (Фрязино)', 'ресторан-пиццерия с детской комнатой', 'Фрязино, ул. 60 лет СССР, 4, стр. 1',
  'Ресторан-пиццерия во Фрязине, родители с детьми отзываются хорошо. Есть детская комната', None, 1200, 'https://festivalcafe.ru',
  YA + ': ресторан, пиццерия; входит в подборку «Места с детской комнатой для семейного отдыха во Фрязино»; аспект «С детьми» 95% (24 отз.); средний счёт 900–1500 ₽; телефон +7 (905) 735-39-75)', None),
 ('cafe-melnitsa-pavlovsky-posad-gertsena', 'Мельница (Павловский Посад)', 'пиццерия с детской комнатой', 'Павловский Посад, ул. Герцена, 14/1',
  'Пиццерия сети «Мельница» в центре Павловского Посада: пицца и бургеры. Есть детская комната', 'Про детскую комнату отзывы разные', 1000, 'https://мельница-пицца.рф',
  YA + ': пиццерия; аспект «Детская комната» 71% (24 отз.), «С детьми» 73% (29 отз.); средний счёт 800–1200 ₽; телефон +7 (499) 505-50-51)', None),
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
