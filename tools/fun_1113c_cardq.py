"""Робот fun 1113c: карточки организаций Яндекса для кандидатов (fwd-<ключ>-1113c), комнаты матери и ребёнка в ТРЦ с
названием ТРЦ (fwg-<ключ>-1113c), часы ТРЦ (fwh-<ключ>-1113c) и второй набор районов (fwa<N>-1113d) → auto/fetch-queue.txt;
справки OSM по ТРЦ → auto/osm-queries.json."""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
D = {
 "fortb-bagr": "Fort Boyard квест, Москва, Багратионовский пр., 5", "fortb-novok": "Fort Boyard квест, Москва, Новокуркинское ш., 1",
 "nightkids": "Автоквесты Night Kids, Москва, Новозаводская ул., 27", "exitmania": "Exitmania, Пушкино, Писаревская ул., 5",
 "kvestkinder": "Квесткиндер, Москва, Гостиничный пр., 6, корп. 2", "hahashow": "Ха-ха Шоу, Москва, Бауманская ул., 58, стр. 4",
 "banger": "Шоу-плейс Бэнгер, Москва, Алтуфьевское ш., 70, корп. 1", "spacekids": "Space Kids, Красногорск, Парковая ул., 8А",
 "gigavriki": "Гигаврики, Красногорск, Международная ул., 12", "zeexar": "Zeexar VR, Люберцы, ул. 8 Марта, 12, корп. 1",
 "galaktika": "Галактика мастер-классы, Москва, Новозаводская ул., 2к6-7", "tinochka": "Арт Тиночка, Москва, ул. Мусоргского, 3",
 "pekan": "Пекан мастер-классы, Москва, ул. Островитянова, 18", "artlab": "АртЛаб, Мытищи, Олимпийский просп., 13с1",
 "tiza": "Арт Студия Tiza, Люберцы, 116-й квартал, к20А", "galerka": "Галёрка мастер-классы, Люберцы, Октябрьский просп., 193",
 "picasso": "Пикассо мастер-классы, Москва, Гончарная ул., 26, корп. 1",
}
G = {"iyun": "Комната матери и ребенка, ТРЦ Июнь, Мытищи, ул. Мира, 51", "megabd": "Комната матери и ребенка, МЕГА Белая Дача, Котельники",
     "kashpl": "Комната матери и ребенка, Каширская Плаза, Каширское ш., 61Г", "kaleid": "Комната матери и ребенка, Калейдоскоп, Сходненская ул., 56",
     "vesna": "Комната матери и ребенка, ТРЦ Весна, Алтуфьевское шоссе", "zelen": "Комната матери и ребенка, Зеленопарк, Ржавки",
     "xl": "Комната матери и ребенка, XL, Мытищи, Коммунистическая ул., 1", "otrada": "Комната матери и ребенка, ТРЦ Отрада, Пятницкое ш.",
     "tsvet": "Комната матери и ребенка, Цветной, Цветной бул., 15", "atrium": "Комната матери и ребенка, Атриум, ул. Земляной Вал, 33",
     "metrop": "Комната матери и ребенка, Метрополис, Ленинградское ш., 16А", "butovo": "Комната матери и ребенка, Бутово Молл, Чечёрский пр., 51",
     "semen": "Комната матери и ребенка, ТРЦ Семёновский, Большая Семёновская ул., 16"}
H = {"rio-len": "РИО торговый центр, Москва, Ленинский просп., 109", "novomosk": "Новомосковский торговый центр, Московский, ул. Хабарова, 2",
     "grand": "Гранд торговый центр, Химки, ул. Бутаково, 4"}
OSMQ = [("fun-1113c-rio-len", 55.6634, 37.5107, 250, "РИО"), ("fun-1113c-grand", 55.8885, 37.4410, 900, "Гранд")]
if __name__ == "__main__":
    A = json.load(open(os.path.join(ROOT, "auto/search-areas.json")))
    P = json.load(open(os.path.join(ROOT, "auto/search-progress-fun.json")))
    first = json.load(open(os.path.join(ROOT, "tools/fun_1113c_queries.json")))["areas"]
    T = ["детский развлекательный центр", "квест для детей", "мастер-класс для детей", "музей для детей", "детская игровая комната"]
    metro = [x for x in A["metro"] if P.get(x, "") <= "2026-11-11" and x not in first][:12]
    towns = [x for x in A["towns"] if P.get(x, "") <= "2026-11-11" and x not in first][:3]
    Q = []
    for i, a in enumerate(metro + towns):
        for k in range(3):
            t = T[(3 * i + k + 2) % 5]
            Q.append({"area": a, "theme": t, "text": f"{t} метро {a}" if a in metro else f"{t} {a}"})
    json.dump({"areas": metro + towns, "q": Q}, open(os.path.join(ROOT, "tools/fun_1113d_queries.json"), "w"), ensure_ascii=False, indent=0)
    base = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?"
    urls = [f"{base}fwd-{k}=1113c&text=" + urllib.parse.quote(v) for k, v in D.items()]
    urls += [f"{base}fwg-{k}=1113c&text=" + urllib.parse.quote(v) for k, v in G.items()]
    urls += [f"{base}fwh-{k}=1113c&text=" + urllib.parse.quote(v) for k, v in H.items()]
    urls += [f"{base}fwa{n}=1113d&text=" + urllib.parse.quote(q["text"]) for n, q in enumerate(Q)]
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    qp = os.path.join(ROOT, "auto/osm-queries.json")
    oq = json.load(open(qp))
    oq += [{"id": i, "lat": la, "lon": lo, "radius": r, "name": n} for i, la, lo, r, n in OSMQ]
    json.dump(oq, open(qp, "w"), ensure_ascii=False, indent=1)
    print(metro + towns, len(urls))
