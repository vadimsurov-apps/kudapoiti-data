"""Карточки организаций партии 1114zg (выдача sections_1114zg_q.py) → auto/fetch-queue.txt, ключи sc<n>-s1114zg (n — номер кандидата).
python3 tools/sections_1114zg_cards.py"""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
KEEP = {0,2,3,16,18,59,60,68,86,87,93,109,110,121,127,131,139,144,152,159,178,179,180,183,184,186,201,205,211,215,235,247,250,263,264,273,276,294,297,299,301,306,310,312,317,321,346,349,361}
if __name__ == "__main__":
    C = json.load(open(os.path.join(ROOT, "tools/sections_1114zg_cands.json")))
    urls = []
    for c in C:
        if c["n"] not in KEEP: continue
        a = re.sub(r",\s*(этаж|подъезд|вход|метро|Метро|СК |КЦ|ТЦ|зал|Центр|мкр|внешняя|есть).*$", "", c["addr"])
        if False and "Московский" not in a and "Люберцы" not in a and "Щёлково" not in a and "Балашиха" not in a and "Химки" not in a and "Реутов" not in a and "Мытищи" not in a and "Московский" not in a and "Островцы" not in a: a = "Москва, " + a
        urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?sc{c['n']}=s1114zg&text=" + urllib.parse.quote(f"{c['name']}, {a}"))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
