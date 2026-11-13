"""Карточки организаций партии 1113h (выдача sections_1113h_q.py) → auto/fetch-queue.txt, ключи sc<n>-s1113h (n — номер кандидата).
python3 tools/sections_1113h_cards.py"""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
KEEP = {14,16,17,23,24,32,50,51,52,53,64,65,66,68,71,75,79,92,96,97,108,109,110,112,113,115,117,119,120,121,124,133,134,135,140,141,142,147,151,152,154,158,159,162,164,165,166,167,168,170,171}
if __name__ == "__main__":
    C = json.load(open(os.path.join(ROOT, "tools/sections_1113h_cands.json")))
    urls = []
    for c in C:
        if c["dup"] or c["n"] not in KEEP: continue
        a = re.sub(r",\s*(этаж|подъезд|вход|метро|Метро|СК |КЦ|ТЦ|зал|Центр|мкр|внешняя|есть).*$", "", c["addr"])
        if "Москва" not in a and "Люберцы" not in a: a = "Москва, " + a
        urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?sc{c['n']}=s1113h&text=" + urllib.parse.quote(f"{c['name']}, {a}"))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
