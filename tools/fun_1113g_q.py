"""Робот fun, 13.11 (запуск 1113g): выдачи Яндекс Карт по 15 районам второго круга (fwa<N>-1113g) → auto/fetch-queue.txt."""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
A = json.load(open(os.path.join(ROOT, "auto/search-areas.json")))
P = json.load(open(os.path.join(ROOT, "auto/search-progress-fun.json")))
T = ["детский развлекательный центр", "квест для детей", "мастер-класс для детей", "музей для детей",
     "детская игровая комната", "лазертаг для детей"]
metro = sorted(A["metro"], key=lambda x: P.get(x, ""))[:12]
towns = sorted(A["towns"], key=lambda x: P.get(x, ""))[:3]
AREAS = metro + towns
Q = []
for i, a in enumerate(AREAS):
    for k in range(3):
        t = T[(3 * i + k) % 6]
        Q.append({"area": a, "theme": t, "text": f"{t} метро {a}" if a in metro else f"{t} {a}"})
if __name__ == "__main__":
    json.dump({"areas": AREAS, "q": Q}, open(os.path.join(ROOT, "tools/fun_1113g_queries.json"), "w"),
              ensure_ascii=False, indent=0)
    base = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?"
    urls = [f"{base}fwa{n}=1113g&text=" + urllib.parse.quote(q["text"]) for n, q in enumerate(Q)]
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(AREAS, len(urls))
