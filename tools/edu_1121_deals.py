"""Акции «пробное бесплатно» у мест робота edu 12.11 (одиннадцатый запуск) — из карточек организаций Яндекс Карт
(«Бесплатное пробное занятие в КлёвоКод = 0 ₽», «Пробный урок программирования для детей = 0 ₽»).
python3 tools/edu_1121_deals.py → дописывает deals.json (только места, добавленные в таблицу)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_edu_1121 import ROWS, E
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
D = {
 "klevokod-lva-yashina": ("trial", E["20:85"]["org"], "Бесплатное пробное занятие", "Пробное занятие по программированию и робототехнике в «КлёвоКод» на улице Льва Яшина — бесплатно."),
 "mentor-it-korabelnaya": ("trial", E["21:177"]["org"], "Бесплатный пробный урок программирования", "Пробный урок программирования для детей 7–17 лет в «Ментор IT» на Корабельной — бесплатно."),
}
p = os.path.join(ROOT, "deals.json")
data = json.load(open(p))
have = {d["id"] for d in data["deals"]}
ids = {r["id"] for r in ROWS}
n = 0
for pid, (kind, url, title, det) in D.items():
    did = f"{pid}-{kind}"
    if pid in ids and did not in have and url:
        data["deals"].append({"id": did, "place_id": pid, "kind": kind, "title": title, "details": det, "code": "", "until": "", "url": url, "checked": "2026-11-12"})
        n += 1
json.dump(data, open(p, "w"), ensure_ascii=False, indent=1)
print("акций:", n)
