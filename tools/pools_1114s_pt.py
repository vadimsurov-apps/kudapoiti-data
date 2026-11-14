"""Робот pools 14.11 (17 UTC): поиск точки для адреса без справки OSM (osm-query не доходит: auto/osm-answers.json ≈ 100 МБ).
1) место базы (все data/parts/*.xlsx + основная таблица) в том же доме с «Точность координат» уровня вход/объект/здание OSM;
2) tools/edu_geo.py — здание OSM по адресу из уже выгруженных справок.  find(addr) → [(lat, lon, точность, id места|None), …]"""
import os, re, glob, sys
import openpyxl
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import edu_geo
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
_R = None
def rows():
    global _R
    if _R is None:
        _R = []
        for f in glob.glob(os.path.join(ROOT, "data/parts/*.xlsx")) + [os.path.join(ROOT, "data/kuda-poiti-mesta.xlsx")]:
            ws = openpyxl.load_workbook(f, read_only=True)["Места"]
            for r in ws.iter_rows(min_row=2, values_only=True):
                if r[0] and r[5]: _R.append((r[0], r[1], r[4] or "", r[5], r[6], r[7] or ""))
    return _R
def key(addr):
    a = addr if re.search(r"Москва|^[А-Я][а-яё-]+,", addr) else "Москва, " + addr
    if not edu_geo.town(a): a = "Москва, " + addr
    return edu_geo.town(a), edu_geo.street(a), edu_geo.house(a)
def find(addr):
    k = key(addr); out = []
    if k[1] and k[2]:
        for pid, name, a, lat, lon, acc in rows():
            if key(a) == k and ("OpenStreetMap" in acc or "вход" in acc or "объект" in acc or "геометк" in acc):
                out.append((lat, lon, acc, pid, name))
    a = addr if edu_geo.town(addr) else "Москва, " + addr
    g = edu_geo.geo(a)
    if g: out.append((g[0], g[1], g[2], None, None))
    return out
if __name__ == "__main__":
    for a in sys.argv[1:]:
        print(a)
        for x in find(a): print("   ", x[0], x[1], x[3], x[4], "|", x[2][:230])
def pois(sub, lat=None, lon=None, r=3000):
    """Именованные объекты OSM из уже выгруженных справок: подстрока названия (+ рядом с точкой)."""
    B, P = edu_geo.index(); s = edu_geo.norm(sub); out = []
    for p in P:
        if s in edu_geo.norm(p["name"]) and (lat is None or edu_geo.dist(p["lat"], p["lon"], lat, lon) <= r): out.append(p)
    return out
def bld(street_sub, hn=None):
    B, P = edu_geo.index(); out = []
    for (st, h), d in B.items():
        if street_sub.lower() in " ".join(st) and (hn is None or h == hn): out += list(d.values())
    return out
