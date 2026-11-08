"""Вадим 08.11: «есть бассейн для деток в ЖК Фили Град — очень хорошее место, его нет на карте».
Школа плавания №1 — бассейн «Фили Град», Береговой пр-д, вл. 5А, к. 1 (страница swim-school-1.ru/basseyni/beregovaya,
проверено 08.11.2026: группы 7–13 лет, 10 400 ₽/мес за 8 занятий, пробное бесплатно). Точку по адресу уточнит osm-local.
Пишет в основную таблицу. Запуск: python3 tools/add_main_1108_filigrad.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_sections_1106 import row
from draw_icons import svg, s, face, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SRC = os.path.join(ROOT, "data", "kuda-poiti-mesta.xlsx")
PID = "swim-school-1-fili-grad"
r = row(PID, "Школа плавания №1 — бассейн «Фили Град»", "детский бассейн",
        (55.75138, 37.50854, "Фили", "приблизительно, ±300 м (по адресу)"),
        "Береговой пр-д, вл. 5А, корп. 1 (ЖК «Фили Град»)", 7, 13, 45, 45, "вода, спорт и активность", 1300,
        "пробное занятие бесплатно; группа 8 занятий — 10 400 ₽/мес, 4 занятия — 6 300 ₽/мес", "ежедневно 7:00–23:00",
        "Бассейн в ЖК «Фили Град»: детские группы плавания 7–13 лет с тренером, после школы и по выходным",
        "Мест в группах мало — записываться заранее", "https://swim-school-1.ru/basseyni/beregovaya", "pools",
        src="swim-school-1.ru/basseyni/beregovaya (проверено 2026-11-08); сообщение Вадима")
r["Проверено (дата)"] = "2026-11-08"
r["Метро"] = "Фили"

wb = openpyxl.load_workbook(SRC); ws = wb["Места"]
hdr = [c.value for c in ws[1]]
assert PID not in {c.value for c in ws["A"]}, "уже есть"
assert not (set(r) - set(hdr)), set(r) - set(hdr)
thin = Side(style="thin", color="D0D0D0"); n = ws.max_row + 1
for i, name in enumerate(hdr, 1):
    c = ws.cell(row=n, column=i, value=r.get(name))
    c.font = Font(name="Arial", size=10); c.border = Border(left=thin, right=thin, top=thin, bottom=thin)
    c.alignment = Alignment(wrap_text=True, vertical="top")
wb.save(SRC)

# Иконка: секундомер-пловец в очках плывёт кролем по дорожке, на циферблате «1»
icon = svg("teal", f'''
<rect x="0" y="84" width="128" height="44" fill="#4FB3E8"/>
<path d="M0 86 Q16 79 32 86 T64 86 T96 86 T128 86 V92 H0Z" fill="#8FD9FF"/>
<path d="M14 98 Q22 94 30 98 M92 104 Q100 100 108 104" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
<path d="M28 74 Q14 58 22 42" fill="none" {s('stroke-width="9"')}/>
<path d="M28 74 Q14 58 22 42" fill="none" stroke="#FFB23E" stroke-width="5.5" stroke-linecap="round"/>
<circle cx="21" cy="40" r="6" fill="#FFB23E" {s()}/>
<path d="M98 82 Q112 92 116 80" fill="none" {s('stroke-width="9"')}/>
<path d="M98 82 Q112 92 116 80" fill="none" stroke="#FFB23E" stroke-width="5.5" stroke-linecap="round"/>
<rect x="56" y="22" width="16" height="10" rx="3" fill="#FF6B5E" {s()}/>
<circle cx="64" cy="66" r="34" fill="#FFB23E" {s()}/>
<circle cx="64" cy="66" r="26" fill="#FFFBEA" {s('stroke-width="2.6"')}/>
<path d="M64 44 V49 M86 66 H81 M64 88 V83 M42 66 H47" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>
<path d="M60 52 L64 49 V60" fill="none" stroke="#2F7FD8" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M44 66 H84" stroke="#2F7FD8" stroke-width="3" opacity=".9"/>
<circle cx="55" cy="66" r="7.5" fill="#BFF0FF" {s('stroke-width="2.6"')}/><circle cx="73" cy="66" r="7.5" fill="#BFF0FF" {s('stroke-width="2.6"')}/>
{face(64, 66, 9, 0.75, mouth=False)}
<path d="M58 77 Q64 82 70 77" fill="none" {s('stroke-width="2.4"')}/>
<rect x="0" y="92" width="128" height="36" fill="#4FB3E8" opacity=".55"/>
{sparkle(100, 30, 6)}{sparkle(36, 18, 4)}
''')
open(os.path.join(ROOT, "icons-src", PID + ".svg"), "w").write(icon)
with open(os.path.join(ROOT, "icons-src", "subjects.txt"), "a") as f:
    f.write(f"{PID} — герой: оранжевый секундомер-пловец в голубых очках с цифрой «1» на циферблате | "
            f"сцена: плывёт кролем в бассейне, одна рука над головой, вторая загребает воду\n")
print("ok", n - 1)
