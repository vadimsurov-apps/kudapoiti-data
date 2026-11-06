"""Иконки робота sections (2026-11-06, ночь): 74 новых сюжета — музыка и танец, единоборства и тренажёры,
гимнастика, игровые виды спорта. Сюжеты сверены с icons-catalog/sheet-01..15.png и icons-src/subjects.txt."""
import os, sys, math
from draw_icons import svg, s, eye, face, sparkle, O
W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=9, k=0.75, **kw: face(cx, cy, d=d, k=k, **kw)
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
R, OR, Y, G, B, P, V, BR, WH, GR, DK = ("#E8654F", "#FF9A3D", "#FFD25E", "#7CD26E", "#5CB7F2", "#FF8FB8", "#A98BF0",
                                        "#C0732E", "#FFFFFF", "#B8BCCB", "#2B2A44")
GOLD, WOOD, SKIN, LB = "#F2C14E", "#E8B06E", "#FFD9B8", "#BFE9FF"
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
    """линия с контуром: тёмная подложка + цвет"""
    return line(d, O, w + 3.2) + line(d, c, w)


I = {}
# ===================== Балет и танцы: BALLETA, ГрандБалет =====================
I["balleta-ovchinnikovsky"] = ("pink", "бальные туфли на каблуке",
    "".join(path(f"M{x} 62 Q{x+4} 92 {x+30} 92 H{x+44} Q{x+50} 92 {x+50} 86 Q{x+50} 78 {x+40} 76 L{x+22} 66 Q{x+12} 56 {x} 62Z", c) +
            path(f"M{x+2} 66 L{x+4} 104 H{x+10} L{x+12} 80", c) + path(f"M{x+14} 70 Q{x+22} 60 {x+30} 72", sw=2.4)
            for x, c in [(14, GOLD), (62, R)]) + f(96, 82, d=5, k=0.38) + f(48, 82, d=5, k=0.38) + sp((30, 30, 7), (100, 34, 5)))
I["balleta-borisovsky"] = ("night", "цилиндр с тростью",
    ell(60, 88, 40, 10, DK) + rect(34, 30, 52, 58, DK, 4) + rect(34, 70, 52, 9, R, 1, 2.4) +
    thick("M104 22 V110", WH, 4) + path("M104 22 Q104 12 94 12 Q86 12 86 20", sw=4) +
    f'<ellipse cx="51" cy="50" rx="3" ry="3.6" fill="#fff"/><ellipse cx="69" cy="50" rx="3" ry="3.6" fill="#fff"/>' +
    line("M55 58 Q60 62 65 58", WH, 2.2) + sp((20, 30, 6), (112, 104, 5)))
I["balleta-krasnogorsk"] = ("green", "флейта Пана",
    "".join(rect(18 + i * 13, 24, 12, 80 - i * 9, WOOD, 4, 2.4) for i in range(7)) +
    rect(14, 52, 96, 10, BR, 3) + f(52, 76, d=8, k=0.55) + sp((104, 100, 7), (100, 28, 5)))
I["grandballet-smolenskaya"] = ("purple", "орган с трубами",
    rect(16, 74, 96, 38, BR, 6) + rect(24, 82, 80, 8, WH, 2, 2) +
    "".join(f'<rect x="{x}" y="{y}" width="11" height="{80-y}" rx="5" fill="#D7DCE8" {W(2.4)}/>' for x, y in
            [(22, 40), (36, 30), (50, 18), (67, 18), (81, 30), (95, 40)]) +
    "".join(line(f"M{x+3} {y+10} h5", O, 2) for x, y in [(22, 40), (36, 30), (50, 18), (67, 18), (81, 30), (95, 40)]) +
    "".join(line(f"M{x} 82 V90", O, 1.4) for x in range(32, 104, 8)) + f(64, 100, d=7, k=0.45, blush=False))
I["grandballet-shabolovka"] = ("yellow", "валторна",
    f'<circle cx="58" cy="62" r="32" fill="none" stroke="{O}" stroke-width="11"/><circle cx="58" cy="62" r="32" fill="none" stroke="{GOLD}" stroke-width="7"/>' +
    f'<circle cx="58" cy="62" r="18" fill="none" stroke="{O}" stroke-width="9"/><circle cx="58" cy="62" r="18" fill="none" stroke="{GOLD}" stroke-width="5"/>' +
    path("M84 44 L112 22 Q120 38 108 52Z", GOLD) + rect(46, 56, 24, 12, GOLD, 3, 2.4) +
    "".join(circ(x, 52, 3.4, WH, 1.6) for x in (50, 58, 66)) + f(58, 90, d=6, k=0.42) + sp((22, 24, 6)))

# ===================== «Гармония» — инструменты =====================
I["harmony-ballet-kapitoliy"] = ("orange", "тромбон",
    path("M24 40 H90 Q104 40 104 54 Q104 68 90 68 H40", sw=0).replace('stroke-width="0"', 'stroke-width="9"') +
    line("M24 40 H90 Q104 40 104 54 Q104 68 90 68 H40", GOLD, 5) + thick("M40 68 H60", GOLD, 5) +
    path("M24 40 L8 26 V58Z", GOLD) + thick("M70 40 V68 M80 40 V68", GOLD, 3) + rect(60, 74, 8, 18, GR, 3, 2) +
    f(52, 90, d=6, k=0.42) + sp((112, 100, 7)))
I["harmony-ballet-profsoyuznaya"] = ("teal", "банджо",
    thick("M70 52 L108 14", WOOD, 7) + rect(100, 8, 16, 12, BR, 3, 2.4) +
    circ(52, 74, 34, "#E3E6EE") + circ(52, 74, 26, WH, 2.4) + "".join(line(f"M{40+i*5} {54+i*2} L{92-i*4} {22+i*2}", O, 1) for i in range(0)) +
    line("M40 60 L96 16 M44 64 L100 20 M48 68 L104 24", "#9AA0B8", 1.4) + rect(42, 86, 20, 6, BR, 2, 2) + f(52, 74, d=7, k=0.5))
I["harmony-ballet-stoletova"] = ("pink", "калимба",
    path("M22 30 Q64 20 106 30 L100 108 Q64 116 28 108Z", WOOD) + circ(64, 84, 9, BR) +
    "".join(rect(28 + i * 9, 26 + abs(i - 4) * 5, 6, 46 - abs(i - 4) * 5, "#D7DCE8", 2, 1.8) for i in range(9)) +
    rect(26, 60, 76, 7, BR, 2, 2) + f(64, 96, d=7, k=0.42, blush=False).replace("", "") + sp((112, 24, 6)))
I["harmony-ballet-vinnitskaya"] = ("blue", "варган",
    path("M64 18 Q96 18 96 50 Q96 70 72 80 L72 112 H56 L56 80 Q32 70 32 50 Q32 18 64 18Z", "#D7DCE8") +
    path("M64 30 Q84 30 84 50 Q84 62 64 66 Q44 62 44 50 Q44 30 64 30Z", "#9AD8F5") +
    thick("M64 40 V118", R, 3) + f(64, 50, d=7, k=0.45) + sp((22, 30, 6), (106, 98, 5)))
I["harmony-ballet-leninsky"] = ("yellow", "трещотка",
    thick("M24 20 V108 M104 20 V108", R, 3) +
    "".join(rect(20, 22 + k * 12, 88, 9, WOOD if k % 2 else "#F4C27A", 3, 2.2) for k in range(8)) +
    rect(14, 12, 14, 12, R, 4, 2) + rect(100, 12, 14, 12, R, 4, 2) + f(64, 64, d=8, k=0.5) + sp((116, 110, 5)))
I["harmony-ballet-michurinsky"] = ("purple", "кахон",
    path("M30 22 H92 L100 110 H22Z", WOOD) + path("M92 22 L106 30 L112 104 L100 110", BR) +
    circ(61, 52, 9, DK) + path("M30 22 H92", sw=4) + f(61, 82, d=9, k=0.6) + sp((112, 18, 5)))
I["harmony-ballet-bolotnikovskaya"] = ("sky", "музыка ветра",
    path("M24 22 H104", sw=5) + thick("M24 22 H104", BR, 3) +
    "".join(line(f"M{x} 22 V{y-24}", O, 1.6) + rect(x - 4, y - 24, 8, 30 + (x % 3) * 6, "#D7DCE8", 3, 2) for x, y in
            [(34, 52), (50, 64), (64, 72), (78, 64), (94, 52)]) +
    line("M64 22 V96", O, 1.4) + circ(64, 100, 6, R, 2.4) + f(64, 54, d=4, k=0.3, blush=False) + sp((20, 90, 6), (110, 96, 5)))
I["harmony-ballet-vargi"] = ("night", "хэндпан",
    ell(64, 70, 50, 26, "#9AA0B8") + ell(64, 62, 46, 20, "#C9CED8", 2.4) + ell(64, 58, 10, 6, "#9AA0B8", 2.4) +
    "".join(ell(x, y, 8, 4.5, "#9AA0B8", 2) for x, y in [(34, 60), (94, 60), (46, 72), (82, 72), (64, 76)]) +
    f(64, 92, d=8, k=0.5, blush=False).replace(O, "#3B3355") + sp((20, 30, 6), (110, 28, 7)))
I["harmony-ballet-ushakova"] = ("green", "мелодика",
    rect(20, 50, 88, 34, B, 8) + "".join(rect(26 + i * 8, 56, 7, 22, WH, 1.5, 1.4) for i in range(10)) +
    "".join(rect(30 + i * 8, 56, 4, 12, DK, 1, 1) for i in (0, 1, 3, 4, 5, 7, 8)) +
    path("M20 66 Q6 66 8 48 Q10 30 28 26 H40", sw=4) + line("M20 66 Q6 66 8 48 Q10 30 28 26 H40", WH, 2) +
    rect(40, 20, 12, 10, Y, 3, 2) + f(64, 98, d=7, k=0.45))

# ===================== «Высота» — звук =====================
I["vysota-ballroom-yablochkova"] = ("orange", "бумбокс",
    path("M36 36 Q36 18 64 18 Q92 18 92 36", sw=5) + rect(12, 36, 104, 60, R, 10) +
    circ(36, 70, 16, DK) + circ(92, 70, 16, DK) + circ(36, 70, 7, GR, 2) + circ(92, 70, 7, GR, 2) +
    rect(52, 46, 24, 14, LB, 3, 2) + "".join(rect(54 + i * 7, 64, 5, 5, WH, 1, 1.4) for i in range(3)) +
    f(64, 82, d=5, k=0.36, blush=False) + sp((112, 22, 6)))
I["vysota-ballroom-timiryazevskaya"] = ("purple", "DJ-пульт",
    rect(10, 52, 108, 52, DK, 10) + circ(38, 76, 20, "#4A4A66") + circ(38, 76, 8, R, 2) + circ(90, 76, 20, "#4A4A66") + circ(90, 76, 8, B, 2) +
    rect(60, 60, 8, 34, GR, 2, 1.6) + rect(58, 70, 12, 6, Y, 2, 1.6) + path("M38 56 L50 70", sw=2.4).replace(O, "#fff") +
    f(64, 40, d=0, k=0) .replace("", "") + "".join(circ(x, 40, 4, c, 1.6) for x, c in [(30, G), (46, Y), (82, P), (98, B)]) +
    f'<ellipse cx="57" cy="40" rx="3" ry="3.6" fill="{O}"/><ellipse cx="71" cy="40" rx="3" ry="3.6" fill="{O}"/>' +
    path("M59 46 Q64 50 69 46", sw=2.2))
I["vysota-ballroom-tatyanin-park"] = ("sky", "компакт-диск",
    circ(64, 62, 44, "#E8EEF8") + f'<path d="M64 62 L100 34 A44 44 0 0 1 106 74Z" fill="{P}" opacity=".55"/>' +
    f'<path d="M64 62 L22 80 A44 44 0 0 1 28 38Z" fill="{B}" opacity=".5"/>' + circ(64, 62, 44, "none") +
    circ(64, 62, 13, WH, 2.4) + circ(64, 62, 5, "#C9D7F0", 2) + f(64, 90, d=8, k=0.5) + sp((110, 106, 6)))
I["vysota-ballroom-vavilova"] = ("yellow", "ретро-радиоприёмник",
    rect(14, 34, 100, 72, BR, 14) + rect(22, 44, 50, 52, "#F5DEB3", 8, 2.4) +
    "".join(line(f"M28 {y} H66", BR, 2) for y in range(52, 92, 7)) + rect(80, 46, 26, 16, LB, 3, 2) + line("M86 54 H100", R, 2) +
    circ(86, 80, 6, Y) + circ(100, 80, 6, Y) + path("M40 34 L28 14", sw=2.4) + circ(28, 12, 3, R, 1.6) +
    f(47, 70, d=7, k=0.45))
I["vysota-ballroom-korolev-gelios"] = ("blue", "барабанные палочки",
    "".join(f'<g transform="rotate({a} 64 64)">' + thick("M64 14 V112", WOOD, 6) + ell(64, 14, 4, 6, "#F4C27A") + "</g>" for a in (-30, 30)) +
    f(64, 72, d=6, k=0.42) + sp((22, 94, 7), (106, 94, 6), (64, 22, 5)))
I["vysota-ballroom-korolev-kalinina"] = ("pink", "медиатор",
    path("M64 108 Q22 70 24 44 Q26 20 64 20 Q102 20 104 44 Q106 70 64 108Z", V) +
    f'<path d="M40 38 Q50 28 64 28" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".6"/>' +
    f(64, 56, d=10, k=0.7) + sp((22, 100, 6), (108, 98, 7)))

# ===================== Energy — танец и праздник =====================
I["energy-dance-otradnoe"] = ("purple", "помпоны черлидинга",
    "".join("".join(line(f"M{cx} {cy} L{cx+26*math.cos(a):.1f} {cy+26*math.sin(a):.1f}", c, 4) for a in [k * 0.45 for k in range(14)])
            + circ(cx, cy, 8, c) for cx, cy, c in [(42, 56, R), (86, 56, Y)]) +
    rect(36, 80, 12, 22, GR, 4, 2.4) + rect(80, 80, 12, 22, GR, 4, 2.4) + f(42, 56, d=3, k=0.28, blush=False) + f(86, 56, d=3, k=0.28, blush=False))
I["energy-dance-dezhneva"] = ("teal", "гавайская юбка",
    rect(30, 34, 68, 12, P, 6) + "".join(path(f"M{x} 44 Q{x-2} 80 {x+2} 110 L{x+8} 110 Q{x+8} 78 {x+8} 44Z", "#8FDB7A", 1.8) for x in range(32, 98, 8)) +
    "".join(circ(x, 40, 5, c, 1.8) for x, c in [(38, Y), (52, WH), (66, OR), (80, WH), (92, Y)]) + f(64, 70, d=8, k=0.5) + sp((18, 24, 6)))
I["energy-dance-kompas"] = ("orange", "пояс с монетками",
    path("M12 50 Q64 76 116 50 L114 64 Q64 90 14 64Z", R) +
    "".join(circ(16 + i * 8, 66 + 10 * math.sin(i / 12 * math.pi) + 6, 4.5, GOLD, 1.6) for i in range(13)) +
    "".join(circ(22 + i * 8, 80 + 10 * math.sin(i / 11 * math.pi), 4, GOLD, 1.4) for i in range(11)) +
    f(64, 66, d=7, k=0.45, blush=False) + sp((26, 28, 7), (104, 30, 5)))
I["energy-dance-green-park"] = ("yellow", "сомбреро",
    ell(64, 84, 56, 16, R) + path("M40 82 Q40 34 64 30 Q88 34 88 82Z", OR) +
    path("M40 70 Q64 78 88 70", sw=3) + "".join(circ(x, 92, 3, Y, 1.4) for x in range(20, 112, 12)) + f(64, 56, d=7, k=0.45))

# ===================== Данко и «Ритм» — костюмы и инструменты =====================
I["danco-break-sokolniki"] = ("green", "волынка",
    path("M30 70 Q24 40 52 38 Q86 36 90 64 Q92 90 62 94 Q34 96 30 70Z", "#E06C9A") +
    path("M34 66 L90 50 M38 80 L92 66", sw=2) +
    thick("M50 40 L40 12 M66 38 L66 6 M82 44 L98 14", BR, 5) + thick("M62 94 L72 118", BR, 5) +
    f(60, 70, d=8, k=0.5) + sp((108, 100, 6)))
I["danco-break-pyataya-avenu"] = ("blue", "кабаса",
    thick("M64 74 V116", BR, 8) + ell(64, 52, 30, 26, "#D7DCE8") +
    "".join(circ(40 + (i % 7) * 8, 34 + (i // 7) * 9, 2.6, GOLD, 1.2) for i in range(35)) + f(64, 52, d=7, k=0.45, blush=False))
I["danco-break-mira"] = ("night", "тюбетейка",
    path("M18 90 L28 50 Q64 38 100 50 L110 90Z", G) + path("M28 50 Q64 38 100 50 Q64 62 28 50Z", "#5FB850") + path("M18 90 H110 V100 H18Z", DK) +
    "".join(path(f"M{x} 86 Q{x+6} 70 {x+12} 86", WH, 1.6) for x in (28, 46, 64, 82)) +
    path("M64 46 V54", sw=1.8) + f(64, 70, d=8, k=0.45, blush=False) + sp((20, 24, 6), (108, 26, 5)))
I["ritm-dance-arena-plaza"] = ("pink", "русский сарафан",
    path("M48 18 H80 L82 42 Q108 76 112 112 H16 Q20 76 46 42Z", R) + path("M48 18 L46 42 M80 18 L82 42", sw=2) +
    path("M18 96 H110", sw=0).replace('stroke-width="0"', 'stroke-width="2"') +
    "".join(circ(x, 104, 3.5, Y, 1.4) for x in range(26, 106, 10)) + "".join(circ(64, y, 3, GOLD, 1.4) for y in (50, 62, 74)) +
    f(64, 30, d=6, k=0.42))
I["ritm-dance-tbilisi"] = ("sky", "косоворотка",
    path("M44 18 L30 26 L10 60 L26 70 L36 52 V110 H92 V52 L102 70 L118 60 L98 26 L84 18 Q64 30 44 18Z", WH) +
    path("M58 22 V60", sw=2.4) + "".join(circ(58, y, 2.4, R, 1.2) for y in (30, 40, 50)) +
    path("M36 92 H92", sw=0).replace('stroke-width="0"', 'stroke-width="2"') + line("M36 96 H92", R, 4) +
    line("M48 20 Q58 24 58 24", R, 3) + f(72, 72, d=7, k=0.45))
I["ritm-dance-shchuka"] = ("yellow", "лапти",
    "".join(path(f"M{x} 70 Q{x} 54 {x+18} 52 Q{x+44} 52 {x+50} 76 Q{x+50} 90 {x+30} 90 H{x+12} Q{x} 90 {x} 70Z", WOOD) +
            "".join(line(f"M{x+6+k*7} 56 L{x+12+k*7} 88", BR, 1.6) for k in range(6)) for x in (8, 66)) +
    path("M20 54 Q22 30 40 24 M78 54 Q80 30 98 24", sw=2.4) + f(34, 74, d=5, k=0.38) + f(92, 74, d=5, k=0.38))

# ===================== «Школа чемпионов», Sambi.st — единоборства и ОФП =====================
I["school-champions-skandinavia"] = ("orange", "макивара",
    rect(56, 20, 16, 92, WOOD, 4) + rect(52, 30, 24, 30, "#E3E6EE", 4) + "".join(line(f"M54 {y} H74", O, 1.8) for y in (38, 46, 54)) +
    FLOOR + f(64, 76, d=4, k=0.34) + sp((26, 34, 7), (104, 40, 6)))
I["school-champions-skandinavia-yug"] = ("blue", "защитный жилет хогу",
    path("M38 18 Q64 32 90 18 L104 38 V106 Q64 118 24 106 V38Z", B) + path("M38 18 Q64 46 90 18", sw=2.4) +
    circ(64, 70, 18, R) + circ(64, 70, 9, WH, 2) + path("M24 60 Q64 52 104 60", sw=2) + f(64, 96, d=7, k=0.42))
I["school-champions-litvina-sedogo"] = ("yellow", "чемпионский пояс",
    path("M6 60 Q64 46 122 60 L122 82 Q64 70 6 82Z", DK) + ell(64, 66, 28, 24, GOLD) + ell(64, 66, 18, 15, "#FFE28A", 2.4) +
    rect(26, 58, 10, 18, GOLD, 3, 2) + rect(92, 58, 10, 18, GOLD, 3, 2) + f(64, 64, d=6, k=0.42) + sp((24, 30, 7), (104, 28, 6)))
I["school-champions-lyublinsky-park"] = ("green", "доска для разбивания",
    rect(10, 86, 30, 18, GR, 3) + rect(88, 86, 30, 18, GR, 3) +
    path("M24 60 H60 L56 74 L64 84 H24Z", WOOD) + path("M68 50 H104 V84 H70 L76 72Z", WOOD) +
    "".join(line(f"M28 {y} H54", BR, 1.4) for y in (66, 76)) + "".join(line(f"M78 {y} H100", BR, 1.4) for y in (60, 72)) +
    f(86, 66, d=5, k=0.36, blush=False) + sp((64, 30, 9), (40, 34, 4), (92, 30, 4)))
I["school-champions-sreda"] = ("night", "хакама",
    path("M36 22 H92 L110 108 H72 L64 64 L56 108 H18Z", "#3B4A8A") + rect(32, 18, 64, 12, "#5566B0", 4) +
    "".join(line(f"M{x} 34 L{x-8+ (x-64)/4:.0f} 104", "#2B3366", 2) for x in (44, 56, 72, 84)) +
    path("M64 30 V64", sw=2) + f(64, 46, d=7, k=0.42, blush=False).replace(O, "#fff").replace('fill="#fff"/>', f'fill="{O}"/>'))
I["school-champions-butovo-park"] = ("pink", "утяжелители на ноги",
    "".join(f'<g transform="rotate({a} {cx} 66)">' + rect(cx - 16, 30, 32, 72, c, 12) + "".join(line(f"M{cx-16} {y} H{cx+16}", O, 2) for y in (50, 66, 82)) +
            rect(cx - 20, 58, 40, 14, GR, 4, 2.2) + "</g>" for cx, a, c in [(42, -12, OR), (86, 12, V)]) +
    f(42, 42, d=4, k=0.32, blush=False) + f(86, 42, d=4, k=0.32, blush=False) + sp((64, 108, 6)))
I["sambist-bauman"] = ("teal", "подвесные петли",
    path("M10 14 H118", sw=6) + thick("M50 14 L40 74 M78 14 L88 74", Y, 4) +
    rect(28, 74, 24, 10, DK, 4) + rect(76, 74, 24, 10, DK, 4) + path("M40 74 V68 M88 74 V68", sw=2) +
    f(64, 48, d=6, k=0.42) + sp((20, 104, 7), (108, 104, 5)))
I["sambist-podolsk"] = ("purple", "пояс штангиста",
    path("M10 56 Q64 34 118 56 L118 88 Q64 66 10 88Z", BR) + rect(52, 44, 26, 30, "#D7DCE8", 4) + rect(58, 50, 14, 18, "none", 2, 2.4) +
    "".join(circ(x, 72 - (x - 64) ** 2 / 300, 2.2, GOLD, 1) for x in (22, 32, 92, 102, 110)) + f(36, 66, d=5, k=0.38, blush=False) + sp((104, 26, 6)))

# ===================== «Мицудэн», «Кайдзен» =====================
I["mitsuden-basmannaya"] = ("orange", "деревянный манекен для ушу",
    rect(50, 18, 28, 92, WOOD, 12) + thick("M50 46 L24 36 M78 46 L104 36", BR, 6) + thick("M64 76 L64 76 M78 80 L100 92", BR, 6) +
    rect(44, 108, 40, 8, BR, 3) + f(64, 32, d=6, k=0.42) + sp((24, 90, 7), (108, 20, 5)))
I["mitsuden-chertanovskaya"] = ("sky", "сай",
    "".join(f'<g transform="rotate({a} 64 64)">' + path("M60 12 L64 6 L68 12 V78 H60Z", "#D7DCE8") +
            path("M60 74 Q46 72 46 58 M68 74 Q82 72 82 58", sw=4) + rect(58, 78, 12, 30, R, 4) + circ(64, 112, 5, GOLD) + "</g>" for a in (-24, 24)) +
    f(64, 90, d=5, k=0.36, blush=False))
I["mitsuden-pereyaslavskaya"] = ("green", "тонфа",
    thick("M22 76 L108 50", WOOD, 9) + thick("M44 70 L36 44", WOOD, 8) + circ(36, 42, 6, BR) +
    f(74, 62, d=5, k=0.38, blush=False) + sp((24, 26, 7), (102, 96, 6)))
I["mitsuden-glinisty"] = ("blue", "фехтовальная шпага",
    thick("M30 98 L112 16", "#D7DCE8", 3) + ell(34, 94, 16, 6, GOLD).replace("/>", ' transform="rotate(-45 34 94)"/>') +
    thick("M16 112 L28 100", DK, 6) + circ(14, 114, 4, GOLD) + f(70, 82, d=0, k=0) .replace("", "") +
    f(80, 84, d=6, k=0.42) + sp((40, 28, 7), (100, 100, 5)))
I["mitsuden-kaspiyskaya"] = ("yellow", "полусфера BOSU",
    path("M14 90 Q14 38 64 38 Q114 38 114 90Z", B) + rect(10, 88, 108, 10, DK, 4) +
    path("M30 58 Q64 44 98 58", sw=2).replace(O, "#fff") + f(64, 68, d=9, k=0.6) + sp((24, 26, 6), (106, 24, 7)))
I["mitsuden-donskaya"] = ("pink", "коврик для йоги",
    path("M14 92 H90", sw=0).replace('stroke-width="0"', 'stroke-width="0"') + rect(10, 84, 82, 16, V, 6) +
    circ(96, 74, 24, V) + circ(96, 74, 14, "#C9B5FA", 2.4) + circ(96, 74, 5, V, 2) + f(50, 92, d=5, k=0.36, blush=False) + sp((28, 36, 7), (60, 26, 5)))
I["kaizen-leskova"] = ("teal", "ролик для пресса",
    circ(64, 70, 26, R) + circ(64, 70, 10, GR, 2.4) + thick("M14 70 H114", "#9AA0B8", 5) +
    rect(6, 62, 16, 16, DK, 6) + rect(106, 62, 16, 16, DK, 6) + f(64, 46, d=0, k=0).replace("", "") +
    f'<ellipse cx="58" cy="60" rx="0" ry="0"/>' + f(64, 98, d=6, k=0.4) + sp((30, 30, 6), (98, 30, 7)))
I["kaizen-mira"] = ("purple", "массажный мячик-ёжик",
    "".join(path(f"M{64+28*math.cos(a):.1f} {66+28*math.sin(a):.1f} L{64+38*math.cos(a+0.1):.1f} {66+38*math.sin(a+0.1):.1f} L{64+28*math.cos(a+0.24):.1f} {66+28*math.sin(a+0.24):.1f}Z", "#7CD26E", 2)
            for a in [k * 0.42 for k in range(15)]) + circ(64, 66, 30, G) + f(64, 66, d=8, k=0.55))
I["kaizen-bolotnikovskaya"] = ("night", "беговая дорожка",
    path("M14 92 L92 76 L104 84 L28 102Z", DK) + path("M18 92 L92 78", "none", 2).replace(O, "#888") +
    thick("M92 76 L98 30", GR, 5) + rect(84, 20, 30, 16, B, 4) + rect(90, 24, 16, 6, LB, 2, 1.4) +
    circ(22, 98, 6, GR) + circ(100, 84, 6, GR) + f(56, 92, d=6, k=0.36, blush=False).replace(O, "#3B3355") + sp((24, 30, 6), (54, 46, 5)))
I["soyuz-sport-volgina"] = ("sky", "гребной тренажёр",
    thick("M16 96 L112 96", "#9AA0B8", 6) + circ(26, 82, 16, DK) + circ(26, 82, 7, GR, 2) + rect(66, 84, 26, 8, R, 3) +
    thick("M26 82 L60 60", O, 1.6) + thick("M54 62 H68", Y, 5) + rect(94, 78, 12, 12, DK, 3) + thick("M16 96 V108 M112 96 V108", "#9AA0B8", 4) +
    f(79, 66, d=5, k=0.38) .replace("", "") + sp((90, 30, 7), (50, 26, 5)))
I["delosport-boxing"] = ("orange", "табурет в углу ринга",
    thick("M106 16 V112", R, 8) + thick("M10 40 H106 M10 62 H106 M10 84 H106", WH, 3) +
    ell(54, 80, 26, 8, BR) + thick("M36 82 L30 112 M72 82 L78 112 M54 86 V112", BR, 4) +
    path("M100 34 Q86 40 90 60 L100 56Z", WH) + f(54, 72, d=0, k=0).replace("", "") + f(54, 98, d=5, k=0.36, blush=False) + sp((24, 22, 6)))
I["tkd-otradnoe"] = ("green", "надувная арка старта",
    GRASS + path("M14 104 V54 Q14 14 64 14 Q114 14 114 54 V104 H96 V56 Q96 32 64 32 Q32 32 32 56 V104Z", R) +
    rect(36, 38, 56, 16, WH, 4, 2.4) + txt(64, 51, "СТАРТ", 11) + f(64, 76, d=7, k=0.45) + sp((22, 24, 5)))

# ===================== Гимнастика Перевозникова =====================
I["perevoznikov-gym-izmaylovo"] = ("pink", "гимнастическое бревно",
    rect(8, 48, 112, 14, "#F4C27A", 7) + thick("M30 62 L22 104 M98 62 L106 104", "#9AA0B8", 5) + thick("M14 104 H34 M94 104 H114", DK, 5) +
    f(64, 80, d=7, k=0.45) + sp((30, 30, 7), (100, 26, 5)))
I["perevoznikov-gym-kosino"] = ("blue", "параллельные брусья",
    thick("M10 46 H118", WOOD, 6) + thick("M10 62 H118", WOOD, 6) +
    thick("M22 46 V104 M106 46 V104 M30 62 V104 M98 62 V104", "#9AA0B8", 4) + thick("M14 106 H38 M90 106 H114", DK, 5) +
    f(64, 84, d=7, k=0.45) + sp((64, 24, 7)))
I["perevoznikov-gym-yurlovsky"] = ("yellow", "мешочек магнезии",
    path("M30 46 Q24 104 64 108 Q104 104 98 46Z", "#F3F3F7") + path("M30 46 Q64 36 98 46 Q64 56 30 46Z", WH) +
    path("M40 42 Q46 22 64 22 Q82 22 88 42", sw=2.4) +
    "".join(circ(x, y, r, WH, 1.4) for x, y, r in [(46, 30, 4), (60, 18, 3), (80, 26, 5), (70, 12, 2.4)]) + f(64, 76, d=9, k=0.6))
I["perevoznikov-gym-solntsevo"] = ("teal", "акробатическая дорожка",
    path("M4 96 L110 66 L124 72 L18 104Z", B) + path("M4 96 L18 104 V112 L4 104Z", "#3E7FC8") + path("M18 104 L124 72 V80 L18 112Z", "#3E7FC8") +
    "".join(line(f"M{4+k*20} {96-k*5.7:.0f} L{18+k*20} {104-k*6:.0f}", WH, 1.6) for k in range(1, 6)) +
    path("M38 74 Q64 30 92 56", sw=2.4) + path("M92 56 l-9 -1 l5 8Z", O) + f(60, 92, d=6, k=0.38, blush=False) + sp((26, 30, 6)))
I["perevoznikov-gym-shcherbinka"] = ("orange", "гимнастический мостик",
    path("M12 96 L112 70 V84 L12 104Z", R) + path("M12 104 L112 84 V96 H12Z", "#B84A38") +
    "".join(f'<path d="M{x} {y} q4 -6 8 0 q4 6 8 0" fill="none" stroke="{GR}" stroke-width="3"/>' for x, y in [(30, 104), (70, 96)]) +
    f(70, 86, d=6, k=0.38, blush=False) + sp((30, 40, 7), (96, 36, 6)))
I["perevoznikov-gym-mgsu"] = ("purple", "накладки на ладони",
    "".join(path(f"M{x} 26 H{x+32} V60 Q{x+32} 82 {x+16} 86 Q{x} 82 {x} 60Z", WOOD) + circ(x + 9, 32, 3, WH, 1.4) + circ(x + 23, 32, 3, WH, 1.4) +
            rect(x - 2, 86, 36, 12, R, 4) for x in (16, 80)) + f(32, 60, d=5, k=0.38) + f(96, 60, d=5, k=0.38))
I["perevoznikov-gym-yasenevo"] = ("green", "стартовые колодки",
    thick("M10 96 H118", "#9AA0B8", 5) + path("M30 96 L42 70 L52 70 L46 96Z", R) + path("M70 96 L84 62 L94 62 L86 96Z", R) +
    line("M8 108 H120", WH, 3) + f(84, 82, d=4, k=0.32, blush=False) + sp((26, 34, 7), (104, 30, 6)))
I["perevoznikov-gym-balashikha"] = ("night", "шарф болельщика",
    path("M40 20 Q64 34 88 20 L96 30 Q64 50 32 30Z", R) +
    path("M40 30 L30 112 H50 L58 40Z", R) + path("M88 30 L80 102 H100 L96 30Z", R) +
    "".join(rect(32 + k * 2, 56 + k * 18, 18, 8, WH, 1, 1.4) for k in range(3)) + "".join(rect(82, 52 + k * 18, 16, 8, WH, 1, 1.4) for k in range(3)) +
    "".join(line(f"M{x} 112 V122", R, 3) for x in (34, 40, 46)) + "".join(line(f"M{x} 102 V112", R, 3) for x in (84, 90, 96)) +
    f(64, 34, d=5, k=0.32, blush=False) + sp((112, 30, 6), (18, 40, 5)))
I["perevoznikov-gym-mytishchi"] = ("yellow", "городки",
    GRASS + "".join(f'<rect x="{x}" y="{y}" width="12" height="28" rx="3" fill="{WOOD}" {s()} transform="rotate({a} {x+6} {y+14})"/>' for x, y, a in
                    [(54, 66, 0), (34, 76, 90), (72, 76, 90), (50, 86, 90)]) +
    thick("M20 30 L66 52", WOOD, 7) + thick("M10 26 L22 30", BR, 6) + f(64, 78, d=4, k=0.3, blush=False) + sp((104, 30, 7)))

# ===================== Art-Gym, GymBalance =====================
I["art-gym-stromynka"] = ("sky", "шары для петанка",
    GRASS + circ(42, 82, 18, "#B8BCCB") + circ(84, 84, 18, "#B8BCCB") + circ(64, 104, 6, R) +
    "".join(line(f"M{x-14} {y} Q{x} {y-8} {x+14} {y}", "#7A7F92", 2) for x, y in [(42, 82), (84, 84)]) +
    f(42, 80, d=5, k=0.38) + f(84, 82, d=5, k=0.38) + sp((30, 30, 6), (100, 34, 6)))
I["art-gym-neptun"] = ("blue", "аэрохоккей",
    path("M20 40 H108 L118 104 H10Z", "#E9F7FF") + path("M64 40 V104", sw=2).replace(O, R) + ell(64, 72, 14, 9, "none", 2) +
    rect(54, 36, 20, 6, R, 2, 1.6) + rect(52, 100, 24, 6, R, 2, 1.6) + ell(44, 62, 10, 6, B) + ell(44, 58, 5, 3, B, 2) +
    ell(84, 86, 10, 6, R) + ell(84, 82, 5, 3, R, 2) + ell(64, 72, 6, 3.5, DK, 2) + f(64, 54, d=0, k=0).replace("", "") +
    f(86, 66, d=4, k=0.3, blush=False))
I["art-gym-volgina"] = ("orange", "настольный футбол",
    rect(12, 38, 104, 64, G, 8) + rect(12, 58, 6, 24, WH, 1, 1.6) + rect(110, 58, 6, 24, WH, 1, 1.6) + path("M64 38 V102", sw=1.8).replace(O, "#fff") +
    "".join(line(f"M{x} 26 V114", "#9AA0B8", 4) + "".join(rect(x - 5, y, 10, 14, c, 3, 1.8) for y in (48, 76)) for x, c in [(36, R), (56, B), (76, R), (96, B)]) +
    circ(66, 70, 4, WH, 1.6) + f(56, 55, d=2, k=0.24, blush=False))
I["gymbalance-lugovoy"] = ("teal", "щётка для кёрлинга",
    ICEF + thick("M84 16 L52 86", DK, 5) + rect(24, 84, 52, 14, R, 6) + "".join(line(f"M{x} 98 V104", O, 2) for x in range(30, 74, 6)) +
    f(50, 90, d=6, k=0.38, blush=False).replace(O, "#3B3355") + sp((28, 30, 6), (102, 52, 7)))
I["gymbalance-andropova"] = ("pink", "гимнастические чешки",
    "".join(path(f"M{x} 70 Q{x} 46 {x+20} 44 Q{x+46} 44 {x+50} 72 Q{x+50} 90 {x+26} 92 Q{x} 92 {x} 70Z", "#FFE1CC") +
            path(f"M{x+10} 58 L{x+40} 82 M{x+40} 56 L{x+10} 84", sw=0).replace('stroke-width="0"', 'stroke-width="5"') +
            line(f"M{x+10} 58 L{x+40} 82 M{x+40} 56 L{x+10} 84", P, 2.4) for x in (8, 68)) +
    f(33, 72, d=5, k=0.36, blush=False) + f(93, 72, d=5, k=0.36, blush=False) + sp((64, 26, 7)))
I["gymbalance-khachaturyana"] = ("blue", "аквагантели",
    WAVE + thick("M44 64 H84", GR, 6) + "".join(f'<g transform="translate({x} 64)">' + path("M-14 -20 Q4 -20 4 0 Q4 20 -14 20 Q-20 0 -14 -20Z" if x < 64 else "M14 -20 Q-4 -20 -4 0 Q-4 20 14 20 Q20 0 14 -20Z", Y) + "</g>" for x in (40, 88)) +
    f(64, 82, d=0, k=0).replace("", "") + f(64, 48, d=6, k=0.42) + sp((24, 26, 6), (108, 26, 5)))
I["gymbalance-dmitrovskoe"] = ("purple", "мешок для сменки",
    path("M28 40 Q22 112 64 112 Q106 112 100 40Z", G) + path("M28 40 Q64 50 100 40", sw=2.4) +
    thick("M30 42 L18 110 M98 42 L110 110", WH, 2) + path("M30 40 Q44 22 52 40 M76 40 Q84 22 98 40", sw=2.4) +
    path("M50 74 L56 84 L76 64", sw=3).replace(O, "#fff") + f(64, 94, d=7, k=0.42) + sp((112, 24, 6)))

# ===================== RusVolley, теннис, бадминтон =====================
I["rusvolley-marksistskaya"] = ("orange", "баскетбольное кольцо со щитом",
    rect(22, 14, 84, 58, WH, 6) + rect(46, 34, 36, 26, "none", 2, 2.6).replace(O, R) +
    thick("M40 66 H88", OR, 4) + "".join(line(f"M{x} 68 L{x+ (64-x)/4:.0f} 98", WH, 2) for x in (42, 52, 64, 76, 86)) +
    line("M44 80 H84 M48 90 H80", WH, 2) + f(64, 34, d=0, k=0).replace("", "") + f(64, 46, d=6, k=0.38, blush=False) + thick("M64 14 V4", GR, 4))
I["rusvolley-novodmitrovskaya"] = ("night", "баскетбольный мяч",
    circ(64, 64, 42, OR) + path("M22 64 H106 M64 22 V106", sw=2.4) + path("M34 34 Q52 64 34 94 M94 34 Q76 64 94 94", sw=2.4) +
    f(64, 64, d=10, k=0.6, blush=False).replace("", "") + sp((20, 20, 6), (110, 110, 5)))
I["rusvolley-garibaldi"] = ("green", "бейсбольная перчатка",
    path("M30 104 Q14 70 22 46 Q26 34 36 38 L40 24 Q46 14 54 22 L58 18 Q66 12 72 22 L78 22 Q88 20 88 34 L94 58 Q110 50 114 62 Q114 84 90 104Z", BR) +
    path("M44 40 V72 M60 30 V68 M76 32 V68", sw=1.8) + circ(98, 34, 13, WH) + path("M90 26 Q96 34 90 42 M106 26 Q100 34 106 42", sw=1.6).replace(O, R) +
    f(60, 86, d=7, k=0.42))
I["rusvolley-ordzhonikidze"] = ("blue", "бейсбольная бита с мячом",
    thick("M24 106 L96 22", "#F4C27A", 14) + thick("M24 106 L40 88", DK, 8) + circ(20, 110, 6, DK) +
    circ(92, 92, 14, WH) + path("M84 84 Q92 92 84 100 M100 84 Q92 92 100 100", sw=1.6).replace(O, R) + f(66, 56, d=5, k=0.36, blush=False))
I["rusvolley-strogino-beach"] = ("yellow", "теннисный стол",
    path("M10 62 L46 42 H118 L86 64Z", "#3E7FC8") + path("M10 62 L86 64 V70 L10 68Z", "#2B5A99") +
    line("M28 52 H100", WH, 1.6) + path("M48 63 L84 43 V36 L48 56Z", "#E9F7FF", 1.8) +
    thick("M18 68 V104 M80 70 V104 M110 62 V96", "#9AA0B8", 4) + circ(66, 30, 5, WH, 2) + f(70, 82, d=6, k=0.4))
I["playpark-tennis"] = ("teal", "машина для подачи мячей",
    rect(24, 50, 80, 50, "#5CCDBA", 10) + path("M24 50 L36 30 H92 L104 50Z", "#BFF0E4") + circ(40, 104, 9, DK) + circ(88, 104, 9, DK) +
    rect(96, 60, 22, 16, GR, 5) + "".join(circ(x, y, 5, "#E8F56A", 1.6) for x, y in [(50, 36), (62, 34), (74, 36), (86, 38), (56, 28)]) +
    circ(118, 44, 5, "#E8F56A", 1.6) + f(60, 74, d=8, k=0.5))
I["legion-tennis"] = ("pink", "тубус с теннисными мячами",
    rect(40, 14, 48, 98, "#E9F7FF", 14) + rect(38, 10, 52, 10, R, 4) +
    "".join(circ(64, y, 18, "#E8F56A") + path(f"M48 {y-6} Q64 {y+4} 80 {y-6}", sw=1.6).replace(O, "#fff") for y in (38, 74)) +
    rect(40, 92, 48, 16, R, 4, 2) + f(64, 74, d=6, k=0.42) + sp((22, 28, 6), (106, 100, 5)))
I["delosport-badminton"] = ("sky", "чехол для ракеток",
    path("M64 14 Q104 14 104 54 Q104 82 76 90 V112 H52 V90 Q24 82 24 54 Q24 14 64 14Z", R) +
    path("M64 24 Q94 24 94 54 Q94 74 64 78 Q34 74 34 54 Q34 24 64 24Z", "#C94A3A", 2.4) + path("M30 40 Q64 30 98 40", sw=2.4).replace(O, Y) +
    thick("M100 36 Q118 60 100 96", DK, 3) + f(64, 54, d=8, k=0.5))

if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        bg, subj, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(bg, body))
    print("svg:", len(ids))
