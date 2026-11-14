"""Робот creative, 14.11 (запуск 1114a): места из выдач Яндекс Карт по 15 районам (Университет дружбы народов … Фрязино,
auto/pages *-cv<N>-1114a*), карточки организаций (*-cc<N>-1114ac*, *-cbo-*-1114a*) и сайты сетей из кэша auto/pages
(artkidscommunity.com — список филиалов и групп по возрасту; monstarz.ru/page2 — расписание филиалов с возрастом групп;
artbalet.ru; risovanie-vo-fryazino.ru). Филиалы, где адрес на сайте и в Яндекс Картах расходится (Monstarz: Б. Марфинская,
Профсоюзная), не добавлены. Возраст — только по источнику. Точки — справка OSM cr14-* (объект OSM места → «объект»;
единственный вход здания по адресу → «вход»; иначе дом по адресу — место скрыто, пока сверка не найдёт вход).
WebFetch не использовался. Запуск: KP_PART=creative python3 tools/add_creative_1114a.py [--dry|deals|verify]"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DT = "2026-11-14"
OBJ = "объект"

AK_SITE = "https://artkidscommunity.com"
AK_PLUS = ("Актёрское мастерство, сценическая речь и импровизация в группах по возрасту: 4–6 лет («Актёрская азбука», 1 час в неделю), "
           "7–9 лет (2 часа), 10–13 и 14–16 лет (3 часа в неделю); без кастингов и отборов; дважды в год ученики играют спектакли "
           "на сцене театра Камбуровой, открытые показы для родителей; при школе есть актёрское агентство; первое занятие бесплатно")
AK_NOTE = "курс для 4–6 лет — 9 500 ₽, для 7–16 лет — 12 900 ₽; первое занятие бесплатно"
AK_SRC = ("сайт artkidscommunity.com (программы «Актёрская азбука» 4–6 лет — 9 500 ₽, 7–9, 10–13, 14–16 лет — 12 900 ₽; "
          "оферта: младшая 4–6, средняя 7–9, старшая 10–13, подростковая 14–16 лет; список филиалов; «Первое занятие бесплатно»)")
MS_SITE = "https://monstarz.ru"
MS_NOTE = "абонемент: 8 занятий в месяц — 7 200 ₽, 4 занятия — 4 800 ₽; пробное занятие — 500 ₽; скидка на второй абонемент — 500 ₽"
MS_SRC = "сайт monstarz.ru (цены, «детские группы с 4-х лет», адреса) и monstarz.ru/page2 (расписание филиала с возрастом групп)"
MS_PHONE = "+7 (926) 188-80-66"


def ms_plus(sched):
    return "Хип-хоп, брейк-данс и K-pop для детей — сеть студий Monstarz Dance работает больше 13 лет, проводит зимние и летние танцевальные сборы. Расписание здесь: " + sched


# id: (название, тип, категории, от, до, метро, адрес, телефон, сайт, как найти, плюс, цена занятия, льготы/абонемент,
#      источник, карточка Яндекса, координаты здания (Яндекс), cat_ages|None)
D = {
 "artkids-narodnogo-opolcheniya": ("Актёрская школа Art Kids Community (Народное Ополчение)", "актёрская школа для детей", "theaterstudio", 4, 16,
    "Народное Ополчение", "Москва, ул. Народного Ополчения, 13", "+7 (916) 744-64-79", AK_SITE, "Этаж: 1",
    AK_PLUS, None, AK_NOTE, AK_SRC, "art_kids_community/232719657005", None),
 "artkids-lazorevy-7": ("Актёрская школа Art Kids Community (Ботанический сад)", "актёрская школа для детей", "theaterstudio", 4, 16,
    "Ботанический сад", "Москва, Лазоревый пр., 7", "+7 (916) 744-64-79", AK_SITE, None,
    AK_PLUS, None, AK_NOTE, AK_SRC, "art_kids_community/239401652252", None),
 "artkids-mozhayskoe-38": ("Актёрская школа Art Kids Community (Можайское шоссе)", "актёрская школа для детей", "theaterstudio", 4, 16,
    "Рабочий Посёлок", "Москва, Можайское ш., 38, корп. 1", "+7 (916) 744-64-79", AK_SITE, None,
    AK_PLUS, None, AK_NOTE, AK_SRC, "art_kids_community/7000555949", None),
 "artkids-shabolovka-56": ("Актёрская школа Art Kids Community (Шаболовка)", "актёрская школа для детей", "theaterstudio", 4, 16,
    "Шаболовская", "Москва, ул. Шаболовка, 56", "+7 (916) 744-64-79", AK_SITE, "Этаж: 2",
    AK_PLUS, None, AK_NOTE, AK_SRC, "art_kids_community/146559607651", None),
 "artkids-shchuseva-5": ("Актёрская школа Art Kids Community (ЗИЛ)", "актёрская школа для детей", "theaterstudio", 4, 16,
    "ЗИЛ", "Москва, ул. Архитектора Щусева, 5, корп. 2", "+7 (916) 744-64-79", AK_SITE, "Этаж: 1\nЗанятия — в студии Gold Dance",
    AK_PLUS, None, AK_NOTE, AK_SRC, "shkola_akterskogo_masterstva_stanislava_bondarenko/119602094623", None),
 "artkids-lyubertsy-vesennyaya": ("Актёрская школа Art Kids Community (Люберцы, Весенняя)", "актёрская школа для детей", "theaterstudio", 4, 16,
    "Некрасовка", "Люберцы, Весенняя ул., 6", "+7 (916) 744-64-79", AK_SITE, None,
    AK_PLUS, None, AK_NOTE, AK_SRC, "art_kids_community/14253178041", None),
 "monstarz-konstantinova": ("Школа танцев Monstarz Dance (ВДНХ, ул. Константинова)", "школа танцев", "dance", 7, 15,
    "ВДНХ", "Москва, ул. Константинова, 11А", MS_PHONE, MS_SITE, "Этаж: 5, фитнес-центр «ArtSpace»",
    ms_plus("пн и ср — хип-хоп 7–10 лет в 18:00, 10–15 лет в 19:00"), 1500, MS_NOTE, MS_SRC, None, None),
 "monstarz-severodvinskaya": ("Школа танцев Monstarz Dance (Медведково, Северодвинская)", "школа танцев", "dance", 4, 10,
    "Медведково", "Москва, Северодвинская ул., 11, корп. 2", MS_PHONE, MS_SITE, "Занятия — в библиотеке",
    ms_plus("пн и чт — брейк-данс 7–10 лет в 18:00, 4–6 лет в 19:00"), 1500, MS_NOTE, MS_SRC, "monstarz_dance/239643913213", None),
 "monstarz-beskudnikovsky": ("Школа танцев Monstarz Dance (Селигерская, Бескудниковский бульвар)", "школа танцев", "dance", 4, 12,
    "Селигерская", "Москва, Бескудниковский бул., 21, корп. 2", MS_PHONE, MS_SITE, "Занятия — в детском центре «Волшебная страна»",
    ms_plus("пн и чт — хип-хоп 4–6 лет в 18:00, 7–12 лет в 19:00"), 1500, MS_NOTE, MS_SRC, None, None),
 "monstarz-altufyevskoe": ("Школа танцев Monstarz Dance (Алтуфьево, Алтуфьевское шоссе)", "школа танцев", "dance", 4, 14,
    "Алтуфьево", "Москва, Алтуфьевское ш., 102Б", MS_PHONE, MS_SITE, "Занятия — в библиотеке",
    ms_plus("вт и чт — K-pop 17:00–18:00, пт — хип-хоп 17:00–19:00, вс — хип-хоп для детей 4–6 лет 12:00–14:00; подростковые группы в сети — 7–14 лет"),
    1500, MS_NOTE, MS_SRC + "; возраст старших групп — «Подростковые 7-14 лет» с главной страницы", "monstarz_dance/38433488316", None),
 "monstarz-bratislavskaya": ("Школа танцев Monstarz Dance (Братиславская)", "школа танцев", "dance", 4, 10,
    "Братиславская", "Москва, Братиславская ул., 19, корп. 1", MS_PHONE, MS_SITE, "Занятия — в библиотеке",
    ms_plus("пн и ср — хип-хоп kids 4–6 лет в 18:00, хип-хоп для начинающих 7–10 лет в 19:00"), 1500, MS_NOTE, MS_SRC, "monstarz_dance/49004910684", None),
 "monstarz-dmitrovskoe": ("Школа танцев Monstarz Dance (Физтех, Дмитровское шоссе)", "школа танцев", "dance", 4, 12,
    "Физтех", "Москва, Дмитровское ш., 124А", MS_PHONE, MS_SITE, None,
    ms_plus("пн и ср — хип-хоп 4–6 лет в 17:00, 7–12 лет в 18:00"), 1500, MS_NOTE, MS_SRC, None, None),
 "churochkina-fryazino": ("Творческая студия Валентины Чурочкиной (Фрязино)", "творческая студия рисования", "drawing", 4, 17,
    "Детская поликлиника (остановка)", "Фрязино, ул. Дудкина, 9", "+7 (905) 567-77-85", "https://risovanie-vo-fryazino.ru", "Этаж: 1\nНапротив школы № 3",
    "Малые группы до 6 человек по возрасту: годовой курс рисования и творчества для 4–5 и 5–6 лет (2 раза в неделю по 45 минут), группы 7+ (2 раза в неделю по 60 минут), скетчинг маркерами для детей от 8 лет; ведут художники с многолетним стажем",
    None, "абонемент на 8 занятий: 4–6 лет — 5 400 ₽, 7+ — 6 400 ₽; скетчинг (4 занятия с материалами) — 3 200 ₽; пробное занятие — 700 ₽",
    "сайт risovanie-vo-fryazino.ru («Годовой курс … для детей 4-5 и 5-6 лет», «7+ Набор в группы», «скетчмаркерами для детей от 8 лет», абонементы 5400 ₽ и 6400 ₽, адрес и телефон) и карточка Яндекс Карт (этаж 1, «Пробное занятие по рисованию — 700 ₽»)",
    "art_studio_valenitny_churochkinoy/118276348311", None),
 "art-balet-radialnaya": ("Школа балета «Арт-Балет» (Царицыно)", "балетная школа", "ballet", 2, 14,
    "Царицыно", "Москва, 6-я Радиальная ул., 3, корп. 6", "+7 (929) 557-75-99", "https://artbalet.ru", "Этаж: 1",
    "Балетные классы для детей 2–14 лет: классический и народно-сценический танец, партерная гимнастика, танец для малышей; «Мама и малыш» — с 1,5 лет; отчётные концерты, конкурсы, летние лагеря и интенсивы; скидка 10% братьям и сёстрам, 7% — неделю до и после дня рождения",
    None, "абонемент на 8 занятий (месяц, 2 раза в неделю) — 10 390 ₽; «Старт» — 12 занятий за 3 месяца, 13 750 ₽; 24 занятия — 24 350 ₽; «Мама и малыш» — 4 занятия 6 200 ₽",
    "сайт artbalet.ru («Балетные классы (с 2 до 14 лет)», «Мама и малыш (с 1,5 лет)», цены абонементов, акции, телефон филиала в Царицыно) и карточка Яндекс Карт (адрес, этаж 1)",
    "art_balet/235460352780", None),
 "montoto-dzerzhinsky": ("Изостудия «Монтото» (Дзержинский)", "изостудия", "drawing", 3, 17,
    "Лесная улица, 13 (остановка)", "Дзержинский, Лесная ул., 6", "+7 (963) 976-29-74", None, "Домофон «Изо-студия»\nЭтаж: 2, кабинет 5",
    "Занятия ИЗО по возрастным группам: малыши 3–4 года, 5–6 лет, 7–11 лет и старшие школьники 12+; творческие мастер-классы — роспись футболок, шоперов, игрушек",
    750, None,
    "карточка Яндекс Карт, раздел «Товары и услуги» («Занятия ИЗО для: Малышей 3-4 года, Младшей группы 5-6 лет, Детей 7-11 лет, Старшие школьники 12+ … 1 ч — 750 ₽»; домофон «Изо-студия», этаж 2, кабинет 5)",
    "montoto/12203855378", None),
 "mechta-dzerzhinsky-lesnaya": ("Творческий центр «Мечта» (Дзержинский)", "творческий центр", "drawing,dance", 4, 17,
    "Угрешская улица, 26 (остановка)", "Дзержинский, Лесная ул., 15А", "+7 (925) 502-17-39", None, None,
    "ИЗО-студия в группах 4–5, 5–6, 6–8 лет и от 8 лет; бальные танцы для детей от 4 лет — турниры и спортивные разряды, партнёра искать не обязательно; студия танца «Мечтатели» от 4 лет — фестивали и выступления на праздниках",
    None, "ИЗО — 8 занятий 5 000 ₽; бальные танцы и студия танца «Мечтатели» — 12 занятий (3 раза в неделю) 5 000 ₽",
    "карточка Яндекс Карт, раздел «Товары и услуги» («ИЗО студия … по возрастным группам: 4-5, 5-6, 6-8 и от 8ми лет — 5000 ₽», «Бальные танцы (дети) … для детей от 4х лет — 5000 ₽», «Студия танца «Мечтатели» … от 4х лет — 5000 ₽»)",
    "dream_artcenter/238543688540", None),
 "gitarus-solnechnogorsk": ("Музыкальная школа «Гитарус» (Солнечногорск)", "музыкальная школа", "music", 6, 17,
    "Налоговая инспекция (остановка)", "Солнечногорск, Красная ул., 60", "+7 (985) 315-85-79", "https://gitarus.com", None,
    "Обучение для детей от 6 лет: акустическая и электрогитара, бас-гитара, укулеле, барабаны (ударная установка), фортепиано; педагоги-музыканты, регулярные концерты",
    None, None,
    "карточка Яндекс Карт, раздел «Товары и услуги» («Обучение игре на акустической гитаре для детей от 6 лет и взрослых», так же барабаны, бас-гитара, укулеле, фортепиано, электрогитара — «для детей от 6 лет»)",
    "gitarus/76767369749", None),
}
PTP = os.path.join(ROOT, "tools", "creative_1114a_points.json")
ENTR = json.load(open(PTP)) if os.path.exists(PTP) else {}
TAGS = {"dance": "спорт и активность, музыка", "ballet": "спорт и активность, музыка", "singing": "музыка",
        "music": "музыка", "theaterstudio": "сказки и театр, творчество", "drawing": "творчество", "ceramics": "творчество"}


def point(pid):
    e = ENTR[pid]
    if e["level"] == OBJ:
        return e["lat"], e["lon"], f'точно (объект: {e["osm"]}), {e["why"]}, 14.11', OBJ
    if e["level"] == "вход":
        return e["lat"], e["lon"], f'точно (вход: {e["osm"]}), OSM вход здания {D[pid][6]} — {e["why"]}, 14.11', "вход"
    return e["lat"], e["lon"], f'точно (дом по адресу {D[pid][6]}, координаты здания — Яндекс Карты); дверь уточнит сверка', "дом"


def row(pid):
    name, typ, cats, a0, a1, met, addr, phone, site, how, plus, price, note, asrc, ya, ca = D[pid]
    lat, lon, acc, lvl = point(pid)
    first = cats.split(",")[0]
    active = any(c in ("dance", "ballet") for c in cats.split(","))
    r = P(pid, name, typ, met, addr, lat, lon, a0, a1, 45, 90, "активно" if active else "спокойно", TAGS[first],
          price, note, None, "да", plus, None, adult=1,
          src=(f"Яндекс Карты: карточка организации yandex.ru/maps/org/{ya} (адрес, этаж, телефон, сайт), 14.11.2026; " if ya else
               "Яндекс Карты: поиск по адресу (координаты здания), 14.11.2026; ") + f"возраст и цены — {asrc}",
          acc=acc, adult_price=None, booking="обязательна", loud="частично" if active or first in ("music", "singing") else "нет",
          sit="нет" if active else "частично", crowd="нет", food="нет", stroller="частично")
    r["Взрослый билет, ₽"] = None
    r["Сайт"] = site
    r["Категории"] = cats
    r["Как найти"] = how
    r["Проверено (дата)"] = DT
    return r


TRIAL = {pid: (f"Первое занятие бесплатно в Art Kids Community ({D[pid][0].split('(')[1].rstrip(')')})",
               "Актёрская школа Art Kids Community для детей 4–16 лет: первое полноценное занятие бесплатно и консультация педагога-актёра после урока",
               AK_SITE) for pid in D if pid.startswith("artkids-")}

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    ROWS = [row(k) for k in D]
    if mode == "deals":
        p = os.path.join(ROOT, "deals.json")
        d = json.load(open(p))
        have = {x["id"] for x in d["deals"]}
        n = 0
        for pid, (t, det, url) in TRIAL.items():
            did = pid + "-trial"
            if did not in have:
                d["deals"].append({"id": did, "place_id": pid, "kind": "trial", "title": t, "details": det, "code": "",
                                   "until": "", "url": url, "checked": DT}); n += 1
        json.dump(d, open(p, "w"), ensure_ascii=False, indent=1)
        print("акций", n); sys.exit()
    if mode == "verify":
        out = {}
        for pid in D:
            r = next(x for x in ROWS if x["id"] == pid)
            f = {"address": r["Адрес"], "type": r["Тип"], "cats": r["Категории"], "age_min": r["Возраст от"],
                 "age_max": r["Возраст до"], "booking": "обязательна", "phone": D[pid][7]}
            if r["Сайт"]: f["url"] = r["Сайт"]
            if r["Как найти"]: f["how"] = r["Как найти"]
            if r["Детский билет, ₽"]: f["price_child"] = r["Детский билет, ₽"]
            if r["Бесплатно до (лет / см)"]: f["free_note"] = r["Бесплатно до (лет / см)"]
            lat, lon, acc, lvl = point(pid)
            if lvl in (OBJ, "вход"):
                f["point"] = {"lat": lat, "lon": lon, "level": lvl, "how": acc}
            out[pid] = {"fields": f, "src": r["Источник"]}
        print(json.dumps(out, ensure_ascii=False, indent=1)); sys.exit()
    pa = json.load(open(os.path.join(ROOT, "places-all.json")))
    PL = {p["id"] for p in (pa["places"] if isinstance(pa, dict) else pa)}
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    bad = [r["id"] for r in ROWS if r["id"] in existing or r["id"] in PL]
    assert not bad, bad
    if mode == "--dry":
        for r in ROWS:
            print(r["id"], "|", r["Адрес"], "|", r["Широта"], r["Долгота"], "|", r["Точность координат"][:90])
        print([k for k in ROWS[0] if k not in hdr]); sys.exit()
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    r0 = ws.max_row + 1
    for n, row_ in enumerate(ROWS):
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=r0 + n, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    print("rows", len(ROWS))
