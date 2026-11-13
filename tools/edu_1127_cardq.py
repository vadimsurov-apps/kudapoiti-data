"""Робот edu 13.11 (семнадцатый запуск). Карточки организаций отобранных кандидатов (ключи ev<n>-1127e) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = json.load(open(os.path.join(ROOT, "tools/edu_1127_keep.json")))
TAKE = {0,2,9,13,15,16,17,18,20,21,23,25,27,28,29,30,31,33,35,37,38,42,47,48,49,51,56,57,59,63,67,70,72,76,78,83,85,86,89,90,91,100,101,102,105,107,
        109,111,112,115,116,117,118,119,123,126,127,129,130,131,133,134,136,139,144,146,147,153,155,157,158,161,163,167,169,175,176,177,178,181,182,183,
        184,185,187,190,193,197,199,201,202,204,206,208,213,214,215,216,221,222,223,228,229,232,236,237,244,245,247,248,249,250,255,260,266,267,268,269,270,272,273,274,275,279,280,281}
def short(a):
    return re.split(r", (Метро|метро|этаж|подъезд|вход|Вход|офис|кабинет|в помещ|домофон|жилой|ЖК|Отдельный|Пройдите)", a)[0]
urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ev{c['n']}=1127e&text=" + urllib.parse.quote(f'{c["name"]}, {short(c["addr"])}')
        for c in K if c["n"] in TAKE]
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
