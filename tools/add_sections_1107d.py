"""Робот sections, 2026-11-07 (06 UTC): бадминтон (BadmPRO в «Карибии», СДЦ «Алексеевский», СШОР №92 «Солнцево»), волейбол (СШОР №21, «Искра-Новогиреево», ВК ДЮСШ «Звезда»),
шахматы (10 детских клубов и центров), бой на мечах для детей (Федерация фехтования на мечах — 5 залов, «Эскалибур»).
Источники (кэш auto/pages, скачан 2026-11-07 через auto/fetch-queue.txt): каталог sportschools.ru по округам
(бадминтон, шахматы, волейбол, фехтование — возраст детских групп, адрес, метро), kartasporta.ru (ФОК «Марьина роща»).
Не брали: только взрослые («Волейбол для всех», Newton Arena, BAD, «Искра»), филиалы Nevsky Bears/RusVolley (уже есть),
шахматы Русской шахматной школы в частных школах (только для своих учеников), Союз-Спорт, ФОК «Марьина роща», Esther Kids (адрес уже есть), BadmPRO в ДС «Динамо» (там уже есть клуб бадминтона).
Координаты — по метро («приблизительно»), уточнит geocode-address.yml.
Запуск: KP_PART=sections python3 tools/add_sections_1107d.py [--dry]"""
import json, os, re, sys, math, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
import add_sections_1106 as A
from add_sections_1106 import at, near, SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
D = "проверено 2026-11-07"
SEC, CH = "спортивная секция", "шахматный клуб"
SP = "спорт и активность"
LOG = "спорт и активность"
SS = "sportschools.ru/gorod-Moscow"
NOP = "цены — у администратора"
R = []


def add(pid, name, typ, loc, addr, a0, a1, d, tags, price, note, plus, minus, site, cat, src):
    r = A.row(pid, name, typ, loc, addr, a0, a1, d[0], d[1], tags, price, note, None, plus, minus, site, cat,
              src=f"{src} ({D})")
    r["Детский билет, ₽"] = price
    r["Взрослый билет, ₽"] = None
    r["Проверено (дата)"] = "2026-11-07"
    R.append(r)


B, V, C, F = (60, 90), (60, 90), (45, 60), (60, 90)
# ---------------- Бадминтон ----------------
add("badmpro-karibia", "Клуб бадминтона BadmPRO — дети (ЦСО «Карибия», Перово)", SEC, at("Перово"),
    "Зелёный пр-т, 10Б (центр семейного отдыха «Карибия»)", 7, 17, B, SP, None, NOP,
    "Бадминтон для детей с 7 лет прямо в семейном центре с аквапарком — пока ребёнок тренируется, можно поплавать",
    "Цены не опубликованы — уточняйте при записи", None, "badminton", f"{SS}/region-VAO/sport-Badminton")
add("sdc-alekseevsky-zubarev", "СДЦ «Алексеевский» — детский бадминтон и шахматы", SEC, at("Алексеевская"),
    "Зубарев пер., 17", 7, 17, B, SP, None, "секции городского спортивно-досугового центра; цены — у администратора",
    "Городской спортивно-досуговый центр: бадминтон и шахматы для детей с 7 лет, ещё танцы и настольный теннис",
    "Расписание групп по возрастам уточняйте в центре", None, "badminton, chess", f"{SS}/region-SVAO/sport-Badminton")
add("sshor92-solntsevo-badminton", "СШОР №92 «Солнцево» — бадминтон для детей", SEC, at("Солнцево"),
    "Солнцевский пр-т, 9", 7, 12, B, SP, 0, "бесплатно — спортшкола Москомспорта (набор по испытаниям)",
    "Спортшкола олимпийского резерва: бесплатный бадминтон для младших школьников с 7–8 лет",
    "Набор раз в год, по результатам просмотра", None, "badminton", f"{SS}/region-ZAO/sport-Badminton")

# ---------------- Волейбол ----------------
add("sshor21-volley-kharitonyevsky", "СШОР №21 Москомспорта — детский волейбол", SEC, at("Красные ворота"),
    "Большой Харитоньевский пер., 22/1", 7, 17, V, SP, 0, "бесплатно — спортшкола Москомспорта (набор по испытаниям)",
    "Спортшкола олимпийского резерва по волейболу: два оборудованных зала, группы с 7 лет",
    "Набор по просмотру; места в группах ограничены", None, "ballgames", f"{SS}/region-CAO/sport-Volleyball")
add("iskra-novogireevo-volley", "Волейбольный клуб «Искра-Новогиреево» — дети", SEC, at("Новогиреево"),
    "ул. Полимерная, 7А", 9, 14, V, SP, None, NOP,
    "Детско-юношеский волейбольный клуб: обучение с нуля и игры с тренером для 9–14 лет",
    "Цены не опубликованы", None, "ballgames", f"{SS}/region-VAO/sport-Volleyball")
add("zvezda-volley-nakhimovsky", "Волейбольный клуб ДЮСШ «Звезда» (Нахимовский пр-т)", SEC, at("Нахимовский проспект"),
    "Нахимовский пр-т, 21", 9, 14, V, SP, None, NOP,
    "Волейбол для детей 9–14 лет: тренировки, соревнования и летний спортивный лагерь",
    "Цены не опубликованы", None, "ballgames", f"{SS}/sport-Volleyball/Deti")

# ---------------- Шахматы ----------------
def chess(pid, name, loc, addr, a0, a1, plus, minus, src):
    add(pid, name, CH, loc, addr, a0, a1, C, LOG, None, NOP, plus, minus, None, "chess", src)

chess("chess-art-valovaya", "Школа «Шахматное искусство» (Валовая ул., Павелецкая)", at("Павелецкая"), "Валовая ул., 14, стр. 8",
      3, 17, "Шахматы для детей с 3 лет в группах до 8 человек или индивидуально", "Цены не опубликованы",
      f"{SS}/region-CAO/sport-Chess")
chess("svobodnye-shakhmaty-tikhvinsky", "Шахматный клуб «Свободные шахматы» (Тихвинский пер.)", at("Менделеевская"),
      "Тихвинский пер., 10–12, корп. 9", 3, 17, "Занятия с тренером для детей с 3 лет и подростков: от первых ходов до турниров",
      "Цены не опубликованы", f"{SS}/region-CAO/sport-Chess")
chess("chesspro-dekabristov", "Шахматная школа ChessPRO (ул. Декабристов, Отрадное)", at("Отрадное"), "ул. Декабристов, 4, корп. 2",
      4, 17, "Шахматы для детей с 4 лет: регулярные турниры внутри школы и матчи с другими клубами",
      "Цены не опубликованы", f"{SS}/region-SVAO/sport-Chess")
chess("kurchatov-school-chess", "Шахматная секция Курчатовской школы (Щукино)", at("Щукинская"), "ул. Академика Бочвара, 2, корп. 2",
      4, 14, "Шахматная секция для детей с 4 лет и подростков при Курчатовской школе", "Уточняйте, принимают ли детей не из школы",
      f"{SS}/region-SZAO/sport-Chess")
chess("russky-shakh-udaltsova", "Шахматная секция «Русский шах» (ул. Удальцова)", at("Проспект Вернадского"), "ул. Удальцова, 69",
      5, 12, "Шахматы для детей 5–12 лет — классические, индийские и даже старинные русские шахматы-таврели",
      "Цены не опубликованы", f"{SS}/region-ZAO/sport-Chess")
chess("sinegoriya-chess", "ЦВР «Синегория» — шахматы для детей (Партизанская ул.)", at("Молодёжная"), "Партизанская ул., 45",
      3, 16, "Городской центр внешкольной работы: шахматы с 3 лет, рядом — туризм, акробатика, скалолазание",
      "Набор в начале учебного года — места в группах ограничены", f"{SS}/region-ZAO/sport-Chess")
chess("stantsiya-talantov-chess", "«Станция юных талантов» школы №1002 — шахматы (Солнцево)", at("Говорово"),
      "Волынская ул., 8, корп. 2", 7, 16, "Шахматы для школьников 7–16 лет на бюджетной основе, ещё спортивные и технические кружки",
      "Бюджетные места ограничены", f"{SS}/region-ZAO/sport-Chess")
chess("pilot-chess-altufyevskoe", "Клуб технического творчества «Пилот» — шахматы", at("Алтуфьево"), "Алтуфьевское ш., 102Б",
      3, 12, "Шахматы для детей с 3 лет в клубе, где ещё строят авиа- и автомодели", "Цены не опубликованы",
      f"{SS}/region-SVAO/sport-Chess")
chess("zemlyane-chess-kokkinaki", "Образовательный центр «Земляне» — шахматы (Аэропорт)", at("Аэропорт"), "ул. Коккинаки, 3",
      5, 12, "Шахматы для детей 5–12 лет, а ещё танцы, акробатика и цирковое искусство в одном центре",
      "Цены не опубликованы", f"{SS}/region-SAO/sport-Chess")
chess("dzhelsomino-chess-zorge", "Творческий центр «Джельсомино» — шахматы (ул. Зорге)", at("Полежаевская"), "ул. Зорге, 6, корп. 3",
      3, 14, "Уроки шахмат для детей с 3 лет в творческом центре с хореографией и ушу", "Цены не опубликованы",
      f"{SS}/region-SAO/sport-Chess")

# ---------------- Бой на мечах ----------------
FMN = f"{SS}/sport-Fencing"
def swords(pid, where, loc, addr, a0, a1, plus):
    add(pid, f"Федерация фехтования на мечах — дети ({where})", SEC, loc, addr, a0, a1, F, SP, None, NOP, plus,
        "Цены не опубликованы — уточняйте по телефону", None, "sport", FMN)

swords("fmech-sokol", "Новопесчаная ул., Сокол", at("Сокол"), "Новопесчаная ул., 17, корп. 4", 5, 14,
       "Бой на мечах для детей 5–14 лет: безопасные мечи, малые группы, подойдёт с любой подготовкой")
swords("fmech-sukharevsky", "Большой Сухаревский пер.", at("Сухаревская"), "Большой Сухаревский пер., 16", 7, 11,
       "Группы для мальчиков и девочек 7–11 лет: учатся держать меч, двигаться и уважать соперника")
swords("fmech-ramenki", "Мосфильмовская ул., Раменки", at("Раменки"), "Мосфильмовская ул., 53", 5, 14,
       "Бой на мечах в малых группах для 5–14 лет по авторской программе федерации")
swords("fmech-prazhskaya", "ул. Красного Маяка, Пражская", at("Пражская"), "ул. Красного Маяка, 15", 5, 13,
       "Небольшие группы для детей 5–13 лет, турниры и соревнования внутри федерации")
swords("fmech-izmaylovo", "Первомайская ул., Измайловская", at("Измайловская"), "Первомайская ул., 42, корп. 1", 5, 12,
       "Группы для детей с 5 лет: координация, реакция и рыцарский кодекс чести")
add("excalibur-knights-tekstilshchiki", "Школа рыцарей «Эскалибур» (Текстильщики)", SEC, at("Текстильщики"),
    "ул. Артюхиной, 4", 5, 17, F, SP, None, NOP,
    "Бой на мечах со щитом для мальчиков и девочек с 5 лет: фехтование плюс общая спортивная подготовка",
    "Цены не опубликованы", None, "sport", FMN)

ROWS = R

if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    allp = json.load(open(os.path.join(ROOT, "places.json")))["places"]
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
