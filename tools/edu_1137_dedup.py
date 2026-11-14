"""Робот edu 14.11 (27-й запуск): кандидаты выдач → убрать повторы, уже имеющиеся у нас (places-all.json + data/parts/*.xlsx, название в том же
доме или том же городе), рубрики вне области edu, места вне Москвы и области; найти здание OSM (tools/edu_geo.py). → tools/edu_1137_keep.json"""
import json, os, re, glob, sys
import openpyxl
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import edu_geo as G
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
C = json.load(open(os.path.join(ROOT, "tools/edu_1137_cands.json")))
PL = json.load(open(os.path.join(ROOT, "places-all.json")))["places"]
def core(n):
    n = re.sub(r"\(.*?\)", "", n or "").lower().replace("ё", "е")
    n = re.sub(r"(детский|развивающий|центр|сад|школа|клуб|студия|программирования|логопедический|частный|развития|«|»|\"|,|\.)", " ", n)
    return re.sub(r"[^a-zа-я0-9]", "", n)
have = [(p["id"], p.get("name"), p.get("address") or "") for p in PL]
for f in glob.glob(os.path.join(ROOT, "data/parts/*.xlsx")):
    ws = openpyxl.load_workbook(f, read_only=True)["Места"]
    rows = ws.iter_rows(values_only=True); h = list(next(rows)); iN, iA = h.index("Название"), h.index("Адрес")
    have += [(r[0], r[iN], r[iA] or "") for r in rows if r[0]]
HV = [(i, core(n), G.town(a) or "Москва", (G.street(a), G.house(a))) for i, n, a in have]
BAD = re.compile(r"(Бассейн|Обучение плаванию|Школа искусств|Общеобразовательная школа|Начальная школа|Гимназия|Лицей|Творческий коллектив|Медцентр|клиника|Больница|Поликлиника|Стоматолог|Театральное образование|Школа танцев|Музыкальное образование|Спортивн|Фитнес|Салон|Магазин|ВУЗ|Колледж|Детский сад, ясли|Государственн|Дом культуры|Библиотека|Социальная служба|Медицинская реабилитация|Санаторий|Аптека|Массажный салон|Косметология)", re.I)
OK_INC = re.compile(r"(ОВЗ|инклюз|аутизм|особ|РАС|Даун|адаптив|иппотерап|сенсор)", re.I)
seen, keep, dup, bad = set(), [], [], []
for c in C:
    k = (core(c["name"]), c["addr"])
    if k in seen: continue
    seen.add(k)
    t = G.town(c["addr"])
    if not t: bad.append(("город", c["name"], c["addr"])); continue
    if BAD.search(c["rubric"]) and not OK_INC.search(c["name"] + " " + c["rubric"]): bad.append(("рубрика", c["name"], c["rubric"])); continue
    nm, hs = core(c["name"]), (G.street(c["addr"]), G.house(c["addr"]))
    hit = [h for h in HV if h[1] and len(nm) > 3 and (nm in h[1] or h[1] in nm) and h[2] == t and (h[3] == hs or len(nm) > 6 or h[3][0] is None)
           or (h[3] == hs and hs[1] and h[1] and nm and (nm[:5] in h[1] or h[1][:5] in nm))]
    if hit: dup.append((c["name"], c["addr"], [h[0] for h in hit][:3])); continue
    c["town"] = t
    c["pt"] = G.geo(c["addr"], c["name"])
    keep.append(c)
json.dump(keep, open(os.path.join(ROOT, "tools/edu_1137_keep.json"), "w"), ensure_ascii=False, indent=0)
print("keep", len(keep), "с точкой", sum(1 for c in keep if c["pt"]), "dup", len(dup), "bad", len(bad))
for c in keep: print(("PT " if c["pt"] else "-- ") + f'{c["n"]} | {c["name"]} | {c["rubric"]} | {c["addr"]} | {c["q"]}')
