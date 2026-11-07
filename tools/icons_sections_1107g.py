"""Иконки робота sections, 2026-11-07 (15 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно.
ПБК ЦСКА — не серия: майка на верёвке, легковушка с мячом на багажнике, девочка в гогглах с броском крюком,
суслик у норки, мяч в граффити-кольцо. Шахматы «Чемпионы» — 11 разных сюжетов (король-Нептун, король-садовник,
пешка-первоклашка, конь на лугу, ферзь-фея превращает пешку, ладья-ракета, пешка-альпинист, две пешки за партией,
конь в шкатулке, король читает сказку, конь-тяжеловоз с тележкой пешек).
Сверено с листами icons-catalog/sheet-01..33 и icons-src/subjects.txt.
Запуск: python3 tools/icons_sections_1107g.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
PINK, GOLD, RED, ORG, LIGHT = "#FF7FA8", "#FFC93C", "#E8554A", "#F28C38", "#FFF7EC"
SKIN = "#FFD8B8"
BALL = "#F2862E"
WHITE, BLACK = "#FFF8EE", "#3A3550"


def add(pid, bg, body, hero, scene):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def G(x, y, body, rot=0, sc=1.0):
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({sc})">{body}</g>'


def bball(r=20, faced=True, k=None):
    """баскетбольный мяч вокруг (0,0)"""
    k = k or r / 26
    g = (f'<circle r="{r}" fill="{BALL}" {W(3)}/>'
         f'<path d="M0 {-r} V{r} M{-r} 0 H{r}" fill="none" {W(2.2)}/>'
         f'<path d="M{-r*0.7:.1f} {-r*0.72:.1f} Q{-r*0.25:.1f} 0 {-r*0.7:.1f} {r*0.72:.1f} M{r*0.7:.1f} {-r*0.72:.1f} Q{r*0.25:.1f} 0 {r*0.7:.1f} {r*0.72:.1f}" fill="none" {W(2.2)}/>')
    if faced:
        g += (f'<circle cx="{-r*0.42:.1f}" cy="{-r*0.12:.1f}" r="{r*0.2:.1f}" fill="{BALL}"/>'
              f'<circle cx="{r*0.42:.1f}" cy="{-r*0.12:.1f}" r="{r*0.2:.1f}" fill="{BALL}"/>'
              f'<rect x="{-r*0.3:.1f}" y="{r*0.1:.1f}" width="{r*0.6:.1f}" height="{r*0.36:.1f}" fill="{BALL}"/>'
              + face(0, -r * 0.12, d=r * 0.42, k=k))
    return g


def vball(r=18, k=None):
    k = k or r / 26
    return (f'<circle r="{r}" fill="#FFE066" {W(3)}/>'
            f'<path d="M{-r} {-2} Q0 {-r*0.5:.1f} {r} {-6}" fill="none" {W(2.2)}/>'
            f'<path d="M{-r*0.2:.1f} {-r} Q{-r*0.6:.1f} 0 {-r*0.1:.1f} {r}" fill="none" {W(2.2)}/>'
            f'<path d="M{-r} {-2} Q{-r*0.6:.1f} {-r*0.8:.1f} {-r*0.2:.1f} {-r}Z" fill="#3E7FD8" {W(2.2)}/>'
            f'<path d="M{-r*0.1:.1f} {r} Q{r*0.7:.1f} {r*0.4:.1f} {r} {-6} Q{r*0.4:.1f} {r*0.1:.1f} {-r*0.1:.1f} {r}Z" fill="#3E7FD8" {W(2.2)}/>'
            + face(r * 0.25, r * 0.15, d=r * 0.3, k=k))


# ---------- шахматные фигуры (основание в (0,0), растут вверх) ----------
def base(w, c):
    return (f'<path d="M{-w} 0 H{w} L{w-3} -9 H{-w+3}Z" fill="{c}" {W(3)}/>'
            f'<rect x="{-w+4}" y="-15" width="{2*w-8}" height="7" rx="3" fill="{c}" {W(2.6)}/>')


def pawn(c=WHITE, sc=1.0, faced=True):
    g = (base(22, c)
         + f'<path d="M-15 -14 Q-12 -34 -8 -40 H8 Q12 -34 15 -14Z" fill="{c}" {W(3)}/>'
         + f'<ellipse cx="0" cy="-41" rx="13" ry="4.5" fill="{c}" {W(2.6)}/>'
         + f'<circle cx="0" cy="-56" r="15" fill="{c}" {W(3)}/>')
    if faced:
        g += face(0, -56, d=6, k=0.55)
    return G(0, 0, g, sc=sc)


def king(c=WHITE, sc=1.0, faced=True):
    g = (base(24, c)
         + f'<path d="M-17 -14 Q-13 -46 -15 -60 H15 Q13 -46 17 -14Z" fill="{c}" {W(3)}/>'
         + f'<path d="M-19 -60 Q-22 -78 -10 -80 Q0 -72 10 -80 Q22 -78 19 -60Z" fill="{c}" {W(3)}/>'
         + f'<path d="M0 -79 V-96 M-7 -89 H7" fill="none" {W(4.5)}/>'
         + f'<path d="M0 -79 V-96 M-7 -89 H7" fill="none" stroke="{GOLD}" stroke-width="2" stroke-linecap="round"/>')
    if faced:
        g += face(0, -40, d=7, k=0.6)
    return G(0, 0, g, sc=sc)


def queen(c=WHITE, sc=1.0, faced=True):
    pts = " ".join(f"{x},{y}" for x, y in [(-18, -60), (-22, -84), (-10, -68), (0, -90), (10, -68), (22, -84), (18, -60)])
    g = (base(24, c)
         + f'<path d="M-17 -14 Q-12 -44 -16 -60 H16 Q12 -44 17 -14Z" fill="{c}" {W(3)}/>'
         + f'<polygon points="{pts}" fill="{c}" {W(3)}/>'
         + "".join(f'<circle cx="{x}" cy="{y}" r="3.6" fill="{GOLD}" {W(2)}/>' for x, y in [(-22, -86), (0, -92), (22, -86)]))
    if faced:
        g += face(0, -40, d=7, k=0.6)
    return G(0, 0, g, sc=sc)


def rook(c=WHITE, sc=1.0, faced=True):
    g = (base(24, c)
         + f'<path d="M-16 -14 L-14 -56 H14 L16 -14Z" fill="{c}" {W(3)}/>'
         + f'<path d="M-20 -56 V-74 H-12 V-66 H-4 V-74 H4 V-66 H12 V-74 H20 V-56Z" fill="{c}" {W(3)}/>')
    if faced:
        g += face(0, -36, d=7, k=0.6)
    return G(0, 0, g, sc=sc)


def knight_head(c=WHITE):
    """голова шахматного коня, смотрит влево; низ шеи около y=0"""
    return (f'<path d="M14 0 Q20 -26 10 -46 Q2 -60 -14 -58 L-12 -66 L-20 -56 Q-34 -44 -36 -28 Q-36 -20 -28 -20 '
            f'Q-20 -24 -14 -28 Q-12 -14 -18 0Z" fill="{c}" {W(3)}/>'
            f'<path d="M10 -46 Q20 -36 16 -12" fill="none" {W(2.4)}/>')


def knight(c=WHITE, sc=1.0):
    g = base(22, c) + G(0, -12, knight_head(c)) + f'<circle cx="-16" cy="-48" r="5.2" fill="#fff"/>' + eye(-16, -48, 0.7) + \
        f'<ellipse cx="-24" cy="-36" rx="3.6" ry="2.2" fill="{PINK}" opacity=".7"/>' + \
        f'<circle cx="-31" cy="-35" r="1.6" fill="{O}"/>'
    return G(0, 0, g, sc=sc)


def board_strip(y, h, n=10, x0=-6, w=140, a="#F4E3C3", b="#8A5A3C"):
    cw = w / n
    return "".join(f'<rect x="{x0 + i*cw:.1f}" y="{y}" width="{cw:.1f}" height="{h}" fill="{a if i % 2 else b}"/>' for i in range(n)) + \
        f'<path d="M{x0} {y} H{x0+w}" {W(2.6)}/>'


# ============================== ПБК ЦСКА ==============================
# Текстильщики: баскетбольная майка сушится на бельевой верёвке
add("pbk-cska-tekstilshchiki", "pink",
    f'<path d="M-6 26 Q64 40 134 26" fill="none" stroke="#7A6A8A" stroke-width="2.6"/>'
    + f'<path d="M40 34 Q44 30 50 32 Q56 40 64 40 Q72 40 78 32 Q84 30 88 34 L96 50 Q92 56 90 60 L92 112 H36 L38 60 Q36 56 32 50Z" fill="#2E55B8" {W(3)}/>'
    + f'<path d="M50 32 Q56 46 64 46 Q72 46 78 32" fill="none" stroke="{RED}" stroke-width="4"/>'
    + f'<path d="M36 104 H92" stroke="{RED}" stroke-width="4"/>'
    + G(64, 76, bball(19))
    + "".join(f'<rect x="{x-3}" y="24" width="6" height="16" rx="2" fill="{GOLD}" {W(2.2)}/>' for x in (46, 82))
    + sparkle(110, 54, 6) + sparkle(18, 64, 5),
    "баскетбольная майка-безрукавка с мячом на груди",
    "сушится на бельевой верёвке на двух жёлтых прищепках после тренировки")

# Автозаводская: красная легковушка везёт на багажнике огромный мяч
add("pbk-cska-avtozavodskaya", "sky",
    f'<rect x="-6" y="108" width="140" height="30" fill="#8E95A6"/>'
    + "".join(f'<rect x="{x}" y="115" width="12" height="3" fill="#fff"/>' for x in (6, 34, 62, 90, 118))
    + f'<path d="M18 104 L22 86 Q26 78 36 76 L44 64 H84 L94 76 Q106 78 110 86 L112 104Z" fill="{RED}" {W(3)}/>'
    + f'<path d="M48 68 H62 V78 H42Z M68 68 H82 L88 78 H68Z" fill="#CFEFFF" {W(2.2)}/>'
    + f'<circle cx="104" cy="90" r="4" fill="{GOLD}" {W(2)}/>'
    + "".join(f'<circle cx="{x}" cy="106" r="10" fill="#3A3550" {W(2.6)}/><circle cx="{x}" cy="106" r="4" fill="#BFC4CF"/>' for x in (38, 92))
    + f'<path d="M44 62 H86" {W(3.4)}/><path d="M50 62 V56 M80 62 V56" {W(3)}/>'
    + G(65, 36, bball(24))
    + f'<path d="M44 40 Q65 70 86 40" fill="none" stroke="#5A3E8A" stroke-width="3.4"/>',
    "маленькая красная легковушка",
    "везёт по дороге на багажнике крыши огромный баскетбольный мяч, пристёгнутый ремнём")

# Щербинка: девочка в спортивных очках бросает крюком
kid_g = (f'<path d="M-14 26 Q-16 -2 0 -4 Q16 -2 14 26Z" fill="#FFD23F" {W(3)}/>'
         f'<path d="M-6 26 L-16 52 M6 26 L4 52" fill="none" stroke="{SKIN}" stroke-width="8" stroke-linecap="round"/>'
         f'<path d="M-6 26 L-16 52 M6 26 L4 52" fill="none" {W(2)}/>'
         f'<path d="M-20 50 h-8 M2 52 h10" stroke="#fff" stroke-width="7" stroke-linecap="round"/>'
         f'<path d="M10 2 Q26 -14 30 -34" fill="none" stroke="{SKIN}" stroke-width="8" stroke-linecap="round"/>'
         f'<path d="M-10 4 Q-24 10 -26 0" fill="none" stroke="{SKIN}" stroke-width="8" stroke-linecap="round"/>'
         f'<circle cx="0" cy="-20" r="15" fill="{SKIN}" {W(3)}/>'
         f'<path d="M-15 -22 Q-14 -40 0 -38 Q14 -40 15 -22 Q6 -30 -15 -22Z" fill="#2B2B3A" {W(2.4)}/>'
         f'<path d="M14 -34 Q24 -30 20 -20" fill="none" stroke="#2B2B3A" stroke-width="5" stroke-linecap="round"/>'
         f'<rect x="-13" y="-24" width="26" height="9" rx="4.5" fill="#6FD3F5" {W(2.4)}/>'
         f'<path d="M-5 -10 Q0 -6 5 -10" fill="none" {W(2.2)}/>')
add("pbk-cska-shcherbinka", "green",
    f'<rect x="-6" y="110" width="140" height="24" fill="#E9A15C"/><path d="M-6 110 H134" {W(2.6)}/>'
    + f'<rect x="96" y="12" width="34" height="28" rx="3" fill="#fff" {W(3)}/><rect x="106" y="22" width="14" height="10" fill="none" stroke="{RED}" stroke-width="2.4"/>'
    + f'<ellipse cx="104" cy="44" rx="13" ry="4" fill="none" stroke="{RED}" stroke-width="3.4"/>'
    + f'<path d="M92 44 L96 60 H112 L116 44" fill="none" stroke="#fff" stroke-width="2"/>'
    + G(52, 66, kid_g, rot=-8)
    + G(84, 26, bball(14, k=0.5))
    + f'<path d="M70 50 Q74 40 70 34" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 4"/>',
    "девочка в спортивных очках-гогглах и жёлтой форме",
    "в прыжке бросает мяч крюком одной рукой под кольцо с щитом")

# Коммунарка: суслик у норки держит мяч над головой
add("pbk-cska-kommunarka", "yellow",
    f'<path d="M-6 100 Q64 88 134 100 V134 H-6Z" fill="#8BD46E" {W(2.6)}/>'
    + f'<ellipse cx="64" cy="108" rx="30" ry="9" fill="#5A3A2A" {W(2.6)}/>'
    + f'<path d="M44 108 Q40 76 48 62 Q56 52 64 52 Q72 52 80 62 Q88 76 84 108Z" fill="#D9A86A" {W(3)}/>'
    + f'<path d="M54 106 Q52 84 64 80 Q76 84 74 106Z" fill="#F4DDB4"/>'
    + f'<path d="M50 66 Q38 54 40 40 M78 66 Q90 54 88 40" fill="none" stroke="#D9A86A" stroke-width="9" stroke-linecap="round"/>'
    + f'<path d="M50 66 Q38 54 40 40 M78 66 Q90 54 88 40" fill="none" {W(2)}/>'
    + f'<circle cx="52" cy="54" r="4" fill="#D9A86A" {W(2)}/><circle cx="76" cy="54" r="4" fill="#D9A86A" {W(2)}/>'
    + face(64, 66, d=7, k=0.55)
    + f'<ellipse cx="64" cy="72" rx="3" ry="2" fill="{O}"/>'
    + G(64, 30, bball(19, faced=False))
    + "".join(f'<path d="M{x} 100 l3 -8 l3 8" fill="#5CB85C" {W(1.8)}/>' for x in (12, 22, 100, 112)),
    "суслик с пухлыми щёчками",
    "встал столбиком у норки на газоне и держит над головой баскетбольный мяч")

# Авиаторов: мяч летит в кольцо, нарисованное баллончиком на кирпичной стене
bricks = "".join(f'<rect x="{x + (14 if r % 2 else 0)}" y="{6 + r*14}" width="26" height="12" rx="1.5" fill="#B5584A" stroke="#7E3A33" stroke-width="1.4"/>'
                 for r in range(9) for x in range(-20, 140, 28))
add("pbk-cska-aviatorov", "purple",
    bricks
    + f'<rect x="64" y="20" width="56" height="40" rx="4" fill="none" stroke="#7CF0C8" stroke-width="5"/>'
    + f'<rect x="80" y="32" width="24" height="16" fill="none" stroke="#FF7FD0" stroke-width="4"/>'
    + f'<ellipse cx="92" cy="64" rx="18" ry="5" fill="none" stroke="#FFE14D" stroke-width="5"/>'
    + f'<path d="M76 66 L82 88 M92 68 V90 M108 66 L102 88 M78 78 H106" fill="none" stroke="#FFE14D" stroke-width="3"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="#7CF0C8"/>' for x, y in [(60, 70), (124, 18), (70, 98)])
    + f'<path d="M8 112 Q30 90 38 72" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="4 5"/>'
    + G(46, 60, bball(21), rot=12)
    + f'<rect x="96" y="100" width="14" height="26" rx="4" fill="#5CC8F0" {W(2.6)}/><rect x="99" y="94" width="8" height="7" fill="#fff" {W(2)}/>',
    "кирпичная стена с кольцом, нарисованным баллончиком",
    "баскетбольный мяч-персонаж летит прямо в граффити-кольцо, у стены стоит баллончик краски")

# ============================== ВОЛЕЙБОЛ ==============================
# Москва-98: белка-летяга планирует над сеткой и бьёт по мячу
add("moskva98-volley-udaltsova", "teal",
    f'<path d="M-6 96 H134" stroke="#fff" stroke-width="4"/>'
    + "".join(f'<path d="M{x} 96 V134" stroke="#fff" stroke-width="1.6" opacity=".8"/>' for x in range(0, 130, 10))
    + "".join(f'<path d="M-6 {y} H134" stroke="#fff" stroke-width="1.6" opacity=".8"/>' for y in range(106, 134, 10))
    + f'<path d="M14 70 Q24 50 44 54 L64 50 Q80 48 84 62 Q78 76 62 76 Q48 86 32 80 Q18 82 14 70Z" fill="#B58A62" {W(3)}/>'
    + f'<path d="M32 76 Q48 82 62 74 Q54 68 42 70Z" fill="#F2DEC4"/>'
    + f'<path d="M18 72 Q4 82 2 98 Q10 86 22 80" fill="#B58A62" {W(2.6)}/>'
    + f'<path d="M64 52 Q72 40 80 32" fill="none" stroke="#B58A62" stroke-width="8" stroke-linecap="round"/>'
    + f'<path d="M64 52 Q72 40 80 32" fill="none" {W(1.6)}/>'
    + f'<circle cx="80" cy="62" r="14" fill="#B58A62" {W(3)}/>'
    + f'<path d="M70 52 l0 -9 l7 5 M84 49 l5 -7 l2 9" fill="#B58A62" {W(2.4)}/>'
    + f'<circle cx="75" cy="61" r="5" fill="#fff" {W(1.8)}/><circle cx="86" cy="61" r="5" fill="#fff" {W(1.8)}/>'
    + eye(75, 61, 0.6) + eye(86, 61, 0.6)
    + f'<ellipse cx="81" cy="69" rx="2.4" ry="1.8" fill="{O}"/>'
    + G(94, 30, vball(19, k=0.55))
    + f'<path d="M114 16 l8 -5 M116 30 l9 0 M113 44 l7 4" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>',
    "белка-летяга с перепонками между лапками",
    "планирует над волейбольной сеткой и в полёте бьёт лапкой по мячу")

# ============================== НАСТОЛЬНЫЙ ТЕННИС ==============================
add("horoshkola-table-tennis", "blue",
    f'<path d="M14 112 A44 44 0 0 1 102 112Z" fill="#FFE27A" {W(3)}/>'
    + "".join(f'<path d="M{58 + 40*math.cos(math.radians(a)):.1f} {112 - 40*math.sin(math.radians(a)):.1f} L{58 + 34*math.cos(math.radians(a)):.1f} {112 - 34*math.sin(math.radians(a)):.1f}" {W(2)}/>'
              for a in range(10, 180, 20))
    + f'<path d="M58 112 L92 74" fill="none" stroke="{RED}" stroke-width="3" stroke-dasharray="4 4"/>'
    + G(46, 52, f'<rect x="-6" y="18" width="12" height="30" rx="5" fill="#C98A4E" {W(3)}/>'
        f'<ellipse cx="0" cy="0" rx="28" ry="30" fill="{RED}" {W(3)}/>' + face(0, 0, d=9, k=0.8), rot=-30)
    + f'<circle cx="96" cy="68" r="9" fill="#fff" {W(2.6)}/>'
    + f'<path d="M100 26 Q108 46 98 58" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 4"/>'
    + sparkle(110, 22, 6, GOLD),
    "ракетка для пинг-понга с транспортиром",
    "отбивает белый мячик и меряет транспортиром угол отскока")

# ============================== ШАХМАТЫ «ЧЕМПИОНЫ» ==============================
def waves(y, c="#4FA6E8"):
    d = f"M-6 {y}" + "".join(" q8 -7 16 0 t16 0" for _ in range(9)) + " V134 H-6Z"
    return f'<path d="{d}" fill="{c}" {W(2.6)}/>'


add("champions-chess-federativny", "blue",
    G(60, 104, king(WHITE, sc=0.92))
    + waves(92)
    + f'<path d="M100 120 V30" {W(4)}/><path d="M100 120 V30" stroke="{GOLD}" stroke-width="2"/>'
    + f'<path d="M88 40 V26 M100 36 V18 M112 40 V26 M88 36 Q100 44 112 36" fill="none" {W(4)}/>'
    + f'<path d="M88 40 V26 M100 36 V18 M112 40 V26 M88 36 Q100 44 112 36" fill="none" stroke="{GOLD}" stroke-width="2"/>'
    + f'<path d="M78 76 Q90 70 98 74" fill="none" stroke="{WHITE}" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M78 76 Q90 70 98 74" fill="none" {W(1.8)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="#fff" stroke-width="2"/>' for x, y, r in [(22, 70, 4), (16, 56, 3), (28, 44, 2.4)]),
    "шахматный король-Нептун с золотым трезубцем",
    "поднимается из морских волн по пояс в воде, вокруг пузырьки")


add("champions-chess-sovetskaya-6a", "green",
    f'<path d="M-6 98 H134 V134 H-6Z" fill="#7A4E34"/>'
    + "".join(f'<rect x="{x}" y="98" width="17.5" height="12" fill="#A06A46"/>' for x in range(-6, 134, 35))
    + "".join(f'<rect x="{x}" y="110" width="17.5" height="12" fill="#A06A46"/>' for x in range(11, 134, 35))
    + f'<path d="M-6 98 H134" {W(2.6)}/>'
    + "".join(G(x, 100, pawn(WHITE, sc=0.42)) + f'<path d="M{x} 74 Q{x-8} 64 {x-12} 68 Q{x-8} 74 {x} 74 Q{x+8} 62 {x+12} 66 Q{x+8} 72 {x} 74Z" fill="#5CB85C" {W(1.8)}/>'
              for x in (22, 48))
    + G(92, 100, king(BLACK, sc=0.72))
    + f'<path d="M64 46 L72 52 L82 54 L78 66 L62 66Z" fill="#6FB6E8" {W(2.6)}/>'
    + f'<path d="M64 50 L44 40" {W(3)}/><ellipse cx="42" cy="39" rx="5" ry="3" fill="#6FB6E8" {W(2)}/>'
    + "".join(f'<path d="M{x} {y} q-2 4 0 6 q2 -2 0 -6Z" fill="#7FD3FF" stroke="#3E8FD8" stroke-width="1.2"/>' for x, y in [(34, 46), (40, 54), (30, 58)]),
    "чёрный шахматный король-садовник с голубой лейкой",
    "поливает белые пешки, которые прорастают с листочками на клетчатой грядке")


add("champions-chess-sovetskaya-16a", "yellow",
    board_strip(108, 30, n=8, a="#FFFFFF", b="#C9B48A")
    + G(56, 114, pawn(WHITE, sc=1.15))
    + f'<path d="M46 40 Q56 30 66 40 Q56 46 46 40Z" fill="{PINK}" {W(2.2)}/><circle cx="56" cy="40" r="3.4" fill="#fff" {W(1.8)}/>'
    + f'<path d="M84 96 L94 58" stroke="#3E8A3E" stroke-width="3"/><path d="M90 98 L96 62 M80 92 L98 66" stroke="#3E8A3E" stroke-width="3"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="8" fill="{c}" {W(2.2)}/><circle cx="{x}" cy="{y}" r="3" fill="{GOLD}"/>'
              for x, y, c in [(94, 56, RED), (100, 64, "#FFFFFF"), (86, 62, "#B98AF0")])
    + f'<path d="M76 92 Q88 96 96 90 L92 102 Q84 104 78 100Z" fill="#E8F4FF" {W(2.2)}/>',
    "белая пешка-первоклашка с бантом на макушке",
    "идёт 1 сентября по клетчатой дорожке с букетом из трёх цветов")


add("champions-chess-nekrasova", "sky",
    f'<path d="M-6 96 Q64 84 134 96 V134 H-6Z" fill="#8FD86E" {W(2.6)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="14" height="10" fill="#6FBF52" opacity=".8"/>' for x, y in [(4, 106), (32, 116), (88, 116), (116, 106), (18, 124), (74, 124)])
    + G(70, 112, knight(BLACK, sc=1.0), rot=-16)
    + f'<path d="M34 96 q-3 -9 0 -14 M38 96 q1 -11 5 -15 M42 96 q3 -8 8 -10" fill="none" stroke="#3E8A3E" stroke-width="3" stroke-linecap="round"/>'
    + f'<path d="M84 26 q6 -8 10 0 q6 -8 10 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    + f'<circle cx="24" cy="28" r="10" fill="#FFE066" {W(2.4)}/>',
    "чёрный шахматный конь-жеребёнок",
    "наклонил голову и щиплет пучок травы на лугу с клетчатыми кочками, светит солнышко")


add("champions-chess-golovashkina", "purple",
    board_strip(110, 30, n=8)
    + G(78, 112, queen(WHITE, sc=0.95))
    + f'<path d="M58 70 L34 56" {W(4)}/><path d="M58 70 L34 56" stroke="{GOLD}" stroke-width="2"/>'
    + sparkle(32, 54, 8, "#FFE066")
    + G(28, 112, pawn(BLACK, sc=0.6, faced=True))
    + f'<path d="M18 66 L22 58 L28 64 L34 58 L38 66Z" fill="{GOLD}" {W(2)}/>'
    + "".join(sparkle(x, y, r, "#fff") for x, y, r in [(12, 80, 5), (46, 84, 4), (20, 46, 4), (44, 46, 3)]),
    "белый шахматный ферзь-фея с волшебной палочкой",
    "превращает чёрную пешку в ферзя — над пешкой в искрах появляется корона")


add("champions-chess-gagarina", "night",
    "".join(sparkle(x, y, r, "#fff") for x, y, r in [(18, 20, 4), (104, 30, 5), (24, 70, 3), (112, 74, 3), (90, 14, 3)])
    + f'<path d="M44 110 Q50 94 64 92 Q78 94 84 110 Q74 102 64 104 Q54 102 44 110Z" fill="{ORG}" {W(2.4)}/>'
    + f'<path d="M52 112 Q58 100 64 100 Q70 100 76 112Z" fill="#FFE066"/>'
    + f'<path d="M44 86 L34 98 L46 94Z M84 86 L94 98 L82 94Z" fill="{RED}" {W(2.4)}/>'
    + G(64, 96, rook(WHITE, sc=0.95, faced=False))
    + f'<circle cx="64" cy="52" r="10" fill="#7FD3FF" {W(2.6)}/>' + face(64, 54, d=4, k=0.45, blush=False)
    + face(64, 74, d=8, k=0.5, mouth=True)
    + f'<path d="M30 126 H98" stroke="#fff" stroke-width="2" opacity=".5"/>',
    "белая шахматная ладья-ракета с иллюминатором",
    "стартует с огненным хвостом в звёздное небо, из иллюминатора выглядывает пешка-космонавт")


add("champions-chess-komsomolskaya", "orange",
    f'<path d="M4 124 L40 70 L56 86 L78 52 L124 124Z" fill="#8C7FA0" {W(3)}/>'
    + f'<path d="M40 70 L46 80 L36 82Z M78 52 L86 66 L72 66Z" fill="#fff"/>'
    + G(30, 124, rook(BLACK, sc=0.45, faced=False)) + G(98, 124, king(WHITE, sc=0.4, faced=False))
    + G(64, 124, queen(BLACK, sc=0.42, faced=False))
    + G(78, 54, pawn(WHITE, sc=0.55))
    + f'<path d="M88 30 V8" {W(3)}/><path d="M88 8 L108 14 L88 20Z" fill="{RED}" {W(2.4)}/>'
    + f'<path d="M84 34 Q86 30 90 32" fill="none" {W(2.4)}/>',
    "белая пешка-альпинист с красным флажком",
    "покорила вершину горы, у подножия которой стоят ладья, ферзь и король")


add("champions-chess-kotovskogo", "pink",
    f'<rect x="34" y="76" width="60" height="8" rx="2" fill="#C98A4E" {W(2.6)}/>'
    + f'<path d="M44 84 L40 118 M84 84 L88 118" {W(3)}/>'
    + "".join(f'<rect x="{38 + i*6.5:.1f}" y="70" width="6.5" height="6" fill="{"#fff" if i % 2 else "#8A5A3C"}"/>' for i in range(8))
    + f'<path d="M38 70 H90" {W(1.6)}/>'
    + G(20, 118, pawn(WHITE, sc=0.88))
    + G(108, 118, pawn(BLACK, sc=0.88))
    + G(52, 70, f'<path d="M-2 0 Q0 -8 2 0Z" fill="#fff"/><circle cy="-9" r="3" fill="#fff" {W(1.6)}/>')
    + G(76, 70, f'<path d="M-2 0 Q0 -8 2 0Z" fill="{BLACK}"/><circle cy="-9" r="3" fill="{BLACK}" {W(1.6)}/>')
    + f'<path d="M100 40 q4 -8 10 -4 q2 6 -6 8 v4" fill="none" stroke="#5A3E8A" stroke-width="3" stroke-linecap="round"/><circle cx="104" cy="54" r="1.8" fill="#5A3E8A"/>',
    "белая и чёрная пешки-соперницы",
    "сидят друг напротив друга за маленьким столиком с доской и задумались над ходом")


add("champions-chess-yuzhnaya", "teal",
    f'<path d="M16 72 L28 24 H104 L112 72Z" fill="#A0663E" {W(3)}/>'
    + "".join(f'<rect x="{34 + (i % 6)*11}" y="{30 + (i // 6)*12}" width="11" height="12" fill="#F4E3C3" opacity=".9"/>'
              for i in range(24) if (i + i // 6) % 2 == 0)
    + f'<rect x="12" y="72" width="104" height="40" rx="4" fill="#B97A48" {W(3)}/>'
    + f'<rect x="58" y="80" width="12" height="9" rx="2" fill="{GOLD}" {W(2)}/>'
    + G(92, 76, knight_head(WHITE), sc=0.62) + eye(82, 50, 0.6)
    + G(36, 74, f'<circle cy="-8" r="8" fill="{BLACK}" {W(2.4)}/>')
    + G(50, 74, f'<path d="M-6 0 V-12 H-8 V-18 H-3 V-14 H3 V-18 H8 V-12 H6 V0Z" fill="#fff" {W(2.2)}/>')
    + sparkle(116, 26, 6),
    "деревянная шахматная шкатулка с клетчатой крышкой",
    "приоткрылась, и из неё с любопытством выглядывают конь и макушки фигур")


add("champions-chess-oktyabrya", "night",
    f'<rect x="-6" y="96" width="140" height="40" fill="#5A4A8A"/>'
    + f'<rect x="58" y="80" width="64" height="26" rx="8" fill="#F4C7D8" {W(2.6)}/>'
    + f'<path d="M58 92 H122" stroke="#fff" stroke-width="4"/>'
    + G(76, 92, pawn(WHITE, sc=0.38)) + G(98, 92, pawn(BLACK, sc=0.38))
    + f'<path d="M64 64 Q74 62 76 72 M90 64 Q98 62 100 72" fill="none" stroke="#7FD3FF" stroke-width="2"/>'
    + G(34, 112, king(WHITE, sc=0.66))
    + f'<path d="M20 50 Q36 34 52 48 L48 52 Q36 44 24 54Z" fill="#6FA8E8" {W(2.2)}/><circle cx="54" cy="48" r="3.4" fill="#fff" {W(1.6)}/>'
    + f'<path d="M44 88 L58 80 L58 94 L44 100Z M44 88 L30 80 L30 94 L44 100Z" fill="#FFE066" {W(2.2)}/>'
    + f'<circle cx="112" cy="30" r="12" fill="#FFE9A8"/><circle cx="118" cy="26" r="11" fill="#3E4AA0"/>'
    + "".join(sparkle(x, y, 3, "#fff") for x, y in [(80, 22), (96, 40), (20, 22)]),
    "белый шахматный король-рассказчик в ночном колпаке",
    "читает книжку сказок двум пешкам-малышам, уснувшим в кроватке под месяцем")


add("champions-chess-nosovikhinskoe", "orange",
    board_strip(112, 30, n=10, a="#FFF2D8", b="#C08A5C")
    + f'<path d="M64 74 H122 L118 104 H68Z" fill="#7A9E4A" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="104" r="9" fill="#5A3A2A" {W(2.4)}/><circle cx="{x}" cy="104" r="3" fill="#C9A06A"/>' for x in (78, 110))
    + "".join(G(x, 76, pawn(c, sc=0.3)) for x, c in [(76, WHITE), (88, BLACK), (100, WHITE), (112, BLACK)])
    + f'<path d="M50 84 L66 84" {W(3)}/>'
    + G(36, 106, knight(BLACK, sc=0.85))
    + f'<path d="M8 40 Q14 34 20 40" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>',
    "чёрный шахматный конь-тяжеловоз",
    "тянет по клетчатой дороге зелёную тележку, полную чёрных и белых пешек")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for pid, code in ICONS.items():
        open(os.path.join(OUT, pid + ".svg"), "w").write(code)
    reg = os.path.join(OUT, "subjects.txt")
    lines = [l for l in open(reg, encoding="utf-8") if l.split(" — ", 1)[0] not in SUBJ]
    lines += [line + "\n" for line in SUBJ.values()]
    open(reg, "w", encoding="utf-8").writelines(lines)
    print(len(ICONS), "иконок:", " ".join(ICONS))
