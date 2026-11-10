"""Робот cafes, 2026-11-05: филиалы Vasilchuki Chaihona №1 и «Урюк» с детской комнатой.
Детская комната подтверждена на официальных страницах филиалов (chaihona.ru/restaurants/<...>, uryk.ru/msk/restaurants/<...>),
проверено 2026-11-05. Филиалы без упоминания детской комнаты на странице (Внуково, Депо, Европейский, БЦ Монарх,
«Урюк» Метрополис) не взяты.
Координаты: OSM (точно), если точка есть в auto/candidates.json; иначе — по уже стоящему в базе месту того же ТЦ
(«приблизительно, ±300 м») или по адресу («приблизительно, ±1 км») — уточнит geocode-address.yml.
Запуск: KP_PART=cafes python3 tools/add_cafes_1105.py"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro, SRC
from batch_helpers import P

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
CAND = {x["osm"]: x for x in json.load(open(os.path.join(ROOT, "auto", "candidates.json")))["candidates"]}
PLACES = {p["id"]: p for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
DAY = "2026-11-05"


def osm(ref):
    x = CAND[ref]
    return x["lat"], x["lon"], f"точно (OpenStreetMap {ref})"


def mall(pid, what):
    p = PLACES[pid]
    return p["lat"], p["lon"], f"приблизительно, ±300 м (по {what})"


def approx(lat, lon):
    return lat, lon, "приблизительно, ±1 км (по адресу, уточнить)"


def cafe(pid, name, addr, loc, hours, plus, minus, url, check, how=None, mt=None, tags="творчество"):
    lat, lon, acc = loc
    r = P(pid, name, "кафе", mt or metro(lat, lon), addr, lat, lon, 0, 14, 60, 150, "спокойно", tags, None,
          f"средний чек ~{check} ₽ на взрослого", hours, "да", plus, minus, adult=3, src=url, acc=acc,
          adult_price=check, booking="желательна", loud="частично", food="да", stroller="да")
    r["Сайт"] = url
    r["Категории"] = "food"
    r["День рождения"] = "да"
    r["Проверено (дата)"] = DAY
    if how:
        r["Как найти"] = how
    return r


VC = "https://chaihona.ru/restaurants/"
VC_MINUS = "Взрослый ресторан, бывает кальян и шумно вечером; детская программа — по выходным"
UR = "https://uryk.ru/msk/restaurants/"
UR_MINUS = "Детские мероприятия только по выходным; вечером ресторан взрослый"

ROWS = [
    # ---------- Vasilchuki Chaihona №1 (chaihona.ru)
    cafe("cafe-chaihona-alabyana", "Vasilchuki Chaihona №1 (Алабяна)", "ул. Алабяна, 7", approx(55.8040, 37.5150),
         "ежедневно 11:00–06:00", "Восточная кухня · детская комната с играми, аниматор по выходным", VC_MINUS,
         VC + "alabyana-7", 2250),
    cafe("cafe-chaihona-ulyanova", "Vasilchuki Chaihona №1 (Дмитрия Ульянова)", "ул. Дмитрия Ульянова, 51",
         approx(55.6880, 37.5520), "ежедневно 11:00–24:00",
         "Восточная кухня · детская комната с играми, аниматор по выходным", VC_MINUS, VC + "dmitriya-ulyanova-51", 2250),
    cafe("cafe-chaihona-zheleznodorozhny", "Vasilchuki Chaihona №1 (Железнодорожный)",
         "Балашиха, мкр Железнодорожный, ул. Пионерская, 3", approx(55.7480, 38.0100), "ежедневно 12:00–24:00",
         "Восточная кухня · большая игровая комната и детское меню", "Аниматор на странице не упомянут — уточняйте",
         VC + "vasilchuki-chaihona-no1-v-gorode-zeleznodoroznyj", 2000, mt="— (на машине / электричке)"),
    cafe("cafe-chaihona-belaya-dacha", "Vasilchuki Chaihona №1 (МЕГА Белая Дача)",
         "Котельники, 1-й Покровский пр-д, 5, ТЦ «МЕГА Белая Дача», 2 этаж",
         mall("joki-joya-mega-belaya-dacha", "ТЦ «МЕГА Белая Дача»"), "ежедневно 10:00–23:00",
         "Восточная кухня в ТЦ · детская комната, мастер-классы по выходным", VC_MINUS, VC + "trc-mega-belaa-daca", 2000,
         how="ТЦ «МЕГА Белая Дача», 2 этаж"),
    cafe("cafe-chaihona-mega-khimki", "Vasilchuki Chaihona №1 (МЕГА Химки)",
         "Химки, 8-й мкр, к1, ТЦ «МЕГА Химки», 2 этаж", mall("cafe-osteria-mega-khimki", "ТЦ «МЕГА Химки»"),
         "вс–чт 10:00–23:00; пт–сб 10:00–24:00", "Восточная кухня в ТЦ · детская комната",
         "Аниматор на странице не упомянут — уточняйте", VC + "g-himki-trc-mega", 2000, how="ТЦ «МЕГА Химки», 2 этаж"),
    cafe("cafe-chaihona-ostrov-mechty", "Vasilchuki Chaihona №1 (Остров Мечты)",
         "пр-т Андропова, 1, ТП «Остров Мечты»", mall("ostrov-mechty", "парку «Остров Мечты»"), "ежедневно 10:00–23:00",
         "Можно поесть после аттракционов · отдельная детская комната, аниматоры", VC_MINUS,
         VC + "tematiceskij-park-ostrov-mecty-pr-t-andropova-1", 2250, how="В тематическом парке «Остров Мечты»"),
    cafe("cafe-chaihona-europolis", "Vasilchuki Chaihona №1 (Европолис)", "пр-т Мира, 211, корп. 2, ТЦ «Европолис», 2 этаж",
         mall("joki-joya-rostokino", "ТЦ «Европолис»"), "ежедневно 11:00–23:00",
         "Восточная кухня в ТЦ · детская комната и детская программа по выходным", VC_MINUS, VC + "prospekt-mira-211", 2000,
         how="ТЦ «Европолис», 2 этаж"),
    cafe("cafe-chaihona-avenue", "Vasilchuki Chaihona №1 (ТРЦ «Авеню»)",
         "пр-т Вернадского, 86А, ТРЦ «Avenue Southwest», 4 этаж", approx(55.6615, 37.4790), "ежедневно 11:00–24:00",
         "Восточная кухня в ТЦ · просторная детская комната, детская программа по выходным", VC_MINUS,
         VC + "prospekt-vernadskogo-86a-trc-avenu", 2000, how="ТРЦ «Авеню», 4 этаж"),
    cafe("cafe-chaihona-afimall", "Vasilchuki Chaihona №1 (Афимолл Сити)", "Пресненская наб., 2, ТРЦ «Афимолл Сити», 5 этаж",
         mall("cin-formula-afimall", "ТРЦ «Афимолл Сити»"), "ежедневно 10:00–24:00",
         "Восточная кухня в Москва-Сити · просторная детская комната, детская программа по выходным", VC_MINUS,
         VC + "trc-afimoll-siti", 2500, how="ТРЦ «Афимолл Сити», 5 этаж"),
    cafe("cafe-chaihona-crocus", "Vasilchuki Chaihona №1 (Vegas Крокус Сити)",
         "Красногорск, ул. Международная, 12, ТРК «Vegas Крокус Сити», 2 этаж", mall("rink-vegas-city", "ТРК «Vegas Крокус Сити»"),
         "вс–чт 10:00–22:00; пт 10:00–23:00", "Восточная кухня в ТЦ · детская комната",
         "Аниматор на странице не упомянут — уточняйте", VC + "vegas-2", 2000, how="ТРК «Vegas Крокус Сити», 2 этаж"),
    cafe("cafe-chaihona-kaleidoskop", "Vasilchuki Chaihona №1 (Калейдоскоп)", "Сходненская ул., 56, ТРЦ «Калейдоскоп», 1 этаж",
         approx(55.8510, 37.4405), "вс–чт 10:00–24:00; пт–сб 10:00–02:00", "Восточная кухня в ТЦ · детская комната",
         "Аниматор на странице не упомянут — уточняйте", VC + "shodnenskaa-56", 2000, how="ТРЦ «Калейдоскоп», 1 этаж"),
    cafe("cafe-chaihona-salaris", "Vasilchuki Chaihona №1 (Саларис)", "Киевское ш., 23-й км, 1, ТРЦ «Саларис», 2 этаж",
         approx(55.6240, 37.4180), "вс–чт 10:00–22:00; пт–сб 10:00–23:00",
         "Восточная кухня в ТЦ · детская комната с играми, детская программа по выходным", VC_MINUS, VC + "trc-salaris", 2000,
         how="ТРЦ «Саларис», 2 этаж"),
    cafe("cafe-chaihona-metropolis", "Vasilchuki Chaihona №1 (Метрополис)", "Ленинградское ш., 16А, стр. 4, ТЦ «Метрополис», 3 этаж",
         approx(55.8235, 37.4970), "вс–чт 10:00–23:00; пт–сб 10:00–24:00", "Восточная кухня в ТЦ · детская комната с играми",
         "Аниматор на странице не упомянут — уточняйте", VC + "leningradskoe-sosse-16a", 2000, how="ТЦ «Метрополис», 3 этаж"),
    # ---------- «Урюк» (uryk.ru)
    cafe("cafe-uryuk-semenovskaya", "Урюк (Семёновская)", "Семёновская пл., 2", osm("node/3478320893"),
         "вс–чт 11:30–24:00; пт–сб 11:30–03:00", "Восточная кухня · детская комната, аниматоры и детские мероприятия по выходным",
         UR_MINUS, UR + "semenovskaa-plosad-2", 2000),
    cafe("cafe-uryuk-riviera", "Урюк (ТРЦ «Ривьера»)", "Автозаводская ул., 18, ТРЦ «Ривьера», 3 этаж", osm("node/4463321543"),
         "вс–чт 10:00–24:00; пт–сб 10:00–02:00", "Восточная кухня в ТЦ · детская комната, мероприятия по выходным",
         UR_MINUS, UR + "ul-avtozavodskaa-18-tc-rivera", 2000, how="ТРЦ «Ривьера», 3 этаж"),
    cafe("cafe-uryuk-shchelkovsky", "Гранд Урюк (Щёлковская)", "Щёлковское ш., 75, ТРЦ «Щёлковский», 3 этаж",
         mall("joki-joya-shchelkovsky", "ТРЦ «Щёлковский»"), "вс–чт 11:00–23:00; пт–сб 11:00–03:00",
         "Восточная кухня у автовокзала · детская игровая комната, мероприятия по выходным", UR_MINUS, UR + "selkovo", 2000,
         how="ТРЦ «Щёлковский», 3 этаж"),
    cafe("cafe-uryuk-vdnh", "Урюк (ВДНХ, «Солнце Москвы»)", "ул. 2-я Останкинская, 3, ВДНХ, у колеса «Солнце Москвы»",
         mall("solnce-moskvy", "колесу «Солнце Москвы»"), "ежедневно 11:00–23:00",
         "Поесть после прогулки по ВДНХ · детский уголок, по выходным — няня", "Детский уголок небольшой; няня только по выходным",
         UR + "restoran-uruk-na-vdnh-solnce-moskvy", 2000, how="У колеса обозрения «Солнце Москвы» на ВДНХ"),
    cafe("cafe-uryuk-evropeisky", "Урюк (ТРЦ «Европейский»)", "пл. Киевского Вокзала, 2, ТРЦ «Европейский», 3 этаж",
         osm("node/6768908024"), "ежедневно 11:00–23:00", "Восточная кухня в ТЦ · детская комната и детское меню",
         UR_MINUS, UR + "trc-evropejskij", 2000, how="ТРЦ «Европейский», 3 этаж"),
    cafe("cafe-uryuk-marshala-zhukova", "Гранд Урюк (Маршала Жукова)", "пр-т Маршала Жукова, 48, корп. 1",
         osm("node/6965829925"), "вс–чт 11:00–24:00; пт–сб 11:00–05:00",
         "Большой восточный ресторан · детское пространство, аниматоры, мероприятия по выходным", UR_MINUS,
         UR + "marsala-zukova-48k1", 2500),
    cafe("cafe-uryuk-prime-park", "Гранд Урюк (Прайм Парк)", "Ленинградский пр-т, 37/6, ЖК «Прайм Парк»",
         approx(55.7905, 37.5390), "ежедневно 11:00–02:00", "Восточная кухня у парка Ходынское поле · детская комната и анимация",
         "Детская комната указана в описании сайта — перед визитом уточните по телефону", UR + "zk-prime-park", 2500),
]

MT = {"cafe-chaihona-metropolis": "Войковская", "cafe-uryuk-riviera": "Автозаводская", "cafe-uryuk-vdnh": "ВДНХ",
      "cafe-chaihona-ulyanova": "Академическая"}
for _r in ROWS:
    _r["Метро"] = MT.get(_r["id"], _r["Метро"])

if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    ids = [r["id"] for r in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    assert not [i for i in ids if i in existing or i in PLACES], [i for i in ids if i in existing or i in PLACES]
    for row_ in ROWS:
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        r = ws.max_row + 1
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=r, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    print("rows", len(ROWS), "total", ws.max_row - 1)
