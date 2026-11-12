"""Уровень точки места (общий для сборки и метрик). Вадим 10.11: «аватарки ставить прямо на вход».
вход — вручную по геометке / вход или ворота / объект OSM самого места; дом — только здание по адресу; примерно — остальное."""
import json, os, re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
_cache = {}


def _j(name):
    if name not in _cache:
        p = os.path.join(ROOT, "auto", name)
        _cache[name] = json.load(open(p)) if os.path.exists(p) else {}
    return _cache[name]


def level(pid, accuracy_text, coord_exact):
    t = (accuracy_text or "").lower()
    v = _j("verified.json").get(pid, {}).get("point", {})
    if v.get("level") in ("вход", "объект"):
        return "вход"
    if "вручную" in t or "вход" in t or "ворот" in t or re.search(r"(node|way|relation)/\d+", t):
        return "вход"
    g = _j("geocode-report.json").get(pid, {})
    if g.get("status") == "high" and g.get("moved_m", 0) <= 300:
        return "вход"
    if _j("osm-address.json").get(pid, {}).get("method") == "osm-entrance":
        return "вход"
    return "дом" if coord_exact else "примерно"


def door(pid, accuracy_text):
    """Насколько точка «на двери» (Вадим 12.11: «аватарка должна быть прямо на входе в нужный подъезд… точность до метра…
    пока не добьёмся 100% — не сможем выйти в App Store»). Честное деление уровня «вход»:
    дверь — человек поставил метку на вход (геометка Вадима/проверяющей) — единственное, что считается «до метра»;
    вход_здания — вход/ворота здания из OSM (дверь есть, но не проверено, что это вход именно этого места);
    объект — точка или центр контура объекта OSM (внутри здания/территории, не дверь)."""
    t = (accuracy_text or "").lower()
    v = _j("verified.json").get(pid, {}).get("point", {})
    how = (str(v.get("how") or "") + " " + str(v.get("src") or "")).lower()
    if "вручную" in t or "вручную" in how or "геомет" in how:
        return "дверь"
    if v.get("level") == "объект":
        return "объект"
    if v.get("level") == "вход" or "вход" in t or "ворот" in t or _j("osm-address.json").get(pid, {}).get("method") == "osm-entrance":
        return "вход_здания"
    return "объект"
