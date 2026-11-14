"""Проверка (сеть с другим адресом — не дубль) дублей новых мест edu (14.11): название (без скобок) в том же городе — places-all.json и все data/parts/*.xlsx."""
import json, re, sys, glob, openpyxl
def norm(s): return re.sub(r"[^a-zа-я0-9]", "", re.sub(r"\(.*?\)", "", (s or "")).lower().replace("ё", "е"))
def town(a): a = (a or "").replace("Москва, ", ""); return a.split(",")[0] if not re.match(r"^(ул|просп|пр|бул|пер|наб|ш|пл|Зеленоград)", a) else "Москва"
pa = json.load(open("places-all.json")); PL = pa["places"] if isinstance(pa, dict) else pa
have = [(p["id"], p.get("name"), p.get("address"), "all") for p in PL]
for f in glob.glob("data/parts/*.xlsx"):
    ws = openpyxl.load_workbook(f, read_only=True)["Места"]; R = ws.iter_rows(values_only=True); h = list(next(R))
    have += [(r[0], r[h.index("Название")], r[h.index("Адрес")], f) for r in R if r[0]]
ids = set(sys.argv[1:])
mine = {i: (n, a) for i, n, a, f in have if i in ids and f.endswith("edu.xlsx")}
for i, (n, a) in mine.items():
    for j, n2, a2, f in have:
        if j == i: continue
        sa = lambda x: re.sub(r"(корп\.|к)\s*", "к", re.sub(r"[^а-яa-z0-9,]", "", (x or "").lower().replace("ё", "е")))
        if norm(n2) and len(norm(n)) > 3 and (norm(n2) == norm(n)) and town(a2) == town(a) and (sa(a).split(",")[-2:] == sa(a2).split(",")[-2:] or not a2):
            print("ДУБЛЬ?", i, n, a, "<->", j, n2, a2, f)
