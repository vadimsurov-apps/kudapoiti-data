"""Иконки робота sections (2026-11-05, вечер): 85 новых сюжетов — танец и музыка, лёд, шахматы и логика,
футбол, волейбол, единоборства, плавание, общий спортинвентарь.
Сюжеты сверены с icons-catalog/sheet-01..13.png и icons-src/subjects.txt (не повторяются)."""
import os, sys
from draw_icons import svg, s, eye, face, sparkle, O
W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=9, k=0.75, **kw: face(cx, cy, d=d, k=k, **kw)
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
R, OR, Y, G, B, P, V, BR, WH, GR, DK = ("#E8654F", "#FF9A3D", "#FFD25E", "#7CD26E", "#5CB7F2", "#FF8FB8", "#A98BF0",
                                        "#C0732E", "#FFFFFF", "#B8BCCB", "#2B2A44")
ICEF = f'<path d="M0 98 Q64 88 128 98 V128 H0Z" fill="#E9F7FF" {W(2.6)}/>'
WAVE = f'<path d="M0 100 Q16 92 32 100 T64 100 T96 100 T128 100 V128 H0Z" fill="#7FD3F7" {W(2.6)}/>'
GRASS = f'<path d="M0 100 Q64 90 128 100 V128 H0Z" fill="#8FDB7A" {W(2.6)}/>'
sp = lambda *pts: "".join(sparkle(x, y, r) for x, y, r in pts)
rect = lambda x, y, w, h, c, rx=4, sw=None: f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{c}" {W(sw) if sw else s()}/>'
circ = lambda x, y, r, c, sw=None: f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" {W(sw) if sw else s()}/>'
path = lambda d, c="none", sw=None: f'<path d="{d}" fill="{c}" {W(sw) if sw else s()}/>'


def piece(top, color=WH):
    """шахматная фигура: общее основание + верх"""
    return (path("M36 108 H92 V98 Q92 92 84 92 H44 Q36 92 36 98Z", color) +
            path("M46 92 Q50 70 54 62 H74 Q78 70 82 92Z", color) + rect(48, 56, 32, 8, color, 3) + top)


I = {}
# ===================== TODES — танец и музыка =====================
I["todes-prospekt-mira"] = ("pink", "веер",
    "".join(f'<path d="M64 100 L{64+52*__import__("math").cos(a)} {100-52*__import__("math").sin(a)}" {W(2)}/>' for a in [0.35, 0.75, 1.15, 1.57, 2.0, 2.4, 2.8])
    + path("M64 100 L14 82 A52 52 0 0 1 114 82Z", R) +
    "".join(path(f"M64 100 L{x} {y}", sw=2) for x, y in [(22, 64), (34, 52), (50, 46), (78, 46), (94, 52), (106, 64)]) +
    path("M30 74 Q64 40 98 74", sw=2.4) + circ(64, 100, 6, Y) + f(64, 70, d=8, k=0.5))
I["todes-dubininskaya"] = ("purple", "бальное платье",
    path("M52 18 H76 L80 46 Q108 76 114 110 H14 Q20 76 48 46Z", P) + path("M48 46 H80", sw=2.6) +
    path("M30 90 Q40 84 50 90 T70 90 T90 90 T104 90", sw=2.2) + f(64, 32, d=7, k=0.5) + sp((24, 30, 6), (104, 28, 5)))
I["todes-baumanskaya"] = ("yellow", "балетный станок",
    path("M14 50 H114", sw=7) +
    rect(24, 44, 8, 66, BR, 3) + rect(96, 44, 8, 66, BR, 3) + f'<path d="M14 50 H114" stroke="#E8B06E" stroke-width="4" stroke-linecap="round"/>' +
    rect(18, 106, 20, 6, BR, 2) + rect(90, 106, 20, 6, BR, 2) + f(64, 70, d=9, k=0.6) + sp((64, 24, 7)))
I["todes-skladochnaya"] = ("night", "хлопушка с конфетти",
    path("M30 106 L52 50 L80 70Z", R) + path("M38 86 L64 62 M44 98 L72 72", sw=2.4) +
    "".join(f'<rect x="{x}" y="{y}" width="7" height="7" rx="1.5" fill="{c}" transform="rotate({a} {x} {y})"/>' for x, y, c, a in
            [(76, 40, Y, 20), (92, 54, P, 50), (86, 26, G, 10), (104, 36, B, 70), (64, 30, OR, 30), (100, 70, Y, 15)])
    + f(56, 78, d=6, k=0.42, blush=False) + sp((96, 92, 6)))
I["todes-rusakovskaya"] = ("teal", "гимнастическая лента",
    path("M30 104 L48 64", sw=5) + path("M48 64 Q76 30 96 44 Q114 60 92 76 Q66 92 74 104 Q84 116 104 104", sw=0).replace('stroke="#3B3355"', 'stroke="#E8654F" ') .replace('stroke-width="0"', 'stroke-width="7"')
    + circ(30, 104, 5, Y) + f(80, 56, d=6, k=0.42) + sp((24, 30, 6)))
I["todes-zilart"] = ("orange", "кокошник",
    path("M14 96 Q14 30 64 18 Q114 30 114 96Z", R) + path("M28 92 Q30 44 64 32 Q98 44 100 92Z", Y) +
    "".join(circ(x, y, 4, WH, 2) for x, y in [(64, 26), (40, 40), (88, 40), (26, 62), (102, 62)]) +
    path("M14 96 H114", sw=4) + f(64, 66, d=9, k=0.65))
I["todes-fili-grad"] = ("blue", "танцевальный коврик со стрелками",
    rect(16, 30, 96, 80, "#3E4AA0", 10) + "".join(rect(x, y, 26, 22, c, 5, 2.4) for x, y, c in
        [(51, 36, P), (21, 59, B), (81, 59, G), (51, 82, Y)]) +
    path("M64 40 L58 50 H70Z", WH, 1.6) + path("M64 100 L58 90 H70Z", WH, 1.6) + path("M26 70 L36 64 V76Z", WH, 1.6) + path("M102 70 L92 64 V76Z", WH, 1.6) +
    f(64, 67, d=6, k=0.42, blush=False))
I["todes-vavilova"] = ("green", "пюпитр с нотами",
    path("M64 66 V108 M44 112 L64 104 L84 112", sw=4) + path("M24 26 H104 L96 70 H32Z", WH) +
    "".join(path(f"M34 {y} H94", sw=1.4) for y in (36, 44, 52, 60)) +
    circ(48, 44, 3.5, O, 1) + circ(70, 52, 3.5, O, 1) + path("M51 44 V32 M73 52 V40", sw=1.6) + f(64, 86, d=6, k=0.42))
I["todes-dokukina"] = ("purple", "дирижёрская палочка",
    path("M30 104 L96 26", sw=4) + f'<path d="M30 104 L96 26" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>' +
    rect(22, 92, 18, 22, BR, 6) + path("M100 50 Q110 60 104 74 M86 30 Q100 22 112 30", sw=2.4) + sp((108, 90, 7), (60, 30, 5)) +
    f(54, 84, d=7, k=0.5, blush=False).replace("", ""))
I["todes-ryazansky"] = ("yellow", "музыкальные тарелки",
    path("M64 18 V108", sw=4) + "".join(path(f"M24 {y} Q64 {y-22} 104 {y} Q64 {y-8} 24 {y}Z", "#F2C14E") for y in (50, 84)) +
    circ(64, 38, 5, BR) + f(64, 66, d=8, k=0.5) + sp((20, 26, 6), (108, 104, 5)))
I["todes-megapolis"] = ("night", "гонг",
    path("M18 108 V22 H110 V108", sw=5) + path("M18 22 H110", sw=7) +
    path("M64 22 V34", sw=2) + circ(64, 66, 32, "#F2C14E") + circ(64, 66, 22, "#E8B03E", 2) +
    rect(92, 84, 26, 8, BR, 3) + f(64, 66, d=8, k=0.55))
I["todes-moskovsky"] = ("orange", "туба",
    path("M46 30 L82 30 L74 56 V96 Q74 110 60 110 Q46 110 46 96 V56 L38 30Z", "#F2C14E") +
    f'<ellipse cx="62" cy="28" rx="30" ry="9" fill="#C9902A" {s()}/>' +
    path("M74 64 Q96 64 96 80 Q96 92 80 92 H74", sw=5) + path("M46 70 H30 Q22 70 22 62", sw=4) +
    "".join(circ(x, 76, 4, WH, 2) for x in (52, 60, 68)) + f(60, 92, d=6, k=0.42) + sp((104, 30, 6)))

# ===================== Лёд: фигурное катание и хоккей =====================
I["ilikeice-olimp-arena"] = ("sky", "чехлы для лезвий",
    "".join(path(f"M{x} 40 H{x+44} Q{x+52} 40 {x+52} 52 V62 H{x}Z", c) + path(f"M{x+4} 62 V72 H{x+48} V62", GR, 2.4) for x, c in [(14, R), (62, B)])
    + f(36, 50, d=6, k=0.42) + f(84, 50, d=6, k=0.42) + ICEF + sp((64, 24, 6)))
I["ilikeice-burevestnik"] = ("purple", "доска-спиннер для вращений",
    ICEF + path("M14 82 Q64 60 114 82 Q64 104 14 82Z", Y) + path("M48 82 Q64 74 80 82", sw=2.4) +
    path("M30 58 Q64 38 98 58", sw=2.2) + path("M98 58 l-8 -2 l4 8Z", O) + f(64, 86, d=7, k=0.45, blush=False) + sp((26, 30, 6), (100, 26, 5)))
I["ilikeice-champion-bitsa"] = ("blue", "страховочная лонжа",
    path("M64 10 V40", sw=3) + circ(64, 44, 6, GR) + path("M24 64 Q64 50 104 64 V82 Q64 70 24 82Z", OR) +
    path("M64 50 L40 64 M64 50 L88 64", sw=2.4) + rect(56, 66, 16, 12, GR, 3) + f(64, 96, d=7, k=0.5) + ICEF[:0])
I["ilikeice-kristall"] = ("teal", "ходунки-опора для катания",
    ICEF + path("M24 98 V44 Q24 32 36 32 H92 Q104 32 104 44 V98", sw=6) +
    f'<path d="M24 98 V44 Q24 32 36 32 H92 Q104 32 104 44 V98" fill="none" stroke="{OR}" stroke-width="3" stroke-linecap="round"/>' +
    path("M24 64 H104", sw=5) + f(64, 50, d=7, k=0.45) + path("M18 100 H30 M98 100 H110", sw=4))
I["ilikeice-fili"] = ("pink", "фитнес-резинка",
    path("M22 64 Q22 34 64 34 Q106 34 106 64 Q106 94 64 94 Q22 94 22 64Z", "none", 0).replace('stroke-width="0"', 'stroke-width="18"') +
    f'<path d="M22 64 Q22 34 64 34 Q106 34 106 64 Q106 94 64 94 Q22 94 22 64Z" fill="none" stroke="{V}" stroke-width="12"/>' +
    f(64, 64, d=8, k=0.55) + sp((104, 22, 6), (22, 106, 5)))
I["ilikeice-alyaska"] = ("night", "термос",
    rect(42, 30, 44, 80, "#4FA3E0", 12) + rect(46, 18, 36, 16, GR, 5) + rect(38, 56, 52, 10, WH, 4, 2.4) +
    path("M86 44 Q100 46 100 64 Q100 82 86 84", sw=4) + f(64, 84, d=8, k=0.5) +
    path("M54 12 Q50 4 56 0 M68 12 Q64 4 70 0", sw=2.2) + sp((22, 30, 6), (108, 100, 5)))
I["ilikeice-mitino"] = ("sky", "скрепер для льда",
    ICEF + path("M78 18 L52 82", sw=6) + f'<path d="M78 18 L52 82" stroke="{BR}" stroke-width="3" stroke-linecap="round"/>' +
    path("M26 80 H78 L74 96 H30Z", B) + path("M30 96 H74", sw=3) + f(52, 86, d=7, k=0.42, blush=False) +
    "".join(f'<circle cx="{x}" cy="104" r="2.5" fill="#fff" {W(1.2)}/>' for x in (86, 96, 106)))
I["ilikeice-solntsevo"] = ("blue", "ледозаливочная машина",
    ICEF + rect(18, 46, 88, 44, "#5CCDBA", 10) + rect(66, 30, 34, 22, "#BFE9FF", 6) + path("M66 52 V46", sw=2) +
    circ(38, 92, 10, DK) + circ(88, 92, 10, DK) + circ(38, 92, 4, GR, 1.6) + circ(88, 92, 4, GR, 1.6) +
    rect(8, 82, 14, 12, GR, 3) + f(40, 66, d=7, k=0.5) + sp((30, 28, 5)))
I["ilikeice-champion-gorky"] = ("green", "массажный поролоновый ролик",
    path("M20 60 L96 36 Q110 36 110 52 Q110 68 96 70 L34 92 Q18 92 18 76 Q18 62 20 60Z", OR) +
    "".join(path(f"M{x} {y} l6 20", sw=2) for x, y in [(40, 52), (56, 47), (72, 42), (88, 37)]) +
    f'<ellipse cx="26" cy="76" rx="8" ry="16" fill="{Y}" {s()}/>' + f(66, 62, d=7, k=0.45) + sp((106, 100, 7)))
I["apia-arena"] = ("yellow", "станок для заточки коньков",
    rect(24, 64, 80, 40, GR, 8) + circ(64, 54, 22, "#9AA0B8") + circ(64, 54, 8, DK, 2) +
    "".join(f'<path d="M{x} 36 l-4 -10" stroke="#FF9A3D" stroke-width="3" stroke-linecap="round"/>' for x in (40, 50, 60)) +
    rect(30, 104, 10, 8, DK, 2) + rect(88, 104, 10, 8, DK, 2) + f(64, 84, d=8, k=0.5))
I["molniya-lobnenskaya"] = ("teal", "маска с трубкой",
    path("M18 52 Q18 36 34 36 H94 Q110 36 110 52 V64 Q110 80 94 80 H76 Q64 70 52 80 H34 Q18 80 18 64Z", "#BFE9FF") +
    path("M18 52 H8 M110 52 H120", sw=6) + path("M100 36 V12 Q100 4 108 4", sw=6) +
    f'<path d="M100 36 V12 Q100 4 108 4" stroke="{OR}" stroke-width="3" fill="none"/>' + f(64, 58, d=14, k=0.6) + WAVE)
I["figurist-vao-vympel"] = ("orange", "балансборд",
    circ(64, 92, 14, BR) + path("M14 70 L114 74 L112 84 L12 80Z", Y) + f(64, 76, d=7, k=0.45, blush=False) +
    path("M44 60 L50 70 M84 62 L80 72", sw=2.4) + sp((24, 30, 6), (104, 32, 6)))
I["figurist-vao-gorod-kosino"] = ("purple", "степ-платформа",
    path("M14 84 L34 64 H110 L114 84Z", "#9AA0B8") + path("M14 84 H114 V96 H14Z", B) +
    rect(20, 96, 18, 10, DK, 3) + rect(90, 96, 18, 10, DK, 3) + f(64, 74, d=8, k=0.5) + sp((30, 30, 7), (98, 36, 5)))
I["figurist-vao-sporttekh"] = ("pink", "фитбол",
    circ(64, 62, 42, "#5CCDBA") + f'<ellipse cx="48" cy="40" rx="14" ry="8" fill="#fff" opacity=".45"/>' + rect(98, 60, 10, 8, WH, 2, 2) +
    f'<ellipse cx="64" cy="108" rx="34" ry="6" fill="#000" opacity=".15"/>' + f(64, 62, d=10, k=0.7))

# ===================== Шахматы и логика =====================
I["chess-csbw-tushino"] = ("green", "шахматный конь",
    path("M36 108 H92 V98 Q92 92 84 92 H44 Q36 92 36 98Z", WH) +
    path("M48 92 Q44 70 56 56 Q48 54 40 60 Q32 56 38 46 Q46 30 62 20 L64 12 L72 22 Q94 34 88 92Z", WH) +
    eye(60, 40, 0.7) + path("M46 50 Q50 52 52 50", sw=2) + sp((104, 30, 6)))
I["chess-csbw-altufyevo"] = ("blue", "шахматная ладья",
    path("M36 108 H92 V98 Q92 92 84 92 H44 Q36 92 36 98Z", DK) + path("M46 92 L50 44 H78 L82 92Z", DK) +
    path("M40 44 V24 H52 V32 H60 V24 H68 V32 H76 V24 H88 V44Z", DK) +
    "".join(eye(x, 64, 0.7).replace(O, "#fff").replace('fill="#fff"/>', 'fill="#3B3355"/>', 1) for x in ()) +
    f'<ellipse cx="56" cy="64" rx="3" ry="3.6" fill="#fff"/><ellipse cx="72" cy="64" rx="3" ry="3.6" fill="#fff"/>' +
    f'<path d="M60 74 Q64 78 68 74" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>' + sp((22, 28, 6), (104, 100, 5)))
I["chess-csbw-tsvetnoy"] = ("pink", "шахматный ферзь",
    piece(path("M44 56 L38 28 L52 40 L58 20 L64 38 L70 20 L76 40 L90 28 L84 56Z", WH) +
          "".join(circ(x, y, 3.5, P, 1.6) for x, y in [(38, 26), (58, 18), (70, 18), (90, 26)])) + f(64, 76, d=7, k=0.45))
I["chess-csbw-park-pobedy"] = ("yellow", "шахматная пешка",
    path("M36 108 H92 V98 Q92 92 84 92 H44 Q36 92 36 98Z", WH) + path("M48 92 Q52 72 56 64 H72 Q76 72 80 92Z", WH) +
    rect(46, 58, 36, 8, WH, 3) + circ(64, 40, 18, WH) + f(64, 40, d=7, k=0.5) + sp((100, 26, 7)))
I["chess-csbw-khimki-grushina"] = ("teal", "шахматный слон",
    piece(path("M64 14 Q88 30 82 50 Q76 58 64 58 Q52 58 46 50 Q40 30 64 14Z", DK) + path("M70 26 L60 40", "none", 0).replace('stroke-width="0"', 'stroke-width="3"').replace(O, "#fff") +
          circ(64, 12, 4, DK), DK) +
    f'<ellipse cx="57" cy="76" rx="3" ry="3.6" fill="#fff"/><ellipse cx="71" cy="76" rx="3" ry="3.6" fill="#fff"/>')
I["chess-csbw-khimki-kalinina"] = ("orange", "шахматные часы",
    rect(14, 46, 100, 56, BR, 10) + circ(42, 74, 18, WH) + circ(86, 74, 18, WH) +
    path("M42 74 V62 M86 74 L94 68", sw=2.6) + rect(30, 34, 22, 12, R, 4) + rect(76, 38, 22, 8, GR, 3) +
    f(64, 92, d=6, k=0.4, blush=False))
I["chess-csbw-khimki-levy-bereg"] = ("night", "демонстрационная шахматная доска",
    rect(18, 18, 92, 80, WH, 6) + "".join(f'<rect x="{22+i*11}" y="{22+j*9}" width="11" height="9" fill="#C0732E"/>'
                                         for i in range(8) for j in range(8) if (i + j) % 2) +
    path("M18 18 h92 v80 h-92Z", sw=3) + path("M40 98 L32 120 M88 98 L96 120", sw=4) + f(64, 60, d=10, k=0.6, blush=False).replace(O, "#2B2A44"))
I["mos-chess-donskogo"] = ("sky", "бланк записи партии",
    rect(28, 14, 64, 92, WH, 6) + "".join(path(f"M36 {y} H84", sw=1.4) for y in range(30, 90, 10)) +
    f'<text x="40" y="28" font-family="Arial" font-size="9" fill="#3B3355">e2-e4</text>' +
    path("M88 70 L110 30 L116 34 L94 74 L86 80Z", Y) + f(56, 64, d=7, k=0.45))
I["mos-chess-dubki"] = ("orange", "нарды",
    rect(12, 30, 104, 70, BR, 6) + rect(18, 36, 44, 58, "#F5DEB3", 3, 2) + rect(66, 36, 44, 58, "#F5DEB3", 3, 2) +
    "".join(path(f"M{x} 36 l5 22 l5 -22Z", c, 1.4) for x, c in [(20, R), (32, DK), (44, R), (68, DK), (80, R), (92, DK)]) +
    circ(40, 82, 6, WH, 2) + circ(88, 82, 6, DK, 2) + f(64, 70, d=8, k=0.45, blush=False))
I["mos-chess-yangelya"] = ("green", "шашки",
    "".join(f'<ellipse cx="{x}" cy="{y}" rx="24" ry="9" fill="{c}" {s()}/>' for x, y, c in
            [(44, 96, R), (44, 86, R), (44, 76, R), (86, 96, WH), (86, 86, WH)]) +
    f'<ellipse cx="44" cy="70" rx="24" ry="9" fill="{R}" {s()}/>' + f(44, 88, d=7, k=0.45, blush=False) + f(86, 94, d=7, k=0.4, blush=False) +
    sp((100, 30, 7), (30, 30, 5)))
I["mos-chess-nekrasovka"] = ("purple", "танграм",
    path("M20 20 H108 L64 64Z", R) + path("M20 20 L64 64 L20 108Z", Y) + path("M108 20 V64 L86 42Z", G) +
    path("M64 64 L86 42 L108 64 L86 86Z", B) + path("M20 108 L64 64 L86 86 L64 108Z", OR) +
    path("M64 108 L86 86 L108 108Z", P) + path("M86 86 L108 64 V108Z", V) + f(52, 44, d=6, k=0.42))
I["mos-chess-zhulebino"] = ("yellow", "шахматный столик",
    rect(16, 40, 96, 18, BR, 3) + "".join(f'<rect x="{18+i*12}" y="42" width="12" height="7" fill="{DK if i % 2 else "#F5DEB3"}"/>' for i in range(8)) +
    "".join(f'<rect x="{18+i*12}" y="49" width="12" height="7" fill="{"#F5DEB3" if i % 2 else DK}"/>' for i in range(8)) +
    path("M28 58 L22 108 M100 58 L106 108", sw=5) + path("M30 84 H98", sw=4) + f(64, 76, d=7, k=0.45, blush=False) +
    path("M56 40 V28 Q56 22 62 22 Q68 22 68 28 V40Z", WH, 2.4))
I["mos-chess-konkovo"] = ("blue", "головоломка из колец",
    "".join(f'<circle cx="{x}" cy="64" r="20" fill="none" stroke="{O}" stroke-width="9"/><circle cx="{x}" cy="64" r="20" fill="none" stroke="{c}" stroke-width="5"/>'
            for x, c in [(36, "#C9CED8"), (64, Y), (92, "#C9CED8")]) + f(64, 98, d=7, k=0.5) + sp((64, 22, 6)))
I["mos-chess-pervomayskaya"] = ("night", "игра «Морской бой»",
    rect(20, 20, 88, 88, "#BFE9FF", 6) + "".join(path(f"M{20+i*11} 20 V108", sw=1) + path(f"M20 {20+i*11} H108", sw=1) for i in range(1, 8)) +
    rect(31, 31, 33, 11, DK, 3, 2) + rect(75, 53, 11, 33, DK, 3, 2) + path("M38 70 l8 8 M46 70 l-8 8", sw=3).replace(O, R) +
    f'<path d="M38 70 l8 8 M46 70 l-8 8" stroke="#E8654F" stroke-width="3" stroke-linecap="round"/>' + f(64, 98, d=7, k=0.4, blush=False))
I["mos-chess-simferopolsky"] = ("pink", "крестики-нолики",
    path("M50 18 V110 M78 18 V110 M18 50 H110 M18 78 H110", sw=4) +
    f'<path d="M24 24 l18 18 M42 24 l-18 18 M86 86 l18 18 M104 86 l-18 18" stroke="{B}" stroke-width="6" stroke-linecap="round"/>' +
    circ(64, 64, 9, "none", 5).replace(f'stroke="{O}"', f'stroke="{R}"') + circ(95, 33, 9, "none", 5).replace(f'stroke="{O}"', f'stroke="{R}"') +
    f(33, 95, d=5, k=0.38, blush=False))
I["mos-chess-partizanskaya"] = ("teal", "судоку",
    rect(18, 18, 92, 92, WH, 6) + "".join(path(f"M{18+i*30.7:.0f} 18 V110 M18 {18+i*30.7:.0f} H110", sw=2.6) for i in (1, 2)) +
    "".join(f'<text x="{x}" y="{y}" font-family="Arial" font-weight="bold" font-size="16" fill="{c}">{t}</text>' for x, y, t, c in
            [(28, 40, 5, O), (90, 40, 3, O), (58, 102, 7, O), (88, 100, 1, B), (28, 98, 9, B)]) + f(64, 64, d=7, k=0.5))
I["mos-chess-cheryomushki"] = ("yellow", "игра «Пятнашки»",
    rect(16, 16, 96, 96, BR, 8) + "".join(rect(22 + (k % 4) * 22, 22 + (k // 4) * 22, 19, 19, "#F5DEB3", 3, 1.8) +
                                         f'<text x="{31+(k%4)*22}" y="{37+(k//4)*22}" font-family="Arial" font-size="10" text-anchor="middle" fill="#3B3355">{k+1}</text>'
                                         for k in range(15)) + f(97, 97, d=4, k=0.32, blush=False))
I["mos-chess-rabochaya"] = ("green", "карточки «Мемори»",
    "".join(rect(x, y, 30, 40, c, 5) for x, y, c in [(18, 24, B), (50, 24, WH), (82, 24, B), (18, 70, WH), (50, 70, B), (82, 70, B)]) +
    path("M57 38 l8 -6 l8 6 l-8 12Z", R, 1.6) + circ(33, 90, 7, Y, 1.6) + f(65, 46, d=4, k=0.3, blush=False))
I["chess-labyrinth-krylatskoe"] = ("orange", "доска для игры го с камнями",
    rect(16, 16, 96, 96, "#F2C46E", 6) + "".join(path(f"M{24+i*10} 24 V104 M24 {24+i*10} H104", sw=1) for i in range(9)) +
    "".join(circ(x, y, 4.6, c, 1.4) for x, y, c in [(44, 44, DK), (54, 44, WH), (54, 54, DK), (64, 54, WH), (74, 64, DK), (44, 74, WH), (84, 34, DK)]) +
    f(64, 90, d=7, k=0.45, blush=False))

# ===================== Хоккей и катки спортшкол =====================
I["ms-snezhnye-barsy"] = ("night", "вратарская хоккейная маска",
    path("M30 50 Q30 14 64 14 Q98 14 98 50 Q98 92 64 110 Q30 92 30 50Z", WH) +
    "".join(path(f"M{x} 54 V100", sw=2) for x in (52, 64, 76)) + path("M40 62 H88 M42 78 H86", sw=2) +
    path("M42 30 Q64 20 86 30", sw=0).replace('stroke-width="0"', 'stroke-width="5"').replace(O, B) + f(64, 42, d=11, k=0.6, blush=False))
I["ms-sozvezdie"] = ("blue", "хоккейные краги",
    path("M30 108 V56 Q30 46 40 46 H52 V30 Q52 22 58 22 Q64 22 64 30 V46 H70 V34 Q70 28 76 28 Q82 28 82 34 V50 Q96 50 96 64 V108Z", R) +
    path("M30 88 H96", sw=2.6) + rect(30, 92, 66, 16, WH, 3, 2.4) + f(64, 70, d=8, k=0.5))
I["ms-lds-tsentralny"] = ("sky", "хоккейный шлем с решёткой",
    path("M24 70 Q24 22 66 22 Q104 22 104 66 V78 H24Z", B) + path("M36 66 H100 V104 Q80 112 56 104 Q40 96 36 82Z", "none", 0) +
    "".join(path(f"M{x} 68 V104", sw=2) for x in (48, 60, 72, 84, 96)) + path("M36 76 H102 M38 90 H102", sw=2) +
    path("M36 66 H104", sw=3) + f(66, 44, d=9, k=0.55))
I["ms-ld-medvedkovo"] = ("orange", "щитки хоккейного вратаря",
    "".join(rect(x, 18, 30, 92, WH, 10) + path(f"M{x} 46 H{x+30} M{x} 74 H{x+30}", sw=2.4) + rect(x+4, 100, 22, 8, R, 3, 2) for x in (24, 74))
    + f(39, 34, d=5, k=0.38, blush=False) + f(89, 34, d=5, k=0.38, blush=False))
I["ms-lc-maryino"] = ("night", "лампа гола",
    rect(54, 74, 20, 36, GR, 4) + path("M38 74 Q38 28 64 28 Q90 28 90 74Z", R) +
    "".join(path(f"M{x} {y} l{dx} {dy}", sw=3).replace(O, Y) for x, y, dx, dy in [(64, 20, 0, -12), (36, 34, -10, -8), (92, 34, 10, -8), (28, 58, -14, 0), (100, 58, 14, 0)]) +
    "".join(f'<path d="M{x} {y} l{dx} {dy}" stroke="#FFD25E" stroke-width="4" stroke-linecap="round"/>' for x, y, dx, dy in [(64, 20, 0, -12), (36, 34, -10, -8), (92, 34, 10, -8), (28, 58, -14, 0), (100, 58, 14, 0)]) +
    f(64, 56, d=8, k=0.55))
I["ms-lc-pingviny"] = ("teal", "рулон тейпа для клюшки",
    circ(64, 64, 40, DK) + circ(64, 64, 20, WH) + path("M98 84 L118 112 L104 116 L90 90Z", DK) +
    f(64, 64, d=7, k=0.45, blush=False) + sp((22, 24, 6)))
I["ms-lc-sinyaya-ptitsa"] = ("green", "налокотник",
    path("M40 20 Q20 20 20 46 V82 Q20 108 46 108 H62 Q72 108 72 96 V40 Q72 20 52 20Z", "#3E7FC8") +
    path("M20 60 Q46 50 72 60", sw=2.4) + rect(72, 36, 26, 14, GR, 4) + rect(72, 80, 26, 14, GR, 4) + f(44, 82, d=7, k=0.45))
I["ms-krasny-mayak"] = ("pink", "хоккейный нагрудник-панцирь",
    path("M20 30 Q30 18 46 22 Q64 30 82 22 Q98 18 108 30 L112 64 Q96 70 92 62 V104 H36 V62 Q32 70 16 64Z", DK) +
    path("M36 50 Q64 60 92 50 M36 74 H92", sw=0).replace('stroke-width="0"', 'stroke-width="2.4"').replace(O, "#fff") +
    f'<path d="M36 50 Q64 60 92 50 M36 74 H92" fill="none" stroke="#fff" stroke-width="2.4"/>' + f(64, 88, d=8, k=0.5))
I["ms-sk-serebryany"] = ("yellow", "пневматический горн болельщика",
    rect(22, 54, 30, 44, R, 8) + rect(28, 44, 18, 12, GR, 3) + path("M52 66 L104 40 V96 L52 82Z", "#F2C14E") +
    path("M110 48 Q118 60 112 72 M114 40 Q126 60 116 82", sw=2.4) + f(37, 76, d=6, k=0.42))
I["ms-tutberidze-center"] = ("purple", "спортивная олимпийка",
    path("M44 20 L22 32 L12 82 L28 86 L34 60 V108 H94 V60 L100 86 L116 82 L106 32 L84 20 Q64 30 44 20Z", R) +
    path("M64 28 V108", sw=2.6) + path("M22 32 L12 82 M106 32 L116 82", sw=0).replace('stroke-width="0"', 'stroke-width="5"').replace(O, "#fff") +
    path("M44 20 Q64 34 84 20", WH, 2.4) + circ(64, 40, 2.5, GR, 1) + f(80, 70, d=6, k=0.42))
I["ms-ld-mechta"] = ("sky", "канат для лазания",
    path("M14 14 H114", sw=6) + path("M64 14 V112", sw=0).replace('stroke-width="0"', 'stroke-width="12"') +
    f'<path d="M64 14 V112" stroke="#E8B06E" stroke-width="8"/>' +
    "".join(path(f"M58 {y} L70 {y+6}", sw=1.6) for y in range(22, 108, 9)) + circ(64, 112, 7, "#E8B06E") +
    f(86, 60, d=6, k=0.42) + sp((30, 50, 6), (36, 92, 5)))
I["ms-ld-khrustalny"] = ("green", "шведская стенка",
    rect(22, 14, 10, 100, BR, 3) + rect(96, 14, 10, 100, BR, 3) +
    "".join(path(f"M32 {y} H96", sw=0).replace('stroke-width="0"', 'stroke-width="6"') + f'<path d="M32 {y} H96" stroke="#E8B06E" stroke-width="3"/>' for y in range(24, 112, 13)) +
    f(64, 64, d=8, k=0.5, blush=False))
I["ms-sk-vdokhnovenie"] = ("orange", "медбол с ручками",
    path("M30 40 Q30 20 46 22 M98 40 Q98 20 82 22", sw=7) + circ(64, 70, 38, "#4A4A5E") +
    path("M32 56 Q64 66 96 56", sw=0).replace('stroke-width="0"', 'stroke-width="2"') +
    f'<path d="M28 76 H100" stroke="{Y}" stroke-width="6"/>' + f(64, 60, d=9, k=0.6).replace("#3B3355", "#2B2A44") +
    f'<text x="64" y="102" font-family="Arial" font-weight="bold" font-size="12" text-anchor="middle" fill="#fff">3 кг</text>')
I["ms-yantar"] = ("blue", "штанга",
    path("M8 64 H120", sw=6) + "".join(rect(x, y, w, h, c, 4) for x, y, w, h, c in
        [(16, 34, 12, 60, R), (28, 42, 10, 44, R), (90, 42, 10, 44, R), (100, 34, 12, 60, R)]) + f(64, 84, d=8, k=0.5) + sp((64, 30, 7)))

# ===================== Футбол =====================
I["ms-arena-sokol"] = ("yellow", "вувузела",
    path("M14 82 L90 40 L112 30 L118 54 L96 54 L20 92Z", "#F7E04B") +
    path("M40 70 L44 78 M60 58 L64 68 M80 48 L84 56", sw=2.2) + f(72, 58, d=6, k=0.42) + sp((30, 30, 6), (100, 100, 6)))
I["ms-avtomobilist"] = ("green", "поролоновая рука болельщика",
    path("M42 112 V72 L34 66 Q30 60 36 56 L48 62 V24 Q48 14 58 14 Q68 14 68 24 V52 H82 Q94 52 94 64 V112Z", B) +
    path("M68 56 V40 M80 52 V44", sw=2.4) + f'<text x="68" y="100" font-family="Arial" font-weight="bold" font-size="18" text-anchor="middle" fill="#fff">№1</text>' +
    f(68, 74, d=7, k=0.45))
I["ms-stadion-kosino"] = ("sky", "манекен-стенка для штрафных",
    GRASS + "".join(path(f"M{x} 100 V44 Q{x} 32 {x+11} 32 Q{x+22} 32 {x+22} 44 V100Z", c) + f(x + 11, 52, d=4, k=0.32, blush=False)
                    for x, c in [(14, Y), (42, B), (70, Y), (98, B)]) + path("M14 100 H120", sw=4))
I["ms-stadion-tushino"] = ("teal", "газонокосилка",
    GRASS + rect(22, 62, 64, 30, R, 8) + path("M86 66 L112 24 H122", sw=5) + circ(34, 96, 10, DK) + circ(76, 96, 10, DK) +
    rect(36, 52, 30, 12, GR, 4) + f(54, 78, d=7, k=0.45))
I["ms-olimp-suzdalskaya"] = ("orange", "тележка для разметки поля",
    GRASS + path("M10 112 H118", sw=0).replace('stroke-width="0"', 'stroke-width="5"').replace(O, "#fff") +
    rect(30, 56, 50, 36, "#F5F5F5", 8) + path("M80 64 L108 28 H118", sw=5) + circ(40, 96, 9, DK) + circ(72, 96, 9, DK) +
    f'<path d="M50 104 H64" stroke="#fff" stroke-width="6"/>' + f(55, 74, d=7, k=0.45))
I["ms-medvedkovo-arena"] = ("pink", "аптечка",
    rect(18, 40, 92, 64, WH, 10) + rect(48, 28, 32, 14, GR, 5) + path("M56 56 H72 V64 H80 V80 H72 V88 H56 V80 H48 V64 H56Z", R, 2.4) +
    f(64, 94, d=6, k=0.4, blush=False) + sp((104, 24, 6)))
I["ms-fk-rodina"] = ("blue", "тренировочная манишка",
    path("M42 16 Q64 34 86 16 L96 24 V108 H32 V24Z", "#C6F04B") + path("M42 16 Q64 34 86 16", sw=2.6) +
    path("M32 50 Q22 50 22 60 V40 M96 50 Q106 50 106 60", sw=0).replace('stroke-width="0"', 'stroke-width="0"') +
    "".join(f'<path d="M{x} 40 V100" stroke="#fff" stroke-width="2" stroke-dasharray="3 5"/>' for x in (44, 84)) + f(64, 64, d=8, k=0.5))
I["ms-fsh-chertanovo"] = ("green", "мяч для регби",
    f'<ellipse cx="64" cy="64" rx="48" ry="30" fill="{BR}" {s()} transform="rotate(-25 64 64)"/>' +
    path("M40 70 L88 48", sw=2.6) + "".join(path(f"M{x} {y} l6 10", sw=2.2) for x, y in [(50, 60), (60, 56), (70, 51), (80, 46)]) +
    f(58, 76, d=7, k=0.45) + sp((104, 100, 6)))
I["ms-arena-chertanovo"] = ("yellow", "доска с расписанием тренировок",
    rect(16, 18, 96, 72, "#E8B06E", 6) + rect(24, 26, 34, 24, WH, 2, 2) + rect(66, 26, 38, 30, "#BFE9FF", 2, 2) + rect(26, 58, 36, 24, "#FFDCEB", 2, 2) +
    "".join(circ(x, y, 3, R, 1.4) for x, y in [(41, 26), (85, 26), (44, 58)]) + path("M40 90 L34 116 M88 90 L94 116", sw=5) + f(86, 70, d=6, k=0.4))
I["ms-borisovskie-prudy-fc"] = ("teal", "рулон газона",
    path("M14 92 L72 92 L72 104 L14 104Z", "#8FDB7A") + circ(88, 80, 26, "#8FDB7A") + circ(88, 80, 16, "#A0662E") + circ(88, 80, 8, "#8FDB7A", 2) +
    "".join(path(f"M{x} 92 l2 -8 l2 8", sw=1.6) for x in range(18, 70, 8)) + f(40, 70, d=7, k=0.45) + sp((30, 30, 6)))

# ===================== Волейбол, гандбол =====================
I["ms-volley-leningradka"] = ("sky", "волейбольный мяч",
    circ(64, 62, 40, WH) + path("M64 22 Q48 52 64 102 M28 46 Q64 54 102 78 M30 84 Q60 66 96 34", sw=2.6) +
    path("M64 22 Q48 52 64 102", sw=0).replace('stroke-width="0"', 'stroke-width="0"') +
    f'<path d="M30 52 Q48 40 66 26" fill="none" stroke="{Y}" stroke-width="6" opacity=".7"/><path d="M70 98 Q92 86 100 68" fill="none" stroke="{B}" stroke-width="6" opacity=".7"/>' +
    f(64, 62, d=8, k=0.5))
I["ms-volley-proletarka"] = ("orange", "волейбольная сетка",
    rect(14, 18, 6, 96, GR, 2) + rect(108, 18, 6, 96, GR, 2) + rect(20, 30, 88, 34, "none", 1, 2.4) +
    "".join(path(f"M{x} 30 V64", sw=1.4) for x in range(28, 108, 8)) + "".join(path(f"M20 {y} H108", sw=1.4) for y in (38, 46, 54)) +
    path("M20 30 H108", sw=0).replace('stroke-width="0"', 'stroke-width="5"').replace(O, "#fff") + f(64, 88, d=8, k=0.5))
I["ms-volley-yasny"] = ("purple", "наколенники",
    "".join(rect(x, 26, 36, 76, "#3E4AA0", 14) + f'<ellipse cx="{x+18}" cy="64" rx="13" ry="16" fill="#6C7BE0" {W(2.4)}/>' for x in (18, 74))
    + f(36, 64, d=5, k=0.38, blush=False) + f(92, 64, d=5, k=0.38, blush=False) + sp((64, 20, 6)))
I["ms-volley-kozhukhovsky"] = ("teal", "спортивные часы",
    rect(50, 10, 28, 108, DK, 10) + rect(38, 36, 52, 56, "#3E4AA0", 14) + rect(44, 42, 40, 44, "#BFE9FF", 10, 2) +
    f'<text x="64" y="58" font-family="Arial" font-weight="bold" font-size="11" text-anchor="middle" fill="#3B3355">12:30</text>' +
    f(64, 70, d=6, k=0.4, blush=False))
I["ms-handball-academy"] = ("yellow", "стартовый номер",
    rect(18, 30, 92, 68, WH, 6) + rect(18, 30, 92, 14, R, 6) +
    f'<text x="64" y="86" font-family="Arial" font-weight="bold" font-size="34" text-anchor="middle" fill="#3B3355">27</text>' +
    "".join(circ(x, y, 3.5, GR, 1.4) for x, y in [(26, 52), (102, 52), (26, 90), (102, 90)]) + sp((104, 18, 6)))

# ===================== Единоборства, гимнастика =====================
I["ms-sambo70-gimnast"] = ("pink", "боксёрская лапа",
    f'<ellipse cx="60" cy="58" rx="36" ry="42" fill="{R}" {s()}/><ellipse cx="60" cy="58" rx="18" ry="22" fill="#fff" {W(2.4)}/>' +
    circ(60, 58, 8, R, 2) + rect(88, 80, 26, 16, DK, 5) + f(60, 34, d=6, k=0.42, blush=False))
I["ms-sambo70-yasenevo"] = ("blue", "боксёрские бинты",
    path("M20 40 Q20 24 36 24 H72 Q88 24 88 40 Q88 56 72 56 H36", R) + circ(36, 40, 14, R) + circ(36, 40, 6, "#B04A3A", 2) +
    path("M72 56 Q104 60 108 88 Q110 108 88 108 H44", "none", 0).replace('stroke-width="0"', 'stroke-width="14"') +
    f'<path d="M72 56 Q104 60 108 88 Q110 108 88 108 H44" fill="none" stroke="{R}" stroke-width="9"/>' + f(62, 40, d=7, k=0.45))
I["ms-sambo70-champion"] = ("yellow", "нунчаки",
    rect(18, 20, 18, 56, BR, 8) + rect(82, 52, 18, 56, BR, 8) + path("M27 76 Q30 100 54 98 Q76 96 82 76", sw=2.6) +
    "".join(path(f"M18 {y} H36", sw=1.6) for y in (32, 64)) + "".join(path(f"M82 {y} H100", sw=1.6) for y in (64, 96)) +
    f(27, 48, d=4, k=0.32, blush=False) + f(91, 80, d=4, k=0.32, blush=False))
I["ms-sambo70-shabolovka"] = ("green", "деревянный меч боккэн",
    path("M24 108 L98 22 Q104 16 108 22 Q110 26 104 32 L32 114Z", "#E8B06E") + path("M36 92 L46 102", sw=6) +
    path("M20 110 L32 98", sw=0).replace('stroke-width="0"', 'stroke-width="8"') + f(74, 56, d=5, k=0.38, blush=False) + sp((30, 30, 7), (100, 96, 5)))
I["ms-yarygin-wrestling"] = ("purple", "борцовское трико",
    path("M44 16 L50 36 Q64 46 78 36 L84 16 L96 20 L90 60 V104 H76 L64 82 L52 104 H38 V60 L32 20Z", R) +
    path("M38 60 H90", sw=2.4) + f'<path d="M50 20 V36 M78 20 V36" stroke="#fff" stroke-width="3"/>' + f(64, 64, d=7, k=0.45))
I["ms-borets-solntsevo"] = ("sky", "боксёрская капа",
    path("M18 56 Q18 30 64 30 Q110 30 110 56 Q110 86 64 92 Q18 86 18 56Z", B) +
    path("M32 56 Q64 40 96 56 Q64 72 32 56Z", WH) + "".join(path(f"M{x} 50 V60", sw=1.4) for x in range(44, 88, 8)) +
    f(64, 76, d=8, k=0.5) + sp((104, 24, 6)))
I["ms-viner-gymnastics"] = ("pink", "булавы для художественной гимнастики",
    "".join(f'<g transform="rotate({a} 64 64)">' + path("M60 18 Q56 18 56 26 L58 48 Q48 70 54 96 Q58 106 64 106 Q70 106 74 96 Q80 70 70 48 L72 26 Q72 18 68 18Z", c) +
            circ(64, 16, 6, c) + "</g>" for a, c in [(-18, V), (18, P)]) + f(64, 84, d=6, k=0.42))

# ===================== Бассейны «Юг» =====================
I["ms-pool-shipilovsky"] = ("blue", "колобашка для плавания",
    path("M28 30 Q64 20 100 30 Q108 48 96 64 Q108 80 100 98 Q64 108 28 98 Q20 80 32 64 Q20 48 28 30Z", Y) +
    path("M32 64 H96", sw=2.6) + f(64, 46, d=8, k=0.5) + WAVE)
I["ms-pool-yuzhny"] = ("teal", "кольца для ныряния",
    WAVE + "".join(f'<ellipse cx="{x}" cy="{y}" rx="16" ry="7" fill="none" stroke="{O}" stroke-width="9"/><ellipse cx="{x}" cy="{y}" rx="16" ry="7" fill="none" stroke="{c}" stroke-width="5"/>'
                   for x, y, c in [(36, 112, R), (64, 116, Y), (94, 110, G)]) +
    circ(64, 46, 22, "#FFD9B8") + f(64, 46, d=7, k=0.45) + path("M42 40 Q64 18 86 40", "#3E7FC8") + sp((106, 30, 6)))
I["ms-pool-moskvorechye"] = ("sky", "лопатки для плавания",
    "".join(path(f"M{x} 30 Q{x+20} 22 {x+40} 30 V88 Q{x+20} 104 {x} 88Z", c) + path(f"M{x+12} 48 H{x+28} M{x+12} 62 H{x+28}", sw=2.4)
            for x, c in [(14, OR), (74, B)]) + f(34, 76, d=5, k=0.38) + f(94, 76, d=5, k=0.38))
I["ms-pool-yerevanskaya"] = ("night", "водолазный шлем",
    circ(64, 58, 40, "#E8B06E") + circ(64, 56, 20, "#BFE9FF") + "".join(circ(x, y, 3, GR, 1.4) for x, y in [(36, 36), (92, 36), (32, 70), (96, 70)]) +
    circ(26, 52, 9, "#BFE9FF") + circ(102, 52, 9, "#BFE9FF") + rect(36, 96, 56, 16, "#9AA0B8", 5) + f(64, 58, d=7, k=0.45) +
    "".join(circ(x, y, r, "none", 2).replace(f'stroke="{O}"', 'stroke="#fff"') for x, y, r in [(108, 20, 5), (116, 36, 3)]))

if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        bg, subj, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(bg, body))
    print("svg:", len(ids))
