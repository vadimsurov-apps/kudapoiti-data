"""Робот cafes 11.11 (13 UTC): последний проход «качество 2026-11» по 64 оставшимся строкам, которые прежние проходы
не нашли в Яндекс Картах. Только перенос фактов из прежнего источника строки (zoon / spravker / jsprav / restoran.cafe /
edagda / сайт сети) в правильный вид: точный тип по тому, как каталог описывает заведение, «Плюс» — живой фразой,
«Минус» — без пометок об источниках и «уточняйте» (остаётся только факт), «Детский билет» и «Бесплатно до» — пусто,
«Взрослый билет» — средний чек, только если он был в источнике. Ничего нового не добавлено.
Запуск: KP_PART=cafes python3 tools/fix_cafes_quality_1111k.py"""
import os, re, sys
import openpyxl
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_helpers import SRC

MARK = "качество 2026-11"
CHECK = {"cafe-rublevka-village": 2500, "cafe-sezam-khutorskaya": 1500}
PLUS = {
 "cafe-shvili-crocus": ("грузинское бистро в ТРК «Vegas Крокус Сити»",
                        "Грузинское бистро в «Vegas Крокус Сити»: хачапури и хинкали. Рядом детская комната"),
 "cafe-rublevka-village": ("загородный ресторан с детской комнатой",
                           "Загородный ресторан при отеле Rublevka Village: кавказская кухня, терраса с видом на сад. "
                           "Есть детская комната, аниматор и детское меню, проводят детские праздники"),
 "cafe-sezam-khutorskaya": ("ресторан с детской комнатой",
                            "Ресторан восточной и международной кухни у метро «Дмитровская», есть банкетный зал. "
                            "Есть детская комната и детское меню, проводят детские праздники"),
 "cafe-mimi-novaya-riga": ("ресторан с детской комнатой",
                           "Ресторан сети MiMi в гастровилле у аутлета «Новая Рига», играет живая музыка. Есть детская комната"),
 "cafe-acharuli-vnukovo": ("аджарский ресторан с детской комнатой",
                           "Аджарский ресторан у метро «Аэропорт Внуково»: хачапури, хинкали. Есть детская комната"),
}


def typ_from(plus):
    p = plus.lower()
    for k, t in (("бургерная", "бургерная"), ("кафе-пекарня", "кафе-пекарня"), ("кафе-пиццерия", "кафе-пиццерия"),
                 ("пиццерия", "пиццерия"), ("кафе-гриль", "кафе-гриль"), ("гастробар", "гастробар"),
                 ("семейное кафе", "семейное кафе"), ("семейный ресторан", "семейный ресторан"),
                 ("загородный ресторан", "загородный ресторан"), ("загородное кафе", "загородное кафе"),
                 ("мясной ресторан", "мясной ресторан"), ("ресторан", "ресторан"), ("кафе", "кафе")):
        if k in p:
            return t + " с детской комнатой"
    return None


def plus_from(plus):
    p = re.sub(r"\s*\(по сайту сети\)", "", plus)
    parts = [x.strip() for x in p.split("·")]
    rest = [x for x in parts[1:] if x and "детская комната" not in x]
    body = parts[0]
    if body.lower() in ("кафе", "ресторан"):
        body = body + " с детской комнатой"
        return body[0].upper() + body[1:]
    s = body + (", " + ", ".join(rest) if rest else "")
    return s + ". Есть детская комната"


wb = openpyxl.load_workbook(SRC)
ws = wb["Места"]
hdr = [c.value for c in ws[1]]
col = {n: i + 1 for i, n in enumerate(hdr)}
n = 0
for r in range(2, ws.max_row + 1):
    pid = ws.cell(r, 1).value
    src = ws.cell(r, col["Источник"]).value or ""
    if not pid or MARK in src:
        continue
    plus = ws.cell(r, col["Плюс"]).value or ""
    minus = ws.cell(r, col["Минус"]).value or ""
    if pid in PLUS:
        t, p = PLUS[pid]
    else:
        t, p = typ_from(plus), plus_from(plus)
    if not t:
        print("skip", pid); continue
    ws.cell(r, col["Тип"]).value = t
    ws.cell(r, col["Плюс"]).value = p
    ws.cell(r, col["Минус"]).value = minus if minus.startswith("Временно не работает") else None
    ws.cell(r, col["Детский билет, ₽"]).value = None
    ws.cell(r, col["Бесплатно до (лет / см)"]).value = None
    ws.cell(r, col["Взрослый билет, ₽"]).value = CHECK.get(pid)
    ws.cell(r, col["Источник"]).value = src + "; " + MARK
    n += 1
    print(pid, "|", t, "|", p)
wb.save(SRC)
print("fixed", n)
