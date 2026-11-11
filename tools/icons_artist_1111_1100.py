"""Робот «художник», 11.11 ~11:00 UTC.
check_unique.py: 1 пара похожих картинок — allonzhe-shcherbinka ~ flamingo-club-savvinsky (одна фигура по центру
на розовом фоне). Фламинго оставлен, «Аллонже» перерисован: рыжая белочка с лентой на мятном фоне.
Запуск из корня: python3 tools/icons_artist_1111_1100.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT

I = {}

# Клуб художественной гимнастики «Аллонже» (Щербинка) — белочка на носочках крутит ленту спиралью
I["allonzhe-shcherbinka"] = (
    "рыжая белочка-гимнастка с пушистым хвостом в фиолетовом купальнике",
    "привстала на носочки на синем ковре и крутит над головой малиновую гимнастическую ленту большой спиралью",
    ("#ECFFF6", "#45B88F"), f'''
<path d="M0 106 H128 V128 H0Z" fill="#2B5DA8"/>
<path d="M0 106 H128" {W(2.6)}/>
<ellipse cx="62" cy="107" rx="16" ry="2.6" fill="#173E78" opacity=".6"/>
<path d="M52 92 Q22 94 20 64 Q18 38 40 38 Q50 40 46 50 Q36 52 38 64 Q42 78 56 82Z" fill="#E07A22" {W(3)}/>
<path d="M44 84 Q28 82 27 64 Q27 50 36 46" fill="none" stroke="#F7B467" stroke-width="5" stroke-linecap="round"/>
<path d="M58 90 L57 103 M68 90 L69 103" {W(8)}/>
<path d="M58 90 L57 103 M68 90 L69 103" stroke="#E07A22" stroke-width="4.6" stroke-linecap="round"/>
<ellipse cx="56" cy="104.5" rx="4" ry="2.4" fill="#E07A22" {W(2.2)}/>
<ellipse cx="70" cy="104.5" rx="4" ry="2.4" fill="#E07A22" {W(2.2)}/>
<ellipse cx="63" cy="77" rx="12.5" ry="16" fill="#7B4FD8" {W(3)}/>
<path d="M56 66 Q63 72 70 66" fill="none" stroke="#B79BFF" stroke-width="2" stroke-linecap="round"/>
{sparkle(60, 80, 2.2)}{sparkle(67, 86, 1.6)}
<path d="M53 72 Q44 76 38 74" fill="none" {W(8)}/><path d="M53 72 Q44 76 38 74" fill="none" stroke="#E07A22" stroke-width="4.6" stroke-linecap="round"/>
<path d="M73 70 Q82 58 88 44" fill="none" {W(8)}/><path d="M73 70 Q82 58 88 44" fill="none" stroke="#E07A22" stroke-width="4.6" stroke-linecap="round"/>
<path d="M88 44 L99 22" {W(5.5)}/><path d="M88 44 L99 22" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>
<circle cx="88" cy="44" r="3.6" fill="#E07A22" {W(2.2)}/>
<path d="M99 22 Q122 26 116 48 Q108 70 92 62 Q80 52 96 46 Q118 42 118 70 Q118 92 96 98" fill="none" {W(8.5)}/>
<path d="M99 22 Q122 26 116 48 Q108 70 92 62 Q80 52 96 46 Q118 42 118 70 Q118 92 96 98" fill="none" stroke="#F0307A" stroke-width="5" stroke-linecap="round"/>
<path d="M53 37 L51 22 L61 33Z" fill="#E07A22" {W(2.6)}/>
<path d="M73 37 L76 22 L66 33Z" fill="#E07A22" {W(2.6)}/>
<path d="M51 22 L49 17 M76 22 L78 17" {W(2.6)}/>
<circle cx="63" cy="47" r="14" fill="#E07A22" {W(3)}/>
<ellipse cx="63" cy="53" rx="8" ry="6" fill="#FBD9AE"/>
{eye(57.5, 46, .62)}{eye(68.5, 46, .62)}
{blush(53, 53, .6)}{blush(73, 53, .6)}
<ellipse cx="63" cy="51" rx="2" ry="1.4" fill="{O}"/>
{smile(63, 54, 3, .8)}
{sparkle(24, 24, 4)}{sparkle(108, 112, 3)}''')

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
