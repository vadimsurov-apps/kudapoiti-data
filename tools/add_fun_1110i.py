"""Робот fun, 2026-11-10 (вечерний проход). Источник — объекты OpenStreetMap из auto/candidates.json: точка — сам объект,
адрес — тег или дом объекта в OSM (справка auto/osm-answers.json, запросы fun-*), часы — тег OSM или сайт.
Пастернак — страница goslitmuz.ru (кэш auto/pages/goslitmuz-ru-museums-dom-muzey-b-l-pasternaka), Бахрушинский музей —
bakhrushinmuseum.ru (кэш auto/pages/bakhrushinmuseum-ru), музей Жуковского — qr.gbumac.ru/?p=10229 (кэш).
Детские библиотеки — как в add_fun_1110g.py (название, точка, часы, телефон — теги OSM; адрес — дом объекта).
Иконки — tools/icons_fun_1110i.py. Запуск: KP_PART=fun python3 tools/add_fun_1110i.py"""
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


# --- музеи и театры ---
PST = "https://goslitmuz.ru/museums/dom-muzey-b-l-pasternaka/"
add("pasternak-house-peredelkino", "way/60779144", "Дом-музей Б. Л. Пастернака (Переделкино)", "литературный музей",
    "Москва, пос. Переделкино, ул. Павленко, 3", (55.661312, 37.333829), 8, 14, 60, 120, "спокойно",
    "история, творчество", 0, "до 16 лет — бесплатно", "Вт–Вс 11:00–18:00",
    "Дача, где Борис Пастернак жил с 1939 года и узнал о Нобелевской премии; на сайте музея есть путеводитель "
    "по Переделкину для детей 6+", "Парковки у музея нет (работает эвакуатор) — машину оставляют у станции «Переделкино»",
    "museums", site=PST, phone="+7 495 695-53-08", adult_price=300, adult=3,
    how="Ориентир: от остановки автобуса «Городок писателей» (№ 316, 468) пройти 50 м по ходу автобуса и свернуть "
        "направо на ул. Павленко, до дома 3\nПарковка: у музея нет, ближайшая — у ж/д станции «Переделкино»")
add("okudzhava-museum-peredelkino", "node/864424236", "Мемориальный музей Б. Ш. Окуджавы (Переделкино)",
    "литературный музей", "Москва, пос. Переделкино, ул. Довженко, 11", (55.650432, 37.316491), 8, 14, 45, 90,
    "спокойно", "история, музыка", None, None, "Чт–Вс 11:00–17:00",
    "Дача Булата Окуджавы в писательском посёлке Переделкино", "", "museums", adult=3)
add("zhukovsky-memorial-museum", "node/2820078760", "Научно-мемориальный музей Н. Е. Жуковского", "музей авиации",
    "Москва, ул. Радио, 17, корп. 5", (55.763582, 37.679104), 6, 14, 60, 120, "спокойно", "техника, наука",
    None, None, None,
    "Более 50 тысяч экспонатов: модели почти всех российских самолётов, вертолётов, первых ракет и спутников, "
    "аэродинамические трубы", "", "museums,science", src_extra="; https://qr.gbumac.ru/?p=10229 (адрес и экспозиция)",
    adult=3)
BKH = "https://bakhrushinmuseum.ru/"
add("bakhrushin-theatre-museum", "node/273356351", "Театральный музей им. А. А. Бахрушина (главное здание)",
    "театральный музей", "Москва, ул. Бахрушина, 31/12, стр. 1", (55.731789, 37.638094), 7, 14, 60, 120, "спокойно",
    "театр, история", None, None, None,
    "Главный театральный музей страны; к Новому году — квест для юных зрителей «дело пропавшего актёра»",
    "С 9 ноября 2026 по 14 января 2027 обычные посещения закрыты — в музее идёт иммерсивный спектакль "
    "«Рождественский детектив»", "museums", site=BKH, phone="+7 499 484-77-77", adult=3, booking="обязательна")
add("hockey-museum-avtozavodskaya", "way/48841578", "Музей хоккея", "музей", "Москва, Автозаводская ул., 23, корп. 3",
    (55.703158, 37.646439), 6, 14, 45, 90, "спокойно", "спорт, история", None, None, "Пн–Сб 12:00–20:00",
    "Музей отечественного хоккея", "", "museums", adult=2)
add("skomorokh-puppets-kolomna", "node/13002548901", "Кукольный театр «Скоморох» (Коломна)", "кукольный театр",
    "Коломна, ул. Пушкина, 3А", (55.105081, 38.764933), 2, 10, 45, 60, "спокойно", "театр", None, None,
    "Ср–Вс 9:30–12:30, 13:00–18:30", "Кукольный театр в Коломне", "", "shows", adult=1, booking="желательна",
    sit="да", dark="частично")

# --- творчество и природа ---
add("ddt-sozvezdie-khimki", "way/174175625", "Дом детского творчества «Созвездие» (Химки)", "дом детского творчества",
    "Химки, ул. Панфилова, 14", (55.880595, 37.429551), 4, 14, 60, 120, "средне", "творчество", None, None, None,
    "Дом детского творчества: кружки и студии для детей", "", "masterclass", adult=1, booking="обязательна")
add("cdt-maryina-roshcha", "way/260112101", "Центр детского творчества «Марьина Роща»", "центр детского творчества",
    "Москва, 1-й Стрелецкий пр-д, 5", (55.796754, 37.607322), 4, 14, 60, 120, "средне", "творчество", None, None,
    None, "Районный центр детского творчества: кружки и студии", "", "masterclass", adult=1, booking="обязательна")
add("eco-bio-center-pavposad", "node/9863733071", "Детский эколого-биологический центр (Павловский Посад)",
    "эколого-биологический центр", "Павловский Посад, Большая Покровская ул., 38/2", (55.774055, 38.655739), 5, 14,
    60, 120, "средне", "природа, животные", None, None, None,
    "Детский эколого-биологический центр городского округа", "", "animals,masterclass", adult=1,
    booking="обязательна")

LIBS = "/tmp/claude-0/fun_libs_1110i.json"
if os.path.exists(LIBS):
    for x in json.load(open(LIBS)):
        add(x["id"], x["osm"], x["name"], "детская библиотека", x["addr"], (x["lat"], x["lon"]), 1, 14, 30, 120,
            "спокойно", "творчество", 0, "вход свободный", x.get("hours"),
            "Детская библиотека: книги для малышей и школьников, можно посидеть и почитать вместе", "", "museums",
            phone=x.get("phone"), site=x.get("site", ""), adult_price=0, adult=1)

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
    json.dump(VER, open("/tmp/claude-0/ver_fun_1110i.json", "w"), ensure_ascii=False, indent=1)
    print("rows", len(ROWS), "total", ws.max_row - 1)
