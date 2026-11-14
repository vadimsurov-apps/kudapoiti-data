"""Робот edu 14.11 (двадцать третий запуск). Карточки организаций отобранных кандидатов (ключи ev<n>-1133e) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = json.load(open(os.path.join(ROOT, "tools/edu_1133_keep.json")))
EXCL = {5,16,37,38,40,62,64,82,102,103,108,139,140,141,150,154,155,163,169,171,175,190,193,211,212,226,228,288,308,313,314,317,319,320,323,327,342,345}
OUT = ("Тула", "Обнинск", "Калуга", "Тверь", "Рязань", "Владимир,", "Ярославль", "Санкт", "Нижний", "Сергиев")
TAKE = {c["n"] for c in K if not any(c["addr"].startswith(o) or (", " + o) in c["addr"] for o in OUT)} - EXCL
def short(a):
    return re.split(r", (Метро|метро|этаж|подъезд|вход|Вход|офис|кабинет|в помещ|домофон|жилой|ЖК|Отдельный|Пройдите)", a)[0]
urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ev{c['n']}=1133e&text=" + urllib.parse.quote(f'{c["name"]}, {short(c["addr"])}')
        for c in K if c["n"] in TAKE]
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
