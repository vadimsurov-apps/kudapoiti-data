"""Робот «художник», 10.11 ~11:00 UTC.
check_unique.py нашёл 6 пар похожих картинок (по цвету и компоновке). Из каждой пары одна остаётся,
другая рисуется заново — своя идея, свой герой, сцена, ракурс и палитра. Каждое тело SVG написано отдельно.
Перерисованы: vittoria-gym-zhebrunova, fd-strogino-katukova, artistic-swim-davydkovskaya (была в двух парах),
tanc-masterskaya-masterkova, top-dance-kondratyevsky.
Запуск из корня: python3 tools/icons_artist_1110_1100.py"""
import os, re, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT

I = {}

# Художественная гимнастика «Vittoria», Сокольники — получешки на носочках, над ними вьётся алая лента
I["vittoria-gym-zhebrunova"] = (
    "пара бежевых получешек художественной гимнастики с мордашками",
    "стоят на самых носочках, а над ними вьётся спиралью алая лента на палочке",
    ("#FFF4CF", "#EFA43A"), f'''
<path d="M0 113 H128 V128 H0Z" fill="#3E7BD6" {W(3)}/>
<path d="M98 16 L82 40" {W(6)}/><path d="M98 16 L82 40" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>
<path d="M82 40 C70 20 52 44 44 28 C38 16 22 22 26 36 C30 50 48 48 52 40" fill="none" {W(8.5)}/>
<path d="M82 40 C70 20 52 44 44 28 C38 16 22 22 26 36 C30 50 48 48 52 40" fill="none" stroke="#E8324A" stroke-width="5" stroke-linecap="round"/>
<path d="M30 56 Q40 52 50 56 L52 70 Q55 88 58 100 L68 106 Q73 112 64 113 L52 112 Q46 110 46 104 Q40 88 32 78 Q26 66 30 56Z" fill="#F7D9B5" {W(3)}/>
<path d="M30 56 Q40 52 50 56 Q40 60 30 56Z" fill="#D9A877" {W(2.4)}/>
<path d="M30 58 Q24 68 33 76" fill="none" stroke="#E8A05A" stroke-width="4" stroke-linecap="round"/>
<path d="M58 102 Q56 108 60 112" fill="none" {W(2)}/>
{eye(46, 80, .6)}{eye(55, 78, .6)}{blush(44, 88, .5)}<path d="M48 88 Q51.5 91 55 87" fill="none" {W(1.8)}/>
<path d="M74 56 Q84 52 94 56 L96 70 Q99 88 102 100 L112 106 Q117 112 108 113 L96 112 Q90 110 90 104 Q84 88 76 78 Q70 66 74 56Z" fill="#F7D9B5" {W(3)}/>
<path d="M74 56 Q84 52 94 56 Q84 60 74 56Z" fill="#D9A877" {W(2.4)}/>
<path d="M74 58 Q68 68 77 76" fill="none" stroke="#E8A05A" stroke-width="4" stroke-linecap="round"/>
<path d="M102 102 Q100 108 104 112" fill="none" {W(2)}/>
{eye(90, 80, .6)}{eye(99, 78, .6)}{blush(88, 88, .5)}<path d="M92 88 Q95.5 91 99 87" fill="none" {W(1.8)}/>
{sparkle(112, 44, 5)}{sparkle(16, 86, 4)}''')

# FD, Строгино (гимнастика и акробатика) — немецкое колесо катится, внутри малыш-акробат звёздочкой
I["fd-strogino-katukova"] = (
    "немецкое гимнастическое колесо — два больших серебристых обода с красными перекладинами",
    "катится по залу, а внутри растопырился звёздочкой малыш-акробат в синей майке",
    ("#FFE3D8", "#E2604A"), f'''
<path d="M6 116 H122" {W(3)}/>
<path d="M10 106 H22 M8 98 H18 M12 90 H20" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".85"/>
<ellipse cx="74" cy="62" rx="30" ry="48" fill="none" {W(9)}/>
<ellipse cx="74" cy="62" rx="30" ry="48" fill="none" stroke="#B9C6D8" stroke-width="5"/>
<path d="M52 18 L70 14 M52 110 L70 110 M23 64 L44 62 M84 64 L102 62" {W(7)}/>
<path d="M52 18 L70 14 M52 110 L70 110 M23 64 L44 62 M84 64 L102 62" stroke="#E8344E" stroke-width="3.6" stroke-linecap="round"/>
<path d="M60 70 L46 106 M68 70 L80 106" {W(7.5)}/><path d="M60 70 L46 106 M68 70 L80 106" stroke="#FFD9B8" stroke-width="4" stroke-linecap="round"/>
<path d="M56 50 L40 24 M72 50 L86 22" {W(7)}/><path d="M56 50 L40 24 M72 50 L86 22" stroke="#FFD9B8" stroke-width="3.6" stroke-linecap="round"/>
<path d="M54 46 Q64 42 74 46 L72 72 H56Z" fill="#2F6FD8" {W(3)}/>
<circle cx="64" cy="35" r="10" fill="#FFD9B8" {W(3)}/>
<path d="M54 33 Q56 22 66 24 Q74 25 74 33 Q68 28 60 30Z" fill="#7A4A2A" {W(2)}/>
{eye(60, 36, .45)}{eye(68, 36, .45)}<path d="M61 40 Q64 42.5 67 40" fill="none" {W(1.6)}/>
<ellipse cx="54" cy="64" rx="30" ry="48" fill="none" {W(9)}/>
<ellipse cx="54" cy="64" rx="30" ry="48" fill="none" stroke="#DCE6F2" stroke-width="5"/>
<path d="M30 40 Q34 30 40 26" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
{sparkle(112, 30, 6)}''')

# Artistic, Давыдковская (плавание и синхронное плавание) — вид сверху: синхронистки кругом-цветком
def _swimmer(a):
    """одна синхронистка в фигуре «цветок» (вид сверху), угол a — направление головы от центра"""
    c, s_ = math.cos(math.radians(a)), math.sin(math.radians(a))
    def p(r, t=0):
        x, y = 64 + r * c - t * s_, 64 + r * s_ + t * c
        return f"{x:.1f} {y:.1f}"
    hx, hy = 64 + 45 * c, 64 + 45 * s_
    return (f'<path d="M{p(14,-2)} L{p(30,-4)} M{p(14,2)} L{p(30,4)}" {W(7)}/>'
            f'<path d="M{p(14,-2)} L{p(30,-4)} M{p(14,2)} L{p(30,4)}" stroke="#FFD3B0" stroke-width="3.8" stroke-linecap="round"/>'
            f'<path d="M{p(36,-7)} L{p(40,-17)} M{p(36,7)} L{p(40,17)}" {W(6.5)}/>'
            f'<path d="M{p(36,-7)} L{p(40,-17)} M{p(36,7)} L{p(40,17)}" stroke="#FFD3B0" stroke-width="3.2" stroke-linecap="round"/>'
            f'<path d="M{p(28,-6)} L{p(38,-8)} L{p(38,8)} L{p(28,6)}Z" fill="#E33A8B" {W(2.6)}/>'
            f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="8" fill="#E8344E" {W(2.6)}/>'
            f'<circle cx="{64 + 47 * c - 3 * s_:.1f}" cy="{64 + 47 * s_ + 3 * c:.1f}" r="2.2" fill="#fff" opacity=".8"/>')


I["artistic-swim-davydkovskaya"] = (
    "шесть синхронисток в красных шапочках и малиновых купальниках, вид сверху",
    "лежат на воде кругом, ногами к центру, раскинув руки, — вместе складываются в цветок вокруг брызг",
    ("#C4E6FF", "#1B54B0"), f'''
<path d="M2 30 Q12 26 22 30 T42 30 M86 104 Q96 100 106 104 T126 104 M2 100 Q10 96 18 100 M104 22 Q114 18 124 22" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" opacity=".55"/>
{_swimmer(-90)}{_swimmer(-30)}{_swimmer(30)}{_swimmer(90)}{_swimmer(150)}{_swimmer(210)}
<path d="M64 50 L67 58 L76 56 L70 63 L77 70 L68 69 L64 78 L60 69 L51 70 L58 63 L52 56 L61 58Z" fill="#fff" {W(2.4)}/>
{sparkle(14, 18, 5)}''')

# Танцевальная мастерская, ул. Мастеркова — портновский манекен в мастерской примеряет розовую пачку
I["tanc-masterskaya-masterkova"] = (
    "портновский манекен с мордашкой и жёлтым сантиметром на шее",
    "в швейной мастерской примеряет новую пышную розовую балетную пачку",
    ("#EEF7DF", "#86AE62"), f'''
<path d="M64 92 V112 M64 108 L46 122 M64 108 L82 122 M64 108 V122" {W(4.5)}/>
<path d="M64 92 V112 M64 108 L46 122 M64 108 L82 122" stroke="#A9764A" stroke-width="2" stroke-linecap="round"/>
<rect x="58" y="12" width="12" height="10" rx="4" fill="#A9764A" {W(2.6)}/>
<path d="M44 30 Q64 18 84 30 Q92 46 82 60 Q80 68 82 76 H46 Q48 68 46 60 Q36 46 44 30Z" fill="#B8324A" {W(3)}/>
<path d="M64 24 V76" stroke="#8E2236" stroke-width="2"/>
<path d="M30 80 L36 72 L42 80 L48 71 L54 80 L60 70 L66 80 L72 70 L78 80 L84 71 L90 80 L96 72 L100 82 Q64 98 28 82Z" fill="#FF9EC7" {W(3)}/>
<path d="M22 86 L30 78 L38 88 L46 78 L54 90 L64 78 L74 90 L82 78 L90 88 L98 78 L106 86 Q64 104 22 86Z" fill="#FFC2DC" {W(3)}/>
<path d="M46 76 H82 L80 82 H48Z" fill="#F470A8" {W(2.6)}/>
<path d="M50 28 Q46 44 48 60" fill="none" stroke="#FFC93C" stroke-width="5.5" stroke-linecap="round"/>
<path d="M78 28 Q84 44 82 58" fill="none" stroke="#FFC93C" stroke-width="5.5" stroke-linecap="round"/>
<path d="M50 28 Q64 22 78 28" fill="none" stroke="#FFC93C" stroke-width="5.5" stroke-linecap="round"/>
<path d="M48 36 h3 M48 44 h3 M48 52 h3 M80 36 h3 M81 44 h3 M81 52 h3" {W(1.4)}/>
<circle cx="58" cy="44" r="5.5" fill="#fff"/><circle cx="70" cy="44" r="5.5" fill="#fff"/>{eye(58, 44, .6)}{eye(70, 44, .6)}<ellipse cx="53" cy="52" rx="3.5" ry="2" fill="#FF9EC0"/><ellipse cx="75" cy="52" rx="3.5" ry="2" fill="#FF9EC0"/>{eye(58, 44, .5)}{eye(70, 44, .5)}<path d="M60 52 Q64 56 68 52" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
{sparkle(108, 30, 6)}{sparkle(20, 40, 4)}''')

# «Топ Дэнс», Большой Кондратьевский — джазовки отбивают ритм в луче прожектора на тёмной сцене
I["top-dance-kondratyevsky"] = (
    "пара ярко-малиновых джазовок на шнуровке с мордашками",
    "отбивают ритм в столбе света на тёмной сцене: одна стоит, другая подбросила носок вверх",
    ("#6A4A8E", "#20143A"), f'''
<path d="M54 0 H74 L114 112 H14Z" fill="#FFF1A8" opacity=".32"/>
<ellipse cx="64" cy="108" rx="48" ry="9" fill="#FFF1A8" opacity=".5"/>
<path d="M14 104 Q16 86 32 84 L48 82 Q58 80 62 90 Q64 98 58 104Z" fill="#E8287A" {W(3)}/>
<path d="M14 104 H58" {W(5)}/>
<path d="M36 84 L40 92 M42 83 L46 91 M48 82 L51 89" {W(1.8)}/>
<path d="M32 84 Q42 76 52 82" fill="none" stroke="#FFFFFF" stroke-width="2" opacity=".7"/>
{eye(24, 94, .5)}{eye(32, 94, .5)}{blush(20, 99, .5)}<path d="M25 99 Q28 101.5 31 99" fill="none" {W(1.5)}/>
<g transform="rotate(-28 92 78)">
 <path d="M68 90 Q70 72 86 70 L102 68 Q112 66 116 76 Q118 84 112 90Z" fill="#FF4B95" {W(3)}/>
 <path d="M68 90 H112" {W(5)}/>
 <path d="M90 70 L94 78 M96 69 L100 77 M102 68 L105 75" {W(1.8)}/>
 {eye(78, 80, .5)}{eye(86, 80, .5)}{blush(74, 85, .5)}<path d="M79 85 Q82 87.5 85 85" fill="none" {W(1.5)}/>
</g>
<path d="M106 44 Q112 50 106 56 M112 40 Q120 50 112 60" fill="none" stroke="#FFF1A8" stroke-width="2.6" stroke-linecap="round"/>
{sparkle(30, 30, 5, "#FFF1A8")}{sparkle(96, 22, 4, "#FFF1A8")}''')


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
