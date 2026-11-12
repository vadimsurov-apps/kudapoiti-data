"""Карточки организаций кандидатов (ключи ev<n>-1119e) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = json.load(open(os.path.join(ROOT, "tools/edu_1119_keep.json")))
DROP = {2, 3, 7, 11, 12, 15, 16, 20, 27, 33, 43, 46, 48, 49, 54, 58, 64, 75, 78, 89, 94, 114, 117, 119, 143, 144, 161, 165, 167, 168, 180, 184, 185, 187, 193, 194, 195, 199, 205, 206, 207, 208, 209, 214, 230, 232, 234}
def short(a):
    a = re.split(r", (Метро|этаж|подъезд|вход|Вход|офис|кабинет|в центр|по коридору|Школа|Нейроджимми|свободного|2 этаж)", a)[0]
    return a
urls = []
for c in K:
    if c["n"] in DROP: continue
    t = f'{c["name"]}, {short(c["addr"])}'
    urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ev{c['n']}=1119e&text=" + urllib.parse.quote(t))
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
