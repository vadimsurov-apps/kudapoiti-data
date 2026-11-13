"""Ночной контроль (Вадим 14.11: «проверять, нет ли ошибок в размещении аватаров в ночное время. Действительно ли цветные все
круглосуточные… и сейчас и в будущем»). Считает по places.json, какие места приложение покажет цветными (открытыми) сейчас по
московскому времени, и пишет auto/night-check.json: сколько цветных, список и «подозрительные» — открыты глубокой ночью
(01:00–06:00), но это не открытая территория и не заведение питания."""
import json, os, datetime
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUTDOOR = {"parks", "estates", "skate", "pumptrack", "sledding", "transport", "tours"}


def open_now(p, now):
    m = p.get("season_months")
    if m and now.month not in m: return False
    if p.get("open_mode") == "always": return True
    w = p.get("open_week")
    if p.get("open_mode") != "hours" or not w or len(w) != 7: return False
    i = now.weekday(); t = now.hour * 60 + now.minute
    s, y = w[i], w[(i + 6) % 7]
    if y and y[1] > 1440 and t < y[1] - 1440: return True
    return bool(s and s[0] <= t < s[1])


def main():
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=3)
    places = json.load(open(os.path.join(ROOT, "places.json")))["places"]
    lit = [p for p in places if open_now(p, now)]
    deep = 1 <= now.hour < 6
    sus = [p for p in lit if deep and not (set(p.get("cats") or []) & (OUTDOOR | {"food"}))]
    row = lambda p: {"id": p["id"], "name": p["name"], "cats": p.get("cats"), "hours": p.get("hours"), "hours_src": p.get("hours_src")}
    out = {"at_msk": now.strftime("%Y-%m-%d %H:%M"), "on_map": len(places), "colored": len(lit),
           "always": sum(1 for p in lit if p.get("open_mode") == "always"),
           "hours_doubt": sum(1 for p in places if p.get("hours_doubt")),
           "suspicious": [row(p) for p in sus], "colored_list": [row(p) for p in lit]}
    json.dump(out, open(os.path.join(ROOT, "auto", "night-check.json"), "w"), ensure_ascii=False, indent=0)
    print(f"{out['at_msk']} МСК: цветных {len(lit)} из {len(places)}, круглосуточных {out['always']}, подозрительных {len(sus)}")


if __name__ == "__main__":
    main()
