"""Иконки робота fun (2026-11-07, вечер): 13 мест. Каждая придумана отдельно (правило абсолютной уникальности).
Сверено с icons-src/subjects.txt (заняты: золотая рыбка, бочка в море, кот учёный, белочка с орешком, зеркало,
аленький цветочек, мамонтёнок, афишная тумба, бинокль, агат, аметист, бобрёнок, мольберт, палитра, карандаши,
прялка, кинобилетик, киноэкран, попкорн, проектор, призма, наушники-плееры, светлячок — не брать).
Запуск: python3 tools/icons_fun_1107e.py [id ...]  (печатает строки для subjects.txt)"""
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

# 1. Музей «В Тишине» — ухо, которое отдыхает от звуков
I["museum-v-tishine"] = ("#F3EEFF", "#9A86DA",
    "большое розовое ухо-персонаж с блаженно закрытыми глазками", "отдыхает в тишине, а звуковые волны вокруг него перечёркнуты",
    f'<path d="M44 30 Q44 8 70 10 Q100 12 100 44 Q100 62 86 72 Q78 80 80 94 Q80 112 62 114 Q46 114 46 100" fill="#FFB8C8" {s()}/>'
    f'<path d="M58 34 Q60 22 72 24 Q86 26 86 42 Q86 52 76 58 Q68 64 70 76" fill="none" stroke="#E07A98" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M66 82 Q60 90 62 98" fill="none" stroke="#E07A98" stroke-width="4" stroke-linecap="round"/>'
    + closed_eye(60, 46, 0.9) + closed_eye(78, 46, 0.9)
    + f'<ellipse cx="54" cy="56" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/><ellipse cx="84" cy="56" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/>'
    f'<path d="M66 56 Q69 59 72 56" fill="none" {W(2.2)}/>'
    + "".join(f'<path d="M{x} {y} q-{w} 12 0 24" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>' for x, y, w in [(24, 50, 6), (16, 46, 9)])
    + f'<path d="M10 76 L32 42" stroke="#E8453C" stroke-width="4.4" stroke-linecap="round"/>'
    + "".join(f'<path d="M{x} {y} q{w} 12 0 24" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>' for x, y, w in [(108, 64, 6), (116, 60, 9)])
    + f'<path d="M104 92 L122 58" stroke="#E8453C" stroke-width="4.4" stroke-linecap="round"/>'
    + sp((28, 24, 4), (112, 30, 3)))

# 2. Музей Пушкина на Пречистенке — дуб у Лукоморья
I["pushkin-museum-prechistenka"] = ("#EAF8FF", "#4E9FD6",
    "могучий зелёный дуб с улыбкой на стволе, обвитый золотой цепью", "растёт у Лукоморья на берегу синего моря, волны лижут его корни",
    f'<path d="M0 100 Q16 94 32 100 T64 100 T96 100 T128 100 V128 H0Z" fill="#3E7FC8" {s()}/>'
    f'<path d="M0 110 Q16 104 32 110 T64 110 T96 110 T128 110" fill="none" stroke="#fff" stroke-width="2.4" opacity=".7"/>'
    f'<path d="M36 104 Q48 96 52 72 L76 72 Q80 96 92 104Z" fill="#9C6A3E" {s()}/>'
    f'<circle cx="64" cy="44" r="30" fill="#5DB34E" {s()}/>'
    f'<circle cx="38" cy="54" r="18" fill="#5DB34E" {s()}/><circle cx="90" cy="54" r="18" fill="#5DB34E" {s()}/>'
    f'<circle cx="46" cy="28" r="14" fill="#6CC45C" {s()}/><circle cx="84" cy="28" r="14" fill="#6CC45C" {s()}/>'
    f'<path d="M30 62 Q64 76 98 62" fill="#5DB34E" stroke="none"/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="3" ry="4" fill="#C98B3A" {W(1.4)}/>' for x, y in [(40, 40), (86, 42), (64, 22)])
    + f'<g>{f(64, 82, d=6, k=0.6)}</g>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="4.4" ry="3" fill="none" stroke="{GO}" stroke-width="2.6" transform="rotate({r} {x} {y})"/>'
              for x, y, r in [(50, 92, -30), (57, 95, 0), (65, 96, 20), (73, 95, 0), (80, 92, -30)])
    + sp((14, 30, 4), (114, 82, 3)))

# 3. Дом-музей В. Л. Пушкина — гусиное перо в чернильнице
I["vl-pushkin-basmannaya"] = ("#FFF7E2", "#D9A55E",
    "белое гусиное перо-персонаж в стеклянной чернильнице", "выводит завитушку стиха на развёрнутом свитке при свете ночника",
    f'<path d="M14 92 Q14 84 22 84 H108 Q116 84 116 92 V104 Q116 112 108 112 H22 Q14 112 14 104Z" fill="#FFFDF4" {s()}/>'
    f'<path d="M24 96 q8 -6 16 0 t16 0 t16 0" fill="none" stroke="#3B3355" stroke-width="2.4" stroke-linecap="round"/>'
    f'<path d="M24 104 H60" stroke="#C8BBA0" stroke-width="2.4" stroke-linecap="round"/>'
    f'<path d="M74 70 Q72 92 86 92 H98 Q112 92 110 70Z" fill="#7CA8D8" opacity=".9" {s()}/>'
    f'<rect x="82" y="62" width="20" height="10" rx="3" fill="#5C6E8A" {s()}/>'
    f'<path d="M80 80 Q92 86 104 80" fill="none" stroke="#2E3A66" stroke-width="5" opacity=".6"/>'
    f'<path d="M92 66 L56 16 Q38 8 34 26 Q36 44 58 56 Z" fill="#FFFFFF" {s()}/>'
    f'<path d="M92 66 L46 22" stroke="#C8C0B0" stroke-width="2.4"/>'
    + "".join(f'<path d="M{x} {y} l-8 6" stroke="#D8D0C2" stroke-width="2"/>' for x, y in [(52, 30), (60, 38), (68, 46)])
    + f'<g>{f(50, 36, d=5, k=0.55)}</g>'
    + sp((20, 30, 5), (112, 30, 3), (24, 66, 3)))

# 4. Дом-музей Тургенева — охотничий сеттер (Записки охотника)
I["turgenev-ostozhenka"] = ("#FAFCD8", "#A9C94E",
    "рыжий сеттер с длинными ушами-лопухами", "делает охотничью стойку в высокой луговой траве, подняв переднюю лапку",
    f'<path d="M0 98 Q64 88 128 98 V128 H0Z" fill="#7DB342" {s()}/>'
    f'<path d="M30 66 Q32 54 50 54 H82 Q94 54 94 66 Q94 78 82 78 H46 Q30 78 30 66Z" fill="#D8742E" {s()}/>'
    f'<path d="M30 62 Q14 54 8 40 Q22 50 32 56" fill="#D8742E" {s()}/>'
    f'<path d="M40 76 L36 104 H44 L50 78 M72 78 L74 104 H82 L82 76" fill="#D8742E" {s()}/>'
    f'<path d="M88 70 L96 84 L104 80" fill="none" stroke="{O}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'
    f'<path d="M88 70 L96 84 L104 80" fill="none" stroke="#D8742E" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
    f'<path d="M84 64 L90 40 Q96 28 108 34 Q120 40 116 50 L100 58 Z" fill="#D8742E" {s()}/>'
    f'<path d="M94 38 Q84 44 86 64 Q92 62 96 52Z" fill="#B0541E" {s()}/>'
    f'<ellipse cx="118" cy="48" rx="4" ry="3.4" fill="{O}"/>'
    + eye(106, 42, 0.8)
    + f'<ellipse cx="108" cy="52" rx="3.4" ry="2" fill="#FF7FA8" opacity=".7"/>'
    + "".join(f'<path d="M{x} 128 Q{x+2} 104 {x+6} 90" fill="none" stroke="#5E9A2E" stroke-width="3" stroke-linecap="round"/>' for x in (6, 22, 54, 62, 92, 112))
    + sp((24, 26, 5), (60, 22, 3)))

# 5. Театр мюзикла — сверкающая лестница (вид сбоку)
STEPS = [(14, 112), (34, 96), (54, 80), (74, 64), (94, 48), (114, 32)]
I["teatr-myuzikla"] = ("#FFD9E6", "#B8185A",
    "золотая парадная лестница мюзикла с лампочками на краю каждой ступеньки", "поднимается зигзагом между красными кулисами к прожектору, сияет и улыбается",
    f'<path d="M0 0 H22 Q18 60 26 128 H0Z" fill="#C4123E" {s()}/><path d="M128 0 H106 Q112 50 104 128 H128Z" fill="#C4123E" {s()}/>'
    f'<path d="M8 0 Q6 60 12 128 M116 0 Q120 50 114 128" fill="none" stroke="#8E0C2C" stroke-width="3"/>'
    f'<path d="M84 0 L128 40 V0Z" fill="#FFF3A8" opacity=".35"/>'
    + "<path d=\"M10 128 " + " ".join(f"L{x} {y} L{x+20} {y}" for x, y in STEPS[:-1]) + " L114 32 L114 128Z\" fill=\"#F6C64E\" " + s() + "/>"
    + "".join(f'<path d="M{x} {y} H{x+20}" stroke="#FFF0B0" stroke-width="3"/>' for x, y in STEPS[:-1])
    + "".join(f'<circle cx="{x+4+k*6}" cy="{y-3}" r="2.4" fill="#FFFDE8" {W(1.2)}/>' for x, y in STEPS[:-1] for k in range(3))
    + f'<g>{f(76, 92, d=8, k=0.8)}</g>'
    + "".join(f'<rect x="{x}" y="{y}" width="5" height="5" fill="{c}" transform="rotate({r} {x} {y})"/>' for x, y, c, r in
              [(36, 26, "#FFF0B0", 20), (54, 12, "#fff", -10), (70, 30, "#FFD25E", 15)])
    + sp((50, 40, 5), (88, 16, 4), (32, 60, 3)))

# 6. Рудно-петрографический музей — геологический молоток
I["rudno-petro-museum"] = ("#E6F4F1", "#5E968C",
    "геологический молоток-персонаж с острым клювом", "раскалывает серый булыжник на музейной подставке, а внутри — сверкающие золотые блёстки руды",
    f'<rect x="20" y="104" width="88" height="14" rx="3" fill="#8A5A3A" {s()}/>'
    f'<path d="M26 104 Q22 82 40 74 L58 70 L54 104Z" fill="#9AA3AB" {s()}/>'
    f'<path d="M64 104 L60 70 L84 74 Q104 82 100 104Z" fill="#9AA3AB" {s()}/>'
    f'<path d="M54 104 L58 70 L62 70 L64 104Z" fill="#4A4D5C"/>'
    + "".join(f'<path d="M{x} {y} l2 4 4 .5 -3 3 .8 4 -3.8 -2 -3.8 2 .8 -4 -3 -3 4 -.5Z" fill="{GO}" {W(1.2)}/>' for x, y in [(40, 84), (82, 86), (44, 94)])
    + f'<circle cx="34" cy="90" r="2" fill="#5A6070"/><circle cx="90" cy="96" r="2" fill="#5A6070"/>'
    f'<g transform="rotate(-28 70 40)">'
    f'<rect x="66" y="34" width="10" height="56" rx="4" fill="#C98B4E" {s()}/>'
    f'<path d="M40 22 H98 Q104 26 98 34 H52 Q40 34 30 46 Q30 30 40 22Z" fill="#6E7A8A" {s()}/>'
    f'</g>'
    + f'<g>{f(70, 28, d=7, k=0.6)}</g>'
    + f'<path d="M46 62 l-8 -6 M56 58 l-2 -10 M66 62 l6 -8" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    + sp((18, 40, 4), (112, 60, 3)))

# 7. «На Вадковском» — бумажный журавлик-оригами
I["na-vadkovskom"] = ("#FFF0E6", "#F08A66",
    "бумажный журавлик-оригами в белую и розовую клетку", "только что сложен на детском столе и взлетает, расправив острые крылья",
    f'<rect x="0" y="104" width="128" height="24" fill="#FFD9A8" {s()}/>'
    f'<rect x="14" y="98" width="30" height="10" rx="2" fill="#7CC8F0" transform="rotate(-8 29 103)" {s()}/>'
    f'<rect x="90" y="100" width="26" height="8" rx="2" fill="#7CD26E" transform="rotate(6 103 104)" {s()}/>'
    f'<path d="M64 84 L18 34 L60 60Z" fill="#FFFFFF" {s()}/>'
    f'<path d="M64 84 L112 28 L70 60Z" fill="#FFE1EC" {s()}/>'
    f'<path d="M64 84 L40 88 L50 70 L60 60 L70 60 L80 70 L88 88Z" fill="#FFF4F8" {s()}/>'
    f'<path d="M50 70 L28 52 L22 44 L34 46Z" fill="#FFFFFF" {s()}/>'
    f'<path d="M28 52 L20 44" stroke="{O}" stroke-width="3"/>'
    f'<path d="M80 70 L104 76 L94 66Z" fill="#FFE1EC" {s()}/>'
    f'<path d="M64 84 L64 62" stroke="#E9B8C8" stroke-width="2"/>'
    + eye(30, 47, 0.55)
    + f'<path d="M20 44 L10 48 L22 47Z" fill="#F08A66" {W(1.4)}/>'
    + sp((92, 22, 5), (50, 22, 3), (114, 52, 3)))

# 8. Музей Темноты — глаза в полной темноте
I["museum-darkness-riviera"] = ("#3B4060", "#0C0E1C",
    "две пары удивлённых глаз — ребёнка и гида — в полной темноте", "моргают в чёрной комнате, а светлая ладошка нащупывает дорогу по шершавой стене",
    f'<path d="M96 0 V128" stroke="#262A40" stroke-width="40"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="#3A3F5A"/>' for x, y in [(84, 20), (100, 34), (90, 52), (108, 70), (86, 90), (102, 106)])
    + f'<ellipse cx="34" cy="46" rx="10" ry="12" fill="#fff" {s()}/><ellipse cx="58" cy="46" rx="10" ry="12" fill="#fff" {s()}/>'
    f'<circle cx="36" cy="48" r="5" fill="{O}"/><circle cx="60" cy="48" r="5" fill="{O}"/>'
    f'<circle cx="34" cy="46" r="1.8" fill="#fff"/><circle cx="58" cy="46" r="1.8" fill="#fff"/>'
    f'<ellipse cx="40" cy="84" rx="7" ry="8.4" fill="#fff" {s()}/><ellipse cx="57" cy="84" rx="7" ry="8.4" fill="#fff" {s()}/>'
    f'<circle cx="42" cy="86" r="3.4" fill="{O}"/><circle cx="59" cy="86" r="3.4" fill="{O}"/>'
    f'<path d="M86 58 Q78 56 76 64 L74 84 Q74 96 84 98 Q94 98 96 88 L98 62 Q98 56 92 56Z" fill="#FFD7B8" {s()}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="6" height="16" rx="3" fill="#FFD7B8" {W(2.4)}/>' for x, y in [(76, 44), (83, 40), (90, 42)])
    + f'<path d="M98 70 L106 62" stroke="{O}" stroke-width="8" stroke-linecap="round"/><path d="M98 70 L106 62" stroke="#FFD7B8" stroke-width="4" stroke-linecap="round"/>'
    + "".join(sparkle(x, y, r, "#FFE79A") for x, y, r in [(20, 22, 3), (66, 18, 2.4)]))

# 9. Музей природы Приокско-Террасного заповедника — барсук
I["prioksky-nature-museum"] = ("#E4F4DC", "#4C8C48",
    "барсук с белой полоской на мордочке", "выглядывает из норы под корнями сосны на песчаном склоне у Оки",
    f'<path d="M0 72 Q40 60 70 70 Q100 80 128 70 V128 H0Z" fill="#E8C98A" {s()}/>'
    f'<path d="M100 0 V64" stroke="{O}" stroke-width="16"/><path d="M100 0 V64" stroke="#B5653A" stroke-width="10"/>'
    f'<path d="M100 60 Q90 72 76 74 M100 60 Q112 74 124 76" fill="none" stroke="#8C4E2E" stroke-width="5" stroke-linecap="round"/>'
    f'<ellipse cx="54" cy="96" rx="40" ry="26" fill="#4A3424" {s()}/>'
    f'<ellipse cx="54" cy="84" rx="28" ry="22" fill="#9A9AA0" {s()}/>'
    f'<path d="M54 62 Q44 62 42 76 Q46 102 54 106 Q62 102 66 76 Q64 62 54 62Z" fill="#FFFFFF"/>'
    f'<path d="M34 74 Q38 66 44 72 L46 98 Q40 96 36 88Z" fill="#2E2E36"/><path d="M74 74 Q70 66 64 72 L62 98 Q68 96 72 88Z" fill="#2E2E36"/>'
    f'<circle cx="30" cy="68" r="6" fill="#9A9AA0" {W(2.4)}/><circle cx="78" cy="68" r="6" fill="#9A9AA0" {W(2.4)}/>'
    + eye(42, 82, 0.7) + eye(66, 82, 0.7)
    + f'<ellipse cx="54" cy="96" rx="5" ry="3.6" fill="{O}"/>'
    f'<path d="M50 102 Q54 105 58 102" fill="none" {W(1.8)}/>'
    f'<path d="M18 116 Q34 108 50 116" fill="none" stroke="#B8955A" stroke-width="3"/>'
    + "".join(f'<path d="M{x} 40 l-10 10 M{x} 40 l10 10 M{x} 30 l-8 8 M{x} 30 l8 8" stroke="#2F6B3A" stroke-width="4" stroke-linecap="round"/>' for x in (100,))
    + sp((22, 30, 4), (60, 18, 3)))

# 10. Музей КМЗ — объектив
I["kmz-museum-krasnogorsk"] = ("#FFF9CC", "#E2B92E",
    "чёрный фотообъектив, глядящий прямо на зрителя", "диафрагма-зрачок раскрывается, на стекле играет радужный блик, сверху — гравировка-полоски",
    f'<circle cx="64" cy="66" r="46" fill="#2E2E36" {s()}/>'
    f'<circle cx="64" cy="66" r="40" fill="#45454F" {W(2)}/>'
    + "".join(f'<path d="M{64+40*math.cos(math.radians(a)):.1f} {66+40*math.sin(math.radians(a)):.1f} l{4*math.cos(math.radians(a)):.1f} {4*math.sin(math.radians(a)):.1f}" stroke="#9A9AA6" stroke-width="2"/>' for a in range(0, 360, 15))
    + f'<circle cx="64" cy="66" r="30" fill="#1C2340" {s()}/>'
    + "".join(f'<path d="M64 66 L{64+30*math.cos(math.radians(a)):.1f} {66+30*math.sin(math.radians(a)):.1f}" stroke="#3A4466" stroke-width="2"/>' for a in range(0, 360, 60))
    + f'<polygon points="' + " ".join(f'{64+13*math.cos(math.radians(a+30)):.1f},{66+13*math.sin(math.radians(a+30)):.1f}' for a in range(0, 360, 60)) + f'" fill="#0A0C18" {W(1.6)}/>'
    f'<path d="M46 52 Q56 42 70 44" fill="none" stroke="#9FE3FF" stroke-width="4" stroke-linecap="round" opacity=".9"/>'
    f'<path d="M48 58 Q54 52 60 52" fill="none" stroke="#FF9FD8" stroke-width="3" stroke-linecap="round" opacity=".8"/>'
    f'<circle cx="60" cy="62" r="2.6" fill="#fff"/>'
    + f'<ellipse cx="40" cy="92" rx="5" ry="3" fill="#FF7FA8" opacity=".75"/><ellipse cx="88" cy="92" rx="5" ry="3" fill="#FF7FA8" opacity=".75"/>'
    f'<path d="M56 100 Q64 106 72 100" fill="none" stroke="#FFE27A" stroke-width="3" stroke-linecap="round"/>'
    + sp((18, 28, 5), (110, 24, 4), (112, 104, 3)))

# 11. Студия «Рыжий кот» — восковой мелок рисует радугу
I["ryzhiy-kot-zelenograd"] = ("#E6FFF5", "#4FC096",
    "толстый оранжевый восковой мелок в бумажной обёртке", "старательно рисует радугу на большом листе бумаги, высунув кончик языка",
    f'<path d="M8 40 L118 30 L124 112 L12 118Z" fill="#FFFFFF" {s()}/>'
    + "".join(f'<path d="M24 {104-i*0} Q60 {44+i*7} {96} {96}" fill="none" stroke="{c}" stroke-width="7" stroke-linecap="round" transform="translate(0 {i*7})"/>'
              for i, c in enumerate(["#E8453C", "#FF9A2E", "#FFD23C", "#5DBB5A", "#4E9BE0"]))
    + f'<g transform="rotate(38 92 66)">'
    f'<path d="M80 30 H104 V96 H80Z" fill="#FF8A2A" {s()}/>'
    f'<path d="M80 46 H104 V84 H80Z" fill="#FFFFFF" {s()}/>'
    f'<path d="M80 96 L92 112 L104 96Z" fill="#FF8A2A" {s()}/>'
    f'<path d="M84 54 H100 M84 76 H100" stroke="#FF8A2A" stroke-width="2.4"/>'
    f'</g>'
    + f'<g>{f(78, 56, d=6, k=0.6, mouth=False)}</g>'
    + f'<path d="M72 62 Q78 68 84 62" fill="#FF7FA8" {W(1.8)}/>'
    + sp((20, 26, 4), (112, 14, 3)))

# 12. «Ковчег» (Кратово) — деревянная юла
I["kovcheg-kratovo"] = ("#FFE6EE", "#E36A8C",
    "расписная деревянная юла-волчок в красно-синюю полоску", "кружится на круглом вязаном коврике в детской комнате, оставляя вихрь-завитки",
    f'<ellipse cx="64" cy="108" rx="52" ry="12" fill="#FFF0C8" {s()}/>'
    f'<ellipse cx="64" cy="108" rx="36" ry="7" fill="none" stroke="#F2B632" stroke-width="2.4"/>'
    f'<path d="M64 104 L36 66 Q64 54 92 66Z" fill="#E8453C" {s()}/>'
    f'<path d="M36 66 Q34 48 64 44 Q94 48 92 66 Q64 78 36 66Z" fill="#FFD23C" {s()}/>'
    f'<path d="M44 74 Q64 82 84 74 L76 86 Q64 90 52 86Z" fill="#3E7FC8"/>'
    f'<path d="M60 44 V22 H68 V44" fill="#B5763A" {s()}/>'
    f'<circle cx="64" cy="20" r="5" fill="#B5763A" {s()}/>'
    + f'<g>{f(64, 56, d=8, k=0.7)}</g>'
    + "".join(f'<path d="M{x} {y} q-10 -4 -14 6" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' for x, y in [(30, 54), (24, 76)])
    + "".join(f'<path d="M{x} {y} q10 -4 14 6" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' for x, y in [(98, 54), (104, 76)])
    + sp((22, 28, 4), (106, 26, 3)))

# 13. Silver Cinema (Подольск) — старинная кинокамера
I["silver-cinema-podolsk"] = ("#F2F5FA", "#8496B4",
    "серебристая старинная кинокамера с двумя бобинами на макушке", "снимает кино на штативе, моргая красной лампочкой «запись»",
    f'<path d="M50 96 L30 126 M64 96 V128 M78 96 L98 126" stroke="{O}" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M50 96 L30 126 M64 96 V128 M78 96 L98 126" stroke="#6C6C78" stroke-width="3.4" stroke-linecap="round"/>'
    f'<circle cx="42" cy="34" r="18" fill="#C8D0DC" {s()}/><circle cx="78" cy="30" r="20" fill="#C8D0DC" {s()}/>'
    + "".join(f'<circle cx="{cx+r*0.55*math.cos(math.radians(a)):.1f}" cy="{cy+r*0.55*math.sin(math.radians(a)):.1f}" r="{r*0.22:.1f}" fill="#7A8498"/>'
              for cx, cy, r in [(42, 34, 18), (78, 30, 20)] for a in (0, 120, 240))
    + f'<circle cx="42" cy="34" r="3" fill="{O}"/><circle cx="78" cy="30" r="3" fill="{O}"/>'
    f'<rect x="22" y="50" width="76" height="46" rx="8" fill="#B4BECE" {s()}/>'
    f'<path d="M98 62 L118 52 V96 L98 86Z" fill="#9AA6B8" {s()}/>'
    f'<circle cx="112" cy="74" r="2" fill="#fff"/>'
    f'<circle cx="34" cy="60" r="4" fill="#FF4A4A" {W(1.6)}/>'
    + f'<g>{f(60, 72, d=10, k=0.75)}</g>'
    + sp((112, 22, 5), (16, 80, 3)))


if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        a, b, hero, scene, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
