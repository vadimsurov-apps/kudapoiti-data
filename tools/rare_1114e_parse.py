"""Робот rare 1114e: разбор выдач Яндекс Карт из auto/pages по маске ключа → список организаций (имя, рубрика, адрес,
статус) без тех, что уже есть в places-all.json и data/parts/*.xlsx (по нормализованному названию).
python3 tools/rare_1114e_parse.py <маска> [...]"""
import json, os, re, sys, glob
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
def norm(s):
    s = s.lower().replace("ё", "е")
    s = re.sub(r"[«»\"'()\-–—.,:!]", " ", s)
    return " ".join(w for w in s.split() if w not in {"каток", "клуб", "школа", "спортивный", "комплекс", "центр", "и", "в", "на"})
def known():
    names = set()
    for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]:
        names.add(norm(p["name"]))
    try:
        import openpyxl
        for f in glob.glob(os.path.join(ROOT, "data/parts/*.xlsx")):
            ws = openpyxl.load_workbook(f, read_only=True).active
            rows = ws.iter_rows(values_only=True); hdr = next(rows)
            i = list(hdr).index("Название") if "Название" in hdr else 1
            for r in rows:
                if r[i]: names.add(norm(str(r[i])))
    except Exception as e:
        print("xlsx:", e, file=sys.stderr)
    return names
def parse(txt):
    part = txt.split("\n### ")[0]
    lines = part.split("\n")[2:]
    out = []
    i = 0
    while i < len(lines):
        l = lines[i]
        if l.endswith(" Фото") and i + 1 < len(lines) and lines[i + 1] == l[:-5]:
            name = lines[i + 1]; j = i + 2; info = []
            while j < len(lines) and not (lines[j].endswith(" Фото") and j + 1 < len(lines) and lines[j + 1] == lines[j][:-5]):
                info.append(lines[j]); j += 1
            out.append((name, info)); i = j
        else:
            i += 1
    return out
if __name__ == "__main__":
    K = known()
    ix = json.load(open(os.path.join(ROOT, "auto/pages/index.json")))
    seen = {}
    for key in sorted(ix):
        if not any(m in key for m in sys.argv[1:]): continue
        f = os.path.join(ROOT, "auto/pages", key + ".txt")
        if not os.path.exists(f): continue
        txt = open(f).read()
        q = txt.split("\n")[1] if "\n" in txt else ""
        for name, info in parse(txt):
            n = norm(name)
            if n in K or name in seen: continue
            inf = [x for x in info if not x.startswith(("Рейтинг", "Открыто", "Закрыто")) and "оцен" not in x]
            seen[name] = (q, inf[:4])
    for name, (q, inf) in seen.items():
        print(f"{name} || {' | '.join(inf)}   [{q}]")
