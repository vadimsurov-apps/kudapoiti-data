"""Иконки робота fun (2026-11-11, проход n): места из tools/add_fun_1111n.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя палитра фона.
Запуск: python3 tools/icons_fun_1111n.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}


def leaf(x, y, r, c, rot):
    return (f'<path d="M{x} {y-r} Q{x+r} {y-r*0.3} {x} {y+r} Q{x-r} {y-r*0.3} {x} {y-r}Z" fill="{c}" '
            f'stroke="#3B3355" stroke-width="1.6" transform="rotate({rot} {x} {y})"/>')


def bubble(x, y, r):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFFFFF" fill-opacity=".35" stroke="#FFFFFF" stroke-width="1.8"/>'
            f'<circle cx="{x - r*0.35:.1f}" cy="{y - r*0.35:.1f}" r="{max(1, r*0.25):.1f}" fill="#fff"/>')


# 1. Комната матери и ребёнка в парке 50-летия Октября — радионяня на скамейке в листопаде
I["chg-park-50-let-oktyabrya"] = ("#FFE7C2", "#E8893A",
    "белая радионяня с короткой антенной и мордашкой на экранчике",
    "стоит на парковой скамейке и ловит колыбельную, а вокруг кружатся жёлтые кленовые листья",
    f'<rect x="14" y="98" width="100" height="8" rx="3" fill="#A0643A" {W(2.6)}/>'
    f'<path d="M24 106 V120 M104 106 V120" stroke="#3B3355" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M58 30 V16" stroke="#3B3355" stroke-width="4" stroke-linecap="round"/><circle cx="58" cy="14" r="4" fill="#FF8A5C" {W(2)}/>'
    f'<rect x="38" y="30" width="48" height="68" rx="16" fill="#FFFFFF" {W(3.4)}/>'
    f'<rect x="45" y="40" width="34" height="24" rx="6" fill="#9FE3D6" {W(2.4)}/>'
    + face(62, 50, d=7, k=0.6) +
    "".join(f'<circle cx="{x}" cy="{y}" r="2.4" fill="#C9C3D9"/>' for x in (52, 62, 72) for y in (76, 84)) +
    f'<path d="M92 44 q6 6 0 12 M98 40 q10 10 0 20" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>'
    f'<text x="100" y="34" font-family="Arial" font-size="14" fill="#5A3A8C">♪</text>'
    + leaf(22, 30, 7, "#FFC531", 30) + leaf(104, 74, 6, "#F06A3A", -40) + leaf(18, 70, 6, "#FFB02E", 70)
    + leaf(110, 22, 5, "#E8503A", 10))

# 2. ТРЦ «Ботаника» — вязаные пинетки висят на ветке фикуса в горшке
I["chg-trc-botanica"] = ("#E3FBEA", "#5FBF85",
    "пара вязаных голубых пинеток с белыми помпонами",
    "сушатся, повиснув на ветке большого фикуса в кадке",
    f'<path d="M6 118 L10 100 H34 L38 118Z" fill="#C8754A" {W(2.6)}/>'
    f'<path d="M22 100 V40 Q22 24 40 22 L116 22" fill="none" stroke="#6B4A2B" stroke-width="5" stroke-linecap="round"/>'
    + leaf(14, 60, 9, "#2E9E5B", -50) + leaf(30, 46, 9, "#3CB46A", 40) + leaf(12, 32, 8, "#2E9E5B", -30)
    + leaf(104, 12, 8, "#3CB46A", 70) + leaf(74, 12, 7, "#2E9E5B", 80) +
    f'<path d="M50 22 V34 M86 22 V40" stroke="#3B3355" stroke-width="2"/>'
    f'<path d="M36 34 h28 v34 q0 14 14 14 h4 q10 0 10 10 q0 8 -10 8 h-34 q-12 0 -12 -12Z" fill="#7EC8F2" {W(3)}/>'
    f'<path d="M72 40 h28 v30 q0 14 12 16 q6 2 6 8 q0 6 -8 6 h-30 q-8 0 -8 -10Z" fill="#9AD6FA" {W(3)}/>'
    f'<path d="M36 44 h28 M72 50 h28" stroke="#5AA8D8" stroke-width="3"/>'
    f'<circle cx="50" cy="34" r="6" fill="#fff" {W(2)}/><circle cx="86" cy="40" r="6" fill="#fff" {W(2)}/>'
    + face(50, 70, d=6, k=0.55) + face(86, 72, d=6, k=0.55))

# 3. ТРК «Европейский» — детская ванночка, полная пены и пузырей
I["chg-trk-evropeisky"] = ("#E9EEFF", "#7F95E8",
    "голубая детская ванночка на подставке с мордашкой на бортике",
    "доверху полна белой пены, из которой поднимаются радужные мыльные пузыри",
    f'<path d="M36 112 L46 86 M92 112 L82 86" stroke="#3B3355" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M18 64 H110 Q106 92 82 92 H46 Q22 92 18 64Z" fill="#5FB8F0" {W(3.4)}/>'
    f'<path d="M20 64 Q26 50 38 56 Q44 44 56 52 Q64 40 74 52 Q86 44 92 56 Q104 50 108 64Z" fill="#FFFFFF" {W(2.6)}/>'
    + face(64, 76, d=10, k=0.75) +
    bubble(40, 34, 8) + bubble(62, 22, 10) + bubble(88, 32, 7) + bubble(102, 18, 5) + bubble(26, 18, 4))

# 4. Vegas Кунцево — пачка влажных салфеток высунула салфетку, как язычок
I["chg-vegas-kuntsevo"] = ("#FFE3EE", "#F27BA8",
    "мягкая пачка влажных детских салфеток с клапаном и мордашкой",
    "лежит на пеленальном матрасике и дразнится, высунув салфетку, как язычок",
    f'<rect x="10" y="94" width="108" height="20" rx="10" fill="#FFF6C9" {W(3)}/>'
    + "".join(f'<path d="M{x} 96 V112" stroke="#F2C94C" stroke-width="2"/>' for x in (34, 56, 78, 100)) +
    f'<path d="M22 56 Q22 42 36 42 H92 Q106 42 106 56 V82 Q106 96 92 96 H36 Q22 96 22 82Z" fill="#B9E8FF" {W(3.4)}/>'
    f'<rect x="44" y="46" width="40" height="14" rx="7" fill="#5DB7E8" {W(2.4)}/>'
    f'<path d="M56 50 Q64 20 80 26 Q72 36 72 50Z" fill="#FFFFFF" {W(2.4)}/>'
    + face(64, 74, d=12, k=0.8) +
    f'<path d="M30 30 l3 -8 M98 28 l-3 -8" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>')

# 5. Vegas Крокус Сити — зубная щётка-ёжик чистит молочный зубик
I["chg-vegas-crocus"] = ("#DFF9F5", "#3FB9A8",
    "детская зубная щётка с мягкой щетинкой-ёжиком и мордашкой на ручке",
    "бережно чистит маленький молочный зубик, вокруг летают пузырьки пены",
    f'<path d="M30 76 Q30 58 46 58 Q52 62 58 58 Q74 58 74 76 Q74 92 66 108 Q62 112 58 104 L52 92 L46 104 Q42 112 38 108 Q30 92 30 76Z" '
    f'fill="#FFFFFF" {W(3.2)}/>'
    + face(52, 78, d=8, k=0.6) +
    f'<rect x="58" y="40" width="58" height="14" rx="7" fill="#FFB547" {W(3)}/>'
    + eye(92, 47, 0.45) + eye(102, 47, 0.45) +
    f'<rect x="50" y="34" width="22" height="10" rx="3" fill="#FFB547" {W(2.4)}/>'
    + "".join(f'<path d="M{x} 34 V{24 + (i % 2) * 3}" stroke="#7A5CC8" stroke-width="3" stroke-linecap="round"/>'
              for i, x in enumerate(range(53, 71, 4))) +
    bubble(30, 40, 6) + bubble(22, 58, 4) + bubble(84, 74, 5) + bubble(94, 88, 3))

# 6. Vegas на Каширском (24 км МКАД) — мыльница-лягушка пускает пузыри над раковиной
I["chg-vegas-kashirskoe"] = ("#FFF7CF", "#F2C230",
    "зелёная мыльница в форме лягушки с кусочком розового детского мыла на спинке",
    "сидит на краю белой раковины и выдувает ртом цепочку мыльных пузырей",
    f'<path d="M6 92 H122 V128 H6Z" fill="#FFFFFF" {W(3)}/><path d="M20 92 Q64 120 108 92" fill="#DDF2FF" {W(2.6)}/>'
    f'<path d="M28 92 Q24 62 54 60 Q84 62 80 92Z" fill="#6CCB5F" {W(3.4)}/>'
    f'<circle cx="38" cy="58" r="9" fill="#6CCB5F" {W(3)}/><circle cx="66" cy="58" r="9" fill="#6CCB5F" {W(3)}/>'
    + eye(38, 58, 0.7) + eye(66, 58, 0.7) +
    f'<ellipse cx="34" cy="80" rx="5" ry="3" fill="#FF7FA8" opacity=".6"/><ellipse cx="72" cy="80" rx="5" ry="3" fill="#FF7FA8" opacity=".6"/>'
    f'<ellipse cx="54" cy="78" rx="7" ry="5" fill="#3B3355"/>'
    f'<rect x="42" y="84" width="24" height="10" rx="4" fill="#FFA6C9" {W(2.2)}/>'
    + bubble(76, 66, 6) + bubble(90, 52, 8) + bubble(104, 34, 10) + bubble(92, 18, 5))

# 7. ТЦ «Орбита» — сложенный подгузник летит по орбите вокруг планеты
I["chg-trc-orbita"] = ("#7C8BE6", "#2E2F7A",
    "белый сложенный подгузник с липучками-ушками и мордашкой",
    "летит, как спутник, по орбите вокруг маленькой планеты с кольцом",
    f'<circle cx="46" cy="80" r="22" fill="#FF9C6B" {W(3)}/>'
    f'<path d="M30 70 q8 4 14 0 M40 92 q10 -4 18 2" fill="none" stroke="#E0663A" stroke-width="3" stroke-linecap="round"/>'
    f'<ellipse cx="62" cy="70" rx="56" ry="20" fill="none" stroke="#C9D1FF" stroke-width="2.4" stroke-dasharray="5 5" transform="rotate(-18 62 70)"/>'
    f'<path d="M74 30 H112 L106 58 Q93 68 80 58Z" fill="#FFFFFF" {W(3.2)}/>'
    f'<rect x="68" y="28" width="12" height="9" rx="3" fill="#7FD3FF" {W(2)}/><rect x="106" y="28" width="12" height="9" rx="3" fill="#7FD3FF" {W(2)}/>'
    + face(93, 42, d=6, k=0.55) +
    f'<path d="M70 66 l-8 6 M76 70 l-6 8" stroke="#FFE38A" stroke-width="2.4" stroke-linecap="round"/>'
    + sparkle(18, 24, 4, "#FFE38A") + sparkle(110, 104, 4, "#FFE38A") + sparkle(40, 20, 2.5, "#fff") + sparkle(96, 92, 2.5, "#fff"))

# 8. Московская школа фокусов — бубновый туз выпрыгивает из веера карт в белой перчатке
I["fun-shkola-fokusov-baumanskaya"] = ("#FFD6D6", "#B32B4A",
    "бубновый туз-персонаж с ручками и ножками",
    "выпрыгивает из веера карт в руке фокусника в белой перчатке",
    "".join(f'<rect x="40" y="70" width="26" height="36" rx="4" fill="#FFFFFF" {W(2.4)} transform="rotate({a} 53 112)"/>'
            for a in (-40, -20, 0, 20)) +
    f'<path d="M30 112 Q30 98 44 96 H72 Q84 98 82 112 Q82 124 66 124 H44 Q30 124 30 112Z" fill="#FFFFFF" {W(3)}/>'
    f'<path d="M40 100 V110 M50 98 V110 M60 98 V110" stroke="#3B3355" stroke-width="2"/>'
    f'<rect x="56" y="14" width="40" height="56" rx="6" fill="#FFFFFF" {W(3.2)} transform="rotate(12 76 42)"/>'
    f'<path d="M78 26 L88 40 L78 54 L68 40Z" fill="#E8304A" {W(2.4)} transform="rotate(12 76 42)"/>'
    f'<text x="58" y="26" font-family="Arial" font-weight="bold" font-size="11" fill="#E8304A" transform="rotate(12 76 42)">A</text>'
    + face(78, 42, d=5, k=0.45) +
    f'<path d="M62 52 l-10 6 M96 50 l10 2 M70 70 l-4 10 M86 70 l4 10" stroke="#3B3355" stroke-width="2.6" stroke-linecap="round"/>'
    + sparkle(22, 30, 5, "#FFE38A") + sparkle(108, 18, 4, "#FFE38A") + sparkle(112, 74, 3, "#fff"))

# 9. Квест центр (Зеленоград) — старинный ключ поворачивается в огромной замочной скважине
I["fun-quest-center-zelenograd"] = ("#3E6E6A", "#16302E",
    "старинный бронзовый ключ с узорчатым кольцом и мордашкой",
    "вставлен в огромную замочную скважину деревянной двери и поворачивается, из щели бьёт золотой свет",
    f'<rect x="0" y="0" width="128" height="128" fill="#7A4E2D"/>'
    + "".join(f'<path d="M{x} 0 V128" stroke="#5E3A20" stroke-width="3"/>' for x in (24, 52, 80, 108)) +
    f'<path d="M64 52 m-14 0 a14 14 0 1 1 28 0 q0 8 -6 12 L78 104 H50 L56 64 q-6 -4 -6 -12Z" fill="#1A1210" {W(3)}/>'
    f'<path d="M58 70 L64 108 L70 70" fill="#FFD95A" opacity=".55"/>'
    f'<circle cx="64" cy="40" r="22" fill="#D99A3A" {W(3.4)}/><circle cx="64" cy="40" r="10" fill="#7A4E2D" {W(2.6)}/>'
    + eye(57, 38, 0.5) + eye(71, 38, 0.5) +
    f'<path d="M60 44 Q64 47 68 44" fill="none" stroke="#3B3355" stroke-width="2"/>'
    f'<rect x="58" y="60" width="12" height="20" rx="2" fill="#D99A3A" {W(2.6)}/>'
    f'<path d="M36 22 l-8 -6 M92 22 l8 -6 M30 44 h-10 M98 44 h10" stroke="#FFD95A" stroke-width="3" stroke-linecap="round"/>')

# 10. Вкусная студия (Зеленоград) — венчик взбивает крем в розовой миске
I["fun-vkusnaya-studiya-zelenograd"] = ("#FFEFE0", "#F5A27A",
    "металлический венчик-персонаж с мордашкой на ручке",
    "весело взбивает в розовой миске белую шапку крема, во все стороны летят сладкие капли",
    f'<path d="M64 74 Q30 50 46 26 Q64 14 64 74Z M64 74 Q98 50 82 26 Q64 14 64 74Z M64 74 Q50 40 64 20 Q78 40 64 74Z" '
    f'fill="none" stroke="#7D879E" stroke-width="3.4" stroke-linejoin="round"/>'
    f'<rect x="52" y="2" width="24" height="24" rx="9" fill="#7AD3C8" {W(3)}/>'
    + eye(59, 13, 0.5) + eye(69, 13, 0.5) +
    f'<path d="M14 78 H114 Q110 116 64 116 Q18 116 14 78Z" fill="#FF8DB4" {W(3.4)}/>'
    f'<path d="M18 78 Q24 62 40 68 Q48 54 64 64 Q80 54 88 68 Q104 62 110 78Z" fill="#FFFDF5" {W(2.6)}/>'
    f'<circle cx="22" cy="44" r="4" fill="#fff" {W(1.6)}/><circle cx="108" cy="48" r="3.5" fill="#fff" {W(1.6)}/><circle cx="100" cy="28" r="3" fill="#fff" {W(1.4)}/>'
    + face(64, 94, d=12, k=0.8))

# 11. Маленький остров (Зеленоград) — розовая морская звёздочка в колпачке у бассейна с шариками
I["fun-malenky-ostrov-zelenograd"] = ("#E6F6FF", "#58B6E8",
    "розовая морская звёздочка в праздничном колпачке",
    "пришла на детский праздник и сидит на бортике сухого бассейна, держа свечку от торта",
    f'<rect x="0" y="96" width="128" height="32" fill="#FFFFFF" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="7" fill="{c}" {W(1.8)}/>' for x, y, c in
              ((14, 108, "#FF5C7A"), (30, 112, "#FFD23F"), (46, 106, "#4FC3F7"), (62, 112, "#8BD86A"), (78, 106, "#FF9F43"),
               (94, 112, "#B388FF"), (110, 106, "#FF5C7A"), (22, 122, "#4FC3F7"), (54, 124, "#FFD23F"), (86, 124, "#FF5C7A"),
               (118, 122, "#8BD86A"))) +
    f'<path d="M64 30 L72 54 L98 56 L78 72 L86 98 L64 82 L42 98 L50 72 L30 56 L56 54Z" fill="#FF8FB8" {W(3.2)}/>'
    + face(64, 64, d=7, k=0.6) +
    f'<path d="M54 34 L64 8 L74 34Z" fill="#FFD23F" {W(2.6)} transform="rotate(-8 64 30)"/><circle cx="62" cy="8" r="4" fill="#FF5C7A" {W(1.8)}/>'
    f'<rect x="100" y="40" width="6" height="20" rx="2" fill="#7FD3FF" {W(2)}/><path d="M103 40 q-4 -6 0 -12 q4 6 0 12Z" fill="#FFB02E" {W(1.6)}/>'
    f'<path d="M92 58 L100 54" stroke="#3B3355" stroke-width="2.6" stroke-linecap="round"/>'
    + sparkle(20, 28, 4, "#FFFFFF") + sparkle(30, 50, 2.5, "#FFFFFF"))

if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
