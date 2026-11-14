"""Робот fun 1114a: вторая пачка кандидатов OSM (зоо, аттракционы, игровые, квесты) — карточки Яндекс Карт (fxp-<n>-1114a)."""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
if __name__ == "__main__":
    L = json.load(open(os.path.join(ROOT, "tools/fun_1114a_osm2.json")))
    base = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?"
    urls = [f"{base}fxp-{n}=1114a&ll={c['lon']:.5f}%2C{c['lat']:.5f}&z=17&text=" + urllib.parse.quote(c["name"].replace('"', ''))
            for n, c in enumerate(L)]
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
