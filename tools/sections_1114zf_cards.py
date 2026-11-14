"""Карточки организаций партии 1114zf (выдача sections_1114zf_q.py) → auto/fetch-queue.txt, ключи sc<n>-s1114zf (n — номер кандидата).
python3 tools/sections_1114zf_cards.py"""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
KEEP = {3,4,6,20,26,41,42,44,45,47,51,56,63,64,65,66,68,74,75,82,83,92,95,96,104,112,114,115,119,123,128,131,133,134,135,140,141,143,145,149,152,154,161,166,171,189,190,195,197,198,199,200,201,202,205,207,210,211,212,214,218,220,221,223,231,238,245,246,250,256,259,262,263,264,266,267,268,272,273,275,281,283,284,291,293,296,300,306,309,310,312,313,318,319,326,327,331,339,340,341,342,343,344,348,349,350,352,353,355,361,363,364,368,370,375,378,379,384}
if __name__ == "__main__":
    C = json.load(open(os.path.join(ROOT, "tools/sections_1114zf_cands.json")))
    urls = []
    for c in C:
        if c["n"] not in KEEP: continue
        a = re.sub(r",\s*(этаж|подъезд|вход|метро|Метро|СК |КЦ|ТЦ|зал|Центр|мкр|внешняя|есть).*$", "", c["addr"])
        if False and "Московский" not in a and "Люберцы" not in a and "Щёлково" not in a and "Балашиха" not in a and "Химки" not in a and "Реутов" not in a and "Мытищи" not in a and "Московский" not in a and "Островцы" not in a: a = "Москва, " + a
        urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?sc{c['n']}=s1114zf&text=" + urllib.parse.quote(f"{c['name']}, {a}"))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
