"""Робот cafes, 2026-11-12 (08 UTC): 30 районов (Аминьевская…Бутырская, Балашиха, Бутово). Поиск Яндекс Карт с фильтром
«Детская комната» (кэш *-kcz*-1112h), карточки *-kcn*-1112h, координаты здания по адресу *-kcg*-1112h.
Детская подтверждена карточкой Яндекса этого заведения: аспект отзывов «Детская комната» / «Детская анимация»
и/или подборка «с детской комнатой / детским уголком / детской зоной», в которую входит эта карточка.
Координаты — здание по адресу (Яндекс Карты); объект/вход уточнит сверка с OSM, до этого место скрыто.
Средний чек: «от N» → N; lo–hi → середина, если hi ≤ 2·lo.
Запуск: KP_PART=cafes python3 tools/add_cafes_1112h.py"""

import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PLACES = {p["id"]: p for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
COORD = json.load(open(os.environ.get("KCOORD", "tools/cafes_1112h_coords.json")))
DAY = "2026-11-12"
A1 = "дом по адресу (Яндекс Карты, координаты здания)"
YA = "Яндекс Карты (карточка заведения 12.11: рубрика, адрес, средний счёт, отзывы"
# id, название, тип, адрес, плюс, минус, средний чек, сайт, источник, как найти
DATA = [
 ("cafe-osteria-botanica-pika", "Osteria Mario (ТЦ «Ботаника»)", "семейный итальянский ресторан с детской комнатой",
  "ул. Вильгельма Пика, 11, ТЦ «Ботаника», 1 этаж",
  "Итальянский семейный ресторан в ТЦ «Ботаника» у Ботанического сада: пицца, паста, десерты. Есть детская комната, бывают аниматоры",
  None, None, "https://osteriamario.ru", "https://osteriamario.ru/children/ (список ресторанов с детской комнатой: «Остерия Марио в ТЦ «Ботаника»»); https://osteriamario.ru/adresa-restoranov-osteria-mario (ТЦ «Botanica», ул. Вильгельма Пика, 11, 1 этаж, +7 (926) 980-76-92); " + YA + "; аспекты «Детская комната» 90% (64 отзыва), «Детская анимация» 85%)", "Этаж: 1, ТЦ «Ботаника»"),
 ("cafe-zdraste-ochakovskoe-5", "Здрасте (Очаковское ш., 5к1)", "семейная кофейня с детской игровой",
  "Очаковское ш., 5, корп. 1",
  "Светлая семейная кофейня сети «Здрасте» в Матвеевском: завтраки, выпечка, есть детское меню. Есть детская игровая с игрушками",
  None, None, None, YA + "; аспекты «Детская комната» 95% (36 отзывов), «С детьми» 97%; отзывы: «хорошая игровая для детей с большим количеством игрушек», «есть детская комната»)", None),
 ("cafe-zdraste-mikhailova-30a", "Здрасте (ул. Михайлова, 30Ак4)", "семейная кофейня с детским уголком",
  "ул. Михайлова, 30А, корп. 4",
  "Семейная кофейня сети «Здрасте» у метро «Окская»: напитки, завтраки, пицца. Есть небольшой детский уголок с книжками и игрушками",
  None, None, None, YA + "; аспект «Детская комната» 80% (19 отзывов); отзыв: «маленький детский уголок, где есть книжки»)", None),
 ("cafe-zdraste-bolshaya-pochtovaya-32", "Здрасте (Большая Почтовая, 32к1)", "семейная кофейня с детской игровой зоной",
  "Большая Почтовая ул., 32, корп. 1",
  "Семейная кофейня сети «Здрасте» у Бауманской: завтраки весь день, пицца, детское меню, летом кресла на улице. Есть игровая зона для малышей",
  None, None, None, YA + "; аспекты «Детская комната» 94% (28 отзывов), «Детское меню» 80%; отзывы: «есть игровая зона для маленьких деток», «завтраки весь день»)", None),
 ("cafe-dodo-khoroshevsky-3a", "Додо Пицца (2-й Хорошёвский пр., 3А)", "пиццерия с детской комнатой",
  "2-й Хорошёвский пр., 3А",
  "Пиццерия «Додо» в Хорошёвском районе: пицца, закуски, десерты и кофе. Есть детская комната",
  None, 500, "https://dodopizza.ru", YA + "; средний счёт 500, аспекты «Детская комната» 100% (49 отзывов), «С детьми» 91%; подборки «Кафе и рестораны с детской комнатой в Хорошёвском районе Москвы», «Рестораны и пиццерии с детской зоной в Хорошёвском районе Москвы»; телефон сети 8 (800) 302-00-60)", None),
 ("cafe-dodo-balashikha-nekrasova-5", "Додо Пицца (Балашиха, ул. Некрасова)", "пиццерия с детской комнатой",
  "Балашиха, ул. Некрасова, 5",
  "Пиццерия «Додо» в микрорайоне Южный: пицца на тонком тесте, мороженое, кофе. Есть небольшая детская комната",
  None, 500, "https://dodopizza.ru", YA + "; средний чек 500, аспект «Детская комната» 71% (20 отзывов); отзывы: «рады, что на Южном… детская комната», «детская комната маленькая»)", None),
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
