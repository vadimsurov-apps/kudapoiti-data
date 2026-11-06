"""Робот sections, 2026-11-06 (вечер): детский теннис (клубы с детскими группами по обзору Т—Ж «Где играть в теннис
в Москве», 27.10.2026, и карточкам zoon.ru), школа плавания MURENA (сайт murenaswim.ru из кэша auto/pages — список
бассейнов), Splash и бассейн «Олимпийской деревни-80» (Т—Ж «7 акваклубов», zoon), гимнастика (zoon), танцы для детей
(сайты из кэша: tdancestudio.ru, samplusclub.ru, tancuytut.ru).
Не брали: «Динамо-центр» на Петровке (там уже Tennis Capital), «Теннис-парк» (уже есть), СК «Максимум» Мурены (адрес
«Остафьевская ул., кГ» не привязать к точке), Inspire (на сайте нет адресов), сайт dyussh62.ru (новостная заглушка).
Координаты: точные из OSM, где объект есть в auto/candidates.json; иначе по станции метро / району.
Запуск: KP_PART=sections python3 tools/add_sections_1106d.py [--dry]"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
import add_sections_1106 as A
from add_sections_1106 import at, near, SRC
from add_batch14 import metro

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SPORT, MUS, WATER = "спорт и активность", "музыка, спорт и активность", "вода, спорт и активность"
SEC, POOL, DANCE = "спортивная секция", "детский бассейн", "танцевальная студия"
MO = "приблизительно, ±2 км (по адресу)"
M5 = "приблизительно, ±500 м (по адресу)"
EX = "точно (OpenStreetMap)"
TJ = "Т—Ж «Где играть в теннис в Москве» (t-j.ru, 27.10.2026): детские группы есть; проверено 2026-11-06"
ZOON = "карточка zoon.ru (проверено 2026-11-06)"
SITE = "сайт места (проверено 2026-11-06)"
ROWS = []


def osm(lat, lon):
    return lat, lon, metro(lat, lon), EX


def add(pid, name, typ, loc, addr, a0, a1, plus, minus, url, cats, tags=SPORT, price=None, note=None, src=SITE,
        d=(45, 90)):
    r = A.row(pid, name, typ, loc, addr, a0, a1, d[0], d[1], tags, price, note, None, plus, minus, url, cats, src=src)
    if price is None:
        r["Детский билет, ₽"] = None
    r["Взрослый билет, ₽"] = None
    ROWS.append(r)


# ---------------- Теннис ----------------
TM = "Корт по расписанию группы; ракетку для начала можно взять в клубе"
TN = "стоимость детской группы — по запросу клуба"
add("kolomensky-tennis-club", "Теннисный клуб «Коломенский» — детские группы", SEC, at("Коломенская"),
    "Коломенская наб., 20, стр. 1", 5, 17, "Теннисный клуб у Москвы-реки с групповыми тренировками для детей",
    TM, "https://tennisist.com/", "racket", note=TN, src=TJ)
add("tennis-art-otradnoe", "Теннисный клуб «Теннис-арт» (Отрадное)", SEC, at("Отрадное"), "Отрадная ул., 16",
    5, 17, "Крытые корты и детские группы по большому теннису", TM, "https://tennisart.ru/", "racket", note=TN, src=TJ)
add("bz-tennis-mosrentgen", "Теннисный клуб «Будь здоров!» (Мосрентген)", SEC, near(55.6195, 37.4735, MO),
    "пос. завода Мосрентген, 39А", 5, 17, "Теннисная школа при клубе: детские группы и игра на кортах",
    "Удобнее на машине или автобусе от Тёплого Стана", "https://bzsport.ru/", "racket", note=TN, src=TJ)
add("major-tennis-nagornaya", "Теннисный клуб «Мейджор» (Электролитный пр-д)", SEC, at("Нагорная"),
    "Электролитный пр-д, 3, стр. 2, 4 этаж", 5, 17, "Крытые корты на крыше бизнес-центра и детские группы",
    "Вход через бизнес-центр — нужен пропуск, закажите заранее", "https://major-tennis.ru/", "racket", note=TN, src=TJ)
add("spartak-tennis-sokolniki", "Теннисный центр «Спартак» (Сокольники)", SEC, osm(55.804014, 37.682283),
    "Майский просек, 7 (парк «Сокольники»)", 5, 17,
    "Легендарный теннисный центр в Сокольниках: детские группы и спортшкола «Спартак»",
    "Популярные часы разбирают быстро", "https://tenniscentre-spartak.ru/", "racket", note=TN, src=TJ)
add("orbita-tennis-park", "«Орбита Теннис Парк» (Ново-Переделкино)", SEC, near(55.6462, 37.3550, M5),
    "Чоботовская ул., 4/2", 5, 17,
    "Теннисный парк с детскими группами; есть бесплатные группы для детей с ОВЗ", TM, "https://orbitatennis.ru/",
    "racket", note=TN, src=TJ)
add("yuzhny-tennis-club", "Теннисный клуб «Южный» (Варшавское ш.)", SEC, at("Улица Академика Янгеля"),
    "Варшавское ш., 125, корп. 3", 5, 17, "Районный теннисный клуб с детскими группами", TM,
    "https://tennisnyj-klub-juzhnyj.clients.site/", "racket", note=TN, src=TJ)
add("champion-olonetsky-tennis", "Школа тенниса СК «Чемпион» (Олонецкий пр-д)", SEC, at("Медведково"),
    "Олонецкий пр-д, 5/1А", 5, 17, "Спорткомплекс с теннисной школой: детские группы на крытых кортах", TM,
    "https://arenachampion.ru/shkola-tennisa", "racket", note=TN, src=TJ)
add("skolkovo-tennis-school", "Школа тенниса «Сколково»", SEC, near(55.6985, 37.3570, MO), "Сколково, Большой б-р, 44",
    5, 17, "Современный теннисный центр в инновационном центре «Сколково» с детскими группами",
    "Далеко от метро — удобнее на машине или МЦД до «Сколково»", "https://skolkovotennis.ru/", "racket", note=TN, src=TJ)
add("ace-tennis-flotskaya", "Теннисный клуб «Эйс» (Флотская ул.)", SEC, at("Речной вокзал"), "Флотская ул., 15, корп. 2, 3 этаж",
    5, 17, "Крытые корты и детские группы недалеко от Речного вокзала", TM, "https://ace-club.ru/", "racket", note=TN, src=TJ)
add("mf41-tennis", "Теннисный центр Mf41 (Мосфильмовская)", SEC, at("Минская"), "Мосфильмовская ул., 41, корп. 2",
    5, 17, "Теннисный центр с детскими группами рядом с «Мосфильмом»", "Один из самых дорогих кортов в списке",
    "https://mf41.ru/", "racket", note=TN, src=TJ)
add("champion-tennis-plyushchikha", "Теннисная школа «Чемпион» (Плющиха)", SEC, at("Фрунзенская"), "ул. Плющиха, 57, стр. 1",
    4, 17, "Детские оздоровительные и спортивные группы по теннису с 4 лет, бесплатное пробное занятие",
    "Группа — от 18 000 ₽ в месяц", "https://chempionov.ru/", "racket", price=18000,
    note="детская группа от 18 000 ₽/мес; пробное занятие для детей бесплатно", src=ZOON)
add("polekort-tennis", "«Полекорт» — теннис для детей (Береговой пр-д)", SEC, at("Шелепиха"), "Береговой пр-д, 5А, корп. 3",
    5, 17, "Групповые занятия теннисом для детей и индивидуальные тренировки", "От метро минут 15 пешком",
    None, "racket", price=1200,
    note="детское групповое занятие от 1200 ₽", src=ZOON)
add("liga-tennis-butlerova", "Детская школа тенниса Liga Tennis (ул. Бутлерова)", SEC, at("Калужская"),
    "ул. Бутлерова, 17, блок В, 3 этаж", 5, 13, "Детские группы 5–8 и 10–13 лет и индивидуальные занятия",
    "Корты в бизнес-центре — уточняйте вход", None, "racket",
    price=11000, note="группа 5–8 лет — 11 000 ₽, 10–13 лет — 16 500 ₽ (абонемент)", src=ZOON)

# ---------------- Гимнастика ----------------
add("gimnast-moscow-gorodetskaya", "Московский гимнастический центр (Городецкая ул.)", SEC, at("Новокосино"),
    "Городецкая ул., 8А", 4, 14, "Спортивная гимнастика для детей в отдельном гимнастическом зале",
    "Абонементы дорогие (от 37 000 ₽ в месяц)", None, "gymnastics",
    src=ZOON)
add("gym-soyuz-semenovsky", "«Гимнастический Союз» — спортивная гимнастика для детей", SEC, at("Семёновская"),
    "Семёновский пер., 15", 4, 14, "Секция спортивной гимнастики для детей рядом с метро «Семёновская»",
    "Группы по возрасту, запись заранее", None, "gymnastics",
    src=ZOON)

# ---------------- Плавание ----------------
add("splash-bakuninskaya", "Школа плавания Splash (Бакунинская ул.)", POOL, at("Бауманская"), "Бакунинская ул., 13, стр. 1",
    4, 14, "Детские группы и индивидуальные занятия плаванием, соревнования и сборы для учеников",
    "Индивидуальное занятие для ребёнка — около 2000 ₽", "https://splash-school.com/", "pools", WATER, price=2900,
    note="4 групповых занятия (1 раз в неделю) — 2900 ₽", src="Т—Ж «7 акваклубов Москвы» и zoon.ru (проверено 2026-11-06)")
add("olimp80-pool", "Бассейн СК «Олимпийская деревня-80»", POOL, near(55.6760, 37.4660, M5),
    "Мичуринский пр-т, Олимпийская деревня, 2", 5, 17,
    "Городской бассейн с мелкими ваннами для обучения детей плаванию и спортивными группами",
    "Абонементы продают только в кассе комплекса", "https://skod80.mossport.ru/sports/ozdorovitelnoe-plavanie",
    "pools", WATER, price=5200, note="13 групповых занятий — 5200 ₽",
    src="Т—Ж «7 акваклубов Москвы» (t-j.ru) и Афиша (проверено 2026-11-06)")

MU = "https://murenaswim.ru/"
MUP = "Школа плавания MURENA заслуженного тренера Д. Лазарева: дети осваивают все стили, есть индивидуальные занятия"
MUM = "Расписание и цены — по телефону школы; бассейн арендованный, вход по пропуску"
for pid, nm, loc, addr in [
    ("murena-korall", "СК «Коралл»", osm(55.785419, 37.668541), "1-й Красносельский пер., 9"),
    ("murena-bauman", "бассейн МГТУ им. Баумана", near(55.7665, 37.6865, M5), "Госпитальная наб., 4, стр. 2"),
    ("murena-severny", "ЦСП «Северный»", osm(55.936631, 37.558807), "ул. Арсюкова, 11"),
    ("murena-mgsu", "бассейн НИУ МГСУ", near(55.8555, 37.6960, M5), "Ярославское ш., 26, стр. 4"),
    ("murena-nekrasovka", "ДС «Некрасовка»", at("Некрасовка"), "Покровская ул., 22"),
    ("murena-izumrudny", "бассейн «Изумрудный»", osm(55.531723, 37.511475), "Южнобутовская ул., 96"),
    ("murena-umka", "СК «Умка»", near(55.8790, 37.4780, MO), "Левобережная ул., 12, корп. 1"),
    ("murena-internat", "бассейн школы-интерната № 1", near(55.8090, 37.6480, MO), "3-я Мытищинская ул., 5, стр. 6"),
    ("murena-zhivopisny", "бассейн «Живописный»", near(55.7935, 37.4605, MO), "Живописная ул., 28, стр. 6"),
]:
    add(pid, f"Школа плавания MURENA ({nm})", POOL, loc, addr, 4, 17, MUP, MUM, MU, "pools", WATER,
        note="стоимость — по запросу школы", src="сайт murenaswim.ru — список бассейнов (кэш auto/pages, 2026-11-06)")

# ---------------- Танцы ----------------
add("tdance-tango-tsska", "Танцевальная студия «Танго» (ЦСКА)", DANCE, at("ЦСКА"), "ул. Авиаконструктора Микояна, 10",
    4, 14, "Балет, бальные танцы, брейк-данс и dance mix для детей у Ходынского поля", "Взрослые группы идут в тех же залах",
    "https://tdancestudio.ru/", "dance", MUS)
add("samplus-krasnoselskaya", "«Сам плюс» — танцы и театр для детей (Красносельская)", DANCE, at("Красносельская"),
    "Верхняя Красносельская ул., 34", 6, 14, "Хип-хоп для детей 6–10 лет, джаз-фанк и актёрское мастерство",
    "Расписание детских групп — вечером", "https://samplusclub.ru/", "dance", MUS)
add("tancuy-tut-tsvetnoy", "Школа танцев «Танцуй тут» (Цветной бульвар)", DANCE, at("Цветной бульвар"),
    "Цветной б-р, 19, корп. 5", 4, 14, "Baby dance для малышей 4–6 лет, dance mix и хип-хоп для детей",
    "Основная аудитория — взрослые", "https://www.tancuytut.ru/", "dance", MUS)

MET = {"murena-mgsu": "ВДНХ (далее автобус по Ярославскому ш.)", "skolkovo-tennis-school": "Сколково (МЦД-1)",
       "murena-umka": "Беломорская"}
for r in ROWS:
    if r["id"] in MET: r["Метро"] = MET[r["id"]]

if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    allids = {x["id"] for x in json.load(open(os.path.join(ROOT, "places.json")))["places"]}
    ids = [r["id"] for r in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    assert not [i for i in ids if i in existing or i in allids], [i for i in ids if i in existing or i in allids]
    if "--dry" in sys.argv:
        for r in ROWS: print(r["id"], "|", r["Название"], "|", r["Метро"], "|", r["Категории"], "|", r["Широта"], r["Долгота"])
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
