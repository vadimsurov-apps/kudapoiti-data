"""Иконки робота fun (2026-11-11, ночной проход a): места из tools/add_fun_1111a.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя палитра фона.
Запуск: python3 tools/icons_fun_1111a.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye, O
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}


def stars(pts, r=3, c="#fff"):
    return "".join(sparkle(x, y, r, c) for x, y in pts)


# 1. Dancity (Апрелевка): египетский квест
I["fun-dancity-aprelevka"] = ("#FFE9B0", "#D98C2B",
    "золотой саркофаг-малыш с полосатым бирюзовым платком фараона",
    "стоит в песках у тёмного входа в пирамиду и с улыбкой приоткрывает свою крышку",
    f'<path d="M0 104 Q40 92 128 102 V128 H0Z" fill="#F2C46B"/>'
    f'<path d="M84 104 L108 52 L132 104Z" fill="#E7B04E" {W(2.6)}/><path d="M100 104 L108 86 L116 104Z" fill="#5A3A1E"/>'
    f'<path d="M30 118 Q22 80 30 40 Q36 18 56 16 Q76 18 82 40 Q90 80 82 118Z" fill="#F5C531" {W(3.2)}/>'
    f'<path d="M30 52 Q28 28 56 24 Q84 28 82 52 L76 66 H36Z" fill="#34B5C2" {W(2.8)}/>'
    + "".join(f'<path d="M{34+i*4} {36+i*0} L{36+i*4} 64" stroke="#F5C531" stroke-width="3"/>' for i in (0, 10)) +
    f'<ellipse cx="56" cy="50" rx="17" ry="15" fill="#F7D98A" {W(2.6)}/>'
    + face(56, 49, d=7, k=0.75) +
    f'<path d="M50 64 H62 L60 80 H52Z" fill="#34B5C2" {W(2.2)}/>'
    + "".join(f'<path d="M40 {86+i*9} H72" stroke="#C98A1A" stroke-width="3"/>' for i in range(3)) +
    f'<path d="M82 40 Q100 44 96 74 L84 112" fill="#E0A81F" {W(3)}/>'
    + stars(((18, 30), (104, 24)), 4, "#FFFFFF"))

# 2. ПроПрятки (Климовск): квест-прятки
I["fun-propryatki-klimovsk"] = ("#E8E2FF", "#7B6CD9",
    "малыш-привидение под белой простынёй с двумя круглыми прорезями",
    "крадётся на цыпочках мимо горшка с фикусом в тёмной комнате, из-под простыни видны полосатые носки",
    f'<rect x="0" y="100" width="128" height="28" fill="#4E3F9E"/>'
    f'<path d="M96 100 L100 80 H118 L122 100Z" fill="#C4683A" {W(2.6)}/>'
    f'<path d="M109 80 Q96 56 104 42 M109 80 Q118 52 124 46 M109 80 Q108 50 112 36" fill="none" stroke="#3E9E5A" stroke-width="5"/>'
    f'<path d="M34 98 Q26 60 36 36 Q48 14 66 16 Q86 18 92 44 Q98 70 90 98 Q82 92 76 98 Q68 92 62 98 Q54 92 48 98 Q40 92 34 98Z" fill="#FFFFFF" {W(3.2)}/>'
    f'<ellipse cx="54" cy="46" rx="6" ry="7" fill="{O}"/><ellipse cx="74" cy="46" rx="6" ry="7" fill="{O}"/>'
    + eye(54, 46, 0.8) + eye(74, 46, 0.8) +
    f'<ellipse cx="46" cy="58" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/><ellipse cx="82" cy="58" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/>'
    f'<rect x="48" y="98" width="9" height="14" fill="#FFFFFF" {W(2.2)}/><rect x="70" y="98" width="9" height="12" fill="#FFFFFF" {W(2.2)}/>'
    + "".join(f'<path d="M48 {101+i*4} H57 M70 {101+i*4} H79" stroke="#E8434A" stroke-width="2"/>' for i in range(3)) +
    f'<ellipse cx="52" cy="114" rx="7" ry="3.5" fill="#E8434A" {W(2)}/><ellipse cx="76" cy="112" rx="7" ry="3.5" fill="#E8434A" {W(2)}/>'
    + stars(((20, 24), (110, 18)), 3, "#FFF6A8"))

# 3. Holly Polly (Старая Купавна): игровая комната
I["fun-holly-polly-kupavna"] = ("#FFF0F5", "#F7A1C4",
    "детский вигвам из полосатой ткани с флажками на макушке",
    "стоит на мягком ковре игровой, из треугольного входа выглядывает малышка с хвостиками",
    f'<rect x="0" y="104" width="128" height="24" fill="#BDE7C8"/>'
    + "".join(f'<circle cx="{x}" cy="114" r="4" fill="{c}"/>' for x, c in ((14, "#FFD23F"), (114, "#3F9BE8"), (28, "#E8434A")))
    + f'<path d="M64 14 L22 108 H106Z" fill="#FFFFFF" {W(3.2)}/>'
    + "".join(f'<path d="M64 14 L{22+i*14} 108" stroke="{c}" stroke-width="6"/>' for i, c in ((1, "#FF8FB8"), (3, "#7CC8F2"), (5, "#FF8FB8")))
    + f'<path d="M64 14 L22 108 H106Z" fill="none" {W(3.2)}/>'
    f'<path d="M58 6 L64 18 L70 6 M64 18 L64 4" {W(2.6)}/>'
    f'<path d="M70 6 L82 10 L70 14Z" fill="#FFD23F" {W(2)}/>'
    f'<path d="M64 56 L46 108 H82Z" fill="#3B3355"/>'
    f'<circle cx="64" cy="84" r="13" fill="#FFD9B8" {W(2.6)}/>'
    f'<path d="M51 82 Q52 70 64 70 Q76 70 77 82 Q70 76 51 82Z" fill="#E3A23A" {W(2)}/>'
    f'<circle cx="49" cy="76" r="5" fill="#E3A23A" {W(2)}/><circle cx="79" cy="76" r="5" fill="#E3A23A" {W(2)}/>'
    + face(64, 86, d=5, k=0.5) + stars(((20, 30), (108, 40)), 4, "#FFFFFF"))

# 5. Студия керамики «Тис» (Апрелевка)
I["fun-keramika-tis-aprelevka"] = ("#E6F4EA", "#6FAF8A",
    "керамическая тарелка с синей росписью-рыбкой",
    "сушится на деревянной полке мастерской и подмигивает, рядом тисовая веточка с красной ягодкой",
    f'<rect x="0" y="96" width="128" height="10" fill="#B07A45" {W(2.6)}/>'
    f'<path d="M14 106 V126 M114 106 V126" {W(4)}/>'
    f'<circle cx="64" cy="58" r="40" fill="#FFFDF6" {W(3.2)}/><circle cx="64" cy="58" r="30" fill="none" stroke="#2F6FD0" stroke-width="2.4" stroke-dasharray="4 3"/>'
    f'<path d="M46 72 Q58 62 72 72 Q58 82 46 72Z M72 72 L82 66 V78Z" fill="#2F6FD0" {W(2)}/>'
    + eye(54, 52, 0.75) + f'<path d="M70 52 Q74 48 78 52" fill="none" {W(2.4)}/>'
    f'<path d="M58 62 Q64 66 70 62" fill="none" {W(2.2)}/>'
    f'<path d="M98 96 Q108 72 120 64" fill="none" stroke="#2E6B3E" stroke-width="3"/>'
    + "".join(f'<path d="M{x} {y} l7 -3" stroke="#3E8E52" stroke-width="3.4"/>' for x, y in ((102, 86), (106, 80), (110, 74), (114, 69)))
    + f'<circle cx="112" cy="88" r="4" fill="#E8434A" {W(1.8)}/>' + stars(((20, 24), (110, 22)), 3, "#FFFFFF"))

# 6. EffectQuest (Дмитров): приключенческие квесты
I["fun-effectquest-dmitrov"] = ("#E3F0D2", "#5E8C3A",
    "полевой бинокль цвета хаки с мордашкой на перемычке",
    "высматривает приключения из зарослей папоротника на краю тёмного леса",
    f'<path d="M0 30 L14 6 L28 30Z M100 34 L114 8 L128 34Z" fill="#2F5A2A"/>'
    f'<path d="M0 128 V96 Q20 80 36 98 Q50 78 64 96 Q80 78 94 98 Q110 80 128 96 V128Z" fill="#4C8A3A" {W(2.4)}/>'
    f'<rect x="20" y="44" width="34" height="46" rx="10" fill="#7A7A3A" {W(3)}/><rect x="74" y="44" width="34" height="46" rx="10" fill="#7A7A3A" {W(3)}/>'
    f'<rect x="50" y="52" width="28" height="18" rx="6" fill="#8E8E48" {W(2.8)}/>'
    f'<circle cx="37" cy="88" r="15" fill="#2C3A4A" {W(3)}/><circle cx="91" cy="88" r="15" fill="#2C3A4A" {W(3)}/>'
    f'<circle cx="32" cy="83" r="5" fill="#9FD3FF"/><circle cx="86" cy="83" r="5" fill="#9FD3FF"/>'
    + face(64, 58, d=6, k=0.55) +
    f'<path d="M20 102 Q30 96 40 104 M88 104 Q98 96 108 102" fill="none" stroke="#3B7A2E" stroke-width="4"/>'
    + stars(((60, 22),), 4, "#FFFFFF"))

# 9. Kisti ArtStudio (Нахабино): картины из смолы и жидкого стекла
I["fun-kisti-nakhabino"] = ("#E0F7F7", "#3BAFB5",
    "круглая доска с застывшей смолой-морем и белой пенной волной",
    "лежит на столе, а по её переливающейся глади плывёт крошечная золотая рыбка-блёстка",
    f'<ellipse cx="64" cy="108" rx="58" ry="14" fill="#C7A27A"/>'
    f'<circle cx="64" cy="64" r="46" fill="#F4E4C8" {W(3.2)}/>'
    f'<path d="M18 64 Q20 34 50 22 Q60 40 46 56 Q36 72 50 92 Q30 92 18 64Z" fill="#E8D2A8"/>'
    f'<path d="M50 22 Q86 14 106 44 Q112 64 100 94 Q80 112 50 104 Q40 96 50 92 Q66 80 58 64 Q50 44 62 34 Q58 28 50 22Z" fill="#1E8FB0"/>'
    f'<path d="M64 26 Q90 30 100 56" fill="none" stroke="#5CD0E8" stroke-width="6"/>'
    f'<path d="M50 92 Q66 80 58 64 Q50 44 62 34" fill="none" stroke="#FFFFFF" stroke-width="5" stroke-dasharray="6 3"/>'
    f'<circle cx="64" cy="64" r="46" fill="none" {W(3.2)}/>'
    + face(84, 72, d=7, k=0.65) +
    f'<path d="M72 46 Q78 42 84 46 Q78 50 72 46Z M84 46 L88 42 V50Z" fill="#FFC72C" {W(1.6)}/>'
    + stars(((40, 40), (96, 92)), 3, "#FFFFFF"))

# 11. Coddy (Нахабино): программирование для детей
I["fun-coddy-nakhabino"] = ("#E2E0FF", "#5A4FCF",
    "фиолетовый игровой геймпад с мордашкой между кнопками",
    "держит в ладошках-ручках маленький экран, на котором бежит строчка зелёного кода",
    f'<rect x="28" y="12" width="72" height="44" rx="6" fill="#1E1B3A" {W(3)}/>'
    + "".join(f'<path d="M36 {22+i*9} H{50+((i*13)%34)}" stroke="#5CE08A" stroke-width="3.4"/>' for i in range(4))
    + f'<path d="M86 22 H92" stroke="#FFD23F" stroke-width="3.4"/><rect x="58" y="49" width="3" height="5" fill="#5CE08A"/>'
    f'<path d="M14 92 Q10 64 34 64 H94 Q118 64 114 92 Q110 112 94 106 L84 96 H44 L34 106 Q18 112 14 92Z" fill="#7B5CE8" {W(3.2)}/>'
    f'<path d="M30 78 H44 M37 71 V85" stroke="#2A2150" stroke-width="5" stroke-linecap="round"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="{c}" {W(1.6)}/>' for x, y, c in ((90, 72, "#FFD23F"), (98, 80, "#E8434A"), (82, 80, "#4CB07A"), (90, 88, "#3F9BE8")))
    + face(64, 80, d=6, k=0.6) + f'<path d="M44 66 L50 56 M84 66 L78 56" {W(3)}/>')

# 12. Арт-зона (Внуково): художественная школа
I["fun-art-zona-vnukovo"] = ("#EAF4FF", "#7FB2E8",
    "толстый цветной карандаш с бумажными крылышками самолёта",
    "пролетает над пушистыми облаками и оставляет за собой красный нарисованный след-петлю",
    f'<ellipse cx="22" cy="100" rx="24" ry="12" fill="#FFFFFF"/><ellipse cx="104" cy="108" rx="30" ry="12" fill="#FFFFFF"/>'
    f'<path d="M10 70 Q24 40 40 66 Q52 88 40 76" fill="none" stroke="#E8434A" stroke-width="4" stroke-linecap="round"/>'
    f'<g transform="rotate(-18 72 60)">'
    f'<path d="M38 50 H96 L114 60 L96 70 H38Z" fill="#E8434A" {W(3)}/>'
    f'<path d="M96 50 L114 60 L96 70Z" fill="#F7D9A8" {W(2.6)}/><path d="M108 57 L114 60 L108 63Z" fill="#E8434A"/>'
    f'<rect x="30" y="50" width="10" height="20" fill="#C9D2DE" {W(2.4)}/>'
    f'<path d="M56 50 L48 30 H64 L72 50Z M56 70 L48 90 H64 L72 70Z" fill="#FFFFFF" {W(2.4)}/>'
    + face(82, 60, d=5, k=0.5) + '</g>' + stars(((100, 22), (26, 22)), 3, "#FFFFFF"))

# 13. Эль Квест (Электросталь, ул. Николаева): мистические квесты
I["fun-el-quest-nikolaeva"] = ("#4A3A6E", "#1C1530",
    "бронзовый канделябр на три свечи с мордашкой на подставке",
    "освещает тёмный чердак с паутиной в углу и старым портретом",
    f'<path d="M0 0 L36 0 Q24 10 0 30Z" fill="none" stroke="#9A8CC0" stroke-width="1.2"/>'
    f'<path d="M0 12 Q14 10 20 0 M0 22 Q24 18 30 0" fill="none" stroke="#9A8CC0" stroke-width="1.2"/>'
    f'<rect x="92" y="20" width="28" height="36" fill="#6E5A3A" {W(2.6)}/><rect x="97" y="25" width="18" height="26" fill="#2E2440"/>'
    f'<circle cx="106" cy="34" r="5" fill="#8C7A9E"/>'
    f'<ellipse cx="60" cy="40" rx="50" ry="40" fill="#FFD27A" opacity=".18"/>'
    f'<path d="M30 56 Q30 72 60 72 Q90 72 90 56" fill="none" stroke="#C98A3A" stroke-width="5"/>'
    f'<path d="M60 52 V104" stroke="#C98A3A" stroke-width="7"/>'
    f'<path d="M40 112 Q60 96 80 112Z" fill="#C98A3A" {W(3)}/>'
    + "".join(f'<rect x="{x-5}" y="{y}" width="10" height="20" rx="2" fill="#FFF6E0" {W(2.2)}/><path d="M{x} {y-12} Q{x-6} {y-4} {x} {y} Q{x+6} {y-4} {x} {y-12}Z" fill="#FFB020" {W(1.6)}/>'
              for x, y in ((30, 38), (60, 32), (90, 38)))
    + f'<circle cx="60" cy="88" r="13" fill="#D9A050" {W(2.6)}/>' + face(60, 87, d=5, k=0.5))

# 14. Эль Квест (Электросталь, Юбилейная ул.): квесты про волшебников
I["fun-el-quest-yubileynaya"] = ("#F0E6D2", "#8A6A3E",
    "толстая старинная книга заклинаний с медной застёжкой",
    "сама парит над школьной партой волшебников и выпускает из страниц стайку светлячков",
    f'<rect x="10" y="104" width="108" height="10" fill="#7A4E2A" {W(2.6)}/><path d="M20 114 V128 M108 114 V128" {W(4)}/>'
    f'<ellipse cx="64" cy="100" rx="30" ry="4" fill="#5A3A1E" opacity=".35"/>'
    f'<path d="M24 48 L64 40 L104 48 V86 L64 78 L24 86Z" fill="#7B2D3A" {W(3.2)}/>'
    f'<path d="M30 44 L64 36 V76 L30 82Z" fill="#FFF6DE" {W(2.6)}/><path d="M98 44 L64 36 V76 L98 82Z" fill="#FFF6DE" {W(2.6)}/>'
    f'<rect x="58" y="56" width="12" height="14" rx="3" fill="#D9963A" {W(2.2)}/>'
    + face(64, 52, d=14, k=0.6, mouth=False) + f'<path d="M58 70 Q64 74 70 70" fill="none" {W(2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#FFF27A"/><circle cx="{x}" cy="{y}" r="6" fill="#FFF27A" opacity=".35"/>' for x, y in ((50, 22), (66, 14), (82, 24), (40, 32), (92, 34))))

# 15. Аркидс Парк (Подольск): квесты для детей
I["fun-arkids-podolsk"] = ("#DFFFF0", "#2EBF8A",
    "большая красная грибовидная кнопка квест-комнаты на жёлтом пульте с полосками",
    "мальчик в кепке обеими ладонями давит на неё, и над пультом загорается зелёная лампочка «Решено!»",
    f'<path d="M14 128 L22 82 H106 L114 128Z" fill="#FFD23F" {W(3.2)}/>'
    + "".join(f'<path d="M{30+i*16} 128 L{38+i*16} 82" stroke="#2B2B2B" stroke-width="6"/>' for i in range(5))
    + f'<path d="M14 128 L22 82 H106 L114 128Z" fill="none" {W(3.2)}/>'
    f'<rect x="40" y="70" width="48" height="14" rx="4" fill="#9AA4B0" {W(2.6)}/>'
    f'<path d="M30 72 Q30 40 64 40 Q98 40 98 72Z" fill="#E8434A" {W(3.2)}/>'
    f'<path d="M42 54 Q50 46 60 46" fill="none" stroke="#FF9A9A" stroke-width="4"/>'
    + face(64, 60, d=9, k=0.7) +
    f'<circle cx="104" cy="22" r="10" fill="#5CE08A" {W(2.6)}/><path d="M104 32 V40" {W(3)}/>'
    + "".join(f'<path d="M{104+dx} {22+dy} l{dx*0.6:.0f} {dy*0.6:.0f}" stroke="#5CE08A" stroke-width="3"/>' for dx, dy in ((14, 0), (-14, 0), (0, -14), (10, -10), (-10, -10)))
    + f'<circle cx="34" cy="22" r="11" fill="#FFD9B8" {W(2.4)}/><path d="M22 20 Q24 8 36 9 Q46 10 46 20Z" fill="#2E7FC0" {W(2)}/><path d="M44 18 H54" stroke="#2E7FC0" stroke-width="4"/>'
    + face(34, 24, d=4, k=0.38) +
    f'<path d="M28 33 Q32 40 40 44 M42 31 Q50 36 52 44" fill="none" stroke="#FFD9B8" stroke-width="6"/>'
    f'<path d="M28 33 Q32 40 40 44 M42 31 Q50 36 52 44" fill="none" {W(1.4)}/>')

# 16. Artplace (Старокрымская): живопись и бисер для детей
I["fun-artplace-starokrymskaya"] = ("#FFF4E8", "#E9A06B",
    "длинная нитка разноцветного бисера на леске с иголкой на конце",
    "свивается в радостную петлю-сердечко над блюдцем с рассыпанными бусинками",
    f'<ellipse cx="64" cy="108" rx="42" ry="12" fill="#FFFFFF" {W(3)}/><ellipse cx="64" cy="106" rx="30" ry="7" fill="#F4ECF6"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3.2" fill="{c}" {W(1.2)}/>' for x, y, c in ((50, 106, "#E8434A"), (60, 104, "#3F9BE8"), (72, 107, "#FFD23F"), (80, 104, "#4CB07A")))
    + "".join(f'<circle cx="{x}" cy="{y}" r="5.4" fill="{c}" {W(1.8)}/>' for (x, y), c in zip(
        ((64, 84), (56, 76), (46, 68), (36, 58), (32, 46), (36, 34), (46, 28), (56, 32), (64, 42), (72, 32), (82, 28), (92, 34), (96, 46), (92, 58), (84, 68)),
        ("#E8434A", "#FF8A2A", "#FFD23F", "#4CB07A", "#3F9BE8", "#7B5CE8", "#FF7FA8", "#E8434A", "#FF8A2A", "#FFD23F", "#4CB07A", "#3F9BE8", "#7B5CE8", "#FF7FA8", "#E8434A")))
    + f'<path d="M84 68 Q96 74 104 84" fill="none" stroke="#8C8C9C" stroke-width="1.6"/>'
    f'<path d="M102 80 L114 98" stroke="#B8C4CF" stroke-width="3"/><ellipse cx="103" cy="81" rx="1.4" ry="2.6" fill="#FFF4E8"/>'
    + face(64, 54, d=7, k=0.65))

# 18. Артмоссфера (ул. Грина): рисование, керамика, история искусств
I["fun-artmossfera-grina"] = ("#FDEBD8", "#C9672F",
    "древнегреческая амфора с чернофигурной росписью-ёжиком",
    "стоит на мраморной колонне, удивлённо держится ручками за бока и рассматривает свою роспись",
    f'<rect x="38" y="96" width="52" height="32" fill="#F2EEE8" {W(3)}/>'
    + "".join(f'<path d="M{x} 100 V128" stroke="#C9C2B8" stroke-width="2"/>' for x in (48, 58, 70, 80))
    + f'<rect x="32" y="90" width="64" height="8" fill="#FFFFFF" {W(2.6)}/>'
    f'<path d="M54 90 Q36 70 42 48 Q46 34 54 28 V18 H74 V28 Q82 34 86 48 Q92 70 74 90Z" fill="#E07A3A" {W(3.2)}/>'
    f'<path d="M54 30 Q38 30 40 46 Q42 54 48 52 M74 30 Q90 30 88 46 Q86 54 80 52" fill="none" {W(3)}/>'
    f'<rect x="50" y="14" width="28" height="6" rx="2" fill="#E07A3A" {W(2.4)}/>'
    f'<path d="M48 70 Q54 60 64 62 Q76 62 80 70 Q70 76 56 74Z" fill="#2A1A10"/>'
    + "".join(f'<path d="M{x} {y} l-2 -6" stroke="#2A1A10" stroke-width="2"/>' for x, y in ((54, 64), (60, 61), (66, 61), (72, 62)))
    + eye(58, 46, 0.6) + eye(70, 46, 0.6) + f'<ellipse cx="64" cy="54" rx="3" ry="3.4" fill="{O}"/>'
    + stars(((20, 24), (106, 30)), 4, "#FFFFFF"))

# 19. Студия живописи Коневой (Краснознаменск): масляная живопись
I["fun-koneva-krasnoznamensk"] = ("#E8F0FF", "#4A6FC0",
    "натянутый холст на подрамнике с мордашкой и свежим подсолнухом маслом",
    "стоит на подоконнике в лучах солнца и любуется, как с него стекает капелька жёлтой краски",
    f'<rect x="0" y="100" width="128" height="10" fill="#FFFFFF" {W(2.6)}/>'
    f'<path d="M0 0 L40 0 L0 40Z" fill="#FFF3B0" opacity=".6"/>'
    f'<rect x="22" y="14" width="84" height="86" fill="#FFFDF4" {W(3.4)}/>'
    f'<rect x="22" y="14" width="84" height="86" fill="none" stroke="#B07A45" stroke-width="2" transform="translate(4 4)"/>'
    + "".join(f'<ellipse cx="{64+16*__import__("math").cos(a/8*6.2832):.1f}" cy="{52+16*__import__("math").sin(a/8*6.2832):.1f}" rx="9" ry="5" fill="#FFC72C" {W(1.6)} transform="rotate({a*45} {64+16*__import__("math").cos(a/8*6.2832):.1f} {52+16*__import__("math").sin(a/8*6.2832):.1f})"/>' for a in range(8))
    + f'<circle cx="64" cy="52" r="11" fill="#6B3A1E" {W(2.2)}/>'
    f'<path d="M64 64 V96" stroke="#3E8E52" stroke-width="4"/><path d="M64 82 Q52 74 46 82 Q56 88 64 82Z" fill="#4CB07A" {W(1.6)}/>'
    + face(64, 52, d=4, k=0.38, blush=False) +
    f'<path d="M86 66 Q88 78 86 86" stroke="#FFC72C" stroke-width="3"/><path d="M86 86 Q82 92 86 95 Q90 92 86 86Z" fill="#FFC72C" {W(1.4)}/>')

if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
