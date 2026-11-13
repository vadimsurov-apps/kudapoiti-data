"""Доп. проверка дублей кандидатов 1113v: любое слово названия (≥4 букв) + совпадение улицы и номера дома в places-all и data/parts."""
import json, os, re, glob, openpyxl
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
def norm(s): return re.sub(r"[^a-zа-я0-9]+", " ", (s or "").lower().replace("ё", "е")).strip()
rows = [(p.get("id"), p.get("name") or "", p.get("address") or "") for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]]
for f in glob.glob(os.path.join(ROOT, "data/parts/*.xlsx")) + [os.path.join(ROOT, "data/kuda-poiti-mesta.xlsx")]:
    for r in openpyxl.load_workbook(f, read_only=True)["Места"].iter_rows(min_row=2, values_only=True):
        if r[0]: rows.append((r[0], r[1] or "", r[4] or ""))
STOP = {"москва","ул","улица","просп","проспект","корп","стр","этаж","ш","бул","пр"}
def key(a):
    n = norm(a).split(); nums = [x for x in n if re.match(r"\d", x)]
    words = [x for x in n if len(x) > 3 and x not in STOP and not re.match(r"\d", x)]
    return set(words), (nums[0] if nums else None)
C = json.load(open(os.path.join(ROOT, "tools/sections_1113v_cands.json")))
for c in C:
    if c["dup"]: continue
    w, num = key(c["addr"])
    nw = {x for x in norm(c["name"]).split() if len(x) >= 4}
    hits = []
    for pid, nm, a in rows:
        w2, n2 = key(a)
        if num and n2 == num and w & w2: hits.append(f"{pid}:{nm}[адрес]")
        elif nw and nw & set(norm(nm).split()) - {"школа","клуб","центр","спорт","детская","секция","академия"} and w & w2: hits.append(f"{pid}:{nm}[имя]")
    if hits: print(c["n"], c["name"], "|", c["addr"], "=>", hits[:4])
