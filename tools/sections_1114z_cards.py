"""Карточки организаций партии 1114z (выдача sections_1114z_q.py) → auto/fetch-queue.txt, ключи sc<n>-s1114z (n — номер кандидата).
python3 tools/sections_1114z_cards.py"""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
KEEP = {13,14,16,32,33,39,47,50,51,55,69,76,80,85,87,92,105,114,121,127,128,132,137,139,144,145,156,158,162,166,168,172,173,176,184,188,189,190,191,193,199,202,203,212,215,219}
if __name__ == "__main__":
    C = json.load(open(os.path.join(ROOT, "tools/sections_1114z_cands.json")))
    urls = []
    for c in C:
        if c["n"] not in KEEP: continue
        a = re.sub(r",\s*(этаж|подъезд|вход|метро|Метро|СК |КЦ|ТЦ|зал|Центр|мкр|внешняя|есть).*$", "", c["addr"])
        if False and "Московский" not in a and "Люберцы" not in a and "Щёлково" not in a and "Балашиха" not in a and "Химки" not in a and "Реутов" not in a and "Мытищи" not in a and "Московский" not in a and "Островцы" not in a: a = "Москва, " + a
        urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?sc{c['n']}=s1114z&text=" + urllib.parse.quote(f"{c['name']}, {a}"))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
