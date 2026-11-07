"""Иконки робота fun (2026-11-07, день): 17 мест — Геликон-опера, «Щелкунчик» Касаткиной и Василёва, Малый театр,
«Русская песня», «Гжель», Музей ратной истории, музей Ферсмана, Электросталь, Химки, Коломна, Ногинск, «Лампа»,
Блинная гора. Каждая иконка придумана отдельно (правило абсолютной уникальности 07.11): свой герой, своя сцена,
своя компоновка и своя палитра фона. Сверено со всеми icons-catalog/sheet-*.png и icons-src/subjects.txt
(заняты: соловей, суфлёрская будка, кокошник, гжельская тарелка, каменный топорик, малыш на плечах у папы,
киноэкран, щелкунчик-солдатик, шлем и мечи, друза аметиста, керосиновая лампа).
Запуск: python3 tools/icons_fun_1107c.py [id ...]  (печатает строки для subjects.txt)"""
import os, sys
from draw_icons import s, eye, face, sparkle, O

W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=9, k=0.75, **kw: face(cx, cy, d=d, k=k, **kw)
sp = lambda *pts: "".join(sparkle(x, y, r) for x, y, r in pts)
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
GO = "#F2B632"


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


def note(x, y, c="#fff", k=1.0):
    return (f'<ellipse cx="{x}" cy="{y}" rx="{4.4*k:.1f}" ry="{3.4*k:.1f}" fill="{c}" {W(1.6)} transform="rotate(-20 {x} {y})"/>'
            f'<path d="M{x+4*k:.1f} {y-1} V{y-16*k:.1f} Q{x+9*k:.1f} {y-12*k:.1f} {x+10*k:.1f} {y-8*k:.1f}" fill="none" {W(1.8)}/>')


I = {}

# 1. Геликон-опера — лорнет в бархатной ложе
I["helikon-opera"] = ("#B0405A", "#4A1226",
    "золотой лорнет на длинной ручке", "выглядывает из бархатной театральной ложи и восхищённо смотрит на летящие ноты арии",
    f'<path d="M0 92 Q64 80 128 92 V128 H0Z" fill="#7E1E36" {s()}/>'
    f'<path d="M0 92 Q64 80 128 92" fill="none" stroke="{GO}" stroke-width="5"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="{GO}"/>' for x, y in [(16, 104), (40, 100), (64, 99), (88, 100), (112, 104)])
    + f'<path d="M30 30 Q24 60 34 92" fill="none" stroke="#E0607A" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M98 30 Q104 60 94 92" fill="none" stroke="#E0607A" stroke-width="6" stroke-linecap="round"/>'
    f'<rect x="60" y="70" width="8" height="34" rx="3" fill="{GO}" {W(2.4)}/>'
    f'<path d="M50 66 H78" stroke="{O}" stroke-width="2.4"/>'
    + "".join(f'<circle cx="{x}" cy="54" r="17" fill="#FFF4D8" {s()}/><circle cx="{x}" cy="54" r="12" fill="#E8F6FF" {W(2)}/>'
              f'<circle cx="{x}" cy="54" r="17" fill="none" stroke="{GO}" stroke-width="4"/>' for x in (46, 82))
    + f'<path d="M60 52 Q64 46 68 52" fill="none" stroke="{GO}" stroke-width="4"/>'
    + eye(46, 54, 0.9) + eye(82, 54, 0.9)
    + f'<ellipse cx="34" cy="68" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/><ellipse cx="94" cy="68" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/>'
    f'<ellipse cx="64" cy="80" rx="4" ry="5" fill="{O}"/>'
    + note(22, 32, "#FFD25E") + note(100, 22, "#fff", 0.8) + note(110, 48, "#FFD25E", 0.7)
    + sp((60, 20, 4), (16, 60, 3)))

# 2. «Щелкунчик» — орешек-балерина
I["kasatkina-ballet-nutcracker"] = ("#F4EEFF", "#9D86D9",
    "грецкий орешек в белой балетной пачке", "стоит на пуанте посреди сцены под кружащимся снегопадом",
    f'<path d="M6 108 Q64 96 122 108 V128 H6Z" fill="#E7DCC8" {s()}/>'
    + "".join(sparkle(x, y, r) for x, y, r in [(18, 34, 4), (108, 28, 5), (26, 74, 3), (104, 74, 4), (40, 18, 3), (88, 14, 3)])
    + f'<path d="M58 104 L62 84 M70 104 L66 84" stroke="#F7C8D8" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M66 84 L78 76" stroke="#F7C8D8" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M54 106 H62 M64 106 H72" stroke="{O}" stroke-width="3" stroke-linecap="round"/>'
    f'<path d="M26 80 Q64 62 102 80 Q64 94 26 80Z" fill="#fff" {s()}/>'
    f'<path d="M34 80 Q64 70 94 80" fill="none" stroke="#E6DEF7" stroke-width="3"/>'
    f'<path d="M64 26 Q86 26 88 50 Q90 74 64 78 Q38 74 40 50 Q42 26 64 26Z" fill="#C8955A" {s()}/>'
    f'<path d="M64 28 Q60 52 64 76" fill="none" {W(2)}/>'
    f'<path d="M50 36 Q46 48 52 60 M78 36 Q82 48 76 60" fill="none" stroke="#A9773F" stroke-width="2.4"/>'
    f'<path d="M42 50 Q24 40 22 26" fill="none" stroke="#C8955A" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M86 50 Q104 40 106 26" fill="none" stroke="#C8955A" stroke-width="5" stroke-linecap="round"/>'
    f'<circle cx="22" cy="24" r="3.5" fill="#C8955A" {W(1.8)}/><circle cx="106" cy="24" r="3.5" fill="#C8955A" {W(1.8)}/>'
    + f(64, 52, d=9, k=0.75)
    + f'<path d="M58 26 Q64 20 70 26" fill="#FF8FB8" {W(1.8)}/>')

# 3. Малый театр — гардеробный номерок («театр начинается с вешалки»)
I["maly-theatre"] = ("#E3F2DF", "#4F8A60",
    "латунный гардеробный номерок с цифрой 1", "висит на крючке театральной вешалки, а за ним — гардероб с шубами",
    f'<rect x="0" y="16" width="128" height="10" fill="#8C5A3A" {W(2.4)}/>'
    + "".join(f'<path d="M{x} 26 v10 q0 6 6 6" fill="none" {W(2.6)}/>' for x in (18, 104))
    + f'<path d="M6 46 Q18 40 30 46 V124 H6Z" fill="#B98AD6" {W(2.4)}/><path d="M98 46 Q110 40 122 46 V124 H98Z" fill="#7FB6E8" {W(2.4)}/>'
    f'<path d="M64 26 v14 q0 7 -6 7" fill="none" {W(3)}/>'
    f'<path d="M60 46 Q64 52 64 58" fill="none" stroke="#C0392B" stroke-width="2.4"/>'
    f'<path d="M64 56 L88 74 L88 108 Q88 118 78 118 H50 Q40 118 40 108 L40 74Z" fill="#E9B949" {s()}/>'
    f'<circle cx="64" cy="66" r="4" fill="#4F8A60" {W(2)}/>'
    f'<path d="M46 76 L64 62 L82 76" fill="none" stroke="#F8DA8A" stroke-width="2.4"/>'
    f'<path d="M60 90 L66 85 V112 M58 112 H72" fill="none" {W(3.4)}/>'
    + eye(52, 98, 0.75) + eye(78, 98, 0.75)
    + f'<ellipse cx="47" cy="106" rx="3.5" ry="2" fill="#FF7FA8" opacity=".7"/><ellipse cx="83" cy="106" rx="3.5" ry="2" fill="#FF7FA8" opacity=".7"/>'
    + sp((26, 34, 3), (110, 92, 3)))

# 4. «Русская песня» — хохломские ложки в пляс
I["russkaya-pesnya-theatre"] = ("#FFF0C8", "#E2553A",
    "пара расписных хохломских ложек", "лихо пляшут вприсядку и отбивают ритм, а вокруг летят ноты частушки",
    "".join(f'''<g transform="rotate({r} {cx} {cy})">
<path d="M{cx-4} {cy+6} L{cx-3} {cy+50} Q{cx} {cy+56} {cx+3} {cy+50} L{cx+4} {cy+6}Z" fill="#E7B23C" {s()}/>
<path d="M{cx-1} {cy+14} q4 6 0 12 q-4 6 0 12" fill="none" stroke="#C0392B" stroke-width="2.4"/>
<ellipse cx="{cx}" cy="{cy-10}" rx="17" ry="22" fill="#1E1A1A" {s()}/>
<ellipse cx="{cx}" cy="{cy-10}" rx="12" ry="16" fill="#C0392B"/>
<path d="M{cx-6} {cy-20} q6 -6 12 0 M{cx-8} {cy} q8 6 16 0" fill="none" stroke="{GO}" stroke-width="2.2"/>
{f(cx, cy-10, d=6, k=0.62)}</g>''' for cx, cy, r in [(42, 52, -22), (86, 52, 22)])
    + f'<path d="M58 30 L64 22 L70 30" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    + note(18, 30, "#fff", 0.8) + note(106, 22, "#FFD25E", 0.8) + note(64, 104, "#fff", 0.7)
    + sp((20, 96, 4), (110, 98, 4)))

# 5. Театр танца «Гжель» — плясунья в гжельской юбке
I["gzhel-dance-theatre"] = ("#F4F8FF", "#7C9EE0",
    "девочка-плясунья в широкой сине-белой юбке с гжельской розой", "кружится на носочке, юбка раскрылась колоколом, а платочек взлетел над головой",
    f'<ellipse cx="64" cy="116" rx="40" ry="6" fill="#5A78C0" opacity=".35"/>'
    f'<path d="M64 66 Q20 80 14 104 Q40 116 64 112 Q88 116 114 104 Q108 80 64 66Z" fill="#fff" {s()}/>'
    f'<path d="M20 102 Q30 92 38 104 Q48 94 56 106 Q64 96 72 106 Q80 94 90 104 Q98 92 108 102" fill="none" stroke="#2F5BC0" stroke-width="3"/>'
    f'<circle cx="64" cy="88" r="9" fill="#2F5BC0" {W(2)}/><path d="M58 88 Q64 80 70 88 Q64 96 58 88Z" fill="#fff"/>'
    f'<circle cx="64" cy="88" r="2.4" fill="#2F5BC0"/>'
    + "".join(f'<path d="M{x} 86 q6 -8 12 0" fill="none" stroke="#2F5BC0" stroke-width="2.4"/>' for x in (34, 82))
    + f'<path d="M64 112 L66 124" stroke="{O}" stroke-width="3" stroke-linecap="round"/>'
    f'<path d="M54 50 H74 L72 70 H56Z" fill="#2F5BC0" {s()}/>'
    f'<path d="M56 54 Q40 44 30 24" fill="none" stroke="#F5D2B5" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M72 54 Q86 50 96 40" fill="none" stroke="#F5D2B5" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M18 14 Q30 8 40 18 Q30 30 22 30Z" fill="#fff" {W(2.2)}/><circle cx="29" cy="20" r="3" fill="#2F5BC0"/>'
    f'<circle cx="64" cy="36" r="13" fill="#F5D2B5" {s()}/>'
    f'<path d="M51 34 Q52 20 64 21 Q76 20 77 34 Q70 26 64 28 Q58 26 51 34Z" fill="#B5652E" {W(2)}/>'
    f'<path d="M77 34 Q86 40 82 50" fill="none" stroke="#B5652E" stroke-width="4" stroke-linecap="round"/>'
    + f(64, 39, d=5, k=0.55))

# 6. Музей ратной истории — берестяная грамота
I["ratnaya-istoriya-museum"] = ("#F6FAEA", "#9DBB6A",
    "свиток берестяной грамоты с процарапанными буквами", "развернулся на берёзовом пеньке, а рядом стоит костяное писало, которым учатся писать как в Древней Руси",
    f'<path d="M24 92 H104 V122 H24Z" fill="#F4EFE4" {s()}/>'
    f'<path d="M24 98 h10 M44 106 h12 M76 100 h14 M94 112 h8 M30 114 h8" stroke="{O}" stroke-width="3" stroke-linecap="round"/>'
    f'<ellipse cx="64" cy="92" rx="40" ry="8" fill="#E9DDC2" {s()}/>'
    f'<ellipse cx="64" cy="92" rx="28" ry="5" fill="none" stroke="#C7B48C" stroke-width="2"/>'
    f'<path d="M22 30 Q64 20 106 30 L102 82 Q64 74 26 82Z" fill="#F2D7A4" {s()}/>'
    f'<path d="M22 30 q-8 4 -6 12 q2 6 8 4" fill="#E2BC80" {W(2.4)}/><path d="M106 30 q8 4 6 12 q-2 6 -8 4" fill="#E2BC80" {W(2.4)}/>'
    f'<path d="M34 40 l4 10 l4 -10 M48 40 v10 M48 45 h6 M58 40 l6 10 M64 40 l-6 10" fill="none" stroke="#7A4E2E" stroke-width="2.6" stroke-linecap="round"/>'
    + f(64, 62, d=10, k=0.8)
    + f'<g transform="rotate(25 104 70)"><rect x="100" y="44" width="7" height="40" rx="3" fill="#FFF8EC" {W(2.4)}/>'
    f'<path d="M100 84 L103.5 94 L107 84Z" fill="#FFF8EC" {W(2)}/><circle cx="103.5" cy="44" r="5" fill="#FFF8EC" {W(2)}/></g>'
    + sp((18, 18, 4), (40, 14, 3)))

# 7. Минералогический музей Ферсмана — срез агата
I["fersman-museum"] = ("#3E7F8C", "#123842",
    "яйцо агата, распиленное пополам, с радужными кольцами внутри", "две половинки лежат на бархатной подставке музейной витрины и любуются друг другом",
    f'<path d="M14 98 H114 L106 120 H22Z" fill="#7A2C4E" {s()}/>'
    f'<rect x="40" y="104" width="48" height="8" rx="2" fill="#F5F0E1" {W(2)}/>'
    + "".join(f'''<g transform="rotate({r} {cx} 66)">
<ellipse cx="{cx}" cy="66" rx="25" ry="31" fill="#8A7A6A" {s()}/>
<ellipse cx="{cx}" cy="66" rx="20" ry="26" fill="#F6E7FF"/>
<ellipse cx="{cx}" cy="66" rx="16" ry="21" fill="#B58FE6"/>
<ellipse cx="{cx}" cy="66" rx="12" ry="16" fill="#FFF3E0"/>
<ellipse cx="{cx}" cy="66" rx="9" ry="12" fill="#5FC6D8"/>
<ellipse cx="{cx}" cy="66" rx="5" ry="7" fill="#E7FBFF"/>
<ellipse cx="{cx}" cy="66" rx="25" ry="31" fill="none" {s()}/></g>''' for cx, r in [(38, -10), (90, 10)])
    + eye(32, 64, 0.65) + eye(44, 62, 0.65) + eye(84, 62, 0.65) + eye(96, 64, 0.65)
    + f'<path d="M34 72 Q39 76 43 71 M85 71 Q89 76 94 72" fill="none" {W(2)}/>'
    + f'<path d="M64 38 c-3 -6 -10 -4 -8 2 c1 4 8 8 8 8 c0 0 7 -4 8 -8 c2 -6 -5 -8 -8 -2Z" fill="#FF8FB8" {W(1.8)}/>'
    + sp((18, 26, 4), (110, 26, 5), (64, 18, 3)))

# 8. Киноцентр «Современник» (Электросталь) — ковш сталевара в 3D-очках
I["elektrostal-sovremennik"] = ("#3A2E5E", "#140E26",
    "малыш-ковш сталевара с огненной сталью внутри", "сидит в тёмном зале в красно-синих 3D-очках, а над ним светится луч проектора",
    f'<path d="M128 0 L40 56 L70 70Z" fill="#FFF3B0" opacity=".35"/>'
    f'<circle cx="122" cy="6" r="8" fill="#FFF3B0" {W(2)}/>'
    + "".join(f'<path d="M{x} 112 q12 -14 24 0 v16 h-24Z" fill="#5A3A7A" {W(2.2)}/>' for x in (2, 102))
    + f'<path d="M30 60 H98 L90 104 Q64 116 38 104Z" fill="#7C8696" {s()}/>'
    f'<path d="M30 60 Q64 72 98 60 Q64 50 30 60Z" fill="#FF8A2A" {s()}/>'
    f'<path d="M44 60 Q64 66 84 60" fill="none" stroke="#FFE066" stroke-width="3"/>'
    f'<path d="M98 66 Q118 66 118 82" fill="none" stroke="#7C8696" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M36 76 H92" stroke="{O}" stroke-width="2.6"/>'
    f'<rect x="40" y="78" width="21" height="13" rx="4" fill="#E8453C" {W(2.4)}/><rect x="67" y="78" width="21" height="13" rx="4" fill="#3E8FE8" {W(2.4)}/>'
    f'<path d="M61 83 H67" stroke="{O}" stroke-width="2.6"/>'
    f'<path d="M56 98 Q64 104 72 98" fill="none" {W(2.4)}/>'
    f'<ellipse cx="44" cy="97" rx="4" ry="2.2" fill="#FF7FA8" opacity=".7"/><ellipse cx="84" cy="97" rx="4" ry="2.2" fill="#FF7FA8" opacity=".7"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFB347"/>' for x, y, r in [(48, 44, 2.4), (62, 36, 3), (78, 42, 2.2), (70, 28, 1.8)]))

# 9. «Артишок» (Химки) — артишок-художник
I["khimki-artishok"] = ("#FFF2E8", "#EE9E7E",
    "зелёный артишок с листьями-чешуйками", "вешает на стену выставочного зала свою картину в золотой раме и поправляет её, встав на цыпочки",
    f'<rect x="0" y="104" width="128" height="24" fill="#D9B08C" {W(2.4)}/>'
    f'<rect x="58" y="16" width="56" height="44" rx="2" fill="{GO}" {s()}/>'
    f'<rect x="65" y="23" width="42" height="30" fill="#BFE6FF" {W(2)}/>'
    f'<path d="M65 53 L78 38 L88 48 L96 40 L107 53Z" fill="#7CD26E" {W(2)}/><circle cx="98" cy="30" r="4" fill="#FFD25E"/>'
    f'<path d="M86 16 L86 8" stroke="{O}" stroke-width="2.4"/><circle cx="86" cy="7" r="2.6" fill="{O}"/>'
    f'<path d="M40 104 L40 112 M54 104 L54 112" stroke="{O}" stroke-width="3.4" stroke-linecap="round"/>'
    f'<path d="M47 106 Q20 98 22 72 Q24 52 47 44 Q70 52 72 72 Q74 98 47 106Z" fill="#6DB36A" {s()}/>'
    + "".join(f'<path d="M{x} {y} q7 -10 14 0" fill="#8FCB76" {W(2)}/>' for x, y in [(26, 92), (40, 96), (54, 92), (32, 80), (48, 82), (36, 66), (50, 68)])
    + f'<path d="M47 44 Q42 32 48 24 Q54 32 47 44Z" fill="#9C7BC8" {W(2)}/>'
    + f'<g>{f(47, 74, d=7, k=0.6)}</g>'
    + f'<path d="M68 70 Q80 64 66 54" fill="none" stroke="#6DB36A" stroke-width="5" stroke-linecap="round"/>'
    + sp((18, 30, 4), (34, 14, 3)))

# 10. VR Party (Химки) — хлопушка в VR-шлеме
I["khimki-vr-party"] = ("#FFE0F6", "#C73E9F",
    "праздничная хлопушка в VR-шлеме", "выстреливает вверх фонтан конфетти и пиксельных звёздочек, как будто попала внутрь игры",
    "".join(f'<rect x="{x}" y="{y}" width="7" height="7" fill="{c}" {W(1.4)} transform="rotate({r} {x} {y})"/>' for x, y, c, r in
            [(24, 20, "#FFD25E", 10), (44, 10, "#5CE1E6", -12), (80, 12, "#7CD26E", 20), (100, 26, "#FFFFFF", 0), (60, 30, "#FF8A3D", 30), (34, 40, "#B49BFF", 0)])
    + "".join(f'<path d="M{x} {y} q4 -8 0 -16" fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round"/>' for x, y, c in [(70, 44, "#fff"), (52, 48, "#FFD25E"), (90, 48, "#5CE1E6")])
    + f'<path d="M40 56 L88 56 L76 120 L52 120Z" fill="#FF6FA8" {s()}/>'
    + "".join(f'<path d="M{a} {b} L{c} {d}" stroke="#FFD25E" stroke-width="4"/>' for a, b, c, d in [(44, 72, 84, 64), (47, 90, 81, 82), (50, 108, 78, 100)])
    + f'<ellipse cx="64" cy="56" rx="24" ry="6" fill="#FFC1DC" {s()}/>'
    f'<rect x="38" y="68" width="52" height="24" rx="10" fill="#2E2A44" {s()}/>'
    f'<rect x="43" y="73" width="42" height="14" rx="6" fill="#4FD8E8" opacity=".85"/>'
    f'<path d="M48 76 l4 4 M78 76 l-4 4" stroke="#fff" stroke-width="2"/>'
    f'<path d="M38 80 H32 M90 80 H96" stroke="{O}" stroke-width="3"/>'
    f'<path d="M58 100 Q64 106 70 100" fill="none" {W(2.4)}/>')

# 11. Усадьба Лажечниковых — Ледяной дом из романа
I["kolomna-lazhechnikov"] = ("#E6F6FF", "#5E98CF",
    "ледяной дворец с колоннами и сосульками", "стоит на снегу и светится изнутри тёплыми окошками, а с крыши свисают сосульки",
    f'<path d="M0 104 Q64 92 128 104 V128 H0Z" fill="#fff" {s()}/>'
    f'<path d="M28 50 L64 26 L100 50Z" fill="#CFEFFF" {s()}/>'
    f'<rect x="26" y="50" width="76" height="8" fill="#B8E2FA" {W(2.6)}/>'
    f'<rect x="30" y="58" width="68" height="44" fill="#DDF4FF" {s()}/>'
    + "".join(f'<rect x="{x}" y="58" width="8" height="44" fill="#BFE6FA" {W(2)}/>' for x in (32, 50, 70, 88))
    + "".join(f'<path d="M{x} 58 l3 {h} l3 -{h}Z" fill="#fff" {W(1.6)}/>' for x, h in [(38, 10), (58, 7), (64, 12), (78, 8)])
    + f'<path d="M56 102 V84 Q64 76 72 84 V102Z" fill="#FFD27A" {W(2.4)}/>'
    f'<rect x="40" y="80" width="8" height="10" rx="2" fill="#FFD27A" {W(1.8)}/><rect x="80" y="80" width="8" height="10" rx="2" fill="#FFD27A" {W(1.8)}/>'
    + f(64, 40, d=7, k=0.6)
    + sp((16, 30, 5), (110, 26, 4), (112, 70, 3), (14, 80, 3)))

# 12. Коломенский краеведческий музей — бивень мамонта
I["kolomna-kraeved"] = ("#FCF2DC", "#CFA36A",
    "изогнутый бивень мамонта", "лежит под стеклянным колпаком на музейной тумбе с табличкой и гордо улыбается посетителям",
    f'<path d="M30 92 H98 V124 H30Z" fill="#8A5A3A" {s()}/>'
    f'<rect x="50" y="102" width="28" height="10" rx="2" fill="#F5E6C4" {W(2)}/>'
    f'<path d="M22 92 V40 Q22 18 64 18 Q106 18 106 40 V92Z" fill="#E8F7FF" opacity=".55" {s()}/>'
    f'<path d="M30 36 Q34 26 44 24" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M30 86 Q34 50 70 40 Q96 34 98 56 Q90 46 72 52 Q46 60 44 86Z" fill="#FFF6E2" {s()}/>'
    f'<path d="M52 64 Q56 58 62 56 M68 48 Q74 46 80 46" fill="none" stroke="#E2CFA6" stroke-width="2.4"/>'
    f'<path d="M26 86 H102" stroke="{O}" stroke-width="3"/>'
    + f(64, 66, d=7, k=0.6)
    + sp((112, 22, 4), (16, 26, 3)))

# 13. Школа ремёсел (Коломна) — берестяной туесок
I["kolomna-shkola-remesel"] = ("#FFF9DE", "#E2B94C",
    "берестяной туесок с резным узором", "сидит на столе мастерской, а из-под крышки выглядывает глиняная птичка-свистулька и свистит",
    f'<rect x="0" y="104" width="128" height="24" fill="#B07A4C" {W(2.4)}/>'
    f'<path d="M30 52 H98 L94 108 H34Z" fill="#F0D6A0" {s()}/>'
    + "".join(f'<path d="M{x} 70 l6 -8 l6 8 l-6 8Z" fill="none" stroke="#9A6A3A" stroke-width="2.2"/>' for x in (40, 58, 76))
    + f'<path d="M34 96 H94" stroke="#9A6A3A" stroke-width="2.4"/>'
    + f(64, 86, d=12, k=0.62)
    + f'<path d="M24 52 Q64 40 104 52 Q64 58 24 52Z" fill="#E2BC80" {s()}/>'
    f'<path d="M58 44 Q64 34 70 44" fill="none" {W(3)}/>'
    f'<path d="M62 42 Q60 22 76 20 Q92 22 90 36 L100 34 L94 42 Q84 48 70 46Z" fill="#E8805A" {s()}/>'
    f'<path d="M68 30 q6 6 14 2" fill="none" stroke="#fff" stroke-width="2.4"/>'
    + eye(80, 27, 0.55)
    + f'<path d="M104 26 q6 -2 10 -8 M104 34 q8 0 12 -2" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>'
    + note(20, 30, "#fff", 0.75))

# 14. Парк Мира (Коломна) — качели-лодочка
I["kolomna-park-mira"] = ("#E9FFF6", "#57BE97",
    "красная качели-лодочка с узором на борту", "взлетела высоко на старинном аттракционе, а её флажок развевается в небе",
    f'<path d="M0 108 Q64 98 128 108 V128 H0Z" fill="#7CD26E" {s()}/>'
    f'<path d="M24 112 L64 16 L104 112" fill="none" stroke="#3F6FB8" stroke-width="6" stroke-linejoin="round"/>'
    f'<path d="M24 112 L64 16 L104 112" fill="none" {W(1.6)}/>'
    f'<circle cx="64" cy="16" r="5" fill="#FFD25E" {W(2)}/>'
    f'<path d="M64 16 L36 64 M64 16 L84 72" stroke="{O}" stroke-width="2.6"/>'
    f'<g transform="rotate(-24 60 72)"><path d="M26 64 H96 Q92 86 61 86 Q30 86 26 64Z" fill="#E8453C" {s()}/>'
    f'<path d="M32 70 H90" stroke="#FFD25E" stroke-width="3"/>'
    + f(61, 76, d=8, k=0.6, mouth=True)
    + f'<path d="M92 64 V44" stroke="{O}" stroke-width="2.4"/><path d="M92 44 L106 49 L92 54Z" fill="#FFD25E" {W(1.8)}/></g>'
    + "".join(f'<path d="M{x} {y} q6 -6 12 0 q6 -6 12 0" fill="#fff" {W(1.8)}/>' for x, y in [(14, 34), (92, 22)]))

# 15. «Почтовая станция Богородск» — верстовой столб
I["noginsk-pochtovaya-stantsiya"] = ("#FFF0DE", "#C9845E",
    "полосатый верстовой столб с табличкой", "стоит у заснеженного тракта и машет вслед почтовому колокольчику, который звенит на дуге",
    f'<path d="M0 98 Q64 86 128 98 V128 H0Z" fill="#fff" {s()}/>'
    f'<path d="M80 128 Q90 100 128 92" fill="none" stroke="#E7D3C0" stroke-width="10"/>'
    f'<rect x="42" y="30" width="22" height="78" fill="#fff" {s()}/>'
    + "".join(f'<path d="M42 {y} L64 {y-10} V{y-2} L42 {y+8}Z" fill="#1F1F2E"/>' for y in (44, 64, 84, 104))
    + f'<rect x="42" y="30" width="22" height="78" fill="none" {s()}/>'
    f'<path d="M38 30 L53 20 L68 30Z" fill="#7A4E2E" {s()}/>'
    f'<rect x="22" y="40" width="30" height="22" rx="3" fill="#F5E6C4" {s()}/>'
    + eye(31, 50, 0.6) + eye(43, 50, 0.6)
    + f'<path d="M33 56 Q37 59 41 56" fill="none" {W(2)}/>'
    f'<path d="M64 52 Q78 44 84 34" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M64 52 Q78 44 84 34" fill="none" {W(1.4)}/>'
    f'<path d="M86 46 Q102 26 118 46" fill="none" stroke="#C0392B" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M96 46 Q102 36 108 46 L110 56 H94Z" fill="{GO}" {s()}/><circle cx="102" cy="58" r="3" fill="{O}"/>'
    f'<path d="M88 60 l-4 4 M116 60 l4 4 M102 66 v5" stroke="{O}" stroke-width="2.2" stroke-linecap="round"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="#fff"/>' for x, y in [(14, 22), (30, 12), (96, 14), (114, 76), (20, 78)]))

# 16. Детский центр «Лампа» (Горки Ленинские) — зелёная настольная лампа
I["gorki-lampa"] = ("#6A5642", "#261B12",
    "настольная лампа с зелёным стеклянным абажуром", "освещает верстак, на котором маленький деревянный робот-самоделка машет ей рукой",
    f'<path d="M30 58 L8 120 H120 L98 58Z" fill="#FFE9A8" opacity=".35"/>'
    f'<rect x="0" y="104" width="128" height="24" fill="#B98552" {W(2.4)}/>'
    f'<path d="M14 104 Q14 96 30 96 Q46 96 46 104Z" fill="#C9A16A" {s()}/>'
    f'<rect x="27" y="48" width="6" height="48" fill="{GO}" {W(2.4)}/>'
    f'<path d="M6 54 Q8 30 46 26 Q68 26 70 40 Q72 54 52 58 Z" fill="#2E9E62" {s()}/>'
    f'<path d="M14 50 Q20 36 44 32" fill="none" stroke="#7FE0A8" stroke-width="3" stroke-linecap="round"/>'
    + f(40, 44, d=7, k=0.55)
    + f'<path d="M58 58 v8" stroke="{GO}" stroke-width="2.4"/><circle cx="58" cy="68" r="2.4" fill="{GO}"/>'
    f'<rect x="78" y="66" width="28" height="26" rx="3" fill="#E2B27A" {s()}/>'
    f'<rect x="82" y="46" width="20" height="18" rx="3" fill="#E2B27A" {s()}/>'
    f'<path d="M92 46 V38" stroke="{O}" stroke-width="2.4"/><circle cx="92" cy="36" r="3" fill="#FF6B6B" {W(1.6)}/>'
    + eye(87, 55, 0.5) + eye(97, 55, 0.5)
    + f'<path d="M89 60 H95" stroke="{O}" stroke-width="2"/>'
    f'<path d="M78 72 Q68 64 66 54" fill="none" stroke="#E2B27A" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M106 72 L112 84" stroke="#E2B27A" stroke-width="5" stroke-linecap="round"/>'
    f'<rect x="82" y="92" width="7" height="12" fill="#C99A62" {W(2)}/><rect x="95" y="92" width="7" height="12" fill="#C99A62" {W(2)}/>'
    + "".join(f'<circle cx="{x}" cy="78" r="2" fill="{O}"/>' for x in (86, 92, 98)))

# 17. Блинная гора (Сергиев Посад) — блинчик-подзорная труба
I["sp-blinnaya-gora"] = ("#FFF2E6", "#F2A48E",
    "румяный блинчик, свёрнутый трубочкой", "смотрит в себя, как в подзорную трубу, с вершины холма на золотые купола лавры вдали",
    f'<path d="M0 96 Q40 60 92 84 Q112 92 128 90 V128 H0Z" fill="#8CCB6A" {s()}/>'
    + "".join(f'<g><rect x="{x-6}" y="{y}" width="12" height="16" fill="#fff" {W(2)}/>'
              f'<path d="M{x-6} {y} Q{x-7} {y-9} {x} {y-14} Q{x+7} {y-9} {x+6} {y}Z" fill="{c}" {W(2)}/>'
              f'<path d="M{x} {y-14} v-6 M{x-3} {y-17} h6" stroke="{O}" stroke-width="1.6"/></g>'
              for x, y, c in [(94, 52, GO), (108, 58, "#5A8FE0"), (82, 60, GO)])
    + f'<g transform="rotate(-18 52 70)"><rect x="18" y="58" width="58" height="24" rx="12" fill="#F2B865" {s()}/>'
    f'<ellipse cx="76" cy="70" rx="7" ry="12" fill="#E3973F" {s()}/><ellipse cx="76" cy="70" rx="3.5" ry="7" fill="#9A4E1E"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="#D58A3A"/>' for x, y in [(28, 64), (44, 76), (60, 62), (36, 72)])
    + f'<path d="M18 70 Q12 62 18 58" fill="none" stroke="#C0392B" stroke-width="3"/>'
    + f(44, 68, d=7, k=0.6) + '</g>'
    + f'<path d="M34 98 L30 112 M54 92 L56 108" stroke="#F2B865" stroke-width="5" stroke-linecap="round"/>'
    + sp((20, 24, 4), (60, 20, 3)))


if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        a, b, hero, scene, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
