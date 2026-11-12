"""Карточки организаций отобранных кандидатов (ключи ev<n>-1121e) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = json.load(open(os.path.join(ROOT, "tools/edu_1121_keep.json")))
TAKE = {20,26,87,90,94,74,154,168,180,181,215,217,247,250,249,252,262,264,58,129,134,93,255,
        8,13,15,27,31,34,36,40,41,42,43,45,47,53,54,55,57,60,61,62,63,64,65,72,78,80,84,92,100,99,111,112,113,114,125,126,136,137,
        141,142,152,155,174,177,191,193,194,195,203,204,216,225,234,238,240,241,22,24,28,29,51,88,101,119,171,178,189,198,209,224,233}
def short(a):
    return re.split(r", (Метро|этаж|подъезд|вход|Вход|офис|кабинет|в помещ|домофон|жилой|ЖК)", a)[0]
urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ev{c['n']}=1121e&text=" + urllib.parse.quote(f'{c["name"]}, {short(c["addr"])}')
        for c in K if c["n"] in TAKE]
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
