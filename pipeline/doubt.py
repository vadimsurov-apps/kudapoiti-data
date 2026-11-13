"""Балл сомнительности карточки (Вадим 13.11: «Виктории на проверку сначала самые сомнительные и недостоверные карточки…»,
«может дать ему [GPT] тоже сначала самые сложные проверить?»). Один расчёт для бота проверяющей (pipeline/tg_reports.py)
и очереди GPT (tools/gpt_queue.py). Пути — от корня репозитория (скрипты запускаются оттуда)."""
import json, os, time
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def _load(path, default):
    try:
        return json.load(open(os.path.join(ROOT, path)))
    except Exception:
        return default


def doubt_map(places=None, gpt=True):
    """{id: (балл, [причины])}; чем больше балл — тем раньше проверять. gpt=False — без учёта споров GPT (для его же очереди)."""
    if places is None:
        places = _load("places.json", {"places": []})["places"]
    ver = _load("auto/verified.json", {}); ya = _load("auto/yandex-entrances.json", {})
    disputes = _load("auto/gpt-disputes.json", {}) if gpt else {}
    answers_ = _load("auto/report-answers.json", {})
    reps = _load("auto/reports.json", []); reps = reps if isinstance(reps, list) else reps.get("reports", [])
    unsolved = {r.get("place_id") for r in reps if answers_.get(str(r.get("id")), {}).get("status") == "need_source"}
    ago = lambda d: time.strftime("%Y-%m-%d", time.gmtime(time.time() - d * 86400))
    out = {}
    for p in places:
        pid = p["id"]; score = 0; why = []
        d = disputes.get(pid)
        if d and not d.get("resolved"):
            st = d.get("status")
            score += 8 if st in ("closed", "moved") else 6 if st == "not_found" else 5
            why.append({"closed": "GPT считает, что место закрыто", "moved": "GPT считает, что место переехало",
                        "not_found": "GPT не нашёл подтверждений, что место существует"}.get(st, "GPT нашёл расхождения"))
        door = p.get("point_door")
        if door == "объект": score += 3; why.append("точка не на входе (центр объекта)")
        elif door == "вход_здания": score += 2; why.append("точка на входе здания, не проверено, что это вход места")
        elif door == "точка_яндекс": score += 1
        if ya.get(pid, {}).get("none"): score += 3; why.append("в Яндекс Картах место не найдено")
        v = ver.get(pid, {}); food = "food" in (p.get("cats") or [])
        fields = [("address", "адрес", 30, p.get("address")), ("hours", "часы", 30, p.get("hours")),
                  ("phone", "телефон", 60, p.get("phone")), ("url", "сайт", 60, p.get("url")),
                  ("how", "как найти", 90, p.get("how_to_find"))]
        if not food: fields.append(("price_child", "цена", 30, p.get("price_child") if p.get("price_child") is not None else p.get("price_adult")))
        nocheck = []
        for k, title, days, val in fields:
            e = v.get(k) or (v.get("price_adult") if k == "price_child" else None)
            if not (e and e.get("date", "") >= ago(days)):
                score += 1; nocheck.append(title)
                if val in (None, "", []): score += 1
        if nocheck: why.append("не подтверждено: " + ", ".join(nocheck))
        if p.get("hours_doubt"): score += 4; why.append("часы «круглосуточно» выглядят ошибкой — уточнить настоящие часы")
        if pid in unsolved: score += 2; why.append("есть правка без источника")
        out[pid] = (score, why)
    return out
