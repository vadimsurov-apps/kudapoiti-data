"""Робот «художник», 08.11 ~20:00 UTC. check_unique.py нашёл одну похожую пару: harmony-ballet-vargi ~
sinergiya-akhmatovoy (оба — мальчик в прыжке-шпагате в луче софита). Балетную «Гармонию» оставляем,
«Синергию» рисуем заново: девочка кружится, юбка-солнце раскрылась колоколом.
Запуск из корня: python3 tools/icons_artist_1108_2000.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT
from icons_artist_1108_0800 import limb
from icons_artist_1108_1400 import head

I = {}

# Академия хореографии «Синергия», ул. Анны Ахматовой — девочка кружится, юбка-солнце взлетела колоколом
I["sinergiya-akhmatovoy"] = ("девочка с рыжими косичками в солнечно-жёлтой юбке-солнце",
                             "кружится на одной ножке, юбка взлетела широким колоколом, косички разлетелись, вокруг дуги вращения",
                             ("#C8F4EC", "#2A9D8F"), f'''
<ellipse cx="64" cy="118" rx="26" ry="4.5" fill="#000" opacity=".22"/>
<path d="M14 70 Q8 92 30 102" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
<path d="M114 70 Q120 92 98 102" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
{limb("M62 92 L60 114", "#FFD9B8", 7)}
{limb("M68 92 L82 104", "#FFD9B8", 7)}
<ellipse cx="59" cy="115" rx="5" ry="3" fill="#E8403A" {W(1.8)}/>
<path d="M64 62 Q30 70 16 92 Q40 100 64 98 Q88 100 112 92 Q98 70 64 62Z" fill="#FFC928" {W(3)}/>
<path d="M30 88 Q44 80 50 72 M46 96 Q54 84 57 70 M82 96 Q74 84 71 70 M98 88 Q84 80 78 72" fill="none" stroke="#E8A010" stroke-width="2" stroke-linecap="round"/>
<path d="M16 92 Q40 100 64 98 Q88 100 112 92" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="3 4" opacity=".9"/>
<path d="M56 48 Q64 44 72 48 L70 66 H58Z" fill="#E8403A" {W(2.6)}/>
{limb("M57 52 Q44 40 40 24", "#FFD9B8", 7)}
{limb("M71 52 Q84 40 88 24", "#FFD9B8", 7)}
{limb("M54 30 Q40 32 30 26", "#E8742A", 7)}
{limb("M74 30 Q88 32 98 26", "#E8742A", 7)}
<circle cx="28" cy="25" r="3.5" fill="#2E6AD8" {W(1.8)}/><circle cx="100" cy="25" r="3.5" fill="#2E6AD8" {W(1.8)}/>
{head(64, 34, 12, "#E8742A", .45)}
{sparkle(108, 46, 5, "#FFF6B0")}{sparkle(20, 50, 4, "#FFF6B0")}''')


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
