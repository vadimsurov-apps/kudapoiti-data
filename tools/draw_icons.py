"""Детские иконки мест, версия 2: дружелюбные персонажи с мордочками,
мягкий контур, всё целиком внутри круга с отступом. 128×128."""
import os, math

O = "#3B3355"     # мягкий тёмно-сливовый контур
SW = 3.2
OUT = os.path.dirname(os.path.abspath(__file__))

BG = {
    "blue":   ("#C9EEFF", "#6CC0F2"),
    "green":  ("#D9F7C2", "#7CD26E"),
    "orange": ("#FFE2B8", "#FFAE6B"),
    "pink":   ("#FFDCEB", "#F58CB8"),
    "purple": ("#E6DAFF", "#A98BF0"),
    "yellow": ("#FFF6C4", "#FFD45E"),
    "teal":   ("#CFF7EF", "#5CCDBA"),
    "night":  ("#8A97E0", "#3E4AA0"),
    "sky":    ("#E4F6FF", "#9DD6F5"),
}


def s(extra=""):
    width = "" if "stroke-width" in extra else f'stroke-width="{SW}" '
    return f'stroke="{O}" {width}stroke-linejoin="round" stroke-linecap="round" {extra}'


def eye(x, y, k=1.0):
    return (f'<ellipse cx="{x}" cy="{y}" rx="{4*k:.1f}" ry="{4.8*k:.1f}" fill="{O}"/>'
            f'<circle cx="{x-1.3*k:.1f}" cy="{y-1.8*k:.1f}" r="{1.7*k:.1f}" fill="#fff"/>'
            f'<circle cx="{x+1.3*k:.1f}" cy="{y+1.6*k:.1f}" r="{0.8*k:.1f}" fill="#fff"/>')


def face(cx, cy, d=9, k=1.0, mouth=True, blush=True):
    out = eye(cx - d, cy, k) + eye(cx + d, cy, k)
    if blush:
        out += (f'<ellipse cx="{cx-d-5*k:.1f}" cy="{cy+7*k:.1f}" rx="{4.5*k:.1f}" ry="{2.6*k:.1f}" fill="#FF7FA8" opacity=".6"/>'
                f'<ellipse cx="{cx+d+5*k:.1f}" cy="{cy+7*k:.1f}" rx="{4.5*k:.1f}" ry="{2.6*k:.1f}" fill="#FF7FA8" opacity=".6"/>')
    if mouth:
        out += f'<path d="M{cx-4*k:.1f} {cy+6*k:.1f} Q{cx} {cy+10.5*k:.1f} {cx+4*k:.1f} {cy+6*k:.1f}" fill="none" {s(f"stroke-width=\"{2.6*k:.1f}\"")}/>'
    return out


def sparkle(x, y, r, color="#fff"):
    return (f'<path d="M{x} {y-r} Q{x+r*.2} {y-r*.2} {x+r} {y} Q{x+r*.2} {y+r*.2} {x} {y+r} '
            f'Q{x-r*.2} {y+r*.2} {x-r} {y} Q{x-r*.2} {y-r*.2} {x} {y-r}Z" fill="{color}"/>')


def svg(bg, body):
    a, b = BG[bg]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
<defs>
 <radialGradient id="g" cx="38%" cy="28%" r="85%"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></radialGradient>
 <clipPath id="c"><circle cx="64" cy="64" r="61"/></clipPath>
</defs>
<circle cx="64" cy="64" r="61" fill="url(#g)"/>
<g clip-path="url(#c)">{body}</g>
<ellipse cx="44" cy="22" rx="20" ry="7" fill="#fff" opacity=".3"/>
</svg>'''


ICONS = {}

# Москвариум — рыбка-клоун с пузырьками
ICONS["moskvarium"] = svg("blue", f'''
<circle cx="98" cy="34" r="5" fill="#fff" opacity=".9" {s('stroke-width="2"')}/><circle cx="106" cy="22" r="3" fill="#fff" opacity=".9" {s('stroke-width="2"')}/>
<path d="M90 64 L110 46 Q114 64 110 82Z" fill="#FF9A3C" {s()}/>
<path d="M56 34 Q64 22 74 34Z M56 94 Q64 106 74 94Z" fill="#FF9A3C" {s()}/>
<ellipse cx="60" cy="64" rx="36" ry="30" fill="#FFA54C" {s()}/>
<path d="M44 37 Q36 64 44 91 L52 92 Q44 64 52 36Z" fill="#fff" {s('stroke-width="2.4"')}/>
<path d="M72 36 Q64 64 72 92 L80 89 Q72 64 80 39Z" fill="#fff" {s('stroke-width="2.4"')}/>
{face(36, 62, d=0, k=1.1, blush=False, mouth=False)}
<circle cx="35" cy="62" r="7" fill="#fff" {s()}/>{eye(35, 62, 1.0)}
<ellipse cx="26" cy="72" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/>
<path d="M28 76 Q32 80 36 77" fill="none" {s('stroke-width="2.5"')}/>
<path d="M58 70 Q66 76 60 82" fill="none" {s()}/>
''')

# Зоопарк — жирафик
ICONS["zoo"] = svg("green", f'''
<path d="M50 130 L54 86 L76 86 L80 130Z" fill="#FFD25E" {s()}/>
<circle cx="62" cy="100" r="5" fill="#F0A04B"/><circle cx="70" cy="116" r="5" fill="#F0A04B"/>
<path d="M54 36 L52 22 M76 36 L78 22" {s()}/>
<circle cx="52" cy="20" r="5.5" fill="#C98547" {s('stroke-width="2.6"')}/><circle cx="78" cy="20" r="5.5" fill="#C98547" {s('stroke-width="2.6"')}/>
<ellipse cx="34" cy="48" rx="11" ry="6" fill="#FFD25E" transform="rotate(-20 34 48)" {s()}/>
<ellipse cx="96" cy="48" rx="11" ry="6" fill="#FFD25E" transform="rotate(20 96 48)" {s()}/>
<ellipse cx="65" cy="58" rx="27" ry="25" fill="#FFD25E" {s()}/>
<ellipse cx="65" cy="74" rx="17" ry="11" fill="#FFE9B0" {s()}/>
<circle cx="59" cy="72" r="1.8" fill="{O}"/><circle cx="71" cy="72" r="1.8" fill="{O}"/>
{face(65, 56, d=11, mouth=False)}
<path d="M61 78 Q65 82 69 78" fill="none" {s('stroke-width="2.4"')}/>
<circle cx="46" cy="42" r="3.5" fill="#F0A04B"/><circle cx="85" cy="40" r="3" fill="#F0A04B"/>
''')

# Экспериментаниум — колба-смайлик
ICONS["experimentanium"] = svg("purple", f'''
<circle cx="58" cy="20" r="5" fill="#C9FFC4" {s('stroke-width="2.4"')}/><circle cx="72" cy="12" r="3.5" fill="#C9FFC4" {s('stroke-width="2.4"')}/><circle cx="80" cy="24" r="4" fill="#C9FFC4" {s('stroke-width="2.4"')}/>
<path d="M54 32 H74 M58 32 V52 L36 92 Q32 104 44 106 H84 Q96 104 92 92 L70 52 V32" fill="#F4FBFF" {s()}/>
<path d="M46 74 H82 L91 92 Q95 102 84 103 H44 Q33 102 37 92Z" fill="#7BE87B"/>
<path d="M54 32 H74 M58 32 V52 L36 92 Q32 104 44 106 H84 Q96 104 92 92 L70 52 V32" fill="none" {s()}/>
{face(64, 86, d=8, k=0.9)}
<path d="M62 38 V50" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
{sparkle(100, 50, 6)}{sparkle(26, 52, 4)}
''')

# Палеонтологический — динозаврик вылупляется из яйца
ICONS["paleo"] = svg("orange", f'''
<path d="M44 42 L48 30 L54 40 L60 28 L64 40" fill="#5ACB7A" {s()}/>
<ellipse cx="62" cy="54" rx="24" ry="22" fill="#6FD68B" {s()}/>
{face(62, 54, d=9)}
<path d="M30 74 Q30 112 64 112 Q98 112 98 74 L90 82 L82 72 L74 82 L64 72 L54 82 L46 72 L38 82Z" fill="#FFF6E6" {s()}/>
<circle cx="50" cy="98" r="4" fill="#FFD0A8"/><circle cx="78" cy="94" r="5" fill="#FFD0A8"/><circle cx="64" cy="104" r="3" fill="#FFD0A8"/>
<path d="M28 64 Q22 56 26 48 M100 64 Q106 56 102 48" fill="none" {s('stroke-width="2.6"')}/>
{sparkle(24, 34, 5)}{sparkle(104, 30, 4)}
''')

# Дарвиновский — бабочка с улыбкой
ICONS["darwin"] = svg("pink", f'''
<ellipse cx="40" cy="52" rx="22" ry="17" fill="#FFB86B" transform="rotate(-25 40 52)" {s()}/>
<ellipse cx="88" cy="52" rx="22" ry="17" fill="#FFB86B" transform="rotate(25 88 52)" {s()}/>
<ellipse cx="46" cy="86" rx="15" ry="12" fill="#B99BFF" transform="rotate(25 46 86)" {s()}/>
<ellipse cx="82" cy="86" rx="15" ry="12" fill="#B99BFF" transform="rotate(-25 82 86)" {s()}/>
<circle cx="38" cy="50" r="6" fill="#FFF07A"/><circle cx="90" cy="50" r="6" fill="#FFF07A"/>
<circle cx="46" cy="88" r="3.5" fill="#fff"/><circle cx="82" cy="88" r="3.5" fill="#fff"/>
<rect x="57" y="54" width="14" height="44" rx="7" fill="#7A5CC2" {s()}/>
<circle cx="64" cy="44" r="13" fill="#7A5CC2" {s()}/>
<path d="M58 32 Q52 20 46 20 M70 32 Q76 20 82 20" fill="none" {s()}/>
<circle cx="46" cy="20" r="3.5" fill="#FF7FA8" {s('stroke-width="2"')}/><circle cx="82" cy="20" r="3.5" fill="#FF7FA8" {s('stroke-width="2"')}/>
<ellipse cx="59" cy="44" rx="2.8" ry="3.4" fill="#fff"/><ellipse cx="69" cy="44" rx="2.8" ry="3.4" fill="#fff"/>
<circle cx="59.5" cy="44.5" r="1.6" fill="{O}"/><circle cx="69.5" cy="44.5" r="1.6" fill="{O}"/>
<path d="M60 50 Q64 53 68 50" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
''')

# Музей космонавтики — ракета с улыбкой
ICONS["cosmos"] = svg("night", f'''
{sparkle(26, 40, 5)}{sparkle(102, 34, 6)}{sparkle(100, 92, 4)}{sparkle(28, 92, 3.5)}
<path d="M56 98 Q64 120 72 98Z" fill="#FFB84D"/><path d="M59 98 Q64 112 69 98Z" fill="#FFF3A0"/>
<path d="M48 78 L36 96 L52 92Z" fill="#FF7A8A" {s()}/><path d="M80 78 L92 96 L76 92Z" fill="#FF7A8A" {s()}/>
<path d="M64 16 C80 28 86 56 80 92 H48 C42 56 48 28 64 16Z" fill="#FFFFFF" {s()}/>
<path d="M55 26 Q64 16 73 26 Q64 31 55 26Z" fill="#FF7A8A"/>
<path d="M64 16 C80 28 86 56 80 92 H48 C42 56 48 28 64 16Z" fill="none" {s()}/>
<circle cx="64" cy="48" r="10" fill="#9ED8FF" {s()}/><circle cx="60" cy="44" r="3" fill="#fff"/>
{face(64, 72, d=7, k=0.85)}
''')

# Музей транспорта — трамвайчик с мордочкой
ICONS["transport"] = svg("yellow", f'''
<path d="M56 30 L64 18 L72 30 M50 18 H78" fill="none" {s()}/>
<rect x="28" y="30" width="72" height="70" rx="16" fill="#FF6B6B" {s()}/>
<rect x="36" y="38" width="56" height="30" rx="8" fill="#D6F0FF" {s()}/>
{face(64, 52, d=11)}
<rect x="28" y="74" width="72" height="6" fill="#FFF3D6"/>
<circle cx="40" cy="88" r="5" fill="#FFF3A0" {s('stroke-width="2.5"')}/><circle cx="88" cy="88" r="5" fill="#FFF3A0" {s('stroke-width="2.5"')}/>
<rect x="34" y="100" width="14" height="9" rx="4" fill="#6B6F86" {s()}/><rect x="80" y="100" width="14" height="9" rx="4" fill="#6B6F86" {s()}/>
<path d="M16 110 H112" {s()}/>
''')

# Политех — лампочка-смайлик с шестерёнкой
def gear(cx, cy, r, teeth, color):
    pts = []
    for i in range(teeth * 2):
        a = math.pi * i / teeth
        rr = r if i % 2 == 0 else r * 0.78
        pts.append(f"{cx + rr*math.cos(a):.1f},{cy + rr*math.sin(a):.1f}")
    return (f'<polygon points="{" ".join(pts)}" fill="{color}" {s()}/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*0.32:.1f}" fill="#fff" {s()}/>')

ICONS["polytech-open"] = svg("teal", f'''
{gear(94, 90, 16, 8, "#A9B7CF")}
<path d="M64 18 C84 18 94 34 90 50 C88 60 80 66 78 78 H50 C48 66 40 60 38 50 C34 34 44 18 64 18Z" fill="#FFE97A" {s()}/>
{face(64, 46, d=9)}
<rect x="50" y="78" width="28" height="8" rx="3" fill="#C9D3E4" {s()}/>
<rect x="52" y="86" width="24" height="8" rx="3" fill="#C9D3E4" {s()}/>
<path d="M58 94 H70 L66 100 H62Z" fill="#6B6F86" {s()}/>
<path d="M48 30 Q52 24 58 22" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
<path d="M24 34 L31 39 M104 34 L97 39 M24 56 H32" {s()}/>
''')

# Остров Мечты — карусель с лошадкой
ICONS["ostrov-mechty"] = svg("pink", f'''
<path d="M64 12 V22" {s()}/><path d="M64 12 L76 16 L64 20Z" fill="#FFD25E" {s('stroke-width="2.4"')}/>
<path d="M22 44 Q64 4 106 44Z" fill="#fff" {s()}/>
<path d="M64 22 L36 44 H50Z M64 22 L64 44 H78Z M64 22 L92 44 H106" fill="#FF7FA8"/>
<path d="M22 44 Q64 4 106 44Z" fill="none" {s()}/>
<path d="M20 44 Q27 52 34 44 Q41 52 48 44 Q55 52 62 44 Q69 52 76 44 Q83 52 90 44 Q97 52 104 44 Q106 48 108 44" fill="#FFD25E" {s('stroke-width="2.4"')}/>
<path d="M26 50 V102 M102 50 V102 M64 50 V104" {s()}/>
<path d="M44 84 Q34 82 34 94" fill="none" stroke="#C9A7FF" stroke-width="6" stroke-linecap="round"/>
<rect x="46" y="94" width="7" height="12" rx="3" fill="#fff" {s('stroke-width="2.4"')}/><rect x="74" y="94" width="7" height="12" rx="3" fill="#fff" {s('stroke-width="2.4"')}/>
<ellipse cx="62" cy="86" rx="20" ry="11" fill="#fff" {s()}/>
<path d="M74 82 Q76 66 84 60 L94 66 Q90 76 80 86Z" fill="#fff" {s()}/>
<ellipse cx="90" cy="64" rx="11" ry="8" fill="#fff" transform="rotate(25 90 64)" {s()}/>
<path d="M82 56 L84 46 L90 55Z" fill="#fff" {s('stroke-width="2.4"')}/>
<path d="M82 58 Q74 62 72 74" fill="none" stroke="#C9A7FF" stroke-width="6" stroke-linecap="round"/>
{eye(90, 62, 0.7)}
<ellipse cx="96" cy="68" rx="3" ry="1.8" fill="#FF7FA8" opacity=".7"/>
<path d="M54 76 Q62 72 70 76 L68 84 Q62 86 56 84Z" fill="#FF7FA8" {s('stroke-width="2.2"')}/>
<rect x="14" y="104" width="100" height="9" rx="4.5" fill="#FFD25E" {s()}/>
''')

# КидЗания — малыш-строитель
ICONS["kidzania"] = svg("blue", f'''
<path d="M30 124 Q32 100 64 98 Q96 100 98 124Z" fill="#FFA54C" {s()}/>
<path d="M52 102 L56 124 M76 102 L72 124" stroke="#FFF07A" stroke-width="5"/>
<circle cx="64" cy="70" r="26" fill="#FFDDBD" {s()}/>
<path d="M36 58 Q36 30 64 30 Q92 30 92 58Z" fill="#FFD43B" {s()}/>
<path d="M30 58 H98" stroke="{O}" stroke-width="9" stroke-linecap="round"/><path d="M30 58 H98" stroke="#FFD43B" stroke-width="4" stroke-linecap="round"/>
<path d="M64 30 V52" {s()}/>
{face(64, 72, d=10)}
''')

# Театр кукол — Петрушка за ширмой
ICONS["obraztsov"] = svg("purple", f'''
<path d="M16 24 H112" stroke="{O}" stroke-width="8" stroke-linecap="round"/><path d="M16 24 H112" stroke="#FF7A8A" stroke-width="3.5" stroke-linecap="round"/>
<path d="M18 28 Q28 56 22 88 L16 88 V28Z" fill="#FF8FA3" {s()}/>
<path d="M110 28 Q100 56 106 88 L112 88 V28Z" fill="#FF8FA3" {s()}/>
<path d="M50 30 L64 10 L78 30Z" fill="#FFD25E" {s()}/><circle cx="64" cy="10" r="4" fill="#fff" {s('stroke-width="2.4"')}/>
<circle cx="64" cy="48" r="20" fill="#FFDDBD" {s()}/>
{face(64, 48, d=8)}
<path d="M48 68 Q40 74 34 70 M80 68 Q88 74 94 70" fill="none" {s()}/>
<circle cx="32" cy="70" r="5" fill="#FFDDBD" {s()}/><circle cx="96" cy="70" r="5" fill="#FFDDBD" {s()}/>
<rect x="14" y="86" width="100" height="30" rx="6" fill="#6FA8FF" {s()}/>
<path d="M44 66 L50 86 H78 L84 66" fill="#FF7A8A" {s()}/>
<circle cx="40" cy="100" r="4" fill="#FFF07A"/><circle cx="64" cy="100" r="4" fill="#FFF07A"/><circle cx="88" cy="100" r="4" fill="#FFF07A"/>
''')

# Уголок Дурова — слонёнок с мячиком
ICONS["durov"] = svg("orange", f'''
<circle cx="98" cy="34" r="12" fill="#fff" {s()}/>
<path d="M86 30 Q98 26 110 34 M88 40 Q98 44 108 40" fill="none" stroke="#5CA9FF" stroke-width="3.5"/>
<ellipse cx="32" cy="62" rx="16" ry="20" fill="#C3CCDC" {s()}/><ellipse cx="32" cy="62" rx="9" ry="12" fill="#FFC2D4"/>
<ellipse cx="96" cy="70" rx="13" ry="17" fill="#C3CCDC" {s()} opacity="0"/>
<circle cx="62" cy="64" r="28" fill="#D3DAE6" {s()}/>
<path d="M68 80 Q74 98 86 96 Q96 92 94 78 Q92 62 96 50" fill="none" stroke="{O}" stroke-width="13" stroke-linecap="round"/>
<path d="M68 80 Q74 98 86 96 Q96 92 94 78 Q92 62 96 50" fill="none" stroke="#D3DAE6" stroke-width="6.5" stroke-linecap="round"/>
{face(58, 60, d=10, mouth=False)}
<path d="M46 108 Q46 94 62 92 Q76 94 78 108Z" fill="#D3DAE6" {s()}/>
''')

# Цирк Никулина — шатёр с флажками
ICONS["nikulin"] = svg("blue", f'''
<path d="M64 22 V10" {s()}/><path d="M64 10 L78 14 L64 18Z" fill="#FFD25E" {s('stroke-width="2.4"')}/>
<path d="M64 22 L102 62 H26Z" fill="#fff" {s()}/>
<path d="M64 22 L44 62 H56Z M64 22 L72 62 H84Z" fill="#FF7A8A"/>
<path d="M64 22 L102 62 H26Z" fill="none" {s()}/>
<rect x="28" y="62" width="72" height="46" fill="#FF8F8F" {s()}/>
<path d="M40 62 V108 M88 62 V108" stroke="#fff" stroke-width="7"/>
<rect x="28" y="62" width="72" height="46" fill="none" {s()}/>
<path d="M50 108 V88 Q64 74 78 88 V108Z" fill="#6A5A9E" {s()}/>
<path d="M24 62 Q31 70 38 62 Q45 70 52 62 Q59 70 66 62 Q73 70 80 62 Q87 70 94 62 Q99 68 104 62" fill="#FFD25E" {s('stroke-width="2.4"')}/>
{sparkle(22, 36, 5)}{sparkle(106, 38, 5, "#FFF07A")}
''')

# Большой цирк — морской котик с мячом
ICONS["bolshoy-circus"] = svg("purple", f'''
<circle cx="64" cy="24" r="12" fill="#FFE066" {s()}/>
<path d="M52 20 Q64 16 76 20 M52 30 Q64 34 76 30" fill="none" stroke="#FF7A8A" stroke-width="3.5"/>
<path d="M42 112 Q32 84 46 64 Q54 50 64 46 Q78 48 80 64 Q86 90 92 112Z" fill="#9AA8C4" {s()}/>
<ellipse cx="66" cy="92" rx="11" ry="16" fill="#C3CCDC"/>
<path d="M48 94 Q34 98 32 108 Q44 108 52 102Z M84 94 Q98 98 100 108 Q88 108 80 102Z" fill="#9AA8C4" {s()}/>
<circle cx="64" cy="66" r="18" fill="#9AA8C4" {s()}/>
{face(64, 64, d=8, mouth=False)}
<ellipse cx="64" cy="72" rx="5" ry="3.5" fill="{O}"/>
<path d="M56 74 L46 72 M56 76 L46 78 M72 74 L82 72 M72 76 L82 78" stroke="{O}" stroke-width="1.6"/>
<path d="M30 116 H98" {s()}/>
''')

# Театр Сац — поющие нотки
ICONS["sats"] = svg("yellow", f'''
<path d="M50 84 V34 L94 24 V74" fill="none" stroke="{O}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M50 34 L94 24 V36 L50 46Z" fill="{O}"/>
<path d="M50 84 V34 L94 24 V74" fill="none" stroke="#8E63E8" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<ellipse cx="40" cy="88" rx="16" ry="13" fill="#B99BFF" transform="rotate(-15 40 88)" {s()}/>
<ellipse cx="84" cy="78" rx="16" ry="13" fill="#FF9FC4" transform="rotate(-15 84 78)" {s()}/>
{face(40, 87, d=6, k=0.7)}{face(84, 77, d=6, k=0.7)}
{sparkle(24, 40, 5)}{sparkle(106, 52, 4)}{sparkle(102, 104, 5, "#fff")}
''')

# Планетарий — Сатурн с улыбкой
ICONS["planetarium"] = svg("night", f'''
{sparkle(24, 32, 5)}{sparkle(104, 28, 6)}{sparkle(26, 98, 4)}{sparkle(104, 100, 3.5)}
<ellipse cx="64" cy="66" rx="46" ry="12" fill="none" stroke="{O}" stroke-width="9" transform="rotate(-15 64 66)"/>
<ellipse cx="64" cy="66" rx="46" ry="12" fill="none" stroke="#FFE2B8" stroke-width="4.5" transform="rotate(-15 64 66)"/>
<circle cx="64" cy="64" r="28" fill="#FFAE6B" {s()}/>
<path d="M40 54 Q64 48 88 54" fill="none" stroke="#FF9A4D" stroke-width="5"/>
{face(64, 66, d=10)}
<path d="M20 80 Q64 74 108 52" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M20 80 Q64 74 108 52" fill="none" stroke="#FFE2B8" stroke-width="4.5" stroke-linecap="round"/>
''')

# Зарядье — мостик над рекой и солнышко
ICONS["zaryadye"] = svg("sky", f'''
<g stroke="#FFC53A" stroke-width="4" stroke-linecap="round"><path d="M96 14 V9 M112 26 L116 22 M80 26 L76 22"/></g>
<circle cx="96" cy="38" r="15" fill="#FFE066" {s()}/>
{face(96, 38, d=5.5, k=0.65)}
<circle cx="28" cy="44" r="13" fill="#7CD26E" {s()}/><circle cx="40" cy="52" r="10" fill="#5CC45A" {s()}/><path d="M32 56 V74" stroke="#8B5A2B" stroke-width="5" stroke-linecap="round"/>
<path d="M0 88 Q32 80 64 88 T128 88 V128 H0Z" fill="#6CC0F2" {s()}/>
<path d="M30 108 Q40 104 50 108 M78 110 Q88 106 98 110" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M14 96 Q64 46 114 96" fill="none" stroke="{O}" stroke-width="12" stroke-linecap="round"/>
<path d="M14 96 Q64 46 114 96" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>
<path d="M22 80 Q64 40 106 80" fill="none" {s()}/>
<path d="M34 76 V82 M48 66 V73 M64 61 V69 M80 66 V73 M94 76 V82" {s('stroke-width="2.6"')}/>
''')

# Парк Горького — колесо обозрения
def wheel_cabins(cx, cy, r):
    colors = ["#FF7A8A", "#FFD25E", "#7CD26E", "#6CB8FF", "#C9A7FF", "#FFAE6B", "#5CCDBA", "#F58CB8"]
    out = ""
    for i in range(8):
        a = 2 * math.pi * i / 8
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        out += f'<path d="M{cx} {cy} L{x:.1f} {y:.1f}" stroke="{O}" stroke-width="2.4"/>'
    for i, c in enumerate(colors):
        a = 2 * math.pi * i / 8
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        out += f'<rect x="{x-7:.1f}" y="{y-2:.1f}" width="14" height="12" rx="5" fill="{c}" {s("stroke-width=\"2.4\"")}/>'
    return out

ICONS["gorky-park"] = svg("orange", f'''
<path d="M64 58 L42 112 M64 58 L86 112 M32 112 H96" fill="none" {s()}/>
<circle cx="64" cy="58" r="34" fill="none" stroke="{O}" stroke-width="8"/>
<circle cx="64" cy="58" r="34" fill="none" stroke="#fff" stroke-width="3.5"/>
{wheel_cabins(64, 58, 34)}
<circle cx="64" cy="58" r="12" fill="#FFE066" {s()}/>
{face(64, 57, d=4.5, k=0.55, blush=False)}
''')

# ВДНХ — золотой фонтан
ICONS["vdnh"] = svg("blue", f'''
<path d="M64 50 Q44 24 26 62 M64 50 Q84 24 102 62 M64 50 Q54 34 42 66 M64 50 Q74 34 86 66" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<circle cx="26" cy="68" r="3.5" fill="#fff"/><circle cx="102" cy="68" r="3.5" fill="#fff"/>
<path d="M58 82 L60 54 H68 L70 82Z" fill="#FFD25E" {s()}/>
<circle cx="64" cy="48" r="8" fill="#FFD25E" {s()}/>
<path d="M18 82 H110 L102 100 H26Z" fill="#FFE066" {s()}/>
<path d="M26 88 H102" stroke="#6CC0F2" stroke-width="5"/>
<path d="M18 82 H110 L102 100 H26Z" fill="none" {s()}/>
<rect x="34" y="100" width="60" height="10" rx="2" fill="#FFC53A" {s()}/>
{face(64, 89, d=12, k=0.7, blush=False)}
''')

# Ферма — овечка
ICONS["vdnh-farm"] = svg("green", f'''
<path d="M50 96 V112 M60 98 V114 M80 98 V114 M90 96 V112" stroke="{O}" stroke-width="5.5" stroke-linecap="round"/>
<g fill="#fff" {s()}>
<circle cx="52" cy="70" r="14"/><circle cx="68" cy="60" r="15"/><circle cx="86" cy="66" r="14"/><circle cx="94" cy="82" r="13"/>
<circle cx="80" cy="94" r="13"/><circle cx="60" cy="92" r="13"/><circle cx="72" cy="78" r="18"/>
</g>
<circle cx="72" cy="78" r="17" fill="#fff"/><circle cx="68" cy="64" r="12" fill="#fff"/><circle cx="84" cy="70" r="12" fill="#fff"/>
<ellipse cx="28" cy="66" rx="9" ry="5" fill="#FFDDBD" transform="rotate(-30 28 66)" {s('stroke-width="2.6"')}/>
<ellipse cx="38" cy="76" rx="17" ry="18" fill="#FFDDBD" {s()}/>
{face(38, 76, d=7, k=0.85)}
<circle cx="32" cy="58" r="7" fill="#fff" {s('stroke-width="2.4"')}/><circle cx="42" cy="56" r="7" fill="#fff" {s('stroke-width="2.4"')}/>
''')

# Атом — атом с улыбчивым ядром
ICONS["vdnh-atom"] = svg("night", f'''
{sparkle(22, 26, 4)}{sparkle(106, 104, 4.5)}{sparkle(108, 24, 3)}
<g fill="none">
<ellipse cx="64" cy="64" rx="44" ry="15" stroke="{O}" stroke-width="8"/><ellipse cx="64" cy="64" rx="44" ry="15" stroke="#9ED8FF" stroke-width="4"/>
<ellipse cx="64" cy="64" rx="44" ry="15" stroke="{O}" stroke-width="8" transform="rotate(60 64 64)"/><ellipse cx="64" cy="64" rx="44" ry="15" stroke="#C9A7FF" stroke-width="4" transform="rotate(60 64 64)"/>
<ellipse cx="64" cy="64" rx="44" ry="15" stroke="{O}" stroke-width="8" transform="rotate(-60 64 64)"/><ellipse cx="64" cy="64" rx="44" ry="15" stroke="#7FEBC6" stroke-width="4" transform="rotate(-60 64 64)"/>
</g>
<circle cx="64" cy="64" r="16" fill="#FF8F8F" {s()}/>
{face(64, 63, d=6, k=0.7)}
<circle cx="108" cy="64" r="5.5" fill="#FFE066" {s('stroke-width="2.4"')}/>
<circle cx="42" cy="26" r="5.5" fill="#FFE066" {s('stroke-width="2.4"')}/>
<circle cx="42" cy="102" r="5.5" fill="#FFE066" {s('stroke-width="2.4"')}/>
''')

# Макет «Моя Россия» — паровозик с мордочкой
ICONS["my-russia-maket"] = svg("sky", f'''
<circle cx="44" cy="22" r="8" fill="#fff" {s('stroke-width="2.4"')}/><circle cx="58" cy="16" r="6" fill="#fff" {s('stroke-width="2.4"')}/><circle cx="34" cy="14" r="5" fill="#fff" {s('stroke-width="2.4"')}/>
<path d="M38 48 L36 32 H50 L48 48Z" fill="#6B6F86" {s()}/>
<rect x="76" y="34" width="34" height="50" rx="6" fill="#FF6B6B" {s()}/>
<rect x="72" y="28" width="42" height="9" rx="4" fill="#6B6F86" {s()}/>
<rect x="84" y="44" width="18" height="14" rx="3" fill="#D6F0FF" {s()}/>
<rect x="22" y="48" width="58" height="36" rx="13" fill="#6CB8FF" {s()}/>
<circle cx="30" cy="66" r="16" fill="#E9EEF7" {s()}/>
{face(30, 64, d=6, k=0.75)}
<circle cx="40" cy="96" r="9" fill="#FF6B6B" {s()}/><circle cx="62" cy="96" r="9" fill="#FF6B6B" {s()}/><circle cx="92" cy="94" r="12" fill="#FF6B6B" {s()}/>
<circle cx="40" cy="96" r="2.5" fill="{O}"/><circle cx="62" cy="96" r="2.5" fill="{O}"/><circle cx="92" cy="94" r="3.5" fill="{O}"/>
<path d="M16 108 H112" {s()}/>
''')

# Аптекарский огород — пальмочка в горшке в оранжерее
ICONS["aptekarsky"] = svg("teal", f'''
<path d="M22 108 V64 Q22 26 64 24 Q106 26 106 64 V108" fill="#F0FFFC" opacity=".5" {s()}/>
<path d="M43 108 V36 M85 108 V36 M22 74 H106" stroke="{O}" stroke-width="1.8" opacity=".35"/>
<path d="M62 84 Q60 66 66 50 L71 52 Q66 68 68 84Z" fill="#C98547" {s()}/>
<path d="M68 50 Q52 36 34 48 Q50 44 66 54Z" fill="#7CD26E" {s()}/>
<path d="M68 50 Q84 34 100 46 Q84 44 70 54Z" fill="#7CD26E" {s()}/>
<path d="M68 50 Q62 30 48 28 Q60 38 64 52Z" fill="#5CC45A" {s()}/>
<path d="M68 50 Q76 30 90 30 Q78 40 72 52Z" fill="#5CC45A" {s()}/>
<path d="M44 84 H88 L82 110 H50Z" fill="#FF9F6B" {s()}/>
{face(66, 95, d=8, k=0.8)}
''')

# Коломенское — яблочко
ICONS["kolomenskoe"] = svg("green", f'''
<path d="M64 38 Q60 26 66 16" fill="none" stroke="#8B5A2B" stroke-width="6" stroke-linecap="round"/>
<path d="M66 32 Q82 14 98 26 Q84 40 66 32Z" fill="#7CD26E" {s()}/>
<path d="M64 42 C42 28 18 46 24 76 C30 104 52 112 64 104 C76 112 98 104 104 76 C110 46 86 28 64 42Z" fill="#FF6B6B" {s()}/>
<path d="M38 56 Q42 48 50 46" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".85"/>
{face(64, 72, d=12)}
''')

# Царицыно — сказочный замок
ICONS["tsaritsyno"] = svg("pink", f'''
<path d="M22 110 V62 H44 V110Z M84 110 V62 H106 V110Z" fill="#FF8F8F" {s()}/>
<path d="M18 62 L33 34 L48 62Z M80 62 L95 34 L110 62Z" fill="#7CD26E" {s()}/>
<rect x="40" y="70" width="48" height="40" fill="#FFA3A3" {s()}/>
<path d="M40 70 V60 H48 V66 H56 V60 H64 V66 H72 V60 H80 V66 H88 V70" fill="#FFA3A3" {s()}/>
<path d="M54 110 V96 Q64 86 74 96 V110Z" fill="#8A6CC9" {s()}/>
{face(64, 80, d=9, k=0.75)}
<rect x="30" y="76" width="6" height="9" rx="3" fill="#FFF3A0"/><rect x="92" y="76" width="6" height="9" rx="3" fill="#FFF3A0"/>
<path d="M33 34 V22 M95 34 V22" {s()}/><path d="M33 22 L43 26 L33 30Z M95 22 L105 26 L95 30Z" fill="#FFD25E" {s('stroke-width="2.4"')}/>
<path d="M14 112 H114" {s()}/>
''')

# Сокольники — бельчонок с орешком
ICONS["sokolniki"] = svg("green", f'''
<path d="M76 106 Q112 104 106 66 Q100 38 80 42 Q96 54 92 70 Q88 86 72 90Z" fill="#FF9A4D" {s()}/>
<path d="M88 56 Q96 66 92 80" fill="none" stroke="#FFC48A" stroke-width="5" stroke-linecap="round"/>
<ellipse cx="56" cy="88" rx="20" ry="22" fill="#FFA65C" {s()}/>
<ellipse cx="56" cy="94" rx="11" ry="13" fill="#FFE8CC"/>
<path d="M36 40 L34 24 L48 36Z M60 36 L68 22 L68 40Z" fill="#FFA65C" {s()}/>
<circle cx="52" cy="56" r="20" fill="#FFA65C" {s()}/>
{face(52, 56, d=8)}
<ellipse cx="56" cy="86" rx="8" ry="9" fill="#D9A15E" {s()}/>
<path d="M47 81 Q56 72 65 81Z" fill="#8B5A2B" {s()}/>
<path d="M40 112 H82" {s()}/>
''')

# ЦДМ — плюшевый мишка
ICONS["tsdm"] = svg("yellow", f'''
<circle cx="36" cy="40" r="14" fill="#D59A5E" {s()}/><circle cx="92" cy="40" r="14" fill="#D59A5E" {s()}/>
<circle cx="36" cy="40" r="7" fill="#F2C99A"/><circle cx="92" cy="40" r="7" fill="#F2C99A"/>
<circle cx="64" cy="66" r="36" fill="#E0A86C" {s()}/>
<ellipse cx="64" cy="80" rx="17" ry="13" fill="#F7DDB8" {s()}/>
<ellipse cx="64" cy="74" rx="6.5" ry="4.5" fill="{O}"/>
<path d="M64 78 V83 M57 84 Q64 90 71 84" fill="none" {s('stroke-width="2.5"')}/>
{face(64, 60, d=13, mouth=False)}
<path d="M50 104 L64 109 L78 104 L78 118 L64 113 L50 118Z" fill="#FF7A8A" {s()}/><circle cx="64" cy="111" r="4.5" fill="#FF7A8A" {s()}/>
''')

# Биологический музей — черепашка (целиком внутри)
ICONS["timiryazev-bio"] = svg("teal", f'''
<ellipse cx="46" cy="94" rx="7" ry="9" fill="#A8E06A" {s()}/><ellipse cx="80" cy="94" rx="7" ry="9" fill="#A8E06A" {s()}/>
<path d="M92 82 L102 86 L92 90Z" fill="#A8E06A" {s()}/>
<circle cx="32" cy="70" r="14" fill="#A8E06A" {s()}/>
{face(30, 70, d=5.5, k=0.7)}
<path d="M38 86 Q38 46 64 46 Q92 46 94 86Z" fill="#5CC45A" {s()}/>
<path d="M54 52 L50 66 L58 78 L72 78 L80 66 L76 52 M50 66 H40 M80 66 H92" fill="none" stroke="#D3F59E" stroke-width="3"/>
<path d="M38 86 Q38 46 64 46 Q92 46 94 86Z" fill="none" {s()}/>
<path d="M34 86 H98" stroke="{O}" stroke-width="7" stroke-linecap="round"/><path d="M34 86 H98" stroke="#FFE066" stroke-width="3" stroke-linecap="round"/>
<path d="M26 104 H102" {s()}/>
''')

# Зоомузей МГУ — совёнок
ICONS["zoomuseum-msu"] = svg("purple", f'''
<path d="M26 106 H102" stroke="#A86F3E" stroke-width="7" stroke-linecap="round"/>
<path d="M40 40 L36 24 L50 34Z M88 40 L92 24 L78 34Z" fill="#C98547" {s()}/>
<path d="M36 94 Q28 56 42 40 Q64 26 86 40 Q100 56 92 94 Q64 110 36 94Z" fill="#D59A5E" {s()}/>
<path d="M46 94 Q42 72 64 68 Q86 72 82 94 Q64 102 46 94Z" fill="#F7DDB8"/>
<circle cx="52" cy="56" r="12" fill="#fff" {s()}/><circle cx="76" cy="56" r="12" fill="#fff" {s()}/>
{eye(53, 57, 1.25)}{eye(75, 57, 1.25)}
<path d="M60 66 L68 66 L64 74Z" fill="#FFB84D" {s('stroke-width="2.4"')}/>
<ellipse cx="42" cy="72" rx="4.5" ry="2.6" fill="#FF7FA8" opacity=".6"/><ellipse cx="86" cy="72" rx="4.5" ry="2.6" fill="#FF7FA8" opacity=".6"/>
<path d="M36 70 Q26 82 34 96 M92 70 Q102 82 94 96" fill="none" {s()}/>
''')

# Мореон — дельфинчик над волной
ICONS["moreon"] = svg("blue", f'''
<circle cx="24" cy="36" r="3" fill="#fff"/><circle cx="104" cy="30" r="3.5" fill="#fff"/><circle cx="94" cy="22" r="2.4" fill="#fff"/>
<path d="M56 46 L64 30 L74 48Z" fill="#7CC8F2" {s()}/>
<path d="M30 74 Q20 62 12 60 Q18 72 14 86 Q22 80 32 80Z" fill="#7CC8F2" {s()}/>
<path d="M24 76 C24 56 46 44 68 46 C80 47 88 50 94 54 L108 55 Q114 59 108 63 L94 64 C88 74 74 82 58 82 C44 82 30 82 24 76Z" fill="#A5DBFA" {s()}/>
<path d="M40 78 Q66 80 88 66" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/>
<path d="M58 72 L52 86 L68 76Z" fill="#7CC8F2" {s()}/>
{eye(84, 55, 0.85)}
<ellipse cx="88" cy="63" rx="3.5" ry="2" fill="#FF7FA8" opacity=".7"/>
<path d="M95 60 Q100 62 104 60" fill="none" {s('stroke-width="2.4"')}/>
<path d="M0 96 Q16 86 32 96 T64 96 T96 96 T128 96 V128 H0Z" fill="#4DA3E6" {s()}/>
<path d="M14 108 Q24 102 34 108 M74 110 Q84 104 94 110" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M44 92 Q40 86 44 80 M80 92 Q86 86 84 80" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''')


if __name__ == "__main__":
    out_dir = os.path.join(OUT, "svg")
    os.makedirs(out_dir, exist_ok=True)
    for f in os.listdir(out_dir):
        os.remove(os.path.join(out_dir, f))
    for pid, data in ICONS.items():
        with open(os.path.join(out_dir, f"{pid}.svg"), "w") as f:
            f.write(data)
    print(len(ICONS), "icons")
