"""Робот rare 14.11 (1114a): разбор обзорных страниц организаций Яндекс Карт (auto/pages/yandex-ru-maps-org-*) из выдачи
rr14q*/rr14x* → таблица кандидатов с отметкой дублей (по названию и по адресу в places-all.json).
python3 tools/rare_1114a_cards.py"""
import glob, json, os, re
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
P = json.load(open(os.path.join(ROOT, "places-all.json")))["places"]
def norm(s): return re.sub(r"[^a-zа-я0-9]", "", (s or "").lower().replace("ё", "е"))
def akey(a):
    a = (a or "").lower().replace("ё", "е")
    a = re.sub(r"москва,?|улица|ул\.|проспект|просп\.|пр-т|шоссе|ш\.|бульвар|бул\.|д\.|дом|,|\s", " ", a)
    return " ".join(a.split())[:40]
names = [(norm(p["name"]), p["id"]) for p in P]
addrs = [(akey(p.get("address")), p["id"], p["name"]) for p in P]
orgs = set()
for f in glob.glob(os.path.join(ROOT, "auto/pages/*rr14[qx]*1114a*.txt")):
    orgs |= set(re.findall(r"yandex\.ru/maps/org/([a-z0-9_]+)/(\d+)/", open(f).read()))
out = []
for slug, oid in sorted(orgs):
    f = os.path.join(ROOT, f"auto/pages/yandex-ru-maps-org-{slug.replace('_', '-')}-{oid}.txt")
    if not os.path.exists(f):
        out.append({"slug": slug, "oid": oid, "missing": True}); continue
    t = open(f).read().split("\n### ")[0]
    L = t.split("\n")
    try:
        i = L.index("Маршруты"); 
    except ValueError:
        i = 0
    name = L[i + 2] if i + 2 < len(L) else ""
    cat = L[i + 1]
    ph = next((l for l in L if l.startswith("+7")), "")
    ai = L.index("Адрес") if "Адрес" in L else -1
    addr = L[ai + 1] if ai >= 0 else ""
    ci = L.index("Контакты") if "Контакты" in L else -1
    site = ""
    if ci >= 0:
        for l in L[ci + 1:ci + 6]:
            if re.match(r"^[a-z0-9.-]+\.[a-z]{2,}(/\S*)?$", l): site = l; break
    hi = L.index("Время работы") if "Время работы" in L else -1
    hrs = L[hi + 1] if hi >= 0 else ""
    st = next((l for l in L[:30] if "не работает" in l.lower() or "закрыто навсегда" in l.lower() or "переехал" in l.lower()), "")
    n = norm(name); a = akey(addr)
    dupn = [pid for nn, pid in names if n and len(n) > 4 and (n == nn or (len(n) > 7 and (n in nn or nn in n)))]
    dupa = [f"{pid}~{nm}" for aa, pid, nm in addrs if a and aa and len(a) > 8 and (aa.startswith(a[:25]) or a.startswith(aa[:25]))]
    out.append({"slug": slug, "oid": oid, "name": name, "cat": cat, "addr": addr, "phone": ph, "site": site, "hours": hrs,
                "st": st, "dupn": dupn[:3], "dupa": dupa[:4]})
json.dump(out, open("/tmp/claude-0/cards.json", "w"), ensure_ascii=False, indent=1)
for o in out:
    if o.get("missing"): print("MISSING", o["slug"]); continue
    fl = "DUPN" if o["dupn"] else ("DUPA" if o["dupa"] else "NEW")
    print(fl, "|", o["slug"], "|", o["name"], "|", o["cat"], "|", o["addr"], "|", o["phone"], "|", o["site"], "|", o["st"], "|", ",".join(o["dupn"] or o["dupa"]))
