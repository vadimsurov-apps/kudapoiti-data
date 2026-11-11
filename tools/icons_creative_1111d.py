"""Иконки робота creative, 11.11 (второй запуск). Каждая придумана и нарисована отдельно: свой герой, своя сцена,
своя компоновка и свой фон (правило абсолютной уникальности). python3 tools/icons_creative_1111d.py → icons-src/<id>.svg"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def bg(a, b, body, cx="38%", cy="28%"):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
<defs>
 <radialGradient id="g" cx="{cx}" cy="{cy}" r="85%"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></radialGradient>
 <clipPath id="c"><circle cx="64" cy="64" r="61"/></clipPath>
</defs>
<circle cx="64" cy="64" r="61" fill="url(#g)"/>
<g clip-path="url(#c)">{body}</g>
<ellipse cx="44" cy="22" rx="20" ry="7" fill="#fff" opacity=".3"/>
</svg>'''


def ln(c, w):
    return f'stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"'


def note(x, y, k=1.0, c=O):
    return (f'<ellipse cx="{x}" cy="{y}" rx="{5*k:.1f}" ry="{4*k:.1f}" fill="{c}" transform="rotate(-20 {x} {y})"/>'
            f'<path d="M{x+4.5*k:.1f} {y-1*k:.1f} V{y-17*k:.1f} Q{x+10*k:.1f} {y-14*k:.1f} {x+11*k:.1f} {y-9*k:.1f}" fill="none" stroke="{c}" stroke-width="{2.4*k:.1f}" stroke-linecap="round"/>')


def tutu(cx, cy, w, c, c2="#fff"):
    pts = []
    n = 9
    for i in range(n + 1):
        x = cx - w + 2 * w * i / n
        pts.append(f"L{x:.1f} {cy + (7 if i % 2 else 3)}")
    return (f'<path d="M{cx - w*0.55:.1f} {cy - 6} Q{cx} {cy - 10} {cx + w*0.55:.1f} {cy - 6} L{cx + w} {cy + 3} '
            + " ".join(reversed(pts)) + f' Z" fill="{c}" {s()}/>'
            f'<path d="M{cx - w*0.7:.1f} {cy} Q{cx} {cy + 5} {cx + w*0.7:.1f} {cy}" fill="none" stroke="{c2}" stroke-width="2" opacity=".8"/>')


I = {}

# 1. Академия детского мюзикла (Беляево) — афишная тумба пританцовывает на сцене
I["adm-miklukho-maklaya"] = ("круглая афишная тумба-колонна с куполом-шапочкой и мордашкой",
    "пританцовывает на сцене, на её боку афиша с поющим малышом и нотами", bg("#FFF4D6", "#F2B94A", f'''
<rect x="0" y="106" width="128" height="26" fill="#8A4B2A"/><path d="M0 106 H128" {s()}/>
<path d="M44 106 l-6 8 M84 106 l6 8" {s('stroke-width="4"')}/>
<rect x="38" y="34" width="52" height="72" rx="6" fill="#3E8E6A" {s()}/>
<path d="M34 34 Q64 4 94 34Z" fill="#2E6E52" {s()}/><circle cx="64" cy="14" r="4" fill="#FFD25E" {s('stroke-width="2"')}/>
<rect x="32" y="32" width="64" height="7" rx="3" fill="#2E6E52" {s()}/>
<rect x="44" y="64" width="40" height="36" rx="2" fill="#FFF6E0" {s('stroke-width="2.4"')}/>
<circle cx="60" cy="78" r="6" fill="#FFCFA8" {s('stroke-width="2"')}/><path d="M54 98 Q60 84 66 98Z" fill="#E8546A" {s('stroke-width="2"')}/>
<ellipse cx="62" cy="81" rx="1.6" ry="2" fill="{O}"/>
{note(74, 82, 0.55, "#E8546A")}{note(78, 92, 0.45, "#3B6FD9")}
{face(64, 50, d=9, k=0.85)}
{sparkle(20, 50, 6)}{sparkle(108, 60, 5)}{sparkle(104, 30, 4)}
'''))

# 2. Гитарная школа № 1 (Беляево) — усилитель-комбик с подключённой гитарой
I["guitar-school-1-miklukho"] = ("чёрный гитарный усилитель-комбик с решёткой-улыбкой",
    "к нему шнуром подключена маленькая оранжевая акустическая гитара, из динамика вылетают ноты", bg("#E8F7EC", "#58B97A", f'''
<rect x="18" y="48" width="58" height="60" rx="8" fill="#2F2B3A" {s()}/>
<rect x="24" y="54" width="46" height="10" rx="3" fill="#C9A35A" {s('stroke-width="2"')}/>
<circle cx="30" cy="59" r="2.4" fill="#2F2B3A"/><circle cx="40" cy="59" r="2.4" fill="#2F2B3A"/><circle cx="50" cy="59" r="2.4" fill="#2F2B3A"/><circle cx="60" cy="59" r="2.4" fill="#2F2B3A"/>
<rect x="24" y="68" width="46" height="34" rx="5" fill="#5A5468" {s('stroke-width="2"')}/>
{eye(38, 78, 0.8)}{eye(56, 78, 0.8)}
<path d="M36 88 Q47 98 58 88" fill="none" stroke="#FFD25E" stroke-width="3" stroke-linecap="round"/>
<path d="M28 94 H66" stroke="#46405A" stroke-width="1.6"/>
<path d="M76 98 Q90 112 96 96" fill="none" {ln("#2F2B3A", 3)}/>
<ellipse cx="100" cy="86" rx="12" ry="14" fill="#F2943A" {s()}/><ellipse cx="100" cy="70" rx="9" ry="10" fill="#F2943A" {s()}/>
<circle cx="100" cy="80" r="4" fill="#5A3416"/>
<rect x="97" y="30" width="6" height="40" rx="2" fill="#8C5A33" {s('stroke-width="2.4"')}/>
<rect x="95" y="24" width="10" height="9" rx="2" fill="#6B4224" {s('stroke-width="2.2"')}/>
{note(44, 38, 0.8, "#fff")}{note(66, 28, 0.6, "#FFD25E")}{note(24, 30, 0.55, "#fff")}
'''))

# 3. Буфф (Пионерская) — девочка в бумажной короне читает стихи с табуретки
I["buff-kastanaevskaya"] = ("девочка-актриса в бумажной короне и плаще из красной занавески",
    "стоит на табуретке и с пафосом читает стихи, раскинув руки", bg("#F2EAFF", "#9C7FE0", f'''
<rect x="44" y="96" width="40" height="7" rx="3" fill="#D9A15E" {s()}/>
<path d="M50 103 L46 124 M78 103 L82 124" {s('stroke-width="4.5"')}/>
<path d="M50 96 Q40 70 46 58 L82 58 Q88 70 78 96Z" fill="#D8344A" {s()}/>
<path d="M58 60 L62 94 L68 94 L70 60Z" fill="#FFE07A" {s('stroke-width="2.4"')}/>
<path d="M46 62 L18 46" {ln(O, 8)}/><path d="M46 62 L18 46" {ln("#FFCFA8", 4.5)}/>
<path d="M82 62 L110 44" {ln(O, 8)}/><path d="M82 62 L110 44" {ln("#FFCFA8", 4.5)}/>
<circle cx="16" cy="45" r="4.5" fill="#FFCFA8" {s('stroke-width="2.2"')}/><circle cx="112" cy="43" r="4.5" fill="#FFCFA8" {s('stroke-width="2.2"')}/>
<circle cx="64" cy="42" r="15" fill="#FFCFA8" {s()}/>
<path d="M49 40 Q50 24 64 24 Q78 24 79 40 Q74 32 64 31 Q54 32 49 40Z" fill="#7A4A2A" {s('stroke-width="2.4"')}/>
<path d="M51 26 L54 12 L60 22 L64 10 L68 22 L74 12 L77 26Z" fill="#FFD25E" {s('stroke-width="2.4"')}/>
<circle cx="64" cy="19" r="2" fill="#E8546A"/>
{eye(58, 42, 0.6)}{eye(70, 42, 0.6)}
<ellipse cx="64" cy="51" rx="4" ry="3.2" fill="#B2283C" {s('stroke-width="1.8"')}/>
<path d="M98 26 q4 -6 8 0 M104 18 q4 -6 8 0" fill="none" {s('stroke-width="2.2"')}/>
'''))

# 4. Академия талантов KRB (Белорусская) — табло «В ЭФИРЕ»
I["krb-yamskogo-polya"] = ("красное табло «В ЭФИРЕ» с мордашкой",
    "горит над детской студией звукозаписи, под ним поп-фильтр и мигающие ноты", bg("#2E2A4A", "#15122A", f'''
<path d="M30 20 L36 34 M98 20 L92 34" {ln("#8A86A8", 3)}/>
<rect x="18" y="32" width="92" height="38" rx="10" fill="#E8343E" {s()}/>
<rect x="24" y="38" width="80" height="26" rx="6" fill="#FF6A6A" opacity=".55"/>
<text x="64" y="57" text-anchor="middle" font-family="Arial" font-weight="bold" font-size="17" fill="#fff">В ЭФИРЕ</text>
{eye(40, 80, 0.8)}{eye(88, 80, 0.8)}
<path d="M56 82 Q64 90 72 82" fill="none" stroke="#FF8A8A" stroke-width="2.6" stroke-linecap="round"/>
<path d="M64 128 V100" {ln("#B9B6CF", 4)}/>
<circle cx="64" cy="100" r="12" fill="#3A3656" {s()}/><circle cx="64" cy="100" r="8" fill="none" stroke="#8A86A8" stroke-width="1.5" stroke-dasharray="2 2"/>
<path d="M76 100 Q86 106 82 116" fill="none" {ln("#B9B6CF", 2.4)}/>
{note(20, 104, 0.7, "#FFD25E")}{note(104, 108, 0.6, "#7FE0FF")}
{sparkle(14, 20, 4)}{sparkle(116, 84, 3.5)}
'''))

# 5. Балет в большом городе (Бауманская) — жёлтое такси-балерина
I["bcballet-baumanskaya"] = ("жёлтое московское такси-балерина в белой пачке",
    "встаёт на цыпочки колёс посреди ночной улицы с огнями", bg("#3B4A86", "#1E2552", f'''
<rect x="4" y="40" width="20" height="60" fill="#2A3366" {s('stroke-width="2"')}/><rect x="104" y="30" width="22" height="70" fill="#2A3366" {s('stroke-width="2"')}/>
<rect x="8" y="48" width="5" height="6" fill="#FFE07A"/><rect x="15" y="62" width="5" height="6" fill="#FFE07A"/><rect x="110" y="40" width="5" height="6" fill="#FFE07A"/><rect x="117" y="56" width="5" height="6" fill="#FFE07A"/><rect x="110" y="72" width="5" height="6" fill="#FFE07A"/>
<rect x="0" y="108" width="128" height="20" fill="#3A3A48"/><path d="M10 116 H28 M48 116 H66 M86 116 H104" stroke="#fff" stroke-width="2.4"/>
<path d="M26 74 Q30 54 46 50 L82 50 Q98 54 102 74 L104 84 H24Z" fill="#FFD23A" {s()}/>
<path d="M40 56 L46 52 H62 V68 H36Z M66 52 H80 L90 68 H66Z" fill="#BFE6FF" {s('stroke-width="2.4"')}/>
<rect x="54" y="40" width="20" height="9" rx="2" fill="#FFF6C4" {s('stroke-width="2.2"')}/>
<path d="M58 44.5 h12" stroke="{O}" stroke-width="1.6" stroke-dasharray="2 2"/>
{tutu(64, 86, 44, "#FFFFFF", "#F7B6CF")}
<path d="M44 94 L44 106 M84 94 L84 106" {s('stroke-width="4"')}/>
<ellipse cx="44" cy="108" rx="6" ry="4" fill="#2F2B3A" {s('stroke-width="2"')}/><ellipse cx="84" cy="108" rx="6" ry="4" fill="#2F2B3A" {s('stroke-width="2"')}/>
{eye(52, 74, 0.6)}{eye(76, 74, 0.6)}<path d="M60 78 Q64 81 68 78" fill="none" {s('stroke-width="1.8"')}/>
{sparkle(64, 18, 5, "#FFE07A")}{sparkle(36, 26, 3)}{sparkle(92, 22, 3)}
'''))

# 6. Ле Пти балерин (Белорусская) — тиара на пышной пачке
I["le-petit-ballerine-yamskogo"] = ("серебряная балетная тиара с жемчужинами и мордашкой",
    "сидит на пышной розовой пачке, как на облаке, а вокруг вьются атласные ленты пуант", bg("#FFF0F6", "#F6A8C8", f'''
<path d="M10 100 Q30 84 20 70 M118 98 Q98 84 110 66" fill="none" {ln("#F48FB8", 4)}/>
<ellipse cx="64" cy="96" rx="48" ry="16" fill="#FFB8D2" {s()}/>
<path d="M18 94 Q30 82 42 92 Q52 80 64 90 Q76 80 86 92 Q98 82 110 94" fill="none" stroke="#fff" stroke-width="3"/>
<ellipse cx="64" cy="84" rx="38" ry="10" fill="#FFCADD" {s()}/>
<path d="M28 80 L36 44 L48 64 L64 30 L80 64 L92 44 L100 80Z" fill="#E4E7F2" {s()}/>
<circle cx="36" cy="44" r="5" fill="#fff" {s('stroke-width="2.2"')}/><circle cx="92" cy="44" r="5" fill="#fff" {s('stroke-width="2.2"')}/>
<circle cx="64" cy="30" r="7" fill="#C9F0FF" {s('stroke-width="2.4"')}/><circle cx="62" cy="28" r="2" fill="#fff"/>
<circle cx="50" cy="74" r="2.8" fill="#fff" {s('stroke-width="1.6"')}/><circle cx="78" cy="74" r="2.8" fill="#fff" {s('stroke-width="1.6"')}/>
{face(64, 62, d=8, k=0.75)}
{sparkle(108, 30, 5)}{sparkle(20, 38, 4)}
'''))

# 7. Рисование (Новопеределкино) — шесть баночек гуаши поют хором
I["risovanie-novoperedelkinskaya"] = ("шесть баночек гуаши в ряд с крышками-шляпками",
    "поют хором, а кисточка-дирижёр машет над ними", bg("#FFFBEA", "#BDE3A6", f'''
<path d="M84 22 L50 44" {ln(O, 7)}/><path d="M84 22 L50 44" {ln("#E8B86A", 4)}/>
<path d="M50 44 L42 50 Q38 54 44 54 L52 48Z" fill="#3B6FD9" {s('stroke-width="2.4"')}/>
<rect x="80" y="18" width="10" height="7" rx="2" fill="#B8BCC8" transform="rotate(-33 85 21)" {s('stroke-width="2"')}/>
''' + "".join(
    f'<rect x="{x}" y="{y}" width="20" height="24" rx="4" fill="#F5F5F5" {s("stroke-width=\"2.6\"")}/>'
    f'<rect x="{x+2}" y="{y+8}" width="16" height="14" rx="2" fill="{c}"/>'
    f'<rect x="{x-2}" y="{y-6}" width="24" height="7" rx="3" fill="{c}" {s("stroke-width=\"2.4\"")}/>'
    f'<circle cx="{x+6}" cy="{y+12}" r="1.5" fill="{O}"/><circle cx="{x+14}" cy="{y+12}" r="1.5" fill="{O}"/>'
    f'<ellipse cx="{x+10}" cy="{y+17}" rx="2.4" ry="2" fill="{O}"/>'
    for x, y, c in [(10, 84, "#E8343E"), (32, 78, "#F2943A"), (54, 74, "#FFD23A"), (76, 78, "#4CC46A"), (98, 84, "#3B8FE8")]) + f'''
<rect x="56" y="104" width="20" height="18" rx="4" fill="#F5F5F5" {s('stroke-width="2.6"')}/><rect x="58" y="110" width="16" height="10" rx="2" fill="#9B5BE0"/>
{note(22, 50, 0.6)}{note(104, 52, 0.6)}{note(70, 52, 0.5, "#E8343E")}
'''))

# 8. Вдохновение (Ясенево) — глиняная кружка в кедах крутится на гончарном круге
I["vdokhnovenie-litovsky"] = ("расписная глиняная кружка-брейкер в красных кедах",
    "крутится на макушке на гончарном круге, а вокруг летают кисть и нота", bg("#E6FBFF", "#6FCFE0", f'''
<ellipse cx="64" cy="112" rx="40" ry="9" fill="#7D8590" {s()}/><ellipse cx="64" cy="108" rx="34" ry="7" fill="#A6ADB8" {s()}/>
<path d="M14 100 Q8 108 14 116 M114 100 Q120 108 114 116" fill="none" {s('stroke-width="2.4"')}/>
<path d="M44 102 Q40 70 46 56 H82 Q88 70 84 102Z" fill="#E59A62" {s()}/>
<ellipse cx="64" cy="102" rx="20" ry="5" fill="#C97A46" {s()}/>
<path d="M84 64 Q102 64 100 78 Q98 90 84 88" fill="none" {s('stroke-width="7"')}/><path d="M84 64 Q102 64 100 78 Q98 90 84 88" fill="none" stroke="#E59A62" stroke-width="3.6"/>
<path d="M48 70 Q56 64 64 70 Q72 76 80 70" fill="none" stroke="#3B6FD9" stroke-width="3"/>
<circle cx="56" cy="88" r="3" fill="#FFD23A"/><circle cx="72" cy="90" r="3" fill="#E8546A"/>
{eye(56, 80, 0.6)}{eye(72, 80, 0.6)}
<path d="M54 58 L42 30" {s('stroke-width="5"')}/><path d="M74 58 L86 30" {s('stroke-width="5"')}/>
<path d="M32 30 Q34 20 46 22 L50 30Z" fill="#E8343E" {s()}/><path d="M32 30 H50" stroke="#fff" stroke-width="2.4"/>
<path d="M78 30 L82 22 Q94 20 96 30Z" fill="#E8343E" {s()}/><path d="M78 30 H96" stroke="#fff" stroke-width="2.4"/>
<path d="M14 62 L30 48" {ln(O, 6)}/><path d="M14 62 L30 48" {ln("#E8C27A", 3)}/><path d="M30 48 Q36 42 34 50Z" fill="#9B5BE0" {s('stroke-width="2"')}/>
{note(104, 52, 0.75)}
'''))


if __name__ == "__main__":
    only = sys.argv[1:]
    for pid, (hero, scene, svgtxt) in I.items():
        if only and pid not in only:
            continue
        open(os.path.join(ROOT, "icons-src", pid + ".svg"), "w").write(svgtxt)
    print(len(I))
