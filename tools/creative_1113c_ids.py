"""Робот creative, 13.11 (запуск 1113c): номера кандидатов → id мест; справка OSM crt-<id> в auto/osm-queries.json."""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
IDS = {41: "vocalmt-polyanka", 59: "deti-evolyutsii-rossoshansky", 63: "allegro-chertanovskaya",
       75: "artel-cherkizovskaya", 83: "babydance-sevilsky", 85: "lil-ballerine-prokshino", 93: "music-star-moskovsky",
       95: "tuybova-piano-vorontsovskaya", 101: "imena-production-marksistskaya",
       116: "dance-lab-vernadskogo", 145: "testa-dance-domodedovo",
       144: "valeriballet-domodedovo", 161: "podval-dance-shchyolkovo", 163: "katri-dance-shchyolkovo",
       120: "deti-v-balete-starovolynskaya", 68: "guitar-school-1-chertanovskaya"}
if __name__ == "__main__":
    E = json.load(open(os.path.join(ROOT, "tools/creative_1113c_ext.json")))
    pa = json.load(open(os.path.join(ROOT, "places-all.json"))); pa = pa["places"] if isinstance(pa, dict) else pa
    have = {p["id"] for p in pa}
    assert not (set(IDS.values()) & have), set(IDS.values()) & have
    p = os.path.join(ROOT, "auto/osm-queries.json"); Q = json.load(open(p))
    for n, pid in IDS.items():
        lat, lon = E[str(n)]["ll"]
        Q.append({"id": "crt-" + pid, "lat": lat, "lon": lon, "radius": 150, "name": E[str(n)]["name"], "geom": False})
    json.dump(Q, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(IDS))
