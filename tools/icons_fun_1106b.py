"""Иконки робота fun (2026-11-06, утро): 34 новых сюжета — сказочные персонажи, игрушки, животные, транспорт,
природа. Каждый сюжет сверен с icons-catalog/sheet-*.png и icons-src/subjects.txt (не повторяется).
Запуск: python3 tools/icons_fun_1106b.py [id ...]"""
import os, sys, math as _m
from draw_icons import svg, s, eye, face, sparkle, O
W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=9, k=0.75, **kw: face(cx, cy, d=d, k=k, **kw)
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
R, OR, Y, G, B, P, V, BR, WH, GR = ("#E8654F", "#FF9A3D", "#FFD25E", "#7CD26E", "#5CB7F2", "#FF8FB8", "#A98BF0",
                                    "#C0732E", "#FFFFFF", "#B8BCCB")
DG, SK, TE, DB, NV = "#4E9A5A", "#FFD9B8", "#5CCDBA", "#8A5A3C", "#2B2A44"
sp = lambda *pts: "".join(sparkle(x, y, r) for x, y, r in pts)
GROUND = f'<path d="M0 104 Q64 92 128 104 V128 H0Z" fill="{G}" {W(2.6)}/>'
WATER = f'<path d="M0 100 Q16 92 32 100 T64 100 T96 100 T128 100 V128 H0Z" fill="#7FD3F7" {W(2.6)}/>'


def kid(cx, cy, r=14, skin=SK):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{skin}" {s()}/>' + f(cx, cy + 1, d=r * 0.38, k=r / 22)


def petals(cx, cy, n, rx, ry, dist, colors, rot0=0):
    o = ""
    for i in range(n):
        a = rot0 + 360 * i / n
        c = colors[i % len(colors)]
        o += (f'<ellipse cx="{cx}" cy="{cy - dist}" rx="{rx}" ry="{ry}" fill="{c}" {W(2.4)} '
              f'transform="rotate({a:.1f} {cx} {cy})"/>')
    return o


def stem(x1, y1, x2, y2, w=4):
    return f'<path d="M{x1} {y1} Q{(x1 + x2) / 2 + 6} {(y1 + y2) / 2} {x2} {y2}" fill="none" stroke="{DG}" stroke-width="{w}" stroke-linecap="round"/>'


def leaf(x, y, rot, rx=12, ry=6, c=G):
    return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{c}" {W(2.2)} transform="rotate({rot} {x} {y})"/>'


I = {}
# ===================== Сказочные персонажи =====================
I["terra-mystic-sokol"] = ("night", "вампирчик в плаще",
    f'<path d="M20 120 Q24 70 64 66 Q104 70 108 120Z" fill="{NV}" {s()}/><path d="M34 120 Q40 84 64 82 Q88 84 94 120Z" fill="{R}" {W(2.4)}/>'
    f'<path d="M30 70 L44 52 L52 70Z M98 70 L84 52 L76 70Z" fill="{NV}" {W(2.4)}/>'
    f'<circle cx="64" cy="54" r="22" fill="#E4E6F4" {s()}/><path d="M42 48 Q50 30 64 42 Q78 30 86 48 Q86 34 64 30 Q42 34 42 48Z" fill="{NV}" {W(2.4)}/>'
    + f(64, 56, d=8, k=0.8) + f'<path d="M58 66 l2 5 l2 -5 M66 66 l2 5 l2 -5" fill="#fff" {W(1.6)}/>'
    + f'<path d="M92 24 q6 -6 12 0 q6 -6 12 0 q-6 2 -12 8 q-6 -6 -12 -8Z" fill="#3B3355" {W(2)}/>' + sp((22, 28, 5), (40, 18, 3)))
I["hide-dark-kostromskaya"] = ("purple", "шапка-невидимка",
    f'<g opacity=".8"><path d="M26 90 Q24 40 64 36 Q104 40 102 90Z" fill="{V}" stroke="#fff" stroke-width="3" stroke-dasharray="6 5"/>'
    + "".join(f'<path d="M{x} 44 Q{x + 2} 66 {x} 88" fill="none" stroke="#C9B8FF" stroke-width="3"/>' for x in (44, 64, 84))
    + f'<rect x="20" y="84" width="88" height="18" rx="8" fill="#C9B8FF" stroke="#fff" stroke-width="3" stroke-dasharray="6 5"/>'
    f'<circle cx="64" cy="30" r="12" fill="#fff" stroke="#C9B8FF" stroke-width="3" stroke-dasharray="4 4"/></g>'
    + f(64, 66, d=9, k=0.8) + sp((18, 40, 6), (108, 48, 5), (24, 112, 4), (104, 112, 5), (40, 20, 3)))
I["theatre-of-nations"] = ("yellow", "Кот в сапогах",
    f'<path d="M44 96 L42 116 H58 L60 96Z M68 96 L70 116 H86 L84 96Z" fill="{BR}" {s()}/>'
    f'<path d="M38 114 H62 V120 H38Z M66 114 H90 V120 H66Z" fill="{DB}" {W(2.4)}/>'
    f'<ellipse cx="64" cy="84" rx="24" ry="20" fill="{OR}" {s()}/><path d="M86 86 Q108 80 104 58" fill="none" stroke="{OR}" stroke-width="7" stroke-linecap="round"/>'
    f'<circle cx="64" cy="50" r="20" fill="{OR}" {s()}/><path d="M46 40 L46 22 L58 34Z M82 40 L82 22 L70 34Z" fill="{OR}" {W(2.4)}/>'
    + f(64, 52, d=8, k=0.8) + f'<path d="M44 56 h-10 M44 60 h-10 M84 56 h10 M84 60 h10" {W(1.8)}/>'
    f'<path d="M34 34 Q64 14 94 34 Q64 28 34 34Z" fill="{R}" {W(2.4)}/><path d="M86 28 Q102 10 110 22" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>')
I["teatr-osobnyak"] = ("sky", "Конёк-Горбунок",
    GROUND + f'<path d="M40 82 L36 112 M50 86 L50 114 M78 86 L78 114 M88 82 L92 112" stroke="{BR}" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M30 78 Q34 58 52 62 Q60 46 70 62 Q90 58 94 78 Q90 92 62 92 Q34 92 30 78Z" fill="#E8B880" {s()}/>'
    f'<path d="M84 76 Q92 50 96 40 L110 46 Q104 64 96 82Z" fill="#E8B880" {s()}/><ellipse cx="104" cy="44" rx="13" ry="10" fill="#E8B880" {s()}/>'
    f'<path d="M96 30 L94 18 L102 26Z M106 32 L110 20 L112 34Z" fill="#E8B880" {W(2.2)}/>'
    + f(104, 44, d=5, k=0.55) + f'<path d="M92 36 Q86 48 88 62" fill="none" stroke="{Y}" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M30 76 Q16 80 18 96" fill="none" stroke="{Y}" stroke-width="5" stroke-linecap="round"/>'
    f'<ellipse cx="44" cy="22" rx="10" ry="12" fill="#fff" opacity=".0"/>' + sp((24, 32, 6), (60, 26, 5)))
I["glazunov-gallery"] = ("orange", "сапоги-скороходы",
    f'<path d="M26 34 H50 V84 Q50 96 62 98 L66 112 H22 Z" fill="{R}" {s()}/><path d="M68 28 H92 V78 Q92 90 104 92 L108 106 H64 Z" fill="{R}" {s()}/>'
    f'<path d="M24 34 H52 M66 28 H94" {W(4)}/><path d="M22 112 H66 M64 106 H108" {W(3.6)}/>'
    + "".join(f'<path d="M{x} {y} q-10 -3 -16 0" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>' for x, y in [(20, 60), (18, 76), (62, 54), (60, 70)])
    + f'<path d="M30 46 Q38 52 46 46 M72 40 Q80 46 88 40" fill="none" stroke="{Y}" stroke-width="3"/>'
    + f(38, 70, d=6, k=0.6) + f(80, 64, d=6, k=0.6) + sp((108, 30, 6), (100, 50, 4)))
I["gmii-gallery-golitsyn"] = ("green", "цветик-семицветик",
    stem(64, 128, 64, 70, 5) + leaf(48, 104, -30) + leaf(80, 96, 30)
    + petals(64, 56, 7, 10, 17, 22, [R, OR, Y, G, "#6CC0F2", B, V])
    + f'<circle cx="64" cy="56" r="14" fill="#FFF3A0" {s()}/>' + f(64, 57, d=6, k=0.6) + sp((20, 24, 6), (108, 22, 5)))

# ===================== Животные =====================
I["shakhmatovo"] = ("yellow", "такса",
    GROUND + f'<rect x="28" y="70" width="64" height="22" rx="11" fill="{BR}" {s()}/>'
    f'<path d="M34 90 V104 M46 90 V104 M74 90 V104 M86 90 V104" stroke="{DB}" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M30 76 Q16 70 14 58" fill="none" stroke="{BR}" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M84 76 Q86 50 100 48 Q116 50 118 64 Q116 74 104 74Z" fill="{BR}" {s()}/>'
    f'<path d="M92 52 Q82 58 88 76 Q96 72 96 56Z" fill="{DB}" {W(2.4)}/><circle cx="117" cy="64" r="3.5" fill="{NV}"/>'
    + eye(104, 58, 0.6) + f'<path d="M48 70 h24" stroke="{R}" stroke-width="4"/><circle cx="60" cy="74" r="3" fill="{Y}" {W(1.6)}/>' + sp((22, 30, 6), (60, 30, 5)))
I["paustovsky-museum"] = ("sky", "сорока",
    f'<path d="M10 92 Q64 84 120 92" fill="none" stroke="{DB}" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M30 70 L6 52 L14 76Z" fill="#3E4AA0" {s()}/>'
    f'<ellipse cx="56" cy="68" rx="28" ry="18" fill="{NV}" {s()}/><path d="M40 70 Q56 86 76 72 Q64 62 40 70Z" fill="#fff" {W(2.4)}/>'
    f'<path d="M44 62 Q58 52 72 60" fill="none" stroke="#5CB7F2" stroke-width="4"/>'
    f'<circle cx="82" cy="50" r="15" fill="{NV}" {s()}/><path d="M96 48 L110 52 L96 56Z" fill="{NV}" {W(2.2)}/>'
    f'<circle cx="86" cy="46" r="4.5" fill="#fff"/>' + eye(86, 46, 0.5)
    + f'<path d="M54 86 V92 M62 86 V92" {W(3)}/><circle cx="108" cy="24" r="6" fill="{Y}" {W(2.2)}/>' + sp((20, 24, 5)))
I["lopasnya-zachatyevskoe"] = ("blue", "ласточка",
    f'<path d="M64 62 Q40 40 10 44 Q36 54 50 70Z M64 62 Q88 40 118 44 Q92 54 78 70Z" fill="{NV}" {s()}/>'
    f'<ellipse cx="64" cy="70" rx="16" ry="20" fill="{NV}" {s()}/><path d="M54 72 Q64 92 74 72 Q64 66 54 72Z" fill="#fff" {W(2.2)}/>'
    f'<path d="M56 88 L48 116 L64 96 L80 116 L72 88Z" fill="{NV}" {W(2.4)}/>'
    f'<path d="M56 60 Q64 66 72 60 Q64 56 56 60Z" fill="{R}" {W(2)}/>' + eye(58, 54, 0.55) + eye(70, 54, 0.55)
    + f'<path d="M62 62 L64 66 L66 62Z" fill="{Y}"/>' + sp((24, 96, 5), (106, 94, 6), (30, 22, 4)))
I["climb-lab-butyrskaya"] = ("teal", "рысь",
    f'<path d="M24 128 Q28 82 64 80 Q100 82 104 128Z" fill="#E0B070" {s()}/>'
    f'<circle cx="64" cy="62" r="30" fill="#E8BE7E" {s()}/>'
    f'<path d="M38 44 L34 14 L54 36Z M90 44 L94 14 L74 36Z" fill="#E8BE7E" {W(2.6)}/><path d="M34 14 V4 M94 14 V4" {W(3.4)}/>'
    f'<path d="M36 72 L22 84 L40 82 M92 72 L106 84 L88 82" fill="#fff" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.4" fill="{DB}"/>' for x, y in [(50, 46), (78, 46), (44, 58), (84, 58), (64, 40)])
    + f(64, 64, d=10, k=0.8) + f'<path d="M60 70 L64 74 L68 70Z" fill="{P}" {W(1.6)}/>')
I["pushisty-ostrov"] = ("pink", "шиншилла",
    GROUND + f'<ellipse cx="62" cy="80" rx="32" ry="26" fill="#C9CCD8" {s()}/>'
    f'<circle cx="38" cy="38" r="14" fill="#C9CCD8" {s()}/><circle cx="86" cy="38" r="14" fill="#C9CCD8" {s()}/>'
    f'<circle cx="38" cy="38" r="7" fill="{P}"/><circle cx="86" cy="38" r="7" fill="{P}"/>'
    f'<circle cx="62" cy="60" r="24" fill="#D8DBE6" {s()}/>' + f(62, 62, d=10, k=0.8)
    + f'<path d="M40 64 h-12 M40 68 h-12 M84 64 h12 M84 68 h12" {W(1.6)}/>'
    f'<path d="M92 92 Q118 90 112 66 Q106 80 94 82" fill="#C9CCD8" {W(2.4)}/>'
    f'<ellipse cx="62" cy="96" rx="12" ry="6" fill="#B0B4C4" {W(2)}/>')
I["kolomna-crocodile-farm"] = ("green", "игуана",
    f'<path d="M6 100 Q64 90 122 100" fill="none" stroke="{DB}" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M30 86 Q20 100 4 96" fill="none" stroke="#5DBB63" stroke-width="7" stroke-linecap="round"/>'
    f'<ellipse cx="58" cy="80" rx="30" ry="13" fill="#5DBB63" {s()}/>'
    + "".join(f'<path d="M{x} {68 - (x % 3)} l4 -8 l4 8" fill="#3E8A48" {W(1.8)}/>' for x in range(38, 82, 9))
    + f'<path d="M84 76 Q90 54 108 56 Q120 60 118 72 Q112 82 92 84Z" fill="#5DBB63" {s()}/>'
    f'<path d="M96 80 Q100 92 90 94 Q86 86 96 80Z" fill="{OR}" {W(2)}/>'
    f'<circle cx="104" cy="64" r="5" fill="#fff" {W(2)}/>' + eye(104, 64, 0.5)
    + f'<path d="M44 90 l-4 10 M70 90 l4 10" stroke="#5DBB63" stroke-width="5" stroke-linecap="round"/>' + sp((24, 30, 6), (60, 30, 5)))
I["dekabrskogo-vosstaniya"] = ("sky", "воробей",
    f'<path d="M10 100 Q64 92 118 100" fill="none" stroke="{DB}" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M30 74 L10 70 L22 88Z" fill="{BR}" {s()}/>'
    f'<ellipse cx="60" cy="74" rx="30" ry="22" fill="#C79A6A" {s()}/><path d="M44 80 Q60 96 80 82 Q66 74 44 80Z" fill="#F2E2C8" {W(2.2)}/>'
    f'<path d="M40 66 Q54 56 70 68 Q56 72 40 66Z" fill="{DB}" {W(2.2)}/>'
    f'<circle cx="84" cy="56" r="18" fill="#C79A6A" {s()}/><path d="M72 46 Q84 36 98 48 Q86 44 72 46Z" fill="{DB}" {W(2)}/>'
    f'<path d="M100 56 L110 60 L100 63Z" fill="{Y}" {W(2)}/>' + eye(88, 54, 0.55)
    + f'<circle cx="84" cy="64" r="3" fill="{P}" opacity=".7"/><path d="M54 94 V100 M64 94 V100" {W(3)}/>' + sp((24, 30, 6), (104, 24, 5)))
I["krivyakino-park"] = ("green", "глухарь",
    GROUND + f'<path d="M24 76 Q10 50 20 30 Q32 52 40 54 Q34 30 46 18 Q50 44 56 56Z" fill="{NV}" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="#fff"/>' for x, y in [(24, 46), (30, 56), (44, 36), (48, 48)])
    + f'<ellipse cx="64" cy="80" rx="28" ry="20" fill="#3B3355" {s()}/>'
    f'<path d="M76 70 Q80 44 94 40 Q108 40 108 54 Q104 66 88 78Z" fill="#3B3355" {s()}/>'
    f'<path d="M86 42 Q92 34 100 40 Q92 44 86 42Z" fill="{R}" {W(2)}/><path d="M106 50 L116 56 L104 58Z" fill="#E8E2C8" {W(2)}/>'
    + eye(98, 50, 0.55) + f'<path d="M84 60 Q90 66 86 74" fill="none" stroke="#4E9A5A" stroke-width="5"/>'
    f'<path d="M56 98 V108 M70 98 V108" {W(3)}/>' + sp((108, 22, 5)))
I["park-50-oktyabrya"] = ("blue", "щука",
    WATER + f'<path d="M12 64 Q40 40 86 50 L100 56 Q114 58 118 64 Q114 70 100 72 L86 78 Q40 88 12 64Z" fill="#8CC66A" {s()}/>'
    f'<path d="M12 64 L2 50 L4 64 L2 78Z" fill="#8CC66A" {W(2.4)}/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="4" ry="2.5" fill="#E8F0A0"/>' for x, y in [(34, 58), (48, 70), (60, 56), (72, 70), (44, 62)])
    + f'<path d="M54 46 Q62 36 74 46Z M56 80 L64 90 L70 80Z" fill="#6FAA52" {W(2.2)}/>'
    f'<path d="M104 66 Q112 66 118 64" fill="none" {W(2.4)}/>' + f'<circle cx="98" cy="58" r="5" fill="#fff" {W(2)}/>' + eye(98, 58, 0.5)
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#fff" {W(1.4)}/>' for x, y in [(110, 40), (116, 28), (106, 22)]))
I["fedorova-park"] = ("orange", "бурундук",
    GROUND + f'<path d="M80 96 Q118 86 108 46 Q100 30 88 40 Q98 60 80 80Z" fill="#C98A4E" {s()}/>'
    f'<ellipse cx="56" cy="80" rx="24" ry="22" fill="#D9985A" {s()}/>'
    + "".join(f'<path d="M{x} 62 Q{x + 2} 80 {x} 98" fill="none" stroke="{DB}" stroke-width="3"/>' for x in (48, 58))
    + f'<circle cx="54" cy="48" r="20" fill="#D9985A" {s()}/><circle cx="38" cy="32" r="6" fill="#D9985A" {W(2.4)}/><circle cx="70" cy="32" r="6" fill="#D9985A" {W(2.4)}/>'
    f'<path d="M44 52 Q54 62 64 52 Q58 64 54 64 Q50 64 44 52Z" fill="#F2E2C8"/>' + f(54, 48, d=8, k=0.7)
    + f'<ellipse cx="54" cy="70" rx="9" ry="7" fill="{BR}" {W(2.2)}/><path d="M48 66 Q54 60 60 66" fill="none" {W(2)}/>' + sp((24, 26, 5), (100, 22, 5)))

# ===================== Игрушки и аттракционы =====================
I["integratsiya-sayanskaya"] = ("purple", "пружинка-радуга (слинки)",
    "".join(f'<ellipse cx="{30 + i * 7}" cy="{86 - 34 * _m.sin(_m.pi * i / 9):.1f}" rx="16" ry="8" fill="none" stroke="{c}" stroke-width="5"/>'
            for i, c in enumerate([R, OR, Y, G, TE, B, V, P, R, OR]))
    + f'<rect x="18" y="96" width="92" height="10" rx="5" fill="#fff" {W(2.4)}/>' + f(64, 56, d=8, k=0.7) + sp((20, 30, 6), (108, 30, 5)))
I["krokha-izmailovo"] = ("pink", "карусель-чашки",
    f'<ellipse cx="64" cy="104" rx="52" ry="12" fill="{Y}" {s()}/>'
    + "".join(
        f'<path d="M{x - 16} {y} H{x + 16} Q{x + 14} {y + 20} {x} {y + 20} Q{x - 14} {y + 20} {x - 16} {y}Z" fill="{c}" {s()}/>'
        f'<path d="M{x + 16} {y + 4} q8 2 2 10" fill="none" stroke="{c}" stroke-width="4"/><ellipse cx="{x}" cy="{y}" rx="16" ry="4" fill="#fff" {W(2)}/>'
        for x, y, c in [(34, 70, B), (94, 70, G), (64, 80, R)])
    + f(64, 92, d=6, k=0.6) + f'<path d="M64 20 V60" {W(3)}/><path d="M40 34 Q64 10 88 34Z" fill="{V}" {s()}/>'
    f'<circle cx="64" cy="18" r="4" fill="{Y}" {W(2)}/>' + sp((20, 30, 5), (108, 30, 6)))
I["juna-life-aqua"] = ("teal", "водяной пистолет",
    f'<path d="M24 54 H92 Q100 54 100 62 V66 H24Z" fill="{OR}" {s()}/><rect x="98" y="58" width="12" height="6" rx="2" fill="{Y}" {W(2.2)}/>'
    f'<rect x="40" y="30" width="34" height="22" rx="10" fill="#7FD3F7" {s()}/><path d="M44 42 Q57 36 70 42 V48 H44Z" fill="#5CB7F2"/>'
    f'<path d="M30 66 L24 104 H44 L50 66Z" fill="{OR}" {s()}/><path d="M56 66 Q56 80 66 78" fill="none" {W(3)}/>'
    + f(70, 60, d=6, k=0.6)
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#7FD3F7" {W(1.8)}/>' for x, y, r in [(114, 72, 4), (118, 84, 3.4), (110, 94, 4.6), (120, 102, 3)])
    + sp((20, 26, 6)))
I["sad-budushchego"] = ("yellow", "садовая тачка",
    GROUND + f'<path d="M24 58 H92 L82 86 H34Z" fill="{G}" {s()}/><path d="M28 58 Q40 40 56 50 Q64 32 78 48 Q90 42 92 58Z" fill="#8A5A3C" {W(2.4)}/>'
    f'<path d="M48 44 V30 M48 34 Q40 26 36 32 M48 34 Q56 24 60 30" fill="none" stroke="{DG}" stroke-width="3" stroke-linecap="round"/>'
    f'<path d="M92 62 L118 46" {W(4)}/><path d="M40 86 L36 102 M74 86 L80 100" {W(4)}/>'
    f'<circle cx="58" cy="98" r="11" fill="{GR}" {s()}/><circle cx="58" cy="98" r="4" fill="#fff" {W(2)}/>' + f(58, 70, d=7, k=0.7))
I["bibirevo-ethno-village"] = ("green", "телега с сеном",
    GROUND + f'<path d="M20 70 Q30 34 64 32 Q98 34 108 70Z" fill="#F0D060" {s()}/>'
    + "".join(f'<path d="M{x} 66 Q{x + 4} 50 {x + 2} 40" fill="none" stroke="#C8A030" stroke-width="2.2"/>' for x in range(30, 104, 12))
    + f'<rect x="16" y="68" width="96" height="16" rx="3" fill="{BR}" {s()}/><path d="M112 76 H124" {W(4)}/>'
    + "".join(f'<circle cx="{x}" cy="96" r="13" fill="{DB}" {s()}/><circle cx="{x}" cy="96" r="4" fill="{Y}" {W(2)}/>'
              f'<path d="M{x - 9} 96 H{x + 9} M{x} 87 V105" stroke="{Y}" stroke-width="2.4"/>' for x in (36, 92))
    + f(64, 54, d=8, k=0.7) + sp((108, 24, 5)))

# ===================== Природа, растения, космос =====================
I["time-clock-museum"] = ("yellow", "солнечные часы",
    f'<path d="M20 100 Q64 88 108 100 V128 H20Z" fill="{G}" {W(2.6)}/>'
    f'<path d="M50 100 L54 76 H74 L78 100Z" fill="{GR}" {s()}/>'
    f'<ellipse cx="64" cy="72" rx="44" ry="14" fill="#E8E2C8" {s()}/>'
    + "".join(f'<path d="M{64 + 34 * _m.cos(a):.0f} {72 + 10 * _m.sin(a):.0f} L{64 + 40 * _m.cos(a):.0f} {72 + 12 * _m.sin(a):.0f}" {W(2.4)}/>'
              for a in [_m.pi * i / 6 for i in range(12)])
    + f'<path d="M64 72 L64 34 L88 72Z" fill="{OR}" {W(2.6)}/><path d="M64 72 L30 80" stroke="#7A6E9A" stroke-width="5" stroke-linecap="round" opacity=".6"/>'
    + f'<circle cx="24" cy="26" r="12" fill="{Y}" {W(2.4)}/>' + f(64, 86, d=6, k=0.6))
I["streltsy-chambers"] = ("orange", "лук и стрелы",
    f'<path d="M40 14 Q96 64 40 114" fill="none" stroke="{BR}" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M40 14 Q96 64 40 114" fill="none" {W(2.4)}/><path d="M40 14 L40 114" stroke="#fff" stroke-width="2.4"/>'
    f'<path d="M20 64 H108" {W(4)}/><path d="M108 64 L96 56 V72Z" fill="{GR}" {W(2.4)}/>'
    f'<path d="M20 64 L12 56 M20 64 L12 72 M26 64 L18 56 M26 64 L18 72" stroke="{R}" stroke-width="4" stroke-linecap="round"/>'
    + f(70, 40, d=6, k=0.6) + f'<path d="M86 96 L118 84 M92 106 L120 98" {W(3)}/><path d="M118 84 l-8 -2 l3 7Z M120 98 l-8 -2 l3 7Z" fill="{GR}" {W(1.8)}/>'
    + sp((22, 26, 6)))
I["vasiliev-museum"] = ("sky", "камень на распутье",
    f'<path d="M0 108 Q64 96 128 108 V128 H0Z" fill="{G}" {W(2.6)}/>'
    f'<path d="M64 128 L58 106 M64 106 L20 128 M64 106 L108 128" stroke="#E8C87A" stroke-width="10" stroke-linecap="round"/>'
    f'<path d="M30 104 Q26 52 64 40 Q102 52 98 104Z" fill="#B0AFC4" {s()}/>'
    f'<path d="M44 62 H84 M44 72 H78 M44 82 H82" stroke="#6A6A88" stroke-width="3" stroke-linecap="round"/>'
    + f(64, 92, d=7, k=0.6) + f'<path d="M96 28 L104 18 L108 30Z" fill="{NV}"/><path d="M100 24 Q112 20 116 28" fill="none" {W(2)}/>'
    + sp((20, 30, 6)))
I["rublev-museum"] = ("purple", "цветок колокольчик (кампанула)",
    stem(64, 128, 60, 30, 4) + leaf(48, 108, -40) + leaf(76, 100, 40)
    + "".join(f'<path d="M{x - 13} {y + 22} Q{x - 12} {y} {x} {y} Q{x + 12} {y} {x + 13} {y + 22} L{x + 8} {y + 18} L{x + 4} {y + 24} L{x} {y + 18} L{x - 4} {y + 24} L{x - 8} {y + 18}Z" fill="#7A8CF0" {s()}/>'
              f'<path d="M{x} {y} Q{x} {y - 8} {sx} {sy}" fill="none" stroke="{DG}" stroke-width="3"/>'
              for x, y, sx, sy in [(38, 44, 58, 36), (88, 58, 62, 50), (50, 76, 60, 66)])
    + f(38, 58, d=5, k=0.5) + f(88, 72, d=5, k=0.5) + f(50, 90, d=5, k=0.5) + sp((104, 26, 6)))
I["oz-city-park"] = ("blue", "василёк",
    stem(64, 128, 64, 66, 5) + leaf(48, 106, -30, 14, 4, DG) + leaf(80, 96, 30, 14, 4, DG)
    + "".join(f'<path d="M64 58 L{64 + 34 * _m.cos(a - .18):.0f} {58 + 34 * _m.sin(a - .18):.0f} L{64 + 40 * _m.cos(a):.0f} {58 + 40 * _m.sin(a):.0f} L{64 + 34 * _m.cos(a + .18):.0f} {58 + 34 * _m.sin(a + .18):.0f}Z" fill="#4A6CE8" {W(2.2)}/>'
              for a in [2 * _m.pi * i / 10 for i in range(10)])
    + f'<circle cx="64" cy="58" r="15" fill="#3E4AA0" {s()}/>' + "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="#fff"/>' for x, y in [(58, 50), (70, 50)])
    + f(64, 60, d=6, k=0.6))
I["park-30-pobedy"] = ("teal", "плакучая ива",
    WATER + f'<path d="M58 100 Q60 70 56 50 H72 Q68 70 70 100Z" fill="{BR}" {s()}/>'
    f'<path d="M20 70 Q16 20 64 16 Q112 20 108 70" fill="#9AD86A" {s()}/>'
    + "".join(f'<path d="M{x} 30 Q{x + (6 if x > 64 else -6)} 70 {x + (4 if x > 64 else -4)} {88 + (x % 7)}" fill="none" stroke="{DG}" stroke-width="4" stroke-linecap="round"/>'
              for x in range(28, 104, 10))
    + f(64, 40, d=7, k=0.65))
I["park-40-pobedy-zelenograd"] = ("green", "цветок мак",
    stem(64, 128, 62, 66, 5) + leaf(46, 108, -35, 13, 5, DG) + leaf(80, 100, 35, 13, 5, DG)
    + petals(62, 56, 4, 20, 22, 14, [R, "#F04A3A"], 45)
    + f'<circle cx="62" cy="56" r="11" fill="{NV}" {s()}/>' + "".join(f'<path d="M62 56 L{62 + 9 * _m.cos(a):.0f} {56 + 9 * _m.sin(a):.0f}" stroke="#fff" stroke-width="1.6"/>' for a in [_m.pi * i / 3 for i in range(6)])
    + f(62, 82, d=6, k=0.6) + sp((22, 26, 6), (106, 24, 5)))
I["severnye-dubki"] = ("yellow", "кузнечик",
    f'<path d="M6 108 Q64 98 122 108" fill="none" stroke="{DG}" stroke-width="6"/>'
    f'<path d="M30 74 Q56 58 92 64 Q100 74 90 82 Q56 88 30 74Z" fill="#7CD26E" {s()}/>'
    f'<path d="M40 70 Q66 52 90 62" fill="#5DBB63" {W(2.2)}/>'
    f'<path d="M58 80 L84 40 L94 104" fill="none" stroke="#5DBB63" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>'
    f'<path d="M58 80 L84 40 L94 104" fill="none" {W(2)}/><path d="M40 82 L36 104 M48 84 L50 104" stroke="#5DBB63" stroke-width="4" stroke-linecap="round"/>'
    f'<circle cx="98" cy="66" r="13" fill="#8EE07A" {s()}/>' + f(100, 66, d=5, k=0.55)
    + f'<path d="M100 54 Q104 30 120 22 M94 56 Q90 30 100 14" fill="none" {W(2.4)}/>' + sp((20, 30, 6)))
I["tyufeleva-roshcha"] = ("teal", "рогоз (камыш)",
    WATER + "".join(stem(x, 112, x + dx, 40 + h, 4) for x, dx, h in [(40, -6, 4), (64, 0, -10), (88, 6, 2)])
    + "".join(f'<rect x="{x - 7}" y="{y}" width="14" height="30" rx="7" fill="{BR}" {s()}/><path d="M{x} {y} V{y - 10}" {W(2.4)}/>'
              for x, y in [(34, 40), (64, 26), (94, 38)])
    + leaf(26, 80, -60, 18, 4, DG) + leaf(104, 78, 60, 18, 4, DG) + f(64, 44, d=5, k=0.5) + sp((108, 18, 5)))
I["borovik-park"] = ("sky", "подснежник",
    f'<path d="M0 104 Q64 94 128 104 V128 H0Z" fill="#fff" {W(2.6)}/>'
    + stem(64, 112, 70, 36, 4) + leaf(52, 96, -70, 18, 5, G) + leaf(80, 98, 70, 18, 5, G)
    + f'<path d="M70 36 Q76 34 80 40" fill="none" stroke="{DG}" stroke-width="4"/>'
    f'<path d="M66 44 Q60 70 76 80 Q90 70 84 44 Q76 38 66 44Z" fill="#fff" {s()}/>'
    f'<path d="M72 46 Q70 66 76 76 Q82 66 80 46Z" fill="#E8F4FF" {W(2)}/><path d="M74 76 L76 82 L78 76" fill="{G}"/>'
    + f(76, 62, d=5, k=0.5) + sp((24, 30, 6), (30, 60, 4), (108, 26, 5)))
I["shkuleva-park"] = ("purple", "кустик черники",
    GROUND + "".join(stem(64, 108, x, y, 3) for x, y in [(34, 54), (64, 34), (94, 52), (46, 80), (84, 78)])
    + "".join(leaf(x, y, r, 9, 5, G) for x, y, r in [(30, 46, -30), (60, 28, 0), (98, 44, 30), (40, 72, -20), (90, 70, 20), (74, 40, 40)])
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#4A4AA8" {s()}/><circle cx="{x - r / 3:.0f}" cy="{y - r / 3:.0f}" r="1.6" fill="#fff"/>'
              for x, y, r in [(44, 60, 8), (58, 70, 7), (78, 62, 9), (68, 88, 8), (88, 90, 6), (40, 92, 7)])
    + f(78, 63, d=5, k=0.5))
I["raduga-park"] = ("blue", "ветка рябины",
    f'<path d="M110 20 Q70 40 34 96" fill="none" stroke="{BR}" stroke-width="5" stroke-linecap="round"/>'
    + "".join(leaf(x, y, r, 11, 4.5, G) for x, y, r in [(96, 22, -20), (106, 40, 60), (82, 38, -10), (92, 54, 60), (68, 58, -20), (78, 72, 60)])
    + "".join(f'<circle cx="{x}" cy="{y}" r="7" fill="{R}" {W(2.2)}/>' for x, y in [(34, 76), (48, 78), (40, 90), (26, 90), (54, 92), (34, 104), (48, 104)])
    + f(40, 90, d=4, k=0.45) + sp((22, 30, 6), (100, 100, 5)))
I["berezovaya-roshcha"] = ("green", "берёза",
    GROUND + f'<path d="M56 112 Q58 70 54 40 H72 Q68 70 72 112Z" fill="#fff" {s()}/>'
    + "".join(f'<path d="M{x} {y} h{w}" stroke="{NV}" stroke-width="3" stroke-linecap="round"/>' for x, y, w in [(56, 50, 6), (64, 62, 6), (57, 76, 7), (64, 90, 6), (58, 102, 5)])
    + f'<path d="M64 44 Q34 40 26 64 M64 40 Q96 30 104 56" fill="none" {W(2.6)}/>'
    + "".join(f'<path d="M{x} {y} q6 -8 0 -14 q-6 6 0 14Z" fill="{c}" {W(1.8)}/>' for x, y, c in
              [(30, 30, "#9AD86A"), (44, 22, Y), (60, 14, "#9AD86A"), (76, 18, Y), (92, 24, "#9AD86A"), (102, 40, Y), (22, 48, Y), (38, 46, "#9AD86A"), (86, 42, Y), (108, 60, "#9AD86A"), (26, 66, "#9AD86A")])
    + f(64, 80, d=6, k=0.6))

if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        bg, subj, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(bg, body))
    print("svg:", len(ids))
