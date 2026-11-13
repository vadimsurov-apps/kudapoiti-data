"""Карточки организаций партии 1113j (выдача sections_1113j_q.py) → auto/fetch-queue.txt, ключи sc<n>-s1113j (n — номер кандидата).
python3 tools/sections_1113j_cards.py"""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
KEEP = {1,4,12,13,19,40,49,55,56,60,63,65,68,71,74,76,81,87,88,97,102,107,109,119,123,129,130,131,134,135,140,141,145,151,153,155,156,159,166,168,170}
if __name__ == "__main__":
    C = json.load(open(os.path.join(ROOT, "tools/sections_1113j_cands.json")))
    urls = []
    for c in C:
        if c["dup"] or c["n"] not in KEEP: continue
        a = re.sub(r",\s*(этаж|подъезд|вход|метро|Метро|СК |КЦ|ТЦ|зал|Центр|мкр|внешняя|есть).*$", "", c["addr"])
        if "Москва" not in a and "Московский" not in a and "Люберцы" not in a and "Щёлково" not in a: a = "Москва, " + a
        urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?sc{c['n']}=s1113j&text=" + urllib.parse.quote(f"{c['name']}, {a}"))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
