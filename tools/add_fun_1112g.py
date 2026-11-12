"""Робот fun, 2026-11-12 (проход g). Второй круг поиска по районам: Яндекс Карты (кэш auto/pages: *fuz*-1112g — поиск
по 15 районам, *fuy*-1112g — карточки организаций, *fux*-1112g — адреса с координатами дома).
Районы: Можайск, Руза, Шатура, Коммунарка, Троицк, Щербинка, Краснопресненская … Лермонтовский проспект.
Поля — только из карточек Яндекса (адрес, этаж, телефон, сайт, цены из «Товаров и услуг»); часов в карточках нет — пусто.
Пеленальных новых нет (оставшиеся точки osm-changing.json — туалеты в парках, где пеленальная уже есть, или без объекта).
Иконки — tools/icons_fun_1112g.py. Запуск: KP_PART=fun python3 tools/add_fun_1112g.py
"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC
from add_batch14 import metro

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DAY = "2026-11-12"
YA = "Яндекс Карты, карточка организации (12.11.2026)"
HOUSE = "приблизительно — здание по адресу (Яндекс Карты, координаты дома)"
ROWS, VER = [], {}


def place(pid, name, typ, cats, tags, addr, lat, lon, a0, a1, d0, d1, energy, plus, phone, site, src,
          hours=None, child=None, adult=None, note=None, how=None, minus="", loud="частично", sit="частично",
          booking="желательна", adult_int=2, food="нет", stroller="частично", crowd="частично", indoor="да"):
    r = P(pid, name, typ, metro(lat, lon), addr, lat, lon, a0, a1, d0, d1, energy, tags, child, note, hours, indoor,
          plus, minus or None, adult=adult_int, src=src, acc=HOUSE, adult_price=adult, booking=booking, sit=sit,
          loud=loud, dark="нет", stroller=stroller, crowd=crowd, food=food)
    r["Сайт"] = site
    r["Категории"] = cats
    r["Проверено (дата)"] = DAY
    if how:
        r["Как найти"] = how
    ROWS.append(r)
    f = {"address": addr}
    if phone:
        f["phone"] = phone
    if site:
        f["url"] = site
    if hours:
        f["hours"] = hours
    if child is not None:
        f["price_child"] = child
    if adult is not None:
        f["price_adult"] = adult
    if note:
        f["free_note"] = note
    VER[pid] = {"fields": f, "src": src}


S = lambda site: f"{YA}; сайт {site} (кэш auto/pages, 12.11.2026)"


YC = lambda n: f"{YA}: «{n}»"

# --- музеи ---
place("fun-troitsk-muzey-lyalko", "Троицкий музей имени М. Н. Лялько", "краеведческий музей", "museums",
      "история", "Троицк, Нагорная ул., 9", 55.491942, 37.299524, 5, 14, 45, 90, "спокойно",
      "Городской музей Троицка с недорогими билетами (45–100 ₽); посетители в отзывах на картах хвалят выставки",
      "+7 495 161-00-08", "https://www.okctinao.ru", YC("Троицкий музей имени М. Н. Лялько"),
      child=45, adult=100, loud="нет", booking="не нужна", adult_int=3)

place("fun-fizicheskaya-kunstkamera-troitsk", "Музей «Физическая кунсткамера» (Троицк, Дом учёных)", "музей науки",
      "museums,science", "наука", "Троицк, Октябрьский просп., 9Б", 55.475837, 37.295059, 7, 14, 45, 90, "средне",
      "Небольшой музей физики в здании Троицкого Дома учёных РАН",
      None, "", YC("Физическая кунсткамера"), loud="нет", booking="желательна", adult_int=3)

place("fun-emalis-taganskiy-park", "Музей эмальерного искусства «Эмалис» (Таганский детский парк)",
      "музей и мастерская", "museums,masterclass", "творчество, ремёсла",
      "Москва, ул. Таганская, 15А, Таганский детский парк", 55.741434, 37.661168, 7, 14, 60, 120, "спокойно",
      "Музей горячей эмали прямо в Таганском детском парке: можно посмотреть работы мастеров и сделать свой кулон, "
      "ёлочную игрушку или картину на мастер-классе (1990–4490 ₽)",
      "+7 967 211-65-38", "https://msk.emalis.org", YC("Музей эмальерного искусства"), child=1990, adult=1990,
      how="Вход: в Таганском детском парке, у детской площадки", booking="обязательна", loud="нет", sit="да")

place("fun-muzey-karameli-arbat", "Музей-мастерская карамели (Арбат)", "музей-мастерская", "museums,masterclass",
      "сладости, творчество", "Москва, ул. Арбат, 11, 2 этаж", 55.751376, 37.597684, 4, 14, 60, 90, "средне",
      "Интерактивный музей-мастерская карамели, 400 м от метро «Арбатская»; есть льготные билеты",
      "+7 966 015-15-79", "", YC("Музей-мастерская карамели"), child=1100, adult=1100,
      how="Этаж: 2", booking="желательна", minus="Билеты 1100–2100 ₽ — зависит от программы")

place("fun-zhivaya-istoriya-kurskaya", "Музей «Живая история» (ДК «Гайдаровец», Курская)", "интерактивный музей",
      "museums,masterclass", "история, ремёсла", "Москва, ул. Земляной Вал, 27, стр. 3, ДК «Гайдаровец», 1 этаж",
      55.759132, 37.658877, 5, 14, 60, 90, "средне",
      "Интерактивные и театрализованные экскурсии о жизни предков с мастер-классом, викториной и призами: "
      "«Как учили на Руси», «Как жили наши предки» (набивка на ткани), «Хлеб всему голова» (поморские козули)",
      "+7 905 548-11-01", "https://zhivayaistoriya.ru", YC("Живая история"), child=750,
      how="Вход: в ДК «Гайдаровец»\nЭтаж: 1", booking="обязательна")

place("fun-muzey-dalekoy-galaktiki", "Музей Далёкой Галактики (библиотека № 161, Крымская)", "музей в библиотеке",
      "museums", "космос, кино", "Москва, Загородное ш., 9, стр. 1, библиотека № 161", 55.692709, 37.606595,
      6, 14, 45, 90, "спокойно",
      "Тематический музей при городской библиотеке № 161, 360 м от МЦК «Крымская»",
      "+7 495 682-42-22", "", YC("Музей Далёкой Галактики") + " (телефон библиотеки, добавочный 2575)",
      loud="нет", booking="желательна", how="Вход: через библиотеку № 161")

place("fun-muzey-lozopleteniya-ruza", "Музей лозоплетения в Фабричном квартале (Руза)", "музей и мастерская",
      "museums,masterclass", "ремёсла, история", "Руза, Социалистическая ул., 14", 55.700978, 36.191129, 5, 14, 45, 90,
      "спокойно", "Музей плетения из лозы с курсами и мастер-классами в Фабричном квартале Рузы",
      None, "", YC("Музей лозоплетения в Фабричном квартале"), loud="нет", booking="желательна", adult_int=3)

# --- игровые, квесты ---
place("fun-legrovaya-butovo-mall", "Игровая комната «Легровая» (ТРЦ «Бутово Молл»)", "игровая комната",
      "playcenters", "игры, конструкторы", "Москва, Чечёрский пр-д, 51, ТРЦ «Бутово Молл», 3 этаж",
      55.524431, 37.517779, 3, 12, 60, 120, "средне",
      "Игровая комната на третьем этаже «Бутово Молла» — можно совместить с покупками",
      None, "", YC("Легровая"), how="Этаж: 3, ТРЦ «Бутово Молл»", booking="не нужна")

place("fun-neskuchayka-butovo-mall", "Игровая комната «Нескучай-ка» (ТРЦ «Бутово Молл»)", "игровая комната",
      "playcenters", "игры", "Москва, Чечёрский пр-д, 51, ТРЦ «Бутово Молл», 3 этаж", 55.524431, 37.517779,
      1, 10, 60, 120, "активно", "Детская игровая на третьем этаже «Бутово Молла», рядом с дрифт-картами Crazy Cart",
      None, "", YC("Нескучай-ка"), how="Этаж: 3, ТРЦ «Бутово Молл»", booking="не нужна", loud="да")

place("fun-atmokids-novinsky", "Детские квесты «Атмокидс» (Новинский бульвар)", "квест", "quests",
      "квесты, праздники", "Москва, Новинский бул., 18, корп. 2, 1 этаж", 55.754071, 37.585089, 6, 14, 60, 120,
      "активно", "Детские квесты и праздники с ведущими сети «Атмокидс» у Дома Шаляпина, 820 м от «Смоленской»",
      "+7 977 177-60-06", "https://atmo-kids.ru", YC("Атмокидс"), how="Этаж: 1", booking="обязательна", loud="да")

place("fun-kto-kruche-baumanskaya", "Шоу-игра «Кто Круче» (Бакунинская)", "шоу-игра", "quests",
      "квесты, праздники", "Москва, Бакунинская ул., 72, стр. 2", 55.777829, 37.691629, 10, 16, 90, 150, "активно",
      "Командная игра в формате телешоу с ведущим и необычными раундами; дни рождения «по-взрослому» для ребят 10–16 лет",
      "+7 958 578-17-20", "https://kto-kruche.ru", YC("Шоу-игра Кто Круче"),
      child=2200, adult=2200, booking="обязательна", loud="да", minus="Только для школьников от 10 лет")

place("fun-kukuruza-vr-ruza", "VR-клуб «КукуРуза» (Руза)", "клуб виртуальной реальности", "playcenters",
      "VR, настольные игры", "Руза, Революционная ул., 27А, 2 этаж", 55.702789, 36.191614, 8, 14, 30, 120, "средне",
      "Виртуальная реальность (500 ₽ за 30 минут в шлеме) и много настольных игр; стол под праздник — 400 ₽ в час, "
      "свою еду можно приносить; имениннику скидка 20% в день рождения и неделю после",
      "+7 495 924-56-72", "https://kukuruza-club.ru", YC("КукуРуза"), child=500, adult=500, how="Этаж: 2",
      booking="желательна")

OBJ = {}  # id -> (lat, lon, "точно (OSM …)") — объект места из auto/osm-answers.json

for r in ROWS:
    if r["id"] in OBJ:
        la, lo, acc = OBJ[r["id"]]
        r["Широта"], r["Долгота"], r["Точность координат"] = la, lo, acc
        VER[r["id"]]["fields"]["point"] = {"lat": la, "lon": lo, "level": "объект", "how": acc}

if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=i, column=1).value for i in range(2, ws.max_row + 1)}
    allids = {x["id"] for x in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    ids = [x["id"] for x in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    assert not [i for i in ids if i in existing or i in allids], [i for i in ids if i in existing or i in allids]
    for row_ in ROWS:
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        rr = ws.max_row + 1
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=rr, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    json.dump(VER, open("/tmp/claude-0/ver_fun_1112g.json", "w"), ensure_ascii=False, indent=1)
    print("rows", len(ROWS), "total", ws.max_row - 1)
