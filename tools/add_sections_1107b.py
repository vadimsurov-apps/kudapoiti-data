"""Робот sections, 2026-11-07 (00 UTC): шахматы «Максимум», «Лабиринты шахмат», Московская баскетбольная академия,
бадминтон SmashClub, настольный теннис SpinArt, фехтование СШОР «Северный», танцы. Ниже — шапка прошлого запуска.
Robot sections, 2026-11-06 (ночь, 21 UTC): бадминтон (СШОР МГФСО, БК «Красногорск»), волейбол/баскетбол
(RusVolley, Русская баскетбольная академия, JUNIBASKET, пляжный волейбол Beach Volleyball), шахматы (ChessKids, Chess First,
«Совёнок», «Гроссмейстер», Moscow Chess School, «Феномен»), прочий спорт (фехтование, настольный теннис, лёгкая атлетика,
парусный спорт), секции Подмосковья (гимнастика Перевозникова, ДСШ Яковлева, Raviga, «Русский самурай», Hockey Way,
Первая школа тенниса, «Футландия»), бассейны («Шторм», «Триумф»), балет и танцы («Азбука балета», «Вортэкс», TDANCE).
Источники — WebSearch → WebFetch только по ссылкам из поиска (проверено 2026-11-06), сырые записи в
tools/sections_1107b_data.json (поле source). Не брали: подтверждённые только каталогами (50chess, kartasporta, yandex/zoon
без сайта), часть залов RusVolley и «Шторма» рядом с уже добавленными бассейнами/залами.
Координаты — по метро или по городу («приблизительно»), уточнит geocode-address.yml.
Запуск: KP_PART=sections python3 tools/add_sections_1107.py [--dry]"""
import json, os, re, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
import add_sections_1106 as A
from add_sections_1106 import at, ST, SRC
from add_batch14 import MET

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sections_1107b_data.json")
D = "проверено 2026-11-07"
MO = "приблизительно, ±1–2 км (по адресу)"

DROP = set()

# координаты по адресу (приблизительно) для мест без метро в справочнике
XY = {"mba-zelenograd": (55.9965, 37.2085), "mba-trinta": (55.7010, 37.6040),
      "mba-krasnaya-pakhra": (55.4600, 37.2700), "sshor-severny-fencing": (55.8760, 37.5560),
      "schoolball-skolkovo": (55.6985, 37.3570), "djigit-solntsevo": (55.669782, 37.414176)}

KIND = {"badminton": ("спортивная секция", "спорт и активность", (60, 90)),
        "ballgames": ("спортивная секция", "спорт и активность", (60, 90)),
        "chess": ("шахматный клуб", "логика и головоломки", (60, 90)),
        "sport": ("спортивная секция", "спорт и активность", (60, 90)),
        "martial": ("спортивная секция", "спорт и активность", (45, 90)),
        "gymnastics": ("спортивная секция", "спорт и активность", (45, 90)),
        "racket": ("спортивная секция", "спорт и активность", (45, 90)),
        "hockey": ("спортивная секция", "спорт и активность", (45, 90)),
        "football": ("спортивная секция", "спорт и активность", (45, 60)),
        "pools": ("детский бассейн", "вода, спорт и активность", (45, 60)),
        "dance": ("танцевальная студия", "музыка, спорт и активность", (45, 60))}


def mdist(lat, lon):
    return min((math.hypot((lat - a) * 111, (lon - b) * 63), n) for n, a, b in MET)


def clean_addr(a):
    a = re.sub(r"^(Московская обл\.,\s*)", "", a.strip())
    a = re.sub(r"^Москва,\s*", "", a)
    a = re.sub(r"^г\.\s*", "", a)
    return a


def load():
    raw = json.load(open(DATA))
    out = []
    for x in raw:
        if x["id"] in DROP: continue
        m = (x.get("metro") or "").split(" (")[0].strip()
        if x["id"] in XY:
            lat, lon = XY[x["id"]]
            km, st = mdist(lat, lon)
            loc = (lat, lon, st if km < 2.0 else None, MO)
        elif m and m.lower().replace("ё", "е") in ST:
            loc = at(m)
        else:
            raise SystemExit(f"нет координат: {x['id']} {m}")
        typ, tags, d = KIND[x["cat"]]
        if x["cat"] == "dance" and "балет" in x["name"].lower(): typ = "балетная школа"
        if "водн" in x.get("sport", "") or x["id"].startswith("vodnik"): tags = "вода, спорт и активность"
        price = x.get("price")
        note = x.get("price_note") or ("бесплатно" if price == 0 else None)
        r = A.row(x["id"], x["name"], typ, loc, clean_addr(x["address"]), x["age_from"], x["age_to"], d[0], d[1], tags,
                  price, note, None, x["plus"], x["minus"], x["url"], x["cat"], src=f"{x['source']} ({D})")
        r["Детский билет, ₽"] = price
        r["Взрослый билет, ₽"] = None
        r["Проверено (дата)"] = "2026-11-07"
        out.append(r)
    return out


ROWS = load()

if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    allp = json.load(open(os.path.join(ROOT, "places-all.json")))["places"]
    allids = {x["id"] for x in allp}
    ids = [r["id"] for r in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    assert not [i for i in ids if i in existing or i in allids], [i for i in ids if i in existing or i in allids]
    # дубли: то же название (первые слова) ближе 300 м
    import glob
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
