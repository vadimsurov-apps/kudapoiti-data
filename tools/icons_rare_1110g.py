"""Иконки робота rare, 2026-11-10 (19 UTC) — места из tools/add_rare_1110g.py.
Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно — свой герой, своя сцена, компоновка и палитра.
Реестр subjects.txt проверен grep'ом: пьедестал «Чемпион» (Олонецкий), корзина-тележка (Tennis Capital Петровка),
пушка, трон, термометр — заняты и обойдены; судейская вышка, картуз-купец, ангар со снегом — свободны.
Запуск: python3 tools/icons_rare_1110g.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
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
    k = f"r7_{pid}"
    draw_icons.BG[k] = pal
    ICONS[pid] = svg(k, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def col(d, c, w):
    return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'


# 1. Tennis Capital (Мичуринский) — высокая судейская вышка с мордашкой, наверху на сиденье мяч в судейской кепке
add("tennis-capital-michurinsky", ("#E8F7FF", "#3A9AD9"),
    path("M-6 110 Q64 102 134 110 V140 H-6Z", "#3FA45B", 2.6) + col("M8 120 H120", "#FFFFFF", 2.6)
    # ножки вышки
    + col("M46 112 L54 62 M82 112 L74 62", O, 7) + col("M46 112 L54 62 M82 112 L74 62", "#FFFFFF", 4)
    + col("M50 92 H78 M52 78 H76", O, 5.5) + col("M50 92 H78 M52 78 H76", "#FFFFFF", 2.8)
    # кабина-сиденье с лицом
    + rect(42, 40, 44, 26, "#1E63D6", 6, 2.8)
    + face(64, 52, d=8, k=0.8)
    + rect(38, 36, 52, 7, "#FFFFFF", 3, 2.6)
    # мяч-судья в кепке
    + ball(64, 24, 12, 15) + face(64, 25, d=4.5, k=0.45, blush=False)
    + path("M53 17 Q64 6 75 17Z", "#E53935", 2.2) + path("M73 16 L84 18 L73 19Z", "#E53935", 1.8)
    # ракетка прислонена к ножке
    + G(100, 88, racket(0, 0, 18, 0.75, rim="#FF8A00", grip="#3B3355", strings="#FFD8A8"), 0)
    + sparkle(20, 30, 6) + sparkle(108, 40, 4.5) + sparkle(24, 64, 3.5),
    "белая судейская вышка теннисного корта с синей кабинкой-мордашкой",
    "стоит у края зелёного корта, на её верхушке сидит жёлтый мяч-судья в красной кепке, к ножке прислонена оранжевая ракетка")

# 2. Купцов теннис (Немчиновка) — мяч-купец в чёрном картузе и с усами на сундуке с мячами
add("kuptsov-tennis-nemchinovka", ("#FFF1DE", "#E39A4C"),
    path("M-6 112 Q64 106 134 112 V140 H-6Z", "#8D5A3B", 2.6)
    # сундук
    + rect(28, 74, 72, 40, "#B5651D", 6, 2.8)
    + rect(28, 74, 72, 10, "#8B4513", 4, 2.6)
    + col("M40 74 V114 M88 74 V114", "#FFC94D", 4) + col("M40 74 V114 M88 74 V114", O, 1.2)
    + rect(58, 86, 12, 12, "#FFC94D", 3, 2.2) + circ(64, 92, 2, O, 0)
    # мячи выглядывают из-под крышки
    + ball(36, 70, 7, 20) + ball(92, 70, 7, -30)
    # мяч-купец
    + ball(64, 46, 22, 0)
    + face(64, 46, d=8, k=0.75, mouth=False)
    + path("M52 56 Q58 52 64 56 Q70 52 76 56 Q70 60 64 57 Q58 60 52 56Z", "#5D3A1A", 2)
    + path("M42 34 Q44 18 64 18 Q84 18 86 34Z", "#2B2B3D", 2.6)
    + path("M40 34 H90 Q88 40 78 38 H40Z", "#2B2B3D", 2.4)
    + rect(44, 29, 40, 4, "#C62828", 1, 0)
    + sparkle(108, 26, 7, "#FFE14D") + sparkle(20, 40, 5) + sparkle(114, 52, 3.5),
    "жёлтый теннисный мяч-купец в чёрном картузе с красным околышем и пышными усами",
    "важно восседает на деревянном сундуке с золотыми полосами, из-под крышки выглядывают ещё два мяча")

# 3. Чемпион (Лобачевского) — ракетка с чемпионской лентой под тёплым куполом крытого корта, снаружи снег
add("champion-tennis-lobachevskogo", ("#EAF0FF", "#5C6BC0"),
    # снег снаружи
    "".join(circ(x, y, 2.2, "#FFFFFF", 0) for x, y in [(12, 30), (22, 50), (110, 26), (118, 52), (100, 12), (16, 74), (114, 80), (30, 14)])
    + path("M-6 112 Q64 108 134 112 V140 H-6Z", "#FFFFFF", 2.6)
    # купол-ангар
    + path("M18 112 V78 Q18 34 64 30 Q110 34 110 78 V112Z", "#FFD9A8", 2.8)
    + col("M40 112 V60 Q50 40 64 38 M88 112 V60 Q78 40 64 38", "#F4B26B", 2.4)
    + path("M26 112 H102", "none", 2.6)
    + rect(26, 104, 76, 8, "#2E9E6A", 2, 2.2)
    # ракетка-персонаж с лентой
    + G(64, 66, racket(0, 0, 0, 1.0, rim="#2E9E6A", grip="#3B3355", strings="#BFE8D2", head="#F2FFF8"), 0)
    + ell(64, 60, 13, 10, "#F2FFF8", 0) + face(64, 58, d=7, k=0.8)
    + path("M50 74 L79 90 L77 95 L48 79Z", "#E53935", 2)
    + circ(80, 94, 5, "#FFC94D", 2)
    # снег на крыше купола
    + path("M30 52 Q40 36 64 33 Q88 36 98 52 Q92 46 84 48 Q76 40 64 42 Q52 40 44 48 Q36 46 30 52Z", "#FFFFFF", 2.2)
    + ball(96, 98, 7, 30)
    + sparkle(64, 20, 6, "#FFE14D"),
    "зелёная ракетка-персонаж с красной чемпионской лентой через «плечо» и золотым значком",
    "стоит в тёплом крытом корте под оранжевым куполом-ангаром, а снаружи падает снег и лежат сугробы")

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
