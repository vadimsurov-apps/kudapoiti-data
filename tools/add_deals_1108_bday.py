"""Робот акций 08.11 вечер (тема 6: дни рождения детей).
Акции подтверждены страницами из кэша auto/pages: uryk.ru (страницы филиалов), gambrinus.ru/akcii,
danco-studio.ru/promotions, karibiya.ru/ceny, just-up.club, batutnevaljashka.clients.site.
Новое место — батутный центр «Неваляшка» (Лобня) в основную таблицу; точку уточнит osm-local по адресу.
Запуск: python3 tools/add_deals_1108_bday.py"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P
from draw_icons import svg, s, face, eye, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SRC = os.path.join(ROOT, "data", "kuda-poiti-mesta.xlsx")
TODAY = "2026-11-08"
NEV = "https://batutnevaljashka.clients.site/"

# --- новое место ---
r = P("batut-nevalyashka-lobnya", "Батутный центр «Неваляшка» (Лобня)", "батутный центр", "— (Лобня)",
      "Лобня, ул. Катюшки, 65А", 56.0235, 37.4880, 6, 14, 60, 120, "активно", "спорт и активность", None,
      "для детей старше 6 лет", None, "да",
      "Много батутов, яма для сальто, полоса препятствий, верёвочная зона и пинг-понг; утром по будням и выходным — час по цене 30 минут",
      "Только для детей старше 6 лет; цены и часы уточняйте по телефону +7 985 042-22-62",
      adult=1, src=NEV + " (сайт на Яндекс Картах: акции, адрес)", acc="приблизительно, ±1 км",
      loud="да", booking="желательна", food="нет")
r["Сайт"] = NEV; r["Категории"] = "trampolines"; r["Проверено (дата)"] = TODAY
r["День рождения"] = "имениннику −50% по документу; организация детских праздников"
ROWS = [r]

wb = openpyxl.load_workbook(SRC); ws = wb["Места"]
hdr = [c.value for c in ws[1]]; have = {c.value for c in ws["A"]}
thin = Side(style="thin", color="D0D0D0")
for row in ROWS:
    if row["id"] in have:
        continue
    assert not (set(row) - set(hdr)), set(row) - set(hdr)
    n = ws.max_row + 1
    for i, name in enumerate(hdr, 1):
        c = ws.cell(row=n, column=i, value=row.get(name))
        c.font = Font(name="Arial", size=10); c.border = Border(left=thin, right=thin, top=thin, bottom=thin)
        c.alignment = Alignment(wrap_text=True, vertical="top")
wb.save(SRC)

# --- иконка: резиновый мячик-попрыгун отскочил от батута так высоко, что пробил облако ---
ICON = svg("teal", f'''
<ellipse cx="64" cy="104" rx="40" ry="9" fill="#2E2A4A" {s()}/>
<path d="M24 104 V114 M44 111 V118 M84 111 V118 M104 104 V114" {s('stroke-width="4"')}/>
<ellipse cx="64" cy="102" rx="34" ry="6" fill="#4A4470"/>
<path d="M40 100 Q64 108 88 100" fill="none" stroke="#8B84C8" stroke-width="2"/>
<path d="M18 30 Q14 20 26 18 Q30 8 42 12 Q52 6 58 16 Q70 16 66 28 Z" fill="#fff" {s()}/>
<path d="M30 22 L28 32 M44 18 L46 30 M58 22 L54 30" stroke="#3B3355" stroke-width="2" stroke-linecap="round" opacity=".5"/>
<circle cx="72" cy="56" r="25" fill="#FF5A7A" {s()}/>
<path d="M48 50 Q72 60 96 50" fill="none" stroke="#FFE14D" stroke-width="7"/>
<path d="M48 50 Q72 60 96 50" fill="none" {s('stroke-width="1.6"')} opacity=".6"/>
<ellipse cx="62" cy="42" rx="6" ry="3.5" fill="#fff" opacity=".7" transform="rotate(-25 62 42)"/>
{face(72, 64, 8, 0.8)}
<path d="M56 82 L54 92 M72 84 V96 M88 82 L90 92" stroke="#3B3355" stroke-width="2.4" stroke-linecap="round" stroke-dasharray="3 4"/>
{sparkle(104, 26, 6)}{sparkle(108, 70, 4)}
''')
open(os.path.join(ROOT, "icons-src", "batut-nevalyashka-lobnya.svg"), "w").write(ICON)
SUBJ = ("batut-nevalyashka-lobnya — герой: красный резиновый мячик-попрыгун с жёлтой полосой | "
        "сцена: отскочил от тёмного батута высоко, под самое облако")
sp = os.path.join(ROOT, "icons-src", "subjects.txt")
if "batut-nevalyashka-lobnya —" not in open(sp).read():
    open(sp, "a").write(SUBJ + "\n")

# --- акции ---
def D(pid, place, kind, title, details, url, until=""):
    return {"id": pid, "place_id": place, "kind": kind, "title": title, "details": details, "code": "",
            "until": until, "url": url, "checked": TODAY}

NEW = [
    D("batut-nevalyashka-lobnya-bday", "batut-nevalyashka-lobnya", "birthday", "Имениннику −50%",
      "Скидка 50% имениннику в день рождения — по паспорту, свидетельству о рождении или записи в паспорте родителя.", NEV, "2026-12-31"),
    D("batut-nevalyashka-lobnya-morning", "batut-nevalyashka-lobnya", "promo", "Утром час по цене 30 минут",
      "Будни 11:00–14:00 и выходные/праздники 10:00–12:00 — час прыжков по цене получаса.", NEV, "2026-12-31"),
    D("batut-nevalyashka-lobnya-mnogodet", "batut-nevalyashka-lobnya", "discount", "Многодетным −100 ₽ на ребёнка",
      "Скидка 100 ₽ каждому прыгающему ребёнку из многодетной семьи по документу (бумажному или электронному).", NEV, "2026-12-31"),
    D("karibia-bday", "karibia", "birthday", "Тариф «Именинник»: 12 часов по цене 5",
      "В течение 7 дней с даты рождения — 12 часов аквапарка и бань: детский 1290 ₽ в будни, 1690 ₽ в выходные (обычно от 2295 ₽). Только в кассах.",
      "https://karibiya.ru/ceny/"),
]
for pid in ("justup-khodynka", "justup-riviera", "justup-sokolniki"):
    NEW.append(D(pid + "-bday", pid, "birthday", "Имениннику — бесплатные прыжки",
                 "В день рождения имениннику — бесплатные прыжки на батутной арене JUST UP!. Условия и время уточняйте у администратора.",
                 "https://just-up.club/"))
    NEW.append(D(pid + "-first", pid, "discount", "Первое занятие −20%",
                 "Скидка 20% на первое занятие (сальто, акробатика) — для тех, кто приходит в JUST UP! впервые.",
                 "https://just-up.club/"))
URYK = {
    "cafe-uryuk-riviera": "https://uryk.ru/msk/restaurants/ul-avtozavodskaa-18-tc-rivera",
    "cafe-uryuk-shchelkovsky": "https://uryk.ru/msk/restaurants/selkovo",
    "cafe-uryuk-vdnh": "https://uryk.ru/msk/restaurants/restoran-uruk-na-vdnh-solnce-moskvy",
    "cafe-uryuk-evropeisky": "https://uryk.ru/msk/restaurants/trc-evropejskij",
    "cafe-uryuk-prime-park": "https://uryk.ru/msk/restaurants/zk-prime-park",
}
for pid, url in URYK.items():
    NEW.append(D(pid + "-bday", pid, "birthday", "Имениннику −20%",
                 "Скидка 20% в день рождения и 6 дней после — по оригиналу документа.", url))
for pid in ("cafe-gambrinus-konkovo", "cafe-gambrinus-perovo", "cafe-gambrinus-spasskaya", "cafe-gambrinus-minskaya"):
    NEW.append(D(pid + "-bday", pid, "birthday", "Имениннику −20%",
                 "В день рождения и 7 дней после — скидка 20%. Не суммируется с другими акциями.", "https://gambrinus.ru/akcii/"))
for pid in ("danco-break-sokolniki", "danco-break-pyataya-avenu", "danco-break-mira"):
    NEW.append(D(pid + "-bday", pid, "birthday", "Абонемент −10% в день рождения",
                 "Скидка 10% на абонемент за два дня до и два дня после дня рождения.", "https://danco-studio.ru/promotions"))

dj = os.path.join(ROOT, "deals.json")
data = json.load(open(dj))
ids = {d["id"] for d in data["deals"]}
added = [d for d in NEW if d["id"] not in ids]
data["deals"].extend(added); data["version"] = TODAY
json.dump(data, open(dj, "w"), ensure_ascii=False, indent=1)
print("акций добавлено:", len(added))
