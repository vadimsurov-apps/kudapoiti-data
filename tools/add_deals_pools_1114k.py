"""Акции робота pools 14.11 (11 UTC): бесплатные пробные занятия новых мест (источник — сайт места в auto/pages).
python3 tools/add_deals_pools_1114k.py <id добавленных мест…>"""
import json, os, sys
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "deals.json")
D = "2026-11-14"


def deal(pid, suf, kind, title, details, url):
    return {"id": pid + "-" + suf, "place_id": pid, "kind": kind, "title": title, "details": details, "code": "", "until": "",
            "url": url, "checked": D}


# id: (бассейн, возраст, адрес страницы)
SS1 = {"ss1-chayka-turchaninov": ("«Чайка»", "с 7 лет", "chaika"), "ss1-meridian": ("«Меридиан»", "с 3 лет", "meridian"),
       "ss1-mgpu": ("МГПУ", "с 3 лет", "mgpu"), "ss1-mgyua": ("МГЮА", "с 7 лет", "mgua"), "ss1-mosgu": ("МосГУ", "с 7 лет", "mosgu"),
       "ss1-nekrasovka": ("Дворца спорта «Некрасовка»", "с 3 лет", "nekrasovka"), "ss1-nika-volzhsky": ("«Ника»", "с 7 лет", "nika"),
       "ss1-profsoyuznaya": ("«Профсоюзная»", "с 3 лет", "profsoyuznaya"), "ss1-soyuz": ("«Союз»", "с 7 лет", "soyuz"),
       "ss1-yantar": ("Дворца спорта «Янтарь»", "с 3 лет", "yantar"), "ss1-stalnoy": ("«Стальной»", "с 7 лет", "stalnoy"),
       "ss1-mgusit": ("МГУСиТ", "с 7 лет", "mgusit"), "ss1-miit": ("МИИТ", "с 7 лет", "miit"),
       "ss1-motsvs": ("Центра водных видов спорта на ул. Ибрагимова", "с 7 лет", "mocvs"),
       "ss1-nadezhda-krupskoy": ("«Надежда»", "с 7 лет", "nadezhda"), "ss1-orekhovo-borisovo": ("«Орехово-Борисово»", "с 7 лет", "orehovo"),
       "ss1-reu-plekhanova": ("РЭУ им. Плеханова", "с 7 лет", "plehanova"), "ss1-ramenki": ("«Раменки»", "с 3 лет", "ramenki"),
       "ss1-rgufk": ("РГУФК", "с 5 лет", "rgufk"), "ss1-khovrino": ("«Ховрино»", "с 7 лет", "hovrino")}
NEW = [deal(pid, "free", "free", "Пробное занятие бесплатно",
            "Школа плавания № 1, бассейн %s: бесплатное пробное занятие для детей %s. Запись — заявкой на сайте или по телефону школы."
            % (pool, age), "https://swim-school-1.ru/basseyni/" + slug) for pid, (pool, age, slug) in SS1.items()]
for pid, where in (("okeanika-tekstilshchiki", "в Текстильщиках (бассейн «Ника»)"), ("okeanika-izmaylovo", "в Измайлове (11-я Парковая ул.)")):
    NEW.append(deal(pid, "free", "free", "Первое занятие бесплатно",
                    "Детская школа плавания «Океаника» %s: первое пробное занятие в группе — бесплатно. Для детей от 2 до 15 лет; "
                    "с собой справка для бассейна." % where, "https://okeanika-swim.com/"))
if __name__ == "__main__":
    ids = set(sys.argv[1:])
    d = json.load(open(P))
    lst = d["deals"] if isinstance(d, dict) else d
    have = {x["id"] for x in lst}
    add = [x for x in NEW if x["place_id"] in ids and x["id"] not in have]
    lst.extend(add)
    json.dump(d, open(P, "w"), ensure_ascii=False, indent=1)
    print("акций добавлено:", len(add))
