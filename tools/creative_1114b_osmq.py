"""Робот creative 14.11 (1114b): справка OSM cr14b-* (здания с контурами, входы, объекты рядом с точкой Яндекс Карт)."""
import json, os, sys, glob, re
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
X = json.load(open(os.path.join(ROOT, "tools/creative_1114b_ext.json")))
def cb(key):
    f = glob.glob(os.path.join(ROOT, f"auto/pages/*?cb-{key}-1114b-*.txt")) or glob.glob(os.path.join(ROOT, f"auto/pages/*-cb-{key}-1114b-*.txt"))
    if not f: return None
    m = re.search(r"Координаты : ([\d.]+), ([\d.]+)", open(f[0]).read())
    return [float(m.group(1)), float(m.group(2))] if m else None
PTS = {  # id: (координаты здания по адресу, название для поиска объекта OSM)
 "banya-chertanovo": (cb("banya-chertanovo"), "Баня"),
 "adm-zhukovskogo": (X["45"]["ll"], "мюзикл"),
 "akter-i-ko-shabolovka": (X["62"]["ll"], "Актер"),
 "active-style-uralskaya": (X["105"]["ll"], "Моссовета"),
 "jam-aviatsionnaya": (X["121"]["ll"], "Джем"),
 "zhivopisnaya-marshala-novikova": (X["124"]["ll"], "Живописная"),
 "taranda-denisovsky": (X["137"]["ll"], "Таранд"),
 "mir-iskusstva-ogorodnaya": (X["47"]["ll"], "Мир искусства"),
 "banya-sviblovo": (cb("banya-sviblovo"), "Баня"),
 "active-style-lazo": (cb("as-lazo"), "Active"),
 "active-style-otkrytoe": (cb("as-otkrytoe"), "Моссовета"),
 "active-style-pugachevskaya": (cb("as-pugachevskaya"), "Моссовета"),
 "active-style-vladimirskaya": (cb("as-vladimirskaya"), "Active"),
}
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = json.load(open(p)); have = {x["id"] for x in old}
    out = []
    for k, (ll, nm) in PTS.items():
        if not ll: print("нет координат", k); continue
        q = {"id": "cr14b-" + k, "lat": ll[0], "lon": ll[1], "radius": 150, "name": nm, "geom": True}
        if q["id"] not in have: out.append(q)
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print("новых запросов", len(out))
