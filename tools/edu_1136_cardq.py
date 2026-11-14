"""Робот edu 14.11 (двадцать шестой запуск). Карточки организаций отобранных кандидатов (ключи ev<n>-1136e, волна 2 — ev<n>-1136g) → auto/fetch-queue.txt.
Не берём рубрики вне области edu: бассейны, школы искусств, общеобразовательные школы, клиники, творческие коллективы."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
BAD = re.compile(r"(Бассейн|Обучение плаванию|Школа искусств|Общеобразовательная школа|Начальная школа|Творческий коллектив|Медцентр|клиника|Больница|Поликлиника|Стоматолог|Театральное образование|Школа танцев|Музыкальное образование|Спортивн|Фитнес|Салон|Магазин|ВУЗ|Колледж|Курсы и мастер-классы)", re.I)
OUT = ("Тула", "Обнинск", "Калуга", "Тверь", "Рязань", "Владимир,", "Ярославль", "Санкт", "Нижний", "Сергиев")
def short(a):
    return re.split(r", (Метро|метро|этаж|подъезд|вход|Вход|офис|кабинет|в помещ|домофон|жилой|ЖК|Отдельный|Пройдите)", a)[0]
urls, n = [], 0
for f, tag in (("edu_1136_keep.json", "1136e"), ("edu_1136_keep2.json", "1136g")):
    for c in json.load(open(os.path.join(ROOT, "tools", f))):
        if BAD.search(c["rubric"]) and not re.search(r"(ОВЗ|инклюз|аутизм|особ)", c["name"] + c["rubric"], re.I): continue
        if any(c["addr"].startswith(o) or (", " + o) in c["addr"] for o in OUT): continue
        urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ev{c['n']}={tag}&text=" + urllib.parse.quote(f'{c["name"]}, {short(c["addr"])}'))
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
