"""Иконки робота fun (2026-11-13, проход h): места из tools/add_fun_1113h.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя компоновка и палитра фона.
Запуск: python3 tools/icons_fun_1113h.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
O = "#3B3355"
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}

# 1. «Туса Джуса» в «Люблю Молл» — в игровой играют в носочках: два носочка-близнеца катятся по спиральной трубе-горке
I["fun-tusa-dzhusa-lyublyu-moll"] = ("#F3E6FF", "#B58BE8",
    "два носочка-близнеца — жёлтый в красную полоску и мятный в белый горошек",
    "вместе вылетают из спиральной красной трубы-горки мягкого лабиринта и задрали пятки от восторга",
    # мягкий лабиринт: синие маты-кубы внизу
    f'<rect x="4" y="100" width="40" height="28" fill="#4C7BE8" {W(3)}/>'
    f'<rect x="84" y="100" width="44" height="28" fill="#FFB341" {W(3)}/>'
    # труба-горка: дуга сверху слева вниз вправо
    f'<path d="M6 30 Q44 20 54 52 Q62 78 96 86" fill="none" stroke="{O}" stroke-width="27" stroke-linecap="round"/>'
    f'<path d="M6 30 Q44 20 54 52 Q62 78 96 86" fill="none" stroke="#E8473C" stroke-width="21" stroke-linecap="round"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.4" fill="#FFC9C2"/>' for x, y in ((22, 25), (42, 30), (52, 46), (58, 64), (72, 79)))
    # носок 1 (жёлтый в полоску), выезжает на мат
    + f'<path d="M80 60 L96 56 L100 78 Q112 80 112 90 Q110 100 96 98 L86 96Z" fill="#FFD84A" {W(3)}/>'
    f'<path d="M81 66 L97 62 M83 73 L98 70 M85 80 L99 77" stroke="#E8473C" stroke-width="3"/>'
    + eye(88, 86, 0.65) + eye(97, 85, 0.65)
    + f'<path d="M89 92 q4 3 8 0" fill="none" stroke="{O}" stroke-width="1.8" stroke-linecap="round"/>'
    # носок 2 (мятный в горошек), чуть позади и выше
    f'<path d="M58 28 L74 26 L76 48 Q88 50 88 60 Q86 70 72 68 L62 66Z" fill="#8FE3C8" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="#fff"/>' for x, y in ((64, 34), (70, 42), (64, 52), (80, 62), (68, 60)))
    + eye(66, 56, 0.6) + eye(74, 56, 0.6)
    + f'<path d="M66 61 q4 3 8 0" fill="none" stroke="{O}" stroke-width="1.8" stroke-linecap="round"/>'
    + sparkle(112, 26, 5, "#fff") + sparkle(28, 72, 4, "#fff") + sparkle(116, 58, 3, "#FFF36B"))

# 2. «Пиксель Пати» (Люберцы) — интерактивный световой пол: плитка-персонаж загорается под прыжком
tiles = ""
for r in range(4):
    for c in range(4):
        x, y = 8 + c * 28, 60 + r * 17
        col = {(1, 1): "#FF4FB8", (2, 0): "#39E6FF", (3, 2): "#B6FF4A", (0, 3): "#FFD23F", (2, 3): "#9B6BFF"}.get((c, r), "#1D2A6B")
        if (c, r) == (1, 0):
            continue
        tiles += f'<rect x="{x}" y="{y}" width="25" height="15" rx="2" fill="{col}" stroke="#0B1240" stroke-width="1.6"/>'
I["fun-pixel-party-lyubertsy"] = ("#2A2F7A", "#0B1240",
    "квадратная плитка светового пола, сияющая оранжевым, с мордашкой",
    "вспыхнула и смеётся, когда на неё с прыжка опустилась детская ножка в розовом носке, а соседние плитки в сетке горят разными цветами",
    tiles
    # главная плитка — больше, приподнята
    + f'<rect x="30" y="50" width="42" height="28" rx="4" fill="#FF9A2E" {W(3)}/>'
    f'<rect x="34" y="53" width="34" height="5" rx="2" fill="#FFD9A6"/>'
    + eye(43, 65, 0.7) + eye(59, 65, 0.7)
    + f'<path d="M45 71 Q51 76 57 71" fill="none" stroke="{O}" stroke-width="2.2" stroke-linecap="round"/>'
    # ножка
    f'<path d="M66 6 L80 6 L80 34 Q96 36 96 44 Q94 50 80 48 L66 46Z" fill="#FF8FC8" {W(3)}/>'
    f'<path d="M66 12 H80" stroke="#fff" stroke-width="3"/>'
    # лучи от плитки
    + "".join(f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#FFE27A" stroke-width="3" stroke-linecap="round"/>'
              for x1, y1, x2, y2 in ((26, 50, 16, 42), (30, 44, 24, 32), (76, 52, 88, 56), (52, 46, 52, 36)))
    + sparkle(18, 22, 5, "#39E6FF") + sparkle(108, 22, 4, "#FF4FB8"))

# 3. «Шервуд» (Бутово) — лофт-игровая «Шервуд»: шапочка Робин Гуда прыгает на мини-батуте
I["fun-sherwood-loft-butovo"] = ("#F4FFD9", "#9CCB5A",
    "зелёная остроконечная шапочка Робин Гуда с длинным красным пером",
    "высоко подлетела над маленьким круглым батутом игровой с синей рамкой и ножками, внизу — пружинистая сетка прогнулась",
    # батут
    f'<ellipse cx="64" cy="104" rx="44" ry="10" fill="#2F5DC9" {W(3)}/>'
    f'<ellipse cx="64" cy="103" rx="34" ry="6" fill="#1B1F3A"/>'
    f'<path d="M30 110 L26 124 M98 110 L102 124 M64 114 V126" stroke="{O}" stroke-width="4" stroke-linecap="round"/>'
    # дуги прыжка
    f'<path d="M44 92 q-6 -6 -4 -14 M84 92 q6 -6 4 -14" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    # шапочка
    f'<path d="M26 66 Q40 52 64 50 Q92 50 104 64 Q96 34 66 14 Q48 30 26 66Z" fill="#3E8E3A" {W(3.2)}/>'
    f'<path d="M22 66 Q64 56 108 66 L104 74 Q64 64 26 74Z" fill="#2D6B2A" {W(2.8)}/>'
    # перо
    f'<path d="M78 52 Q100 30 118 8 Q112 30 84 56Z" fill="#E8473C" {W(2.6)}/>'
    f'<path d="M80 54 Q100 32 116 10" stroke="#FFC2B8" stroke-width="1.6" fill="none"/>'
    + face(58, 44, d=10, k=0.8)
    + sparkle(18, 30, 5, "#fff") + sparkle(110, 92, 4, "#FFF36B"))

# 4. Лофт «Домми» (Медведково) — бумажная дискотека: воздушная пушка выстреливает облако бумаги
paper = "".join(
    f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}" transform="rotate({a} {x} {y})" stroke="{O}" stroke-width="1.2"/>'
    for x, y, w, h, c, a in ((20, 20, 10, 6, "#fff", 20), (40, 10, 8, 5, "#FF9EC4", -30), (62, 24, 11, 6, "#fff", 50),
                             (86, 12, 9, 6, "#FFE36B", -15), (104, 30, 10, 6, "#fff", 35), (30, 40, 8, 5, "#9EE7FF", 70),
                             (78, 38, 9, 5, "#FF9EC4", -60), (52, 44, 10, 6, "#fff", 10), (14, 52, 9, 5, "#FFE36B", -40),
                             (96, 50, 8, 5, "#fff", 25)))
I["fun-dommi-loft-medvedkovo"] = ("#FFE7D6", "#F28C5C",
    "толстая оранжевая воздушная пушка аниматора на короткой рукоятке, с мордашкой",
    "стоит на полу лофта и выстреливает вверх фонтан белых, розовых и жёлтых бумажных лоскутков — «бумажная дискотека»",
    paper
    # пушка (наклонена вверх-вправо)
    + f'<g transform="rotate(-35 58 92)">'
      f'<rect x="26" y="76" width="70" height="32" rx="12" fill="#FF7A1A" {W(3.2)}/>'
      f'<ellipse cx="96" cy="92" rx="8" ry="16" fill="#C74F00" {W(3)}/>'
      f'<rect x="32" y="80" width="56" height="5" rx="2.5" fill="#FFC08A"/>'
      + eye(52, 92, 0.75) + eye(68, 92, 0.75)
      + f'<path d="M54 99 Q60 104 66 99" fill="none" stroke="{O}" stroke-width="2.2" stroke-linecap="round"/>'
      f'</g>'
    # рукоятка и подставка
    + f'<path d="M44 104 L40 124 H56 L56 108" fill="#5B5B6B" {W(2.8)}/>'
    + sparkle(116, 72, 5, "#fff") + sparkle(12, 86, 4, "#fff"))

# 5. Игровое шоу «Джуманджи» («Филион») — детёныш ягуара крадётся по клеткам игрового поля к финишу
board = "".join(f'<rect x="{x}" y="{y}" width="20" height="14" fill="{c}" stroke="#5A3A1A" stroke-width="1.4"/>'
                for i, (x, y, c) in enumerate(((0, 104, "#F2D79B"), (20, 104, "#C98B3C"), (40, 104, "#F2D79B"),
                                               (60, 104, "#C98B3C"), (80, 104, "#F2D79B"), (100, 104, "#C98B3C"),
                                               (108, 90, "#F2D79B"))))
I["fun-dzhumandzhi-filion"] = ("#D8F7C9", "#2E8B57",
    "детёныш ягуара — золотистый, в чёрных розетках-пятнышках, с круглыми ушками",
    "крадётся на мягких лапках по клеткам деревянного игрового поля среди огромных тропических листьев к финишной клетке с красным флажком",
    # тропические листья по бокам
    f'<path d="M-4 40 Q30 30 40 70 Q14 74 -4 60Z" fill="#1F7A3A" {W(2.6)}/>'
    f'<path d="M132 28 Q96 22 88 60 Q114 64 132 50Z" fill="#2FA04E" {W(2.6)}/>'
    f'<path d="M0 50 Q20 52 34 66 M128 40 Q108 44 94 56" stroke="#9BE08A" stroke-width="2" fill="none"/>'
    + board
    + f'<path d="M118 90 V66" stroke="{O}" stroke-width="3"/><path d="M118 66 L132 72 L118 78Z" fill="#E8473C" {W(2)}/>'
    # ягуарёнок
    f'<path d="M30 102 Q30 78 58 76 Q84 76 88 96 L88 104 H30Z" fill="#E9A93A" {W(3)}/>'
    f'<path d="M30 92 Q14 86 18 70" fill="none" stroke="{O}" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M30 92 Q14 86 18 70" fill="none" stroke="#E9A93A" stroke-width="4" stroke-linecap="round"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="none" stroke="#3A2410" stroke-width="2"/>'
              for x, y in ((42, 86), (54, 82), (66, 88), (48, 96), (76, 92)))
    + f'<circle cx="84" cy="70" r="17" fill="#F0B548" {W(3)}/>'
    f'<circle cx="72" cy="56" r="6" fill="#F0B548" {W(2.6)}/><circle cx="96" cy="56" r="6" fill="#F0B548" {W(2.6)}/>'
    f'<circle cx="72" cy="56" r="2.6" fill="#3A2410"/><circle cx="96" cy="56" r="2.6" fill="#3A2410"/>'
    f'<ellipse cx="86" cy="78" rx="8" ry="5" fill="#FFF2D6"/>'
    + eye(78, 68, 0.8) + eye(92, 68, 0.8)
    + f'<path d="M83 74 h6 l-3 3Z" fill="#3A2410"/>'
    f'<path d="M86 77 q-3 4 -6 2 M86 77 q3 4 6 2" fill="none" stroke="{O}" stroke-width="1.8" stroke-linecap="round"/>'
    + sparkle(54, 20, 5, "#fff") + sparkle(28, 14, 3, "#FFF36B"))

# 6. «Атмокидс» на 1-й ул. Энтузиастов — квест «Алиса в Зазеркалье»: зеркало, сквозь которое шагает девочка
I["fun-atmokids-entuziastov"] = ("#E2F1FF", "#5B7FD6",
    "высокое овальное зеркало в золотой резной раме с мордашкой на навершии",
    "девочка в голубом платье с белым фартучком шагает сквозь его стекло — по ту сторону видна её половинка, а вокруг кружатся игральные карты-червы",
    # рама
    f'<ellipse cx="64" cy="70" rx="36" ry="48" fill="#E8B83A" {W(3.4)}/>'
    f'<ellipse cx="64" cy="70" rx="28" ry="40" fill="#BFE6FF" {W(2.6)}/>'
    f'<path d="M44 46 L58 38 M50 60 L70 46" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>'
    # навершие с мордашкой
    f'<circle cx="64" cy="20" r="11" fill="#F5CF5A" {W(2.8)}/>'
    + eye(60, 19, 0.5) + eye(68, 19, 0.5)
    + f'<path d="M61 24 q3 2 6 0" fill="none" stroke="{O}" stroke-width="1.6" stroke-linecap="round"/>'
    # девочка: левая половина снаружи зеркала (перед ним), правая — в стекле
    f'<path d="M50 120 L56 90 H74 L80 120Z" fill="#6EB6FF" {W(3)}/>'
    f'<path d="M58 94 H72 L76 118 H54Z" fill="#fff" {W(2)}/>'
    f'<circle cx="65" cy="76" r="12" fill="#FFD9B8" {W(3)}/>'
    f'<path d="M52 74 Q54 58 65 60 Q78 58 78 74 Q72 64 65 66 Q58 64 52 74Z" fill="#FFD84A" {W(2.4)}/>'
    f'<path d="M54 66 Q65 60 76 66" stroke="#2B4BB5" stroke-width="3" fill="none"/>'
    + face(65, 79, d=8, k=0.7)
    # карты
    + "".join(f'<g transform="rotate({a} {x} {y})"><rect x="{x-7}" y="{y-10}" width="14" height="20" rx="2" fill="#fff" {W(2)}/>'
              f'<path d="M{x} {y+4} l-4 -4 a2.4 2.4 0 0 1 4 -3 a2.4 2.4 0 0 1 4 3Z" fill="#E8473C"/></g>'
              for x, y, a in ((18, 40, -20), (110, 36, 18), (16, 92, 12), (112, 96, -14)))
    + sparkle(100, 64, 4, "#fff") + sparkle(26, 64, 3, "#fff"))

if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
