"""Робот cafes 1114c: карточки (kcn<n>-1114c) и дома (kcg<n>-1114c) кандидатов → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
C = {c["n"]: c for c in json.load(open(os.path.join(ROOT, "tools/cafes_1114c_cands.json")))}
PICK = json.load(open(os.path.join(ROOT, "tools/cafes_1114c_pick.json")))
def clean(a): return re.sub(r",\s*(этаж|вход|метро|ТЦ|БЦ|Белый дом|левое|В ресторане).*$", "", a)
if __name__ == "__main__":
    base = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?"
    urls = []
    for n in PICK:
        c = C[n]; a = clean(c["addr"])
        if c["area"] not in a and not re.search(r"Коломна|Москва|Балашиха|Королёв|Реутов|посёлок|Московская|д\\. |п\\. г\\. т|рабочий", a): a = c["area"] + ", " + a
        urls.append(f"{base}kcn{n}=1114c&text=" + urllib.parse.quote(f"{c['name']}, {a}"))
        urls.append(f"{base}kcg{n}=1114c&text=" + urllib.parse.quote(a))
    p = os.path.join(ROOT, "auto/fetch-queue.txt"); old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old); print(len(urls))
