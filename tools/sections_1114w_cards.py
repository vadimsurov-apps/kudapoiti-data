"""Карточки организаций партии 1114w (выдача sections_1114w_q.py) → auto/fetch-queue.txt, ключи sc<n>-s1114w (n — номер кандидата).
python3 tools/sections_1114w_cards.py"""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
KEEP = {2,3,4,5,14,15,16,18,19,20,21,28,30,32,34,36,37,38,39,47,49,52,53,57,58,64,68,69,71,72,73,75,76,77,79,87,88,91,96,97,98,101,103,105,107,111,112,113,116,121,122,123,125,128,129,132,134,135,139,140,151,152,153,155,156,157,160,162,165,166,168,171,182,184}
if __name__ == "__main__":
    C = json.load(open(os.path.join(ROOT, "tools/sections_1114w_cands.json")))
    urls = []
    for c in C:
        if c["n"] not in KEEP: continue
        a = re.sub(r",\s*(этаж|подъезд|вход|метро|Метро|СК |КЦ|ТЦ|зал|Центр|мкр|внешняя|есть).*$", "", c["addr"])
        if False and "Московский" not in a and "Люберцы" not in a and "Щёлково" not in a and "Балашиха" not in a and "Химки" not in a and "Реутов" not in a and "Мытищи" not in a and "Московский" not in a and "Островцы" not in a: a = "Москва, " + a
        urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?sc{c['n']}=s1114w&text=" + urllib.parse.quote(f"{c['name']}, {a}"))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
