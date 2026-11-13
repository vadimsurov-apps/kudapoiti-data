"""Робот sections 13.11 (00 UTC, партия 1113e): поиск по районам — выдача Яндекс Карт → auto/fetch-queue.txt.
python3 tools/sections_1113e_q.py"""
import os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
AREAS = ["Пушкинская", "Пыхтино", "Пятницкое шоссе", "Рассказовка", "Римская", "Ростокино", "Румянцево",
         "Саларьево", "Севастопольская", "Селигерская", "Семеновская", "Серпуховская", "Славянский бульвар", "Смоленская", "Сокол"]
TOWNS = {"Пыхтино", "Рассказовка", "Саларьево"}
Q = ["самбо дзюдо борьба для детей", "бокс карате тхэквондо для детей", "художественная гимнастика акробатика для детей",
     "футбол баскетбол лёгкая атлетика секция для детей"]
if __name__ == "__main__":
    urls = []
    for i, a in enumerate(AREAS):
        for j, q in enumerate(Q):
            t = f"{q} {a}" if a in TOWNS else f"{q} метро {a}"
            urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?sz{i}x{j}=1113e&text=" + urllib.parse.quote(t))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
