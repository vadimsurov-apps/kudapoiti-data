"""Робот cafes, 2026-11-09 (13 UTC): 13 кафе и ресторанов с детской комнатой.
Детская комната подтверждена: справочник spravker.ru (рубрика «Рестораны с детской комнатой», кэш auto/pages),
каталог restoran.cafe (подборка «с детской комнатой», кэш auto/pages), сайт сети MiMi (restoran-mimi.ru — у филиала
отмечено «Детская комната»). Координаты приблизительные — точку уточнит сверка с OSM по адресу (osm-local.yml).
Запуск: KP_PART=cafes python3 tools/add_cafes_1109d.py"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PLACES = {p["id"]: p for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
DAY = "2026-11-09"


def SP(city):
    return f"https://{city}.spravker.ru/restorany-s-detskoi-komnatoi/"


RC = "https://restoran.cafe/moskva/collections/special/detskaia-komnata"
MIMI = "https://restoran-mimi.ru/"
A1 = "приблизительно, ±1 км (по адресу, уточнить)"
A3 = "приблизительно, ±3 км (по адресу, уточнить)"
# id, название, адрес, lat, lon, источник, плюс, часы, точность, сайт
DATA = [
 ("cafe-nebo-rooftop-korolev", "Небо Руфтоп (Королёв)", "Королёв, ул. Ленина, 25",
  55.9175, 37.8265, SP("korolev"), "Ресторан на крыше с видом на Королёв, банкеты и семейные праздники · детская комната",
  "пн–чт 12:00–00:00; пт, сб 12:00–06:00; вс 12:00–00:00", A1, None),
 ("cafe-olimp-uvarovo", "Олимп (Коломна, Малое Уварово)", "Коломенский г. о., д. Малое Уварово",
  55.0600, 38.8000, SP("kolomna"), "Загородный ресторан с бранчами под Коломной · детская комната", "ежедневно, круглосуточно",
  "приблизительно, ±5 км (по адресу, уточнить)", None),
 ("cafe-vesna-rogozinino", "Vesna (Рогозинино)", "Новая Москва, д. Рогозинино, Луговая ул., вл. 20А, стр. 3",
  55.5395, 37.1870, SP("aprelevka"), "Семейный ресторан с бранчами в Новой Москве · детская комната", "ежедневно 10:00–23:00", A1, None),
 ("cafe-labirint-zhukovka", "Лабиринт (Жуковка)", "Одинцовский г. о., д. Жуковка, 57",
  55.7335, 37.2480, SP("odintsovo"), "Ресторан на Рублёвке · детская комната", None, A1, None),
 ("cafe-sosedi-odintsovo", "Соседи (Одинцово, Триумфальная)", "Одинцово, Триумфальная ул., 8",
  55.6745, 37.2560, SP("odintsovo"), "Семейное кафе-гастробар сети «Соседи» в жилом квартале · детская комната", None, A1, None),
 ("cafe-udachi-pominovo", "Удачи (Поминово, Развилка)", "Ленинский г. о., д. Поминово, территория Развилка 68-й км, 3/1",
  55.5880, 37.7470, SP("egorevsk"), "Ресторан с бранчами у МКАД на юге · детская комната", "ежедневно 12:00–00:00", A3, None),
 ("cafe-le-cafe-skokovo", "Le Café (Скоково)", "Одинцовский г. о., д. Скоково, Парковая ул.",
  55.7050, 36.9500, SP("zvenigorod"), "Загородное кафе с бургерами под Звенигородом · детская комната", "ежедневно 09:00–21:00", A3, None),
 ("cafe-veranda-mytishchi", "Веранда (Мытищи, Олимпийский пр-т)", "Мытищи, Олимпийский пр-т, стр. 13А",
  55.9150, 37.7560, SP("solnechnogorsk"), "Гастробар-веранда в Мытищах · детская комната", None, A1, None),
 ("cafe-danilovsky", "Даниловский (Староданиловский пер.)", "Большой Староданиловский пер., 5",
  55.7085, 37.6250, SP("aprelevka"), "Ресторан с банкетными залами для семейных праздников · детская комната",
  "ежедневно 12:00–22:00", A1, None),
 ("cafe-mimi-annino", "MiMi (Варшавское ш., Аннино)", "Варшавское ш., 160",
  55.5850, 37.5970, MIMI, "Семейный ресторан сети MiMi: живая музыка, летняя веранда · детская комната (по сайту сети)",
  "ежедневно 12:00–00:00", A1, "https://restoran-mimi.ru/"),
 ("cafe-mimi-novaya-riga", "MiMi (Гастровилла Novaya Riga)", "Истринский г. о., д. Покровское, ул. Центральная, 33, корп. 12, Гастровилла Novaya Riga",
  55.7925, 37.1045, MIMI, "Ресторан сети MiMi в гастровилле у аутлета «Новая Рига»: живая музыка · детская комната (по сайту сети)",
  "ежедневно 10:00–22:00", A1, "https://restoran-mimi.ru/"),
 ("cafe-ivanovskoe-konny", "Ивановское (конно-спортивный комплекс)", "Богородский г. о., с. Ивановское, Луговая ул., 23",
  56.0300, 38.3000, RC, "Ресторан на территории конно-спортивного комплекса: русская и европейская кухня, веранда и камин · детская комната",
  None, "приблизительно, ±5 км (по адресу, уточнить)", None),
 ("cafe-sahara-mkad", "Сахара (МКАД, 73-й км)", "МКАД, 73-й км, 7, корп. 1",
  55.8800, 37.4400, "https://restoran.cafe/moskva/popular-nedorogie-restorany-s-detskoi-komnatoi",
  "Недорогой ресторан у МКАД с банкетным залом · детская комната", None, A3, None),
]


def row(d):
    pid, name, addr, lat, lon, src, plus, hours, acc, site = d
    if "mimi" in src:
        where = "сайту сети MiMi (у филиала отмечена детская комната)"
    elif "spravker" in src:
        where = "справочнику spravker.ru (рубрика «Рестораны с детской комнатой»)"
    else:
        where = "каталогу restoran.cafe (подборка ресторанов с детской комнатой)"
    minus = f"Детская комната — по {where}; что в ней есть, часы работы и аниматоров уточняйте по телефону"
    r = P(pid, name, "кафе", metro(lat, lon), addr, lat, lon, 0, 12, 60, 150, "спокойно", "творчество", None,
          "средний чек — уточняйте", hours, "да", plus, minus, adult=3, src=src, acc=acc,
          booking="желательна", loud="частично", food="да", stroller="да")
    r["Сайт"] = site
    r["Категории"] = "food"
    r["Проверено (дата)"] = DAY
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
    wb.save(SRC)
    print("rows", len(ROWS), "total", ws.max_row - 1)
