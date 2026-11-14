"""Акции робота pools 14.11 (05 UTC): бесплатные и пробные первые занятия новых мест (источник — сайт школы в auto/pages или
прайс-лист карточки организации в Яндекс Картах).   python3 tools/add_deals_pools_1114e.py <id добавленных мест…>"""
import json, os, sys
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "deals.json")
D = "2026-11-14"


def deal(pid, suf, kind, title, details, url):
    return {"id": pid + "-" + suf, "place_id": pid, "kind": kind, "title": title, "details": details, "code": "", "until": "",
            "url": url, "checked": D}


NEW = [deal("ss1-neptun-federativny", "free", "free", "Пробное занятие бесплатно",
            "Школа плавания № 1, бассейн «Нептун»: бесплатное пробное занятие в группе — для детей 3–6 и 7–13 лет. Запись — "
            "заявкой на сайте или по телефону школы.", "https://swim-school-1.ru/basseyni/neptun")]
for pid, pool, age in (("ss1-zhivopisny", "Живописный", "с 7 лет"), ("ss1-kolomensky", "Коломенский", "с 3 лет"),
                       ("ss1-eseninsky", "Есенинский", "с 7 лет"), ("ss1-kachalovsky", "Качаловский", "с 7 лет"),
                       ("ss1-odintsovo-mozhayskoe", "Большой Одинцовский", "с 7 лет")):
    NEW.append(deal(pid, "free", "free", "Пробное занятие бесплатно",
                    "Школа плавания № 1, бассейн «%s»: бесплатное пробное занятие в группе для детей %s. Запись — заявкой на "
                    "сайте или по телефону школы." % (pool, age), "https://swim-school-1.ru/basseyni"))
for pid, pool in (("swimclub-fryazevskaya", "«Олимпия» на Фрязевской улице"), ("swimclub-zemlyanoy-val", "«Университетский» на "
                  "Земляном Валу"), ("swimclub-yunosti", "МосГУ на улице Юности")):
    NEW.append(deal(pid, "free", "free", "Первое занятие в группе бесплатно",
                    "Школа плавания SwimClub, бассейн %s: первое пробное групповое занятие — бесплатно. Для детей от 4 до 18 "
                    "лет, запись по телефону или на сайте школы." % pool, "https://swimclubteam.ru/"))
for pid, pool in (("swimming-moscow-shchorsa", "«Восход» в Солнцеве"), ("swimming-moscow-samory-mashela", "«Гармония» у РУДН"),
                  ("swimming-moscow-koshtoyantsa", "на улице Коштоянца"), ("swimming-moscow-donskogo", "«Качаловский» в Северном "
                  "Бутове"), ("swimming-moscow-ostafyevskaya", "«Максимум» в Южном Бутове"), ("swimming-moscow-vnukovo", "«Пегас» "
                  "во Внукове")):
    NEW.append(deal(pid, "trial", "trial", "Первое занятие в группе — 1000 ₽",
                    "Школа плавания Swimming Moscow, бассейн %s: первое занятие в группе стоит 1000 ₽. Для детей от 5 до 17 лет, "
                    "группу подбирают по возрасту и уровню." % pool, "https://swimmingmoscow.ru/"))
NEW += [
 deal("falko-zarechye", "free", "free", "Пробное занятие бесплатно",
      "Школа плавания Григория Фалько в Заречье: пробное занятие — бесплатно. Группы для детей 4–6 и 6–17 лет, запись на сайте "
      "или по телефону школы.", "https://swimfalko.ru/"),
 deal("flamingo-selyatino", "first", "discount", "Первое занятие со скидкой 50%",
      "Семейный аквацентр «ФламинGo!» в Селятине: первое занятие для ребёнка — за полцены. Плавание для детей от 1,5 месяцев до "
      "10 лет.", "https://flamingocentr.ru/"),
 deal("akvarel-zvenigorod", "trial", "trial", "Пробное занятие — 600 ₽",
      "Школа плавания «Акварель» в Звенигороде: пробное занятие в группе — 600 ₽ вместо 1500 ₽ за разовое. Для детей от 4 до "
      "18 лет.", "https://yandex.ru/maps/org/170751221080/prices/"),
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
