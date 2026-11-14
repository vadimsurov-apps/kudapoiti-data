"""Робот rare 14.11 (1114e), шаг 2: выдачи Яндекс Карт по городам Подмосковья, где в базе нет ни одного катка/хоккея/
фигурного (ключи rr14et*), и проверка картингов-кандидатов OSM (rr14ek*) → auto/fetch-queue.txt.   python3 tools/rare_1114e_towns.py"""
import os, urllib.parse as u
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
TOWNS = ["Голицыно", "Дедовск", "Долгопрудный", "Дубна", "Егорьевск", "Звенигород", "Ивантеевка", "Кашира", "Краснознаменск",
         "Кубинка", "Лосино-Петровский", "Луховицы", "Люберцы", "Павловский Посад", "Пушкино", "Руза", "Сергиев Посад",
         "Солнечногорск", "Старая Купавна", "Талдом", "Троицк", "Фрязино", "Шатура", "Щербинка", "Электроугли"]
QT = ["ледовый дворец каток {}", "хоккей фигурное катание для детей {}"]
KART = ["картинг MIKS Руднево", "детский картинг Филёвский парк", "картинг Le Mans Кунцево", "картинг Звенигород",
        "картинг Электросталь", "картинг Егорьевск", "скалодром Зеленоград ЭЛМА", "скалодром Солнечногорск"]
fq = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?rr14et{i:03d}=1114e&text=" + u.quote(q.format(t))
      for i, (t, q) in enumerate((t, q) for t in TOWNS for q in QT)]
fq += [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?rr14ek{i:02d}=1114e&text=" + u.quote(t) for i, t in enumerate(KART)]
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in fq if l not in old]) + "\n")
    print(len(fq))
