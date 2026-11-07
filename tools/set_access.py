"""Записать «Как найти» и «Парковка» в таблицу, где лежит место (основная или data/parts/<робот>.xlsx).
Робот «навигатор»: python3 tools/set_access.py access-batch.json
Файл: {"<id>": {"how": "Вход: …\\nЭтаж: …\\nПарковка: …", "parking": "да"|"нет"|null, "src": "сайт/OSM/поиск"}, …}
- how — пишется в «Как найти» целиком (заменяет старое; старое, если в нём было что-то, чего нет в новом, робот
  должен перенести сам);
- parking — в «Парковка» (null — не трогать);
Таблицы роботов, у которых сейчас висит замок auto/lock-<робот> (моложе 75 мин), пропускаются — эти места остаются
на следующий запуск. Обработанные id пишутся в auto/access-reviewed.json {id: {"date", "src"}}."""
import datetime, json, os, sys
import openpyxl

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def locked(part):
    p = os.path.join(ROOT, "auto", f"lock-{part}")
    if not os.path.exists(p):
        return False
    try:
        t = datetime.datetime.fromisoformat(open(p).read().strip().replace("Z", "+00:00"))
        if t.tzinfo is None:
            t = t.replace(tzinfo=datetime.timezone.utc)
        return (datetime.datetime.now(datetime.timezone.utc) - t).total_seconds() < 75 * 60
    except Exception:
        return True


def main():
    batch = json.load(open(sys.argv[1], encoding="utf-8"))
    tables = [("main", os.path.join(ROOT, "data", "kuda-poiti-mesta.xlsx"))]
    pd = os.path.join(ROOT, "data", "parts")
    for f in sorted(os.listdir(pd)):
        if f.endswith(".xlsx"):
            tables.append((f[:-5], os.path.join(pd, f)))
    rev_path = os.path.join(ROOT, "auto", "access-reviewed.json")
    rev = json.load(open(rev_path)) if os.path.exists(rev_path) else {}
    done, skipped = set(), []
    today = datetime.date.today().isoformat()
    for part, path in tables:
        wb = openpyxl.load_workbook(path)
        ws = wb["Места"]
        head = [c.value for c in ws[1]]
        ci, ch, cp = head.index("id"), head.index("Как найти"), head.index("Парковка")
        changed = False
        for row in ws.iter_rows(min_row=2):
            pid = row[ci].value
            if pid not in batch or pid in done:
                continue
            if part != "main" and locked(part):
                skipped.append(pid)
                continue
            b = batch[pid]
            if b.get("how"):
                row[ch].value = b["how"].strip()
            if b.get("parking") in ("да", "нет"):
                row[cp].value = b["parking"]
            done.add(pid)
            rev[pid] = {"date": today, "src": b.get("src", "")}
            changed = True
        if changed:
            wb.save(path)
    for pid in batch:
        if pid not in done and pid not in skipped:
            rev[pid] = {"date": today, "src": "нет данных"}      # не нашли строку — не повторять каждый раз
    json.dump(rev, open(rev_path, "w"), ensure_ascii=False, indent=0, sort_keys=True)
    print(f"записано {len(done)}, отложено (замок робота) {len(skipped)}, не найдено {len(batch) - len(done) - len(skipped)}")


if __name__ == "__main__":
    main()
