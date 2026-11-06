"""Обходит сайты мест и вытаскивает фразы про скидки, акции, пробные/бесплатные занятия.
Пишет auto/promo-snippets.json. Это сырьё: дальше его разбирает ИИ и оформляет в акции."""
import datetime, hashlib, html, json, os, re, sys
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse
import urllib.request
import spam  # фильтр казино/букмекеров (pipeline/spam.py)

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
KEY = re.compile(r"акци|скидк|бесплатн|пробн|перв\w* (?:заняти|посещени|урок|визит)|промокод|подар|именинник|"
                 r"дн[её]м рождени\w* скид|−\s?\d+\s?%|-\s?\d+\s?%|\d+\s?% скид|по будням|счастлив\w* час|"
                 r"абонемент|спецпредложени|выгод|кэшб|cashback|sale|promo", re.I)
LINK = re.compile(r"akci|aktsi|action|sale|skidk|promo|special|offer|news|novost|акци|скидк|предложени|пробн|trial|free", re.I)
NOISE = re.compile(r"казино|casino|слот|букмекер|ставк|1win|покердом|винлайн|бонус\w* при пополн|влажност|cookie|персональных данных|политик\w* конфиденц|©|все права", re.I)


def get(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "ru"})
        with urllib.request.urlopen(req, timeout=15) as r:
            if "html" not in r.headers.get("Content-Type", "html"): return None
            raw = r.read(1_500_000)
            enc = r.headers.get_content_charset() or "utf-8"
            return raw.decode(enc, "ignore")
    except Exception:
        return None


def text_blocks(page):
    page = re.sub(r"(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", page)
    page = re.sub(r"(?i)<br\s*/?>|</(p|div|li|h\d|td|section|article|span|a)>", "\n", page)
    page = html.unescape(re.sub(r"<[^>]+>", " ", page))
    for line in page.split("\n"):
        line = re.sub(r"\s+", " ", line).strip()
        if 12 <= len(line) <= 400: yield line


def links(page, base):
    host = urlparse(base).netloc
    for href, label in re.findall(r'(?is)<a[^>]+href="([^"#]+)"[^>]*>(.*?)</a>', page):
        u = urljoin(base, href)
        if urlparse(u).netloc != host: continue
        label = re.sub(r"<[^>]+>", " ", label)
        if LINK.search(href) or LINK.search(label): yield u


def scan(item):
    url = item["url"]
    if not url.startswith("http"): url = "https://" + url
    home = get(url)
    if home is None:
        return {**item, "ok": False}
    pages, seen = [(url, home)], {url}
    for u in links(home, url):
        if u in seen: continue
        seen.add(u)
        p = get(u)
        if p: pages.append((u, p))
        if len(pages) >= 4: break
    if any(spam.is_spam_text(" ".join(text_blocks(p))) for _, p in pages):
        return {**item, "ok": True, "spam": True, "snippets": []}  # сайт взломан — фраз не берём
    snippets = []
    for u, p in pages:
        for t in text_blocks(p):
            if KEY.search(t) and not NOISE.search(t) and not spam.hits(t) and t not in (s["t"] for s in snippets):
                snippets.append({"t": t, "page": u})
            if len(snippets) >= 25: break
    h = hashlib.md5("".join(s["t"] for s in snippets).encode()).hexdigest()[:10]
    return {**item, "ok": True, "hash": h, "snippets": snippets}


def main():
    items = []
    for p in json.load(open("places.json"))["places"]:
        if p.get("url"): items.append({"ref": p["id"], "name": p["name"], "url": p["url"].split(" ")[0].strip(";, ")})
    if os.path.exists("auto/candidates.json"):
        for c in json.load(open("auto/candidates.json"))["candidates"]:
            if c.get("url") and c["cat"] not in ("attraction",):
                items.append({"ref": "osm:" + c["osm"], "name": c["name"], "url": c["url"].split(";")[0].strip()})
    # один сайт — один обход (у сетей много филиалов с одним сайтом)
    by_host = {}
    for it in items:
        by_host.setdefault(urlparse(it["url"] if "//" in it["url"] else "https://" + it["url"]).netloc.lower().removeprefix("www."), it)
    bad = spam.load_domains()
    todo = [it for h, it in by_host.items() if h not in bad]
    old = {}
    if os.path.exists("auto/promo-snippets.json"):
        old = {s["ref"]: s.get("hash") for s in json.load(open("auto/promo-snippets.json"))["sites"]}
    with ThreadPoolExecutor(40) as ex:
        res = list(ex.map(scan, todo))
    for r in res:
        r["new"] = r.get("ok") and bool(r.get("snippets")) and old.get(r["ref"]) != r.get("hash")
    res.sort(key=lambda r: (not r["new"], r["name"]))
    print("новые спам-домены:", spam.add_domains(spam.domain(r["url"]) for r in res if r.get("spam")))
    os.makedirs("auto", exist_ok=True)
    with open("auto/promo-snippets.json", "w") as f:
        json.dump({"version": datetime.date.today().isoformat(), "sites": res}, f, ensure_ascii=False, indent=0)
    ok = sum(r["ok"] for r in res)
    withs = sum(bool(r.get("snippets")) for r in res)
    print(f"Сайтов: {len(res)}, открылось: {ok}, с упоминанием акций: {withs}, новых/изменённых: {sum(r['new'] for r in res)}")


main()
