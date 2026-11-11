"""Акции «пробное бесплатно» у мест робота edu 11.11 (четвёртый запуск) — из карточек организаций Яндекс Карт (auto/pages *-ev<N>-1114e*).
python3 tools/edu_1114_deals.py → дописывает deals.json (только места, добавленные в таблицу)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_edu_1114 import ROWS
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
D = {
 "kiberone-ogorodny-17": ("trial", "https://yandex.ru/maps/org/kiberone/153049260119/", "Пробный IT-урок бесплатно", "Бесплатный пробный урок программирования для детей 6–14 лет.", None),
 "baby-club-krupskoy-1": ("trial", "https://yandex.ru/maps/org/baby_club/1331337368/", "Первое занятие бесплатно", "Первое развивающее занятие в Бэби-клубе — бесплатно, для детей от 8 месяцев до 7 лет.", None),
 "iq007-dolgoprudny": ("trial", "https://yandex.ru/maps/org/iq007/172181664256/", "Бесплатное пробное занятие", "Пробное занятие бесплатно: чтение, ментальная арифметика, подготовка к школе.", None),
 "kubik-shturvalnaya": ("free", "https://yandex.ru/maps/org/kubik/118447593143/", "Два бесплатных занятия в ноябре", "В ноябре — два бесплатных занятия в детском центре «Кубик».", "2026-11-30"),
}
p = os.path.join(ROOT, "deals.json")
data = json.load(open(p))
have = {d["id"] for d in data["deals"]}
ids = {r["id"] for r in ROWS}
n = 0
for pid, (kind, url, title, det, until) in D.items():
    did = f"{pid}-{kind}"
    if pid in ids and did not in have:
        d = {"id": did, "place_id": pid, "kind": kind, "title": title, "details": det, "url": url, "checked": "2026-11-11"}
        if until:
            d["until"] = until
        data["deals"].append(d)
        n += 1
json.dump(data, open(p, "w"), ensure_ascii=False, indent=1)
print("акций:", n)
