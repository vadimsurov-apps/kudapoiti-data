"""Робот fun, 2026-11-09 (вечер, 5-й проход). Поиск по районам (Кутузовская, Крылатское, Марьино, Медведково,
Мичуринский пр-т, Коммунарка, Ступино, Коломна и др.) + справочник jsprav.ru; каждое место подтверждено сайтом
(auto/pages: a4kidscity-ru, irbis-studio-ru, sdelal-sam-com, chudesa-maryino-tilda-ws, www-clever-kids-ru,
www-myvmesteschool-ru, ostrovdetstva-stupino-orgs-biz, xn-80aaouofezt-xn-p1ai) или карточкой 2ГИС в поиске.
Координаты приблизительные — точку по адресу поправит сверка с OSM. Иконки — tools/icons_fun_1109f.py.
Запуск: KP_PART=fun python3 tools/add_fun_1109f.py"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC
from add_batch14 import metro

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DAY = "2026-11-09"
ROWS = []


def add(pid, name, typ, cats, tags, addr, lat, lon, a0, a1, d0, d1, energy, plus, minus, q,
        price=None, note="цены — уточняйте", hours="уточняйте", acc=None, indoor="да", adult=1,
        booking="желательна", sit="нет", dark="нет", loud="нет", food="нет", stroller="частично",
        crowd="частично", moscow=True):
    m = metro(lat, lon) if moscow else "— (на машине / электричке)"
    r = P(pid, name, typ, m, addr, lat, lon, a0, a1, d0, d1, energy, tags, price, note, hours, indoor, plus, minus,
          adult=adult, src=q, acc=acc or "приблизительно, ±500 м",
          booking=booking, sit=sit, dark=dark, loud=loud, food=food, stroller=stroller, crowd=crowd)
    r["Сайт"] = ""
    r["Категории"] = cats
    r["Проверено (дата)"] = DAY
    ROWS.append(r)


KM = "приблизительно, ±1 км"
PLAY = dict(energy="активно", loud="да", stroller="да")
STUDIO = dict(energy="спокойно", booking="обязательна", sit="частично", stroller="нет")
QUEST = dict(energy="средне", booking="обязательна", dark="частично", stroller="нет", crowd="нет")


def play(pid, name, addr, lat, lon, plus, minus, q, a0=1, a1=8, **kw):
    add(pid, name, "игровая комната", "playcenters", "спорт и активность", addr, lat, lon, a0, a1, 60, 180,
        plus=plus, minus=minus, q=q, **{"note": "оплата по времени — уточняйте тарифы", **PLAY, **kw})


def studio(pid, name, addr, lat, lon, plus, minus, q, a0=4, a1=14, typ="творческая студия", cats="masterclass",
           tags="творчество", **kw):
    add(pid, name, typ, cats, tags, addr, lat, lon, a0, a1, 60, 120, plus=plus, minus=minus, q=q,
        **{"note": "разовые мастер-классы и абонементы — уточняйте", "hours": "по расписанию занятий", **STUDIO, **kw})


def quest(pid, name, addr, lat, lon, plus, minus, q, a0=7, a1=14, **kw):
    add(pid, name, "квест", "quests", "загадки и приключения", addr, lat, lon, a0, a1, 60, 120, plus=plus,
        minus=minus, q=q, **{"note": "цена за команду — уточняйте", "hours": "по записи", "adult": 2, **QUEST, **kw})





M300 = "приблизительно, ±300 м (тот же ТЦ)"
M = lambda a: f"детская игровая комната метро {a}"
QQ = lambda a: f"квест для детей метро {a}"
T = lambda a: f"творческая студия для детей метро {a}"
MK = lambda a: f"мастер-класс для детей метро {a}"
OBL = dict(moscow=False, acc=KM)
IRB = "сайт irbis-studio.ru (филиалы, 09.11.2026)"


def irbis(pid, name, addr, lat, lon, how, plus):
    studio(pid, name, addr, lat, lon, plus,
           "Регулярные занятия раз в неделю по 2–3 часа, нужна запись; помещение арендованное — ищите по описанию входа",
           IRB, a0=4, a1=16, typ="театральная студия", cats="masterclass", tags="сказки и театр, творчество", hours="по расписанию групп")
    ROWS[-1]["Как найти"] = how


add("a4-kids-city-columbus", "Город профессий и челленджей A4 Kids City (Columbus)", "город профессий", "playcenters,masterclass",
    "творчество, спорт и активность", "Кировоградская ул., 13А, МФК «Columbus», 3 этаж", 55.6115, 37.6069, 4, 13, 120, 240, "активно",
    "Детский город профессий от команды блогера Влада А4: маршрут из профессий и челленджей (совместно со Сбером), дни рождения",
    "Билеты по времени, в выходные людно", "сайт a4kidscity.ru (09.11.2026); Афиша, KudaGo",
    acc="приблизительно, ±300 м (тот же ТЦ)", note="билеты на сайте — уточняйте тарифы", hours="ежедневно, уточняйте",
    booking="желательна", loud="да", food="частично", stroller="частично", crowd="да", adult=1)
ROWS[-1]["Как найти"] = "Этаж: 3, МФК «Columbus»"

studio("sdelal-sam-kutuzovsky", "Детская столярная мастерская «Сделал Сам»", "Кутузовский пр-т, 36, стр. 4", 55.7418, 37.5300,
       "Настоящие инструменты и дерево: разовые мастер-классы с готовой поделкой домой, регулярные занятия и праздники",
       "С 7 лет, нужна запись", "сайт sdelal-sam.com (09.11.2026)", a0=7, a1=14, typ="мастерская")
studio("chudesa-maryino", "Детский центр «Чудеса» (Марьино)", "ул. Верхние Поля, 24", 55.6630, 37.7470,
       "Тематические мастер-классы по выходным (афиша на месяц на сайте) и кружки для малышей от 3 лет",
       "Мастер-классы по записи, места ограничены", "сайт chudesa.maryino.tilda.ws (афиша ноября 2026)", a0=3, a1=10,
       typ="детский центр")
studio("clever-kids-chelyuskinskaya", "Семейный клуб «Клевер» (Медведково)", "Челюскинская ул., 9", 55.8838, 37.6735,
       "Каллиграфия, театральная студия, «малышники» и раннее развитие; летний клуб",
       "Переехал с Челюскинской, 13 на дом 9 — ориентируйтесь на новый адрес", "сайт clever-kids.ru (09.11.2026)",
       a0=1, a1=12, typ="детский центр")
studio("my-vmeste-michurinsky", "Центр развития «Мы вместе» (Мичуринский проспект)", "Мичуринский пр-т, 39", 55.6930, 37.4985,
       "Театральная студия 3–14 лет, живопись 3–12 лет, вокал, клуб настольных игр от 9 лет, развивающие группы 2–6 лет",
       "Занятия по абонементу, нужна запись", "сайт myvmesteschool.ru (09.11.2026)", a0=2, a1=14, typ="детский центр")
irbis("irbis-kutuzovskaya", "Детская театральная студия «Ирбис» (Кутузовская)", "Кутузовский пр-т, 36, стр. 51", 55.7400, 37.5285,
      "Вход: от м. «Кутузовская» выход 4, через подземный переход (подробно — на сайте студии)",
      "Актёрское мастерство в группах 4–5, 6–8, 9–12 и 13–16 лет, спектакли и театральные сборы на каникулах")
irbis("irbis-bratislavskaya", "Детская театральная студия «Ирбис» (Братиславская)", "Братиславская ул., 21, корп. 2", 55.6575, 37.7490,
      "Вход: двухэтажное здание во дворе за домом 19к1 (ориентир — «Пятёрочка»), со стороны детской площадки у кафе «Дом кебаба»\nОриентир: под вывеской «#танцы» две двери — левая",
      "Театральные группы для детей и подростков рядом с метро, зимние и летние театральные интенсивы")
irbis("irbis-krylatskoe", "Детская театральная студия «Ирбис» (Крылатское)", "Крылатская ул., 33, корп. 3", 55.7605, 37.4170,
      "Ориентир: супермаркет «Верный» — обойти справа; от м. «Крылатское» ~15 минут пешком",
      "Актёрское мастерство, сценическая речь и пластика в группах по возрасту, показы спектаклей для родителей")
irbis("irbis-babushkinskaya", "Детская театральная студия «Ирбис» (Бабушкинская)", "ул. Лётчика Бабушкина, 17, корп. 1", 55.8717, 37.6633,
      "Вход: здание торцом с вывесками «Фитнес клуб» и «Автошкола»\nЭтаж: 2, помещение студии «Факультет ПРО»",
      "Театральные группы 4–16 лет у метро «Бабушкинская», каникулярные театральные сборы")
play("palana-kommunarka", "Детская игровая комната «Палана» (ЖК «Москва А101»)", "пос. Коммунарка, Бачуринская ул., 17", 55.5500, 37.4930,
     "Игровая для малышей прямо в квартале ЖК «Москва А101» — удобно жителям Коммунарки",
     "Небольшая, часы и тарифы уточняйте", "карточка 2ГИС (поиск 09.11.2026)", a0=1, a1=7)
play("ostrov-detstva-stupino", "Детский игровой комплекс «Остров детства» (Ступино)", "Ступино, Пристанционная ул., 6, 1 этаж", 54.8925, 38.0710,
     "Батуты и лабиринты, комната для праздников; по отзывам всё в хорошем состоянии",
     "По выходным людно на днях рождения", "сайт ostrovdetstva--stupino.orgs.biz (09.11.2026); справочник jsprav.ru", a0=1, a1=10, **OBL)
studio("zavatsky-pottery-kolomna", "Гончарная мастерская Завацких (арт-квартал «Патефонка», Коломна)", "Коломна, ул. Уманская, 3Д", 55.0880, 38.7740,
       "Семейная гончарная мастерская: гончарный круг и лепка, мастер-классы для детей вместе с родителями",
       "Нужна запись; изделия забирают после обжига", "сайт патефонка.рф (09.11.2026); справочник jsprav.ru", a0=5, a1=14,
       typ="мастерская", **OBL)
SITES = {"a4-kids-city-columbus": "https://a4kidscity.ru/", "sdelal-sam-kutuzovsky": "https://sdelal-sam.com/",
         "chudesa-maryino": "http://chudesa.maryino.tilda.ws/", "clever-kids-chelyuskinskaya": "https://www.clever-kids.ru/",
         "my-vmeste-michurinsky": "https://www.myvmesteschool.ru/", "irbis-kutuzovskaya": "https://irbis-studio.ru/filialy/kutuzovskaya/",
         "irbis-bratislavskaya": "https://irbis-studio.ru/", "irbis-krylatskoe": "https://irbis-studio.ru/", "irbis-babushkinskaya": "https://irbis-studio.ru/",
         "ostrov-detstva-stupino": "https://ostrovdetstva--stupino.orgs.biz/", "zavatsky-pottery-kolomna": "https://xn--80aaouofezt.xn--p1ai/"}
for _r in ROWS:
    _r["Сайт"] = SITES.get(_r["id"], "")

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
