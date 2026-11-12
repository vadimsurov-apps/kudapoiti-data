"""Иконки робота fun (2026-11-12, проход n): места из tools/add_fun_1112n.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя компоновка и палитра фона.
Запуск: python3 tools/icons_fun_1112n.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}

# 1. Пеленальная на Андреевской набережной — складной пеленальный коврик раскрылся на гранитном парапете, над рекой чайка
I["chg-andreevskaya-nab"] = ("#DDF4F0", "#5FB3B0",
    "складной дорожный пеленальный коврик в мятную клетку с мордашкой на клапане",
    "раскрылся на гранитном парапете набережной, как книжка, а над рекой пролетает белая чайка",
    # река
    f'<rect x="0" y="96" width="128" height="40" fill="#3E8FC4"/>'
    f'<path d="M10 108 q8 -4 16 0 t16 0 M70 116 q8 -4 16 0 t16 0" fill="none" stroke="#BDE6FF" stroke-width="2.4" stroke-linecap="round"/>'
    # парапет
    f'<rect x="-4" y="78" width="136" height="20" fill="#B8B2AA" {W(3)}/>'
    + "".join(f'<path d="M{x} 78 V98" stroke="#8E877F" stroke-width="2"/>' for x in (30, 64, 98))
    # коврик: две половинки
    + f'<path d="M20 74 L60 70 L60 34 L22 40Z" fill="#B8EBD8" {W(3)}/>'
    f'<path d="M68 70 L108 74 L106 40 L68 34Z" fill="#B8EBD8" {W(3)}/>'
    + "".join(f'<path d="M{20+i*10} {73-i} L{22+i*10} {40-i*0.2}" stroke="#7CCBB0" stroke-width="2"/>' for i in range(1, 4))
    + "".join(f'<path d="M{68+i*10} {70+i} L{68+i*10} {34+i*1.5}" stroke="#7CCBB0" stroke-width="2"/>' for i in range(1, 4))
    + f'<path d="M22 52 L60 48 M22 63 L60 59 M68 48 L106 52 M68 59 L107 63" stroke="#7CCBB0" stroke-width="2"/>'
    # корешок-клапан с мордашкой
    f'<rect x="58" y="30" width="12" height="44" rx="5" fill="#2FA37F" {W(2.8)}/>'
    + face(86, 56, d=8, k=0.8) +
    # чайка
    f'<path d="M30 20 Q38 12 46 20 Q54 12 62 20" fill="none" stroke="#3B3355" stroke-width="3" stroke-linecap="round"/>'
    f'<circle cx="46" cy="21" r="2.4" fill="#fff" {W(1.6)}/>'
    + sparkle(104, 20, 4, "#fff") + sparkle(14, 30, 3, "#fff"))

# 2. Babyback — двухэтажная мягкая игровая башня, малыш машет из окошка второго этажа, внизу батут
I["fun-babyback-sheremetyevskaya"] = ("#FFE9F2", "#E87FA8",
    "двухэтажная мягкая игровая башня с сетчатым окошком наверху и жёлтой крышей-шатром",
    "малыш машет из окошка второго этажа, а у подножия башни пружинит маленький круглый батут",
    # башня
    f'<rect x="30" y="38" width="56" height="70" rx="6" fill="#7FD3F7" {W(3.2)}/>'
    f'<path d="M30 74 H86" stroke="#3B3355" stroke-width="3"/>'
    f'<path d="M24 40 L58 12 L92 40Z" fill="#FFD23F" {W(3.2)}/>'
    f'<circle cx="58" cy="12" r="4" fill="#FF6B6B" {W(2)}/>'
    # окно второго этажа с сеткой
    f'<rect x="42" y="46" width="32" height="22" rx="4" fill="#FFF6E0" {W(2.6)}/>'
    # малыш
    f'<circle cx="58" cy="58" r="8" fill="#FFD9B8" {W(2.4)}/>'
    + face(58, 59, d=5, k=0.55) +
    f'<path d="M66 56 Q72 48 70 44" fill="none" stroke="#3B3355" stroke-width="2.6" stroke-linecap="round"/>'
    f'<circle cx="70" cy="43" r="3" fill="#FFD9B8" {W(1.8)}/>'
    + "".join(f'<path d="M{x} 46 V68" stroke="#3B3355" stroke-width="1" opacity=".45"/>' for x in (48, 54, 62, 68))
    + "".join(f'<path d="M42 {y} H74" stroke="#3B3355" stroke-width="1" opacity=".45"/>' for y in (52, 62))
    # дверь первого этажа
    + f'<path d="M48 108 V88 Q58 78 68 88 V108" fill="#5B5BD6" {W(2.6)}/>'
    # батут
    f'<ellipse cx="100" cy="98" rx="16" ry="6" fill="#3B3355" {W(2.6)}/>'
    f'<ellipse cx="100" cy="96.5" rx="12.5" ry="3.8" fill="#6EE7B7"/>'
    f'<path d="M87 100 L85 108 M113 100 L115 108 M100 104 V110" stroke="#3B3355" stroke-width="3" stroke-linecap="round"/>'
    
    + sparkle(104, 86, 4, "#fff") + sparkle(16, 60, 3, "#fff"))

# 3. Just Me — картонная коробка-ракета, малыш выглядывает из иллюминатора, рядом фломастеры
I["fun-justme-khoroshevskaya"] = ("#F2ECFF", "#9C86E0",
    "большая картонная коробка-ракета с нарисованным иллюминатором и бумажным носом-конусом",
    "малыш выглядывает из иллюминатора, а рядом на полу лежат три фломастера, которыми её разрисовали",
    # конус
    f'<path d="M38 44 L64 10 L90 44Z" fill="#FF8A5B" {W(3.2)}/>'
    # коробка
    f'<rect x="38" y="44" width="52" height="58" rx="3" fill="#D9A866" {W(3.2)}/>'
    f'<path d="M38 56 H90" stroke="#B5844A" stroke-width="2"/>'
    # крылья
    f'<path d="M38 82 L24 104 L38 102Z" fill="#FF8A5B" {W(2.8)}/>'
    f'<path d="M90 82 L104 104 L90 102Z" fill="#FF8A5B" {W(2.8)}/>'
    # иллюминатор с малышом
    f'<circle cx="64" cy="74" r="15" fill="#BFE6FF" {W(3)}/>'
    f'<circle cx="64" cy="76" r="9" fill="#FFD9B8" {W(2.2)}/>'
    f'<path d="M56 72 Q64 62 72 72" fill="#5A3B2E" {W(1.8)}/>'
    + face(64, 78, d=5, k=0.55) +
    # нарисованные звёздочки на коробке
    sparkle(48, 94, 3.5, "#FFF3B0") + sparkle(80, 50, 3, "#FFF3B0") +
    # фломастеры на полу
    f'<rect x="6" y="112" width="26" height="6" rx="3" fill="#FF4D6D" {W(2)}/>'
    f'<rect x="96" y="110" width="26" height="6" rx="3" fill="#2FA37F" {W(2)}/>'
    f'<rect x="100" y="118" width="24" height="6" rx="3" fill="#4D8BFF" {W(2)}/>'
    f'<path d="M30 98 Q34 104 36 108" fill="none" stroke="#FF4D6D" stroke-width="2.4" stroke-linecap="round"/>')

# 4. «Игра и культура» — сюжетно-ролевая игра в магазин: девочка в маминой шляпе протягивает монетку мальчику за прилавком
I["fun-igra-i-kultura-spasskaya"] = ("#FFF4D9", "#E7B04D",
    "девочка в большой маминой соломенной шляпе с красным цветком и с плетёной корзинкой",
    "играет в магазин: протягивает картонную монетку мальчику-продавцу за прилавком из табуретки с яблоком",
    # прилавок-табуретка
    f'<rect x="72" y="80" width="46" height="8" rx="2" fill="#C98E5A" {W(2.8)}/>'
    f'<path d="M78 88 V118 M112 88 V118" stroke="#3B3355" stroke-width="4" stroke-linecap="round"/>'
    f'<circle cx="104" cy="74" r="6" fill="#FF4D4D" {W(2.2)}/><path d="M104 68 q2 -4 5 -4" fill="none" stroke="#2FA37F" stroke-width="2.4"/>'
    # мальчик-продавец
    f'<circle cx="92" cy="54" r="11" fill="#FFD9B8" {W(2.6)}/>'
    f'<path d="M81 50 Q92 38 103 50" fill="#3B2A20" {W(2)}/>'
    + face(92, 56, d=6, k=0.6) +
    f'<path d="M80 80 Q80 66 92 66 Q104 66 104 80" fill="#5BB8FF" {W(2.6)}/>'
    # девочка
    f'<path d="M22 118 Q24 82 42 80 Q60 82 60 118Z" fill="#FF8FB1" {W(2.8)}/>'
    f'<circle cx="42" cy="64" r="13" fill="#FFD9B8" {W(2.6)}/>'
    + face(42, 66, d=7, k=0.65) +
    # шляпа
    f'<ellipse cx="42" cy="54" rx="26" ry="7" fill="#F2D27A" {W(2.8)}/>'
    f'<path d="M30 54 Q32 36 42 36 Q52 36 54 54" fill="#F2D27A" {W(2.8)}/>'
    f'<circle cx="53" cy="45" r="4.5" fill="#E8344E" {W(1.8)}/>'
    # рука с монеткой
    f'<path d="M56 92 Q66 86 70 78" fill="none" stroke="#3B3355" stroke-width="3" stroke-linecap="round"/>'
    f'<circle cx="72" cy="74" r="5" fill="#FFC93C" {W(2)}/>'
    # корзинка
    f'<path d="M14 98 h18 l-3 12 h-12Z" fill="#C98E5A" {W(2.2)}/><path d="M17 98 Q23 88 29 98" fill="none" stroke="#3B3355" stroke-width="2"/>'
    + sparkle(110, 24, 4, "#fff") + sparkle(18, 22, 3, "#fff"))

# 5. Буби Room — стенка-скалолазка над поролоновой ямой, малыш спиной плюхается в кирпичики
I["fun-bubiroom-sergiev-posad"] = ("#E4F7FF", "#4FA9DA",
    "синяя стенка-скалолазка с разноцветными зацепами-звёздочками",
    "малыш отпустил зацепы и спиной плюхается в поролоновую яму с жёлтыми и розовыми кирпичиками",
    # стенка
    f'<rect x="72" y="6" width="44" height="88" rx="4" fill="#3B6FD6" {W(3.2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="{c}" {W(1.8)}/>' for x, y, c in
              ((82, 20, "#FFD23F"), (104, 30, "#FF6B6B"), (86, 44, "#6EE7B7"), (106, 58, "#FFB3CF"), (84, 72, "#FFD23F"), (102, 82, "#FF8A5B")))
    # яма
    + f'<rect x="4" y="92" width="120" height="40" rx="6" fill="#7A4FC4" {W(3.2)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="14" height="10" rx="2" fill="{c}" {W(1.8)} transform="rotate({r} {x+7} {y+5})"/>'
              for x, y, c, r in ((10, 92, "#FFD23F", -12), (26, 96, "#FF9EC4", 10), (88, 94, "#FF9EC4", -8), (104, 92, "#FFD23F", 14),
                                 (16, 106, "#FF9EC4", 6), (96, 108, "#FFD23F", -6), (78, 104, "#FFF3B0", 18)))
    # малыш в полёте спиной вниз
    + f'<path d="M30 80 Q44 70 62 78 Q58 92 40 92 Q30 90 30 80Z" fill="#FF6B6B" {W(2.8)}/>'
    f'<circle cx="26" cy="74" r="11" fill="#FFD9B8" {W(2.6)}/>'
    + face(26, 75, d=6, k=0.6) +
    f'<path d="M56 78 L70 60 M60 84 L74 72" stroke="#3B3355" stroke-width="3" stroke-linecap="round"/>'
    f'<path d="M34 72 L40 56 M40 74 L50 58" stroke="#3B3355" stroke-width="3" stroke-linecap="round"/>'
    + sparkle(48, 30, 4, "#fff") + sparkle(20, 46, 3, "#fff"))


if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
