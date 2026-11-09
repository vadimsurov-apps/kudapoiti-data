"""Иконки робота fun (2026-11-09, 2-й проход по районам): 56 мест из tools/add_fun_1109c.py.
Каждая придумана и нарисована отдельно (правило абсолютной уникальности); сверено с листами icons-catalog и subjects.txt.
Запуск: python3 tools/icons_fun_1109c.py [id ...]  (печатает строки для subjects.txt)"""
import os, sys
from draw_icons import s, eye, face, sparkle, O

W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=9, k=0.75, **kw: face(cx, cy, d=d, k=k, **kw)
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")


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


def kid(cx, cy, k=1.0, hair="#6B3F23", skin="#FFD9B8"):
    r = 13 * k
    return (f'<circle cx="{cx}" cy="{cy}" r="{r:.1f}" fill="{skin}" {W(2.8)}/>'
            f'<path d="M{cx-r:.1f} {cy-2*k:.1f} Q{cx-r:.1f} {cy-r-3*k:.1f} {cx:.1f} {cy-r-2*k:.1f} '
            f'Q{cx+r:.1f} {cy-r-3*k:.1f} {cx+r:.1f} {cy-2*k:.1f} Q{cx+4*k:.1f} {cy-9*k:.1f} {cx-r:.1f} {cy-2*k:.1f}Z" '
            f'fill="{hair}" {W(2.4)}/>'
            + face(cx, cy + 2 * k, d=5 * k, k=0.5 * k))


I = {}

# ---------------- игровые и семейные центры ----------------
I["funzone-riviera"] = ("#E6F4FF", "#5AA9E6",
    "жёлтая закрученная спиральная горка-труба с глазками",
    "из нижнего конца трубы вылетает хохочущий мальчик в красной кепке",
    f'<path d="M30 22 Q90 14 96 40 Q100 62 60 62 Q26 62 30 84 Q34 104 80 104" fill="none" stroke="{O}" stroke-width="27" stroke-linecap="round"/>'
    f'<path d="M30 22 Q90 14 96 40 Q100 62 60 62 Q26 62 30 84 Q34 104 80 104" fill="none" stroke="#FFD23F" stroke-width="21" stroke-linecap="round"/>'
    f'<path d="M36 22 Q84 18 88 38" fill="none" stroke="#FFF3B0" stroke-width="5" stroke-linecap="round"/>'
    + f(64, 40, d=7, k=0.6) +
    kid(100, 98, k=0.85, hair="#5A3A22") +
    f'<path d="M89 88 Q100 80 111 88 L112 84 Q100 74 88 84Z" fill="#E8303A" {W(2.2)}/>'
    f'<path d="M92 108 L84 118 M108 108 L116 116" {W(3.4)}/>'
    f'<circle cx="74" cy="118" r="3" fill="#fff" opacity=".9"/><circle cx="66" cy="112" r="2" fill="#fff" opacity=".9"/>')

I["monbini-likhacheva"] = ("#FFF0E8", "#F49A6C",
    "бизиборд — доска с замочком, выключателем, шестерёнкой и дверцей",
    "малыш в синем комбинезоне открывает на ней маленькую красную дверцу и удивляется",
    f'<rect x="18" y="20" width="76" height="80" rx="8" fill="#F6C98E" {W(3.2)}/>'
    f'<rect x="28" y="30" width="22" height="26" rx="3" fill="#E8303A" {W(2.6)}/><circle cx="46" cy="44" r="2" fill="#FFD23F"/>'
    f'<rect x="60" y="32" width="24" height="14" rx="4" fill="#fff" {W(2.4)}/><rect x="62" y="34" width="10" height="10" rx="3" fill="#4CC38A" {W(1.8)}/>'
    f'<circle cx="72" cy="70" r="12" fill="#45A8F0" {W(2.8)}/>'
    + "".join(f'<rect x="{70}" y="{55}" width="4" height="6" fill="#45A8F0" {W(1.6)} transform="rotate({a} 72 70)"/>' for a in range(0, 360, 45)) +
    f'<circle cx="72" cy="70" r="4" fill="#fff" {W(1.8)}/>'
    f'<rect x="28" y="66" width="22" height="22" rx="4" fill="#B392F0" {W(2.4)}/><path d="M33 77 h12 M39 71 v12" {W(2.4)}/>'
    + kid(100, 82, k=0.9, hair="#F2C14E") +
    f'<path d="M88 94 Q100 90 112 94 L114 124 L86 124Z" fill="#3D6FD8" {W(2.8)}/>'
    f'<path d="M90 100 Q76 96 52 46" fill="none" {W(3.2)}/>')

I["neon-arena-solntsevo"] = ("#3A2A6E", "#140E33",
    "девочка с двумя светящимися неоновыми браслетами-палочками",
    "прыгает в темноте, а за руками тянутся розовые и голубые светящиеся дуги",
    f'<path d="M14 70 Q30 20 64 26" fill="none" stroke="#FF4FD8" stroke-width="5" stroke-linecap="round" opacity=".9"/>'
    f'<path d="M114 70 Q98 20 64 26" fill="none" stroke="#3FF3FF" stroke-width="5" stroke-linecap="round" opacity=".9"/>'
    f'<path d="M20 112 h88" stroke="#7CFF6B" stroke-width="4" stroke-linecap="round" opacity=".8"/>'
    + kid(64, 54, k=1.0, hair="#2B1B12") +
    f'<path d="M52 68 Q64 64 76 68 L80 94 L48 94Z" fill="#FFD23F" {W(3)}/>'
    f'<path d="M52 72 L34 52 M76 72 L94 52" {W(3.4)}/>'
    f'<rect x="26" y="44" width="12" height="5" rx="2.5" fill="#FF4FD8" transform="rotate(-45 32 46)"/>'
    f'<rect x="90" y="44" width="12" height="5" rx="2.5" fill="#3FF3FF" transform="rotate(45 96 46)"/>'
    f'<path d="M56 94 L50 108 M72 94 L80 106" {W(3.4)}/>'
    + sparkle(22, 30, 4, "#3FF3FF") + sparkle(106, 96, 4, "#FF4FD8"))

I["kosmostar-solntsevo"] = ("#24305E", "#0D1433",
    "карусель-цепочка, где вместо кресел — маленькие планеты",
    "дети на планетах кружатся вокруг улыбающейся звезды на мачте",
    f'<rect x="61" y="40" width="6" height="80" fill="#C9CBE8" {W(2.4)}/>'
    f'<path d="M64 14 l7 14 15 2 -11 10 3 15 -14 -7 -14 7 3 -15 -11 -10 15 -2Z" fill="#FFD23F" {W(2.8)}/>'
    + f(64, 34, d=5, k=0.5) +
    f'<ellipse cx="64" cy="62" rx="50" ry="10" fill="none" stroke="#8C9BFF" stroke-width="2.4" stroke-dasharray="4 4"/>'
    f'<path d="M64 52 L22 74 M64 52 L106 74 M64 52 L44 84 M64 52 L84 84" stroke="#C9CBE8" stroke-width="2"/>'
    f'<circle cx="22" cy="80" r="10" fill="#FF8A5C" {W(2.6)}/><circle cx="106" cy="80" r="10" fill="#4CC38A" {W(2.6)}/>'
    f'<circle cx="44" cy="92" r="9" fill="#45A8F0" {W(2.6)}/><circle cx="84" cy="92" r="9" fill="#E26DD8" {W(2.6)}/>'
    f'<ellipse cx="84" cy="92" rx="15" ry="3.5" fill="none" stroke="#FFD23F" stroke-width="2.4"/>'
    f'<circle cx="22" cy="68" r="5" fill="#FFD9B8" {W(2)}/><circle cx="106" cy="68" r="5" fill="#FFD9B8" {W(2)}/>'
    + sparkle(20, 30, 3) + sparkle(108, 26, 3) + sparkle(100, 112, 2.5))

I["happy-city-solntsevo"] = ("#FFF7DB", "#8ED38A",
    "большая паутина из толстых красных канатов игрового лабиринта",
    "в центре паутины повис вверх ногами довольный мальчик и машет рукой",
    "".join(f'<path d="M64 64 L{x} {y}" stroke="#D83A3A" stroke-width="5" stroke-linecap="round"/>'
            for x, y in [(4, 30), (124, 30), (4, 100), (124, 100), (64, 0), (64, 128), (0, 64), (128, 64)]) +
    "".join(f'<circle cx="64" cy="64" r="{r}" fill="none" stroke="#D83A3A" stroke-width="4"/>' for r in (18, 34, 50)) +
    f'<path d="M56 50 L50 30 M72 50 L80 32" {W(3.4)}/>'
    f'<path d="M54 50 Q64 46 74 50 L76 74 L52 74Z" fill="#45A8F0" {W(3)}/>'
    + kid(64, 86, k=0.95, hair="#6B3F23") +
    f'<path d="M52 66 Q40 74 36 86" fill="none" {W(3.4)}/><circle cx="35" cy="88" r="4" fill="#FFD9B8" {W(2)}/>')

I["myau-loft-tatyanin-park"] = ("#FFE9F3", "#F48FB8",
    "праздничный бумажный колпачок с кошачьими ушками и усами",
    "сидит на голове смеющейся девочки, вокруг летит конфетти",
    kid(64, 80, k=1.5, hair="#3A2414") +
    f'<path d="M44 58 L64 10 L84 58Z" fill="#FFB13B" {W(3.2)}/>'
    f'<path d="M50 44 L58 26 M70 26 L78 44" stroke="#fff" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M50 40 L44 22 L58 32Z M78 40 L84 22 L70 32Z" fill="#FFB13B" {W(2.6)}/>'
    f'<circle cx="64" cy="10" r="5" fill="#FF5C8A" {W(2.4)}/>'
    f'<path d="M48 88 L30 84 M48 92 L30 94 M80 88 L98 84 M80 92 L98 94" {W(2)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="6" height="3" rx="1.5" fill="{c}" transform="rotate({r} {x} {y})"/>'
              for x, y, c, r in [(18, 30, "#45A8F0", 30), (100, 24, "#4CC38A", -20), (24, 60, "#FFD23F", 60), (106, 58, "#B392F0", 10), (14, 104, "#FF5C8A", -40), (112, 108, "#FFB13B", 40)]))

I["happy-city-mozaika"] = ("#FDF3FF", "#C39BEF",
    "надувная горка-радуга, сложенная из цветных квадратиков мозаики",
    "девочка в косичках съезжает по ней на попе, подняв руки",
    "".join(f'<rect x="{x}" y="{y}" width="12" height="12" fill="{c}" {W(1.8)}/>'
            for i, (x, y, c) in enumerate([(14, 92, "#FF5C8A"), (16, 78, "#FFB13B"), (22, 64, "#FFE14D"), (32, 52, "#4CC38A"), (44, 42, "#45A8F0"), (58, 38, "#7B5BE0"),
                                           (72, 40, "#FF5C8A"), (84, 46, "#FFB13B"), (94, 56, "#FFE14D"), (102, 68, "#4CC38A"), (106, 82, "#45A8F0"), (106, 96, "#7B5BE0")])) +
    f'<rect x="0" y="108" width="128" height="22" fill="#F2D3F8" {W(2.4)}/>'
    + kid(96, 44, k=0.9, hair="#C9762E") +
    f'<path d="M84 40 Q76 44 78 52 M108 40 Q116 44 114 52" fill="none" stroke="#C9762E" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M86 56 Q96 52 106 58 L104 70 L88 70Z" fill="#4CC38A" {W(2.8)}/>'
    f'<path d="M86 58 L80 44 M106 58 L114 44" {W(3)}/>')

I["gorodok-parovozikov-mozaika"] = ("#EAF7EE", "#7CC79A",
    "деревянная игрушечная железная дорога-восьмёрка из светлых брусков",
    "малыш на коленках ставит на рельсы красный вагончик с кругляшами-колёсами",
    f'<path d="M64 64 C40 30 10 46 22 70 C34 94 54 80 64 64 C74 48 94 34 106 58 C118 82 88 98 64 64Z" fill="none" stroke="{O}" stroke-width="16"/>'
    f'<path d="M64 64 C40 30 10 46 22 70 C34 94 54 80 64 64 C74 48 94 34 106 58 C118 82 88 98 64 64Z" fill="none" stroke="#E9C38A" stroke-width="11"/>'
    f'<path d="M64 64 C40 30 10 46 22 70 C34 94 54 80 64 64 C74 48 94 34 106 58 C118 82 88 98 64 64Z" fill="none" stroke="#B9884C" stroke-width="2" stroke-dasharray="3 6"/>'
    f'<rect x="88" y="34" width="22" height="16" rx="3" fill="#E8303A" {W(2.6)}/>'
    f'<circle cx="94" cy="52" r="3.5" fill="#FFD23F" {W(1.8)}/><circle cx="104" cy="52" r="3.5" fill="#FFD23F" {W(1.8)}/>'
    + kid(46, 100, k=0.85, hair="#F2C14E") +
    f'<path d="M56 96 Q76 78 90 50" fill="none" {W(3)}/>')

I["happy-city-kuzminki"] = ("#E8FBFF", "#45C1D8",
    "вертикальная стена-лабиринт с жёлобами, по которым бегут цветные шарики",
    "малыш тянется на цыпочках и запускает сверху новый шарик",
    f'<rect x="20" y="16" width="70" height="98" rx="6" fill="#fff" {W(3.2)}/>'
    f'<path d="M26 32 L80 40 M84 56 L30 64 M26 80 L80 88" stroke="#FFB13B" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M26 32 L80 40 M84 56 L30 64 M26 80 L80 88" {W(2)} fill="none"/>'
    f'<circle cx="60" cy="31" r="5" fill="#FF5C8A" {W(2)}/><circle cx="46" cy="56" r="5" fill="#4CC38A" {W(2)}/>'
    f'<circle cx="70" cy="80" r="5" fill="#7B5BE0" {W(2)}/><circle cx="34" cy="106" r="5" fill="#FFD23F" {W(2)}/>'
    + kid(104, 74, k=0.85, hair="#4A2C1A") +
    f'<path d="M94 86 Q104 82 114 86 L116 118 L92 118Z" fill="#E8303A" {W(2.8)}/>'
    f'<path d="M96 88 Q90 50 84 22" fill="none" {W(3)}/><circle cx="84" cy="18" r="5" fill="#45A8F0" {W(2)}/>')

I["detsky-ugolok-afimall"] = ("#F0F7FF", "#9BB7E8",
    "оранжевый мяч-прыгун с рожками-ручками",
    "малыш скачет на нём верхом высоко над полом, за ним дуга прыжка",
    f'<path d="M14 112 Q30 40 64 70" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="5 5"/>'
    f'<ellipse cx="64" cy="114" rx="22" ry="5" fill="#7F96C8" opacity=".5"/>'
    f'<circle cx="64" cy="82" r="26" fill="#FF8A3D" {W(3.2)}/>'
    f'<path d="M50 60 Q46 46 54 44 M78 60 Q82 46 74 44" fill="none" stroke="#FF8A3D" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M50 60 Q46 46 54 44 M78 60 Q82 46 74 44" fill="none" {W(2)}/>'
    + f(64, 86, d=8, k=0.7) +
    kid(64, 32, k=0.9, hair="#7A4A26") +
    f'<path d="M54 44 Q64 42 74 44" fill="none" {W(3)}/>'
    f'<path d="M50 56 L40 72 M78 56 L88 72" {W(3.2)}/>')

I["igrarium-park-pobedy"] = ("#EFFBEA", "#5DBB63",
    "настольный футбол-кикер с синими и красными фигурками на штангах",
    "две фигурки-человечка в упор бьют по белому мячу, мяч летит к воротам",
    f'<rect x="12" y="34" width="104" height="66" rx="6" fill="#3E9E4F" {W(3.2)}/>'
    f'<path d="M64 34 V100" stroke="#fff" stroke-width="2.4"/><circle cx="64" cy="67" r="10" fill="none" stroke="#fff" stroke-width="2.4"/>'
    f'<rect x="8" y="56" width="6" height="22" fill="#fff" {W(2)}/><rect x="114" y="56" width="6" height="22" fill="#fff" {W(2)}/>'
    f'<path d="M44 20 V114 M84 20 V114" stroke="#C9CBE8" stroke-width="4"/><path d="M44 20 V114 M84 20 V114" {W(1.4)}/>'
    f'<rect x="36" y="56" width="16" height="22" rx="5" fill="#3D6FD8" {W(2.6)}/>'
    f'<circle cx="44" cy="50" r="7" fill="#FFD9B8" {W(2.4)}/>'
    f'<rect x="76" y="56" width="16" height="22" rx="5" fill="#E8303A" {W(2.6)}/>'
    f'<circle cx="84" cy="50" r="7" fill="#FFD9B8" {W(2.4)}/>'
    + eye(42, 50, 0.4) + eye(46, 50, 0.4) + eye(82, 50, 0.4) + eye(86, 50, 0.4) +
    f'<circle cx="64" cy="82" r="6" fill="#fff" {W(2.4)}/>'
    f'<path d="M20 108 h16 M24 114 h10" stroke="#fff" stroke-width="2" opacity=".7"/>')

I["bondiki-ovchinnikovsky"] = ("#FFF6E5", "#F2B66B",
    "широкая деревянная горка-скат с бортиками",
    "малыш в полосатой кофте съезжает по ней на животе головой вперёд, раскинув руки",
    f'<path d="M20 30 H44 L112 100 H88Z" fill="#E9B872" {W(3.2)}/>'
    f'<path d="M20 30 L88 100 M44 30 L112 100" {W(2.4)}/>'
    f'<rect x="14" y="30" width="10" height="84" fill="#C98B4A" {W(2.8)}/>'
    f'<path d="M14 52 H34 M14 72 H30 M14 92 H30" {W(2.6)}/>'
    f'<rect x="0" y="108" width="128" height="22" fill="#F7E2B8" {W(2.4)}/>'
    + kid(92, 80, k=0.85, hair="#3A2414") +
    f'<path d="M80 74 L60 58 Q56 54 52 58 L66 74Z" fill="#fff" {W(2.6)}/>'
    f'<path d="M62 62 l4 4 M58 58 l3 3" stroke="#E8303A" stroke-width="3"/>'
    f'<path d="M84 72 L96 60 M98 86 L110 76" {W(3)}/><path d="M54 58 L44 50 M58 56 L52 44" {W(3)}/>')

I["starlab-metropolis"] = ("#2E2A6B", "#0E0B2E",
    "стеклянная банка-лаборатория, полная маленьких светящихся звёзд",
    "мальчик в защитных очках приоткрыл крышку, и звёзды вылетают наружу",
    f'<rect x="26" y="48" width="48" height="62" rx="12" fill="#BFE8FF" opacity=".55" {W(3)}/>'
    f'<rect x="28" y="40" width="44" height="10" rx="3" fill="#C9CBE8" {W(2.6)} transform="rotate(-18 50 45)"/>'
    + "".join(sparkle(x, y, r, c) for x, y, r, c in [(40, 74, 4, "#FFE14D"), (58, 90, 4, "#FFE14D"), (46, 100, 3, "#FFD9F0"), (60, 64, 3, "#9FF0FF"),
                                                     (50, 26, 4, "#FFE14D"), (68, 14, 3, "#9FF0FF"), (30, 18, 3, "#FFD9F0")]) +
    kid(96, 68, k=0.95, hair="#C9762E") +
    f'<rect x="82" y="60" width="28" height="9" rx="4.5" fill="#4CC38A" opacity=".75" {W(2)}/>'
    f'<path d="M84 82 Q96 78 108 82 L110 118 L82 118Z" fill="#fff" {W(2.8)}/>'
    f'<path d="M84 86 Q74 76 70 52" fill="none" {W(3)}/>')

I["kids-castle-mitino"] = ("#FFF4E0", "#E9A15C",
    "картонная коробка-замок с прорезанными зубцами и окошком",
    "мальчик в короне из фольги выглядывает в окошко, на башне — флажок на палочке",
    f'<path d="M24 44 h12 v-10 h12 v10 h12 v-10 h12 v10 h12 v-10 h12 v10 h8 V112 H24Z" fill="#D9A066" {W(3.2)}/>'
    f'<path d="M24 70 L104 66 M60 112 L58 80" stroke="#B57A3E" stroke-width="2"/>'
    f'<rect x="46" y="58" width="36" height="34" rx="16" fill="#5A3A22" {W(2.8)}/>'
    + kid(64, 80, k=0.9, hair="#5A3A22") +
    f'<path d="M52 66 L56 56 L60 64 L64 54 L68 64 L72 56 L76 66Z" fill="#E3E6EE" {W(2.4)}/>'
    f'<path d="M100 34 V10" {W(2.6)}/><path d="M100 10 L116 16 L100 22Z" fill="#E8303A" {W(2.4)}/>'
    f'<rect x="0" y="110" width="128" height="20" fill="#9FD67C" {W(2.4)}/>')

I["wow-land-krasnogorsk"] = ("#FFF0F6", "#F06A9B",
    "три фольгированных шара-буквы «W», «O», «W»",
    "парят на ленточках над праздничным столом с маленьким тортиком",
    f'<path d="M14 30 l6 26 6 -18 6 18 6 -26" fill="none" stroke="{O}" stroke-width="13" stroke-linejoin="round" stroke-linecap="round"/>'
    f'<path d="M14 30 l6 26 6 -18 6 18 6 -26" fill="none" stroke="#B392F0" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>'
    f'<circle cx="64" cy="38" r="15" fill="none" stroke="{O}" stroke-width="13"/><circle cx="64" cy="38" r="15" fill="none" stroke="#FFD23F" stroke-width="8"/>'
    f'<path d="M86 30 l6 26 6 -18 6 18 6 -26" fill="none" stroke="{O}" stroke-width="13" stroke-linejoin="round" stroke-linecap="round"/>'
    f'<path d="M86 30 l6 26 6 -18 6 18 6 -26" fill="none" stroke="#45C1D8" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>'
    f'<path d="M26 60 Q30 76 50 88 M64 56 V86 M98 60 Q96 76 78 88" fill="none" stroke="{O}" stroke-width="1.6"/>'
    f'<rect x="8" y="98" width="112" height="10" rx="3" fill="#fff" {W(2.6)}/>'
    f'<rect x="50" y="84" width="28" height="14" rx="3" fill="#FF8AB0" {W(2.6)}/><path d="M64 84 v-6" {W(2.2)}/>'
    f'<path d="M64 72 q3 3 0 6 q-3 -3 0 -6Z" fill="#FFB13B"/>' + f(64, 90, d=5, k=0.4))

I["konfetka-krasnogorsk"] = ("#F3FFF4", "#86D9A0",
    "качели-балансир в виде конфеты в фантике: концы-хвостики служат сиденьями",
    "два малыша качаются на концах — один вверху, другой внизу",
    f'<path d="M58 112 L64 82 L70 112Z" fill="#B392F0" {W(3)}/>'
    f'<g transform="rotate(-14 64 80)">'
    f'<rect x="40" y="70" width="48" height="20" rx="10" fill="#FF5C8A" {W(3)}/>'
    f'<path d="M48 72 l8 16 M60 72 l8 16 M72 72 l8 16" stroke="#fff" stroke-width="3"/>'
    f'<path d="M40 80 L12 70 L12 90Z M88 80 L116 70 L116 90Z" fill="#FFD23F" {W(2.8)}/>'
    + kid(18, 58, k=0.7, hair="#6B3F23") + kid(110, 58, k=0.7, hair="#F2C14E") + '</g>'
    f'<rect x="0" y="112" width="128" height="18" fill="#BFEFC8" {W(2.4)}/>')

I["hello-park-mega-teply-stan"] = ("#E7F0FF", "#6E8BEA",
    "стол для аэрохоккея с белым полем и голубыми бортами",
    "две детские руки с красной и жёлтой битами, шайба со свистом летит в ворота",
    f'<rect x="20" y="16" width="88" height="100" rx="12" fill="#fff" {W(3.2)}/>'
    f'<rect x="20" y="16" width="88" height="100" rx="12" fill="none" stroke="#45A8F0" stroke-width="5"/>'
    f'<path d="M20 66 H108" stroke="#E8303A" stroke-width="2"/><circle cx="64" cy="66" r="12" fill="none" stroke="#45A8F0" stroke-width="2"/>'
    f'<rect x="50" y="14" width="28" height="6" rx="3" fill="{O}"/><rect x="50" y="112" width="28" height="6" rx="3" fill="{O}"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1" fill="#9BB7E8"/>' for x in range(30, 104, 10) for y in range(26, 110, 12)) +
    f'<circle cx="62" cy="94" r="10" fill="#E8303A" {W(2.8)}/><circle cx="62" cy="94" r="4" fill="#B51E28" {W(1.8)}/>'
    f'<circle cx="74" cy="36" r="10" fill="#FFD23F" {W(2.8)}/><circle cx="74" cy="36" r="4" fill="#E0A800" {W(1.8)}/>'
    f'<ellipse cx="58" cy="60" rx="7" ry="4" fill="{O}"/><path d="M66 66 L84 80 M70 62 L88 72" stroke="#9BB7E8" stroke-width="2"/>'
    + f(62, 92, d=4, k=0.35, mouth=False, blush=False))

I["kids-lab-loft-ostrovityanova"] = ("#F6FFE8", "#A8D86A",
    "колба «слоновья зубная паста» с извергающейся полосатой пеной",
    "девочка в больших защитных очках отпрыгивает и смеётся, пена летит до потолка",
    f'<path d="M30 112 L42 74 V56 H58 V74 L70 112Z" fill="#E9F7FF" {W(3.2)}/>'
    f'<path d="M34 104 L66 104 L70 112 L30 112Z" fill="#B392F0" {W(2)}/>'
    f'<path d="M44 58 Q30 30 48 20 Q60 6 70 22 Q90 10 92 32 Q104 36 94 48 Q84 58 66 50 Q60 60 52 56Z" fill="#fff" {W(3)}/>'
    f'<path d="M50 30 Q60 24 70 32 M64 42 Q76 36 86 42" fill="none" stroke="#FF5C8A" stroke-width="3" stroke-linecap="round"/>'
    f'<path d="M52 22 Q66 16 80 24" fill="none" stroke="#45C1D8" stroke-width="3" stroke-linecap="round"/>'
    + kid(98, 78, k=0.9, hair="#2B1B12") +
    f'<rect x="84" y="72" width="28" height="10" rx="5" fill="#FFE14D" opacity=".75" {W(2)}/>'
    f'<path d="M86 90 Q98 86 110 90 L112 118 L84 118Z" fill="#fff" {W(2.8)}/>'
    f'<path d="M86 94 L76 80 M110 94 L118 82" {W(3)}/>')

I["lunomosik-chertanovo"] = ("#FFF8E1", "#F7B733",
    "пиньята в форме пятиконечной звезды с бахромой и ленточками",
    "мальчик с повязкой на глазах бьёт её палкой, из неё сыплются конфеты",
    f'<path d="M80 10 V22" {W(2)}/>'
    f'<path d="M80 22 l8 16 18 2 -13 12 4 18 -17 -9 -17 9 4 -18 -13 -12 18 -2Z" fill="#FF5C8A" {W(3)}/>'
    f'<path d="M66 54 l-4 14 M74 60 l-2 14 M86 60 l2 14 M94 54 l4 14" stroke="#45C1D8" stroke-width="3" stroke-linecap="round"/>'
    + f(80, 48, d=6, k=0.55) +
    kid(36, 84, k=0.95, hair="#5A3A22") +
    f'<rect x="22" y="76" width="28" height="6" rx="3" fill="#7B5BE0" {W(1.8)}/>'
    f'<path d="M46 92 L66 64" stroke="#C98B4A" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M28 98 Q36 94 44 98 L46 122 L26 122Z" fill="#4CC38A" {W(2.8)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="8" height="5" rx="2.5" fill="{c}" {W(1.4)} transform="rotate({r} {x} {y})"/>'
              for x, y, c, r in [(70, 90, "#FFD23F", 20), (86, 98, "#45A8F0", -30), (98, 86, "#E8303A", 40), (78, 108, "#4CC38A", 10)]))

I["mesto-vstrechi-solntsevo"] = ("#EAF1FF", "#7FA4E8",
    "круглый общий стол с разными стульчиками, вид сверху",
    "четверо детей за столом вместе лепят, рисуют и клеят, посреди стола — банка с кисточками",
    f'<circle cx="64" cy="64" r="34" fill="#F6C98E" {W(3.2)}/>'
    + "".join(kid(x, y, k=0.65, hair=h) for x, y, h in [(64, 18, "#3A2414"), (110, 64, "#F2C14E"), (64, 110, "#C9762E"), (18, 64, "#6B3F23")]) +
    f'<rect x="46" y="40" width="16" height="12" fill="#fff" {W(2)}/><path d="M50 46 q4 -4 8 0" fill="none" stroke="#E8303A" stroke-width="2"/>'
    f'<circle cx="82" cy="72" r="6" fill="#4CC38A" {W(2)}/><circle cx="88" cy="66" r="4" fill="#FF8A3D" {W(2)}/>'
    f'<rect x="50" y="78" width="14" height="10" rx="2" fill="#FFE14D" {W(2)}/>'
    f'<circle cx="64" cy="64" r="7" fill="#BFE8FF" {W(2.4)}/><path d="M62 60 L58 50 M66 60 L70 50" {W(2)}/>')

# ---------------- квесты и лазертаг ----------------
I["liga-mirov-reaktor"] = ("#1E3B2E", "#0A1A12",
    "зелёная светящаяся капсула-реактор с решёткой и мигающей лампой",
    "мальчик в шлеме с лазерным бластером осторожно выглядывает из-за неё",
    f'<rect x="28" y="30" width="44" height="80" rx="20" fill="#7CFF6B" opacity=".9" {W(3.2)}/>'
    f'<path d="M30 52 H70 M30 72 H70 M30 92 H70" {W(2.6)}/>'
    f'<rect x="40" y="14" width="20" height="18" rx="4" fill="#9AA3B5" {W(2.6)}/><circle cx="50" cy="12" r="5" fill="#FF3B3B" {W(2)}/>'
    f'<path d="M42 8 L36 2 M58 8 L64 2" stroke="#FF3B3B" stroke-width="2.4" stroke-linecap="round"/>'
    + f(50, 62, d=8, k=0.7) +
    kid(90, 70, k=0.95, hair="#2B1B12") +
    f'<path d="M77 66 Q90 50 103 66" fill="#3D6FD8" {W(2.6)}/>'
    f'<path d="M78 84 Q90 80 102 84 L104 118 L76 118Z" fill="#3D6FD8" {W(2.8)}/>'
    f'<rect x="96" y="88" width="24" height="9" rx="3" fill="#FFB13B" {W(2.4)}/><path d="M120 92 h8" stroke="#FF3B3B" stroke-width="3"/>')

I["lovushka-quest-shchipkovsky"] = ("#FFF5DC", "#D8AE68",
    "деревянная летательная машина Леонардо с перепончатыми крыльями, как у летучей мыши",
    "парит над головой удивлённого мальчика, который светит на неё фонариком",
    f'<path d="M64 40 Q40 18 8 26 Q22 34 18 44 Q30 40 34 50 Q44 44 50 52Z" fill="#F3E2BE" {W(3)}/>'
    f'<path d="M64 40 Q88 18 120 26 Q106 34 110 44 Q98 40 94 50 Q84 44 78 52Z" fill="#F3E2BE" {W(3)}/>'
    f'<path d="M64 40 L18 30 M64 40 L30 44 M64 40 L110 30 M64 40 L98 44" stroke="#9B6B35" stroke-width="2"/>'
    f'<rect x="56" y="34" width="16" height="22" rx="5" fill="#C98B4A" {W(2.8)}/><path d="M64 56 V66" {W(2.4)}/>'
    f'<path d="M50 90 L60 60 L74 60 L82 90Z" fill="#FFF3B0" opacity=".7"/>'
    + kid(64, 98, k=0.95, hair="#3A2414") +
    f'<path d="M56 86 L60 76" {W(3)}/><rect x="56" y="70" width="8" height="10" rx="2" fill="#5B4A6E" {W(2)}/>'
    f'<ellipse cx="64" cy="104" rx="3" ry="3.6" fill="{O}"/>')

I["atmokids-varshavka"] = ("#E9E8FF", "#7D73D9",
    "сияющий фиолетовый кристалл-головоломка на каменном пьедестале",
    "две детские ладошки одновременно касаются его граней, и кристалл вспыхивает",
    f'<rect x="40" y="88" width="48" height="26" rx="3" fill="#B6B2C9" {W(3)}/><path d="M40 98 H88" {W(2)}/>'
    f'<path d="M64 20 L86 46 L76 86 H52 L42 46Z" fill="#B392F0" {W(3.2)}/>'
    f'<path d="M64 20 L58 46 L64 86 M58 46 H42 M58 46 L86 46" fill="none" stroke="#7B5BE0" stroke-width="2"/>'
    + f(66, 60, d=6, k=0.55) +
    f'<path d="M14 70 Q24 58 38 56 L40 62 Q30 66 26 76Z" fill="#FFD9B8" {W(2.6)}/>'
    f'<path d="M114 70 Q104 58 90 56 L88 62 Q98 66 102 76Z" fill="#FFC89E" {W(2.6)}/>'
    + sparkle(30, 34, 5, "#FFE14D") + sparkle(98, 30, 5, "#FFE14D") + sparkle(64, 10, 4, "#fff"))

I["kvest-dlya-vsekh-mira"] = ("#FFF4DE", "#C9925A",
    "старый пергаментный лист, по которому сами собой бегут чернильные следы ног",
    "девочка в мантии подсвечивает его кончиком волшебной палочки",
    f'<path d="M16 34 Q40 26 70 34 L66 104 Q40 96 12 104Z" fill="#F7E6C2" {W(3)}/>'
    f'<path d="M16 34 Q8 40 14 46 M12 104 Q4 98 10 92" fill="none" {W(2.6)}/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="3" ry="4.4" fill="#5B4A6E" transform="rotate({r} {x} {y})"/>'
              for x, y, r in [(24, 90, -20), (32, 84, 10), (34, 74, -20), (42, 68, 10), (44, 58, -10), (52, 52, 20), (54, 42, 0)]) +
    kid(96, 58, k=0.95, hair="#8A4B1E") +
    f'<path d="M80 70 Q96 64 112 70 L118 120 L74 120Z" fill="#3A2F6E" {W(2.8)}/>'
    f'<path d="M86 66 L96 72 L106 66" fill="none" stroke="#E8303A" stroke-width="3"/>'
    f'<path d="M82 80 L66 62" stroke="#8A5A2B" stroke-width="3.4" stroke-linecap="round"/>' + sparkle(64, 58, 5, "#FFE14D"))

I["fort-boyard-tushinskaya"] = ("#E6F6FF", "#3F8FC9",
    "тяжёлое бревно-маятник на цепях, раскачивающееся над водой",
    "мальчик в жёлтой футболке перепрыгивает через него с узкой доски на доску",
    f'<path d="M0 100 Q16 94 32 100 T64 100 T96 100 T128 100 V130 H0Z" fill="#3FA2E0" {W(2.6)}/>'
    f'<path d="M30 6 L48 56 M78 6 L60 56" {W(2.6)} stroke-dasharray="4 3"/>'
    f'<rect x="22" y="52" width="62" height="16" rx="8" fill="#B07A44" {W(3)} transform="rotate(-10 53 60)"/>'
    f'<path d="M30 56 l6 6 M70 52 l6 6" stroke="#7E5128" stroke-width="2"/>'
    f'<rect x="4" y="86" width="30" height="8" fill="#D9A066" {W(2.4)}/><rect x="94" y="86" width="30" height="8" fill="#D9A066" {W(2.4)}/>'
    + kid(96, 30, k=0.85, hair="#5A3A22") +
    f'<path d="M86 42 Q96 38 106 42 L104 58 L88 58Z" fill="#FFD23F" {W(2.8)}/>'
    f'<path d="M88 46 L76 38 M104 46 L116 40 M90 58 L84 72 M102 58 L112 68" {W(3)}/>')

I["vpodvale-leningradskoe"] = ("#F1E4CF", "#9C6B3E",
    "дубовая бочка, доверху полная красных яблок",
    "в бочке спрятался мальчик — видны только глаза и макушка, он подслушивает",
    f'<path d="M28 44 Q24 80 30 116 H98 Q104 80 100 44Z" fill="#B07A44" {W(3.2)}/>'
    f'<path d="M26 62 Q64 68 102 62 M27 98 Q64 104 101 98" fill="none" stroke="#5B4A6E" stroke-width="5"/>'
    f'<path d="M48 46 Q46 80 50 114 M80 46 Q82 80 78 114" fill="none" stroke="#7E5128" stroke-width="2"/>'
    f'<ellipse cx="64" cy="44" rx="36" ry="9" fill="#5A3A22" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="7" fill="#E8303A" {W(2.2)}/><path d="M{x} {y-7} l2 -4" {W(1.8)}/>'
              for x, y in [(38, 40), (90, 40), (78, 34)]) +
    f'<path d="M48 40 Q64 12 80 40" fill="#C9762E" {W(2.6)}/>'
    + eye(57, 34, 0.75) + eye(71, 34, 0.75) +
    f'<path d="M44 30 Q40 24 44 20" fill="none" {W(2)}/>')

I["dzhumandzhi-yasenevo"] = ("#E9F7DC", "#4F9A3E",
    "открытая коробка настольной игры, из которой вырастают лианы и большой цветок с зубками",
    "мальчик с кубиком в руке отшатывается от цветка, а он любопытно тянется к нему",
    f'<path d="M14 92 L64 78 L114 92 L64 106Z" fill="#7C4A2B" {W(3)}/>'
    f'<path d="M14 92 V104 L64 118 L114 104 V92" fill="#5A3A22" {W(3)}/>'
    f'<path d="M36 88 Q20 60 40 40 Q54 28 46 14 M64 88 Q70 60 86 52 M90 88 Q110 70 100 50" fill="none" stroke="#3E9E4F" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M40 40 q-10 -6 -14 2 q8 6 14 -2Z M86 52 q8 -10 16 -4 q-6 10 -16 4Z" fill="#6DBB4F" {W(2)}/>'
    f'<circle cx="46" cy="14" r="12" fill="#E8303A" {W(2.8)}/><path d="M38 18 l3 -4 3 4 3 -4 3 4 3 -4" fill="#fff" {W(1.6)}/>'
    + eye(42, 9, 0.5) + eye(50, 9, 0.5) +
    kid(96, 30, k=0.75, hair="#C9762E") +
    f'<rect x="108" y="40" width="9" height="9" rx="2" fill="#fff" {W(2)}/><circle cx="112.5" cy="44.5" r="1.4" fill="{O}"/>')

# ---------------- музей ----------------
I["sensorium-arbat"] = ("#2A2340", "#0B0814",
    "большой светлый нос, который нюхает в полной темноте",
    "в темноте светятся только нос с зажмуренными глазками и маленькая ромашка перед ним",
    f'<path d="M58 30 Q50 64 40 76 Q36 90 52 92 Q60 98 70 92 Q84 92 82 78 Q74 64 70 30Z" fill="#FFD9B8" {W(3.2)}/>'
    f'<ellipse cx="54" cy="86" rx="4" ry="3" fill="{O}"/><ellipse cx="70" cy="86" rx="4" ry="3" fill="{O}"/>'
    f'<path d="M44 30 q6 6 12 0 M70 30 q6 6 12 0" fill="none" stroke="#FFD9B8" stroke-width="3" stroke-linecap="round"/>'
    + "".join(f'<ellipse cx="{94+9*__import__("math").cos(a*0.785)}" cy="{100+9*__import__("math").sin(a*0.785)}" rx="5" ry="3" fill="#fff" transform="rotate({a*45} {94+9*__import__("math").cos(a*0.785)} {100+9*__import__("math").sin(a*0.785)})"/>' for a in range(8)) +
    f'<circle cx="94" cy="100" r="4.5" fill="#FFD23F" {W(1.6)}/>'
    f'<path d="M84 90 Q80 84 82 78 M90 86 Q88 80 92 74" fill="none" stroke="#9FF0FF" stroke-width="2" stroke-linecap="round" opacity=".8"/>'
    + sparkle(22, 30, 2.5, "#666a88") + sparkle(108, 26, 2, "#666a88"))

# ---------------- творческие студии ----------------
I["lulu-pyatnitskoe"] = ("#FFF4FA", "#F2A7C9",
    "длинная бумажная лента-рулон, размотанная по полу",
    "малыш лежит на животе и рисует на ней фломастером извилистую дорожку-змейку",
    f'<rect x="96" y="20" width="22" height="36" rx="10" fill="#fff" {W(3)}/><ellipse cx="107" cy="20" rx="11" ry="4" fill="#E3E6EE" {W(2.4)}/>'
    f'<path d="M100 54 L40 96 L10 120 H40 L118 56Z" fill="#fff" {W(3)}/>'
    f'<path d="M96 64 Q86 60 82 70 Q78 80 66 76 Q56 74 52 86 Q48 96 36 98" fill="none" stroke="#7B5BE0" stroke-width="3.4" stroke-linecap="round"/>'
    + kid(40, 58, k=0.85, hair="#6B3F23") +
    f'<path d="M34 70 Q22 72 14 84 L22 88 Q30 78 40 76Z" fill="#4CC38A" {W(2.6)}/>'
    f'<path d="M46 70 L54 84" {W(3)}/><rect x="52" y="82" width="5" height="12" rx="2" fill="#7B5BE0" {W(1.6)} transform="rotate(-30 54 88)"/>')

I["mnogogrannik-mitino"] = ("#E8F7F5", "#4FB8A8",
    "бумажный многогранник из разноцветных пятиугольников",
    "девочка держит его на ладони и приклеивает последнюю грань тюбиком клея",
    f'<path d="M50 20 L74 18 L86 38 L72 58 L48 58 L36 40Z" fill="#FFB13B" {W(3)}/>'
    f'<path d="M50 20 L58 34 L74 18 M58 34 L52 50 L36 40 M58 34 L72 44 L86 38 M52 50 L48 58 M72 44 L72 58" fill="none" {W(2.2)}/>'
    f'<path d="M58 34 L72 44 L86 38 L74 18Z" fill="#45A8F0" {W(2.2)}/><path d="M36 40 L52 50 L48 58Z" fill="#FF5C8A" {W(2.2)}/>'
    + f(60, 44, d=5, k=0.45) +
    f'<path d="M86 30 L100 22 L104 34Z" fill="#4CC38A" {W(2.2)}/>'
    + kid(64, 92, k=0.95, hair="#3A2414") +
    f'<path d="M40 64 Q48 70 54 80 M88 72 Q96 50 100 40" fill="none" {W(3)}/>'
    f'<rect x="96" y="38" width="8" height="18" rx="2" fill="#fff" {W(2)} transform="rotate(30 100 47)"/>')

I["art-klass-mitino"] = ("#FFFBEA", "#F0C75E",
    "трафарет-пластинка с вырезанной звездой",
    "мальчик через трафарет набивает краску губкой, на листе появляется синяя звезда",
    f'<rect x="10" y="54" width="108" height="66" rx="4" fill="#fff" {W(3)}/>'
    f'<path d="M84 64 l5 10 11 1.5 -8 7.5 2 11 -10 -5 -10 5 2 -11 -8 -7.5 11 -1.5Z" fill="#45A8F0" {W(2.4)}/>'
    f'<rect x="16" y="60" width="54" height="50" rx="3" fill="#B392F0" opacity=".9" {W(2.8)} transform="rotate(-8 43 85)"/>'
    f'<path d="M42 68 l5 10 11 1.5 -8 7.5 2 11 -10 -5 -10 5 2 -11 -8 -7.5 11 -1.5Z" fill="#fff" {W(2.4)} transform="rotate(-8 43 85)"/>'
    f'<rect x="34" y="38" width="22" height="16" rx="5" fill="#FFD23F" {W(2.6)}/><path d="M36 54 h18" stroke="#45A8F0" stroke-width="3"/>'
    + kid(80, 24, k=0.8, hair="#6B3F23") + f'<path d="M72 34 Q62 40 56 44" fill="none" {W(3)}/>')

I["in-art-krasnogorsk"] = ("#F0FAFF", "#79C3E8",
    "резиновый штамп-ёжик на деревянной ручке",
    "штампует на листе ровный ряд зелёных ёжиков и подмигивает",
    f'<rect x="6" y="84" width="116" height="38" rx="4" fill="#fff" {W(3)}/>'
    + "".join(f'<path d="M{x} 114 Q{x-2} 98 {x+12} 96 l3 -6 4 5 4 -6 4 6 4 -4 Q{x+32} 102 {x+30} 114Z" fill="#4CC38A" {W(2)}/><circle cx="{x+8}" cy="106" r="1.6" fill="{O}"/>' for x in (12, 84)) +
    f'<rect x="50" y="10" width="28" height="32" rx="10" fill="#C98B4A" {W(3)}/>'
    f'<rect x="36" y="40" width="56" height="16" rx="4" fill="#D9A066" {W(3)}/>'
    f'<path d="M36 56 h56 l-3 10 -5 -6 -5 8 -5 -8 -5 8 -5 -8 -5 8 -5 -8 -5 8 -5 -6Z" fill="#4CC38A" {W(2.6)}/>'
    + eye(57, 26, 0.65) + f'<path d="M66 26 q4 -4 7 0" fill="none" {W(2.2)}/>'
    f'<path d="M58 33 q6 4 11 0" fill="none" {W(2.2)}/>' + sparkle(108, 30, 5, "#FFE14D"))

I["neotkrytye-ostrova"] = ("#E3F4FF", "#3E8ED0",
    "раскрытая книга-парусник: страницы — паруса, обложка — корпус",
    "плывёт по волнам к неизвестной зелёной земле на горизонте, над ней чайка",
    f'<path d="M86 64 Q100 52 116 62 L118 66 H84Z" fill="#6DBB4F" {W(2.6)}/>'
    f'<path d="M0 92 Q16 86 32 92 T64 92 T96 92 T128 92 V130 H0Z" fill="#45A8F0" {W(2.6)}/>'
    f'<path d="M22 84 L86 84 L78 100 L30 100Z" fill="#E8303A" {W(3)}/>'
    f'<path d="M54 82 V20" {W(2.8)}/>'
    f'<path d="M52 24 Q36 40 28 78 L52 78Z" fill="#fff" {W(2.8)}/><path d="M56 24 Q72 40 80 78 L56 78Z" fill="#fff" {W(2.8)}/>'
    f'<path d="M36 50 h12 M34 60 h14 M60 50 h12 M60 60 h14" stroke="#9BB7E8" stroke-width="2"/>'
    + f(54, 92, d=6, k=0.5) +
    f'<path d="M96 30 q5 -5 10 0 q5 -5 10 0" fill="none" {W(2.4)}/>')

I["vitaart-garibaldi"] = ("#FFF0F0", "#F08C8C",
    "ватная палочка-художник с румяной ваткой-головой",
    "рисует точками на листе: из цветных точек складывается большой цветок",
    f'<rect x="10" y="20" width="84" height="96" rx="4" fill="#fff" {W(3)}/>'
    + "".join(f'<circle cx="{52+20*__import__("math").cos(a*1.0472)+dx}" cy="{60+20*__import__("math").sin(a*1.0472)+dy}" r="3.4" fill="{c}"/>'
              for a in range(6) for (dx, dy), c in zip([(0, 0), (5, 4), (-4, 5)], ["#FF5C8A", "#FFB13B", "#B392F0"])) +
    "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#FFD23F"/>' for x, y in [(52, 60), (48, 56), (56, 64), (56, 56), (48, 64)]) +
    "".join(f'<circle cx="52" cy="{y}" r="3" fill="#4CC38A"/>' for y in (84, 92, 100, 108)) +
    f'<rect x="96" y="30" width="7" height="70" rx="3.5" fill="#fff" {W(2.6)} transform="rotate(28 100 65)"/>'
    f'<ellipse cx="114" cy="36" rx="10" ry="12" fill="#FFE0E8" {W(2.6)}/>' + f(114, 36, d=4, k=0.4) +
    f'<ellipse cx="84" cy="96" rx="7" ry="9" fill="#FFE0E8" {W(2.6)}/><circle cx="84" cy="100" r="3" fill="#FF5C8A"/>')

I["goncharnaya-sreda-panferova"] = ("#F3ECE4", "#B9957A",
    "глиняная кружка с отпечатком детской ладошки на боку",
    "кисточка раскрашивает пальчики-лучи отпечатка в жёлтое солнышко",
    f'<path d="M30 34 H90 L86 112 Q60 118 34 112Z" fill="#E4C3A1" {W(3.2)}/>'
    f'<path d="M90 50 Q112 52 110 72 Q108 92 88 90" fill="none" stroke="{O}" stroke-width="12"/>'
    f'<path d="M90 50 Q112 52 110 72 Q108 92 88 90" fill="none" stroke="#E4C3A1" stroke-width="7"/>'
    f'<ellipse cx="60" cy="34" rx="30" ry="6" fill="#C9A07A" {W(3)}/>'
    f'<circle cx="58" cy="80" r="12" fill="#FFD23F" {W(2.4)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="7" height="16" rx="3.5" fill="{c}" {W(2)} transform="rotate({r} {x+3} {y+16})"/>'
              for x, y, r, c in [(40, 58, -30, "#FFD23F"), (48, 52, -12, "#FFD23F"), (56, 50, 0, "#FFD23F"), (64, 52, 12, "#E4C3A1"), (70, 62, 40, "#E4C3A1")]) +
    f(58, 80, d=4, k=0.4) +
    f'<rect x="86" y="10" width="6" height="36" rx="3" fill="#C98B4A" {W(2.4)} transform="rotate(30 89 28)"/>'
    f'<path d="M72 50 Q68 56 72 60 Q78 54 74 48Z" fill="#FFD23F" {W(2)}/>')

I["smart-art-lomonosovsky"] = ("#EAFBFF", "#5CC4E0",
    "поролоновый спонж-губка с глазками",
    "прыгает по листу, оставляя за собой цветные отпечатки-облачка",
    f'<rect x="6" y="64" width="116" height="54" rx="4" fill="#fff" {W(3)}/>'
    + "".join(f'<path d="M{x} {y} q-6 0 -6 -6 q0 -7 8 -6 q2 -6 9 -4 q7 -2 8 5 q6 1 4 7 q-1 4 -6 4Z" fill="{c}" opacity=".85"/>'
              for x, y, c in [(20, 106, "#FF5C8A"), (44, 92, "#FFB13B"), (68, 104, "#4CC38A")]) +
    f'<path d="M30 70 Q46 40 60 74 M58 76 Q70 46 88 64" fill="none" stroke="#5CC4E0" stroke-width="2.4" stroke-dasharray="4 4"/>'
    f'<rect x="80" y="30" width="34" height="28" rx="6" fill="#FFE14D" {W(3)} transform="rotate(12 97 44)"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="#E0B800"/>' for x, y in [(86, 34), (108, 40), (90, 52), (104, 54)]) +
    f(97, 44, d=6, k=0.55) +
    f'<path d="M84 60 q-2 -4 2 -6 M110 62 q2 -4 -2 -6" fill="none" {W(2)}/>')

I["istok-teply-stan"] = ("#EEF2FF", "#8A9CE6",
    "самодельный робот-щёткоход из зубной щётки с моторчиком и глазками-бусинами",
    "бегает по столу на щетинках, мальчик хлопает в ладоши",
    f'<rect x="0" y="92" width="128" height="38" fill="#D9A066" {W(2.6)}/>'
    f'<rect x="14" y="68" width="62" height="16" rx="6" fill="#45C1D8" {W(3)}/>'
    + "".join(f'<path d="M{x} 84 l-3 10" stroke="#fff" stroke-width="3"/><path d="M{x} 84 l-3 10" {W(1.2)}/>' for x in range(20, 74, 6)) +
    f'<rect x="38" y="54" width="22" height="16" rx="3" fill="#B6B2C9" {W(2.6)}/><path d="M46 54 V46 M52 54 V46" {W(2)}/>'
    f'<circle cx="46" cy="44" r="3" fill="#E8303A" {W(1.6)}/><circle cx="52" cy="44" r="3" fill="#4CC38A" {W(1.6)}/>'
    + eye(22, 76, 0.55) + eye(30, 76, 0.55) +
    f'<path d="M80 98 h8 M86 104 h6 M8 104 h8" stroke="#fff" stroke-width="2" stroke-linecap="round"/>'
    + kid(100, 50, k=0.85, hair="#F2C14E") +
    f'<path d="M90 62 Q100 58 110 62 L112 90 L88 90Z" fill="#FF8A3D" {W(2.8)}/>'
    f'<path d="M90 66 L98 54 M110 66 L102 54" {W(3)}/>' + sparkle(100, 24, 4, "#FFE14D"))

I["izopark-teply-stan"] = ("#F4FFEC", "#8CCB5E",
    "дерево, у которого вместо листьев — круглые мазки красок всех цветов",
    "девочка стоит у мольберта в парке и дорисовывает последний мазок",
    f'<rect x="18" y="80" width="10" height="36" fill="#8A5A2B" {W(2.6)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="10" fill="{c}" {W(2.4)}/>' for x, y, c in
              [(12, 64, "#FF5C8A"), (24, 50, "#FFB13B"), (40, 60, "#45A8F0"), (30, 70, "#7B5BE0"), (14, 82, "#FFE14D"), (40, 80, "#4CC38A")]) +
    f'<path d="M70 40 L60 116 M100 40 L110 116 M85 40 V110" {W(2.6)}/>'
    f'<rect x="64" y="36" width="42" height="40" rx="2" fill="#fff" {W(2.8)}/>'
    f'<rect x="83" y="64" width="4" height="12" fill="#8A5A2B"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="{c}"/>' for x, y, c in [(78, 54, "#FF5C8A"), (86, 48, "#FFB13B"), (94, 56, "#45A8F0"), (84, 58, "#4CC38A")]) +
    kid(116, 88, k=0.7, hair="#3A2414") + f'<path d="M108 96 Q100 80 98 62" fill="none" {W(2.6)}/>'
    f'<rect x="0" y="114" width="128" height="16" fill="#9FD67C" {W(2.4)}/>')

I["metr-s-kepkoy-teply-stan"] = ("#FFF8EC", "#F2C46B",
    "деревянный ростомер-линейка с красной отметкой «1 м»",
    "малыш в огромной кепке тянется к отметке на цыпочках, кепка почти достаёт",
    f'<rect x="76" y="10" width="22" height="112" rx="3" fill="#F3D59B" {W(3)}/>'
    + "".join(f'<path d="M76 {y} h{8 if y % 20 == 10 else 5}" {W(2)}/>' for y in range(20, 120, 10)) +
    f'<rect x="74" y="34" width="28" height="9" rx="2" fill="#E8303A" {W(2.4)}/>'
    f'<text x="88" y="56" font-family="Arial" font-size="12" font-weight="bold" fill="{O}" text-anchor="middle">1м</text>'
    + kid(50, 60, k=1.05, hair="#6B3F23") +
    f'<path d="M34 54 Q50 30 66 50 L74 50 Q66 56 34 56Z" fill="#45A8F0" {W(2.8)}/>'
    f'<path d="M40 76 Q50 72 60 76 L62 104 L38 104Z" fill="#FFB13B" {W(2.8)}/>'
    f'<path d="M42 104 L42 118 M58 104 L58 118" {W(3.4)}/><ellipse cx="42" cy="120" rx="3" ry="2" fill="{O}"/><ellipse cx="58" cy="120" rx="3" ry="2" fill="{O}"/>')

I["smartikids-solntsevo"] = ("#F2EEFF", "#9E8AE8",
    "три фломастера-друга без колпачков",
    "держатся за руки-колпачки и вместе рисуют на листе радугу",
    f'<rect x="8" y="76" width="112" height="44" rx="4" fill="#fff" {W(3)}/>'
    + "".join(f'<path d="M24 112 Q64 {64+i*8} 104 112" fill="none" stroke="{c}" stroke-width="5" stroke-linecap="round"/>'
              for i, c in enumerate(["#E8303A", "#FFD23F", "#45A8F0"])) +
    "".join(f'<rect x="{x}" y="22" width="16" height="50" rx="5" fill="{c}" {W(2.8)} transform="rotate({r} {x+8} 72)"/>' + f(x + 8, 40, d=3.5, k=0.35)
            for x, c, r in [(28, "#E8303A", 14), (56, "#FFD23F", 0), (84, "#45A8F0", -14)]) +
    f'<path d="M44 46 h12 M72 46 h12" {W(2.6)}/>')

I["gonchar-khudozhnik-tatyanin"] = ("#FFF3E8", "#E59B66",
    "пузатая глиняная вазочка в чёрном берете художника",
    "держит кисточку и палитру и любуется своим портретом на маленьком холсте",
    f'<path d="M40 52 Q24 70 34 102 Q46 116 64 114 Q82 116 92 102 Q102 70 86 52Z" fill="#D88A55" {W(3.2)}/>'
    f'<rect x="46" y="44" width="34" height="10" rx="4" fill="#C2733F" {W(2.6)}/>'
    f'<path d="M42 44 Q50 26 76 30 Q90 34 84 44Z" fill="#2E2A38" {W(2.6)}/><path d="M64 28 l2 -6" {W(2.4)}/>'
    + f(63, 76, d=8, k=0.7) +
    f'<ellipse cx="24" cy="94" rx="14" ry="9" fill="#F7E6C2" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="{c}"/>' for x, y, c in [(18, 92, "#E8303A"), (26, 88, "#45A8F0"), (30, 96, "#FFD23F")]) +
    f'<path d="M96 88 L112 68" stroke="#8A5A2B" stroke-width="3" stroke-linecap="round"/><circle cx="113" cy="66" r="2.6" fill="#4CC38A"/>'
    f'<rect x="98" y="16" width="24" height="30" fill="#fff" {W(2.4)}/><circle cx="110" cy="31" r="7" fill="#D88A55" {W(1.6)}/>')

I["tvorchesky-miks-solntsevo"] = ("#F0FFF8", "#6CCFA8",
    "пушистый разноцветный помпон из ниток с глазками",
    "девочка наматывает на картонное колечко нитку, из которой он и получается",
    f'<circle cx="44" cy="58" r="30" fill="#FF8AB0" {W(3)}/>'
    + "".join(f'<path d="M{44+26*__import__("math").cos(a/4)} {58+26*__import__("math").sin(a/4)} l{6*__import__("math").cos(a/4):.1f} {6*__import__("math").sin(a/4):.1f}" stroke="{c}" stroke-width="3" stroke-linecap="round"/>'
              for a, c in zip(range(25), ["#FFD23F", "#45A8F0", "#4CC38A", "#7B5BE0", "#FF8A3D"] * 5)) +
    f'<path d="M24 50 Q44 40 64 52 M22 66 Q44 56 66 68" fill="none" stroke="#FFD23F" stroke-width="3"/>'
    + f(44, 60, d=7, k=0.65) +
    kid(98, 74, k=0.9, hair="#2B1B12") +
    f'<circle cx="84" cy="102" r="10" fill="none" stroke="#C98B4A" stroke-width="6"/><circle cx="84" cy="102" r="10" fill="none" {W(1.6)}/>'
    f'<path d="M84 92 Q70 80 66 66" fill="none" stroke="#45A8F0" stroke-width="2.4"/>'
    f'<path d="M88 88 Q98 84 108 88 L110 120 L86 120Z" fill="#B392F0" {W(2.8)}/>')

I["stolyarkino-novoperedelkino"] = ("#F7F1E3", "#C6A46C",
    "деревянная машинка-самоделка с колёсами из катушек",
    "мальчик в защитных очках прикручивает отвёрткой последнее колесо",
    f'<rect x="0" y="100" width="128" height="30" fill="#E2C08A" {W(2.6)}/>'
    f'<rect x="16" y="64" width="64" height="22" rx="4" fill="#D9A066" {W(3)}/><rect x="30" y="50" width="30" height="16" rx="3" fill="#E9C38A" {W(2.8)}/>'
    f'<path d="M24 70 h48 M24 78 h48" stroke="#B57A3E" stroke-width="1.6"/>'
    f'<rect x="18" y="82" width="16" height="20" rx="3" fill="#E8303A" {W(2.6)}/><rect x="56" y="82" width="16" height="20" rx="3" fill="#45A8F0" {W(2.6)}/>'
    f'<path d="M18 92 h16 M56 92 h16" {W(2)}/>'
    + eye(38, 58, 0.5) + eye(50, 58, 0.5) +
    kid(100, 60, k=0.85, hair="#C9762E") +
    f'<rect x="88" y="54" width="24" height="8" rx="4" fill="#9FF0FF" opacity=".75" {W(2)}/>'
    f'<path d="M90 72 Q100 68 110 72 L112 100 L88 100Z" fill="#4CC38A" {W(2.8)}/>'
    f'<path d="M90 78 L80 88" {W(3)}/><path d="M80 88 L74 92" stroke="#FFD23F" stroke-width="5" stroke-linecap="round"/><path d="M74 92 L70 94" {W(2)}/>')

I["zolotoy-klyuchik-dmitrovskoe"] = ("#FFF3D6", "#E5A93B",
    "холщовая театральная ширма с нарисованным очагом и котелком",
    "из-за ширмы девочка поднимает перчаточную куклу-петушка, кукла кланяется",
    f'<rect x="12" y="56" width="104" height="62" rx="3" fill="#F3E2BE" {W(3)}/>'
    f'<path d="M12 56 L20 48 H108 L116 56" fill="#C98B4A" {W(2.6)}/>'
    f'<path d="M40 112 V80 Q64 62 88 80 V112Z" fill="#B07A44" {W(2.6)}/>'
    f'<path d="M56 112 Q58 98 64 104 Q70 94 72 112Z" fill="#FF8A3D" {W(2)}/>'
    f'<ellipse cx="64" cy="90" rx="10" ry="7" fill="#5B4A6E" {W(2)}/><path d="M56 86 Q64 80 72 86" fill="none" {W(2)}/>'
    f'<path d="M86 56 V40" {W(3)}/>'
    f'<path d="M78 40 Q72 22 86 14 Q100 18 96 34 Q92 42 78 40Z" fill="#E8303A" {W(2.6)}/>'
    f'<path d="M84 14 l2 -6 3 5 3 -5 1 7" fill="#FFD23F" {W(2)}/><path d="M96 26 l7 2 -6 3Z" fill="#FFD23F" {W(1.8)}/>'
    + eye(90, 24, 0.5) +
    kid(40, 34, k=0.75, hair="#6B3F23"))

I["martynycheva-studio"] = ("#EAF6FF", "#5C9EE0",
    "облако-пузырь со скороговоркой, вылетающее изо рта",
    "мальчик на маленькой сцене выпаливает «Ш-Ш-Ш!», буквы кувыркаются в облаке",
    f'<path d="M44 20 Q46 6 64 10 Q78 2 90 12 Q112 10 112 30 Q122 44 106 54 Q100 66 82 60 Q68 70 56 58 Q38 60 40 44 Q30 32 44 20Z" fill="#fff" {W(3)}/>'
    f'<path d="M58 60 L46 74 L64 64Z" fill="#fff" {W(2.6)}/>'
    f'<text x="76" y="44" font-family="Arial" font-size="20" font-weight="bold" fill="#E8303A" text-anchor="middle" transform="rotate(-8 76 40)">Ш-Ш!</text>'
    + kid(40, 86, k=0.95, hair="#F2C14E") +
    f'<ellipse cx="40" cy="92" rx="4" ry="3" fill="#B83A52"/>'
    f'<path d="M28 98 Q40 94 52 98 L54 116 L26 116Z" fill="#7B5BE0" {W(2.8)}/>'
    f'<rect x="0" y="114" width="128" height="16" fill="#C98B4A" {W(2.6)}/>')

I["lisich-delegatskaya"] = ("#E8F0FF", "#6D8FD8",
    "оконное стекло, расписанное белыми гуашевыми снежинками",
    "девочка в красном свитере стоит на стуле и дорисовывает кисточкой ещё одну снежинку",
    f'<rect x="14" y="12" width="78" height="100" rx="4" fill="#BFD6FF" {W(3.2)}/>'
    f'<path d="M53 12 V112 M14 60 H92" {W(3)}/>'
    + "".join(f'<path d="M{x-7} {y} h14 M{x} {y-7} v14 M{x-5} {y-5} l10 10 M{x+5} {y-5} l-10 10" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'
              for x, y in [(32, 34), (74, 30), (34, 84), (72, 90)]) +
    kid(106, 64, k=0.85, hair="#C9762E") +
    f'<path d="M96 76 Q106 72 116 76 L118 106 L94 106Z" fill="#E8303A" {W(2.8)}/>'
    f'<path d="M96 80 Q86 70 82 56" fill="none" {W(3)}/><rect x="78" y="40" width="4" height="18" rx="2" fill="#8A5A2B" transform="rotate(-20 80 49)"/>'
    f'<rect x="90" y="106" width="32" height="6" fill="#B07A44" {W(2.2)}/><path d="M94 112 V126 M118 112 V126" {W(2.6)}/>')

I["dva-etyuda-tsvetnoy"] = ("#FFF6EC", "#E9A37A",
    "пустая золотая рама-паспарту",
    "девочка держит раму перед лицом, как окошко, и рисует внутри неё сама себя",
    f'<rect x="22" y="22" width="84" height="84" rx="4" fill="#E9B44C" {W(3.2)}/>'
    f'<rect x="34" y="34" width="60" height="60" fill="#FFF3D6" {W(2.6)}/>'
    f'<path d="M22 22 L34 34 M106 22 L94 34 M22 106 L34 94 M106 106 L94 94" {W(2)}/>'
    + kid(64, 64, k=1.2, hair="#3A2414") +
    f'<path d="M24 50 Q14 60 18 80 M104 50 Q114 60 110 80" fill="none" {W(3.2)}/>'
    f'<rect x="108" y="74" width="5" height="22" rx="2" fill="#8A5A2B" transform="rotate(-25 110 85)"/><circle cx="105" cy="74" r="2.4" fill="#E8303A"/>'
    f'<path d="M40 86 q6 4 10 0" fill="none" stroke="#E8303A" stroke-width="2" stroke-dasharray="2 2"/>')

I["ddt-taganka"] = ("#F1ECFF", "#A08AD8",
    "деревянная ткацкая рамка с натянутыми нитями и полосатым ковриком",
    "челнок с красной ниткой бежит между нитями, как маленький кораблик",
    f'<rect x="16" y="16" width="96" height="96" rx="6" fill="#D9A066" {W(3.2)}/>'
    f'<rect x="28" y="28" width="72" height="72" fill="#FFF8EC" {W(2.4)}/>'
    + "".join(f'<path d="M{x} 28 V100" stroke="#C9CBE8" stroke-width="1.6"/>' for x in range(34, 100, 6)) +
    "".join(f'<rect x="28" y="{y}" width="72" height="8" fill="{c}" {W(1.4)}/>' for y, c in [(92, "#4CC38A"), (84, "#FFD23F"), (76, "#45A8F0"), (68, "#FF8A3D")]) +
    f'<path d="M28 64 Q50 56 70 62" fill="none" stroke="#E8303A" stroke-width="3"/>'
    f'<path d="M64 54 L92 54 L100 60 L92 66 L64 66 L56 60Z" fill="#C2733F" {W(2.6)}/>' + f(78, 59, d=5, k=0.4) +
    "".join(f'<circle cx="{x}" cy="22" r="2" fill="#7E5128"/><circle cx="{x}" cy="106" r="2" fill="#7E5128"/>' for x in range(34, 100, 12)))

I["artist-andropova"] = ("#2F2347", "#140C24",
    "гримёрное зеркало с круглыми лампочками по краю",
    "девочка в бумажной короне строит в него смешную рожицу, высунув язык",
    f'<rect x="20" y="14" width="88" height="80" rx="8" fill="#F4E3B5" {W(3.2)}/>'
    f'<rect x="30" y="24" width="68" height="60" rx="4" fill="#BFE0F0" {W(2.6)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#FFF3A6" {W(1.6)}/>' for x, y in
              [(25, 22), (25, 42), (25, 62), (25, 82), (103, 22), (103, 42), (103, 62), (103, 82), (45, 19), (64, 19), (83, 19)]) +
    kid(64, 58, k=1.0, hair="#5A3A22") +
    f'<path d="M50 44 L54 32 L60 40 L64 30 L68 40 L74 32 L78 44Z" fill="#FFD23F" {W(2.2)}/>'
    f'<path d="M62 66 q2 6 4 0" fill="#FF7FA8" {W(1.6)}/>'
    f'<rect x="12" y="94" width="104" height="10" rx="3" fill="#B07A44" {W(2.6)}/>'
    f'<circle cx="36" cy="90" r="4" fill="#FF5C8A" {W(1.6)}/><rect x="84" y="82" width="6" height="12" rx="2" fill="#E8303A" {W(1.6)}/>')

I["senzitivnost-voykovskaya"] = ("#FFF9EB", "#E8C26E",
    "деревянная сенсорная коробка, полная пёстрой фасоли и спрятанных игрушек",
    "малыш погрузил в фасоль обе ручки по локти и нашёл жёлтую уточку-пищалку",
    f'<path d="M14 70 H114 L106 116 H22Z" fill="#C98B4A" {W(3.2)}/>'
    f'<path d="M14 70 Q64 58 114 70" fill="#F0D9A8" {W(2.6)}/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="3.4" ry="2.2" fill="{c}" transform="rotate({r} {x} {y})"/>'
              for x, y, c, r in [(24, 68, "#E8303A", 20), (34, 64, "#5A3A22", -10), (46, 66, "#fff", 30), (82, 64, "#E8303A", -20), (96, 66, "#5A3A22", 10), (106, 68, "#fff", -30), (70, 68, "#8A5A2B", 0), (58, 70, "#E8303A", 40)]) +
    kid(64, 32, k=0.95, hair="#F2C14E") +
    f'<path d="M50 44 L46 64 M78 44 L84 60" {W(3.4)}/>'
    f'<path d="M80 58 Q84 48 94 50 Q100 52 98 58 L104 58 L98 62 Q96 66 86 64Z" fill="#FFD23F" {W(2.4)}/><circle cx="92" cy="54" r="1.4" fill="{O}"/>')

I["radost-mikhalkovskaya"] = ("#FFF0E6", "#F59A62",
    "пара пёстрых маракасов с весёлыми лицами",
    "пляшут крест-накрест, а вокруг разлетаются ноты и горошины",
    f'<g transform="rotate(-24 50 60)"><ellipse cx="50" cy="44" rx="20" ry="24" fill="#FF5C8A" {W(3)}/>'
    f'<path d="M32 40 Q50 50 68 40" fill="none" stroke="#FFD23F" stroke-width="4"/><rect x="46" y="66" width="8" height="40" rx="4" fill="#C98B4A" {W(2.6)}/>'
    + f(50, 44, d=6, k=0.55) + '</g>'
    f'<g transform="rotate(24 80 60)"><ellipse cx="80" cy="44" rx="20" ry="24" fill="#45C1D8" {W(3)}/>'
    f'<path d="M62 40 Q80 50 98 40" fill="none" stroke="#fff" stroke-width="4"/><rect x="76" y="66" width="8" height="40" rx="4" fill="#C98B4A" {W(2.6)}/>'
    + f(80, 44, d=6, k=0.55) + '</g>'
    f'<path d="M14 26 v14" {W(2.4)}/><ellipse cx="10" cy="40" rx="4" ry="3" fill="{O}"/>'
    f'<path d="M112 84 v14" {W(2.4)}/><ellipse cx="108" cy="98" rx="4" ry="3" fill="{O}"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="{c}"/>' for x, y, c in [(20, 70, "#FFD23F"), (110, 24, "#4CC38A"), (30, 110, "#7B5BE0"), (100, 116, "#FFD23F")]))

I["skazochnaya-zhizn-voykovsky"] = ("#F5EEFF", "#B08EE0",
    "волшебный клубок красных ниток с глазками",
    "катится по извилистой тропинке к лесу, за ним шагает девочка в кокошнике",
    f'<path d="M-4 120 Q30 92 60 104 Q90 116 132 84 V130 H-4Z" fill="#9FD67C" {W(2.6)}/>'
    f'<path d="M10 124 Q40 98 64 108 Q88 118 118 94" fill="none" stroke="#F3E2BE" stroke-width="8" stroke-linecap="round"/>'
    + "".join(f'<path d="M{x} {y} l9 -22 9 22Z" fill="#3E9E4F" {W(2.2)}/>' for x, y in [(84, 70), (100, 66), (114, 72)]) +
    f'<circle cx="74" cy="96" r="12" fill="#E8303A" {W(2.8)}/>'
    f'<path d="M64 92 Q74 86 84 94 M64 100 Q74 94 84 102" fill="none" stroke="#B51E28" stroke-width="2"/>'
    + f(74, 96, d=4, k=0.4) + f'<path d="M62 100 Q50 104 40 102" fill="none" stroke="#E8303A" stroke-width="2"/>'
    + kid(32, 62, k=0.9, hair="#C9762E") +
    f'<path d="M20 56 Q32 34 44 56 Q32 50 20 56Z" fill="#E8303A" {W(2.4)}/><circle cx="32" cy="44" r="2.4" fill="#FFD23F"/>'
    f'<path d="M22 74 Q32 70 42 74 L48 104 L16 104Z" fill="#45A8F0" {W(2.8)}/>')

I["apple-family-zheleznyaka"] = ("#EAFBF1", "#6BC59A",
    "три куклы на пальцах — папа с усами, мама с бантом и малыш в шапочке",
    "надеты на детскую ладошку и вместе кланяются",
    f'<path d="M30 128 Q26 96 34 84 L94 84 Q104 96 98 128Z" fill="#FFD9B8" {W(3)}/>'
    f'<path d="M24 92 Q14 80 20 70 Q28 68 32 84" fill="#FFD9B8" {W(2.8)}/>'
    + "".join(f'<rect x="{x-10}" y="{y}" width="20" height="{94-y}" rx="10" fill="{c}" {W(2.8)}/>' + f(x, y + 14, d=4, k=0.4)
              for x, y, c in [(44, 34, "#45A8F0"), (64, 28, "#FF8AB0"), (84, 46, "#FFD23F")]) +
    f'<path d="M38 52 q6 4 12 0" fill="none" {W(2.4)}/>'
    f'<path d="M58 30 l-6 -6 0 10Z M70 30 l6 -6 0 10Z" fill="#E8303A" {W(2)}/>'
    f'<path d="M74 50 Q84 34 94 50Z" fill="#4CC38A" {W(2.2)}/><circle cx="84" cy="38" r="3" fill="#fff" {W(1.6)}/>')

I["artkash-school"] = ("#F2F2F6", "#A2A6B8",
    "угольная палочка художника с глазками",
    "рисует на большом листе кота и испачкала себе нос чёрным",
    f'<rect x="8" y="16" width="86" height="104" rx="3" fill="#fff" {W(3)}/>'
    f'<path d="M30 96 Q24 70 40 62 L36 46 L48 56 Q56 52 64 56 L74 44 L72 62 Q86 72 78 96Z" fill="none" stroke="#2E2A38" stroke-width="3" stroke-linejoin="round"/>'
    f'<path d="M78 92 Q92 90 88 76" fill="none" stroke="#2E2A38" stroke-width="3" stroke-linecap="round"/>'
    f'<circle cx="46" cy="72" r="2" fill="#2E2A38"/><circle cx="62" cy="72" r="2" fill="#2E2A38"/>'
    f'<rect x="96" y="30" width="14" height="64" rx="5" fill="#3B3846" {W(2.6)} transform="rotate(22 103 62)"/>'
    + eye(104, 52, 0.5) + eye(112, 55, 0.5) +
    f'<ellipse cx="106" cy="62" rx="4" ry="3" fill="#111"/>'
    f'<path d="M84 92 q4 4 8 2" fill="none" stroke="#2E2A38" stroke-width="2"/>')

I["masterskaya-talantov-marksistskaya"] = ("#FFF6F0", "#EE8F7A",
    "детские красные ножницы с закруглёнными концами и глазками на винтике",
    "вырезают из сложенного голубого листа ажурную бумажную звезду, вокруг летят обрезки",
    f'<path d="M14 74 l12 -24 26 -4 -20 -16 6 -26 -22 14 -22 -14 6 26 -20 16 26 4Z" fill="#9FD4FF" {W(3)} transform="translate(44 40)"/>'
    f'<circle cx="58" cy="44" r="5" fill="#FFF6F0" {W(2)}/><circle cx="36" cy="62" r="4" fill="#FFF6F0" {W(2)}/><circle cx="76" cy="66" r="4" fill="#FFF6F0" {W(2)}/>'
    f'<path d="M56 74 l6 -8 6 8Z" fill="#FFF6F0" {W(2)}/>'
    f'<path d="M80 92 L116 36" stroke="#C9CBE8" stroke-width="7" stroke-linecap="round"/><path d="M80 92 L116 36" {W(1.6)}/>'
    f'<path d="M84 80 L118 98" stroke="#C9CBE8" stroke-width="7" stroke-linecap="round"/><path d="M84 80 L118 98" {W(1.6)}/>'
    f'<ellipse cx="74" cy="106" rx="9" ry="12" fill="none" stroke="#E8303A" stroke-width="6"/><ellipse cx="74" cy="106" rx="9" ry="12" fill="none" {W(1.6)}/>'
    f'<ellipse cx="102" cy="112" rx="12" ry="9" fill="none" stroke="#E8303A" stroke-width="6"/><ellipse cx="102" cy="112" rx="12" ry="9" fill="none" {W(1.6)}/>'
    f'<circle cx="88" cy="86" r="4" fill="#FFD23F" {W(2)}/>' + eye(84, 78, 0.45) + eye(94, 80, 0.45) +
    "".join(f'<path d="M{x} {y} l5 2 -3 4Z" fill="#9FD4FF" {W(1.4)}/>' for x, y in [(20, 104), (30, 116), (110, 20), (100, 12)]))

I["tsentr-kreativa-babyegorodsky"] = ("#EAF6FF", "#64A8E6",
    "робот из картонных коробок с глазами-крышками от бутылок",
    "девочка приклеивает ему руку-трубочку широким скотчем",
    f'<rect x="20" y="22" width="40" height="32" rx="2" fill="#D9A066" {W(3)}/>'
    f'<circle cx="32" cy="38" r="7" fill="#E8303A" {W(2.4)}/><circle cx="50" cy="38" r="7" fill="#45A8F0" {W(2.4)}/>'
    f'<circle cx="32" cy="38" r="2.4" fill="#fff"/><circle cx="50" cy="38" r="2.4" fill="#fff"/>'
    f'<path d="M40 22 V12" {W(2.4)}/><circle cx="40" cy="10" r="3" fill="#FFD23F" {W(1.8)}/>'
    f'<rect x="14" y="54" width="52" height="46" rx="2" fill="#C98B4A" {W(3)}/>'
    f'<rect x="26" y="64" width="28" height="16" fill="#fff" {W(2)}/><path d="M30 72 h4 M38 72 h4 M46 72 h4" {W(2)}/>'
    f'<rect x="22" y="100" width="12" height="16" fill="#D9A066" {W(2.4)}/><rect x="46" y="100" width="12" height="16" fill="#D9A066" {W(2.4)}/>'
    f'<rect x="66" y="60" width="26" height="9" rx="4.5" fill="#E3E6EE" {W(2.4)}/>'
    f'<rect x="62" y="56" width="10" height="16" fill="#BFE8FF" opacity=".8" {W(1.6)}/>'
    + kid(104, 72, k=0.85, hair="#3A2414") +
    f'<path d="M94 84 Q104 80 114 84 L116 116 L92 116Z" fill="#FFB13B" {W(2.8)}/>'
    f'<path d="M94 88 L74 66" {W(3)}/>')
if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        a, b, hero, scene, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
