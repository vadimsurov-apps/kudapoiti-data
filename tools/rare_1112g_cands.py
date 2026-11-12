"""Робот rare, 12.11 (06:45 UTC): кандидаты из выдачи Яндекс Карт (auto/pages, запросы r13a*-1112g) по районам
Лубянка, Марьина Роща, Видное, Воскресенск, Маяковская, Медведково, Международная, Менделеевская, Минская, Митино,
Мичуринский проспект, Мнёвники, Молодёжная, Мякинино (каток / хоккей / фигурное / настольный теннис / волейбол / скалодром)
+ массовое катание в ледовых дворцах (в базе они есть только как секции). Пишет запросы справки OSM (auto/osm-queries.json)
и карточки в /tmp/r/fq.txt. python3 tools/rare_1112g_cands.py"""
import json, os, re, urllib.parse as u
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
VID = (55.5520, 37.7080); VOS = (55.3230, 38.6750)
C = [
 ("climb-limestone-dobroslobodskaya", "ЛаймСтоун скалодром", "Москва, Доброслободская ул., 21", "Доброслободская", "Бауманская", 2500, "", "climbing"),
 ("climb-garm-glagoleva", "Гарм скалодром", "Москва, ул. Генерала Глаголева, 19", "Генерала Глаголева", "Народное Ополчение", 2500, "Гарм", "climbing"),
 ("fk-angely-plyushchenko-molodenovo", "Ангелы Плющенко", "Одинцовский г. о., д. Молоденово, Речная ул., 19", "Речная", (55.7400, 37.1700), 5000, "Плющенко", "figureskating"),
 ("tt-raketlon-lobachevskogo", "Ракетлон", "Москва, ул. Лобачевского, 138, стр. 2", "Лобачевского", (55.6650, 37.4700), 3500, "Ракетлон", "tabletennis"),
 ("fk-bulycheva-vidnoe", "Bulycheva Team", "Видное, Старо-Нагорная ул., 20В", "Старо-Нагорная", VID, 4000, "", "figureskating"),
 ("rink-vidny-sport", "Видный спорт", "Видное, Старо-Нагорная ул., 20В", "Старо-Нагорная", VID, 4000, "Видный", "rinks"),
 ("hockey-sport-vsegda-vidnoe", "Спорт всегда хоккей", "Видное, Зелёный пер., с10", "Зелёный", VID, 4000, "Арктика", "hockey"),
 ("fk-art-ice-vidnoe", "Спортивный балет на льду Art&ice", "Видное, Зелёный пер., с10", "Зелёный", VID, 4000, "Арктика", "figureskating"),
 ("hockey-broskovaya-voskresensk", "Бросковая зона Воскресенск", "Воскресенск, Лопатинская ул., 9", "Лопатинская", VOS, 4000, "", "hockey"),
 ("rink-kamenskogo-voskresensk", "Ледовая арена имени В.В. Каменского", "Воскресенск, ул. Менделеева, 2/1", "Менделеева", VOS, 4000, "Каменского", "rinks"),
 ("hockey-star-sportivnoy-aviatsii", "Hockey-star.ru", "Москва, ул. Спортивной Авиации, 3", "Спортивной Авиации", "Спартак", 2500, "", "hockey"),
 ("rink-mitino-ice-arena", "Митино айс арена массовое катание", "Москва, Дубравная ул., 51, стр. 1", "Дубравная", "Пятницкое шоссе", 2500, "Митино", "rinks"),
 ("rink-pingviny-bulatnikovskaya", "Пингвины массовое катание", "Москва, Булатниковская ул., 2Б", "Булатниковская", "Улица Академика Янгеля", 3000, "Пингвин", "rinks"),
 ("rink-serebryany-glagoleva", "Серебряный массовое катание", "Москва, ул. Генерала Глаголева, 10, корп. 3", "Генерала Глаголева", "Народное Ополчение", 2500, "Серебряный", "rinks"),
 ("rink-apia-arena", "Апиа Арена массовое катание", "Москва, ул. Яблочкова, 7", "Яблочкова", "Тимирязевская", 2500, "Апиа", "rinks"),
 ("rink-arena-play-sever", "Арена Плей Север массовое катание", "Москва, Ботаническая ул., 2, стр. 1", "Ботаническая", "Владыкино", 3500, "Арена", "rinks"),
 ("rink-akademiya-lda-streletsky", "Академия льда", "Москва, 1-й Стрелецкий пр., 14", "Стрелецкий", (55.7940, 37.5880), 2500, "Академия льда", "rinks"),
 ("rink-chempion-yuzhnoportovy", "Чемпион каток", "Москва, 2-й Южнопортовый пр., 2", "Южнопортовый", "Кожуховская", 2500, "Чемпион", "rinks"),
 ("rink-medvedkovo-zapovednaya", "Ледовый дворец Медведково массовое катание", "Москва, Заповедная ул., 3", "Заповедная", (55.8880, 37.6390), 2500, "Медведково", "rinks"),
 ("rink-molodezhka-kuntsevo", "Молодёжка ледовый дворец Кунцево", "Москва", "", "Кунцевская", 4000, "Молодёжка", "rinks"),
]
GEN = ["массовое катание ледовый дворец Москва", "массовое катание ледовая арена Московская область", "тюбинг Москва",
       "тюбинг Московская область", "горнолыжная школа для детей Москва", "горнолыжный склон Московская область",
       "сквош для детей Москва", "театр зверей", "памп-трек Московская область", "цирк шапито Москва",
       "настольный теннис для детей Московская область", "хоккейная школа для детей Московская область",
       "фигурное катание для детей Московская область", "каток в парке Москва"]
import sys as _s
if __name__ == "__main__":
    sw = open(os.path.join(ROOT, "tools", "MetroStations.swift")).read()
    def st(n):
        m = re.search(r'"' + re.escape(n.lower()) + r'"\s*:\s*\("[^"]*",\s*([\d.]+),\s*([\d.]+)\)', sw)
        if not m: raise SystemExit("нет станции " + n)
        return float(m.group(1)), float(m.group(2))
    qp = os.path.join(ROOT, "auto", "osm-queries.json")
    qs = json.load(open(qp)); have = {q["id"] for q in qs}
    fq = []
    for i, c in enumerate(C if "2" not in _s.argv else []):
        lat, lon = c[4] if isinstance(c[4], tuple) else st(c[4])
        q = {"id": "rare12g-" + c[0], "lat": lat, "lon": lon, "radius": c[5], "name": c[6]}
        if c[3]: q["street"] = c[3]
        if q["id"] not in have: qs.append(q)
        fq.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?r13b{i:02d}=1112g&text=" + u.quote(f"{c[1]}, {c[2]}"))
    for i, t in enumerate(GEN if "2" not in _s.argv else []):
        fq.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?r13c{i:02d}=1112g&text=" + u.quote(t))
    json.dump(qs, open(qp, "w"), ensure_ascii=False, indent=1)
    open("/tmp/r/fq.txt", "w").write("\n".join(fq) + "\n")
    print(len(C), len(fq))
C2 = [
 ("rink-vityaz-podolsk", "Ледовый дворец Витязь массовое катание", "Подольск, ул. Кирова, 63А", "Кирова", (55.4300, 37.5300), 4000, "Витязь", "rinks"),
 ("hockey-biryukov-dolgoprudny", "Хоккейная академия Бирюкова", "Долгопрудный, просп. Ракетостроителей, 4", "Ракетостроителей", (55.9380, 37.5100), 4000, "", "hockey"),
 ("hockey-sshor-mytishchi", "Спортивная школа олимпийского резерва по хоккею Мытищи", "Мытищи, Лётная ул., 17", "Лётная", (55.9150, 37.7500), 4000, "", "hockey"),
 ("hockey-pro-hockey-soloslovo", "Хоккейная школа Pro Hockey", "Одинцовский г. о., д. Солослово, КП Резиденции Берёзки, 314", "", (55.7200, 37.1900), 5000, "", "hockey"),
 ("rink-arena-morozovo", "Арена Морозово массовое катание", "Москва, Новоостаповская ул., 5, стр. 2", "Новоостаповская", "Дубровка", 2500, "Морозово", "rinks"),
]
if __name__ == "__main__" and "2" in __import__("sys").argv:
    qs = json.load(open(qp)); have = {q["id"] for q in qs}; fq = []
    for i, c in enumerate(C2):
        lat, lon = c[4] if isinstance(c[4], tuple) else st(c[4])
        q = {"id": "rare12g-" + c[0], "lat": lat, "lon": lon, "radius": c[5], "name": c[6]}
        if c[3]: q["street"] = c[3]
        if q["id"] not in have: qs.append(q)
        fq.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?r13d{i:02d}=1112g&text=" + u.quote(f"{c[1]}, {c[2]}"))
    json.dump(qs, open(qp, "w"), ensure_ascii=False, indent=1)
    open("/tmp/r/fq.txt", "w").write("\n".join(fq) + "\n")
