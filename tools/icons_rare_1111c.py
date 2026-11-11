"""Иконки робота rare, 2026-11-11 (07 UTC) — места из tools/add_rare_1111c.py.
Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно. Перед рисованием просмотрен реестр subjects.txt
(grep: кегли, карт, батут, ветроуказатель, взлётная полоса, лягушка — заняты как герои в других сценах; кегля-пилот
в карте и батут-взлётная полоса со «садящимся» ребёнком-самолётом — свободны).
Запуск: python3 tools/icons_rare_1111c.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, face, sparkle, eye, O, s
from icons_sections_1108g import rect, circ, ell, path

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}


def add(pid, pal, body, hero, scene):
    k = f"r11c_{pid}"
    draw_icons.BG[k] = pal
    ICONS[pid] = svg(k, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


# 1. ZelenoKart — крытый электрокартинг с боулингом: белая кегля в красном шлеме сама ведёт зелёный карт
kart = (
    circ(28, 100, 13, "#2B2B3A", 3.0) + circ(28, 100, 5, "#BFC6D1", 2.0)                  # заднее колесо
    + path("M10 96 L16 84 H44 L52 90 H84 L96 82 H114 L122 92 L118 100 H12Z", "#3FBF5A", 3.0)  # низкое шасси карта
    + path("M96 82 L106 74 H118 L114 82", "#2E8F44", 2.6)                                  # обтекатель носа
    + '<path d="M58 92 L66 92 L62 97 L70 97 L58 106 L61 99 L55 99Z" fill="#FFE14D" stroke="#3B3355" stroke-width="1.6"/>'
    + circ(104, 101, 11, "#2B2B3A", 3.0) + circ(104, 101, 4.5, "#BFC6D1", 2.0)              # переднее колесо
    + path("M80 86 L86 66", "none", 3.0)                                                    # рулевая колонка
    + ell(87, 64, 4, 8, "#2B2B3A", 2.2)                                                     # руль
)
pin = (
    path("M54 92 Q44 74 52 60 Q56 52 54 44 Q52 34 64 32 Q76 34 74 44 Q72 52 76 60 Q84 74 74 92Z", "#FFFFFF", 3.0)
    + '<path d="M55 48 H73 M55.5 53 H72.5" stroke="#E23B3B" stroke-width="3.2"/>'          # красные полоски
    + path("M50 40 Q50 18 64 18 Q78 18 78 40 Z", "#E23B3B", 2.8)                            # шлем
    + '<path d="M55 30 H78 V36 H55Z" fill="#2B2B3A" opacity=".85"/>'                        # визор
    + eye(60, 70, 0.55) + eye(68, 70, 0.55)
    + '<path d="M60 76 Q64 80 68 76" fill="none" stroke="#3B3355" stroke-width="2.2" stroke-linecap="round"/>'
    + '<ellipse cx="56" cy="75" rx="2.6" ry="1.6" fill="#FF7FA8" opacity=".7"/><ellipse cx="72" cy="75" rx="2.6" ry="1.6" fill="#FF7FA8" opacity=".7"/>'
    + path("M74 70 Q80 68 85 64", "none", 2.6)                                              # ручка на руле
)
speed = ('<path d="M-2 82 H8 M-4 92 H4 M0 72 H10" stroke="#fff" stroke-width="3.2" stroke-linecap="round" opacity=".9"/>')
add("karting-zelenokart-zelenopark", ("#E9FCE1", "#5DB86A"),
    '<rect x="-4" y="108" width="136" height="24" fill="#4A5568"/>'
    + '<path d="M-4 112 H132" stroke="#F2F2F2" stroke-width="2.4" stroke-dasharray="10 8"/>'
    + kart + pin + speed + sparkle(110, 30, 5) + sparkle(88, 46, 3.5),
    "белая кегля для боулинга с красными полосками, в красном шлеме с тёмным визором",
    "сама сидит за рулём зелёного электрокарта с жёлтой молнией на борту и мчится по крытой трассе")

# 2. Airway — батутный центр: батут, размеченный как взлётная полоса, и ребёнок, «садящийся» на него с руками-крыльями
tramp = (
    path("M20 104 L26 122 M108 104 L102 122", "none", 3.2)                                 # ножки
    + ell(64, 100, 50, 14, "#5B6BD6", 3.0)                                                 # рама
    + ell(64, 99, 42, 9.5, "#2D3446", 0)                                                   # полотно
    + '<path d="M30 99 H98" stroke="#FFFFFF" stroke-width="2.6" stroke-dasharray="7 6"/>'    # осевая разметка полосы
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#FFD84D" stroke="#3B3355" stroke-width="1.2"/>'
              for x, y in ((20, 98), (34, 89), (52, 86), (76, 86), (94, 89), (108, 98)))     # огни полосы
)
kid = (
    path("M64 50 L22 40 L26 48 L62 60Z", "#FFFFFF", 2.6)                                    # левое «крыло»-рука
    + path("M64 50 L106 40 L102 48 L66 60Z", "#FFFFFF", 2.6)                                # правое «крыло»-рука
    + rect(54, 46, 20, 24, "#2FB3A0", 7, 2.8)                                              # футболка
    + path("M58 70 L54 84 M70 70 L76 82", "none", 3.4)                                      # ноги
    + circ(64, 34, 11, "#FFD7B5", 2.8)
    + path("M53 31 Q56 20 64 21 Q73 20 75 31 Q68 26 64 28 Q59 26 53 31Z", "#7A4A2A", 2.2)  # волосы
    + eye(60, 35, 0.48) + eye(68, 35, 0.48)
    + '<path d="M60 40 Q64 43.5 68 40" fill="none" stroke="#3B3355" stroke-width="2.2" stroke-linecap="round"/>'
)
arc = '<path d="M30 20 Q18 40 24 62" fill="none" stroke="#fff" stroke-width="2.6" stroke-dasharray="4 5" stroke-linecap="round" opacity=".9"/>'
add("trampoline-airway-orekhovo", ("#FFF3E0", "#F28C5A"),
    tramp + '<ellipse cx="64" cy="97" rx="12" ry="3" fill="#000" opacity=".25"/>' + arc + kid
    + sparkle(104, 22, 5) + sparkle(22, 76, 3.5),
    "синий батут, расчерченный как взлётная полоса: белый пунктир посередине и жёлтые огоньки по раме",
    "на него, расставив руки, как крылья самолёта, заходит на посадку прыгающий ребёнок в бирюзовой футболке")

# 3. «Жемчужина» (Крылатское) — центр ракеточных видов: волан, у которого пробка — большая перламутровая жемчужина,
#    а юбка — из нитей жемчуга, перелетает через бадминтонную сетку
net = (
    path("M6 86 H122", "none", 3.0)
    + '<rect x="6" y="86" width="116" height="26" fill="url(#mesh)" opacity=".9"/>'
    + path("M6 86 V122 M122 86 V122", "none", 3.2)
    + '<path d="M6 112 H122" stroke="#3B3355" stroke-width="2"/>'
)
mesh = ('<defs><pattern id="mesh" width="8" height="8" patternUnits="userSpaceOnUse">'
        '<path d="M0 0 L8 8 M8 0 L0 8" stroke="#ffffff" stroke-width="1.2"/></pattern></defs>')
ribs = ((56, 38), (60, 51), (64, 64), (68, 77), (72, 90))
skirt = (
    path("M54 70 L36 24 Q64 12 92 24 L74 70Z", "#FFFFFF", 3.0)
    + "".join(f'<path d="M{x0} 70 L{x1} 21" stroke="#D9D2E6" stroke-width="1.6"/>' for x0, x1 in ribs)
    + "".join(f'<circle cx="{x0 + (x1 - x0) * k:.1f}" cy="{70 - 49 * k:.1f}" r="2.4" fill="#FFF8EE" '
              f'stroke="#3B3355" stroke-width="1.1"/>' for x0, x1 in ribs for k in (0.2, 0.42, 0.64, 0.86))
    + path("M44 46 Q64 40 84 46", "none", 2.2)
)
pearl = (
    circ(64, 80, 15, "#F6EEF7", 3.0)
    + '<ellipse cx="58" cy="74" rx="5" ry="3.4" fill="#ffffff" opacity=".95"/>'
    + '<path d="M52 86 Q64 96 76 86" fill="none" stroke="#E5C6E8" stroke-width="2.6" opacity=".8"/>'
    + face(64, 80, d=5.5, k=0.5)
)
strands = f'<g transform="rotate(32 64 64) translate(-2 2) scale(0.94) translate(4 0)">{skirt}{pearl}</g>'
pearl = ""
trail = '<path d="M14 40 Q26 30 40 34" fill="none" stroke="#fff" stroke-width="2.6" stroke-dasharray="4 5" stroke-linecap="round"/>'
add("badminton-jemchujina-krylatskoe", ("#E4F4FF", "#3E7CC9"),
    mesh + net + trail + strands + pearl + sparkle(104, 34, 5) + sparkle(24, 64, 3.5) + sparkle(98, 72, 3),
    "волан, у которого пробковая головка — большая перламутровая жемчужина с мордашкой, а белая юбка расшита рядами жемчужинок",
    "перелетает через белую бадминтонную сетку, оставляя пунктирный след")

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
