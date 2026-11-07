"""Иконки робота fun (2026-11-07, ночь): 34 места — Подольск, Климовск, Раменское, Химки, Мытищи, Балашиха,
Королёв, Видное, Красногорск, Реутов. Каждая иконка придумана отдельно (правило абсолютной уникальности 07.11):
свой герой, своя сцена, своя компоновка и свой фон (у каждой иконки своя пара цветов градиента).
Сверено со всеми icons-catalog/sheet-*.png и icons-src/subjects.txt.
Запуск: python3 tools/icons_fun_1107.py [id ...]"""
import os, sys
from draw_icons import s, eye, face, sparkle, O

W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=9, k=0.75, **kw: face(cx, cy, d=d, k=k, **kw)
sp = lambda *pts: "".join(sparkle(x, y, r) for x, y, r in pts)
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
R, OR, Y, G, B, P, V, BR, WH, GR = ("#E8654F", "#FF9A3D", "#FFD25E", "#7CD26E", "#5CB7F2", "#FF8FB8", "#A98BF0",
                                    "#C0732E", "#FFFFFF", "#B8BCCB")
DG, SK, NV, GO = "#4E9A5A", "#FFD9B8", "#2B2A44", "#F2B632"


def svg(a, b, body):
    """Свой фон у каждой иконки: a — светлый центр, b — край."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
<defs>
 <radialGradient id="g" cx="38%" cy="28%" r="85%"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></radialGradient>
 <clipPath id="c"><circle cx="64" cy="64" r="61"/></clipPath>
</defs>
<circle cx="64" cy="64" r="61" fill="url(#g)"/>
<g clip-path="url(#c)">{body}</g>
<ellipse cx="44" cy="22" rx="20" ry="7" fill="#fff" opacity=".3"/>
</svg>'''


I = {}
# ======================= Подольск, Климовск =======================
I["podolsk-ivanovskoe-estate"] = ("#FFF3DC", "#E2A86E",
    "деревянный рубанок-мастер с круглой ручкой", "строгает доску на верстаке, из-под него вьётся кудрявая стружка",
    f'<rect x="4" y="92" width="120" height="14" fill="#C98D52" {s()}/><path d="M14 106 V128 M114 106 V128" {W(8)}/>'
    f'<path d="M14 106 V128 M114 106 V128" stroke="#A86E3A" stroke-width="5"/>'
    f'<path d="M30 70 H100 Q106 70 106 76 V92 H24 V76 Q24 70 30 70Z" fill="#E7B36F" {s()}/>'
    f'<path d="M58 70 L66 56 L74 70Z" fill="{GR}" {W(2.4)}/>'
    f'<path d="M80 70 Q80 44 96 44 Q110 44 108 60 Q106 70 96 70" fill="#B5652F" {s()}/>'
    f'<path d="M30 70 Q24 54 34 50 Q44 48 44 58" fill="none" stroke="#9C5A2A" stroke-width="7" stroke-linecap="round"/>'
    + f(52, 81, d=8, k=0.7)
    + f'<path d="M24 86 Q8 84 10 70 Q12 58 22 62 Q30 66 24 72 Q18 76 16 70" fill="none" stroke="#F3D29A" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M24 86 Q8 84 10 70 Q12 58 22 62 Q30 66 24 72 Q18 76 16 70" fill="none" {W(1.6)}/>')

I["podolsk-dubrovitsy"] = ("#EAF7FF", "#7FB8D8",
    "белокаменный храм-башенка с золотой ажурной короной", "стоит на мысу над слиянием двух рек и отражается в воде",
    f'<path d="M0 96 Q30 86 64 92 Q98 86 128 96 V128 H0Z" fill="#6FC3EA" {W(2.4)}/>'
    f'<path d="M64 92 L40 128 M64 92 L90 128" stroke="#9ADCF8" stroke-width="3"/>'
    f'<path d="M20 92 Q64 70 108 92Z" fill="{G}" {W(2.6)}/>'
    f'<rect x="44" y="50" width="40" height="34" rx="4" fill="#FFFBEF" {s()}/>'
    f'<rect x="52" y="28" width="24" height="24" rx="3" fill="#FFFBEF" {s()}/>'
    f'<path d="M50 28 L54 14 L58 24 L64 8 L70 24 L74 14 L78 28Z" fill="{GO}" {W(2.4)}/>'
    f'<circle cx="64" cy="6" r="3" fill="{GO}" {W(1.6)}/>'
    + "".join(f'<path d="M{x} 50 q4 -8 8 0" fill="none" stroke="#D9C9A0" stroke-width="2.4"/>' for x in (46, 56, 66, 76))
    + f(64, 66, d=8, k=0.7)
    + f'<path d="M58 84 V76 Q64 70 70 76 V84" fill="#C9B88E" {W(2)}/>')

I["podolsk-kpc-dubrovitsy"] = ("#FFF0F4", "#D98AA8",
    "свиток-афиша с деревянными ручками", "разворачивается сверху вниз, из него вылетают звёздочки и нотка",
    f'<rect x="30" y="20" width="68" height="78" fill="#FFF7E0" {s()}/>'
    f'<rect x="22" y="12" width="84" height="12" rx="6" fill="#A8683A" {s()}/>'
    f'<rect x="22" y="94" width="84" height="12" rx="6" fill="#A8683A" {s()}/>'
    f'<path d="M40 34 H88 M44 42 H84" stroke="{R}" stroke-width="4" stroke-linecap="round"/>'
    + f(64, 62, d=10, k=0.85)
    + f'<path d="M42 84 H86" stroke="#D9C9A0" stroke-width="3" stroke-linecap="round"/>'
    f'<path d="M14 54 L18 44 L22 54 L32 56 L22 60 L18 70 L14 60 L4 56Z" fill="{Y}" {W(1.8)}/>'
    f'<path d="M108 70 V48 L118 46 V66" fill="none" {W(2.6)}/><ellipse cx="104" cy="70" rx="5" ry="4" fill="{NV}"/>'
    f'<ellipse cx="114" cy="66" rx="5" ry="4" fill="{NV}"/>' + sp((112, 30, 6), (16, 90, 5)))

I["podolsk-dk-oktyabr"] = ("#F3ECFF", "#9B86D4",
    "серый волк в бабушкином кружевном чепце", "лежит в кровати из сказки про Красную Шапочку и выглядывает из-под одеяла",
    f'<rect x="10" y="54" width="10" height="70" rx="3" fill="#A8683A" {s()}/><rect x="108" y="64" width="10" height="60" rx="3" fill="#A8683A" {s()}/>'
    f'<circle cx="15" cy="52" r="6" fill="{GO}" {W(2)}/>'
    f'<path d="M30 54 Q22 30 34 26 L42 40Z M74 54 Q86 30 76 24 L66 38Z" fill="#8E93A6" {s()}/>'
    f'<ellipse cx="54" cy="64" rx="28" ry="24" fill="#9DA2B6" {s()}/>'
    f'<path d="M24 54 Q54 22 84 54 Q78 44 54 42 Q30 44 24 54Z" fill="#fff" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#fff" {W(1.4)}/>' for x, y in [(26, 54), (34, 44), (44, 38), (54, 36), (64, 38), (74, 44), (82, 54)])
    + f'<ellipse cx="66" cy="74" rx="14" ry="9" fill="#D6D9E6" {s()}/><ellipse cx="78" cy="71" rx="4" ry="3" fill="{NV}"/>'
    + eye(44, 62, 0.8) + eye(60, 60, 0.8)
    + f'<path d="M4 84 Q64 74 124 84 V128 H4Z" fill="{R}" {s()}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="10" height="10" fill="#fff" opacity=".55"/>' for x, y in [(20, 92), (44, 100), (68, 92), (92, 100), (32, 112), (80, 112)])
    + f'<path d="M30 84 Q34 76 40 82 M46 82 Q50 74 56 80" fill="#9DA2B6" {W(2.2)}/>')

I["podolsk-vystavochny-zal"] = ("#FFFBE6", "#EAC75E",
    "детский рисунок-каляка с солнышком и цветком", "висит на верёвочке на двух прищепках, как на выставке",
    f'<path d="M-4 22 Q64 40 132 22" fill="none" {W(2.6)}/>'
    f'<g transform="rotate(-4 64 72)"><rect x="22" y="32" width="84" height="76" fill="#fff" {s()}/>'
    f'<circle cx="46" cy="54" r="11" fill="{Y}" {W(2.2)}/>'
    + "".join(f'<path d="M{46+15*c} {54+15*sn} L{46+21*c} {54+21*sn}" stroke="{OR}" stroke-width="3" stroke-linecap="round"/>'
              for c, sn in [(1, 0), (0.7, 0.7), (0, 1), (-0.7, 0.7), (-1, 0), (-0.7, -0.7), (0, -1), (0.7, -0.7)])
    + eye(42, 52, 0.5) + eye(50, 52, 0.5)
    + f'<path d="M80 100 Q82 80 80 66" stroke="{DG}" stroke-width="3.4" fill="none"/>'
    + "".join(f'<ellipse cx="{80+9*c}" cy="{60+9*sn}" rx="6" ry="6" fill="{P}" {W(1.6)}/>' for c, sn in [(1, 0), (0, 1), (-1, 0), (0, -1)])
    + f'<circle cx="80" cy="60" r="5" fill="{OR}" {W(1.6)}/>'
    f'<path d="M30 100 Q50 92 70 100" stroke="{G}" stroke-width="4" fill="none" stroke-linecap="round"/></g>'
    f'<rect x="30" y="18" width="7" height="22" rx="2" fill="#7AC6F0" {W(2)}/><rect x="90" y="18" width="7" height="22" rx="2" fill="#7AC6F0" {W(2)}/>')

I["klimovsk-kraeved"] = ("#E8FBF4", "#59B79A",
    "ткацкий челнок-лодочка с катушкой внутри", "проносится сквозь натянутые нити основы и оставляет за собой полосатую ткань",
    "".join(f'<path d="M{x} 0 V128" stroke="#F4EBD8" stroke-width="3"/>' for x in range(8, 128, 10))
    + f'<rect x="0" y="86" width="128" height="42" fill="#F6E7C8" {W(2.2)}/>'
    + "".join(f'<rect x="0" y="{y}" width="128" height="5" fill="{c}"/>' for y, c in [(92, R), (102, "#5CB7F2"), (112, R), (122, "#5CB7F2")])
    + f'<path d="M8 60 Q40 42 64 44 H96 Q112 46 122 60 Q112 74 96 76 H64 Q40 78 8 60Z" fill="#D69A55" {s()}/>'
    f'<rect x="54" y="52" width="34" height="16" rx="6" fill="#8A5A3C" {W(2.2)}/>'
    f'<rect x="58" y="54" width="26" height="12" rx="4" fill="{R}"/>'
    + f(40, 60, d=7, k=0.6)
    + f'<path d="M122 60 Q124 76 100 88" fill="none" stroke="{R}" stroke-width="2.4"/>'
    f'<path d="M-2 66 h-0 M2 72 h14 M0 52 h12" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')

# ======================= Раменское =======================
I["ramenskoe-kdc-saturn"] = ("#FFF4E8", "#F0A35E",
    "вопросительный знак — ведущий викторины", "выпрыгивает из раскрытой книги сказок и тянет руку с ответом",
    f'<path d="M8 104 Q36 92 64 100 Q92 92 120 104 V118 Q92 108 64 116 Q36 108 8 118Z" fill="#fff" {s()}/>'
    f'<path d="M64 100 V116" {W(2)}/><path d="M18 106 Q40 100 56 104 M72 104 Q90 100 110 106" stroke="#C9CCD8" stroke-width="2" fill="none"/>'
    f'<path d="M42 40 Q42 14 64 14 Q88 14 88 36 Q88 50 72 58 Q66 62 66 74 V80" fill="none" stroke="{V}" stroke-width="16" stroke-linecap="round"/>'
    f'<path d="M42 40 Q42 14 64 14 Q88 14 88 36 Q88 50 72 58 Q66 62 66 74 V80" fill="none" {W(2)}/>'
    f'<circle cx="66" cy="94" r="8" fill="{V}" {s()}/>'
    + f(66, 34, d=7, k=0.6)
    + f'<path d="M86 48 L104 30" {W(3)}/><circle cx="106" cy="27" r="5" fill="#fff" {W(2)}/>'
    + sp((22, 30, 6), (110, 64, 5), (28, 74, 4)))

I["ramenskoe-dk-vorovskogo"] = ("#FFEFF0", "#E07C7C",
    "огромный клоунский башмак с жёлтыми шнурками", "шагает по красному манежу, шнурки болтаются",
    f'<ellipse cx="64" cy="108" rx="62" ry="22" fill="{R}" {s()}/><ellipse cx="64" cy="108" rx="48" ry="14" fill="#F6D18A" {W(2)}/>'
    f'<path d="M24 92 Q16 72 30 64 Q38 60 44 62 L52 40 H74 L80 64 Q110 62 116 80 Q120 96 98 98 H34 Q26 98 24 92Z" fill="#3F7BD6" {s()}/>'
    f'<path d="M24 92 H116" {W(2)}/><path d="M22 94 Q60 104 118 92" fill="none" stroke="#fff" stroke-width="4"/>'
    f'<rect x="50" y="34" width="26" height="10" rx="3" fill="#2B5BA8" {W(2.2)}/>'
    + f(92, 78, d=8, k=0.7)
    + f'<path d="M62 50 L70 56 M60 58 L72 62" stroke="{Y}" stroke-width="3" stroke-linecap="round"/>'
    f'<path d="M66 60 Q54 70 46 64 M66 60 Q72 74 62 80" fill="none" stroke="{Y}" stroke-width="3.4" stroke-linecap="round"/>'
    + sp((18, 34, 6), (108, 30, 7)))

# ======================= Химки =======================
I["khimki-tolstoy-park"] = ("#F0FFF0", "#5FA868",
    "машинка автодрома с длинной штангой-токосъёмником", "катится под высокими соснами, наверху на сетке проскакивает искорка",
    f'<path d="M0 18 H128" stroke="#8C8FA3" stroke-width="2"/><path d="M0 10 L128 26 M0 26 L128 10" stroke="#B8BCCB" stroke-width="1.4"/>'
    + "".join(f'<path d="M{x} 104 V60" stroke="#8A5A3C" stroke-width="5"/><path d="M{x-14} 70 L{x} 36 L{x+14} 70Z M{x-11} 56 L{x} 28 L{x+11} 56Z" fill="{DG}" {W(2)}/>' for x in (14, 114))
    + f'<rect x="0" y="104" width="128" height="24" fill="#9AA0B4" {W(2.2)}/>'
    f'<path d="M64 74 L80 20" {W(3.4)}/><path d="M76 20 L84 20" {W(3)}/>'
    + sparkle(82, 16, 7, Y)
    + f'<path d="M30 104 Q28 84 40 78 H90 Q102 80 100 104Z" fill="{OR}" {s()}/>'
    f'<path d="M24 98 H106" stroke="{NV}" stroke-width="8" stroke-linecap="round"/>'
    + f(64, 90, d=9, k=0.7))

I["khimki-dk-rodina"] = ("#FFF6E8", "#D99D5A",
    "русская печь на колёсах с трубой", "сама едет по снежной дороге, из трубы валит дымок колечками",
    f'<path d="M0 106 Q64 98 128 106 V128 H0Z" fill="#fff" {W(2.4)}/>'
    f'<path d="M22 100 V56 Q22 46 32 46 H92 Q102 46 102 56 V100Z" fill="#FFF5E8" {s()}/>'
    f'<path d="M86 46 V22 H100 V46" fill="#FFF5E8" {s()}/>'
    f'<path d="M44 100 V82 Q44 70 58 70 Q72 70 72 82 V100Z" fill="{NV}" {W(2.4)}/>'
    f'<path d="M50 100 Q52 90 58 92 Q62 86 66 100Z" fill="{OR}"/>'
    + f(62, 58, d=10, k=0.75)
    + "".join(f'<circle cx="{x}" cy="106" r="9" fill="#A8683A" {s()}/><circle cx="{x}" cy="106" r="3" fill="{NV}"/>' for x in (34, 92))
    + f'<circle cx="96" cy="12" r="5" fill="none" stroke="#fff" stroke-width="3"/><circle cx="108" cy="6" r="4" fill="none" stroke="#fff" stroke-width="3"/>'
    f'<path d="M6 92 h10 M2 82 h12" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')

I["khimki-ekobereg"] = ("#E6FBFF", "#3E9CC4",
    "водомерка на длинных тонких ножках", "скользит по глади канала, от лапок расходятся круги",
    f'<path d="M0 70 H128 V128 H0Z" fill="#5CB7E2" opacity=".55"/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="14" ry="4" fill="none" stroke="#fff" stroke-width="2"/>' for x, y in [(18, 96), (110, 96), (30, 66), (98, 66)])
    + f'<path d="M50 70 Q34 60 30 66 M50 78 Q30 84 18 96 M78 70 Q94 60 98 66 M78 78 Q98 84 110 96" fill="none" stroke="{NV}" stroke-width="3.2" stroke-linecap="round"/>'
    f'<path d="M56 64 Q50 48 34 40 M72 64 Q78 48 94 40" fill="none" stroke="{NV}" stroke-width="2.6" stroke-linecap="round"/>'
    f'<ellipse cx="64" cy="80" rx="12" ry="26" fill="#6B5B3E" {s()}/><circle cx="64" cy="54" r="11" fill="#7E6A48" {s()}/>'
    + eye(59, 53, 0.7) + eye(69, 53, 0.7)
    + f'<path d="M60 60 Q64 63 68 60" fill="none" {W(2)}/>'
    f'<path d="M0 30 Q20 20 40 28" stroke="{DG}" stroke-width="4" fill="none"/><path d="M110 4 L114 34 M120 8 L118 34" stroke="{DG}" stroke-width="4"/>')

I["khimki-podrezkovo-park"] = ("#F2F9E8", "#86B85A",
    "деревянный сруб родника с медной трубкой", "из трубки бежит струйка в подставленный деревянный ковшик",
    f'<path d="M0 100 Q64 90 128 100 V128 H0Z" fill="{G}" {W(2.4)}/>'
    + "".join(f'<rect x="18" y="{y}" width="72" height="12" rx="6" fill="#C98D52" {W(2.2)}/><circle cx="24" cy="{y+6}" r="4" fill="#E8C48A" {W(1.4)}/><circle cx="84" cy="{y+6}" r="4" fill="#E8C48A" {W(1.4)}/>' for y in (60, 73, 86))
    + f'<ellipse cx="54" cy="60" rx="34" ry="6" fill="#7FD3F7" {W(2)}/>'
    + f(54, 82, d=10, k=0.8)
    + f'<rect x="86" y="70" width="18" height="7" rx="3" fill="#D98A3C" {W(2)}/>'
    f'<path d="M104 76 Q108 84 104 92" stroke="#7FD3F7" stroke-width="5" fill="none" stroke-linecap="round"/>'
    f'<path d="M90 92 H118 Q116 108 104 108 Q92 108 90 92Z" fill="#B5652F" {s()}/><path d="M118 94 L126 88" {W(4)}/>'
    + "".join(sparkle(x, y, 4, "#BFEFFF") for x, y in [(110, 76), (96, 82)]))

I["khimki-dubki-la7"] = ("#EAF3FF", "#7E9BD8",
    "истребитель Ла-7 с красной звездой и пропеллером", "стоит на постаменте у входа в парк между двумя молодыми дубками",
    f'<path d="M0 108 Q64 100 128 108 V128 H0Z" fill="{G}" {W(2.4)}/>'
    + "".join(f'<path d="M{x} 108 V80" stroke="#8A5A3C" stroke-width="4"/><circle cx="{x}" cy="72" r="13" fill="{DG}" {s()}/>' for x in (14, 114))
    + f'<rect x="44" y="84" width="40" height="24" fill="#C9CCD8" {s()}/><path d="M54 108 V84 M74 108 V84" stroke="#A3A7B8" stroke-width="2"/>'
    f'<path d="M20 58 Q24 46 44 46 H96 Q108 48 110 58 Q104 66 92 66 H34 Q22 66 20 58Z" fill="#7A9A6A" {s()}/>'
    f'<path d="M40 56 L28 36 H40 L56 56Z" fill="#5E7E50" {W(2.4)}/>'
    f'<path d="M58 60 L52 82 H70 L76 60Z" fill="#5E7E50" {W(2.4)}/>'
    f'<path d="M66 44 Q72 34 84 36 L88 46" fill="#BFE6FF" {W(2.2)}/>'
    f'<path d="M110 58 h6" {W(3)}/><ellipse cx="118" cy="58" rx="3" ry="16" fill="{GR}" {W(2)}/>'
    f'<path d="M30 52 l2 4 h4 l-3 3 l1 4 l-4 -2 l-4 2 l1 -4 l-3 -3 h4Z" fill="{R}"/>'
    + f(84, 56, d=6, k=0.55) + f'<path d="M64 84 V66" {W(3)}/>')

# ======================= Мытищи =======================
I["mytishchi-gallery"] = ("#F4F1EA", "#B7A88C",
    "мраморный бюст в бархатном берете", "стоит на подставке и косится на соседнюю картину с котом",
    f'<rect x="0" y="0" width="128" height="128" fill="#E9DFC9" opacity=".4"/>'
    f'<rect x="72" y="22" width="44" height="40" fill="#fff" stroke="{GO}" stroke-width="6"/>'
    f'<rect x="72" y="22" width="44" height="40" fill="none" {W(1.6)}/>'
    f'<path d="M82 56 Q82 40 94 40 Q106 40 106 56Z" fill="{OR}" {W(1.6)}/><path d="M86 42 L84 34 L90 40 M102 42 L104 34 L98 40" fill="{OR}" {W(1.6)}/>'
    f'<rect x="30" y="96" width="44" height="32" fill="#C9CCD8" {s()}/><rect x="24" y="90" width="56" height="8" fill="#E1E3EC" {s()}/>'
    f'<path d="M30 90 Q30 70 52 70 Q74 70 74 90Z" fill="#F2F2F5" {s()}/>'
    f'<ellipse cx="52" cy="54" rx="18" ry="21" fill="#F2F2F5" {s()}/>'
    f'<path d="M30 42 Q34 26 56 28 Q76 30 70 42 Q52 36 30 42Z" fill="{V}" {s()}/><circle cx="54" cy="27" r="3" fill="{V}" {W(1.6)}/>'
    + eye(52, 54, 0.7) + eye(62, 54, 0.7)
    + f'<path d="M50 66 Q55 63 60 66" fill="none" {W(2)}/><path d="M56 56 Q58 60 55 62" fill="none" {W(1.6)}/>')

# ======================= Балашиха =======================
I["balashikha-kraeved"] = ("#3D3560", "#1F1B33",
    "горящая лучина в кованом светце", "освещает тёмную избу, рядом угольки падают в корытце с водой",
    f'<circle cx="74" cy="34" r="34" fill="{Y}" opacity=".18"/><circle cx="74" cy="34" r="20" fill="{Y}" opacity=".22"/>'
    f'<rect x="60" y="50" width="8" height="66" fill="#6E6E82" {s()}/>'
    f'<path d="M44 116 H84" stroke="#6E6E82" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M64 50 L52 44 M64 50 L76 44" {W(3)}/><path d="M64 50 L52 44 M64 50 L76 44" stroke="#8E8EA6" stroke-width="2"/>'
    f'<path d="M50 46 L92 28" stroke="#E8C48A" stroke-width="6" stroke-linecap="round"/><path d="M50 46 L92 28" fill="none" {W(1.6)}/>'
    f'<path d="M88 30 Q86 14 96 4 Q96 16 104 18 Q104 30 94 32Z" fill="{OR}" {W(2.2)}/><path d="M92 28 Q92 20 96 14 Q100 22 98 28Z" fill="{Y}"/>'
    + f(64, 82, d=7, k=0.6).replace('fill="#3B3355"', 'fill="#fff"', 2)
    + f'<path d="M78 112 Q76 96 92 96 H118 Q120 112 112 116Z" fill="#8A5A3C" {s()}/><path d="M84 100 H114" stroke="#7FD3F7" stroke-width="4"/>'
    f'<circle cx="98" cy="54" r="2.4" fill="{OR}"/><circle cx="100" cy="72" r="2" fill="{OR}"/>'
    + sp((20, 30, 3), (30, 100, 2.4)))

I["balashikha-pekhra"] = ("#FFF8EC", "#C9A879",
    "каменный лев с кудрявой гривой", "лежит у ступеней усадьбы, положив лапу на каменный шар",
    "".join(f'<rect x="{-6+8*i}" y="{100+8*i}" width="{140-16*i}" height="10" fill="#E6DED0" {W(2)}/>' for i in range(3))
    + f'<rect x="4" y="18" width="14" height="82" fill="#FFFDF7" {W(2.2)}/><rect x="110" y="18" width="14" height="82" fill="#FFFDF7" {W(2.2)}/>'
    f'<ellipse cx="68" cy="88" rx="38" ry="14" fill="#D7D2C6" {s()}/>'
    f'<path d="M96 84 Q112 70 104 60" fill="none" stroke="#D7D2C6" stroke-width="5" stroke-linecap="round"/><circle cx="104" cy="58" r="5" fill="#BDB5A4" {W(1.6)}/>'
    + "".join(f'<circle cx="{44+15*c:.1f}" cy="{58+15*sn:.1f}" r="10" fill="#B3A68C" {W(1.8)}/>'
              for c, sn in [(1, 0), (0.7, 0.7), (0, 1), (-0.7, 0.7), (-1, 0), (-0.7, -0.7), (0, -1), (0.7, -0.7)])
    + f'<circle cx="44" cy="58" r="15" fill="#E3DED2" {s()}/>' + f(44, 56, d=6, k=0.55)
    + f'<path d="M40 64 L48 64 L44 68Z" fill="{NV}"/><path d="M28 46 L24 38 L34 42Z M60 46 L64 38 L54 42Z" fill="#B3A68C" {W(1.6)}/>'
    + f'<path d="M100 88 Q122 82 116 66" fill="none" stroke="#D7D2C6" stroke-width="4"/><circle cx="116" cy="64" r="5" fill="#B3A68C" {W(1.6)}/>'
    + f'<circle cx="24" cy="94" r="10" fill="#C9C2B2" {s()}/><ellipse cx="32" cy="88" rx="9" ry="5" fill="#E3DED2" {W(2)}/>')

I["balashikha-naive-gallery"] = ("#FFF7D9", "#9FCB6A",
    "кисточка в соломенной шляпке", "рисует на деревянном заборе наивный розовый цветок",
    "".join(f'<path d="M{x} 128 V40 L{x+9} 32 L{x+18} 40 V128Z" fill="#E8C48A" {W(2)}/>' for x in range(-4, 70, 18))
    + f'<path d="M30 112 Q32 88 32 76" stroke="{DG}" stroke-width="3.6" fill="none"/><path d="M32 96 Q20 92 18 84 Q28 84 32 94" fill="{G}" {W(1.6)}/>'
    + "".join(f'<circle cx="{32+10*c:.1f}" cy="{66+10*sn:.1f}" r="7" fill="{P}" {W(1.8)}/>' for c, sn in [(1, 0), (0.3, 0.95), (-0.8, 0.6), (-0.8, -0.6), (0.3, -0.95)])
    + f'<circle cx="32" cy="66" r="6" fill="{Y}" {W(1.8)}/>'
    f'<g transform="rotate(-30 92 70)"><rect x="86" y="54" width="12" height="64" rx="5" fill="{R}" {s()}/>'
    f'<rect x="85" y="44" width="14" height="12" fill="{GR}" {W(2.2)}/><path d="M85 44 Q86 26 92 18 Q98 26 99 44Z" fill="{P}" {s()}/></g>'
    f'<ellipse cx="100" cy="66" rx="20" ry="6" fill="#F4D27A" {s()}/><path d="M90 66 Q90 52 100 52 Q110 52 110 66Z" fill="#F4D27A" {s()}/>'
    f'<path d="M90 62 H110" stroke="{R}" stroke-width="3"/>' + f(102, 78, d=6, k=0.55))

I["balashikha-kartinka"] = ("#E9F3FF", "#6E8FE0",
    "книжка-раскладушка с картонными страницами", "из разворота встаёт бумажный замок с флажком и облачком",
    f'<path d="M8 100 L64 112 L120 100 L120 112 L64 124 L8 112Z" fill="#fff" {s()}/>'
    f'<path d="M8 100 L64 88 L120 100 L64 112Z" fill="#FFF3D6" {s()}/><path d="M64 88 V112" {W(2)}/>'
    f'<path d="M36 94 V56 H46 V48 H54 V56 H74 V48 H82 V56 H92 V94" fill="#FFB27A" {s()}/>'
    f'<path d="M58 30 V56" {W(2.4)}/><path d="M58 30 L74 36 L58 42Z" fill="{R}" {W(2)}/>'
    f'<path d="M58 94 V82 Q64 74 70 82 V94" fill="#8A5A3C" {W(2)}/>'
    + f(64, 68, d=10, k=0.7)
    + f'<path d="M92 36 Q92 26 102 28 Q106 20 114 26 Q122 26 120 36Z" fill="#fff" {W(2)}/>'
    f'<path d="M36 94 L28 98 M92 94 L100 98" {W(2)}/>')

I["balashikha-pekhorka-park"] = ("#E8FFF3", "#4FB38A",
    "круглые качели-гнездо из канатной сетки", "раскачиваются на верёвках над травой у реки Пехорки",
    f'<path d="M0 104 Q64 96 128 104 V128 H0Z" fill="{G}" {W(2.4)}/>'
    f'<path d="M0 112 Q30 106 60 112 T128 110 V128 H0Z" fill="#7FD3F7" {W(2)}/>'
    f'<path d="M8 6 L120 6" stroke="#8A5A3C" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M36 8 L22 70 M92 8 L106 70 M50 8 L44 64 M78 8 L84 64" {W(2.4)}/>'
    f'<g transform="rotate(-10 64 72)"><ellipse cx="64" cy="74" rx="46" ry="16" fill="{OR}" {s()}/>'
    f'<ellipse cx="64" cy="72" rx="36" ry="10" fill="#FFD9A8" {W(2)}/>'
    + "".join(f'<path d="M{x} 64 L{x+10} 82 M{x+10} 64 L{x} 82" stroke="{OR}" stroke-width="2"/>' for x in range(32, 96, 12))
    + "</g>" + f(64, 76, d=12, k=0.8) + sp((18, 30, 6), (110, 28, 5)))

# ======================= Королёв =======================
I["korolev-tsvetaeva"] = ("#F7EDE4", "#B88C72",
    "тетрадь стихов с атласной ленточкой-закладкой", "лежит на дачной скамейке под соснами, страницы шелестят на ветру",
    "".join(f'<path d="M{x} 0 V70" stroke="#8A5A3C" stroke-width="6"/><circle cx="{x}" cy="10" r="20" fill="{DG}" {W(2)}/>' for x in (10, 118))
    + f'<rect x="10" y="88" width="108" height="10" rx="3" fill="#A8683A" {s()}/><path d="M22 98 V122 M106 98 V122" {W(6)}/>'
    f'<path d="M22 98 V122 M106 98 V122" stroke="#A8683A" stroke-width="3"/>'
    f'<path d="M30 86 L64 76 L98 86 L64 92Z" fill="#fff" {s()}/>'
    f'<path d="M64 76 Q52 52 32 44 L30 86" fill="#FFFBEF" {s()}/><path d="M64 76 Q76 48 98 40 L98 86" fill="#FFFBEF" {s()}/>'
    + "".join(f'<path d="M{a} {y} Q{(a+b)/2} {y-4} {b} {y-6}" stroke="#9AA3C2" stroke-width="2" fill="none"/>' for a, b, y in [(72, 92, 64), (72, 92, 72), (70, 90, 80)])
    + f(48, 66, d=6, k=0.55)
    + f'<path d="M64 80 Q60 100 52 108 M64 80 Q70 100 76 104" stroke="{R}" stroke-width="3.4" fill="none" stroke-linecap="round"/>'
    f'<path d="M108 30 Q116 26 120 32 M100 52 Q108 48 112 54" stroke="#fff" stroke-width="2.4" fill="none"/>')

I["korolev-papaninskaya-dacha"] = ("#F2FAFF", "#86BCE6",
    "полярная палатка с флагом и ветряком", "стоит на льдине посреди детского городка, рядом лопатка и снежок",
    f'<path d="M0 96 Q64 88 128 96 V128 H0Z" fill="#5CA8DA" {W(2.2)}/>'
    f'<path d="M6 98 L18 82 H112 L122 98 L104 108 H22Z" fill="#fff" {s()}/>'
    f'<path d="M30 88 Q64 20 98 88Z" fill="{OR}" {s()}/><path d="M64 34 V88" {W(2)}/>'
    f'<path d="M52 88 Q64 64 76 88Z" fill="{NV}" {W(2)}/>'
    + f(64, 56, d=8, k=0.65)
    + f'<path d="M64 34 V10" {W(2.4)}/><path d="M64 10 L84 14 L64 20Z" fill="{R}" {W(2)}/>'
    f'<path d="M104 86 V54" {W(2.4)}/>'
    + "".join(f'<path d="M104 54 L{104+12*c:.0f} {54+12*sn:.0f}" stroke="#fff" stroke-width="5" stroke-linecap="round"/>' for c, sn in [(1, -0.2), (-0.4, -1), (-0.6, 0.9)])
    + f'<circle cx="104" cy="54" r="3" fill="{NV}"/><circle cx="20" cy="88" r="6" fill="#fff" {W(2)}/>')

# ======================= Видное =======================
I["vidnoe-timokhovo"] = ("#FFFDF0", "#D7C46A",
    "садовая лейка с длинным носиком", "поливает круглую клумбу перед белым усадебным домом с колоннами",
    f'<rect x="10" y="30" width="108" height="40" fill="#FFF5E8" {W(2.2)}/><path d="M4 32 L64 12 L124 32Z" fill="#E8C48A" {W(2.2)}/>'
    + "".join(f'<rect x="{x}" y="36" width="6" height="34" fill="#fff" {W(1.6)}/>' for x in (30, 46, 76, 92))
    + f'<path d="M0 84 Q64 74 128 84 V128 H0Z" fill="{G}" {W(2.4)}/>'
    f'<ellipse cx="38" cy="106" rx="28" ry="10" fill="#8A5A3C" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="{c}" {W(1.6)}/>' for x, y, c in [(22, 100, R), (34, 96, Y), (46, 98, P), (56, 104, R), (30, 106, V)])
    + f'<path d="M72 74 Q70 104 84 108 H108 Q118 104 114 74Z" fill="#5CB7F2" {s()}/>'
    f'<path d="M80 74 Q92 56 108 74" fill="none" {W(3.4)}/>'
    f'<path d="M74 86 L44 66" stroke="#5CB7F2" stroke-width="7" stroke-linecap="round"/><path d="M74 86 L44 66" fill="none" {W(1.8)}/>'
    + f(94, 90, d=8, k=0.65)
    + "".join(f'<path d="M{x} {y} q-2 6 0 8" stroke="#7FD3F7" stroke-width="2.6" fill="none"/>' for x, y in [(40, 70), (34, 76), (46, 76)]))

I["vidnoe-rastorguevsky-park"] = ("#F0FFE8", "#77C46B",
    "летающая тарелка-фрисби", "несётся над поляной, за ней в прыжке тянется рыжий щенок",
    f'<path d="M0 100 Q64 90 128 100 V128 H0Z" fill="{G}" {W(2.4)}/>'
    f'<ellipse cx="80" cy="40" rx="34" ry="12" fill="#FF6FA0" {s()}/><ellipse cx="80" cy="37" rx="22" ry="6" fill="#FF9EC0"/>'
    + f(80, 40, d=8, k=0.6)
    + f'<path d="M30 30 h12 M26 42 h14 M32 54 h10" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    f'<ellipse cx="44" cy="88" rx="22" ry="11" fill="{OR}" {s()}/><circle cx="62" cy="72" r="12" fill="{OR}" {s()}/>'
    f'<path d="M54 64 Q48 56 52 50 L60 62Z" fill="#C86A2A" {W(1.8)}/>'
    + eye(64, 70, 0.55) + f'<circle cx="73" cy="74" r="2.6" fill="{NV}"/>'
    f'<path d="M28 92 L18 104 M58 94 L66 106 M24 84 Q12 80 10 72" fill="none" stroke="{OR}" stroke-width="5" stroke-linecap="round"/>')

I["vidnoe-zemlyanichny-gorod"] = ("#FFF2F2", "#E58A8A",
    "огородное пугало в соломенной шляпе", "машет рукавами над грядками с земляникой, отгоняя воробья",
    f'<path d="M0 98 Q64 88 128 98 V128 H0Z" fill="#9C6B3E" {W(2.4)}/>'
    + "".join(f'<path d="M{x} 104 q6 -8 12 0" fill="{G}" {W(1.6)}/><path d="M{x+6} 110 l-4 -4 h8z" fill="{R}" {W(1.4)}/>' for x in (6, 30, 84, 108))
    + f'<path d="M64 128 V40" stroke="#8A5A3C" stroke-width="6"/><path d="M14 58 H114" stroke="#8A5A3C" stroke-width="5"/>'
    f'<path d="M40 52 H88 L84 96 H44Z" fill="#5CB7F2" {s()}/><rect x="54" y="70" width="12" height="12" fill="{Y}" {W(1.6)}/>'
    f'<path d="M40 52 L14 50 L12 68 L40 64Z M88 52 L114 50 L116 68 L88 64Z" fill="#5CB7F2" {s()}/>'
    + "".join(f'<path d="M{x} {y} l-6 4 M{x} {y} l-4 8" stroke="#E8C48A" stroke-width="2.6"/>' for x, y in [(12, 62)])
    + f'<path d="M116 60 l6 4 M116 60 l4 8" stroke="#E8C48A" stroke-width="2.6"/>'
    f'<circle cx="64" cy="36" r="16" fill="#F4E2B8" {s()}/>' + f(64, 37, d=6, k=0.55)
    + f'<ellipse cx="64" cy="22" rx="28" ry="6" fill="#E8C48A" {s()}/><path d="M50 22 Q52 6 64 6 Q76 6 78 22Z" fill="#E8C48A" {s()}/>'
    f'<ellipse cx="104" cy="28" rx="8" ry="6" fill="#A8683A" {W(1.8)}/><path d="M110 26 l5 -1 l-4 4" fill="{Y}"/>')

I["vidnoe-dk"] = ("#F8EDFF", "#B27CD8",
    "две ладошки, хлопающие в аплодисментах", "аплодируют перед сценой, вокруг разлетаются звёздочки",
    f'<path d="M0 110 H128 V128 H0Z" fill="#D9A066" {W(2.2)}/>'
    f'<g transform="rotate(-22 50 80)"><rect x="30" y="40" width="36" height="58" rx="18" fill="#FFD3B0" {s()}/>'
    f'<path d="M30 70 Q18 62 20 52 Q28 50 32 60" fill="#FFD3B0" {s()}/><path d="M38 48 V58 M48 44 V56 M58 48 V58" stroke="#E0A882" stroke-width="2.4" stroke-linecap="round"/>'
    f'<rect x="30" y="94" width="36" height="14" rx="4" fill="{V}" {s()}/></g>'
    f'<g transform="rotate(22 78 80)"><rect x="62" y="40" width="36" height="58" rx="18" fill="#FFC79C" {s()}/>'
    f'<path d="M98 70 Q110 62 108 52 Q100 50 96 60" fill="#FFC79C" {s()}/><path d="M70 48 V58 M80 44 V56 M90 48 V58" stroke="#E09A70" stroke-width="2.4" stroke-linecap="round"/>'
    f'<rect x="62" y="94" width="36" height="14" rx="4" fill="{V}" {s()}/></g>'
    + f(64, 76, d=8, k=0.7)
    + f'<path d="M64 26 V12 M48 30 L40 18 M80 30 L88 18" stroke="{Y}" stroke-width="4.4" stroke-linecap="round"/>'
    + sp((16, 34, 7), (112, 40, 8), (14, 80, 5), (116, 84, 5)))

# ======================= Красногорск =======================
I["krasnogorsk-skazochny"] = ("#E8FFF6", "#4FAF8F",
    "Баба-Яга в деревянной ступе с метлой", "летит над горками детского городка, платок развевается",
    f'<path d="M0 104 Q64 96 128 104 V128 H0Z" fill="{G}" {W(2.4)}/>'
    f'<path d="M86 104 L104 72 H112 V104" fill="{Y}" {W(2.2)}/><path d="M96 104 Q100 88 112 84" fill="none" stroke="{R}" stroke-width="6"/>'
    f'<path d="M24 46 L36 84 Q48 90 60 84 L72 46Z" fill="#A8683A" {s()}/><path d="M28 58 H68 M32 70 H64" stroke="#7A4A26" stroke-width="2.4"/>'
    f'<circle cx="48" cy="36" r="13" fill="#FFD9B8" {s()}/>' + f(48, 37, d=5, k=0.5)
    + f'<path d="M34 34 Q34 18 50 18 Q64 20 62 36 Q56 26 34 34Z" fill="{R}" {s()}/>'
    f'<path d="M62 30 Q78 26 86 34 Q74 32 66 38Z" fill="{R}" {W(2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="#fff"/>' for x, y in [(42, 24), (52, 22), (58, 30)])
    + f'<path d="M58 44 L100 20" stroke="#8A5A3C" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M98 22 L120 8 M100 20 L122 16 M98 18 L116 2" stroke="#E8C48A" stroke-width="3" stroke-linecap="round"/>'
    f'<path d="M14 92 q6 -4 12 0 M8 82 q6 -4 12 0" stroke="#fff" stroke-width="3" fill="none"/>')

I["krasnogorsk-znamenskoe-gubaylovo"] = ("#FFF7EE", "#C6A07E",
    "парковая каменная ваза-урна на ножке", "стоит на балюстраде усадьбы, из неё свисают розовые петунии",
    f'<rect x="0" y="92" width="128" height="10" fill="#EFE7DA" {s()}/>'
    + "".join(f'<path d="M{x} 102 Q{x-6} 110 {x} 118 Q{x+6} 110 {x} 102Z" fill="#E6DED0" {W(1.8)}/>' for x in range(8, 128, 16))
    + f'<rect x="0" y="118" width="128" height="10" fill="#EFE7DA" {W(2)}/>'
    f'<rect x="46" y="80" width="36" height="12" rx="2" fill="#D7D2C6" {s()}/><path d="M56 80 Q58 72 64 70 Q70 72 72 80Z" fill="#D7D2C6" {W(2.2)}/>'
    f'<path d="M30 40 H98 Q98 70 64 72 Q30 70 30 40Z" fill="#E3DED2" {s()}/>'
    f'<rect x="26" y="34" width="76" height="8" rx="3" fill="#D7D2C6" {s()}/>'
    + f(64, 54, d=10, k=0.8)
    + "".join(f'<circle cx="{x}" cy="{y}" r="7" fill="{c}" {W(1.6)}/>' for x, y, c in [(36, 28, P), (52, 22, "#FF6FA0"), (70, 22, P), (88, 28, "#FF6FA0")])
    + f'<path d="M30 42 Q20 56 22 70 M98 42 Q108 56 106 70" stroke="{DG}" stroke-width="3.4" fill="none"/>'
    f'<circle cx="22" cy="72" r="6" fill="{P}" {W(1.6)}/><circle cx="106" cy="72" r="6" fill="#FF6FA0" {W(1.6)}/>')

I["krasnogorsk-dk-podmoskovye"] = ("#EEFFF0", "#2FA86A",
    "Железный Дровосек с воронкой на голове", "смазывает из маслёнки свой скрипучий локоть на изумрудной дорожке",
    f'<path d="M0 112 L44 92 H84 L128 112 V128 H0Z" fill="#3FC47A" {W(2.2)}/>'
    + "".join(f'<path d="M{x} 100 h14" stroke="#2A9A5A" stroke-width="2"/>' for x in (44, 70))
    + f'<rect x="46" y="62" width="36" height="38" rx="8" fill="#C9CCD8" {s()}/>'
    f'<path d="M52 100 V118 M76 100 V118" stroke="#AEB2C2" stroke-width="10" stroke-linecap="round"/><path d="M52 100 V118 M76 100 V118" fill="none" {W(1.6)}/>'
    f'<rect x="50" y="30" width="28" height="30" rx="6" fill="#DADDE8" {s()}/>' + f(64, 44, d=6, k=0.55)
    + f'<path d="M50 30 L64 6 L78 30Z" fill="#AEB2C2" {s()}/><path d="M62 10 h4" {W(2)}/>'
    f'<path d="M82 70 L98 80 L92 96" fill="none" stroke="#C9CCD8" stroke-width="9" stroke-linecap="round"/><path d="M82 70 L98 80 L92 96" fill="none" {W(1.6)}/>'
    f'<path d="M46 70 L28 82" stroke="#C9CCD8" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M14 90 Q12 76 22 76 H30 Q34 82 30 90Z" fill="{GO}" {s()}/><path d="M28 78 L48 70" {W(3)}/>'
    f'<path d="M50 70 q2 4 0 6" stroke="#8A5A3C" stroke-width="2.4" fill="none"/>'
    f'<circle cx="64" cy="76" r="5" fill="{R}" {W(1.6)}/>' + sp((106, 30, 6), (20, 30, 5)))

I["krasnogorsk-ivanovskie-prudy"] = ("#EAFBFF", "#4AA6B8",
    "головастик с хвостиком-завитком", "плывёт по пруду среди кувшинок и пускает цепочку пузырьков",
    f'<rect x="0" y="0" width="128" height="128" fill="#7FD3F7" opacity=".25"/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="14" ry="6" fill="{G}" {W(2)}/><path d="M{x} {y} l10 -4" {W(1.6)}/>' for x, y in [(22, 30), (108, 96), (20, 106)])
    + f'<circle cx="108" cy="92" r="4" fill="#fff" {W(1.4)}/>'
    f'<path d="M80 66 Q104 54 110 66 Q116 80 98 76 Q90 74 96 68" fill="none" stroke="#3A4A6E" stroke-width="9" stroke-linecap="round"/>'
    f'<ellipse cx="58" cy="64" rx="28" ry="24" fill="#4A5A80" {s()}/>'
    + f(54, 62, d=9, k=0.75).replace('fill="#3B3355"', 'fill="#fff"', 2)
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="#fff" stroke-width="2.2"/>' for x, y, r in [(40, 32, 4), (48, 20, 5.5), (40, 8, 3.5)]))

I["krasnogorsk-pavshinskaya-poyma"] = ("#FFF9E6", "#E2B24C",
    "двухместный велосипед-тандем", "мчится по набережной Москвы-реки, два седока крутят педали в одном ритме",
    f'<path d="M0 90 Q64 84 128 90 V128 H0Z" fill="#6FC3EA" {W(2.2)}/><path d="M0 98 H128" stroke="#C9CCD8" stroke-width="7"/>'
    + "".join(f'<circle cx="{x}" cy="78" r="17" fill="none" {W(3.4)}/><circle cx="{x}" cy="78" r="3" fill="{NV}"/>' + "".join(f'<path d="M{x} 78 l{dx} {dy}" stroke="#9AA0B4" stroke-width="1.4"/>' for dx, dy in [(17,0),(0,17),(-17,0),(0,-17),(12,12),(-12,12),(12,-12),(-12,-12)]) for x in (22, 106))
    + f'<path d="M22 78 L44 54 H86 L106 78 M44 54 L58 78 L86 54 M58 78 L72 54" fill="none" stroke="{R}" stroke-width="5" stroke-linejoin="round"/>'
    f'<path d="M86 54 L92 40 H102" fill="none" {W(3.4)}/><path d="M40 48 H52 M66 48 H78" {W(4)}/>'
    f'<circle cx="46" cy="28" r="11" fill="{SK}" {s()}/>' + f(46, 29, d=4.4, k=0.42)
    + f'<path d="M35 26 Q36 14 46 15 Q56 14 57 26Z" fill="{Y}" {W(2)}/>'
    f'<circle cx="74" cy="28" r="11" fill="{SK}" {s()}/>' + f(74, 29, d=4.4, k=0.42)
    + f'<path d="M63 26 Q64 14 74 15 Q84 14 85 26Z" fill="#5CB7F2" {W(2)}/>'
    f'<path d="M46 40 V48 M74 40 V48 M46 40 L60 44 L88 42" stroke="{SK}" stroke-width="5" stroke-linecap="round" fill="none"/>'
    f'<path d="M4 50 h10 M0 62 h8" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')

# ======================= Реутов =======================
I["reutov-fabrichny-prud"] = ("#EFF6FF", "#6A8FB8",
    "ондатра с блестящей мокрой шёрсткой", "плывёт по фабричному пруду, держа в зубах стебель камыша",
    f'<path d="M0 72 Q64 64 128 72 V128 H0Z" fill="#5C9FD0" {W(2.2)}/>'
    + "".join(f'<path d="M{x} {y} q8 -4 16 0" stroke="#fff" stroke-width="2.4" fill="none"/>' for x, y in [(10, 90), (90, 100), (20, 112), (100, 82)])
    + "".join(f'<path d="M{x} 72 V{t}" stroke="{DG}" stroke-width="3"/><rect x="{x-3}" y="{t}" width="6" height="16" rx="3" fill="#8A5A3C" {W(1.4)}/>' for x, t in [(110, 24), (118, 34)])
    + f'<path d="M14 84 Q2 80 6 72" stroke="#6E4B2E" stroke-width="5" fill="none" stroke-linecap="round"/>'
    f'<path d="M18 84 Q30 64 62 66 Q86 66 94 80 Q76 90 40 88Z" fill="#8A5E3A" {s()}/>'
    f'<circle cx="84" cy="66" r="14" fill="#9A6B44" {s()}/><circle cx="76" cy="54" r="3.4" fill="#8A5E3A" {W(1.4)}/>'
    + eye(86, 63, 0.6) + f'<circle cx="97" cy="68" r="2.4" fill="{NV}"/>'
    f'<path d="M92 72 L60 40" stroke="{DG}" stroke-width="3"/><rect x="54" y="28" width="7" height="16" rx="3" fill="#8A5A3C" {W(1.4)}/>'
    f'<ellipse cx="78" cy="72" rx="3.6" ry="2.2" fill="#FF7FA8" opacity=".7"/>')

I["reutov-central-park"] = ("#FFF4EA", "#E59160",
    "полосатый шлагбаум автогородка", "поднимается и пропускает маленькую педальную машинку с флажком",
    f'<rect x="0" y="92" width="128" height="36" fill="#7E8296" {W(2.2)}/>'
    + "".join(f'<rect x="{x}" y="108" width="14" height="4" fill="#fff"/>' for x in range(0, 128, 24))
    + f'<rect x="12" y="54" width="18" height="44" rx="4" fill="{GR}" {s()}/>'
    f'<g transform="rotate(-32 22 60)"><rect x="18" y="54" width="100" height="12" rx="6" fill="#fff" {s()}/>'
    + "".join(f'<rect x="{x}" y="54" width="12" height="12" fill="{R}"/>' for x in (34, 58, 82, 106))
    + f'<rect x="18" y="54" width="100" height="12" rx="6" fill="none" {W(2.2)}/></g>'
    + f(21, 76, d=4, k=0.45)
    + f'<path d="M54 96 Q56 80 70 78 H96 Q108 80 110 96Z" fill="#5CB7F2" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="98" r="7" fill="{NV}" {W(2)}/>' for x in (66, 100))
    + f'<path d="M104 78 V60" {W(2.2)}/><path d="M104 60 L118 64 L104 68Z" fill="{Y}" {W(1.6)}/>' + f(82, 88, d=6, k=0.5))

I["reutov-museum"] = ("#FDF0FF", "#C27FB3",
    "ситцевый набивной платок с цветочным узором", "развевается на ветру над деревянной набойкой-штампом мануфактуры",
    f'<path d="M14 30 Q40 18 64 26 Q90 34 116 22 L110 80 Q86 92 62 82 Q38 74 18 86Z" fill="#FFF6E0" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="{c}" {W(1.4)}/><circle cx="{x}" cy="{y}" r="1.8" fill="{Y}"/>' for x, y, c in [(30, 38, R), (52, 34, "#5CB7F2"), (96, 34, R), (100, 66, "#5CB7F2"), (34, 70, "#5CB7F2"), (82, 76, R)])
    + f'<path d="M14 30 Q40 18 64 26 Q90 34 116 22" fill="none" stroke="{R}" stroke-width="4"/>'
    + f(66, 54, d=10, k=0.8)
    + f'<rect x="40" y="98" width="48" height="16" rx="3" fill="#C98D52" {s()}/><rect x="56" y="88" width="16" height="12" rx="3" fill="#A8683A" {W(2)}/>'
    f'<path d="M44 114 H84" stroke="{R}" stroke-width="3"/>')

I["reutov-chudo-park"] = ("#FFFDE8", "#F0C640",
    "мягкая поролоновая гусеница-полоса препятствий", "малыш перелезает через её разноцветные горбы-валики",
    f'<rect x="0" y="104" width="128" height="24" fill="#5CB7F2" {W(2.2)}/>'
    + "".join(f'<path d="M{x} 106 Q{x} {y} {x+18} {y} Q{x+36} {y} {x+36} 106Z" fill="{c}" {s()}/>'
              for x, y, c in [(2, 86, R), (30, 74, "#7CD26E"), (58, 82, "#A98BF0"), (86, 74, OR)])
    + f'<circle cx="112" cy="70" r="16" fill="{OR}" {s()}/>' + f(112, 70, d=6, k=0.55)
    + f'<path d="M106 54 Q102 44 108 40 M118 54 Q122 44 116 40" fill="none" {W(2.2)}/>'
    f'<circle cx="48" cy="52" r="12" fill="{SK}" {s()}/>' + f(48, 53, d=4.6, k=0.45)
    + f'<path d="M36 48 Q38 36 48 38 Q58 36 60 48Z" fill="{Y}" {W(2)}/>'
    f'<path d="M48 64 L46 80 M38 68 L30 76 M58 68 L66 74" stroke="{SK}" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M44 66 h10 v12 h-10z" fill="#FF6FA0" {W(2)}/>')

if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        a, b, hero, scene, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
    print("svg:", len(ids))
