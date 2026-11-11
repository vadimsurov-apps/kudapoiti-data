"""Пачки проверок от параллельных сверщиков (Вадим 11.11: «проверить все точки по всем фронтам за 2–4 дня»).
Сверщики-«смены» не трогают таблицы xlsx (иначе их пуши конфликтуют), а кладут пачку в auto/verify-batches/<смена>-<время>.json
(формат — как у tools/set_verified.py). Action verify-apply.yml по одной применяет их к таблицам и реестру.
Место в таблице робота под замком — остаётся в пачке до следующего раза; не найдено — в auto/verify-batches/missing.json."""
import glob, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import set_verified
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def main():
    files = sorted(glob.glob(os.path.join(ROOT, "auto", "verify-batches", "*.json")))
    files = [f for f in files if not f.endswith("missing.json")]
    total = 0
    miss_path = os.path.join(ROOT, "auto", "verify-batches", "missing.json")
    missing_all = json.load(open(miss_path)) if os.path.exists(miss_path) else {}
    for f in files:
        try:
            batch = json.load(open(f, encoding="utf-8"))
        except Exception as e:
            print("не JSON:", f, e); os.rename(f, f + ".bad"); continue
        tried = batch.pop("_tried", None) or []   # попытки по скрытым местам (не подтвердилось) — в auto/confirm-tried.json
        if tried:
            tp = os.path.join(ROOT, "auto", "confirm-tried.json")
            t = json.load(open(tp)) if os.path.exists(tp) else {}
            import datetime
            t.update({pid: datetime.date.today().isoformat() for pid in tried})
            json.dump(t, open(tp, "w"), ensure_ascii=False, indent=0, sort_keys=True)
        done, skipped, missing = set_verified.apply(batch) if batch else (set(), set(), set())
        total += len(done)
        for m in missing:
            missing_all[m] = batch[m]
        rest = {k: v for k, v in batch.items() if k in skipped}
        if rest:
            json.dump(rest, open(f, "w"), ensure_ascii=False, indent=0)
        else:
            os.remove(f)
    if missing_all:
        json.dump(missing_all, open(miss_path, "w"), ensure_ascii=False, indent=0)
    print(f"пачек: {len(files)}, записано мест: {total}")


if __name__ == "__main__":
    main()
