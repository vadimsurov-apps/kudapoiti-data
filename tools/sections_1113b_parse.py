"""Разбор выдачи Яндекс Карт (auto/pages, ключи sz*-1113b) → кандидаты; отсев дублей по places-all.json и data/parts/*.xlsx.
python3 tools/sections_1113b_parse.py > /tmp/cands.txt"""
import json, os, re, glob, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
TAG = sys.argv[1] if len(sys.argv) > 1 else "1113b"
idx = json.load(open(os.path.join(ROOT, "auto/pages/index.json")))
BAD = ("переехала", "Временно не работает", "Больше не работает", "Закрыто навсегда")


def norm(s):
    s = s.lower().replace("ё", "е")
    return re.sub(r"[^a-zа-я0-9]+", " ", s).strip()


def orgs(txt):
    txt = txt.split("\n### ")[0]
    L = [l.strip() for l in txt.split("\n")]
    res = []
    for i, l in enumerate(L):
        if l.endswith(" Фото") and i + 1 < len(L) and L[i + 1] == l[:-5]:
            res.append([i, l[:-5]])
    out = []
    for k, (i, nm) in enumerate(res):
        end = res[k + 1][0] if k + 1 < len(res) else len(L)
        blk = L[i + 2:end]
        flag = [b for b in blk if any(x in b for x in BAD)]
        adr = next((b for b in blk if re.search(r"\d", b) and ("Москва" in b or "ул" in b or "просп" in b or "ш.," in b or "обл" in b or "б-р" in b or "пер." in b or "мкр" in b)), "")
        cat = next((b for b in blk if "секция" in b or "клуб" in b.lower() or "школа" in b.lower() or "центр" in b.lower()), "")
        out.append((nm, adr, cat, "; ".join(flag)))
    return out


# существующие названия
names = []
for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]:
    names.append((norm(p.get("name", "")), p.get("address", "") or ""))
import openpyxl
for f in glob.glob(os.path.join(ROOT, "data/parts/*.xlsx")):
    ws = openpyxl.load_workbook(f, read_only=True).active
    rows = ws.iter_rows(values_only=True)
    h = list(next(rows))
    ni, ai = h.index("Название"), h.index("Адрес")
    for r in rows:
        if r[ni]:
            names.append((norm(str(r[ni])), str(r[ai] or "")))

seen = {}
for k, v in idx.items():
    if f"=" in v["url"] and f"={TAG}&" in v["url"] and "?sz" in v["url"]:
        fp = os.path.join(ROOT, "auto/pages", k + ".txt")
        if not os.path.exists(fp):
            continue
        for nm, adr, cat, flag in orgs(open(fp).read()):
            seen.setdefault((nm, adr), (cat, flag, k))
for (nm, adr), (cat, flag, k) in seen.items():
    n = norm(nm)
    w = [x for x in n.split() if len(x) > 3]
    hit = [a for (en, a) in names if n and (n in en or (w and all(x in en for x in w)))]
    street = norm(adr).split()[:3]
    st = [x for x in norm(adr.replace("Москва", "")).split() if len(x) > 4 and not x.isdigit()][:2]
    same = [a for a in hit if st and any(x in norm(a) for x in st)]
    dup = "ДУБЛЬ" if same else ("имя?" if hit else "")
    print(f"{dup}\t{nm}\t{adr}\t{cat}\t{flag}\t{(same or hit)[:2]}")
