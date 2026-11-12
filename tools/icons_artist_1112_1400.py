"""Робот «художник», 12.11 ~14:00 UTC.
check_unique.py: 0 повторов по точному тексту и картинке, но в реестре — серии одного героя, которые проверка не ловит
(разные шапки на том же предмете): 21 «футбольный мяч в …», 14 «баскетбольный мяч …», 8 «теннисная ракетка …».
По правилу абсолютной уникальности из каждой серии оставлен один, остальные перерисуются по нескольку за запуск;
в этом запуске — все такие иконки мест, которые сейчас на карте. Каждая придумана и нарисована отдельно.
Запуск из корня: python3 tools/icons_artist_1112_1400.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT


def limb(d, color, w=7):
    return (f'<path d="{d}" fill="none" stroke="{O}" stroke-width="{w+3}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')


def football(cx, cy, r, fill="#FFFFFF", patch="#2B2B33"):
    """футбольный мяч: центральный пятиугольник и края соседних"""
    import math
    pts = " ".join(f"{cx + r*.36*math.sin(math.radians(a)):.1f},{cy - r*.36*math.cos(math.radians(a)):.1f}" for a in range(0, 360, 72))
    out = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" {W(2.8)}/><polygon points="{pts}" fill="{patch}"/>'
    for a in range(0, 360, 72):
        x1, y1 = cx + r*.36*math.sin(math.radians(a)), cy - r*.36*math.cos(math.radians(a))
        x2, y2 = cx + r*.78*math.sin(math.radians(a)), cy - r*.78*math.cos(math.radians(a))
        out += f'<path d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}" fill="none" stroke="{patch}" stroke-width="{max(1.4, r*.1):.1f}"/>'
        x3, y3 = cx + r*.98*math.sin(math.radians(a)), cy - r*.98*math.cos(math.radians(a))
        out += f'<circle cx="{x3:.1f}" cy="{y3:.1f}" r="{r*.2:.1f}" fill="{patch}"/>'
    return out + f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" {W(2.8)}/>'


def basketball(cx, cy, r):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#F08A2E" {W(2.8)}/>'
            f'<path d="M{cx-r} {cy} H{cx+r} M{cx} {cy-r} V{cy+r} '
            f'M{cx-r*.7} {cy-r*.7} Q{cx-r*.25} {cy} {cx-r*.7} {cy+r*.7} '
            f'M{cx+r*.7} {cy-r*.7} Q{cx+r*.25} {cy} {cx+r*.7} {cy+r*.7}" fill="none" stroke="{O}" stroke-width="2"/>')


def white_eye(x, y, k=1.0):
    return (f'<circle cx="{x}" cy="{y}" r="{4.6*k:.1f}" fill="#FFFFFF"/>'
            f'<circle cx="{x+.6*k:.1f}" cy="{y+.6*k:.1f}" r="{2.6*k:.1f}" fill="{O}"/>'
            f'<circle cx="{x-.3*k:.1f}" cy="{y-.6*k:.1f}" r="{1*k:.1f}" fill="#fff"/>')


I = {}

# Академия умного футбола: «умный» удар — девочка в очках закручивает мяч по пунктирной дуге
I["smart-football-perervinsky"] = (
    "кудрявая девочка-футболистка в круглых очках и синей форме",
    "закручивает удар: мяч улетает вверх по белой пунктирной дуге, как по расчёту",
    ("#E9FFF2", "#45B88C"), f'''
<ellipse cx="64" cy="118" rx="60" ry="10" fill="#5DBB55" {W(2.2)}/>
<path d="M52 104 Q96 104 102 60 Q104 44 96 36" fill="none" stroke="#FFFFFF" stroke-width="3.6" stroke-dasharray="5 6" stroke-linecap="round"/>
{football(92, 30, 15)}
{limb("M38 84 L34 110", "#2F5FB3", 8)}
<path d="M28 110 h12 v4 h-14 z" fill="#2B2B33" {W(2)}/>
{limb("M46 84 Q54 96 58 104", "#2F5FB3", 8)}
<ellipse cx="60" cy="106" rx="6" ry="4" fill="#2B2B33" {W(2)}/>
{limb("M34 64 L22 78", "#F6D2B0", 5)}
{limb("M54 64 L64 74", "#F6D2B0", 5)}
<path d="M32 60 H56 L54 88 H34 Z" fill="#3E7BE0" {W(3)}/>
<path d="M44 62 V86" fill="none" stroke="#FFFFFF" stroke-width="3"/>
<circle cx="44" cy="44" r="12" fill="#F6D2B0" {W(2.8)}/>
<circle cx="34" cy="36" r="6" fill="#6B3E22" {W(2)}/><circle cx="41" cy="31" r="6" fill="#6B3E22" {W(2)}/>
<circle cx="49" cy="31" r="6" fill="#6B3E22" {W(2)}/><circle cx="55" cy="37" r="6" fill="#6B3E22" {W(2)}/>
{eye(39.5, 46, .5)}{eye(48.5, 46, .5)}
<circle cx="39.5" cy="46" r="5" fill="none" {W(2)}/><circle cx="48.5" cy="46" r="5" fill="none" {W(2)}/>
<path d="M44.5 46 h-0" fill="none" {W(2)}/>
{smile(44, 52, 3, .6)}
{sparkle(112, 18, 4.5)}''')

# ФК «Легенда»: бронзовый памятник юному футболисту — нога на мяче
I["legenda-football-pyatnitskoe"] = (
    "бронзовая статуя мальчика-футболиста на сером гранитном постаменте",
    "гордо подбоченилась и поставила ногу на бронзовый мяч, сверкая на солнце",
    ("#FFF3D6", "#C9A15A"), f'''
<path d="M30 92 H98 L94 120 H34 Z" fill="#9AA0AA" {W(3)}/>
<rect x="26" y="86" width="76" height="9" rx="2" fill="#B9BEC6" {W(2.6)}/>
<path d="M44 106 H84" fill="none" stroke="#7D838D" stroke-width="2.4" stroke-linecap="round"/>
{football(84, 72, 14, "#E2AE6A", "#6A3A12")}
{limb("M56 68 L54 86", "#B87333", 9)}
{limb("M64 66 L72 62", "#B87333", 9)}
{limb("M50 44 Q38 50 46 58", "#B87333", 6)}
{limb("M70 44 Q80 34 82 22", "#B87333", 6)}
<path d="M48 40 H72 L70 70 H50 Z" fill="#B87333" {W(3)}/>
<path d="M60 42 V68" fill="none" stroke="#8C5A2B" stroke-width="2.6"/>
<circle cx="60" cy="27" r="12" fill="#C47F3E" {W(2.8)}/>
<path d="M48 25 Q50 14 60 14 Q70 14 72 25 Q66 19 60 20 Q54 19 48 25 Z" fill="#8C5A2B" {W(2)}/>
{eye(55.5, 28, .55)}{eye(64.5, 28, .55)}{smile(60, 33, 3, .6)}
{sparkle(86, 50, 5)}{sparkle(40, 66, 3.5)}{sparkle(22, 30, 4)}''')

# ФК «Энергия»: энергичный петушок-футболист
I["energiya-fc-mroshcha"] = (
    "рыжий петушок-футболист с красным гребешком и зелёным хвостом",
    "с утра пораньше в прыжке лупит лапой по мячу, крылья нараспашку",
    ("#FFF0C8", "#F29A3A"), f'''
<path d="M30 64 Q10 46 18 28 Q26 48 36 54 Q24 36 34 22 Q38 46 44 54 Z" fill="#2FA36B" {W(2.6)}/>
<ellipse cx="54" cy="68" rx="24" ry="20" fill="#E8692C" {W(3)}/>
<path d="M44 62 Q52 50 66 60 Q56 74 44 62 Z" fill="#C84A1E" {W(2.2)}/>
<path d="M50 86 L46 106 M46 106 l-6 4 M46 106 l2 6" fill="none" stroke="#F2B21A" stroke-width="4" stroke-linecap="round"/>
<path d="M62 84 L78 96 M78 96 l6 -2 M78 96 l4 5" fill="none" stroke="#F2B21A" stroke-width="4" stroke-linecap="round"/>
<path d="M64 56 Q66 40 70 34" fill="none" stroke="{O}" stroke-width="14" stroke-linecap="round"/>
<path d="M64 56 Q66 40 70 34" fill="none" stroke="#E8692C" stroke-width="10" stroke-linecap="round"/>
<circle cx="72" cy="32" r="12" fill="#E8692C" {W(2.8)}/>
<path d="M64 22 Q64 12 70 16 Q72 8 77 14 Q82 10 82 20 Z" fill="#E0302E" {W(2.4)}/>
<path d="M83 30 L94 34 L83 38 Z" fill="#F6C83B" {W(2.2)}/>
<path d="M80 40 Q84 48 78 48 Q76 44 78 40 Z" fill="#E0302E" {W(1.8)}/>
{eye(74, 29, .6)}{blush(72, 37, .5)}
{football(94, 100, 14)}
<path d="M100 76 l6 -4 M108 84 l7 -1" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>
{sparkle(104, 22, 4)}''')

# Pinkov Football Academy: розовый страусёнок длинной ногой бьёт по мячу
I["pinkov-academy-presnensky"] = (
    "розовый пушистый страусёнок на длинных ногах",
    "вытянул шею к небу и длинной ногой отправляет мяч вперёд",
    ("#FFEAF4", "#E46AA6"), f'''
<ellipse cx="64" cy="118" rx="58" ry="9" fill="#77C46A" {W(2.2)}/>
{limb("M44 78 L42 96 L44 112", "#F2B48C", 4)}
<path d="M38 112 h12" fill="none" {W(3)}/>
{limb("M54 78 L66 92 L82 98", "#F2B48C", 4)}
<path d="M30 66 Q22 52 34 46 Q40 36 52 42 Q64 38 68 50 Q78 56 70 68 Q66 80 52 80 Q34 82 30 66 Z" fill="#F7A6CB" {W(3)}/>
<path d="M28 54 Q18 50 20 40 M32 48 Q26 38 32 32" fill="none" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>
<path d="M62 48 Q64 30 70 20" fill="none" stroke="{O}" stroke-width="10" stroke-linecap="round"/>
<path d="M62 48 Q64 30 70 20" fill="none" stroke="#F7C5DC" stroke-width="6.4" stroke-linecap="round"/>
<circle cx="72" cy="18" r="9" fill="#F7C5DC" {W(2.6)}/>
<path d="M80 17 Q90 18 80 23 Z" fill="#F2B48C" {W(2)}/>
<path d="M68 10 q-2 -6 2 -6 M72 9 q0 -6 4 -5" fill="none" stroke="{O}" stroke-width="2" stroke-linecap="round"/>
{eye(73, 17, .55)}{blush(70, 23, .45)}
{football(96, 96, 15)}
{sparkle(104, 52, 4.5)}{sparkle(20, 92, 3.5)}''')

# СК «Виктория» в Электроуглях: уголёк-футболист
I["viktoriya-elektrougli"] = (
    "чёрный уголёк с оранжевыми светящимися трещинками и огоньком на макушке",
    "в прыжке забивает мяч, из-под ноги разлетаются искры",
    ("#FFE4D2", "#B5452E"), f'''
<path d="M46 34 Q44 22 52 16 Q52 26 58 24 Q58 14 64 10 Q66 22 70 28 Q74 22 72 16 Q80 26 74 36 Z" fill="#FFB02E" {W(2.4)}/>
<path d="M54 30 Q56 24 60 24 Q62 30 66 30" fill="none" stroke="#FFE27A" stroke-width="3" stroke-linecap="round"/>
{limb("M50 84 L44 104", "#3A3A44", 7)}
{limb("M68 82 L82 92", "#3A3A44", 7)}
{limb("M38 58 L26 50", "#3A3A44", 6)}
{limb("M80 58 L90 48", "#3A3A44", 6)}
<path d="M36 46 Q40 32 58 32 Q76 30 82 46 Q88 66 78 80 Q64 92 46 84 Q30 74 36 46 Z" fill="#3A3A44" {W(3)}/>
<path d="M42 72 L48 66 M76 72 L72 66" fill="none" stroke="#FF8A2B" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
{white_eye(52, 50, .9)}{white_eye(68, 50, .9)}
<path d="M53 60 Q60 68 67 60" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>
{football(96, 98, 15)}
<circle cx="84" cy="80" r="2.4" fill="#FFB02E"/><circle cx="78" cy="102" r="2" fill="#FFB02E"/><circle cx="88" cy="74" r="1.6" fill="#FFE27A"/>
{sparkle(104, 30, 4.5)}''')

# ФК «Ястреб»: «ястребиный глаз» — телекамера на штативе следит, пересёк ли мяч линию ворот
I["fk-yastreb-kommunarka"] = (
    "чёрная телекамера «ястребиный глаз» с огромным объективом-глазом на высоком штативе",
    "пристально следит, как футбольный мяч пересекает белую линию у штанги ворот",
    ("#E3F2FF", "#5A8FD0"), f'''
<rect x="0" y="104" width="128" height="30" fill="#5DBB55"/>
<path d="M0 104 H128" fill="none" stroke="{O}" stroke-width="2.4"/>
<path d="M0 110 H58" fill="none" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round"/>
<path d="M12 40 H32 V110" fill="none" stroke="{O}" stroke-width="10" stroke-linejoin="round"/>
<path d="M12 40 H32 V110" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-linejoin="round"/>
<path d="M14 46 L28 60 M14 60 L28 74 M14 74 L28 88 M14 88 L28 102 M28 46 L14 60 M28 60 L14 74 M28 74 L14 88" fill="none" stroke="#FFFFFF" stroke-width="1.4" opacity=".8"/>
{football(46, 98, 12)}
<path d="M92 72 L76 116 M92 72 L108 116 M92 72 V116" fill="none" stroke="{O}" stroke-width="3.4" stroke-linecap="round"/>
<rect x="72" y="44" width="42" height="28" rx="6" fill="#2E3140" {W(3)}/>
<rect x="88" y="36" width="16" height="9" rx="2" fill="#2E3140" {W(2.4)}/>
<circle cx="72" cy="58" r="15" fill="#2E3140" {W(3)}/>
<circle cx="72" cy="58" r="10" fill="#7FC8F0" {W(2)}/>
<circle cx="70" cy="60" r="5" fill="{O}"/><circle cx="68" cy="56" r="2.6" fill="#FFFFFF"/>
<circle cx="106" cy="52" r="3" fill="#FF3B3B"/>
{blush(96, 64, .6)}<path d="M92 60 Q97 64 102 60" fill="none" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round"/>
{sparkle(52, 24, 4.5)}''')

# Hola Fútbol: весёлый кактус в бутсах (испанское «Hola!»)
I["hola-futbol-vnukovo"] = (
    "зелёный кактус-футболист с розовым цветком на макушке, в красных бутсах",
    "стоит на песке, приветственно вскинул руку-отросток и пинает мяч",
    ("#FFEEDD", "#D9764A"), f'''
<path d="M0 112 Q40 100 70 108 Q100 114 128 104 V128 H0 Z" fill="#F2C77A" {W(2.4)}/>
<path d="M50 100 L46 110 M62 100 L70 106" fill="none" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M50 100 L46 110 M62 100 L70 106" fill="none" stroke="#3E9A4A" stroke-width="4" stroke-linecap="round"/>
<path d="M38 112 Q38 106 46 108 L50 112 Z" fill="#E0302E" {W(2)}/>
<path d="M68 102 Q76 100 78 106 L72 110 Z" fill="#E0302E" {W(2)}/>
<path d="M40 58 Q24 58 24 44 V32 Q24 26 30 26 Q36 26 36 32 V44 Q36 48 40 48 Z" fill="#4DB35A" {W(2.8)}/>
<path d="M72 70 Q88 70 88 58 V52 Q88 46 82 46 Q76 46 76 52 V58 Q76 60 72 60 Z" fill="#4DB35A" {W(2.8)}/>
<path d="M40 100 V34 Q40 22 56 22 Q72 22 72 34 V100 Z" fill="#4DB35A" {W(3)}/>
<path d="M50 30 V96 M62 30 V96" fill="none" stroke="#3E9A4A" stroke-width="2.2"/>
<path d="M44 76 l-4 -2 M68 82 l4 -2 M44 92 l-4 2 M68 40 l4 -2" fill="none" stroke="{O}" stroke-width="1.8" stroke-linecap="round"/>
<circle cx="50" cy="20" r="5" fill="#F27BAA" {W(2)}/><circle cx="58" cy="17" r="5" fill="#F27BAA" {W(2)}/><circle cx="64" cy="22" r="5" fill="#F27BAA" {W(2)}/>
<circle cx="57" cy="22" r="3" fill="#FFD45E"/>
{face(56, 50, 7, .7)}
{football(96, 96, 14)}
{sparkle(104, 30, 4.5)}{sparkle(22, 84, 3.5)}''')

# «Хаски» (Смольная): поролоновая рука болельщика «№1» указывает на мяч, влетающий в кольцо
I["husky-basket-smolnaya"] = (
    "огромная синяя поролоновая рука болельщика с вытянутым указательным пальцем и цифрой 1",
    "показывает пальцем вверх на баскетбольный мяч, который влетает в кольцо",
    ("#E8E8FF", "#5B5BD6"), f'''
<rect x="80" y="10" width="40" height="28" rx="3" fill="#FFFFFF" {W(2.8)}/>
<rect x="92" y="20" width="16" height="12" fill="none" stroke="#E0302E" stroke-width="2.6"/>
{basketball(100, 46, 9)}
<ellipse cx="100" cy="42" rx="13" ry="3.4" fill="none" stroke="{O}" stroke-width="5"/>
<ellipse cx="100" cy="42" rx="13" ry="3.4" fill="none" stroke="#F06A2E" stroke-width="2.6"/>
<path d="M88 44 L92 58 M96 45 L97 60 M104 45 L103 60 M112 44 L108 58 M91 52 H109" fill="none" stroke="#FFFFFF" stroke-width="1.6"/>
<path d="M30 120 L28 96 Q20 86 26 74 L38 70 L42 64 Q40 56 48 54 L56 52 L58 30 Q58 20 66 20 Q74 20 74 30 L74 60 Q86 62 84 76 L82 96 L78 120 Z" fill="#3F64E0" {W(3.2)}/>
<path d="M42 64 Q52 66 56 62 M38 72 Q46 76 54 72" fill="none" {W(2.2)}/>
<path d="M44 104 H70 L68 120 H46 Z" fill="#FFD45E" {W(2.6)}/>
<path d="M60 108 L62 106 V118" fill="none" stroke="{O}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
{eye(58, 84, .6)}{eye(70, 84, .6)}{blush(54, 91, .5)}{blush(74, 91, .5)}{smile(64, 90, 3, .6)}
<path d="M80 26 Q76 18 82 12" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" opacity=".8"/>
{sparkle(30, 34, 5)}''')

# «Хаски» (Ярославское ш.): ленивец лениво висит на баскетбольном кольце, обнимая мяч
I["husky-basket-yaroslavskoe"] = (
    "бурый ленивец с тёмной полоской у глаз и сонной улыбкой",
    "висит на длинных лапах на оранжевом кольце под щитом и в обнимку держит баскетбольный мяч",
    ("#EFF7E8", "#7FB862"), f'''
<rect x="34" y="6" width="60" height="30" rx="3" fill="#FFFFFF" {W(2.8)}/>
<rect x="54" y="16" width="20" height="14" fill="none" stroke="#E0302E" stroke-width="2.6"/>
<path d="M50 42 L54 58 M58 43 L60 58 M70 43 L68 58 M78 42 L74 58" fill="none" stroke="#FFFFFF" stroke-width="1.8"/>
{limb("M50 42 Q46 56 50 72", "#9A6B44", 8)}
{limb("M78 42 Q82 56 78 72", "#9A6B44", 8)}
<path d="M46 40 q2 -6 6 0 M74 40 q2 -6 6 0" fill="none" stroke="{O}" stroke-width="2.4" stroke-linecap="round"/>
<ellipse cx="64" cy="40" rx="18" ry="4" fill="none" stroke="{O}" stroke-width="5.6"/>
<ellipse cx="64" cy="40" rx="18" ry="4" fill="none" stroke="#F06A2E" stroke-width="3"/>
<ellipse cx="64" cy="94" rx="24" ry="24" fill="#9A6B44" {W(3)}/>
<ellipse cx="64" cy="76" rx="16" ry="13" fill="#E9D3B0" {W(2.6)}/>
<path d="M50 76 Q56 70 62 76 M66 76 Q72 70 78 76" fill="none" stroke="#5A3A22" stroke-width="5" stroke-linecap="round"/>
<path d="M53 75 Q56 78 59 75 M69 75 Q72 78 75 75" fill="none" stroke="{O}" stroke-width="2.2" stroke-linecap="round"/>
<ellipse cx="64" cy="81" rx="3" ry="2" fill="{O}"/>
{smile(64, 84, 4, .7)}
{basketball(64, 104, 13)}
{limb("M42 94 Q48 106 56 106", "#9A6B44", 6)}
{limb("M86 94 Q80 106 72 106", "#9A6B44", 6)}
<path d="M86 26 q4 -2 8 0 M90 20 q3 -2 6 0" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
{sparkle(20, 60, 4)}''')

# «Стремление» (ул. Яблочкова): коала упорно карабкается по стойке кольца с мячом под мышкой
I["stremlenie-basket-timiryazevskaya"] = (
    "серая коала с пушистыми ушами и большим чёрным носом",
    "упорно лезет вверх по стойке баскетбольного кольца, зажав мяч под мышкой",
    ("#F1ECFF", "#9A7FD9"), f'''
<rect x="78" y="20" width="12" height="110" fill="#7D8794" {W(3)}/>
<rect x="62" y="6" width="56" height="26" rx="3" fill="#FFFFFF" {W(2.8)}/>
<rect x="78" y="14" width="20" height="12" fill="none" stroke="#E0302E" stroke-width="2.6"/>
<ellipse cx="78" cy="38" rx="14" ry="3.4" fill="none" stroke="{O}" stroke-width="5.4"/>
<ellipse cx="78" cy="38" rx="14" ry="3.4" fill="none" stroke="#F06A2E" stroke-width="2.8"/>
<path d="M66 40 L70 52 M74 41 L75 54 M82 41 L81 54 M90 40 L86 52" fill="none" stroke="#FFFFFF" stroke-width="1.6"/>
<ellipse cx="66" cy="88" rx="18" ry="22" fill="#9EA7B4" {W(3)}/>
<ellipse cx="66" cy="94" rx="10" ry="13" fill="#E4E8EE"/>
{limb("M72 74 Q80 70 84 62", "#9EA7B4", 7)}
{limb("M74 104 Q82 104 84 98", "#9EA7B4", 7)}
<circle cx="40" cy="44" r="11" fill="#9EA7B4" {W(2.8)}/><circle cx="40" cy="44" r="6" fill="#F3C9D8"/>
<circle cx="76" cy="44" r="11" fill="#9EA7B4" {W(2.8)}/><circle cx="76" cy="44" r="6" fill="#F3C9D8"/>
<circle cx="58" cy="58" r="17" fill="#9EA7B4" {W(3)}/>
<ellipse cx="58" cy="62" rx="5.5" ry="7" fill="#2B2B33"/>
{eye(50, 54, .6)}{eye(66, 54, .6)}{blush(46, 64, .55)}{blush(70, 64, .55)}
<path d="M54 71 Q58 74 62 71" fill="none" {W(2)}/>
{basketball(42, 92, 13)}
{limb("M52 82 Q40 80 34 88", "#9EA7B4", 6)}
<path d="M24 22 v8 M20 26 h8" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"/>
{sparkle(108, 60, 4)}''')

# СШОР «Спартак» по баскетболу: бросок крюком в прыжке
I["sshor-spartak-basket-lyubertsy"] = (
    "темноволосый мальчик в красной майке с белой полосой поперёк груди",
    "в прыжке бросает мяч крюком одной рукой через голову — мяч летит к кольцу справа вверху",
    ("#FFE9E6", "#D9484A"), f'''
<rect x="98" y="8" width="30" height="24" fill="#FFFFFF" {W(2.6)}/>
<ellipse cx="104" cy="38" rx="12" ry="3" fill="none" stroke="{O}" stroke-width="5"/>
<ellipse cx="104" cy="38" rx="12" ry="3" fill="none" stroke="#F06A2E" stroke-width="2.6"/>
<path d="M94 40 L97 50 M104 41 V52 M114 40 L111 50" fill="none" stroke="#FFFFFF" stroke-width="1.6"/>
<path d="M44 22 Q66 4 88 26" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-dasharray="4 5" stroke-linecap="round"/>
{limb("M60 92 L54 104 L60 114", "#F6D2B0", 6)}
{limb("M72 92 L76 116", "#F6D2B0", 6)}
<path d="M52 112 h12 v4 h-14 z M70 116 h12 v4 h-14 z" fill="#FFFFFF" {W(2)}/>
<path d="M56 82 H76 L78 94 H54 Z" fill="#FFFFFF" {W(2.6)}/>
{limb("M58 64 Q42 52 40 34", "#F6D2B0", 6)}
{limb("M74 66 L92 74", "#F6D2B0", 6)}
<path d="M56 60 H76 L76 84 H56 Z" fill="#D8263A" {W(3)}/>
<path d="M56 70 H76" fill="none" stroke="#FFFFFF" stroke-width="4.4"/>
<circle cx="68" cy="46" r="11" fill="#F6D2B0" {W(2.8)}/>
<path d="M57 44 Q57 32 68 32 Q80 32 79 44 Q74 38 68 39 Q62 38 57 44 Z" fill="#3B2A22" {W(2)}/>
{eye(64, 47, .55)}{eye(72, 47, .55)}{smile(68, 52, 3, .6)}
{basketball(38, 26, 13)}
{sparkle(20, 72, 4.5)}{sparkle(104, 96, 4)}''')

# СК «Виртуоз» (баскетбол и футбол): тукан-виртуоз держит баскетбольный мяч на клюве, а футбольный — на лапе
I["virtuoz-16-parkovaya"] = (
    "чёрный тукан с белой грудкой и огромным оранжево-жёлтым клювом",
    "балансирует баскетбольным мячом на кончике клюва и одновременно футбольным на поднятой лапе",
    ("#E4FBFF", "#3AB7C9"), f'''
{basketball(98, 26, 14)}
<path d="M58 54 Q80 40 94 40 Q98 44 92 50 Q78 60 60 64 Z" fill="#F6A21E" {W(2.8)}/>
<path d="M60 58 Q78 50 92 46" fill="none" {W(1.8)}/>
<path d="M88 42 Q94 40 94 44 Q92 48 88 48 Z" fill="#E0302E"/>
<path d="M38 66 Q30 92 40 108 Q50 116 60 106 Q70 92 66 70 Z" fill="#2B2B33" {W(3)}/>
<path d="M36 104 L28 120 L40 112 Z" fill="#2B2B33" {W(2.4)}/>
<circle cx="52" cy="54" r="16" fill="#2B2B33" {W(3)}/>
<path d="M44 62 Q48 80 60 82 Q66 74 64 62 Q56 56 44 62 Z" fill="#FFF6E0"/>
<circle cx="56" cy="50" r="7" fill="#7FD3E8" {W(1.8)}/>
{eye(57, 50, .6)}
<path d="M48 108 V118 M48 118 l-4 3 M48 118 l4 3" fill="none" stroke="#5CC0E8" stroke-width="3.4" stroke-linecap="round"/>
<path d="M58 102 L74 104 L80 96" fill="none" stroke="#5CC0E8" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>
{football(88, 86, 11)}
{sparkle(24, 30, 5)}{sparkle(114, 64, 3.5)}''')

# Школа тенниса Екатерины Бородиной: девочка в прыжке подаёт сверху
I["tennis-borodina-kapitoliy"] = (
    "рыжая девочка-теннисистка с высоким хвостом в голубом теннисном платье",
    "подаёт сверху: подбросила жёлтый мяч левой рукой, ракетка занесена за голову",
    ("#FDF2FF", "#C46ED8"), f'''
{limb("M58 98 L56 116", "#F6D2B0", 6)}
{limb("M68 98 L72 114", "#F6D2B0", 6)}
<path d="M50 116 h12 v4 h-14 z M68 114 h12 v4 h-14 z" fill="#FFFFFF" {W(2)}/>
{limb("M56 64 Q46 46 44 30", "#F6D2B0", 5)}
{limb("M72 64 Q82 58 84 46", "#F6D2B0", 5)}
<path d="M84 46 L94 34" fill="none" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M84 46 L94 34" fill="none" stroke="#2B2B33" stroke-width="4" stroke-linecap="round"/>
<ellipse cx="102" cy="22" rx="12" ry="15" transform="rotate(38 102 22)" fill="#FFFFFF" fill-opacity=".35" stroke="{O}" stroke-width="3.4"/>
<path d="M96 12 L110 30 M93 17 L106 34 M100 8 L113 25 M94 26 L108 14 M98 31 L112 19 M92 20 L104 10" fill="none" stroke="{O}" stroke-width="1.2" opacity=".7"/>
<path d="M54 60 H74 L84 100 H44 Z" fill="#7CC8F2" {W(3)}/>
<path d="M48 92 H80" fill="none" stroke="#FFFFFF" stroke-width="3"/>
<path d="M70 38 Q86 30 88 48 Q84 40 72 46 Z" fill="#E87A2E" {W(2.4)}/>
<circle cx="64" cy="46" r="11" fill="#F6D2B0" {W(2.8)}/>
<path d="M53 44 Q53 33 64 33 Q75 33 75 44 Q70 38 64 39 Q58 38 53 44 Z" fill="#E87A2E" {W(2)}/>
{eye(60, 47, .55)}{eye(68, 47, .55)}{smile(64, 52, 3, .6)}
<circle cx="40" cy="16" r="9" fill="#D7F25A" {W(2.6)}/>
<path d="M33 12 Q40 16 34 22 M46 10 Q40 16 47 21" fill="none" stroke="#FFFFFF" stroke-width="1.8"/>
{sparkle(22, 60, 4.5)}{sparkle(104, 84, 4)}''')

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
