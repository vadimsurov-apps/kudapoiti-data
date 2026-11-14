"""Акции у мест робота edu, двадцать второй запуск — из карточек организаций Яндекс Карт (пробное/приём бесплатно).
python3 tools/edu_1131_deals.py → дописывает deals.json (только места, добавленные в таблицу)."""
import json, os, sys, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
with contextlib.redirect_stdout(io.StringIO()):
    import add_edu_1132 as A26
from edu_1132_sel import DEALS, SEL
E = A26.A.E
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
p = os.path.join(ROOT, "deals.json")
data = json.load(open(p))
have = {d["id"] for d in data["deals"]}
ids = {r["id"] for r in A26.ROWS}
n = 0
for pid, (kind, title, det) in DEALS.items():
    did = f"{pid}-{kind}"
    url = E[SEL[pid][0]].get("org")
    if pid in ids and did not in have and url:
        data["deals"].append({"id": did, "place_id": pid, "kind": kind, "title": title, "details": det, "code": "", "until": "", "url": url, "checked": "2026-11-14"})
        n += 1
json.dump(data, open(p, "w"), ensure_ascii=False, indent=1)
print("акций:", n)
