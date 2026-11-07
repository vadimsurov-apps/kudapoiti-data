"""Иконки робота sections, 2026-11-07 (18 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно.
Kurchatov Chess (10 площадок) — не серия: слон-химик, ферзь-капитан, зеркало Зазеркалья, ферзь-дирижёр, король-робот,
ладья-чертёжник, пешка-путешественница, конь-сыщик в лабиринте, ладья-маяк, пешка-пчеловод.
Шахматная школа № 1: король-барабанщик, пешка-грибник, король-поэт, конь-качалка, ферзь-аэростат.
Москомспорт: слон-астроном (Ориента), пешка-волейболистка (Некрасовка), енот-фехтовальщик (ОД-80), кузнечик-фехтовальщик
(Бутово), бобрёнок-гандболист (Москворечье), мальчик-прыгун в длину (Инженерная).
Space ВДНХ — ракетка-космонавт на Луне; «Флэш» Митино — лисёнок-фехтовальщик с молнией.
Сверено со всеми листами icons-catalog/sheet-01..34 и icons-src/subjects.txt (маски, скрещённые клинки, дети-фехтовальщики,
пингвин со шпагой, воланы-персонажи, маяк, осьминоги — уже заняты, не повторяем).
Запуск: python3 tools/icons_sections_1107h.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
PINK, GOLD, RED, ORG = "#FF7FA8", "#FFC93C", "#E8554A", "#F28C38"
SKIN = "#FFD8B8"
WHITE, BLACK = "#FFF8EE", "#3A3550"


def add(pid, bg, body, hero, scene):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def G(x, y, body, rot=0, sc=1.0):
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({sc})">{body}</g>'


# ---------- шахматные фигуры (основание в (0,0), растут вверх) ----------
def dface(c, cx, cy, d, k):
    """мордочка; у тёмных фигур — белые белки, чтобы глаза читались"""
    g = ""
    if c == BLACK:
        g = "".join(f'<circle cx="{cx+dx}" cy="{cy}" r="{5.6*k:.1f}" fill="#fff"/>' for dx in (-d, d))
    return g + face(cx, cy, d=d, k=k)


def base(w, c):
    return (f'<path d="M{-w} 0 H{w} L{w-3} -9 H{-w+3}Z" fill="{c}" {W(3)}/>'
            f'<rect x="{-w+4}" y="-15" width="{2*w-8}" height="7" rx="3" fill="{c}" {W(2.6)}/>')


def pawn(c=WHITE, sc=1.0, faced=True, fy=-56):
    g = (base(22, c)
         + f'<path d="M-15 -14 Q-12 -34 -8 -40 H8 Q12 -34 15 -14Z" fill="{c}" {W(3)}/>'
         + f'<ellipse cx="0" cy="-41" rx="13" ry="4.5" fill="{c}" {W(2.6)}/>'
         + f'<circle cx="0" cy="-56" r="15" fill="{c}" {W(3)}/>')
    if faced:
        g += dface(c, 0, fy, 6, 0.55)
    return G(0, 0, g, sc=sc)


def king(c=WHITE, sc=1.0, faced=True):
    g = (base(24, c)
         + f'<path d="M-17 -14 Q-13 -46 -15 -60 H15 Q13 -46 17 -14Z" fill="{c}" {W(3)}/>'
         + f'<path d="M-19 -60 Q-22 -78 -10 -80 Q0 -72 10 -80 Q22 -78 19 -60Z" fill="{c}" {W(3)}/>'
         + f'<path d="M0 -79 V-96 M-7 -89 H7" fill="none" {W(4.5)}/>'
         + f'<path d="M0 -79 V-96 M-7 -89 H7" fill="none" stroke="{GOLD}" stroke-width="2" stroke-linecap="round"/>')
    if faced:
        g += dface(c, 0, -40, 7, 0.6)
    return G(0, 0, g, sc=sc)


def queen(c=WHITE, sc=1.0, faced=True, crown=True):
    pts = " ".join(f"{x},{y}" for x, y in [(-18, -60), (-22, -84), (-10, -68), (0, -90), (10, -68), (22, -84), (18, -60)])
    g = (base(24, c)
         + f'<path d="M-17 -14 Q-12 -44 -16 -60 H16 Q12 -44 17 -14Z" fill="{c}" {W(3)}/>')
    if crown:
        g += (f'<polygon points="{pts}" fill="{c}" {W(3)}/>'
              + "".join(f'<circle cx="{x}" cy="{y}" r="3.6" fill="{GOLD}" {W(2)}/>' for x, y in [(-22, -86), (0, -92), (22, -86)]))
    if faced:
        g += dface(c, 0, -40, 7, 0.6)
    return G(0, 0, g, sc=sc)


def rook(c=WHITE, sc=1.0, faced=True, fy=-36):
    g = (base(24, c)
         + f'<path d="M-16 -14 L-14 -56 H14 L16 -14Z" fill="{c}" {W(3)}/>'
         + f'<path d="M-20 -56 V-74 H-12 V-66 H-4 V-74 H4 V-66 H12 V-74 H20 V-56Z" fill="{c}" {W(3)}/>')
    if faced:
        g += dface(c, 0, fy, 7, 0.6)
    return G(0, 0, g, sc=sc)


def bishop(c=WHITE, sc=1.0, faced=True):
    g = (base(22, c)
         + f'<path d="M-14 -14 Q-10 -36 -8 -42 H8 Q10 -36 14 -14Z" fill="{c}" {W(3)}/>'
         + f'<ellipse cx="0" cy="-43" rx="14" ry="4.5" fill="{c}" {W(2.6)}/>'
         + f'<path d="M0 -84 Q-18 -70 -14 -56 Q-10 -46 0 -46 Q10 -46 14 -56 Q18 -70 0 -84Z" fill="{c}" {W(3)}/>'
         + f'<path d="M4 -76 L-6 -62" stroke="{O}" stroke-width="3" stroke-linecap="round"/>'
         + f'<circle cx="0" cy="-89" r="5" fill="{c}" {W(2.6)}/>')
    if faced:
        g += dface(c, 0, -60, 6, 0.5)
    return G(0, 0, g, sc=sc)


def knight_head(c=WHITE):
    return (f'<path d="M14 0 Q20 -26 10 -46 Q2 -60 -14 -58 L-12 -66 L-20 -56 Q-34 -44 -36 -28 Q-36 -20 -28 -20 '
            f'Q-20 -24 -14 -28 Q-12 -14 -18 0Z" fill="{c}" {W(3)}/>'
            f'<path d="M10 -46 Q20 -36 16 -12" fill="none" {W(2.4)}/>')


def knight(c=WHITE, sc=1.0, flip=False):
    g = base(22, c) + G(0, -12, knight_head(c)) + f'<circle cx="-16" cy="-48" r="5.2" fill="#fff"/>' + eye(-16, -48, 0.7) + \
        f'<ellipse cx="-24" cy="-36" rx="3.6" ry="2.2" fill="{PINK}" opacity=".7"/>' + \
        f'<circle cx="-31" cy="-35" r="1.6" fill="{O}"/>'
    if flip:
        g = f'<g transform="scale(-1 1)">{g}</g>'
    return G(0, 0, g, sc=sc)


def ground(y, c, wave=8):
    return f'<path d="M-6 {y} Q32 {y-wave} 64 {y} Q96 {y+wave} 134 {y} V140 H-6Z" fill="{c}" {W(2.6)}/>'


def checks(x0, y0, n, m, cw, a="#FFF2D8", b="#8E6A9E"):
    return "".join(f'<rect x="{x0+i*cw}" y="{y0+j*cw}" width="{cw}" height="{cw}" fill="{a if (i+j) % 2 else b}"/>'
                   for i in range(n) for j in range(m))


# ============================== Kurchatov Chess ==============================
# Центральный (Курчатов): чёрный слон-химик в белом халате с колбой
add("kurchatov-chess-central", "teal",
    G(58, 116, bishop(BLACK, sc=1.0))
    # халат
    + f'<path d="M38 106 L42 74 Q58 66 74 74 L78 106Z" fill="#fff" {W(3)}/>'
    + f'<path d="M58 70 V106 M48 72 L58 82 L68 72" fill="none" {W(2.4)}/>'
    + f'<circle cx="62" cy="84" r="1.8" fill="{O}"/><circle cx="62" cy="94" r="1.8" fill="{O}"/>'
    # рука с колбой
    + f'<path d="M72 78 Q86 76 90 66" fill="none" stroke="#fff" stroke-width="9" stroke-linecap="round"/>'
    + f'<path d="M72 78 Q86 76 90 66" fill="none" {W(2.2)}/>'
    + f'<path d="M88 30 H100 M90 30 V44 L80 64 Q78 70 84 70 H104 Q110 70 108 64 L98 44 V30" fill="#F4FBFF" {W(3)}/>'
    + f'<path d="M84 58 H104 L107 64 Q108 68 104 68 H84 Q80 68 81 64Z" fill="#7BE87B"/>'
    + f'<path d="M88 30 H100 M90 30 V44 L80 64 Q78 70 84 70 H104 Q110 70 108 64 L98 44 V30" fill="none" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#C9FFC4" {W(1.8)}/>' for x, y, r in [(94, 20, 4), (102, 12, 3), (88, 10, 2.5)]),
    "чёрный шахматный слон-химик в белом халате",
    "поднял над головой стеклянную колбу с зелёной жидкостью, из которой поднимаются пузыри")

# Алые Паруса: белый ферзь-капитан у штурвала под алым парусом
wheel = (f'<circle r="15" fill="none" stroke="#8A5A3C" stroke-width="5"/><circle r="15" fill="none" {W(1.6)}/>'
         + "".join(f'<path d="M0 0 L{19*math.cos(a):.1f} {19*math.sin(a):.1f}" stroke="#8A5A3C" stroke-width="3.4" stroke-linecap="round"/>'
                   for a in [i * math.pi / 4 for i in range(8)])
         + f'<circle r="4" fill="{GOLD}" {W(2)}/>')
add("kurchatov-chess-alye-parusa", "sky",
    f'<path d="M66 8 V96" stroke="#8A5A3C" stroke-width="4"/>'
    + f'<path d="M70 12 Q110 30 108 82 L70 82Z" fill="#E8344A" {W(3)}/>'
    + f'<path d="M62 18 Q34 40 36 78 L62 78Z" fill="#FF5A6E" {W(3)}/>'
    + f'<path d="M-6 112 Q30 104 64 112 Q98 120 134 110 V140 H-6Z" fill="#3E8FE0" {W(2.4)}/>'
    + f'<path d="M14 94 H118 L106 116 H26Z" fill="#B87A4A" {W(3)}/>'
    + G(44, 98, queen(WHITE, sc=0.72))
    # треуголка
    + G(45, 25, f'<path d="M-16 4 Q0 -10 16 4 Q0 9 -16 4Z" fill="#2E3A7A" {W(2.6)}/><circle cx="0" cy="-2" r="2.4" fill="{GOLD}"/>', rot=-14)
    + G(84, 96, wheel),
    "белый шахматный ферзь-капитан в синей треуголке",
    "стоит на палубе у деревянного штурвала, над ним надуваются алые паруса")

# Зазеркалье: зеркало в золотой раме, в котором белый конь отражается чёрным
add("kurchatov-chess-zazerkalye", "purple",
    checks(-6, 108, 12, 2, 12)
    + f'<path d="M-6 108 H134" {W(2.6)}/>'
    + f'<ellipse cx="82" cy="58" rx="30" ry="40" fill="#F0C64A" {W(3)}/>'
    + f'<ellipse cx="82" cy="58" rx="23" ry="33" fill="#CFE8FF" {W(2.6)}/>'
    + f'<path d="M66 40 Q70 30 78 28" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    + f'<path d="M82 98 V108 M70 108 H94" {W(3.4)}/>'
    + G(84, 86, knight(BLACK, sc=0.62, flip=True))
    + G(34, 108, knight(WHITE, sc=0.85))
    + eye(76, 18, 0.5) + eye(88, 18, 0.5)
    + sparkle(112, 22, 5) + sparkle(16, 30, 4),
    "овальное зеркало в золотой раме с глазками на макушке рамы",
    "перед ним стоит белый шахматный конь, а в стекле отражается тот же конь, только чёрный")

# Брокколини: чёрный ферзь-дирижёр управляет хором пешек
add("kurchatov-chess-brokkolini", "pink",
    f'<rect x="-6" y="112" width="140" height="24" fill="#B5584A"/><path d="M-6 112 H134" {W(2.6)}/>'
    + G(42, 114, queen(BLACK, sc=0.92))
    + f'<path d="M32 90 L42 95 L52 90 L52 100 L42 96 L32 100Z" fill="#fff" {W(2)}/>'
    + f'<path d="M56 64 Q66 56 72 46" fill="none" stroke="{BLACK}" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M70 48 L84 22" stroke="#fff" stroke-width="3" stroke-linecap="round"/><path d="M70 48 L84 22" {W(1.2)}/>'
    + "".join(G(x, 114, pawn(WHITE, sc=0.42)) for x in (82, 100, 118))
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="4" ry="3" fill="{O}"/><path d="M{x+3.5} {y} V{y-12} Q{x+8} {y-10} {x+9} {y-6}" fill="none" {W(2)}/>'
              for x, y in [(92, 40), (110, 30), (104, 56)]),
    "чёрный шахматный ферзь-дирижёр с белым воротничком-бабочкой",
    "взмахивает палочкой перед хором из трёх белых пешек, над которыми летят ноты")

# СмартСкул Раменки: белый король-робот с экраном на груди
add("kurchatov-chess-ramenki", "night",
    f'<rect x="-6" y="114" width="140" height="20" fill="#2E3270"/><path d="M-6 114 H134" {W(2.6)}/>'
    # корпус-король
    + f'<rect x="38" y="52" width="52" height="56" rx="8" fill="#DDE4F0" {W(3)}/>'
    + f'<rect x="32" y="106" width="64" height="10" rx="3" fill="#DDE4F0" {W(3)}/>'
    + f'<path d="M36 52 Q34 32 48 30 Q56 40 64 30 Q72 40 80 30 Q94 32 92 52Z" fill="#DDE4F0" {W(3)}/>'
    + f'<path d="M64 30 V12 M57 19 H71" fill="none" {W(4.5)}/><path d="M64 30 V12 M57 19 H71" stroke="#FF5A6E" stroke-width="2" stroke-linecap="round"/>'
    + f'<circle cx="64" cy="10" r="3" fill="#FFE14D" {W(1.6)}/>'
    + eye(54, 42, 0.6) + eye(74, 42, 0.6)
    # экран с доской
    + f'<rect x="46" y="62" width="36" height="34" rx="3" fill="#1D2250" {W(2.6)}/>'
    + checks(50, 66, 4, 4, 7, a="#7CF0C8", b="#1D2250")
    + f'<path d="M57 90 Q66 78 74 70" fill="none" stroke="#FFE14D" stroke-width="2.6" stroke-linecap="round"/>'
    + f'<path d="M70 69 L75 69 L74 74" fill="none" stroke="#FFE14D" stroke-width="2.6" stroke-linecap="round"/>'
    + f'<path d="M38 72 Q24 74 22 60 M90 72 Q104 74 106 60" fill="none" stroke="#DDE4F0" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M38 72 Q24 74 22 60 M90 72 Q104 74 106 60" fill="none" {W(1.8)}/>'
    + sparkle(16, 26, 4) + sparkle(112, 30, 5) + sparkle(104, 96, 3),
    "белый шахматный король-робот с антенной-крестиком",
    "на экране у него на груди светится клетчатая доска, и жёлтая стрелка рисует следующий ход")

# СмартСкул Новаторская (ул. Лобачевского): оранжевая ладья-чертёжник с циркулем
add("kurchatov-chess-lobachevskogo", "yellow",
    f'<path d="M10 88 L118 80 L124 124 L4 130Z" fill="#fff" {W(2.6)}/>'
    + "".join(f'<path d="M{10+i*12} {88-i*0.9:.1f} L{6+i*13} 130" stroke="#BFD8F0" stroke-width="1.2"/>' for i in range(1, 9))
    + "".join(f'<path d="M{8} {96+j*9} L{120} {88+j*9}" stroke="#BFD8F0" stroke-width="1.2"/>' for j in range(4))
    + f'<ellipse cx="88" cy="106" rx="20" ry="11" fill="none" stroke="#3E7FD8" stroke-width="3"/>'
    + G(40, 112, rook("#FF9F45", sc=0.9))
    # циркуль
    + f'<path d="M86 34 L70 104 M86 34 L106 104" fill="none" stroke="#7A8090" stroke-width="4" stroke-linecap="round"/>'
    + f'<circle cx="86" cy="32" r="5" fill="{GOLD}" {W(2.2)}/>'
    + f'<path d="M106 104 l2 6" stroke="#3E7FD8" stroke-width="3" stroke-linecap="round"/>'
    + f'<path d="M58 62 Q72 50 82 40" fill="none" stroke="#FF9F45" stroke-width="7" stroke-linecap="round"/><path d="M58 62 Q72 50 82 40" fill="none" {W(1.8)}/>',
    "оранжевая шахматная ладья-чертёжник",
    "чертит большим циркулем ровный синий круг на листе в клетку")

# Полиглотики: чёрная пешка-путешественница с клетчатым чемоданом под указателем
add("kurchatov-chess-smolnaya", "green",
    ground(108, "#8BD46E")
    + f'<path d="M96 24 V110" stroke="#8A5A3C" stroke-width="5"/>'
    + f'<path d="M96 28 H124 L130 36 L124 44 H96Z" fill="#FF7F50" {W(2.4)}/>'
    + f'<path d="M96 50 H70 L64 58 L70 66 H96Z" fill="#5CC8F0" {W(2.4)}/>'
    + f'<path d="M96 72 H122 L128 80 L122 88 H96Z" fill="#FFE14D" {W(2.4)}/>'
    + G(46, 112, pawn(BLACK, sc=1.1))
    + f'<rect x="58" y="86" width="30" height="24" rx="4" fill="#fff" {W(2.6)}/>'
    + checks(60, 88, 4, 3, 6.5, a="#fff", b="#E8554A")
    + f'<rect x="58" y="86" width="30" height="24" rx="4" fill="none" {W(2.6)}/>'
    + f'<path d="M66 86 V80 H80 V86" fill="none" {W(2.6)}/>'
    + f'<path d="M30 30 Q34 22 40 26" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>',
    "чёрная шахматная пешка-путешественница с клетчатым чемоданом",
    "стоит на тропинке под дорожным указателем с тремя разноцветными стрелками")

# Реутов «Головоломка»: белый конь-сыщик с лупой в лабиринте из живой изгороди
hedge = "#3FAE5A"
add("kurchatov-chess-reutov", "orange",
    f'<rect x="-6" y="70" width="140" height="70" fill="#E9D7A8"/>'
    + "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{hedge}" {W(2.4)}/>'
              for x, y, w, h in [(-6, 70, 30, 12), (40, 70, 94, 12), (-6, 96, 54, 12), (76, 96, 58, 12), (24, 82, 12, 26),
                                 (100, 82, 12, 14), (-6, 120, 140, 14)])
    + f'<path d="M30 116 H64 V90 H88" fill="none" stroke="#E8554A" stroke-width="2.4" stroke-dasharray="4 4"/>'
    + G(64, 88, knight(WHITE, sc=0.95))
    + f'<circle cx="28" cy="40" r="12" fill="#CFEFFF" opacity=".8" {W(3)}/><path d="M37 49 L48 58" stroke="#8A5A3C" stroke-width="6" stroke-linecap="round"/>'
    + f'<path d="M37 49 L48 58" {W(1.6)}/>',
    "белый шахматный конь-сыщик с увеличительным стеклом",
    "ищет выход из зелёного лабиринта живой изгороди, за ним тянется красный пунктир пути")

# Красногорск «Океана»: белая ладья-маяк светит над ночным морем
add("kurchatov-chess-krasnogorsk-okeana", "blue",
    f'<path d="M64 32 L134 8 V60Z" fill="#FFF6B0" opacity=".75"/>'
    + f'<path d="M64 32 L-6 14 V56Z" fill="#FFF6B0" opacity=".45"/>'
    + f'<path d="M-6 96 Q20 88 40 96 Q64 104 88 96 Q110 88 134 96 V140 H-6Z" fill="#2B5FB8" {W(2.4)}/>'
    + f'<path d="M30 92 Q64 80 98 92 L94 112 H34Z" fill="#8E95A6" {W(2.6)}/>'
    + G(64, 96, rook(WHITE, sc=0.86, fy=-24))
    + f'<rect x="51" y="54" width="26" height="8" fill="#E8344A"/>'
    + G(64, 96, rook("none", sc=0.86, faced=False))
    + f'<circle cx="64" cy="32" r="5" fill="#FFE14D" {W(2)}/>'
    + f'<path d="M6 116 Q14 110 22 116 M100 120 Q108 114 116 120" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>',
    "белая шахматная ладья-маяк с красной полосой",
    "стоит на камнях и светит жёлтым лучом с зубчатой макушки над морем, о подножие плещут волны")

# Красногорск «Бихайв»: белая пешка-пчеловод в шляпе с сеткой у сотов
hexes = "".join(f'<path d="M{x} {y-9} l8 4.6 v9.2 l-8 4.6 l-8 -4.6 v-9.2Z" fill="#FFC93C" {W(2)}/>'
                for x, y in [(98, 70), (114, 70), (106, 84), (90, 84), (122, 84), (98, 98), (114, 98)])
add("kurchatov-chess-pavshinsky", "yellow",
    hexes
    + G(48, 118, pawn(WHITE, sc=1.15))
    + f'<ellipse cx="48" cy="44" rx="28" ry="6" fill="#F4E3C3" {W(2.6)}/>'
    + f'<path d="M34 44 Q34 26 48 26 Q62 26 62 44" fill="#F4E3C3" {W(2.6)}/>'
    + f'<path d="M24 46 L28 66 M72 46 L68 66" stroke="#7A8090" stroke-width="1.6" stroke-dasharray="2 2"/>'
    + "".join(G(x, y, f'<ellipse rx="7" ry="5.5" fill="#FFD23F" {W(2)}/><path d="M-2 -5 V5 M2 -5 V5" stroke="{O}" stroke-width="2"/>'
                        f'<ellipse cx="-2" cy="-7" rx="4" ry="3" fill="#E4F6FF" opacity=".9" {W(1.4)}/><ellipse cx="3" cy="-7" rx="4" ry="3" fill="#E4F6FF" opacity=".9" {W(1.4)}/>',
                        rot=r)
              for x, y, r in [(86, 30, -10), (112, 42, 15), (18, 82, 0)]),
    "белая шахматная пешка-пчеловод в шляпе с сеткой",
    "стоит возле золотых медовых сот, вокруг неё кружат три полосатые пчёлки")


# ============================== Шахматная школа № 1 ==============================
# Первомайская: чёрный король-барабанщик марширует
drum = (f'<ellipse cx="0" cy="0" rx="20" ry="6" fill="#fff" {W(2.6)}/>'
        f'<path d="M-20 0 V22 Q0 30 20 22 V0" fill="#E8344A" {W(2.8)}/>'
        f'<path d="M-20 4 L-10 22 L0 6 L10 22 L20 4" fill="none" stroke="{GOLD}" stroke-width="2.6"/>'
        f'<ellipse cx="0" cy="0" rx="20" ry="6" fill="#fff" {W(2.6)}/>')
add("chess1-pervomayskaya", "pink",
    checks(-6, 110, 12, 3, 12, a="#FFE6F0", b="#C46A9A") + f'<path d="M-6 110 H134" {W(2.6)}/>'
    + "".join(f'<path d="M{x} 10 V46" stroke="#8A5A3C" stroke-width="2"/><path d="M{x} 12 l14 6 l-14 6Z" fill="{c}" {W(1.6)}/>'
              for x, c in [(14, "#E8344A"), (104, "#3E7FD8")])
    + G(48, 112, king(BLACK, sc=0.95))
    + G(82, 80, drum, rot=-6)
    + f'<path d="M62 70 L78 58 M64 82 L96 62" stroke="#C98547" stroke-width="3.4" stroke-linecap="round"/>'
    + f'<circle cx="78" cy="58" r="3" fill="#fff" {W(1.6)}/><circle cx="96" cy="62" r="3" fill="#fff" {W(1.6)}/>'
    + f'<path d="M98 40 l4 -6 M106 46 l6 -4" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>',
    "чёрный шахматный король-барабанщик",
    "марширует по праздничной клетчатой площади с флажками и бьёт палочками в красный барабан")

# Лосиноостровский: чёрная пешка-грибник с корзинкой на опушке
mush = lambda x, y, sc, cap: G(x, y, f'<path d="M-5 0 Q-6 -10 -4 -14 H4 Q6 -10 5 0Z" fill="#FFF2D8" {W(2)}/>'
                                     f'<path d="M-13 -13 Q0 -30 13 -13Z" fill="{cap}" {W(2.4)}/>', sc=sc)
add("chess1-tayninskaya", "green",
    "".join(f'<path d="M{x} {y} l-14 30 h28Z M{x} {y+16} l-17 30 h34Z" fill="#2E8B57" {W(2.4)}/><rect x="{x-3}" y="{y+46}" width="6" height="8" fill="#8A5A3C"/>'
            for x, y in [(16, 30), (112, 22)])
    + ground(104, "#9BD86E", 6)
    + G(56, 116, pawn(BLACK, sc=1.05))
    + f'<path d="M72 92 Q90 104 108 92" fill="#C98547" {W(2.6)}/>'
    + f'<path d="M70 92 H110 L104 112 H76Z" fill="#E0A96A" {W(2.6)}/>'
    + f'<path d="M74 98 H106 M76 104 H104" stroke="#B5783A" stroke-width="1.8"/>'
    + f'<path d="M78 92 Q90 72 102 92" fill="none" stroke="#B5783A" stroke-width="3.4"/>'
    + mush(84, 92, 0.6, "#8A4A2A") + mush(96, 92, 0.5, "#E8344A")
    + mush(24, 112, 0.8, "#8A4A2A") + mush(116, 114, 0.7, "#C9733A"),
    "чёрная шахматная пешка-грибник",
    "собирает грибы в плетёную корзинку на лесной опушке среди ёлок")

# Переделкино: белый король-поэт с гусиным пером при свече
add("chess1-lukinskaya", "orange",
    f'<rect x="-6" y="106" width="140" height="30" fill="#8A5A3C"/><path d="M-6 106 H134" {W(2.6)}/>'
    + f'<path d="M66 100 Q64 92 72 90 H118 Q126 92 122 100 Q118 108 110 106 H76 Q68 108 66 100Z" fill="#FFF6E0" {W(2.6)}/>'
    + "".join(f'<path d="M78 {94+i*4} H{112-i*6}" stroke="#7A6A8A" stroke-width="1.4"/>' for i in range(3))
    + G(40, 112, king(WHITE, sc=0.9))
    + f'<path d="M56 74 Q70 74 80 84" fill="none" stroke="{WHITE}" stroke-width="7" stroke-linecap="round"/><path d="M56 74 Q70 74 80 84" fill="none" {W(1.8)}/>'
    + f'<path d="M80 86 Q74 60 92 40 Q96 56 86 70 Q84 78 80 86Z" fill="#fff" {W(2.4)}/><path d="M80 86 Q84 66 90 48" fill="none" {W(1.6)}/>'
    + f'<rect x="108" y="66" width="10" height="26" rx="2" fill="#FFF2D8" {W(2.4)}/>'
    + f'<path d="M113 66 Q106 56 113 46 Q120 56 113 66Z" fill="#FFB020" {W(2)}/>'
    + f'<circle cx="113" cy="56" r="14" fill="#FFE14D" opacity=".3"/>',
    "белый шахматный король-поэт",
    "пишет гусиным пером стихи на свитке за столом при зажжённой свече")

# г. Московский: лошадка-качалка с головой шахматного коня, на ней пешка
add("chess1-moskovsky", "sky",
    f'<rect x="-6" y="112" width="140" height="24" fill="#C9A06A"/><path d="M-6 112 H134" {W(2.6)}/>'
    + f'<path d="M14 100 Q64 126 114 100" fill="none" stroke="#B5584A" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M14 100 Q64 126 114 100" fill="none" {W(1.8)}/>'
    + f'<path d="M40 108 L46 86 M88 108 L82 86" stroke="#8A5A3C" stroke-width="5" stroke-linecap="round"/>'
    + f'<rect x="38" y="74" width="54" height="16" rx="8" fill="#F4E3C3" {W(2.8)}/>'
    + G(98, 90, knight("#F4E3C3", sc=0.95, flip=True).replace(base(22, "#F4E3C3"), ""))
    + f'<path d="M36 80 Q24 82 20 94" fill="none" stroke="#8A5A3C" stroke-width="4" stroke-linecap="round"/>'
    + G(60, 76, pawn(BLACK, sc=0.55)),
    "деревянная лошадка-качалка с головой шахматного коня",
    "раскачивается на красных полозьях, а на её спине верхом сидит маленькая чёрная пешка")

# Коммунарка (пос. Газопровод): белый ферзь-аэростат с корзиной пешек
add("chess1-gazoprovod", "purple",
    "".join(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="8" fill="#fff" opacity=".9"/>' for x, y, rx in [(18, 110, 22), (108, 116, 26), (112, 30, 14)])
    + f'<path d="M64 6 Q100 10 98 44 Q96 66 72 78 H56 Q32 66 30 44 Q28 10 64 6Z" fill="{WHITE}" {W(3)}/>'
    + "".join(f'<path d="M{x} {y} Q64 {y-6} {128-x} {y}" fill="none" stroke="#C9B8F0" stroke-width="2"/>' for x, y in [(34, 34), (32, 50)])
    + "".join(f'<circle cx="{x}" cy="{y}" r="3.6" fill="{GOLD}" {W(2)}/>' for x, y in [(46, 14), (64, 8), (82, 14)])
    + face(64, 46, d=9, k=0.75)
    + f'<path d="M56 78 L52 94 M72 78 L76 94" {W(2.4)}/>'
    + f'<path d="M48 94 H80 L76 112 H52Z" fill="#C98547" {W(2.6)}/>'
    + f'<path d="M50 100 H78 M51 106 H77" stroke="#8A5A3C" stroke-width="1.6"/>'
    + G(58, 96, pawn(BLACK, sc=0.32)) + G(71, 96, pawn(WHITE, sc=0.32)),
    "белый шахматный ферзь-аэростат с короной из золотых шариков",
    "парит над облаками, а в плетёной корзине под ним едут чёрная и белая пешки")

# ============================== Москомспорт ==============================
# СК «Ориента»: чёрный слон-астроном с подзорной трубой и созвездием-конём
stars = [(84, 18), (96, 14), (104, 24), (98, 36), (110, 44), (90, 44)]
add("ms-orienta-chess", "night",
    "".join(f'<path d="M{a[0]} {a[1]} L{b[0]} {b[1]}" stroke="#9FB0FF" stroke-width="1.6" stroke-dasharray="3 3"/>'
            for a, b in zip(stars, stars[1:]))
    + "".join(sparkle(x, y, 4.5, "#FFE14D") for x, y in stars)
    + sparkle(20, 20, 3) + sparkle(30, 44, 2.5)
    + f'<path d="M-6 110 Q64 98 134 110 V140 H-6Z" fill="#2E3270" {W(2.4)}/>'
    + G(44, 116, bishop(BLACK, sc=0.95))
    + G(70, 64, f'<rect x="0" y="-7" width="34" height="14" rx="3" fill="#C98547" {W(2.6)}/>'
                f'<rect x="30" y="-9" width="10" height="18" rx="3" fill="{GOLD}" {W(2.4)}/>'
                f'<rect x="-6" y="-5" width="8" height="10" rx="2" fill="#8A5A3C" {W(2)}/>', rot=-36)
    + f'<path d="M58 80 Q66 76 70 68" fill="none" stroke="{BLACK}" stroke-width="7" stroke-linecap="round"/>',
    "чёрный шахматный слон-астроном",
    "смотрит в подзорную трубу на ночное созвездие, сложенное буквой «Г», как ход коня")

# ДС «Некрасовка»: белая пешка-волейболистка в наколенниках бьёт по мячу над сеткой
add("ms-nekrasovka-sections", "orange",
    f'<rect x="-6" y="112" width="140" height="24" fill="#E9A15C"/><path d="M-6 112 H134" {W(2.6)}/>'
    + f'<path d="M100 40 V114" stroke="#7A6A8A" stroke-width="4"/>'
    + f'<rect x="100" y="42" width="40" height="30" fill="none" stroke="#fff" stroke-width="1.6"/>'
    + "".join(f'<path d="M{100+i*7} 42 V72" stroke="#fff" stroke-width="1.2"/>' for i in range(1, 5))
    + "".join(f'<path d="M100 {42+j*7.5} H134" stroke="#fff" stroke-width="1.2"/>' for j in range(1, 4))
    + f'<rect x="100" y="40" width="40" height="5" fill="#fff" {W(1.6)}/>'
    + G(50, 104, pawn(WHITE, sc=1.05), rot=-8)
    + f'<rect x="30" y="92" width="10" height="7" rx="2" fill="#3E7FD8" {W(1.8)}/><rect x="58" y="88" width="10" height="7" rx="2" fill="#3E7FD8" {W(1.8)}/>'
    + f'<path d="M62 44 Q74 32 80 22" fill="none" stroke="{WHITE}" stroke-width="8" stroke-linecap="round"/><path d="M62 44 Q74 32 80 22" fill="none" {W(2)}/>'
    + G(90, 18, f'<circle r="13" fill="#FFE066" {W(2.6)}/><path d="M-13 -1 Q0 -7 13 -3 M-3 -13 Q-8 0 -1 13" fill="none" {W(1.8)}/>'
                f'<path d="M-13 -1 Q-8 -10 -3 -13Z" fill="#3E7FD8" {W(1.6)}/>')
    + f'<path d="M106 12 l8 -4 M108 22 l9 0" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'
    + f'<path d="M10 104 Q14 96 22 98" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="3 3"/>',
    "белая шахматная пешка-волейболистка в синих наколенниках",
    "в прыжке у волейбольной сетки бьёт сверху по жёлто-синему мячу")

# Space ВДНХ: бадминтонная ракетка-космонавт на Луне
add("space-vdnh-badminton", "night",
    f'<circle cx="104" cy="24" r="12" fill="#5CC8F0" {W(2.4)}/><path d="M96 20 Q102 16 106 22 Q104 30 96 28Z" fill="#7BE87B"/>'
    + sparkle(18, 22, 4) + sparkle(40, 12, 2.5) + sparkle(78, 10, 3)
    + f'<path d="M-6 104 Q40 94 70 100 Q100 106 134 98 V140 H-6Z" fill="#C7CBD6" {W(2.6)}/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r/2.6:.1f}" fill="#A4A9B8" {W(1.8)}/>' for x, y, r in [(20, 116, 9), (92, 118, 12), (60, 126, 6)])
    + G(50, 66, f'<rect x="-3.5" y="18" width="7" height="34" rx="3" fill="#FFE14D" {W(2.6)}/>'
                f'<rect x="-5" y="38" width="10" height="18" rx="3" fill="#3E7FD8" {W(2.4)}/>'
                f'<ellipse cx="0" cy="-8" rx="20" ry="26" fill="#FF8FB8" {W(3)}/>'
                f'<ellipse cx="0" cy="-8" rx="14" ry="20" fill="#FFF0F6" {W(2)}/>'
                + "".join(f'<path d="M{x} -26 V10" stroke="#C46A9A" stroke-width="1.2"/>' for x in (-8, -4, 0, 4, 8))
                + "".join(f'<path d="M-13 {y} H13" stroke="#C46A9A" stroke-width="1.2"/>' for y in (-20, -14, -8, -2, 4))
                + face(0, -8, d=6, k=0.6)
                + f'<ellipse cx="0" cy="-10" rx="27" ry="33" fill="#CFEFFF" opacity=".35" {W(2.4)}/>'
                f'<path d="M-14 -34 Q-6 -40 4 -40" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>', rot=14)
    + G(98, 64, f'<path d="M-8 -6 L8 -10 L4 6 L-6 4Z" fill="#fff" {W(2)}/><circle cx="-8" cy="6" r="5" fill="#E8554A" {W(2)}/>', rot=30)
    + f'<path d="M72 44 Q84 50 90 60" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="3 4"/>',
    "розовая бадминтонная ракетка-космонавт в стеклянном шлеме",
    "отбивает волан на Луне среди серых кратеров, вдали висит голубая Земля")

# «Флэш» Митино: рыжий лисёнок-фехтовальщик, со шпаги срывается молния
add("flash-fencing-mitino", "teal",
    f'<rect x="-6" y="112" width="140" height="24" fill="#B9C2CC"/><path d="M-6 112 H134 M-6 118 H134" {W(2)}/>'
    + f'<path d="M30 112 L40 90 M54 112 L50 92" stroke="#fff" stroke-width="9" stroke-linecap="round"/>'
    + f'<path d="M30 112 L40 90 M54 112 L50 92" fill="none" {W(2)}/>'
    + f'<path d="M24 86 Q8 80 6 64 Q16 72 26 74Z" fill="#F28C38" {W(2.4)}/><path d="M6 64 Q8 70 12 72" fill="#fff" {W(1.6)}/>'
    + f'<path d="M30 92 Q28 66 46 62 Q62 62 60 92Z" fill="#fff" {W(3)}/>'
    + f'<path d="M58 72 Q72 66 80 64" fill="none" stroke="#fff" stroke-width="9" stroke-linecap="round"/><path d="M58 72 Q72 66 80 64" fill="none" {W(2)}/>'
    + f'<path d="M80 64 L114 52" stroke="#9AA4B2" stroke-width="3" stroke-linecap="round"/>'
    + f'<ellipse cx="80" cy="64" rx="3" ry="6" fill="{GOLD}" {W(1.8)}/>'
    + f'<path d="M114 52 L124 42 L118 42 L128 30" fill="none" stroke="#FFE14D" stroke-width="3.4" stroke-linejoin="round"/>'
    # голова лисёнка
    + f'<path d="M32 46 L30 26 L42 36Z M56 44 L62 26 L50 36Z" fill="#F28C38" {W(2.6)}/>'
    + f'<circle cx="46" cy="48" r="15" fill="#F28C38" {W(3)}/>'
    + f'<path d="M34 52 Q46 66 58 52 Q52 58 46 58 Q40 58 34 52Z" fill="#fff" {W(1.8)}/>'
    + eye(41, 45, 0.6) + eye(53, 45, 0.6) + f'<circle cx="47" cy="54" r="2.2" fill="{O}"/>',
    "рыжий лисёнок-фехтовальщик в белом костюме",
    "делает выпад на фехтовальной дорожке, и с кончика его шпаги срывается жёлтая молния")

# ОД-80: енот-фехтовальщик (своя «маска» на мордочке) салютует шпагой у лаврового венка
add("ms-od80-fencing", "yellow",
    f'<rect x="-6" y="114" width="140" height="22" fill="#8E95A6"/><path d="M-6 114 H134" {W(2.4)}/>'
    + f'<path d="M94 92 Q86 72 100 58 M110 92 Q118 72 104 58" fill="none" stroke="#3FAE5A" stroke-width="5" stroke-linecap="round"/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="4" ry="2.4" fill="#5CC86E" transform="rotate({r} {x} {y})" {W(1.2)}/>'
              for x, y, r in [(90, 80, -60), (90, 68, -40), (114, 80, 60), (114, 68, 40), (96, 60, -20), (108, 60, 20)])
    + f'<rect x="88" y="92" width="28" height="22" rx="3" fill="#F0C64A" {W(2.6)}/>'
    + f'<path d="M24 112 Q28 96 34 92 M50 112 Q48 98 46 92" stroke="#fff" stroke-width="9" stroke-linecap="round"/><path d="M24 112 Q28 96 34 92 M50 112 Q48 98 46 92" fill="none" {W(1.8)}/>'
    + f'<path d="M26 94 Q24 70 40 66 Q56 70 54 94Z" fill="#fff" {W(3)}/>'
    + f'<path d="M18 92 Q4 98 6 84 Q10 76 20 82" fill="#8E8A9E" {W(2.2)}/><path d="M8 86 l6 2 M10 80 l6 3" stroke="{O}" stroke-width="2"/>'
    + f'<path d="M54 78 Q62 70 64 58" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round"/><path d="M54 78 Q62 70 64 58" fill="none" {W(1.8)}/>'
    + f'<path d="M64 58 V14" stroke="#9AA4B2" stroke-width="3" stroke-linecap="round"/><ellipse cx="64" cy="58" rx="7" ry="2.6" fill="{GOLD}" {W(1.8)}/>'
    + f'<path d="M26 40 L24 24 L36 32Z M54 40 L58 24 L46 32Z" fill="#8E8A9E" {W(2.4)}/>'
    + f'<circle cx="40" cy="48" r="16" fill="#B7B3C6" {W(3)}/>'
    + f'<path d="M26 46 Q32 38 40 44 Q48 38 54 46 Q48 54 40 50 Q32 54 26 46Z" fill="{BLACK}"/>'
    + eye(33, 46, 0.55).replace('fill="#3B3355"', 'fill="#fff"', 1) + eye(47, 46, 0.55).replace('fill="#3B3355"', 'fill="#fff"', 1)
    + f'<ellipse cx="40" cy="56" rx="7" ry="5" fill="#fff" {W(1.6)}/><circle cx="40" cy="54" r="2" fill="{O}"/>',
    "енот-фехтовальщик в белом костюме — со своей чёрной «маской» на мордочке",
    "салютует поднятой шпагой у пьедестала с лавровым венком")

# ФОК «Южное Бутово»: зелёный кузнечик-фехтовальщик делает выпад над лугом
add("ms-butovo-fencing", "sky",
    ground(108, "#8BD46E", 6)
    + "".join(f'<path d="M{x} 110 q2 -12 6 -16 M{x+4} 110 q0 -10 -4 -14" fill="none" stroke="#3FAE5A" stroke-width="2.4" stroke-linecap="round"/>' for x in (8, 112, 120))
    + f'<path d="M20 30 Q40 24 52 34" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    # тело
    + f'<path d="M22 88 Q30 70 56 66 Q74 66 76 76 Q70 90 42 92Z" fill="#7BD35A" {W(3)}/>'
    + f'<path d="M34 72 Q50 62 72 68" fill="none" {W(1.8)}/>'
    + f'<path d="M30 84 L12 62 L14 104" fill="none" stroke="#5DB848" stroke-width="5" stroke-linejoin="round"/><path d="M30 84 L12 62 L14 104" fill="none" {W(1.6)}/>'
    + f'<path d="M46 92 L44 108 M58 90 L62 108" stroke="#5DB848" stroke-width="4" stroke-linecap="round"/>'
    + f'<circle cx="80" cy="62" r="13" fill="#7BD35A" {W(3)}/>'
    + f'<path d="M78 50 Q70 30 58 24 M84 50 Q90 30 104 22" fill="none" {W(2)}/>'
    + eye(76, 60, 0.6) + eye(87, 60, 0.6) + f'<path d="M78 68 Q82 71 86 68" fill="none" {W(2)}/>'
    + f'<path d="M70 76 Q84 80 92 78" fill="none" stroke="#5DB848" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M92 78 L126 72" stroke="#9AA4B2" stroke-width="3" stroke-linecap="round"/><ellipse cx="92" cy="78" rx="2.6" ry="6" fill="{GOLD}" {W(1.8)}/>'
    + sparkle(122, 64, 4),
    "зелёный кузнечик-фехтовальщик на длинных прыгучих ногах",
    "делает глубокий выпад тонкой шпагой над летним лугом")

# МСК Москворечье: бобрёнок-гандболист бросает мяч у реки
add("ms-moskvorechye-handball", "blue",
    f'<path d="M-6 96 Q30 90 64 96 Q98 102 134 94 V140 H-6Z" fill="#7DC4F0" {W(2.4)}/>'
    + f'<path d="M-6 112 H134 V140 H-6Z" fill="#E9D7A8"/><path d="M-6 112 H134" {W(2.4)}/>'
    + f'<path d="M92 46 H128 V112" fill="none" stroke="#E8344A" stroke-width="6"/>'
    + "".join(f'<path d="M{x} 46 h5" stroke="#fff" stroke-width="6"/>' for x in (100, 114))
    + "".join(f'<path d="M{128} {y} v5" stroke="#fff" stroke-width="6"/>' for y in (60, 80, 100))
    + f'<path d="M92 46 H128 V112" fill="none" {W(1.6)}/>'
    + "".join(f'<path d="M{96+i*8} 50 L{100+i*6} 110" stroke="#fff" stroke-width="1" opacity=".8"/>' for i in range(4))
    # бобрёнок
    + f'<ellipse cx="30" cy="110" rx="14" ry="6" fill="#6B4A2E" {W(2.2)}/><path d="M20 108 l4 4 M28 106 l2 5 M36 108 l-1 5" stroke="#4A3220" stroke-width="1.6"/>'
    + f'<path d="M34 108 Q30 84 44 76 Q58 74 62 90 Q62 104 54 110Z" fill="#2E55B8" {W(3)}/>'
    + f'<text x="47" y="100" font-family="Arial" font-weight="700" font-size="12" fill="#fff">7</text>'
    + f'<path d="M38 112 l-2 6 M54 110 l4 6" stroke="#B5783A" stroke-width="6" stroke-linecap="round"/>'
    + f'<path d="M56 80 Q66 66 70 52" fill="none" stroke="#B5783A" stroke-width="7" stroke-linecap="round"/><path d="M56 80 Q66 66 70 52" fill="none" {W(1.6)}/>'
    + f'<circle cx="46" cy="60" r="16" fill="#B5783A" {W(3)}/>'
    + f'<circle cx="33" cy="48" r="5" fill="#B5783A" {W(2.2)}/><circle cx="59" cy="48" r="5" fill="#B5783A" {W(2.2)}/>'
    + f'<ellipse cx="46" cy="66" rx="8" ry="6" fill="#E9C9A0" {W(1.6)}/><circle cx="46" cy="63" r="2.4" fill="{O}"/>'
    + f'<rect x="43" y="68" width="6" height="5" fill="#fff" {W(1.2)}/>'
    + eye(40, 57, 0.55) + eye(52, 57, 0.55)
    + G(74, 42, f'<circle r="10" fill="#FFD23F" {W(2.4)}/><path d="M-10 0 Q0 -5 10 0 M0 -10 Q-5 0 0 10" fill="none" stroke="#3E7FD8" stroke-width="2.2"/>')
    + f'<path d="M80 36 Q86 30 90 30" fill="none" stroke="#fff" stroke-width="2.2" stroke-dasharray="3 3"/>',
    "бобрёнок-гандболист в синей майке с номером 7",
    "на песчаном берегу реки замахивается и бросает мяч в полосатые красно-белые ворота")

# СК «На Инженерной»: мальчик-прыгун в длину летит над ямой с песком
add("ms-inzhenernaya-athletics", "green",
    f'<rect x="-6" y="104" width="76" height="32" fill="#D8573F"/>'
    + "".join(f'<path d="M-6 {y} H70" stroke="#fff" stroke-width="1.6"/>' for y in (112, 122))
    + f'<rect x="58" y="104" width="10" height="5" fill="#fff" {W(1.6)}/>'
    + f'<path d="M68 104 H134 V136 H68Z" fill="#F2D27A"/><path d="M-6 104 H134" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1.4" fill="#C9A04A"/>' for x, y in [(80, 112), (96, 118), (110, 110), (124, 120), (88, 126)])
    + f'<path d="M104 104 q-4 -6 0 -8 q6 0 4 8" fill="#C9A04A"/>'
    + f'<path d="M8 100 Q20 70 40 62" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="4 5"/>'
    # мальчик в полёте
    + G(76, 70, f'<path d="M-12 -2 Q-10 -18 4 -18 Q16 -16 14 2 Z" fill="#3FAE5A" {W(3)}/>'
                f'<path d="M14 0 Q26 4 30 16 M6 4 Q16 14 26 22" fill="none" stroke="{SKIN}" stroke-width="7" stroke-linecap="round"/>'
                f'<path d="M14 0 Q26 4 30 16 M6 4 Q16 14 26 22" fill="none" {W(1.6)}/>'
                f'<path d="M30 16 l6 2 M26 22 l6 3" stroke="#3E7FD8" stroke-width="6" stroke-linecap="round"/>'
                f'<path d="M-8 -12 Q-22 -26 -12 -38 M2 -16 Q4 -34 18 -40" fill="none" stroke="{SKIN}" stroke-width="7" stroke-linecap="round"/>'
                f'<path d="M-8 -12 Q-22 -26 -12 -38 M2 -16 Q4 -34 18 -40" fill="none" {W(1.6)}/>'
                f'<circle cx="-14" cy="-6" r="12" fill="{SKIN}" {W(3)}/>'
                f'<path d="M-26 -8 Q-24 -20 -12 -18 Q-2 -18 -2 -10 Q-12 -14 -26 -8Z" fill="#8A5A3C" {W(2)}/>'
                + eye(-18, -4, 0.5) + eye(-10, -4, 0.5)
                + f'<ellipse cx="-14" cy="2" rx="3" ry="2.4" fill="{O}"/>', rot=-10, sc=1.2)
    + "".join(f'<path d="M{x} {y} l-10 2" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>' for x, y in [(30, 40), (26, 52), (30, 64)]),
    "мальчик-прыгун в длину в зелёной майке",
    "в полёте над ямой с песком тянет вперёд обе ноги, позади белая планка отталкивания на красной дорожке")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for pid, code in ICONS.items():
        open(os.path.join(OUT, pid + ".svg"), "w").write(code)
    reg = os.path.join(OUT, "subjects.txt")
    lines = [l for l in open(reg, encoding="utf-8") if l.split(" — ", 1)[0] not in SUBJ]
    lines += [line + "\n" for line in SUBJ.values()]
    open(reg, "w", encoding="utf-8").writelines(lines)
    print(len(ICONS), "иконок:", " ".join(ICONS))
