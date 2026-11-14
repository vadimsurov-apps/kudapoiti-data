"""Иконки робота creative, 14.11 (запуск 1114i). Каждая придумана и нарисована отдельно: свой герой, своя сцена,
своя компоновка и свой фон (правило абсолютной уникальности). python3 tools/icons_creative_1114i.py [--subjects] [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, sparkle, O
from icons_creative_1112k import bg, ln, note, SKIN

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
I = {}


def arm(x1, y1, x2, y2, c=SKIN, w=4):
    return f'<path d="M{x1} {y1} L{x2} {y2}" {ln(O, w + 3)}/><path d="M{x1} {y1} L{x2} {y2}" {ln(c, w)}/>'


def kid(x, y, r, hair, k=0.5):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{SKIN}" {s()}/>'
            f'<path d="M{x-r} {y-1} A{r} {r} 0 0 1 {x+r} {y-1} Q{x} {y-r+5} {x-r} {y-1}Z" fill="{hair}" {s("stroke-width=\"2.2\"")}/>'
            f'{eye(x-4, y+2, k)}{eye(x+4, y+2, k)}'
            f'<path d="M{x-3} {y+6} Q{x} {y+9} {x+3} {y+6}" fill="none" {s("stroke-width=\"1.6\"")}/>')


# «Миллениум», Клары Цеткин (джаз-модерн, концертные номера, гран-при): девочка в прыжке-звёздочке под золотым салютом
I["millenium-klary-tsetkin"] = ("девочка с чёрным пучком в серебристом концертном платье с бахромой и красных лаковых туфельках",
    "зависла в прыжке-«звёздочке» над краем тёмной сцены, раскинув руки и ноги, а над ней раскрывается золотой салют, фон ночной фиолетовый",
    bg("#9775FA", "#3B1F7A", f'''
{''.join(f'<path d="M64 26 L{64+30*dx:.0f} {26+30*dy:.0f}" {ln("#FFD43B", 2.4)}/><circle cx="{64+33*dx:.0f}" cy="{26+33*dy:.0f}" r="2.6" fill="#FFE066"/>' for dx, dy in [(1, 0), (.7, .7), (.7, -.7), (0, -1), (-.7, -.7), (-1, 0), (-.7, .7)])}
<rect x="-4" y="108" width="136" height="24" fill="#212529" {s()}/>
<path d="M-4 108 H132" {ln("#FFD43B", 2)}/>
<path d="M58 82 L36 104" {ln(O, 8)}/><path d="M58 82 L36 104" {ln(SKIN, 5)}/>
<path d="M70 82 L92 104" {ln(O, 8)}/><path d="M70 82 L92 104" {ln(SKIN, 5)}/>
<path d="M31 102 l8 6 l-2 -9Z M97 102 l-8 6 l2 -9Z" fill="#E03131" {s('stroke-width="2"')}/>
{arm(54, 58, 28, 40)}{arm(74, 58, 100, 40)}
<path d="M28 40 l-6 -4 M28 40 l-7 0 M28 40 l-5 -7 M100 40 l6 -4 M100 40 l7 0 M100 40 l5 -7" {ln(O, 2)}/>
<path d="M52 54 Q64 50 76 54 L80 86 H48Z" fill="#DEE2E6" {s()}/>
{''.join(f'<path d="M{x} 86 L{x} 94" {ln("#ADB5BD", 2.2)}/>' for x in range(50, 80, 4))}
<path d="M52 62 H76 M50 72 H78" {ln("#fff", 1.6)}/>
{kid(64, 40, 12, "#212529", 0.55)}
<circle cx="64" cy="25" r="7" fill="#212529" {s('stroke-width="2.2"')}/>
<circle cx="70" cy="22" r="2.4" fill="#E03131"/>
{sparkle(22, 70, 4, "#FFE066")}{sparkle(108, 72, 3.5, "#fff")}
''', cx="50%", cy="20%"))

# «Жете», Кузьминки (балет 3–16 лет): бабочка-капустница в пачке делает гран-жете между одуванчиками
I["zhete-kuzminki"] = ("белая бабочка-капустница с чёрными пятнышками на крыльях, в крошечной розовой пачке и на тонких ножках-пуантах",
    "летит в балетном гран-жете с одного жёлтого одуванчика на другой, вытянув ножки в шпагат, над зелёным лугом, фон утренний мятный",
    bg("#E6FCF5", "#63E6BE", f'''
<path d="M-4 104 Q30 96 64 102 Q98 96 132 104 V132 H-4Z" fill="#8CE99A" {s()}/>
<path d="M22 104 L24 78 M106 104 L104 76" {ln("#2F9E44", 3)}/>
{''.join(f'<path d="M{cx} {cy} l{8*dx:.1f} {8*dy:.1f}" {ln("#FAB005", 3)}/>' for cx, cy in [(24, 74), (104, 72)] for dx, dy in [(1, 0), (.7, .7), (0, 1), (-.7, .7), (-1, 0), (-.7, -.7), (0, -1), (.7, -.7)])}
<circle cx="24" cy="74" r="6" fill="#FFD43B" {s('stroke-width="2"')}/><circle cx="104" cy="72" r="6" fill="#FFD43B" {s('stroke-width="2"')}/>
<path d="M30 70 Q46 52 64 52 Q82 52 98 68" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="3 5"/>
<path d="M56 62 L30 66 M72 62 L98 60" {ln(O, 2.6)}/>
<path d="M30 66 l-4 2 M98 60 l4 1" {ln("#F783AC", 3)}/>
<path d="M60 44 Q40 18 26 30 Q20 46 58 52Z" fill="#fff" {s()}/>
<path d="M68 44 Q88 18 102 30 Q108 46 70 52Z" fill="#fff" {s()}/>
<path d="M58 52 Q38 54 34 66 Q48 70 60 56Z M70 52 Q90 54 94 66 Q80 70 68 56Z" fill="#F8F9FA" {s()}/>
<circle cx="38" cy="32" r="4" fill="#495057"/><circle cx="90" cy="32" r="4" fill="#495057"/>
<path d="M26 30 Q30 26 34 28 M102 30 Q98 26 94 28" {ln("#495057", 3)}/>
<ellipse cx="64" cy="60" rx="18" ry="5" fill="#FCC2D7" {s()}/>
<ellipse cx="64" cy="50" rx="5" ry="13" fill="#F1F3F5" {s()}/>
<circle cx="64" cy="34" r="8" fill="#F8F9FA" {s()}/>
{eye(61, 34, 0.45)}{eye(67, 34, 0.45)}
<path d="M61 22 Q58 12 52 10 M67 22 Q70 12 76 10" fill="none" {ln(O, 2)}/>
<circle cx="52" cy="10" r="2.4" fill="{O}"/><circle cx="76" cy="10" r="2.4" fill="{O}"/>
{sparkle(112, 40, 4, "#fff")}
''', cx="40%", cy="18%"))

# «Премьера», Арбат (детский театр фонда Золотухина): арбатский фонарь освещает уличную сцену мальчику в треуголке
I["premiera-arbat"] = ("чугунный трёхрожковый фонарь Старого Арбата с тёплыми плафонами и мордашкой на столбе",
    "вечером склонил плафон и светит конусом света на дощатый помост, где мальчик в бумажной треуголке читает монолог, вскинув руку, фон сине-вечерний",
    bg("#4C6EF5", "#1C2A6B", f'''
<rect x="-4" y="104" width="136" height="28" fill="#868E96" {s()}/>
<path d="M10 104 l-4 28 M36 104 l-2 28 M62 104 v28 M88 104 l2 28 M114 104 l4 28" {ln("#495057", 1.6)}/>
<path d="M40 20 L4 104 H74Z" fill="#FFE066" opacity=".35"/>
<rect x="30" y="16" width="8" height="92" rx="2" fill="#343A40" {s()}/>
<path d="M22 108 h24" {ln(O, 6)}/>
<path d="M34 22 Q34 10 46 10 M34 22 Q34 10 22 10" fill="none" {ln("#343A40", 4)}/>
<path d="M18 10 h10 l-2 10 h-6Z M40 10 h10 l-2 10 h-6Z" fill="#FFD43B" {s('stroke-width="2.2"')}/>
<path d="M30 4 h8 l-1 9 h-6Z" fill="#FFD43B" {s('stroke-width="2.2"')}/>
<ellipse cx="34" cy="52" rx="7" ry="9" fill="#495057"/>
{eye(31, 50, 0.4)}{eye(37, 50, 0.4)}<path d="M31 56 Q34 58 37 56" fill="none" {ln("#fff", 1.4)}/>
<rect x="52" y="90" width="64" height="14" fill="#C08A4A" {s()}/>
<path d="M60 90 v14 M76 90 v14 M92 90 v14 M108 90 v14" {ln("#8B5A2B", 1.6)}/>
<path d="M78 76 L74 90 M86 76 L90 90" {ln(O, 7)}/><path d="M78 76 L74 90 M86 76 L90 90" {ln("#364FC7", 4)}/>
<path d="M74 54 Q82 50 90 54 L90 78 H74Z" fill="#E03131" {s()}/>
<path d="M82 56 v20" {ln("#FFD43B", 2)}/>
{arm(88, 58, 104, 38)}{arm(76, 58, 70, 70)}
<path d="M104 38 l3 -5 M104 38 l5 -1" {ln(O, 2)}/>
{kid(82, 42, 10, "#7B4B2A", 0.45)}
<path d="M68 36 Q82 20 96 36 Q82 30 68 36Z" fill="#fff" {s('stroke-width="2.2"')}/>
<circle cx="82" cy="28" r="2.4" fill="#E03131"/>
{sparkle(110, 18, 4, "#fff")}{sparkle(62, 14, 3, "#FFF3BF")}
''', cx="60%", cy="20%"))

# «Дети райка», Жулебино (театральная студия; райок — верхний ярус театра): голубь-зритель аплодирует на галёрке
I["deti-rayka-zhulebino"] = ("пухлый сизый голубь-театрал с радужной шейкой и красной бабочкой",
    "сидит на бархатном бортике верхнего яруса-галёрки под самым потолком с золотой лепниной и хлопает крыльями-аплодисментами, внизу виден край сцены с занавесом, фон тёмно-вишнёвый",
    bg("#C2255C", "#5C0F2E", f'''
<path d="M-4 6 Q16 18 36 6 Q56 18 76 6 Q96 18 116 6 Q126 12 132 8" fill="none" {ln("#FFD43B", 4)}/>
<circle cx="36" cy="10" r="3" fill="#FFD43B"/><circle cx="76" cy="10" r="3" fill="#FFD43B"/><circle cx="116" cy="10" r="3" fill="#FFD43B"/>
<path d="M-4 112 Q20 104 40 112 V132 H-4Z M88 112 Q108 104 132 112 V132 H88Z" fill="#E03131" {s()}/>
<path d="M40 118 H88 V132 H40Z" fill="#E9B872" {s()}/>
<rect x="-4" y="78" width="136" height="16" rx="6" fill="#A61E4D" {s()}/>
<path d="M-4 86 H132" {ln("#FFD43B", 2.4)}/>
<path d="M14 94 v16 M34 94 v16 M94 94 v16 M114 94 v16" {ln("#FFD43B", 3)}/>
<path d="M58 78 l-2 8 M70 78 l2 8" {ln("#F76707", 3)}/>
<ellipse cx="64" cy="62" rx="24" ry="18" fill="#ADB5BD" {s()}/>
<path d="M44 56 Q28 40 34 30 Q46 42 50 54Z" fill="#868E96" {s()}/>
<path d="M84 56 Q100 40 94 30 Q82 42 78 54Z" fill="#868E96" {s()}/>
<path d="M34 30 l-4 -4 M36 28 l-1 -6 M94 30 l4 -4 M92 28 l1 -6" {ln("#fff", 2)}/>
<ellipse cx="64" cy="48" rx="13" ry="9" fill="#63E6BE" opacity=".8"/>
<circle cx="64" cy="36" r="13" fill="#CED4DA" {s()}/>
{eye(59, 35, 0.5)}{eye(69, 35, 0.5)}
<path d="M61 41 L64 46 L67 41Z" fill="#F08C00" {s('stroke-width="1.6"')}/>
<path d="M56 50 l8 3 l8 -3 l-1 6 l-7 -3 l-7 3Z" fill="#E03131" {s('stroke-width="1.8"')}/>
<circle cx="64" cy="53" r="2.2" fill="#C92A2A"/>
{sparkle(20, 40, 4, "#FFE066")}{sparkle(110, 46, 3.5, "#fff")}
''', cx="50%", cy="30%"))

# «Артист», Фрунзенская набережная (актёрское, живопись и керамика 4–12 лет): глиняный человечек кланяется на гончарном круге
I["artist-frunzenskaya-nab"] = ("терракотовый глиняный человечек с отпечатками пальцев на животике и синим шарфиком",
    "стоит на вращающемся гончарном круге, как на сцене, и раскланивается, держа над головой кисточку с каплей бирюзовой краски, фон сливочно-абрикосовый",
    bg("#FFF4E6", "#FFA94D", f'''
<ellipse cx="64" cy="104" rx="46" ry="12" fill="#868E96" {s()}/>
<ellipse cx="64" cy="100" rx="46" ry="12" fill="#CED4DA" {s()}/>
<ellipse cx="64" cy="100" rx="30" ry="7" fill="#ADB5BD"/>
<path d="M20 92 Q12 98 20 104 M108 92 Q116 98 108 104" fill="none" {ln(O, 2.2)}/>
<path d="M58 80 L54 98 M70 80 L74 98" {ln(O, 11)}/><path d="M58 80 L54 98 M70 80 L74 98" {ln("#D9773A", 7)}/>
<path d="M46 52 Q64 44 82 52 L80 84 Q64 90 48 84Z" fill="#E8590C" {s()}/>
<circle cx="58" cy="66" r="2.4" fill="#C2410C"/><circle cx="68" cy="72" r="2.4" fill="#C2410C"/><circle cx="62" cy="76" r="2" fill="#C2410C"/>
<path d="M48 58 Q34 66 30 80" fill="none" {ln(O, 11)}/><path d="M48 58 Q34 66 30 80" fill="none" {ln("#D9773A", 7)}/>
<path d="M80 56 L96 32" {ln(O, 11)}/><path d="M80 56 L96 32" {ln("#D9773A", 7)}/>
<path d="M94 34 L110 12" {ln(O, 5)}/><path d="M94 34 L110 12" {ln("#C08A4A", 3)}/>
<path d="M108 14 Q112 6 114 10 Q114 16 110 16Z" fill="#212529" {s('stroke-width="1.6"')}/>
<path d="M114 18 Q117 24 114 26 Q111 24 114 18Z" fill="#22B8CF" {s('stroke-width="1.4"')}/>
<circle cx="62" cy="38" r="15" fill="#E8590C" {s()}/>
<path d="M54 36 q3 -3 6 0 M64 36 q3 -3 6 0" fill="none" {ln(O, 2)}/>
<path d="M56 44 Q62 49 68 44" fill="none" {ln(O, 2)}/>
<circle cx="52" cy="42" r="3" fill="#FF8787" opacity=".7"/><circle cx="72" cy="42" r="3" fill="#FF8787" opacity=".7"/>
<path d="M48 52 Q64 60 80 52 L82 58 Q64 64 46 58Z" fill="#1C7ED6" {s('stroke-width="2"')}/>
<path d="M78 58 l6 14 l5 -2 l-5 -13" fill="#1C7ED6" {s('stroke-width="2"')}/>
{sparkle(24, 30, 4.5, "#fff")}
''', cx="40%", cy="25%"))

# «Сурик-АРТ», Измайлово (художественная студия с 5 лет): банка краски «СУРИК» рисует на мольберте рыжее солнце
I["surik-art-izmaylovo"] = ("пухлая жестяная банка оранжево-красной краски с этикеткой «СУРИК», ручкой-дужкой и мордашкой",
    "стоит на табуретке у мольберта и кисточкой в ручке рисует на холсте рыжее солнце с лучами, с края банки стекает капля краски, фон светло-лимонный",
    bg("#FFF9DB", "#FFD43B", f'''
<path d="M84 18 L76 112 M108 18 L116 112 M96 12 V108" {ln("#8B5A2B", 4)}/>
<rect x="74" y="26" width="46" height="54" fill="#fff" {s()}/>
<circle cx="97" cy="52" r="10" fill="#F76707"/>
{''.join(f'<path d="M{97+14*dx:.1f} {52+14*dy:.1f} l{5*dx:.1f} {5*dy:.1f}" {ln("#F76707", 3)}/>' for dx, dy in [(1, 0), (.7, .7), (0, 1), (-.7, .7), (-1, 0), (-.7, -.7), (0, -1), (.7, -.7)])}
<rect x="70" y="80" width="54" height="5" fill="#8B5A2B" {s('stroke-width="2"')}/>
<rect x="12" y="98" width="52" height="8" rx="2" fill="#8B5A2B" {s()}/>
<path d="M18 106 l-4 24 M58 106 l4 24" {ln("#8B5A2B", 5)}/>
<path d="M14 44 Q38 24 62 44" fill="none" {ln(O, 3)}/>
<rect x="14" y="44" width="48" height="54" rx="6" fill="#E8590C" {s()}/>
<ellipse cx="38" cy="44" rx="24" ry="6" fill="#C92A2A" {s()}/>
<path d="M18 46 Q20 56 22 50 Q24 60 27 48" fill="#C92A2A" {s('stroke-width="1.6"')}/>
<rect x="20" y="70" width="36" height="16" rx="3" fill="#FFF3BF" {s('stroke-width="2"')}/>
<text x="38" y="82" font-family="Arial" font-weight="bold" font-size="9" text-anchor="middle" fill="{O}">СУРИК</text>
{eye(31, 58, 0.5)}{eye(45, 58, 0.5)}
<path d="M34 64 Q38 67 42 64" fill="none" {ln(O, 1.8)}/>
<path d="M60 60 Q70 56 74 48" fill="none" {ln(O, 7)}/><path d="M60 60 Q70 56 74 48" fill="none" {ln("#E8590C", 4)}/>
<path d="M73 50 L84 40" {ln(O, 4.6)}/><path d="M73 50 L84 40" {ln("#C08A4A", 2.6)}/>
<path d="M83 41 l4 -4 l2 2 l-4 4Z" fill="#F76707" {s('stroke-width="1.4"')}/>
''', cx="35%", cy="25%"))

# «Рисуем с радостью», 1-й Грайвороновский (рисование с 2 лет): малыш в огромном фартуке рисует пальчиками радугу
I["risuem-s-radostyu-graivoronovsky"] = ("малыш лет трёх с белыми кудряшками в огромном лимонном фартуке до пят",
    "сидит на полу на большом листе бумаги и рисует пальчиками радугу, подняв к зрителю разноцветные ладошки, фон нежно-голубой",
    bg("#E7F5FF", "#74C0FC", f'''
<path d="M-4 84 L132 76 V132 H-4Z" fill="#fff" {s()}/>
{''.join(f'<path d="M{8+i*5} 118 Q{60} {44+i*5} {116-i*5} 112" fill="none" {ln(c, 5)}/>' for i, c in enumerate(["#FA5252", "#FD7E14", "#FAB005", "#40C057", "#339AF0", "#7950F2"]))}
<path d="M40 112 Q62 82 84 112Z" fill="#FFE066" {s()}/>
<path d="M50 112 L46 120 M74 112 L78 120" {ln(O, 9)}/><path d="M50 112 L46 120 M74 112 L78 120" {ln(SKIN, 6)}/>
<path d="M50 74 Q62 70 74 74 L70 96 H54Z" fill="#FFE066" {s()}/>
<path d="M56 74 V68 M68 74 V68" {ln(O, 2.2)}/>
{arm(52, 78, 34, 60)}{arm(72, 78, 92, 60)}
<circle cx="32" cy="56" r="7" fill="#FF6B6B" {s('stroke-width="2.2"')}/>
<circle cx="94" cy="56" r="7" fill="#4DABF7" {s('stroke-width="2.2"')}/>
<path d="M27 50 l-2 -5 M32 49 v-6 M37 50 l2 -5 M89 50 l-2 -5 M94 49 v-6 M99 50 l2 -5" {ln(O, 3)}/>
<path d="M28 50 l-2 -4 M33 49 v-5 M90 50 l-2 -4 M95 49 v-5" {ln("#FFD43B", 1.6)}/>
<circle cx="62" cy="54" r="13" fill="{SKIN}" {s()}/>
{''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="#F8F9FA" {s("stroke-width=\"1.8\"")}/>' for x, y in [(52, 44), (58, 40), (66, 40), (72, 44)])}
{eye(57, 55, 0.5)}{eye(67, 55, 0.5)}
<path d="M58 61 Q62 66 66 61Z" fill="#C92A2A" {s('stroke-width="1.6"')}/>
<circle cx="55" cy="62" r="2" fill="#4DABF7"/><circle cx="70" cy="59" r="1.8" fill="#40C057"/>
{sparkle(108, 22, 4, "#fff")}{sparkle(18, 22, 3, "#fff")}
''', cx="50%", cy="25%"))

# «А-голос», Жулебино (вокал с 3 лет, Baby music и Kids vocal): рыжий котёнок-солист поёт в микрофон нотами-сердечками
I["a-golos-zhulebino"] = ("рыжий полосатый котёнок-солист с белой грудкой и широко открытым ротиком",
    "стоит на маленьком круглом подиуме и поёт в серебряный микрофон на стойке, зажмурившись от удовольствия, а из ротика вылетают розовые ноты-сердечки, фон мятно-бирюзовый",
    bg("#C3FAE8", "#20C997", f'''
<ellipse cx="54" cy="110" rx="36" ry="9" fill="#7048E8" {s()}/>
<ellipse cx="54" cy="106" rx="36" ry="9" fill="#9775FA" {s()}/>
<path d="M90 106 V56" {ln(O, 4)}/><path d="M80 108 h20" {ln(O, 4)}/>
<path d="M90 60 L76 50" {ln(O, 3)}/>
<rect x="66" y="42" width="11" height="14" rx="5.5" fill="#CED4DA" {s()} transform="rotate(-35 71 49)"/>
<path d="M68 46 l7 -2 M69 50 l7 -2" {ln("#868E96", 1.4)}/>
<path d="M44 102 L42 90 M60 102 L62 90" {ln(O, 10)}/><path d="M44 102 L42 90 M60 102 L62 90" {ln("#FD7E14", 7)}/>
<ellipse cx="52" cy="80" rx="18" ry="16" fill="#FD7E14" {s()}/>
<ellipse cx="52" cy="84" rx="10" ry="10" fill="#fff"/>
<path d="M36 74 l6 2 M36 82 l6 0 M68 74 l-6 2" {ln("#D9480F", 2.4)}/>
<path d="M34 86 Q18 80 22 64" fill="none" {ln(O, 9)}/><path d="M34 86 Q18 80 22 64" fill="none" {ln("#FD7E14", 6)}/>
<path d="M66 76 L72 60" {ln(O, 9)}/><path d="M66 76 L72 60" {ln("#FD7E14", 6)}/>
<circle cx="50" cy="48" r="18" fill="#FD7E14" {s()}/>
<path d="M34 40 L32 24 L46 32Z M66 40 L68 24 L54 32Z" fill="#FD7E14" {s()}/>
<path d="M36 36 l0 -8 l6 5Z M64 36 l0 -8 l-6 5Z" fill="#FFC9C9"/>
<path d="M44 38 l4 2 M56 38 l-4 2 M50 32 v6" {ln("#D9480F", 2.4)}/>
<path d="M40 46 q3 -3 6 0 M54 46 q3 -3 6 0" fill="none" {ln(O, 2)}/>
<ellipse cx="50" cy="57" rx="5" ry="6" fill="#C92A2A" {s('stroke-width="2"')}/>
<path d="M50 50 l-2 2 h4Z" fill="#F783AC"/>
<path d="M36 52 l-8 -1 M36 55 l-8 2 M64 52 l8 -1 M64 55 l8 2" {ln(O, 1.4)}/>
{''.join(f'<path d="M{x} {y} q-4 -5 0 -7 q4 -2 4 3 q0 -5 4 -3 q4 2 0 7 l-4 4Z" fill="#F06595" {s("stroke-width=\"1.6\"")}/>' for x, y in [(100, 30), (112, 48), (96, 14)])}
<path d="M104 26 v-12 l6 2" fill="none" {ln(O, 2)}/>
''', cx="40%", cy="25%"))

# «А-голос», Жуковский (вокал с 3 лет; Жуковский — город авиации): девочка-лётчица поёт в микрофон на крыле самолёта
I["a-golos-zhukovsky"] = ("девочка-лётчица в коричневом кожаном шлемофоне с поднятыми круглыми очками и длинном белом шарфе",
    "стоит на серебристом крыле летящего самолёта среди облаков и поёт в ретро-микрофон, а шарф развевается за ней вместе с нотами, фон небесно-голубой",
    bg("#D0EBFF", "#4DABF7", f"""
<ellipse cx="22" cy="30" rx="18" ry="8" fill="#fff"/><ellipse cx="108" cy="104" rx="22" ry="9" fill="#fff"/><ellipse cx="30" cy="112" rx="14" ry="6" fill="#fff"/>
<path d="M-4 90 L128 72 L132 84 L-4 104Z" fill="#CED4DA" {s()}/>
<path d="M10 96 L118 81" {ln("#ADB5BD", 2)}/>
<circle cx="112" cy="80" r="3" fill="#E03131"/>
<path d="M52 86 L50 70 M64 84 L66 70" {ln(O, 9)}/><path d="M52 86 L50 70 M64 84 L66 70" {ln("#495057", 6)}/>
<path d="M46 86 h9 M62 84 h9" {ln(O, 5)}/>
<path d="M46 46 Q58 42 70 46 L68 72 H48Z" fill="#8B5A2B" {s()}/>
<path d="M58 48 V70" {ln("#5C3A1A", 2)}/>
<path d="M50 44 Q34 40 18 50 Q30 52 22 60 Q38 54 50 52Z" fill="#fff" {s('stroke-width="2.2"')}/>
{arm(68, 50, 82, 40, "#8B5A2B", 5)}{arm(48, 52, 40, 64, "#8B5A2B", 5)}
<path d="M82 40 L88 30" {ln(O, 4)}/>
<rect x="84" y="18" width="12" height="16" rx="6" fill="#ADB5BD" {s()} transform="rotate(25 90 26)"/>
<path d="M86 24 l9 4 M85 28 l9 4" {ln("#495057", 1.4)}/>
<circle cx="58" cy="32" r="12" fill="{SKIN}" {s()}/>
<path d="M45 34 Q44 16 58 16 Q72 16 71 34 L68 34 Q68 22 58 22 Q48 22 48 34Z" fill="#7B4B2A" {s('stroke-width="2.2"')}/>
<path d="M46 34 v8 M70 34 v8" {ln("#7B4B2A", 4)}/>
<circle cx="52" cy="19" r="4.5" fill="#99E9F2" {s('stroke-width="2"')}/><circle cx="63" cy="19" r="4.5" fill="#99E9F2" {s('stroke-width="2"')}/>
{eye(54, 33, 0.45)}{eye(62, 33, 0.45)}
<ellipse cx="58" cy="39" rx="2.6" ry="3" fill="#C92A2A" {s('stroke-width="1.4"')}/>
{note(30, 26, 0.7, "#fff")}{note(104, 52, 0.75, O)}
"""))

# «А-голос», Раменское (вокал с 3 лет, своя студия звукозаписи): сосновая шишка в наушниках поёт в студийный микрофон
I["a-golos-ramenskoe"] = ("смолисто-коричневая сосновая шишка с мордашкой в больших красных наушниках",
    "поёт в студийный микрофон с сеточкой-поп-фильтром в звукозаписывающей кабине, за стеклом светится пульт с ползунками, фон тёплый янтарный",
    bg("#FFE8CC", "#F08C00", f"""
<rect x="-4" y="-4" width="136" height="40" fill="#343A40" {s()}/>
<rect x="8" y="10" width="112" height="18" rx="3" fill="#495057" {s('stroke-width="2"')}/>
{''.join(f'<path d="M{x} 13 V25" {ln("#212529", 2.4)}/><rect x="{x-3}" y="{y}" width="6" height="4" fill="{c}"/>' for x, y, c in [(18, 15, "#69DB7C"), (30, 20, "#FFD43B"), (42, 14, "#FF6B6B"), (86, 18, "#69DB7C"), (98, 22, "#4DABF7"), (110, 15, "#FFD43B")])}
<path d="M-4 36 H132" {ln("#868E96", 3)}/>
<rect x="-4" y="104" width="136" height="28" fill="#5C3A1A" {s()}/>
<path d="M92 104 V64" {ln(O, 4)}/><path d="M80 106 h24" {ln(O, 4)}/>
<path d="M92 66 L84 60" {ln(O, 3)}/>
<rect x="74" y="44" width="14" height="20" rx="7" fill="#868E96" {s()}/>
<path d="M76 50 h10 M76 55 h10" {ln("#495057", 1.4)}/>
<circle cx="66" cy="54" r="9" fill="none" stroke="{O}" stroke-width="2.4"/>
<circle cx="66" cy="54" r="7" fill="#343A40" opacity=".35"/>
<path d="M66 63 Q64 72 72 72" fill="none" {ln(O, 2)}/>
<ellipse cx="38" cy="72" rx="20" ry="30" fill="#A0522D" {s()}/>
{''.join(f'<path d="M{x-6} {y} Q{x} {y+7} {x+6} {y}" fill="#CD853F" {s("stroke-width=\"1.8\"")}/>' for x, y in [(30, 52), (44, 52), (24, 66), (38, 66), (52, 66), (30, 80), (46, 80), (38, 94)])}
<path d="M38 42 V34" {ln("#5C3A1A", 4)}/>
<path d="M20 66 Q18 40 38 38 Q58 40 56 66" fill="none" {ln(O, 6)}/><path d="M20 66 Q18 40 38 38 Q58 40 56 66" fill="none" {ln("#E03131", 3.4)}/>
<ellipse cx="18" cy="68" rx="6" ry="9" fill="#E03131" {s()}/><ellipse cx="58" cy="68" rx="6" ry="9" fill="#E03131" {s()}/>
<rect x="26" y="56" width="24" height="20" rx="8" fill="#F4D7B3" {s('stroke-width="2"')}/>
<path d="M30 62 q3 -3 6 0 M40 62 q3 -3 6 0" fill="none" {ln(O, 2)}/>
<ellipse cx="38" cy="70" rx="3" ry="3.4" fill="#C92A2A" {s('stroke-width="1.4"')}/>
{note(108, 70, 0.7, "#fff")}{note(116, 92, 0.55, "#FFF3BF")}
"""))

if __name__ == "__main__":
    if "--subjects" in sys.argv:
        for k, (h, sc, _) in I.items():
            print(f"{k} — герой: {h} | сцена: {sc}")
        sys.exit()
    ids = [a for a in sys.argv[1:] if not a.startswith("-")] or list(I)
    for k in ids:
        open(os.path.join(ROOT, "icons-src", k + ".svg"), "w").write(I[k][2])
    print(len(ids))
