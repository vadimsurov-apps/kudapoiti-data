"""Точки из справки OSM cr14-*: объект OSM с названием места → «объект»; иначе входы на контуре здания с номером дома
из адреса: ровно один вход → «вход»; иначе — «дом» (координаты Яндекса), место скрыто до сверки."""
import json, os, re, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_creative_1114a import D
from creative_1114a_osmq import PTS
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
A = json.load(open(os.path.join(ROOT, "auto/osm-answers.json")))
NAMES = {"artkids": ["art kids", "арт кидс", "бондаренко"], "monstarz": ["monstarz", "монстарз"], "churochkina": ["чурочкин"],
         "art-balet": ["арт-балет", "арт балет"], "montoto": ["монтото"], "mechta": ["мечта"], "gitarus": ["гитарус", "gitarus"]}
def hn(addr):
    m = re.search(r",\s*(\d+[А-Яа-я]?)(?:,\s*(?:корп\.|стр\.)\s*(\d+))?\s*$", addr)
    if not m: return None
    return m.group(1).lower() + ("к" + m.group(2) if m.group(2) else "")
def dist(a, b, c, d):
    return math.hypot((a - c) * 111320, (b - d) * 111320 * math.cos(math.radians(a)))
def on_ring(lat, lon, geom):
    pts = []
    cs = geom["coordinates"]
    if geom["type"] == "MultiPolygon": rings = [r for poly in cs for r in poly]
    elif geom["type"] == "Polygon": rings = cs
    else: rings = [cs]
    for r in rings:
        for (x1, y1), (x2, y2) in zip(r, r[1:]):
            # расстояние до отрезка в метрах
            kx = 111320 * math.cos(math.radians(lat)); ky = 111320
            ax, ay, bx, by, px, py = x1 * kx, y1 * ky, x2 * kx, y2 * ky, lon * kx, lat * ky
            dx, dy = bx - ax, by - ay
            t = max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy or 1)))
            if math.hypot(ax + t * dx - px, ay + t * dy - py) < 1.5: return True
    return False
out = {}
for pid in D:
    q = A.get("cr14-" + pid)
    ll = PTS[pid][0]
    if not q: print("нет ответа", pid); continue
    keys = next(v for k, v in NAMES.items() if pid.startswith(k))
    obj = [p for p in q["pois"] if p.get("name") and any(k in p["name"].lower() for k in keys) and p["d"] <= 150]
    if obj:
        o = obj[0]
        out[pid] = {"lat": o["lat"], "lon": o["lon"], "level": "объект", "osm": o["osm"],
                    "why": f'объект OSM «{o["name"]}», {o["d"]} м от точки здания по адресу'}
        continue
    h = hn(D[pid][6])
    blds = [b for b in q.get("outlines", []) if b.get("geom") and b.get("addr:housenumber") and
            re.sub(r"\s|корпус|стр.*", "", b["addr:housenumber"].lower().replace("к", "к")) == h and b["d"] <= 120]
    ents = []
    if blds:
        b = blds[0]
        ents = [e for e in q["entrances"] if e.get("entrance") and on_ring(e["lat"], e["lon"], b["geom"])]
        ents = list({e["osm"]: e for e in ents}.values())
    if len(ents) == 1:
        e = ents[0]
        out[pid] = {"lat": e["lat"], "lon": e["lon"], "level": "вход", "osm": e["osm"],
                    "why": f'единственный вход (entrance={e["entrance"]}) здания {blds[0]["osm"]} (дом {blds[0]["addr:housenumber"]})'}
    else:
        out[pid] = {"lat": ll[0], "lon": ll[1], "level": "дом", "osm": None,
                    "why": f'здание {"найдено" if blds else "не найдено"} в OSM, входов на контуре: {len(ents)}'}
    print(pid, out[pid]["level"], out[pid]["why"])
json.dump(out, open(os.path.join(ROOT, "tools/creative_1114a_points.json"), "w"), ensure_ascii=False, indent=1)
