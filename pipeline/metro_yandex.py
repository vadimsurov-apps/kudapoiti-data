"""Сверка выходов метро (metro-exits.json, OSM) с Яндекс Картами (Вадим 13.11: «сверь по Яндекс Картам, возможно
какие-то станции были упущены или перепутаны. Или поставлены не точно»).
Карточка станции в Яндексе отдаёт entrances — координаты входов (без номеров). По каждой станции: запрос «метро <имя>»
у центра наших выходов, берём карточки станций с тем же названием не дальше 1,5 км, собираем их входы.
Пишет auto/metro-exits-yandex.json: по станции — входы Яндекса; сравнение делает pipeline/metro_exits.py (поле ya у выхода)."""
import datetime, json, os, re, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yandex_entrances import fetch, dist
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "auto", "metro-exits-yandex.json")

def norm(s):
    return re.sub(r"[^a-zа-я0-9]+", " ", (s or "").lower().replace("ё", "е")).strip()

def stations(html):
    res, seen = [], set()
    def walk(x):
        if isinstance(x, dict):
            c = x.get("coordinates")
            if x.get("title") and isinstance(c, list) and len(c) == 2 and "transit/stop" in str(x.get("uri") or ""):
                if x.get("id") not in seen:
                    seen.add(x.get("id"))
                    res.append({"id": str(x.get("id")), "title": x["title"], "lat": c[1], "lon": c[0], "address": x.get("address"),
                                "ent": [[e["coordinates"][1], e["coordinates"][0]] for e in (x.get("entrances") or [])
                                        if isinstance(e, dict) and e.get("coordinates")]})
            for v in x.values(): walk(v)
        elif isinstance(x, list):
            for v in x: walk(v)
    for b in re.findall(r'<script[^>]*type="application/json"[^>]*>(.*?)</script>', html, re.S):
        try: walk(json.loads(b))
        except Exception: pass
    return res

def main(limit=400):
    exits = json.load(open(os.path.join(ROOT, "metro-exits.json")))["exits"]
    by = {}
    for e in exits:
        for name in e["station"].split(" / "):
            by.setdefault(name, []).append(e)
    done = json.load(open(OUT)) if os.path.exists(OUT) else {}
    n = fails = 0
    for name, es in sorted(by.items()):
        if name in done and done[name].get("v") == 1:
            continue
        if n >= limit: break
        la = sum(e["lat"] for e in es) / len(es); lo = sum(e["lon"] for e in es) / len(es)
        mcc = "(МЦК)" in name; clean = name.replace(" (МЦК)", "")
        html = fetch(("станция МЦК " if mcc else "метро ") + clean, la, lo)
        if html.startswith("ERR") or "captcha" in html[:6000].lower():
            fails += 1; print("сбой:", name, html[:80])
            if fails >= 4: print("Яндекс не отвечает — остановка"); break
            time.sleep(40); continue
        st = [s for s in stations(html) if norm(s["title"]) == norm(clean) and dist(la, lo, s["lat"], s["lon"]) <= 1500]
        ent = []
        for s in st:
            for p in s["ent"]:
                if not any(dist(p[0], p[1], q[0], q[1]) < 2 for q in ent): ent.append(p)
        done[name] = {"v": 1, "date": datetime.date.today().isoformat(), "found": len(st),
                      "cards": [{"id": s["id"], "lat": s["lat"], "lon": s["lon"], "address": s["address"]} for s in st], "ent": ent}
        n += 1; print(name, "| карточек", len(st), "| входов", len(ent), "| наших", len(es))
        if n % 20 == 0: json.dump(done, open(OUT, "w"), ensure_ascii=False, indent=0)
        time.sleep(5)
    json.dump(done, open(OUT, "w"), ensure_ascii=False, indent=0)
    print("станций сверено:", len(done), "из", len(by))

if __name__ == "__main__":
    main(*[int(a) for a in sys.argv[1:]])
