"""Карточки организаций партии 1114zc (выдача sections_1114zc_q.py) → auto/fetch-queue.txt, ключи sc<n>-s1114zc (n — номер кандидата).
python3 tools/sections_1114zc_cards.py"""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
KEEP = {12,16,30,36,38,48,57,61,96,97,102,115,116,119,122,124,126,127,128,132,133,137,144,147,155,156,161,162,164,166,168,169,176,179,180,181,184,186,191,196,201,203}
if __name__ == "__main__":
    C = json.load(open(os.path.join(ROOT, "tools/sections_1114zc_cands.json")))
    urls = []
    for c in C:
        if c["n"] not in KEEP: continue
        a = re.sub(r",\s*(этаж|подъезд|вход|метро|Метро|СК |КЦ|ТЦ|зал|Центр|мкр|внешняя|есть).*$", "", c["addr"])
        if False and "Московский" not in a and "Люберцы" not in a and "Щёлково" not in a and "Балашиха" not in a and "Химки" not in a and "Реутов" not in a and "Мытищи" not in a and "Московский" not in a and "Островцы" not in a: a = "Москва, " + a
        urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?sc{c['n']}=s1114zc&text=" + urllib.parse.quote(f"{c['name']}, {a}"))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
