"""Робот rare, 12.11 (16:10 UTC): кандидаты из выдачи Яндекс Карт по районам второго круга (auto/pages, r16a* — 1112u):
Парк Победы … Полежаевская × (каток / хоккей / фигурное катание / настольный теннис / волейбол для детей) + катки Подмосковья.
Пишет справку OSM (auto/osm-queries.json, rare12u-*) и карточки Яндекс Карт (r16b*) в fetch-queue. python3 tools/rare_1112u_cands.py"""
import json, os, urllib.parse as u
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
# (id, название для поиска, адрес, улица OSM, (lat, lon) | id места базы в том же доме, радиус, имя OSM)
C = [
 ("rink-arena-mytishchi", "Арена Мытищи им. В. И. Шалимова", "Мытищи, Лётная ул., 17", "Лётная", "hockey-sshor-mytishchi", 600, "Арена"),
 ("rink-kosmoled-korolev", "Каток Космолёд", "Королёв, Октябрьская ул., 6, стр. 1", "Октябрьская", (55.918, 37.823), 3500, "Космол"),
 ("rink-talalikhina-podolsk", "Каток Парка КИО им. Талалихина", "Подольск, Рабочая ул., 5Б", "Рабочая", "podolsk-talalikhin-park", 800, "Каток"),
 ("rink-favorit-borodino", "Каток Фаворит", "д. Бородино, Варшавское ш., 1, стр. 1", "Варшавское", (55.505, 37.586), 4000, "Фаворит"),
 ("rink-lytkarino-lsk", "Ледовый спортивный комплекс Лыткарино", "Лыткарино, Советская ул., 9А", "Советская", "lyapkin-hockey-lytkarino", 600, "Ледов"),
 ("rink-maksimova-chekhov", "ДС Олимпийский им. В. С. Максимова ледовый дворец", "Чехов, Московская ул., 104", "Московская", (55.153, 37.462), 4000, "Олимпийский"),
 ("rink-pekhorka-arena", "Арена Пехорка", "Балашиха, Парковая ул., 2А", "Парковая", "balashikha-pekhorka-park", 1000, "Арена"),
 ("rink-krasnogorsk-arena", "Красногорск Арена", "Красногорск, Лесная ул., 1А", "Лесная", "karting-global-racing-krasnogorsk", 1000, "Арена"),
 ("rink-cska-arena", "ЦСКА Арена массовое катание", "Москва, квартал Парк Легенд", "", (55.7065, 37.6585), 1200, "ЦСКА"),
 ("rink-sporttekh-arena", "СпортТех Арена", "Москва, ул. Вилиса Лациса, вл26", "Вилиса Лациса", (55.8655, 37.4285), 1500, "Спорт"),
 ("rink-icem-vegas-crocus", "Icem Group Вегас-2 Крокус Сити каток", "Красногорск, Международная ул., 12", "Международная", "ambiland-crocus", 800, "Vegas"),
 ("rink-serebryany-led", "Серебряный лёд", "Москва, Московский просп., 2, стр. 2", "", "pool-izmaylovo", 1500, "Серебр"),
 ("hockey-star-molochny", "Hockey-star.ru", "Москва, Молочный пер., 1", "Молочный", (55.7405, 37.5960), 800, ""),
 ("hockey-star-kievsky", "Hockey-star.ru", "Москва, площадь Киевского Вокзала, 1", "", (55.7435, 37.5665), 800, "Каток"),
 ("hockey-star-entuziastov", "Hockey-star.ru", "Москва, ш. Энтузиастов, вл33", "", "figurist-vao-sporttekh", 500, ""),
 ("hockeychance-magistralnaya", "HockeyChance", "Москва, 2-я Магистральная ул., 10, стр. 2", "2-я Магистральная", "lemans-karting", 800, ""),
 ("hockey-shark-skills", "Шарк Скилс Хоккей", "Москва, Ленинградский просп., 39, стр. 1", "Ленинградский", (55.791, 37.551), 1000, "Шарк"),
 ("hockey-edition-volgogradsky", "Хоккей Эдишен", "Москва, Волгоградский просп., 46/15с10", "Волгоградский", (55.7105, 37.7280), 1000, ""),
 ("hockey-krasnaya-mashina-opalikha", "Красная машина Юниор", "Красногорск, мкр Опалиха, ул. Ахматовой, 26", "", "rink-start-arena-opalikha", 500, ""),
 ("hockey-arena-bobry", "Арена Бобры", "Мытищи, мкр Посёлок Пироговский, Пионерская ул., с2Б/1", "Пионерская", (55.975, 37.715), 4000, "Бобр"),
 ("fk-polar-team", "Polar team фигурное катание", "Москва, ул. Плющиха, 59, стр. 11", "Плющиха", (55.7385, 37.5765), 800, ""),
 ("fk-vyshe-vseh", "Выше всех спортивная школа", "Москва, Егорьевский пр., 3Ж, стр. 6", "", "fd-egoryevsky", 400, ""),
 ("fk-klub-lider-lefortovo", "Клуб Лидер фигурное катание", "Москва, ш. Энтузиастов, 12, корп. 2", "", "rink-grad-lefortovo", 400, ""),
 ("fk-v-ritme-sporta", "В Ритме Спорта", "Москва, ул. Талалихина, 28, стр. 4", "Талалихина", "pool-atlant", 600, ""),
 ("fk-ledovaya-feeriya-mytishchi", "Ледовая феерия", "Мытищи, Лётная ул., 17", "", "hockey-sshor-mytishchi", 500, ""),
 ("fk-led-balashikha", "Лёд школа фигурного катания", "Балашиха, Парковая ул., 2", "", "balashikha-pekhorka-park", 1000, ""),
 ("fk-led-korolev", "Лёд школа фигурного катания", "Королёв, Октябрьский бул., 10, стр. 1", "", "rink-kasatonov-korolev", 400, ""),
 ("fk-led-mytishchi", "Лёд школа фигурного катания", "Мытищи, Лётная ул., 17", "", "hockey-sshor-mytishchi", 500, ""),
 ("tt-hurricane", "Харрикейн-ТТ", "Москва, ул. Сущёвский Вал, 5, стр. 11", "Сущёвский Вал", "ttleader-savelovsky", 500, ""),
 ("tt-territoriya-altufyevskoe", "Территория настольного тенниса", "Москва, Алтуфьевское ш., 8", "Алтуфьевское", "extremekids-roller-otradnoe", 500, ""),
 ("tt-o2-parkovaya", "О2 настольный теннис", "Москва, 11-я Парковая ул., 24", "11-я Парковая", (55.795, 37.795), 1200, ""),
 ("tt-lucentr", "ЛуЦентр настольный теннис", "Москва, Старокирочный пер., 2", "Старокирочный", "idanko-ballet-starokirochny", 400, ""),
 ("volley-open-zhukova", "Open Volleyball", "Москва, просп. Маршала Жукова, 4, стр. 2", "", "doaflip-zhukova", 500, ""),
 ("volley-palma-vavilova", "Palma volley club", "Москва, ул. Вавилова, 81, корп. 1", "", "shturm-vavilova", 400, ""),
 ("volley-spektr-latsisa", "Spektr volley", "Москва, ул. Вилиса Лациса, вл20", "", "ms-handball-academy", 400, ""),
 ("volley-panda-nagatinskaya", "Панда Воллей", "Москва, Нагатинская ул., 16", "", "minimania-nagatinskaya", 400, ""),
 ("volley-playforfun-latsisa", "Play For Fun волейбол", "Москва, ул. Вилиса Лациса, вл20", "", "ms-handball-academy", 400, ""),
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
            q = {"id": "rare12u-" + c[0], "lat": ll[0], "lon": ll[1], "radius": c[5], "name": c[6]}
            if c[3]: q["street"] = c[3]
            if q["id"] not in have: qs.append(q)
        else:
            print("нет точки для запроса:", c[0])
        fq.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?r16b{i:02d}=1112u&text=" + u.quote(f"{c[1]}, {c[2]}"))
    json.dump(qs, open(qp, "w"), ensure_ascii=False, indent=1)
    open(os.path.join(ROOT, "auto", "fetch-queue.txt"), "a").write("\n".join(fq) + "\n")
    print(len(C), len(fq))
