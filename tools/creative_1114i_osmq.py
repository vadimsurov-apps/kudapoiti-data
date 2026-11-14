"""Робот creative 14.11 (1114i): справка OSM cr14i-* (здания с контурами, входы, объекты рядом с точкой Яндекс Карт)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from creative_1114i_data import LL
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
NM = {"millenium-klary-tsetkin": "Миллениум", "zhete-kuzminki": "Жете", "premiera-arbat": "Дом актёра", "deti-rayka-zhulebino": "Библиотека",
      "artist-frunzenskaya-nab": "Артист", "surik-art-izmaylovo": "Сурик", "risuem-s-radostyu-graivoronovsky": "Рисуем",
      "naydi-sebya-lesnaya": "Найди", "a-golos-zhulebino": "голос", "a-golos-zhukovsky": "голос", "a-golos-ramenskoe": "голос"}
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = json.load(open(p)); have = {x["id"] for x in old}
    out = []
    for k, ll in LL.items():
        if not ll: print("нет координат", k); continue
        q = {"id": "cr14i-" + k, "lat": ll[0], "lon": ll[1], "radius": (400 if k == "naydi-sebya-lesnaya" else 150), "name": NM[k], "geom": True}
        if q["id"] not in have: out.append(q)
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print("новых запросов", len(out))
