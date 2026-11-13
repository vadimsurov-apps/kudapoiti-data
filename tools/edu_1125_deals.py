"""Акции у мест робота edu, пятнадцатый запуск — из карточек организаций Яндекс Карт (пробное/консультация бесплатно).
python3 tools/edu_1125_deals.py → дописывает deals.json (только места, добавленные в таблицу)."""
import json, os, sys, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
with contextlib.redirect_stdout(io.StringIO()):
    import add_edu_1125 as A25
E = A25.A.E
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
D = {
 "yarkie-deti-nagatinskaya": ("trial", E["20:58"]["org"], "Бесплатный пробный урок", "Бесплатный пробный урок в центре «Яркие дети» на Нагатинской набережной — подберут курс по уровню и возрасту ребёнка."),
 "invacon-studeny": ("free", E["25:256"]["org"], "Бесплатная консультация клинического психолога", "В центре «Инвакон» на Студёном проезде — бесплатная консультация клинического психолога для семей детей и подростков с ОВЗ."),
}
p = os.path.join(ROOT, "deals.json")
data = json.load(open(p))
have = {d["id"] for d in data["deals"]}
ids = {r["id"] for r in A25.ROWS}
n = 0
for pid, (kind, url, title, det) in D.items():
    did = f"{pid}-{kind}"
    if pid in ids and did not in have and url:
        data["deals"].append({"id": did, "place_id": pid, "kind": kind, "title": title, "details": det, "code": "", "until": "", "url": url, "checked": "2026-11-13"})
        n += 1
json.dump(data, open(p, "w"), ensure_ascii=False, indent=1)
print("акций:", n)
