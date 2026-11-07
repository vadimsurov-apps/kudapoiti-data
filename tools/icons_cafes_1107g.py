"""Робот cafes, 2026-11-07 (13 UTC): иконки 29 новых кафе. Каждая придумана и нарисована отдельно
(правило абсолютной уникальности: свой герой, своя сцена, своя компоновка и палитра фона).
Запуск из корня: python3 tools/icons_cafes_1107g.py  → icons-src/<id>.svg + строки в icons-src/subjects.txt"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def W(w):
    return s(f'stroke-width="{w}"')


def svg2(a, b, body, cx="38%", cy="28%"):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
<defs>
 <radialGradient id="g" cx="{cx}" cy="{cy}" r="85%"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></radialGradient>
 <clipPath id="c"><circle cx="64" cy="64" r="61"/></clipPath>
</defs>
<circle cx="64" cy="64" r="61" fill="url(#g)"/>
<g clip-path="url(#c)">{body}</g>
<ellipse cx="44" cy="22" rx="20" ry="7" fill="#fff" opacity=".3"/>
</svg>'''


STEAM = 'fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round"'


def sleepy(cx, cy, d=8, k=1.0):
    """закрытые счастливые глазки-дужки"""
    return (f'<path d="M{cx-d-4*k} {cy} Q{cx-d} {cy-4*k} {cx-d+4*k} {cy} M{cx+d-4*k} {cy} Q{cx+d} {cy-4*k} {cx+d+4*k} {cy}" '
            f'fill="none" {W(2.4*k)}/>'
            f'<ellipse cx="{cx-d-4*k}" cy="{cy+6*k}" rx="{4*k}" ry="{2.3*k}" fill="#FF7FA8" opacity=".6"/>'
            f'<ellipse cx="{cx+d+4*k}" cy="{cy+6*k}" rx="{4*k}" ry="{2.3*k}" fill="#FF7FA8" opacity=".6"/>')


def ring(cx, cy, r, n, rx, ry, fill, sw=1.8):
    out = ""
    for i in range(n):
        a = 2 * math.pi * i / n
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        out += (f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{rx}" ry="{ry}" fill="{fill}" {W(sw)} '
                f'transform="rotate({math.degrees(a)+90:.0f} {x:.1f} {y:.1f})"/>')
    return out


I = {}

# 1 Леон — манговый мусс-львёнок с гривой из шоколадной стружки зевает на блюдце
I["cafe-leon-dmitrov"] = (svg2("#E0FBF4", "#3FB3A2", f'''
<ellipse cx="64" cy="104" rx="46" ry="11" fill="#FFFFFF" {s()}/>
<ellipse cx="64" cy="102" rx="30" ry="5" fill="#E6F4F1"/>
{ring(64, 66, 31, 14, 7, 11, "#7A4A28")}
<circle cx="40" cy="44" r="7" fill="#FFB43A" {s()}/><circle cx="88" cy="44" r="7" fill="#FFB43A" {s()}/>
<path d="M36 96 Q34 46 64 42 Q94 46 92 96Z" fill="#FFB43A" {s()}/>
<path d="M42 92 Q64 98 86 92" fill="none" stroke="#E8922A" stroke-width="2.4"/>
<path d="M46 62 Q50 58 54 62 M74 62 Q78 58 82 62" fill="none" {W(2.6)}/>
<ellipse cx="45" cy="70" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/><ellipse cx="83" cy="70" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/>
<ellipse cx="64" cy="76" rx="7" ry="9" fill="#8A2E3B" {W(2.4)}/>
<ellipse cx="64" cy="80" rx="4" ry="3" fill="#FF8FA3"/>
<path d="M60 66 L64 70 L68 66Z" fill="#7A4A28"/>
<path d="M98 30 q4 -6 10 -4 M100 22 q4 -6 10 -4" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
'''), "герой: манговый мусс-львёнок с гривой из шоколадной стружки | сцена: широко зевает, сидя на белом десертном блюдце")

# 2 Голенищево — горка гречки с тающим маслом в глиняной мисочке у окна избы
I["cafe-golenishchevo"] = (svg2("#FFF1DD", "#B7835A", f'''
<rect x="18" y="14" width="40" height="34" rx="3" fill="#CFEFFF" {s()}/>
<path d="M38 14 V48 M18 31 H58" {W(3)}/>
<path d="M14 12 H62" stroke="#8A5A33" stroke-width="5" stroke-linecap="round"/>
<rect x="0" y="100" width="128" height="30" fill="#A8703F" {s()}/>
<path d="M0 112 H128" stroke="#8A5A33" stroke-width="2"/>
<path d="M28 76 H100 Q98 104 64 106 Q30 104 28 76Z" fill="#C46A3A" {s()}/>
<path d="M34 88 Q64 94 94 88" fill="none" stroke="#F2C9A0" stroke-width="3"/>
<path d="M30 78 Q34 50 64 46 Q94 50 98 78Z" fill="#8A5A33" {s()}/>
<g fill="#B27A48">{''.join(f'<ellipse cx="{x}" cy="{y}" rx="2.2" ry="1.5"/>' for x, y in [(42,70),(50,62),(58,72),(74,58),(82,68),(88,74),(66,64),(46,76),(78,76)])}</g>
<path d="M56 46 L64 38 L74 44 L68 52 L58 52Z" fill="#FFE27A" {W(2.4)}/>
<path d="M60 52 Q58 58 62 60 M70 52 Q72 58 68 58" fill="#FFE27A" stroke="#E8C24A" stroke-width="1.6"/>
{face(64, 66, d=10, k=0.8)}
<path d="M84 34 Q80 26 86 18 M96 38 Q92 28 98 20" {STEAM}/>
'''), "герой: горка гречневой каши с тающим кубиком сливочного масла | сцена: дымится в глиняной мисочке на столе у окна деревенской избы")

# 3 Первый — корн-дог первым рвёт финишную ленточку
I["cafe-pervyy-elizavetino"] = (svg2("#EAF6FF", "#4C8BE0", f'''
<path d="M0 104 H128 V128 H0Z" fill="#E8574A"/>
<path d="M0 108 H128" stroke="#fff" stroke-width="2" stroke-dasharray="8 6"/>
<path d="M4 58 Q28 60 46 66" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>
<path d="M82 66 Q104 58 124 64" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>
<path d="M4 58 Q28 60 46 66 M82 66 Q104 58 124 64" fill="none" stroke="#E8574A" stroke-width="2" stroke-dasharray="4 4"/>
<g transform="rotate(14 64 64)">
<rect x="61" y="88" width="6" height="34" rx="3" fill="#F5E6C8" {W(2.4)}/>
<rect x="40" y="16" width="48" height="78" rx="24" fill="#E8A23A" {s()}/>
<path d="M50 30 Q56 36 50 42 Q44 48 50 54 Q56 60 50 66 Q44 72 50 78" fill="none" stroke="#FFD93A" stroke-width="4" stroke-linecap="round"/>
<g fill="#C9802A"><circle cx="76" cy="30" r="1.6"/><circle cx="80" cy="44" r="1.6"/><circle cx="74" cy="76" r="1.6"/></g>
{face(66, 54, d=9, k=0.85)}
</g>
<path d="M28 40 H14 M26 50 H8 M30 30 H18" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
'''), "герой: золотистый корн-дог на палочке с волной горчицы | сцена: первым рвёт грудью финишную ленточку на беговой дорожке")

# 4 Амарис — яйца Бенедикт укрылись соусом-голландез как пледом
I["cafe-amaris-konstantinovo"] = (svg2("#FFF0F5", "#D46A8F", f'''
<ellipse cx="64" cy="98" rx="54" ry="15" fill="#FFFFFF" {s()}/>
<ellipse cx="64" cy="96" rx="40" ry="8" fill="#F3EEF6"/>
<g>
<ellipse cx="42" cy="86" rx="20" ry="7" fill="#D9A55E" {s()}/>
<ellipse cx="42" cy="80" rx="20" ry="6" fill="#F28B9A" {W(2.4)}/>
<path d="M24 78 Q24 56 42 54 Q60 56 60 78Z" fill="#FFFFFF" {s()}/>
<path d="M22 74 Q24 58 42 56 Q60 58 62 74 Q58 84 54 76 Q48 86 42 78 Q36 86 30 76 Q26 84 22 74Z" fill="#FFD84A" {W(2.4)}/>
{sleepy(42, 68, d=6, k=0.7)}
</g>
<g>
<ellipse cx="86" cy="86" rx="20" ry="7" fill="#D9A55E" {s()}/>
<ellipse cx="86" cy="80" rx="20" ry="6" fill="#F28B9A" {W(2.4)}/>
<path d="M68 78 Q68 52 86 50 Q104 52 104 78Z" fill="#FFFFFF" {s()}/>
<path d="M66 72 Q68 54 86 52 Q104 54 106 72 Q102 84 98 74 Q92 86 86 76 Q80 86 74 74 Q70 84 66 72Z" fill="#FFD84A" {W(2.4)}/>
{face(86, 64, d=6, k=0.7)}
</g>
<g fill="#4CAF50"><circle cx="40" cy="58" r="1.8"/><circle cx="88" cy="54" r="1.8"/><circle cx="94" cy="58" r="1.4"/></g>
'''), "герой: двое яиц Бенедикт на маффинах с ветчиной | сцена: устроились на тарелке, укрывшись жёлтым соусом-голландез, как пледом")

# 5 Мираторг — картофельные дольки по-деревенски высовываются из бумажного кулька и машут укропом
I["cafe-miratorg-shcherbinka-domodedovo"] = (svg2("#F2F2F2", "#6B6F7A", f'''
<g {s()}>
<path d="M22 60 Q10 34 30 18 Q40 34 44 60Z" fill="#F2B544"/>
<path d="M48 60 Q46 26 66 12 Q74 34 70 60Z" fill="#E8A23A"/>
<path d="M76 60 Q84 30 106 22 Q106 44 94 62Z" fill="#F2B544"/>
</g>
<path d="M30 18 Q40 34 44 60 M66 12 Q74 34 70 60 M106 22 Q106 44 94 62" fill="none" stroke="#B5651D" stroke-width="4" stroke-linecap="round"/>
<g fill="#FFF3C4" opacity=".8"><circle cx="26" cy="40" r="1.6"/><circle cx="56" cy="34" r="1.6"/><circle cx="88" cy="40" r="1.6"/></g>
<path d="M104 24 Q110 16 114 8" fill="none" {W(2.4)}/>
<path d="M110 14 l6 -2 M112 10 l-4 -5 M114 6 l6 0 M107 18 l-5 -3" stroke="#3FA34D" stroke-width="2.4" stroke-linecap="round"/>
<path d="M18 56 H110 L74 122 H54Z" fill="#D9B48A" {s()}/>
<path d="M32 56 L60 120 M56 56 L64 120 M84 56 L68 120 M102 56 L72 118" stroke="#C49A6A" stroke-width="2"/>
<path d="M18 56 H110" {W(3.4)}/>
{face(64, 76, d=10, k=0.85)}
<circle cx="30" cy="44" r="1.6" fill="{O}"/><circle cx="36" cy="44" r="1.6" fill="{O}"/>
<circle cx="58" cy="40" r="1.6" fill="{O}"/><circle cx="64" cy="40" r="1.6" fill="{O}"/>
<circle cx="88" cy="44" r="1.6" fill="{O}"/><circle cx="94" cy="44" r="1.6" fill="{O}"/>
'''), "герой: три картофельные дольки по-деревенски с поджаристыми спинками | сцена: высовываются из бумажного кулька, крайняя машет веточкой укропа")

# 6 Аист — плюшка-сердечко выпрыгивает из корзинки, рассыпая сахар
I["cafe-aist-elektrostal"] = (svg2("#FFE9E0", "#E8704F", f'''
<path d="M20 92 H108 L100 122 H28Z" fill="#C4884A" {s()}/>
<path d="M24 102 H104 M26 112 H102" stroke="#9A6234" stroke-width="2.4"/>
<path d="M36 92 V122 M52 92 V122 M68 92 V122 M84 92 V122 M98 92 V118" stroke="#9A6234" stroke-width="2"/>
<path d="M20 92 Q40 80 50 92 Q64 82 78 92 Q90 82 108 92" fill="#6EA8E8" {W(2.4)}/>
<path d="M64 84 C40 66 30 46 44 34 C54 26 62 32 64 40 C66 32 74 26 84 34 C98 46 88 66 64 84Z" fill="#E8A23A" {s()}/>
<path d="M50 40 Q56 36 60 42 M70 42 Q76 36 80 40" fill="none" stroke="#C9802A" stroke-width="2"/>
<g fill="#FFFFFF">{''.join(f'<rect x="{x}" y="{y}" width="3" height="3" rx="1" transform="rotate(30 {x} {y})"/>' for x, y in [(52,50),(70,48),(60,60),(76,58),(46,56),(64,70),(56,44)])}</g>
{face(64, 54, d=9, k=0.75)}
<g fill="#FFFFFF">{''.join(f'<circle cx="{x}" cy="{y}" r="2"/>' for x, y in [(26,30),(102,26),(18,50),(110,48),(34,16),(92,12),(100,66),(22,68)])}</g>
<path d="M30 24 l0 -6 M98 18 l0 6" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
'''), "герой: пышная плюшка-сердечко в сахарной посыпке | сцена: выпрыгивает из плетёной корзинки с голубым полотенцем, рассыпая сахар как снежинки")

# 7 Дача гриль — жульен в кокотнице стоит на садовом пеньке у штакетника
I["cafe-dacha-grill-istra"] = (svg2("#F3FFE0", "#86B84A", f'''
<g fill="#FFFFFF" {W(2.4)}>{''.join(f'<path d="M{x} 74 V30 L{x+6} 22 L{x+12} 30 V74Z"/>' for x in range(-2, 130, 18))}</g>
<path d="M0 40 H128 M0 64 H128" stroke="#FFFFFF" stroke-width="6"/>
<path d="M0 40 H128 M0 64 H128" stroke="{O}" stroke-width="1" opacity=".3"/>
<path d="M0 84 Q64 72 128 84 V128 H0Z" fill="#5E9E3A"/>
<path d="M34 92 V118 Q64 126 94 118 V92Z" fill="#9A6234" {s()}/>
<ellipse cx="64" cy="92" rx="30" ry="9" fill="#E8C48A" {s()}/>
<ellipse cx="64" cy="92" rx="18" ry="5" fill="none" stroke="#C9A06A" stroke-width="2"/>
<ellipse cx="64" cy="92" rx="8" ry="2.4" fill="none" stroke="#C9A06A" stroke-width="2"/>
<path d="M42 86 L46 58 H82 L86 86 Q64 92 42 86Z" fill="#B8BDC8" {s()}/>
<path d="M84 66 L112 54" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M84 66 L112 54" stroke="#B8BDC8" stroke-width="3.4" stroke-linecap="round"/>
<path d="M44 60 Q46 40 64 40 Q82 40 84 60Z" fill="#E8B04A" {s()}/>
<g fill="#C9802A"><circle cx="54" cy="48" r="2.6"/><circle cx="74" cy="46" r="2"/><circle cx="66" cy="54" r="1.6"/></g>
{face(64, 68, d=9, k=0.75)}
'''), "герой: жульен в металлической кокотнице с длинной ручкой и запечённой сырной шапочкой | сцена: стоит на садовом пеньке у белого дачного штакетника")

# 8 Краббург — булочка краб-ролл шагает боком по песку, щёлкая клешнями из крабовых палочек
I["cafe-krabburg-istra"] = (svg2("#E6F9FF", "#2E9FD0", f'''
<path d="M0 62 Q32 56 64 62 Q96 68 128 62 V80 H0Z" fill="#7FD0F0"/>
<path d="M0 84 Q64 74 128 84 V128 H0Z" fill="#F5D99A"/>
<g fill="#E8C47A"><circle cx="20" cy="104" r="2"/><circle cx="104" cy="112" r="2"/><circle cx="36" cy="118" r="1.6"/></g>
<path d="M44 96 L36 110 M54 98 L50 114 M74 98 L78 114 M84 96 L92 110" stroke="#E8574A" stroke-width="4" stroke-linecap="round"/>
<path d="M30 74 Q20 70 14 56" fill="none" stroke="{O}" stroke-width="10" stroke-linecap="round"/>
<path d="M30 74 Q20 70 14 56" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>
<path d="M30 74 Q20 70 14 56" fill="none" stroke="#E8574A" stroke-width="3" stroke-linecap="round" transform="translate(1 -2)"/>
<path d="M98 74 Q108 70 114 56" fill="none" stroke="{O}" stroke-width="10" stroke-linecap="round"/>
<path d="M98 74 Q108 70 114 56" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>
<path d="M98 74 Q108 70 114 56" fill="none" stroke="#E8574A" stroke-width="3" stroke-linecap="round" transform="translate(-1 -2)"/>
<path d="M8 50 Q12 40 20 46 L14 54Z M120 50 Q116 40 108 46 L114 54Z" fill="#E8574A" {W(2.4)}/>
<path d="M24 82 Q22 56 64 54 Q106 56 104 82 Q104 100 64 100 Q24 100 24 82Z" fill="#E8B060" {s()}/>
<path d="M32 70 Q40 52 64 50 Q88 52 96 70 Q88 66 80 70 Q72 62 64 70 Q56 62 48 70 Q40 64 32 70Z" fill="#FF9AA8" {W(2.4)}/>
<path d="M44 60 L50 58 M60 56 L68 56 M78 58 L84 60" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"/>
{face(64, 82, d=10, k=0.8)}
'''), "герой: булочка краб-ролл с розовым крабовым мясом | сцена: шагает боком по пляжному песку, щёлкая клешнями из крабовых палочек")

# 9 Cyclo — миска супа фо едет в корзине вьетнамской велорикши
I["cafe-cyclo-kolomna"] = (svg2("#FFF9D6", "#E2B23A", f'''
<circle cx="36" cy="100" r="20" fill="none" {s()}/>
<circle cx="36" cy="100" r="16" fill="none" stroke="{O}" stroke-width="1.6"/>
<path d="M36 84 V116 M20 100 H52 M25 89 L47 111 M47 89 L25 111" stroke="{O}" stroke-width="1.4"/>
<circle cx="36" cy="100" r="3" fill="{O}"/>
<circle cx="104" cy="108" r="12" fill="none" {s()}/>
<circle cx="104" cy="108" r="2.4" fill="{O}"/>
<path d="M36 100 L104 108 M76 78 L104 108 M100 72 L104 108" {W(3)}/>
<path d="M94 70 H106" {W(4)}/>
<path d="M16 50 H70 V84 Q44 92 16 84Z" fill="#D8433A" {s()}/>
<path d="M16 60 H70" stroke="#A82E28" stroke-width="2"/>
<path d="M14 44 Q42 30 72 44" fill="#2E8B57" {s()}/>
<path d="M22 58 H64 Q62 78 43 80 Q24 78 22 58Z" fill="#FFFFFF" {s()}/>
<path d="M24 62 H62" stroke="#3E78C8" stroke-width="2.4"/>
<path d="M22 56 Q43 52 64 56" fill="#F2C46B" {W(2)}/>
<path d="M30 54 Q36 46 40 54 M46 54 Q50 46 56 54" fill="none" stroke="#F5E6C8" stroke-width="2.4"/>
<path d="M54 50 l8 -6 l2 6Z" fill="#4CAF50" {W(1.6)}/><circle cx="30" cy="52" r="4" fill="#B8E06A" {W(1.6)}/>
{face(43, 68, d=7, k=0.6)}
<path d="M34 40 Q30 32 36 26 M48 40 Q44 30 50 24" {STEAM}/>
'''), "герой: миска вьетнамского супа фо с базиликом и лаймом | сцена: едет под зелёным навесом в красной корзине вьетнамской велорикши")

# 10 Lounge Cafe Pastila — батончик нуги с орешками отдыхает на пуфике под торшером
I["cafe-pastila-lounge-kolomna"] = (svg2("#EFE6FF", "#7B5BC9", f'''
<path d="M104 112 V40" {W(3)}/>
<ellipse cx="104" cy="114" rx="10" ry="3" fill="{O}"/>
<path d="M88 40 L94 18 H114 L120 40Z" fill="#FFE07A" {s()}/>
<path d="M90 42 L60 100 H128 L120 42Z" fill="#FFF3B0" opacity=".35"/>
<ellipse cx="54" cy="104" rx="42" ry="12" fill="#9C6ADE" {s()}/>
<path d="M12 104 V88 Q12 74 54 74 Q96 74 96 88 V104" fill="#B48CF0" {s()}/>
<path d="M30 80 L34 96 M54 78 V98 M78 80 L74 96" stroke="#8E5ED8" stroke-width="2"/>
<g transform="rotate(-10 54 66)">
<rect x="20" y="52" width="68" height="28" rx="8" fill="#FFF8EC" {s()}/>
<g {W(1.6)}><ellipse cx="30" cy="60" rx="4" ry="3" fill="#C88A3E"/><ellipse cx="80" cy="72" rx="4" ry="3" fill="#C88A3E"/>
<ellipse cx="78" cy="58" rx="3" ry="4" fill="#7FC46A"/><ellipse cx="28" cy="74" rx="3" ry="4" fill="#7FC46A"/>
<ellipse cx="42" cy="74" rx="3" ry="2.4" fill="#E8574A"/><ellipse cx="68" cy="56" rx="3" ry="2.4" fill="#E8574A"/></g>
{sleepy(54, 64, d=8, k=0.8)}
<path d="M50 72 Q54 75 58 72" fill="none" {W(2)}/>
</g>
<text x="30" y="34" font-family="Arial" font-size="12" font-weight="bold" fill="#fff">z</text>
<text x="40" y="24" font-family="Arial" font-size="9" font-weight="bold" fill="#fff">z</text>
'''), "герой: батончик белой нуги с орешками и цукатами | сцена: дремлет, развалившись на мягком сиреневом пуфике под торшером")

# 11 ВИВА Пицца — мини-пиццетта с глазками-оливками делает колесо на лужайке
I["cafe-viva-pizza-kolomna"] = (svg2("#E7F0FF", "#7F8FE8", f'''
<path d="M0 98 Q64 86 128 98 V128 H0Z" fill="#7CC46A"/>
<path d="M14 100 l3 -6 l3 6 M100 96 l3 -6 l3 6 M60 94 l2 -5 l2 5" fill="none" stroke="#4E9A3E" stroke-width="2"/>
<path d="M20 66 Q18 40 40 26 M108 66 Q110 40 88 26" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="2 7" stroke-linecap="round"/>
<g transform="rotate(-28 64 60)">
<path d="M46 84 L38 100 M82 84 L90 100" {W(5)}/>
<circle cx="38" cy="101" r="4" fill="{O}"/><circle cx="90" cy="101" r="4" fill="{O}"/>
<circle cx="64" cy="56" r="32" fill="#E8A84A" {s()}/>
<circle cx="64" cy="56" r="25" fill="#E8483A" {W(2)}/>
<path d="M44 46 Q52 38 60 46 Q66 52 74 44 Q82 40 86 52 Q84 66 74 70 Q64 74 54 70 Q42 64 44 46Z" fill="#FFE8A0"/>
<g fill="#4CAF50"><path d="M48 66 l5 -3 l-1 6Z"/><path d="M80 58 l5 -3 l-1 6Z"/></g>
<circle cx="54" cy="52" r="5.4" fill="#2B2B2B" {W(1.6)}/><circle cx="74" cy="52" r="5.4" fill="#2B2B2B" {W(1.6)}/>
<circle cx="53" cy="50" r="1.8" fill="#fff"/><circle cx="73" cy="50" r="1.8" fill="#fff"/>
<path d="M58 62 Q64 68 70 62" fill="none" {W(2.4)}/>
<ellipse cx="46" cy="60" rx="3.6" ry="2" fill="#FF7FA8" opacity=".7"/><ellipse cx="82" cy="60" rx="3.6" ry="2" fill="#FF7FA8" opacity=".7"/>
</g>
'''), "герой: мини-пиццетта с глазками из чёрных оливок | сцена: весело делает колесо на зелёной лужайке")

# 12 Цукини — фаршированная лодочка из кабачка плывёт по томатному соусу под парусом-петрушкой
I["cafe-tsukini-korolev"] = (svg2("#FFF4EC", "#F2A08A", f'''
<path d="M0 90 Q20 82 40 90 Q60 98 80 90 Q100 82 128 90 V128 H0Z" fill="#D9483B" {s()}/>
<path d="M10 104 Q20 100 30 104 M76 110 Q86 106 96 110" fill="none" stroke="#F2847A" stroke-width="2.4" stroke-linecap="round"/>
<path d="M66 56 V20" {W(3)}/>
<path d="M66 22 Q88 24 92 38 Q84 48 68 50Z" fill="#4CAF50" {s()}/>
<path d="M68 28 Q78 34 86 38 M70 40 L80 42" fill="none" stroke="#2E7D32" stroke-width="1.8"/>
<path d="M14 64 Q16 96 64 98 Q112 96 114 64Z" fill="#3E8E3A" {s()}/>
<path d="M18 66 Q22 88 64 90 Q106 88 110 66" fill="none" stroke="#9BD27A" stroke-width="3"/>
<path d="M16 64 Q20 50 40 54 Q52 46 64 54 Q78 46 90 54 Q108 50 112 64Z" fill="#A0522D" {s()}/>
<path d="M30 58 Q40 52 50 58 Q62 52 74 58 Q86 52 98 58" fill="none" stroke="#FFE07A" stroke-width="4" stroke-linecap="round"/>
{face(64, 76, d=12, k=0.85)}
'''), "герой: лодочка из кабачка, фаршированная мясом под сырной корочкой | сцена: плывёт по морю из томатного соуса под парусом-листиком петрушки")

# 13 Glow — ириска-тянучка светится в темноте, как ночник
I["cafe-glow-korolev"] = (svg2("#5A4FA0", "#1E1846", f'''
<circle cx="64" cy="66" r="50" fill="#FFE9A8" opacity=".14"/>
<circle cx="64" cy="66" r="40" fill="#FFE9A8" opacity=".2"/>
<circle cx="64" cy="66" r="31" fill="#FFE9A8" opacity=".28"/>
{sparkle(22, 30, 6)}{sparkle(104, 24, 5)}{sparkle(110, 92, 6)}{sparkle(18, 96, 4)}{sparkle(92, 112, 3)}
<rect x="36" y="40" width="56" height="52" rx="16" fill="#D08A3A" {s()}/>
<path d="M44 48 Q50 44 58 46" fill="none" stroke="#F5C27A" stroke-width="4" stroke-linecap="round"/>
<path d="M40 82 Q64 90 88 82" fill="none" stroke="#B06E28" stroke-width="2.4"/>
{face(64, 64, d=10, k=0.85)}
'''), "герой: квадратная сливочная ириска-тянучка | сцена: тёплым светом светится в тёмной комнате, как ночник, среди искорок")

# 14 Royal Green Park — кусок торта «Наполеон» гуляет по зелёной аллее мимо фонаря
I["cafe-royal-green-park-korolev"] = (svg2("#E9FFE9", "#3E9A57", f'''
<path d="M44 128 L58 70 H70 L84 128Z" fill="#E8D8B0"/>
<circle cx="16" cy="70" r="20" fill="#2E7D32" {s()}/><circle cx="112" cy="70" r="20" fill="#2E7D32" {s()}/>
<circle cx="30" cy="54" r="14" fill="#43A047" {s()}/><circle cx="98" cy="54" r="14" fill="#43A047" {s()}/>
<path d="M108 120 V36" {W(3)}/>
<path d="M100 36 H116 L112 26 H104Z" fill="#FFE07A" {W(2.4)}/>
<path d="M52 108 L48 122 M76 108 L80 122" {W(4)}/>
<path d="M42 122 H52 M76 122 H86" {W(4)}/>
<rect x="36" y="56" width="56" height="52" rx="4" fill="#F5E6C8" {s()}/>
<path d="M38 70 H90 M38 84 H90 M38 98 H90" stroke="#D9A55E" stroke-width="5"/>
<path d="M36 56 Q40 50 46 54 Q52 48 58 54 Q64 48 70 54 Q76 48 82 54 Q88 50 92 56Z" fill="#E8C48A" {W(2)}/>
<g fill="#C9802A"><circle cx="46" cy="58" r="1.4"/><circle cx="60" cy="57" r="1.4"/><circle cx="74" cy="58" r="1.4"/><circle cx="86" cy="57" r="1.4"/></g>
{face(64, 76, d=10, k=0.8)}
'''), "герой: прямоугольный кусок торта «Наполеон» с хрустящей крошкой | сцена: гуляет по аллее зелёного парка мимо старинного фонаря")

# 15 Пронто Мытищи — чиабатта-сэндвич с полосками гриля мчится на самокате
I["cafe-pronto-mytishchi"] = (svg2("#FFF7CC", "#F5B700", f'''
<path d="M6 46 H24 M2 60 H20 M8 74 H26" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
<path d="M30 104 H96 L102 96" fill="none" {W(5)}/>
<path d="M96 104 L104 30 M96 30 H112" fill="none" {W(4)}/>
<circle cx="36" cy="108" r="9" fill="#5B6BD8" {s()}/><circle cx="96" cy="108" r="9" fill="#5B6BD8" {s()}/>
<circle cx="36" cy="108" r="2.4" fill="#fff"/><circle cx="96" cy="108" r="2.4" fill="#fff"/>
<path d="M54 92 L50 104 M74 92 L76 104" {W(4)}/>
<path d="M84 60 Q94 48 100 36" fill="none" {W(4)}/>
<path d="M26 74 Q28 46 62 44 Q96 46 96 74 Q94 94 62 94 Q28 94 26 74Z" fill="#E8C07A" {s()}/>
<path d="M28 72 Q62 80 94 72" fill="none" stroke="#7FC46A" stroke-width="5"/>
<path d="M30 76 Q62 84 92 76" fill="none" stroke="#E8574A" stroke-width="3"/>
<path d="M40 52 L48 64 M56 48 L64 62 M72 48 L80 62" stroke="#9A6234" stroke-width="3.4" stroke-linecap="round"/>
<g fill="#F5E6C8"><circle cx="36" cy="60" r="1.4"/><circle cx="86" cy="58" r="1.4"/></g>
{face(62, 64, d=9, k=0.7)}
'''), "герой: чиабатта-сэндвич с полосками гриля и листом салата | сцена: мчится на синем самокате, оставляя за собой ветер")

# 16 Кегли — сырный шарик в панировке сбивает кегли-сосиски
I["cafe-kegli-kievsky"] = (svg2("#F0F4FF", "#3A4F9C", f'''
<path d="M0 92 H128 V128 H0Z" fill="#E8C48A" {s()}/>
<path d="M0 104 H128 M0 116 H128" stroke="#C9A06A" stroke-width="1.6"/>
<g {s()}>
<rect x="86" y="44" width="14" height="48" rx="7" fill="#F28B7A"/>
<rect x="106" y="34" width="14" height="44" rx="7" fill="#F28B7A" transform="rotate(50 113 56)"/>
<rect x="74" y="0" width="14" height="40" rx="7" fill="#F28B7A" transform="rotate(-60 81 20)"/>
</g>
<path d="M86 56 H100 M86 80 H100" stroke="#D9605A" stroke-width="2"/>
<path d="M86 14 l-2 -8 M104 16 l6 -6 M118 30 l8 -2 M62 10 l-6 -4" stroke="#FFE07A" stroke-width="3" stroke-linecap="round"/>
<circle cx="40" cy="70" r="24" fill="#F2B544" {s()}/>
<g fill="#C9802A">{''.join(f'<circle cx="{x}" cy="{y}" r="1.6"/>' for x, y in [(26,60),(34,52),(48,54),(56,64),(52,82),(28,80),(40,88),(22,70)])}</g>
{face(40, 68, d=8, k=0.8)}
<path d="M4 58 H12 M2 72 H10 M6 84 H14" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
'''), "герой: сырный шарик в золотистой панировке | сцена: катится по дорожке боулинга и делает страйк, раскидывая кегли-сосиски")

# 17 Мохито — острый суп том-ям с креветкой пыхтит паром, высунув язычок
I["cafe-mohito-noginsk"] = (svg2("#E9FFF2", "#22A06B", f'''
<path d="M14 70 H114 Q110 112 64 114 Q18 112 14 70Z" fill="#FFFFFF" {s()}/>
<path d="M18 84 Q64 92 110 84" fill="none" stroke="#2E8B57" stroke-width="3"/>
<path d="M20 98 L26 92 L32 98 L38 92 L44 98 M84 98 L90 92 L96 98 L102 92 L108 98" fill="none" stroke="#2E8B57" stroke-width="2"/>
<ellipse cx="64" cy="70" rx="50" ry="12" fill="#F26A2A" {s()}/>
<path d="M28 66 Q30 58 40 60 Q36 64 38 70" fill="#FF9AA8" {W(2.2)}/>
<circle cx="92" cy="66" r="7" fill="#D9F27A" {W(2)}/><path d="M92 59 V73 M85 66 H99" stroke="#9BC23A" stroke-width="1.4"/>
<path d="M50 64 l6 -2 M66 74 l6 -1" stroke="#4CAF50" stroke-width="3" stroke-linecap="round"/>
<path d="M44 58 Q40 30 64 28 Q88 30 84 58Z" fill="#F26A2A" opacity="0"/>
{eye(54, 46, 0.9)}{eye(74, 46, 0.9)}
<ellipse cx="46" cy="54" rx="4" ry="2.4" fill="#FF5A5A" opacity=".8"/><ellipse cx="82" cy="54" rx="4" ry="2.4" fill="#FF5A5A" opacity=".8"/>
<path d="M58 54 Q64 58 70 54" fill="none" {W(2.4)}/>
<path d="M61 56 Q60 66 64 66 Q68 66 67 56Z" fill="#FF6B7A" {W(2)}/>
<path d="M34 34 Q30 26 36 18 M96 34 Q100 24 94 16 M50 30 Q46 20 52 12 M80 28 Q84 20 78 12" {STEAM}/>
'''), "герой: острый тайский суп том-ям с креветкой и лаймом | сцена: пыхтит паром из пиалы и высунул язычок от остроты")

# 18 ПиццаФабрика — сицилийская пицца выезжает из ворот фабрики по конвейеру
I["cafe-pizzafabrika-noginsk"] = (svg2("#FFE8D6", "#B5562B", f'''
<rect x="-4" y="22" width="44" height="80" fill="#C2603A" {s()}/>
<path d="M-4 40 H40 M-4 58 H40 M-4 76 H40 M18 22 V40 M8 40 V58 M28 40 V58 M18 58 V76" stroke="#9A4A2A" stroke-width="2"/>
<rect x="18" y="4" width="12" height="20" fill="#9A4A2A" {s()}/>
<path d="M22 2 Q18 -4 24 -8" fill="none" stroke="#fff" stroke-width="3"/>
<path d="M6 102 V64 Q6 54 20 54 Q34 54 34 64 V102Z" fill="#3B3355"/>
<rect x="10" y="98" width="118" height="10" rx="5" fill="#8A8FA0" {s()}/>
<g fill="#5A5F70">{''.join(f'<circle cx="{x}" cy="113" r="5"/>' for x in range(22, 128, 18))}</g>
<g transform="rotate(-6 76 80)">
<rect x="40" y="62" width="76" height="34" rx="6" fill="#E8A84A" {s()}/>
<rect x="46" y="66" width="64" height="26" rx="3" fill="#E8483A"/>
<path d="M48 72 Q56 68 62 74 Q72 66 82 74 Q92 68 104 74 V88 Q92 84 82 90 Q70 84 60 90 Q52 86 48 88Z" fill="#FFE8A0"/>
<g fill="#4CAF50"><path d="M54 80 l5 -3 l0 6Z"/><path d="M98 82 l5 -3 l0 6Z"/></g>
{face(78, 78, d=10, k=0.75)}
</g>
'''), "герой: прямоугольная сицилийская пицца на толстом тесте | сцена: выезжает по ленте конвейера из кирпичных ворот пиццерии-фабрики")

# 19 Лазика — чахохбили в глиняной кеци плывёт по волнам Чёрного моря
I["cafe-lazika-kaluzhskoe"] = (svg2("#E0F4FF", "#1F6FB2", f'''
<path d="M0 30 Q20 18 40 28 L60 22 L80 30 Q100 20 128 30 V46 H0Z" fill="#8FC9A8" opacity=".7"/>
<path d="M0 84 Q16 76 32 84 Q48 92 64 84 Q80 76 96 84 Q112 92 128 84 V128 H0Z" fill="#1A5A96" {s()}/>
<path d="M8 100 Q16 96 24 100 M60 106 Q68 102 76 106 M100 98 Q108 94 116 98" fill="none" stroke="#7FB8F0" stroke-width="2.4" stroke-linecap="round"/>
<path d="M18 70 Q20 94 64 96 Q108 94 110 70Z" fill="#9A4A2A" {s()}/>
<path d="M22 76 Q26 90 64 92 Q102 90 106 76" fill="none" stroke="#C2703A" stroke-width="2.4"/>
<path d="M10 70 H18 M110 70 H118" {W(5)}/>
<ellipse cx="64" cy="70" rx="46" ry="10" fill="#C8382E" {s()}/>
<path d="M78 64 Q86 52 98 56 Q102 62 94 66 Z" fill="#C8782E" {W(2.2)}/>
<path d="M96 56 l6 -4 M98 60 l6 0" stroke="#F5E6C8" stroke-width="3" stroke-linecap="round"/>
<g fill="#4CAF50"><path d="M36 66 l6 -3 l-1 6Z"/><path d="M54 74 l6 -3 l-1 6Z"/><path d="M70 66 l5 -3 l0 6Z"/></g>
{face(52, 82, d=10, k=0.75)}
<path d="M84 22 q6 -6 12 0 q6 -6 12 0" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
'''), "герой: чахохбили — курица в томатном соусе в глиняной сковородке-кеци | сцена: плывёт, как плот, по волнам Чёрного моря вдоль зелёного берега")

# 20 Просто бистро — френч-тост с ягодами делает утреннюю зарядку-приседания
I["cafe-prosto-bistro-shcherbinka"] = (svg2("#FFFBEF", "#F2C46B", f'''
<ellipse cx="64" cy="112" rx="48" ry="9" fill="#FFFFFF" {s()}/>
<path d="M44 96 L36 104 L42 112 M84 96 L92 104 L86 112" fill="none" {W(4.4)}/>
<path d="M34 64 L14 60 M94 64 L114 60" {W(4.4)}/>
<circle cx="12" cy="60" r="4" fill="#F5E6C8" {W(2)}/><circle cx="116" cy="60" r="4" fill="#F5E6C8" {W(2)}/>
<path d="M30 44 Q30 24 48 26 Q56 18 64 22 Q72 18 80 26 Q98 24 98 44 V96 H30Z" fill="#B8702A" {s()}/>
<path d="M36 46 Q36 32 50 32 Q58 26 64 30 Q70 26 78 32 Q92 32 92 46 V90 H36Z" fill="#F2C46B"/>
<g {W(1.8)}><circle cx="48" cy="22" r="5" fill="#C8243A"/><circle cx="60" cy="16" r="5" fill="#3A4FB0"/><circle cx="72" cy="18" r="5" fill="#C8243A"/><circle cx="84" cy="24" r="4" fill="#3A4FB0"/></g>
<path d="M40 30 Q64 36 90 30" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" opacity=".9"/>
{face(64, 62, d=10, k=0.85)}
<path d="M100 36 Q104 42 100 46 Q96 42 100 36Z" fill="#7FC8F8" {W(1.6)}/>
<path d="M18 88 Q12 82 18 76 M110 88 Q116 82 110 76" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
'''), "герой: толстый френч-тост с малиной и черникой | сцена: делает утреннюю зарядку — приседает на тарелке, вытянув ручки вперёд")

# 21 Золотой Снитч — шоколадная конфета в золотой фольге с крылышками порхает в облаках
I["cafe-zolotoy-snitch-podolsk"] = (svg2("#FFE3E3", "#B22234", f'''
<ellipse cx="22" cy="104" rx="22" ry="10" fill="#FFFFFF" opacity=".9"/><ellipse cx="40" cy="100" rx="14" ry="9" fill="#FFFFFF" opacity=".9"/>
<ellipse cx="104" cy="110" rx="24" ry="10" fill="#FFFFFF" opacity=".9"/><ellipse cx="90" cy="104" rx="12" ry="8" fill="#FFFFFF" opacity=".9"/>
<path d="M38 60 Q12 36 6 50 Q4 58 14 60 Q4 64 10 72 Q18 76 38 68Z" fill="#FFFFFF" {s()}/>
<path d="M90 60 Q116 36 122 50 Q124 58 114 60 Q124 64 118 72 Q110 76 90 68Z" fill="#FFFFFF" {s()}/>
<path d="M14 54 Q24 58 34 62 M18 66 Q26 66 34 66 M114 54 Q104 58 94 62 M110 66 Q102 66 94 66" fill="none" stroke="#C9C9D9" stroke-width="1.6"/>
<circle cx="64" cy="64" r="28" fill="#F5C23A" {s()}/>
<path d="M44 50 L52 56 L46 64 L54 70 L48 80 M84 50 L76 56 L82 64 L74 70 L80 80 M60 38 L64 46 L68 38" fill="none" stroke="#C9922A" stroke-width="1.8"/>
<path d="M48 48 Q54 42 62 42" fill="none" stroke="#FFF2B0" stroke-width="4" stroke-linecap="round"/>
{face(64, 64, d=9, k=0.8)}
{sparkle(28, 26, 6, "#FFE07A")}{sparkle(100, 22, 5, "#FFE07A")}{sparkle(112, 86, 4, "#FFE07A")}
'''), "герой: шоколадная конфета в золотой фольге с белыми крылышками | сцена: порхает над облаками, рассыпая золотые искорки")

# 22 ТиАмо — мороженое-сэндвич признаётся в любви с розочкой
I["cafe-tiamo-pushkino"] = (svg2("#FFE6F2", "#F06AA8", f'''
<g transform="rotate(-8 60 70)">
<rect x="22" y="40" width="76" height="20" rx="6" fill="#5A3420" {s()}/>
<rect x="24" y="58" width="72" height="22" fill="#FFF8EC" {s()}/>
<rect x="22" y="78" width="76" height="20" rx="6" fill="#5A3420" {s()}/>
<g fill="#3A2010">{''.join(f'<circle cx="{x}" cy="{y}" r="1.8"/>' for x, y in [(32,46),(46,52),(60,46),(74,52),(88,46),(32,88),(46,92),(60,86),(74,92),(88,86)])}</g>
{face(60, 66, d=10, k=0.75)}
</g>
<path d="M96 70 L110 40" stroke="#2E8B57" stroke-width="3.4" stroke-linecap="round"/>
<path d="M102 56 q8 -2 8 6 q-8 0 -8 -6Z" fill="#4CAF50" {W(1.6)}/>
<path d="M98 72 Q92 68 96 64" fill="none" {W(3)}/>
<circle cx="110" cy="36" r="9" fill="#E8243A" {s()}/>
<path d="M104 36 Q110 30 116 36 M106 40 Q110 44 114 40" fill="none" stroke="#A8142A" stroke-width="1.8"/>
'''), "герой: мороженое-сэндвич между двумя шоколадными печеньями | сцена: смущённо протягивает алую розочку на длинном стебле")

# 23 Burger Club — картофель-спиралька на шпажке крутится юлой
I["cafe-burger-club-ramenskoe"] = (svg2("#E3F8FF", "#00A3C4", f'''
<ellipse cx="64" cy="116" rx="26" ry="5" fill="#007A94" opacity=".5"/>
<path d="M64 116 V14" {W(3.4)}/>
<path d="M64 116 V14" stroke="#F5E6C8" stroke-width="1.6"/>
<g {W(2.6)}>
<ellipse cx="64" cy="100" rx="10" ry="4" fill="#F2B544"/>
<ellipse cx="64" cy="90" rx="18" ry="6" fill="#E8A23A"/>
<ellipse cx="64" cy="78" rx="26" ry="7" fill="#F2B544"/>
<ellipse cx="64" cy="64" rx="32" ry="8" fill="#E8A23A"/>
<ellipse cx="64" cy="50" rx="28" ry="7" fill="#F2B544"/>
<ellipse cx="64" cy="37" rx="20" ry="6" fill="#E8A23A"/>
<ellipse cx="64" cy="26" rx="10" ry="4" fill="#F2B544"/>
</g>
<g fill="#E8483A"><circle cx="44" cy="62" r="1.4"/><circle cx="84" cy="66" r="1.4"/><circle cx="56" cy="48" r="1.2"/></g>
{face(64, 62, d=10, k=0.7)}
<path d="M18 50 Q10 64 18 78 M110 50 Q118 64 110 78 M26 36 Q20 44 22 52 M102 36 Q108 44 106 52" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
'''), "герой: картофель-спиралька на деревянной шпажке | сцена: крутится юлой на одной ножке, разбрасывая ветерок")

# 24 Еда на связи — буррито болтает по телефону из стаканчиков с ниткой-спагеттиной
I["cafe-eda-na-svyazi-ramenskoe"] = (svg2("#F6E9FF", "#9B51C9", f'''
<path d="M50 50 Q80 20 104 28" fill="none" stroke="#FFD93A" stroke-width="3" stroke-linecap="round"/>
<path d="M96 18 L114 22 L110 40 L94 36Z" fill="#FFFFFF" {s()}/>
<path d="M96 22 L112 26" stroke="#E8574A" stroke-width="3"/>
<g transform="rotate(12 64 80)"><path d="M30 70 Q28 40 64 38 Q100 40 98 70 L94 112 Q64 120 34 112Z" fill="#F2DDB0" {s()}/>
<path d="M34 80 L94 80 L92 112 Q64 120 36 112Z" fill="#C9CCD6" {s()}/>
<path d="M40 90 L48 104 M58 88 L64 108 M76 90 L72 106 M88 88 L82 104" stroke="#A8ACB8" stroke-width="2"/>
<path d="M36 52 Q48 44 56 50 Q66 42 76 50 Q86 44 94 52" fill="none" stroke="#7FC46A" stroke-width="4" stroke-linecap="round"/>
<path d="M40 58 Q52 54 60 58 Q72 54 88 58" fill="none" stroke="#E8574A" stroke-width="3" stroke-linecap="round"/>
<path d="M30 70 Q22 62 30 54" fill="none" {W(4)}/>
<path d="M30 46 L46 44 L48 60 L32 62Z" fill="#FFFFFF" {s()}/>
<path d="M32 50 L46 48" stroke="#E8574A" stroke-width="3"/>
{face(66, 66, d=10, k=0.8)}</g>
'''), "герой: буррито в серебристой фольге | сцена: болтает по самодельному телефону из бумажных стаканчиков, соединённых спагеттиной")

# 25 Эгомания — пышный баурсак любуется собой в зеркальце
I["cafe-egomania-reutov"] = (svg2("#E9F5EC", "#5B8C6E", f'''
<path d="M30 92 Q22 60 50 54 Q56 38 76 44 Q100 46 100 74 Q104 98 72 104 Q38 108 30 92Z" fill="#E8A84A" {s()}/>
<path d="M44 60 Q50 56 56 60 M80 54 Q86 54 90 60" fill="none" stroke="#F5D08A" stroke-width="3" stroke-linecap="round"/>
<g fill="#FFFFFF">{''.join(f'<circle cx="{x}" cy="{y}" r="1.6"/>' for x, y in [(46,72),(62,62),(84,70),(70,92),(50,94),(90,88),(58,80)])}</g>
{eye(58, 78, 0.8)}{eye(76, 78, 0.8)}
<ellipse cx="50" cy="86" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/><ellipse cx="84" cy="86" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/>
<path d="M62 88 Q67 93 72 88" fill="none" {W(2.4)}/>
<path d="M96 70 L108 60" {W(4)}/>
<path d="M104 64 L116 46" stroke="#C9922A" stroke-width="6" stroke-linecap="round"/>
<ellipse cx="108" cy="32" rx="14" ry="18" fill="#F5C23A" {s()}/>
<ellipse cx="108" cy="32" rx="10" ry="14" fill="#CFEFFF" {W(2)}/>
<path d="M102 24 L106 20 M102 32 L110 24" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
{sparkle(24, 34, 7)}{sparkle(40, 20, 4)}
'''), "герой: пышный баурсак в сахарной пудре | сцена: держит золотое ручное зеркальце и с восторгом любуется собой")

# 26 Добрынинский — блинный торт со сметанными слоями на хохломском подносе
I["cafe-dobryninsky-reutov"] = (svg2("#FFEFC2", "#3A2F2A", f'''
<ellipse cx="64" cy="104" rx="56" ry="16" fill="#1E1A18" {s()}/>
<path d="M20 104 Q30 94 42 100 Q36 108 26 108 M108 104 Q98 94 86 100 Q92 108 102 108" fill="#D8332A"/>
<path d="M50 112 Q56 106 64 110 Q72 106 78 112" fill="none" stroke="#F2C23A" stroke-width="2.4"/>
<path d="M30 100 q-4 -6 2 -8 M98 100 q4 -6 -2 -8" fill="none" stroke="#F2C23A" stroke-width="2"/>
<g {s()}>
<ellipse cx="64" cy="94" rx="36" ry="9" fill="#E8B060"/>
<rect x="28" y="40" width="72" height="54" fill="#E8B060" stroke="none"/>
</g>
<path d="M28 40 V94 M100 40 V94" {s()}/>
<path d="M28 52 Q64 60 100 52 M28 64 Q64 72 100 64 M28 76 Q64 84 100 76 M28 88 Q64 96 100 88" fill="none" stroke="#FFF8EC" stroke-width="4"/>
<path d="M28 52 Q64 60 100 52 M28 64 Q64 72 100 64 M28 76 Q64 84 100 76 M28 88 Q64 96 100 88" fill="none" stroke="#C88A3E" stroke-width="1" opacity=".5"/>
<ellipse cx="64" cy="40" rx="36" ry="9" fill="#FFF8EC" {s()}/>
<circle cx="56" cy="36" r="4" fill="#C8243A" {W(1.8)}/><circle cx="66" cy="34" r="4" fill="#C8243A" {W(1.8)}/><circle cx="74" cy="38" r="3.4" fill="#3A4FB0" {W(1.6)}/>
{face(64, 70, d=11, k=0.85)}
'''), "герой: высокий блинный торт со сметанными прослойками и ягодами сверху | сцена: красуется на чёрно-золотом хохломском подносе с алыми завитками")

# 27 Монтана — рёбрышки барбекю греются у костра в каньоне под звёздами
I["cafe-montana-sergiev"] = (svg2("#FFB86B", "#7A2E1F", f'''
<path d="M0 60 H20 V44 H44 V60 H60 V128 H0Z" fill="#B5502E" opacity=".8"/>
<path d="M84 128 V54 H100 V40 H122 V56 H128 V128Z" fill="#9A3E24" opacity=".8"/>
{sparkle(70, 18, 4)}{sparkle(30, 28, 3)}{sparkle(104, 24, 3)}
<path d="M0 104 Q64 96 128 104 V128 H0Z" fill="#6E3A1E"/>
<path d="M78 112 L106 100 M80 100 L106 112" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M78 112 L106 100 M80 100 L106 112" stroke="#8A5A33" stroke-width="4" stroke-linecap="round"/>
<path d="M92 104 Q80 92 88 80 Q90 88 94 86 Q92 76 100 70 Q100 82 106 88 Q108 98 92 104Z" fill="#FF8A2A" {W(2.4)}/>
<path d="M94 100 Q90 94 94 88 Q98 94 100 92 Q100 98 94 100Z" fill="#FFE07A"/>
<path d="M14 90 Q12 66 40 62 L72 60 Q80 62 78 74 Q76 94 46 96 Q16 98 14 90Z" fill="#8A3E1E" {s()}/>
<g {W(2.4)} fill="#FFF8EC"><rect x="20" y="54" width="6" height="12" rx="3"/><rect x="34" y="52" width="6" height="12" rx="3"/><rect x="48" y="52" width="6" height="12" rx="3"/><rect x="62" y="52" width="6" height="12" rx="3"/></g>
<path d="M24 70 Q22 84 26 92 M38 68 V92 M52 68 V92 M66 66 Q68 80 66 90" stroke="#5A2810" stroke-width="2.4" fill="none"/>
<path d="M20 74 Q40 70 74 70" fill="none" stroke="#C8603A" stroke-width="3" stroke-linecap="round" opacity=".8"/>
{face(46, 80, d=10, k=0.75)}
'''), "герой: глазированные рёбрышки барбекю с белыми косточками | сцена: греются у костра на дне красного каньона под первыми звёздами")

# 28 Рестобар Лофтъ — связка сушек висит на гвоздике у кирпичной стены рядом с лампочкой Эдисона
I["cafe-loft-sergiev"] = (svg2("#D9785A", "#8E3A26", f'''
<g fill="#B85A3E" stroke="#7A3424" stroke-width="1.4">{''.join(f'<rect x="{x + (14 if (y // 16) % 2 else 0)}" y="{y}" width="26" height="14" rx="1.5"/>' for y in range(0, 128, 16) for x in range(-14, 128, 28))}</g>
<path d="M100 0 V28" {W(2)}/>
<circle cx="100" cy="40" r="22" fill="#FFE9A8" opacity=".35"/>
<path d="M94 28 H106 V34 Q112 40 110 48 Q106 56 100 56 Q94 56 90 48 Q88 40 94 34Z" fill="#FFE07A" {W(2.4)}/>
<path d="M96 36 Q100 46 104 36" fill="none" stroke="#E89A2A" stroke-width="1.6"/>
<circle cx="46" cy="16" r="4" fill="#8A8FA0" {W(2)}/>
<path d="M46 16 Q30 50 32 70 M46 16 Q62 50 60 70" fill="none" stroke="#F5E6C8" stroke-width="2.4"/>
<g {s()}>
<circle cx="34" cy="74" r="13" fill="#E8B060"/><circle cx="58" cy="74" r="13" fill="#E8B060"/>
<circle cx="46" cy="96" r="18" fill="#E8B060"/>
<circle cx="34" cy="50" r="10" fill="#E8B060"/><circle cx="58" cy="50" r="10" fill="#E8B060"/>
</g>
<g fill="#B85A3E" {W(2)}><circle cx="34" cy="74" r="4"/><circle cx="58" cy="74" r="4"/><circle cx="34" cy="50" r="3"/><circle cx="58" cy="50" r="3"/></g>
<circle cx="46" cy="106" r="4" fill="#B85A3E" {W(2)}/>
{face(46, 92, d=8, k=0.7)}
'''), "герой: связка румяных сушек на бечёвке | сцена: висит на гвоздике у кирпичной стены лофта, рядом светит лампочка Эдисона")

# 29 Мясницкий ряд — пирог-перемяч сидит на прилавке мясной лавки рядом с весами
I["cafe-myasnitsky-ryad-zelenograd"] = (svg2("#F7EDE2", "#6E4B3A", f'''
<path d="M0 22 H128" stroke="#8C3B3B" stroke-width="10"/>
<path d="M0 22 H128" stroke="#fff" stroke-width="10" stroke-dasharray="12 12"/>
<rect x="-2" y="92" width="132" height="40" fill="#8A5A33" {s()}/>
<path d="M-2 102 H130" stroke="#6E4224" stroke-width="2"/>
<path d="M88 92 V62 M76 62 H112" {W(3.4)}/>
<path d="M72 62 L68 72 H84 L80 62 M108 62 L104 72 H120 L116 62" fill="none" {W(2)}/>
<path d="M66 72 Q76 80 86 72Z M102 72 Q112 80 122 72Z" fill="#C9CCD6" {W(2)}/>
<path d="M82 92 H94 V86 H82Z" fill="#C9CCD6" {W(2)}/>
<ellipse cx="48" cy="88" rx="38" ry="8" fill="#6E4224" opacity=".4"/>
<ellipse cx="46" cy="72" rx="36" ry="20" fill="#E8A84A" {s()}/>
<ellipse cx="46" cy="64" rx="9" ry="5" fill="#8A3E1E" {W(2.4)}/>
<path d="M18 70 Q24 62 32 64 M60 62 Q68 62 74 70" fill="none" stroke="#F5D08A" stroke-width="3" stroke-linecap="round"/>
{face(46, 78, d=11, k=0.8)}
'''), "герой: круглый пирог-перемяч с дырочкой и мясной начинкой | сцена: сидит на деревянном прилавке мясной лавки рядом со старинными весами")


if __name__ == "__main__":
    reg = os.path.join(ROOT, "icons-src", "subjects.txt")
    lines = open(reg, encoding="utf-8").read().splitlines()
    lines = [l for l in lines if l.split(" — ", 1)[0] not in I]
    for pid, (svg_, subj) in I.items():
        open(os.path.join(ROOT, "icons-src", pid + ".svg"), "w").write(svg_)
        lines.append(f"{pid} — {subj}")
    open(reg, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("иконок:", len(I))
