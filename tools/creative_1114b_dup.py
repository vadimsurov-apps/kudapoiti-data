"""Доп. проверка дублей кандидатов 1114b по телефону и домену сайта (places-all + data/parts)."""
import json, re, glob, openpyxl
X = json.load(open("tools/creative_1114b_ext.json"))
pa = json.load(open("places-all.json")); pa = pa["places"] if isinstance(pa, dict) else pa
def dig(s): return re.sub(r"\D", "", s or "")[-10:]
def dom(s): return re.sub(r"^(https?://)?(www\.)?", "", (s or "").lower()).split("/")[0]
ph, dm = {}, {}
for p in pa:
    for f in ("phone",): 
        if p.get(f): ph.setdefault(dig(p[f]), []).append(p["id"])
    if p.get("url"): dm.setdefault(dom(p["url"]), []).append((p["id"], p.get("address")))
for f in glob.glob("data/parts/*.xlsx") + ["data/kuda-poiti-mesta.xlsx"]:
    ws = openpyxl.load_workbook(f, read_only=True)["Места"]; h = None
    for r in ws.iter_rows(values_only=True):
        if h is None: h = list(r); continue
        d = dict(zip(h, r))
        if d.get("Телефон"): ph.setdefault(dig(str(d["Телефон"])), []).append(d["id"])
        if d.get("Сайт"): dm.setdefault(dom(d["Сайт"]), []).append((d["id"], d.get("Адрес")))
for k, o in X.items():
    hits = ph.get(dig(o.get("phone")), []) if o.get("phone") else []
    dh = dm.get(dom(o.get("site")), []) if o.get("site") else []
    if hits or dh: print(k, o["name"], "|", o.get("addr"), "| phone:", hits[:3], "| site:", dh[:4])
