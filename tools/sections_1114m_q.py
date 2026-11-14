"""Робот sections 14.11 (09 UTC, партия 1114m): второй круг поиска по районам — выдача Яндекс Карт → auto/fetch-queue.txt.
python3 tools/sections_1114m_q.py"""
import os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
AREAS = ["Павловский-Посад", "Старая-Купавна", "Сосенское", "Новомосковский", "Мосрентген", "Библиотека им.Ленина",
         "Боровицкая", "Водный стадион", "Войковская", "Волгоградский проспект", "Волжская", "Волоколамская",
         "Воробьевы горы", "Воронцовская", "Выставочная"]
METRO = set(AREAS[5:])
Q = ["самбо дзюдо борьба для детей", "бокс карате тхэквондо для детей", "художественная гимнастика акробатика для детей",
     "футбол баскетбол лёгкая атлетика секция для детей", "спортивная гимнастика шахматы для детей"]
def where(a):
    a = a.replace("-", " ").replace("им.Ленина", "имени Ленина")
    return f"метро {a}" if a.replace(" ", "-") in METRO or a in METRO or "Ленина" in a else a
if __name__ == "__main__":
    urls = []
    for i, a in enumerate(AREAS):
        for j, q in enumerate(Q):
            urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?sz{i}x{j}=1114m&text=" + urllib.parse.quote(f"{q} {where(a)}"))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
