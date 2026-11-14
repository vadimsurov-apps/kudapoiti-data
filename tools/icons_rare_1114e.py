"""Иконки робота rare 14.11 (1114e). Каждая придумана и нарисована отдельно (правило абсолютной уникальности):
свой герой, своя сцена, своя компоновка и палитра.  python3 tools/icons_rare_1114e.py [id ...]"""
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


def blade(x1, x2, y, w="3"):
    """коньковое лезвие с загнутым носком"""
    return (f'<path d="M{x1} {y} H{x2} Q{x2+6} {y} {x2+5} {y-5}" fill="none" stroke="#C9D3E0" stroke-width="{w}" '
            f'stroke-linecap="round"/><path d="M{x1} {y} H{x2} Q{x2+6} {y} {x2+5} {y-5}" fill="none" {s("stroke-width=\"1.2\"")}/>')


I = {}

# 1. Ляпкин, Томилино (хоккей с 3 лет — малыши учатся не спеша): улитка, у которой раковина — красный хоккейный шлем
#    с решёткой-визором; маленькой клюшкой медленно ведёт шайбу по льду, за ней блестящий след; фон мятный
I["lyapkin-hockey-tomilino"] = svg("#E6FFF4", "#69CFA6", f'''
<path d="M-4 98 Q64 90 132 98 V132 H-4Z" fill="#F2FBFF" {s('stroke-width="2.4"')}/>
<path d="M8 104 Q30 100 46 104" stroke="#BDE8FF" stroke-width="5" stroke-linecap="round" opacity=".9"/>
{sparkle(16, 100, 3)}{sparkle(34, 98, 2.5)}
<path d="M34 96 Q36 80 52 80 H82 Q92 80 94 70 L98 52 Q100 46 106 48 Q112 50 110 58 L104 84 Q100 98 84 98 H40 Q34 98 34 96Z" fill="#F7C9A0" {s()}/>
<path d="M100 50 L98 36 M106 51 L110 38" {s('stroke-width="2.4"')}/>
<circle cx="98" cy="35" r="3" fill="{O}"/><circle cx="110" cy="37" r="3" fill="{O}"/>
{eye(100, 60, .8)}{eye(108, 61, .8)}
<path d="M99 69 Q104 73 109 69" fill="none" {s('stroke-width="2.2"')}/>
<path d="M36 82 Q34 46 62 42 Q88 42 88 70 Q88 82 80 84 H40 Q36 84 36 82Z" fill="#E53935" {s()}/>
<path d="M44 60 Q60 50 80 58" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
<path d="M62 44 V82" stroke="#B71C1C" stroke-width="2.4"/>
<path d="M40 72 H70 M40 78 H70 M48 68 V84 M56 68 V84 M64 68 V84" stroke="#ECEFF1" stroke-width="2"/>
<rect x="38" y="66" width="34" height="18" rx="5" fill="none" {s('stroke-width="2.4"')}/>
<path d="M104 80 L92 104 H72" fill="none" stroke="{O}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M104 80 L92 104 H72" fill="none" stroke="#F4B860" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
<ellipse cx="62" cy="106" rx="9" ry="3.5" fill="#26232F"/>
<rect x="53" y="102" width="18" height="4" fill="#26232F"/>
<ellipse cx="62" cy="102" rx="9" ry="3.5" fill="#3C3848"/>
''')

# 2. Ляпкин, Некрасовка (тренировки на льду с 8 утра): рыжий петух в синем хоккейном шлеме и с клюшкой под крылом
#    стоит на льду и кукарекает, за бортом встаёт большое солнце; фон рассветный персиково-розовый
I["lyapkin-hockey-nekrasovka"] = svg("#FFE9C9", "#FF9A8B", f'''
<circle cx="96" cy="78" r="26" fill="#FFD54F" opacity=".95"/>
<rect x="-4" y="84" width="136" height="10" fill="#FFFFFF" {s('stroke-width="2.4"')}/>
<path d="M-4 94 H132 V132 H-4Z" fill="#EAF6FF" {s('stroke-width="2.4"')}/>
<path d="M30 70 Q14 60 18 40 Q26 54 34 56 Q26 42 32 30 Q38 48 44 54Z" fill="#2E7D32" {s('stroke-width="2.4"')}/>
<ellipse cx="54" cy="74" rx="24" ry="18" fill="#F57C00" {s()}/>
<path d="M44 70 Q54 82 66 72" fill="none" stroke="#FFB74D" stroke-width="3" stroke-linecap="round"/>
<path d="M60 60 Q60 40 70 34 Q82 30 84 44 Q86 56 74 62Z" fill="#F57C00" {s()}/>
<path d="M66 36 Q66 18 78 18 Q90 18 90 34 Q82 28 78 30 Q72 30 66 36Z" fill="#1E5AC8" {s('stroke-width="2.6"')}/>
<path d="M70 22 Q72 14 76 20 Q78 12 82 20" fill="#E53935" {s('stroke-width="2"')}/>
<path d="M84 40 L98 36 L86 46Z" fill="#FFC107" {s('stroke-width="2.4"')}/>
<path d="M98 30 q6 -2 8 -6 M100 38 q7 0 10 -3 M98 44 q6 2 9 6" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M82 48 Q86 54 82 58 Q78 54 82 48Z" fill="#E53935" {s('stroke-width="2"')}/>
{eye(76, 38, .8)}
<path d="M48 90 V98 M60 90 V98" {s('stroke-width="3"')}/>
<path d="M42 99 H54 M54 99 H66" stroke="#C9D3E0" stroke-width="3" stroke-linecap="round"/>
<path d="M30 64 L20 104 H6" fill="none" stroke="{O}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M30 64 L20 104 H6" fill="none" stroke="#8D6E63" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
<ellipse cx="38" cy="108" rx="7" ry="2.8" fill="#26232F"/>
''', cx="75%", cy="55%")

# 3. Ледовая арена ПСБ «Патриот» (Кубинка, рядом с военным парком): маленький зелёный танк с мордашкой на башне стоит
#    на двух коньковых лезвиях вместо гусениц и скользит по льду; из пушки торчит вязаный помпон; фон морозный серо-голубой
I["rink-psb-patriot-kubinka"] = svg("#EEF4FA", "#8FA9C4", f'''
<path d="M-4 100 Q64 94 132 100 V132 H-4Z" fill="#FFFFFF" {s('stroke-width="2.4"')}/>
<path d="M14 108 H40 M90 112 H116" stroke="#B9C9DA" stroke-width="2.4" stroke-linecap="round"/>
<path d="M22 70 H106 Q112 70 110 78 L104 90 H24 L18 78 Q16 70 22 70Z" fill="#6B8E3A" {s()}/>
<path d="M28 80 H100" stroke="#55732A" stroke-width="3"/>
<circle cx="34" cy="80" r="3" fill="#55732A"/><circle cx="50" cy="80" r="3" fill="#55732A"/><circle cx="78" cy="80" r="3" fill="#55732A"/><circle cx="94" cy="80" r="3" fill="#55732A"/>
<path d="M38 70 Q38 46 62 46 Q84 46 84 70Z" fill="#7FA346" {s()}/>
<path d="M82 56 H112" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M82 56 H112" stroke="#7FA346" stroke-width="5" stroke-linecap="round"/>
<circle cx="117" cy="56" r="6" fill="#E53935" {s('stroke-width="2.2"')}/>
<path d="M113 52 l8 8 M121 52 l-8 8 M117 50 v12" stroke="#FFCDD2" stroke-width="1.4"/>
<path d="M52 47 Q54 40 62 40 Q70 40 72 47" fill="#55732A" {s('stroke-width="2.4"')}/>
{face(60, 58, 7, .85)}
<path d="M30 92 V98 M98 92 V98" {s('stroke-width="3"')}/>
{blade(22, 50, 99)}{blade(78, 104, 99)}
{sparkle(24, 30, 5)}{sparkle(100, 24, 4)}{sparkle(14, 56, 3)}
''')

# 4. «Орион-Технопул» (Железнодорожный): три звёздочки пояса Ориона в белых коньках держатся за руки и катятся
#    цепочкой по ночному льду, над ними пунктиром — остальной контур созвездия; фон тёмно-синий
def star5(cx, cy, r, c):
    import math
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * .5
        pts.append(f"{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{c}" {s("stroke-width=\"2.4\"")}/>'


I["rink-orion-technopool-zheldor"] = svg("#3A4FA8", "#121A45", f'''
<path d="M-4 96 Q64 88 132 96 V132 H-4Z" fill="#CFE6FF" {s('stroke-width="2.4"')}/>
<path d="M24 22 L40 34 M96 20 L84 34 M30 112 L40 96 M100 114 L88 96" stroke="#9FB4FF" stroke-width="1.6" stroke-dasharray="3 4"/>
<circle cx="24" cy="22" r="3" fill="#FFB199"/><circle cx="96" cy="20" r="3.4" fill="#A9D4FF"/>
<path d="M44 64 L56 60 M72 60 L84 64" {s('stroke-width="3"')}/>
{star5(34, 66, 17, "#FFE066")}{star5(64, 58, 19, "#FFD23F")}{star5(94, 66, 17, "#FFE066")}
{face(34, 66, 4.5, .6, blush=False)}{face(64, 58, 5, .65)}{face(94, 66, 4.5, .6, blush=False)}
<path d="M30 80 v8 M38 80 v8 M60 74 v10 M68 74 v10 M90 80 v8 M98 80 v8" {s('stroke-width="2.6"')}/>
<path d="M27 88 h8 l1 3 h-9z M35 88 h8 l1 3 h-9z M57 84 h8 l1 3 h-9z M65 84 h8 l1 3 h-9z M87 88 h8 l1 3 h-9z M95 88 h8 l1 3 h-9z" fill="#fff" {s('stroke-width="1.6"')}/>
<path d="M26 93 h20 M56 89 h20 M86 93 h20" stroke="#C9D3E0" stroke-width="2.2" stroke-linecap="round"/>
{sparkle(112, 40, 3)}{sparkle(14, 44, 2.5)}{sparkle(60, 22, 3, "#FFF3B0")}
''', cx="50%", cy="20%")

# 5. Каток ФОК «Салют» (Долгопрудный): белый фигурный конёк с мордашкой подпрыгнул над льдом, а над ним в ночном небе
#    распускаются три разноцветных салюта; фон глубокий фиолетовый
def burst(cx, cy, r, c):
    out = ""
    for a in range(0, 360, 30):
        out += f'<path d="M{cx} {cy - r * .35} V{cy - r}" stroke="{c}" stroke-width="2.6" stroke-linecap="round" transform="rotate({a} {cx} {cy})"/>'
    return out + f'<circle cx="{cx}" cy="{cy}" r="2.5" fill="{c}"/>'


I["rink-salyut-dolgoprudny"] = svg("#6A3FB5", "#22104A", f'''
{burst(30, 30, 16, "#FF6FA8")}{burst(98, 26, 14, "#6FE3FF")}{burst(66, 16, 10, "#FFE066")}
<path d="M-4 104 Q64 98 132 104 V132 H-4Z" fill="#D9ECFF" {s('stroke-width="2.4"')}/>
<ellipse cx="62" cy="108" rx="24" ry="3" fill="#9CB6D6" opacity=".7"/>
<path d="M46 46 Q46 38 54 38 H70 Q76 38 76 46 V70 Q76 78 86 80 Q96 82 96 88 V92 H46Z" fill="#FFFFFF" {s()}/>
<path d="M54 46 L70 52 M54 54 L70 60 M54 62 L70 68" stroke="#E53980" stroke-width="2.4" stroke-linecap="round"/>
<path d="M46 92 H96" {s('stroke-width="2.4"')}/>
<path d="M54 92 V98 M88 92 V98" {s('stroke-width="2.6"')}/>
<path d="M42 99 H96 Q104 99 102 92" fill="none" stroke="#C9D3E0" stroke-width="3.4" stroke-linecap="round"/>
<path d="M42 99 h4 l-2 4z" fill="#C9D3E0"/>
{face(64, 78, 6, .7)}
<path d="M30 112 q6 -4 12 0 M84 114 q6 -4 12 0" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
''', cx="50%", cy="30%")

# 6. Школа Алексея Моторина (Долгопрудный): розовый фигурный конёк с маленьким пропеллером-моторчиком на пятке мчится
#    по льду, за моторчиком вылетают белые облачка; фон лимонно-жёлтый
I["fk-motorin-dolgoprudny"] = svg("#FFFBD6", "#FFD34D", f'''
<path d="M-4 98 Q64 104 132 96 V132 H-4Z" fill="#F4FAFF" {s('stroke-width="2.4"')}/>
<path d="M16 108 H50 M64 114 H96" stroke="#BCD4EA" stroke-width="2.4" stroke-linecap="round"/>
<circle cx="18" cy="62" r="7" fill="#fff" opacity=".9"/><circle cx="10" cy="54" r="5" fill="#fff" opacity=".8"/><circle cx="6" cy="68" r="4" fill="#fff" opacity=".7"/>
<path d="M44 36 Q44 28 52 28 H68 Q74 28 74 36 V60 Q74 68 86 70 Q100 72 100 80 V86 H44Z" fill="#FF8DB8" {s()}/>
<path d="M52 36 L68 42 M52 44 L68 50 M52 52 L68 58" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M44 86 H100" {s('stroke-width="2.4"')}/>
<rect x="30" y="62" width="14" height="14" rx="3" fill="#90A4AE" {s('stroke-width="2.4"')}/>
<path d="M30 69 H24" {s('stroke-width="2.6"')}/>
<ellipse cx="22" cy="60" rx="3" ry="10" fill="#455A64" {s('stroke-width="1.8"')}/>
<ellipse cx="22" cy="78" rx="3" ry="10" fill="#455A64" {s('stroke-width="1.8"')}/>
<circle cx="22" cy="69" r="2.6" fill="#E53935"/>
<path d="M52 86 V92 M92 86 V92" {s('stroke-width="2.6"')}/>
<path d="M42 93 H96 Q104 93 102 86" fill="none" stroke="#C9D3E0" stroke-width="3.4" stroke-linecap="round"/>
{face(84, 74, 5.5, .7)}
<path d="M106 54 h12 M104 62 h16 M108 70 h10" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
''', cx="60%", cy="30%")

# 7. «Лига фигурного катания» (Зеленоград, синхронное катание): три девочки-фигуристки в одинаковых сиреневых платьях
#    едут по льду ровной линией, положив руки друг другу на плечи; фон светло-бирюзовый
def girl(x, y, hair):
    return f'''
<path d="M{x-6} {y+13} H{x+6} L{x+5} {y+22} L{x+13} {y+34} H{x-13} L{x-5} {y+22}Z" fill="#B784E8" {s('stroke-width="2.4"')}/>
<path d="M{x-5} {y+22} H{x+5}" stroke="#fff" stroke-width="1.6"/>
<path d="M{x-4} {y+34} V{y+48} M{x+4} {y+34} V{y+46}" {s('stroke-width="2.6"')}/>
<path d="M{x-8} {y+48} h7 l1 3 h-8z M{x+1} {y+46} h7 l1 3 h-8z" fill="#fff" {s('stroke-width="1.4"')}/>
<circle cx="{x}" cy="{y+4}" r="9" fill="#FFDCC2" {s('stroke-width="2.4"')}/>
<path d="M{x-9} {y+3} Q{x-8} {y-8} {x} {y-7} Q{x+9} {y-8} {x+9} {y+3} Q{x+3} {y-2} {x-9} {y+3}Z" fill="{hair}" {s('stroke-width="2"')}/>
<circle cx="{x}" cy="{y-9}" r="3.4" fill="{hair}" {s('stroke-width="1.8"')}/>
{eye(x-3, y+5, .5)}{eye(x+3, y+5, .5)}
<path d="M{x-2} {y+9} Q{x} {y+11} {x+2} {y+9}" fill="none" {s('stroke-width="1.6"')}/>'''


I["liga-fskate-zelenograd"] = svg("#E3FFFB", "#58C9C0", f'''
<path d="M-4 92 Q64 86 132 92 V132 H-4Z" fill="#FFFFFF" {s('stroke-width="2.4"')}/>
<path d="M14 104 H114" stroke="#B2E4F2" stroke-width="3" stroke-linecap="round" stroke-dasharray="10 6"/>
{girl(34, 44, "#6D4C41")}{girl(64, 40, "#F2C94C")}{girl(94, 44, "#2E2A38")}
<path d="M43 56 Q50 50 56 54 M73 54 Q80 50 86 56" fill="none" stroke="#B784E8" stroke-width="5" stroke-linecap="round"/>
<path d="M43 56 Q50 50 56 54 M73 54 Q80 50 86 56" fill="none" {s('stroke-width="1.4"')}/>
<path d="M24 96 h20 M54 92 h20 M84 96 h20" stroke="#C9D3E0" stroke-width="2.2" stroke-linecap="round"/>
{sparkle(18, 26, 4)}{sparkle(112, 30, 3.5)}
''', cx="45%", cy="25%")

# 8. Golden Star, Железнодорожный: девочка-фигуристка в форменной фуражке машиниста делает «ласточку» на льду,
#    вытянув руку как семафор; фон небесно-голубой с жёлтыми бликами
I["golden-star-zheleznodorozhny"] = svg("#EAF7FF", "#6FB6F0", f'''
<path d="M-4 100 Q64 94 132 100 V132 H-4Z" fill="#FFFFFF" {s('stroke-width="2.4"')}/>
<path d="M18 110 H60" stroke="#BCD4EA" stroke-width="2.4" stroke-linecap="round"/>
<path d="M58 60 Q74 52 92 62 Q80 72 64 72Z" fill="#E53935" {s()}/>
<path d="M60 66 Q50 82 54 94" fill="none" {s('stroke-width="3"')}/>
<path d="M48 94 h10 l1 4 h-11z" fill="#fff" {s('stroke-width="1.6"')}/>
<path d="M44 100 H62 Q66 100 65 96" fill="none" stroke="#C9D3E0" stroke-width="3" stroke-linecap="round"/>
<path d="M88 62 Q102 54 116 50" fill="none" {s('stroke-width="3"')}/>
<path d="M114 46 h8 l1 4 h-9z" fill="#fff" {s('stroke-width="1.6"')} transform="rotate(-20 118 48)"/>
<path d="M62 62 Q48 50 34 38" fill="none" {s('stroke-width="3"')}/>
<circle cx="32" cy="36" r="4" fill="#FFDCC2" {s('stroke-width="2"')}/>
<circle cx="56" cy="50" r="10" fill="#FFDCC2" {s('stroke-width="2.4"')}/>
<path d="M46 46 Q46 36 56 36 Q66 36 66 46Z" fill="#1F3A6E" {s('stroke-width="2.2"')}/>
<path d="M44 46 H70" {s('stroke-width="3"')}/>
<circle cx="56" cy="40" r="2.4" fill="#FFD23F"/>
<path d="M64 52 Q72 54 72 60" fill="none" stroke="#8D5A3A" stroke-width="4" stroke-linecap="round"/>
{eye(53, 52, .55)}{eye(59, 52, .55)}
<path d="M54 57 Q56 59 58 57" fill="none" {s('stroke-width="1.6"')}/>
{sparkle(22, 72, 4, "#FFE066")}{sparkle(108, 82, 3)}
''')

# 9. Golden Star, Молоково: пакет молока с мордашкой и синей коровьей пятнистой полосой стоит на белых фигурных коньках
#    и кружится во вращении, вокруг разлетаются капельки молока; фон нежно-розовый
I["golden-star-molokovo"] = svg("#FFF0F5", "#F7A8C4", f'''
<path d="M-4 102 Q64 96 132 102 V132 H-4Z" fill="#FFFFFF" {s('stroke-width="2.4"')}/>
<ellipse cx="64" cy="106" rx="22" ry="5" fill="none" stroke="#C7D7EA" stroke-width="2.4"/>
<path d="M42 44 L64 30 L86 44 V88 H42Z" fill="#FFFFFF" {s()}/>
<path d="M42 44 H86 L64 30Z" fill="#E3EEF9" {s('stroke-width="2.6"')}/>
<path d="M56 34 L64 22 L72 34" fill="#FFFFFF" {s('stroke-width="2.4"')}/>
<path d="M42 72 H86 V88 H42Z" fill="#4A90E2" {s('stroke-width="2.6"')}/>
<path d="M48 76 q5 -3 8 2 q-2 5 -8 2z M70 80 q6 -4 10 1 q-3 5 -10 1z" fill="#fff"/>
{face(64, 56, 7, .85)}
<path d="M54 88 V96 M74 88 V96" {s('stroke-width="2.8"')}/>
<path d="M48 96 h10 l1 4 h-11z M68 96 h10 l1 4 h-11z" fill="#fff" {s('stroke-width="1.6"')}/>
<path d="M46 101 H62 M66 101 H82" stroke="#C9D3E0" stroke-width="2.6" stroke-linecap="round"/>
<path d="M24 40 q3 -6 6 0 q0 5 -3 5 q-3 0 -3 -5z M100 50 q3 -6 6 0 q0 5 -3 5 q-3 0 -3 -5z M30 74 q2.5 -5 5 0 q0 4 -2.5 4 q-2.5 0 -2.5 -4z M96 80 q2.5 -5 5 0 q0 4 -2.5 4 q-2.5 0 -2.5 -4z" fill="#FFFFFF" {s('stroke-width="1.6"')}/>
<path d="M22 58 q-6 -10 2 -16 M106 66 q6 -10 -2 -16" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
''')

# 10. Golden Star в «Айсберге» (Химки): белая полярная совушка с жёлтыми глазами в фиолетовой юбочке катится «пистолетиком»
#     на одном коньке, вытянув крыло вперёд; фон ледяной лавандовый
I["golden-star-khimki-aysberg"] = svg("#F1ECFF", "#A99BE6", f'''
<path d="M-4 102 Q64 96 132 102 V132 H-4Z" fill="#FFFFFF" {s('stroke-width="2.4"')}/>
<path d="M30 112 H70" stroke="#C8C0EE" stroke-width="2.4" stroke-linecap="round"/>
<ellipse cx="60" cy="62" rx="22" ry="26" fill="#FAFAFA" {s()}/>
<path d="M44 46 L40 34 L52 42 M76 46 L80 34 L68 42" fill="#FAFAFA" {s('stroke-width="2.4"')}/>
<circle cx="52" cy="54" r="8" fill="#FFE066" {s('stroke-width="2.2"')}/><circle cx="68" cy="54" r="8" fill="#FFE066" {s('stroke-width="2.2"')}/>
<circle cx="52" cy="55" r="4" fill="{O}"/><circle cx="68" cy="55" r="4" fill="{O}"/>
<circle cx="50.6" cy="53.4" r="1.4" fill="#fff"/><circle cx="66.6" cy="53.4" r="1.4" fill="#fff"/>
<path d="M58 62 L60 67 L62 62Z" fill="#F2A33A" {s('stroke-width="1.6"')}/>
<path d="M50 70 q2 2 4 0 M58 74 q2 2 4 0 M66 70 q2 2 4 0" fill="none" stroke="#B0B7C3" stroke-width="1.6"/>
<path d="M80 60 Q100 56 114 62 Q100 68 82 70Z" fill="#F0F0F0" {s('stroke-width="2.4"')}/>
<path d="M40 64 Q30 72 32 82" fill="none" {s('stroke-width="2.4"')}/>
<path d="M40 80 Q60 76 80 80 L84 90 Q60 96 36 90Z" fill="#8E5BD8" {s('stroke-width="2.4"')}/>
<path d="M56 92 V100" {s('stroke-width="3"')}/>
<path d="M50 100 h10 l1 4 h-11z" fill="#fff" {s('stroke-width="1.6"')}/>
<path d="M46 106 H64 Q68 106 67 101" fill="none" stroke="#C9D3E0" stroke-width="3" stroke-linecap="round"/>
<path d="M66 92 Q80 94 92 92" fill="none" {s('stroke-width="3"')}/>
<path d="M92 88 h9 l1 4 h-10z" fill="#fff" {s('stroke-width="1.6"')}/>
{sparkle(104, 30, 5)}{sparkle(22, 30, 3.5)}
''', cx="45%", cy="30%")

# 11. «Арена Легенд» (Озёры): серебристо-голубая рыбка подо льдом смотрит снизу вверх сквозь прозрачный лёд,
#     как над ней проезжает пара красных коньков; сверху светлый лёд, снизу тёмная вода; фон — сама вода
I["rink-arena-legend-ozery"] = svg("#4FB3C9", "#0E4A63", f'''
<path d="M-4 18 H132 V52 H-4Z" fill="#E8F7FF" opacity=".92"/>
<path d="M-4 52 H132" {s('stroke-width="2.6"')}/>
<path d="M10 40 L22 28 M90 44 L104 30 M50 46 L58 38" stroke="#BCE3F5" stroke-width="2" stroke-linecap="round"/>
<path d="M44 20 Q44 14 50 14 H58 Q62 14 62 20 V30 Q62 34 68 35 Q74 36 74 40 V42 H44Z" fill="#E53935" {s('stroke-width="2.4"')}/>
<path d="M44 42 H74" {s('stroke-width="2"')}/>
<path d="M40 48 H74 Q80 48 78 43" fill="none" stroke="#C9D3E0" stroke-width="3" stroke-linecap="round"/>
<path d="M50 42 V48 M70 42 V48" {s('stroke-width="2"')}/>
<path d="M30 92 Q46 66 76 74 Q96 80 98 94 Q86 108 62 108 Q40 106 30 92Z" fill="#B7D8EA" {s()}/>
<path d="M98 94 L116 80 L114 106Z" fill="#7FB2D0" {s('stroke-width="2.6"')}/>
<path d="M56 74 Q62 64 72 72" fill="#7FB2D0" {s('stroke-width="2.4"')}/>
<path d="M60 92 Q64 98 60 104 M68 90 Q72 96 68 102" fill="none" stroke="#7FB2D0" stroke-width="2"/>
{eye(44, 84, .9)}
<path d="M36 94 Q40 98 44 96" fill="none" {s('stroke-width="2.2"')}/>
<ellipse cx="48" cy="92" rx="3.4" ry="2" fill="#FF7FA8" opacity=".6"/>
<circle cx="40" cy="70" r="3" fill="none" stroke="#DDF3FF" stroke-width="1.8"/><circle cx="36" cy="60" r="2" fill="none" stroke="#DDF3FF" stroke-width="1.6"/>
''', cx="50%", cy="20%")

if __name__ == "__main__":
    import sys
    for pid, body in I.items():
        if len(sys.argv) > 1 and pid not in sys.argv[1:]:
            continue
        open(os.path.join(ROOT, "icons-src", pid + ".svg"), "w").write(body)
    print(len(I))
