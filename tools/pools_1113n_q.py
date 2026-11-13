"""Робот pools 13.11 (15 UTC): выдачи Яндекс Карт по новым районам (ключ pz<N>=1113n: метро Крымская … Лермонтовский проспект и
города Электросталь … Раменское) → auto/fetch-queue.txt.   python3 tools/pools_1113n_q.py"""
import os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
METRO = ["Крымская", "Кузнецкий мост", "Кузьминки", "Кунцевская", "Курская", "Кутузовская", "Ленинский проспект",
         "Лермонтовский проспект"]
TOWNS = ["Электросталь", "Коломна", "Одинцово", "Домодедово", "Серпухов", "Щёлково", "Раменское"]
QS = ("обучение плаванию детей с 3 лет ", "грудничковое плавание ", "детский бассейн ")
AREAS = [("метро " + a) for a in METRO] + TOWNS
if __name__ == "__main__":
    lines = []
    for i, a in enumerate(AREAS):
        for j, q in enumerate(QS):
            lines.append("https://yandex.ru/maps/1/moscow-and-moscow-oblast/?pz%d=1113n&text=%s" % (i * 3 + j, urllib.parse.quote(q + a)))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in lines if l not in old]) + "\n")
    print(len(lines))
