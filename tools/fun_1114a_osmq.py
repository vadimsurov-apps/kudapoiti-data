"""Робот fun 1114a: кандидаты OSM (auto/candidates.json), которых нет у нас: парки, музеи, зоо, аттракционы —
карточки Яндекс Карт по названию (fxo-<n>-1114a) → auto/fetch-queue.txt; список → tools/fun_1114a_osm.json."""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PICK = ["relation/10330072", "relation/10234070", "relation/2186779", "way/365165205", "relation/11657035",
        "relation/16031", "way/564373238", "relation/7151077", "relation/8467059", "relation/16734094",
        "relation/7231830", "relation/4494168", "relation/11733300", "relation/6886516", "relation/10789215",
        "way/28381713", "relation/12684398", "relation/2369059", "relation/8118918", "relation/7478422",
        "relation/5312705", "relation/10973523", "way/162756579", "relation/6912449",
        "node/14162331916", "way/390134684", "way/93582644", "way/439372440", "way/557385078", "relation/14878200",
        "node/2812338027", "way/510529899", "node/6790183428", "relation/13018588", "way/315853935",
        "relation/2421978", "relation/8273120", "node/3503118696", "relation/1813336", "relation/7486944",
        "node/6016427284", "node/3502556677", "node/1406961084", "node/913308087", "node/3501090950",
        "node/6417697385", "node/3502599105", "node/3501148879", "node/5614559233", "relation/5246176",
        "node/10971892284", "node/3670614109", "node/4924657143", "node/1396891662"]
if __name__ == "__main__":
    C = {c["osm"]: c for c in json.load(open(os.path.join(ROOT, "auto/candidates.json")))["candidates"]}
    L = [C[o] for o in PICK]
    json.dump(L, open(os.path.join(ROOT, "tools/fun_1114a_osm.json"), "w"), ensure_ascii=False, indent=0)
    base = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?"
    urls = [f"{base}fxo-{n}=1114a&ll={c['lon']:.4f}%2C{c['lat']:.4f}&z=15&text=" + urllib.parse.quote(c["name"].replace('"', ''))
            for n, c in enumerate(L)]
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
