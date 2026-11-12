"""Робот rare, 12.11 (03:45 UTC): кандидаты из выдачи Яндекс Карт (auto/pages, запросы r12y*-1112d) по районам
Коммунарка, Новомосковский, Бутово, Мосрентген, Крылатское, Крымская, Кузнецкий мост, Кузьминки, Кунцевская, Курская,
Кутузовская, Ленинский проспект, Лермонтовский проспект, Лесопарковая + тюбинг/склоны/театры зверей/памп-треки/сквош.
Генерирует запросы справки OSM (дописывает в auto/osm-queries.json) и строки для auto/fetch-queue.txt (карточки).
python3 tools/rare_1112d_cands.py"""
import json, os, re, urllib.parse as u
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
C = [
 ("hockey-mastera-mosfilmovskaya", "Мастера Хоккея", "Москва, Мосфильмовская ул., 41, корп. 3", "Мосфильмовская", "Минская", 2500, "Мастера", "hockey"),
 ("fk-ledyanye-krylya-ostafyevskaya", "Школа фигурного катания Ледяные Крылья", "Москва, Остафьевская ул., 21/1", "Остафьевская", "Бунинская аллея", 2500, "Монтреал", "figureskating"),
 ("rink-montreal-ostafyevskaya", "Монтреал", "Москва, Остафьевская ул., 21/1", "Остафьевская", "Бунинская аллея", 2500, "Монтреал", "rinks"),
 ("volley-rusvolley-elektrolitny-7", "Rusvolley", "Москва, Электролитный пр., 7, корп. 2, стр. 3", "Электролитный", "Нагорная", 2500, "", "volleyball"),
 ("volley-rusvolley-elektrolitny-3", "Rusvolley", "Москва, Электролитный пр., 3, стр. 33", "Электролитный", "Нагорная", 2500, "", "volleyball"),
 ("volley-rusvolley-moldavskaya", "Rusvolley", "Москва, Молдавская ул., 6, корп. 2", "Молдавская", "Кунцевская", 2500, "", "volleyball"),
 ("volley-alekseev-grodnenskaya", "Школа волейбола Станислава Алексеева", "Москва, Гродненская ул., 5", "Гродненская", "Кунцевская", 3000, "", "volleyball"),
 ("volley-alekseev-filevskaya", "Школа волейбола Станислава Алексеева", "Москва, Большая Филёвская ул., 32", "Филёвская", "Фили", 2500, "", "volleyball"),
 ("fk-razryad-filevsky", "Школа фигурного катания Разряд", "Москва, Филёвский бул., 38", "Филёвский", "Багратионовская", 2500, "Арена", "figureskating"),
 ("tt-serebryaniki", "Спортивный клуб в Серебрениках", "Москва, Серебрянический пер., 9", "Серебрянический", "Таганская", 2500, "", "tabletennis"),
 ("tt-ishanov-krasnoselskaya", "Школа настольного тенниса Али Ишанова", "Москва, Нижняя Красносельская ул., 40/12к4", "Красносельская", "Бауманская", 2500, "", "tabletennis"),
 ("hockey-edition-volgogradsky", "Хоккей Эдишен", "Москва, Волгоградский просп., 46/15с10", "Волгоградский", "Текстильщики", 3000, "", "hockey"),
 ("hockey-star-yunykh-lenintsev", "Hockey-star.ru", "Москва, ул. Юных Ленинцев, 52, стр. 2", "Юных Ленинцев", "Кузьминки", 2500, "", "hockey"),
 ("hockey-star-ryazansky", "Hockey-star.ru", "Москва, Рязанский просп., 4", "Рязанский", "Рязанский проспект", 4000, "", "hockey"),
 ("hockey-star-golubinskaya", "Hockey-star.ru", "Москва, Голубинская ул., 28, корп. 3", "Голубинская", "Новоясеневская", 2500, "Созвездие", "hockey"),
 ("trampoline-doaflip-khoroshevskaya", "Doaflip", "Москва, 3-я Хорошёвская улица", "Хорошёвская", "Полежаевская", 2500, "Doaflip", "trampolines"),
 ("fk-la-skadi-morozovo", "La Skadi", "Москва, Новоостаповская ул., 5, стр. 2", "Новоостаповская", "Дубровка", 2500, "", "figureskating"),
 ("volley-palma-vavilova", "Palma volley club", "Москва, ул. Вавилова, 81, корп. 1", "Вавилова", "Профсоюзная", 2500, "", "volleyball"),
 ("ski-chulkovo-academy", "Горнолыжная академия Чулково", "посёлок имени Тельмана, Курганная ул., 1", "Курганная", (55.6230, 38.1300), 6000, "Чулково", "ski"),
 ("fk-ice-pro-reutov", "Айс Про", "Реутов, Юбилейный просп., 43", "Юбилейный", "Новокосино", 3000, "", "figureskating"),
 ("tt-tennisko-letovo", "Тенниско", "д. Летово, Малая Летовская ул., 6", "Летовская", "Ольховая", 4000, "", "tabletennis"),
 ("squash-padlhab-sosenki", "Падлхаб", "д. Сосенки, Сосновая ул., 1Б", "Сосновая", "Коммунарка", 3000, "", "squash"),
 ("squash-1210", "Сквош-клуб 12:10", "Москва", "", "Кутузовская", 3000, "12:10", "squash"),
 ("rink-kommunarka", "Каток в Коммунарке", "Москва, Коммунарка", "", "Коммунарка", 3000, "Каток", "rinks"),
 ("hockey-dikie-tigry", "Дикие Тигры хоккей", "Москва", "", "Крылатское", 3000, "Тигр", "hockey"),
]
if __name__ == "__main__":
    sw = open(os.path.join(ROOT, "tools", "MetroStations.swift")).read()
    def st(n):
        m = re.search(r'"' + re.escape(n.lower()) + r'"\s*:\s*\("[^"]*",\s*([\d.]+),\s*([\d.]+)\)', sw)
        if not m: raise SystemExit("нет станции " + n)
        return float(m.group(1)), float(m.group(2))
    qp = os.path.join(ROOT, "auto", "osm-queries.json")
    qs = json.load(open(qp)); have = {q["id"] for q in qs}
    fq = []
    for i, c in enumerate(C):
        lat, lon = c[4] if isinstance(c[4], tuple) else st(c[4])
        q = {"id": "rare12d-" + c[0], "lat": lat, "lon": lon, "radius": c[5], "name": c[6]}
        if c[3]: q["street"] = c[3]
        if q["id"] not in have: qs.append(q)
        fq.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?r12z{i}=1112d&text=" + u.quote(f"{c[1]}, {c[2]}"))
    json.dump(qs, open(qp, "w"), ensure_ascii=False, indent=1)
    open("/tmp/r/fq2.txt", "w").write("\n".join(fq) + "\n")
    print(len(C))
