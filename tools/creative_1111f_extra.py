"""Робот creative (третий запуск): акция «пробное бесплатно» и пачка для tools/set_verified.py.
python3 tools/creative_1111f_extra.py deals | verify > batch.json"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

if sys.argv[1] == "deals":
    p = os.path.join(ROOT, "deals.json")
    d = json.load(open(p))
    have = {x["id"] for x in d["deals"]}
    did = "nedushnaya-muzykalka-dubninskaya-trial"
    if did not in have:
        d["deals"].append({"id": did, "place_id": "nedushnaya-muzykalka-dubninskaya", "kind": "trial",
                           "title": "Бесплатное пробное групповое занятие",
                           "details": "Первое знакомство со школой и инструментом: пробное групповое занятие — бесплатно, без обязательств.",
                           "url": "https://nedushnayamusic.ru", "checked": "2026-11-12"})
    json.dump(d, open(p, "w"), ensure_ascii=False, indent=1)
    print("ok")
else:
    from add_creative_1111f import ROWS, CARDS, PTS
    from creative_1111f_data import D
    out = {}
    for k, v in D.items():
        r = next(x for x in ROWS if x["id"] == v[0]); c = CARDS[str(k)]
        f = {"address": r["Адрес"], "type": r["Тип"], "cats": r["Категории"], "age_min": r["Возраст от"], "age_max": r["Возраст до"],
             "booking": "обязательна"}
        if c.get("phone"):
            f["phone"] = c["phone"]
        if r.get("Сайт"):
            f["url"] = r["Сайт"]
        if r.get("Как найти"):
            f["how"] = r["Как найти"]
        if v[0] in PTS and "объект:" in PTS[v[0]][2]:
            lat, lon, acc = PTS[v[0]]
            f["point"] = {"lat": lat, "lon": lon, "level": "объект", "how": acc}
        out[v[0]] = {"fields": f, "src": r["Источник"]}
    print(json.dumps(out, ensure_ascii=False, indent=1))
