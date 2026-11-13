"""Робот «художник», 13.11 ~08:00 UTC.
check_unique.py: 3 иконки с повтором — baglay-aerial-tushinskaya похожа по цвету и компоновке (сиреневый фон,
маленькая фигурка под потолком) на barsukova-aerial-skladochnaya и progress-lobnya-krupskoy. Те две оставлены,
baglay перерисована заново: свой снаряд (воздушная луна), своя сцена и коралловая палитра.
Запуск из корня: python3 tools/icons_artist_1113_0800.py"""
import math, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT
from icons_artist_1112_1400 import limb


def crescent(cx, cy, r, ix, iy, ir):
    """полумесяц: большой круг (cx,cy,r) минус круг (ix,iy,ir)"""
    dx, dy = ix - cx, iy - cy
    d = math.hypot(dx, dy)
    a = (r * r - ir * ir + d * d) / (2 * d)
    h = math.sqrt(r * r - a * a)
    mx, my = cx + a * dx / d, cy + a * dy / d
    p1 = (mx + h * dy / d, my - h * dx / d)
    p2 = (mx - h * dy / d, my + h * dx / d)
    return (f"M{p1[0]:.1f} {p1[1]:.1f} A{r} {r} 0 1 0 {p2[0]:.1f} {p2[1]:.1f} "
            f"A{ir} {ir} 0 0 1 {p1[0]:.1f} {p1[1]:.1f} Z")


I = {}

# Школа воздушной гимнастики Марии Баглай, Тушинская (дети с 3 лет): воздушная луна
I["baglay-aerial-tushinskaya"] = (
    "золотая воздушная луна-полумесяц с сонной улыбкой",
    "висит на стропе в зале, а в её изгибе сидит малыш в красном комбинезоне и болтает ножками",
    ("#FFE6DA", "#F07A62"), f'''
<path d="M62 -2 L62 22" fill="none" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M62 -2 L62 22" fill="none" stroke="#FFF4E8" stroke-width="3.5" stroke-linecap="round"/>
<path d="{crescent(58, 72, 46, 80, 62, 36)}" fill="#FFC93C" {W(3.4)}/>
<path d="M30 52 Q24 72 34 94" fill="none" stroke="#FFE68A" stroke-width="5" stroke-linecap="round" opacity=".9"/>
<path d="M27 70 Q31 75 35 70" fill="none" {W(2.6)}/>
<ellipse cx="25" cy="80" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/>
<path d="M30 84 Q36 89 41 84" fill="none" {W(2.6)}/>
{limb("M66 98 Q74 108 70 116", "#E8443A", 8)}
{limb("M76 96 Q88 102 90 112", "#E8443A", 8)}
<ellipse cx="69" cy="118" rx="5.5" ry="3.6" fill="#FFFFFF" {W(2.4)}/>
<ellipse cx="91" cy="114" rx="5.5" ry="3.6" fill="#FFFFFF" {W(2.4)}/>
<path d="M60 98 Q58 78 72 74 Q86 76 84 98 Z" fill="#E8443A" {W(3)}/>
{limb("M64 80 Q56 70 60 58", "#FFD9BE", 6)}
{limb("M80 80 Q92 74 96 64", "#FFD9BE", 6)}
<circle cx="72" cy="62" r="12" fill="#FFD9BE" {W(3)}/>
<path d="M60 60 Q62 46 74 48 Q86 50 84 60 Q78 54 70 56 Q64 56 60 60Z" fill="#8A4B2A" {W(2.4)}/>
{eye(68, 63, 0.6)}{eye(77, 63, 0.6)}
{blush(64, 68, 0.6)}{blush(81, 68, 0.6)}
{smile(72.5, 67, 3, 0.8)}
{sparkle(104, 34, 6)}{sparkle(22, 30, 4)}{sparkle(108, 92, 4)}
''')


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
