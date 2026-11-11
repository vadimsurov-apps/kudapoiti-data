"""Робот fun, 2026-11-11 (проход b). Систематический поиск по районам: Видное, Королёв, Красногорск,
Люберцы, Мытищи, Одинцово, Подольск, Реутов, Авиамоторная, Автозаводская, Академическая, Алексеевская, Алма-Атинская,
Алтуфьево, Аминьевская (+ соседние районы из выдачи). Источник — выдача и карточки Яндекс Карт (кэш auto/pages/*-fnb*-1111b*,
*-fnc*-1111b*): название, вид, адрес, этаж/вход, телефон, сайт, возраст и цены — только то, что есть в карточке.
Точка: объект OSM с тем же названием, если есть; иначе здание по адресу из OSM (справка auto/osm-answers.json,
запросы fun-*), вход найдёт сверка osm_address. Часы не указываем (в карточках нет).
Иконки — tools/icons_fun_1111b.py. Запуск: KP_PART=fun python3 tools/add_fun_1111b.py"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC
from add_batch14 import metro

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DAY = "2026-11-11"
YA = "Яндекс Карты, карточка организации (11.11.2026)"
HOUSE = "приблизительно — здание по адресу (OpenStreetMap)"
COORD = json.load(open(os.path.join(ROOT, "tools", "coords_fun_1111b.json")))   # {id: [lat, lon, osm-объект или ""]}
ROWS = []
VER = {}


def add(pid, name, typ, cats, tags, addr, a0, a1, d0, d1, energy, plus, minus="", price=None, aprice="",
        phone=None, site="", adult=1, booking="обязательна", sit="частично", loud="нет", dark="нет",
        stroller="нет", crowd="нет", food="нет", how=None):
    if pid not in COORD:
        print("нет точки — пропуск:", pid)
        return
    lat, lon, osm = COORD[pid]
    acc = f"точно (OpenStreetMap {osm})" if osm else HOUSE
    r = P(pid, name, typ, metro(lat, lon), addr, lat, lon, a0, a1, d0, d1, energy, tags, price, None, None, "да",
          plus, minus, adult=adult, src=YA + (f"; OSM {osm}" if osm else "; здание — OSM"), acc=acc, adult_price=aprice,
          booking=booking, sit=sit, loud=loud, dark=dark, stroller=stroller, crowd=crowd, food=food)
    r["Сайт"] = site
    r["Категории"] = cats
    r["Проверено (дата)"] = DAY
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
    VER[pid] = {"fields": f, "src": YA + (f"; OSM {osm}" if osm else "")}


Q = dict(cats="quests", tags="приключения, логика", energy="активно", loud="да", sit="нет", d0=60, d1=90)
M = dict(cats="masterclass", tags="творчество", energy="спокойно")
S = dict(cats="masterclass,science", tags="техника, история и наука", energy="спокойно", d0=60, d1=90)
P_ = dict(cats="playcenters", tags="спорт и активность", energy="активно", loud="да", sit="нет", booking="желательна",
          stroller="частично", crowd="частично")

# --- игровые и праздники ---
add("fun-mega-pesochnitsa-mytishchi", "Игровая «Мега Песочница» (Мытищи)", "игровая комната",
    addr="Мытищи, Шараповский пр., вл. 2, стр. 3, этаж 3", a0=2, a1=10, d0=60, d1=180,
    plus="Игровая комната с праздниками; посещение — 600 или 800 ₽, абонемент на 5 часов — 3500 ₽; "
    "за 500 ₽ няня присмотрит за малышом от двух лет и проведёт мастер-класс по песочным фигуркам",
    price=600, phone="+7 911 746-46-00", site="https://www.msandbox.ru", how="Этаж: 3", **P_)
add("fun-igrovaya-deti-podolsk", "Игровая «Дети» (Подольск, фудхолл «Центральный»)", "игровая комната с няней",
    addr="Подольск, Комсомольская ул., 3, фудхолл «Центральный», этаж 2", a0=2, a1=10, d0=30, d1=120,
    plus="Игровая с няней прямо в фудхолле: первые 30 минут — 450 ₽, дальше 100 ₽ за каждые 10 минут — "
    "ребёнок играет под присмотром, а родители спокойно обедают", price=450, phone="+7 916 951-10-90",
    site="https://igrovaya-deti.ru", how="Этаж: 2, фудхолл «Центральный»", **{**P_, "food": "да", "booking": "не нужна"})
add("fun-deti-pri-dele-podolsk", "Игровое пространство «Дети при деле» (Подольск)", "детский клуб и игровая",
    addr="Подольск, ул. 50 лет ВЛКСМ, 2", a0=3, a1=12, d0=60, d1=180,
    plus="Игровое пространство с конструктором: в будни 3 часа — 1000 ₽; большой зал можно снять под праздник",
    price=1000, phone="+7 925 315-02-15", site="https://детиприделе.рф", **P_)
add("fun-kinderika-korolev", "Детские праздники «Киндерика» (Королёв, ТЦ «Юпитер»)", "детский праздничный центр",
    "playcenters", "спорт и активность", "Королёв, просп. Космонавтов, 34Б, ТЦ «Юпитер», этаж 3", 3, 10, 120, 180,
    "активно", "Площадка для детских дней рождения в торговом центре «Юпитер»", loud="да", sit="нет",
    how="Вход: через ТЦ «Юпитер»\nЭтаж: 3")

# --- лазертаг, VR, квесты ---
add("fun-drugie-miry-korolev", "VR-клуб «Другие Миры» (Королёв)", "клуб виртуальной реальности", "quests",
    "приключения, техника", "Королёв, просп. Космонавтов, 15", 8, 14, 30, 60, "активно",
    "Игры в виртуальной реальности: 30 минут — 700 ₽ в будни и 900 ₽ в выходные, час — 1100 и 1500 ₽; "
    "праздники для компаний от 6 человек", price=700, phone="+7 926 300-50-50",
    site="https://korolev.another-world.com", loud="да", sit="нет")
add("fun-portal-vr-lyubertsy", "VR-клуб Portal VR (Люберцы, ЖК «Самолёт»)", "клуб виртуальной реальности", "quests",
    "приключения, техника", "Люберцы, мкр Зенино, ЖК «Самолёт», Озёрная ул., 2, этаж 1", 7, 14, 30, 60, "активно",
    "VR-арена со свободным перемещением — 800 ₽, VR-квесты и игры — 600 ₽, автосимулятор — 450 ₽; дни рождения",
    price=450, phone="+7 903 130-19-51", site="https://lubercy.portal-vr.ru", how="Этаж: 1", loud="да", sit="нет")

# --- мастерские ---
add("fun-tk-school-vidnoe", "Арт-студия Tk School (Видное)", "художественная студия",
    addr="Видное, Завидная ул., 6, этаж 1", a0=3, a1=14, d0=120, d1=120, price=1800,
    plus="Живопись маслом и акрилом и современное искусство для детей от 3 лет: занятие 2 часа — 1800 ₽, "
    "пробное — 500 ₽; здесь же празднуют дни рождения с мастер-классом", phone="+7 967 261-65-24",
    how="Вход: с внешней стороны здания\nЭтаж: 1", **M)
add("fun-levandovskikh-odintsovo", "Студия керамики и живописи Левандовских (Одинцово)", "гончарная мастерская",
    addr="Одинцово, Молодёжная ул., 46, стр. 1, этаж 2, кабинет 26", a0=6, a1=14, d0=90, d1=120, price=1800,
    plus="Ручная лепка из глины для детей от 7 лет и рисование от 6 лет — 1800 ₽ за занятие, группы до 14 человек; "
    "можно устроить праздник в студии", phone="+7 916 278-04-96", how="Этаж: 2, кабинет 26", **M)
add("fun-masterim-podolsk", "Творческая мастерская «Мастерим» (Подольск)", "художественная мастерская",
    addr="Подольск, Февральская ул., 59, этаж 2", a0=5, a1=14, d0=90, d1=90, price=2200,
    plus="«Арт-релакс» для детей за 1,5 часа: картина акрилом на холсте и мягкая игрушка из фетра — 2200 ₽; "
    "детские праздники", phone="+7 965 200-09-17", site="https://www.мастерим.com", how="Этаж: 2", **M)
add("fun-yunyy-master-podolsk", "Столярная мастерская «Юный мастер» (Подольск)", "детская столярная мастерская",
    addr="Подольск, ул. Ульяновых, 1", a0=6, a1=14, d0=60, d1=120,
    plus="Столярный кружок для детей: пилят, строгают и собирают поделки из дерева",
    phone="+7 926 561-72-77", site="https://mastersschool.clients.site", **M)
add("fun-tuki-tuki-reutov", "Столярная мастерская «Туки-Туки» (Реутов)", "детская столярная мастерская",
    addr="Реутов, ул. Октября, 22", a0=5, a1=14, d0=150, d1=150,
    plus="Столярные мастер-классы: за 2,5 часа ребёнок сам делает игрушку или вещь для дома из дерева; "
    "дни рождения в мастерской", phone="+7 916 192-51-53",
    how="Вход: со стороны Центрального парка, от входа налево", **M)
add("fun-art-smart-michurinsky", "Арт-студия «Смарт» (Мичуринский проспект)", "художественная студия",
    addr="Москва, Мичуринский просп., 9, корп. 2", a0=4, a1=12, d0=60, d1=90,
    plus="Художественный кружок для детей 4–6 лет: рисование, лепка из глины и поделки; детские праздники",
    phone="+7 499 673-00-17", how="Вход: со двора", **M)
add("fun-glinka-60-oktyabrya", "Гончарная мастерская «Глинка» (проспект 60-летия Октября)", "гончарная мастерская",
    addr="Москва, просп. 60-летия Октября, 16, корп. 1", a0=7, a1=14, d0=90, d1=150,
    plus="Гончарный круг и лепка за столом, мастер-классы и дни рождения", **M)

# --- наука и техника ---
add("fun-stem-lab-vidnoe", "Детский центр IT и инженерии Stem Lab (Видное)", "детский IT-центр",
    addr="Видное, Берёзовая ул., 9, этаж 1", a0=5, a1=14,
    plus="Робототехника, Scratch и Python, разработка игр в Roblox и инженерия — курсы от 5000 ₽",
    phone="+7 968 599-97-03", site="https://stemlab-vidnoe.ru",
    how="Вход: под вывеской «Детский центр IT и инженерии»\nЭтаж: 1", **S)
add("fun-inzhinirium-korolev", "Инжинириум МГТУ им. Баумана (Королёв)", "инженерная школа для детей",
    addr="Королёв, ул. Калинина, 14", a0=5, a1=14, price=1200,
    plus="Робототехника с 5–6 лет, программирование для школьников (Scratch, Python, C++) и курс юного инженера — "
    "занятие 1200 ₽", phone="+7 905 555-23-45", site="https://inginirium-korolev.ru", **S)
add("fun-robocentr-poligon-altufyevo", "Робоцентр «Полигон» (Алтуфьево)", "школа робототехники",
    addr="Москва, Алтуфьевское ш., 102Б, этаж 1", a0=7, a1=14,
    plus="Робототехника на конструкторе EV3 для детей от 9 лет и программирование для 7–10 лет",
    phone="+7 903 979-03-77", site="https://www.robot-polygon.ru", how="Этаж: 1", **S)


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
    json.dump(VER, open("/tmp/claude-0/ver_fun_1111b.json", "w"), ensure_ascii=False, indent=1)
    print("rows", len(ROWS), "total", ws.max_row - 1)
