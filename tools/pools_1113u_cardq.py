"""Робот pools 13.11 (17 UTC), шаг 2: карточки Яндекс Карт новых кандидатов (ключ po<N>=1113u) → auto/fetch-queue.txt,
справка OSM (pl25-*) → auto/osm-queries.json.   python3 tools/pools_1113u_cardq.py"""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
# id: (название в Яндексе, адрес в Яндексе, центр поиска, радиус, улица OSM, имя для сверки)
Q = {
 "akvabulko-reutov": ("Аквабулько", "Реутов, Юбилейный просп., 68", (55.762, 37.866), 2500, "Юбилейный", "Аквабульк"),
 "agidel-reutov": ("Агидель", "Реутов, Юбилейный просп., 59", None, 0, "", ""),
 "vtoroe-rozhdenie-reutov": ("Второе рождение", "Реутов, Лесная ул., 5", (55.757, 37.862), 2500, "Лесная", "рождение"),
 "tf-reutov-yubileyny": ("Школа плавания Территория Фитнеса", "Реутов, Юбилейный просп., 43", None, 0, "", ""),
 "world-swim-reutov": ("World Swim", "Реутов, ул. Г.И. Котовского, 13А", (55.760, 37.858), 2500, "Котовского", "Волна"),
 "akvadarina-reutov": ("АкваДарина", "Реутов, ул. Некрасова, 17", (55.763, 37.853), 2500, "Некрасова", "Дарина"),
 "volna-reutov": ("Волна, спортивный комплекс", "Реутов, ул. Г.И. Котовского, 13А", None, 0, "", ""),
 "krol-zhukovsky": ("Кроль", "Жуковский, ул. Пушкина, 3А", (55.600, 38.115), 3500, "Пушкина", "Метеор"),
 "meteor-zhukovsky": ("Метеор, спортивный комплекс", "Жуковский, ул. Пушкина, 3", None, 0, "", ""),
 "uchinka-pushkino": ("Учинка", "Пушкино, микрорайон Заветы Ильича, Счастливая ул.", (56.045, 37.860), 3500, "Счастливая", "Учинка"),
 "marlin-pushkino": ("Марлин", "Пушкино, Набережная ул., 8", None, 0, "", ""),
 "provodu-dolgoprudny": ("ПроВоду", "Долгопрудный, просп. Ракетостроителей, 5, корп. 1", (55.953, 37.497), 3000, "Ракетостроителей", "ПроВоду"),
 "torpeda-ivanteevka": ("Школа плавания Торпеда", "Ивантеевка, Первомайская ул., 53", None, 0, "", ""),
 "afalina-zamyshlyaeva": ("Афалина", "Сергиев Посад, ул. Замышляева, 1А", (56.325, 38.135), 5000, "Замышляева", "Афалина"),
 "neptun-orekhovo": ("Нептун", "Орехово-Зуево, Торфобрикетная ул., 8", (55.805, 38.975), 5500, "Торфобрикетная", "Нептун"),
 "delfin-noginsk": ("Дельфин", "Ногинск, Юбилейная ул., 32", (55.870, 38.445), 5000, "Юбилейная", "Дельфин"),
 "plyvi-malysh-michurinsky": ("Плыви, малыш", "Москва, Мичуринский просп., 16", (55.700, 37.510), 1500, "Мичуринский", "малыш"),
 "ss1-mei": ("Школа плавания № 1", "Москва, Энергетический пр., 3, стр. 3", (55.757, 37.706), 900, "Энергетический", "бассейн"),
 "ss1-dinamo-leningradskoe": ("Школа плавания № 1", "Москва, Ленинградское ш., 39, стр. 53", (55.840, 37.487), 1300, "Ленинградское", "Динамо"),
 "ss1-luzhniki": ("Школа плавания № 1", "Москва, Лужнецкая наб., 24, стр. 4", None, 0, "", ""),
 "swimrocket-luzhniki": ("SwimRocket", "Москва, Лужнецкая наб., 24", None, 0, "", ""),
 "ss1-burevestnik-plyushchikha": ("Школа плавания № 1, бассейн", "Москва, ул. Плющиха, 57, стр. 1", None, 0, "", ""),
}
EXTRA = ["https://yandex.ru/maps/org/shkola_plavaniya_1/20599930706/prices/",   # Есенинский бул., 9, корп. 2, стр. 1
         "https://yandex.ru/maps/org/shkola_plavaniya_1/34196938705/prices/",   # Живописная ул., 28, стр. 6
         "https://yandex.ru/maps/org/shkola_plavaniya_1/82483225930/prices/",
         "https://yandex.ru/maps/org/shkola_plavaniya_1/25610735350/prices/",   # Островная ул., 1, стр. 1
         "https://swim-school-1.ru/basseyni/kuryanovo", "https://swim-school-1.ru/basseyni/altayskiy",
         "https://swim-school-1.ru/basseyni/burevestnik", "https://swim-school-1.ru/basseyni/eseninskiy",
         "https://swim-school-1.ru/basseyni/dinamo", "https://swim-school-1.ru/basseyni/kachalovskiy",
         "https://swim-school-1.ru/basseyni/krylatskoe", "https://swim-school-1.ru/basseyni/jivopisniy"]
if __name__ == "__main__":
    lines, out = list(EXTRA), []
    for i, (pid, (nm, addr, c, r, st, match)) in enumerate(Q.items()):
        if nm:
            lines.append("https://yandex.ru/maps/1/moscow-and-moscow-oblast/?po%d=1113u&text=%s" % (i, urllib.parse.quote(nm + ", " + addr)))
        if c:
            q = {"id": "pl25-" + pid, "lat": c[0], "lon": c[1], "radius": r, "name": match}
            if st: q["street"] = st
            out.append(q)
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in lines if l not in old]) + "\n")
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("pl25-")]
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(out), len(lines))
