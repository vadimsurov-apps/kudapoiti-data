"""Карточки отобранных кандидатов второго захода (ключи ex<n>-1124e) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = json.load(open(os.path.join(ROOT, "tools/edu_1124_keep2.json")))
TAKE = {2, 19, 20, 26, 28, 35, 38, 72, 57, 10, 65, 12, 24, 86, 85}
def short(a):
    return re.split(r", (Метро|этаж|подъезд|вход|Вход|офис|кабинет|в помещ|домофон|жилой|ЖК)", a)[0]
urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ex{c['n']}=1124e&text=" + urllib.parse.quote(f'{c["name"]}, {short(c["addr"])}')
        for c in K if c["n"] in TAKE]
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
