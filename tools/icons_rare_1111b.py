"""Иконки робота rare, 2026-11-11 (04 UTC) — места из tools/add_rare_1111b.py.
Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно. Перед рисованием просмотрены листы icons-catalog
и реестр subjects.txt (grep: карабин, коляска, облачко-реплика, лиана, тарзанка, качели, буква на батуте — заняты как
герои; облачко-реплика с буквами на батуте и живая лиана-верёвка с ребёнком между платформами — свободны).
Запуск: python3 tools/icons_rare_1111b.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, face, sparkle, eye, O, s
from icons_sections_1108g import rect, circ, ell, path

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}


def add(pid, pal, body, hero, scene):
    k = f"r10_{pid}"
    draw_icons.BG[k] = pal
    ICONS[pid] = svg(k, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


# 1. LinguaGym — языковой спортивный центр: облачко-реплика с буквами подпрыгивает на большом батуте
tramp = (
    path("M22 104 L30 120 M106 104 L98 120 M64 108 V122", "none", 3.2)          # ножки
    + ell(64, 100, 46, 13, "#2E6FD8", 3.0)                                       # рама
    + ell(64, 99, 38, 9, "#1C2B4A", 0)                                           # сетка
    + "".join(f'<path d="M{x} 92 v14" stroke="#FFD54F" stroke-width="2"/>' for x in (30, 44, 84, 98))
    + ell(64, 100, 46, 13, "none", 3.0)
)
bubble = (
    path("M30 28 Q30 14 46 14 H84 Q100 14 100 28 V52 Q100 66 84 66 H60 L46 78 L49 66 H46 Q30 66 30 52Z", "#FFFFFF", 3.0)
    + '<text x="65" y="37" font-family="Arial Black, Arial, sans-serif" font-weight="900" font-size="15" '
      'text-anchor="middle" fill="#E8414F">A<tspan fill="#2E6FD8">Б</tspan><tspan fill="#2FAE5B">C</tspan></text>'
    + face(65, 49, d=9, k=0.62)
)
arcs = ('<path d="M18 70 Q14 58 20 46 M110 70 Q114 58 108 46" fill="none" stroke="#fff" stroke-width="3" '
        'stroke-linecap="round" opacity=".9"/>')
add("trampoline-linguagym-dolgoprudny", ("#EAF9D6", "#8FD15A"),
    tramp + '<ellipse cx="64" cy="98" rx="14" ry="3" fill="#000" opacity=".25"/>' + bubble + arcs
    + sparkle(20, 26, 5) + sparkle(110, 86, 4),
    "белое облачко-реплика с разноцветными буквами «АБС» и улыбкой",
    "подпрыгивает высоко над большим синим батутом с жёлтыми пружинами, по бокам — дуги прыжка")

# 2. «Лиана парк» — живая лиана с листочками, на которой ребёнок в каске перелетает между двумя платформами на деревьях
trees = (
    rect(10, 34, 14, 96, "#8A5A3B", 3, 3.0) + rect(104, 34, 14, 96, "#8A5A3B", 3, 3.0)
    + rect(4, 86, 32, 8, "#C98B52", 2, 2.6) + rect(92, 86, 32, 8, "#C98B52", 2, 2.6)            # платформы
    + path("M24 92 Q64 112 104 92", "none", 2.4)                                                  # страховочный трос
    + path("M-8 26 Q30 0 64 12 Q98 0 136 26 V-8 H-8Z", "#5DBB63", 3.0)                            # крона сверху
)
LP = "M64 14 Q54 30 62 44 Q72 56 70 66"
liana = (
    path(LP, "none", 9.5)
    + f'<path d="{LP}" fill="none" stroke="#3FA34D" stroke-width="6.5" stroke-linecap="round"/>'
    + "".join(path(f"M{x} {y} q{dx} -7 {dx*2} 0 q-{dx} 7 -{dx*2} 0Z", "#8BE06A", 2.2)
              for x, y, dx in ((56, 24, -7), (66, 40, 7), (70, 56, 7)))
    + eye(55, 33, 0.5) + eye(62, 34, 0.5)
    + '<path d="M55 39 Q58.5 42 62 39" fill="none" stroke="#3B3355" stroke-width="2" stroke-linecap="round"/>'
)
kid = (
    path("M70 66 L62 80 M70 66 L78 80", "none", 3.2)                    # руки держат лиану
    + rect(60, 84, 20, 17, "#FF7A45", 6, 2.8)                            # куртка
    + path("M63 101 L56 112 M77 101 L86 110", "none", 3.4)              # ноги в полёте
)
head = (circ(70, 78, 9, "#FFD7B5", 2.6) + path("M60.5 76 Q70 63 79.5 76Z", "#FFD54F", 2.4)
        + eye(67, 80, 0.42) + eye(73, 80, 0.42))
add("ropes-liana-park-serpukhov", ("#FFF1D6", "#F4A259"),
    trees + liana + kid + head
    + '<path d="M40 70 Q48 64 56 66 M36 78 Q44 72 52 74" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" opacity=".85"/>'
    + sparkle(100, 40, 4.5) + sparkle(28, 46, 3.5),
    "зелёная лиана-верёвка с глазками и листочками",
    "свисает с ветки над лесом и переносит ребёнка в жёлтой каске от одной деревянной платформы на сосне к другой")

if __name__ == "__main__":
    reg = os.path.join(OUT, "subjects.txt")
    have = open(reg, encoding="utf-8").read()
    lines = []
    for pid, code in ICONS.items():
        open(os.path.join(OUT, f"{pid}.svg"), "w").write(code)
        if f"\n{pid} — " not in "\n" + have:
            lines.append(SUBJ[pid])
    if lines:
        with open(reg, "a", encoding="utf-8") as f:
            f.write(("" if have.endswith("\n") else "\n") + "\n".join(lines) + "\n")
    print(len(ICONS), "icons;", len(lines), "registry lines")
