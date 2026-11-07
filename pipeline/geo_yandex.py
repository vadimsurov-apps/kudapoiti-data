"""Точные точки мест по Яндексу (07.11, Вадим: «точки почти всегда не там — нужна автоматическая сверхточность,
до подъезда; проверять потом редко»).

Для каждого места:
1) Поиск по организациям Яндекса (API «Поиск по организациям»): ищем название рядом с текущей точкой.
   Принимаем организацию, если название совпадает и она не дальше 1,5 км (адрес с тем же номером дома — плюс).
   Точка организации в Яндексе стоит у её входа — это лучший доступный ориентир.
2) Не нашли — Геокодер Яндекса по адресу (только точность «дом»/exact, не дальше 3 км).
3) Не нашли — оставляем как было, повтор через 30 дней.
Найденное пишется в auto/geo-yandex.json; сборка (tools/xlsx_to_json.py) подставляет точку, если в таблице за это время
координаты не меняли вручную. Перепроверка найденного — раз в 90 дней (места переезжают редко).

Ключи — секреты GitHub YANDEX_ORG_KEY и YANDEX_GEOCODER_KEY. Без ключей скрипт ничего не делает.
python3 pipeline/geo_yandex.py [--limit-org 450] [--limit-geo 900]"""
import json, math, os, re, sys, time, urllib.parse, urllib.request
from datetime import date, datetime, timedelta

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
STATE = os.path.join(ROOT, "auto", "geo-yandex.json")
ORG_KEY = os.environ.get("YANDEX_ORG_KEY", "").strip()
GEO_KEY = os.environ.get("YANDEX_GEOCODER_KEY", "").strip()
GENERIC = {"детский", "детская", "детское", "детские", "центр", "клуб", "студия", "школа", "парк", "музей", "театр",
           "кафе", "ресторан", "бассейн", "секция", "для", "детей", "и", "в", "на", "им", "имени", "москва", "фитнес",
           "спортивный", "спортивная", "развлекательный", "игровой", "игровая", "комната", "семейный", "семейное"}


def dist(a, b):
    R = 6371000
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


def words(s):
    s = (s or "").lower().replace("ё", "е")
    s = re.sub(r"\(.*?\)", " ", s)
    return {w for w in re.findall(r"[a-zа-я0-9]+", s) if len(w) > 1 and w not in GENERIC}


def core_name(name):
    q = re.search(r"[«\"]([^»\"]+)[»\"]", name or "")
    return q.group(1) if q else re.split(r"\s+[—–-]\s+|\(", name or "")[0]


def house(addr):
    m = re.search(r"(?:^|[ ,])(?:д\.?\s*|вл\.?\s*)?(\d+[а-я]?)(?:\s*(?:к|корп\.?)\s*(\d+))?", (addr or "").lower())
    return (m.group(1), m.group(2)) if m else (None, None)


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "kudapoiti-data/1.0", "Referer": "https://vadimsurov-apps.github.io/"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode("utf-8"))


def org_search(p):
    q = core_name(p["name"])
    ll = f'{p["lon"]},{p["lat"]}'
    url = ("https://search-maps.yandex.ru/v1/?" + urllib.parse.urlencode(
        dict(apikey=ORG_KEY, text=q, lang="ru_RU", ll=ll, spn="0.03,0.03", rspn=1, type="biz", results=10)))
    data = get(url)
    want, (h1, k1) = words(q) | words(p["name"]), house(p.get("address"))
    best = None
    for f in data.get("features", []):
        lon, lat = f["geometry"]["coordinates"]
        meta = f["properties"].get("CompanyMetaData", {})
        name, addr = meta.get("name", ""), meta.get("address", "")
        common = want & words(name)
        if not common or len(common) < min(2, len(words(q)) or 1):
            continue
        d = dist((p["lat"], p["lon"]), (lat, lon))
        if d > 1500:
            continue
        h2, k2 = house(addr)
        score = len(common) * 10 + (15 if h1 and h1 == h2 else 0) + (5 if k1 and k1 == k2 else 0) - d / 200
        if best is None or score > best[0]:
            best = (score, lat, lon, name, addr, meta.get("id"))
    return best


def geocode(p):
    addr = p.get("address")
    if not addr or not house(addr)[0]:
        return None
    q = addr if re.search(r"москва|область|г\.|пос|деревн|раменское|химки|балашиха|мытищи|подольск|люберцы|королёв|королев|красногорск|одинцово|зеленоград", addr.lower()) else "Москва, " + addr
    data = get("https://geocode-maps.yandex.ru/1.x/?" + urllib.parse.urlencode(
        dict(apikey=GEO_KEY, geocode=q, format="json", results=1, lang="ru_RU", ll=f'{p["lon"]},{p["lat"]}', spn="0.3,0.3")))
    m = data["response"]["GeoObjectCollection"]["featureMember"]
    if not m:
        return None
    g = m[0]["GeoObject"]
    meta = g["metaDataProperty"]["GeocoderMetaData"]
    if meta.get("precision") not in ("exact", "number"):
        return None
    lon, lat = map(float, g["Point"]["pos"].split())
    if dist((p["lat"], p["lon"]), (lat, lon)) > 3000:
        return None
    return lat, lon, meta.get("text", "")


def main():
    if not ORG_KEY and not GEO_KEY:
        print("Нет ключей YANDEX_ORG_KEY / YANDEX_GEOCODER_KEY — пропуск"); return
    lim_org = int(sys.argv[sys.argv.index("--limit-org") + 1]) if "--limit-org" in sys.argv else 450
    lim_geo = int(sys.argv[sys.argv.index("--limit-geo") + 1]) if "--limit-geo" in sys.argv else 900
    places = json.load(open(os.path.join(ROOT, "places.json"), encoding="utf-8"))["places"]
    tc_path = "auto/table-coords.json" if not globals().get("ROOT") else os.path.join(ROOT, "auto", "table-coords.json")
    if os.path.exists(tc_path):                      # точки из таблиц, без уже применённых уточнений
        tc = json.load(open(tc_path))
        for p in places:
            if p["id"] in tc: p["lat"], p["lon"] = tc[p["id"]]
    state = json.load(open(STATE, encoding="utf-8")) if os.path.exists(STATE) else {}
    today = date.today()

    def due(p):
        e = state.get(p["id"])
        if p.get("lat") is None:
            return False
        if not e:
            return True
        if abs(e.get("src_lat", 0) - p["lat"]) > 1e-6 or abs(e.get("src_lon", 0) - p["lon"]) > 1e-6:
            return e.get("method") is None          # в таблице поменяли точку вручную — найденное не трогаем
        age = (today - date.fromisoformat(e["checked"])).days
        return age > (90 if e.get("method") else 30)

    # сначала неточные, потом остальные; внутри — самые давние
    todo = sorted((p for p in places if due(p)), key=lambda p: (bool(p.get("coord_exact")), p["id"] in state))
    n_org = n_geo = found = 0
    for p in todo:
        if n_org >= lim_org and (n_geo >= lim_geo or not GEO_KEY):
            break
        e = dict(src_lat=p["lat"], src_lon=p["lon"], checked=today.isoformat(), method=None)
        try:
            r = None
            if ORG_KEY and n_org < lim_org:
                n_org += 1
                r = org_search(p)
                time.sleep(0.2)
            if r:
                _, lat, lon, name, addr, oid = r
                e.update(lat=lat, lon=lon, method="yandex-org", matched=name, matched_addr=addr, yandex_id=oid)
            elif GEO_KEY and n_geo < lim_geo:
                n_geo += 1
                g = geocode(p)
                time.sleep(0.15)
                if g:
                    e.update(lat=g[0], lon=g[1], method="yandex-addr", matched_addr=g[2])
        except Exception as ex:          # лимит/сбой — остановиться, продолжим в следующий раз
            print("стоп:", p["id"], ex)
            break
        if e.get("method"):
            found += 1
            e["moved_m"] = round(dist((p["lat"], p["lon"]), (e["lat"], e["lon"])))
        state[p["id"]] = e
    json.dump(state, open(STATE, "w", encoding="utf-8"), ensure_ascii=False, indent=0, sort_keys=True)
    done = sum(1 for e in state.values() if e.get("method"))
    print(f"проверено {n_org} (организации) + {n_geo} (адреса); найдено {found}; всего точных по Яндексу {done} из {len(places)}")


if __name__ == "__main__":
    main()
