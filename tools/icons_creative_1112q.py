"""Иконки робота creative, 12.11 (запуск 1112q). Каждая придумана и нарисована отдельно: свой герой, своя сцена,
своя компоновка и свой фон (правило абсолютной уникальности). python3 tools/icons_creative_1112q.py [--subjects]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_creative_1112k import bg, ln, limb, note, SKIN

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
I = {}


def cheeks(x1, x2, y, c="#FF7FA8"):
    return (f'<ellipse cx="{x1}" cy="{y}" rx="3" ry="1.8" fill="{c}" opacity=".65"/>'
            f'<ellipse cx="{x2}" cy="{y}" rx="3" ry="1.8" fill="{c}" opacity=".65"/>')


# 1 Музыкальные классы (Некрасовка, сольфеджио и инструменты с 5 лет): восьмая нота взбирается по нотному стану-лестнице
I["musicclasses-lipchanskogo"] = ("восьмая нота-малыш с хвостиком-флажком и румяной головкой",
    "взбирается вверх по пяти линейкам нотного стана, поставленным наискосок, как по лестнице", bg("#DFF7EE", "#1F8A70", f'''
<g transform="rotate(-28 64 70)">
{''.join(f'<path d="M-10 {y} H140" {ln("#0E5C4A", 3)}/>' for y in (46, 58, 70, 82, 94))}
</g>
<g transform="translate(62 46) rotate(-12)">
<path d="M14 -2 V-44" {ln(O, 7)}/><path d="M14 -2 V-44" {ln("#2B2B3B", 4)}/>
<path d="M14 -44 Q30 -36 32 -20 Q24 -30 14 -30" fill="#2B2B3B" {s()}/>
<ellipse cx="2" cy="2" rx="17" ry="13" fill="#2B2B3B" transform="rotate(-20 2 2)" {s()}/>
{eye(-3, 0, 0.5)}{eye(7, -3, 0.5)}<path d="M-1 7 Q3 10 8 6" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round"/>
<ellipse cx="-8" cy="6" rx="3" ry="1.8" fill="#FF7FA8" opacity=".8"/>
</g>
{limb(54, 58, 46, 74, "#2B2B3B", 3)}{limb(66, 60, 70, 76, "#2B2B3B", 3)}
{sparkle(104, 22, 5)}{sparkle(20, 100, 3.5)}
'''))

# 2 Active Style (хип-хоп для детей 4–15, Новогиреево): девочка в панамке танцует у граффити-стены
I["active-style-zeleny"] = ("кудрявая девочка в широких голубых джинсах и жёлтой панамке",
    "танцует хип-хоп, вскинув одну руку вверх, перед кирпичной стеной с яркими граффити-пятнами", bg("#FFE9D6", "#E8743B", f'''
<rect x="0" y="0" width="128" height="104" fill="#D9825B"/>
<g stroke="#B9623F" stroke-width="2">{''.join(f'<path d="M0 {y} H128"/>' for y in range(14, 104, 14))}</g>
<path d="M8 30 Q26 14 44 32 Q30 44 12 40Z" fill="#7CE0FF" opacity=".9"/><path d="M84 18 Q104 10 116 30 Q100 38 86 32Z" fill="#B6FF5C" opacity=".9"/>
<path d="M94 70 Q112 60 122 78 Q108 90 96 84Z" fill="#FF5CC8" opacity=".85"/>
<path d="M0 104 H128 V128 H0Z" fill="#6B6B7B"/>
<path d="M56 84 L46 112 M70 84 L82 110" {ln(O, 13)}/><path d="M56 84 L46 112 M70 84 L82 110" {ln("#5B8FE0", 10)}/>
<ellipse cx="44" cy="114" rx="8" ry="4" fill="#fff" {s()}/><ellipse cx="85" cy="112" rx="8" ry="4" fill="#fff" {s()}/>
<path d="M50 56 Q63 50 76 56 L74 86 H52Z" fill="#FF4F6D" {s()}/>
{limb(52, 60, 36, 74, SKIN, 5)}{limb(74, 58, 92, 30, SKIN, 5)}
<circle cx="63" cy="40" r="13" fill="{SKIN}" {s()}/>
<g fill="#5A3A22" {s('stroke-width="1.8"')}><circle cx="51" cy="40" r="5"/><circle cx="75" cy="40" r="5"/><circle cx="52" cy="48" r="4"/><circle cx="74" cy="48" r="4"/></g>
<path d="M46 32 Q63 14 80 32 L86 34 H40Z" fill="#FFD23C" {s()}/>
{eye(58, 41, 0.5)}{eye(68, 41, 0.5)}<path d="M59 47 Q63 50 67 47" fill="none" {ln(O, 1.8)}/>{cheeks(54, 72, 45)}
'''))

# 3 «Жете» (балет, Новокосино): балерина в мятной пачке в прыжке гран-жете над полумесяцем
I["zhete-novokosino-gorodetskaya"] = ("девочка-балерина в мятной пачке и белых пуантах",
    "летит в прыжке гран-жете в шпагате над тонким золотым полумесяцем в ночном небе", bg("#6E5BC4", "#241A5E", f'''
<path d="M30 112 Q64 76 98 112 Q64 92 30 112Z" fill="#FFD66B" {s()}/>
{''.join(sparkle(x, y, r) for x, y, r in ((14, 30, 3), (110, 24, 3.5), (100, 60, 2.5), (22, 70, 2.5)))}
{limb(58, 62, 18, 66, SKIN, 5)}{limb(70, 62, 110, 54, SKIN, 5)}
<path d="M16 62 L10 68 L18 70Z M112 50 L120 54 L112 58Z" fill="#fff" {s('stroke-width="2"')}/>
<path d="M40 60 Q64 46 88 60 Q64 72 40 60Z" fill="#9FF0D2" {s()}/>
<path d="M56 60 Q64 34 72 60Z" fill="#7FDBBE" {s()}/>
{limb(60, 46, 40, 28, SKIN, 4)}{limb(68, 46, 88, 30, SKIN, 4)}
<circle cx="64" cy="34" r="10" fill="{SKIN}" {s()}/>
<circle cx="64" cy="22" r="5" fill="#6B3D1E" {s('stroke-width="2"')}/>
{eye(60, 35, 0.42)}{eye(68, 35, 0.42)}<path d="M61 39 Q64 41 67 39" fill="none" {ln(O, 1.6)}/>{cheeks(57, 71, 38)}
'''))

# 4 Первая танцевальная академия (бальные танцы, Реутов): розовое бальное платье-колокол с номером «1» кружится
I["first-dance-academy-reutov"] = ("пышное розовое бальное платье-колокол с рюшами и мордашкой на лифе",
    "кружится на паркете турнира, на спинке приколот номер участника «1», а за ним летят блёстки", bg("#FFF3D9", "#C9862D", f'''
<path d="M0 108 H128 V128 H0Z" fill="#B97A3F"/><path d="M0 116 H128 M20 108 L14 128 M52 108 L48 128 M84 108 L82 128 M114 108 L114 128" stroke="#94602E" stroke-width="2"/>
<path d="M30 104 Q34 70 50 56 L78 56 Q94 70 98 104 Q64 116 30 104Z" fill="#FF8FB8" {s()}/>
<path d="M34 92 Q50 100 64 92 Q78 100 94 92" fill="none" {ln("#fff", 3)}/><path d="M32 102 Q48 110 64 102 Q80 110 96 102" fill="none" {ln("#fff", 3)}/>
<path d="M50 56 Q48 34 56 26 H72 Q80 34 78 56Z" fill="#FF6FA3" {s()}/>
<rect x="84" y="36" width="22" height="18" rx="2" fill="#fff" transform="rotate(12 95 45)" {s('stroke-width="2.4"')}/>
<path d="M94 40 L97 38 V52" {ln(O, 2.6)} fill="none" transform="rotate(12 95 45)"/>
{face(64, 42, 7, 0.6)}
<path d="M56 26 Q64 18 72 26" fill="none" {ln("#FFD23C", 4)}/>
{sparkle(18, 40, 4)}{sparkle(22, 76, 3)}{sparkle(110, 80, 3)}{sparkle(14, 18, 2.6, "#FFD23C")}
'''))

# 5 ViArtfam (брейк, хип-хоп, детский танец 3+): малыш в зелёном комбинезоне крутит «винт» на синем коврике
I["viartfam-suzdalskaya"] = ("малыш в травяно-зелёном комбинезоне и белой шапочке-бини",
    "крутит брейк-«винт» на спине, ноги в воздухе ножницами, на круглом синем коврике под лучом прожектора", bg("#2E2E48", "#0F0F1E", f'''
<path d="M64 0 L30 110 H98Z" fill="#FFF7C2" opacity=".18"/>
<ellipse cx="64" cy="104" rx="44" ry="12" fill="#3D7BFF" {s()}/>
<path d="M28 98 Q64 112 100 98" fill="none" stroke="#9DBBFF" stroke-width="2.4" opacity=".8"/>
<ellipse cx="64" cy="90" rx="22" ry="11" fill="#4CC35B" {s()}/>
{limb(70, 84, 96, 46, "#4CC35B", 8)}{limb(62, 84, 40, 44, "#4CC35B", 8)}
<ellipse cx="98" cy="42" rx="7" ry="5" fill="#fff" {s()}/><ellipse cx="38" cy="40" rx="7" ry="5" fill="#fff" {s()}/>
{limb(48, 92, 30, 104, SKIN, 4)}
<circle cx="86" cy="94" r="11" fill="{SKIN}" {s()}/>
<path d="M76 90 Q86 76 97 90Z" fill="#fff" {s('stroke-width="2.4"')}/>
{eye(83, 96, 0.42)}{eye(90, 96, 0.42)}<path d="M84 100 Q87 102 90 100" fill="none" {ln(O, 1.6)}/>
<path d="M30 30 Q24 24 30 18 M100 22 Q108 18 106 10" fill="none" {ln("#FFE14F", 3)}/>
{sparkle(20, 60, 3.5, "#FFE14F")}{sparkle(112, 70, 3, "#7CFF6B")}
'''))

# 6 Хоровая школа «Радуга» (Реутов): семь полосок радуги-хористов поют на облаке
I["raduga-hor-reutov"] = ("радуга из семи цветных полосок, у каждой свой поющий ротик",
    "стоит на пушистом облаке, как хор на ступеньках, и поёт хором — сверху летит одна большая нота", bg("#E8F6FF", "#4A9BE0", f'''
{''.join(f'<path d="M{18 + 5*i} 92 A{46 - 5*i} {46 - 5*i} 0 0 1 {110 - 5*i} 92" fill="none" stroke="{c}" stroke-width="6"/>' for i, c in enumerate(("#FF4D4D", "#FF9A3C", "#FFD93C", "#5BD46A", "#4AB3FF", "#4A63E0", "#9B5BE0")))}
<path d="M14 92 A50 50 0 0 1 114 92" fill="none" stroke="{O}" stroke-width="2.4"/><path d="M50 92 A14 14 0 0 1 78 92" fill="none" stroke="{O}" stroke-width="2.4"/>
{''.join(f'<ellipse cx="{x}" cy="{y}" rx="2.2" ry="3" fill="{O}"/>' for x, y in ((24, 70), (34, 52), (48, 40), (64, 36), (80, 40), (94, 52), (104, 70)))}
<path d="M10 104 Q8 90 22 92 Q26 80 40 88 Q50 80 62 90 Q74 80 86 88 Q98 80 106 92 Q122 90 118 106 Q64 116 10 104Z" fill="#fff" {s()}/>
{eye(52, 98, 0.45)}{eye(76, 98, 0.45)}<path d="M60 102 Q64 105 68 102" fill="none" {ln(O, 1.8)}/>
{note(64, 18, 1.2, O)}{sparkle(108, 26, 4)}{sparkle(20, 30, 3)}
'''))

# 7 Школа вокала Рамос (вокал для детей 5–11, Реутов): розовый караоке-микрофон поёт, звук расходится кольцами
I["ramos-vocal-reutov"] = ("розовый детский караоке-микрофон со светящейся голубой головкой и мордашкой на ручке",
    "стоит на маленьком круглом подиуме и поёт, а из головки расходятся три дуги-волны звука", bg("#FFE0F0", "#D6337F", f'''
<ellipse cx="64" cy="112" rx="30" ry="8" fill="#FFD23C" {s()}/>
<path d="M50 54 L54 108 H74 L78 54Z" fill="#FF6FB0" {s()}/>
<circle cx="64" cy="40" r="20" fill="#8BE6FF" {s()}/>
<path d="M48 34 Q64 26 80 34 M46 42 H82 M48 50 Q64 56 80 50" fill="none" stroke="#3FB5D6" stroke-width="2"/>
<rect x="46" y="54" width="36" height="6" rx="3" fill="#C24A88" {s('stroke-width="2.2"')}/>
{eye(59, 76, 0.5)}{eye(69, 76, 0.5)}<ellipse cx="64" cy="86" rx="4" ry="5" fill="{O}"/>{cheeks(55, 73, 82)}
<path d="M92 24 Q100 40 92 56 M102 16 Q114 40 102 64 M30 26 Q22 40 30 54" fill="none" {ln("#fff", 3.4)}/>
'''))

# 9 Testa Dance Show (детская и подростковая хореография): красная юбка-солнце кружится на сцене под конфетти
I["testa-dance-pavlovsky"] = ("красная юбка-солнце с мордашкой на широком золотом поясе",
    "кружится на сцене, подол разлетается волной, из-под него видны ножки в белых чешках, сверху падает серебряное конфетти", bg("#3B1F4E", "#14081E", f'''
<path d="M0 108 H128 V128 H0Z" fill="#6B3A2A"/>
{limb(56, 96, 50, 112, SKIN, 4)}{limb(72, 96, 80, 110, SKIN, 4)}
<ellipse cx="49" cy="113" rx="5" ry="3" fill="#fff" {s('stroke-width="2"')}/><ellipse cx="82" cy="111" rx="5" ry="3" fill="#fff" {s('stroke-width="2"')}/>
<path d="M50 48 L20 92 Q30 100 42 92 Q52 102 64 94 Q76 102 86 92 Q98 100 110 90 L78 48Z" fill="#E8263C" {s()}/>
<path d="M58 54 L44 92 M70 54 L82 92" stroke="#B5172B" stroke-width="2"/>
<rect x="46" y="38" width="36" height="14" rx="5" fill="#FFC93C" {s()}/>
{eye(58, 45, 0.45)}{eye(70, 45, 0.45)}<path d="M61 49 Q64 51 67 49" fill="none" {ln(O, 1.6)}/>
{''.join(f'<rect x="{x}" y="{y}" width="4" height="7" rx="1" fill="#D8DEE8" transform="rotate({r} {x} {y})"/>' for x, y, r in ((18, 18, 20), (40, 10, -30), (90, 14, 40), (108, 34, -10), (28, 40, 60), (102, 60, 15)))}
{sparkle(64, 18, 4)}
'''))

# 10 ДШИ им. Римского-Корсакова (музыка, Новогиреево): золотая белка из «Сказки о царе Салтане» стучит орешком по клавишам рояля
I["dshi-rimsky-korsakov-novogireevo"] = ("золотая сказочная белка с изумрудным орешком в лапках",
    "сидит на клавиатуре чёрного рояля и выстукивает орешком мелодию, хвост трубой", bg("#FFF6D8", "#C99A2E", f'''
<path d="M6 82 H122 V112 H6Z" fill="#222232" {s()}/>
<rect x="12" y="82" width="104" height="16" fill="#fff" {s('stroke-width="2.4"')}/>
<g stroke="{O}" stroke-width="1.6">{''.join(f'<path d="M{x} 82 V98"/>' for x in range(22, 116, 10))}</g>
<g fill="#222232">{''.join(f'<rect x="{x}" y="82" width="5" height="9"/>' for x in (19, 29, 49, 59, 69, 89, 99))}</g>
<path d="M78 76 Q110 70 106 40 Q102 20 86 26 Q98 34 92 48 Q86 60 72 62Z" fill="#FFC93C" {s()}/>
<path d="M90 32 Q100 40 96 52" fill="none" stroke="#E0A21E" stroke-width="2.4"/>
<ellipse cx="62" cy="64" rx="15" ry="18" fill="#FFC93C" {s()}/>
<circle cx="56" cy="40" r="13" fill="#FFC93C" {s()}/>
<path d="M46 32 L44 20 L52 28Z M60 28 L64 16 L66 30Z" fill="#FFC93C" {s('stroke-width="2.4"')}/>
{eye(52, 40, 0.45)}{eye(60, 40, 0.45)}<path d="M53 46 Q56 48 59 46" fill="none" {ln(O, 1.6)}/>{cheeks(48, 63, 45)}
<circle cx="50" cy="66" r="6" fill="#27C27A" {s()}/>{limb(58, 60, 50, 66, "#FFC93C", 3)}
<path d="M42 72 Q40 78 44 82" fill="none" {ln(O, 2)}/>
{note(28, 30, 0.8)}{note(18, 56, 0.6)}{sparkle(110, 18, 4)}
'''))

# 11 Арт-студия «Исток» (рисование 6–14, Новопеределкино): девочка в перепачканном фартуке катит радугу валиком
I["istok-art-lukinskaya"] = ("девочка-художница с хвостиком в фартуке, перепачканном красками",
    "стоит на коленках у большого листа на полу и прокатывает малярным валиком широкую полосу-радугу", bg("#EAF8FF", "#5BB6D6", f'''
<rect x="8" y="78" width="112" height="40" rx="3" fill="#fff" transform="rotate(-4 64 98)" {s()}/>
{''.join(f'<path d="M14 {96 + 5*i} Q50 {84 + 5*i} 84 {94 + 5*i}" fill="none" stroke="{c}" stroke-width="5" stroke-linecap="round"/>' for i, c in enumerate(("#FF5050", "#FFB23C", "#FFE14F", "#4CC35B", "#4A90E2")))}
<rect x="80" y="84" width="22" height="16" rx="4" fill="#9B5BE0" {s()}/>
{limb(91, 84, 80, 62, "#8A8A9A", 3)}
{limb(64, 60, 80, 62, SKIN, 4)}
<path d="M50 50 Q60 44 70 50 L72 78 H48Z" fill="#FFF3C4" {s()}/>
<circle cx="56" cy="62" r="3" fill="#FF5050"/><circle cx="64" cy="70" r="2.6" fill="#4A90E2"/><circle cx="54" cy="72" r="2.4" fill="#4CC35B"/>
<circle cx="60" cy="36" r="12" fill="{SKIN}" {s()}/>
<path d="M48 34 Q52 22 62 23 Q72 24 72 34 Q64 28 48 34Z" fill="#8B4A22" {s('stroke-width="2.2"')}/>
<path d="M70 26 Q84 22 82 36" fill="none" {ln(O, 7)}/><path d="M70 26 Q84 22 82 36" fill="none" {ln("#8B4A22", 4)}/>
{eye(56, 37, 0.45)}{eye(64, 37, 0.45)}<path d="M57 42 Q60 44 63 42" fill="none" {ln(O, 1.6)}/>
<circle cx="66" cy="42" r="2" fill="#FFB23C"/>
'''))

# 12 Planeta (вокал и барабаны с 4 лет, Пролетарская): оранжевая планета с кольцом-обручем барабана, по которому стучат палочки
I["planeta-vocal-melnikova"] = ("маленькая оранжевая планета с мордашкой и широким кольцом",
    "кольцо планеты превратилось в обод барабана — по нему лупят две барабанные палочки, а вокруг в космосе пляшут нотки", bg("#2B2366", "#0D0A2B", f'''
{''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".8"/>' for x, y, r in ((14, 20, 1.5), (110, 16, 1.8), (20, 96, 1.4), (116, 100, 1.6), (96, 40, 1.2)))}
<ellipse cx="64" cy="70" rx="54" ry="14" fill="none" {ln(O, 12)}/>
<ellipse cx="64" cy="70" rx="54" ry="14" fill="none" stroke="#E04D4D" stroke-width="8"/>
<circle cx="64" cy="62" r="30" fill="#FF9F3C" {s()}/>
<path d="M38 52 Q64 46 90 52 M36 68 Q64 62 92 68" fill="none" stroke="#E07A1E" stroke-width="3"/>
<path d="M10 70 A54 14 0 0 0 118 70" fill="none" {ln(O, 12)}/><path d="M10 70 A54 14 0 0 0 118 70" fill="none" stroke="#E04D4D" stroke-width="8"/>
<path d="M18 72 Q64 84 110 72" fill="none" stroke="#FFD5D5" stroke-width="2"/>
{eye(56, 58, 0.55)}{eye(72, 58, 0.55)}<path d="M58 66 Q64 72 70 66" fill="none" {ln(O, 2)}/>{cheeks(50, 78, 64)}
{limb(30, 30, 44, 80, "#E8C07A", 3)}{limb(100, 28, 86, 80, "#E8C07A", 3)}
{note(20, 46, 0.7, "#FFE14F")}{note(110, 54, 0.6, "#7CE0FF")}
'''))

# 13 X-temp (Baby dance с 2,5 лет, ритмика, Новокосино): малышка в лимонных гетрах хлопает над головой среди прыгающих мячиков
I["x-temp-saltykovskaya"] = ("малышка с двумя пучками в лимонных гетрах и фиолетовой юбочке",
    "на ритмике топает ножкой и хлопает над головой, а вокруг в такт подпрыгивают три маленьких мячика", bg("#F3E8FF", "#9B5BE0", f'''
<path d="M0 108 H128 V128 H0Z" fill="#C9A6F2"/>
{limb(58, 82, 52, 104, "#F3F05A", 6)}{limb(70, 82, 80, 98, "#F3F05A", 6)}
<ellipse cx="50" cy="106" rx="7" ry="4" fill="#fff" {s()}/><ellipse cx="84" cy="99" rx="7" ry="4" fill="#fff" {s()}/>
<path d="M46 76 Q64 70 82 76 L88 86 H40Z" fill="#7B3FC4" {s()}/>
<path d="M54 56 Q64 50 74 56 L74 78 H54Z" fill="#fff" {s()}/>
{limb(56, 58, 52, 26, SKIN, 4)}{limb(72, 58, 76, 26, SKIN, 4)}
<circle cx="56" cy="22" r="4" fill="{SKIN}" {s('stroke-width="2"')}/><circle cx="72" cy="22" r="4" fill="{SKIN}" {s('stroke-width="2"')}/>
<path d="M60 16 L64 12 L68 16" fill="none" {ln("#fff", 2)}/>
<circle cx="64" cy="42" r="12" fill="{SKIN}" {s()}/>
<circle cx="53" cy="32" r="5" fill="#E07A3C" {s('stroke-width="2"')}/><circle cx="75" cy="32" r="5" fill="#E07A3C" {s('stroke-width="2"')}/>
{eye(60, 43, 0.45)}{eye(68, 43, 0.45)}<ellipse cx="64" cy="48" rx="2.4" ry="2" fill="{O}"/>{cheeks(56, 72, 47)}
<circle cx="20" cy="88" r="7" fill="#FF5C8A" {s()}/><circle cx="108" cy="80" r="7" fill="#3FD0C9" {s()}/><circle cx="22" cy="54" r="6" fill="#FFB23C" {s()}/>
<path d="M14 100 Q20 96 26 100 M102 92 Q108 88 114 92" fill="none" {ln(O, 1.6)}/>
'''))

# 14 Impulse (танцы 7+, Королёв — город космонавтики): девочка-космонавт танцует «волну» на Луне
I["impulse-dance-korolev"] = ("девочка-космонавт в белом скафандре с прозрачным шлемом и розовой чёлкой",
    "танцует хип-хоп «волну» руками на серой Луне, а за ней висит голубая Земля", bg("#22234A", "#090A1C", f'''
<circle cx="104" cy="24" r="14" fill="#4AA8FF" {s()}/><path d="M96 18 Q104 14 108 22 Q102 30 96 26Z" fill="#5BD46A"/>
<path d="M0 104 Q64 88 128 104 V128 H0Z" fill="#B7B9C8" {s()}/>
<circle cx="30" cy="110" r="5" fill="#9A9CAE"/><circle cx="96" cy="112" r="4" fill="#9A9CAE"/>
{limb(56, 84, 50, 104, "#F2F2F7", 8)}{limb(72, 84, 80, 102, "#F2F2F7", 8)}
<rect x="48" y="58" width="32" height="30" rx="10" fill="#F2F2F7" {s()}/>
<rect x="58" y="66" width="12" height="9" rx="2" fill="#FF6FA3" {s('stroke-width="2"')}/>
<path d="M48 64 Q38 58 32 66 Q26 74 18 68" fill="none" {ln(O, 11)}/><path d="M48 64 Q38 58 32 66 Q26 74 18 68" fill="none" {ln("#F2F2F7", 7)}/>
<path d="M80 64 Q90 56 96 64 Q102 72 110 64" fill="none" {ln(O, 11)}/><path d="M80 64 Q90 56 96 64 Q102 72 110 64" fill="none" {ln("#F2F2F7", 7)}/>
<circle cx="64" cy="40" r="20" fill="#CFEFFF" opacity=".55" {s()}/>
<circle cx="64" cy="42" r="12" fill="{SKIN}" {s('stroke-width="2.2"')}/>
<path d="M52 40 Q56 28 66 30 Q74 30 76 40 Q66 34 52 40Z" fill="#FF6FA3" {s('stroke-width="2"')}/>
{eye(60, 44, 0.42)}{eye(68, 44, 0.42)}<path d="M61 48 Q64 50 67 48" fill="none" {ln(O, 1.6)}/>
<ellipse cx="56" cy="32" rx="5" ry="3" fill="#fff" opacity=".7"/>
{sparkle(16, 24, 3)}{sparkle(40, 14, 2.4)}
'''))

# 15 Синергия (фортепиано и пение с 5 лет, Балашиха): гусеница из клавиш фортепиано ползёт по листу
I["sinergiya-music-balashikha"] = ("гусеница, сложенная из чёрно-белых клавиш фортепиано",
    "ползёт волной по большому зелёному листу, приподняв голову в наушниках-цветочках, и напевает", bg("#EFFFE0", "#5FB33A", f'''
<path d="M6 112 Q30 70 82 70 Q118 72 124 112Z" fill="#7ED957" {s()}/>
<path d="M14 108 Q60 88 118 104" fill="none" stroke="#4E9E2E" stroke-width="3"/>
{''.join(f'<rect x="{18 + 14*i}" y="{78 - (8 if i % 2 else 0)}" width="14" height="24" rx="3" fill="#fff" {s("stroke-width=\"2.4\"")}/>' for i in range(5))}
{''.join(f'<rect x="{28 + 14*i}" y="{76 - (8 if i % 2 else 0)}" width="8" height="14" rx="2" fill="#2A2A3A"/>' for i in range(4))}
<circle cx="98" cy="62" r="16" fill="#2A2A3A" {s()}/>
<circle cx="84" cy="52" r="5" fill="#FF8FB0" {s('stroke-width="2"')}/><circle cx="112" cy="52" r="5" fill="#FF8FB0" {s('stroke-width="2"')}/>
<path d="M84 50 Q98 36 112 50" fill="none" {ln("#FF8FB0", 3)}/>
{eye(93, 62, 0.5)}{eye(103, 62, 0.5)}<path d="M94 69 Q98 72 102 69" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round"/>
<ellipse cx="89" cy="67" rx="3" ry="1.8" fill="#FF7FA8" opacity=".8"/><ellipse cx="107" cy="67" rx="3" ry="1.8" fill="#FF7FA8" opacity=".8"/>
{note(74, 28, 0.8)}{note(90, 18, 0.65)}{sparkle(20, 30, 4)}
'''))

# 16 Дом художников (живопись и рисунок 5–16, Химки): деревянная палитра с кляксами рисует солнце на холсте у стены
I["dom-khudozhnikov-khimki"] = ("деревянная палитра художника с дыркой для пальца и шестью кляксами красок",
    "держит ручкой-ленточкой тонкую кисть и дорисовывает жёлтое солнце на холсте, прибитом к бирюзовой стене", bg("#DFFAF6", "#2AA198", f'''
<rect x="70" y="16" width="46" height="54" rx="3" fill="#FFFBEA" {s()}/>
<circle cx="93" cy="42" r="10" fill="#FFD23C" {s('stroke-width="2"')}/>
<path d="M93 24 V28 M93 56 V60 M75 42 H79 M107 42 H111 M80 29 L83 32 M106 29 L103 32" stroke="#FFB300" stroke-width="2.4" stroke-linecap="round"/>
<path d="M0 104 H128 V128 H0Z" fill="#1E7F78"/>
<path d="M12 80 Q10 52 40 48 Q74 46 80 70 Q84 90 66 96 Q56 98 56 108 Q54 118 38 116 Q14 110 12 80Z" fill="#D9A35E" {s()}/>
<ellipse cx="62" cy="86" rx="6" ry="5" fill="#1E7F78" {s('stroke-width="2.4"')}/>
{''.join(f'<circle cx="{x}" cy="{y}" r="5.5" fill="{c}" {s("stroke-width=\"2\"")}/>' for x, y, c in ((24, 66, "#E53935"), (38, 58, "#FFB23C"), (54, 58, "#FFE14F"), (68, 68, "#4CC35B"), (22, 86, "#3D6BE0"), (30, 102, "#9B5BE0")))}
{eye(38, 82, 0.55)}{eye(50, 82, 0.55)}<path d="M40 90 Q44 94 48 90" fill="none" {ln(O, 2)}/>{cheeks(33, 55, 88)}
<path d="M70 66 Q76 60 82 54" fill="none" {ln(O, 5)}/><path d="M70 66 Q76 60 82 54" fill="none" {ln("#D9A35E", 2.6)}/>
{limb(82, 54, 90, 40, "#8B5A2B", 2)}<path d="M89 42 L92 37" {ln("#FFB300", 3.4)}/>
{sparkle(20, 30, 4)}{sparkle(46, 18, 3)}
'''))

# 17 Белый слон (ИЗО и керамика 5–12, Химки): белый слонёнок хоботом вытягивает вазу на гончарном круге
I["bely-slon-khimki"] = ("белый слонёнок-гончар в синем фартуке",
    "сидит за гончарным кругом и хоботом бережно вытягивает горлышко рыжей глиняной вазы", bg("#FFF0E0", "#D9824A", f'''
<path d="M0 106 H128 V128 H0Z" fill="#B76A3B"/>
<rect x="74" y="88" width="40" height="20" rx="4" fill="#5A6577" {s()}/>
<ellipse cx="94" cy="86" rx="24" ry="6" fill="#8A93A3" {s()}/>
<path d="M84 84 Q80 70 88 62 Q86 54 92 50 H96 Q102 54 100 62 Q108 70 104 84Z" fill="#E0703C" {s()}/>
<path d="M86 72 Q94 76 102 72" fill="none" stroke="#B5532A" stroke-width="2"/>
<ellipse cx="42" cy="82" rx="28" ry="24" fill="#F7F7FB" {s()}/>
<path d="M28 74 Q42 90 56 74 L58 104 H26Z" fill="#3D6BE0" {s()}/>
<ellipse cx="46" cy="50" rx="22" ry="18" fill="#F7F7FB" {s()}/>
<ellipse cx="24" cy="50" rx="10" ry="14" fill="#F2E6EE" {s()}/>
<path d="M62 56 Q76 54 82 48 Q88 44 92 50" fill="none" {ln(O, 11)}/><path d="M62 56 Q76 54 82 48 Q88 44 92 50" fill="none" {ln("#F7F7FB", 7)}/>
{eye(44, 46, 0.5)}{eye(56, 46, 0.5)}<path d="M46 60 Q50 63 54 60" fill="none" {ln(O, 1.8)}/>{cheeks(38, 60, 54)}
{sparkle(108, 30, 4)}{sparkle(18, 20, 3)}
'''))

# 18 StarLight (детский музыкальный театр с 3 лет, Подольск): звёздочка с лучиками-косичками выглядывает из-за занавеса и поёт
I["starlight-podolsk"] = ("золотая звёздочка-малышка с двумя лучиками-косичками",
    "выглядывает из щели между половинками бордового занавеса и поёт в крошечный микрофон-гарнитуру", bg("#FFE6B8", "#E09A2E", f'''
<path d="M0 0 H128 V10 H0Z" fill="#6E1630"/>
<path d="M0 8 H50 Q46 60 54 128 H0Z" fill="#A11F44" {s()}/>
<path d="M128 8 H78 Q82 60 74 128 H128Z" fill="#A11F44" {s()}/>
<path d="M14 10 Q12 70 18 128 M30 10 Q28 70 34 128 M114 10 Q116 70 110 128 M98 10 Q100 70 94 128" fill="none" stroke="#7A1634" stroke-width="3"/>
<path d="M64 36 L71 52 L88 54 L75 65 L79 82 L64 73 L49 82 L53 65 L40 54 L57 52Z" fill="#FFD23C" {s()}/>
<circle cx="45" cy="54" r="3.4" fill="#FF6F91" {s('stroke-width="1.8"')}/><circle cx="83" cy="54" r="3.4" fill="#FF6F91" {s('stroke-width="1.8"')}/>
{eye(59, 60, 0.45)}{eye(69, 60, 0.45)}<ellipse cx="64" cy="67" rx="2.4" ry="2.2" fill="{O}"/>{cheeks(55, 73, 65)}
<path d="M76 62 Q74 70 68 70" fill="none" {ln(O, 1.6)}/><circle cx="67" cy="70" r="2" fill="{O}"/>
<path d="M0 112 H128 V128 H0Z" fill="#5A3A22"/>
{sparkle(64, 20, 4, "#fff")}{sparkle(64, 100, 3, "#FFD23C")}
'''))


if __name__ == "__main__":
    for pid, (hero, scene, svg_) in I.items():
        open(os.path.join(ROOT, "icons-src", pid + ".svg"), "w").write(svg_)
    if "--subjects" in sys.argv:
        p = os.path.join(ROOT, "icons-src", "subjects.txt")
        have = open(p, encoding="utf-8").read()
        with open(p, "a", encoding="utf-8") as f:
            for pid, (hero, scene, _) in I.items():
                if not any(l.startswith(pid + " — ") for l in have.splitlines()):
                    f.write(f"{pid} — герой: {hero} | сцена: {scene}\n")
    print(len(I))
