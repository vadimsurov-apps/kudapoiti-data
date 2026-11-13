"""Робот rare, 13.11 (07 UTC; 1113c): кандидаты из выдачи Яндекс Карт (auto/pages, rr13e*) — без дублей по places-all (адрес+название).
Пишет справку OSM (auto/osm-queries.json, rare13d-*) и карточки Яндекс Карт (rr13g*) в fetch-queue.
Точка запроса — места базы на той же улице/в том же городе (медиана). python3 tools/rare_1113c_cands.py"""
import json, os, statistics as st, urllib.parse as u
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
# id, имя для поиска, адрес, улица (фильтр OSM), якорь (медиана точек базы), радиус, имя для OSM
C = [
 ("rink-olimpiysky-chekhov", "ДС Олимпийский им. В. С. Максимова ледовый дворец", "Чехов, Московская ул., 104", "Московская", "Чехов", 4000, "Олимпийский"),
 ("rink-petrusevoy-pavlovsky-posad", "Ледовая арена имени Н.А. Петрусевой", "Павловский Посад, Большая Покровская ул., 60В", "Покровская", "Павловский Посад", 4000, ""),
 ("rink-meshchera-egoryevsk", "Мещера спортивный комплекс каток", "Егорьевск, Октябрьская ул., 121", "Октябрьская", "Егорьевск", 4000, "Мещера"),
 ("rink-b-class-serpukhov", "Ледовая арена Б-Класс", "Серпухов, Московское ш., 55, корп. 1", "Московское", "Серпухов, Московское ш., 55", 600, ""),
 ("fk-aksel-serpukhov", "Аксель фигурное катание Серпухов", "Серпухов, Московское ш., 55, корп. 1", "Московское", "Серпухов, Московское ш., 55", 600, ""),
 ("rink-bolshedvorsky", "Большедворский спортивный комплекс", "рабочий посёлок Большие Дворы", "", "Павловский Посад", 8000, "Большедвор"),
 ("rink-lider-saranskaya", "Лидер спортивный комплекс каток", "Москва, Саранская ул., вл7", "Саранская", "Саранская", 800, "Лидер"),
 ("rink-snezhny-bars-ochakovo", "Ледовая арена Снежный Барс", "Москва, Большая Очаковская ул., 2, корп. 2, стр. 3", "Очаковская", "Очаковская", 1000, ""),
 ("hockey-red-machine-ochakovo", "Красная Машина хоккей", "Москва, Большая Очаковская ул., 2, корп. 2, стр. 3", "Очаковская", "Очаковская", 1000, ""),
 ("hockey-star-ostafyevskaya", "Hockey-star.ru", "Москва, Остафьевская ул., 21/1", "Остафьевская", "Остафьевская ул., 21", 600, "Монтреал"),
 ("hockey-star-saltykovskaya", "Hockey-star.ru", "Москва, Салтыковская ул., 1, стр. 1", "Салтыковская", "Салтыковская ул., 1", 600, "Атлетикс"),
 ("hockey-star-entuziastov-12", "Hockey-star.ru", "Москва, ш. Энтузиастов, 12, корп. 2", "Энтузиастов", "Энтузиастов, 12", 500, "Город"),
 ("hockey-shark-skills-leningradsky", "Шарк Скилс Хоккей", "Москва, Ленинградский просп., 39, стр. 1", "Ленинградский", "Ленинградский просп., 39", 600, ""),
 ("hockey-edition-voronezhskaya", "Хоккей Эдишен", "Москва, Воронежская ул., 13", "Воронежская", "Воронежская ул., 13", 500, "Русь"),
 ("volley-rusvolley-aviamotornaya", "Rusvolley", "Москва, Авиамоторная ул., 1", "Авиамоторная", "Авиамоторная", 800, ""),
 ("volley-rusvolley-kondratyevsky", "Rusvolley", "Москва, Большой Кондратьевский переулок", "Кондратьевский", "Кондратьевский", 600, ""),
 ("volley-rusvolley-zolotorozhsky", "Rusvolley", "Москва, Верхний Золоторожский пер., 2", "Золоторожский", "Золоторожский", 600, ""),
 ("volley-rusvolley-saltykovskaya-49", "Rusvolley", "Москва, Салтыковская ул., вл49", "Салтыковская", "Салтыковская", 1500, ""),
 ("volley-rusvolley-mira-101", "Rusvolley", "Москва, просп. Мира, 101В, стр. 3", "Мира", "Мира, 101", 500, ""),
 ("volley-rusvolley-krupskoy", "Rusvolley", "Москва, ул. Крупской, 17", "Крупской", "Ломоносовский", 1200, ""),
 ("volley-rusvolley-podvoyskogo", "Rusvolley", "Москва, ул. Подвойского, 2, стр. 1", "Подвойского", "Красная Пресня", 1500, ""),
 ("volley-rusvolley-yablochkova", "RusVolley", "Москва, ул. Яблочкова, 7", "Яблочкова", "Яблочкова, 7", 500, "Апиа"),
 ("volley-nevsky-bears-novorogozhskaya", "Невские медведи волейбол", "Москва, Новорогожская ул., 5", "Новорогожская", "Новорогожская", 600, ""),
 ("squash-1210-berezhkovskaya", "Сквош-клуб 12:10", "Москва, Бережковская наб., 20, стр. 64", "Бережковская", "Бережковская", 1200, ""),
 ("squash-ostafyevskaya", "Сквош клуб", "Москва, Остафьевская ул., литГ", "Остафьевская", "Остафьевская ул., 21", 800, "сквош"),
 ("tt-krasny-kit-mytishchi", "Школа настольного тенниса Красный Кит", "Мытищи, Шараповский пр., вл2с3", "Шараповский", "Шараповский", 600, "Красный Кит"),
 ("rink-yurlovsky", "Ледовый комплекс Юрловский", "Москва, Юрловский пр., вл6", "Юрловский", "Юрловский", 600, "Юрлов"),
 ("rink-spartak-sporttekh-latsisa", "Спартак - Спорттех", "Москва, ул. Вилиса Лациса, вл26", "Лациса", "Лациса, 26", 600, ""),
 ("volley-like-club-rastunovo", "Like Club волейбол", "село Растуново, Мирная ул., 3", "Мирная", "Домодедово", 15000, "Like"),
]
if __name__ == "__main__":
    P = json.load(open(os.path.join(ROOT, "places-all.json")))["places"]
    qp = os.path.join(ROOT, "auto", "osm-queries.json")
    qs = json.load(open(qp)); have = {q["id"] for q in qs}; fq = []
    for i, c in enumerate(C):
        if os.environ.get("ONLY") and c[0] not in os.environ["ONLY"].split(): continue
        pts = [(p["lat"], p["lon"]) for p in P if p.get("lat") and c[4].lower() in ((p.get("address") or "") + " " + p["name"]).lower()]
        if pts:
            ll = (st.median(x for x, _ in pts), st.median(y for _, y in pts))
            q = {"id": "rare13d-" + c[0], "lat": ll[0], "lon": ll[1], "radius": c[5], "name": c[6]}
            if c[3]: q["street"] = c[3]
            if q["id"] not in have: qs.append(q)
        else:
            print("нет точки для запроса:", c[0])
        fq.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?rr13g{i:02d}=1113c&text=" + u.quote(f"{c[1]}, {c[2]}"))
    json.dump(qs, open(qp, "w"), ensure_ascii=False, indent=1)
    open(os.path.join(ROOT, "auto", "fetch-queue.txt"), "a").write("\n".join(fq) + "\n")
    print(len(C), len(fq))
