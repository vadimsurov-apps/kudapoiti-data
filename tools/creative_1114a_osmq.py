"""Робот creative 14.11 (1114a): справка OSM cr14-* (здания с контурами, входы, объекты рядом с точкой Яндекс Карт)."""
import json, os, sys, glob, re
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
X = json.load(open(os.path.join(ROOT, "tools/creative_1114a_ext.json")))
def cb(key):
    f = glob.glob(os.path.join(ROOT, f"auto/pages/*?cb-{key}-1114a-*.txt")) or glob.glob(os.path.join(ROOT, f"auto/pages/*-cb-{key}-1114a-*.txt"))
    if not f: return None
    m = re.search(r"Координаты : ([\d.]+), ([\d.]+)", open(f[0]).read())
    return [float(m.group(1)), float(m.group(2))] if m else None
PTS = {  # id: (координаты здания по адресу, название для поиска объекта OSM)
 "artkids-narodnogo-opolcheniya": (X["88"]["ll"], "Art Kids"),
 "artkids-lazorevy-7": (cb("ak-lazorevy"), "Art Kids"),
 "artkids-mozhayskoe-38": (cb("ak-mozhayskoe"), "Art Kids"),
 "artkids-shabolovka-56": (cb("ak-shabolovka"), "Art Kids"),
 "artkids-shchuseva-5": (cb("ak-shchuseva"), "Art Kids"),
 "artkids-lyubertsy-vesennyaya": (cb("ak-lyubertsy"), "Art Kids"),
 "churochkina-fryazino": (X["157"]["ll"], "Чурочкин"),
 "art-balet-radialnaya": (X["123"]["ll"], "Арт-балет"),
 "mechta-dzerzhinsky-lesnaya": (X["144"]["ll"], "Мечта"),
 "gitarus-solnechnogorsk": (X["151"]["ll"], "Гитарус"),
 "montoto-dzerzhinsky": (cb("montoto"), "Монтото"),
 "monstarz-konstantinova": (cb("ms-konstantinova"), "ArtSpace"),
 "monstarz-severodvinskaya": (cb("ms-severodvinskaya"), "библиотека"),
 "monstarz-beskudnikovsky": (cb("ms-beskudnikovsky"), "Волшебная страна"),
 "monstarz-altufyevskoe": (cb("ms-altufyevskoe"), "библиотека"),
 "monstarz-bratislavskaya": (cb("ms-bratislavskaya"), "библиотека"),
 "monstarz-dmitrovskoe": (cb("ms-dmitrovskoe"), "Monstarz"),
}
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = json.load(open(p)); have = {x["id"] for x in old}
    out = []
    for k, (ll, nm) in PTS.items():
        if not ll: print("нет координат", k); continue
        q = {"id": "cr14-" + k, "lat": ll[0], "lon": ll[1], "radius": 150, "name": nm, "geom": True}
        if q["id"] not in have: out.append(q)
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print("новых запросов", len(out))
