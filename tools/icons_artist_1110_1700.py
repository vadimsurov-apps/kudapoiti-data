"""Робот «художник», 10.11 ~17:00 UTC.
check_unique.py: 2 пары похожих картинок (фигурка в центре на сиреневом фоне):
graciya-m-vernadskogo ~ megaball-volgogradsky-157, stremlenie-dance-katukova ~ vodnaya-stikhiya-polyany.
Гимнастка и синхронистка остаются, футбол и танцы рисуются заново — свой герой, сцена, ракурс и палитра.
Запуск из корня: python3 tools/icons_artist_1110_1700.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT

I = {}

# Футбольная школа «Мегаболл» (Волгоградский) — ёжик-футболист ведёт носом большой мяч по полю
_spikes = "M18 92 L14 84 L20 82 L16 72 L24 72 L22 62 L30 64 L31 54 L38 58 L42 49 L47 56 L53 50 L55 59 L62 56 L61 66 L67 66 L63 74 L66 80 Z"
I["megaball-volgogradsky-157"] = (
    "ёжик-футболист с колючками-шипами",
    "сосредоточенно ведёт носом по газону большой бело-чёрный мяч, а за ним вьётся пыльный след",
    ("#E9FFF0", "#3FB37A"), f'''
<path d="M0 100 Q64 92 128 100 V128 H0Z" fill="#2E8B4F"/>
<path d="M0 100 Q64 92 128 100" fill="none" stroke="#fff" stroke-width="2.4" opacity=".7"/>
<ellipse cx="44" cy="103" rx="26" ry="3.5" fill="#1F6B3B" opacity=".5"/>
<ellipse cx="90" cy="104" rx="22" ry="3.5" fill="#1F6B3B" opacity=".5"/>
<circle cx="10" cy="96" r="4" fill="#fff" opacity=".55"/><circle cx="4" cy="90" r="2.6" fill="#fff" opacity=".45"/>
<path d="{_spikes}" fill="#7A4B2A" {W(3)}/>
<path d="M22 92 Q20 74 34 66 Q50 60 60 70 Q66 78 64 92 Z" fill="#7A4B2A"/>
<path d="M48 70 Q60 62 70 76 Q74 82 70 88 Q62 94 52 92 Q44 84 48 70Z" fill="#F2D2A9" {W(3)}/>
<circle cx="72" cy="84" r="3.4" fill="{O}"/>
{eye(58, 75, .62)}{blush(56, 84, .55)}
<path d="M60 88 Q63 90 66 88" fill="none" {W(1.8)}/>
<path d="M28 92 V100 M40 93 V101 M50 93 V100" {W(5)}/>
<path d="M28 92 V100 M40 93 V101 M50 93 V100" stroke="#F2D2A9" stroke-width="2.4" stroke-linecap="round"/>
<circle cx="96" cy="80" r="22" fill="#FFFFFF" {W(3.2)}/>
<path d="M96 72 L104 78 L101 87 L91 87 L88 78Z" fill="{O}"/>
<path d="M96 58 L96 66 L96 72 M104 78 L113 74 M101 87 L107 96 M91 87 L85 96 M88 78 L79 74" fill="none" {W(2)}/>
<path d="M90 58.8 L96 63 L102 58.8 L99 58.2 L93 58.2Z" fill="{O}"/>
<path d="M115 70 L117 79 L117.8 76 L116 69Z" fill="{O}"/>
<path d="M78 86 L80 93 L77 90Z" fill="{O}"/>
<path d="M102 101 L106 94 L111 97 L108 100Z" fill="{O}"/>
{sparkle(108, 30, 5)}{sparkle(22, 30, 3.5)}''')

# Танцевальная студия «Стремление» (Строгино) — бегемотик-балерина делает плие у станка
I["stremlenie-dance-katukova"] = (
    "серый бегемотик-балерина в розовой пачке",
    "держится за деревянный балетный станок и старательно делает плие, а станок под ним чуть прогнулся",
    ("#FFF1DE", "#F2A65E"), f'''
<path d="M0 106 H128 V128 H0Z" fill="#C98A4E"/>
<path d="M0 106 H128" {W(2.6)}/>
<path d="M8 62 Q64 70 120 62" fill="none" {W(9)}/><path d="M8 62 Q64 70 120 62" fill="none" stroke="#B5763B" stroke-width="5.6" stroke-linecap="round"/>
<path d="M14 64 V106 M114 64 V106" {W(5)}/><path d="M14 64 V106 M114 64 V106" stroke="#B5763B" stroke-width="2.4"/>
<path d="M50 96 Q44 100 42 106 L52 106 Q54 100 56 96Z" fill="#9AA3B5" {W(2.6)}/>
<path d="M78 96 Q84 100 86 106 L76 106 Q74 100 72 96Z" fill="#9AA3B5" {W(2.6)}/>
<ellipse cx="45" cy="106" rx="6" ry="2.6" fill="#FF8FB5" {W(2)}/>
<ellipse cx="83" cy="106" rx="6" ry="2.6" fill="#FF8FB5" {W(2)}/>
<ellipse cx="64" cy="80" rx="22" ry="20" fill="#9AA3B5" {W(3.2)}/>
<path d="M30 88 Q38 76 48 80 Q56 74 64 78 Q72 74 80 80 Q90 76 98 88 Q88 94 80 90 Q72 96 64 92 Q56 96 48 90 Q40 94 30 88Z" fill="#FFB6CF" {W(2.8)}/>
<path d="M46 72 Q36 66 34 62" fill="none" {W(6.5)}/><path d="M46 72 Q36 66 34 62" fill="none" stroke="#9AA3B5" stroke-width="3.4" stroke-linecap="round"/>
<path d="M82 70 Q94 58 100 44" fill="none" {W(6.5)}/><path d="M82 70 Q94 58 100 44" fill="none" stroke="#9AA3B5" stroke-width="3.4" stroke-linecap="round"/>
<ellipse cx="64" cy="44" rx="18" ry="16" fill="#9AA3B5" {W(3.2)}/>
<ellipse cx="64" cy="54" rx="14" ry="9" fill="#B8C0CF" {W(2.6)}/>
<circle cx="60" cy="53" r="1.4" fill="{O}"/><circle cx="68" cy="53" r="1.4" fill="{O}"/>
<path d="M59 58.5 Q64 61 69 58.5" fill="none" {W(1.8)}/>
<circle cx="50" cy="30" r="4.4" fill="#9AA3B5" {W(2.6)}/><circle cx="78" cy="30" r="4.4" fill="#9AA3B5" {W(2.6)}/>
<circle cx="50" cy="30" r="1.8" fill="#FF9DB8"/><circle cx="78" cy="30" r="1.8" fill="#FF9DB8"/>
{eye(57, 42, .55)}{eye(71, 42, .55)}{blush(52, 48, .55)}{blush(76, 48, .55)}
<path d="M58 26 Q64 20 70 26 Q64 29 58 26Z" fill="#FF6E9C" {W(2)}/>
{sparkle(108, 26, 5)}{sparkle(22, 40, 3.5)}''')

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
