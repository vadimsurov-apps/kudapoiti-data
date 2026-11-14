"""Робот pools 14.11 (02 UTC): выдачи Яндекс Карт по новым районам (ключ pz<N>=1114c: метро Нагатинская … Новаторская и
Зеленоград, Коммунарка, Московский, Троицк, Щербинка, Нахабино, Дедовск) → auto/fetch-queue.txt.
python3 tools/pools_1114c_q.py"""
import os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
METRO = ["Нагатинская", "Нагатинский затон", "Нагорная", "Народное Ополчение", "Нахимовский проспект", "Некрасовка",
         "Нижегородская", "Новаторская"]
TOWNS = ["Зеленоград", "Коммунарка", "Московский", "Троицк", "Щербинка", "Нахабино", "Дедовск"]
QS = ("обучение плаванию детей с 3 лет ", "грудничковое плавание ", "детский бассейн ")
AREAS = [("метро " + a) for a in METRO] + TOWNS
EXTRA = []
if __name__ == "__main__":
    lines = list(EXTRA)
    for i, a in enumerate(AREAS):
        for j, q in enumerate(QS):
            lines.append("https://yandex.ru/maps/1/moscow-and-moscow-oblast/?pz%d=1114c&text=%s" % (i * 3 + j, urllib.parse.quote(q + a)))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in lines if l not in old]) + "\n")
    print(len(lines))
