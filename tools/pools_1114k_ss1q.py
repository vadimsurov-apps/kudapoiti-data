"""Робот pools 14.11 (11 UTC), шаг 3: Школа плавания № 1 — бассейны из полного списка на страницах swim-school-1.ru/basseyni/*
(блок «Название ( адрес )»), которых нет в базе: карточки Яндекс Карт (ключ ps<N>=1114k), страницы бассейнов сайта (адреса
страниц подобраны по образцу известных: lujniki, javoronki, serebryanniy…) → auto/fetch-queue.txt; справка OSM (pl33-*) —
там, где по этому адресу в базе нет места с точкой.   python3 tools/pools_1114k_ss1q.py"""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
# id: (адрес для Яндекса, варианты адреса страницы, центр OSM | None, радиус, улица)
Q = {
 "ss1-obraztsova": ("Москва, ул. Образцова, 11, стр. 4", ["evreyskiy-centr", "evreyskiy-center", "obrazcova"], None, 0, ""),
 "ss1-kolomensky": ("Москва, Коломенский пр., 15А", ["kolomenskiy", "kolomensky"], (55.6690, 37.6620), 1500, "Коломенский"),
 "ss1-krasny-oktyabr": ("Москва, Тушинская ул., 16А", ["krasniy-oktyabr", "krasnyi-oktyabr", "krasniyoktyabr", "krasny-oktyabr"], None, 0, ""),
 "ss1-mgpu": ("Москва, ул. Касаткина, 23", ["mgpu"], None, 0, ""),
 "ss1-mgusit": ("Москва, ул. Лескова, 25А", ["mgusit"], (55.8950, 37.6030), 1200, "Лескова"),
 "ss1-mgyua": ("Москва, Бакунинская ул., 13, стр. 1", ["mgua", "mgyua"], None, 0, ""),
 "ss1-miit": ("Москва, Новосущёвская ул., 24, стр. 1", ["miit"], (55.7880, 37.6030), 900, "Новосущёвская"),
 "ss1-motsvs": ("Москва, ул. Ибрагимова, 32", ["mocvs", "motsvs"], (55.7890, 37.7350), 900, "Ибрагимова"),
 "ss1-meridian": ("Москва, Рязанский просп., 7, корп. 3", ["meridian"], (55.7290, 37.7480), 900, "Рязанский"),
 "ss1-mosgu": ("Москва, ул. Юности, 5, стр. 32", ["mosgu"], None, 0, ""),
 "ss1-nadezhda-krupskoy": ("Москва, ул. Крупской, 1, корп. 1", ["nadejda", "nadezhda"], (55.6880, 37.5300), 900, "Крупской"),
 "ss1-nekrasovka": ("Москва, Покровская ул., 22", ["nekrasovka"], None, 0, ""),
 "ss1-neptun-federativny": ("Москва, Федеративный просп., 8А, стр. 1", [], None, 0, ""),
 "ss1-nika-volzhsky": ("Москва, Волжский бул., 8А", ["nika"], None, 0, ""),
 "ss1-otssp": ("Москва, Автозаводская ул., 23А, корп. 4", ["ocsp", "otssp"], None, 0, ""),
 "ss1-orekhovo-borisovo": ("Москва, Ореховый пр., 43А", ["orehovo-borisovo", "orehovo"], (55.6090, 37.7290), 1200, "Ореховый"),
 "ss1-park-pobedy": ("Москва, ул. Барклая, 6, стр. 5", ["park-pobedy", "parkpobedy"], None, 0, ""),
 "ss1-profsoyuznaya": ("Москва, Новочерёмушкинская ул., 53А", ["profsoyuznaya", "profsouznaya"], (55.6740, 37.5600), 900, "Новочерёмушкинская"),
 "ss1-ranhigs": ("Москва, просп. Вернадского, 82, стр. 3", ["ranhigs", "ranhigs-na-vernadskogo"], (55.6650, 37.4800), 900, "Вернадского"),
 "ss1-rgufk": ("Москва, Сиреневый бул., 2", ["rgufk"], None, 0, ""),
 "ss1-reu-plekhanova": ("Москва, Большой Строченовский пер., 10", ["reu", "reu-plehanova", "plehanova"], (55.7275, 37.6290), 600, "Строченовский"),
 "ss1-ramenki": ("Москва, ул. Раменки, 19, стр. 1", ["ramenki"], (55.6930, 37.4950), 900, "Раменки"),
 "ss1-severny": ("Москва, ул. Арсюкова, 11", ["severniy", "severny", "severnyy"], None, 0, ""),
 "ss1-sila-soobshchestv": ("Москва, Лазоревый пр., 7", ["sila-soobshestv", "silasoobshestv", "sila-soobschestv"], None, 0, ""),
 "ss1-sokolniki": ("Москва, Большая Тихоновская ул., 18, стр. 1", ["sokolniki"], (55.8090, 37.6890), 1200, "Тихоновская"),
 "ss1-soyuz": ("Москва, ул. Тёплый Стан, 9, корп. 9", ["soyuz", "souz"], None, 0, ""),
 "ss1-stalnoy": ("Москва, ул. Павла Корчагина, 7/1", ["stalnoy"], None, 0, ""),
 "ss1-filevsky-maly": ("Москва, Береговой пр., 5, корп. 4", ["filevskiy-maliy", "filevskiy", "filevskiy-malyy"], None, 0, ""),
 "ss1-forum-khimki": ("Химки, ул. Кудрявцева, 23", ["forum"], (55.8920, 37.4490), 2500, "Кудрявцева"),
 "ss1-khovrino": ("Москва, ул. Маршала Федоренко, 12А", ["hovrino", "khovrino"], (55.8720, 37.5020), 1200, "Маршала Федоренко"),
 "ss1-chayka-turchaninov": ("Москва, Турчанинов пер., 3, стр. 1", ["chayka", "chaika"], None, 0, ""),
 "ss1-chaykovsky": ("Москва, Малая Грузинская ул., 24, корп. 3", ["chaykovskiy", "chaikovskiy", "chaykovsky"], (55.7680, 37.5750), 700, "Малая Грузинская"),
 "ss1-yantar": ("Москва, ул. Маршала Катукова, 22", ["yantar"], None, 0, ""),
 "ss1-mts-luzhniki": ("Москва, Новолужнецкий пр., 13", ["mcs-lujniki", "mcs"], None, 0, ""),
 "ss1-krylatskoe-ostrovnaya": ("Москва, Островная ул., 1, стр. 1", ["krylatskoe", "krilatskoe"], (55.7680, 37.4340), 1500, ""),
}
SITES = ["https://xn--5-jtbxgj8a.xn--p1ai/", "https://kidsfunclub.ru/", "https://na-volne.su/", "https://artisticsport.ru/",
         "https://swimming-krylatskoe.tilda.ws/", "https://dss-pp.ru/", "https://dush-lp.edumsko.ru/", "https://basseyn-volna.ru/",
         "https://okeanika-swim.com/", "https://www.mevis-1.ru/", "https://swim-school-1.ru/grudnichkovoe-plavanie"]
if __name__ == "__main__":
    lines, out = list(SITES), []
    for i, (pid, (addr, slugs, c, r, st)) in enumerate(Q.items()):
        lines.append("https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ps%d=1114k&text=%s" % (i, urllib.parse.quote("Школа плавания № 1, " + addr)))
        lines += ["https://swim-school-1.ru/basseyni/" + s for s in slugs]
        if c:
            q = {"id": "pl33-" + pid, "lat": c[0], "lon": c[1], "radius": r, "name": "бассейн"}
            if st: q["street"] = st
            out.append(q)
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in lines if l not in old]) + "\n")
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = json.load(open(p)); have = {x["id"] for x in old}
    json.dump(old + [q for q in out if q["id"] not in have], open(p, "w"), ensure_ascii=False, indent=1)
    print(len(out), len(lines))
