"""Карточки организаций партии 1113i (выдача sections_1113i_q.py) → auto/fetch-queue.txt, ключи sc<n>-s1113i (n — номер кандидата).
python3 tools/sections_1113i_cards.py"""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
KEEP = {0,5,27,42,47,48,52,54,64,81,82,89,91,92,93,95,98,100,103,104,106,113,115,116,118,128,131,135,136,138,147,148,152,154}
if __name__ == "__main__":
    C = json.load(open(os.path.join(ROOT, "tools/sections_1113i_cands.json")))
    urls = []
    for c in C:
        if c["dup"] or c["n"] not in KEEP: continue
        a = re.sub(r",\s*(этаж|подъезд|вход|метро|Метро|СК |КЦ|ТЦ|зал|Центр|мкр|внешняя|есть).*$", "", c["addr"])
        if "Москва" not in a and "Московский" not in a and "Люберцы" not in a: a = "Москва, " + a
        urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?sc{c['n']}=s1113i&text=" + urllib.parse.quote(f"{c['name']}, {a}"))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
