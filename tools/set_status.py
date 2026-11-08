"""Робот «статус мест»: python3 tools/set_status.py batch.json
batch: {"<id>": {"Часы работы": "...", "Минусы+": "добавить к «Минус»", "Статус данных": "closed", ...}}
Ключ "Минусы+" дописывает текст к колонке «Минус» (если его там ещё нет). Таблицы роботов с замком пропускаются."""
import json, os, sys
import openpyxl
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from set_access import locked, ROOT

batch = json.load(open(sys.argv[1], encoding="utf-8"))
tables = [("main", os.path.join(ROOT, "data", "kuda-poiti-mesta.xlsx"))]
pd = os.path.join(ROOT, "data", "parts")
tables += [(f[:-5], os.path.join(pd, f)) for f in sorted(os.listdir(pd)) if f.endswith(".xlsx")]
done = set()
for part, path in tables:
    wb = openpyxl.load_workbook(path); ws = wb["Места"]
    head = [c.value for c in ws[1]]; ci = head.index("id"); changed = False
    for row in ws.iter_rows(min_row=2):
        pid = row[ci].value
        if pid not in batch or pid in done:
            continue
        if part != "main" and locked(part):
            print("locked", part, pid); continue
        for k, v in batch[pid].items():
            if k == "Минусы+":
                c = row[head.index("Минус")]; old = c.value or ""
                if v not in old:
                    c.value = (old.rstrip(". ") + ". " if old else "") + v
            else:
                row[head.index(k)].value = v
        done.add(pid); changed = True; print("ok", part, pid)
    if changed:
        wb.save(path)
print("missing:", set(batch) - done)
