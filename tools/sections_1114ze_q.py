"""Робот sections 14.11 (12 UTC, вторая пачка 1114ze): 15 районов второго круга, где sections не искал дольше всего (с 12.11) —
выдача Яндекс Карт по видам спорта → auto/fetch-queue.txt (ключи sz<i>x<j>-1114ze). python3 tools/sections_1114ze_q.py"""
import os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
AREAS = ["Лефортово", "Лианозово", "Лихоборы", "Локомотив", "Ломоносовский проспект", "Лубянка", "Лужники", "Лухмановская", "Люблино", "Марксистская", "Марьина Роща", "Марьино", "Маяковская", "Медведково", "Международная"]
TOWNS = set()
PROG = {}
Q = ["самбо дзюдо борьба для детей", "бокс карате тхэквондо для детей", "художественная гимнастика акробатика для детей",
     "футбол баскетбол лёгкая атлетика секция для детей", "спортивная гимнастика шахматы для детей"]
if __name__ == "__main__":
    urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?sz{i}x{j}=1114ze&text=" + urllib.parse.quote(f"{q} {a}" if a in TOWNS else f"{q} метро {a}")
            for i, a in enumerate(AREAS) for j, q in enumerate(Q)]
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
