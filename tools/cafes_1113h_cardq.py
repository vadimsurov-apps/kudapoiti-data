"""Робот cafes 1113h: карточки (kcn<n>-1113h) и дома (kcg<n>-1113h) кандидатов → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
C = {c["n"]: c for c in json.load(open(os.path.join(ROOT, "tools/cafes_1113h_cands.json")))}
PICK = [7, 9, 11, 16, 17, 22, 26, 45, 46, 47, 48, 53, 54, 58, 59, 60, 68, 76, 80, 82, 83, 85, 87, 90, 93, 106, 110, 112, 116, 117, 124, 126, 131, 132, 135, 144, 146, 147, 152, 157, 158, 164, 170, 171]
OLD = [1, 4, 7, 13, 15, 17, 18, 19, 34, 36, 37, 38, 41, 42, 44, 46, 47, 50, 55, 56, 58, 64, 68, 72, 73, 74, 75, 76, 78, 79,
        84, 92, 100, 101, 106, 108, 109, 110, 111, 113, 115, 116, 119, 121, 122, 127, 129, 132, 137, 142, 146, 151, 157, 160]
def clean(a): return re.sub(r",\s*(этаж|вход|метро|ТЦ|БЦ|Белый дом|левое|В ресторане).*$", "", a)
if __name__ == "__main__":
    base = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?"
    urls = []
    for n in PICK:
        c = C[n]; a = clean(c["addr"])
        if c["area"] not in a and not re.search(r"Коломна|Зарайск|посёлок|Московская", a): a = c["area"] + ", " + a
        urls.append(f"{base}kcn{n}=1113h&text=" + urllib.parse.quote(f"{c['name']}, {a}"))
        urls.append(f"{base}kcg{n}=1113h&text=" + urllib.parse.quote(a))
    p = os.path.join(ROOT, "auto/fetch-queue.txt"); old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old); print(len(urls))
