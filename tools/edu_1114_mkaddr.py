"""Робот edu 11.11 (четвёртый запуск): адреса, телефоны, сайты и «Как найти» мест из карточек Яндекс Карт (auto/pages *-ev<N>-1114e*).
python3 tools/edu_1114_mkaddr.py <cards.json> <cand.json> → tools/edu_1114_addr.json (дописывает)"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from edu_1114_sel import SEL
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
C = json.load(open(sys.argv[1])); CAND = json.load(open(sys.argv[2]))
OFF = int(sys.argv[3]) if len(sys.argv) > 3 else 0
P = os.path.join(ROOT, "tools", "edu_1114_addr.json")
A = json.load(open(P)) if os.path.exists(P) else {}


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


for n, v in SEL.items():
    if n < OFF or n >= OFF + 300:
        continue
    d = C.get(str(n - OFF)); x = CAND[n - OFF]
    if not d:
        continue
    site = d.get("site")
    if site and not site.startswith("clck."):
        site = "https://" + site.rstrip("/") + ("/" if "/" not in site else "")
    else:
        site = None
    q = f'{x["topic"]} | {x["area"]}'
    if x["area"] in ("Реутов", "Долгопрудный", "Жуковский", "Видное", "Пушкино"):
        q = q.replace(" | ", " ")
    A[v[0]] = {"n": n, "addr": d["addr"], "addr2": d["addr2"], "how": how(d["addr2"]), "phone": d["phone"], "site": site,
               "q": q, "page": d["key"], "rubric": d["rubric"], "qid": f"edu14-{n}", "street": x.get("street")}
json.dump(A, open(P, "w"), ensure_ascii=False, indent=1)
print(len(A))
for k, a in A.items():
    print(k, "|", a["addr"], "|", (a["how"] or "").replace("\n", " / "), "|", a["site"])
