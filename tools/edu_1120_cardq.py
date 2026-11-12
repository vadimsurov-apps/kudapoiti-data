"""Карточки организаций кандидатов (ключи ev<n>-1120e) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = json.load(open(os.path.join(ROOT, "tools/edu_1120_keep.json")))
DROP = {17,20,24,26,38,41,45,49,51,52,67,68,69,72,73,74,76,78,83,91,92,106,118,119,120,124,134,137,140,154,157,167,179,185,191,192,193,202,203,204,210,211,212,213,214,220,223,224,225,226,230,231,232,237}
def short(a):
    a = re.split(r", (Метро|этаж|подъезд|вход|Вход|офис|кабинет|в центр|по коридору|Школа|Нейроджимми|свободного|2 этаж)", a)[0]
    return a
urls = []
for c in K:
    if c["n"] in DROP: continue
    t = f'{c["name"]}, {short(c["addr"])}'
    urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ev{c['n']}=1120e&text=" + urllib.parse.quote(t))
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
