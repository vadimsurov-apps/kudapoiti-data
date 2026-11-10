"""Приём отчёта ChatGPT из issue/PR (ChatGPT-задача по расписанию не всегда может положить файл в репозиторий).
python3 tools/gpt_intake.py <файл с текстом>  — достаёт JSON отчёта (из ```json …``` или первый {…}) и сохраняет
в gpt/reports/<дата>-<время>.json. Печатает путь или «нет отчёта»."""
import datetime, json, os, re, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
text = open(sys.argv[1], encoding="utf-8").read()
cands = re.findall(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.S) or [text[text.find("{"): text.rfind("}") + 1]]
for c in cands:
    try:
        rep = json.loads(c)
    except Exception:
        continue
    if isinstance(rep, dict) and isinstance(rep.get("places"), list) and rep["places"]:
        rep.setdefault("checker", "ChatGPT")
        name = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H%M%S") + ".json"
        path = os.path.join(ROOT, "gpt", "reports", name)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        json.dump(rep, open(path, "w"), ensure_ascii=False, indent=1)
        print(path); sys.exit(0)
print("нет отчёта"); sys.exit(1)
