"""Робот cafes, 2026-11-08 (10 UTC): 14 кафе и ресторанов с детской комнатой в Москве.
Детская комната — по каталогу restoran.cafe (у заведения отметка «Детская комната» или описание детской/игровой),
кэш auto/pages: подборки «С детской комнатой», «Детское меню», «Загородные», «С аниматором» (постранично /page/N).
Координаты приблизительные (уточнит сверка с OSM по адресу). Запуск: KP_PART=cafes python3 tools/add_cafes_1108d.py"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PLACES = {p["id"]: p for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
DAY = "2026-11-08"
RC = "https://restoran.cafe/moskva/"
A = "приблизительно, ±1 км (по адресу, уточнить)"
A5 = "приблизительно, ±500 м (по адресу, уточнить)"

# id, название, адрес, lat, lon, источник, плюс, что в детской (или None), средний чек, точность
DATA = [
 ("cafe-moremania-kashirskoe", "Моремания (Каширское ш.)", "Каширское ш., 80", 55.6280, 37.7000,
  RC + "popular-s-detskoi-komnatoi-i-zavtrakami/page/5",
  "Рыбный ресторан с торговой лавкой, морская и японская кухня, завтраки, детское меню · детская зона",
  "детская зона с горкой, телевизором, пуфами и игрушками", 1300, A),
 ("cafe-taksim-columbus", "Taksim (ТРЦ «Columbus»)", "Кировоградская ул., 13А, ТРЦ «Columbus»", 55.6115, 37.6069,
  RC + "popular-s-detskoi-komnatoi-i-zavtrakami/page/5",
  "Халяльный ресторан турецкой кухни со своей пекарней, завтраки, детское меню · детская комната", None, 1500, A5),
 ("cafe-annenfeld-uralskaya", "Анненфельд (Уральская ул.)", "Уральская ул., 17", 55.8112, 37.8045,
  RC + "collections/special/detskoe-meniu/page/29?v=1",
  "Кафе кавказской и европейской кухни, живая музыка · отдельная комната для детей", None, 1000, A),
 ("cafe-tgi-fridays-kashirskoe", "TGI Fridays (Каширское ш.)", "Каширское ш., 61Г", 55.6214, 37.7135,
  RC + "popular-restorany-s-letnei-verandoi-i-detskoi-komnatoi/page/6",
  "Американская кухня: бургеры, рёбрышки, летняя веранда · детская комната", None, 1500, A5),
 ("cafe-perchini-prime-plaza", "Перчини (ТЦ «Прайм Плаза»)", "ул. Каховка, 29А, ТЦ «Прайм Плаза»", 55.6563, 37.5700,
  RC + "popular-s-detskoi-komnatoi-i-zavtrakami/page/5",
  "Итальянская кухня сети «Перчини», отдельное детское меню · детская комната", None, 2000, A5),
 ("cafe-zharovnya-ostrov", "Жаровня (пр-т Андропова, 1)", "пр-т Андропова, 1", 55.6937, 37.6719,
  RC + "collections/special/detskaia-komnata/page/13?v=1",
  "Гриль-бар: блюда на гриле, пицца и паста, завтраки, мастер-классы для детей · детская комната", None, 2000, A),
 ("cafe-sytaya-utka-mira", "Сытая Утка (пр-т Мира, 188Б)", "пр-т Мира, 188Б, корп. 4", 55.8344, 37.6579,
  RC + "collections/special/detskaia-komnata/page/14?v=1",
  "Семейный ресторан с утиными блюдами и «утиной» концепцией, завтраки, летняя веранда · детская комната", None, 2000, A5),
 ("cafe-sytaya-utka-kurkino", "Сытая Утка (Куркино)", "Соколово-Мещерская ул., 16/114", 55.8950, 37.3930,
  RC + "collections/special/detskaia-komnata/page/14?v=1",
  "Просторный семейный ресторан с панорамными окнами, блюда из утки, детское меню · детская игровая",
  "детская комната с телевизором, мягкими игрушками и книжками", 1000, A),
 ("cafe-ferma-vdnh", "Ферма (ВДНХ)", "пр-т Мира, 119, стр. 244, ВДНХ", 55.8360, 37.6270,
  RC + "collections/special/detskaia-komnata/page/14?v=1",
  "Кафе в сканди-стиле на ВДНХ с видом на парк, детское меню, летняя веранда · детская комната",
  "детская комната с игрушками, кубиками и книжками", None, A),
 ("cafe-verba-kolomenskoe", "Верба (у парка «Коломенское»)", "пр-т Андропова, 37", 55.6730, 37.6647,
  RC + "collections/special/animator/page/7?v=1",
  "Семейный ресторан европейской кухни у парка «Коломенское», своя кондитерская, аниматор в пт–вс · детская игровая зона",
  None, 2000, A5),
 ("cafe-boris-godunov-kiselny", "Борис Годунов (Нижний Кисельный пер.)", "Нижний Кисельный пер., 4", 55.7652, 37.6290,
  RC + "collections/special/detskoe-meniu/page/23?v=1",
  "Ресторан русской и европейской кухни при одноимённом отеле, детское меню · детский уголок", None, 3000, A),
 ("cafe-russkoe-podvorye-zyuzino", "Русское подворье (Зюзино)", "Симферопольский б-р, 16, корп. 1", 55.6600, 37.6040,
  RC + "collections/special/detskoe-meniu/page/25?v=1",
  "Семейный ресторан русской и европейской кухни, аниматор · детская комната", None, 4000, A),
 ("cafe-ilpatio-mitinskaya", "IL Патио (Митинская ул.)", "Митинская ул., 16", 55.8457, 37.3623,
  RC + "collections/special/detskoe-meniu/page/27?v=1",
  "Итальянская кухня сети IL Патио: пицца, паста, завтраки · детская комната", None, 1200, A5),
 ("cafe-vino-i-eda-gzhatskaya", "Вино и Еда by Первый Нос (Гжатская ул.)", "Гжатская ул., 5, корп. 1", 55.7175, 37.4337,
  RC + "collections/special/detskoe-meniu/page/29?v=1",
  "Итальянская кухня, вегетарианские блюда, детское меню · детская комната", None, 2000, A),
]


def row(d):
    pid, name, addr, lat, lon, src, plus, room, check, acc = d
    what = f"по каталогу restoran.cafe: {room}" if room else "по каталогу restoran.cafe (отметка «Детская комната»)"
    minus = f"Детская — {what}; часы работы детской и аниматоров уточняйте по телефону"
    note = f"средний чек ~{check} ₽" if check else "средний чек — уточняйте"
    r = P(pid, name, "кафе", metro(lat, lon), addr, lat, lon, 0, 12, 60, 150, "спокойно", "творчество", None,
          note, None, "да", plus, minus, adult=3, src=src, acc=acc,
          booking="желательна", loud="частично", food="да", stroller="да")
    r["Сайт"] = None
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
