"""Карточки организаций партии 1113g (выдача sections_1113g_q.py) → auto/fetch-queue.txt, ключи sc<n>-s1113g (n — номер кандидата).
python3 tools/sections_1113g_cards.py"""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SKIP = {72, 148, 75, 158, 157, 159, 113, 132, 12, 100, 161, 47}
if __name__ == "__main__":
    C = json.load(open(os.path.join(ROOT, "tools/sections_1113g_cands.json")))
    urls = []
    for c in C:
        if c["dup"] or c["n"] in SKIP: continue
        a = re.sub(r",\s*(этаж|подъезд|вход|метро|Метро|СК |КЦ|ТЦ|зал|Центр|мкр|внешняя|есть).*$", "", c["addr"])
        if "Москва" not in a and "Люберцы" not in a: a = "Москва, " + a
        urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?sc{c['n']}=s1113g&text=" + urllib.parse.quote(f"{c['name']}, {a}"))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
