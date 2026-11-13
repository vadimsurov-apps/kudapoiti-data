"""Точки мест робота sections 13.11 (15 UTC, 1113t): справка OSM sec13t-* — объект OSM с тем же названием в здании по адресу
(уровень «объект»), иначе здание строго по адресу источника (улица + номер дома/корпуса/строения совпадают, уровень «дом»).
python3 tools/sections_1113t_pick.py → tools/sections_1113t_points.json"""
import json, os, re, math
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
A = json.load(open(os.path.join(ROOT, "auto", "osm-answers.json")))
HN = {"mfteam-polyarnaya": ["21"], "upgrade-molodtsova": ["2 к4", "2к4"], "musa-tkd-leninsky": ["158"],
      "white-lotus-vernadskogo": ["37 к2", "37к2"], "tornado-fc-kirovogradskaya": ["23"], "acroarena-novoyasenevsky": ["26"],
      "yarkova-gym-aviamotornaya": ["30А к1", "30Ак1", "30а к1"], "torpedo-boxing-vostochnaya": ["4А с4", "4Ас4"],
      "aerial-vostochnaya": ["4А с4", "4Ас4"], "football-lab-panferova": ["8 к2", "8к2"],
      "bekhoev-team-borisovskie": ["26 к2", "26к2"], "facultet-pro-altufyevskoe": ["70 к1"], "fiet-nezhinskaya": ["17 к4", "17к4"],
      "karate1-babushkina": ["26"], "novy-orion-babushkina": ["17 к1", "17к1"]}
def n(s): return re.sub(r"\s+", "", (s or "").replace("корп.", "к").replace("стр.", "с").replace("строение", "с")).lower()
PT, MISS = {}, {}
for pid, hns in HN.items():
    a = A.get("sec13t-" + pid)
    if not a:
        MISS[pid] = "нет ответа"; continue
    st = a["query"]["street"].lower()
    bs = {b["osm"]: b for b in a["buildings"] if st[:6] in (b.get("addr:street") or "").lower()
          and n(b.get("addr:housenumber")) in [n(h) for h in hns]}
    m = [p for p in a["pois"] if p.get("match") and len(bs) == 1
         and math.hypot((p["lat"] - list(bs.values())[0]["lat"]) * 111000, (p["lon"] - list(bs.values())[0]["lon"]) * 63000) < 80]
    if len({p["osm"] for p in m}) == 1:
        p = m[0]; PT[pid] = [p["lat"], p["lon"], f"объект OpenStreetMap {p['osm']} «{p['name']}» в здании по адресу", "объект"]; continue
    if len(bs) == 1:
        b = list(bs.values())[0]
        PT[pid] = [b["lat"], b["lon"], f"по адресу: здание из OpenStreetMap {b['osm']} ({b['addr:street']}, {b['addr:housenumber']})", "дом"]
    else:
        MISS[pid] = [(b["osm"], b.get("addr:street"), b.get("addr:housenumber")) for b in bs.values()]
json.dump(PT, open(os.path.join(ROOT, "tools", "sections_1113t_points.json"), "w"), ensure_ascii=False, indent=1)
print(len(PT)); print(json.dumps(MISS, ensure_ascii=False))
for k, v in PT.items(): print(k, v[2], v[3])
