"""Карточки организаций партии 1114zd (выдача sections_1114zd_q.py) → auto/fetch-queue.txt, ключи sc<n>-s1114zd (n — номер кандидата).
python3 tools/sections_1114zd_cards.py"""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
KEEP = {7,14,20,25,28,36,55,59,65,69,92,93,114,115,123,124,126,133,135,136,140,143,145,147,148,152,165,167,176,178,185,187,191,195,200,203,204,210}
if __name__ == "__main__":
    C = json.load(open(os.path.join(ROOT, "tools/sections_1114zd_cands.json")))
    urls = []
    for c in C:
        if c["n"] not in KEEP: continue
        a = re.sub(r",\s*(этаж|подъезд|вход|метро|Метро|СК |КЦ|ТЦ|зал|Центр|мкр|внешняя|есть).*$", "", c["addr"])
        if False and "Московский" not in a and "Люберцы" not in a and "Щёлково" not in a and "Балашиха" not in a and "Химки" not in a and "Реутов" not in a and "Мытищи" not in a and "Московский" not in a and "Островцы" not in a: a = "Москва, " + a
        urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?sc{c['n']}=s1114zd&text=" + urllib.parse.quote(f"{c['name']}, {a}"))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
