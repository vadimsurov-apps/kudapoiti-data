"""Скачивает страницы по списку URL (аргумент — через пробел) в auto/raw/<имя>.html — для разбора."""
import os, re, sys, time, urllib.request
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
os.makedirs("auto/raw", exist_ok=True)
for url in sys.argv[1].split():
    name = re.sub(r"[^a-z0-9]+", "_", url.lower().split("//", 1)[1])[:120]
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "ru"})
        with urllib.request.urlopen(req, timeout=40) as r:
            open(f"auto/raw/{name}.html", "wb").write(r.read())
        print("ok", url)
    except Exception as e:
        print("FAIL", url, e)
    time.sleep(1.5)
