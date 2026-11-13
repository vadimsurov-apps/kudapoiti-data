"""Робот cafes, 2026-11-13 (15–17 UTC): 30 районов (Электроугли…Автозаводская, Академическая…Баррикадная). Поиск Яндекс Карт (кэш kcz*-1113k/1113m),
карточки kcn*-1113k/1113m, координаты kcg*-1113k/1113m. Детская подтверждена карточкой Яндекса этого заведения: аспект отзывов
«Детская комната» (≥ 60% положительных, не меньше 12 отзывов) / подборка «Заведения с детским уголком». Координаты — здание
по адресу (Яндекс Карты); объект/вход уточнит сверка. Часы — подставит робот yandex-entrances (в карточке только «открыто до»).
Средний чек — только из карточки («Средний счёт»); lo–hi → середина, если hi ≤ 2·lo.
Запуск: KP_PART=cafes python3 tools/add_cafes_1113k.py"""


import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PLACES = {p["id"]: p for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
COORD = json.load(open(os.path.join(ROOT, "tools", "cafes_1113k_coords.json")))
DAY = "2026-11-13"
A1 = "дом по адресу (Яндекс Карты, координаты здания)"
YA = "Яндекс Карты (карточка заведения 13.11: рубрика, адрес, отзывы"
# id, название, тип, адрес, плюс, минус, средний чек, сайт, источник, как найти
DATA = [
 ('cafe-slivki-staraya-kupavna', 'Сливки (Старая Купавна)', 'кофейня с детской игровой комнатой', 'Старая Купавна, Большая Московская ул., 77',
  'Уютная кофейня в Старой Купавне: завтраки, драники с сёмгой, вафли, пицца и паста. Есть игровая комната для детей, летом открыта терраса', None, None,
  'https://slivki-bolshaja-moskovskaja-ulitsa.clients.site',
  YA + ': кофейня; в описании «есть летняя терраса и игровая комната для детей»; аспект «Детская комната» 83% (14 отз.), «С детьми» 85% (36 отз.); телефон +7 (925) 375-44-14)', None),
 ('cafe-dinozavriya-zelenograd', 'Динозаврия (Зеленоград)', 'семейное кафе с детской комнатой', 'Зеленоград, Солнечная аллея, к936',
  'Семейное кафе-ресторан в Зеленограде с детской комнатой и детским меню. Родители в отзывах хвалят детскую и десерты', 'Про скорость обслуживания отзывы разные', None,
  'https://dinozavria-zel.ru',
  YA + ': кафе, ресторан; аспект «Детская комната» 82% (48 отз.), «С детьми» 81% (85 отз.), «Детское меню» 71% (17 отз.), «Десерты» 92%, «Время ожидания» 18% отрицательных; входит в подборки «Рестораны и кафе с игровыми зонами в Зеленограде», «Семейные заведения Зеленограда с игрушками и игровыми комнатами»; адрес — подъезд 4; телефон +7 (993) 258-42-26)', 'Вход: подъезд 4'),
 ('cafe-dodo-shcherbinka-zheleznodorozhnaya', 'Додо Пицца (Щербинка, Железнодорожная ул., 51)', 'пиццерия с детской комнатой', 'Щербинка, Железнодорожная ул., 51',
  'Пиццерия сети «Додо Пицца» в Щербинке: пицца, закуски, десерты. Есть детская комната — в отзывах её хвалят', None, 500,
  'https://dodopizza.ru',
  YA + ': пиццерия, кафе; аспект «Детская комната» 85% (45 отз.), «С детьми» 79% (62 отз.); входит в подборку «Заведения с детской комнатой в Щербинке: где поесть с детьми»; средний счёт 500 ₽; этаж 1; телефон 8 (800) 302-00-60)', 'Этаж: 1'),
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
