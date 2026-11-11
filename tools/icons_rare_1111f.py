"""Иконки робота rare, 2026-11-11 (14 UTC) — места из tools/add_rare_1111f.py.
Правило АБСОЛЮТНОЙ уникальности: просмотрены все листы icons-catalog (монтажи) и реестр subjects.txt (grep: цирк,
трапеция, кольцо, полотна, стойка на руках, тумба, ролла-бола, колесо, жонглёр, силач, шимпанзе, перш, шест).
Занято почти всё цирковое; свободен перш: взрослый акробат держит на плече длинный шест, на верхушке — малышка.
Запуск: python3 tools/icons_rare_1111f.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, sparkle, eye, O
from icons_sections_1108g import rect, circ, ell, path

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}


def add(pid, pal, body, hero, scene):
    k = f"r11f_{pid}"
    draw_icons.BG[k] = pal
    ICONS[pid] = svg(k, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def mouth(x, y, w=3, sw=2.0):
    return f'<path d="M{x-w} {y} Q{x} {y+w*0.9} {x+w} {y}" fill="none" stroke="{O}" stroke-width="{sw}" stroke-linecap="round"/>'


def blush(x, y, rx=2.4, ry=1.5):
    return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#FF7FA8" opacity=".7"/>'


# «Чимп Чамп» — школа циркового искусства. Перш: внизу на красно-белом бортике манежа стоит улыбчивый акробат
# в бирюзовом трико, на его плече — длинный золотой шест; на круглой площадке наверху шеста малышка в звёздном
# малиновом трико поднимает руку с маленьким флажком. Фон — тёмно-синий купол с прожектором.
dome = ('<path d="M-4 0 L64 -6 L132 0 V128 H-4Z" fill="none"/>'
        '<path d="M64 0 L40 128 H88Z" fill="#FFF6B0" opacity=".22"/>'
        + sparkle(22, 30, 4) + sparkle(104, 24, 3.4) + sparkle(110, 60, 2.6))
ring = ('<rect x="-4" y="104" width="136" height="30" fill="#E8D5B0"/>'
        '<path d="M-4 104 H132" stroke="#3B3355" stroke-width="2.6"/>'
        + "".join(f'<rect x="{x}" y="104" width="10" height="9" fill="{c}"/>'
                  for x, c in zip(range(-4, 132, 10), ["#E23B3B", "#FFFFFF"] * 7))
        + '<path d="M-4 113 H132" stroke="#3B3355" stroke-width="2.6"/>')
base = (
    path("M54 104 L57 84 H71 L74 104", "#2FB5A8", 3.0)                 # ноги в трико
    + rect(50, 66, 28, 22, "#2FB5A8", 9, 3.0)                          # торс
    + path("M76 72 Q84 70 80 66", "none", 3.2)                         # рука держит шест
    + circ(64, 54, 11, "#FFD7B5", 3.0)                                 # голова
    + path("M53 51 Q56 41 64 42 Q72 41 75 51 Q68 46 64 47 Q59 46 53 51Z", "#5B3A29", 2.2)   # волосы
    + eye(60, 54, 0.5) + eye(68, 54, 0.5) + mouth(64, 58) + blush(57, 59) + blush(71, 59)
)
pole = (path("M80 78 V54", "none", 5.6)
        + '<path d="M80 78 V54" stroke="#FFC93C" stroke-width="3.2" stroke-linecap="round"/>'
        + rect(72, 50, 16, 5, "#FFC93C", 2.5, 2.4))                    # площадка на верхушке
girl = (
    path("M73 18 L75 10 M79 18 L77 10", "none", 2.8)                   # ножки
    + rect(70, -2, 12, 13, "#E0457B", 5, 2.6)                          # трико
    + sparkle(76, 4, 2.4, "#FFF6B0")
    + path("M71 1 Q64 -4 62 -10", "none", 2.6)                         # рука вверх
    + path("M62 -10 V-20", "none", 2.0) + path("M62 -20 L70 -17 L62 -14Z", "#FFD23F", 1.8)  # флажок
    + circ(76, -8, 6.5, "#FFD7B5", 2.6)
    + path("M69.5 -10 Q72 -16 76 -15.5 Q81 -16 82.5 -10 Q79 -13 76 -12.5 Q72 -13 69.5 -10Z", "#F28C28", 1.8)
    + eye(74, -7.5, 0.35) + eye(78.5, -7.5, 0.35) + mouth(76.2, -4.5, 1.8, 1.4)
)
# сдвигаем всю верхнюю часть вниз, чтобы малышка была в круге
add("circus-chimp-champ-vatutinki", ("#4E5BC8", "#1E2466"),
    dome + ring + f'<g transform="translate(0 12)">{base}</g>' + pole + f'<g transform="translate(4 32)">{girl}</g>',
    "малышка в малиновом звёздном трико с рыжими волосами на верхушке золотого перша",
    "акробат в бирюзовом трико держит шест на плече посреди красно-белого манежа, а она машет жёлтым флажком под куполом")

if __name__ == "__main__":
    for pid, txt in ICONS.items():
        open(os.path.join(OUT, f"{pid}.svg"), "w").write(txt)
    reg = os.path.join(OUT, "subjects.txt")
    lines = open(reg).read().splitlines()
    have = {l.split(" — ")[0] for l in lines}
    with open(reg, "a") as f:
        for pid, line in SUBJ.items():
            if pid not in have:
                f.write(line + "\n")
    print("icons:", len(ICONS))
