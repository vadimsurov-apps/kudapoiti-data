"""Робот cafes 1113g: карточки (kcn<n>-1113g) и дома (kcg<n>-1113g) кандидатов → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
C = {c["n"]: c for c in json.load(open(os.path.join(ROOT, "tools/cafes_1113g_cands.json")))}
PICK = [1, 4, 7, 13, 15, 17, 18, 19, 34, 36, 37, 38, 41, 42, 44, 46, 47, 50, 55, 56, 58, 64, 68, 72, 73, 74, 75, 76, 78, 79,
        84, 92, 100, 101, 106, 108, 109, 110, 111, 113, 115, 116, 119, 121, 122, 127, 129, 132, 137, 142, 146, 151, 157, 160]
def clean(a): return re.sub(r",\s*(этаж|вход|метро|ТЦ|БЦ|Белый дом|левое|В ресторане).*$", "", a)
if __name__ == "__main__":
    base = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?"
    urls = []
    for n in PICK:
        c = C[n]; a = clean(c["addr"])
        if not re.search(r"Москва|Дзержинский|Реутов|посёлок|Московский", a): a = "Москва, " + a
        urls.append(f"{base}kcn{n}=1113g&text=" + urllib.parse.quote(f"{c['name']}, {a}"))
        urls.append(f"{base}kcg{n}=1113g&text=" + urllib.parse.quote(a))
    p = os.path.join(ROOT, "auto/fetch-queue.txt"); old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old); print(len(urls))
