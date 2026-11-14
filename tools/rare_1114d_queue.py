"""Робот rare 14.11 (12:50 UTC; 1114d): выдачи Яндекс Карт по 14 районам второго круга (каток / хоккей-фигурное /
настольный теннис-волейбол-сквош / скалодром-батуты-картинг-падел; ключи rr14dq*), зимние выдачи (rr14dx*) и обзорные
страницы организаций-кандидатов из выдач 1114c, которых ещё нет в кэше → auto/fetch-queue.txt.   python3 tools/rare_1114d_queue.py"""
import os, urllib.parse as u
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
AREAS = ["Бутово", "Королёв", "Красногорск", "Крестьянская застава", "Кропоткинская", "Крылатское", "Крымская",
         "Кузнецкий мост", "Кузьминки", "Кунцевская", "Курская", "Кутузовская", "Ленинский проспект", "Лермонтовский проспект"]
TOWNS = {"Бутово", "Королёв", "Красногорск"}
QM = ["каток {}", "хоккей фигурное катание для детей {}", "настольный теннис волейбол сквош бадминтон для детей {}",
      "скалодром батуты картинг падел {}"]
EXTRA = ["тюбинг Подмосковье", "горнолыжный комплекс Московская область", "детская горнолыжная школа Подмосковье",
         "ледовый дворец массовое катание Подмосковье", "каток в парке Подмосковье", "цирк Московская область",
         "театр зверей Подмосковье", "сквош Москва", "настольный теннис клуб Москва", "памп-трек Московская область"]
def area(a): return a if a in TOWNS else a + " метро"
fq = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?rr14dq{i:03d}=1114d&text=" + u.quote(q.format(area(a)))
      for i, (a, q) in enumerate((a, q) for a in AREAS for q in QM)]
fq += [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?rr14dx{i:02d}=1114d&text=" + u.quote(t) for i, t in enumerate(EXTRA)]
if __name__ == "__main__":
    import sys
    fq += ["https://yandex.ru/maps/org/" + o + "/" for o in sys.argv[1:]]
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in fq if l not in old]) + "\n")
    print(len(fq))
