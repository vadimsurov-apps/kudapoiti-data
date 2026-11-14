"""Убрать повторы выдачи и места, которые уже есть у нас (places-all.json + data/parts/*.xlsx): название + тот же дом/город."""
import json, os, re, glob
import openpyxl
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
C = json.load(open(os.path.join(ROOT, "tools/edu_1133_cands.json")))
pa = json.load(open(os.path.join(ROOT, "places-all.json")))
PL = pa["places"] if isinstance(pa, dict) else pa
def norm(s): return re.sub(r"[^a-zа-я0-9]", "", (s or "").lower().replace("ё", "е"))
have = [(norm(p.get("name")), p.get("address") or "", p["id"], p.get("cats") or p.get("categories")) for p in PL]
for f in glob.glob(os.path.join(ROOT, "data/parts/*.xlsx")):
    ws = openpyxl.load_workbook(f, read_only=True)["Места"]
    rows = ws.iter_rows(values_only=True); h = list(next(rows))
    iN, iA = h.index("Название"), h.index("Адрес")
    for r in rows:
        if r[0]: have.append((norm(r[iN]), r[iA] or "", r[0], None))
def street_house(a):
    a = a.replace("ё", "е")
    m = re.search(r"([А-Яа-я0-9\- ]+?(ул\.|ш\.|пр\.|просп\.|бул\.|пер\.|наб\.|пр-т|проезд)[^,]*|(ул\.|просп\.|пер\.)\s*[^,]+),\s*(\d+[^,]*)", a)
    return norm((m.group(1) or "") + (m.group(4) or "")) if m else norm(a)[:30]
seen, keep, dup = set(), [], []
for c in C:
    k = (norm(c["name"]), street_house(c["addr"]))
    if k in seen: continue
    seen.add(k)
    sh = street_house(c["addr"]); nn = norm(c["name"])
    hit = [h for h in have if (h[0] and (nn in h[0] or h[0] in nn) and len(nn) > 3 and (street_house(h[1]) == sh or nn == h[0] and len(nn) > 8)) or (street_house(h[1]) == sh and h[0] and nn[:6] in h[0])]
    if hit: dup.append((c["n"], c["name"], c["addr"], [(h[2], h[3]) for h in hit][:3])); continue
    keep.append(c)
json.dump(keep, open(os.path.join(ROOT, "tools/edu_1133_keep.json"), "w"), ensure_ascii=False, indent=0)
print("keep", len(keep))
for d in dup: print("DUP", d)
