"""Точки мест робота rare 13.11 (07 UTC; 1113c): справка OSM (auto/osm-answers.json, rare13d-*/rare13e-*) — объект места
(ледовая арена, ледовый комплекс, ТРЦ, спорткомплекс) или здание по адресу зала (школа, где идут тренировки RusVolley).
python3 tools/rare_1113c_pick.py → tools/rare_1113c_points.json"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
A = json.load(open(os.path.join(ROOT, "auto", "osm-answers.json")))
PT = {}


def find(q, osm, pre="rare13d-"):
    a = A[pre + q]
    return next(p for p in a["pois"] + a["buildings"] + a["outlines"] if p["osm"] == osm)


def obj(q, osm, what, pre="rare13d-"):
    p = find(q, osm, pre)
    return [p["lat"], p["lon"], f"точно (объект: {osm} {what}), OSM"]


def bld(q, osm, addr, pre="rare13d-"):
    p = find(q, osm, pre)
    return [p["lat"], p["lon"], f"точно (OpenStreetMap), здание {osm} по адресу {addr}"]


ICE = "«Ледовая арена» (ice_rink) в ТРК «Б-Класс», Московское ш., 55 к1"
PT["rink-b-class-serpukhov"] = obj("rink-b-class-serpukhov", "node/10648010659", ICE)
PT["fk-aksel-serpukhov"] = obj("fk-aksel-serpukhov", "node/10648010659", ICE)
PT["hockey-star-ostafyevskaya"] = obj("hockey-star-ostafyevskaya", "relation/19583252", "ледовый комплекс «Монтреал», Остафьевская ул., 21/1")
PT["hockey-star-entuziastov-12"] = obj("hockey-star-entuziastov-12", "way/46922224", "ТРЦ «Город Лефортово», ш. Энтузиастов, 12 к2")
PT["volley-rusvolley-yablochkova"] = obj("volley-rusvolley-yablochkova", "way/1237517637", "СК «Апиа Арена», ул. Яблочкова, 7")
PT["volley-rusvolley-kolomenskaya-nab"] = bld("volley-rusvolley-kolomenskaya-nab", "relation/1412051", "Коломенская набережная, 8 (школа)")
PT["volley-rusvolley-samory-mashela"] = bld("volley-rusvolley-samory-mashela", "way/48892159", "улица Саморы Машела, 6 к3 (школа)")
PT["volley-rusvolley-nikulinskaya"] = bld("volley-rusvolley-nikulinskaya", "way/56010902", "Никулинская улица, 5")
PT["volley-rusvolley-800-letiya"] = bld("volley-rusvolley-800-letiya", "way/28678364", "улица 800-летия Москвы, 7А (школа)")
EXTRA = os.path.join(ROOT, "tools", "rare_1113c_points_extra.json")
if os.path.exists(EXTRA):
    for k, (q, osm, kind, what) in json.load(open(EXTRA)).items():
        PT[k] = obj(q, osm, what, "rare13e-") if kind == "obj" else bld(q, osm, what, "rare13e-")
json.dump(PT, open(os.path.join(ROOT, "tools", "rare_1113c_points.json"), "w"), ensure_ascii=False, indent=1)
for k, v in PT.items():
    print(k, v)
