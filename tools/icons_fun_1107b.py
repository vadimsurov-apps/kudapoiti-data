"""Иконки робота fun (2026-11-07, утро): 18 мест — скалодромы, Зеленоград, Долгопрудный, Федоскино, два театра.
Каждая иконка придумана отдельно (правило абсолютной уникальности 07.11): свой герой, своя сцена, своя компоновка
и свой фон. Сверено со всеми icons-catalog/sheet-*.png и icons-src/subjects.txt (на скалодромах уже заняты:
ребёнок на стене, муравей, гора, кран, мешочек магнезии, зелёная зацепа, рысь, скала, небоскрёб, ленивец, тупик).
Запуск: python3 tools/icons_fun_1107b.py [id ...]"""
import os, sys
from draw_icons import s, eye, face, sparkle, O

W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=9, k=0.75, **kw: face(cx, cy, d=d, k=k, **kw)
sp = lambda *pts: "".join(sparkle(x, y, r) for x, y, r in pts)
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
R, OR, Y, G, B, P, V, WH, GR = ("#E8654F", "#FF9A3D", "#FFD25E", "#7CD26E", "#5CB7F2", "#FF8FB8", "#A98BF0",
                                "#FFFFFF", "#B8BCCB")
NV, GO, BR = "#2B2A44", "#F2B632", "#9A6A44"


def svg(a, b, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
<defs>
 <radialGradient id="g" cx="38%" cy="28%" r="85%"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></radialGradient>
 <clipPath id="c"><circle cx="64" cy="64" r="61"/></clipPath>
</defs>
<circle cx="64" cy="64" r="61" fill="url(#g)"/>
<g clip-path="url(#c)">{body}</g>
<ellipse cx="44" cy="22" rx="20" ry="7" fill="#fff" opacity=".3"/>
</svg>'''


def hold(x, y, r, c, rot=0):
    """зацепа скалодрома — неровная капля с винтом"""
    return (f'<g transform="rotate({rot} {x} {y})"><path d="M{x-r} {y} Q{x-r} {y-r*0.9} {x} {y-r} Q{x+r*1.1} {y-r*0.8} '
            f'{x+r} {y+r*0.1} Q{x+r*0.7} {y+r} {x-r*0.1} {y+r*0.8} Q{x-r} {y+r*0.6} {x-r} {y}Z" fill="{c}" {W(2)}/>'
            f'<circle cx="{x}" cy="{y}" r="{max(1.4, r*0.22):.1f}" fill="{O}" opacity=".55"/></g>')


I = {}
# ---------------------------------------------------------------- скалодромы
I["tengu-lobachevskogo"] = ("#FFF1E0", "#F0A35C",
    "салатовый геккон с круглыми подушечками на пальцах", "ползёт вверх по наклонной стене скалодрома, цепляясь за разноцветные зацепы",
    f'<path d="M0 30 L128 6 V128 H0Z" fill="#F7E3C7" {W(2.4)}/>'
    + hold(22, 50, 7, R) + hold(104, 34, 7, B, 30) + hold(100, 104, 8, V, -20) + hold(20, 108, 7, Y, 50) + hold(108, 70, 5, P)
    + f'<path d="M64 88 Q70 110 92 118 Q104 120 108 112" fill="none" stroke="#9BD45A" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M64 88 Q70 110 92 118 Q104 120 108 112" fill="none" {W(1.6)} opacity=".0"/>'
    + "".join(f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#9BD45A" stroke-width="7" stroke-linecap="round"/>'
              f'<circle cx="{x2}" cy="{y2}" r="5" fill="#C9F08A" {W(1.8)}/>' for x1, y1, x2, y2 in
              [(54, 56, 30, 50), (74, 56, 98, 38), (54, 86, 28, 104), (74, 86, 96, 100)])
    + f'<ellipse cx="64" cy="72" rx="15" ry="22" fill="#9BD45A" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#6FAE3A"/>' for x, y in [(58, 66), (70, 72), (60, 82), (68, 60)])
    + f'<ellipse cx="64" cy="38" rx="17" ry="15" fill="#9BD45A" {s()}/>' + f(64, 38, d=8, k=0.85))

I["tengu-yuzhnaya"] = ("#F2F4F8", "#9AA6BD",
    "пара скальных туфель с загнутыми носами", "висят, связанные шнурками, на большой жёлтой зацепе",
    f'<rect x="0" y="0" width="128" height="128" fill="#DCE1EC"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1.6" fill="#A7AFC2"/>' for x in range(12, 128, 20) for y in range(10, 128, 20))
    + hold(64, 24, 14, Y)
    + f'<path d="M58 30 Q40 46 38 62 M70 30 Q88 46 90 58" fill="none" stroke="#fff" stroke-width="3.6"/>'
    f'<path d="M58 30 Q40 46 38 62 M70 30 Q88 46 90 58" fill="none" {W(1.2)}/>'
    f'<g transform="rotate(-14 38 84)"><path d="M26 62 H50 V92 Q50 104 38 106 Q16 108 10 100 Q8 94 18 92 Q26 90 26 82Z" fill="{R}" {s()}/>'
    f'<path d="M10 100 Q8 94 18 92 Q30 92 50 98 V104 Q30 110 10 100Z" fill="{NV}" {W(1.6)}/>' + f(37, 76, d=6, k=0.6) + '</g>'
    f'<g transform="rotate(12 92 82)"><path d="M80 58 H104 V88 Q104 100 92 102 Q70 104 64 96 Q62 90 72 88 Q80 86 80 78Z" fill="{V}" {s()}/>'
    f'<path d="M64 96 Q62 90 72 88 Q84 88 104 94 V100 Q84 106 64 96Z" fill="{NV}" {W(1.6)}/>' + f(91, 72, d=6, k=0.6) + '</g>')

I["tengu-maryina-roshcha"] = ("#FFF0F6", "#D98CB3",
    "серый опоссум с розовым носиком", "висит вниз головой, зацепившись хвостом за оранжевую зацепу",
    f'<rect x="0" y="0" width="128" height="16" fill="#C97FA6"/>'
    + hold(64, 20, 11, OR)
    + f'<path d="M64 30 Q50 26 54 18 Q60 10 70 16 Q76 22 68 28" fill="none" stroke="#F4B6C8" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M64 30 Q64 38 64 42" stroke="#F4B6C8" stroke-width="7" stroke-linecap="round"/>'
    f'<ellipse cx="64" cy="64" rx="22" ry="24" fill="#B6B4C4" {s()}/>'
    f'<path d="M44 58 Q36 64 40 72 M84 58 Q92 64 88 72" fill="none" stroke="#B6B4C4" stroke-width="7" stroke-linecap="round"/>'
    f'<circle cx="38" cy="74" r="4" fill="#F4B6C8" {W(1.6)}/><circle cx="90" cy="74" r="4" fill="#F4B6C8" {W(1.6)}/>'
    f'<circle cx="46" cy="102" r="9" fill="#F4B6C8" {s()}/><circle cx="82" cy="102" r="9" fill="#F4B6C8" {s()}/>'
    f'<path d="M64 120 Q42 110 44 92 Q48 80 64 80 Q80 80 84 92 Q86 110 64 120Z" fill="#fff" {s()}/>'
    f'<ellipse cx="64" cy="116" rx="5" ry="4" fill="#FF7FA8" {W(1.6)}/>'
    + eye(56, 96, 0.8) + eye(72, 96, 0.8)
    + f'<path d="M59 104 Q64 109 69 104" fill="none" {W(2.2)}/>')

I["bigwall-dinamo"] = ("#E8FBFF", "#5FB2D9",
    "пухлый рыжий сурок", "встал столбиком на самой верхушке скалодрома и машет лапой",
    f'<path d="M20 128 L32 70 H96 L108 128Z" fill="#F4F0E6" {s()}/>'
    + hold(48, 86, 6, R) + hold(80, 82, 6, B, 40) + hold(62, 104, 7, G, -10) + hold(90, 112, 6, V) + hold(40, 116, 6, Y)
    + f'<rect x="28" y="66" width="72" height="8" rx="3" fill="#C6B9A0" {W(2)}/>'
    f'<path d="M48 66 Q44 30 64 24 Q84 30 80 66Z" fill="#C98A4E" {s()}/>'
    f'<ellipse cx="64" cy="52" rx="10" ry="12" fill="#F2D3A6"/>'
    f'<circle cx="54" cy="26" r="5" fill="#B2733C" {W(2)}/><circle cx="74" cy="26" r="5" fill="#B2733C" {W(2)}/>'
    + f(64, 36, d=7, k=0.7)
    + f'<rect x="60" y="42" width="8" height="5" rx="1.5" fill="#fff" {W(1.4)}/>'
    f'<path d="M78 48 Q92 40 94 26" fill="none" stroke="#C98A4E" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M78 48 Q92 40 94 26" fill="none" {W(1.4)} opacity=".0"/>'
    f'<circle cx="94" cy="24" r="5" fill="#C98A4E" {W(2)}/>'
    f'<path d="M100 18 l6 -4 M102 26 l7 0" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')

I["bigwall-vodny"] = ("#F6FFE0", "#B8D45A",
    "толстый синий мат-подушка для боулдеринга", "лежит под стеной, раскинув ручки, и ловит падающую розовую зацепу",
    f'<rect x="0" y="0" width="128" height="78" fill="#EDE4D0"/>'
    + hold(26, 22, 6, OR) + hold(98, 18, 6, V, 30) + hold(40, 54, 6, B) + hold(102, 52, 5, R)
    + f'<g transform="rotate(25 66 30)">' + hold(66, 30, 9, P) + '</g>'
    f'<path d="M58 14 l-4 -8 M66 12 v-9 M74 14 l4 -8" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    f'<path d="M8 84 Q8 74 18 74 H110 Q120 74 120 84 V112 Q120 122 110 122 H18 Q8 122 8 112Z" fill="#3E7FD6" {s()}/>'
    f'<path d="M14 100 H114" stroke="#2E62A8" stroke-width="3"/>'
    f'<path d="M24 76 Q14 60 22 48 M104 76 Q114 60 106 48" fill="none" stroke="#3E7FD6" stroke-width="8" stroke-linecap="round"/>'
    f'<circle cx="22" cy="46" r="6" fill="#3E7FD6" {W(2)}/><circle cx="106" cy="46" r="6" fill="#3E7FD6" {W(2)}/>'
    + f'<g>{f(64, 88, d=10, k=0.85)}</g>')

I["bigwall-crocus"] = ("#5A4A9E", "#2A2160",
    "долгопят с огромными круглыми глазами", "обнимает длинными пальцами большую зелёную зацепу на ночной стене",
    "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="#fff" opacity=".7"/>' for x, y in [(18, 30), (110, 24), (100, 110), (14, 96), (36, 14)])
    + f'<path d="M64 90 Q96 110 108 96 Q116 84 104 80" fill="none" stroke="#8C6A4A" stroke-width="4" stroke-linecap="round"/>'
    + hold(64, 92, 20, "#57C08F")
    + f'<ellipse cx="64" cy="76" rx="20" ry="16" fill="#B98A5E" {s()}/>'
    f'<circle cx="64" cy="48" r="26" fill="#C99B6C" {s()}/>'
    f'<path d="M40 34 Q30 18 40 16 Q48 18 46 30 M88 34 Q98 18 88 16 Q80 18 82 30" fill="#E7B98E" {W(2)}/>'
    + "".join(f'<circle cx="{x}" cy="48" r="12" fill="#F6D27A" {W(2.2)}/><circle cx="{x}" cy="49" r="8" fill="{O}"/>'
              f'<circle cx="{x-3}" cy="45" r="3" fill="#fff"/>' for x in (52, 76))
    + f'<path d="M60 64 Q64 68 68 64" fill="none" {W(2.2)}/><circle cx="64" cy="60" r="2" fill="#7A4E2E"/>'
    + "".join(f'<path d="M{x} 84 Q{x+d} 92 {x+2*d} 96" fill="none" stroke="#C99B6C" stroke-width="4" stroke-linecap="round"/>'
              f'<circle cx="{x+2*d}" cy="96" r="3" fill="#E7B98E" {W(1.4)}/>' for x, d in [(50, -5), (56, -2), (72, 2), (78, 5)])
    + sp((20, 60, 5), (110, 64, 4)))

I["skalodrom-ru-odintsovo"] = ("#FFFCE0", "#E7C24A",
    "голубоспинный поползень с чёрной полоской у глаза", "спускается по стене скалодрома вниз головой, как по стволу дерева",
    f'<rect x="30" y="0" width="68" height="128" fill="#F6EFD8" {W(2.4)}/>'
    + hold(46, 18, 6, R) + hold(84, 30, 6, V) + hold(44, 112, 7, B) + hold(86, 108, 6, G, 30)
    + hold(40, 58, 6, OR) + hold(88, 62, 6, P, 40)
    + f'<path d="M56 30 L64 8 L72 30Z" fill="#5D7BA8" {W(2)}/>'
    f'<ellipse cx="64" cy="58" rx="19" ry="30" fill="#7E9CC9" {s()}/>'
    f'<path d="M70 32 Q84 56 74 84 Q80 58 70 32Z" fill="#F5A35A" {W(1.6)}/>'
    f'<path d="M50 46 Q56 60 52 74" fill="none" stroke="#5D7BA8" stroke-width="3"/>'
    f'<path d="M48 58 L40 58 M80 62 L88 62" stroke="#4A4A5C" stroke-width="3" stroke-linecap="round"/>'
    f'<circle cx="64" cy="92" r="17" fill="#7E9CC9" {s()}/>'
    f'<path d="M64 108 L59 122 L69 122Z" fill="#4A4A5C" {W(1.6)}/>'
    f'<ellipse cx="64" cy="100" rx="12" ry="6" fill="#FFF3DC"/>'
    f'<path d="M47 88 H81" stroke="{NV}" stroke-width="5" stroke-linecap="round"/>'
    + eye(57, 88, 0.7) + eye(71, 88, 0.7)
    + f'<ellipse cx="52" cy="97" rx="3.6" ry="2.2" fill="#FF7FA8" opacity=".6"/><ellipse cx="76" cy="97" rx="3.6" ry="2.2" fill="#FF7FA8" opacity=".6"/>')

I["staraya-shkola-climb"] = ("#E9F7F1", "#5FAF96",
    "кусочек белого школьного мела в круглых очках", "рисует пунктирную стрелку-маршрут между зацепами на тёмно-зелёной стене-доске",
    f'<rect x="8" y="12" width="112" height="86" rx="4" fill="#2F5E4E" {s()}/>'
    f'<rect x="8" y="94" width="112" height="8" fill="#B98A5E" {W(2)}/>'
    + hold(26, 80, 6, Y) + hold(48, 54, 6, R) + hold(36, 30, 6, B, 40) + hold(70, 26, 6, P)
    + f'<path d="M30 74 Q40 64 46 60 M50 48 Q44 40 40 36 M42 28 Q56 22 64 26" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="5 4" stroke-linecap="round"/>'
    f'<path d="M66 22 l4 -6 M66 22 l7 1" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    f'<g transform="rotate(-28 92 74)"><rect x="80" y="44" width="24" height="62" rx="5" fill="#FBFBF4" {s()}/>'
    f'<path d="M80 98 H104" stroke="#E2E2D6" stroke-width="5"/>'
    + "".join(f'<circle cx="{x}" cy="64" r="6.5" fill="#fff" fill-opacity=".4" {W(2)}/>' for x in (86, 99))
    + f'<path d="M92.5 64 h0.1" {W(2)}/>' + eye(86, 64, 0.55) + eye(99, 64, 0.55)
    + f'<path d="M88 76 Q92.5 80 97 76" fill="none" {W(2)}/></g>'
    f'<path d="M14 104 Q10 112 18 116 M108 104 Q118 112 110 118" fill="none" stroke="#fff" stroke-width="2.4" opacity=".7"/>')

I["raduga-climb-shcherbinka"] = ("#FFF3E8", "#E58B6E",
    "золотистый панголин в чешуйках-лепестках", "карабкается по стене, где зацепы выложены всеми цветами радуги",
    f'<path d="M0 0 H128 V128 H0Z" fill="#FBE3D3"/>'
    + "".join(hold(x, y, 5.5, c, x) for x, y, c in [(14, 40, R), (26, 22, OR), (46, 12, Y), (82, 12, G), (102, 22, B), (114, 40, "#4C6FD6"), (118, 62, V)])
    + f'<g transform="rotate(-35 62 74)">'
    f'<path d="M24 84 Q20 58 50 54 Q84 50 100 70 Q104 86 88 92 Q60 100 24 84Z" fill="#E2A64E" {s()}/>'
    + "".join(f'<path d="M{x} {y} q7 -9 14 0" fill="#D08E36" {W(1.8)}/>' for x, y in
              [(32, 74), (46, 66), (60, 62), (74, 66), (86, 74), (40, 82), (54, 78), (68, 78), (80, 84)])
    + f'<path d="M24 84 Q8 94 4 112" fill="none" stroke="#E2A64E" stroke-width="10" stroke-linecap="round"/>'
    f'<path d="M94 64 Q116 54 122 72 Q122 90 98 90Z" fill="#F0C98E" {s()}/>'
    + eye(106, 70, 0.8) + eye(116, 72, 0.7) + f'<ellipse cx="104" cy="80" rx="3.6" ry="2.2" fill="#FF7FA8" opacity=".7"/>'
    + f'<path d="M108 80 Q112 84 116 80" fill="none" {W(2)}/>'
    + "".join(f'<path d="M{x} 92 l-2 10 M{x+4} 92 l2 10" stroke="{NV}" stroke-width="2.2" stroke-linecap="round"/>' for x in (44, 78))
    + '</g>')

I["highwall-kurkino"] = ("#F7EBFF", "#A77BD9",
    "квокка с широкой улыбкой", "висит на двух руках на стене-борту корабля с круглыми иллюминаторами вместо зацеп",
    f'<path d="M-4 20 Q64 6 132 20 V128 H-4Z" fill="#E9D4B8" {s()}/>'
    + "".join(f'<path d="M-4 {y} Q64 {y-14} 132 {y}" fill="none" stroke="#C9A982" stroke-width="2.4"/>' for y in (44, 70, 96))
    + "".join(f'<circle cx="{x}" cy="{y}" r="8" fill="#9FD8F2" stroke="{GO}" stroke-width="4"/><circle cx="{x}" cy="{y}" r="8" fill="none" {W(1.4)}/>'
              for x, y in [(36, 30), (92, 30), (20, 96), (108, 100)])
    + f'<path d="M50 52 Q40 40 36 36 M78 52 Q88 40 92 36" fill="none" stroke="#B08560" stroke-width="8" stroke-linecap="round"/>'
    f'<ellipse cx="64" cy="94" rx="18" ry="22" fill="#C29B74" {s()}/>'
    f'<ellipse cx="64" cy="98" rx="10" ry="13" fill="#EED7BC"/>'
    f'<circle cx="48" cy="48" r="8" fill="#C29B74" {W(2)}/><circle cx="80" cy="48" r="8" fill="#C29B74" {W(2)}/>'
    f'<circle cx="64" cy="64" r="20" fill="#C29B74" {s()}/>'
    f'<circle cx="49" cy="50" r="4" fill="#E8B7A6"/><circle cx="79" cy="50" r="4" fill="#E8B7A6"/>'
    + eye(57, 62, 0.75) + eye(71, 62, 0.75)
    + f'<ellipse cx="64" cy="70" rx="3.4" ry="2.4" fill="{NV}"/>'
    f'<path d="M54 74 Q64 84 74 74" fill="#fff" {W(2.2)}/>'
    f'<ellipse cx="50" cy="72" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/><ellipse cx="78" cy="72" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/>')

# ---------------------------------------------------------------- Зеленоград
I["zelenograd-museum"] = ("#FFF8EC", "#D9B27C",
    "каменный топорик с деревянной рукоятью", "выглядывает из песчаного раскопа, расчерченного верёвочкой на квадраты",
    f'<path d="M0 70 Q64 58 128 70 V128 H0Z" fill="#F0D29A" {s()}/>'
    + "".join(f'<path d="M{x} 66 L{x+(x-64)//3} 128" stroke="#fff" stroke-width="2"/>' for x in (24, 50, 78, 104))
    + f'<path d="M0 94 Q64 84 128 94" fill="none" stroke="#fff" stroke-width="2"/>'
    + "".join(f'<rect x="{x-3}" y="{y}" width="6" height="12" fill="#B98A5E" {W(1.4)}/>' for x, y in [(24, 60), (104, 60)])
    + f'<g transform="rotate(-24 64 60)"><rect x="60" y="24" width="10" height="64" rx="4" fill="#B5723E" {s()}/>'
    f'<path d="M34 30 Q30 50 40 60 Q56 64 66 54 V30 Q54 22 34 30Z" fill="#8F96A8" {s()}/>'
    f'<path d="M40 36 Q38 46 42 54" fill="none" stroke="#B9BFCC" stroke-width="3"/>'
    f'<path d="M58 30 L74 40 M58 46 L74 36" stroke="#D9B27C" stroke-width="3"/>'
    + f(52, 44, d=6, k=0.6) + '</g>'
    f'<path d="M30 88 Q64 76 98 88 Q64 96 30 88Z" fill="#E7C27F"/>' + sp((106, 34, 6), (20, 40, 4)))

I["zelenograd-museum-hall"] = ("#FCEFF0", "#C76B7A",
    "латунные столбики с бархатным канатом", "вежливо охраняют картину с солнышком в золотой раме",
    f'<rect x="0" y="98" width="128" height="30" fill="#E7C9A8"/>'
    f'<rect x="30" y="14" width="68" height="54" fill="{GO}" {s()}/><rect x="38" y="22" width="52" height="38" fill="#BFE6FF" {W(2)}/>'
    f'<path d="M38 60 Q56 46 70 54 Q80 48 90 56 V60Z" fill="{G}" {W(1.6)}/><circle cx="74" cy="36" r="7" fill="{Y}" {W(1.6)}/>'
    + "".join(f'<rect x="{x-4}" y="66" width="8" height="40" rx="3" fill="#E2B23E" {s()}/>'
              f'<circle cx="{x}" cy="64" r="7" fill="#F2C94C" {s()}/><ellipse cx="{x}" cy="108" rx="11" ry="4" fill="#C9962C" {W(2)}/>'
              + f(x, 84, d=2.6, k=0.4, blush=False) for x in (22, 106))
    + f'<path d="M28 68 Q64 96 100 68" fill="none" stroke="#9E1F3C" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M28 68 Q64 96 100 68" fill="none" stroke="#C93A5A" stroke-width="4" stroke-linecap="round"/>')

I["miet-museum"] = ("#EFFAFF", "#6CB4C9",
    "чёрный транзистор-«таблетка» на трёх ножках", "шагает по зелёной печатной плате мимо медных дорожек",
    f'<path d="M0 84 L128 76 V128 H0Z" fill="#3E9B5A" {s()}/>'
    + "".join(f'<path d="M{x} 128 V{y} H{x+18}" fill="none" stroke="#E5A653" stroke-width="3"/><circle cx="{x+18}" cy="{y}" r="3" fill="#E5A653" {W(1.2)}/>'
              for x, y in [(8, 100), (90, 96), (100, 116), (20, 118)])
    + f'<path d="M40 30 H88 V76 H40Z" fill="#2E2E3A" {s()}/>'
    f'<path d="M40 30 Q64 18 88 30" fill="#2E2E3A" {s()}/><rect x="40" y="30" width="48" height="10" fill="#4A4A5A"/>'
    f'<path d="M50 76 L44 98 M64 76 V100 M78 76 L86 96" stroke="#C7CCD6" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M50 76 L44 98 M64 76 V100 M78 76 L86 96" fill="none" {W(1.2)} opacity=".0"/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="5" ry="2.5" fill="#C7CCD6" {W(1.4)}/>' for x, y in [(44, 99), (64, 101), (87, 97)])
    + f'<ellipse cx="54" cy="56" rx="4" ry="4.8" fill="#fff"/><ellipse cx="74" cy="56" rx="4" ry="4.8" fill="#fff"/>'
    f'<circle cx="55" cy="57" r="2.2" fill="{NV}"/><circle cx="75" cy="57" r="2.2" fill="{NV}"/>'
    f'<path d="M58 66 Q64 70 70 66" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'
    f'<path d="M100 40 l6 -6 M104 50 h8 M100 60 l6 6" stroke="{Y}" stroke-width="3" stroke-linecap="round"/>')

I["zelenograd-dom-lani"] = ("#EEF8E6", "#6FA86A",
    "крапчатая перепёлка с хохолком-капелькой", "семенит по лесной тропинке между ёлочками к кормушке экоцентра",
    f'<path d="M40 128 Q56 96 64 80 Q72 96 92 128Z" fill="#E8D3A6" {W(2)}/>'
    + "".join(f'<path d="M{x} {y} L{x-12} {y+26} H{x+12}Z" fill="#3F8F55" {W(2)}/><rect x="{x-2}" y="{y+26}" width="4" height="6" fill="#8A5A3A"/>'
              for x, y in [(16, 40), (112, 34), (24, 74), (106, 72)])
    + f'<ellipse cx="62" cy="80" rx="30" ry="24" fill="#B58A5E" {s()}/>'
    f'<ellipse cx="60" cy="86" rx="20" ry="14" fill="#E8CFA6"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="#6E4A2C"/>' for x, y in [(48, 72), (58, 68), (70, 70), (80, 76), (52, 92), (66, 94), (74, 88)])
    + f'<path d="M90 70 Q104 66 108 78 L98 82Z" fill="#8A6440" {W(2)}/>'
    f'<circle cx="46" cy="52" r="16" fill="#B58A5E" {s()}/>'
    f'<path d="M48 36 Q46 22 58 22 Q54 30 52 38" fill="{NV}" {W(1.6)}/><circle cx="58" cy="22" r="4" fill="{NV}"/>'
    + f(44, 52, d=6, k=0.6)
    + f'<path d="M30 54 L22 56 L30 60Z" fill="{OR}" {W(1.6)}/>'
    f'<path d="M50 104 V114 M70 104 V114 M50 114 l-5 3 M50 114 l5 3 M70 114 l-5 3 M70 114 l5 3" stroke="{OR}" stroke-width="3" stroke-linecap="round"/>')

# ---------------------------------------------------------------- Долгопрудный, Федоскино
I["dolgoprudny-museum"] = ("#E9EEFF", "#5C6FC2",
    "двустворчатые шлюзовые ворота канала", "распахиваются, пропуская маленький белый пароходик с красной трубой",
    f'<rect x="0" y="78" width="128" height="50" fill="#5BB6E8" {W(2)}/>'
    f'<path d="M0 94 Q16 90 32 94 T64 94 T96 94 T128 94" fill="none" stroke="#fff" stroke-width="2.4"/>'
    f'<rect x="0" y="36" width="20" height="50" fill="#B9BCC8" {s()}/><rect x="108" y="36" width="20" height="50" fill="#B9BCC8" {s()}/>'
    f'<path d="M20 40 L46 54 V96 L20 88Z" fill="#8C6A4A" {s()}/><path d="M108 40 L82 54 V96 L108 88Z" fill="#8C6A4A" {s()}/>'
    + "".join(f'<path d="M20 {y} L46 {y+14}" stroke="#6E5038" stroke-width="2.4"/><path d="M108 {y} L82 {y+14}" stroke="#6E5038" stroke-width="2.4"/>' for y in (56, 72))
    + f(33, 66, d=4, k=0.45) + f(95, 66, d=4, k=0.45)
    + f'<path d="M48 86 H80 L76 98 H52Z" fill="#fff" {s()}/><rect x="56" y="76" width="16" height="10" fill="#fff" {W(2)}/>'
    f'<rect x="60" y="62" width="7" height="14" fill="{R}" {W(2)}/>'
    f'<path d="M64 56 q-6 -8 2 -14 q8 -6 2 -14" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>'
    f'<circle cx="58" cy="91" r="2.4" fill="{B}" {W(1.2)}/><circle cx="70" cy="91" r="2.4" fill="{B}" {W(1.2)}/>')

I["fedoskino-lukutin"] = ("#FFFBEA", "#C9A13B",
    "овальная чёрная лаковая брошь с ромашками", "лежит на бархатной вишнёвой подушечке под стеклянным колпаком витрины",
    f'<path d="M24 104 Q24 30 64 22 Q104 30 104 104Z" fill="#E9F6FF" fill-opacity=".55" {s()}/>'
    f'<ellipse cx="64" cy="106" rx="50" ry="10" fill="#8C6A4A" {s()}/>'
    f'<path d="M30 100 Q30 84 64 84 Q98 84 98 100 Q98 108 64 108 Q30 108 30 100Z" fill="#B02E4C" {s()}/>'
    f'<ellipse cx="64" cy="64" rx="28" ry="22" fill="{GO}" {s()}/><ellipse cx="64" cy="64" rx="23" ry="17" fill="#1E1B2A"/>'
    + "".join(f'<g transform="translate({x} {y})">' + "".join(f'<ellipse cx="0" cy="-4" rx="1.8" ry="3.6" fill="#fff" transform="rotate({a})"/>' for a in range(0, 360, 45))
              + f'<circle r="2" fill="{Y}"/></g>' for x, y in [(52, 56), (76, 58), (64, 74)])
    + f'<path d="M58 62 Q64 66 70 62 M54 70 l6 -2 M74 70 l-6 -2" stroke="#5FAF5A" stroke-width="2" fill="none"/>'
    + eye(57, 66, 0.45) + eye(71, 66, 0.45)
    + f'<path d="M36 40 Q40 30 50 28" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>'
    + sp((100, 40, 6), (24, 70, 4)))

# ---------------------------------------------------------------- театры
I["dmtya-theatre"] = ("#FFEDEA", "#E36C5B",
    "полукруглая суфлёрская будка с окошком", "выглядывает из края сцены и подсказывает слова из раскрытой тетрадки",
    f'<path d="M0 0 H22 Q18 50 26 100 H0Z M128 0 H106 Q110 50 102 100 H128Z" fill="#B3263A" {s()}/>'
    f'<rect x="0" y="88" width="128" height="40" fill="#C98D52" {W(2.4)}/>'
    + "".join(f'<path d="M{x} 92 V128" stroke="#A86E3A" stroke-width="2"/>' for x in (20, 44, 68, 92, 116))
    + f'<path d="M30 92 Q30 46 64 46 Q98 46 98 92Z" fill="#7A2340" {s()}/>'
    f'<path d="M40 92 Q40 60 64 60 Q88 60 88 92Z" fill="#2B2A44"/>'
    f'<circle cx="64" cy="78" r="13" fill="#FFD9B8" {s()}/>' + f(64, 78, d=5, k=0.5)
    + f'<path d="M50 94 L64 88 L78 94 L78 104 L64 98 L50 104Z" fill="#fff" {W(2)}/><path d="M64 88 V98" {W(1.6)}/>'
    f'<path d="M54 94 h6 M68 94 h6" stroke="#9AA" stroke-width="1.4"/>'
    f'<path d="M86 40 Q100 30 112 40 Q118 52 104 54 L96 60 L98 52 Q84 50 86 40Z" fill="#fff" {W(2)}/>'
    f'<path d="M94 44 h12 M94 48 h8" stroke="{R}" stroke-width="2" stroke-linecap="round"/>')

I["galateya-solnechnogorsk"] = ("#FBF0E6", "#B98A68",
    "латунный гардеробный номерок с цифрой 7", "висит на крючке театральной вешалки рядом с маленьким жёлтым пальтишком",
    f'<rect x="0" y="22" width="128" height="10" fill="#8A5A3A" {s()}/>'
    + "".join(f'<path d="M{x} 32 V42 Q{x} 50 {x+6} 48" fill="none" stroke="#5B5B6B" stroke-width="3" stroke-linecap="round"/>' for x in (28, 64, 100))
    + f'<path d="M84 46 Q100 40 116 46 L122 100 Q100 106 78 100Z" fill="{Y}" {s()}/>'
    f'<path d="M100 44 V102" {W(1.8)}/>' + "".join(f'<circle cx="104" cy="{y}" r="2.2" fill="{R}"/>' for y in (60, 72, 84))
    + f'<path d="M84 46 Q90 56 100 52 Q110 56 116 46" fill="#F5B52E" {W(2)}/>'
    + f'<path d="M64 42 V52" stroke="#5B5B6B" stroke-width="3"/>'
    f'<path d="M64 54 L42 70 V110 Q64 120 86 110 V70Z" fill="#E7B94A" {s()}/>'
    f'<circle cx="64" cy="64" r="5" fill="#FBF0E6" {W(2)}/>'
    f'<text x="64" y="104" font-family="Arial" font-weight="bold" font-size="18" fill="#7A4E1E" text-anchor="middle">7</text>'
    + f(64, 82, d=8, k=0.65)
    + f'<path d="M14 50 Q20 44 26 50 L30 96 Q20 100 10 96Z" fill="#7CB7E8" {s()}/>')

if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        a, b, hero, scene, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
    print("svg:", len(ids))
