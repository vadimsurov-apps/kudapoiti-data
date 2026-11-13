"""Робот edu 13.11 (шестнадцатый запуск). Карточки организаций отобранных кандидатов (ключи ev<n>-1126e) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = json.load(open(os.path.join(ROOT, "tools/edu_1126_keep.json")))
TAKE = {2,6,7,12,14,15,16,17,18,21,24,28,29,30,32,34,37,38,40,41,43,44,45,48,50,52,56,59,60,62,64,65,69,71,72,74,75,80,83,87,89,90,100,102,104,
        111,112,113,114,122,124,126,129,131,133,135,136,137,139,140,141,145,147,152,154,155,160,163,164,165,166,167,168,169,171,172,173,174,175,
        181,182,183,185,188,189,191,197,198,199,201,202,203,205,213,214,215,217,220,223,232,234,235,240,241,242,243,244,247,252,253,254,255,256,257,
        260,261,263,264,265,266,267}
def short(a):
    return re.split(r", (Метро|метро|этаж|подъезд|вход|Вход|офис|кабинет|в помещ|домофон|жилой|ЖК|Отдельный|Пройдите)", a)[0]
urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ev{c['n']}=1126e&text=" + urllib.parse.quote(f'{c["name"]}, {short(c["addr"])}')
        for c in K if c["n"] in TAKE]
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
