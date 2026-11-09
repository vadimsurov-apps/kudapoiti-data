"""Робот fun, 2026-11-09 (день, 4-й проход). Яндекс-страницы больше не скачиваются (все домены yandex.* попали в
auto/spam-domains.txt), поэтому источник — справочник orgpage.ru по городам Подмосковья + проверка по сайтам мест
(auto/pages: www-sovenok-club-ru, kapiclub-ru, www-center-zolushka-ru). Координаты приблизительные — точку по адресу
поправит сверка с OSM. Иконки — tools/icons_fun_1109e.py.
Запуск: KP_PART=fun python3 tools/add_fun_1109e.py"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC
from add_batch14 import metro

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DAY = "2026-11-09"
ROWS = []


def add(pid, name, typ, cats, tags, addr, lat, lon, a0, a1, d0, d1, energy, plus, minus, q,
        price=None, note="цены — уточняйте", hours="уточняйте", acc=None, indoor="да", adult=1,
        booking="желательна", sit="нет", dark="нет", loud="нет", food="нет", stroller="частично",
        crowd="частично", moscow=True):
    m = metro(lat, lon) if moscow else "— (на машине / электричке)"
    r = P(pid, name, typ, m, addr, lat, lon, a0, a1, d0, d1, energy, tags, price, note, hours, indoor, plus, minus,
          adult=adult, src=q, acc=acc or "приблизительно, ±500 м",
          booking=booking, sit=sit, dark=dark, loud=loud, food=food, stroller=stroller, crowd=crowd)
    r["Сайт"] = ""
    r["Категории"] = cats
    r["Проверено (дата)"] = DAY
    ROWS.append(r)


KM = "приблизительно, ±1 км"
PLAY = dict(energy="активно", loud="да", stroller="да")
STUDIO = dict(energy="спокойно", booking="обязательна", sit="частично", stroller="нет")
QUEST = dict(energy="средне", booking="обязательна", dark="частично", stroller="нет", crowd="нет")


def play(pid, name, addr, lat, lon, plus, minus, q, a0=1, a1=8, **kw):
    add(pid, name, "игровая комната", "playcenters", "спорт и активность", addr, lat, lon, a0, a1, 60, 180,
        plus=plus, minus=minus, q=q, **{"note": "оплата по времени — уточняйте тарифы", **PLAY, **kw})


def studio(pid, name, addr, lat, lon, plus, minus, q, a0=4, a1=14, typ="творческая студия", cats="masterclass",
           tags="творчество", **kw):
    add(pid, name, typ, cats, tags, addr, lat, lon, a0, a1, 60, 120, plus=plus, minus=minus, q=q,
        **{"note": "разовые мастер-классы и абонементы — уточняйте", "hours": "по расписанию занятий", **STUDIO, **kw})


def quest(pid, name, addr, lat, lon, plus, minus, q, a0=7, a1=14, **kw):
    add(pid, name, "квест", "quests", "загадки и приключения", addr, lat, lon, a0, a1, 60, 120, plus=plus,
        minus=minus, q=q, **{"note": "цена за команду — уточняйте", "hours": "по записи", "adult": 2, **QUEST, **kw})





M300 = "приблизительно, ±300 м (тот же ТЦ)"
M = lambda a: f"детская игровая комната метро {a}"
QQ = lambda a: f"квест для детей метро {a}"
T = lambda a: f"творческая студия для детей метро {a}"
MK = lambda a: f"мастер-класс для детей метро {a}"
OBL = dict(moscow=False, acc=KM)


OBL = dict(moscow=False, acc=KM)

studio("sovenok-club-zhukovsky", "Детский клуб «Совёнок» (Жуковский)", "Жуковский, ул. Гудкова, 18", 55.6005, 38.1130,
       "Клуб с 15-летней историей: изостудия, хореография, подготовка к школе, малые группы до 10 детей",
       "Занятия по абонементу, нужна запись", "сайт sovenok-club.ru (09.11.2026); справочник orgpage.ru",
       a0=3, a1=11, typ="детский центр", **OBL)
studio("kapitosha-ramenskoe", "Клуб гармоничного развития «Капитоша» (Раменское)", "Раменское, ул. Гурьева, 11А", 55.5728, 38.2398,
       "Арт-мастерская, логорисование, группы «Самостоятельный малыш» и подготовка к школе",
       "Нужна запись", "сайт kapiclub.ru (09.11.2026); справочник orgpage.ru",
       a0=2, a1=10, typ="детский центр", **OBL)
studio("zolushka-center-odintsovo", "Центр развития «Золушка» (Одинцово)", "Одинцово, Можайское ш., 119, 2 этаж", 55.6830, 37.2885,
       "Центр работает 29 лет: раннее развитие, подготовка к школе, «Школа изобретателей» 6–12 лет; за успехи — «золотарики»",
       "Пробное занятие по записи", "сайт center-zolushka.ru (09.11.2026); справочник orgpage.ru",
       a0=1, a1=14, typ="детский центр", cats="masterclass,science", tags="наука и открытия", **OBL)
SITES = {"sovenok-club-zhukovsky": "https://www.sovenok-club.ru/", "kapitosha-ramenskoe": "https://kapiclub.ru/",
         "zolushka-center-odintsovo": "https://www.center-zolushka.ru/"}
for _r in ROWS:
    _r["Сайт"] = SITES.get(_r["id"], "")

if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    allids = {x["id"] for x in json.load(open(os.path.join(ROOT, "places.json")))["places"]}
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    ids = [r["id"] for r in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    assert not [i for i in ids if i in existing or i in allids], [i for i in ids if i in existing or i in allids]
    for row_ in ROWS:
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        r = ws.max_row + 1
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=r, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    print("rows", len(ROWS), "total", ws.max_row - 1)
