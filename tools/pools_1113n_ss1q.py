"""Робот pools 13.11 (15 UTC), шаг 1б: Школа плавания № 1 — бассейны из списка swim-school-1.ru/basseyni, которых нет в базе:
карточки Яндекс Карт (ключ po<N>=1113n) → auto/fetch-queue.txt, справка OSM (pl22-*) → auto/osm-queries.json.
python3 tools/pools_1113n_ss1q.py"""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
# id: (адрес для Яндекса, центр поиска, радиус, улица OSM)
Q = {
 "ss1-korall-krasnoselsky": ("Москва, 1-й Красносельский пер., 9", (55.7795, 37.668), 900, "Красносельский"),
 "ss1-kolomensky-proezd": ("Москва, Коломенский пр., 15А", (55.670, 37.662), 1500, "Коломенский"),
 "ss1-veshnyaki-kosinskaya": ("Москва, Косинская ул., 12Б", (55.7195, 37.823), 1200, "Косинская"),
 "ss1-zorky-krasnogorsk": ("Красногорск, Советская ул., 15", (55.8215, 37.3305), 1500, "Советская"),
 "ss1-altaysky": ("Москва, Алтайская ул., 33", (55.816, 37.830), 1200, "Алтайская"),
 "ss1-burevestnik-plyushchikha": ("Москва, ул. Плющиха, 57, стр. 1", (55.7375, 37.573), 900, "Плющиха"),
 "ss1-dinamo-leningradskoe": ("Москва, Ленинградское ш., 9, стр. 53", (55.822, 37.497), 1800, "Ленинградское"),
 "ss1-eseninsky": ("Москва, Есенинский бул., 9, корп. 2, стр. 1", (55.703, 37.775), 1200, "Есенинский"),
 "ss1-obraztsova": ("Москва, ул. Образцова, 11, стр. 4", (55.789, 37.608), 900, "Образцова"),
 "ss1-zhivopisny": ("Москва, Живописная ул., 28, стр. 6", (55.787, 37.455), 1500, "Живописная"),
 "ss1-krylatskoe-ostrovnaya": ("Москва, Островная ул., 1, стр. 1", (55.767, 37.435), 1500, "Островная"),
 "ss1-kuryanovo": ("Москва, 1-й Курьяновский пр., 17, стр. 1", (55.650, 37.700), 1500, "Курьяновский"),
 "ss1-kachalovsky": ("Москва, бул. Дмитрия Донского, 14", (55.567, 37.578), 1500, "Дмитрия Донского"),
 "ss1-odintsovo-mozhayskoe": ("Одинцово, Можайское ш., 109А", (55.673, 37.250), 2500, "Можайское"),
}
if __name__ == "__main__":
    lines, out = [], []
    for i, (pid, (addr, c, r, st)) in enumerate(Q.items()):
        lines.append("https://yandex.ru/maps/1/moscow-and-moscow-oblast/?po%d=1113n&text=%s" % (i, urllib.parse.quote("Школа плавания № 1, " + addr)))
        out.append({"id": "pl22-" + pid, "lat": c[0], "lon": c[1], "radius": r, "name": "бассейн", "street": st})
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in lines if l not in old]) + "\n")
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("pl22-")]
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(out), len(lines))
