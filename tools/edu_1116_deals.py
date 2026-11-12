"""Акции «пробное бесплатно» у мест робота edu 12.11 (шестой запуск) — из карточек организаций Яндекс Карт (auto/pages *-ev<N>-1116e*).
python3 tools/edu_1116_deals.py → дописывает deals.json (только места, добавленные в таблицу)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_edu_1116 import ROWS
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
D = {
 "baby-club-izmaylovsky-5a": ("trial", "https://yandex.ru/maps/org/baby_club/220569716935/", "Бесплатное пробное занятие", "Пробное развивающее занятие в Бэби-клубе на Измайловском проезде — бесплатно.", None),
 "tesla-robo-izmaylovsky": ("trial", "https://yandex.ru/maps/org/tesla/95688257333/", "Пробное занятие по робототехнике бесплатно", "Бесплатное пробное занятие с группой в клубе юных инженеров «Тесла».", None),
 "klevocode-semeynaya-ramenskoe": ("trial", "https://yandex.ru/maps/org/program_school/64985206291/", "Бесплатное пробное занятие", "Пробное занятие по программированию и робототехнике в «КлёвоКод» — бесплатно.", None),
 "klevocode-severnoe-ramenskoe": ("trial", "https://yandex.ru/maps/org/program_school/237952948831/", "Бесплатное пробное занятие", "Пробное занятие по программированию и робототехнике в «КлёвоКод» — бесплатно.", None),
}
p = os.path.join(ROOT, "deals.json")
data = json.load(open(p))
have = {d["id"] for d in data["deals"]}
ids = {r["id"] for r in ROWS}
n = 0
for pid, (kind, url, title, det, until) in D.items():
    did = f"{pid}-{kind}"
    if pid in ids and did not in have:
        d = {"id": did, "place_id": pid, "kind": kind, "title": title, "details": det, "url": url, "checked": "2026-11-12"}
        if until:
            d["until"] = until
        data["deals"].append(d)
        n += 1
json.dump(data, open(p, "w"), ensure_ascii=False, indent=1)
print("акций:", n)
