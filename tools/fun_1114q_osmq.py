"""Робот fun 1114q: кандидаты OSM (auto/candidates.json), которых нет у нас: музеи, зоо, аттракционы —
карточки Яндекс Карт по названию рядом с объектом (fqo-<n>-1114q) → auto/fetch-queue.txt; список → tools/fun_1114q_osm.json."""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PICK = ["node/4250506199", "node/8840921870", "node/6573803423", "node/3125490638", "node/9591722217", "way/83341194",
        "node/12406922629", "node/4932922184", "node/3865094589", "relation/21039371", "node/5647683845", "node/7048609400",
        "node/5371334147", "way/1337590874", "way/868336219", "node/3502560194", "node/3501108218", "node/8209683163",
        "node/6387808396", "node/5928928442", "node/11360099597", "node/944400411", "node/700913751", "way/77042858",
        "node/361207435", "node/267719856", "way/32566508", "node/2465851425", "node/1833558556", "node/10689567676",
        "node/9957821698", "node/5164523568", "node/5392524821", "way/227522096", "way/860810497", "way/567514655",
        "node/5890623220", "node/10576714130", "way/162445714", "way/560636372", "node/7317043163", "way/1086156327",
        "way/1301437648", "way/907878809", "relation/19451228", "node/4369839239", "relation/1956038",
        "node/13209006602", "node/11191199559", "node/10648010667", "way/1328757640", "node/7096791723",
        "way/334694226", "way/904283165"]
if __name__ == "__main__":
    C = {c["osm"]: c for c in json.load(open(os.path.join(ROOT, "auto/candidates.json")))["candidates"]}
    L = [C[o] for o in PICK]
    json.dump(L, open(os.path.join(ROOT, "tools/fun_1114q_osm.json"), "w"), ensure_ascii=False, indent=0)
    base = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?"
    urls = [f"{base}fqo-{n}=1114q&ll={c['lon']:.4f}%2C{c['lat']:.4f}&z=16&text=" + urllib.parse.quote(c["name"].replace('"', ''))
            for n, c in enumerate(L)]
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
