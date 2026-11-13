"""Схема метро и МЦК для маршрутов «игрушечной железной дорогой» (Вадим 13.11: «строить железную дорогу от станции до
станции с пересадками… наподобие путей из детского конструктора»).
Источник — OSM: отношения route=subway (+ МЦК), остановки в порядке следования, геометрия путей; пересадки — stop_area_group.
  python3 pipeline/metro_graph.py ids   rel.osm          → ids.txt (какие отношения-маршруты нужны с геометрией)
  python3 pipeline/metro_graph.py build rel.osm routes.osm → metro-graph.json (+ auto/metro-graph-report.json)
Формат metro-graph.json: lines [{id,name,color}], stations [{id,name,line,lat,lon}], edges [{a,b,sec,pts[[lat,lon]…]}],
transfers [{a,b,sec}], exits [{id,lat,lon,ref,st:[id станций]}] (выходы из metro-exits.json, привязанные к станциям)."""
import json, math, re, sys, os, datetime
import xml.etree.ElementTree as ET

def dist(a, b, c, d):
    k = math.cos(math.radians((a + c) / 2))
    return math.hypot((a - c) * 111320, (b - d) * 111320 * k)

def norm(s):
    return re.sub(r"[^a-zа-я0-9]+", " ", (s or "").lower().replace("ё", "е")).strip()

def parse(path):
    nodes, ways, rels = {}, {}, {}
    for ev, el in ET.iterparse(path):
        if el.tag == "node":
            nodes[el.get("id")] = (float(el.get("lat")), float(el.get("lon")), {x.get("k"): x.get("v") for x in el.findall("tag")})
            el.clear()
        elif el.tag == "way":
            ways[el.get("id")] = [x.get("ref") for x in el.findall("nd")]
            el.clear()
        elif el.tag == "relation":
            rels[el.get("id")] = ({x.get("k"): x.get("v") for x in el.findall("tag")},
                                  [(m.get("type"), m.get("ref"), m.get("role") or "") for m in el.findall("member")])
            el.clear()
    return nodes, ways, rels

def is_mcc(t):
    s = " ".join([t.get("network", ""), t.get("name", ""), t.get("operator", "")])
    return t.get("route") == "train" and ("МЦК" in s or "Московское центральное кольцо" in s)

def wanted(rels):
    return {rid for rid, (t, m) in rels.items() if t.get("type") == "route" and (t.get("route") in ("subway", "light_rail") or is_mcc(t))
            and t.get("state") != "proposed" and "construction" not in t.get("route", "")}

def simplify(pts, tol):
    if len(pts) < 3: return pts
    a, b = pts[0], pts[-1]; best, bi = 0, 0
    L = dist(a[0], a[1], b[0], b[1]) or 1e-9
    for i in range(1, len(pts) - 1):
        p = pts[i]
        k = math.cos(math.radians(a[0]))
        x1, y1 = 0, 0; x2, y2 = (b[1] - a[1]) * 111320 * k, (b[0] - a[0]) * 111320
        x0, y0 = (p[1] - a[1]) * 111320 * k, (p[0] - a[0]) * 111320
        d = abs((y2 - y1) * x0 - (x2 - x1) * y0) / L
        if d > best: best, bi = d, i
    if best <= tol: return [a, b]
    return simplify(pts[:bi + 1], tol)[:-1] + simplify(pts[bi:], tol)

def build(rel_path, routes_path):
    _, _, rels_all = parse(rel_path)
    nodes, ways, rels = parse(routes_path)
    want = wanted(rels)
    masters = {}
    for rid, (t, m) in rels_all.items():
        if t.get("type") == "route_master":
            for typ, ref, role in m:
                masters[ref] = t
    lines, stations, edges, node2st, report = {}, {}, {}, {}, {"routes": 0, "straight": [], "no_name": 0}
    def sid(line, name):
        key = (line, norm(name))
        if key not in stations:
            stations[key] = {"id": len(stations) + 1, "name": name, "line": line}
        return key
    for rid in sorted(want, key=int):
        t, mem = rels[rid]; mt = masters.get(rid, {})
        ref = "МЦК" if is_mcc(t) else (t.get("ref") or mt.get("ref") or "?")
        colour = t.get("colour") or mt.get("colour") or "#888888"
        lname = (mt.get("name") or t.get("name") or ref).split(":")[0].strip()
        if is_mcc(t): lname = "Московское центральное кольцо"
        lines.setdefault(ref, {"id": ref, "name": lname, "color": colour})
        stops = []
        for typ, r, role in mem:
            if typ == "node" and role.startswith("stop") and r in nodes:
                nm = nodes[r][2].get("name")
                if not nm: report["no_name"] += 1; continue
                nm = re.sub(r"^(станция метро|станция|метро)\s+", "", nm, flags=re.I).strip()
                stops.append((r, nm))
        if len(stops) < 2: continue
        report["routes"] += 1
        # цепочки путей
        chains, cur = [], []
        for typ, r, role in mem:
            if typ != "way" or r not in ways or role.startswith("platform"): continue
            w = ways[r]
            if not cur: cur = list(w)
            elif cur[-1] == w[0]: cur += w[1:]
            elif cur[-1] == w[-1]: cur += w[::-1][1:]
            elif cur[0] == w[0]: cur = cur[::-1] + w[1:]
            elif cur[0] == w[-1]: cur = cur[::-1] + w[::-1][1:]
            else: chains.append(cur); cur = list(w)
        if cur: chains.append(cur)
        def locate(nid):
            la, lo = nodes[nid][0], nodes[nid][1]; best = None
            for ci, ch in enumerate(chains):
                if nid in ch: return ci, ch.index(nid), 0
                for i, n in enumerate(ch):
                    if n in nodes:
                        d = dist(la, lo, nodes[n][0], nodes[n][1])
                        if best is None or d < best[2]: best = (ci, i, d)
            return best
        prev = None
        for nid, nm in stops:
            key = sid(ref, nm); node2st[nid] = key
            st = stations[key]
            if "lat" not in st: st["lat"], st["lon"] = nodes[nid][0], nodes[nid][1]
            if prev and prev[1] != key:
                ek = tuple(sorted([stations[prev[1]]["id"], st["id"]]))
                if ek not in edges:
                    a, b = locate(prev[0]), locate(nid); pts = None
                    pa, pb = nodes[prev[0]], nodes[nid]; straight = dist(pa[0], pa[1], pb[0], pb[1])
                    if a and b and a[0] == b[0] and a[2] < 80 and b[2] < 80:
                        ch = chains[a[0]]; i, j = a[1], b[1]
                        seg = ch[i:j + 1] if i <= j else ch[j:i + 1][::-1]
                        pts = [(nodes[n][0], nodes[n][1]) for n in seg if n in nodes]
                        ln = sum(dist(pts[k][0], pts[k][1], pts[k + 1][0], pts[k + 1][1]) for k in range(len(pts) - 1))
                        if ln > 2.5 * straight + 300 and ch[0] == ch[-1]:      # кольцо: взяли длинную сторону — берём другую
                            alt = (ch[j:] + ch[1:i + 1]) if i <= j else (ch[i:] + ch[1:j + 1])
                            alt = alt[::-1] if i <= j else alt
                            p2 = [(nodes[n][0], nodes[n][1]) for n in alt if n in nodes]
                            l2 = sum(dist(p2[k][0], p2[k][1], p2[k + 1][0], p2[k + 1][1]) for k in range(len(p2) - 1))
                            if l2 < ln: pts, ln = p2, l2
                        if ln > 2.5 * straight + 300 or len(pts) < 2: pts = None
                    if not pts:
                        pts = [(pa[0], pa[1]), (pb[0], pb[1])]; ln = straight
                        report["straight"].append(f"{ref}: {stations[prev[1]]['name']} — {nm}")
                    pts = [(pa[0], pa[1])] + pts[1:-1] + [(pb[0], pb[1])] if len(pts) > 2 else [(pa[0], pa[1]), (pb[0], pb[1])]
                    pts = simplify(pts, 6)
                    if stations[prev[1]]["id"] > st["id"]: pts = pts[::-1]
                    edges[ek] = {"a": ek[0], "b": ek[1], "sec": round(ln / 11.5 + 40),
                                 "pts": [[round(p[0], 6), round(p[1], 6)] for p in pts]}
            prev = (nid, key)
    # пересадки: stop_area_group → stop_area → узлы остановок
    area_nodes = {rid: [r for typ, r, role in m if typ == "node"] for rid, (t, m) in rels_all.items() if t.get("public_transport") == "stop_area"}
    transfers = {}
    def add_tr(k1, k2, how):
        if k1 == k2 or k1[0] == k2[0] and k1[1] == k2[1]: return
        a, b = stations[k1], stations[k2]
        d = dist(a["lat"], a["lon"], b["lat"], b["lon"])
        if d > 900: return
        ek = tuple(sorted([a["id"], b["id"]]))
        transfers.setdefault(ek, {"a": ek[0], "b": ek[1], "sec": round(150 + d / 1.1), "by": how})
    for rid, (t, m) in rels_all.items():
        if t.get("public_transport") == "stop_area_group":
            keys = {node2st[n] for typ, r, role in m if typ == "relation" for n in area_nodes.get(r, []) if n in node2st}
            keys = sorted(keys)
            for i in range(len(keys)):
                for j in range(i + 1, len(keys)): add_tr(keys[i], keys[j], "group")
    # выходы → станции; узлы с общим выходом («A / B») — тоже пересадка
    exits_out = []
    if os.path.exists("metro-exits.json"):
        by_name = {}
        for key, st in stations.items(): by_name.setdefault(key[1], []).append(key)
        for e in json.load(open("metro-exits.json"))["exits"]:
            ks = []
            for nm in e["station"].split(" / "):
                mcc = "(МЦК)" in nm; n = norm(nm.replace("(МЦК)", ""))
                c = [k for k in by_name.get(n, []) if (k[0] == "МЦК") == mcc and "lat" in stations[k]]
                c.sort(key=lambda k: dist(e["lat"], e["lon"], stations[k]["lat"], stations[k]["lon"]))
                if c and dist(e["lat"], e["lon"], stations[c[0]]["lat"], stations[c[0]]["lon"]) <= 900: ks.append(c[0])
            for i in range(len(ks)):
                for j in range(i + 1, len(ks)): add_tr(ks[i], ks[j], "exit")
            if ks:
                x = {"id": e["id"], "lat": e["lat"], "lon": e["lon"], "st": sorted({stations[k]["id"] for k in ks})}
                if e.get("ref"): x["ref"] = e["ref"]
                exits_out.append(x)
            else:
                report.setdefault("exits_no_station", []).append(e["station"])
    sts = sorted(({"id": s["id"], "name": s["name"], "line": s["line"], "lat": round(s["lat"], 6), "lon": round(s["lon"], 6)}
                  for s in stations.values() if "lat" in s), key=lambda s: s["id"])
    out = {"version": datetime.date.today().isoformat(), "source": "OpenStreetMap", "lines": sorted(lines.values(), key=lambda l: l["id"]),
           "stations": sts, "edges": sorted(edges.values(), key=lambda e: (e["a"], e["b"])),
           "transfers": [{k: v for k, v in t.items() if k != "by"} for t in sorted(transfers.values(), key=lambda t: (t["a"], t["b"]))],
           "exits": exits_out}
    json.dump(out, open("metro-graph.json", "w"), ensure_ascii=False, separators=(",", ":"))
    name = {s["id"]: f"{s['name']} ({s['line']})" for s in sts}
    report.update({"date": out["version"], "lines": [f"{l['id']} {l['name']} {l['color']}" for l in out["lines"]], "stations": len(sts),
                   "edges": len(edges), "transfers": sorted(f"{name[t['a']]} ↔ {name[t['b']]} [{t['by']}, {t['sec']} с]" for t in transfers.values()),
                   "exits": len(exits_out), "per_line": {l: sum(1 for s in sts if s["line"] == l) for l in lines},
                   "exits_no_station": sorted(set(report.get("exits_no_station", [])))})
    json.dump(report, open("auto/metro-graph-report.json", "w"), ensure_ascii=False, indent=1)
    print(f"линий {len(lines)}, станций {len(sts)}, перегонов {len(edges)} (прямой линией: {len(report['straight'])}), "
          f"пересадок {len(transfers)}, выходов привязано {len(exits_out)}, размер {os.path.getsize('metro-graph.json') // 1024} КБ")

if __name__ == "__main__":
    if sys.argv[1] == "ids":
        _, _, rels = parse(sys.argv[2])
        ids = wanted(rels)
        open("ids.txt", "w").write("".join(f"r{i}\n" for i in sorted(ids, key=int)))
        print("маршрутов:", len(ids))
    else:
        build(sys.argv[2], sys.argv[3])
