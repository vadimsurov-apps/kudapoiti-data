"""Робот edu 14.11 (26-й запуск): контроль дублей отобранных мест — ядро названия (без кавычек и скобок) + тот же населённый пункт,
и тот же дом (улица+номер) с похожим названием; по places-all.json и всем data/parts/*.xlsx."""
import json, os, re, sys, glob
import openpyxl
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from edu_1136_sel import SEL
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
def core(n):
    n = re.sub(r"\(.*?\)", "", n or "").lower().replace("ё", "е")
    n = re.sub(r"(детский|развивающий|центр|сад|школа|клуб|студия|программирования|логопедический|частный|центр развития|«|»|\"|,|\.)", " ", n)
    return re.sub(r"[^a-zа-я0-9]", "", n)
def town(a):
    a = a or ""
    for t in ("Зеленоград", "Мытищи", "Балашиха", "Одинцово", "Красногорск", "Люберцы", "Подольск", "Химки", "Пушкино", "Коммунарка", "Реутов"):
        if t in a: return t
    return "Москва"
def house(a):
    m = re.search(r"([А-ЯЁа-яё\-]+[^,]*?(ул\.|улица|ш\.|просп|бул|пер\.|наб|проезд|пр\.|площадь|Вал)[^,]*),\s*(д\.\s*)?(\d+\w*)", a or "")
    return (re.sub(r"[^а-яa-z0-9]", "", m.group(1).lower().replace("ё", "е")), m.group(4).lower()) if m else None
have = [(p["id"], p.get("name"), p.get("address")) for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]]
for f in glob.glob(os.path.join(ROOT, "data/parts/*.xlsx")):
    ws = openpyxl.load_workbook(f, read_only=True)["Места"]
    rows = ws.iter_rows(values_only=True); h = list(next(rows)); iN, iA = h.index("Название"), h.index("Адрес")
    have += [(r[0], r[iN], r[iA]) for r in rows if r[0]]
E = {}
for w, fn in (("36", "edu_1136_ext.json"), ("36g", "edu_1136_ext2.json"), ("36i", "edu_1136_ext3.json")):
    E.update({w + ":" + k: v for k, v in json.load(open(os.path.join(ROOT, "tools", fn))).items()})
ids = {h[0] for h in have}
bad = {}
for pid, v in SEL.items():
    if pid in ids: bad[pid] = ["тот же id"]; continue
    nm, ad = core(v[1]), E[v[0]]["addr"][0]
    for hid, hn, ha in have:
        c = core(hn)
        same_name = len(nm) > 3 and c and (nm in c or c in nm) and town(ha) == town(ad)
        same_house = house(ha) and house(ha) == house(ad) and c and nm and (nm[:5] in c or c[:5] in nm)
        if same_name and (house(ha) == house(ad) or not house(ha) or not house(ad)) or same_house:
            bad.setdefault(pid, []).append(f"{hid} | {hn} | {ha}")
for k, v in bad.items(): print(k, "→", v[:3])
print(len(bad))
