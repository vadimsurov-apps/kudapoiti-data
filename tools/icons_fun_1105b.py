"""Иконки робота fun (2026-11-05, вечер): 70 новых сюжетов — сказочные персонажи, игрушки, животные, транспорт,
природа, космос. Каждый сюжет сверен с icons-catalog/sheet-*.png и icons-src/subjects.txt (не повторяется).
Запуск: python3 tools/icons_fun_1105b.py [id ...]"""
import os, sys
from draw_icons import svg, s, eye, face, sparkle, O
W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=9, k=0.75, **kw: face(cx, cy, d=d, k=k, **kw)
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
R, OR, Y, G, B, P, V, BR, WH, GR = ("#E8654F", "#FF9A3D", "#FFD25E", "#7CD26E", "#5CB7F2", "#FF8FB8", "#A98BF0",
                                    "#C0732E", "#FFFFFF", "#B8BCCB")
DG, SK, TE = "#4E9A5A", "#FFD9B8", "#5CCDBA"
sp = lambda *pts: "".join(sparkle(x, y, r) for x, y, r in pts)
GROUND = f'<path d="M0 104 Q64 92 128 104 V128 H0Z" fill="{G}" {W(2.6)}/>'
WATER = f'<path d="M0 100 Q16 92 32 100 T64 100 T96 100 T128 100 V128 H0Z" fill="#7FD3F7" {W(2.6)}/>'

I = {}
# ===================== Театры: сказочные персонажи и предметы =====================
I["domisolka"] = ("pink", "музыкальная шкатулка",
    f'<path d="M24 66 H104 V104 H24Z" fill="{V}" {s()}/><path d="M24 66 L34 54 H94 L104 66Z" fill="#C9B6FF" {s()}/>'
    f'<path d="M30 54 L22 30 L100 22 L94 54" fill="{P}" {s()}/><rect x="98" y="78" width="12" height="6" rx="3" fill="{Y}" {W(2.4)}/>'
    f'<path d="M64 54 V40" {W(2.4)}/><path d="M56 40 Q64 30 72 40 Z" fill="#fff" {W(2.2)}/><circle cx="64" cy="28" r="5" fill="{SK}" {W(2.2)}/>'
    + f(64, 86, d=9, k=0.6) + sp((20, 20, 6), (110, 44, 5)))
I["koleso-dmitrov"] = ("sky", "ветряная мельница",
    GROUND + f'<path d="M46 104 L52 50 H76 L82 104Z" fill="{BR}" {s()}/><path d="M48 50 L64 36 L80 50Z" fill="{R}" {s()}/>'
    + "".join(f'<path d="M64 46 L{x} {y}" stroke="{O}" stroke-width="3"/><rect x="{min(64,x)-0}" y="0" width="0" height="0"/>' for x, y in [])
    + "".join(f'<path d="M64 46 L64 6 L74 8 L70 42Z" fill="#fff" {W(2.4)} transform="rotate({a} 64 46)"/>' for a in (20, 110, 200, 290))
    + f'<circle cx="64" cy="46" r="5" fill="{Y}" {W(2.4)}/>' + f(64, 80, d=8, k=0.6))
I["klyaksa"] = ("yellow", "клякса-человечек",
    f'<path d="M64 22 Q78 18 80 32 Q96 26 98 42 Q112 48 102 62 Q114 76 98 84 Q100 102 82 98 Q74 112 60 102 Q44 110 40 96 Q22 98 26 80 Q12 70 26 58 Q18 42 34 40 Q36 22 52 28 Q56 20 64 22Z" fill="#3E4AA0" {s()}/>'
    f'<circle cx="108" cy="30" r="6" fill="#3E4AA0" {W(2.4)}/><circle cx="20" cy="108" r="5" fill="#3E4AA0" {W(2.4)}/>'
    f'<circle cx="54" cy="58" r="8" fill="#fff"/><circle cx="76" cy="58" r="8" fill="#fff"/>' + f(65, 60, d=11, k=0.8, blush=False, mouth=False)
    + f'<path d="M54 78 Q65 88 76 78" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')
I["kukly-i-lyudi"] = ("night", "Пьеро",
    f'<path d="M28 128 L40 74 H88 L100 128Z" fill="#fff" {s()}/><path d="M36 76 Q64 92 92 76 L88 70 H40Z" fill="#fff" {W(2.6)}/>'
    + "".join(f'<circle cx="64" cy="{y}" r="4" fill="{O}"/>' for y in (96, 110))
    + f'<circle cx="64" cy="50" r="24" fill="#F4F4F8" {s()}/><path d="M42 40 Q64 14 86 40 Q64 30 42 40Z" fill="{O}" {W(2.4)}/>'
    + f(64, 52, d=9, k=0.7, mouth=False, blush=False)
    + f'<path d="M55 58 L55 66 M73 58 L73 66" stroke="#5CB7F2" stroke-width="2.4" stroke-linecap="round"/>'
    f'<path d="M58 68 Q64 64 70 68" fill="none" {W(2.4)}/>' + sp((20, 24, 6), (108, 30, 5)))
I["ognivo"] = ("orange", "огниво с искрами",
    f'<path d="M24 74 Q24 54 44 54 H84 Q104 54 104 74 Q104 82 96 82 H32 Q24 82 24 74Z" fill="#8C93A8" {s()}/>'
    f'<path d="M40 54 Q40 40 52 40 H76 Q88 40 88 54" fill="none" {W(5)}/>'
    f'<path d="M34 96 L60 86 L72 104 L48 112Z" fill="#9AA0B8" {s()}/>' + f(64, 68, d=10, k=0.6)
    + "".join(f'<path d="M{x} {y} l{dx} {dy}" stroke="{Y}" stroke-width="3.5" stroke-linecap="round"/>' for x, y, dx, dy in
              [(76, 92, 14, -6), (78, 98, 16, 4), (74, 102, 8, 12)]) + sp((106, 92, 7), (98, 112, 5)))
I["nash-dom-khimki"] = ("purple", "джинн",
    f'<path d="M40 112 Q64 120 88 112 Q70 104 74 92 Q86 84 86 70 L42 70 Q42 84 54 92 Q58 104 40 112Z" fill="{B}" {s()}/>'
    f'<path d="M48 120 Q40 100 60 96" fill="none" stroke="{B}" stroke-width="10" stroke-linecap="round"/>'
    f'<circle cx="64" cy="54" r="22" fill="#6FA8F0" {s()}/><path d="M42 44 Q42 22 64 22 Q86 22 86 44 Q76 34 64 36 Q52 34 42 44Z" fill="{R}" {s()}/>'
    f'<circle cx="64" cy="30" r="5" fill="{Y}" {W(2.2)}/><path d="M54 66 Q64 60 74 66 Q64 76 54 66Z" fill="#2B2A44"/>'
    + f(64, 52, d=8, k=0.6, mouth=False) + f'<circle cx="40" cy="80" r="5" fill="{Y}" {W(2)}/><circle cx="88" cy="80" r="5" fill="{Y}" {W(2)}/>'
    + sp((18, 30, 6), (110, 26, 6), (106, 104, 5)))
I["vernadskogo-13"] = ("orange", "скатерть-самобранка",
    f'<path d="M10 78 Q40 66 64 72 Q90 78 118 64 L112 104 Q86 116 62 108 Q36 100 16 112Z" fill="#fff" {s()}/>'
    + "".join(f'<path d="M{x} {y} l6 -6 l6 6 l-6 6Z" fill="{R}" {W(1.6)}/>' for x, y in [(22, 98), (44, 96), (70, 100), (94, 96)])
    + f'<path d="M14 106 Q40 94 62 102 Q88 108 114 96" fill="none" stroke="{R}" stroke-width="3"/>'
    + f'<path d="M40 74 Q40 56 54 56 H62 V74Z" fill="{OR}" {s()}/><path d="M66 74 V50 Q66 40 76 40 Q86 40 86 50 V74Z" fill="#E0A85C" {s()}/>'
    + f'<ellipse cx="98" cy="64" rx="12" ry="6" fill="{Y}" {W(2.2)}/><circle cx="98" cy="58" r="5" fill="{R}" {W(2)}/>'
    + f'<path d="M48 52 Q52 44 48 36 M76 36 Q80 28 76 20" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    + f(64, 88, d=8, k=0.55) + sp((22, 30, 6), (108, 30, 5)))
I["lianozovsky-theatre"] = ("green", "леший",
    f'<path d="M30 118 Q22 70 40 44 Q52 28 64 26 Q76 28 88 44 Q106 70 98 118Z" fill="#8A6A3E" {s()}/>'
    f'<path d="M40 44 Q30 30 20 30 M88 44 Q98 30 110 28 M64 26 Q60 12 50 8 M64 26 Q70 10 80 8" fill="none" stroke="#8A6A3E" stroke-width="6" stroke-linecap="round"/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="9" ry="5" fill="{G}" {W(2)} transform="rotate({a} {x} {y})"/>' for x, y, a in
              [(18, 28, -20), (110, 26, 20), (48, 8, -30), (82, 6, 30)])
    + f'<path d="M44 74 Q48 104 64 108 Q80 104 84 74 Q64 84 44 74Z" fill="{G}" {W(2.6)}/>' + f(64, 60, d=10, k=0.75))
I["most-theatre"] = ("blue", "водяной",
    WATER + f'<ellipse cx="64" cy="70" rx="34" ry="30" fill="{TE}" {s()}/>'
    f'<path d="M34 74 Q30 110 44 104 Q48 120 58 106 Q64 122 70 106 Q80 120 84 104 Q98 110 94 74" fill="#9BE07A" {s()}/>'
    f'<path d="M42 46 Q34 30 44 22 M86 46 Q94 30 84 22" fill="none" stroke="{DG}" stroke-width="5" stroke-linecap="round"/>'
    + f(64, 64, d=11, k=0.8) + f'<circle cx="100" cy="30" r="5" fill="#fff" {W(2)}/><circle cx="108" cy="18" r="3" fill="#fff" {W(1.6)}/>')
I["fest-mytishchi"] = ("yellow", "шут с бубенцами",
    f'<path d="M36 56 Q24 30 10 34 Q22 46 30 62Z" fill="{R}" {s()}/><path d="M92 56 Q104 30 118 34 Q106 46 98 62Z" fill="{V}" {s()}/>'
    f'<path d="M48 48 Q64 6 80 48Z" fill="{G}" {s()}/><circle cx="10" cy="34" r="6" fill="{Y}" {W(2.4)}/>'
    f'<circle cx="118" cy="34" r="6" fill="{Y}" {W(2.4)}/><circle cx="64" cy="10" r="6" fill="{Y}" {W(2.4)}/>'
    f'<circle cx="64" cy="70" r="26" fill="{SK}" {s()}/><path d="M36 92 L46 104 L56 94 L64 106 L72 94 L82 104 L92 92" fill="#fff" {s()}/>'
    + f(64, 68, d=9, k=0.8) + f'<path d="M58 60 l-4 -4 M70 60 l4 -4" {W(2)}/>')
I["cdr-begovaya"] = ("teal", "кикимора",
    f'<path d="M26 120 Q30 80 40 70 H88 Q98 80 102 120Z" fill="#7C8A5A" {s()}/>'
    f'<circle cx="64" cy="58" r="26" fill="#C6E39A" {s()}/>'
    f'<path d="M38 48 Q30 70 22 92 M42 40 Q34 60 36 96 M86 40 Q96 64 92 98 M90 48 Q98 70 108 90" fill="none" stroke="#5E7C3A" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M40 40 Q64 18 88 40 Q76 30 64 32 Q52 30 40 40Z" fill="#5E7C3A" {W(2.4)}/><circle cx="74" cy="30" r="5" fill="{P}" {W(2)}/>'
    + f(64, 60, d=9, k=0.7) + f'<path d="M64 62 l-3 6 h6Z" fill="#9CC46A" {W(1.6)}/>')
I["liliya-tim"] = ("night", "пегас",
    f'<path d="M30 70 Q30 50 54 52 L82 54 Q96 56 98 74 Q98 88 84 90 H48 Q30 90 30 70Z" fill="#fff" {s()}/>'
    f'<path d="M40 88 V108 M52 90 V110 M74 90 V110 M86 88 V106" {W(5)}/>'
    f'<path d="M84 58 L94 30 Q100 20 110 26 L114 36 Q106 38 102 44 L96 64Z" fill="#fff" {s()}/>'
    f'<path d="M94 30 Q90 22 96 18" fill="none" stroke="{P}" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M50 56 Q30 20 54 14 Q52 30 62 26 Q62 40 72 38 Q70 48 60 56Z" fill="#E0D4FF" {s()}/>'
    f'<path d="M30 70 Q16 70 14 86" fill="none" stroke="{P}" stroke-width="6" stroke-linecap="round"/>'
    + eye(104, 32, 0.6) + sp((20, 30, 6), (110, 104, 6), (32, 112, 4)))
I["kamernaya-scena-lobnya"] = ("sky", "Снегурочка",
    f'<path d="M30 128 L42 72 H86 L98 128Z" fill="#8FD0F5" {s()}/><path d="M64 76 V128" stroke="#fff" stroke-width="4"/>'
    + "".join(sparkle(x, y, 5) for x, y in [(48, 100), (80, 108), (54, 120)])
    + f'<circle cx="64" cy="54" r="22" fill="{SK}" {s()}/><path d="M38 50 Q38 18 64 18 Q90 18 90 50 Q88 34 64 34 Q40 34 38 50Z" fill="#8FD0F5" {s()}/>'
    f'<path d="M42 26 L50 10 L58 22 L64 6 L70 22 L78 10 L86 26" fill="#fff" {s()}/>'
    f'<path d="M86 60 Q100 80 92 104" fill="none" stroke="#F2C86A" stroke-width="9" stroke-linecap="round"/>' + f(64, 56, d=8, k=0.7))
I["spesivtsev"] = ("purple", "ступа Бабы-Яги",
    f'<path d="M36 52 H92 L84 108 H44Z" fill="{BR}" {s()}/><path d="M38 64 H90 M42 90 H86" {W(2.4)}/>'
    f'<path d="M30 46 H98 V56 H30Z" fill="#A0602A" {s()}/><path d="M100 14 L78 60" stroke="{BR}" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M78 60 L70 70 M78 60 L76 72 M78 60 L84 70" stroke="#E8C77A" stroke-width="3" stroke-linecap="round"/>'
    + f(64, 78, d=10, k=0.7) + f'<path d="M20 116 Q30 108 40 112 Q48 104 58 114" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".8"/>'
    + sp((22, 28, 6), (110, 92, 5)))
I["gorod-dolgoprudny"] = ("sky", "летучий корабль",
    f'<path d="M14 74 H114 Q106 100 82 102 H46 Q22 100 14 74Z" fill="{BR}" {s()}/>'
    + f(64, 88, d=10, k=0.6) + f'<path d="M64 74 V24" {W(4)}/><path d="M66 26 Q92 40 66 66Z" fill="#fff" {s()}/>'
    f'<path d="M24 78 Q2 70 6 54 Q22 66 30 60 Q22 50 30 42 Q38 58 40 76Z" fill="#fff" {s()}/>'
    f'<path d="M104 78 Q126 70 122 54 Q106 66 98 60 Q106 50 98 42 Q90 58 88 76Z" fill="#fff" {s()}/>'
    f'<path d="M64 24 L76 20 L64 16Z" fill="{R}" {W(2)}/>' + sp((30, 20, 5), (100, 24, 6)))
I["gubernsky-theatre"] = ("pink", "царский трон",
    f'<path d="M34 112 V34 Q34 16 64 14 Q94 16 94 34 V112" fill="{R}" {s()}/><path d="M44 70 V36 Q44 26 64 26 Q84 26 84 36 V70Z" fill="{Y}" {s()}/>'
    f'<path d="M26 70 H102 V86 H26Z" fill="#B23A3A" {s()}/><path d="M32 86 V112 M96 86 V112" {W(5)}/>'
    f'<path d="M54 10 L58 2 L64 8 L70 2 L74 10Z" fill="{Y}" {W(2)}/>' + f(64, 50, d=8, k=0.6))
I["podolsk-drama"] = ("blue", "меч-кладенец",
    f'<path d="M58 84 V20 L64 8 L70 20 V84Z" fill="#E4E8F2" {s()}/><path d="M64 14 V80" stroke="#B8BCCB" stroke-width="2"/>'
    f'<path d="M36 84 H92 Q96 84 96 90 Q96 94 92 94 H36 Q32 94 32 90 Q32 84 36 84Z" fill="{Y}" {s()}/>'
    f'<rect x="58" y="94" width="12" height="20" rx="4" fill="{BR}" {s()}/><circle cx="64" cy="118" r="6" fill="{R}" {W(2.4)}/>'
    + f(64, 52, d=4, k=0.38, blush=False) + sp((30, 34, 7), (98, 42, 6), (92, 112, 5)))
I["folk-center-moskva"] = ("orange", "богатырь",
    f'<path d="M24 128 Q26 92 64 90 Q102 92 104 128Z" fill="#9AA0B8" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.4" fill="{O}"/>' for x in range(36, 96, 10) for y in (104, 116))
    + f'<circle cx="64" cy="62" r="24" fill="{SK}" {s()}/><path d="M40 58 Q40 30 64 14 Q88 30 88 58Z" fill="#C9CEDB" {s()}/>'
    f'<path d="M64 14 V4" {W(3)}/><path d="M60 58 V66" {W(3)}/><path d="M46 74 Q64 100 82 74 Q64 84 46 74Z" fill="#E0A85C" {W(2.4)}/>'
    + f(64, 66, d=9, k=0.65, mouth=False))
I["kc-zelenograd"] = ("green", "часы с кукушкой",
    f'<path d="M30 46 L64 18 L98 46Z" fill="{BR}" {s()}/><rect x="36" y="44" width="56" height="50" fill="#E0A85C" {s()}/>'
    f'<circle cx="64" cy="74" r="14" fill="#fff" {W(2.6)}/><path d="M64 74 V64 M64 74 H72" {W(2.4)}/>'
    f'<rect x="56" y="30" width="16" height="14" fill="#2B2A44" {W(2.4)}/><circle cx="64" cy="36" r="7" fill="{Y}" {W(2.2)}/>'
    f'<path d="M70 36 L80 34 L70 40Z" fill="{OR}" {W(1.6)}/>' + eye(62, 34, 0.45)
    + f'<path d="M52 94 V114 M76 94 V108" {W(2)}/><path d="M48 112 h8 l-4 8Z M72 106 h8 l-4 8Z" fill="{Y}" {W(2)}/>')

# ===================== Кино: животные, транспорт, природа =====================
I["kronverk-semenovsky"] = ("blue", "акула",
    WATER + f'<path d="M14 66 Q40 40 82 46 Q100 48 112 60 L124 48 L120 70 L126 90 L110 78 Q96 90 74 90 Q36 92 14 66Z" fill="#8C9DB8" {s()}/>'
    f'<path d="M58 46 L68 22 L82 48Z" fill="#8C9DB8" {s()}/><path d="M20 70 Q50 92 80 88 Q46 80 20 70Z" fill="#fff"/>'
    f'<path d="M28 72 L34 78 L38 72 L44 79 L48 73" fill="none" {W(2)}/>' + eye(36, 60, 0.8)
    + f'<path d="M58 62 Q62 68 60 74 M64 60 Q68 68 66 76" fill="none" {W(2)}/>')
I["cinema-park-metropolis"] = ("orange", "монстр-трак",
    f'<path d="M30 54 H74 L86 38 H100 L106 54 Q114 54 114 62 V70 H22 V62 Q22 54 30 54Z" fill="{G}" {s()}/>'
    f'<path d="M88 42 H98 L102 54 H82Z" fill="#BFE9FF" {W(2.4)}/>' + f(48, 62, d=8, k=0.5)
    + "".join(f'<circle cx="{x}" cy="92" r="22" fill="#2B2A44" {s()}/><circle cx="{x}" cy="92" r="9" fill="{GR}" {W(2.4)}/>'
              + "".join(f'<path d="M{x} 70 v6" stroke="#5A5870" stroke-width="5" transform="rotate({a} {x} 92)"/>' for a in range(0, 360, 45))
              for x in (36, 94)) + f'<path d="M52 70 V80 H78 V70" {W(3)}/>')
I["moskino-iskra"] = ("yellow", "дикобраз",
    "".join(f'<path d="M64 74 L{64+44*__import__("math").cos(a):.0f} {74-44*__import__("math").sin(a):.0f}" stroke="#6B5640" stroke-width="3.5" stroke-linecap="round"/>'
            f'<circle cx="{64+44*__import__("math").cos(a):.0f}" cy="{74-44*__import__("math").sin(a):.0f}" r="2" fill="#fff"/>'
            for a in [i * 0.2 + 0.3 for i in range(13)])
    + f'<path d="M22 100 Q22 60 64 60 Q106 60 106 100 Z" fill="#8A6E52" {s()}/>'
    f'<ellipse cx="40" cy="92" rx="22" ry="16" fill="#D9B48C" {s()}/><circle cx="20" cy="92" r="4" fill="{O}"/>'
    + f(40, 88, d=7, k=0.5) + f'<path d="M50 108 v8 M82 108 v8" {W(5)}/>' + GROUND[:0])
I["pobeda-zaraysk"] = ("sky", "самосвал",
    f'<path d="M10 92 V70 H34 L42 52 H58 V92Z" fill="{R}" {s()}/><path d="M38 70 L44 58 H54 V70Z" fill="#BFE9FF" {W(2.4)}/>'
    f'<path d="M58 86 L64 52 L118 40 L118 86Z" fill="{Y}" {s()}/><path d="M66 56 L114 46" {W(2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="7" fill="#C0956A" {W(2)}/>' for x, y in [(80, 40), (94, 36), (106, 34), (88, 30)])
    + f'<path d="M6 86 H122" {W(3)}/>' + "".join(f'<circle cx="{x}" cy="96" r="12" fill="#2B2A44" {s()}/><circle cx="{x}" cy="96" r="5" fill="{GR}"/>' for x in (28, 76, 104))
    + f(88, 66, d=8, k=0.5))
I["pavlovsky-cinema"] = ("green", "еловая шишка",
    f'<path d="M64 16 V8" stroke="{BR}" stroke-width="5" stroke-linecap="round"/><path d="M58 10 Q46 0 40 12 Q52 12 58 10Z" fill="{DG}" {W(2)}/>'
    f'<path d="M64 16 Q96 36 92 78 Q88 112 64 118 Q40 112 36 78 Q32 36 64 16Z" fill="#B07A44" {s()}/>'
    + "".join(f'<path d="M{44+d} {y} Q64 {y+10} {84-d} {y}" fill="none" {W(2.4)}/>' for d, y in [(8, 36), (0, 52), (-4, 68), (0, 86), (8, 102)])
    + f(64, 72, d=9, k=0.65))
I["cinema-city-noginsk"] = ("teal", "жук-олень",
    f'<path d="M50 40 Q30 32 26 12 Q38 22 44 20 Q40 30 54 36Z M78 40 Q98 32 102 12 Q90 22 84 20 Q88 30 74 36Z" fill="#7A3E1E" {s()}/>'
    f'<ellipse cx="64" cy="50" rx="18" ry="12" fill="#3B2A22" {s()}/>'
    f'<path d="M40 70 Q40 58 64 58 Q88 58 88 70 V96 Q88 118 64 118 Q40 118 40 96Z" fill="#6E3A20" {s()}/><path d="M64 60 V118" {W(2.4)}/>'
    + "".join(f'<path d="M{a} {y} L{b} {y+8}" {W(3)}/>' for a, b, y in [(40, 24, 72), (40, 22, 90), (88, 104, 72), (88, 106, 90)])
    + f(64, 50, d=8, k=0.55))
I["galaks-dolgoprudny"] = ("orange", "сурикат",
    GROUND + f'<path d="M44 110 Q38 70 50 50 Q56 40 64 40 Q72 40 78 50 Q90 70 84 110Z" fill="#D9B07A" {s()}/>'
    f'<ellipse cx="64" cy="84" rx="12" ry="20" fill="#F2DDB8"/><circle cx="64" cy="34" r="18" fill="#D9B07A" {s()}/>'
    f'<ellipse cx="56" cy="34" rx="7" ry="6" fill="#5A4030"/><ellipse cx="72" cy="34" rx="7" ry="6" fill="#5A4030"/>'
    + eye(56, 34, 0.55) + eye(72, 34, 0.55) + f'<ellipse cx="64" cy="44" rx="4" ry="3" fill="{O}"/>'
    f'<path d="M50 62 Q56 70 62 64 M78 62 Q72 70 66 64" fill="none" {W(2.6)}/><circle cx="46" cy="20" r="4" fill="#D9B07A" {W(2.2)}/><circle cx="82" cy="20" r="4" fill="#D9B07A" {W(2.2)}/>')
I["baltika-skhodnenskaya"] = ("blue", "гидроплан",
    WATER + f'<path d="M20 60 Q20 48 40 48 H92 Q106 48 112 58 L118 40 L124 42 L120 64 Q110 70 92 70 H40 Q20 70 20 60Z" fill="#fff" {s()}/>'
    f'<path d="M50 52 L70 52 L74 30 H54Z" fill="{R}" {s()}/><path d="M48 72 V88 M86 72 V88" {W(3)}/>'
    f'<path d="M30 90 H64 Q66 96 58 98 H32Z M70 90 H104 Q106 96 98 98 H72Z" fill="{Y}" {s()}/>'
    f'<path d="M14 46 V74" stroke="{O}" stroke-width="4" stroke-linecap="round"/><circle cx="20" cy="60" r="4" fill="{GR}" {W(2)}/>'
    + f(84, 58, d=6, k=0.45) + "".join(f'<rect x="{x}" y="54" width="7" height="6" rx="2" fill="#BFE9FF" {W(1.6)}/>' for x in (94,)))

# ===================== Музеи =====================
I["buratino-pinokkio"] = ("yellow", "шарманка",
    f'<rect x="26" y="40" width="70" height="56" rx="6" fill="{BR}" {s()}/><rect x="34" y="48" width="54" height="30" rx="4" fill="#E0A85C" {W(2.4)}/>'
    + "".join(f'<path d="M{x} 50 V76" {W(1.6)}/>' for x in range(40, 88, 8))
    + f'<path d="M96 60 H108 V44 H116" fill="none" {W(4)}/><circle cx="116" cy="44" r="5" fill="{R}" {W(2.2)}/>'
    f'<path d="M36 96 L30 116 M86 96 L92 116" {W(4)}/><circle cx="30" cy="116" r="5" fill="#2B2A44"/><circle cx="92" cy="116" r="5" fill="#2B2A44"/>'
    + f(61, 88, d=8, k=0.45) + "".join(f'<path d="M{x} {y} q4 -8 8 0" fill="none" stroke="{O}" stroke-width="2.4"/><circle cx="{x}" cy="{y+1}" r="3" fill="{O}"/>' for x, y in [(30, 28), (60, 18), (88, 26)]))
I["rusdessert-zvenigorod"] = ("pink", "дымковская барыня",
    f'<path d="M28 116 Q30 70 64 66 Q98 70 100 116Z" fill="#fff" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="{c}" {W(1.6)}/>' for x, y, c in [(44, 92, R), (64, 100, B), (84, 92, R), (54, 110, G), (76, 110, Y), (64, 82, Y)])
    + f'<path d="M30 112 Q64 100 98 112" fill="none" stroke="{R}" stroke-width="3"/>'
    f'<circle cx="64" cy="50" r="18" fill="#fff" {s()}/><path d="M42 44 Q40 22 64 20 Q88 22 86 44 Q80 30 64 32 Q48 30 42 44Z" fill="{OR}" {s()}/>'
    f'<path d="M46 28 Q64 8 82 28 Q72 22 64 24 Q56 22 46 28Z" fill="{R}" {W(2.4)}/>' + f(64, 52, d=7, k=0.55))
I["dog-museum"] = ("sky", "ошейник с медальоном",
    f'<ellipse cx="64" cy="54" rx="40" ry="30" fill="none" stroke="{O}" stroke-width="16"/><ellipse cx="64" cy="54" rx="40" ry="30" fill="none" stroke="{R}" stroke-width="10"/>'
    + "".join(f'<circle cx="{64+40*__import__("math").cos(a):.0f}" cy="{54+30*__import__("math").sin(a):.0f}" r="3" fill="{Y}"/>' for a in [0.3, 0.9, 1.5 - 0.6, 2.2, 2.8, 3.6, 4.4, 5.2, 5.8])
    + f'<path d="M64 84 V92" {W(3)}/><circle cx="64" cy="104" r="14" fill="{Y}" {s()}/>' + f(64, 104, d=5, k=0.45)
    + f'<path d="M56 98 q8 -6 16 0" fill="none" stroke="#fff" stroke-width="2"/>')
I["tram-museum-kolomna"] = ("teal", "компостер",
    f'<path d="M64 8 V30" {W(5)}/><rect x="32" y="30" width="64" height="62" rx="10" fill="{R}" {s()}/>'
    f'<rect x="40" y="38" width="48" height="16" rx="4" fill="#2B2A44" {W(2.4)}/><path d="M48 46 H80" stroke="{Y}" stroke-width="3" stroke-dasharray="3 4"/>'
    f'<path d="M50 92 V104 H78 V92" fill="#9AA0B8" {s()}/><rect x="70" y="56" width="26" height="40" rx="2" fill="#fff" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="{O}"/>' for x, y in [(78, 66), (86, 72), (80, 82)])
    + f(52, 72, d=7, k=0.5))
I["vbv-retro-cars"] = ("green", "дом на колёсах",
    f'<path d="M14 92 V48 Q14 36 28 36 H96 Q114 36 116 56 L118 92Z" fill="#fff" {s()}/><path d="M14 66 H118" stroke="{OR}" stroke-width="6"/>'
    f'<rect x="24" y="44" width="22" height="16" rx="4" fill="#BFE9FF" {W(2.4)}/><rect x="52" y="44" width="16" height="36" rx="3" fill="{BR}" {W(2.4)}/>'
    f'<path d="M96 44 H106 Q112 46 114 60 H96Z" fill="#BFE9FF" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="94" r="11" fill="#2B2A44" {s()}/><circle cx="{x}" cy="94" r="4" fill="{GR}"/>' for x, in [(34,), (96,)])
    + f(84, 54, d=6, k=0.42) + f'<path d="M30 36 V26 H60 V36" fill="none" {W(3)}/>')
I["pvo-museum"] = ("sky", "радар-локатор",
    GROUND + f'<path d="M50 104 L58 70 H70 L78 104Z" fill="#7C9A6A" {s()}/>'
    f'<path d="M24 32 Q64 14 104 32 L98 56 Q64 42 30 56Z" fill="#9AA0B8" {s()}/>'
    + "".join(f'<path d="M{x} {24 if x==64 else 30} V{48 if x==64 else 52}" {W(1.6)}/>' for x in (40, 52, 64, 76, 88))
    + f'<path d="M64 52 V70" {W(4)}/>' + f(64, 86, d=7, k=0.5)
    + "".join(f'<path d="M{110+r} {20-r} q6 6 0 12" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' for r in (0, 6)))
I["gvtm-ivanovskoe"] = ("yellow", "бульдозер",
    f'<path d="M8 66 Q20 60 22 96 H10Z" fill="{GR}" {s()}/><path d="M22 74 H30" {W(4)}/>'
    f'<rect x="30" y="60" width="64" height="24" rx="4" fill="{Y}" {s()}/><path d="M56 60 V34 H86 V60" fill="{Y}" {s()}/>'
    f'<rect x="62" y="40" width="18" height="14" rx="2" fill="#BFE9FF" {W(2.4)}/><path d="M98 46 V60" {W(4)}/>'
    f'<rect x="30" y="84" width="90" height="26" rx="13" fill="#2B2A44" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="97" r="7" fill="{GR}" {W(2)}/>' for x in (44, 64, 84, 104)) + f(46, 70, d=6, k=0.42))
I["doroga-pamyati"] = ("sky", "голубь мира",
    f'<path d="M30 70 Q30 46 56 46 Q72 46 86 58 L112 50 L98 70 L112 86 L84 80 Q70 94 50 92 Q30 90 30 70Z" fill="#fff" {s()}/>'
    f'<path d="M50 60 Q60 20 92 14 Q84 36 96 40 Q78 50 66 72Z" fill="#E8F2FF" {s()}/>'
    f'<path d="M30 66 L16 70 L30 74Z" fill="{OR}" {W(2)}/><path d="M18 74 Q10 86 20 92 Q16 82 24 78" fill="{G}" {W(2)}/>'
    + eye(40, 62, 0.6) + sp((22, 26, 6), (108, 108, 6)))
I["podzemnaya-moskva"] = ("night", "сталактиты в пещере",
    f'<path d="M0 0 H128 V30 Q112 30 108 52 L102 30 Q92 34 88 72 L80 30 Q70 32 64 50 L56 30 Q46 30 40 84 L32 30 Q18 30 14 60 L8 30 H0Z" fill="#8C7A6A" {s()}/>'
    f'<path d="M0 112 Q20 104 30 110 L38 90 L46 110 Q70 102 82 110 L90 96 L98 110 Q116 104 128 112 V128 H0Z" fill="#8C7A6A" {s()}/>'
    + f(40, 64, d=4, k=0.38, blush=False) + f'<circle cx="88" cy="80" r="3" fill="#7FD3F7"/><circle cx="64" cy="56" r="3" fill="#7FD3F7"/>' + sp((74, 82, 5)))
I["telephone-museum"] = ("pink", "игрушечный телефон на колёсиках",
    f'<path d="M30 52 Q30 40 44 40 H84 Q98 40 98 52 L102 96 H26Z" fill="{R}" {s()}/>'
    f'<path d="M20 34 Q20 20 40 22 H88 Q108 20 108 34 Q108 42 98 42 H86 V32 H42 V42 H30 Q20 42 20 34Z" fill="{Y}" {s()}/>'
    f'<circle cx="64" cy="70" r="18" fill="#fff" {W(2.6)}/>' + "".join(f'<circle cx="{64+12*__import__("math").cos(a):.1f}" cy="{70+12*__import__("math").sin(a):.1f}" r="2.6" fill="{O}"/>' for a in [i*0.63 for i in range(10)])
    + f(64, 70, d=4, k=0.35, blush=False) + "".join(f'<circle cx="{x}" cy="104" r="8" fill="{B}" {s()}/>' for x in (38, 90))
    + f'<path d="M108 34 Q122 40 116 60 Q110 76 118 84" fill="none" {W(2.4)}/>')
I["sputnik-museum"] = ("night", "лунный модуль",
    f'<path d="M0 108 Q64 98 128 108 V128 H0Z" fill="#B8BCCB" {W(2.6)}/><circle cx="30" cy="114" r="4" fill="#9AA0B8"/><circle cx="96" cy="116" r="5" fill="#9AA0B8"/>'
    f'<path d="M36 64 H92 L100 82 H28Z" fill="{Y}" {s()}/><path d="M44 64 L50 38 H78 L84 64Z" fill="#E4E8F2" {s()}/>'
    f'<path d="M34 82 L20 106 M94 82 L108 106 M48 82 L42 106 M80 82 L86 106" {W(3)}/><path d="M14 106 H26 M102 106 H114 M36 106 H48 M80 106 H92" {W(4)}/>'
    f'<path d="M64 38 V22" {W(2.4)}/><circle cx="64" cy="20" r="4" fill="{R}" {W(2)}/>' + f(64, 52, d=7, k=0.5) + sp((18, 24, 6), (108, 34, 5)))
I["samotsvety-museum"] = ("purple", "жеода",
    f'<path d="M22 70 Q18 34 50 24 Q90 16 104 44 Q116 74 96 98 Q72 116 44 106 Q20 96 22 70Z" fill="#9A8A7A" {s()}/>'
    f'<path d="M34 70 Q32 42 56 36 Q86 32 94 54 Q100 80 84 92 Q64 104 46 96 Q32 88 34 70Z" fill="#6B3FA0" {W(2.6)}/>'
    + "".join(f'<path d="M{x} {y} l6 -12 l6 12Z" fill="#D9C2FF" {W(1.6)}/>' for x, y in [(40, 70), (50, 56), (62, 48), (76, 52), (84, 66), (44, 86), (78, 84)])
    + f(64, 74, d=7, k=0.5) + sp((108, 22, 6)))
I["prishvin-dunino"] = ("sky", "журавль",
    f'<path d="M30 60 Q36 40 62 44 Q84 48 92 66 Q80 80 58 78 Q38 76 30 60Z" fill="#D7DCE6" {s()}/>'
    f'<path d="M64 46 Q74 30 92 34 L104 76 Q84 70 70 72Z" fill="#8C93A8" {W(2.4)}/>'
    f'<path d="M36 58 Q30 30 40 16" fill="none" stroke="#D7DCE6" stroke-width="7" stroke-linecap="round"/><path d="M36 58 Q30 30 40 16" fill="none" {W(2)} opacity="0"/>'
    f'<circle cx="42" cy="16" r="7" fill="#2B2A44" {W(2)}/><circle cx="44" cy="12" r="3" fill="{R}"/><path d="M48 16 L66 20 L48 20Z" fill="#E0B030" {W(1.8)}/>'
    f'<path d="M58 78 L54 116 M66 78 L72 116" stroke="#2B2A44" stroke-width="3"/>' + GROUND[:0]
    + f'<path d="M0 116 Q64 108 128 116 V128 H0Z" fill="{G}" {W(2.4)}/>' + eye(42, 14, 0.4))
I["lock-museum-dubna"] = ("teal", "сейф",
    f'<rect x="22" y="24" width="84" height="80" rx="8" fill="#8C93A8" {s()}/><rect x="30" y="32" width="68" height="64" rx="6" fill="#A8AEC2" {W(2.4)}/>'
    f'<circle cx="62" cy="64" r="20" fill="#5A6078" {s()}/>' + "".join(f'<path d="M62 46 V50" stroke="#fff" stroke-width="2" transform="rotate({a} 62 64)"/>' for a in range(0, 360, 30))
    + f'<rect x="88" y="50" width="6" height="28" rx="3" fill="{Y}" {W(2)}/><path d="M34 104 V112 H46 V104 M82 104 V112 H94 V104" {W(2.6)}/>'
    + f(62, 64, d=6, k=0.45))
I["dubna-museum"] = ("blue", "выхухоль",
    WATER + f'<path d="M24 86 Q24 62 54 60 Q84 58 96 74 Q100 90 82 94 H40 Q24 94 24 86Z" fill="#8A6E5A" {s()}/>'
    f'<path d="M94 72 Q108 70 120 62 Q118 74 104 80" fill="#E7A0B0" {s()}/>'
    f'<path d="M26 88 Q10 92 6 104 Q18 96 30 96" fill="#6B5040" {s()}/>' + eye(84, 70, 0.55)
    + f'<path d="M40 94 v6 M70 94 v6" {W(4)}/>' + sp((22, 30, 5)) + f'<circle cx="104" cy="40" r="4" fill="#fff" {W(1.6)}/>')
I["sport-museum"] = ("yellow", "гепард",
    f'<path d="M20 74 Q24 54 52 54 H84 Q98 54 100 70 Q100 86 86 86 H40 Q20 86 20 74Z" fill="#F2C060" {s()}/>'
    f'<path d="M26 82 L12 104 M44 86 L40 110 M80 86 L92 108 M94 80 L114 96" {W(6)}/>'
    f'<circle cx="100" cy="52" r="16" fill="#F2C060" {s()}/><path d="M90 40 l-2 -8 l8 4 M110 40 l2 -8 l-8 4" fill="#F2C060" {W(2.2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="{O}"/>' for x, y in [(34, 64), (46, 72), (58, 62), (70, 74), (82, 64), (40, 78), (64, 80)])
    + f'<path d="M94 54 L92 64 M106 54 L108 64" stroke="{O}" stroke-width="2"/>' + eye(94, 50, 0.5) + eye(106, 50, 0.5)
    + f'<path d="M20 70 Q8 60 10 46" fill="none" stroke="#F2C060" stroke-width="5" stroke-linecap="round"/>')
I["ussr-zvenigorod"] = ("pink", "пупс в ванночке",
    f'<circle cx="64" cy="54" r="22" fill="#FFCFA8" {s()}/><path d="M48 40 Q56 30 64 40 Q72 30 80 40" fill="none" {W(2.4)}/>'
    + f(64, 56, d=8, k=0.65) + f'<path d="M30 70 L92 70 Q96 70 98 74 L92 104 H36 L30 74Z" fill="none"/>'
    f'<path d="M18 68 H110 Q108 100 90 106 H38 Q20 100 18 68Z" fill="{B}" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" {W(1.6)}/>' for x, y, r in [(30, 64, 6), (44, 62, 7), (84, 62, 6), (98, 64, 7), (108, 52, 4)])
    + f'<path d="M30 106 L24 116 M98 106 L104 116" {W(4)}/>')
I["babya-dolya-kolomna"] = ("orange", "кукла-мотанка",
    f'<path d="M34 118 Q40 70 64 66 Q88 70 94 118Z" fill="{R}" {s()}/>'
    + "".join(f'<path d="M{x} 80 L{x-4} 116" stroke="#fff" stroke-width="2"/>' for x in (54, 64, 74))
    + f'<path d="M36 88 H92" stroke="{Y}" stroke-width="5"/><path d="M28 74 L46 70 M100 74 L82 70" stroke="#F2EAD8" stroke-width="10" stroke-linecap="round"/>'
    f'<circle cx="64" cy="48" r="20" fill="#F2EAD8" {s()}/><path d="M42 46 Q42 24 64 24 Q86 24 86 46 Q74 36 64 36 Q54 36 42 46Z" fill="{G}" {s()}/>'
    f'<path d="M58 66 H70" {W(3)}/><path d="M44 50 L84 50" stroke="{R}" stroke-width="0"/>'
    + "".join(f'<circle cx="{x}" cy="30" r="2.4" fill="#fff"/>' for x in (52, 64, 76)))
I["voennaya-forma"] = ("blue", "оловянный солдатик",
    f'<rect x="40" y="108" width="48" height="10" rx="3" fill="#9AA0B8" {s()}/>'
    f'<path d="M52 108 V82 H76 V108" fill="#3E5FA8" {s()}/><path d="M64 84 V108" {W(2)}/>'
    f'<rect x="46" y="50" width="36" height="36" rx="6" fill="{R}" {s()}/><path d="M46 62 H82" stroke="#fff" stroke-width="3"/>'
    f'<path d="M86 22 V96" stroke="#8C93A8" stroke-width="5" stroke-linecap="round"/><path d="M86 22 L88 12" {W(2.4)}/>'
    f'<circle cx="64" cy="38" r="12" fill="{SK}" {s()}/><rect x="54" y="8" width="20" height="24" rx="6" fill="#2B2A44" {s()}/>'
    f'<circle cx="64" cy="22" r="3" fill="{Y}"/>' + f(64, 40, d=5, k=0.42, blush=False))
I["padikovo-museum"] = ("green", "полевая кухня",
    f'<path d="M24 50 H96 V88 H24Z" fill="#6E7F4E" {s()}/><path d="M96 70 H118" {W(4)}/><circle cx="118" cy="70" r="4" fill="{GR}" {W(2)}/>'
    f'<path d="M36 50 V22 H46 V50" fill="#5A6640" {s()}/><path d="M42 18 Q50 10 42 2 M34 16 Q42 8 34 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    f'<ellipse cx="74" cy="50" rx="18" ry="6" fill="#8C93A8" {W(2.4)}/>' + f(64, 72, d=9, k=0.55)
    + "".join(f'<circle cx="{x}" cy="96" r="14" fill="#2B2A44" {s()}/><circle cx="{x}" cy="96" r="5" fill="{GR}"/>' for x in (40, 84)))
I["krasnogorsk-pobeda"] = ("yellow", "гвоздика",
    f'<path d="M64 60 Q60 90 66 120" fill="none" stroke="{DG}" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M64 96 Q44 90 36 76 Q54 78 64 92Z" fill="{G}" {W(2.2)}/>'
    f'<path d="M50 56 L56 64 H72 L78 56Z" fill="{G}" {W(2.2)}/>'
    f'<path d="M40 50 L46 30 L52 40 L58 20 L64 34 L70 20 L76 40 L82 30 L88 50 Q64 64 40 50Z" fill="{R}" {s()}/>'
    + f(64, 44, d=7, k=0.5) + sp((100, 26, 6), (26, 100, 5)))
I["rusimp-museum"] = ("green", "ландыш",
    f'<path d="M50 120 Q30 70 46 26 Q62 70 56 120Z" fill="{G}" {s()}/><path d="M62 120 Q60 70 78 40" fill="none" stroke="{DG}" stroke-width="4" stroke-linecap="round"/>'
    + "".join(f'<path d="M{x} {y} q0 -10 8 -10 q8 0 8 10 l-3 -2 l-3 3 l-2 -3 l-3 3 l-2 -3Z" fill="#fff" {W(2.2)}/><path d="M{x+8} {y-10} q2 -8 {6+ (y//20)} -12" fill="none" stroke="{DG}" stroke-width="2"/>'
            for x, y in [(70, 60), (80, 76), (86, 94), (66, 104)])
    + f(42, 84, d=5, k=0.4) + sp((100, 30, 6)))
I["lubok-museum"] = ("orange", "птица Сирин",
    f'<path d="M40 70 Q40 102 70 104 Q104 104 112 80 Q90 88 84 70Z" fill="{V}" {s()}/>'
    f'<path d="M80 74 Q100 40 122 46 Q110 60 112 80" fill="#C9B6FF" {s()}/>'
    f'<path d="M50 104 Q40 116 24 116 Q34 104 44 100" fill="{R}" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="{Y}" {W(1.6)}/>' for x, y in [(60, 88), (74, 94), (88, 86)])
    + f'<circle cx="48" cy="52" r="18" fill="{SK}" {s()}/><path d="M30 46 Q30 28 48 28 Q66 28 66 46 Q58 36 48 38 Q38 36 30 46Z" fill="#7A4A2A" {W(2.4)}/>'
    f'<path d="M34 28 L38 14 L44 24 L48 10 L52 24 L58 14 L62 28Z" fill="{Y}" {s()}/>' + f(48, 54, d=6, k=0.5))
I["apple-museum"] = ("teal", "тамагочи",
    f'<path d="M64 14 Q102 16 104 60 Q106 108 64 112 Q22 108 24 60 Q26 16 64 14Z" fill="{P}" {s()}/>'
    f'<rect x="40" y="36" width="48" height="40" rx="8" fill="#C8E6B0" {s()}/>'
    f'<path d="M58 66 Q54 52 64 50 Q74 52 70 66Z" fill="#2B2A44"/><circle cx="61" cy="57" r="1.6" fill="#fff"/><circle cx="67" cy="57" r="1.6" fill="#fff"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="{Y}" {W(2.2)}/>' for x, y in [(48, 92), (64, 96), (80, 92)])
    + f'<path d="M64 14 V4" {W(3)}/><circle cx="64" cy="4" r="3" fill="{R}"/>')
I["strannoe-mesto"] = ("night", "домовой",
    f'<path d="M30 112 Q26 64 64 60 Q102 64 98 112Z" fill="#8A6E52" {s()}/>'
    f'<path d="M34 64 Q30 30 64 26 Q98 30 94 64 Q92 92 64 94 Q36 92 34 64Z" fill="#B09070" {s()}/>'
    + "".join(f'<path d="M{x} {y} q-6 -10 2 -16" fill="none" stroke="#6B5040" stroke-width="3" stroke-linecap="round"/>' for x, y in [(40, 40), (52, 32), (66, 30), (80, 34), (90, 44)])
    + f'<path d="M44 74 Q64 100 84 74 Q74 86 64 84 Q54 86 44 74Z" fill="#6B5040"/>' + f(64, 60, d=10, k=0.7)
    + f'<path d="M18 112 V96 H30 V112" fill="{Y}" {W(2.2)}/><path d="M24 96 V90" {W(2)}/>' + sp((108, 24, 5)))

# ===================== Парки и животные =====================
I["av-park-mytishchi"] = ("sky", "башня свободного падения",
    GROUND + f'<rect x="56" y="10" width="16" height="96" fill="{R}" {s()}/>'
    + "".join(f'<path d="M56 {y} L72 {y+12}" stroke="#fff" stroke-width="2"/>' for y in range(14, 100, 14))
    + f'<path d="M50 6 H78 L64 0Z" fill="{Y}" {W(2)}/><rect x="36" y="46" width="56" height="16" rx="6" fill="{Y}" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="42" r="5" fill="{SK}" {W(2)}/>' for x in (44, 56, 72, 84)) + f(64, 54, d=6, k=0.42, blush=False)
    + f'<path d="M30 30 v8 M98 30 v8" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')
I["otrada-zoo"] = ("green", "фазан",
    f'<path d="M20 80 Q44 40 74 56 Q90 64 92 80 Q86 96 62 96 Q36 96 20 80Z" fill="#B0502A" {s()}/>'
    f'<path d="M24 82 Q6 90 2 112 Q20 98 34 90Z" fill="#C88A40" {s()}/>'
    f'<path d="M86 66 Q90 40 100 30 Q114 28 112 42 Q104 46 100 64Z" fill="#2E7A6A" {s()}/><path d="M86 64 Q96 70 102 62" stroke="#fff" stroke-width="4"/>'
    f'<path d="M100 32 Q104 36 108 34 Q106 40 100 40Z" fill="{R}"/><path d="M112 38 L120 42 L112 44Z" fill="{Y}" {W(1.6)}/>'
    + "".join(f'<path d="M{x} {y} q4 -4 8 0" fill="none" stroke="#7A3A1A" stroke-width="2"/>' for x, y in [(44, 74), (56, 80), (68, 72), (52, 66)])
    + eye(106, 36, 0.4) + f'<path d="M58 96 V112 M70 96 V112" {W(3)}/>' + GROUND[:0])
I["russian-alpacas"] = ("yellow", "цесарка",
    f'<path d="M24 76 Q24 46 60 44 Q96 44 100 70 Q100 96 64 98 Q30 98 24 76Z" fill="#5A6078" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#fff"/>' for x in range(34, 96, 9) for y in (60, 72, 84) if (x + y) % 2 == 0)
    + f'<path d="M88 56 Q92 32 104 30 Q114 32 112 46 L106 60Z" fill="#7FD3F7" {s()}/>'
    f'<path d="M104 30 L108 20 L112 30Z" fill="#E0A040" {W(1.6)}/><path d="M112 44 L122 46 L112 50Z" fill="{R}" {W(1.6)}/>'
    f'<ellipse cx="108" cy="52" rx="3" ry="5" fill="{R}"/>' + eye(106, 40, 0.45) + f'<path d="M54 98 V114 M70 98 V114" {W(3)}/>')

# ===================== Игры =====================
I["aw-narofominsk"] = ("purple", "грифон",
    f'<path d="M30 80 Q30 60 56 60 H82 Q100 60 100 80 Q100 96 82 96 H48 Q30 96 30 80Z" fill="#E0B060" {s()}/>'
    f'<path d="M40 96 V112 M56 96 V112 M76 96 V112 M90 94 V110" {W(5)}/><path d="M30 80 Q14 74 12 58" fill="none" stroke="#E0B060" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M50 64 Q40 30 70 18 Q66 36 80 34 Q74 50 70 66Z" fill="#F2E2C0" {s()}/>'
    f'<circle cx="94" cy="50" r="16" fill="#fff" {s()}/><path d="M106 50 L120 56 L106 60Z" fill="{Y}" {s()}/>'
    + eye(98, 46, 0.5) + f'<path d="M84 38 L88 30 L94 36" fill="#fff" {W(2)}/>' + sp((20, 24, 6), (114, 110, 5)))
I["aw-reutov"] = ("orange", "шахтёрская вагонетка",
    f'<path d="M4 108 H124" {W(4)}/><path d="M12 116 h8 M36 116 h8 M60 116 h8 M84 116 h8 M108 116 h8" stroke="{BR}" stroke-width="5"/>'
    f'<path d="M20 50 H108 L98 96 H30Z" fill="#8C93A8" {s()}/><path d="M24 62 H104" {W(2)}/>'
    + "".join(f'<path d="M{x} {y} l8 -10 l10 4 l2 10 l-12 4Z" fill="#5A5870" {W(2)}/>' for x, y in [(30, 50), (50, 46), (70, 50), (88, 48)])
    + f'<path d="M58 38 l6 -8 l6 8 l-6 6Z" fill="{Y}" {W(2)}/>' + f(64, 78, d=9, k=0.55)
    + "".join(f'<circle cx="{x}" cy="100" r="8" fill="#2B2A44" {s()}/>' for x in (42, 86)))
I["aw-dmitrov"] = ("teal", "циклоп",
    f'<path d="M28 128 Q28 86 64 84 Q100 86 100 128Z" fill="#8A6E52" {s()}/>'
    f'<circle cx="64" cy="58" r="34" fill="#9BD08A" {s()}/><path d="M44 30 L38 14 L52 26 M84 30 L90 14 L76 26" fill="#F2EAD8" {W(2.4)}/>'
    f'<circle cx="64" cy="52" r="14" fill="#fff" {s()}/>' + eye(64, 52, 1.6)
    + f'<path d="M50 74 Q64 86 78 74" fill="none" {W(3)}/><path d="M56 78 v5 M72 78 v5" stroke="#fff" stroke-width="3"/>')
I["aw-lubertsy"] = ("pink", "минотавр",
    f'<path d="M30 128 Q30 92 64 90 Q98 92 98 128Z" fill="#C88A6A" {s()}/>'
    f'<path d="M40 40 Q14 40 14 16 Q26 30 42 28 M88 40 Q114 40 114 16 Q102 30 86 28" fill="#F2EAD8" {s()}/>'
    f'<path d="M36 50 Q36 22 64 22 Q92 22 92 50 Q92 74 82 84 Q64 96 46 84 Q36 74 36 50Z" fill="#8A5A3E" {s()}/>'
    f'<ellipse cx="64" cy="74" rx="16" ry="11" fill="#D9A88A" {W(2.4)}/><circle cx="58" cy="74" r="2.4" fill="{O}"/><circle cx="70" cy="74" r="2.4" fill="{O}"/>'
    f'<circle cx="64" cy="84" r="6" fill="none" stroke="{Y}" stroke-width="3"/>' + f(64, 52, d=10, k=0.7, mouth=False))
I["aw-mytishchi"] = ("green", "кентавр",
    GROUND + f'<path d="M52 66 Q52 54 70 54 H96 Q112 54 112 70 Q112 84 98 84 H64 Q52 84 52 74Z" fill="#B07A44" {s()}/>'
    f'<path d="M60 84 V106 M74 84 V106 M92 84 V106 M104 82 V104" {W(5)}/><path d="M112 66 Q124 70 122 90" fill="none" stroke="#5A3A20" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M48 70 Q42 50 50 36 H66 Q72 50 66 70Z" fill="{SK}" {s()}/><circle cx="58" cy="26" r="13" fill="{SK}" {s()}/>'
    f'<path d="M46 24 Q46 10 58 10 Q72 10 70 24 Q62 16 46 24Z" fill="#5A3A20" {W(2.2)}/>' + f(58, 28, d=5, k=0.45)
    + f'<path d="M30 30 Q24 50 30 70 M30 30 Q40 50 30 70 M30 50 H46" fill="none" {W(2.6)}/>')
I["flytour-kolomna"] = ("sky", "планер",
    f'<path d="M6 58 Q64 48 122 58 L122 64 Q64 58 6 64Z" fill="#fff" {s()}/>'
    f'<path d="M28 60 Q40 50 64 50 Q96 50 104 60 Q96 70 64 70 Q40 70 28 60Z" fill="#fff" {s()}/>'
    f'<path d="M98 60 L112 36 H118 L114 62Z" fill="{R}" {s()}/><path d="M104 64 L118 66 L104 70Z" fill="#fff" {W(2)}/>'
    f'<path d="M36 58 Q44 50 54 52 Q52 60 40 62Z" fill="#BFE9FF" {W(2)}/>' + f(68, 61, d=6, k=0.42)
    + f'<path d="M14 92 Q30 84 46 92 Q60 82 78 92" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".8"/>' + sp((30, 26, 6)))
I["vr-home"] = ("yellow", "сфинкс",
    f'<path d="M4 112 L44 40 L84 112Z" fill="#E8C87A" {s()}/><path d="M44 40 L56 112" {W(2)} opacity=".5"/>'
    f'<path d="M40 112 V90 Q40 80 52 80 H98 Q112 80 112 92 V112Z" fill="#D9A85A" {s()}/>'
    f'<path d="M84 80 V56 Q84 44 98 44 Q112 44 112 56 V80Z" fill="#D9A85A" {s()}/>'
    f'<path d="M80 60 Q78 42 98 38 Q118 42 116 60 L112 80 H84Z" fill="{B}" opacity=".9" {W(2.4)}/><path d="M86 52 H110 V74 H86Z" fill="#E8C87A" {W(2)}/>'
    + f(98, 62, d=5, k=0.42) + f'<path d="M50 112 V100 H66 V112" fill="#E8C87A" {W(2)}/>' + sp((110, 18, 7)))
I["warpoint-lubertsy"] = ("night", "чёрная дыра",
    "".join(f'<ellipse cx="64" cy="64" rx="{rx}" ry="{rx*0.42:.0f}" fill="none" stroke="{c}" stroke-width="{w}" transform="rotate(-18 64 64)"/>'
            for rx, c, w in [(56, "#FFB45E", 6), (46, "#FF7A3D", 5), (36, "#FFD25E", 4)])
    + f'<circle cx="64" cy="64" r="22" fill="#14122A" {s()}/>' + f(64, 64, d=7, k=0.55, blush=False)
    + f'<path d="M30 70 Q64 92 98 58" fill="none" stroke="#FFB45E" stroke-width="5" transform="rotate(-18 64 64)"/>'
    + sp((20, 20, 5), (110, 24, 6), (104, 108, 4)))
I["limestone-climb"] = ("sky", "снежный барс",
    f'<path d="M0 98 L30 60 L50 80 L80 40 L128 92 V128 H0Z" fill="#E4E8F2" {s()}/>'
    f'<path d="M30 92 Q32 72 58 72 H84 Q100 72 100 88 Q100 102 86 102 H46 Q30 102 30 92Z" fill="#F4F4F0" {s()}/>'
    f'<path d="M30 92 Q12 96 10 76 Q8 62 22 62" fill="none" stroke="#F4F4F0" stroke-width="10" stroke-linecap="round"/><path d="M30 92 Q12 96 10 76 Q8 62 22 62" fill="none" {W(2)} opacity=".25"/>'
    f'<circle cx="96" cy="66" r="18" fill="#F4F4F0" {s()}/><path d="M82 52 l2 -10 l8 8 M110 52 l-2 -10 l-8 8" fill="#F4F4F0" {W(2.2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3.4" fill="none" stroke="#5A6078" stroke-width="2"/>' for x, y in [(44, 82), (58, 90), (72, 82), (84, 94), (50, 96)])
    + f(96, 68, d=7, k=0.5))
I["qwestern-leningradsky"] = ("orange", "перекати-поле",
    f'<path d="M0 108 Q64 98 128 108 V128 H0Z" fill="#E8C87A" {W(2.6)}/>'
    f'<circle cx="64" cy="70" r="32" fill="#D9B07A" {s()}/>'
    + "".join(f'<path d="M{64+30*__import__("math").cos(a):.0f} {70+30*__import__("math").sin(a):.0f} Q64 70 {64+30*__import__("math").cos(a+2.4):.0f} {70+30*__import__("math").sin(a+2.4):.0f}" fill="none" stroke="#8A6E52" stroke-width="2.4"/>' for a in [i*0.7 for i in range(9)])
    + f(64, 70, d=8, k=0.55) + f'<path d="M14 64 h14 M10 76 h12 M16 88 h10" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    + f'<circle cx="106" cy="24" r="12" fill="{Y}" {W(2.4)}/>')
I["claustrophobia-mira"] = ("purple", "мумия",
    f'<path d="M36 120 V56 Q36 28 64 28 Q92 28 92 56 V120Z" fill="#F2EAD8" {s()}/>'
    + "".join(f'<path d="M36 {y} Q64 {y+d} 92 {y-4}" fill="none" stroke="#C9BFA8" stroke-width="2.6"/>' for y, d in [(44, 6), (66, -6), (80, 6), (94, -4), (108, 6)])
    + f'<rect x="44" y="48" width="40" height="16" rx="8" fill="#2B2A44"/>' + f(64, 56, d=8, k=0.6, mouth=False, blush=False)
    + f'<path d="M92 80 L112 74 M36 84 L16 78" stroke="#F2EAD8" stroke-width="10" stroke-linecap="round"/>'
    + f'<path d="M92 80 L112 74" {W(2)} opacity=".3"/><path d="M58 70 Q64 74 70 70" fill="none" {W(2.4)}/>')
I["lemans-karting"] = ("green", "квадроцикл",
    f'<path d="M24 68 Q30 52 50 52 H84 Q102 52 106 68 L110 76 H20Z" fill="{OR}" {s()}/>'
    f'<path d="M50 52 Q52 40 66 40 H76 L80 52" fill="#2B2A44" {s()}/><path d="M86 46 L98 36 M98 36 H108" {W(4)}/>'
    + "".join(f'<circle cx="{x}" cy="88" r="17" fill="#2B2A44" {s()}/><circle cx="{x}" cy="88" r="7" fill="{GR}" {W(2)}/>' for x in (34, 96))
    + f(64, 64, d=7, k=0.45) + f'<path d="M4 108 Q64 100 124 108" fill="none" stroke="#8A6E52" stroke-width="5" stroke-linecap="round"/>')
I["mayak-karting"] = ("sky", "снегоход",
    f'<path d="M0 104 Q64 94 128 104 V128 H0Z" fill="#fff" {W(2.6)}/>'
    f'<path d="M20 98 H94 Q108 98 116 86" fill="none" {W(4)}/><path d="M84 98 Q108 98 118 92" fill="none" {W(4)}/>'
    f'<path d="M24 84 Q24 62 46 60 L70 58 L86 42 H96 L104 76 Q104 88 88 88 H30Z" fill="{R}" {s()}/>'
    f'<path d="M86 42 L80 30 L92 28" fill="none" {W(3)}/><path d="M30 62 Q40 50 66 52 L60 62Z" fill="#2B2A44" {W(2)}/>'
    f'<rect x="28" y="84" width="56" height="12" rx="6" fill="#2B2A44" {W(2.4)}/>' + f(66, 72, d=7, k=0.45) + sp((24, 26, 6), (100, 18, 5)))
I["tushino-paintball"] = ("teal", "геккон",
    f'<path d="M64 20 Q80 22 80 40 Q80 60 70 78 Q62 96 70 114 Q76 122 86 118" fill="none" stroke="{G}" stroke-width="14" stroke-linecap="round"/>'
    f'<path d="M64 20 Q80 22 80 40 Q80 60 70 78 Q62 96 70 114 Q76 122 86 118" fill="none" {W(2.4)} opacity=".35"/>'
    f'<ellipse cx="64" cy="26" rx="16" ry="14" fill="{G}" {s()}/>' + f(64, 24, d=7, k=0.55)
    + "".join(f'<path d="M{a} {b} L{c} {d}" stroke="{G}" stroke-width="6" stroke-linecap="round"/><circle cx="{c}" cy="{d}" r="4" fill="#9BE07A" {W(1.6)}/>'
              for a, b, c, d in [(76, 44, 98, 36), (78, 50, 54, 46), (68, 86, 92, 94), (66, 92, 44, 98)])
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="{Y}"/>' for x, y in [(78, 58), (70, 74), (66, 100)]))
I["chernaya-metka"] = ("blue", "рыба-фугу",
    WATER + f'<circle cx="62" cy="62" r="34" fill="{Y}" {s()}/>'
    + "".join(f'<path d="M{62+34*__import__("math").cos(a):.0f} {62+34*__import__("math").sin(a):.0f} l{8*__import__("math").cos(a):.0f} {8*__import__("math").sin(a):.0f}" {W(2.6)}/>' for a in [i*0.52 for i in range(12)])
    + f'<path d="M96 62 L114 50 V74Z" fill="{OR}" {s()}/><ellipse cx="60" cy="78" rx="20" ry="10" fill="#FFF3C4"/>'
    + f(52, 58, d=9, k=0.7, mouth=False) + f'<circle cx="52" cy="74" r="4" fill="{O}"/>')

# --- перерисовки после просмотра ---
import math as _m
I["pavlovsky-cinema"] = ("green", "еловая шишка",
    f'<path d="M64 18 V6" stroke="{BR}" stroke-width="5" stroke-linecap="round"/><path d="M62 10 Q50 0 42 10 Q54 14 62 10Z" fill="{DG}" {W(2)}/>'
    + f'<path d="M64 16 Q98 36 92 80 Q86 114 64 120 Q42 114 36 80 Q30 36 64 16Z" fill="#9A6234" {s()}/>'
    + "".join(f'<path d="M{x-9} {y} Q{x} {y+14} {x+9} {y}" fill="#C88A50" {W(2.2)}/>'
              for y, xs in [(30, (58, 70)), (44, (46, 64, 82)), (60, (42, 58, 74, 88)), (76, (42, 58, 74, 88)), (92, (48, 64, 80)), (106, (58, 70))] for x in xs)
    + f(64, 66, d=8, k=0.5, blush=False))
I["tushino-paintball"] = ("teal", "геккон",
    "".join(f'<path d="M{a} {b} Q{(a+c)//2} {d-6} {c} {d}" fill="none" stroke="#5CB84A" stroke-width="7" stroke-linecap="round"/>'
            + "".join(f'<circle cx="{c+ex}" cy="{d+ey}" r="3.6" fill="#9BE07A" {W(1.4)}/>' for ex, ey in [(-5, -3), (0, -6), (5, -3)])
            for a, b, c, d in [(56, 50, 30, 36), (72, 50, 98, 36), (56, 82, 30, 98), (72, 82, 98, 98)])
    + f'<path d="M64 88 Q66 108 82 112 Q96 114 100 104" fill="none" stroke="#5CB84A" stroke-width="10" stroke-linecap="round"/>'
    + f'<ellipse cx="64" cy="66" rx="14" ry="26" fill="#5CB84A" {s()}/><ellipse cx="64" cy="32" rx="16" ry="14" fill="#5CB84A" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="{Y}"/>' for x, y in [(60, 56), (68, 66), (60, 76), (68, 86)])
    + f(64, 30, d=7, k=0.55))
I["qwestern-leningradsky"] = ("orange", "перекати-поле",
    f'<path d="M0 108 Q64 98 128 108 V128 H0Z" fill="#E8C87A" {W(2.6)}/>'
    + "".join(f'<path d="M{64+30*_m.cos(a):.0f} {70+28*_m.sin(a):.0f} Q{64+50*_m.cos(a+1.3):.0f} {70+40*_m.sin(a+1.3):.0f} {64+28*_m.cos(a+2.9):.0f} {70+26*_m.sin(a+2.9):.0f}" fill="none" stroke="#9A7A50" stroke-width="3" stroke-linecap="round"/>'
              for a in [i*0.83 for i in range(14)])
    + "".join(f'<path d="M{64+18*_m.cos(a):.0f} {70+18*_m.sin(a):.0f} q{8*_m.cos(a+1):.0f} {8*_m.sin(a+1):.0f} {14*_m.cos(a+.3):.0f} {14*_m.sin(a+.3):.0f}" fill="none" stroke="#B89060" stroke-width="2.4"/>' for a in [i*1.1 for i in range(6)])
    + f'<ellipse cx="64" cy="70" rx="16" ry="13" fill="#E0C090" {W(2.4)}/>' + f(64, 70, d=6, k=0.45)
    + f'<path d="M8 60 h14 M4 74 h14 M10 88 h10" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    + f'<circle cx="108" cy="22" r="11" fill="{Y}" {W(2.4)}/>')

if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        bg, subj, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(bg, body))
    print("svg:", len(ids))
