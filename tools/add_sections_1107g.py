"""Робот sections, 2026-11-07 (15 UTC): приоритет — ballgames, chess, sport.
Источники (кэш auto/pages, WebFetch не использовался):
 - cskabasket.school/addr — сеть детских школ баскетбола ПБК ЦСКА, 5 центров, которых ещё не было
   (Текстильщики, Автозаводская, Щербинка, Коммунарка, Авиаторов); Авангардную ул. не брали — рядом уже стоят
   «Смольная» и «Кронштадтский б-р» (последнего на сайте больше нет — возможно, переехал на Авангардную), группы 3–16 лет;
 - champion-chesskids.ru (+ /adres) — детский шахматный клуб «Чемпионы», 3–14 лет, пробное бесплатно, 11 из 15 адресов
   (Реутов и Федеративный пр-т; остальные 4 — соседние дома тех же улиц, оставлены);
 - moscowvolley.ru/volleyball/childrensvolleyball/schools — спортшкола волейбола ЦОиС «Москва-98» (СШ «Олимп»), ул. Удальцова, 40;
 - hi.horoshkola.ru/nastolnyj-tennis — настольный теннис для 1–7 классов в Хорошколе, ул. Народного Ополчения, 7А.
Не брали (не подтвердилось страницей места): Федерация фехтования на мечах на Партизанской и Хорошёвском ш. (только
агрегаторы), СШОР ЦСКА по пятиборью на Дыбенко, клубы настольного тенниса из SEO-подборки vc.ru (TENIX, ArtTT, V2,
ЛуЦентр), Play Badminton (только взрослые).
Координаты — по метро или соседним точкам («приблизительно»), точку по адресу уточнит osm-local.
Запуск: KP_PART=sections python3 tools/add_sections_1107g.py [--dry]"""
import json, os, re, sys, math, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
import add_sections_1106 as A
from add_sections_1106 import at, near, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DT = "2026-11-07"
R = []
SEC = "спортивная секция"
SP = "спорт и активность"


def add(pid, name, loc, addr, a0, a1, price, note, plus, minus, cat, site, src, tags=SP, d=(45, 60), typ=SEC, hours=None):
    r = A.row(pid, name, typ, loc, addr, a0, a1, d[0], d[1], tags, price, note, hours, plus, minus, site, cat,
              src=f"{src} (проверено {DT})")
    r["Детский билет, ₽"] = price
    r["Взрослый билет, ₽"] = None
    r["Проверено (дата)"] = DT
    R.append(r)


# ---------------- ПБК ЦСКА — детские школы баскетбола ----------------
CSKA = "https://cskabasket.school/addr/"
for pid, where, addr, loc in [
        ("pbk-cska-tekstilshchiki", "Текстильщики", "Волжский б-р, 16, корп. 2", at("Текстильщики")),
        ("pbk-cska-avtozavodskaya", "Автозаводская ул.", "Автозаводская ул., 25", at("Автозаводская")),
        ("pbk-cska-shcherbinka", "Щербинка", "Щербинка, Индустриальная ул., 2", near(55.5062, 37.5590)),
        ("pbk-cska-kommunarka", "Коммунарка", "пос. Газопровод, 101, корп. 8 (Коммунарка)", at("Ольховая")),
        ("pbk-cska-aviatorov", "ул. Авиаторов", "ул. Авиаторов, 7Б (Солнцево)", near(55.6418, 37.4052))]:
    add(pid, f"Школа баскетбола ПБК ЦСКА ({where})", loc, addr, 3, 16, None,
        "пробное занятие — по записи на сайте; цены абонементов — у администратора центра",
        "Детская школа баскетбола от профессионального клуба ЦСКА: группы по возрасту с 3 до 16 лет, игровые тренировки",
        "Цены на сайте не опубликованы; запись на пробное заранее", "ballgames", CSKA, "cskabasket.school — адреса центров")

# ---------------- Шахматный клуб «Чемпионы» ----------------
CH = "http://champion-chesskids.ru/adres"
CHP = ("Шахматы для детей 3–14 лет в небольших группах: малыши учатся в игровой форме, старшие — турниры и разряды. "
       "Первое занятие бесплатно")
CHM = "Занятия проходят в помещениях школ и центров — точный вход уточняйте у администратора"
for pid, addr, loc in [
        ("champions-chess-federativny", "Федеративный пр-т, 8А", near(55.7512, 37.7836, "приблизительно, ±300 м (соседний дом)")),
        ("champions-chess-sovetskaya-6a", "Реутов, Советская ул., 6А", near(55.7600, 37.8580)),
        ("champions-chess-sovetskaya-16a", "Реутов, Советская ул., 16А", near(55.7612, 37.8620)),
        ("champions-chess-nekrasova", "Реутов, ул. Некрасова, 8", near(55.7705, 37.8512, "приблизительно, ±500 м (по соседнему дому)")),
        ("champions-chess-golovashkina", "Реутов, ул. Головашкина, 7", near(55.7598, 37.8482)),
        ("champions-chess-gagarina", "Реутов, ул. Гагарина, 17Б", near(55.7642, 37.8645)),
        ("champions-chess-komsomolskaya", "Реутов, Комсомольская ул., 15", near(55.7658, 37.8592)),
        ("champions-chess-kotovskogo", "Реутов, ул. Котовского, 13", near(55.7478, 37.8690, "приблизительно, ±300 м (соседний дом)")),
        ("champions-chess-yuzhnaya", "Реутов, Южная ул., 8", near(55.7486, 37.8612, "приблизительно, ±300 м (соседний дом)")),
        ("champions-chess-oktyabrya", "Реутов, ул. Октября, 50", near(55.7530, 37.8812, "приблизительно, ±500 м (по соседнему дому)")),
        ("champions-chess-nosovikhinskoe", "Реутов, Носовихинское ш., 24", near(55.7522, 37.8702))]:
    short = re.sub(r"^Реутов, ", "", addr)
    city = "Реутов, " if addr.startswith("Реутов") else ""
    add(pid, f"Шахматный клуб «Чемпионы» ({city}{short})", loc, addr, 3, 14, 0,
        "первое пробное занятие бесплатно; абонемент — у администратора", CHP, CHM, "chess", CH,
        "champion-chesskids.ru — адреса филиалов", tags="логика, спорт и активность", d=(45, 60))

# ---------------- Волейбол: ЦОиС «Москва-98» (СШ «Олимп») ----------------
add("moskva98-volley-udaltsova", "Спортшкола «Олимп» ЦОиС «Москва-98» — детский волейбол", at("Проспект Вернадского"),
    "ул. Удальцова, 40", 7, 17, 0,
    "бюджетные группы — бесплатно по отбору; запись — mos.ru «Запись в спортшколу»",
    "Государственная спортшкола Москомспорта с отделением волейбола — в списке спортшкол Московской федерации волейбола",
    "Набор по возрасту и отбору, места в группах ограничены", "ballgames",
    "https://moscowvolley.ru/volleyball/childrensvolleyball/schools/", "moscowvolley.ru — спортшколы", d=(90, 90))

# ---------------- Настольный теннис в Хорошколе ----------------
add("horoshkola-table-tennis", "Настольный теннис в Хорошколе (Народного Ополчения)", at("Народное Ополчение"),
    "ул. Народного Ополчения, 7А (прогимназия)", 7, 13, 1450, "1450 ₽ за занятие",
    "Секция настольного тенниса для 1–7 классов: вращения, углы и тактика, тренер — чемпион Костромской области",
    "Занятия 1–2 раза в неделю по расписанию, запись через сайт", "sport",
    "https://hi.horoshkola.ru/nastolnyj-tennis", "hi.horoshkola.ru — настольный теннис", d=(60, 60))

ROWS = R
if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    allp = json.load(open(os.path.join(ROOT, "places.json")))["places"]
    allids = {x["id"] for x in allp}
    ids = [r["id"] for r in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    assert not [i for i in ids if i in existing or i in allids], [i for i in ids if i in existing or i in allids]
    pts = [(p["name"], p["lat"], p["lon"]) for p in allp]
    for f in glob.glob(os.path.join(ROOT, "data", "parts", "*.xlsx")):
        rr = list(openpyxl.load_workbook(f, read_only=True)["Места"].values); h = rr[0]
        pts += [(r[h.index("Название")], r[h.index("Широта")], r[h.index("Долгота")]) for r in rr[1:] if r[h.index("Широта")]]
    key = lambda n: re.sub(r"[«»\"()—,.-]", " ", str(n).lower()).split()[:2]
    for r in ROWS:
        for n, a, b in pts:
            if a and math.hypot((r["Широта"] - a) * 111000, (r["Долгота"] - b) * 63000) < 300 and key(n) == key(r["Название"]):
                print("ДУБЛЬ?", r["id"], "~", n)
    if "--dry" in sys.argv:
        for r in ROWS: print(r["id"], "|", r["Название"], "|", r["Метро"], "|", r["Категории"], "|", r["Широта"], r["Долгота"])
        from collections import Counter
        print("rows", len(ROWS), Counter(r["Категории"] for r in ROWS)); sys.exit()
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    for row_ in ROWS:
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        r = ws.max_row + 1
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=r, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    print("rows", len(ROWS), "total", ws.max_row - 1)
