"""Робот pools 14.11 (11 UTC), шаг 5: клуб синхронного плавания «Артистик» — карточки Яндекс Карт филиалов (ключ pa<N>=1114k) →
auto/fetch-queue.txt, справка OSM (pl33-artistic-*) → auto/osm-queries.json.   python3 tools/pools_1114k_artq.py"""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q = {
 "artistic-manhattan": ("Москва, Новодмитровская ул., 5А, стр. 2", None, 0, ""),
 "artistic-fitnes-park-izmaylovo": ("Москва, Измайловское ш., 71, стр. 8", (55.7905, 37.7480), 700, "Измайловское"),
 "artistic-kenga-festivalnaya": ("Москва, Фестивальная ул., 22, стр. 6А", (55.8560, 37.4800), 1200, "Фестивальная"),
 "artistic-yauza-mytishchi": ("Мытищи, Новомытищинский просп., 88, корп. 5", (55.9000, 37.7180), 1500, "Новомытищинский"),
 "artistic-wegym-aviamotornaya": ("Москва, 2-я ул. Синичкина, 9А", (55.7600, 37.7140), 900, "Синичкина"),
}
if __name__ == "__main__":
    lines, out = [], []
    for i, (pid, (addr, c, r, st)) in enumerate(Q.items()):
        lines.append("https://yandex.ru/maps/1/moscow-and-moscow-oblast/?pa%d=1114k&text=%s" % (i, urllib.parse.quote("Артистик, " + addr)))
        if c: out.append({"id": "pl33-" + pid, "lat": c[0], "lon": c[1], "radius": r, "name": "бассейн", "street": st})
    lines += ["https://artisticsport.ru/sinhronnoe-plavanie/", "https://artisticsport.ru/plavanie/", "https://artisticsport.ru/oplata/"]
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in lines if l not in old]) + "\n")
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = json.load(open(p)); have = {x["id"] for x in old}
    json.dump(old + [q for q in out if q["id"] not in have], open(p, "w"), ensure_ascii=False, indent=1)
    print(len(out), len(lines))
