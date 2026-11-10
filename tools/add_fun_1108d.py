"""Робот fun, 2026-11-08 (день): места Подмосковья из путеводителей travelto.ru «Куда сходить с детьми в …» и
городских страниц (кэш auto/pages), новостей РИАМО (кэш) и OSM (auto/candidates.json).
Иконки — tools/icons_fun_1108c.py. Запуск: KP_PART=fun python3 tools/add_fun_1108c.py"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC
from add_batch14 import metro

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DAY = "2026-11-08"
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



O = " ; OpenStreetMap"
TT = "https://travelto.ru/blog/kuda-shodit-s-detmi-v-"

add("tsagi-demo-center-zhukovsky", "Демонстрационный центр ЦАГИ (Жуковский)", "музей", "museums,science",
    "наука, самолёты", "Жуковский, ул. Жуковского, 1, корп. 1", 55.596722, 38.111474, 7, 14, 60, 120, "спокойно",
    None, "экскурсии и программы — по записи, цены уточняйте", "в дни экскурсионных программ (по записи)",
    "Музей главного авиационного института страны: продувочные модели самолётов, модели экспериментальных установок, "
    "макеты перспективных летательных аппаратов; на программах показывают учебные установки и объясняют, как воздух "
    "обтекает самолёт. Рядом — уличная экспозиция «История ЦАГИ»",
    "Свободного входа нет — только экскурсии и дни открытых дверей, запись заранее",
    TT + "zhukovskom/" + O, exact=True, moscow=False, booking="обязательна", adult=3)
add("kolomna-battle-glory-museum", "Музей боевой славы (Коломна)", "музей", "museums", "история",
    "Коломна, ул. Непобедимого, 1", 55.093891, 38.771742, 8, 14, 45, 90, "спокойно", None,
    "билеты — в кассе музея", "уточняйте",
    "Экспозиция о военной истории и коломенцах — защитниках страны в разные эпохи; экскурсии, лекции и "
    "интерактивные программы для школьников",
    "Военная тема — лучше для школьников постарше; с малышами в Коломне интереснее музеи игрушки или калача",
    TT + "kolomne/" + O, exact=True, moscow=False, adult=3)
add("yaropolets-goncharov-estate", "Усадьба Загряжских-Гончаровых (Ярополец)", "усадьба", "museums,tours",
    "история, природа", "Волоколамский г.о., с. Ярополец", 56.134117, 35.827402, 7, 14, 60, 120, "средне", None,
    "осмотр — по программе Ярополецкого краеведческого музея", "уточняйте в Ярополецком краеведческом музее",
    "Пушкинское место: сюда поэт приезжал к родственникам Натальи Гончаровой. Главный дом, флигели, церковь и старый "
    "парк; рядом — краеведческий музей и старинная Ярополецкая ГЭС на Ламе",
    "Далеко от Москвы; какой формат осмотра доступен в день поездки — узнавать в краеведческом музее",
    TT + "volokolamske/" + O, exact=True, moscow=False, indoor="частично", adult=3, booking="желательна")
add("panfilov-heroes-museum-nelidovo", "Музей Героев-панфиловцев (Нелидово)", "музей", "museums", "история",
    "Волоколамский г.о., д. Нелидово, ул. Крестьянская, 18", 55.975, 35.85, 8, 14, 60, 90, "спокойно", None,
    "билеты — в кассе музея (филиал Волоколамского кремля)", "уточняйте",
    "Филиал Волоколамского кремля: документы, письма, фотографии и вещи бойцов Панфиловской дивизии, рядом — "
    "интерактивное пространство с реконструкциями; в километре — мемориал у разъезда Дубосеково",
    "Тяжёлая военная тема — для школьников; младшим лучше экскурсия с рассказом о людях",
    TT + "volokolamske/", acc="приблизительно, ±2 км", moscow=False, adult=3)
add("darovoe-dostoevsky-estate", "Музей-усадьба Достоевского «Даровое»", "усадьба", "museums,tours",
    "книги, история, природа", "г.о. Зарайск, д. Даровое", 54.703, 38.656, 7, 14, 120, 180, "средне", None,
    "билеты — в кассе музея-заповедника «Зарайский кремль»", "уточняйте",
    "Родовая усадьба Достоевских, где будущий писатель проводил детские летние месяцы (здесь происходит рассказ "
    "«Мужик Марей»): дом, парк, поля и рощи; входит в музей-заповедник «Зарайский кремль»",
    "Далеко (в стороне от Зарайска), нужна машина; детям интереснее после знакомства с рассказом",
    TT + "zarayske/ ; riamo.ru (музей-усадьба открыт)", acc="приблизительно, ±3 км", moscow=False,
    indoor="частично", adult=3)
add("kolomenskoe-falcon-yard", "Соколиный двор (Коломенское)", "музей", "museums,animals", "история, животные",
    "Москва, музей-заповедник «Коломенское», пр-т Андропова, 39", 55.671994, 37.680851, 6, 14, 45, 90, "спокойно",
    None, "билеты — на сайте и в кассах музея-заповедника", "вт–вс 10:00–18:00",
    "Двор царской соколиной охоты в Коломенском: рассказ о любимой забаве царя Алексея Михайловича, "
    "экскурсии «Соколиная охота царя Алексея Михайловича»; после — прогулка по Коломенскому",
    "Небольшая экспозиция — лучше совмещать с прогулкой по музею-заповеднику",
    "https://www.mgomz.ru/ru/place/sytnyi-dvor (экскурсия «Соколиная охота…»)" + O, exact=True,
    site="https://www.mgomz.ru/", adult=2)

if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    allids = {x["id"] for x in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
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
