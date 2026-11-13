"""Сводка карточек Яндекс Карт (cc<N>-1113g): только первая секция страницы (сама организация)."""
import json, os, re, glob, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
X = json.load(open(os.path.join(ROOT, "tools/creative_1113g_ext.json")))
def card(n):
    fs = glob.glob(os.path.join(ROOT, f"auto/pages/*-cc{n}-1113g-*.txt"))
    if not fs: return None
    T = open(fs[0]).read().split("\n### ")[0]
    return [l.strip() for l in T.splitlines() if l.strip()]
if __name__ == "__main__":
    for k, o in X.items():
        L = card(k)
        if not L: continue
        t = "\n".join(L)
        closed = bool(re.search(r"Больше не работает|Закрыто навсегда|Временно не работает", t))
        hrs = [l for l in L if re.match(r"(Открыто|Закрыто|Круглосуточно)", l)][:1]
        svc = []
        if "Витрина" in L or "Товары и услуги" in L:
            i = L.index("Витрина") if "Витрина" in L else L.index("Товары и услуги")
            j = next((x for x in range(i, len(L)) if L[x].startswith("Посмотреть все")), min(i + 30, len(L)))
            svc = L[i + 1:j]
        feats = [l for l in L if re.search(r"(лет|год|возраст|групп|дет|пробн)", l, re.I) and len(l) < 200]
        print(f"\n## {k} [{o['theme'][:6]}] {L[1] if len(L)>1 else ''} | {L[2] if len(L)>2 else ''} | {o.get('addr')} | {o.get('addr2')} | {o.get('phone')} | {o.get('site')} | {'CLOSED' if closed else ''} {hrs}")
        print("   svc:", " / ".join(svc)[:500])
        print("   ages:", " / ".join(dict.fromkeys(feats))[:500])
