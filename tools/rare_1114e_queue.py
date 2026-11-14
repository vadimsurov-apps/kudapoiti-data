"""Робот rare 14.11 (15:50 UTC; 1114e): выдачи Яндекс Карт по 14 районам второго круга (каток / хоккей-фигурное /
настольный теннис-волейбол-сквош / скалодром-батуты-картинг-падел; ключи rr14eq*) и зимние выдачи (rr14ex*)
→ auto/fetch-queue.txt.   python3 tools/rare_1114e_queue.py [org/<slug>/<id> ...]"""
import os, urllib.parse as u
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
AREAS = ["Лесопарковая", "Лефортово", "Лианозово", "Лихоборы", "Локомотив", "Ломоносовский проспект", "Лубянка",
         "Лужники", "Лухмановская", "Люблино", "Марксистская", "Марьина Роща", "Марьино", "Маяковская"]
QM = ["каток {}", "хоккей фигурное катание для детей {}", "настольный теннис волейбол сквош бадминтон для детей {}",
      "скалодром батуты картинг падел {}"]
EXTRA = ["тюбинг Москва", "снежный парк тюбинг Подмосковье", "горнолыжная школа для детей Москва",
         "каток массовое катание Подмосковье ледовая арена", "каток в парке Москва", "цирк шапито Москва",
         "театр зверей Москва", "памп-трек Москва", "сквош для детей Москва", "настольный теннис для детей Подмосковье"]
def area(a): return a + " метро"
fq = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?rr14eq{i:03d}=1114e&text=" + u.quote(q.format(area(a)))
      for i, (a, q) in enumerate((a, q) for a in AREAS for q in QM)]
fq += [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?rr14ex{i:02d}=1114e&text=" + u.quote(t) for i, t in enumerate(EXTRA)]
if __name__ == "__main__":
    import sys
    fq += ["https://yandex.ru/maps/org/" + o + "/" for o in sys.argv[1:]]
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in fq if l not in old]) + "\n")
    print(len(fq))
