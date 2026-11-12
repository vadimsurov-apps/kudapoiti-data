"""Робот rare, 12.11 (19 UTC): кандидаты из выдачи Яндекс Карт по районам второго круга (auto/pages, r19a* — 1112x):
Полянка … Рассказовка × (каток / хоккей / фигурное / настольный теннис / волейбол для детей) + катки и тюбинг Подмосковья.
Пишет справку OSM (auto/osm-queries.json, rare12x-*) и карточки Яндекс Карт (r19b*) в fetch-queue. python3 tools/rare_1112x_cands.py"""
import json, os, urllib.parse as u
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
C = [
 ("ski-school-kant", "Кант горнолыжная школа", "Москва, Электролитный пр., 7Б", "Электролитный", "tube-kant", 600, "Кант"),
 ("tubing-gotubing-podrezkovo", "Тюбинг трасса GOTubing", "Химки, микрорайон Подрезково", "", "khimki-podrezkovo-park", 2500, "ubing"),
 ("rink-ledovy-konstruktor-khimki", "Ледовый Конструктор", "Химки, Транспортный пр., вл17с1", "Транспортный", "batut-solnyshko-khimki", 1500, "Конструктор"),
 ("rink-ledo-kashirskoe", "Ледо каток", "Москва, МКАД, 24-й километр, 1", "", (55.5875, 37.7255), 900, "Ледо"),
 ("rink-riga-ice-land", "Riga Ice Land", "Красногорск, Новорижское шоссе, 26-й километр, с6", "", (55.772, 37.215), 4000, "Riga"),
 ("rink-orion-tekhnopul", "Орион-Технопул каток", "Балашиха, микрорайон Железнодорожный", "", (55.748, 38.010), 3500, "Орион"),
 ("volley-sila-voley-vnukovo", "Сила Волей", "Москва, улица Бориса Пастернака, 16", "Бориса Пастернака", "kitenok-vnukovo-pasternaka", 600, ""),
 ("hockey-smart-arena-mitino", "Смарт Хоккей Арена", "Москва, Дубравная ул., 51, стр. 1", "Дубравная", "rink-mitino-ice-arena", 400, ""),
 ("fk-ice-stars-mitino", "Ice Stars фигурное катание", "Москва, Дубравная ул., 51, стр. 1", "Дубравная", "rink-mitino-ice-arena", 400, ""),
 ("hockey-star-mitino", "Hockey-star.ru", "Москва, Дубравная ул., 51, стр. 1", "Дубравная", "rink-mitino-ice-arena", 400, ""),
 ("fk-axel-plyushchikha", "Axel фигурное катание", "Москва, ул. Плющиха, 57", "Плющиха", "ilikeice-burevestnik", 400, ""),
 ("volley-preobrazhaet", "Волейбол преображает", "Москва, 1-я ул. Бухвостова, 3", "Бухвостова", (55.7935, 37.7085), 900, ""),
 ("fk-armiya-ochakovo", "Армия фигурного катания", "Москва, Большая Очаковская ул., 2, корп. 2, стр. 3", "Очаковская", "cafe-senoval-ochakovo", 600, ""),
 ("hockeychance-prospekt-mira", "HockeyChance", "Москва, просп. Мира, 51, стр. 1", "Мира", (55.7845, 37.6345), 900, ""),
 ("tt-trclub-tikhvinsky", "TR club настольный теннис", "Москва, Тихвинский пер., 10-12к9", "Тихвинский", "svobodnye-shakhmaty-tikhvinsky", 400, ""),
 ("tt-schastlivoe-vremya", "Счастливое время", "Москва, ул. Адмирала Лазарева, 77", "Адмирала Лазарева", (55.5400, 37.5170), 1500, ""),
 ("volley-sportklub-potapovo", "СпортКлуб Потапово", "Москва, ул. Адмирала Лазарева, 76А", "Адмирала Лазарева", (55.5400, 37.5170), 1500, ""),
 ("tt-mytishchi-top-team", "Mytishchi top team", "Мытищи, просп. Астрахова, 7/1", "Астрахова", "chess-first-mytishchi", 500, ""),
 ("tt-ping-point", "Ping Point", "Москва, 1-я Квесисская ул., 9", "Квесисская", (55.7905, 37.5835), 900, ""),
 ("tt-klassnaya-podacha", "Классная Подача", "Мытищи, Юбилейная ул., с27А", "Юбилейная", (55.920, 37.750), 3500, ""),
 ("tt-rakettka-nezhinskaya", "Ракеттка", "Москва, Нежинская ул., 17, корп. 4", "Нежинская", "flyzone-parkour-slavyansky", 400, ""),
 ("tt-match-point-krasnogorsk", "Матч Поинт", "Красногорск, Международная ул., 20", "Международная", "tennisart-school-krasnogorsk", 500, ""),
 ("rink-platinum-zelenograd", "Платинум спортивный комплекс", "Зеленоград, к2045", "", (55.980, 37.160), 3500, "Платинум"),
 ("squash-club-moskva-luzhniki", "Сквош-клуб Москва", "Москва, ул. Лужники, 24, стр. 21", "Лужники", "padel-multisport-luzhniki", 700, ""),
 ("fk-led-khimki", "Лёд школа фигурного катания", "Химки, ул. Мичурина, с24", "Мичурина", "aquababy-khimki-michurina", 700, ""),
 ("fk-led-zheleznodorozhny", "Лёд школа фигурного катания", "Балашиха, Железнодорожный, Пионерская ул., 1А", "Пионерская", (55.748, 38.010), 3500, ""),
]
if __name__ == "__main__":
    allp = {p["id"]: p for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
    qp = os.path.join(ROOT, "auto", "osm-queries.json")
    qs = json.load(open(qp)); have = {q["id"] for q in qs}; fq = []
    for i, c in enumerate(C):
        ll = c[4]
        if isinstance(ll, str):
            p = allp.get(ll)
            ll = (p["lat"], p["lon"]) if p and p.get("lat") else None
        if ll:
            q = {"id": "rare12x-" + c[0], "lat": ll[0], "lon": ll[1], "radius": c[5], "name": c[6]}
            if c[3]: q["street"] = c[3]
            if q["id"] not in have: qs.append(q)
        else:
            print("нет точки для запроса:", c[0])
        fq.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?r19b{i:02d}=1112x&text=" + u.quote(f"{c[1]}, {c[2]}"))
    json.dump(qs, open(qp, "w"), ensure_ascii=False, indent=1)
    open(os.path.join(ROOT, "auto", "fetch-queue.txt"), "a").write("\n".join(fq) + "\n")
    print(len(C), len(fq))
