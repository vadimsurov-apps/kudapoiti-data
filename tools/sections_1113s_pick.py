"""Точки мест робота sections 13.11 (21 UTC, 1113s): справка OSM sec13s-* — объект OSM с тем же названием в здании по адресу
(уровень «объект»), иначе здание строго по адресу источника (улица + номер дома/корпуса/строения совпадают, уровень «дом»).
python3 tools/sections_1113s_pick.py → tools/sections_1113s_points.json"""
import json, os, re, math
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
A = json.load(open(os.path.join(ROOT, "auto", "osm-answers.json")))
HN = {"flamingo-club-verkhnie-polya": ["29"], "flamingo-club-starokashirskoe": ["2 к11", "2к11"], "flamingo-club-vavilova-5": ["5 к2", "5к2"],
      "iskusstvo-dvizheniya-tyumensky": ["3 к5", "3к5"], "rhythm-club-buninskaya": ["9"], "lime-rg-bartenevskaya": ["17"],
      "arsenal-kids-pilyugina": ["14А", "14а"], "arsenal-kids-krylatskie": ["45 к2", "45к2"], "arsenal-kids-orekhovy": ["21 к2", "21к2"],
      "taekwon-pro-novorossiyskaya": ["36"], "taekwon-pro-karibia": ["10Б", "10б"], "taekwon-pro-samory-mashela": ["6 к4", "6к4"],
      "strike-fc-yablochkova": ["7"], "strike-fc-smolnaya": ["12"], "strike-fc-molodtsova": ["23"], "strike-fc-lokomotivny": ["13"]}
def n(s): return re.sub(r"\s+", "", (s or "").replace("корп.", "к").replace("стр.", "с").replace("строение", "с")).lower()
PT, MISS = {}, {}
for pid, hns in HN.items():
    a = A.get("sec13s2-" + pid) or A.get("sec13s-" + pid)
    if not a:
        MISS[pid] = "нет ответа"; continue
    st = a["query"]["street"].lower()
    bs = {b["osm"]: b for b in a["buildings"] if st[:6] in (b.get("addr:street") or "").lower()
          and n(b.get("addr:housenumber")) in [n(h) for h in hns]}
    m = [p for p in a["pois"] if p.get("match") and "церк" not in p["name"].lower() and len(bs) == 1
         and math.hypot((p["lat"] - list(bs.values())[0]["lat"]) * 111000, (p["lon"] - list(bs.values())[0]["lon"]) * 63000) < 80]
    if len({p["osm"] for p in m}) == 1:
        p = m[0]; PT[pid] = [p["lat"], p["lon"], f"объект OpenStreetMap {p['osm']} «{p['name']}» в здании по адресу", "объект"]; continue
    if len(bs) == 1:
        b = list(bs.values())[0]
        PT[pid] = [b["lat"], b["lon"], f"по адресу: здание из OpenStreetMap {b['osm']} ({b['addr:street']}, {b['addr:housenumber']})", "дом"]
    else:
        MISS[pid] = [(b["osm"], b.get("addr:street"), b.get("addr:housenumber")) for b in bs.values()]
# «Карибия» (Зелёный пр-т, 10Б): у здания в OSM нет адреса — берём контур самого центра way/131440393 «Центр семейного отдыха Карибия»
a = A.get("sec13s-taekwon-pro-karibia")
if a:
    k = [p for p in a["pois"] if p.get("osm") == "way/131440393"]
    if k:
        PT["taekwon-pro-karibia"] = [k[0]["lat"], k[0]["lon"], "объект OpenStreetMap way/131440393 «Центр семейного отдыха Карибия» (клуб занимается в центре)", "объект"]
        MISS.pop("taekwon-pro-karibia", None)
json.dump(PT, open(os.path.join(ROOT, "tools", "sections_1113s_points.json"), "w"), ensure_ascii=False, indent=1)
print(len(PT)); print(json.dumps(MISS, ensure_ascii=False))
for k, v in PT.items(): print(k, v[2], v[3])
