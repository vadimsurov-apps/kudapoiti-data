"""Иконки робота rare, 2026-11-10 (09–10 UTC) — места из tools/add_rare_1110d.py.
Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно — свой герой, своя сцена, компоновка и палитра.
Просмотрены все листы icons-catalog (сводки 3×3) и реестр subjects.txt; заняты и заменены: волан/мяч-спутник у Земли,
геккон и ящерица на стене, олимпийский факел, мяч-планета, красный тубус для мячей, карты в пламени/змейкой/с зубами.
Запуск: python3 tools/icons_rare_1110d.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, eye, face, sparkle, O
from icons_sections_1107c import G
from icons_sections_1108g import rect, circ, ell, path
from icons_rare_1110b import racket, ball

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}


def add(pid, pal, body, hero, scene):
    k = f"r4_{pid}"
    draw_icons.BG[k] = pal
    ICONS[pid] = svg(k, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


# 1. «Столица Карт» — синий карт мчится вдоль кремлёвской стены
merlons = "".join(path(f"M{x} 52 V40 L{x+4} 45 L{x+8} 40 V52Z", "#C62828", 2.2) for x in range(-4, 132, 16))
add("stolica-kart-skladochnaya", ("#FFF1DC", "#E9A15A"),
    merlons
    + rect(-6, 50, 140, 30, "#C62828", 0, 2.6)
    + "".join(path(f"M{x} 58 h10 M{x+8} 68 h10", "none", 1.4).replace(O, "#8E1B1B") for x in range(0, 128, 20))
    + rect(-6, 80, 140, 60, "#9E9E9E", 0, 2.6)
    + "".join(path(f"M{x} 92 h12 M{x+8} 104 h12 M{x} 116 h12", "none", 1.4).replace(O, "#6D6D6D") for x in range(0, 128, 22))
    + path("M8 86 H30 M4 96 H24 M10 106 H28", "none", 3).replace(O, "#FFFFFF")
    # карт
    + G(-12, 0, circ(48, 106, 10, "#37474F", 2.8) + circ(48, 106, 4, "#B0BEC5", 2)
    + circ(100, 106, 10, "#37474F", 2.8) + circ(100, 106, 4, "#B0BEC5", 2)
    + path("M34 98 Q36 84 52 84 H92 Q112 84 116 98 Q116 104 108 104 H40 Q34 104 34 98Z", "#1E63D6", 2.8)
    + path("M60 84 Q62 70 74 70 Q84 70 86 84Z", "#FFC107", 2.6)
    + rect(66, 64, 14, 10, "#FFFFFF", 5, 2.2)
    + path("M106 92 l3 -2 l1 3.5 l3.6 0 l-3 2.2 l1.2 3.4 l-2.8 -2 l-3 2 l1.2 -3.4 l-3 -2.2Z", "#E53935", 1.2)
    + eye(98, 94, 0.55) + eye(110, 95, 0.45)
    + path("M100 101 Q106 103 112 100", "none", 2), 0)
    + path("M30 70 l-14 0 M28 78 l-18 0", "none", 2.6).replace(O, "#FFFFFF"),
    "синий гоночный карт с глазками-фарами и красной звёздочкой на носу",
    "мчится по серой брусчатке вдоль красной зубчатой стены, за ним белые полоски скорости")

# 2. Клаймберс (2-я Песчаная) — фенёк лезет по песочной стене с зацепами
holds = [(30, 30, "#E53935"), (88, 26, "#43A047"), (46, 58, "#1E88E5"), (100, 60, "#8E24AA"),
         (26, 90, "#FB8C00"), (82, 104, "#00ACC1"), (54, 112, "#E53935")]
add("climbers-club-peschanaya", ("#FFF6D8", "#E6B85C"),
    path("M14 0 L118 0 L124 128 L4 128Z", "#F4D58D", 2.6)
    + "".join(path(f"M{x-6} {y+4} Q{x-6} {y-6} {x} {y-6} Q{x+7} {y-6} {x+7} {y+2} Q{x+2} {y+7} {x-6} {y+4}Z", c, 2.2)
              for x, y, c in holds)
    + path("M66 -4 V40", "none", 2.6).replace(O, "#D32F2F")
    # фенёк
    + G(66, 72,
        path("M-10 -26 L-24 -52 L-2 -32Z", "#F6C48E", 2.6) + path("M10 -26 L24 -52 L2 -32Z", "#F6C48E", 2.6)
        + path("M-9 -30 L-18 -46 L-4 -33Z", "#FFD6E0", 0) + path("M9 -30 L18 -46 L4 -33Z", "#FFD6E0", 0)
        + ell(0, -18, 15, 13, "#F6C48E", 2.6)
        + ell(0, -12, 8, 6, "#FFF3E0", 0)
        + eye(-6, -20, 0.55) + eye(6, -20, 0.55) + circ(0, -13, 2.2, O, 0)
        + path("M-3 -9 Q0 -6 3 -9", "none", 1.8)
        + ell(0, 8, 12, 15, "#F6C48E", 2.6)
        + path("M-12 4 H12 M-11 12 H11", "none", 3).replace(O, "#1565C0")
        + path("M-10 -2 L-22 -26 M10 -2 L20 -30", "none", 5).replace(O, "#F6C48E")
        + path("M-10 -2 L-22 -26 M10 -2 L20 -30", "none", 1.2)
        + path("M-8 20 L-16 34 M8 20 L14 36", "none", 5).replace(O, "#F6C48E")
        + path("M10 18 Q30 22 26 40", "none", 7).replace(O, "#F6C48E"), 0)
    + sparkle(112, 112, 5),
    "лисёнок-фенёк с огромными ушами в синей страховочной обвязке",
    "карабкается по песочно-жёлтой стене с разноцветными зацепами на красной страховочной верёвке")

# 3. Sputnik — рыжая лайка в козырьке держит ракетку в зубах на грунтовом корте
add("sputnik-tennis-zhivopisnaya", ("#FFE6D6", "#D9673C"),
    rect(-6, 92, 140, 50, "#C8553D", 0, 2.6)
    + path("M-6 100 H134", "none", 3).replace(O, "#FFFFFF")
    + ell(60, 92, 30, 22, "#E8A25B", 2.8)
    + path("M42 104 V118 M54 106 V120 M70 106 V120 M80 104 V118", "none", 6).replace(O, "#E8A25B")
    + path("M86 86 Q100 74 98 62", "none", 6).replace(O, "#E8A25B")
    + G(46, 56,
        path("M-18 -10 L-22 -34 L-6 -20Z", "#E8A25B", 2.6) + path("M18 -10 L22 -34 L6 -20Z", "#E8A25B", 2.6)
        + ell(0, 0, 22, 19, "#E8A25B", 2.8)
        + path("M-8 -6 Q0 -16 8 -6 Q14 4 10 12 Q0 18 -10 12 Q-14 4 -8 -6Z", "#FFFFFF", 0)
        + path("M-24 -12 Q0 -26 24 -12 L22 -8 Q0 -18 -22 -8Z", "#FFFFFF", 2.2)
        + path("M-24 -12 Q-34 -8 -34 -4 L-22 -8", "#FFFFFF", 2.2)
        + eye(-8, -2, 0.55) + eye(8, -2, 0.55) + ell(0, 6, 3.4, 2.6, O, 0)
        + ell(-15, 6, 3.6, 2.2, "#FF7FA8", 0) + ell(15, 6, 3.6, 2.2, "#FF7FA8", 0), 0)
    + racket(84, 52, 62, 0.62, rim="#1E88E5")
    + ball(98, 112, 7),
    "рыжая собачка-лайка с белой мордочкой в белом теннисном козырьке",
    "сидит на терракотовом грунтовом корте и гордо держит в зубах синюю теннисную ракетку")

# 4. «Олимпиец» — тележка тренера с мячами-учениками на синем харде
add("olimpiets-tennis-chobotovskaya", ("#E3F0FF", "#2F6FD6"),
    rect(-6, 96, 140, 40, "#2A5DB0", 0, 2.6)
    + path("M-6 104 H134 M64 104 V136", "none", 2.6).replace(O, "#FFFFFF")
    + path("M34 46 H94 L88 92 H40Z", "#B0BEC5", 2.8)
    + "".join(path(f"M{x} 48 L{x - 2 + (x - 64) * 0.08:.1f} 90", "none", 1.6) for x in range(44, 92, 8))
    + path("M36 64 H92 M38 78 H90", "none", 1.6)
    + ball(50, 42, 8, 20) + ball(66, 38, 8, -15) + ball(80, 43, 8, 40)
    + G(64, 70, rect(-14, -8, 28, 18, "#FFFFFF", 8, 2.2) + face(0, 0, d=6, k=0.5), 0)
    + path("M94 46 L104 30 H112", "none", 3)
    + circ(46, 98, 6, "#455A64", 2.4) + circ(82, 98, 6, "#455A64", 2.4)
    + G(24, 30, ball(0, 0, 8, 10) + face(0, 0, d=3.5, k=0.35, mouth=False), 0)
    + G(108, 72, ball(0, 0, 8, -30) + face(0, 0, d=3.5, k=0.35, mouth=False), 0)
    + path("M22 42 q2 8 10 12 M110 84 q-4 6 -12 8", "none", 2).replace(O, "#FFFFFF"),
    "серебристая сетчатая тележка-корзина тренера на колёсиках с мордашкой",
    "катится по синему харду, а из неё выпрыгивают жёлтые мячи-ученики")

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for pid, b in ICONS.items():
        open(os.path.join(OUT, f"{pid}.svg"), "w").write(b)
    reg = os.path.join(OUT, "subjects.txt")
    have = {l.split(" — ")[0] for l in open(reg, encoding="utf-8")}
    with open(reg, "a", encoding="utf-8") as f:
        for pid, line in SUBJ.items():
            if pid not in have:
                f.write(line + "\n")
    print(len(ICONS), "icons")
