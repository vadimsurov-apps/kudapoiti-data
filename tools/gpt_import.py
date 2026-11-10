"""Разбор отчётов независимого проверяющего (ChatGPT) из gpt/reports/*.json — Вадим 10.11.
python3 tools/gpt_import.py            — разобрать новые отчёты
- auto/gpt-checks.json {id: {"date", "ok": [поля], "wrong": {поле: {value, source}}, "status", "file"}}
- auto/gpt-disputes.json — расхождения (wrong / closed / moved): их перепроверяет сверщик по указанному источнику и
  исправляет через set_verified.py, если подтвердилось (GPT тоже может ошибаться — ничего не меняем вслепую).
- Совпадения (ok со ссылкой) — вторая независимая проверка: metrics.py их показывает отдельно."""
import glob, json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
P = lambda *a: os.path.join(ROOT, *a)
J = lambda p, d: json.load(open(P(p))) if os.path.exists(P(p)) else d


def main():
    checks, disputes = J("auto/gpt-checks.json", {}), J("auto/gpt-disputes.json", {})
    done = {c.get("file") for c in checks.values()}
    n_files = n_ok = n_wrong = 0
    for f in sorted(glob.glob(P("gpt", "reports", "*.json"))):
        name = os.path.basename(f)
        if name in done:
            continue
        try:
            rep = json.load(open(f))
        except Exception as e:
            print("не JSON:", name, e); continue
        n_files += 1
        for pl in rep.get("places", []):
            pid = pl.get("id")
            if not pid:
                continue
            ok, wrong = [], {}
            for k, v in (pl.get("fields") or {}).items():
                if not isinstance(v, dict) or not v.get("source"):
                    continue
                if v.get("verdict") == "ok":
                    ok.append(k)
                elif v.get("verdict") == "wrong":
                    wrong[k] = {"value": v.get("value"), "source": v.get("source")}
            sources = sorted({v.get("source") for v in (pl.get("fields") or {}).values()
                              if isinstance(v, dict) and v.get("source")} | set(pl.get("sources") or []))
            checks[pid] = {"date": rep.get("date"), "by": rep.get("checker", "GPT"), "ok": ok, "wrong": wrong,
                           "sources": sources,
                           "status": pl.get("status"), "note": pl.get("note"), "file": name}
            n_ok += len(ok); n_wrong += len(wrong)
            if wrong or pl.get("status") in ("closed", "moved", "not_found"):
                disputes[pid] = {"date": rep.get("date"), "status": pl.get("status"), "wrong": wrong,
                                 "note": pl.get("note"), "sources": sources, "resolved": False}
    json.dump(checks, open(P("auto", "gpt-checks.json"), "w"), ensure_ascii=False, indent=0, sort_keys=True)
    json.dump(disputes, open(P("auto", "gpt-disputes.json"), "w"), ensure_ascii=False, indent=0, sort_keys=True)
    print(f"отчётов разобрано {n_files}; совпадений {n_ok}; расхождений {n_wrong}; "
          f"открытых споров {sum(1 for d in disputes.values() if not d.get('resolved'))}")


if __name__ == "__main__":
    main()
