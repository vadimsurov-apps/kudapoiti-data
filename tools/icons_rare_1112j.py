"""Иконки робота rare, 2026-11-12 (09:45 UTC) — места из tools/add_rare_1112j.py.
Правило АБСОЛЮТНОЙ уникальности: просмотрены все листы icons-catalog (монтажом по 4 листа) и реестр subjects.txt
(grep: батут, сальто, щучка, настольн, конёк/коньки, солнце, белка, лось, снегирь, ворота, комета, кленовый лист, морж,
медвежонок). Заняты: лось-вратарь, хоккейные ворота с мордашкой, снегирь, кленовый лист, комета, морской конёк,
звёздочка-фигуристка, прокатные коньки с биркой, кубик льда на коньках — их не берём.
Каждая иконка придумана отдельно: свой герой, своя сцена, своя палитра фона.
Запуск: python3 tools/icons_rare_1112j.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O
from icons_sections_1107c import G

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')


def rect(x, y, w, h, c, rx=4, sw=2.8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{c}" {W(sw)}/>'


def circ(x, y, r, c, sw=2.8):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" {W(sw)}/>'


def ell(x, y, rx, ry, c, sw=2.8):
    return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{c}" {W(sw)}/>'


def path(d, c="none", sw=2.8):
    return f'<path d="{d}" fill="{c}" {W(sw)}/>'


def mouth(x, y, w=3, sw=2.0):
    return f'<path d="M{x-w} {y} Q{x} {y+w*0.9} {x+w} {y}" fill="none" {W(sw)}/>'


def blush(x, y, rx=2.6, ry=1.6):
    return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#FF7FA8" opacity=".7"/>'


def add(pid, pal, body, hero, scene):
    k = f"r12j_{pid}"
    draw_icons.BG[k] = pal
    ICONS[pid] = svg(k, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def skate(x, y, boot="#FFFFFF", k=1.0, blade="#B8C4D6"):
    """фигурный конёк: (x, y) — носок у лезвия, смотрит вправо"""
    b = (path("M-14 -22 H-2 Q0 -10 8 -8 Q14 -7 14 -2 V0 H-14Z", boot, 2.6)
         + path("M-10 -18 H-4 M-10 -13 H-3", "none", 1.8)
         + path("M-15 5 H12 Q17 5 17 0", "none", 2.4)
         + f'<path d="M-15 5 H12 Q17 5 17 0" stroke="{blade}" stroke-width="1.2" fill="none"/>'
         + path("M-10 0 V5 M8 0 V5", "none", 2.2))
    return G(x, y, b, 0, k)


# 1) Ледовая арена Солнцево — название: солнышко само вышло на лёд.
ice = ('<rect x="-4" y="94" width="136" height="40" fill="#EAF7FF"/>'
       '<path d="M-4 94 H132" stroke="#9CCBE8" stroke-width="2.4"/>'
       '<path d="M14 112 Q40 104 62 110" stroke="#9CCBE8" stroke-width="2" fill="none" stroke-dasharray="4 4"/>'
       '<path d="M20 120 Q46 112 66 118" stroke="#9CCBE8" stroke-width="2" fill="none" stroke-dasharray="4 4"/>')
rays = "".join(G(66, 56, path("M-5 -40 L0 -50 L5 -40Z", "#FFB020", 2.2), a) for a in range(0, 360, 30))
sun = (rays + circ(66, 56, 30, "#FFC93C", 3.0)
       + face(66, 54, 10, 1.05) + path("M38 60 Q30 70 36 78", "none", 3.0) + path("M94 60 Q102 66 98 74", "none", 3.0))
add("rink-solntsevo-aviatorov", ("#D7F0FF", "#4E9FE0"),
    ice + sun + path("M54 84 V88 M78 84 V88", "none", 2.8) + skate(56, 94, "#FFFFFF", 1.0) + skate(82, 94, "#FFFFFF", 1.0)
    + sparkle(22, 34, 4) + sparkle(108, 92, 3),
    "оранжево-жёлтое солнышко с лучами-треугольниками на двух белых фигурных коньках",
    "выкатилось на голубой лёд и скользит, оставляя за собой пунктирные дорожки")

# 2) Ледовый дворец Сокольники (у парка с белками) — белка на массовом катании, хвост как парус.
ice2 = ('<rect x="-4" y="98" width="136" height="36" fill="#F4FCFF"/>'
        '<path d="M-4 98 H132" stroke="#8CC7D9" stroke-width="2.4"/>')
tail = path("M44 84 Q14 80 18 50 Q22 24 46 30 Q36 44 44 56 Q52 70 44 84Z", "#E8732C", 3.0) \
    + path("M30 44 Q28 58 38 70", "none", 2.0)
body = (ell(66, 74, 18, 20, "#F08A3C", 3.0) + ell(66, 80, 10, 12, "#FFE0C0", 2.2)
        + circ(70, 46, 15, "#F08A3C", 3.0)
        + path("M58 36 L56 24 L64 32Z", "#F08A3C", 2.4) + path("M78 34 L84 22 L84 34Z", "#F08A3C", 2.4)
        + eye(65, 45, 0.7) + eye(76, 45, 0.7) + mouth(71, 51, 2.6) + blush(61, 52) + blush(80, 52)
        + circ(71, 50, 1.6, O, 0))
scarf = path("M54 58 Q70 64 86 56 L86 62 Q70 70 54 64Z", "#2F6FD6", 2.6) + path("M80 60 L92 74 L86 76 L76 63Z", "#2F6FD6", 2.4)
paws = path("M54 72 Q44 70 40 64", "none", 3.0) + path("M80 70 Q92 66 96 58", "none", 3.0)
add("rink-ld-sokolniki", ("#D5FBEF", "#3FB59A"),
    ice2 + tail + body + scarf + paws + path("M60 92 V94 M74 92 V94", "none", 2.6)
    + skate(60, 98, "#FFFFFF", 0.8) + skate(78, 98, "#FFFFFF", 0.8) + sparkle(104, 30, 4) + sparkle(98, 86, 2.6),
    "рыжая белка в синем шарфе на белых фигурных коньках",
    "катится по льду крытого дворца, распустив пушистый хвост парусом")


# 3) Аляска — массовое катание: три малыша паровозиком по кругу катка.
def kid(x, y, shirt, hat, k=1.0, lean=0):
    b = (path("M-5 18 L-8 30 M5 18 L8 30", "none", 3.0)
         + rect(-9, 0, 18, 20, shirt, 6, 2.8)
         + circ(0, -8, 9, "#FFD7B5", 2.8)
         + path("M-9 -9 Q-9 -20 0 -20 Q9 -20 9 -9Z", hat, 2.4) + circ(0, -22, 3, "#FFFFFF", 2.0)
         + eye(-3, -7, 0.45) + eye(3.5, -7, 0.45) + mouth(0, -3, 2.2, 1.6)
         + path("M-11 34 H-3 M3 34 H11", "none", 2.6) + path("M-12 31 L-4 31 L-5 34 M4 31 L12 31 L11 34", "#FFFFFF", 2.2))
    return G(x, y, b, lean, k)


rink3 = (ell(64, 104, 70, 26, "#E9F8FF", 2.6) + ell(64, 104, 54, 16, "none", 1.6)
         .replace('fill="none"', 'fill="none" stroke-dasharray="4 4"'))
arms = path("M38 74 L54 70 M70 72 L84 70", "none", 3.0)
add("rink-alyaska-nizhnelikhoborsky", ("#E6E2FF", "#7A6CD8"),
    rink3 + kid(34, 74, "#E24B4B", "#2E7DD7", 0.95, -8) + kid(64, 70, "#FFC12E", "#E24B4B", 0.95, -8)
    + kid(94, 66, "#3CB371", "#FFC12E", 0.95, -8) + arms + sparkle(22, 30, 4) + sparkle(110, 34, 3.4) + sparkle(64, 22, 2.6),
    "три малыша в разноцветных шапках с помпонами — красный, жёлтый и зелёный",
    "катятся паровозиком друг за другом по кругу катка, держась за куртки")


# 4) Монреаль — клуб зовёт мальчиков И девочек с 4 лет: мальчик и девочка-хоккеисты отбивают клюшки «дай пять».
def player(x, flip, jersey, helmet, girl=False):
    b = (path("M-6 24 L-8 40 M6 24 L8 40", "none", 3.2)
         + path("M-13 40 H-3 M3 40 H13", "none", 2.8)
         + rect(-13, 0, 26, 26, jersey, 8, 3.0)
         + path("M-13 10 H13", "none", 2.2) + '<path d="M-12 10 H12" stroke="#FFFFFF" stroke-width="2.4"/>'
         + circ(0, -10, 11, "#FFD7B5", 2.8)
         + path("M-12 -10 Q-12 -25 0 -25 Q12 -25 12 -10 L8 -12 H-8Z", helmet, 2.6)
         + eye(-4, -9, 0.5) + eye(4, -9, 0.5) + mouth(0, -4, 2.6, 1.8) + blush(-7, -4, 2, 1.2) + blush(7, -4, 2, 1.2))
    if girl:
        b += path("M10 -14 Q20 -10 16 2", "none", 4.4) + '<path d="M10 -14 Q20 -10 16 2" stroke="#C0612B" stroke-width="2.4" fill="none"/>'
    stick = path("M12 4 L30 -26", "none", 5.2) + '<path d="M12 4 L30 -26" stroke="#E9B872" stroke-width="3" fill="none"/>' \
        + path("M8 4 Q12 0 16 2", "none", 2.6)
    b = stick + b
    return f'<g transform="translate({x} 62) scale({-1 if flip else 1} 1)">{b}</g>'


ice4 = '<rect x="-4" y="104" width="136" height="30" fill="#F2FAFF"/><path d="M-4 104 H132" stroke="#9AC4E0" stroke-width="2.2"/>'
puck = ell(64, 108, 9, 3.6, "#2B2B33", 2.2)
add("hockey-montreal-butovo", ("#FFE3E3", "#D8454F"),
    ice4 + player(40, False, "#C8102E", "#1D3E8A") + player(88, True, "#1D3E8A", "#C8102E", girl=True) + puck
    + sparkle(64, 26, 5, "#FFF3A6") + sparkle(56, 36, 2.4) + sparkle(74, 36, 2.4),
    "мальчик и девочка-хоккеисты в красном и синем свитерах",
    "скрестили клюшки над головами «дай пять», а у их коньков лежит чёрная шайба")

# 5) Снегирь Арена — место не добавлено (нет точки в OSM), иконку не рисуем.

# 6) «Звезда» (Некрасовка) — белый конёк со звездой на голенище подпрыгивает в прыжке, под ним петля следа.
loop = '<path d="M20 106 Q40 118 62 106 Q80 94 66 88 Q52 84 60 100 Q70 116 108 108" stroke="#FFFFFF" stroke-width="3" fill="none" stroke-dasharray="5 4"/>'
star = path("M0 -9 L2.6 -3 L9 -2.8 L4 1.4 L5.6 8 L0 4.4 L-5.6 8 L-4 1.4 L-9 -2.8 L-2.6 -3Z", "#FFD23F", 2.0)
jump = G(64, 64, path("M-24 -34 H-2 Q2 -12 16 -9 Q26 -7 26 2 V8 H-24Z", "#FFFFFF", 3.0)
         + path("M-26 16 H20 Q30 16 30 6", "none", 3.0) + '<path d="M-26 16 H20 Q30 16 30 6" stroke="#C9D3E2" stroke-width="1.4" fill="none"/>'
         + path("M-16 8 V16 M14 8 V16", "none", 2.6) + path("M28 10 L34 14", "none", 2.6)
         + G(-12, -20, star, 0, 1.0)
         + eye(0, -8, 0.7) + eye(10, -6, 0.7) + mouth(5, 0, 2.6) + blush(-4, 0) + blush(15, 2), -14, 1.0)
add("fk-zvezda-nekrasovka", ("#C9D4FF", "#3346A8"),
    '<rect x="-4" y="100" width="136" height="36" fill="#8FB6F0"/>' + loop + jump
    + "".join(G(x, y, path("M0 -3 L1 -1 L3 0 L1 1 L0 3 L-1 1 L-3 0 L-1 -1Z", "#FFF3A6", 1.0), 0, 1.4)
              for x, y in ((22, 30), (104, 26), (100, 62), (28, 70)))
    + sparkle(64, 18, 3.4),
    "белый фигурный конёк с жёлтой звёздочкой на голенище",
    "подпрыгнул над тёмно-синим вечерним льдом, а под ним вьётся пунктирная петля следа")


# 7) «Сальто» — спортивный батут: мальчик в «щучке» высоко над прямоугольной сеткой с синими матами.
tramp = (rect(14, 100, 100, 10, "#2E62C9", 3, 2.8) + rect(24, 102, 80, 5, "#1F1F2B", 2, 1.8)
         + path("M22 110 L16 124 M106 110 L112 124 M50 110 V124 M78 110 V124", "none", 3.0))
boy = G(66, 52, path("M-2 10 L22 6 L30 4", "none", 4.4)            # прямые ноги вперёд
        + path("M30 4 L34 2", "none", 4.4) + '<path d="M-2 10 L30 4" stroke="#3456C8" stroke-width="2.4" fill="none"/>'
        + rect(-14, -6, 16, 20, "#E33B3B", 6, 2.8)                    # корпус
        + path("M0 -2 Q14 -4 26 2", "none", 3.0)                       # руки тянутся к носочкам
        + circ(-10, -14, 9, "#FFD7B5", 2.8)
        + path("M-19 -16 Q-17 -25 -9 -24 Q-1 -24 -1 -16 Q-6 -20 -10 -19 Q-14 -20 -19 -16Z", "#6B3E26", 2.0)
        + eye(-12, -13, 0.45) + eye(-6, -12, 0.45) + mouth(-8, -8, 2, 1.6), 0, 1.15)
add("salto-batut-nagatinskaya", ("#FFE6F0", "#E0569A"),
    tramp + '<path d="M40 96 Q42 76 48 66" stroke="#FFFFFF" stroke-width="2.6" fill="none" stroke-dasharray="4 4"/>'
    + boy + sparkle(100, 28, 4.4) + sparkle(24, 40, 3),
    "мальчик-батутист в красной майке и синих шортах",
    "завис в позе «щучка» — ноги прямо вперёд, руки к носочкам — высоко над спортивным батутом с синей рамой")

# 8) ТТ Текстильщики — девочка отрабатывает удары у стола, вторая половина которого поднята стенкой.
table = (path("M10 84 H66 L60 92 H4Z", "#1E9E62", 2.8) + path("M66 84 L66 30 L76 26 L76 84Z", "#1E9E62", 2.8)
         + '<path d="M36 84 L32 92" stroke="#FFFFFF" stroke-width="1.6"/><path d="M71 32 V80" stroke="#FFFFFF" stroke-width="1.6"/>'
         + path("M10 92 V112 M58 92 V112 M70 84 V112", "none", 3.0))
girl = (path("M94 92 L90 116 M104 92 L108 116", "none", 3.2) + path("M86 116 H94 M104 116 H112", "none", 2.8)
        + rect(88, 62, 22, 32, "#7B4FD6", 8, 3.0) + path("M90 70 L80 64", "none", 3.2)
        + G(74, 58, ell(0, 0, 8, 9, "#E33B3B", 2.6) + path("M4 6 L10 14", "none", 4.0), 30, 1.0)
        + circ(99, 50, 11, "#FFD7B5", 2.8)
        + path("M88 48 Q88 37 99 37 Q110 37 110 48 Q104 43 99 44 Q93 43 88 48Z", "#3A2A20", 2.0)
        + path("M109 42 Q120 44 118 56", "none", 4.4) + '<path d="M109 42 Q120 44 118 56" stroke="#3A2A20" stroke-width="2.6" fill="none"/>'
        + eye(94, 50, 0.5) + eye(101, 51, 0.5) + mouth(97, 56, 2.4, 1.6) + blush(91, 56, 2, 1.2))
ball = circ(50, 50, 4.6, "#FFFFFF", 2.2) + '<path d="M70 44 Q60 40 55 48" stroke="#FFFFFF" stroke-width="2" fill="none" stroke-dasharray="3 3"/>'
add("tt-tekstilshchiki-saratovskaya", ("#FFF4C8", "#E5B530"),
    table + girl + ball + sparkle(24, 32, 4) + sparkle(44, 22, 2.6),
    "девочка с тёмным хвостиком в фиолетовом спортивном костюме с красной ракеткой",
    "тренируется одна у теннисного стола, вторая половина которого поднята стенкой, — мячик отскакивает от неё обратно")

if __name__ == "__main__":
    only = sys.argv[1:]
    for pid, body in ICONS.items():
        if only and pid not in only:
            continue
        open(os.path.join(OUT, pid + ".svg"), "w").write(body)
    subj = os.path.join(OUT, "subjects.txt")
    have = {l.split(" — ")[0] for l in open(subj, encoding="utf-8")}
    with open(subj, "a", encoding="utf-8") as f:
        for pid, line in SUBJ.items():
            if pid not in have and (not only or pid in only):
                f.write(line + "\n")
    print(len(ICONS))
