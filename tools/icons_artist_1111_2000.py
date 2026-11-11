"""Робот «художник», 11.11 ~20:00 UTC.
check_unique.py: 2 пары похожих картинок (одинаковый фон и компоновка):
peppi-myachkovsky ~ pirouette-gym-napolny (сиреневый фон, вертикальная фигура по центру),
fd-yasenevaya ~ rgc1-borisovskie-prudy (малиновый фон, высокая фигура по центру).
Pirouette и ЦХГ № 1 оставлены; перерисованы:
- «Пеппи» (студия английского) — облачко речи «Hi!» с рыжими косичками на небесно-голубом фоне;
- «Fitness Дети» (школа гимнастики) — пара гимнастических колец на ремнях, мятный фон.
Запуск из корня: python3 tools/icons_artist_1111_2000.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT

I = {}

# Студия английского «Пеппи» (Марьино) — облачко речи «Hi!», шутка — косички как у Пеппи
I["peppi-myachkovsky"] = (
    "белое облачко речи с надписью «Hi!» и торчащими рыжими косичками с зелёными бантиками",
    "облачко-девочка весело здоровается по-английски, косички торчат в стороны",
    ("#EAF7FF", "#3D8FD6"), f'''
<path d="M32 32 Q20 30 18 18" fill="none" stroke="#E8551E" stroke-width="7" stroke-linecap="round"/>
<path d="M96 32 Q108 30 110 18" fill="none" stroke="#E8551E" stroke-width="7" stroke-linecap="round"/>
<path d="M18 20 l-9 -2 4 8z M110 20 l9 -2 -4 8z" fill="#3DBE5A" {W(1.8)}/>
<path d="M40 92 L30 116 L58 96" fill="#FFFFFF" {W(3.2)}/>
<ellipse cx="64" cy="62" rx="48" ry="38" fill="#FFFFFF" {W(3.2)}/>
<path d="M33 94 L58 96" stroke="#FFFFFF" stroke-width="5"/>
<path d="M36 32 Q50 22 64 30 Q78 22 92 32" fill="#E8551E" {W(2.4)}/>
{eye(50, 46, .8)}{eye(78, 46, .8)}
{blush(38, 56, .8)}{blush(90, 56, .8)}
<text x="64" y="88" text-anchor="middle" font-family="Arial Rounded MT Bold, Arial, sans-serif" font-weight="900" font-size="31" fill="#1F4E9C">Hi!</text>
{sparkle(108, 102, 4)}''')

# Школа гимнастики «Fitness Дети» (Ясенево) — гимнастические кольца
def ring(cx, cy, tilt):
    return f'''<g transform="rotate({tilt} {cx} 0)">
<path d="M{cx-4} 0 L{cx-4} {cy-24} M{cx+4} 0 L{cx+4} {cy-24}" stroke="#2B3A55" stroke-width="2.6"/>
<rect x="{cx-5.5}" y="-4" width="11" height="{cy-22}" rx="3" fill="#F2C14E" {W(2.4)}/>
<circle cx="{cx}" cy="{cy}" r="21" fill="none" stroke="#2B3A55" stroke-width="15"/>
<circle cx="{cx}" cy="{cy}" r="21" fill="none" stroke="#C98A4B" stroke-width="10"/>
<path d="M{cx-14} {cy-12} A18 18 0 0 1 {cx+4} {cy-20}" fill="none" stroke="#E8B27A" stroke-width="3" stroke-linecap="round"/>
{eye(cx-7, cy+21, .62)}{eye(cx+7, cy+21, .62)}
</g>'''

I["fd-yasenevaya"] = (
    "пара деревянных гимнастических колец на жёлтых ремнях",
    "два кольца-близнеца с глазками раскачиваются навстречу друг другу, будто просят: «повиси на нас!»",
    ("#EFFFF8", "#2DB592"), f'''
{ring(42, 78, 8)}{ring(86, 78, -8)}
{sparkle(64, 40, 5, "#FFF6B0")}{sparkle(20, 110, 3)}{sparkle(110, 112, 3.5)}''')

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
