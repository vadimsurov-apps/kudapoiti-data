"""Карточки кандидатов «Особым детям» (ключи ev<n>-1119e, n ≥ 300) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = json.load(open(os.path.join(ROOT, "tools/edu_1119_keep2.json")))
TAKE = {301, 302, 310, 313, 316, 336, 337, 338, 321, 328, 340}
urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ev{c['n']}=1119e&text=" + urllib.parse.quote(f'{c["name"]}, {re.split(r", (этаж|помещение|корп)", c["addr"])[0]}') for c in K if c["n"] in TAKE]
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/fetch-queue.txt"); old = open(p).read()
    if urls[0] not in old: open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
