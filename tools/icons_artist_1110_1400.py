"""Робот «художник», 10.11 ~14:00 UTC.
check_unique.py нашёл 1 пару похожих картинок: atmosfera-rocknroll-pistsovaya ~ gymbalance-samory-mashela
(обе — фигурка в центре на бирюзовом фоне). Гимнастика остаётся, рок-н-ролл рисуется заново:
своя идея, свой герой, сцена, ракурс и тёплая «дайнерская» палитра.
Запуск из корня: python3 tools/icons_artist_1110_1400.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT

I = {}

# СК «Атмосфера», акробатический рок-н-ролл (Писцовая) — девочка с хвостиком делает высокий кик
# на чёрно-белом клетчатом полу, как в американском дайнере 50-х
_floor = "".join(
    f'<rect x="{x}" y="108" width="14" height="20" fill="{"#222" if (x // 14) % 2 else "#FFFFFF"}"/>'
    for x in range(0, 128, 14))
I["atmosfera-rocknroll-pistsovaya"] = (
    "девочка с высоким хвостом и красной косынкой-бантом, в юбке-солнце в белый горошек",
    "делает высокий рок-н-ролльный мах ногой вперёд на чёрно-белом клетчатом полу",
    ("#FFE6EE", "#F07C95"), f'''
{_floor}<path d="M0 108 H128" {W(3)}/>
<path d="M57 80 L55 104" {W(8)}/><path d="M57 80 L55 104" stroke="#FFD9BE" stroke-width="4.4" stroke-linecap="round"/>
<path d="M47 103 Q55 99 61 103 L61 108 H47Z" fill="#1E1E1E" {W(2.6)}/>
<path d="M66 78 L98 58" {W(8)}/><path d="M66 78 L98 58" stroke="#FFD9BE" stroke-width="4.4" stroke-linecap="round"/>
<path d="M96 53 Q105 50 108 56 L101 63 Q96 62 96 53Z" fill="#1E1E1E" {W(2.6)}/>
<path d="M53 63 H71 Q86 70 92 82 Q74 90 60 88 Q42 90 34 84 Q42 70 53 63Z" fill="#E3283E" {W(3)}/>
<circle cx="46" cy="80" r="2.4" fill="#fff"/><circle cx="58" cy="83" r="2.4" fill="#fff"/><circle cx="72" cy="81" r="2.4" fill="#fff"/>
<circle cx="83" cy="78" r="2.4" fill="#fff"/><circle cx="64" cy="72" r="2.4" fill="#fff"/><circle cx="52" cy="73" r="2.2" fill="#fff"/>
<path d="M56 64 L83 24" {W(7)}/><path d="M56 64 L83 24" stroke="#FFD9BE" stroke-width="3.6" stroke-linecap="round"/>
<path d="M58 54 L38 64" {W(7)}/><path d="M58 54 L38 64" stroke="#FFD9BE" stroke-width="3.6" stroke-linecap="round"/>
<path d="M53 44 Q62 41 70 44 L71 64 H53Z" fill="#FFFFFF" {W(3)}/>
<path d="M55 44 L62 52 L69 44" fill="none" {W(2)}/>
<path d="M54 26 Q40 18 30 30 Q38 26 42 32 Q34 36 36 44 Q44 34 54 32Z" fill="#5A3420" {W(2.6)}/>
<circle cx="62" cy="33" r="11" fill="#FFD9BE" {W(3)}/>
<path d="M51 31 Q52 19 63 20 Q73 21 73 30 Q66 25 58 27Z" fill="#5A3420" {W(2.4)}/>
<path d="M52 24 Q50 17 45 19 Q47 25 52 27 Q53 31 48 33 Q53 34 55 28Z" fill="#E3283E" {W(2)}/>
{eye(58, 34, .5)}{eye(67, 34, .5)}{blush(56, 39, .5)}{blush(70, 39, .5)}
<path d="M59 39 Q62.5 42.5 66 39" fill="#B8323E" {W(1.6)}/>
<path d="M92 32 V18 L102 15 V29" fill="none" {W(2.6)}/>
<ellipse cx="89" cy="32" rx="4" ry="3" fill="{O}"/><ellipse cx="99" cy="29" rx="4" ry="3" fill="{O}"/>
{sparkle(20, 92, 4)}{sparkle(110, 86, 5)}''')

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
