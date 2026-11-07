"""Робот fun, 2026-11-07 (после полудня): 11 мест — Дом Гоголя, центр «На Донской» (наука и техника), зооклуб
ZOOландия (Истра), музей «Еда Руси» (Жаворонки), Музей органической культуры (Коломна), музей «Усадьба Костино»
(Королёв), игровая «Непоседы» (Раменское), термы «Наутико» (Видное), керамическая студия «Все сейчас хорошо» (Ногинск),
ДШИ — музыкальный театр и ДК «Мир» (Реутов).
Источники: кэш auto/pages (domgogolya.ru, dnttm.su, travelto.ru/blog/kuda-shodit-s-detmi-v-* — сентябрь 2026)
+ точки OSM из auto/candidates.json. Без OSM-точки — приблизительно по адресу (уточнит сверка osm-local).
Дубли проверены по places.json и data/parts/*.xlsx. Иконки — tools/icons_fun_1107d.py.
Запуск: KP_PART=fun python3 tools/add_fun_1107d.py"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC
from add_batch14 import metro

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DAY = "2026-11-07"
TT = "https://travelto.ru/blog/kuda-shodit-s-detmi-v-"
ROWS = []


def add(pid, name, typ, cats, tags, addr, lat, lon, a0, a1, d0, d1, energy, price, note, hours, plus, minus,
        src, exact=False, acc=None, indoor="да", adult=2, booking="не нужна", sit="нет", dark="нет", loud="нет",
        food="нет", season=None, stroller="частично", crowd="частично", moscow=True, site=""):
    m = metro(lat, lon) if moscow else "— (на машине / электричке)"
    r = P(pid, name, typ, m, addr, lat, lon, a0, a1, d0, d1, energy, tags, price, note, hours, indoor, plus, minus,
          adult=adult, src=src, acc="точно (OpenStreetMap)" if exact else (acc or "приблизительно, ±1 км"),
          booking=booking, sit=sit, dark=dark, loud=loud, food=food, season=season, stroller=stroller, crowd=crowd)
    r["Сайт"] = site
    r["Категории"] = cats
    r["Проверено (дата)"] = DAY
    ROWS.append(r)


def show(pid, name, addr, lat, lon, a0, plus, minus, src, site, typ="театр", note="билеты — на сайте театра",
         hours="по афише", **kw):
    add(pid, name, typ, "shows", kw.pop("tags", "театр, музыка"), addr, lat, lon, a0, 14, 60, 150, "спокойно", None,
        note, hours, plus, minus, src, sit="да", dark="частично", booking="обязательна", stroller="нет", site=site,
        adult=kw.pop("adult", 3), **kw)



# ===================== Москва =====================
add("gogol-house", "Дом Н. В. Гоголя — мемориальный музей", "музей", "museums", "литература, история",
    "Москва, Никитский бульвар, 7А", 55.754145, 37.599814, 7, 14, 45, 90, "спокойно", None,
    "цены — на сайте музея; действует «Пушкинская карта»",
    "вт, ср, пт 12:00–19:00; чт 14:00–21:00; сб, вс 12:00–18:00; пн — выходной",
    "Дом, где Гоголь прожил последние годы: мемориальные комнаты, камин, у которого он сжёг второй том «Мёртвых душ», "
    "выставки и семейные программы; рядом — двор с памятником писателю",
    "Малышам скучновато — лучше со школьниками и экскурсоводом", "https://www.domgogolya.ru/ ; OpenStreetMap",
    exact=True, adult=3, site="https://www.domgogolya.ru/")
add("na-donskoy-center", "Центр «На Донской» (ДНТТМ) — техника и наука для детей", "центр творчества",
    "science,masterclass", "наука и техника, творчество", "Москва, ул. Донская, 37", 55.718888, 37.605215, 7, 14,
    60, 120, "средне", None, "условия и запись — на сайте центра", "по расписанию занятий",
    "Городской центр технического творчества: математика, робототехника, электроника, инженерное моделирование, "
    "химия, нейросети и 3D; есть программы «Каникулы с пользой»",
    "Это кружки и курсы, а не музей: приходить — на конкретное занятие по записи", "http://dnttm.su",
    exact=True, booking="обязательна", site="http://dnttm.su")

# ===================== Подмосковье =====================
add("zoolandiya-istra", "Семейный зооклуб ZOOландия (Истра)", "контактный зоопарк", "animals", "животные, природа",
    "Истринский г. о., зооклуб «ZOOландия»", 55.8802, 36.7952, 1, 12, 90, 150, "средне", None,
    "цены — уточняйте у зооклуба", None,
    "Семейный зооклуб: знакомство с животными и отдельная детская игровая площадка — хороший выезд с дошкольником",
    "Перед поездкой проверьте график — работает не каждый день одинаково",
    TT + "istre/ ; afisha.ru/istra/park/zoolandiya-21453", exact=True, indoor="частично", moscow=False,
    stroller="частично")
add("eda-rusi-zhavoronki", "Интерактивный музей «Еда Руси» (Жаворонки)", "музей", "museums,masterclass",
    "история, еда, творчество", "г. о. Химки, д. Жаворонки (рядом с усадьбой Середниково)", 56.0005, 37.2010, 3, 14,
    120, 180, "средне", None, "цены — по программе", "по записи",
    "Музей русской кухни: костюмированные программы с Домовым и Василисой, устройство русской печи и кулинарные "
    "мастер-классы; отдельные программы для 3–6 лет и для школьников",
    "Без брони не принимают — записывайтесь заранее", TT + "himkah/ ; sputnik8.com (экскурсия Середниково — "
    "Жаворонки — «Еда Руси»)", acc="приблизительно, ±2 км", booking="обязательна", moscow=False, adult=3)
add("kolomna-organic-culture", "Музей органической культуры (Коломна)", "музей", "museums", "искусство, фотография",
    "Коломна, ул. Казакова, 10", 55.1047, 38.7598, 12, 14, 60, 90, "спокойно", None, "цены — уточняйте", None,
    "Несколько площадок с искусством XX–XXI веков, фотографией и сменными выставками — другая Коломна для подростка",
    "Малышам будет скучно: содержание абстрактное", TT + "kolomne/", moscow=False, adult=3)
add("korolev-usadba-kostino", "Музей «Усадьба Костино» (Королёв)", "музей", "museums", "история",
    "Королёв, ул. Ильича, 1", 55.9318, 37.8125, 8, 14, 45, 90, "спокойно", None, "цены — уточняйте",
    "режим — у музейного объединения Королёва",
    "Историческая усадьба и экспозиция о Болшевской трудовой коммуне; после экскурсии — прогулка по парку «Костино»",
    "Тема сложная для дошкольника — лучше со школьником и экскурсоводом", TT + "koroleve/", moscow=False)
add("ramenskoe-neposedy", "Игровая комната «Непоседы» (ТЦ «Сириус», Раменское)", "игровая комната", "playcenters",
    "игры", "Раменское, ул. Гурьева, ТЦ «Сириус»", 55.5717, 38.2405, 1, 7, 60, 120, "активно", None,
    "цены — у администратора", "по режиму ТЦ",
    "Игровая для дошкольников и младших школьников в торговом центре — остановка в дождь или после прогулки",
    "Обычная игровая: ехать специально ради неё не стоит", TT + "ramenskom/", moscow=False, loud="да", adult=1)
add("vidnoe-nautiko", "Термы «Наутико» (Видное)", "термальный комплекс", "water", "вода, спорт и активность",
    "Видное, Олимпийская ул., 6, корп. 1", 55.5515, 37.7120, 3, 14, 120, 240, "средне", None,
    "цены — на сайте комплекса", None,
    "Крытый детский бассейн, взрослые бассейны и подогреваемая открытая зона — семейный день в тепле",
    "Для детей есть отдельные правила посещения водных и термальных зон — прочитайте до поездки",
    TT + "vidnom/", moscow=False, booking="желательна", food="частично")
add("noginsk-vse-horosho", "Керамическая студия «Все сейчас хорошо» (Ногинск)", "мастерская", "masterclass",
    "творчество", "Ногинск, Рабочая ул., 30", 55.8555, 38.4405, 5, 14, 60, 120, "спокойно", None,
    "цены — по мастер-классу", "по расписанию мастер-классов",
    "Керамика и ручная лепка для детей и взрослых; есть занятия, куда можно прийти вместе с ребёнком",
    "Только по записи на конкретный мастер-класс", TT + "noginske/", booking="обязательна", moscow=False)
show("reutov-music-theatre", "Детская школа искусств — музыкальный театр (Реутов)", "Реутов, Южная ул., 5",
     55.7502, 37.8618, 3,
     "Необычная школа-театр: дети 4–17 лет учатся музыке, хореографии и актёрскому мастерству и играют спектакли",
     "Приходить — на конкретный спектакль или концерт из афиши", TT + "reutove/ ; muz-teatr.ru", "http://muz-teatr.ru",
     exact=True, moscow=False, tags="театр, музыка", adult=2)
show("reutov-dk-mir", "ДК «Мир» (Реутов) — детские спектакли и шоу", "Реутов, ул. Победы, 20", 55.7650, 37.8605, 3,
     "Главная концертная площадка Реутова: гастрольные спектакли, музыкальные сказки и семейные представления; "
     "рядом — парк ДК «Мир» с площадками", "Есть и взрослые события — смотрите возрастную маркировку",
     TT + "reutove/", "", moscow=False, typ="концертный зал", tags="театр, музыка", adult=2)

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
