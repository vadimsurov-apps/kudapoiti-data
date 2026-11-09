"""Иконки робота rare, 2026-11-09 (03 UTC) — места из tools/add_rare_1109b.py.
Правило АБСОЛЮТНОЙ уникальности: каждая придумана отдельно (свой герой, сцена, компоновка, палитра).
Перед рисованием просмотрены все 46 листов icons-catalog и subjects.txt; заняты и НЕ использованы: кенгуру, комета,
пропеллер у мяча/кепки, кукурузник, ушанка, помпон, силач, наушники, большая и маленькая ракетки, корона.
Запуск: python3 tools/icons_rare_1109b.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, eye, face, sparkle, O
from icons_sections_1107c import G
from icons_sections_1108b import limb
from icons_sections_1108g import rect, circ, ell, path, SKIN
from icons_rare_1109 import kart, padel

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
draw_icons.BG.update({
    "rb_palace": ("#F7F0FF", "#9C7BD6"), "rb_under": ("#5C6B8A", "#1F2638"), "rb_air": ("#F2FBFF", "#8CC7EA"),
    "rb_river": ("#E8F6FF", "#3F8FD0"), "rb_radio": ("#FFF8E6", "#F2A93B"), "rb_turtle": ("#F4FFF2", "#5DB37A"),
    "rb_pump": ("#FFF3EC", "#E2774F"),
})
LIME = "#D7F25A"


def add(pid, bg, body, hero, scene):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def lime(x, y, r=8, fc=False, k=0.4):
    b = circ(x, y, r, LIME, 2.4) + path(f"M{x-r*.8} {y-r*.4} Q{x} {y+r*.35} {x+r*.8} {y-r*.4}", "none", 1.6).replace(O, "#fff", 1)
    return b + (face(x, y, r * .4, k) if fc else "")


# 1. Дворец творчества на Миусах — мальчик в белом шлеме показывает «класс» из красного карта
kid = (G(-6, -14,
         limb("M6 4 L20 -10", "#1E63D6", 6) + circ(21, -13, 4.5, SKIN, 2.2) + path("M21 -17 V-24", "none", 3.4).replace(O, SKIN, 1)
         + path("M21 -17 V-24", "none", 1.4)
         + circ(0, -6, 12, SKIN, 2.4)
         + path("M-12 -7 Q-12 -20 0 -20 Q12 -20 12 -7 Z", "#FFFFFF", 2.4) + path("M-12 -10 H12", "none", 3).replace(O, "#1E63D6", 1)
         + face(0, -3, 4.5, 0.42)))
add("karting-dtdm-miusy", "rb_palace",
    path("M-6 106 H134 V140 H-6Z", "#C99A5E", 2.4)
    + "".join(path(f"M{x} 106 V140", "none", 1.4).replace(O, "#A87A44", 1) for x in range(6, 128, 18))
    + G(60, 86, kart("#E53935", 1.3, driver=kid))
    + sparkle(106, 34, 6, "#FFF3A6") + sparkle(92, 22, 3.5, "#FFF3A6"),
    "мальчик-кружковец в белом шлеме с синей полосой",
    "показывает большой палец, сидя в красном карте на паркете дворца творчества")

# 2. Liberty Karting под МЕГОЙ — лампа паркинга освещает синий карт
add("karting-liberty-teply-stan", "rb_under",
    path("M-6 100 H134 V140 H-6Z", "#3A4257", 2.4)
    + "".join(rect(x, 112, 12, 4, "#F5D547", 1, 0) for x in (4, 34, 64, 94, 124))
    + path("M64 -4 V14", "none", 2.4)
    + path("M44 26 L64 12 L84 26 Z", "#FFD54F", 2.4)
    + face(64, 20, 5, 0.38)
    + path("M42 28 L20 96 H108 L86 28 Z", "#FFF3B0", 0).replace("<path", '<path opacity=".28"', 1)
    + G(62, 82, kart("#1E63D6", 1.25,
                     driver=G(-8, -16, circ(0, 0, 11, "#F2F2F2", 2.4) + rect(-9, -3, 18, 7, "#263238", 3, 1.8)))),
    "жёлтая лампа подземного паркинга с лицом",
    "светит сверху на синий карт, проносящийся по подземной трассе")

# 3. ADM Karting у аэродрома Мячково — карт с пропеллером на носу на взлётной полосе
add("karting-adm-myachkovo", "rb_air",
    path("M-6 98 L134 92 V140 H-6Z", "#8E9AA6", 2.4)
    + "".join(path(f"M{x} {97 - x*0.043:.1f} h12", "none", 3).replace(O, "#ffffff", 1) for x in (2, 30, 58, 86, 114))
    + path("M18 30 q8 -9 18 -2 q8 -6 14 3Z", "#fff", 2) + path("M94 44 q6 -6 12 -1 q6 -4 10 2Z", "#fff", 2)
    + G(58, 80, kart("#43A047", 1.3,
                     driver=G(-8, -16, circ(0, 0, 11, "#FF8F00", 2.4) + rect(-9, -3, 18, 7, "#3B3355", 3, 1.8)))
        + circ(46, 6, 4, "#FFD54F", 2) + ell(46, -6, 3.2, 11, "#ECEFF1", 2) + ell(46, 18, 3.2, 11, "#ECEFF1", 2)
        + path("M-48 14 l-10 -2 M-50 4 l-12 0", "none", 2).replace(O, "#ffffff", 1)),
    "зелёный карт с пропеллером на носу, как у самолёта",
    "разгоняется по взлётной полосе аэродрома с белой разметкой")

# 4. «Папа Падел» у Речного вокзала — усатая ракетка-папа держит на макушке мяч-малыша
add("padel-papa-rechnoy", "rb_river",
    path("M-6 104 q16 -7 32 0 t32 0 t32 0 t32 0 t32 0 V140 H-6Z", "#5BB2F0", 2.2)
    + G(64, 66, padel("#2E5BBA", 25, 29)
        + eye(-8, -4, .62) + eye(8, -4, .62)
        + path("M-1 6 Q-10 2 -16 9 Q-9 8 -1 10 Q9 8 16 9 Q10 2 1 6Z", "#5D4037", 1.8)
        + ell(-15, 4, 4, 2.4, "#FF7FA8", 0).replace("<ellipse", '<ellipse opacity=".6"', 1)
        + ell(15, 4, 4, 2.4, "#FF7FA8", 0).replace("<ellipse", '<ellipse opacity=".6"', 1))
    + lime(64, 26, 9, True, 0.36),
    "усатая синяя падел-ракетка-папа",
    "держит на макушке лаймовый мяч-малыша у реки")

# 5. «Падел 77» на Сигнальном проезде — ракетка-рация передаёт сигнал мячу
add("padel-77-signalny", "rb_radio",
    G(54, 70, path("M14 -26 L22 -50", "none", 3.4) + circ(22, -51, 3.2, "#E53935", 2)
        + padel("#F57C00", 24, 28) + rect(-12, 8, 24, 9, "#3B3355", 3, 1.6)
        + "".join(rect(-9 + i * 6, 10, 4, 5, "#9CE37D", 1, 0) for i in range(3))
        + face(0, -8, 7, 0.5), -8)
    + path("M84 40 q8 8 0 18", "none", 2.6) + path("M90 34 q13 14 0 30", "none", 2.6)
    + lime(108, 50, 9, True, 0.36),
    "оранжевая падел-ракетка-рация с антенной",
    "передаёт сигнал дугами-волнами лаймовому мячу")

# 6. «Моспадел» — ракетка-черепаха ползёт к мячу
add("padel-mospadel-dmitrovskoe", "rb_turtle",
    path("M-6 108 H134 V140 H-6Z", "#7CC576", 2.4)
    + G(56, 72,
        ell(-24, 22, 8, 5, "#A5D6A7", 2.2) + ell(20, 24, 8, 5, "#A5D6A7", 2.2)
        + circ(30, -4, 11, "#A5D6A7", 2.4) + eye(28, -6, .5) + eye(35, -6, .5)
        + path("M27 2 Q31 5 35 2", "none", 1.8)
        + G(0, 0, padel("#26A69A", 26, 22), 90), -4)
    + lime(108, 96, 8)
    + path("M92 98 h-6 M92 92 h-4", "none", 2),
    "бирюзовая падел-ракетка-черепаха: голова и лапки торчат из-под ракетки с дырочками",
    "медленно, но верно ползёт по траве к лаймовому мячу")

# 7. Памп-трек на Щукинском полуострове — беговел-персонаж катится с волны
bike = (path("M-18 10 L0 -6 L16 10", "none", 4).replace(O, "#E53935", 1) + path("M-18 10 L0 -6 L16 10", "none", 1.4)
        + path("M0 -6 L-4 -14", "none", 3) + path("M-10 -15 H2", "none", 3.4)
        + path("M16 10 L14 -12 L22 -16", "none", 3) + circ(-18, 12, 10, "#2B2B2B", 2.6) + circ(-18, 12, 3.6, "#E0E0E0", 1.6)
        + circ(16, 12, 10, "#2B2B2B", 2.6) + circ(16, 12, 3.6, "#E0E0E0", 1.6)
        + face(0, 0, 4.5, 0.42, blush=True))
add("pumptrack-strogino", "rb_pump",
    path("M-6 96 Q18 70 42 92 Q66 112 90 86 Q112 64 134 84 V140 H-6Z", "#B98B6A", 2.6)
    + path("M-6 112 q20 -6 40 0 t40 0 t40 0 t40 0 V140 H-6Z", "#64B5F6", 2)
    + G(62, 62, bike, 16, 1.6)
    + path("M30 56 h-12 M32 64 h-14", "none", 2.2).replace(O, "#ffffff", 1),
    "красный беговел с мордашкой на раме",
    "скатывается с земляной волны памп-трека у реки")

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for pid, body in ICONS.items():
        open(os.path.join(OUT, f"{pid}.svg"), "w").write(body)
    reg = os.path.join(OUT, "subjects.txt")
    have = {l.split(" — ")[0] for l in open(reg, encoding="utf-8")}
    with open(reg, "a", encoding="utf-8") as f:
        for pid, line in SUBJ.items():
            if pid not in have:
                f.write(line + "\n")
    print(len(ICONS), "icons")
