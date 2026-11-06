"""Применяет auto/geocode-report.json (сверка с выгрузкой OSM) и auto/entrances.json к таблице — строго:
- тип объекта в OSM совпадает с нашим (tag_ok) и все значимые слова названия совпадают целиком (не «Небо» ↔ «Небоскрёб»);
- места, у которых уже точная точка (Яндекс / дом по адресу), сдвигаем только на ≤ 200 м (уточнение);
- филиалы сетей — только ≤ 400 м (иначе это другой филиал), остальные ≤ 1500 м, большие территории ≤ 3000 м;
- для парков/усадеб/зоопарков ставим точку ВХОДА (из entrances.json) и пишем «Как найти: вход …».
Запуск: python3 tools/apply_osm.py [--dry]"""
import json, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "pipeline"))
import openpyxl
from geocode import tokens, norm, dist

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(root, "data", "kuda-poiti-mesta.xlsx")
rep = json.load(open(os.path.join(root, "auto", "geocode-report.json")))
ent = json.load(open(os.path.join(root, "auto", "entrances.json")))
BIG = {"парк", "ботанический сад", "усадьба", "зоопарк", "кремль", "монастырь", "парк развлечений", "ферма",
       "контактный зоопарк", "пляж", "горнолыжный курорт", "железная дорога", "аквапарк"}
CHAIN = re.compile(r"anderson|chaihona|joki|kitchen|jooie|ribambelle|osteria|dapino|pavlin|mimi|pancho|uryuk|warpoint|"
                   r"nebo-|cin-|lt-|climb-|pool-|teika|kidburg|another-world|formula|karo|mega", re.I)


# проверено вручную 05.11: OSM нашёл не тот объект (памятник, соседний парк, велотрек и т.п.)
WRONG = {"my-russia-maket", "gorki-leninskie", "rink-krylatskoe", "rink-fili", "polenovo", "yasenevo-usadba",
         "fili-park", "serebryany-bor"}


def strict(name, osm_name):
    if not osm_name: return False
    ws = set(norm(osm_name).split())
    base = re.sub(r"\(.*?\)", "", name).strip() or name
    toks = tokens(base)
    return bool(toks) and all(any(w == t or (w.startswith(t) and len(w) - len(t) <= 2) or
                                  (t.startswith(w) and len(t) - len(w) <= 2 and len(w) >= 4) for w in ws) for t in toks)


def main(dry=False):
    import glob
    log = []
    for path in [SRC] + sorted(glob.glob(os.path.join(root, "data", "parts", "*.xlsx"))):
        log += apply_file(path, dry)
    return log


def apply_file(SRC, dry=False):
    print(os.path.basename(SRC), end=": ")
    wb = openpyxl.load_workbook(SRC); ws = wb["Места"]
    h = {c.value: i + 1 for i, c in enumerate(ws[1])}
    stats = {"точка": 0, "вход": 0, "пропущено": 0}
    log = []
    for r in range(2, ws.max_row + 1):
        pid = ws.cell(r, h["id"]).value
        x = rep.get(pid)
        if not x or x.get("status") not in ("high", "medium") or pid in WRONG: continue
        acc = str(ws.cell(r, h["Точность координат"]).value or "")
        if "вручную" in acc or "проверено" in acc: continue
        typ = str(ws.cell(r, h["Тип"]).value or "").split(",")[0].strip()
        lat0, lon0 = ws.cell(r, h["Широта"]).value, ws.cell(r, h["Долгота"]).value
        e = ent.get(pid)
        if typ in BIG and e and x.get("tag_ok") is not False and strict(x["name"], x.get("osm_name")):
            moved = dist(e["lat"], e["lon"], lat0, lon0)
            if moved <= 4000:
                ws.cell(r, h["Широта"]).value, ws.cell(r, h["Долгота"]).value = e["lat"], e["lon"]
                ws.cell(r, h["Точность координат"]).value = f'точно (вход, OpenStreetMap {e["osm"]})'
                if not ws.cell(r, h["Как найти"]).value:
                    nm = f' «{e["name"]}»' if e.get("name") else ""
                    tail = f', ближе всего к м. {e["metro"]}' if e.get("metro") else ""
                    ws.cell(r, h["Как найти"]).value = f"Точка — вход{nm}{tail}"
                stats["вход"] += 1; log.append(("вход", pid, round(moved)))
                continue
        ok = x.get("tag_ok") is True and strict(x["name"], x.get("osm_name"))
        moved = x.get("moved_m", 1e9)
        lim = 200 if acc.startswith("точно") else (400 if CHAIN.search(pid) else (3000 if typ in BIG else 1500))
        if ok and moved <= lim:
            ws.cell(r, h["Широта"]).value, ws.cell(r, h["Долгота"]).value = x["lat"], x["lon"]
            ws.cell(r, h["Точность координат"]).value = f'точно (OpenStreetMap {x["osm"]})'
            stats["точка"] += 1; log.append(("точка", pid, moved))
        else:
            stats["пропущено"] += 1
    if not dry: wb.save(SRC)
    print(stats)
    return log


if __name__ == "__main__":
    for l in main("--dry" in sys.argv): print(*l)
