"""Робот creative, 13.11 (запуск 1113h): места из выдач Яндекс Карт по 15 районам (Тютчевская … Ивантеевка, 7 тем,
auto/pages *-cv<N>-1113h*), карточки организаций (*-cc<N>-1113h*: рубрика, адрес, этаж/вход, телефон, сайт, услуги с
возрастом групп) и сайты мест из кэша auto/pages. Возраст — только по источнику; «с N лет» без верхней границы → до 17.
Точки — справка OSM crs-* (объект OSM места → «объект»; иначе дом строго по адресу — место скрыто, пока сверка не найдёт вход).
WebFetch не использовался. Запуск: KP_PART=creative python3 tools/add_creative_1113h.py [--dry|deals|verify]"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DT = "2026-11-13"
YA = "https://yandex.ru/maps/org/"
OBJ = "объект"
# id: (название, тип, категории, от, до, метро, до метро, адрес, (lat, lon, уровень, osm), телефон, сайт, часы, как найти,
#      плюс, источник возраста/услуг, карточка Яндекса, cat_ages|None)
D = {
 "soul-presnensky-val": ("Музыкальная школа-студия Soul (Пресненский Вал)", "музыкальная школа-студия", "music,singing", 5, 17,
    "Улица 1905 года", "420 м", "ул. Пресненский Вал, 5", None,
    "+7 (903) 729-23-86", "https://soul5.ru", None, "Вход: подъезд 3",
    "Индивидуальные уроки для детей и взрослых, можно с нуля: фортепиано и вокал — для детей с 5 лет, гитара (акустическая, классическая, электро, бас, укулеле) — с 7 лет, барабаны и саксофон; урок 60 минут — 1 250 ₽; ученикам — бесплатные репетиции на акустической ударной установке",
    "карточка Яндекс Карт, раздел «Товары и услуги» («Уроки фортепиано для детей с 5-ти лет и взрослых — 1250 ₽», «Уроки вокала для детей с 5-ти лет и взрослых — 1250 ₽», «гитаре взрослых и детей от 7 лет — 1250 ₽», «Бесплатные репетиции на акустической ударной установке для учащихся», подъезд 3)", "soul/32446035487", None, 1250, None),
 "my-risuem-rudneva": ("Студия рисования «Мы рисуем!» (Бутово)", "школа рисования для детей", "drawing", 5, 17,
    "Улица Горчакова", "470 м", "ул. Адмирала Руднева, 4", None,
    "+7 (915) 117-75-25", "https://мы-рисуем.рф", None, "Вход: вход 2\nЭтаж: 5, кабинет 17",
    "Рисование для детей в группах по возрасту: 5–6 лет (занятие 1 час), 7–9 лет (1,5 часа) и старшие группы (2 часа); пробное занятие — 700, 800 и 900 ₽",
    "карточка Яндекс Карт, раздел «Товары и услуги» («Группа для детей от 5 до 6 лет — Пробное занятие, 1 час — 700 ₽», «Группа для ребят от 7 до 9 лет — 1,5 часа — 800 ₽», «Старшие группы — 2 часа — 900 ₽»; вход 2, этаж 5, кабинет 17); у старших групп верхняя граница возраста не указана", "mi_risuem_/72667949303", None, None, None),
 "didance-lab-dmitrievskogo": ("Школа танцев Didance lab (ул. Дмитриевского)", "школа танцев", "dance", 3, 17,
    "Улица Дмитриевского", "510 м", "ул. Дмитриевского, 10", None,
    "+7 (929) 977-19-01", "https://didance-lab.clients.site", None, "Этаж: 3",
    "Бэйбидэнс для 3–7 лет (2 раза в неделю по 45 минут), контемпорари для 7–14 лет (2 раза по 1,5 часа), хип-хоп — группы 10+ и 13+, вог — 11+ и 15+ (2 раза в неделю по часу); есть профессиональная команда с чемпионатами и выступлениями",
    "карточка Яндекс Карт, раздел «Товары и услуги» («Бэйбидэнс … Возраст 3-7 лет — 4000 ₽», «Контемпорари … Возраст: 7-14 лет — 5500 ₽», «Хипхоп … Возрастные группы 10+ 13+ — 5000 ₽», «Вог … 11+ 15+ — 5000 ₽»; этаж 3)", "didance_lab/189545489739", None, None,
    "абонемент на месяц: бэйбидэнс — 4 000 ₽, хип-хоп и вог — 5 000 ₽, контемпорари — 5 500 ₽"),
 "kuznetsova-art-sedova": ("Арт-студия Натальи Кузнецовой (Свиблово)", "арт-студия", "drawing", 5, 17,
    "Ботанический сад", "580 м", "ул. Седова, 3", None,
    "+7 (968) 569-77-55", "https://www.kuznetsovanatalia.com", None, None,
    "Занятия рисованием для детей от 5 лет в мини-группах до 8 человек: 2 часа с перерывом на чай с баранками, все материалы включены, ведёт профессиональный художник — 2 000 ₽ за занятие",
    "карточка Яндекс Карт, раздел «Товары и услуги» («Занятие по рисованию для детей от 5 лет — 2 ч … Мини-группы до 8 человек … Перерыв на чай с баранками — 2000 ₽») и сайт kuznetsovanatalia.com («Арт-студия. Занятия живописью для детей и взрослых»)", "art_studio_of_natalia_kuznetsova/34732104446", None, 2000, None),
 "danceland-sharikopodshipnikovskaya": ("Школа танцев «ДансЛенд» (Шарикоподшипниковская)", "школа спортивных бальных танцев для детей", "dance", 3, 17,
    "Дубровка", "520 м", "Шарикоподшипниковская ул., 13, стр. 3", None,
    "+7 (903) 973-17-88", "https://dancelandschool.ru", None, None,
    "Спортивные бальные танцы для детей от 3 лет — европейская и латиноамериканская программы; первое занятие проходит индивидуально в присутствии родителей: диагностика физических данных и подробная обратная связь; разовое групповое занятие — 2 000 ₽",
    "сайт dancelandschool.ru («Школа танцев для детей», «Направление — спортивные бальные танцы. Танцы для детей от 3-х лет», «Первое занятие … в индивидуальном формате в присутствии родителей») и карточка Яндекс Карт («Разовое посещение группового занятия — 2000 ₽», «Пробное занятие в индивидуальном формате — 1 ₽», обновлено 28 октября)", "danslend/175030584865", None, 2000, None),
 "dhs-egoryevsk-tupitsyna": ("Детская художественная студия (Егорьевск)", "детская художественная студия", "drawing,ceramics", 5, 17,
    "Свято-Троицкий монастырь (остановка)", "180 м", "Егорьевск, ул. Алексея Тупицына, 2/14", None,
    "+7 (926) 304-52-26", "https://dhs-eg.ru", None, None,
    "Дети с 5 лет занимаются в малых группах по программе «Художественное творчество»: живопись, рисунок, композиция, скульптура, основы дизайна; есть керамика (группы до 8 человек), скетчинг, «Юный дизайнер» для 6–8 лет и подготовка в художественные колледжи и вузы; поступление — после собеседования с домашними работами",
    "сайт dhs-eg.ru («В студии занимаются дети с 5 лет, в малых группах», «Подготовка в художественные колледжи и ВУЗы», «Курсы керамики», расписание: «Юный дизайнер (6-8 лет)», «Керамика младшие») и карточка Яндекс Карт (адрес, телефон)", "detskaya_khudozhestvennaya_studiya/38628377716", None, None, None),
 "tants-premier-vernadskogo": ("Студия танцев «Танц-премьер» (просп. Вернадского)", "студия танцев", "dance", 4, 17,
    "Университет", "250 м", "просп. Вернадского, 9/10", None,
    "+7 (977) 109-29-93", "https://dance-premier.ru", None, "Этаж: цокольный",
    "Студия танцев для детей с 4 лет и взрослых: современные и восточные танцы, фламенко, хореография, модерн; двойной абонемент дешевле",
    "сайт dance-premier.ru («Студия танцев для детей и взрослых», «Возраст с 4-х до 60-и лет», «Двойной абонемент дешевле») и выдача Яндекс Карт (адрес, цокольный этаж, телефон, «Танцы: современные, восточные, фламенко, хореография, модерн»)", None, None, None, None),
}
PTP = os.path.join(ROOT, "tools", "creative_1113h_points.json")
ENTR = json.load(open(PTP)) if os.path.exists(PTP) else {}
_X = json.load(open(os.path.join(ROOT, 'tools', 'creative_1113h_ext.json')))
_IDS = json.load(open(os.path.join(ROOT, 'tools', 'creative_1113h_ids.json')))
TAGS = {"dance": "спорт и активность, музыка", "ballet": "спорт и активность, музыка", "singing": "музыка",
        "music": "музыка", "theaterstudio": "сказки и театр, творчество", "drawing": "творчество", "ceramics": "творчество"}


def point(pid):
    """Точка из справки OSM crz-* (tools/creative_1113h_points.json): объект OSM этого места или вход здания;
    иначе — дом по адресу (координаты Яндекс Карт), место скрыто, пока сверка не найдёт вход."""
    v = D[pid]
    if pid in ENTR:
        e = ENTR[pid]
        if e["level"] == OBJ:
            return e["lat"], e["lon"], f'точно (объект: {e["osm"]}), {e["why"]}, 13.11', OBJ, e
        return e["lat"], e["lon"], f'точно (вход: {e["osm"]}), OSM вход здания {v[7]} — {e["why"]}, 13.11', "вход", e
    o = _X[[k for k, v in _IDS.items() if v == pid][0]]
    lat, lon = o["ll"]
    return lat, lon, f"точно (дом по адресу {v[7]}, координаты здания — Яндекс Карты); подъезд уточнит сверка", "дом", None


def row(pid):
    name, typ, cats, a0, a1, met, dist, addr, pt, phone, site, hours, how, plus, asrc, ya, ca, price, note = D[pid]
    lat, lon, acc, lvl, _ = point(pid)
    first = cats.split(",")[0]
    active = first in ("dance", "ballet")
    r = P(pid, name, typ, met, addr, lat, lon, a0, a1, 45, 90, "активно" if active else "спокойно", TAGS[first],
          price, note, hours, "да", plus, None, adult=1,
          src=(f"Яндекс Карты: карточка организации yandex.ru/maps/org/{ya} (адрес, этаж/вход, телефон, сайт, услуги), 13.11.2026; " if ya else "Яндекс Карты: выдача поиска по названию и адресу, 13.11.2026; ") + f"возраст — {asrc}",
          acc=acc, adult_price=None, booking="обязательна", loud="частично" if active or first in ("music", "singing") else "нет",
          sit="нет" if active else "частично", crowd="нет", food="нет", stroller="частично")
    r["Взрослый билет, ₽"] = None
    r["Сайт"] = site
    r["Категории"] = cats
    r["Как найти"] = how
    r["Проверено (дата)"] = DT
    return r


ROWS = [row(k) for k in D]
TRIAL = {"danceland-sharikopodshipnikovskaya": ("Пробное занятие за 1 ₽ в «ДансЛенде»", "Школа спортивных бальных танцев «ДансЛенд» на Шарикоподшипниковской: пробное занятие в индивидуальном формате — 1 ₽; дети от 3 лет, первое занятие проходит в присутствии родителей с диагностикой и обратной связью", "https://yandex.ru/maps/org/danslend/175030584865/prices/")}

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
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
                 "age_max": r["Возраст до"], "booking": "обязательна", "phone": D[pid][9]}
            if r["Сайт"]:
                f["url"] = r["Сайт"]
            if r["Как найти"]:
                f["how"] = r["Как найти"]
            if r["Часы работы"]:
                f["hours"] = r["Часы работы"]
            lat, lon, acc, lvl, _ = point(pid)
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
            print(r["id"], "|", r["Адрес"], "|", r["Широта"], r["Долгота"], "|", r["Точность координат"][:70], "|", r["Сайт"])
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
    cp = os.path.join(ROOT, "auto", "cat-ages.json")
    ca = json.load(open(cp)) if os.path.exists(cp) else {}
    for pid, v in D.items():
        if v[16]:
            ca[pid] = dict(v[16], src=f"{v[14]} (13.11.2026)")
    json.dump(ca, open(cp, "w"), ensure_ascii=False, indent=1)
    print("rows", len(ROWS))
