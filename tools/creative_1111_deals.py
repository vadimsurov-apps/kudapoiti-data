"""Акции «пробное бесплатно» для новых мест робота creative (11.11) — из карточек Яндекс Карт (раздел «Товары и услуги»)."""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PTS = json.load(open(os.path.join(ROOT, "tools", "creative_1111_points.json")))
NEW = [
    ("free-voice-lab-olminskogo", "Бесплатное пробное занятие по вокалу и в хоре",
     "Пробное занятие по вокалу и пробное занятие в хоре с прослушиванием — бесплатно.",
     "https://yandex.ru/maps/org/free_voice_lab/93410916907/prices/"),
    ("invibe-vnukovo", "Первое занятие — бесплатно",
     "Первое занятие в детских группах школы танцев — бесплатно.",
     "https://yandex.ru/maps/org/invibe/160599160176/prices/"),
    ("paint-school-vnukovo", "Бесплатный пробный урок рисования",
     "Пробный урок в группе — бесплатно: первый рисунок по правилам техник рисования.",
     "https://yandex.ru/maps/org/studiya_risovaniya/183517072408/prices/"),
]
p = os.path.join(ROOT, "deals.json")
d = json.load(open(p))
have = {x["id"] for x in d["deals"]}
n = 0
for pid, title, det, url in NEW:
    did = pid + "-trial"
    if pid not in PTS or did in have:
        continue
    d["deals"].append({"id": did, "place_id": pid, "kind": "trial", "title": title, "details": det, "url": url,
                       "checked": "2026-11-11"})
    n += 1
json.dump(d, open(p, "w"), ensure_ascii=False, indent=1)
print("акций:", n)
