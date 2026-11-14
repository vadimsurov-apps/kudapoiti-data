"""Акции робота pools 13.11 (23 UTC): первые и пробные занятия новых мест (источник — сайт места в auto/pages или прайс-лист
карточки организации в Яндекс Картах).   python3 tools/add_deals_pools_1113z.py <id добавленных мест…>"""
import json, os, sys
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "deals.json")
D = "2026-11-13"
NEW = [
 {"id": "vshp-ostrovnaya-trial", "place_id": "vshp-ostrovnaya", "kind": "free", "title": "Первая тренировка бесплатно",
  "details": "Высшая школа плавания в Крылатском: первая тренировка бесплатно — для детей и взрослых, в группе или "
             "индивидуально. Нужно оставить заявку на сайте школы.",
  "code": "", "until": "", "url": "https://vshp-swim-school.ru/", "checked": D},
 {"id": "gorod-voln-ochakovo-first", "place_id": "gorod-voln-ochakovo", "kind": "discount",
  "title": "Первое занятие со скидкой 50%",
  "details": "Детский бассейн «Город волн»: первое индивидуальное занятие для новых гостей — за полцены, без покупки "
             "абонемента. Для детей от рождения до 14 лет.",
  "code": "", "until": "", "url": "https://gorodvoln.ru/", "checked": D},
 {"id": "barabulka-dzerzhinsky-trial", "place_id": "barabulka-dzerzhinsky", "kind": "trial",
  "title": "Первое занятие — 900 ₽",
  "details": "Детский бассейн «БараБулька»: первое индивидуальное занятие с инструктором, 30 минут, для новичков — 900 ₽ "
             "вместо 2200 ₽. Для детей от 2 месяцев до 8 лет.",
  "code": "", "until": "", "url": "https://barabulka.com/", "checked": D},
 {"id": "mini-swimmer-oktyabrsky-trial", "place_id": "mini-swimmer-oktyabrsky", "kind": "trial",
  "title": "Пробное занятие в подарок при покупке абонемента",
  "details": "Детский центр плавания Mini Swimmer: если купить абонемент в день пробного занятия, само пробное — в подарок. "
             "Для детей от 2 месяцев до 7 лет.",
  "code": "", "until": "", "url": "https://miniswimmer.com/", "checked": D},
 {"id": "ustinov-zorky-krasnogorsk-trial", "place_id": "ustinov-zorky-krasnogorsk", "kind": "trial",
  "title": "Пробное занятие — 1000 ₽",
  "details": "Школа плавания Евгения Устинова в бассейне «Зоркий»: пробное занятие в мини-группе, 45 минут, — 1000 ₽. "
             "Для детей от 6 до 17 лет.",
  "code": "", "until": "", "url": "https://ustinovswim.pro/dates/", "checked": D},
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
