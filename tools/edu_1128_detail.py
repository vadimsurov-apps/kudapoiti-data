"""Детали отобранных карточек (возраст групп, цены, доступность) — для ручного заполнения edu_1128_sel.py."""
import os, re, glob, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
AGE = re.compile(r"(\d\s*(-|–|до)\s*\d+\s*(лет|года|год|мес)|\bот \d+[,.]?\d*\s*(лет|года|год|мес|х)|с \d+[,.]?\d*\s*(лет|года|мес)|\d+\+|\d+\s*(класс)|дошкольн|школьник|малыш|ОВЗ|РАС|ЗПР|аутиз|адаптив|Доступность|Пандус|Туалет для|Лифт|Парковка для|инвалид)", re.I)
for n in sys.argv[1:]:
    f = glob.glob(os.path.join(ROOT, f"auto/pages/*-{"ey" if str(n).startswith("y") else "ev"}{str(n).lstrip("y")}-1128e-*.txt"))[0]
    secs = open(f).read().split("\n### ")
    txt = "\n".join([secs[0]] + [s for s in secs[1:] if s.startswith("https://yandex.ru/maps/org/")])
    L = [l.strip() for l in txt.splitlines() if l.strip()]
    out = []
    for i, l in enumerate(L):
        if AGE.search(l) and len(l) < 170 and not l.startswith(("Хорошее место", "Подборка", "Акция : Подготовка к школе для детей с РАС")) and "Хорошее место" not in l:
            nxt = L[i + 1] if i + 1 < len(L) and "₽" in L[i + 1] else ""
            out.append(l + (" = " + nxt if nxt else ""))
    out = list(dict.fromkeys(out))
    h = [L[i + 1] for i, l in enumerate(L) if l == "График" and i + 1 < len(L)][:1]
    print(f"== {n}: " + " ¦ ".join(x[:70] for x in out[:14]))
