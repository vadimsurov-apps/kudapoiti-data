"""Сводка «Товары и услуги» из карточек Яндекс Карт партии 1114w. python3 tools/sections_1114w_svc.py [n…]"""
import glob, os, re, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
for n in [int(x) for x in sys.argv[1:]]:
    fs = glob.glob(os.path.join(ROOT, f"auto/pages/*-sc{n}-s1114w-*.txt"))
    if not fs: continue
    L = [l.strip() for l in open(fs[0]).read().split("\n### ")[0].splitlines()[1:]]
    s = " / ".join(L)
    m = re.search(r"Похожие места / Товары и услуги / (.*?) / (Посмотреть все товары|Панорама|Адрес)", s)
    w = re.search(r"Контакты / (.*?) / Время работы", s)
    print(n, "|", " / ".join(L[:2])[:90], "| SVC:", (m.group(1)[:700] if m else "-"), "| CT:", (w.group(1)[:120] if w else "-"))
