"""Очередь для независимого проверяющего (ChatGPT) — Вадим 10.11: «привлечь GPT как независимого проверяющего».
Пишет gpt/queue.json: сначала места НА КАРТЕ, которые GPT ещё не проверял (самые сомнительные первыми), затем скрытые
(поле hidden), затем повторный круг, с полями карточки. GPT берёт отсюда пачку, проверяет и кладёт отчёт в gpt/reports/<дата>-<n>.json
по формату gpt/README.md. Отчёты разбирает tools/gpt_import.py."""
import json, os, datetime
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
J = lambda p, d: json.load(open(os.path.join(ROOT, p))) if os.path.exists(os.path.join(ROOT, p)) else d
places = J("places.json", {"places": []})["places"]
ver, gpt = J("auto/verified.json", {}), J("auto/gpt-checks.json", {})
FIELDS = ["name", "type", "address", "lat", "lon", "how_to_find", "hours", "price_child", "price_adult", "phone", "url",
          "age_min", "age_max", "cats", "plus", "minus"]
def last(pid):
    d = [v.get("date", "") for v in ver.get(pid, {}).values() if isinstance(v, dict)] + [gpt.get(pid, {}).get("date", "")]
    return max(d) if d else ""
pri = {"food": 0, "kidsroom": 0, "playcenters": 1, "pools": 1, "dance": 2}
# Вадим 13.11: «может дать ему тоже сначала самые сложные проверить?» — сначала те, что GPT ещё не проверял, и среди них
# самые сомнительные (pipeline/doubt.py: нет в Яндексе, точка не на входе, неподтверждённые и пустые поля).
import sys
sys.path.insert(0, os.path.join(ROOT, "pipeline"))
from doubt import doubt_map
# Вадим 13.11 16:16: «Пусть GPT сначала проверит все опубликованные, затем все скрытые». Порядок: 1) на карте, GPT ещё не
# смотрел (самые сомнительные первыми); 2) скрытые (не закрытые), GPT ещё не смотрел; 3) повторный круг — давно не проверенные.
shown = {p["id"] for p in places}
hidden = [p for p in J("places-all.json", {"places": []})["places"] if p["id"] not in shown and p.get("status") != "closed"]
everyone = places + hidden
doubt = doubt_map(everyone, gpt=False)
everyone.sort(key=lambda p: (bool(gpt.get(p["id"])), p["id"] not in shown, -doubt.get(p["id"], (0, []))[0], last(p["id"]),
                             min([pri.get(c, 5) for c in p.get("cats") or []] or [5])))
q = [{"id": p["id"], **{k: p.get(k) for k in FIELDS}, **({} if p["id"] in shown else {"hidden": True})} for p in everyone[:800]]
left_map = sum(1 for p in places if not gpt.get(p["id"])); left_hidden = sum(1 for p in hidden if not gpt.get(p["id"]))
print("GPT ещё не проверял: на карте", left_map, "скрытых", left_hidden)
os.makedirs(os.path.join(ROOT, "gpt", "reports"), exist_ok=True)
json.dump({"date": datetime.date.today().isoformat(), "places": q}, open(os.path.join(ROOT, "gpt", "queue.json"), "w"),
          ensure_ascii=False, indent=1)
print("в очереди", len(q))
