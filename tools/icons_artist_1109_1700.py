"""Робот «художник», 09.11 ~17:00 UTC. check_unique.py нашёл 3 похожие пары картинок:
attitude-volskaya ~ futbolika-maryina-roshcha, chg1-pererva ~ magiya-tatyanin-park, alexstars-sovkhoznaya ~ demetra-kubanskaya.
Из каждой пары одну оставляем, вторую рисуем заново — каждую отдельно, своей идеей и своей палитрой.
Запуск из корня: python3 tools/icons_artist_1109_1700.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT
from icons_artist_1108_0800 import limb
from icons_artist_1108_1400 import head

I = {}

# 1. Футбольная школа «Футболика», Марьина Роща — девочка отбивает мяч головой, вид сбоку, лимонный фон
I["futbolika-maryina-roshcha"] = (
    "девочка с хвостиком в сиреневой футболке с номером 7",
    "в прыжке отбивает футбольный мяч лбом, мяч отлетает вверх с дугами удара",
    ("#FFF3A6", "#E0A800"), f'''
<ellipse cx="54" cy="119" rx="22" ry="4" fill="#000" opacity=".2"/>
{limb("M50 88 L40 106 L46 114", "#FFD9B8", 7)}
{limb("M60 88 L70 104 L64 112", "#FFD9B8", 7)}
<path d="M40 112 h9 v5 h-11Z" fill="#2B2B2B" {W(1.8)}/><path d="M62 110 h9 v5 h-11Z" fill="#2B2B2B" {W(1.8)}/>
<path d="M44 80 h22 l2 10 h-26Z" fill="#3A3F8F" {W(2.4)}/>
<path d="M42 56 Q55 50 68 56 L68 82 H42Z" fill="#B48CF0" {W(2.6)}/>
<text x="55" y="76" font-family="Arial" font-weight="bold" font-size="14" fill="#fff" text-anchor="middle">7</text>
{limb("M43 60 Q32 66 26 58", "#FFD9B8", 7)}
{limb("M67 60 Q78 68 86 62", "#FFD9B8", 7)}
<path d="M44 34 Q32 30 26 40 Q32 38 38 42Z" fill="#7A4A26" {W(2.2)}/>
{head(52, 42, 13, "#7A4A26", .45)}
<circle cx="74" cy="22" r="15" fill="#fff" {W(2.8)}/>
<path d="M74 15 l6 4.5 -2.3 7 h-7.4 l-2.3 -7Z" fill="#2B2B2B"/>
<path d="M74 15 V7 M80 19.5 L88 16 M77.7 26.5 L82 33 M70.3 26.5 L66 33 M68 19.5 L60 16" fill="none" {W(1.8)}/>
<path d="M92 12 Q98 20 94 30 M98 6 Q106 18 101 32" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
{sparkle(104, 52, 5, "#fff")}''')

# 2. Центр художественной гимнастики №1 (Марьино) — гимнастический мяч-чемпион с медалью «1»
I["chg1-pererva"] = (
    "коралловый мяч для художественной гимнастики с золотой медалью «1» на ленточке",
    "высоко подпрыгнул над ковром, внизу пунктир-дуга прыжка и маленькая тень",
    ("#C9F1E6", "#3BA88E"), f'''
<ellipse cx="64" cy="117" rx="16" ry="3.5" fill="#000" opacity=".2"/>
<path d="M14 108 Q30 60 52 50" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="4 5" stroke-linecap="round" opacity=".9"/>
<circle cx="70" cy="56" r="34" fill="#FF7A6B" {W(3)}/>
<path d="M44 40 Q60 26 82 28" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".55"/>
<circle cx="52" cy="70" r="2" fill="#fff" opacity=".8"/><circle cx="92" cy="44" r="2" fill="#fff" opacity=".8"/><circle cx="88" cy="76" r="1.6" fill="#fff" opacity=".8"/>
{face(70, 52, 10, 1.05)}
<path d="M58 76 L70 88 L82 76" fill="none" stroke="#2E6AD8" stroke-width="5" stroke-linejoin="round"/>
<circle cx="70" cy="96" r="10" fill="#FFC928" {W(2.6)}/>
<text x="70" y="101" font-family="Arial" font-weight="bold" font-size="13" fill="#8A5A00" text-anchor="middle">1</text>
{sparkle(108, 22, 6, "#FFF6B0")}{sparkle(22, 30, 4, "#fff")}''')

# 3. Школа бальных танцев «Деметра», Люблино — голубая бальная туфелька с колоском делает реверанс
I["demetra-kubanskaya"] = (
    "небесно-голубая бальная туфелька на каблучке с золотым колоском у ремешка",
    "приседает в реверансе на ёлочке паркета, носок изящно вытянут вперёд",
    ("#FFE1E8", "#D9708C"), f'''
<path d="M0 100 H128 V128 H0Z" fill="#C98B5A"/>
<path d="M0 100 L14 114 L28 100 L42 114 L56 100 L70 114 L84 100 L98 114 L112 100 L126 114 M0 114 L14 128 L28 114 L42 128 L56 114 L70 128 L84 114 L98 128 L112 114 L126 128" fill="none" stroke="#9C6238" stroke-width="2"/>
<path d="M0 100 H128" {W(2.4)}/>
<ellipse cx="62" cy="101" rx="40" ry="4" fill="#000" opacity=".2"/>
<path d="M84 84 L90 100 H84 L78 88Z" fill="#2E5FB8" {W(2.6)}/>
<path d="M14 96 Q12 84 28 82 Q44 80 54 84 Q70 86 86 66 Q98 60 100 72 Q100 84 88 88 Q72 92 58 98 Q38 103 20 101 Q14 100 14 96Z" fill="#7EC4F2" {W(3)}/>
<path d="M54 84 Q70 86 86 66 Q92 70 90 78 Q76 88 58 90 Q54 88 54 84Z" fill="#2E5FB8" {W(2.2)}/>
<path d="M24 90 Q34 86 44 88" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".7"/>
{face(36, 92, 6.5, .75)}
<path d="M92 66 Q96 46 100 26" fill="none" stroke="#C88A10" stroke-width="2.4" stroke-linecap="round"/>
<ellipse cx="99" cy="30" rx="3.2" ry="5.5" fill="#FFC928" {W(1.6)} transform="rotate(30 99 30)"/>
<ellipse cx="95" cy="38" rx="3.2" ry="5.5" fill="#FFC928" {W(1.6)} transform="rotate(-20 95 38)"/>
<ellipse cx="102" cy="40" rx="3.2" ry="5.5" fill="#FFC928" {W(1.6)} transform="rotate(50 102 40)"/>
<ellipse cx="91" cy="46" rx="3.2" ry="5.5" fill="#FFC928" {W(1.6)} transform="rotate(-30 91 46)"/>
{sparkle(26, 40, 6, "#fff")}{sparkle(46, 26, 4, "#fff")}''')


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
