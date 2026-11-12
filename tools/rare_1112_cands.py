"""Робот rare, 12.11 (00 UTC): кандидаты из выдачи Яндекс Карт (auto/pages, запросы r12x*-1112a) по районам
ЗИЛ … Кропоткинская + тюбинг/склоны/скалодромы. Генерирует auto/osm-queries.json (центр — станция метро/город)
и строки для auto/fetch-queue.txt (точный поиск карточки). python3 tools/rare_1112_cands.py"""
import json, os, re, urllib.parse as u
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
# id, название для поиска, адрес (как в Яндексе), улица-фильтр, центр (станция или (lat,lon)), радиус, имя для OSM, категория
C = [
 ("hockey-rus-mha-zyablikovo", "Ледовый центр Русь Московской академии хоккея", "Москва, Воронежская ул., 13", "Воронежская", "Зябликово", 2500, "Русь", "hockey"),
 ("hockey-star-kosino", "Hockey-star.ru", "Москва, Новоухтомское ш., 2А", "Новоухтомское", "Косино", 2500, "Город", "hockey"),
 ("hockey-star-molochny", "Hockey-star.ru", "Москва, Молочный пер., 1", "Молочный", "Парк культуры", 2500, "", "hockey"),
 ("hockey-kharlamov-sokolniki", "Академия хоккея имени Валерия Харламова", "Москва, ул. Сокольнический Вал, 1Б", "Сокольнический Вал", "Сокольники", 2500, "Ледовый дворец", "hockey"),
 ("hockey-champion-sokolniki", "Хоккейный клуб Чемпион", "Москва, ул. Сокольнический Вал, 1Б", "Сокольнический Вал", "Сокольники", 2500, "Чемпион", "hockey"),
 ("fk-vselenskiy-led", "Вселенский Лед", "Москва, Большая Тихоновская ул., 2", "Тихоновская", "Ботанический сад", 3000, "Спартак", "figureskating"),
 ("fk-volosozhar-sokolniki", "Центр фигурного катания Татьяны Волосожар", "Москва, ул. Сокольнический Вал, 1Б, стр. 2", "Сокольнический Вал", "Сокольники", 2500, "Волосожар", "figureskating"),
 ("fk-ice-fenix-sokolniki", "Клуб фигурного катания Ice Fenix", "Москва, ул. Сокольнический Вал, 1Б", "Сокольнический Вал", "Сокольники", 2500, "Fenix", "figureskating"),
 ("fk-morozovo-school", "Школа фигурного катания Морозово", "Москва, Новоостаповская ул., 5, стр. 2", "Новоостаповская", "Дубровка", 2500, "Морозово", "figureskating"),
 ("rink-mayak-yasenevo", "Каток Маяк", "Москва, ул. Красного Маяка, вл28", "Красного Маяка", "Пражская", 2500, "Маяк", "rinks"),
 ("rink-snegir-arena", "Снегирь Арена", "д. Марушкино, 2", "", (55.600, 37.265), 6000, "Снегирь", "rinks"),
 ("rink-kasatonov-korolev", "Ледовая арена имени А. В. Касатонова", "Королёв, Октябрьский бул., 10, стр. 1", "Октябрьский", (55.9162, 37.8545), 4000, "Касатонов", "rinks"),
 ("volley-sunvolley-novokuznetskaya", "SunVolley", "Москва, Новокузнецкая ул., 16, стр. 10", "Новокузнецкая", "Павелецкая", 2500, "SunVolley", "volleyball"),
 ("volley-krokodil-sokolniki", "Пляжный центр Крокодил", "Москва, ул. Сокольнический Вал, 1Б, стр. 4", "Сокольнический Вал", "Сокольники", 2500, "Крокодил", "volleyball"),
 ("volley-panda-nagatinskaya", "Панда Воллей", "Москва, Нагатинская ул., 16", "Нагатинская", "Нагатинская", 2500, "Панда", "volleyball"),
 ("volley-nevskie-novorogozhskaya", "Невские медведи", "Москва, Новорогожская ул., 5", "Новорогожская", "Римская", 2500, "Невские", "volleyball"),
 ("volley-rusvolley-zoologicheskaya", "Rusvolley", "Москва, Зоологическая ул., 28, стр. 1", "Зоологическая", "Баррикадная", 2500, "", "volleyball"),
 ("volley-rusvolley-krasina", "Rusvolley", "Москва, ул. Красина, 20, стр. 1", "Красина", "Маяковская", 2500, "", "volleyball"),
 ("volley-rusvolley-ukrainsky", "Rusvolley", "Москва, Украинский бул., 9", "Украинский", "Киевская", 2500, "", "volleyball"),
 ("volley-rusvolley-bakhrushina", "Rusvolley", "Москва, ул. Бахрушина, 24, стр. 1", "Бахрушина", "Павелецкая", 2500, "", "volleyball"),
 ("volley-rusvolley-dubininskaya", "Rusvolley", "Москва, Дубининская ул., 42", "Дубининская", "Павелецкая", 2500, "", "volleyball"),
 ("volley-rusvolley-krasnoselskaya", "Rusvolley", "Москва, Верхняя Красносельская ул., 30", "Красносельская", "Красносельская", 2500, "", "volleyball"),
 ("volley-rusvolley-saltykovskaya", "Rusvolley", "Москва, Салтыковская ул., вл49", "Салтыковская", "Новокосино", 3000, "", "volleyball"),
 ("tt-lucentr-baumanskaya", "ЛуЦентр", "Москва, Старокирочный пер., 2", "Старокирочный", "Бауманская", 2500, "ЛуЦентр", "tabletennis"),
 ("tt-novoryazanskaya", "Настольный теннис", "Москва, Новорязанская ул., 23, стр. 1", "Новорязанская", "Бауманская", 2500, "", "tabletennis"),
 ("sled-chernevskaya-gorka", "Черневская горка", "Красногорск, улица Карбышева", "Карбышева", (55.815, 37.345), 4000, "Черневская", "sledding"),
 ("ski-rodina-skhodnya", "Горнолыжная база СК Родина", "Химки, микрорайон Сходня, Овражная ул., 35", "Овражная", (55.946, 37.300), 4000, "Родина", "ski"),
 ("climb-tengus-sushchevsky", "Тенгус", "Москва, ул. Сущёвский Вал, 49", "Сущёвский", "Марьина Роща", 2500, "Tengu", "climbing"),
 ("climb-limestone-dobroslobodskaya", "ЛаймСтоун", "Москва, Доброслободская ул., 21", "Доброслободская", "Бауманская", 2500, "", "climbing"),
]
if __name__ == "__main__":
    sw = open(os.path.join(ROOT, "tools", "MetroStations.swift")).read()
    def st(n):
        m = re.search(r'"' + re.escape(n.lower()) + r'"\s*:\s*\("[^"]*",\s*([\d.]+),\s*([\d.]+)\)', sw)
        if not m: raise SystemExit("нет станции " + n)
        return float(m.group(1)), float(m.group(2))
    qs, fq = [], []
    for i, c in enumerate(C):
        lat, lon = c[4] if isinstance(c[4], tuple) else st(c[4])
        q = {"id": "rare12-" + c[0], "lat": lat, "lon": lon, "radius": c[5], "name": c[6]}
        if c[3]: q["street"] = c[3]
        qs.append(q)
        fq.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?r12c{i}=1112b&text=" + u.quote(f"{c[1]}, {c[2]}"))
    json.dump(qs, open(os.path.join(ROOT, "auto", "osm-queries.json"), "w"), ensure_ascii=False, indent=1)
    open("/tmp/r/fq.txt", "w").write("\n".join(fq) + "\n")
    print(len(qs))
