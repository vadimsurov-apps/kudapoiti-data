"""Акции робота pools 13.11 (08 UTC): пробные занятия новых мест (источник — страница филиала на сайте школы в auto/pages
или прайс-лист карточки организации).   python3 tools/add_deals_pools_1113h.py"""
import json, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "deals.json")
SS1 = {"lihobory": "lihobory", "fili-dvs": "fili", "mgsu": "mgsu", "bauman": "mgtu-baumana", "serebryany": "serebryanniy",
       "fitnes-praktika": "fitnespraktika", "odintsovo": "odincovo", "zhavoronki": "javoronki"}
NEW = [{"id": f"ss1-{k}-trial", "place_id": f"ss1-{k}", "kind": "free", "title": "Пробное занятие бесплатно",
        "details": "Школа плавания № 1: бесплатное пробное занятие в группе — запись на сайте или по телефону школы.",
        "code": "", "until": "", "url": f"https://swim-school-1.ru/basseyni/{v}", "checked": "2026-11-13"} for k, v in SS1.items()]
NEW += [
 {"id": "mama-ya-plyvu-nagatinskaya-trial", "place_id": "mama-ya-plyvu-nagatinskaya", "kind": "trial",
  "title": "Пробное занятие — 990 ₽", "details": "Первое пробное занятие плаванием с тренером, 30 минут — 990 ₽ вместо 3600 ₽.",
  "code": "", "until": "", "url": "https://mamayaplyvu.com/", "checked": "2026-11-13"},
 {"id": "strong-swim-kosinskaya-trial", "place_id": "strong-swim-kosinskaya", "kind": "free",
  "title": "Пробное занятие бесплатно", "details": "Бесплатное пробное занятие в детской группе — запись по телефону школы.",
  "code": "", "until": "", "url": "https://yandex.ru/maps/org/strong_swim/189947356153/prices/", "checked": "2026-11-13"},
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
