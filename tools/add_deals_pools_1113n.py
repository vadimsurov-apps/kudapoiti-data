"""Акции робота pools 13.11 (15 UTC): пробные занятия новых мест (источник — сайт места в auto/pages или прайс-лист карточки
организации в Яндекс Картах).   python3 tools/add_deals_pools_1113n.py"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import add_deals_pools_1113k as K
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "deals.json")
PT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pools_1113n_points.json")
D = "2026-11-13"
YA = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?text=%D0%90%D0%BA%D0%B2%D0%B0%D0%B7%D0%B0%D0%B2%D1%80%D0%B8%D0%BA%2C%20%D0%9E%D0%B4%D0%B8%D0%BD%D1%86%D0%BE%D0%B2%D0%BE%2C%20%D0%B1%D1%83%D0%BB.%20%D0%9C%D0%B0%D1%80%D1%88%D0%B0%D0%BB%D0%B0%20%D0%9A%D1%80%D1%8B%D0%BB%D0%BE%D0%B2%D0%B0%2C%2025%D0%90"
NEW = [x for x in K.NEW if x["place_id"] == "rannee-plavanie-khimki-yunnatov"] + [
 {"id": "ss1-korall-krasnoselsky-trial", "place_id": "ss1-korall-krasnoselsky", "kind": "free", "title": "Пробное занятие бесплатно",
  "details": "Школа плавания № 1 в бассейне «Коралл»: бесплатное пробное занятие в группе для детей 3–6 или 7–12 лет — запись на сайте или по телефону школы.",
  "code": "", "until": "", "url": "https://swim-school-1.ru/basseyni/korall", "checked": D},
 {"id": "ss1-zorky-krasnogorsk-trial", "place_id": "ss1-zorky-krasnogorsk", "kind": "free", "title": "Пробное занятие бесплатно",
  "details": "Школа плавания № 1 в бассейне «Зоркий»: бесплатное пробное занятие в группе — запись на сайте или по телефону школы.",
  "code": "", "until": "", "url": "https://swim-school-1.ru/basseyni/zorkiy", "checked": D},
 {"id": "krabibu-ramenskoe-trial", "place_id": "krabibu-ramenskoe", "kind": "trial", "title": "Первое пробное занятие — 900 ₽",
  "details": "Первое индивидуальное занятие плаванием в аква-клубе «Крабибу» — 900 ₽ вместо 1850 ₽. Нужны справка от педиатра и анализы.",
  "code": "", "until": "", "url": "https://krabyboo.ru/", "checked": D},
 {"id": "akvazavrik-odintsovo-trial", "place_id": "akvazavrik-odintsovo", "kind": "trial", "title": "Пробное занятие — 1000 ₽",
  "details": "Пробное индивидуальное занятие с инструктором, 30 минут — 1000 ₽ вместо 2700 ₽; родитель в воду не заходит.",
  "code": "", "until": "", "url": YA, "checked": D},
 {"id": "akvazavrik-odintsovo-friend", "place_id": "akvazavrik-odintsovo", "kind": "promo", "title": "Приведи друга — занятие в подарок",
  "details": "Акция «Приводи друга»: приведите друга в «Аквазаврик» и получите одно занятие в подарок.",
  "code": "", "until": "2027-01-01", "url": "https://akvazavrik.clients.site/", "checked": D},
]
if __name__ == "__main__":
    added = set(json.load(open(PT)))            # акции — только для мест, которые добавлены в таблицу
    raw = open(P, encoding="utf-8").read()
    d = json.loads(raw)
    L = d["deals"] if isinstance(d, dict) else d
    have = {x["id"] for x in L}
    add = [x for x in NEW if x["id"] not in have and x["place_id"] in added]
    L.extend(add)
    indent = 1 if raw.startswith("{\n ") or raw.startswith("[\n ") else (2 if "\n  " in raw[:50] else None)
    json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=indent)
    print("добавлено акций:", len(add))
