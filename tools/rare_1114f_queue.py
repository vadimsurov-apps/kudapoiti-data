"""Робот rare 14.11 (18:45 UTC; 1114f): выдачи Яндекс Карт по 14 районам второго круга (rr14fq*), зимние выдачи (rr14fx*)
и города (rr14ft*) → auto/fetch-queue.txt.   python3 tools/rare_1114f_queue.py [org/<slug>/<id> ...]"""
import os, urllib.parse as u
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
AREAS = ["Медведково", "Международная", "Менделеевская", "Минская", "Митино", "Мичуринский проспект", "Мнёвники",
         "Молодежная", "Мякинино", "Нагатинская", "Нагатинский затон", "Нагорная", "Народное Ополчение", "Нахимовский проспект"]
QM = ["каток {}", "хоккей фигурное катание для детей {}", "настольный теннис волейбол сквош бадминтон для детей {}",
      "скалодром батуты картинг падел {}"]
TOWNS = ["Химки", "Мытищи", "Одинцово"]
QT = ["каток массовое катание {}", "тюбинг горка {}", "скалодром батутный центр {}"]
EXTRA = ["тюбинг парк Москва", "горнолыжный склон Подмосковье детская школа", "горнолыжная школа для детей Подмосковье",
         "снежный парк Подмосковье", "каток с искусственным льдом в парке Москва", "цирк шапито Подмосковье",
         "театр кошек собак Москва", "памп-трек Подмосковье", "сквош корт Москва", "крытый каток в торговом центре Москва",
         "ледовый каток в ТЦ Подмосковье", "настольный теннис для детей Москва клуб", "школа фигурного катания для детей Москва",
         "детская хоккейная школа Подмосковье", "волейбол для детей Москва секция"]
fq = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?rr14fq{i:03d}=1114f&text=" + u.quote(q.format(a + " метро"))
      for i, (a, q) in enumerate((a, q) for a in AREAS for q in QM)]
fq += [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?rr14ft{i:03d}=1114f&text=" + u.quote(q.format(t))
       for i, (t, q) in enumerate((t, q) for t in TOWNS for q in QT)]
fq += [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?rr14fx{i:02d}=1114f&text=" + u.quote(t) for i, t in enumerate(EXTRA)]
if __name__ == "__main__":
    import sys
    fq += ["https://yandex.ru/maps/org/" + o + "/" for o in sys.argv[1:]]
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in fq if l not in old]) + "\n")
    print(len(fq))
