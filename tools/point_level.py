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
