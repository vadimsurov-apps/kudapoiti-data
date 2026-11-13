"""Робот pools 13.11 (08 UTC), шаг 2: карточки Яндекс Карт новых кандидатов (ключ po<N>=1113h) → auto/fetch-queue.txt,
справка OSM (pl19-*) → auto/osm-queries.json.   python3 tools/pools_1113h_cardq.py"""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
# id: (название в Яндексе | None — карточка не нужна, адрес, центр, радиус, улица OSM, имя для сверки)
Q = {
 "ss1-lihobory": (None, "Москва, Дмитровское ш., 73Б", (55.85608, 37.556312), 350, "Дмитровское", "бассейн"),
 "ss1-fili-dvs": (None, "Москва, Большая Филёвская ул., 18", (55.748765, 37.498972), 300, "Филёвская", "бассейн"),
 "ss1-mgsu": (None, "Москва, Ярославское ш., 26, стр. 4", (55.8555, 37.696), 450, "Ярославское", "бассейн"),
 "ss1-mei": ("Школа плавания № 1", "Москва, Энергетический пр., 3, стр. 3", (55.75193, 37.71744), 400, "Энергетический", "бассейн"),
 "ss1-bauman": (None, "Москва, Госпитальная наб., 4, стр. 1", (55.77207, 37.697522), 300, "Госпитальная", "бассейн"),
 "ss1-serebryany": (None, "Москва, ул. Генерала Глаголева, 10, корп. 3", (55.781302, 37.466198), 300, "Глаголева", "Серебрян"),
 "ss1-fitnes-praktika": ("Фитнес Практика", "Москва, ул. Толбухина, 10, корп. 3", (55.7206, 37.4045), 500, "Толбухина", "Практика"),
 "ss1-odintsovo": ("Школа плавания № 1", "Одинцово, Молодёжная ул., 48", (55.6772, 37.2715), 600, "Молодёжная", "бассейн"),
 "ss1-zhavoronki": ("Школа плавания № 1", "Одинцовский округ, Жаворонки, Минское шоссе, 39-й километр, 2с5", (55.615207, 37.083526), 700, "Минское", "Жаворонки"),
 "mama-ya-plyvu-nagatinskaya": ("Мама, я плыву!", "Москва, Нагатинская ул., 16", (55.678579, 37.642326), 400, "Нагатинская", "плыву"),
 "kitik-veshnyakovskaya": ("Детский бассейн Китик", "Москва, Вешняковская ул., 12Ж", (55.7163, 37.8165), 500, "Вешняковская", "Китик"),
 "grudnichkovoe-gazoprovod": ("Грудничковое плавание", "Москва, посёлок Газопровод, 101А", (55.570016, 37.45805), 350, "Газопровод", "бассейн"),
 "chayka-gazoprovod": ("Чайка, бассейн", "Москва, посёлок Газопровод, 101А", (55.570016, 37.45805), 350, "Газопровод", "Чайка"),
 "morskie-zvezdy-kommunarka": ("Морские звезды", "Москва, посёлок Коммунарка, ул. Липовый Парк, 2", (55.57166, 37.492549), 400, "Липовый", "звезд"),
 "akvalider-kotlyakovsky": ("Аквалидер", "Москва, 1-й Котляковский пер., 4, корп. 2", (55.651932, 37.632266), 300, "Котляковский", "лидер"),
 "aqville-miklukho": ("Aqville", "Москва, ул. Миклухо-Маклая, 16/10к19", (55.646899, 37.509526), 400, "Миклухо-Маклая", "бассейн"),
 "aqua-yuna-life-pervomayskaya": ("Aqua Юна Life", "Москва, Первомайская ул., 42, корп. 1", (55.788746, 37.77889), 400, "Первомайская", "Юна"),
 "volna-uspekha-kosinskaya": ("Клуб синхронного плавания Волна Успеха", "Москва, Косинская ул., 12Б", (55.724794, 37.833585), 200, "Косинская", "бассейн"),
 "strong-swim-kosinskaya": ("Strong Swim", "Москва, Косинская ул., 12Б", (55.724794, 37.833585), 200, "Косинская", "бассейн"),
 "sssr-tkatskaya": ("СССР, фитнес-клуб", "Москва, Ткацкая ул., 5, стр. 1", (55.7877, 37.7215), 500, "Ткацкая", "СССР"),
 "swimclub-zemlyanoy-val": ("SwimClub", "Москва, ул. Земляной Вал, 71, стр. 2", (55.7455, 37.6545), 300, "Земляной", "бассейн"),
 "ss1-kolomensky": ("Школа плавания № 1", "Москва, Коломенский пр., 15А", (55.6625, 37.6535), 600, "Коломенский", "бассейн"),
 "ss1-zil": ("Школа плавания № 1", "Москва, Автозаводская ул., 23А, корп. 4", (55.7045, 37.6375), 500, "Автозаводская", "бассейн"),
 "ss1-korall": ("Школа плавания № 1", "Москва, 1-й Красносельский пер., 9", (55.7795, 37.6665), 500, "Красносельский", "Коралл"),
 "ss1-misis": ("Школа плавания № 1", "Москва, Профсоюзная ул., 83Б", (55.6435, 37.5255), 500, "Профсоюзная", "бассейн"),
 "plyvi-malysh-michurinsky": ("Плыви, малыш, детский бассейн", "Москва, Мичуринский просп., 16", (55.7005, 37.5075), 700, "Мичуринский", "малыш"),
 "akvaladushki-shagala": ("Акваладушки, детский бассейн", "Москва, наб. Марка Шагала, 11, корп. 3", (55.6935, 37.6335), 1200, "Марка Шагала", "ладушки"),
 "pyat-utyat-mozhayskoe": ("Пять утят, детский бассейн", "Москва, Можайское ш., 18, корп. 1", (55.7178, 37.4185), 900, "Можайское", "утят"),
}
SITES = ["https://mamayaplyvu.com/nagatinskaya", "https://mamayaplyvu.com/contacts", "https://swim-school-1.ru/basseyni/fitnespraktika",
         "https://swim-school-1.ru/ceny", "https://swim-school-1.ru/deti-3-6", "https://aqville.ru/price", "https://aqville.ru/schedule"]
OSMQ = ["ss1-lihobory", "ss1-fili-dvs", "ss1-mgsu", "ss1-mei", "ss1-bauman", "ss1-serebryany", "ss1-fitnes-praktika", "ss1-odintsovo",
        "ss1-zhavoronki", "mama-ya-plyvu-nagatinskaya", "kitik-veshnyakovskaya", "grudnichkovoe-gazoprovod",
        "morskie-zvezdy-kommunarka", "akvalider-kotlyakovsky", "aqville-miklukho", "sssr-tkatskaya"]
if __name__ == "__main__":
    lines, out = list(SITES), []
    for i, (pid, (nm, addr, c, r, st, match)) in enumerate(Q.items()):
        if nm:
            lines.append("https://yandex.ru/maps/1/moscow-and-moscow-oblast/?po%d=1113h&text=%s" % (i, urllib.parse.quote(nm + ", " + addr)))
        if pid in OSMQ:
            out.append({"id": "pl19-" + pid, "lat": c[0], "lon": c[1], "radius": r, "name": match, "street": st})
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in lines if l not in old]) + "\n")
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("pl19-")]
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(out), len(lines))
