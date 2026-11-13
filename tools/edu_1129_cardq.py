"""Робот edu 13.11 (девятнадцатый запуск). Карточки организаций отобранных кандидатов (ключи ev<n>-1129e) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = json.load(open(os.path.join(ROOT, "tools/edu_1129_keep.json")))
TAKE = set([0,2,4,5,6,10,11,12,14,15,16,17,22,23,24,25,26,27,30,31,32,34,35,36,37,40,41,43,45,46,47,48,49,50,51,52,53,54,56,58,60,61,63,64,68,70,76,77,78,79,80,82,83,89,91,92,93,96,98,99,100,101,102,103,104,105,106,107,108,112,113,114,116,118,119,120,121,125,131,132,134,135,136,137,142,144,146,147,148,149,150,151,153,155,156,158,160,162,166,173,174,178,179,180,188,190,192,197,198,199,200,201,202,203,204,205,209,210,214,216,217])
def short(a):
    return re.split(r", (Метро|метро|этаж|подъезд|вход|Вход|офис|кабинет|в помещ|домофон|жилой|ЖК|Отдельный|Пройдите)", a)[0]
urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ev{c['n']}=1129e&text=" + urllib.parse.quote(f'{c["name"]}, {short(c["addr"])}')
        for c in K if c["n"] in TAKE]
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
