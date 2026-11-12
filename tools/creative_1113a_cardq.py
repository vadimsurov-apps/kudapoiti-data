"""Очередь карточек организаций (cc<N>-1113a) и адресов (ca<N>-1113a, координаты здания) по новым кандидатам."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
C = json.load(open(os.path.join(ROOT, "tools/creative_1113a_cands.json")))
SKIP = set(json.load(open(os.path.join(ROOT, "tools/creative_1113a_skip.json"))))
def addr_clean(a):
    parts = [p.strip() for p in a.split(",")]
    keep = [p for p in parts if not re.search(r"этаж|вход|офис|подъезд|кабинет|аудитория|Здание|помещении|метро|Между|Отдельный|Окружной|напр", p, re.I)]
    s = ", ".join(keep)
    return s if re.search(r"Москва|Балашиха|Химки|Подольск|Реутов|Королёв", s) else "Москва, " + s
SEL = [c for c in C if not c["dup"] and c["n"] not in SKIP]
if __name__ == "__main__":
    urls = []
    for c in SEL:
        a = addr_clean(c["addr"])
        urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?cc{c['n']}=1113a&text=" + urllib.parse.quote(f"{c['name']}, {a}"))
        urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ca{c['n']}=1113a&text=" + urllib.parse.quote(a))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(SEL), len(urls))
