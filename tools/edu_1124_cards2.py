"""Выжимка карточек организаций (ev<n>-1123e): название, адрес, телефон, сайт, строки с возрастом и ценами → tools/edu_1124_cards2.json"""
import json, os, re, glob
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = {c["n"]: c for c in json.load(open(os.path.join(ROOT, "tools/edu_1124_keep2.json")))}
out = {}
for f in glob.glob(os.path.join(ROOT, "auto/pages/*-ex*-1124e-*.txt")):
    n = int(re.search(r"-ex(\d+)-1124e", f).group(1))
    t = open(f).read()
    parts = t.split("\n### ")
    main = "\n".join([parts[0]] + [s for s in parts[1:] if s.startswith("https://yandex.ru/maps/org/")])
    L = [l.strip() for l in main.splitlines() if l.strip()]
    d = {"n": n, "cand": K[n]["name"], "caddr": K[n]["addr"], "page": os.path.basename(f)[:-4], "q": K[n]["q"]}
    d["head"] = L[1:4]
    org = re.findall(r"https://yandex\.ru/maps/org/[^/\s]+/\d+/", t)
    d["org"] = org[0] if org else None
    if "Адрес" in L:
        i = L.index("Адрес"); a = []
        for l in L[i + 1:i + 5]:
            if l in ("Показать входы", "Маршрут", "Контакты"): break
            a.append(l)
        d["addr"] = a
    ph = [l for l in L if re.search(r"\+7 \(\d{3}\)", l)]
    d["phone"] = re.sub(r"\s*Показать телефон", "", ph[0]) if ph else None
    if ph:
        j = L.index(ph[0])
        d["site"] = next((l for l in L[j + 1:j + 4] if re.match(r"^[\w\-\.]+\.(ru|com|рф|org|net|online|pro|moscow|su|info|school|club|kids|io)(/\S*)?$", l)), None)
    if "Время работы" in L:
        i = L.index("Время работы"); d["hours"] = L[i + 1:i + 3]
    ag = [l for l in L if re.search(r"(\d\s*(лет|года|год|мес)|\d\+|от \d|с \d|₽|малыш)", l) and len(l) < 160]
    d["lines"] = ag[:40]
    rest = "\n".join(parts[1:])
    d["more"] = [l.strip() for l in rest.splitlines() if re.search(r"(\d\s*(лет|года|мес)|\d\+|₽)", l) and len(l.strip()) < 160][:25]
    out[n] = d
json.dump(out, open(os.path.join(ROOT, "tools/edu_1124_cards2.json"), "w"), ensure_ascii=False, indent=1)
print(len(out))
