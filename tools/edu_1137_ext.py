"""Робот edu 14.11 (27-й запуск): выжимка карточек Яндекс Карт (ev<n>-1137e — ключ «37:n», кандидаты tools/edu_1137_keep1.json;
ev<n>-1137h — «37h:n», tools/edu_1137_keep.json): название, адрес, телефон, сайт, часы, особенности (доступность), услуги с ценами,
строки с возрастом, акции → tools/edu_1137_ext.json; печать для отбора."""
import json, os, re, glob, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K1 = {c["n"]: c for c in json.load(open(os.path.join(ROOT, "tools/edu_1137_keep1.json")))}
K2 = {c["n"]: c for c in json.load(open(os.path.join(ROOT, "tools/edu_1137_keep.json")))}
OUT = {}
for tag, w, K in (("1137e", "37", K1), ("1137h", "37h", K2)):
    for f in glob.glob(os.path.join(ROOT, f"auto/pages/*-ev*-{tag}-*.txt")):
        n = int(re.search(rf"-ev(\d+)-{tag}", f).group(1))
        t = open(f).read(); parts = t.split("\n### ")
        main = "\n".join([parts[0]] + [s for s in parts[1:] if s.startswith("https://yandex.ru/maps/org/")])
        L = [l.strip() for l in main.splitlines() if l.strip()]
        d = {"cand": K[n]["name"], "caddr": K[n]["addr"], "q": K[n]["q"], "head": L[1:5], "pt": K[n].get("pt")}
        org = re.findall(r"https://yandex\.ru/maps/org/[^/\s]+/\d+/", t); d["org"] = org[0] if org else None
        d["addr"] = None
        if "Адрес" in L:
            i = L.index("Адрес"); a = []
            for l in L[i + 1:i + 5]:
                if l in ("Показать входы", "Маршрут", "Контакты"): break
                a.append(l)
            d["addr"] = a
        ph = [l for l in L if re.search(r"\+7 \(\d{3}\)", l)]
        d["phone"] = re.sub(r"\s*Показать телефон", "", ph[0]) if ph else None
        d["site"] = None
        if ph:
            j = L.index(ph[0])
            d["site"] = next((l for l in L[j + 1:j + 4] if re.match(r"^[\w\-\.]+\.(ru|com|рф|org|net|online|pro|moscow|su|info|school|club|kids|io|academy|space|site)(/\S*)?$", l)), None)
        d["hours"] = L[L.index("Время работы") + 1:L.index("Время работы") + 3] if "Время работы" in L else None
        d["closed"] = any(x in L for x in ("Больше не работает", "Временно не работает"))
        feats = []
        for i, l in enumerate(L):
            if l == "Особенности" and i > 15:
                for x in L[i + 1:]:
                    if x in ("Подробнее об организации", "Панорама", "Похожие места"): break
                    feats.append(x)
                if feats: break
        d["feats"] = feats
        serv = []
        for i, l in enumerate(L):
            if l in ("Товары и услуги", "Витрина", "Цены") and i > 5:
                for x in L[i + 1:i + 70]:
                    if x.startswith("Посмотреть все") or x in ("Панорама", "Адрес", "Новости", "Особенности"): break
                    if re.match(r"^(от )?[\d\s]+₽", x) and serv: serv[-1] += " = " + x
                    elif x != "Давно не обновлялось" and len(x) < 160: serv.append(x)
                break
        d["serv"] = serv[:18]
        d["act"] = [l for l in L if l.startswith("Акция :")][:2]
        d["ages"] = [l for l in L if re.search(r"(\d\s*(лет|года|год|мес)|\d\+|от \d|с \d|малыш|возраст)", l, re.I) and len(l) < 200][:25]
        OUT[f"{w}:{n}"] = d
json.dump(OUT, open(os.path.join(ROOT, "tools/edu_1137_ext.json"), "w"), ensure_ascii=False, indent=1)
if __name__ == "__main__":
    SKIP = re.compile(r"^(Оплата картой|Wi-Fi|Подарочный сертификат|Можно с собакой|Посещение с животными|Способ оплаты|Кнопка вызова|Онлайн-запись|Есть сайт)", re.I)
    for k, o in sorted(OUT.items(), key=lambda x: (x[0].split(":")[0], int(x[0].split(":")[1]))):
        if len(sys.argv) > 1 and k not in sys.argv[1:]: continue
        print(f"== {k} {o['cand']} {'ЗАКРЫТО' if o['closed'] else ''} | {o['head'][:2]} | {o['addr']} | {o['phone']} | {o['site']} | {o['hours']}")
        print("  F:", " ¦ ".join(x[:110] for x in o["feats"] if not SKIP.match(x)))
        print("  S:", " ¦ ".join(x[:90] for x in o["serv"]))
        print("  AGE:", " ¦ ".join(x[:110] for x in o["ages"][:14]))
        if o["act"]: print("  A:", " ¦ ".join(o["act"]))
