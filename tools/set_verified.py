"""Сверка карточек: записать ПОДТВЕРЖДЁННЫЕ поля места и отметить в реестре проверок auto/verified.json.
Вадим 10.11: «информация в приложении должна быть достоверной всегда, с точностью 100%» — каждое поле с источником и датой.

python3 tools/set_verified.py batch.json
batch.json: {"<id>": {
    "fields": {                      # только то, что ПОДТВЕРЖДЕНО источником сегодня (значение может совпасть со старым)
        "address": "…", "hours": "…", "price_child": 750, "price_adult": 1250, "free_note": "…", "type": "…",
        "how": "Вход: …\\nЭтаж: …", "parking": "да"|"нет", "booking": "обязательна"|…,
        "point": {"lat": 55.1, "lon": 37.1, "level": "вход"|"объект"|"дом", "how": "OSM node/… / вручную / сайт"},
        "phone": "+7 …", "url": "https://…"
    },
    "empty": ["hours", …],           # источник проверен, данных НЕТ — поле очистить (не выдумывать)
    "src": "сайт alpacainfo.ru; OSM node/…; 2ГИС-сниппет",   # обязательно
    "closed": false                  # true — место закрыто навсегда/переехало без нового адреса: статус closed, с карты убрать
}}
- Пишет в таблицу места (основная или data/parts/<робот>.xlsx; таблицы роботов с замком моложе 75 мин — пропускает).
- phone/url — в auto/contacts.json (их применяет сборка), как set_access.py.
- Реестр auto/verified.json: {id: {поле: {"date", "src"}}} — по нему сборка считает точность (auto/metrics.json).
- Если подтверждены ВСЕ основные поля (point, address, hours, phone, url + цена/чек где применимо) — «Статус данных» =
  проверено, «Проверено (дата)» = сегодня."""
import datetime, json, os, sys
import openpyxl

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
COLS = {"address": "Адрес", "hours": "Часы работы", "price_child": "Детский билет, ₽", "price_adult": "Взрослый билет, ₽",
        "free_note": "Бесплатно до (лет / см)", "type": "Тип", "how": "Как найти", "parking": "Парковка", "booking": "Запись"}
CORE = ("point", "address", "hours", "phone", "url")


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
    today = datetime.date.today().isoformat()
    vpath = os.path.join(ROOT, "auto", "verified.json")
    ver = json.load(open(vpath)) if os.path.exists(vpath) else {}
    cpath = os.path.join(ROOT, "auto", "contacts.json")
    contacts = json.load(open(cpath)) if os.path.exists(cpath) else {}
    tables = [("main", os.path.join(ROOT, "data", "kuda-poiti-mesta.xlsx"))]
    pd = os.path.join(ROOT, "data", "parts")
    tables += [(f[:-5], os.path.join(pd, f)) for f in sorted(os.listdir(pd)) if f.endswith(".xlsx")]
    done, skipped = set(), set()
    for part, path in tables:
        wb = openpyxl.load_workbook(path)
        ws = wb["Места"]
        head = [c.value for c in ws[1]]
        col = {k: head.index(v) for k, v in COLS.items() if v in head}
        changed = False
        for row in ws.iter_rows(min_row=2):
            pid = row[0].value
            if pid not in batch or pid in done:
                continue
            if part != "main" and locked(part):
                skipped.add(pid); continue
            b = batch[pid]
            if not b.get("src"):
                print("нет src — пропущено:", pid); done.add(pid); continue
            f, rec = b.get("fields", {}), ver.setdefault(pid, {})
            if b.get("closed"):
                row[head.index("Статус данных")].value = "closed"
                rec["closed"] = {"date": today, "src": b["src"]}
            for k, v in f.items():
                if k == "point":
                    row[head.index("Широта")].value, row[head.index("Долгота")].value = v["lat"], v["lon"]
                    row[head.index("Точность координат")].value = f"точно ({v.get('level', 'объект')}: {v.get('how', b['src'])}, проверено {today})"
                elif k in col:
                    row[col[k]].value = v
                elif k in ("phone", "url"):
                    e = contacts.setdefault(pid, {}); e[k] = v
                    if k == "url": e["url_override"] = True
                    e.update(src=b["src"], checked=today)
                rec[k] = {"date": today, "src": b["src"], **({"level": v.get("level")} if k == "point" else {})}
            for k in b.get("empty", []):
                if k in col:
                    row[col[k]].value = None
                rec[k] = {"date": today, "src": b["src"], "empty": True}
            fresh = {k for k, v in rec.items() if isinstance(v, dict) and v.get("date", "") >= (datetime.date.today() - datetime.timedelta(days=30)).isoformat()}
            if set(CORE) <= fresh and not b.get("closed"):
                row[head.index("Статус данных")].value = "проверено"
                row[head.index("Проверено (дата)")].value = today
            done.add(pid); changed = True
        if changed:
            wb.save(path)
    json.dump(ver, open(vpath, "w"), ensure_ascii=False, indent=0, sort_keys=True)
    json.dump(contacts, open(cpath, "w"), ensure_ascii=False, indent=0, sort_keys=True)
    print(f"записано {len(done)}, отложено (замок) {len(skipped)}, не найдено {len(set(batch) - done - skipped)}")


if __name__ == "__main__":
    main()
