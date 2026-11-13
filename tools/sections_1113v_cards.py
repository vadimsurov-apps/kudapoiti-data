"""Карточки организаций партии 1113v (выдача sections_1113v_q.py) → auto/fetch-queue.txt, ключи sc<n>-s1113v (n — номер кандидата).
python3 tools/sections_1113v_cards.py"""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
KEEP = {4,11,13,15,22,23,24,36,37,38,39,41,43,44,46,48,49,50,57,58,59,63,77,79,81,85,90,94,100,105,109,110,114,116,117,121,128,131,135,136,137,140,142,144,145,147,149,151,155,158,162,171,173,174,175,176,181,184,189,190,191,193,194,202,208}
if __name__ == "__main__":
    C = json.load(open(os.path.join(ROOT, "tools/sections_1113v_cands.json")))
    urls = []
    for c in C:
        if c["dup"] or c["n"] not in KEEP: continue
        a = re.sub(r",\s*(этаж|подъезд|вход|метро|Метро|СК |КЦ|ТЦ|зал|Центр|мкр|внешняя|есть).*$", "", c["addr"])
        if "Москва" not in a and "Московский" not in a and "Люберцы" not in a and "Щёлково" not in a and "Балашиха" not in a and "Химки" not in a and "Реутов" not in a and "Мытищи" not in a and "Московский" not in a and "Островцы" not in a: a = "Москва, " + a
        urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?sc{c['n']}=s1113v&text=" + urllib.parse.quote(f"{c['name']}, {a}"))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
