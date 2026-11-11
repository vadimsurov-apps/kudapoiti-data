"""Пачка для tools/set_verified.py по местам робота edu 11.11 (четвёртый запуск): подтверждённые карточкой Яндекс Карт поля.
python3 tools/edu_1114_verify.py > batch.json"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_edu_1114 import ROWS, ADDR, PTS, HOW
from edu_1114_sel import SEL

BY = {v[0]: v for v in SEL.values()}
out = {}
for r in ROWS:
    pid = r["id"]; a = ADDR[pid]; v = BY[pid]
    src = f"Яндекс Карты, карточка организации и выдача «{a['q'].replace(' | ', ' метро ')}» (11.11.2026)"
    f = {"address": r["Адрес"], "type": r["Тип"], "cats": r["Категории"], "age_min": v[4]}
    if v[5] != 17:
        f["age_max"] = v[5]
    if a.get("phone"):
        f["phone"] = a["phone"]
    if a.get("site"):
        f["url"] = a["site"]
    if v[6]:
        f["price_child"] = v[6]
    if HOW.get(pid):
        f["how"] = HOW[pid]
    lat, lon, acc = PTS[pid]
    if acc.startswith("точно (объект:"):
        f["point"] = {"lat": lat, "lon": lon, "level": "объект", "how": acc}
    out[pid] = {"fields": f, "src": src}
print(json.dumps(out, ensure_ascii=False, indent=1))
