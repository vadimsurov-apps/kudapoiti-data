"""Робот fun 1114a: сайты кандидатов OSM (часы, цены) → auto/fetch-queue.txt."""
import os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SITES = ["https://gabrileon.ru/", "https://zoolandia-istra.ru/", "https://attragrad.ru/", "https://ecocenter-vg.tilda.ws/", "https://museum.timacad.ru/",
         "https://museumsport.ru/", "https://www.trk-mari.ru/", "https://www.avenue-sw.ru/", "https://www.waypark.ru/",
         "https://june-mytishi.ru/", "https://www.tcperlovsky.ru/"]
Q = {"tank": "Танковый музей Кубинка", "kosmo": "Павильон 34 Космонавтика и авиация ВДНХ"}
if __name__ == "__main__":
    base = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?"
    urls = SITES + [f"{base}fxg-{k}=1114a&text=" + urllib.parse.quote(t) for k, t in Q.items()]
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
