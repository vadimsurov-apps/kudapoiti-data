"""Возраст по направлениям (урок 8) у мест робота edu 12.11 (шестой запуск) — только из названий услуг карточки Яндекс Карт.
python3 tools/edu_1116_catages.py → дописывает auto/cat-ages.json (только места, добавленные в таблицу)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_edu_1116 import ROWS
from edu_1116_sel import CATAGES
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Y = "Яндекс Карты, карточка организации, услуги: "
p = os.path.join(ROOT, "auto", "cat-ages.json")
data = json.load(open(p))
ids = {r["id"] for r in ROWS}
n = 0
for pid, (ages, txt) in CATAGES.items():
    if pid in ids:
        data[pid] = {**ages, "src": Y + txt + "; 12.11.2026"}
        n += 1
json.dump(data, open(p, "w"), ensure_ascii=False, indent=1)
print("cat_ages:", n)
