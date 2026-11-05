"""Партия 15 (2026-11-05): места из OpenStreetMap, где ночной робот нашёл детские акции, + несколько
проверенных роботом (сайт отвечает) детских мест. Координаты — OSM (точные).
Сайты в этот запуск напрямую не открывались — акции взяты из фраз робота (auto/promo-snippets.json от 2026-11-05)."""
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import base, swim, section, play, SRC

OSM = "OpenStreetMap; акция — с сайта места (робот, 2026-11-05)"
NOTE = "цену уточняйте на сайте"


def thermal(pid, name, lat, lon, site, plus, addr=None, hours="ежедневно 9:00–24:00"):
    return base(pid, name, "аквапарк", lat, lon, 1, 14, 180, 300, "активно", "вода", None,
                "акватермальный комплекс; детский тариф и бесплатный возраст — на сайте", hours, "да", plus,
                "Это термальный СПА-комплекс: много взрослых, часть зон 18+", site, "water", addr=addr,
                booking="желательна", food="да", loud="частично", crowd="да", adult=3)


def museum(pid, name, lat, lon, site, a0, plus, minus, tags="", hours=None, addr=None, typ="музей",
           price=None, note=NOTE, adult=3, indoor="да"):
    return base(pid, name, typ, lat, lon, a0, 14, 60, 120, "средне", tags, price, note, hours, indoor, plus, minus,
                site, "museums", addr=addr, food="нет", adult=adult)


ROWS = [
    swim("manta-club", "Manta Club — детский бассейн", 55.802706, 37.55603, "https://mantaclub.ru/",
         "Плавание для малышей и детей, есть пробное занятие и бесплатная парковка", a0=0, a1=10, price=None,
         hours="ежедневно 9:00–21:00"),
    swim("morelax-pool", "Детский бассейн «Морелакс»", 55.609288, 37.703982, "https://morelaxclub.ru/",
         "Бассейн для малышей; на пробное — аквапамперсы бесплатно", a0=0, a1=7, price=None),
    thermal("termoland-putilkovo", "Termoland Путилково (ВейПарк)", 55.859484, 37.395315,
            "https://putilkovo.termoland.ru/", "Тёплые бассейны и детские программы оздоровления"),
    thermal("termoland-fizteh", "Termoland Физтех", 55.921089, 37.534091, "https://fizteh.termoland.ru/",
            "Бассейны, надувной аттракцион, бесплатный трансфер от МЦД и метро", hours="ежедневно 9:00–24:00"),
    thermal("termoland-butovo", "Termoland Бутово", 55.55066, 37.540534, "https://butovo.termoland.ru/",
            "Детский бассейн с тёплой водой, горкой и водопадом-грибом", addr="аллея Витте, 1"),
    play("questkinder-among-us", "QuestKinder — детские квесты и шоу", "квест", 55.844518, 37.576583,
         "https://questkinder.events/", 6, None, "Квесты и шоу для детских праздников",
         "Нужна запись, лучше компанией", "quests", addr="Гостиничный пр-д, 6, корп. 2",
         hours="ежедневно 10:00–20:00", energy="средне", tags="сказки и театр"),
    section("redpoint-climb", "Скалодром RedPoint", 55.797082, 37.58103, "http://redpoint.msk.ru",
            "Скалодром с тренерами, можно попробовать подъёмы со снаряжением", "Скалолазание", a0=5, price=None,
            addr="Вятская ул., 27, стр. 12", hours="пн–пт 9:00–23:00; сб–вс 10:00–22:00"),
    play("jump-park-istra", "Батутный центр Jump Park (Истра)", "батутный центр", 55.915519, 36.857786,
         "https://jumppark.ru/", 3, None, "Батуты и тренировки, первое занятие бесплатно",
         "Выходные — многолюдно", "trampolines", hours="пн–пт 12:00–21:00; сб–вс 10:00–21:00"),
    play("nebo-sokol", "Батутный центр «Небо» (Сокол)", "батутный центр", 55.808676, 37.511925,
         "https://nebojump.ru/", 3, None, "Батуты и игровой центр, сопровождающим детей до 6 лет — бесплатно",
         "В выходные много детей", "trampolines", hours="ежедневно 10:00–22:00"),
    play("joki-joya-mozaika", "Joki Joya (Мозаика)", "развлекательный центр", 55.71089, 37.677556,
         "https://joki-joya.ru/park/mozaika", 1, None, "Большой игровой парк в ТРЦ «Мозаика», лазертаг",
         "Громко и людно в выходные", "playcenters", hours="ежедневно 10:00–22:00"),
    play("wanderia-zhukovsky", "Семейный парк «Вандерия» (Жуковский)", "развлекательный центр", 55.609864, 38.083272,
         "https://wanderia.ru/", 2, None, "Игровой парк и детские праздники", "Далеко от Москвы",
         "playcenters", addr="Жуковский, Театральная ул., 7Д"),
    play("drakosha-chekhov", "Детский центр «Дракоша» (Чехов)", "развлекательный центр", 55.399773, 37.603479,
         "http://drakoncik.ru/", 1, None, "Игровая для малышей и дни рождения с аниматорами",
         "Небольшой центр, далеко от Москвы", "playcenters"),
    base("mori-cinema-mytishchi", "Кинотеатр Mori Cinema (Мытищи)", "кинотеатр", 55.91969, 37.707822, 3, 14, 90, 120,
         "спокойно", "сказки и театр", None, "цена зависит от сеанса", "по расписанию", "да",
         "Детские сеансы, скидка многодетным", "Проверяйте афишу", "https://mori-cinema.ru/cinema_detail/82_mytishchi",
         "cinema", dark="да", sit="да", food="да", loud="частично"),
    museum("metro-na-dache", "Музей «Метро на даче»", 55.567735, 37.041277, "https://metro-na-dache.clients.site", 3,
           "Частный музей метро: вагоны, турникеты, таблички", "Открыт только по четвергам и воскресеньям",
           tags="машины и транспорт", hours="чт,вс 11:00–19:00", addr="КИЗ «Полис», 18",
           note="детям до 6 лет бесплатно", adult=3),
    museum("tsar-maket", "Музей «Царь-макет»", 55.817112, 37.655463, "https://tsar-maket.ru/", 3,
           "Огромный движущийся макет с поездами и городами", "Касса до 18:15", tags="машины и транспорт",
           hours="ежедневно 10:00–19:00"),
    museum("mk-zoya", "Музейный комплекс «Зоя» (Петрищево)", 55.49372, 36.306729, "https://mk-zoya.ru", 7,
           "Музей памяти Зои Космодемьянской, экспозиция о войне для школьников",
           "Далеко от Москвы; тема серьёзная — для детей постарше", addr="Рузский округ, д. Петрищево, 89, стр. 2",
           adult=3),
    base("minty-elephant", "Детский клуб «Мятный слон» (Серпухов)", "мастерская", 54.925399, 37.443583, 1, 7, 60, 120,
         "средне", "творчество", 800, "пробное занятие 800–1000 ₽", None, "да",
         "Развивающие занятия для малышей, можно прийти на пробное", "Далеко от Москвы", "https://mintyelephant.tilda.ws/",
         "masterclass", booking="обязательна", food="нет", adult=1),
    base("ato-theatre", "Театральная студия «АТО»", "театр", 55.791359, 37.808819, 5, 14, 60, 90,
         "средне", "сказки и театр", None, "первое занятие бесплатно", "по расписанию", "да",
         "Актёрские занятия для детей, первое ознакомительное — бесплатно",
         "Зачисление в группу — по итогам пробного", "https://www.ato-teatr.ru/", "shows", booking="обязательна",
         food="нет", stroller="нет", adult=1),
    base("ecobiocentre", "Детский эколого-биологический центр", "мастерская", 55.820512, 37.672413, 5, 14, 60, 120,
         "средне", "природа, животные", None, NOTE, None, "частично",
         "Кружки по биологии и экологии для школьников рядом с ВДНХ", "Занятия по записи и расписанию",
         "https://www.ecobiocentre.ru/", "science", booking="обязательна", food="нет", adult=1),
    base("safari-park-mozhaysk", "Сафари-парк (Можайский округ)", "зоопарк", 55.466562, 35.719482, 2, 14, 60, 180,
         "средне", "животные, природа", None, "корм для копытных выдают бесплатно", "ежедневно 10:00–18:00", "нет",
         "Прогулка с проводником среди копытных, можно кормить животных",
         "Только с проводником, одежда — для леса", "https://safaripark50.ru", "animals", food="нет",
         stroller="нет", adult=3),
]
for r in ROWS:
    r["Источник"] = OSM
    if r["id"] == "redpoint-climb":
        r["Тип"] = "скалодром"

if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    ids = [r["id"] for r in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    assert not [i for i in ids if i in existing], [i for i in ids if i in existing]
    for row in ROWS:
        assert not (set(row) - set(hdr)), (row["id"], set(row) - set(hdr))
        r = ws.max_row + 1
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=r, column=i, value=row.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    print("rows", len(ROWS), "total", ws.max_row - 1)
    for r in ROWS: print(r["id"], "|", r["Метро"])
