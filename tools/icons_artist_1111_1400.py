"""Робот «художник», 11.11 ~14:00 UTC.
check_unique.py: 2 пары похожих картинок (одинаковый тёмно-синий «ночной» фон с мелкими звёздами):
kosmik-sergiev-posad ~ piksel-podolsk, akademiya-budushchego-varshavskoe ~ montessori-klass-savvinskoe.
Кинотеатр «Космик» и «Академия будущего» оставлены; перерисованы:
- «Пиксель» (школа программирования) — значок кода </> с весёлой косой чертой на лаймовом фоне;
- «Монтессори класс» — розовая башня Монтессори на коврике на лавандовом фоне.
Запуск из корня: python3 tools/icons_artist_1111_1400.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT

I = {}


def px_heart(x, y, k, color):
    """пиксельное сердечко из квадратиков (шутка по названию «Пиксель»)"""
    cells = ["0110110", "1111111", "1111111", "0111110", "0011100", "0001000"]
    out = ""
    for r, row in enumerate(cells):
        for c, ch in enumerate(row):
            if ch == "1":
                out += f'<rect x="{x+c*k}" y="{y+r*k}" width="{k}" height="{k}" fill="{color}"/>'
    return out


# Школа программирования «Пиксель» (Подольск) — знак кода </>, косая черта — персонаж
I["piksel-podolsk"] = (
    "знак кода </> из толстых белых уголков и оранжевой косой черты с мордашкой",
    "косая черта радостно стоит между уголками кода, над ней парит маленькое пиксельное сердечко",
    ("#F9FFE0", "#8CC63F"), f'''
<path d="M42 40 L16 66 L42 92" fill="none" {W(17)}/>
<path d="M42 40 L16 66 L42 92" fill="none" stroke="#FFFFFF" stroke-width="10.5" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M86 40 L112 66 L86 92" fill="none" {W(17)}/>
<path d="M86 40 L112 66 L86 92" fill="none" stroke="#FFFFFF" stroke-width="10.5" stroke-linecap="round" stroke-linejoin="round"/>
<g transform="rotate(18 64 68)">
<rect x="52" y="30" width="24" height="76" rx="12" fill="#FF8A2B" {W(3.2)}/>
<rect x="56" y="36" width="5" height="26" rx="2.5" fill="#FFC27A"/>
{eye(58, 62, .72)}{eye(70, 62, .72)}
{blush(55, 70, .7)}{blush(73, 70, .7)}
{smile(64, 70, 4, .9)}
</g>
{px_heart(84, 14, 3.4, "#E8336B")}
{sparkle(24, 106, 4)}{sparkle(106, 106, 3)}''')

# Частная школа «Монтессори класс» (Железнодорожный) — розовая башня Монтессори
def cube(x, y, a, front="#F48FB1", top="#FBC4D8", side="#D9658F", d=None):
    d = d if d is not None else a * .28
    return (f'<path d="M{x} {y} L{x+d} {y-d} L{x+a+d} {y-d} L{x+a} {y}Z" fill="{top}" {W(2.4)}/>'
            f'<path d="M{x+a} {y} L{x+a+d} {y-d} L{x+a+d} {y+a-d} L{x+a} {y+a}Z" fill="{side}" {W(2.4)}/>'
            f'<rect x="{x}" y="{y}" width="{a}" height="{a}" fill="{front}" {W(2.6)}/>')

parts, y = [], 106
for a in (30, 22, 16, 12, 8, 5):
    y -= a
    parts.append(cube(60 - a / 2, y, a))
tower = "".join(parts)
I["montessori-klass-savvinskoe"] = (
    "розовая башня Монтессори из шести кубиков от большого к крошечному",
    "стоит ровной пирамидкой на бежевом рабочем коврике, нижний большой кубик улыбается, сверху блестит самый маленький",
    ("#F6F0FF", "#8F7AD8"), f'''
<path d="M10 100 L118 100 L124 120 L4 120Z" fill="#E9D3A8" {W(2.6)}/>
<path d="M16 108 H112" stroke="#C9A976" stroke-width="2" stroke-dasharray="4 4"/>
{tower}
{eye(54, 87, .75)}{eye(66, 87, .75)}
{blush(50, 95, .7)}{blush(70, 95, .7)}
{smile(60, 94, 4, .9)}
{sparkle(76, 18, 4.5, "#FFF6B0")}{sparkle(98, 34, 3.5)}{sparkle(24, 44, 3)}''')

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
