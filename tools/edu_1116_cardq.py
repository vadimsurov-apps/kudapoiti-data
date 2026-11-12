"""Карточки организаций кандидатов (ключи ev<n>-1116e) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = json.load(open(os.path.join(ROOT, "tools/edu_1116_keep.json")))
DROP = {52, 62, 101, 104, 114, 115, 121, 122, 129, 133, 135, 137, 138, 141, 142, 168}
def short(a):
    a = re.split(r", (Метро|этаж|подъезд|вход|Вход|офис|кабинет|в центр|по коридору|Школа|Нейроджимми|свободного|2 этаж)", a)[0]
    return a
urls = []
for c in K:
    if c["n"] in DROP: continue
    t = f'{c["name"]}, {short(c["addr"])}'
    urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ev{c['n']}=1116e&text=" + urllib.parse.quote(t))
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
