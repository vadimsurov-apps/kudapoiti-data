"""Робот «художник», 14.11 ~02:00 UTC.
check_unique.py: 2 похожие пары — kodklass-dubna ~ progym-lyubertsy-iskra (тёмный фон, светлая линия по диагонали),
balet-s-2-let-odintsovo ~ probalero-reutov-yubileyny (розовый фон, девочка с поднятыми руками по центру).
progym и probalero оставлены, kodklass и balet-s-2-let-odintsovo перерисованы заново.
Запуск из корня: python3 tools/icons_artist_1114_0200.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT
from icons_artist_1112_1400 import limb

I = {}

# КодКласс (Дубна) — компьютерные курсы: светлое окно редактора кода и стрелка-курсор, жмущая «▶ Запуск»
I["kodklass-dubna"] = (
    "оранжевая стрелка-курсор мыши с мордашкой",
    "нажимает зелёную кнопку «▶» в белом окне редактора кода с цветными строчками программы",
    ("#F1FBD6", "#8FCB4E"), f'''
<rect x="14" y="26" width="92" height="70" rx="9" fill="#FFFFFF" {W(3.2)}/>
<path d="M14 35 Q14 26 23 26 H97 Q106 26 106 35 V40 H14Z" fill="#4C8DF0" {W(3.2)}/>
<circle cx="24" cy="33" r="2.6" fill="#FF6B6B"/><circle cx="32" cy="33" r="2.6" fill="#FFD23F"/><circle cx="40" cy="33" r="2.6" fill="#5BD37A"/>
<path d="M24 52 H44" stroke="#C36BF0" stroke-width="5" stroke-linecap="round"/>
<path d="M50 52 H66" stroke="#4C8DF0" stroke-width="5" stroke-linecap="round"/>
<path d="M32 64 H58" stroke="#FF9F43" stroke-width="5" stroke-linecap="round"/>
<path d="M32 76 H48" stroke="#5BD37A" stroke-width="5" stroke-linecap="round"/>
<circle cx="84" cy="74" r="13" fill="#3CC46A" {W(3)}/>
<path d="M80 67 L91 74 L80 81Z" fill="#FFFFFF"/>
<path d="M78 78 L78 118 L88 108 L96 124 L104 120 L96 104 L110 104Z" fill="#FF8A2B" {W(3.4)}/>
{eye(86, 98, 0.62)}{eye(94, 98, 0.62)}
{blush(83, 104, 0.5)}
{smile(90, 103, 3, 0.7)}
{sparkle(100, 60, 5)}{sparkle(108, 82, 3.5)}
''')

# Школа «Балет с 2 лет» (Одинцово): слонёнок-малыш — тяжёлый, а танцует легко
I["balet-s-2-let-odintsovo"] = (
    "серый слонёнок-малыш в сиреневой пачке",
    "стоит на цыпочках на одной ножке, а хоботом над головой поднимает розовый бантик",
    ("#E2F7F0", "#6FCDB0"), f'''
<ellipse cx="62" cy="116" rx="26" ry="5" fill="#3E8F78" opacity=".25"/>
{limb("M56 92 L54 114", "#B9BFD0", 9)}
{limb("M74 94 Q92 104 106 96", "#B9BFD0", 9)}
<path d="M30 88 Q62 70 94 88 Q90 98 62 100 Q34 98 30 88Z" fill="#D9C2FF" {W(3)}/>
<path d="M36 90 Q46 94 50 98 M62 90 V100 M88 90 Q78 94 74 98" fill="none" stroke="#B79AF2" stroke-width="2"/>
<ellipse cx="62" cy="76" rx="20" ry="16" fill="#B9BFD0" {W(3.2)}/>
<path d="M36 46 Q18 44 20 62 Q24 74 40 66Z" fill="#B9BFD0" {W(3)}/>
<path d="M88 46 Q106 44 104 62 Q100 74 84 66Z" fill="#B9BFD0" {W(3)}/>
<path d="M30 52 Q26 60 36 62" fill="none" stroke="#F2A9C4" stroke-width="3.5" stroke-linecap="round"/>
<path d="M94 52 Q98 60 88 62" fill="none" stroke="#F2A9C4" stroke-width="3.5" stroke-linecap="round"/>
<circle cx="62" cy="54" r="22" fill="#B9BFD0" {W(3.2)}/>
{limb("M62 62 Q66 40 58 26 Q54 18 60 14", "#B9BFD0", 9)}
<path d="M50 12 L60 16 L50 22Z M70 10 L60 16 L70 22Z" fill="#FF7FB0" {W(2.2)}/>
<circle cx="60" cy="16" r="3" fill="#FF7FB0" {W(2)}/>
{eye(52, 52, 0.75)}{eye(72, 52, 0.75)}
{blush(46, 61, 0.8)}{blush(78, 61, 0.8)}
<path d="M56 66 Q58 70 62 68" fill="none" {W(2.4)}/>
<ellipse cx="53" cy="115" rx="6" ry="3" fill="#FFB3CF" {W(2.2)}/>
{sparkle(100, 30, 5)}{sparkle(24, 32, 4)}{sparkle(106, 104, 3.5)}
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
