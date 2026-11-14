"""Сводка карточек Яндекс Карт партии 1114t (auto/pages, ключи sc<n>-s1114t): адрес, этаж, телефон, сайт, услуги, особенности, строки с возрастом.
python3 tools/sections_1114t_ext.py [n…]"""
import json, os, re, glob, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
C = {c["n"]: c for c in json.load(open(os.path.join(ROOT, "tools/sections_1114t_cands.json")))}
def card(n):
    fs = glob.glob(os.path.join(ROOT, f"auto/pages/*-sc{n}-s1114t-*.txt"))
    if not fs: return None
    t = open(fs[0]).read()
    L = [l.strip() for l in t.split("\n### ")[0].splitlines()[1:]]
    return t, L
if __name__ == "__main__":
    ns = [int(x) for x in sys.argv[1:]] or sorted(C)
    for n in ns:
        r = card(n)
        if not r: continue
        t, L = r
        print("=" * 8, n, C[n]["name"], "|", C[n]["addr"])
        print("  card:", " / ".join(L[:2]))
        if "Адрес" in L:
            i = L.index("Адрес"); print("  addr:", " / ".join(L[i + 1:i + 4]))
        ph = re.findall(r"\+7 \(\d{3}\) [\d-]+", t); print("  tel:", ph[:2])
        st = [l for l in L if re.match(r"^[a-z0-9.-]+\.(ru|com|рф|su|net|org|club|pro|moscow|online|info)(/\S*)?$", l)]; print("  site:", st[:2])
        if "Витрина" in L:
            i = L.index("Витрина"); j = L.index("Посмотреть все товары и услуги") if "Посмотреть все товары и услуги" in L else i + 16
            print("  svc:", " | ".join(L[i + 1:j])[:500])
        age = [l for l in L if re.search(r"(\d+\s*(лет|года|год)|возраст|дет)", l, re.I) and len(l) < 200]
        print("  age:", " | ".join(age)[:600])
        feats = [l for l in L if " : " in l]; print("  feat:", " | ".join(feats)[:400])
        hrs = [l for l in L if re.match(r"^(Ежедневно|Пн|Вт|Будни|Открыто до|Закрыто до|Круглосуточно)", l)]; print("  hrs:", hrs[:3])
