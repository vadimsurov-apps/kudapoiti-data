"""Входы организаций из Яндекс Карт (Вадим 12.11: «аватарка должна быть прямо на входе в нужный подъезд… точки должны
находить боты: точки входа в заведение, точки расположения внутри больших торговых центров»).
Страница поиска Яндекс Карт отдаёт у каждой организации: coordinates (точка организации), entrances (координаты входов
и направление двери), additionalAddress (этаж), fullAddress. Скрипт ищет каждое место по названию и адресу рядом с нашей
точкой, выбирает ту же организацию (близко + совпадает название) и пишет auto/yandex-entrances.json. Точку применяет сборка.

python3 pipeline/yandex_entrances.py [N]        — очередь: N мест (по умолчанию 120), у которых ещё нет записи/старше 60 дней
python3 pipeline/yandex_entrances.py --probe    — запросы из auto/entrance-probe.json, ответ в auto/entrance-probe-out.json"""
import datetime, json, math, os, random, re, sys, time, urllib.parse, urllib.request

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "auto", "yandex-entrances.json")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
STOP = set("детский детская детское детей для клуб центр студия школа секция кафе ресторан бассейн и в на по the of".split())


def fetch(q, lat, lon):
    u = f"https://yandex.ru/maps/213/moscow/search/{urllib.parse.quote(q)}/?ll={lon}%2C{lat}&z=17"
    try:
        r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA, "Accept-Language": "ru"}), timeout=40)
        return r.read().decode("utf-8", "replace")
    except Exception as e:
        return "ERR " + str(e)[:100]


def orgs(html):
    """Все организации со страницы: словари с title + coordinates (+ entrances, этаж, адрес)."""
    found, seen = [], set()
    blobs = re.findall(r'<script[^>]*type="application/json"[^>]*>(.*?)</script>', html, re.S)

    def walk(x):
        if isinstance(x, dict):
            c = x.get("coordinates")
            if x.get("title") and isinstance(c, list) and len(c) == 2 and all(isinstance(v, (int, float)) for v in c) \
                    and ("fullAddress" in x or "address" in x or "entrances" in x):
                key = (x.get("id") or x.get("title"), round(c[0], 6), round(c[1], 6))
                if key not in seen:
                    seen.add(key)
                    found.append({"id": str(x.get("id") or ""), "title": x.get("title"), "lat": c[1], "lon": c[0],
                                  "address": x.get("fullAddress") or (x.get("address") if isinstance(x.get("address"), str) else None),
                                  "floor": x.get("additionalAddress"), "status": x.get("status"),
                                  "hours": x.get("workingTimeText"),
                                  "phone": next((ph.get("number") for ph in (x.get("phones") or []) if isinstance(ph, dict) and ph.get("number")), None),
                                  "entrances": [[e["coordinates"][1], e["coordinates"][0], round(e.get("azimuth") or 0)]
                                                for e in (x.get("entrances") or []) if isinstance(e, dict) and e.get("coordinates")]})
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    for b in blobs:
        try:
            walk(json.loads(b))
        except Exception:
            pass
    return found


def dist(a, b, c, d):
    return math.hypot((a - c) * 111200, (b - d) * 111200 * math.cos(math.radians(a)))


TR = dict(zip("абвгдезийклмнопрстуфхцыэ", "abvgdeziyklmnoprstufhcye"))
TR.update({"ж": "zh", "ч": "ch", "ш": "sh", "щ": "sch", "ю": "yu", "я": "ya", "ь": "", "ъ": "", "ё": "e"})


def toks(s):
    """Слова названия без уточнения в скобках (там обычно район/ТЦ), латиницей — «Ла Рива» = «La Riva»."""
    s = re.sub(r"\(.*?\)", " ", (s or "").lower().replace("ё", "е"))
    out = set()
    for t in re.findall(r"[a-zа-я0-9]{3,}", s):
        if t in STOP:
            continue
        t = "".join(TR.get(ch, ch) for ch in t).replace("ck", "k").replace("c", "k").replace("y", "i").replace("w", "v")
        out.add(t)
    return out


def pick(place, found):
    """Та же организация: ближе 300 м и общие слова в названии; лучшая — больше общих слов, потом ближе."""
    want = toks(place["name"]); best = None
    for o in found:
        d = dist(place["lat"], place["lon"], o["lat"], o["lon"])
        have = toks(o["title"]); common = want & have
        if d > 300 or not common:
            continue
        # доля совпавших слов — от нашего названия и от названия в Яндексе; хватает 60% с одной из сторон
        share = max(len(common) / max(1, len(want)), len(common) / max(1, len(have)))
        if share < 0.6:
            continue
        score = (share, len(common), -d)
        if not best or score > best[0]:
            best = (score, o, d, sorted(common))
    if not best:
        return None
    o = dict(best[1]); o["dist_m"] = round(best[2]); o["match"] = best[3]; o["name_share"] = round(best[0][0], 2)
    return o


def query(place):
    name = re.sub(r"\(.*?\)", " ", place["name"]).replace("«", "").replace("»", "").strip()
    addr = re.sub(r"\(.*?\)", " ", place.get("address") or "").strip()
    html = fetch(f"{name} {addr}".strip(), place["lat"], place["lon"])
    if html.startswith("ERR"):
        return {"error": html}
    if re.search(r"showcaptcha|SmartCaptcha", html[:30000]):
        return {"error": "captcha"}
    found = orgs(html)
    o = pick(place, found)
    return o or {"none": True, "seen": len(found)}


def main():
    today = datetime.date.today().isoformat()
    if "--probe" in sys.argv:
        res = {}
        for q in json.load(open(os.path.join(ROOT, "auto", "entrance-probe.json"))):
            html = fetch(q["q"], q["lat"], q["lon"])
            res[q["id"]] = {"bytes": len(html), "orgs": orgs(html)[:6]}
        json.dump(res, open(os.path.join(ROOT, "auto", "entrance-probe-out.json"), "w"), ensure_ascii=False, indent=1)
        return
    n = int(next((a for a in sys.argv[1:] if a.isdigit()), 120))
    done = json.load(open(OUT)) if os.path.exists(OUT) else {}
    places = json.load(open(os.path.join(ROOT, "places.json")))["places"]
    old = (datetime.date.today() - datetime.timedelta(days=60)).isoformat()
    todo = [p for p in places if p.get("lat") is not None and p.get("point_door") != "дверь"
            and (p["id"] not in done or done[p["id"]].get("date", "") < old or done[p["id"]].get("error")
                 or done[p["id"]].get("v") != 2)]       # v2 (13.11): плюс часы работы и телефон — старые записи перезапросить
    random.Random(today).shuffle(todo)
    # сначала те, у кого нет записи совсем, потом перезапрос старых
    todo.sort(key=lambda p: p["id"] in done)
    ok = miss = 0
    for p in todo[:n]:
        r = query(p)
        if r.get("error") == "captcha":
            print("капча — останавливаюсь, продолжу в следующий запуск"); break
        r["date"] = today; r["v"] = 2; done[p["id"]] = r
        ok += "lat" in r; miss += "none" in r
        time.sleep(random.uniform(4, 8))
    json.dump(done, open(OUT, "w"), ensure_ascii=False, indent=0, sort_keys=True)
    print(f"найдено {ok}, не найдено {miss}, всего записей {len(done)}, осталось в очереди {max(0, len(todo) - n)}")


if __name__ == "__main__":
    main()
