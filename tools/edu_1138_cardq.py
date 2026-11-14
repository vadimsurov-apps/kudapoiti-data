"""Робот edu 14.11 (28-й запуск): карточки организаций кандидатов, для которых нашлось здание OSM (ключи ev<n>-1138e) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
def short(a):
    return re.split(r", (Метро|метро|этаж|подъезд|вход|Вход|офис|кабинет|помещ|домофон|жилой|ЖК|Отдельный|Пройдите|цокольный|г\. )", a)[0]
K = json.load(open(os.path.join(ROOT, "tools/edu_1138_keep.json")))
SKIP = {75}  # студия звукозаписи — не детское занятие
urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ev{c['n']}=1138e&text=" + urllib.parse.quote(f'{c["name"]}, {short(c["addr"])}') for c in K if c["pt"] and c["n"] not in SKIP]
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
