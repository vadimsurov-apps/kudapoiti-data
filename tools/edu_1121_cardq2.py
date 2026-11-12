"""Карточки кандидатов второго круга «Особым детям» (ключи ey<n>-1121e) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = json.load(open(os.path.join(ROOT, "tools/edu_1121_keep2.json")))
TAKE = {5, 6, 20, 27, 117, 118, 21, 24, 32, 36, 42, 92, 103, 112, 113, 119, 120, 19, 111}
def short(a):
    return re.split(r", (Метро|этаж|подъезд|вход|Вход|офис|через|отдельны|э)", a)[0]
urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ey{c['n']}=1121e&text=" + urllib.parse.quote(f'{c["name"]}, {short(c["addr"])}')
        for c in K if c["n"] in TAKE]
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
