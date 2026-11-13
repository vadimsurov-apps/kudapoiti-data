"""Возраст по направлениям (урок 8) у мест робота edu, пятнадцатый запуск: отложенные 1122 — из tools/edu_1124_catages.py (NEW),
новые — из карточек Яндекс Карт (tools/edu_1125_sel.py). python3 tools/edu_1125_catages.py → дописывает auto/cat-ages.json."""
import json, os, sys, io, contextlib, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
with contextlib.redirect_stdout(io.StringIO()):
    import add_edu_1125 as A25
src = open(os.path.join(ROOT, "tools/edu_1124_catages.py")).read()
OLD = eval(re.search(r"NEW = (\{.*?\n\})\n", src, re.S).group(1))
from edu_1125_sel import CATAGES as C25
Y = "Яндекс Карты, карточка организации, услуги: "
p = os.path.join(ROOT, "auto", "cat-ages.json")
data = json.load(open(p))
ids = {r["id"] for r in A25.ROWS}
n = 0
for pid, (ages, txt) in {**OLD, **C25}.items():
    if pid in ids:
        data[pid] = {**ages, "src": Y + txt + "; 13.11.2026"}
        n += 1
json.dump(data, open(p, "w"), ensure_ascii=False, indent=1)
print("cat_ages:", n)
