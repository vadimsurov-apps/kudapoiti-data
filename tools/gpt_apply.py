"""Автоприменение находок ChatGPT (Вадим 10.11: «если GPT что-то обнаружил и предоставил подтверждение — этого
достаточно, чтобы сделать изменения и не ждать Викторию»).
python3 tools/gpt_apply.py — после tools/gpt_import.py (Action gpt.yml сам запускает оба).
- Расхождение (wrong) со ссылкой-источником -> исправить поле через tools/set_verified.py (src: «GPT: <ссылка>»).
- Совпадение (ok) со ссылкой -> поле считается переподтверждённым (дата в auto/verified.json обновляется).
- status closed + хоть одна ссылка-источник -> место закрыто (closed): уходит с карты и сайта.
- Что нельзя применить механически (часы в непонятном формате, точка дальше 500 м — похоже на другой филиал,
  «как найти» не в нашем формате, детской комнаты нет, переезд без нового адреса) — остаётся в auto/gpt-disputes.json
  открытым: его разбирает сверщик.
Таблицы роботов с замком set_verified пропускает — такие места применятся при следующем запуске."""
import datetime, json, math, os, re, subprocess, sys, tempfile

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
P = lambda *a: os.path.join(ROOT, *a)
J = lambda p, d: json.load(open(P(p))) if os.path.exists(P(p)) else d
sys.path.insert(0, P("tools"))
from xlsx_to_json import parse_hours  # noqa: E402

TODAY = datetime.date.today().isoformat()
HOW_PREFIX = ("Вход:", "Этаж:", "Домофон:", "Шлагбаум:", "Парковка:", "Ориентир:")
DAY = r"(?:пн|вт|ср|чт|пт|сб|вс|ежедневно)"


def norm_hours(v):
    """«Пн–пт 09:00–23:00, сб–вс 11:00–23:00» -> «пн-пт 09:00-23:00; сб-вс 11:00-23:00»; не разбирается -> None."""
    if not isinstance(v, str) or not v.strip():
        return None
    t = v.strip().lower().replace("–", "-").replace("—", "-").replace("ежедневно с ", "ежедневно ")
    t = re.sub(r"\bс\s*(\d{1,2}[:.]\d{2})\s*до\s*(\d{1,2}[:.]\d{2})", r"\1-\2", t)
    t = re.sub(r"(\d{1,2})\.(\d{2})", r"\1:\2", t)
    t = re.sub(r"\s*-\s*", "-", t)
    t = re.sub(r"(\d{1,2}:\d{2})-(\d{1,2}:\d{2})", r"\1-\2", t)
    t = re.sub(r"[,;]\s*(?=" + DAY + ")", "; ", t)
    t = re.sub(r"(" + DAY + r"(?:-" + DAY + r")?)\s*:?\s+(?=\d)", r"\1 ", t)
    t = re.sub(r"\b(\d):(\d{2})", r"0\1:\2", t)
    try:
        mode, _ = parse_hours(t)
    except Exception:
        return None
    return t if mode in ("hours", "always") else None


def money(v):
    """«Средний счёт 1200–1500 ₽» -> 1350 (середина, до 50 ₽); «до 1000 ₽» -> 1000; 1300 -> 1300."""
    if isinstance(v, (int, float)):
        return int(v)
    nums = [int(re.sub(r"\s", "", n)) for n in re.findall(r"\d[\d\s]{2,}", str(v or "")) if re.sub(r"\s", "", n)]
    nums = [n for n in nums if 50 <= n <= 50000]
    if not nums:
        return None
    return int(round(sum(nums[:2]) / len(nums[:2]) / 50) * 50)


def how_ok(v):
    lines = [l.strip() for l in str(v or "").split("\n") if l.strip()]
    lines = [l for l in lines if l.startswith(HOW_PREFIX) and "не подтвержд" not in l.lower() and "уточн" not in l.lower()]
    return "\n".join(lines) or None


def dist(a, b):
    return 6371000 * math.hypot(math.radians(a[0] - b[0]), math.radians(a[1] - b[1]) * math.cos(math.radians(a[0])))


def main():
    disputes, checks = J("auto/gpt-disputes.json", {}), J("auto/gpt-checks.json", {})
    applied = J("auto/gpt-applied.json", {})        # {id: файл отчёта} — ok-поля уже засчитаны
    allp = {p["id"]: p for p in J("places-all.json", {"places": []})["places"]}
    batch, plan = {}, {}
    for pid, c in checks.items():
        p = allp.get(pid)
        if not p or p.get("status") == "closed":
            continue
        d = disputes.get(pid) if not disputes.get(pid, {}).get("resolved") else None
        if d and d.get("applied") and applied.get(pid) == c.get("file"):
            d = None        # уже применено, остаток ждёт сверщика — не перезаписывать таблицы каждый час
        if applied.get(pid) == c.get("file") and not d:
            continue
        food = "food" in (p.get("cats") or [])
        fields, left, srcs = {}, {}, set()
        # совпадения: переподтверждаем текущее значение
        gone = c.get("status") == "closed"          # закрыто — поля не переподтверждаем
        for k in ([] if gone else c.get("ok", [])):
            if k == "address" and p.get("address"): fields["address"] = p["address"]
            elif k == "hours" and p.get("hours"): fields["hours"] = p["hours"]
            elif k == "phone" and p.get("phone"): fields["phone"] = p["phone"]
            elif k == "url" and p.get("url"): fields["url"] = p["url"]
            elif k == "how" and p.get("how_to_find"): fields["how"] = p["how_to_find"]
            elif k == "point" and p.get("lat"):
                fields["point"] = {"lat": p["lat"], "lon": p["lon"], "level": "вход", "how": "совпало с проверкой GPT"}
            elif k == "price":
                if food and p.get("price_adult"): fields["price_adult"] = p["price_adult"]
                elif not food and p.get("price_child") is not None: fields["price_child"] = p["price_child"]
        # расхождения со ссылкой: исправляем
        closed = False
        if d:
            srcs |= {w.get("source") for w in d.get("wrong", {}).values() if w.get("source")}
            srcs |= set(d.get("sources") or [])
            if d.get("status") == "closed" and (srcs or c.get("ok") or c.get("sources")):
                closed = True
            for k, w in (d.get("wrong") or {}).items():
                v, s = w.get("value"), w.get("source")
                if not s or v in (None, "", []):
                    left[k] = w; continue
                if closed:
                    continue
                if k in ("address", "phone", "url") and isinstance(v, str):
                    fields[k] = v.strip()
                elif k == "hours":
                    h = norm_hours(v)
                    if h: fields["hours"] = h
                    else: left[k] = w
                elif k == "point" and isinstance(v, list) and len(v) == 2:
                    if p.get("lat") and dist((p["lat"], p["lon"]), v) > 500:
                        left[k] = {**w, "why": "дальше 500 м — возможно другой филиал"}
                    else:
                        fields["point"] = {"lat": round(float(v[0]), 6), "lon": round(float(v[1]), 6), "level": "вход",
                                           "how": "вход по проверке GPT: " + s}
                elif k == "price":
                    m = money(v)
                    if food and m: fields["price_adult"] = m
                    else: left[k] = w
                elif k == "how":
                    h = how_ok(v)
                    if h: fields["how"] = h
                    else: left[k] = w
                elif k == "age" and isinstance(v, list) and len(v) == 2:
                    # 12.11: сужение возраста само не применяем — прячет место в «Кто идёт». Первый же отчёт Codex дал
                    # музею транспорта «7–18» со страницы льгот: это возраст детского билета, а не «с какого пускают».
                    lo, hi = int(v[0]), int(v[1])
                    if p.get("age_min") is not None and p.get("age_max") is not None and (lo > p["age_min"] or hi < p["age_max"]):
                        left[k] = {**w, "why": "сужает возраст — проверить, что это возраст допуска, а не категория билета"}
                    else:
                        fields["age_min"], fields["age_max"] = lo, hi
                else:
                    left[k] = w        # kidsroom и прочее — смотрит сверщик
        srcs |= set(c.get("sources") or [])
        if not fields and not closed:
            if d and not left and d.get("status") not in ("moved", "not_found"):
                d.update(resolved=True, result="нечего менять")
            continue
        src = "проверка GPT " + (c.get("date") or "") + ": " + "; ".join(sorted(s for s in srcs if s)[:4])
        batch[pid] = {"fields": {} if closed else fields, "src": src, **({"closed": True} if closed else {})}
        plan[pid] = (d, left, closed, c.get("file"))
    if not batch:
        print("GPT: применять нечего"); return
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(batch, f, ensure_ascii=False)
    subprocess.run([sys.executable, P("tools", "set_verified.py"), f.name], check=True)
    ver = J("auto/verified.json", {})
    n_fix = n_closed = n_wait = 0
    for pid, (d, left, closed, fname) in plan.items():
        rec = ver.get(pid, {})
        done = any(isinstance(x, dict) and x.get("date") == TODAY and "GPT" in x.get("src", "") for x in rec.values())
        if not done:
            n_wait += 1; continue                      # таблица под замком робота — в следующий раз
        applied[pid] = fname
        if closed: n_closed += 1
        else: n_fix += 1
        if d:
            if left and not closed:
                d.update(wrong=left, applied=TODAY, result="применено автоматически; осталось для сверщика: " + ", ".join(left))
            else:
                d.update(resolved=True, result=("закрыто" if closed else "применено") + " автоматически (GPT со ссылкой)")
    json.dump(disputes, open(P("auto", "gpt-disputes.json"), "w"), ensure_ascii=False, indent=0, sort_keys=True)
    json.dump(applied, open(P("auto", "gpt-applied.json"), "w"), ensure_ascii=False, indent=0, sort_keys=True)
    print(f"GPT: исправлено/подтверждено мест {n_fix}, закрыто {n_closed}, ждут снятия замка {n_wait}")


if __name__ == "__main__":
    main()
