"""Робот rare 13.11 (1113c): разбор выдачи Яндекс Карт (auto/pages, rr13e*/rr13f*) → кандидаты без дублей.
python3 tools/rare_1113c_parse.py rr13e"""
import glob, json, os, re, sys, urllib.parse as u
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
key = sys.argv[1]
P = json.load(open(os.path.join(ROOT, "places-all.json")))["places"]
def norm(s): return re.sub(r"[^a-zа-я0-9]", "", (s or "").lower().replace("ё", "е"))
names = [(norm(p["name"]), p["id"]) for p in P]
seen = {}
for f in sorted(glob.glob(os.path.join(ROOT, "auto", "pages", f"*{key}*.txt"))):
    txt = open(f).read()
    first = txt.split("\n### ")[0]
    lines = first.split("\n")
    q = lines[1]
    for i, l in enumerate(lines):
        if l.endswith(" Фото") and i + 1 < len(lines) and lines[i + 1] == l[:-5]:
            name = lines[i + 1]
            blk = lines[i + 2:i + 16]
            st = next((b for b in blk if "не работает" in b), "")
            cat = addr = ""
            for j, b in enumerate(blk):
                if b.endswith(" Фото"): blk = blk[:j]; break
            for j, b in enumerate(blk):
                if re.search(r"(ул\.|просп|ш\.|пр\.|бул\.|наб\.|пер\.|Москва|\d+[А-Яа-я]?,|д\. |посёлок|деревня|парк|сквер)", b) and not b.startswith(("Рейтинг", "Акция", "В подборке", "Награды")) and j > 0:
                    addr = b; cat = blk[j - 1]; break
            k = (name, addr)
            if k in seen: seen[k]["q"].append(q); continue
            n = norm(name)
            dup = [pid for nn, pid in names if n and (n in nn or nn in n) and len(n) > 4]
            seen[k] = {"name": name, "cat": cat, "addr": addr, "st": st, "dup": dup[:3], "q": [q]}
for v in seen.values():
    flag = "DUP" if v["dup"] else ("CLOSED" if v["st"] else "NEW")
    print(flag, "|", v["name"], "|", v["cat"], "|", v["addr"], "|", v["st"], "|", ",".join(v["dup"]), "|", v["q"][0])
