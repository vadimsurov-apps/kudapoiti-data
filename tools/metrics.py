"""Точность данных (Вадим 10.11: «всегда пиши, какой процент точности у нас сейчас по всем объектам и всей информации»).
Запускает build_all.py после каждой сборки. Выход: auto/metrics.json (сейчас) и auto/metrics-history.json (по дням).

Что считается ПОДТВЕРЖДЁННЫМ (строго, без «вроде верно»):
- точка: на входе или на объекте самого места (вручную по геометке, вход/ворота из OSM, объект OSM с тем же названием).
  «Дом по адресу без входа» и приблизительная — НЕ подтверждены, такие места скрыты с карты;
- адрес, часы, цена: запись в реестре проверок auto/verified.json не старше 30 дней (робот-сверщик, set_verified.py);
- телефон, сайт: реестр/auto/contacts.json не старше 60 дней (сайт — также если сайт места открылся при последнем обходе);
- «Как найти»: заполнено конкретикой и проверено (auto/access-reviewed.json или реестр) не старше 90 дней.
Достоверность информации = подтверждённые поля / все поля карточек на карте (7 полей: точка, адрес, часы, цена,
телефон, сайт, как найти; у кафе цена = средний чек — считается, только если он есть)."""
import datetime, json, os, re
from urllib.parse import urlparse
import openpyxl

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
J = lambda p, d=None: json.load(open(os.path.join(ROOT, p))) if os.path.exists(os.path.join(ROOT, p)) else (d if d is not None else {})
today = datetime.date.today()
ago = lambda n: (today - datetime.timedelta(days=n)).isoformat()


def main():
    allp = J("places-all.json")["places"]
    shown = {p["id"] for p in J("places.json")["places"]}
    ver, contacts, acc = J("auto/verified.json"), J("auto/contacts.json"), J("auto/access-reviewed.json")
    geo, addr = J("auto/geocode-report.json"), J("auto/osm-address.json")
    pages = J("auto/pages/index.json")
    # проверки людьми (бот, кнопка «✅ Всё верно», Вадим 10.11): карточка подтверждена целиком на 30 дней
    human = {}
    for c in J("auto/human-checks.json", []):
        if c.get("ok") and c.get("date", "") >= ago(30):
            human[c["place_id"]] = max(human.get(c["place_id"], ""), c["date"])
    ok_hosts = {urlparse(v.get("url", "")).netloc.replace("www.", "") for v in pages.values() if v.get("ok")}
    acc_txt = {}
    files = [os.path.join(ROOT, "data", "kuda-poiti-mesta.xlsx")] + [os.path.join(ROOT, "data", "parts", f) for f in sorted(os.listdir(os.path.join(ROOT, "data", "parts"))) if f.endswith(".xlsx")]
    for f in files:
        ws = openpyxl.load_workbook(f, read_only=True)["Места"]
        rows = ws.iter_rows(values_only=True); h = list(next(rows)); i = h.index("Точность координат")
        for r in rows:
            if r[0]: acc_txt[r[0]] = str(r[i] or "").lower()

    def point_level(p):
        return p.get("point_level") or "примерно"

    def _old(p):
        t = acc_txt.get(p["id"], "")
        if p["id"] in ver and ver[p["id"]].get("point", {}).get("level") in ("вход", "объект"): return "вход"
        if "вручную" in t or "вход" in t or "ворот" in t or re.search(r"(node|way|relation)/\d+", t): return "вход"
        g = geo.get(p["id"], {})
        if g.get("status") == "high" and g.get("moved_m", 0) <= 300: return "вход"
        a = addr.get(p["id"], {})
        if a.get("method") == "osm-entrance": return "вход"
        return "дом" if p.get("coord_exact") else "примерно"

    def fresh(pid, k, days):
        e = ver.get(pid, {}).get(k)
        return bool(e and e.get("date", "") >= ago(days))

    n_fields = n_ok = full = 0
    per = {k: [0, 0] for k in ("точка до входа", "адрес", "часы", "цена", "телефон", "сайт", "как найти")}
    lv = {"вход": 0, "дом": 0, "примерно": 0}
    closed = 0
    for p in allp:
        if p.get("status") == "closed": closed += 1; continue
        lvl = point_level(p); lv[lvl] += 1
        if p["id"] not in shown: continue
        pid = p["id"]; food = "food" in (p.get("cats") or [])
        c = contacts.get(pid, {})
        host = urlparse(p.get("url") or "").netloc.replace("www.", "")
        h = p.get("how_to_find") or ""
        checks = {
            "точка до входа": lvl == "вход",
            "адрес": fresh(pid, "address", 30),
            "часы": fresh(pid, "hours", 30),
            "телефон": fresh(pid, "phone", 60) or bool(c.get("phone") and c.get("checked", "") >= ago(60)),
            "сайт": fresh(pid, "url", 60) or bool(c.get("url") and c.get("checked", "") >= ago(60)) or (host in ok_hosts),
            "как найти": fresh(pid, "how", 90) or (len(h) > 25 and "точка — вход" not in h.lower()
                                                     and acc.get(pid, {}).get("src") not in (None, "нет данных")
                                                     and acc.get(pid, {}).get("date", "") >= ago(90)),
        }
        if not food or p.get("price_adult"):
            checks["цена"] = fresh(pid, "price_child", 30) or fresh(pid, "price_adult", 30)
        if pid in human:
            checks = {k: True for k in checks}
        for k, v in checks.items():
            per[k][1] += 1; per[k][0] += v
        n_fields += len(checks); n_ok += sum(checks.values())
        full += all(checks.values())
    pct = lambda a, b: round(100 * a / b, 1) if b else 0.0
    total = len(allp) - closed
    m = {"date": today.isoformat(),
         "мест_всего": total, "на_карте": len(shown), "скрыто_неподтверждённых": total - len(shown), "закрыто": closed,
         "точки": {"на_входе_или_объекте": lv["вход"], "только_дом": lv["дом"], "приблизительно": lv["примерно"],
                   "процент_точно_до_входа": pct(lv["вход"], total),
                   # 12.11 Вадим: «прямо на входе в нужный подъезд, точность до метра» — честное деление точек на карте
                   "на_карте_дверь_подтверждена_человеком": sum(1 for p in J("places.json")["places"] if p.get("point_door") == "дверь"),
                   "на_карте_вход_организации_по_Яндексу": sum(1 for p in J("places.json")["places"] if p.get("point_door") == "вход_яндекс"),
                   "на_карте_точка_организации_по_Яндексу": sum(1 for p in J("places.json")["places"] if p.get("point_door") == "точка_яндекс"),
                   "на_карте_вход_здания_из_OSM": sum(1 for p in J("places.json")["places"] if p.get("point_door") == "вход_здания"),
                   "на_карте_объект_OSM_не_дверь": sum(1 for p in J("places.json")["places"] if p.get("point_door") == "объект"),
                   "процент_на_карте_дверь_подтверждена": pct(sum(1 for p in J("places.json")["places"] if p.get("point_door") == "дверь"), len(shown))},
         "достоверность_информации_на_карте_%": pct(n_ok, n_fields),
         "полностью_проверенных_карточек": full, "полностью_проверенных_%": pct(full, len(shown)),
         "по_полям_%": {k: pct(a, b) for k, (a, b) in per.items()},
         "проверено_людьми_за_30_дней": len(human),
         "вторая_проверка_GPT_мест": len(J("auto/gpt-checks.json", {})),
         "споры_GPT_открыто": sum(1 for d in J("auto/gpt-disputes.json", {}).values() if not d.get("resolved")),
         "проверено_людьми_сегодня": {n: sum(1 for c in J("auto/human-checks.json", []) if c.get("date") == today.isoformat() and c.get("by") == n)
                                      for n in sorted({c.get("by") for c in J("auto/human-checks.json", [])})}}
    json.dump(m, open(os.path.join(ROOT, "auto", "metrics.json"), "w"), ensure_ascii=False, indent=1)
    hist = J("auto/metrics-history.json")
    hist[today.isoformat()] = m
    json.dump(hist, open(os.path.join(ROOT, "auto", "metrics-history.json"), "w"), ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps(m, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
