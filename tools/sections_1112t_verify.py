"""Пачка для tools/set_verified.py по местам робота sections 12.11 (03 UTC): поля, подтверждённые карточкой Яндекс Карт
(auto/pages, sc*-1112t) и сайтом клуба/сети; точка — справка OSM (sections_1112t_points.json).
python3 tools/sections_1112t_verify.py > batch.json"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_sections_1112t import ROWS, PHONE, SRC, URL, PT

out = {}
for r in ROWS:
    pid = r["id"]
    f = {"address": r["Адрес"], "type": r["Тип"], "cats": r["Категории"],
         "age_min": r["Возраст от"], "age_max": r["Возраст до"]}
    if PHONE.get(pid):
        f["phone"] = PHONE[pid]
    if URL.get(pid):
        f["url"] = URL[pid]
    if r.get("Как найти"):
        f["how"] = r["Как найти"]
    p = PT[pid]
    f["point"] = {"lat": p[0], "lon": p[1], "level": p[3], "how": p[2]}
    out[pid] = {"fields": f, "src": SRC[pid] + "; OSM (справка osm-query) (проверено 2026-11-12)"}
print(json.dumps(out, ensure_ascii=False, indent=1))
