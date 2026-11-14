"""Робот creative, 14.11 (запуск 1114d): места из выдач Яндекс Карт по 15 районам (Внуково, Сосенское, Новомосковский, Бутово,
Мосрентген + второй круг Авиамоторная … Аннино, auto/pages *-cv<N>-1114d*), карточки организаций (*-cc<N>-1114dc*) и сайты мест
из кэша auto/pages (lovedancestudio.ru, vetamusiclab.ru, dance-butovo.ru, карнавалмосква.рф). Возраст — только по источнику
(группы набора); без указанного возраста места не брались. Точки — справка OSM cr14d-*. WebFetch не использовался.
Запуск: KP_PART=creative python3 tools/add_creative_1114d.py [--dry|deals|catages|verify]"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DT = "2026-11-14"
OBJ = "объект"

from creative_1114d_data import D, TRIAL_SRC

PTP = os.path.join(ROOT, "tools", "creative_1114d_points.json")
ENTR = json.load(open(PTP)) if os.path.exists(PTP) else {}
TAGS = {"dance": "спорт и активность, музыка", "ballet": "спорт и активность, музыка", "singing": "музыка",
        "music": "музыка", "theaterstudio": "сказки и театр, творчество", "drawing": "творчество", "ceramics": "творчество"}


def point(pid):
    e = ENTR[pid]
    if e["level"] == OBJ:
        return e["lat"], e["lon"], f'точно (объект: {e["osm"]}), {e["why"]}, 14.11', OBJ
    if e["level"] == "вход":
        return e["lat"], e["lon"], f'точно (вход: {e["osm"]}), OSM вход здания {D[pid][6]} — {e["why"]}, 14.11', "вход"
    return e["lat"], e["lon"], f'точно (дом по адресу {D[pid][6]}, координаты здания — Яндекс Карты); дверь уточнит сверка', "дом"


def row(pid):
    name, typ, cats, a0, a1, met, addr, phone, site, how, plus, price, note, asrc, ya, ca = D[pid]
    lat, lon, acc, lvl = point(pid)
    first = cats.split(",")[0]
    active = any(c in ("dance", "ballet") for c in cats.split(","))
    r = P(pid, name, typ, met, addr, lat, lon, a0, a1, 45, 90, "активно" if active else "спокойно", TAGS[first],
          price, note, None, "да", plus, None, adult=1,
          src=(f"Яндекс Карты: карточка организации yandex.ru/maps/org/{ya} (адрес, этаж, телефон, сайт), 14.11.2026; " if ya else
               "Яндекс Карты: поиск по адресу (координаты здания), 14.11.2026; ") + f"возраст и цены — {asrc}",
          acc=acc, adult_price=None, booking="обязательна", loud="частично" if active or first in ("music", "singing") else "нет",
          sit="нет" if active else "частично", crowd="нет", food="нет", stroller="частично")
    r["Взрослый билет, ₽"] = None
    r["Сайт"] = site
    r["Категории"] = cats
    r["Как найти"] = how
    r["Проверено (дата)"] = DT
    return r


TRIAL = TRIAL_SRC

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    ROWS = [row(k) for k in D]
    if mode == "deals":
        p = os.path.join(ROOT, "deals.json")
        d = json.load(open(p))
        have = {x["id"] for x in d["deals"]}
        n = 0
        for pid, (t, det, url) in TRIAL.items():
            did = pid + "-trial"
            if did not in have:
                d["deals"].append({"id": did, "place_id": pid, "kind": "trial", "title": t, "details": det, "code": "",
                                   "until": "", "url": url, "checked": DT}); n += 1
        json.dump(d, open(p, "w"), ensure_ascii=False, indent=1)
        print("акций", n); sys.exit()
    if mode == "catages":
        p = os.path.join(ROOT, "auto/cat-ages.json")
        ca = json.load(open(p))
        for pid in D:
            if D[pid][15]:
                ca[pid] = dict(D[pid][15], src=D[pid][13])
        json.dump(ca, open(p, "w"), ensure_ascii=False, indent=1)
        print("cat_ages", sum(1 for pid in D if D[pid][15])); sys.exit()
    if mode == "verify":
        out = {}
        for pid in D:
            r = next(x for x in ROWS if x["id"] == pid)
            f = {"address": r["Адрес"], "type": r["Тип"], "cats": r["Категории"], "age_min": r["Возраст от"],
                 "age_max": r["Возраст до"], "booking": "обязательна", "phone": D[pid][7]}
            if r["Сайт"]: f["url"] = r["Сайт"]
            if r["Как найти"]: f["how"] = r["Как найти"]
            if r["Детский билет, ₽"]: f["price_child"] = r["Детский билет, ₽"]
            if r["Бесплатно до (лет / см)"]: f["free_note"] = r["Бесплатно до (лет / см)"]
            lat, lon, acc, lvl = point(pid)
            if lvl in (OBJ, "вход"):
                f["point"] = {"lat": lat, "lon": lon, "level": lvl, "how": acc}
            out[pid] = {"fields": f, "src": r["Источник"]}
        print(json.dumps(out, ensure_ascii=False, indent=1)); sys.exit()
    pa = json.load(open(os.path.join(ROOT, "places-all.json")))
    PL = {p["id"] for p in (pa["places"] if isinstance(pa, dict) else pa)}
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    bad = [r["id"] for r in ROWS if r["id"] in existing or r["id"] in PL]
    assert not bad, bad
    if mode == "--dry":
        for r in ROWS:
            print(r["id"], "|", r["Адрес"], "|", r["Широта"], r["Долгота"], "|", r["Точность координат"][:90])
        print([k for k in ROWS[0] if k not in hdr]); sys.exit()
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    r0 = ws.max_row + 1
    for n, row_ in enumerate(ROWS):
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=r0 + n, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    print("rows", len(ROWS))
