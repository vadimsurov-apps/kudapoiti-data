"""Робот edu 14.11 (26-й запуск): справка OSM edu42* застряла в Action, поэтому точка — здание OSM строго по адресу карточки из уже
выгруженных ответов auto/osm-answers.json (другие запросы рядом): полное совпадение улицы (с типом: улица/проспект/бульвар…),
номера дома и расстояние до центра района запроса в пределах его радиуса. Неоднозначно (несколько разных зданий) — не берём.
python3 tools/edu_1136_pick0.py → дописывает tools/edu_1136_points.json"""
import json, os, re, sys, io, contextlib, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
with contextlib.redirect_stdout(io.StringIO()):
    import edu_1136_pick as PK
    import edu_1136_q as Q
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
AB = {"ул.": "улица", "просп.": "проспект", "бул.": "бульвар", "наб.": "набережная", "ш.": "шоссе", "пер.": "переулок", "пр.": "проезд", "б-р": "бульвар"}
def nst(s):
    s = (s or "").lower().replace("ё", "е")
    for a, b in AB.items(): s = re.sub(r"(^|\s)" + re.escape(a) + r"(?=\s|$)", r"\1" + b, s)
    return tuple(sorted(w for w in re.split(r"[\s.]+", s) if w and w != "имени"))
def street(addr):
    for part in addr.split(","):
        if re.search(r"(ул\.|улица|ш\.|шоссе|просп|бул\.|бульвар|пер\.|наб\.|проезд|площадь|Вал)", part): return nst(part.strip())
def dist(a, b, c, d):
    return math.hypot((a - c) * 111000, (b - d) * 111000 * math.cos(math.radians(a)))
A = json.load(open(os.path.join(ROOT, "auto/osm-answers.json")))
B = {}
for a in A.values():
    for b in a.get("buildings", []): B.setdefault(b.get("osm"), b)
QQ = {q["id"]: q for q in Q.Q}
pp = os.path.join(ROOT, "tools/edu_1136_points.json")
PT = json.load(open(pp)) if os.path.exists(pp) else {}
for pid, (key, qid) in PK.JOBS.items():
    if pid in PT: continue
    addr = PK.ADDR_FIX.get(pid) or PK.A21.addr_how(key)[0]
    hn, st, q = PK.house(addr), street(addr), QQ.get(qid)
    if not hn or not st or not q: print("нет", pid, addr); continue
    bl = [b for b in B.values() if PK.osm_hn(b.get("addr:housenumber")) == hn and nst(b.get("addr:street")) == st and dist(b["lat"], b["lon"], q["lat"], q["lon"]) <= q["radius"]]
    bl = {b["osm"]: b for b in bl}
    if len(bl) == 1:
        b = list(bl.values())[0]
        PT[pid] = (b["lat"], b["lon"], f'точно (OpenStreetMap), здание {b["osm"]} по адресу {b.get("addr:street")}, {b.get("addr:housenumber")}')
        print("OK", pid, PT[pid][2])
    else:
        print("нет", pid, addr, len(bl))
json.dump(PT, open(pp, "w"), ensure_ascii=False, indent=1)
print(len(PT))
