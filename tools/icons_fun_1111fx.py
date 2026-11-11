"""Иконки робота fun (2026-11-11, проход fx): места из tools/add_fun_1111fx.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя компоновка и палитра фона.
Запуск: python3 tools/icons_fun_1111fx.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}


def stars(pts, r=3, c="#fff"):
    return "".join(sparkle(x, y, r, c) for x, y in pts)


# 1. «Дерзай, малыш!» (Люберцы) — игровая с 6 месяцев: мягкий кубик-ступенька подсаживает ползунка на волну
I["fun-derzai-malysh-lyubertsy"] = ("#E4FBF1", "#47B98B",
    "толстый поролоновый кубик-ступенька вишнёвого цвета с мордашкой",
    "подставил спину малышу в ползунках, который карабкается с него на мягкую жёлтую волну-горку",
    f'<path d="M58 112 Q74 70 96 70 Q118 70 124 112Z" fill="#FFD34D" {W(3.2)}/>'
    f'<path d="M70 104 Q82 82 96 80" fill="none" stroke="#FFF2B8" stroke-width="4" stroke-linecap="round"/>'
    f'<rect x="12" y="66" width="52" height="46" rx="9" fill="#D9365E" {W(3.4)}/>'
    f'<path d="M18 72 H58" stroke="#F58AA5" stroke-width="3" stroke-linecap="round"/>'
    + face(38, 90, d=9, k=0.85) +
    # малыш в голубых ползунках
    f'<ellipse cx="54" cy="58" rx="14" ry="10" fill="#7FC8FF" {W(3)}/>'
    f'<circle cx="70" cy="46" r="11" fill="#FFE0C4" {W(3)}/>'
    f'<path d="M62 38 Q70 30 78 38" fill="none" stroke="#8A5A2B" stroke-width="3"/>'
    + eye(67, 46, 0.5) + eye(74, 46, 0.5) +
    f'<path d="M68 51 Q71 53 74 51" fill="none" {W(1.8)}/>'
    f'<path d="M78 52 Q86 52 88 62" fill="none" stroke="#7FC8FF" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M78 52 Q86 52 88 62" fill="none" {W(1.6)} opacity=".0"/>'
    f'<circle cx="89" cy="64" r="4" fill="#FFE0C4" {W(2)}/>'
    f'<path d="M44 64 L38 70" stroke="#7FC8FF" stroke-width="6" stroke-linecap="round"/>'
    + stars(((20, 30), (104, 34)), 3.4, "#FFFFFF"))

# 3. Квест-Лофт (Сходненская) — квесты о школе волшебников с 7 лет: свеча освещает тайную дверь
I["fun-kvest-loft-skhodnenskaya"] = ("#3A2E5C", "#15102A",
    "толстая восковая свеча в медном подсвечнике-блюдце с мордашкой",
    "держит огонёк у потайной каменной двери, на которой светится замочная скважина в форме звезды",
    f'<rect x="58" y="16" width="56" height="96" rx="4" fill="#5B5378" {W(3)}/>'
    + "".join(f'<path d="M{x} {y} h{w}" stroke="#463F63" stroke-width="2"/>' for x, y, w in
              ((60, 36, 52), (60, 56, 52), (60, 76, 52), (60, 96, 52))) +
    f'<path d="M66 112 V44 Q86 26 106 44 V112Z" fill="#7B4B2A" {W(3)}/>'
    f'<path d="M86 30 V112" stroke="#5E3820" stroke-width="2"/>'
    f'<path d="M86 66 l3 6 6 1 -4.5 4 1.2 6 -5.7 -3 -5.7 3 1.2 -6 -4.5 -4 6 -1Z" fill="#FFE066" {W(1.8)}/>'
    f'<circle cx="86" cy="74" r="14" fill="#FFE066" opacity=".22"/>'
    f'<circle cx="34" cy="40" r="26" fill="#FFC94D" opacity=".18"/>'
    f'<ellipse cx="34" cy="108" rx="24" ry="6" fill="#C9874A" {W(3)}/>'
    f'<path d="M54 106 q10 0 8 -8" fill="none" stroke="#C9874A" stroke-width="4" stroke-linecap="round"/>'
    f'<rect x="20" y="52" width="28" height="54" rx="6" fill="#FFF6DD" {W(3.2)}/>'
    f'<path d="M24 56 q0 8 4 10" fill="none" stroke="#E8DDBE" stroke-width="3" stroke-linecap="round"/>'
    f'<path d="M34 52 V46" {W(2.4)}/>'
    f'<path d="M34 24 Q44 36 34 46 Q24 36 34 24Z" fill="#FF9F1C" {W(2.4)}/>'
    f'<path d="M34 32 Q38 38 34 42 Q30 38 34 32Z" fill="#FFE98A"/>'
    + face(34, 78, d=6, k=0.7) + stars(((14, 18), (120, 120), (48, 14)), 2.6, "#FFE98A"))

# 4. CooknRun (Строгино) — кулинарное квест-шоу «Адская кухня»: таймер-помидор бежит наперегонки
I["fun-cooknrun-strogino"] = ("#FFF7D6", "#F2C230",
    "кухонный таймер в виде пузатого помидора с циферблатом и мордашкой",
    "бежит на тонких ножках в кроссовках к финишной ленточке, а позади вьётся пар",
    f'<path d="M100 40 V108" stroke="#3B3355" stroke-width="3"/><path d="M100 40 h18 v10 h-18" fill="#fff" {W(2)}/>'
    f'<path d="M104 40 h4 v5 h-4Z M112 45 h4 v5 h-4Z" fill="#3B3355"/>'
    f'<path d="M14 66 q8 -6 0 -12 q-8 -6 0 -12 M26 74 q8 -6 0 -12 q-8 -6 0 -12" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" opacity=".9"/>'
    f'<path d="M50 92 L42 112 M68 92 L80 110" stroke="#3B3355" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M34 110 h14 q2 4 -2 5 h-14Z" fill="#2EC4B6" {W(2)}/><path d="M78 108 h14 q2 4 -2 5 h-14Z" fill="#2EC4B6" {W(2)}/>'
    f'<circle cx="60" cy="66" r="30" fill="#F2453D" {W(3.4)}/>'
    f'<path d="M48 38 l6 6 6 -8 6 8 6 -6 -4 10 h-16Z" fill="#4CAF50" {W(2.4)}/>'
    f'<circle cx="60" cy="78" r="12" fill="#FFF5EE" {W(2.4)}/>'
    + "".join(f'<path d="M{60 + 10 * c:.1f} {78 + 10 * sn:.1f} L{60 + 8 * c:.1f} {78 + 8 * sn:.1f}" {W(1.4)}/>'
              for c, sn in ((1, 0), (0, 1), (-1, 0), (0, -1))) +
    f'<path d="M60 78 L65 72" {W(2.2)}/>'
    + eye(50, 58, 0.7) + eye(70, 58, 0.7) +
    f'<ellipse cx="42" cy="66" rx="4" ry="2.4" fill="#FFB3C1" opacity=".8"/><ellipse cx="78" cy="66" rx="4" ry="2.4" fill="#FFB3C1" opacity=".8"/>'
    f'<path d="M34 64 L22 58 M86 62 L96 52" stroke="#3B3355" stroke-width="4" stroke-linecap="round"/>')

if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
