"""Робот «художник», 10.11 ~02:00 UTC. check_unique.py нашёл 1 похожую пару картинок:
balet-s-2-let-odintsovo ~ dzhima-gym-perova-polya. Балет оставляем, «Джиму» рисуем заново — своей идеей и палитрой.
Запуск из корня: python3 tools/icons_artist_1110_0200.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT

I = {}

GI = "#F7C948"   # жёлтая шкурка
SP = "#C9782B"   # пятна

# Школа гимнастики «Джима», Перово Поле — длинноногий жирафёнок сел в продольный шпагат и машет лентой
I["dzhima-gym-perova-polya"] = (
    "жирафёнок в фиолетовом купальнике с длинными пятнистыми ножками",
    "сел в продольный шпагат на мятном ковре и поднял над головой палочку с розовой лентой-волной",
    ("#FFE6CF", "#EE8A55"), f'''
<path d="M-4 100 Q64 92 132 100 V132 H-4Z" fill="#8FE0C8" {W(2.6)}/>
<ellipse cx="64" cy="104" rx="50" ry="4" fill="#000" opacity=".15"/>
<!-- ноги в шпагате -->
<path d="M58 96 L14 98 Q10 99 12 103 L58 104Z" fill="{GI}" {W(2.8)}/>
<path d="M70 96 L114 98 Q118 99 116 103 L70 104Z" fill="{GI}" {W(2.8)}/>
<path d="M10 97 h7 v7 h-8Z" fill="#6B4A2E" {W(2)}/><path d="M118 97 h-7 v7 h8Z" fill="#6B4A2E" {W(2)}/>
<circle cx="30" cy="100" r="2.4" fill="{SP}"/><circle cx="44" cy="100" r="2" fill="{SP}"/>
<circle cx="86" cy="100" r="2" fill="{SP}"/><circle cx="100" cy="100" r="2.4" fill="{SP}"/>
<!-- туловище в купальнике -->
<path d="M50 104 Q48 80 54 68 Q64 62 74 68 Q80 80 78 104Z" fill="#8E5CE0" {W(3)}/>
<path d="M56 74 L64 84 L72 74" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".8"/>
<!-- руки вверх к палочке -->
<path d="M54 72 Q44 60 46 46" fill="none" {W(6.5)}/><path d="M54 72 Q44 60 46 46" fill="none" stroke="{GI}" stroke-width="3.3" stroke-linecap="round"/>
<path d="M74 72 Q84 60 84 50" fill="none" {W(6.5)}/><path d="M74 72 Q84 60 84 50" fill="none" stroke="{GI}" stroke-width="3.3" stroke-linecap="round"/>
<!-- шея и голова -->
<path d="M59 68 L59 40 Q64 36 69 40 L69 68Z" fill="{GI}" {W(2.8)}/>
<circle cx="62" cy="52" r="2.2" fill="{SP}"/><circle cx="66" cy="60" r="2" fill="{SP}"/><circle cx="66" cy="45" r="1.8" fill="{SP}"/>
<path d="M57 22 L55 12 M71 22 L73 12" fill="none" {W(2.6)}/>
<circle cx="55" cy="11" r="3" fill="#6B4A2E" {W(1.8)}/><circle cx="73" cy="11" r="3" fill="#6B4A2E" {W(1.8)}/>
<ellipse cx="50" cy="24" rx="5" ry="2.8" fill="{GI}" {W(2)} transform="rotate(-25 50 24)"/>
<ellipse cx="78" cy="24" rx="5" ry="2.8" fill="{GI}" {W(2)} transform="rotate(25 78 24)"/>
<ellipse cx="64" cy="30" rx="13" ry="11.5" fill="{GI}" {W(2.8)}/>
<ellipse cx="64" cy="37" rx="8" ry="5" fill="#FFE3A3" {W(2)}/>
{eye(59, 27, .6)}{eye(69, 27, .6)}{blush(54, 33, .7)}{blush(74, 33, .7)}
<path d="M61 38 Q64 40.5 67 38" fill="none" {W(1.8)}/>
<!-- палочка и лента -->
<path d="M84 50 L92 32" fill="none" {W(2.6)}/>
<path d="M92 32 Q104 22 98 15 Q88 10 93 24 Q98 34 106 28 Q114 22 110 40" fill="none" stroke="#F0418C" stroke-width="5" stroke-linecap="round"/>
<circle cx="46" cy="45" r="3.2" fill="{GI}" {W(2)}/>
{sparkle(24, 40, 6, "#fff")}{sparkle(36, 22, 4, "#FFF6B0")}''')


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
    print("нарисовано:", len(I))
