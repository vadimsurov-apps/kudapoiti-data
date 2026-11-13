"""Робот edu 13.11. Карточки организаций отобранных кандидатов (ключи ev<n>-1124e) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = json.load(open(os.path.join(ROOT, "tools/edu_1124_keep.json")))
TAKE = {88,89,127,128,163,252,165,201,205,210,239,258,101,58,162,79,229,21,30,50,97,
        43,44,78,80,120,187,198,47,
        7,11,12,13,60,61,123,63,124,126,141,143,167,170,212,220,240,
        64,65,67,68,105,106,107,109,157,191,192,194,16,
        214,15,34,66,139,49,
        4,8,17,53,62,69,72,136,158,168,174,178,185,197,216}
def short(a):
    return re.split(r", (Метро|этаж|подъезд|вход|Вход|офис|кабинет|в помещ|домофон|жилой|ЖК)", a)[0]
urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ev{c['n']}=1124e&text=" + urllib.parse.quote(f'{c["name"]}, {short(c["addr"])}')
        for c in K if c["n"] in TAKE]
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
