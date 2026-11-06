"""Применяет auto/address-geocode.json (дом по точному адресу, OSM Nominatim/Photon) ко всем таблицам.
Только если номер дома (и строение) в ответе совпал с адресом; не трогает большие территории, ВДНХ и места,
у которых уже точная точка. Для мест в ТЦ дописывает «Как найти: Внутри ТЦ «…», N этаж».
python3 tools/apply_address.py [--dry]"""
import glob, json, os, re, sys
import openpyxl
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = json.load(open(os.path.join(root, "auto", "address-geocode.json")))
BIG = {"парк", "ботанический сад", "усадьба", "зоопарк", "кремль", "монастырь", "парк развлечений", "ферма",
       "контактный зоопарк", "пляж", "горнолыжный курорт", "железная дорога", "аквапарк", "экскурсия", "прогулка",
       "смотровая площадка", "детская площадка", "горка", "каток", "скейт-парк"}
norm = lambda s: s.lower().replace(" ", "").replace("стр", "с").replace("корп", "к")


def good(v):
    if v.get("status") != "house" or "километр" in (v.get("display") or ""): return False
    m = re.search(r",\s*(\d+[а-яА-Яa-z]?(?:/\d+)?(?:[ск]\d+\w*)*)\s*$", v["q"].split("(")[0].strip())
    if not m: return False
    want = norm(m.group(1)); toks = [norm(t) for t in (v.get("display") or "").split(",")]
    return any(t == want or (t.startswith(want) and t[len(want):len(want) + 1] in ("с", "к", "/")) for t in toks)


def run(path, dry):
    wb = openpyxl.load_workbook(path); ws = wb["Места"]; h = {c.value: i + 1 for i, c in enumerate(ws[1])}
    n = hints = 0
    for r in range(2, ws.max_row + 1):
        pid = ws.cell(r, h["id"]).value
        v = A.get(pid)
        if not v or not good(v): continue
        if str(ws.cell(r, h["Точность координат"]).value or "").startswith("точно"): continue
        typ = str(ws.cell(r, h["Тип"]).value or "").split(",")[0].strip()
        addr = ws.cell(r, h["Адрес"]).value or ""
        if typ in BIG or "ВДНХ" in addr: continue
        ws.cell(r, h["Широта"]).value, ws.cell(r, h["Долгота"]).value = v["lat"], v["lon"]
        ws.cell(r, h["Точность координат"]).value = f"точно (дом по адресу, OpenStreetMap {v['osm']})"
        n += 1
        if "Как найти" in h and not ws.cell(r, h["Как найти"]).value:
            mall = re.search(r"(ТЦ|ТРЦ|ТРК|МФК|БЦ)\s*«[^»]+»(?:,\s*(\d+)\s*этаж)?", addr)
            if mall:
                ws.cell(r, h["Как найти"]).value = f"Внутри {mall.group(0).split(',')[0]}" + (f", {mall.group(2)} этаж" if mall.group(2) else "")
                hints += 1
    if not dry: wb.save(path)
    print(os.path.basename(path), "домов:", n, "подсказок:", hints)


for p in [os.path.join(root, "data", "kuda-poiti-mesta.xlsx")] + sorted(glob.glob(os.path.join(root, "data", "parts", "*.xlsx"))):
    run(p, "--dry" in sys.argv)
