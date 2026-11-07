"""Иконки робота fun (2026-11-07, вечер 2): 17 мест. Каждая придумана отдельно (правило абсолютной уникальности).
Сверено с каталогом и icons-src/subjects.txt (заняты: ступа, Емеля, клубок, паровозик, светофор, лорнет, соловей,
кинохлопушка, кенгуру, автомат-хваталка, песочные часы, ключи, 3D-очки, НЛО, комета, амфора — не брать).
Запуск: python3 tools/icons_fun_1107f.py [id ...]  (печатает строки для subjects.txt)"""
import os, sys, math
from draw_icons import s, eye, face, sparkle, O

W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=9, k=0.75, **kw: face(cx, cy, d=d, k=k, **kw)
sp = lambda *pts: "".join(sparkle(x, y, r) for x, y, r in pts)
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
GO = "#F2B632"


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


def closed_eye(x, y, k=1.0):
    return f'<path d="M{x-4*k} {y} Q{x} {y-5*k} {x+4*k} {y}" fill="none" {W(2.6*k)}/>'


I = {}


def rr(x, y, w, h, r, fill, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" {s()} {extra}/>'


# 1. Пластилин — брусок пластилина лепит пирамиду
I["plastilin-museum"] = ("#FFF1D6", "#F39A3A",
    "разноцветный полосатый брусок пластилина с глазками", "лепит на деревянной дощечке крошечную египетскую пирамиду из пластилиновых колбасок",
    f'<rect x="8" y="98" width="112" height="16" rx="4" fill="#C98B4E" {s()}/>'
    f'<path d="M70 98 L92 62 L114 98Z" fill="#F7C948" {s()}/>'
    + "".join(f'<path d="M{70+i*4} {98-i*7.2} H{114-i*4}" stroke="#D9A21E" stroke-width="2.4"/>' for i in range(1, 5))
    + f'<g transform="rotate(-8 40 70)">'
    + rr(16, 46, 48, 50, 8, "#4E9BE0")
    + f'<rect x="16" y="46" width="16" height="50" fill="#E8453C" {s()}/><rect x="32" y="46" width="16" height="50" fill="#5DBB5A" {s()}/>'
    + rr(16, 46, 48, 50, 8, "none")
    + f'</g>'
    + f'<g>{f(40, 66, d=8, k=0.75)}</g>'
    + f'<path d="M62 82 Q72 74 80 80" fill="none" stroke="#5DBB5A" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M62 82 Q72 74 80 80" fill="none" {W(1.6)}/>'
    + sp((24, 26, 5), (102, 34, 4)))

# 2. Музей леса — срез бревна с годовыми кольцами
I["forest-museum"] = ("#D8F2CF", "#2F7A3E",
    "срез бревна с годовыми кольцами вместо лица", "стоит среди ёлок, из макушки пробивается зелёный росток с двумя листочками",
    "".join(f'<path d="M{x} {y} l-14 26 h28Z M{x} {y-14} l-11 20 h22Z" fill="#1F5E30" {W(2.4)}/>' for x, y in [(14, 72), (114, 70)])
    + f'<path d="M0 108 Q64 96 128 108 V128 H0Z" fill="#7A5A3A" {s()}/>'
    + f'<ellipse cx="64" cy="70" rx="40" ry="38" fill="#B5763A" {s()}/>'
    + f'<ellipse cx="64" cy="70" rx="33" ry="31" fill="#F3D7A2" {W(2.4)}/>'
    + "".join(f'<ellipse cx="{64+i*0.6}" cy="{70+i*0.4}" rx="{33-i*6}" ry="{31-i*5.6}" fill="none" stroke="#D2A86A" stroke-width="2"/>' for i in range(1, 5))
    + f'<g>{f(64, 68, d=11, k=0.8)}</g>'
    + f'<path d="M64 32 V18" stroke="#3E8E3E" stroke-width="4" stroke-linecap="round"/>'
    + f'<path d="M64 22 Q50 10 44 20 Q54 28 64 22Z M64 20 Q78 6 86 16 Q76 26 64 20Z" fill="#6CC45C" {W(2.2)}/>'
    + sp((30, 30, 4), (100, 28, 3)))

# 3. Особняк-Небылица — мухомор с дверцей
I["nebylitsa-museum"] = ("#B9A2F0", "#3E2A7A",
    "большой красный мухомор с резной дверцей и окошком", "стоит на сказочной ночной поляне, в окошке горит тёплый свет",
    f'<path d="M0 104 Q64 92 128 104 V128 H0Z" fill="#3C8E4A" {s()}/>'
    + f'<path d="M44 108 Q40 76 48 62 H80 Q88 76 84 108Z" fill="#FFF4E0" {s()}/>'
    + f'<path d="M14 64 Q16 18 64 16 Q112 18 114 64 Q64 76 14 64Z" fill="#E8302E" {s()}/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r*0.8}" fill="#fff" {W(1.6)}/>' for x, y, r in [(40, 34, 6), (66, 26, 5), (90, 38, 7), (28, 54, 4), (100, 56, 4), (60, 48, 4)])
    + f'<path d="M56 108 V90 Q64 80 72 90 V108Z" fill="#9C5E34" {s()}/><circle cx="69" cy="98" r="1.8" fill="{O}"/>'
    + f'<circle cx="64" cy="72" r="6" fill="#FFD54A" {W(2.2)}/><path d="M58 72 H70 M64 66 V78" stroke="{O}" stroke-width="1.6"/>'
    + eye(52, 80, 0.55) + eye(76, 80, 0.55)
    + "".join(sparkle(x, y, r, "#FFF3A0") for x, y, r in [(18, 20, 4), (110, 22, 3), (100, 90, 3), (22, 88, 2.4)]))

# 4. Паровозное депо — семафор с крылом
I["depo-podmoskovnaya"] = ("#E1F3FF", "#5A9FD8",
    "старинный железнодорожный семафор с полосатым крылом и глазами-фонарями", "поднял крыло, пропуская облачко паровозного пара над рельсами",
    f'<path d="M0 112 H128 M0 122 H128" stroke="#6A5A4A" stroke-width="4"/>'
    + "".join(f'<rect x="{x}" y="106" width="6" height="22" fill="#8A6A4A"/>' for x in range(4, 128, 16))
    + f'<rect x="58" y="34" width="10" height="76" fill="#4A4D5C" {s()}/>'
    + f'<path d="M50 112 H76" stroke="{O}" stroke-width="6" stroke-linecap="round"/>'
    + f'<g transform="rotate(-35 63 40)"><rect x="63" y="34" width="54" height="12" rx="3" fill="#E8453C" {s()}/>'
    + "".join(f'<rect x="{x}" y="34" width="7" height="12" fill="#fff"/>' for x in (74, 90, 106))
    + f'<rect x="63" y="34" width="54" height="12" rx="3" fill="none" {s()}/></g>'
    + rr(38, 44, 26, 44, 8, "#2E2E36")
    + f'<circle cx="51" cy="56" r="7" fill="#FF5A4A" {W(2)}/><circle cx="51" cy="76" r="7" fill="#6CE07A" {W(2)}/>'
    + eye(49, 57, 0.5) + eye(49, 77, 0.5)
    + f'<path d="M20 30 Q12 20 22 16 Q24 6 36 10 Q46 4 50 14 Q60 16 54 26 Q40 32 20 30Z" fill="#fff" {W(2.2)}/>'
    + sp((104, 86, 4)))

# 5. Бункер Сталина — гермодверь
I["bunker-stalina"] = ("#B7C3C9", "#3E4C56",
    "толстая круглая стальная гермодверь с рулём-штурвалом", "приоткрывается в подземный тоннель, из щели светит тёплая лампочка",
    f'<rect x="0" y="0" width="128" height="128" fill="#55626C"/>'
    + "".join(f'<path d="M0 {y} H128" stroke="#4A565F" stroke-width="2"/>' for y in (20, 44, 68, 92, 116))
    + f'<circle cx="64" cy="64" r="48" fill="#2A2E38" {s()}/>'
    + f'<path d="M64 16 A48 48 0 0 1 64 112Z" fill="#FFE9A0"/>'
    + f'<circle cx="80" cy="30" r="5" fill="#FFD54A"/>'
    + f'<g transform="translate(-14 0)"><circle cx="64" cy="64" r="42" fill="#8E9AA6" {s()}/>'
    + f'<circle cx="64" cy="64" r="34" fill="#A8B3BE" {W(2.4)}/>'
    + "".join(f'<circle cx="{64+38*math.cos(math.radians(a)):.1f}" cy="{64+38*math.sin(math.radians(a)):.1f}" r="2.4" fill="#5A6470"/>' for a in range(0, 360, 30))
    + f'<circle cx="64" cy="64" r="18" fill="none" stroke="#C4302B" stroke-width="5"/>'
    + "".join(f'<path d="M64 64 L{64+18*math.cos(math.radians(a)):.1f} {64+18*math.sin(math.radians(a)):.1f}" stroke="#C4302B" stroke-width="4"/>' for a in (45, 135, 225, 315))
    + f'<circle cx="64" cy="64" r="5" fill="#C4302B" {W(1.6)}/>'
    + f'{f(64, 90, d=9, k=0.6)}</g>')

# 6. Музей наивного искусства — лоскутное одеяло
PATCH = ["#FF8A9A", "#FFD25E", "#7CC8F0", "#8ED46A", "#C49AF0", "#FFA45C"]
I["naive-museum-soyuzny"] = ("#FFF0E8", "#F2A0A8",
    "лоскутное одеяло-персонаж из ярких квадратиков", "сушится на бельевой верёвке в деревенском дворике под наивным круглым солнцем",
    f'<circle cx="104" cy="22" r="11" fill="#FFD23C" {W(2.2)}/>'
    + f'<path d="M0 30 Q64 44 128 30" fill="none" stroke="{O}" stroke-width="2.4"/>'
    + f'<path d="M0 104 Q64 96 128 104 V128 H0Z" fill="#9AD27A" {s()}/>'
    + "".join(f'<rect x="{22+(i%4)*21}" y="{38+(i//4)*21}" width="21" height="21" fill="{PATCH[(i*5)%6]}" {W(2)}/>' for i in range(12))
    + "".join(f'<path d="M{x} {y} l4 4 m0 -4 l-4 4" stroke="#fff" stroke-width="1.6"/>' for x, y in [(30, 46), (72, 66), (94, 88), (50, 88)])
    + f'<rect x="22" y="38" width="84" height="63" fill="none" {s()}/>'
    + "".join(f'<rect x="{x}" y="32" width="6" height="12" rx="2" fill="#C98B4E" {W(1.8)}/>' for x in (30, 60, 92))
    + f'<g>{f(64, 64, d=10, k=0.8)}</g>'
    + sp((14, 64, 4)))

# 7. Музей писем Чехова — почтовая марка
I["chekhov-letters-museum"] = ("#EAF2FF", "#8FA9D8",
    "почтовая марка с зубчатыми краями и нарисованным пенсне", "приклеивается к белому конверту, рядом ложится круглый почтовый штемпель",
    f'<path d="M6 54 L100 34 L122 104 L28 124Z" fill="#FFFFFF" {s()}/>'
    + f'<path d="M6 54 L64 92 L100 34" fill="none" stroke="#C8D2E4" stroke-width="2.4"/>'
    + f'<g transform="rotate(-10 64 60)">'
    + f'<rect x="40" y="26" width="48" height="58" fill="#FFF7E2" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="26" r="2.8" fill="#8FA9D8"/><circle cx="{x}" cy="84" r="2.8" fill="#8FA9D8"/>' for x in range(42, 90, 7))
    + "".join(f'<circle cx="40" cy="{y}" r="2.8" fill="#8FA9D8"/><circle cx="88" cy="{y}" r="2.8" fill="#8FA9D8"/>' for y in range(30, 84, 7))
    + f'<rect x="46" y="32" width="36" height="46" fill="#7DB8E8" {W(2)}/>'
    + f'<circle cx="57" cy="52" r="6" fill="none" {W(2.4)}/><circle cx="71" cy="52" r="6" fill="none" {W(2.4)}/><path d="M63 52 H65 M57 46 Q58 38 64 36" fill="none" {W(1.8)}/>'
    + f'{f(64, 66, d=6, k=0.5)}</g>'
    + f'<circle cx="96" cy="86" r="14" fill="none" stroke="#5A6EA8" stroke-width="2.6" stroke-dasharray="4 3"/>'
    + f'<path d="M86 84 q5 -5 10 0 t10 0" fill="none" stroke="#5A6EA8" stroke-width="2.4"/>'
    + sp((18, 24, 4), (112, 22, 3)))

# 8. Театр Юного Москвича — марионетка
I["tyum-theatre"] = ("#FFD6EF", "#C2307E",
    "деревянная кукла-марионетка в красном колпачке на ниточках", "пляшет на маленькой сцене, а ниточки тянутся вверх к деревянной крестовине",
    f'<rect x="0" y="104" width="128" height="24" fill="#8A4A2A" {s()}/>'
    + f'<path d="M38 12 H90 M64 4 V20" stroke="#B5763A" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M38 12 H90 M64 4 V20" fill="none" {W(1.6)}/>'
    + "".join(f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#fff" stroke-width="1.4"/>' for x1, y1, x2, y2 in [(38, 12, 34, 62), (90, 12, 96, 58), (64, 20, 64, 30), (48, 12, 50, 100), (80, 12, 80, 100)])
    + f'<path d="M50 70 L44 100 M78 70 L82 100" stroke="#E0A86A" stroke-width="7" stroke-linecap="round"/>'
    + f'<circle cx="44" cy="102" r="5" fill="#2E2E36"/><circle cx="82" cy="102" r="5" fill="#2E2E36"/>'
    + f'<path d="M48 52 L34 62 M80 52 L96 58" stroke="#E0A86A" stroke-width="6" stroke-linecap="round"/>'
    + f'<path d="M48 48 H80 L84 74 H44Z" fill="#3E7FC8" {s()}/>'
    + f'<circle cx="64" cy="40" r="13" fill="#F3C89A" {s()}/>'
    + f'<path d="M50 34 Q64 10 82 34Z" fill="#E8302E" {s()}/><circle cx="82" cy="30" r="3.6" fill="#fff" {W(1.4)}/>'
    + f'{f(64, 42, d=5, k=0.5)}'
    + sp((18, 40, 4), (110, 80, 3)))

# 9. Театр Российской армии — театр-звезда
def star(cx, cy, R, r):
    return " ".join(f'{cx+(R if i%2==0 else r)*math.cos(math.radians(-90+i*36)):.1f},{cy+(R if i%2==0 else r)*math.sin(math.radians(-90+i*36)):.1f}' for i in range(10))
I["teatr-armii"] = ("#5B6FC8", "#1A2260",
    "пятиконечная звезда-театр с белыми колоннами по краю", "сияет на зелёной площади, а над ней рассыпается праздничный салют",
    f'<path d="M0 110 Q64 100 128 110 V128 H0Z" fill="#4E9A54" {s()}/>'
    + f'<polygon points="{star(64, 70, 48, 21)}" fill="#E9E2D0" {s()}/>'
    + f'<polygon points="{star(64, 70, 34, 15)}" fill="#D84A3C" {W(2)}/>'
    + "".join(f'<path d="M{64+30*math.cos(math.radians(-90+i*72+36)):.1f} {70+30*math.sin(math.radians(-90+i*72+36)):.1f} l0 0" stroke="#fff" stroke-width="5" stroke-linecap="round"/>' for i in range(5))
    + "".join(f'<rect x="{x}" y="96" width="4" height="12" fill="#fff" {W(1.2)}/>' for x in (54, 62, 70))
    + f'{f(64, 70, d=8, k=0.75)}'
    + "".join(f'<path d="M{cx} {cy} l{dx} {dy}" stroke="{c}" stroke-width="2.6" stroke-linecap="round"/>' for cx, cy, c in [(22, 26, "#FFD54A"), (104, 22, "#FF8AC8")] for dx, dy in [(8, 0), (-8, 0), (0, 8), (0, -8), (6, 6), (-6, -6), (6, -6), (-6, 6)]))

# 10. Новая Опера — поющая люстра
I["novaya-opera"] = ("#FFB8B0", "#7A1430",
    "хрустальная люстра с подвесками-капельками", "поёт, раскачиваясь под расписным потолком зрительного зала, а вокруг вылетают ноты",
    f'<path d="M64 0 V24" stroke="{GO}" stroke-width="4"/>'
    + f'<path d="M24 52 Q64 76 104 52" fill="none" stroke="{GO}" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M24 52 Q64 76 104 52" fill="none" {W(1.4)}/>'
    + f'<ellipse cx="64" cy="42" rx="22" ry="20" fill="#FFE7A0" {s()}/>'
    + "".join(f'<path d="M{x} {y} v10" stroke="#fff" stroke-width="1.4"/><path d="M{x} {y+10} l-4 6 4 6 4 -6Z" fill="#DDF4FF" {W(1.6)}/>' for x, y in [(28, 56), (44, 64), (64, 66), (84, 64), (100, 56)])
    + "".join(f'<path d="M{x} 52 v-10" stroke="#FFF6D0" stroke-width="5" stroke-linecap="round"/><ellipse cx="{x}" cy="38" rx="3" ry="5" fill="#FFB02E"/>' for x in (24, 104))
    + f'{f(64, 40, d=7, k=0.6, mouth=False)}'
    + f'<ellipse cx="64" cy="50" rx="4" ry="5" fill="#C4302B" {W(1.6)}/>'
    + "".join(f'<path d="M{x} {y} v-14 l8 -3 v14" fill="none" stroke="#FFE7A0" stroke-width="2.4"/><ellipse cx="{x-3}" cy="{y}" rx="3.6" ry="3" fill="#FFE7A0"/><ellipse cx="{x+5}" cy="{y-3}" rx="3.6" ry="3" fill="#FFE7A0"/>' for x, y in [(22, 104), (98, 100)])
    + sp((60, 112, 4)))

# 11. Камерная сцена Покровского — муха в сарафане
I["pokrovsky-chamber"] = ("#F4FFD0", "#9CCB3A",
    "муха в цветастом сарафане с прозрачными крылышками", "нашла на лужайке блестящую денежку и пляшет, подняв её над головой",
    f'<path d="M0 104 Q64 94 128 104 V128 H0Z" fill="#6DAE3A" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="{c}" {W(1.4)}/><circle cx="{x}" cy="{y}" r="1.4" fill="#FFD23C"/>' for x, y, c in [(16, 112, "#fff"), (108, 114, "#FF8AC8"), (34, 120, "#fff")])
    + f'<ellipse cx="38" cy="58" rx="22" ry="12" fill="#E6F6FF" opacity=".9" transform="rotate(-30 38 58)" {W(2.2)}/>'
    + f'<ellipse cx="90" cy="58" rx="22" ry="12" fill="#E6F6FF" opacity=".9" transform="rotate(30 90 58)" {W(2.2)}/>'
    + f'<path d="M48 64 Q64 58 80 64 L90 100 Q64 108 38 100Z" fill="#E8453C" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#FFE27A"/>' for x, y in [(52, 80), (66, 90), (78, 78), (58, 98), (82, 96)])
    + f'<path d="M54 100 L50 112 M74 100 L78 112" stroke="{O}" stroke-width="3" stroke-linecap="round"/>'
    + f'<circle cx="64" cy="48" r="16" fill="#3B3F5C" {s()}/>'
    + f'<circle cx="56" cy="46" r="6" fill="#9AD8FF" {W(1.6)}/><circle cx="72" cy="46" r="6" fill="#9AD8FF" {W(1.6)}/>'
    + eye(56, 46, 0.55) + eye(72, 46, 0.55)
    + f'<path d="M58 56 Q64 60 70 56" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>'
    + f'<path d="M50 70 L36 40 M78 70 L92 40" stroke="#3B3F5C" stroke-width="4" stroke-linecap="round"/>'
    + f'<circle cx="94" cy="32" r="9" fill="{GO}" {s()}/><path d="M91 30 h6 M94 27 v7" stroke="#B5801A" stroke-width="2"/>'
    + sp((112, 18, 4), (82, 22, 3)))

# 12. Центр Михалкова — мегафон
I["mikhalkov-centre-pilyugina"] = ("#FFF8C8", "#F2B72E",
    "красный режиссёрский мегафон-рупор с ручкой", "командует «Мотор!» над съёмочной площадкой, из раструба вылетают звёздочки",
    f'<path d="M0 108 H128 V128 H0Z" fill="#7A5A3A" {s()}/>'
    + "".join(f'<path d="M{x} 108 L{x+8} 84 M{x+16} 108 L{x+8} 84 M{x+2} 96 H{x+14}" stroke="#3B3355" stroke-width="3" stroke-linecap="round"/><rect x="{x}" y="76" width="16" height="8" fill="#2E2E36"/>' for x in (12, 100))
    + f'<g transform="rotate(-14 60 60)">'
    + f'<path d="M30 52 L86 30 L86 94 L30 72Z" fill="#E8302E" {s()}/>'
    + f'<ellipse cx="86" cy="62" rx="8" ry="32" fill="#FF6A5A" {s()}/>'
    + rr(18, 50, 14, 24, 4, "#F4F4F4")
    + f'<path d="M48 72 L44 92 H56 L58 70" fill="#3B3355" {W(2)}/>'
    + f'{f(54, 60, d=8, k=0.7)}</g>'
    + "".join(sparkle(x, y, r, c) for x, y, r, c in [(108, 30, 6, "#fff"), (114, 58, 4, "#E8302E"), (100, 12, 4, "#fff"), (116, 82, 3, "#fff")]))

# 13. Кенга и Ко — парик на болванке
I["kenga-theatre"] = ("#F3E4FF", "#B78AE6",
    "пышный кудрявый театральный парик на деревянной болванке", "сидит на гримёрном столике среди баночек грима и пуховки",
    f'<rect x="0" y="96" width="128" height="32" fill="#C98B4E" {s()}/>'
    + rr(42, 82, 44, 16, 4, "#B5763A")
    + f'<ellipse cx="64" cy="62" rx="20" ry="26" fill="#E8C9A0" {s()}/>'
    + "".join(f'<circle cx="{64+30*math.cos(math.radians(a)):.1f}" cy="{54+28*math.sin(math.radians(a)):.1f}" r="11" fill="#F7E07A" {W(2.4)}/>' for a in range(150, 400, 22))
    + f'<ellipse cx="64" cy="36" rx="22" ry="14" fill="#F7E07A" {W(2.4)}/>'
    + "".join(f'<path d="M{x} {y} q4 -6 8 0" fill="none" stroke="#D9B640" stroke-width="2"/>' for x, y in [(50, 34), (64, 30), (72, 38), (40, 56), (82, 60)])
    + f'{f(64, 66, d=8, k=0.7)}'
    + rr(10, 84, 14, 12, 3, "#FF8AC8") + rr(98, 82, 18, 14, 3, "#7CC8F0")
    + f'<circle cx="107" cy="78" r="8" fill="#FFF4F8" {W(2)}/>'
    + sp((20, 30, 5), (110, 30, 3)))

# 14. Zамания 4Daily — аркадный автомат
I["zamania-4daily"] = ("#D6FBFF", "#28A9C6",
    "аркадный игровой автомат с джойстиком и большой красной кнопкой", "подмигивает светящимся экраном в игровом зале, по экрану бежит пиксельная змейка",
    f'<path d="M30 116 V28 Q30 14 44 14 H84 Q98 14 98 28 V116Z" fill="#7B4AE0" {s()}/>'
    + rr(38, 24, 52, 40, 6, "#1C2340")
    + "".join(f'<rect x="{x}" y="{y}" width="5" height="5" fill="#6CE07A"/>' for x, y in [(46, 52), (51, 52), (56, 52), (56, 47), (61, 47), (66, 47)])
    + f'<rect x="76" y="34" width="5" height="5" fill="#FF6A6A"/>'
    + f'<ellipse cx="54" cy="36" rx="4" ry="5" fill="#fff"/><circle cx="55" cy="37" r="2.2" fill="{O}"/>'
    + f'<path d="M68 36 q4 -4 8 0" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'
    + f'<path d="M30 70 H98 L104 86 H24Z" fill="#9B6CF0" {s()}/>'
    + f'<path d="M46 78 V66" stroke="{O}" stroke-width="4"/><circle cx="46" cy="64" r="5" fill="#FFD23C" {W(2)}/>'
    + f'<ellipse cx="78" cy="78" rx="8" ry="5" fill="#E8302E" {W(2.2)}/>'
    + f'<rect x="54" y="96" width="20" height="6" rx="2" fill="#1C2340"/>'
    + f'<path d="M0 116 H128 V128 H0Z" fill="#2A3A6A"/>'
    + sp((14, 40, 5), (114, 60, 4), (112, 24, 3)))

# 15. Quest Reality — кодовый замок
I["quest-reality-chistye"] = ("#DFFFF0", "#3BB38A",
    "навесной кодовый замок с крутящимися цифровыми колёсиками", "висит на загадочной зелёной двери, колёсики подбирают код 7-1-4",
    f'<rect x="14" y="0" width="100" height="128" fill="#2E8A66" {s()}/>'
    + "".join(f'<path d="M14 {y} H114" stroke="#267556" stroke-width="2"/>' for y in (30, 64, 98))
    + f'<rect x="10" y="40" width="22" height="8" rx="3" fill="#8A8A96" {W(2)}/>'
    + f'<path d="M44 58 V40 Q44 20 64 20 Q84 20 84 40 V58" fill="none" stroke="{O}" stroke-width="12"/>'
    + f'<path d="M44 58 V40 Q44 20 64 20 Q84 20 84 40 V58" fill="none" stroke="#C8CED8" stroke-width="7"/>'
    + rr(32, 54, 64, 54, 10, "#F2B632")
    + "".join(rr(40 + i * 17, 70, 14, 22, 3, "#FFFDF0") + f'<text x="{47+i*17}" y="87" font-size="15" font-family="Arial" font-weight="700" fill="{O}" text-anchor="middle">{d}</text>' for i, d in enumerate("714"))
    + eye(52, 62, 0.5) + eye(76, 62, 0.5)
    + f'<path d="M58 100 Q64 104 70 100" fill="none" {W(2)}/>'
    + sp((104, 20, 5), (110, 112, 3)))

# 16. Студия «Академия» — античная колонна
I["studia-academia"] = ("#FFF6E2", "#D9B47A",
    "белая античная колонна с завитками-капителью", "держит на макушке лавровый венок и развёрнутый свиток на фоне греческого орнамента",
    "".join(f'<path d="M{x} 118 v-8 h8 v4 h-4 v-4" fill="none" stroke="#B88A4A" stroke-width="2"/>' for x in range(0, 128, 12))
    + f'<path d="M0 104 H128" stroke="#B88A4A" stroke-width="2"/>'
    + rr(36, 96, 56, 12, 2, "#F4EFE6")
    + f'<rect x="44" y="44" width="40" height="52" fill="#FBF8F2" {s()}/>'
    + "".join(f'<path d="M{x} 46 V94" stroke="#D8CFC0" stroke-width="2"/>' for x in (52, 60, 68, 76))
    + f'<path d="M34 34 H94 V44 H34Z" fill="#F4EFE6" {s()}/>'
    + f'<circle cx="36" cy="40" r="7" fill="#F4EFE6" {s()}/><circle cx="92" cy="40" r="7" fill="#F4EFE6" {s()}/>'
    + f'<path d="M33 40 a3 3 0 1 1 3 3 M95 40 a3 3 0 1 0 -3 3" fill="none" {W(1.6)}/>'
    + f'{f(64, 66, d=8, k=0.7)}'
    + f'<path d="M44 24 Q64 4 84 24" fill="none" stroke="#5DA04A" stroke-width="3"/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="5" ry="2.6" fill="#6CC45C" transform="rotate({r} {x} {y})" {W(1.2)}/>' for x, y, r in [(48, 18, -40), (56, 12, -20), (72, 12, 20), (80, 18, 40)])
    + f'<path d="M98 56 H120 V84 H98Z" fill="#FFF3D0" {W(2.2)}/><path d="M102 64 H116 M102 70 H116 M102 76 H112" stroke="#B88A4A" stroke-width="1.6"/>'
    + sp((16, 40, 4)))

# 17. Космик (Сергиев Посад) — киноплёнка в космосе
I["kosmik-sergiev-posad"] = ("#4A3E9A", "#120E30",
    "рулон киноплёнки с дырочками по краям", "разматывается змейкой по звёздному космосу, на кадриках — планеты и звёзды",
    "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".8"/>' for x, y, r in [(14, 40, 1.6), (30, 104, 1.2), (110, 98, 1.6), (96, 18, 1.2), (60, 116, 1.4)])
    + f'<path d="M30 46 Q58 30 76 52 Q96 76 116 64" fill="none" stroke="{O}" stroke-width="26"/>'
    + f'<path d="M30 46 Q58 30 76 52 Q96 76 116 64" fill="none" stroke="#2E2E36" stroke-width="20"/>'
    + f'<path d="M30 46 Q58 30 76 52 Q96 76 116 64" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="3 5" transform="translate(0 -7)"/>'
    + f'<path d="M30 46 Q58 30 76 52 Q96 76 116 64" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="3 5" transform="translate(0 7)"/>'
    + f'<circle cx="56" cy="40" r="5" fill="#FF9A4A"/><circle cx="96" cy="66" r="4" fill="#7CD8FF"/>'
    + f'<circle cx="34" cy="76" r="26" fill="#3A3A46" {s()}/><circle cx="34" cy="76" r="20" fill="#55556A" {W(2)}/>'
    + "".join(f'<circle cx="{34+11*math.cos(math.radians(a)):.1f}" cy="{76+11*math.sin(math.radians(a)):.1f}" r="4.4" fill="#2A2A36"/>' for a in (90, 210, 330))
    + f'<circle cx="34" cy="76" r="4" fill="#C8C8D8"/>'
    + f'{f(34, 66, d=7, k=0.55)}'
    + "".join(sparkle(x, y, r, "#FFE79A") for x, y, r in [(100, 30, 5), (78, 104, 4), (20, 22, 3)]))


if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        a, b, hero, scene, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
