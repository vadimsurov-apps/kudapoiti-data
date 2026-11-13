"""Робот pools 13.11 (15 UTC), шаг 2: карточки Яндекс Карт новых кандидатов (ключ po<N>=1113n, N с 20) → auto/fetch-queue.txt,
справка OSM (pl23-*) → auto/osm-queries.json.   python3 tools/pools_1113n_cardq.py"""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
# id: (название в Яндексе, адрес в Яндексе, центр поиска, радиус, улица OSM, имя для сверки)
Q = {
 "strela-grimau": ("Стрела", "Москва, ул. Гримау, 6", (55.688, 37.573), 900, "Гримау", "Стрела"),
 "pyat-utyat-filevskaya": ("Пять утят", "Москва, Малая Филёвская ул., 30", (55.737, 37.465), 1800, "Филёвская", "утят"),
 "pikalova-luzhniki": ("Pikalova swimming, школа плавания", "Москва, Лужнецкая наб., 24, стр. 4", (55.7165, 37.555), 1500, "", "водных"),
 "swimrocket-luzhniki": ("SwimRocket", "Москва, Лужнецкая наб., 24", None, 0, "", ""),
 "chudo-ostrov-elektrostal": ("Чудо Остров", "Электросталь, ул. Ялагина, 3", (55.775, 38.465), 4000, "Ялагина", "Остров"),
 "akva-smart-elektrostal": ("Аква Smart", "Электросталь, ул. Радио, 35", (55.785, 38.445), 4000, "Радио", "бассейн"),
 "rybka-moya-odintsovo": ("Рыбка моя", "Одинцово, микрорайон Новая Трёхгорка, Кутузовская ул., 72", (55.655, 37.31), 2500, "Кутузовская", "Рыбка"),
 "akvazavrik-odintsovo": ("Аквазаврик", "Одинцово, бул. Маршала Крылова, 25А", (55.667, 37.285), 2500, "Крылова", "Аквазавр"),
 "real-swim-odintsovo": ("Реал Свим", "Одинцово, ул. Маковского, 16", (55.667, 37.27), 3500, "Маковского", "бассейн"),
 "okeanika-domodedovo": ("Детская школа плавания Океаника", "Домодедово, микрорайон Центральный, Каширское ш., 107А", (55.44, 37.76), 4500, "Каширское", "бассейн"),
 "komornikov-domodedovo": ("Школа Дмитрия Коморникова", "Домодедово, Каширское ш., 107А", None, 0, "", ""),
 "akvautyata-serpukhov": ("АкваУтятаПлюс", "Серпухов, ул. Ворошилова, 57", (54.925, 37.43), 4500, "Ворошилова", "Утят"),
 "akvatika-shchelkovo": ("Акватика", "Щёлково, ул. Мичурина, 58", (55.92, 38.0), 4500, "Мичурина", "Акватик"),
 "krabibu-ramenskoe": ("Крабибу", "Раменское, ул. Приборостроителей, 1А", (55.57, 38.22), 4500, "Приборостроителей", "Краб"),
 "morskoy-lvenok-ramenskoe": ("Aqua клуб Морской львёнок", "Раменское, Бронницкая ул., 6", (55.565, 38.225), 4500, "Бронницкая", "льв"),
 "laguna-volzhsky": ("Лагуна", "Москва, Волжский бул., 8А", (55.709, 37.745), 1800, "Волжский", "Лагуна"),
 "spn-khimki-michurina": ("", "", (55.912, 37.458), 900, "Мичурина", "бассейн"),
}
if __name__ == "__main__":
    lines, out = [], []
    for i, (pid, (nm, addr, c, r, st, match)) in enumerate(Q.items()):
        if nm:
            lines.append("https://yandex.ru/maps/1/moscow-and-moscow-oblast/?po%d=1113n&text=%s" % (i + 20, urllib.parse.quote(nm + ", " + addr)))
        if c:
            q = {"id": "pl23-" + pid, "lat": c[0], "lon": c[1], "radius": r, "name": match}
            if st: q["street"] = st
            out.append(q)
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in lines if l not in old]) + "\n")
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("pl23-")]
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(out), len(lines))
