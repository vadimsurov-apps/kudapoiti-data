"""Робот «художник», 11.11 05:00 UTC.
check_unique.py: 1 пара похожих картинок (фон и компоновка) — fabrika-dance-sergiev-posad ~ karate-champion-ramenskoe.
karate-champion остаётся, «Фабрика» (танцевальный спорт) перерисована: шестерёнки фабрики танцуют вальс.
(Диско-шар отброшен — он уже есть у perspektiva-lyublinskaya.)
Запуск из корня: python3 tools/icons_artist_1111_0500.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT

I = {}


def _gear(cx, cy, r, teeth, fill, rot=0):
    """шестерёнка: круг с прямоугольными зубцами"""
    import math
    out = []
    for i in range(teeth):
        a = rot + 360 * i / teeth
        out.append(f'<rect x="{cx-r*.22:.1f}" y="{cy-r-r*.32:.1f}" width="{r*.44:.1f}" height="{r*.5:.1f}" rx="2" '
                   f'fill="{fill}" {W(2.6)} transform="rotate({a:.1f} {cx} {cy})"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" {W(3)}/>')
    return "".join(out)


# Танцевальный центр «Фабрика» (Сергиев Посад) — две шестерёнки фабрики кружатся в вальсе как бальная пара
I["fabrika-dance-sergiev-posad"] = (
    "две шестерёнки-танцоры: большая оранжевая в чёрной бабочке и маленькая розовая в пышной оборке-юбке",
    "кружатся в бальном вальсе на паркете, сцепившись зубчиками, как за руки, вокруг разлетаются нотки",
    ("#E3FFF6", "#3FB8A0"), f'''
<path d="M0 106 H128 V128 H0Z" fill="#B9773E"/>
<path d="M0 106 H128" {W(2.6)}/>
<path d="M14 106 L24 128 M40 106 L30 128 M58 106 L68 128 M84 106 L74 128 M102 106 L112 128" stroke="#8E5528" stroke-width="2"/>
<g transform="rotate(-8 64 64)">
{_gear(46, 58, 22, 9, "#FF9A2E", 10)}
<circle cx="46" cy="58" r="12" fill="#FFC77A"/>
{eye(40, 54, .62)}{eye(53, 54, .62)}
{blush(36, 62, .6)}{blush(57, 62, .6)}
{smile(46, 62, 4, .9)}
<path d="M38 75 L46 79 L38 83Z M54 75 L46 79 L54 83Z" fill="#1F1A2E" {W(2)}/>
<circle cx="46" cy="79" r="2.4" fill="#1F1A2E"/>
<path d="M74 82 L94 82 Q100 92 106 102 Q102 106 98 102 Q94 106 90 102 Q86 106 82 102 Q78 106 74 102 Q70 106 66 102 Q70 92 74 82Z" fill="#FF8FC4" {W(2.6)}/>
<path d="M72 92 Q84 96 98 92" fill="none" stroke="#FFD1E8" stroke-width="2.2" stroke-linecap="round"/>
{_gear(84, 72, 15, 7, "#FF6FAE", 4)}
<circle cx="84" cy="72" r="7.5" fill="#FFC2DD"/>
{eye(80, 70, .48)}{eye(88, 70, .48)}
<path d="M81 75 Q84 78 87 75" fill="none" {W(1.8)}/>
<path d="M76 54 L80 46 L84 52 L88 46 L92 54" fill="#FFD84A" {W(2)}/>
</g>
<path d="M104 20 V36" {W(2.6)}/><ellipse cx="100" cy="37" rx="4.6" ry="3.4" fill="{O}"/><path d="M104 20 Q110 22 112 28" fill="none" {W(2.6)}/>
<path d="M18 30 V44" {W(2.6)}/><ellipse cx="14" cy="45" rx="4.2" ry="3.2" fill="{O}"/>
{sparkle(112, 60, 4.5)}{sparkle(22, 86, 3.5)}''')

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
