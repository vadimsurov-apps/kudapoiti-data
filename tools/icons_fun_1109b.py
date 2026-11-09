"""Иконки робота fun (2026-11-09, утро, поиск по районам): 38 мест из tools/add_fun_1109b.py.
Каждая придумана и нарисована отдельно (правило абсолютной уникальности). Сверено со всеми листами icons-catalog
(01–45) и icons-src/subjects.txt. Заняты и НЕ брать: мастихин, гипсовые тела, скетчбук, бескозырка, подъёмный мост,
маяк, гонг, кодовый замок, шифровальный диск, связка ключей, свиток с печатью, банка с червячками, морской форт.
Запуск: python3 tools/icons_fun_1109b.py [id ...]  (печатает строки для subjects.txt)"""
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

# ---------------- игровые комнаты ----------------
I["parovozovo-chongarsky"] = ("#FFF4D6", "#F2B94B",
    "жёлтый толокар-машинка с красным рулём и глазками-фарами",
    "малыш сидит в нём и отталкивается ножками по полу игровой, сзади летят пылинки-облачка",
    f'<rect x="0" y="104" width="128" height="26" fill="#F7D9A6" {W(2.4)}/>'
    f'<path d="M22 96 Q20 70 40 66 L84 64 Q104 64 106 84 L106 96Z" fill="#FFD23F" {W(3.2)}/>'
    f'<circle cx="38" cy="100" r="9" fill="#5B4A6E" {W(2.8)}/><circle cx="92" cy="100" r="9" fill="#5B4A6E" {W(2.8)}/>'
    f'<circle cx="38" cy="100" r="3" fill="#fff"/><circle cx="92" cy="100" r="3" fill="#fff"/>'
    + f(92, 80, d=6, k=0.6) +
    f'<path d="M66 64 L70 44" {W(3)}/><ellipse cx="72" cy="42" rx="10" ry="4" fill="#E8303A" {W(2.6)}/>'
    + kid(56, 40, k=0.9, hair="#C9762E") +
    f'<path d="M48 52 Q46 60 52 64 M64 52 Q70 50 72 44" fill="none" {W(3)}/>'
    f'<path d="M50 96 Q44 108 36 112" fill="none" {W(3.4)}/><ellipse cx="34" cy="113" rx="5" ry="3" fill="{O}"/>'
    f'<circle cx="14" cy="104" r="5" fill="#fff" opacity=".8"/><circle cx="8" cy="96" r="3.5" fill="#fff" opacity=".8"/>')

I["nora-bratca-krolika-delegatskaya"] = ("#E8F8E0", "#86C96A",
    "зелёный холмик-нора с круглой красной дверцей",
    "из приоткрытой дверцы торчат два длинных серых уха и выглядывает любопытный нос, у порога — морковный коврик",
    f'<path d="M-4 112 Q64 10 132 112 V130 H-4Z" fill="#6DBB4F" {W(3.2)}/>'
    f'<path d="M20 94 Q30 88 36 94 M90 70 Q98 64 104 72 M54 40 Q60 36 66 40" fill="none" stroke="#3E8A33" stroke-width="2.4" stroke-linecap="round"/>'
    f'<circle cx="64" cy="86" r="24" fill="#5A3A22" {W(3)}/>'
    f'<path d="M64 62 A24 24 0 0 1 88 86 L64 86Z" fill="#E2483F" {W(2.8)}/><circle cx="80" cy="80" r="2.6" fill="#FFD23F" {W(1.6)}/>'
    f'<path d="M50 70 Q42 34 50 24 Q58 34 56 68Z" fill="#C7C7D6" {W(2.8)}/><path d="M50 62 Q48 40 51 32" fill="none" stroke="#F4A6C0" stroke-width="3" stroke-linecap="round"/>'
    f'<path d="M58 68 Q60 36 70 30 Q72 44 64 70Z" fill="#C7C7D6" {W(2.8)}/><path d="M62 64 Q64 44 68 38" fill="none" stroke="#F4A6C0" stroke-width="3" stroke-linecap="round"/>'
    f'<ellipse cx="54" cy="82" rx="12" ry="10" fill="#D9D9E6" {W(2.8)}/>'
    f'{eye(50,80,0.6)}<circle cx="58" cy="86" r="2.6" fill="#F06292"/>'
    f'<rect x="44" y="108" width="40" height="7" rx="3.5" fill="#FF9A3C" {W(2.4)}/><path d="M80 108 l6 -6 M82 108 l8 -2" {W(2)}/>')

I["lentochny-labirint-vdnh"] = ("#F4E8FF", "#B392F0",
    "занавес-лабиринт из длинных разноцветных атласных лент",
    "девочка в жёлтом платье раздвигает ленты руками и выглядывает, смеясь, ленты колышутся",
    f'<rect x="10" y="12" width="108" height="8" rx="4" fill="#8C6BC8" {W(2.8)}/>'
    + "".join(f'<path d="M{x} 20 Q{x+5} 60 {x-2} 118" fill="none" stroke="{c}" stroke-width="9" stroke-linecap="round"/>'
              for x, c in [(18, "#FF5C8A"), (30, "#FFB13B"), (42, "#FFE14D"), (88, "#4CC38A"), (100, "#45A8F0"), (112, "#7B5BE0")]) +
    f'<path d="M54 20 Q44 60 36 116 M76 20 Q86 60 94 116" fill="none" stroke="#FF8A3D" stroke-width="9" stroke-linecap="round"/>'
    + kid(64, 62, k=1.05, hair="#4A2C1A") +
    f'<path d="M50 78 Q64 74 78 78 L84 118 L44 118Z" fill="#FFD23F" {W(3)}/>'
    f'<path d="M50 80 Q40 72 40 60 M78 80 Q88 72 88 60" fill="none" {W(3.4)}/>'
    f'<circle cx="40" cy="58" r="4.5" fill="#FFD9B8" {W(2.2)}/><circle cx="88" cy="58" r="4.5" fill="#FFD9B8" {W(2.2)}/>')

I["toy-berry-lefortovo"] = ("#E9E4FF", "#6E63C9",
    "пухлая ягода ежевика с зелёной шапочкой-чашелистиком",
    "весело съезжает по жёлтой волнистой горке, раскинув листочки-ручки",
    f'<path d="M14 34 H40 Q52 34 56 50 Q64 80 84 92 Q100 100 120 100 L120 112 Q96 114 78 104 Q52 90 46 56 Q42 46 30 46 H14Z" fill="#FFD23F" {W(3)}/>'
    f'<path d="M14 46 V118 M30 46 V118" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="7.5" fill="#4B2A6E" {W(2.2)}/><circle cx="{x-2}" cy="{y-2.5}" r="2" fill="#B9A3E8"/>'
              for x, y in [(70, 50), (84, 48), (98, 52), (64, 62), (78, 62), (92, 62), (104, 64), (70, 74), (84, 76), (98, 74)]) +
    f'<path d="M72 42 Q84 26 96 42 Q86 36 72 42Z" fill="#58C26B" {W(2.4)}/><path d="M84 34 V24" {W(2.6)}/>'
    + f(84, 62, d=8, k=0.75) +
    f'<path d="M62 60 Q50 52 46 40" fill="none" stroke="#58C26B" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M106 60 Q116 50 118 40" fill="none" stroke="#58C26B" stroke-width="4" stroke-linecap="round"/>'
    + sparkle(30, 26, 4) + sparkle(110, 26, 3))

I["skazka-tut-volgogradsky"] = ("#FFE4EE", "#EE7FA6",
    "раскрытая книга сказок, стоящая домиком-шалашом",
    "в книжном домике горит окошко, из трубы-закладки идёт дымок-завиток, у входа ждёт крошечная тропинка",
    f'<path d="M0 108 Q64 98 128 108 V130 H0Z" fill="#B8E07A" {W(2.4)}/>'
    f'<path d="M64 26 L18 98 L64 92Z" fill="#7FD0F5" {W(3.2)}/><path d="M64 26 L110 98 L64 92Z" fill="#FFB86B" {W(3.2)}/>'
    f'<path d="M64 26 L24 94 M64 26 L104 94" fill="none" stroke="#fff" stroke-width="2"/>'
    f'<path d="M34 76 L52 74 M38 68 L54 66 M86 66 L74 64 M90 74 L76 72" {W(1.8)}/>'
    f'<path d="M70 30 V14 L76 18 L82 14 V34" fill="#E2483F" {W(2.4)}/>'
    f'<path d="M80 12 Q86 6 82 2 Q90 4 88 -2" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>'
    f'<path d="M54 92 V76 Q64 64 74 76 V92Z" fill="#5A3A22" {W(2.8)}/>'
    f'<path d="M58 80 Q64 72 70 80 V88 H58Z" fill="#FFE066"/>'
    + f(64, 52, d=8, k=0.7) +
    f'<path d="M64 92 Q58 104 66 116" fill="none" stroke="#E8C79A" stroke-width="6" stroke-linecap="round"/>')

I["apelsinka-veshnyakovskaya"] = ("#E0F4FF", "#5DB3E8",
    "долька апельсина-качалка с белыми прожилками",
    "двое малышей качаются на ней, как на балансире, один взлетел вверх и радуется",
    f'<path d="M14 92 Q64 132 114 92Z" fill="#FF9A2E" {W(3.2)}/>'
    f'<path d="M22 94 Q64 124 106 94" fill="#FFC56B" {W(2)}/>'
    + "".join(f'<path d="M64 98 L{x} {y}" stroke="#fff" stroke-width="2.4"/>' for x, y in [(34, 100), (48, 108), (64, 112), (80, 108), (94, 100)]) +
    f'<path d="M10 90 L118 74" {W(5)}/><path d="M10 90 L118 74" stroke="#FF8A1F" stroke-width="2.6"/>'
    + f(64, 108, d=8, k=0.6, mouth=False) +
    kid(26, 72, k=0.75, hair="#E0A030") + kid(104, 52, k=0.75, hair="#5A3A22") +
    f'<path d="M96 60 L92 46 M112 60 L118 46" {W(3)}/>'
    + sparkle(116, 30, 4) + sparkle(88, 32, 3))

I["pugovka-oblaka"] = ("#E6FFF8", "#49C3A6",
    "большая малиновая пуговица с четырьмя дырочками",
    "сидит на пушистом облаке, а через её дырочки продета нитка, которую она, как скакалку, перекидывает через себя",
    f'<path d="M14 100 Q12 84 30 86 Q34 70 54 76 Q66 64 82 76 Q102 70 104 88 Q120 88 114 104Z" fill="#fff" {W(3)}/>'
    f'<path d="M40 62 Q30 30 64 18 Q98 30 88 62" fill="none" stroke="#FFB300" stroke-width="3.4" stroke-linecap="round"/>'
    f'<circle cx="64" cy="66" r="28" fill="#E0457B" {W(3.2)}/><circle cx="64" cy="66" r="21" fill="none" stroke="#B8285C" stroke-width="2.6"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#7A1840"/>' for x, y in [(55, 57), (73, 57), (55, 75), (73, 75)]) +
    f'<path d="M55 57 L40 62 M73 57 L88 62" stroke="#FFB300" stroke-width="3" stroke-linecap="round"/>'
    + f(64, 66, d=5, k=0.55) + sparkle(20, 40, 4) + sparkle(108, 36, 3))

I["star-lab-zhulebino"] = ("#5B5FC7", "#1E1F4D",
    "жёлтая звёздочка-лаборант в круглых защитных очках",
    "переливает светящуюся голубую жидкость из одной пробирки в другую, над пробирками поднимаются пузырьки",
    f'<path d="M64 18 L76 48 L108 50 L83 70 L92 102 L64 84 L36 102 L45 70 L20 50 L52 48Z" fill="#FFD23F" {W(3.2)}/>'
    f'<circle cx="55" cy="60" r="8" fill="#BDEBFF" {W(2.6)}/><circle cx="73" cy="60" r="8" fill="#BDEBFF" {W(2.6)}/>'
    f'<path d="M63 60 H65" {W(2.4)}/>{eye(55,60,0.55)}{eye(73,60,0.55)}'
    f'<path d="M58 74 Q64 79 70 74" fill="none" {W(2.4)}/>'
    f'<rect x="12" y="68" width="14" height="38" rx="7" fill="#E9F7FF" {W(2.6)}/><rect x="13.5" y="88" width="11" height="16" rx="5" fill="#45E0F0"/>'
    f'<path d="M26 72 Q38 60 104 66" fill="none" stroke="#45E0F0" stroke-width="3" stroke-dasharray="1 5" stroke-linecap="round"/>'
    f'<rect x="102" y="62" width="14" height="40" rx="7" fill="#E9F7FF" {W(2.6)}/><rect x="103.5" y="82" width="11" height="18" rx="5" fill="#45E0F0"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="#9FF4FF" stroke-width="1.8"/>' for x, y, r in [(108, 50, 3), (114, 40, 2.2), (20, 58, 2.6)]) +
    sparkle(34, 24, 3, "#FFF3B0") + sparkle(98, 22, 4, "#FFF3B0"))

I["motor-city-kotelniki"] = ("#D8F6F8", "#3FB6C4",
    "маленькая красная игрушечная машинка, вся в мыльной пене",
    "проезжает через детскую автомойку между двумя вертящимися синими щётками",
    f'<rect x="0" y="106" width="128" height="24" fill="#9AA6B8" {W(2.4)}/>'
    f'<path d="M14 106 V30 H114 V106" fill="none" {W(3.2)}/><rect x="14" y="24" width="100" height="12" rx="4" fill="#FFD23F" {W(3)}/>'
    + "".join(f'<path d="M{x} 40 V104" stroke="#3E6FD8" stroke-width="12" stroke-linecap="round" stroke-dasharray="3 3"/><rect x="{x-7}" y="38" width="14" height="68" rx="7" fill="none" {W(2.4)}/>'
              for x in (26, 102)) +
    f'<path d="M38 102 V88 Q40 76 54 74 L78 74 Q90 76 92 88 V102Z" fill="#E8303A" {W(3)}/>'
    f'<path d="M50 76 L54 64 H76 L80 76Z" fill="#BDEBFF" {W(2.6)}/>'
    f'<circle cx="48" cy="104" r="7" fill="#3B3355"/><circle cx="82" cy="104" r="7" fill="#3B3355"/>'
    + f(65, 90, d=7, k=0.55) +
    "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" {W(1.6)}/>' for x, y, r in [(50, 62, 6), (60, 56, 7), (72, 58, 6), (82, 64, 5), (44, 70, 4)]) +
    "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="#fff" stroke-width="1.8"/>' for x, y, r in [(64, 44, 3), (48, 48, 2.4), (84, 48, 2.6)]))

I["avto-kids-shchelkovo"] = ("#FFE9D6", "#F58A4B",
    "многоэтажный игрушечный гараж-парковка с винтовым пандусом",
    "по спиральному пандусу съезжают три разноцветные машинки, на крыше машет флажок",
    f'<rect x="30" y="30" width="58" height="84" rx="4" fill="#F5F0E6" {W(3.2)}/>'
    + "".join(f'<path d="M30 {y} H88" {W(2.6)}/>' for y in (58, 86)) +
    f'<path d="M88 34 Q112 40 88 52 Q112 62 88 74 Q112 84 88 96 Q112 106 92 114" fill="none" stroke="#7C8BA3" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M88 34 Q112 40 88 52 Q112 62 88 74 Q112 84 88 96 Q112 106 92 114" fill="none" stroke="{O}" stroke-width="1.6"/>'
    f'<rect x="94" y="38" width="14" height="9" rx="3" fill="#3E6FD8" {W(2)}/><rect x="94" y="64" width="14" height="9" rx="3" fill="#FFD23F" {W(2)}/><rect x="94" y="90" width="14" height="9" rx="3" fill="#58C26B" {W(2)}/>'
    f'<rect x="38" y="66" width="22" height="12" rx="4" fill="#E8303A" {W(2.4)}/><circle cx="43" cy="80" r="3" fill="{O}"/><circle cx="55" cy="80" r="3" fill="{O}"/>'
    + f(56, 44, d=7, k=0.6) +
    f'<path d="M36 30 V12" {W(2.6)}/><path d="M36 12 L52 17 L36 22Z" fill="#E8303A" {W(2.2)}/>'
    f'<rect x="38" y="96" width="18" height="18" fill="#C9D3E3" {W(2.4)}/>')

I["schastegrad-ramenskoe"] = ("#FFF0F6", "#F25C8C",
    "золотая праздничная хлопушка-цилиндр в полоску",
    "только что бабахнула: из неё летят серпантин, конфетти и маленькие звёздочки, а сама она зажмурилась от удовольствия",
    f'<path d="M40 112 L58 54 L86 64 L66 118Z" fill="#FFC93C" {W(3.2)}/>'
    + "".join(f'<path d="M{48+i*5} {100-i*14} L{70+i*5} {108-i*14}" stroke="#E8303A" stroke-width="4"/>' for i in range(3)) +
    f'<ellipse cx="72" cy="59" rx="15" ry="6" transform="rotate(20 72 59)" fill="#FFE9A8" {W(2.8)}/>'
    + f(62, 88, d=6, k=0.6, mouth=True) +
    f'<path d="M72 54 Q60 30 76 14 M76 54 Q96 36 110 40 M70 52 Q50 40 34 44" fill="none" stroke-width="3.4" stroke-linecap="round" stroke="#3E6FD8"/>'
    f'<path d="M74 50 Q88 26 100 18" fill="none" stroke="#58C26B" stroke-width="3.4" stroke-linecap="round"/>'
    + "".join(f'<rect x="{x}" y="{y}" width="6" height="6" rx="1.5" transform="rotate({x} {x+3} {y+3})" fill="{c}"/>'
              for x, y, c in [(30, 30, "#FFD23F"), (52, 20, "#58C26B"), (92, 28, "#E8303A"), (108, 56, "#7B5BE0"), (22, 56, "#3E6FD8")]) +
    sparkle(90, 12, 4, "#FFE14D") + sparkle(46, 32, 3, "#FFE14D"))

I["ostrov-sokrovishch-ramenskoe"] = ("#FFF6D9", "#E8C76A",
    "золотой пиратский дублон с весёлой рожицей",
    "выпрыгивает из свежевыкопанной ямки под красным крестиком на песке, рядом воткнута лопатка",
    f'<path d="M0 92 Q64 80 128 92 V130 H0Z" fill="#F2D38B" {W(2.6)}/>'
    f'<ellipse cx="60" cy="100" rx="22" ry="7" fill="#9C6B36" {W(2.6)}/>'
    f'<path d="M42 110 L54 120 M54 110 L42 120" stroke="#E2302E" stroke-width="4" stroke-linecap="round"/>'
    f'<circle cx="60" cy="56" r="24" fill="#FFC21A" {W(3.2)}/><circle cx="60" cy="56" r="18" fill="none" stroke="#D99400" stroke-width="2.6"/>'
    + f(60, 56, d=7, k=0.65) +
    f'<path d="M48 84 Q52 92 58 96 M72 84 Q68 92 62 96" fill="none" stroke="#9C6B36" stroke-width="2.4" stroke-dasharray="2 4"/>'
    f'<path d="M98 102 L104 50" {W(3.4)}/><path d="M96 104 L108 104 L106 118 Q102 124 98 118Z" fill="#B0B8C8" {W(2.6)}/>'
    f'<path d="M100 50 H110" {W(3.4)}/>'
    + sparkle(30, 40, 4, "#FFF6C8") + sparkle(88, 30, 3, "#FFF6C8") + sparkle(26, 70, 2.5, "#FFF6C8"))

# ---------------- творческие студии ----------------
I["art-nechaevoy-artekovskaya"] = ("#E2FFF3", "#47B98C",
    "холщовая сумка-шоппер с длинными ручками",
    "кисточка дорисовывает на ней последний лепесток красной ромашки, сумка довольно улыбается",
    f'<path d="M44 44 Q44 18 64 18 Q84 18 84 44" fill="none" stroke="#D8C7A4" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M44 44 Q44 18 64 18 Q84 18 84 44" fill="none" {W(1.6)}/>'
    f'<path d="M30 42 H98 L102 112 H26Z" fill="#F4E9D2" {W(3.2)}/>'
    + "".join(f'<ellipse cx="{56+11*__import__("math").cos(a)}" cy="{74+11*__import__("math").sin(a)}" rx="7" ry="4.5" '
              f'transform="rotate({a*57.3} {56+11*__import__("math").cos(a)} {74+11*__import__("math").sin(a)})" fill="#F0485A" {W(2)}/>'
              for a in [i * 0.898 for i in range(6)]) +
    f'<circle cx="56" cy="74" r="7" fill="#FFD23F" {W(2.2)}/>'
    + f(56, 98, d=7, k=0.55) +
    f'<path d="M104 20 L80 70" stroke="#C88A4E" stroke-width="5" stroke-linecap="round"/><path d="M104 20 L80 70" fill="none" {W(1.4)}/>'
    f'<path d="M82 66 L76 80 L74 70Z" fill="#F0485A" {W(2)}/>')

I["art-discovery-bolotnikovskaya"] = ("#DCE6FF", "#3D5BB8",
    "оранжевая рыбка с картины в золотой раме",
    "выпрыгивает из нарисованного моря прямо из рамы, разбрызгивая капли краски наружу",
    f'<rect x="18" y="38" width="80" height="70" rx="3" fill="#E4B53C" {W(3.2)}/>'
    f'<rect x="28" y="48" width="60" height="50" fill="#7FD0F5" {W(2.4)}/>'
    f'<path d="M28 80 Q38 72 48 80 Q58 88 68 80 Q78 72 88 80 V98 H28Z" fill="#2F7FD0"/>'
    f'<path d="M66 74 Q76 48 96 34 Q104 30 106 40 Q110 54 92 66 Q82 74 70 78Z" fill="#FF8A2B" {W(3)}/>'
    f'<path d="M66 74 L54 84 L62 70 L52 66Z" fill="#FF8A2B" {W(2.6)}/>'
    f'{eye(96,42,0.65)}<path d="M100 52 Q104 54 104 50" fill="none" {W(2)}/>'
    f'<path d="M82 52 Q86 60 80 66" fill="none" stroke="#FFD08A" stroke-width="2.6" stroke-linecap="round"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" {W(1.6)}/>' for x, y, r, c in [(110, 66, 3.5, "#2F7FD0"), (112, 80, 2.6, "#7FD0F5"), (100, 26, 3, "#2F7FD0")]))

I["dtdm-sevastopolets"] = ("#E6F6FF", "#5AA9E0",
    "гирлянда морских сигнальных флажков на мачте",
    "весело развевается над белым дворцом с колоннами и треугольным фронтоном",
    f'<path d="M0 112 H128 V130 H0Z" fill="#B8D8A8" {W(2.4)}/>'
    f'<path d="M30 70 L64 54 L98 70Z" fill="#fff" {W(3)}/>'
    f'<rect x="28" y="70" width="72" height="8" fill="#fff" {W(2.8)}/>'
    + "".join(f'<rect x="{x}" y="78" width="7" height="28" fill="#fff" {W(2.4)}/>' for x in (34, 48, 63, 78, 90)) +
    f'<rect x="24" y="104" width="80" height="8" fill="#fff" {W(2.8)}/>'
    f'<path d="M64 54 V14" {W(3)}/>'
    f'<path d="M64 16 Q86 22 116 50" fill="none" {W(2)}/><path d="M64 16 Q40 24 12 52" fill="none" {W(2)}/>'
    + "".join(f'<path d="M{x} {y} l9 2 -2 9 -9 -2Z" fill="{c}" {W(1.8)}/>'
              for x, y, c in [(72, 20, "#E8303A"), (84, 26, "#FFD23F"), (95, 33, "#3E6FD8"), (105, 42, "#fff"),
                              (52, 21, "#58C26B"), (40, 27, "#FF8A2B"), (28, 35, "#3E6FD8"), (18, 44, "#E8303A")]) +
    f(64, 90, d=8, k=0.6))

I["perotti-raskovoy"] = ("#FFEADF", "#D9744A",
    "деревянный этюдник на трёх ножках",
    "держит недописанную картину с большим подсолнухом, рядом на ножке висит берет",
    f'<path d="M64 20 L34 118 M64 20 L94 118 M64 20 L64 112" {W(4)}/>'
    f'<rect x="32" y="30" width="64" height="60" rx="2" fill="#FFF8EC" {W(3.2)}/>'
    + "".join(f'<ellipse cx="{64+14*__import__("math").cos(i*0.785)}" cy="{58+14*__import__("math").sin(i*0.785)}" rx="7" ry="4" '
              f'transform="rotate({i*45} {64+14*__import__("math").cos(i*0.785)} {58+14*__import__("math").sin(i*0.785)})" fill="#FFC21A" {W(1.8)}/>'
              for i in range(7)) +
    f'<circle cx="64" cy="58" r="9" fill="#7A4A22" {W(2.2)}/>'
    f'<path d="M64 68 V88 M64 80 Q56 74 52 80" fill="none" stroke="#4CA64C" stroke-width="3"/>'
    f'<rect x="28" y="88" width="72" height="7" rx="2" fill="#B8783E" {W(2.6)}/>'
    + f(64, 102, d=7, k=0.55, blush=False) +
    f'<ellipse cx="96" cy="100" rx="11" ry="5" fill="#2E2A50" {W(2.4)}/><path d="M96 95 V91" {W(2.4)}/>')

I["barbariki-korolyova"] = ("#FFF2DC", "#F2A541",
    "картонная маска рыжей лисы на палочке, раскрашенная гуашью",
    "лежит на столе среди бумажных обрезков и подмигивает, рядом детские ножницы с круглыми ручками",
    f'<rect x="0" y="96" width="128" height="34" fill="#C9E2F5" {W(2.4)}/>'
    f'<path d="M30 40 L40 16 L54 36 Q64 32 74 36 L88 16 L98 40 Q106 62 64 86 Q22 62 30 40Z" fill="#FF8A2B" {W(3.2)}/>'
    f'<path d="M40 22 L44 34 M88 22 L84 34" stroke="#3B3355" stroke-width="2"/>'
    f'<path d="M44 62 Q64 76 84 62 Q74 84 64 86 Q54 84 44 62Z" fill="#fff" {W(2.4)}/>'
    f'<path d="M44 52 Q50 46 56 52" fill="none" {W(2.6)}/>{eye(76,50,0.7)}<circle cx="64" cy="70" r="3.5" fill="{O}"/>'
    f'<path d="M64 86 L64 122" stroke="#C88A4E" stroke-width="5" stroke-linecap="round"/><path d="M64 86 L64 122" fill="none" {W(1.4)}/>'
    f'<circle cx="96" cy="108" r="7" fill="none" stroke="#E8303A" stroke-width="3.4"/><circle cx="110" cy="102" r="7" fill="none" stroke="#E8303A" stroke-width="3.4"/>'
    f'<path d="M100 104 L120 86 M104 100 L118 90" {W(2.6)}/>'
    f'<path d="M18 104 l8 4 -6 6Z M30 116 l6 -2 2 6Z" fill="#7FD0F5" {W(1.6)}/>')

I["proart-oskanova"] = ("#F1E6FF", "#9A73DA",
    "брусок зелёного пластилина из коробки",
    "выпрыгнул из коробки с разноцветными брусками и сам лепит себе круглые ушки",
    f'<path d="M14 88 H94 L102 118 H22Z" fill="#FFD84A" {W(3)}/>'
    + "".join(f'<rect x="{x}" y="80" width="12" height="16" rx="2" fill="{c}" {W(2.2)}/>'
              for x, c in [(24, "#E8303A"), (38, "#3E6FD8"), (52, "#FF8A2B"), (80, "#B060D8")]) +
    f'<rect x="66" y="80" width="12" height="16" rx="2" fill="none" stroke="{O}" stroke-width="2" stroke-dasharray="3 3"/>'
    f'<rect x="54" y="26" width="34" height="46" rx="8" fill="#5BC35B" {W(3.2)}/>'
    f'<path d="M58 40 H84 M58 56 H84" stroke="#3E9A3E" stroke-width="1.8"/>'
    + f(71, 46, d=7, k=0.6) +
    f'<circle cx="58" cy="24" r="7" fill="#5BC35B" {W(2.6)}/><circle cx="86" cy="24" r="6" fill="#5BC35B" {W(2.6)}/>'
    f'<path d="M88 52 Q100 40 92 28" fill="none" stroke="#5BC35B" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M66 72 L64 82 M78 72 L80 82" {W(3)}/>' + sparkle(108, 60, 4) + sparkle(30, 46, 3))

I["teatr-alt-uglichskaya"] = ("#3A2A6B", "#140C2E",
    "маленькая жёлтая укулеле с бантиком на грифе",
    "стоит на сцене в круглом луче софита и поёт — из розетки вылетают ноты",
    f'<path d="M40 -4 L88 -4 L112 118 L16 118Z" fill="#FFF1A8" opacity=".25"/>'
    f'<ellipse cx="64" cy="114" rx="44" ry="8" fill="#FFF1A8" opacity=".5"/>'
    f'<rect x="0" y="112" width="128" height="20" fill="#8B4B2A" {W(2.4)}/>'
    f'<path d="M58 14 H70 V52 H58Z" fill="#7A4A22" {W(2.8)}/><rect x="54" y="6" width="20" height="12" rx="3" fill="#5A3A22" {W(2.6)}/>'
    f'<path d="M64 52 Q42 52 44 72 Q46 82 42 92 Q40 112 64 112 Q88 112 86 92 Q82 82 84 72 Q86 52 64 52Z" fill="#FFC72C" {W(3.2)}/>'
    f'<circle cx="64" cy="76" r="7" fill="#3B2410" {W(2.2)}/>'
    f'<path d="M61 14 V96 M67 14 V96" stroke="#fff" stroke-width="1.2"/><rect x="54" y="94" width="20" height="5" rx="2" fill="#5A3A22" {W(1.8)}/>'
    + f(64, 88, d=10, k=0.6, mouth=False) +
    f'<path d="M70 24 l10 -6 v8 l-10 6Z" fill="#E8305A" {W(2)}/>'
    f'<path d="M90 50 V36 l8 -3" fill="none" stroke="#fff" stroke-width="2.6"/><ellipse cx="88" cy="50" rx="4" ry="3" fill="#fff"/>'
    f'<path d="M30 46 V30" stroke="#fff" stroke-width="2.6"/><ellipse cx="28" cy="46" rx="4" ry="3" fill="#fff"/>')

I["zeleny-mayak-tvardovskogo"] = ("#E4FAD8", "#5DB548",
    "стеклянная банка с водой для мытья кисточек",
    "в неё окунули три кисти, и в воде расплываются цветные облачка краски, банка удивлённо смотрит",
    f'<path d="M34 46 H94 V108 Q94 116 86 116 H42 Q34 116 34 108Z" fill="#E8F8FF" {W(3.2)}/>'
    f'<path d="M36 60 H92 V108 Q92 114 86 114 H42 Q36 114 36 108Z" fill="#BFE8F7"/>'
    f'<ellipse cx="50" cy="80" rx="10" ry="7" fill="#58C26B" opacity=".75"/><ellipse cx="74" cy="92" rx="12" ry="8" fill="#F25C8C" opacity=".6"/>'
    f'<ellipse cx="68" cy="72" rx="8" ry="6" fill="#FFD23F" opacity=".75"/>'
    f'<rect x="30" y="40" width="68" height="8" rx="3" fill="#fff" {W(2.8)}/>'
    + "".join(f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{c}" stroke-width="5" stroke-linecap="round"/><path d="M{x1} {y1} L{x2} {y2}" fill="none" {W(1.4)}/>'
              for x1, y1, x2, y2, c in [(46, 70, 34, 14, "#E8303A"), (62, 66, 64, 8, "#3E6FD8"), (78, 70, 96, 16, "#B8783E")]) +
    f'{eye(54,100,0.65)}{eye(74,100,0.65)}<ellipse cx="64" cy="108" rx="3" ry="3.5" fill="{O}"/>')

I["studiya-yunogo-tvorchestva-leningradsky"] = ("#FFE8F2", "#D85A93",
    "жёлтая поролоновая губка-штамп в краске",
    "прижимается к трафарету-звезде на листе, а под ним уже отпечатались три цветные звёздочки",
    f'<rect x="12" y="62" width="104" height="58" rx="3" fill="#fff" {W(3)}/>'
    + "".join(f'<path d="M{x} {y-9} l3 6 7 1 -5 5 1 7 -6 -3 -6 3 1 -7 -5 -5 7 -1Z" fill="{c}"/>'
              for x, y, c in [(28, 98, "#3E6FD8"), (52, 106, "#58C26B"), (100, 104, "#FF8A2B")]) +
    f'<rect x="58" y="70" width="44" height="34" rx="2" fill="#B8C4D6" {W(2.4)}/>'
    f'<path d="M80 74 l4 8 9 1 -7 6 2 9 -8 -5 -8 5 2 -9 -7 -6 9 -1Z" fill="#fff" {W(1.8)}/>'
    f'<rect x="58" y="22" width="44" height="40" rx="8" fill="#FFD23F" {W(3.2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="#E0A800"/>' for x, y in [(66, 30), (90, 32), (72, 54), (94, 52), (82, 28)]) +
    f'<rect x="58" y="54" width="44" height="10" rx="4" fill="#E8305A" {W(2.4)}/>'
    + f(80, 40, d=8, k=0.6) + sparkle(30, 40, 4) + sparkle(42, 22, 3))

I["magiya-krasok-shipilovskaya"] = ("#E8FBFF", "#43B4D2",
    "бабочка-монотипия из сложенного листа бумаги",
    "лист раскрылся, и симметричная клякса-бабочка оживает и взлетает с листа",
    f'<path d="M14 116 L64 98 L114 116 L64 128Z" fill="#fff" {W(2.6)}/><path d="M64 98 V128" {W(1.8)}/>'
    f'<path d="M30 112 Q44 104 56 110 M98 112 Q84 104 72 110" fill="none" stroke="#B060D8" stroke-width="3" opacity=".5"/>'
    f'<path d="M62 70 Q40 30 20 40 Q8 52 26 66 Q10 78 26 90 Q42 98 62 76Z" fill="#B060D8" {W(3)}/>'
    f'<path d="M66 70 Q88 30 108 40 Q120 52 102 66 Q118 78 102 90 Q86 98 66 76Z" fill="#B060D8" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>' for x, y, r, c in
              [(34, 52, 7, "#FFD23F"), (94, 52, 7, "#FFD23F"), (32, 80, 5, "#43C8E8"), (96, 80, 5, "#43C8E8"), (46, 66, 3, "#FF5C8A"), (82, 66, 3, "#FF5C8A")]) +
    f'<ellipse cx="64" cy="68" rx="5" ry="16" fill="#4A2A6E" {W(2.6)}/>'
    f'<path d="M62 54 Q56 40 50 38 M66 54 Q72 40 78 38" fill="none" {W(2.2)}/>'
    + f(64, 62, d=3, k=0.4, mouth=False, blush=False) + sparkle(110, 20, 4) + sparkle(20, 22, 3))

I["yarkie-kraski-kashirskoe"] = ("#FFF8DA", "#E9C33C",
    "открытая жестяная коробка акварели с двенадцатью цветными кюветами",
    "кисточка окунается в синюю кювету, а коробка улыбается в крышке-зеркальце",
    f'<path d="M20 64 L108 64 L108 112 L20 112Z" fill="#3E4A8C" {W(3.2)}/>'
    f'<path d="M20 64 L30 22 L118 22 L108 64Z" fill="#5867B5" {W(3)}/>'
    f'<rect x="38" y="30" width="62" height="24" rx="4" fill="#CFE6FF" {W(2.2)}/>'
    + f(69, 41, d=8, k=0.6) +
    "".join(f'<rect x="{26+(i%6)*13.5}" y="{72+(i//6)*18}" width="11" height="14" rx="2.5" fill="{c}" {W(1.8)}/>'
            for i, c in enumerate(["#E8303A", "#FF8A2B", "#FFD23F", "#9BD24A", "#2FA65A", "#1BA6B0",
                                   "#3E6FD8", "#7B5BE0", "#D04EB0", "#8B5A2B", "#3B3355", "#F2A0C0"])) +
    f'<path d="M78 92 L118 120" stroke="#E8C79A" stroke-width="5" stroke-linecap="round"/><path d="M78 92 L118 120" fill="none" {W(1.4)}/>'
    f'<path d="M80 94 L72 86 L76 96Z" fill="#3E6FD8" {W(2)}/>')

I["guryanova-art-zakharova"] = ("#E5ECFF", "#7186D8",
    "жёлтая груша-натурщица с листиком на хвостике",
    "важно позирует на синей складчатой драпировке, а сбоку на листе уже набросан её портрет карандашом",
    f'<path d="M0 86 Q30 72 54 88 Q78 104 128 84 V130 H0Z" fill="#2F5BD0" {W(3)}/>'
    f'<path d="M14 100 Q30 92 40 104 M70 110 Q86 100 102 108" fill="none" stroke="#7FA2F0" stroke-width="2.4"/>'
    f'<path d="M50 28 Q62 28 62 44 Q62 52 70 62 Q78 74 70 86 Q60 96 46 92 Q30 86 34 70 Q38 60 42 52 Q44 30 50 28Z" fill="#FFD23F" {W(3.2)}/>'
    f'<path d="M50 28 Q50 20 54 16" fill="none" {W(2.8)}/><path d="M54 18 Q64 8 70 18 Q62 22 54 18Z" fill="#58C26B" {W(2.2)}/>'
    + f(52, 68, d=7, k=0.6) +
    f'<rect x="82" y="30" width="38" height="50" rx="2" fill="#fff" transform="rotate(8 100 55)" {W(2.6)}/>'
    f'<path d="M98 40 Q104 42 102 50 Q110 60 104 68 Q96 74 92 66 Q90 58 96 52 Q94 44 98 40Z" fill="none" stroke="#7A7A8A" stroke-width="1.8"/>')

I["art-mars-domodedovo"] = ("#FFE6E0", "#E2604A",
    "деревянные пяльцы с ковровой вышивкой",
    "в пяльцах вырастает пушистое красное сердечко из петелек, игла-панч ещё торчит в ткани",
    f'<circle cx="60" cy="68" r="42" fill="#F5EBDC" {W(3.2)}/>'
    f'<circle cx="60" cy="68" r="42" fill="none" stroke="#C88A4E" stroke-width="7"/><circle cx="60" cy="68" r="42" fill="none" {W(1.6)}/>'
    f'<rect x="56" y="18" width="8" height="12" rx="2" fill="#B87443" {W(2.4)}/>'
    f'<path d="M60 96 Q30 76 36 58 Q42 44 60 56 Q78 44 84 58 Q90 76 60 96Z" fill="#E8303A" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3.2" fill="#FF6B6B" {W(1.2)}/>' for x, y in
              [(46, 62), (54, 66), (66, 66), (74, 62), (50, 74), (60, 76), (70, 74), (56, 84), (64, 84), (60, 60)]) +
    f(60, 72, d=7, k=0.5, blush=False) +
    f'<path d="M84 50 L112 20" stroke="#C9CDD8" stroke-width="4" stroke-linecap="round"/>'
    f'<rect x="104" y="10" width="10" height="20" rx="3" transform="rotate(42 109 20)" fill="#FFD23F" {W(2.2)}/>'
    f'<path d="M112 22 Q120 40 106 52" fill="none" stroke="#E8303A" stroke-width="2"/>')

I["davayte-risovat-domodedovo"] = ("#E9F7E3", "#79BE5C",
    "длинный рулон ватмана",
    "раскатывается по полу, превращаясь в нарисованную дорогу, по которой уже едет нарисованная машинка",
    f'<path d="M30 58 L128 58 L128 130 L-4 130 Z" fill="#fff" {W(3)}/>'
    f'<path d="M6 116 Q40 100 60 104 Q90 108 128 92" fill="none" stroke="#9AA6B8" stroke-width="3" stroke-dasharray="8 6"/>'
    f'<rect x="20" y="30" width="96" height="28" rx="14" fill="#F7F4EA" {W(3.2)}/>'
    f'<ellipse cx="22" cy="44" rx="8" ry="14" fill="#E2DCC8" {W(2.6)}/><ellipse cx="22" cy="44" rx="3" ry="5" fill="#C9C0A8"/>'
    f'<path d="M62 102 L64 92 Q68 84 78 84 L90 84 Q96 86 98 94 L98 102Z" fill="#E8303A" {W(2.6)}/>'
    f'<circle cx="70" cy="104" r="5" fill="#3B3355"/><circle cx="92" cy="104" r="5" fill="#3B3355"/>'
    + f(70, 44, d=9, k=0.6) +
    f'<path d="M100 14 L116 4" stroke="#3E6FD8" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M30 74 Q40 70 46 78" fill="none" stroke="#58C26B" stroke-width="3" stroke-linecap="round"/>')

I["tochilka-lyubertsy"] = ("#DFF1FF", "#4D8FD6",
    "синяя квадратная точилка-кубик с прозрачным окошком",
    "точит зелёный карандаш, а из неё вьётся длинная стружка-гармошка с цветной каёмкой",
    f'<rect x="18" y="46" width="52" height="52" rx="8" fill="#2F6FD0" {W(3.2)}/>'
    f'<rect x="26" y="70" width="36" height="20" rx="4" fill="#BFE3FF" {W(2.2)}/>'
    + f(44, 60, d=9, k=0.65) +
    f'<path d="M70 58 L116 40 L120 50 L74 68Z" fill="#4CB050" {W(3)}/>'
    f'<path d="M116 40 L124 42 L120 50Z" fill="#F2D2A0" {W(2)}/>'
    f'<path d="M30 98 Q20 106 30 112 Q42 118 34 124 M40 98 Q50 106 44 114 Q38 120 50 126" fill="none" stroke="#E8C79A" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M30 98 Q20 106 30 112 Q42 118 34 124" fill="none" stroke="#4CB050" stroke-width="1.6"/>'
    + sparkle(96, 22, 4) + sparkle(108, 76, 3))

I["dvoretskoy-ramenskoe"] = ("#E6EEFF", "#4F6FC8",
    "цыплёнок-аппликация из жёлтых бумажных кружков",
    "приклеен на голубой картон, у него вырезной клювик и лапки, рядом клей-карандаш со снятым колпачком",
    f'<rect x="14" y="20" width="84" height="92" rx="3" fill="#BFE3FF" transform="rotate(-6 56 66)" {W(3)}/>'
    f'<circle cx="56" cy="78" r="22" fill="#FFD23F" {W(2.8)}/><circle cx="54" cy="48" r="15" fill="#FFE14D" {W(2.8)}/>'
    f'<path d="M52 36 L50 28 L56 34 L58 26 L60 36" fill="#FFE14D" {W(2)}/>'
    f'{eye(48,46,0.55)}{eye(60,46,0.55)}<path d="M52 54 L58 52 L54 60Z" fill="#FF8A2B" {W(2)}/>'
    f'<path d="M36 76 Q30 70 34 64 Q42 70 40 80Z" fill="#F7C21A" {W(2.2)}/>'
    f'<path d="M48 100 L46 108 L40 110 M64 100 L66 108 L72 110" fill="none" stroke="#FF8A2B" stroke-width="3" stroke-linecap="round"/>'
    f'<rect x="96" y="54" width="16" height="50" rx="4" fill="#fff" {W(2.8)}/><rect x="96" y="54" width="16" height="16" fill="#E8303A" {W(2.4)}/>'
    f'<path d="M98 54 V44 Q104 40 110 44 V54Z" fill="#F4F4F8" {W(2.4)}/>'
    f'<rect x="100" y="108" width="10" height="12" rx="2" fill="#E8303A" {W(2.2)}/>')

# ---------------- центры ----------------
I["tehnorama-ryazansky"] = ("#FFFBE0", "#F2C94C",
    "пальчиковая батарейка с полосатым плюсиком",
    "держит в руках два проводка и зажигает лампочку на макетной плате, от лампочки разлетаются лучики",
    f'<rect x="18" y="98" width="92" height="22" rx="3" fill="#F5F5F5" {W(2.6)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1.4" fill="#9AA6B8"/>' for x in range(26, 106, 8) for y in (104, 112)) +
    f'<rect x="20" y="40" width="28" height="56" rx="6" fill="#2F2F38" {W(3.2)}/><rect x="20" y="40" width="28" height="22" rx="6" fill="#E8303A" {W(3)}/>'
    f'<rect x="29" y="34" width="10" height="7" rx="2" fill="#C9CDD8" {W(2.2)}/>'
    f'<path d="M34 46 V56 M29 51 H39" stroke="#fff" stroke-width="2.6"/>'
    + f(34, 74, d=6, k=0.55) +
    f'<path d="M48 70 Q66 70 74 60 M48 84 Q80 88 92 68" fill="none" stroke="#3E6FD8" stroke-width="3" stroke-linecap="round"/>'
    f'<circle cx="84" cy="48" r="16" fill="#FFF2A0" {W(3)}/><rect x="76" y="62" width="16" height="10" rx="2" fill="#B0B8C8" {W(2.4)}/>'
    f'<path d="M78 50 Q84 40 90 50" fill="none" stroke="#FF8A2B" stroke-width="2"/>'
    + "".join(f'<path d="M{84+22*__import__("math").cos(a)} {48+22*__import__("math").sin(a)} L{84+30*__import__("math").cos(a)} {48+30*__import__("math").sin(a)}" stroke="#FF9F1C" stroke-width="3" stroke-linecap="round"/>'
              for a in (-2.6, -2.0, -1.4, -0.8, -0.2, 0.4)))

I["letal-i-shagal"] = ("#E9E8FF", "#7E7CD8",
    "красный детский резиновый сапожок с белыми крылышками",
    "шагает по облакам, как по ступенькам, оставляя за собой пунктир-след в небе",
    f'<path d="M6 108 Q10 96 24 100 Q30 88 46 96 Q58 90 66 104 Q74 112 60 116 H10Z" fill="#fff" {W(2.8)}/>'
    f'<path d="M78 76 Q82 66 94 70 Q102 60 114 70 Q126 72 120 84 H80Z" fill="#fff" {W(2.8)}/>'
    f'<path d="M40 86 Q44 60 70 54" fill="none" stroke="#fff" stroke-width="2.6" stroke-dasharray="3 5" stroke-linecap="round"/>'
    f'<path d="M70 20 H94 V56 Q94 62 102 64 Q114 68 112 76 H70Z" fill="#E8303A" {W(3.2)}/>'
    f'<rect x="66" y="76" width="50" height="7" rx="3" fill="#3B3355"/>'
    f'<rect x="68" y="16" width="28" height="8" rx="3" fill="#FFD23F" {W(2.4)}/>'
    + f(84, 46, d=6, k=0.6) +
    f'<path d="M70 34 Q52 22 50 34 Q44 34 48 42 Q42 46 52 48 Q60 48 70 44Z" fill="#fff" {W(2.4)}/>'
    + sparkle(30, 30, 4) + sparkle(112, 30, 3))

# ---------------- квесты ----------------
I["zona-q-varshavskoe"] = ("#2E1E5E", "#0E0A24",
    "фиолетовый ультрафиолетовый фонарик с глазками",
    "светит на тёмную стену, и на ней проступает светящаяся зелёная стрелка-подсказка и цифры кода",
    f'<path d="M50 74 L118 30 L124 92Z" fill="#B57CFF" opacity=".35"/>'
    f'<path d="M100 54 H114 M108 48 L114 54 L108 60" fill="none" stroke="#7CFF6B" stroke-width="4" stroke-linecap="round"/>'
    + "".join(f'<circle cx="{x}" cy="74" r="2.6" fill="#7CFF6B"/>' for x in (94, 102, 110)) +
    f'<rect x="12" y="70" width="44" height="22" rx="6" transform="rotate(-24 34 81)" fill="#7B4BE0" {W(3.2)}/>'
    f'<path d="M48 62 L58 56 L66 76 L56 80Z" fill="#5A2FB8" {W(2.8)}/>'
    f'<ellipse cx="62" cy="66" rx="4" ry="10" transform="rotate(-24 62 66)" fill="#E5CCFF" {W(2.2)}/>'
    + f(32, 82, d=7, k=0.6) + sparkle(30, 30, 3, "#B57CFF") + sparkle(80, 22, 2.5, "#B57CFF"))

I["dzhumandzhi-show-kashirskoe"] = ("#E3F6D2", "#4E9B3A",
    "белый игральный кубик-персонаж с чёрными точками",
    "выкатился из старой деревянной коробки-игры, а из неё вокруг вырастают огромные листья джунглей",
    f'<path d="M-6 80 Q20 40 34 70 Q30 30 10 20 M128 70 Q104 30 90 66 Q100 26 124 16" fill="#3DA34A" {W(2.6)}/>'
    f'<path d="M0 60 Q30 20 52 54Z M128 54 Q98 14 78 50Z" fill="#5CC05A" {W(2.6)}/>'
    f'<path d="M14 92 L72 80 L114 92 L56 106Z" fill="#8B5A2B" {W(3)}/>'
    f'<path d="M14 92 V112 L56 126 V106 M114 92 V112 L56 126" fill="#6B4220" {W(3)}/>'
    f'<path d="M30 92 L72 84 L98 92 L56 100Z" fill="#3B2410"/>'
    f'<path d="M50 44 L76 38 L84 62 L58 70Z" fill="#fff" {W(3.2)}/><path d="M50 44 L46 64 L58 70 M50 44 L58 42" fill="#E8E8F0" {W(2.6)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.8" fill="{O}"/>' for x, y in [(60, 48), (76, 46), (72, 64)]) +
    f(66, 56, d=4, k=0.42, mouth=True, blush=False))

I["kvest-kids-krasnoselskaya"] = ("#FFF0DA", "#E59A4A",
    "девочка-сыщик в клетчатой кепке и бежевом плаще",
    "присела и разглядывает через большую лупу цепочку маленьких следов на полу",
    f'<rect x="0" y="100" width="128" height="30" fill="#C8A47A" {W(2.4)}/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="3" ry="5" transform="rotate(70 {x} {y})" fill="#7A5232"/>' for x, y in [(86, 112), (100, 106), (114, 114), (126, 108)]) +
    f'<path d="M32 98 Q30 64 50 60 Q66 60 66 96Z" fill="#D9B98C" {W(3)}/>'
    + kid(48, 44, k=1.0, hair="#B0602A") +
    f'<path d="M34 38 Q36 22 50 22 Q62 22 64 36 L74 38 Q72 42 64 40 Z" fill="#9C6F4E" {W(2.6)}/>'
    f'<path d="M40 30 L58 28 M38 34 L60 32 M46 24 V36 M54 24 V36" stroke="#6A4630" stroke-width="1.4"/>'
    f'<path d="M62 76 L78 92" {W(4)}/><circle cx="88" cy="100" r="13" fill="#DFF6FF" {W(3.2)}/>'
    f'<ellipse cx="91" cy="102" rx="3" ry="5" transform="rotate(70 91 102)" fill="#7A5232"/>'
    f'<path d="M82 94 Q86 90 90 92" fill="none" stroke="#fff" stroke-width="2.4"/>')

I["fort-boyard-sheremetyevskaya"] = ("#E6F4FA", "#3E8DB0",
    "старинная водяная клепсидра — бронзовая чаша над стеклянным сосудом",
    "из чаши тонкой струйкой капает вода, отсчитывая время испытания, сосуд наполнился уже наполовину",
    f'<rect x="20" y="112" width="88" height="10" rx="3" fill="#8B5A2B" {W(2.6)}/>'
    f'<path d="M30 30 Q64 64 98 30Z" fill="#C98B3A" {W(3.2)}/><path d="M30 30 H98" {W(3.2)}/>'
    f'<path d="M30 30 V20 M98 30 V20 M30 20 H98" {W(3)}/>'
    f'<path d="M64 48 V64" stroke="#3DA4E0" stroke-width="3" stroke-linecap="round" stroke-dasharray="3 4"/>'
    f'<path d="M38 64 H90 V108 Q90 114 84 114 H44 Q38 114 38 108Z" fill="#E8F8FF" {W(3.2)}/>'
    f'<path d="M40 86 Q64 80 88 86 V108 Q88 112 84 112 H44 Q40 112 40 108Z" fill="#45A8F0"/>'
    + "".join(f'<path d="M86 {y} H92" {W(2)}/>' for y in (74, 84, 94, 104)) +
    f(64, 96, d=8, k=0.6))

I["fort-boyard-kurkino"] = ("#FFF1D8", "#D99A4C",
    "деревянная катапульта на колёсиках с чашей-ложкой",
    "запускает мягкий красный мяч прямо в кольцо на зубчатой каменной башне",
    f'<path d="M86 118 V44 H120 V118Z" fill="#B9B2A6" {W(3)}/>'
    + "".join(f'<rect x="{x}" y="34" width="9" height="12" fill="#B9B2A6" {W(2.4)}/>' for x in (86, 100, 112)) +
    f'<path d="M92 60 H112 M92 80 H116 M90 100 H110" stroke="#8F877A" stroke-width="2"/>'
    f'<circle cx="102" cy="58" r="9" fill="none" stroke="#FF8A2B" stroke-width="3.4"/>'
    f'<path d="M14 106 L60 106 L40 80Z" fill="#B87443" {W(3)}/><circle cx="22" cy="110" r="7" fill="#7A4A22" {W(2.6)}/><circle cx="52" cy="110" r="7" fill="#7A4A22" {W(2.6)}/>'
    f'<path d="M40 82 L14 48" stroke="#C88A4E" stroke-width="6" stroke-linecap="round"/><path d="M40 82 L14 48" fill="none" {W(1.6)}/>'
    f'<ellipse cx="13" cy="44" rx="9" ry="5" fill="#C88A4E" {W(2.4)}/>'
    f'<path d="M24 34 Q60 0 92 50" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 5"/>'
    f'<circle cx="74" cy="22" r="10" fill="#E8303A" {W(2.8)}/>' + f(74, 22, d=4, k=0.4, blush=False) + f(40, 96, d=6, k=0.5))

I["fort-boyard-ramenskoe"] = ("#E9E2D6", "#8E7A62",
    "мальчишка в зелёной бандане",
    "выглядывает сквозь решётчатое окошко тяжёлой дубовой двери камеры и показывает «победу», на двери висит амбарный замок",
    f'<rect x="20" y="10" width="88" height="124" rx="6" fill="#8B5A2B" {W(3.2)}/>'
    + "".join(f'<path d="M{x} 12 V132" stroke="#6B4220" stroke-width="2"/>' for x in (42, 64, 86)) +
    f'<path d="M20 40 H108 M20 104 H108" stroke="#3B3355" stroke-width="4"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#3B3355"/>' for x in (28, 100) for y in (40, 104)) +
    f'<rect x="38" y="46" width="52" height="40" rx="4" fill="#3A2A20" {W(2.8)}/>'
    + kid(64, 70, k=1.0, hair="#4A2C1A") +
    f'<path d="M50 60 Q64 52 78 60 L76 64 Q64 58 52 64Z" fill="#3DA34A" {W(2.2)}/><path d="M78 60 L86 56 L84 64Z" fill="#3DA34A" {W(1.8)}/>'
    + "".join(f'<path d="M{x} 46 V86" stroke="#9AA0AE" stroke-width="3.4"/>' for x in (48, 58, 70, 80)) +
    f'<path d="M86 74 L90 62 M90 74 L96 64" stroke="#FFD9B8" stroke-width="3.4" stroke-linecap="round"/>'
    f'<path d="M58 102 Q58 92 66 92 Q74 92 74 102" fill="none" stroke="#C9CDD8" stroke-width="3"/><rect x="54" y="100" width="24" height="18" rx="3" fill="#C9CDD8" {W(2.6)}/>')

I["zoloto-forta-vegas"] = ("#3A1F1F", "#120808",
    "золотой слиток-персонаж с гравировкой-звездой",
    "лежит на бархатной подушке, а вокруг крест-накрест натянуты красные лучи сигнализации",
    f'<path d="M0 30 L128 70 M0 90 L128 40 M10 128 L118 0" stroke="#FF2E3E" stroke-width="2" opacity=".85"/>'
    f'<ellipse cx="64" cy="100" rx="44" ry="12" fill="#B0204A" {W(3)}/>'
    f'<path d="M24 98 L28 108 M104 98 L100 108" {W(2.4)}/>'
    f'<path d="M30 92 L42 62 H86 L98 92Z" fill="#FFC21A" {W(3.2)}/><path d="M42 62 L48 74 H80 L86 62" fill="#FFE27A" {W(2.4)}/>'
    f'<path d="M64 64 l2 4 4 0 -3 3 1 4 -4 -2 -4 2 1 -4 -3 -3 4 0Z" fill="#E0A000"/>'
    + f(64, 82, d=9, k=0.6) + sparkle(30, 56, 4, "#FFE27A") + sparkle(100, 50, 3, "#FFE27A"))

I["ramquest-ramenskoe"] = ("#E2F0EC", "#5E9C8E",
    "кудрявый белый барашек со свечой в подсвечнике",
    "крадётся на цыпочках по чёрно-белому шахматному полу тёмного коридора, озираясь",
    f'<path d="M0 100 L128 92 V130 H0Z" fill="#fff" {W(2.4)}/>'
    + "".join(f'<path d="M{x} {100-(x/128)*8} l16 -1 v15 l-16 1Z" fill="#3B3355"/>' for x in range(0, 128, 32)) +
    f'<path d="M100 40 Q100 30 106 30 Q112 30 112 40" fill="#FFE27A" opacity=".5"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="11" fill="#fff" {W(2.6)}/>' for x, y in [(44, 64), (60, 58), (76, 62), (52, 76), (70, 78), (36, 76)]) +
    f'<ellipse cx="56" cy="70" rx="22" ry="12" fill="#fff"/>'
    f'<path d="M40 86 L36 98 M52 88 L52 98 M66 88 L68 98 M78 84 L82 96" {W(3.4)}/>'
    f'<ellipse cx="88" cy="56" rx="11" ry="13" fill="#3B3355" {W(2.6)}/>'
    f'<circle cx="84" cy="54" r="2.4" fill="#fff"/><circle cx="92" cy="54" r="2.4" fill="#fff"/>'
    f'<path d="M80 44 Q74 40 76 48 M96 44 Q102 40 100 48" fill="#3B3355" {W(2)}/>'
    f'<path d="M98 66 L106 60" {W(2.8)}/><rect x="102" y="46" width="8" height="14" rx="2" fill="#FFF6E0" {W(2.2)}/>'
    f'<path d="M106 46 Q102 40 106 34 Q110 40 106 46Z" fill="#FFB300" {W(1.6)}/><ellipse cx="106" cy="61" rx="8" ry="2.6" fill="#C9A24A" {W(2)}/>')

if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        a, b, hero, scene, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
