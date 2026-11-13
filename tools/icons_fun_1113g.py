"""Иконки робота fun (2026-11-13, проход g): места из tools/add_fun_1113g.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя компоновка и палитра фона.
Запуск: python3 tools/icons_fun_1113g.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
O = "#3B3355"
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}

# 1. Метрополис (-1 этаж) — электрический стерилизатор-колпак, внутри три бутылочки, сверху пар
I["chg-metropolis"] = ("#E4F0FF", "#7C93D8",
    "белый электрический стерилизатор для бутылочек с прозрачным куполом и синей кнопкой",
    "под куполом стоят три крошечные бутылочки, из дырочки сверху поднимается пар завитками, стерилизатор жмурится от удовольствия",
    # подставка
    f'<rect x="26" y="92" width="76" height="22" rx="9" fill="#FFFFFF" {W(3.2)}/>'
    f'<circle cx="88" cy="103" r="5" fill="#3D7BFF" {W(2)}/>'
    f'<rect x="34" y="99" width="40" height="7" rx="3.5" fill="#BFE3FF" stroke="{O}" stroke-width="1.8"/>'
    # купол
    f'<path d="M30 92 V60 Q30 30 64 30 Q98 30 98 60 V92Z" fill="#DDF3FF" fill-opacity=".75" {W(3.2)}/>'
    f'<rect x="58" y="24" width="12" height="7" rx="3" fill="#FFFFFF" {W(2.4)}/>'
    # три бутылочки
    + "".join(f'<rect x="{x-6}" y="{y}" width="12" height="{92-y}" rx="4" fill="#FFFFFF" {W(2.2)}/>'
              f'<path d="M{x-4} {y} Q{x} {y-10} {x+4} {y}Z" fill="{c}" {W(1.8)}/>'
              f'<path d="M{x-6} {y+10} H{x+6} M{x-6} {y+16} H{x+6}" stroke="#9BB7E0" stroke-width="1.4"/>'
              for x, y, c in ((44, 62, "#FF9EC4"), (64, 56, "#FFD24A"), (84, 62, "#8FE0B0")))
    # пар
    + f'<path d="M58 20 q-6 -6 0 -12 q6 -6 0 -12 M70 20 q6 -6 0 -12" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    # мордашка на подставке: зажмуренные глазки
    + f'<path d="M40 109 q4 -4 8 0" fill="none" stroke="{O}" stroke-width="2.2" stroke-linecap="round"/>'
    f'<path d="M56 109 q4 -4 8 0" fill="none" stroke="{O}" stroke-width="2.2" stroke-linecap="round"/>'
    + sparkle(110, 46, 5, "#fff") + sparkle(16, 70, 4, "#fff"))

# 2. Бутово Молл — силиконовая тарелка на присоске с тремя отделениями прилипла к столику
I["chg-butovo-mall"] = ("#FFF0D6", "#F2A65A",
    "мятная силиконовая детская тарелка на присоске с тремя отделениями-секциями",
    "крепко присосалась к деревянному столику и упирается, пока маленькая ручка пытается её оторвать",
    # столик
    f'<rect x="0" y="94" width="128" height="40" fill="#C98B4E" {W(3)}/>'
    f'<path d="M0 104 H128" stroke="#A86E38" stroke-width="2"/>'
    # тарелка в перспективе
    f'<ellipse cx="64" cy="82" rx="46" ry="20" fill="#7FDCC0" {W(3.2)}/>'
    f'<ellipse cx="64" cy="78" rx="40" ry="15" fill="#A8EED8" stroke="{O}" stroke-width="2.2"/>'
    f'<path d="M64 63 V78 M64 78 L36 86 M64 78 L92 86" stroke="#5CB89C" stroke-width="3" stroke-linecap="round"/>'
    # еда в отделениях
    f'<circle cx="50" cy="72" r="5" fill="#FFB347" stroke="{O}" stroke-width="1.6"/>'
    f'<circle cx="78" cy="71" r="4" fill="#9ED36A" stroke="{O}" stroke-width="1.6"/><circle cx="84" cy="74" r="3.5" fill="#9ED36A" stroke="{O}" stroke-width="1.6"/>'
    f'<path d="M58 88 q6 -6 12 0" fill="#FFF3B0" stroke="{O}" stroke-width="1.6"/>'
    # присоска-ножка под тарелкой
    f'<path d="M46 98 Q64 108 82 98" fill="#5CB89C" {W(2.6)}/>'
    # мордашка на бортике: упрямо надутые щёчки
    + eye(42, 86, 0.65) + eye(86, 86, 0.65)
    # детская ручка тянет за край
    + f'<path d="M108 66 Q118 58 128 60 V74 Q118 76 108 74Z" fill="#FFD9B8" {W(2.6)}/>'
    f'<circle cx="106" cy="70" r="7" fill="#FFD9B8" {W(2.6)}/>'
    + f'<path d="M98 50 l4 6 M106 46 l1 7 M90 54 l5 5" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    + sparkle(22, 36, 5, "#fff"))

# 3. Облака — стопка из трёх сложенных фланелевых пелёнок лежит на облаке
I["chg-oblaka"] = ("#F3E8FF", "#9C8BE0",
    "стопка из трёх сложенных фланелевых пелёнок — розовая в цветочек, мятная в полоску и жёлтая в горошек",
    "мягко покачивается на пушистом белом облаке в сиреневом небе, верхняя пелёнка сонно улыбается",
    # облако
    f'<path d="M14 104 Q8 86 26 84 Q28 68 46 72 Q56 58 72 68 Q90 60 98 76 Q118 74 116 94 Q122 108 104 110 H26 Q12 112 14 104Z" fill="#FFFFFF" {W(3)}/>'
    # пелёнки снизу вверх
    f'<rect x="32" y="78" width="64" height="14" rx="6" fill="#FFE27A" {W(2.8)}/>'
    + "".join(f'<circle cx="{x}" cy="85" r="2" fill="#F2B544"/>' for x in (40, 52, 64, 76, 88))
    + f'<rect x="36" y="62" width="58" height="16" rx="6" fill="#9BE7CF" {W(2.8)}/>'
    + "".join(f'<path d="M{x} 63 V77" stroke="#6CC9AD" stroke-width="3"/>' for x in (46, 56, 66, 76, 86))
    + f'<rect x="40" y="42" width="52" height="20" rx="7" fill="#FFC2D9" {W(2.8)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#fff"/><circle cx="{x}" cy="{y}" r="1.1" fill="#F27BA8"/>'
              for x, y in ((48, 47), (84, 47), (50, 57), (82, 57)))
    # сонное лицо на верхней пелёнке
    + f'<path d="M57 51 q3 3 6 0 M69 51 q3 3 6 0" fill="none" stroke="{O}" stroke-width="2.2" stroke-linecap="round"/>'
    f'<path d="M62 56 q4 3 8 0" fill="none" stroke="{O}" stroke-width="2" stroke-linecap="round"/>'
    + f'<text x="98" y="38" font-family="Arial" font-weight="bold" font-size="12" fill="#fff">z</text>'
    f'<text x="106" y="28" font-family="Arial" font-weight="bold" font-size="9" fill="#fff">z</text>'
    + sparkle(22, 40, 5, "#fff"))

# 4. Каширская Плаза — ниблер с клубникой внутри сеточки
I["chg-kashirskaya-plaza"] = ("#FFE6EA", "#E8667E",
    "ниблер — детский прикормочник с сеточкой и кусочком клубники внутри, на оранжевой ручке-колечке",
    "стоит ручкой вниз, как эскимо, и подмигивает, а внутри сеточки краснеет клубничка",
    # ручка-колечко
    f'<circle cx="64" cy="104" r="13" fill="none" stroke="{O}" stroke-width="9"/>'
    f'<circle cx="64" cy="104" r="13" fill="none" stroke="#FF9F3A" stroke-width="5.5"/>'
    # держатель
    f'<path d="M44 76 H84 L78 90 H50Z" fill="#FF9F3A" {W(3)}/>'
    # сеточка
    f'<path d="M46 76 Q38 46 64 24 Q90 46 82 76Z" fill="#FFF7F7" fill-opacity=".85" {W(3)}/>'
    # клубника внутри
    f'<path d="M64 70 Q48 58 52 44 Q64 36 76 44 Q80 58 64 70Z" fill="#F0384F" {W(2.4)}/>'
    f'<path d="M56 42 L60 36 L64 41 L68 36 L72 42" fill="#59B34A" {W(2)}/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="1.2" ry="1.8" fill="#FFE27A"/>' for x, y in ((58, 50), (70, 50), (64, 57), (59, 61), (69, 61)))
    # сетка поверх
    + "".join(f'<path d="M{48+i*8} 74 Q{50+i*7} 48 64 26" fill="none" stroke="#C9B6C0" stroke-width="1.2"/>' for i in range(5))
    + "".join(f'<path d="M{44+i} {40+i*10} H{84-i}" stroke="#C9B6C0" stroke-width="1.2"/>' for i in range(4))
    # мордашка на держателе: подмигивает
    + eye(56, 82, 0.6) + f'<path d="M68 82 q3 -3 6 0" fill="none" stroke="{O}" stroke-width="2" stroke-linecap="round"/>'
    + sparkle(100, 30, 6, "#fff") + sparkle(24, 54, 4, "#fff"))

# 5. Мегаполис — детские маникюрные ножнички с закруглёнными кончиками
I["chg-megapolis"] = ("#E0FFF4", "#3FB59A",
    "детские маникюрные ножнички с закруглёнными кончиками и большими розовыми кольцами-ручками",
    "стоят на кончиках, как балерина, раскрыв лезвия буквой «Л», и осторожно улыбаются",
    # лезвия
    f'<path d="M60 70 L42 16 Q40 10 46 12 L64 62Z" fill="#E6EDF2" {W(2.8)}/>'
    f'<path d="M68 70 L86 16 Q88 10 82 12 L64 62Z" fill="#D2DCE3" {W(2.8)}/>'
    f'<circle cx="44" cy="14" r="4" fill="#E6EDF2" {W(2.2)}/><circle cx="84" cy="14" r="4" fill="#D2DCE3" {W(2.2)}/>'
    # винтик
    f'<circle cx="64" cy="68" r="5" fill="#FFD24A" {W(2.4)}/>'
    # ручки-кольца
    f'<path d="M60 72 Q44 82 42 94" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M60 72 Q44 82 42 94" fill="none" stroke="#FF8DB8" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M68 72 Q84 82 86 94" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M68 72 Q84 82 86 94" fill="none" stroke="#FF8DB8" stroke-width="5" stroke-linecap="round"/>'
    f'<ellipse cx="38" cy="104" rx="13" ry="11" fill="none" stroke="{O}" stroke-width="9"/>'
    f'<ellipse cx="38" cy="104" rx="13" ry="11" fill="none" stroke="#FF8DB8" stroke-width="5"/>'
    f'<ellipse cx="90" cy="104" rx="13" ry="11" fill="none" stroke="{O}" stroke-width="9"/>'
    f'<ellipse cx="90" cy="104" rx="13" ry="11" fill="none" stroke="#FF8DB8" stroke-width="5"/>'
    # мордашка на лезвиях
    + eye(57, 46, 0.6) + eye(71, 46, 0.6)
    + f'<path d="M60 54 q4 3 8 0" fill="none" stroke="{O}" stroke-width="2" stroke-linecap="round"/>'
    + sparkle(110, 40, 5, "#fff") + sparkle(18, 50, 5, "#fff") + sparkle(64, 112, 4, "#fff"))

# 6. Зеленопарк — голубая груша-аспиратор для носика
I["chg-zelenopark"] = ("#EAF7FF", "#5FA8E8",
    "голубая резиновая груша-аспиратор для носика малыша с белым мягким наконечником",
    "стоит носиком вверх в белой раковине, зажмурилась и громко чихает облачком пузырьков",
    # раковина
    f'<path d="M0 100 H128 V128 H0Z" fill="#FFFFFF" {W(3)}/>'
    f'<path d="M8 100 Q64 122 120 100" fill="#D7EEFA" stroke="{O}" stroke-width="2.4"/>'
    # груша: шар внизу, сужающийся носик вверх
    f'<path d="M56 50 Q30 58 32 82 Q34 104 58 104 Q82 104 84 82 Q86 58 64 50 L62 34 H58Z" fill="#57B6F0" {W(3.2)}/>'
    f'<ellipse cx="46" cy="70" rx="7" ry="10" fill="#BFE6FF" opacity=".8"/>'
    f'<path d="M57 36 Q56 22 60 16 Q64 22 63 36Z" fill="#FFFFFF" {W(2.6)}/>'
    # чих-пузырьки
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" fill-opacity=".75" stroke="#3B83B8" stroke-width="1.3"/>'
              for x, y, r in ((72, 12, 4), (80, 22, 3), (84, 10, 2.5), (50, 10, 2.6)))
    # мордашка: зажмуренные глаза, рот «апчхи»
    + f'<path d="M46 76 l6 3 l-6 3 M70 76 l-6 3 l6 3" fill="none" stroke="{O}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'
    f'<ellipse cx="58" cy="92" rx="5" ry="4" fill="{O}"/>'
    f'<ellipse cx="42" cy="88" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/><ellipse cx="74" cy="88" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/>'
    + sparkle(20, 34, 5, "#fff"))

# 7. Лазертаг Лофт — армейский ящик-укрытие, за ним бластер, над ним лучи
I["fun-lazertag-loft-chertanovo"] = ("#6B4A8F", "#24163A",
    "деревянный армейский ящик-укрытие с жёлтой трафаретной звездой и мордашкой",
    "за ящиком прячется зелёный кончик игрушечного бластера, а над ним в тёмном зале проносятся красные и голубые лучи",
    # пол
    f'<rect x="0" y="104" width="128" height="30" fill="#3A2A55"/>'
    # лучи
    f'<path d="M0 30 L128 52" stroke="#FF4D6D" stroke-width="4" stroke-linecap="round"/><path d="M0 30 L128 52" stroke="#FFD0DA" stroke-width="1.3"/>'
    f'<path d="M128 20 L10 62" stroke="#4DD9FF" stroke-width="4" stroke-linecap="round"/><path d="M128 20 L10 62" stroke="#D0F6FF" stroke-width="1.3"/>'
    # бластер выглядывает
    # ящик
    f'<rect x="22" y="64" width="80" height="46" rx="4" fill="#B98547" {W(3.2)}/>'
    f'<path d="M22 79 H102 M22 95 H102" stroke="#8A5E2E" stroke-width="2.4"/>'
    f'<rect x="18" y="62" width="88" height="8" rx="3" fill="#9C6C36" {W(2.6)}/>'
    f'<path d="M62 80 l3 7 h7 l-6 4 l2 7 l-6 -4 l-6 4 l2 -7 l-6 -4 h7Z" fill="#FFD24A" stroke="#8A5E2E" stroke-width="1"/>'
    + f'<path d="M84 50 H112 V58 H96 L94 64 H86Z" fill="#7ED957" {W(2.6)}/><circle cx="112" cy="54" r="3.2" fill="#FFF36B" {W(1.4)}/>'
    + eye(42, 88, 0.75) + eye(84, 88, 0.75)
    + f'<path d="M40 100 q4 3 8 0 M80 100 q4 3 8 0" fill="none" stroke="{O}" stroke-width="2" stroke-linecap="round"/>'
    + sparkle(24, 18, 4, "#FFE27A") + sparkle(106, 96, 3, "#4DD9FF"))

# 8. Exitmania Пушкино — картонная коробка, в которой спрятался ребёнок (прятки)
I["fun-exitmania-pushkino"] = ("#2F3B66", "#121831",
    "большая картонная коробка с двумя круглыми дырочками, из которых блестят глаза спрятавшегося ребёнка",
    "стоит в углу тёмного игрового лабиринта, а из-под приоткрытого клапана торчат детские кроссовки",
    # стены лабиринта
    f'<path d="M0 30 H40 V60 M128 40 H94 V70 M0 96 H20" fill="none" stroke="#5B6BA8" stroke-width="7" stroke-linecap="round"/>'
    # коробка
    f'<path d="M28 58 H100 V108 H28Z" fill="#D9A867" {W(3.2)}/>'
    f'<path d="M28 58 L40 44 H112 L100 58Z" fill="#E8BE84" {W(3)}/>'
    f'<path d="M100 58 L112 44 V94 L100 108Z" fill="#B8874A" {W(3)}/>'
    f'<path d="M64 58 V108" stroke="#B8874A" stroke-width="2"/>'
    f'<path d="M30 58 L20 40" stroke="{O}" stroke-width="3.2" stroke-linecap="round"/>'
    f'<path d="M30 58 L20 40 L46 40 L56 58Z" fill="#E8BE84" {W(3)}/>'
    # дырочки с глазками
    f'<circle cx="52" cy="78" r="8" fill="#1A1F33" {W(2.4)}/><circle cx="76" cy="78" r="8" fill="#1A1F33" {W(2.4)}/>'
    f'<circle cx="53" cy="78" r="3.6" fill="#fff"/><circle cx="77" cy="78" r="3.6" fill="#fff"/>'
    f'<circle cx="54" cy="79" r="1.8" fill="#3B3355"/><circle cx="78" cy="79" r="1.8" fill="#3B3355"/>'
    # кроссовки снизу
    f'<path d="M40 108 h16 q4 0 4 6 h-20Z" fill="#FF6B6B" {W(2.4)}/><path d="M68 108 h16 q4 0 4 6 h-20Z" fill="#FF6B6B" {W(2.4)}/>'
    + sparkle(110, 22, 4, "#FFE27A") + sparkle(16, 76, 3, "#fff"))

# 9. Zaga-Game Сергиев Посад — пиксельный VR-снежок
I["fun-zaga-game-sergiev-posad"] = ("#2E6FB7", "#0E1E4A",
    "виртуальный снежок из светящихся голубых пикселей-квадратиков с мордашкой",
    "летит, задорно улыбаясь, над светящейся сеткой VR-арены и рассыпает за собой пиксельные снежинки",
    # сетка арены в перспективе
    "".join(f'<path d="M{64+(x-64)*0.35} 82 L{x} 128" stroke="#59E1FF" stroke-width="1.4" opacity=".7"/>' for x in range(-40, 170, 26))
    + "".join(f'<path d="M0 {y} H128" stroke="#59E1FF" stroke-width="1.4" opacity=".7"/>' for y in (86, 94, 106, 122))
    # хвост из пикселей
    + "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{w}" fill="#BDF3FF" opacity="{o}"/>'
              for x, y, w, o in ((14, 70, 6, .5), (24, 62, 7, .6), (10, 56, 4, .4), (32, 72, 5, .55), (20, 46, 5, .4)))
    # снежок из пикселей
    + "".join(f'<rect x="{46+i*8}" y="{30+j*8}" width="8" height="8" fill="{"#FFFFFF" if (i+j)%3 else "#D7F7FF"}"/>'
              for i in range(5) for j in range(5) if not (i in (0, 4) and j in (0, 4)))
    + f'<path d="M54 30 H78 V38 H86 V62 H78 V70 H54 V62 H46 V38 H54Z" fill="none" {W(3)}/>'
    + eye(59, 48, 0.75) + eye(73, 48, 0.75)
    + f'<path d="M60 58 q6 5 12 0" fill="none" stroke="{O}" stroke-width="2.4" stroke-linecap="round"/>'
    + sparkle(104, 24, 6, "#BDF3FF") + sparkle(108, 60, 4, "#fff"))


if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
