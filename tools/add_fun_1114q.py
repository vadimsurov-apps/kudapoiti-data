"""Робот fun, 2026-11-14 (проход 1114q). Пеленальные комнаты на вокзалах Москвы и в ТРЦ (выдачи Яндекс Карт fqk<N>/fqm<N>/fqn-<k>
-1114q, сайты ТРЦ), музеи и зоопарк из кандидатов OSM (карточки fqo-<N>-1114q), второй круг поиска по районам (выдачи fqa<N>-1114q:
Пионерская … Профсоюзная, карточки fqd-<N>-1114q). Точки — объекты OSM (auto/candidates.json, справки auto/osm-answers.json).
Иконки — tools/icons_fun_1114q.py. Запуск: KP_PART=fun python3 tools/add_fun_1114q.py"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC
from add_batch14 import metro

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DAY = "2026-11-14"
HOUSE = "приблизительно — здание по адресу (Яндекс Карты, координаты дома)"
ROWS, VER = [], {}
ANS = json.load(open(os.path.join(ROOT, "auto/osm-answers.json")))


def place(pid, name, typ, cats, tags, addr, lat, lon, a0, a1, d0, d1, energy, plus, phone, site, src,
          hours=None, child=None, adult=None, note=None, how=None, minus="", loud="частично", sit="частично",
          booking="желательна", adult_int=2, food="нет", stroller="частично", crowd="частично", indoor="да",
          osm=None, changing=None, acc=None):
    acc = acc or (f"точно (объект: OSM {osm}, проверено {DAY})" if osm else HOUSE)
    r = P(pid, name, typ, metro(lat, lon), addr, lat, lon, a0, a1, d0, d1, energy, tags, child, note, hours, indoor,
          plus, minus or None, adult=adult_int, src=src, acc=acc, adult_price=adult, booking=booking, sit=sit,
          loud=loud, dark="нет", stroller=stroller, crowd=crowd, food=food)
    r["Сайт"] = site
    r["Категории"] = cats
    r["Проверено (дата)"] = DAY
    if changing:
        r["Пеленальный стол"] = changing
    if how:
        r["Как найти"] = how
    ROWS.append(r)
    f = {"address": addr}
    if osm:
        f["point"] = {"lat": lat, "lon": lon, "level": "объект", "how": f"OSM {osm}"}
    if phone:
        f["phone"] = phone
    if site:
        f["url"] = site
    if hours:
        f["hours"] = hours
    if child is not None:
        f["price_child"] = child
    if adult not in (None, ""):
        f["price_adult"] = adult
    if note:
        f["free_note"] = note
    if cats != "changing":
        f["age_min"] = a0
        f["age_max"] = a1
    VER[pid] = {"fields": f, "src": src}


def obj(qid, osm):
    """координаты объекта OSM из справки auto/osm-answers.json (qid) — первый совпавший по osm-id"""
    for k in ([qid] if qid else list(ANS)):
        v = ANS.get(k) or {}
        for p in v.get("pois", []) + v.get("buildings", []):
            if p.get("osm") == osm:
                return p["lat"], p["lon"]
    raise KeyError((qid, osm))


# ---------------- пеленальные комнаты ----------------
YK = "Яндекс Карты, выдача «{q}» (кэш auto/pages, {k}-1114q, 14.11.2026)"


def chg(pid, name, addr, lat, lon, osm, plus, src, hours=None, how=None, phone=None, site=None, minus=""):
    place(pid, name, "пеленальная комната", "changing", "малыши", addr, lat, lon, 0, 3, 10, 20, "спокойно", plus, phone, site,
          src, hours=hours, child=0, adult=0, how=how, minus=minus, loud="нет", sit="частично", booking="не нужна",
          adult_int=1, food="нет", stroller="да", crowd="нет", indoor="да", osm=osm, changing="да")



la, lo = obj("fun-mall-4", "relation/1395483")
chg("chg-kursky-vokzal", "Пеленальная комната — Курский вокзал", "Москва, ул. Земляной Вал, 29, Курский вокзал, 2 этаж", la, lo,
    "relation/1395483", "Комната матери и ребёнка на Курском вокзале работает круглосуточно",
    "Яндекс Карты, карточка «Комната матери и ребенка» (кэш auto/pages, fqn-kursky-1114q и fxn-atrium-1114a, 14.11.2026): «Москва, ул. "
    "Земляной Вал, 29, этаж 2», rzd.ru, «Время работы Круглосуточно», «Курский вокзал 145 м»; точка — объект OSM relation/1395483 "
    "«Курский вокзал» (railway=train_station, ул. Земляной Вал 29, auto/osm-answers.json, справка fun-mall-4)",
    hours="круглосуточно", how="Этаж: 2, в здании вокзала", site="https://www.rzd.ru/")
la, lo = obj("confirm-2-fun-pavilion-transport-kievsky", "relation/2261797")
chg("chg-kievsky-vokzal", "Пеленальная комната — Киевский вокзал", "Москва, площадь Киевского Вокзала, 1, Киевский вокзал", la, lo,
    "relation/2261797", "Комната матери и ребёнка на Киевском вокзале; на вокзале есть и круглосуточная детская игровая площадка (подъезд 1)",
    YK.format(q="комната матери и ребенка Киевский вокзал", k="fqk4") + ": «Комната матери и ребенка … Открыто до 11:00 PM», «Детская игровая "
    "площадка … Круглосуточно … Москва, площадь Киевского Вокзала, 1, подъезд 1»; выдача fqn-kievsky-1114q «Комната матери и ребенка, Москва, "
    "площадь Киевского Вокзала, 1»: первой — «Комната матери и ребенка, Открыто до 11:00 PM», затем «Киевский вокзал»; полного графика нет — "
    "часы не пишем; точка — объект OSM relation/2261797 «Киевский вокзал» (площадь Киевского Вокзала 1, auto/osm-answers.json)")
la, lo = obj("edu25-122", "relation/7253185")
chg("chg-paveletsky-vokzal", "Пеленальная комната — Павелецкий вокзал", "Москва, Павелецкая площадь, 1, Павелецкий вокзал", la, lo,
    "relation/7253185", "Комната матери и ребёнка на Павелецком вокзале",
    YK.format(q="комната матери и ребенка Павелецкий вокзал", k="fqk5") + ": «Комната матери и ребёнка … Открыто до 10:00 PM», «Павелецкий "
    "вокзал … Круглосуточно»; выдача fqn-paveletsky-1114q «Комната матери и ребенка, Москва, Павелецкая площадь, 1» — комнаты «Открыто до "
    "10:00 PM»; полного графика нет — часы не пишем; точка — объект OSM relation/7253185 «Павелецкий вокзал» (railway=train_station, "
    "Павелецкая площадь 1А, auto/osm-answers.json)")
la, lo = obj("fun-1114f-o9", "relation/16127615")
chg("chg-belorussky-vokzal", "Пеленальная комната — Белорусский вокзал", "Москва, площадь Тверская Застава, 7, Белорусский вокзал", la, lo,
    "relation/16127615", "Комната матери и ребёнка на Белорусском вокзале работает круглосуточно",
    YK.format(q="комната матери и ребенка Белорусский вокзал", k="fqk6") + ": «Белорусский вокзал … Круглосуточно», следом «Комната матери и "
    "ребенка … Круглосуточно»; выдача fqn-belorussky-1114q «Комната матери и ребенка, Москва, площадь Тверская Застава, 7»: первой — «Комната "
    "матери и ребенка … Круглосуточно»; точка — объект OSM relation/16127615 (building=train_station, площадь Тверская Застава 1, "
    "auto/osm-answers.json)", hours="круглосуточно")
la, lo = obj("fun-1114z-o18", "way/365905388")
chg("chg-vykhodnoy-lyubertsy", "Пеленальная комната — ТРЦ «Выходной» (Люберцы)", "Люберцы, Октябрьский просп., 112, ТРЦ «Выходной»",
    la, lo, "way/365905388", "Комнаты матери и ребёнка в ТРЦ «Выходной» на Октябрьском проспекте; в том же ТРЦ на 2 этаже — игровая «Чайлэнд»",
    YK.format(q="комната матери и ребенка ТРЦ Выходной Люберцы Октябрьский проспект 112", k="fqk11") + ": «Провыходной … Открыто до 10:00 PM, "
    "Торговый центр, Люберцы, Октябрьский просп., 112», следом две «Комната матери и ребенка … Открыто до 10:00 PM», «Чайлэнд … Игровая "
    "комната, Люберцы, Октябрьский просп., 112, этаж 2»; выдача fqn-vykhodnoy-1114q — три комнаты «Открыто до 10:00 PM»; карточка ТРЦ "
    "fqm11-1114q: vykhodnoy.ru; полного графика нет — часы не пишем; точка — объект OSM way/365905388 «Торговый центр «Выходной»» "
    "(shop=mall, Октябрьский проспект вл112, справка fun-1114z-o18)", site="https://vykhodnoy.ru/")


# ---------------- музеи и зоопарк из кандидатов OSM (карточки Яндекс Карт fqo-<N>-1114q) ----------------
YO = "Яндекс Карты, карточка «{n}» (кэш auto/pages, fqo-{k}-1114q, 14.11.2026)"


def museum(pid, name, addr, lat, lon, osm, k, ynm, plus, ysrc, phone=None, site=None, hours=None, cats="museums",
           tags="история", note=None, how=None, a0=0, a1=17, adult_int=3, d1=90, typ="музей", extra_src="", indoor="да",
           energy="спокойно", loud="нет", booking="желательна", sit="частично", crowd="частично"):
    place(pid, name, typ, cats, tags, addr, lat, lon, a0, a1, 45, d1, energy, plus, phone, site,
          YO.format(n=ynm, k=k) + ": " + ysrc + f"; объект OSM {osm} (auto/candidates.json)" + extra_src,
          hours=hours, note=note, how=how, loud=loud, sit=sit, booking=booking, adult_int=adult_int, indoor=indoor,
          crowd=crowd, osm=osm)


museum("fun-muzey-khleba-serpukhov", "Музей хлеба (Серпухов)", "Серпухов, Калужская ул., 9", 54.915194, 37.411031,
       "node/9591722217", 4, "Музей хлеба",
       "Музей хлеба в центре Серпухова с экскурсиями и чаепитием «у купчихи»; для детей 4+ — мастер-классы (до 8 лет — со взрослым); "
       "билеты — 300–500 ₽",
       "«Музей хлеба», «Музей», «Серпухов, Калужская ул., 9», «+7 (903) 592-27-15», museumbread.ru, «Билеты : 300–500 ₽», отзывы "
       "«Экскурсии · 89% положительный», подборки «Город павлинов: маршрут по Серпухову на один день», «Исторические музеи Серпухова»; "
       "сайт museumbread.ru (кэш auto/pages, 14.11.2026): «Пн Вт Ср Чт Пт Сб Вс / выходной выходной выходной выходной / 14:00-18:00 / "
       "11:00-18:00 / 11:00-17:00», «Стоимость 600 ₽ с человека», мастер-класс «Возраст участников 4+, до 8 лет детей должен сопровождать взрослый»",
       phone="+7 (903) 592-27-15", site="https://museumbread.ru/", tags="история, еда",
       hours="пт 14:00–18:00; сб 11:00–18:00; вс 11:00–17:00; пн–чт выходной",
       how="Остановка: «Земляной мост» — 350 м")
museum("fun-muzey-rvsn-vlasikha", "Музей Ракетных войск стратегического назначения (Власиха)",
       "Одинцовский г.о., пос. Власиха, ул. Маршала Жукова, 36, стр. 321", 55.687102, 37.18927, "way/83341194", 5, "Музей РВСН",
       "Музей Ракетных войск стратегического назначения в посёлке Власиха, рядом со штабом РВСН; билеты — 50–100 ₽",
       "«Музей РВСН», «Музей», «посёлок Власиха, ул. Маршала Жукова, 36, стр. 321», «+7 (495) 598-71-86», www.cmaf.ru, «Билеты : 50–100 ₽», "
       "«Штаб РВСН 340 м»; график в карточке не показан («Закрыто до понедельника») — часы не пишем",
       phone="+7 (495) 598-71-86", site="https://www.cmaf.ru/", tags="техника, история, космос")
museum("fun-kolomenskiy-navigator", "Музей «Коломенский навигатор» (Старая Коломна)", "Коломна, ул. Зайцева, 14", 55.105812, 38.763605,
       "node/3125490638", 3, "Коломенский навигатор",
       "Музей и туристический центр в Старой Коломне: экспозиция «Загляни в Коломну!» с гидом (45 мин — 600 ₽), самостоятельный "
       "квест-экскурсия «Коломенская кругосветка» (50 мин — 500 ₽) и пешая экскурсия по Коломенскому посаду (60 мин — 950 ₽)",
       "«Коломенский навигатор», «Туристический инфоцентр экскурсии музей», «Коломна, ул. Зайцева, 14», «+7 (495) 228-11-10», "
       "kolomna-navigator.ru, «Открыто до 8:00 PM», услуги: «Пешая экскурсия по территории Коломенского посада … 950 ₽ 60 мин», "
       "«Экскурсия по музейной экспозиции нижнего зала с гидом «Загляни в Коломну!» … 600 ₽ 45 мин», «Самостоятельный квест-экскурсия "
       "«Коломенская кругосветка» … 500 ₽ 50 мин»",
       phone="+7 (495) 228-11-10", site="https://kolomna-navigator.ru/", hours="ежедневно 10:00–20:00", cats="museums,tours",
       tags="история, прогулки", extra_src=", часы «Mo-Su 10:00-20:00» (OSM) совпадают с карточкой и сайтом kolomna-navigator.ru «с 10:00 до 20:00»; "
       "сайт: «Посещение музеев для детей до 3 лет, детей-инвалидов с одним сопровождающим … бесплатно»",
       note="Детям до 3 лет — бесплатно; ребёнку-инвалиду с одним сопровождающим — бесплатно",
       energy="средне", how="Остановка: «Рынок» — 280 м")
museum("fun-zheleznoe-tsarstvo", "Музей скульптур из металла «Железное царство» (Коростово)", "д. Коростово, 24 (Подмосковье)",
       55.899916, 37.302225, "node/5371334147", 12, "Музей скульптур из металла Железное Царство",
       "Частный музей скульптур из металла в деревне Коростово: фигуры, сваренные из железа; есть экскурсии",
       "«Музей скульптур из металла Железное Царство», «Музей», «д. Коростово, 24», «Валентин Яковлевич +7 (985) 784-10-49», "
       "www.частныемузеи.рф, «Открыто до 5:00 PM», отзывы «Экскурсии · 99% положительный», «Скульптура · 100% положительный»; "
       "в OSM «Музей изделей из металла»; полный график не показан — часы не пишем",
       phone="+7 (985) 784-10-49", site=None, tags="искусство, техника", indoor="частично",
       how="Остановка: «Светлые Горы» — 520 м")
museum("fun-naro-fominsk-museum", "Наро-Фоминский историко-краеведческий музей", "Наро-Фоминск, ул. Маршала Жукова, 8", 55.384234, 36.724213,
       "node/1833558556", 28, "Наро-Фоминский историко-краеведческий музей",
       "Краеведческий музей Наро-Фоминска: археология, быт, военная история и сельское хозяйство края, есть аудиогид; билеты — 100–150 ₽, есть льготные",
       "«Наро-Фоминский историко-краеведческий музей», «Музей», «Наро-Фоминск, ул. Маршала Жукова, 8», «+7 (49634) 3-80-48», "
       "museum-nf.mo.muzkult.ru, «Особенности: Оплата картой, Льготные билеты, Аудиогид, Музей : антропологический, историко-бытовой, "
       "декоративное-прикладное искусство, этнографический, общеисторический, сельское хозяйство, военно-исторический, изобразительное "
       "искусство, археологический, краеведческий, фотография», «Билеты : 100–150 ₽»; часы в OSM («Tu-Sa 09:30-17:30») и в карточке "
       "(«Открыто до 7:00 PM» в субботу) расходятся — не пишем",
       phone="+7 (49634) 3-80-48", site="https://museum-nf.mo.muzkult.ru/")
museum("fun-muzey-mikroelektroniki", "Музей микроэлектроники им. А. И. Шокина (Зеленоград)", "Зеленоград, площадь Шокина, 2, стр. 3",
       55.98196, 37.213697, "node/9957821698", 30, "Музей микроэлектроники",
       "Музейно-выставочный центр имени А. И. Шокина у МИЭТ — история микроэлектроники и Зеленограда",
       "«Музей микроэлектроники», «Музей выставочный центр», «Москва, Зеленоградский административный округ, площадь Шокина, 2, стр. 3», "
       "«+7 (499) 720-80-46», museum.angstrem.ru, «МИЭТ 274 м»; в OSM «Музейно-выставочный центр им. А. И. Шокина», адрес «площадь Шокина, "
       "2 с4»; график не показан («Закрыто до понедельника») — часы не пишем",
       phone="+7 (499) 720-80-46", site="https://museum.angstrem.ru/", cats="museums,science", tags="техника, наука")
museum("fun-ekoderevushka-parfentyevo", "Мини-зоопарк «Экодеревушка» (Парфентьево, Коломна)", "Коломна, село Парфентьево, Полевая ул., 32",
       55.10942, 38.826089, "way/567514655", 35, "Экодеревушка",
       "Зоопарк-деревня в селе Парфентьево под Коломной, по соседству с Крокодиловой фермой",
       "«Экодеревушка», «Зоопарк», «село Парфентьево, Полевая ул., 32, Экодеревушка», «Открыто до 8:00 PM», подборка «Коломна: калачи, "
       "пастила и кремль…», рядом «Крокодиловая ферма … село Парфентьево»; сайт www.ecoderevushka.ru (OSM); полный график не показан — часы не пишем",
       site="https://www.ecoderevushka.ru/", typ="зоопарк", cats="animals", tags="животные, природа", indoor="частично",
       energy="средне", loud="частично", booking="не нужна", sit="нет", adult_int=2)


if __name__ == "__main__":
    import glob, re
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=i, column=1).value for i in range(2, ws.max_row + 1)}
    allp = json.load(open(os.path.join(ROOT, "places-all.json")))["places"]
    allids = {x["id"] for x in allp}
    norm = lambda t: re.sub(r"\W", "", (t or "").lower().replace("ё", "е"))
    names = {norm(x["name"]) for x in allp}
    for f in glob.glob(os.path.join(ROOT, "data", "parts", "*.xlsx")) + [os.path.join(ROOT, "data", "kuda-poiti-mesta.xlsx")]:
        w2 = openpyxl.load_workbook(f, read_only=True)["Места"]
        for r in w2.iter_rows(min_row=2, values_only=True):
            if r[0]:
                allids.add(r[0]); names.add(norm(r[1]))
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    ids = [x["id"] for x in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    assert not [i for i in ids if i in existing or i in allids], [i for i in ids if i in existing or i in allids]
    assert not [x["Название"] for x in ROWS if norm(x["Название"]) in names], [x["Название"] for x in ROWS if norm(x["Название"]) in names]
    for row_ in ROWS:
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        rr = ws.max_row + 1
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=rr, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    out = os.environ.get("VER_OUT", "/tmp/claude-0/ver_fun_1114q.json")
    json.dump(VER, open(out, "w"), ensure_ascii=False, indent=1)
    print("rows", len(ROWS), "total", ws.max_row - 1, ids)
