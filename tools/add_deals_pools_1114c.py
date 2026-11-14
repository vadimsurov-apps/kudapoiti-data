"""Акции робота pools 14.11 (02 UTC): первые и пробные занятия новых мест (источник — сайт места в auto/pages или прайс-лист
карточки организации в Яндекс Картах).   python3 tools/add_deals_pools_1114c.py <id добавленных мест…>"""
import json, os, sys
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "deals.json")
D = "2026-11-14"
NEW = [
 {"id": "laguna-detstva-voskresenskoe-trial", "place_id": "laguna-detstva-voskresenskoe", "kind": "trial",
  "title": "Пробное занятие — 900 ₽",
  "details": "Детский бассейн «Лагуна детства»: пробное индивидуальное занятие с тренером, 30 минут, — 900 ₽ вместо 2000 ₽ "
             "(45 минут — 1300 ₽). Для детей от 2 месяцев до 7 лет.",
  "code": "", "until": "", "url": "https://lagunadetstva.ru/", "checked": D},
 {"id": "umka-nekrasovka-trial", "place_id": "umka-nekrasovka", "kind": "trial", "title": "Пробное занятие — 500 ₽",
  "details": "Детский бассейн «Умка» в Некрасовке: пробное индивидуальное занятие с инструктором — 500 ₽ вместо 2500 ₽. "
             "Для детей от рождения до 7 лет.",
  "code": "", "until": "", "url": "https://yandex.ru/maps/org/umka/183656016837/prices/", "checked": D},
 {"id": "neptunyata-troitsk-trial", "place_id": "neptunyata-troitsk", "kind": "trial",
  "title": "Пробное занятие — 1200 ₽ при покупке абонемента",
  "details": "Акваклуб «Нептунята» в Троицке: пробное занятие, 30 минут, стоит 1200 ₽ вместо 2800 ₽, если купить абонемент "
             "в день пробного. Для детей от 2 месяцев до 9 лет.",
  "code": "", "until": "", "url": "https://neptunyata.ru/", "checked": D},
 {"id": "akuly-troitsk-letokhova-free", "place_id": "akuly-troitsk-letokhova", "kind": "free",
  "title": "Первое групповое занятие бесплатно",
  "details": "Школа плавания и водного поло «Акулы»: первое групповое занятие — бесплатно, на нём тренер определит уровень "
             "ребёнка и подберёт группу. Нужно оставить заявку на сайте школы. Для детей от 6 до 17 лет.",
  "code": "", "until": "", "url": "https://sharksh2o.ru/", "checked": D},
 {"id": "vremya-pobezhdat-sudostroitelnaya-free", "place_id": "vremya-pobezhdat-sudostroitelnaya", "kind": "free",
  "title": "Пробное занятие бесплатно",
  "details": "Клуб синхронного и спортивного плавания «Время побеждать»: пробное занятие — бесплатно. Запись — через анкету "
             "на сайте клуба. Для детей от 5 лет.",
  "code": "", "until": "", "url": "https://vremyapobezhdat.ru/", "checked": D},
]
if __name__ == "__main__":
    added = set(sys.argv[1:])                   # акции — только для мест, которые добавлены в таблицу
    raw = open(P, encoding="utf-8").read()
    d = json.loads(raw)
    L = d["deals"] if isinstance(d, dict) else d
    have = {x["id"] for x in L}
    add = [x for x in NEW if x["id"] not in have and x["place_id"] in added]
    L.extend(add)
    indent = 1 if raw.startswith("{\n ") or raw.startswith("[\n ") else (2 if "\n  " in raw[:50] else None)
    json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=indent)
    print("добавлено акций:", len(add), [x["id"] for x in add])
