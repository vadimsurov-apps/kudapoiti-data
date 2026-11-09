"""Иконки робота fun (2026-11-09, 3-й проход по районам): 85 мест из tools/add_fun_1109d.py.
Каждая придумана и нарисована отдельно (правило абсолютной уникальности); сверено с листами icons-catalog и subjects.txt.
Запуск: python3 tools/icons_fun_1109d.py [id ...]  (печатает строки для subjects.txt)"""
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


def kid(cx, cy, k=1.0, hair="#6B3F23", skin="#FFD9B8"):
    r = 13 * k
    return (f'<circle cx="{cx}" cy="{cy}" r="{r:.1f}" fill="{skin}" {W(2.8)}/>'
            f'<path d="M{cx-r:.1f} {cy-2*k:.1f} Q{cx-r:.1f} {cy-r-3*k:.1f} {cx:.1f} {cy-r-2*k:.1f} '
            f'Q{cx+r:.1f} {cy-r-3*k:.1f} {cx+r:.1f} {cy-2*k:.1f} Q{cx+4*k:.1f} {cy-9*k:.1f} {cx-r:.1f} {cy-2*k:.1f}Z" '
            f'fill="{hair}" {W(2.4)}/>'
            + face(cx, cy + 2 * k, d=5 * k, k=0.5 * k))


I = {}

# ================= игровые комнаты =================
I["svetlyachok-narodny"] = ("#4A4F9A", "#1E2050",
    "улитка, у которой домик-ракушка светится, как фонарь",
    "ползёт вверх по красной горке игровой в вечернем полумраке",
    f'<path d="M6 120 L100 30 L118 40 L28 128Z" fill="#E8434A" {W(3)}/>'
    f'<path d="M16 118 L102 36" stroke="#FF8A8F" stroke-width="4" stroke-linecap="round"/>'
    f'<circle cx="70" cy="58" r="34" fill="#FFE36B" opacity=".25"/>'
    f'<path d="M30 96 Q28 84 44 82 L86 80 Q96 80 96 90 Q96 100 84 100 L40 102 Q30 102 30 96Z" fill="#B8E07A" {W(3)}/>'
    f'<circle cx="68" cy="60" r="24" fill="#FFE36B" {W(3.2)}/>'
    f'<path d="M68 60 m-4 0 a4 4 0 1 1 8 0 a9 9 0 1 1 -17 0 a14 14 0 1 1 27 2" fill="none" stroke="#F2A93B" stroke-width="3.4" stroke-linecap="round"/>'
    + sparkle(96, 38, 5, "#FFF6A8") + sparkle(42, 40, 4, "#FFF6A8") +
    f'<path d="M88 84 L94 66 M92 86 L104 72" {W(2.6)}/><circle cx="94" cy="65" r="3" fill="#FFE36B" {W(1.8)}/><circle cx="105" cy="71" r="3" fill="#FFE36B" {W(1.8)}/>'
    + f(84, 90, d=5, k=0.5))

I["parovozovo-sirenevy"] = ("#F6EEFF", "#A97FDB",
    "пышная гроздь сирени с глазками и двумя листочками-ручками",
    "съезжает с жёлтой детской горки, подняв листочки вверх",
    f'<path d="M14 40 L62 40 L112 100 L112 112 L94 112 L52 62 L14 62Z" fill="#FFD23F" {W(3)}/>'
    f'<path d="M58 46 L108 104" stroke="#FFF3B0" stroke-width="4" stroke-linecap="round"/>'
    f'<rect x="12" y="62" width="8" height="54" fill="#5AA9E6" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="9" fill="{c}" {W(2.2)}/>' for x, y, c in
              [(62, 30, "#C9A6F5"), (50, 40, "#B48AF0"), (74, 40, "#B48AF0"), (44, 54, "#9E6FE6"), (62, 50, "#C9A6F5"),
               (80, 54, "#9E6FE6"), (52, 66, "#B48AF0"), (72, 66, "#B48AF0"), (62, 78, "#9E6FE6")]) +
    f'<ellipse cx="62" cy="56" rx="15" ry="11" fill="#C9A6F5"/>' + f(62, 54, d=6, k=0.55) +
    f'<path d="M40 60 Q24 50 22 34 Q36 38 42 52Z" fill="#6FCF6A" {W(2.4)}/>'
    f'<path d="M84 60 Q100 48 98 32 Q86 38 82 52Z" fill="#6FCF6A" {W(2.4)}/>')

I["zushek-shchelkovsky"] = ("#FFEBDD", "#EE8A55",
    "горка в виде серого слона, хобот которого — скат",
    "малыш в жёлтой кофточке съезжает по хоботу, раскинув руки",
    f'<ellipse cx="54" cy="70" rx="38" ry="30" fill="#A9B6C9" {W(3.2)}/>'
    f'<path d="M30 92 v20 h12 v-16 M64 96 v16 h12 v-20" fill="#A9B6C9" {W(3)}/>'
    f'<ellipse cx="34" cy="58" rx="16" ry="20" fill="#C7D1E0" {W(3)}/>'
    f'<path d="M84 60 Q110 66 112 96 L112 112 L98 112 L98 98 Q96 80 80 78" fill="#A9B6C9" {W(3.2)}/>'
    f'<path d="M100 98 Q100 76 84 70" fill="none" stroke="#D6DEEA" stroke-width="4" stroke-linecap="round"/>'
    + f(66, 58, d=8, k=0.65) +
    kid(98, 66, k=0.75, hair="#7A4A22") +
    f'<path d="M90 76 Q98 72 106 76 L110 92 L88 92Z" fill="#FFD23F" {W(2.4)}/>'
    f'<path d="M90 80 L78 70 M106 80 L118 70" {W(2.8)}/>')

I["igrovoy-ugolok-medikov"] = ("#FFF4DE", "#F2B45A",
    "мягкий поролоновый модуль-треугольник в синем чехле",
    "малыш в шапочке с помпоном съезжает с него на попе и смеётся",
    f'<path d="M12 104 L108 104 L108 42 Q108 36 102 38 L16 96 Q10 100 12 104Z" fill="#4F86E8" {W(3.2)}/>'
    f'<path d="M26 98 L100 50" stroke="#8EB4FF" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M60 104 L60 72 M84 104 L84 56" stroke="#3566C2" stroke-width="3"/>'
    f'<rect x="8" y="104" width="112" height="12" rx="4" fill="#FF8C5A" {W(3)}/>'
    + f(84, 86, d=7, k=0.6) +
    kid(48, 52, k=0.8, hair="#E8C26A") +
    f'<path d="M37 46 Q48 32 59 46Z" fill="#E8303A" {W(2.2)}/><circle cx="48" cy="36" r="4" fill="#fff" {W(1.8)}/>'
    f'<path d="M40 62 Q48 58 56 62 L58 74 L38 76Z" fill="#7CD26E" {W(2.4)}/>'
    f'<path d="M40 70 L28 76 M56 66 L68 58" {W(2.8)}/>')

I["parovozovo-kavkazsky"] = ("#DDF6FF", "#4FA9E0",
    "голубой дельфин-качалка на толстой пружине",
    "девочка с косичками качается на нём верхом, держась за ручки",
    f'<ellipse cx="64" cy="114" rx="34" ry="7" fill="#7C8BA1" {W(2.8)}/>'
    + "".join(f'<ellipse cx="64" cy="{y}" rx="12" ry="4" fill="none" stroke="#C7CED8" stroke-width="5"/>' for y in (108, 100, 92)) +
    f'<path d="M16 66 Q30 44 64 46 Q96 48 108 62 Q100 64 96 72 Q86 84 60 84 Q30 84 16 66Z" fill="#5EC2F2" {W(3.2)}/>'
    f'<path d="M108 62 L120 52 L118 72Z" fill="#5EC2F2" {W(2.6)}/>'
    f'<path d="M58 46 Q62 30 74 34 Q70 40 70 48" fill="#5EC2F2" {W(2.6)}/>'
    f'<path d="M14 66 L6 64" {W(3)}/>' + eye(28, 62, 0.6) +
    f'<path d="M20 70 Q26 74 32 70" fill="none" {W(2.2)}/>'
    + kid(64, 26, k=0.7, hair="#8B4A2A") +
    f'<path d="M54 22 q-8 4 -6 12 M74 22 q8 4 6 12" fill="none" stroke="#8B4A2A" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M56 36 Q64 34 72 36 L74 50 L54 50Z" fill="#F58CB8" {W(2.4)}/>')

I["misty-park-gravitatsiya"] = ("#FFE3F1", "#DC5A9C",
    "игровой автомат-пинбол с наклонным полем и двумя флипперами",
    "серебряный шарик мечется между грибками-бамперами с улыбками",
    f'<path d="M30 14 L98 14 L110 116 L18 116Z" fill="#2F2A60" {W(3.2)}/>'
    f'<path d="M36 22 L92 22 L102 108 L26 108Z" fill="#5B4FC4" {W(2)}/>'
    f'<circle cx="48" cy="48" r="10" fill="#FFD23F" {W(2.6)}/><circle cx="80" cy="46" r="10" fill="#4CD3B0" {W(2.6)}/>'
    f'<circle cx="64" cy="70" r="10" fill="#FF6B6B" {W(2.6)}/>'
    + f(48, 48, d=3.5, k=0.32, blush=False) + f(80, 46, d=3.5, k=0.32, blush=False) + f(64, 70, d=3.5, k=0.32, blush=False) +
    f'<path d="M36 96 L56 104" stroke="#FF8C3A" stroke-width="7" stroke-linecap="round"/><path d="M92 96 L72 104" stroke="#FF8C3A" stroke-width="7" stroke-linecap="round"/>'
    f'<circle cx="72" cy="88" r="6" fill="#E6E9F0" {W(2.2)}/><circle cx="70" cy="86" r="2" fill="#fff"/>'
    f'<path d="M82 92 l6 4 M80 96 l4 6" stroke="#fff" stroke-width="2" stroke-linecap="round"/>' + sparkle(92, 64, 4, "#FFF6A8"))

I["kubiks-cdm"] = ("#FFF7DC", "#E3B24A",
    "огромные механические часы с открытыми шестерёнками",
    "из маленького окошка под циферблатом машет мальчик в синей кепке",
    "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#C9A35A" {W(2.4)}/>' for x, y, r in [(24, 32, 12), (104, 30, 14), (106, 74, 10)]) +
    f'<circle cx="64" cy="54" r="36" fill="#FFFDF4" {W(3.4)}/><circle cx="64" cy="54" r="30" fill="none" stroke="#D9B66A" stroke-width="2"/>'
    + "".join(f'<path d="M{64+26*__import__("math").sin(a*0.5236):.1f} {54-26*__import__("math").cos(a*0.5236):.1f} l0 0" {W(4)}/>' for a in range(12)) +
    f'<path d="M64 54 L64 32 M64 54 L80 60" {W(3.4)}/><circle cx="64" cy="54" r="3.5" fill="{O}"/>'
    + f(64, 70, d=6, k=0.45, mouth=False) +
    f'<rect x="44" y="92" width="40" height="30" rx="4" fill="#B0423A" {W(3)}/><rect x="52" y="98" width="24" height="20" rx="3" fill="#BFE8FF" {W(2.2)}/>'
    + kid(64, 110, k=0.55, hair="#3A2414") +
    f'<path d="M57 104 Q64 96 71 104Z" fill="#3D6FD8" {W(1.8)}/><path d="M74 112 L84 100" {W(2.6)}/>')

I["igrolend-cdm"] = ("#E8EEFF", "#7086DC",
    "серая жестяная заводная мышка с латунным ключиком в боку",
    "мчится по полу игровой, за ней вьются линии скорости и катится колёсико",
    f'<path d="M18 92 Q20 56 60 50 Q98 48 110 84 Q112 94 100 96 L28 98 Q18 98 18 92Z" fill="#B9C2D6" {W(3.2)}/>'
    f'<path d="M30 70 Q52 58 80 62" fill="none" stroke="#DCE2EE" stroke-width="4" stroke-linecap="round"/>'
    f'<circle cx="88" cy="56" r="11" fill="#F5B5C8" {W(2.8)}/><circle cx="88" cy="56" r="5" fill="#E88AA8"/>'
    f'<circle cx="106" cy="86" r="4" fill="#3B3355"/>' + eye(92, 74, 0.6) +
    f'<path d="M108 90 l10 -2 M108 92 l10 4" {W(1.6)}/>'
    f'<path d="M18 90 Q4 86 6 70 Q8 60 16 62" fill="none" {W(3)}/>'
    f'<rect x="54" y="30" width="6" height="22" fill="#E8B83A" {W(2.4)}/>'
    f'<path d="M57 30 q-12 -12 -16 -2 q4 8 16 2 q12 -12 16 -2 q-4 8 -16 2" fill="#FFD45E" {W(2.4)}/>'
    f'<circle cx="40" cy="100" r="7" fill="#7C8BA1" {W(2.4)}/><circle cx="84" cy="100" r="7" fill="#7C8BA1" {W(2.4)}/>'
    f'<path d="M8 106 h-6 M14 114 h-10 M24 120 h-8" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')

I["minimania-nagatinskaya"] = ("#EAFFEA", "#53BF74",
    "зелёный массажный мячик-ёжик с мягкими шипиками",
    "малыш в подгузнике катит его ладошками по коврику",
    f'<circle cx="70" cy="58" r="30" fill="#7EE07F" {W(3.2)}/>'
    + "".join(f'<circle cx="{70+30*__import__("math").cos(a*0.3927):.1f}" cy="{58+30*__import__("math").sin(a*0.3927):.1f}" r="5" fill="#7EE07F" {W(2)}/>' for a in range(16)) +
    f'<circle cx="70" cy="58" r="27" fill="#7EE07F"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#4FB85A"/>' for x, y in [(56, 44), (82, 42), (52, 66), (90, 64), (70, 78), (64, 40)]) +
    f(70, 56, d=8, k=0.7) +
    f'<rect x="8" y="108" width="112" height="14" rx="5" fill="#FFB86B" {W(2.6)}/>'
    + kid(30, 82, k=0.75, hair="#F2C14E") +
    f'<path d="M20 92 Q30 88 40 92 Q42 104 30 106 Q18 104 20 92Z" fill="#fff" {W(2.4)}/>'
    f'<path d="M38 88 L44 72" {W(3)}/>')

I["parovozovo-andropova"] = ("#DFFFF8", "#33B79C",
    "длинный надувной тоннель в красно-белую полоску",
    "с обоих концов выглядывают двое малышей и машут друг другу",
    f'<path d="M18 50 L110 50 L110 92 L18 92Z" fill="#fff" {W(3.2)}/>'
    + "".join(f'<rect x="{x}" y="50" width="12" height="42" fill="#E8434A"/>' for x in (26, 50, 74, 98)) +
    f'<path d="M18 50 L110 50 M18 92 L110 92" {W(3.2)}/>'
    f'<ellipse cx="18" cy="71" rx="10" ry="21" fill="#FFD23F" {W(3)}/><ellipse cx="110" cy="71" rx="10" ry="21" fill="#FFD23F" {W(3)}/>'
    f'<ellipse cx="18" cy="71" rx="5" ry="15" fill="#2F2A60"/><ellipse cx="110" cy="71" rx="5" ry="15" fill="#2F2A60"/>'
    + kid(24, 74, k=0.6, hair="#5A3A22") + kid(104, 74, k=0.6, hair="#E8B04A") +
    f'<path d="M30 82 L40 96 M98 82 L88 96" {W(2.6)}/>' + sparkle(64, 30, 6, "#FFF6A8") + sparkle(64, 108, 4, "#fff"))

I["apelsinka-pesochnitsa-nora"] = ("#FFF9E3", "#F5C542",
    "пластиковая формочка-пасочка в виде половинки апельсина с дольками",
    "только что слепила из кинетического песка рыжий куличик-апельсинчик и гордится",
    f'<ellipse cx="64" cy="108" rx="52" ry="12" fill="#E8C58A" {W(2.6)}/>'
    f'<path d="M14 70 A30 30 0 0 1 74 70Z" fill="#FF9A2E" {W(3.2)}/>'
    f'<path d="M20 70 A24 24 0 0 1 68 70Z" fill="#FFC56B"/>'
    + "".join(f'<path d="M44 70 L{44+24*__import__("math").cos(a):.1f} {70-24*__import__("math").sin(a):.1f}" stroke="#FF9A2E" stroke-width="2.4"/>' for a in (0.6, 1.2, 1.9, 2.5)) +
    f'<path d="M14 70 L74 70" {W(3.2)}/>' + f(44, 52, d=6, k=0.5) +
    f'<path d="M78 104 Q76 80 96 78 Q116 80 114 104Z" fill="#F4A64A" {W(3)}/>'
    f'<path d="M84 84 l4 18 M96 80 v24 M108 84 l-4 18" stroke="#D9822A" stroke-width="2"/>'
    + f(96, 92, d=5, k=0.42) +
    f'<path d="M96 78 q2 -8 8 -8" fill="none" stroke="#4FB85A" stroke-width="3" stroke-linecap="round"/>')

I["goodlandia-nora"] = ("#FFECEC", "#E85C5C",
    "клоунский гудок-клаксон с красной резиновой грушей и латунным раструбом",
    "гудит так громко, что из раструба вылетает фейерверк конфетти",
    f'<circle cx="34" cy="80" r="22" fill="#E8303A" {W(3.2)}/><ellipse cx="28" cy="72" rx="7" ry="5" fill="#FF8A8F"/>'
    + f(34, 82, d=7, k=0.6) +
    f'<rect x="52" y="72" width="22" height="14" rx="3" fill="#E8B83A" {W(2.8)}/>'
    f'<path d="M72 74 L112 46 L118 112 L72 86Z" fill="#FFD45E" {W(3.2)}/>'
    f'<ellipse cx="115" cy="79" rx="5" ry="33" fill="#F2B23A" {W(2.6)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="7" height="4" rx="1" fill="{c}" transform="rotate({r} {x} {y})"/>' for x, y, r, c in
              [(96, 18, 20, "#4F86E8"), (80, 28, -30, "#7CD26E"), (104, 34, 50, "#B48AF0"), (70, 14, 10, "#FF8C3A"), (88, 10, -50, "#E8303A")]) +
    f'<path d="M14 40 l8 8 M20 30 l4 10" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')

I["lucky-lama-kommunarka"] = ("#F4FFE4", "#A9CF5C",
    "белая кудрявая лама с золотой подковой-кулоном на шее",
    "высоко подпрыгивает над разноцветными шариками сухого бассейна",
    "".join(f'<circle cx="{x}" cy="{y}" r="8" fill="{c}" {W(2)}/>' for x, y, c in
            [(14, 112, "#E8434A"), (30, 116, "#4F86E8"), (46, 112, "#FFD23F"), (62, 118, "#7CD26E"), (78, 112, "#B48AF0"),
             (94, 116, "#FF8C3A"), (110, 112, "#4F86E8")]) +
    f'<path d="M40 86 L36 100 M52 88 L54 102 M78 88 L76 102 M90 84 L96 98" {W(3.2)}/>'
    f'<ellipse cx="64" cy="74" rx="32" ry="16" fill="#FFFCF5" {W(3.2)}/>'
    f'<path d="M80 66 L84 30 Q86 20 96 22 Q104 24 104 32 L98 36 L94 64Z" fill="#FFFCF5" {W(3.2)}/>'
    f'<path d="M88 22 L86 12 L92 18 M98 22 L100 12 L102 22" fill="#FFFCF5" {W(2.4)}/>' + eye(95, 30, 0.55) +
    f'<path d="M98 37 q-3 2 -6 0" fill="none" {W(1.8)}/>'
    f'<path d="M80 48 Q88 54 96 48" fill="none" stroke="#E8434A" stroke-width="2.4"/>'
    f'<path d="M84 54 a6 6 0 1 0 8 0" fill="none" stroke="#E8B83A" stroke-width="4" stroke-linecap="round"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="#FFFCF5"/>' for x, y in [(44, 66), (56, 62), (68, 64)]) +
    f'<path d="M30 100 l-6 6 M98 96 l6 6" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>')

I["chasiki-60-oktyabrya"] = ("#E8F1FF", "#5684DC",
    "большой круглый циферблат с цифрами-точками",
    "мальчик съезжает по длинной минутной стрелке, как по горке",
    f'<circle cx="64" cy="64" r="48" fill="#FFFDF2" {W(3.4)}/>'
    + "".join(f'<circle cx="{64+40*__import__("math").sin(a*0.5236):.1f}" cy="{64-40*__import__("math").cos(a*0.5236):.1f}" r="3.4" fill="{["#E8434A","#4F86E8","#FFD23F","#7CD26E"][a%4]}"/>' for a in range(12)) +
    f'<path d="M64 64 L96 30" stroke="#E8434A" stroke-width="9" stroke-linecap="round"/><path d="M64 64 L96 30" fill="none" {W(1.6)}/>'
    f'<path d="M64 64 L46 84" stroke="#2F2A60" stroke-width="7" stroke-linecap="round"/>'
    f'<circle cx="64" cy="64" r="6" fill="#FFD23F" {W(2.6)}/>'
    + kid(80, 40, k=0.6, hair="#5A3A22") +
    f'<path d="M84 48 L92 54 M74 48 L68 54" {W(2.6)}/>' + f(56, 92, d=5, k=0.42))

I["syurpriz-balashikha"] = ("#FDEFFF", "#C77FE0",
    "пластиковая капсула из игрушечного автомата — половинка красная, половинка прозрачная",
    "раскрылась, и из неё выглядывает крошечный зелёный динозаврик",
    f'<path d="M24 74 A40 40 0 0 0 104 74Z" fill="#E8303A" {W(3.2)}/>'
    f'<path d="M30 80 Q40 102 60 106" fill="none" stroke="#FF8A8F" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M30 60 A36 36 0 0 1 98 42" fill="#D6F2FF" opacity=".7" {W(3)} transform="rotate(-24 30 60)"/>'
    f'<path d="M48 74 Q46 50 64 46 Q82 48 82 64 L80 74Z" fill="#7CD26E" {W(3)}/>'
    f'<path d="M60 46 l-4 -8 6 4 4 -8 4 8 6 -4 -4 10" fill="#4FB85A" {W(2)}/>' + f(66, 60, d=6, k=0.55) +
    f'<path d="M24 74 L104 74" {W(3.2)}/>' + sparkle(100, 22, 6, "#fff") + sparkle(22, 38, 4, "#FFF6A8"))

I["solnechny-gorod-khimki"] = ("#FFFBE3", "#FFC22E",
    "круглое карманное зеркальце в розовой оправе",
    "пускает солнечного зайчика — светлое пятно-зайчик прыгает по стене игровой",
    f'<rect x="0" y="0" width="128" height="70" fill="#FFE9A8"/>'
    f'<path d="M0 70 H128" {W(2.4)}/>'
    f'<path d="M40 100 L84 30" stroke="#FFF7CF" stroke-width="16" stroke-linecap="round" opacity=".8"/>'
    f'<ellipse cx="88" cy="30" rx="16" ry="12" fill="#FFFDF0" opacity=".95"/>'
    f'<path d="M80 22 q-2 -12 4 -12 q2 6 0 12 M92 20 q2 -12 8 -10 q0 6 -4 12" fill="#FFFDF0"/>'
    f'<circle cx="84" cy="28" r="1.6" fill="#E8B83A"/><circle cx="92" cy="28" r="1.6" fill="#E8B83A"/>'
    f'<circle cx="38" cy="98" r="22" fill="#F58CB8" {W(3.2)}/><circle cx="38" cy="98" r="16" fill="#E6F6FF" {W(2.4)}/>'
    f'<path d="M30 92 l8 -6" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    f'<path d="M52 114 L70 128" stroke="#F58CB8" stroke-width="9" stroke-linecap="round"/>' + f(38, 100, d=5, k=0.45))

I["igralife-pravoberezhnaya"] = ("#ECE6FF", "#7C60D8",
    "игровой автомат-толкатель монет со стеклянным колпаком",
    "золотые жетоны с улыбками сыплются с полочки прямо в лоток",
    f'<rect x="24" y="14" width="80" height="104" rx="10" fill="#E8434A" {W(3.2)}/>'
    f'<rect x="32" y="24" width="64" height="56" rx="6" fill="#BFE8FF" {W(2.6)}/>'
    f'<rect x="36" y="56" width="56" height="10" fill="#7C8BA1" {W(2)}/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="7" ry="3.4" fill="#FFD23F" {W(1.8)}/>' for x, y in [(44, 54), (58, 52), (72, 54), (86, 53), (50, 48), (66, 46)]) +
    f'<rect x="38" y="90" width="52" height="18" rx="4" fill="#2F2A60" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="8" fill="#FFD23F" {W(2.4)}/>' for x, y in [(52, 100), (74, 104)]) +
    f(52, 99, d=3, k=0.3, blush=False) + f(74, 103, d=3, k=0.3, blush=False) +
    f'<circle cx="64" cy="84" r="7" fill="#FFD23F" {W(2.2)}/>' + sparkle(108, 30, 5, "#FFF6A8") + sparkle(18, 70, 4, "#fff"))

I["maksiboom-mega-khimki"] = ("#FFEEDB", "#E3702E",
    "аттракцион-силомер — высокий столб со шкалой и звонком на макушке",
    "девочка лупит огромной киянкой по наковальне, шайба взлетает до звонка: БУМ",
    f'<rect x="76" y="20" width="18" height="90" rx="4" fill="#fff" {W(3)}/>'
    + "".join(f'<rect x="79" y="{y}" width="12" height="8" fill="{c}"/>' for y, c in [(94, "#7CD26E"), (80, "#FFD23F"), (66, "#FF8C3A"), (52, "#E8434A"), (38, "#B48AF0")]) +
    f'<circle cx="85" cy="16" r="9" fill="#FFD23F" {W(2.8)}/><path d="M70 10 l-6 -4 M100 10 l6 -4 M85 4 v-4" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>'
    f'<rect x="78" y="26" width="14" height="8" rx="3" fill="#E8434A" {W(2)}/>'
    f'<rect x="64" y="108" width="42" height="12" rx="3" fill="#7C8BA1" {W(2.6)}/>'
    + kid(36, 64, k=0.8, hair="#7A4A22") +
    f'<path d="M26 76 Q36 72 46 76 L50 104 L22 104Z" fill="#45A8F0" {W(2.6)}/>'
    f'<path d="M44 78 L62 96" {W(3.4)}/><rect x="52" y="90" width="26" height="18" rx="4" fill="#C98B4A" {W(2.6)}/>'
    f'<path d="M48 40 l4 -8 M58 46 l8 -4" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')

I["star-lab-mega-khimki"] = ("#38336E", "#15123A",
    "ночник-черепаха с панцирем из звёздочек-дырочек",
    "проецирует на тёмный потолок игровой целое звёздное небо",
    "".join(sparkle(x, y, r, c) for x, y, r, c in [(20, 30, 4, "#FFF6A8"), (40, 16, 3, "#BFE8FF"), (64, 24, 5, "#FFF6A8"), (90, 14, 3, "#fff"),
                                                    (108, 34, 4, "#BFE8FF"), (30, 50, 3, "#fff"), (100, 56, 3, "#FFF6A8")]) +
    f'<path d="M46 80 L28 40 M64 76 L64 34 M82 80 L100 42" stroke="#FFE98A" stroke-width="10" opacity=".18" stroke-linecap="round"/>'
    f'<ellipse cx="64" cy="112" rx="46" ry="8" fill="#2A2560"/>'
    f'<path d="M30 104 Q30 70 64 70 Q98 70 98 104Z" fill="#4CC3A0" {W(3.2)}/>'
    + "".join(sparkle(x, y, 4, "#FFF6A8") for x, y in [(48, 86), (64, 80), (80, 86), (56, 96), (72, 96)]) +
    f'<circle cx="108" cy="96" r="11" fill="#8BE0C4" {W(3)}/>' + f(108, 95, d=4, k=0.4) +
    f'<path d="M36 104 v8 M88 104 v8" {W(5)}/>')

I["igray-oblaka"] = ("#E0FAFF", "#2FAFC4",
    "райская птица с длинным хвостом-веером из голубых и золотых перьев",
    "качается на подвесных гимнастических кольцах в игровой",
    f'<path d="M40 0 L40 30 M88 0 L88 30" {W(3)}/>'
    f'<circle cx="40" cy="38" r="9" fill="none" stroke="#FF8C3A" stroke-width="5"/><circle cx="88" cy="38" r="9" fill="none" stroke="#FF8C3A" stroke-width="5"/>'
    f'<path d="M58 74 Q40 100 22 120 M64 78 Q60 104 54 124 M70 76 Q84 100 102 118" stroke="#3B6FE0" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M58 74 Q40 100 22 120 M64 78 Q60 104 54 124 M70 76 Q84 100 102 118" stroke="#FFD23F" stroke-width="3" stroke-linecap="round"/>'
    f'<ellipse cx="64" cy="60" rx="18" ry="20" fill="#E8434A" {W(3.2)}/>'
    f'<path d="M48 50 Q40 40 42 34 M80 50 Q88 40 86 34" fill="none" {W(3.2)}/>'
    f'<path d="M58 40 q-2 -10 4 -12 q2 6 2 12 M66 40 q2 -10 8 -10 q-2 6 -4 12" fill="#FFD23F" {W(2)}/>'
    + f(64, 56, d=6, k=0.55) + f'<path d="M60 64 L64 70 L68 64Z" fill="#FFB13B" {W(1.8)}/>')

I["time-kids-oblaka"] = ("#F0FFF2", "#7FCB97",
    "кухонный таймер-помидор с зелёным хвостиком и шкалой",
    "звенит и подпрыгивает — время игры началось, вокруг разлетаются нотки",
    f'<ellipse cx="64" cy="114" rx="34" ry="6" fill="#5BAA76" opacity=".6"/>'
    f'<circle cx="64" cy="70" r="38" fill="#F2453A" {W(3.4)}/>'
    f'<path d="M34 84 Q64 96 94 84" fill="none" stroke="#FFD9D4" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M64 90 l-4 -8 h8Z" fill="{O}"/>' 
    f'<path d="M64 34 l-12 -8 8 0 4 -10 4 10 8 0Z" fill="#4FB85A" {W(2.4)}/>'
    f'<ellipse cx="48" cy="52" rx="7" ry="4" fill="#FF9A90"/>' + f(64, 56, d=8, k=0.65) +
    f'<path d="M14 40 l8 4 M18 26 l8 8 M112 40 l-8 4 M108 26 l-8 8" stroke="#FFD23F" stroke-width="3.4" stroke-linecap="round"/>'
    f'<path d="M104 14 v10 q-4 -2 -6 2 q2 4 6 0" fill="none" {W(2.2)}/>')

# ================= квесты =================
I["fort-boyard-varshavka"] = ("#E3F2FF", "#3E7CC8",
    "верёвочная лестница с деревянными перекладинами, свисающая с крепостной стены",
    "мальчик в оранжевой футболке карабкается по ней над бирюзовой водой",
    f'<rect x="0" y="0" width="34" height="128" fill="#C9B48A"/>'
    + "".join(f'<path d="M0 {y} H34 M{x} {y} v16" stroke="#9C8458" stroke-width="2"/>' for y, x in [(16, 18), (32, 8), (48, 22), (64, 12), (80, 20)]) +
    f'<path d="M34 0 V128" {W(3)}/>'
    f'<path d="M0 100 Q32 92 64 100 Q96 108 128 100 V128 H0Z" fill="#3EC6C0" {W(2.6)}/>'
    f'<path d="M54 0 Q50 60 58 104 M86 0 Q84 60 90 104" fill="none" stroke="#B07A3C" stroke-width="4"/>'
    + "".join(f'<path d="M{53-y*0.02:.0f} {y} L{86-y*0.0:.0f} {y+2}" stroke="#D9A066" stroke-width="7" stroke-linecap="round"/><path d="M{53-y*0.02:.0f} {y} L86 {y+2}" fill="none" {W(1.4)}/>' for y in (16, 36, 56, 76, 94)) +
    kid(70, 50, k=0.85, hair="#3A2414") +
    f'<path d="M60 62 Q70 58 80 62 L82 82 L58 82Z" fill="#FF8C3A" {W(2.6)}/>'
    f'<path d="M60 64 L54 56 M80 64 L86 56 M64 82 L58 96 M76 82 L84 96" {W(3)}/>')

I["fort-boyard-veshnyakovskaya"] = ("#DCE3EE", "#6E7FA0",
    "горящий факел в железном держателе на каменной стене",
    "освещает потайную дверцу с золотой замочной скважиной",
    "".join(f'<rect x="{x}" y="{y}" width="30" height="16" rx="2" fill="#B9C3D6" {W(1.6)}/>' for y in range(0, 128, 16) for x in range(-((y // 16) % 2) * 15, 128, 30)) +
    f'<circle cx="38" cy="38" r="30" fill="#FFC94A" opacity=".35"/>'
    f'<path d="M30 52 L34 80 L42 80 L46 52Z" fill="#8B5A2B" {W(2.8)}/>'
    f'<path d="M26 52 H50" {W(3)}/><path d="M24 50 Q38 58 52 50" fill="#7C8BA1" {W(2.6)}/>'
    f'<path d="M38 48 Q22 34 32 16 Q36 26 40 22 Q42 10 50 6 Q48 20 54 30 Q56 42 38 48Z" fill="#FF8C2E" {W(2.8)}/>'
    f'<path d="M38 44 Q30 36 36 26 Q40 32 44 30 Q48 38 38 44Z" fill="#FFE36B"/>' + f(39, 36, d=4, k=0.38) +
    f'<path d="M70 120 V64 Q70 46 90 46 Q110 46 110 64 V120Z" fill="#8B5A2B" {W(3.2)}/>'
    f'<path d="M80 120 V68 M90 120 V60 M100 120 V68" stroke="#6E431D" stroke-width="2.4"/>'
    f'<circle cx="100" cy="88" r="5" fill="#FFD23F" {W(2)}/><path d="M100 92 v6" stroke="#FFD23F" stroke-width="3"/>')

I["fort-boyard-balashikha"] = ("#E6F7D9", "#6DB34F",
    "толстый канат с морским узлом посередине",
    "двое детей в красной и синей футболках тянут его в разные стороны — перетягивание",
    f'<path d="M14 66 Q40 60 52 66 M76 66 Q90 60 114 66" fill="none" stroke="#C99A55" stroke-width="10" stroke-linecap="round"/>'
    f'<path d="M14 66 Q40 60 52 66 M76 66 Q90 60 114 66" fill="none" stroke="#E8C88A" stroke-width="4" stroke-dasharray="4 5" stroke-linecap="round"/>'
    f'<circle cx="64" cy="66" r="15" fill="#E8C88A" {W(3)}/><path d="M54 58 Q64 74 74 58 M54 74 Q64 58 74 74" fill="none" stroke="#B07A3C" stroke-width="3"/>'
    + f(64, 64, d=5, k=0.45) +
    kid(22, 44, k=0.75, hair="#5A3A22") + kid(106, 44, k=0.75, hair="#E8B04A") +
    f'<path d="M12 54 Q22 50 32 54 L34 76 L12 78Z" fill="#E8434A" {W(2.4)}/><path d="M96 54 Q106 50 116 54 L118 78 L94 76Z" fill="#4F86E8" {W(2.4)}/>'
    f'<path d="M16 78 L6 98 M30 78 L36 98 M100 78 L92 98 M112 78 L122 98" {W(3)}/>'
    f'<rect x="54" y="96" width="20" height="14" fill="#fff" {W(2)}/><path d="M64 96 V118" {W(2.4)}/>')

I["hide-dark-kolomenskaya"] = ("#2C5C38", "#0A1D10",
    "очки ночного видения с двумя светящимися зелёными трубками",
    "в их луче видно девочку, спрятавшуюся за ящиком в полной темноте",
    f'<path d="M60 70 L128 30 L128 128 L60 90Z" fill="#7CFF9A" opacity=".25"/>'
    f'<rect x="92" y="78" width="30" height="30" fill="#2E7A44" {W(2.4)}/>'
    + kid(100, 72, k=0.7, hair="#14381F", skin="#A6F2B6") +
    f'<path d="M88 70 L96 60" stroke="#A6F2B6" stroke-width="3" stroke-linecap="round"/>'
    f'<rect x="14" y="52" width="48" height="30" rx="10" fill="#3B4A40" {W(3.2)}/>'
    f'<rect x="20" y="40" width="14" height="22" rx="4" fill="#556B5C" {W(2.6)}/><rect x="40" y="40" width="14" height="22" rx="4" fill="#556B5C" {W(2.6)}/>'
    f'<circle cx="27" cy="40" r="8" fill="#7CFF9A" {W(2.6)}/><circle cx="47" cy="40" r="8" fill="#7CFF9A" {W(2.6)}/>'
    f'<circle cx="25" cy="38" r="2.4" fill="#fff"/><circle cx="45" cy="38" r="2.4" fill="#fff"/>'
    f'<path d="M14 66 Q2 66 4 90" fill="none" {W(4)}/>' + f(38, 70, d=7, k=0.5))

I["pryatki-vauli-dnepropetrovskaya"] = ("#FFF1E2", "#EE9E55",
    "длинная бархатная штора-занавеска с кисточками и глазками",
    "из-под неё торчат ноги в полосатых носках — кто-то плохо спрятался",
    f'<rect x="10" y="10" width="108" height="8" rx="4" fill="#C98B4A" {W(2.6)}/>'
    f'<path d="M20 18 Q16 60 22 100 L106 100 Q112 60 108 18Z" fill="#6E4BC8" {W(3.2)}/>'
    + "".join(f'<path d="M{x} 20 Q{x-3} 60 {x} 98" fill="none" stroke="#8C6BE0" stroke-width="5"/>' for x in (38, 56, 74, 92)) +
    f(64, 46, d=9, k=0.7) +
    f'<rect x="40" y="98" width="12" height="16" fill="#fff" {W(2.4)}/><rect x="76" y="98" width="12" height="16" fill="#fff" {W(2.4)}/>'
    f'<path d="M40 104 h12 M40 110 h12 M76 104 h12 M76 110 h12" stroke="#E8434A" stroke-width="3"/>'
    f'<path d="M36 114 h18 q4 0 4 4 h-22Z M74 114 h18 q4 0 4 4 h-22Z" fill="#E8434A" {W(2.4)}/>'
    f'<circle cx="22" cy="68" r="4" fill="#FFD23F" {W(1.8)}/><path d="M22 72 v8" stroke="#FFD23F" stroke-width="3"/>')

I["kvestern-lobanova"] = ("#FCEBD0", "#CC8640",
    "рыжий ковбойский сапог с вышитым узором и серебряной шпорой-звёздочкой",
    "шпора крутится, а сапог шагает по пыльной дороге мимо кактусов",
    f'<path d="M0 104 Q64 96 128 104 V128 H0Z" fill="#E8C58A" {W(2.4)}/>'
    f'<path d="M100 104 V66 Q100 58 108 58 Q114 58 114 66 V104 M114 80 h8 v-12" fill="#6FBF6A" {W(2.6)}/>'
    f'<path d="M40 14 L80 14 L80 72 Q84 82 98 86 Q108 90 104 104 L28 104 Q22 104 24 92 L40 80Z" fill="#C46A2E" {W(3.4)}/>'
    f'<path d="M38 14 h44 v10 h-44Z" fill="#9C4E1C" {W(2.6)}/>'
    f'<path d="M52 34 q8 10 0 20 q-8 -10 0 -20 M66 34 q8 10 0 20" fill="none" stroke="#FFD45E" stroke-width="2.6"/>'
    + f(58, 70, d=7, k=0.55) +
    f'<path d="M24 96 L12 94" {W(3)}/>'
    f'<path d="M10 94 l3 -8 3 8 8 0 -6 5 3 8 -8 -5 -8 5 3 -8 -6 -5Z" fill="#DDE3EE" {W(2)}/>'
    f'<path d="M30 112 q6 -4 10 0 M60 116 q6 -4 10 0" fill="none" stroke="#C99A55" stroke-width="2.6" stroke-linecap="round"/>')

I["semya-grimm-pervomayskaya"] = ("#E2FAF2", "#55BFA0",
    "золотой гусь из сказки братьев Гримм",
    "важно шагает, а за ним цепочкой прилипли мальчик и девочка",
    f'<path d="M46 90 Q38 66 62 62 L78 62 Q84 56 80 44 Q74 30 82 18 Q92 10 100 18 Q104 26 96 30 Q90 36 94 48 Q102 64 98 80 Q92 100 70 100 Q54 100 46 90Z" fill="#F7B81E" {W(3.2)}/>'
    f'<path d="M100 18 L116 24 L100 28Z" fill="#FF7A1E" {W(2.4)}/>' + eye(92, 20, 0.5) +
    f'<path d="M84 8 l2 -8 4 6 4 -6 4 6 2 -6 2 8Z" fill="#FFE36B" {W(1.8)}/>'
    f'<path d="M58 80 Q72 70 88 80" fill="none" stroke="#D99510" stroke-width="3"/>'
    f'<path d="M66 100 v12 l-6 4 M80 100 v12 l6 4" fill="none" stroke="#FF7A1E" stroke-width="4" stroke-linecap="round"/>'
    + sparkle(104, 58, 5, "#fff") +
    kid(36, 72, k=0.7, hair="#5A3A22") + kid(14, 82, k=0.6, hair="#E8B04A") +
    f'<path d="M36 82 L30 104 L42 104Z" fill="#4F86E8" {W(2.2)}/><path d="M14 90 L8 110 L20 110Z" fill="#F58CB8" {W(2.2)}/>'
    f'<path d="M44 80 L50 82 M22 88 L30 86" {W(2.6)}/>')

I["endorfin-krzhizhanovskogo"] = ("#5E4392", "#24113F",
    "жёлтый карманный фонарик с кнопкой",
    "в темноте квест-комнаты высвечивает на стене большой знак вопроса",
    f'<path d="M40 82 L96 30 L112 64 Z" fill="#FFF3A6" opacity=".35"/>'
    f'<ellipse cx="102" cy="46" rx="18" ry="22" fill="#FFF3A6" opacity=".5"/>'
    f'<path d="M96 36 Q96 28 104 28 Q112 28 112 36 Q112 42 104 46 V52" fill="none" stroke="#5E4392" stroke-width="5" stroke-linecap="round"/>'
    f'<circle cx="104" cy="60" r="3" fill="#5E4392"/>'
    f'<path d="M14 104 L44 74 L58 88 L28 118Z" fill="#FFD23F" {W(3.2)}/>'
    f'<path d="M44 74 L52 66 L66 80 L58 88Z" fill="#E8A21A" {W(3)}/><path d="M52 66 L66 80" stroke="#FFF7C2" stroke-width="3"/>'
    f'<circle cx="30" cy="96" r="4" fill="#E8434A" {W(1.8)}/>' + f(38, 98, d=5, k=0.42))

I["atmoquest-novocheremushkinskaya"] = ("#D8F5C8", "#3E9E52",
    "ярко-синяя лягушка-древолаз в чёрных крапинках",
    "сидит на огромном листе в джунглях и держит обрывок карты с крестиком",
    f'<path d="M10 120 Q20 60 70 50 Q120 46 122 70 Q100 110 10 120Z" fill="#4FB85A" {W(3.2)}/>'
    f'<path d="M16 116 Q60 80 118 66" fill="none" stroke="#2E8A3E" stroke-width="3"/>'
    f'<path d="M0 30 Q30 20 40 0 M100 0 Q100 20 128 26" fill="none" stroke="#2E8A3E" stroke-width="6" stroke-linecap="round"/>'
    f'<ellipse cx="64" cy="70" rx="30" ry="22" fill="#2E8AE8" {W(3.2)}/>'
    f'<circle cx="50" cy="50" r="10" fill="#2E8AE8" {W(3)}/><circle cx="78" cy="50" r="10" fill="#2E8AE8" {W(3)}/>'
    + eye(50, 50, 0.8) + eye(78, 50, 0.8) +
    "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="{O}"/>' for x, y in [(48, 78), (82, 80), (60, 86), (72, 66)]) +
    f'<path d="M56 66 Q64 72 72 66" fill="none" {W(2.4)}/>'
    f'<path d="M86 80 L104 92 L94 108 L76 96Z" fill="#FFF0C8" {W(2.4)}/><path d="M86 94 l6 4 M92 94 l-6 4" stroke="#E8434A" stroke-width="2.6"/>'
    f'<path d="M80 84 Q86 86 88 90" fill="none" {W(2.4)}/>')

I["atmoquest-novinsky"] = ("#F2EEE4", "#A89A7A",
    "латунный телеграфный ключ азбуки Морзе на деревянной подставке",
    "стучит, и из-под него вылетают точки и тире зашифрованного послания",
    f'<rect x="16" y="84" width="96" height="22" rx="5" fill="#8B5A2B" {W(3.2)}/>'
    f'<path d="M24 84 L24 76 L104 70 L104 78" fill="none" {W(3)}/>'
    f'<path d="M28 74 L100 64" stroke="#E8B83A" stroke-width="8" stroke-linecap="round"/><path d="M28 74 L100 64" fill="none" {W(1.6)}/>'
    f'<circle cx="100" cy="58" r="10" fill="#2F2A60" {W(2.6)}/><circle cx="64" cy="76" r="5" fill="#E8B83A" {W(2)}/>'
    + f(56, 94, d=7, k=0.55) +
    "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="{O}"/>' for x, y in [(30, 40), (78, 28)]) +
    "".join(f'<rect x="{x}" y="{y}" width="14" height="6" rx="3" fill="{O}"/>' for x, y in [(42, 30), (60, 20), (88, 38)]) +
    f'<path d="M106 50 l6 -6 M110 58 l8 -2" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')

I["fantastic-beasts-vasilevskogo"] = ("#E7E2FF", "#6E5BC8",
    "пушистый круглый зверёк неизвестной породы — одни огромные глаза и уши-кисточки",
    "выглядывает из старого деревянного ящика с соломой и надписью «не открывать»",
    f'<rect x="18" y="66" width="92" height="50" rx="4" fill="#C98B4A" {W(3.2)}/>'
    f'<path d="M18 84 H110 M18 100 H110" stroke="#A86E34" stroke-width="2.4"/>'
    f'<path d="M14 66 L110 50 L114 60 L18 76Z" fill="#D9A066" {W(3)}/>'
    f'<path d="M30 66 l6 -10 M50 64 l2 -12 M80 62 l-4 -12" stroke="#F2C14E" stroke-width="3" stroke-linecap="round"/>'
    f'<circle cx="64" cy="64" r="22" fill="#F2E6C9" {W(3)}/>'
    + "".join(f'<path d="M{64+22*__import__("math").cos(a*0.5):.0f} {64+22*__import__("math").sin(a*0.5):.0f} l{4*__import__("math").cos(a*0.5):.0f} {4*__import__("math").sin(a*0.5):.0f}" {W(2)}/>' for a in range(-6, 1)) +
    f'<path d="M46 50 L36 30 L52 44 M82 50 L92 30 L76 44" fill="#F2E6C9" {W(2.6)}/>'
    + eye(56, 62, 1.25) + eye(72, 62, 1.25) +
    f'<path d="M34 108 h16 M62 108 h10" stroke="#E8434A" stroke-width="3" stroke-linecap="round"/>')

I["igra-v-kalmara-mozaika"] = ("#FFE3EE", "#E8508A",
    "круглая сахарная конфета-пластинка с выдавленной звездой",
    "девочка осторожно вырезает звезду иголкой, высунув язык от старания",
    f'<circle cx="60" cy="74" r="40" fill="#E8A54A" {W(3.4)}/><circle cx="60" cy="74" r="34" fill="#F2BE6A"/>'
    f'<path d="M60 50 l7 14 15 2 -11 10 3 15 -14 -7 -14 7 3 -15 -11 -10 15 -2Z" fill="#F7D48E" {W(2.6)}/>'
    + f(60, 76, d=6, k=0.45) +
    f'<path d="M86 50 L110 18" stroke="#C7CED8" stroke-width="3" stroke-linecap="round"/>'
    + kid(108, 24, k=0.65, hair="#3A2414") +
    f'<path d="M104 32 q4 4 8 0" fill="#E8434A"/>'
    f'<path d="M16 34 l6 4 M24 22 l4 6" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')

I["iskateli-vremeni-balashikha"] = ("#EFE6FF", "#9A7BD8",
    "жестяная капсула времени — коробка с часами на крышке",
    "мальчик с лопаткой откопал её под деревом, а из щели пробивается волшебный свет",
    f'<path d="M0 92 Q64 80 128 92 V128 H0Z" fill="#8B5A2B" {W(2.6)}/>'
    f'<path d="M84 0 Q90 40 96 84 M110 0 Q104 40 104 86" fill="none" stroke="#6E431D" stroke-width="8"/>'
    f'<rect x="22" y="70" width="56" height="34" rx="6" fill="#A9B6C9" {W(3.2)}/>'
    f'<rect x="18" y="62" width="64" height="12" rx="4" fill="#C7D1E0" {W(3)}/>'
    f'<path d="M30 62 L70 62" stroke="#FFF3A6" stroke-width="3"/><path d="M40 60 L32 40 M50 58 L52 34 M60 60 L70 40" stroke="#FFF3A6" stroke-width="4" stroke-linecap="round" opacity=".8"/>'
    f'<circle cx="50" cy="88" r="11" fill="#fff" {W(2.4)}/><path d="M50 88 V81 M50 88 L56 90" {W(2)}/>'
    + kid(102, 66, k=0.7, hair="#5A3A22") +
    f'<path d="M94 76 Q102 72 110 76 L112 92 L92 92Z" fill="#4CC38A" {W(2.4)}/>'
    f'<path d="M92 80 L80 98" {W(3)}/><path d="M76 96 l8 6 -6 6 -6 -6Z" fill="#7C8BA1" {W(2)}/>')

# ================= студии и мастерские =================
I["narochno-dukhovskoy"] = ("#FFE7DE", "#E07A5F",
    "нарочно кривой глиняный кувшин с перекошенным горлышком",
    "крутится на гончарном круге и показывает язык",
    f'<ellipse cx="64" cy="108" rx="44" ry="10" fill="#7C8BA1" {W(3)}/><ellipse cx="64" cy="104" rx="40" ry="8" fill="#A9B6C9" {W(2.6)}/>'
    f'<path d="M40 102 Q26 76 44 56 Q50 48 46 36 L50 26 Q66 30 76 22 L80 32 Q74 42 82 52 Q104 72 88 102Z" fill="#D9895A" {W(3.4)}/>'
    f'<path d="M50 26 Q64 34 80 32" fill="none" stroke="#B06838" stroke-width="3"/>'
    f'<path d="M48 70 Q64 64 84 74" fill="none" stroke="#F2B48A" stroke-width="4" stroke-linecap="round"/>'
    + eye(56, 80, 0.6) + eye(74, 78, 0.75) +
    f'<path d="M58 90 Q66 96 74 88" fill="none" {W(2.4)}/><path d="M64 92 q2 8 8 2" fill="#FF7FA8" {W(1.8)}/>'
    f'<path d="M16 80 q-4 10 4 14 M112 80 q4 10 -4 14" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')

I["strontsianovaya-goloturiya"] = ("#D5F1FF", "#2E86C1",
    "оранжевая голотурия — морской огурец в пупырышках",
    "рисует кисточкой картину на холсте прямо на морском дне",
    f'<path d="M0 108 Q64 98 128 108 V128 H0Z" fill="#F2D59A" {W(2.4)}/>'
    f'<rect x="72" y="30" width="40" height="44" fill="#fff" {W(3)}/><path d="M80 74 L74 104 M104 74 L110 104" {W(3)}/>'
    f'<path d="M78 62 Q88 46 96 56 Q102 64 108 48" fill="none" stroke="#4FB85A" stroke-width="4" stroke-linecap="round"/><circle cx="100" cy="40" r="5" fill="#FFD23F"/>'
    f'<path d="M14 96 Q12 74 30 72 Q48 70 62 80 Q72 88 62 100 Q40 108 14 96Z" fill="#F2894A" {W(3.2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#FFC08A"/>' for x, y in [(24, 80), (36, 76), (48, 78), (30, 92), (44, 94), (56, 88)]) +
    f(30, 86, d=5, k=0.45) +
    f'<path d="M58 80 L76 60" stroke="#C98B4A" stroke-width="4" stroke-linecap="round"/><path d="M76 60 l4 -4" stroke="#E8434A" stroke-width="5" stroke-linecap="round"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="#fff" stroke-width="2"/>' for x, y, r in [(22, 50, 4), (30, 36, 3), (24, 24, 2)]))

I["charodeyka-brateevskaya"] = ("#FFF1F6", "#E58FB0",
    "белый керамический кот-копилка с прорезью на макушке",
    "кисточка дорисовывает ему на боку синие цветочки",
    f'<path d="M30 104 Q20 70 40 56 L34 30 L50 44 Q64 40 78 44 L94 30 L88 56 Q108 70 98 104Z" fill="#FFFDF8" {W(3.4)}/>'
    f'<rect x="56" y="44" width="16" height="4" rx="2" fill="{O}"/>'
    + f(64, 66, d=10, k=0.75) +
    f'<path d="M58 74 l6 3 6 -3" fill="none" {W(2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#4F86E8"/><circle cx="{x}" cy="{y}" r="1.6" fill="#FFD23F"/>' for x, y in [(44, 90), (56, 96), (40, 78)]) +
    f'<path d="M100 40 L80 86" stroke="#C98B4A" stroke-width="5" stroke-linecap="round"/><path d="M80 86 l-3 8" stroke="#4F86E8" stroke-width="6" stroke-linecap="round"/>'
    f'<rect x="96" y="36" width="8" height="6" fill="#C7CED8" {W(1.6)} transform="rotate(22 100 40)"/>')

I["muza-korabelnaya"] = ("#F5F0FF", "#9C8BE0",
    "золотая античная лира с завитками",
    "одна её струна превратилась в кисточку и рисует в воздухе радугу",
    f'<path d="M86 30 Q110 10 112 40" fill="none" stroke="#E8434A" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M88 36 Q108 20 110 44" fill="none" stroke="#FFD23F" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M90 42 Q106 30 108 48" fill="none" stroke="#4F86E8" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M40 110 Q28 80 30 54 Q32 30 46 24 Q40 40 46 52 M88 110 Q100 80 98 54 Q96 30 82 24 Q88 40 82 52" fill="none" stroke="#E8B83A" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M40 110 Q28 80 30 54 Q32 30 46 24 M88 110 Q100 80 98 54 Q96 30 82 24" fill="none" {W(1.8)}/>'
    f'<rect x="34" y="102" width="60" height="14" rx="5" fill="#E8B83A" {W(3)}/>'
    f'<rect x="38" y="42" width="52" height="8" rx="4" fill="#C98B4A" {W(2.4)}/>'
    + "".join(f'<path d="M{x} 50 V102" stroke="#fff" stroke-width="2"/>' for x in (50, 60, 70)) +
    f'<path d="M80 50 Q84 40 88 38" stroke="#C98B4A" stroke-width="3" fill="none"/>'
    + f(64, 80, d=8, k=0.6))

I["linii-i-kraski-sudostroitelnaya"] = ("#FFFDE6", "#E8D24A",
    "деревянная линейка с делениями и глазками",
    "сама ведёт ровную синюю линию, а вокруг подпрыгивают капли краски",
    f'<path d="M14 100 L114 100" stroke="#4F86E8" stroke-width="5" stroke-linecap="round"/>'
    f'<rect x="10" y="44" width="104" height="30" rx="4" fill="#F2C78A" {W(3.2)}/>'
    + "".join(f'<path d="M{x} 44 v{8 if i % 2 else 13}" {W(2)}/>' for i, x in enumerate(range(18, 112, 8))) +
    f(62, 62, d=10, k=0.65) +
    f'<path d="M108 74 L112 98" {W(2.4)}/>'
    + "".join(f'<path d="M{x} {y} q5 8 0 11 q-5 -3 0 -11Z" fill="{c}" {W(1.8)}/>' for x, y, c in [(24, 18, "#E8434A"), (54, 12, "#7CD26E"), (88, 20, "#B48AF0"), (40, 108, "#FF8C3A")]))

I["art-people-likhacheva"] = ("#E3FFF7", "#45C2A5",
    "человечек, вылепленный из разноцветного пластилина",
    "приветливо машет, стоя на дощечке рядом со стекой и брусками пластилина",
    f'<rect x="14" y="100" width="100" height="14" rx="4" fill="#C98B4A" {W(3)}/>'
    f'<circle cx="64" cy="36" r="16" fill="#FFB86B" {W(3)}/>' + f(64, 38, d=6, k=0.5) +
    f'<path d="M56 22 q8 -8 16 0" fill="none" stroke="#7A4A22" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M48 54 Q64 48 80 54 L84 78 L44 78Z" fill="#4F86E8" {W(3)}/>'
    f'<path d="M50 58 Q36 50 30 36" fill="none" stroke="#E8434A" stroke-width="9" stroke-linecap="round"/><path d="M50 58 Q36 50 30 36" fill="none" {W(1.6)}/>'
    f'<path d="M78 58 Q90 66 92 78" fill="none" stroke="#E8434A" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M54 78 V100 M74 78 V100" stroke="#7CD26E" stroke-width="10" stroke-linecap="round"/>'
    f'<path d="M98 98 L114 70" stroke="#2F2A60" stroke-width="4" stroke-linecap="round"/>'
    f'<rect x="16" y="88" width="16" height="12" rx="2" fill="#FFD23F" {W(2)}/><rect x="20" y="78" width="12" height="10" rx="2" fill="#B48AF0" {W(2)}/>')

I["zn-lab-megapolis"] = ("#E9ECF5", "#7C8BB0",
    "алюминиевый тюбик цинковых белил с надписью Zn",
    "сам выдавливает белую краску волнистой змейкой на чёрный картон",
    f'<rect x="8" y="78" width="112" height="36" rx="4" fill="#2F2A60" {W(2.6)}/>'
    f'<path d="M20 96 Q34 84 46 96 Q58 108 70 96 Q82 84 94 96" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M20 96 Q34 84 46 96 Q58 108 70 96 Q82 84 94 96" fill="none" stroke="#DCE3EE" stroke-width="2.4" stroke-linecap="round"/>'
    f'<path d="M96 70 L120 18 L104 10 L82 62Z" fill="#D7DCE6" {W(3)}/>'
    f'<path d="M120 18 L104 10" stroke="#9AA4B8" stroke-width="6"/>'
    f'<rect x="88" y="62" width="10" height="12" rx="2" fill="#7C8BA1" {W(2.2)} transform="rotate(24 93 68)"/>'
    f'<text x="96" y="46" font-family="Arial" font-weight="bold" font-size="13" fill="#4F86E8" transform="rotate(-65 100 42)">Zn</text>'
    + f(102, 30, d=4, k=0.4))

I["prityazhenie-opolcheniya"] = ("#FFEFE6", "#F08A6A",
    "красный воздушный шарик, натёртый о свитер",
    "притягивает к себе пушистые волосы малыша — они встали дыбом",
    f'<ellipse cx="94" cy="40" rx="22" ry="26" fill="#E8303A" {W(3.2)}/>'
    f'<ellipse cx="86" cy="30" rx="6" ry="8" fill="#FF8A8F"/><path d="M94 66 l-4 6 h8Z" fill="#E8303A" {W(2)}/>'
    f'<path d="M94 72 Q90 90 98 110" fill="none" {W(2)}/>' + f(94, 42, d=7, k=0.55) +
    f'<circle cx="44" cy="86" r="22" fill="#FFD9B8" {W(3)}/>' + face(44, 88, d=7, k=0.6) +
    "".join(f'<path d="M{30+i*5} 70 Q{40+i*8} {50-i*2} {66+i*3} {36+i*4}" fill="none" stroke="#E8B04A" stroke-width="3" stroke-linecap="round"/>' for i in range(5)) +
    f'<path d="M26 108 Q44 100 62 108 L66 128 L22 128Z" fill="#7CD26E" {W(2.8)}/>'
    + "".join(f'<path d="M{x} {y} l3 -6 l3 6" fill="none" stroke="#FFD23F" stroke-width="2.4" stroke-linecap="round"/>' for x, y in [(70, 60), (66, 76)]))

I["tsifra-pilyugina"] = ("#EAF6FF", "#69A9E0",
    "большая цифра 4 в виде синего стульчика",
    "на ней, как на стуле, сидит малыш и считает на пальцах",
    f'<path d="M66 14 L30 76 L96 76" fill="none" stroke="#3566C2" stroke-width="18" stroke-linecap="round" stroke-linejoin="round"/>'
    f'<path d="M78 14 V118" stroke="#3566C2" stroke-width="18" stroke-linecap="round"/>'
    f'<path d="M66 14 L30 76 L96 76 M78 14 V118" fill="none" stroke="#5E8FF0" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'
    + f(52, 96, d=6, k=0.5) +
    kid(56, 50, k=0.75, hair="#5A3A22") +
    f'<path d="M48 60 Q56 56 64 60 L66 74 L46 74Z" fill="#FFD23F" {W(2.4)}/>'
    f'<path d="M46 62 L34 54 M64 62 L74 52" {W(2.8)}/><path d="M72 48 v-6 M75 48 v-7 M78 49 v-5" stroke="#FFD9B8" stroke-width="2.6" stroke-linecap="round"/>'
    + "".join(f'<text x="{x}" y="{y}" font-family="Arial" font-weight="bold" font-size="12" fill="#fff">{t}</text>' for x, y, t in [(14, 40, "1"), (104, 30, "2"), (108, 100, "3")]))

I["effee-pups-pilyugina"] = ("#FFF6E8", "#F3B970",
    "пупс-голыш с круглыми щёчками и хохолком",
    "сидит на листе бумаги и рисует пальчиками разноцветные отпечатки",
    f'<rect x="10" y="78" width="108" height="40" rx="3" fill="#fff" {W(2.6)}/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="5" ry="6" fill="{c}"/>' for (x, y), c in zip([(22, 96), (32, 106), (96, 90), (106, 104), (90, 108)],
              ["#E8434A", "#4F86E8", "#7CD26E", "#B48AF0", "#FF8C3A"])) +
    f'<ellipse cx="64" cy="82" rx="26" ry="22" fill="#FFD3B5" {W(3.2)}/>'
    f'<circle cx="64" cy="44" r="24" fill="#FFD3B5" {W(3.2)}/>' + f(64, 46, d=8, k=0.7) +
    f'<path d="M62 20 q2 -8 8 -6 q-4 2 -2 8" fill="none" {W(2.4)}/>'
    f'<path d="M40 76 Q30 86 34 96 M88 76 Q98 86 94 96" fill="none" stroke="#FFD3B5" stroke-width="9" stroke-linecap="round"/>'
    f'<circle cx="34" cy="98" r="5" fill="#4F86E8" {W(2)}/><circle cx="94" cy="98" r="5" fill="#E8434A" {W(2)}/>')

I["house-of-arts-myasnitskaya"] = ("#E9F9FF", "#55B8E8",
    "домик в форме палитры художника с окошками-пятнами краски",
    "из его трубы-кисточки валит радужный дым",
    f'<path d="M20 110 Q10 70 34 54 L64 30 L94 54 Q118 70 108 110Z" fill="#E8C08A" {W(3.4)}/>'
    f'<path d="M64 30 L20 66 M64 30 L108 66" fill="none" stroke="#C9935A" stroke-width="3"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="8" fill="{c}" {W(2.2)}/>' for x, y, c in [(40, 72, "#E8434A"), (64, 62, "#FFD23F"), (88, 72, "#4F86E8"), (44, 96, "#7CD26E")]) +
    f'<path d="M72 110 V90 Q72 82 80 82 Q88 82 88 90 V110Z" fill="#8B5A2B" {W(2.6)}/>'
    f'<path d="M86 40 L90 18" stroke="#C98B4A" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M90 16 Q96 4 106 10 Q114 2 120 12" fill="none" stroke="#E8434A" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M92 22 Q98 10 108 16 Q116 8 122 18" fill="none" stroke="#FFD23F" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M94 28 Q100 16 110 22 Q118 14 124 24" fill="none" stroke="#4F86E8" stroke-width="4" stroke-linecap="round"/>'
    + f(52, 86, d=5, k=0.45, blush=False))

I["dkhsh-7-pervomayskaya"] = ("#F6F6F6", "#A0A8B8",
    "чёрный брусок угля для рисования с глазками",
    "рисует углём на белом листе кота, оставляя пыльный след",
    f'<rect x="14" y="18" width="78" height="96" rx="2" fill="#fff" {W(3)}/>'
    f'<path d="M34 90 Q30 64 44 58 L40 44 L50 52 Q56 50 62 52 L70 44 L68 58 Q80 66 74 90Z" fill="none" stroke="#2F2A60" stroke-width="3.4" stroke-linejoin="round"/>'
    f'<circle cx="49" cy="66" r="2" fill="#2F2A60"/><circle cx="62" cy="66" r="2" fill="#2F2A60"/>'
    f'<path d="M74 86 Q90 84 86 70" fill="none" stroke="#2F2A60" stroke-width="3"/>'
    f'<path d="M86 104 L112 58 L124 66 L98 112Z" fill="#2B2B33" {W(3)}/>'
    f'<path d="M86 104 L98 112 L90 116Z" fill="#555"/>'
    + eye(103, 80, 0.55) + eye(111, 86, 0.55) +
    f'<circle cx="80" cy="112" r="2" fill="#888"/><circle cx="74" cy="108" r="1.6" fill="#999"/>')

I["chudo-shkola-umnitsa"] = ("#F2FFE9", "#86C96A",
    "тетрадка в клетку с красной пятёркой на обложке",
    "радостно подпрыгивает, а из неё вылетают буквы",
    f'<path d="M30 30 L94 22 L102 102 L36 110Z" fill="#fff" {W(3.2)}/>'
    + "".join(f'<path d="M{30+i*8+i*0.9:.0f} {30-i:.0f} L{36+i*8+i*0.9:.0f} {110-i:.0f}" stroke="#BFD8FF" stroke-width="1.4"/>' for i in range(1, 8)) +
    "".join(f'<path d="M{31+j*0.7:.0f} {30+j*10} L{95+j*0.9:.0f} {22+j*10}" stroke="#BFD8FF" stroke-width="1.4"/>' for j in range(1, 8)) +
    f'<path d="M30 30 L36 110" stroke="#4F86E8" stroke-width="5"/>'
    f'<text x="58" y="56" font-family="Arial" font-weight="bold" font-size="26" fill="#E8303A">5</text>'
    + f(66, 78, d=9, k=0.7) +
    f'<text x="98" y="30" font-family="Arial" font-weight="bold" font-size="16" fill="#E8434A">А</text>'
    f'<text x="12" y="28" font-family="Arial" font-weight="bold" font-size="14" fill="#4F86E8">Б</text>'
    f'<path d="M40 118 l-6 4 M90 114 l6 4" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')

I["pluzhnikova-arch-school"] = ("#FFF4E0", "#E5A651",
    "макет домика из белого картона с прорезанными окнами",
    "девочка аккуратно опускает на него треугольную крышу",
    f'<rect x="10" y="102" width="108" height="10" rx="3" fill="#7CD26E" {W(2.4)}/>'
    f'<rect x="22" y="62" width="52" height="40" fill="#FFFDF6" {W(3)}/>'
    f'<path d="M74 62 L92 54 L92 94 L74 102Z" fill="#E6E2D6" {W(3)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="10" height="10" fill="#BFE8FF" {W(2)}/>' for x, y in [(30, 70), (54, 70)]) +
    f'<rect x="40" y="84" width="12" height="18" fill="#C98B4A" {W(2)}/>'
    f'<path d="M18 46 L48 24 L78 46Z" fill="#E8434A" {W(3)}/><path d="M78 46 L96 38 L66 18 L48 24" fill="#B8322A" {W(2.6)}/>'
    + kid(104, 30, k=0.65, hair="#3A2414") +
    f'<path d="M98 40 L84 36 M108 40 L104 22" {W(2.6)}/>' + f(48, 92, d=4, k=0.36, blush=False))

I["artistika-velaskesa"] = ("#FFE6F5", "#D86AB0",
    "три баночки гуаши — красная, жёлтая и синяя",
    "жонглируют друг другом по дуге, как в цирке, разбрызгивая капельки",
    f'<path d="M24 100 Q64 -10 104 100" fill="none" stroke="#fff" stroke-width="2.6" stroke-dasharray="4 6"/>'
    + "".join(f'<g transform="rotate({r} {x} {y})"><rect x="{x-13}" y="{y-12}" width="26" height="26" rx="5" fill="{c}" {W(2.8)}/><rect x="{x-15}" y="{y-18}" width="30" height="9" rx="3" fill="#fff" {W(2.4)}/></g>'
              for x, y, r, c in [(26, 94, -18, "#E8434A"), (64, 30, 0, "#FFD23F"), (102, 94, 18, "#4F86E8")]) +
    f(26, 96, d=4, k=0.38) + f(64, 32, d=4, k=0.38) + f(102, 96, d=4, k=0.38) +
    "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="{c}"/>' for x, y, c in [(44, 58, "#E8434A"), (84, 56, "#4F86E8"), (60, 70, "#FFD23F")]))

I["ars-nova-lipovy-park"] = ("#3A4FA8", "#18225E",
    "сверхновая звезда-взрыв из брызг краски",
    "сияет в космосе, разбрасывая лучи-мазки всех цветов",
    "".join(f'<path d="M64 64 L{64+56*__import__("math").cos(a*0.5236):.0f} {64+56*__import__("math").sin(a*0.5236):.0f}" stroke="{c}" stroke-width="9" stroke-linecap="round"/>'
            for a, c in zip(range(12), ["#E8434A", "#FF8C3A", "#FFD23F", "#7CD26E", "#4CD3B0", "#45A8F0", "#B48AF0", "#F58CB8"] * 2)) +
    "".join(f'<circle cx="{64+58*__import__("math").cos(a*0.5236+0.26):.0f}" cy="{64+58*__import__("math").sin(a*0.5236+0.26):.0f}" r="3" fill="#fff"/>' for a in range(12)) +
    f'<circle cx="64" cy="64" r="26" fill="#FFF3A6" {W(3.2)}/>' + f(64, 64, d=8, k=0.65) +
    sparkle(22, 24, 4, "#fff") + sparkle(106, 108, 4, "#fff"))

I["delta-velaskesa"] = ("#E6FAFF", "#4DB0D9",
    "треугольный дельтаплан с крылом в разноцветных мазках",
    "мальчик-пилот парит над облаками и рисует кисточкой на ходу",
    f'<ellipse cx="30" cy="108" rx="26" ry="10" fill="#fff"/><ellipse cx="100" cy="112" rx="22" ry="8" fill="#fff"/>'
    f'<path d="M64 20 L118 62 L64 52 L10 62Z" fill="#FFD23F" {W(3.2)}/>'
    f'<path d="M64 20 L40 58 M64 20 L88 58" stroke="#E8434A" stroke-width="7"/><path d="M64 20 L64 52" stroke="#4F86E8" stroke-width="6"/>'
    f'<path d="M64 20 L118 62 L64 52 L10 62Z" fill="none" {W(3.2)}/>'
    f'<path d="M64 52 L58 72 M64 52 L72 72 M50 72 H80" {W(2.4)}/>'
    + kid(64, 84, k=0.7, hair="#3A2414") +
    f'<path d="M56 94 Q64 90 72 94 L74 108 L54 108Z" fill="#4CC38A" {W(2.4)}/>'
    f'<path d="M72 96 L90 104" {W(2.6)}/><path d="M90 104 l6 4" stroke="#B48AF0" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M98 110 q6 -4 12 0" fill="none" stroke="#B48AF0" stroke-width="3" stroke-linecap="round"/>' + f(64, 38, d=6, k=0.45))

I["blago-monakhovoy"] = ("#FFFBEA", "#F0B93C",
    "бумажная гирлянда из вырезанных человечков, держащихся за руки",
    "растягивается между двумя детскими ножницами, все человечки улыбаются",
    f'<path d="M6 64 h8 l4 -14 a6 6 0 1 1 8 0 l4 14 h0 l-4 4 l2 14 h-6 l-2 -10 l-2 10 h-6 l2 -14 l-4 -4Z" fill="none"/>'
    + "".join(f'<g transform="translate({x} 0)"><circle cx="14" cy="44" r="8" fill="{c}" {W(2.4)}/>'
              f'<path d="M4 58 H24 L22 76 L18 76 L16 92 L12 92 L10 76 L6 76Z" fill="{c}" {W(2.4)}/>'
              f'<path d="M-2 60 H30" stroke="{c}" stroke-width="6" stroke-linecap="round"/></g>'
              for x, c in [(22, "#FF8C9A"), (46, "#7FC8F8"), (70, "#9EE07F"), (94, "#C6A6F5")]) +
    "".join(f(36 + i * 24, 44, d=3, k=0.28, blush=False) for i in range(4)) +
    f'<path d="M8 100 l12 -8 M8 92 l12 8" stroke="#E8434A" stroke-width="3" stroke-linecap="round"/>'
    f'<circle cx="6" cy="104" r="4" fill="none" stroke="#E8434A" stroke-width="2.6"/><circle cx="6" cy="88" r="4" fill="none" stroke="#E8434A" stroke-width="2.6"/>'
    + sparkle(64, 106, 6, "#fff") + sparkle(110, 20, 4, "#fff"))

I["glinoteka-edalgo"] = ("#F6EEDB", "#C2A36B",
    "деревянная книжная полка, где вместо книг стоят глиняные горшочки",
    "горшочки выстроились по росту, как тома в библиотеке, и один выглядывает",
    f'<rect x="14" y="20" width="100" height="96" rx="4" fill="#A86E34" {W(3.2)}/>'
    f'<rect x="20" y="26" width="88" height="40" fill="#F2E3C6"/><rect x="20" y="72" width="88" height="38" fill="#F2E3C6"/>'
    f'<path d="M14 68 H114" {W(3)}/>'
    + "".join(f'<path d="M{x-w} 66 Q{x-w-2} {66-h/2} {x-w/2} {66-h} H{x+w/2} Q{x+w+2} {66-h/2} {x+w} 66Z" fill="{c}" {W(2.2)}/>' for x, w, h, c in
              [(30, 7, 34, "#D9895A"), (48, 8, 28, "#C46A2E"), (66, 7, 22, "#E8A06A"), (82, 6, 18, "#B85C2A"), (98, 6, 14, "#D9895A")]) +
    f'<path d="M30 110 Q24 90 36 84 H52 Q62 90 56 110Z" fill="#D9895A" {W(2.6)}/>' + f(44, 98, d=5, k=0.45) +
    "".join(f'<rect x="{x}" y="{y}" width="8" height="{h}" fill="{c}" {W(1.8)}/>' for x, y, h, c in [(70, 86, 24, "#4F86E8"), (80, 90, 20, "#7CD26E"), (90, 84, 26, "#E8434A")]))

I["art-vizual-balashikha"] = ("#EDFFF0", "#5DC28A",
    "огромный глаз-персонаж, у которого ресницы — кисточки с краской",
    "подмигивает и раскрашивает ресницами-кистями всё вокруг",
    f'<path d="M10 66 Q64 14 118 66 Q64 116 10 66Z" fill="#fff" {W(3.4)}/>'
    f'<circle cx="64" cy="66" r="22" fill="#45A8F0" {W(3)}/><circle cx="64" cy="66" r="10" fill="{O}"/><circle cx="58" cy="60" r="5" fill="#fff"/>'
    + "".join(f'<path d="M{64+52*__import__("math").cos(a):.0f} {66-30*__import__("math").sin(a):.0f} l{14*__import__("math").cos(a):.0f} {-14*__import__("math").sin(a):.0f}" stroke="#C98B4A" stroke-width="4" stroke-linecap="round"/>'
              f'<circle cx="{64+68*__import__("math").cos(a):.0f}" cy="{66-46*__import__("math").sin(a):.0f}" r="4.5" fill="{c}"/>'
              for a, c in zip([0.5, 0.95, 1.4, 1.85, 2.3, 2.7], ["#E8434A", "#FF8C3A", "#FFD23F", "#7CD26E", "#B48AF0", "#F58CB8"])) +
    f'<path d="M50 98 Q64 104 78 98" fill="none" {W(2.6)}/>'
    f'<ellipse cx="28" cy="88" rx="6" ry="3.4" fill="#FF7FA8" opacity=".6"/><ellipse cx="100" cy="88" rx="6" ry="3.4" fill="#FF7FA8" opacity=".6"/>')

I["art-kaleidoskop-balashikha"] = ("#FFF0E0", "#F2994A",
    "прозрачная шестерёнка спирографа с дырочками",
    "крутится внутри кольца и вычерчивает ручкой узор-цветок",
    f'<circle cx="64" cy="64" r="50" fill="#fff" {W(3)}/>'
    + "".join(f'<ellipse cx="64" cy="64" rx="34" ry="12" fill="none" stroke="{c}" stroke-width="2.4" transform="rotate({r} 64 64)"/>' for r, c in
              zip(range(0, 180, 30), ["#E8434A", "#FF8C3A", "#4F86E8", "#7CD26E", "#B48AF0", "#F58CB8"])) +
    f'<circle cx="64" cy="64" r="50" fill="none" stroke="#C7CED8" stroke-width="6"/>'
    f'<circle cx="84" cy="80" r="20" fill="#BFE8FF" opacity=".8" {W(2.6)}/>'
    + "".join(f'<path d="M{84+20*__import__("math").cos(a*0.524):.0f} {80+20*__import__("math").sin(a*0.524):.0f} l{4*__import__("math").cos(a*0.524):.0f} {4*__import__("math").sin(a*0.524):.0f}" {W(2.4)}/>' for a in range(12)) +
    f'<circle cx="90" cy="76" r="3" fill="#E8434A" {W(1.6)}/><path d="M90 76 L108 50" stroke="#4F86E8" stroke-width="4" stroke-linecap="round"/>'
    + f(80, 84, d=5, k=0.4))

I["artpodval-balashikha"] = ("#F3D9CF", "#B5654A",
    "крутая лестница вниз в уютный творческий подвал",
    "над ней висит гирлянда лампочек, а внизу ждёт мольберт с картиной",
    "".join(f'<rect x="{x}" y="{y}" width="24" height="12" rx="2" fill="#D9886A" {W(1.4)}/>' for y in range(0, 60, 12) for x in range(-(y // 12 % 2) * 12, 128, 24)) +
    f'<path d="M0 10 Q32 26 64 14 Q96 2 128 18" fill="none" {W(2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="{c}" {W(1.8)}/>' for x, y, c in [(16, 20, "#FFD23F"), (40, 22, "#FF8C3A"), (64, 18, "#7CD26E"), (88, 12, "#FFD23F"), (112, 16, "#45A8F0")]) +
    f'<path d="M0 60 H128 V128 H0Z" fill="#5A3A44"/>'
    + "".join(f'<path d="M{10+i*12} {60+i*12} h22 v12" fill="#9C6A52" {W(2.4)}/>' for i in range(6)) +
    f'<path d="M92 120 L100 84 L108 120 M100 84 V74" {W(2.6)}/><rect x="86" y="66" width="28" height="22" fill="#fff" {W(2.4)}/>'
    f'<circle cx="94" cy="76" r="4" fill="#FFD23F"/><path d="M90 86 Q100 74 112 84" fill="none" stroke="#4FB85A" stroke-width="3"/>'
    + f(100, 104, d=4, k=0.36, blush=False))

I["finebot-zheleznodorozhny"] = ("#E4ECFF", "#5677D8",
    "маленький робот-паучок на шести суставчатых ножках с антенной",
    "ползёт по столу кружка, а за ним тянется разноцветный проводок",
    f'<rect x="0" y="96" width="128" height="32" fill="#D9A066"/><path d="M0 96 H128" {W(2.6)}/>'
    + "".join(f'<path d="M{64+s1*14} 72 L{64+s1*(30+i*4)} {56+i*10} L{64+s1*(36+i*6)} 98" fill="none" {W(3.2)}/>' for s1 in (-1, 1) for i in range(3)) +
    f'<ellipse cx="64" cy="70" rx="26" ry="20" fill="#C7D1E0" {W(3.2)}/>'
    f'<rect x="50" y="54" width="28" height="16" rx="6" fill="#2F2A60" {W(2.4)}/>'
    f'<circle cx="58" cy="62" r="4" fill="#4CD3B0"/><circle cx="70" cy="62" r="4" fill="#4CD3B0"/>'
    f'<path d="M64 50 V38" {W(2.4)}/><circle cx="64" cy="36" r="4" fill="#E8434A" {W(2)}/>'
    f'<path d="M38 78 Q20 84 14 104 Q10 116 2 118" fill="none" stroke="#E8434A" stroke-width="3"/>'
    f'<path d="M38 82 Q24 90 22 110 Q20 118 10 124" fill="none" stroke="#FFD23F" stroke-width="3"/>'
    f'<path d="M58 80 Q64 84 70 80" fill="none" {W(2.2)}/>')

I["limonad-balashikha"] = ("#FFFFE0", "#C8D84A",
    "сочная долька лимона в красном берете художника",
    "держит кисточку и рисует на листе жёлтое солнышко",
    f'<path d="M14 92 A44 44 0 0 1 102 92Z" fill="#FFE34A" {W(3.4)}/><path d="M22 92 A36 36 0 0 1 94 92Z" fill="#FFF6A8"/>'
    + "".join(f'<path d="M58 92 L{58+34*__import__("math").cos(a):.0f} {92-34*__import__("math").sin(a):.0f}" stroke="#FFE34A" stroke-width="3"/>' for a in (0.5, 1.0, 1.57, 2.1, 2.6)) +
    f'<path d="M14 92 H102" {W(3.4)}/>' + f(58, 74, d=8, k=0.6) +
    f'<path d="M30 52 Q44 32 68 40 Q74 46 62 50 Q46 52 30 52Z" fill="#E8303A" {W(2.6)}/><path d="M56 38 l2 -6" {W(2.4)}/>'
    f'<rect x="88" y="98" width="34" height="24" fill="#fff" {W(2.4)}/><circle cx="105" cy="110" r="6" fill="#FFD23F"/>'
    f'<path d="M98 82 L108 104" stroke="#C98B4A" stroke-width="4" stroke-linecap="round"/>')

I["ornament-balashikha"] = ("#E9F3FF", "#7FA8D8",
    "керамическая кружка-лисичка с ручкой-хвостом и голубым орнаментом",
    "стоит на гончарном столе, и девочка дорисовывает ей узор",
    f'<rect x="8" y="106" width="112" height="10" rx="3" fill="#C98B4A" {W(2.4)}/>'
    f'<path d="M26 40 L30 104 L82 104 L86 40Z" fill="#F08A3A" {W(3.4)}/>'
    f'<path d="M26 40 L32 22 L44 40 M86 40 L80 22 L68 40" fill="#F08A3A" {W(3)}/>'
    f'<path d="M86 52 Q112 50 108 76 Q104 96 82 88" fill="none" stroke="#F08A3A" stroke-width="10" stroke-linecap="round"/>'
    f'<path d="M86 52 Q112 50 108 76 Q104 96 82 88" fill="none" {W(1.6)}/><path d="M96 90 q8 -2 12 -12" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M30 80 L82 80" stroke="#fff" stroke-width="8"/><path d="M34 80 l6 -4 6 4 6 -4 6 4 6 -4 6 4 6 -4" fill="none" stroke="#3566C2" stroke-width="2.4"/>'
    + f(56, 58, d=9, k=0.7) +
    kid(110, 36, k=0.55, hair="#3A2414") + f'<path d="M104 44 L84 76" {W(2.4)}/>')

I["amaklass-khimki"] = ("#F0E9FF", "#A58BE0",
    "деревянная шнуровка в виде кусочка сыра с дырочками",
    "через дырочки пролезает красный шнурок-червячок с глазками",
    f'<path d="M14 92 L64 30 L114 70 L114 104 L14 104Z" fill="#FFD45E" {W(3.4)}/>'
    f'<path d="M14 92 L114 70" stroke="#E8B83A" stroke-width="3"/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r*0.85:.1f}" fill="#E8B83A" {W(2.2)}/>' for x, y, r in [(46, 66, 7), (80, 62, 6), (64, 90, 7), (96, 92, 5)]) +
    f'<path d="M24 100 Q30 82 46 66 Q60 54 80 62 Q96 70 96 92" fill="none" stroke="#E8434A" stroke-width="5" stroke-linecap="round" stroke-dasharray="20 14"/>'
    f'<circle cx="24" cy="102" r="7" fill="#E8434A" {W(2.2)}/>' + eye(21, 101, 0.4) + eye(28, 101, 0.4) +
    f(44, 86, d=5, k=0.42))

I["liniya-kisti-khimki"] = ("#E8FFFB", "#3DBFA8",
    "широкая плоская кисть-флейц с деревянной ручкой",
    "одним длинным мазком проводит радужную волну через весь лист",
    f'<path d="M6 96 Q34 56 62 80 Q90 104 118 60" fill="none" stroke="#E8434A" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M6 104 Q34 64 62 88 Q90 112 118 68" fill="none" stroke="#FFD23F" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M6 112 Q34 72 62 96 Q90 120 118 76" fill="none" stroke="#4F86E8" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M98 62 L114 52 L128 72 L112 82Z" fill="#4F86E8" {W(2.6)}/>'
    f'<path d="M100 58 L112 50 L104 40 L92 48Z" fill="#C7CED8" {W(2.6)}/>'
    f'<path d="M98 44 L60 12 L54 20 L92 50" fill="#E8A54A" {W(3)}/>' + f(78, 34, d=5, k=0.42))

I["klass-sovkhoznaya-khimki"] = ("#FFF0EE", "#E86A6A",
    "школьный пенал-тубус на молнии",
    "молния расстегнулась, и из пенала, как из ракеты, вылетают цветные карандаши",
    f'<rect x="14" y="60" width="78" height="40" rx="20" fill="#3566C2" {W(3.4)}/>'
    f'<path d="M30 60 Q54 54 78 60" fill="none" stroke="#C7CED8" stroke-width="4" stroke-dasharray="3 3"/>'
    f'<rect x="76" y="54" width="10" height="8" rx="2" fill="#FFD23F" {W(2)}/>'
    + f(52, 82, d=8, k=0.65) +
    "".join(f'<g transform="rotate({r} 70 60)"><rect x="66" y="{20}" width="9" height="36" fill="{c}" {W(2)}/><path d="M66 20 L70.5 10 L75 20Z" fill="#F2D3A0" {W(1.8)}/></g>'
            for r, c in [(-30, "#E8434A"), (-5, "#7CD26E"), (22, "#FFD23F"), (48, "#B48AF0")]) +
    f'<path d="M20 106 l-6 6 M36 108 l-4 8" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')

I["saba-rubtsovoy-khimki"] = ("#F9E8FF", "#B86AE0",
    "стеклянная баночка с золотыми блёстками",
    "опрокинулась, и блёстки высыпаются звёздочками на самодельную открытку",
    f'<rect x="20" y="78" width="88" height="40" rx="3" fill="#FFFDF4" {W(2.6)}/><path d="M64 78 V118" stroke="#E6DCC6" stroke-width="2"/>'
    f'<path d="M36 100 q8 -14 16 0 q-8 10 -16 0" fill="#F58CB8" {W(2)}/>'
    f'<g transform="rotate(-38 54 46)"><rect x="34" y="28" width="38" height="44" rx="8" fill="#DDF3FF" opacity=".85" {W(3)}/>'
    f'<rect x="32" y="20" width="42" height="12" rx="4" fill="#E8434A" {W(2.6)}/>'
    f'<rect x="38" y="46" width="30" height="22" rx="6" fill="#FFD23F"/></g>' + f(54, 54, d=6, k=0.5) +
    "".join(sparkle(x, y, r, "#FFD23F") for x, y, r in [(84, 60, 5), (94, 74, 4), (78, 76, 3), (100, 90, 4), (88, 92, 3), (72, 92, 4)]))

I["chunikhin-musical-khimki"] = ("#2D2350", "#120C2A",
    "лестница, у которой ступеньки — клавиши пианино",
    "девочка в блестящем платье спускается по ней и поёт, каждая ступенька звучит",
    f'<path d="M64 0 L20 128 H108Z" fill="#FFF3A6" opacity=".14"/>'
    + "".join(f'<rect x="{10+i*16}" y="{24+i*16}" width="{118-i*16}" height="14" fill="#fff" {W(2.2)}/>'
              f'<rect x="{18+i*16}" y="{24+i*16}" width="8" height="8" fill="{O}"/><rect x="{40+i*16}" y="{24+i*16}" width="8" height="8" fill="{O}"/>' for i in range(6)) +
    kid(34, 22, k=0.7, hair="#E8B04A") +
    f'<path d="M26 32 Q34 28 42 32 L48 52 L20 52Z" fill="#E8508A" {W(2.4)}/>'
    + "".join(sparkle(x, y, 2.6, "#fff") for x, y in [(30, 42), (38, 46), (34, 38)]) +
    f'<path d="M50 18 q6 -8 10 -2 M58 8 q6 -6 8 0" fill="none" stroke="#FFD23F" stroke-width="2.6"/>'
    f'<circle cx="50" cy="20" r="2.6" fill="#FFD23F"/><circle cx="58" cy="10" r="2.6" fill="#FFD23F"/>')

I["les-i-glina-khimki"] = ("#EAF7DE", "#7DAF55",
    "глиняный гриб-боровик с толстой ножкой, ещё со следами пальцев",
    "стоит на пеньке в лесу рядом с настоящим листиком и ягодкой",
    f'<path d="M24 112 L28 84 H100 L104 112Z" fill="#B07A3C" {W(3)}/><ellipse cx="64" cy="84" rx="36" ry="8" fill="#D9A066" {W(3)}/>'
    f'<ellipse cx="64" cy="84" rx="20" ry="4" fill="none" stroke="#B07A3C" stroke-width="2"/>'
    f'<path d="M48 82 Q44 60 52 50 H76 Q84 60 80 82Z" fill="#E8D3B0" {W(3.2)}/>'
    f'<path d="M24 54 Q26 18 64 16 Q102 18 104 54 Q64 64 24 54Z" fill="#B8703C" {W(3.4)}/>'
    f'<path d="M40 30 q6 4 4 10 M84 28 q-4 6 0 10" fill="none" stroke="#D99A60" stroke-width="3" stroke-linecap="round"/>'
    + f(64, 68, d=7, k=0.55) +
    f'<path d="M98 80 Q112 70 118 78 Q110 90 98 80Z" fill="#6FBF4A" {W(2.2)}/><circle cx="22" cy="80" r="5" fill="#E8303A" {W(2)}/>')

I["stepashkin-izostudia-khimki"] = ("#FFF5F0", "#F09A7A",
    "банка из-под варенья, в которой кисти стоят, как букет цветов",
    "кончики кистей в разных красках распустились лепестками",
    f'<path d="M36 64 L36 112 Q36 118 42 118 H86 Q92 118 92 112 L92 64Z" fill="#DDF3FF" opacity=".9" {W(3.2)}/>'
    f'<rect x="32" y="58" width="64" height="10" rx="4" fill="#C7E6FF" {W(2.6)}/>'
    f'<path d="M38 92 H90 V112 Q90 116 86 116 H42 Q38 116 38 112Z" fill="#9FC9F0" opacity=".7"/>'
    + "".join(f'<path d="M{x0} 112 L{x1} {y1}" stroke="#C98B4A" stroke-width="4" stroke-linecap="round"/>'
              f'<ellipse cx="{x1}" cy="{y1-6}" rx="6" ry="10" fill="{c}" {W(2)} transform="rotate({r} {x1} {y1-6})"/>'
              for x0, x1, y1, r, c in [(48, 30, 30, -30, "#E8434A"), (56, 50, 18, -10, "#FFD23F"), (64, 70, 16, 8, "#7CD26E"), (72, 92, 26, 28, "#4F86E8"), (80, 108, 44, 48, "#B48AF0")]) +
    f(64, 82, d=8, k=0.6))

I["alkhimik-khoroshevskaya"] = ("#DDF5F3", "#3E9C96",
    "глиняный горшочек, превратившийся в золото",
    "сияет на гончарном круге, и из него сыплются искры, как у алхимика",
    f'<ellipse cx="64" cy="112" rx="42" ry="9" fill="#7C8BA1" {W(3)}/>'
    f'<path d="M36 108 Q24 80 40 62 L42 50 H86 L88 62 Q104 80 92 108Z" fill="#F2C12E" {W(3.4)}/>'
    f'<ellipse cx="64" cy="50" rx="24" ry="6" fill="#FFE36B" {W(3)}/>'
    f'<path d="M44 76 Q48 66 56 64" fill="none" stroke="#FFF7C2" stroke-width="5" stroke-linecap="round"/>'
    + f(66, 86, d=8, k=0.65) +
    "".join(sparkle(x, y, r, c) for x, y, r, c in [(50, 30, 6, "#FFE36B"), (70, 18, 7, "#fff"), (88, 32, 5, "#FFE36B"), (30, 44, 4, "#fff"), (102, 50, 4, "#fff")]))

I["glinka-biryuzova"] = ("#FFF0DB", "#D99A50",
    "мягкий ком рыжей глины с отпечатком детской ладошки",
    "лежит на гончарном круге и радуется, что его сейчас превратят в чашку",
    f'<ellipse cx="64" cy="108" rx="48" ry="12" fill="#A9B6C9" {W(3)}/><ellipse cx="64" cy="104" rx="44" ry="10" fill="#C7D1E0" {W(2.6)}/>'
    f'<path d="M24 102 Q18 60 64 50 Q110 60 104 102 Q64 112 24 102Z" fill="#C8693A" {W(3.4)}/>'
    f'<path d="M52 66 Q50 54 54 50 M60 64 V46 M68 64 V46 M76 66 Q78 54 74 50 M46 74 Q38 70 36 62" fill="none" stroke="#9E4E26" stroke-width="5" stroke-linecap="round"/>'
    f'<ellipse cx="60" cy="76" rx="14" ry="9" fill="#9E4E26"/>'
    + f(64, 90, d=9, k=0.7) +
    f'<path d="M14 92 q-6 -8 0 -16 M114 92 q6 -8 0 -16" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')

I["zeleny-mayak-molodogvardeyskaya"] = ("#E7F9E7", "#4CAF6A",
    "капля зелёной краски в капитанской фуражке",
    "командует с горки из баночек, указывая кисточкой вперёд",
    "".join(f'<rect x="{x}" y="{y}" width="26" height="20" rx="4" fill="{c}" {W(2.6)}/><rect x="{x-2}" y="{y-5}" width="30" height="7" rx="3" fill="#fff" {W(2)}/>'
            for x, y, c in [(18, 98, "#E8434A"), (50, 98, "#FFD23F"), (82, 98, "#4F86E8"), (34, 74, "#B48AF0"), (66, 74, "#FF8C3A")]) +
    f'<path d="M64 14 Q40 46 44 56 Q50 70 64 70 Q78 70 84 56 Q88 46 64 14Z" fill="#3FBF5A" {W(3.2)}/>'
    f'<path d="M48 34 Q64 22 80 34 L80 40 H48Z" fill="#fff" {W(2.6)}/><rect x="44" y="38" width="40" height="6" rx="3" fill="#2F2A60" {W(2)}/>'
    f'<circle cx="64" cy="31" r="3" fill="#FFD23F"/>' + f(64, 54, d=7, k=0.55) +
    f'<path d="M84 52 L106 36" stroke="#C98B4A" stroke-width="4" stroke-linecap="round"/><path d="M106 36 l6 -4" stroke="#3FBF5A" stroke-width="6" stroke-linecap="round"/>')

I["igra-stolov-garibaldi"] = ("#FFF8E8", "#E8C26A",
    "домашняя лапша, развешанная сушиться на деревянной палочке",
    "дети только что сами её раскатали, а мука ещё летит облачком",
    f'<path d="M14 30 L114 22" stroke="#B07A3C" stroke-width="7" stroke-linecap="round"/><path d="M14 30 L114 22" fill="none" {W(1.6)}/>'
    + "".join(f'<path d="M{x} {30-(x-14)*0.08:.0f} Q{x-4} {64+(x%3)*6} {x+2} {96+(x%5)*3}" fill="none" stroke="#FFE7A8" stroke-width="6" stroke-linecap="round"/>'
              f'<path d="M{x} {30-(x-14)*0.08:.0f} Q{x-4} {64+(x%3)*6} {x+2} {96+(x%5)*3}" fill="none" {W(1.4)}/>' for x in range(26, 108, 9)) +
    f(66, 52, d=8, k=0.6) +
    f'<ellipse cx="30" cy="112" rx="18" ry="8" fill="#fff" opacity=".9"/><ellipse cx="46" cy="106" rx="10" ry="6" fill="#fff" opacity=".8"/>'
    f'<path d="M84 104 h30" stroke="#C98B4A" stroke-width="8" stroke-linecap="round"/><path d="M80 104 h4 M114 104 h4" stroke="#8B5A2B" stroke-width="5" stroke-linecap="round"/>')

I["goncharnaya-studiya-1-garibaldi"] = ("#E6EEFF", "#6A86D0",
    "глиняная ваза в форме цифры 1 с носиком-горлышком",
    "вырастает прямо из гончарного круга, а мокрые руки мастера её подравнивают",
    f'<ellipse cx="64" cy="112" rx="46" ry="10" fill="#7C8BA1" {W(3)}/><ellipse cx="64" cy="108" rx="40" ry="8" fill="#A9B6C9" {W(2.6)}/>'
    f'<path d="M50 106 Q46 100 54 98 V42 L40 52 L36 40 L62 18 H76 V98 Q84 100 80 106Z" fill="#D9895A" {W(3.4)}/>'
    f'<path d="M58 30 L70 22" stroke="#F2B48A" stroke-width="4" stroke-linecap="round"/>'
    + f(65, 64, d=5, k=0.45) +
    f'<path d="M12 78 Q26 70 44 76 Q50 80 46 86 L16 90Z" fill="#FFD9B8" {W(2.6)}/><path d="M116 78 Q102 70 84 76 Q78 80 82 86 L112 90Z" fill="#FFD9B8" {W(2.6)}/>')

I["family-woods-nametkina"] = ("#F2FBE6", "#8FBF4A",
    "деревянная машинка, собранная из брусков и катушек-колёс",
    "малыш везёт её за верёвочку, а в кузове едут стружки",
    f'<rect x="38" y="64" width="62" height="24" rx="3" fill="#E8C08A" {W(3)}/>'
    f'<rect x="76" y="46" width="24" height="20" rx="3" fill="#D9A066" {W(3)}/><rect x="82" y="50" width="12" height="10" fill="#BFE8FF" {W(2)}/>'
    f'<path d="M44 72 h28 M44 80 h28" stroke="#C9935A" stroke-width="2"/>'
    f'<path d="M46 64 q4 -10 10 -4 q4 -8 10 -2 q4 -6 8 2" fill="#F7DCA8" {W(2)}/>'
    + "".join(f'<circle cx="{x}" cy="92" r="10" fill="#B07A3C" {W(3)}/><circle cx="{x}" cy="92" r="3.4" fill="#F2D3A0"/>' for x in (52, 88)) +
    f(88, 74, d=0.1, k=0.0001, blush=False) + eye(84, 74, 0.5) + eye(94, 74, 0.5) +
    f'<path d="M38 76 Q30 86 22 82" fill="none" stroke="#E8434A" stroke-width="2.4"/>'
    + kid(18, 70, k=0.6, hair="#F2C14E") +
    f'<path d="M10 80 Q18 76 26 80 L28 98 L8 98Z" fill="#45A8F0" {W(2.4)}/><path d="M12 98 v10 M24 98 v10" {W(3)}/>'
    f'<path d="M0 110 H128" stroke="#7FA84A" stroke-width="3"/>')

I["naukograd-vvedenskogo"] = ("#E9F0FF", "#3F63C4",
    "маятник Ньютона — пять стальных шариков на ниточках",
    "крайний шарик отлетел и ударил, а остальные дружно зажмурились",
    f'<path d="M14 22 H114 M20 22 V110 M108 22 V110 M14 110 H114" fill="none" stroke="#C7CED8" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M14 22 H114 M20 22 V110 M108 22 V110 M14 110 H114" fill="none" {W(1.6)}/>'
    + "".join(f'<path d="M{x} 22 L{x} 76" {W(1.8)}/><circle cx="{x}" cy="80" r="9" fill="#DCE3EE" {W(2.6)}/>' for x in (46, 64, 82)) +
    f'<path d="M28 22 L22 70" {W(1.8)}/><circle cx="21" cy="74" r="9" fill="#DCE3EE" {W(2.6)}/>'
    f'<path d="M100 22 L100 76" {W(1.8)}/><circle cx="100" cy="80" r="9" fill="#DCE3EE" {W(2.6)}/>'
    + "".join(f'<path d="M{x-5} 79 q2 -2 4 0 M{x+1} 79 q2 -2 4 0" fill="none" {W(1.6)}/><path d="M{x-2} 84 q2 1.6 4 0" fill="none" {W(1.4)}/>' for x in (46, 64, 82, 100)) +
    eye(18, 72, 0.35) + eye(24, 72, 0.35) +
    f'<path d="M30 74 l6 -2 M30 80 l6 0" stroke="#FFD23F" stroke-width="2.4" stroke-linecap="round"/>')

I["iq007-chongarsky"] = ("#FFEAF4", "#E86FA6",
    "розовый мозг-силач с румяными щёчками",
    "поднимает над собой гантель, вокруг — капельки пота и звёздочки",
    f'<path d="M30 76 Q20 56 36 46 Q38 30 56 32 Q64 22 76 30 Q94 28 96 46 Q110 56 100 76 Q96 92 80 92 H48 Q32 92 30 76Z" fill="#FF9CC2" {W(3.4)}/>'
    f'<path d="M64 34 V90 M44 52 q8 4 6 14 M84 50 q-8 6 -4 14 M50 78 q6 -4 12 0 M70 78 q6 -6 14 -2" fill="none" stroke="#E8689A" stroke-width="3" stroke-linecap="round"/>'
    + f(64, 64, d=10, k=0.7) +
    f'<path d="M36 46 L26 24 M92 46 L102 24" {W(3.4)}/>'
    f'<path d="M18 22 H110" stroke="#7C8BA1" stroke-width="6" stroke-linecap="round"/>'
    f'<rect x="8" y="10" width="12" height="24" rx="3" fill="#2F2A60" {W(2)}/><rect x="108" y="10" width="12" height="24" rx="3" fill="#2F2A60" {W(2)}/>'
    f'<path d="M30 92 v16 M98 92 v16" {W(3.4)}/><path d="M24 110 h12 M92 110 h12" {W(3.4)}/>'
    f'<path d="M108 52 q4 6 0 9 q-4 -3 0 -9Z" fill="#BFE8FF" {W(1.6)}/>')

I["cpm-robotics-dorogomilovskaya"] = ("#FFF9DA", "#E8B930",
    "колёсный робот-машинка с датчиками-глазами снизу",
    "едет по чёрной извилистой линии трассы на белом поле",
    f'<rect x="6" y="40" width="116" height="80" rx="4" fill="#fff" {W(2.6)}/>'
    f'<path d="M14 108 Q30 60 56 84 Q80 106 96 70 Q104 52 116 50" fill="none" stroke="#2F2A60" stroke-width="7" stroke-linecap="round"/>'
    f'<rect x="40" y="56" width="44" height="30" rx="8" fill="#45A8F0" {W(3)}/>'
    f'<rect x="44" y="40" width="36" height="20" rx="6" fill="#E8434A" {W(2.6)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="10" height="16" rx="3" fill="#2F2A60" {W(2)}/>' for x, y in [(32, 58), (82, 58)]) +
    eye(54, 70, 0.6) + eye(70, 70, 0.6) +
    f'<path d="M58 78 q4 3 8 0" fill="none" {W(2)}/>'
    f'<circle cx="56" cy="48" r="3" fill="#FFD23F"/><circle cx="68" cy="48" r="3" fill="#7CD26E"/>'
    f'<path d="M48 88 l-4 6 M76 88 l4 6" stroke="#E8434A" stroke-width="2.4" opacity=".7"/>')

I["polycent-maroseyka"] = ("#E6FFF0", "#47B97A",
    "серебристый школьный циркуль с карандашом на одной ножке",
    "мальчик держит его за макушку и чертит идеальный круг",
    f'<circle cx="62" cy="80" r="34" fill="none" stroke="#3566C2" stroke-width="3" stroke-dasharray="210 30"/>'
    f'<circle cx="62" cy="80" r="3" fill="{O}"/>'
    f'<path d="M62 80 L72 30 L96 78" fill="none" stroke="#C7CED8" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
    f'<path d="M62 80 L72 30 L96 78" fill="none" {W(1.6)}/>'
    f'<rect x="92" y="70" width="8" height="18" rx="2" fill="#FFD23F" {W(2)} transform="rotate(-26 96 78)"/>'
    f'<circle cx="72" cy="28" r="6" fill="#E8434A" {W(2.2)}/>' + f(74, 46, d=4, k=0.36) +
    kid(98, 22, k=0.6, hair="#3A2414") + f'<path d="M90 28 L76 28" {W(2.6)}/>')

I["lisya-nora-kozhukhovskaya"] = ("#FFF2DC", "#E89B3C",
    "уютная нора в зелёном холме с круглой красной дверцей",
    "из приоткрытой дверцы торчит пушистый рыжий хвост с белым кончиком",
    f'<path d="M0 110 Q8 40 64 34 Q120 40 128 110 V128 H0Z" fill="#7CC85A" {W(3.2)}/>'
    f'<path d="M20 70 q6 -6 12 0 M96 60 q6 -6 12 0" fill="none" stroke="#5AA845" stroke-width="3" stroke-linecap="round"/>'
    f'<circle cx="64" cy="84" r="28" fill="#6E431D" {W(3.2)}/>'
    f'<path d="M64 56 A28 28 0 0 1 92 84 L64 84Z" fill="#E8434A" {W(2.8)}/><circle cx="82" cy="78" r="3" fill="#FFD23F" {W(1.6)}/>'
    f'<path d="M50 96 Q30 88 26 104 Q24 118 40 114 Q52 110 58 100Z" fill="#F08A3A" {W(3)}/>'
    f'<path d="M26 104 Q24 118 40 114 Q30 110 32 102Z" fill="#fff" {W(2)}/>'
    + eye(52, 78, 0.6) + eye(62, 76, 0.6) +
    f'<circle cx="64" cy="18" r="8" fill="#FFE36B"/>')

I["kot-filius-andropova"] = ("#EAE6FF", "#7F6AD6",
    "серый полосатый кот-мастер в синем фартуке и круглых очках",
    "стоит за столом мастерской и гордо показывает слепленную им вазочку",
    f'<path d="M30 46 L36 20 L50 36 M98 46 L92 20 L78 36" fill="#A9B0C2" {W(3)}/>'
    f'<ellipse cx="64" cy="50" rx="34" ry="28" fill="#A9B0C2" {W(3.2)}/>'
    f'<path d="M54 26 v8 M64 24 v10 M74 26 v8" stroke="#7C8399" stroke-width="3" stroke-linecap="round"/>'
    f'<circle cx="52" cy="50" r="9" fill="none" {W(2.4)}/><circle cx="76" cy="50" r="9" fill="none" {W(2.4)}/><path d="M61 50 h6" {W(2)}/>'
    + eye(52, 50, 0.55) + eye(76, 50, 0.55) +
    f'<path d="M60 62 l4 3 4 -3" fill="none" {W(2)}/><path d="M34 60 h-14 M34 66 h-12 M94 60 h14 M94 66 h12" {W(1.6)}/>'
    f'<path d="M36 78 Q64 70 92 78 L96 120 H32Z" fill="#3D6FD8" {W(3)}/><rect x="50" y="92" width="28" height="14" rx="3" fill="#5E8FF0" {W(2)}/>'
    f'<path d="M90 92 Q104 86 108 76" fill="none" stroke="#A9B0C2" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M102 76 Q98 60 108 56 Q118 60 114 76Z" fill="#D9895A" {W(2.4)}/>')

I["palitra-kondrashinoy-yakornaya"] = ("#E2F5FF", "#2F9AD6",
    "белая чайка-художник с жёлтым клювом",
    "держит кисть в клюве и рисует волны прямо на воде затона",
    f'<path d="M0 90 Q16 82 32 90 T64 90 T96 90 T128 90 V128 H0Z" fill="#3E9BE0" {W(2.6)}/>'
    f'<path d="M10 104 Q26 96 42 104 T74 104" fill="none" stroke="#B48AF0" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M40 116 Q56 108 72 116 T104 116" fill="none" stroke="#FFD23F" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M14 40 Q40 20 58 46 Q76 20 108 34 Q84 38 74 56 Q64 72 50 60 Q34 46 14 40Z" fill="#fff" {W(3.2)}/>'
    f'<path d="M14 40 Q24 36 30 42 M108 34 Q100 32 96 38" fill="none" stroke="#7C8BA1" stroke-width="3"/>'
    f'<circle cx="62" cy="54" r="12" fill="#fff" {W(2.8)}/>' + eye(60, 52, 0.55) +
    f'<path d="M68 58 L80 62 L68 64Z" fill="#FFB13B" {W(2)}/>'
    f'<path d="M78 62 L94 90" stroke="#C98B4A" stroke-width="3.4" stroke-linecap="round"/><path d="M94 90 l3 5" stroke="#E8434A" stroke-width="5" stroke-linecap="round"/>')

I["palitra-kondrashinoy-andropova"] = ("#F3FFE6", "#9CC94A",
    "радужная лужа из пролитых красок",
    "малыш в жёлтых резиновых сапогах прыгает в неё, и брызги летят цветными каплями",
    f'<ellipse cx="64" cy="104" rx="56" ry="16" fill="#B48AF0" {W(3)}/><ellipse cx="60" cy="102" rx="42" ry="11" fill="#45A8F0"/>'
    f'<ellipse cx="58" cy="100" rx="28" ry="7" fill="#7CD26E"/><ellipse cx="56" cy="99" rx="14" ry="4" fill="#FFD23F"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" {W(1.6)}/>' for x, y, r, c in [(20, 80, 5, "#E8434A"), (100, 76, 6, "#FF8C3A"), (28, 64, 4, "#45A8F0"), (96, 60, 4, "#7CD26E")]) +
    kid(64, 34, k=0.75, hair="#5A3A22") +
    f'<path d="M54 44 Q64 40 74 44 L76 64 L52 64Z" fill="#E8434A" {W(2.4)}/>'
    f'<path d="M54 46 L42 34 M74 46 L86 34" {W(2.8)}/>'
    f'<path d="M54 64 h10 v20 h-14 v-6 h4Z M66 64 h10 v14 h4 v6 h-14Z" fill="#FFD23F" {W(2.4)}/>')

I["vozrozhdenie-eletskaya"] = ("#FDF3E3", "#D2A26A",
    "старинная фреска на кусочке штукатурки с нарисованным ангелочком",
    "юная художница в берете кисточкой бережно подновляет ей краски",
    f'<path d="M14 18 L94 12 L102 50 L96 100 L20 106 L10 64Z" fill="#F2D9B0" {W(3.2)}/>'
    f'<path d="M30 30 L84 26 L88 90 L32 94Z" fill="#E8C49A"/>'
    f'<circle cx="58" cy="52" r="12" fill="#FFD9B8" {W(2.4)}/>' + f(58, 54, d=4, k=0.36) +
    f'<path d="M46 50 Q34 40 32 56 Q40 60 46 56 M70 50 Q82 40 84 56 Q76 60 70 56" fill="#fff" {W(2)}/>'
    f'<path d="M48 64 Q58 60 68 64 L72 86 L44 86Z" fill="#7FB3E8" {W(2.4)}/>'
    f'<circle cx="58" cy="38" r="9" fill="none" stroke="#E8B83A" stroke-width="2.4"/>'
    f'<path d="M24 40 l10 4 M86 80 l8 6" stroke="#C49A6A" stroke-width="2"/>'
    + kid(108, 82, k=0.6, hair="#7A4A22") +
    f'<path d="M98 74 Q108 64 118 74Z" fill="#E8303A" {W(2)}/>'
    f'<path d="M100 90 L82 76" stroke="#C98B4A" stroke-width="3" stroke-linecap="round"/>')

I["zyablik-art-orekhovy"] = ("#E8F4FF", "#86B8E8",
    "зяблик с розово-рыжей грудкой и голубой шапочкой",
    "сидит на краю альбома и рисует кисточкой в клюве ветку с ягодками",
    f'<rect x="12" y="78" width="104" height="40" rx="3" fill="#fff" {W(2.6)}/>'
    f'<path d="M24 108 Q50 94 80 100" fill="none" stroke="#8B5A2B" stroke-width="3" stroke-linecap="round"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3.4" fill="#E8434A"/>' for x, y in [(40, 98), (56, 94), (68, 100)]) +
    f'<path d="M78 40 Q100 30 112 50 Q110 64 98 74 L68 78 Q56 60 78 40Z" fill="#8B6A4A" {W(3)}/>'
    f'<path d="M70 56 Q84 52 90 74 L70 78Z" fill="#F29A7A" {W(2.4)}/>'
    f'<path d="M78 40 Q90 34 100 40 Q94 46 84 48Z" fill="#7FA8D8" {W(2.2)}/>'
    f'<path d="M98 50 Q112 48 120 58 L104 64Z" fill="#fff" {W(2)}/>' + eye(80, 50, 0.5) +
    f'<path d="M72 54 L62 56 L70 60Z" fill="#B0B8C8" {W(1.8)}/><path d="M62 57 L42 70" stroke="#C98B4A" stroke-width="3" stroke-linecap="round"/>'
    f'<path d="M80 78 v8 M90 78 v8" {W(2.4)}/>')

I["rodnik-yasenevaya"] = ("#E3FBFF", "#4FC0D8",
    "родник, бьющий из груды круглых камней",
    "малыш подставил под струйку грязную кисточку, и вода стала радужной",
    f'<path d="M0 110 Q64 98 128 110 V128 H0Z" fill="#7CC85A" {W(2.4)}/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{c}" {W(2.6)}/>' for x, y, rx, ry, c in
              [(30, 96, 18, 12, "#A9B6C9"), (58, 100, 16, 10, "#C7D1E0"), (42, 78, 16, 12, "#B9C3D6"), (20, 70, 12, 10, "#C7D1E0")]) +
    f'<path d="M50 74 Q74 60 88 84 Q94 100 92 110" fill="none" stroke="#5EC2F2" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M50 74 Q74 60 88 84" fill="none" stroke="#DDF6FF" stroke-width="3" stroke-linecap="round"/>'
    f'<path d="M88 94 Q96 104 92 116" fill="none" stroke="#B48AF0" stroke-width="4" stroke-linecap="round"/><path d="M92 92 Q102 102 100 114" fill="none" stroke="#F58CB8" stroke-width="4" stroke-linecap="round"/>'
    + f(42, 78, d=5, k=0.42) +
    kid(104, 50, k=0.65, hair="#E8B04A") + f'<path d="M96 60 L86 80" {W(2.6)}/><path d="M86 80 l-2 6" stroke="#E8434A" stroke-width="5" stroke-linecap="round"/>')

I["masterskaya-shipilovskaya"] = ("#F0F0F0", "#8E99A8",
    "синие слесарные тиски с винтовой ручкой",
    "крепко зажали деревянный брусок, а из бруска мастерят кораблик",
    f'<rect x="10" y="98" width="108" height="12" rx="3" fill="#C98B4A" {W(2.6)}/>'
    f'<rect x="30" y="62" width="24" height="36" rx="3" fill="#3566C2" {W(3)}/><rect x="74" y="62" width="24" height="36" rx="3" fill="#3566C2" {W(3)}/>'
    f'<rect x="54" y="50" width="20" height="30" fill="#E8C08A" {W(2.6)}/>'
    f'<path d="M52 50 L76 50 L70 40 L58 40Z" fill="#D9A066" {W(2.2)}/><path d="M64 40 V22 L76 32 L64 34" fill="#fff" {W(2.2)}/>'
    f'<path d="M98 80 H118 M118 70 V90" {W(4)}/><circle cx="118" cy="70" r="4" fill="#E8434A" {W(1.8)}/><circle cx="118" cy="90" r="4" fill="#E8434A" {W(1.8)}/>'
    + f(42, 80, d=4, k=0.4) + f(86, 80, d=4, k=0.4))

I["moy-gnom-moskvorechye"] = ("#FFF0F5", "#F38BB0",
    "пластиковые стаканчики-вкладыши всех цветов радуги",
    "малыш построил из них башню выше себя и тянется поставить последний",
    "".join(f'<path d="M{64-w} {y} L{64-w+3} {y-14} H{64+w-3} L{64+w} {y}Z" fill="{c}" {W(2.4)}/>' for y, w, c in
            [(116, 22, "#E8434A"), (102, 20, "#FF8C3A"), (88, 18, "#FFD23F"), (74, 16, "#7CD26E"), (60, 14, "#45A8F0"), (46, 12, "#B48AF0")]) +
    f(64, 106, d=6, k=0.45, blush=False) +
    kid(100, 92, k=0.75, hair="#F2C14E") +
    f'<path d="M92 102 Q100 98 108 102 L110 120 L90 120Z" fill="#4CC38A" {W(2.4)}/>'
    f'<path d="M92 104 L78 22" {W(2.8)}/>'
    f'<path d="M66 30 L68 20 H80 L82 30Z" fill="#F58CB8" {W(2.2)}/>')

