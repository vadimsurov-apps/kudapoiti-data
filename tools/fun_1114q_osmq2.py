"""Робот fun 1114q, круг 3: кандидаты OSM — театры, кино (карточки Яндекс Карт рядом с объектом, fqt-<n>-1114q) → auto/fetch-queue.txt;
список → tools/fun_1114q_osm2.json."""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PICK = ["way/220594547", "node/13272958452", "node/3737822327", "node/5812677558", "node/3441521464", "node/1037207428",
        "node/6183553286", "node/13019032534", "node/690549518", "way/28852204", "node/14184832265", "node/7814702187",
        "way/355513093", "node/11237099040", "way/1071544815", "node/10146665550", "way/276532981"]
if __name__ == "__main__":
    C = {c["osm"]: c for c in json.load(open(os.path.join(ROOT, "auto/candidates.json")))["candidates"]}
    L = [C[o] for o in PICK]
    json.dump(L, open(os.path.join(ROOT, "tools/fun_1114q_osm2.json"), "w"), ensure_ascii=False, indent=0)
    base = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?"
    urls = [f"{base}fqt-{n}=1114q&ll={c['lon']:.4f}%2C{c['lat']:.4f}&z=17&text=" + urllib.parse.quote(c["name"].replace('"', ''))
            for n, c in enumerate(L)]
    urls += [base + "fqs-semenovsky=1114q&text=" + urllib.parse.quote("ТРЦ Семёновский комната матери и ребенка этаж 2")]
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
