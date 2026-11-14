"""Робот edu 14.11 (двадцать четвёртый запуск), вторая волна (особым детям): карточки организаций (ключи ev<n>-1134g) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = json.load(open(os.path.join(ROOT, "tools/edu_1134_keep2.json")))
TAKE = {1, 2, 3, 5, 9, 22, 31, 35, 45, 50, 66, 67, 69, 70, 72, 96, 98, 101, 108, 135, 142, 146, 157, 158, 162, 169, 171, 173, 174, 175, 176, 177, 178, 182, 183, 184, 185, 187, 189, 192, 193, 194, 196, 200, 210, 211, 212, 214, 215, 217, 219, 220, 229}
def short(a):
    return re.split(r", (Метро|метро|этаж|подъезд|вход|Вход|офис|кабинет|в помещ|домофон|жилой|ЖК|Отдельный|Пройдите|слева)", a)[0]
urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ev{c['n']}=1134g&text=" + urllib.parse.quote(f'{c["name"]}, {short(c["addr"])}')
        for c in K if c["n"] in TAKE]
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
