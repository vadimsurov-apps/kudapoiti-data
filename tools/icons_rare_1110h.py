"""Иконки робота rare, 2026-11-10 (22 UTC) — места из tools/add_rare_1110h.py.
Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно. Перед рисованием просмотрены все 66 листов
icons-catalog и реестр subjects.txt (grep): гамак, гуськом, маяк, ракета, пилот, стеклянная стенка, арфа — заняты;
ракетка-рама для портрета и падел-ракетка-жонглёр — свободны.
Запуск: python3 tools/icons_rare_1110h.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, face, sparkle, O
from icons_sections_1107c import G
from icons_sections_1108g import rect, circ, ell, path
from icons_rare_1110b import ball

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}


def add(pid, pal, body, hero, scene):
    k = f"r8_{pid}"
    draw_icons.BG[k] = pal
    ICONS[pid] = svg(k, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


LIME = "#D7F53C"

# 1. Дмитровская теннисная академия — ракетка-рама на стене почёта, в ней портрет мяча-чемпиона в лавровом венке
strings = "".join(f'<path d="M{x} 20 V100" stroke="#C9B48A" stroke-width="1.6"/>' for x in range(42, 87, 9)) + \
          "".join(f'<path d="M30 {y} H98" stroke="#C9B48A" stroke-width="1.6"/>' for y in range(28, 97, 10))
leaf = lambda x, y, r: G(x, y, ell(0, 0, 3.2, 6.5, "#4CAF50", 1.6), r)
add("tennis-dmitrov-academy", ("#FFF3DC", "#E9A04F"),
    # гвоздик и шнурок на стене
    path("M64 2 L50 14 M64 2 L78 14", "none", 2.2) + circ(64, 3, 2.6, "#B0B0B0", 1.6)
    # ручка ракетки вниз
    + path("M58 98 L60 112 H68 L70 98", "#7A1F2B", 2.6)
    + rect(59, 110, 10, 22, "#3B3355", 4, 2.4) + path("M60 116 H68 M60 122 H68", "none", 1.2).replace(O, "#8E86A8")
    # голова ракетки — рама
    + ell(64, 58, 36, 44, "#FFF8E8", 0)
    + f'<clipPath id="dmf"><ellipse cx="64" cy="58" rx="34" ry="42"/></clipPath><g clip-path="url(#dmf)">{strings}</g>'
    + f'<ellipse cx="64" cy="58" rx="34" ry="42" fill="none" stroke="#9C2A3A" stroke-width="8"/>'
    + f'<ellipse cx="64" cy="58" rx="38.5" ry="46.5" fill="none" stroke="{O}" stroke-width="2.6"/>'
    + f'<ellipse cx="64" cy="58" rx="29.5" ry="37.5" fill="none" stroke="{O}" stroke-width="1.8"/>'
    # мяч-чемпион в венке
    + ball(64, 60, 18, 15) + face(64, 60, d=7, k=0.75)
    + "".join(leaf(64 + dx, 60 + dy, r) for dx, dy, r in
              [(-21, 6, -20), (-22, -4, 0), (-19, -13, 25), (-13, -20, 50), (21, 6, 20), (22, -4, 0), (19, -13, -25), (13, -20, -50)])
    + sparkle(104, 30, 6, "#FFE14D") + sparkle(22, 40, 4.5) + sparkle(106, 88, 3.5),
    "вишнёвая теннисная ракетка-рама, висящая на гвоздике на стене",
    "в её овале, как в портрете на стене почёта, улыбается жёлтый мяч-чемпион в зелёном лавровом венке")


# 2. Jet Arena — падел-ракетка с мордашкой жонглирует тремя лаймовыми мячами
def padel(x, y, rot=0, sc=1.0, c="#FF7A1A"):
    holes = "".join(circ(hx, hy, 2.3, "#FFFFFF", 0) for hx, hy in
                    [(-12, -16), (0, -19), (12, -16), (-16, -5), (16, -5), (-14, 7), (14, 7), (-7, 16), (7, 16), (0, 20)])
    body = (path("M-5 26 L-4 34 H4 L5 26", c, 2.4)
            + rect(-4.5, 32, 9, 22, "#2E2A45", 3.5, 2.4)
            + path("M0 54 Q-6 62 0 66 Q6 62 0 54", "none", 2)
            + path("M-24 0 Q-24 -28 0 -29 Q24 -28 24 0 Q24 24 0 30 Q-24 24 -24 0Z", c, 3)
            + path("M-19 0 Q-19 -23 0 -24 Q19 -23 19 0 Q19 20 0 25 Q-19 20 -19 0Z", "none", 1.6).replace(O, "#FFFFFF")
            + holes)
    return G(x, y, body, rot, sc)


arc = lambda d: f'<path d="{d}" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="3 4" stroke-linecap="round" opacity=".9"/>'
add("jet-arena-voronino", ("#EFE6FF", "#8C6CE6"),
    path("M-6 116 Q64 110 134 116 V140 H-6Z", "#3FA45B", 2.6)
    + padel(64, 74, 0, 1.25)
    + face(64, 70, d=8, k=0.8)
    # ручки-струнки (руки) вверх
    + path("M38 66 Q28 52 32 40", "none", 3) + path("M90 66 Q100 52 96 40", "none", 3)
    # дуги полёта мячей
    + arc("M32 36 Q40 6 64 12") + arc("M64 12 Q88 6 96 36")
    + G(32, 34, circ(0, 0, 8, LIME, 2.4) + path("M-6 -4 Q0 0 -6 4 M6 -4 Q0 0 6 4", "none", 1.4).replace(O, "#FFFFFF"))
    + G(64, 12, circ(0, 0, 8, LIME, 2.4) + path("M-6 -4 Q0 0 -6 4 M6 -4 Q0 0 6 4", "none", 1.4).replace(O, "#FFFFFF"))
    + G(96, 34, circ(0, 0, 8, LIME, 2.4) + path("M-6 -4 Q0 0 -6 4 M6 -4 Q0 0 6 4", "none", 1.4).replace(O, "#FFFFFF"))
    + sparkle(14, 70, 5) + sparkle(114, 74, 4.5) + sparkle(20, 100, 3),
    "оранжевая падел-ракетка с белыми дырочками и мордашкой",
    "стоит на зелёной травке корта и жонглирует тремя лаймовыми мячами, подбрасывая их дугой над собой")

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
