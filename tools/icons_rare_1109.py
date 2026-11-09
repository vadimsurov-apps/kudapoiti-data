"""Иконки робота rare, 2026-11-09 (00 UTC) — места из поиска по районам (tools/add_rare_1109.py).
Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно — свой герой, своя сцена, компоновка и палитра.
Перед рисованием просмотрены все 44 листа icons-catalog и subjects.txt; заняты и НЕ использованы: белочка, лосёнок,
яблоко Ньютона, глобус, мяч-планета, шляпа фокусника, хрустальный шар, ракетка-парус, лётный шлем, капитанская
повязка, тележка для мячей, близнецы, «дай пять», батут с лицом, пружинка, зонтик, гамак, ночной колпак, дятел,
шишка, подснежник, лейка, пьедестал «1», кепка малыша, соска, плащ-ферзь, лапша/пиала, ласка/кулан/шершень на картах.
Запуск: python3 tools/icons_rare_1109.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O
from icons_sections_1107c import G
from icons_sections_1108b import limb
from icons_sections_1108g import rect, circ, ell, path, W, SKIN

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
draw_icons.BG.update({
    "r_avia": ("#F2FAFF", "#7FB6E6"), "r_space": ("#2A2350", "#0E0B24"), "r_coach": ("#F3FFE9", "#6DBE45"),
    "r_squash": ("#FFF3E8", "#E8743B"), "r_school": ("#EAFBF7", "#2FA58E"), "r_play": ("#FBEFFF", "#B266D9"),
    "r_rail": ("#EEF2F7", "#6F86A6"), "r_magic": ("#FFEFFA", "#D2479B"), "r_lake": ("#E6FBFF", "#1F9CC2"),
    "r_ruta": ("#FFFDE8", "#B8C93A"), "r_first": ("#FFF9E0", "#F2B705"), "r_grass": ("#EEFFE9", "#3E9B4F"),
    "r_baby": ("#FFF1E9", "#F3A27B"), "r_team": ("#F7FFE0", "#A9CF2E"), "r_clay": ("#FFF0E4", "#D9692F"),
    "r_spring": ("#F1FFEF", "#79C46B"), "r_photo": ("#EFF7F7", "#4E8F8C"), "r_newton": ("#EEF6FF", "#5A7FD6"),
    "r_alp": ("#F0F4FA", "#6C83B5"), "r_jump": ("#FFF6E6", "#F09A1E"), "r_irish": ("#F0FFF2", "#2E9D5A"),
    "r_camo": ("#F4F6E8", "#7A8B4A"), "r_mud": ("#FFF2E8", "#A8643A"), "r_party": ("#FFF0F5", "#EC5F8E"),
    "r_garage": ("#F4F4F7", "#8C8FA3"), "r_hero": ("#FFF6E4", "#E2562F"),
})
YB = "#E8F23A"   # теннисный мяч


def add(pid, bg, body, hero, scene):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def tball(x, y, r=8, fc=False, k=0.45):
    b = circ(x, y, r, YB, 2.4) + path(f"M{x-r*.8} {y-r*.45} Q{x} {y+r*.3} {x+r*.8} {y-r*.45}", "none", 1.8).replace(O, "#fff", 1)
    return b + (face(x, y, r * .38, k) if fc else "")


def racket(c="#3D7BE0", strings="#ffffff", rx=22, ry=27, handle="#5B4636", face_k=None):
    """теннисная ракетка головой вверх, центр головы (0,0), ручка вниз"""
    st = "".join(f'<path d="M{x} {-ry+3} V{ry-3}" stroke="{strings}" stroke-width="1.4"/>' for x in range(-rx + 6, rx - 4, 6))
    st += "".join(f'<path d="M{-rx+3} {y} H{rx-3}" stroke="{strings}" stroke-width="1.4"/>' for y in range(-ry + 6, ry - 4, 6))
    out = (path(f"M-7 {ry-2} L-4 {ry+12} L4 {ry+12} L7 {ry-2}", "none", 3)
           + rect(-4.5, ry + 10, 9, 26, handle, 4, 2.6)
           + ell(0, 0, rx, ry, c, 4.5) + f'<g clip-path="url(#c)"><ellipse cx="0" cy="0" rx="{rx-3}" ry="{ry-3}" fill="#ffffff" opacity=".18"/></g>'
           + f'<g>{st}</g>' + ell(0, 0, rx, ry, "none", 4.5).replace(O, c, 1) + ell(0, 0, rx + 2.2, ry + 2.2, "none", 2.4)
           + ell(0, 0, rx - 2.4, ry - 2.4, "none", 1.6))
    if face_k:
        out += face(0, -2, rx * .32, face_k)
    return out


def padel(c="#20B07A", rx=21, ry=24, holes=True):
    """сплошная ракетка падела с дырочками и темляком"""
    h = ""
    if holes:
        for yy in range(-ry + 8, ry - 4, 7):
            for xx in range(-rx + 7, rx - 4, 7):
                if (xx / (rx - 3)) ** 2 + (yy / (ry - 3)) ** 2 < .75:
                    h += f'<circle cx="{xx}" cy="{yy}" r="1.6" fill="{O}" opacity=".55"/>'
    return (rect(-5, ry - 4, 10, 26, "#333", 4, 2.6) + path(f"M3 {ry+20} q10 8 2 16", "none", 2).replace(O, "#E53935", 1)
            + ell(0, 0, rx, ry, c, 3) + h)


def squash(c="#E53935", rx=15, ry=24):
    """узкая каплевидная ракетка для сквоша"""
    st = "".join(f'<path d="M{x} {-ry+4} V{ry-6}" stroke="#fff" stroke-width="1.2"/>' for x in range(-rx + 5, rx - 3, 5))
    st += "".join(f'<path d="M{-rx+3} {y} H{rx-3}" stroke="#fff" stroke-width="1.2"/>' for y in range(-ry + 6, ry - 6, 5))
    return (path(f"M-4 {ry-4} L-3 {ry+14} L3 {ry+14} L4 {ry-4}", "#555", 2.4) + rect(-4, ry + 12, 8, 22, "#222", 3, 2.4)
            + path(f"M0 {-ry} C{rx+4} {-ry} {rx} {ry*.5} 0 {ry} C{-rx} {ry*.5} {-rx-4} {-ry} 0 {-ry}Z", "none", 4).replace(O, c, 1)
            + f'<g>{st}</g>'
            + path(f"M0 {-ry} C{rx+4} {-ry} {rx} {ry*.5} 0 {ry} C{-rx} {ry*.5} {-rx-4} {-ry} 0 {-ry}Z", "none", 2.2))


def sqball(x, y, r=6):
    return circ(x, y, r, "#1E1E24", 2) + circ(x - 2, y - 1, 1.3, "#FFD400", 0) + circ(x + 2, y - 1, 1.3, "#FFD400", 0)


def kart(c="#E53935", k=1.0, driver=""):
    """карт сбоку, носом вправо, центр (0,0)"""
    return G(0, 0,
             path("M-36 4 L-30 -6 L18 -6 L34 0 L36 8 L-36 8Z", c, 2.8)
             + rect(-40, -10, 8, 14, "#333", 2, 2.2)
             + driver
             + path("M8 -6 L2 -18", "none", 3)
             + circ(-24, 12, 9, "#2B2B2B", 2.6) + circ(-24, 12, 3.5, "#BDBDBD", 1.6)
             + circ(24, 12, 9, "#2B2B2B", 2.6) + circ(24, 12, 3.5, "#BDBDBD", 1.6), 0, k)


def shuttle(rot=0, k=1.0, fc=False):
    body = (path("M-11 -22 L11 -22 L5 2 L-5 2Z", "#ffffff", 2.4)
            + path("M-6 -22 L-2 0 M0 -22 V0 M6 -22 L2 0", "none", 1.4)
            + path("M-9 -10 H9", "none", 1.4) + ell(0, 7, 7, 6.5, "#FF7043", 2.4))
    if fc:
        body += face(0, -11, 3, 0.3, mouth=False)
    return G(0, 0, body, rot, k)


# ============================== ТЕННИС ==============================
add("tennis-vpt-avia", "r_avia",
    path("M14 96 q10 -10 22 -2 q10 -12 24 0 q8 -6 14 2 Z", "#fff", 2.2) + path("M92 30 q6 -7 14 -1 q8 -6 12 2Z", "#fff", 2)
    + G(80, 52, racket("#2E6FD8", face_k=None), -24, 1.0)
    + G(42, 72,
        path("M-30 4 L22 -8 L-6 10Z", "#FFFFFF", 2.4) + path("M-6 10 L22 -8 L-10 22Z", "#E9F0FA", 2.4)
        + path("M-30 4 L-6 10 L-10 22", "none", 1.6)
        + "".join(f'<path d="M{-24+i*8} {2+i*-1.6} l3 9" stroke="#9EC2EE" stroke-width="1"/>' for i in range(5))
        + eye(-4, 6, .55) + eye(4, 4, .55) + tball(-6, -8, 7), -8, 1.35)
    + path("M8 84 q-8 6 -14 2", "none", 2).replace(O, "#ffffff", 1),
    "тетрадный бумажный самолётик в клеточку",
    "несёт на спине жёлтый мяч и пролетает мимо наклонённой синей ракетки над облаками")

add("tennis-planeta-lefortovo", "r_space",
    "".join(sparkle(x, y, r, "#FFF6C8") for x, y, r in ((20, 34, 4), (104, 28, 3), (28, 96, 3), (110, 92, 4), (60, 16, 2.5)))
    + G(58, 66,
        racket("#FF8A3D", "#FFE0C7", rx=20, ry=24)
        + circ(0, 0, 25, "#BFEFFF", 2.4).replace('fill="#BFEFFF"', 'fill="#BFEFFF" fill-opacity=".35"')
        + face(0, -1, 6, 0.6)
        + path("M-14 -16 q6 -6 12 -6", "none", 2.4).replace(O, "#ffffff", 1), 14)
    + limb("M44 84 Q30 96 22 88", "#F4F4F4", 6)
    + G(98, 46, tball(0, 0, 9), 20)
    + path("M84 52 q6 4 4 10", "none", 1.8).replace(O, "#FFF6C8", 1),
    "оранжевая теннисная ракетка-астронавт в круглом стеклянном шлеме",
    "парит в открытом космосе и тянется к дрейфующему мячу среди звёзд")

add("tennis-club-liga-velozavodskaya", "r_coach",
    path("M-6 104 H134 V140 H-6Z", "#58A845", 2.4) + path("M-6 108 H134", "none", 2).replace(O, "#fff", 1)
    + G(44, 56, racket("#D7263D", rx=21, ry=26, face_k=0.6), -6)
    + path("M34 70 Q44 82 58 72", "none", 1.8) + G(62, 74, ell(0, 0, 7, 5, "#E0A526", 2.2) + rect(-2, -8, 4, 5, "#E0A526", 1, 1.6), 10)
    + path("M72 66 l8 -4 M72 74 l9 0 M70 82 l8 4", "none", 2)
    + tball(84, 98, 11, True, 0.5) + tball(102, 101, 8.5, True, 0.4) + tball(116, 104, 6.5, True, 0.32),
    "красная ракетка-тренер с медным свистком на шнурке",
    "свистит, а три мячика-новичка выстроились перед ней по росту на газоне")

add("squash-belka-nagatinsky", "r_squash",
    rect(56, -6, 80, 150, "#FBF6EE", 0, 2.6) + path("M56 64 H136", "none", 2.6).replace(O, "#D32F2F", 1)
    + path("M56 100 H136", "none", 2).replace(O, "#D32F2F", 1)
    + G(34, 62, squash("#1565C0"), -18)
    + G(84, 48, sparkle(0, 0, 9, "#FFF3A6"))
    + G(76, 82, circ(0, 0, 13, "#1E1E24", 2.6) + circ(-5, -5, 2.6, "#FFD400", 0) + circ(5, -5, 2.6, "#FFD400", 0)
        + eye(-5, 1, .6).replace(O, "#fff").replace('fill="#fff"', 'fill="#1E1E24"') + eye(5, 1, .6).replace(O, "#fff").replace('fill="#fff"', 'fill="#1E1E24"')
        + path("M-4 7 Q0 10 4 7", "none", 2).replace(O, "#fff", 1))
    + path("M66 92 q-10 10 -24 10", "none", 2).replace(O, "#ffffff", 1),
    "чёрный сквош-мячик с двумя жёлтыми точками",
    "отскакивает от белой стены корта, оставив звёздочку удара, рядом синяя узкая сквош-ракетка")

add("tennis-dtssh-belokamennaya", "r_school",
    rect(8, 18, 72, 50, "#2F5D50", 4, 3) + rect(4, 66, 80, 6, "#A1887F", 2, 2.2)
    + path("M18 34 q12 -12 24 0 T66 34", "none", 2).replace(O, "#ffffff", 1) + circ(70, 30, 3, "#fff", 0)
    + path("M20 52 l8 6 l12 -12", "none", 2).replace(O, "#ffffff", 1)
    + G(92, 62, racket("#7E57C2", rx=19, ry=23)
        + circ(-7, -3, 6, "none", 2.2) + circ(7, -3, 6, "none", 2.2) + path("M-1 -3 H1", "none", 2)
        + eye(-7, -3, .5) + eye(7, -3, .5) + path("M-4 8 Q0 11 4 8", "none", 2.2), 8)
    + path("M74 70 L56 46", "none", 3.4).replace(O, "#8D6E63", 1)
    + tball(30, 98, 10, True, 0.45) + tball(56, 104, 9, True, 0.4),
    "ракетка-учительница в круглых очках с указкой",
    "у школьной доски объясняет двум мячикам-ученикам, куда бить")

add("tennis-play-korolyova", "r_play",
    G(60, 70, racket("#EC4C9A", "#FFD6EB", rx=26, ry=31)
      + path("M-9 -14 L15 0 L-9 14Z", "#ffffff", 2.6), -10)
    + G(98, 30, tball(0, 0, 10, True, 0.45))
    + path("M86 40 q-4 8 -12 10", "none", 2).replace(O, "#ffffff", 1)
    + path("M92 50 h8 M88 56 h6", "none", 2),
    "розовая теннисная ракетка с белым треугольником «плей» на струнах",
    "жёлтый мяч подпрыгивает над ней, как над кнопкой запуска")

add("squash-central-komsomolskaya", "r_rail",
    rect(-6, 100, 140, 40, "#B0BEC5", 0, 2.4) + path("M-6 100 H134", "none", 3).replace(O, "#FFD54F", 1)
    + rect(-6, 26, 30, 50, "#4F6C8F", 3, 2.4) + rect(0, 34, 18, 14, "#BBDEFB", 2, 2)
    + G(62, 56, squash("#2E7D32", rx=15, ry=23)
        + path("M-16 -22 Q0 -34 16 -22 L14 -18 L-14 -18Z", "#283593", 2.4) + rect(-16, -21, 32, 5, "#1A237E", 1.5, 2)
        + circ(0, -24, 2.6, "#FFD54F", 1.4) + face(0, -4, 5, 0.5), 0)
    + G(92, 88, path("M0 0 V-26", "none", 2.6) + path("M0 -26 L16 -21 L0 -16Z", "#E53935", 2.2))
    + sqball(108, 94, 7) + rect(104, 82, 9, 6, "#FFF8E1", 1, 1.6),
    "зелёная сквош-ракетка в фуражке проводника",
    "встречает на вокзальном перроне чёрный мячик-пассажира с билетиком, подняв красный флажок")

add("tennis-magiya-borisovo", "r_magic",
    G(54, 72, racket("#7B1FA2", "#F8BBD0", rx=22, ry=27, face_k=0.55), -28)
    + path("M70 56 Q90 34 104 40", "none", 7).replace(O, "#FF5252", 1)
    + path("M72 60 Q92 40 106 46", "none", 5).replace(O, "#FFD740", 1)
    + path("M74 64 Q94 46 108 52", "none", 5).replace(O, "#69F0AE", 1)
    + path("M76 68 Q96 52 110 58", "none", 5).replace(O, "#40C4FF", 1)
    + tball(110, 46, 9)
    + "".join(sparkle(x, y, r, "#FFFFFF") for x, y, r in ((88, 24, 4), (30, 26, 3.5), (100, 76, 3))),
    "фиолетовая ракетка-фея с розовыми струнами",
    "отбивает мяч, и за ним тянется радужный хвост из искорок")

add("tennis-centre-tushino", "r_lake",
    path("M-6 86 q14 -6 28 0 t28 0 t28 0 t28 0 t28 0 V140 H-6Z", "#3BB0D8", 2.4)
    + rect(-6, 62, 46, 8, "#A1887F", 1, 2.4) + path("M6 70 V96 M30 70 V96", "none", 3)
    + G(66, 58, racket("#43A047", rx=17, ry=21)
        + path("M-18 -6 Q-18 -26 0 -26 Q18 -26 18 -6Z", "#FFFFFF", 2.4)
        + "".join(circ(x, y, 2.2, "#F06292", 0) for x, y in ((-10, -14), (0, -20), (10, -14), (-4, -9), (6, -9)))
        + face(0, 2, 5, 0.5), 52)
    + tball(98, 96, 8) + path("M86 100 q12 -4 24 0", "none", 2).replace(O, "#ffffff", 1)
    + path("M44 44 q-4 -6 0 -10 M54 40 q-2 -6 2 -9", "none", 2).replace(O, "#ffffff", 1),
    "зелёная ракетка в купальной шапочке в горошек",
    "ныряет с деревянных мостков в водохранилище за упавшим мячом")

add("tennis-ruta-krasnogo-mayaka", "r_ruta",
    path("M-6 106 H134 V140 H-6Z", "#5E9E44", 2.4)
    + G(64, 74, racket("#2E7D32", "#C5E1A5", rx=20, ry=25), 0)
    + "".join(G(x, y, "".join(G(0, 0, ell(0, -5, 3.4, 5, "#FFEB3B", 1.6), a) for a in (0, 72, 144, 216, 288))
                  + circ(0, 0, 2.6, "#F9A825", 1.4)) for x, y in ((44, 30), (84, 28), (64, 18), (34, 54), (94, 52)))
    + path("M44 36 Q56 50 62 52 M84 34 Q72 48 66 52 M64 24 V48 M38 58 Q50 60 56 62 M90 58 Q78 60 72 62", "none", 2).replace(O, "#558B2F", 1)
    + face(64, 76, 6, 0.6)
    + tball(104, 98, 8),
    "кустик руты с жёлтыми цветочками, выросший из теннисной ракетки",
    "цветёт прямо на корте, а рядом в траве лежит мяч")

add("padel-pervaya-raketka-obrucheva", "r_first",
    G(60, 62, padel("#00A6A6", 21, 25)
      + G(0, -28, path("M0 0 Q-20 -14 -18 2 Q-10 8 0 0 Q10 8 18 2 Q20 -14 0 0Z", "#FFFFFF", 2.4) + circ(0, 0, 4, "#FFFFFF", 2.2))
      + face(0, -3, 7, 0.6))
    + G(98, 72, path("M0 30 L-4 0 M0 30 L4 -2 M0 30 L10 2", "none", 2).replace(O, "#2E7D32", 1)
        + ell(-4, -4, 5, 7, "#FF4081", 2) + ell(5, -6, 5, 7, "#FFFFFF", 2) + ell(11, 0, 5, 6, "#FF8A65", 2), -10)
    + limb("M78 74 Q86 80 94 96", "#00A6A6", 4)
    + tball(26, 102, 8),
    "падел-ракетка-первоклассница с большим белым бантом",
    "шагает на первый урок с букетом гладиолусов")

add("tennis-losinka-ostashkovskaya", "r_grass",
    G(64, 54, racket("#5D4037", "#D7CCC8", rx=21, ry=26), 0)
    + path("M-6 92 Q10 72 24 88 Q34 70 48 86 Q60 70 72 86 Q86 70 98 86 Q112 72 134 90 V140 H-6Z", "#43A047", 2.4)
    + G(66, 96, circ(0, 0, 13, YB, 2.4) + face(0, 0, 4.6, 0.45, mouth=False))
    + path("M50 92 Q58 78 66 86 Q74 76 82 92", "#66BB6A", 2.2)
    + G(58, 82, ell(0, 0, 4, 8, "#7CB342", 2), -30) + G(76, 82, ell(0, 0, 4, 8, "#7CB342", 2), 30),
    "жёлтый мяч в маскировочной шапке из листьев",
    "прячется в высокой траве под коричневой ракеткой, видны только глаза")

add("tennis-atennis-kubinka", "r_baby",
    G(78, 52, racket("#F57C00", "#FFE0B2", rx=24, ry=29), 18)
    + G(46, 84, ell(0, 18, 16, 12, "#FFFFFF", 2.6) + ell(0, 4, 15, 14, SKIN, 2.6)
        + circ(0, -16, 14, SKIN, 2.6) + path("M-2 -30 q4 -6 6 0", "none", 2.4) + face(0, -14, 5, 0.55)
        + rect(-16, 2, 7, 6, "#29B6F6", 2, 1.8)
        + limb("M10 0 Q22 -2 28 -16", SKIN, 6))
    + G(98, 102, tball(0, 0, 14)),
    "карапуз в подгузнике и голубом напульснике",
    "двумя руками тянет оранжевую ракетку больше себя, к нему катится огромный мяч")

add("tennis-team-nakhabino", "r_team",
    G(64, 96, racket("#1976D2", rx=16, ry=26), 90, 1.0)
    + tball(64, 70, 13, True, 0.55)
    + tball(51, 46, 11, True, 0.45).replace(YB, "#D4F73C") + tball(77, 46, 11, True, 0.45).replace(YB, "#F0F74A")
    + limb("M44 52 L36 60", "#C6DD3A", 3) + limb("M84 52 L92 60", "#C6DD3A", 3)
    + sparkle(64, 24, 6, "#ffffff"),
    "три теннисных мяча-друга",
    "стоят пирамидкой акробатов на лежащей синей ракетке")

add("tennis-family-club-isakovo", "r_clay",
    path("M-6 98 H134 V140 H-6Z", "#C8642A", 2.4) + path("M-6 106 H134", "none", 2).replace(O, "#ffffff", 1)
    + G(84, 84, path("M-20 -12 H14 Q20 -12 18 0 Q14 12 0 12 H-16 Q-22 0 -20 -12Z", "#5C6BC0", 2.4)
        + path("M14 -12 Q16 -28 0 -26 Q-6 -24 -6 -12", "#7986CB", 2.4)
        + circ(-12, 16, 5, "#333", 2) + circ(10, 16, 5, "#333", 2) + path("M-20 -12 L-30 -22", "none", 3)
        + tball(-2, -10, 7, True, 0.35))
    + G(40, 66, circ(0, 0, 17, YB, 2.6) + path("M-17 -4 Q-10 -24 10 -18 Q18 -14 17 -4 Q4 -12 -17 -4Z", "#E91E63", 2.4)
        + face(0, 4, 6, 0.6) + limb("M14 6 Q30 4 50 -6", YB, 4))
    + G(108, 34, racket("#8E6E53", rx=11, ry=13), 20),
    "мяч-мама в розовой косынке",
    "катит по оранжевому грунтовому корту синюю коляску с мячиком-малышом")

add("squash-aprel-sport-aprelevka", "r_spring",
    circ(104, 26, 12, "#FFE066", 2.4)
    + rect(20, 40, 40, 56, "#8D6E63", 3, 2.6) + path("M14 42 L40 22 L66 42Z", "#5D4037", 2.6) + circ(40, 62, 8, "#3E2723", 2.2)
    + rect(36, 96, 8, 40, "#6D4C41", 1, 2.4)
    + G(78, 80, ell(0, 0, 18, 13, "#37474F", 2.6) + circ(14, -12, 10, "#37474F", 2.6)
        + "".join(circ(x, y, 1.2, "#FFFFFF", 0) for x, y in ((-6, -2), (2, 4), (-10, 6), (8, 2), (12, -16), (18, -8)))
        + path("M23 -12 L32 -10 L23 -7Z", "#FFC107", 2) + eye(16, -14, .55)
        + path("M-16 4 L-28 10 L-18 12Z", "#263238", 2.2)
        + limb("M-4 12 L-6 22 M4 12 L6 22", "#FF8F00", 2.4))
    + G(56, 92, squash("#E53935", rx=10, ry=15), -60)
    + sqball(98, 108, 5),
    "скворец со сквош-ракеткой под крылом",
    "вернулся весной к своему скворечнику и готов к тренировке")

add("padel-r-aprelevka", "r_photo",
    G(60, 66, padel("#F4511E", 22, 26) + face(0, 4, 7, 0.6)
      + G(0, -10, rect(-14, -8, 28, 18, "#37474F", 3, 2.4) + circ(0, 1, 6, "#90CAF9", 2.2) + rect(6, -12, 6, 4, "#37474F", 1, 1.6)))
    + G(104, 34, tball(0, 0, 9).replace(YB, "#D7F25A"))
    + path("M76 52 L94 40 M78 58 L98 54 M76 46 L88 30", "none", 2).replace(O, "#FFF59D", 1)
    + sparkle(92, 50, 6, "#FFFDE7"),
    "оранжевая падел-ракетка с фотоаппаратом",
    "щёлкает вспышкой лаймовый мяч в прыжке")

# ============================== БАДМИНТОН ==============================
add("badminton-newton-arena", "r_newton",
    rect(10, 14, 108, 8, "#90A4AE", 3, 2.6) + rect(12, 22, 6, 92, "#90A4AE", 2, 2.4) + rect(110, 22, 6, 92, "#90A4AE", 2, 2.4)
    + rect(6, 110, 116, 10, "#607D8B", 3, 2.6)
    + "".join(path(f"M{x} 22 L{x} 56", "none", 1.8) + G(x, 72, shuttle(180, 1.0, fc=(x == 64)))
              for x in (50, 64, 78))
    + path("M36 22 L22 52", "none", 1.8) + G(18, 66, shuttle(205, 1.0))
    + path("M92 22 L92 56", "none", 1.8) + G(92, 72, shuttle(180, 1.0))
    + path("M14 46 q-4 10 0 18", "none", 2).replace(O, "#ffffff", 1),
    "колыбель Ньютона из пяти воланов",
    "крайний волан отлетел в сторону и сейчас ударит по ряду")

# ============================== СКАЛОДРОМ ==============================
add("climb-edelweiss-sinichkina", "r_alp",
    rect(18, -6, 92, 150, "#B0BEC5", 0, 2.6)
    + "".join(G(x, y, path("M-6 -4 Q0 -10 6 -4 Q8 4 0 6 Q-8 4 -6 -4Z", c, 2.2))
              for x, y, c in ((34, 22, "#E53935"), (90, 30, "#FFB300"), (40, 104, "#1E88E5"), (94, 110, "#8E24AA"), (30, 66, "#43A047"), (98, 74, "#FB8C00")))
    + G(64, 64,
        "".join(G(0, 0, ell(0, -14, 6, 13, "#FFFFFF", 2.4), a) for a in range(0, 360, 45))
        + circ(0, 0, 9, "#FFE082", 2.4) + "".join(circ(x, y, 1.2, "#C49000", 0) for x, y in ((-3, -3), (3, -2), (0, 3)))
        + face(0, 0, 3.4, 0.3, mouth=False))
    + limb("M52 50 Q42 34 36 26", "#81C784", 4) + limb("M76 74 Q86 82 92 106", "#81C784", 4)
    + path("M64 -6 V50", "none", 1.8).replace(O, "#FFEB3B", 1),
    "белый цветок эдельвейс с пушистыми лепестками",
    "карабкается по скалодрому, цепляясь листочками за цветные зацепы")

# ============================== БАТУТЫ ==============================
add("batut-gibbon-podolsk", "r_jump",
    ell(64, 102, 46, 12, "#26323F", 2.8) + ell(64, 100, 40, 9, "#1E88E5", 2.4)
    + path("M24 104 L20 126 M104 104 L108 126 M50 112 L48 130 M78 112 L80 130", "none", 3.4)
    + path("M64 88 q-4 -14 0 -26", "none", 1.8).replace(O, "#ffffff", 1)
    + G(62, 46, ell(0, 0, 16, 9, "#7CB342", 2.4) + circ(15, -4, 8, "#8BC34A", 2.4)
        + eye(17, -6, .6) + path("M18 0 Q21 2 23 0", "none", 1.8)
        + limb("M-8 4 L-20 -12 L-28 4", "#689F38", 3) + limb("M4 6 L-4 18", "#689F38", 3)
        + path("M20 -11 Q28 -26 36 -20 M17 -11 Q20 -28 30 -28", "none", 1.6), -18)
    + "".join(sparkle(x, y, 4, "#ffffff") for x, y in ((28, 32), (100, 26))),
    "зелёный кузнечик-прыгун",
    "подлетает высоко над синим батутом, вытянув длинные ноги")

# ============================== КАРТИНГ ==============================
add("karting-okart-odintsovo", "r_irish",
    rect(-6, 92, 140, 50, "#4E5B5F", 0, 2.4) + path("M-6 98 H134", "none", 2).replace(O, "#FFFFFF", 1)
    + G(62, 76, kart("#2E7D32",
                     driver=G(-6, -16, circ(0, 0, 11, "#43A047", 2.4) + face(0, 1, 4, 0.45)
                              + ell(0, -10, 16, 3, "#1B5E20", 2.2) + rect(-9, -24, 18, 14, "#1B5E20", 3, 2.2)
                              + rect(-9, -14, 18, 3, "#FFC107", 0, 1.4)
                              + G(9, -19, "".join(G(0, 0, circ(0, -3, 2.6, "#7CFC00", 1.2), a) for a in (0, 120, 240)), 0, 1))))
    + path("M18 66 h-12 M14 74 h-10 M20 82 h-12", "none", 2.2)
    + "".join(rect(100 + (i % 2) * 6, 24 + (i // 2) * 6, 6, 6, "#222" if (i + i // 2) % 2 == 0 else "#fff", 0, 0) for i in range(8))
    + path("M100 24 V60", "none", 2.4),
    "зелёный карт в ирландском котелке с трилистником",
    "мчится к клетчатому флагу по серой трассе")

add("karting-patriot-kubinka", "r_camo",
    "".join(G(x, 74, path("M0 -30 L-12 -4 L-6 -4 L-14 12 L14 12 L6 -4 L12 -4Z", "#33691E", 2.2)) for x in (12, 116))
    + path("M-6 100 Q30 84 64 96 T134 92 V140 H-6Z", "#8D6E63", 2.4)
    + G(62, 80, kart("#6B7B3A",
                     driver=G(-6, -16, circ(0, 0, 11, "#556B2F", 2.4) + face(0, 1, 4, 0.45)
                              + path("M-12 -6 Q0 -18 12 -6 L10 -3 L-10 -3Z", "#556B2F", 2.2)
                              + circ(0, -10, 2, "#E53935", 1)), )
      + "".join(ell(x, y, 5, 3, c, 0) for x, y, c in ((-20, 0, "#3E4A1E"), (0, 2, "#A1A86A"), (18, -2, "#3E4A1E"))), -8)
    + path("M28 100 q-6 -6 -14 -2 M100 98 q6 -8 14 -4", "none", 2),
    "карт в камуфляжной раскраске и пилотке",
    "подпрыгивает на лесной грунтовой трассе между ёлками")

add("karting-krasnye-mashiny-balashikha", "r_mud",
    path("M-6 106 Q40 92 64 104 T134 100 V140 H-6Z", "#6D4C41", 2.4)
    + G(64, 58,
        path("M-34 2 L-26 -14 L22 -14 L36 0 L34 10 L-34 10Z", "#D32F2F", 2.8)
        + path("M-20 -14 L-14 -32 L12 -32 L20 -14", "none", 3.2)
        + circ(-26, 16, 14, "#2B2B2B", 2.6) + circ(-26, 16, 5, "#E0E0E0", 1.8)
        + circ(26, 16, 14, "#2B2B2B", 2.6) + circ(26, 16, 5, "#E0E0E0", 1.8)
        + eye(-6, -4, .6) + eye(8, -4, .6) + path("M-2 2 Q1 6 4 2", "none", 2), -12)
    + "".join(circ(x, y, r, "#8D6E63", 1.6) for x, y, r in ((24, 96, 4), (14, 86, 3), (34, 88, 2.5), (104, 92, 3.5), (114, 82, 2.5)))
    + path("M18 64 h-10 M22 72 h-12", "none", 2.2),
    "красный багги с огромными колёсами",
    "перелетает через кочку, разбрызгивая грязь")

add("karting-crazydrift-lapshinka", "r_party",
    path("M-6 100 H134 V140 H-6Z", "#5E5A80", 2.4)
    + path("M14 96 q-10 -8 -4 -18 q-10 -4 -4 -14", "none", 3).replace(O, "#ECEFF1", 1)
    + G(66, 78,
        path("M-34 6 L34 6 L34 14 L-34 14Z", "#FF80AB", 2.6)
        + rect(-30, -24, 60, 30, "#FFF3E0", 6, 2.8) + path("M-30 -16 Q-22 -10 -14 -16 T2 -16 T18 -16 T30 -16", "none", 2.6).replace(O, "#F48FB1", 1)
        + "".join(rect(x - 2, -38, 4, 13, c, 1.5, 1.6) + path(f"M{x} -38 q-3 -5 0 -9 q3 4 0 9Z", "#FFB300", 1.2)
                  for x, c in ((-16, "#42A5F5"), (0, "#66BB6A"), (16, "#AB47BC")))
        + face(0, -6, 7, 0.6)
        + circ(-24, 18, 8, "#2B2B2B", 2.4) + circ(24, 18, 8, "#2B2B2B", 2.4), -14)
    + "".join(rect(x, y, 4, 7, c, 1, 0) for x, y, c in ((104, 28, "#FFEB3B"), (92, 18, "#4FC3F7"), (114, 46, "#F06292"), (24, 30, "#AED581"))),
    "розовый карт-торт с горящими свечками",
    "заносит в вираж на дне рождения, а огоньки свечек не гаснут")

add("karting-red-racing-fili", "r_garage",
    rect(-6, -6, 140, 30, "#616161", 0, 2.4) + rect(-6, 100, 140, 40, "#9E9E9E", 0, 2.4)
    + path("M-6 112 H134", "none", 2.4).replace(O, "#FFEB3B", 1).replace('stroke-width="2.4"', 'stroke-width="2.4" stroke-dasharray="10 8"')
    + G(108, 46, rect(-12, -12, 24, 24, "#1565C0", 4, 2.4) + '<text x="0" y="8" font-family="Arial" font-weight="bold" font-size="20" fill="#fff" text-anchor="middle">P</text>')
    + path("M108 58 V100", "none", 3)
    + G(54, 84, kart("#212121",
                     driver=G(-6, -18, circ(0, 0, 14, "#E53935", 2.6) + path("M-2 -4 H14 Q14 6 6 8 H-2Z", "#263238", 2.2)
                              + eye(6, 1, .55).replace(O, "#ffffff") + path("M-12 4 Q-4 10 4 10", "none", 1.8))))
    + path("M16 76 h-12 M18 86 h-14", "none", 2.2),
    "красный гоночный шлем с тёмным визором",
    "выезжает за рулём чёрного карта с этажа парковки под синим знаком «P»")

add("karting-super-cart-olimp", "r_hero",
    path("M-6 104 H134 V140 H-6Z", "#455A64", 2.4)
    + path("M56 72 Q30 56 2 66 Q14 74 6 84 Q30 78 52 84Z", "#E53935", 2.4)
    + G(66, 84, kart("#1E63D6",
                     driver=G(-8, -16, circ(0, 0, 11, "#FFD54F", 2.4)
                              + path("M-11 -3 Q0 -9 11 -3 L11 3 Q0 -1 -11 3Z", "#E53935", 2)
                              + eye(-4, 0, .45).replace(O, "#fff").replace('fill="#fff"', f'fill="{O}"') + eye(4, 0, .45)
                              + path("M-3 6 Q0 9 3 6", "none", 1.8))) +
      G(8, 0, path("M-8 -6 L0 -14 L8 -6 L0 2Z", "#FFD600", 2)))
    + sparkle(104, 30, 6, "#FFF59D") + sparkle(84, 20, 4, "#FFF59D"),
    "маленький синий карт в красной маске и развевающемся плаще супергероя",
    "мчится вперёд, плащ полощется на ветру")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for pid, body in ICONS.items():
        open(os.path.join(OUT, f"{pid}.svg"), "w").write(body)
    reg = os.path.join(OUT, "subjects.txt")
    have = {l.split(" — ")[0] for l in open(reg, encoding="utf-8")}
    with open(reg, "a", encoding="utf-8") as f:
        for pid, line in SUBJ.items():
            if pid not in have:
                f.write(line + "\n")
    print(len(ICONS), "icons")
