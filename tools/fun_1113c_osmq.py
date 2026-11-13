"""Робот fun 1113c: справки OSM по кандидатам (координаты дома из Яндекс Карт, fwe-*-1113c) → auto/osm-queries.json;
третий набор районов (fwa<N>-1113e) и сайты мест → auto/fetch-queue.txt."""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q = [("fortb-novok", 55.884969, 37.407196, "Форт Боярд"), ("fortb-dd", 55.564053, 37.570941, "Форт Боярд"),
     ("hahashow", 55.767671, 37.678819, "Ха-ха"), ("banger", 55.888296, 37.588683, "Бэнгер"),
     ("grand", 55.886645, 37.436625, "Гранд"), ("tsvet", 55.771160, 37.620079, "Цветной"),
     ("konyashin", 55.782800, 38.437060, "Коняшина"), ("pikselek", 55.799279, 38.437644, "Пикселек"),
     ("trimetly", 55.081869, 38.757534, "Три метлы"), ("nerealnost", 55.664563, 37.627310, "Нереальность"),
     ("exitmania", 56.008420, 37.842582, "Exitmania"), ("fortb-bagr", 55.743654, 37.508131, "Форт Боярд"),
     ("kvestinfo", 55.666817, 37.627669, "Квестинфо")]
SITES = ["https://el-museum.ru/", "https://pixelek.ru/", "https://kvestkolomna.ru/", "https://nerealnostvr.ru/",
         "https://www.kvestinfo.ru/", "https://butovo-fb.kvest-show.ru/", "https://hahashow.ru/kvesty"]
if __name__ == "__main__":
    qp = os.path.join(ROOT, "auto/osm-queries.json")
    oq = json.load(open(qp))
    have = {x["id"] for x in oq}
    oq += [{"id": f"fun-1113c-{k}", "lat": la, "lon": lo, "radius": 300, "name": n} for k, la, lo, n in Q
           if f"fun-1113c-{k}" not in have]
    json.dump(oq, open(qp, "w"), ensure_ascii=False, indent=1)
    A = json.load(open(os.path.join(ROOT, "auto/search-areas.json")))
    P = json.load(open(os.path.join(ROOT, "auto/search-progress-fun.json")))
    used = json.load(open(os.path.join(ROOT, "tools/fun_1113c_queries.json")))["areas"] + \
        json.load(open(os.path.join(ROOT, "tools/fun_1113d_queries.json")))["areas"]
    T = ["детский развлекательный центр", "квест для детей", "мастер-класс для детей", "музей для детей", "детская игровая комната"]
    metro = [x for x in A["metro"] if P.get(x, "") <= "2026-11-11" and x not in used][:12]
    towns = [x for x in A["towns"] if P.get(x, "") <= "2026-11-11" and x not in used][:3]
    QQ = []
    for i, a in enumerate(metro + towns):
        for k in range(3):
            t = T[(3 * i + k + 3) % 5]
            QQ.append({"area": a, "theme": t, "text": f"{t} метро {a}" if a in metro else f"{t} {a}"})
    json.dump({"areas": metro + towns, "q": QQ}, open(os.path.join(ROOT, "tools/fun_1113e_queries.json"), "w"), ensure_ascii=False, indent=0)
    base = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?"
    urls = [f"{base}fwa{n}=1113e&text=" + urllib.parse.quote(q["text"]) for n, q in enumerate(QQ)] + SITES
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(metro + towns, len(urls))
