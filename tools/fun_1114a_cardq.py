"""Робот fun 1114a: карточки организаций Яндекса для кандидатов из выдач (fxd-<n>-1114a) → auto/fetch-queue.txt."""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PICK = [1, 4, 5, 13, 15, 16, 18, 30, 32, 38, 40, 41, 55, 63, 68, 72, 79, 80]
if __name__ == "__main__":
    C = {c["n"]: c for c in json.load(open(os.path.join(ROOT, "tools/fun_1114a_cands.json")))}
    base = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?"
    urls = [f"{base}fxd-{n}=1114a&text=" + urllib.parse.quote(C[n]["name"] + ", " + C[n]["addr"]) for n in PICK]
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
