"""Акции робота pools 14.11 (17 UTC): бесплатные пробные занятия новых мест (источник — сайт места в auto/pages / карточка Яндекс Карт).
python3 tools/add_deals_pools_1114s.py <id добавленных мест…>"""
import json, os, sys
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "deals.json")
D = "2026-11-14"


def deal(pid, suf, kind, title, details, url):
    return {"id": pid + "-" + suf, "place_id": pid, "kind": kind, "title": title, "details": details, "code": "", "until": "",
            "url": url, "checked": D}


NEW = [
 deal("ss1-kuryanovo", "free", "free", "Пробное занятие бесплатно",
      "Школа плавания № 1, бассейн «Курьяново» (1-й Курьяновский пр-д, 17, стр. 1): бесплатное пробное занятие для детей 7–13 лет. "
      "Запись — заявкой на сайте или по телефону школы.", "https://swim-school-1.ru/basseyni/kuryanovo"),
]
if __name__ == "__main__":
    ids = set(sys.argv[1:])
    d = json.load(open(P))
    lst = d["deals"] if isinstance(d, dict) else d
    have = {x["id"] for x in lst}
    add = [x for x in NEW if x["place_id"] in ids and x["id"] not in have]
    lst.extend(add)
    json.dump(d, open(P, "w"), ensure_ascii=False, indent=1)
    print("акций добавлено:", len(add))
