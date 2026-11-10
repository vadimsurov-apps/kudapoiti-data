"""Робот «художник», 10.11 ~05:00 UTC.
check_unique.py повторов по строкам не нашёл, но в реестре остались серии «один герой + разные шапки»
(ровно то, что Вадим запретил 07.11): шахматный конь-персонаж ×15, баскетбольный мяч-персонаж ×12,
гимнастка в прыжке «звёздочкой» ×5, красная куртка самбо-персонаж ×4. Из каждой серии одна иконка остаётся
(karpov-chess-school, ibasket-skhodnenskaya, perevoznikov-korolev, sambo-80-polyanka), остальные рисуем заново —
каждая своя идея, свой герой, сцена и палитра. Без циклов-генераторов: каждое тело SVG написано отдельно.
Запуск из корня: python3 tools/icons_artist_1110_0500.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT

I = {}
BB = "#F28A2E"   # баскетбольная кожа


def bline(cx, cy, r):
    """швы баскетбольного мяча (рисующий примитив, не генератор сюжетов)"""
    return (f'<path d="M{cx-r} {cy} H{cx+r} M{cx} {cy-r} V{cy+r}" fill="none" {W(2.2)}/>'
            f'<path d="M{cx-r*.62} {cy-r*.78} Q{cx-r*.25} {cy} {cx-r*.62} {cy+r*.78}" fill="none" {W(2.2)}/>'
            f'<path d="M{cx+r*.62} {cy-r*.78} Q{cx+r*.25} {cy} {cx+r*.62} {cy+r*.78}" fill="none" {W(2.2)}/>')


# ───────────────────────── ШАХМАТЫ ─────────────────────────

# «Лабиринты шахмат», Беляево — клетчатый лабиринт сверху, красная нить ведёт к короне в центре
I["chess-labyrinth-belyaevo"] = (
    "лабиринт из чёрно-белых шахматных клеток (вид сверху) с улыбчивой золотой короной в центре",
    "красная нить Ариадны вьётся от входа через проходы к короне",
    ("#E3FFF4", "#3FB59A"), f'''
<rect x="22" y="22" width="84" height="84" rx="6" fill="#FFF8EA" {W(3)}/>
<path d="M22 36 H36 V22 M50 22 V36 H64 M78 22 V50 H92 V36 M106 64 H92 V78 M22 64 H36 V78 H50
 M64 106 V92 H78 M92 106 V92 M36 92 H50 V106 M64 50 V64 M50 50 H64" fill="none" {W(3)}/>
<rect x="36" y="22" width="14" height="14" fill="{O}"/><rect x="92" y="22" width="14" height="14" fill="{O}"/>
<rect x="22" y="50" width="14" height="14" fill="{O}"/><rect x="78" y="78" width="14" height="14" fill="{O}"/>
<rect x="50" y="92" width="14" height="14" fill="{O}"/><rect x="22" y="92" width="14" height="14" fill="{O}"/>
<rect x="92" y="64" width="14" height="14" fill="{O}" opacity=".85"/>
<path d="M14 114 Q30 112 29 100 Q28 86 43 85 Q57 84 57 74" fill="none" stroke="#E8344E" stroke-width="3.4" stroke-linecap="round" stroke-dasharray="1 0"/>
<path d="M51 74 L49 58 L57 65 L64 54 L71 65 L79 58 L77 74Z" fill="#FFC930" {W(2.8)}/>
<circle cx="64" cy="53" r="2.6" fill="#E8344E" {W(1.6)}/>
{eye(59, 67, .5)}{eye(69, 67, .5)}{blush(55, 71, .5)}{blush(73, 71, .5)}
{sparkle(108, 14, 5)}''')

# Шахматная школа №1, Одинцово — золотой кубок, у которого чаша — зубчатая ладья, на ступеньке «1»
I["chess1-odintsovo"] = (
    "золотой кубок, чаша которого — зубчатая шахматная ладья",
    "сияет на синем пьедестале с цифрой «1» и улыбается",
    ("#CFE0FF", "#3157B8"), f'''
<rect x="34" y="96" width="60" height="28" rx="3" fill="#2A3F8F" {W(3)}/>
<text x="64" y="118" text-anchor="middle" font-family="Arial Black,Arial" font-weight="900" font-size="20" fill="#FFD84A">1</text>
<path d="M50 96 H78 L74 88 H54Z" fill="#E9A916" {W(2.8)}/>
<rect x="58" y="74" width="12" height="14" fill="#F4BE2A" {W(2.8)}/>
<path d="M42 30 H52 V36 H59 V30 H69 V36 H76 V30 H86 V46 Q86 72 64 76 Q42 72 42 46Z" fill="#FFCB36" {W(3)}/>
<path d="M42 44 Q28 44 30 56 Q32 64 44 62 M86 44 Q100 44 98 56 Q96 64 84 62" fill="none" {W(3)}/>
<path d="M48 40 V58" stroke="#FFF2B0" stroke-width="3.5" stroke-linecap="round"/>
{eye(57, 52, .7)}{eye(71, 52, .7)}{blush(52, 59)}{blush(76, 59)}{smile(64, 59, 4)}
{sparkle(20, 40, 6, "#FFF6B0")}{sparkle(108, 30, 5, "#FFF6B0")}{sparkle(104, 78, 4)}''')

# Студия Александры Костенюк — «шахматная королева»: корона ферзя на клетчатой бархатной подушке
I["kosteniuk-chess-tukhachevskogo"] = (
    "золотая корона шахматного ферзя с шариком на макушке",
    "отдыхает на бархатной подушке в чёрно-белую клетку с кисточками",
    ("#FFD9E2", "#A6284E"), f'''
<path d="M18 98 Q20 76 64 76 Q108 76 110 98 Q108 114 64 114 Q20 114 18 98Z" fill="#fff" {W(3)}/>
<path d="M40 79 H54 V112 H40Z M74 77 H88 V112 H74Z" fill="{O}" opacity=".9"/>
<path d="M18 92 Q64 102 110 92" fill="none" {W(2)} opacity=".5"/>
<path d="M18 98 Q8 100 10 108 M110 98 Q120 100 118 108" fill="none" {W(2.6)}/>
<circle cx="10" cy="110" r="3.5" fill="#FFC930" {W(1.8)}/><circle cx="118" cy="110" r="3.5" fill="#FFC930" {W(1.8)}/>
<path d="M36 80 L32 40 L46 54 L54 32 L64 50 L74 32 L82 54 L96 40 L92 80Z" fill="#FFC930" {W(3)}/>
<circle cx="32" cy="38" r="4" fill="#FFE27A" {W(2)}/><circle cx="54" cy="30" r="4" fill="#FFE27A" {W(2)}/>
<circle cx="74" cy="30" r="4" fill="#FFE27A" {W(2)}/><circle cx="96" cy="38" r="4" fill="#FFE27A" {W(2)}/>
<circle cx="64" cy="22" r="6" fill="#FFE27A" {W(2.4)}/><path d="M64 28 V48" {W(2.4)}/>
<rect x="36" y="74" width="56" height="7" rx="2" fill="#E6A512" {W(2.4)}/>
{eye(56, 63, .7)}{eye(72, 63, .7)}{blush(50, 69)}{blush(78, 69)}{smile(64, 69, 3.5)}
{sparkle(108, 22, 5)}{sparkle(18, 22, 4)}''')

# Chess First, Раменки — воздушный шар в шахматную клетку, в корзине едет чёрный слон
I["chessfirst-ramenki"] = (
    "воздушный шар в чёрно-белую шахматную клетку",
    "летит над закатными облаками, в корзинке сидит чёрный шахматный слон",
    ("#FFE8C8", "#F37A5A"), f'''
<ellipse cx="22" cy="104" rx="20" ry="8" fill="#fff" opacity=".85"/><ellipse cx="106" cy="98" rx="18" ry="7" fill="#fff" opacity=".85"/>
<path d="M64 14 Q100 14 100 46 Q100 70 72 84 H56 Q28 70 28 46 Q28 14 64 14Z" fill="#fff" {W(3)}/>
<path d="M64 14 Q50 30 50 46 Q50 66 58 84 L64 84 Q60 60 64 46Z" fill="{O}"/>
<path d="M64 14 Q80 30 80 46 Q80 66 70 84 L64 84 Q68 66 70 46 Q70 28 64 14Z" fill="#fff"/>
<path d="M30 30 Q40 34 50 46 L50 58 Q38 50 29 52Z M98 30 Q88 34 80 46 L80 58 Q90 50 99 52Z" fill="{O}"/>
<path d="M64 14 Q100 14 100 46 Q100 70 72 84 H56 Q28 70 28 46 Q28 14 64 14Z" fill="none" {W(3)}/>
<path d="M57 84 L54 96 M71 84 L74 96" {W(2.2)}/>
<path d="M60 70 Q62 66 64 70 Q66 66 68 70" fill="none" stroke="#fff" stroke-width="0"/>
<ellipse cx="64" cy="94" rx="6" ry="7" fill="{O}" {W(2)}/><circle cx="64" cy="86" r="2.4" fill="{O}"/>
<path d="M50 98 H78 L74 116 H54Z" fill="#C98A4B" {W(3)}/><path d="M53 104 H75 M54 110 H74" {W(1.6)} opacity=".6"/>
{eye(60, 94, .4)}{eye(68, 94, .4)}
{eye(40, 40, .6)}{eye(88, 40, .6)}{blush(36, 48, .8)}{blush(92, 48, .8)}
<path d="M58 56 Q64 62 70 56" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
{sparkle(14, 26, 5)}''')

# Esther Kids, Ленинградское ш. — белая лама держит в зубах шахматного коня, думает над ходом
I["esther-kids-chess"] = (
    "белая кудрявая лама с длинной шеей",
    "задумчиво держит в зубах чёрного шахматного коня над доской",
    ("#F3E8FF", "#9B7BD8"), f'''
<path d="M10 100 L64 88 L118 100 L64 118Z" fill="#fff" {W(3)}/>
<path d="M37 94 L50 91 L64 94 L50 97Z M64 94 L77 91 L91 94 L77 97Z M23 100 L37 97 L50 100 L37 103Z M50 100 L64 97 L77 100 L64 103Z M77 100 L91 97 L104 100 L91 103Z
 M37 106 L50 103 L64 106 L50 109Z M64 106 L77 103 L91 106 L77 109Z M50 112 L64 109 L77 112 L64 115Z" fill="{O}" opacity=".85"/>
<path d="M58 90 Q54 70 60 50 Q62 40 64 30 L80 32 Q78 50 76 70 Q76 82 80 92" fill="#FFFDF7" {W(3)}/>
<path d="M60 64 q4 -4 8 0 q4 -4 8 0 M60 76 q4 -4 8 0 q4 -4 8 0" fill="none" {W(1.6)} opacity=".5"/>
<path d="M62 22 L58 8 L66 18 M78 22 L82 8 L74 18" fill="#FFFDF7" {W(2.6)}/>
<ellipse cx="70" cy="28" rx="16" ry="12" fill="#FFFDF7" {W(3)}/>
<path d="M60 18 q3 -5 6 0 q3 -5 6 0 q3 -5 6 0" fill="#FFFDF7" {W(2)}/>
<ellipse cx="80" cy="34" rx="7" ry="6" fill="#FFE6EE" {W(2.4)}/>
{eye(64, 26, .6)}{eye(75, 26, .6)}{blush(60, 32, .7)}
<path d="M84 50 Q92 44 92 34 Q84 30 88 20 Q96 12 104 20 Q110 30 106 40 L110 50Z" fill="{O}" {W(2.2)}/>
<path d="M92 14 L96 8 L98 15" fill="{O}" {W(1.8)}/><circle cx="98" cy="22" r="1.8" fill="#fff"/>
<rect x="82" y="50" width="30" height="7" rx="2.5" fill="{O}"/>
<path d="M80 36 Q84 38 88 40" fill="none" {W(2.2)}/>
<circle cx="104" cy="54" r="3" fill="#fff" opacity=".9"/><circle cx="110" cy="44" r="2" fill="#fff" opacity=".9"/>''')

# «Гарде», Красногорск — клетчатый щит-охранник заслоняет белого ферзя («гарде» = берегись, ферзь!)
I["garde-chess-krasnogorsk"] = (
    "рыцарский щит в шахматную клетку с бровками",
    "смело заслоняет собой белого ферзя, который выглядывает из-за его края",
    ("#E9F5D6", "#6E9E3A"), f'''
<path d="M76 30 L72 20 L80 26 L84 16 L88 26 L96 20 L92 30Z" fill="#fff" {W(2.4)}/>
<path d="M78 30 Q74 44 82 52 Q72 60 72 104 H104 Q104 60 94 52 Q102 44 98 30Z" fill="#fff" {W(3)}/>
<circle cx="88" cy="14" r="3" fill="#fff" {W(2)}/>
{eye(84, 40, .45)}{eye(93, 40, .45)}<path d="M85 46 Q88.5 44 92 46" fill="none" {W(1.8)}/>
<path d="M20 26 H84 V64 Q84 98 52 114 Q20 98 20 64Z" fill="#fff" {W(3.2)}/>
<path d="M20 26 H52 V58 H20Z M52 58 H84 V64 Q84 82 76 92 L52 92Z" fill="{O}"/>
<path d="M52 92 V114 Q34 106 26 92 Z" fill="none"/>
<path d="M20 26 H84 V64 Q84 98 52 114 Q20 98 20 64Z" fill="none" {W(3.2)}/>
<circle cx="38" cy="72" r="0"/>
{eye(64, 40, .7)}{eye(74, 40, .7)}
<path d="M58 32 L68 35 M80 32 L70 35" {W(2.4)}/>
<path d="M30 74 Q38 80 46 74" fill="none" {W(2.6)}/>
{blush(28, 66, .9)}
<rect x="48" y="112" width="8" height="10" fill="#B27A3B" {W(2)}/>
{sparkle(110, 70, 5)}''')

# СДЦ «Люблино» — белый ферзь гребёт на деревянной лодочке по Люблинскому пруду
I["sdts-lyublino-chess"] = (
    "белый шахматный ферзь-гребец",
    "катается на деревянной лодочке по пруду среди камышей и кувшинок",
    ("#DDF7F4", "#1E8C8C"), f'''
<path d="M-4 86 Q64 78 132 86 V132 H-4Z" fill="#7FD3E0" {W(2.6)}/>
<path d="M16 96 q6 -3 12 0 M92 108 q6 -3 12 0 M40 118 q6 -3 12 0" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M104 86 V54 M110 86 V60 M98 86 V64" {W(2.4)}/>
<ellipse cx="104" cy="54" rx="3" ry="7" fill="#9A6A3A" {W(2)}/><ellipse cx="110" cy="60" rx="3" ry="6" fill="#9A6A3A" {W(2)}/>
<ellipse cx="20" cy="110" rx="10" ry="4" fill="#5FBF6A" {W(2)}/><circle cx="24" cy="106" r="3" fill="#FF9EC0" {W(1.6)}/>
<path d="M50 40 L46 28 L54 34 L58 22 L62 34 L70 28 L66 40Z" fill="#fff" {W(2.4)}/><circle cx="58" cy="19" r="3" fill="#fff" {W(2)}/>
<path d="M52 40 Q46 56 54 62 Q44 70 46 84 H70 Q72 70 62 62 Q70 56 64 40Z" fill="#fff" {W(3)}/>
{eye(54, 50, .5)}{eye(62, 50, .5)}{blush(50, 55, .5)}{blush(66, 55, .5)}<path d="M55 56 Q58 58.5 61 56" fill="none" {W(1.8)}/>
<path d="M24 82 H96 Q90 100 60 100 Q30 100 24 82Z" fill="#C9874A" {W(3)}/>
<path d="M30 88 H90" {W(1.8)} opacity=".6"/>
<path d="M44 70 L20 104 M68 70 L96 102" fill="none" {W(3)}/>
<ellipse cx="18" cy="107" rx="4" ry="7" fill="#C9874A" transform="rotate(35 18 107)" {W(2)}/>
<ellipse cx="98" cy="105" rx="4" ry="7" fill="#C9874A" transform="rotate(-40 98 105)" {W(2)}/>''')

# МЦ «Галактика» — зелёный пришелец двигает пешку на доске, стоящей на астероиде
I["galaktika-chess-filevsky"] = (
    "зелёный пришелец-шахматист с тремя глазами и антеннами",
    "сидит на сером астероиде среди звёзд и двигает белую пешку по маленькой доске",
    ("#4B3C8F", "#140F3A"), f'''
{sparkle(18, 40, 4)}{sparkle(110, 26, 5)}{sparkle(30, 18, 3, "#FFE27A")}{sparkle(104, 60, 3, "#FFE27A")}
<circle cx="96" cy="38" r="7" fill="#FF9E5E" {W(2)}/><path d="M86 40 Q96 34 106 36" fill="none" {W(1.8)}/>
<path d="M14 104 Q16 88 40 86 Q64 80 90 86 Q114 88 114 104 Q110 122 64 122 Q18 122 14 104Z" fill="#9B97B5" {W(3)}/>
<circle cx="34" cy="106" r="5" fill="#7D7A99"/><circle cx="96" cy="110" r="4" fill="#7D7A99"/>
<path d="M60 86 L110 76 L116 86 L66 96Z" fill="#fff" {W(2.6)}/>
<path d="M72 84 L84 82 L86 86 L74 88Z M96 80 L108 78 L110 82 L98 84Z M60 86 L72 84 L74 88 L62 90Z M84 82 L96 80 L98 84 L86 86Z" fill="{O}" opacity=".9"/>
<path d="M30 88 Q26 64 44 58 Q62 64 58 88Z" fill="#7BE36A" {W(3)}/>
<path d="M36 40 L30 24 M52 40 L58 24" {W(2.4)}/><circle cx="30" cy="22" r="3.5" fill="#FFE27A" {W(1.8)}/><circle cx="58" cy="22" r="3.5" fill="#FFE27A" {W(1.8)}/>
<ellipse cx="44" cy="46" rx="18" ry="15" fill="#7BE36A" {W(3)}/>
{eye(36, 44, .6)}{eye(44, 40, .6)}{eye(52, 44, .6)}<path d="M39 52 Q44 56 49 52" fill="none" {W(2)}/>
<path d="M56 70 Q68 70 80 74" fill="none" {W(6)}/><path d="M56 70 Q68 70 80 74" fill="none" stroke="#7BE36A" stroke-width="2.8" stroke-linecap="round"/>
<path d="M80 80 Q78 74 82 70 Q78 66 82 62 Q86 58 90 62 Q94 66 90 70 Q94 74 92 80Z" fill="#fff" {W(2.4)}/>''')

# ChessKids, Войковская — складная шахматная доска-чемоданчик шагает в клуб, из щели выглядывают фигурки
I["chesskids-voykovsky"] = (
    "складная деревянная шахматная доска-чемоданчик на тонких ножках",
    "шагает вприпрыжку в клуб, из приоткрытой щели выглядывают белая ладья и чёрный слон",
    ("#FFE3D9", "#E8664D"), f'''
<path d="M50 96 L44 116 H34 M78 96 L86 116 H96" fill="none" {W(3)}/>
<ellipse cx="32" cy="117" rx="7" ry="3.5" fill="#E8344E" {W(2)}/><ellipse cx="98" cy="117" rx="7" ry="3.5" fill="#E8344E" {W(2)}/>
<path d="M30 42 L98 42 L94 30 L34 30Z" fill="#fff" {W(2.4)}/>
<path d="M44 30 L46 20 L50 20 L50 16 L54 16 L54 20 L58 20 L58 30Z" fill="#fff" {W(2.2)}/>
<path d="M70 30 Q66 22 72 16 Q76 12 80 16 Q86 22 80 30Z" fill="{O}" {W(2)}/><circle cx="75" cy="12" r="2.4" fill="{O}"/>
{eye(50, 24, .3)}{eye(54, 24, .3)}<circle cx="73" cy="22" r="1.4" fill="#fff"/><circle cx="78" cy="22" r="1.4" fill="#fff"/>
<rect x="26" y="40" width="76" height="58" rx="5" fill="#E7B377" {W(3.2)}/>
<rect x="26" y="40" width="19" height="14.5" fill="{O}" opacity=".85"/><rect x="64" y="40" width="19" height="14.5" fill="{O}" opacity=".85"/>
<rect x="45" y="54.5" width="19" height="14.5" fill="{O}" opacity=".85"/><rect x="83" y="54.5" width="19" height="14.5" fill="{O}" opacity=".85"/>
<rect x="26" y="69" width="19" height="14.5" fill="{O}" opacity=".85"/><rect x="64" y="69" width="19" height="14.5" fill="{O}" opacity=".85"/>
<rect x="45" y="83.5" width="19" height="14.5" fill="{O}" opacity=".85"/><rect x="83" y="83.5" width="19" height="14.5" fill="{O}" opacity=".85"/>
<rect x="26" y="40" width="76" height="58" rx="5" fill="none" {W(3.2)}/>
<rect x="56" y="98" width="16" height="6" rx="2" fill="#C9874A" {W(2)}/>
<circle cx="54" cy="62" r="9" fill="#FFF3E0" {W(2.2)}/><circle cx="74" cy="62" r="0"/>
{eye(50, 61, .5)}{eye(58, 61, .5)}<path d="M51 66 Q54 69 57 66" fill="none" {W(1.8)}/>
{sparkle(112, 70, 5)}''')

# Chess First, Мытищи — чёрно-белая корова с пятнами-клетками двигает ладью копытом
I["chess-first-mytishchi"] = (
    "чёрно-белая корова с пятнами в форме шахматных клеток",
    "двигает копытом белую ладью по доске на зелёном лугу",
    ("#EEFFD8", "#86C64A"), f'''
<path d="M-4 96 Q64 88 132 96 V132 H-4Z" fill="#5FBF6A" {W(2.6)}/>
<path d="M66 104 L118 98 L124 110 L72 116Z" fill="#fff" {W(2.6)}/>
<path d="M79 103 L92 101 L94 106 L81 108Z M105 100 L118 98 L120 103 L107 105Z M66 104 L79 103 L81 108 L68 109Z M92 101 L105 100 L107 105 L94 106Z
 M81 108 L94 106 L96 112 L83 114Z M107 105 L120 103 L122 108 L109 110Z" fill="{O}" opacity=".9"/>
<path d="M100 98 V88 H98 V82 H102 V85 H105 V82 H109 V85 H112 V82 H116 V88 H114 V98Z" fill="#fff" {W(2.2)}/>
<path d="M20 60 Q18 44 34 42 H70 Q84 44 82 60 V86 Q80 92 74 92 H28 Q20 92 20 84Z" fill="#fff" {W(3)}/>
<path d="M34 42 H48 V56 H34Z M58 56 H72 V70 H58Z M24 70 H38 V84 H24Z M48 78 H60 V92 H48Z" fill="{O}"/>
<path d="M28 92 V108 M44 92 V110 M64 92 V110" {W(5)}/><path d="M28 92 V108 M44 92 V110 M64 92 V110" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
<path d="M76 70 Q90 76 98 92" fill="none" {W(5)}/><path d="M76 70 Q90 76 98 92" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
<rect x="94" y="90" width="7" height="5" rx="1.5" fill="{O}"/>
<path d="M14 40 Q10 28 18 22 M42 40 Q46 28 40 22" fill="none" {W(3)}/>
<path d="M14 40 Q10 28 18 22 M42 40 Q46 28 40 22" fill="none" stroke="#FFE3A3" stroke-width="1.5"/>
<ellipse cx="28" cy="44" rx="17" ry="15" fill="#fff" {W(3)}/>
<ellipse cx="28" cy="54" rx="11" ry="7" fill="#FFB8C8" {W(2.4)}/><circle cx="24" cy="54" r="1.5" fill="{O}"/><circle cx="32" cy="54" r="1.5" fill="{O}"/>
{eye(22, 40, .55)}{eye(34, 40, .55)}
<ellipse cx="9" cy="42" rx="5" ry="3" fill="#fff" {W(2)} transform="rotate(-20 9 42)"/>''')

# «Совёнок», Королёв — совёнок с перьями в шахматную клетку сидит на ветке под луной и держит пешку
I["sovenok-chess-korolev"] = (
    "пушистый совёнок с грудкой в шахматную клетку",
    "ночью сидит на ветке под луной и держит в лапках белую пешку",
    ("#2E4C7A", "#0D1A33"), f'''
<circle cx="98" cy="30" r="13" fill="#FFF3B0" {W(2.2)}/><circle cx="104" cy="26" r="11" fill="#1B2E52"/>
{sparkle(24, 24, 4)}{sparkle(40, 12, 3)}{sparkle(112, 60, 3)}
<path d="M-4 100 Q40 92 132 104" fill="none" {W(9)}/><path d="M-4 100 Q40 92 132 104" fill="none" stroke="#8C5A33" stroke-width="5.5" stroke-linecap="round"/>
<ellipse cx="108" cy="92" rx="7" ry="4" fill="#5FBF6A" transform="rotate(-30 108 92)" {W(1.8)}/>
<path d="M36 40 L30 24 L46 32 Z M92 40 L98 24 L82 32Z" fill="#B88554" {W(2.6)}/>
<ellipse cx="64" cy="66" rx="32" ry="34" fill="#B88554" {W(3)}/>
<path d="M44 70 Q44 96 64 98 Q84 96 84 70 Q64 62 44 70Z" fill="#fff" {W(2.4)}/>
<path d="M44 70 H54 V79 H44Z M64 66 H74 V74 H64Z M54 79 H64 V88 H54Z M74 79 H84 V88 H74Z M64 88 H74 V97 H64Z" fill="{O}" opacity=".85"/>
<circle cx="52" cy="50" r="12" fill="#FFE9C8" {W(2.4)}/><circle cx="76" cy="50" r="12" fill="#FFE9C8" {W(2.4)}/>
{eye(52, 50, 1.0)}{eye(76, 50, 1.0)}
<path d="M60 58 L64 66 L68 58Z" fill="#FFB43A" {W(2)}/>
<path d="M88 94 Q86 88 90 84 Q86 80 90 76 Q94 72 98 76 Q102 80 98 84 Q102 88 100 94Z" fill="#fff" {W(2.4)}/>
<path d="M82 82 Q88 88 90 92" fill="none" {W(3)}/>
<path d="M54 98 v4 M60 98 v5 M68 98 v5 M74 98 v4" {W(2.4)}/>''')

# «Гроссмейстер», Раменское — мудрая чёрная ладья-дедушка с седой бородой и тросточкой
I["grossmeyster-ramenskoe"] = (
    "чёрная шахматная ладья-дедушка с пышной седой бородой",
    "важно опирается на тросточку и подкручивает ус на клетчатом полу",
    ("#F4EFD9", "#A99A63"), f'''
<path d="M-4 104 L132 104 V132 H-4Z" fill="#fff" {W(2.6)}/>
<path d="M10 104 H30 V132 H10Z M50 104 H70 V132 H50Z M90 104 H110 V132 H90Z" fill="{O}" opacity=".85"/>
<path d="M30 104 L36 96 H92 L98 104Z" fill="#3B3355" {W(3)}/>
<path d="M38 96 L42 54 H86 L90 96Z" fill="#4A4168" {W(3)}/>
<path d="M36 54 V30 H46 V38 H56 V30 H72 V38 H82 V30 H92 V54Z" fill="#4A4168" {W(3)}/>
<path d="M46 60 V90" stroke="#6E6496" stroke-width="3.5" stroke-linecap="round"/>
<path d="M44 66 Q42 92 64 96 Q86 92 84 66 Q78 70 72 66 Q64 72 56 66 Q50 70 44 66Z" fill="#F3F3F7" {W(2.6)}/>
<path d="M52 64 Q58 58 64 64 Q70 58 76 64 Q72 70 64 66 Q56 70 52 64Z" fill="#fff" {W(2.2)}/>
<path d="M50 50 Q55 46 60 50 M68 50 Q73 46 78 50" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<circle cx="56" cy="54" r="2.6" fill="#fff"/><circle cx="72" cy="54" r="2.6" fill="#fff"/>
<path d="M102 104 V60 Q102 50 94 52" fill="none" {W(7)}/><path d="M102 104 V60 Q102 50 94 52" fill="none" stroke="#C9874A" stroke-width="3.6" stroke-linecap="round"/>
<path d="M88 68 Q96 64 100 64" fill="none" {W(6)}/><path d="M88 68 Q96 64 100 64" fill="none" stroke="#4A4168" stroke-width="2.6" stroke-linecap="round"/>
{sparkle(20, 40, 5)}''')

# Moscow Chess School, Ярцевская (в гимназии) — школьная парта с доской на крышке, пешка тянет руку
I["moscow-chess-school-yartsevskaya"] = (
    "зелёная школьная парта с шахматной доской на крышке",
    "за партой белая пешка-ученица тянет руку, на доске стоит партия",
    ("#FFF0D0", "#E6A64A"), f'''
<path d="M48 70 Q46 60 56 58 Q50 50 54 42 Q58 36 64 36 Q70 36 74 42 Q78 50 72 58 Q82 60 80 70Z" fill="#fff" {W(3)}/>
<path d="M54 50 Q44 40 46 22" fill="none" {W(6)}/><path d="M54 50 Q44 40 46 22" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/>
<circle cx="46" cy="20" r="4" fill="#fff" {W(2)}/>
{eye(60, 47, .5)}{eye(68, 47, .5)}{blush(56, 52, .5)}{blush(72, 52, .5)}<path d="M61 53 Q64 55 67 53" fill="none" {W(1.6)}/>
<path d="M22 112 V84 M106 112 V84" {W(4)}/>
<path d="M14 70 L114 70 L106 88 L22 88Z" fill="#4FB27A" {W(3)}/>
<path d="M26 72 H102 L98 84 H30Z" fill="#fff" {W(2)}/>
<path d="M26 72 H38.7 L38 76 H25Z M51.3 72 H64 V76 H50.7Z M76.7 72 H89.4 L89.7 76 H77Z M38 76 H50.7 L50 80 H37Z M64 76 H77 L77.3 80 H64Z M89.7 76 H100.3 L99.7 80 H90Z M30 80 H37 L36.5 84 H29Z M50 80 H64 V84 H49.6Z M77.3 80 H90 L90.4 84 H77.6Z" fill="{O}" opacity=".9"/>
<path d="M44 72 V64 H42 V60 H46 V62 H49 V60 H53 V62 H56 V60 H60 V64 H58 V72Z" fill="{O}" {W(1.8)}/>
<path d="M78 72 Q76 66 80 62 Q76 58 82 56 Q88 58 84 62 Q88 66 86 72Z" fill="#fff" {W(2)}/>
{sparkle(30, 30, 6, "#fff")}{sparkle(104, 40, 4, "#fff")}''')

# Moscow Chess School, Таганская (в библиотеке) — книжный червячок в очках с шахматным конём на стопке книг
I["moscow-chess-school-taganka"] = (
    "розовый книжный червячок в круглых очках",
    "выглядывает из дырочки в стопке книг и держит маленького шахматного коня",
    ("#E8DDCF", "#8A6447"), f'''
<rect x="22" y="94" width="84" height="16" rx="3" fill="#3E7DC4" {W(3)}/><path d="M30 99 H98 M30 105 H98" stroke="#fff" stroke-width="1.6" opacity=".6"/>
<rect x="28" y="78" width="74" height="16" rx="3" fill="#E8344E" {W(3)}/><path d="M36 83 H94 M36 89 H94" stroke="#fff" stroke-width="1.6" opacity=".6"/>
<rect x="18" y="58" width="80" height="20" rx="3" fill="#fff" {W(3)}/>
<path d="M18 58 H32 V68 H18Z M46 58 H60 V68 H46Z M74 58 H88 V68 H74Z M32 68 H46 V78 H32Z M60 68 H74 V78 H60Z M88 68 H98 V78 H88Z" fill="{O}" opacity=".88"/>
<rect x="18" y="58" width="80" height="20" rx="3" fill="none" {W(3)}/>
<path d="M50 60 Q46 40 58 30 Q70 22 78 30" fill="none" {W(17)}/><path d="M50 60 Q46 40 58 30 Q70 22 78 30" fill="none" stroke="#FF9EC0" stroke-width="11" stroke-linecap="round"/>
<path d="M51 52 L57 50 M51 44 L57 44" stroke="#E46E9C" stroke-width="2" stroke-linecap="round"/>
<circle cx="82" cy="34" r="14" fill="#FF9EC0" {W(3)}/>
<circle cx="77" cy="32" r="5.5" fill="#fff" fill-opacity=".5" {W(2)}/><circle cx="89" cy="32" r="5.5" fill="#fff" fill-opacity=".5" {W(2)}/><path d="M82.5 32 H83.5" {W(2)}/>
{eye(77, 32, .45)}{eye(89, 32, .45)}<path d="M80 41 Q83 43.5 86 41" fill="none" {W(1.8)}/>
<path d="M98 58 Q96 52 100 48 Q98 44 102 40 Q108 38 110 44 L112 52 H106 L108 58Z" fill="{O}" {W(1.8)}/>
<path d="M94 46 Q98 48 100 50" fill="none" {W(5)}/><path d="M94 46 Q98 48 100 50" fill="none" stroke="#FF9EC0" stroke-width="2" stroke-linecap="round"/>
{sparkle(30, 30, 5, "#FFF6B0")}''')


# ───────────────────────── БАСКЕТБОЛ ─────────────────────────

# IBASKET, Подольск — баскетбольный щит с кольцом-ртом, мяч крутится по ободу
I["ibasket-podolsk"] = (
    "белый баскетбольный щит с глазками и красным кольцом",
    "мяч крутится по ободу кольца, щит затаил дыхание",
    ("#E8FFC8", "#9BCF3C"), f'''
<path d="M64 128 V96" {W(8)}/><path d="M64 128 V96" stroke="#9AA3B5" stroke-width="4.5"/>
<rect x="18" y="20" width="92" height="64" rx="6" fill="#fff" {W(3.2)}/>
<rect x="46" y="52" width="36" height="28" fill="none" stroke="#E8344E" stroke-width="3"/>
{eye(46, 38, .8)}{eye(82, 38, .8)}{blush(38, 46)}{blush(90, 46)}
<path d="M42 82 L48 106 H80 L86 82" fill="none" {W(2)}/>
<path d="M46 90 H82 M48 98 H80 M52 82 L56 106 M64 82 V106 M76 82 L72 106" fill="none" {W(1.4)} opacity=".7"/>
<ellipse cx="64" cy="82" rx="24" ry="5" fill="none" {W(6)}/><ellipse cx="64" cy="82" rx="24" ry="5" fill="none" stroke="#E8344E" stroke-width="3"/>
<circle cx="80" cy="66" r="13" fill="{BB}" {W(2.8)}/>{bline(80, 66, 13)}
<path d="M98 58 q4 4 2 10 M102 52 q6 6 3 16" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# «Хаски», Генерала Антонова — собачья будка с кольцом над входом, из будки вылетает мяч, торчат уши
I["husky-basket-antonova"] = (
    "деревянная собачья будка с баскетбольным кольцом над входом",
    "из тёмного входа выглядывают голубые глаза и острые ушки, мяч выпрыгивает наружу",
    ("#FFE0EC", "#E06C9A"), f'''
<path d="M-4 110 H132 V132 H-4Z" fill="#fff" opacity=".7"/>
<path d="M18 58 L64 22 L110 58Z" fill="#D2553E" {W(3.2)}/>
<rect x="26" y="56" width="76" height="56" fill="#E8B06A" {W(3.2)}/>
<path d="M26 72 H102 M26 88 H102" {W(1.6)} opacity=".45"/>
<path d="M46 112 V88 Q46 72 64 72 Q82 72 82 88 V112Z" fill="#3B3355" {W(3)}/>
<path d="M52 86 L54 76 L60 84Z M76 86 L74 76 L68 84Z" fill="#9AA3B5" {W(1.8)}/>
<circle cx="58" cy="92" r="3.4" fill="#7FD3FF"/><circle cx="70" cy="92" r="3.4" fill="#7FD3FF"/>
<circle cx="58" cy="92" r="1.4" fill="{O}"/><circle cx="70" cy="92" r="1.4" fill="{O}"/>
<ellipse cx="64" cy="99" rx="2.6" ry="2" fill="#fff"/>
<rect x="56" y="44" width="16" height="10" rx="1" fill="#fff" {W(2.2)}/>
<ellipse cx="64" cy="56" rx="10" ry="2.8" fill="none" stroke="#E8344E" stroke-width="3"/>
<circle cx="104" cy="30" r="12" fill="{BB}" {W(2.8)}/>{bline(104, 30, 12)}
<path d="M88 46 q4 -4 6 -8" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# «Хаски», Войковская — мяч мчится на деревянных санках с ледяной горки
I["husky-basket-voykovskaya"] = (
    "баскетбольный мяч на деревянных санках",
    "с визгом мчится с заснеженной горки, за ним вихрь снежинок",
    ("#F0F8FF", "#7A9CC6"), f'''
<path d="M-4 54 Q50 70 132 118 V132 H-4Z" fill="#fff" {W(3)}/>
{sparkle(20, 30, 5)}{sparkle(34, 46, 3)}{sparkle(110, 30, 4)}
<circle cx="24" cy="66" r="3" fill="#fff" {W(1.6)}/><circle cx="14" cy="58" r="2" fill="#fff" {W(1.4)}/>
<path d="M44 88 L96 110 Q106 114 106 106" fill="none" {W(3.4)}/>
<path d="M48 76 L90 94 L86 102 L44 84Z" fill="#C9874A" {W(3)}/>
<path d="M54 86 L52 94 M80 98 L78 104" {W(2.6)}/>
<path d="M44 82 Q36 78 40 70" fill="none" {W(2.4)}/>
<circle cx="70" cy="62" r="22" fill="{BB}" {W(3.2)}/>{bline(70, 62, 22)}
{eye(63, 58, .8)}{eye(78, 58, .8)}
<path d="M64 68 Q70 76 78 68 Z" fill="{O}"/>
<path d="M40 56 L30 54 M40 64 L28 64" stroke="#fff" stroke-width="3" stroke-linecap="round"/>''')

# РБА, школа «Логос» — мяч сладко спит в сетке кольца, как в гамаке
I["rba-basket-logos"] = (
    "сетка баскетбольного кольца, растянутая как гамак",
    "в ней сладко спит баскетбольный мяч, над ним «z-z»",
    ("#D8FFF3", "#3BB89A"), f'''
<path d="M10 28 L118 28" {W(4)}/><path d="M10 28 L118 28" stroke="#E8344E" stroke-width="2"/>
<path d="M14 28 Q64 120 114 28" fill="#fff" fill-opacity=".35" {W(2.4)}/>
<path d="M22 28 Q64 104 106 28 M34 28 Q64 88 94 28 M14 28 L44 92 M34 28 L56 98 M64 28 V100 M94 28 L72 98 M114 28 L84 92" fill="none" {W(1.6)} opacity=".75"/>
<circle cx="64" cy="70" r="24" fill="{BB}" {W(3.2)}/>{bline(64, 70, 24)}
<path d="M52 68 Q56 72 60 68 M68 68 Q72 72 76 68" fill="none" {W(2.4)}/>{blush(50, 76)}{blush(78, 76)}
<path d="M60 80 Q64 83 68 80" fill="none" {W(2.2)}/>
<text x="92" y="58" font-family="Arial Black,Arial" font-weight="900" font-size="12" fill="#fff" stroke="{O}" stroke-width="1">z</text>
<text x="100" y="46" font-family="Arial Black,Arial" font-weight="900" font-size="16" fill="#fff" stroke="{O}" stroke-width="1">Z</text>''')

# РБА, «Сколка» (Сколково) — лампочка-идея, внутри вместо нити баскетбольный мяч
I["rba-basket-skolka"] = (
    "лампочка-изобретатель, внутри которой светится баскетбольный мяч",
    "загорелась идеей и сияет лучами над синим цоколем",
    ("#E0F4FF", "#2B86C9"), f'''
<path d="M64 10 V18 M30 22 L36 28 M98 22 L92 28 M18 52 H26 M102 52 H110" stroke="#FFE27A" stroke-width="4" stroke-linecap="round"/>
<path d="M64 20 Q94 20 94 52 Q94 70 80 82 V92 H48 V82 Q34 70 34 52 Q34 20 64 20Z" fill="#FFF7C8" {W(3.2)}/>
<circle cx="64" cy="52" r="20" fill="{BB}" {W(2.8)}/>{bline(64, 52, 20)}
<path d="M44 34 Q40 42 42 50" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/>
{eye(57, 50, .7)}{eye(71, 50, .7)}{smile(64, 57, 4)}
<rect x="46" y="92" width="36" height="8" rx="2" fill="#5A6E8C" {W(2.6)}/>
<rect x="48" y="100" width="32" height="8" rx="2" fill="#5A6E8C" {W(2.6)}/>
<path d="M54 108 H74 L70 116 H58Z" fill="#3B3355"/>''')

# РБА, Арена «Небо» — облако с кольцом, мяч взлетает в небе
I["rba-basket-nebo"] = (
    "пухлое облако с баскетбольным кольцом сбоку",
    "мяч взмывает в закатном небе прямо в кольцо на облаке",
    ("#FFE3C9", "#F07A6A"), f'''
<path d="M30 54 Q22 54 22 44 Q22 32 36 34 Q40 20 56 24 Q66 12 80 22 Q96 20 98 34 Q110 36 106 48 Q104 56 94 54Z" fill="#fff" {W(3)}/>
{eye(52, 40, .7)}{eye(70, 40, .7)}{blush(46, 47)}{blush(76, 47)}{smile(61, 46, 4)}
<rect x="88" y="44" width="5" height="16" fill="#fff" {W(2)}/>
<path d="M78 60 L82 74 H100 L104 60" fill="none" {W(1.8)}/><path d="M80 66 H102 M88 60 L90 74 M96 60 L94 74" {W(1.2)} opacity=".7"/>
<ellipse cx="91" cy="60" rx="14" ry="3.5" fill="none" {W(5.5)}/><ellipse cx="91" cy="60" rx="14" ry="3.5" fill="none" stroke="#E8344E" stroke-width="2.6"/>
<path d="M30 116 Q40 90 58 84" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="4 5" stroke-linecap="round"/>
<circle cx="66" cy="88" r="15" fill="{BB}" {W(2.8)}/>{bline(66, 88, 15)}
{sparkle(18, 80, 4)}{sparkle(112, 96, 5)}''')

# РБА, SportVille (Нахабино) — лось ловит мяч в рога, как в корзину
I["rba-basket-sportville"] = (
    "лось с широкими рогами-лопатами",
    "поймал баскетбольный мяч прямо в рога, как в корзину, на опушке у ёлок",
    ("#E6F5D4", "#4E8A3A"), f'''
<path d="M10 100 L20 70 L30 100Z M100 104 L112 66 L124 104Z" fill="#2F7A4A" {W(2.4)}/>
<path d="M-4 104 Q64 96 132 104 V132 H-4Z" fill="#B7E08A" {W(2.4)}/>
<path d="M50 56 Q30 56 26 40 Q24 32 30 30 L34 38 L36 26 L42 36 L46 26 L50 40 Q52 48 58 50Z" fill="#E8C48A" {W(2.8)}/>
<path d="M78 56 Q98 56 102 40 Q104 32 98 30 L94 38 L92 26 L86 36 L82 26 L78 40 Q76 48 70 50Z" fill="#E8C48A" {W(2.8)}/>
<circle cx="64" cy="34" r="15" fill="{BB}" {W(2.8)}/>{bline(64, 34, 15)}
<path d="M48 120 V96 Q46 74 64 72 Q82 74 80 96 V120" fill="#9A5E34" {W(3)}/>
<ellipse cx="64" cy="70" rx="16" ry="16" fill="#9A5E34" {W(3)}/>
<path d="M50 72 Q50 98 64 100 Q78 98 78 72" fill="#9A5E34" {W(3)}/>
<ellipse cx="64" cy="94" rx="12" ry="9" fill="#C98A5C" {W(2.6)}/>
<circle cx="59" cy="94" r="1.8" fill="{O}"/><circle cx="69" cy="94" r="1.8" fill="{O}"/>
{eye(57, 72, .6)}{eye(71, 72, .6)}
<ellipse cx="44" cy="64" rx="7" ry="3.5" fill="#9A5E34" {W(2.2)} transform="rotate(-25 44 64)"/>
<ellipse cx="84" cy="64" rx="7" ry="3.5" fill="#9A5E34" {W(2.2)} transform="rotate(25 84 64)"/>
<path d="M60 102 Q64 105 68 102" fill="none" {W(2)}/>''')

# РБА, школа № 875 — здание школы с баскетбольным кольцом над дверью, мяч летит в кольцо
I["rba-basket-school875"] = (
    "кирпично-жёлтое здание школы с часами на фронтоне и кольцом над дверью",
    "мяч влетает в кольцо над входом, окна-глазки радостно смотрят",
    ("#E3EEFF", "#7C8FD6"), f'''
<path d="M-4 112 H132 V132 H-4Z" fill="#9AA3B5"/>
<path d="M14 112 V52 H114 V112Z" fill="#FFD27A" {W(3.2)}/>
<path d="M8 54 L64 24 L120 54Z" fill="#D2553E" {W(3)}/>
<circle cx="64" cy="42" r="7" fill="#fff" {W(2.2)}/><path d="M64 38 V42 L67 44" fill="none" {W(1.8)}/>
<rect x="22" y="62" width="18" height="16" rx="2" fill="#BEE7FF" {W(2.4)}/><rect x="88" y="62" width="18" height="16" rx="2" fill="#BEE7FF" {W(2.4)}/>
{eye(31, 70, .55)}{eye(97, 70, .55)}
<rect x="22" y="86" width="18" height="16" rx="2" fill="#BEE7FF" {W(2.4)}/><rect x="88" y="86" width="18" height="16" rx="2" fill="#BEE7FF" {W(2.4)}/>
<path d="M52 112 V90 Q52 82 64 82 Q76 82 76 90 V112Z" fill="#8C5A33" {W(2.8)}/>
<rect x="58" y="62" width="12" height="9" fill="#fff" {W(2)}/>
<path d="M54 72 L57 80 H71 L74 72" fill="none" {W(1.6)}/>
<ellipse cx="64" cy="72" rx="10" ry="2.6" fill="none" {W(5)}/><ellipse cx="64" cy="72" rx="10" ry="2.6" fill="none" stroke="#E8344E" stroke-width="2.4"/>
<circle cx="78" cy="56" r="10" fill="{BB}" {W(2.6)}/>{bline(78, 56, 10)}
<path d="M90 36 Q86 42 86 48" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 4" stroke-linecap="round"/>''')

# JUNIBASKET, Тимирязевская (рядом агроакадемия) — кактус в горшке зацвёл баскетбольным мячом
I["junibasket-timiryazevskaya"] = (
    "колючий кактус в терракотовом горшке",
    "на его макушке распустился баскетбольный мяч вместо цветка, кактус гордо улыбается",
    ("#FBFFE0", "#C9C24A"), f'''
<path d="M38 92 H90 L84 120 H44Z" fill="#D9774A" {W(3)}/><rect x="34" y="86" width="60" height="10" rx="3" fill="#E98B5C" {W(3)}/>
<path d="M50 86 V56 Q50 42 64 42 Q78 42 78 56 V86Z" fill="#5CB85C" {W(3)}/>
<path d="M50 70 H40 Q34 70 34 62 V54" fill="none" {W(9)}/><path d="M50 70 H40 Q34 70 34 62 V54" fill="none" stroke="#5CB85C" stroke-width="5.5" stroke-linecap="round"/>
<path d="M78 64 H88 Q94 64 94 56 V50" fill="none" {W(9)}/><path d="M78 64 H88 Q94 64 94 56 V50" fill="none" stroke="#5CB85C" stroke-width="5.5" stroke-linecap="round"/>
<path d="M56 50 l-3 -2 M72 52 l3 -2 M54 80 l-3 1 M75 78 l3 1 M64 82 v3" {W(1.6)}/>
{eye(58, 64, .65)}{eye(70, 64, .65)}{blush(53, 70, .8)}{blush(75, 70, .8)}{smile(64, 71, 3.5)}
<path d="M50 36 Q44 30 48 22 M78 36 Q84 30 80 22" fill="none" {W(2.4)}/>
<circle cx="64" cy="26" r="16" fill="{BB}" {W(2.8)}/>{bline(64, 26, 16)}
{sparkle(24, 32, 5)}{sparkle(104, 24, 4)}''')

# JUNIBASKET, Мытищи — мальчик в оранжевой повязке крутит мяч на пальце
I["junibasket-mytishchi"] = (
    "мальчик с оранжевой спортивной повязкой на лбу и в майке №5",
    "крутит баскетбольный мяч на указательном пальце, мяч оставляет круги вращения",
    ("#FFF0E8", "#F59A6A"), f'''
<path d="M30 126 Q32 96 64 92 Q96 96 98 126Z" fill="#2B8FD6" {W(3)}/>
<text x="64" y="120" text-anchor="middle" font-family="Arial Black,Arial" font-weight="900" font-size="18" fill="#fff">5</text>
<path d="M50 92 Q64 102 78 92" fill="none" stroke="#fff" stroke-width="2.4"/>
<path d="M92 100 Q100 70 92 48" fill="none" {W(9)}/><path d="M92 100 Q100 70 92 48" fill="none" stroke="#F5C9A0" stroke-width="5.5" stroke-linecap="round"/>
<circle cx="64" cy="66" r="22" fill="#F5C9A0" {W(3)}/>
<path d="M42 62 Q42 40 64 40 Q86 40 86 62 Q80 52 64 52 Q48 52 42 62Z" fill="#5A3A22" {W(2.6)}/>
<rect x="42" y="52" width="44" height="7" rx="3" fill="#FF8A2E" {W(2.2)}/>
{eye(56, 66, .65)}{eye(72, 66, .65)}{blush(50, 73, .8)}{blush(78, 73, .8)}
<path d="M58 75 Q64 80 70 75" fill="none" {W(2.2)}/>
<circle cx="92" cy="28" r="15" fill="{BB}" {W(2.8)}/>{bline(92, 28, 15)}
<path d="M72 26 Q74 12 92 10 M112 30 Q110 44 96 46" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')


# ───────────────────────── ГИМНАСТИКА ─────────────────────────

# Перевозников, Красногорск — мальчик на кольцах держит «крест»
I["perevoznikov-krasnogorsk"] = (
    "мальчик-гимнаст в белой майке и синих брюках",
    "держит «крест» на гимнастических кольцах, руки в стороны, сосредоточенно улыбается",
    ("#E0E6FF", "#5160C4"), f'''
<path d="M18 -4 V36 M110 -4 V36" {W(3)}/>
<circle cx="18" cy="44" r="9" fill="none" {W(6)}/><circle cx="18" cy="44" r="9" fill="none" stroke="#C9874A" stroke-width="3"/>
<circle cx="110" cy="44" r="9" fill="none" {W(6)}/><circle cx="110" cy="44" r="9" fill="none" stroke="#C9874A" stroke-width="3"/>
<path d="M26 46 H102" fill="none" {W(10)}/><path d="M26 46 H102" fill="none" stroke="#F5C9A0" stroke-width="6.5" stroke-linecap="round"/>
<path d="M52 46 H76 L74 78 H54Z" fill="#fff" {W(3)}/>
<path d="M54 78 H74 L72 116 H66 L64 92 L62 116 H56Z" fill="#2B4FA8" {W(3)}/>
<ellipse cx="59" cy="118" rx="5" ry="3" fill="#fff" {W(2)}/><ellipse cx="69" cy="118" rx="5" ry="3" fill="#fff" {W(2)}/>
<circle cx="64" cy="30" r="13" fill="#F5C9A0" {W(3)}/>
<path d="M51 28 Q52 16 64 16 Q76 16 77 28 Q70 22 64 22 Q58 22 51 28Z" fill="#E0A23A" {W(2.4)}/>
{eye(59, 31, .5)}{eye(69, 31, .5)}{blush(55, 36, .6)}{blush(73, 36, .6)}<path d="M61 37 H67" {W(2)}/>
{sparkle(30, 90, 5)}{sparkle(100, 96, 4)}''')

# Перевозников, Видное — девочка делает «колесо» на голубом ковре
I["perevoznikov-vidnoe"] = (
    "девочка-гимнастка с рыжим пучком в жёлтом купальнике",
    "делает «колесо» на голубом ковре, за ней дуга из звёздочек",
    ("#FFF7D6", "#F2B636"), f'''
<path d="M-4 104 Q64 96 132 104 V132 H-4Z" fill="#7FC6F2" {W(2.6)}/>
<path d="M16 86 Q30 30 64 26 Q98 30 112 86" fill="none" stroke="#fff" stroke-width="2.6" stroke-dasharray="2 6" stroke-linecap="round"/>
<path d="M64 74 L40 102" {W(8)}/><path d="M64 74 L40 102" stroke="#F5C9A0" stroke-width="4.5" stroke-linecap="round"/>
<path d="M64 74 L88 102" {W(8)}/><path d="M64 74 L88 102" stroke="#F5C9A0" stroke-width="4.5" stroke-linecap="round"/>
<path d="M58 54 L34 26" {W(8)}/><path d="M58 54 L34 26" stroke="#F5C9A0" stroke-width="4.5" stroke-linecap="round"/>
<path d="M70 54 L94 26" {W(8)}/><path d="M70 54 L94 26" stroke="#F5C9A0" stroke-width="4.5" stroke-linecap="round"/>
<path d="M54 50 Q64 44 74 50 L72 74 Q64 80 56 74Z" fill="#FFD23A" {W(3)}/>
<circle cx="64" cy="88" r="11" fill="#F5C9A0" {W(2.8)}/>
<path d="M53 86 Q54 98 64 99 Q74 98 75 86 Q70 92 64 92 Q58 92 53 86Z" fill="#E0703A" {W(2.2)}/>
<circle cx="64" cy="103" r="5" fill="#E0703A" {W(2)}/>
<path d="M60 82 Q61 80 62 82 M66 82 Q67 80 68 82" fill="none" {W(1.8)}/>
<path d="M61 77 Q64 75 67 77" fill="none" {W(1.8)}/>
{sparkle(16, 86, 5)}{sparkle(112, 86, 5)}{sparkle(64, 18, 4)}''')

# Перевозников, Пушкино — девочка на разновысоких брусьях в розовом купальнике
I["perevoznikov-pushkino"] = (
    "девочка-гимнастка в малиновом купальнике с белыми звёздами",
    "висит на верхней жерди разновысоких брусьев и тянет носочки к нижней",
    ("#E8FFF4", "#4CB88A"), f'''
<path d="M24 120 V30 M104 120 V60" {W(3.2)}/>
<path d="M14 30 H104" {W(5)}/><path d="M14 30 H104" stroke="#F0E0C0" stroke-width="2.4"/>
<path d="M14 60 H114" {W(5)}/><path d="M14 60 H114" stroke="#F0E0C0" stroke-width="2.4"/>
<path d="M24 120 L14 120 M24 120 L34 120 M104 120 L94 120 M104 120 L114 120" {W(3.2)}/>
<path d="M58 30 L60 44 M70 30 L68 44" {W(7)}/><path d="M58 30 L60 44 M70 30 L68 44" stroke="#F5C9A0" stroke-width="3.6" stroke-linecap="round"/>
<circle cx="58" cy="30" r="3" fill="#F5C9A0" {W(1.8)}/><circle cx="70" cy="30" r="3" fill="#F5C9A0" {W(1.8)}/>
<circle cx="64" cy="54" r="10" fill="#F5C9A0" {W(2.8)}/>
<path d="M54 52 Q56 42 64 42 Q72 42 74 52 Q70 46 64 46 Q58 46 54 52Z" fill="#3A2A1C" {W(2)}/>
<circle cx="64" cy="40" r="4" fill="#3A2A1C" {W(1.8)}/>
{eye(60, 55, .4)}{eye(68, 55, .4)}<path d="M61 59 Q64 61 67 59" fill="none" {W(1.6)}/>
<path d="M56 66 Q64 62 72 66 L76 84 Q66 90 58 86Z" fill="#E0306A" {W(3)}/>
{sparkle(64, 74, 3)}
<path d="M62 86 L84 92 M70 86 L92 88" {W(7)}/><path d="M62 86 L84 92 M70 86 L92 88" stroke="#F5C9A0" stroke-width="3.6" stroke-linecap="round"/>
<path d="M84 92 L96 96 M92 88 L104 88" stroke="#F5C9A0" stroke-width="3" stroke-linecap="round"/>
{sparkle(108, 40, 5)}''')

# Перевозников, Химки — рыжий котёнок стоит на руках на бревне
I["perevoznikov-khimki"] = (
    "рыжий полосатый котёнок-гимнаст",
    "стоит на передних лапках на гимнастическом бревне, хвост держит равновесие",
    ("#F5E6FF", "#B07CDB"), f'''
<rect x="10" y="88" width="108" height="10" rx="4" fill="#E9D3B0" {W(3)}/>
<path d="M30 98 L26 124 M98 98 L102 124" {W(4)}/>
<path d="M54 86 V72 M74 86 V72" {W(8)}/><path d="M54 86 V72 M74 86 V72" stroke="#F59A3A" stroke-width="4.5" stroke-linecap="round"/>
<ellipse cx="54" cy="87" rx="4.5" ry="2.6" fill="#fff" {W(1.8)}/><ellipse cx="74" cy="87" rx="4.5" ry="2.6" fill="#fff" {W(1.8)}/>
<ellipse cx="64" cy="48" rx="15" ry="22" fill="#F59A3A" {W(3)}/>
<path d="M52 40 H58 M70 40 H76 M51 50 H58 M70 50 H77" {W(2)} opacity=".6"/>
<path d="M56 28 L58 14 M72 28 L70 14" {W(8)}/><path d="M56 28 L58 14 M72 28 L70 14" stroke="#F59A3A" stroke-width="4.5" stroke-linecap="round"/>
<path d="M64 26 Q84 10 96 22 Q104 30 96 36" fill="none" {W(7)}/><path d="M64 26 Q84 10 96 22 Q104 30 96 36" fill="none" stroke="#F59A3A" stroke-width="3.6" stroke-linecap="round"/>
<circle cx="64" cy="70" r="0"/>
<g transform="translate(0,0)">
<path d="M50 74 L46 62 L56 68Z M78 74 L82 62 L72 68Z" fill="#F59A3A" {W(2.4)}/>
</g>
<ellipse cx="64" cy="76" rx="16" ry="12" fill="#F59A3A" {W(3)}/>
<path d="M58 70 Q61 67 64 70 M64 70 Q67 67 70 70" fill="none" {W(1.6)} opacity=".6"/>
{eye(58, 78, .55)}{eye(70, 78, .55)}<path d="M62 74 L64 72.5 L66 74Z" fill="#FF7FA8"/>
<path d="M61 83 Q64 81 67 83" fill="none" {W(1.6)}/>
{sparkle(24, 60, 5)}{sparkle(106, 66, 4)}''')


# ───────────────────────── ЕДИНОБОРСТВА ─────────────────────────

# ДСШ Яковлева, Железнодорожный (дзюдо) — зубр в белом кимоно кланяется на татами
I["yakovlev-balashiha-sovetskaya"] = (
    "могучий бурый зубр в белом кимоно с жёлтым поясом",
    "склонил рогатую голову в поклоне «рэй» у красной границы татами",
    ("#E2F5EA", "#3E8E62"), f'''
<path d="M-4 100 L132 100 V132 H-4Z" fill="#58B36E" {W(2.6)}/><path d="M-4 112 H132" stroke="#E8344E" stroke-width="3"/>
<path d="M36 100 Q30 70 52 58 H84 Q104 66 98 100Z" fill="#fff" {W(3)}/>
<path d="M60 58 L70 80 L82 58" fill="none" {W(2.4)}/>
<rect x="36" y="80" width="62" height="7" fill="#FFD23A" {W(2.4)}/>
<path d="M62 87 L56 100 M70 87 L76 100" stroke="#FFD23A" stroke-width="4" stroke-linecap="round"/>
<path d="M28 58 Q22 42 34 34 Q40 50 38 56Z" fill="#6B4528" {W(2.6)}/>
<ellipse cx="44" cy="58" rx="22" ry="18" fill="#7A4E2C" {W(3)}/>
<path d="M28 42 Q24 30 30 24 M58 44 Q66 34 62 26" fill="none" {W(5)}/><path d="M28 42 Q24 30 30 24 M58 44 Q66 34 62 26" fill="none" stroke="#F3E6C8" stroke-width="2.4" stroke-linecap="round"/>
<path d="M30 46 Q44 34 58 46 Q50 42 44 44 Q36 42 30 46Z" fill="#4A2E18"/>
<ellipse cx="40" cy="68" rx="12" ry="8" fill="#9A6A44" {W(2.4)}/><circle cx="36" cy="68" r="1.6" fill="{O}"/><circle cx="44" cy="68" r="1.6" fill="{O}"/>
<path d="M34 56 Q37 58 40 56 M48 56 Q51 58 54 56" fill="none" {W(2)}/>
<path d="M50 84 Q44 92 50 100" fill="none" {W(7)}/><path d="M50 84 Q44 92 50 100" fill="none" stroke="#fff" stroke-width="3.6" stroke-linecap="round"/>
{sparkle(108, 30, 5)}''')

# ДСШ Яковлева, Королёв-Юбилейный (тхэквондо) — мальчик в шлеме в прыжке бьёт ногой, на небе ракета Королёва
I["yakovlev-korolev-yubileyny"] = (
    "мальчик-тхэквондист в белом добоке и синем защитном шлеме",
    "в высоком прыжке бьёт ногой по красной лапе тренера, вдали взлетает ракета",
    ("#DDE8FF", "#3A62B8"), f'''
<path d="M104 52 L108 34 L112 52Z" fill="#fff" {W(2)}/><path d="M104 52 Q108 62 112 52" fill="#FFB43A"/>
<path d="M108 62 Q104 80 110 100" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="2 4" opacity=".8"/>
<path d="M58 82 L36 104" {W(9)}/><path d="M58 82 L36 104" stroke="#fff" stroke-width="5.5" stroke-linecap="round"/>
<path d="M64 76 L96 54" {W(9)}/><path d="M64 76 L96 54" stroke="#fff" stroke-width="5.5" stroke-linecap="round"/>
<ellipse cx="98" cy="52" rx="4" ry="3" fill="#F5C9A0" {W(2)}/>
<path d="M90 40 Q100 30 108 38 Q104 48 94 50Z" fill="#E8344E" {W(2.6)}/>
<path d="M46 56 Q56 50 66 56 L68 80 Q58 86 48 80Z" fill="#fff" {W(3)}/>
<path d="M52 56 L57 66 L62 56" fill="none" {W(2)}/>
<rect x="46" y="72" width="22" height="5" fill="{O}"/>
<path d="M48 60 L32 70 M66 60 L80 50" {W(8)}/><path d="M48 60 L32 70 M66 60 L80 50" stroke="#fff" stroke-width="4.5" stroke-linecap="round"/>
<circle cx="31" cy="71" r="4" fill="#F5C9A0" {W(2)}/><circle cx="81" cy="49" r="4" fill="#F5C9A0" {W(2)}/>
<circle cx="54" cy="38" r="14" fill="#2F6FDE" {W(3)}/>
<ellipse cx="55" cy="42" rx="9" ry="8" fill="#F5C9A0" {W(2.2)}/>
{eye(52, 41, .45)}{eye(59, 41, .45)}<path d="M53 46 Q56 48 59 46" fill="none" {W(1.6)}/>
{sparkle(22, 30, 5)}{sparkle(30, 112, 4)}''')

# «Русский самурай», Раменское — хорёк в белом кимоно и ушанке в боевой стойке
I["rusamurai-ramenskoe-saturn"] = (
    "белый хорёк в кимоно с чёрным поясом и шапке-ушанке",
    "стоит в боевой стойке на татами под падающими лепестками",
    ("#FFE8E0", "#C94A3A"), f'''
<path d="M-4 104 H132 V132 H-4Z" fill="#E9D3A0" {W(2.4)}/><path d="M40 104 V132 M88 104 V132" {W(1.6)} opacity=".4"/>
<path d="M50 104 L42 86 M78 104 L86 86" {W(8)}/><path d="M50 104 L42 86 M78 104 L86 86" stroke="#fff" stroke-width="4.5" stroke-linecap="round"/>
<path d="M44 88 Q42 62 64 58 Q86 62 84 88Z" fill="#fff" {W(3)}/>
<path d="M56 60 L64 76 L72 60" fill="none" {W(2.2)}/>
<rect x="44" y="76" width="40" height="6" fill="{O}"/><path d="M60 82 L56 94 M68 82 L72 94" stroke="{O}" stroke-width="4" stroke-linecap="round"/>
<path d="M46 66 L28 56 M82 66 L100 72" {W(8)}/><path d="M46 66 L28 56 M82 66 L100 72" stroke="#fff" stroke-width="4.5" stroke-linecap="round"/>
<circle cx="27" cy="55" r="5" fill="#F4ECE0" {W(2)}/><circle cx="101" cy="73" r="5" fill="#F4ECE0" {W(2)}/>
<ellipse cx="64" cy="44" rx="17" ry="14" fill="#F4ECE0" {W(3)}/>
<path d="M54 42 Q58 36 62 42 M66 42 Q70 36 74 42" fill="#8C7A66" opacity=".55"/>
{eye(57, 43, .55)}{eye(71, 43, .55)}<ellipse cx="64" cy="50" rx="2.6" ry="2" fill="#FF7FA8" {W(1.4)}/>
<path d="M60 53 Q64 55.5 68 53" fill="none" {W(1.6)}/>
<path d="M54 50 L42 48 M54 52 L43 54 M74 50 L86 48 M74 52 L85 54" {W(1.2)}/>
<path d="M44 38 Q44 18 64 18 Q84 18 84 38 Z" fill="#7A5A3E" {W(3)}/>
<path d="M44 32 Q40 44 44 52 L50 50 Q48 42 50 34Z M84 32 Q88 44 84 52 L78 50 Q80 42 78 34Z" fill="#B88A5E" {W(2.4)}/>
<rect x="44" y="30" width="40" height="8" rx="4" fill="#B88A5E" {W(2.4)}/>
<circle cx="64" cy="24" r="3" fill="#E8344E" {W(1.6)}/>
<ellipse cx="20" cy="22" rx="4" ry="2.4" fill="#FFB8C8" transform="rotate(-30 20 22)"/><ellipse cx="108" cy="40" rx="4" ry="2.4" fill="#FFB8C8" transform="rotate(20 108 40)"/>
<ellipse cx="96" cy="16" rx="3.5" ry="2" fill="#FFB8C8"/>''')


if __name__ == "__main__":
    for pid, (hero, scene, (a, b), body) in I.items():
        open(os.path.join(ROOT, "icons-src", f"{pid}.svg"), "w").write(bgsvg(a, b, body))
    reg = os.path.join(ROOT, "icons-src", "subjects.txt"); txt = open(reg, encoding="utf-8").read()
    for pid in I:
        txt = re.sub(rf"^{re.escape(pid)} — .*\n", "", txt, flags=re.M)
    if not txt.endswith("\n"):
        txt += "\n"
    txt += "".join(f"{pid} — герой: {h} | сцена: {sc}\n" for pid, (h, sc, _, _) in I.items())
    open(reg, "w", encoding="utf-8").write(txt)
    print(" ".join(I))
