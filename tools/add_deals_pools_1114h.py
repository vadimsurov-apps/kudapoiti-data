"""Акции робота pools 14.11 (08 UTC): пробные первые занятия новых мест (источник — сайт места в auto/pages).
python3 tools/add_deals_pools_1114h.py <id добавленных мест…>"""
import json, os, sys
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "deals.json")
D = "2026-11-14"


def deal(pid, suf, kind, title, details, url):
    return {"id": pid + "-" + suf, "place_id": pid, "kind": kind, "title": title, "details": details, "code": "", "until": "",
            "url": url, "checked": D}


NEW = [
 deal("glubina-berzarina", "trial", "trial", "Первое занятие — 990 ₽",
      "Детский бассейн «Глубина» в Щукине: первое пробное занятие стоит 990 ₽ вместо 3600 ₽. Индивидуально с тренером, 30 минут, "
      "для детей от 2 месяцев до 7 лет.", "https://glubinaswim.ru/"),
 deal("laguna-boba-borisovsky", "trial", "trial", "Пробное занятие — 1500 ₽",
      "Детский бассейн «Лагуна Боба»: пробное занятие стоит 1500 ₽ вместо 2800 ₽ за разовое. Индивидуально с тренером, 30 минут, "
      "для детей от 3 месяцев до 8 лет.", "https://laguna-boba.ru/"),
]
for pid, pool, age in (("chayka-krylatskoe", "в Крылатском", "4–14 лет"), ("chayka-zorky-krasnogorsk", "в бассейне «Зоркий» в Красногорске", "4–14 лет"),
                       ("chayka-gazoprovod", "в посёлке Газопровод (Коммунарка)", "с 6 лет"), ("chayka-dubrovka", "в ЖК «Дубровка»", "4–14 лет"),
                       ("chayka-avtozavodskaya", "на Автозаводской", "4–14 лет")):
    NEW.append(deal(pid, "trial", "trial", "Пробное занятие — 990 ₽",
                    "Школа спортивного развития «Чайка» %s: пробное занятие синхронным или спортивным плаванием — 990 ₽. Для детей "
                    "%s, умение плавать не обязательно." % (pool, age), "https://chaikaschool.com/"))
if __name__ == "__main__":
    ids = set(sys.argv[1:])
    d = json.load(open(P))
    lst = d["deals"] if isinstance(d, dict) else d
    have = {x["id"] for x in lst}
    add = [x for x in NEW if x["place_id"] in ids and x["id"] not in have]
    lst.extend(add)
    json.dump(d, open(P, "w"), ensure_ascii=False, indent=1)
    print("акций добавлено:", len(add))
