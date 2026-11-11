"""Робот «художник», 11.11 05:00 UTC.
check_unique.py: 1 пара похожих картинок (фон и компоновка) — fabrika-dance-sergiev-posad ~ karate-champion-ramenskoe.
karate-champion остаётся, «Фабрика» (танцевальный спорт) перерисована: зеркальный диско-шар над танцполом.
Запуск из корня: python3 tools/icons_artist_1111_0500.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT

I = {}


def _tiles():
    """зеркальные квадратики диско-шара: сетка, обрезанная по кругу шара"""
    out = ['<clipPath id="ball"><circle cx="64" cy="54" r="31"/></clipPath><g clip-path="url(#ball)">']
    cols = ["#E9EEF7", "#C9D3E6", "#F7F9FD", "#B5C1DA", "#DCE4F2"]
    k = 0
    for row, y in enumerate(range(22, 88, 9)):
        for x in range(30 + (row % 2) * 4, 100, 9):
            out.append(f'<rect x="{x}" y="{y}" width="8.4" height="8.4" fill="{cols[k % 5]}"/>')
            k += 1
    out.append('<rect x="70" y="31" width="8.4" height="8.4" fill="#FF7AD9"/>'
               '<rect x="39" y="67" width="8.4" height="8.4" fill="#5FE3FF"/>'
               '<rect x="84" y="58" width="8.4" height="8.4" fill="#FFE36B"/></g>')
    return "".join(out)


# Танцевальный центр «Фабрика» (Сергиев Посад) — диско-шар раскачивается и пускает цветные зайчики на танцпол
I["fabrika-dance-sergiev-posad"] = (
    "зеркальный диско-шар с весёлой мордашкой",
    "висит на цепочке под потолком танцзала, подмигивает и пускает вниз цветные лучи — на тёмном паркете пляшут розовые, голубые и жёлтые зайчики",
    ("#5B3FA8", "#1C0F45"), f'''
<path d="M0 104 Q64 96 128 104 V128 H0Z" fill="#3A2416"/>
<path d="M0 104 Q64 96 128 104" fill="none" {W(2.6)}/>
<path d="M50 80 L18 108 L34 112Z" fill="#FF7AD9" opacity=".45"/>
<path d="M64 86 L56 114 L74 114Z" fill="#5FE3FF" opacity=".45"/>
<path d="M80 80 L100 110 L114 104Z" fill="#FFE36B" opacity=".45"/>
<ellipse cx="26" cy="110" rx="10" ry="3.6" fill="#FF7AD9"/>
<ellipse cx="65" cy="114" rx="10" ry="3.6" fill="#5FE3FF"/>
<ellipse cx="107" cy="107" rx="10" ry="3.6" fill="#FFE36B"/>
<path d="M64 0 V23" {W(3)}/>
<rect x="59" y="17" width="10" height="7" rx="2" fill="#B5C1DA" {W(2.4)}/>
{_tiles()}
<circle cx="64" cy="54" r="31" fill="none" {W(3.4)}/>
<path d="M44 34 Q52 27 62 26" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".9"/>
<circle cx="64" cy="56" r="15" fill="#F7F9FD" opacity=".85"/>
{eye(57, 52, .7)}
<path d="M67 52 Q71 49 75 52" fill="none" {W(2.4)}/>
{blush(52, 60, .7)}{blush(77, 60, .7)}
{smile(64, 60, 5, 1)}
{sparkle(104, 24, 6)}{sparkle(22, 34, 4.5, "#FFE36B")}{sparkle(110, 70, 3.5, "#5FE3FF")}{sparkle(18, 74, 3.5, "#FF7AD9")}''')

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
