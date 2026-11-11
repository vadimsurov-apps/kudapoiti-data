"""Иконки робота rare, 2026-11-11 (01 UTC) — места из tools/add_rare_1111.py.
Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно. Перед рисованием просмотрены все 66 листов
icons-catalog и реестр subjects.txt (grep): акула, ленивец, сачок, мяч-прыгун, пружинка, буква на батуте, красная
звезда-персонаж — заняты; ракетка с акульими зубками, звезда, вплетённая в струны, табличка «ТУТ!» — свободны.
Запуск: python3 tools/icons_rare_1111.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
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
    k = f"r9_{pid}"
    draw_icons.BG[k] = pal
    ICONS[pid] = svg(k, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def strings(cid, rx, ry, col, step=7):
    st = "".join(f'<path d="M{x} {-ry} V{ry}" stroke="{col}" stroke-width="1.7"/>' for x in range(-rx + 4, rx, step))
    st += "".join(f'<path d="M{-rx} {y} H{rx}" stroke="{col}" stroke-width="1.7"/>' for y in range(-ry + 5, ry, step))
    return (f'<clipPath id="{cid}"><ellipse cx="0" cy="0" rx="{rx}" ry="{ry}"/></clipPath>'
            f'<g clip-path="url(#{cid})">{st}</g>')


# 1. «Акула Тенниса» — ракетка с акульими зубками по ободу «кусает» мяч
def shark_racket():
    rx, ry = 27, 34
    teeth = ""
    import math
    for i in range(11):
        a = math.radians(-40 + i * 7)       # правая дуга обода (со стороны мяча)
        x, y = (rx + 4) * math.cos(a), (ry + 4) * math.sin(a)
        nx, ny = math.cos(a), math.sin(a)
        tx, ty = -ny * 3.2, nx * 3.2
        teeth += (f'<path d="M{x - tx:.1f} {y - ty:.1f} L{x + nx * 7:.1f} {y + ny * 7:.1f} L{x + tx:.1f} {y + ty:.1f}Z" '
                  f'fill="#FFFFFF" stroke="{O}" stroke-width="1.4" stroke-linejoin="round"/>')
    body = (path("M-6 32 L-4 48 H4 L6 32", "#1F4E8C", 2.6)
            + rect(-5, 46, 10, 26, "#F3F0FA", 4, 2.6)
            + path("M-5 52 L5 56 M-5 60 L5 64 M-5 68 L5 72", "none", 1.4)
            + teeth
            + ell(0, 0, rx, ry, "#E9F6FF", 0)
            + strings("akrs", rx, ry, "#8FB4D9")
            + f'<ellipse cx="0" cy="0" rx="{rx}" ry="{ry}" fill="none" stroke="#1F4E8C" stroke-width="7"/>'
            + f'<ellipse cx="0" cy="0" rx="{rx + 4}" ry="{ry + 4}" fill="none" stroke="{O}" stroke-width="2.6"/>'
            + f'<ellipse cx="0" cy="0" rx="{rx - 4}" ry="{ry - 4}" fill="none" stroke="{O}" stroke-width="1.6"/>'
            + ell(0, 2, 15, 11, "#E9F6FF", 0)
            + face(0, 0, d=8, k=0.85))
    return body


add("tennis-akula-letovskaya", ("#D8F6F6", "#2E9DB3"),
    path("M-6 118 Q30 110 64 116 Q98 122 134 112 V140 H-6Z", "#1E7FA0", 2.4)
    + G(50, 62, shark_racket(), -18)
    + ball(97, 44, 10, 20)
    + face(97, 44, d=4, k=0.45, blush=False)
    + path("M106 30 Q111 25 114 31 M108 58 Q113 62 111 67", "none", 1.8)
    + sparkle(22, 30, 5) + sparkle(110, 70, 4) + sparkle(26, 100, 3.5),
    "синяя теннисная ракетка с рядом белых акульих зубок по верхнему краю обода и мордашкой на струнах",
    "играючи «кусает» с замаха жёлтый мяч, а мяч отскакивает в сторону и хихикает")


# 2. «Красная Звезда» — в струны белой ракетки вплетена красная звёздочка, от удара по мячу — салют звёздочек
def star(cx, cy, r, c, sw=2.4):
    import math
    pts = []
    for i in range(10):
        rr = r if i % 2 == 0 else r * 0.45
        a = math.radians(-90 + i * 36)
        pts.append(f"{cx + rr * math.cos(a):.1f} {cy + rr * math.sin(a):.1f}")
    return path("M" + " L".join(pts) + "Z", c, sw)


def star_racket():
    rx, ry = 26, 33
    return (path("M-6 31 L-4 46 H4 L6 31", "#FFFFFF", 2.6)
            + rect(-5, 44, 10, 28, "#C62032", 4, 2.6)
            + ell(0, 0, rx, ry, "#FDFBF4", 0)
            + strings("rsrs", rx, ry, "#C9C2D9")
            + star(0, 2, 17, "#E53935", 2.4)
            + face(0, 4, d=5, k=0.55, blush=False)
            + f'<ellipse cx="0" cy="0" rx="{rx}" ry="{ry}" fill="none" stroke="#FFFFFF" stroke-width="7"/>'
            + f'<ellipse cx="0" cy="0" rx="{rx + 4}" ry="{ry + 4}" fill="none" stroke="{O}" stroke-width="2.6"/>'
            + f'<ellipse cx="0" cy="0" rx="{rx - 4}" ry="{ry - 4}" fill="none" stroke="{O}" stroke-width="1.6"/>')


add("tennis-red-star-peschanaya", ("#B9C8F7", "#2E3F96"),
    G(52, 66, star_racket(), 24)
    + ball(94, 36, 10)
    + star(112, 50, 5.5, "#FF5252", 1.6) + star(94, 14, 5, "#FF5252", 1.6) + star(114, 24, 4.5, "#FFD54F", 1.4)
    + star(76, 22, 4, "#FFD54F", 1.4) + star(80, 52, 3.5, "#FF5252", 1.4)
    + sparkle(20, 26, 5) + sparkle(18, 104, 3.5),
    "белая теннисная ракетка с красной пятиконечной звёздочкой, вплетённой прямо в сетку струн",
    "отбивает жёлтый мяч под вечерним синим небом, и от удара вокруг мяча разлетается салют из красных и жёлтых звёздочек")


# 3. «Тут батуТ» — жёлтая табличка-стрелка «ТУТ!» показывает на большой круглый батут
tramp = (
    # ножки
    path("M14 98 L10 118 M92 98 L96 118 M36 104 L34 122 M72 104 L74 122", "none", 3.4)
    # рамка (красное кольцо) и чёрная сетка
    + ell(54, 92, 46, 16, "#E8414F", 2.8)
    + ell(54, 91, 36, 10.5, "#2E2A45", 2.2)
    # пружинки по рамке
    + "".join(f'<path d="M{x} {y} l3 -3" stroke="#BFC6D6" stroke-width="2"/>' for x, y in
              [(22, 86), (32, 82), (44, 80), (56, 80), (68, 80), (78, 82), (86, 86)])
    + ell(54, 91, 36, 10.5, "none", 2.2)
)
bounce = '<path d="{0}" fill="none" stroke="#C2185B" stroke-width="2.4" stroke-dasharray="4 4" stroke-linecap="round" opacity=".95"/>'
sign = (
    rect(110, 34, 6, 80, "#FFFFFF", 2, 2.4)
    + "".join(rect(110, y, 6, 6, "#E8414F", 0, 0) for y in range(40, 112, 12))
    + rect(110, 34, 6, 80, "none", 2, 2.4)
    # стрелка-табличка, указывает вниз-влево на батут
    + path("M76 24 H116 Q120 24 120 28 V42 Q120 46 116 46 H76 L64 35Z", "#FFD54F", 2.8)
    + '<text x="95" y="40.5" font-family="Arial Black, Arial, sans-serif" font-weight="900" font-size="12.5" '
      f'text-anchor="middle" fill="{O}">ТУТ!</text>'
)
add("batut-tutbatut-moskovsky", ("#FFE9D9", "#FF8A65"),
    tramp
    + bounce.format("M28 76 Q36 46 46 74") + bounce.format("M50 74 Q60 36 70 74")
    + sign
    + face(54, 90, d=10, k=0.7)
    + sparkle(22, 30, 5.5) + sparkle(84, 64, 3.5) + sparkle(40, 20, 3),
    "жёлтая табличка-стрелка с надписью «ТУТ!» на полосатом красно-белом столбике",
    "показывает острым концом на большой круглый батут с красной рамкой и улыбающейся чёрной сеткой, над которой пружинят пунктирные дуги прыжков")

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
