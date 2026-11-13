"""Точки мест робота sections 13.11 (06 UTC, 1113g): справка OSM sec13g-* — объект OSM с тем же названием (match), иначе
здание строго по адресу источника (улица + номер дома/корпуса/строения совпадают).
python3 tools/sections_1113g_pick.py → tools/sections_1113g_points.json"""
import json, os, re, math
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
A = json.load(open(os.path.join(ROOT, "auto", "osm-answers.json")))
HN = {"gladiator-taganskaya": ["40 с2"], "gladiator-luganskaya": ["4 к2"], "gladiator-marksistskaya": ["9 с1"],
      "gladiator-izyumskaya": ["22 к3"], "gladiator-kovshovoy": ["8 к1"], "gladiator-obrucheva": ["23 к3"],
      "gladiator-rudnevka": ["5"], "gladiator-vernadskogo": ["21 к3"], "tkd-yug-sholokhova": ["5 к2"],
      "tkd-yug-lukinskaya": ["9 к1"], "tkd-yug-bromley": ["6"], "husky-basket-latsisa": ["16"], "mon-svobody": ["91"],
      "dobrynya-svobody": ["89 к5"], "footballmsk-zhivopisnaya": ["21 с4"], "footballmsk-peschanaya": ["2А", "2а"],
      "footballmsk-novozavodskaya": ["27А с1", "27а с1"], "footballmsk-razumovskaya": ["22"],
      "footballmsk-ostrovityanova": ["10"], "footballmsk-yaroslavskaya": ["12"], "musa-tkd-leninsky": ["158"],
      "mir-edinoborstv-polyany": ["53"], "baglay-aerial-tushinskaya": ["19"]}
ST = {"gladiator-vernadskogo": "Вернадского", "footballmsk-peschanaya": "3-я Песчаная", "footballmsk-razumovskaya": "Петровско-Разумовская",
      "musa-tkd-leninsky": "Ленинский"}
def n(s): return re.sub(r"\s+", " ", (s or "").replace("корп.", "к").replace("стр.", "с")).strip().lower()
PT, MISS = {}, {}
for pid, hns in HN.items():
    a = A["sec13g-" + pid]
    st = ST.get(pid, a["query"]["street"]).lower()
    bs = {b["osm"]: b for b in a["buildings"] if st.split()[-1].lower()[:6] in (b.get("addr:street") or "").lower()
          and n(b.get("addr:housenumber")) in [n(h) for h in hns]}
    key = a["query"]["name"].lower()[:6]
    m = [p for p in a["pois"] if key in (p.get("name") or "").lower() and len(bs) == 1
         and math.hypot((p["lat"] - list(bs.values())[0]["lat"]) * 111000, (p["lon"] - list(bs.values())[0]["lon"]) * 63000) < 120]
    if len({p["osm"] for p in m}) == 1:
        p = m[0]; PT[pid] = [p["lat"], p["lon"], f"объект OpenStreetMap {p['osm']} «{p['name']}» в здании по адресу", "объект"]; continue
    if len(bs) == 1:
        b = list(bs.values())[0]
        PT[pid] = [b["lat"], b["lon"], f"по адресу: здание из OpenStreetMap {b['osm']} ({b['addr:street']}, {b['addr:housenumber']})", "дом"]
    else:
        MISS[pid] = [(b["osm"], b.get("addr:street"), b.get("addr:housenumber")) for b in bs.values()] or [x.get("name") for x in m]
# разобрано вручную: два контура с одним адресом рядом (≤45 м) — берём здание/стадион
for pid, osm, why in (("footballmsk-peschanaya", "relation/3868693", "стадион «ВЭБ Арена», 3-я Песчаная улица, 2А"),
                      ("footballmsk-novozavodskaya", "way/44423189", "Новозаводская улица, 27А"),
                      ("mir-edinoborstv-polyany", "way/35424107", "улица Поляны, 53 — здание школы № 1883")):
    b = [x for x in A["sec13g-" + pid]["buildings"] if x["osm"] == osm][0]
    PT[pid] = [b["lat"], b["lon"], f"по адресу: здание из OpenStreetMap {osm} ({why})", "дом"]; MISS.pop(pid, None)
# повторная справка sec13h-* с точным центром (у первой справки нужный дом не попал в 120 ближайших)
for pid, hns in (("husky-basket-latsisa", ["16"]), ("mon-svobody", ["91"]), ("dobrynya-svobody", ["89 к5"]),
                 ("footballmsk-zhivopisnaya", ["21 с4"]), ("footballmsk-ostrovityanova", ["10"]), ("musa-tkd-leninsky", ["158"]),
                 ("tkd-yug-bromley", ["6"])):
    a = A.get("sec13h-" + pid)
    if not a: continue
    st = a["query"]["street"].lower()
    bs = {b["osm"]: b for b in a["buildings"] if st[:6] in (b.get("addr:street") or "").lower() and n(b.get("addr:housenumber")) in [n(h) for h in hns]}
    if len(bs) == 1:
        b = list(bs.values())[0]
        PT[pid] = [b["lat"], b["lon"], f"по адресу: здание из OpenStreetMap {b['osm']} ({b['addr:street']}, {b['addr:housenumber']})", "дом"]; MISS.pop(pid, None)
    else:
        MISS[pid] = [(b["osm"], b.get("addr:housenumber")) for b in bs.values()]
json.dump(PT, open(os.path.join(ROOT, "tools", "sections_1113g_points.json"), "w"), ensure_ascii=False, indent=1)
print(len(PT)); print(json.dumps(MISS, ensure_ascii=False))
for k, v in PT.items(): print(k, v[2], v[3])
