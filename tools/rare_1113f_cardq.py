"""Робот rare 13.11 (1113f), шаг 2: карточки Яндекс Карт новых кандидатов из выдачи rr13k* (ключ rr13l<N>=1113f)
→ auto/fetch-queue.txt; справка OSM (rare13j-*) → auto/osm-queries.json.   python3 tools/rare_1113f_cardq.py"""
import json, os, urllib.parse as u
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
# id: (название в Яндексе, адрес, центр, радиус, имя для сверки OSM, улица OSM)
Q = {
 "volley-plotik-khimki": ("Школа волейбола Плотик", "Химки, ул. Кирова, с24", (55.8905, 37.437), 1500, "Плот", "Кирова"),
 "tt-lucentr-starokirochny": ("ЛуЦентр", "Москва, Старокирочный пер., 2", (55.771354, 37.678059), 300, "ЛуЦентр", "Старокирочный"),
 "volley-palma-vavilova": ("Palma volley club", "Москва, ул. Вавилова, 81, корп. 1", (55.6825, 37.546), 800, "Palma", "Вавилова"),
 "volley-panda-nagatinskaya": ("Панда Воллей", "Москва, Нагатинская ул., 16", (55.678579, 37.642326), 300, "Панда", "Нагатинская"),
 "volley-lav-nakhimovsky": ("Лав Волейбол", "Москва, Нахимовский просп., 4А", (55.672, 37.614), 1200, "Лав", "Нахимовский"),
 "tt-tekstilshchiki-saratovskaya": ("Настольный теннис ТТ Текстильщики", "Москва, Саратовская ул., 9с1", (55.7095, 37.735), 900, "теннис", "Саратовская"),
 "tt-fortuna-armavirskaya": ("Фортуна теннисный клуб", "Москва, Армавирская ул., 1/20", (55.6555, 37.7445), 1200, "Фортуна", "Армавирская"),
 "volley-leto-vostryakovskoe": ("Центр пляжных видов спорта Лето", "Москва, Востряковское ш., 7А", (55.597, 37.616), 2000, "Лето", "Востряковское"),
 "rink-olimpiysky-maksimova-chekhov": ("ДС Олимпийский им. В. С. Максимова, ледовый дворец", "Чехов, Московская ул., 104", (55.144, 37.47), 3000, "Ледов", "Московская"),
 "rink-armada-odintsovo": ("Ледовый дворец Армада", "Одинцово, Молодёжная ул., 15", (55.673, 37.268), 2500, "Армада", "Молодёжная"),
 "rink-arena-morozovo-mass": ("Арена Морозово", "Москва, Новоостаповская ул., 5, стр. 2", (55.72389636, 37.67736111), 300, "Морозово", "Новоостаповская"),
}
if __name__ == "__main__":
    lines, out = [], []
    for i, (pid, (nm, addr, c, r, mt, st)) in enumerate(Q.items()):
        lines.append("https://yandex.ru/maps/1/moscow-and-moscow-oblast/?rr13l%02d=1113f&text=%s" % (i, u.quote(nm + ", " + addr)))
        q = {"id": "rare13j-" + pid, "lat": c[0], "lon": c[1], "radius": r, "name": mt}
        if st: q["street"] = st
        out.append(q)
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in lines if l not in old]) + "\n")
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("rare13j-")]
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(out), len(lines))
