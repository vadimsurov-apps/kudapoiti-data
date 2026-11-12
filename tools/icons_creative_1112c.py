"""Иконки робота creative, 12.11 (запуск 1112c). Каждая придумана и нарисована отдельно: свой герой, своя сцена,
своя компоновка и свой фон (правило абсолютной уникальности). python3 tools/icons_creative_1112c.py [--subjects]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_creative_1112k import bg, ln, limb, note, head, SKIN

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
I = {}

# 1 «Космическое тело» (классическая хореография 5–13): балерина в арабеске на полумесяце в космосе
I["kosmicheskoe-telo-zemlyanoy-val"] = ("девочка-балерина в тёмно-синем купальнике и пачке в золотых звёздочках",
    "делает арабеск на носочке, стоя на улыбающемся жёлтом полумесяце в открытом космосе", bg("#5B4FB8", "#1A1446", f'''
{sparkle(18, 30, 3)}{sparkle(108, 22, 4)}{sparkle(24, 84, 2.5)}{sparkle(112, 70, 3)}{sparkle(92, 40, 2)}
<path d="M30 92 Q46 128 92 116 Q60 116 52 92 Q48 80 54 70 Q34 74 30 92Z" fill="#FFD54F" {s()}/>
<path d="M40 96 Q42 100 46 99" fill="none" {ln(O, 2)}/>{eye(38, 90, 0.45)}
{limb(64, 72, 60, 96, SKIN, 5)}
{limb(68, 70, 104, 58, SKIN, 5)}
<path d="M48 70 Q66 60 84 70 Q66 80 48 70Z" fill="#2B3A9C" {s()}/>
<g fill="#FFD54F">{''.join(f'<circle cx="{x}" cy="{y}" r="1.8"/>' for x, y in ((55, 69), (62, 66), (70, 67), (77, 70), (64, 73)))}</g>
<path d="M58 70 Q60 50 66 42 Q72 50 72 70Z" fill="#2B3A9C" {s()}/>
{limb(62, 48, 40, 30, SKIN, 4)}{limb(70, 48, 88, 30, SKIN, 4)}
<circle cx="66" cy="32" r="10" fill="{SKIN}" {s()}/>
<circle cx="66" cy="21" r="5" fill="#5A3A22" {s('stroke-width="2.2"')}/>
<path d="M56 30 Q66 20 76 30" fill="#5A3A22" {s('stroke-width="2"')}/>
{eye(62, 33, 0.45)}{eye(70, 33, 0.45)}<path d="M64 38 Q66 40 68 38" fill="none" {ln(O, 1.6)}/>
'''))

# 2 «Изодом» (ИЗО 4–17): черепашка с панцирем-палитрой ползёт по листу и оставляет цветной след
I["izodom-staraya-basmannaya"] = ("зелёная черепашка, у которой панцирь — деревянная палитра с пятнами красок",
    "ползёт по белому листу бумаги, оставляя за собой дорожку из разноцветных пятен", bg("#FFF8E1", "#F6B24A", f'''
<path d="M6 70 L118 58 L124 112 L10 122Z" fill="#fff" {s()}/>
<g>{''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="{c}"/>' for x, y, c in ((18, 104, "#E53935"), (30, 98, "#FB8C00"), (40, 106, "#FDD835"), (24, 114, "#43A047"), (12, 92, "#1E88E5")))}</g>
<ellipse cx="54" cy="102" rx="6" ry="4" fill="#7CB342" {s('stroke-width="2.4"')}/><ellipse cx="96" cy="102" rx="6" ry="4" fill="#7CB342" {s('stroke-width="2.4"')}/>
<path d="M44 94 Q48 52 82 50 Q112 54 108 92 Q76 104 44 94Z" fill="#D7A86E" {s()}/>
<ellipse cx="96" cy="66" rx="5" ry="4" fill="#fff" {s('stroke-width="2"')}/>
<g>{''.join(f'<circle cx="{x}" cy="{y}" r="5.5" fill="{c}" {s("stroke-width=\"1.8\"")}/>' for x, y, c in ((60, 74, "#E53935"), (74, 64, "#FDD835"), (88, 80, "#1E88E5"), (70, 86, "#43A047"), (54, 88, "#AB47BC")))}</g>
<path d="M108 84 Q124 80 122 66 Q118 56 108 64" fill="#9CCC65" {s()}/>
{eye(114, 68, 0.5)}<path d="M117 75 Q120 76 121 73" fill="none" {ln(O, 1.6)}/>
'''))

# 4 Stella (актёрское 4–17, вокал): девочка в картонной короне играет королеву между кулисами
I["stella-rublevskoe"] = ("девочка в самодельной картонной короне и красной мантии с белой опушкой",
    "играет королеву на маленькой сцене между раздвинутыми бирюзовыми кулисами, подняв руку в приветствии", bg("#FFF0F5", "#C2185B", f'''
<path d="M0 0 H30 Q22 60 34 128 H0Z M128 0 H98 Q106 60 94 128 H128Z" fill="#26A69A" {s()}/>
<path d="M0 0 H128 V14 Q64 22 0 14Z" fill="#00796B" {s()}/>
<path d="M20 112 H108 V128 H20Z" fill="#8D6E63" {s()}/>
<path d="M44 112 Q46 72 64 70 Q82 72 84 112Z" fill="#D32F2F" {s()}/>
<path d="M44 112 H84" {ln("#fff", 5)}/><path d="M52 76 Q64 84 76 76" fill="none" {ln("#fff", 4)}/>
{limb(78, 82, 96, 62, SKIN, 5)}
<circle cx="64" cy="56" r="14" fill="{SKIN}" {s()}/>
<path d="M50 54 Q50 42 64 42 Q78 42 78 54 Q74 46 64 47 Q54 46 50 54Z" fill="#6D4C41" {s('stroke-width="2.2"')}/>
<path d="M50 44 L50 30 L57 37 L64 26 L71 37 L78 30 L78 44Z" fill="#E0B35A" {s()}/>
<circle cx="64" cy="34" r="2.6" fill="#E53935"/>
{eye(59, 57, 0.5)}{eye(69, 57, 0.5)}<path d="M61 63 Q64 66 67 63" fill="none" {ln(O, 1.8)}/>
'''))

# 5 Радченко (музыкально-хоровая школа): три воробья поют хором на проводах-нотном стане
I["radchenko-vorontsovskaya"] = ("три пухлых воробья в красной, жёлтой и синей бабочках",
    "поют хором с раскрытыми клювами, сидя на пяти проводах, натянутых как нотный стан, над ними ноты", bg("#E3F2FD", "#64B5F6", f'''
<g>{''.join(f'<path d="M0 {y} Q64 {y+6} 128 {y}" fill="none" stroke="#37474F" stroke-width="2"/>' for y in (70, 76, 82, 88, 94))}</g>
''' + ''.join(f'''
<ellipse cx="{x}" cy="62" rx="14" ry="12" fill="#A1887F" {s()}/>
<ellipse cx="{x}" cy="66" rx="8" ry="6" fill="#EFEBE9"/>
<circle cx="{x}" cy="46" r="10" fill="#8D6E63" {s()}/>
{eye(x - 4, 45, 0.4)}{eye(x + 4, 45, 0.4)}
<path d="M{x-4} 51 L{x} 58 L{x+4} 51Z" fill="#FFB300" {s('stroke-width="2"')}/>
<path d="M{x-5} 56 L{x+5} 56 L{x} 60Z" fill="{c}" {s('stroke-width="1.6"')}/>
<path d="M{x-3} 74 V80 M{x+3} 74 V80" {ln(O, 2.2)}/>''' for x, c in ((30, "#E53935"), (64, "#FDD835"), (98, "#1E88E5"))) + f'''
{note(28, 26, 0.7)}{note(62, 20, 0.8)}{note(96, 28, 0.7)}
'''))

# 6 ArbatGuitar (гитара с 8/11 лет): акустическая гитара-верзила в кедах шагает с нотной тетрадью
I["arbatguitar-marksistskaya"] = ("долговязая акустическая гитара медового цвета в синих кедах",
    "бодро шагает по тротуару на занятие, прижимая к деке зелёную нотную тетрадь", bg("#F1F8E9", "#7CB342", f'''
<path d="M0 112 H128 V128 H0Z" fill="#BDBDBD"/><path d="M0 112 H128" {ln("#9E9E9E", 2)}/>
<path d="M60 6 H72 V48 H60Z" fill="#6D4C41" {s()}/>
<path d="M58 2 H74 V12 H58Z" fill="#4E342E" {s()}/>
<g>{''.join(f'<path d="M60 {y} H72" stroke="#BCAAA4" stroke-width="1.4"/>' for y in (20, 28, 36, 44))}</g>
<path d="M66 46 Q44 44 46 62 Q48 70 42 76 Q34 96 50 104 Q66 110 82 104 Q98 96 90 76 Q84 70 86 62 Q88 44 66 46Z" fill="#E8A44B" {s()}/>
<circle cx="66" cy="84" r="7" fill="#4E342E" {s('stroke-width="2.4"')}/>
<path d="M62 48 V100 M70 48 V100" stroke="#FFF3E0" stroke-width="1.2"/>
{face(66, 64, 7, 0.6)}
{limb(56, 104, 50, 116, "#1E88E5", 6)}{limb(76, 104, 84, 116, "#1E88E5", 6)}
<path d="M42 116 H56 V120 H42Z M78 116 H92 V120 H78Z" fill="#fff" {s('stroke-width="2"')}/>
<rect x="88" y="70" width="22" height="28" rx="2" fill="#43A047" {s()} transform="rotate(10 99 84)"/>
<path d="M92 78 H106 M92 84 H106 M92 90 H104" stroke="#fff" stroke-width="1.6" transform="rotate(10 99 84)"/>
{limb(88, 70, 94, 80, "#E8A44B", 4)}
'''))

# 7 ДШИ № 14 (музыка, фольклор, вокал, ИЗО с 3 лет): гусли с мордашкой, по струнам бегут детские пальчики
I["dshi-14-pronskaya"] = ("деревянные крыловидные гусли с расписным красным узором и мордашкой",
    "лежат на коленках, по струнам бегут детские пальчики, из гуслей вылетают золотые ноты", bg("#FFF3E0", "#E65100", f'''
<path d="M14 70 L114 50 Q122 74 106 96 L22 104 Q8 90 14 70Z" fill="#C68642" {s()}/>
<g>{''.join(f'<path d="M{24+i*3} {72+i*4} L{108-i*1} {58+i*6}" stroke="#FFF8E1" stroke-width="1.4"/>' for i in range(7))}</g>
<path d="M16 72 Q12 88 22 102" fill="none" {ln("#B71C1C", 5)}/>
<g fill="#D32F2F">{''.join(f'<circle cx="{x}" cy="{y}" r="2.6"/>' for x, y in ((20, 80), (20, 92), (26, 86)))}</g>
{face(66, 86, 8, 0.6)}
<g>{''.join(f'<ellipse cx="{x}" cy="{y}" rx="4" ry="6" fill="{SKIN}" {s("stroke-width=\"2\"")} transform="rotate(-20 {x} {y})"/>' for x, y in ((80, 66), (88, 64), (96, 63)))}</g>
<path d="M70 72 Q80 54 102 56 Q110 58 106 66" fill="{SKIN}" {s()}/>
{note(30, 40, 0.8, "#FFB300")}{note(56, 28, 0.9, "#FFB300")}{note(94, 26, 0.7, "#FFB300")}
'''))

# 8 Школа телевидения и эстрады (Воронежская): девочка-репортёр перед телекамерой с REC
I["schooltv-voronezhskaya"] = ("девочка-репортёр с каре в оранжевом пиджаке с ручным микрофоном",
    "ведёт репортаж прямо в объектив телекамеры, у которой горит красная лампочка REC", bg("#E8EAF6", "#3949AB", f'''
<path d="M70 52 H116 V84 H70Z" fill="#424242" {s()}/>
<circle cx="76" cy="68" r="12" fill="#212121" {s()}/><circle cx="76" cy="68" r="6" fill="#5C6BC0"/><circle cx="73" cy="65" r="2" fill="#fff"/>
<circle cx="108" cy="58" r="3.4" fill="#F44336"/>
<path d="M100 84 L92 124 M106 84 V124 M112 84 L120 124" {ln("#616161", 4)}/>
<path d="M16 124 Q18 90 38 86 Q58 90 60 124Z" fill="#FB8C00" {s()}/>
<path d="M32 88 L38 100 L44 88" fill="#fff" {s('stroke-width="2"')}/>
{limb(52, 98, 60, 80, "#FB8C00", 6)}
<rect x="57" y="62" width="7" height="18" rx="2" fill="#212121" {s('stroke-width="2"')}/>
<circle cx="60.5" cy="60" r="5" fill="#9E9E9E" {s('stroke-width="2"')}/>
<circle cx="38" cy="66" r="15" fill="{SKIN}" {s()}/>
<path d="M22 70 Q20 48 38 48 Q56 48 54 70 L52 60 Q38 54 24 60Z" fill="#3E2723" {s('stroke-width="2.4"')}/>
{eye(33, 67, 0.5)}{eye(43, 67, 0.5)}<ellipse cx="38" cy="75" rx="3" ry="2.6" fill="{O}"/>
'''))

# 10 «Синий Кот» (театральная мастерская 4–18): синий кот в полумаске раскланивается на краю сцены
I["sinkot-kirovogradsky"] = ("синий кот в чёрной полумаске и бархатной шляпе с белым пером",
    "раскланивается на краю деревянной сцены, сняв шляпу, за ним свисает край алого занавеса", bg("#FFFDE7", "#FBC02D", f'''
<path d="M100 0 Q92 60 110 128 H128 V0Z" fill="#C62828" {s()}/>
<path d="M0 104 H128 V128 H0Z" fill="#A1887F" {s()}/><path d="M0 110 H128" {ln("#8D6E63", 2)}/>
<path d="M38 104 Q36 72 56 68 Q76 70 74 104Z" fill="#3F51B5" {s()}/>
<path d="M70 104 Q90 98 92 84" fill="none" {ln("#3F51B5", 6)}/>
<circle cx="50" cy="50" r="18" fill="#3F51B5" {s()}/>
<path d="M36 40 L34 22 L46 34Z M60 34 L70 22 L66 40Z" fill="#3F51B5" {s()}/>
<path d="M36 46 Q50 38 64 46 Q60 56 50 52 Q40 56 36 46Z" fill="#212121" {s('stroke-width="2"')}/>
<circle cx="44" cy="47" r="2.4" fill="#FFEB3B"/><circle cx="56" cy="47" r="2.4" fill="#FFEB3B"/>
<path d="M46 60 Q50 63 54 60" fill="none" {ln("#fff", 2)}/>
{limb(66, 80, 88, 88, "#3F51B5", 5)}
<path d="M80 92 Q90 78 102 88 L104 94 H78Z" fill="#4A148C" {s()}/>
<path d="M98 86 Q112 70 116 80 Q108 82 100 90" fill="#fff" {s('stroke-width="2"')}/>
'''))

# 11 «А-ля Прима» (рисование 5–11): малыш на коленках рисует пальцем огромное солнце на ватмане
I["alya-prima-pokrovka"] = ("малыш в полосатой сине-белой футболке с перепачканными краской пальцами",
    "стоит на коленках и рисует пальцем огромное оранжевое солнце на расстеленном по полу ватмане", bg("#E1F5FE", "#4FC3F7", f'''
<path d="M4 90 L124 84 L126 126 L2 126Z" fill="#fff" {s()}/>
<circle cx="84" cy="104" r="14" fill="#FF9800"/>
<g>{''.join(f'<path d="M{84+19*c:.0f} {104+11*s_:.0f} L{84+27*c:.0f} {104+15*s_:.0f}" {ln("#FF9800", 4)}/>' for c, s_ in ((1, 0), (0.7, 0.7), (0, 1), (-0.7, 0.7), (-1, 0), (-0.7, -0.7), (0, -1), (0.7, -0.7)))}</g>
<path d="M20 100 Q22 66 40 64 Q58 66 58 96Z" fill="#fff" {s()}/>
<g>{''.join(f'<path d="M{24+ (i%2)} {72+i*6} H{56}" stroke="#1E88E5" stroke-width="3"/>' for i in range(4))}</g>
<path d="M20 100 Q22 66 40 64 Q58 66 58 96Z" fill="none" {s()}/>
{limb(54, 76, 70, 98, SKIN, 5)}
<circle cx="72" cy="100" r="3.6" fill="#FF9800" {s('stroke-width="1.6"')}/>
<path d="M22 100 Q40 112 58 100 L58 108 Q40 118 22 108Z" fill="#455A64" {s()}/>
<circle cx="40" cy="46" r="15" fill="{SKIN}" {s()}/>
<path d="M26 42 Q30 28 44 30 Q56 32 54 44 Q46 36 26 42Z" fill="#FFCA28" {s('stroke-width="2.2"')}/>
{eye(35, 48, 0.5)}{eye(46, 48, 0.5)}<path d="M37 56 Q41 59 45 56" fill="none" {ln(O, 1.8)}/>
<circle cx="31" cy="54" r="2.4" fill="#E53935" opacity=".7"/>
{sparkle(108, 30, 4)}{sparkle(22, 20, 3)}
'''))

# 12 «Орбита» (вокал с 7 лет): микрофон-ракета взлетает над облаками, хвост из нот
I["orbita-lva-tolstogo"] = ("серебристый микрофон-ракета с сеточкой-головой и красными стабилизаторами",
    "взлетает над пушистыми облаками, оставляя за собой хвост из цветных нот вместо огня", bg("#311B92", "#120638", f'''
{sparkle(20, 24, 3)}{sparkle(108, 30, 3.5)}{sparkle(30, 60, 2)}{sparkle(112, 70, 2)}
<path d="M0 112 Q14 96 30 106 Q40 92 58 102 Q72 90 88 104 Q104 94 128 108 V128 H0Z" fill="#ECEFF1" {s()}/>
<g transform="rotate(30 70 54)">
<path d="M58 84 L50 98 L60 94Z M82 84 L90 98 L80 94Z" fill="#E53935" {s()}/>
<rect x="58" y="40" width="24" height="50" rx="8" fill="#B0BEC5" {s()}/>
<circle cx="70" cy="32" r="15" fill="#CFD8DC" {s()}/>
<path d="M58 28 H82 M58 36 H82 M64 18 V46 M76 18 V46" stroke="#78909C" stroke-width="1.6"/>
{face(70, 64, 5, 0.5)}
<rect x="62" y="80" width="16" height="6" fill="#E53935" {s('stroke-width="2"')}/>
</g>
{note(44, 90, 0.7, "#FFEB3B")}{note(30, 104, 0.6, "#4FC3F7")}{note(16, 84, 0.5, "#F06292")}
'''))

# 13 Школа живописи Малеванных (4–17): стакан с кисточками, распустившимися как цветы
I["malevannye-molchanovka"] = ("гранёный стакан воды с мордашкой, полный кисточек",
    "кисточки в нём распустились, как букет цветов, — каждый кончик окрашен в свой цвет, стакан стоит на подоконнике", bg("#E8F5E9", "#66BB6A", f'''
<path d="M0 104 H128 V128 H0Z" fill="#ECEFF1" {s()}/>
<g>{''.join(f'<path d="M64 80 L{x} {y}" {ln("#8D6E63", 4)}/><ellipse cx="{x}" cy="{y}" rx="6" ry="10" fill="{c}" {s("stroke-width=\"2.2\"")} transform="rotate({r} {x} {y})"/>' for x, y, c, r in ((36, 30, "#E53935", -30), (52, 18, "#FDD835", -12), (72, 14, "#1E88E5", 8), (92, 24, "#AB47BC", 26), (104, 44, "#FB8C00", 45), (24, 50, "#43A047", -48)))}</g>
<path d="M40 60 H88 L82 108 H46Z" fill="#B3E5FC" opacity=".9" {s()}/>
<path d="M44 76 Q64 70 84 76" fill="none" {ln("#81D4FA", 3)}/>
<path d="M54 62 L52 106 M64 62 V106 M74 62 L76 106" stroke="#fff" stroke-width="1.6" opacity=".8"/>
{face(64, 88, 8, 0.6)}
'''))

# 14 Гончарная студия Mira (лепка 4–13): глиняная кружка-лягушонок на гончарном круге в детских ладошках
I["mira-zubovsky"] = ("неглазурованная терракотовая кружка-лягушонок с выпуклыми глазками на ободке",
    "крутится на гончарном круге, а с двух сторон её бережно обнимают мокрые детские ладошки", bg("#F3E5F5", "#8E24AA", f'''
<ellipse cx="64" cy="108" rx="50" ry="12" fill="#78909C" {s()}/>
<ellipse cx="64" cy="104" rx="42" ry="9" fill="#B0BEC5" {s()}/>
<path d="M22 112 Q18 106 26 104 M106 112 Q110 106 102 104" fill="none" {ln("#fff", 2.4)}/>
<path d="M42 54 H86 L82 102 H46Z" fill="#D9825B" {s()}/>
<path d="M86 64 Q102 66 100 80 Q98 92 84 90" fill="none" {ln(O, 9)}/><path d="M86 64 Q102 66 100 80 Q98 92 84 90" fill="none" {ln("#D9825B", 5)}/>
<circle cx="52" cy="52" r="9" fill="#D9825B" {s()}/><circle cx="76" cy="52" r="9" fill="#D9825B" {s()}/>
{eye(52, 52, 0.55)}{eye(76, 52, 0.55)}
<path d="M54 74 Q64 82 74 74" fill="none" {ln(O, 2.4)}/>
<ellipse cx="50" cy="78" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/><ellipse cx="78" cy="78" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/>
<path d="M14 64 Q30 60 40 70 Q44 80 38 90 Q24 92 14 84Z" fill="{SKIN}" {s()}/>
<path d="M114 64 Q98 60 88 70 Q84 80 90 90 Q104 92 114 84Z" fill="{SKIN}" {s()}/>
<path d="M30 80 Q34 82 36 86 M98 80 Q94 82 92 86" fill="none" {ln("#BF6B45", 2.4)}/>
'''))

# 15 Art Impulse (скетч маркерами 6–13, аниме): толстый маркер рисует аниме-глаз в скетчбуке
I["art-impulse-abelmanovskaya"] = ("толстый двусторонний спиртовой маркер мятного цвета с мордашкой",
    "рисует в раскрытом скетчбуке огромный аниме-глаз с бликами и длинными ресницами", bg("#E0F2F1", "#26A69A", f'''
<path d="M8 60 L62 66 L62 118 L10 112Z" fill="#fff" {s()}/><path d="M62 66 L116 58 L118 110 L62 118Z" fill="#fff" {s()}/>
<path d="M62 66 V118" {ln("#B0BEC5", 2)}/>
<path d="M18 88 Q34 72 52 86 Q34 100 18 88Z" fill="#fff" {s('stroke-width="2.6"')}/>
<circle cx="35" cy="87" r="8" fill="#7E57C2" {s('stroke-width="2"')}/><circle cx="35" cy="88" r="4" fill="#311B92"/>
<circle cx="32" cy="84" r="2.4" fill="#fff"/><circle cx="38" cy="90" r="1.2" fill="#fff"/>
<path d="M18 86 L12 80 M22 80 L18 72 M30 76 L28 68" {ln(O, 2.4)}/>
<g transform="rotate(35 88 52)">
<rect x="78" y="10" width="20" height="62" rx="8" fill="#80CBC4" {s()}/>
<rect x="78" y="10" width="20" height="14" rx="6" fill="#00897B" {s()}/>
<path d="M82 72 L94 72 L90 86 L86 86Z" fill="#7E57C2" {s('stroke-width="2.4"')}/>
{face(88, 46, 5, 0.5)}
</g>
'''))

# 16 Matita (рисунок 4–16, «matita» — итал. карандаш): карандаш с подкрученными усами штрихует шар с тенью
I["matita-tsvetnoy"] = ("графитовый карандаш-итальянец в зелёно-бело-красном шарфике с подкрученными чёрными усами",
    "штрихует на листе академический шар с падающей тенью, вокруг на листе лежат графитовые крошки", bg("#FAFAFA", "#90A4AE", f'''
<path d="M6 54 L100 46 L106 122 L10 124Z" fill="#FFFDF5" {s()}/>
<circle cx="46" cy="92" r="20" fill="none" {ln("#546E7A", 2.4)}/>
<g>{''.join(f'<path d="M{40+i*4} {76+i*2} L{60} {96-i*4}" stroke="#78909C" stroke-width="1.3"/>' for i in range(5))}</g>
<ellipse cx="54" cy="114" rx="22" ry="4" fill="#90A4AE" opacity=".7"/>
<g transform="rotate(32 92 52)">
<rect x="84" y="6" width="18" height="62" fill="#37474F" {s()}/>
<path d="M84 68 L93 84 L102 68Z" fill="#FFE0B2" {s()}/><path d="M90 78 L93 84 L96 78Z" fill="{O}"/>
<rect x="84" y="4" width="18" height="8" fill="#F48FB1" {s('stroke-width="2.4"')}/>
{eye(89, 30, 0.45)}{eye(97, 30, 0.45)}
<path d="M86 38 Q89 34 93 38 Q97 34 100 38" fill="none" {ln("#212121", 2.6)}/>
<path d="M80 46 H106 V52 H80Z" fill="#43A047" {s('stroke-width="2"')}/><path d="M89 46 H97 V52 H89Z" fill="#fff"/><path d="M97 46 H106 V52 H97Z" fill="#E53935"/>
</g>
<g fill="#455A64">{''.join(f'<circle cx="{x}" cy="{y}" r="1.4"/>' for x, y in ((76, 104), (82, 110), (70, 112)))}</g>
'''))

# 17 Virtuozoff (вокал, гитара, фортепиано, барабаны с 5 лет): девочка с косичками-нотами поёт, стоя на банкетке
I["virtuozoff-studencheskaya"] = ("девочка лет пяти, у которой две косички заканчиваются чёрными нотами-восьмушками",
    "поёт с закрытыми глазами, стоя на круглой красной фортепианной банкетке, руки раскинуты", bg("#FFF3E0", "#FF7043", f'''
<path d="M0 118 H128 V128 H0Z" fill="#6D4C41"/>
<path d="M40 96 H88 V104 H40Z" fill="#C62828" {s()}/><ellipse cx="64" cy="96" rx="24" ry="5" fill="#E53935" {s()}/>
<path d="M48 104 L44 118 M80 104 L84 118 M64 104 V118" {ln(O, 4)}/>
{limb(58, 82, 56, 94, SKIN, 5)}{limb(70, 82, 72, 94, SKIN, 5)}
<path d="M48 84 Q50 58 64 56 Q78 58 80 84Z" fill="#FFCA28" {s()}/>
{limb(52, 64, 28, 52, SKIN, 5)}{limb(76, 64, 100, 52, SKIN, 5)}
<circle cx="64" cy="40" r="15" fill="{SKIN}" {s()}/>
<path d="M49 38 Q50 24 64 24 Q78 24 79 38 Q72 30 64 31 Q56 30 49 38Z" fill="#5D4037" {s('stroke-width="2.2"')}/>
<path d="M50 34 Q36 36 32 24 M78 34 Q92 36 96 24" fill="none" {ln("#5D4037", 4)}/>
{note(30, 26, 0.75)}{note(94, 26, 0.75)}
<path d="M57 40 Q59 38 61 40 M67 40 Q69 38 71 40" fill="none" {ln(O, 1.8)}/>
<ellipse cx="64" cy="48" rx="3.2" ry="3.6" fill="{O}"/>
<ellipse cx="54" cy="45" rx="3" ry="1.8" fill="#FF7FA8" opacity=".6"/><ellipse cx="74" cy="45" rx="3" ry="1.8" fill="#FF7FA8" opacity=".6"/>
{note(14, 70, 0.55, "#7E57C2")}{note(112, 72, 0.55, "#00897B")}
'''))

# 18 Арт-студия «Домик» (живопись с 1 года, керамика детям): гигантская акварельная капля-радуга стекает в глиняную миску
I["domik-lopukhinsky"] = ("неровная глиняная мисочка ручной лепки с отпечатками пальчиков и мордашкой",
    "в неё с кончика толстой кисти падает радужная капля краски, по краям мисочки — разноцветные мазки", bg("#FFFDE7", "#AED581", f'''
<path d="M14 26 L74 46" {ln(O, 12)}/><path d="M14 26 L74 46" {ln("#A1887F", 8)}/>
<path d="M70 42 Q86 44 88 56 Q78 62 70 52Z" fill="#7E57C2" {s()}/>
<path d="M80 62 Q72 74 80 80 Q88 74 80 62Z" fill="url(#rb)" {s('stroke-width="2.4"')}/>
<defs><linearGradient id="rb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E53935"/><stop offset=".35" stop-color="#FDD835"/><stop offset=".7" stop-color="#43A047"/><stop offset="1" stop-color="#1E88E5"/></linearGradient></defs>
<path d="M22 86 Q26 120 64 120 Q102 120 106 86 Q64 94 22 86Z" fill="#D7A27A" {s()}/>
<ellipse cx="64" cy="86" rx="42" ry="8" fill="#C48A62" {s()}/>
<ellipse cx="64" cy="87" rx="30" ry="4" fill="#1E88E5" opacity=".6"/>
<g fill="#B97A55">{''.join(f'<ellipse cx="{x}" cy="{y}" rx="3" ry="4"/>' for x, y in ((34, 100), (92, 102), (50, 112)))}</g>
{face(64, 104, 8, 0.55)}
<path d="M30 92 Q34 96 38 92" fill="none" {ln("#E53935", 3)}/><path d="M92 94 Q96 98 100 94" fill="none" {ln("#43A047", 3)}/>
{sparkle(108, 30, 4, "#FFB300")}{sparkle(30, 60, 3)}
'''))


if __name__ == "__main__":
    for pid, (hero, scene, svg_) in I.items():
        open(os.path.join(ROOT, "icons-src", pid + ".svg"), "w").write(svg_)
    if "--subjects" in sys.argv:
        p = os.path.join(ROOT, "icons-src", "subjects.txt")
        have = open(p, encoding="utf-8").read()
        with open(p, "a", encoding="utf-8") as f:
            for pid, (hero, scene, _) in I.items():
                if not any(l.startswith(pid + " — ") for l in have.splitlines()):
                    f.write(f"{pid} — герой: {hero} | сцена: {scene}\n")
    print(len(I))
