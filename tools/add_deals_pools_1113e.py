"""Акции робота pools 13.11 (05 UTC): пробные занятия новых бассейнов (источник — сайт места в auto/pages).
python3 tools/add_deals_pools_1113e.py"""
import json, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "deals.json")
NEW = [
 {"id": "octoskills-starovolynskaya-first55", "place_id": "octoskills-starovolynskaya", "kind": "trial",
  "title": "Первое занятие −55%", "details": "Новым клиентам — скидка 55% на первое занятие плаванием в аквастудии.",
  "code": "", "until": "", "url": "https://octoskills.ru/", "checked": "2026-11-13"},
 {"id": "akulyata-krasnogorsk-first", "place_id": "akulyata-krasnogorsk", "kind": "trial",
  "title": "Первое занятие — 1000 ₽",
  "details": "Первая индивидуальная тренировка 30 минут — 1000 ₽ вместо 2790 ₽. Если купить абонемент в день первого занятия — скидка 10%.",
  "code": "", "until": "", "url": "https://aculata.com/", "checked": "2026-11-13"},
 {"id": "mighty-sharks-mitino-trial", "place_id": "mighty-sharks-mitino", "kind": "free",
  "title": "Пробное занятие бесплатно", "details": "Школа плавания приглашает на бесплатное пробное занятие — запись на сайте или по телефону филиала.",
  "code": "", "until": "", "url": "https://mightysharks.ru/", "checked": "2026-11-13"},
 {"id": "mighty-sharks-novogorsk-trial", "place_id": "mighty-sharks-novogorsk", "kind": "free",
  "title": "Пробное занятие бесплатно", "details": "Школа плавания приглашает на бесплатное пробное занятие — запись на сайте или по телефону филиала.",
  "code": "", "until": "", "url": "https://mightysharks.ru/", "checked": "2026-11-13"},
]
if __name__ == "__main__":
    raw = open(P, encoding="utf-8").read()
    d = json.loads(raw)
    L = d["deals"] if isinstance(d, dict) else d
    have = {x["id"] for x in L}
    add = [x for x in NEW if x["id"] not in have]
    L.extend(add)
    indent = 1 if raw.startswith("{\n ") or raw.startswith("[\n ") else (2 if "\n  " in raw[:50] else None)
    json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=indent)
    print("добавлено акций:", len(add))
