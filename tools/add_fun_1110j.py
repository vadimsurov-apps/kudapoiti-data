"""Робот fun, 2026-11-10 (ночной проход j). Источник — объекты OpenStreetMap из auto/candidates.json: точка — сам объект,
адрес — тег объекта или дом, в котором он стоит (справка auto/osm-answers.json, запросы fun-*; дом с адресом ≤ 20 м
или постройка с тем же названием), часы и телефон — теги OSM. Дом-музей Цветаевой — сайт dommuseum.ru (кэш
auto/pages/osm-way-300426888: часы, адрес), музей Высоцкого — сайт visotsky.ru (кэш auto/pages/osm-node-2715045290: экспозиция).
Взяты только те, у кого адрес подтверждён; кандидаты с мёртвыми сайтами и без дома с адресом пропущены.
Иконки — tools/icons_fun_1110j.py. Запуск: KP_PART=fun python3 tools/add_fun_1110j.py"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC
from add_batch14 import metro

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DAY = "2026-11-10"
EX = "точно (OpenStreetMap)"
ROWS = []
VER = {}   # для tools/set_verified.py


def add(pid, osm, name, typ, addr, ll, a0, a1, d0, d1, energy, tags, price, note, hours, plus, minus, cats,
        site="", phone=None, adult_price=None, src_extra="", how=None, adult=2, booking="не нужна", **kw):
    lat, lon = ll
    r = P(pid, name, typ, metro(lat, lon), addr, lat, lon, a0, a1, d0, d1, energy, tags, price, note, hours, "да",
          plus, minus, adult=adult, src=f"OpenStreetMap {osm} (адрес — объект/дом в OSM)" + (f"; {site}" if site else "")
          + src_extra, acc=EX, adult_price=adult_price, booking=booking, food="нет", crowd="нет", **kw)
    r["Сайт"] = site
    r["Категории"] = cats
    r["Проверено (дата)"] = DAY
    if how:
        r["Как найти"] = how
    ROWS.append(r)
    src = f"OSM {osm}" + (f"; {site}" if site else "") + src_extra
    f = {"point": {"lat": lat, "lon": lon, "level": "объект", "how": f"OSM {osm}"}, "address": addr}
    if hours:
        f["hours"] = hours
    if phone:
        f["phone"] = phone
    if site:
        f["url"] = site
    VER[pid] = {"fields": f, "src": src}


# --- музеи ---
add("tsvetaeva-house-borisoglebsky", "way/300426888", "Дом-музей Марины Цветаевой (Борисоглебский пер.)",
    "литературный музей", "Москва, Борисоглебский пер., 6, стр. 1", (55.754199, 37.590127), 10, 14, 45, 90, "спокойно",
    "история, творчество", None, None, "Вт, Ср, Пт–Вс 12:00–19:00, Чт 12:00–21:00",
    "Дом, где Марина Цветаева жила с семьёй с 1914 по 1922 год", "", "museums",
    site="http://www.dommuseum.ru", phone="+7 495 695-35-43", adult=3)
add("vysotsky-house-taganka", "node/2715045290", "Музей Владимира Высоцкого (Дом Высоцкого на Таганке)", "музей",
    "Москва, ул. Высоцкого, 3, стр. 1", (55.744477, 37.651818), 10, 14, 60, 90, "спокойно", "музыка, театр, история",
    None, None, "Вт, Ср, Пт 11:00–18:00, Чт 13:00–21:00, Сб–Вс 11:00–17:00",
    "Экспозиция с интерактивными витринами: можно снять трубку телефона и услышать песню, увидеть голограмму "
    "Высоцкого, костюмы из кино и спектаклей", "", "museums", site="https://www.visotsky.ru", phone="+7 495 915-29-79",
    adult=3)
MG = "https://www.mgomz.ru/"
add("kolomenskoe-water-mill", "node/5366770779", "Водяная мельница (Коломенское)", "музей",
    "Москва, пр-т Андропова, 39, стр. 62 (музей-заповедник «Коломенское»)", (55.672109, 37.680276), 5, 14, 20, 45,
    "спокойно", "история, техника", None, None, "Ср–Пт 10:00–18:00, Сб 11:00–19:00, Вс 10:00–18:00",
    "Водяная мельница в музее-заповеднике «Коломенское»", "", "museums", site=MG, phone="+7 499 782-89-17", adult=2)
add("peter-dutch-house", "node/5366770786", "Голландский домик царя Петра I (Коломенское)", "музей",
    "Москва, пр-т Андропова, 39 (музей-заповедник «Коломенское»)", (55.672067, 37.679586), 6, 14, 20, 45,
    "спокойно", "история", None, None, "Ср–Пт 10:00–18:00, Сб 11:00–19:00, Вс 10:00–18:00",
    "Музейный домик, посвящённый Петру I, рядом с водяной мельницей в «Коломенском»", "", "museums", site=MG,
    phone="+7 499 782-89-17", adult=2)
add("gorky-park-museum", "node/7797262065", "Музей Парка Горького", "музей", "Москва, ул. Крымский Вал, 9",
    (55.731344, 37.603725), 6, 14, 30, 60, "спокойно", "история", None, None, "Вт–Вс 11:00–22:00",
    "Музей истории Парка Горького у главного входа в парк", "", "museums", site="https://park-gorkogo.com/",
    phone="+7 495 995-00-20", adult=2)

# --- детские библиотеки (название, точка, часы, телефон — теги OSM; адрес — дом объекта) ---
add("lib-griboedov-kids", "node/697026275", "Детская библиотека им. Грибоедова", "детская библиотека",
    "Москва, ул. Сущёвский Вал, 66", (55.792196, 37.62781), 1, 14, 30, 120, "спокойно", "творчество", 0,
    "вход свободный", "Вт–Сб 10:00–21:00, Вс 10:00–20:00",
    "Детская библиотека: книги для малышей и школьников, можно посидеть и почитать вместе", "", "museums",
    phone="+7 495 631-05-45", adult_price=0, adult=1)
add("lib125-kids", "node/3062506725", "Детская библиотека №125", "детская библиотека",
    "Москва, 3-й Павловский пер., 14", (55.718342, 37.630306), 1, 14, 30, 120, "спокойно", "творчество", 0,
    "вход свободный", "Вт–Сб 10:00–22:00, Вс 10:00–20:00",
    "Детская библиотека: книги для малышей и школьников, можно посидеть и почитать вместе",
    "Последний вторник месяца — санитарный день", "museums", phone="+7 495 682-42-22", adult_price=0, adult=1)
add("lib14-kids-central", "node/4945836155", "Центральная детская библиотека №14", "детская библиотека",
    "Москва, ул. Бахрушина, 4, стр. 1", (55.736418, 37.634121), 1, 14, 30, 120, "спокойно", "творчество", 0,
    "вход свободный", "Вт–Сб 10:00–21:00, Вс 10:00–20:00",
    "Детская библиотека: книги для малышей и школьников, можно посидеть и почитать вместе", "", "museums",
    phone="+7 495 953-54-06", adult_price=0, adult=1)


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
    json.dump(VER, open("/tmp/claude-0/ver_fun_1110j.json", "w"), ensure_ascii=False, indent=1)
    print("rows", len(ROWS), "total", ws.max_row - 1)
