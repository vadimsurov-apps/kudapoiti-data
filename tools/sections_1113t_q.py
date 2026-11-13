"""Робот sections 13.11 (15 UTC, партия 1113t): второй круг поиска по районам — выдача Яндекс Карт → auto/fetch-queue.txt.
python3 tools/sections_1113t_q.py"""
import os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
AREAS = ["Юго-Западная", "Южная", "Ясенево", "Авиамоторная", "Автозаводская", "Академическая", "Алексеевская",
         "Алма-Атинская", "Алтуфьево", "Аминьевская", "Андроновка", "Аннино", "Аэропорт", "Бабушкинская", "Багратионовская"]
Q = ["самбо дзюдо борьба для детей", "бокс карате тхэквондо для детей", "художественная гимнастика акробатика для детей",
     "футбол баскетбол лёгкая атлетика секция для детей", "спортивная гимнастика шахматы для детей"]
if __name__ == "__main__":
    urls = []
    for i, a in enumerate(AREAS):
        for j, q in enumerate(Q):
            urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?sz{i}x{j}=1113t&text=" + urllib.parse.quote(f"{q} метро {a}"))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
