"""Карточки организаций второго захода («Особым детям» + специалисты, ключи ex<n>-1123e) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = json.load(open(os.path.join(ROOT, "tools/edu_1123_keep2.json")))
TAKE = {1179, 1196, 1042, 1069, 1212, 1218, 1220, 1045, 1221, 1222, 1015, 1094, 1123, 1124, 1054, 1175, 1164, 1122, 1048,
        1113, 1143, 1099, 1095, 1114, 1165, 1146, 1147}
def short(a):
    return re.split(r", (Метро|этаж|подъезд|вход|Вход|офис|кабинет|в помещ|домофон|жилой|ЖК)", a)[0]
urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ex{c['n']}=1123e&text=" + urllib.parse.quote(f'{c["name"]}, {short(c["addr"])}')
        for c in K if c["n"] in TAKE]
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
