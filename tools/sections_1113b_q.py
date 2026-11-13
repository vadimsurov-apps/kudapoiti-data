"""Робот sections 13.11 (00 UTC, партия 1113b): поиск по районам — выдача Яндекс Карт → auto/fetch-queue.txt.
python3 tools/sections_1113b_q.py"""
import os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
AREAS = ["Партизанская", "Первомайская", "Перово", "Петровский парк", "Петровско-Разумовская", "Печатники", "Пионерская",
         "Планерная", "Площадь Гагарина", "Площадь Ильича", "Полежаевская", "Полянка", "Подольск", "Химки"]
TOWNS = {"Подольск", "Химки"}
Q = ["самбо дзюдо борьба для детей", "бокс карате тхэквондо для детей", "художественная гимнастика акробатика для детей"]
if __name__ == "__main__":
    urls = []
    for i, a in enumerate(AREAS):
        for j, q in enumerate(Q):
            t = f"{q} {a}" if a in TOWNS else f"{q} метро {a}"
            urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?sz{i}x{j}=1113b&text=" + urllib.parse.quote(t))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
