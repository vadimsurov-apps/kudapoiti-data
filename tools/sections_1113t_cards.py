"""Карточки организаций партии 1113t (выдача sections_1113t_q.py) → auto/fetch-queue.txt, ключи sc<n>-s1113t (n — номер кандидата).
python3 tools/sections_1113t_cards.py"""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
KEEP = {2,3,4,10,13,22,27,28,31,34,35,39,40,41,44,48,49,50,52,53,54,56,57,60,61,65,71,73,74,75,81,82,84,85,86,88,92,93,95,96,105,106,108,110,111,115,121,123,125,127,128,129,132,133,134,140,142,152,153,154,155,156,159,161,166,167,169,170,171,178,179,180,181,187,193,205,211,217,218,221,222,223,226,229,231,232,235,236,238,242,243,247,249,250,251}
if __name__ == "__main__":
    C = json.load(open(os.path.join(ROOT, "tools/sections_1113t_cands.json")))
    urls = []
    for c in C:
        if c["dup"] or c["n"] not in KEEP: continue
        a = re.sub(r",\s*(этаж|подъезд|вход|метро|Метро|СК |КЦ|ТЦ|зал|Центр|мкр|внешняя|есть).*$", "", c["addr"])
        if "Москва" not in a and "Московский" not in a and "Люберцы" not in a and "Щёлково" not in a and "Балашиха" not in a: a = "Москва, " + a
        urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?sc{c['n']}=s1113t&text=" + urllib.parse.quote(f"{c['name']}, {a}"))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
