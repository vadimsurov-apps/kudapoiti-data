"""Робот sections 14.11 (00 UTC, 1114a): запросы OSM sec14a-<n> (здания по улице из адреса карточки Яндекса в радиусе от центра
города, объект по названию) → auto/osm-queries.json. python3 tools/sections_1114a_osmq.py"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_batch14 import MET
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ST = {n: (a, b) for n, a, b in MET}
TOWN = {"Балашиха": (55.790, 37.960, 9000), "Реутов": (55.760, 37.857, 4000), "Мытищи": (55.910, 37.736, 7000),
        "Люберцы": (55.676, 37.893, 6000), "Электросталь": (55.784, 38.445, 6000), "Коломна": (55.080, 38.778, 8000),
        "Домодедово": (55.437, 37.766, 9000), "Серпухов": (54.913, 37.416, 7000), "Щёлково": (55.920, 37.997, 7000),
        "Фрязино": (55.959, 38.045, 4000), "Орехово-Зуево": (55.806, 38.962, 6000), "Ликино-Дулёво": (55.708, 38.957, 5000),
        "Раменское": (55.567, 38.230, 7000), "Долгопрудный": (55.938, 37.510, 5000), "Жуковский": (55.597, 38.112, 6000),
        "Ивантеевка": (55.971, 37.921, 4000), "Химки": (55.900, 37.400, 12000), "Котельники": (55.660, 37.860, 4000),
        "Чехов": (55.143, 37.455, 6000), "Красногорск": (55.831, 37.330, 7000), "Подольск": (55.400, 37.540, 12000),
        "д. Островцы": (55.590, 38.000, 5000), "д. Беляниново": (55.935, 37.680, 5000), "Осташковское": (55.940, 37.700, 6000),
        "посёлок Государственного": (55.400, 37.800, 15000), "дачный посёлок Загорянский": (55.935, 37.965, 4000),
        "Москва": None}
STREET = r"(ул\.|улица|просп\.|проспект|ш\.|шоссе|бул\.|б-р|пер\.|пр\.|площадь|наб\.|Набережная|Юбилейный)"
def street_of(addr):
    for part in addr.split(","):
        p = part.strip()
        if re.search(STREET, p):
            w = [x for x in re.split(r"[\s.]+", re.sub(STREET, " ", p)) if len(x) > 2 and not x[0].isdigit()]
            if w: return max(w, key=len)
    return None
def town_of(addr):
    for t in TOWN:
        if t != "Москва" and t in addr: return t
    return None
if __name__ == "__main__":
    C = {c["n"]: c for c in json.load(open(os.path.join(ROOT, "tools/sections_1114a_cands.json")))}
    NS = [int(x) for x in sys.argv[1:]]
    out = []
    for n in NS:
        c = C[n]; a = c["addr"]; t = town_of(a); s = street_of(a)
        nm = re.sub(r"[«»\"]", "", c["name"]).split(" - ")[0]
        if t: lat, lon, r = TOWN[t]
        else:
            st = {"3": "Физтех", "6": "Медведково"}.get(str(n), "Физтех"); lat, lon = ST[st]; r = 4000
        q = {"id": f"sec14a-{n}", "lat": lat, "lon": lon, "radius": r, "name": nm}
        if s: q["street"] = s
        out.append(q); print(n, t, "|", s, "|", nm, "|", a)
    p = os.path.join(ROOT, "auto/osm-queries.json")
    ids = {x["id"] for x in out}
    old = [x for x in json.load(open(p)) if x["id"] not in ids]
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(out))
