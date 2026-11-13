"""Акции робота pools 13.11 (17 UTC): пробные занятия новых мест (источник — сайт места в auto/pages или прайс-лист карточки
организации в Яндекс Картах).   python3 tools/add_deals_pools_1113u.py"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import add_deals_pools_1113n as N
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "deals.json")
PT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pools_1113u_points.json")
D = "2026-11-13"
SS1 = "https://swim-school-1.ru/basseyni/"
def ss1(pid, slug, pool, ages):
    return {"id": pid + "-trial", "place_id": pid, "kind": "free", "title": "Пробное занятие бесплатно",
            "details": "Школа плавания № 1, %s: бесплатное пробное занятие в группе для детей %s — запись на сайте или по "
                       "телефону школы." % (pool, ages), "code": "", "until": "", "url": SS1 + slug, "checked": D}
NEW = [x for x in N.NEW if x["place_id"] == "akvazavrik-odintsovo"] + [
 ss1("ss1-altaysky", "altayskiy", "бассейн «Алтайский»", "7–13 лет"),
 ss1("ss1-luzhniki", "lujniki", "аквакомплекс «Лужники»", "7–13 лет"),
 ss1("ss1-mei", "mei", "бассейн МЭИ", "7–16 лет"),
 ss1("ss1-dinamo-leningradskoe", "dinamo", "бассейн «Динамо»", "7–12 лет"),
 {"id": "akvabulko-reutov-trial", "place_id": "akvabulko-reutov", "kind": "free", "title": "Пробное занятие бесплатно",
  "details": "Бесплатное пробное занятие в акваклубе «Аквабулько», 30 минут: грудничковое плавание для малышей до 2 лет, "
             "«мама + малыш» или индивидуально с инструктором для детей до 8 лет.",
  "code": "", "until": "", "url": "https://yandex.ru/maps/org/akvabulco/71698625818/prices/", "checked": D},
 {"id": "world-swim-reutov-trial", "place_id": "world-swim-reutov", "kind": "free", "title": "Первое пробное занятие бесплатно",
  "details": "Школа плавания World Swim: первое пробное занятие бесплатно, учат детей с 4 лет — запись на сайте школы.",
  "code": "", "until": "", "url": "https://worldswim.ru/", "checked": D},
 {"id": "akvadarina-reutov-trial", "place_id": "akvadarina-reutov", "kind": "trial", "title": "Пробное занятие — 900 ₽",
  "details": "Пробное занятие по плаванию для детей от 2 месяцев до 12 лет: 30 минут с тренером за 900 ₽ вместо 2700 ₽.",
  "code": "", "until": "", "url": "https://yandex.ru/maps/org/aquadarina/156456989848/prices/", "checked": D},
 {"id": "akvadarina-reutov-gift", "place_id": "akvadarina-reutov", "kind": "promo", "title": "Пробное занятие в подарок",
  "details": "Пробное занятие в подарок, если купить абонемент в день пробного занятия.",
  "code": "", "until": "2026-11-15", "url": "https://aqua-darina.clients.site/", "checked": D},
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
