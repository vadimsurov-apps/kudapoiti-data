"""Иконки робота sections, 2026-11-07 (06 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно —
свой герой, своя сцена, своя компоновка и палитра. Якорь вида спорта читается сразу (бадминтон — волан и ракетка,
волейбол — бело-жёлто-синий мяч и сетка, шахматы — фигуры, бой на мечах — меч/щит/шлем).
Сверено с листами icons-catalog/sheet-01..30 и icons-src/subjects.txt (заняты: волан-персонаж в шапках, волан-спутник,
-лебедь, -альпинист, -парашютист; мяч-персонаж с аксессуарами, мяч-фотон, -парусник, медвежонок у сетки; кони/пешки/
короли-персонажи в шапках, конь-Пегас, пешка на ковре-самолёте; меч-кладенец, маски фехтовальщиков).
Запуск: python3 tools/icons_sections_1107d.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
W = lambda w: s(f'stroke-width="{w}"')
PINK, GOLD, RED, ORG, LIGHT = "#FF7FA8", "#FFC93C", "#E8554A", "#F28C38", "#FFF7EC"
VY, VB = "#FFD23F", "#3E7FD8"  # волейбольный мяч
ICONS, SUBJ = {}, {}


def add(pid, bg, body, hero, scene):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def G(x, y, body, rot=0, sc=1.0):
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({sc})">{body}</g>'


def shuttle(fc=True, cork="#FFFFFF", band=RED, feathers=("#FFFFFF",), closed=False):
    """волан вокруг (0,0): пробка внизу, юбка из перьев вверх; высота ~86"""
    n = len(feathers)
    g = ""
    xs = [-30 + 60 * i / n for i in range(n + 1)]
    for i, c in enumerate(feathers):
        a, b = xs[i], xs[i + 1]
        ba, bb = -14 + 28 * i / n, -14 + 28 * (i + 1) / n
        g += f'<path d="M{a:.1f} -40 L{ba:.1f} 12 H{bb:.1f} L{b:.1f} -40 Q{(a+b)/2:.1f} -44 {a:.1f} -40Z" fill="{c}"/>'
    g += (f'<path d="M-30 -40 L-14 12 H14 L30 -40 Q0 -48 -30 -40Z" fill="none" {W(3)}/>'
          f'<path d="M-15 -43 L-6 12 M0 -45 V12 M15 -43 L6 12" fill="none" {W(1.8)}/>'
          f'<path d="M-24 -20 Q0 -25 24 -20 M-19 -2 Q0 -6 19 -2" fill="none" {W(1.8)}/>'
          f'<rect x="-16" y="10" width="32" height="7" rx="2" fill="{band}" {W(2.6)}/>'
          f'<path d="M-16 17 H16 Q16 38 0 38 Q-16 38 -16 17Z" fill="{cork}" {W(3)}/>')
    if fc:
        g += face(0, 25, d=6.5, k=0.62, mouth=not closed)
    return g


def racket(c="#5CB7F2", grip="#4A4466"):
    """бадминтонная ракетка: голова вверху (центр 0,-30), ручка до y=+48"""
    st = ""
    for i in range(-12, 13, 6):
        hh = 22 * math.sqrt(max(0, 1 - (i / 18) ** 2))
        st += f'M{i} {-30-hh:.1f} V{-30+hh:.1f} '
    for j in range(-18, 19, 6):
        ww = 16 * math.sqrt(max(0, 1 - (j / 23) ** 2))
        st += f'M{-ww:.1f} {-30+j} H{ww:.1f} '
    return (f'<rect x="-2.2" y="-6" width="4.4" height="30" fill="#C9CED8" {W(2.2)}/>'
            f'<rect x="-5" y="22" width="10" height="26" rx="4" fill="{grip}" {W(2.4)}/>'
            f'<ellipse cx="0" cy="-30" rx="19" ry="25" fill="#fff" fill-opacity=".55" stroke="{c}" stroke-width="7"/>'
            f'<ellipse cx="0" cy="-30" rx="19" ry="25" fill="none" {W(2.4)}/>'
            f'<ellipse cx="0" cy="-30" rx="22.5" ry="28.5" fill="none" {W(2.4)}/>'
            f'<path d="{st}" fill="none" stroke="{O}" stroke-width="1.1" opacity=".55"/>')


def vball(cx, cy, r, fc=True, sleepy=False, k=None):
    """волейбольный мяч: белый с жёлтыми и синими долями"""
    k = k or r / 34
    out = (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" {W(3)}/>'
           f'<path d="M{cx} {cy} Q{cx-r*0.2} {cy-r*0.75} {cx+r*0.35} {cy-r*0.94} A{r} {r} 0 0 0 {cx-r*0.62} {cy-r*0.78} Q{cx-r*0.55} {cy-r*0.3} {cx} {cy}Z" fill="{VY}" {W(2)}/>'
           f'<path d="M{cx} {cy} Q{cx+r*0.75} {cy+r*0.05} {cx+r*0.96} {cy+r*0.28} A{r} {r} 0 0 0 {cx+r*0.92} {cy-r*0.38} Q{cx+r*0.5} {cy-r*0.15} {cx} {cy}Z" fill="{VB}" {W(2)}/>'
           f'<path d="M{cx} {cy} Q{cx-r*0.55} {cy+r*0.62} {cx-r*0.5} {cy+r*0.87} A{r} {r} 0 0 1 {cx-r*0.96} {cy+r*0.2} Q{cx-r*0.6} {cy+r*0.3} {cx} {cy}Z" fill="{VB}" {W(2)}/>'
           f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" {W(3)}/>')
    if fc:
        if sleepy:
            d = r * 0.3
            out += (f'<path d="M{cx-d-5*k} {cy+r*0.25} q{5*k} {4*k} {10*k} 0 M{cx+d-5*k} {cy+r*0.25} q{5*k} {4*k} {10*k} 0" fill="none" {W(2.4)}/>'
                    f'<path d="M{cx-4*k} {cy+r*0.5} Q{cx} {cy+r*0.62} {cx+4*k} {cy+r*0.5}" fill="none" {W(2.4)}/>')
        else:
            out += face(cx, cy + r * 0.3, d=r * 0.28, k=k * 0.9)
    return out


def net(y, h=14, x0=-4, x1=132, posts=False):
    out = f'<rect x="{x0}" y="{y}" width="{x1-x0}" height="{h}" fill="#fff" fill-opacity=".35"/>'
    cells = "".join(f'M{x} {y} V{y+h} ' for x in range(x0, x1, 7)) + "".join(f'M{x0} {yy} H{x1} ' for yy in range(y + 5, y + h, 5))
    out += f'<path d="{cells}" fill="none" stroke="{O}" stroke-width="1" opacity=".6"/>'
    out += f'<rect x="{x0}" y="{y-3}" width="{x1-x0}" height="5" fill="#fff" {W(2.4)}/>'
    if posts:
        out += f'<rect x="10" y="{y-6}" width="6" height="60" fill="#C9CED8" {W(2.4)}/><rect x="112" y="{y-6}" width="6" height="60" fill="#C9CED8" {W(2.4)}/>'
    return out


def pawn(c=LIGHT, c2="#E9DCC8", fc=True):
    g = (f'<rect x="-24" y="34" width="48" height="11" rx="4" fill="{c}" {W(3)}/>'
         f'<path d="M-19 36 Q-14 12 -8 2 H8 Q14 12 19 36Z" fill="{c}" {W(3)}/>'
         f'<rect x="-14" y="-4" width="28" height="8" rx="4" fill="{c2}" {W(3)}/>'
         f'<circle cx="0" cy="-21" r="18" fill="{c}" {W(3)}/>')
    if fc:
        g += face(0, -21, d=6.5, k=0.62)
    return g


def rook(c=LIGHT, c2="#E9DCC8", fc=True, fy=8):
    """ладья вокруг (0,0): основание y=+44, зубцы y=-44"""
    g = (f'<rect x="-28" y="34" width="56" height="11" rx="4" fill="{c}" {W(3)}/>'
         f'<path d="M-20 34 L-16 -20 H16 L20 34Z" fill="{c}" {W(3)}/>'
         f'<rect x="-22" y="-24" width="44" height="7" rx="3" fill="{c2}" {W(3)}/>'
         f'<path d="M-24 -24 V-44 H-14 V-36 H-5 V-44 H5 V-36 H14 V-44 H24 V-24Z" fill="{c}" {W(3)}/>')
    if fc:
        g += face(0, fy, d=7, k=0.66)
    return g


def queen(c=LIGHT, c2="#E9DCC8", fc=True):
    g = (f'<rect x="-26" y="34" width="52" height="11" rx="4" fill="{c}" {W(3)}/>'
         f'<path d="M-20 35 Q-14 8 -10 -14 H10 Q14 8 20 35Z" fill="{c}" {W(3)}/>'
         f'<rect x="-15" y="-20" width="30" height="7" rx="3" fill="{c2}" {W(3)}/>'
         f'<path d="M-20 -20 L-24 -42 L-12 -30 L0 -46 L12 -30 L24 -42 L20 -20Z" fill="{c}" {W(3)}/>'
         f'<circle cx="-24" cy="-45" r="4" fill="{GOLD}" {W(2.2)}/><circle cx="0" cy="-50" r="4" fill="{GOLD}" {W(2.2)}/>'
         f'<circle cx="24" cy="-45" r="4" fill="{GOLD}" {W(2.2)}/>')
    if fc:
        g += face(0, 6, d=6.5, k=0.62)
    return g


def knight_head(c="#F4F1EC"):
    """голова шахматного коня (смотрит влево) вокруг (0,0), высота ~80"""
    return (f'<path d="M-22 40 H24 L20 18 Q30 -4 22 -22 Q14 -40 -4 -40 L-8 -50 L-14 -38 Q-28 -32 -32 -14 '
            f'L-34 -2 Q-30 8 -20 4 L-8 -2 Q-8 14 -22 26Z" fill="{c}" {W(3)}/>'
            f'<path d="M4 -38 Q18 -30 18 -10" fill="none" {W(2)}/>'
            + eye(-6, -20, 0.9) + f'<circle cx="-28" cy="-6" r="1.8" fill="{O}"/>'
            f'<ellipse cx="-14" cy="-10" rx="4" ry="2.4" fill="{PINK}" opacity=".6"/>'
            f'<path d="M-30 2 Q-26 5 -22 2" fill="none" {W(2.2)}/>')


def cloud(x, y, k=1.0, c="#fff"):
    return (f'<g transform="translate({x} {y}) scale({k})"><path d="M-22 8 Q-30 8 -28 0 Q-28 -10 -16 -9 Q-12 -20 0 -18 '
            f'Q12 -22 16 -10 Q28 -10 27 0 Q28 8 20 8Z" fill="{c}" {W(2.6)}/></g>')


def sword(L=78, blade="#DDE3EC", guard=GOLD, grip="#8A5A3C", fc=False, w=6):
    """меч остриём вверх вокруг (0,0): гарда y=0, клинок вверх на L, рукоять вниз ~26"""
    g = (f'<path d="M{-w} 0 V{-L+12} L0 {-L} L{w} {-L+12} V0Z" fill="{blade}" {W(2.8)}/>'
         f'<path d="M0 -4 V{-L+14}" stroke="#B8C1CF" stroke-width="2"/>'
         f'<rect x="-18" y="-2" width="36" height="8" rx="4" fill="{guard}" {W(2.6)}/>'
         f'<rect x="-4.5" y="6" width="9" height="18" rx="3" fill="{grip}" {W(2.4)}/>'
         f'<circle cx="0" cy="27" r="5" fill="{guard}" {W(2.4)}/>')
    if fc:
        g += face(0, -L * 0.5, d=w * 0.45, k=w / 16, blush=False)
    return g


def kid(skin="#FFD8B8", hair="#7A4A2E", shirt=RED, girl=False):
    """голова+туловище ребёнка вокруг (0,0): голова центр (0,-22), туловище до y=+30"""
    g = f'<path d="M-16 30 Q-18 0 0 -2 Q18 0 16 30Z" fill="{shirt}" {W(3)}/>'
    if girl:
        g += (f'<circle cx="-19" cy="-14" r="6" fill="{hair}" {W(2.4)}/><circle cx="19" cy="-14" r="6" fill="{hair}" {W(2.4)}/>')
    g += (f'<circle cx="0" cy="-22" r="17" fill="{skin}" {W(3)}/>'
          f'<path d="M-17 -24 Q-14 -42 0 -40 Q14 -42 17 -24 Q8 -32 0 -30 Q-8 -32 -17 -24Z" fill="{hair}" {W(2.6)}/>'
          + face(0, -18, d=6, k=0.6))
    return g


# ============================== БАДМИНТОН ==============================
# BadmPRO в «Карибии»: волан-попугай с перьями цветов Карибов сидит на пальмовой ветке
add("badmpro-karibia", "teal",
    f'<path d="M-4 104 Q50 92 132 100" fill="none" stroke="#8A5A3C" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M-4 104 Q50 92 132 100" fill="none" {W(1.6)}/>'
    + "".join(f'<path d="M{x} {y} q{dx} {dy} {dx*2} {dy*0.4}" fill="none" stroke="#4E9A44" stroke-width="6" stroke-linecap="round"/>'
              for x, y, dx, dy in [(18, 100, 6, 14), (94, 98, 8, 14), (108, 99, 8, 12)])
    + G(64, 58, shuttle(feathers=("#E8554A", "#FFC93C", "#5CB7F2", "#4FBF6B"), cork="#FF9A3C", band="#4A4466"), sc=0.86)
    + f'<path d="M59 86 Q64 93 69 86 L64 83Z" fill="{GOLD}" {W(2.2)}/>'
    + f'<path d="M56 91 V98 M61 91 V98 M67 91 V98 M72 91 V98" fill="none" {W(2.6)}/>',
    "пробковый волан-попугай с красно-жёлто-сине-зелёными перьями",
    "сидит на пальмовой ветке у аквапарка, вцепившись лапками и раскрыв клювик")

# СДЦ «Алексеевский» (бадминтон + шахматы): волан вышел на шахматную доску и делает ход против пешки
add("sdc-alekseevsky-zubarev", "yellow",
    f'<path d="M0 92 H128 V128 H0Z" fill="#FFF7EC"/>'
    + "".join(f'<rect x="{x}" y="{y}" width="16" height="12" fill="#8A6A55"/>' for x in range(0, 128, 32) for y in (92, 116))
    + "".join(f'<rect x="{x}" y="104" width="16" height="12" fill="#8A6A55"/>' for x in range(16, 128, 32))
    + f'<path d="M0 92 H128" {W(3)}/>'
    + G(44, 50, shuttle(), sc=0.82)
    + G(96, 70, pawn(c="#3B3355", c2="#5A5378", fc=False), sc=0.5)
    + face(96, 59, d=4, k=0.45)
    + f'<path d="M66 40 Q80 26 92 40" fill="none" stroke="{RED}" stroke-width="2.6" stroke-dasharray="3 4"/>'
    + f'<path d="M88 36 L93 41 L86 43" fill="none" stroke="{RED}" stroke-width="2.6"/>',
    "волан-шахматист с красной полоской",
    "встал на клетку шахматной доски и пунктирной дугой «ходит» к маленькой чёрной пешке")

# СШОР №92 «Солнцево»: девочка с косичками на цыпочках отбивает волан над головой на фоне большого солнца
add("sshor92-solntsevo-badminton", "orange",
    f'<circle cx="40" cy="40" r="26" fill="#FFE27A" stroke="#FFC93C" stroke-width="3"/>'
    + "".join(f'<path d="M{40+31*math.cos(a):.1f} {40+31*math.sin(a):.1f} L{40+38*math.cos(a):.1f} {40+38*math.sin(a):.1f}" stroke="#FFE27A" stroke-width="4" stroke-linecap="round"/>' for a in [i * math.pi / 4 for i in range(8)])
    + G(54, 86, kid(shirt="#FFC93C", hair="#5A3A22", girl=True))
    + f'<path d="M66 92 L82 70" fill="none" stroke="#FFD8B8" stroke-width="7" stroke-linecap="round"/><path d="M66 92 L82 70" fill="none" {W(1.4)}/>'
    + G(88, 50, racket(c="#E8554A"), rot=24, sc=0.62)
    + G(106, 18, shuttle(), rot=210, sc=0.42)
    + f'<path d="M46 116 V130 M60 116 V130" fill="none" {W(6)}/>',
    "девочка с косичками в жёлтой спортивной футболке",
    "тянется вверх и отбивает ракеткой волан над головой, за спиной встаёт большое солнце")

# ============================== ВОЛЕЙБОЛ ==============================
# СШОР №21: сонный мяч-луна висит в ночном небе над сеткой
add("sshor21-volley-kharitonyevsky", "night",
    sparkle(22, 30, 5) + sparkle(104, 24, 4) + sparkle(110, 60, 3) + sparkle(16, 66, 3)
    + vball(64, 50, 32, sleepy=True)
    + f'<text x="94" y="34" font-family="Arial" font-weight="bold" font-size="12" fill="#fff">z</text>'
    + f'<text x="102" y="24" font-family="Arial" font-weight="bold" font-size="9" fill="#fff">z</text>'
    + net(94, posts=True),
    "сонный волейбольный мяч-луна",
    "дремлет в ночном небе над волейбольной сеткой среди звёзд")

# «Искра-Новогиреево»: мальчик в красной форме подаёт мяч в прыжке, от ладони летят искры
add("iskra-novogireevo-volley", "pink",
    net(100, h=16)
    + G(52, 78, kid(shirt=RED, hair="#3B2A20"))
    + f'<path d="M62 74 L80 46" fill="none" stroke="#FFD8B8" stroke-width="7" stroke-linecap="round"/><path d="M62 74 L80 46" fill="none" {W(1.4)}/>'
    + f'<path d="M42 76 L30 90" fill="none" stroke="#FFD8B8" stroke-width="7" stroke-linecap="round"/>'
    + vball(92, 30, 17, k=0.5)
    + f'<path d="M76 40 L70 34 M82 36 L80 28 M74 48 L66 48" fill="none" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>'
    + sparkle(68, 26, 4, GOLD) + sparkle(64, 42, 3, "#fff") + sparkle(84, 54, 3, GOLD)
    + f'<path d="M44 108 L40 120 M60 108 L66 118" fill="none" {W(6)}/>',
    "мальчик-волейболист в красной форме",
    "в прыжке бьёт подачу сверху, и от ладони во все стороны летят золотые искры")

# ВК ДЮСШ «Звезда»: утконос подбрасывает мяч плоским клювом у сетки
add("zvezda-volley-nakhimovsky", "sky",
    net(96, h=12, x0=70)
    + f'<rect x="66" y="88" width="6" height="44" fill="#C9CED8" {W(2.4)}/>'
    + f'<path d="M14 118 Q4 104 22 98 L40 110Z" fill="#8A5A3C" {W(2.8)}/>'
    + f'<ellipse cx="44" cy="96" rx="28" ry="22" fill="#A8774F" {W(3)}/>'
    + f'<circle cx="54" cy="68" r="16" fill="#A8774F" {W(3)}/>'
    + f'<path d="M62 60 Q78 44 86 50 Q88 58 70 72Z" fill="#4A4466" {W(2.8)}/>'
    + eye(52, 64, 0.8) + f'<ellipse cx="46" cy="72" rx="4" ry="2.4" fill="{PINK}" opacity=".6"/>'
    + f'<path d="M36 112 L32 122 M52 114 L54 124" fill="none" {W(5)}/>'
    + vball(92, 30, 18, k=0.5)
    + f'<path d="M84 52 Q86 50 88 50" fill="none" stroke="#fff" stroke-width="2"/>'
    + f'<path d="M80 46 l-4 -4 M88 46 l2 -5" fill="none" stroke="{O}" stroke-width="2"/>',
    "коричневый утконос с плоским клювом",
    "подбрасывает волейбольный мяч клювом, стоя у стойки сетки")

# ============================== ШАХМАТЫ ==============================
# «Шахматное искусство»: мраморный бюст шахматного коня на пьедестале с лавровой ветвью
add("chess-art-valovaya", "purple",
    f'<rect x="38" y="96" width="52" height="34" fill="#F1EEF6" {W(3)}/>'
    f'<rect x="32" y="90" width="64" height="9" rx="2" fill="#E2DCEC" {W(3)}/>'
    f'<path d="M46 104 V128 M58 104 V128 M70 104 V128 M82 104 V128" stroke="#C9C1D8" stroke-width="2"/>'
    + G(66, 50, knight_head(c="#F1EEF6"))
    + f'<path d="M50 70 Q52 78 60 80" fill="none" stroke="#C9C1D8" stroke-width="2"/>'
    + f'<path d="M22 92 Q14 66 30 44" fill="none" stroke="#4E9A44" stroke-width="3"/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="6" ry="3" transform="rotate({r} {x} {y})" fill="#7CD26E" {W(1.8)}/>'
              for x, y, r in [(16, 80, -60), (24, 76, 30), (14, 64, -70), (24, 60, 20), (22, 48, -50), (32, 46, 40)]),
    "мраморный бюст шахматного коня",
    "стоит на колонне-пьедестале в музейном зале, рядом лавровая ветвь")

# «Свободные шахматы»: белая пешка с крылышками вылетает из открытой птичьей клетки
add("svobodnye-shakhmaty-tikhvinsky", "green",
    f'<path d="M8 126 V84 Q8 58 32 56 Q56 58 56 84 V126" fill="#fff" fill-opacity=".35" {W(2.6)}/>'
    f'<path d="M20 126 V66 M32 126 V56 M44 126 V66" fill="none" {W(2)}/>'
    f'<path d="M4 126 H60" {W(3.2)}/><circle cx="32" cy="52" r="4" fill="{GOLD}" {W(2)}/>'
    f'<path d="M56 86 L74 74 V112 L56 118" fill="#fff" fill-opacity=".5" {W(2.4)}/>'
    + f'<path d="M66 58 Q48 44 56 30 Q66 40 72 50Z M100 50 Q118 34 122 50 Q110 58 98 58Z" fill="#fff" {W(2.6)}/>'
    + G(84, 56, pawn(), rot=14, sc=0.78)
    + f'<path d="M60 96 q-6 2 -10 -2 M64 104 q-8 4 -14 0" fill="none" stroke="#fff" stroke-width="2.4"/>',
    "белая пешка с крылышками",
    "вырвалась из открытой птичьей клетки на свободу и летит вверх")

# ChessPRO: ферзь-супергерой в красном плаще летит над облаками, вытянув вперёд кулак
add("chesspro-dekabristov", "blue",
    cloud(28, 104, 1.0) + cloud(104, 112, 0.8)
    + f'<path d="M48 56 Q14 70 6 102 Q30 92 44 96 Q34 84 60 72Z" fill="{RED}" {W(3)}/>'
    + G(70, 56, queen(), rot=-28, sc=0.8)
    + f'<path d="M12 40 H32 M8 52 H24 M18 28 H34" stroke="#fff" stroke-width="3" stroke-linecap="round"/>',
    "белый ферзь-супергерой в красном плаще",
    "летит над облаками, вытянув вперёд кулак, плащ развевается за спиной")

# Курчатовская школа: пешка-атом — вокруг головы кружат три орбиты с электронами
add("kurchatov-school-chess", "teal",
    G(64, 70, pawn(c="#FFF7EC"), sc=0.9)
    + "".join(f'<ellipse cx="64" cy="51" rx="40" ry="12" transform="rotate({r} 64 51)" fill="none" stroke="#3E7FD8" stroke-width="2.6"/>' for r in (0, 60, 120))
    + f'<circle cx="104" cy="51" r="5" fill="{RED}" {W(2)}/><circle cx="44" cy="17" r="5" fill="{GOLD}" {W(2)}/><circle cx="44" cy="86" r="5" fill="#4FBF6B" {W(2)}/>',
    "белая пешка-атом",
    "вокруг её головы, как вокруг ядра, кружат три орбиты с цветными электронами")

# «Русский шах» (таврели): маленькая чёрная пешка балансирует на макушке белой ладьи — фигура-башенка
add("russky-shakh-udaltsova", "orange",
    f'<path d="M0 112 H128 V128 H0Z" fill="#8A6A55"/>'
    + "".join(f'<rect x="{x}" y="112" width="16" height="16" fill="#FFF7EC"/>' for x in range(0, 128, 32))
    + f'<path d="M0 112 H128" {W(3)}/>'
    + G(64, 78, rook(fy=4), sc=0.78)
    + G(66, 24, pawn(c="#3B3355", c2="#5A5378", fc=False), rot=8, sc=0.42)
    + face(64, 14, d=3.6, k=0.4)
    + f'<path d="M40 22 q-6 4 -4 10 M90 22 q6 4 4 10" fill="none" {W(2.4)}/>',
    "башенка-таврель: белая ладья с чёрной пешкой на макушке",
    "пешка балансирует на зубцах ладьи, раскинув ручки, обе стоят на одной клетке")

# ЦВР «Синегория»: синяя ладья-крепость со снежными зубцами возвышается над облаками
add("sinegoriya-chess", "sky",
    G(64, 62, rook(c="#5C8FE0", c2="#3E6FC0"), sc=0.95)
    + f'<path d="M41 20 H51 V27 H41Z M59 20 H69 V27 H59Z M77 20 H87 V27 H77Z" fill="#fff" {W(2)}/>'
    + cloud(24, 104, 1.1) + cloud(100, 106, 1.2) + cloud(62, 116, 1.0),
    "синяя шахматная ладья со снежными шапками на зубцах",
    "возвышается над облаками, как горная крепость")

# «Станция юных талантов»: пешка дошла до последней горизонтали — над ней вспыхивает корона ферзя
add("stantsiya-talantov-chess", "yellow",
    f'<path d="M12 100 L116 100 L128 128 H0Z" fill="#FFF7EC" {W(2.6)}/>'
    + "".join(f'<path d="M{12+i*26} 100 L{0+i*32} 128 L{0+(i+1)*32} 128 L{12+(i+1)*26} 100Z" fill="#8A6A55"/>' for i in (0, 2))
    + f'<path d="M12 100 L116 100" {W(3)}/>'
    + G(64, 72, pawn(), sc=0.72)
    + f'<path d="M46 32 L44 14 L55 24 L64 8 L73 24 L84 14 L82 32Z" fill="{GOLD}" {W(2.8)}/>'
    + sparkle(30, 26, 6, "#fff") + sparkle(100, 20, 5, "#fff") + sparkle(98, 50, 4, "#FFE27A") + sparkle(26, 52, 4, "#FFE27A"),
    "белая пешка на последней горизонтали",
    "дошла до края доски, и над её головой вспыхивает золотая корона — превращение в ферзя")

# Клуб «Пилот»: пешка-пилот в лётных очках летит на клетчатом самолётике
add("pilot-chess-altufyevskoe", "sky",
    cloud(22, 98, 0.8) + cloud(110, 30, 0.6)
    + f'<path d="M20 70 Q20 54 40 54 H98 Q112 58 112 68 Q112 80 98 82 H40 Q20 82 20 70Z" fill="#FFF7EC" {W(3)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="10" height="9" fill="#8A6A55"/>' for x, y in [(44, 56), (64, 56), (54, 65), (74, 65), (44, 73), (64, 73), (84, 56), (84, 73)])
    + f'<path d="M20 70 Q20 54 40 54 H98 Q112 58 112 68 Q112 80 98 82 H40 Q20 82 20 70Z" fill="none" {W(3)}/>'
    + f'<path d="M50 80 L36 104 H52 L70 80Z" fill="{RED}" {W(2.8)}/><path d="M22 66 L10 50 H20 L32 60Z" fill="{RED}" {W(2.6)}/>'
    + f'<rect x="112" y="60" width="6" height="18" rx="2" fill="#C9CED8" {W(2)}/><ellipse cx="121" cy="69" rx="3" ry="18" fill="#fff" fill-opacity=".7" {W(2)}/>'
    + G(66, 46, f'<circle cx="0" cy="-8" r="15" fill="{LIGHT}" {W(3)}/>' + face(0, -6, d=5.5, k=0.55)
        + f'<path d="M-16 -16 H16" stroke="#7A4A2E" stroke-width="4"/><circle cx="-6" cy="-16" r="5" fill="#9DD6F5" {W(2)}/><circle cx="6" cy="-16" r="5" fill="#9DD6F5" {W(2)}/>')
    + f'<path d="M58 48 Q64 52 72 48" fill="none" {W(2)}/>',
    "белая пешка-пилот в лётных очках",
    "летит на самолётике с клетчатым шахматным фюзеляжем среди облаков")

# «Земляне» (рядом цирк и акробатика): чёрная ладья балансирует на полосатом цирковом мяче посреди доски
add("zemlyane-chess-kokkinaki", "green",
    f'<path d="M0 112 H128 V128 H0Z" fill="#FFF7EC"/>'
    + "".join(f'<rect x="{x}" y="112" width="20" height="16" fill="#8A6A55"/>' for x in range(4, 128, 40))
    + f'<path d="M0 112 H128" {W(3)}/>'
    + f'<circle cx="64" cy="94" r="18" fill="{RED}" {W(3)}/>'
    + f'<path d="M50 82 Q64 94 78 82 M47 98 Q64 110 81 98" fill="none" stroke="#fff" stroke-width="4"/>'
    + f'<circle cx="64" cy="94" r="18" fill="none" {W(3)}/>'
    + G(64, 40, rook(c="#3B3355", c2="#5A5378", fc=False), rot=-8, sc=0.66)
    + face(64, 44, d=5.5, k=0.56)
    + f'<path d="M44 46 L28 38 M84 42 L100 32" fill="none" stroke="#3B3355" stroke-width="5" stroke-linecap="round"/>'
    + sparkle(20, 30, 5, "#fff") + sparkle(108, 60, 4, "#fff"),
    "чёрная шахматная ладья-эквилибрист",
    "балансирует на полосатом цирковом мяче посреди доски, раскинув ручки")

# «Джельсомино»: белая пешка поёт так громко, что вокруг разлетаются ноты
add("dzhelsomino-chess-zorge", "pink",
    G(52, 70, pawn(fc=False), sc=0.85)
    + eye(46, 50, 0.6) + eye(58, 50, 0.6)
    + f'<ellipse cx="52" cy="60" rx="4" ry="5" fill="{RED}" {W(2)}/>'
    + f'<path d="M78 46 Q90 40 96 48 M80 58 Q96 54 104 64 M78 70 Q92 72 98 82" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    + f'<path d="M104 20 V36 M104 20 L116 16 V30" fill="none" {W(2.6)}/><ellipse cx="101" cy="37" rx="4" ry="3" fill="{O}"/><ellipse cx="113" cy="31" rx="4" ry="3" fill="{O}"/>'
    + f'<path d="M24 22 V36" fill="none" {W(2.6)}/><ellipse cx="21" cy="37" rx="4" ry="3" fill="{O}"/><path d="M24 22 q6 2 6 8" fill="none" {W(2.4)}/>'
    + f'<path d="M110 92 V104" fill="none" {W(2.6)}/><ellipse cx="107" cy="105" rx="4" ry="3" fill="{O}"/>',
    "белая пешка-певица",
    "поёт во весь голос с широко открытым ртом, вокруг разлетаются ноты и звуковые волны")

# ============================== БОЙ НА МЕЧАХ ==============================
# Федерация фехтования на мечах (Сокол): деревянный тренировочный меч-персонаж в стойке «к бою»
add("fmech-sokol", "orange",
    G(60, 88, sword(L=88, blade="#D9A86C", guard="#A8774F", grip="#6B4A32", w=13, fc=True), rot=20)
    + f'<path d="M20 116 Q64 104 108 116" fill="none" stroke="#fff" stroke-width="3" opacity=".7"/>'
    + sparkle(26, 34, 6, "#fff") + sparkle(108, 92, 4, "#fff"),
    "деревянный тренировочный меч-персонаж",
    "стоит наискосок в стойке «к бою», гордо выпрямив клинок")

# Федерация фехтования на мечах (Сухаревская): мальчик и девочка скрестили мечи, на перекрестье звёздочка
add("fmech-sukharevsky", "blue",
    G(46, 70, sword(L=58), rot=38) + G(82, 70, sword(L=58, guard="#5CB7F2"), rot=-38)
    + sparkle(64, 30, 9, "#FFE27A")
    + G(24, 104, kid(shirt="#4FBF6B", hair="#3B2A20"), sc=0.8)
    + G(104, 104, kid(shirt="#FF7FA8", hair="#C46A2E", girl=True), sc=0.8),
    "мальчик и девочка с деревянными мечами",
    "скрестили мечи над головами, и на перекрестье вспыхивает жёлтая звёздочка")

# Федерация фехтования на мечах (Раменки): рыцарский шлем с плюмажем подмигивает сквозь щель забрала
add("fmech-ramenki", "purple",
    G(64, 70, sword(L=50, blade="#C9CED8"), rot=40) + G(64, 70, sword(L=50, blade="#C9CED8"), rot=-40)
    + f'<path d="M64 20 Q84 6 96 16 Q84 18 76 30Z" fill="{RED}" {W(2.8)}/>'
    + f'<path d="M36 104 V52 Q36 28 64 28 Q92 28 92 52 V104Z" fill="#C9CED8" {W(3)}/>'
    + f'<path d="M64 28 V104" stroke="#A8AFBD" stroke-width="2.4"/>'
    + f'<rect x="40" y="56" width="48" height="10" rx="4" fill="#3B3355"/>'
    + f'<circle cx="52" cy="61" r="3.6" fill="#fff"/><path d="M71 61 Q76 57 81 61" fill="none" stroke="#fff" stroke-width="2.4"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="#3B3355"/>' for x in (52, 58, 70, 76) for y in (80, 90))
    + f'<ellipse cx="44" cy="74" rx="4" ry="2.4" fill="{PINK}" opacity=".7"/><ellipse cx="84" cy="74" rx="4" ry="2.4" fill="{PINK}" opacity=".7"/>',
    "стальной рыцарский шлем-ведро с красным плюмажем",
    "подмигивает сквозь щель забрала на фоне двух скрещённых мечей")

# Федерация фехтования на мечах (Пражская): круглый деревянный щит отражает удар меча, разлетаются звёздочки
add("fmech-prazhskaya", "teal",
    G(98, 40, sword(L=56), rot=-130)
    + f'<circle cx="56" cy="74" r="40" fill="#C98A52" {W(3)}/>'
    + f'<circle cx="56" cy="74" r="34" fill="none" stroke="#8A5A3C" stroke-width="2.4"/>'
    + f'<path d="M22 74 H90 M56 40 V108" stroke="#8A5A3C" stroke-width="2" opacity=".6"/>'
    + f'<circle cx="56" cy="74" r="13" fill="#C9CED8" {W(2.8)}/>'
    + face(56, 74, d=5, k=0.5)
    + sparkle(86, 46, 7, "#FFE27A") + sparkle(102, 62, 4, "#fff") + sparkle(74, 30, 4, "#fff"),
    "круглый деревянный щит с металлической шишкой посередине",
    "принимает на себя удар меча, и от места удара разлетаются искры-звёздочки")

# Федерация фехтования на мечах (Измайловская): девочка-рыцарь в кольчуге поднимает меч у ворот деревянного кремля
add("fmech-izmaylovo", "yellow",
    f'<path d="M4 120 V60 L16 42 L28 60 V120Z M100 120 V60 L112 42 L124 60 V120Z" fill="#C98A52" {W(2.8)}/>'
    f'<path d="M4 60 H28 M100 60 H124" {W(2.4)}/><path d="M28 120 V78 H100 V120" fill="#E0B07A" {W(2.8)}/>'
    + G(58, 98, kid(shirt="#A8AFBD", hair="#E8A43C", girl=True))
    + "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="none" stroke="#6B7280" stroke-width="1.2"/>' for x in (50, 58, 66) for y in (104, 112, 120))
    + f'<path d="M70 104 L84 80" fill="none" stroke="#FFD8B8" stroke-width="7" stroke-linecap="round"/>'
    + G(88, 74, sword(L=56), rot=20),
    "девочка-рыцарь в серебристой кольчуге с рыжими косичками",
    "поднимает меч к небу у бревенчатых ворот деревянного кремля")

# Школа рыцарей «Эскалибур»: меч в камне сияет, вокруг искорки
add("excalibur-knights-tekstilshchiki", "night",
    f'<circle cx="64" cy="58" r="36" fill="#FFE27A" opacity=".25"/>'
    + G(64, 70, sword(L=60, blade="#E8EEF6"), rot=180)
    + f'<path d="M20 120 Q16 92 38 84 Q56 74 80 80 Q108 84 110 120Z" fill="#9AA3B5" {W(3)}/>'
    + f'<path d="M40 100 q8 -4 14 2 M84 104 q6 -6 12 0" fill="none" stroke="#7A8396" stroke-width="2.4"/>'
    + face(64, 102, d=7, k=0.66)
    + sparkle(28, 40, 6, "#FFE27A") + sparkle(102, 34, 5, "#fff") + sparkle(96, 66, 3, "#FFE27A") + sparkle(34, 70, 3, "#fff"),
    "меч Экскалибур в сером валуне",
    "сияет, наполовину вонзённый в улыбающийся камень, вокруг мерцают искорки")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for pid, code in ICONS.items():
        open(os.path.join(OUT, pid + ".svg"), "w").write(code)
    reg = os.path.join(OUT, "subjects.txt")
    lines = [l for l in open(reg, encoding="utf-8") if l.split(" — ", 1)[0] not in SUBJ]
    lines += [line + "\n" for line in SUBJ.values()]
    open(reg, "w", encoding="utf-8").writelines(lines)
    print(len(ICONS), "иконок:", " ".join(ICONS))
