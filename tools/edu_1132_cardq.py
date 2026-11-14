"""Робот edu 14.11 (двадцать второй запуск). Карточки организаций отобранных кандидатов (ключи ev<n>-1132e) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = json.load(open(os.path.join(ROOT, "tools/edu_1132_keep.json")))
EXCL = {1,121,4,5,7,8,16,18,22,31,32,43,67,70,98,106,125,126,127,128,145,146,170,171,172,173,174,176,185,188,191,213,214,215,222,223,248,256,258,259,273,275,287,290,309,310,311,312,319,320,321,325,326,327,331,334,355,370}
TAKE = {c["n"] for c in K} - EXCL
def short(a):
    return re.split(r", (Метро|метро|этаж|подъезд|вход|Вход|офис|кабинет|в помещ|домофон|жилой|ЖК|Отдельный|Пройдите)", a)[0]
urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ev{c['n']}=1132e&text=" + urllib.parse.quote(f'{c["name"]}, {short(c["addr"])}')
        for c in K if c["n"] in TAKE]
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
