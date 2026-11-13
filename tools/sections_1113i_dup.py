"""Проверка дублей для робота sections (1113i): по названию в places-all.json и всех таблицах (main + data/parts)."""
import json, os, re, glob
import openpyxl
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
def norm(s): return re.sub(r"[^a-zа-я0-9]+", " ", (s or "").lower().replace("ё", "е")).strip()
pa = json.load(open(os.path.join(ROOT, "places-all.json")))["places"]
names = [(norm(p.get("name")), p.get("id"), p.get("address") or "", p.get("lat"), p.get("lon")) for p in pa]
for f in glob.glob(os.path.join(ROOT, "data/parts/*.xlsx")) + [os.path.join(ROOT, "data/kuda-poiti-mesta.xlsx")]:
    for r in openpyxl.load_workbook(f, read_only=True)["Места"].iter_rows(min_row=2, values_only=True):
        if r[0]: names.append((norm(r[1]), r[0], r[4] or "", r[5], r[6]))
STOP = {"школа", "клуб", "спортивный", "спортивная", "детская", "детский", "центр", "для", "детей", "секция", "и",
        "единоборств", "футбольная", "академия", "федерация", "сдюшор", "спортшкола", "фк", "мгфсо", "москомспорта", "гбу", "до", "дюсш", "сш"}
def addr_hits(addr):
    """места с тем же адресом (улица+дом)"""
    na = set(norm(addr).split()) - {"москва", "ул", "улица", "проспект", "просп", "корп", "к", "стр", "с", "этаж"}
    out = []
    for nn, pid, a, la, lo in names:
        sa = set(norm(a).split())
        if na and len(na & sa) >= max(2, len(na) - 1): out.append((pid, nn))
    return out
def dup(name, addr):
    n = norm(name); w = set(n.split()) - STOP
    for nn, pid, a, la, lo in names:
        if not nn: continue
        if nn == n or (w and w <= set(nn.split())):
            st = set(norm(addr).split()) & set(norm(a).split()) - {"москва", "ул", "улица", "проспект", "просп"}
            if st or nn == n: return pid
    return None
