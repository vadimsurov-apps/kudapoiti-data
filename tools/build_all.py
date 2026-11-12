"""Сборка всего, что генерируется (запускает GitHub Action build.yml после каждого пуша роботов):
places.json (основная таблица + data/parts/*.xlsx), PNG иконок новых/изменённых SVG, index.json/versions.json,
страницы «Поделиться», каталог иконок. Роботы сами эти файлы НЕ коммитят — только свою таблицу и icons-src/*.svg.
python3 tools/build_all.py [id_изменённых_svg ...]"""
import json, os, subprocess, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(root)
ALL = "places-all.json" if os.path.exists("places-all.json") else "places.json"
old_ids = {p["id"] for p in json.load(open(ALL))["places"]} if os.path.exists(ALL) else set()
old = len(old_ids)
subprocess.run([sys.executable, "tools/xlsx_to_json.py", "data/kuda-poiti-mesta.xlsx", "places.json"], check=True,
               stdout=subprocess.DEVNULL)
places = json.load(open("places-all.json"))["places"]
closed = {l.split(" — ")[0].strip() for l in open("auto/closed.txt") if l.strip() and not l.startswith("#")} \
    if os.path.exists("auto/closed.txt") else set()
gone = old_ids - {p["id"] for p in places}
if gone and gone <= closed:
    print("сняты закрытые места (auto/closed.txt):", " ".join(sorted(gone)))
elif len(places) < old:
    sys.exit(f"мест стало меньше: {old} → {len(places)} — сборка остановлена")
ids = {p["id"] for p in places}
# акции: убрать ссылки на взломанные сайты и спам казино/букмекеров
sys.path.insert(0, "pipeline"); import spam
bad = spam.load_domains(); dj = json.load(open("deals.json"))
keep = [d for d in dj["deals"] if not spam.is_spam_url(d.get("url"), bad) and not spam.is_spam_text(json.dumps(d, ensure_ascii=False))]
if len(keep) != len(dj["deals"]):
    print("СПАМ: убраны акции", [d["id"] for d in dj["deals"] if d not in keep])
    dj["deals"] = keep; json.dump(dj, open("deals.json", "w"), ensure_ascii=False, indent=1)
# иконки: перерисовать изменённые SVG + отрисовать новые места, у которых есть SVG, а PNG ещё нет
bundled = set(json.load(open("tools/bundled_icons.json")))
todo = {a for a in sys.argv[1:] if a in ids}
todo |= {p for p in ids if p not in bundled and os.path.exists(f"icons-src/{p}.svg") and not os.path.exists(f"icons/{p}.png")}
# SVG поменялся с прошлой отрисовки (хэш в icons/svg-hashes.json) — перерисовать, даже если пуш был раньше
import hashlib
hp = "icons/svg-hashes.json"; hashes = json.load(open(hp)) if os.path.exists(hp) else {}
cur = {p: hashlib.sha1(open(f"icons-src/{p}.svg", "rb").read()).hexdigest()[:10]
       for p in ids if os.path.exists(f"icons-src/{p}.svg")}
if hashes:
    # встроенные в приложение: впервые увиденные — только запомнить хэш; перерисованные — отрисовать,
    # приложение (с версии, где удалённая иконка важнее встроенной) покажет новую
    todo |= {p for p, h in cur.items() if (p in hashes or p not in bundled) and hashes.get(p) != h}
if todo:
    subprocess.run([sys.executable, "tools/render_icons.py", *sorted(todo)], check=True)
json.dump(cur, open(hp, "w"), indent=0, sort_keys=True)
subprocess.run([sys.executable, "tools/make_share_pages.py"], check=True)
subprocess.run([sys.executable, "tools/make_catalog.py"], check=True)
no_icon = sorted(p for p in ids if p not in bundled and not os.path.exists(f"icons/{p}.png"))
print(f"мест: {old} → {len(places)}; иконок отрисовано: {len(todo)}; мест без иконки: {len(no_icon)}", no_icon[:20])
# точность данных для отчётов Вадиму (10.11) — auto/metrics.json, auto/metrics-history.json
subprocess.run([sys.executable, "tools/metrics.py"], check=False, stdout=subprocess.DEVNULL)
# независимый проверяющий (ChatGPT, 10.11): разобрать его отчёты и обновить для него очередь
subprocess.run([sys.executable, "tools/gpt_import.py"], check=False, stdout=subprocess.DEVNULL)
subprocess.run([sys.executable, "tools/gpt_queue.py"], check=False, stdout=subprocess.DEVNULL)
subprocess.run([sys.executable, "tools/call_queue.py"], check=False, stdout=subprocess.DEVNULL)   # обзвон для помощницы
subprocess.run([sys.executable, "tools/gpt_rules.py"], check=False, stdout=subprocess.DEVNULL)   # свод правил для GPT (Вадим 11.11)
