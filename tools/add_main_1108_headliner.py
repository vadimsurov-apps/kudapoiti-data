"""Вадим 08.11: «в моём ЖК (Headliner) два кафе с детскими игровыми, их нет на карте» — прислал карточки:
Winners (кофейня-пекарня, ул. Янковского, 1к1 — Яндекс Карты; детская игровая — со слов Вадима, он там бывает)
и стейк-хаус Muu (Мукомольный пр-д, 2 — tomesto.ru/moskva/places/muu-mukomolnyy: игровая комната и детское меню).
Пишет в основную таблицу. Точку по адресу уточнит osm-local. Запуск: python3 tools/add_main_1108_headliner.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P
from draw_icons import svg, s, face, eye, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SRC = os.path.join(ROOT, "data", "kuda-poiti-mesta.xlsx")
ACC = "приблизительно, ±300 м (по адресу)"


def cafe(pid, name, addr, lat, lon, hours, plus, minus, url, src, check):
    r = P(pid, name, "кафе с детской комнатой", "Шелепиха", addr, lat, lon, 0, 10, 60, 120, "спокойно", "творчество",
          None, f"средний чек ~{check} ₽ на взрослого", hours, "да", plus, minus, adult=3, src=src, acc=ACC,
          adult_price=check, booking="не нужна", loud="частично", food="да", stroller="да")
    r["Сайт"] = url; r["Категории"] = "food"; r["Проверено (дата)"] = "2026-11-08"
    return r


ROWS = [
    cafe("cafe-winners-yankovskogo", "Кофейня Winners (ЖК Headliner)", "ул. Янковского, 1, корп. 1 (ЖК Headliner)",
         55.7605, 37.5386, "ежедневно до 23:00",
         "Кофейня-пекарня в ЖК Headliner с детской игровой: родители пьют кофе, дети играют рядом",
         "Небольшая кофейня — в выходные утром бывает тесно", "https://winnerscoffee.ru/",
         "Яндекс Карты (Winners, ул. Янковского, 1к1); детская игровая — сообщение Вадима 2026-11-08", 700),
    cafe("cafe-muu-mukomolny", "Стейк-хаус Muu (ЖК Headliner)", "Мукомольный пр-д, 2 (ЖК Headliner)",
         55.7598, 37.5392, "ежедневно 12:00–24:00",
         "Стейк-хаус с детской игровой комнатой и отдельным детским меню — удобно поужинать всей семьёй",
         "Вечером ресторан взрослый; часы игровой уточняйте", "https://tomesto.ru/moskva/places/muu-mukomolnyy",
         "tomesto.ru/moskva/places/muu-mukomolnyy (игровая комната, детское меню); сообщение Вадима 2026-11-08", 2000),
]

wb = openpyxl.load_workbook(SRC); ws = wb["Места"]
hdr = [c.value for c in ws[1]]; have = {c.value for c in ws["A"]}
thin = Side(style="thin", color="D0D0D0")
for r in ROWS:
    assert r["id"] not in have and not (set(r) - set(hdr)), r["id"]
    n = ws.max_row + 1
    for i, name in enumerate(hdr, 1):
        c = ws.cell(row=n, column=i, value=r.get(name))
        c.font = Font(name="Arial", size=10); c.border = Border(left=thin, right=thin, top=thin, bottom=thin)
        c.alignment = Alignment(wrap_text=True, vertical="top")
wb.save(SRC)

# Winners: канеле-победитель с золотой медалью «1», в руке крошечная чашка капучино; тёплый карамельный фон
ICONS = {}
ICONS["cafe-winners-yankovskogo"] = (svg("orange", f'''
<ellipse cx="64" cy="108" rx="34" ry="7" fill="#C9864A" opacity=".35"/>
<path d="M38 100 L44 40 Q64 28 84 40 L90 100 Q64 110 38 100Z" fill="#B5652B" {s()}/>
<path d="M47 98 L51 44 M58 102 L60 38 M70 102 L68 38 M81 98 L77 44" stroke="#8A4419" stroke-width="3" stroke-linecap="round"/>
<ellipse cx="64" cy="40" rx="20" ry="7" fill="#7A3A12" {s()}/>
<ellipse cx="64" cy="39" rx="9" ry="3" fill="#4E230A"/>
{face(64, 66, 9, 0.85)}
<path d="M50 50 L64 80 L78 50" fill="none" stroke="#2F7FD8" stroke-width="4" stroke-linejoin="round"/>
<circle cx="64" cy="86" r="10" fill="#FFD23F" {s()}/>
<path d="M62 82 L65 80 V92" fill="none" stroke="{O}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M90 64 Q100 60 104 54" fill="none" {s('stroke-width="5"')}/>
<path d="M98 50 h14 l-2 11 h-10z" fill="#fff" {s('stroke-width="2.6"')}/><ellipse cx="105" cy="50" rx="7" ry="2.4" fill="#E9C9A2" {s('stroke-width="2"')}/>
<path d="M112 53 q5 1 0 6" fill="none" {s('stroke-width="2.4"')}/>
{sparkle(24, 34, 6)}{sparkle(34, 70, 4)}
'''), "канеле-победитель с золотой медалью «1» на синей ленте | поднимает крошечную чашку капучино, как кубок, на тёплом карамельном фоне")

# Muu: стейк T-bone сидит в сухом бассейне детской игровой и подбрасывает цветной шарик
ICONS["cafe-muu-mukomolny"] = (svg("purple", f'''
<rect x="0" y="86" width="128" height="42" fill="#7CC8FF"/>
<rect x="6" y="80" width="116" height="12" rx="6" fill="#FF8FB8" {s()}/>
<path d="M30 84 Q26 48 48 38 Q70 30 88 42 Q106 54 98 84Z" fill="#B3473B" {s()}/>
<path d="M40 76 Q38 52 54 46 Q72 40 84 50 Q94 60 90 78" fill="none" stroke="#F3C6A6" stroke-width="5" stroke-linecap="round"/>
<path d="M62 44 V82 M62 62 H92" stroke="#FFF6E8" stroke-width="7" stroke-linecap="round"/>
<path d="M62 44 V82 M62 62 H92" stroke="{O}" stroke-width="1.6" stroke-linecap="round" opacity=".5"/>
<path d="M44 58 L52 52 M70 72 L80 66" stroke="#7A2A22" stroke-width="3" stroke-linecap="round"/>
{eye(48, 66, 0.85)}{eye(78, 54, 0.85)}
<path d="M58 74 Q64 80 70 76" fill="none" {s('stroke-width="2.6"')}/>
<ellipse cx="44" cy="74" rx="4" ry="2.3" fill="#FF7FA8" opacity=".6"/>
<path d="M96 60 Q108 46 104 30" fill="none" {s('stroke-width="7"')}/>
<path d="M96 60 Q108 46 104 30" fill="none" stroke="#B3473B" stroke-width="4" stroke-linecap="round"/>
<circle cx="104" cy="20" r="8" fill="#FFD23F" {s()}/>
<circle cx="20" cy="100" r="9" fill="#FF6B5E" {s()}/><circle cx="42" cy="104" r="9" fill="#FFD23F" {s()}/>
<circle cx="64" cy="102" r="9" fill="#5DD27A" {s()}/><circle cx="86" cy="104" r="9" fill="#FF8FB8" {s()}/>
<circle cx="108" cy="100" r="9" fill="#5B8CFF" {s()}/><circle cx="32" cy="118" r="9" fill="#5B8CFF" {s()}/>
<circle cx="54" cy="120" r="9" fill="#FF6B5E" {s()}/><circle cx="76" cy="120" r="9" fill="#FFD23F" {s()}/><circle cx="98" cy="118" r="9" fill="#5DD27A" {s()}/>
{sparkle(22, 30, 5)}
'''), "стейк T-bone с белой косточкой в форме буквы Т | сидит по пояс в сухом бассейне с цветными шариками детской игровой и подбрасывает жёлтый шарик")

with open(os.path.join(ROOT, "icons-src", "subjects.txt"), "a") as f:
    for pid, (body, subj) in ICONS.items():
        open(os.path.join(ROOT, "icons-src", pid + ".svg"), "w").write(body)
        h, sc = subj.split(" | ")
        f.write(f"{pid} — герой: {h} | сцена: {sc}\n")
print("ok", [r["id"] for r in ROWS])
