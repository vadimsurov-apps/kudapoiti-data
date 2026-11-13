"""Робот edu 13.11 (двадцать первый запуск). Карточки организаций отобранных кандидатов (ключи ev<n>-1131e) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = json.load(open(os.path.join(ROOT, "tools/edu_1131_keep.json")))
EXCL = {48,56,64,68,70,174,226,230,25,26,27,9,12,13,63,99,108,185,200,201,202,203,218,105,111,114,220,223,224,239,57,58,60,121,122,228,5,184}
TAKE = {c["n"] for c in K} - EXCL
def short(a):
    return re.split(r", (Метро|метро|этаж|подъезд|вход|Вход|офис|кабинет|в помещ|домофон|жилой|ЖК|Отдельный|Пройдите)", a)[0]
urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ev{c['n']}=1131e&text=" + urllib.parse.quote(f'{c["name"]}, {short(c["addr"])}')
        for c in K if c["n"] in TAKE]
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
