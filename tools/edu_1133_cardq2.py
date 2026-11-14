"""Робот edu 14.11 (двадцать третий запуск), вторая волна (особым детям): карточки организаций (ключи ev<n>-1133g) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = json.load(open(os.path.join(ROOT, "tools/edu_1133_keep2.json")))
TAKE = {0, 3, 4, 5, 6, 7, 16, 19, 20, 21, 22, 26, 27, 30, 35, 40, 48, 54, 59, 71, 73, 74, 75, 76, 77}
def short(a):
    return re.split(r", (Метро|метро|этаж|подъезд|вход|Вход|офис|кабинет|в помещ|домофон|жилой|ЖК|Отдельный|Пройдите|слева)", a)[0]
urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ev{c['n']}=1133g&text=" + urllib.parse.quote(f'{c["name"]}, {short(c["addr"])}')
        for c in K if c["n"] in TAKE]
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
