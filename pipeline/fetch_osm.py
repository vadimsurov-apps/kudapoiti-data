"""Собирает из OpenStreetMap дворовые площадки и катки Москвы.
Пишет компактный файл auto/osm-moscow.json. Координаты из OSM точные —
это и есть "уточнение местоположения", руками ничего двигать не надо."""
import json, math, sys, time, urllib.request, urllib.parse, datetime

SERVERS = ["https://overpass-api.de/api/interpreter",
           "https://overpass.kumi.systems/api/interpreter",
           "https://maps.mail.ru/osm/tools/overpass/api/interpreter"]

QUERY = """
[out:json][timeout:300];
area["ISO3166-2"="RU-MOW"]->.a;
(
  nwr["leisure"="playground"](area.a);
  nwr["leisure"="ice_rink"](area.a);
  nwr["sport"="ice_skating"](area.a);
);
out center tags;
"""

def fetch():
    data = urllib.parse.urlencode({"data": QUERY}).encode()
    for url in SERVERS:
        for attempt in range(2):
            try:
                req = urllib.request.Request(url, data=data, headers={"User-Agent": "kudapoiti-pipeline/1.0"})
                with urllib.request.urlopen(req, timeout=400) as r:
                    return json.load(r)
            except Exception as e:
                print(f"{url}: {e}", file=sys.stderr); time.sleep(20)
    sys.exit("Overpass недоступен")

def dist(a, b, c, d):
    return math.hypot((a - c) * 111000, (b - d) * 111000 * math.cos(math.radians(a)))

def main():
    raw = fetch()
    curated = json.load(open("places.json"))["places"]
    out, seen = [], []
    for el in raw["elements"]:
        t = el.get("tags", {})
        lat = el.get("lat") or el.get("center", {}).get("lat")
        lon = el.get("lon") or el.get("center", {}).get("lon")
        if lat is None: continue
        if t.get("access") in ("private", "no", "customers"): continue
        kind = "rink" if (t.get("leisure") == "ice_rink" or t.get("sport") == "ice_skating") else "playground"
        # не дублируем места из основной базы (ближе 60 м)
        if any(dist(lat, lon, p["lat"], p["lon"]) < 60 for p in curated): continue
        # схлопываем дубликаты одной площадки (точка + контур)
        if any(k == kind and dist(lat, lon, a, b) < 25 for k, a, b in seen): continue
        seen.append((kind, lat, lon))
        item = {"id": f"osm-{el['type'][0]}{el['id']}", "kind": kind,
                "lat": round(lat, 6), "lon": round(lon, 6)}
        name = t.get("name")
        if name: item["name"] = name
        if t.get("covered") == "yes" or t.get("indoor") == "yes": item["indoor"] = True
        if t.get("seasonal") or kind == "rink": item["season"] = "winter" if kind == "rink" else None
        if item.get("season") is None: item.pop("season", None)
        out.append(item)
    out.sort(key=lambda x: x["id"])
    res = {"version": datetime.date.today().isoformat(), "source": "© OpenStreetMap contributors, ODbL",
           "count": len(out), "places": out}
    json.dump(res, open("auto/osm-moscow.json", "w"), ensure_ascii=False, separators=(",", ":"))
    by = {}
    for x in out: by[x["kind"]] = by.get(x["kind"], 0) + 1
    print("Итого:", len(out), by)

main()
