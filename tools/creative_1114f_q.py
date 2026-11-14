"""Робот creative, 14.11 (запуск 1114e, вторая волна 1114f): по тем же 15 районам — остальные 4 темы (cv<N>-1114f)."""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
A = json.load(open(os.path.join(ROOT, "auto/search-areas.json")))
E = json.load(open(os.path.join(ROOT, "tools/creative_1114e_queries.json")))
T = ["танцы для детей", "балетная школа для детей", "вокал для детей", "музыкальная школа для детей",
     "театральная студия для детей", "рисование для детей", "гончарная мастерская для детей"]
done = {(q["area"], q["theme"]) for q in E["q"]}
Q = []
for a in E["areas"]:
    for t in T:
        if (a, t) not in done:
            Q.append({"area": a, "theme": t, "text": f"{t} метро {a}" if a in A["metro"] else f"{t} {a}"})
if __name__ == "__main__":
    json.dump({"areas": E["areas"], "q": Q}, open(os.path.join(ROOT, "tools/creative_1114f_queries.json"), "w"), ensure_ascii=False, indent=0)
    urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?cv{n}=1114f&text=" + urllib.parse.quote(q["text"]) for n, q in enumerate(Q)]
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old_ = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old_)
    print(len(urls))
