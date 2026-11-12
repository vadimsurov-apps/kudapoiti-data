"""Робот «художник», 12.11 ~05:00 UTC.
check_unique.py: 5 похожих пар; nastavnik-pervomayskaya (кувырок на зелёном татами) похожа на 4 иконки,
djigit-nikulinskaya ~ dmsh-lista-kosinskaya (у обеих — музыкальный треугольник), а csihg-balashikha-fadeeva
повторяла сцену mosgimnastika-vagonoremontnaya («колесо» по зелёному ковру). Перерисованы все три.
Запуск из корня: python3 tools/icons_artist_1112_0500.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT


def limb(d, color, w=7):
    """рука/рукав: тёмный контур + цвет"""
    return (f'<path d="{d}" fill="none" stroke="{O}" stroke-width="{w+3}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')


I = {}

# Академия единоборств «Наставник» (с 2 лет): наставник и малыш — большое синее кимоно обнимает рукавом крошечное белое
I["nastavnik-pervomayskaya"] = (
    "большое синее кимоно с чёрным поясом и крошечное белое кимоно с жёлтым поясом — наставник и малыш",
    "стоят рядом на красном татами, большое по-отечески положило рукав на плечо маленькому",
    ("#FFEFE2", "#EE8A5B"), f'''
<ellipse cx="64" cy="112" rx="52" ry="9" fill="#D8433B" {W(2.4)}/>
<path d="M88 76 L80 88 L84 94 L89 88 Z" fill="#FFFFFF" {W(2.6)}/>
<path d="M112 76 L120 88 L116 94 L111 88 Z" fill="#FFFFFF" {W(2.6)}/>
<path d="M88 74 H112 L113 112 H87 Z" fill="#FFFFFF" {W(3)}/>
<path d="M94 74 L100 84 L106 74" fill="none" {W(2.4)}/>
<path d="M100 104 V112" fill="none" {W(1.8)}/>
<rect x="86" y="97" width="28" height="6" rx="2" fill="#F6C83B" {W(2.2)}/>
<path d="M100 100 L95 109 M100 100 L105 109" fill="none" stroke="{O}" stroke-width="5.4" stroke-linecap="round"/>
<path d="M100 100 L95 109 M100 100 L105 109" fill="none" stroke="#F6C83B" stroke-width="3" stroke-linecap="round"/>
<circle cx="100" cy="100" r="3" fill="#F6C83B" {W(2)}/>
{eye(95, 89, .55)}{eye(105, 89, .55)}{smile(100, 93, 2.6, .6)}
<path d="M32 44 L12 58 L18 72 L32 64 Z" fill="#2F5FB3" {W(3)}/>
<path d="M30 42 H70 L72 110 H28 Z" fill="#2F5FB3" {W(3.2)}/>
<path d="M40 42 L50 60 L60 42" fill="none" stroke="{O}" stroke-width="8" stroke-linejoin="round"/>
<path d="M40 42 L50 60 L60 42" fill="none" stroke="#24488C" stroke-width="5" stroke-linejoin="round"/>
<path d="M50 96 V110" fill="none" {W(2)}/>
<rect x="27" y="84" width="46" height="8" rx="3" fill="#2B2B33" {W(2.4)}/>
<path d="M50 88 L44 102 M50 88 L56 102" fill="none" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M50 88 L44 102 M50 88 L56 102" fill="none" stroke="#2B2B33" stroke-width="4" stroke-linecap="round"/>
<circle cx="50" cy="88" r="4" fill="#2B2B33" {W(2)}/>
<path d="M68 44 L96 66 L91 76 L68 62 Z" fill="#2F5FB3" {W(3)}/>
{eye(43, 70, .8)}{eye(57, 70, .8)}{blush(37, 77, .7)}{blush(63, 77, .7)}{smile(50, 76, 4, .8)}
{sparkle(108, 30, 5)}{sparkle(84, 18, 3.5)}''')

# «Джигит.ру» — кавказские танцы: пара в танце — мальчик в синей черкеске и чёрной папахе, девочка в розовом платье с фатой
I["djigit-nikulinskaya"] = (
    "пара малышей в кавказских костюмах — мальчик в синей черкеске с газырями и чёрной папахе, девочка в розовом платье до пола с белой фатой",
    "танцуют вместе на деревянном полу: он на носочках вскинул руку вверх, она плывёт к нему, протянув руку-крыло",
    ("#FFF4D0", "#D98A2B"), f'''
<ellipse cx="64" cy="113" rx="50" ry="8" fill="#A8693A" {W(2.4)}/>
{limb("M38 60 Q28 50 24 34", "#2F5FB3")}
{limb("M52 62 Q60 62 68 60", "#2F5FB3")}
<path d="M40 98 L38 111 L42 111 L44 98 Z" fill="#2B2B33" {W(2.2)}/>
<path d="M48 98 L50 111 L54 111 L52 98 Z" fill="#2B2B33" {W(2.2)}/>
<path d="M37 56 H53 L60 100 H30 Z" fill="#2F5FB3" {W(3)}/>
<path d="M45 56 V100" fill="none" {W(1.8)}/>
<path d="M38 62 h4 M38 66 h4 M38 70 h4 M48 62 h4 M48 66 h4 M48 70 h4" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"/>
<rect x="33" y="76" width="24" height="4" rx="2" fill="#E3B23C" {W(1.8)}/>
<circle cx="45" cy="46" r="10" fill="#F6D2B0" {W(2.8)}/>
<path d="M33 40 Q32 24 45 24 Q58 24 57 40 Z" fill="#2B2B33" {W(2.6)}/>
<path d="M35 30 q3 -3 6 0 q3 -3 6 0 q3 -3 6 0" fill="none" stroke="#55555F" stroke-width="1.8" stroke-linecap="round"/>
{eye(41, 47, .55)}{eye(49, 47, .55)}{smile(45, 51, 2.6, .6)}
<path d="M80 50 Q72 70 72 104" fill="none" stroke="{O}" stroke-width="6" stroke-linecap="round"/>
<path d="M80 50 Q72 70 72 104" fill="none" stroke="#2B2B33" stroke-width="3.4" stroke-linecap="round"/>
<path d="M82 40 Q100 40 104 64 Q108 86 112 100 L96 92 Q94 70 90 52 Z" fill="#FFFFFF" {W(2.4)}/>
{limb("M80 64 Q74 60 70 58", "#F27BAA", 6)}
{limb("M92 64 Q102 58 108 48", "#F27BAA", 6)}
<path d="M80 60 H92 L104 110 H68 Z" fill="#F27BAA" {W(3)}/>
<path d="M78 82 Q86 86 94 82" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"/>
<circle cx="86" cy="50" r="9" fill="#F6D2B0" {W(2.6)}/>
<path d="M77 48 Q78 38 86 38 Q94 38 95 48 Q90 42 86 43 Q82 42 77 48 Z" fill="#2B2B33" {W(1.8)}/>
<rect x="80" y="33" width="12" height="7" rx="3" fill="#D8433B" {W(2.2)}/>
{eye(82.5, 51, .5)}{eye(89.5, 51, .5)}{smile(86, 55, 2.4, .55)}
{sparkle(104, 24, 4.5)}{sparkle(20, 76, 3.5)}''')

# Центр спортивной и художественной гимнастики (Балашиха): лисичка-гимнастка с лентой
I["csihg-balashikha-fadeeva"] = (
    "рыжая лисичка-гимнастка в изумрудном купальнике с пушистым хвостом",
    "стоит на носочке одной лапки, другую отвела назад, и крутит над головой спираль малиновой ленты в голубом небе",
    ("#EAF6FF", "#4C8FD6"), f'''
<path d="M54 84 Q22 92 20 66 Q30 76 44 72 Q40 66 52 70 Z" fill="#F08A2E" {W(2.8)}/>
<path d="M20 66 Q22 76 30 80 Q24 72 26 66 Z" fill="#FFFFFF" {W(2)}/>
{limb("M62 86 L63 112", "#F08A2E", 6)}
{limb("M70 82 Q84 88 96 80", "#F08A2E", 6)}
{limb("M56 64 Q46 70 40 62", "#F08A2E", 5)}
{limb("M70 62 Q78 50 80 38", "#F08A2E", 5)}
<path d="M56 58 H72 L74 88 H58 Z" fill="#1FA67A" {W(3)}/>
<path d="M60 58 L66 70 L70 58" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
<path d="M50 34 L48 18 L58 28 Z" fill="#F08A2E" {W(2.6)}/>
<path d="M76 34 L80 18 L68 28 Z" fill="#F08A2E" {W(2.6)}/>
<path d="M48 36 Q48 24 63 24 Q78 24 78 36 Q78 50 63 58 Q48 50 48 36 Z" fill="#F08A2E" {W(2.8)}/>
<path d="M52 42 Q58 52 63 57 Q68 52 74 42 Q68 46 63 46 Q58 46 52 42 Z" fill="#FFFFFF"/>
<circle cx="63" cy="54" r="2.6" fill="{O}"/>
{eye(57, 38, .7)}{eye(69, 38, .7)}{blush(53, 45, .55)}{blush(73, 45, .55)}
<path d="M80 38 L86 20" fill="none" stroke="{O}" stroke-width="3" stroke-linecap="round"/>
<path d="M86 20 Q112 10 110 30 Q108 46 92 40 Q80 34 96 26 Q106 22 104 32" fill="none" stroke="{O}" stroke-width="7.5" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M86 20 Q112 10 110 30 Q108 46 92 40 Q80 34 96 26 Q106 22 104 32" fill="none" stroke="#E0337A" stroke-width="4.6" stroke-linecap="round" stroke-linejoin="round"/>
<ellipse cx="63" cy="113" rx="12" ry="3.5" fill="#2F6FB8" opacity=".5"/>
{sparkle(30, 30, 4.5)}{sparkle(108, 92, 4)}{sparkle(22, 100, 3)}''')

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
