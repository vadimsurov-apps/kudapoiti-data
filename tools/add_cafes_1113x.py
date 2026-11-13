"""Робот cafes, 2026-11-13 (19–20 UTC): 15 районов (Бульвар Рокоссовского…Воробьёвы горы). Поиск Яндекс Карт (кэш kcz*-1113x),
карточки kcn*-1113x, координаты kcg*-1113x. Детская подтверждена карточкой Яндекса этого заведения: аспект отзывов
«Детская комната» (≥ 60% положительных, не меньше 12 отзывов) / подборка «Заведения с детским уголком». Координаты — здание
по адресу (Яндекс Карты); объект/вход уточнит сверка. Часы — подставит робот yandex-entrances (в карточке только «открыто до»).
Средний чек — только из карточки («Средний счёт»); lo–hi → середина, если hi ≤ 2·lo.
Запуск: KP_PART=cafes python3 tools/add_cafes_1113x.py"""


import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PLACES = {p["id"]: p for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
COORD = json.load(open(os.path.join(ROOT, "tools", "cafes_1113x_coords.json")))
DAY = "2026-11-13"
A1 = "дом по адресу (Яндекс Карты, координаты здания)"
YA = "Яндекс Карты (карточка заведения 13.11: рубрика, адрес, отзывы"
# id, название, тип, адрес, плюс, минус, средний чек, сайт, источник, как найти
DATA = [
 ('cafe-tanuki-petrozavodskaya-11a', 'Тануки (Петрозаводская ул., 11А)', 'ресторан японской кухни с детской комнатой', 'Петрозаводская ул., 11А',
  'Японский ресторан в Ховрине: роллы, суши, горячее. Есть детская комната, детское меню и детская анимация — родители в отзывах их хвалят', None, None,
  'https://tanukifamily.ru',
  YA + ': ресторан, суши-бар, 5858 оценок; аспекты «С детьми» 89% (257 отз.), «Детская комната» 91% (144 отз.), «Детское меню» 87% (26 отз.), «Детская анимация» 100% (24 отз.); в отзыве: «Есть детская комната»)', None),
 ('cafe-tanuki-volgogradsky-17', 'Тануки (Волгоградский пр-т, 17)', 'ресторан японской кухни с детской игровой зоной', 'Волгоградский просп., 17',
  'Японский ресторан на Волгоградском проспекте: роллы, суши, горячее. Есть игровая зона для детей и детское меню', 'Игровая зона небольшая', None,
  'https://tanukifamily.ru',
  YA + ': ресторан, суши-бар, 6020 оценок; аспекты «С детьми» 95% (203 отз.), «Детская комната» 96% (89 отз.), «Детское меню» 92% (37 отз.); в отзыве: «имеется небольшая игровая зона для детей»)', None),
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
