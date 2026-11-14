"""Карточки организаций партии 1114s (выдача sections_1114s_q.py) → auto/fetch-queue.txt, ключи sc<n>-s1114s (n — номер кандидата).
python3 tools/sections_1114s_cards.py"""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
KEEP = {0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 15, 16, 17, 18, 20, 21, 23, 24, 27, 29, 30, 31, 33, 34, 35, 36, 39, 40, 41, 43, 44, 45, 46, 48, 51, 54, 55, 56, 57, 58, 61, 63, 65, 66, 67, 68, 69, 70, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 100, 101, 102, 103, 105, 106, 107, 110, 111, 114, 115, 117, 119, 122, 123, 128, 129, 130, 131, 132, 133, 134, 136, 138, 139, 140, 142, 143, 144, 145, 150, 151, 152, 153, 156, 158, 159, 161, 162, 171, 172, 176, 178, 179}
if __name__ == "__main__":
    C = json.load(open(os.path.join(ROOT, "tools/sections_1114s_cands.json")))
    urls = []
    for c in C:
        if c["dup"] or c["n"] not in KEEP: continue
        a = re.sub(r",\s*(этаж|подъезд|вход|метро|Метро|СК |КЦ|ТЦ|зал|Центр|мкр|внешняя|есть).*$", "", c["addr"])
        if False and "Московский" not in a and "Люберцы" not in a and "Щёлково" not in a and "Балашиха" not in a and "Химки" not in a and "Реутов" not in a and "Мытищи" not in a and "Московский" not in a and "Островцы" not in a: a = "Москва, " + a
        urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?sc{c['n']}=s1114s&text=" + urllib.parse.quote(f"{c['name']}, {a}"))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
