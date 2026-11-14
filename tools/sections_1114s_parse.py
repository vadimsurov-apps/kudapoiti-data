"""Разбор выдач Яндекс Карт sz*-1114s → tools/sections_1114s_cands.json (отсев дублей: places-all + data/parts)."""
import json, os, re, glob
import openpyxl
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
from sections_1114s_q import AREAS, Q
def norm(s): return re.sub(r"[^a-zа-я0-9]+", " ", (s or "").lower().replace("ё", "е")).strip()
pa = json.load(open(os.path.join(ROOT, "places-all.json")))["places"]
names = [(norm(p.get("name")), p.get("id"), p.get("address") or "") for p in pa]
for f in glob.glob(os.path.join(ROOT, "data/parts/*.xlsx")) + [os.path.join(ROOT, "data/kuda-poiti-mesta.xlsx")]:
    for r in openpyxl.load_workbook(f, read_only=True)["Места"].iter_rows(min_row=2, values_only=True):
        if r[0]: names.append((norm(r[1]), r[0], r[4] or ""))
STOP = {"школа", "клуб", "спортивный", "спортивная", "детская", "детский", "центр", "для", "детей", "секция", "и",
        "единоборств", "футбольная", "академия", "федерация", "сдюшор", "спортшкола", "фк", "мгфсо", "москомспорта", "гбу", "до", "дюсш", "сш"}
def dup(name, addr):
    n = norm(name); w = set(n.split()) - STOP
    for nn, pid, a in names:
        if not nn: continue
        if nn == n or (w and w <= set(nn.split())):
            st = set(norm(addr).split()) & set(norm(a).split()) - {"москва", "ул", "улица", "проспект", "просп"}
            if st or nn == n: return pid
    return None
out, seen = [], set()
for i, a in enumerate(AREAS):
    for j, q in enumerate(Q):
        fs = glob.glob(os.path.join(ROOT, f"auto/pages/*-sz{i}x{j}-1114s-*.txt"))
        if not fs: continue
        L = [l.strip() for l in open(fs[0]).read().split("\n### ")[0].splitlines()]
        for k, l in enumerate(L):
            if re.search(r" Фото( \d+)?$", l):
                name = re.sub(r" Фото( \d+)?$", "", l)
                for m in range(k + 1, min(k + 14, len(L))):
                    if re.search(r" Фото( \d+)?$", L[m]): break
                    if "," in L[m] and re.search(r"\d", L[m]) and not L[m].startswith(("Рейтинг", "Закрыто", "Открыто", "В подборке")):
                        key = (norm(name), norm(L[m]))
                        if key in seen: break
                        seen.add(key)
                        out.append({"n": len(out), "area": a, "q": j, "name": name, "rubric": L[m - 1], "addr": L[m], "dup": dup(name, L[m])})
                        break
json.dump(out, open(os.path.join(ROOT, "tools/sections_1114s_cands.json"), "w"), ensure_ascii=False, indent=0)
new = [c for c in out if not c["dup"]]
print(len(out), "new", len(new))
for c in new: print(c["n"], c["area"][:10], "|", c["name"], "|", c["rubric"], "|", c["addr"])
