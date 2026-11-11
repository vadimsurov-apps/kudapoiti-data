"""Пачки для Codex (ChatGPT по подписке Вадима, без оплаты API) — Вадим 11.11: «бесплатный и не менее продуктивный вариант».
python3 tools/codex_slices.py <сколько пачек> <мест в пачке> <папка-вывода> [папка с пачками открытых PR]
→ пишет <папка-вывода>/<имя>.json и печатает имена.
Места берутся из gpt/queue.json по порядку, пропуская те, что уже лежат в пачках последних 2 суток (две пачки никогда
не берут одно место) и проверенные GPT сегодня. Старые пачки (> 3 суток) удаляются."""
import datetime, json, os, sys, time
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
D = os.path.join(ROOT, "gpt", "slices")
os.makedirs(D, exist_ok=True)
k, n, OUT = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
os.makedirs(OUT, exist_ok=True)
now = time.time()
busy = set()
files = [os.path.join(D, f) for f in os.listdir(D)]
if len(sys.argv) > 4 and os.path.isdir(sys.argv[4]):
    files += [os.path.join(sys.argv[4], f) for f in os.listdir(sys.argv[4])]
for p in files:
    if not p.endswith(".json"):
        continue
    age = now - os.path.getmtime(p)
    try:
        ids = [x["id"] for x in json.load(open(p))["places"]]
    except Exception:
        ids = []
    if p.startswith(D) and age > 3 * 86400:
        os.remove(p); continue
    if age < 2 * 86400 or not p.startswith(D):
        busy.update(ids)
checks = json.load(open(os.path.join(ROOT, "auto", "gpt-checks.json"))) if os.path.exists(os.path.join(ROOT, "auto", "gpt-checks.json")) else {}
today = datetime.date.today().isoformat()
queue = [p for p in json.load(open(os.path.join(ROOT, "gpt", "queue.json")))["places"]
         if p["id"] not in busy and checks.get(p["id"], {}).get("date") != today]
stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d-%H%M")
for i in range(k):
    part = queue[i * n:(i + 1) * n]
    if not part:
        break
    name = f"{stamp}-{i}"
    json.dump({"name": name, "date": today, "places": part}, open(os.path.join(OUT, name + ".json"), "w"),
              ensure_ascii=False, indent=1)
    print(name)
