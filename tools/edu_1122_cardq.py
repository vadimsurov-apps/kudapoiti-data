"""Карточки организаций отобранных кандидатов (ключи ev<n>-1122e) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = json.load(open(os.path.join(ROOT, "tools/edu_1122_keep.json")))
TAKE = {10,11,13,23,24,41,44,46,57,59,76,94,105,106,107,109,110,112,127,129,131,133,144,145,147,185,199,200,201,202,203,206,208,216,218,219,222,224,233,234,239,241,243,251,252,256,257,258,259,260,261,262,263,174,
        2,4,9,15,18,47,48,49,53,67,69,71,72,82,86,87,95,99,101,103,104,115,117,119,136,138,141,143,163,165,167,168,169,170,183,184,192,209,211,215,227,228,231}
def short(a):
    return re.split(r", (Метро|этаж|подъезд|вход|Вход|офис|кабинет|в помещ|домофон|жилой|ЖК)", a)[0]
urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ev{c['n']}=1122e&text=" + urllib.parse.quote(f'{c["name"]}, {short(c["addr"])}')
        for c in K if c["n"] in TAKE]
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
