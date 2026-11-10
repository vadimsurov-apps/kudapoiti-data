"""Кэш текстов сайтов для роботов: чтобы роботы не ходили на сайты сами (каждый новый сайт требует подтверждения
Вадима), GitHub Action заранее скачивает сайты кандидатов и страницы сетей и кладёт ТЕКСТ в auto/pages/<ключ>.txt.
Источники: auto/candidates.json (у кого есть url) + auto/fetch-queue.txt (любые адреса, по одному в строке).
Для каждого сайта: главная + до 4 внутренних страниц про адреса/филиалы/детское/цены/расписание.
auto/pages/index.json: {ключ: {url, ok, pages, bytes}}. Ключ: osm-id кандидата или домен+путь для очереди."""
import concurrent.futures as cf, html, json, os, re, sys, time, urllib.parse, urllib.request
import spam  # фильтр казино/букмекеров (pipeline/spam.py)

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
KIDS = {"kids_cafe", "dance", "sports_school", "swimming", "kids_center", "playcenter", "trampoline", "escape", "climbing",
        "karting", "lasertag", "horse", "farm", "zoo", "aquarium", "water_park", "theme_park", "museum", "theatre",
        "planetarium", "circus", "library_kids", "bowling", "cinema"}
LINK = re.compile(r"контакт|адрес|филиал|ресторан|кафе|детск|дет[иея]|kids|child|о-нас|about|contact|расписан|цен|price|"
                  r"секци|групп|занят|абонем|пробн|branches|locations|address", re.I)
MAX = 16000


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "ru"})
    with urllib.request.urlopen(req, timeout=20) as r:
        if "html" not in (r.headers.get("Content-Type") or "html"): return ""
        return r.read(1_500_000).decode(r.headers.get_content_charset() or "utf-8", "replace")


def text(page):
    page = re.sub(r"(?is)<(script|style|noscript|svg).*?</\1>", " ", page)
    page = re.sub(r"(?i)<br\s*/?>|</(p|div|li|h\d|tr)>", "\n", page)
    t = html.unescape(re.sub(r"<[^>]+>", " ", page))
    lines = [re.sub(r"\s+", " ", l).strip() for l in t.split("\n")]
    return "\n".join(l for l in lines if len(l) > 2)


def links(page, base):
    host = urllib.parse.urlparse(base).netloc
    out = []
    for href, label in re.findall(r'(?is)<a[^>]+href="([^"#]+)"[^>]*>(.*?)</a>', page):
        u = urllib.parse.urljoin(base, href)
        if urllib.parse.urlparse(u).netloc != host or u in out: continue
        if LINK.search(href) or LINK.search(re.sub(r"<[^>]+>", "", label)): out.append(u)
    return out[:4]


def site(key, url):
    try:
        first = get(url)
    except Exception as e:
        return key, {"url": url, "ok": False, "err": str(e)[:120]}, ""
    parts, done = [f"### {url}\n" + text(first)], 1
    for u in links(first, url):
        try:
            parts.append(f"### {u}\n" + text(get(u))); done += 1
        except Exception:
            pass
        time.sleep(0.5)
    body = "\n\n".join(parts)[:MAX]
    if not spam.trusted(spam.domain(url)) and spam.is_spam_text("\n".join(parts)):
        # сайт взломан: текст не сохраняем, чтобы роботы его не читали
        return key, {"url": url, "ok": False, "spam": True, "tries": 99}, "СПАМ: сайт взломан (казино/букмекеры). Не использовать.\n"
    return key, {"url": url, "ok": True, "pages": done, "bytes": len(body)}, body


def main():
    os.makedirs("auto/pages", exist_ok=True)
    idx_path = "auto/pages/index.json"
    idx = json.load(open(idx_path)) if os.path.exists(idx_path) else {}
    jobs = {}
    c = json.load(open("auto/candidates.json")); c = c.get("candidates", c)
    for x in c:
        if x.get("url") and x.get("cat") in KIDS:
            jobs["osm-" + x["osm"].replace("/", "-")] = x["url"] if x["url"].startswith("http") else "https://" + x["url"]
    if os.path.exists("auto/fetch-queue.txt"):
        for u in open("auto/fetch-queue.txt").read().split():
            if u.startswith("http"):
                jobs[re.sub(r"[^a-z0-9]+", "-", u.lower().split("//", 1)[1])[:90].strip("-")] = u
    bad = spam.load_domains()
    jobs = {k: u for k, u in jobs.items() if spam.domain(u) not in bad}
    force = "--force" in sys.argv
    todo = {k: u for k, u in jobs.items() if force or k not in idx or not idx[k].get("ok") and idx[k].get("tries", 0) < 3}
    print("сайтов в очереди:", len(todo), "из", len(jobs), flush=True)
    with cf.ThreadPoolExecutor(10) as ex:
        for i, (key, meta, body) in enumerate(ex.map(lambda kv: site(*kv), todo.items())):
            meta["tries"] = meta.get("tries") or idx.get(key, {}).get("tries", 0) + (0 if meta["ok"] else 1)
            idx[key] = meta
            if body: open(f"auto/pages/{key}.txt", "w").write(body)
            if i % 50 == 0:
                print(i, key, meta.get("ok"), flush=True)
                json.dump(idx, open(idx_path, "w"), ensure_ascii=False, indent=0)
    json.dump(idx, open(idx_path, "w"), ensure_ascii=False, indent=0)
    print("новые спам-домены:", spam.add_domains(spam.domain(v["url"]) for v in idx.values() if v.get("spam")))
    print("готово:", sum(1 for v in idx.values() if v.get("ok")), "сайтов с текстом")


main()
