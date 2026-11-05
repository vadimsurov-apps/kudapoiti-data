"""Кандидаты в интересные детские места из OpenStreetMap (Москва + Подмосковье).
Пишет auto/candidates.json — это НЕ попадает в приложение, это список на проверку."""
import json, math, os, re, sys, time, urllib.request, urllib.parse, datetime

SERVERS = ["https://overpass-api.de/api/interpreter",
           "https://overpass.kumi.systems/api/interpreter",
           "https://maps.mail.ru/osm/tools/overpass/api/interpreter"]

# (категория, фильтр OSM) — порядок важен: первая подошедшая категория
RULES = [
  ("zoo", '["tourism"="zoo"]'), ("aquarium", '["tourism"="aquarium"]'),
  ("theme_park", '["tourism"="theme_park"]'), ("water_park", '["leisure"="water_park"]'),
  ("planetarium", '["amenity"="planetarium"]'), ("circus", '["amenity"="circus"]'),
  ("museum", '["tourism"="museum"]'), ("theatre", '["amenity"="theatre"]'),
  ("cinema", '["amenity"="cinema"]'), ("trampoline", '["leisure"="trampoline_park"]'),
  ("playcenter", '["leisure"="indoor_play"]'), ("playcenter", '["leisure"="amusement_arcade"]'),
  ("escape", '["leisure"="escape_game"]'),
  ("climbing", '["sport"="climbing"]["leisure"~"sports_centre|climbing"]'),
  ("farm", '["amenity"="animal_petting"]'),
  ("karting", '["sport"="karting"]'),
  ("horse", '["sport"="equestrian"]["leisure"~"horse_riding|sports_centre"]'),
  ("lasertag", '["sport"~"laser_tag|paintball"]'), ("bowling", '["leisure"="bowling_alley"]'),
  ("library_kids", '["amenity"="library"]["name"~"[Дд]етск"]'),
  ("swimming", '["leisure"="sports_centre"]["sport"~"swimming"]["name"]'),
  ("swimming", '["leisure"="swimming_pool"]["name"]'),
  ("sports_school", '["leisure"="sports_centre"]["name"~"[Дд]етск|ДЮСШ|СШОР|СДЮШОР|[Шш]кола"]'),
  ("dance", '["leisure"="dance"]["name"]'),
  ("kids_center", '["amenity"="community_centre"]["name"~"[Дд]етск|[Тт]ворчеств|[Юю]ност"]'),
  ("kids_center", '["amenity"~"studio|music_school|arts_centre"]["name"~"[Дд]етск|[Шш]кола|[Сс]тудия"]'),
  ("kids_center", '["club"]["name"~"[Дд]етск|[Сс]тудия|[Шш]кола"]'),
  ("kids_cafe", '["amenity"~"restaurant|cafe|fast_food"]["kids_area"~"yes|indoor|outdoor"]'),
  ("kids_cafe", '["amenity"~"restaurant|cafe"]["name"~"[Дд]етск|[Kk]ids|Андерсон|Чайхона|Урюк|Jooie|Ribambelle|Лепим и варим|Додо|Пицца ?[Фф]абрика"]'),
  ("park", '["leisure"="park"]["name"]["wikidata"]'),
  ("attraction", '["tourism"="attraction"]["name"]'),
]
AREAS = '(area["ISO3166-2"="RU-MOW"];area["ISO3166-2"="RU-MOS"];)->.a;'


def query():
    parts = "".join(f"nwr{f}(area.a);" for _, f in RULES)
    return f"[out:json][timeout:900];{AREAS}({parts});out center tags;"


def fetch():
    data = urllib.parse.urlencode({"data": query()}).encode()
    for url in SERVERS:
        for _ in range(2):
            try:
                req = urllib.request.Request(url, data=data, headers={"User-Agent": "kudapoiti-pipeline/1.0"})
                with urllib.request.urlopen(req, timeout=1000) as r:
                    return json.load(r)
            except Exception as e:
                print(f"{url}: {e}", file=sys.stderr)
                time.sleep(30)
    sys.exit("Overpass недоступен")


def match(t, f):
    for k, op, v in re.findall(r'\["([^"]+)"(?:(=|~)"([^"]*)")?\]', f):
        if k not in t: return False
        if op == "=" and t[k] != v: return False
        if op == "~" and not re.search(v, t[k]): return False
    return True


def dist(a, b, c, d):
    return math.hypot((a - c) * 111000, (b - d) * 111000 * math.cos(math.radians(a)))


def main():
    raw = fetch()
    curated = json.load(open("places.json"))["places"]
    out = []
    for el in raw["elements"]:
        t = el.get("tags", {})
        name = t.get("name")
        if not name: continue
        lat = el.get("lat") or el.get("center", {}).get("lat")
        lon = el.get("lon") or el.get("center", {}).get("lon")
        if lat is None or t.get("disused") or t.get("access") == "private": continue
        cat = next((c for c, f in RULES if match(t, f)), "other")
        low = name.lower()
        near = [p for p in curated if dist(lat, lon, p["lat"], p["lon"]) < 250]
        if any(low[:6] in p["name"].lower() or p["name"].lower()[:6] in low for p in near):
            continue  # уже есть в базе
        if any(c["name"] == name and dist(lat, lon, c["lat"], c["lon"]) < 300 for c in out):
            continue  # дубль (точка + контур)
        addr = ", ".join(x for x in [t.get("addr:city"), t.get("addr:street"), t.get("addr:housenumber")] if x)
        out.append({k: v for k, v in {
            "osm": f"{el['type']}/{el['id']}", "cat": cat, "name": name,
            "lat": round(lat, 6), "lon": round(lon, 6), "address": addr or None,
            "url": t.get("website") or t.get("contact:website"), "hours": t.get("opening_hours"),
            "phone": t.get("phone") or t.get("contact:phone"), "wikidata": t.get("wikidata"),
            "desc": t.get("description"), "min_age": t.get("min_age"),
        }.items() if v})
    out.sort(key=lambda x: (x["cat"], x["name"]))
    os.makedirs("auto", exist_ok=True)
    with open("auto/candidates.json", "w") as f:
        json.dump({"version": datetime.date.today().isoformat(), "source": "© OpenStreetMap contributors, ODbL",
                   "count": len(out), "candidates": out}, f, ensure_ascii=False, indent=0)
    by = {}
    for x in out: by[x["cat"]] = by.get(x["cat"], 0) + 1
    print("Итого:", len(out), dict(sorted(by.items(), key=lambda kv: -kv[1])))


main()
