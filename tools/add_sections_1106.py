"""Робот sections, 2026-11-06 (ночь): балет и детские танцы, единоборства, гимнастика, волейбол, теннис, бадминтон.
Источники — официальные сайты сетей (WebSearch → WebFetch, проверено 2026-11-06):
 балет BALLETA (балета.рф), ГРАНДБАЛЕТ grand-ballet.ru, «Гармония» balletschoolharmony.ru, «Высота» (высота-бальные.москва),
 Energy energy-studio.ru, Данко danco-studio.ru, «РИТМ» danceritm.ru; «Школа чемпионов» schoolofchampions.msk.ru,
 Sambi.st, «Мицудэн» mitsuden.ru, «Кайдзен» centerkaizen.com, «Союз-Спорт» ssport.ru, «ДелоСпорт» (делоспорт.рф),
 tkd-otradnoe.ru; гимнастика Перевозникова (гимнастика.рф/shkoly), art-gym.ru, msk.gymbalance.ru; rusvolley.ru/kids,
 playpark.moscow, fit-l.com.
Координаты — по станции метро из адреса («приблизительно»), уточнит geocode-address.yml.
Запуск: KP_PART=sections python3 tools/add_sections_1106.py [--dry]"""
import json, os, math, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import base, metro, MET, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ST = {n.lower().replace("ё", "е"): (a, b) for n, a, b in MET}
SRC_OK = "сайт места (проверено 2026-11-06)"
APPROX = "приблизительно, ±1 км (по станции метро)"
_used = {}


def at(st):
    a, b = ST[st.lower().replace("ё", "е")]
    k = _used.get(st, 0); _used[st] = k + 1
    if k:
        ang = k * 2.1; a += 0.0012 * math.sin(ang); b += 0.002 * math.cos(ang)
    return round(a, 6), round(b, 6), st, APPROX


def near(lat, lon, label="приблизительно, ±2 км (по адресу)"):
    return lat, lon, metro(lat, lon), label


def row(pid, name, typ, loc, addr, a0, a1, d0, d1, tags, price, note, hours, plus, minus, site, cats, src=SRC_OK):
    lat, lon, mt, acc = loc
    r = base(pid, name, typ, lat, lon, a0, a1, d0, d1, "активно", tags, price, note, hours, "да", plus, minus,
             site, cats, addr=addr, booking="обязательна", food="нет", adult=1)
    r["Метро"] = mt; r["Точность координат"] = acc; r["Источник"] = src
    r["Проверено (дата)"] = "2026-11-06"
    return r


ROWS = []
SPORT = "спорт и активность"
MUS = "музыка, спорт и активность"
DANCE, BAL = "танцевальная студия", "балетная школа"
SEC = "спортивная секция"

# ---------------- Балет и танцы ----------------
for slug, addr, loc in [("ovchinnikovsky", "Большой Овчинниковский пер., 24, стр. 5", at("Новокузнецкая")),
                        ("borisovsky", "Борисовский пр-д, 22, корп. 1, стр. 2", at("Шипиловская")),
                        ("krasnogorsk", "Красногорск, Подмосковный б-р, 12", near(55.8285, 37.3820))]:
    ROWS.append(row(f"balleta-{slug}", f"Школа балета BALLETA ({addr.split(',')[0]})", BAL, loc, addr, 3, 16, 45, 60, MUS,
                    1125, "пробное занятие бесплатно; 4 занятия — 4500 ₽/мес, 8 — 6000 ₽/мес", None,
                    "Классический балет для девочек 3–16 лет, группы по возрасту, пробное бесплатно",
                    "Группы в основном для девочек; запись заранее", "https://xn--80aaacv0ahdw0c3c.xn--p1ai/", "dance"))

for slug, addr, st, a0 in [("smolenskaya", "пер. Каменная Слобода, 7", "Смоленская", 2),
                           ("shabolovka", "ул. Шаболовка, 31Г (вход со стороны Конного пер.)", "Шаболовская", 3)]:
    ROWS.append(row(f"grandballet-{slug}", f"Школа балета «ГрандБалет» ({addr.split(',')[0]})", BAL, at(st), addr, a0, 14,
                    45, 60, MUS, None, "пробное занятие — по записи; цены — у администратора", None,
                    "Русская школа искусств Марии Володиной: классический балет и современная хореография, малыши — вместе с мамой",
                    "Цены на сайте не опубликованы", "https://grand-ballet.ru/", "dance"))

HARM = [("kapitoliy", "пр-т Вернадского, 6 (ТЦ «Капитолий»)", "Университет"),
        ("profsoyuznaya", "Профсоюзная ул., 96", "Беляево"),
        ("stoletova", "ул. Столетова, 11", "Раменки"),
        ("vinnitskaya", "Винницкая ул., 4", "Раменки"),
        ("leninsky", "Ленинский пр-т, 99", "Новаторская"),
        ("michurinsky", "Мичуринский пр-т, 56 (детский центр «Мастерская Олли»)", "Мичуринский проспект"),
        ("bolotnikovskaya", "Болотниковская ул., 52, корп. 4", "Зюзино"),
        ("vargi", "ул. Академика Варги, 38", "Теплый Стан"),
        ("ushakova", "б-р Адмирала Ушакова, 12", "Улица Скобелевская")]
for slug, addr, st in HARM:
    ROWS.append(row(f"harmony-ballet-{slug}", f"Школа балета «Гармония» ({addr.split(' (')[0].split(',')[0]})", BAL, at(st), addr,
                    2, 16, 45, 60, MUS, 1250, "абонемент — от 1250 ₽ за занятие", None,
                    "Детская хореография с 2–3 лет, классический балет и балетная гимнастика для школьников",
                    "Какие возрастные группы в этом филиале — уточняйте у администратора",
                    "https://balletschoolharmony.ru/", "dance"))

VYS = [("yablochkova", "ул. Яблочкова, 24А, 2 этаж", at("Фонвизинская")),
       ("timiryazevskaya", "Тимирязевская ул., 1, стр. 2, 8 этаж", at("Дмитровская")),
       ("tatyanin-park", "ул. Татьянин Парк, 19, корп. 1, 2 этаж", at("Говорово")),
       ("vavilova", "ул. Вавилова, 81, корп. 1", at("Профсоюзная")),
       ("korolev-gelios", "Королёв, пр-т Космонавтов, 20А (ОДЦ «Гелиос»)", near(55.9205, 37.8360)),
       ("korolev-kalinina", "Королёв, ул. Терешковой, 1 (ЦДК им. Калинина)", near(55.9160, 37.8255))]
for slug, addr, loc in VYS:
    ROWS.append(row(f"vysota-ballroom-{slug}", f"Школа бальных танцев «Высота» ({'Королёв, ' + addr.split(', ')[1] if addr.startswith('Королёв') else addr.split(',')[0]})",
                    DANCE, loc, addr, 3, 12, 45, 60, MUS, 625, "абонемент — от 625 ₽ за занятие", None,
                    "Спортивные бальные танцы для мальчиков и девочек: группы 3–4, 5–7 и 8–12 лет",
                    "Нужна пара — тренеры помогают подобрать партнёра", "https://xn--80aiaeayko7bg3bydwc.xn--80adxhks/", "dance"))

EN = [("otradnoe", "ул. Декабристов, 27, 6 этаж", "Отрадное"), ("dezhneva", "пр-д Дежнёва, 29, корп. 1, 5 этаж", "Бабушкинская"),
      ("kompas", "ул. Красная Сосна, 2А (ТЦ «Компас»), 2 этаж", "Ростокино"),
      ("green-park", "Сельскохозяйственная ул., 35 (ЖК Green Park)", "Ботанический сад")]
for slug, addr, st in EN:
    ROWS.append(row(f"energy-dance-{slug}", f"Танцевальная студия Energy ({addr.split(' (')[0].split(',')[0]})", DANCE, at(st), addr,
                    3, 17, 55, 60, MUS, None, "цены — у администратора студии", None,
                    "Детская хореография с 3 лет, хип-хоп, брейк, K-pop и современные танцы до 17 лет",
                    "Цены на сайте не опубликованы", "https://www.energy-studio.ru/", "dance"))

for slug, addr, st in [("sokolniki", "Сокольнический Вал, 1Б (вход «Трибуна Б»), 4 этаж", "Сокольники"),
                       ("pyataya-avenu", "ул. Маршала Бирюзова, 32 (ТРЦ «Пятая Авеню»), 3 этаж", "Октябрьское поле"),
                       ("mira", "пр-т Мира, 101, стр. 2", "Алексеевская")]:
    ROWS.append(row(f"danco-break-{slug}", f"Школа танцев «Данко» — детский брейк ({addr.split(' (')[0].split(',')[0]})", DANCE, at(st),
                    addr, 8, 16, 60, 60, MUS, None, "пробное занятие — по записи", "2 раза в неделю по 60 минут",
                    "Детский брейк-данс в небольших группах, с 8 лет", "Цены на странице не указаны",
                    "https://danco-studio.ru/kids/break-dance", "dance"))

for slug, addr, st in [("arena-plaza", "Ленинградский пр-т, 36 (ТЦ «Арена Плаза»), 1 этаж", "Динамо"),
                       ("tbilisi", "Новочерёмушкинская ул., 53А (ТЦ «Тбилиси»), 3 этаж", "Профсоюзная"),
                       ("shchuka", "Щукинская ул., 42 (ТЦ «Щука»), 4 этаж", "Щукинская")]:
    ROWS.append(row(f"ritm-dance-{slug}", f"Танцевальная школа «Ритм» ({addr.split('«')[1].split('»')[0]})", DANCE, at(st), addr,
                    3, 16, 45, 60, MUS, 500, "занятия — от 500 ₽", None,
                    "Ритмика с 3 лет и больше 20 детских танцевальных направлений до 16 лет",
                    "Цена «от» — за занятие по абонементу", "https://danceritm.ru/tancy-dlya-detej", "dance"))

# ---------------- Единоборства ----------------
SC = [("skandinavia", "пос. Коммунарка, Скандинавский б-р, 6 (ЖК «Скандинавия»)", near(55.5690, 37.4880), 4, 16, 8000, "page71686957"),
      ("skandinavia-yug", "пос. Коммунарка, Скандинавский б-р, 19 (ЖК «Скандинавия»)", near(55.5655, 37.4850), 4, 15, 8000, "page71431419"),
      ("litvina-sedogo", "ул. Литвина-Седого, 3А", at("Улица 1905 года"), 3, 16, 10000, "page71687265"),
      ("lyublinsky-park", "Люблинская ул., 76, корп. 5 (ЖК «Люблинский парк»)", at("Люблино"), 4, 15, 8000, "page71687337"),
      ("sreda", "Рязанский пр-т, 2/1, корп. 4 (ЖК «Среда»)", at("Рязанский проспект"), 4, 15, 9000, "page71687447"),
      ("butovo-park", "Ленинский г.о., ЖК «Бутово парк», корп. 18, корп. 1, 3 этаж", near(55.5400, 37.5850), 3, 15, 6000, "page71687493")]
TT = {"skandinavia": "Скандинавский б-р, 6", "skandinavia-yug": "Скандинавский б-р, 19", "litvina-sedogo": "ул. Литвина-Седого",
      "lyublinsky-park": "ЖК «Люблинский парк»", "sreda": "ЖК «Среда»", "butovo-park": "ЖК «Бутово парк»"}
for slug, addr, loc, a0, a1, p, page in SC:
    ROWS.append(row(f"school-champions-{slug}", f"«Школа чемпионов» — самбо и дзюдо ({TT[slug]})",
                    SEC, loc, addr, a0, a1, 60, 60, SPORT, 1000, f"первое занятие бесплатно; 8 занятий — {p} ₽", None,
                    "Самбо и дзюдо для детей в залах рядом с домом, группы по возрасту, первое занятие бесплатно",
                    "Группы небольшие — запись заранее", f"https://schoolofchampions.msk.ru/{page}.html", "martial"))
ROWS.append(row("sambist-bauman", "Школа самбо Sambi.st (МГТУ им. Баумана) — детские группы", SEC, at("Бауманская"),
                "Госпитальная наб., 4, стр. 1", 4, 15, 60, 90, SPORT, 1500, "разовое занятие 1500 ₽; месяц — 5400–9000 ₽", None,
                "Самбо для детей 4–6, 7–10 и 10–15 лет при спорткомплексе МГТУ", "Вход по пропуску — встречают у входа",
                "https://sambi.st/", "martial"))
ROWS.append(row("sambist-podolsk", "Школа самбо Sambi.st (Подольск) — детские группы", SEC, near(55.4300, 37.5450, "приблизительно, ±3 км (по району)"),
                "Подольск, Бородинский б-р, 7 (фитнес-клуб World-Body)", 5, 13, 60, 60, SPORT, None,
                "цены — у тренера", None, "Детское самбо в Подольске: младшая и старшая группы",
                "Цены не опубликованы", "https://sambi.st/", "martial"))

MIT = [("basmannaya", "Старая Басманная ул., 36, стр. 2 (центральный додзё)", "Бауманская", 4, 17),
       ("chertanovskaya", "Чертановская ул., 30, корп. 1", "Южная", 5, 14),
       ("pereyaslavskaya", "Переяславская ул., 8А", "Рижская", 6, 18),
       ("glinisty", "Глинистый пер., 7, стр. 1", "Рижская", 6, 11),
       ("kaspiyskaya", "Каспийская ул., 20, корп. 1", "Царицыно", 7, 14),
       ("donskaya", "Донская ул., 6, стр. 1", "Октябрьская", 3, 14)]
for slug, addr, st, a0, a1 in MIT:
    ROWS.append(row(f"mitsuden-{slug}", f"Каратэ «Мицудэн» ({addr.split(' (')[0].split(',')[0]})", SEC, at(st), addr, a0, a1,
                    60, 90, SPORT, None, "стоимость — у тренера зала", None,
                    "Каратэ кёкусинкай для детей: группы по возрасту, аттестации на пояса",
                    "Цены и расписание — у тренера конкретного зала", "https://mitsuden.ru/karate-v-moskve/", "martial"))

for slug, addr, st, a0, p in [("leskova", "ул. Лескова, 14", "Бибирево", 4, 7200),
                              ("mira", "пр-т Мира, 188Б, корп. 1", "Ботанический сад", 6, 7000),
                              ("bolotnikovskaya", "Болотниковская ул., 52, корп. 3", "Нахимовский проспект", 7, 7000)]:
    ROWS.append(row(f"kaizen-{slug}", f"Центр каратэ «Кайдзен» ({addr.split(',')[0]})", SEC, at(st), addr, a0, 14, 60, 90, SPORT,
                    0, f"пробная тренировка бесплатно; абонемент от {p} ₽/мес", None,
                    "Каратэ кёкусинкай для детей, бесплатная пробная тренировка, экипировка на первое занятие не нужна",
                    "Группы малышей есть не во всех залах", "https://www.centerkaizen.com/", "martial"))

ROWS.append(row("soyuz-sport-volgina", "«Союз-Спорт» — детский бокс и тхэквондо", SEC, at("Калужская"),
                "ул. Академика Волгина, 33А", 4, 17, 60, 90, SPORT, 1000, "пробное 1000 ₽; бокс — 7000 ₽/мес (2 раза в неделю)", None,
                "Бокс для детей с 6 лет и тхэквондо для малышей с 4 лет в одном клубе", "Цены — на сезон 2026/27",
                "https://www.ssport.ru/detskij_klub/boks/", "martial"))
ROWS.append(row("delosport-boxing", "«ДелоСпорт» — детский бокс (Фили)", SEC, at("Фили"), "Большая Филёвская ул., 20", 6, 16, 60, 60,
                SPORT, 1200, "разовое 1200 ₽, по абонементу — 1000 ₽ за занятие", None,
                "Бокс для детей с 6 лет в детской экипировке", "Запись заранее", "https://xn--d1acsmafifm.xn--p1ai/deti/boks", "martial"))
ROWS.append(row("tkd-otradnoe", "Зал единоборств «Отрадное» — тхэквондо", SEC, at("Отрадное"), "Отрадная ул., 8", 5, 16, 60, 90,
                SPORT, None, "цены — у тренера", None, "Тхэквондо для детей: игровые группы 5–7 лет и соревновательные",
                "Цены на сайте не опубликованы", "https://www.tkd-otradnoe.ru/", "martial"))

# ---------------- Гимнастика ----------------
PER = [("izmaylovo", "Сиреневый б-р, 4, стр. 1 (РУС «ГЦОЛИФК»)", at("Измайловская")),
       ("kosino", "Большая Косинская ул., 5А (СК «Атлант»)", at("Новокосино")),
       ("yurlovsky", "Юрловский пр-д, вл. 6", near(55.8790, 37.6110)),
       ("solntsevo", "ул. Щорса, 6", at("Солнцево")),
       ("shcherbinka", "Щербинка, Индустриальная ул., 2", near(55.5030, 37.5660)),
       ("mgsu", "Ярославское ш., 26, стр. 16 (Дворец спорта МГСУ)", near(55.8655, 37.7045)),
       ("yasenevo", "Новоясеневский пр-т, 26", at("Ясенево")),
       ("balashikha", "Балашиха, мкр Заря, Молодёжная ул., 22 (СК «Метеор»)", near(55.7960, 37.9250, "приблизительно, ±3 км (по району)")),
       ("mytishchi", "Мытищи, Силикатная ул., 28/2", near(55.9190, 37.7560))]
for slug, addr, loc in PER:
    ttl = addr.split(" (")[0].split(",")[0] if not addr.split(",")[0] in ("Щербинка", "Балашиха", "Мытищи") else addr.split(",")[0]
    ROWS.append(row(f"perevoznikov-gym-{slug}", f"Школа спортивной гимнастики Андрея Перевозникова ({ttl})", SEC, loc, addr, 3, 14,
                    60, 90, SPORT, 0, "первое занятие бесплатно; абонемент — у администратора", None,
                    "Спортивная гимнастика для мальчиков и девочек с 3 лет: снаряды, акробатика, растяжка",
                    "Цены абонементов на сайте не опубликованы", "https://xn--80af1bf8a.xn--p1ai/shkoly/", "gymnastics"))

for slug, addr, st in [("stromynka", "ул. Стромынка, 20А", "Сокольники"),
                       ("neptun", "Федеративный пр-т, 8А, стр. 1 (ФОК «Нептун»)", "Перово"),
                       ("volgina", "ул. Академика Волгина, 11 (школа № 170)", "Беляево")]:
    ROWS.append(row(f"art-gym-{slug}", f"Art-Gym — художественная гимнастика ({addr.split(' (')[0].split(',')[0]})", SEC, at(st), addr,
                    3, 12, 60, 60, SPORT, 0, "пробное занятие бесплатно; абонемент — у администратора", None,
                    "Художественная гимнастика для девочек с 3 лет: растяжка, предметы, выступления",
                    "Для девочек; цены не опубликованы", "https://art-gym.ru/", "gymnastics"))

for slug, addr, st, trial in [("lugovoy", "Луговой пр-д, 5", "Марьино", True), ("andropova", "пр-т Андропова, 22", "Технопарк", True),
                              ("khachaturyana", "ул. Хачатуряна, 10, стр. 1", "Владыкино", True),
                              ("dmitrovskoe", "Дмитровское ш., 25, корп. 1", "Тимирязевская", False)]:
    ROWS.append(row(f"gymbalance-{slug}", f"GymBalance — гимнастика для малышей ({addr.split(',')[0]})", SEC, at(st), addr, 3, 9, 55, 60,
                    SPORT, 1700, ("пробное бесплатно; " if trial else "") + "8 занятий — 8400 ₽/мес, разовое 1700 ₽", None,
                    "Художественная гимнастика для детей 3–9 лет, небольшие группы",
                    "Пробного занятия в этом филиале нет" if not trial else "Только для малышей до 9 лет",
                    "https://msk.gymbalance.ru/", "gymnastics"))

# ---------------- Волейбол, теннис, бадминтон ----------------
for slug, addr, st, beach in [("marksistskaya", "Марксистская ул., 22, стр. 1", "Таганская", False),
                              ("novodmitrovskaya", "Новодмитровская ул., 5А, стр. 2", "Дмитровская", False),
                              ("garibaldi", "ул. Гарибальди, 28, корп. 3", "Новые Черемушки", False),
                              ("ordzhonikidze", "ул. Орджоникидзе, 11, стр. 8", "Ленинский проспект", False),
                              ("strogino-beach", "ул. 2-я Лыковская, 73А («2х2 TEAM»)", "Строгино", True)]:
    ROWS.append(row(f"rusvolley-{slug}", f"RusVolley — детский {'пляжный ' if beach else ''}волейбол ({addr.split(' (')[0].split(',')[0]})",
                    SEC, at(st), addr, 11, 15, 90, 90, SPORT, None, "скидка 20% на первый месяц; цены — на сайте школы", None,
                    "Детская волейбольная школа: группы по уровню, " + ("пляжный волейбол" if beach else "есть группы в выходные"),
                    "Залы — школьные спортзалы, расписание вечером", "https://rusvolley.ru/kids/", "ballgames"))

ROWS.append(row("playpark-tennis", "Академия спорта PlayPark — детский теннис", SEC, at("Юго-Западная"), "ул. Академика Анохина, вл. 2",
                4, 14, 60, 60, SPORT, 0, "бесплатная пробная тренировка; 12 занятий в месяц — 25 200 ₽", None,
                "Большой теннис для детей с 4 лет, группы по возрасту", "Дорого; корты под крышей — уточняйте",
                "https://playpark.moscow/childrenstennisschool", "racket"))
ROWS.append(row("legion-tennis", "Академия тенниса «Легион» — детский теннис", SEC, at("Борисово"), "ул. Борисовские Пруды, 12, корп. 2",
                3, 14, 45, 60, SPORT, 0, "пробное бесплатно; 1 раз в неделю — 6000 ₽/мес", None,
                "Теннис для детей, младшая группа с 3,5 лет", "Запись заранее",
                "https://www.fit-l.com/akademiya-tennisa/detskij-tennis/", "racket"))
ROWS.append(row("delosport-badminton", "«ДелоСпорт» — детский бадминтон (Фили)", SEC, at("Пионерская"), "Большая Филёвская ул., 32",
                8, 16, 60, 60, SPORT, 1200, "разовое занятие 1200 ₽", None,
                "Бадминтон для детей с 8 лет рядом с Филёвским парком", "Только с 8 лет",
                "https://xn--d1acsmafifm.xn--p1ai/deti/badmintion-deti", "racket"))

for r in ROWS:
    if r["id"] == "perevoznikov-gym-mgsu":
        r["Метро"] = "— (автобус по Ярославскому ш.)"

if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    allids = {x["id"] for x in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
    ids = [r["id"] for r in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    assert not [i for i in ids if i in existing or i in allids], [i for i in ids if i in existing or i in allids]
    if "--dry" in sys.argv:
        for r in ROWS: print(r["id"], "|", r["Название"], "|", r["Метро"])
        print("rows", len(ROWS)); sys.exit()
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    for row_ in ROWS:
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        r = ws.max_row + 1
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=r, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    print("rows", len(ROWS), "total", ws.max_row - 1)
