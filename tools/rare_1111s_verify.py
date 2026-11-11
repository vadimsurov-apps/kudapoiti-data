"""Пачка для tools/set_verified.py по местам робота rare 11.11 (19 UTC): только поля, подтверждённые карточкой/выдачей
Яндекс Карт (auto/pages) и, для точки, объектом OSM из справки osm-query. Возраст — только где он есть в источнике.
python3 tools/rare_1111s_verify.py > batch.json"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_rare_1111s import ROWS, CARD, PTS

out = {}
for r in ROWS:
    pid = r["id"]; c = CARD[pid]
    f = {"address": r["Адрес"], "type": r["Тип"], "cats": r["Категории"]}
    if c["ages_src"]:
        f["age_min"] = r["Возраст от"]; f["age_max"] = r["Возраст до"]
    if r.get("Детский билет, ₽") is not None:
        f["price_child"] = r["Детский билет, ₽"]
    if c.get("phone"):
        f["phone"] = c["phone"]
    if r.get("Сайт"):
        f["url"] = r["Сайт"]
    if r.get("Как найти"):
        f["how"] = r["Как найти"]
    p = PTS.get(pid)
    if p and p.get("level"):
        f["point"] = {"lat": p["lat"], "lon": p["lon"], "level": p["level"], "how": p["acc"]}
    out[pid] = {"fields": f, "src": c["src"] + " (проверено 2026-11-11)"}
print(json.dumps(out, ensure_ascii=False, indent=1))
