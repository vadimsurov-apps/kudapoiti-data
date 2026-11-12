"""Очередь обзвона для помощницы (Вадим 12.11: «помощнице надо давать такие места на проверку, где нужно именно
звонить и уточнять»). Сборка пишет auto/call-queue.json: места НА КАРТЕ с телефоном, у которых роботы уже пробовали
проверить данные по сайту/картам (есть запись в реестре), но часы или цена так и не подтверждены, либо у важных для
семей мест нет сведений о доступной среде. У каждого места — конкретные вопросы, которые надо задать по телефону.
Бот (pipeline/tg_reports.py, кнопка «📞 Обзвон») выдаёт их по одному."""
import datetime, json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
P = lambda *a: os.path.join(ROOT, *a)
ACCESS_CATS = {"museums", "science", "shows", "circus", "animaltheater", "cinema", "pools", "water", "playcenters",
               "trampolines", "amusement", "estates", "inclusive", "early", "montessori"}
SECTION_CATS = {"sport", "martial", "boxing", "wrestling", "sambo", "judo", "karate", "taekwondo", "football", "ballgames",
                "volleyball", "hockey", "figureskating", "gymnastics", "rhythmic", "acrobatics", "racket", "tabletennis",
                "squash", "padel", "badminton", "chess", "dance", "ballet", "singing", "music", "theaterstudio", "drawing",
                "ceramics", "school", "languages", "robotics", "coding", "lego", "kindergarten", "reading", "math", "mentalmath", "early", "montessori", "speech", "lfk", "psych", "inclusive"}


def main():
    places = json.load(open(P("places.json"), encoding="utf-8"))["places"]
    reg = json.load(open(P("auto", "verified.json"), encoding="utf-8")) if os.path.exists(P("auto", "verified.json")) else {}
    fresh = (datetime.date.today() - datetime.timedelta(days=30)).isoformat()
    out = []
    for p in places:
        if not p.get("phone"):
            continue
        r = reg.get(p["id"]) or {}
        if not r:
            continue                      # роботы ещё не проверяли по сайту — сначала они
        ok = lambda k: (r.get(k) or {}).get("date", "") >= fresh
        cats = set(p.get("cats") or [])
        food = "food" in cats
        section = bool(cats & SECTION_CATS)
        q = []
        if not ok("hours"):
            q.append(("hours", "Часы работы по дням недели (будни и выходные)?"))
        if not food and not (ok("price_child") or ok("price_adult")):
            if section:
                q.append(("price", "Сколько стоит занятие или абонемент для ребёнка? Есть ли бесплатное пробное?"))
            else:
                q.append(("price", "Сколько стоит детский и взрослый билет? До какого возраста ребёнку бесплатно? "
                                   "Есть ли льготы многодетным?"))
        if section and p.get("age_min") is None:
            q.append(("age", "С какого возраста берут детей и до какого?"))
        if not q and not (cats & ACCESS_CATS and not p.get("access")):
            continue
        if cats & ACCESS_CATS and not p.get("access"):
            q.append(("access", "Можно ли попасть на инвалидной коляске — есть пандус или лифт? Есть ли доступный туалет? "
                                "Есть ли занятия или льготы для детей с инвалидностью?"))
        if not food and not section and not p.get("booking"):
            q.append(("booking", "Нужно ли записываться заранее или можно просто прийти?"))
        main_q = sum(1 for k, _ in q if k in ("hours", "price", "age"))
        out.append({"id": p["id"], "name": p["name"], "phone": p["phone"], "address": p.get("address"),
                    "type": ", ".join(p.get("type") or []), "questions": [{"key": k, "q": t} for k, t in q],
                    "_rank": (-main_q, -len(q))})
    out.sort(key=lambda x: x.pop("_rank"))
    json.dump({"updated": datetime.date.today().isoformat(), "places": out}, open(P("auto", "call-queue.json"), "w"),
              ensure_ascii=False, indent=0)
    print("Обзвон: мест в очереди", len(out))


if __name__ == "__main__":
    main()
