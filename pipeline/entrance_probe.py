"""Проба (12.11): отдают ли 2ГИС и Яндекс Карты координаты ВХОДОВ организаций в HTML страницы поиска.
Запросы — auto/entrance-probe.json [{"id","q","lat","lon"}], ответ — auto/entrance-probe-out.json."""
import json, re, urllib.parse, urllib.request
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
def get(u):
    try:
        r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA, "Accept-Language": "ru"}), timeout=40)
        return r.status, r.read().decode("utf-8", "replace")
    except Exception as e:
        return str(e)[:120], ""
out = {}
for q in json.load(open("auto/entrance-probe.json")):
    t = urllib.parse.quote(q["q"]); res = {}
    for name, u in (("2gis", f"https://2gis.ru/moscow/search/{t}"),
                    ("yandex", f"https://yandex.ru/maps/213/moscow/search/{t}/?ll={q['lon']}%2C{q['lat']}&z=17")):
        st, h = get(u)
        res[name] = {"status": st, "bytes": len(h), "captcha": bool(re.search("captcha|showcaptcha|робот", h[:20000], re.I)),
                     "entrances_ctx": [m[:500] for m in re.findall(r'"entrances?"\s*:\s*\[.{0,480}', h)[:4]],
                     "points": re.findall(r"POINT\([0-9. ]+\)", h)[:12],
                     "coords_ctx": [m[:300] for m in re.findall(r'"(?:coordinates|point)"\s*:\s*[\[{].{0,280}', h)[:5]],
                     "floor_ctx": [m[:200] for m in re.findall(r'.{60}(?:"floor|этаж).{0,130}', h)[:4]]}
    out[q["id"]] = res
json.dump(out, open("auto/entrance-probe-out.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps({k: {n: (v["status"], v["bytes"], len(v["entrances_ctx"]), len(v["points"])) for n, v in r.items()} for k, r in out.items()}))
