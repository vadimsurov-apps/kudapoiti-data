"""Иконки робота fun (2026-11-13, проход f): места из tools/add_fun_1113f.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя компоновка и палитра фона.
Запуск: python3 tools/icons_fun_1113f.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
O = "#3B3355"
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}

# 1. «Медведь» Петровско-Разумовское — электронная мишень лазертага на треноге ловит красный луч в датчик
I["lt-medved-petrovsko-razumovskoe"] = ("#E9FFE0", "#5FA85A",
    "электронная мишень лазертага — чёрный диск с красным светящимся датчиком-яблочком на трёхногой стойке",
    "ловит красный лазерный луч, прилетевший слева, прямо в датчик и радостно жмурится от попадания",
    # тренога
    f'<path d="M70 92 L52 124 M70 92 L88 124 M70 92 V124" stroke="#6B4A2B" stroke-width="5" stroke-linecap="round"/>'
    # диск
    f'<circle cx="70" cy="62" r="34" fill="#2E2B3A" {W(3.4)}/>'
    f'<circle cx="70" cy="62" r="25" fill="none" stroke="#FFD24A" stroke-width="3"/>'
    f'<circle cx="70" cy="62" r="11" fill="#FF3B3B" {W(2.6)}/>'
    f'<circle cx="66" cy="58" r="3.5" fill="#FFC2C2"/>'
    # сияние попадания
    + "".join(f'<path d="M{70+16*dx} {62+16*dy} L{70+22*dx} {62+22*dy}" stroke="#FFE27A" stroke-width="3" stroke-linecap="round"/>'
              for dx, dy in ((0, -1), (1, 0), (0.7, 0.7), (-0.7, 0.7), (0.7, -0.7)))
    # луч слева
    + f'<path d="M0 74 L58 63" stroke="#FF4D4D" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M0 74 L58 63" stroke="#FFD0D0" stroke-width="1.4"/>'
    # зажмуренные глазки и улыбка на диске
    + f'<path d="M50 50 q5 -6 10 0 M80 50 q5 -6 10 0" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round"/>'
    f'<path d="M58 84 Q70 92 82 84" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>'
    + sparkle(104, 24, 5, "#fff") + sparkle(22, 30, 4, "#fff"))

# 2. «Медведь» Братеево — братья-лазертагеры спина к спине
def kid(cx, flip, shirt, band, gun):
    k = -1 if flip else 1
    return (
        f'<path d="M{cx-12} 120 V96 Q{cx-12} 84 {cx} 84 Q{cx+12} 84 {cx+12} 96 V120Z" fill="{shirt}" {W(3)}/>'
        f'<circle cx="{cx}" cy="66" r="15" fill="#FFD9B8" {W(3)}/>'
        f'<path d="M{cx-15} 60 Q{cx} 46 {cx+15} 60 Q{cx} 54 {cx-15} 60Z" fill="#7A4A26" {W(2.2)}/>'
        f'<rect x="{cx-16}" y="58" width="32" height="6" rx="3" fill="{band}" {W(2)}/>'
        f'<circle cx="{cx}" cy="61" r="2.6" fill="#FFF36B"/>'
        + eye(cx + 5 * k, 69, 0.7) + f'<path d="M{cx+1*k} 75 q{4*k} 3 {8*k} 0" fill="none" stroke="{O}" stroke-width="2" stroke-linecap="round"/>'
        # бластер наружу на уровне груди и луч к краю
        f'<path d="M{cx+6*k} 94 H{cx+34*k} V102 H{cx+18*k} L{cx+16*k} 110 H{cx+10*k} L{cx+10*k} 102 H{cx+6*k}Z" fill="{gun}" {W(2.6)}/>'
        f'<circle cx="{cx+34*k}" cy="98" r="3.2" fill="#FFF36B" {W(1.4)}/>'
        f'<path d="M{cx+38*k} 98 H{cx+80*k}" stroke="{gun}" stroke-width="3" stroke-linecap="round" opacity=".9"/>'
    )

I["lt-medved-brateevo"] = ("#3D3F8F", "#1B1A45",
    "два брата-лазертагера — младший в красной футболке, старший в синей, у обоих налобные повязки с огоньком",
    "стоят спина к спине в тёмном неоновом зале и держат светящиеся бластеры стволами вверх",
    # неоновые полосы
    "".join(f'<path d="M0 {y} H128" stroke="{c}" stroke-width="2" opacity=".7"/>' for y, c in ((30, "#5CF2FF"), (40, "#FF5CD6")))
    + kid(48, True, "#E94B4B", "#2EC4B6", "#FF9F1C") + kid(80, False, "#3D7BFF", "#FF5CD6", "#B8F35A")
    + sparkle(20, 104, 4, "#5CF2FF") + sparkle(108, 106, 4, "#FF5CD6"))

# 3. Rabbit Hole «Авиапарк» — неоновая нора-воронка, из неё выпрыгивает девочка с бластером
I["fun-rabbit-hole-aviapark"] = ("#5A2A7A", "#22103A",
    "круглая неоновая нора-воронка из розовых, фиолетовых и голубых колец",
    "из её глубины выпрыгивает к нам девочка с хвостиками и зелёным бластером, вокруг летают лазерные искры",
    # кольца норы
    "".join(f'<ellipse cx="64" cy="92" rx="{rx}" ry="{rx*0.42}" fill="none" stroke="{c}" stroke-width="3.4"/>'
            for rx, c in ((56, "#FF5CD6"), (44, "#B07CFF"), (32, "#5CF2FF"), (20, "#FF5CD6")))
    + f'<ellipse cx="64" cy="92" rx="10" ry="4.2" fill="#0B0618"/>'
    # девочка
    f'<path d="M52 104 L58 76 H70 L76 104" fill="#FFC857" {W(3)}/>'
    f'<circle cx="64" cy="58" r="15" fill="#FFD9B8" {W(3)}/>'
    f'<path d="M49 54 Q64 38 79 54 Q64 48 49 54Z" fill="#3B2A1E" {W(2.2)}/>'
    f'<path d="M48 52 q-12 2 -12 14 q8 -2 12 -8Z M80 52 q12 2 12 14 q-8 -2 -12 -8Z" fill="#3B2A1E" {W(2)}/>'
    + face(64, 62, d=9, k=0.8)
    # руки и бластер
    + f'<path d="M58 82 L44 74 M70 82 L84 72" stroke="#FFD9B8" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M80 64 H104 V72 H92 L90 80 H84Z" fill="#4CD964" {W(2.6)}/>'
    f'<circle cx="104" cy="68" r="3" fill="#FFF36B"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.4" fill="{c}"/>' for x, y, c in ((112, 52, "#7DFFB0"), (22, 40, "#FF5CD6"),
                                                                                (106, 30, "#5CF2FF"), (30, 72, "#FFF36B")))
    + sparkle(24, 22, 4, "#fff"))

# 4. Музей шоколада в Крылатском — плитка-малыш в старинной жестяной коробке конфет
I["museum-shokolad-krylatskoe"] = ("#FFF1D6", "#E0A458",
    "молочная шоколадная плитка-малыш в квадратиках с отломанным уголком",
    "лежит, как в кроватке, в открытой старинной красной жестяной коробке конфет с золотым вензелем на откинутой крышке",
    # крышка (откинута назад)
    f'<path d="M24 22 H104 L98 58 H30Z" fill="#C8322E" {W(3)}/>'
    f'<path d="M30 28 H98 L94 52 H34Z" fill="none" stroke="#F5C451" stroke-width="2"/>'
    f'<path d="M56 40 q8 -12 16 0 q-8 10 -16 0Z" fill="#F5C451" {W(1.6)}/>'
    # коробка
    f'<path d="M18 62 H110 V108 Q64 118 18 108Z" fill="#B3282A" {W(3.2)}/>'
    f'<path d="M18 62 H110" stroke="#F5C451" stroke-width="3"/>'
    f'<rect x="26" y="64" width="76" height="40" rx="4" fill="#F7E6C4" {W(2.4)}/>'
    # плитка
    f'<path d="M30 68 H92 L98 74 V100 H30Z" fill="#8B5A2B" {W(2.8)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="13" height="10" rx="2" fill="#9C6A38" stroke="#6E4520" stroke-width="1.4"/>'
              for x in (34, 50, 66, 82) for y in (72, 86) if not (x == 82 and y == 72))
    + f'<path d="M92 68 L98 74 L90 76Z" fill="#F7E6C4" {W(1.4)}/>'
    + eye(52, 82, 0.8) + eye(72, 82, 0.8)
    + f'<path d="M56 92 Q62 97 68 92" fill="none" stroke="#FFF1D6" stroke-width="2.4" stroke-linecap="round"/>'
    f'<circle cx="46" cy="89" r="3" fill="#E58A8A" opacity=".7"/><circle cx="78" cy="89" r="3" fill="#E58A8A" opacity=".7"/>'
    # крошка отломанного уголка
    f'<path d="M106 114 l6 -2 l1 5 l-6 1Z" fill="#8B5A2B" {W(1.6)}/>'
    + sparkle(112, 18, 5, "#fff") + sparkle(14, 46, 4, "#fff"))

if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
