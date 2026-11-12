"""Робот edu 12.11 (шестой запуск): адреса/телефоны/сайты/«Как найти» отобранных мест из карточек Яндекс Карт
(auto/pages *-ev<N>-1116e*) → tools/edu_1116_addr.json; запросы OSM edu16-<N> дописываются в auto/osm-queries.json."""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_batch14 import MET
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
C = json.load(open(os.path.join(ROOT, "tools/edu_1116_cards.json")))
SEL = json.load(open(os.path.join(ROOT, "tools/edu_1116_sel.json")))
TOWN = {"Серпухов": (54.9150, 37.4110), "Орехово Зуево": (55.8060, 38.9800), "Раменское": (55.5690, 38.2300)}
def how(a2):
    out = []
    for p in [x.strip() for x in a2.split(",") if x.strip()]:
        if p.startswith("Метро") or p.startswith("Улица") or p.startswith("Чертаново") or p.startswith("Котельники"):
            continue
        if p.startswith("этаж"):
            out.append("Этаж: " + p[5:].strip())
        elif p.startswith("подъезд"):
            out.append("Вход: подъезд " + p[8:].strip())
        elif re.match(r"(офис|кабинет|помещение|комната)", p):
            out.append(p[0].upper() + p[1:])
        else:
            out.append("Вход: " + p[0].lower() + p[1:] if not p.lower().startswith("вход") else "Вход: " + p[5:].strip())
    # «Этаж» и «Офис» — одной строкой
    et = [x for x in out if x.startswith("Этаж")]; of = [x for x in out if re.match(r"(Офис|Кабинет|Помещение|Комната)", x)]
    rest = [x for x in out if x not in et + of]
    if et and of:
        et = [et[0] + ", " + of[0].lower()]; of = []
    return "\n".join(rest + et + of) or None


A = {}
Q = []
for pid, v in SEL.items():
    n = str(v["n"]); d = C[n]
    a = [x for x in d["addr"] if not x.startswith("Метро")] + [re.sub(r"^Метро:[^,]*(, [А-Яа-я]+)*?, (?=этаж)", "", x) for x in d["addr"] if x.startswith("Метро")]
    addr = d["addr"][0]
    if addr.endswith(", Москва"):
        addr = "Москва, " + addr[:-8]
    a2 = ", ".join(x for x in d["addr"][1:])
    site = d.get("site")
    site = ("https://" + site.rstrip("/") + "/") if site else None
    q = d["q"]
    area = q.split(" метро ")[-1] if " метро " in q else next(t for t in TOWN if q.endswith(t))
    if area in TOWN:
        lat, lon = TOWN[area]
    else:
        lat, lon = next((a_, b_) for nm, a_, b_ in MET if nm == area)
    m = re.search(r",\s*([^,]*?)(ул\.|пр\.|ш\.|пер\.|наб\.|просп\.)?\s*([^,]*?),\s*\d", addr)
    street = v.get("street")
    A[pid] = {"n": int(n), "addr": addr, "addr2": a2, "how": how(a2) if a2 else None, "phone": d["phone"], "site": site,
              "q": q, "page": d["page"], "org": d["org"], "qid": f"edu16-{n}", "street": street, "name": v["osmname"]}
    Q.append({"id": f"edu16-{n}", "lat": lat, "lon": lon, "radius": 5500, "name": v["osmname"], "street": street})
A["baby-club-izmaylovsky-5a"]["how"] = "Этаж: 1"
A["tropinki-4-parkovaya"]["how"] = None
json.dump(A, open(os.path.join(ROOT, "tools/edu_1116_addr.json"), "w"), ensure_ascii=False, indent=1)
if "--q" in sys.argv:
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("edu16-")]
    json.dump(old + Q, open(p, "w"), ensure_ascii=False, indent=1)
for k, x in A.items():
    print(k, "|", x["addr"], "|", (x["how"] or "").replace("\n", " / "), "|", x["street"], "|", x["site"])
