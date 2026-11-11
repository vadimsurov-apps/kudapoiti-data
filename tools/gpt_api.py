"""ChatGPT-проверяющий через API OpenAI — полностью автоматически, без чатов и людей (Вадим 11.11: «gpt тоже может создать
армию роботов, которые постоянно проверяют… но он должен знать всё, о чём мы договорились»).
Запуск — Action gpt-api.yml (каждый час, несколько смен). Нужен секрет OPENAI_API_KEY в GitHub (без него ничего не делает).
Каждая смена берёт свою долю gpt/queue.json (позиция % SHARDS == SHARD), по одному месту спрашивает модель с веб-поиском,
передавая ей gpt/RULES.md (наши договорённости) и gpt/README.md (формат отчёта), и кладёт отчёт в gpt/reports/.
Отчёт применяет gpt.yml так же, как отчёты из ChatGPT.
Переменные: OPENAI_MODEL (по умолчанию gpt-5), SHARD, SHARDS, N (мест за запуск, по умолчанию 25)."""
import datetime, json, os, re, sys, time
import urllib.request
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
P = lambda *a: os.path.join(ROOT, *a)


def ask(key, model, instructions, place):
    body = {"model": model, "instructions": instructions, "tools": [{"type": "web_search"}],
            "input": "Проверь это место и верни ТОЛЬКО один JSON-объект места (элемент массива places из формата отчёта), "
                     "без пояснений:\n" + json.dumps(place, ensure_ascii=False)}
    req = urllib.request.Request("https://api.openai.com/v1/responses", data=json.dumps(body).encode(),
                                 headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as r:
        resp = json.load(r)
    text = resp.get("output_text") or "".join(
        c.get("text", "") for o in resp.get("output", []) if o.get("type") == "message"
        for c in o.get("content", []) if c.get("type") in ("output_text", "text"))
    m = re.search(r"\{.*\}", text, re.S)
    obj = json.loads(m.group(0)) if m else None
    usage = resp.get("usage") or {}
    return obj, usage


def main():
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key:
        print("нет секрета OPENAI_API_KEY — пропуск"); return
    model = os.environ.get("OPENAI_MODEL") or "gpt-5"
    shard, shards, n = int(os.environ.get("SHARD", 0)), int(os.environ.get("SHARDS", 1)), int(os.environ.get("N", 25))
    queue = json.load(open(P("gpt", "queue.json")))["places"]
    checks = json.load(open(P("auto", "gpt-checks.json"))) if os.path.exists(P("auto", "gpt-checks.json")) else {}
    today = datetime.date.today().isoformat()
    todo = [p for i, p in enumerate(queue) if i % shards == shard and checks.get(p["id"], {}).get("date") != today][:n]
    instructions = ("Ты — независимый проверяющий данных приложения «Куда пойти с детьми». Работаешь без людей.\n\n"
                    + open(P("gpt", "README.md"), encoding="utf-8").read() + "\n\n"
                    + open(P("gpt", "RULES.md"), encoding="utf-8").read())
    out, tok = [], 0
    for p in todo:
        try:
            obj, usage = ask(key, model, instructions, p)
            tok += usage.get("total_tokens", 0)
            if obj and obj.get("id") == p["id"]:
                out.append(obj)
            else:
                print("не разобран ответ:", p["id"])
        except Exception as e:
            print("ошибка:", p["id"], str(e)[:200]); time.sleep(5)
    if not out:
        print("отчёт пуст"); return
    name = f"{datetime.datetime.utcnow():%Y-%m-%d-%H%M}-api-{shard}.json"
    json.dump({"checker": f"GPT API ({model})", "date": today, "places": out},
              open(P("gpt", "reports", name), "w"), ensure_ascii=False, indent=1)
    print(f"отчёт {name}: мест {len(out)} из {len(todo)}, токенов {tok}")


if __name__ == "__main__":
    main()
