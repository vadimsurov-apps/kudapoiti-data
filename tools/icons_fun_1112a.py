"""Иконки робота fun (2026-11-12, проход a): места из tools/add_fun_1112a.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя палитра фона.
Запуск: python3 tools/icons_fun_1112a.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}

# 1. Лазертаг Арена – Телепорт: круглая арка-портал выплёвывает красный луч
I["fun-lt-arena-teleport"] = ("#3A2A6E", "#120A2E",
    "лиловая круглая арка-телепорт с вихрем внутри и глазками на ободе",
    "выстреливает из центра вихря красный лазерный луч через тёмную арену",
    f'<rect x="0" y="104" width="128" height="24" fill="#22184A"/>'
    f'<circle cx="54" cy="62" r="38" fill="#9B6BFF" {W(3.6)}/>'
    f'<circle cx="54" cy="62" r="26" fill="#2A1660" {W(3)}/>'
    f'<path d="M54 44 Q72 50 66 66 Q58 78 46 70 Q38 60 50 56 Q58 56 56 64" fill="none" stroke="#5FF2E0" stroke-width="3.4" stroke-linecap="round"/>'
    f'<path d="M58 62 L126 48" stroke="#FF2E4A" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M58 62 L126 48" stroke="#FFC0C8" stroke-width="1.6" stroke-linecap="round"/>'
    f'<circle cx="58" cy="62" r="5" fill="#FF6070"/>'
    + face(54, 28, d=8, k=0.62) +
    f'<rect x="26" y="96" width="56" height="10" rx="4" fill="#6B4CC8" {W(2.6)}/>'
    + sparkle(104, 82, 4, "#FFD23F") + sparkle(16, 30, 3, "#5FF2E0") + sparkle(110, 22, 3, "#fff"))

# 2. Лазертаг Арена – Забытая фабрика: бластер-станок стреляет в мишень на кирпичной стене
I["fun-lt-arena-zabytaya-fabrika"] = ("#E8C9A6", "#8A5A3A",
    "оранжевый лазертаг-бластер с медными заклёпками и манометром, как старый заводской станок",
    "стреляет зелёным лучом в круглую мишень на кирпичной стене заброшенного цеха",
    "".join(f'<rect x="{x}" y="{y}" width="22" height="10" fill="#B5643E" stroke="#7A3E22" stroke-width="1.4"/>'
            for y in range(4, 64, 11) for x in ((70, 92, 114) if (y // 11) % 2 == 0 else (59, 81, 103)))
    + f'<circle cx="98" cy="30" r="15" fill="#FFF" {W(2.6)}/><circle cx="98" cy="30" r="9" fill="#FF4F4F" {W(2)}/><circle cx="98" cy="30" r="3.5" fill="#FFF"/>'
    f'<path d="M58 70 L94 34" stroke="#3CFF7A" stroke-width="4.4" stroke-linecap="round"/>'
    f'<path d="M58 70 L94 34" stroke="#D8FFE4" stroke-width="1.4" stroke-linecap="round"/>'
    f'<rect x="0" y="108" width="128" height="20" fill="#5C3A26"/>'
    f'<path d="M14 66 H62 Q70 66 70 74 V82 Q70 88 62 88 H40 L36 108 H20 L24 88 H14 Q8 88 8 80 V74 Q8 66 14 66Z" fill="#FF8A2A" {W(3.4)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="#B8742A" stroke="#3B3355" stroke-width="1"/>' for x, y in ((14, 72), (62, 72), (14, 82), (62, 82)))
    + f'<circle cx="30" cy="58" r="9" fill="#F2E6C8" {W(2.4)}/><path d="M30 58 L35 54" stroke="#D02C2C" stroke-width="2" stroke-linecap="round"/>'
    f'<path d="M30 67 V66" {W(2.4)}/>'
    + face(42, 76, d=7, k=0.6))

# 3. Лига Миров: Пандора — светящийся инопланетный гриб в повязке-датчике
I["fun-liga-mirov-pandora"] = ("#B9F5E6", "#2E7A8C",
    "бирюзовый светящийся инопланетный гриб с пятнами-огоньками",
    "надел на шляпку чёрную повязку-датчик лазертага с мигающими лампочками и выглядывает из лилового леса",
    f'<path d="M0 92 Q20 84 40 92 T80 92 T128 90 V128 H0Z" fill="#5A2F8A"/>'
    f'<path d="M10 92 Q6 60 18 40 Q24 62 22 92Z" fill="#8E4FD0" {W(2.4)}/>'
    f'<path d="M108 92 Q104 66 116 48 Q122 70 118 92Z" fill="#8E4FD0" {W(2.4)}/>'
    f'<path d="M50 66 Q48 96 44 108 H84 Q80 96 78 66Z" fill="#E6FFF8" {W(3.2)}/>'
    f'<path d="M22 66 Q24 26 64 22 Q104 26 106 66 Q64 76 22 66Z" fill="#2FD6C0" {W(3.6)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#E8FF7A"/>' for x, y, r in ((40, 44, 4), (84, 38, 5), (66, 32, 3)))
    + f'<path d="M24 56 Q64 66 104 56 L104 64 Q64 74 24 64Z" fill="#2C2C3A" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="{c}"/>' for x, y, c in ((40, 63, "#FF3B5C"), (64, 67, "#3CFF7A"), (88, 63, "#FF3B5C")))
    + face(64, 86, d=8, k=0.7)
    + sparkle(30, 18, 3, "#FFF") + sparkle(108, 30, 3, "#E8FF7A"))

# 4. Квант Эпицентр — атом с электронами-лампочками держит маленький бластер
I["fun-kvant-epicentr"] = ("#FFF6C8", "#E0A21E",
    "красное ядро-атом с тремя орбитами и синими электронами-огоньками",
    "в центре своих орбит держит синий лазерный пистолетик и пускает вверх жёлтый луч",
    f'<ellipse cx="64" cy="70" rx="50" ry="16" fill="none" stroke="#3B3355" stroke-width="3" transform="rotate(30 64 70)"/>'
    f'<ellipse cx="64" cy="70" rx="50" ry="16" fill="none" stroke="#3B3355" stroke-width="3" transform="rotate(-30 64 70)"/>'
    f'<ellipse cx="64" cy="70" rx="50" ry="16" fill="none" stroke="#3B3355" stroke-width="3" transform="rotate(90 64 70)"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="#3F8CFF" {W(2.2)}/>' for x, y in ((22, 46), (104, 98), (64, 22)))
    + f'<circle cx="64" cy="70" r="22" fill="#FF5A4A" {W(3.4)}/>'
    + face(64, 68, d=8, k=0.7) +
    f'<path d="M84 76 h14 v-6 h6 v10 h-8 l-2 8 h-6Z" fill="#3F8CFF" {W(2.4)}/>'
    f'<path d="M104 72 L120 40" stroke="#FFE600" stroke-width="4" stroke-linecap="round"/>'
    + sparkle(120, 36, 4, "#FFF") + sparkle(16, 100, 3, "#FFF"))

if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
