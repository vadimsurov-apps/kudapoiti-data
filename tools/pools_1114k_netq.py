"""Робот pools 14.11 (11 UTC): выдачи Яндекс Карт по сетям и кандидатам прошлого запуска (ключ pn<N>=1114k) → auto/fetch-queue.txt.
python3 tools/pools_1114k_netq.py"""
import os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Y = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?pn%d=1114k&text=%s"
QS = ["ГрудничОк аквацентр", "Mevis школа плавания", "Аква академия школа плавания для детей", "Mini Swim детский бассейн",
      "детский бассейн Кит грудничковое плавание", "Школа спортивно-оздоровительного плавания Крылатские Холмы 15 корп. 2",
      "СинхрО2 Красногорск Советская 15", "Океаника школа плавания", "Аквакласс детский бассейн", "Aquababyclub детский бассейн",
      "раннее плавание для малышей студия", "бассейн для грудничков ЖК", "X-Fit детская школа плавания",
      "детская школа плавания Москомспорт бассейн", "Дельфин школа плавания для детей", "Акулы школа плавания для детей",
      "Swim Kids школа плавания", "Аквастар детский бассейн", "Капитошка детский бассейн", "Утёнок детский бассейн плавание для малышей"]
LINES = [Y % (i, urllib.parse.quote(q)) for i, q in enumerate(QS)]
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in LINES if l not in old]) + "\n")
    print(len(LINES))
