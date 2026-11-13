"""Акции робота pools 13.11 (20 UTC): пробные занятия новых мест (источник — сайт места в auto/pages или прайс-лист карточки
организации в Яндекс Картах).   python3 tools/add_deals_pools_1113x.py <id добавленных мест…>"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import add_deals_pools_1113u as U
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "deals.json")
D = "2026-11-13"
OLD = ("ss1-mei", "akvabulko-reutov", "world-swim-reutov", "akvadarina-reutov")
def fs(pid, pool, ages):
    return {"id": pid + "-trial", "place_id": pid, "kind": "free", "title": "Первое занятие бесплатно",
            "details": "Школа плавания Flowswim, бассейн %s: первое пробное занятие в группе для детей %s бесплатно — 45 минут, "
                       "тренер знакомится с ребёнком и подбирает группу." % (pool, ages),
            "code": "", "until": "", "url": "https://flowswim.ru/", "checked": D}
NEW = [x for x in U.NEW if x["place_id"] in OLD] + [
 fs("flowswim-yauza", "«Яуза»", "от 7 лет"),
 fs("flowswim-balans", "«Баланс»", "от 3 лет"),
 fs("flowswim-severny", "«Северный»", "от 7 лет"),
 {"id": "afalina-dmitrov-trial", "place_id": "afalina-dmitrov", "kind": "free", "title": "Первое пробное занятие бесплатно",
  "details": "Центр плавания «Афалина»: первое пробное занятие бесплатно — можно посмотреть, как ребёнку в воде и с тренером.",
  "code": "", "until": "", "url": "https://afalina-swim.ru/", "checked": D},
 {"id": "akuly-brassa-dmitrov-trial", "place_id": "akuly-brassa-dmitrov", "kind": "trial", "title": "Пробное занятие — 900 ₽",
  "details": "Пробное занятие в детском бассейне «Акулы брасса»: 30 минут с тренером за 900 ₽ — мягкое знакомство с водой "
             "для детей от 2 месяцев до 14 лет.",
  "code": "", "until": "", "url": "https://акулы-брасса.рф/dmitrov", "checked": D},
 {"id": "zolotoy-morzhik-vidnoe-trial", "place_id": "zolotoy-morzhik-vidnoe", "kind": "discount",
  "title": "Пробное занятие за полцены",
  "details": "Скидка 50% на пробное занятие, если купить абонемент в день первого посещения. Детский бассейн для малышей "
             "от рождения до 7 лет.",
  "code": "", "until": "2028-07-31", "url": "https://zolotoj-morzhik-olhovaja-ulitsa.clients.site/", "checked": D},
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
