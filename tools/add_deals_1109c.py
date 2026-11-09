"""Робот акций 09.11, 13:26 UTC (тема 4: музеи и театры). Источники — фразы promo-snippets с сайтов мест, кэш auto/pages
(mos.ru о Московской музейной неделе 9–15 ноября, расписание otello.ru по календарю мэрии).
Запуск: python3 tools/add_deals_1109c.py"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
F = os.path.join(ROOT, "deals.json")
TODAY = "2026-11-09"
d = json.load(open(F)); L = d["deals"]
before = len(L)
L[:] = [x for x in L if not (x.get("until") and x["until"] < TODAY)]
removed = before - len(L)

def D(id, pid, kind, title, details, url, until="", code=""):
    x = dict(id=id, place_id=pid, kind=kind, title=title, details=details, code=code, url=url, checked=TODAY)
    if until: x["until"] = until
    return x

MOS = "https://www.mos.ru/news/item/178120073"
OT = "https://otello.ru/nomer/kuda-skhodit-v-moskve-v-noyabre"
MMW = ("Московская музейная неделя: в этот день вход бесплатный. Взрослым нужен электронный билет на «Мосбилете» "
       "(через Mos ID, билеты разбирают быстро), детям до 18 лет бесплатный билет выдают в кассе музея.")
NEW = [
    # Московская музейная неделя 9–15 ноября
    D("borodino-panorama-mmw-1109", "borodino-panorama", "free", "Сегодня, 9 ноября — вход бесплатный", MMW, MOS, "2026-11-09"),
    D("museum-of-moscow-mmw-1110", "museum-of-moscow", "free", "10 ноября — вход бесплатный", MMW, OT, "2026-11-10"),
    D("kuzminki-estate-mmw-1111", "kuzminki-estate-museum", "free", "11 ноября — вход бесплатный", MMW, OT, "2026-11-11"),
    D("lyublino-mmw-1111", "lyublino-park", "free", "11 ноября — усадьба Люблино бесплатно", MMW + " Бесплатен вход в музей «Кузьминки-Люблино» (усадьба), парк открыт всегда.", OT, "2026-11-11"),
    D("scriabin-mmw-1111", "scriabin-museum", "free", "11 ноября — вход бесплатный", MMW, OT, "2026-11-11"),
    D("kuskovo-mmw-1112", "kuskovo", "free", "12 ноября — вход бесплатный", MMW, MOS, "2026-11-12"),
    D("glazunov-mmw-1112", "glazunov-gallery", "free", "12 ноября — вход бесплатный", MMW, OT, "2026-11-12"),
    D("kolomenskoe-mmw-1113", "kolomenskoe", "free", "13 ноября — музеи бесплатно", MMW, OT, "2026-11-13"),
    D("izmaylovo-island-mmw-1113", "izmaylovo-island", "free", "13 ноября — музей бесплатно", MMW, OT, "2026-11-13"),
    D("gmom-mmw-1114", "gmom", "free", "14 ноября — вход бесплатный", MMW, OT, "2026-11-14"),
    # музеи: постоянные льготы со страницы цен
    D("music-museum-kids-free", "music-museum-kids", "free", "Детям до 6 лет и многодетным — бесплатно",
      "Бесплатное посещение: дети до 6 лет включительно; члены многодетных семей (граждане РФ) — дети до 18 лет и их родители. Льготу оформляют в кассе по документу.",
      "https://music-museum.ru"),
    D("prokofiev-museum-free", "prokofiev-museum", "free", "Детям до 6 лет и многодетным — бесплатно",
      "Бесплатное посещение: дети до 6 лет включительно; члены многодетных семей (граждане РФ) — дети до 18 лет и их родители. Льготу оформляют в кассе по документу.",
      "https://music-museum.ru"),
    D("golovanov-museum-free", "golovanov-museum", "free", "Детям до 6 лет и многодетным — бесплатно",
      "Бесплатное посещение: дети до 6 лет включительно; члены многодетных семей (граждане РФ) — дети до 18 лет и их родители. Льготу оформляют в кассе по документу.",
      "https://music-museum.ru"),
    D("zadorozhny-free-under7", "zadorozhny", "free", "Детям до 7 лет — бесплатно",
      "Бесплатно: дети до 7 лет и школьники с действующей картой «Москвёнок». Дети 7–17 лет и многодетные родители — льготный билет (нужен документ).",
      "https://tmuseum.ru/"),
    # очередь promo-snippets
    D("avgust13-dmitrovskoe-bday", "cafe-avgust13-dmitrovskoe", "birthday", "Имениннику −10%",
      "Скидка 10% в день рождения. Условия уточняйте при бронировании.", "https://avgust13.ru/timireazevskaya/"),
    D("shikari-leninsky-bday", "cafe-shikari-leninsky", "birthday", "Имениннику −20% и двойные бонусы",
      "День рождения в «Шикари»: скидка 20% и двойные бонусы по карте гостя. Условия уточняйте в ресторане.", "https://www.shikary.ru/stock/"),
    D("akademiya-chempionov-klenovy-trial", "akademiya-chempionov-klenovy", "trial", "Пробная тренировка бесплатно",
      "Знакомство с тренером и группой, бесплатная пробная тренировка (самбо и единоборства для детей).", "https://champacademy.ru/"),
    D("odingym-tishinskaya-trial", "odingym-tishinskaya", "trial", "Первое занятие бесплатно",
      "Бесплатное пробное занятие по гимнастике — «1 занятие в подарок». Запись через сайт.", "https://odingym.ru/"),
    D("babyboss-trial", "babyboss-kosmodamianskaya", "trial", "Пробное — бесплатно при покупке абонемента",
      "Пробное занятие в акваклубе бесплатно, если после него купить абонемент. Если не понравится — вернут деньги за первое занятие.", "https://babybossclub.ru/"),
    D("rucheek-rechnikov-trial", "rucheek-rechnikov", "trial", "Первое занятие — 0 ₽",
      "Бесплатное пробное занятие в детском бассейне: мягкая адаптация к воде, знакомство с тренером.", "https://ru-cheek.ru/"),
    D("chudo-shkola-umnitsa-2child", "chudo-shkola-umnitsa", "discount", "Второму ребёнку −10%, в день демо −10%",
      "−10% второму и каждому следующему ребёнку; −10% на абонемент на месяц, купленный в день демо-занятия (для новых); многодетным −5%. Скидки не суммируются, только групповые занятия.",
      "https://www.chudo-shkola.ru/kompensacii-i-skidki"),
    D("fsa-yuzhnoportovaya-trial", "fsa-yuzhnoportovaya", "trial", "Первое занятие бесплатно",
      "Оставьте заявку на сайте — первое занятие по борьбе бесплатно.", "https://sasport.ru/"),
    D("progimnastika-kapitsy-trial", "progimnastika-kapitsy", "trial", "Бесплатное пробное занятие",
      "Бесплатное пробное занятие по гимнастике: знакомство с тренером, подбор группы.", "https://pro-gymnastics.ru/"),
    D("gymnastic-lab-pyatnitskoe-trial", "gymnastic-lab-pyatnitskoe", "trial", "Первое занятие бесплатно",
      "Гимнастика, акробатика и чирлидинг для детей — первое занятие бесплатно.", "https://gymnastic-moscow.ru/"),
    D("sambo-vodny-trial", "sambo-vodny-zheleznyaka", "trial", "Бесплатная пробная тренировка",
      "Можно бесплатно попробовать несколько направлений единоборств и выбрать подходящее.", "https://sambo-vodny.ru/"),
    D("sambo-vodny-family", "sambo-vodny-zheleznyaka", "discount", "Семейный абонемент: 2 — −10%, 3 — −20%",
      "При одновременной покупке полных абонементов двум и более членам семьи: 2 абонемента — −10%, 3 абонемента — −20%. Не суммируется с другими акциями.", "https://sambo-vodny.ru/"),
    D("sambo-judo-cao-trial", "sambo-judo-cao-sretenka", "trial", "Бесплатная пробная тренировка",
      "Пробное занятие бесплатно, проходит как обычная тренировка в группе по возрасту; тренер потом расскажет родителям, как прошло.", "https://uni-sport.su/"),
    D("energym-trial", "energym-sokolnichesky", "trial", "Первая тренировка бесплатно",
      "Первое пробное занятие по художественной гимнастике бесплатно, после него тренер подберёт группу.", "https://energym-rg.ru/"),
    D("grand-gym-trial", "grand-gym-kosinskaya", "trial", "Бесплатное пробное занятие",
      "Бесплатное пробное занятие по художественной гимнастике. Пригласите друга — −10% на абонемент в следующем месяце.", "https://sc-grand.ru/stocks"),
    D("capoeira-andropova-trial", "capoeira-andropova", "trial", "Пробное занятие бесплатно",
      "Первое занятие по капоэйре бесплатно.", "https://capoeiraway.ru/"),
    D("sport-dance-sosensky-trial", "sport-dance-sosensky", "trial", "Пробное 0 ₽ по большинству направлений",
      "Для новых клиентов пробное занятие бесплатно по большинству направлений (по некоторым — 700 ₽). Семейные абонементы: двоим −10%, троим и больше −15%.",
      "https://sport-dance-kmk.ru/"),
    D("olimpia-start-trial", "olimpia-start-basmanny", "trial", "Пробная тренировка бесплатно",
      "Бесплатная пробная тренировка по художественной гимнастике.", "https://olimpiastart.ru/company/trial-training/"),
    D("karate-nikolaeva-trial", "karate-nikolaeva-kotelniki", "trial", "Первое занятие бесплатно",
      "Первое занятие по каратэ бесплатно, запись на сайте.", "https://karate-nikolaeva.ru/"),
    D("gavrilenko-gym-trial", "gavrilenko-gym-mikhalkovskaya", "trial", "Первое занятие бесплатно",
      "Набор девочек от 3 лет в группы по 7–10 человек, первое занятие по художественной гимнастике бесплатно.", "https://schoolgavrilenko.ru/"),
]
ids = {x["id"] for x in L}
added = 0
for n in NEW:
    if n["id"] not in ids:
        L.append(n); ids.add(n["id"]); added += 1
d["version"] = TODAY
json.dump(d, open(F, "w"), ensure_ascii=False, indent=1)
print("снято", removed, "добавлено", added)
