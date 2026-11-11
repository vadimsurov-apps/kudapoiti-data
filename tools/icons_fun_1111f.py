"""Иконки робота fun (2026-11-11, проход f): места из tools/add_fun_1111f.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя палитра фона.
Запуск: python3 tools/icons_fun_1111f.py [id ...]"""
import os, sys, math
from draw_icons import s, face, sparkle, eye, O
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}


def stars(pts, r=3, c="#fff"):
    return "".join(sparkle(x, y, r, c) for x, y in pts)


# 1. Триквестр (Войковская): квест «Дом великана»
I["fun-trikvestr-voykovskaya"] = ("#E8F7D8", "#7BBF5A",
    "огромный стоптанный башмак великана с дверцей-входом и круглыми окошками",
    "стоит на зелёном лугу как домик, а из окошка выглядывает маленький искатель с фонариком",
    f'<path d="M0 104 Q64 92 128 104 V128 H0Z" fill="#5FA845" {W(2.4)}/>'
    f'<path d="M22 104 V58 Q22 40 40 40 H62 Q72 40 72 52 V70 Q96 66 108 82 Q114 94 110 104Z" fill="#9A5A2E" {W(3.2)}/>'
    f'<path d="M20 104 H112" {W(4)}/>'
    f'<path d="M30 40 Q46 30 64 40" fill="none" {W(2.6)}/>'
    f'<path d="M50 48 L62 54 M48 56 L62 62 M50 64 L64 68" {W(2.2)}/>'
    f'<path d="M36 104 V84 Q42 76 50 84 V104Z" fill="#F2C14E" {W(2.6)}/><circle cx="46" cy="94" r="1.6" fill="{O}"/>'
    f'<circle cx="90" cy="86" r="8" fill="#FFF3B0" {W(2.4)}/>'
    f'<circle cx="90" cy="87" r="4.6" fill="#FFD9B8" {W(1.6)}/>' + eye(88.4, 87, 0.32) + eye(91.6, 87, 0.32) +
    f'<path d="M96 80 L118 70 L118 86Z" fill="#FFF7C2" opacity=".7"/>'
    f'<circle cx="34" cy="60" r="6" fill="#FFF3B0" {W(2.2)}/>'
    + face(48, 74, d=0, k=0, mouth=False, blush=False)
    + stars(((100, 24), (20, 22), (112, 46)), 3.4, "#FFFFFF"))

# 2. Учёный кот (Отрадное): центр развития
I["fun-uchenyy-kot-otradnoe"] = ("#EDE6FF", "#9C86E8",
    "серый котёнок в квадратной шапке выпускника с жёлтой кисточкой",
    "сидит на стопке из трёх цветных книжек и держит в лапке деревянную указку",
    f'<rect x="30" y="98" width="68" height="12" rx="3" fill="#E8434A" {W(2.6)}/>'
    f'<rect x="34" y="86" width="60" height="12" rx="3" fill="#3F8FE8" {W(2.6)}/>'
    f'<rect x="28" y="74" width="66" height="12" rx="3" fill="#FFC72C" {W(2.6)}/>'
    f'<path d="M86 80 H92 M86 92 H90 M90 104 H96" stroke="#FFFFFF" stroke-width="2"/>'
    f'<path d="M78 72 Q96 66 92 50" fill="none" stroke="#9AA3B5" stroke-width="5"/>'
    f'<ellipse cx="60" cy="62" rx="20" ry="14" fill="#A8ADBF" {W(3)}/>'
    f'<circle cx="60" cy="42" r="18" fill="#A8ADBF" {W(3)}/>'
    f'<path d="M44 34 L42 16 L54 26Z M76 34 L78 16 L66 26Z" fill="#A8ADBF" {W(2.6)}/>'
    + face(60, 44, d=7, k=0.75) +
    f'<path d="M50 50 H40 M50 52 L41 56 M70 50 H80 M70 52 L79 56" stroke="{O}" stroke-width="1.4"/>'
    f'<path d="M36 22 L60 12 L84 22 L60 32Z" fill="#2B2B3A" {W(2.4)}/>'
    f'<path d="M84 22 V36" stroke="#FFD23F" stroke-width="2.6"/><circle cx="84" cy="38" r="3" fill="#FFD23F"/>'
    f'<path d="M80 64 L104 40" stroke="#B5763A" stroke-width="4"/><circle cx="80" cy="64" r="5" fill="#A8ADBF" {W(2.2)}/>'
    + stars(((18, 40), (110, 74), (106, 22)), 3.4, "#FFFFFF"))

# 3. Exotag Арена (Ленинский пр.): лазертаг
I["fun-exotag-arena-leninsky"] = ("#3A2C6E", "#140E33",
    "оранжевый лазертаг-бластер с круглым прицелом и мордашкой на корпусе",
    "выглядывает из-за неонового бетонного блока-укрытия и пускает тонкий красный луч в круглую мишень",
    f'<rect x="0" y="96" width="128" height="32" fill="#22194A"/>'
    f'<path d="M0 100 H128" stroke="#38E0FF" stroke-width="2" opacity=".7"/>'
    f'<circle cx="104" cy="44" r="14" fill="#FFFFFF" {W(2.6)}/><circle cx="104" cy="44" r="9" fill="#FF4B6E"/>'
    f'<circle cx="104" cy="44" r="4" fill="#FFFFFF"/>'
    f'<path d="M90 50 L100 46" stroke="#FF2E4D" stroke-width="3"/>'
    f'<path d="M72 46 H86 V56 H72Z" fill="#5A5878" {W(2.6)}/><circle cx="88" cy="51" r="3.4" fill="#FF2E4D" {W(1.6)}/>'
    f'<path d="M16 40 H66 Q74 40 74 48 V56 Q74 64 66 64 H16 Q10 64 10 56 V48 Q10 40 16 40Z" fill="#FF8A1F" {W(3)}/>'
    f'<rect x="28" y="30" width="22" height="10" rx="5" fill="#2B2B3A" {W(2)}/><circle cx="50" cy="35" r="3" fill="#38E0FF"/>'
    f'<path d="M24 64 L20 80 H32 L36 64Z" fill="#E86E10" {W(2.6)}/>'
    + face(42, 52, d=7, k=0.6) +
    f'<rect x="8" y="74" width="64" height="30" rx="4" fill="#5A5878" {W(3)}/>'
    f'<path d="M8 80 H72" stroke="#B45CFF" stroke-width="3"/><path d="M8 94 H72" stroke="#38E0FF" stroke-width="3"/>'
    + stars(((90, 18), (60, 22), (118, 76)), 3, "#B9F2FF"))

# 4. Хобби Клевер (Отрадное): рукоделие для детей
I["fun-hobbi-klever-otradnoe"] = ("#FFF0D9", "#F0A860",
    "полосатый вязаный шарфик-змейка с помпонами на концах",
    "сидит в плетёной корзинке с клубками и сам довязывает свой хвостик спицами",
    f'<path d="M24 92 H104 L96 118 H32Z" fill="#C98E3E" {W(3)}/>'
    f'<path d="M30 100 H98 M28 108 H100" stroke="#A86F2A" stroke-width="2.4"/>'
    f'<circle cx="38" cy="90" r="10" fill="#4CB07A" {W(2.4)}/><circle cx="92" cy="90" r="10" fill="#3F8FE8" {W(2.4)}/>'
    f'<path d="M32 86 Q38 92 44 86 M86 86 Q92 92 98 86" fill="none" stroke="#FFFFFF" stroke-width="1.6"/>'
    f'<path d="M62 92 Q50 74 62 60 Q74 46 62 30" fill="none" stroke="{O}" stroke-width="20" stroke-linecap="round"/>'
    f'<path d="M62 92 Q50 74 62 60 Q74 46 62 30" fill="none" stroke="#E8434A" stroke-width="15" stroke-linecap="round"/>'
    f'<path d="M62 92 Q50 74 62 60 Q74 46 62 30" fill="none" stroke="#FFD23F" stroke-width="15" stroke-dasharray="7 7" stroke-linecap="butt"/>'
    + face(62, 30, d=5, k=0.55) +
    f'<circle cx="62" cy="15" r="6" fill="#FF7FA8" {W(2)}/>'
    f'<path d="M74 70 L104 46 M78 76 L110 58" stroke="#B5763A" stroke-width="3.4"/>'
    f'<circle cx="104" cy="46" r="3" fill="#FFD23F" {W(1.4)}/><circle cx="110" cy="58" r="3" fill="#FFD23F" {W(1.4)}/>'
    + stars(((20, 30), (102, 22)), 3.4, "#FFFFFF"))

# 5. Время рисовать (Филёвский парк): уроки рисования
I["fun-vremya-risovat-filevsky"] = ("#E2F5FF", "#7AC4EE",
    "круглые настенные часы, у которых часовая и минутная стрелки — две кисточки",
    "висят над деревянным мольбертом и стрелками-кисточками рисуют на холсте радугу",
    f'<path d="M40 128 L52 70 M88 128 L76 70 M64 70 V128" stroke="#B5763A" stroke-width="5"/>'
    f'<rect x="34" y="70" width="60" height="42" rx="3" fill="#FFFFFF" {W(3)}/>'
    + "".join(f'<path d="M42 104 Q64 {80+i*5} 86 104" fill="none" stroke="{c}" stroke-width="3.6"/>'
              for i, c in enumerate(("#E8434A", "#FF9F1C", "#FFD23F", "#4CB07A", "#3F8FE8")))
    + f'<circle cx="64" cy="36" r="26" fill="#FFFDF5" {W(3.4)}/>'
    + "".join(f'<path d="M{64+20*math.sin(math.radians(a)):.1f} {36-20*math.cos(math.radians(a)):.1f} L{64+23*math.sin(math.radians(a)):.1f} {36-23*math.cos(math.radians(a)):.1f}" {W(2.4)}/>' for a in range(0, 360, 30))
    + f'<path d="M64 36 L50 54" stroke="#B5763A" stroke-width="3"/><path d="M48 52 Q44 60 50 58 Q54 56 52 52Z" fill="#E8434A" {W(1.6)}/>'
    f'<path d="M64 36 L82 50" stroke="#B5763A" stroke-width="3"/><path d="M80 50 Q86 58 88 52 Q86 48 82 48Z" fill="#3F8FE8" {W(1.6)}/>'
    f'<circle cx="64" cy="36" r="3" fill="{O}"/>'
    + face(64, 26, d=7, k=0.5, mouth=False) +
    f'<path d="M60 31 Q64 33.5 68 31" fill="none" {W(1.6)}/>'
    + stars(((16, 30), (112, 26), (110, 60)), 3.4, "#FFFFFF"))

# 6. Art фабрика (Таганка): рисование
I["fun-art-fabrika-taganka"] = ("#F3E3FF", "#B57EE6",
    "три баночки акриловой краски-тройняшки: красная, жёлтая и синяя",
    "стоят на деревянной палитре и выливают краску в общий радужный водоворот",
    f'<path d="M12 98 Q8 76 34 72 H100 Q124 74 118 96 Q112 116 74 116 H44 Q16 116 12 98Z" fill="#E8C08A" {W(3)}/>'
    f'<ellipse cx="34" cy="100" rx="7" ry="5" fill="#F3E3FF" {W(2.4)}/>'
    f'<path d="M58 100 Q64 88 78 94 Q90 102 78 108 Q64 112 62 102 Q64 96 72 99" fill="none" stroke="#E8434A" stroke-width="5"/>'
    f'<path d="M58 100 Q64 88 78 94 Q90 102 78 108" fill="none" stroke="#FFD23F" stroke-width="2.4" stroke-dasharray="5 4"/>'
    f'<path d="M66 96 Q74 94 76 102" fill="none" stroke="#3F8FE8" stroke-width="3"/>'
    + "".join(
        f'<path d="M{x-11} {y} H{x+11} V{y+24} Q{x+11} {y+28} {x+7} {y+28} H{x-7} Q{x-11} {y+28} {x-11} {y+24}Z" fill="#FFFFFF" {W(2.8)}/>'
        f'<path d="M{x-11} {y+6} H{x+11} V{y+18} H{x-11}Z" fill="{c}"/>'
        f'<rect x="{x-12}" y="{y-6}" width="24" height="7" rx="2" fill="{c}" {W(2.4)}/>'
        f'<path d="M{x+(4 if x < 64 else -4 if x > 64 else 0)} {y+28} Q{x+(10 if x < 64 else -10 if x > 64 else 0)} {y+38} {66} 98" fill="none" stroke="{c}" stroke-width="4"/>'
        + face(x, y + 12, d=4, k=0.38)
        for x, y, c in ((32, 34, "#E8434A"), (64, 26, "#FFC72C"), (96, 34, "#3F8FE8")))
    + stars(((16, 30), (112, 24)), 3.4, "#FFFFFF"))

# 7. Детский технопарк МАИ «Траектория взлёта» (Войковская)
I["fun-traektoriya-vzleta-mai"] = ("#DDF0FF", "#5B9FE0",
    "серебристый пассажирский лайнер-модель с синей полосой и мордашкой в кабине",
    "взлетает с детской учебной парты по пунктирной дуге-траектории прямо в облака",
    f'<ellipse cx="96" cy="30" rx="18" ry="8" fill="#FFFFFF"/><ellipse cx="108" cy="24" rx="10" ry="7" fill="#FFFFFF"/>'
    f'<rect x="8" y="98" width="58" height="8" rx="2" fill="#E8B26A" {W(2.8)}/>'
    f'<path d="M14 106 V126 M60 106 V126" {W(4)}/>'
    f'<path d="M26 98 Q46 70 74 58" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-dasharray="5 5"/>'
    f'<g transform="rotate(-24 82 52)">'
    f'<path d="M54 52 Q54 44 64 44 H104 Q116 44 118 52 Q116 60 104 60 H64 Q54 60 54 52Z" fill="#DDE3EE" {W(3)}/>'
    f'<path d="M58 54 H112" stroke="#3F6FD0" stroke-width="3"/>'
    f'<path d="M78 58 L70 76 H80 L92 58Z" fill="#C3CAD8" {W(2.6)}/>'
    f'<path d="M78 46 L74 34 H82 L90 46Z" fill="#C3CAD8" {W(2.4)}/>'
    f'<path d="M56 46 L50 34 H58 L64 44Z" fill="#E8434A" {W(2.4)}/>'
    + face(106, 50, d=3.6, k=0.34, blush=False) +
    f'</g>'
    + stars(((18, 28), (44, 20), (114, 92)), 3.4, "#FFFFFF"))

# 8. Детский кружок «Туки-туки» (Северное Бутово): столярный кружок
I["fun-tuki-tuki-kulikovskaya"] = ("#FFF4D6", "#E9B44C",
    "свежесобранная деревянная табуретка-малышка с мордашкой на сиденье",
    "гордо стоит на столярном верстаке среди кудрявых стружек и рассыпанных гвоздиков",
    f'<rect x="6" y="94" width="116" height="12" rx="2" fill="#B5763A" {W(3)}/>'
    f'<path d="M16 106 V128 M112 106 V128" {W(5)}/>'
    f'<path d="M40 92 L46 66 M88 92 L82 66 M58 92 L60 66 M70 92 L68 66" stroke="{O}" stroke-width="9"/>'
    f'<path d="M40 92 L46 66 M88 92 L82 66 M58 92 L60 66 M70 92 L68 66" stroke="#F2C27A" stroke-width="5"/>'
    f'<path d="M44 80 H84" stroke="{O}" stroke-width="7"/><path d="M44 80 H84" stroke="#E8A95A" stroke-width="3"/>'
    f'<rect x="30" y="52" width="68" height="16" rx="6" fill="#F2C27A" {W(3)}/>'
    f'<path d="M36 58 Q52 56 68 60 Q80 62 92 58" fill="none" stroke="#C98E3E" stroke-width="1.8"/>'
    + face(64, 58, d=8, k=0.55) +
    "".join(f'<path d="M{x} {y} q4 -6 8 0 q4 6 8 0" fill="none" stroke="#E8A95A" stroke-width="2.6"/>' for x, y in ((12, 90), (100, 88), (18, 84)))
    + "".join(f'<path d="M{x} {y} L{x+8} {y-3}" stroke="#7A8090" stroke-width="2.4"/><circle cx="{x}" cy="{y}" r="2" fill="#7A8090"/>'
              for x, y in ((100, 98), (26, 100)))
    + stars(((20, 30), (108, 30), (64, 22)), 3.4, "#FFFFFF"))

# 9. Химико-биологическая школа «Бион» (Борисово)
I["fun-bion-borisovo"] = ("#E0FFF0", "#55C79A",
    "стеклянная пипетка с красной резиновой грушей-шапочкой",
    "капает зелёную каплю в чашку Петри, где колония микробов сложилась в улыбку",
    f'<ellipse cx="64" cy="104" rx="42" ry="12" fill="#D8F3FF" {W(3)}/>'
    f'<ellipse cx="64" cy="100" rx="38" ry="9" fill="#F4FFF8" {W(2.2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#9BD84A" {W(1.4)}/>' for x, y, r in
              ((44, 100, 3.4), (52, 104, 3), (62, 106, 3.4), (72, 104, 3), (80, 100, 3.4), (52, 96, 2.6), (74, 96, 2.6)))
    + f'<path d="M64 84 Q60 78 64 72 Q68 78 64 84Z" fill="#6FD34A" {W(1.8)}/>'
    f'<path d="M56 64 L60 18 H68 L72 64 L64 72Z" fill="#EAF8FF" {W(3)}/>'
    f'<path d="M58 44 L60 18 H68 L70 44Z" fill="#BFE8D0" opacity=".7"/>'
    f'<rect x="54" y="6" width="20" height="16" rx="7" fill="#E8434A" {W(2.8)}/>'
    + face(64, 40, d=5, k=0.5) +
    f'<path d="M62 54 H66 M61 60 H67" stroke="#9AA3B5" stroke-width="1.6"/>'
    + stars(((22, 30), (106, 34), (104, 70)), 3.4, "#FFFFFF"))

# 10. Сад Бабочек (Арбат)
I["fun-sad-babochek-arbat"] = ("#E6FFE8", "#4FB86A",
    "синяя тропическая бабочка морфо с переливающимися крыльями и мордашкой",
    "сидит на дольке апельсина среди листьев оранжереи и пьёт сок хоботком",
    f'<path d="M0 30 Q24 40 20 70 Q10 56 0 54Z" fill="#2E8F4E" {W(2.4)}/>'
    f'<path d="M128 70 Q100 74 102 104 Q116 92 128 94Z" fill="#2E8F4E" {W(2.4)}/>'
    f'<path d="M24 112 Q64 70 104 112Z" fill="#FFA62B" {W(3)}/>'
    f'<path d="M32 110 Q64 80 96 110" fill="none" stroke="#FFD27A" stroke-width="3"/>'
    + "".join(f'<path d="M64 108 L{64+28*math.cos(math.radians(a)):.1f} {108-28*math.sin(math.radians(a)):.1f}" stroke="#FFD27A" stroke-width="2"/>' for a in (45, 90, 135))
    + f'<path d="M62 56 Q36 18 18 34 Q10 58 40 66 Q24 78 34 90 Q48 92 62 70Z" fill="#2F7BFF" {W(3)}/>'
    f'<path d="M66 56 Q92 18 110 34 Q118 58 88 66 Q104 78 94 90 Q80 92 66 70Z" fill="#2F7BFF" {W(3)}/>'
    f'<path d="M58 54 Q38 30 26 40 Q24 54 44 60Z M70 54 Q90 30 102 40 Q104 54 84 60Z" fill="#7FD0FF" opacity=".8"/>'
    f'<ellipse cx="64" cy="66" rx="6" ry="20" fill="#2B2B3A" {W(2)}/>'
    f'<circle cx="64" cy="44" r="9" fill="#2B2B3A" {W(2)}/>'
    + eye(60.5, 44, 0.45) + eye(67.5, 44, 0.45) +
    f'<path d="M60 36 Q54 24 48 24 M68 36 Q74 24 80 24" fill="none" {W(1.8)}/>'
    f'<path d="M64 52 Q70 70 66 86" fill="none" stroke="#FFFFFF" stroke-width="1.4"/>'
    + stars(((106, 18), (22, 92)), 3.4, "#FFFFFF"))

# 11. Школа рисования «Баня» (Вавиловская)
I["fun-shkola-banya-leninsky"] = ("#FFEFE3", "#E88B5A",
    "деревянная банная шайка с ручкой, полная красок вместо воды",
    "в ней с удовольствием моется кисточка, пуская разноцветную мыльную пену",
    f'<path d="M22 70 H106 L98 112 Q96 118 88 118 H40 Q32 118 30 112Z" fill="#D9A15E" {W(3.2)}/>'
    f'<path d="M40 70 L44 118 M64 70 V118 M88 70 L84 118" stroke="#B5763A" stroke-width="2.4"/>'
    f'<path d="M26 84 H102 M28 102 H100" stroke="#7A8090" stroke-width="4"/>'
    f'<rect x="96" y="58" width="22" height="10" rx="4" fill="#C98E3E" {W(2.6)}/>'
    f'<ellipse cx="64" cy="70" rx="42" ry="8" fill="#FF6FA3" {W(2.6)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" {W(2)}/>' for x, y, r, c in
              ((34, 62, 8, "#FFD23F"), (48, 56, 9, "#7FD0FF"), (82, 58, 8, "#9BE36A"), (96, 62, 6, "#C9A2FF"), (26, 44, 5, "#FFFFFF"), (100, 40, 4, "#FFFFFF")))
    + f'<path d="M58 66 L70 22" stroke="{O}" stroke-width="10" stroke-linecap="round"/>'
    f'<path d="M58 66 L70 22" stroke="#E8434A" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M68 30 L72 16" stroke="#C0C6D2" stroke-width="7"/>'
    f'<path d="M70 18 Q76 4 80 12 Q78 8 74 10 Q70 6 68 14Z" fill="#3B3355"/>'
    + face(64, 44, d=4.6, k=0.42) +
    stars(((18, 24), (110, 22)), 3.4, "#FFFFFF"))

# 12. Экоцентр «Лосиный остров» — «Красная сосна»
I["fun-ekocentr-krasnaya-sosna"] = ("#E9F6FF", "#7FB4D8",
    "рыжий ствол сосны с мордашкой в коре и пушистой зелёной шапкой-кроной",
    "держит в ветке-руке лупу и рассматривает муравья на другой ветке",
    f'<path d="M0 112 Q64 100 128 112 V128 H0Z" fill="#8CC66A" {W(2.4)}/>'
    f'<path d="M50 112 L54 46 H74 L78 112Z" fill="#D9743A" {W(3.2)}/>'
    f'<path d="M58 60 L62 66 M68 80 L64 86 M56 94 L60 100 M70 100 L66 106" stroke="#A9512A" stroke-width="2.2"/>'
    f'<path d="M24 52 Q20 30 42 30 Q46 12 64 14 Q84 12 88 30 Q110 30 104 52 Q96 60 64 56 Q32 60 24 52Z" fill="#2E8F4E" {W(3)}/>'
    f'<path d="M36 44 L42 38 M58 26 L64 20 M84 40 L90 34" stroke="#5FC27A" stroke-width="2.4"/>'
    + face(64, 72, d=6, k=0.55) +
    f'<path d="M76 84 Q92 84 98 72" fill="none" stroke="#D9743A" stroke-width="5"/>'
    f'<circle cx="102" cy="66" r="9" fill="#DFF4FF" {W(2.6)}/><path d="M96 72 L90 78" {W(3)}/>'
    f'<path d="M52 88 Q36 90 26 84" fill="none" stroke="#D9743A" stroke-width="5"/>'
    f'<ellipse cx="24" cy="80" rx="3" ry="2.2" fill="#2B2B3A"/><circle cx="20" cy="79" r="2" fill="#2B2B3A"/><circle cx="28" cy="80" r="2.4" fill="#2B2B3A"/>'
    f'<path d="M22 82 L20 86 M25 82 L25 86 M28 82 L30 86" stroke="#2B2B3A" stroke-width="1"/>'
    + stars(((18, 22), (112, 24)), 3.4, "#FFFFFF"))

# 13. Гончарная «Гуси Лепят» (Южное Бутово)
I["fun-gusi-lepyat-yuzhnobutovskaya"] = ("#FFF3E8", "#E3A27A",
    "серый пушистый гусёнок в глиняном коричневом фартуке",
    "крутит лапкой гончарный круг и вытягивает клювом горлышко кувшина",
    f'<rect x="60" y="100" width="58" height="10" rx="5" fill="#7A8090" {W(2.8)}/>'
    f'<path d="M89 110 V126" {W(5)}/>'
    f'<path d="M74 100 Q70 84 80 76 Q84 70 82 62 H96 Q94 70 98 76 Q108 84 104 100Z" fill="#C97B4A" {W(3)}/>'
    f'<ellipse cx="89" cy="62" rx="8" ry="2.6" fill="#A9603A" {W(2)}/>'
    f'<path d="M80 86 Q89 90 100 86" fill="none" stroke="#A9603A" stroke-width="2"/>'
    f'<ellipse cx="42" cy="88" rx="28" ry="24" fill="#B9BCC8" {W(3)}/>'
    f'<path d="M18 84 Q8 78 12 70 Q20 76 22 80Z" fill="#B9BCC8" {W(2.4)}/>'
    f'<path d="M30 76 Q42 82 56 76 L58 106 Q42 112 26 106Z" fill="#8A5A3A" {W(2.6)}/>'
    f'<circle cx="48" cy="52" r="18" fill="#B9BCC8" {W(3)}/>'
    + eye(43, 50, 0.7) + eye(54, 50, 0.7) +
    f'<ellipse cx="38" cy="58" rx="3.6" ry="2.2" fill="#FF7FA8" opacity=".6"/>'
    f'<path d="M60 54 Q72 54 76 60 Q70 64 60 62Z" fill="#FF9F1C" {W(2.2)}/>'
    f'<path d="M58 88 Q70 86 76 90" fill="none" stroke="{O}" stroke-width="6"/><path d="M58 88 Q70 86 76 90" fill="none" stroke="#B9BCC8" stroke-width="3"/>'
    f'<path d="M30 106 L22 118 H36Z" fill="#FF9F1C" {W(2.2)}/>'
    f'<path d="M44 34 Q48 28 52 34" fill="none" {W(2)}/>'
    + stars(((20, 24), (108, 26), (114, 50)), 3.4, "#FFFFFF"))

# 14. Rebotica (Дмитровская): программирование и разработка игр
I["fun-rebotica-novodmitrovskaya"] = ("#E3FFF6", "#36B8A0",
    "большая клавиша Enter со стрелкой-уголком и мордашкой",
    "по ней нажимают пальцем, и из неё выпрыгивает пиксельный человечек из компьютерной игры",
    f'<rect x="6" y="94" width="116" height="34" rx="6" fill="#2B2B3A"/>'
    + "".join(f'<rect x="{x}" y="100" width="14" height="10" rx="2" fill="#5A5878"/>' for x in (12, 30, 98))
    + f'<path d="M30 112 V76 H62 V56 H98 V112Z" fill="#F4F6FA" {W(3.4)}/>'
    f'<path d="M34 108 V80 H66 V60 H94 V108Z" fill="#FFFFFF"/>'
    f'<path d="M84 70 V84 H58 M64 78 L58 84 L64 90" fill="none" stroke="#36B8A0" stroke-width="3.4"/>'
    + face(64, 98, d=8, k=0.6) +
    f'<path d="M98 54 Q104 40 98 26" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-dasharray="3 4"/>'
    + "".join(f'<rect x="{90+x*4}" y="{6+y*4}" width="4" height="4" fill="{c}"/>' for x, y, c in
              ((1, 0, "#FFD9B8"), (2, 0, "#FFD9B8"), (1, 1, "#FFD9B8"), (2, 1, "#FFD9B8"),
               (0, 2, "#E8434A"), (1, 2, "#E8434A"), (2, 2, "#E8434A"), (3, 2, "#E8434A"),
               (1, 3, "#E8434A"), (2, 3, "#E8434A"), (1, 4, "#3F6FD0"), (2, 4, "#3F6FD0"),
               (0, 5, "#3F6FD0"), (3, 5, "#3F6FD0")))
    + f'<rect x="90" y="6" width="16" height="24" fill="none" stroke="{O}" stroke-width="0"/>'
    f'<path d="M20 70 H10 M22 60 L14 54 M22 80 L14 86" stroke="#FFFFFF" stroke-width="3"/>'
    + stars(((18, 30), (60, 20), (114, 46)), 3.4, "#FFFFFF"))

# 15. Галерея «Листок» (Бунинская аллея): изостудия
I["fun-listok-galereya-lazareva"] = ("#FFF8DC", "#C9D66A",
    "зелёный листок липы с прожилками, мордашкой и синим беретом",
    "сам пишет свой портрет на маленьком мольберте, держа кисточку черенком",
    f'<path d="M80 124 L88 72 M112 124 L104 72 M96 72 V124" stroke="#B5763A" stroke-width="4"/>'
    f'<rect x="78" y="64" width="36" height="34" rx="2" fill="#FFFFFF" {W(2.8)}/>'
    f'<path d="M96 70 Q84 76 88 88 Q96 94 104 88 Q108 76 96 70Z" fill="#9BE36A" {W(1.8)}/>'
    f'<path d="M96 70 V92" stroke="#4CB07A" stroke-width="1.4"/>'
    f'<path d="M44 26 Q14 30 14 62 Q16 92 44 104 Q72 92 74 62 Q74 30 44 26Z" fill="#6CC24A" {W(3.2)}/>'
    f'<path d="M44 30 V100 M44 56 L26 44 M44 56 L62 44 M44 76 L24 66 M44 76 L64 66" stroke="#3E9A34" stroke-width="2.2"/>'
    + face(44, 60, d=9, k=0.62) +
    f'<path d="M24 30 Q42 14 62 24 Q60 32 42 32 Q30 34 24 30Z" fill="#3F6FD0" {W(2.6)}/><circle cx="44" cy="18" r="2.6" fill="{O}"/>'
    f'<path d="M44 104 Q46 114 40 120" fill="none" stroke="#3E9A34" stroke-width="4"/>'
    f'<path d="M66 78 L80 74" stroke="#B5763A" stroke-width="3"/><circle cx="82" cy="74" r="2.6" fill="#E8434A" {W(1.4)}/>'
    + stars(((106, 26), (84, 40), (20, 110)), 3.4, "#FFFFFF"))

# 16. «5 ключей Форта» (Подольск): квест для детей
I["fun-5-klyuchey-forta-podolsk"] = ("#F0E6FF", "#7F5BC8",
    "кованый сундук-сокровищница с пятью замочными скважинами на передней стенке",
    "крышка приоткрыта, из щели льётся золотой свет и сыплются монетки",
    f'<path d="M24 26 L40 52 M64 18 V50 M104 26 L88 52" stroke="#FFE27A" stroke-width="6" opacity=".7"/>'
    f'<path d="M20 68 Q20 50 64 50 Q108 50 108 68Z" fill="#8A4B2A" {W(3.2)}/>'
    f'<path d="M20 64 L108 62" stroke="#FFD23F" stroke-width="3"/>'
    f'<rect x="20" y="68" width="88" height="44" rx="4" fill="#A9603A" {W(3.2)}/>'
    f'<path d="M20 78 H108 M34 68 V112 M94 68 V112" stroke="#6E6A80" stroke-width="5"/>'
    + "".join(f'<circle cx="{x}" cy="96" r="3.2" fill="#FFD23F" {W(1.4)}/><path d="M{x} 98 V103" stroke="{O}" stroke-width="2"/>'
              for x in (44, 54, 64, 74, 84))
    + face(64, 84, d=8, k=0.42, mouth=False) +
    "".join(f'<ellipse cx="{x}" cy="{y}" rx="4.4" ry="3" fill="#FFC72C" {W(1.6)}/>' for x, y in ((14, 116), (110, 118), (118, 108), (100, 46)))
    + stars(((30, 20), (98, 18), (64, 10)), 3.4, "#FFF3B0"))

# 17. Плейпорт (Аннино): игровой центр
I["fun-playport-annino"] = ("#DCF3FF", "#4AA7E0",
    "кораблик-игровой домик с иллюминаторами, мачтой и горкой-трапом",
    "пришвартован в игровом порту на волнах, с трапа-горки съезжает малыш в оранжевой футболке",
    f'<path d="M0 104 Q16 98 32 104 T64 104 T96 104 T128 104 V128 H0Z" fill="#3F8FE8" {W(2.4)}/>'
    f'<path d="M14 84 H100 L90 108 H26Z" fill="#E8434A" {W(3.2)}/>'
    f'<path d="M22 92 H96" stroke="#FFFFFF" stroke-width="3"/>'
    f'<rect x="32" y="58" width="46" height="26" rx="4" fill="#FFD23F" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="70" r="5" fill="#BFE8FF" {W(2)}/>' for x in (44, 66))
    + f'<path d="M56 58 V22" {W(3)}/><path d="M56 22 L76 28 L56 34Z" fill="#4CB07A" {W(2)}/>'
    f'<path d="M100 84 L120 106" stroke="{O}" stroke-width="11"/><path d="M100 84 L120 106" stroke="#7CD26E" stroke-width="7"/>'
    f'<circle cx="104" cy="78" r="6" fill="#FFD9B8" {W(2)}/>' + eye(102.6, 78, 0.3) + eye(105.6, 78, 0.3) +
    f'<path d="M100 84 L110 90 L106 94 L98 88Z" fill="#FF8A1F" {W(1.8)}/>'
    + face(55, 98, d=0, k=0, mouth=False, blush=False)
    + stars(((18, 30), (104, 22), (24, 60)), 3.4, "#FFFFFF"))

# 18. Play Day (Селигерская): игровые автоматы и детская комната
I["fun-play-day-seligerskaya"] = ("#FFE3F1", "#E65C9C",
    "автомат-хватайка со стеклянной витриной и металлической лапкой-клешнёй",
    "лапка вытягивает из горки игрушек плюшевого жёлтого цыплёнка, а на табло мигают огоньки",
    f'<rect x="28" y="14" width="72" height="104" rx="8" fill="#7A4CE0" {W(3.2)}/>'
    f'<rect x="34" y="20" width="60" height="12" rx="4" fill="#2B2B3A"/>'
    + "".join(f'<circle cx="{40+i*8}" cy="26" r="2.4" fill="{c}"/>' for i, c in enumerate(("#FFD23F", "#FF6FA3", "#5FD3FF", "#9BE36A", "#FFD23F", "#FF6FA3", "#5FD3FF")))
    + f'<rect x="36" y="36" width="56" height="50" rx="3" fill="#E6F7FF" {W(2.6)}/>'
    f'<path d="M64 36 V50" stroke="#9AA3B5" stroke-width="2"/>'
    f'<path d="M58 50 H70 M60 50 L54 60 M68 50 L74 60" fill="none" stroke="#9AA3B5" stroke-width="2.6"/>'
    f'<circle cx="64" cy="64" r="8" fill="#FFD23F" {W(2.2)}/>' + eye(61.5, 63, 0.4) + eye(66.5, 63, 0.4) +
    f'<path d="M63 67 L65 67 L64 69Z" fill="#FF9F1C"/>'
    f'<circle cx="46" cy="80" r="6" fill="#FF6FA3" {W(1.8)}/><circle cx="58" cy="82" r="5" fill="#5FD3FF" {W(1.8)}/>'
    f'<circle cx="80" cy="80" r="6" fill="#9BE36A" {W(1.8)}/><circle cx="70" cy="84" r="4" fill="#FF9F1C" {W(1.6)}/>'
    f'<rect x="36" y="90" width="56" height="20" rx="3" fill="#5B36B8" {W(2.4)}/>'
    f'<path d="M50 104 V94" {W(3)}/><circle cx="50" cy="93" r="4" fill="#E8434A" {W(1.8)}/>'
    f'<circle cx="76" cy="100" r="5" fill="#FFD23F" {W(2)}/>'
    + stars(((16, 30), (112, 28), (112, 90)), 3.4, "#FFFFFF"))

if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
