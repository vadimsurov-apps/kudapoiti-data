"""Робот edu 13.11 (пятнадцатый запуск). Карточки организаций отобранных кандидатов (ключи ev<n>-1125e) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = json.load(open(os.path.join(ROOT, "tools/edu_1125_keep.json")))
TAKE = {20,22,23,29,36,45,46,51,54,79,85,103,117,121,151,178,182,190,192,203,204,205,217,253,255,256,264,270,271,272,273,274,275,276,278,
        8,9,10,12,32,70,89,91,114,126,138,146,193,207,244,246,277,
        39,40,41,105,106,107,170,171,108,109,96,225,
        124,169,202,179,58,60,184,241,
        26,31,62,88,122,143,164,167,233,235,239}
def short(a):
    return re.split(r", (Метро|метро|этаж|подъезд|вход|Вход|офис|кабинет|в помещ|домофон|жилой|ЖК|Отдельный|Пройдите)", a)[0]
urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ev{c['n']}=1125e&text=" + urllib.parse.quote(f'{c["name"]}, {short(c["addr"])}')
        for c in K if c["n"] in TAKE]
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
