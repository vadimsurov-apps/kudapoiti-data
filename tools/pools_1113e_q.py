"""Робот pools 13.11 (05 UTC): кандидаты из кэша выдач Яндекс Карт (ключи pz*=1113c, районы Водный стадион … Давыдково):
карточки → auto/fetch-queue.txt (ключ po<N>=1113e), запросы OSM pl18-* → auto/osm-queries.json; выдачи по новым районам
(ключ pz<N>=1113e, Деловой центр … Измайлово).   python3 tools/pools_1113e_q.py"""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
# id: (название в Яндексе, адрес в Яндексе, центр поиска, радиус, улица OSM, имя для сверки)
Q = {
 "plyvi-malysh-michurinsky": ("Плыви, малыш", "Москва, Мичуринский просп., 16", (55.7005, 37.5075), 700, "Мичуринский", "малыш"),
 "octoskills-starovolynskaya": ("OctoSkills", "Москва, Староволынская ул., 15, корп. 1", (55.7135, 37.468), 900, "Староволынская", "Octo"),
 "akulyata-krasnogorsk": ("Акулята", "Красногорск, Красногорский бул., 3А", (55.8185, 37.378), 1500, "Красногорский", "Акулят"),
 "pyat-utyat-mozhayskoe": ("Пять утят", "Москва, Можайское ш., 18, корп. 1", (55.7178, 37.4185), 900, "Можайское", "утят"),
 "mighty-sharks-mitino": ("Mighty Sharks", "Москва, Митинская ул., 24А, стр. 1", (55.845, 37.362), 1000, "Митинская", "Sharks"),
 "swimrocket-guu": ("SwimRocket", "Москва, Рязанский просп., 99, корп. 3", (55.7153, 37.8125), 500, "Рязанский", "бассейн"),
 "swimrocket-luzhniki": ("SwimRocket", "Москва, Лужнецкая наб., 24", (55.7115, 37.556), 900, "Лужнецкая", "бассейн"),
 "ssh1-luzhniki-24s4": ("Школа плавания № 1", "Москва, Лужнецкая наб., 24, стр. 4", (55.7115, 37.556), 900, "Лужнецкая", "плавани"),
 "ssh1-novoluzhnetsky": ("Школа плавания № 1", "Москва, Новолужнецкий пр., 13", (55.723211, 37.551453), 500, "Новолужнецкий", "плавани"),
 "swimaquarel-teply-stan": ("Swimaquarel", "Москва, ул. Тёплый Стан, 9, корп. 9", (55.618712, 37.492764), 300, "Тёплый Стан", "бассейн"),
 "mevis-teply-stan": ("Mevis", "Москва, ул. Тёплый Стан, 9, корп. 9", (55.618712, 37.492764), 300, "Тёплый Стан", "Mevis"),
 "piranya-zarechye": ("Пиранья", "Заречье, Заречная ул., 2", (55.688806, 37.393141), 400, "Заречная", "Пиран"),
 "nado-plavat-tushinskaya": ("Надо Плавать", "Москва, Тушинская ул., 16А", (55.8275, 37.443), 600, "Тушинская", "Октябрь"),
 "wellness-hall-dinamo": ("Веллнес Холл", "Москва, Ленинградское ш., 39, стр. 53", (55.837373, 37.479071), 400, "Ленинградское", "Wellness"),
 "swimrocket-dinamo": ("SwimRocket", "Москва, Ленинградское ш., 39, стр. 53", (55.837373, 37.479071), 400, "Ленинградское", "бассейн"),
 "vtoroe-rozhdenie-kosinskaya": ("Второе рождение", "Москва, Косинская ул., 12Б", (55.724794, 37.833585), 300, "Косинская", "рождение"),
 "shkola-plavaniya-shchorsa": ("Школа плавания", "Москва, ул. Щорса, 6", (55.646672, 37.403031), 300, "Щорса", "плавани"),
 "fitness-hall-shcherbinka": ("Фитнес Холл", "Щербинка, ул. Чапаева, 8А", (55.5075, 37.565), 1500, "Чапаева", "Холл"),
 "moskvich-volgogradsky": ("Москвич, бассейн", "Москва, Волгоградский просп., 46/15с7", (55.7095, 37.722), 800, "Волгоградский", "Москвич"),
 "kitenok-volgogradsky-32": ("Китёнок", "Москва, Волгоградский просп., 32/5к2", (55.719553, 37.690716), 400, "Волгоградский", "Китёнок"),
}
AREAS = ["Деловой центр", "Динамо", "Дмитровская", "Добрынинская", "Домодедовская", "Достоевская", "Дубровка", "Жулебино",
         "ЗИЛ", "Зорге", "Зюзино", "Зябликово", "Измайлово"]
SITES = ["https://octoskills.ru/rannee-plavanie-dlya-detej/", "https://mevis.ru/", "https://www.swimrocket.ru/bassein",
         "https://www.swimrocket.ru/detskie-gruppy"]
if __name__ == "__main__":
    lines, out = list(SITES), []
    for i, (pid, (nm, addr, c, r, st, match)) in enumerate(Q.items()):
        lines.append("https://yandex.ru/maps/1/moscow-and-moscow-oblast/?po%d=1113e&text=%s" % (i, urllib.parse.quote(nm + ", " + addr)))
        out.append({"id": "pl18-" + pid, "lat": c[0], "lon": c[1], "radius": r, "name": match, "street": st})
    for i, a in enumerate(AREAS):
        for j, q in enumerate(("обучение плаванию детей с 3 лет метро ", "грудничковое плавание метро ")):
            lines.append("https://yandex.ru/maps/1/moscow-and-moscow-oblast/?pz%d=1113e&text=%s" % (i * 2 + j, urllib.parse.quote(q + a)))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in lines if l not in old]) + "\n")
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("pl18-")]
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(out), len(lines))
