"""Применяет отчёт auto/geocode-report.json к таблице: точные координаты из OSM.
python3 tools/apply_geocode.py [--with-medium id1,id2,...]
- high: применяется всегда (если место не отмечено «точно (вручную)»);
- medium: только перечисленные id (после ручной проверки);
- low / not-found: не трогаем, выводим список на ручную проверку."""
import json, os, sys
import openpyxl

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(root, "data", "kuda-poiti-mesta.xlsx")
rep = json.load(open(os.path.join(root, "auto", "geocode-report.json")))
extra = set()
if "--with-medium" in sys.argv:
    extra = set(sys.argv[sys.argv.index("--with-medium") + 1].split(","))

wb = openpyxl.load_workbook(SRC)
ws = wb["Места"]
hdr = {c.value: i + 1 for i, c in enumerate(ws[1])}
applied, skipped = 0, []
for r in range(2, ws.max_row + 1):
    pid = ws.cell(r, hdr["id"]).value
    x = rep.get(pid)
    if not x: continue
    acc = str(ws.cell(r, hdr["Точность координат"]).value or "")
    if "вручную" in acc or "проверено" in acc: continue
    ok = x.get("status") == "high" or (x.get("status") == "medium" and pid in extra)
    if not ok:
        skipped.append((pid, x.get("status"), x.get("moved_m"), x.get("osm_name")))
        continue
    ws.cell(r, hdr["Широта"]).value = x["lat"]
    ws.cell(r, hdr["Долгота"]).value = x["lon"]
    ws.cell(r, hdr["Точность координат"]).value = f'точно (OpenStreetMap {x["osm"]})'
    applied += 1
wb.save(SRC)
print("применено:", applied, "на проверку:", len(skipped))
