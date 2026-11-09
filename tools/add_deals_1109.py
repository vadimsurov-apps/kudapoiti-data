"""Робот акций 09.11 ночь (тема 0: батуты и игровые центры). Источники — кэш auto/pages.
Запуск: python3 tools/add_deals_1109.py"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
F = os.path.join(ROOT, "deals.json")
TODAY = "2026-11-09"
d = json.load(open(F)); L = d["deals"]
before = len(L)
L[:] = [x for x in L if not (x.get("until") and x["until"] < TODAY)]
removed = before - len(L)
by = {x["id"]: x for x in L}

# перепроверено по кэшу (страница подтверждает)
for i in ["moreon-bday", "nebo-bagrationovsky-bday", "nebo-sevastopolsky-bday", "nebo-lyublino-bday",
          "panda-meshchersky-bday", "panda-fili-bday", "climb-lab-trial", "exitgames-two", "hippo-land-discount",
          "kidway-rodionovskaya-trial", "kidway-rodionovskaya-family", "maket-autumn", "fiji-kids-trial", "akhilles-promo"]:
    by[i]["checked"] = TODAY
e = by["exitgames-bday"]
e.update(title="Имениннику −15% на квест в будни",
         details="Скидка 15% имениннику и его команде на квест «План побега» и фиджитал-аркады в будние дни, "
                 "за неделю до и неделю после дня рождения. Не суммируется с другими скидками.",
         url="https://exitgames.ru/news", checked=TODAY)
recheck = 15

NEW = [
    dict(id="panda-meshchersky-mnogodet", place_id="panda-meshchersky", kind="discount",
         title="Многодетным — маршрут в подарок каждому ребёнку",
         details="По удостоверению многодетной семьи: при покупке билета каждый ребёнок получает ещё один маршрут в тот же день. Не суммируется с другими акциями.",
         code="", url="https://pandapark.org/mnogodetnym/", checked=TODAY),
    dict(id="panda-fili-mnogodet", place_id="panda-fili", kind="discount",
         title="Многодетным — маршрут в подарок каждому ребёнку",
         details="По удостоверению многодетной семьи: при покупке билета каждый ребёнок получает ещё один маршрут в тот же день. Не суммируется с другими акциями.",
         code="", url="https://pandapark.org/mnogodetnym/", checked=TODAY),
    dict(id="pyat-zvezd-novokuz-kids150", place_id="cin-pyat-zvezd", kind="discount",
         title="Детям и многодетным — билет 150 ₽ утром пн–ср",
         details="По удостоверению в кассе: в понедельник, вторник и среду до 12:00 билет 150 ₽ (детский — до 11 лет на фильмы 0+ и 6+; многодетным — от трёх членов семьи, включая родителя). В праздники не действует.",
         code="", url="https://5zvezd.ru/article/sistema-skidok-dla-moskovskih-kinoteatrov", checked=TODAY),
    dict(id="pyat-zvezd-novokuz-under4", place_id="cin-pyat-zvezd", kind="free",
         title="Детям до 4 лет — без билета на фильмы 0+",
         details="Малыш до 4 лет включительно смотрит фильм 0+ бесплатно, если сидит на кресле с родителем.",
         code="", url="https://5zvezd.ru/article/sistema-skidok-dla-moskovskih-kinoteatrov", checked=TODAY),
    dict(id="pyat-zvezd-pavel-under4", place_id="cin-5zvezd-paveletskaya", kind="free",
         title="Детям до 4 лет — без билета на фильмы 0+",
         details="Малыш до 4 лет включительно смотрит фильм 0+ бесплатно, если сидит на кресле с родителем.",
         code="", url="https://5zvezd.ru/article/sistema-skidok-dla-moskovskih-kinoteatrov", checked=TODAY),
    dict(id="soyuzmultpark-bday", place_id="soyuzmultpark", kind="birthday",
         title="Имениннику −20% на билет",
         details="В день рождения по подтверждающему документу на ресепшен парка. Акции и скидки не суммируются.",
         code="", url="https://souzmultpark.ru/", checked=TODAY),
    dict(id="soyuzmultpark-mnogodet", place_id="soyuzmultpark", kind="discount",
         title="Многодетным −20%",
         details="Билет покупается на кассе медиацентра по удостоверению многодетной семьи. Не суммируется с другими скидками.",
         code="", url="https://souzmultpark.ru/", checked=TODAY),
    dict(id="soyuzmultpark-under3", place_id="soyuzmultpark", kind="free",
         title="Детям до 3 лет — бесплатно",
         details="Бесплатный билет для детей от 0 до 3 лет по подтверждающему документу. Коляски оставляют в специальном месте.",
         code="", url="https://souzmultpark.ru/", checked=TODAY),
]
ids = {x["id"] for x in L}
added = 0
for n in NEW:
    if n["id"] not in ids:
        L.append(n); added += 1
d["version"] = TODAY
json.dump(d, open(F, "w"), ensure_ascii=False, indent=1)
print("снято", removed, "добавлено", added, "перепроверено", recheck)
