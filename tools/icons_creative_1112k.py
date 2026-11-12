"""Иконки робота creative, 12.11 (запуск 1112k). Каждая придумана и нарисована отдельно: свой герой, своя сцена,
своя компоновка и свой фон (правило абсолютной уникальности). python3 tools/icons_creative_1112k.py → icons-src/<id>.svg"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SKIN = "#FFD2B0"


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


def limb(x1, y1, x2, y2, c, w=5):
    return f'<path d="M{x1} {y1} L{x2} {y2}" {ln(O, w + 3)}/><path d="M{x1} {y1} L{x2} {y2}" {ln(c, w)}/>'


def note(x, y, k=1.0, c=O):
    return (f'<ellipse cx="{x}" cy="{y}" rx="{5*k:.1f}" ry="{4*k:.1f}" fill="{c}" transform="rotate(-20 {x} {y})"/>'
            f'<path d="M{x+4.5*k:.1f} {y-1*k:.1f} V{y-17*k:.1f} Q{x+10*k:.1f} {y-14*k:.1f} {x+11*k:.1f} {y-9*k:.1f}" fill="none" stroke="{c}" stroke-width="{2.4*k:.1f}" stroke-linecap="round"/>')


def head(x, y, r, hair, k=0.6):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{SKIN}" {s()}/>'
            f'<path d="M{x-r} {y-1} Q{x-r} {y-r-3} {x} {y-r-2} Q{x+r} {y-r-3} {x+r} {y-1} Q{x} {y-r+6} {x-r} {y-1}Z" fill="{hair}" {s("stroke-width=\"2.4\"")}/>'
            f'{eye(x-5, y+2, k)}{eye(x+5, y+2, k)}<path d="M{x-3} {y+7} Q{x} {y+10} {x+3} {y+7}" fill="none" {s("stroke-width=\"1.8\"")}/>')


I = {}

# 1 Квасневская (джаз-модерн): девочка в чёрном трико — «джазовые ручки» в круге света
I["kvasnevskaya-melnikova"] = ("девочка в чёрном трико и красной юбке-полусолнце",
    "показывает «джазовые ручки» с растопыренными ладонями, стоя на одной ноге в круге света", bg("#2FB8B0", "#0E4D57", f'''
<ellipse cx="64" cy="112" rx="40" ry="9" fill="#FFF3B0" opacity=".55"/>
<path d="M40 0 L24 112 H104 L88 0Z" fill="#FFF7CC" opacity=".18"/>
{limb(60, 88, 58, 112, "#26222F", 6)}{limb(68, 88, 86, 96, "#26222F", 6)}
<path d="M48 76 Q64 70 80 76 L92 92 Q64 98 36 92Z" fill="#E8344A" {s()}/>
<path d="M54 50 Q64 46 74 50 L76 78 H52Z" fill="#26222F" {s()}/>
{limb(54, 54, 30, 40, "#26222F", 6)}{limb(74, 54, 98, 40, "#26222F", 6)}
<g fill="{SKIN}" {s('stroke-width="2.2"')}><circle cx="27" cy="37" r="6"/><circle cx="101" cy="37" r="6"/></g>
<path d="M21 30 l-4 -5 M25 28 l-1 -7 M30 29 l2 -6 M107 30 l4 -5 M103 28 l1 -7 M98 29 l-2 -6" {ln(O, 2.2)}/>
{head(64, 34, 12, "#1E1A2E")}
<circle cx="64" cy="20" r="5" fill="#1E1A2E" {s('stroke-width="2"')}/>
{sparkle(18, 64, 4)}{sparkle(110, 66, 5)}
'''))

# 2 Шокс (бальные с 3 лет): розовая бальная юбка-годе сама кружится колоколом
I["shoks-letnyaya"] = ("розовая бальная юбка-годе с блёстками и пояском-бантом",
    "кружится колоколом сама по себе, разбрасывая блёстки над маленькой сценой с рампой", bg("#FFF4FA", "#F28CC0", f'''
<rect x="0" y="104" width="128" height="24" fill="#8E3D6B"/><path d="M0 104 H128" {s('stroke-width="2.4"')}/>
<g fill="#FFE27A">{''.join(f'<circle cx="{x}" cy="110" r="3"/>' for x in range(12, 128, 16))}</g>
<path d="M44 44 H84 L106 96 Q64 108 22 96Z" fill="#FF6FB0" {s()}/>
<path d="M50 52 L36 94 M64 52 V100 M78 52 L92 94" stroke="#E0458F" stroke-width="3" fill="none"/>
<path d="M22 96 Q30 90 36 98 Q44 90 50 100 Q58 92 64 101 Q70 92 78 100 Q84 90 92 98 Q98 90 106 96" fill="none" {s()}/>
<rect x="42" y="38" width="44" height="10" rx="5" fill="#C2185B" {s('stroke-width="2.4"')}/>
<path d="M64 43 L54 32 L54 50Z M64 43 L74 32 L74 50Z" fill="#C2185B" {s('stroke-width="2.4"')}/>
{eye(54, 70, 0.8)}{eye(74, 70, 0.8)}<path d="M59 78 Q64 83 69 78" fill="none" {s('stroke-width="2.2"')}/>
<ellipse cx="47" cy="78" rx="4" ry="2.4" fill="#FF3F8E" opacity=".6"/><ellipse cx="81" cy="78" rx="4" ry="2.4" fill="#FF3F8E" opacity=".6"/>
<path d="M14 64 q6 -10 12 0 M102 58 q6 -10 12 0" fill="none" {ln("#fff", 3)}/>
{sparkle(24, 40, 5, "#FFD23A")}{sparkle(104, 34, 4, "#FFD23A")}{sparkle(16, 86, 3)}{sparkle(112, 82, 3.5)}
'''))

# 3 Театральная мастерская: накладные гусарские усы на палочке примеряются у гримёрного зеркальца
I["tsoi-teatr-baryshikha"] = ("накладные пышные гусарские усы на палочке с глазками",
    "примеряются перед круглым зеркальцем на подставке, подкручивая кончики", bg("#FFE0B8", "#C2662D", f'''
<rect x="0" y="100" width="128" height="28" fill="#7A3E1A"/>
<circle cx="88" cy="58" r="28" fill="#DFF3FF" {s()}/><circle cx="88" cy="58" r="22" fill="#BFE4F7"/>
<path d="M78 46 Q86 40 94 44" stroke="#fff" stroke-width="3" fill="none" opacity=".8"/>
<path d="M88 86 V100 M76 102 H100" {ln(O, 5)}/><path d="M88 86 V100 M76 102 H100" {ln("#D9A441", 3)}/>
<path d="M30 96 L44 64" {ln(O, 6)}/><path d="M30 96 L44 64" {ln("#C98E52", 3.5)}/>
<path d="M44 62 Q30 50 14 60 Q10 50 20 46 Q34 44 44 56 Q54 44 68 46 Q78 50 74 60 Q58 50 44 62Z" fill="#3A2418" {s()}/>
<path d="M14 60 q-4 -6 2 -10 M74 60 q4 -6 -2 -10" fill="none" {ln(O, 2.4)}/>
{eye(36, 52, 0.55)}{eye(52, 52, 0.55)}
<path d="M84 60 Q88 56 92 60 Q88 58 84 60Z" fill="#3A2418" opacity=".55"/>
{sparkle(108, 26, 4)}{sparkle(20, 24, 3.5)}
'''))

# 4 Летц Денс (беби-дэнс 3–5): малышка в розовой туту и кроссовках прыгает «звёздочкой»
I["letsdance-2-frunzenskaya"] = ("малышка в розовой юбке-туту и белых кроссовках",
    "прыгает «звёздочкой» — руки и ноги врозь — над зелёным коврик-матом танцкласса", bg("#F2FFE6", "#7CC95A", f'''
<rect x="18" y="104" width="92" height="12" rx="4" fill="#3FA34D" {s()}/>
<ellipse cx="64" cy="100" rx="20" ry="3.5" fill="#000" opacity=".15"/>
{limb(58, 74, 40, 94, SKIN, 5)}{limb(70, 74, 88, 94, SKIN, 5)}
<path d="M33 92 h12 v7 h-14 q-2 -7 2 -7Z M83 92 h12 q4 0 2 7 h-14Z" fill="#fff" {s('stroke-width="2.2"')}/>
<path d="M44 70 Q64 60 84 70 Q90 78 84 80 Q64 74 44 80 Q38 78 44 70Z" fill="#FF9CC8" {s()}/>
<path d="M54 46 H74 L76 70 H52Z" fill="#FFD9EA" {s()}/>
{limb(54, 50, 30, 30, SKIN, 5)}{limb(74, 50, 98, 30, SKIN, 5)}
{head(64, 34, 12, "#C77B3A")}
<circle cx="50" cy="26" r="5" fill="#C77B3A" {s('stroke-width="2"')}/><circle cx="78" cy="26" r="5" fill="#C77B3A" {s('stroke-width="2"')}/>
<path d="M45 22 l-3 -3 m3 3 l-4 1 M83 22 l3 -3 m-3 3 l4 1" {ln("#FF4F9A", 2.5)}/>
{sparkle(22, 58, 4.5)}{sparkle(108, 58, 4.5)}{sparkle(64, 12, 3.5)}
'''))

# 5 Ichi Music School (барабаны и гитара): бас-барабан ударной установки подпрыгивает от педали
I["ichi-music-leninsky"] = ("большой бас-барабан ударной установки с мордашкой на пластике",
    "подпрыгивает от удара колотушки педали, вокруг расходятся дуги «БУМ»", bg("#E9E4FF", "#4B3FA8", f'''
<rect x="0" y="108" width="128" height="20" fill="#2B2560"/>
<path d="M20 50 q-8 14 0 28 M12 44 q-12 20 0 40 M108 50 q8 14 0 28 M116 44 q12 20 0 40" fill="none" {ln("#FFD23A", 3.5)}/>
<ellipse cx="64" cy="64" rx="34" ry="34" fill="#E8344A" {s()}/>
<circle cx="64" cy="64" r="27" fill="#FFF8EC" {s()}/>
<g fill="#C0C6D0" {s('stroke-width="2"')}>{''.join(f'<rect x="{64+31*c-3:.1f}" y="{64+31*sn-3:.1f}" width="6" height="6" rx="1.5"/>' for c, sn in ((1,0),(-1,0),(0,1),(0,-1),(.7,.7),(-.7,.7),(.7,-.7),(-.7,-.7)))}</g>
{face(64, 62, 9, 0.85)}
<path d="M30 96 L40 104 M98 96 L88 104" {ln(O, 4)}/>
<path d="M64 98 V112" {ln(O, 4)}/><rect x="52" y="110" width="24" height="7" rx="2" fill="#555" {s('stroke-width="2"')}/>
<path d="M64 112 L56 100" {ln(O, 3.5)}/><circle cx="55" cy="98" r="5" fill="#fff" {s('stroke-width="2.4"')}/>
<text x="64" y="26" text-anchor="middle" font-family="Arial Black,Arial" font-weight="900" font-size="15" fill="#FFD23A" stroke="{O}" stroke-width="1.6">БУМ!</text>
'''))

# 6 Арт Фа: басовый ключ «фа» дирижирует хором из трёх нот
I["art-fa-myasnitskaya"] = ("басовый ключ «фа» с глазками и дирижёрской палочкой",
    "дирижирует хором из трёх поющих нот, стоящих лесенкой на ступеньках хоровых станков", bg("#FFF0E0", "#F08A4B", f'''
<path d="M70 100 H128 V128 H70Z M84 86 H128 V100 H84Z M98 72 H128 V86 H98Z" fill="#B8572A" {s('stroke-width="2.4"')}/>
<path d="M22 52 Q22 26 44 26 Q64 26 62 48 Q60 70 30 92" fill="none" {ln(O, 13)}/>
<path d="M22 52 Q22 26 44 26 Q64 26 62 48 Q60 70 30 92" fill="none" {ln("#2E2A5A", 8)}/>
<circle cx="24" cy="52" r="9" fill="#2E2A5A" {s()}/>
<circle cx="72" cy="36" r="4" fill="#2E2A5A" {s('stroke-width="2"')}/><circle cx="72" cy="52" r="4" fill="#2E2A5A" {s('stroke-width="2"')}/>
<circle cx="38" cy="40" r="4.2" fill="#fff"/><circle cx="50" cy="40" r="4.2" fill="#fff"/>
<circle cx="38" cy="41" r="2.4" fill="{O}"/><circle cx="50" cy="41" r="2.4" fill="{O}"/>
<path d="M40 50 Q44 54 48 50" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>
<path d="M58 58 L82 32" {ln(O, 5)}/><path d="M58 58 L82 32" {ln("#fff", 2.5)}/>
{note(84, 92, 0.9, "#2E2A5A")}{note(98, 78, 0.9, "#2E2A5A")}{note(112, 64, 0.9, "#2E2A5A")}
<g fill="#fff"><circle cx="80" cy="91" r="1.2"/><circle cx="94" cy="77" r="1.2"/><circle cx="108" cy="63" r="1.2"/></g>
{sparkle(100, 22, 5)}{sparkle(14, 108, 4)}
'''))

# 7 ДМШ им. Листа (ритмика, хор, инструменты): стальной музыкальный треугольник звенит
I["dmsh-lista-kosinskaya"] = ("стальной музыкальный треугольник с мордашкой",
    "висит на красной петельке, по нему стучит металлическая палочка, и во все стороны расходятся звонкие кольца", bg("#EAF6FF", "#5AA8E0", f'''
<circle cx="64" cy="70" r="46" fill="none" stroke="#fff" stroke-width="2.5" opacity=".5"/>
<circle cx="64" cy="70" r="56" fill="none" stroke="#fff" stroke-width="2" opacity=".35"/>
<path d="M64 10 V28" {ln("#E8344A", 3)}/>
<path d="M64 28 L100 96 H28Z" fill="none" {ln(O, 11)}/>
<path d="M64 28 L100 96 H28Z" fill="none" {ln("#C9D2DC", 6)}/>
<path d="M64 34 L94 92" stroke="#fff" stroke-width="2" opacity=".7"/>
{face(64, 74, 8, 0.75)}
<path d="M112 46 L88 70" {ln(O, 5)}/><path d="M112 46 L88 70" {ln("#AEB8C4", 2.5)}/>
<path d="M92 56 l-6 -4 M96 50 l-2 -6" {ln("#FFD23A", 3)}/>
{sparkle(22, 30, 5)}{sparkle(106, 108, 4)}
'''))

# 8 ДМШ им. Шостаковича (ансамбль «Завалинка»): балалайка на завалинке у избы
I["dmsh-shostakovicha-zhemchugovoy"] = ("красная балалайка с расписной декой и мордашкой",
    "сидит на бревенчатой завалинке у резного окошка избы и бренчит сама по себе", bg("#FFF6D8", "#E2B04A", f'''
<rect x="0" y="20" width="128" height="74" fill="#B7793A"/>
{''.join(f'<path d="M0 {y} H128" stroke="{O}" stroke-width="2" opacity=".55"/>' for y in (32, 46, 60, 74, 88))}
<rect x="80" y="30" width="34" height="30" fill="#BFE4F7" {s()}/><path d="M97 30 V60 M80 45 H114" {s('stroke-width="2.4"')}/>
<path d="M76 30 Q97 16 118 30 M76 60 H118 L112 66 H82Z" fill="#fff" {s('stroke-width="2.4"')}/>
<rect x="0" y="94" width="128" height="10" fill="#8A5527" {s('stroke-width="2.4"')}/><rect x="0" y="104" width="128" height="24" fill="#6E8F3A"/>
<path d="M44 22 L52 18 L58 50" fill="none" {ln(O, 7)}/><path d="M44 22 L52 18 L58 50" fill="none" {ln("#5A3418", 4)}/>
<path d="M58 48 L26 92 H92Z" fill="#E8344A" {s()}/>
<circle cx="58" cy="76" r="6" fill="#5A1A1A" {s('stroke-width="2"')}/>
<path d="M58 50 L58 90 M55 50 L50 90 M61 50 L66 90" stroke="#F5E6C8" stroke-width="1.3"/>
<path d="M36 86 q4 -6 8 0 q4 -6 8 0 M64 86 q4 -6 8 0 q4 -6 8 0" fill="none" {ln("#FFD23A", 2.2)}/>
{eye(48, 70, 0.6)}{eye(68, 70, 0.6)}
{note(18, 60, 0.7, "#5A3418")}{note(110, 82, 0.6, "#5A3418")}
'''))

# 9 Школа музыки Лизы Бонд: футляр гитары-агент «007»
I["bond-music-ukrainsky"] = ("чёрный футляр для гитары с мордашкой и наклейкой «007»",
    "стоит у двери на освещённом крыльце, из приоткрытой молнии выглядывают ноты", bg("#E4ECF2", "#5D7487", f'''
<rect x="78" y="12" width="40" height="88" fill="#7D4A2A" {s()}/><circle cx="86" cy="58" r="3" fill="#FFD23A" {s('stroke-width="1.6"')}/>
<rect x="0" y="100" width="128" height="28" fill="#9AA7B2"/><path d="M0 100 H128" {s('stroke-width="2.4"')}/>
<path d="M50 18 Q66 16 66 30 L66 40 Q80 46 78 66 Q86 76 84 92 Q80 108 50 108 Q20 108 16 92 Q14 76 22 66 Q20 46 34 40 L34 30 Q34 16 50 18Z" fill="#26222F" {s()}/>
<path d="M66 40 Q80 46 78 66 Q86 76 84 92" fill="none" stroke="#C9D2DC" stroke-width="2" stroke-dasharray="3 3"/>
<path d="M70 50 L80 44" {ln("#C9D2DC", 3)}/>
{note(92, 40, 0.75, "#FFD23A")}{note(104, 26, 0.65, "#fff")}
<rect x="32" y="78" width="30" height="13" rx="3" fill="#fff" {s('stroke-width="2"')}/>
<text x="47" y="89" text-anchor="middle" font-family="Arial Black,Arial" font-weight="900" font-size="11" fill="#E8344A">007</text>
<circle cx="42" cy="60" r="4.5" fill="#fff"/><circle cx="58" cy="60" r="4.5" fill="#fff"/>
<circle cx="43" cy="61" r="2.5" fill="{O}"/><circle cx="59" cy="61" r="2.5" fill="{O}"/>
<path d="M45 69 Q50 73 55 69" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>
'''))

# 10 Vocalette (детский вокальный ансамбль): ноты-ласточки сидят на нотном стане-проводах и поют
I["vocalette-novodmitrovskaya"] = ("нотный стан из пяти линеек-проводов между двумя столбиками",
    "на линейках, как ласточки на проводах, сидят пять нот-певуний с открытыми ротиками", bg("#FFFDE8", "#F6C93C", f'''
<rect x="8" y="30" width="8" height="98" fill="#8A5527" {s()}/><rect x="112" y="30" width="8" height="98" fill="#8A5527" {s()}/>
{''.join(f'<path d="M16 {y} Q64 {y+8} 112 {y}" fill="none" stroke="{O}" stroke-width="2.4"/>' for y in (44, 56, 68, 80, 92))}
{''.join(f'<g>{note(x, y, 0.95, c)}<circle cx="{x-1}" cy="{y-1}" r="1.1" fill="#fff"/><ellipse cx="{x+1}" cy="{y+1.5}" rx="1.4" ry="1.1" fill="#FF7FA8"/></g>'
        for x, y, c in ((30, 46, "#E8344A"), (48, 72, "#2E7DD1"), (64, 62, "#7A3EB8"), (80, 86, "#1E9E6A"), (96, 54, "#F06A1A")))}
<path d="M36 22 q3 -5 6 0 M70 30 q3 -5 6 0 M98 22 q3 -5 6 0" fill="none" {ln(O, 2)}/>
{sparkle(58, 18, 4, "#fff")}{sparkle(110, 108, 4, "#fff")}
'''))

# 11 КиноРебёнок (актёрская киношкола): мальчик-актёр в огромных тёмных очках позирует под вспышками
I["kinorebenok-khodynsky"] = ("мальчик-актёр в огромных кинозвёздных тёмных очках и красном шарфике",
    "позирует, уперев руку в бок, под вспышками фотоаппаратов на фоне тёмного задника со звёздочками", bg("#3A2E6E", "#120D2E", f'''
{''.join(sparkle(x, y, r, "#FFE27A") for x, y, r in ((16, 40, 3), (26, 84, 2.5), (108, 30, 3), (112, 76, 2.5), (90, 14, 2)))}
<path d="M0 30 L24 44 L0 52Z M128 34 L104 46 L128 56Z" fill="#fff" opacity=".85"/>
<path d="M50 74 H78 L84 128 H44Z" fill="#2E7DD1" {s()}/>
{limb(52, 80, 40, 98, "#2E7DD1", 6)}<circle cx="40" cy="100" r="5" fill="{SKIN}" {s('stroke-width="2.2"')}/>
<path d="M76 80 L90 90 L78 98" fill="none" {ln(O, 9)}/><path d="M76 80 L90 90 L78 98" fill="none" {ln("#2E7DD1", 6)}/>
<path d="M50 72 Q64 80 78 72 L80 80 Q64 86 48 80Z" fill="#E8344A" {s('stroke-width="2.4"')}/><path d="M74 80 L80 98 L70 96Z" fill="#E8344A" {s('stroke-width="2.2"')}/>
<circle cx="64" cy="52" r="18" fill="{SKIN}" {s()}/>
<path d="M46 50 Q44 30 64 30 Q84 30 82 50 Q76 40 64 40 Q52 40 46 50Z" fill="#E0A23A" {s('stroke-width="2.4"')}/>
<path d="M42 50 H86" {ln(O, 3)}/>
<rect x="44" y="47" width="18" height="12" rx="5" fill="#1E1A2E" {s('stroke-width="2.2"')}/><rect x="66" y="47" width="18" height="12" rx="5" fill="#1E1A2E" {s('stroke-width="2.2"')}/>
<path d="M48 50 l4 0 M70 50 l4 0" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
<path d="M56 64 Q64 70 72 64" fill="none" {s('stroke-width="2.2"')}/>
'''))

# 12 Балетка: девочка в голубом купальнике у станка делает плие перед зеркалом
I["baletka-yablochkova"] = ("девочка в бледно-голубом купальнике с пучком на макушке",
    "держится за деревянный балетный станок и делает плие перед высоким зеркалом зала", bg("#F3F0FF", "#A99BE6", f'''
<rect x="64" y="10" width="54" height="94" fill="#DCE9F5" {s()}/><path d="M74 20 L90 36 M82 16 L104 38" stroke="#fff" stroke-width="3" opacity=".8"/>
<rect x="0" y="104" width="128" height="24" fill="#C49A6C"/><path d="M0 104 H128" {s('stroke-width="2.4"')}/>
<path d="M8 62 H120" {ln(O, 8)}/><path d="M8 62 H120" {ln("#D9A86A", 5)}/>
<path d="M20 62 V104 M108 62 V104" {ln(O, 3)}/>
{limb(46, 82, 34, 94, "#FFC9D9", 5)}{limb(34, 94, 38, 106, "#FFC9D9", 5)}
{limb(54, 82, 66, 94, "#FFC9D9", 5)}{limb(66, 94, 62, 106, "#FFC9D9", 5)}
<path d="M32 104 h10 M58 104 h10" {ln("#FF8FB3", 5)}/>
<path d="M42 54 Q50 50 58 54 L58 84 Q50 88 42 84Z" fill="#BFE0FF" {s()}/>
{limb(56, 58, 70, 62, SKIN, 4.5)}{limb(44, 58, 30, 46, SKIN, 4.5)}
{head(50, 40, 10, "#6B3E1F", 0.5)}
<circle cx="50" cy="26" r="5.5" fill="#6B3E1F" {s('stroke-width="2"')}/>
<circle cx="92" cy="80" r="6" fill="#BFE0FF" opacity=".7"/>
{sparkle(30, 24, 4)}{sparkle(110, 116, 3)}
'''))

# 13 Tatiana's Music Studio: бас-гитара прислонилась к усилителю-комбику
I["tatiana-music-beregovaya"] = ("бирюзовая бас-гитара с четырьмя толстыми струнами и мордашкой на корпусе",
    "прислонилась к оранжевому усилителю-комбику, гудит низкой нотой, и динамик комбика дрожит", bg("#E2FBF6", "#3DBFA5", f'''
<rect x="0" y="108" width="128" height="20" fill="#20675A"/>
<rect x="70" y="62" width="48" height="48" rx="5" fill="#F07A2A" {s()}/>
<circle cx="94" cy="88" r="15" fill="#3A2F2A" {s()}/><circle cx="94" cy="88" r="6" fill="#6D5D52"/>
<rect x="74" y="66" width="40" height="7" rx="2" fill="#26222F"/><circle cx="80" cy="69.5" r="1.8" fill="#FFD23A"/><circle cx="88" cy="69.5" r="1.8" fill="#FFD23A"/>
<path d="M108 84 q6 4 0 8 M114 80 q9 8 0 16" fill="none" {ln("#fff", 2.4)}/>
<path d="M54 10 L60 6 L66 12 L62 54" fill="none" {ln(O, 8)}/><path d="M54 10 L60 6 L66 12 L62 54" fill="none" {ln("#5A3418", 5)}/>
<g fill="#E0E0E0" {s('stroke-width="1.6"')}><circle cx="52" cy="12" r="2.5"/><circle cx="54" cy="20" r="2.5"/><circle cx="68" cy="16" r="2.5"/><circle cx="66" cy="24" r="2.5"/></g>
<path d="M62 52 Q80 50 78 70 Q86 82 74 102 Q60 116 40 106 Q24 96 34 80 Q30 62 46 58 Q52 52 62 52Z" fill="#27C2B0" {s()}/>
<path d="M56 56 L50 100 M59 56 L54 100 M62 56 L58 100 M65 56 L62 100" stroke="#F5F5F5" stroke-width="1.4"/>
<rect x="46" y="88" width="20" height="6" rx="2" fill="#26222F"/>
{eye(46, 74, 0.6)}{eye(70, 74, 0.6)}<path d="M54 82 Q58 85 62 82" fill="none" {s('stroke-width="1.8"')}/>
{sparkle(20, 30, 4.5)}{sparkle(104, 30, 3.5)}
'''))

# 14 Школа эстрадного искусства Юрия Гончара: ретро-микрофон «ушастый» на эстраде с гирляндой лампочек
I["gonchar-school-universitetsky"] = ("серебряный ретро-микрофон 50-х с решёткой-«ушами» на хромированной стойке",
    "стоит посреди эстрады под аркой из жёлтых лампочек-гирлянды и сам себе подмигивает", bg("#FFE6E6", "#B8323C", f'''
<path d="M8 128 V58 Q64 -4 120 58 V128" fill="none" {ln(O, 6)}/>
{''.join(f'<circle cx="{64 + 56*__import__("math").cos(a):.1f}" cy="{58 - 56*__import__("math").sin(a)*1.05:.1f}" r="4" fill="#FFE27A" {s("stroke-width=\"1.8\"")}/>' for a in [i*3.1416/10 for i in range(11)])}
<rect x="0" y="108" width="128" height="20" fill="#5A1A20"/><path d="M0 108 H128" {s('stroke-width="2.4"')}/>
<path d="M64 78 V108 M50 110 H78" {ln(O, 7)}/><path d="M64 78 V108 M50 110 H78" {ln("#D8DDE3", 4)}/>
<rect x="44" y="34" width="40" height="46" rx="16" fill="#D8DDE3" {s()}/>
<rect x="50" y="40" width="28" height="34" rx="11" fill="#B4BCC6"/>
{''.join(f'<path d="M52 {y} H76" stroke="#8C96A2" stroke-width="1.6"/>' for y in (46, 52, 58, 64, 70))}
<path d="M44 52 H36 V62 H44 M84 52 H92 V62 H84" fill="#D8DDE3" {s('stroke-width="2.4"')}/>
<circle cx="57" cy="56" r="4.4" fill="#fff" {s('stroke-width="1.6"')}/><circle cx="57" cy="57" r="2.4" fill="{O}"/>
<path d="M67 57 Q71 54 75 57" fill="none" {s('stroke-width="2.4"')}/>
<path d="M59 66 Q64 70 69 66" fill="none" {s('stroke-width="2"')}/>
'''))

# 15 Школа вокала Екатерины Медведевой (с 1,5 лет): малышка в бодике поёт «А-а-а» в игрушечный микрофон
I["medvedeva-vocal-presnenskaya"] = ("полуторагодовалая малышка в жёлтом бодике с бантиком на макушке",
    "сидит на пушистом коврике и во весь голос поёт «А-а-а» в розовый игрушечный микрофон, вокруг летят ноты-сердечки", bg("#FFF0F5", "#E58FB2", f'''
<ellipse cx="64" cy="112" rx="50" ry="12" fill="#FFFFFF" opacity=".75" {s('stroke-width="2"')}/>
<ellipse cx="64" cy="98" rx="30" ry="14" fill="#FFD84A" {s()}/>
<circle cx="44" cy="104" r="7" fill="{SKIN}" {s('stroke-width="2.4"')}/><circle cx="84" cy="104" r="7" fill="{SKIN}" {s('stroke-width="2.4"')}/>
<path d="M44 72 Q64 64 84 72 L86 98 H42Z" fill="#FFD84A" {s()}/>
<circle cx="64" cy="48" r="20" fill="{SKIN}" {s()}/>
<path d="M60 28 q4 -6 8 0" fill="none" {ln(O, 2.4)}/>
<path d="M64 30 L54 22 L54 36Z M64 30 L74 22 L74 36Z" fill="#FF5FA2" {s('stroke-width="2.2"')}/>
<path d="M54 46 q3 -3 6 0 M68 46 q3 -3 6 0" fill="none" {ln(O, 2.4)}/>
<ellipse cx="64" cy="58" rx="4.5" ry="5.5" fill="#B0303E" {s('stroke-width="2"')}/>
<ellipse cx="50" cy="54" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/><ellipse cx="78" cy="54" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/>
{limb(76, 76, 88, 66, SKIN, 5)}
<path d="M88 66 L94 52" {ln(O, 6)}/><path d="M88 66 L94 52" {ln("#FF8FC0", 3.5)}/>
<circle cx="96" cy="47" r="8" fill="#FF5FA2" {s()}/>
<path d="M100 26 c-3 -4 -8 0 -4 4 l4 4 4 -4 c4 -4 -1 -8 -4 -4Z M20 40 c-3 -4 -8 0 -4 4 l4 4 4 -4 c4 -4 -1 -8 -4 -4Z" fill="#E8344A" {s('stroke-width="1.6"')}/>
<text x="28" y="74" font-family="Arial Black,Arial" font-weight="900" font-size="12" fill="#fff" stroke="{O}" stroke-width="1.2">А-а!</text>
'''))

if __name__ == "__main__":
    reg = os.path.join(ROOT, "icons-src", "subjects.txt")
    lines = open(reg, encoding="utf-8").read().splitlines()
    lines = [l for l in lines if l.split(" — ")[0] not in I]
    for pid, (hero, scene, body) in I.items():
        open(os.path.join(ROOT, "icons-src", f"{pid}.svg"), "w").write(body)
        if True:
            lines.append(f"{pid} — герой: {hero} | сцена: {scene}")
    open(reg, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(len(I))
