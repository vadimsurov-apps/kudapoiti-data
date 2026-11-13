"""Точки мест робота sections 13.11 (09 UTC, 1113i): справка OSM sec13i-* — объект OSM с тем же названием в здании по адресу
(уровень «объект»), иначе здание строго по адресу источника (улица + номер дома/корпуса/строения совпадают, уровень «дом»).
python3 tools/sections_1113i_pick.py → tools/sections_1113i_points.json"""
import json, os, re, math
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
A = json.load(open(os.path.join(ROOT, "auto", "osm-answers.json")))
HN = {"rg-prosport-festivalnaya": ["4Б"], "sambo-goncharov-leninsky": ["30"], "kanrit-malaya-tulskaya": ["16"],
      "akro-miks-gazoprovod": ["9А"], "valset-chertanovskaya": ["23А"], "mir-edinoborstv-starokachalovskaya": ["1Д"],
      "corsair-barklaya": ["6 с5"], "flamingo-club-luzhniki": ["24 с5"], "shingitay-khoroshevskoe": ["42"],
      "salto-style-komarova": ["11В"], "rhythm-club-moskovsky": ["23Г с1", "23г с1", "23Г"], "zapad-sport-novozavodskaya": ["27А с1"]}
def n(s): return re.sub(r"\s+", " ", (s or "").replace("корп.", "к").replace("стр.", "с").replace("строение", "с")).strip().lower()
PT, MISS = {}, {}
for pid, hns in HN.items():
    a = A.get("sec13i-" + pid)
    if not a:
        MISS[pid] = "нет ответа"; continue
    st = a["query"]["street"].lower()
    bs = {b["osm"]: b for b in a["buildings"] if st[:6] in (b.get("addr:street") or "").lower()
          and n(b.get("addr:housenumber")) in [n(h) for h in hns]}
    key = a["query"]["name"].lower()[:5]
    m = [p for p in a["pois"] if p.get("match") and len(bs) == 1
         and math.hypot((p["lat"] - list(bs.values())[0]["lat"]) * 111000, (p["lon"] - list(bs.values())[0]["lon"]) * 63000) < 80]
    if len({p["osm"] for p in m}) == 1:
        p = m[0]; PT[pid] = [p["lat"], p["lon"], f"объект OpenStreetMap {p['osm']} «{p['name']}» в здании по адресу", "объект"]; continue
    if len(bs) == 1:
        b = list(bs.values())[0]
        PT[pid] = [b["lat"], b["lon"], f"по адресу: здание из OpenStreetMap {b['osm']} ({b['addr:street']}, {b['addr:housenumber']})", "дом"]
    else:
        MISS[pid] = [(b["osm"], b.get("addr:street"), b.get("addr:housenumber")) for b in bs.values()]
# разобрано вручную: УСЗ «Дружба» — объект OSM самого зала (адрес клуба — Лужнецкая наб., 24, стр. 5 = УСЗ «Дружба»);
# Новозаводская, 27А — два контура с одним адресом, берём здание стадиона «Фили» way/44423189 (как в 1113g)
for pid, osm, key, lvl in (("flamingo-club-luzhniki", "way/52708461", "pois", "объект"),
                           ("zapad-sport-novozavodskaya", "way/44423189", "buildings", "дом")):
    b = [x for x in A["sec13i-" + pid][key] if x["osm"] == osm][0]
    why = (f"объект OpenStreetMap {osm} «{b.get('name')}» — зал, где занимается клуб" if lvl == "объект"
           else f"по адресу: здание из OpenStreetMap {osm} ({b.get('addr:street')}, {b.get('addr:housenumber')})")
    PT[pid] = [b["lat"], b["lon"], why, lvl]; MISS.pop(pid, None)
json.dump(PT, open(os.path.join(ROOT, "tools", "sections_1113i_points.json"), "w"), ensure_ascii=False, indent=1)
print(len(PT)); print(json.dumps(MISS, ensure_ascii=False))
for k, v in PT.items(): print(k, v[2], v[3])
