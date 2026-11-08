"""Иконки робота fun (2026-11-08, день): 13 мест Подмосковья. Каждая придумана и нарисована отдельно (правило
абсолютной уникальности). Сверено со всеми листами icons-catalog и icons-src/subjects.txt (заняты: ретро-автобус
сбоку, ракеты/шлемы/скафандры, номерки, маски, челнок, дуга с колокольчиком, верстовой столб, карета-тыква,
свистулька, парта, камертон, пюпитр, кинокамера с бобинами, вечный огонь — не брать).
Запуск: python3 tools/icons_fun_1108c.py [id ...]  (печатает строки для subjects.txt)"""
import os, sys
from draw_icons import s, eye, face, sparkle, O

W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=9, k=0.75, **kw: face(cx, cy, d=d, k=k, **kw)
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")


def svg(a, b, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
<defs>
 <radialGradient id="g" cx="38%" cy="28%" r="85%"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></radialGradient>
 <clipPath id="c"><circle cx="64" cy="64" r="61"/></clipPath>
</defs>
<circle cx="64" cy="64" r="61" fill="url(#g)"/>
<g clip-path="url(#c)">{body}</g>
<ellipse cx="44" cy="22" rx="20" ry="7" fill="#fff" opacity=".3"/>
</svg>'''


I = {}

# Музей Мострансавто — пузатый ЗИЛ-158 анфас едет на зрителя между берёзками
I["mostransavto-museum-chekhov"] = ("#E6FFF0", "#7FD6A8",
    "пузатый кремово-красный автобус ЗИЛ-158 анфас, круглые фары — глаза",
    "катит прямо на зрителя по просёлочной дороге между двумя берёзками",
    f'<path d="M0 96 Q64 86 128 96 V128 H0Z" fill="#8BCB6A" {W(2.4)}/>'
    + f'<path d="M50 128 L58 96 H70 L78 128Z" fill="#D9B98A" {W(2.2)}/>'
    + "".join(f'<path d="M{x} 96 V30" stroke="#fff" stroke-width="6"/><path d="M{x-3} 96 V30 M{x+3} 96 V30" {W(1.6)}/>'
              f'<path d="M{x-3} {y} h3 M{x} {y+12} h3" {W(1.6)}/>'
              f'<ellipse cx="{x}" cy="30" rx="13" ry="11" fill="#9BD15C" {W(2.2)}/>' for x, y in [(14, 60), (114, 52)])
    + f'<path d="M30 98 V54 Q30 30 64 30 Q98 30 98 54 V98Z" fill="#F7EAC8" {W(3.2)}/>'
    + f'<path d="M30 76 H98 V98 H30Z" fill="#E2453C" {W(3)}/>'
    + f'<path d="M38 40 Q64 32 90 40 V62 H38Z" fill="#BFE3FF" {W(2.6)}/>'
    + f'<path d="M64 36 V62" {W(2.2)}/>'
    + f'<rect x="50" y="80" width="28" height="12" rx="3" fill="#FFE59A" {W(2.2)}/>'
    + "".join(f'<path d="M54 {y} H74" {W(1.4)}/>' for y in (84, 88))
    + f'<circle cx="40" cy="86" r="7" fill="#FFF7D6" {W(2.4)}/><circle cx="88" cy="86" r="7" fill="#FFF7D6" {W(2.4)}/>'
    + eye(40, 86, 0.7) + eye(88, 86, 0.7)
    + f'<path d="M58 70 Q64 74 70 70" fill="none" {W(2.4)}/>'
    + f'<rect x="28" y="98" width="72" height="8" rx="3" fill="#B8B8C8" {W(2.4)}/>'
    + f'<rect x="32" y="106" width="12" height="10" rx="3" fill="{O}"/><rect x="84" y="106" width="12" height="10" rx="3" fill="{O}"/>'
    + sparkle(60, 20, 4, "#fff"))

# Музей Быковского — космический тюбик «Борщ» в невесомости у иллюминатора
I["bykovsky-museum-pavposad"] = ("#5A7BD6", "#1E2766",
    "космический тюбик-обед с надписью «БОРЩ» и колпачком",
    "парит в невесомости у круглого иллюминатора, за которым голубая Земля",
    f'<circle cx="88" cy="46" r="30" fill="#C9CCDA" {W(3)}/>'
    + f'<circle cx="88" cy="46" r="22" fill="#0E1238" {W(2.6)}/>'
    + f'<circle cx="96" cy="56" r="13" fill="#4FA3F0"/><path d="M88 52 Q92 46 98 50 Q100 56 94 58Z M100 62 Q106 60 106 66 Q102 68 100 62Z" fill="#6CCB6A"/>'
    + "".join(f'<circle cx="{88+26*c}" cy="{46+26*s_}" r="2.4" fill="{O}"/>' for c, s_ in [(1, 0), (-1, 0), (0, 1), (0, -1)])
    + sparkle(80, 36, 2.6, "#fff") + sparkle(98, 34, 1.8, "#fff")
    + '<g transform="rotate(-28 50 78)">'
    + f'<path d="M30 60 H70 L74 96 Q50 104 26 96Z" fill="#F2F4F8" {W(3.2)}/>'
    + f'<path d="M30 60 H70 V66 H30Z" fill="#B8BCC9" {W(2.4)}/>'
    + f'<path d="M26 96 Q50 104 74 96 L70 104 Q50 110 30 104Z" fill="#D7DAE4" {W(2.4)}/>'
    + f'<rect x="44" y="104" width="12" height="12" rx="3" fill="#E2453C" {W(2.4)}/>'
    + f'<rect x="33" y="84" width="34" height="9" rx="2" fill="#E2453C" {W(2)}/>'
    + '<text x="50" y="91.5" font-family="Arial" font-weight="700" font-size="7.5" fill="#fff" text-anchor="middle">БОРЩ</text>'
    + f(50, 74, d=8, k=0.65) + '</g>'
    + f'<path d="M18 46 q4 -4 8 0 M14 98 q4 -4 8 0" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" opacity=".7"/>'
    + sparkle(24, 28, 3, "#FFE79A") + sparkle(112, 100, 3, "#FFE79A") + sparkle(60, 22, 2, "#fff"))

# Зимний театр — бархатный занавес в снегу, сквозь щель золотой свет
I["zimniy-teatr-oz"] = ("#E8F4FF", "#8FB8E8",
    "бордовый бархатный занавес с золотыми кистями",
    "на его ламбрекене лежит пушистый снег, сверху падают снежинки, в щели посередине горит тёплый золотой свет",
    f'<path d="M58 34 H70 V112 H58Z" fill="#FFD66B"/>'
    + f'<path d="M60 40 L52 120 H76 L68 40Z" fill="#FFF0B0" opacity=".7"/>'
    + f'<path d="M14 34 H62 Q58 70 64 112 H22 Q30 72 14 34Z" fill="#A3203F" {W(3)}/>'
    + f'<path d="M114 34 H66 Q70 70 64 112 H106 Q98 72 114 34Z" fill="#A3203F" {W(3)}/>'
    + f'<path d="M28 44 Q34 76 30 108 M44 42 Q48 76 46 110 M100 44 Q94 76 98 108 M84 42 Q80 76 82 110" fill="none" stroke="#7A1530" stroke-width="2.4"/>'
    + f'<path d="M10 22 H118 V40 Q104 48 92 40 Q78 48 64 40 Q50 48 36 40 Q24 48 10 40Z" fill="#C2304F" {W(3)}/>'
    + f'<path d="M8 24 Q20 14 34 20 Q46 12 60 18 Q74 10 88 18 Q102 12 120 22 L118 26 H10Z" fill="#fff" {W(2.6)}/>'
    + f'<circle cx="56" cy="76" r="6" fill="#FFC53D" {W(2.4)}/><path d="M53 82 L50 94 H62 L59 82Z" fill="#FFC53D" {W(2.2)}/>'
    + f'<circle cx="72" cy="76" r="6" fill="#FFC53D" {W(2.4)}/><path d="M69 82 L66 94 H78 L75 82Z" fill="#FFC53D" {W(2.2)}/>'
    + f(64, 56, d=12, k=0.7)
    + f'<path d="M0 112 H128 V128 H0Z" fill="#8A5A3C" {W(2.6)}/>'
    + "".join(sparkle(x, y, r, "#fff") for x, y, r in [(22, 10, 3), (100, 8, 3.4), (60, 6, 2.4), (116, 60, 2.6), (8, 70, 2.6)]))

# Дом Оглоблина — карманные часы-луковица на цепочке у полукруглого окна особняка
I["ogloblin-house-oz"] = ("#FFE9D6", "#E7A77B",
    "золотые карманные часы-луковица с откинутой крышкой",
    "висят на цепочке на гвоздике у полукруглого окна старинного купеческого особняка",
    f'<path d="M18 128 V54 Q18 18 54 18 Q90 18 90 54 V128Z" fill="#FFF6E6" {W(3)}/>'
    + f'<path d="M26 128 V56 Q26 26 54 26 Q82 26 82 56 V128Z" fill="#A9D8F5" {W(2.6)}/>'
    + f'<path d="M54 26 V128 M26 66 H82" {W(2.4)}/>'
    + f'<path d="M30 40 Q36 34 40 40" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'
    + f'<circle cx="98" cy="22" r="3" fill="{O}"/>'
    + f'<path d="M98 22 Q92 30 90 40" fill="none" stroke="#C99A2E" stroke-width="2.4" stroke-dasharray="3 2"/>'
    + f'<rect x="85" y="38" width="10" height="8" rx="2" fill="#FFCF4D" {W(2.2)}/>'
    + f'<path d="M66 70 Q62 50 76 52" fill="#FFE07A" {W(2.6)}/>'
    + f'<circle cx="90" cy="76" r="27" fill="#FFCF4D" {W(3.2)}/>'
    + f'<circle cx="90" cy="76" r="20" fill="#FFFBEF" {W(2.4)}/>'
    + "".join(f'<path d="M{90+17*c:.1f} {76+17*s_:.1f} L{90+20*c:.1f} {76+20*s_:.1f}" {W(1.8)}/>'
              for c, s_ in [(1, 0), (-1, 0), (0, 1), (0, -1)])
    + f(90, 80, d=7, k=0.6)
    + f'<path d="M90 76 V62 M90 76 L100 70" {W(2.2)}/>'
    + sparkle(112, 52, 3.4, "#fff") + sparkle(66, 104, 2.4, "#fff"))

# «Мир исторической реконструкции» — советский автомат газированной воды
I["ussr-reconstruction-dulevo"] = ("#FFF7C2", "#F5C84B",
    "красный советский автомат газированной воды с окошком-нишей и монетоприёмником",
    "стоит на тротуаре и наливает шипучую струю в гранёный стакан",
    f'<path d="M0 108 H128 V128 H0Z" fill="#C7C2B5" {W(2.4)}/>'
    + f'<path d="M0 108 L20 128 M40 108 L60 128 M80 108 L100 128 M120 108 L128 116" {W(1.6)}/>'
    + f'<rect x="34" y="14" width="60" height="96" rx="8" fill="#E2453C" {W(3.2)}/>'
    + f'<rect x="40" y="22" width="48" height="16" rx="3" fill="#FFF3D1" {W(2.4)}/>'
    + '<text x="64" y="34" font-family="Arial" font-weight="700" font-size="10" fill="#C2303A" text-anchor="middle">ВОДА</text>'
    + f(54, 48, d=7, k=0.6)
    + f'<rect x="76" y="44" width="10" height="14" rx="2" fill="#FFD23F" {W(2.2)}/>'
    + f'<path d="M79 48 H83" {W(2)}/>'
    + f'<rect x="42" y="62" width="44" height="38" rx="4" fill="#5A2230" {W(2.6)}/>'
    + f'<path d="M60 62 V68 H68 V62" fill="#B8BCC9" {W(2)}/>'
    + f'<path d="M64 68 V82" stroke="#BFE8FF" stroke-width="4"/>'
    + f'<path d="M55 82 L57 98 H71 L73 82Z" fill="#DFF4FF" {W(2.4)}/>'
    + f'<path d="M57 88 H71 M59 82 V98 M64 82 V98 M69 82 V98" {W(1.4)} opacity=".7"/>'
    + '<circle cx="61" cy="92" r="1.4" fill="#fff"/><circle cx="66" cy="88" r="1.2" fill="#fff"/><circle cx="64" cy="76" r="1.2" fill="#fff"/>'
    + sparkle(104, 30, 4, "#fff") + sparkle(20, 50, 3, "#fff") + sparkle(108, 80, 2.6, "#fff"))

# Ферма «Северный олень» — чум с дымком на снегу и нарты под розовым солнцем
I["severny-olen-farm"] = ("#FFE3F2", "#B9A2E8",
    "конусный чум из шкур с жердями, торчащими из макушки",
    "стоит на снегу под низким розовым морозным солнцем, из макушки вьётся дымок, рядом деревянные нарты",
    f'<circle cx="98" cy="42" r="14" fill="#FF9EB5"/>'
    + f'<path d="M0 98 Q40 88 70 94 Q100 100 128 92 V128 H0Z" fill="#fff" {W(2.6)}/>'
    + f'<path d="M64 24 L28 102 H100Z" fill="#B88A5E" {W(3.2)}/>'
    + f'<path d="M64 24 L46 64 Q64 70 82 64Z" fill="#9C6F45"/>'
    + f'<path d="M36 86 Q64 92 92 86" fill="none" {W(2)}/>'
    + f'<path d="M58 16 L66 32 M70 16 L62 32 M64 12 V30" {W(2.6)}/>'
    + f'<path d="M64 12 Q58 4 64 -2 Q70 -6 66 -12" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".85"/>'
    + f'<path d="M56 102 Q56 80 64 78 Q72 80 72 102Z" fill="#5A3B26" {W(2.6)}/>'
    + f(64, 60, d=8, k=0.65)
    + f'<path d="M96 108 H124 M98 100 H122 M100 100 V108 M120 100 V108 M124 108 Q128 104 126 98" fill="none" stroke="#9C6F45" stroke-width="3.4" stroke-linecap="round"/>'
    + f'<path d="M96 108 H124 M98 100 H122" fill="none" {W(1.4)}/>'
    + "".join(sparkle(x, y, r, "#fff") for x, y, r in [(20, 30, 3.4), (34, 54, 2.4), (110, 70, 2.6), (14, 70, 2.2)]))

# Кинотеатр «Волга-Волга» — колёсный пароход с киноэкраном вместо паруса
I["volga-volga-dubna"] = ("#FFE0B8", "#F28A4B",
    "белый колёсный пароход с красным гребным колесом сбоку",
    "плывёт по Волге на закате, вместо паруса на мачтах натянут киноэкран с мультяшной звездой",
    f'<path d="M0 88 Q32 82 64 88 Q96 94 128 88 V128 H0Z" fill="#4F8FE0" {W(2.6)}/>'
    + f'<path d="M10 104 q8 -4 16 0 M92 112 q8 -4 16 0 M50 118 q8 -4 16 0" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'
    + f'<path d="M40 24 V58 M96 24 V58" {W(3)}/>'
    + f'<rect x="36" y="20" width="64" height="38" rx="3" fill="#fff" {W(3)}/>'
    + f'<path d="M68 28 l3 7 8 1 -6 5 2 8 -7 -4 -7 4 2 -8 -6 -5 8 -1Z" fill="#FFD23F" {W(2)}/>'
    + f'<path d="M14 72 H112 L102 96 H24Z" fill="#fff" {W(3.2)}/>'
    + f'<rect x="30" y="58" width="58" height="14" rx="3" fill="#FFF3D1" {W(2.6)}/>'
    + "".join(f'<circle cx="{x}" cy="65" r="3" fill="#7FC8FF" {W(1.6)}/>' for x in (40, 52, 76))
    + f'<rect x="96" y="44" width="10" height="28" fill="#2F2A40" {W(2.4)}/><path d="M94 44 H108" {W(3)}/>'
    + f'<circle cx="34" cy="88" r="14" fill="#E2453C" {W(3)}/><circle cx="34" cy="88" r="5" fill="#fff" {W(2)}/>'
    + "".join(f'<path d="M34 88 L{34+13*c:.1f} {88+13*s_:.1f}" {W(1.8)}/>' for c, s_ in [(1, 0), (-1, 0), (0, 1), (0, -1), (.7, .7), (-.7, .7), (.7, -.7), (-.7, -.7)])
    + f(68, 84, d=8, k=0.6)
    + f'<path d="M0 98 Q32 92 64 98 Q96 104 128 98" fill="none" stroke="#4F8FE0" stroke-width="5" opacity=".8"/>'
    + sparkle(112, 22, 3.4, "#fff") + sparkle(18, 40, 2.6, "#fff"))

# Путевой дворец (Солнечногорск) — почтовый дилижанс с сундуками на крыше у озера Сенеж
I["putevoy-dvorets-solnechnogorsk"] = ("#E0F2FF", "#6FB6E8",
    "зелёный почтовый дилижанс с окошком, сундуками на крыше и большими деревянными колёсами",
    "остановился на тракте у берега озера Сенеж, рядом с каменной коновязью-тумбой",
    f'<path d="M0 76 Q64 70 128 76 V96 H0Z" fill="#3E8FD8" {W(2.4)}/>'
    + f'<path d="M14 84 q6 -3 12 0 M96 86 q6 -3 12 0" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>'
    + f'<path d="M0 94 Q64 88 128 94 V128 H0Z" fill="#D9C08E" {W(2.6)}/>'
    + f'<rect x="28" y="30" width="22" height="10" rx="2" fill="#B5733C" {W(2.4)}/><rect x="52" y="26" width="26" height="14" rx="2" fill="#7A4E2D" {W(2.4)}/>'
    + f'<path d="M22 40 H86 L90 50 V84 Q56 90 22 84 V50Z" fill="#3FA56B" {W(3.2)}/>'
    + f'<rect x="30" y="50" width="22" height="16" rx="3" fill="#BFE3FF" {W(2.4)}/>'
    + f'<rect x="60" y="50" width="22" height="30" rx="3" fill="#2F8656" {W(2.4)}/>'
    + f(41, 58, d=6, k=0.55)
    + f'<path d="M90 64 L110 60" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="94" r="{r}" fill="#F2C66D" {W(3)}/><circle cx="{x}" cy="94" r="3" fill="{O}"/>'
              + "".join(f'<path d="M{x} 94 L{x+r*c:.1f} {94+r*s_:.1f}" {W(1.8)}/>' for c, s_ in [(1, 0), (-1, 0), (0, 1), (0, -1)])
              for x, r in [(34, 13), (78, 13)])
    + f'<rect x="106" y="82" width="12" height="22" rx="4" fill="#C4BEB2" {W(2.6)}/><circle cx="112" cy="80" r="5" fill="none" {W(2.4)}/>'
    + sparkle(110, 26, 4, "#fff") + sparkle(18, 22, 2.6, "#fff"))

# Отдел художественных ремёсел (Хотьково) — майоликовый изразец с синим цветком на кирпичной стене
I["abramtsevo-crafts-khotkovo"] = ("#FFE8D8", "#D9875E",
    "квадратный майоликовый изразец с выпуклым синим цветком",
    "вмурован в кирпичную стену мастерской, рядом висит резец по дереву и вьётся стружка",
    "".join(f'<rect x="{x}" y="{y}" width="26" height="12" fill="#C8643F" {W(1.6)}/>'
            for y in range(0, 128, 12) for x in range(-13 * ((y // 12) % 2), 128, 26))
    + f'<rect x="28" y="28" width="62" height="62" rx="6" fill="#FFF3D6" {W(3.4)}/>'
    + f'<rect x="34" y="34" width="50" height="50" rx="4" fill="none" stroke="#2F6FD0" stroke-width="3"/>'
    + "".join(f'<path d="M{a} {b} q4 4 0 8 q-4 -4 0 -8Z" fill="#3CA36A"/>' for a, b in [(38, 38), (80, 38), (38, 76), (80, 76)])
    + "".join(f'<ellipse cx="{59+14*c:.1f}" cy="{59+14*s_:.1f}" rx="9" ry="9" fill="#4F8FE0" {W(2.4)}/>'
              for c, s_ in [(1, 0), (-1, 0), (0, 1), (0, -1)])
    + f'<circle cx="59" cy="59" r="12" fill="#FFD23F" {W(2.6)}/>'
    + f(59, 58, d=5, k=0.5)
    + f'<path d="M104 30 L112 92" stroke="#C99A62" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M104 30 L112 92" fill="none" {W(1.8)}/>'
    + f'<path d="M112 92 L116 110 L110 106Z" fill="#B8BCC9" {W(2.2)}/>'
    + f'<path d="M96 112 q6 -8 12 0 q6 8 12 0" fill="none" stroke="#F2C66D" stroke-width="3.4" stroke-linecap="round"/>'
    + sparkle(20, 20, 3.4, "#fff") + sparkle(104, 18, 2.6, "#fff"))

# Дендропарк Яблокова (Ивантеевка) — золотая осенняя лиственница с этикеткой на колышке
I["yablokov-dendropark-ivanteevka"] = ("#DDF1FF", "#7DB7E8",
    "золотая осенняя лиственница с тремя ярусами пушистых ветвей и коричневыми шишечками",
    "стоит в начале аллеи, у ствола на колышке табличка-этикетка с латинским названием, вниз осыпается золотая хвоя",
    f'<path d="M0 102 Q64 94 128 102 V128 H0Z" fill="#9CC86A" {W(2.4)}/>'
    + f'<path d="M54 128 L60 102 H68 L74 128Z" fill="#E8D8B0" {W(2)}/>'
    + "".join(f'<path d="M{x} 104 V60" stroke="#8A5A3C" stroke-width="3"/><path d="M{x} 56 L{x-9} 92 Q{x} 96 {x+9} 92Z" fill="#E6A93A" {W(2)}/>' for x in (14, 114))
    + f'<path d="M60 106 V24 H68 V106Z" fill="#8A5A3C" {W(2.6)}/>'
    + "".join(f'<path d="M64 {y} Q{64-w} {y+h*0.55} {64-w-4} {y+h} Q{64-w/2} {y+h-6} 64 {y+h-2} Q{64+w/2} {y+h-6} {64+w+4} {y+h} Q{64+w} {y+h*0.55} 64 {y}Z" fill="#F5B52E" {W(3)}/>'
              + f'<path d="M{64-w+4} {y+h-4} l-3 5 M{64-w/2} {y+h-4} l-1 6 M{64+w/2} {y+h-4} l1 6 M{64+w-4} {y+h-4} l3 5" {W(2)}/>'
              for y, w, h in [(12, 16, 26), (32, 26, 30), (56, 36, 32)])
    + "".join(f'<ellipse cx="{a}" cy="{b}" rx="3.2" ry="4" fill="#9C5B2E" {W(1.6)}/>' for a, b in [(48, 80), (84, 78), (74, 50), (54, 54)])
    + f(64, 70, d=9, k=0.7)
    + f'<path d="M92 108 V94" {W(2.4)}/><rect x="82" y="88" width="24" height="9" rx="2" fill="#fff" {W(2)}/>'
    + f'<path d="M85 92.5 H103" stroke="#2F6FD0" stroke-width="1.6"/>'
    + "".join(f'<path d="M{a} {b} l3 4" stroke="#E6A93A" stroke-width="2.2" stroke-linecap="round"/>' for a, b in [(30, 96), (104, 100), (40, 110), (22, 112)])
    + sparkle(104, 26, 3.6, "#fff") + sparkle(24, 30, 2.6, "#fff"))

# Музейный комплекс Зои Космодемьянской — фронтовое письмо-треугольник на снегу у берёзки
I["petrishchevo-zoya-museum"] = ("#EDF2FA", "#9FB1D0",
    "сложенное треугольником фронтовое письмо с полевым штемпелем",
    "лежит на снегу у тонкой берёзки, над ним горит маленькая красная звёздочка",
    f'<path d="M0 90 Q64 80 128 92 V128 H0Z" fill="#fff" {W(2.6)}/>'
    + f'<path d="M98 92 V18" stroke="#fff" stroke-width="7"/><path d="M95 92 V18 M101 92 V18" {W(1.8)}/>'
    + "".join(f'<path d="M{a} {b} h4" {W(2)}/>' for a, b in [(95, 30), (97, 46), (95, 62), (97, 78)])
    + f'<path d="M98 30 Q110 40 118 36 M98 50 Q86 58 80 54" fill="none" {W(2)}/>'
    + "".join(f'<path d="M{a} {b} l4 -3 l1 5Z" fill="#F2C66D" {W(1.2)}/>' for a, b in [(114, 36), (80, 54), (108, 42)])
    + '<g transform="rotate(-8 56 84)">'
    + f'<path d="M20 70 H92 L56 106Z" fill="#F5EBD3" {W(3.2)}/>'
    + f'<path d="M20 70 L56 88 L92 70" fill="none" {W(2.4)}/>'
    + f'<circle cx="74" cy="80" r="6" fill="none" stroke="#5A6BB0" stroke-width="2"/>'
    + f'<path d="M30 76 H46 M34 80 H48" stroke="#5A6BB0" stroke-width="1.4"/>'
    + f(54, 80, d=7, k=0.6) + '</g>'
    + f'<path d="M56 22 l4 9 10 1 -8 6 3 10 -9 -6 -9 6 3 -10 -8 -6 10 -1Z" fill="#E2453C" {W(2.4)}/>'
    + "".join(sparkle(x, y, r, "#fff") for x, y, r in [(20, 30, 3), (30, 50, 2.2), (118, 64, 2.4), (76, 14, 2.4)]))

# Музей семьи великого князя К. К. (Осташёво) — овальная рамка семейного фото с ребятами
I["ostashevo-romanov-museum"] = ("#F3E8FF", "#B694DA",
    "старинная овальная золочёная рамка семейного фото, внутри — родители и шестеро ребят-кружочков",
    "стоит на ножке-подставке на кружевной салфетке комода",
    f'<path d="M0 104 H128 V128 H0Z" fill="#8A5A3C" {W(2.6)}/>'
    + f'<path d="M20 104 Q30 98 40 104 Q50 98 60 104 Q70 98 80 104 Q90 98 100 104 Q110 98 108 104 L104 112 H24Z" fill="#fff" {W(2)}/>'
    + f'<path d="M84 98 L94 110" {W(3)}/>'
    + f'<ellipse cx="64" cy="58" rx="40" ry="44" fill="#E8B33A" {W(3.2)}/>'
    + f'<ellipse cx="64" cy="58" rx="32" ry="36" fill="#F2E6CF" {W(2.6)}/>'
    + "".join(f'<circle cx="{a}" cy="{b}" r="2.4" fill="#FFF3B0"/>' for a, b in [(64, 16), (28, 58), (100, 58), (64, 100)])
    + f'<circle cx="54" cy="40" r="7" fill="#FFD9B8" {W(2)}/><circle cx="74" cy="40" r="7" fill="#FFD9B8" {W(2)}/>'
    + f'<path d="M48 36 Q54 30 60 36 M68 34 Q74 28 80 34" fill="#6B4A2E" {W(1.6)}/>'
    + "".join(f'<circle cx="{a}" cy="{b}" r="5.5" fill="#FFE2C8" {W(1.8)}/>'
              f'<circle cx="{a-1.8:.1f}" cy="{b}" r=".9" fill="{O}"/><circle cx="{a+1.8:.1f}" cy="{b}" r=".9" fill="{O}"/>'
              for a, b in [(44, 62), (56, 62), (68, 62), (80, 62), (50, 76), (74, 76)])
    + f'<path d="M50 50 H78" {W(1.4)} opacity=".4"/>'
    + "".join(f'<circle cx="{a-2.4:.1f}" cy="40" r="1" fill="{O}"/><circle cx="{a+2.4:.1f}" cy="40" r="1" fill="{O}"/>' for a in (54, 74))
    + f'<path d="M62 76 Q64 80 66 76" fill="none" {W(1.4)}/>'
    + sparkle(112, 24, 3.6, "#fff") + sparkle(16, 36, 2.6, "#fff"))

# Дом-музей Танеева (Дютьково) — скрипичный ключ катается на качелях между липами
I["taneev-museum-dyutkovo"] = ("#E8FFE6", "#8ED08A",
    "чёрный скрипичный ключ-персонаж",
    "качается на деревянных дачных качелях, подвешенных к ветке старой липы, вокруг разлетаются ноты",
    f'<path d="M0 104 Q64 96 128 104 V128 H0Z" fill="#6DBA5A" {W(2.4)}/>'
    + f'<path d="M12 104 Q16 60 10 20" fill="none" stroke="#7A5434" stroke-width="10" stroke-linecap="round"/>'
    + f'<path d="M12 104 Q16 60 10 20" fill="none" {W(1.6)}/>'
    + f'<path d="M10 28 Q60 12 118 26" fill="none" stroke="#7A5434" stroke-width="7" stroke-linecap="round"/>'
    + f'<ellipse cx="34" cy="16" rx="30" ry="14" fill="#4FA34A" {W(2.4)}/><ellipse cx="96" cy="14" rx="30" ry="12" fill="#5CB352" {W(2.4)}/>'
    + f'<path d="M50 24 L46 92 M84 24 L88 92" {W(2.4)}/>'
    + f'<rect x="40" y="90" width="54" height="8" rx="3" fill="#C98A4B" {W(2.6)}/>'
    + f'<path d="M66 90 C58 84 56 72 64 66 C74 58 82 70 72 76 C62 82 54 72 58 60 C62 48 74 40 72 30 C70 24 64 26 64 34 L68 98" '
      f'fill="none" stroke="#2F2A40" stroke-width="5.5" stroke-linecap="round"/>'
    + f'<circle cx="62" cy="100" r="4" fill="#2F2A40"/>'
    + eye(62, 70, 0.55) + eye(72, 70, 0.55)
    + f'<path d="M64 76 Q67 79 70 76" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round"/>'
    + "".join(f'<ellipse cx="{a}" cy="{b}" rx="3.6" ry="2.8" fill="{O}" transform="rotate(-20 {a} {b})"/><path d="M{a+3} {b} V{b-12}" {W(2)}/>'
              for a, b in [(102, 58), (112, 80), (26, 70)])
    + sparkle(108, 40, 3, "#fff") + sparkle(30, 92, 2.4, "#fff"))


if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        a, b, hero, scene, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
