"""Очередь для сверщика-смены (Вадим 11.11: «проверить все точки по всем фронтам за 2–4 дня»).
python3 tools/verify_queue.py <смена> <всего смен> map|hidden [N=50]
- map — места НА КАРТЕ: сначала без записи в auto/verified.json, потом с самой старой проверкой основных полей;
- hidden — СКРЫТЫЕ (не closed): сначала не пробованные (auto/confirm-tried.json старше 14 дней или нет);
Места делятся между сменами по хэшу id — две смены никогда не берут одно место. Внутри — сначала кафе, детские
центры, секции, бассейны. Печатает JSON-список {id, name, address, url, cats, last}."""
import datetime, hashlib, json, os, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
J = lambda p, d: json.load(open(os.path.join(ROOT, p))) if os.path.exists(os.path.join(ROOT, p)) else d
CORE = ("point", "address", "hours", "phone", "url", "how", "price_child", "price_adult")
PRIO = ("food", "playcenters", "kidsroom", "pools", "dance", "martial", "football", "gymnastics", "sport", "changing")


def main():
    shard, n, mode = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    limit = int(sys.argv[4]) if len(sys.argv) > 4 else 50
    allp = J("places-all.json", {"places": []})["places"]
    shown = {p["id"] for p in J("places.json", {"places": []})["places"]}
    ver, tried = J("auto/verified.json", {}), J("auto/confirm-tried.json", {})
    old = (datetime.date.today() - datetime.timedelta(days=14)).isoformat()
    pend = set()
    for f in os.listdir(os.path.join(ROOT, "auto", "verify-batches")) if os.path.isdir(os.path.join(ROOT, "auto", "verify-batches")) else []:
        if f.endswith(".json"):
            try: pend |= set(json.load(open(os.path.join(ROOT, "auto", "verify-batches", f))))
            except Exception: pass
    out = []
    for p in allp:
        pid = p["id"]
        if p.get("status") == "closed" or pid in pend:
            continue
        if int(hashlib.md5(pid.encode()).hexdigest(), 16) % n != shard:
            continue
        if mode == "map" and pid not in shown:
            continue
        if mode == "hidden" and (pid in shown or tried.get(pid, "") > old):
            continue
        rec = ver.get(pid, {})
        dates = [rec[k]["date"] for k in CORE if isinstance(rec.get(k), dict) and rec[k].get("date")]
        last = min(dates) if dates and len(dates) >= 5 else ""
        prio = 0 if any(c in PRIO for c in (p.get("cats") or [])) else 1
        out.append((last, prio, pid, p))
    out.sort(key=lambda x: (x[0], x[1]))
    print(json.dumps([{"id": pid, "name": p["name"], "address": p.get("address"), "url": p.get("url"),
                       "cats": p.get("cats"), "last": last or None} for last, _, pid, p in out[:limit]],
                     ensure_ascii=False, indent=0))
    print(f"# в смене {shard}/{n} ({mode}) мест в очереди: {len(out)}", file=sys.stderr)


if __name__ == "__main__":
    main()
