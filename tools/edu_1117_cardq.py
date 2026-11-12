"""Карточки организаций кандидатов (ключи ev<n>-1117e) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = json.load(open(os.path.join(ROOT, "tools/edu_1117_keep.json")))
DROP = {0, 3, 4, 5, 8, 12, 16, 17, 26, 42, 43, 44, 56, 58, 59, 60, 79, 117, 121, 129, 138, 139, 151, 153, 155, 158, 160, 166, 167, 181, 183, 189, 196, 209, 212}
def short(a):
    a = re.split(r", (Метро|этаж|подъезд|вход|Вход|офис|кабинет|в центр|по коридору|Школа|Нейроджимми|свободного|2 этаж)", a)[0]
    return a
urls = []
for c in K:
    if c["n"] in DROP: continue
    t = f'{c["name"]}, {short(c["addr"])}'
    urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ev{c['n']}=1117e&text=" + urllib.parse.quote(t))
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
