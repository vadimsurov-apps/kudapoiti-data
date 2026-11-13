"""Робот cafes 1114a: разбор выдач Яндекс Карт (kcz<N>-1114a) → tools/cafes_1114a_cands.json (с отсевом дублей)."""
import json, os, re, glob
import openpyxl
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q = json.load(open(os.path.join(ROOT, "tools/cafes_1114a_queries.json")))["q"]
def norm(s): return re.sub(r"[^a-zа-я0-9]+", " ", (s or "").lower().replace("ё", "е")).strip()
pa = json.load(open(os.path.join(ROOT, "places-all.json"))); pa = pa["places"] if isinstance(pa, dict) else pa
names = [(norm(p.get("name")), p.get("id"), p.get("address") or "") for p in pa]
for f in glob.glob(os.path.join(ROOT, "data/parts/*.xlsx")) + [os.path.join(ROOT, "data/kuda-poiti-mesta.xlsx")]:
    ws = openpyxl.load_workbook(f, read_only=True)["Места"]
    for r in ws.iter_rows(min_row=2, values_only=True):
        if r[0]: names.append((norm(r[1]), r[0], r[4] or ""))
closed = norm(open(os.path.join(ROOT, "auto/closed.txt")).read())
STOP = {"кафе", "ресторан", "и", "семейное", "семейный", "the", "бар", "пиццерия", "кофейня"}
def house(a):
    a = norm(a); m = re.findall(r"([а-яa-z]{4,})\D{0,25}?(\d+[а-яa-z]?)", a)
    return {f"{s} {n}" for s, n in m if s not in ("москва", "этаж", "корп")}
def samehouse(addr):
    h = house(addr)
    return [pid for nn, pid, a in names if pid and str(pid).startswith("cafe") and h & house(a)][:3]
def dup(name, addr):
    n = norm(name); w = set(n.split()) - STOP
    for nn, pid, a in names:
        if not nn: continue
        nb = re.sub(r"\s*\d.*$", "", nn)
        if nn.startswith(n) or (w and w <= set(nn.split())):
            st = set(norm(addr).split()) & set(norm(a).split()) - {"москва", "ул", "улица", "просп", "этаж", "1", "2"}
            if st: return pid
    return None
out, seen = [], set()
for n, q in enumerate(Q):
    fs = glob.glob(os.path.join(ROOT, f"auto/pages/*-kcz{n}-1114a-*.txt"))
    if not fs: continue
    L = [l.strip() for l in open(fs[0]).read().split('{"config"')[0].splitlines()]
    for i, l in enumerate(L):
        if i + 1 < len(L) and L[i + 1].startswith("Рейтинг") or (i + 1 < len(L) and L[i+1] == "Нет отзывов"):
            h = l.split(" "); k = len(h) // 2
            name = " ".join(h[:k]) if len(h) % 2 == 0 and h[:k] == h[k:] else l
            for j in range(i + 2, min(i + 14, len(L))):
                if L[j].startswith(("Открыто", "Закрыто", "Круглосуточно")) and j + 2 < len(L):
                    rub, addr = L[j + 1], L[j + 2]
                    chk = L[j + 3] if j + 3 < len(L) else ""
                    key = (norm(name), norm(addr))
                    if key not in seen:
                        seen.add(key)
                        out.append({"n": len(out), "qn": n, "area": q["area"], "name": name, "rubric": rub, "addr": addr,
                                    "chk": chk, "dup": dup(name, addr), "same": samehouse(addr), "closed": bool(norm(name) and norm(name) + " " in closed)})
                    break
json.dump(out, open(os.path.join(ROOT, "tools/cafes_1114a_cands.json"), "w"), ensure_ascii=False, indent=0)
new = [c for c in out if not c["dup"]]
print(len(out), "new", len(new))
for c in new: print(c["n"], c["area"][:10], "|", c["name"], "|", c["rubric"], "|", c["addr"], "|", c["chk"], c["same"], "|C" if c["closed"] else "")
