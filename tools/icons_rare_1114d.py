"""Иконки робота rare 14.11 (1114d). Каждая придумана и нарисована отдельно (правило абсолютной уникальности):
свой герой, своя сцена, своя компоновка и палитра.  python3 tools/icons_rare_1114d.py"""
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


I = {}

# 1. Bulldozer: бульдог-хоккеист в шлеме ведёт шайбу клюшкой, лёд, фон ледяной голубой
I["bulldozer-hockey-megasport"] = svg("#E8F7FF", "#7FB8E6", f'''
<path d="M0 100 Q64 92 128 100 V128 H0Z" fill="#F4FBFF" {s('stroke-width="2.4"')}/>
<path d="M20 96 L104 96" stroke="#E04848" stroke-width="3" opacity=".6"/>
<ellipse cx="58" cy="78" rx="26" ry="18" fill="#C98A4B" {s()}/>
<path d="M40 92 v8 M50 94 v7 M66 94 v7 M76 92 v8" {s('stroke-width="5"')}/>
<ellipse cx="54" cy="52" rx="24" ry="21" fill="#D9A066" {s()}/>
<path d="M30 46 Q28 30 40 30 Q44 40 38 48Z" fill="#8A5A2E" {s('stroke-width="2.4"')}/>
<path d="M78 46 Q80 30 68 30 Q64 40 70 48Z" fill="#8A5A2E" {s('stroke-width="2.4"')}/>
<path d="M32 44 Q32 22 54 21 Q76 22 76 44 Q66 36 54 36 Q42 36 32 44Z" fill="#2E6FD8" {s()}/>
<path d="M44 26 v12 M54 23 v13 M64 26 v12" stroke="#fff" stroke-width="2"/>
<ellipse cx="54" cy="62" rx="13" ry="9" fill="#F2D3B0" {s('stroke-width="2.4"')}/>
<ellipse cx="54" cy="57" rx="5" ry="3.5" fill="{O}"/>
{eye(45, 49, .9)}{eye(63, 49, .9)}
<path d="M46 66 Q54 72 62 66" fill="none" {s('stroke-width="2.4"')}/>
<path d="M48 66 l2 4 l2 -3 M56 66 l2 3 l2 -4" fill="#fff" {s('stroke-width="1.6"')}/>
<path d="M78 70 L98 100" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M78 70 L98 100" stroke="#E0B070" stroke-width="5" stroke-linecap="round"/>
<path d="M96 100 L114 100 Q118 100 117 104 L98 104 Z" fill="#E0B070" {s('stroke-width="2.6"')}/>
<ellipse cx="108" cy="110" rx="9" ry="3.6" fill="#1E1E2A" {s('stroke-width="2"')}/>
<path d="M90 112 h-12 M92 116 h-16" stroke="#9AC7E8" stroke-width="2.4" stroke-linecap="round"/>
''')

# 2. «Безумные снежинки»: огромный белый конёк фигуриста с голубыми снежинками-шнурками крутит вращение на зубце,
#    вокруг по орбите кружат три снежинки с косыми глазками; фон тёмно-сиреневый вечерний
def flake(x, y, r, c="#fff"):
    out = ""
    for a in (0, 60, 120):
        out += f'<path d="M{x} {y-r} V{y+r}" stroke="{c}" stroke-width="2.4" stroke-linecap="round" transform="rotate({a} {x} {y})"/>'
    return out


I["crazy-snowflakes-soloslovo"] = svg("#B9A8F0", "#4B3A9A", f'''
<ellipse cx="64" cy="64" rx="50" ry="16" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="5 6" opacity=".7" transform="rotate(-14 64 64)"/>
<g transform="rotate(-10 64 66)">
<path d="M44 24 Q44 18 52 18 H72 Q78 18 78 26 L80 70 Q96 72 98 84 Q98 90 92 90 H46 Q40 90 40 84 Z" fill="#FFFFFF" {s()}/>
<path d="M50 30 l20 6 M50 38 l20 6 M50 46 l20 6 M50 54 l20 6" stroke="#5CB8F0" stroke-width="3" stroke-linecap="round"/>
<path d="M46 90 V98 M90 90 V98" {s('stroke-width="3"')}/>
<path d="M36 100 H96 Q102 100 100 106 L94 104 H38 Q32 104 36 100Z" fill="#D8DEE8" {s('stroke-width="2.6"')}/>
<path d="M36 100 l-4 4 l4 2" fill="none" {s('stroke-width="2.4"')}/>
{eye(56, 72, .9)}{eye(72, 72, .9)}
<path d="M58 80 Q64 86 70 80" fill="none" {s('stroke-width="2.4"')}/>
</g>
{flake(20, 46, 7)}<circle cx="18" cy="44" r="1" fill="{O}"/><circle cx="22" cy="44" r="1" fill="{O}"/>
{flake(108, 58, 8)}<circle cx="106" cy="56" r="1" fill="{O}"/><circle cx="111" cy="57" r="1" fill="{O}"/>
{flake(96, 22, 5, "#CFEFFF")}
<path d="M14 72 q6 6 12 2 M104 84 q6 -4 10 2" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
''', cx="50%", cy="45%")

# 3. Ping Point: красная ракетка для настольного тенниса, перевёрнутая как метка на карте, воткнута ручкой в зелёный стол,
#    над ней подпрыгивает белый мячик; фон мандариновый
I["pingpoint-tt-savelovskaya"] = svg("#FFE9C8", "#FF9E4A", f'''
<path d="M6 104 L122 104 L112 118 L16 118Z" fill="#2E9E5B" {s()}/>
<path d="M64 104 L64 118" stroke="#fff" stroke-width="2"/>
<path d="M11 110 H117" stroke="#fff" stroke-width="1.6" opacity=".7"/>
<ellipse cx="64" cy="104" rx="10" ry="3" fill="#1D6E3E" opacity=".5"/>
<path d="M58 76 L64 104 L70 76 Z" fill="#C88A4A" {s()}/>
<circle cx="64" cy="50" r="30" fill="#E23B3B" {s()}/>
<circle cx="64" cy="50" r="22" fill="#F25C5C"/>
{face(64, 48, 8, 1.0)}
<circle cx="98" cy="20" r="8" fill="#FFFFFF" {s('stroke-width="2.6"')}/>
<path d="M90 30 q-4 6 -8 8 M88 26 q-8 2 -12 0" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
''', cx="40%", cy="30%")

# 4. «Самолёт Арена»: маленький голубой самолётик с мордашкой стоит на двух коньках-лезвиях вместо шасси и скользит по льду,
#    за ним две белые царапины-следа; фон розово-лиловый закат
I["samolet-arena-rink-kommunarka"] = svg("#FFE0F0", "#C98BE0", f'''
<path d="M0 98 Q64 90 128 98 V128 H0Z" fill="#EAF6FF" {s('stroke-width="2.4"')}/>
<path d="M8 108 Q30 104 52 106 M14 116 Q36 112 58 114" stroke="#9CC9EC" stroke-width="2.4" fill="none" stroke-linecap="round"/>
<path d="M58 60 L74 30 Q78 26 82 30 L80 60Z" fill="#7CC4F5" {s()}/>
<path d="M22 70 L12 50 Q12 46 16 48 L32 62Z" fill="#7CC4F5" {s()}/>
<path d="M22 58 Q22 50 34 50 H96 Q118 52 118 66 Q118 80 96 82 H34 Q22 82 22 70Z" fill="#4AA3EA" {s()}/>
<circle cx="102" cy="62" r="6" fill="#E9F8FF" {s('stroke-width="2.4"')}/>
<path d="M40 66 H70 L62 76 H46Z" fill="#2E7BC4" {s('stroke-width="2.4"')}/>
{face(84, 64, 7, .85)}
<path d="M44 82 V92 M86 82 V92" {s('stroke-width="3"')}/>
<path d="M34 92 H56 Q60 92 58 96 H36Z M76 92 H98 Q102 92 100 96 H78Z" fill="#D7DEE8" {s('stroke-width="2.4"')}/>
{sparkle(30, 30, 6)}{sparkle(108, 26, 4)}
''')

# 5. СК «Легенда» (Домодедово): сам каток — овальное ледовое поле с синими бортами, вид сверху наискосок; лицо ему
#    нарезали коньки (глаза и улыбка — следы лезвий), над катком висит золотой лавровый венок легенды; фон глубокий синий
I["legenda-rink-domodedovo"] = svg("#4C6FD8", "#16245E", f'''
<ellipse cx="64" cy="80" rx="54" ry="34" fill="#2F6FD8" {s()}/>
<ellipse cx="64" cy="78" rx="46" ry="27" fill="#E9F6FF" {s('stroke-width="2.4"')}/>
<path d="M64 52 V104" stroke="#E04848" stroke-width="2" opacity=".5"/>
<circle cx="64" cy="78" r="8" fill="none" stroke="#5CA8E8" stroke-width="2" opacity=".7"/>
<path d="M44 70 q4 -8 8 0 M76 70 q4 -8 8 0" fill="none" stroke="#7BB6E6" stroke-width="3" stroke-linecap="round"/>
<path d="M44 84 Q64 100 84 84" fill="none" stroke="#7BB6E6" stroke-width="3" stroke-linecap="round"/>
<path d="M40 86 l-6 1 M88 86 l6 1" stroke="#7BB6E6" stroke-width="2" stroke-linecap="round"/>
<path d="M40 40 Q36 22 52 16 M88 40 Q92 22 76 16" fill="none" stroke="#E2B53A" stroke-width="3" stroke-linecap="round"/>
<path d="M40 34 q-8 -2 -8 -8 q8 0 8 8Z M38 26 q-6 -4 -4 -10 q6 2 4 10Z M44 20 q-2 -8 4 -10 q2 6 -4 10Z" fill="#F7C948" {s('stroke-width="1.8"')}/>
<path d="M88 34 q8 -2 8 -8 q-8 0 -8 8Z M90 26 q6 -4 4 -10 q-6 2 -4 10Z M84 20 q2 -8 -4 -10 q-2 6 4 10Z" fill="#F7C948" {s('stroke-width="1.8"')}/>
<circle cx="64" cy="14" r="4" fill="#FFE58A" {s('stroke-width="1.8"')}/>
{sparkle(112, 40, 4, "#FFE58A")}{sparkle(16, 52, 3)}
''', cx="50%", cy="25%")

# 6. Squash Time: чёрный сквош-мячик с двумя жёлтыми точками стал будильником — сверху две латунные чашечки звонка
#    и молоточек, внизу ножки; звенит у красной линии белой стены корта, рядом сосны загородного посёлка; фон хвойно-мятный
I["squash-time-myshenskoe"] = svg("#E2F6E6", "#7FC79A", f'''
<rect x="8" y="58" width="112" height="70" fill="#FFFFFF" {s('stroke-width="2.4"')}/>
<path d="M8 74 H120" stroke="#E04848" stroke-width="3"/>
<path d="M14 58 L22 36 L30 58Z M98 58 L106 32 L114 58Z" fill="#2F8A4E" {s('stroke-width="2.4"')}/>
<circle cx="40" cy="44" r="10" fill="#C9A13B" {s()}/>
<circle cx="88" cy="44" r="10" fill="#C9A13B" {s()}/>
<path d="M64 34 V44 M56 30 H72" {s('stroke-width="3.2"')}/>
<circle cx="64" cy="76" r="30" fill="#24242E" {s()}/>
<circle cx="56" cy="52" r="4" fill="#FFD53D" {s('stroke-width="1.6"')}/>
<circle cx="72" cy="52" r="4" fill="#FFD53D" {s('stroke-width="1.6"')}/>
<ellipse cx="54" cy="74" rx="4.4" ry="5.2" fill="#fff"/><circle cx="55" cy="75" r="2.4" fill="{O}"/>
<ellipse cx="74" cy="74" rx="4.4" ry="5.2" fill="#fff"/><circle cx="75" cy="75" r="2.4" fill="{O}"/>
<path d="M54 88 Q64 96 74 88" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<path d="M44 102 L38 114 M84 102 L90 114" {s('stroke-width="4"')}/>
<path d="M24 34 q-6 -4 -8 -10 M104 26 q6 -2 10 -8 M30 26 q-2 -6 0 -10" fill="none" stroke="{O}" stroke-width="2" stroke-linecap="round"/>
''')


# 7. ЛД «Крылатское»: сам ледовый дворец с волнистой крышей-«волной» и мордашкой на фасаде, перед ним большая голубая
#    ледовая дорожка-овал, по которой несётся красная шапочка-помпон конькобежца; фон утренний персиковый
I["krylatskoe-ld-rink"] = svg("#E3FBF1", "#5FC7A2", f'''
<ellipse cx="64" cy="106" rx="60" ry="18" fill="#CDEBFF" {s('stroke-width="2.6"')}/>
<ellipse cx="64" cy="106" rx="40" ry="9" fill="#F7FCFF" {s('stroke-width="2"')}/>
<path d="M14 82 Q30 40 48 62 Q64 30 80 62 Q98 40 114 82 Z" fill="#3D8BE0" {s()}/>
<rect x="18" y="72" width="92" height="22" rx="3" fill="#EAF2FA" {s()}/>
<path d="M24 78 h80" stroke="#9CC0E0" stroke-width="2"/>
{eye(52, 84, .8)}{eye(76, 84, .8)}
<path d="M58 89 Q64 93 70 89" fill="none" {s('stroke-width="2.2"')}/>
<circle cx="104" cy="106" r="6" fill="#E2453C" {s('stroke-width="2.2"')}/>
<circle cx="104" cy="99" r="3" fill="#fff" {s('stroke-width="1.6"')}/>
<path d="M92 104 h-14 M93 110 h-10" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>
{sparkle(100, 24, 5)}{sparkle(26, 30, 3)}
''', cx="45%", cy="25%")


# 8. «Космолёд» (Королёв): серебристый шарик Спутника-1 с четырьмя усами-антеннами, откинутыми назад, катится по
#    открытому катку на двух коньковых лезвиях; позади фонари и звёзды; фон тёмно-бирюзовый вечер
I["kosmoled-rink-korolev"] = svg("#3FA7A8", "#123F4F", f'''
<path d="M0 100 Q64 92 128 100 V128 H0Z" fill="#DFF4FF" {s('stroke-width="2.4"')}/>
<path d="M50 54 L6 40 M50 62 L4 62 M52 70 L8 84 M54 48 L18 22" stroke="{O}" stroke-width="4" stroke-linecap="round"/>
<path d="M50 54 L6 40 M50 62 L4 62 M52 70 L8 84 M54 48 L18 22" stroke="#C8CED8" stroke-width="2" stroke-linecap="round"/>
<circle cx="72" cy="62" r="26" fill="#D7DDE6" {s()}/>
<path d="M52 56 Q72 46 92 56" fill="none" stroke="#9AA4B4" stroke-width="2"/>
<circle cx="64" cy="48" r="5" fill="#fff" opacity=".7"/>
{face(74, 64, 8, .9)}
<path d="M62 86 V94 M84 86 V94" {s('stroke-width="3"')}/>
<path d="M54 94 H72 Q76 94 74 98 H56Z M76 94 H94 Q98 94 96 98 H78Z" fill="#AEB8C6" {s('stroke-width="2.2"')}/>
<path d="M40 106 h-16 M46 112 h-20" stroke="#8FC6EA" stroke-width="2.4" stroke-linecap="round"/>
{sparkle(104, 22, 5, "#FFE58A")}{sparkle(84, 14, 3)}{sparkle(116, 44, 3)}
''', cx="60%", cy="20%")

# 9. Каток в парке Малевича: красный супрематический круг с мордашкой в белых фигурных коньках катится по белому льду,
#    за ним наискосок лежат чёрная и жёлтая полосы-«бортики» в духе супрематизма; фон кремовый
I["malevich-rink-odintsovo"] = svg("#FFF8EA", "#EAD7B2", f'''
<rect x="-10" y="86" width="150" height="50" fill="#FFFFFF" {s('stroke-width="2.4"')}/>
<rect x="6" y="20" width="58" height="10" fill="#1E1E24" transform="rotate(-24 35 25)"/>
<rect x="70" y="24" width="44" height="8" fill="#F2C230" transform="rotate(-24 92 28)"/>
<rect x="14" y="100" width="34" height="6" fill="#2D5BD0" transform="rotate(-24 31 103)"/>
<circle cx="66" cy="58" r="26" fill="#E0342E" {s()}/>
{face(66, 56, 8, .95)}
<path d="M56 82 Q52 88 54 92 H66 Q66 86 62 82Z M72 82 Q70 88 72 92 H84 Q84 86 80 82Z" fill="#FFFFFF" {s('stroke-width="2.4"')}/>
<path d="M50 96 H68 M68 96 H88" {s('stroke-width="3"')}/>
<path d="M96 104 h18 M100 110 h14" stroke="#B9C4D4" stroke-width="2.2" stroke-linecap="round"/>
''')

if __name__ == "__main__":
    import sys
    for pid, body in I.items():
        if len(sys.argv) > 1 and pid not in sys.argv[1:]:
            continue
        open(os.path.join(ROOT, "icons-src", pid + ".svg"), "w").write(body)
    print(len(I))
