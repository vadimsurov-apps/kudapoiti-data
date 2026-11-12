"""Робот rare, 12.11 (22 UTC): кандидаты из выдачи Яндекс Карт по районам второго круга (auto/pages, rr22a* — 1112z):
Речной вокзал … Славянский бульвар × (каток / хоккей / фигурное / настольный теннис / скалодром для детей) + катки Подмосковья,
тюбинг, склоны, сквош, скалодромы, картинг, верёвочные парки. Пишет справку OSM (auto/osm-queries.json, rare12z-*) и карточки
Яндекс Карт (rr22b*) в fetch-queue. python3 tools/rare_1112z_cands.py"""
import json, os, urllib.parse as u
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
C = [
 ("rink-kolomna-speed-center", "Конькобежный центр Коломна", "Коломна, наб. реки Коломенки, 7", "Коломенки", (55.0950, 38.7660), 2000, "Коломна"),
 ("rink-ionova-elektrostal", "Крытый тренировочный каток имени А.С. Ионова", "Электросталь, Спортивная ул., 10", "Спортивная", "pool-kristall-elektrostal", 600, "Ионова"),
 ("fk-led-noginsk", "Лёд школа фигурного катания", "Ногинск, ул. Климова, 48А", "Климова", (55.8540, 38.4420), 3000, ""),
 ("rink-ld-dmitrov", "Ледовый дворец Дмитров", "Дмитров, Профессиональная ул., 25", "Профессиональная", "hockey-center-dmitrov", 500, "Ледов"),
 ("fk-curling-dmitrov", "Центр фигурного катания и кёрлинга", "Дмитров, Профессиональная ул., 29", "Профессиональная", "hockey-center-dmitrov", 500, "кёрлинг"),
 ("rink-ld-naro-fominsk", "Ледовый дворец Наро-Фоминск имени Шалимова", "Наро-Фоминск, Профсоюзная ул., 36Б", "Профсоюзная", (55.3860, 36.7350), 3500, "Ледов"),
 ("rink-selyatino-arena", "Ледовая арена Селятино имени Мышкина", "Селятино, Спортивная ул., 3, стр. 4", "Спортивная", (55.5150, 36.9800), 3000, "Ледов"),
 ("rink-lutchenko-ramenskoe", "ФОК Ледовая арена имени Лутченко", "Раменское, ул. Махова, 18/2", "Махова", "climb-gran-ramenskoe", 3000, "Лутченко"),
 ("rink-aispark-zhukovsky", "АйсПарк", "Жуковский, Молодёжная ул., 9", "Молодёжная", "akademiya-figuristov-zhukovsky", 400, ""),
 ("rink-lobnya-ds", "Ледовый каток Дворец спорта Лобня", "Лобня, ул. Ленина, 65, стр. 3", "Ленина", "championika-lobnya", 500, ""),
 ("rink-fok-oka-dzerzhinsky", "ФОК ОКА", "Дзержинский, Окская наб., 5А", "Окская", "ski-snegiri-dzerzhinsky", 3000, "Ока"),
 ("rink-arena-legend-ozery", "Арена Легенд", "Озёры, Парковая ул., 2Г", "Парковая", "pool-chayka-ozery", 3000, "Арена"),
 ("fk-aksel-serpukhov", "Аксель фигурное катание", "Серпухов, Московское ш., 55, корп. 1", "Московское", "aqua-serpukhov", 500, ""),
 ("rink-burevestnik-plyushchikha", "Каток Буревестник", "Москва, ул. Плющиха, 59, стр. 11", "Плющиха", "fk-axel-plyushchikha", 400, ""),
 ("rink-varshavskoe-10", "Каток", "Москва, Варшавское ш., 10, корп. 1", "Варшавское", (55.7000, 37.6215), 1200, "ат"),
 ("rink-skryabina-7", "Каток", "Москва, ул. Академика Скрябина, 7, корп. 1", "Скрябина", (55.7190, 37.7700), 1800, "ат"),
 ("rink-yurlovsky", "Ледовый комплекс Юрловский", "Москва, Юрловский пр., вл6", "Юрловский", "sport-katok-yurlovsky", 400, ""),
 ("rink-lds-moskvich", "Ледовый дворец спорта Москвич", "Москва, Волгоградский просп., 46/15с10", "Волгоградский", "akro-miks-volgogradsky", 600, "Москвич"),
 ("rink-legenda-77", "Легенда 77", "Москва, Даниловская наб., 8А", "Даниловская", "hockey-star-danilovskaya", 400, "Легенда"),
 ("fk-razryad-fili", "Школа фигурного катания Разряд", "Москва, Филёвский бул., 38", "Филёвский", "hc-volki-fili", 400, ""),
 ("fk-victory-skating-solntsevo", "Victory Skating Team", "Москва, ул. Авиаторов, 7А", "Авиаторов", "rink-solntsevo-aviatorov", 400, ""),
 ("hockey-snaiper-select-solntsevo", "Хоккейная школа Снайпер-select", "Москва, ул. Авиаторов, 7А", "Авиаторов", "rink-solntsevo-aviatorov", 400, ""),
 ("hockey-verkhovod-solntsevo", "ХК Верховод", "Москва, ул. Авиаторов, 7А", "Авиаторов", "rink-solntsevo-aviatorov", 400, ""),
 ("hockey-star-solntsevo", "Хоккей стар", "Москва, ул. Авиаторов, 7А", "Авиаторов", "rink-solntsevo-aviatorov", 400, ""),
 ("fk-ice-group-filevskaya", "Айс Групп фигурное катание", "Москва, Большая Филёвская ул., 22, стр. 15", "Филёвская", "hc-volki-fili", 2000, ""),
 ("hockey-snaiper-select-fili", "Хоккейный клуб Снайпер-select", "Москва, Большая Филёвская ул., 22, стр. 15", "Филёвская", "hc-volki-fili", 2000, ""),
 ("hockey-mastera-mosfilmovskaya", "Мастера Хоккея", "Москва, Мосфильмовская ул., 41, корп. 3", "Мосфильмовская", "rink-led-mosfilmovskaya", 500, ""),
 ("hockey-monstr-balaklavsky", "Монстр хоккея", "Москва, Балаклавский просп., 33", "Балаклавский", "ilikeice-champion-bitsa", 500, ""),
 ("hockey-dnk-novoperedelkino", "Dnk Hockey Team", "Москва, Новоорловская ул., 7В", "Новоорловская", "galaktika-figure-arktika", 400, ""),
 ("hockey-star-novoorlovskaya", "Hockey-star.ru", "Москва, Новоорловская ул., 7В", "Новоорловская", "galaktika-figure-arktika", 400, ""),
 ("mazvs-novorogozhskaya", "Московская академия зимних видов спорта", "Москва, Новорогожская ул., 25, стр. 4", "Новорогожская", "ms-sk-vdokhnovenie", 400, ""),
 ("hockey-sadov-ryazansky", "Хоккей. Антон Садов", "Москва, Рязанский просп., 4, стр. 3", "Рязанский", "tennis-park-ryazansky", 500, ""),
 ("hockey-star-ryazansky4", "Hockey-star.ru", "Москва, Рязанский просп., 4", "Рязанский", "tennis-park-ryazansky", 500, ""),
 ("hockey-star-ryazansky7", "Hockey-star.ru", "Москва, Рязанский просп., 7, корп. 2", "Рязанский", "tennis-park-ryazansky", 800, ""),
 ("hockey-star-skhodnenskaya", "Hockey Star team", "Москва, Сходненская ул., 56", "Сходненская", "rink-kaleidoskop", 400, ""),
 ("hockey-star-tikhonovskaya", "Хоккей-стар.ру", "Москва, Большая Тихоновская ул., 2", "Тихоновская", (55.7905, 37.6935), 1500, ""),
 ("fk-bresmartim-medvedkovo", "Группа фигурного катания БресМарТим", "Москва, Заповедная ул., 3", "Заповедная", "ms-ld-medvedkovo", 400, ""),
 ("tt-planet-flotskaya", "Tt Planet", "Москва, Флотская ул., 7, стр. 1", "Флотская", "matsarr-activity-hall", 400, ""),
 ("tt-harrikein-savelovsky", "Харрикейн-ТТ", "Москва, ул. Сущёвский Вал, 5, стр. 11", "Сущёвский", "ttleader-savelovsky", 400, ""),
 ("tt-lucentr-starokirochny", "ЛуЦентр", "Москва, Старокирочный пер., 2", "Старокирочный", "idanko-ballet-starokirochny", 400, ""),
 ("tt-tops-losinka", "Топс-Лосинка", "Москва, ул. Лётчика Бабушкина, 17, корп. 1", "Бабушкина", "irbis-babushkinskaya", 500, ""),
 ("tt-naten-vernadskogo", "Натен", "Москва, просп. Вернадского, 78, стр. 5", "Вернадского", (55.6660, 37.4800), 1200, ""),
 ("tt-thunder-polyarnaya", "Thunder настольный теннис", "Москва, Полярная ул., 27, корп. 4", "Полярная", "act-place-polyarnaya", 500, ""),
 ("tt-ishanov-krasnoselskaya", "Школа настольного тенниса Али Ишанова", "Москва, Нижняя Красносельская ул., 40/12к4", "Красносельская", "irbis-baumanskaya", 500, ""),
 ("tt-ping-point-kvesisskaya", "Ping Point", "Москва, 1-я Квесисская ул., 9", "Квесисская", (55.7905, 37.5835), 900, ""),
 ("climb-limestone-dobroslobodskaya", "ЛаймСтоун скалодром", "Москва, Доброслободская ул., 21", "Доброслободская", (55.7695, 37.6745), 900, ""),
 ("climb-mars-ryazansky", "Марс скалодром", "Москва, Рязанский просп., 8А, корп. 3, стр. 8", "Рязанский", "tennis-park-ryazansky", 800, ""),
 ("climb-arena-smirnovskaya", "Арена скалодром", "Москва, Смирновская ул., 25, стр. 1", "Смирновская", "doaflip-smirnovskaya", 400, ""),
 ("climb-alpindustriya-simonovsky", "АльпИндустрия скалодром", "Москва, ул. Симоновский Вал, 7Б", "Симоновский", (55.7265, 37.6640), 900, ""),
 ("climb-tengu-dnepropetrovskaya", "Тенгус скалодром", "Москва, Днепропетровская ул., 2", "Днепропетровская", "bogi-gimnastiki-dnepropetrovskaya", 400, ""),
 ("climb-bigwall-avtozavodskaya", "Бигвол Спорт", "Москва, Автозаводская ул., 18", "Автозаводская", "art-insight-avtozavodskaya", 400, ""),
 ("squash-space-khimki", "Space сквош", "Химки, ул. Кирова, с24", "Кирова", (55.8890, 37.4450), 3000, ""),
 ("ski-moon-village-krasnogorsk", "Moon Village club", "Красногорск", "", None, 0, ""),
 ("ski-elki77-krasnogorsk", "Elki 77", "Красногорск, Красногорский бул., 23, корп. 1", "", None, 0, ""),
 ("ski-snowpark-spas-kamenka", "Сноупарк Спас-Каменка", "д. Спас-Каменка, Набережная ул., 2", "", None, 0, ""),
 ("ski-chernevskaya-gorka", "Черневская горка", "Подмосковье", "", None, 0, ""),
 ("ropes-tip-top", "Тип-Топ верёвочный парк", "Подмосковье", "", None, 0, ""),
 ("ropes-krona", "Крона верёвочный парк", "Подмосковье", "", None, 0, ""),
 ("karting-adm-raceway", "Комплекс технических видов спорта Adm Raceway", "Подмосковье", "", None, 0, ""),
 ("climb-les", "Скалодром Лес", "Подмосковье", "", None, 0, ""),
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
            q = {"id": "rare12z-" + c[0], "lat": ll[0], "lon": ll[1], "radius": c[5], "name": c[6]}
            if c[3]: q["street"] = c[3]
            if q["id"] not in have: qs.append(q)
        else:
            print("нет точки для запроса:", c[0])
        fq.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?rr22b{i:02d}=1112z&text=" + u.quote(f"{c[1]}, {c[2]}"))
    json.dump(qs, open(qp, "w"), ensure_ascii=False, indent=1)
    open(os.path.join(ROOT, "auto", "fetch-queue.txt"), "a").write("\n".join(fq) + "\n")
    print(len(C), len(fq))
