"""Выжимка из карточек Яндекс Карт (cc<N>-1113h) и адресных страниц (ca<N>-1113h) → tools/creative_1113h_ext.json."""
import json, os, re, glob, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from creative_1113h_cardq import SEL
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
out = {}
for c in SEL:
    n = c["n"]; o = {"name": c["name"], "q": c["addr"], "theme": c["theme"], "area": c["area"]}
    fs = glob.glob(os.path.join(ROOT, f"auto/pages/*-cc{n}-1113hc-*.txt"))
    if fs:
        T = open(fs[0]).read()
        parts = T.split("\n### ")
        L = [l.strip() for l in parts[0].splitlines() if l.strip()]
        o["title"] = L[1] if len(L) > 1 and not L[1].isdigit() else (L[2] if len(L) > 2 else "")
        if o["title"].isdigit(): o["title"] = L[2]
        m = re.search(r"https://yandex\.ru/maps/org/([^/]+/\d+)", T); o["org"] = m.group(1) if m else None
        if "Адрес" in L:
            i = L.index("Адрес"); o["addr"] = L[i + 1]; o["addr2"] = L[i + 2] if L[i + 2] not in ("Показать входы", "Маршрут") else None
        ph = re.findall(r"(\+7 \(\d{3}\) \d{3}-\d{2}-\d{2})", parts[0]); o["phone"] = ph[0] if ph else None
        if "Контакты" in L:
            i = L.index("Контакты")
            site = [x for x in L[i + 1:i + 6] if re.match(r"^[\w.\-а-яё]+\.(ru|рф|com|net|org|su|pro|online|site|ws|me|art|studio|moscow|club|info|io|school)(/\S*)?$", x, re.I)]
            o["site"] = site[0] if site else None
        if "Как добраться" in L:
            i = L.index("Как добраться"); o["metro"] = L[i + 1]; o["mdist"] = L[i + 2]
        o["closed"] = bool(re.search(r"Больше не работает|Закрыто навсегда|Временно не работает", T))
        ages = sorted(set(re.findall(r"[^\n]{0,70}(?:\d+\s*(?:–|-|до)\s*\d+\s*лет|от\s*\d+(?:,\d)?\s*(?:лет|года|год)|с\s*\d+(?:,\d)?\s*(?:лет|года|-х|-ти)|\d+\+|для детей|детск|дошкол|школьник|подрост|взросл)[^\n]{0,70}", T, re.I)))
        o["ages"] = ages[:25]
        feats = []
        if "Особенности" in L:
            j = len(L) - 1 - L[::-1].index("Особенности")
            feats = L[j + 1:j + 14]
        o["feats"] = [x for x in feats if ":" in x]
        o["ru"] = L[2] if len(L) > 2 else ""
    fa = glob.glob(os.path.join(ROOT, f"auto/pages/*-ca{n}-1113hc-*.txt"))
    if fa:
        m = re.search(r"Координаты : ([\d.]+), ([\d.]+)", open(fa[0]).read())
        if m: o["ll"] = [float(m.group(1)), float(m.group(2))]
    out[str(n)] = o
json.dump(out, open(os.path.join(ROOT, "tools/creative_1113h_ext.json"), "w"), ensure_ascii=False, indent=0)
print(len(out), sum(1 for o in out.values() if o.get("ll")), sum(1 for o in out.values() if o.get("org")))
