"""Робот fun 1113f: карточки организаций Яндекса для кандидатов из выдач (fwd-<n>-1113f) → auto/fetch-queue.txt."""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PICK = [3, 29, 30, 34, 38, 43, 44, 46, 49, 52, 60, 64, 65, 68, 76, 78, 84, 93, 100, 103, 104, 113]
if __name__ == "__main__":
    C = {c["n"]: c for c in json.load(open(os.path.join(ROOT, "tools/fun_1113f_cands.json")))}
    base = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?"
    urls = [f"{base}fwd-{n}=1113f&text=" + urllib.parse.quote(C[n]["name"] + ", " + C[n]["addr"]) for n in PICK]
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
