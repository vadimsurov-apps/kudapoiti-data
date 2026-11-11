"""Робот fun, 2026-11-11 (ночной проход a). Систематический поиск по районам: Апрелевка, Краснознаменск,
Лосино-Петровский, Старая Купавна, Голицыно, Кубинка, Нахабино, Дедовск, Московский, Внуково, Сосенское (Коммунарка),
Бутово, Мосрентген (+ соседние города из выдачи). Источник — выдача и карточки Яндекс Карт (кэш auto/pages/*-fnk*-1111a*,
*-fnj*-1111a*): название, вид, адрес, этаж/вход, телефон, сайт, возраст и цены — только то, что есть в карточке.
Точка: объект OSM с тем же названием, если есть; иначе здание по адресу из OSM (справка auto/osm-answers.json,
запросы fun-*), вход найдёт сверка osm_address. Часы не указываем (в карточках нет).
Иконки — tools/icons_fun_1111a.py. Запуск: KP_PART=fun python3 tools/add_fun_1111a.py"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC
from add_batch14 import metro

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DAY = "2026-11-11"
YA = "Яндекс Карты, карточка организации (11.11.2026)"
HOUSE = "приблизительно — здание по адресу (OpenStreetMap)"
COORD = json.load(open(os.path.join(ROOT, "tools", "coords_fun_1111a.json")))   # {id: [lat, lon, osm-объект или ""]}
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

# --- квесты ---
add("fun-dancity-aprelevka", "Квест-комната Dancity (Апрелевка)", "квест-комната для детей", addr="Апрелевка, ул. Дубки, 11",
    a0=3, a1=12, plus="Детские квесты: «Пиратский» для малышей 3–7 лет (30 минут — 2500 ₽) и «Египетский»; "
    "после квеста можно отметить праздник", phone="+7 910 401-54-90", site="https://quest-dancity.ru", **Q)
add("fun-propryatki-klimovsk", "Квест «ПроПрятки» (Климовск)", "квест-комната для детей",
    addr="Подольск, мкр Климовск, Школьная ул., 1А", a0=5, a1=14,
    plus="Квесты для детей и школьников, здесь же устраивают детские праздники",
    phone="+7 499 647-47-87", site="https://propryatki.ru", **Q)
add("fun-effectquest-dmitrov", "Квест EffectQuest (Дмитров)", "квест-комната", addr="Дмитров, Школьная ул., 2",
    a0=7, a1=14, plus="Три приключенческих квеста для детей от 7 лет — 3900 ₽ за час игры; можно отметить день рождения",
    phone="+7 495 255-25-24", site="https://effectquest.ru", **Q)
add("fun-5-klyuchey-forta-podolsk", "Квест «5 ключей Форта» (Подольск)", "квесты и игровая комната",
    addr="Подольск, ул. Карла Маркса, 25/130", a0=6, a1=14,
    plus="Квест «5 ключей Форта» — 1000 ₽, «НеДетские прятки» — 2000 ₽; есть игровая комната",
    phone="+7 926 521-43-66", site="http://www.fbpodolsk.ru",
    how="Вход: с улицы Карла Маркса, напротив «Вкусно — и точка»", **Q)
add("fun-fort-boyard-kurkino", "Квест «Форт Боярд» (Куркино)", "квест-шоу", addr="Москва, Новокуркинское ш., 1, этаж 3",
    a0=6, a1=14, plus="Испытания в духе телешоу для детей и взрослых, здесь празднуют дни рождения и выпускные",
    how="Этаж: 3", **Q)
add("fun-el-quest-nikolaeva", "Квесты «Эль Квест» (Электросталь, ул. Николаева)", "квест-комната",
    addr="Электросталь, ул. Николаева, 17А, этаж 2", a0=7, a1=14,
    plus="Квесты для школьников: приключения, «Гарри Поттер», по фильмам и играм; детские праздники",
    phone="+7 926 067-03-08", site="https://el-quest.ru", how="Этаж: 2", **Q)
add("fun-el-quest-yubileynaya", "Квесты «Эль Квест» (Электросталь, Юбилейная ул.)", "квест-комната",
    addr="Электросталь, Юбилейная ул., 11", a0=7, a1=14, plus="Квесты для школьников и детские праздники — от 4000 ₽",
    phone="+7 926 067-03-08", site="https://el-quest.ru", **Q)
add("fun-arkids-podolsk", "Квест-парк «Аркидс Парк» (Подольск)", "квесты и виртуальная реальность",
    addr="Подольск, ул. Клемента Готвальда, 6В, этаж 3, помещение 16, 18", a0=6, a1=14,
    plus="Детский квест «Аркидс», экшн-квест «Фараон», клуб виртуальной реальности и дни рождения",
    phone="+7 968 439-28-93", site="https://arkids.ru", how="Этаж: 3, помещение 16, 18", **Q)

# --- игровая ---
add("fun-holly-polly-kupavna", "Игровая комната Holly Polly (Старая Купавна)", "игровая комната", "playcenters",
    "спорт и активность", "Старая Купавна, ул. Горького, 1А", 1, 8, 60, 180, "активно",
    "Игровая зона: в будни 10:00–15:00 — 450 ₽ в час или 800 ₽ безлимит, 15:00–21:00 — 600 ₽ в час; "
    "в выходные 700 ₽ в час, 1200 ₽ безлимит", price=450, phone="+7 985 889-62-89", booking="не нужна", loud="да",
    sit="нет", stroller="частично", crowd="частично")

# --- мастер-классы и студии ---
M = dict(cats="masterclass", tags="творчество", energy="спокойно")
add("fun-shkola-shokolada-vyazemy", "Школа шоколада (Малые Вязёмы)", "кулинарная студия",
    addr="Одинцовский г.о., д. Малые Вязёмы, Петровское ш., 5", a0=5, a1=14, d0=60, d1=120,
    plus="Кулинарные мастер-классы для детей, подростков и взрослых, детские праздники",
    phone="+7 916 207-50-29", **M)
add("fun-keramika-tis-aprelevka", "Студия керамики «Тис» (Апрелевка)", "керамическая мастерская",
    addr="Апрелевка, Августовская ул., 1, ТЦ «Водолей», этаж 3", a0=6, a1=14, d0=60, d1=120,
    plus="Ручная лепка из глины для детей от 6 лет и взрослых; мастер-класс на гончарном круге — 3000 ₽",
    phone="+7 925 842-50-96", site="https://ceramicstis.ru", how="Этаж: 3, по лестнице направо, последний кабинет", **M)
add("fun-kisti-nakhabino", "Kisti ArtStudio (Нахабино)", "художественная мастерская",
    addr="Красногорск, пгт Нахабино, Новая ул., 17, этаж 2, кабинет 6", a0=6, a1=14, d0=90, d1=180,
    plus="Мастер-классы по живописи и картины жидким стеклом; есть занятия для детей", phone="+7 926 133-69-14",
    how="Этаж: 2, кабинет 6", **M)
add("fun-fru-fru-nakhabino", "Гончарная мастерская «Фру-Фру керамикс» (Нахабино)", "гончарная мастерская",
    addr="Красногорск, пгт Нахабино, Институтская ул., 18", a0=7, a1=14, d0=60, d1=60,
    plus="Гончарная мастерская и клуб для детей и подростков: занятия на гончарном круге индивидуально, "
    "оплата по часам — от 2500 ₽", phone="+7 967 128-81-32", **M)
add("fun-coddy-nakhabino", "Школа программирования Coddy (Нахабино)", "школа программирования для детей",
    "masterclass,science", "техника, история и наука", "Красногорск, пгт Нахабино, Школьная ул., 2, этаж 3", 8, 14,
    60, 90, "спокойно", "Курсы программирования для детей 8–12 лет: Scratch, Python, игровые движки Unity и Unreal",
    phone="+7 995 917-85-86", site="https://nahabino.coddyschool.com", how="Этаж: 3, кабинет «Нескучные науки»")
add("fun-art-zona-vnukovo", "Художественная студия «Арт-зона» (Внуково)", "художественная студия",
    addr="Москва, ул. Лётчика Грицевца, 14А, этаж 2", a0=4, a1=14, d0=60, d1=90,
    plus="Художественная школа: рисование для детей и взрослых", how="Этаж: 2", **M)
add("fun-artplace-starokrymskaya", "Творческие мастерские Artplace (Старокрымская ул.)", "художественная мастерская",
    addr="Москва, Старокрымская ул., 15, корп. 1", a0=5, a1=14, d0=60, d1=120,
    plus="Живопись для детей, бисероплетение и другие мастер-классы — от 1800 ₽", phone="+7 916 734-26-93",
    how="Вход: отдельный, подъезд 1", **M)
add("fun-shkola-tvorchestva-butovo-park", "Школа творчества (ЖК «Бутово парк»)", "детский творческий клуб",
    "masterclass,science", "творчество, техника", "Ленинский г.о., пгт Бутово, ЖК «Бутово парк», 5", 5, 12, 60, 60,
    "спокойно", "Клуб для детей: программирование в Scratch и творческие занятия — от 1000 ₽; здесь же «Школа юного "
    "инженера» с робототехникой для 6–8 лет", phone="+7 916 781-31-11", site="https://family-ecoclub.ru",
    how="Вход: отдельный, под вывеской «Школа творчества»\nЭтаж: 1")
add("fun-artmossfera-grina", "Студия «Артмоссфера» (ул. Грина)", "детская студия искусств",
    addr="Москва, ул. Грина, 5", a0=4, a1=9, d0=60, d1=90,
    plus="Рисование для детей 5–7 лет, ручная лепка из керамики 4–7 лет, история искусств 5–9 лет",
    phone="+7 993 633-63-60", site="https://www.artmossfera.ru", how="Вход: со стороны двора", **M)
add("fun-koneva-krasnoznamensk", "Студия живописи Коневой (Краснознаменск)", "студия живописи",
    addr="Краснознаменск, Октябрьская ул., 12", a0=5, a1=14, d0=60, d1=80, price=1400,
    plus="Масляная живопись для детей до 16 лет: разовое занятие — 1400 ₽, все материалы дают; "
    "малыши до 7 лет занимаются 60 минут, старшие — 80", phone="+7 977 144-62-34", **M)
add("fun-cosew-krasnobogatyrskaya", "Швейная мастерская «Сошью» (Краснобогатырская ул.)", "курсы шитья",
    addr="Москва, Краснобогатырская ул., 90, стр. 22, этаж 4", a0=8, a1=14, d0=90, d1=180,
    plus="Курсы кройки и шитья для детей и подростков и разовые мастер-классы: шоппер, футболка, вышивка",
    phone="+7 901 585-52-42", site="https://cosew.ru", how="Этаж: 4", **M)


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
    json.dump(VER, open("/tmp/claude-0/ver_fun_1111a.json", "w"), ensure_ascii=False, indent=1)
    print("rows", len(ROWS), "total", ws.max_row - 1)
