"""Выжимка карточек Яндекс Карт отделений ГППЦ (ev300+-1130e) → дописывает tools/edu_1130_ext.json (ключи "300"…)."""
import json, os, re, glob, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from edu_1130_gppc import G, KEY
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
P = os.path.join(ROOT, "tools/edu_1130_ext.json")
OUT = json.load(open(P))
for pid, n in KEY.items():
    f = glob.glob(os.path.join(ROOT, f"auto/pages/*-ev{n}-1130e-*.txt"))[0]
    t = open(f).read(); parts = t.split("\n### ")
    main = "\n".join([parts[0]] + [s for s in parts[1:] if s.startswith("https://yandex.ru/maps/org/")])
    L = [l.strip() for l in main.splitlines() if l.strip()]
    d = {"name": L[1] if len(L) > 1 else None, "head": L[1:4], "q": "Городской психолого-педагогический центр, " + G[pid][1]}
    org = re.findall(r"https://yandex\.ru/maps/org/[^/\s]+/\d+/", t); d["org"] = org[0] if org else None
    a = []
    if "Адрес" in L:
        i = L.index("Адрес")
        for l in L[i + 1:i + 5]:
            if l in ("Показать входы", "Маршрут", "Контакты"): break
            a.append(l)
    d["addr"] = a or None
    ph = [l for l in L if re.search(r"\+7 \(\d{3}\)", l)]
    d["phone"] = re.sub(r"\s*Показать телефон", "", ph[0]) if ph else None
    d["site"] = "gppc.ru" if any("gppc.ru" in l for l in L) else None
    feats = []
    for i, l in enumerate(L):
        if l == "Особенности" and i > 40:
            for x in L[i + 1:]:
                if x in ("Подробнее об организации", "Панорама", "Похожие места"): break
                feats.append(x)
            break
    d["feats"] = feats; d["serv"] = []; d["act"] = []
    OUT[str(n)] = d
    print(pid, n, "|", d["name"], "|", a, "|", d["phone"], "|", d["org"], "|", " ¦ ".join(x for x in feats if not x.startswith(("Оплата", "Способ")))[:300])
json.dump(OUT, open(P, "w"), ensure_ascii=False, indent=1)
