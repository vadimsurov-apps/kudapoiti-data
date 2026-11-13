"""Разбор выдач Яндекс Карт (pz<N>-1113k) → tools/pools_1113k_cands.json, с отсевом дублей (places-all + data/parts)."""
import json, os, re, glob
import openpyxl
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
def norm(s): return re.sub(r"[^a-zа-я0-9]+", " ", (s or "").lower().replace("ё", "е")).strip()
pa = json.load(open(os.path.join(ROOT, "places-all.json")))
pa = pa["places"] if isinstance(pa, dict) else pa
names = [(norm(p.get("name")), p.get("id"), p.get("address") or "") for p in pa]
for f in glob.glob(os.path.join(ROOT, "data/parts/*.xlsx")) + [os.path.join(ROOT, "data/kuda-poiti-mesta.xlsx")]:
    ws = openpyxl.load_workbook(f, read_only=True)["Места"]
    for r in ws.iter_rows(min_row=2, values_only=True):
        if r[0]: names.append((norm(r[1]), r[0], r[4] or ""))
STOP = {"школа", "плавания", "детский", "бассейн", "центр", "для", "детей", "клуб", "и", "the", "school", "swim", "фитнес",
        "спортивный", "комплекс", "ск", "фок", "аквацентр", "акваклуб", "студия", "детского", "раннего", "семейный"}
def hn(a):
    a = norm(a); m = re.findall(r"\b(\d+[а-я]?)\b", a); return set(m)
def street(a):
    return set(norm(a).split()) - {"москва", "ул", "улица", "просп", "проспект", "корп", "стр", "ш", "шоссе", "бул", "б", "р", "пр", "д",
                                   "этаж", "наб", "пер", "мкр", "1", "2", "3"} - hn(a)
def dup(name, addr):
    n = norm(name); w = set(n.split()) - STOP
    res = []
    for nn, pid, a in names:
        sa = street(addr) & street(a); ha = hn(addr) & hn(a)
        if sa and ha and ("бассейн" in nn or "плав" in nn or "аква" in nn or "swim" in nn or (w and w & set(nn.split()))):
            res.append(pid)          # тот же адрес и водное место/то же имя
        elif w and w <= set(nn.split()) and sa:
            res.append(pid)
    return res[:3]
out, seen = [], set()
for fs in sorted(glob.glob(os.path.join(ROOT, "auto/pages/*-pz*-1113k-*.txt"))):
    L = [l.strip() for l in open(fs).read().split("\n### ")[0].splitlines()]
    for i, l in enumerate(L):
        if re.search(r" Фото( \d+)?$", l) or (len(l.split()) % 2 == 0 and l.split()[:len(l.split())//2] == l.split()[len(l.split())//2:] and l):
            name = re.sub(r" Фото( \d+)?$", "", l)
            ws_ = name.split()
            if len(ws_) % 2 == 0 and ws_[:len(ws_)//2] == ws_[len(ws_)//2:]: name = " ".join(ws_[:len(ws_)//2])
            for j in range(i + 1, min(i + 14, len(L))):
                if re.search(r" Фото( \d+)?$", L[j]): break
                if "," in L[j] and re.search(r"\d", L[j]) and not L[j].startswith(("Рейтинг", "Закрыто", "Открыто", "В подборке", "Акция", "Награды")):
                    key = (norm(name), norm(L[j]))
                    if key in seen: break
                    seen.add(key)
                    out.append({"n": len(out), "q": L[1] if len(L) > 1 else "", "name": name, "rubric": L[j - 1], "addr": L[j],
                                "dup": dup(name, L[j])})
                    break
json.dump(out, open(os.path.join(ROOT, "tools/pools_1113k_cands.json"), "w"), ensure_ascii=False, indent=0)
new = [c for c in out if not c["dup"]]
print(len(out), "new", len(new))
for c in out: print(c["n"], "|", c["name"], "|", c["rubric"][:45], "|", c["addr"], "|", ",".join(c["dup"]))
