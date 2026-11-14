"""Робот rare 1114f, шаг 2: точные выдачи Яндекс Карт по новым (нет в базе) организациям (rr14fn*) и их карточки → auto/fetch-queue.txt.
python3 tools/rare_1114f_queue2.py"""
import os, urllib.parse as u
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q = ["Шарк Скилс Хоккей Ленинградский проспект 39", "Хоккейная академия IceZubrus Ленинградский проспект 39",
     "Невские медведи Нагатинская 16", "Панда Воллей Нагатинская 16", "ТТ Лидер Сущёвский Вал 5",
     "Школа настольного тенниса Али Ишанова Отрадное", "Арена-ск сквош Сколково", "Беркут волейбол Адмирала Лазарева 24",
     "Zavadovskaya club Крылатская 1", "Полюс Арена Горки-2 каток", "Московская академия фигурного катания Заповедная 5",
     "Фигурное катание Олимпийская деревня 2 стр 1 Академия хоккея"]
ORG = ["gbu_sportivnaya_shkola_2/15282342221", "figurnoye_kataniye/122387306862", "ledovy_dvorets/1062470155"]
fq = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?rr14fn{i:02d}=1114f&text=" + u.quote(t) for i, t in enumerate(Q)]
fq += ["https://yandex.ru/maps/org/" + o + "/" for o in ORG]
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in fq if l not in old]) + "\n")
    print(len(fq))
# шаг 3: сайты новых мест (детские группы, возраст, часы)
SITES = ["https://sharkskills.ru/", "https://aliishanov.ru/", "https://zavadovskaya.club/", "https://polyus-arena.ru/",
         "https://polyus-arena.ru/contacts/", "https://nevsky-bears.ru/moscow/nagatinskaya/", "https://pandavolleyhall.ru/"]
if __name__ == "__main__" and "--sites" in __import__("sys").argv:
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in SITES if l not in old]) + "\n")
