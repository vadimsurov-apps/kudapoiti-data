"""Робот pools 13.11 (17 UTC): выдачи Яндекс Карт по новым районам (ключ pz<N>=1113u: метро Лесопарковая … Лужники и
города Орехово-Зуево … Ногинск) → auto/fetch-queue.txt.   python3 tools/pools_1113u_q.py"""
import os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
METRO = ["Лесопарковая", "Лефортово", "Лианозово", "Лихоборы", "Локомотив", "Ломоносовский проспект", "Лубянка", "Лужники"]
TOWNS = ["Орехово-Зуево", "Долгопрудный", "Реутов", "Жуковский", "Пушкино", "Сергиев Посад", "Ногинск"]
QS = ("обучение плаванию детей с 3 лет ", "грудничковое плавание ", "детский бассейн ")
AREAS = [("метро " + a) for a in METRO] + TOWNS
if __name__ == "__main__":
    lines = []
    for i, a in enumerate(AREAS):
        for j, q in enumerate(QS):
            lines.append("https://yandex.ru/maps/1/moscow-and-moscow-oblast/?pz%d=1113u&text=%s" % (i * 3 + j, urllib.parse.quote(q + a)))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in lines if l not in old]) + "\n")
    print(len(lines))
