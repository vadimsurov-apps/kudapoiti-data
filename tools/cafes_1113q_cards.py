"""Робот cafes 1113q: что сказано в карточках кандидатов (детская комната, рубрика, адрес, телефон, сайт, средний счёт, этаж) и координаты дома."""
import json, os, re, glob
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
from cafes_1113q_cardq import PICK, C
res = {}
for n in PICK:
    f = glob.glob(os.path.join(ROOT, f"auto/pages/*-kcn{n}-1113q-*.txt")); g = glob.glob(os.path.join(ROOT, f"auto/pages/*-kcg{n}-1113q-*.txt"))
    t = open(f[0]).read().split('{"config"')[0] if f else ""
    L = [l.strip() for l in t.splitlines()]
    d = {"name": L[2] if len(L) > 2 else "", "rubric": L[3] if len(L) > 3 else ""}
    for i, l in enumerate(L):
        if l.startswith("Детская комната ·") or l.startswith("С детьми ·") or l.startswith("Детское меню ·") or l.startswith("Аниматор"):
            d.setdefault("asp", []).append(l + " " + (L[i + 1] if i + 1 < len(L) else ""))
        if l == "Адрес" and "addr" not in d: d["addr"] = L[i + 1]; d["floor"] = L[i + 2] if L[i + 2].startswith("этаж") else None
        if "Показать телефон" in l and "phone" not in d: d["phone"] = l.replace(" Показать телефон", "")
        if l.startswith("Средний счёт"): d["check"] = l
        if re.search(r"(детск|игров|аниматор)", l, re.I) and ("Подборка" in L[i - 1] or "подборк" in l.lower() or "Особенности" in L[i-3:i]):
            d.setdefault("feat", []).append(l)
        if L[i - 1:i] and L[i-1].startswith("Подборка") is False and re.search(r"(детск\w* (комнат|уголк|игров)|аниматор)", l, re.I) and len(l) < 120 and i + 1 < len(L) and L[i + 1] == "Яндекс Карты": d.setdefault("feat", []).append(l)
    m = re.search(r"\n([a-z0-9.-]+\.(?:ru|com|рф|net|moscow|su|site|cafe|org))\n", t); d["site"] = m.group(1) if m else None
    if g:
        m = re.search(r"Координаты : ([\d.]+), ([\d.]+)", open(g[0]).read()); d["coord"] = [float(m.group(1)), float(m.group(2))] if m else None
    res[n] = d
json.dump(res, open(os.path.join(ROOT, "tools/cafes_1113q_cards.json"), "w"), ensure_ascii=False, indent=0)
for n, d in res.items():
    print(n, C[n]["name"], "|", d.get("name"), "|", d.get("addr"), d.get("floor"), "|", d.get("check"), "|", d.get("asp"), "|", d.get("feat"), "|", d.get("coord") is not None)
