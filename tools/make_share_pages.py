"""Страницы «Поделиться»: p/<id>/index.html для каждого места — с названием и картинкой для превью
в Telegram/WhatsApp. Запускать после перегенерации places.json: python3 tools/make_share_pages.py
Иконки старых мест лежат в p/img (из приложения), новых — копируются из icons/."""
import html, json, os, re, shutil
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)
BASE = "https://vadimsurov-apps.github.io/kudapoiti-data/p/"
tpl = open("p/index.html", encoding="utf-8").read()
places = json.load(open("places.json"))["places"]
ids = set()
for p in places:
    pid = p["id"]; ids.add(pid)
    if os.path.exists(f"icons/{pid}.png"):
        shutil.copy(f"icons/{pid}.png", f"p/img/{pid}.png")
    img = BASE + (f"img/{pid}.png" if os.path.exists(f"p/img/{pid}.png") else "app.png")
    desc = " · ".join(x for x in [p.get("address"), ("м. " + p["metro"]) if p.get("metro") else None, p.get("plus")] if x)
    e = lambda s: html.escape(s or "", quote=True)
    head = (f'<title>{e(p["name"])} — Куда пойти с детьми</title>\n'
            f'<meta property="og:title" content="{e(p["name"])}">\n'
            f'<meta property="og:description" content="{e(desc[:280])}">\n'
            f'<meta property="og:image" content="{img}">\n'
            f'<meta property="og:url" content="{BASE}{pid}/">\n'
            f'<meta name="twitter:card" content="summary">')
    page = re.sub(r"<title>.*?</title>\s*<meta property=\"og:title\"[^>]*>\s*<meta property=\"og:description\"[^>]*>",
                  lambda m: head, tpl, flags=re.S)
    page = page.replace('const id = new URLSearchParams(location.search).get("id") || "";', f'const id = {json.dumps(pid)};')
    os.makedirs(f"p/{pid}", exist_ok=True)
    open(f"p/{pid}/index.html", "w", encoding="utf-8").write(page)
# убрать страницы удалённых мест
for d in os.listdir("p"):
    if os.path.isdir(f"p/{d}") and d != "img" and d not in ids:
        shutil.rmtree(f"p/{d}")
print("страниц:", len(ids))
