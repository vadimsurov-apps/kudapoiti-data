"""Робот fun 1114a: сайты кандидатов из выдач по районам + повторные поиски карточек (fxf-<ключ>-1114a) → auto/fetch-queue.txt."""
import os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SITES = ["https://mytysa.ru/", "https://xn--80ajiasde0a8a.xn--80adxhks/", "https://lazertag.zone/",
         "https://fortupgrade-podolsk.ru/", "https://questkinder.events/"]
Q = {"hryu": "Скажи Хрю! антикафе, Москва, проспект Вернадского, 11/19",
     "kapibar": "Капибарная, Москва, Большой Толмачёвский переулок, 4с1",
     "terminal": "Терминал, Мытищи, улица Мира, 32/2",
     "shokolad": "История Московского шоколада, музей, Москва, Рублёвское шоссе, 30к1",
     "jumji": "Jum&ji, Красногорск, Ново-Никольская улица, 122с1",
     "minilandia": "МиниЛандия игровая комната, Красногорск, Международная улица, 12"}
if __name__ == "__main__":
    base = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?"
    urls = SITES + [f"{base}fxf-{k}=1114a&text=" + urllib.parse.quote(t) for k, t in Q.items()]
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
