"""Робот edu 14.11 (двадцать пятый запуск). Карточки организаций отобранных кандидатов (ключи ev<n>-1135e) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = json.load(open(os.path.join(ROOT, "tools/edu_1135_keep.json")))
EXCL = {0,1,3,5,6,27,31,32,35,36,37,38,40,46,49,51,52,74,76,77,78,79,81,92,133,159,160,177,188,189,197,200,214,218,222,223,225,226,227,231,237,253,277,291,292,294,295,297,298,299,302,305,306,307,308,309,316,325}  # бассейны, спорт, клиники, общеобразовательные школы, искусство
OUT = ("Тула", "Обнинск", "Калуга", "Тверь", "Рязань", "Владимир,", "Ярославль", "Санкт", "Нижний", "Сергиев")
TAKE = {c["n"] for c in K if not any(c["addr"].startswith(o) or (", " + o) in c["addr"] for o in OUT)} - EXCL
def short(a):
    return re.split(r", (Метро|метро|этаж|подъезд|вход|Вход|офис|кабинет|в помещ|домофон|жилой|ЖК|Отдельный|Пройдите)", a)[0]
urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ev{c['n']}=1135e&text=" + urllib.parse.quote(f'{c["name"]}, {short(c["addr"])}')
        for c in K if c["n"] in TAKE]
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
