"""Иконки робота sections (2026-11-06, вечер), метод «Якорь + Характер + Шутка».
Теннис: A — ракетка со струнами-персонаж, B — теннисный мяч-персонаж, C — ребёнок с ракеткой, D — сетка.
Плавание MURENA: якорь — вода/бассейн, персонаж — мурена (название школы) в плавательной шапочке; шутка по бассейну.
Сюжеты сверены с листами icons-catalog/sheet-01..20.png и icons-src/subjects.txt.
Запуск: python3 tools/icons_sections_1106d.py [id ...]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import svg, s, eye, face, sparkle, O

W = lambda w: s(f'stroke-width="{w}"')
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
R, OR, Y, G, B, P, V, WH, GR, DK = ("#E8654F", "#FF9A3D", "#FFD25E", "#7CD26E", "#5CB7F2", "#FF8FB8", "#A98BF0",
                                    "#FFFFFF", "#B8BCCB", "#2B2A44")
GOLD, SKIN, TB = "#F2C14E", "#FFD9B8", "#D7F25A"
rect = lambda x, y, w, h, c, rx=4, sw=2.6: f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{c}" {W(sw)}/>'
circ = lambda x, y, r, c, sw=2.6: f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" {W(sw)}/>'
ell = lambda x, y, rx, ry, c, sw=2.6: f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{c}" {W(sw)}/>'
path = lambda d, c="none", sw=3.2: f'<path d="{d}" fill="{c}" {W(sw)}/>'
line = lambda d, c, w: f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
txt = lambda x, y, t, size=12, c=O: f'<text x="{x}" y="{y}" font-family="Arial" font-weight="bold" font-size="{size}" text-anchor="middle" fill="{c}">{t}</text>'
sp = lambda *pts: "".join(sparkle(x, y, r) for x, y, r in pts)
WATER = f'<path d="M0 98 Q16 90 32 98 T64 98 T96 98 T128 98 V128 H0Z" fill="#7FD3F7" {W(2.6)}/>'
WAVES = line("M10 112 Q20 106 30 112 M90 116 Q100 110 110 116", "#fff", 2.6)


def rot(body, a, cx, cy):
    return f'<g transform="rotate({a} {cx} {cy})">{body}</g>'


def racket(cx=64, cy=48, rx=30, ry=36, frame=R, ang=-20, faced=True, strings="#fff", k=0.8, handle=34):
    """теннисная ракетка: овальный обод, струны, горло, ручка с обмоткой"""
    cid = f"rk{cx}{cy}{rx}"
    hy = cy + ry
    b = (f'<path d="M{cx-9} {hy-4} L{cx-4} {hy+12} H{cx+4} L{cx+9} {hy-4}" fill="none" stroke="{O}" stroke-width="9" stroke-linejoin="round"/>'
         f'<path d="M{cx-9} {hy-4} L{cx-4} {hy+12} H{cx+4} L{cx+9} {hy-4}" fill="none" stroke="{frame}" stroke-width="4" stroke-linejoin="round"/>'
         + rect(cx - 6, hy + 10, 12, handle, DK, 4, 2.6)
         + "".join(line(f"M{cx-6} {hy+16+i*7} L{cx+6} {hy+12+i*7}", "#5A5470", 1.6) for i in range(int(handle / 7)))
         + f'<clipPath id="{cid}"><ellipse cx="{cx}" cy="{cy}" rx="{rx-4}" ry="{ry-4}"/></clipPath>'
         + f'<ellipse cx="{cx}" cy="{cy}" rx="{rx-4}" ry="{ry-4}" fill="#FFF7EC" fill-opacity=".85"/>'
         + f'<g clip-path="url(#{cid})">'
         + "".join(f'<path d="M{x} {cy-ry} V{cy+ry}" stroke="{strings}" stroke-width="2"/>' for x in range(cx - rx + 8, cx + rx, 7))
         + "".join(f'<path d="M{cx-rx} {y} H{cx+rx}" stroke="{strings}" stroke-width="2"/>' for y in range(cy - ry + 8, cy + ry, 7))
         + "".join(f'<path d="M{x} {cy-ry} V{cy+ry}" stroke="#9A93B0" stroke-width=".8"/>' for x in range(cx - rx + 8, cx + rx, 7))
         + "".join(f'<path d="M{cx-rx} {y} H{cx+rx}" stroke="#9A93B0" stroke-width=".8"/>' for y in range(cy - ry + 8, cy + ry, 7))
         + '</g>'
         + f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{O}" stroke-width="11"/>'
         + f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{frame}" stroke-width="5.5"/>')
    if faced:
        b += face(cx, cy + 2, d=10 * k / 0.8, k=k)
    return rot(b, ang, cx, cy + ry) if ang else b


def tball(x=64, y=64, r=28, mood="smile", d=None, k=None):
    """теннисный мяч-персонаж: жёлто-салатовый, два белых шва-дуги"""
    k = k or r / 32
    d = d or r * 0.32
    cid = f"tb{x}{y}{r}"
    m = {"smile": f"M{x-6*k:.0f} {y+8*k:.0f} Q{x} {y+14*k:.0f} {x+6*k:.0f} {y+8*k:.0f}",
         "open": f"M{x-6*k:.0f} {y+7*k:.0f} Q{x} {y+17*k:.0f} {x+6*k:.0f} {y+7*k:.0f}Z",
         "o": None, "none": None}[mood]
    b = (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{TB}"/>'
         f'<clipPath id="{cid}"><circle cx="{x}" cy="{y}" r="{r}"/></clipPath><g clip-path="url(#{cid})">'
         f'<path d="M{x-r*0.62:.0f} {y-r*1.05:.0f} Q{x-r*0.05:.0f} {y:.0f} {x-r*0.62:.0f} {y+r*1.05:.0f}" fill="none" stroke="#fff" stroke-width="{max(2.5, r/7):.1f}"/>'
         f'<path d="M{x+r*0.62:.0f} {y-r*1.05:.0f} Q{x+r*0.05:.0f} {y:.0f} {x+r*0.62:.0f} {y+r*1.05:.0f}" fill="none" stroke="#fff" stroke-width="{max(2.5, r/7):.1f}"/></g>'
         f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" {s()}/>')
    if mood == "none":
        return b
    b += eye(x - d, y, k) + eye(x + d, y, k)
    b += (f'<ellipse cx="{x-d-5*k:.1f}" cy="{y+7*k:.1f}" rx="{4.5*k:.1f}" ry="{2.6*k:.1f}" fill="#FF7FA8" opacity=".7"/>'
          f'<ellipse cx="{x+d+5*k:.1f}" cy="{y+7*k:.1f}" rx="{4.5*k:.1f}" ry="{2.6*k:.1f}" fill="#FF7FA8" opacity=".7"/>')
    if m:
        b += f'<path d="{m}" fill="{"#E8554A" if mood == "open" else "none"}" stroke="{O}" stroke-width="{2.6*k:.1f}" stroke-linecap="round"/>'
    return b


def mini(x, y, r=8):
    return tball(x, y, r, mood="none")


def kid(x, y, shirt, pose="serve", hair="#8A5A3C", skirt=False):
    """ребёнок-игрок (голова в x,y)"""
    head = circ(x, y, 13, SKIN, 3) + path(f"M{x-13} {y-2} Q{x-12} {y-16} {x} {y-15} Q{x+12} {y-16} {x+13} {y-2} Q{x+4} {y-9} {x-13} {y-2}Z", hair, 2.4) + face(x, y + 2, d=4.5, k=0.42)
    body = path(f"M{x-9} {y+15} H{x+9} L{x+8} {y+40} H{x-8}Z", shirt, 2.6)
    if skirt:
        body += path(f"M{x-8} {y+34} L{x-14} {y+44} H{x+14} L{x+8} {y+34}Z", shirt, 2.4)
    legs = line(f"M{x-4} {y+40} L{x-12} {y+62} M{x+4} {y+40} L{x+14} {y+60}", O, 5)
    return legs + body + head


def murena(x=64, y=62, col="#7FBF5A", spots="#4E8F3A", k=0.9, cap=R, mouth="smile", tail=True):
    """мурена-персонаж: длинная голова с открытой улыбкой выныривает из воды, в плавательной шапочке"""
    b = ""
    if tail:
        b += path(f"M{x+18} 104 Q{x+40} 88 {x+34} 74 Q{x+30} 66 {x+40} 60", col, 3) + line(f"M{x+18} 104 Q{x+40} 88 {x+34} 74 Q{x+30} 66 {x+40} 60", col, 6)
    b += path(f"M{x+22} {y-12} Q{x+36} {y} {x+30} {y+30} Q{x+34} {y+50} {x+28} 112 H{x+16}Z", "#FF9A6B", 2.6)
    b += path(f"M{x-20} 112 Q{x-26} {y+20} {x-18} {y-6} Q{x-8} {y-34} {x+12} {y-30} Q{x+30} {y-24} {x+26} {y+2} Q{x+20} {y+24} {x+20} 112Z", col)
    b += "".join(circ(x + dx, y + dy, r, spots, 0) for dx, dy, r in [(-12, 18, 3), (-4, 30, 2.5), (8, 22, 3), (14, 36, 2.5), (-10, 40, 2.5)])
    b += path(f"M{x-14} {y-4} Q{x-2} {y-14} {x+22} {y-4}", sw=0)
    # шапочка
    if cap:
        b += path(f"M{x-17} {y-10} Q{x-12} {y-36} {x+10} {y-32} Q{x+28} {y-28} {x+25} {y-6} Q{x+4} {y-16} {x-17} {y-10}Z", cap, 2.8)
        b += line(f"M{x-8} {y-24} Q{x+4} {y-30} {x+16} {y-22}", "#fff", 2.4)
    b += face(x + 4, y + 2, d=10 * k, k=k, mouth=False)
    if mouth == "smile":
        b += path(f"M{x-6} {y+12} Q{x+4} {y+22} {x+14} {y+12}Z", "#E8554A", 2.4) + path(f"M{x-2} {y+13} L{x} {y+16} L{x+2} {y+13} M{x+6} {y+14} L{x+8} {y+17} L{x+10} {y+14}", "#fff", 1.2)
    return b


I = {}
# ========================== ТЕННИС ==========================
I["kolomensky-tennis-club"] = ("sky", "теннисный мяч в шапке Мономаха (Коломенское)",
    tball(64, 74, 34) +
    path("M38 46 Q64 32 90 46 L88 54 Q64 46 40 54Z", "#8A5A3C", 2.8) +
    path("M42 46 Q44 20 64 18 Q84 20 86 46 Q64 38 42 46Z", GOLD, 2.8) +
    line("M52 40 Q54 26 64 22 M76 40 Q74 26 64 22", "#C99A2E", 2) +
    line("M64 18 V6 M58 11 H70", O, 3) + circ(52, 34, 2.6, R, 1.2) + circ(76, 34, 2.6, B, 1.2) + sp((18, 30, 6), (110, 28, 5)))
I["tennis-art-otradnoe"] = ("purple", "теннисная ракетка с радужными струнами («Теннис-арт»)",
    racket(62, 48, 32, 38, B, -18, strings="#fff") +
    "".join(f'<path d="M{20+i*8} 4 L{20+i*8} 4" />' for i in range(1)) +
    rot("".join(f'<path d="M{34+i*9} 14 V82" stroke="{c}" stroke-width="4" opacity=".75" stroke-linecap="round"/>'
                for i, c in enumerate([R, OR, Y, G, B, V, P])), -18, 62, 86) +
    rot(face(62, 50, d=12, k=0.85), -18, 62, 86) +
    path("M100 96 Q104 104 100 110 Q96 104 100 96Z", V, 2) + path("M108 84 Q111 90 108 94 Q105 90 108 84Z", OR, 1.8) +
    mini(24, 100, 9))
I["bz-tennis-mosrentgen"] = ("green", "теннисный мяч чихает — «Будь здоров!»",
    tball(58, 70, 34, mood="o") +
    path("M48 82 Q58 90 68 82", sw=2.6) +
    path("M88 66 Q104 52 118 60 Q112 74 98 76 Q92 76 88 66Z", "#fff", 2.6) +
    "".join(circ(x, y, r, "#BFE9FF", 1.6) for x, y, r in [(100, 38, 4), (112, 46, 3), (92, 30, 2.6)]) +
    line("M22 30 L30 38 M18 44 L28 46", O, 2.6) + txt(64, 22, "АПЧХИ!", 12))
I["major-tennis-nagornaya"] = ("orange", "малыш поднимает над головой кубок турнира («Мейджор»)",
    kid(54, 46, "#5CB7F2") + line("M46 64 L34 40 M62 64 L74 40", O, 5) +
    path("M26 18 H52 V28 Q52 42 39 42 Q26 42 26 28Z", GOLD, 2.6) + path("M26 22 Q16 22 18 30 Q20 36 27 34 M52 22 Q62 22 60 30 Q58 36 51 34", sw=2.4) +
    rect(34, 42, 10, 6, GOLD, 2, 2.2) + rect(30, 48, 18, 5, "#C98A4B", 2, 2.2) +
    racket(96, 72, 16, 19, R, 24, faced=False, handle=20) + mini(108, 30, 8) + sp((112, 104, 6), (16, 96, 5)))
I["spartak-tennis-sokolniki"] = ("sky", "теннисная ракетка в красно-белом шарфе болельщика («Спартак»)",
    racket(64, 46, 30, 36, R, 0, k=0.85) +
    path("M34 88 Q64 98 94 88 L96 98 Q64 108 32 98Z", "#E8454F", 2.6) +
    "".join(line(f"M{x} {89+abs(64-x)//8} L{x-2} {99+abs(64-x)//8}", "#fff", 4) for x in (42, 56, 72, 86)) +
    path("M84 96 L90 122 L100 120 L96 96Z", "#E8454F", 2.4) + line("M88 104 L97 103 M90 112 L99 111", "#fff", 3) +
    mini(110, 30, 9) + sp((18, 30, 6)))
I["orbita-tennis-park"] = ("night", "теннисный мяч-планета с кольцом орбиты («Орбита»)",
    f'<ellipse cx="64" cy="66" rx="52" ry="14" fill="none" stroke="{O}" stroke-width="8" transform="rotate(-14 64 66)"/>'
    f'<ellipse cx="64" cy="66" rx="52" ry="14" fill="none" stroke="#FFB36B" stroke-width="4" transform="rotate(-14 64 66)"/>' +
    tball(64, 64, 32) +
    f'<path d="M14 72 Q64 92 116 52" fill="none" stroke="{O}" stroke-width="8" transform="rotate(0)"/>'
    f'<path d="M15 72 Q64 92 114 53" fill="none" stroke="#FFB36B" stroke-width="4"/>' +
    sp((20, 24, 6), (108, 22, 4), (110, 104, 5), (26, 104, 4)) + circ(100, 26, 3, "#fff", 0))
I["yuzhny-tennis-club"] = ("yellow", "теннисный мяч перепрыгивает сетку, как через скакалку",
    path("M12 76 V112 M116 76 V112", sw=6) + rect(12, 76, 104, 22, "#fff", 2, 2.6) +
    "".join(line(f"M{x} 78 V96", "#9A93B0", 1.4) for x in range(20, 116, 8)) +
    "".join(line(f"M14 {y} H114", "#9A93B0", 1.4) for y in (84, 91)) + line("M12 77 H116", "#fff", 6) + path("M12 77 H116", sw=1.6) +
    tball(64, 44, 22, mood="open") + line("M44 64 Q52 70 58 66 M84 64 Q76 70 70 66", O, 4) +
    line("M30 50 Q36 36 46 32 M98 50 Q92 36 82 32", "#fff", 3) + "".join(line(f"M{x} 118 Q{x+8} 112 {x+16} 118", "#E0B44A", 2) for x in (20, 90)))
I["champion-olonetsky-tennis"] = ("pink", "теннисная ракетка на высшей ступеньке пьедестала («Чемпион»)",
    rect(10, 98, 36, 30, "#C9D2E3", 2, 2.6) + rect(46, 84, 36, 44, GOLD, 2, 2.6) + rect(82, 104, 36, 24, "#E0A06A", 2, 2.6) +
    txt(64, 112, "1", 20, "#fff") + txt(28, 120, "2", 14) + txt(100, 122, "3", 12) +
    racket(64, 36, 22, 26, B, 0, k=0.62, handle=12) + line("M40 28 L32 22 M88 28 L96 22", O, 3) +
    sp((20, 28, 7), (108, 34, 6), (106, 80, 4)))
I["skolkovo-tennis-school"] = ("teal", "теннисный мяч-робот с антенной и лампочкой («Сколково»)",
    tball(64, 70, 34) +
    line("M64 36 V18", O, 3) + circ(64, 14, 6, "#FFE16B", 2.4) + line("M54 10 L50 6 M74 10 L78 6 M64 4 V0", "#FFE16B", 2.4) +
    rect(24, 62, 8, 16, GR, 3, 2.4) + rect(96, 62, 8, 16, GR, 3, 2.4) +
    "".join(circ(x, y, 2.2, GR, 1.2) for x, y in [(46, 48), (82, 48), (46, 92), (82, 92)]) + sp((18, 28, 6), (108, 32, 5)))
I["ace-tennis-flotskaya"] = ("blue", "теннисный мяч выглядывает из игральной карты-туза («Эйс»)",
    rot(rect(30, 18, 64, 92, "#fff", 8, 3) + txt(42, 38, "A", 16, R) + path("M80 96 Q72 88 76 84 Q80 82 82 86 Q84 82 88 84 Q92 88 84 96Z", R, 1.6), -10, 62, 64) +
    tball(70, 72, 26) + line("M100 96 L112 92 M98 104 L114 104 M100 112 L112 116", "#fff", 3) + sp((18, 104, 6), (108, 20, 5)))
I["mf41-tennis"] = ("purple", "теннисный мяч-кинозвезда на красной дорожке («Мосфильм»)",
    path("M40 128 L52 92 H76 L88 128Z", "#E8454F", 2.6) + line("M40 128 L52 92 M88 128 L76 92", "#C0303A", 2) +
    tball(64, 62, 28) +
    path("M64 10 L69 22 L82 22 L72 30 L76 42 L64 35 L52 42 L56 30 L46 22 L59 22Z", GOLD, 2.4) +
    "".join(line(d, "#FFF6C4", 2.6) for d in ["M22 30 L32 38", "M106 30 L96 38", "M16 56 H28", "M112 56 H100"]) +
    racket(104, 96, 10, 12, B, 30, faced=False, handle=10))
I["champion-tennis-plyushchikha"] = ("green", "теннисная ракетка, увитая плющом («Плющиха»)",
    racket(64, 48, 30, 36, "#A98BF0", 0, k=0.85) +
    "".join(path(f"M{x} {y} q6 -8 12 0 q-6 8 -12 0Z", "#4FAE4A", 1.8) for x, y in
            [(30, 30), (40, 14), (62, 8), (84, 16), (92, 34), (94, 58), (84, 78), (34, 70), (30, 52)]) +
    line("M36 30 Q34 14 62 10 Q90 12 98 40 Q100 62 86 80", "#3E8A3A", 2) +
    mini(24, 106, 9) + sp((110, 108, 6)))
I["polekort-tennis"] = ("orange", "малыш бьёт двуручный бэкхенд",
    kid(58, 40, "#7CD26E", hair="#3B3355") +
    line("M52 62 L74 52 M64 62 L76 56", O, 5) +
    racket(96, 34, 16, 19, B, 40, faced=False, handle=18) +
    tball(24, 34, 10, mood="open", d=4, k=0.4) + line("M36 40 L48 46 M34 48 L46 52", "#fff", 3) + sp((110, 100, 6), (16, 100, 5)))
I["liga-tennis-butlerova"] = ("teal", "два теннисных мяча дают «пять» («Лига»)",
    tball(38, 72, 24) + tball(90, 72, 24) +
    line("M58 66 L62 48 M70 66 L66 48", O, 5) +
    circ(62, 44, 6, TB, 2.4) + circ(66, 44, 6, TB, 2.4) +
    "".join(line(d, "#fff", 3) for d in ["M64 30 V22", "M52 34 L46 28", "M76 34 L82 28"]) +
    racket(18, 112, 8, 10, R, -30, faced=False, handle=8) + sp((110, 24, 6)))

# ========================== ГИМНАСТИКА ==========================
I["gimnast-moscow-gorodetskaya"] = ("pink", "гимнастка делает стойку на руках, судья показывает «10»",
    rect(14, 108, 100, 12, "#5CB7F2", 4, 2.6) +
    line("M52 104 L46 80 M64 104 L70 80", O, 5) +
    path("M48 82 H68 L66 54 H50Z", P, 2.6) +
    line("M52 56 L44 28 M64 56 L74 30", O, 5) + circ(58, 90, 11, SKIN, 3) + face(58, 90, d=4, k=0.4) +
    path("M48 96 Q58 102 68 96", "#8A5A3C", 2) +
    rect(88, 20, 30, 24, "#fff", 4, 2.6) + txt(103, 39, "10", 18, R) + line("M103 44 V58", O, 3) + sp((22, 30, 7), (30, 60, 4)))
I["gym-soyuz-semenovsky"] = ("yellow", "гимнастический конь с ушками и хвостиком",
    line("M34 82 L28 116 M94 82 L100 116 M40 82 L42 116 M88 82 L86 116", O, 5) +
    path("M18 62 Q18 52 30 52 H98 Q110 52 110 62 V76 Q110 86 98 86 H30 Q18 86 18 76Z", "#C98A4B") +
    path("M46 52 V40 Q46 34 52 34 H56 V52 M72 52 V34 H76 Q82 34 82 40 V52", "#F2F2F2", 2.6) +
    path("M18 58 L10 42 L24 50Z M24 54 L20 38 L32 50Z", "#C98A4B", 2.4) +
    path("M110 64 Q124 66 120 86 Q116 78 110 76", "#6B4226", 2.4) +
    face(64, 66, d=12, k=0.75) + sp((22, 24, 6), (108, 26, 5)))

# ========================== ПЛАВАНИЕ ==========================
I["splash-bakuninskaya"] = ("blue", "малыш ныряет в бассейн — большой «бульк» с брызгами",
    WATER +
    path("M30 98 Q36 70 46 86 Q50 60 60 82 Q64 52 70 82 Q78 58 82 86 Q92 70 98 98Z", "#BFE9FF", 2.6) +
    "".join(circ(x, y, r, "#BFE9FF", 2) for x, y, r in [(28, 70, 4), (100, 68, 5), (40, 52, 3), (88, 46, 3.5)]) +
    line("M58 40 L60 22 M70 40 L68 22", O, 5) + ell(64, 46, 9, 8, SKIN, 2.6) +
    path("M54 56 H74 L70 80 H58Z", "#FF8A3D", 2.4) + circ(64, 60, 0.1, O, 0) + sp((112, 24, 6)))
I["olimp80-pool"] = ("sky", "малыш в шапочке плывёт по дорожке между поплавками, на тумбе «80»",
    WATER.replace("M0 98", "M0 64").replace("V128 H0Z", "V128 H0Z") + rect(-4, 60, 140, 70, "#7FD3F7", 0, 0) +
    "".join(circ(x, 74, 4.5, R if (x // 10) % 2 else "#fff", 1.6) for x in range(4, 128, 10)) +
    "".join(circ(x, 112, 4.5, R if (x // 10) % 2 else "#fff", 1.6) for x in range(4, 128, 10)) +
    rect(92, 34, 28, 24, "#fff", 3, 2.6) + txt(106, 52, "80", 14, B) + line("M96 58 L94 70 M116 58 L118 70", O, 3) +
    ell(52, 94, 14, 12, SKIN, 2.6) + path("M38 92 Q40 76 52 76 Q66 76 66 92Z", Y, 2.6) + face(52, 96, d=5, k=0.45) +
    line("M30 96 Q22 88 18 96 M74 96 Q82 88 86 96", "#fff", 3) + sp((22, 26, 6), (60, 30, 5)))

MUR = {
    "murena-korall": ("blue", "мурена в шапочке выглядывает из кораллового рифа (СК «Коралл»)",
        dict(col="#E0B44A", spots="#9C6A1E", cap=R),
        path("M8 112 Q6 82 18 76 Q14 92 26 90 Q22 70 34 66 Q32 88 40 112Z", "#FF8F7A", 2.6)
        + path("M96 112 Q90 86 102 80 Q100 94 110 92 Q108 74 120 72 Q122 96 122 112Z", "#FF8FB8", 2.6)),
    "murena-bauman": ("sky", "мурена держит доску для плавания (МГТУ им. Баумана)",
        dict(col="#E0B44A", spots="#B58A2A", cap=B),
        rect(84, 70, 34, 22, "#FFE16B", 9, 2.6) + line("M92 81 H110", "#FF9A3D", 3)),
    "murena-severny": ("teal", "мурена в полосатом шарфе выныривает («Северный»)",
        dict(col="#8C9CC8", spots="#5E6E9E", cap=None),
        path("M40 78 Q64 88 90 78 L92 88 Q64 98 38 88Z", B, 2.6) + line("M50 82 V92 M64 85 V95 M78 82 V92", "#fff", 3)
        + path("M86 84 L98 104 L106 98 L92 82Z", B, 2.4) + path("M42 38 Q48 22 66 20 Q86 20 92 38 Q66 28 42 38Z", "#fff", 2.6)
        + circ(66, 16, 5, R, 2)),
    "murena-mgsu": ("yellow", "мурена в строительной каске (НИУ МГСУ)",
        dict(col="#9DB0D8", spots="#5E6E9E", cap=None),
        path("M40 40 Q42 18 66 18 Q90 18 92 40Z", "#FFC93C", 2.8) + rect(34, 38, 64, 7, "#FFC93C", 3, 2.6) + line("M66 18 V38", "#E0A020", 3)),
    "murena-nekrasovka": ("sky", "мурена плавает в надувном круге (ДС «Некрасовка»)",
        dict(col="#A98BF0", spots="#7A5CC4", cap=Y),
        ell(64, 98, 44, 14, R, 2.8) + ell(64, 96, 26, 7, "#7FD3F7", 2.4)
        + "".join(line(d, "#fff", 6) for d in ["M30 92 L34 106", "M94 92 L90 106", "M64 84 V88", "M64 110 V112"])),
    "murena-izumrudny": ("green", "изумрудная мурена пускает пузыри-сердечки (бассейн «Изумрудный»)",
        dict(col="#3CC78A", spots="#22966A", cap=P),
        "".join(path(f"M{x} {y+4} q-6 -6 -6 -10 q0 -5 6 -3 q6 -2 6 3 q0 4 -6 10Z", "#FF8FB8", 1.8) for x, y in [(20, 40), (30, 22), (102, 34)])),
    "murena-umka": ("blue", "мурена в шапочке с ушками белого медвежонка (СК «Умка»)",
        dict(col="#E0B44A", spots="#B58A2A", cap="#fff"),
        circ(48, 30, 7, "#fff", 2.6) + circ(80, 28, 7, "#fff", 2.6) + circ(48, 30, 3, P, 0) + circ(80, 28, 3, P, 0)),
    "murena-internat": ("pink", "мурена-первоклашка с большим бантом (бассейн школы-интерната)",
        dict(col="#F2A27E", spots="#C0644A", cap=None),
        path("M66 30 Q48 14 44 30 Q48 44 66 34 Q84 44 88 30 Q84 14 66 30Z", "#fff", 2.6) + circ(66, 32, 5, "#fff", 2.4)),
    "murena-zhivopisny": ("teal", "мурена в нарукавниках учится плавать (бассейн «Живописный»)",
        dict(col="#C9A3F0", spots="#8C64C8", cap=G),
        ell(40, 84, 10, 8, OR, 2.6) + ell(92, 84, 10, 8, OR, 2.6) + line("M34 84 H46 M86 84 H98", "#fff", 2.4)),
}
for pid, (bg, subj, kw, extra) in MUR.items():
    if kw is None:
        body = (WATER + path("M14 98 Q22 34 64 30 Q104 32 112 98", sw=0)
                + f'<path d="M20 98 Q30 36 66 32 Q102 34 110 96" fill="none" stroke="{O}" stroke-width="20" stroke-linecap="round"/>'
                + f'<path d="M20 98 Q30 36 66 32 Q102 34 110 96" fill="none" stroke="#FF9A6B" stroke-width="13" stroke-linecap="round"/>'
                + "".join(circ(x, y, 2.6, "#D9653E", 0) for x, y in [(30, 64), (44, 44), (88, 42), (102, 62)])
                + path("M60 22 Q66 14 76 20 Q82 26 76 32 Q64 36 58 30Z", R, 2.6)
                + face(70, 34, d=5, k=0.45, mouth=False) + path("M66 40 Q71 44 76 40", sw=2)
                + "".join(circ(x, y, r, "#BFE9FF", 2) for x, y, r in [(16, 86, 4), (114, 84, 4), (24, 76, 3), (106, 74, 3)])
                + WAVES)
    else:
        body = WATER + murena(**kw) + extra + WAVES
    I[pid] = (bg, subj, body)

# ========================== ТАНЦЫ ==========================
def pointe(x, y, ang, col=P):
    b = (line(f"M{x-12} {y-36} Q{x-26} {y-50} {x-14} {y-58} M{x+12} {y-36} Q{x+24} {y-48} {x+16} {y-58}", "#E85A92", 3)
         + path(f"M{x-14} {y-38} Q{x-16} {y} {x-8} {y+18} Q{x} {y+26} {x+8} {y+18} Q{x+16} {y} {x+14} {y-38}Z", col, 3)
         + rect(x - 8, y + 12, 16, 10, "#F7B6CF", 4, 2.4)
         + line(f"M{x-14} {y-30} L{x+14} {y-14} M{x+14} {y-30} L{x-14} {y-14}", "#E85A92", 3))
    return rot(b, ang, x, y)


I["tdance-tango-tsska"] = ("orange", "пуанты танцуют танго с розой в зубах (студия «Танго»)",
    pointe(44, 70, -12, P) + pointe(84, 70, 12, "#FFB3CC") + face(43, 56, d=5, k=0.5) + face(85, 56, d=5, k=0.5, mouth=False) +
    path("M80 66 Q85 70 90 66", sw=2) + line("M90 68 L106 60", "#3E8A3A", 2.6) + circ(109, 57, 6, R, 2.2) +
    sp((16, 104, 6), (112, 104, 5), (64, 18, 6)))
I["samplus-krasnoselskaya"] = ("purple", "малыш крутит брейк-данс на голове в кепке козырьком назад",
    ell(64, 112, 34, 7, "#C9B8F5", 2.4) +
    circ(64, 96, 12, SKIN, 3) + path("M52 104 Q64 116 76 104 L76 110 Q64 118 52 110Z", R, 2.4) + face(64, 94, d=4.5, k=0.42) +
    path("M54 80 H74 L72 56 H56Z", Y, 2.6) +
    line("M58 56 L40 30 M70 56 L90 28", O, 5) + line("M56 80 L38 92 M72 80 L90 92", O, 5) +
    line("M24 72 Q20 56 30 44 M104 72 Q108 56 98 44", "#fff", 3) + path("M30 44 l-6 2 l4 -6Z", "#fff", 0) +
    sp((22, 20, 6), (108, 18, 5)))
I["tancuy-tut-tsvetnoy"] = ("pink", "девочка-балеринка в пачке и диадеме кружится (Baby dance)",
    line("M58 92 L54 118 M70 92 L80 116", O, 4.5) + path("M50 118 H58 M78 116 L86 112", sw=4) +
    path("M14 86 Q64 66 114 86 Q104 100 64 102 Q24 100 14 86Z", "#FFE1EE", 2.8) +
    path("M26 88 Q64 76 102 88 Q92 96 64 96 Q36 96 26 88Z", "#FFC2DA", 2) +
    path("M54 84 L52 58 H76 L74 84Z", P, 2.6) +
    line("M54 62 Q38 50 34 34 M74 62 Q90 50 94 34", O, 4.5) +
    circ(64, 42, 14, SKIN, 3) + path("M50 40 Q50 26 64 26 Q78 26 78 40 Q70 32 64 34 Q58 32 50 40Z", "#8A5A3C", 2.4) +
    circ(64, 22, 6, "#8A5A3C", 2.4) + face(64, 44, d=5, k=0.45) +
    path("M54 30 L57 22 L61 28 L64 18 L67 28 L71 22 L74 30Z", GOLD, 2) +
    line("M12 58 Q6 70 12 82 M116 58 Q122 70 116 82", "#fff", 3) + sp((22, 26, 6), (106, 24, 5)))

if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        bg, subj, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(bg, body))
    print("svg:", len(ids))
