"""Робот rare 1114f, шаг 4: организации из подборок Яндекс Карт (auto/pages), которых нет в базе (rr14fp*) → auto/fetch-queue.txt."""
import os, urllib.parse as u
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q = ["Диксодром картинг", "Kart Racing Club картинг Москва", "Навка Арена каток", "Арена Сталкер каток Москва",
     "Академия льда Москва фигурное катание", "Matterhorn фигурное катание Москва", "Pro-katanie фигурное катание Химки",
     "Arthur_hockey_ хоккей Москва", "Спортивный клуб Кирилла Ефремова скалодром Одинцово", "FlyFactory Электросталь батуты",
     "Школа настольного тенниса Али Ишанова Отрадное Прокофьева 1А"]
fq = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?rr14fp{i:02d}=1114f&text=" + u.quote(t) for i, t in enumerate(Q)]
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in fq if l not in old]) + "\n")
    print(len(fq))
