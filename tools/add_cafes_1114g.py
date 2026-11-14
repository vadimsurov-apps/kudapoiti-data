"""Робот cafes, 2026-11-14 (10–12 UTC): районы Тютчевская…Филатов Луг (15 районов: «кафе с детской комнатой», «ресторан с детской
игровой», «семейное кафе с аниматором»). Поиск Яндекс Карт (кэш kcz*-1114g/f), карточки kcn*, координаты kcg*.
Детская подтверждена карточкой Яндекса этого заведения: аспект отзывов «Детская комната» (≥ 79%, не меньше 41 отзыва) и/или подборки
«с детской комнатой». Координаты — здание по адресу (Яндекс Карты). Часы подставит робот yandex-entrances.
Средний чек — только из карточки («Средний счёт»); lo–hi → середина, если hi ≤ 2·lo.
Запуск: KP_PART=cafes python3 tools/add_cafes_1114g.py"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PLACES = {p["id"]: p for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
COORD = json.load(open(os.path.join(ROOT, "tools", "cafes_1114g_coords.json")))
DAY = "2026-11-14"
A1 = "дом по адресу (Яндекс Карты, координаты здания)"
YA = "Яндекс Карты (карточка заведения 14.11: рубрика, адрес, отзывы"
DATA = [
 ('cafe-qalaquri-family-beregovoy-5', 'Qalaquri Family (Береговой пр., 5с1)', 'грузинский ресторан с детским уголком', 'Береговой пр., 5, стр. 1',
  'Грузинский ресторан с открытой кухней в Филях: хачапури, хинкали, шашлыки на мангале, грузинские вина. Есть детский уголок',
  'Это ещё и кальян-бар', None, 'https://fili.qalaqurifamily.ru',
  YA + ': ресторан, кальян-бар, кафе; подборки «Заведения общественного питания с детским уголком в районе Филёвский Парк», «Рестораны для семейного отдыха в районе Филёвский Парк»; телефон +7 (925) 140-08-88); https://qalaqurifamily.ru (адрес Береговой проезд 5 с1, часы ежедневно 12:00–00:00, меню)', None, 'ежедневно 12:00–00:00'),
 ('cafe-up-sushi-maloe-ponizovye-4', 'Up Sushi (Коммунарка, ул. Малое Понизовье, 4)', 'суши-бар и пиццерия с детской игровой', 'Коммунарка, ул. Малое Понизовье, 4',
  'Суши-бар и пиццерия в Коммунарке: роллы, суши, рамен, пицца. Есть небольшая детская игровая. Место отмечено наградой Яндекс Карт «Хорошее место 2026»',
  None, None, 'https://upsushi.ru',
  YA + ': суши-бар, пиццерия, 815 оценок, «Хорошее место 2026»; аспекты «Детская комната» 89% (27 отз.), «С детьми» 83% (43 отз.); в отзывах — «детский уголок», «небольшая детская игровая», рамен)', None, None),
]


def row(d):
    pid, name, typ, addr, plus, minus, check, site, src, how, hours = d
    lat, lon = COORD[pid]
    r = P(pid, name, typ, metro(lat, lon), addr, lat, lon, 0, 12, 60, 150, "спокойно", "творчество", None,
          None, hours, "да", plus, minus, adult=3, src=src, acc=A1,
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
