"""Акции «пробное бесплатно» у мест робота edu, тринадцатый запуск — из карточек организаций Яндекс Карт.
python3 tools/edu_1123_deals.py → дописывает deals.json (только места, добавленные в таблицу)."""
import json, os, sys, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
with contextlib.redirect_stdout(io.StringIO()):
    import add_edu_1123 as A23
E = A23.A.E
from edu_1123_sel import DEALS
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
D = {
 "kiberone-nekrasovka": ("trial", E["20:87"]["org"], "Бесплатный пробный урок программирования", "Пробный урок в KIBERone на улице Ухтомского Ополчения (Некрасовка) для детей 6–14 лет — бесплатно."),
 "yarkie-deti-nagatinskaya": ("trial", E["20:58"]["org"], "Бесплатный пробный урок", "Бесплатный пробный урок в центре «Яркие дети» на Нагатинской набережной — подберут курс по уровню и возрасту ребёнка."),
 **DEALS,
}
p = os.path.join(ROOT, "deals.json")
data = json.load(open(p))
have = {d["id"] for d in data["deals"]}
ids = {r["id"] for r in A23.ROWS}
n = 0
for pid, (kind, url, title, det) in D.items():
    did = f"{pid}-{kind}"
    if pid in ids and did not in have and url:
        data["deals"].append({"id": did, "place_id": pid, "kind": kind, "title": title, "details": det, "code": "", "until": "", "url": url, "checked": "2026-11-12"})
        n += 1
json.dump(data, open(p, "w"), ensure_ascii=False, indent=1)
print("акций:", n)
