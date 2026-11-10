"""Робот sections, 2026-11-07 (09 UTC): баскетбол (БК «Стремление» — 2 новых зала, ДБК «Спартаковец», «Прогресс», «Медведи»,
«Академия Будущего», TeenBasket, «Крылья Советов», «Движение вверх»), волейбол («Залп», «Зенит-Москва», Globus, RusVolley
Павелецкая, ВК «Тактика»), гандбол (СШОР №53, «Юность Москвы» — «Кунцево»), бадминтон (СК РГАУ-МСХА, конноспортивная база ЦСКА),
шахматы («Гранит», клуб в «Алисиуме», «Этюд», «Подкова», «Ферзьбери», «Королевская пешка», aChess, «Феномен» ×3,
Шахматная школа №1 ×5), фехтование («Сталь» на 3-м Хорошёвском, Федерация фехтования на мечах — Баррикадная, Тропарёво).
Источник — каталог sportschools.ru (кэш auto/pages, скачан 2026-11-07 через auto/fetch-queue.txt): карточки с детскими
возрастными группами, адресом и метро. Не брали: только взрослые группы (ВК «Тактика» Позитив/Арсенал/Кунцево, RAYDAS, Rodina),
аренду залов без секций, многопрофильные детские центры без явной секции, училища олимпийского резерва (МССУОР), филиалы,
которые уже есть («Стремление» на Стромынке и Яблочкова, «Невские Медведи», RusVolley Дмитровское ш., «Ленинградка»).
Координаты — по метро («приблизительно»), уточнит geocode-address.yml.
Запуск: KP_PART=sections python3 tools/add_sections_1107e.py [--dry]"""
import json, os, re, sys, math, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
import add_sections_1106 as A
from add_sections_1106 import at, near, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
D = "проверено 2026-11-07"
SEC, CH = "спортивная секция", "шахматный клуб"
SP, LOG = "спорт и активность", "спорт и активность"
SS = "sportschools.ru/gorod-Moscow"
NOP = "цены — у администратора"
R = []


def add(pid, name, typ, loc, addr, a0, a1, d, price, note, plus, minus, cat, src, tags=SP):
    r = A.row(pid, name, typ, loc, addr, a0, a1, d[0], d[1], tags, price, note, None, plus, minus, None, cat,
              src=f"{src} ({D})")
    r["Детский билет, ₽"] = price
    r["Взрослый билет, ₽"] = None
    r["Проверено (дата)"] = "2026-11-07"
    R.append(r)


B = (60, 90)
BS = f"{SS}/sport-Basketball/Deti"
CP = "Цены не опубликованы — уточняйте по телефону"
# ---------------- Баскетбол ----------------
STR = "Баскетбол для школьников с любым уровнем подготовки: турниры своей лиги и сборы в Подмосковье на каникулах"
add("stremlenie-basket-kalitniki", "Баскетбольный клуб «Стремление» (Большая Калитниковская ул.)", SEC, at("Пролетарская"),
    "Большая Калитниковская ул., 34/3, стр. 1", 7, 16, B, None, NOP, STR, CP, "ballgames", f"{SS}/region-CAO/sport-Basketball")
add("stremlenie-basket-egerskaya", "Баскетбольный клуб «Стремление» (Егерская ул., Сокольники)", SEC, at("Сокольники"),
    "Егерская ул., 4", 5, 17, B, None, NOP, "Баскетбол для детей с 5 лет рядом с парком Сокольники, летние и зимние лагеря",
    CP, "ballgames", f"{SS}/region-VAO/sport-Basketball")
add("stremlenie-basket-shelepikha", "Баскетбольный клуб «Стремление» (2-я Магистральная ул., Шелепиха)", SEC, at("Шелепиха"),
    "2-я Магистральная ул., 16, стр. 1", 7, 17, B, None, NOP, STR, CP, "ballgames", f"{SS}/region-SAO/sport-Basketball")
add("spartakovets-basket-presnya", "Детский баскетбольный клуб «Спартаковец» (Красная Пресня)", SEC, at("Краснопресненская"),
    "ул. Красная Пресня, 24, стр. 1", 5, 14, B, None, NOP, "Тренировки по баскетболу для детей с 5 лет в центре города",
    CP, "ballgames", f"{SS}/region-CAO/sport-Basketball")
add("spartakovets-basket-aviamotornaya", "Детский баскетбольный клуб «Спартаковец» (Авиамоторная ул.)", SEC, at("Авиамоторная"),
    "Авиамоторная ул., 55, корп. 8", 7, 16, B, None, NOP, "Баскетбол для детей 7–16 лет: группы по возрасту, игры с другими клубами",
    CP, "ballgames", BS)
add("progress-basket-solntsevo", "Баскетбольная академия «Прогресс» (Мещерский лес, Солнцево)", SEC, at("Говорово"),
    "Домостроительная ул., 4А", 5, 17, B, None, NOP, "Баскетбол с 5 лет: тренировки, игровая практика, сборы и соревнования",
    CP, "ballgames", f"{SS}/region-ZAO/sport-Basketball")
add("medvedi-basket-prospekt-mira", "Баскетбольный клуб «Медведи» (пр-т Мира, Алексеевская)", SEC, at("Алексеевская"),
    "пр-т Мира, 101В", 8, 17, B, None, NOP, "Баскетбольные группы для детей 8–17 лет с выступлениями на соревнованиях",
    CP, "ballgames", f"{SS}/region-SVAO/sport-Basketball")
add("akademiya-budushchego-terekhovo", "«Академия Будущего» — детский баскетбол (Терехово)", SEC, at("Терехово"),
    "ул. Нижние Мнёвники, 10", 3, 16, B, None, NOP, "Баскетбол для малышей с 3 лет и школьников, рядом — футбол и художественная гимнастика",
    CP, "ballgames", f"{SS}/region-SZAO/sport-Basketball")
add("akademiya-budushchego-cheryomushki", "«Академия Будущего» — баскетбол и художественная гимнастика (Черёмушки)", SEC,
    at("Профсоюзная"), "Новочерёмушкинская ул., 34, корп. 2", 3, 16, B, None, NOP,
    "Секции баскетбола и художественной гимнастики для детей с 3 лет в одном зале", CP, "ballgames, gymnastics", BS)
add("teenbasket-shchelkovskaya", "Школа основ баскетбола TeenBasket (16-я Парковая ул.)", SEC, at("Щёлковская"),
    "16-я Парковая ул., 20", 7, 16, B, None, NOP, "Баскетбол для детей и подростков: эстафеты, игры с мячом и соревнования на тренировках",
    CP, "ballgames", f"{SS}/region-VAO/sport-Basketball")
add("krylya-sovetov-basket", "Секция баскетбола на стадионе «Крылья Советов»", SEC, at("Семёновская"),
    "пр-т Будённого, 17А", 6, 12, B, None, NOP, "Баскетбол для детей с 6 лет на старом московском стадионе", CP,
    "ballgames", f"{SS}/region-VAO/sport-Basketball")
add("dvizhenie-vverkh-basket", "Баскетбольная академия «Движение вверх» (Армейская ул.)", SEC, at("Аэропорт"),
    "Армейская ул., 5, стр. 12", 5, 17, B, None, NOP, "Баскетбол с нуля для детей с 5 лет и группы продвинутого уровня",
    CP, "ballgames", BS)

# ---------------- Волейбол ----------------
VS = f"{SS}/sport-Volleyball/Deti"
add("zalp-volley-vdnkh", "Школа волейбола «Залп» (Прудовой пр-д, ВДНХ)", SEC, at("ВДНХ"), "Прудовой пр-д, 9", 7, 17, B, None, NOP,
    "Волейбол для детей с 7 лет, тренеры — бывшие профессиональные игроки", CP, "ballgames", f"{SS}/region-SVAO/sport-Volleyball")
add("zenit-moskva-volley", "Детско-юношеский волейбольный клуб «Зенит-Москва» (Тёплый Стан)", SEC, at("Тёплый Стан"),
    "Профсоюзная ул., 154, корп. 7", 9, 16, B, None, NOP, "Волейбол для детей 9–16 лет, индивидуальные занятия и летние сборы",
    CP, "ballgames", VS)
add("globus-volley-kuzminki", "Школа волейбола Globus (ул. Юных Ленинцев)", SEC, at("Кузьминки"), "ул. Юных Ленинцев, 45, корп. 2",
    9, 17, B, None, NOP, "Волейбол в малых группах для детей с 9 лет, контрольные матчи с другими клубами", CP, "ballgames", VS)
add("rusvolley-paveletskaya", "RusVolley — детский волейбол (3-й Монетчиковский пер.)", SEC, at("Павелецкая"),
    "3-й Монетчиковский пер., 11, стр. 1", 5, 15, B, None, NOP, "Классический и пляжный волейбол для детей 5–15 лет, кемпы на каникулах",
    CP, "ballgames", f"{SS}/region-CAO/sport-Volleyball")
add("taktika-volley-dvintsev", "Волейбольный клуб «Тактика» (ул. Двинцев)", SEC, at("Савёловская"), "ул. Двинцев, 12, корп. 1А",
    11, 17, B, None, NOP, "Волейбол для подростков с 11 лет: обучение и игровые тренировки", "Только с 11 лет; цены не опубликованы",
    "ballgames", f"{SS}/region-SVAO/sport-Volleyball")

# ---------------- Гандбол ----------------
HB = f"{SS}/sport-Handball/Deti"
add("sshor53-handball-vykhino", "СШОР №53 — детский гандбол (Выхино)", SEC, at("Выхино"), "ул. Молдагуловой, 20А", 7, 12, B, 0,
    "бесплатно — государственная спортшкола (набор по просмотру)", "Гандбол для детей с 7 лет в спортшколе, рядом — спортивная акробатика",
    "Набор раз в год, места ограничены", "sport", HB)
add("yunost-kuntsevo-handball", "СШОР «Юность Москвы» — «Кунцево»: детский гандбол", SEC, at("Кунцевская"), "Можайское ш., 7", 7, 14, B, 0,
    "бесплатно — государственная спортшкола (набор по просмотру)", "Гандбол для детей 7–14 лет в спорткомплексе «Кунцево» с бассейном",
    "Набор по просмотру; расписание уточняйте", "sport", HB)

# ---------------- Бадминтон ----------------
add("timiryazevka-sk-badminton", "СК РГАУ-МСХА им. Тимирязева — детский бадминтон", SEC, at("Петровско-Разумовская"),
    "Лиственничная аллея, 12, корп. 2", 5, 17, B, None, NOP, "Бадминтон для детей с 5 лет в спорткомплексе Тимирязевской академии",
    "Комплекс университетский — расписание детских групп уточняйте", "badminton", f"{SS}/region-SAO/sport-Badminton")
add("cska-horse-base-badminton", "Конноспортивная база ЦСКА — бадминтон для детей", SEC, at("Речной вокзал"), "ул. Дыбенко, 5", 7, 17, B,
    None, NOP, "Бадминтон для детей с 7 лет, а ещё верховая езда и тхэквондо на той же базе", CP, "badminton",
    f"{SS}/region-SAO/sport-Badminton")

# ---------------- Шахматы ----------------
C = (45, 60)
CC = f"{SS}/sport-Chess/Deti"
def chess(pid, name, loc, addr, a0, a1, plus, src, minus=CP):
    add(pid, name, CH, loc, addr, a0, a1, C, None, NOP, plus, minus, "chess", src, tags=LOG)

chess("granit-chess-makarenko", "Шахматный клуб «Гранит» (ул. Макаренко)", at("Чистые пруды"), "ул. Макаренко, 8", 3, 17,
      "Шахматы для детей с 3 лет и ежемесячные турниры с национальным рейтингом", f"{SS}/region-CAO/sport-Chess")
chess("alisium-chess", "Шахматный клуб в мультимедийном центре «Алисиум»", at("Тверская"), "Большой Гнездниковский пер., 3", 3, 17,
      "Занятия, детские турниры, сеансы одновременной игры, шахматные праздники и квесты", f"{SS}/region-CAO/sport-Chess")
chess("etyud-chess-otradnoe", "Шахматная школа «Этюд» (Отрадное)", at("Отрадное"), "ул. Римского-Корсакова, 10", 4, 17,
      "Школа с историей: дети с 4 лет, педагоги — международные мастера, встречи с гроссмейстерами-выпускниками",
      f"{SS}/region-SVAO/sport-Chess")
chess("podkova-chess-kurkino", "Шахматный клуб «Подкова» (Детский клуб Буракова, Куркино)", near(55.8960, 37.3925),
      "Новокуркинское ш., 51", 3, 17, "Шахматы для детей с 3 лет, воспитанники ездят на российские и зарубежные турниры",
      f"{SS}/region-SZAO/sport-Chess")
chess("ferzbury-chess-strogino", "Школа шахмат «Ферзьбери» (Строгино)", at("Строгино"), "ул. Маршала Катукова, 22", 5, 17,
      "Шахматы для детей с 5 лет в мини-группах и индивидуально", f"{SS}/region-SZAO/sport-Chess")
chess("korolevskaya-peshka-chess", "Студия шахмат «Королевская пешка» (ул. Мельникова)", at("Пролетарская"), "ул. Мельникова, 7, стр. 1",
      4, 17, "Шахматы для детей с 4 лет, можно заниматься всей семьёй", CC)
chess("achess-shabolovka", "Шахматная школа aChess (библиотека №164, Шаболовка)", at("Шаболовская"), "ул. Шаболовка, 36 (библиотека №164)",
      3, 17, "Шахматы для детей с 3 лет в районной библиотеке", CC)
FEN = "Мини-группы до 8 человек для детей с 5 лет, турниры с рейтингом и летний шахматный лагерь"
chess("fenomen-chess-chelyuskinskaya", "Шахматная школа «Феномен» (Челюскинская ул., Медведково)", at("Медведково"),
      "Челюскинская ул., 2", 5, 16, FEN, f"{SS}/region-SVAO/sport-Chess")
chess("fenomen-chess-argunovskaya", "Шахматная школа «Феномен» (Аргуновская ул.)", at("Улица Академика Королёва"),
      "Аргуновская ул., 14, стр. 2", 5, 17, FEN, f"{SS}/region-SVAO/sport-Chess")
chess("fenomen-chess-babushkina", "Шахматная школа «Феномен» (ул. Лётчика Бабушкина)", at("Бабушкинская"),
      "ул. Лётчика Бабушкина, 32, корп. 3", 5, 17, FEN, f"{SS}/region-SVAO/sport-Chess")
S1 = "Шахматы для детей с 4 лет по авторской программе, официальные турниры с обсчётом рейтинга"
chess("chess1-sushchevsky-val", "Шахматная школа №1 (Сущёвский Вал, Марьина Роща)", at("Марьина Роща"), "ул. Сущёвский Вал, 66", 4, 14, S1,
      f"{SS}/region-CAO/sport-Chess")
chess("chess1-dubninskaya", "Шахматная школа №1 (Дубнинская ул., Дегунино)", at("Селигерская"), "Дубнинская ул., 16, корп. 1", 4, 14, S1,
      f"{SS}/region-SAO/sport-Chess")
chess("chess1-bratislavskaya", "Шахматная школа №1 (Братиславская ул.)", at("Братиславская"), "Братиславская ул., 19, корп. 1", 4, 12, S1, CC)
chess("chess1-kastanaevskaya", "Шахматная школа №1 (Кастанаевская ул., Пионерская)", at("Пионерская"), "Кастанаевская ул., 52, стр. 2",
      4, 12, S1, f"{SS}/region-ZAO/sport-Chess")
chess("chess1-moreon-golubinskaya", "Шахматная школа №1 (Голубинская ул., «Мореон»)", at("Ясенево"), "Голубинская ул., 16", 4, 12, S1, CC)

# ---------------- Фехтование ----------------
FE = f"{SS}/sport-Fencing"
add("stal-fencing-khoroshevsky", "Фехтовальный клуб «Сталь» (3-й Хорошёвский пр-д)", SEC, at("Полежаевская"), "3-й Хорошёвский пр-д, 5, стр. 6",
    6, 17, B, None, NOP, "Фехтование на шпагах для детей с 6 лет: группы для начинающих и продолжающих", CP, "sport", FE)
add("fmech-barrikadnaya", "Федерация фехтования на мечах — дети (Большая Никитская ул.)", SEC, at("Баррикадная"),
    "Большая Никитская ул., 47, стр. 2", 5, 10, B, None, NOP, "Бой на мечах в малых группах для детей 5–10 лет с любой подготовкой",
    CP, "sport", FE)
add("fmech-troparevo", "Федерация фехтования на мечах — дети (ул. Островитянова, Тропарёво)", SEC, at("Тропарёво"),
    "ул. Островитянова, 6", 5, 12, B, None, NOP, "Бой на мечах для детей 5–12 лет: безопасные мечи, турниры федерации",
    CP, "sport", FE)

ROWS = R
if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    allp = json.load(open(os.path.join(ROOT, "places-all.json")))["places"]
    allids = {x["id"] for x in allp}
    ids = [r["id"] for r in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    assert not [i for i in ids if i in existing or i in allids], [i for i in ids if i in existing or i in allids]
    pts = [(p["name"], p["lat"], p["lon"]) for p in allp]
    for f in glob.glob(os.path.join(ROOT, "data", "parts", "*.xlsx")):
        rr = list(openpyxl.load_workbook(f, read_only=True)["Места"].values); h = rr[0]
        pts += [(r[h.index("Название")], r[h.index("Широта")], r[h.index("Долгота")]) for r in rr[1:] if r[h.index("Широта")]]
    key = lambda n: re.sub(r"[«»\"()—,.-]", " ", str(n).lower()).split()[:2]
    for r in ROWS:
        for n, a, b in pts:
            if a and math.hypot((r["Широта"] - a) * 111000, (r["Долгота"] - b) * 63000) < 300 and key(n) == key(r["Название"]):
                print("ДУБЛЬ?", r["id"], "~", n)
    if "--dry" in sys.argv:
        for r in ROWS: print(r["id"], "|", r["Метро"], "|", r["Категории"], "|", r["Широта"], r["Долгота"])
        from collections import Counter
        print("rows", len(ROWS), Counter(r["Категории"] for r in ROWS)); sys.exit()
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
