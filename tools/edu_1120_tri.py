"""Сводка карточек (ev<n>-1120e): рубрика, адрес, сайт, часы и фразы про ОВЗ/доступность/возраст — для отбора вручную."""
import json, os, re, glob
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
C = json.load(open(os.path.join(ROOT, "tools/edu_1120_cards.json")))
KW = re.compile(r"(ОВЗ|овз|инвалид|коляск|аутиз|РАС\b|расстройств|синдром|ДЦП|адаптив|инклюзи|особенн|сенсорн|пандус|доступн|туалет для|дефектолог|АВА|ABA|нейропсихолог|ЛФК|массаж|иппо)", re.I)
for n, d in sorted(C.items(), key=lambda x: int(x[0])):
    f = glob.glob(os.path.join(ROOT, f"auto/pages/*-ev{n}-1120e-*.txt"))[0]
    t = open(f).read()
    L = list(dict.fromkeys(l.strip() for l in t.splitlines() if KW.search(l) and len(l.strip()) < 200))
    print(f"== {n} {d['cand']} | {d['head'][:2]} | {d.get('addr')} | {d.get('phone')} | {d.get('site')} | {d.get('hours')}")
    print("   KW:", " ¦ ".join([x[:90] for x in L[:8]]))
    print("   AGE:", " ¦ ".join([x[:80] for x in (d["lines"] + d["more"])[:6]]))
