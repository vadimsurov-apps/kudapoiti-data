"""Пачка для tools/set_verified.py по местам робота creative 11.11 (второй запуск): поля, подтверждённые карточкой
Яндекс Карт и сайтом места. Точки нет (справка OSM не пришла) — point не пишем. python3 tools/creative_1111d_verify.py > batch.json"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_creative_1111d import ROWS, D

out = {}
for r in ROWS:
    pid = r["id"]; d = D[pid]
    f = {"address": r["Адрес"], "type": r["Тип"], "cats": r["Категории"], "age_min": r["Возраст от"], "age_max": r["Возраст до"],
         "phone": d[7]}
    if d[8]:
        f["url"] = d[8]
    if d[6]:
        f["how"] = d[6]
    out[pid] = {"fields": f, "src": r["Источник"]}
print(json.dumps(out, ensure_ascii=False, indent=1))
