"""Раскрывает короткие ссылки (yandex.ru/maps/-/...) — в конечном адресе есть точные координаты (ll=долгота,широта).
Аргумент: URL через пробел. Пишет auto/raw/resolved.json {короткая: конечная}."""
import json, os, sys, time, urllib.request, urllib.parse, urllib.error
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k): return None

op = urllib.request.build_opener(NoRedirect)
path = "auto/raw/resolved.json"
out = json.load(open(path)) if os.path.exists(path) else {}
for url in sys.argv[1].split():
    cur = url
    for _ in range(5):
        try:
            r = op.open(urllib.request.Request(cur, headers={"User-Agent": UA}), timeout=30)
            break
        except urllib.error.HTTPError as e:
            loc = e.headers.get("Location")
            if not loc: break
            cur = urllib.parse.urljoin(cur, loc)
        except Exception as e:
            print("FAIL", url, e); break
    out[url] = cur
    print(url, "->", cur[:160])
    time.sleep(1)
os.makedirs("auto/raw", exist_ok=True)
json.dump(out, open(path, "w"), ensure_ascii=False, indent=0)
