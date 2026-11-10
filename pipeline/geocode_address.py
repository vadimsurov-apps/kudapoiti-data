"""Координаты по точному адресу (дом/строение) через Nominatim (OpenStreetMap).
Для мест, которых нет в OSM по названию: точка здания по адресу — обычно 5–30 м до входа.
Пишет auto/address-geocode.json: {id: {lat, lon, house, display, moved_m, status}}.
Nominatim разрешает 1 запрос в секунду — соблюдаем."""
import json, math, os, re, sys, time, urllib.parse, urllib.request

UA = {"User-Agent": "kudapoiti-geocode/1.0 (github.com/vadimsurov-apps/kudapoiti-data)", "Accept-Language": "ru"}
ABBR = [(r"\bул\.", "улица"), (r"\bпр-т\b\.?", "проспект"), (r"\bпер\.", "переулок"), (r"\bш\.", "шоссе"),
        (r"\bб-р\b\.?", "бульвар"), (r"\bпр-д\b\.?", "проезд"), (r"\bнаб\.", "набережная"), (r"\bпл\.", "площадь"),
        (r"\bмкр\.", "микрорайон"), (r"\bд\.\s", "деревня "), (r"\bс\.\s", "село "), (r"\bг\.\s?", ""), (r"\bр\. ?п\.\s", "")]


def dist(a, b, c, d):
    return math.hypot((a - c) * 111320, (b - d) * 111320 * math.cos(math.radians(a)))


def clean(addr):
    a = re.sub(r",?\s*(ТЦ|ТРЦ|ТРК|БЦ|МФК|ЖК|Депо)\s*[«\"].*$", "", addr)       # всё после названия ТЦ
    a = re.sub(r",?\s*\d+\s*этаж.*$", "", a)
    a = re.sub(r"\bвл\.\s*", "", a)
    a = re.sub(r"(\d\w*),\s*стр\.\s*(\w+)", r"\1с\2", a)
    a = re.sub(r"(\d\w*),\s*корп\.\s*(\w+)", r"\1к\2", a)
    a = re.sub(r",\s*(стр|корп)\.\s*", ", ", a)
    a = re.sub(r"(\d)\s*/\s*(\d)", r"\1/\2", a)
    for k, v in ABBR:
        a = re.sub(k, v, a)
    return re.sub(r"\s+", " ", a).strip(" ,")


def query(q):
    url = "https://nominatim.openstreetmap.org/search?" + urllib.parse.urlencode(
        {"q": q, "format": "jsonv2", "limit": 3, "countrycodes": "ru", "addressdetails": 1})
    for _ in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
                return json.load(r)
        except Exception as e:
            print("  nominatim:", e, file=sys.stderr); time.sleep(5)
    return None


def photon(q, lat, lon):
    """Запасной геокодер на данных OSM (komoot Photon) — когда Nominatim не нашёл или ограничил запросы."""
    url = "https://photon.komoot.io/api/?" + urllib.parse.urlencode({"q": q, "limit": 3, "lat": lat, "lon": lon})
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
            feats = json.load(r).get("features", [])
    except Exception as e:
        print("  photon:", e, file=sys.stderr); return []
    out = []
    for f in feats:
        pr = f.get("properties", {}); lo, la = f["geometry"]["coordinates"]
        out.append({"lat": la, "lon": lo, "address": {"house_number": pr.get("housenumber")},
                    "category": "building" if pr.get("osm_key") == "building" else pr.get("osm_key"),
                    "display_name": ", ".join(x for x in [pr.get("street"), pr.get("housenumber"), pr.get("city")] if x),
                    "osm_type": pr.get("osm_type"), "osm_id": pr.get("osm_id"), "src": "photon"})
    return out


def main():
    places = json.load(open("places-all.json" if __import__("os").path.exists("places-all.json") else "places.json"))["places"]
    rep = json.load(open("auto/geocode-report.json")) if os.path.exists("auto/geocode-report.json") else {}
    path = "auto/address-geocode.json"
    old = json.load(open(path)) if os.path.exists(path) else {}
    only = set(sys.argv[1:])
    out = dict(old)
    for i, p in enumerate(places):
        pid = p["id"]
        if only and pid not in only: continue
        if not only and (p.get("coord_exact") or rep.get(pid, {}).get("status") == "high"): continue
        addr = p.get("address") or ""
        if not re.search(r"\d", addr) or p.get("lat") is None: continue
        if not only and pid in old and old[pid].get("addr") == addr and old[pid].get("status") == "house": continue
        q = clean(addr)
        region = "Москва" if dist(p["lat"], p["lon"], 55.7558, 37.6173) < 30000 else "Московская область"
        res = query(f"{q}, {region}") or []
        if not res and region == "Москва":
            res = query(f"{q}, Московская область") or []
        if not any((x.get("address") or {}).get("house_number") for x in res):
            res = res + photon(q, p["lat"], p["lon"])
        best = None
        for x in res:
            lat, lon = float(x["lat"]), float(x["lon"])
            d = dist(lat, lon, p["lat"], p["lon"])
            house = bool(x.get("address", {}).get("house_number")) or x.get("category") == "building"
            if d > (5000 if region == "Москва" else 20000): continue
            if best is None or (house, -d) > (best["house"], -best["moved_m"]):
                best = {"lat": round(lat, 6), "lon": round(lon, 6), "house": house, "moved_m": round(d),
                        "display": x.get("display_name"), "osm": f'{x.get("osm_type")}/{x.get("osm_id")}'}
        r = best or {}
        r["status"] = "house" if best and best["house"] else ("street" if best else "not-found")
        r["addr"] = addr; r["q"] = q
        out[pid] = r
        print(i, pid, r["status"], r.get("moved_m"), q, flush=True)
        if len(out) % 20 == 0:
            json.dump(out, open(path, "w"), ensure_ascii=False, indent=0)
        time.sleep(1.5)
    json.dump(out, open(path, "w"), ensure_ascii=False, indent=0)
    from collections import Counter
    print("Итого:", Counter(v["status"] for v in out.values()))


main()
