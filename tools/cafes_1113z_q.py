"""Робот cafes 1113z: выдачи Яндекс Карт по районам (kcz<N>-1113z) → auto/fetch-queue.txt, список запросов → tools/cafes_1113z_queries.json."""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
a = json.load(open(os.path.join(ROOT, "auto/search-areas.json"))); p = json.load(open(os.path.join(ROOT, "auto/search-progress-cafes.json")))
areas = sorted([("m", x) for x in a["metro"]] + [("t", x) for x in a["towns"]], key=lambda t: p.get(t[1], ""))[:15]
Q = []
for k, x in areas:
    loc = f"метро {x}" if k == "m" else x
    for t in ("кафе с детской игровой комнатой", "ресторан с детской комнатой и аниматорами", "семейный ресторан с детской зоной"):
        Q.append({"area": x, "q": f"{t} {loc}"})
base = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?"
urls = [f"{base}kcz{n}=1113z&text=" + urllib.parse.quote(q["q"]) for n, q in enumerate(Q)]
json.dump({"q": Q}, open(os.path.join(ROOT, "tools/cafes_1113z_queries.json"), "w"), ensure_ascii=False, indent=0)
fp = os.path.join(ROOT, "auto/fetch-queue.txt"); old = open(fp).read()
open(fp, "w").write("\n".join(urls) + "\n" + old)
print(len(urls), [x for _, x in areas])
