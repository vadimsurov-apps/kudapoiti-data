"""Карточки организаций партии 1114zb (выдача sections_1114zb_q.py) → auto/fetch-queue.txt, ключи sc<n>-s1114zb (n — номер кандидата).
python3 tools/sections_1114zb_cards.py"""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
KEEP = {3,6,8,12,17,18,19,20,21,22,36,37,39,41,44,45,47,49,50,56,57,59,60,67,77,80,84,91,93,100,107,114,118,120,131,135,139,141,151,154,167,174}
if __name__ == "__main__":
    C = json.load(open(os.path.join(ROOT, "tools/sections_1114zb_cands.json")))
    urls = []
    for c in C:
        if c["n"] not in KEEP: continue
        a = re.sub(r",\s*(этаж|подъезд|вход|метро|Метро|СК |КЦ|ТЦ|зал|Центр|мкр|внешняя|есть).*$", "", c["addr"])
        if False and "Московский" not in a and "Люберцы" not in a and "Щёлково" not in a and "Балашиха" not in a and "Химки" not in a and "Реутов" not in a and "Мытищи" not in a and "Московский" not in a and "Островцы" not in a: a = "Москва, " + a
        urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?sc{c['n']}=s1114zb&text=" + urllib.parse.quote(f"{c['name']}, {a}"))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
