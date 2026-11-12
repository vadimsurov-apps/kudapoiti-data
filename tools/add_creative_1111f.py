"""Робот creative, третий запуск 11.11–12.11 (данные — tools/creative_1111f_data.py, точки — tools/creative_1111f_points.json
от tools/creative_1111f_pick.py по справке OSM crq-*). Точки нет — станция метро из карточки, «примерно»: место скрыто, пока
сверка с OSM по адресу не поставит его на дом/вход. WebFetch не использовался.
Запуск: KP_PART=creative python3 tools/add_creative_1111f.py [--dry]"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC
from creative_1111f_data import D, ORG

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DT = "2026-11-12"
CARDS = json.load(open(os.path.join(ROOT, "tools", "creative_1111f_cards.json")))
PTP = os.path.join(ROOT, "tools", "creative_1111f_points.json")
PTS = json.load(open(PTP)) if os.path.exists(PTP) else {}
MET = {}
for m in re.finditer(r'"([^"]+)": \("([^"]+)", ([\d.]+), ([\d.]+)\)', open(os.path.join(ROOT, "tools", "MetroStations.swift")).read()):
    MET[m.group(2)] = (float(m.group(3)), float(m.group(4)))
TAGS = {"dance": "спорт и активность, музыка", "ballet": "спорт и активность, музыка", "singing": "музыка",
        "music": "музыка", "theaterstudio": "сказки и театр, творчество", "drawing": "творчество", "ceramics": "творчество"}


def short(a):
    a = re.sub(r"^(Москва|Пушкино),\s*", "", a)
    a = re.sub(r"^.*микрорайон ", "мкр. ", a)
    return re.split(r", (этаж|подъезд|вход|аудитория|офис|помещение|кабинет|квартира|ТЦ|Библиотека|налево)", a)[0]


def row(k):
    pid, name, typ, cats, a0, a1, how, plus, asrc, _ = D[k]
    c = CARDS[str(k)]
    st, dist = c["metro"]
    if pid in PTS:
        lat, lon, acc = PTS[pid]
    else:
        if st not in MET:
            st, dist = c["q"].split("метро ")[-1], "по выдаче поиска"
        lat, lon = MET[st]
        acc = f"примерно: станция метро {st} (по карточке до места {dist}); дом и вход уточнит сверка с OSM по адресу"
    first = cats.split(",")[0]
    active = first in ("dance", "ballet")
    r = P(pid, name, typ, st, short(c["addr"]), lat, lon, a0, a1, 45, 90, "активно" if active else "спокойно", TAGS[first],
          None, None, None, "да", plus, None, adult=1,
          src=f"Яндекс Карты: выдача «{c['q']}» и карточка организации {('yandex.ru/maps/org/' + ORG[k]) if k in ORG else 'по названию и адресу'} (адрес, этаж, телефон, сайт, услуги), 11.11.2026; возраст — {asrc}",
          acc=acc, adult_price=None, booking="обязательна", loud="частично" if active or first in ("music", "singing") else "нет",
          sit="нет" if active else "частично", crowd="нет", food="нет", stroller="частично")
    r["Взрослый билет, ₽"] = None
    r["Сайт"] = ("https://" + c["site"].split()[0]) if c.get("site") else None
    r["Категории"] = cats
    r["Как найти"] = how
    r["Проверено (дата)"] = DT
    return r


ROWS = [row(k) for k in D]

if __name__ == "__main__":
    pa = json.load(open(os.path.join(ROOT, "places-all.json")))
    PL = {p["id"] for p in (pa["places"] if isinstance(pa, dict) else pa)}
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    ids = [r["id"] for r in ROWS]
    assert not [i for i in ids if i in existing or i in PL], [i for i in ids if i in existing or i in PL]
    if "--dry" in sys.argv:
        for r in ROWS:
            print(r["id"], "|", r["Адрес"], "|", r["Метро"], r["Широта"], r["Долгота"], "|", r["Точность координат"][:60], "|", r["Сайт"])
        sys.exit()
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
    cp = os.path.join(ROOT, "auto", "cat-ages.json")
    ca = json.load(open(cp)) if os.path.exists(cp) else {}
    for k, v in D.items():
        if v[9]:
            ca[v[0]] = dict(v[9], src=f"{v[8]} (11.11.2026)")
    json.dump(ca, open(cp, "w"), ensure_ascii=False, indent=1)
    print("rows", len(ROWS))
