"""Точная проверка дублей кандидатов 1114zf/1114zg: слово названия (≥4 букв, не общее) есть в названии места базы
И совпадает улица → дубль. Печатает только новых. python3 tools/sections_1114zg_new.py zf|zg"""
import json, os, re, glob, sys, openpyxl
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
def norm(s): return re.sub(r"[^a-zа-я0-9]+", " ", (s or "").lower().replace("ё", "е")).strip()
rows = [(p["id"], p.get("name") or "", p.get("address") or "") for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]]
for f in glob.glob(os.path.join(ROOT, "data/parts/*.xlsx")):
    for r in openpyxl.load_workbook(f, read_only=True)["Места"].iter_rows(min_row=2, values_only=True):
        if r[0]: rows.append((r[0], r[1] or "", r[4] or ""))
GEN = set("школа клуб центр спорт спортивный спортивная детская детский секция академия федерация единоборств москва для детей гимнастики художественной гимнастика шахматная шахмат шахматный каратэ карате бокса бокс самбо дзюдо футбольная футбол баскетбола спортклуб клубе студия имени москомспорта мгфсо сшор".split())
STR = set("москва ул улица просп проспект корп стр этаж ш шоссе бул пер пр наб вл".split())
def streets(a): return {x for x in norm(a).split() if len(x) > 3 and x not in STR and not x[0].isdigit()}
C = json.load(open(os.path.join(ROOT, f"tools/sections_1114{sys.argv[1]}_cands.json")))
for c in C:
    nw = {x for x in norm(c["name"]).split() if len(x) >= 4} - GEN
    st = streets(c["addr"])
    hit = [f"{pid}:{nm}" for pid, nm, a in rows if (nw and nw & set(norm(nm).split())) and (st & streets(a) or not nw - set(norm(nm).split()))]
    if not hit: print(c["n"], c["area"][:10], "|", c["name"], "|", c["rubric"][:30], "|", c["addr"][:90])
