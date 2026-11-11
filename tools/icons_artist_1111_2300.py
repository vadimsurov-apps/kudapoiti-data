"""Робот «художник», 11.11 ~23:00 UTC.
check_unique.py: 1 пара похожих картинок (сиреневый фон, фигура по центру):
barsukova-aerial-skladochnaya ~ volshebnaya-strana-beskudnikovsky-21.
Воздушная гимнастика оставлена; перерисована «Волшебная страна» (английский от 4 лет) —
красный британский почтовый ящик-тумба с мордашкой, из щели выглядывает письмо «ABC», солнечный фон.
Запуск из корня: python3 tools/icons_artist_1111_2300.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT

I = {}

# Центр «Волшебная страна» (Бескудниково): английский — красный лондонский почтовый ящик-тумба
I["volshebnaya-strana-beskudnikovsky-21"] = (
    "красный круглый британский почтовый ящик-тумба с куполом-крышкой и мордашкой",
    "из щели для писем, как язычок, высовывается белый конверт с синими буквами «ABC», ящик стоит на зелёной травке",
    ("#FFF8D6", "#F2B53A"), f'''
<ellipse cx="64" cy="114" rx="36" ry="8" fill="#6CC46A" {W(2.4)}/>
<rect x="38" y="44" width="52" height="68" rx="6" fill="#E0312F" {W(3.2)}/>
<path d="M34 46 Q34 18 64 18 Q94 18 94 46 Z" fill="#E0312F" {W(3.2)}/>
<rect x="32" y="42" width="64" height="9" rx="4" fill="#B8221F" {W(2.8)}/>
<circle cx="64" cy="16" r="5" fill="#B8221F" {W(2.4)}/>
<rect x="34" y="104" width="60" height="8" rx="3" fill="#B8221F" {W(2.6)}/>
<rect x="46" y="58" width="36" height="6" rx="3" fill="#3B3355"/>
<g transform="rotate(-6 64 66)">
<rect x="49" y="60" width="30" height="24" rx="2" fill="#FFFFFF" {W(2.4)}/>
<path d="M49 61 L64 71 L79 61" fill="none" {W(1.8)}/>
<text x="64" y="82" text-anchor="middle" font-family="Arial Rounded MT Bold, Arial, sans-serif" font-weight="900" font-size="10" fill="#1F4E9C">ABC</text>
</g>
{eye(54, 34, .75)}{eye(74, 34, .75)}
{blush(46, 41, .7)}{blush(82, 41, .7)}
{smile(64, 39, 4, .8)}
{sparkle(108, 36, 5)}{sparkle(20, 70, 3.5)}''')

if __name__ == "__main__":
    for pid, (hero, scene, (a, b), body) in I.items():
        open(os.path.join(ROOT, "icons-src", f"{pid}.svg"), "w").write(bgsvg(a, b, body))
    reg = os.path.join(ROOT, "icons-src", "subjects.txt"); txt = open(reg, encoding="utf-8").read()
    for pid in I:
        txt = re.sub(rf"^{re.escape(pid)} — .*\n", "", txt, flags=re.M)
    if not txt.endswith("\n"):
        txt += "\n"
    txt += "".join(f"{pid} — герой: {h} | сцена: {sc}\n" for pid, (h, sc, _, _) in I.items())
    open(reg, "w", encoding="utf-8").write(txt)
    print(" ".join(I))
