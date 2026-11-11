"""Пачка для tools/set_verified.py по местам робота creative 11.11: поля, подтверждённые карточкой Яндекс Карт и сайтом места.
python3 tools/creative_1111_verify.py > batch.json"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_creative_1111 import ROWS, CARD, PTS

out = {}
for r in ROWS:
    pid = r["id"]; c = CARD[pid]
    src = (f"Яндекс Карты, карточка организации и выдача «{c['q']}» (11.11.2026)"
           + (f"; сайт {c['site']} — возраст групп" if c.get("site") else ""))
    f = {"address": r["Адрес"], "type": r["Тип"], "cats": r["Категории"], "age_min": r["Возраст от"], "age_max": r["Возраст до"]}
    if c.get("phone"):
        f["phone"] = c["phone"]
    if r.get("Сайт"):
        f["url"] = r["Сайт"]
    if r.get("Как найти"):
        f["how"] = r["Как найти"]
    lat, lon, acc = PTS[pid]
    if acc.startswith("точно (объект:"):
        f["point"] = {"lat": lat, "lon": lon, "level": "объект", "how": acc}
    out[pid] = {"fields": f, "src": src}
print(json.dumps(out, ensure_ascii=False, indent=1))
