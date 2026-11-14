"""Робот sections 14.11 (00 UTC, партия 1114a): второй круг поиска по районам — выдача Яндекс Карт → auto/fetch-queue.txt.
python3 tools/sections_1114a_q.py"""
import os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
AREAS = ["Физтех", "Яхромская", "Балашиха", "Мытищи", "Люберцы", "Электросталь", "Коломна", "Домодедово", "Серпухов",
         "Щёлково", "Орехово-Зуево", "Раменское", "Долгопрудный", "Реутов", "Жуковский"]
METRO = {"Физтех", "Яхромская"}
Q = ["самбо дзюдо борьба для детей", "бокс карате тхэквондо для детей", "художественная гимнастика акробатика для детей",
     "футбол баскетбол лёгкая атлетика секция для детей", "спортивная гимнастика шахматы для детей"]
def where(a): return f"метро {a}" if a in METRO else a
if __name__ == "__main__":
    urls = []
    for i, a in enumerate(AREAS):
        for j, q in enumerate(Q):
            urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?sz{i}x{j}=1114a&text=" + urllib.parse.quote(f"{q} {where(a)}"))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
