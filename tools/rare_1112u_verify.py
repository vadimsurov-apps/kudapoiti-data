"""Пачка для tools/set_verified.py по местам робота rare 12.11 (16 UTC): только поля, подтверждённые карточкой/выдачей Яндекс Карт и
сайтом (auto/pages), точка — справка OSM (объект места → «объект», здание по адресу → «дом»). Возраст — только где он в источнике.
python3 tools/rare_1112u_verify.py > batch.json"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_rare_1112u import ROWS, CARD, PTS

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
    lat, lon, acc = PTS[pid]
    lvl = "вход" if "вход:" in acc else "объект" if "объект:" in acc else "дом"
    f["point"] = {"lat": lat, "lon": lon, "level": lvl, "how": acc}
    out[pid] = {"fields": f, "src": c["src"] + " (проверено 2026-11-12)"}
print(json.dumps(out, ensure_ascii=False, indent=1))
