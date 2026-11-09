"""Иконка робота rare, 2026-11-09 (вечер) — место из tools/add_rare_1109f.py.
АБСОЛЮТНАЯ уникальность: просмотрены листы icons-catalog 28 (картинг — карты сбоку со зверятами-пилотами, шины, руль,
дрифт в дыму, тучка с дождём), 45, 51 и реестр subjects.txt (нет ни ледовой трассы, ни якоря на карте).
Запуск: python3 tools/icons_rare_1109f.py → icons-src/<id>.svg + строка реестра в subjects.txt"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, eye, face, sparkle, O
from icons_sections_1107c import G
from icons_sections_1108g import rect, circ, ell, path, SKIN

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
draw_icons.BG.update({"rf_ice": ("#F4FCFF", "#6FA8DC")})


def add(pid, bg, body, hero, scene):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def flake(x, y, r):
    return path(f"M{x-r} {y} H{x+r} M{x} {y-r} V{y+r} M{x-r*.7} {y-r*.7} L{x+r*.7} {y+r*.7} M{x-r*.7} {y+r*.7} L{x+r*.7} {y-r*.7}",
                "none", 1.8).replace(O, "#ffffff", 1)


def anchor(x, y, k=1.0):
    return G(x, y, circ(0, -9, 3, "none", 2.4).replace(O, "#C98A00", 1)
             + path("M0 -6 V9 M-5 -2 H5 M-9 3 Q-8 11 0 10 Q8 11 9 3", "none", 2.6).replace(O, "#C98A00", 1)
             + path("M0 -6 V9 M-5 -2 H5 M-9 3 Q-8 11 0 10 Q8 11 9 3", "none", 1.3).replace(O, "#FFD54F", 1), 0, k)


# Нахимов (Вялки): открытая трасса, зимой — по льду; имя адмирала — золотой якорь на носу карта
ice = (path("M-4 84 Q64 70 132 82 L132 132 L-4 132Z", "#E8F5FF", 2.4)
       + path("M10 112 Q40 92 78 104 Q104 112 122 98", "none", 3).replace(O, "#A9CDEB", 1)
       + path("M4 124 Q46 104 86 116", "none", 2.4).replace(O, "#C4DDF2", 1))
spray = "".join(G(x, y, path("M0 -4 L3 0 L0 4 L-3 0Z", "#FFFFFF", 1.4), r) for x, y, r in
                [(10, 96, 10), (6, 84, -20), (18, 82, 30), (4, 106, 0), (20, 104, 45), (12, 72, 15)])
driver = (path("M-10 -14 Q-6 -6 4 -9", "none", 6).replace(O, "#FF8A3D", 1)
          + circ(-6, -25, 12, "#FF8A3D", 2.6) + path("M-17 -30 Q-6 -40 5 -30", "none", 2.4).replace(O, "#FFFFFF", 1)
          + circ(-3, -24, 7.5, SKIN, 2.2) + eye(-6, -25, .42) + eye(0, -25, .42)
          + path("M-5 -21 Q-3 -19 -1 -21", "none", 1.4))
kart = G(0, 0,
         path("M-38 4 L-31 -8 L16 -8 L34 -1 L38 8 L-38 8Z", "#1F4FB5", 2.8)
         + path("M-28 -2 H26", "none", 2).replace(O, "#FFFFFF", 1)
         + rect(-43, -12, 8, 15, "#2B2B2B", 2, 2.2)
         + driver
         + path("M8 -8 L2 -20", "none", 3) + path("M-1 -22 L6 -18", "none", 3.4)
         + anchor(27, -1, 0.8)
         + eye(10, 0, .5) + eye(18, 0, .5)
         + path("M11 4 Q14 7 17 4", "none", 1.6)
         + circ(-25, 12, 10, "#2B2B2B", 2.6) + circ(-25, 12, 4, "#BDBDBD", 1.6)
         + circ(25, 12, 10, "#2B2B2B", 2.6) + circ(25, 12, 4, "#BDBDBD", 1.6)
         + "".join(path(f"M{cx-7} {12+dy} l2 -2 M{cx+5} {12+dy} l2 -2", "none", 1.2).replace(O, "#FFFFFF", 1)
                   for cx in (-25, 25) for dy in (-6, 7)))
add("nahimov-karting-vyalki", "rf_ice",
    ice + spray
    + G(64, 78, kart, 6, 1.16)
    + flake(20, 30, 5) + flake(104, 24, 4) + flake(60, 16, 3.5) + flake(116, 52, 3) + flake(36, 50, 3)
    + sparkle(92, 40, 4),
    "тёмно-синий карт с белой полосой, шипами на колёсах и маленьким золотым якорем на носу",
    "заносит боком на ледовой зимней трассе под открытым небом — из-под колёс летят ледяные искры, падают снежинки")

if __name__ == "__main__":
    only = set(sys.argv[1:])
    for pid, s_ in ICONS.items():
        if not only or pid in only:
            open(os.path.join(OUT, pid + ".svg"), "w").write(s_)
    reg = os.path.join(OUT, "subjects.txt")
    keep = [l for l in open(reg).read().splitlines() if l.split(" — ")[0] not in SUBJ]
    open(reg, "w").write("\n".join(keep + [SUBJ[p] for p in SUBJ]) + "\n")
    print("icons", len(ICONS))
