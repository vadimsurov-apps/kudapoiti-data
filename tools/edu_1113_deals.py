"""Акции «пробное бесплатно» у мест робота edu 11.11 (третий запуск) — из карточек организаций Яндекс Карт.
python3 tools/edu_1113_deals.py → дописывает deals.json (только места, добавленные в таблицу)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_edu_1113 import ROWS
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
D = {
 "tesla-snezhnaya": ("https://yandex.ru/maps/org/klub_yunykh_inzhenerov_tesla/216796314300/", "Первое занятие по робототехнике бесплатно", "Бесплатное пробное занятие с группой: юные инженеры собирают свои первые электронные схемы."),
 "tesla-odintsovo-makovskogo": ("https://yandex.ru/maps/org/the_tesla_young_engineers_club/76587154080/", "Первое занятие по робототехнике бесплатно", "Бесплатное пробное занятие с группой: юные инженеры собирают свои первые электронные схемы."),
 "abc-myachkovsky": ("https://yandex.ru/maps/org/tsentr_yazykov_abc/119851416169/", "Пробное занятие бесплатно", "Бесплатное пробное занятие английским в мини-группе для детей 3–6 и 7–12 лет."),
 "ils-odintsovo-severnaya": ("https://yandex.ru/maps/org/ils/159778666527/", "Бесплатный пробный урок", "Бесплатный урок иностранного языка в школе ILS — для детей и подростков."),
 "ils-odintsovo-nedelina": ("https://yandex.ru/maps/org/ils/59365718422/", "Бесплатный пробный урок", "Бесплатный урок иностранного языка в школе ILS — для детей и подростков."),
 "ils-odintsovo-novosportivnaya": ("https://yandex.ru/maps/org/ils/1071183549/", "Бесплатный пробный урок", "Бесплатный урок иностранного языка в школе ILS — для детей и подростков."),
 "ils-odintsovo-mozhayskoe": ("https://yandex.ru/maps/org/ils/1737214476/", "Бесплатный пробный урок", "Бесплатный урок иностранного языка в школе ILS — для детей и подростков."),
}
p = os.path.join(ROOT, "deals.json")
data = json.load(open(p))
have = {d["id"] for d in data["deals"]}
ids = {r["id"] for r in ROWS}
n = 0
for pid, (url, title, det) in D.items():
    did = f"{pid}-trial"
    if pid in ids and did not in have:
        data["deals"].append({"id": did, "place_id": pid, "kind": "trial", "title": title, "details": det, "url": url, "checked": "2026-11-11"})
        n += 1
json.dump(data, open(p, "w"), ensure_ascii=False, indent=1)
print("акций:", n)
