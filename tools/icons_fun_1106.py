"""Иконки робота fun (2026-11-06, ночь): 57 новых сюжетов — сказочные персонажи, игрушки, животные, транспорт,
природа, космос. Каждый сюжет сверен с icons-catalog/sheet-*.png и icons-src/subjects.txt (не повторяется).
Запуск: python3 tools/icons_fun_1106.py [id ...]"""
import os, sys, math as _m
from draw_icons import svg, s, eye, face, sparkle, O
W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=9, k=0.75, **kw: face(cx, cy, d=d, k=k, **kw)
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
R, OR, Y, G, B, P, V, BR, WH, GR = ("#E8654F", "#FF9A3D", "#FFD25E", "#7CD26E", "#5CB7F2", "#FF8FB8", "#A98BF0",
                                    "#C0732E", "#FFFFFF", "#B8BCCB")
DG, SK, TE, DB = "#4E9A5A", "#FFD9B8", "#5CCDBA", "#8A5A3C"
sp = lambda *pts: "".join(sparkle(x, y, r) for x, y, r in pts)
GROUND = f'<path d="M0 104 Q64 92 128 104 V128 H0Z" fill="{G}" {W(2.6)}/>'
WATER = f'<path d="M0 100 Q16 92 32 100 T64 100 T96 100 T128 100 V128 H0Z" fill="#7FD3F7" {W(2.6)}/>'
SAND = f'<path d="M0 106 Q64 96 128 106 V128 H0Z" fill="#E8C87A" {W(2.6)}/>'


def kid(cx, cy, r=14, hair="#7A4A2A", skin=SK):
    """голова ребёнка/персонажа"""
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{skin}" {s()}/>' + f(cx, cy + 1, d=r * 0.38, k=r / 22)


I = {}
# ===================== Театры: сказочные персонажи =====================
I["mosspectacle"] = ("pink", "принцесса на горошине",
    "".join(f'<rect x="{30+i%2*3}" y="{96-i*12}" width="{68-i%2*6}" height="12" rx="5" fill="{c}" {W(2.6)}/>'
            for i, c in enumerate([B, Y, G, P, V]))
    + f'<rect x="22" y="104" width="84" height="8" rx="3" fill="{BR}" {W(2.6)}/>'
    + kid(64, 34, 13) + f'<path d="M52 26 L56 16 L64 24 L72 16 L76 26Z" fill="{Y}" {W(2.4)}/>'
    + f'<path d="M48 48 Q64 40 80 48" fill="{P}" {W(2.4)}/><circle cx="96" cy="104" r="4" fill="{G}" {W(2)}/>'
    + sp((18, 30, 6), (110, 30, 5)))
I["funny-bell"] = ("green", "Красная Шапочка",
    GROUND + f'<path d="M40 112 L50 62 H78 L88 112Z" fill="{R}" {s()}/>'
    + f'<path d="M40 52 Q64 10 88 52 Q90 72 80 74 L48 74 Q38 72 40 52Z" fill="{R}" {s()}/>' + kid(64, 54, 15)
    + f'<path d="M86 92 h22 l-4 16 h-14Z" fill="{BR}" {W(2.4)}/><path d="M88 92 Q97 80 106 92" fill="none" {W(2.4)}/>'
    + f'<circle cx="94" cy="90" r="3" fill="{Y}"/><circle cx="100" cy="90" r="3" fill="{R}"/>')
I["most-main"] = ("yellow", "Мальчик-с-пальчик на листке",
    f'<path d="M14 92 Q50 52 112 70 Q84 108 14 92Z" fill="{G}" {s()}/><path d="M18 92 Q60 80 108 72" fill="none" stroke="{DG}" stroke-width="3"/>'
    + f'<path d="M56 86 L60 64 H72 L76 84Z" fill="{B}" {W(2.6)}/>' + kid(66, 52, 11)
    + f'<path d="M56 44 Q66 30 76 44Z" fill="{R}" {W(2.4)}/><path d="M76 66 L90 52" {W(3)}/><circle cx="91" cy="50" r="3" fill="{Y}" {W(2)}/>'
    + sp((24, 30, 6), (104, 28, 5)))
I["mayakovsky-sretenka"] = ("orange", "Емеля на печи",
    f'<path d="M22 112 V66 H92 V112Z" fill="#fff" {s()}/><path d="M92 112 V40 H108 V112Z" fill="#fff" {s()}/>'
    f'<path d="M96 40 V24 H104 V40" fill="{GR}" {W(2.6)}/><path d="M40 112 Q40 88 56 88 Q72 88 72 112Z" fill="#3B3355" {W(2.6)}/>'
    f'<path d="M46 112 Q56 96 66 112" fill="{OR}"/>'
    + kid(54, 50, 13) + f'<path d="M42 46 Q54 30 68 46" fill="{R}" {W(2.4)}/><path d="M36 66 Q56 56 80 66" fill="{Y}" {W(2.6)}/>'
    + f'<path d="M100 18 Q106 10 100 4" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')
I["mayakovsky-main"] = ("night", "Кощей Бессмертный",
    f'<path d="M40 128 L48 74 H80 L88 128Z" fill="#5A4E8A" {s()}/><path d="M48 80 L64 96 L80 80" fill="none" stroke="{Y}" stroke-width="3"/>'
    f'<ellipse cx="64" cy="54" rx="15" ry="20" fill="#E4E8D8" {s()}/>'
    + f(64, 50, d=6, k=0.6, blush=False) + f'<path d="M52 66 Q64 80 76 66" fill="#B8BCCB" {W(2.2)}/>'
    f'<path d="M48 36 L52 20 L58 32 L64 16 L70 32 L76 20 L80 36Z" fill="{Y}" {W(2.4)}/>'
    f'<ellipse cx="100" cy="94" rx="9" ry="12" fill="#fff" {W(2.4)}/><path d="M96 92 h8" stroke="{R}" stroke-width="2"/>'
    + sp((20, 30, 6), (108, 40, 5)))
I["rosta-theatre"] = ("pink", "Дюймовочка в тюльпане",
    f'<path d="M64 128 V84" stroke="{DG}" stroke-width="5"/><path d="M64 110 Q40 100 34 84 Q54 88 64 104" fill="{G}" {W(2.4)}/>'
    f'<path d="M34 50 Q34 92 64 92 Q94 92 94 50 L80 64 L64 44 L48 64Z" fill="{R}" {s()}/>'
    + kid(64, 56, 11) + f'<path d="M54 50 Q64 40 74 50" fill="{Y}" {W(2.2)}/>'
    + f'<ellipse cx="50" cy="40" rx="9" ry="5" fill="#E8F4FF" opacity=".9" {W(2)}/><ellipse cx="78" cy="40" rx="9" ry="5" fill="#E8F4FF" opacity=".9" {W(2)}/>'
    + sp((22, 26, 6), (106, 24, 6)))
I["tsd-theatre"] = ("purple", "карета-тыква",
    f'<path d="M24 80 Q24 40 64 40 Q104 40 104 80 Q104 96 64 96 Q24 96 24 80Z" fill="{OR}" {s()}/>'
    + "".join(f'<path d="M{x} 42 Q{x+(64-x)*.2} 68 {x} 94" fill="none" {W(2.2)}/>' for x in (46, 82))
    + f'<path d="M64 40 V28 Q72 24 74 18" fill="none" stroke="{DG}" stroke-width="4" stroke-linecap="round"/>'
    + f'<rect x="54" y="58" width="20" height="18" rx="6" fill="#FFF3C4" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="102" r="12" fill="#fff" {s()}/><circle cx="{x}" cy="102" r="3" fill="{Y}" {W(2)}/>' for x in (38, 90))
    + f(64, 82, d=8, k=0.55) + sp((20, 30, 6), (108, 28, 5)))
I["music-museum-kids"] = ("teal", "гусли-самогуды",
    f'<path d="M18 92 L40 40 Q64 30 104 56 L110 96 Q64 108 18 92Z" fill="#E0A85C" {s()}/>'
    + "".join(f'<path d="M{30+i*9} {84+i} L{44+i*8} {44+i*2}" stroke="#fff" stroke-width="2"/>' for i in range(7))
    + f'<circle cx="76" cy="80" r="10" fill="{BR}" {W(2.4)}/>' + f(76, 64, d=7, k=0.55)
    + "".join(f'<path d="M{x} {y} q4 -8 0 -14 l6 2" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' for x, y in [(98, 38), (110, 52)])
    + sp((22, 28, 6)))
# ===================== Театры: животные =====================


def animal(body, head, extra=""):
    return body + head + extra


I["na-naberezhnoy"] = ("blue", "ламантин",
    WATER.replace('#7FD3F7', '#9FDEF7') + f'<path d="M20 70 Q30 44 66 46 Q96 48 104 66 L118 54 Q120 76 110 84 Q100 92 70 92 Q24 92 20 70Z" fill="#A9A3B8" {s()}/>'
    f'<path d="M48 88 Q44 100 54 100" fill="#A9A3B8" {W(2.6)}/><ellipse cx="30" cy="72" rx="9" ry="7" fill="#C6C0D2" {W(2.4)}/>'
    + f(40, 62, d=6, k=0.6) + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#fff" {W(1.8)}/>' for x, y in [(80, 30), (88, 20)]))
I["inside-studio"] = ("green", "сурок",
    GROUND + f'<ellipse cx="64" cy="80" rx="26" ry="28" fill="#C08A55" {s()}/><ellipse cx="64" cy="88" rx="15" ry="16" fill="#E8C49A" {W(2.4)}/>'
    f'<circle cx="64" cy="46" r="20" fill="#C08A55" {s()}/><circle cx="48" cy="30" r="5" fill="#C08A55" {W(2.4)}/><circle cx="80" cy="30" r="5" fill="#C08A55" {W(2.4)}/>'
    f'<ellipse cx="64" cy="54" rx="9" ry="6" fill="#E8C49A" {W(2.2)}/><rect x="60" y="58" width="8" height="6" fill="#fff" {W(1.6)}/>'
    + f(64, 44, d=8, k=0.65, mouth=False) + f'<path d="M50 74 Q56 70 60 76 M78 74 Q72 70 68 76" fill="none" {W(2.4)}/>')
I["kovcheg-sp"] = ("orange", "вомбат",
    SAND + f'<path d="M22 96 Q20 52 64 52 Q108 52 106 96Z" fill="#9C7A5C" {s()}/>'
    f'<circle cx="40" cy="64" r="22" fill="#9C7A5C" {s()}/><circle cx="26" cy="46" r="6" fill="#9C7A5C" {W(2.4)}/><circle cx="50" cy="44" r="6" fill="#9C7A5C" {W(2.4)}/>'
    f'<ellipse cx="36" cy="74" rx="10" ry="7" fill="#3B3355"/>' + f(40, 60, d=8, k=0.6, mouth=False)
    + "".join(f'<rect x="{x}" y="94" width="10" height="10" rx="4" fill="#9C7A5C" {W(2.4)}/>' for x in (36, 84)))
I["vishnevy-sad"] = ("sky", "снегирь на ветке",
    f'<path d="M10 96 Q60 84 118 92" fill="none" stroke="{DB}" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M90 90 l10 -14 M40 88 l-6 -12" stroke="{DB}" stroke-width="4" stroke-linecap="round"/>'
    f'<circle cx="34" cy="74" r="5" fill="{R}" {W(2)}/><circle cx="100" cy="74" r="5" fill="{R}" {W(2)}/>'
    f'<path d="M90 64 L112 76 L92 78Z" fill="#3B3355"/><ellipse cx="66" cy="64" rx="28" ry="24" fill="{R}" {s()}/>'
    f'<path d="M58 40 Q80 36 92 60 Q76 52 58 56Z" fill="#6B7290" {W(2.4)}/><path d="M42 50 Q50 34 66 40 Q50 44 44 58Z" fill="#3B3355"/>'
    f'<path d="M38 56 L28 60 L38 64Z" fill="#3B3355"/>' + f(50, 58, d=5, k=0.55, mouth=False)
    + f'<path d="M58 88 v8 M70 88 v8" {W(2.6)}/>' + sp((20, 22, 5), (108, 26, 6)))
I["tepigra"] = ("purple", "шиншилла",
    f'<ellipse cx="64" cy="86" rx="30" ry="28" fill="#C6C8D6" {s()}/><path d="M92 96 Q114 90 112 70" fill="none" stroke="#C6C8D6" stroke-width="12" stroke-linecap="round"/>'
    f'<ellipse cx="38" cy="40" rx="14" ry="18" fill="#C6C8D6" {s()}/><ellipse cx="90" cy="40" rx="14" ry="18" fill="#C6C8D6" {s()}/>'
    f'<ellipse cx="38" cy="40" rx="7" ry="10" fill="{P}"/><ellipse cx="90" cy="40" rx="7" ry="10" fill="{P}"/>'
    f'<circle cx="64" cy="62" r="24" fill="#D8DAE6" {s()}/><circle cx="64" cy="70" r="3" fill="{P}"/>'
    + f(64, 60, d=10, k=0.8, mouth=False) + "".join(f'<path d="M{x} 72 l{dx} {dy}" {W(1.6)}/>' for x, dx, dy in [(56, -14, -2), (56, -14, 4), (72, 14, -2), (72, 14, 4)])
    + sp((20, 100, 5)))
I["shalom-novoslobodskaya"] = ("teal", "тапир",
    GROUND + f'<ellipse cx="70" cy="74" rx="36" ry="24" fill="#4E4A66" {s()}/><path d="M48 70 H92 V92 Q70 98 48 92Z" fill="#fff" {W(2.4)}/>'
    + "".join(f'<rect x="{x}" y="90" width="10" height="16" rx="4" fill="#4E4A66" {W(2.4)}/>' for x in (44, 60, 82, 96))
    + f'<circle cx="34" cy="62" r="18" fill="#4E4A66" {s()}/><path d="M18 62 Q6 66 10 80" fill="none" stroke="#4E4A66" stroke-width="9" stroke-linecap="round"/>'
    f'<ellipse cx="40" cy="44" rx="5" ry="7" fill="#4E4A66" {W(2.2)}/><circle cx="32" cy="58" r="6" fill="#fff"/>' + eye(32, 58, 0.8)
    + f'<circle cx="104" cy="24" r="10" fill="{Y}" {W(2.4)}/>')
I["shalom-varshavka"] = ("yellow", "панголин",
    SAND + f'<path d="M24 96 Q20 44 70 44 Q110 46 108 92 Q96 104 60 102 Q34 102 24 96Z" fill="#C8955A" {s()}/>'
    + "".join(f'<path d="M{x} {y} q8 -10 16 0" fill="#B07A44" {W(2.2)}/>' for x, y in
              [(40, 62), (58, 54), (76, 54), (92, 64), (34, 78), (52, 72), (70, 70), (88, 78), (48, 88), (68, 86)])
    + f'<path d="M108 88 Q122 96 116 110 Q104 112 100 100" fill="#C8955A" {W(2.6)}/>'
    + f'<path d="M24 84 Q8 86 10 98 Q20 102 30 96" fill="#E0B482" {W(2.6)}/>' + eye(20, 90, 0.7))
I["shchelkovo-theatre"] = ("green", "богомол",
    f'<path d="M20 116 Q64 104 108 116" fill="none" stroke="{DG}" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M50 110 L58 80 M78 110 L70 80 M44 112 L54 90" stroke="#5FBF55" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M56 96 Q48 64 60 52 Q72 56 72 96Z" fill="#7FD46E" {s()}/>'
    f'<path d="M62 56 L44 44 L36 58 M62 60 L80 44 L90 56" fill="none" stroke="#5FBF55" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
    f'<path d="M48 40 L64 22 L80 40 Q64 50 48 40Z" fill="#9BE58A" {s()}/>'
    f'<circle cx="50" cy="32" r="6" fill="#fff" {W(2.2)}/><circle cx="78" cy="32" r="6" fill="#fff" {W(2.2)}/>' + eye(50, 32, 0.7) + eye(78, 32, 0.7)
    + f'<path d="M58 20 Q50 8 40 10 M70 20 Q78 8 88 10" fill="none" {W(2)}/>')
I["ermitazh-theatre"] = ("night", "опоссум на ветке",
    f'<path d="M6 46 Q64 34 122 46" fill="none" stroke="{DB}" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M78 44 Q90 30 80 22 Q70 22 74 34" fill="none" stroke="#F0C8D0" stroke-width="5" stroke-linecap="round"/>'
    f'<ellipse cx="64" cy="64" rx="24" ry="20" fill="#C9C6D4" {s()}/>'
    f'<path d="M44 74 Q34 92 50 98 Q64 104 78 98 Q94 92 84 74Z" fill="#EDEBF2" {s()}/>'
    f'<circle cx="50" cy="84" r="5" fill="#2B2A44"/><circle cx="78" cy="84" r="5" fill="#2B2A44"/>'
    f'<path d="M58 96 L64 104 L70 96Z" fill="{P}" {W(2)}/>' + f(64, 86, d=0, k=0.0, mouth=False, blush=False)
    + eye(54, 86, 0.6) + eye(74, 86, 0.6) + sp((20, 100, 6), (108, 96, 5), (22, 20, 4)))
I["gavit"] = ("orange", "ехидна",
    GROUND + f'<path d="M22 98 Q22 54 66 54 Q104 54 106 98Z" fill="#8A6A50" {s()}/>'
    + "".join(f'<path d="M{x} {y} l{dx} {dy}" stroke="#F4E2C8" stroke-width="4" stroke-linecap="round"/>' for x, y, dx, dy in
              [(40, 64, -6, -14), (52, 58, -2, -16), (66, 56, 2, -16), (80, 58, 6, -14), (92, 66, 10, -10), (48, 74, -4, -12), (62, 70, 0, -14), (76, 72, 4, -12), (88, 80, 10, -8)])
    + f'<ellipse cx="30" cy="88" rx="12" ry="10" fill="#B08A6C" {W(2.6)}/><path d="M20 92 L6 98" stroke="#8A6A50" stroke-width="5" stroke-linecap="round"/>'
    + eye(30, 84, 0.7) + sp((108, 28, 6)))
I["ethno-theatre"] = ("sky", "соболь",
    f'<path d="M0 104 Q64 94 128 104 V128 H0Z" fill="#fff" {W(2.6)}/>'
    f'<path d="M30 96 Q40 66 70 70 Q96 74 100 96Z" fill="#6A4A34" {s()}/>'
    f'<path d="M96 92 Q120 88 116 66 Q106 74 98 78" fill="#6A4A34" {W(2.6)}/>'
    f'<circle cx="40" cy="62" r="18" fill="#7A5640" {s()}/><path d="M28 48 l-2 -10 l8 6 M50 46 l4 -10 l2 10" fill="#7A5640" {W(2.4)}/>'
    f'<path d="M30 72 Q40 80 50 72 Q44 90 34 88Z" fill="#F2C86A" {W(2.2)}/>' + f(40, 60, d=7, k=0.6)
    + sp((20, 24, 6), (104, 28, 5), (80, 40, 4)))
I["cdr-povarskaya"] = ("pink", "морская свинка",
    f'<path d="M14 100 Q64 90 114 100 V112 H14Z" fill="#E8D49A" {W(2.4)}/>'
    f'<ellipse cx="66" cy="76" rx="42" ry="28" fill="#fff" {s()}/><path d="M76 50 Q104 52 106 80 Q96 94 76 90Z" fill="{OR}" {W(2.4)}/>'
    f'<path d="M30 60 Q38 52 48 56 L44 92 Q28 90 26 78Z" fill="#8A5A3C" {W(2.4)}/>'
    f'<ellipse cx="38" cy="54" rx="7" ry="5" fill="{P}" {W(2)}/><circle cx="26" cy="80" r="3" fill="{P}"/>'
    + eye(34, 72, 0.75) + f'<path d="M24 86 Q28 90 32 86" fill="none" {W(2)}/>')
I["armenian-theatre"] = ("yellow", "удод",
    f'<path d="M14 108 H114" stroke="{DB}" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M54 106 v-12 M70 106 v-12" {W(3)}/>'
    f'<path d="M60 84 Q40 82 44 62 Q54 46 78 52 Q100 60 112 92 Q90 92 60 84Z" fill="#E8A868" {s()}/>'
    + "".join(f'<path d="M{x} {y} l12 -4" stroke="#3B3355" stroke-width="3"/><path d="M{x} {y+6} l12 -4" stroke="#fff" stroke-width="3"/>' for x, y in [(80, 66), (88, 74)])
    + "".join(f'<path d="M52 50 L{x} {y}" stroke="{OR}" stroke-width="6" stroke-linecap="round"/><circle cx="{x}" cy="{y}" r="3" fill="#3B3355"/>' for x, y in [(36, 22), (48, 18), (60, 20), (70, 26)])
    + f'<path d="M44 62 L16 72" stroke="{O}" stroke-width="3.4" stroke-linecap="round"/>' + eye(52, 60, 0.7)
    + sp((106, 26, 6)))
I["pushkin-theatre"] = ("blue", "разбитое корыто",
    SAND + f'<path d="M18 74 H110 L98 102 H30Z" fill="#B88A5A" {s()}/><path d="M60 74 L68 88 L58 102" fill="none" {W(3)}/>'
    f'<path d="M24 82 H104" stroke="#9A6E44" stroke-width="2.4"/>' + f(46, 88, d=7, k=0.55)
    + f'<path d="M0 64 Q20 56 40 64 T80 64 T128 64" fill="none" stroke="#fff" stroke-width="3" opacity=".8"/>'
    + f'<path d="M92 50 Q104 36 112 46 Q104 50 100 58Z" fill="{Y}" {W(2.4)}/><path d="M86 58 Q96 46 100 58" fill="{Y}" {W(2.4)}/>'
    + sp((20, 30, 6), (64, 26, 5)))
I["kz-izmailovo"] = ("night", "шапка-невидимка",
    f'<path d="M24 86 Q24 40 64 34 Q104 40 104 86Z" fill="{V}" opacity=".9" {s()}/>'
    f'<path d="M18 84 Q64 74 110 84 Q112 98 64 100 Q16 98 18 84Z" fill="#fff" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.5" fill="#3B3355"/>' for x, y in [(36, 88), (52, 92), (76, 92), (92, 88)])
    + f'<circle cx="64" cy="30" r="7" fill="{Y}" {W(2.4)}/>' + f(64, 64, d=10, k=0.8)
    + "".join(f'<path d="M{x} {y} q-6 6 0 12" fill="none" stroke="#C9B6FF" stroke-width="3" stroke-linecap="round" stroke-dasharray="3 4"/>' for x, y in [(16, 50), (112, 50)])
    + sp((22, 22, 6), (104, 18, 5), (110, 112, 5)))
I["modern-theatre"] = ("night", "звездочёт",
    f'<path d="M30 128 L44 70 H80 L94 128Z" fill="#3E4AA0" {s()}/>'
    + "".join(f'<path d="M{x} {y} l3 6 l-3 6 l-3 -6Z" fill="{Y}"/>' for x, y in [(52, 90), (70, 104), (60, 116)])
    + kid(62, 58, 13) + f'<path d="M64 62 Q60 84 66 90 Q70 80 72 62" fill="#fff" {W(2.2)}/>'
    + f'<path d="M44 48 L60 8 L80 48Z" fill="#3E4AA0" {s()}/><circle cx="62" cy="26" r="3" fill="{Y}"/>'
    + f'<path d="M78 70 L108 40" stroke="{BR}" stroke-width="8" stroke-linecap="round"/><path d="M78 70 L108 40" stroke="{Y}" stroke-width="3"/>'
    + sp((104, 22, 7), (20, 40, 5), (24, 90, 4)))
I["et-cetera"] = ("orange", "волшебный фонарь",
    f'<rect x="20" y="54" width="54" height="44" rx="8" fill="{BR}" {s()}/><path d="M74 66 L92 60 V92 L74 86Z" fill="{GR}" {s()}/>'
    f'<path d="M30 54 V40 H44 V54" fill="{GR}" {W(2.6)}/><path d="M36 40 Q38 30 34 24" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    f'<path d="M92 64 L122 44 V108 L92 88Z" fill="#FFF3A8" opacity=".85"/>'
    f'<circle cx="108" cy="76" r="8" fill="{Y}" {W(2)}/><path d="M104 74 q4 -4 8 0" fill="none" {W(1.8)}/>'
    + f(46, 76, d=8, k=0.65) + "".join(f'<circle cx="{x}" cy="104" r="5" fill="{GR}" {W(2.2)}/>' for x in (30, 64)))
# ===================== Кинотеатры =====================
I["mori-kuntsevo"] = ("orange", "тушканчик",
    SAND + f'<path d="M64 88 Q100 96 112 72" fill="none" {W(3)}/><path d="M110 70 l6 -6 l2 8Z" fill="#fff" {W(2.2)}/>'
    f'<ellipse cx="58" cy="82" rx="18" ry="16" fill="#E8C08A" {s()}/><path d="M60 96 L80 104 L52 104" fill="none" stroke="{O}" stroke-width="3.4" stroke-linejoin="round"/>'
    f'<ellipse cx="44" cy="30" rx="7" ry="20" fill="#E8C08A" transform="rotate(-12 44 30)" {s()}/><ellipse cx="62" cy="28" rx="7" ry="20" fill="#E8C08A" transform="rotate(12 62 28)" {s()}/>'
    f'<circle cx="52" cy="56" r="15" fill="#E8C08A" {s()}/>' + f(52, 56, d=6, k=0.6) + sp((104, 26, 6)))
I["prada3d-balashikha"] = ("green", "окапи",
    GROUND + f'<path d="M44 68 Q46 50 70 52 Q96 54 96 70 L94 82 H46Z" fill="#7A4A34" {s()}/>'
    + "".join(f'<rect x="{x}" y="78" width="9" height="26" rx="3" fill="#fff" {W(2.4)}/><path d="M{x} {84} h9 M{x} 92 h9" stroke="#3B3355" stroke-width="2.6"/>' for x in (48, 60, 80, 88))
    + f'<path d="M92 72 l14 -2 l4 6Z" fill="#fff" {W(2.2)}/><path d="M92 74 h12 M96 78 h12" stroke="#3B3355" stroke-width="2"/>'
    f'<path d="M48 58 L36 34" stroke="#7A4A34" stroke-width="12" stroke-linecap="round"/>'
    f'<ellipse cx="30" cy="32" rx="14" ry="11" fill="#9A6A4C" {s()}/><ellipse cx="20" cy="36" rx="6" ry="5" fill="#C69A7C" {W(2)}/>'
    f'<path d="M34 22 l2 -8 M40 24 l6 -6" {W(2.6)}/>' + eye(32, 30, 0.7))
I["kostino-korolev"] = ("night", "планета Марс",
    f'<circle cx="64" cy="64" r="36" fill="#E8704A" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#C8543A" {W(1.8)}/>' for x, y, r in [(44, 50, 7), (84, 80, 9), (78, 44, 4), (48, 82, 5)])
    + f'<path d="M30 60 Q64 68 98 58" fill="none" stroke="#F8A070" stroke-width="3"/>' + f(64, 64, d=10, k=0.8)
    + f'<circle cx="104" cy="22" r="6" fill="#C8C0B8" {W(2.2)}/><circle cx="22" cy="104" r="4" fill="#C8C0B8" {W(2)}/>'
    + sp((20, 22, 6), (110, 100, 5)))
I["yunost-odintsovo"] = ("sky", "бильбоке",
    f'<path d="M48 120 L58 70" stroke="{BR}" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M36 70 Q36 92 58 92 Q80 92 80 70Z" fill="{R}" {s()}/><ellipse cx="58" cy="70" rx="22" ry="7" fill="#C84A3A" {W(2.6)}/>'
    f'<path d="M78 76 Q100 60 92 34" fill="none" stroke="#fff" stroke-width="2.6" stroke-dasharray="4 3"/>'
    f'<circle cx="92" cy="28" r="12" fill="{Y}" {s()}/>' + f(92, 28, d=4, k=0.45) + f(58, 80, d=8, k=0.55)
    + sp((24, 30, 6)))
I["music-museum-kids"] = I["music-museum-kids"]
# ===================== Игровые, VR, квесты, боулинг =====================
I["brooklyn-bowl-mytishchi"] = ("teal", "муравьед",
    GROUND + f'<path d="M34 72 Q40 52 72 54 Q100 58 100 80 Q96 92 70 92 Q40 92 34 72Z" fill="#9A7A64" {s()}/>'
    f'<path d="M98 66 Q122 50 118 92 Q106 84 98 82" fill="#7A5A46" {W(2.6)}/>'
    f'<path d="M50 60 L78 90" stroke="#3B3355" stroke-width="6"/><path d="M52 58 L80 88" stroke="#fff" stroke-width="3"/>'
    + "".join(f'<rect x="{x}" y="86" width="9" height="16" rx="3" fill="#9A7A64" {W(2.4)}/>' for x in (44, 58, 76, 88))
    + f'<path d="M38 66 Q24 64 10 76 Q22 80 38 78Z" fill="#B09A86" {s()}/>' + eye(34, 66, 0.6)
    + "".join(f'<circle cx="{x}" cy="106" r="2" fill="#3B3355"/>' for x in (14, 20, 26)))
I["zamania-gorod"] = ("yellow", "бочонки лото",
    "".join(f'<rect x="{x}" y="{y}" width="26" height="32" rx="10" fill="#E0B07A" {s()}/><ellipse cx="{x+13}" cy="{y+4}" rx="11" ry="3" fill="#C8955A"/>'
            f'<text x="{x+13}" y="{y+24}" font-family="Arial" font-weight="bold" font-size="14" text-anchor="middle" fill="{c}">{n}</text>'
            for x, y, n, c in [(22, 70, 7, R), (51, 76, 33, B), (80, 66, 90, DG)])
    + f'<path d="M34 50 Q64 28 96 46 L90 62 Q64 50 40 64Z" fill="{R}" {s()}/><path d="M40 64 Q64 50 90 62" fill="none" stroke="#fff" stroke-width="2.4"/>'
    + f(64, 46, d=7, k=0.55) + sp((20, 30, 6), (110, 30, 5)))
I["kidburg-khorosho"] = ("pink", "игрушечная касса",
    f'<path d="M20 70 H108 L102 108 H26Z" fill="{B}" {s()}/><path d="M30 46 H98 L104 70 H24Z" fill="#9FD8F8" {s()}/>'
    + "".join(f'<rect x="{34+i%4*16}" y="{50+i//4*9}" width="10" height="6" rx="2" fill="{c}" {W(1.6)}/>' for i, c in enumerate([R, Y, G, P, Y, G, P, R]))
    + f'<rect x="72" y="22" width="30" height="20" rx="4" fill="#2B2A44" {W(2.4)}/><text x="87" y="37" font-family="Arial" font-weight="bold" font-size="12" text-anchor="middle" fill="{G}">25</text>'
    f'<path d="M80 42 V46 M94 42 V46" {W(2.4)}/><rect x="40" y="90" width="48" height="10" rx="3" fill="#fff" {W(2.2)}/>' + f(64, 80, d=8, k=0.55))
I["aw-krasnogorsk"] = ("night", "реактивный ранец",
    f'<rect x="44" y="36" width="40" height="48" rx="10" fill="{GR}" {s()}/>'
    + "".join(f'<rect x="{x}" y="30" width="14" height="56" rx="7" fill="{R}" {s()}/><path d="M{x+2} 86 L{x+7} 112 L{x+12} 86Z" fill="{Y}" {W(2.2)}/><path d="M{x+4} 86 L{x+7} 100 L{x+10} 86Z" fill="#fff"/>' for x in (30, 84))
    + f'<circle cx="64" cy="54" r="10" fill="#7FD3F7" {W(2.4)}/>' + f(64, 70, d=8, k=0.55)
    + sp((20, 22, 6), (108, 20, 5), (24, 104, 4), (106, 108, 4)))
I["inferno-paintball"] = ("orange", "огненная саламандра",
    GROUND + f'<path d="M20 86 Q40 70 64 80 Q88 90 110 74 Q118 70 116 80 Q100 96 64 92 Q38 92 20 96Z" fill="#2B2A44" {s()}/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="6" ry="3.5" fill="{Y}"/>' for x, y in [(40, 84), (58, 86), (76, 88), (94, 84)])
    + f'<path d="M40 92 l-6 10 M54 92 l4 10 M80 92 l-4 10 M94 88 l6 10" stroke="#2B2A44" stroke-width="5" stroke-linecap="round"/>'
    f'<ellipse cx="22" cy="86" rx="14" ry="10" fill="#2B2A44" {s()}/>' + eye(20, 82, 0.6)
    + f'<circle cx="26" cy="80" r="3" fill="{Y}"/><path d="M98 30 Q104 44 96 52 Q88 44 98 30Z" fill="{OR}" {W(2)}/>')
# ===================== Музеи =====================
I["avtomobili-mira"] = ("blue", "гоночный болид",
    f'<path d="M0 104 H128 V128 H0Z" fill="#8A8FA8"/><path d="M8 112 H28 M44 112 H64 M80 112 H100" stroke="#fff" stroke-width="3"/>'
    f'<path d="M14 84 L36 70 H72 L96 64 L118 76 V88 H14Z" fill="{R}" {s()}/><path d="M104 60 H120 V80" fill="{R}" {W(2.6)}/>'
    f'<path d="M8 74 H22 V90" fill="none" {W(3)}/><path d="M52 70 Q58 56 70 56 Q78 56 80 68" fill="{Y}" {W(2.6)}/>'
    + "".join(f'<circle cx="{x}" cy="92" r="13" fill="#2B2A44" {s()}/><circle cx="{x}" cy="92" r="5" fill="{GR}"/>' for x in (34, 96))
    + f(62, 80, d=7, k=0.55) + f'<path d="M4 60 h14 M2 50 h10" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')
I["bunker-703"] = ("night", "дрезина",
    f'<path d="M0 104 H128" stroke="{GR}" stroke-width="5"/>' + "".join(f'<rect x="{x}" y="104" width="10" height="6" fill="{DB}"/>' for x in range(4, 128, 20))
    + f'<rect x="24" y="76" width="80" height="16" rx="4" fill="{OR}" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="96" r="9" fill="{GR}" {s()}/>' for x in (38, 90))
    + f'<path d="M64 76 V52" {W(4)}/><path d="M38 50 L90 54" stroke="{R}" stroke-width="6" stroke-linecap="round"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="{SK}" {W(2)}/>' for x, y in [(40, 50), (88, 54)])
    + f(64, 84, d=8, k=0.5) + f'<path d="M14 30 L38 70 M114 30 L90 70" stroke="#FFF3A8" stroke-width="2" opacity=".6"/>'
    + f'<circle cx="64" cy="20" r="6" fill="{Y}" {W(2.2)}/>')
I["damuseum"] = ("yellow", "глиняная свистулька-птичка",
    f'<path d="M26 84 Q22 56 54 54 Q70 40 86 50 Q96 40 108 44 Q102 58 94 62 Q102 92 64 96 Q34 98 26 84Z" fill="#fff" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="{c}"/>' for x, y, c in [(44, 76, R), (58, 82, B), (72, 78, G), (52, 66, Y), (80, 66, R)])
    + f'<path d="M38 88 Q64 98 88 82" fill="none" stroke="{R}" stroke-width="3"/><path d="M26 80 L12 76 L22 88Z" fill="{OR}" {W(2.2)}/>'
    + f'<circle cx="64" cy="100" r="10" fill="#fff" {W(2.6)}/><path d="M60 98 h8" stroke="{B}" stroke-width="3"/>' + eye(84, 56, 0.7)
    + "".join(f'<path d="M{x} {y} q6 -4 4 -10" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' for x, y in [(16, 60), (22, 46)]))
I["gmom"] = ("sky", "аэросани",
    f'<path d="M0 100 Q64 92 128 100 V128 H0Z" fill="#fff" {W(2.6)}/>'
    f'<path d="M14 98 H104 Q114 98 116 92" fill="none" stroke="{BR}" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M24 92 L28 66 Q30 56 44 56 H74 L84 92Z" fill="#6E9A62" {s()}/><path d="M36 64 H60 V76 H34Z" fill="#9FD8F8" {W(2.4)}/>'
    f'<path d="M84 70 H94" {W(4)}/><ellipse cx="98" cy="70" rx="4" ry="22" fill="{GR}" {W(2.6)}/>'
    f'<path d="M32 92 v6 M76 92 v6" {W(3)}/>' + f(58, 84, d=7, k=0.5)
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#fff" {W(1.6)}/>' for x, y in [(20, 20), (40, 30), (100, 24), (114, 44)]))
I["dary-duba"] = ("green", "сойка с желудем",
    f'<path d="M8 100 Q64 90 120 100" fill="none" stroke="{DB}" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M86 66 L114 88 L90 84Z" fill="#3E6AB8" {W(2.4)}/><ellipse cx="62" cy="70" rx="30" ry="22" fill="#D8B496" {s()}/>'
    f'<path d="M66 60 Q90 56 96 76 Q80 78 66 72Z" fill="#5CA0E8" {W(2.2)}/><path d="M70 64 h18 M72 70 h18" stroke="#2B2A44" stroke-width="2"/>'
    f'<path d="M40 52 Q44 36 58 44 L52 52Z" fill="#E8D0BA" {W(2.2)}/>' + eye(44, 62, 0.75)
    + f'<path d="M34 66 L24 70 L34 72Z" fill="#3B3355"/><ellipse cx="24" cy="78" rx="6" ry="8" fill="{BR}" {W(2.2)}/><path d="M18 74 Q24 66 30 74Z" fill="#8A5A3C" {W(2)}/>'
    f'<path d="M56 92 v8 M68 92 v8" {W(2.6)}/>' + sp((100, 30, 6)))
I["lomakovka"] = ("sky", "фуникулёр",
    f'<path d="M0 112 L128 40 V128 H0Z" fill="{G}" {W(2.6)}/><path d="M0 104 L128 32" stroke="{GR}" stroke-width="4"/>'
    f'<g transform="rotate(-29 64 70)"><rect x="38" y="48" width="52" height="32" rx="6" fill="{R}" {s()}/>'
    f'<rect x="44" y="54" width="16" height="12" rx="3" fill="#fff" {W(2)}/><rect x="66" y="54" width="16" height="12" rx="3" fill="#fff" {W(2)}/>'
    + f(64, 72, d=7, k=0.5) + '</g>' + f'<circle cx="108" cy="22" r="9" fill="{Y}" {W(2.4)}/>')
I["mirozdanie"] = ("blue", "трилобит",
    f'<path d="M64 18 Q100 20 100 52 Q100 90 64 112 Q28 90 28 52 Q28 20 64 18Z" fill="#B09A86" {s()}/>'
    f'<path d="M64 18 Q84 20 88 40 H40 Q44 20 64 18Z" fill="#C8B4A0" {W(2.4)}/>'
    + "".join(f'<path d="M{34+i*2} {48+i*9} Q64 {54+i*9} {94-i*2} {48+i*9}" fill="none" {W(2)}/>' for i in range(6))
    + f'<path d="M54 40 V100 M74 40 V100" {W(2)}/>' + f(64, 30, d=10, k=0.6, mouth=False)
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#fff" {W(1.6)}/>' for x, y in [(16, 30), (112, 40), (110, 100)]))
I["jinr-museum"] = ("night", "пульсар",
    f'<path d="M64 64 L20 6 L36 2Z M64 64 L108 122 L92 126Z" fill="#9FD8F8" opacity=".7"/>'
    f'<ellipse cx="64" cy="64" rx="48" ry="12" fill="none" stroke="{V}" stroke-width="3" transform="rotate(-20 64 64)"/>'
    f'<circle cx="64" cy="64" r="20" fill="#E8F4FF" {s()}/>' + f(64, 64, d=7, k=0.6)
    + sp((20, 100, 6), (108, 24, 6), (100, 90, 4), (30, 40, 4)))
I["chocolate-sokolniki"] = ("teal", "квокка",
    GROUND + f'<ellipse cx="64" cy="86" rx="26" ry="24" fill="#B8865A" {s()}/><ellipse cx="64" cy="92" rx="15" ry="14" fill="#E4C09A" {W(2.4)}/>'
    f'<circle cx="40" cy="34" r="9" fill="#B8865A" {W(2.6)}/><circle cx="88" cy="34" r="9" fill="#B8865A" {W(2.6)}/>'
    f'<circle cx="64" cy="50" r="24" fill="#B8865A" {s()}/><ellipse cx="64" cy="60" rx="10" ry="7" fill="#E4C09A" {W(2.2)}/>'
    f'<ellipse cx="64" cy="56" rx="4" ry="3" fill="#3B3355"/>' + f(64, 48, d=10, k=0.8, mouth=False)
    + f'<path d="M56 62 Q64 72 72 62" fill="#fff" {W(2.4)}/><path d="M48 80 Q54 74 60 82 M80 80 Q74 74 68 82" fill="none" {W(2.4)}/>')
I["heroes-museum"] = ("sky", "орёл",
    f'<path d="M64 60 Q40 30 6 40 Q24 50 26 60 Q14 64 12 72 Q40 70 64 76 Q88 70 116 72 Q114 64 102 60 Q104 50 122 40 Q88 30 64 60Z" fill="#8A5A3C" {s()}/>'
    f'<path d="M54 74 L50 104 L64 96 L78 104 L74 74Z" fill="#8A5A3C" {s()}/>'
    f'<circle cx="64" cy="54" r="15" fill="#fff" {s()}/><path d="M66 58 L78 62 L68 68Z" fill="{Y}" {W(2.2)}/>' + eye(60, 52, 0.7)
    + f'<path d="M56 104 l-4 8 M72 104 l4 8" stroke="{Y}" stroke-width="4" stroke-linecap="round"/><circle cx="104" cy="104" r="8" fill="{Y}" {W(2.2)}/>')
I["burganov-house"] = ("orange", "носуха",
    f'<path d="M88 84 Q120 70 108 30" fill="none" stroke="#9A6A44" stroke-width="12" stroke-linecap="round"/>'
    + "".join(f'<path d="M{x} {y} l10 -4" stroke="#3B3355" stroke-width="4"/>' for x, y in [(100, 66), (106, 52), (106, 40)])
    + GROUND + f'<ellipse cx="64" cy="84" rx="30" ry="18" fill="#B8865A" {s()}/>'
    + "".join(f'<rect x="{x}" y="92" width="9" height="14" rx="3" fill="#8A5A3C" {W(2.4)}/>' for x in (42, 56, 74, 84))
    + f'<path d="M40 68 Q28 56 34 46 Q46 50 50 64Z" fill="#B8865A" {W(2.6)}/><ellipse cx="36" cy="74" rx="16" ry="12" fill="#C8986A" {s()}/>'
    f'<path d="M24 78 L8 86" stroke="#B8865A" stroke-width="7" stroke-linecap="round"/><circle cx="8" cy="86" r="3" fill="#3B3355"/>'
    f'<path d="M30 74 Q36 80 44 74" fill="#fff" opacity=".7"/>' + eye(34, 70, 0.65))
I["recycling-museum"] = ("green", "дождевой червь",
    f'<path d="M0 90 Q64 80 128 90 V128 H0Z" fill="#8A5A3C" {W(2.6)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#6A4430"/>' for x, y in [(14, 108), (40, 118), (90, 112), (112, 120), (64, 104)])
    + f'<path d="M24 96 Q30 60 56 66 Q80 72 80 50 Q80 30 98 30" fill="none" stroke="#F09AAE" stroke-width="16" stroke-linecap="round"/>'
    + "".join(f'<path d="M{x} {y} l6 6" stroke="#D07890" stroke-width="2"/>' for x, y in [(30, 74), (46, 62), (66, 66), (76, 52)])
    + f'<circle cx="98" cy="30" r="12" fill="#F09AAE" {s()}/>' + f(98, 30, d=5, k=0.5)
    + f'<path d="M14 24 Q24 14 34 24 Q24 30 14 24Z" fill="{DG}" {W(2)}/>')
I["tricks-museum"] = ("green", "лепрекон",
    f'<path d="M80 96 Q80 116 98 116 Q116 116 116 96Z" fill="#3B3355" {s()}/><ellipse cx="98" cy="96" rx="18" ry="5" fill="#2B2A44"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="{Y}" {W(1.8)}/>' for x, y in [(90, 92), (100, 90), (108, 94), (96, 86)])
    + f'<path d="M30 128 L38 82 H68 L76 128Z" fill="{DG}" {s()}/><rect x="38" y="96" width="30" height="6" fill="#3B3355"/><rect x="48" y="94" width="10" height="10" fill="{Y}" {W(1.8)}/>'
    + kid(53, 64, 15) + f'<path d="M40 72 Q53 96 66 72" fill="{OR}" {W(2.4)}/>'
    + f'<path d="M32 50 H74 L68 44 V22 H38 V44Z" fill="{DG}" {s()}/><rect x="38" y="38" width="30" height="5" fill="#3B3355"/>'
    + sp((104, 30, 6), (96, 58, 4)))
I["podolie"] = ("sky", "тетерев",
    f'<path d="M0 108 Q64 98 128 108 V128 H0Z" fill="#fff" {W(2.6)}/>'
    f'<path d="M84 60 Q104 34 118 46 Q106 54 100 70Z" fill="#2B2A44" {W(2.4)}/><path d="M86 66 Q114 54 120 70 Q104 70 92 76Z" fill="#2B2A44" {W(2.4)}/>'
    f'<ellipse cx="62" cy="76" rx="30" ry="22" fill="#3E3A5A" {s()}/><path d="M48 90 Q62 96 80 88" fill="none" stroke="#fff" stroke-width="3"/>'
    f'<circle cx="38" cy="52" r="14" fill="#3E3A5A" {s()}/><path d="M32 40 Q38 34 44 40 Q38 44 32 40Z" fill="{R}" {W(2)}/>'
    f'<path d="M26 54 L16 58 L26 60Z" fill="#3B3355"/>' + f'<circle cx="34" cy="52" r="5" fill="#fff"/>' + eye(34, 52, 0.6)
    + f'<path d="M54 96 v10 M70 96 v10" {W(2.6)}/>' + sp((24, 20, 5), (64, 26, 4)))
I["romanov-chambers"] = ("night", "серый волк",
    f'<path d="M0 110 Q64 98 128 110 V128 H0Z" fill="#5A6AA8" {W(2.6)}/>'
    f'<path d="M64 112 Q30 110 34 78 Q38 60 64 60 Q90 60 94 78 Q98 110 64 112Z" fill="#9A9CB0" {s()}/>'
    f'<path d="M40 46 L36 14 L56 34Z M88 46 L92 14 L72 34Z" fill="#9A9CB0" {s()}/>'
    f'<path d="M64 26 Q96 28 92 60 Q84 84 64 86 Q44 84 36 60 Q32 28 64 26Z" fill="#B0B2C4" {s()}/>'
    f'<path d="M52 66 Q64 92 76 66 Q64 70 52 66Z" fill="#E4E4EE" {W(2.2)}/><ellipse cx="64" cy="66" rx="6" ry="4" fill="#3B3355"/>'
    + f(64, 52, d=10, k=0.75, mouth=False) + f'<circle cx="104" cy="24" r="10" fill="{Y}" {W(2.4)}/>' + sp((20, 30, 5)))
I["po-susekam"] = ("yellow", "репка",
    GROUND + f'<path d="M64 46 Q34 18 30 34 Q40 44 58 50Z M64 46 Q64 10 76 16 Q76 34 68 48Z M66 48 Q96 22 100 38 Q90 48 70 52Z" fill="{G}" {s()}/>'
    f'<path d="M64 48 Q104 48 102 82 Q98 108 64 112 Q30 108 26 82 Q24 48 64 48Z" fill="{Y}" {s()}/>'
    f'<path d="M30 62 Q64 54 98 62 Q90 50 64 48 Q38 50 30 62Z" fill="#C89AE0" {W(2.4)}/>'
    f'<path d="M64 112 Q66 120 62 124" fill="none" {W(2.4)}/>' + f(64, 82, d=11, k=0.85))
I["podolsk-kraeved"] = ("orange", "аммонит",
    SAND + f'<circle cx="64" cy="64" r="38" fill="#D8B48A" {s()}/>'
    + "".join(f'<path d="M64 64 L{64+38*_m.cos(a):.0f} {64+38*_m.sin(a):.0f}" stroke="#B88A5A" stroke-width="2"/>' for a in [i * 0.52 for i in range(12)])
    + f'<path d="M64 64 m0 -28 a28 28 0 1 1 -1 0 M64 64 m0 -18 a18 18 0 1 1 -1 0" fill="none" stroke="#9A6A44" stroke-width="2.6"/>'
    + f'<circle cx="64" cy="64" r="10" fill="#E8C8A0" {W(2.4)}/>' + f(64, 64, d=4, k=0.45) + sp((108, 26, 6)))
I["kino-museum-karetny"] = ("purple", "зоотроп",
    f'<path d="M64 108 V92" {W(4)}/><path d="M40 112 H88" {W(5)}/>'
    f'<path d="M22 44 V82 Q64 98 106 82 V44" fill="{R}" {s()}/><ellipse cx="64" cy="44" rx="42" ry="12" fill="#C84A3A" {s()}/>'
    + "".join(f'<rect x="{x}" y="56" width="6" height="16" rx="2" fill="#2B2A44"/>' for x in (32, 50, 68, 86))
    + "".join(f'<circle cx="{x}" cy="78" r="4" fill="{Y}" {W(1.6)}/>' for x in (40, 58, 76, 94))
    + f(64, 30, d=0, k=0, mouth=False, blush=False) + f'<path d="M34 30 q30 -16 60 0" fill="none" stroke="#fff" stroke-width="2.4" opacity=".6"/>'
    + sp((20, 20, 6), (110, 104, 5)))
I["orient-museum"] = ("pink", "дарума",
    f'<path d="M64 20 Q104 22 104 72 Q104 108 64 110 Q24 108 24 72 Q24 22 64 20Z" fill="{R}" {s()}/>'
    f'<path d="M40 48 Q64 34 88 48 Q92 74 64 80 Q36 74 40 48Z" fill="#FFF0E4" {s()}/>'
    f'<circle cx="54" cy="58" r="8" fill="#fff" {W(2.4)}/><circle cx="74" cy="58" r="8" fill="#fff" {W(2.4)}/><circle cx="54" cy="58" r="4" fill="#3B3355"/>'
    f'<path d="M44 50 Q54 42 60 48 M68 48 Q74 42 84 50" fill="none" {W(3)}/><path d="M58 70 Q64 74 70 70" fill="none" {W(2.4)}/>'
    f'<path d="M50 92 Q64 84 78 92 Q74 100 64 100 Q54 100 50 92Z" fill="{Y}" {W(2.2)}/>' + sp((112, 30, 6), (16, 40, 5)))
I["muar"] = ("orange", "термитник",
    SAND + f'<path d="M24 104 Q30 70 40 60 Q44 30 56 22 Q64 16 70 28 Q76 40 82 46 Q100 56 104 104Z" fill="#C8784A" {s()}/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="4" ry="5" fill="#6A3A24"/>' for x, y in [(58, 42), (72, 58), (48, 72), (84, 80), (62, 92)])
    + f(64, 70, d=9, k=0.7) + "".join(f'<ellipse cx="{x}" cy="112" rx="4" ry="2.6" fill="#fff" {W(1.4)}/>' for x in (16, 112))
    + f'<circle cx="106" cy="22" r="10" fill="{Y}" {W(2.4)}/>')
I["pushkin-arbat"] = ("blue", "бочка в море",
    f'<path d="M0 84 Q16 76 32 84 T64 84 T96 84 T128 84 V128 H0Z" fill="#5CB7F2" {W(2.6)}/>'
    f'<g transform="rotate(-12 64 70)"><path d="M34 46 Q30 70 34 94 H94 Q98 70 94 46Z" fill="#C8955A" {s()}/>'
    f'<path d="M32 56 H96 M32 84 H96" stroke="#7A5A46" stroke-width="5"/>' + f(64, 70, d=10, k=0.75) + '</g>'
    + f'<path d="M0 100 Q16 92 32 100 T64 100 T96 100 T128 100 V128 H0Z" fill="#7FD3F7" {W(2.4)}/>'
    + f'<path d="M100 22 l3 8 8 0 -6 5 2 8 -7 -5 -7 5 2 -8 -6 -5 8 0Z" fill="{Y}" {W(1.8)}/>' + sp((20, 26, 6)))
I["barbierium"] = ("pink", "бумажная кукла",
    f'<path d="M28 30 H78 V112 H28Z" fill="#fff" {s()}/><path d="M36 38 H70 V104 H36Z" fill="none" stroke="#D0C8E0" stroke-width="2" stroke-dasharray="4 3"/>'
    + kid(53, 52, 10) + f'<path d="M42 64 L38 96 H68 L64 64Z" fill="{P}" {W(2.4)}/><path d="M46 96 v8 M60 96 v8" {W(2.6)}/>'
    + f'<path d="M84 50 L118 50 L112 90 H90Z" fill="{V}" {s()}/><path d="M90 50 l-4 -6 M112 50 l4 -6" {W(2.6)}/>'
    + f'<path d="M96 66 h12 M98 76 h10" stroke="#fff" stroke-width="2.4"/>' + sp((20, 20, 6), (110, 108, 5)))
I["tsagi-scientists-house"] = ("sky", "автожир",
    f'<path d="M20 30 L108 22" stroke="{GR}" stroke-width="6" stroke-linecap="round"/><circle cx="64" cy="26" r="5" fill="{Y}" {W(2.2)}/>'
    f'<path d="M64 30 V48" {W(4)}/><path d="M28 70 Q28 50 54 48 H80 Q100 50 104 66 Q104 82 80 84 H40 Q28 82 28 70Z" fill="{OR}" {s()}/>'
    f'<path d="M58 54 H82 Q92 56 94 66 H58Z" fill="#9FD8F8" {W(2.4)}/><ellipse cx="22" cy="68" rx="4" ry="16" fill="{GR}" {W(2.4)}/>'
    f'<path d="M104 70 L120 60 V80Z" fill="{R}" {W(2.4)}/><path d="M50 84 L44 100 M78 84 L84 100" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="102" r="6" fill="#2B2A44" {W(2.2)}/>' for x in (42, 86)) + f(48, 68, d=7, k=0.55)
    + f'<path d="M6 100 Q30 92 40 104" fill="#fff" opacity=".8"/>')

# ---- перерисовка после просмотра (похожи на уже занятые сюжеты) ----
I["chocolate-sokolniki"] = ("teal", "какао-дерево с плодами",
    GROUND + f'<path d="M58 104 Q60 70 56 50 H72 Q68 70 70 104Z" fill="{DB}" {s()}/>'
    f'<path d="M64 54 Q20 60 22 34 Q30 14 64 20 Q98 14 106 34 Q108 60 64 54Z" fill="{DG}" {s()}/>'
    + "".join(f'<path d="M{x} {y} Q{x-9} {y+14} {x} {y+26} Q{x+9} {y+14} {x} {y}Z" fill="{c}" {W(2.4)}/><path d="M{x} {y+3} V{y+23}" stroke="#fff" stroke-width="1.6" opacity=".6"/>'
              for x, y, c in [(50, 64, OR), (80, 66, "#C8543A"), (64, 76, Y)])
    + f(64, 34, d=10, k=0.75) + sp((110, 70, 5), (16, 70, 4)))
I["tepigra"] = ("purple", "кальмар",
    "".join(f'<path d="M{x} 78 Q{x+dx} 100 {x+dx*2} 118" fill="none" stroke="{P}" stroke-width="6" stroke-linecap="round"/>' for x, dx in [(46, -8), (56, -3), (64, 0), (72, 3), (82, 8)])
    + f'<path d="M64 10 L94 40 Q98 70 84 82 H44 Q30 70 34 40Z" fill="#FFA8C8" {s()}/>'
    f'<path d="M64 10 L94 40 L78 34 Q64 30 50 34 L34 40Z" fill="{P}" {W(2.6)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="{P}"/>' for x, y in [(50, 50), (78, 50), (64, 44)])
    + f(64, 64, d=9, k=0.8) + f'<circle cx="104" cy="96" r="4" fill="#fff" {W(1.6)}/><circle cx="112" cy="84" r="3" fill="#fff" {W(1.4)}/>')
I["mori-kuntsevo"] = ("blue", "морской ёж",
    f'<path d="M0 100 Q64 90 128 100 V128 H0Z" fill="#E8C87A" {W(2.6)}/>'
    + "".join(f'<path d="M64 74 L{64+44*_m.cos(a):.0f} {74+40*_m.sin(a):.0f}" stroke="#6A3A8A" stroke-width="4" stroke-linecap="round"/>' for a in [_m.pi + i * _m.pi / 10 for i in range(11)])
    + f'<path d="M30 94 Q30 52 64 52 Q98 52 98 94Z" fill="#8A4AA8" {s()}/>' + f(64, 78, d=10, k=0.8)
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#fff" {W(1.6)}/>' for x, y in [(20, 30), (30, 18), (104, 26)]))
I["ermitazh-theatre"] = ("night", "скунс",
    GROUND + f'<path d="M84 92 Q122 84 112 42 Q100 26 88 40 Q100 58 80 78Z" fill="#2B2A44" {s()}/>'
    f'<path d="M108 44 Q112 64 92 82" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round"/>'
    f'<ellipse cx="60" cy="84" rx="28" ry="18" fill="#2B2A44" {s()}/><path d="M40 72 Q60 66 82 76" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/>'
    f'<circle cx="36" cy="68" r="17" fill="#2B2A44" {s()}/><path d="M36 52 V66" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M24 56 l-2 -10 l8 5 M46 54 l4 -9 l1 10" fill="#2B2A44" {W(2.4)}/>'
    f'<circle cx="29" cy="68" r="5" fill="#fff"/><circle cx="43" cy="68" r="5" fill="#fff"/>' + eye(29, 68, 0.6) + eye(43, 68, 0.6)
    + f'<ellipse cx="36" cy="78" rx="3" ry="2" fill="{P}"/>' + sp((20, 24, 5), (64, 30, 4)))
I["kz-izmailovo"] = ("sky", "Царевна-Несмеяна",
    f'<path d="M30 128 L42 80 H86 L98 128Z" fill="{V}" {s()}/><path d="M50 80 L64 100 L78 80" fill="none" stroke="{Y}" stroke-width="3"/>'
    f'<path d="M38 60 Q36 96 46 100 L50 64Z M90 60 Q92 96 82 100 L78 64Z" fill="#E8B04A" {W(2.4)}/>'
    f'<circle cx="64" cy="58" r="22" fill="{SK}" {s()}/><path d="M42 52 Q44 34 64 34 Q84 34 86 52 Q74 44 64 46 Q54 44 42 52Z" fill="#E8B04A" {W(2.4)}/>'
    f'<path d="M46 36 L48 20 L56 30 L64 16 L72 30 L80 20 L82 36Z" fill="{Y}" {W(2.4)}/>'
    f'<path d="M50 56 Q55 52 60 56 M68 56 Q73 52 78 56" fill="none" {W(2.6)}/><path d="M57 72 Q64 66 71 72" fill="none" {W(2.4)}/>'
    f'<path d="M52 60 Q49 68 52 72 Q55 68 52 60Z M76 60 Q73 68 76 72 Q79 68 76 60Z" fill="#5CB7F2"/>' + sp((18, 30, 5), (110, 30, 6)))
I["podolie"] = ("green", "водопад",
    f'<path d="M0 30 Q30 20 50 34 L52 128 H0Z" fill="#9A9CB0" {s()}/><path d="M128 26 Q100 18 80 32 L78 128 H128Z" fill="#9A9CB0" {s()}/>'
    f'<path d="M48 34 Q64 28 82 32 L84 100 H46Z" fill="#7FD3F7" {s()}/>'
    + "".join(f'<path d="M{x} 40 V{y}" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>' for x, y in [(54, 80), (64, 92), (74, 76)])
    + f'<path d="M20 104 Q40 94 64 102 Q90 94 110 104 V128 H20Z" fill="#5CB7F2" {W(2.6)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" {W(1.6)}/>' for x, y, r in [(42, 100, 5), (86, 100, 6), (64, 108, 4)])
    + f(64, 62, d=8, k=0.65) + f'<path d="M6 30 Q14 16 26 22 M104 22 Q114 12 122 20" fill="none" stroke="{DG}" stroke-width="5" stroke-linecap="round"/>')

if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        bg, subj, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(bg, body))
    print("svg:", len(ids))
