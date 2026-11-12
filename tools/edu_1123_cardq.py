"""Карточки организаций отобранных кандидатов (ключи ev<n>-1123e) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = json.load(open(os.path.join(ROOT, "tools/edu_1123_keep.json")))
TAKE = {12,74,77,92,158,159,176,227,228,241,254,213,204,198,248,256,257,258,25,26,28,147,193,10,229,
        8,9,36,37,38,39,69,71,72,73,94,95,96,97,129,130,131,132,133,151,187,188,215,216,217,218,
        3,5,6,11,22,40,43,49,53,65,99,100,103,110,137,142,149,155,157,196,212,214,224,242,245,52,86,87,90,54,64,68}
def short(a):
    return re.split(r", (Метро|этаж|подъезд|вход|Вход|офис|кабинет|в помещ|домофон|жилой|ЖК)", a)[0]
urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ev{c['n']}=1123e&text=" + urllib.parse.quote(f'{c["name"]}, {short(c["addr"])}')
        for c in K if c["n"] in TAKE]
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
