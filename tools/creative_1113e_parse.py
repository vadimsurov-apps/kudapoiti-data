"""Разбор выдач Яндекс Карт (cv<N>-1113e) → tools/creative_1113e_cands.json, с отсевом дублей (places-all + data/parts)."""
import json, os, re, glob
import openpyxl
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q = json.load(open(os.path.join(ROOT, "tools/creative_1113e_queries.json")))["q"]
def norm(s): return re.sub(r"[^a-zа-я0-9]+", " ", (s or "").lower().replace("ё", "е")).strip()
pa = json.load(open(os.path.join(ROOT, "places-all.json")))
pa = pa["places"] if isinstance(pa, dict) else pa
names = [(norm(p.get("name")), p.get("id"), p.get("address") or "") for p in pa]
for f in glob.glob(os.path.join(ROOT, "data/parts/*.xlsx")) + [os.path.join(ROOT, "data/kuda-poiti-mesta.xlsx")]:
    ws = openpyxl.load_workbook(f, read_only=True)["Места"]
    for r in ws.iter_rows(min_row=2, values_only=True):
        if r[0]: names.append((norm(r[1]), r[0], r[4] or ""))
STOP = {"школа", "студия", "танцев", "танца", "детская", "детский", "центр", "для", "детей", "музыкальная", "театральная",
        "художественная", "искусств", "дшиис", "дши", "дмш", "мастерская", "гончарная", "вокала", "клуб", "и", "the", "school", "studio", "dance"}
def dup(name, addr):
    n = norm(name); w = set(n.split()) - STOP
    hn = re.findall(r"\d+", addr)
    for nn, pid, a in names:
        if not nn: continue
        if nn == n or (w and w <= set(nn.split())):
            # same name; check street overlap
            st = set(norm(addr).split()) & set(norm(a).split()) - {"москва", "ул", "улица"}
            if st or nn == n: return pid
    return None
out, seen = [], set()
for n, q in enumerate(Q):
    fs = glob.glob(os.path.join(ROOT, f"auto/pages/*-cv{n}-1113e-*.txt"))
    if not fs: continue
    L = [l.strip() for l in open(fs[0]).read().split("\n### ")[0].splitlines()]
    for i, l in enumerate(L):
        if re.search(r" Фото( \d+)?$", l):
            name = re.sub(r" Фото( \d+)?$", "", l)
            for j in range(i + 1, min(i + 14, len(L))):
                if re.search(r" Фото( \d+)?$", L[j]): break
                if "," in L[j] and re.search(r"\d", L[j]) and not L[j].startswith(("Рейтинг", "Закрыто", "Открыто", "В подборке")):
                    key = (norm(name), norm(L[j]))
                    if key in seen: break
                    seen.add(key)
                    out.append({"n": len(out), "qn": n, "area": q["area"], "theme": q["theme"], "name": name,
                                "rubric": L[j - 1], "addr": L[j], "dup": dup(name, L[j])})
                    break
json.dump(out, open(os.path.join(ROOT, "tools/creative_1113e_cands.json"), "w"), ensure_ascii=False, indent=0)
new = [c for c in out if not c["dup"]]
print(len(out), "new", len(new))
for c in new: print(c["n"], c["theme"][:8], "|", c["name"], "|", c["rubric"], "|", c["addr"])
