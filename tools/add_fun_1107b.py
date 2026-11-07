"""Робот fun, 2026-11-07 (утро): 18 мест — скалодромы (их мало: 14), Зеленоград, Долгопрудный, Федоскино,
два детских/семейных театра.
Источники: скалодромы — kp.ru/russia/moskva/skalodromy (2026) и t-j.ru/list/climbing-wall-moscow (16.06.2026);
Зеленоград/Долгопрудный/Мытищи — travelto.ru/blog/kuda-shodit-s-detmi-v-* (сентябрь 2026);
кэш сайтов auto/pages (ДМТЮА dmtya.ru, «Галатея» teatrgalateya.ru) + точки OSM из auto/candidates.json.
Координаты без OSM-точки — приблизительно по адресу (уточнит geocode-address.yml).
Дубли проверены по places.json и data/parts/*.xlsx (название + < 300 м). Иконки — tools/icons_fun_1107b.py.
Запуск: KP_PART=fun python3 tools/add_fun_1107b.py"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC
from add_batch14 import metro

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DAY = "2026-11-07"
KPC = "https://www.kp.ru/russia/moskva/skalodromy/"
TJ = "https://t-j.ru/list/climbing-wall-moscow/"
TT = "https://travelto.ru/blog/kuda-shodit-s-detmi-v-"
ROWS = []


def add(pid, name, typ, cats, tags, addr, lat, lon, a0, a1, d0, d1, energy, price, note, hours, plus, minus,
        src, exact=False, acc=None, indoor="да", adult=2, booking="не нужна", sit="нет", dark="нет", loud="нет",
        food="нет", season=None, stroller="частично", crowd="частично", moscow=True, site=""):
    m = metro(lat, lon) if moscow else "— (на машине / электричке)"
    r = P(pid, name, typ, m, addr, lat, lon, a0, a1, d0, d1, energy, tags, price, note, hours, indoor, plus, minus,
          adult=adult, src=src, acc="точно (OpenStreetMap)" if exact else (acc or "приблизительно, ±500 м"),
          booking=booking, sit=sit, dark=dark, loud=loud, food=food, season=season, stroller=stroller, crowd=crowd)
    r["Сайт"] = site
    r["Категории"] = cats
    r["Проверено (дата)"] = DAY
    ROWS.append(r)


def climb(pid, name, addr, lat, lon, a0, price, plus, minus, src, hours=None, **kw):
    add(pid, name, "скалодром", "climbing", "спорт и активность", addr, lat, lon, a0, 14, 60, 120, "активно",
        price, "разовое посещение «от»; детям — с инструктором/в группе", hours, plus, minus, src,
        booking="желательна", stroller="нет", adult=kw.pop("adult", 3), **kw)


# ===================== Скалодромы =====================
climb("tengu-lobachevskogo", "Скалодром Tengu's (ул. Лобачевского)", "Москва, ул. Лобачевского, 114", 55.6745, 37.4665, 6,
      850, "Боулдеринг-зал с групповыми тренировками для детей и взрослых; повторный вход в течение дня — в цене",
      "Детский возраст для групп — уточняйте", KPC + " ; " + TJ, hours="будни 8:00–24:00, сб–вс 9:00–24:00",
      acc="приблизительно, ±1 км")
climb("tengu-yuzhnaya", "Скалодром Tengu's (Южная)", "Москва, Днепропетровская ул., 2", 55.6230, 37.6095, 6, 1100,
      "Зал сети Tengu's у метро «Южная»: боулдеринг для начинающих и опытных", "Детские группы — уточняйте", TJ)
climb("tengu-maryina-roshcha", "Скалодром Tengu's (Марьина Роща)", "Москва, ул. Сущевский Вал, 49", 55.7945, 37.6160, 6,
      1100, "Зал сети Tengu's; безлимит на все залы сети — абонементом", "Детские группы — уточняйте", TJ)
climb("bigwall-dinamo", "Скалодром BigWall Sport (Динамо)", "Москва, Ленинградский пр-т, 36", 55.7905, 37.5600, 5, 700,
      "Большой скалодром сети BigWall рядом с метро «Динамо»; утром в будни дешевле",
      "Вечером и в выходные билет дороже (≈1350 ₽)", KPC + " ; " + TJ, hours="будни 7:00–23:30, выходные 8:00–23:00")
climb("bigwall-vodny", "Скалодром BigWall Sport (Водный стадион)", "Москва, Кронштадтский б-р, 3А", 55.8390, 37.4915, 5,
      690, "Зал сети BigWall у метро «Водный стадион»", "Вечером и в выходные дороже", TJ)
climb("bigwall-crocus", "Детский скалодром BigWall (Vegas Крокус Сити)", "МКАД 66 км, Vegas Крокус Сити, Международная ул., 12",
      55.8215, 37.3880, 4, 700, "Детский скалодром при батутном центре в ТРЦ — удобно совместить с батутами",
      "В выходные людно", KPC, hours="ежедневно 10:00–22:00", moscow=False, adult=2)
climb("skalodrom-ru-odintsovo", "Скалодром.ру (Одинцово)", "Одинцово, Транспортная ул., 2", 55.6790, 37.2620, 6, 800,
      "Скалодром в Одинцове — не нужно ехать в Москву", "Детские группы — уточняйте", TJ, moscow=False,
      acc="приблизительно, ±1 км")
climb("staraya-shkola-climb", "Скалодром «Старая школа»", "Москва, ш. Энтузиастов, 31, стр. 50, 3-й этаж", 55.7560,
      37.7405, 6, 600, "Занятия для детей и взрослых, недорогое разовое посещение", "Вход во дворе бизнес-центра", TJ,
      acc="приблизительно, ±1 км")
climb("raduga-climb-shcherbinka", "Скалодром «Радуга» (Щербинка)", "Щербинка, Юбилейная ул., 3А", 55.5050, 37.5620, 6,
      760, "Скалодром в Новой Москве — для жителей Щербинки и Бутова", "Детские группы — уточняйте", TJ,
      acc="приблизительно, ±1 км")
climb("highwall-kurkino", "Скалодром HighWall (Куркино)", "Москва, Воротынская ул., 18, ТЦ «Корабль»", 55.8945, 37.3955,
      5, 600, "Детская секция с группами по возрасту, скалодром в ТЦ", "Детский возраст — уточняйте", TJ,
      acc="приблизительно, ±1 км")

# ===================== Зеленоград =====================
ZG = TT + "zelenograde/"
add("zelenograd-museum", "Музей Зеленограда (дом «Флейта»)", "музей", "museums", "история",
    "Зеленоград, корпус 360 (дом «Флейта»)", 55.992232, 37.218356, 6, 14, 60, 120, "спокойно", None,
    "цены — на сайте музея; бывают дни бесплатного посещения",
    "вт–вс, в чт вечерний режим; пн — выходной",
    "Выставка «Здесь будет Зеленоград» от каменного века до войны; археологические занятия с раскопками в песке",
    "Программы — по расписанию", ZG, exact=True, adult=3)
add("zelenograd-museum-hall", "Выставочный зал Музея Зеленограда (Крюково)", "музей", "museums", "история, искусство",
    "Зеленоград, корпус 1410 (ул. Михайловка)", 55.986634, 37.146701, 5, 14, 45, 90, "спокойно", None,
    "цены — на сайте музея", "как у Музея Зеленограда; пн — выходной",
    "Сменные выставки с интерактивом для дошкольников", "Выставки меняются — смотрите афишу", ZG, exact=True)
add("miet-museum", "Музей истории МИЭТа («История электроники»)", "музей", "museums,science", "наука и техника, история",
    "Зеленоград, пл. Шокина, 1", 55.9842, 37.2115, 8, 14, 60, 90, "спокойно", None, "по регистрации",
    "по расписанию экскурсий", "Экспозиция «История электроники» и экскурсии по университету",
    "Только по предварительной регистрации; школьникам от 8 лет", ZG, booking="обязательна", adult=3)
add("zelenograd-dom-lani", "Экоцентр «Дом лани» (Крюковский лесопарк)", "ферма", "animals,parks", "животные, природа",
    "Зеленоград, Никольский пр-д, за домом 2, Крюковский лесопарк", 55.9947, 37.2406, 2, 14, 60, 120, "средне", 0,
    "многие мероприятия бесплатно по регистрации", "ежедневно 10:00–17:00; последний пн месяца — санитарный день",
    "Лани, декоративные птицы и кролики; экоквесты, викторины и тропа к смотровой площадке",
    "Экскурсии и занятия — по регистрации", ZG, exact=True, indoor="нет", stroller="частично")

# ===================== Долгопрудный, Мытищи, Федоскино =====================
add("dolgoprudny-museum", "Долгопрудненский историко-художественный музей", "музей", "museums", "история, наука и техника",
    "Долгопрудный, ул. Циолковского, 34", 55.940732, 37.513319, 6, 14, 60, 90, "спокойно", None,
    "цены — уточняйте", None, "Дирижаблестроение, канал Москва–Волга, мастер-классы и программы для детей",
    "Отдельные залы могут временно закрываться", TT + "dolgoprudnom/", exact=True, moscow=False)
add("fedoskino-lukutin", "Музей народных промыслов «Усадьба Лукутиных» (Федоскино)", "музей", "museums,masterclass",
    "искусство, творчество", "Мытищи, с. Федоскино", 56.055453, 37.582609, 5, 14, 60, 120, "спокойно", None,
    "цены — уточняйте", None, "Федоскинская лаковая миниатюра; семейные экскурсии и мастер-классы по росписи",
    "Мастер-классы — по записи", TT + "mytishchah/", exact=True, moscow=False, booking="желательна")

# ===================== Театры =====================
add("dmtya-theatre", "Детский музыкальный театр юного актёра (ДМТЮА)", "театр", "shows", "театр, музыка",
    "Москва, район Малой Дмитровки (основная сцена; есть сцена на ул. Макаренко)", 55.768197, 37.606755, 4, 14, 60, 120,
    "спокойно", None, "билеты — на сайте театра без комиссии", "по афише",
    "Детский театр, где играют сами дети; спектакли и театральные студии с 4 лет",
    "Часть спектаклей — на других площадках (Макаренко, Vegas City Hall); проверяйте место в билете",
    "https://dmtya.ru/", exact=True, sit="да", dark="частично", booking="обязательна", stroller="нет",
    site="https://dmtya.ru/")
add("galateya-solnechnogorsk", "Театр «Галатея» (Солнечногорск)", "театр", "shows", "театр",
    "Солнечногорск, здание ГЦНТиД «Лепсе»", 56.191147, 36.969962, 4, 14, 50, 90, "спокойно", None,
    "билеты — онлайн на сайте театра, есть Пушкинская карта", "по афише",
    "Городской театр Солнечногорска с детскими спектаклями", "Детские спектакли — не каждый день, смотрите афишу",
    "http://teatrgalateya.ru/", exact=True, sit="да", dark="частично", booking="желательна", stroller="нет",
    moscow=False, site="http://teatrgalateya.ru/")

if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    allids = {x["id"] for x in json.load(open(os.path.join(ROOT, "places.json")))["places"]}
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    ids = [r["id"] for r in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    assert not [i for i in ids if i in existing or i in allids], [i for i in ids if i in existing or i in allids]
    for row_ in ROWS:
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        r = ws.max_row + 1
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=r, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    print("rows", len(ROWS), "total", ws.max_row - 1)
