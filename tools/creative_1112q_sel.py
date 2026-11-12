"""Робот creative, 12.11 (1112q): отобранные кандидаты (номер в creative_1112q_cands.json → id места) и запросы OSM crq-<id>."""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SEL = {14: "musicclasses-lipchanskogo", 50: "active-style-zeleny", 54: "zhete-novokosino-gorodetskaya",
       56: "first-dance-academy-reutov", 57: "viartfam-suzdalskaya", 61: "raduga-hor-reutov", 63: "ramos-vocal-reutov",
       70: "canvas-tolmachevsky", 85: "testa-dance-pavlovsky", 49: "dshi-rimsky-korsakov-novogireevo",
       103: "istok-art-lukinskaya", 116: "planeta-vocal-melnikova", 139: "x-temp-saltykovskaya",
       142: "impulse-dance-korolev", 150: "sinergiya-music-balashikha", 156: "dom-khudozhnikov-khimki",
       164: "bely-slon-khimki", 173: "starlight-podolsk"}
if __name__ == "__main__":
    E = json.load(open(os.path.join(ROOT, "tools/creative_1112q_ext.json")))
    p = os.path.join(ROOT, "auto/osm-queries.json")
    q = json.load(open(p))
    have = {x["id"] for x in q}
    for n, pid in SEL.items():
        o = E[str(n)]
        if "crq-" + pid in have: continue
        q.append({"id": "crq-" + pid, "lat": o["ll"][0], "lon": o["ll"][1], "radius": 150, "name": o["name"], "geom": False})
    json.dump(q, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(q))
