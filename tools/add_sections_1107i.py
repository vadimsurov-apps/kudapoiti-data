"""Робот sections, 2026-11-07 (21 UTC): детские бассейны сети «Китёнок» — филиалы в Подмосковье и новые московские
ЖК, которых ещё не было (список адресов с 1kitenok.ru, кэш auto/pages/osm-node-9433110275; WebFetch не использовался).
Обнинск не брали (Калужская обл.). Точки: Реутов и «Мещерский лес» — объекты OSM «Китёнок» (node/7022176119,
node/9433110275), остальные — приблизительно по адресу, дом уточнит osm-local.
Остальные кандидаты из candidates.json (dance/sports_school/swimming) этого запуска не подтвердились: сайты не открываются
(racketball.ru, school-ball.com, bulkbulk.ru, quokkaclub.ru, osminozhka.su, myakishclub.ru, sheba-karate.ru) или без детских групп.
Запуск: KP_PART=sections python3 tools/add_sections_1107i.py [--dry]"""
import json, os, re, sys, math, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
import add_sections_1106 as A
from add_sections_1106 import at, near, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DT = "2026-11-07"
R = []


def add(pid, name, typ, loc, addr, a0, a1, d, price, note, plus, minus, cat, site, src, tags="спорт и активность",
        hours=None):
    r = A.row(pid, name, typ, loc, addr, a0, a1, d[0], d[1], tags, price, note, hours, plus, minus, site, cat,
              src=f"{src} (проверено {DT})")
    r["Детский билет, ₽"] = price
    r["Взрослый билет, ₽"] = price if price is not None else None
    r["Проверено (дата)"] = DT
    R.append(r)


# ---------------- «Китёнок» ----------------
OSM = "точно (OpenStreetMap)"
A1 = "приблизительно, ±1 км (по адресу)"
KIT = [
    ("metropoliya", "Волгоградский пр-т", "Волгоградский пр-т, 32/5, корп. 2 (ЖК «Метрополия»)", near(55.7236, 37.6930, A1)),
    ("meshchersky-les", "ЖК «Мещерский лес»", "ул. Домостроительная, 2 (ЖК «Мещерский лес»)",
     near(55.644544, 37.386618, OSM + " node/9433110275")),
    ("sirenevy-park", "Тагильская ул.", "Тагильская ул., 2, корп. 1 (ЖК «Сиреневый парк»)", near(55.8150, 37.7530, A1)),
    ("nikolskie-luga", "Варшавское ш., 282", "Варшавское ш., 282, корп. 1 (ЖК «Никольские Луга»)", near(55.5530, 37.5770, A1)),
    ("desnarechye", "Троицк, ЖК «Деснаречье»", "Троицк, ЖК «Деснаречье», квартал 9, д. 3, корп. 5",
     near(55.4790, 37.3160, "приблизительно, ±2 км (по адресу)")),
    ("sputnik", "ЖК «Спутник»", "Красногорск, ул. Липовой Рощи, 5, корп. 6 (ЖК «Спутник»)", near(55.8110, 37.3810, A1)),
    ("dolgoprudny", "Долгопрудный", "Долгопрудный, пр-т Лихачёва, 18, корп. 2 (ЖК «Квартал на набережной»)",
     near(55.9300, 37.5040, A1)),
    ("selyatino", "Селятино", "Наро-Фоминский г.о., пос. Селятино, Спортивная ул., 3/1", near(55.5160, 36.9790, A1)),
    ("drozhzhino", "Дрожжино", "Ленинский г.о., пос. Дрожжино, Южная ул., 12, корп. 3, пом. 3 (ЖК «Бутово Парк 2»)",
     near(55.5350, 37.5970, A1)),
    ("kotelniki-parkovy", "Котельники, мкр. Парковый", "Котельники, мкр. Парковый, 2", near(55.6600, 37.8640, A1)),
    ("kotelniki-novye", "Новые Котельники", "Котельники, мкр. Новые Котельники, 10", near(55.6470, 37.8380, A1)),
    ("mytishchi", "Мытищи", "Мытищи, Благовещенская ул., 4", near(55.9235, 37.7420, A1)),
    ("lyubertsy-krasnaya-gorka", "Люберцы, Красная горка", "Люберцы, пр-т Гагарина, 22, корп. 1 (мкр. Красная горка)",
     near(55.6770, 37.9060, A1)),
    ("lyubertsy-ukhtomskaya", "Люберцы, Ухтомская", "Люберцы, Колхозная ул., 10 (ст. Ухтомская)", near(55.6975, 37.9140, A1)),
    ("krasnoznamensk", "Краснознаменск", "Краснознаменск, Краснознаменная ул., 17А", near(55.6000, 37.0420, A1)),
    ("reutov", "Реутов", "Реутов, Комсомольская ул., 14", near(55.755676, 37.85186, OSM + " node/7022176119")),
    ("balashikha-zheleznodorozhny", "Балашиха, Железнодорожный", "Балашиха, Автозаводская ул., 6, стр. 1 (мкр. Железнодорожный)",
     near(55.7470, 38.0300, A1)),
    ("balashikha-pavlino", "Балашиха, Павлино", "Балашиха, д. Павлино, 67, пом. 2", near(55.7370, 38.0000, A1)),
    ("khimki-novokurkino", "Химки, Новокуркино", "Химки, Молодёжная ул., 50 (мкр. Новокуркино)", near(55.8960, 37.3960, A1)),
    ("khimki-yubileyny", "Химки, Юбилейный пр-т", "Химки, Юбилейный пр-т, 1/1", near(55.8870, 37.4340, A1)),
    ("lytkarino", "Лыткарино", "Лыткарино, Первомайская ул., 19, корп. 1", near(55.5810, 37.9030, A1)),
    ("odintsovo", "Одинцово", "Одинцово, Можайское ш., 121", near(55.6740, 37.2560, A1)),
    ("krasnogorsk-ilyinskoe", "Красногорск, Ильинское ш.", "Красногорск, Ильинское ш., 1А", near(55.8140, 37.3120, A1)),
    ("ilyinskie-luga", "ЖК «Ильинские Луга»", "Красногорск, пос. Ильинское-Усово, Заповедная ул., 15 (ЖК «Ильинские Луга»)",
     near(55.7780, 37.2350, A1)),
]
for slug, short, addr, loc in KIT:
    add(f"kitenok-{slug}", f"«Китёнок» — детский бассейн ({short})", "детский бассейн", loc, addr, 0, 10, (30, 60), 1500,
        "пробное занятие 1500 ₽; цену абонемента — у администратора",
        "Оздоровительное плавание для малышей с рождения и детей до 10 лет: индивидуальные занятия с тренером "
        "1 на 1 в тёплой воде",
        "Цены абонементов на сайте не опубликованы; занятия только по записи", "pools", "https://1kitenok.ru/",
        "1kitenok.ru — адреса филиалов", tags="вода, спорт и активность", hours="ежедневно 9:00–21:00")

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
