"""Робот fun, 2026-11-10 (поздний проход z). Систематический поиск по районам: Шелепиха, Шипиловская, Шоссе Энтузиастов,
Щукинская, Электрозаводская, Юго-Восточная, Юго-Западная, Южная, Ясенево, Яхромская, Луховицы, Талдом,
Павловский Посад, Электроугли. Источник — выдача и карточки Яндекс Карт (кэш auto/pages/yandex-ru-maps-*-fnz*-1110z*,
*-fny*-1110z*): название, вид, адрес, этаж, телефон, сайт и цены — только то, что есть в карточке.
Точка: у «Ну, погоди-ка!» и «Джельсомино» — объект OSM с тем же названием; у остальных — здание по адресу из OSM
(справка auto/osm-answers.json, запросы fun-*), вход найдёт сверка osm_address. Часы не указываем (в карточках нет).
Иконки — tools/icons_fun_1110z.py. Запуск: KP_PART=fun python3 tools/add_fun_1110z.py"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC
from add_batch14 import metro

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DAY = "2026-11-10"
YA = "Яндекс Карты, карточка организации (10.11.2026)"
HOUSE = "приблизительно — здание по адресу (OpenStreetMap)"
ROWS = []
VER = {}


def add(pid, name, typ, cats, tags, addr, ll, a0, a1, d0, d1, energy, plus, minus="", osm=None, price=None,
        aprice=None, phone=None, site="", floor=None, adult=1, booking="обязательна", sit="частично", loud="нет",
        dark="нет", stroller="нет", crowd="нет", food="нет", how=None):
    lat, lon = ll
    acc = f"точно (OpenStreetMap {osm})" if osm else HOUSE
    r = P(pid, name, typ, metro(lat, lon), addr, lat, lon, a0, a1, d0, d1, energy, tags, price, None, None, "да",
          plus, minus, adult=adult, src=YA + (f"; OSM {osm}" if osm else "; здание — OSM"), acc=acc, adult_price=aprice,
          booking=booking, sit=sit, loud=loud, dark=dark, stroller=stroller, crowd=crowd, food=food)
    r["Сайт"] = site
    r["Категории"] = cats
    r["Проверено (дата)"] = DAY
    h = how or (f"Этаж: {floor}" if floor else None)
    if h:
        r["Как найти"] = h
    ROWS.append(r)
    f = {"address": addr}
    if osm:
        f["point"] = {"lat": lat, "lon": lon, "level": "объект", "how": f"OSM {osm}"}
    if phone:
        f["phone"] = phone
    if site:
        f["url"] = site
    VER[pid] = {"fields": f, "src": YA + (f"; OSM {osm}" if osm else "")}


# --- игровые ---
add("fun-nupogodika-zaraysk", "Игровая комната «Ну, погоди-ка!» (Зарайск)", "игровая комната с батутами и кафе",
    "playcenters", "спорт и активность", "Зарайск, Советская ул., 43", (54.758209, 38.889618),
    1, 10, 60, 180, "активно", "Игровая комната, батутный центр и кафе в одном месте", osm="node/12605164803",
    phone="+7 926 744-05-05", booking="желательна", loud="да", stroller="частично", crowd="частично", food="да",
    adult=1, sit="нет")

# --- наука и техника ---
add("fun-altair-vernadskogo", "Детский технопарк «Альтаир» РТУ МИРЭА", "детский технопарк", "science,masterclass",
    "история и наука, техника", "Москва, просп. Вернадского, 86, стр. 2", (55.660978, 37.476092), 7, 17, 90, 120,
    "спокойно", "Технопарк университета МИРЭА: школьники делают собственные проекты под руководством педагогов",
    phone="+7 912 076-96-56", site="https://www.mirea.ru")
add("fun-liga-robotov-yuzhnaya", "Лига роботов (Чертаново, Днепропетровская ул.)", "клуб робототехники",
    "masterclass,science", "техника, история и наука", "Москва, Днепропетровская ул., 3, корп. 5А, этаж 2, офис 205",
    (55.621922, 37.601455), 6, 10, 60, 90, "спокойно", "Робототехника для детей 6–7 и 8–10 лет",
    phone="+7 905 579-79-29", site="https://chertanovo.s.ligarobotov.ru", how="Этаж: 2, офис 205")
add("fun-tesla-beskudnikovsky", "Клуб юных инженеров «Тесла» (Бескудниково)", "клуб робототехники",
    "masterclass,science", "техника, история и наука", "Москва, Бескудниковский пр., 2, корп. 1", (55.87482, 37.550024),
    5, 10, 60, 90, "спокойно",
    "Робототехника: электроника, механика и программирование — группы 5–7 и 8–10 лет; первое занятие бесплатно, "
    "4 занятия — 7600 ₽", phone="+7 499 213-15-10", site="https://robotesla.ru")

# --- мастер-классы и творчество ---
add("fun-pervoe-hobbi-yasenevo", "Клуб «Первое хобби» (Ясенево)", "клуб рукоделия для детей", "masterclass",
    "творчество", "Москва, Новоясеневский просп., 24, корп. 4, этаж 6, помещение 2", (55.602758, 37.52809), 6, 14,
    90, 90, "спокойно", "Детские кружки вязания, шитья и мягкой игрушки — 1200 ₽ за занятие",
    price=1200, aprice=0, phone="+7 985 525-81-18", site="https://1-hobby.ru", how="Этаж: 6, помещение 2")
add("fun-lepka-shipilovskaya", "Мастерская лепки из глины (Шипиловская ул., 58)", "гончарная мастерская",
    "masterclass", "творчество", "Москва, Шипиловская ул., 58, корп. 1, этаж 2, павильон 236", (55.621244, 37.745544),
    4, 14, 60, 60, "спокойно", "Разовый детский мастер-класс по лепке из глины в группе — 1200 ₽",
    price=1200, aprice=0, site="https://vk.ru/okeramike", how="Этаж: 2, павильон 236")
add("fun-dzhelsomino-shelepiha", "Творческий центр «Джельсомино» (Шелепиха)", "детский творческий центр",
    "masterclass,playcenters", "творчество", "Москва, Шелепихинская наб., 22", (55.757758, 37.518372), 4, 12, 60, 210,
    "средне", "Студия активного досуга «Я-сам»: за вечер ребёнок и творит, и двигается — 1500 ₽ за 3,5 часа",
    osm="node/6982565912", price=1500, aprice=0, phone="+7 926 842-33-77", site="https://www.djelso.ru")

# --- театральные студии ---
add("fun-artkids-shelepiha", "Актёрская школа Art Kids Community (Шелепиха)", "детская актёрская школа",
    "masterclass", "театр, творчество", "Москва, Шелепихинская наб., 34к2зд2", (55.762865, 37.510629), 5, 16,
    60, 90, "средне", "Актёрская школа для детей; первое занятие бесплатно", phone="+7 916 744-64-79",
    site="https://artkidscommunity.com")
add("fun-otrazhenie-kirovogradskaya", "Театральная студия «Отражение» (Пражская)", "детская театральная студия",
    "masterclass", "театр, творчество", "Москва, Кировоградская ул., 11, корп. 1, этаж 4", (55.614424, 37.606655),
    6, 17, 60, 90, "средне", "Актёрское мастерство для детей и подростков — 12 400 ₽; есть пробное занятие",
    phone="+7 499 955-45-22", site="https://detskaya.studio-otragenie.ru", how="Этаж: 4")
add("fun-krylataya-dolina-lobachevskogo", "Студия творчества «Крылатая долина» (ул. Лобачевского)",
    "детская студия творчества и театр", "masterclass,shows", "театр, творчество",
    "Москва, ул. Лобачевского, 52, корп. 1", (55.672181, 37.492373), 5, 14, 60, 60, "спокойно",
    "Каждое воскресенье — спектакли для детей и подростков (800 ₽); театральная студия 5–8 лет — 1400 ₽ за час",
    price=800, phone="+7 968 320-82-22", site="https://krylataya-dolina.ru", how="Вход: в арку дома", booking="желательна",
    sit="да")

# --- квесты ---
add("fun-quest-hunter-semenovskaya", "Квесты «Квест Хантер» (Электрозаводская)", "квест", "quests",
    "загадки и приключения", "Москва, Большая Семёновская ул., 11, стр. 5", (55.783392, 37.703073), 8, 14, 60, 90,
    "средне", "Приключенческий квест «Операция Nike» для дня рождения — команда секретных агентов (11 000 ₽ за игру)",
    phone="+7 936 314-69-88", site="https://quest-hunter.ru", dark="частично", adult=2)


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
    json.dump(VER, open("/tmp/claude-0/ver_fun_1110z.json", "w"), ensure_ascii=False, indent=1)
    print("rows", len(ROWS), "total", ws.max_row - 1)
