"""Робот pools 12.11 (21 UTC), вторая пачка кандидатов из кэша выдач Яндекс Карт: карточки → auto/fetch-queue.txt
(ключ pn<N>=1112r), запросы OSM pl14-* → auto/osm-queries.json.   python3 tools/pools_1112c_q.py"""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q = {
 "utka-boss-leskova": ("Утка Босс", "Москва, ул. Лескова, 14", (55.895, 37.60), 2500, "Лескова", "Утка"),
 "kapitan-barboss-bitsa": ("Капитан БарBoss", "посёлок Битца, жилой комплекс Южная Битца, Южный бул., 4", (55.545, 37.60), 4000, "Южный", "Бар"),
 "margaritka-peschanaya": ("Маргаритка", "Москва, 2-я Песчаная ул., 4А, стр. 2", (55.795, 37.515), 2000, "Песчаная", "Маргаритка"),
 "morekids-moskovsky": ("Морекидс", "Московский, Солнечная ул., 3А, стр. 1", (55.60, 37.35), 4000, "Солнечная", "Морекидс"),
 "kitenok-opalikha": ("Китенок", "Красногорск, микрорайон Опалиха, ул. Геологов, 4, корп. 2", (55.825, 37.25), 4000, "Геологов", "Китенок"),
 "kva-kva-puziki-pushkino": ("Ква-Ква-Пузики", "Пушкино, Набережная ул., 8", (56.00, 37.87), 4000, "Набережная", "Пузики"),
 "lotos-stavropolskaya": ("Лотос", "Москва, Ставропольская ул., 13", (55.675, 37.76), 3000, "Ставропольская", "Лотос"),
 "plyvi-s-alisoy-goncharnaya": ("Плыви с Алисой", "Москва, Гончарная наб., 9/16с2", (55.743, 37.648), 1500, "Гончарная", "Алис"),
 "plyvi-s-alisoy-stoletova": ("Плыви с Алисой", "Москва, ул. Столетова, 11", (55.705, 37.50), 2500, "Столетова", "Алис"),
 "swimaquarel-teply-stan": ("Swimaquarel", "Москва, ул. Тёплый Стан, 9, корп. 9", (55.625, 37.49), 2500, "Тёплый Стан", "Swim"),
 "silver-swim-filevskaya": ("Silver Swim", "Москва, Большая Филёвская ул., 18", (55.745, 37.50), 2500, "Филёвская", "Silver"),
 "magic-swim-tushinskaya": ("Magic Swim", "Москва, Тушинская ул., 16А", (55.83, 37.445), 2500, "Тушинская", "Magic"),
 "vodny-mir-krylova-bakuninskaya": ("Водный мир Владимира Крылова", "Москва, Бакунинская ул., 13, стр. 1", (55.775, 37.68), 2000, "Бакунинская", "Крылова"),
 "aqville-miklukho-maklaya": ("Aqville", "Москва, ул. Миклухо-Маклая, 16/10к19", (55.65, 37.50), 2500, "Миклухо-Маклая", "Aqville"),
 "plyvi-v-potoke-arsyukova": ("Плыви в потоке", "Москва, ул. Арсюкова, 11", (55.94, 37.545), 4000, "Арсюкова", "потоке"),
 "shpp-plyushchikha": ("Школа персонального плавания", "Москва, ул. Плющиха, 57, стр. 1", (55.737, 37.573), 1500, "Плющиха", "плавания"),
 "akvapups-zil": ("Аквапупс", "Москва, бул. Братьев Весниных, 2", (55.70, 37.64), 2500, "Весниных", "Аквапупс"),
 "akvaklub-more-kommunarka": ("Акваклуб Море", "Москва, Коммунарка, Скандинавский бульвар, 2, корп. 8", (55.565, 37.48), 5000, "Скандинавский", "Море"),
 "neptunyata-troitsk": ("Нептунята", "Троицк, ул. Академика Черенкова, 17", (55.485, 37.305), 5000, "Черенкова", "Нептунята"),
}
if __name__ == "__main__":
    lines, out = [], []
    for i, (pid, (nm, addr, c, r, st, match)) in enumerate(Q.items()):
        lines.append("https://yandex.ru/maps/1/moscow-and-moscow-oblast/?pn%d=1112r&text=%s" % (i, urllib.parse.quote(nm + ", " + addr)))
        out.append({"id": "pl14-" + pid, "lat": c[0], "lon": c[1], "radius": r, "name": match, "street": st})
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in lines if l not in old]) + "\n")
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("pl14-")]
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(out))
