"""Робот cafes 1113k: карточки (kcn<n>-1113k) и дома (kcg<n>-1113k) кандидатов → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
C = {c["n"]: c for c in json.load(open(os.path.join(ROOT, "tools/cafes_1113k_cands.json")))}
PICK = [4, 9, 11, 16, 23, 24, 25, 33, 39, 42, 43, 44, 48, 50, 51, 53, 56, 59, 64, 68, 72, 73, 75, 78, 80, 83, 85, 86, 87, 91, 95, 97, 99, 106, 112, 113, 122, 125, 126, 127, 128, 129, 132, 137, 139, 140, 142, 147, 148, 149, 150, 153, 156]
def clean(a): return re.sub(r",\s*(этаж|вход|метро|ТЦ|БЦ|Белый дом|левое|В ресторане).*$", "", a)
if __name__ == "__main__":
    base = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?"
    urls = []
    for n in PICK:
        c = C[n]; a = clean(c["addr"])
        if c["area"] not in a and not re.search(r"Коломна|Москва|Балашиха|Королёв|Реутов|посёлок|Московская|д\\. |п\\. г\\. т|рабочий", a): a = c["area"] + ", " + a
        urls.append(f"{base}kcn{n}=1113k&text=" + urllib.parse.quote(f"{c['name']}, {a}"))
        urls.append(f"{base}kcg{n}=1113k&text=" + urllib.parse.quote(a))
    p = os.path.join(ROOT, "auto/fetch-queue.txt"); old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old); print(len(urls))
