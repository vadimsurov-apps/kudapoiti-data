"""Точки мест робота sections 13.11 (18 UTC, 1113v): справка OSM sec13v-* — объект OSM с тем же названием в здании по адресу
(уровень «объект»), иначе здание строго по адресу источника (улица + номер дома/корпуса/строения совпадают, уровень «дом»).
python3 tools/sections_1113v_pick.py → tools/sections_1113v_points.json"""
import json, os, re, math
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
A = json.load(open(os.path.join(ROOT, "auto", "osm-answers.json")))
HN = {"vdokhnovenie-gym-miklukho": ["16/10 к18", "16/10к18", "16/10 с18"],
      "first-step-basket-sholokhova": ["9"], "first-step-basket-fedosyino": ["4 к2", "4к2"], "first-step-basket-ramenki": ["15 к2", "15к2"],
      "first-step-basket-kozhinoy": ["13"], "first-step-basket-myachkovsky": ["10 к2", "10к2"], "first-step-basket-krasnogo-mayaka": ["28 к1", "28к1"],
      "roshchin-team-ulyanina": ["5"], "sk-nevsky-gritsevtsa": ["3 с2", "3с2"],
      "agatsukan-9-maya": ["21 к2", "21к2"], "agatsukan-podrezkovo": ["2"], "specnaz21-altufyevskoe": ["64"],
      "voronin-sambo-moskovsky": ["2"], "glissada-proizvodstvennaya": ["4А", "4а"], "mosgimnastika-rimskogo-korsakova": ["11А", "11а"]}
def n(s): return re.sub(r"\s+", "", (s or "").replace("корп.", "к").replace("стр.", "с").replace("строение", "с")).lower()
PT, MISS = {}, {}
for pid, hns in HN.items():
    a = A.get("sec13v2-" + pid) or A.get("sec13v-" + pid)
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
# Хабарова, 2: в OSM два здания с этим номером — берём relation/7110329 (основной корпус ТРЦ «Новомосковский», у него
# стоят точки других мест ТРЦ), второе — пристройка в 230 м
a = A["sec13v2-voronin-sambo-moskovsky"]
b = [b for b in a["buildings"] if b["osm"] == "relation/7110329"][0]
PT["voronin-sambo-moskovsky"] = [b["lat"], b["lon"], f"по адресу: здание из OpenStreetMap {b['osm']} ({b['addr:street']}, {b['addr:housenumber']}, ТРЦ «Новомосковский»)", "дом"]
MISS.pop("voronin-sambo-moskovsky", None)
json.dump(PT, open(os.path.join(ROOT, "tools", "sections_1113v_points.json"), "w"), ensure_ascii=False, indent=1)
print(len(PT)); print(json.dumps(MISS, ensure_ascii=False))
for k, v in PT.items(): print(k, v[2], v[3])
