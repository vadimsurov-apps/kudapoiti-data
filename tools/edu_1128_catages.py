"""Возраст по направлениям (урок 8) у мест робота edu, восемнадцатый запуск (tools/edu_1128_sel.py) — из карточек Яндекс Карт.
python3 tools/edu_1127_catages.py → дописывает auto/cat-ages.json."""
import json, os, sys, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
with contextlib.redirect_stdout(io.StringIO()):
    import add_edu_1128 as A26
from edu_1128_sel import CATAGES as C26
Y = "Яндекс Карты, карточка организации, услуги: "
p = os.path.join(ROOT, "auto", "cat-ages.json")
data = json.load(open(p))
ids = {r["id"] for r in A26.ROWS}
n = 0
for pid, (ages, txt) in C26.items():
    if pid in ids and pid not in data:
        data[pid] = {**ages, "src": Y + txt + "; 13.11.2026"}
        n += 1
json.dump(data, open(p, "w"), ensure_ascii=False, indent=1)
print("cat_ages:", n)
