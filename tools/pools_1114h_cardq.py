"""Робот pools 14.11 (08 UTC), шаг 2: карточки Яндекс Карт новых кандидатов (ключ po<N>=1114h) и сайты → auto/fetch-queue.txt,
справка OSM (pl30-*) → auto/osm-queries.json.   python3 tools/pools_1114h_cardq.py"""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
# id: (название в Яндексе, адрес в Яндексе, центр поиска, радиус, улица OSM, имя для сверки)
Q = {
 "mama-ya-plyvu-cheryomushki": ("Мама, я плыву!", "Москва, Новочерёмушкинская ул., 53А", (55.6725, 37.5610), 900, "Новочерёмушкинская", "плыву"),
 "kitik-veshnyakovskaya": ("Детский бассейн Китик", "Москва, Вешняковская ул., 12Ж", (55.7240, 37.8170), 900, "Вешняковская", "Китик"),
 "glubina-berzarina": ("Глубина", "Москва, ул. Берзарина, 32", (55.7860, 37.4620), 900, "Берзарина", "Глубина"),
 "grudnichkovoe-gazoprovod": ("Грудничковое плавание", "посёлок Газопровод, 101А", (55.5700, 37.4700), 2500, "", "Чайка"),
 "chayka-gazoprovod": ("Чайка", "посёлок Газопровод, 101А", None, 0, "", ""),
 "laguna-boba-borisovsky": ("Лагуна Боба", "Москва, Борисовский пр., 8/1", (55.6330, 37.7270), 1200, "Борисовский", "Лагуна"),
 "krya-kva-stupino": ("Кря-Ква", "Ступино, Приокский пер., 9", (54.8870, 38.0780), 4000, "Приокский", "Кря"),
 "olimp-kashira": ("Олимп", "Кашира, ул. Металлургов, 7, корп. 2", (54.8530, 38.2500), 6000, "Металлургов", "Олимп"),
 "yubileyny-kashira": ("Спортклуб Кашира имени Н.П. Елисеева Дворец спорта Юбилейный", "Кашира, Гвардейская ул., 3", (54.8340, 38.1520), 6000, "Гвардейская", "Юбилейный"),
 "sportshkola-lukhovitsy": ("Плавательный бассейн", "Луховицы, ул. Пушкина, 29", (54.9650, 39.0250), 4000, "Пушкина", "бассейн"),
 "akvarium-lukhovitsy": ("Аквариум", "Луховицы, Парковая ул., 1", (54.9651, 39.0251), 4000, "Парковая", "Аквариум"),
 "basseyn-mozhaysk": ("Бассейн", "Можайск, ул. Мира, 17", (55.5060, 36.0200), 3500, "Мира", "бассейн"),
 "viktoriya-mozhaysk": ("Виктория", "Можайск, ул. Мира, 15", None, 0, "", ""),
 "dvvs-ruza": ("Дворец водных видов спорта", "Руза, микрорайон Северный, 10", (55.7100, 36.2000), 3500, "", "водных"),
 "sshor-ruza": ("Спортивная школа олимпийского резерва по водным видам спорта", "Руза, микрорайон Северный, 10", None, 0, "", ""),
 "stary-gorodok": ("Старый городок, бассейн", "Старый Городок, Почтовая ул., 21", (55.6130, 36.7450), 4000, "Почтовая", "бассейн"),
 "atlant-taldom": ("Атлант", "Талдом, ул. З. Голицыной, 24", (56.7330, 37.5300), 3500, "Голицыной", "Атлант"),
 "ds-shatura": ("Дворец спорта Шатура", "Шатура, просп. Ильича, 65", (55.5770, 39.5400), 4000, "Ильича", "Дворец спорта"),
 "olimpiysky-shatura": ("Дворец спорта Олимпийский", "Шатура, ул. Клары Цеткин, 31", (55.5771, 39.5401), 4000, "Клары Цеткин", "Олимпийский"),
}
EXTRA = ["https://mamayaplyvu.com/contacts", "https://mamayaplyvu.com/filials", "https://mamayaplyvu.com/novye-cheremushki"]
if __name__ == "__main__":
    lines, out = list(EXTRA), []
    for i, (pid, (nm, addr, c, r, st, match)) in enumerate(Q.items()):
        lines.append("https://yandex.ru/maps/1/moscow-and-moscow-oblast/?po%d=1114h&text=%s" % (i, urllib.parse.quote(nm + ", " + addr)))
        if c:
            q = {"id": "pl30-" + pid, "lat": c[0], "lon": c[1], "radius": r, "name": match}
            if st: q["street"] = st
            out.append(q)
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in lines if l not in old]) + "\n")
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("pl30-")]
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(out), len(lines))
