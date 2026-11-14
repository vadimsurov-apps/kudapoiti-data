"""Робот fun 1114a: координаты домов (fxh-<ключ>-1114a) и страница режима ГМИИ → auto/fetch-queue.txt."""
import os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
H = {"lazertag-zone": "Москва, Производственная улица, 12к2", "fort-podolsk": "Подольск, Авиационная улица, 29"}
SITES = ["https://pushkinmuseum.art/visitors/hours/index.php?lang=ru", "https://pushkinmuseum.art/museum/buildings/main/index.php?lang=ru"]
if __name__ == "__main__":
    base = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?"
    urls = SITES + [f"{base}fxh-{k}=1114a&text=" + urllib.parse.quote(t) for k, t in H.items()]
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
