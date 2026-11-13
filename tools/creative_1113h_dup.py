"""Робот creative 1113h: строгая проверка дублей кандидатов (координаты ≤300 м + сайт/телефон/название) по places-all и всем data/parts."""
import json, glob, math, re, os, openpyxl
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
pa = json.load(open(os.path.join(ROOT, 'places-all.json'))); pa = pa['places'] if isinstance(pa, dict) else pa
ALL = [(p['id'], p.get('name') or '', p.get('lat'), p.get('lon'), (p.get('url') or '') + ' ' + (p.get('phone') or ''), p.get('categories') or p.get('cats') or '') for p in pa]
for f in glob.glob(os.path.join(ROOT, 'data/parts/*.xlsx')):
    ws = openpyxl.load_workbook(f, read_only=True)['Места']
    hdr = None
    for r in ws.iter_rows(values_only=True):
        if hdr is None: hdr = list(r); continue
        if not r[0]: continue
        d = dict(zip(hdr, r))
        ALL.append((d['id'], d.get('Название') or '', d.get('Широта'), d.get('Долгота'), f"{d.get('Сайт') or ''} {d.get('Телефон') or ''}", d.get('Категории') or ''))
def dist(a, b, c, d):
    try: return 6371000 * math.hypot(math.radians(c - a), math.radians(d - b) * math.cos(math.radians(a)))
    except Exception: return 1e9
def digits(p): return re.sub(r'\D', '', p or '')[-10:]
def check(name, ll, site, phone):
    out = []
    dom = re.sub(r'^(https?://)?(www\.)?', '', site or '').split('/')[0].lower()
    ph = digits(phone)
    for pid, n, la, lo, extra, cats in ALL:
        dd = dist(ll[0], ll[1], la, lo) if ll and la else 1e9
        hit = (dom and len(dom) > 4 and dom in extra.lower()) or (ph and len(ph) == 10 and ph in re.sub(r'\D', '', extra))
        if hit or dd < 120:
            out.append((pid, n, int(dd) if dd < 1e8 else None, 'URL/ТЕЛ' if hit else ''))
    return out
if __name__ == '__main__':
    X = json.load(open(os.path.join(ROOT, 'tools/creative_1113h_ext.json')))
    for k, o in X.items():
        if o.get('closed') or not o.get('org'): continue
        r = check(o.get('title') or o['name'], o.get('ll'), o.get('site'), o.get('phone'))
        print(k, o.get('title') or o['name'], '|', [x for x in r][:6])
