"""Иконки робота fun (2026-11-06, вечер): 55 новых сюжетов — ПандаПарк, картинг, игровые центры, музеи и парки
городов Подмосковья. Сверено с icons-catalog/sheet-*.png и icons-src/subjects.txt.
Запуск: python3 tools/icons_fun_1106d.py [id ...]"""
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


# ---------- ПандаПарк: панда висит на канате ----------
def panda(extra_front="", extra_back=""):
    return (f'<path d="M0 30 Q64 44 128 30" fill="none" stroke="#C9A06A" stroke-width="6"/><path d="M0 30 Q64 44 128 30" fill="none" {W(1.6)}/>'
            + extra_back
            + f'<path d="M44 74 Q36 50 40 38 M84 74 Q92 50 88 38" fill="none" stroke="{NV}" stroke-width="13" stroke-linecap="round"/>'
            f'<ellipse cx="64" cy="100" rx="26" ry="22" fill="#fff" {s()}/>'
            f'<ellipse cx="50" cy="118" rx="9" ry="8" fill="{NV}" {W(2)}/><ellipse cx="78" cy="118" rx="9" ry="8" fill="{NV}" {W(2)}/>'
            f'<circle cx="40" cy="44" r="7" fill="{NV}"/><circle cx="88" cy="44" r="7" fill="{NV}"/>'
            f'<circle cx="44" cy="54" r="9" fill="{NV}" {W(2)}/><circle cx="84" cy="54" r="9" fill="{NV}" {W(2)}/>'
            f'<circle cx="64" cy="72" r="24" fill="#fff" {s()}/>'
            f'<ellipse cx="54" cy="72" rx="7" ry="8" fill="{NV}" transform="rotate(-20 54 72)"/><ellipse cx="74" cy="72" rx="7" ry="8" fill="{NV}" transform="rotate(20 74 72)"/>'
            f'<circle cx="55" cy="71" r="2.4" fill="#fff"/><circle cx="73" cy="71" r="2.4" fill="#fff"/>'
            f'<ellipse cx="64" cy="81" rx="3.5" ry="2.5" fill="{NV}"/><path d="M60 85 Q64 89 68 85" fill="none" {W(2.2)}/>'
            f'<ellipse cx="46" cy="84" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/><ellipse cx="82" cy="84" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/>'
            + extra_front)


# ---------- Карт-персонаж (вид сбоку) ----------
def kart(col=R, extra="", driver=True):
    o = ""
    if driver:
        o += f'<circle cx="58" cy="54" r="14" fill="#fff" {s()}/><path d="M44 54 Q44 40 58 40 Q72 40 72 54Z" fill="{Y}" {W(2.6)}/><rect x="56" y="48" width="18" height="8" rx="4" fill="#9AD6FF" {W(2)}/>'
    o += (f'<path d="M16 88 Q16 70 34 68 L60 66 Q68 60 80 62 L104 68 Q116 72 116 86 L114 92 H18Z" fill="{col}" {s()}/>'
          f'<path d="M84 62 L92 50" {W(4)}/><circle cx="92" cy="48" r="5" fill="{NV}" {W(2)}/>'
          f'<circle cx="34" cy="94" r="14" fill="{NV}" {s()}/><circle cx="34" cy="94" r="5" fill="{GR}"/>'
          f'<circle cx="98" cy="94" r="14" fill="{NV}" {s()}/><circle cx="98" cy="94" r="5" fill="{GR}"/>'
          + f(98, 78, d=6, k=0.6)
          + "".join(f'<path d="M{x} {y} h-12" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' for x, y in [(12, 70), (8, 80)])
          + extra)
    return o


# ---------- Батут + прыгун ----------
def tramp(jumper, col=B):
    return (f'<path d="M26 112 L22 124 M102 112 L106 124 M64 116 V126" {W(4)}/>'
            f'<ellipse cx="64" cy="108" rx="46" ry="10" fill="{col}" {s()}/><ellipse cx="64" cy="106" rx="36" ry="6" fill="{NV}" opacity=".85"/>'
            + "".join(f'<path d="M{x} 100 q4 -6 8 0" fill="none" stroke="#fff" stroke-width="2.6"/>' for x in (30, 90))
            + jumper)


def frame_pic(x, y, w, h, inner):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{GO}" {s()}/>'
            f'<rect x="{x+8}" y="{y+8}" width="{w-16}" height="{h-16}" fill="#BFE8FF" {W(2.4)}/>' + inner)


I = {}
# ===================== ПандаПарк =====================
I["panda-aviapark"] = ("sky", "панда на канате в лётных очках-авиаторах", panda(
    f'<path d="M40 62 H88" stroke="{BR}" stroke-width="4"/>'
    f'<circle cx="53" cy="64" r="9" fill="#9AD6FF" stroke="{BR}" stroke-width="4"/><circle cx="75" cy="64" r="9" fill="#9AD6FF" stroke="{BR}" stroke-width="4"/>'
    f'<circle cx="51" cy="61" r="2.5" fill="#fff"/><circle cx="73" cy="61" r="2.5" fill="#fff"/>') + sp((16, 70, 6), (112, 70, 5)))
I["panda-zelenopark"] = ("green", "панда на канате жуёт веточку бамбука", panda(
    f'<path d="M66 86 L104 70" stroke="{DG}" stroke-width="5" stroke-linecap="round"/><path d="M80 80 l2 -4 M92 75 l2 -4" {W(2)}/>'
    f'<path d="M100 72 Q112 58 118 64 Q110 74 100 72Z" fill="{G}" {W(2.2)}/><path d="M90 76 Q96 88 104 86 Q100 78 90 76Z" fill="{G}" {W(2.2)}/>')
    + sp((16, 70, 6)))
I["panda-luzhniki"] = ("blue", "панда на канате с золотой медалью на шее", panda(
    f'<path d="M50 94 L64 106 L78 94" fill="none" stroke="{R}" stroke-width="5"/>'
    f'<circle cx="64" cy="110" r="10" fill="{GO}" {W(2.4)}/><path d="M60 110 l3 3 l6 -7" fill="none" stroke="#fff" stroke-width="2.4"/>')
    + sp((16, 70, 6), (112, 72, 5)))
I["panda-sokolniki"] = ("orange", "панда на канате с бельчонком на макушке", panda(
    f'<path d="M78 50 Q96 30 88 14 Q104 22 98 44 Q94 54 80 54Z" fill="{BR}" {W(2.4)}/>'
    f'<ellipse cx="68" cy="50" rx="11" ry="8" fill="{OR}" {W(2.4)}/><circle cx="60" cy="42" r="7" fill="{OR}" {W(2.4)}/>'
    f'<path d="M56 36 l-2 -6 l5 3Z" fill="{OR}" {W(1.8)}/>' + eye(58, 42, 0.5)) + sp((16, 70, 6)))

# ===================== Картинг =====================
I["karting-serebryanyi-dozhd"] = ("sky", "карт-персонаж под серебристой тучкой с дождиком", kart(B,
    f'<path d="M34 26 Q32 12 46 14 Q52 4 64 10 Q78 6 80 18 Q92 18 90 28 Z" fill="#E6E9F2" {W(2.6)}/>'
    + "".join(f'<path d="M{x} 34 l-3 8" stroke="#A8B0C8" stroke-width="3" stroke-linecap="round"/>' for x in (44, 56, 68, 80)))
    + sp((110, 24, 6)))
I["karting-e-go"] = ("teal", "электрокарт-персонаж с хвостом-вилкой от розетки", kart(G,
    f'<path d="M18 84 Q4 90 8 108 Q12 118 22 116" fill="none" {W(3)}/>'
    f'<rect x="18" y="110" width="12" height="10" rx="2" fill="{GR}" {W(2)}/><path d="M22 120 v5 M27 120 v5" {W(2)}/>'
    f'<path d="M66 72 l-6 10 h6 l-4 10 l10 -13 h-6 l4 -7Z" fill="{Y}" {W(1.8)}/>') + sp((110, 26, 6), (20, 28, 5)))
I["karting-vegas"] = ("yellow", "карт-персонаж в ковбойской шляпе", kart(OR,
    f'<path d="M84 64 Q98 58 112 64" fill="none" {W(2)}/><path d="M82 62 Q98 70 116 60 Q112 66 98 66 Q88 66 82 62Z" fill="{BR}" {W(2.4)}/>'
    f'<path d="M88 62 Q88 46 98 48 Q108 46 108 62Z" fill="{BR}" {W(2.4)}/><path d="M89 58 H107" stroke="{R}" stroke-width="3"/>', driver=True)
    + sp((20, 28, 6), (110, 26, 5)))
I["karting-kartracing"] = ("green", "карт-персонаж везёт золотой кубок", kart(V,
    f'<path d="M28 66 L26 46 H46 L44 66Z" fill="{GO}" {W(2.4)}/><path d="M26 50 Q16 50 18 58 Q20 62 28 60 M46 50 Q56 50 54 58 Q52 62 44 60" fill="none" {W(2.4)}/>'
    f'<rect x="30" y="64" width="12" height="5" fill="{GO}" {W(2)}/>', driver=False)
    + f'<circle cx="62" cy="50" r="14" fill="#fff" {s()}/><path d="M48 50 Q48 36 62 36 Q76 36 76 50Z" fill="{R}" {W(2.6)}/><rect x="60" y="44" width="18" height="8" rx="4" fill="#9AD6FF" {W(2)}/>'
    + sp((110, 26, 6), (20, 24, 5)))
I["karting-lemans-dezhneva"] = ("purple", "карт-персонаж с будильником на капоте (24 часа Ле-Мана)", kart(R,
    f'<circle cx="104" cy="34" r="16" fill="#fff" {s()}/><path d="M104 34 V24 M104 34 L111 38" {W(2.6)}/>'
    f'<circle cx="92" cy="20" r="5" fill="{Y}" {W(2)}/><circle cx="116" cy="20" r="5" fill="{Y}" {W(2)}/>'
    f'<path d="M96 50 l-3 4 M112 50 l3 4" {W(2.6)}/>') + sp((20, 26, 6)))
I["crazy-cart-zelenopark"] = ("pink", "малыш на дрифт-карте крутит «пончик» в облаке дыма",
    "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".85" {W(2)}/>' for x, y, r in [(18, 96, 12), (30, 110, 10), (14, 76, 8), (110, 104, 10)])
    + f'<path d="M24 60 Q40 30 76 34" fill="none" stroke="#fff" stroke-width="4" stroke-dasharray="6 6" stroke-linecap="round"/>'
    f'<g transform="rotate(-14 64 86)"><rect x="30" y="80" width="68" height="18" rx="8" fill="{TE}" {s()}/>'
    f'<circle cx="38" cy="102" r="10" fill="{NV}" {s()}/><circle cx="92" cy="102" r="10" fill="{NV}" {s()}/>'
    f'<path d="M84 80 L96 64" {W(4)}/><circle cx="96" cy="62" r="5" fill="{NV}"/></g>'
    + kid(62, 60, r=16) + f'<path d="M46 58 Q46 40 62 40 Q78 40 78 58Z" fill="{OR}" {W(2.6)}/>'
    + f'<path d="M42 80 L30 72 M80 76 L94 66" {W(4)}/>' + sp((108, 28, 6)))

# ===================== Игровые центры Москвы =====================
I["pogruzhenie-cdm"] = ("night", "дверца с замочной скважиной и золотой ключ",
    f'<path d="M30 118 V44 Q30 16 64 16 Q98 16 98 44 V118Z" fill="{BR}" {s()}/>'
    + "".join(f'<path d="M{x} 30 V114" stroke="#9A5A26" stroke-width="2.4"/>' for x in (48, 64, 80))
    + f(64, 50, d=12, k=0.85)
    + f'<circle cx="64" cy="80" r="8" fill="{NV}"/><path d="M60 82 L58 98 H70 L68 82Z" fill="{NV}"/>'
    + f'<g transform="rotate(-30 100 96)"><circle cx="100" cy="96" r="9" fill="{GO}" {W(2.4)}/><circle cx="100" cy="96" r="3" fill="{BR}"/>'
    f'<rect x="108" y="93" width="22" height="6" fill="{GO}" {W(2)}/><rect x="122" y="99" width="5" height="6" fill="{GO}" {W(1.8)}/></g>'
    + "".join(sparkle(x, y, r, Y) for x, y, r in [(16, 30, 6), (112, 20, 5)]))
I["hello-park-riviera"] = ("pink", "шарик из сухого бассейна машет ладошкой «привет»",
    "".join(f'<circle cx="{x}" cy="{y}" r="11" fill="{c}" {W(2.2)}/>' for x, y, c in
            [(10, 110, Y), (30, 116, B), (52, 120, G), (76, 120, R), (98, 116, V), (118, 110, OR), (20, 96, G), (110, 94, B)])
    + f'<circle cx="64" cy="70" r="34" fill="{R}" {s()}/><ellipse cx="52" cy="54" rx="9" ry="6" fill="#fff" opacity=".45"/>'
    + f(64, 72, d=11, k=0.9)
    + f'<path d="M96 60 Q108 44 104 30" fill="none" {W(4)}/><circle cx="104" cy="26" r="9" fill="{R}" {W(2.4)}/>'
    + "".join(f'<path d="M{x} {y} q4 -3 2 -8" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>' for x, y in [(116, 24), (114, 36)])
    + sp((20, 30, 6)))
I["kidburg-zelenopark"] = ("teal", "докторский чемоданчик с крестиком и стетоскопом",
    f'<path d="M48 36 V26 Q48 20 54 20 H74 Q80 20 80 26 V36" fill="none" {W(5)}/>'
    f'<rect x="20" y="36" width="88" height="70" rx="12" fill="#fff" {s()}/>'
    f'<path d="M58 48 h12 v10 h10 v12 h-10 v10 h-12 v-10 h-10 v-12 h10Z" fill="{R}" {W(2.2)}/>'
    + f(64, 92, d=12, k=0.7)
    + f'<path d="M22 60 Q6 80 18 100 Q30 112 40 104" fill="none" stroke="{NV}" stroke-width="4"/><circle cx="42" cy="104" r="6" fill="{GR}" {W(2.2)}/>'
    + sp((110, 24, 6), (16, 26, 5)))
I["happylon-vegas"] = ("purple", "автомат с хваталкой достаёт плюшевого зайчика",
    f'<rect x="24" y="14" width="80" height="104" rx="10" fill="{P}" {s()}/><rect x="32" y="26" width="64" height="56" rx="4" fill="#E4F6FF" {W(2.6)}/>'
    f'<path d="M64 26 V44" {W(2.4)}/><path d="M56 44 H72 M58 44 L54 56 M70 44 L74 56" {W(2.6)}/>'
    f'<ellipse cx="64" cy="66" rx="10" ry="9" fill="#fff" {W(2.4)}/><ellipse cx="58" cy="54" rx="3" ry="8" fill="#fff" {W(2)}/><ellipse cx="70" cy="54" rx="3" ry="8" fill="#fff" {W(2)}/>'
    + eye(60, 65, 0.5) + eye(68, 65, 0.5)
    + "".join(f'<circle cx="{x}" cy="78" r="5" fill="{c}" {W(1.6)}/>' for x, c in [(40, Y), (50, G), (80, B), (88, Y)])
    + f(64, 98, d=12, k=0.75) + f'<circle cx="92" cy="96" r="5" fill="{R}" {W(2)}/><path d="M92 96 V86" {W(3)}/>'
    + sp((14, 30, 6), (114, 26, 5)))

# ===================== Химки =====================
I["khimki-gorshin-gallery"] = ("orange", "картина в раме-персонаж разглядывает себя в лупу",
    frame_pic(16, 22, 76, 84, f'<path d="M24 90 L44 62 L58 78 L68 66 L84 90Z" fill="{G}" {W(2)}/><circle cx="72" cy="42" r="7" fill="{Y}" {W(2)}/>')
    + f(54, 52, d=10, k=0.7)
    + f'<path d="M94 98 L114 118" stroke="{BR}" stroke-width="8" stroke-linecap="round"/><circle cx="88" cy="90" r="14" fill="#E4F6FF" opacity=".85" {s()}/>'
    + sp((112, 28, 6)))
I["khimki-style-studio"] = ("night", "ёлочный шар-персонаж и кисточка рисует на нём звёздочку",
    f'<path d="M58 10 Q64 4 70 10" fill="none" {W(2.4)}/><rect x="56" y="12" width="16" height="10" rx="2" fill="{GO}" {W(2.4)}/>'
    f'<circle cx="64" cy="66" r="42" fill="{R}" {s()}/><ellipse cx="48" cy="46" rx="10" ry="6" fill="#fff" opacity=".5"/>'
    f'<path d="M24 76 Q64 90 104 76" fill="none" stroke="{Y}" stroke-width="4"/>'
    + f(64, 62, d=12, k=0.85)
    + f'<path d="M88 86 l3 6 l6 1 l-5 4 l1 6 l-5 -3 l-6 3 l1 -6 l-4 -4 l6 -1Z" fill="{Y}" {W(1.4)}/>'
    f'<g transform="rotate(35 104 104)"><rect x="100" y="82" width="8" height="40" rx="3" fill="{BR}" {W(2)}/><path d="M100 82 Q104 70 108 82Z" fill="{Y}" {W(2)}/></g>'
    + "".join(sparkle(x, y, r, Y) for x, y, r in [(18, 24, 6), (110, 20, 5)]))

# ===================== Королёв =====================
I["korolev-rkk-energia"] = ("sky", "спускаемый аппарат «Союз» на полосатом парашюте",
    f'<path d="M14 46 Q64 -10 114 46 Q102 40 90 46 Q78 38 64 46 Q50 38 38 46 Q26 40 14 46Z" fill="{OR}" {s()}/>'
    f'<path d="M38 46 Q50 10 64 4 M90 46 Q78 10 64 4" fill="none" stroke="#fff" stroke-width="3"/>'
    f'<path d="M14 46 L50 82 M114 46 L78 82 M64 46 V78" {W(2)}/>'
    f'<path d="M44 118 Q40 86 64 76 Q88 86 84 118Z" fill="#8C9099" {s()}/><path d="M42 112 H86" stroke="{NV}" stroke-width="4"/>'
    + f(64, 98, d=8, k=0.7).replace(f'fill="{O}"', 'fill="#1E1D33"')
    + sp((18, 80, 5), (110, 80, 6)))
I["korolev-noveishaya-istoriya"] = ("night", "метеорит-персонаж с огненным хвостом",
    f'<path d="M108 14 Q80 40 70 60 L48 46 Q76 30 108 14Z" fill="{OR}" {W(2.4)}/><path d="M118 34 Q92 52 78 68 L64 56 Q90 42 118 34Z" fill="{Y}" {W(2.4)}/>'
    f'<path d="M30 52 Q48 36 72 48 Q90 58 86 82 Q82 106 56 108 Q30 108 24 86 Q20 66 30 52Z" fill="#8E7A6A" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#6E5C4E" {W(1.8)}/>' for x, y, r in [(40, 60, 5), (72, 94, 6), (34, 92, 4)])
    + f(56, 78, d=10, k=0.8) + "".join(sparkle(x, y, r, "#FFE9A8") for x, y, r in [(18, 24, 5), (100, 110, 6), (30, 116, 3)]))
I["korolev-fun-fantastic"] = ("purple", "космонавт прыгает на батуте", tramp(
    f'<g transform="rotate(-10 64 52)"><rect x="46" y="54" width="36" height="34" rx="12" fill="#fff" {s()}/>'
    f'<path d="M48 64 L30 50 M80 64 L98 50" stroke="#fff" stroke-width="10" stroke-linecap="round"/><path d="M48 64 L30 50 M80 64 L98 50" fill="none" {W(1.8)}/>'
    f'<circle cx="64" cy="38" r="20" fill="#fff" {s()}/><circle cx="64" cy="40" r="14" fill="#9AD6FF" {W(2.4)}/>'
    + f(64, 41, d=6, k=0.55) + f'<rect x="58" y="66" width="12" height="8" rx="2" fill="{R}" {W(1.6)}/></g>'
    f'<path d="M54 88 L50 96 M74 88 L80 94" stroke="#fff" stroke-width="10" stroke-linecap="round"/>', col=V)
    + "".join(sparkle(x, y, r, Y) for x, y, r in [(18, 24, 6), (110, 22, 5), (100, 70, 3)]))

# ===================== Ступино =====================
I["stupino-museum"] = ("orange", "каменный топорик археолога-персонаж с кисточкой",
    f'<path d="M58 30 L70 30 L74 120 L54 120Z" fill="{BR}" {s()}/>'
    f'<path d="M20 40 Q30 18 66 22 Q104 18 110 44 Q104 70 66 66 Q28 70 20 40Z" fill="#A8A29A" {s()}/>'
    f'<path d="M54 26 L78 26 L80 64 L52 64Z" fill="none" stroke="#C9A06A" stroke-width="5"/>'
    + f(66, 44, d=12, k=0.8)
    + f'<g transform="rotate(-30 26 98)"><rect x="22" y="80" width="8" height="34" rx="3" fill="{Y}" {W(2)}/><path d="M20 80 Q26 66 32 80Z" fill="{BR}" {W(2)}/></g>'
    + sp((112, 96, 6)))
I["stupino-young-actor"] = ("purple", "малыш-актёр в короне раздвигает занавес",
    f'<rect x="0" y="0" width="128" height="16" fill="{R}" {W(2)}/>'
    f'<path d="M0 14 Q26 40 18 128 H0Z M128 14 Q102 40 110 128 H128Z" fill="{R}" {s()}/>'
    f'<path d="M30 110 H98 V124 H30Z" fill="{BR}" {W(2.4)}/>'
    + kid(64, 66, r=22) + f'<path d="M46 48 L50 30 L58 42 L64 26 L70 42 L78 30 L82 48Z" fill="{GO}" {W(2.4)}/>'
    + f'<path d="M50 90 Q64 96 78 90 L82 110 H46Z" fill="{Y}" {W(2.4)}/><path d="M24 64 L44 80 M104 64 L84 80" {W(4)}/>'
    + sp((64, 12, 0)))
I["stupino-polet-shmelya"] = ("yellow", "шмель прыгает на батуте", tramp(
    f'<ellipse cx="40" cy="44" rx="16" ry="11" fill="#fff" opacity=".85" {W(2.2)} transform="rotate(-30 40 44)"/>'
    f'<ellipse cx="88" cy="44" rx="16" ry="11" fill="#fff" opacity=".85" {W(2.2)} transform="rotate(30 88 44)"/>'
    f'<ellipse cx="64" cy="66" rx="26" ry="24" fill="{Y}" {s()}/>'
    f'<path d="M42 60 Q64 66 86 60 M40 74 Q64 80 88 74" fill="none" stroke="{NV}" stroke-width="6"/>'
    + f(64, 56, d=9, k=0.7) + f'<path d="M56 44 L50 30 M72 44 L78 30" {W(2.4)}/><circle cx="50" cy="28" r="3.5" fill="{NV}"/><circle cx="78" cy="28" r="3.5" fill="{NV}"/>'
    f'<path d="M52 88 L48 96 M76 88 L80 96" {W(3)}/>', col=OR) + sp((16, 30, 6), (112, 22, 5)))
I["stupino-ostrovsky-park"] = ("green", "скейтборд-персонаж в шлеме прыгает над дорожкой парка",
    f'<path d="M0 112 Q64 100 128 112 V128 H0Z" fill="#C9C4B8" {W(2.4)}/>'
    f'<g transform="rotate(-12 64 70)"><rect x="18" y="62" width="92" height="20" rx="10" fill="{OR}" {s()}/>'
    f'<circle cx="36" cy="90" r="8" fill="{NV}" {W(2.2)}/><circle cx="92" cy="90" r="8" fill="{NV}" {W(2.2)}/>' + f(64, 72, d=10, k=0.6)
    + f'<path d="M44 62 Q44 36 64 36 Q84 36 84 62Z" fill="{B}" {s()}/><path d="M56 40 Q64 34 72 40" fill="none" stroke="#fff" stroke-width="3"/></g>'
    + "".join(f'<path d="M{x} {y} h-12" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' for x, y in [(14, 60), (12, 74)])
    + sp((110, 24, 6)))

# ===================== Жуковский =====================
I["zhukovsky-sky-museum"] = ("sky", "биплан-кукурузник в лётном шлеме с очками",
    f'<path d="M96 66 L118 46 L122 50 L110 72Z" fill="{R}" {s()}/>'
    f'<rect x="30" y="30" width="44" height="12" rx="6" fill="{G}" {s()}/>'
    f'<path d="M16 68 Q16 52 36 52 H96 Q110 56 112 70 Q110 84 96 84 H36 Q16 84 16 68Z" fill="{Y}" {s()}/>'
    f'<path d="M40 42 V54 M64 42 V54" {W(3)}/>'
    f'<rect x="24" y="72" width="56" height="12" rx="6" fill="{G}" {s()}/>'
    f'<path d="M14 68 H8" {W(4)}/><ellipse cx="7" cy="68" rx="4" ry="20" fill="{GR}" opacity=".75" {W(1.6)}/>'
    f'<path d="M44 84 L40 100 M64 84 L68 100" {W(3)}/><circle cx="40" cy="104" r="6" fill="{NV}" {W(2)}/><circle cx="68" cy="104" r="6" fill="{NV}" {W(2)}/>'
    + f(38, 66, d=8, k=0.65)
    + f'<path d="M70 54 Q70 38 84 38 Q98 38 98 54Z" fill="{BR}" {s()}/><circle cx="80" cy="46" r="4.5" fill="#9AD6FF" {W(2)}/><circle cx="90" cy="46" r="4.5" fill="#9AD6FF" {W(2)}/>'
    + "".join(f'<path d="M{x} {y} h14" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' for x, y in [(100, 96), (106, 108)])
    + sp((100, 20, 6), (20, 24, 5)))
I["zhukovsky-tu144"] = ("blue", "сверхзвуковой Ту-144 с опущенным носом-клювом",
    f'<path d="M8 74 Q30 60 70 60 L104 62 Q118 64 122 74 L118 86 L70 84 Q30 86 8 74Z" fill="#fff" {s()}/>'
    f'<path d="M104 62 L124 72 Q122 80 116 82Z" fill="#E6E9F2" {W(2.4)}/>'
    f'<path d="M30 80 L60 106 L84 106 L74 84Z" fill="#E6E9F2" {s()}/><path d="M16 70 L10 44 L26 46 L36 66Z" fill="#E6E9F2" {s()}/>'
    f'<path d="M30 72 H96" stroke="{B}" stroke-width="3" stroke-dasharray="4 5"/>'
    + f(96, 72, d=6, k=0.55)
    + "".join(f'<path d="M{x} {y} h-14" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' for x, y in [(20, 96), (14, 108)])
    + sp((100, 26, 6), (40, 24, 5)))
I["zhukovsky-park"] = ("green", "бетонный мишка-скульптура на постаменте под сосной",
    f'<path d="M100 8 L82 40 H92 L76 66 H124 L108 40 H118Z" fill="{DG}" {s()}/><rect x="96" y="66" width="8" height="40" fill="{BR}" {W(2)}/>'
    + GROUND + f'<rect x="20" y="92" width="64" height="18" rx="3" fill="#C9C4B8" {s()}/>'
    f'<ellipse cx="52" cy="72" rx="22" ry="20" fill="#D6D2CA" {s()}/><circle cx="52" cy="44" r="18" fill="#D6D2CA" {s()}/>'
    f'<circle cx="38" cy="30" r="7" fill="#D6D2CA" {W(2.4)}/><circle cx="66" cy="30" r="7" fill="#D6D2CA" {W(2.4)}/>'
    + f(52, 46, d=7, k=0.65) + f'<ellipse cx="52" cy="52" rx="5" ry="3.5" fill="#9A958C"/>'
    + sp((20, 20, 5)))
I["zhukovsky-strela"] = ("orange", "театральная маска-улыбка, пронзённая стрелой Амура",
    f'<path d="M22 30 Q64 16 106 30 Q110 74 64 104 Q18 74 22 30Z" fill="#fff" {s()}/>'
    f'<path d="M38 50 Q46 42 54 50 M74 50 Q82 42 90 50" fill="none" {W(4)}/>'
    f'<path d="M42 70 Q64 92 86 70" fill="{R}" {W(3)}/>'
    f'<ellipse cx="36" cy="64" rx="6" ry="3.5" fill="#FF7FA8" opacity=".6"/><ellipse cx="92" cy="64" rx="6" ry="3.5" fill="#FF7FA8" opacity=".6"/>'
    f'<path d="M6 104 L122 20" stroke="{BR}" stroke-width="4"/><path d="M122 20 L108 22 L118 32Z" fill="{GR}" {W(2)}/>'
    f'<path d="M6 104 L4 92 M6 104 L18 106 M12 100 L10 88 M12 100 L24 102" stroke="{R}" stroke-width="3"/>'
    + sp((112, 104, 6)))

# ===================== Раменское =====================
I["ramenskoe-park"] = ("sky", "паровозик парковой железной дороги на фоне колеса обозрения",
    f'<circle cx="80" cy="44" r="34" fill="none" stroke="#fff" stroke-width="4"/>'
    + "".join(f'<path d="M80 44 L{80+34*c:.0f} {44+34*s_:.0f}" stroke="#fff" stroke-width="2"/>' for c, s_ in [(1, 0), (-1, 0), (0, 1), (0, -1), (.7, .7), (-.7, .7), (.7, -.7), (-.7, -.7)])
    + f'<path d="M0 116 H128" {W(4)}/>'
    f'<rect x="20" y="58" width="34" height="34" rx="4" fill="{R}" {s()}/><rect x="26" y="64" width="22" height="14" rx="3" fill="#9AD6FF" {W(2)}/>'
    f'<rect x="50" y="72" width="54" height="30" rx="12" fill="{B}" {s()}/><rect x="86" y="54" width="12" height="20" fill="{NV}" {W(2.4)}/>'
    f'<path d="M104 88 L116 104 H100Z" fill="{Y}" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="106" r="9" fill="{NV}" {W(2.4)}/>' for x in (32, 62, 90))
    + f(76, 86, d=8, k=0.65) + f'<circle cx="94" cy="44" r="5" fill="#fff" {W(1.6)}/><circle cx="100" cy="32" r="7" fill="#fff" {W(1.6)}/>')
I["ramenskoe-museum"] = ("blue", "гжельская тарелка-персонаж с синим цветком",
    f'<circle cx="64" cy="64" r="48" fill="#fff" {s()}/><circle cx="64" cy="64" r="38" fill="none" stroke="#2F5BC4" stroke-width="4"/>'
    + "".join(f'<path d="M{64+30*c:.0f} {64+30*s_:.0f} q4 -4 8 0 q-4 4 -8 0Z" fill="#2F5BC4"/>' for c, s_ in [(1, 0), (-1, 0), (0, -1), (.7, -.7), (-.7, -.7), (.7, .7), (-.7, .7), (0, 1)])
    + f'<path d="M48 40 Q56 30 64 40 Q72 30 80 40 Q76 52 64 50 Q52 52 48 40Z" fill="#2F5BC4" {W(1.8)}/>'
    + f(64, 70, d=11, k=0.8).replace(f'fill="{O}"', 'fill="#1E3C8C"') + sp((112, 22, 6), (16, 108, 5)))

# ===================== Воскресенск =====================
I["voskresensk-zvezdochka"] = ("night", "звёздочка-персонаж съезжает с горки",
    f'<path d="M16 120 Q40 120 60 90 Q78 64 100 60 L110 60 V120Z" fill="{TE}" {s()}/><path d="M100 60 V20 H116 V120" fill="none" {W(4)}/>'
    + "".join(f'<path d="M100 {y} H116" {W(3)}/>' for y in (36, 52))
    + f'<g transform="rotate(-20 54 70)"><path d="M54 36 L63 58 L86 60 L68 74 L74 98 L54 84 L34 98 L40 74 L22 60 L45 58Z" fill="{Y}" {s()}/>'
    + f(54, 68, d=7, k=0.6) + '</g>' + "".join(sparkle(x, y, r, Y) for x, y, r in [(18, 24, 5), (110, 108, 0), (34, 40, 3)]))
I["voskresensk-bon-bon"] = ("pink", "конфета-персонаж ныряет в бассейн с шариками",
    "".join(f'<circle cx="{x}" cy="{y}" r="11" fill="{c}" {W(2.2)}/>' for x, y, c in
            [(8, 104, B), (28, 110, Y), (50, 116, G), (74, 116, R), (96, 112, V), (118, 104, Y), (16, 122, R), (62, 124, B), (106, 124, G)])
    + f'<g transform="rotate(-20 64 64)"><path d="M28 64 L10 50 L12 78Z M100 64 L118 50 L116 78Z" fill="{Y}" {s()}/>'
    f'<ellipse cx="64" cy="64" rx="38" ry="26" fill="{R}" {s()}/>'
    + "".join(f'<path d="M{x} 40 Q{x+8} 64 {x} 88" fill="none" stroke="#fff" stroke-width="4" opacity=".7"/>' for x in (44, 64, 84))
    + f(64, 62, d=10, k=0.8) + '</g>' + sp((20, 24, 6), (110, 22, 5)))
I["voskresensk-moskvoretsky"] = ("teal", "кувшинка-персонаж на реке",
    WATER + f'<ellipse cx="64" cy="100" rx="50" ry="12" fill="{DG}" {s()}/><path d="M64 100 L100 94" stroke="#7FD3F7" stroke-width="6"/>'
    + "".join(f'<path d="M64 92 Q{64+dx} {60} {64+dx*1.4:.0f} 40 Q{64+dx*.3:.0f} 60 64 92Z" fill="{P}" {W(2.4)}/>' for dx in (-28, 28))
    + f'<path d="M64 92 Q40 50 64 26 Q88 50 64 92Z" fill="#FFC0D8" {s()}/>'
    + f(64, 66, d=7, k=0.65) + sp((18, 24, 6), (110, 30, 5)))

# ===================== Ногинск =====================
I["noginsk-central-park"] = ("green", "царевна-лягушка в короне со стрелой",
    GROUND + f'<ellipse cx="64" cy="84" rx="38" ry="28" fill="{G}" {s()}/>'
    f'<circle cx="44" cy="52" r="14" fill="{G}" {s()}/><circle cx="84" cy="52" r="14" fill="{G}" {s()}/>'
    + eye(44, 52, 1.1) + eye(84, 52, 1.1)
    + f'<path d="M44 84 Q64 98 84 84" fill="none" {W(3)}/><ellipse cx="34" cy="78" rx="6" ry="3.5" fill="#FF7FA8" opacity=".6"/><ellipse cx="94" cy="78" rx="6" ry="3.5" fill="#FF7FA8" opacity=".6"/>'
    + f'<path d="M50 40 L52 24 L60 34 L64 20 L68 34 L76 24 L78 40Z" fill="{GO}" {W(2.4)}/>'
    + f'<path d="M30 96 L108 70" stroke="{BR}" stroke-width="4"/><path d="M108 70 L96 66 L100 78Z" fill="{GR}" {W(2)}/>'
    f'<path d="M30 96 l-4 -8 M30 96 l-8 4" stroke="{R}" stroke-width="3"/>' + sp((18, 22, 6), (110, 26, 5)))
I["noginsk-lost-world"] = ("orange", "мамонтёнок-персонаж с длинными бивнями",
    f'<ellipse cx="70" cy="80" rx="40" ry="30" fill="{BR}" {s()}/>'
    + "".join(f'<rect x="{x}" y="96" width="14" height="24" rx="5" fill="{BR}" {W(2.6)}/>' for x in (44, 84))
    + f'<circle cx="46" cy="56" r="26" fill="#A96A3A" {s()}/><path d="M30 40 Q40 24 60 32" fill="none" stroke="#7A4A26" stroke-width="5"/>'
    f'<path d="M28 66 Q18 84 26 104 Q30 110 34 104 Q30 90 38 74" fill="#A96A3A" {s()}/>'
    f'<path d="M36 76 Q24 92 40 100 Q46 96 44 92" fill="#FFF6E0" {W(2.4)}/>'
    + f(48, 56, d=8, k=0.7) + f'<path d="M108 74 Q120 80 116 92" fill="none" {W(3)}/>' + sp((108, 30, 6)))
I["noginsk-cosmostar"] = ("night", "ракета-карусель с маленькими ракетками на цепочках",
    f'<path d="M64 14 Q80 28 80 60 H48 Q48 28 64 14Z" fill="#fff" {s()}/><circle cx="64" cy="40" r="7" fill="#9AD6FF" {W(2)}/>'
    f'<path d="M48 54 L38 66 H48Z M80 54 L90 66 H80Z" fill="{R}" {W(2.2)}/><rect x="60" y="60" width="8" height="54" fill="{GR}" {W(2.2)}/>'
    f'<path d="M20 64 L64 58 L108 64" fill="none" {W(2.6)}/>'
    + "".join(f'<path d="M{x} 64 L{x+dx} 88" {W(1.8)}/><g transform="rotate({rot} {x+dx} 94)"><ellipse cx="{x+dx}" cy="94" rx="8" ry="12" fill="{c}" {W(2.2)}/></g>'
              for x, dx, c, rot in [(20, -4, Y, 20), (108, 4, P, -20)])
    + f(64, 80, d=0, k=0.01, mouth=False, blush=False)
    + f'<ellipse cx="64" cy="116" rx="30" ry="6" fill="{V}" {W(2.4)}/>' + f(64, 44, d=0, k=0.01, mouth=False, blush=False)
    + eye(58, 42, 0.6) + eye(70, 42, 0.6)
    + "".join(sparkle(x, y, r, Y) for x, y, r in [(20, 24, 5), (108, 22, 6), (100, 108, 3)]))
I["noginsk-drama-comedy"] = ("purple", "кот в сапогах в шляпе с пером",
    f'<path d="M40 70 Q36 112 46 116 H82 Q92 112 88 70Z" fill="{OR}" {s()}/>'
    f'<path d="M42 104 V122 H58 V108 M70 108 V122 H88 V104" fill="{BR}" {s()}/>'
    f'<circle cx="64" cy="56" r="26" fill="{OR}" {s()}/><path d="M42 44 L40 24 L56 34Z M86 44 L88 24 L72 34Z" fill="{OR}" {W(2.6)}/>'
    + f(64, 58, d=10, k=0.8) + f'<path d="M48 64 H30 M48 68 L32 74 M80 64 H98 M80 68 L96 74" {W(1.6)}/>'
    + f'<path d="M30 36 Q64 22 98 36 Q64 44 30 36Z" fill="{NV}" {W(2.4)}/><path d="M46 34 Q48 14 64 14 Q80 14 82 34Z" fill="{NV}" {W(2.4)}/>'
    f'<path d="M80 22 Q104 4 116 16 Q100 16 84 30Z" fill="{R}" {W(2.2)}/>' + sp((18, 90, 6)))
I["noginsk-morozov-house"] = ("orange", "старинный камин-персонаж с часами на полке",
    f'<rect x="18" y="40" width="92" height="78" rx="4" fill="#E8DCC8" {s()}/><rect x="10" y="32" width="108" height="12" rx="3" fill="{BR}" {s()}/>'
    f'<path d="M38 118 V80 Q38 62 64 62 Q90 62 90 80 V118Z" fill="{NV}" {s()}/>'
    f'<path d="M50 118 Q48 100 58 92 Q58 104 64 98 Q70 88 66 80 Q82 94 78 118Z" fill="{OR}" {W(2)}/><path d="M58 118 Q60 108 64 104 Q70 110 68 118Z" fill="{Y}"/>'
    + "".join(f'<rect x="{x}" y="{y}" width="12" height="12" fill="{B}" opacity=".7" {W(1.4)}/>' for x, y in [(22, 48), (94, 48), (22, 66), (94, 66)])
    + f(64, 50, d=14, k=0.6)
    + f'<rect x="54" y="8" width="20" height="24" rx="4" fill="{GO}" {W(2.4)}/><circle cx="64" cy="18" r="6" fill="#fff" {W(1.6)}/><path d="M64 18 V14 M64 18 h3" {W(1.4)}/>')

# ===================== Электросталь =====================
I["elektrostal-museum"] = ("blue", "шестерёнка-персонаж с кисточкой художника",
    "".join(f'<rect x="58" y="10" width="12" height="18" rx="2" fill="{GR}" {W(2.4)}/>'.replace('x="58" y="10"', 'x="58" y="10"').replace("/>", f' transform="rotate({a} 64 64)"/>') for a in range(0, 360, 45))
    + f'<circle cx="64" cy="64" r="40" fill="{GR}" {s()}/><circle cx="64" cy="64" r="30" fill="#D6DAE6" {W(2)}/>'
    + f(64, 64, d=10, k=0.8)
    + f'<g transform="rotate(30 104 100)"><rect x="100" y="76" width="8" height="40" rx="3" fill="{BR}" {W(2)}/><path d="M100 76 Q104 62 108 76Z" fill="{R}" {W(2)}/></g>'
    + f'<path d="M86 102 Q92 112 100 108" fill="none" stroke="{R}" stroke-width="4" stroke-linecap="round"/>' + sp((18, 22, 6)))
I["elektrostal-chudo-park"] = ("sky", "малыш в ватрушке-тюбинге катится с горки под люстрой торгового центра",
    f'<path d="M30 0 V12 M98 0 V12" {W(2)}/><path d="M20 12 H108 L100 22 H28Z" fill="{Y}" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="26" r="4" fill="#FFF6C4" {W(1.6)}/>' for x in (36, 52, 76, 92))
    + f'<path d="M0 60 Q60 66 128 118 V128 H0Z" fill="#fff" {s()}/>'
    + f'<g transform="rotate(16 62 80)">' + kid(62, 62, r=16) + f'<path d="M46 60 Q46 42 62 42 Q78 42 78 60Z" fill="{G}" {W(2.6)}/>'
    f'<path d="M22 84 Q22 66 62 66 Q102 66 102 84 Q102 104 62 104 Q22 104 22 84Z" fill="{R}" {s()}/>'
    f'<ellipse cx="62" cy="78" rx="24" ry="7" fill="#B8402F" {W(2)}/><path d="M32 92 Q62 100 92 92" fill="none" stroke="#fff" stroke-width="3" opacity=".6"/>'
    f'<path d="M40 78 L30 66 M84 78 L96 64" {W(4)}/></g>'
    + "".join(f'<path d="M{x} {y} q-6 -2 -12 2" fill="none" stroke="{B}" stroke-width="3" stroke-linecap="round"/>' for x, y in [(22, 70), (16, 84)]))
I["elektrostal-nrg-arena"] = ("night", "лазерный бластер-персонаж с молнией энергии",
    f'<path d="M20 50 H96 Q108 50 108 62 V66 Q108 74 96 74 H64 L56 108 H36 L44 74 H20Z" fill="{B}" {s()}/>'
    f'<rect x="96" y="56" width="22" height="12" rx="3" fill="{GR}" {W(2.4)}/>'
    + f(64, 62, d=9, k=0.65) + f'<path d="M118 62 H128" stroke="#FF5FA2" stroke-width="5"/>'
    + f'<path d="M24 14 l-10 20 h12 l-8 20 l22 -26 h-12 l8 -14Z" fill="{Y}" {W(2.2)}/>'
    + "".join(sparkle(x, y, r, "#FF5FA2") for x, y, r in [(110, 30, 6), (96, 110, 5)]))
I["elektrostal-fly-factory"] = ("sky", "малыш в лётном шлеме парит над батутом, раскинув руки-крылья", tramp(
    f'<path d="M26 56 Q44 44 50 58 M102 56 Q84 44 78 58" fill="none" stroke="{SK}" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M26 56 Q44 44 50 58 M102 56 Q84 44 78 58" fill="none" {W(1.6)}/>'
    f'<rect x="50" y="56" width="28" height="26" rx="10" fill="{OR}" {s()}/><path d="M54 82 L50 92 M74 82 L78 92" {W(4)}/>'
    + kid(64, 42, r=15) + f'<path d="M49 40 Q49 24 64 24 Q79 24 79 40Z" fill="{BR}" {W(2.6)}/>'
    f'<circle cx="58" cy="30" r="4" fill="#9AD6FF" {W(1.6)}/><circle cx="70" cy="30" r="4" fill="#9AD6FF" {W(1.6)}/>', col=Y)
    + "".join(f'<path d="M{x} {y} q8 -4 16 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' for x, y in [(10, 30), (100, 20)]))
I["elektrostal-avangard"] = ("teal", "игрушечный кораблик-парусник на пруду",
    WATER + f'<path d="M24 86 H104 L92 104 H36Z" fill="{R}" {s()}/><path d="M62 86 V20" {W(3)}/>'
    f'<path d="M64 22 Q96 50 96 80 H64Z" fill="#fff" {s()}/><path d="M60 30 Q38 56 36 80 H60Z" fill="{Y}" {s()}/>'
    f'<path d="M64 20 L80 14 L64 10" fill="{B}" {W(2)}/>' + f(64, 94, d=9, k=0.6) + sp((18, 24, 6), (110, 24, 5)))

# ===================== Орехово-Зуево =====================
I["oz-museum"] = ("green", "старинный кожаный футбольный мяч со шнуровкой в кепке",
    GROUND + f'<circle cx="64" cy="72" r="36" fill="{BR}" {s()}/>'
    f'<path d="M30 60 Q64 72 98 60 M30 86 Q64 96 98 86 M64 36 Q52 72 64 108" fill="none" stroke="#7A4A26" stroke-width="3"/>'
    + "".join(f'<path d="M{x} 46 l8 4 M{x} 50 l8 -4" {W(1.8)}/>' for x in (56, 64))
    + f(64, 74, d=10, k=0.75)
    + f'<path d="M30 46 Q32 24 64 24 Q96 24 98 46Z" fill="#E8DCC8" {s()}/><path d="M92 42 Q110 40 116 46 Q104 50 92 46Z" fill="#E8DCC8" {W(2.4)}/>'
    + sp((18, 22, 6)))
I["oz-cosmopark"] = ("purple", "робот-персонаж купается в сухом бассейне",
    f'<path d="M64 14 V24" {W(3)}/><circle cx="64" cy="12" r="5" fill="{R}" {W(2)}/>'
    f'<rect x="36" y="24" width="56" height="40" rx="10" fill="{GR}" {s()}/><rect x="44" y="32" width="40" height="24" rx="6" fill="#E4F6FF" {W(2)}/>'
    + f(64, 42, d=9, k=0.65) + f'<rect x="40" y="64" width="48" height="36" rx="8" fill="#D6DAE6" {s()}/>'
    f'<path d="M40 72 L18 56 M88 72 L110 56" {W(5)}/><circle cx="18" cy="54" r="6" fill="{GR}" {W(2)}/><circle cx="110" cy="54" r="6" fill="{GR}" {W(2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="11" fill="{c}" {W(2.2)}/>' for x, y, c in
              [(8, 104, B), (28, 100, Y), (50, 110, G), (74, 108, R), (96, 102, P), (118, 106, Y), (18, 122, R), (62, 124, B), (106, 124, G), (40, 124, Y), (86, 124, OR)]))
I["oz-chudo-park"] = ("orange", "бельчонок обнимает орех и съезжает с горки",
    f'<path d="M10 124 Q30 120 50 96 Q70 70 96 64 L112 64 V124Z" fill="{B}" {s()}/><path d="M112 64 V24 H124" fill="none" {W(4)}/>'
    + f'<g transform="rotate(-24 56 66)"><path d="M70 74 Q100 60 92 30 Q86 16 74 26 Q86 40 66 60Z" fill="{BR}" {s()}/>'
    f'<ellipse cx="54" cy="74" rx="20" ry="16" fill="{OR}" {s()}/><circle cx="52" cy="50" r="16" fill="{OR}" {s()}/>'
    f'<path d="M40 40 L38 28 L48 36Z M62 38 L66 26 L68 40Z" fill="{OR}" {W(2.2)}/>' + f(52, 52, d=7, k=0.6)
    + f'<ellipse cx="50" cy="78" rx="11" ry="12" fill="#C98A4A" {W(2.4)}/><path d="M42 72 Q50 64 58 72" fill="#7A4A26" {W(2)}/></g>'
    + sp((20, 24, 6)))
I["oz-koldashova-theatre"] = ("night", "раскрытая книга сказок в короне",
    f'<path d="M64 46 Q40 36 14 42 V106 Q40 100 64 110Z" fill="#fff" {s()}/><path d="M64 46 Q88 36 114 42 V106 Q88 100 64 110Z" fill="#FFF6E0" {s()}/>'
    + "".join(f'<path d="M{x1} {y} Q{(x1+x2)//2} {y-4} {x2} {y}" fill="none" stroke="{GR}" stroke-width="2.4"/>' for x1, x2, y in [(22, 56, 92), (72, 106, 92), (72, 106, 100)])
    + f(40, 66, d=7, k=0.6) + f'<path d="M84 80 Q96 58 100 74" fill="none" stroke="{V}" stroke-width="3"/><circle cx="92" cy="64" r="5" fill="{Y}" {W(1.8)}/>'
    + f'<path d="M44 36 L46 16 L56 28 L64 10 L72 28 L82 16 L84 36Z" fill="{GO}" {W(2.4)}/>'
    + "".join(sparkle(x, y, r, Y) for x, y, r in [(16, 24, 5), (112, 22, 6)]))
I["dulevo-porcelain"] = ("pink", "фарфоровый слоник с синей росписью",
    f'<ellipse cx="72" cy="74" rx="36" ry="28" fill="#fff" {s()}/>'
    + "".join(f'<rect x="{x}" y="90" width="13" height="24" rx="5" fill="#fff" {W(2.6)}/>' for x in (48, 86))
    + f'<circle cx="44" cy="58" r="24" fill="#fff" {s()}/><path d="M30 46 Q8 40 12 66 Q16 80 28 72" fill="#E4F0FF" {s()}/>'
    f'<path d="M24 70 Q14 92 24 104 Q30 108 32 102 Q26 92 34 76" fill="#fff" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="#2F5BC4" opacity=".85"/><circle cx="{x}" cy="{y}" r="2" fill="#fff"/>' for x, y in [(70, 66), (88, 76), (78, 86), (96, 62)])
    + f(48, 60, d=7, k=0.6) + f'<path d="M106 70 Q116 76 112 86" fill="none" {W(2.6)}/>' + sp((108, 28, 6)))

# ===================== Подольск =====================
I["podolsk-talalikhin-park"] = ("teal", "весёлая лодочка с вёслами на речке",
    WATER + f'<path d="M14 82 H114 Q104 108 64 108 Q24 108 14 82Z" fill="{OR}" {s()}/>'
    f'<path d="M18 92 H110" stroke="#fff" stroke-width="3"/>'
    f'<path d="M28 60 L8 108 M100 60 L120 108" stroke="{BR}" stroke-width="5" stroke-linecap="round"/>'
    f'<ellipse cx="8" cy="110" rx="5" ry="9" fill="{BR}" {W(2)}/><ellipse cx="120" cy="110" rx="5" ry="9" fill="{BR}" {W(2)}/>'
    + f(64, 92, d=11, k=0.8) + f'<circle cx="96" cy="30" r="12" fill="{Y}" {W(2.4)}/>' + sp((24, 28, 6)))
I["podolsk-jumpyland"] = ("yellow", "малыш-ниндзя в прыжке на батуте", tramp(
    f'<rect x="50" y="54" width="28" height="28" rx="10" fill="{NV}" {s()}/><path d="M50 62 L30 46 M78 62 L98 74" {W(5)}/>'
    f'<path d="M54 82 L44 94 M74 82 L82 92" {W(5)}/>'
    + f'<circle cx="64" cy="38" r="16" fill="{NV}" {s()}/><rect x="50" y="32" width="28" height="11" rx="5" fill="{SK}" {W(2)}/>'
    + eye(58, 37, 0.65) + eye(70, 37, 0.65)
    + f'<path d="M48 34 L34 26 M48 36 L36 40" stroke="{R}" stroke-width="4" stroke-linecap="round"/><path d="M48 32 H80" stroke="{R}" stroke-width="4"/>', col=R)
    + sp((18, 26, 6), (110, 24, 5)))

# ===================== Домодедово =====================
I["domodedovo-yolochki"] = ("sky", "ёлочка-персонаж в кабинке колеса обозрения",
    f'<circle cx="64" cy="54" r="42" fill="none" stroke="#fff" stroke-width="5"/>'
    + "".join(f'<path d="M64 54 L{64+42*c:.0f} {54+42*s_:.0f}" stroke="#fff" stroke-width="2.4"/>' for c, s_ in [(1, 0), (-1, 0), (0, -1), (.7, .7), (-.7, .7), (.7, -.7), (-.7, -.7)])
    + f'<path d="M64 54 L44 124 M64 54 L84 124" {W(4)}/>'
    + "".join(f'<rect x="{x-7}" y="{y}" width="14" height="10" rx="3" fill="{c}" {W(2)}/>' for x, y, c in [(106, 54, R), (22, 54, Y), (94, 24, B), (34, 24, V)])
    + f'<path d="M64 96 L50 104 Q48 120 64 120 Q80 120 78 104Z" fill="{OR}" {s()}/>'
    + f'<path d="M64 74 L52 92 H58 L48 108 H80 L70 92 H76Z" fill="{DG}" {s()}/>' + f(64, 98, d=5, k=0.45)
    + f'<path d="M64 70 l2 4 h4 l-3 3 l1 4 l-4 -2 l-4 2 l1 -4 l-3 -3 h4Z" fill="{Y}" {W(1.2)}/>')
I["domodedovo-museum"] = ("orange", "древняя амфора-персонаж с ручками-«ушками»",
    f'<path d="M50 14 H78 V26 Q96 40 96 70 Q96 102 64 116 Q32 102 32 70 Q32 40 50 26Z" fill="#D9824A" {s()}/>'
    f'<path d="M50 30 Q30 30 30 48 Q32 58 40 56 M78 30 Q98 30 98 48 Q96 58 88 56" fill="none" {W(4)}/>'
    f'<path d="M36 82 H92 M40 92 H88" stroke="#8A4A26" stroke-width="3"/>'
    + "".join(f'<path d="M{x} 86 l4 -3 l4 3" fill="none" stroke="#8A4A26" stroke-width="2"/>' for x in (44, 56, 68, 80))
    + f(64, 62, d=10, k=0.8) + f'<path d="M84 106 l10 -8 l6 6 l-10 10Z" fill="#B66A3A" {W(2)}/>' + sp((20, 24, 6), (110, 24, 5)))
I["domodedovo-batutti"] = ("blue", "пингвинёнок прыгает на батуте", tramp(
    f'<ellipse cx="64" cy="62" rx="24" ry="28" fill="{NV}" {s()}/><ellipse cx="64" cy="68" rx="16" ry="20" fill="#fff"/>'
    f'<path d="M40 56 L24 44 M88 56 L104 44" stroke="{NV}" stroke-width="8" stroke-linecap="round"/>'
    + f(64, 52, d=8, k=0.6).replace(f'fill="{O}"', 'fill="#fff"', 2)
    + f'<path d="M58 60 L64 66 L70 60Z" fill="{OR}" {W(1.8)}/><path d="M52 90 L48 98 H58Z M76 90 L80 98 H70Z" fill="{OR}" {W(2)}/>', col=P)
    + sp((18, 26, 6), (110, 24, 5)))
I["domodedovo-choko-changa"] = ("yellow", "шоколадная плитка-персонаж лезет по скалодрому",
    f'<rect x="0" y="0" width="56" height="128" fill="#BFA6E8" {W(2)}/>'
    + "".join(f'<path d="M{x} {y} q6 -4 10 2 q-4 6 -10 -2Z" fill="{c}" {W(1.6)}/>' for x, y, c in [(10, 20, R), (30, 50, G), (8, 80, Y), (36, 104, B), (40, 14, OR)])
    + f'<g transform="rotate(-8 80 66)"><rect x="54" y="26" width="52" height="76" rx="6" fill="#7A4A26" {s()}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="20" height="20" rx="3" fill="#8E5A34" {W(1.6)}/>' for x in (58, 82) for y in (30, 54, 78))
    + f(80, 64, d=9, k=0.7) + '</g>'
    + f'<path d="M56 46 L40 30 M56 86 L42 100" stroke="#7A4A26" stroke-width="7" stroke-linecap="round"/><path d="M104 96 L110 116" stroke="#7A4A26" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M106 10 Q96 30 92 26" fill="none" {W(2)}/>' + sp((112, 30, 5)))

# ===================== Видное =====================
I["vidnoe-central-park"] = ("pink", "лошадка с карусели на золотом шесте",
    f'<rect x="60" y="4" width="8" height="120" fill="{GO}" {W(2.4)}/><path d="M60 20 l8 6 M60 34 l8 6 M60 100 l8 6 M60 114 l8 6" stroke="#C99A20" stroke-width="2"/>'
    f'<path d="M30 70 Q30 54 50 54 H84 Q98 54 98 68 Q98 84 84 84 H50 Q30 84 30 70Z" fill="#fff" {s()}/>'
    f'<path d="M90 60 Q96 36 108 30 Q120 34 116 48 Q110 54 100 58Z" fill="#fff" {s()}/>'
    f'<path d="M92 44 Q96 26 108 22 M98 48 Q104 34 112 30" fill="none" stroke="{P}" stroke-width="5" stroke-linecap="round"/>'
    + eye(108, 40, 0.6) + f'<ellipse cx="114" cy="48" rx="3" ry="2" fill="#FF7FA8"/>'
    f'<path d="M40 82 L34 104 M54 84 L52 106 M82 84 L86 106 M92 80 L100 100" {W(4)}/>'
    f'<path d="M30 64 Q16 60 14 76" fill="none" stroke="{P}" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M50 54 Q64 46 78 54 Q64 64 50 54Z" fill="{V}" {W(2)}/>' + sp((20, 24, 6), (108, 108, 5)))
I["vidnoe-history-center"] = ("night", "старинный уличный фонарь-персонаж",
    f'<rect x="58" y="70" width="12" height="54" fill="{NV}" stroke="#9AA0C8" stroke-width="2.4"/><path d="M44 124 H84" stroke="#9AA0C8" stroke-width="5"/>'
    f'<path d="M40 30 H88 L80 72 H48Z" fill="#FFE07A" stroke="#9AA0C8" stroke-width="3"/><path d="M36 30 L64 12 L92 30Z" fill="{NV}" stroke="#9AA0C8" stroke-width="3"/>'
    f'<circle cx="64" cy="8" r="4" fill="{NV}" stroke="#9AA0C8" stroke-width="2"/>'
    + f(64, 50, d=8, k=0.65) + f'<circle cx="64" cy="50" r="40" fill="{Y}" opacity=".15"/>'
    + "".join(sparkle(x, y, r, Y) for x, y, r in [(18, 24, 5), (108, 20, 6), (100, 96, 3)]))

if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        bg, subj, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(bg, body))
    print("svg:", len(ids))
