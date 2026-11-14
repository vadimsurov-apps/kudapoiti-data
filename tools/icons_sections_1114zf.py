"""Иконки робота sections 14.11 (партия 1114zf/zg). Каждая придумана и нарисована отдельно (правило абсолютной уникальности):
свой герой, своя сцена, своя компоновка и палитра.  python3 tools/icons_sections_1114zf.py [id ...]"""
import os
from draw_icons import s, eye, face, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def svg(a, b, body, cx="38%", cy="28%"):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
<defs>
 <radialGradient id="g" cx="{cx}" cy="{cy}" r="85%"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></radialGradient>
 <clipPath id="c"><circle cx="64" cy="64" r="61"/></clipPath>
</defs>
<circle cx="64" cy="64" r="61" fill="url(#g)"/>
<g clip-path="url(#c)">{body}</g>
<ellipse cx="44" cy="22" rx="20" ry="7" fill="#fff" opacity=".3"/>
</svg>'''


def blush(x, y, k=1.0):
    return f'<ellipse cx="{x}" cy="{y}" rx="{4*k}" ry="{2.4*k}" fill="#FF7FA8" opacity=".6"/>'


def smile(x, y, w=5, sw=2.4):
    return f'<path d="M{x-w} {y} Q{x} {y+w*0.9} {x+w} {y}" fill="none" {s(f"stroke-width=\"{sw}\"")}/>'


def glove(x, y, k=1.0, col="#E53935", flip=False):
    """боксёрская перчатка (кулак вправо, манжета слева)"""
    t = f'translate({x} {y}) scale({-k if flip else k} {k})'
    return (f'<g transform="{t}"><path d="M-14 -10 Q-14 -20 0 -20 Q16 -20 16 -4 Q16 10 2 12 L-14 12Z" fill="{col}" {s("stroke-width=\"2.6\"")}/>'
            f'<path d="M-6 -4 Q2 -10 8 -4" fill="none" stroke="#fff" stroke-width="2" opacity=".6"/>'
            f'<rect x="-22" y="-8" width="9" height="20" rx="3" fill="#fff" {s("stroke-width=\"2.4\"")}/></g>')


I = {}

# 1. Спортшкола Реутова (бокс с рингом, самбо, дзюдо…): красная угловая стойка ринга с мордашкой и золотой медалькой держит
#    три натянутых каната над синим ковром; фон лаймовый
I["reutov-sportschool-oktyabrya"] = svg("#F3FFD1", "#9ED24B", f'''
<path d="M-4 96 L132 96 V132 H-4Z" fill="#2F6FD6" {s('stroke-width="2.6"')}/>
<path d="M8 108 H120" stroke="#5B92EA" stroke-width="3" opacity=".7"/>
<path d="M50 50 L128 44 M50 64 L128 60 M50 78 L128 76" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M50 50 L128 44" stroke="#E53935" stroke-width="4" stroke-linecap="round"/>
<path d="M50 64 L128 60" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round"/>
<path d="M50 78 L128 76" stroke="#1E5AC8" stroke-width="4" stroke-linecap="round"/>
<rect x="28" y="30" width="30" height="72" rx="10" fill="#E53935" {s()}/>
<rect x="24" y="96" width="38" height="10" rx="4" fill="#B71C1C" {s('stroke-width="2.6"')}/>
{eye(37, 52, .9)}{eye(50, 52, .9)}{blush(33, 60, .8)}{blush(54, 60, .8)}
{smile(43.5, 60, 5)}
<path d="M34 66 L43 80 L52 66" fill="none" stroke="#1E88E5" stroke-width="3.4"/>
<circle cx="43" cy="84" r="7" fill="#FFC72C" {s('stroke-width="2.4"')}/>
<path d="M43 80.5 V87.5" stroke="#B8860B" stroke-width="2"/>
{sparkle(64, 34, 4)}{sparkle(110, 30, 3)}
''')

# 2. «Хаски», Салтыковская ул.: оранжевый баскетбольный мяч в синей повязке на лбу висит, ухватившись ручками за кольцо после
#    броска, сетка колышется; фон вечерний сиреневый
I["husky-basket-saltykovskaya"] = svg("#EEE3FF", "#9A7FE0", f'''
<rect x="78" y="10" width="44" height="30" rx="3" fill="#FFFFFF" {s('stroke-width="2.6"')}/>
<rect x="92" y="20" width="16" height="12" fill="none" stroke="#E53935" stroke-width="2.4"/>
<path d="M30 40 H100" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M30 40 H100" stroke="#FF7043" stroke-width="3.6" stroke-linecap="round"/>
<path d="M36 42 L44 62 M52 42 L52 62 M66 42 L62 62 M82 42 L74 62 M94 42 L84 62 M40 52 H90 M46 62 H80" fill="none" stroke="#FFFFFF" stroke-width="2.2"/>
<circle cx="56" cy="84" r="27" fill="#FF8F1F" {s()}/>
<path d="M29 84 H83 M56 57 V111 M36 66 Q56 84 36 102 M76 66 Q56 84 76 102" fill="none" stroke="{O}" stroke-width="2.4"/>
<path d="M32 70 Q56 60 80 70" fill="none" stroke="#1E5AC8" stroke-width="7" stroke-linecap="round"/>
<path d="M78 68 l8 -6 M78 70 l9 0" stroke="#1E5AC8" stroke-width="3" stroke-linecap="round"/>
<path d="M40 64 Q34 52 38 42 M72 64 Q78 52 74 42" fill="none" {s('stroke-width="5"')}/>
<path d="M40 64 Q34 52 38 42 M72 64 Q78 52 74 42" fill="none" stroke="#FF8F1F" stroke-width="2.6"/>
{eye(47, 84, .9)}{eye(65, 84, .9)}{blush(42, 93, .8)}{blush(70, 93, .8)}
<ellipse cx="56" cy="95" rx="4" ry="4.6" fill="{O}"/>
''', cx="30%", cy="70%")

# 3. «Легион Кудо», Сокол: белый шлем кудо с прозрачным забралом, внутри видны глазки; сидит на татами рядом с веточкой
#    сакуры; фон тёмно-бирюзовый
I["legion-kudo-sokol"] = svg("#BDEDE6", "#1F8C86", f'''
<path d="M-4 100 H132 V132 H-4Z" fill="#E9D8A6" {s('stroke-width="2.6"')}/>
<path d="M-4 112 H132 M40 100 V132 M88 100 V132" stroke="#C9B37A" stroke-width="2.4"/>
<path d="M30 96 Q24 40 64 32 Q104 40 98 96 Z" fill="#FFFFFF" {s()}/>
<path d="M38 60 Q64 48 90 60 L88 90 Q64 100 40 90 Z" fill="#BFE8FF" opacity=".75" {s('stroke-width="2.6"')}/>
<path d="M44 62 Q52 58 58 60" fill="none" stroke="#fff" stroke-width="3" opacity=".9"/>
{eye(55, 74, 1)}{eye(73, 74, 1)}{smile(64, 84, 5)}
<path d="M30 96 H98" {s()}/>
<path d="M36 50 Q64 38 92 50" fill="none" stroke="#1E5AC8" stroke-width="3"/>
<path d="M100 98 Q104 80 116 70" fill="none" stroke="#6D4C41" stroke-width="3" stroke-linecap="round"/>
<circle cx="116" cy="70" r="5" fill="#FFB7CF" {s('stroke-width="1.8"')}/><circle cx="106" cy="82" r="4.4" fill="#FFB7CF" {s('stroke-width="1.8"')}/>
<circle cx="116" cy="70" r="1.6" fill="#E91E63"/><circle cx="106" cy="82" r="1.4" fill="#E91E63"/>
''')

# 4. «Шершень», Нежинская: полосатый шершень в красных боксёрских перчатках порхает и бьёт джеб по маленькой воздушной груше;
#    фон медово-жёлтый
I["shershen-nezhinskaya"] = svg("#FFF4C2", "#F5B731", f'''
<path d="M100 14 V40" stroke="{O}" stroke-width="2.4"/>
<ellipse cx="100" cy="50" rx="10" ry="12" fill="#8D6E63" {s('stroke-width="2.6"')}/>
<ellipse cx="44" cy="40" rx="18" ry="10" fill="#E3F6FF" opacity=".9" transform="rotate(-25 44 40)" {s('stroke-width="2.2"')}/>
<ellipse cx="66" cy="34" rx="16" ry="9" fill="#E3F6FF" opacity=".9" transform="rotate(20 66 34)" {s('stroke-width="2.2"')}/>
<ellipse cx="40" cy="78" rx="26" ry="17" fill="#FFC107" transform="rotate(-15 40 78)" {s()}/>
<path d="M24 70 Q28 84 34 92 M38 64 Q42 80 48 90" fill="none" stroke="{O}" stroke-width="6"/>
<path d="M14 88 L4 98 L18 94Z" fill="{O}"/>
<circle cx="70" cy="64" r="16" fill="#FFC107" {s()}/>
<path d="M62 50 Q58 40 54 38 M74 49 Q78 40 84 38" fill="none" {s('stroke-width="2.4"')}/>
{eye(66, 63, .85)}{eye(77, 62, .85)}{smile(72, 71, 4)}
{glove(92, 60, .8)}
{glove(56, 92, .7, "#C62828")}
{sparkle(88, 40, 3.5)}{sparkle(112, 70, 3)}
''', cx="60%", cy="30%")

# 5. Kensei, Митино: журавлик-оригами в синем дзюдоги бросает через бедро мягкую подушку на жёлтом татами; фон светло-голубой
I["kensei-angelov"] = svg("#EAF6FF", "#7FBDF0", f'''
<path d="M-4 102 H132 V132 H-4Z" fill="#F7D35C" {s('stroke-width="2.6"')}/>
<path d="M30 102 V132 M74 102 V132 M110 102 V132" stroke="#D9B23A" stroke-width="2.4"/>
<path d="M44 96 L52 60 L76 60 L84 96 Z" fill="#1E5AC8" {s()}/>
<path d="M58 60 L64 76 L70 60" fill="none" stroke="#FFFFFF" stroke-width="2.6"/>
<path d="M50 82 H78" stroke="#FFFFFF" stroke-width="5"/><path d="M50 82 H78" stroke="#111" stroke-width="2"/>
<path d="M50 60 L28 40 L60 50 Z" fill="#FFFFFF" {s('stroke-width="2.6"')}/>
<path d="M78 60 L104 34 L70 52 Z" fill="#FFFFFF" {s('stroke-width="2.6"')}/>
<path d="M64 60 L64 40 L80 26 L72 42 Z" fill="#FFFFFF" {s('stroke-width="2.6"')}/>
<path d="M80 26 L88 28 L80 32Z" fill="#E53935" {s('stroke-width="1.8"')}/>
{eye(71, 36, .7)}
<path d="M86 64 Q104 54 112 72 Q118 88 100 92 Q88 90 86 64Z" fill="#FFAFC8" {s('stroke-width="2.6"')}/>
<path d="M94 70 l4 4 m0 -4 l-4 4" stroke="{O}" stroke-width="1.8"/>
<path d="M104 46 Q112 50 112 58" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 4"/>
''')

# 6. Top Fight, Пятницкое ш.: чёрно-золотая боксёрская груша в тайской повязке монгкон раскачивается на цепи, на ней
#    звёздочки от ударов; фон тёмно-красный
I["top-fight-pyatnitskoe"] = svg("#FF9C8A", "#A3201B", f'''
<path d="M64 0 V20" stroke="#B0BEC5" stroke-width="4" stroke-dasharray="4 3"/>
<path d="M54 22 H74 L72 28 H56Z" fill="#B0BEC5" {s('stroke-width="2.2"')}/>
<rect x="40" y="28" width="48" height="80" rx="20" fill="#212121" {s()}/>
<rect x="40" y="88" width="48" height="10" fill="#FFC107"/>
<rect x="40" y="38" width="48" height="10" fill="#FFC107"/>
<path d="M36 52 Q64 42 92 52 L92 60 Q64 50 36 60Z" fill="#E53935" {s('stroke-width="2.4"')}/>
<path d="M92 56 Q104 52 108 62 Q100 60 96 66" fill="#E53935" {s('stroke-width="2.2"')}/>
<circle cx="58" cy="72" r="5" fill="#fff"/><circle cx="58" cy="72" r="2.6" fill="{O}"/>
<circle cx="72" cy="72" r="5" fill="#fff"/><circle cx="72" cy="72" r="2.6" fill="{O}"/>
<path d="M58 82 Q65 87 72 82" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
{sparkle(30, 70, 6, "#FFE082")}{sparkle(98, 84, 5, "#FFE082")}{sparkle(26, 92, 3.5, "#FFE082")}
''', cx="50%", cy="30%")

# 7. ЦХГ «Открытие», Каширское ш.: золотой ключик с бантиком отпирает замочек, из скважины вылетает розовая спираль гимнастической
#    ленты; фон бирюзовый
I["otkrytie-gym-kashirskoe"] = svg("#D3FBF5", "#3CC4B4", f'''
<rect x="18" y="62" width="40" height="38" rx="8" fill="#FFB300" {s()}/>
<path d="M26 62 V48 Q26 32 38 32 Q50 32 50 48" fill="none" {s('stroke-width="6"')}/>
<path d="M26 62 V48 Q26 32 38 32 Q50 32 50 48" fill="none" stroke="#B0BEC5" stroke-width="3"/>
<circle cx="38" cy="78" r="4" fill="{O}"/><path d="M38 80 V90" stroke="{O}" stroke-width="3.6"/>
<path d="M42 78 Q70 70 70 54 Q70 40 84 40 Q100 40 98 56 Q96 70 84 66 Q76 62 82 54 Q90 48 100 30 Q108 18 120 16" fill="none" stroke="#FF4F9A" stroke-width="5" stroke-linecap="round"/>
<circle cx="88" cy="96" r="13" fill="#FFD54F" {s()}/>
<circle cx="88" cy="96" r="5" fill="#FFF3C4" {s('stroke-width="2"')}/>
<path d="M76 94 L50 88 M60 90 L58 96 M66 92 L64 98" fill="none" {s('stroke-width="5"')}/>
<path d="M76 94 L50 88" stroke="#FFD54F" stroke-width="2.4"/>
{eye(84, 108, .5)}{eye(93, 108, .5)}
<path d="M96 84 Q104 76 110 84 Q104 88 96 84Z M96 84 Q94 74 102 70" fill="#FF4F9A" {s('stroke-width="2"')}/>
{sparkle(110, 52, 4)}{sparkle(60, 28, 3)}
''')

# 8. ЦХГ «Открытие», Южное Бутово: голубая гимнастическая булава с мордашкой и короной из страз стоит на одной ручке на ковре,
#    рядом лежит вторая булава; фон персиковый
I["otkrytie-gym-dzhankoyskaya"] = svg("#FFEBDD", "#FFAA7F", f'''
<path d="M-4 104 H132 V132 H-4Z" fill="#7E57C2" {s('stroke-width="2.6"')}/>
<path d="M64 102 L58 70 Q50 50 52 36 Q56 20 64 20 Q72 20 76 36 Q78 50 70 70 Z" fill="#4FC3F7" {s()}/>
<rect x="56" y="96" width="16" height="8" rx="3" fill="#4FC3F7" {s('stroke-width="2.4"')}/>
<circle cx="64" cy="18" r="6" fill="#4FC3F7" {s('stroke-width="2.6"')}/>
<path d="M52 40 L56 28 L60 36 L64 24 L68 36 L72 28 L76 40Z" fill="#FFD54F" {s('stroke-width="2.2"')}/>
<circle cx="64" cy="31" r="2" fill="#E91E63"/>
{eye(59, 52, .8)}{eye(70, 52, .8)}{smile(64.5, 60, 4)}{blush(55, 58, .6)}{blush(74, 58, .6)}
<path d="M20 100 L56 90" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M20 100 L56 90" stroke="#81D4FA" stroke-width="5.6" stroke-linecap="round"/>
<path d="M78 80 l14 -6 M78 66 l16 2" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
{sparkle(100, 40, 4)}{sparkle(28, 50, 3)}
''', cx="60%", cy="30%")

# 9. ЦХГ «Открытие», Царицыно: фиолетовый гимнастический мяч с блёстками и мордашкой катится по дорожке из звёздочек под
#    стрельчатой аркой Царицына; фон розово-лиловый
I["otkrytie-gym-sevanskaya"] = svg("#FCE4F5", "#D17CC6", f'''
<path d="M14 120 V58 Q14 22 64 18 Q114 22 114 58 V120" fill="none" stroke="#B23A48" stroke-width="10"/>
<path d="M14 120 V58 Q14 22 64 18 Q114 22 114 58 V120" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-dasharray="6 6"/>
{sparkle(28, 104, 4)}{sparkle(42, 100, 3.4)}{sparkle(56, 102, 3)}
<circle cx="80" cy="82" r="24" fill="#8E44D8" {s()}/>
<path d="M62 70 Q74 58 90 62" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".6"/>
<circle cx="70" cy="94" r="1.8" fill="#FFF59D"/><circle cx="92" cy="96" r="1.8" fill="#FFF59D"/><circle cx="96" cy="72" r="1.6" fill="#FFF59D"/>
{face(80, 82, 8, .9)}
''')

# 10. ЦХГ «Открытие», Кантемировская: жёлтая гимнастическая скакалка, на красных ручках две мордашки; скакалка сама
#     закручивается восьмёркой над синим ковром; фон мятный
I["otkrytie-gym-erevanskaya"] = svg("#E3FFF1", "#62D29C", f'''
<path d="M-4 108 H132 V132 H-4Z" fill="#3949AB" {s('stroke-width="2.6"')}/>
<path d="M30 40 C30 10 98 10 98 40 C98 70 30 70 30 92 M30 40 C30 70 98 70 98 92" fill="none" {s('stroke-width="7"')}/>
<path d="M30 40 C30 10 98 10 98 40 C98 70 30 70 30 92 M30 40 C30 70 98 70 98 92" fill="none" stroke="#FFE14D" stroke-width="3.6"/>
<rect x="18" y="88" width="24" height="18" rx="8" fill="#E53935" {s()}/>
<rect x="86" y="88" width="24" height="18" rx="8" fill="#E53935" {s()}/>
{eye(26, 96, .6)}{eye(34, 96, .6)}{eye(94, 96, .6)}{eye(102, 96, .6)}
<path d="M27 101 Q30 103 33 101 M95 101 Q98 103 101 101" fill="none" stroke="#fff" stroke-width="1.6"/>
{sparkle(64, 54, 5)}{sparkle(112, 24, 3)}
''')

# 11. СДЦ «Полёт», Судостроительная: красная куртка-самбовка с мордашкой и лётными очками-авиаторами летит над облаками,
#    раскинув рукава как крылья; фон небесный
I["polet-sambo-sudostroitelnaya"] = svg("#EAF8FF", "#6EC1F2", f'''
<ellipse cx="26" cy="100" rx="22" ry="10" fill="#fff"/><ellipse cx="44" cy="96" rx="16" ry="10" fill="#fff"/>
<ellipse cx="100" cy="108" rx="24" ry="9" fill="#fff"/>
<path d="M44 46 L10 58 L14 72 L44 66 Z" fill="#E53935" {s()}/>
<path d="M84 46 L118 58 L114 72 L84 66 Z" fill="#E53935" {s()}/>
<path d="M44 40 Q64 34 84 40 L86 90 Q64 96 42 90 Z" fill="#E53935" {s()}/>
<path d="M54 40 L64 62 L74 40" fill="#FFCDD2" {s('stroke-width="2.4"')}/>
<path d="M42 78 Q64 84 86 78" fill="none" stroke="#C62828" stroke-width="7"/>
<path d="M42 78 Q64 84 86 78" fill="none" {s('stroke-width="2"')}/>
<path d="M60 82 L54 98 M68 82 L74 98" stroke="#C62828" stroke-width="5" stroke-linecap="round"/>
<circle cx="56" cy="30" r="9" fill="#BFE8FF" {s('stroke-width="2.6"')}/><circle cx="74" cy="30" r="9" fill="#BFE8FF" {s('stroke-width="2.6"')}/>
<path d="M65 30 H65" {s()}/>
<path d="M46 28 Q64 14 84 28" fill="none" stroke="#795548" stroke-width="4"/>
{eye(56, 31, .6)}{eye(74, 31, .6)}
<path d="M58 50 Q64 54 70 50" fill="none" {s('stroke-width="2.2"')}/>
<path d="M2 64 H-4 M6 78 L-2 80" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', cx="50%", cy="20%")

# 12. СДЦ «Полёт», Каширское ш.: бумажный самолётик, подпоясанный красным поясом самбо, заходит на посадку на зелёный ковёр и
#    оставляет пунктирный след; фон светло-жёлтый
I["polet-sambo-kashirskoe-55"] = svg("#FFFCE0", "#F2D35B", f'''
<path d="M-4 106 H132 V132 H-4Z" fill="#43A047" {s('stroke-width="2.6"')}/>
<path d="M8 30 Q40 30 56 52" fill="none" stroke="#fff" stroke-width="3.4" stroke-dasharray="5 6" stroke-linecap="round"/>
<path d="M40 48 L118 88 L60 70 Z" fill="#FFFFFF" {s()}/>
<path d="M40 48 L60 70 L56 96 Z" fill="#E3EEF7" {s()}/>
<path d="M60 70 L118 88" {s('stroke-width="2.4"')}/>
<path d="M66 60 L72 84" stroke="#E53935" stroke-width="7"/>
<path d="M66 60 L72 84" fill="none" {s('stroke-width="2"')}/>
<path d="M72 80 L80 94 M70 82 L64 96" stroke="#E53935" stroke-width="4" stroke-linecap="round"/>
{eye(86, 74, .75)}{eye(97, 78, .75)}
<path d="M86 84 Q91 88 96 86" fill="none" {s('stroke-width="2"')}/>
<circle cx="100" cy="30" r="12" fill="#FFF59D" opacity=".9"/>
''', cx="80%", cy="20%")

# 13. СДЦ «Полёт», Медынская: круглый ковёр самбо (красный круг на синем) с мордашкой смотрит вверх на пролетающий
#    полосатый воздушный шар; фон закатный оранжевый
I["polet-sambo-medynskaya"] = svg("#FFE0B8", "#F77E2E", f'''
<ellipse cx="64" cy="98" rx="56" ry="22" fill="#1E5AC8" {s()}/>
<ellipse cx="64" cy="98" rx="38" ry="14" fill="#E53935" {s('stroke-width="2.6"')}/>
<ellipse cx="64" cy="98" rx="24" ry="8" fill="#1E5AC8"/>
{eye(54, 94, .8)}{eye(74, 94, .8)}
<ellipse cx="64" cy="102" rx="3.5" ry="2.4" fill="{O}"/>
<path d="M64 14 Q90 14 90 38 Q90 54 70 62 H58 Q38 54 38 38 Q38 14 64 14Z" fill="#FFD54F" {s()}/>
<path d="M50 18 Q46 40 60 62 M78 18 Q82 40 68 62" fill="none" stroke="#E53935" stroke-width="5"/>
<path d="M58 62 L60 72 M70 62 L68 72" {s('stroke-width="2"')}/>
<rect x="57" y="72" width="14" height="9" rx="2" fill="#8D6E63" {s('stroke-width="2.4"')}/>
{sparkle(104, 26, 4)}{sparkle(22, 40, 3)}
''', cx="50%", cy="30%")

# 14. СК «Отвага», Зелёная зона: смелый зелёный кузнечик в красной самбовке бросает через плечо большой одуванчик на траве;
#    фон зелёный
I["otvaga-zelenaya-zona"] = svg("#E9FFD8", "#5DBB46", f'''
<path d="M-4 108 Q20 100 40 108 Q64 100 88 108 Q110 100 132 108 V132 H-4Z" fill="#2E7D32" {s('stroke-width="2.4"')}/>
<path d="M28 106 L22 70 L44 62 Z" fill="#7CB342" {s()}/>
<path d="M22 70 L12 98 M34 64 L40 100" {s('stroke-width="3"')}/>
<path d="M36 76 Q36 56 54 54 Q70 54 70 74 L64 88 H42 Z" fill="#E53935" {s()}/>
<path d="M46 56 L54 70 L62 56" fill="#FFCDD2" {s('stroke-width="2"')}/>
<path d="M40 84 H66" stroke="#B71C1C" stroke-width="4"/>
<circle cx="56" cy="40" r="15" fill="#8BC34A" {s()}/>
<path d="M50 26 Q44 10 36 8 M60 26 Q66 10 76 6" fill="none" {s('stroke-width="2.4"')}/>
{eye(51, 39, .85)}{eye(62, 39, .85)}{smile(57, 46, 4)}
<path d="M68 60 Q84 50 92 40" fill="none" {s('stroke-width="5"')}/>
<path d="M68 60 Q84 50 92 40" fill="none" stroke="#E53935" stroke-width="2.6"/>
<path d="M92 40 Q100 60 104 92" fill="none" stroke="#558B2F" stroke-width="3.4"/>
<circle cx="92" cy="30" r="14" fill="#FFF9C4" {s('stroke-width="2.4"')}/>
<path d="M92 16 V44 M78 30 H106 M82 20 L102 40 M102 20 L82 40" stroke="#FFE57F" stroke-width="2"/>
<circle cx="92" cy="30" r="4" fill="#FBC02D"/>
''', cx="40%", cy="25%")

# 15. «Дружина», ТЦ «Звёздочка»: три жёлтые звёздочки-акробаты стоят пирамидкой на синем мате, верхняя машет рукой;
#    фон тёмно-синий ночной
def star(cx, cy, r, col="#FFD54F"):
    import math
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * .5
        pts.append(f"{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{col}" {s("stroke-width=\"2.8\"")}/>'


I["druzhina-pokryshkina"] = svg("#5C6BC0", "#1A237E", f'''
<rect x="10" y="104" width="108" height="14" rx="5" fill="#29B6F6" {s('stroke-width="2.6"')}/>
{star(44, 86, 20)}{star(84, 86, 20, "#FFCA28")}{star(64, 50, 20, "#FFE082")}
{eye(40, 87, .6)}{eye(48, 87, .6)}{eye(80, 87, .6)}{eye(88, 87, .6)}{eye(60, 51, .6)}{eye(68, 51, .6)}
<path d="M40 93 Q44 96 48 93 M80 93 Q84 96 88 93 M60 57 Q64 60 68 57" fill="none" {s('stroke-width="1.8"')}/>
<path d="M78 40 Q86 30 84 22" fill="none" {s('stroke-width="3"')}/>
<circle cx="84" cy="20" r="3" fill="#FFE082" {s('stroke-width="2"')}/>
<circle cx="20" cy="30" r="1.6" fill="#fff"/><circle cx="108" cy="40" r="1.6" fill="#fff"/><circle cx="30" cy="60" r="1.2" fill="#fff"/>
{sparkle(104, 18, 3)}
''', cx="50%", cy="20%")

# 16. «Твенти Ван», Судостроительная: бумажный кораблик с парусом из розовой гимнастической ленты плывёт по волнам, лента вьётся
#     спиралью; фон светло-аквамариновый
I["twentyone-gym-sudostroitelnaya"] = svg("#E0FFFA", "#58C9C0", f'''
<path d="M-4 96 Q14 88 30 96 Q48 104 64 96 Q80 88 96 96 Q114 104 132 96 V132 H-4Z" fill="#1E88E5" {s('stroke-width="2.6"')}/>
<path d="M24 82 H104 L92 100 H36 Z" fill="#FFFFFF" {s()}/>
<path d="M44 82 L64 64 L84 82" fill="#ECEFF1" {s('stroke-width="2.6"')}/>
{eye(54, 90, .7)}{eye(74, 90, .7)}
<path d="M60 95 Q64 98 68 95" fill="none" {s('stroke-width="2"')}/>
<path d="M64 64 V24" stroke="#8D6E63" stroke-width="3.4"/>
<circle cx="64" cy="22" r="3" fill="#FFC107" {s('stroke-width="1.8"')}/>
<path d="M64 26 Q96 22 92 38 Q86 52 70 44 Q60 38 72 32 Q86 28 100 40 Q112 52 104 66" fill="none" stroke="#FF4F9A" stroke-width="5" stroke-linecap="round"/>
<path d="M14 108 q8 -4 16 0 M92 112 q8 -4 16 0" fill="none" stroke="#BBDEFB" stroke-width="2.4"/>
''')

# 17. Клуб каратэ № 1, Ясеневая: белая каратэги-куртка с чёрным поясом и большой «1» на спине стоит в стойке, рядом лист ясеня;
#     фон тёплый оливковый
I["karate1-yasenevaya"] = svg("#F6F3D9", "#B5B85E", f'''
<path d="M-4 110 H132 V132 H-4Z" fill="#C8A26B" {s('stroke-width="2.6"')}/>
<path d="M36 34 Q64 26 92 34 L98 84 Q64 92 30 84 Z" fill="#FFFFFF" {s()}/>
<path d="M36 34 L14 62 L26 70 L40 52" fill="#FFFFFF" {s()}/>
<path d="M92 34 L114 62 L102 70 L88 52" fill="#FFFFFF" {s()}/>
<path d="M30 76 H98" stroke="#212121" stroke-width="7"/>
<path d="M58 78 L50 96 M70 78 L78 96" stroke="#212121" stroke-width="5" stroke-linecap="round"/>
<path d="M30 84 L36 108 H54 L60 88 M98 84 L92 108 H74 L68 88" fill="#FFFFFF" {s()}/>
<path d="M58 44 L66 38 V68" fill="none" stroke="#E53935" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
{eye(52, 56, .7)}{eye(80, 56, .7)}
<path d="M110 22 Q122 30 116 46 Q104 40 110 22Z" fill="#7CB342" {s('stroke-width="2.2"')}/>
<path d="M110 22 L116 46" stroke="#558B2F" stroke-width="1.6"/>
''', cx="40%", cy="25%")

# 18. Клуб каратэ № 1, Борисовские Пруды: деревянная дощечка с мордашкой раскалывается пополам от удара маленького кулачка в белом
#     рукаве, летят щепки-звёздочки; фон голубой прудовый
I["karate1-borisovskie-prudy"] = svg("#E1F3FF", "#5AA9E6", f'''
<path d="M30 48 L58 40 L62 70 L50 64 L36 76 Z" fill="#D7A86E" {s()}/>
<path d="M68 40 L98 48 L92 76 L78 64 L66 70 Z" fill="#D7A86E" {s()}/>
<path d="M36 56 L54 52 M74 52 L92 56" stroke="#A97C45" stroke-width="2"/>
{eye(44, 62, .7)}{eye(84, 62, .7)}
<path d="M40 70 Q44 66 48 70 M80 70 Q84 66 88 70" fill="none" {s('stroke-width="2"')}/>
<path d="M64 120 L64 92" stroke="{O}" stroke-width="22" stroke-linecap="round"/>
<path d="M64 120 L64 92" stroke="#FFFFFF" stroke-width="16" stroke-linecap="round"/>
<path d="M52 90 Q52 72 64 72 Q76 72 76 90 Z" fill="#FFCC9E" {s()}/>
<path d="M56 78 H72 M56 84 H72" stroke="{O}" stroke-width="1.8"/>
{sparkle(64, 30, 6, "#FFF59D")}{sparkle(22, 36, 4, "#FFF59D")}{sparkle(106, 34, 4, "#FFF59D")}
''', cx="50%", cy="30%")

# 19. Bekhoev Team, ТЦ «Браво»: зелёный крокодильчик в синем рашгарде держит в захвате плюшевую грушу на борцовском ковре;
#     фон оранжевый
I["bekhoev-team-borisovskie-prudy"] = svg("#FFE7C7", "#FF9838", f'''
<path d="M-4 106 H132 V132 H-4Z" fill="#E53935" {s('stroke-width="2.6"')}/>
<path d="M8 116 H120" stroke="#FFCDD2" stroke-width="2.4"/>
<rect x="70" y="50" width="34" height="56" rx="14" fill="#8D6E63" {s()}/>
<path d="M70 66 H104 M70 90 H104" stroke="#5D4037" stroke-width="3"/>
<path d="M22 104 Q20 70 44 64 Q62 62 66 84 L66 104 Z" fill="#1E5AC8" {s()}/>
<path d="M30 70 Q28 40 48 36 L80 40 Q86 44 80 50 L52 52 Q46 54 46 64" fill="#66BB6A" {s()}/>
<path d="M56 46 l4 4 l4 -4 l4 4 l4 -4" fill="none" stroke="#fff" stroke-width="2"/>
{eye(42, 40, .9)}
<circle cx="76" cy="42" r="1.6" fill="{O}"/>
<path d="M50 74 Q74 62 84 74" fill="none" {s('stroke-width="8"')}/>
<path d="M50 74 Q74 62 84 74" fill="none" stroke="#66BB6A" stroke-width="4.6"/>
<path d="M52 88 Q76 82 88 90" fill="none" {s('stroke-width="8"')}/>
<path d="M52 88 Q76 82 88 90" fill="none" stroke="#1E5AC8" stroke-width="4.6"/>
''', cx="35%", cy="25%")

# 20. Школа «Орион», Бабушкинская: созвездие Орион из семи звёзд, пояс Ориона — розовая гимнастическая лента, вьётся по ночному
#     фиолетовому небу
I["orion-gym-babushkina"] = svg("#7E57C2", "#2A1559", f'''
<path d="M40 26 L56 56 L86 30 M56 56 L50 62 M86 30 L78 64 M44 98 L52 68 M92 100 L76 70" fill="none" stroke="#B39DDB" stroke-width="1.8" stroke-dasharray="3 4"/>
<path d="M20 64 Q36 50 52 64 Q64 74 76 64 Q90 52 108 66 Q118 74 112 84" fill="none" stroke="#FF5CA8" stroke-width="7" stroke-linecap="round"/>
<path d="M20 64 Q36 50 52 64 Q64 74 76 64 Q90 52 108 66" fill="none" stroke="#FFC1DC" stroke-width="2" stroke-linecap="round"/>
{sparkle(40, 26, 7, "#FFF59D")}{sparkle(86, 30, 8, "#FFFFFF")}{sparkle(44, 100, 6, "#BBDEFB")}{sparkle(92, 100, 7, "#FFF59D")}
<circle cx="52" cy="64" r="7" fill="#FFF59D" {s('stroke-width="2.2"')}/><circle cx="64" cy="68" r="7" fill="#FFF59D" {s('stroke-width="2.2"')}/>
<circle cx="76" cy="64" r="7" fill="#FFF59D" {s('stroke-width="2.2"')}/>
{eye(61.5, 67, .45)}{eye(66.5, 67, .45)}
''', cx="50%", cy="40%")

# 21. Центр прогресса бокса: красный боксёрский шлем с мордашкой шагает вверх по трём столбикам растущего графика к
#     оранжевой звезде; фон лимонный
I["progress-boxing-rabfakovsky"] = svg("#FFFDE3", "#E8DD57", f'''
<rect x="10" y="92" width="26" height="30" fill="#90CAF9" {s()}/>
<rect x="40" y="78" width="26" height="44" fill="#64B5F6" {s()}/>
<rect x="70" y="60" width="26" height="62" fill="#42A5F5" {s()}/>
<rect x="100" y="40" width="26" height="82" fill="#1E88E5" {s()}/>
<path d="M50 70 Q46 30 76 26 Q104 30 100 70 Q96 82 75 82 Q54 82 50 70Z" fill="#E53935" {s()}/>
<path d="M58 50 Q75 42 92 50 L90 70 Q75 76 60 70Z" fill="#FFE0C2" {s('stroke-width="2.6"')}/>
<path d="M60 50 H90" stroke="#B71C1C" stroke-width="5"/>
{eye(68, 60, .7)}{eye(82, 60, .7)}
<path d="M70 67 Q75 70 80 67" fill="none" {s('stroke-width="2"')}/>
<path d="M75 82 V90" stroke="#B71C1C" stroke-width="5"/>
{sparkle(113, 22, 9, "#FF8F00")}
''')

# 22. MyGym, Таганка: маленькая выдра в оранжевой футболке делает кувырок вперёд по мягкой горке-мату; фон светло-коралловый
I["mygym-solzhenitsyna"] = svg("#FFE8E2", "#F59B85", f'''
<path d="M6 112 L44 76 H122 V112 Z" fill="#4DD0E1" {s()}/>
<path d="M44 76 L6 112 M60 76 V112 M84 76 V112" stroke="#00ACC1" stroke-width="2.4"/>
<circle cx="78" cy="52" r="22" fill="#8D6E63" {s()}/>
<path d="M62 62 Q78 80 96 62 Q90 72 78 72 Q66 72 62 62Z" fill="#FF8A1F" {s('stroke-width="2.4"')}/>
<path d="M58 40 Q50 26 64 24" fill="none" {s('stroke-width="5"')}/><path d="M58 40 Q50 26 64 24" fill="none" stroke="#8D6E63" stroke-width="2.6"/>
<ellipse cx="78" cy="44" rx="12" ry="9" fill="#D7B899" {s('stroke-width="2.2"')}/>
{eye(72, 42, .7)}{eye(84, 42, .7)}
<ellipse cx="78" cy="47" rx="2.6" ry="1.8" fill="{O}"/>
<path d="M96 46 Q112 40 112 26" fill="none" {s('stroke-width="6"')}/><path d="M96 46 Q112 40 112 26" fill="none" stroke="#8D6E63" stroke-width="3"/>
<path d="M34 46 Q44 30 60 30" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="4 5" stroke-linecap="round"/>
''', cx="30%", cy="25%")

# 23. MyGym, Коптево: коала-малыш в голубых шортиках висит на детских гимнастических кольцах и болтает лапками; фон светло-жёлтый
I["mygym-novopetrovskaya"] = svg("#FFFBE0", "#F7D774", f'''
<path d="M44 0 V30 M84 0 V30" stroke="#A1887F" stroke-width="3"/>
<circle cx="44" cy="38" r="9" fill="none" {s('stroke-width="6"')}/><circle cx="44" cy="38" r="9" fill="none" stroke="#FF7043" stroke-width="3"/>
<circle cx="84" cy="38" r="9" fill="none" {s('stroke-width="6"')}/><circle cx="84" cy="38" r="9" fill="none" stroke="#FF7043" stroke-width="3"/>
<path d="M48 44 L54 62 M80 44 L74 62" {s('stroke-width="9"')}/><path d="M48 44 L54 62 M80 44 L74 62" stroke="#B0BEC5" stroke-width="5.6" stroke-linecap="round"/>
<ellipse cx="64" cy="86" rx="16" ry="18" fill="#B0BEC5" {s()}/>
<path d="M48 90 Q64 98 80 90 L80 102 Q64 108 48 102Z" fill="#4FC3F7" {s('stroke-width="2.6"')}/>
<path d="M56 102 Q52 112 46 116 M72 102 Q78 112 84 114" {s('stroke-width="7"')}/>
<path d="M56 102 Q52 112 46 116 M72 102 Q78 112 84 114" stroke="#B0BEC5" stroke-width="4" stroke-linecap="round"/>
<circle cx="44" cy="62" r="10" fill="#CFD8DC" {s()}/><circle cx="84" cy="62" r="10" fill="#CFD8DC" {s()}/>
<circle cx="64" cy="64" r="17" fill="#B0BEC5" {s()}/>
{eye(57, 62, .8)}{eye(71, 62, .8)}
<ellipse cx="64" cy="70" rx="5" ry="4" fill="#455A64"/>
''', cx="50%", cy="30%")

# 24. MyGym, Шаболовка: жирафёнок в розовом купальнике идёт по низкому гимнастическому бревну, раскинув руки, позади сетчатый
#     силуэт Шуховской башни; фон мятный
I["mygym-shabolovka"] = svg("#E5FFF4", "#7FD8B4", f'''
<path d="M96 120 L104 40 L112 120 M98 100 H110 M100 80 H108 M101 60 H107 M96 120 L110 60 M112 120 L100 60" fill="none" stroke="#5BA88A" stroke-width="2"/>
<rect x="10" y="100" width="92" height="9" rx="4" fill="#C49A6C" {s('stroke-width="2.6"')}/>
<path d="M22 109 V122 M90 109 V122" {s('stroke-width="4"')}/>
<path d="M44 98 L42 80 M58 98 L60 80" {s('stroke-width="5"')}/><path d="M44 98 L42 80 M58 98 L60 80" stroke="#FFCC66" stroke-width="2.6"/>
<path d="M40 82 Q38 64 50 60 Q64 60 62 82 Z" fill="#FF6FA8" {s()}/>
<path d="M44 62 L18 54 M58 62 L84 54" {s('stroke-width="5"')}/><path d="M44 62 L18 54 M58 62 L84 54" stroke="#FFCC66" stroke-width="2.6"/>
<path d="M48 62 L46 34 M56 62 L56 34" {s('stroke-width="2.6"')}/>
<path d="M45 62 L44 34 H58 L58 62Z" fill="#FFCC66"/>
<ellipse cx="52" cy="28" rx="12" ry="10" fill="#FFCC66" {s()}/>
<path d="M46 18 V12 M58 18 V12" {s('stroke-width="2.6"')}/><circle cx="46" cy="11" r="2.4" fill="#8D6E63"/><circle cx="58" cy="11" r="2.4" fill="#8D6E63"/>
<circle cx="50" cy="44" r="2.6" fill="#C98A3A"/><circle cx="54" cy="52" r="2.2" fill="#C98A3A"/>
{eye(48, 27, .65)}{eye(57, 27, .65)}
<path d="M49 33 Q52 35 55 33" fill="none" {s('stroke-width="1.8"')}/>
''', cx="35%", cy="25%")

# 25. «Довмонт», Бибирево: маленький русский шлем-шишак с мордашкой в накладках для рукопашного боя стоит в стойке на татами;
#     фон тёмно-зелёный
I["dovmont-kostromskaya"] = svg("#B9E3B0", "#2F6B3A", f'''
<path d="M-4 106 H132 V132 H-4Z" fill="#1565C0" {s('stroke-width="2.6"')}/>
<path d="M64 10 L60 24 H68 Z" fill="#B0BEC5" {s('stroke-width="2.4"')}/>
<path d="M30 70 Q30 26 64 22 Q98 26 98 70 Z" fill="#CFD8DC" {s()}/>
<path d="M38 50 Q64 36 90 50" fill="none" stroke="#FFD54F" stroke-width="3"/>
<rect x="28" y="66" width="72" height="10" rx="4" fill="#FFC107" {s('stroke-width="2.6"')}/>
<path d="M60 76 V94 H68 V76" fill="#B0BEC5" {s('stroke-width="2.4"')}/>
<path d="M36 76 Q36 100 64 102 Q92 100 92 76 Z" fill="#FFE0C2" {s()}/>
{eye(52, 86, .8)}{eye(76, 86, .8)}
{blush(46, 94, .6)}{blush(82, 94, .6)}
{glove(20, 84, .7, "#E53935", flip=True)}{glove(108, 84, .7, "#E53935")}
''', cx="40%", cy="25%")

SUBJ = {
 "reutov-sportschool-oktyabrya": "красная угловая стойка боксёрского ринга с мордашкой и золотой медалькой | держит три натянутых каната ринга — красный, белый и синий — над синим ковром, фон лаймовый",
 "husky-basket-saltykovskaya": "оранжевый баскетбольный мяч с мордашкой в синей повязке на лбу | висит, ухватившись ручками за кольцо после броска, под щитом, фон вечерний сиреневый",
 "legion-kudo-sokol": "белый шлем кудо с прозрачным забралом, за которым видны глазки | сидит на соломенном татами рядом с веточкой цветущей сакуры, фон тёмно-бирюзовый",
 "shershen-nezhinskaya": "полосатый шершень в красных боксёрских перчатках | порхает и бьёт джеб по маленькой подвесной груше, фон медово-жёлтый",
 "kensei-angelov": "журавлик-оригами в синем дзюдоги с чёрным поясом | бросает через бедро розовую подушку на жёлтом татами, фон светло-голубой",
 "top-fight-pyatnitskoe": "чёрно-золотая боксёрская груша в красной тайской повязке монгкон | раскачивается на цепи, вокруг вспыхивают жёлтые звёздочки от ударов, фон тёмно-красный",
 "otkrytie-gym-kashirskoe": "золотой ключик с мордашкой и розовым бантиком | отпирает жёлтый замочек, из скважины вылетает розовая спираль гимнастической ленты, фон бирюзовый",
 "otkrytie-gym-dzhankoyskaya": "голубая гимнастическая булава с мордашкой в короне из страз | стоит на одной ручке на фиолетовом ковре, рядом лежит вторая булава, фон персиковый",
 "otkrytie-gym-sevanskaya": "фиолетовый гимнастический мяч с блёстками и мордашкой | катится по дорожке из звёздочек под красной стрельчатой аркой Царицына, фон розово-лиловый",
 "otkrytie-gym-erevanskaya": "жёлтая гимнастическая скакалка с двумя мордашками на красных ручках | сама закручивается восьмёркой над синим ковром, фон мятный",
 "polet-sambo-sudostroitelnaya": "красная куртка-самбовка с мордашкой в лётных очках-авиаторах | летит над облаками, раскинув рукава как крылья самолёта, фон небесный",
 "polet-sambo-kashirskoe-55": "бумажный самолётик, подпоясанный красным поясом самбо | заходит на посадку на зелёный ковёр и оставляет пунктирный след, фон светло-жёлтый",
 "polet-sambo-medynskaya": "круглый синий ковёр самбо с красным кругом и мордашкой | смотрит вверх на пролетающий жёлтый воздушный шар в красную полоску, фон закатный оранжевый",
 "otvaga-zelenaya-zona": "смелый зелёный кузнечик в красной самбовке | бросает через плечо большой одуванчик на траве, фон ярко-зелёный",
 "druzhina-pokryshkina": "три жёлтые звёздочки-акробаты с мордашками | стоят пирамидкой на голубом мате, верхняя машет рукой, фон тёмно-синий ночной",
 "twentyone-gym-sudostroitelnaya": "бумажный кораблик с мордашкой и парусом из розовой гимнастической ленты | плывёт по синим волнам, лента-парус вьётся спиралью, фон светло-аквамариновый",
 "karate1-yasenevaya": "белая каратэги-куртка с чёрным поясом и красной цифрой «1» | стоит в широкой стойке на деревянном полу додзё, рядом зелёный лист ясеня, фон тёплый оливковый",
 "karate1-borisovskie-prudy": "деревянная дощечка для разбивания с мордашками на обеих половинках | раскалывается от удара маленького кулачка в белом рукаве, вокруг жёлтые искры, фон голубой прудовый",
 "bekhoev-team-borisovskie-prudy": "зелёный крокодильчик в синем рашгарде | держит в захвате коричневую грушу на красном борцовском ковре, фон оранжевый",
 "orion-gym-babushkina": "созвездие Орион, пояс которого — розовая гимнастическая лента | лента вьётся между тремя звёздами пояса с мордашкой по ночному фиолетовому небу",
 "progress-boxing-rabfakovsky": "красный боксёрский шлем с мордашкой | стоит на столбиках растущего голубого графика, над верхним — оранжевая звезда, фон лимонный",
 "mygym-solzhenitsyna": "маленькая выдра в оранжевой футболке | делает кувырок вперёд с мягкой бирюзовой горки-мата, фон светло-коралловый",
 "mygym-novopetrovskaya": "коала-малыш в голубых шортиках | висит на детских гимнастических кольцах с оранжевой обмоткой и болтает лапками, фон светло-жёлтый",
 "mygym-shabolovka": "жирафёнок в розовом купальнике | идёт по низкому гимнастическому бревну, раскинув руки, позади сетчатый силуэт Шуховской башни, фон мятный",
 "dovmont-kostromskaya": "маленький серебряный шлем-шишак с мордашкой и красными накладками для рукопашного боя | стоит в боевой стойке на синем татами, фон тёмно-зелёный",
}

if __name__ == "__main__":
    import sys
    for pid, body in I.items():
        if len(sys.argv) > 1 and pid not in sys.argv[1:]:
            continue
        open(os.path.join(ROOT, "icons-src", pid + ".svg"), "w").write(body)
    print(len(I))
