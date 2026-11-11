"""Робот fun, 2026-11-11 (проход fx).
1) Пеленальные: точки auto/osm-changing.json исчерпаны (остались аэропорты/ВДНХ/Сокольники — уже есть по одной на объект,
   туалеты у трасс и набережных без объекта). Поиск «комната матери и ребёнка» по 18 ТЦ/районам (кэш *fqa42–59*, *fqb25–49*)
   не дал карточек с адресом внутри ТЦ — новые пеленальные в этот проход не добавлены (не подтвердилось).
2) Поиск по районам (Яндекс Карты, кэш auto/pages/*fqa*-1111fx* — выдачи, *fqb* — карточки, *fqc*/*fqd* — координаты домов):
   Деловой центр, Корниловская, Кунцевская, Кутузовская, Ленинский проспект, Лесопарковая, Лианозово, Лихоборы,
   Ломоносовский проспект, Лухмановская, Марьина Роща, Медведково, Минская, Митино.
   Только места с возрастом в источнике (урок 7); остальные (Замания ×5, Визардия, Babyback, Сладкотня, Хокинг,
   Квесткиндер, Лофт Домми, Fort Boyard в «Филионе») пропущены до подтверждения возраста.
Точка — дом по адресу (Яндекс Карты, координаты дома): объект/вход OSM не получен (справка OSM не отработала) —
места скрыты до подтверждения входа подтверждателем.
Иконки — tools/icons_fun_1111fx.py. Запуск: KP_PART=fun python3 tools/add_fun_1111fx.py"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC
from add_batch14 import metro

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DAY = "2026-11-11"
YA = "Яндекс Карты, карточка организации (11.11.2026)"
HOUSE = "приблизительно — здание по адресу (Яндекс Карты, координаты дома)"
ROWS, VER = [], {}


def place(pid, name, typ, cats, tags, addr, lat, lon, a0, a1, d0, d1, energy, plus, phone, site, src, how=None,
          minus="", loud="частично", sit="частично", booking="обязательна", adult=1, price=None, note=None,
          stroller="нет"):
    r = P(pid, name, typ, metro(lat, lon), addr, lat, lon, a0, a1, d0, d1, energy, tags, price, note, None, "да",
          plus, minus, adult=adult, src=src, acc=HOUSE, adult_price="", booking=booking, sit=sit, loud=loud,
          dark="нет", stroller=stroller, crowd="нет", food="нет")
    r["Сайт"] = site
    r["Категории"] = cats
    r["Проверено (дата)"] = DAY
    if how:
        r["Как найти"] = how
    ROWS.append(r)
    f = {"address": addr, "phone": phone, "age_min": a0, "age_max": a1, "booking": booking}
    if site:
        f["url"] = site
    if price is not None:
        f["price_child"] = price
    if note:
        f["free_note"] = note
    VER[pid] = {"fields": f, "src": src}


place("fun-derzai-malysh-lyubertsy", "Игровая комната «Дерзай, малыш!» (Люберцы)", "детская игровая комната",
      "playcenters", "игры, праздники", "Люберцы, Весенняя ул., 10, этаж 1", 55.700091, 37.909022, 0, 12, 60, 180,
      "активно",
      "Яркая игровая для детей от 6 месяцев до 10–12 лет; в свободное от праздников время — свободное посещение без брони, "
      "550 ₽ за час в будни; для взрослых есть зона отдыха с чаем. Можно арендовать под день рождения со своей едой "
      "(до 15 детей и 20 взрослых)", "+7 993 263-27-55", "https://derzaymalysh.ru",
      YA + "; услуги и цены: «Яркая игровая комната для детей от 6 месяцев до 10–12 лет», «1 час в игровой будни (свободное посещение, без брони)» 550 ₽",
      how="Этаж: 1", minus="Когда идёт праздник по аренде, свободного посещения нет", loud="да", sit="нет",
      booking="желательна", price=550)

place("fun-kvest-loft-skhodnenskaya", "Квест-Лофт (Сходненская)", "квесты и детские праздники", "quests",
      "загадки, приключения, волшебство", "Москва, ул. Фабрициуса, 9", 55.842999, 37.441655, 7, 17, 60, 60, "средне",
      "Квесты в реальности о школе волшебников: «Битва магов» — для детей от 7 лет и взрослых, 5000 ₽ за команду до 4 "
      "человек; есть «мафия» в волшебном антураже и детские праздники", "+7 903 713-01-05", "https://portkey-loft.ru",
      YA + "; товары и услуги: квест «Хогвартс. Битва магов» — «для детей от 7 лет и взрослых», 5000 ₽",
      price=5000)

place("fun-cooknrun-strogino", "Кулинарное квест-шоу CooknRun (Строгино)", "кулинарное квест-шоу", "quests,masterclass",
      "кулинария, приключения, праздники", "Москва, ул. Твардовского, 8, корп. 5, стр. 3", 55.792579, 37.388736, 6, 17,
      150, 150, "активно",
      "Кулинарное квест-шоу «Адская кухня»: команды детей с ведущими-шефами готовят и проходят испытания, шоу длится "
      "2,5 часа, участникам от 6 лет; на одной площадке до 30 гостей — подходит для дня рождения и праздника класса",
      "+7 (495) 308-39-17", "https://cookn.run",
      "сайт cookn.run («2,5 часа длится шоу», «от 6 до 60 лет возраст участников», «до 30 гостей на одной площадке», адрес); " + YA,
      loud="да", sit="нет")

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
    json.dump(VER, open("/tmp/claude-0/ver_fun_1111fx.json", "w"), ensure_ascii=False, indent=1)
    print("rows", len(ROWS), "total", ws.max_row - 1)
