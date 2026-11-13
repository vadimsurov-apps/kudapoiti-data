"""Акции робота pools 13.11 (11 UTC): пробные занятия новых мест (источник — сайт места в auto/pages или прайс-лист карточки
организации в Яндекс Картах).   python3 tools/add_deals_pools_1113k.py"""
import json, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "deals.json")
PT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pools_1113k_points.json")
D = "2026-11-13"
NEW = [
 {"id": "rannee-plavanie-khimki-yunnatov-trial", "place_id": "rannee-plavanie-khimki-yunnatov", "kind": "trial",
  "title": "Первое занятие — со скидкой 50 %",
  "details": "Первое (пробное) занятие в «Школе раннего плавания» — со скидкой 50 %: знакомство с бассейном и тренером, подбор группы по возрасту.",
  "code": "", "until": "", "url": "https://swim-baby.ru/", "checked": D},
 {"id": "akvakids-korolev-lesnaya-trial", "place_id": "akvakids-korolev-lesnaya", "kind": "trial",
  "title": "Пробное занятие — 1100 ₽ вместо 2200 ₽",
  "details": "Пробное индивидуальное занятие со скидкой 50 %; при покупке абонемента в день пробного — ещё скидка 10 % на абонемент.",
  "code": "", "until": "", "url": "https://aquakidskorolev.ru/", "checked": D},
 {"id": "malenkiy-plovets-mytishchi-trial", "place_id": "malenkiy-plovets-mytishchi", "kind": "trial",
  "title": "Пробное занятие — 1000 ₽",
  "details": "Пробное индивидуальное занятие с тренером по грудничковому и детскому плаванию, 30 минут — 1000 ₽ вместо 2400 ₽.",
  "code": "", "until": "", "url": "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?text=%D0%9C%D0%B0%D0%BB%D0%B5%D0%BD%D1%8C%D0%BA%D0%B8%D0%B9%20%D0%BF%D0%BB%D0%BE%D0%B2%D0%B5%D1%86%2C%20%D0%9C%D1%8B%D1%82%D0%B8%D1%89%D0%B8%2C%20%D1%83%D0%BB.%20%D0%9A%D0%BE%D0%BB%D0%BF%D0%B0%D0%BA%D0%BE%D0%B2%D0%B0%2C%2024", "checked": D},
 {"id": "more-detyam-mytishchi-trial", "place_id": "more-detyam-mytishchi", "kind": "trial",
  "title": "Первое пробное занятие — 1000 ₽",
  "details": "Первое пробное занятие 45 минут для детей 0–8 лет — 1000 ₽ вместо 2500 ₽, один раз.",
  "code": "", "until": "", "url": "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?text=%D0%9C%D0%BE%D1%80%D0%B5%20%D0%B4%D0%B5%D1%82%D1%8F%D0%BC%2C%20%D0%9C%D1%8B%D1%82%D0%B8%D1%89%D0%B8%2C%20%D1%83%D0%BB.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B5%D0%B4%D1%87%D0%B8%D0%BA%D0%B0%20%D0%90%D0%B1%D0%B5%D0%BB%D1%8F%2C%203%D0%90", "checked": D},
 {"id": "morskie-zvezdy-kommunarka-trial", "place_id": "morskie-zvezdy-kommunarka", "kind": "trial",
  "title": "Пробное занятие — 1000 ₽",
  "details": "Первое пробное занятие плаванием, индивидуально с тренером, — 1000 ₽.",
  "code": "", "until": "", "url": "https://xn----7sbbabz2ajbsaiel8afa8b.xn--p1ai/", "checked": D},
 {"id": "ss1-kashirskoe-65-trial", "place_id": "ss1-kashirskoe-65", "kind": "free", "title": "Пробное занятие бесплатно",
  "details": "Школа плавания № 1: бесплатное пробное занятие в группе — запись на сайте или по телефону школы.",
  "code": "", "until": "", "url": "https://swim-school-1.ru/basseyni", "checked": D},
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
