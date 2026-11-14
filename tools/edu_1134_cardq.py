"""Робот edu 14.11 (двадцать четвёртый запуск). Карточки организаций отобранных кандидатов (ключи ev<n>-1134e) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = json.load(open(os.path.join(ROOT, "tools/edu_1134_keep.json")))
EXCL = {6,16,28,31,32,33,36,38,55,77,113,120,121,125,131,136,144,158,159,162,194,197,200,215,219,222,227,238,254,260,274,279,281,282,284,296,297,298,299,303,308,312,314,318,352,354,355,356}  # бассейны, спорт, клиники, общеобразовательные школы, искусство
OUT = ("Тула", "Обнинск", "Калуга", "Тверь", "Рязань", "Владимир,", "Ярославль", "Санкт", "Нижний", "Сергиев")
TAKE = {c["n"] for c in K if not any(c["addr"].startswith(o) or (", " + o) in c["addr"] for o in OUT)} - EXCL
def short(a):
    return re.split(r", (Метро|метро|этаж|подъезд|вход|Вход|офис|кабинет|в помещ|домофон|жилой|ЖК|Отдельный|Пройдите)", a)[0]
urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ev{c['n']}=1134e&text=" + urllib.parse.quote(f'{c["name"]}, {short(c["addr"])}')
        for c in K if c["n"] in TAKE]
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
