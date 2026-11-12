"""Карточки организаций кандидатов (ключи ev<n>-1118e) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = json.load(open(os.path.join(ROOT, "tools/edu_1118_keep.json")))
DROP = {1, 3, 5, 10, 39, 42, 43, 45, 48, 58, 72, 73, 96, 97, 103, 106, 109, 115, 116, 117, 118, 120, 149, 150, 151, 152, 156, 157, 162, 176, 189, 192, 195, 209, 221}
def short(a):
    a = re.split(r", (Метро|этаж|подъезд|вход|Вход|офис|кабинет|в центр|по коридору|Школа|Нейроджимми|свободного|2 этаж)", a)[0]
    return a
urls = []
for c in K:
    if c["n"] in DROP: continue
    t = f'{c["name"]}, {short(c["addr"])}'
    urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ev{c['n']}=1118e&text=" + urllib.parse.quote(t))
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
