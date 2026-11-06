"""Иконки робота fun (2026-11-06, день): 45 новых сюжетов — игрушки, животные, сказочные персонажи, транспорт,
космос; для музеев — главный экспонат. Сверено с icons-catalog/sheet-*.png и icons-src/subjects.txt.
Запуск: python3 tools/icons_fun_1106c.py [id ...]"""
import os, sys
from draw_icons import svg, s, eye, face, sparkle, O
W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=9, k=0.75, **kw: face(cx, cy, d=d, k=k, **kw)
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
R, OR, Y, G, B, P, V, BR, WH, GR = ("#E8654F", "#FF9A3D", "#FFD25E", "#7CD26E", "#5CB7F2", "#FF8FB8", "#A98BF0",
                                    "#C0732E", "#FFFFFF", "#B8BCCB")
DG, SK, TE, DB, NV, GO = "#4E9A5A", "#FFD9B8", "#5CCDBA", "#8A5A3C", "#2B2A44", "#F2B632"
sp = lambda *pts: "".join(sparkle(x, y, r) for x, y, r in pts)
GROUND = f'<path d="M0 104 Q64 92 128 104 V128 H0Z" fill="{G}" {W(2.6)}/>'
WATER = f'<path d="M0 100 Q16 92 32 100 T64 100 T96 100 T128 100 V128 H0Z" fill="#7FD3F7" {W(2.6)}/>'


def kid(cx, cy, r=14, skin=SK):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{skin}" {s()}/>' + f(cx, cy + 1, d=r * 0.38, k=r / 22)


def px(x0, y0, cell, rows, pal, stroke=True):
    """Пиксель-арт: rows — строки символов, pal — {символ: цвет}; '.' — пусто."""
    o = ""
    for j, row in enumerate(rows):
        for i, ch in enumerate(row):
            if ch in pal:
                o += (f'<rect x="{x0 + i * cell}" y="{y0 + j * cell}" width="{cell}" height="{cell}" fill="{pal[ch]}"'
                      + (f' {W(1.6)}' if stroke else '') + '/>')
    return o


def floor(c=("#FF5FA2", "#5CE1E6", "#FFE45E", "#8B7CF6")):
    """светящийся пол из плиток внизу иконки"""
    o = ""
    for j, y in enumerate((96, 110)):
        for i in range(7):
            o += f'<rect x="{8 + i * 16}" y="{y}" width="15" height="13" rx="2" fill="{c[(i + j) % 4]}" {W(1.8)}/>'
    return o


I = {}
# ===================== Сергиев Посад =====================
I["sp-kukhmisterskaya"] = ("orange", "леденец-петушок на палочке",
    f'<path d="M60 98 L56 124" stroke="#F3E3C8" stroke-width="8" stroke-linecap="round"/><path d="M60 98 L56 124" {W(2)}/>'
    f'<path d="M40 40 Q42 24 52 30 Q54 18 62 26 Q68 18 70 32 Q66 40 58 40Z" fill="#D8322A" {W(2.4)}/>'
    f'<path d="M34 98 Q22 66 38 50 Q50 38 64 44 Q74 50 72 64 Q86 52 98 30 Q114 46 106 74 Q100 96 72 100Z" fill="{R}" {s()}/>'
    f'<path d="M92 36 Q100 54 92 74 M100 40 Q108 58 100 80" fill="none" stroke="#B8402F" stroke-width="2.6"/>'
    f'<path d="M30 54 L18 58 L30 62Z" fill="{Y}" {W(2.2)}/><path d="M34 64 Q30 72 36 74" fill="#D8322A" {W(2)}/>'
    + f(52, 58, d=7, k=0.75)
    + f'<path d="M44 84 Q60 92 80 84" fill="none" stroke="#fff" stroke-width="3" opacity=".6"/>'
    + sp((20, 30, 6), (110, 104, 5)))
I["sp-soviet-childhood"] = ("blue", "пионерский горн с красным вымпелом",
    f'<path d="M30 74 L84 44 L100 26 Q112 40 108 70 Q96 66 86 60 L34 84Z" fill="{GO}" {s()}/>'
    f'<ellipse cx="104" cy="48" rx="8" ry="22" fill="#FFE07A" {s()} transform="rotate(20 104 48)"/>'
    f'<rect x="18" y="74" width="18" height="12" rx="4" fill="{GO}" {s()} transform="rotate(-28 27 80)"/>'
    f'<path d="M52 72 L48 112 L72 100 L86 108 L76 66Z" fill="{R}" {s()}/>'
    f'<path d="M58 84 l3 6 l6 1 l-5 4 l1 6 l-5 -3 l-6 3 l1 -6 l-4 -4 l6 -1Z" fill="{Y}" {W(1.2)}/>'
    + f(66, 56, d=7, k=0.6)
    + "".join(f'<path d="M{x} {y} q6 -6 12 -4" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' for x, y in [(104, 14), (114, 24)])
    + sp((22, 30, 6), (30, 108, 4)))
I["sp-craft-house"] = ("yellow", "катушка ниток с иголкой",
    f'<rect x="30" y="26" width="68" height="12" rx="4" fill="{DB}" {s()}/><rect x="30" y="92" width="68" height="12" rx="4" fill="{DB}" {s()}/>'
    f'<rect x="38" y="38" width="52" height="54" fill="{R}" {s()}/>'
    + "".join(f'<path d="M38 {y} Q64 {y + 4} 90 {y}" fill="none" stroke="#B8463A" stroke-width="2"/>' for y in (46, 56, 76, 86))
    + f(64, 64, d=9, k=0.8)
    + f'<path d="M90 70 Q112 76 104 100 Q98 114 84 112" fill="none" stroke="{R}" stroke-width="3"/>'
    f'<path d="M98 18 L80 52" stroke="{GR}" stroke-width="4" stroke-linecap="round"/><path d="M98 18 L80 52" {W(1.6)}/>'
    f'<ellipse cx="96" cy="22" rx="1.6" ry="3" fill="#fff" {W(1.2)} transform="rotate(28 96 22)"/>' + sp((20, 60, 5)))
I["sp-matryoshka-museum"] = ("pink", "матрёшка открылась — внутри малышка, рядом кисточка",
    f'<path d="M24 76 Q24 52 40 50 Q34 36 46 28 Q58 22 66 32 Q74 42 66 52 Q80 56 80 78 Q80 110 52 110 Q24 110 24 76Z" fill="{R}" {s()}/>'
    f'<circle cx="52" cy="42" r="12" fill="{SK}" {W(2.4)}/>' + f(52, 43, d=5, k=0.5)
    + f'<path d="M36 82 Q52 70 68 82 Q60 100 52 100 Q42 100 36 82Z" fill="{Y}" {W(2.2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="{R}" {W(1.6)}/>' for x, y in [(46, 86), (58, 86), (52, 94)])
    + f'<path d="M80 74 Q86 60 98 60 Q110 60 110 76 Q110 98 96 98 Q82 98 80 74Z" fill="{Y}" {s()}/><circle cx="96" cy="70" r="7" fill="{SK}" {W(2)}/>'
    + f(96, 71, d=3, k=0.32)
    + f'<path d="M100 14 L84 44" stroke="{DB}" stroke-width="5" stroke-linecap="round"/><path d="M84 44 Q80 52 86 54 Q90 50 88 44Z" fill="{B}" {W(2)}/>'
    + sp((112, 30, 5)))
I["sp-park-chudes"] = ("sky", "цепочная карусель-вертушка",
    GROUND + f'<rect x="60" y="40" width="8" height="64" fill="{GR}" {s()}/>'
    f'<path d="M28 48 Q64 14 100 48Z" fill="{R}" {s()}/><path d="M46 36 Q64 22 82 36" fill="none" stroke="#fff" stroke-width="3"/>'
    f'<circle cx="64" cy="20" r="5" fill="{Y}" {W(2)}/>'
    + "".join(f'<path d="M{x} 48 L{x2} 76" stroke="{O}" stroke-width="2"/><rect x="{x2 - 8}" y="76" width="16" height="7" rx="3" fill="{c}" {W(2)}/>'
              + f'<circle cx="{x2}" cy="70" r="6" fill="{SK}" {W(1.8)}/>'
              for x, x2, c in [(34, 18, Y), (52, 44, B), (76, 84, G), (94, 110, P)])
    + f(64, 34, d=6, k=0.55) + sp((20, 24, 5), (108, 22, 5)))

# ===================== Коломна =====================
I["kolomna-pastila-factory"] = ("green", "яблочко в поварском колпаке",
    f'<path d="M64 46 Q40 32 26 54 Q16 84 40 106 Q52 114 64 108 Q76 114 88 106 Q112 84 102 54 Q88 32 64 46Z" fill="{G}" {s()}/>'
    f'<path d="M64 46 Q60 38 62 32" fill="none" stroke="{DB}" stroke-width="4" stroke-linecap="round"/>'
    + f(64, 76, d=11, k=0.95)
    + f'<path d="M40 40 Q34 22 50 22 Q54 8 66 14 Q78 6 84 20 Q98 20 90 40Z" fill="#fff" {s()}/><rect x="42" y="36" width="46" height="9" rx="3" fill="#fff" {s()}/>'
    + sp((20, 30, 5), (110, 34, 5)))
I["kolomna-10-zaytsev"] = ("orange", "зайчик с печатным пряником",
    f'<path d="M48 40 Q40 6 50 6 Q60 8 58 40Z M70 40 Q72 6 82 8 Q90 12 78 42Z" fill="#EDE6F3" {s()}/>'
    f'<path d="M52 36 Q48 16 52 12 M74 38 Q78 16 82 14" stroke="{P}" stroke-width="4" fill="none" stroke-linecap="round"/>'
    f'<ellipse cx="64" cy="94" rx="26" ry="24" fill="#EDE6F3" {s()}/><circle cx="64" cy="56" r="22" fill="#EDE6F3" {s()}/>'
    + f(64, 56, d=8, k=0.8) + f'<path d="M62 62 h4" {W(2.4)}/>'
    + f'<rect x="38" y="78" width="52" height="36" rx="8" fill="{BR}" {s()}/><rect x="44" y="84" width="40" height="24" rx="5" fill="none" stroke="#FFE2B8" stroke-width="2.4"/>'
    f'<path d="M54 96 l10 -8 l10 8 l-10 8Z" fill="none" stroke="#FFE2B8" stroke-width="2.4"/>'
    + f'<ellipse cx="38" cy="90" rx="7" ry="6" fill="#EDE6F3" {W(2.2)}/><ellipse cx="90" cy="90" rx="7" ry="6" fill="#EDE6F3" {W(2.2)}/>')
I["kolomna-shvedov"] = ("pink", "кремовый торт с подкрученными усами кондитера",
    f'<rect x="26" y="66" width="76" height="40" rx="8" fill="{P}" {s()}/><rect x="36" y="44" width="56" height="26" rx="6" fill="#FFF3E0" {s()}/>'
    f'<path d="M26 80 Q36 90 46 80 Q56 90 66 80 Q76 90 86 80 Q96 90 102 80" fill="none" stroke="#fff" stroke-width="4"/>'
    + "".join(f'<circle cx="{x}" cy="42" r="6" fill="#fff" {W(2)}/>' for x in (44, 56, 72, 84))
    + f'<circle cx="64" cy="34" r="7" fill="{R}" {W(2.2)}/>'
    + f(64, 88, d=10, k=0.8, mouth=False)
    + f'<path d="M64 96 Q54 92 46 98 Q40 92 44 88 M64 96 Q74 92 82 98 Q88 92 84 88" fill="none" stroke="{NV}" stroke-width="3.6" stroke-linecap="round"/>'
    + sp((20, 30, 6), (108, 30, 5)))
I["kolomna-toy-museum"] = ("purple", "заводная обезьянка с тарелками",
    f'<circle cx="64" cy="52" r="24" fill="{BR}" {s()}/><circle cx="38" cy="50" r="8" fill="{BR}" {W(2.6)}/><circle cx="90" cy="50" r="8" fill="{BR}" {W(2.6)}/>'
    f'<ellipse cx="64" cy="58" rx="15" ry="13" fill="#F3C9A0" {W(2.4)}/>' + f(64, 52, d=8, k=0.75)
    + f'<rect x="44" y="74" width="40" height="34" rx="10" fill="{R}" {s()}/><rect x="44" y="88" width="40" height="6" fill="{Y}" {W(2)}/>'
    f'<ellipse cx="24" cy="80" rx="12" ry="5" fill="{GO}" {s()} transform="rotate(-60 24 80)"/>'
    f'<ellipse cx="104" cy="80" rx="12" ry="5" fill="{GO}" {s()} transform="rotate(60 104 80)"/>'
    f'<path d="M44 80 L30 80 M84 80 L98 80" stroke="{BR}" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M84 98 h12 M96 92 v12 M92 92 h8 M92 104 h8" stroke="{GR}" stroke-width="4" stroke-linecap="round"/>'
    f'<rect x="54" y="28" width="20" height="8" rx="3" fill="{R}" {W(2)}/>' + sp((22, 24, 6), (108, 30, 5)))
I["kolomna-samovar"] = ("yellow", "самовар раздувают сапогом",
    f'<rect x="46" y="100" width="36" height="8" fill="{DB}" {W(2.4)}/><path d="M38 114 L46 106 H82 L90 114Z" fill="{DB}" {W(2.4)}/>'
    f'<ellipse cx="64" cy="72" rx="36" ry="32" fill="{GO}" {s()}/><rect x="40" y="38" width="48" height="10" rx="4" fill="{GO}" {s()}/>'
    f'<path d="M28 62 Q14 62 16 80 Q18 86 26 84 M100 62 Q114 62 112 80 Q110 86 102 84" fill="none" {W(4)}/>'
    f'<path d="M50 94 H34 V102" fill="none" stroke="{DB}" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M36 70 Q64 80 92 70" fill="none" stroke="#FFE7A0" stroke-width="3"/>'
    + f(64, 70, d=10, k=0.85)
    + f'<rect x="58" y="26" width="12" height="14" fill="{GR}" {W(2.4)}/>'
    f'<path d="M58 26 L60 6 H74 L72 18 Q86 18 88 26Z" fill="{NV}" {s()}/>'
    f'<path d="M92 10 q6 -4 10 0 M96 20 q6 -4 10 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    + sp((20, 30, 6)))
I["kolomna-kuznechnaya"] = ("orange", "наковальня с молотом",
    f'<path d="M18 52 H96 Q112 52 112 40 Q100 44 92 40 H30 Q22 40 18 52Z" fill="#6E7389" {s()}/>'
    f'<path d="M30 52 H96 V64 Q80 66 78 76 H48 Q46 66 30 64Z" fill="#6E7389" {s()}/><rect x="40" y="76" width="46" height="12" fill="#6E7389" {s()}/>'
    f'<path d="M30 88 H96 L104 108 H22Z" fill="{DB}" {s()}/>'
    + f(64, 62, d=9, k=0.8)
    + f'<rect x="72" y="8" width="30" height="16" rx="3" fill="{GR}" {s()} transform="rotate(25 86 16)"/>'
    f'<path d="M80 22 L66 40" stroke="{BR}" stroke-width="6" stroke-linecap="round"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="{Y}"/>' for x, y in [(44, 32), (36, 26), (52, 24), (28, 34)]))
I["kolomna-patefon"] = ("blue", "патефон-чемоданчик с поющей птичкой",
    f'<rect x="18" y="60" width="92" height="44" rx="8" fill="#B5432F" {s()}/><path d="M18 60 L30 26 H98 L110 60Z" fill="#D86A50" {s()}/>'
    f'<ellipse cx="62" cy="64" rx="34" ry="9" fill="{NV}" {W(2.4)}/><ellipse cx="62" cy="64" rx="8" ry="3" fill="{R}"/>'
    f'<path d="M98 62 L82 56" stroke="{GR}" stroke-width="4" stroke-linecap="round"/>'
    + f(64, 84, d=10, k=0.8)
    + f'<rect x="56" y="102" width="16" height="6" rx="2" fill="{GO}" {W(2)}/>'
    + f'<ellipse cx="96" cy="22" rx="11" ry="9" fill="{Y}" {W(2.4)}/><path d="M106 20 l8 2 l-8 3Z" fill="{OR}" {W(1.6)}/>'
    + eye(98, 19, 0.5) + f'<path d="M24 30 q4 -10 8 -2 v-10" fill="none" {W(2.4)}/><circle cx="23" cy="31" r="3" fill="{O}"/>')

# ===================== Серпухов, Зарайск, Пушкино =====================
I["serpukhov-peacock-museum"] = ("teal", "павлинье перо рисует кисточкой",
    f'<path d="M40 120 Q52 70 66 30" fill="none" stroke="{DG}" stroke-width="4"/>'
    + "".join(f'<path d="M{48 + i * 4} {100 - i * 14} q-{18 - i} -8 -{22 - i} -2 M{50 + i * 4} {96 - i * 14} q{16 - i} -10 {22 - i} -6" fill="none" stroke="{TE}" stroke-width="3"/>' for i in range(4))
    + f'<ellipse cx="66" cy="40" rx="28" ry="32" fill="{TE}" {s()}/><ellipse cx="66" cy="40" rx="18" ry="21" fill="{GO}" {W(2.4)}/>'
    f'<ellipse cx="66" cy="42" rx="11" ry="13" fill="#3E4AA0" {W(2.4)}/>' + f(66, 42, d=5, k=0.5)
    + f'<path d="M110 70 L92 94" stroke="{DB}" stroke-width="5" stroke-linecap="round"/><path d="M92 94 Q86 104 94 106 Q98 100 96 94Z" fill="{R}" {W(2)}/>'
    + sp((20, 30, 5), (108, 22, 5)))
I["serpukhov-dolls"] = ("pink", "кукла с бантом и рожком мороженого",
    f'<path d="M36 112 Q40 76 64 74 Q88 76 92 112Z" fill="{V}" {s()}/><path d="M44 112 L50 92 M84 112 L78 92" stroke="#fff" stroke-width="3"/>'
    f'<circle cx="64" cy="50" r="24" fill="{SK}" {s()}/><path d="M40 50 Q38 22 64 22 Q90 22 88 50 Q80 34 64 36 Q48 34 40 50Z" fill="#E8A040" {s()}/>'
    f'<path d="M64 24 L46 12 L48 30Z M64 24 L82 12 L80 30Z" fill="{P}" {W(2.4)}/><circle cx="64" cy="24" r="4" fill="{R}" {W(2)}/>'
    + f(64, 54, d=8, k=0.75)
    + f'<path d="M96 76 L104 106 L112 76Z" fill="#E8B86A" {W(2.4)}/><circle cx="104" cy="70" r="9" fill="{P}" {W(2.4)}/><circle cx="104" cy="60" r="7" fill="#FFF3E0" {W(2.2)}/>'
    f'<path d="M88 90 L98 84" stroke="{SK}" stroke-width="6" stroke-linecap="round"/>' + sp((20, 30, 5)))
I["serpukhov-history-museum"] = ("yellow", "портрет усатого купца в золотой раме",
    f'<rect x="22" y="18" width="84" height="94" rx="6" fill="{GO}" {s()}/><rect x="32" y="28" width="64" height="74" fill="#7FB8E8" {W(2.4)}/>'
    f'<path d="M36 102 Q40 76 64 74 Q88 76 92 102Z" fill="{NV}" {W(2.4)}/>'
    f'<circle cx="64" cy="56" r="17" fill="{SK}" {W(2.6)}/><path d="M46 46 Q48 32 64 32 Q80 32 82 46 Q72 40 64 42 Q56 40 46 46Z" fill="{DB}" {W(2.2)}/>'
    + f(64, 54, d=6, k=0.6, mouth=False)
    + f'<path d="M64 64 Q56 60 48 66 Q50 58 56 58 M64 64 Q72 60 80 66 Q78 58 72 58" fill="{DB}" {W(2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#FFF3A0"/>' for x, y in [(22, 18), (106, 18), (22, 112), (106, 112)]))
I["russian-ostrich-farm"] = ("green", "эму с морковкой",
    GROUND + f'<path d="M52 104 L48 122 M74 104 L78 122" stroke="{OR}" stroke-width="5" stroke-linecap="round"/>'
    f'<ellipse cx="62" cy="86" rx="34" ry="22" fill="#8A7360" {s()}/>'
    + "".join(f'<path d="M{x} {y} q6 6 12 0" fill="none" stroke="#6A5545" stroke-width="2.4"/>' for x, y in [(40, 84), (56, 92), (70, 82), (52, 76)])
    + f'<path d="M80 74 Q86 50 80 30" fill="none" stroke="#7FA6D8" stroke-width="12" stroke-linecap="round"/><path d="M80 74 Q86 50 80 30" fill="none" {W(1.8)}/>'
    f'<ellipse cx="80" cy="26" rx="14" ry="12" fill="#7FA6D8" {s()}/><path d="M92 26 L106 30 L92 32Z" fill="#3B3355"/>' + f(78, 24, d=5, k=0.5)
    + f'<path d="M100 36 L116 52" stroke="{OR}" stroke-width="7" stroke-linecap="round"/><path d="M100 36 L116 52" {W(1.6)}/>'
    f'<path d="M98 34 l-4 -8 M100 34 l2 -9" stroke="{G}" stroke-width="3" stroke-linecap="round"/>' + sp((20, 24, 5)))
I["bylinkino-goat-farm"] = ("sky", "козлёнок скачет с колокольчиком",
    GROUND + f'<path d="M44 90 L36 112 M54 92 L52 114 M80 92 L84 114 M90 88 L98 108" stroke="#fff" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M44 90 L36 112 M54 92 L52 114 M80 92 L84 114 M90 88 L98 108" fill="none" stroke="{O}" stroke-width="1.6"/>'
    f'<ellipse cx="66" cy="80" rx="32" ry="18" fill="#fff" {s()}/><path d="M34 74 q-8 -6 -4 -14" fill="none" {W(3)}/>'
    f'<ellipse cx="96" cy="52" rx="15" ry="13" fill="#fff" {s()}/><path d="M88 40 q-4 -10 2 -14 M100 40 q2 -10 8 -12" fill="none" stroke="#C9A06A" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M82 50 q-10 -2 -12 4 q8 4 12 0" fill="#fff" {W(2.2)}/>' + f(98, 52, d=5, k=0.5)
    + f'<path d="M88 64 Q96 70 104 64" fill="none" stroke="{R}" stroke-width="3"/><path d="M92 68 Q96 80 100 68" fill="{GO}" {W(2)}/>'
    + sp((22, 28, 6), (40, 18, 4)))
I["zaraysk-kovrizhka"] = ("orange", "горшочек мёда с ложкой",
    f'<path d="M30 54 Q22 104 50 110 H78 Q106 104 98 54Z" fill="#D9844A" {s()}/><rect x="26" y="44" width="76" height="14" rx="6" fill="#D9844A" {s()}/>'
    f'<path d="M30 46 Q40 64 48 50 Q56 66 64 50 Q74 64 82 50 Q92 64 98 46" fill="{GO}" {W(2.4)}/>'
    + f(64, 82, d=11, k=0.9)
    + f'<rect x="36" y="94" width="56" height="10" fill="#FFF3E0" opacity=".7"/>'
    + f'<path d="M86 10 L74 50" stroke="{BR}" stroke-width="6" stroke-linecap="round"/><ellipse cx="88" cy="14" rx="9" ry="6" fill="{BR}" {W(2.2)} transform="rotate(-70 88 14)"/>'
    + sp((20, 28, 6)))
I["zaraysk-baranka"] = ("purple", "баранка в короне",
    f'<circle cx="64" cy="72" r="38" fill="#E0A055" {s()}/><circle cx="64" cy="72" r="14" fill="#C9B8FF" {s()}/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="2" ry="1.2" fill="#FFF3E0" transform="rotate({r} {x} {y})"/>' for x, y, r in [(40, 56, 30), (50, 46, 0), (80, 46, -20), (92, 62, 60), (88, 92, -40), (44, 92, 40), (34, 76, 80)])
    + f(64, 98, d=9, k=0.7)
    + f'<path d="M42 38 L40 16 L52 26 L64 12 L76 26 L88 16 L86 38Z" fill="{GO}" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="{R}" {W(1.4)}/>' for x, y in [(52, 30), (64, 28), (76, 30)])
    + sp((20, 30, 6), (108, 26, 5)))
I["syrok-museum"] = ("sky", "молочный завод: из трубы облако-молоко",
    GROUND + f'<rect x="24" y="58" width="64" height="48" fill="#fff" {s()}/><path d="M24 58 L40 46 V58 L56 46 V58 L72 46 V58" fill="#fff" {s()}/>'
    f'<rect x="84" y="34" width="16" height="72" fill="{R}" {s()}/><rect x="84" y="50" width="16" height="6" fill="#fff" {W(1.8)}/>'
    f'<rect x="36" y="86" width="16" height="20" fill="{B}" {W(2.2)}/>'
    + f(56, 74, d=8, k=0.7)
    + f'<path d="M80 30 Q74 18 88 16 Q92 4 106 10 Q120 8 118 22 Q124 32 110 32 H86 Q76 34 80 30Z" fill="#fff" {s()}/>'
    + eye(96, 22, 0.45) + eye(106, 22, 0.45) + sp((20, 30, 5)))

# ===================== Мытищи, Люберцы, Балашиха =====================
I["mytishchi-history-museum"] = ("yellow", "деревянная азбука-доска с буквой «Аз»",
    f'<path d="M24 30 H104 V100 H24Z" fill="#E6B27A" {s()}/><path d="M64 20 L64 30" {W(3)}/><circle cx="64" cy="18" r="5" fill="{BR}" {W(2)}/>'
    + "".join(f'<path d="M24 {y} H104" stroke="#C99560" stroke-width="2"/>' for y in (48, 66, 84))
    + f'<path d="M44 92 L56 42 H66 L78 92 M48 76 H74" fill="none" stroke="{R}" stroke-width="7" stroke-linejoin="round"/>'
    f'<path d="M44 92 L56 42 H66 L78 92 M48 76 H74" fill="none" {W(1.4)}/>'
    + f(92, 54, d=5, k=0.5) + f'<path d="M80 108 Q90 116 104 106" fill="none" stroke="{DB}" stroke-width="4" stroke-linecap="round"/>'
    + sp((112, 22, 5)))
I["lyubertsy-raduga-puppets"] = ("blue", "лягушонок-перчатка над ширмой с радугой",
    f'<path d="M14 92 Q64 30 114 92" fill="none" stroke="{R}" stroke-width="7"/><path d="M22 92 Q64 40 106 92" fill="none" stroke="{Y}" stroke-width="7"/>'
    f'<path d="M30 92 Q64 50 98 92" fill="none" stroke="{G}" stroke-width="7"/>'
    f'<path d="M48 92 Q44 62 64 58 Q84 62 80 92Z" fill="{G}" {s()}/><circle cx="54" cy="56" r="9" fill="{G}" {W(2.6)}/><circle cx="74" cy="56" r="9" fill="{G}" {W(2.6)}/>'
    + eye(54, 56, 0.6) + eye(74, 56, 0.6) + f'<path d="M54 74 Q64 82 74 74" fill="none" {W(2.6)}/>'
    f'<ellipse cx="50" cy="78" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/><ellipse cx="78" cy="78" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/>'
    + f'<rect x="12" y="88" width="104" height="34" rx="4" fill="{V}" {s()}/>'
    + "".join(f'<path d="M{x} 92 V120" stroke="#8A6CE0" stroke-width="3"/>' for x in (30, 50, 70, 90))
    + sp((22, 24, 5), (106, 24, 5)))
I["lyubertsy-museum"] = ("night", "собака-космонавт в шлеме",
    f'<circle cx="64" cy="64" r="36" fill="#CFE8FF" opacity=".5" {s()}/>'
    f'<path d="M40 58 Q28 50 32 78 Q38 80 42 72Z M88 58 Q100 50 96 78 Q90 80 86 72Z" fill="{BR}" {W(2.6)}/>'
    f'<ellipse cx="64" cy="66" rx="24" ry="22" fill="#fff" {s()}/><ellipse cx="64" cy="76" rx="11" ry="8" fill="#F3E3D0" {W(2.2)}/>'
    f'<ellipse cx="64" cy="71" rx="4" ry="3" fill="{O}"/>' + f(64, 62, d=8, k=0.75, mouth=False)
    + f'<path d="M58 80 Q64 86 70 80" fill="none" {W(2.4)}/>'
    + f'<path d="M30 92 Q64 112 98 92" fill="{R}" {s()}/><path d="M50 100 L64 108 L78 100" fill="none" stroke="{Y}" stroke-width="3"/>'
    + "".join(sparkle(x, y, r) for x, y, r in [(16, 30, 5), (110, 26, 6), (108, 98, 4), (22, 104, 4)]))
I["balashikha-small-puppets"] = ("purple", "белочка грызёт золотой орешек",
    f'<path d="M84 104 Q118 92 108 54 Q100 30 82 40 Q96 52 90 70 Q82 86 84 104Z" fill="{OR}" {s()}/>'
    f'<ellipse cx="58" cy="88" rx="24" ry="24" fill="{OR}" {s()}/><ellipse cx="58" cy="94" rx="13" ry="14" fill="#FFE2B8" {W(2.2)}/>'
    f'<circle cx="56" cy="52" r="20" fill="{OR}" {s()}/><path d="M42 40 L40 22 L52 34Z M70 40 L74 22 L62 34Z" fill="{OR}" {W(2.4)}/>'
    + f(56, 52, d=7, k=0.7)
    + f'<ellipse cx="58" cy="78" rx="9" ry="11" fill="{GO}" {s()}/><path d="M50 72 Q58 64 66 72" fill="#B8862A" {W(2)}/>'
    + sp((58, 76, 3), (24, 30, 6), (100, 22, 5), (22, 96, 4)))

# ===================== Москва: музеи и театры =====================
I["optical-illusions-kosygina"] = ("teal", "невозможный треугольник",
    f'<path d="M64 14 L114 100 H90 L64 54 L54 72 L42 72 Z" fill="{V}" {s()}/>'
    f'<path d="M114 100 H14 L26 80 H78 L68 62 L80 62 L90 100" fill="{Y}" {s()}/>'
    f'<path d="M14 100 L64 14 L76 34 L36 100" fill="{P}" {s()}/>'
    + f(64, 82, d=7, k=0.6) + sp((20, 24, 6), (108, 26, 5), (110, 116, 4)))
I["mkhat-museum"] = ("night", "театральный бинокль",
    f'<path d="M30 46 H58 L56 30 Q44 26 32 30Z M70 46 H98 L96 30 Q84 26 72 30Z" fill="{GO}" {s()}/>'
    f'<rect x="56" y="48" width="16" height="12" rx="4" fill="{GO}" {s()}/>'
    f'<circle cx="42" cy="74" r="24" fill="#E9D7FF" {s()}/><circle cx="86" cy="74" r="24" fill="#E9D7FF" {s()}/>'
    f'<circle cx="42" cy="74" r="15" fill="{NV}" {W(2.4)}/><circle cx="86" cy="74" r="15" fill="{NV}" {W(2.4)}/>'
    + eye(42, 74, 1.1) + eye(86, 74, 1.1)
    + f'<path d="M56 100 Q64 106 72 100" fill="none" {W(2.6)}/>'
    f'<ellipse cx="22" cy="96" rx="5" ry="3" fill="#FF7FA8" opacity=".6"/><ellipse cx="106" cy="96" rx="5" ry="3" fill="#FF7FA8" opacity=".6"/>'
    + f'<path d="M98 50 Q116 66 110 112" fill="none" stroke="{GO}" stroke-width="3"/>' + sp((20, 20, 5), (64, 18, 4)))
I["kamburova-theatre"] = ("pink", "соловей поёт на нотном стане",
    "".join(f'<path d="M8 {y} H120" stroke="{O}" stroke-width="1.8" opacity=".5"/>' for y in (86, 94, 102, 110, 118))
    + f'<ellipse cx="62" cy="62" rx="30" ry="24" fill="#B98A62" {s()}/><path d="M34 62 Q14 54 12 72 Q28 72 36 70Z" fill="#9A6E4A" {W(2.4)}/>'
    f'<ellipse cx="66" cy="70" rx="16" ry="12" fill="#F3E3D0" {W(2.2)}/>'
    f'<path d="M84 52 L100 46 L86 60Z" fill="{OR}" {W(2.2)}/>' + f(72, 52, d=6, k=0.6, mouth=False)
    + f'<path d="M54 84 L52 92 M68 84 L70 92" {W(3)}/>'
    + f'<path d="M100 30 v-16 l8 -2 v16" fill="none" {W(2.6)}/><ellipse cx="97" cy="31" rx="4" ry="3" fill="{O}"/><ellipse cx="105" cy="28" rx="4" ry="3" fill="{O}"/>'
    f'<path d="M30 30 v-14" {W(2.6)}/><ellipse cx="27" cy="31" rx="4" ry="3" fill="{O}"/>' + sp((60, 18, 5)))
I["illusion-theatre-lazo"] = ("night", "игральная карта-туз выпрыгивает с поклоном",
    f'<rect x="34" y="18" width="60" height="88" rx="8" fill="#fff" {s()} transform="rotate(-8 64 62)"/>'
    f'<path d="M64 46 Q50 32 44 44 Q40 54 64 72 Q88 54 84 44 Q78 32 64 46Z" fill="{R}" {s()} transform="rotate(-8 64 62)"/>'
    + f(62, 86, d=8, k=0.7)
    + f'<text x="38" y="38" font-family="Arial" font-weight="700" font-size="16" fill="{R}" transform="rotate(-8 64 62)">A</text>'
    f'<path d="M30 70 Q14 64 16 50 M98 66 Q114 60 112 46" fill="none" {W(3)}/>'
    + "".join(sparkle(x, y, r, Y) for x, y, r in [(18, 28, 7), (110, 30, 6), (108, 100, 5), (20, 104, 5)]))

# ===================== Пиксель-квесты =====================
PAL = {"R": R, "Y": Y, "G": G, "B": "#5CE1E6", "P": "#FF5FA2", "V": "#8B7CF6", "K": NV, "W": "#fff", "O": OR}
I["pixel-quest-kievskaya"] = ("night", "пиксельный паровозик на светящемся полу",
    floor() + px(20, 30, 8, ["...KK.....", "...KK.....", "RRRRRRRYYY", "RWWRRRRYKY", "RWWRRRRYYY", "RRRRRRRRRR",
                              ".KK..KK.KK"], PAL)
    + eye(76, 58, 0.55) + eye(90, 58, 0.55) + sp((20, 20, 4), (110, 22, 5)))
I["pixel-quest-komsomolskaya"] = ("purple", "пиксельный котик",
    floor() + px(28, 18, 8, ["Y.....Y", "YY...YY", "YYYYYYY", "YKYYYKY", "YYYPYYY", "YYYYYYY", ".YYYYY.", ".Y...Y."], PAL)
    + sp((18, 24, 5), (110, 26, 5)))
I["pixel-quest-serpukhovskaya"] = ("orange", "малыш прыгает по полу-лаве",
    "".join(f'<rect x="{8 + i * 16}" y="{y}" width="15" height="13" rx="2" fill="{c}" {W(1.8)}/>'
            for y in (96, 110) for i, c in enumerate([R, OR, "#5CE1E6", R, OR, "#5CE1E6", R]))
    + "".join(f'<path d="M{x} 96 q-4 -8 0 -14 q4 6 6 0 q4 8 0 14Z" fill="{Y}" {W(1.6)}/>' for x in (14, 62, 110))
    + f'<path d="M58 60 L42 44 M70 60 L86 44 M60 76 L48 90 M68 76 L80 88" stroke="{SK}" stroke-width="7" stroke-linecap="round"/>'
    f'<rect x="52" y="54" width="24" height="26" rx="8" fill="{B}" {s()}/>' + kid(64, 38, 14) + sp((24, 24, 5)))
I["pixel-quest-shelepikha"] = ("blue", "пиксельный кораблик",
    floor(("#5CE1E6", "#5CB7F2", "#8B7CF6", "#5CE1E6")) + px(24, 20, 8, ["....W.....", "....WW....", "....WWW...", "....WWWW..",
                                                                        "....K.....", "RRRRRRRRRR", ".RRRRRRRR.", "..RRRRRR.."], PAL)
    + eye(56, 74, 0.55) + eye(72, 74, 0.55) + sp((20, 30, 5), (108, 28, 5)))
I["pixel-quest-mari"] = ("green", "тетрис-блок прыгает в ряд",
    floor() + px(32, 26, 16, ["VVV.", ".V..", ".....", "G..YY", "GGGYY"], PAL)
    + f(56, 42, d=7, k=0.6) + sp((20, 24, 5), (106, 30, 5)))
I["pixel-quest-odintsovo"] = ("night", "пиксельный инопланетянин",
    floor() + px(20, 22, 8, ["..G.....G..", "...G...G...", "..GGGGGGG..", ".GGKGGGKGG.", "GGGGGGGGGGG", "G.GGGGGGG.G",
                              "G.G.....G.G", "...GG.GG..."], PAL)
    + sp((18, 18, 4), (112, 20, 5), (64, 12, 3)))

# ===================== Квесты =====================
I["fastum-quests"] = ("teal", "статуя моаи с острова Пасхи",
    GROUND + f'<path d="M40 104 V48 Q40 22 64 20 Q88 22 86 48 V104Z" fill="#9A9AAE" {s()}/>'
    f'<path d="M44 42 H84" {W(4)}/><path d="M62 46 Q56 66 62 74 H70" fill="none" {W(3)}/>'
    + f(64, 56, d=12, k=0.8, mouth=False) + f'<path d="M56 86 Q64 90 72 86" fill="none" {W(3)}/>'
    + f'<path d="M48 22 Q64 6 80 22 Q64 16 48 22Z" fill="{R}" {W(2.4)}/>'
    f'<path d="M100 104 Q98 70 110 60 M110 60 q-12 -4 -18 4 M110 60 q4 -12 12 -12 M110 60 q12 2 14 10" fill="none" stroke="{DG}" stroke-width="4" stroke-linecap="round"/>'
    + sp((20, 30, 5)))
I["pogruzhenie-riviera"] = ("yellow", "мешок с золотыми монетами",
    f'<path d="M44 40 Q20 70 28 100 Q34 114 64 114 Q94 114 100 100 Q108 70 84 40Z" fill="#C9A06A" {s()}/>'
    f'<path d="M44 40 Q64 48 84 40 L90 28 Q64 36 38 28Z" fill="#C9A06A" {s()}/><path d="M44 42 Q64 50 84 42" fill="none" stroke="{R}" stroke-width="4"/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="9" ry="9" fill="{GO}" {W(2.2)}/>' for x, y in [(52, 26), (66, 22), (78, 28)])
    + f(64, 80, d=11, k=0.9) + "".join(sparkle(x, y, r) for x, y, r in [(20, 30, 6), (108, 22, 5), (112, 96, 4)])
    + f'<ellipse cx="104" cy="112" rx="9" ry="5" fill="{GO}" {W(2)}/><ellipse cx="22" cy="114" rx="9" ry="5" fill="{GO}" {W(2)}/>')
I["pogruzhenie-shcherbinka"] = ("night", "сова-почтальон с конвертом",
    f'<path d="M30 70 Q14 66 12 50 Q30 52 40 62Z M98 70 Q114 66 116 50 Q98 52 88 62Z" fill="#B98A62" {W(2.6)}/>'
    f'<ellipse cx="64" cy="70" rx="30" ry="36" fill="#C99A72" {s()}/><ellipse cx="64" cy="80" rx="18" ry="20" fill="#F3E3D0" {W(2.2)}/>'
    f'<path d="M38 42 L36 24 L52 36Z M90 42 L92 24 L76 36Z" fill="#C99A72" {W(2.4)}/>'
    f'<circle cx="52" cy="54" r="11" fill="#fff" {W(2.4)}/><circle cx="76" cy="54" r="11" fill="#fff" {W(2.4)}/>' + eye(52, 54, 0.9) + eye(76, 54, 0.9)
    + f'<path d="M60 64 L64 72 L68 64Z" fill="{OR}" {W(1.8)}/>'
    + f'<rect x="44" y="88" width="40" height="26" rx="3" fill="#FFF3E0" {s()}/><path d="M44 88 L64 102 L84 88" fill="none" {W(2.4)}/>'
    f'<circle cx="64" cy="102" r="5" fill="{R}" {W(1.8)}/>' + sp((20, 22, 5), (108, 24, 5), (112, 104, 3)))
I["quest-loft-skhodnenskaya"] = ("purple", "летающая волшебная метла",
    f'<path d="M14 110 L92 32" stroke="{BR}" stroke-width="8" stroke-linecap="round"/><path d="M14 110 L92 32" {W(1.6)}/>'
    f'<path d="M84 40 L104 14 Q120 20 118 32 Q114 40 112 46 L92 56Z" fill="{Y}" {s()} transform="rotate(10 100 36)"/>'
    + "".join(f'<path d="M{96 + i * 4} {22 + i * 3} L{102 + i * 4} {46 + i * 2}" stroke="#D9A830" stroke-width="2"/>' for i in range(4))
    + f'<rect x="80" y="40" width="14" height="10" rx="2" fill="{R}" {W(2)} transform="rotate(-45 87 45)"/>'
    + f(52, 68, d=7, k=0.6)
    + "".join(f'<path d="M{x} {y} q-10 2 -16 10" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>' for x, y in [(30, 108), (22, 96)])
    + "".join(sparkle(x, y, r, Y) for x, y, r in [(26, 30, 7), (50, 20, 4), (106, 98, 6), (80, 112, 4)]))
I["fort-boyard-borisovo"] = ("orange", "свиток с подсказкой и сургучной печатью",
    f'<rect x="28" y="28" width="72" height="72" fill="#FFF3D6" {s()}/>'
    f'<rect x="20" y="20" width="88" height="14" rx="7" fill="#E6C99A" {s()}/><rect x="20" y="94" width="88" height="14" rx="7" fill="#E6C99A" {s()}/>'
    + "".join(f'<path d="M40 {y} H{x}" stroke="#C9A06A" stroke-width="3" stroke-linecap="round"/>' for y, x in [(70, 84), (80, 76)])
    + f(64, 52, d=9, k=0.8)
    + f'<circle cx="90" cy="86" r="12" fill="{R}" {s()}/><path d="M84 86 l6 -6 l6 6 l-6 6Z" fill="none" stroke="#FFB0A0" stroke-width="2"/>'
    + sp((112, 50, 5), (16, 60, 5)))
I["klyuchi-forta-chertanovo"] = ("blue", "связка старинных ключей на кольце",
    f'<circle cx="64" cy="34" r="18" fill="none" stroke="{GR}" stroke-width="6"/><circle cx="64" cy="34" r="18" fill="none" {W(1.6)}/>'
    + "".join(f'<g transform="rotate({a} 64 52)"><rect x="60" y="48" width="8" height="54" rx="3" fill="{c}" {W(2.4)}/>'
              f'<rect x="68" y="88" width="10" height="6" fill="{c}" {W(2)}/><rect x="68" y="96" width="7" height="5" fill="{c}" {W(2)}/></g>'
              for a, c in [(-34, GO), (34, "#C0C4D6")])
    + f'<rect x="60" y="48" width="8" height="58" rx="3" fill="{GO}" {W(2.4)}/><circle cx="64" cy="54" r="14" fill="{GO}" {s()}/>'
    + f(64, 55, d=5, k=0.5) + f'<rect x="68" y="92" width="12" height="6" fill="{GO}" {W(2)}/><rect x="68" y="100" width="8" height="5" fill="{GO}" {W(2)}/>'
    + sp((20, 30, 6), (108, 30, 5)))
I["hogwarts-quest-maslovka"] = ("night", "волшебный котёл с зельем",
    f'<path d="M24 60 Q22 108 64 110 Q106 108 104 60Z" fill="{NV}" stroke="#9AA0C8" stroke-width="3"/><rect x="18" y="54" width="92" height="12" rx="6" fill="#4A4A6A" stroke="#9AA0C8" stroke-width="3"/>'
    f'<path d="M24 58 Q40 40 52 54 Q64 38 76 54 Q88 40 104 58Z" fill="{G}" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#A8F08A" {W(1.8)}/>' for x, y, r in [(48, 34, 6), (70, 24, 8), (86, 38, 5)])
    + f(64, 84, d=10, k=0.85).replace(O, "#fff") + f'<path d="M36 110 l-6 10 M92 110 l6 10" stroke="#9AA0C8" stroke-width="4" stroke-linecap="round"/>'
    + "".join(sparkle(x, y, r, Y) for x, y, r in [(20, 26, 5), (106, 20, 6)]))
I["wednesday-quest-podsosensky"] = ("purple", "чёрный зонтик с глазками",
    f'<path d="M16 66 Q20 22 64 20 Q108 22 112 66 Q102 58 92 66 Q80 56 64 66 Q48 56 36 66 Q26 58 16 66Z" fill="{NV}" {s()}/>'
    f'<path d="M64 20 Q50 40 48 62 M64 20 Q78 40 80 62" fill="none" stroke="#5A5880" stroke-width="2.4"/>'
    f'<path d="M64 12 V20" {W(4)}/>' + f(64, 42, d=10, k=0.8).replace(f'fill="{O}"', 'fill="#fff"')
    + f'<path d="M64 66 V106 Q64 116 54 116 Q46 116 46 108" fill="none" {W(5)}/><path d="M64 66 V106 Q64 116 54 116 Q46 116 46 108" fill="none" stroke="{GR}" stroke-width="2.4"/>'
    + "".join(f'<path d="M{x} {y} v6" stroke="#9AD6FF" stroke-width="3" stroke-linecap="round"/>' for x, y in [(22, 84), (38, 96), (90, 92), (106, 80)]))
I["quest-33-misfortunes"] = ("teal", "очки-маскировка с усами",
    f'<path d="M16 50 H112" {W(4)}/><circle cx="42" cy="58" r="20" fill="#E8F6FF" {s()}/><circle cx="86" cy="58" r="20" fill="#E8F6FF" {s()}/>'
    + eye(42, 58, 1.1) + eye(86, 58, 1.1)
    + f'<path d="M58 62 Q64 76 70 62" fill="{SK}" {s()}/>'
    + f'<path d="M64 82 Q50 74 36 86 Q30 94 42 92 Q54 88 64 86 Q74 88 86 92 Q98 94 92 86 Q78 74 64 82Z" fill="{NV}" {s()}/>'
    + f'<path d="M22 40 Q42 30 58 40 M70 40 Q86 30 106 40" fill="none" stroke="{NV}" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M40 104 Q64 114 88 104" fill="none" {W(3)}/>' + sp((20, 108, 5), (110, 106, 5)))

# ===================== Zамания =====================
I["zamania-4daily-mytishchi"] = ("pink", "йо-йо крутит трюк",
    f'<path d="M64 8 Q60 40 72 52" fill="none" {W(2.4)}/><circle cx="64" cy="8" r="5" fill="{R}" {W(2)}/>'
    f'<circle cx="78" cy="78" r="34" fill="{B}" {s()}/><circle cx="78" cy="78" r="24" fill="#8FD2FF" {W(2.4)}/>'
    f'<circle cx="78" cy="78" r="6" fill="{Y}" {W(2)}/>' + f(78, 82, d=10, k=0.8)
    + "".join(f'<path d="M{x} {y} q-10 6 -14 16" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' for x, y in [(34, 58), (30, 80), (36, 102)])
    + sp((22, 30, 6), (108, 20, 5)))
I["zamania-kaleidoskop"] = ("yellow", "воздушный шарик-собачка",
    f'<ellipse cx="44" cy="70" rx="20" ry="13" fill="{R}" {s()}/><ellipse cx="80" cy="66" rx="16" ry="13" fill="{R}" {s()}/>'
    f'<ellipse cx="96" cy="44" rx="15" ry="14" fill="{R}" {s()}/><ellipse cx="88" cy="26" rx="6" ry="13" fill="{R}" {W(2.6)} transform="rotate(-20 88 26)"/>'
    f'<ellipse cx="112" cy="50" rx="9" ry="6" fill="{R}" {W(2.6)}/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="5" ry="12" fill="{R}" {W(2.6)}/>' for x, y in [(36, 92), (52, 92), (74, 88), (88, 88)])
    + f'<ellipse cx="22" cy="58" rx="10" ry="5" fill="{R}" {W(2.6)} transform="rotate(-30 22 58)"/>'
    + f(98, 44, d=6, k=0.6)
    + "".join(f'<path d="M{x} {y} q4 -4 8 -2" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' for x, y in [(36, 64), (74, 60), (90, 38)])
    + f'<path d="M64 74 Q60 100 70 120" fill="none" {W(1.8)}/>' + sp((20, 24, 6), (60, 22, 4)))

if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        bg, subj, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(bg, body))
    print("svg:", len(ids))
