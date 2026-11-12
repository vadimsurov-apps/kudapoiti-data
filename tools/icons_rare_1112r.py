"""Иконки робота rare, 2026-11-12 (12:47 UTC) — места из tools/add_rare_1112r.py.
Правило АБСОЛЮТНОЙ уникальности: реестр subjects.txt проверен grep'ом по задуманным героям (шлем/птенец, иглу, самолёт,
шорты, клевер, подкова, маяк, лампа гола, щитки, краги, пингвин, опора, робот, табурет, звёздочка на льду, ёлочка, буллит,
две клюшки). Заняты и НЕ взяты: маяк (каратэ, ладья), лампа гола, клевер, подкова, щитки вратаря, краги, робот-пушка НТ,
пингвинёнок, диско-шар, шайба/клюшка/ворота с мордашкой, девочка-фигуристка в платье. Каждая иконка придумана отдельно:
свой герой, своя сцена, своя палитра фона.
Иконки hockey-star-yunykh-lenintsev и rink-samolet-arena-kommunarka нарисованы, но не записаны (места без точки OSM).
Запуск: python3 tools/icons_rare_1112r.py [id…] → icons-src/<id>.svg + строки реестра в subjects.txt"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O
from icons_sections_1107c import G

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
SKIN = "#FFD7B5"


def rect(x, y, w, h, c, rx=4, sw=2.8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{c}" {W(sw)}/>'


def circ(x, y, r, c, sw=2.8):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" {W(sw)}/>'


def ell(x, y, rx, ry, c, sw=2.8):
    return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{c}" {W(sw)}/>'


def path(d, c="none", sw=2.8):
    return f'<path d="{d}" fill="{c}" {W(sw)}/>'


def mouth(x, y, w=3, sw=2.0):
    return f'<path d="M{x-w} {y} Q{x} {y+w*0.9} {x+w} {y}" fill="none" {W(sw)}/>'


def blush(x, y, rx=2.6, ry=1.6):
    return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#FF7FA8" opacity=".7"/>'


def puck(x, y, k=1.0):
    return G(x, y, ell(0, 2, 8, 3.4, "#2B2B33", 2.2) + ell(0, -1, 8, 3.4, "#3A3A44", 2.2), 0, k)


def stick(x, y, rot, c="#C98A3C", tape="#FFFFFF", k=1.0):
    """клюшка: (x,y) — верх рукоятки, рукоять вниз, крюк вправо"""
    b = (path("M-2.5 0 H2.5 V44 Q2.5 48 7 48 H20 Q24 48 24 52 V54 H2 Q-2.5 54 -2.5 49Z", c, 2.4)
         + f'<path d="M12 48.5 V53.5 M16 48.5 V53.5" stroke="{tape}" stroke-width="2"/>'
         + rect(-3, -1, 6, 8, "#2B2B33", 2, 1.8))
    return G(x, y, b, rot, k)


def add(pid, pal, body, hero, scene):
    k = f"r12r_{pid}"
    draw_icons.BG[k] = pal
    ICONS[pid] = svg(k, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def ice(y, c="#F2FBFF", line="#9FCFE6"):
    return (f'<rect x="-4" y="{y}" width="136" height="{132-y}" fill="{c}"/>'
            f'<path d="M-4 {y} H132" stroke="{line}" stroke-width="2.4"/>')


# 1) Hockey Star, Юных Ленинцев — шлем-гнездо: в перевёрнутом шлеме поселился птенец и болеет за шайбу.
helmet = (path("M26 92 Q26 52 64 50 Q102 52 102 92Z", "#2F6FD6", 3.0)
          + path("M34 92 Q36 66 64 64 Q92 66 94 92Z", "#E8D3A6", 2.4)
          + path("M40 92 Q44 76 54 74 M74 74 Q86 76 88 92", "none", 1.6)
          + rect(98, 74, 10, 18, "#C9D4E2", 3, 2.2) + path("M98 80 H108 M98 86 H108", "none", 1.6))
chick = (ell(64, 74, 16, 14, "#FFD23F", 3.0) + path("M58 60 Q60 54 64 58 Q66 52 70 58", "#FFD23F", 2.2)
         + eye(58, 72, 0.7) + eye(70, 72, 0.7) + path("M61 78 L64 84 L67 78Z", "#FF8A2A", 2.0)
         + blush(53, 79) + blush(75, 79) + path("M48 76 Q40 70 42 62", "#FFD23F", 2.6))
add("hockey-star-yunykh-lenintsev", ("#DFFBEA", "#4FC48A"),
    ice(92, "#F0FFF8", "#8ED9B5") + helmet + chick + puck(108, 108, 1.0)
    + '<path d="M28 110 Q60 102 96 108" stroke="#8ED9B5" stroke-width="2" fill="none" stroke-dasharray="4 4"/>'
    + sparkle(22, 34, 4) + sparkle(106, 30, 3),
    "жёлтый птенец, поселившийся в перевёрнутом синем хоккейном шлеме, как в гнезде",
    "высунулся из шлема на льду и, раскрыв клюв, провожает глазами проскользнувшую мимо шайбу")

# 2) Hockey Star, Красного Маяка — малыш упал на лёд «звёздочкой» и хохочет, над ним кружат звёздочки.
kid2 = (path("M64 76 L36 64 M64 76 L92 62", "none", 7.5) + path("M64 76 L36 64 M64 76 L92 62", "none", 0)
        + '<path d="M64 76 L36 64 M64 76 L92 62" stroke="#E2463F" stroke-width="5" stroke-linecap="round"/>'
        + path("M60 90 L40 110 M68 90 L90 110", "none", 7.5)
        + '<path d="M60 90 L40 110 M68 90 L90 110" stroke="#2B3A67" stroke-width="5" stroke-linecap="round"/>'
        + path("M34 106 L44 116 M86 116 L96 106", "none", 3.2)
        + ell(64, 82, 13, 14, "#E2463F", 3.0) + path("M52 82 H76", "none", 2.0)
        + circ(64, 58, 12, SKIN, 2.8) + path("M51 56 Q52 42 64 42 Q76 42 77 56Z", "#E2463F", 2.8)
        + path("M56 60 Q58 56 60 60 M68 60 Q70 56 72 60", "none", 2.0) + path("M58 64 Q64 70 70 64Z", "#FFFFFF", 2.0)
        + blush(54, 64) + blush(74, 64))
add("hockey-star-krasnogo-mayaka", ("#FFE6DE", "#F07A5C"),
    ice(70, "#F5FCFF", "#A9D3E8") + stick(14, 50, -60, "#3C8DDA") + puck(108, 92, 0.9) + kid2
    + sparkle(46, 30, 4.4, "#FFE14D") + sparkle(64, 22, 3.6, "#FFE14D") + sparkle(82, 30, 4.4, "#FFE14D"),
    "малыш-хоккеист в красном шлеме и красном свитере",
    "шлёпнулся на спину и лежит на льду «звёздочкой», хохоча с зажмуренными глазами, клюшка и шайба отлетели в стороны")

# 3) Hockey Star в ледовой арене «Аляска» — иглу, у которого вместо входа хоккейные ворота.
igloo = (path("M18 100 Q18 40 64 38 Q110 40 110 100Z", "#F4FAFF", 3.0)
         + path("M22 82 H106 M28 64 H100 M42 48 H86 M46 82 V100 M84 82 V100 M40 64 V82 M64 64 V82 M88 64 V82 M56 48 V64 M74 48 V64", "none", 1.6)
         + face(64, 56, 9, 0.8)
         + path("M44 100 V80 Q44 74 50 74 H78 Q84 74 84 100", "#2A2F45", 3.0)
         + path("M44 100 V80 Q44 74 50 74 H78 Q84 74 84 100", "none", 0)
         + '<path d="M44 100 V80 Q44 74 50 74 H78 Q84 74 84 100" stroke="#E23B3B" stroke-width="5" fill="none"/>'
         + '<path d="M50 80 L78 96 M50 92 L72 78 M58 76 L78 88 M50 86 L64 76" stroke="#FFFFFF" stroke-width="1.2" opacity=".8"/>')
add("hockey-star-nizhnelikhoborsky", ("#E3E6FF", "#6A78D8"),
    ice(100, "#EAF6FF", "#8FB6E0") + igloo + puck(64, 92, 0.9)
    + '<path d="M118 116 Q96 110 74 96" stroke="#8FB6E0" stroke-width="2" fill="none" stroke-dasharray="4 4"/>'
    + sparkle(20, 26, 4) + sparkle(110, 24, 3.4) + sparkle(100, 52, 2.4),
    "белое иглу из ледяных блоков с мордашкой, у которого вход — красные хоккейные ворота с сеткой",
    "шайба влетела в ворота-вход, и иглу довольно улыбается среди ночного голубого льда")

# 4) Hockey Star на катке «Авиапарка» — самолётик на хоккейных коньках садится на лёд.
plane = (path("M24 66 Q24 54 40 54 H92 Q108 56 112 64 Q108 72 92 74 H40 Q24 74 24 66Z", "#FFC93C", 3.0)
         + path("M56 56 L44 30 H56 L74 56Z", "#FF8A2A", 2.6) + path("M56 74 L46 90 H56 L70 74Z", "#FF8A2A", 2.6)
         + path("M26 60 L16 44 H26 L36 56Z", "#FF8A2A", 2.4)
         + circ(98, 64, 5, "#9FE0FF", 2.2) + circ(86, 63, 4, "#9FE0FF", 2.0)
         + eye(103, 66, 0.55) + mouth(104, 70, 2.2, 1.6) + blush(98, 72))
blades = (path("M40 74 V82 M84 74 V82", "none", 2.6)
          + path("M32 84 H50 Q54 84 54 80", "none", 2.6) + path("M76 84 H94 Q98 84 98 80", "none", 2.6)
          + '<path d="M32 84 H50 Q54 84 54 80 M76 84 H94 Q98 84 98 80" stroke="#B8C4D6" stroke-width="1.2" fill="none"/>'
          + rect(34, 74, 14, 8, "#2B2B33", 3, 2.2) + rect(78, 74, 14, 8, "#2B2B33", 3, 2.2))
spray = "".join(circ(x, y, r, "#FFFFFF", 1.6) for x, y, r in ((24, 84, 3), (18, 78, 2.4), (14, 88, 2)))
add("hockey-star-aviapark", ("#FFF3D6", "#F2A93B"),
    ice(86, "#EEF8FF", "#9BC9E6") + plane + blades + spray + puck(110, 100, 0.85) + sparkle(110, 30, 4) + sparkle(84, 22, 3),
    "жёлтый самолётик с оранжевыми крыльями, у которого вместо шасси — чёрные хоккейные коньки",
    "заходит на посадку прямо на лёд катка и тормозит лезвиями, поднимая брызги ледяной крошки")

# 5) Hockey Star на Даниловской набережной — котёнок в огромных хоккейных трусах подтягивает их, клюшка под мышкой.
cat = (path("M50 40 L46 24 L58 34Z M78 34 L84 22 L86 40Z", "#F2A65A", 2.6)
       + circ(66, 46, 18, "#F2A65A", 3.0) + path("M54 40 Q58 38 60 42 M72 40 Q76 38 80 42", "none", 1.8)
       + eye(59, 47, 0.75) + eye(73, 47, 0.75) + path("M64 53 L66 55 L68 53", "none", 2.0) + mouth(66, 57, 2.6, 1.8)
       + blush(54, 54) + blush(78, 54)
       + path("M44 52 H36 M44 56 H37 M88 52 H96 M88 56 H95", "none", 1.4)
       + path("M100 96 Q116 92 112 76", "none", 4.0) + '<path d="M100 96 Q116 92 112 76" stroke="#F2A65A" stroke-width="2.2" fill="none"/>')
shorts = (path("M38 70 H94 L100 106 H72 L66 90 L60 106 H32Z", "#2A55B8", 3.0)
          + path("M38 74 H94", "none", 2.0) + '<path d="M34 98 H62 M70 98 H98" stroke="#FFFFFF" stroke-width="3"/>'
          + path("M46 70 L50 58 M86 70 L82 58", "none", 3.0)
          + '<path d="M46 70 L50 58 M86 70 L82 58" stroke="#E23B3B" stroke-width="1.8"/>')
paws5 = circ(48, 72, 5, "#F2A65A", 2.4) + circ(84, 72, 5, "#F2A65A", 2.4)
legs5 = rect(38, 106, 10, 10, "#F2A65A", 4, 2.4) + rect(84, 106, 10, 10, "#F2A65A", 4, 2.4)
add("hockey-star-danilovskaya", ("#E6F4FF", "#5FA8E8"),
    ice(116, "#F4FBFF", "#9CC8E4") + stick(110, 26, 25, "#2F2F38") + cat + legs5 + shorts + paws5
    + sparkle(20, 30, 4) + sparkle(24, 70, 2.6),
    "рыжий котёнок в огромных синих хоккейных трусах на красных подтяжках",
    "двумя лапками подтягивает сползающие трусы, а за спиной у него торчит чёрная клюшка")

# 6) Hockey Star в Ясеневе — большая клюшка-мама учит маленькую клюшку вести шайбу.
def bigstick(x, y, rot, c, k, fc):
    """клюшка: рукоять вверх, крупный крюк вправо, мордашка на крюке"""
    b = (path("M-5 0 H5 V58 Q5 64 12 64 H44 Q52 64 52 72 V80 H6 Q-5 80 -5 70Z", c, 3.0)
         + '<path d="M38 64.5 V79.5 M44 65 V79.5" stroke="#FFFFFF" stroke-width="2.6"/>'
         + rect(-5.5, -2, 11, 14, "#2B2B33", 3, 2.0) + G(24, 72, fc, -rot, 1.0))
    return G(x, y, b, rot, k)


big = bigstick(20, 22, -4, "#7A4FD0", 0.92, eye(-6, -1, 0.7) + eye(5, -1, 0.7) + mouth(0, 3, 2.6, 1.8))
small = bigstick(80, 60, 2, "#FF9F2E", 0.55, eye(-6, -1, 0.9) + eye(6, -1, 0.9) + mouth(0, 4, 3, 2.2))
add("hockey-star-novoyasenevsky26", ("#F1E4FF", "#A27BE6"),
    ice(104, "#F7F3FF", "#B9A6E8") + small + big + puck(108, 104, 0.95)
    + sparkle(102, 30, 4) + sparkle(110, 62, 3),
    "большая фиолетовая хоккейная клюшка с глазками и маленькая оранжевая клюшка-малыш",
    "большая клюшка крюком бережно подталкивает маленькую, которая впервые сама ведёт шайбу по льду")

# 7) Hockey chance — «шанс» забить: мальчик выходит один на один на буллит и подкидывает шайбу на крюке клюшки.
goal7 = (path("M84 58 V96 M84 58 H118 V96", "none", 0) + rect(84, 58, 36, 38, "none", 4, 0)
         + '<path d="M84 96 V58 H120" stroke="#E23B3B" stroke-width="4.4" fill="none"/>'
         + '<path d="M88 62 L118 92 M88 76 L108 96 M98 62 L118 82 M88 88 L96 96 M108 62 L118 72" stroke="#FFFFFF" stroke-width="1.2" opacity=".85"/>')
boy7 = (path("M40 96 L34 114 M48 96 L58 112", "none", 6.5)
        + '<path d="M40 96 L34 114 M48 96 L58 112" stroke="#1E7F4E" stroke-width="4" stroke-linecap="round"/>'
        + path("M28 116 H40 M54 114 H66", "none", 3.0)
        + rect(30, 66, 28, 32, "#2FB36B", 9, 3.0) + '<text x="44" y="90" font-family="Arial" font-weight="700" font-size="14" text-anchor="middle" fill="#FFFFFF">1</text>'
        + circ(44, 52, 12, SKIN, 2.8) + path("M31 52 Q32 38 44 38 Q56 38 57 52Z", "#2FB36B", 2.8)
        + eye(47, 53, 0.6) + eye(53, 53, 0.6) + mouth(51, 59, 2.4, 1.8) + blush(55, 58)
        + path("M56 74 L66 68", "none", 3.4))
stick7 = stick(66, 64, -55, "#E8B04A")
add("hockey-chance-danilovskaya", ("#E2FAD9", "#56B84A"),
    ice(108, "#F2FFF0", "#9AD48F") + goal7 + boy7 + stick7 + puck(98, 40, 0.85)
    + path("M84 34 Q92 26 98 34", "none", 1.8) + sparkle(110, 22, 4) + sparkle(16, 34, 3.4),
    "мальчик-хоккеист в зелёном свитере с номером 1",
    "выходит один на один на буллит и подбрасывает шайбу крюком клюшки высоко над льдом перед пустыми воротами")

# 8) Школа «Лёд» (с 3,5 лет) — малышка в пушистых наушниках впервые едет «ёлочкой», высунув язык от старания.
girl8 = (path("M58 92 L48 108 M70 92 L80 108", "none", 7)
         + '<path d="M58 92 L48 108 M70 92 L80 108" stroke="#F06BA8" stroke-width="4.4" stroke-linecap="round"/>'
         + path("M38 110 L52 106 M76 106 L90 110", "none", 3.4)
         + path("M36 114 L54 109 M74 109 L92 114", "none", 2.4)
         + '<path d="M36 114 L54 109 M74 109 L92 114" stroke="#B8C4D6" stroke-width="1.2" fill="none"/>'
         + rect(48, 62, 32, 34, "#F06BA8", 12, 3.0) + path("M64 64 V94", "none", 1.6)
         + path("M50 70 L30 64 M78 70 L98 62", "none", 6.5)
         + '<path d="M50 70 L30 64 M78 70 L98 62" stroke="#F06BA8" stroke-width="4" stroke-linecap="round"/>'
         + circ(28, 63, 4, "#FFFFFF", 2.2) + circ(100, 61, 4, "#FFFFFF", 2.2)
         + circ(64, 46, 14, SKIN, 2.8) + path("M50 44 Q50 30 64 30 Q78 30 78 44", "none", 3.0)
         + circ(50, 46, 6.5, "#FFFFFF", 2.4) + circ(78, 46, 6.5, "#FFFFFF", 2.4)
         + eye(59, 46, 0.6) + eye(69, 46, 0.6) + path("M60 53 Q64 56 68 53", "none", 2.0)
         + path("M66 54 Q68 60 71 56Z", "#FF7FA8", 1.6) + blush(57, 52) + blush(72, 52))
add("fk-led-tenisty", ("#FFE9F3", "#EE8DBA"),
    ice(104, "#F8FCFF", "#B6D6EA")
    + '<path d="M44 124 L52 108 M86 124 L78 108" stroke="#B6D6EA" stroke-width="2" stroke-dasharray="3 3"/>'
    + girl8 + sparkle(22, 28, 4) + sparkle(104, 26, 3.4) + sparkle(108, 88, 2.6),
    "малышка лет четырёх в розовом комбинезоне и пушистых белых наушниках",
    "впервые едет по льду «ёлочкой», раскинув руки в стороны и высунув кончик языка от старания")

# 9) «Самолёт Арена» — массовое катание с прокатной опорой: пластиковый пингвин-опора везёт малыша.
peng = (ell(48, 80, 20, 26, "#2B3550", 3.0) + ell(48, 86, 13, 18, "#FFFFFF", 2.4)
        + circ(48, 52, 15, "#2B3550", 3.0) + ell(48, 55, 10, 9, "#FFFFFF", 2.0)
        + eye(44, 53, 0.55) + eye(53, 53, 0.55) + path("M46 58 L49 62 L52 58Z", "#FFA21F", 1.8)
        + path("M26 74 Q18 84 26 92 M70 74 Q78 84 70 92", "none", 3.0)
        + '<path d="M30 70 Q48 62 66 70" stroke="#FFA21F" stroke-width="5" fill="none" stroke-linecap="round"/>'
        + path("M34 104 H62 Q66 104 66 100", "none", 2.8) + rect(34, 100, 28, 6, "#FFA21F", 3, 2.2))
kid9 = (path("M86 96 L82 112 M94 96 L100 112", "none", 6.5)
        + '<path d="M86 96 L82 112 M94 96 L100 112" stroke="#2E8BD8" stroke-width="4" stroke-linecap="round"/>'
        + path("M76 114 H88 M96 114 H108", "none", 3.0)
        + rect(78, 70, 26, 28, "#FFC93C", 9, 3.0)
        + path("M80 78 L66 70", "none", 3.4) + circ(66, 70, 3.2, "#FFC93C", 2.0)
        + circ(92, 56, 11, SKIN, 2.8) + path("M80 54 Q80 42 92 42 Q104 42 104 54Z", "#2E8BD8", 2.6)
        + circ(92, 39, 4, "#FFFFFF", 2.0) + eye(88, 57, 0.55) + eye(95, 57, 0.55) + mouth(91, 62, 2.4, 1.6) + blush(85, 61))
sky_plane = G(98, 22, path("M-14 0 L12 -4 L14 0 L12 4Z", "#FFFFFF", 2.0) + path("M-2 -2 L-8 -10 H-4 L4 -2 M-2 2 L-8 10 H-4 L4 2", "#FFFFFF", 1.8), -8, 0.9)
add("rink-samolet-arena-kommunarka", ("#DCEBFF", "#4F7FDB"),
    ice(108, "#F2F8FF", "#9DBBE6") + peng + kid9 + sky_plane + sparkle(20, 26, 4) + sparkle(116, 74, 3),
    "чёрно-белая пластиковая опора-пингвин для катания с оранжевой ручкой-дугой на спине",
    "на массовом катании везёт по льду малыша в жёлтой куртке, который держится за ручку, а под куполом пролетает белый самолётик")

# 10) Tenix — малышке не хватает роста: она встала на табурет-ступеньку у теннисного стола и отбивает шарик.
tbl = (path("M4 70 H70 L76 78 H10Z", "#2A6FD8", 2.8) + '<path d="M40 70 L43 78" stroke="#FFFFFF" stroke-width="1.6"/>'
       + rect(66, 62, 4, 16, "#FFFFFF", 1, 1.8) + path("M14 78 V112 M66 78 V112", "none", 3.0))
stool = (rect(78, 100, 34, 10, "#E8A13A", 3, 2.8) + path("M82 110 L80 122 M108 110 L110 122", "none", 3.0))
girl10 = (path("M90 86 V100 M100 86 V100", "none", 3.2)
          + rect(84, 58, 22, 30, "#19B7A6", 8, 3.0) + path("M86 66 L74 60", "none", 3.2)
          + G(70, 54, ell(0, 0, 7.5, 8.5, "#E33B3B", 2.6) + path("M3 6 L8 13", "none", 4.0), 40, 1.0)
          + circ(95, 46, 11, SKIN, 2.8)
          + path("M84 44 Q84 33 95 33 Q106 33 106 44 Q100 39 95 40 Q89 39 84 44Z", "#6B3E26", 2.0)
          + circ(82, 36, 4.2, "#6B3E26", 2.0) + circ(108, 36, 4.2, "#6B3E26", 2.0)
          + eye(90, 47, 0.5) + eye(97, 47, 0.5) + mouth(93, 53, 2.4, 1.6) + blush(87, 52, 2, 1.2))
ball10 = circ(46, 52, 4.4, "#FF9A2E", 2.2) + '<path d="M64 52 Q56 44 50 50" stroke="#FFFFFF" stroke-width="2" fill="none" stroke-dasharray="3 3"/>'
add("tt-tenix-novocheremushkinskaya", ("#FFF6D9", "#F0C24A"),
    tbl + stool + girl10 + ball10 + sparkle(22, 30, 4) + sparkle(36, 18, 2.6),
    "маленькая девочка с двумя каштановыми пучками в бирюзовой футболке и с красной ракеткой",
    "не доросла до стола — встала на оранжевую табуретку-ступеньку у синего теннисного стола и отбивает оранжевый шарик")

if __name__ == "__main__":
    only = sys.argv[1:]
    for pid, body in ICONS.items():
        if only and pid not in only:
            continue
        open(os.path.join(OUT, pid + ".svg"), "w").write(body)
    subj = os.path.join(OUT, "subjects.txt")
    have = {l.split(" — ")[0] for l in open(subj, encoding="utf-8")}
    with open(subj, "a", encoding="utf-8") as f:
        for pid, line in SUBJ.items():
            if pid not in have and (not only or pid in only):
                f.write(line + "\n")
    print(len(ICONS))
