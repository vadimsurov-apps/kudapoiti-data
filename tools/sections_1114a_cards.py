"""Карточки организаций партии 1114a (выдача sections_1114a_q.py) → auto/fetch-queue.txt, ключи sc<n>-s1114a (n — номер кандидата).
python3 tools/sections_1114a_cards.py"""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
KEEP = {11, 14, 18, 25, 27, 38, 39, 41, 42, 44, 46, 47, 48, 49, 53, 54, 55, 58, 59, 60, 61, 62, 63, 64, 68, 71, 75, 77, 78, 79, 80, 81, 82, 84, 85, 88, 92, 94, 96, 97, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 111, 112, 113, 114, 118, 119, 125, 126, 127, 128, 129, 130, 131, 132, 134, 137, 139, 141, 142, 145, 147, 148, 149, 150, 152, 155, 157, 159, 160, 161, 164, 165, 166, 167, 168, 169, 170, 171, 172, 174, 178, 179, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 198, 202, 203, 204, 205, 207, 210, 211, 212, 213, 214, 216, 218, 219, 220, 224, 228, 229, 233, 235, 236, 237, 239, 240, 241, 242, 243, 245, 246, 247, 250, 252, 253, 98, 99, 124, 143, 153, 3, 6, 91, 95}
if __name__ == "__main__":
    C = json.load(open(os.path.join(ROOT, "tools/sections_1114a_cands.json")))
    urls = []
    for c in C:
        if c["dup"] or c["n"] not in KEEP: continue
        a = re.sub(r",\s*(этаж|подъезд|вход|метро|Метро|СК |КЦ|ТЦ|зал|Центр|мкр|внешняя|есть).*$", "", c["addr"])
        if False and "Московский" not in a and "Люберцы" not in a and "Щёлково" not in a and "Балашиха" not in a and "Химки" not in a and "Реутов" not in a and "Мытищи" not in a and "Московский" not in a and "Островцы" not in a: a = "Москва, " + a
        urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?sc{c['n']}=s1114a&text=" + urllib.parse.quote(f"{c['name']}, {a}"))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
