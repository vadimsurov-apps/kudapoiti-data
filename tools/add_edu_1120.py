"""Робот edu, 2026-11-12 (десятый запуск): места из карточек Яндекс Карт (tools/edu_1120_sel.py), точка — справка OSM (edu19-*/edu20-*).
Запуск: KP_PART=edu python3 tools/add_edu_1120.py [--dry]"""
import glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC
from edu_1120_sel import SEL

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
HERE = os.path.dirname(os.path.abspath(__file__))
DT = "2026-11-12"
E = {**{"19:" + k: v for k, v in json.load(open(os.path.join(HERE, "edu_1119_ext.json"))).items()},
     **{"20:" + k: v for k, v in (json.load(open(os.path.join(HERE, "edu_1120_ext.json"))).items() if os.path.exists(os.path.join(HERE, "edu_1120_ext.json")) else [])}}
_pp = os.path.join(HERE, "edu_1120_points.json")
PTS = json.load(open(_pp)) if os.path.exists(_pp) else {}
YA = "Яндекс Карты: карточка организации (рубрика, адрес, этаж/вход, телефон, сайт, услуги, цены и возраст групп, доступность), выдача «{q}», 12.11.2026"
SITE_SRC = {"cns-neiro-zlatoustinsky": "сайт cns-neiro.ru (помогаем детям с 2015 года; ждём на диагностику детей от 3 лет)",
            "zdorovy-rebenok-ivanteevka": "сайт zr-ivanteevka.ru (дети от 2 лет)"}
HOW_FIX = {}
TOWNS = ("Москва", "Ивантеевка", "Дзержинский", "Солнечногорск", "Фрязино", "Лыткарино", "Реутов", "Щёлково", "Истра", "Лобня", "Зеленоград")


def page(n):
    f = glob.glob(os.path.join(ROOT, f"auto/pages/*-ev{n.split(':')[1]}-11{n.split(':')[0]}e-*.txt"))[0]
    secs = open(f).read().split("\n### ")
    return [l.strip() for l in "\n".join([secs[0]] + [s for s in secs[1:] if s.startswith("https://yandex.ru/maps/org/")]).splitlines() if l.strip()]


def addr_how(n):
    a = E[n]["addr"]
    first = a[0].replace(", Москва вход", ", Москва, вход").replace(", Москва Вход", ", Москва, Вход")
    if ", Москва, " in first and not first.startswith("Москва"):
        first, rest = first.split(", Москва, ", 1)
        first += ", Москва"; a = [first, rest] + a[1:]
    # «Москва, Новомосковский административный округ, район Коммунарка, ЖК Скандинавия, улица …» → короче
    first = re.sub(r"Новомосковский административный округ, район Коммунарка, (ЖК Скандинавия, )?", "посёлок Коммунарка, ", first)
    first = first.replace("Москва, Зеленоградский административный округ, ", "Москва, Зеленоград, ")
    extra = []
    m = re.match(r"(.*?\d+[А-Яа-я]?(, (корп|стр)\. ?\S+)?)\s+([Вв]ход .*|подъезд .*|вывеска .*)$", first)
    if m:
        first, extra = m.group(1), [m.group(4)]
    if first.endswith(", Москва"):
        first = "Москва, " + first[:-8]
    if first.startswith("посёлок Коммунарка"):
        first = "Москва, " + first
    for t in TOWNS[1:]:
        if first.endswith(", " + t):
            first = t + ", " + first[:-len(t) - 2]
    if not first.startswith(TOWNS):
        first = "Москва, " + first
    extra += [x for x in a[1:]]
    how = []
    for p in ", ".join(extra).split(", "):
        p = p.strip()
        if not p or p.startswith(("Метро", "Улица")):
            continue
        if p.startswith("этаж"):
            how.append("Этаж: " + p[5:].strip())
        elif p.startswith("подъезд"):
            how.append("Вход: подъезд " + p[8:].strip())
        elif re.match(r"(офис|кабинет|помещение|комната)", p):
            how.append(p[0].upper() + p[1:])
        elif re.match(r"^\d+$", p):
            continue
        else:
            v = p[5:].strip() if p.lower().startswith("вход ") else p
            how.append("Вход: " + v[0].lower() + v[1:])
    vh = [x[6:] for x in how if x.startswith("Вход: ")]
    et = [x for x in how if x.startswith("Этаж")]
    of = [x for x in how if re.match(r"(Офис|Кабинет|Помещение|Комната)", x)]
    out = (["Вход: " + ", ".join(vh)] if vh else [])
    if et:
        out.append(et[0] + (", " + of[0][0].lower() + of[0][1:] if of else ""))
    elif of:
        out.append(of[0])
    return first, "\n".join(out) or None


def access(n, inclusive_note=None):
    L = page(n)
    ent = next((l.split(":")[-1].strip() for l in L if l.startswith("Доступность входа на инвалидной коляске :")), None)
    room = next((l.split(":")[-1].strip() for l in L if l.startswith("Доступность помещения на инвалидной коляске :")), None)
    a = {}
    if ent == "недоступно" or room == "недоступно":
        a["wheelchair"] = "no"
    elif ent == "доступно" and room == "доступно":
        a["wheelchair"] = "yes"
    elif ent or room:
        a["wheelchair"] = "limited"
    notes = []
    if ent: notes.append(f"вход на коляске — {ent}")
    if room: notes.append(f"помещение — {room}")
    if "Пандус" in L: notes.append("есть пандус")
    if "Туалет для людей с инвалидностью" in L: a["toilet"] = "yes"
    if "Лифт" in L: a["lift"] = "yes"
    if "Парковка для людей с инвалидностью" in L: a["parking"] = "yes"
    if inclusive_note: a["programs"] = inclusive_note
    if notes: a["note"] = ", ".join(notes).capitalize() + " (Яндекс Карты)"
    return a


def row(pid):
    n, name, typ, cats, a0, a1, price, note, plus, tags, trial = SEL[pid]
    o = E[n]
    addr, how = addr_how(n)
    lat, lon, acc = PTS[pid]
    src = YA.format(q=o["q"]) + (f"; {o['org']}" if o.get("org") else "") + (f"; {SITE_SRC[pid]}" if pid in SITE_SRC else "")
    r = P(pid, name, typ, metro(lat, lon) if addr.startswith("Москва") else None, addr, lat, lon, a0, a1, 45, 60, "спокойно", tags, price, note, None, "да",
          plus, None, adult=1, src=src, acc=acc, adult_price=None,
          booking="обязательна", loud="нет", sit="частично", crowd="нет", food="нет", stroller="частично")
    r["Взрослый билет, ₽"] = None
    r["Сайт"] = ("https://" + o["site"].rstrip("/") + "/") if o.get("site") else None
    r["Категории"] = cats
    r["Как найти"] = "\n".join(l for l in (how or "").split("\n") if "филиал" not in l.lower()) or None
    if pid in HOW_FIX: r["Как найти"] = HOW_FIX[pid]
    r["Проверено (дата)"] = DT
    r["Коляска"] = None
    r["Громко"] = None
    return r


ROWS = [row(p) for p in SEL if p in PTS]

if __name__ == "__main__":
    pa = json.load(open(os.path.join(ROOT, "places-all.json")))
    PL = {p["id"] for p in (pa["places"] if isinstance(pa, dict) else pa)}
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    ids = [r["id"] for r in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    ROWS = [r for r in ROWS if r["id"] not in existing and r["id"] not in PL]
    if "--dry" in sys.argv:
        for r in ROWS: print(r["id"], "|", r["Адрес"], "|", (r["Как найти"] or "").replace("\n", " / "), "|", r["Метро"], "|", r["Сайт"])
        print(len(ROWS)); sys.exit()
    r0 = 2 if ws.max_row == 1 or ws.cell(row=2, column=1).value is None else ws.max_row + 1
    for k, row_ in enumerate(ROWS):
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        r = r0 + k
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=r, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    print("rows", len(ROWS))
