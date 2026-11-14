"""Иконки робота creative, 14.11 (запуск 1114g/1114h). Каждая придумана и нарисована отдельно: свой герой, своя сцена,
своя компоновка и свой фон (правило абсолютной уникальности). python3 tools/icons_creative_1114g.py [--subjects] [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_creative_1112k import bg, ln, limb, note, SKIN

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
I = {}


def kid(x, y, r, hair, k=0.5, smile=True):
    """Голова ребёнка: кожа, чёлка, глазки, улыбка."""
    m = f'<path d="M{x-3} {y+6} Q{x} {y+9} {x+3} {y+6}" fill="none" {s("stroke-width=\"1.6\"")}/>' if smile else ""
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{SKIN}" {s()}/>'
            f'<path d="M{x-r} {y-1} A{r} {r} 0 0 1 {x+r} {y-1} Q{x} {y-r+5} {x-r} {y-1}Z" fill="{hair}" {s("stroke-width=\"2.2\"")}/>'
            f'{eye(x-4, y+2, k)}{eye(x+4, y+2, k)}{m}')


# BabyDance, Берёзовая аллея (танцы для малышей 2,5–7 лет): малышка в юбке-ромашке кружится под берёзкой
I["babydance-berezovaya"] = ("малышка с рыжим хвостиком в пачке-ромашке из белых лепестков с жёлтой серединкой-поясом",
    "кружится на носочке под белой берёзкой, подняв над головой зелёный берёзовый листик, как веер",
    bg("#EBFBEE", "#2F9E44", f'''
<rect x="92" y="-4" width="12" height="112" fill="#fff" {s()}/>
<path d="M92 20 h6 M98 40 h6 M92 62 h7 M97 84 h7" {ln(O, 2.6)}/>
<path d="M104 14 Q120 8 128 18 Q116 24 104 22Z M104 46 Q122 42 130 52 Q116 56 104 52Z" fill="#8CE99A" {s('stroke-width="2"')}/>
<ellipse cx="54" cy="112" rx="34" ry="6" fill="#B2F2BB"/>
<path d="M50 84 L46 108 M58 84 L60 106" {ln(O, 7)}/><path d="M50 84 L46 108 M58 84 L60 106" {ln(SKIN, 4)}/>
<path d="M42 108 h7 M56 106 l7 -3" {ln("#F783AC", 4)}/>
{''.join(f'<ellipse cx="{54+26*c:.1f}" cy="{80+8*sn:.1f}" rx="9" ry="5" fill="#fff" {s("stroke-width=\"2\"")} transform="rotate({a} {54+26*c:.1f} {80+8*sn:.1f})"/>' for a, c, sn in [(0, 1, 0), (35, .8, .6), (-35, .8, -.6), (0, -1, 0), (-35, -.8, .6), (35, -.8, -.6), (90, 0, 1), (90, .35, 1), (90, -.35, 1)])}
<ellipse cx="54" cy="78" rx="16" ry="6" fill="#FFD43B" {s()}/>
<path d="M46 56 Q54 52 62 56 L62 74 H46Z" fill="#fff" {s()}/>
<path d="M62 60 L74 40" {ln(O, 7)}/><path d="M62 60 L74 40" {ln(SKIN, 4)}/>
<path d="M46 60 L34 70" {ln(O, 7)}/><path d="M46 60 L34 70" {ln(SKIN, 4)}/>
<path d="M74 40 Q70 24 80 18 Q86 30 74 40Z" fill="#69DB7C" {s('stroke-width="2"')}/><path d="M75 38 L79 22" {ln("#2F9E44", 1.6)}/>
{kid(54, 42, 11, "#E8590C", 0.5)}
<path d="M64 36 Q76 34 72 50 Q68 42 62 42Z" fill="#E8590C" {s('stroke-width="2"')}/>
<circle cx="64" cy="35" r="3" fill="#F06595" {s('stroke-width="1.6"')}/>
{sparkle(24, 40, 5, "#fff")}{sparkle(30, 94, 3.5, "#FFF3BF")}
'''))

# Танц_Среда, Лазоревый проезд (современный танец 7–14 лет): девочка в прыжке, за ней летит длинная лазурная лента-шарф
I["tanzsreda-lazorevy"] = ("девочка-подросток с длинным тёмным хвостом в белой майке и широких лазурных брюках",
    "летит в современном прыжке, откинув голову и раскинув руки, а за её плечами по воздуху вьётся длинная лазурная лента-шарф над пустым деревянным полом зала",
    bg("#E7F5FF", "#1864AB", f'''
<rect x="-4" y="104" width="136" height="28" fill="#E9B872" {s()}/>
<path d="M10 104 L2 132 M40 104 L36 132 M72 104 L72 132 M104 104 L108 132" {ln("#C08A4A", 2)}/>
<path d="M30 46 Q8 34 14 18 Q24 30 40 28 Q58 26 66 40" fill="none" {ln(O, 9)}/>
<path d="M30 46 Q8 34 14 18 Q24 30 40 28 Q58 26 66 40" fill="none" {ln("#4DABF7", 6)}/>
<path d="M56 58 L84 72 L96 92" {ln(O, 13)}/><path d="M56 58 L84 72 L96 92" {ln("#74C0FC", 9)}/>
<path d="M58 62 L46 84 L30 90" {ln(O, 13)}/><path d="M58 62 L46 84 L30 90" {ln("#74C0FC", 9)}/>
<path d="M96 92 l6 4 M30 90 l-6 -2" {ln(O, 5)}/>
<path d="M50 42 Q62 38 70 46 L62 66 Q52 66 48 58Z" fill="#fff" {s()}/>
<path d="M52 46 L28 34" {ln(O, 7)}/><path d="M52 46 L28 34" {ln(SKIN, 4)}/>
<path d="M68 46 L96 34" {ln(O, 7)}/><path d="M68 46 L96 34" {ln(SKIN, 4)}/>
<circle cx="62" cy="30" r="10" fill="{SKIN}" {s()}/>
<path d="M53 26 A10 10 0 0 1 71 25 Q64 22 53 26Z" fill="#343A40" {s('stroke-width="2"')}/>
<path d="M70 24 Q90 10 104 22 Q92 20 76 30Z" fill="#343A40" {s('stroke-width="2"')}/>
<path d="M57 31 q2 -2 4 0 M64 31 q2 -2 4 0" fill="none" {ln(O, 1.8)}/>
<path d="M59 35 Q62 38 65 35" fill="none" {ln(O, 1.6)}/>
{sparkle(108, 54, 5, "#fff")}{sparkle(20, 64, 4, "#D0EBFF")}
'''))

# ManGo, ул. Горчакова (спортивная хореография, мажоретки, твирлинг): манго в шапке мажоретки подбрасывает жезл
I["mango-gorchakova"] = ("спелое жёлто-оранжевое манго с мордашкой в высокой синей шапке мажоретки с белым плюмажем",
    "марширует, высоко подняв колено, а над ним в воздухе вертится подброшенный серебряный жезл-батон с белыми набалдашниками",
    bg("#FFF9DB", "#F08C00", f'''
<path d="M84 34 L118 14" {ln(O, 7)}/><path d="M84 34 L118 14" {ln("#DEE2E6", 4)}/>
<circle cx="84" cy="34" r="5.5" fill="#fff" {s()}/><circle cx="118" cy="14" r="4.5" fill="#fff" {s()}/>
<path d="M90 16 q6 -8 14 -6 M110 38 q8 -2 10 -10" fill="none" {ln("#fff", 2.6)}/>
<path d="M56 102 L52 118 M74 98 L84 88 L86 102" {ln(O, 7)}/><path d="M56 102 L52 118 M74 98 L84 88 L86 102" {ln("#FFD8A8", 4)}/>
<path d="M46 118 h10 M82 104 h9" {ln("#fff", 5)}/>
<path d="M64 46 Q96 48 94 80 Q90 106 62 104 Q34 100 36 74 Q38 46 64 46Z" fill="#FFB238" {s()}/>
<path d="M78 56 Q92 64 88 84 Q80 96 70 100 Q90 88 78 56Z" fill="#F76707" opacity=".55"/>
<path d="M46 60 Q48 54 54 52" fill="none" {ln("#FFF3BF", 3)}/>
{face(64, 76, 9, 0.75)}
<path d="M46 50 L48 30 Q64 24 80 30 L82 50 Q64 44 46 50Z" fill="#1C7ED6" {s()}/>
<path d="M48 44 Q64 40 80 44" fill="none" {ln("#FCC419", 2.6)}/>
<path d="M64 26 Q58 10 66 4 Q74 12 66 26Z" fill="#fff" {s('stroke-width="2.2"')}/>
<path d="M40 82 L22 86" {ln(O, 6)}/><path d="M40 82 L22 86" {ln("#FFB238", 3.4)}/>
<path d="M90 70 L104 48" {ln(O, 6)}/><path d="M90 70 L104 48" {ln("#FFB238", 3.4)}/>
{sparkle(114, 40, 4, "#fff")}{sparkle(16, 60, 4, "#FFF3BF")}
'''))

# Planeta Place, Щербинка (современные танцы, эстрадный вокал, ИЗО): сиреневая планета с кольцом из мазков краски поёт в микрофон
I["planeta-place-shcherbinka"] = ("сиреневая планета с мордашкой и кольцом из радужных мазков краски",
    "напевает в маленький серебристый микрофон, а по её кольцу, как по сцене, скачут три нотки среди звёзд ночного неба",
    bg("#7048E8", "#1B1340", f'''
{sparkle(20, 36, 4, "#FFF3BF")}{sparkle(108, 30, 5, "#fff")}{sparkle(102, 108, 3.5, "#D0BFFF")}{sparkle(24, 100, 3, "#fff")}
<ellipse cx="64" cy="70" rx="56" ry="15" fill="none" {ln(O, 13)} transform="rotate(-14 64 70)"/>
<path d="M14 84 Q40 82 64 70" fill="none" {ln("#FF6B6B", 9)} transform="rotate(-14 64 70)"/>
<path d="M64 70 Q90 58 116 56" fill="none" {ln("#FCC419", 9)} transform="rotate(-14 64 70)"/>
<circle cx="64" cy="64" r="30" fill="#B197FC" {s()}/>
<path d="M40 52 Q52 46 62 50 M70 86 Q82 84 88 76" fill="none" {ln("#9775FA", 4)}/>
<path d="M14 84 Q40 92 64 86" fill="none" {ln("#51CF66", 9)} transform="rotate(-14 64 70)"/>
<path d="M64 86 Q92 82 116 58" fill="none" {ln("#339AF0", 9)} transform="rotate(-14 64 70)"/>
{face(58, 60, 8, 0.7)}
<path d="M80 72 L90 82" {ln(O, 5)}/><path d="M80 72 L90 82" {ln("#868E96", 2.6)}/>
<circle cx="76" cy="68" r="6.5" fill="#CED4DA" {s()}/><path d="M72 66 h8 M72 70 h8" {ln(O, 1.2)}/>
{note(26, 70, 0.7, "#fff")}{note(98, 78, 0.65, "#FFE066")}{note(50, 26, 0.6, "#fff")}
'''))

# Art керамика, Коммунарка (ручная лепка для детей от 7 лет): сырая глиняная сова из жгутиков на дощечке
I["art-keramika-kommunarka"] = ("серая необожжённая глиняная совушка, вылепленная из жгутиков и колбасок, с глазами-пуговками",
    "сидит на деревянной дощечке рядом с деревянной стекой и мисочкой мутной воды и ждёт печи для обжига",
    bg("#FFF4E6", "#A0522D", f'''
<path d="M-4 100 L132 92 L132 132 L-4 132Z" fill="#D9A066" {s()}/>
<path d="M14 104 L118 98" {ln("#B07A44", 2)}/>
<path d="M84 98 L118 76" {ln(O, 7)}/><path d="M84 98 L118 76" {ln("#E8C07A", 4)}/>
<path d="M114 78 l6 -4 l-2 7Z" fill="#E8C07A" {s('stroke-width="1.6"')}/>
<ellipse cx="22" cy="100" rx="16" ry="6" fill="#74C0FC" {s()}/>
<path d="M6 100 Q8 112 22 112 Q36 112 38 100" fill="#E9ECEF" {s()}/>
<path d="M14 98 Q22 102 30 98" fill="none" {ln("#A5D8FF", 2)}/>
<path d="M44 96 Q36 70 46 48 Q50 38 56 34 L58 44 Q64 40 70 44 L72 34 Q78 38 82 48 Q92 70 84 96Z" fill="#ADB5BD" {s()}/>
<path d="M50 64 Q64 58 78 64 M48 74 Q64 68 80 74 M48 84 Q64 78 80 84" fill="none" {ln("#868E96", 2.6)}/>
<circle cx="56" cy="52" r="8" fill="#CED4DA" {s('stroke-width="2.4"')}/><circle cx="72" cy="52" r="8" fill="#CED4DA" {s('stroke-width="2.4"')}/>
{eye(56, 52, 0.75)}{eye(72, 52, 0.75)}
<path d="M64 56 l-3 5 h6Z" fill="#E8C07A" {s('stroke-width="1.6"')}/>
<path d="M46 70 Q38 80 44 90 M82 70 Q90 80 84 90" fill="none" {ln("#868E96", 3)}/>
<path d="M54 96 v4 M60 96 v4 M68 96 v4 M74 96 v4" {ln(O, 2.4)}/>
{sparkle(104, 34, 5, "#fff")}{sparkle(22, 46, 4, "#FFE8CC")}
'''))

# «Я – Актёр!», ул. Шкулёва (актёрское мастерство 4–17 лет): мальчик в луче прожектора с маской-улыбкой на палочке
I["ya-akter-shkuleva"] = ("кудрявый мальчик в синей жилетке с белой маской-улыбкой на палочке",
    "стоит один в жёлтом конусе прожектора на тёмной сцене и раскланивается, прижав ладонь к груди, а маску держит в поднятой руке",
    bg("#862E9C", "#1F0A2E", f'''
<path d="M50 -4 L78 -4 L118 112 L10 112Z" fill="#FFE066" opacity=".55"/>
<rect x="-4" y="108" width="136" height="24" fill="#7F4A1E" {s()}/>
<ellipse cx="64" cy="110" rx="34" ry="5" fill="#FFF3BF" opacity=".8"/>
<path d="M56 84 L54 108 M70 84 L72 108" {ln(O, 8)}/><path d="M56 84 L54 108 M70 84 L72 108" {ln("#495057", 5)}/>
<path d="M48 108 h9 M70 108 h9" {ln(O, 5)}/>
<path d="M50 56 Q63 52 76 56 L76 86 H50Z" fill="#fff" {s()}/>
<path d="M54 56 L60 86 M72 56 L66 86" {ln("#1971C2", 7)}/><path d="M50 56 L58 86 H50Z M76 56 L68 86 H76Z" fill="#1971C2" {s('stroke-width="2"')}/>
<path d="M56 66 Q62 70 66 66" {ln(O, 7)}/><path d="M56 66 Q62 70 66 66" {ln(SKIN, 4)}/>
<path d="M76 60 L90 46" {ln(O, 7)}/><path d="M76 60 L90 46" {ln(SKIN, 4)}/>
<path d="M90 46 L92 34" {ln("#A0673A", 3)}/>
<ellipse cx="93" cy="26" rx="13" ry="11" fill="#fff" {s()}/>
<path d="M86 23 q3 -3 6 0 M94 23 q3 -3 6 0" fill="none" {ln(O, 2)}/><path d="M86 29 Q93 36 100 29" fill="none" {ln(O, 2.2)}/>
<circle cx="63" cy="42" r="11" fill="{SKIN}" {s()} transform="rotate(14 63 42)"/>
<path d="M52 38 Q50 26 60 28 Q62 22 70 26 Q78 26 75 38 Q70 32 63 34 Q56 32 52 38Z" fill="#5C3A1E" {s('stroke-width="2"')}/>
<path d="M58 45 q2 2 4 0 M66 46 q2 2 4 0" fill="none" {ln(O, 1.8)}/><path d="M60 50 Q64 53 68 50" fill="none" {ln(O, 1.6)}/>
{sparkle(24, 30, 4, "#fff")}{sparkle(30, 70, 3, "#FFE066")}
'''))

# Школа рисования «Ярис», Красногорск (рисование гуашью 4–6 лет, скетчинг 9–14 лет): баночка гуаши в крышке-берете рисует динозаврика
I["yaris-krasnogorsk"] = ("пузатая стеклянная баночка синей гуаши с мордашкой и откинутой набок крышкой, похожей на берет",
    "держит кисточку и дорисовывает на приколотом к доске листе кривого зелёного динозаврика с жёлтыми пятнышками",
    bg("#FFF0F6", "#D6336C", f'''
<rect x="8" y="14" width="64" height="58" rx="3" fill="#C9A27A" {s()}/>
<rect x="13" y="19" width="54" height="48" fill="#fff" {s('stroke-width="2"')}/>
<circle cx="18" cy="23" r="2.4" fill="#E03131"/><circle cx="62" cy="23" r="2.4" fill="#1C7ED6"/>
<path d="M18 50 Q24 56 30 54" fill="none" {ln(O, 6)}/><path d="M18 50 Q24 56 30 54" fill="none" {ln("#69DB7C", 3)}/>
<ellipse cx="38" cy="52" rx="12" ry="8" fill="#69DB7C" {s('stroke-width="2.2"')}/>
<path d="M46 48 Q50 36 52 30" fill="none" {ln(O, 8)}/><path d="M46 48 Q50 36 52 30" fill="none" {ln("#69DB7C", 5)}/>
<ellipse cx="55" cy="28" rx="7" ry="5" fill="#69DB7C" {s('stroke-width="2.2"')}/><circle cx="57" cy="27" r="1.4" fill="{O}"/>
<path d="M32 59 v5 M44 59 v5" {ln(O, 3)}/>
<path d="M28 45 l3 -4 l3 4 l3 -4 l3 4" fill="#FCC419" {s('stroke-width="1.6"')}/>
<circle cx="36" cy="53" r="2.2" fill="#FFD43B"/><circle cx="42" cy="50" r="1.8" fill="#FFD43B"/>
<path d="M62 112 Q56 86 62 78 H106 Q112 86 106 112Z" fill="#D0EBFF" {s()}/>
<path d="M60 92 Q84 86 108 92 L108 112 H60Z" fill="#1C7ED6" opacity=".9"/>
<path d="M62 112 Q56 86 62 78 H106 Q112 86 106 112Z" fill="none" {s()}/>
<rect x="64" y="72" width="40" height="8" rx="2" fill="#E9ECEF" {s('stroke-width="2.2"')}/>
<path d="M98 72 Q110 56 124 66 Q118 74 104 74Z" fill="#E64980" {s()}/><circle cx="114" cy="62" r="2.6" fill="{O}"/>
{face(84, 98, 8, 0.65)}
<path d="M70 92 L58 70" {ln(O, 6)}/><path d="M70 92 L58 70" {ln("#D0EBFF", 3)}/>
<path d="M58 70 L54 62" {ln("#A0673A", 3.4)}/><path d="M54 62 l-2 -5" {ln("#2F9E44", 4)}/>
{sparkle(106, 30, 5, "#fff")}{sparkle(26, 92, 4, "#FFDEEB")}
'''))

# «Зигма Арт», Смоленская набережная (театральная студия 5–16 лет): маска Пьеро с розой выглядывает из-за кулисы
I["zigma-art-smolenskaya"] = ("белая маска Пьеро с чёрной слезинкой, в остроконечном белом колпачке с чёрными помпонами",
    "выглядывает из-за бирюзовой кулисы, протягивая зрителям алую розу, а за ней в глубине сцены горят три лампы рампы",
    bg("#E6FCF5", "#087F5B", f'''
<rect x="-4" y="104" width="136" height="28" fill="#5C3A1E" {s()}/>
<circle cx="76" cy="104" r="5" fill="#FFE066" {s('stroke-width="2"')}/><circle cx="96" cy="104" r="5" fill="#FFE066" {s('stroke-width="2"')}/><circle cx="116" cy="104" r="5" fill="#FFE066" {s('stroke-width="2"')}/>
<path d="M-4 -4 H48 Q40 30 46 60 Q52 90 40 110 H-4Z" fill="#0CA678" {s()}/>
<path d="M14 -4 Q8 50 16 110 M30 -4 Q24 50 30 110" fill="none" {ln("#087F5B", 3)}/>
<path d="M62 30 L82 4 L96 34Z" fill="#fff" {s()}/>
<circle cx="82" cy="4" r="4" fill="{O}"/><circle cx="72" cy="22" r="3" fill="{O}"/><circle cx="88" cy="24" r="3" fill="{O}"/>
<path d="M58 44 Q58 30 78 30 Q100 30 100 48 Q100 70 80 74 Q58 72 58 44Z" fill="#fff" {s()}/>
<path d="M66 44 q4 -4 8 0 M84 44 q4 -4 8 0" fill="none" {ln(O, 2.6)}/>
<path d="M70 50 q-2 6 0 10 q2 -4 0 -10Z" fill="{O}"/>
<path d="M74 62 Q80 66 86 62" fill="none" {ln("#E03131", 2.6)}/>
<ellipse cx="94" cy="56" rx="4" ry="2.4" fill="#FF8787" opacity=".7"/>
<path d="M46 74 Q58 76 66 84" {ln(O, 7)}/><path d="M46 74 Q58 76 66 84" {ln("#fff", 4)}/>
<path d="M66 84 L86 82" {ln("#2F9E44", 3)}/><path d="M76 83 q2 -6 8 -6 q-2 6 -8 6Z" fill="#51CF66" {s('stroke-width="1.6"')}/>
<circle cx="90" cy="81" r="7" fill="#E03131" {s()}/><path d="M86 80 q4 -4 8 0 q-4 4 -8 0" fill="none" {ln("#A61E4D", 1.8)}/>
{sparkle(112, 22, 5, "#fff")}{sparkle(108, 70, 3.5, "#C3FAE8")}
'''))

# Salsa-Да!, ул. Академика Варги (латиноамериканские танцы для детей 4–6 лет): мальчик кружит девочку в сальсе
I["salsa-da-vargi"] = ("пара дошколят: мальчик в чёрной жилетке с алым галстуком-бабочкой и девочка в жёлтом платье с оборками",
    "танцуют сальсу: мальчик поднял руку, а девочка кружится под ней так, что юбка-волан разлетается колоколом",
    bg("#FFE3E3", "#C2255C", f'''
<path d="M-4 112 H132 V132 H-4Z" fill="#862E9C" {s()}/>
<path d="M30 92 L28 112 M40 92 L42 112" {ln(O, 7)}/><path d="M30 92 L28 112 M40 92 L42 112" {ln("#212529", 4)}/>
<path d="M22 112 h8 M40 112 h8" {ln(O, 4.4)}/>
<path d="M24 60 Q35 56 46 60 L46 94 H24Z" fill="#fff" {s()}/>
<path d="M24 60 L32 94 H24Z M46 60 L38 94 H46Z" fill="#212529" {s('stroke-width="2"')}/>
<path d="M30 60 l5 4 l5 -4 l0 6 l-5 -2 l-5 2Z" fill="#E03131" {s('stroke-width="1.6"')}/>
<path d="M46 64 L60 40 L74 26" {ln(O, 7)}/><path d="M46 64 L60 40 L74 26" {ln(SKIN, 4)}/>
<path d="M24 66 L16 82" {ln(O, 7)}/><path d="M24 66 L16 82" {ln(SKIN, 4)}/>
{kid(35, 46, 10, "#212529", 0.5)}
<path d="M82 98 L80 112 M92 98 L96 110" {ln(O, 7)}/><path d="M82 98 L80 112 M92 98 L96 110" {ln(SKIN, 4)}/>
<path d="M74 112 h8 M94 110 l8 -2" {ln("#E03131", 4)}/>
<path d="M66 96 Q72 74 86 70 Q100 74 108 96 Q98 92 94 100 Q88 92 80 100 Q76 92 66 96Z" fill="#FCC419" {s()}/>
<path d="M72 92 Q80 86 86 90 M92 90 Q98 86 104 92" fill="none" {ln("#F59F00", 2.2)}/>
<path d="M80 72 Q87 68 94 72 L92 78 H82Z" fill="#FCC419" {s('stroke-width="2.2"')}/>
<path d="M82 72 L76 28" {ln(O, 7)}/><path d="M82 72 L76 28" {ln(SKIN, 4)}/>
<path d="M94 74 L108 82" {ln(O, 7)}/><path d="M94 74 L108 82" {ln(SKIN, 4)}/>
{kid(87, 58, 10, "#7B4B2A", 0.5)}
<path d="M95 52 Q106 50 104 64 Q100 58 96 60Z" fill="#7B4B2A" {s('stroke-width="2"')}/>
<circle cx="80" cy="49" r="3" fill="#E03131" {s('stroke-width="1.4"')}/>
<path d="M62 76 q-6 4 -4 10 M112 70 q6 4 4 10" fill="none" {ln("#fff", 2.4)}/>
{sparkle(108, 30, 5, "#fff")}{sparkle(16, 34, 4, "#FFF3BF")}
'''))

# «Эмюзиан», Красногорск (вокал и танцы для детей от 3 лет): девочка с пучком-ананасом поёт у стойки и делает шаг в сторону
I["emusian-krasnogorsk"] = ("девочка с высоким пучком-ананасом и зелёной резинкой в блестящем золотом комбинезоне",
    "поёт в микрофон на чёрной стойке и одновременно отставляет ножку в танцевальном шаге, а над сценой мигает гирлянда из круглых лампочек",
    bg("#4C2A85", "#160B2E", f'''
<path d="M-4 18 Q64 34 132 18" fill="none" {ln(O, 2.6)}/>
{''.join(f'<circle cx="{x}" cy="{18 + 16 - abs(x-64)/4:.0f}" r="4.5" fill="{c}" {s("stroke-width=\"1.8\"")}/>' for x, c in [(10, "#FFE066"), (30, "#FF8787"), (50, "#74C0FC"), (78, "#FFE066"), (98, "#FF8787"), (118, "#74C0FC")])}
<rect x="-4" y="108" width="136" height="24" fill="#343A40" {s()}/>
<path d="M88 50 L84 108 M76 108 h16" {ln(O, 4)}/>
<path d="M88 50 L74 54" {ln(O, 3)}/>
<ellipse cx="70" cy="55" rx="5" ry="6.5" fill="#868E96" {s()} transform="rotate(-20 70 55)"/>
<path d="M46 84 L40 108 M54 84 L74 98" {ln(O, 8)}/><path d="M46 84 L40 108 M54 84 L74 98" {ln("#FCC419", 5)}/>
<path d="M34 108 h9 M72 96 l7 4" {ln("#fff", 5)}/>
<path d="M40 58 Q50 54 60 58 L58 86 H42Z" fill="#FCC419" {s()}/>
<path d="M44 64 l3 2 M52 70 l3 2 M46 78 l3 2" {ln("#fff", 1.8)}/>
<path d="M58 62 L66 56" {ln(O, 7)}/><path d="M58 62 L66 56" {ln(SKIN, 4)}/>
<path d="M42 62 L26 50" {ln(O, 7)}/><path d="M42 62 L26 50" {ln(SKIN, 4)}/>
<circle cx="50" cy="44" r="11" fill="{SKIN}" {s()}/>
<path d="M39 42 A11 11 0 0 1 61 42 Q50 36 39 42Z" fill="#7B4B2A" {s('stroke-width="2"')}/>
<ellipse cx="50" cy="26" rx="8" ry="7" fill="#7B4B2A" {s('stroke-width="2.2"')}/>
<path d="M46 22 l4 -10 l4 10" fill="#40C057" {s('stroke-width="1.8"')}/>
<rect x="44" y="31" width="12" height="3" rx="1.5" fill="#40C057"/>
<path d="M45 45 q2 -2 4 0 M52 45 q2 -2 4 0" fill="none" {ln(O, 1.8)}/>
<ellipse cx="53" cy="51" rx="3" ry="2.6" fill="#C92A2A" {s('stroke-width="1.4"')}/>
{note(104, 72, 0.7, "#FFE066")}{note(20, 76, 0.6, "#fff")}
{sparkle(112, 98, 3.5, "#fff")}
'''))

if __name__ == "__main__":
    if "--subjects" in sys.argv:
        for k, (h, sc, _) in I.items():
            print(f"{k} — герой: {h} | сцена: {sc}")
        sys.exit()
    ids = [a for a in sys.argv[1:] if not a.startswith("-")] or list(I)
    for k in ids:
        open(os.path.join(ROOT, "icons-src", k + ".svg"), "w").write(I[k][2])
    print(len(ids))
