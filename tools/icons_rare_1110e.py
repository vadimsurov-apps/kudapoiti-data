"""Иконки робота rare, 2026-11-10 (13 UTC) — места из tools/add_rare_1110e.py.
Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно — свой герой, своя сцена, компоновка и палитра.
Просмотрены все 64 листа icons-catalog и реестр subjects.txt; заняты и обойдены: ходулист (ДК «Вперёд»), пудель на шаре,
жонглёр с кольцами, клоун, трапеция, канатоходец, диаболо (читается как бантик — заменено на рола-болу), смэш со сплющенным мячом (падел), самокат с мордашкой (памп-трек).
Запуск: python3 tools/icons_rare_1110e.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
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
    k = f"r5_{pid}"
    draw_icons.BG[k] = pal
    ICONS[pid] = svg(k, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def white(d, w=2.0):
    return f'<path d="{d}" fill="none" stroke="#FFFFFF" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'


# 1. Abctennis — на струнах большой ракетки мелом выведено «ABC», мяч-ученик скачет рядом
add("abctennis-rabochaya", ("#F3FFE0", "#9ED36A"),
    G(58, 58, racket(0, 0, -18, 1.9, rim="#14A3A0", grip="#3B3355", strings="#B9D6D3", head="#2F6E6B"), 0)
    + G(58, 58, f'<g transform="rotate(-18)">'
      + white("M-24 10 L-18 -8 L-12 10 M-21 3 H-15", 3.4)
      + white("M-6 -8 V10 M-6 -8 Q4 -8 4 -3 Q4 1 -6 1 Q6 1 6 6 Q6 10 -6 10", 3.4)
      + white("M24 -5 Q19 -9 15 -6 Q10 -2 10 1 Q10 6 15 9 Q20 11 24 7", 3.4) + '</g>', 0)
    + G(100, 36, ball(0, 0, 12, 20) + face(0, 1, d=4, k=0.45), 0)
    + white("M92 44 q-4 6 -2 12 M98 48 q-2 5 0 9", 1.8)
    + sparkle(24, 28, 6),
    "бирюзовая теннисная ракетка-доска, на тёмных струнах мелом крупно выведено «ABC»",
    "стоит наискосок, как школьная доска, а жёлтый мячик-ученик подпрыгивает рядом, будто тянет руку")

# 2. Школа Екатерины Камневой — круглый серый камешек обнимает огромную ракетку на грунте
add("tennis-kamneva-taganskaya", ("#F1E9FF", "#B79CF2"),
    path("M-6 100 Q64 92 134 100 V140 H-6Z", "#E07B4C", 2.6)
    + white("M10 112 H118", 2.2)
    + G(76, 52, racket(0, 0, 24, 1.7, rim="#FF8A3D", grip="#5A3E8C", strings="#C8BEDD"), 0)
    + ell(42, 92, 26, 19, "#A7A9B4", 3)
    + path("M26 84 q6 -6 14 -4 M48 78 q8 -1 12 4", "none", 2).replace(O, "#C9CBD3")
    + face(42, 92, d=8, k=0.8)
    + path("M62 86 Q72 80 78 86", "none", 3)
    + G(30, 34, ball(0, 0, 11, 0), 0)
    + sparkle(108, 102, 5),
    "круглый серый камешек-голыш с румяными щёчками",
    "сидит на оранжевом грунтовом корте и обнимает огромную оранжевую ракетку, над ней летит мяч")

# 3. «Белокаменная» на Самокатной — ракетка едет на самокате (Самокатная улица)
add("belokamennaya-samokatnaya", ("#E8F7FF", "#5FB0E6"),
    path("M-6 112 H134 V140 H-6Z", "#8FA3B8", 2.4)
    + white("M8 122 H30 M48 122 H70 M88 122 H110", 2.6)
    + path("M30 104 H86 L94 92", "none", 5).replace(f'stroke="{O}"', 'stroke="#E53935"')
    + path("M30 104 H86 L94 92", "none", 2.2)
    + path("M94 92 L88 44", "none", 4.5).replace(f'stroke="{O}"', 'stroke="#E53935"')
    + path("M94 92 L88 44", "none", 2)
    + path("M78 42 H98", "none", 4)
    + circ(30, 108, 7, "#37474F", 2.4) + circ(90, 108, 7, "#37474F", 2.4)
    + G(54, 58, racket(0, 0, -8, 1.65, rim="#FFFFFF", grip="#1E63D6", strings="#9FB4C8", head="#E9F4FF"), 0)
    + G(54, 52, rect(-13, -9, 26, 20, "#FFFFFF", 9, 0) + face(0, 0, d=7, k=0.75), 0)
    + path("M60 84 Q72 70 82 46", "none", 2.6)
    + path("M4 60 H20 M0 74 H16 M6 88 H20", "none", 3).replace(O, "#2B6CB0")
    + G(112, 26, ball(0, 0, 8, 30), 0),
    "белоснежная теннисная ракетка с синей ручкой и мордашкой на струнах",
    "мчится стоя на красном самокате по серой улице, держась за руль, за ней — линии скорости")

# 4. «Точка Удара» — мяч попал точно в центр струн, от точки расходятся круги
add("tochka-udara-letovskaya", ("#FFF0DA", "#FF9F5A"),
    G(64, 54, racket(0, 0, 0, 2.2, rim="#2E7D32", grip="#3B3355", strings="#A5C8A7", head="#F4FFF2"), 0)
    + "".join(f'<ellipse cx="64" cy="52" rx="{r*0.8:.0f}" ry="{r:.0f}" fill="none" stroke="#FF7043" stroke-width="3.2" opacity="{op}"/>'
              for r, op in ((18, 1), (28, .8), (38, .55)))
    + G(64, 52, ball(0, 0, 13, 15) + face(0, 1, d=5, k=0.55), 0)
    + circ(64, 52, 2.4, "#E53935", 0)
    + sparkle(22, 30, 6) + sparkle(108, 40, 5),
    "пушистый жёлтый мячик с зажмуренными от удовольствия глазками",
    "влетел точно в самый центр струн зелёной ракетки, и от точки удара по струнам расходятся оранжевые круги, как по воде")

# 5. Цирковая студия «Надежда» — девочка в стойке на руках на пирамиде из цирковых тумб
add("circus-nadezhda-lyubertsy", ("#8E7BE6", "#3C2E86"),
    '<path d="M44 -6 L84 -6 L112 130 L16 130Z" fill="#FFF3B0" opacity=".25"/>'
    + path("M-6 114 Q64 104 134 114 V140 H-6Z", "#C62828", 2.6)
    + rect(28, 96, 72, 18, "#E53935", 4, 2.6) + "".join(rect(x, 96, 9, 18, "#FFFFFF", 0, 0) for x in (38, 56, 74, 92))
    + rect(28, 96, 72, 18, "none", 4, 2.6)
    + rect(38, 80, 52, 16, "#1E63D6", 4, 2.6) + rect(38, 86, 52, 4, "#FFC107", 0, 0) + rect(38, 80, 52, 16, "none", 4, 2.6)
    + rect(48, 66, 32, 14, "#FFC107", 4, 2.6) + path("M64 66 V80", "none", 2).replace(O, "#E53935")
    # девочка вниз головой: ладони на тумбе, голова между рук, ноги вверх
    + path("M52 66 L56 50 M76 66 L72 50", "none", 3.6).replace(O, "#3B3355")
    + path("M52 66 L56 50 M76 66 L72 50", "none", 2).replace(O, "#FFD7B5")
    + circ(64, 56, 8, "#FFD7B5", 2.6) + G(64, 57, face(0, 0, d=3.5, k=0.42, blush=False, mouth=False), 180)
    + path("M57 61 q7 6 14 0", "none", 0) + path("M56 60 Q64 68 72 60 L72 63 Q64 72 56 63Z", "#7A4A2A", 2)
    + path("M55 50 Q55 30 60 22 L68 22 Q73 30 73 50Z", "#FF6FA8", 2.8)
    + path("M60 22 L56 8 M68 22 L74 8", "none", 4.2).replace(O, "#FF6FA8")
    + path("M60 22 L56 8 M68 22 L74 8", "none", 1.8)
    + ell(55, 7, 4, 2.6, "#FFFFFF", 2) + ell(75, 7, 4, 2.6, "#FFFFFF", 2)
    + sparkle(24, 32, 6) + sparkle(104, 26, 7) + sparkle(110, 74, 4),
    "девочка-акробатка в розовом трико",
    "стоит на руках на самой верхней из трёх полосатых цирковых тумб-пирамидой, под лучом прожектора на красном манеже")

# 6. Цирковая студия «Арена» — малыш балансирует на доске, лежащей на катушке (рола-бола), посреди манежа
add("circus-arena-smena-bibirevo", ("#E2FFF7", "#3FC2A6"),
    path("M-6 106 Q64 94 134 106 V140 H-6Z", "#FFC94D", 2.6)
    + path("M-6 114 Q64 102 134 114", "none", 3).replace(O, "#C62828")
    + "".join(sparkle(x, 122, 3.4, "#FFFFFF") for x in (18, 50, 82, 112))
    # катушка-цилиндр
    + rect(42, 84, 44, 22, "#E53935", 11, 2.8)
    + "".join(sparkle(x, 95, 3.6, "#FFE082") for x in (54, 64, 74))
    + ell(86, 95, 5, 11, "#FF8A80", 2.4)
    # доска
    + G(64, 80, rect(-36, -4, 72, 8, "#A1662F", 3, 2.6), -9)
    # малыш с раскинутыми руками
    + path("M56 77 L58 58 M70 75 L68 57", "none", 4).replace(O, "#1E63D6") + path("M56 77 L58 58 M70 75 L68 57", "none", 1.6)
    + rect(53, 36, 20, 24, "#FF9800", 8, 2.6)
    + path("M54 42 L32 34 M72 42 L94 30", "none", 4).replace(O, "#FFD7B5") + path("M54 42 L32 34 M72 42 L94 30", "none", 1.6)
    + circ(31, 34, 3.6, "#FFD7B5", 2) + circ(95, 30, 3.6, "#FFD7B5", 2)
    + circ(63, 26, 10, "#FFD7B5", 2.6) + face(63, 26, d=4.5, k=0.5)
    + path("M53 22 Q56 12 63 14 Q71 12 73 22 Q66 16 60 18Z", "#3B3355", 2)
    + sparkle(22, 62, 5) + sparkle(110, 60, 6),
    "малыш в оранжевой майке с раскинутыми руками",
    "балансирует на доске, лежащей на красной катушке рола-бола, посреди золотого манежа")

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
