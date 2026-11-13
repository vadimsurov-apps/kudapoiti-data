"""Робот pools 13.11 (23 UTC): выдачи Яндекс Карт по новым районам (ключ pz<N>=1113z: метро Лухмановская … Медведково и
города Лобня, Видное … Ивантеевка) → auto/fetch-queue.txt; сайты мест, оставленных прошлым запуском без возраста групп.
python3 tools/pools_1113z_q.py"""
import os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
METRO = ["Международная", "Менделеевская", "Минская", "Митино", "Мичуринский проспект", "Мнёвники", "Молодежная", "Мякинино"]
TOWNS = ["Дзержинский", "Солнечногорск", "Фрязино", "Лыткарино", "Воскресенск", "Ступино", "Истра"]
QS = ("обучение плаванию детей с 3 лет ", "грудничковое плавание ", "детский бассейн ")
AREAS = [("метро " + a) for a in METRO] + TOWNS
EXTRA = ["https://agidel-reutov.ru/", "https://art-swim.ru/", "https://kinderpool.ru/", "https://dreamswim.ru/", "https://aqualife-zel.ru/"]
if __name__ == "__main__":
    lines = list(EXTRA)
    for i, a in enumerate(AREAS):
        for j, q in enumerate(QS):
            lines.append("https://yandex.ru/maps/1/moscow-and-moscow-oblast/?pz%d=1113z&text=%s" % (i * 3 + j, urllib.parse.quote(q + a)))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in lines if l not in old]) + "\n")
    print(len(lines))
