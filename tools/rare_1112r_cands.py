"""Робот rare, 12.11 (12:47 UTC): кандидаты из выдачи Яндекс Карт по районам второго круга (auto/pages, запросы r15a* — 1112r):
Новохохловская, Новоясеневская, Новые Черёмушки, Озёрная, Окружная, Окская, Октябрьская, Октябрьское поле, Ольховая, Орехово,
Отрадное, Охотный ряд, Павелецкая, Панфиловская × (каток / хоккей / фигурное катание / настольный теннис / волейбол для детей)
+ общие (тюбинг, склоны, театр зверей, памп-трек, сквош, шапито, каток в ТЦ).
Пишет справку OSM (auto/osm-queries.json, rare12r-*) и карточки Яндекс Карт (r15b*) в fetch-queue. python3 tools/rare_1112r_cands.py"""
import json, os, urllib.parse as u
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
# (id, название для поиска, адрес, улица для OSM, (lat, lon) примерно, радиус, имя объекта OSM, категория); lat=None — точка от места базы
C = [
 ("rink-luch-volokolamskoe", "Луч каток", "Москва, Волоколамское ш., 88, корп. 9, стр. 3", "Волоколамское", (55.8235, 37.4430), 1500, "Луч", "rinks"),
 ("hockey-krasnaya-mashina-ochakovo", "Красная Машина хоккей", "Москва, Большая Очаковская ул., 2, корп. 2, стр. 3", "Большая Очаковская", (55.6915, 37.4675), 1500, "", "hockey"),
 ("fk-plushenko-vostryakovskoe", "Ангелы Плющенко", "Москва, Востряковское ш., 1", "Востряковское", (55.6560, 37.3950), 4000, "", "figureskating"),
 ("volley-leto-vostryakovskoe", "Центр пляжных видов спорта Лето", "Москва, Востряковское ш., 7А", "Востряковское", (55.6560, 37.3950), 4000, "Лето", "volleyball"),
 ("volley-svs-vostryakovskoe", "Svs волейбол", "Москва, Востряковское ш., 7А", "Востряковское", (55.6560, 37.3950), 4000, "", "volleyball"),
 ("rink-legenda77-danilovskaya", "Легенда 77", "Москва, Даниловская наб., 8А", "Даниловская", (55.7055, 37.6455), 1500, "Легенда", "rinks"),
 ("hockey-chance-danilovskaya", "Hockey chance", "Москва, Даниловская наб., 8А", "Даниловская", (55.7055, 37.6455), 1500, "", "hockey"),
 ("hockey-star-danilovskaya", "Хоккей стар", "Москва, Даниловская наб., 8А", "Даниловская", (55.7055, 37.6455), 1500, "", "hockey"),
 ("fk-led-tenisty", "Лёд школа фигурного катания", "Москва, Тенистый пр., 8, стр. 1", "Тенистый", (55.8560, 37.6530), 1500, "", "figureskating"),
 ("rink-samolet-arena-kommunarka", "Самолёт Арена", "Москва, Коммунарка, квартал № 195, 16к1вл1", "", (55.5700, 37.4700), 4000, "Самол", "rinks"),
 ("rink-sodruzhestvo-novoyasenevsky", "Содружество спортивный комплекс", "Москва, Новоясеневский просп., 30", "Новоясеневский", (55.6040, 37.5370), 1500, "Содружество", "rinks"),
 ("tt-ping-point-kvesisskaya", "Ping Point", "Москва, 1-я Квесисская ул., 9", "Квесисская", (55.7935, 37.5800), 1500, "", "tabletennis"),
 ("tt-spin-pong-kommunarka", "Spin Pong", "Москва, Коммунарка, Скандинавский бульвар, 12", "Скандинавский", (55.5690, 37.4870), 2500, "", "tabletennis"),
 ("volley-sportbeach-bibirevskaya", "SportBeach", "Москва, Бибиревская ул., 10, корп. 1", "Бибиревская", (55.8840, 37.6050), 1500, "", "volleyball"),
 ("volley-moskvich-volgogradsky", "Москвич спортивный комплекс", "Москва, Волгоградский просп., 46/15с7", "Волгоградский", (55.7105, 37.7280), 1500, "Москвич", "volleyball"),
 ("tt-tenix-novocheremushkinskaya", "Tenix", "Москва, Новочерёмушкинская ул., 25", "Новочерёмушкинская", (55.6880, 37.5770), 1500, "", "tabletennis"),
 ("tt-voyka-kosmonavta-volkova", "Войка ТТ", "Москва, ул. Космонавта Волкова, 10", "Космонавта Волкова", (55.8154, 37.5148), 1000, "", "tabletennis"),
 ("volley-taktika-kashirskoe", "Taktika волейбол", "Москва, Каширское ш., 65, корп. 3", "Каширское", (55.6005, 37.7235), 1500, "", "volleyball"),
 ("volley-evaivi-leningradsky", "Эвайви спорт", "Москва, Ленинградский просп., 80, корп. 4А", "Ленинградский", (55.8085, 37.5110), 1000, "", "volleyball"),
 ("hockey-star-ryazansky7", "Hockey-star.ru", "Москва, Рязанский просп., 7, корп. 2", "Рязанский", (55.7265, 37.7470), 1500, "", "hockey"),
 ("hockey-star-yunykh-lenintsev", "Hockey-star.ru", "Москва, ул. Юных Ленинцев, 52, стр. 2", "Юных Ленинцев", (55.6999, 37.7650), 1500, "", "hockey"),
 ("hockey-star-novoyasenevsky26", "Hockey-star.ru", "Москва, Новоясеневский просп., 26", "", None, 0, "", "hockey"),
 ("hockey-star-krasnogo-mayaka", "Hockey-star.ru", "Москва, ул. Красного Маяка, вл28", "", None, 0, "", "hockey"),
 ("hockey-star-nizhnelikhoborsky", "Hockey-star.ru", "Москва, 3-й Нижнелихоборский пр., 1, стр. 6", "", None, 0, "", "hockey"),
 ("hockey-star-aviapark", "Hockey-star.ru", "Москва, Ходынский бул., 4", "", None, 0, "", "hockey"),
 ("hockey-ledovaya-druzhba-morozovo", "Ледовая дружба", "Москва, Новоостаповская ул., 5, стр. 2", "", None, 0, "", "hockey"),
 ("hockey-dp-coach-rus", "D. P. Hockey’s Coach", "Москва, Воронежская ул., 13", "", None, 0, "", "hockey"),
 ("hockey-bulldozer-megasport", "Bulldozer хоккей", "Москва, Ходынский бул., 3", "", None, 0, "", "hockey"),
 ("volley-evaivi-novokuznetskaya", "Эвайви спорт", "Москва, Новокузнецкая ул., 16, стр. 10", "", None, 0, "", "volleyball"),
 ("tt-tops-podolsk", "Топс настольный теннис", "Подольск, ул. Клемента Готвальда, 6В", "", None, 0, "", "tabletennis"),
 ("tt-krasny-kit-mytishchi", "Школа настольного тенниса Красный Кит", "Мытищи, Шараповский пр., вл2с3", "", None, 0, "", "tabletennis"),
]
if __name__ == "__main__":
    qp = os.path.join(ROOT, "auto", "osm-queries.json")
    qs = json.load(open(qp)); have = {q["id"] for q in qs}; fq = []
    for i, c in enumerate(C):
        if c[4]:
            q = {"id": "rare12r-" + c[0], "lat": c[4][0], "lon": c[4][1], "radius": c[5], "name": c[6]}
            if c[3]: q["street"] = c[3]
            if q["id"] not in have: qs.append(q)
        fq.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?r15b{i:02d}=1112r&text=" + u.quote(f"{c[1]}, {c[2]}"))
    json.dump(qs, open(qp, "w"), ensure_ascii=False, indent=1)
    open(os.path.join(ROOT, "auto", "fetch-queue.txt"), "a").write("\n".join(fq) + "\n")
    print(len(C), len(fq))
