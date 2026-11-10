"""Робот cafes, 2026-11-10 (05:00 UTC): районы Бутово…Третьяковская. Выдача Яндекс Карт недоступна (yandex.* в
auto/spam-domains.txt), restoclub.ru отвечает 503 — источник подборки eatout.ru «Кафе и рестораны с детской комнатой» по
станциям метро (кэш auto/pages, карточки заведений eatout: адрес, детская комната) + сайт самого заведения (работает,
адрес совпадает). Места, у которых сайт не открылся или детская есть только в старой карточке, не добавлены.
Также cafe-jesstaurant (Лапино, 65) → «Летто»: по этому адресу сейчас семейный ресторан Летто (letto.rest).
Запуск: KP_PART=cafes python3 tools/add_cafes_1110c.py"""

import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PLACES = {p["id"]: p for p in json.load(open(os.path.join(ROOT, "places.json")))["places"]}
DAY = "2026-11-10"
EO = "eatout.ru (подборка «Кафе и рестораны с детской комнатой» по станции метро)"
A1 = "приблизительно, ±1 км (по адресу, уточнить)"
# id, название, тип, адрес, lat, lon, плюс, минус, средний чек, сайт, источник
DATA = [
 ("cafe-govyadina-columbus", "ГОВЯDИНА (ТРЦ «Columbus»)", "мясной ресторан с игровой зоной",
  "Кировоградская ул., 13А, ТРЦ «Columbus»", 55.6115, 37.6069,
  "Семейный ресторан у «Пражской»: стейки, около десятка бургеров, блины, блюда из своей коптильни, милкшейки. Для детей есть игровая зона",
  None, 1000, "https://www.govyadinarestaurant.ru/", EO + " (карточка ресторана ГОВЯDИНА: адрес, игровая зона, детская комната); сайт govyadinarestaurant.ru (адрес Кировоградская, 13а)"),
 ("cafe-testo-veshki", "Тесто (пос. Вешки)", "итальянский ресторан с игровой комнатой",
  "Мытищинский г.о., пос. Вешки, Заводская ул., стр. 10", 55.9293, 37.5937,
  "Ресторан итальянской и европейской кухни в посёлке Вешки, в двух километрах от МКАД, светлый интерьер в стиле прованс. Для малышей есть игровая комната, бывают кулинарные мастер-классы",
  "Без машины добираться неудобно", 1500, "https://www.testo-kafe.ru/", EO + " (карточка ресторана Тесто); сайт testo-kafe.ru: «Для самых маленьких гостей в ресторане есть игровая комната», адрес"),
]


def row(d):
    pid, name, typ, addr, lat, lon, plus, minus, check, site, src = d
    r = P(pid, name, typ, metro(lat, lon), addr, lat, lon, 0, 12, 60, 150, "спокойно", "творчество", None,
          None, None, "да", plus, minus, adult=3, src=src, acc=A1,
          booking="желательна", loud="частично", food="да", stroller="да")
    r["Взрослый билет, ₽"] = check
    r["Сайт"] = site
    r["Категории"] = "food"
    r["Проверено (дата)"] = DAY
    r["Источник"] += "; качество 2026-11"
    return r


ROWS = [row(d) for d in DATA]

if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    ids = [r["id"] for r in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    assert not [i for i in ids if i in existing or i in PLACES], [i for i in ids if i in existing or i in PLACES]
    for row_ in ROWS:
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        r = ws.max_row + 1
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=r, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    # Jesstaurant (Лапино, 65) → «Летто»: сайт letto.rest — семейный ресторан по этому адресу, большая детская комната
    col = {n: i + 1 for i, n in enumerate(hdr)}
    for rr in range(2, ws.max_row + 1):
        if ws.cell(row=rr, column=1).value == "cafe-jesstaurant":
            upd = {"Название": "Летто (Лапино)", "Тип": "семейный ресторан с детской комнатой",
                   "Адрес": "Одинцовский г.о., д. Лапино, 65",
                   "Детский билет, ₽": None, "Бесплатно до (лет / см)": None, "Взрослый билет, ₽": 2000,
                   "Часы работы": "ежедневно 09:30–22:00",
                   "Плюс": "Семейный ресторан европейской и японской кухни с завтраками и тортами на заказ. Большая детская игровая, "
                           "по выходным — квесты, шоу и спектакли для детей, можно устроить детский праздник",
                   "Минус": "Игровая платная: 500 ₽ за ребёнка в будни, 1000 ₽ в выходные и праздники",
                   "Сайт": "https://www.letto.rest/",
                   "Источник": "сайт letto.rest (адрес, часы, игровая, афиша); eatout.ru (средний чек); качество 2026-11",
                   "Проверено (дата)": DAY}
            for k, v in upd.items():
                ws.cell(row=rr, column=col[k]).value = v
            print("обновлено cafe-jesstaurant → Летто")
    wb.save(SRC)
    print("rows", len(ROWS), "total", ws.max_row - 1)
