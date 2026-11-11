"""Робот cafes, 2026-11-11 (23 UTC): 26 районов (Талдом…Щербинка, Нахимовский пр.…Октябрьская). Поиск Яндекс Карт
(кэш *-kcz/kcr/kca*-1112a), карточки *-kcn*-1112a, координаты здания по адресу *-kcg*-1112a.
Детская подтверждена карточкой Яндекса этого заведения: аспект отзывов «Детская комната» / «Детская анимация»
и/или подборка «с детской комнатой / детским уголком / детской зоной», в которую входит эта карточка.
Координаты — здание по адресу (Яндекс Карты); объект/вход уточнит сверка с OSM, до этого место скрыто.
Средний чек: «от N» → N; lo–hi → середина, если hi ≤ 2·lo.
Запуск: KP_PART=cafes python3 tools/add_cafes_1112a.py"""

import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PLACES = {p["id"]: p for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
COORD = json.load(open(os.environ.get("KCOORD", "tools/cafes_1112a_coords.json")))
DAY = "2026-11-11"
A1 = "дом по адресу (Яндекс Карты, координаты здания)"
YA = "Яндекс Карты (карточка заведения 11.11: рубрика, адрес, средний счёт, отзывы"
# id, название, тип, адрес, плюс, минус, средний чек, сайт, источник, как найти
DATA = [
 ("cafe-rusalka-novinki", "Rusalka (Новинки)", "ресторан с детской комнатой",
  "г. о. Истра, д. Новинки, 115, стр. 5",
  "Ресторан в Новинках по соседству с «Пикником» и «Чайханой»: рыба и морепродукты, устрицы, пицца, есть доставка. Есть детская комната",
  None, 3750, "https://rusalkabistro.ru", YA + "; средний счёт 2500–5000, аспекты «Детская комната» 89%, «С детьми» 87%, «Морепродукты», «Рыба», «Устрицы»; телефон +7 (495) 995-44-44)", None),
 ("cafe-solnechny-moskovsky", "Солнечный (г. Московский)", "ресторан с детской комнатой",
  "г. Московский, Солнечная ул., 3А, стр. 1",
  "Ресторан на Солнечной улице: живая музыка, десерты и молочные коктейли, здесь отмечают дни рождения и устраивают банкеты. Есть детская комната",
  None, 2250, None, YA + "; средний счёт 1500–3000, аспекты «Детская комната» 76%, «С детьми» 85%, «Живая музыка» 89%, «День рождения»; подборки «Места для семейного отдыха с едой в городе Московский», «Места для банкетов в Московском»; телефон +7 (916) 739-00-40)", None),
 ("cafe-polianto-troitsk", "Полианто (Троицк)", "ресторан-пиццерия с детской комнатой",
  "Троицк, Троицкий бул., 2",
  "Ресторан-пиццерия итальянской кухни в микрорайоне Солнечный: пицца, салаты, завтраки, есть доставка. Есть детская комната, бывают детские аниматоры",
  None, 1250, "https://polianto.ru", YA + "; средний счёт 1000–1500, аспекты «Детская комната» 85% (143 отзыва), «Детская анимация» 100%, «Детское меню»; подборки «Места с детской зоной в Троицке», «Места для посещения с детьми: кафе, рестораны и пиццерии в Троицке»; телефон +7 (985) 584-84-78)", None),
 ("cafe-soul-okskaya", "Соул (Окская)", "кофейня с детским уголком",
  "ул. Михайлова, 30А, корп. 6",
  "Кофейня у метро Окская: кофе, авторские сэндвичи, десерты, азиатское меню. Есть детский уголок",
  None, None, None, YA + "; аспект «Детская комната» 100%; подборки «Заведения с детским уголком в районе Рязанский», «Заведения с детской зоной в районе Рязанский»; вход слева, подъезд №1; телефон +7 (993) 355-90-91)", "Вход: подъезд № 1"),
 ("cafe-la-provincia-oktyabrskaya", "La Provincia (Октябрьская)", "ресторан с детскими аниматорами",
  "Калужская пл., 1, стр. 4",
  "Ресторан у метро Октябрьская: паста, ризотто, пицца, стейки, торты и раздел свежих морепродуктов. Бывают детские аниматоры",
  None, 3000, "https://laprovincia.moscow", YA + "; средний счёт 2500–3500, аспект «Детская анимация» 100%; телефон +7 (906) 046-51-37)", None),
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
