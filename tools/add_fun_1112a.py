"""Робот fun, 2026-11-12 (проход a). Поиск по районам второго круга (Яндекс Карты, кэш auto/pages/*fuz*-1112a* —
поиск, *fuy* — карточки, *fux* — адреса с координатами): Мичуринский проспект, Мнёвники, Молодёжная, Мякинино,
Нагатинская, Нагорная, Народное Ополчение, Некрасовка, Нижегородская, Новогиреево, Новокосино, Новопеределкино,
Новоясеневская, Новые Черёмушки. Возраст — с сайта сети (кэш auto/pages). Пеленальных новых нет: оставшиеся точки
osm-changing.json — у дорог/набережных без понятного объекта (обратный поиск 1111w).
Иконки — tools/icons_fun_1112a.py. Запуск: KP_PART=fun python3 tools/add_fun_1112a.py
"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC
from add_batch14 import metro

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DAY = "2026-11-12"
YA = "Яндекс Карты, карточка организации (12.11.2026)"
HOUSE = "приблизительно — здание по адресу (Яндекс Карты, координаты дома)"
CH = {x["osm"]: x for x in json.load(open(os.path.join(ROOT, "auto", "osm-changing.json")))["points"]}
ROWS, VER = [], {}


def row(r, f, src):
    r["Проверено (дата)"] = DAY
    ROWS.append(r)
    VER[r["id"]] = {"fields": f, "src": src}


def changing(pid, name, osm, addr, plus, how, minus=""):
    x = CH[osm]
    lat, lon = round(x["lat"], 7), round(x["lon"], 7)
    src = f"OpenStreetMap {osm} (changing_table=yes)"
    r = P(pid, name, "пеленальная комната", metro(lat, lon), addr, lat, lon, 0, 3, 10, 20, "спокойно", "малыши",
          None, None, None, "да", plus, minus, adult=1, src=src, acc=f"точно (OSM {osm})", adult_price="",
          booking="не нужна", sit="частично", loud="нет", dark="нет", stroller="да", crowd="нет", food="нет")
    r["Категории"] = "changing"
    r["Пеленальный стол"] = "да"
    r["Как найти"] = how
    row(r, {"point": {"lat": lat, "lon": lon, "level": "объект", "how": f"OSM {osm}"}, "address": addr}, src)




# --- новые места по районам ---
def place(pid, name, typ, cats, tags, addr, lat, lon, a0, a1, d0, d1, energy, plus, phone, site="", how=None,
          minus="", loud="нет", sit="частично", booking="обязательна", adult=1, price=None):
    r = P(pid, name, typ, metro(lat, lon), addr, lat, lon, a0, a1, d0, d1, energy, tags, price, None, None, "да",
          plus, minus, adult=adult, src=YA, acc=HOUSE, adult_price="", booking=booking, sit=sit, loud=loud,
          dark="нет", stroller="нет", crowd="нет", food="нет")
    r["Сайт"] = site
    r["Категории"] = cats
    if how:
        r["Как найти"] = how
    f = {"address": addr, "phone": phone}
    if site:
        f["url"] = site
    row(r, f, YA)


OBJ = {}  # id -> (lat, lon, "точно (OSM …)") из auto/osm-answers.json, если нашёлся объект места

LT = "Лазертаг Арена: «Дети с 6 лет могут играть в наших клубах без сопровождения» (lt-arena.ru)"
place("fun-lt-arena-teleport", "Лазертаг «Лазертаг Арена» — локация «Телепорт»", "лазертаг", "quests",
      "спорт и активность, игры", "Москва, ул. Академика Анохина, 30", 55.660440, 37.467706, 6, 14, 60, 120, "активно",
      "Крытая лазертаг-арена сети «Лазертаг Арена»: классические игры и детские дни рождения; дети с 6 лет играют "
      "без сопровождения взрослых, имениннику игра бесплатно при наборе минимальной группы",
      "+7 495 414-31-33", "https://lt-arena.ru", loud="да", sit="нет")
place("fun-lt-arena-zabytaya-fabrika", "Лазертаг «Лазертаг Арена» — локация «Забытая фабрика»", "лазертаг", "quests",
      "спорт и активность, игры", "Москва, Профсоюзная ул., 56, этаж 4", 55.670123, 37.552543, 6, 14, 60, 120, "активно",
      "Крытая лазертаг-арена в антураже заброшенной фабрики: классические игры и детские дни рождения; дети с 6 лет "
      "играют без сопровождения взрослых, имениннику игра бесплатно при наборе минимальной группы",
      "+7 495 414-31-33", "https://lt-arena.ru", how="Этаж: 4", loud="да", sit="нет")
place("fun-liga-mirov-pandora", "Лазертаг-арена «Лига Миров: Пандора» (Вешняки)", "лазертаг", "quests",
      "спорт и активность, игры", "Москва, Вешняковская ул., 18, этаж 5", 55.724089, 37.825101, 7, 16, 60, 120, "активно",
      "Лазертаг и сюжетные игры: сценарий выбирают по возрасту самого младшего игрока, детские — от 7 лет; "
      "классический лазертаг в будни до 18:00 — от 6000 ₽ за час на 6 игроков", "+7 495 128-06-43",
      "https://ligamirov.ru", how="Этаж: 5", loud="да", sit="нет",
      minus="Есть сценарии с лёгким хоррором — выбирайте сюжет под возраст и смелость детей")
place("fun-kvant-epicentr", "Лазертаг «Квант Эпицентр» (Текстильщики)", "лазертаг", "quests",
      "спорт и активность, игры", "Москва, 8-я ул. Текстильщиков, 8", 55.704052, 37.740498, 7, 16, 60, 120, "активно",
      "Лазертаг с инструктором-ведущим и сюжетная игра «Роблокс» для ребят 7+; в будни час игры от 6 игроков, "
      "1300 ₽ за каждого дополнительного; после игры — 20 минут в зоне ожидания", "+7 965 118-18-16",
      "https://www.lasertagkvant.ru", loud="да", sit="нет")

for r in ROWS:
    if r["id"] in OBJ:
        la, lo, acc = OBJ[r["id"]]
        r["Широта"], r["Долгота"], r["Точность координат"] = la, lo, acc
        VER[r["id"]]["fields"]["point"] = {"lat": la, "lon": lo, "level": "объект", "how": acc}
VER["fun-lt-arena-teleport"]["src"] = VER["fun-lt-arena-zabytaya-fabrika"]["src"] = YA + "; " + LT

#PLACES

if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=i, column=1).value for i in range(2, ws.max_row + 1)}
    allids = {x["id"] for x in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    ids = [x["id"] for x in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    assert not [i for i in ids if i in existing or i in allids], [i for i in ids if i in existing or i in allids]
    for row_ in ROWS:
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        rr = ws.max_row + 1
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=rr, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    json.dump(VER, open("/tmp/claude-0/ver_fun_1112a.json", "w"), ensure_ascii=False, indent=1)
    print("rows", len(ROWS), "total", ws.max_row - 1)
