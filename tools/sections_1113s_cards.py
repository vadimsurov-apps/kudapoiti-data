"""Карточки организаций партии 1113s (выдача sections_1113s_q.py) → auto/fetch-queue.txt, ключи sc<n>-s1113s (n — номер кандидата).
python3 tools/sections_1113s_cards.py"""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
KEEP = {6,7,8,12,15,16,24,27,29,34,38,39,42,43,44,45,46,49,55,56,57,58,63,69,72,79,84,86,89,91,102,105,114,116,118,119,120,122,128,131,132,138,139,142,144,146,154,157,158,163,169,179,183,185,187,188,196,199,201,202,211,225,226}
if __name__ == "__main__":
    C = json.load(open(os.path.join(ROOT, "tools/sections_1113s_cands.json")))
    urls = []
    for c in C:
        if c["dup"] or c["n"] not in KEEP: continue
        a = re.sub(r",\s*(этаж|подъезд|вход|метро|Метро|СК |КЦ|ТЦ|зал|Центр|мкр|внешняя|есть).*$", "", c["addr"])
        if "Москва" not in a and "Московский" not in a and "Люберцы" not in a and "Щёлково" not in a and "Балашиха" not in a and "Химки" not in a and "Реутов" not in a and "Мытищи" not in a and "Московский" not in a and "Островцы" not in a: a = "Москва, " + a
        urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?sc{c['n']}=s1113s&text=" + urllib.parse.quote(f"{c['name']}, {a}"))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
