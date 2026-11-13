"""Робот cafes 1113x: карточки (kcn<n>-1113x) и дома (kcg<n>-1113x) кандидатов → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
C = {c["n"]: c for c in json.load(open(os.path.join(ROOT, "tools/cafes_1113x_cands.json")))}
PICK = [3,5,7,8,10,11,23,24,26,28,31,34,37,41,47,50,57,60,62,65,67,74,75,81,85,86,87,89,97,100,102,104,105,112,113,116,121,123,129,132,133,137,138]
def clean(a): return re.sub(r",\s*(этаж|вход|метро|ТЦ|БЦ|Белый дом|левое|В ресторане).*$", "", a)
if __name__ == "__main__":
    base = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?"
    urls = []
    for n in PICK:
        c = C[n]; a = clean(c["addr"])
        if c["area"] not in a and not re.search(r"Коломна|Москва|Балашиха|Королёв|Реутов|посёлок|Московская|д\\. |п\\. г\\. т|рабочий", a): a = c["area"] + ", " + a
        urls.append(f"{base}kcn{n}=1113x&text=" + urllib.parse.quote(f"{c['name']}, {a}"))
        urls.append(f"{base}kcg{n}=1113x&text=" + urllib.parse.quote(a))
    p = os.path.join(ROOT, "auto/fetch-queue.txt"); old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old); print(len(urls))
