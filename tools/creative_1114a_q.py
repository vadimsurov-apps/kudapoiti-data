"""Робот creative, 14.11 (запуск 1114a): запросы выдач Яндекс Карт по 15 районам (ключи cv<N>-1114a) → auto/fetch-queue.txt."""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
A = json.load(open(os.path.join(ROOT, "auto/search-areas.json")))
P = json.load(open(os.path.join(ROOT, "auto/search-progress-creative.json")))
T = ["танцы для детей", "балетная школа для детей", "вокал для детей", "музыкальная школа для детей",
     "театральная студия для детей", "рисование для детей", "гончарная мастерская для детей"]
metro = [x for x in A["metro"] if x not in P][:12]
towns = [x for x in A["towns"] if x not in P][:3]
AREAS = metro + towns
Q = []
for i, a in enumerate(AREAS):
    for k in range(3):
        t = T[(3 * i + k + 4) % 7]
        Q.append({"area": a, "theme": t, "text": f"{t} метро {a}" if a in metro else f"{t} {a}"})
if __name__ == "__main__":
    json.dump({"areas": AREAS, "q": Q}, open(os.path.join(ROOT, "tools/creative_1114a_queries.json"), "w"), ensure_ascii=False, indent=0)
    urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?cv{n}=1114a&text=" + urllib.parse.quote(q["text"]) for n, q in enumerate(Q)]
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(AREAS, len(urls))
