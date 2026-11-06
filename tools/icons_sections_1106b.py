"""Иконки робота sections (2026-11-06, день): 97 новых сюжетов — бассейн для малышей, музыка и танец, лёд, мячи и
инвентарь, единоборства, настольные логические игры. Сюжеты сверены с icons-catalog/sheet-01..18.png и
icons-src/subjects.txt (ни один не повторяется)."""
import os, sys
from draw_icons import svg, s, eye, face, sparkle, O
W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=9, k=0.75, **kw: face(cx, cy, d=d, k=k, **kw)
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
R, OR, Y, G, B, P, V, BR, WH, GR, DK = ("#E8654F", "#FF9A3D", "#FFD25E", "#7CD26E", "#5CB7F2", "#FF8FB8", "#A98BF0",
                                        "#C0732E", "#FFFFFF", "#B8BCCB", "#2B2A44")
GOLD, WOOD, SKIN, LB, TQ = "#F2C14E", "#E8B06E", "#FFD9B8", "#BFE9FF", "#5CCDBA"
WAVE = f'<path d="M0 100 Q16 92 32 100 T64 100 T96 100 T128 100 V128 H0Z" fill="#7FD3F7" {W(2.6)}/>'
FLOOR = f'<path d="M0 104 Q64 96 128 104 V128 H0Z" fill="#E8C9A0" {W(2.6)}/>'
GRASS = f'<path d="M0 100 Q64 90 128 100 V128 H0Z" fill="#8FDB7A" {W(2.6)}/>'
ICEF = f'<path d="M0 98 Q64 88 128 98 V128 H0Z" fill="#E9F7FF" {W(2.6)}/>'
sp = lambda *pts: "".join(sparkle(x, y, r) for x, y, r in pts)
rect = lambda x, y, w, h, c, rx=4, sw=None: f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{c}" {W(sw) if sw else s()}/>'
circ = lambda x, y, r, c, sw=None: f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" {W(sw) if sw else s()}/>'
ell = lambda x, y, rx, ry, c, sw=None: f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{c}" {W(sw) if sw else s()}/>'
path = lambda d, c="none", sw=None: f'<path d="{d}" fill="{c}" {W(sw) if sw else s()}/>'
line = lambda d, c, w: f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
txt = lambda x, y, t, size=12, c=O: f'<text x="{x}" y="{y}" font-family="Arial" font-weight="bold" font-size="{size}" text-anchor="middle" fill="{c}">{t}</text>'


def thick(d, c, w):
    return line(d, O, w + 3.2) + line(d, c, w)


I = {}
# ===================== Бассейны для малышей =====================
I["aquababy-yakhromskaya"] = ("sky", "надувной круг на шею для грудничков",
    WAVE + path("M64 30 A30 30 0 1 1 40 44 L50 52 A18 18 0 1 0 64 46Z", Y) +
    "".join(rect(x, 34, 6, 12, B, 2, 2) for x in (54, 66)) + circ(64, 64, 13, SKIN) + f(64, 66, d=5, k=0.38) +
    path("M54 56 Q64 46 74 56", "#FFE7A8", 2.2) + sp((22, 26, 6), (106, 30, 5)))
I["aquababy-chelobitevo"] = ("teal", "подгузник для плавания",
    path("M22 36 H106 L98 60 Q88 92 64 98 Q40 92 30 60Z", "#E9F7FF") + path("M22 36 H106 V46 H22Z", B, 2.4) +
    "".join(circ(x, y, 4, P, 1.6) for x, y in [(44, 62), (64, 74), (84, 62), (56, 86), (74, 86)]) +
    rect(16, 34, 14, 14, Y, 3, 2) + rect(98, 34, 14, 14, Y, 3, 2) + f(64, 56, d=7, k=0.45) + WAVE.replace("100 Q", "112 Q").replace("V128", "V140"))
I["aquababy-eletskaya"] = ("pink", "пеленальный столик",
    rect(18, 56, 92, 12, WOOD, 3) + path("M18 56 V40 H24 V56 M110 56 V40 H104 V56", WOOD) + rect(26, 46, 76, 12, P, 6, 2.4) +
    rect(24, 68, 80, 36, "#F7D7A8", 4) + rect(30, 74, 30, 12, WOOD, 3, 2) + rect(68, 74, 30, 12, WOOD, 3, 2) +
    rect(30, 90, 68, 10, WOOD, 3, 2) + line("M24 104 V114 M104 104 V114", O, 4) + f(64, 81, d=6, k=0.42, blush=False) + sp((104, 24, 6)))
I["aquababy-khoroshevskaya"] = ("blue", "детская лейка",
    path("M30 50 H82 L88 98 H24Z", G) + path("M82 60 L114 34 L118 40 L88 74", G) + ell(116, 37, 6, 9, "#5FB45A", 2.4) +
    thick("M38 50 Q56 22 74 50", G, 4) + f(56, 74, d=8, k=0.5) +
    "".join(line(f"M{x} {y} l3 7", "#BFE9FF", 3) for x, y in [(110, 52), (118, 54), (114, 64), (122, 66)]))
I["aquababy-lyublinskaya"] = ("sky", "детский надувной бассейн",
    ell(64, 84, 52, 24, B) + ell(64, 78, 52, 22, "#8ED3FA") + ell(64, 76, 38, 13, "#7FD3F7", 2.4) +
    path("M18 78 Q22 92 40 98 M110 78 Q106 92 88 98", sw=2) + "".join(circ(x, y, 3.4, Y, 1.6) for x, y in [(30, 70), (98, 70), (64, 58)]) +
    ell(52, 74, 7, 4, "#fff", 1.6) + ell(80, 79, 6, 3.4, "#fff", 1.6) + f(64, 94, d=7, k=0.45) + sp((24, 30, 7), (104, 28, 5)))
I["aquababy-profsoyuznaya"] = ("teal", "надувной матрас",
    WAVE + path("M14 70 Q12 52 30 52 H100 Q118 52 116 70 Q118 88 100 88 H30 Q12 88 14 70Z", OR) +
    "".join(line(f"M{x} 56 V84", "#E07A2A", 3) for x in (40, 56, 72, 88)) + rect(98, 56, 14, 28, Y, 6, 2.2) +
    f(64, 70, d=7, k=0.45) + sp((26, 30, 6), (100, 30, 5)))
I["aquababy-khimki-panfilova"] = ("blue", "тонущие палочки для ныряния",
    "".join(rect(x, y, 16, 64, c, 8) + rect(x, y + 40, 16, 6, "#fff", 2, 1.4) for x, y, c in [(26, 34, R), (56, 22, Y), (86, 40, G)]) +
    f(64, 44, d=4, k=0.32) + WAVE.replace("100 Q", "86 Q") + "".join(circ(x, y, 3, "#fff", 1.4) for x, y in [(106, 24), (112, 14)]))
I["aquababy-khimki-molodezhnaya"] = ("sky", "сачок для чистки бассейна",
    WAVE + thick("M18 18 L74 74", "#C9CED9", 5) + path("M70 66 Q96 58 112 78 Q110 104 84 104 Q64 96 70 66Z", "#E9F7FF") +
    "".join(line(d, "#9AA0B8", 1.4) for d in ["M76 72 L100 100", "M86 66 L108 92", "M70 84 L90 104", "M78 70 L70 92", "M96 66 L84 102"]) +
    path("M70 66 Q96 58 112 78", sw=3.4) + ell(92, 110, 5, 2.6, G, 1.6) + f(40, 40, d=4, k=0.32, blush=False) + sp((104, 24, 6)))
I["aquababy-khimki-michurina"] = ("purple", "беруши для плавания",
    path("M40 44 Q40 26 52 26 Q62 26 60 44 Q58 60 48 62 Q40 60 40 44Z", Y) + path("M76 44 Q76 26 88 26 Q98 26 96 44 Q94 60 84 62 Q76 60 76 44Z", Y) +
    line("M48 62 Q48 100 66 100 Q86 100 86 62", OR, 3) + ell(50, 38, 4, 7, "#FFE7A8", 1.4) + ell(86, 38, 4, 7, "#FFE7A8", 1.4) +
    rect(46, 92, 40, 20, B, 6) + f(66, 102, d=5, k=0.36) + sp((22, 30, 6), (108, 96, 5)))
I["aquababy-krasnogorsk-bulvar"] = ("teal", "гермомешок (драйбэг)",
    path("M34 40 H94 L98 106 Q64 116 30 106Z", OR) + rect(30, 26, 68, 16, "#E07A2A", 5) + line("M34 34 H94", O, 2) +
    thick("M30 34 Q14 40 22 58 M98 34 Q114 40 106 58", DK, 3) + rect(44, 82, 40, 12, "#FFE7A8", 4, 2) +
    f(64, 62, d=7, k=0.45) + WAVE.replace("100 Q", "112 Q") + sp((112, 22, 6)))
I["aquababy-krasnogorsk-opolcheniya"] = ("blue", "детский гидрокостюм",
    path("M44 22 H84 L104 40 L96 54 L86 46 V112 H70 L64 80 L58 112 H42 V46 L32 54 L24 40Z", DK) +
    path("M44 22 Q64 34 84 22", "#5CB7F2", 2.4) + line("M64 30 V76", Y, 3) + rect(48, 50, 10, 30, B, 3, 2) + rect(70, 50, 10, 30, B, 3, 2) +
    f(64, 90, d=5, k=0.36, blush=False).replace(O, "#fff") + sp((18, 90, 6), (110, 92, 5)))
I["aquababy-otradnoe-pyatnitskaya"] = ("night", "подводный фонарик",
    '<path d="M70 56 L122 30 V94 L70 72Z" fill="#FFF3B0" opacity=".6"/>' +
    rect(20, 50, 46, 28, Y, 8) + rect(62, 46, 12, 36, "#9AA0B8", 3) + rect(30, 54, 10, 20, OR, 3, 2) +
    line("M20 64 Q8 64 8 80", O, 3) + f(46, 64, d=6, k=0.42) + "".join(circ(x, y, 3, "#fff", 1.4) for x, y in [(30, 30), (40, 20), (100, 104)]))
I["aquababy-korolev"] = ("yellow", "шкафчик в раздевалке",
    rect(28, 14, 72, 102, "#7FC8F0", 6) + line("M64 14 V116", O, 3) +
    "".join(line(f"M{x} {y} h18", "#4E8DB8", 3) for x in (36, 70) for y in (24, 30, 36)) +
    circ(56, 66, 3.4, GR, 1.6) + circ(72, 66, 3.4, GR, 1.6) + rect(32, 98, 28, 10, "#E5F4FF", 2, 1.6) + rect(68, 98, 28, 10, "#E5F4FF", 2, 1.6) +
    f(46, 80, d=5, k=0.36) + f(82, 80, d=5, k=0.36) + sp((112, 30, 6)))
I["detskaya-bukhta-ostrovityanova"] = ("green", "питьевой фонтанчик",
    rect(50, 64, 28, 50, GR, 4) + path("M30 56 H98 Q98 72 64 72 Q30 72 30 56Z", "#D7DCE8") + rect(60, 44, 8, 14, "#9AA0B8", 2, 2) +
    line("M66 44 Q80 18 96 40", "#7FD3F7", 5) + "".join(circ(x, y, 2.4, "#BFE9FF", 1.2) for x, y in [(98, 46), (92, 52)]) +
    f(64, 92, d=6, k=0.42) + sp((24, 30, 6), (108, 96, 5)))
I["detskaya-bukhta-lefortovo"] = ("orange", "вешалка с крючками",
    rect(14, 30, 100, 14, WOOD, 4) + "".join(path(f"M{x} 44 V58 Q{x} 66 {x+8} 62", sw=3.4) for x in (30, 60, 90)) +
    path("M22 62 H44 L48 104 H18Z", P) + path("M52 62 Q64 70 76 62 L80 92 H48Z", B) + ell(98, 72, 12, 10, Y) +
    f(64, 80, d=5, k=0.36) + "".join(circ(x, 37, 2.4, BR, 1.2) for x in (24, 104)))
I["detskaya-bukhta-izmaylovo"] = ("sky", "ростомер",
    rect(70, 10, 26, 108, Y, 4) + "".join(line(f"M70 {y} h{12 if i % 2 else 7}", O, 2) for i, y in enumerate(range(18, 112, 8))) +
    rect(56, 40, 40, 8, R, 3) + circ(46, 70, 14, SKIN) + path("M32 66 Q46 46 60 66", BR, 2.4) + f(46, 72, d=5, k=0.36) +
    path("M34 84 H58 V112 H34Z", G) + sp((22, 28, 6)))
I["detskaya-bukhta-reutov"] = ("purple", "напольные весы",
    rect(22, 44, 84, 66, "#F1F3F8", 16) + rect(42, 54, 44, 20, DK, 6, 2.4) + txt(64, 69, "18,5", 13, "#7CF0C0") +
    ell(46, 92, 12, 8, GR, 2) + ell(82, 92, 12, 8, GR, 2) + f(64, 84, d=5, k=0.36, blush=False) + sp((20, 26, 6), (108, 26, 5)))
I["aqua-nemo-prazhskaya"] = ("teal", "абонемент с печатями",
    rect(16, 32, 96, 64, "#FFF8E6", 8) + rect(16, 32, 96, 16, TQ, 8, 2.4) + txt(64, 45, "8 ЗАНЯТИЙ", 10, "#fff") +
    "".join(circ(x, y, 7, R if (i < 5) else "#FFF8E6", 2) for i, (x, y) in enumerate([(32, 62), (52, 62), (72, 62), (92, 62), (32, 82), (52, 82), (72, 82), (92, 82)])) +
    path("M28 58 l4 4 6-8 M48 58 l4 4 6-8", "none", 1.6).replace(O, "#fff") + f(82, 82, d=4, k=0.3) + sp((110, 104, 6)))
I["aqua-nemo-akademicheskaya"] = ("pink", "лейкопластырь",
    f'<g transform="rotate(-35 64 64)">' + rect(14, 46, 100, 36, "#F7C99A", 18) + rect(44, 50, 40, 28, "#FBE3C8", 6, 2) +
    "".join(circ(x, y, 1.8, "#D9A070", 0.8) for x in (24, 32, 96, 104) for y in (58, 70)) + "</g>" +
    f(64, 64, d=6, k=0.42) + sp((24, 28, 6), (104, 100, 6)))
I["aqua-nemo-khovrino"] = ("blue", "пончо-дождевик",
    path("M64 18 Q84 18 86 40 L112 96 Q64 110 16 96 L42 40 Q44 18 64 18Z", Y) + path("M48 40 Q64 52 80 40 Q78 26 64 26 Q50 26 48 40Z", "#FFE7A8", 2.4) +
    f(64, 66, d=7, k=0.45) + "".join(line(f"M{x} {y} l-3 8", "#E5F4FF", 2.6) for x, y in [(18, 20), (30, 34), (104, 22), (116, 40), (24, 56)]))
I["aqua-nemo-sevastopolskaya"] = ("yellow", "турникет на входе",
    rect(20, 40, 30, 70, GR, 6) + rect(78, 40, 30, 70, GR, 6) + rect(26, 48, 18, 10, "#7CF0C0", 3, 2) +
    thick("M50 64 H76 M50 64 L66 80 M50 64 L66 48", "#D7DCE8", 4) + circ(50, 64, 6, DK) +
    f(93, 76, d=5, k=0.36) + sp((64, 24, 7)))
I["aqua-nemo-sviblovo"] = ("green", "бейдж участника на ленте",
    thick("M30 10 L58 66 M98 10 L70 66", B, 8) +
    rect(34, 62, 60, 50, "#FFFFFF", 8) + rect(34, 62, 60, 14, R, 8, 2) + rect(56, 58, 16, 10, GR, 3, 2) +
    line("M44 96 H84 M48 104 H80", GR, 3) + f(64, 86, d=5, k=0.36) + sp((112, 90, 6)))
I["aqua-nemo-lyubertsy"] = ("orange", "клетчатый плед",
    path("M16 40 H96 Q112 40 112 56 V104 H32 Q16 104 16 88Z", R) +
    "".join(line(f"M{x} 40 V104", "#F7A493", 5) for x in (36, 60, 84)) + "".join(line(f"M16 {y} H112", "#F7A493", 5) for y in (56, 80)) +
    path("M96 40 Q112 40 112 56 Q100 50 96 40Z", "#C94A3A", 2) + "".join(line(f"M{x} 104 v8", O, 2) for x in (40, 52, 64, 76, 88, 100)) +
    f(64, 72, d=7, k=0.45) + sp((22, 24, 6)))
I["more-detyam-malygina"] = ("sky", "поющие бокалы с водой",
    "".join(path(f"M{x} 40 H{x+22} Q{x+22} 70 {x+11} 72 Q{x} 70 {x} 40Z", "#F1F8FF") + path(f"M{x+1} {y} H{x+21} Q{x+20} 70 {x+11} 70 Q{x+2} 70 {x+1} {y}Z", "#7FD3F7", 1.6) +
            line(f"M{x+11} 72 V96 M{x+2} 98 H{x+20}", O, 3) for x, y in [(12, 62), (40, 54), (68, 48), (96, 58)]) +
    path("M22 40 Q14 28 20 20", sw=2) + "".join(txt(x, 26, "♪", 14) for x in (54, 84)) + f(51, 82, d=4, k=0.3) + WAVE.replace("100 Q", "112 Q"))

# ===================== Танцы и балет =====================
I["zvezda-dance-petrozavodskaya"] = ("orange", "бандана",
    path("M14 44 Q64 24 114 44 L64 112Z", R) + "".join(circ(x, y, 4, "#fff", 1.4) for x, y in [(40, 50), (64, 44), (88, 50), (52, 70), (76, 70), (64, 92)]) +
    path("M14 44 L4 30 M14 44 L6 56 M114 44 L124 30 M114 44 L122 56", sw=4) + f(64, 58, d=6, k=0.42, blush=False) + sp((104, 100, 6)))
I["zvezda-dance-playpark"] = ("night", "лаунчпад с кнопками",
    rect(16, 24, 96, 82, DK, 10) + "".join(rect(24 + c * 22, 32 + r * 18, 16, 12, [P, B, Y, G][(r + c) % 4], 3, 1.8)
                                           for r in range(4) for c in range(4)) +
    f(64, 96, d=6, k=0.4, blush=False).replace(O, "#fff") + sp((112, 18, 6), (14, 112, 5)))
I["zvezda-dance-armada"] = ("purple", "худи с капюшоном",
    path("M40 26 Q64 10 88 26 L114 50 L102 66 L92 58 V112 H36 V58 L26 66 L14 50Z", OR) + path("M46 26 Q64 46 82 26 Q64 16 46 26Z", "#E07A2A", 2.4) +
    line("M58 38 V60 M70 38 V60", WH, 2.4) + rect(46, 84, 36, 16, "#E07A2A", 6, 2.4) + f(64, 70, d=7, k=0.45) + sp((112, 96, 6)))
I["zvezda-dance-shchipkovsky"] = ("night", "генератор дыма",
    rect(14, 72, 54, 34, GR, 6) + rect(66, 80, 14, 14, "#9AA0B8", 3) +
    path("M80 86 Q92 70 104 80 Q118 66 122 84 Q128 98 112 100 Q100 108 90 98 Q78 100 80 86Z", "#E9ECF6") +
    path("M86 66 Q96 52 108 60 Q118 50 122 62", "#F4F6FB", 2.2) + f(40, 88, d=7, k=0.45) + sp((30, 30, 6), (64, 26, 4)))
I["zvezda-dance-shchepkina"] = ("pink", "поп-фильтр у микрофона",
    thick("M34 112 V70 M34 70 L58 54", GR, 4) + rect(52, 34, 18, 34, GR, 9) + "".join(line(f"M52 {y} h18", O, 1.4) for y in (42, 48, 54)) +
    circ(90, 50, 24, "#2B2A44") + circ(90, 50, 19, "#5A5876", 1.4) +
    "".join(line(d, "#77749A", 1) for d in ["M76 40 L104 64", "M74 50 L100 70", "M80 32 L106 54", "M90 30 L108 46"]) +
    line("M70 56 Q76 70 70 82", O, 2) + f(90, 50, d=5, k=0.36, blush=False).replace(O, "#fff"))
I["idanko-ballet-starokirochny"] = ("yellow", "гримёрное зеркало с лампочками",
    rect(22, 18, 84, 78, "#F2D6B3", 10) + rect(34, 30, 60, 54, "#DDF3FF", 6) +
    "".join(circ(x, y, 5, "#FFF6C4", 1.8) for x in (28, 100) for y in (30, 50, 70, 90)) + "".join(circ(x, 22, 5, "#FFF6C4", 1.8) for x in (48, 64, 80)) +
    rect(14, 98, 100, 12, WOOD, 3) + f(64, 58, d=7, k=0.45))
I["idanko-ballet-kedrova"] = ("purple", "круглая банкетка пианиста",
    ell(64, 44, 38, 14, R) + path("M26 44 V54 Q64 70 102 54 V44", R) + ell(64, 42, 34, 10, "#F28A78", 1.6) +
    thick("M40 62 L34 112 M88 62 L94 112 M60 66 V112", BR, 5) + thick("M46 90 H82", BR, 3) + f(64, 46, d=6, k=0.42) + sp((112, 24, 6), (16, 100, 5)))
I["idanko-ballet-baltiyskaya"] = ("pink", "боа из перьев",
    "".join(ell(x, y, 10, 7, c, 2) for x, y, c in [(20, 30, P), (32, 42, "#FFB3CF"), (44, 54, P), (56, 64, "#FFB3CF"), (70, 70, P), (84, 72, "#FFB3CF"),
                                                     (96, 68, P), (106, 58, "#FFB3CF"), (110, 44, P), (104, 32, "#FFB3CF")]) +
    "".join(line(f"M{x} {y} l{dx} {dy}", "#fff", 1.4) for x, y, dx, dy in [(20, 30, -6, -4), (44, 54, -6, 4), (70, 70, 0, 8), (96, 68, 4, 6), (110, 44, 6, 0)]) +
    f(70, 70, d=4, k=0.3) + sp((60, 26, 7), (30, 100, 5)))
I["idanko-ballet-novomaryinskaya"] = ("green", "веночек с лентами",
    ell(64, 44, 42, 20, "none", 7).replace(O, "#5FB45A") +
    "".join(circ(x, y, 7, c, 2) for x, y, c in [(24, 44, R), (40, 30, Y), (64, 24, P), (88, 30, B), (104, 44, R), (64, 64, Y), (40, 58, V), (88, 58, V)]) +
    "".join(thick(f"M{x} 64 Q{x+dx} 90 {x+dx*2} 116", c, 4) for x, dx, c in [(46, -6, R), (56, -2, B), (72, 2, Y), (82, 6, P)]) + f(64, 44, d=5, k=0.36))
I["idanko-ballet-garibaldi"] = ("orange", "браслет с бубенцами на щиколотку",
    ell(64, 50, 40, 16, "none", 8).replace(O, "#E05A8A") +
    "".join(circ(x, y, 9, GOLD) + line(f"M{x-5} {y+2} H{x+5}", O, 1.6) + circ(x, y + 5, 1.6, O, 0.1)
            for x, y in [(28, 64), (48, 74), (64, 76), (80, 74), (100, 64)]) + f(64, 40, d=5, k=0.36) + sp((20, 28, 6), (112, 100, 6)))
I["probalet-garibaldi"] = ("purple", "воздушные полотна",
    rect(20, 8, 88, 8, GR, 3) + path("M54 16 Q50 60 40 116 H56 Q60 60 62 16Z", "#FF7FA8") + path("M66 16 Q68 60 72 116 H88 Q78 60 74 16Z", "#E05A8A") +
    path("M48 70 Q64 80 80 70 Q64 88 48 70Z", "#FFB3CF", 2) + f(64, 46, d=4, k=0.32) + sp((24, 40, 6), (106, 50, 5), (100, 100, 4)))

# ===================== Лёд: фигурное катание и хоккей =====================
I["sport-katok-kosino"] = ("sky", "камень для кёрлинга",
    ICEF + ell(64, 84, 44, 14, "#9AA0B8") + path("M20 84 V70 Q64 54 108 70 V84 Q64 100 20 84Z", "#C9CED9") + ell(64, 68, 44, 14, "#E05A4A") +
    thick("M52 62 V44 H84", Y, 6) + f(64, 76, d=6, k=0.42) + sp((24, 30, 6), (104, 30, 5)))
I["sport-katok-yurlovsky"] = ("blue", "стадионная трибуна",
    "".join(rect(14 + i * 6, 40 + i * 18, 100 - i * 12, 14, c, 3) for i, c in enumerate([R, Y, B, G])) +
    "".join(circ(x, 34 + i * 18, 5, SKIN, 1.6) for i, row in enumerate([(30, 64, 98), (40, 80), (52, 76), ()]) for x in row) +
    f(64, 87, d=5, k=0.36) + sp((112, 20, 6)))
I["sport-katok-mayak"] = ("pink", "чемпионская лента через плечо",
    path("M30 14 L48 14 L104 112 L86 112Z", R) + path("M38 14 L94 112", "none", 2).replace(O, Y) +
    path("M86 112 L80 124 M104 112 L110 124", sw=3) + circ(66, 64, 16, GOLD) + txt(66, 69, "1", 14) +
    f(66, 90, d=5, k=0.36) + sp((24, 92, 7), (108, 30, 5)))
I["sport-katok-ostrov"] = ("teal", "значок-пин",
    circ(64, 60, 38, "#FFFFFF") + circ(64, 60, 30, B, 2.4) + path("M64 40 L69 54 H84 L72 63 L76 78 L64 69 L52 78 L56 63 L44 54 H59Z", Y, 2) +
    rect(58, 98, 12, 6, GR, 2, 2) + thick("M64 104 V116", GR, 3) + f(64, 60, d=4, k=0.3) + sp((20, 26, 6), (108, 100, 5)))
I["sport-katok-krylatskoe"] = ("night", "снежная пушка-вентилятор",
    ICEF + thick("M48 100 L60 74 M76 100 L64 74", GR, 5) + circ(58, 50, 30, "#D7DCE8") + circ(58, 50, 23, "#5A5876", 2) +
    "".join(f'<g transform="rotate({a} 58 50)">' + ell(58, 38, 6, 12, "#B8BCCB", 1.6) + "</g>" for a in (0, 90, 180, 270)) + circ(58, 50, 6, R, 2) +
    "".join(circ(x, y, r, "#fff", 1.2) for x, y, r in [(98, 40, 4), (110, 30, 3), (106, 52, 3.4), (120, 44, 2.6), (116, 60, 2.4)]) +
    f(58, 50, d=0, k=0, mouth=False, blush=False))
I["sport-katok-vegas-krokus"] = ("purple", "медальница на стене",
    rect(14, 26, 100, 22, DK, 6) + txt(64, 42, "ЧЕМПИОН", 12, "#FFD25E") +
    "".join(thick(f"M{x} 48 L{x+4} 74", c, 3) + circ(x + 4, 84, 11, m) for x, c, m in [(26, R, GOLD), (50, B, "#D7DCE8"), (74, G, "#E2A267"), (96, P, GOLD)]) +
    f(54, 84, d=4, k=0.3) + sp((112, 104, 6)))
I["rfhockey-alaska"] = ("green", "рация тренера",
    rect(36, 34, 52, 80, DK, 10) + rect(46, 16, 8, 22, "#5A5876", 3) + rect(44, 44, 36, 24, "#7CF0C0", 4, 2) +
    "".join(circ(x, y, 3, GR, 1.2) for x in (50, 62, 74) for y in (78, 88, 98)) + f(62, 54, d=6, k=0.42) +
    path("M98 40 Q106 50 98 60 M106 34 Q118 50 106 66", sw=2.6) + sp((22, 30, 6)))
I["rfhockey-aviapark"] = ("yellow", "турнирная сетка плей-офф",
    rect(12, 18, 104, 92, "#FFFFFF", 8) +
    "".join(rect(18, y, 26, 10, c, 2, 1.6) for y, c in [(26, B), (42, R), (66, G), (82, P)]) + rect(54, 34, 26, 10, B, 2, 1.6) + rect(54, 74, 26, 10, G, 2, 1.6) +
    rect(88, 54, 24, 12, GOLD, 2, 1.6) + line("M44 31 H49 V47 H44 M49 39 H54 M44 71 H49 V87 H44 M49 79 H54 M80 39 H84 V79 H80 M84 60 H88", O, 2) +
    f(100, 82, d=4, k=0.3))
I["rfhockey-fili"] = ("orange", "силовые сани-прицеп",
    path("M18 96 H96 Q110 96 112 84", sw=5) + rect(24, 66, 66, 26, R, 4) + rect(36, 48, 12, 18, GR, 2) + ell(42, 48, 14, 5, "#9AA0B8") +
    ell(42, 42, 14, 5, "#9AA0B8") + thick("M90 76 L120 54", "#FFE7A8", 3) + f(66, 80, d=6, k=0.42) + sp((24, 26, 6)))
I["rfhockey-snezhkom"] = ("teal", "тренировочная покрышка",
    ell(64, 88, 48, 20, DK) + ell(64, 80, 48, 20, "#4A4868") + ell(64, 78, 24, 9, "#2B2A44", 2.4) +
    "".join(line(f"M{x} {y} l6 -6", "#77749A", 2) for x, y in [(22, 84), (36, 92), (88, 92), (100, 84), (30, 70), (94, 70)]) +
    f(64, 54, d=0, k=0, mouth=False, blush=False) + f(64, 66, d=7, k=0.45).replace(O, "#fff") + sp((20, 30, 6), (106, 28, 5)))
I["hamovniki-hockey"] = ("blue", "лототрон с шарами",
    circ(64, 54, 36, "#E9F7FF") + "".join(circ(x, y, 8, c, 2) for x, y, c in [(50, 68, R), (66, 74, Y), (80, 64, G), (58, 52, B), (74, 46, P)]) +
    thick("M64 90 V106 M40 110 H88", GR, 5) + thick("M100 54 H116 V66", GR, 4) +
    f(56, 36, d=5, k=0.36) + sp((20, 24, 6)))
I["ldinka-korovinskoe"] = ("pink", "диаболо на нитке",
    thick("M14 30 L44 74 M114 30 L84 74", WOOD, 4) + line("M44 74 Q64 92 84 74", O, 1.6) +
    path("M44 60 L64 76 L44 92Z", R) + path("M84 60 L64 76 L84 92Z", R) + circ(64, 76, 5, "#C94A3A", 2) +
    ell(44, 76, 4, 16, "#F28A78", 2) + ell(84, 76, 4, 16, "#F28A78", 2) + f(64, 48, d=5, k=0.36) + sp((106, 104, 6)))
I["arenaplay-skating"] = ("purple", "жонглёрские мячи",
    "".join(circ(x, y, 13, c) + path(f"M{x-13} {y} Q{x} {y-8} {x+13} {y}", sw=1.6) for x, y, c in [(34, 70, R), (64, 34, Y), (94, 70, G)]) +
    path("M38 52 Q48 30 56 30 M72 30 Q82 30 90 52", "none", 1.6).replace(O, "#fff") + f(64, 38, d=4, k=0.3) + f(34, 74, d=4, k=0.3) +
    path("M20 108 Q64 92 108 108", sw=3) + sp((112, 26, 6)))
I["olimp-ice-loko"] = ("sky", "пакет со льдом",
    path("M30 46 Q30 30 46 30 H82 Q98 30 98 46 V96 Q98 110 82 110 H46 Q30 110 30 96Z", "#7FC8F0") + rect(52, 18, 24, 14, B, 4) +
    "".join(rect(x, y, 14, 14, "#E9F7FF", 3, 1.6) for x, y in [(40, 76), (58, 82), (74, 74), (48, 92), (68, 94)]) +
    f(64, 56, d=7, k=0.45) + sp((18, 28, 6), (110, 104, 5)))

# ===================== Футбол =====================
I["cska-football-plyushchikha"] = ("green", "сетка-ребаундер",
    GRASS + path("M24 30 H104 L96 96 H32Z", "#E9F7FF") + "".join(line(f"M{x} 32 L{x - (x-64)//8} 94", "#9AA0B8", 1.4) for x in range(34, 104, 10)) +
    "".join(line(f"M{26 + (y-30)//8} {y} H{102 - (y-30)//8}", "#9AA0B8", 1.4) for y in range(40, 96, 10)) +
    path("M24 30 H104 L96 96 H32Z", "none", 4).replace(O, R) + thick("M32 96 L24 112 M96 96 L104 112", R, 3) + f(64, 62, d=7, k=0.45))
I["cska-football-novogireevo"] = ("teal", "фишки-тарелочки для разметки",
    GRASS + "".join(ell(x, y, 16, 6, c) + ell(x, y - 4, 9, 4, "#fff", 1.6) for x, y, c in [(26, 98, OR), (60, 86, Y), (96, 98, OR), (44, 112, Y), (84, 114, OR)]) +
    f(60, 72, d=5, k=0.36) + sp((22, 30, 6), (104, 34, 5)) + circ(108, 56, 9, "#fff", 2))
I["cska-football-marino-manezh"] = ("sky", "надувной купол манежа",
    GRASS + path("M10 100 Q10 30 64 30 Q118 30 118 100Z", "#F1F3F8") +
    "".join(line(f"M{x} 100 Q{x + (64-x)//3} 36 64 31", "#C9CED9", 2) for x in (30, 48, 80, 98)) +
    rect(52, 76, 24, 24, B, 4) + path("M10 100 Q10 30 64 30 Q118 30 118 100", "none", 3.2) + f(64, 58, d=7, k=0.45) + sp((112, 18, 6)))
I["cska-football-yasenevo"] = ("yellow", "рулетка",
    circ(50, 60, 32, Y) + circ(50, 60, 14, "#E0B030", 2.4) + rect(78, 76, 14, 10, R, 2) +
    path("M80 86 H122 V96 H80Z", "#F7E6A0", 2) + "".join(line(f"M{x} 86 v{5 if i % 2 else 8}", O, 1.4) for i, x in enumerate(range(84, 122, 4))) +
    f(50, 60, d=5, k=0.36) + sp((100, 30, 6), (20, 104, 5)))
I["spartak-cityfootball-sokolniki"] = ("orange", "мяч-прыгун с рожками",
    circ(64, 72, 38, R) + thick("M50 38 Q46 22 36 22", R, 6) + thick("M78 38 Q82 22 92 22", R, 6) + circ(36, 22, 5, R) + circ(92, 22, 5, R) +
    ell(50, 58, 10, 6, "#F59383", 0.1) + f(64, 76, d=9, k=0.62) + path("M10 116 Q64 104 118 116", sw=3))
I["spartak-cityfootball-tulskaya"] = ("purple", "поясная сумка",
    thick("M6 54 Q64 40 122 54", DK, 6) + path("M28 56 Q28 44 44 44 H84 Q100 44 100 56 V82 Q100 98 84 98 H44 Q28 98 28 82Z", R) +
    line("M34 62 Q64 54 94 62", O, 2.4) + rect(58, 50, 12, 6, GR, 2, 1.4) + f(64, 78, d=7, k=0.45) + sp((20, 100, 6), (108, 26, 5)))
I["spartak-cityfootball-rublevo"] = ("green", "тарзанка",
    path("M0 26 Q64 10 128 22 V8 H0Z", BR) + thick("M64 18 L84 92", "#E8C27A", 4) + circ(86, 100, 14, R) + line("M74 100 H98", O, 2) +
    f(86, 100, d=4, k=0.3) + GRASS.replace("100 Q", "112 Q") + sp((26, 60, 6), (110, 50, 5)))
# ===================== Баскетбол, волейбол =====================
I["cska-basket-nagornaya"] = ("orange", "кистевой динамометр",
    path("M30 30 Q30 18 44 18 H84 Q98 18 98 30 V60 H30Z", GR) + circ(64, 40, 16, "#FFFFFF", 2.4) + line("M64 40 L74 32", R, 2.6) +
    "".join(line(f"M{x} 30 l2 3", O, 1.2) for x in (54, 64, 74)) + path("M30 60 Q30 112 64 112 Q98 112 98 60", sw=6) +
    path("M42 60 Q42 98 64 98 Q86 98 86 60", sw=4) + f(64, 78, d=5, k=0.36) + sp((112, 26, 6)))
I["cska-basket-lyublino"] = ("blue", "велотренажёр",
    path("M24 106 H104", sw=6) + thick("M40 106 L56 66 L86 66 L94 106", GR, 5) + rect(46, 52, 20, 8, DK, 4) + thick("M86 66 L94 40 H104", GR, 4) +
    circ(78, 84, 12, "#D7DCE8") + rect(66, 70, 30, 20, B, 6) + f(81, 80, d=5, k=0.36) + sp((22, 30, 6)))
I["cska-basket-butovo"] = ("yellow", "плетёный мяч сепактакрау",
    circ(64, 64, 40, "#E8B06E") + "".join(f'<polygon points="{x},{y-10} {x+9},{y-5} {x+9},{y+5} {x},{y+10} {x-9},{y+5} {x-9},{y-5}" fill="#FFE7A8" {W(2)}/>'
                                         for x, y in [(64, 40), (46, 52), (82, 52), (46, 76), (82, 76), (64, 88), (64, 64)]) +
    f(64, 64, d=5, k=0.36) + sp((20, 24, 6), (112, 108, 5)))
I["cska-basket-golovinskoe"] = ("teal", "мяч для флорбола",
    thick("M16 22 L74 82 Q78 90 70 96 L56 104", "#3E7FC8", 5) + circ(92, 82, 22, "#FFFFFF") +
    "".join(circ(x, y, 3.4, "#C9CED9", 1.2) for x, y in [(84, 70), (98, 72), (104, 84), (86, 92), (100, 96), (80, 82)]) + f(92, 80, d=4, k=0.3) + sp((104, 24, 6)))
I["ibasket-molodezhnaya"] = ("night", "карабин",
    thick("M52 18 Q26 18 26 50 V82 Q26 110 52 110 Q78 110 78 82 V44 Q78 18 56 18", OR, 7) + thick("M78 44 L60 26", "#D7DCE8", 5) +
    rect(70, 60, 16, 20, "#D7DCE8", 3) + f(52, 66, d=6, k=0.42).replace(O, "#fff") + sp((108, 26, 6), (104, 100, 5)))
I["ibasket-novokosino"] = ("green", "КП ориентирования (призма)",
    GRASS + thick("M64 72 V112", GR, 4) + path("M34 24 L64 14 L94 24 L94 64 L64 74 L34 64Z", "#FFFFFF") +
    path("M34 24 L64 34 L94 24 M64 34 V74", "none", 2.4) + path("M34 24 L64 34 L34 64Z", OR, 2) + path("M64 74 L94 64 L94 24 L64 34Z", "#FFFFFF", 2) +
    path("M64 34 L94 24 L94 64Z", OR, 2) + f(79, 48, d=4, k=0.3))
I["nevsky-bears-tsaritsyno"] = ("pink", "ядро для толкания",
    FLOOR + ell(64, 104, 30, 6, "#D9B080", 1.6) + circ(64, 64, 34, "#6E6A8A") + circ(52, 52, 8, "#8E8AAE", 0.1) +
    f(64, 68, d=7, k=0.5).replace(O, "#fff") + sp((108, 26, 6), (20, 30, 5)))
I["nevsky-bears-izmaylovo"] = ("sky", "диск для метания",
    ell(64, 64, 46, 22, "#D7DCE8") + ell(64, 64, 34, 15, "#8E6A4A", 2.4) + ell(64, 62, 12, 6, "#C9CED9", 2.4) +
    path("M14 92 Q30 100 44 92 M8 80 Q20 86 30 82", sw=2.4) + f(64, 72, d=5, k=0.36) + sp((112, 30, 6), (20, 30, 5)))
I["nevsky-bears-altufyevo"] = ("yellow", "грабли для прыжковой ямы",
    path("M0 96 Q64 84 128 96 V128 H0Z", "#F4D58C") + thick("M98 10 L50 84", WOOD, 5) + rect(24, 80, 56, 10, GR, 3) +
    "".join(line(f"M{x} 90 v10", O, 3) for x in range(30, 80, 9)) + f(52, 108, d=5, k=0.36) +
    "".join(circ(x, y, 1.6, "#D9B060", 0.1) for x, y in [(90, 104), (100, 110), (16, 108), (110, 100)]))
# ===================== Теннис, падел =====================
I["tennis-capital-petrovka"] = ("green", "корзина-тележка для теннисных мячей",
    thick("M30 112 L40 92 M98 112 L88 92", GR, 4) + path("M30 40 H98 L90 92 H38Z", "#E9ECF6") +
    "".join(line(d, "#9AA0B8", 1.4) for d in ["M44 40 L48 92", "M58 40 V92", "M70 40 V92", "M84 40 L80 92", "M34 58 H94", "M36 76 H92"]) +
    "".join(circ(x, y, 7, "#E8F56A", 1.6) for x, y in [(44, 34), (58, 30), (72, 32), (86, 34), (50, 22), (66, 20), (80, 24)]) +
    thick("M30 40 L20 18", GR, 4) + f(64, 66, d=6, k=0.42))
I["tennis-capital-kashirskaya"] = ("orange", "воротца для крикета",
    GRASS + "".join(thick(f"M{x} 34 V102", "#F2D6A8", 6) for x in (44, 64, 84)) + thick("M42 32 H62 M66 32 H86", "#E8B06E", 4) +
    circ(104, 92, 9, R) + line("M98 88 Q104 92 110 88", "#fff", 1.4) + f(104, 93, d=3, k=0.24) +
    f(64, 64, d=10, k=0.42, blush=False))
I["tennis-capital-yuzhnaya"] = ("purple", "клюшка для лакросса",
    thick("M22 114 L70 50", "#E9ECF6", 5) + path("M70 50 Q60 22 82 14 Q110 6 114 30 Q116 50 88 60Z", "none", 4) +
    "".join(line(d, "#C9CED9", 1.2) for d in ["M72 44 L106 22", "M76 52 L112 34", "M74 30 L94 54", "M84 18 L102 50"]) +
    circ(96, 36, 8, "#FFFFFF", 2) + f(96, 37, d=3, k=0.24) + sp((24, 30, 6), (110, 100, 5)))
I["champion-tennis-novaya-doroga"] = ("green", "бильярдный кий с шарами",
    rect(0, 70, 128, 58, "#3E9E5A", 0) + thick("M10 30 L74 76", "#E8B06E", 5) + line("M66 70 L74 76", "#5CB7F2", 6) +
    circ(86, 86, 10, "#FFFFFF") + "".join(circ(x, y, 10, c) for x, y, c in [(104, 76, R), (106, 98, Y), (88, 108, B)]) +
    f(86, 86, d=3, k=0.24) + sp((106, 26, 6)))
I["tennis-park-ryazansky"] = ("sky", "слэклайн между деревьями",
    GRASS + rect(10, 30, 14, 76, BR, 4) + rect(104, 30, 14, 76, BR, 4) + circ(17, 26, 18, G) + circ(111, 26, 18, G) +
    thick("M24 66 Q64 80 104 66", Y, 4) + circ(64, 52, 9, SKIN, 2) + thick("M64 61 V72 M52 56 L76 56", B, 3) +
    f(64, 52, d=3, k=0.24))
I["padlhub-yasenevo"] = ("yellow", "мешок для бега в мешках",
    GRASS + path("M36 40 Q30 76 36 108 H92 Q98 76 92 40Z", "#E8C99A") + path("M36 40 Q64 50 92 40", sw=3) +
    "".join(line(f"M{x} 60 l4 4", "#C9A070", 2) for x in (46, 70, 84)) + circ(64, 28, 14, SKIN) + f(64, 30, d=4, k=0.32) +
    path("M50 22 Q64 6 78 22", BR, 2) + sp((112, 30, 6), (16, 40, 5)))
I["padlhub-terekhovo"] = ("orange", "ходули",
    thick("M44 14 V116 M84 14 V116", WOOD, 6) + rect(30, 76, 16, 8, R, 2) + rect(82, 76, 16, 8, R, 2) +
    thick("M44 84 L36 76 M84 84 L92 76", WOOD, 3) + f(64, 46, d=8, k=0.5) + sp((20, 30, 6), (108, 104, 5)))
I["a-padel-khodynka"] = ("pink", "йо-йо",
    line("M64 8 V40", O, 2) + circ(64, 8, 3, R, 1.6) + circ(64, 72, 36, R) + circ(64, 72, 26, "#F28A78", 2) + circ(64, 72, 7, "#C94A3A", 2) +
    f(64, 86, d=6, k=0.42) + sp((22, 30, 6), (108, 30, 5)))

# ===================== Единоборства =====================
I["tri-medvedya-mitino"] = ("blue", "борцовский манекен-чучело",
    FLOOR + path("M40 30 Q40 16 64 16 Q88 16 88 30 V58 L112 50 L116 62 L88 74 V100 L78 104 H50 L40 100 V74 L12 62 L16 50 L40 58Z", "#C0584A") +
    line("M64 18 V100", "#A04438", 2) + f(64, 38, d=7, k=0.45) + sp((22, 26, 6)))
I["tri-medvedya-slavyansky"] = ("orange", "скоростная груша на платформе",
    rect(14, 14, 100, 14, WOOD, 4) + rect(58, 28, 12, 8, GR, 2) + path("M64 36 Q90 46 82 80 Q76 96 64 96 Q52 96 46 80 Q38 46 64 36Z", R) +
    ell(56, 56, 5, 10, "#F59383", 0.1) + f(64, 70, d=7, k=0.45) + path("M20 60 Q28 66 20 72 M108 60 Q100 66 108 72", sw=2.4))
I["tri-medvedya-svobodny"] = ("yellow", "свиток с иероглифом",
    rect(34, 22, 60, 84, "#FFF8E6", 3) + rect(28, 14, 72, 10, BR, 5) + rect(28, 104, 72, 10, BR, 5) +
    line("M52 40 H76 M64 32 V60 M50 60 L64 50 L78 60 M54 74 H74 M64 66 V92", O, 4) + circ(80, 88, 6, R, 1.6) +
    line("M40 14 L50 4 L60 14", O, 2) + sp((112, 30, 6), (16, 96, 5)))
I["tri-medvedya-federativny"] = ("green", "гимнастические палки",
    FLOOR + "".join(f'<g transform="rotate({a} 64 70)">' + thick("M14 70 H114", c, 6) + "</g>" for a, c in [(-20, R), (0, Y), (20, B)]) +
    f(64, 92, d=6, k=0.42) + sp((24, 30, 6), (104, 30, 5)))
I["tri-medvedya-elektrozavodskaya"] = ("purple", "тканевый тоннель-лаз",
    FLOOR + "".join(ell(x, 64, 18, 36, c, 2.6) for x, c in [(30, R), (52, Y), (74, G), (96, B)]) + ell(96, 64, 12, 28, "#3E4AA0", 2) +
    f(96, 64, d=4, k=0.32).replace(O, "#fff"))
I["tri-medvedya-magnitogorskaya"] = ("sky", "поролоновый клин-горка",
    FLOOR + path("M16 100 L104 40 V100Z", B) + path("M104 40 L116 46 V104 L104 100Z", "#3E8FD0") + path("M16 100 L28 104 H116", sw=3) +
    f(80, 80, d=6, k=0.42) + sp((24, 30, 6), (60, 30, 5)))
I["tri-medvedya-kommunarka"] = ("night", "фехтовальная маска",
    path("M34 30 Q34 14 64 14 Q94 14 94 30 V84 Q94 108 64 108 Q34 108 34 84Z", "#4A4868") +
    "".join(line(f"M{x} 22 V102", "#77749A", 1.4) for x in range(42, 92, 6)) + "".join(line(f"M36 {y} H92", "#77749A", 1.4) for y in range(26, 104, 6)) +
    path("M34 30 Q34 14 64 14 Q94 14 94 30 V84 Q94 108 64 108 Q34 108 34 84Z", "none", 3.2) + path("M28 92 Q64 120 100 92 L100 104 Q64 128 28 104Z", "#FFFFFF") +
    f(64, 58, d=8, k=0.5).replace(O, "#fff") + sp((112, 24, 6)))
I["tri-medvedya-troitsk"] = ("orange", "ситар",
    circ(44, 88, 26, "#E8B06E") + circ(44, 88, 17, "#C88A50", 2) + thick("M54 70 L104 14", "#C88A50", 9) +
    "".join(line(f"M{58 + i * 9} {66 - i * 10} l6 5", O, 1.6) for i in range(5)) + line("M30 98 L104 14", "#fff", 0.9) +
    circ(100, 30, 4, Y, 1.4) + f(44, 88, d=5, k=0.36) + sp((20, 30, 6)))
I["ronin-club-borisovo"] = ("teal", "барабан джембе",
    path("M30 30 H98 Q90 60 76 66 L84 112 H44 L52 66 Q38 60 30 30Z", "#C88A50") + ell(64, 30, 34, 9, "#F7E6C8") +
    "".join(line(f"M{a} 36 L{b} 104", "#7A4A20", 1.6) for a, b in [(36, 50), (50, 56), (78, 72), (92, 78)]) +
    path("M54 66 H74", sw=2.4) + f(64, 46, d=6, k=0.42) + sp((112, 104, 6)))
I["bayder-aikido-vyatskaya"] = ("purple", "поющая чаша с палочкой",
    path("M20 60 H108 Q104 104 64 104 Q24 104 20 60Z", GOLD) + ell(64, 60, 44, 10, "#E0A830") + ell(64, 60, 36, 6, "#C98E20", 1.6) +
    thick("M82 50 L118 22", BR, 5) + path("M24 40 Q18 30 24 22 M104 40 Q112 32 106 22", sw=2.2) + f(64, 82, d=7, k=0.45) + ell(64, 112, 26, 4, "#B33A3A", 2))
I["bayder-aikido-babushkina"] = ("yellow", "диджериду",
    f'<g transform="rotate(-38 64 64)">' + path("M2 54 H116 Q126 54 126 64 Q126 74 116 74 H2Z", "#C0732E") +
    "".join(path(f"M{x} 56 Q{x+4} 64 {x} 72", "none", 2).replace(O, "#7A4A20") for x in (20, 40, 60, 80)) +
    "".join(circ(x, 64, 2.4, Y, 0.1) for x in (30, 50, 70, 90)) + "</g>" + f(64, 64, d=5, k=0.36) + sp((26, 30, 6), (104, 100, 5)))
I["bayder-aikido-pokryshkina"] = ("pink", "барабаны бонго",
    path("M18 46 H58 L52 98 H24Z", "#C88A50") + ell(38, 46, 20, 7, "#F7E6C8") + path("M62 54 H110 L102 106 H70Z", "#B0703A") + ell(86, 54, 24, 8, "#F7E6C8") +
    rect(54, 70, 14, 8, GR, 2, 2) + line("M24 60 H52 M68 70 H104", "#7A4A20", 2) + f(38, 76, d=4, k=0.32) + f(86, 84, d=5, k=0.36))
I["bayder-aikido-novoyasenevsky"] = ("night", "литавры",
    path("M18 50 H110 Q108 98 64 98 Q20 98 18 50Z", "#E2A267") + ell(64, 50, 46, 12, "#F7E6C8") +
    "".join(thick(f"M{x} 92 L{x + d} 116", GR, 3) for x, d in [(36, -8), (64, 0), (92, 8)]) + thick("M100 18 L80 44", WOOD, 3) + circ(80, 44, 5, "#fff", 2) +
    f(64, 72, d=7, k=0.45) + sp((20, 24, 6)))
I["zolotye-vorota-wushu-strogino"] = ("blue", "музыкальная пила со смычком",
    path("M14 92 Q50 70 72 84 Q96 100 118 70 L122 78 Q100 110 70 94 Q46 82 18 102Z", "#D7DCE8") + rect(4, 88, 22, 14, WOOD, 4) +
    "".join(line(f"M{x} {y} l2 4", "#9AA0B8", 1.2) for x, y in [(34, 90), (46, 86), (58, 86), (82, 92), (96, 92), (108, 84)]) +
    thick("M56 24 L96 92", "#C88A50", 3) + line("M60 22 L100 90", "#fff", 1) + txt(30, 46, "♪", 18))
I["zolotye-vorota-wushu-tsaritsyno"] = ("teal", "терменвокс",
    rect(26, 70, 76, 26, BR, 6) + thick("M86 70 V18", "#D7DCE8", 3) + path("M26 80 Q8 80 10 64 Q12 52 26 56", "none", 4).replace(O, "#D7DCE8") +
    rect(30, 96, 8, 16, BR, 2) + rect(90, 96, 8, 16, BR, 2) + f(56, 82, d=6, k=0.42) +
    path("M98 30 Q106 36 98 42 M104 24 Q116 36 104 48", sw=2.2) + sp((20, 26, 6)))
I["gigant-boxing-kids"] = ("orange", "рейнстик",
    f'<g transform="rotate(40 64 64)">' + rect(52, 6, 24, 116, "#C9A070", 10) + rect(50, 4, 28, 12, R, 5) + rect(50, 112, 28, 12, R, 5) +
    "".join(line(f"M54 {y} L74 {y+8}", "#9A7040", 1.6) for y in range(22, 104, 14)) + "</g>" +
    f(64, 64, d=4, k=0.32) + "".join(circ(x, y, 2.4, B, 1) for x, y in [(30, 30), (24, 40), (36, 44), (100, 96), (106, 86)]))

# ===================== Гимнастика, паркур =====================
I["gimnast-moscow-dobrolyubova"] = ("yellow", "доска для игры «Мельница»",
    rect(14, 14, 100, 100, "#F2D6A8", 6) + "".join(rect(14 + k, 14 + k, 100 - 2 * k, 100 - 2 * k, "none", 6 if k == 0 else 0).replace('rx="6"', 'rx="0"')
                                                for k in (10, 26, 42)) +
    line("M64 24 V56 M64 72 V104 M24 64 H56 M72 64 H104", O, 3) +
    "".join(circ(x, y, 6, c, 2) for x, y, c in [(24, 24, DK), (64, 40, "#fff"), (104, 64, DK), (40, 88, "#fff"), (88, 88, DK)]) + f(64, 64, d=4, k=0.3))
I["opolchenets-gym"] = ("orange", "доска для игры манкала (калах)",
    rect(10, 38, 108, 52, BR, 24) + ell(22, 64, 8, 18, "#8E5420", 2) + ell(106, 64, 8, 18, "#8E5420", 2) +
    "".join(circ(x, y, 7, "#8E5420", 2) for x in (40, 56, 72, 88) for y in (52, 76)) +
    "".join(circ(x, y, 2.4, c, 0.8) for x, y, c in [(40, 50, G), (42, 54, B), (56, 76, R), (72, 52, Y), (88, 78, G), (104, 60, P), (24, 66, B)]) +
    f(64, 104, d=6, k=0.42) + sp((112, 24, 6)))
I["flyzone-parkour-slavyansky"] = ("sky", "паркурные перила на блоках",
    rect(8, 82, 40, 34, "#C9CED9", 3) + rect(80, 70, 40, 46, "#C9CED9", 3) + thick("M14 54 H114", "#5A5876", 4) +
    thick("M24 82 V54 M104 70 V54", "#5A5876", 3) + "".join(line(f"M{x} {y} l6 0", "#9AA0B8", 1.6) for x, y in [(16, 92), (30, 104), (90, 82), (100, 100)]) +
    f(64, 92, d=0, k=0, mouth=False, blush=False) + f(100, 90, d=5, k=0.36) + sp((50, 26, 6)))
I["flyzone-parkour-konkovo"] = ("purple", "китайские шашки на звёздной доске",
    path("M64 10 L78 44 L116 44 L86 68 L98 106 L64 84 L30 106 L42 68 L12 44 L50 44Z", "#FFF6C4") +
    "".join(circ(x, y, 4, c, 1.4) for x, y, c in [(64, 24, R), (60, 34, R), (68, 34, R), (100, 50, G), (92, 50, G), (96, 58, G),
                                                   (28, 50, B), (36, 50, B), (32, 58, B), (88, 92, Y), (40, 92, P), (64, 60, "#fff"), (56, 70, "#fff")]) +
    f(64, 64, d=0, k=0, mouth=False, blush=False) + f(64, 72, d=5, k=0.32))
I["nebo-sport-parkour-sokol"] = ("teal", "сёги (японские шахматы)",
    rect(10, 60, 108, 50, "#F2D6A8", 4) + "".join(line(f"M10 {y} H118", "#B08850", 1.4) for y in (72, 84, 96)) +
    "".join(line(f"M{x} 60 V110", "#B08850", 1.4) for x in range(22, 118, 12)) +
    "".join(path(f"M{x} {y-22} L{x+14} {y-14} L{x+12} {y+8} H{x-12} L{x-14} {y-14}Z", "#F7E0B0") for x, y in [(40, 40), (88, 44)]) +
    line("M34 28 H46 M40 26 V44 M33 36 H47 M33 44 H47", O, 2.2) + line("M82 32 H94 M88 30 V48 M82 40 H94 M84 48 H92", O, 2.2) + f(64, 86, d=5, k=0.36))
I["nebo-sport-parkour-oblaka"] = ("blue", "плиобокс (прыжковая тумба)",
    FLOOR + path("M20 56 L44 40 H112 L88 56Z", "#5CB7F2") + rect(20, 56, 68, 52, "#3E8FD0", 2) + path("M88 56 L112 40 V92 L88 108Z", "#2B6FB0") +
    txt(54, 90, "60", 16, "#fff") + f(54, 70, d=6, k=0.42).replace(O, "#fff") + sp((20, 24, 6), (110, 20, 5)))

# ===================== Шахматы =====================
I["chessrussian-gogolevsky"] = ("yellow", "шахматный король",
    rect(30, 98, 68, 14, DK, 5) + path("M42 98 Q46 74 52 60 H76 Q82 74 86 98Z", DK) + ell(64, 58, 22, 7, DK) +
    path("M50 56 Q44 38 64 32 Q84 38 78 56Z", DK) + thick("M64 10 V30 M56 18 H72", GOLD, 4) +
    f(64, 80, d=6, k=0.42).replace(O, "#fff") + sp((108, 30, 6), (20, 40, 5)))
I["detstvo-club-chess"] = ("green", "реверси (отелло)",
    rect(12, 12, 104, 104, "#2E8B4E", 6) + "".join(line(f"M{p} 12 V116 M12 {p} H116", "#1E6B3A", 1.4) for p in range(38, 116, 26)) +
    "".join(circ(x, y, 10, c) for x, y, c in [(51, 51, "#fff"), (77, 51, DK), (51, 77, DK), (77, 77, "#fff"), (25, 25, DK), (103, 103, "#fff")]) +
    f(51, 52, d=3, k=0.24) + f(77, 78, d=3, k=0.24))

if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        bg, subj, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(bg, body))
    print("svg:", len(ids))
