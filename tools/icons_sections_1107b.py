"""Иконки робота sections, 2026-11-07 (00 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно —
свой герой, своя сцена, своя компоновка и палитра. Якорь вида спорта читается сразу (шахматы — фигуры и клетчатая доска,
баскетбол — оранжевый мяч с линиями и кольцо, бадминтон — волан и ракетка, настольный теннис — красная ракетка и шарик,
фехтование — шпага и белый костюм, танцы — пышная юбка/кроссовки и ноты, футбол — мяч).
Сверено с листами icons-catalog/sheet-01..27 и icons-src/subjects.txt.
Запуск: python3 tools/icons_sections_1107b.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
W = lambda w: s(f'stroke-width="{w}"')
PINK, GOLD, RED, BLUE, ORG = "#FF7FA8", "#FFC93C", "#E8554A", "#5CB7F2", "#F28C38"
LIGHT, DARK = "#FFF7EC", "#4A4466"
ICONS, SUBJ = {}, {}


def board(x, y, n, c, a="#FFF7EC", b="#8A6A55", w=3):
    """шахматная доска n×n клеток размера c, левый верх (x, y)"""
    out = f'<rect x="{x}" y="{y}" width="{n*c}" height="{n*c}" fill="{a}"/>'
    for i in range(n):
        for j in range(n):
            if (i + j) % 2:
                out += f'<rect x="{x+i*c}" y="{y+j*c}" width="{c}" height="{c}" fill="{b}"/>'
    return out + f'<rect x="{x}" y="{y}" width="{n*c}" height="{n*c}" fill="none" {W(w)}/>'


def knight(c=LIGHT, c2="#E9DCC8", ew=O):
    """шахматный конь вокруг (0,0), высота ~92"""
    return (f'<rect x="-30" y="34" width="60" height="12" rx="4" fill="{c}" {W(3)}/>'
            f'<rect x="-22" y="22" width="44" height="14" rx="3" fill="{c2}" {W(3)}/>'
            f'<path d="M-18 22 C-24 2 -20 -18 -10 -30 L-14 -46 L0 -36 C20 -38 34 -24 32 -6 L20 -4 C12 -4 8 0 12 8 C16 14 20 18 22 22Z" fill="{c}" {W(3)}/>'
            f'<path d="M-6 -32 Q-14 -16 -12 2" fill="none" stroke="{c2}" stroke-width="5"/>'
            f'<ellipse cx="10" cy="-22" rx="4.4" ry="5.2" fill="{ew}"/><circle cx="8.6" cy="-24" r="1.7" fill="#fff"/>'
            f'<ellipse cx="18" cy="-12" rx="5" ry="3" fill="{PINK}" opacity=".7"/><circle cx="28" cy="-10" r="1.6" fill="{O}"/>')


def pawn(c=LIGHT, c2="#E9DCC8", k=1.0):
    return (f'<g transform="scale({k})"><rect x="-26" y="34" width="52" height="11" rx="4" fill="{c}" {W(3)}/>'
            f'<path d="M-21 36 Q-16 12 -9 2 H9 Q16 12 21 36Z" fill="{c}" {W(3)}/>'
            f'<rect x="-15" y="-4" width="30" height="8" rx="4" fill="{c2}" {W(3)}/><circle cx="0" cy="-22" r="19" fill="{c}" {W(3)}/></g>')


def bball(cx, cy, r, fc=True, d=None, k=None):
    """баскетбольный мяч"""
    d = d or r * 0.27
    k = k or r / 34
    q = r * 0.65
    out = (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{ORG}" {W(3)}/>'
           f'<path d="M{cx-r} {cy} H{cx+r} M{cx} {cy-r} V{cy+r}" fill="none" {W(2.2)}/>'
           f'<path d="M{cx-q} {cy-r*0.76} Q{cx-r*0.22} {cy} {cx-q} {cy+r*0.76} M{cx+q} {cy-r*0.76} Q{cx+r*0.22} {cy} {cx+q} {cy+r*0.76}" fill="none" {W(2.2)}/>')
    if fc:
        out += face(cx, cy + r * 0.12, d=d, k=k)
    return out


def hoop(x, y, w=40, board=True):
    """щит с кольцом и сеткой; x,y — центр кольца"""
    out = ""
    if board:
        out += (f'<rect x="{x-w*0.6}" y="{y-w*0.75}" width="{w*1.2}" height="{w*0.8}" rx="3" fill="#fff" {W(3)}/>'
                f'<rect x="{x-w*0.22}" y="{y-w*0.42}" width="{w*0.44}" height="{w*0.4}" fill="none" stroke="{RED}" stroke-width="2.6"/>')
    hw = w * 0.42
    net = "".join(f'<path d="M{x-hw+i*hw/2:.1f} {y} L{x-hw*0.6+i*hw*0.3:.1f} {y+w*0.45:.1f}" stroke="#fff" stroke-width="2"/>' for i in range(5))
    out += (f'<path d="M{x-hw} {y} L{x-hw*0.6:.1f} {y+w*0.45:.1f} H{x+hw*0.6:.1f} L{x+hw} {y}" fill="none" {W(2)}/>' + net
            + f'<path d="M{x-hw*0.8:.1f} {y+w*0.2:.1f} H{x+hw*0.8:.1f}" stroke="#fff" stroke-width="1.6"/>'
            f'<ellipse cx="{x}" cy="{y}" rx="{hw}" ry="4" fill="none" stroke="{O}" stroke-width="6"/>'
            f'<ellipse cx="{x}" cy="{y}" rx="{hw}" ry="4" fill="none" stroke="{RED}" stroke-width="3"/>')
    return out


def add(pid, bg, body, hero, scene):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


# ============================== ШАХМАТЫ ==============================
# «Максимум» в ТРК «Нора»: конь выглядывает из норки в клетчатом холме
add("chessmax-nora", "green",
    '<path d="M-10 92 Q64 30 138 92 V140 H-10Z" fill="#8FD07A" stroke="#3B3355" stroke-width="3"/>'
    + '<clipPath id="hill"><path d="M-10 92 Q64 30 138 92 V140 H-10Z"/></clipPath><g clip-path="url(#hill)" opacity=".55">'
    + "".join(f'<rect x="{x}" y="{y}" width="14" height="14" fill="#4E9A45"/>' for x in range(-10, 140, 28) for y in range(50, 140, 28))
    + "".join(f'<rect x="{x+14}" y="{y+14}" width="14" height="14" fill="#4E9A45"/>' for x in range(-10, 140, 28) for y in range(50, 140, 28))
    + '</g><ellipse cx="64" cy="100" rx="38" ry="20" fill="#5A3F35" stroke="#3B3355" stroke-width="3"/>'
    + f'<g transform="translate(64 62) scale(0.8)">{knight()}</g>'
    + '<path d="M26 100 A38 20 0 0 0 102 100 L102 132 H26Z" fill="#8FD07A"/>'
    + '<path d="M26 100 A38 20 0 0 0 102 100" fill="none" stroke="#3B3355" stroke-width="3"/>'
    + '<path d="M30 92 q-6 -4 -10 2 M98 92 q6 -4 10 2" fill="#FFF7EC" stroke="#3B3355" stroke-width="2.6"/>'
    + '<circle cx="104" cy="28" r="4" fill="#fff"/>' + sparkle(22, 34, 6),
    "белый шахматный конь-норушка", "выглядывает из круглой норки в клетчатом зелёном холме")

# «Максимум» в Марьино: чёрный и белый кони жмут друг другу копыта над доской
add("chessmax-mari", "yellow",
    board(16, 92, 8, 12, a="#FFE9B8", b="#C98B4E")
    + f'<g transform="translate(40 58) scale(0.6)">{knight()}</g>'
    + f'<g transform="translate(88 58) scale(-0.6 0.6)">{knight("#4A4466", "#6A6488", "#fff")}</g>'
    + f'<path d="M50 54 Q58 46 64 50" stroke="{O}" stroke-width="10" stroke-linecap="round" fill="none"/>'
    + f'<path d="M50 54 Q58 46 64 50" stroke="{LIGHT}" stroke-width="5" stroke-linecap="round" fill="none"/>'
    + f'<path d="M78 54 Q70 46 64 50" stroke="{O}" stroke-width="10" stroke-linecap="round" fill="none"/>'
    + f'<path d="M78 54 Q70 46 64 50" stroke="#6A6488" stroke-width="5" stroke-linecap="round" fill="none"/>'
    + '<path d="M58 30 l3 -6 M64 28 v-7 M70 30 l-3 -6" stroke="#3B3355" stroke-width="2.6" stroke-linecap="round"/>',
    "пара шахматных коней, белый и чёрный", "жмут друг другу копыта над доской перед партией")

# «Максимум» в «Филионе»: малышка толкает огромную уличную пешку
add("chessmax-filion", "sky",
    board(-4, 98, 6, 24, a="#E9F2DA", b="#7FB069")
    + f'<g transform="translate(78 54) scale(1.0)">{pawn("#FFFFFF", "#DCE3EE")}</g>'
    + face(78, 32, d=7, k=0.7)
    # девочка-малышка, упирается руками в пешку
    + '<path d="M34 104 L40 86 M46 104 L44 86" stroke="#3B3355" stroke-width="4" stroke-linecap="round"/>'
    + f'<path d="M30 88 Q40 64 52 70 L54 88Z" fill="{PINK}" {W(3)}/>'
    + '<path d="M48 72 L60 66" stroke="#3B3355" stroke-width="7" stroke-linecap="round"/><path d="M48 72 L60 66" stroke="#FFD9B8" stroke-width="3.4" stroke-linecap="round"/>'
    + f'<circle cx="38" cy="56" r="11" fill="#FFD9B8" {W(3)}/><path d="M27 52 Q38 40 49 52" fill="#8A5A3C" {W(2.6)}/>'
    + f'<path d="M27 52 l-6 8" stroke="#8A5A3C" stroke-width="5" stroke-linecap="round"/>'
    + eye(42, 57, 0.6) + '<path d="M40 64 h5" stroke="#3B3355" stroke-width="2" stroke-linecap="round"/>'
    + '<path d="M18 76 h-8 M20 84 h-10" stroke="#fff" stroke-width="3" stroke-linecap="round"/>',
    "огромная уличная пешка ростом с ребёнка", "малышка изо всех сил толкает её по клеткам уличной шахматной площадки")

# «Лабиринты шахмат» (Багратионовская): конь скачет буквой «Г», пунктирный след
add("chesslab-bagrationovskaya", "purple",
    board(10, 14, 6, 18, a="#F1E8FF", b="#9B82D6")
    + '<path d="M28 104 V50 H64" fill="none" stroke="#FF9F43" stroke-width="5" stroke-dasharray="2 9" stroke-linecap="round"/>'
    + f'<circle cx="28" cy="104" r="5" fill="#FF9F43" {W(2)}/>'
    + f'<g transform="translate(78 54) scale(0.62)">{knight("#FF9F43", "#FFC98E")}</g>'
    + '<path d="M58 44 l-6 -4 M58 52 h-8" stroke="#fff" stroke-width="3" stroke-linecap="round"/>',
    "оранжевый шахматный конь", "скачет по доске буквой «Г», за ним тянется пунктирный след хода")

# «Лабиринты шахмат» (Новаторская): поверженный король машет белым флажком
add("chesslab-novatorskaya", "teal",
    board(-6, 92, 7, 20, a="#E2FAF4", b="#58B9A6")
    + f'<g transform="translate(56 106) rotate(-14) scale(0.86)">'
      f'<rect x="-26" y="-12" width="52" height="13" rx="4" fill="{DARK}" {W(3)}/>'
      f'<path d="M-20 -10 Q-15 -40 -18 -58 H18 Q15 -40 20 -10Z" fill="{DARK}" {W(3)}/>'
      f'<rect x="-22" y="-66" width="44" height="9" rx="4" fill="#6A6488" {W(3)}/>'
      f'<path d="M-15 -66 Q0 -84 15 -66Z" fill="{DARK}" {W(3)}/>'
      f'<path d="M0 -98 V-78 M-8 -90 H8" stroke="{O}" stroke-width="8" stroke-linecap="round"/>'
      f'<path d="M0 -98 V-78 M-8 -90 H8" stroke="{GOLD}" stroke-width="4" stroke-linecap="round"/>'
      '<path d="M-12 -40 q4 -3 8 0 M4 -40 q4 -3 8 0" stroke="#fff" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
      '<ellipse cx="0" cy="-28" rx="4" ry="3" fill="#fff"/>'
      f'<ellipse cx="-13" cy="-32" rx="3.4" ry="2" fill="{PINK}" opacity=".8"/><ellipse cx="13" cy="-32" rx="3.4" ry="2" fill="{PINK}" opacity=".8"/>'
      f'<path d="M18 -36 L34 -44" stroke="{O}" stroke-width="7" stroke-linecap="round"/><path d="M18 -36 L34 -44" stroke="#6A6488" stroke-width="3.4" stroke-linecap="round"/></g>'
    + '<path d="M90 84 L98 22" stroke="#3B3355" stroke-width="3.4" stroke-linecap="round"/>'
    + f'<path d="M98 22 Q110 18 120 26 Q110 32 116 42 Q104 36 96 40Z" fill="#fff" {W(3)}/>'
    + '<path d="M26 34 l4 4 M22 44 h6" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>',
    "поверженный чёрный шахматный король", "пошатнулся на доске и с ойкающим ртом поднимает белый флажок — сдаётся")

# «Лабиринты шахмат» в детской библиотеке (Свиблово): из раскрытой книги-доски выпрыгивают пешки
add("chesslab-sviblovo", "pink",
    f'<path d="M14 92 Q38 82 64 92 Q90 82 114 92 V108 Q90 98 64 108 Q38 98 14 108Z" fill="#C0504D" {W(3)}/>'
    + f'<path d="M18 88 Q40 78 64 88 V100 Q40 90 18 100Z" fill="#fff" {W(3)}/>'
    + f'<path d="M110 88 Q88 78 64 88 V100 Q88 90 110 100Z" fill="#fff" {W(3)}/>'
    + "".join(f'<path d="M{24+i*10} {86-i*1.2:.0f} l8 -1 v8 l-8 1Z" fill="#8A6A55"/>' for i in range(0, 4, 2))
    + "".join(f'<path d="M{70+i*10} {82+i*1.2:.0f} l8 1 v8 l-8 -1Z" fill="#8A6A55"/>' for i in range(0, 4, 2))
    + f'<g transform="translate(46 56) scale(0.7) rotate(-12)">{pawn()}</g>' + face(43, 40, d=6, k=0.6)
    + f'<g transform="translate(82 44) scale(0.56) rotate(14)">{pawn(DARK, "#6A6488")}</g>'
    + eye(80, 31, 0.5).replace(O, "#fff", 1) + eye(88, 33, 0.5).replace(O, "#fff", 1)
    + '<path d="M30 70 q-4 -8 2 -14 M96 70 q6 -6 2 -14" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round"/>'
    + sparkle(64, 22, 6),
    "раскрытая книга с шахматными клетками на страницах", "из неё выпрыгивают белая и чёрная пешки, как в детской библиотеке")

# «Лабиринты шахмат» (Солнцево): чёрная пешка встаёт из-за края доски, как солнце
add("chesslab-solntsevo", "orange",
    "".join(f'<path d="M64 74 L{64+60*math.cos(a):.1f} {74-60*math.sin(a):.1f}" stroke="#FFE38A" stroke-width="7" stroke-linecap="round"/>'
            for a in [math.radians(d) for d in (12, 40, 68, 90, 112, 140, 168)])
    + f'<g transform="translate(64 78) scale(1.15)">{pawn(DARK, "#6A6488")}</g>'
    + '<g transform="translate(64 53)"><ellipse cx="-8" cy="0" rx="3.6" ry="4.4" fill="#fff"/><ellipse cx="8" cy="0" rx="3.6" ry="4.4" fill="#fff"/>'
      '<circle cx="-8" cy="1" r="1.8" fill="#3B3355"/><circle cx="8" cy="1" r="1.8" fill="#3B3355"/>'
      '<path d="M-4 8 Q0 12 4 8" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>'
      f'<ellipse cx="-14" cy="7" rx="3.4" ry="2" fill="{PINK}" opacity=".8"/><ellipse cx="14" cy="7" rx="3.4" ry="2" fill="{PINK}" opacity=".8"/></g>'
    + board(-8, 78, 9, 16, a="#FFF1D6", b="#B9763F"),
    "чёрная пешка-рассвет", "поднимается из-за края шахматной доски, как солнце из-за горизонта, с лучами")

# ============================== БАСКЕТБОЛ (Московская баскетбольная академия) ==============================
# Гомельского: жираф дотягивается шеей и кладёт мяч в кольцо
add("mba-gomelsky", "blue",
    hoop(98, 40, 34)
    + '<path d="M40 128 L44 90 Q48 60 70 40 L80 46 Q62 66 60 92 L62 128Z" fill="#FFC85A" stroke="#3B3355" stroke-width="3"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#D9883A"/>' for x, y, r in ((52, 104, 5), (56, 84, 4), (64, 66, 3.4), (50, 120, 4)))
    + f'<path d="M64 34 Q74 22 88 30 Q92 38 84 46 L70 46 Q62 42 64 34Z" fill="#FFC85A" {W(3)}/>'
    + f'<path d="M70 26 l-2 -8 M76 24 l1 -8" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/><circle cx="68" cy="17" r="3" fill="#B86A2A" {W(2)}/><circle cx="77" cy="15" r="3" fill="#B86A2A" {W(2)}/>'
    + eye(76, 32, 0.7) + f'<ellipse cx="84" cy="40" rx="3" ry="2" fill="{PINK}" opacity=".8"/><path d="M80 42 q3 2 6 0" stroke="{O}" stroke-width="2" fill="none"/>'
    + bball(98, 24, 11, fc=False)
    + '<path d="M86 36 Q90 34 92 30" stroke="#3B3355" stroke-width="2.4" fill="none"/>',
    "жираф-баскетболист", "дотягивается длинной шеей и кладёт мяч в кольцо сверху")

# Зеленоград (город науки): робот бросает мяч клешнёй в кольцо
add("mba-zelenograd", "teal",
    hoop(30, 46, 32)
    + f'<rect x="64" y="64" width="40" height="40" rx="8" fill="#B8C4D6" {W(3)}/><rect x="72" y="104" width="8" height="14" fill="#8A97AE" {W(3)}/><rect x="88" y="104" width="8" height="14" fill="#8A97AE" {W(3)}/>'
    + f'<rect x="68" y="34" width="32" height="26" rx="6" fill="#DCE3EE" {W(3)}/><path d="M84 34 V24" stroke="{O}" stroke-width="3"/><circle cx="84" cy="22" r="4" fill="{RED}" {W(2)}/>'
    + eye(77, 46, 0.7) + eye(91, 46, 0.7) + '<path d="M80 54 q4 3 8 0" stroke="#3B3355" stroke-width="2.2" fill="none"/>'
    + f'<circle cx="76" cy="80" r="4" fill="{GOLD}" {W(2)}/><circle cx="92" cy="80" r="4" fill="#7CD26E" {W(2)}/>'
    + f'<path d="M66 72 L50 60 L48 44" fill="none" stroke="{O}" stroke-width="8" stroke-linecap="round"/><path d="M66 72 L50 60 L48 44" fill="none" stroke="#8A97AE" stroke-width="4" stroke-linecap="round"/>'
    + f'<path d="M44 42 l-4 -6 M52 42 l4 -6" stroke="{O}" stroke-width="3" stroke-linecap="round"/>'
    + bball(48, 26, 10, fc=False)
    + '<path d="M104 72 L114 64" stroke="#3B3355" stroke-width="6" stroke-linecap="round"/>',
    "робот-баскетболист с антенной", "бросает мяч в кольцо механической клешнёй")

# «Первомайская»: осьминожка ведёт сразу четыре мяча щупальцами
add("mba-pervomayskaya", "pink",
    '<path d="M0 110 H128 V128 H0Z" fill="#E7B98A"/><path d="M0 110 H128" stroke="#3B3355" stroke-width="3"/>'
    + f'<path d="M40 60 Q40 26 64 26 Q88 26 88 60 Q88 72 80 74 H48 Q40 72 40 60Z" fill="#B98CF0" {W(3)}/>'
    + face(64, 54, d=9, k=0.8)
    + "".join(f'<path d="M{x0} 72 Q{x1} {y1} {x2} {y2}" fill="none" stroke="{O}" stroke-width="10" stroke-linecap="round"/>'
              f'<path d="M{x0} 72 Q{x1} {y1} {x2} {y2}" fill="none" stroke="#B98CF0" stroke-width="5" stroke-linecap="round"/>'
              for x0, x1, y1, x2, y2 in ((46, 30, 74, 22, 84), (56, 48, 88, 46, 92), (72, 80, 88, 82, 92), (82, 98, 74, 106, 84)))
    + bball(18, 98, 10, fc=False) + bball(44, 102, 8, fc=False) + bball(84, 102, 8, fc=False) + bball(110, 98, 10, fc=False)
    + '<path d="M18 86 v-4 M44 92 v-4 M84 92 v-4 M110 86 v-4" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>',
    "сиреневая осьминожка-баскетболистка", "ведёт по паркету сразу четыре мяча четырьмя щупальцами")

# «Тринта»: тележка-корзина с баскетбольными мячами катится по паркету
add("mba-trinta", "yellow",
    '<path d="M0 104 H128 V128 H0Z" fill="#E2A868"/>' + "".join(f'<path d="M{x} 104 V128" stroke="#C98A4E" stroke-width="2"/>' for x in range(8, 128, 18))
    + '<path d="M0 104 H128" stroke="#3B3355" stroke-width="3"/>'
    + bball(44, 48, 15, fc=False) + bball(74, 44, 15) + bball(58, 30, 13, fc=False)
    + f'<path d="M22 56 H106 L98 94 H30Z" fill="#9AA6BC" fill-opacity=".35" {W(3)}/>'
    + "".join(f'<path d="M{x} 56 L{x+(64-x)*0.1:.1f} 94" stroke="{O}" stroke-width="2"/>' for x in range(34, 100, 12))
    + '<path d="M26 74 H102" stroke="#3B3355" stroke-width="2"/>'
    + f'<path d="M106 56 L116 40" stroke="{O}" stroke-width="4" stroke-linecap="round"/>'
    + f'<circle cx="40" cy="100" r="5" fill="#fff" {W(2.6)}/><circle cx="88" cy="100" r="5" fill="#fff" {W(2.6)}/>'
    + '<path d="M14 84 h-8 M16 92 h-10" stroke="#fff" stroke-width="3" stroke-linecap="round"/>',
    "тележка-корзина с баскетбольными мячами", "катится по паркету спортзала, верхний мяч улыбается")

# «Глория» у зоопарка: слонёнок подбрасывает мяч хоботом под кольцом
add("mba-gloriya", "orange",
    hoop(96, 34, 30)
    + f'<path d="M20 112 Q16 74 46 66 Q76 60 84 88 L84 112Z" fill="#AEB8C8" {W(3)}/>'
    + f'<rect x="28" y="100" width="14" height="22" rx="5" fill="#AEB8C8" {W(3)}/><rect x="64" y="100" width="14" height="22" rx="5" fill="#AEB8C8" {W(3)}/>'
    + f'<ellipse cx="44" cy="72" rx="16" ry="18" fill="#C6CEDB" {W(3)}/>'
    + f'<path d="M72 78 Q86 74 88 56 Q90 46 96 44" fill="none" stroke="{O}" stroke-width="13" stroke-linecap="round"/><path d="M72 78 Q86 74 88 56 Q90 46 96 44" fill="none" stroke="#AEB8C8" stroke-width="8" stroke-linecap="round"/>'
    + eye(64, 72, 0.75) + f'<ellipse cx="70" cy="84" rx="4" ry="2.4" fill="{PINK}" opacity=".7"/>'
    + bball(100, 64, 11, fc=False)
    + '<path d="M90 76 q4 -4 8 -2" stroke="#fff" stroke-width="2.4" fill="none" stroke-linecap="round"/>',
    "серый слонёнок-баскетболист", "подбрасывает мяч хоботом к кольцу")

# «Гольяново»: ночная игра — мяч-луна светит над кольцом
add("mba-golyanovo", "night",
    "".join(sparkle(x, y, r) for x, y, r in ((18, 30, 4), (36, 18, 3), (104, 96, 3), (20, 70, 3), (112, 22, 4)))
    + '<circle cx="74" cy="44" r="34" fill="#FFB24C" opacity=".25"/>'
    + bball(74, 44, 26)
    + f'<path d="M20 128 V70" stroke="{O}" stroke-width="7"/><path d="M20 128 V70" stroke="#8A97AE" stroke-width="3"/>'
    + hoop(36, 88, 26)
    + '<path d="M62 18 q-6 2 -8 8" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round" opacity=".7"/>',
    "баскетбольный мяч-луна", "светит над уличным кольцом в ночном небе со звёздами")

# «Тимирязевская» (парк-дендрарий): бельчонок забрасывает мяч в кольцо на дупле
add("mba-timiryazevskaya", "green",
    f'<path d="M76 -4 H112 V132 H76Z" fill="#9A6A45" {W(3)}/><ellipse cx="94" cy="36" rx="9" ry="12" fill="#4A2F22" {W(2.6)}/>'
    + '<path d="M84 70 q6 4 10 0 M80 96 q8 4 14 0" stroke="#6E4A30" stroke-width="2.4" fill="none"/>'
    + hoop(66, 54, 28, board=False) + f'<path d="M78 54 H84" stroke="{O}" stroke-width="4"/>'
    + f'<path d="M30 112 Q4 92 18 70 Q30 56 40 70 Q34 84 46 96" fill="#E0823D" {W(3)}/>'
    + f'<ellipse cx="44" cy="100" rx="14" ry="16" fill="#F29A4A" {W(3)}/><circle cx="44" cy="76" r="13" fill="#F29A4A" {W(3)}/>'
    + f'<path d="M34 66 l-2 -10 l8 6 M50 64 l4 -9 l3 10" fill="#F29A4A" {W(2.6)}/>'
    + face(44, 76, d=5, k=0.6) + f'<ellipse cx="44" cy="104" rx="8" ry="9" fill="#FFE2B8"/>'
    + f'<path d="M52 92 L60 78" stroke="{O}" stroke-width="7" stroke-linecap="round"/><path d="M52 92 L60 78" stroke="#F29A4A" stroke-width="3.4" stroke-linecap="round"/>'
    + bball(62, 34, 11, fc=False)
    + '<path d="M50 30 q4 -6 8 -8" stroke="#fff" stroke-width="2.4" fill="none" stroke-linecap="round"/>',
    "рыжий бельчонок-баскетболист", "закидывает мяч в кольцо, прибитое к дереву с дуплом в парке")

# «Красная Пахра» (спортбаза «Олимпийские надежды»): уличное кольцо на лесной поляне среди сосен
add("mba-krasnaya-pakhra", "sky",
    '<path d="M-4 100 Q64 84 132 100 V132 H-4Z" fill="#9BDB7E" stroke="#3B3355" stroke-width="3"/>'
    + "".join(f'<path d="M{x} {y} l-14 26 h28Z M{x} {y+14} l-17 28 h34Z" fill="#3E9A5A" {W(2.6)}/><rect x="{x-3}" y="{y+42}" width="6" height="10" fill="#8A5A3C"/>'
              for x, y in ((18, 48), (110, 44)))
    + f'<path d="M64 124 V40" stroke="{O}" stroke-width="9"/><path d="M64 124 V40" stroke="#C98A4E" stroke-width="4.6"/>'
    + hoop(64, 44, 34)
    + bball(64, 26, 12)
    + '<path d="M46 14 q6 -4 10 0 M82 14 q-6 -4 -10 0" stroke="#fff" stroke-width="2.6" fill="none" stroke-linecap="round"/>',
    "уличное баскетбольное кольцо на деревянном столбе", "стоит на лесной поляне между соснами и ловит улыбчивый мяч")

# ============================== БАДМИНТОН / НАСТОЛЬНЫЙ ТЕННИС / ФЕХТОВАНИЕ ==============================
# SmashClub: ракетка бьёт смэш — волан летит вниз с молнией
add("smashclub-ivanteevskaya", "purple",
    f'<g transform="translate(82 44) rotate(38)">'
    f'<path d="M0 30 V70" stroke="{O}" stroke-width="10" stroke-linecap="round"/><path d="M0 34 V70" stroke="#FFD25E" stroke-width="5.6" stroke-linecap="round"/>'
    f'<ellipse cx="0" cy="0" rx="20" ry="27" fill="#fff" {W(3)}/>'
    + "".join(f'<path d="M{x} -26 V26" stroke="#C9CDD8" stroke-width="1.4"/>' for x in range(-14, 16, 7))
    + "".join(f'<path d="M-19 {y} H19" stroke="#C9CDD8" stroke-width="1.4"/>' for y in range(-21, 24, 7))
    + f'<ellipse cx="0" cy="0" rx="20" ry="27" fill="none" stroke="{O}" stroke-width="6"/><ellipse cx="0" cy="0" rx="20" ry="27" fill="none" stroke="#FF5FA0" stroke-width="3"/></g>'
    + face(84, 42, d=7, k=0.65)
    + f'<path d="M106 52 L98 62 L108 62 L100 72" fill="none" stroke="{O}" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>'
    + f'<path d="M106 52 L98 62 L108 62 L100 72" fill="none" stroke="#FFE34D" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>'
    + f'<g transform="translate(98 96) rotate(-20) scale(0.66)"><path d="M-9 6 L-20 -26 Q0 -32 20 -26 L9 6Z" fill="#fff" {W(2.6)}/>'
      f'<path d="M-9 6 Q-10 22 0 22 Q10 22 9 6Z" fill="{RED}" {W(2.6)}/></g>',
    "фиолетовая бадминтонная ракетка-силач", "делает смэш — волан с молнией летит вниз")

# SpinArt: крученый шарик вращается вихрем над ракеткой для настольного тенниса
add("spinart-semenovskaya", "blue",
    f'<g transform="translate(58 78) rotate(-24)"><path d="M0 26 V56" stroke="{O}" stroke-width="14" stroke-linecap="round"/><path d="M0 28 V56" stroke="#C08A5A" stroke-width="8" stroke-linecap="round"/>'
    f'<ellipse cx="0" cy="0" rx="30" ry="28" fill="#2E6FD8" {W(3)}/><ellipse cx="0" cy="0" rx="24" ry="22" fill="#3A80E8"/></g>'
    + face(56, 80, d=8, k=0.75)
    + '<path d="M60 40 Q84 22 100 34 Q110 46 96 54 Q84 60 80 48" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>'
    + '<path d="M54 30 Q80 6 108 24" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".8"/>'
    + f'<circle cx="92" cy="40" r="11" fill="#FFA640" {W(3)}/>'
    + '<path d="M86 34 Q92 42 98 36" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>'
    + eye(89, 41, 0.45) + eye(96, 41, 0.45),
    "оранжевый шарик для настольного тенниса", "крутится вихрем после подачи над синей ракеткой-улыбкой")

# СШОР «Северный»: пингвин-фехтовальщик делает выпад шпагой на льдине
add("sshor-severny-fencing", "sky",
    f'<path d="M4 108 L22 96 H104 L124 108 L108 118 H18Z" fill="#fff" {W(3)}/><path d="M0 118 H128 V132 H0Z" fill="#7CC8F2"/>'
    + f'<path d="M30 98 Q22 60 44 44 Q64 34 74 56 Q80 76 70 98Z" fill="#2F2A44" {W(3)}/>'
    + f'<path d="M38 96 Q34 66 48 54 Q62 48 66 68 Q68 84 62 96Z" fill="#fff"/>'
    + f'<path d="M44 52 Q46 30 58 32 Q70 34 68 50" fill="#2F2A44" {W(3)}/>'
    + f'<rect x="44" y="34" width="22" height="20" rx="8" fill="#5A5470" {W(2.6)}/>'
    + "".join(f'<path d="M{x} 36 V52" stroke="#9A95B2" stroke-width="1.4"/>' for x in range(48, 64, 4))
    + '<ellipse cx="55" cy="43" rx="2.4" ry="3" fill="#fff"/><ellipse cx="61" cy="43" rx="2.4" ry="3" fill="#fff"/>'
    + f'<path d="M66 44 L74 46 L66 49Z" fill="#FFB648" {W(1.8)}/>'
    + f'<path d="M68 70 L82 62" stroke="{O}" stroke-width="7" stroke-linecap="round"/><path d="M68 70 L82 62" stroke="#2F2A44" stroke-width="3.6" stroke-linecap="round"/>'
    + f'<path d="M80 58 Q86 54 88 62 Q84 66 80 58Z" fill="#C9CDD8" {W(2)}/><path d="M86 60 L122 40" stroke="{O}" stroke-width="4.6" stroke-linecap="round"/><path d="M86 60 L122 40" stroke="#E6EAF2" stroke-width="2" stroke-linecap="round"/>'
    + f'<path d="M40 98 l-6 6 h10 M62 98 l2 6 h10" fill="#FFB648" {W(2)}/>'
    + sparkle(104, 20, 5) + sparkle(20, 28, 4),
    "пингвин-фехтовальщик в сетчатой маске", "делает выпад шпагой на северной льдине")

# ============================== ТАНЦЫ ==============================
# Dance City (Медведково): медвежонок в бальном платье кружится в вальсе
add("dance-city-medvedkovo", "pink",
    f'<path d="M64 62 Q30 70 22 108 Q64 120 106 108 Q98 70 64 62Z" fill="#9B6BFF" {W(3)}/>'
    + '<path d="M36 104 Q44 84 52 70 M64 112 V66 M92 104 Q84 84 76 70" stroke="#C7AEFF" stroke-width="3" fill="none"/>'
    + f'<path d="M50 66 Q64 54 78 66 L74 76 H54Z" fill="#8458E8" {W(3)}/>'
    + f'<circle cx="44" cy="22" r="7" fill="#B07A4E" {W(3)}/><circle cx="84" cy="22" r="7" fill="#B07A4E" {W(3)}/>'
    + f'<circle cx="64" cy="40" r="22" fill="#B07A4E" {W(3)}/><ellipse cx="64" cy="48" rx="10" ry="7" fill="#E8C49A" {W(2.4)}/>'
    + eye(56, 38, 0.7) + eye(72, 38, 0.7) + '<ellipse cx="64" cy="45" rx="3" ry="2.2" fill="#3B3355"/>'
    + '<path d="M60 51 q4 3 8 0" stroke="#3B3355" stroke-width="2" fill="none"/>'
    + f'<path d="M50 70 Q34 60 30 44" stroke="{O}" stroke-width="9" stroke-linecap="round" fill="none"/><path d="M50 70 Q34 60 30 44" stroke="#B07A4E" stroke-width="5" stroke-linecap="round" fill="none"/>'
    + f'<path d="M78 70 Q94 60 98 44" stroke="{O}" stroke-width="9" stroke-linecap="round" fill="none"/><path d="M78 70 Q94 60 98 44" stroke="#B07A4E" stroke-width="5" stroke-linecap="round" fill="none"/>'
    + '<path d="M12 80 Q6 70 14 62 M116 80 Q122 70 114 62" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round"/>'
    + '<path d="M108 30 v12 a4 4 0 1 1 -3 -3 M108 30 l6 2" stroke="#3B3355" stroke-width="2.6" fill="none" stroke-linecap="round"/>',
    "медвежонок в пышном бальном платье", "кружится в вальсе, раскинув лапы")

# MAINSTREAM (хип-хоп): пара ярких кроссовок пританцовывает на граффити-ступеньке
add("mainstream-dance-kids", "night",
    '<path d="M-4 96 H132 V132 H-4Z" fill="#3A3F7A"/>'
    + '<path d="M8 110 Q20 100 30 112 T56 108 M70 116 Q84 104 98 116 T124 110" stroke="#FF5FA0" stroke-width="4" fill="none" stroke-linecap="round"/>'
    + '<path d="M10 122 Q30 114 46 124 M84 124 Q100 116 118 124" stroke="#5CE0C8" stroke-width="4" fill="none" stroke-linecap="round"/>'
    + '<path d="M-4 96 H132" stroke="#3B3355" stroke-width="3"/>'
    + f'<g transform="translate(40 78) rotate(-14)"><path d="M-24 4 Q-24 -12 -14 -14 L-8 -28 H8 L10 -10 Q24 -8 28 4 V10 H-24Z" fill="#FFD23F" {W(3)}/>'
      f'<path d="M-24 10 H28 V16 H-24Z" fill="#fff" {W(3)}/><path d="M-4 -24 l8 4 M-6 -18 l10 4" stroke="{RED}" stroke-width="2.4"/></g>'
    + face(42, 76, d=6, k=0.6)
    + f'<g transform="translate(88 64) rotate(18)"><path d="M-24 4 Q-24 -12 -14 -14 L-8 -28 H8 L10 -10 Q24 -8 28 4 V10 H-24Z" fill="#5CE0C8" {W(3)}/>'
      f'<path d="M-24 10 H28 V16 H-24Z" fill="#fff" {W(3)}/><path d="M-4 -24 l8 4 M-6 -18 l10 4" stroke="#FF5FA0" stroke-width="2.4"/></g>'
    + face(88, 62, d=6, k=0.6)
    + '<path d="M60 22 v14 a4 4 0 1 1 -3 -3 M60 22 l8 -3 v14 a4 4 0 1 1 -3 -3" stroke="#fff" stroke-width="2.6" fill="none" stroke-linecap="round"/>'
    + sparkle(104, 24, 5, "#FFD23F") + sparkle(22, 32, 4, "#FF5FA0"),
    "пара ярких кроссовок-хипхоперов", "пританцовывают на ночной улице над граффити, вокруг ноты")

# ============================== ФУТБОЛ ==============================
# «Школа мяча» в Сколково (город инноваций): 3D-принтер печатает футбольный мяч слой за слоем
add("schoolball-skolkovo", "green",
    f'<rect x="14" y="20" width="100" height="94" rx="8" fill="#DCE3EE" {W(3)}/>'
    + f'<rect x="24" y="30" width="80" height="70" rx="4" fill="#F4F7FB" {W(2.6)}/>'
    + f'<path d="M24 42 H104" stroke="{O}" stroke-width="4"/><rect x="56" y="36" width="16" height="12" rx="2" fill="#7CD26E" {W(2.4)}/><path d="M64 48 L64 54" stroke="{O}" stroke-width="3"/>'
    + '<clipPath id="printed"><rect x="30" y="58" width="68" height="40"/></clipPath>'
    + '<g clip-path="url(#printed)">'
    + f'<circle cx="64" cy="82" r="26" fill="#fff" {W(3)}/><path d="M64 66 l9 7 -3 10 h-12 l-3 -10Z" fill="{O}"/>'
      f'<path d="M40 78 l6 -2 4 6 -4 8 -6 -2Z M88 78 l-6 -2 -4 6 4 8 6 -2Z" fill="{O}"/></g>'
    + '<path d="M38 58 H90" stroke="#FF8A3C" stroke-width="3" stroke-dasharray="4 3"/>'
    + face(64, 90, d=8, k=0.65)
    + f'<rect x="24" y="100" width="80" height="6" fill="#B8C4D6" {W(2.4)}/>'
    + f'<circle cx="100" cy="26" r="3" fill="{RED}"/><circle cx="90" cy="26" r="3" fill="#7CD26E"/>',
    "3D-принтер инноград", "печатает футбольный мяч слой за слоем, мяч уже улыбается")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for pid, code in ICONS.items():
        open(os.path.join(OUT, pid + ".svg"), "w").write(code)
    reg = os.path.join(OUT, "subjects.txt")
    lines = [l for l in open(reg, encoding="utf-8") if l.split(" — ", 1)[0] not in SUBJ]
    lines += [line + "\n" for line in SUBJ.values()]
    open(reg, "w", encoding="utf-8").writelines(lines)
    print(len(ICONS), "иконок:", " ".join(ICONS))
