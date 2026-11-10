"""Иконки робота rare, 2026-11-10 (16 UTC) — места из tools/add_rare_1110f.py.
Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно — свой герой, своя сцена, компоновка и палитра.
Реестр subjects.txt проверен grep'ом; заняты и обойдены: кенгуру, мяч-хоппер с рожками, светофор, лампочка-идея,
мяч/ракетка в очках у доски, свиристель в очках (Smart Tennis на Войковской), облачко-персонаж, пружинка-слинки.
Запуск: python3 tools/icons_rare_1110f.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
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
    k = f"r6_{pid}"
    draw_icons.BG[k] = pal
    ICONS[pid] = svg(k, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def col(d, c, w):
    return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'


# 1. Air Arena — большой спортивный батут олимпийского образца, над ним в высоком прыжке мальчик «звездой»
add("airarena-novaya-riga", ("#E6F2FF", "#4F7FE0"),
    path("M4 92 L22 74 H106 L124 92Z", "#E53935", 2.8)
    + path("M22 79 H106 L116 89 H12Z", "#2B2B3D", 2.4)
    + col("M30 82 Q64 94 98 82", "#4A4A66", 1.6)
    + path("M8 96 V122 M120 96 V122 M26 92 V114 M102 92 V114", "none", 5).replace(O, "#1E3A8A")
    + rect(2, 90, 124, 9, "#1E63D6", 4, 2.6)
    + face(64, 108, d=9, k=0.85)
    + col("M64 70 V60 M54 70 L50 64 M74 70 L78 64", "#FFFFFF", 2.2)
    # мальчик «звездой»
    + path("M58 42 L46 58 M70 42 L82 58", "none", 4.6).replace(O, "#1E3A8A") + path("M58 42 L46 58 M70 42 L82 58", "none", 1.8)
    + rect(55, 24, 18, 20, "#FF9800", 7, 2.6)
    + path("M57 28 L40 14 M71 28 L88 14", "none", 4).replace(O, "#FFD7B5") + path("M57 28 L40 14 M71 28 L88 14", "none", 1.6)
    + circ(39, 13, 3.6, "#FFD7B5", 2) + circ(89, 13, 3.6, "#FFD7B5", 2)
    + circ(64, 14, 9, "#FFD7B5", 2.4) + face(64, 14, d=3.6, k=0.42, blush=False)
    + path("M55 11 Q57 3 64 4 Q71 3 73 11 Q67 7 60 9Z", "#5D4037", 1.8)
    + sparkle(20, 36, 6) + sparkle(108, 40, 6) + sparkle(30, 60, 3.5),
    "большой спортивный батут олимпийского образца — синяя рама, красные маты, улыбка на чёрной сетке",
    "над ним в высоком прыжке «звездой» парит мальчик в оранжевой майке, раскинув руки и ноги")

# 2. НовоТеннис (Новогорск) — открылась банка новых мячей, крышка отлетела, мячи выпрыгивают
add("novotennis-novogorsk", ("#FFF6D8", "#F3B23F"),
    path("M-6 112 Q64 104 134 112 V140 H-6Z", "#2E9E6A", 2.6)
    + rect(42, 58, 44, 58, "#C9D3DE", 8, 2.8)
    + rect(42, 72, 44, 22, "#1E63D6", 0, 0) + rect(42, 58, 44, 58, "none", 8, 2.8)
    + col("M50 83 H78", "#FFFFFF", 3) + col("M54 89 H74", "#FFFFFF", 2)
    + face(64, 104, d=8, k=0.75)
    + ell(64, 58, 22, 5, "#E9EEF3", 2.6)
    # крышка отлетела
    + G(28, 34, ell(0, 0, 16, 5, "#FFFFFF", 2.6) + ell(0, -2, 14, 3, "#E53935", 0), -30)
    # три мяча
    + ball(62, 40, 10, 20) + ball(82, 24, 9, -30) + ball(98, 46, 8, 50)
    + col("M58 52 V48 M70 50 L74 44 M88 34 L92 30", "#FFFFFF", 2)
    + sparkle(112, 22, 6) + sparkle(16, 70, 5),
    "серебристая банка для теннисных мячей с синей этикеткой и мордашкой",
    "с хлопком открылась на зелёной траве: красная крышка отлетела в сторону, а три новеньких жёлтых мяча выпрыгивают вверх")

# 3. Теннис Класс — мяч на ободе ракетки показывает «класс!» большим пальцем
add("tennis-klass-verkhoyanskaya", ("#FBE6FF", "#C46FE0"),
    G(70, 74, racket(0, 0, 58, 2.0, rim="#7B3FB5", grip="#2B2B3D", strings="#D8C4EA", head="#F8F0FF"), 0)
    + G(44, 46, ball(0, 0, 20, -15) + face(0, 2, d=7, k=0.75), 0)
    # белая перчатка-кулачок с поднятым большим пальцем
    + rect(62, 46, 18, 16, "#FFFFFF", 6, 2.4)
    + col("M62 51 H72 M62 56 H72", O, 1.6)
    + rect(66, 26, 8, 22, "#FFFFFF", 4, 2.4)
    + path("M26 46 Q16 52 18 62", "none", 3).replace(O, "#FFFFFF") + path("M26 46 Q16 52 18 62", "none", 1.6)
    + sparkle(92, 22, 7, "#FFE14D") + sparkle(108, 36, 4, "#FFE14D") + sparkle(20, 22, 5),
    "жёлтый теннисный мяч с белой ручкой-перчаткой",
    "уселся на ободок лиловой ракетки, лежащей наискосок, и показывает большой палец вверх — «класс!»")

# 4. Smart Tennis (Петровско-Разумовский) — ракетка-умница держит собранный кубик Рубика
add("smart-tennis-petrovsko-razumovsky", ("#E4FFF0", "#3EB489"),
    path("M-6 108 Q64 100 134 108 V140 H-6Z", "#4C8BF5", 2.6) + col("M10 118 H118", "#FFFFFF", 2.4)
    + G(58, 58, racket(0, 0, -12, 2.0, rim="#FF7A2F", grip="#3B3355", strings="#FFC9A6", head="#FFF6EF"), 0)
    + G(56, 54, face(0, 0, d=8, k=0.8), -12)
    # рука к кубику
    + path("M80 66 Q90 56 94 44", "none", 4).replace(O, "#FF7A2F") + path("M80 66 Q90 56 94 44", "none", 1.6)
    # кубик Рубика (изометрия)
    + G(100, 30, path("M0 -12 L13 -5 L0 2 L-13 -5Z", "#FFE14D", 2.2)
        + path("M-13 -5 L0 2 V16 L-13 9Z", "#E53935", 2.2)
        + path("M13 -5 L0 2 V16 L13 9Z", "#1E63D6", 2.2)
        + col("M-6.5 -8.5 L6.5 -1.5 M6.5 -8.5 L-6.5 -1.5 M-13 0 L0 7 M-13 4.5 L0 11.5 M13 0 L0 7 M13 4.5 L0 11.5 "
              "M-8.7 -2.7 V11.3 M-4.3 -0.3 V13.7 M4.3 -0.3 V13.7 M8.7 -2.7 V11.3", O, 1.2), 0)
    + ball(26, 96, 9, 10)
    + sparkle(114, 58, 6) + sparkle(84, 14, 4) + sparkle(20, 32, 5),
    "оранжевая ракетка-умница с мордашкой на струнах",
    "стоит на синем корте и гордо поднимает над собой только что собранный кубик Рубика, у ног — жёлтый мяч")

if __name__ == "__main__":
    only = set(sys.argv[1:])
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
