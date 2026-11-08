"""Иконки робота sections, 2026-11-08 (09 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно —
свой герой, своя сцена, своя палитра фона. Сверено со всеми листами icons-catalog/sheet-01…37 и icons-src/subjects.txt
(в баскетболе уже заняты: мячи с аксессуарами, жираф, слон, белка, кенгуру, лягушка, осьминог, робот, медвежонок, сова,
хаски, котёнок, суслик, черепаха, голубь, машина, самолёт, корабль, ракета, НЛО, снеговик, яблоня, луна, солнце, атом,
гамак, майка на верёвке, кроссовок, корзинка, пирамида, сетка-мешок, кубок, вид сверху, «дай пять», мяч на пальце,
дети на кольце, девочка с дриблингом, подросток в худи, малыш на плечах у папы).
Новые баскетбольные герои: хомячок в мяче-колесе, мяч-профессор у доски, пингвинёнок на льду, две подружки с пасом,
тигрёнок, ёжик, мяч-ныряльщик, панда-жонглёр, динозаврик с короткими лапками, морской котик, лиса с дриблингом за
спиной, мяч-будильник, обезьянка на хвосте, енот-воришка, табло «24», попугай ара, бегемотик в прыжке, качели-доска,
мяч под зонтиком, такса, дирижабль-мяч, мяч-капитан с рупором, кольцо на гараже на закате, краб.
Прочее: мальчик в черкеске (лезгинка), ферзь-садовница с лейкой, пешка-босс за столом, малыш с ракетой в бассейне,
кот-мушкетёр с рапирой, рапира-персонаж в салюте.
Запуск: python3 tools/icons_sections_1108d.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O
from icons_sections_1107h import G, king, queen, rook, bishop, knight, pawn, WHITE, BLACK
from icons_sections_1107c import ball, hoop
from icons_sections_1108b import limb, head

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
PINK, GOLD, RED, ORG, SKIN = "#FF7FA8", "#FFC93C", "#E8554A", "#F28C38", "#FFD8B8"
draw_icons.BG.update({
    "d_hamster": ("#FFF6E0", "#E9A94A"), "d_board": ("#EAF6EC", "#3E7E5A"), "d_ice": ("#F2FBFF", "#7CC4E8"),
    "d_pass": ("#F7EBFF", "#A879E0"), "d_tiger": ("#FFFBEA", "#8FC85A"), "d_hedgehog": ("#FFF1E8", "#D98A63"),
    "d_dive": ("#E3FBFF", "#1FA3C9"), "d_panda": ("#F3FFF4", "#62B88A"), "d_dino": ("#FFF9F0", "#E7B07A"),
    "d_seal": ("#EEF4FF", "#5A7FD8"), "d_fox": ("#FFF4F7", "#E86D8F"), "d_clock": ("#FFFDF2", "#D8C25A"),
    "d_monkey": ("#F4FFE8", "#4FA35A"), "d_raccoon": ("#F5F1FF", "#6E62B5"), "d_shot": ("#2C2F45", "#11131F"),
    "d_parrot": ("#FFF7F0", "#F07A3C"), "d_hippo": ("#F0FBFF", "#8A9BE0"), "d_seesaw": ("#FFFDF0", "#F2B843"),
    "d_rain": ("#E9EEF5", "#8296B2"), "d_dachs": ("#FFF5EC", "#C77B4E"), "d_airship": ("#F0FAFF", "#6FB3E8"),
    "d_captain": ("#FFF0F0", "#D94B5A"), "d_garage": ("#FFE4C2", "#C4544A"), "d_crab": ("#FFFBE6", "#3DB3B0"),
    "d_lezgi": ("#FDF3E7", "#9C4A3A"), "d_garden": ("#F2FFF0", "#8DCB6A"), "d_boss": ("#F4F6FA", "#6B7A99"),
    "d_rocketpool": ("#EAFAFF", "#3E8FD8"), "d_musket": ("#FFF8E8", "#B88A3E"), "d_salute": ("#F4EEFF", "#7457C8"),
})


def add(pid, bg, body, hero, scene):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def floor(y=108, c="#E8B77A"):
    return f'<rect x="-6" y="{y}" width="140" height="30" fill="{c}" {W(2.6)}/>'


# ============================== БАСКЕТБОЛ (IBASKET) ==============================
# 1. Кожуховская: хомячок бежит внутри баскетбольного мяча, как в колесе
add("ibasket-kozhukhovsky-17", "d_hamster",
    floor(106, "#C98B4E")
    + f'<circle cx="64" cy="62" r="42" fill="{ORG}" fill-opacity=".55" {W(3.2)}/>'
    + f'<path d="M22 62 H106 M64 20 V104" fill="none" {W(2.2)}/>'
    + f'<path d="M38 28 Q54 62 38 96 M90 28 Q74 62 90 96" fill="none" {W(2.2)}/>'
    + f'<ellipse cx="62" cy="76" rx="20" ry="15" fill="#F6C27A" {W(2.8)}/>'
    + f'<ellipse cx="62" cy="80" rx="12" ry="8" fill="#FFF1DA"/>'
    + f'<circle cx="50" cy="62" r="5" fill="#F6C27A" {W(2.4)}/><circle cx="72" cy="61" r="5" fill="#F6C27A" {W(2.4)}/>'
    + face(62, 70, d=6, k=0.6)
    + limb("M48 88 L42 98", "#F6C27A", 4) + limb("M74 88 L82 96", "#F6C27A", 4)
    + f'<path d="M108 52 h10 M110 62 h12 M108 72 h10" stroke="#fff" stroke-width="3" stroke-linecap="round"/>',
    "золотистый хомячок",
    "бежит внутри полупрозрачного баскетбольного мяча, как в беговом колесе, и катит его по паркету")

# 2. Ломоносовский: мяч-профессор в очках чертит мелом на доске траекторию броска
add("ibasket-lomonosovsky", "d_board",
    f'<rect x="10" y="14" width="108" height="62" rx="6" fill="#2F5E46" {W(3)}/>'
    + f'<path d="M24 64 Q50 10 92 40" fill="none" stroke="#fff" stroke-width="2.6" stroke-dasharray="5 5"/>'
    + f'<circle cx="24" cy="64" r="5" fill="none" stroke="#fff" stroke-width="2.4"/>'
    + f'<path d="M86 40 h14 l-3 10 h-8z" fill="none" stroke="#fff" stroke-width="2.4"/>'
    + f'<text x="36" y="70" font-family="Arial" font-weight="bold" font-size="12" fill="#fff">y=x²</text>'
    + ball(48, 96, 24)
    + f'<circle cx="41" cy="96" r="6" fill="none" {W(2.2)}/><circle cx="55" cy="96" r="6" fill="none" {W(2.2)}/><path d="M47 96 h2" {W(2)}/>'
    + limb("M68 92 L86 78", ORG, 5)
    + f'<rect x="84" y="70" width="12" height="5" rx="2" fill="#fff" transform="rotate(-35 90 72)" {W(1.8)}/>'
    + f'<rect x="-6" y="114" width="140" height="20" fill="#8C6A4E" {W(2.4)}/>',
    "баскетбольный мяч-профессор в круглых очках",
    "стоит у школьной доски и рисует мелом пунктирную параболу броска в кольцо")

# 3. Кастанаевская («Интеграл»): пингвинёнок скользит на животе по льду, толкая мяч клювом
add("ibasket-kastanaevskaya", "d_ice",
    f'<rect x="-6" y="96" width="140" height="40" fill="#DDF3FF" {W(2.6)}/>'
    + f'<path d="M8 104 h22 M40 112 h30 M86 104 h26" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    + f'<path d="M14 84 Q20 64 48 66 Q78 70 82 86 Q78 98 46 98 Q16 98 14 84Z" fill="#3A3F5C" {W(3)}/>'
    + f'<path d="M30 92 Q48 96 70 90 Q66 80 46 80 Q30 82 30 92Z" fill="#fff"/>'
    + f'<path d="M14 78 L2 70 L8 84Z" fill="#3A3F5C" {W(2.4)}/>'
    + f'<path d="M80 80 L92 82 L80 86Z" fill="{GOLD}" {W(2.2)}/>'
    + eye(70, 76, 0.7)
    + f'<path d="M28 98 l-6 6 M40 98 l-4 7" stroke="{GOLD}" stroke-width="4" stroke-linecap="round"/>'
    + ball(106, 80, 15, k=0.45)
    + f'<path d="M96 54 q4 -6 8 0 M108 48 q4 -6 8 0" fill="none" {W(2)}/>',
    "пингвинёнок",
    "скользит на животе по льду и толкает клювом баскетбольный мяч, как шайбу")

# 4. аллея Витте (есть группа девочек): две подружки в фиолетовой форме пасуют мяч друг другу
add("ibasket-vitte", "d_pass",
    floor(108, "#E8C08A")
    + limb("M30 84 L24 108", SKIN, 6) + limb("M38 84 L42 108", SKIN, 6)
    + f'<path d="M22 86 Q22 60 34 56 Q46 60 46 86Z" fill="#7B4FD0" {W(2.8)}/>'
    + f'<text x="28" y="78" font-family="Arial" font-weight="bold" font-size="11" fill="#fff">4</text>'
    + limb("M44 64 L60 56", SKIN, 5)
    + head(34, 44, hair="#3A2A20", r=12, k=0.45, style="short")
    + f'<circle cx="22" cy="36" r="6" fill="#3A2A20" {W(2)}/><circle cx="46" cy="36" r="6" fill="#3A2A20" {W(2)}/>'
    + limb("M92 84 L88 108", SKIN, 6) + limb("M100 84 L106 108", SKIN, 6)
    + f'<path d="M84 86 Q84 60 96 56 Q108 60 108 86Z" fill="#7B4FD0" {W(2.8)}/>'
    + f'<text x="90" y="78" font-family="Arial" font-weight="bold" font-size="11" fill="#fff">7</text>'
    + limb("M86 64 L72 58", SKIN, 5)
    + head(96, 44, hair="#E0A040", r=12, k=0.45, style="tail")
    + ball(64, 40, 12, fc=False)
    + f'<path d="M54 52 Q44 40 50 30 M74 52 Q84 40 78 30" fill="none" stroke="#fff" stroke-width="2.6" stroke-dasharray="3 4"/>',
    "две девочки-подружки в одинаковой фиолетовой форме с номерами 4 и 7",
    "стоят друг напротив друга и перебрасывают баскетбольный мяч точным пасом")

# 5. Бунинская аллея: тигрёнок-баскетболист бросает мяч в прыжке, полоски на хвосте
add("ibasket-lazareva-62", "d_tiger",
    hoop(98, 34, w=30)
    + f'<path d="M30 96 Q14 100 10 86" fill="none" stroke="#F5A33A" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M30 96 Q14 100 10 86" fill="none" {W(1.2)}/>'
    + f'<ellipse cx="46" cy="86" rx="20" ry="22" fill="#F5A33A" {W(3)}/>'
    + f'<path d="M34 76 l6 4 M32 88 l7 2 M58 76 l-6 4" {W(2.6)}/>'
    + limb("M38 104 L32 118", "#F5A33A", 7) + limb("M54 104 L60 116", "#F5A33A", 7)
    + limb("M58 74 L72 50", "#F5A33A", 7)
    + f'<circle cx="46" cy="52" r="18" fill="#F5A33A" {W(3)}/>'
    + f'<path d="M32 38 L30 28 L40 34Z M60 38 L62 28 L52 34Z" fill="#F5A33A" {W(2.4)}/>'
    + f'<path d="M46 36 v6 M38 38 l2 5 M54 38 l-2 5" {W(2.4)}/>'
    + f'<ellipse cx="46" cy="60" rx="9" ry="6" fill="#FFF3E0"/>'
    + face(46, 52, d=7, k=0.6)
    + ball(76, 40, 11, fc=False),
    "тигрёнок-баскетболист в полоску",
    "в прыжке бросает мяч одной лапой в кольцо со щитом, хвост закручен для равновесия")

# 6. Изюмская: ёжик несёт баскетбольный мяч, наколотый на иголки спины
add("ibasket-izyumskaya", "d_hedgehog",
    f'<rect x="-6" y="100" width="140" height="30" fill="#A6D46A" {W(2.6)}/>'
    + "".join(f'<path d="M{x} 100 l3 -7 l3 7" fill="#7FB84A" {W(1.6)}/>' for x in (8, 110))
    + f'<path d="M24 92 Q24 52 64 50 Q100 52 104 86 L96 80 L98 70 L88 72 L86 60 L76 66 L70 54 L62 64 L54 54 L48 66 L38 60 L36 72 L26 70 L30 82Z" fill="#7A5A44" {W(2.8)}/>'
    + f'<path d="M24 92 Q40 104 64 102 Q96 100 104 86 Q92 78 70 80 Q40 82 24 92Z" fill="#E8C49A" {W(2.8)}/>'
    + f'<circle cx="104" cy="88" r="3.5" fill="{O}"/>'
    + eye(88, 86, 0.6) + f'<ellipse cx="82" cy="94" rx="4" ry="2.2" fill="{PINK}" opacity=".6"/>'
    + limb("M44 100 L42 108", "#E8C49A", 4) + limb("M80 100 L82 108", "#E8C49A", 4)
    + ball(62, 34, 18, k=0.5),
    "ёжик",
    "топает по траве и несёт баскетбольный мяч, наколотый на иголки спины")

# 7. Конаковский (Водный стадион): мяч-ныряльщик в маске прыгает в кольцо, как в бассейн
add("ibasket-konakovsky", "d_dive",
    hoop(64, 82, w=46, board=False)
    + f'<path d="M40 112 q8 -6 16 0 t16 0 t16 0" fill="none" stroke="#fff" stroke-width="3"/>'
    + ball(64, 36, 20, fc=False)
    + f'<rect x="50" y="34" width="28" height="14" rx="6" fill="#9FE6FF" {W(2.6)}/>'
    + eye(58, 41, 0.6) + eye(70, 41, 0.6)
    + f'<path d="M78 38 L84 20" stroke="#FFE14D" stroke-width="5" stroke-linecap="round"/><path d="M78 38 L84 20" {W(1.4)}/>'
    + f'<circle cx="30" cy="30" r="4" fill="#fff" {W(1.8)}/><circle cx="22" cy="44" r="3" fill="#fff" {W(1.8)}/><circle cx="102" cy="28" r="3.5" fill="#fff" {W(1.8)}/>',
    "баскетбольный мяч-ныряльщик в маске с трубкой",
    "ныряет вниз головой прямо в кольцо с сеткой, как в бассейн, вокруг пузырьки")

# 8. Каширское ш.: панда жонглирует двумя баскетбольными мячами
add("ibasket-kashirskoe-116", "d_panda",
    f'<rect x="-6" y="110" width="140" height="20" fill="#D9B98A" {W(2.4)}/>'
    + f'<ellipse cx="64" cy="90" rx="26" ry="24" fill="#fff" {W(3)}/>'
    + limb("M50 108 L46 116", "#3A3550", 8) + limb("M78 108 L82 116", "#3A3550", 8)
    + limb("M42 80 L26 56", "#3A3550", 8) + limb("M86 80 L102 56", "#3A3550", 8)
    + f'<circle cx="64" cy="56" r="22" fill="#fff" {W(3)}/>'
    + f'<circle cx="46" cy="38" r="8" fill="#3A3550" {W(2.4)}/><circle cx="82" cy="38" r="8" fill="#3A3550" {W(2.4)}/>'
    + f'<ellipse cx="56" cy="56" rx="6" ry="8" fill="#3A3550"/><ellipse cx="72" cy="56" rx="6" ry="8" fill="#3A3550"/>'
    + f'<circle cx="56" cy="55" r="2" fill="#fff"/><circle cx="72" cy="55" r="2" fill="#fff"/>'
    + f'<ellipse cx="64" cy="64" rx="3.5" ry="2.5" fill="{O}"/><path d="M60 69 Q64 72 68 69" fill="none" {W(2)}/>'
    + ball(22, 42, 12, fc=False) + ball(106, 28, 12, fc=False)
    + f'<path d="M30 24 Q64 -4 98 14" fill="none" stroke="#fff" stroke-width="2.6" stroke-dasharray="4 4"/>',
    "панда-баскетболистка",
    "жонглирует двумя баскетбольными мячами, перекидывая их дугой над головой")

# 9. Воронежская: динозаврик с короткими лапками не дотягивается до мяча, застрявшего на кольце
add("ibasket-voronezhskaya", "d_dino",
    hoop(96, 34, w=28)
    + ball(96, 28, 10, fc=False)
    + f'<path d="M14 112 Q20 70 40 64 L42 40 Q44 22 62 22 Q80 24 78 40 Q76 52 62 54 L58 70 Q76 80 74 112Z" fill="#6CCB7A" {W(3)}/>'
    + f'<path d="M14 112 Q4 104 2 92" fill="none" stroke="#6CCB7A" stroke-width="8" stroke-linecap="round"/>'
    + f'<path d="M48 22 l4 -8 l4 8 M58 22 l4 -8 l4 8" fill="#4FA85E" {W(2)}/>'
    + eye(66, 36, 0.7) + f'<path d="M66 46 Q72 48 76 44" fill="none" {W(2.2)}/>'
    + limb("M60 74 L68 70", "#6CCB7A", 5)
    + f'<path d="M72 64 l4 -4 M78 66 l5 -2" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'
    + f'<text x="78" y="62" font-family="Arial" font-weight="bold" font-size="16" fill="{O}">?</text>'
    + f'<rect x="-6" y="112" width="140" height="20" fill="#C9A06A" {W(2.4)}/>',
    "зелёный динозаврик-тираннозавр с крошечными передними лапками",
    "стоит под кольцом, где застрял мяч, и растерянно не может до него дотянуться")

# 10. Капицы: морской котик крутит баскетбольный мяч на носу
add("ibasket-kapitsy", "d_seal",
    f'<rect x="-6" y="104" width="140" height="30" fill="#7FA0E8" {W(2.6)}/>'
    + f'<path d="M30 110 Q24 70 54 56 Q78 50 82 70 Q80 96 64 108 Q44 116 30 110Z" fill="#8A8F9E" {W(3)}/>'
    + f'<path d="M30 110 L14 118 L22 104Z M64 108 L80 116 L72 102Z" fill="#8A8F9E" {W(2.4)}/>'
    + f'<ellipse cx="68" cy="58" rx="16" ry="13" fill="#8A8F9E" {W(3)}/>'
    + eye(64, 56, 0.6) + eye(74, 54, 0.6)
    + f'<circle cx="82" cy="58" r="3" fill="{O}"/><path d="M78 62 l8 1 M78 64 l8 3" {W(1.4)}/>'
    + ball(86, 30, 16, k=0.45)
    + f'<path d="M66 22 Q62 30 66 36 M106 24 Q110 32 106 38" fill="none" stroke="#fff" stroke-width="2.6"/>',
    "морской котик",
    "сидит на краю бортика и крутит баскетбольный мяч на кончике носа")

# 11. Окская: лиса-баскетболистка ведёт мяч за спиной
add("ibasket-okskaya", "d_fox",
    floor(110, "#F2D2A2")
    + f'<path d="M30 80 Q8 86 6 66 Q20 74 32 70Z" fill="#F07A2C" {W(2.6)}/><path d="M6 66 Q10 74 16 74" fill="#fff"/>'
    + limb("M54 96 L44 114", "#F07A2C", 6) + limb("M66 96 L78 112", "#F07A2C", 6)
    + f'<path d="M44 98 Q42 66 60 60 Q78 66 76 98Z" fill="#2C9C8C" {W(2.8)}/>'
    + f'<text x="54" y="88" font-family="Arial" font-weight="bold" font-size="12" fill="#fff">11</text>'
    + limb("M46 70 Q34 88 42 102", "#F07A2C", 5)
    + ball(32, 104, 9, fc=False)
    + f'<path d="M60 36 L44 18 L46 40Z M64 36 L82 18 L80 40Z" fill="#F07A2C" {W(2.4)}/>'
    + f'<path d="M42 42 Q62 32 84 42 Q80 62 63 66 Q46 62 42 42Z" fill="#F07A2C" {W(3)}/>'
    + f'<path d="M52 56 Q63 68 74 56 Q68 64 63 64 Q58 64 52 56Z" fill="#fff"/>'
    + eye(55, 48, 0.55) + eye(71, 48, 0.55) + f'<circle cx="63" cy="58" r="2.6" fill="{O}"/>'
    + f'<path d="M20 98 q-4 -6 0 -10" fill="none" stroke="#fff" stroke-width="2.6"/>',
    "рыжая лиса-баскетболистка в бирюзовой форме с номером 11",
    "хитро ведёт мяч за спиной, обманывая невидимого защитника")

# 12. Лефортово: мяч-будильник со звонками на макушке подпрыгивает и звенит — пора на тренировку
add("ibasket-krasnokazarmennaya-11", "d_clock",
    f'<path d="M42 30 Q40 14 56 18Z M86 30 Q88 14 72 18Z" fill="#C9CED8" {W(2.6)}/>'
    + f'<path d="M58 22 L64 14 L70 22" fill="none" {W(2.6)}/>'
    + ball(64, 62, 32, fc=False)
    + f'<circle cx="64" cy="62" r="18" fill="#FFFBEA" {W(2.6)}/>'
    + f'<path d="M64 62 V50 M64 62 L72 66" {W(2.8)}/>'
    + eye(58, 70, 0.4) + eye(70, 70, 0.4)
    + limb("M44 92 L38 104", "#C9CED8", 5) + limb("M84 92 L90 104", "#C9CED8", 5)
    + f'<path d="M20 26 l-8 -4 M18 36 l-10 0 M108 26 l8 -4 M110 36 l10 0" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>'
    + f'<path d="M30 112 h68" stroke="{O}" stroke-width="2.6" stroke-dasharray="6 6"/>',
    "баскетбольный мяч-будильник со стрелками и двумя звонками на макушке",
    "подпрыгивает на ножках и громко звенит — пора на тренировку")

# 13. Белореченская: обезьянка висит на кольце, зацепившись хвостом, и держит мяч
add("ibasket-belorechenskaya", "d_monkey",
    f'<rect x="34" y="6" width="60" height="30" rx="4" fill="#fff" {W(3)}/>'
    + f'<ellipse cx="64" cy="40" rx="18" ry="4" fill="none" stroke="{RED}" stroke-width="4"/>'
    + f'<path d="M80 40 Q96 44 90 56 Q84 66 76 62" fill="none" stroke="#8A5A3C" stroke-width="5" stroke-linecap="round"/>'
    + f'<ellipse cx="66" cy="74" rx="14" ry="16" fill="#8A5A3C" {W(3)}/>'
    + f'<circle cx="64" cy="98" r="15" fill="#8A5A3C" {W(3)}/>'
    + f'<ellipse cx="64" cy="102" rx="10" ry="8" fill="#F2CFA0"/>'
    + f'<circle cx="48" cy="96" r="5" fill="#F2CFA0" {W(2.2)}/><circle cx="80" cy="96" r="5" fill="#F2CFA0" {W(2.2)}/>'
    + eye(59, 100, 0.5) + eye(69, 100, 0.5) + f'<path d="M60 106 Q64 108 68 106" fill="none" {W(2)}/>'
    + limb("M56 84 L36 90", "#8A5A3C", 5) + ball(28, 92, 12, fc=False)
    + limb("M72 86 L86 104", "#8A5A3C", 5),
    "коричневая обезьянка",
    "висит вниз головой на баскетбольном кольце, зацепившись хвостом, и протягивает мяч")

# 14. Кошкина (Москворечье): енот в «маске» крадётся на цыпочках с мячом в лапах
add("ibasket-koshkina", "d_raccoon",
    floor(110, "#D9C6A0")
    + f'<path d="M86 96 Q110 92 112 74" fill="none" stroke="#9A9AAE" stroke-width="10" stroke-linecap="round"/>'
    + "".join(f'<path d="M{100+i*4} {92-i*6} l5 -3" stroke="#3A3550" stroke-width="4"/>' for i in range(3))
    + f'<ellipse cx="66" cy="88" rx="24" ry="18" fill="#9A9AAE" {W(3)}/>'
    + limb("M50 102 L44 112", "#9A9AAE", 5) + limb("M80 102 L86 112", "#9A9AAE", 5)
    + f'<circle cx="54" cy="56" r="20" fill="#9A9AAE" {W(3)}/>'
    + f'<path d="M38 42 L36 30 L46 38Z M70 42 L72 30 L62 38Z" fill="#9A9AAE" {W(2.4)}/>'
    + f'<path d="M36 54 Q54 44 72 54 Q70 62 62 60 Q54 56 46 60 Q38 62 36 54Z" fill="#3A3550"/>'
    + f'<circle cx="46" cy="55" r="2.6" fill="#fff"/><circle cx="62" cy="55" r="2.6" fill="#fff"/>'
    + f'<ellipse cx="54" cy="68" rx="8" ry="5" fill="#fff"/><circle cx="54" cy="66" r="2.4" fill="{O}"/>'
    + ball(84, 74, 12, fc=False) + limb("M70 80 L78 76", "#9A9AAE", 4)
    + f'<path d="M24 100 q3 -4 6 0 M14 92 q3 -4 6 0" fill="none" {W(1.8)}/>',
    "полосатохвостый енот с тёмной «маской» на глазах",
    "крадётся на цыпочках по площадке, прижимая к себе баскетбольный мяч — «я только поиграть»")

# 15. Нижегородская: табло-секундомер «24» на стойке щита отсчитывает время атаки
add("ibasket-nizhegorodskaya-67", "d_shot",
    f'<rect x="58" y="70" width="12" height="60" fill="#8C93A8" {W(2.6)}/>'
    + f'<rect x="22" y="14" width="84" height="56" rx="10" fill="#1E2030" {W(3)}/>'
    + f'<text x="34" y="56" font-family="Arial" font-weight="bold" font-size="36" fill="#FF5A4A">24</text>'
    + f'<circle cx="94" cy="24" r="4" fill="#7CFF8A"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1.6" fill="#fff"/>' for x, y in [(14, 90), (24, 104), (112, 12), (8, 30)])
    + ball(100, 96, 14, fc=False)
    + f'<path d="M86 84 Q94 78 104 80" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 3"/>'
    + f'<rect x="-6" y="114" width="140" height="20" fill="#C98B4E" {W(2.4)}/>'
    + eye(44, 26, 0.5) + eye(84, 26, 0.5),
    "табло-секундомер атаки с красными цифрами «24»",
    "смотрит глазками с верхушки стойки ночью на пустую площадку, рядом отскакивает мяч")

# 16. Чоботовская: попугай ара держит мяч лапой и кричит
add("ibasket-chobotovskaya", "d_parrot",
    f'<path d="M10 92 H118" stroke="#8A5A3C" stroke-width="8" stroke-linecap="round"/><path d="M10 92 H118" {W(1.4)}/>'
    + f'<path d="M64 112 L56 130 L72 130Z" fill="#3E7BE0" {W(2.4)}/>'
    + f'<ellipse cx="62" cy="80" rx="18" ry="26" fill="#E8403A" {W(3)}/>'
    + f'<path d="M48 76 Q40 96 54 106 L60 86Z" fill="#FFD43A" {W(2.4)}/>'
    + f'<circle cx="64" cy="44" r="18" fill="#E8403A" {W(3)}/>'
    + f'<ellipse cx="70" cy="42" rx="8" ry="9" fill="#fff" {W(2)}/>' + eye(71, 42, 0.55)
    + f'<path d="M80 44 Q96 46 88 62 Q84 54 78 54Z" fill="#3A3550" {W(2.4)}/>'
    + ball(30, 70, 13, fc=False) + limb("M50 92 L36 80", "#8A8F9E", 3)
    + f'<path d="M94 26 l10 -6 M98 36 l12 -2 M96 46 l10 4" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>',
    "красный попугай ара",
    "сидит на жёрдочке, сжимает лапой баскетбольный мяч и громко кричит «Трёхочковый!»")

# 17. Олимпийская деревня: бегемотик-баскетболист в прыжке тянется к кольцу
add("ibasket-olimpiyskaya-derevnya", "d_hippo",
    hoop(92, 30, w=28)
    + ball(92, 22, 9, fc=False)
    + f'<ellipse cx="54" cy="80" rx="30" ry="24" fill="#B9A6E0" {W(3)}/>'
    + limb("M40 100 L34 114", "#B9A6E0", 8) + limb("M66 100 L72 112", "#B9A6E0", 8)
    + limb("M70 66 L84 42", "#B9A6E0", 7)
    + f'<ellipse cx="44" cy="54" rx="22" ry="18" fill="#B9A6E0" {W(3)}/>'
    + f'<ellipse cx="38" cy="62" rx="16" ry="10" fill="#D9CCF2" {W(2.4)}/>'
    + f'<circle cx="32" cy="62" r="2" fill="{O}"/><circle cx="44" cy="62" r="2" fill="{O}"/>'
    + f'<circle cx="34" cy="38" r="5" fill="#B9A6E0" {W(2.2)}/><circle cx="54" cy="38" r="5" fill="#B9A6E0" {W(2.2)}/>'
    + eye(40, 48, 0.5) + eye(52, 48, 0.5)
    + f'<path d="M20 118 h50" stroke="#fff" stroke-width="3" stroke-dasharray="6 6"/>',
    "сиреневый бегемотик",
    "отрывается от земли в тяжёлом, но гордом прыжке и тянет лапу к мячу на кольце")

# 18. Загорьевский: два мяча-близнеца качаются на доске-качалке
add("ibasket-zagoryevsky", "d_seesaw",
    f'<rect x="-6" y="108" width="140" height="24" fill="#9CCB6A" {W(2.4)}/>'
    + f'<path d="M64 82 L50 108 H78Z" fill="#5A8FD6" {W(2.8)}/>'
    + f'<rect x="12" y="76" width="104" height="9" rx="4" fill="#E86A4A" transform="rotate(-14 64 80)" {W(2.6)}/>'
    + ball(26, 70, 15, k=0.45) + ball(100, 46, 13, k=0.4)
    + f'<path d="M100 26 q-4 -8 2 -12 M108 30 q4 -6 10 -4" fill="none" stroke="#fff" stroke-width="2.4"/>',
    "два баскетбольных мяча-близнеца, большой и поменьше",
    "качаются на красной доске-качалке во дворе: один внизу, другой взлетел вверх")

# 19. Измайловский: мяч под зонтиком ждёт под дождём на уличной площадке
add("ibasket-izmaylovsky-115", "d_rain",
    "".join(f'<path d="M{x} {y} l-3 8" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'
            for x, y in [(14, 20), (30, 50), (110, 40), (100, 70), (20, 80), (118, 92), (12, 104)])
    + f'<path d="M30 52 Q64 10 98 52 Q90 46 81 52 Q72 46 64 52 Q56 46 47 52 Q38 46 30 52Z" fill="#FFD43A" {W(3)}/>'
    + f'<path d="M64 30 V86 Q64 94 56 92" fill="none" {W(3)}/>'
    + ball(64, 84, 20, k=0.55)
    + limb("M80 80 L68 64", ORG, 4)
    + f'<ellipse cx="64" cy="112" rx="36" ry="6" fill="#6E86A8" {W(2.2)}/>',
    "баскетбольный мяч-персонаж с жёлтым зонтом",
    "стоит в луже на уличной площадке под дождём и всё равно ждёт тренировку")

# 20. Героев Панфиловцев: такса-баскетболистка несёт мяч на длинной спине
add("ibasket-panfilovtsev-35", "d_dachs",
    floor(108, "#F2C99A")
    + f'<rect x="20" y="70" width="80" height="26" rx="13" fill="#A0582E" {W(3)}/>'
    + f'<path d="M20 78 Q8 74 6 64" fill="none" stroke="#A0582E" stroke-width="6" stroke-linecap="round"/>'
    + limb("M30 94 L30 106", "#A0582E", 6) + limb("M44 94 L44 106", "#A0582E", 6)
    + limb("M80 94 L80 106", "#A0582E", 6) + limb("M92 94 L94 106", "#A0582E", 6)
    + f'<ellipse cx="104" cy="66" rx="16" ry="13" fill="#A0582E" {W(3)}/>'
    + f'<path d="M100 56 Q88 60 92 80 Q100 74 100 62Z" fill="#7A3E1E" {W(2.4)}/>'
    + f'<circle cx="120" cy="70" r="3.2" fill="{O}"/>' + eye(108, 62, 0.55)
    + f'<rect x="54" y="66" width="22" height="8" rx="3" fill="#2C9CD8" {W(2)}/>'
    + ball(64, 50, 16, k=0.45),
    "длинная такса-баскетболистка в синей повязке",
    "аккуратно несёт баскетбольный мяч, уложенный на её длинную спину, через всю площадку")

# 21. Монаховой (Коммунарка): дирижабль в виде баскетбольного мяча летит над новыми домами
add("ibasket-monakhovoy", "d_airship",
    f'<path d="M-6 130 V96 H18 V82 H40 V104 H58 V76 H82 V100 H100 V88 H134 V130Z" fill="#F2F5FA" {W(2.6)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="6" height="6" fill="#9FD3F5"/>' for x, y in [(24, 88), (64, 82), (64, 94), (106, 94), (46, 108)])
    + f'<ellipse cx="62" cy="40" rx="40" ry="22" fill="{ORG}" {W(3)}/>'
    + f'<path d="M22 40 H102 M62 18 V62" fill="none" {W(2.2)}/>'
    + f'<path d="M40 22 Q50 40 40 58 M84 22 Q74 40 84 58" fill="none" {W(2.2)}/>'
    + f'<path d="M100 32 L114 22 L112 40 L114 58 L100 48" fill="#FF6B6B" {W(2.4)}/>'
    + f'<rect x="50" y="64" width="24" height="10" rx="4" fill="#fff" {W(2.4)}/>'
    + f'<path d="M54 62 v2 M70 62 v2" {W(2)}/>'
    + eye(48, 44, 0.5) + eye(62, 44, 0.5),
    "дирижабль в виде баскетбольного мяча с гондолой",
    "плывёт по небу над новыми многоэтажками Коммунарки")

# 22. Новочерёмушкинская: мяч-капитан с повязкой «К» зовёт команду в рупор
add("ibasket-novocheryomushkinskaya-48", "d_captain",
    ball(52, 70, 30, fc=False)
    + f'<rect x="22" y="64" width="12" height="16" rx="2" fill="#fff" {W(2.2)}/>'
    + f'<text x="24" y="77" font-family="Arial" font-weight="bold" font-size="12" fill="{RED}">К</text>'
    + eye(44, 66, 0.6) + eye(60, 66, 0.6)
    + f'<path d="M44 80 Q52 88 60 80Z" fill="#7A2A2A" {W(2)}/>'
    + f'<path d="M76 62 L104 46 L104 92 L76 78Z" fill="#fff" {W(3)}/>'
    + f'<rect x="70" y="62" width="10" height="16" rx="3" fill="#FFC93C" {W(2.4)}/>'
    + f'<path d="M110 54 q8 15 0 30 M116 48 q12 21 0 42" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    + limb("M40 98 L36 112", ORG, 5) + limb("M64 98 L68 112", ORG, 5),
    "баскетбольный мяч-капитан с повязкой «К»",
    "кричит в белый рупор, созывая всю команду на площадку")

# 23. Барышиха (Митино): уличное кольцо на двери гаража на закате
add("ibasket-baryshikha-42", "d_garage",
    f'<circle cx="96" cy="86" r="22" fill="#FFD25A" opacity=".9"/>'
    + f'<rect x="14" y="44" width="76" height="70" fill="#8C93A8" {W(3)}/>'
    + f'<path d="M8 46 L52 22 L96 46Z" fill="#5A607A" {W(3)}/>'
    + f'<rect x="24" y="66" width="56" height="48" fill="#C9CED8" {W(2.6)}/>'
    + "".join(f'<path d="M24 {72+i*8} H80" {W(1.4)}/>' for i in range(5))
    + f'<rect x="38" y="34" width="28" height="20" rx="2" fill="#fff" {W(2.4)}/>'
    + f'<ellipse cx="52" cy="56" rx="10" ry="3" fill="none" stroke="{RED}" stroke-width="3.4"/>'
    + f'<path d="M43 56 L46 66 H58 L61 56" fill="none" {W(1.6)}/>'
    + ball(106, 40, 11)
    + f'<rect x="-6" y="114" width="140" height="20" fill="#7A5A44" {W(2.4)}/>',
    "старое баскетбольное кольцо, прибитое над дверью гаража",
    "ждёт игроков на закате, а мяч-персонаж весело летит к нему со стороны солнца")

# 24. Немчинова (Тимирязевская): краб держит мяч клешнями и бочком несёт к кольцу
add("ibasket-nemchinova", "d_crab",
    f'<rect x="-6" y="100" width="140" height="34" fill="#F2DC9A" {W(2.6)}/>'
    + f'<path d="M12 112 q6 -4 12 0 M96 118 q6 -4 12 0" fill="none" stroke="#fff" stroke-width="2.4"/>'
    + limb("M44 92 L28 106", "#E8553A", 4) + limb("M48 96 L38 110", "#E8553A", 4)
    + limb("M84 92 L100 106", "#E8553A", 4) + limb("M80 96 L90 110", "#E8553A", 4)
    + f'<ellipse cx="64" cy="84" rx="28" ry="18" fill="#E8553A" {W(3)}/>'
    + f'<path d="M56 70 V58 M72 70 V58" {W(2.6)}/>' + eye(56, 56, 0.55) + eye(72, 56, 0.55)
    + f'<path d="M58 90 Q64 94 70 90" fill="none" {W(2.2)}/>'
    + limb("M40 80 L26 60", "#E8553A", 5) + limb("M88 80 L102 60", "#E8553A", 5)
    + ball(64, 30, 18, fc=False)
    + f'<path d="M22 58 Q30 40 44 34 L40 46Z M106 58 Q98 40 84 34 L88 46Z" fill="#E8553A" {W(2.4)}/>',
    "красный краб",
    "держит над головой баскетбольный мяч двумя клешнями и бочком несёт его по песку")

# ============================== ТАНЦЫ ==============================
# 25. «Джигит.ру» (Мытищи): мальчик в черкеске танцует лезгинку на носочках
add("djigit-mytishchi-yauza", "d_lezgi",
    f'<rect x="-6" y="112" width="140" height="20" fill="#E8C08A" {W(2.4)}/>'
    + limb("M58 90 L52 112", "#2A2230", 6) + limb("M70 90 L76 112", "#2A2230", 6)
    + f'<path d="M48 112 h8 M74 112 h8" stroke="#2A2230" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M48 94 Q46 56 64 52 Q82 56 80 94 L74 92 L64 98 L54 92Z" fill="#2A2230" {W(2.8)}/>'
    + "".join(f'<rect x="{x}" y="60" width="3" height="10" fill="#E8C060" {W(1)}/>' for x in (52, 56, 70, 74))
    + limb("M50 60 L22 48", "#2A2230", 6) + limb("M78 60 L106 46", "#2A2230", 6)
    + f'<circle cx="64" cy="40" r="11" fill="{SKIN}" {W(2.6)}/>' + face(64, 41, d=4, k=0.4)
    + f'<path d="M52 34 Q50 16 64 16 Q78 16 76 34Z" fill="#F2F0EA" {W(2.6)}/>'
    + "".join(f'<path d="M{x} 20 q2 3 0 6" fill="none" {W(1.2)}/>' for x in (56, 62, 68, 74))
    + f'<path d="M14 40 l-6 -6 M114 38 l6 -6" stroke="#fff" stroke-width="3" stroke-linecap="round"/>',
    "мальчик в чёрной черкеске с газырями и белой папахе",
    "танцует лезгинку на самых носочках, широко раскинув руки в стороны")

# ============================== ШАХМАТЫ ==============================
# 26. Опалиха: ферзь-садовница поливает из лейки клумбу-шахматную доску
_board = "".join(f'<rect x="{14+i*12}" y="{100+j*10}" width="12" height="10" fill="{"#6E4A30" if (i+j)%2 else "#F4E2C2"}"/>'
                 for i in range(8) for j in range(3))
add("kurchatov-chess-opalikha", "d_garden",
    _board + f'<rect x="14" y="100" width="96" height="30" fill="none" {W(2.6)}/>'
    + "".join(f'<path d="M{x} 100 V88" stroke="#3E9A4A" stroke-width="3"/><circle cx="{x}" cy="86" r="5" fill="{c}" {W(1.8)}/>'
              for x, c in [(26, "#FF7FA8"), (50, "#FFD43A"), (98, "#B48BF0")])
    + G(78, 98, queen(WHITE, sc=0.62))
    + f'<path d="M58 48 L38 48 L34 64 L58 64Z" fill="#7FC4F0" {W(2.6)}/>'
    + f'<path d="M38 52 L18 40" stroke="#7FC4F0" stroke-width="5" stroke-linecap="round"/><path d="M38 52 L18 40" {W(1.4)}/>'
    + f'<path d="M58 52 Q66 46 64 58" fill="none" {W(2.4)}/>'
    + "".join(f'<path d="M{16+i*4} {44+i*6} l-2 6" stroke="#3E9AE0" stroke-width="2.4" stroke-linecap="round"/>' for i in range(4)),
    "белый шахматный ферзь-садовница",
    "поливает из голубой лейки цветочную клумбу, растущую прямо на шахматной доске")

# 27. «БэбиБосс»: пешка-малыш в галстуке за огромным начальственным столом
add("kurchatov-chess-babyboss", "d_boss",
    f'<rect x="14" y="82" width="100" height="14" rx="3" fill="#7A4A2E" {W(3)}/>'
    + f'<rect x="20" y="96" width="14" height="30" fill="#7A4A2E" {W(2.6)}/><rect x="94" y="96" width="14" height="30" fill="#7A4A2E" {W(2.6)}/>'
    + f'<path d="M40 82 V30 Q64 18 88 30 V82" fill="#2F2A40" {W(3)}/>'
    + G(64, 84, pawn(WHITE, sc=0.72))
    + f'<path d="M60 58 L64 62 L68 58 L66 74 L64 76 L62 74Z" fill="{RED}" {W(1.8)}/>'
    + f'<rect x="88" y="70" width="18" height="12" rx="2" fill="#fff" {W(2.2)}/>'
    + G(26, 82, knight(BLACK, sc=0.22)),
    "пешка-малыш в красном галстуке",
    "важно сидит в огромном кожаном кресле начальника за большим деревянным столом")

# ============================== БАССЕЙН ==============================
# 28. «Аквакласс» (ВДНХ): малыш в нарукавниках плывёт за надувной ракетой
add("aqua-class-koroleva", "d_rocketpool",
    f'<rect x="-6" y="70" width="140" height="70" fill="#5CC4F0" {W(2.6)}/>'
    + f'<path d="M-6 72 q10 -6 20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0" fill="none" stroke="#fff" stroke-width="3"/>'
    + G(92, 62, f'<path d="M0 -26 C10 -18 12 0 8 18 H-8 C-12 0 -10 -18 0 -26Z" fill="#fff" {W(2.6)}/>'
               f'<circle cx="0" cy="-4" r="5" fill="#9ED8FF" {W(2)}/>'
               f'<path d="M-8 10 L-16 22 L-6 18Z M8 10 L16 22 L6 18Z" fill="{RED}" {W(2)}/>', rot=60)
    + head(42, 70, hair="#F2C14E", r=14, k=0.5)
    + f'<rect x="16" y="76" width="12" height="12" rx="6" fill="#FF8A3C" {W(2.4)}/><rect x="56" y="76" width="12" height="12" rx="6" fill="#FF8A3C" {W(2.4)}/>'
    + f'<circle cx="20" cy="50" r="3" fill="#fff" {W(1.6)}/><circle cx="66" cy="44" r="2.5" fill="#fff" {W(1.6)}/>',
    "малыш-«космонавт» в оранжевых нарукавниках",
    "плывёт по бассейну за надувной бело-красной ракетой, как настоящий космонавт")

# ============================== ФЕХТОВАНИЕ ==============================
# 29. SportVille: кот-мушкетёр в шляпе с пером делает выпад рапирой
add("flash-fencing-sportville", "d_musket",
    f'<rect x="-6" y="112" width="140" height="20" fill="#C9A06A" {W(2.4)}/>'
    + f'<path d="M30 100 Q10 96 12 80" fill="none" stroke="#9A9AAE" stroke-width="6" stroke-linecap="round"/>'
    + limb("M40 96 L24 112", "#9A9AAE", 6) + limb("M52 96 L66 112", "#9A9AAE", 6)
    + f'<path d="M32 98 Q30 64 46 60 Q60 64 60 98Z" fill="#3E5FC0" {W(2.8)}/>'
    + f'<path d="M40 66 L46 76 L52 66" fill="none" stroke="#fff" stroke-width="2.6"/>'
    + limb("M56 72 L80 66", "#9A9AAE", 5)
    + f'<path d="M80 66 L124 54" stroke="#C9CED8" stroke-width="3" stroke-linecap="round"/><path d="M80 66 L124 54" {W(1)}/>'
    + f'<path d="M78 60 Q86 64 80 72" fill="none" stroke="{GOLD}" stroke-width="3.4"/>'
    + f'<circle cx="46" cy="46" r="15" fill="#9A9AAE" {W(2.8)}/>'
    + f'<path d="M34 38 L32 26 L42 34Z M58 38 L60 26 L50 34Z" fill="#9A9AAE" {W(2.2)}/>'
    + face(46, 46, d=5.5, k=0.5)
    + f'<path d="M26 32 Q46 18 66 30 Q46 30 26 32Z" fill="#3A3550" {W(2.4)}/>'
    + f'<path d="M58 26 Q74 6 84 16 Q72 18 62 28" fill="#FF7FA8" {W(2)}/>',
    "серый кот-мушкетёр в синем плаще и шляпе с розовым пером",
    "делает изящный выпад длинной рапирой на фехтовальной дорожке")

# 30. AirArena: рапира-персонаж с гардой-чашкой отдаёт фехтовальный салют
add("flash-fencing-airarena", "d_salute",
    f'<rect x="-6" y="114" width="140" height="18" fill="#B9A6E0" {W(2.4)}/>'
    + f'<path d="M64 10 L64 74" stroke="#E4E8F0" stroke-width="6" stroke-linecap="round"/><path d="M64 10 L64 74" {W(1.4)}/>'
    + f'<path d="M40 74 Q64 100 88 74Z" fill="#E8C060" {W(3)}/>'
    + face(64, 82, d=8, k=0.55)
    + f'<rect x="60" y="92" width="8" height="18" rx="3" fill="#5A3A28" {W(2.4)}/>'
    + limb("M44 82 L28 70", "#E8C060", 4) + limb("M84 82 L100 94", "#E8C060", 4)
    + sparkle(30, 30, 6) + sparkle(98, 26, 5) + sparkle(104, 58, 3.5),
    "рапира-персонаж с золотой гардой-чашкой и глазками",
    "стоит клинком вверх и отдаёт фехтовальный салют перед боем, вокруг искорки")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for pid, code in ICONS.items():
        open(os.path.join(OUT, pid + ".svg"), "w").write(code)
    reg = os.path.join(OUT, "subjects.txt")
    lines = [l for l in open(reg, encoding="utf-8") if l.split(" — ", 1)[0] not in SUBJ]
    lines += [line + "\n" for line in SUBJ.values()]
    open(reg, "w", encoding="utf-8").writelines(lines)
    print(len(ICONS), "иконок:", " ".join(ICONS))
