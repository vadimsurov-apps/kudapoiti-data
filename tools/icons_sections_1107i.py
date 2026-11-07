"""Иконки робота sections, 2026-11-07 (21 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно.
Бассейны «Китёнок» в Подмосковье и новых ЖК — НЕ серия: у каждого филиала свой герой, своя сцена, своя палитра фона
(тукан-лейка, бабушка в шапочке с цветами, цапля на одной ноге, аист со свёртком, карп кои, пришелец в тарелке,
спасательный круг, коала на бортике, тритон, единорог, стрекоза, овечка-облако, подводная лодка, капельки, верблюжонок,
ослик, львёнок под душем, двойняшки, ньюфаундленд, гребешок с жемчужиной, дедушка-тренер, рыба-меч, бабочка-баттерфляй,
мокрый бассейн-ромашка).
Сверено с листами icons-catalog и icons-src/subjects.txt (бегемоты, пеликан, морской конёк, утконос, головастик,
морская звезда, панда, слон, такса, лемур, кенгуру, белые медвежата, капибары, кувшинки — уже заняты, не берём).
Запуск: python3 tools/icons_sections_1107i.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O
from icons_sections_1107d import kid, G, W, PINK, GOLD, RED, ORG

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
SKIN = "#FFD8B8"
draw_icons.BG.update({
    "mango": ("#FFF0C9", "#FF9F45"),
    "lilac": ("#F3E6FF", "#C08BE8"),
    "deepsea": ("#BFF3E6", "#2E9C8E"),
    "mint": ("#E8FFF2", "#86DDB0"),
    "lemon": ("#FFFDE0", "#E8E05A"),
    "sand": ("#FFF1D6", "#E6B877"),
    "coral": ("#FFE3DC", "#FF8C7A"),
    "rose": ("#FFE8F3", "#E98AC0"),
    "steel": ("#E2ECF7", "#7F9DC4"),
    "peach": ("#FFEADF", "#F7A68A"),
    "aqua": ("#D9FBFF", "#3FC3D8"),
    "olive": ("#F0F6D8", "#A9C25C"),
    "berry": ("#F7DDF0", "#B05C9E"),
    "dusk": ("#FFD9C2", "#8D6CC0"),
    "ice": ("#F2FBFF", "#B5D8F0"),
})


def add(pid, bg, body, hero, scene):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def water(y, c="#5CB7F2", amp=4, n=4, edge="#3E8FD8"):
    step = 140 / n
    d = f"M-6 {y}" + "".join(f" q{step/4:.1f} {-amp} {step/2:.1f} 0 t{step/2:.1f} 0" for _ in range(n)) + " V134 H-6Z"
    return f'<path d="{d}" fill="{c}" stroke="{edge}" stroke-width="2.6"/>'


def bubbles(pts, c="#fff"):
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{c}" stroke-width="2"/>' for x, y, r in pts)


def drops(pts, c="#7FD0F5"):
    return "".join(f'<path d="M{x} {y-6} Q{x+4} {y} {x} {y+3} Q{x-4} {y} {x} {y-6}Z" fill="{c}" {W(1.6)}/>' for x, y in pts)


def edge(y, c="#F4F1EA", line="#CFC8BA"):
    """кафельный бортик бассейна шириной во весь круг"""
    return (f'<rect x="-6" y="{y}" width="140" height="10" fill="{c}" {W(2.4)}/>'
            + "".join(f'<path d="M{x} {y} V{y+10}" stroke="{line}" stroke-width="1.4"/>' for x in range(4, 130, 12)))


def capkid(x, y, cap, sc=1.0, skin=SKIN, closed=False):
    """голова малыша в плавательной шапочке, центр (x,y)"""
    g = (f'<circle cx="0" cy="0" r="14" fill="{skin}" {W(2.8)}/>'
         f'<path d="M-14 -1 Q-14 -17 0 -17 Q14 -17 14 -1 Q0 -6 -14 -1Z" fill="{cap}" {W(2.6)}/>'
         + (f'<path d="M-8 3 q3 -3 6 0 M2 3 q3 -3 6 0" fill="none" {W(2)}/>' if closed else face(0, 3, d=5, k=0.5))
         + f'<path d="M-3 9 Q0 12 3 9" fill="none" {W(1.8)}/>')
    return G(x, y, g, sc=sc)


# 1. «Метрополия»: тукан черпает клювом воду и поливает малыша, как из лейки
add("kitenok-metropoliya", "mango",
    water(84, "#4FB6E8")
    + edge(74)
    + capkid(92, 98, "#4FBF6B")
    + f'<path d="M32 74 Q22 50 34 32 Q46 20 58 30 Q64 42 60 74Z" fill="#2E2A36" {W(3)}/>'
    + f'<path d="M40 50 Q48 44 56 50 Q54 62 46 64 Q40 60 40 50Z" fill="#FFF3D6" {W(2.2)}/>'
    + f'<path d="M56 34 Q90 26 104 46 Q96 56 80 52 Q64 48 56 46Z" fill="#FFB02E" {W(3)}/>'
    + f'<path d="M58 44 Q80 46 102 48" fill="none" {W(2)}/>'
    + f'<path d="M96 40 Q104 44 104 46 Q100 48 96 46Z" fill="{RED}" {W(1.6)}/>'
    + f'<circle cx="49" cy="38" r="7" fill="#9EE07A" {W(2.4)}/>' + eye(50, 38, 0.8)
    + f'<path d="M36 74 V80 M46 74 V80" fill="none" stroke="#7A8798" stroke-width="3.4"/>'
    + drops([(100, 62), (92, 68), (106, 74)], "#9FDFFF"),
    "чёрный тукан с огромным жёлто-оранжевым клювом",
    "сидит на бортике и льёт с клюва воду, как из лейки, на малыша в зелёной шапочке")

# 2. «Мещерский лес»: бабушка в шапочке с резиновыми цветами плывёт брассом
add("kitenok-meshchersky-les", "olive",
    water(70, "#62C3EA", amp=3)
    + f'<path d="M14 92 Q34 80 54 92" fill="none" stroke="#fff" stroke-width="3"/>'
    + G(60, 70, f'<circle cx="0" cy="0" r="22" fill="{SKIN}" {W(3)}/>'
        + f'<path d="M-22 -2 Q-22 -26 0 -26 Q22 -26 22 -2 Q0 -10 -22 -2Z" fill="#FFFFFF" {W(2.8)}/>'
        + "".join(f'<g transform="translate({x} {y})">' + "".join(
            f'<ellipse cx="{4*math.cos(a):.1f}" cy="{4*math.sin(a):.1f}" rx="4" ry="2.6" transform="rotate({math.degrees(a):.0f} {4*math.cos(a):.1f} {4*math.sin(a):.1f})" fill="{c}" {W(1.2)}/>'
            for a in [i * 1.2566 for i in range(5)]) + f'<circle r="2.4" fill="{GOLD}"/></g>'
            for x, y, c in [(-12, -18, "#FF8FB8"), (2, -23, "#9C7BF0"), (14, -16, "#FFB02E")])
        + f'<circle cx="-8" cy="2" r="6.5" fill="none" {W(2.2)}/><circle cx="8" cy="2" r="6.5" fill="none" {W(2.2)}/>'
        + f'<path d="M-1.5 2 H1.5" {W(2)}/>' + eye(-8, 2, 0.6) + eye(8, 2, 0.6)
        + f'<path d="M-5 12 Q0 16 5 12" fill="none" {W(2.2)}/>'
        + f'<ellipse cx="-15" cy="10" rx="3.6" ry="2" fill="{PINK}" opacity=".6"/><ellipse cx="15" cy="10" rx="3.6" ry="2" fill="{PINK}" opacity=".6"/>')
    + f'<path d="M32 82 Q14 74 8 84 M88 82 Q106 74 112 84" fill="none" stroke="{SKIN}" stroke-width="8" stroke-linecap="round"/>'
    + f'<path d="M32 82 Q14 74 8 84 M88 82 Q106 74 112 84" fill="none" {W(1.4)}/>'
    + f'<path d="M6 76 q6 -6 12 0 M104 76 q6 -6 12 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>',
    "бабушка в белой резиновой шапочке с цветами и в очках",
    "плывёт брассом прямо на нас, разводя руками волны, голова над водой")

# 3. «Сиреневый парк»: цапля на одной ноге в лягушатнике, малыш повторяет позу
add("kitenok-sirenevy-park", "lilac",
    water(92, "#8FD6F2", amp=2, n=5)
    + f'<path d="M44 92 V60 M44 74 L54 66" stroke="#E07A5F" stroke-width="3.4" stroke-linecap="round"/>'
    + f'<path d="M44 92 V60 M44 74 L54 66" fill="none" stroke="{O}" stroke-width="1"/>'
    + f'<path d="M22 60 Q24 40 46 40 Q64 42 60 58 Q50 66 30 64Z" fill="#FFB3CF" {W(3)}/>'
    + f'<path d="M26 54 Q20 64 14 66 Q24 66 32 60" fill="#F58CB8" {W(2.4)}/>'
    + f'<path d="M52 42 Q60 26 54 18" fill="none" stroke="#FFB3CF" stroke-width="9" stroke-linecap="round"/>'
    + f'<path d="M52 42 Q60 26 54 18" fill="none" {W(1.4)}/>'
    + f'<circle cx="54" cy="16" r="9" fill="#FFB3CF" {W(2.8)}/>'
    + f'<path d="M62 14 L84 19 L62 20Z" fill="#FFB02E" {W(2.2)}/>' + eye(55, 14, 0.7)
    + G(94, 68, kid(shirt="#9C7BF0", hair="#4A3328", girl=True), sc=0.8)
    + f'<path d="M94 92 V114 M94 100 L104 94" stroke="{SKIN}" stroke-width="6" stroke-linecap="round"/>'
    + f'<path d="M80 70 L66 60 M108 70 L122 60" stroke="{SKIN}" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M80 108 q14 -5 28 0" fill="none" stroke="#fff" stroke-width="3"/>',
    "розовая цапля с жёлтым клювом",
    "стоит на одной ноге в лягушатнике, а девочка рядом старательно повторяет позу")

# 4. Никольские Луга: аист несёт к бассейну свёрток-малыша в шапочке
add("kitenok-nikolskie-luga", "sky",
    water(100, "#4FA8E0", amp=3, n=5)
    + f'<path d="M14 64 Q44 36 74 44 L98 50 Q90 66 70 68 Q40 74 14 64Z" fill="#FFFFFF" {W(3)}/>'
    + f'<path d="M30 52 Q46 18 74 30 Q60 46 46 56Z" fill="#FFFFFF" {W(2.6)}/>'
    + f'<path d="M34 50 Q48 30 66 34" fill="none" stroke="#2E2A36" stroke-width="6" stroke-linecap="round"/>'
    + f'<path d="M14 64 L4 58 L6 70Z" fill="#2E2A36" {W(2)}/>'
    + f'<circle cx="96" cy="46" r="9" fill="#FFFFFF" {W(2.8)}/>' + eye(98, 44, 0.65)
    + f'<path d="M104 44 L124 52 L104 52Z" fill="{RED}" {W(2.2)}/>'
    + f'<path d="M118 52 L112 68" {W(2)}/>'
    + f'<path d="M98 64 Q112 60 124 66 Q122 84 110 86 Q96 84 98 64Z" fill="#FFE8A8" {W(2.6)}/>'
    + f'<path d="M110 62 Q118 52 118 52" fill="none" {W(2)}/>'
    + capkid(111, 74, "#4FBF6B", sc=0.55)
    + f'<path d="M40 70 L34 86 M56 70 L54 86" stroke="{RED}" stroke-width="3" stroke-linecap="round"/>',
    "белый аист с красным клювом",
    "летит над бассейном и несёт в клюве свёрток с малышом в зелёной шапочке")

# 5. «Деснаречье»: карп кои выпрыгивает дугой над бортиком
add("kitenok-desnarechye", "deepsea",
    water(88, "#2F8FC4", amp=4, n=4, edge="#1E6A9A")
    + G(64, 60, f'<path d="M-42 14 Q-30 -26 10 -26 Q36 -24 42 -6 Q30 12 4 12 Q-20 14 -42 14Z" fill="#FFFFFF" {W(3)}/>'
        + f'<path d="M-20 -14 Q-10 -24 4 -20 Q0 -8 -14 -6Z" fill="#F0552E"/>'
        + f'<path d="M10 -24 Q24 -20 26 -8 Q14 -6 10 -14Z" fill="#F0552E"/>'
        + f'<path d="M-6 4 Q2 -2 14 4 Q6 10 -6 4Z" fill="#FFB02E"/>'
        + f'<path d="M-42 14 L-58 -2 Q-54 12 -62 26Z" fill="#F0552E" {W(2.6)}/>'
        + f'<path d="M-10 -24 Q0 -38 10 -24" fill="#F0552E" {W(2.4)}/>'
        + f'<circle cx="28" cy="-10" r="5.5" fill="#fff" {W(2)}/>' + eye(28, -10, 0.7)
        + f'<path d="M40 -4 Q46 2 52 0 M40 -2 Q44 6 50 8" fill="none" {W(1.8)}/>'
        + f'<path d="M34 4 Q38 7 42 4" fill="none" {W(2)}/>', rot=-14)
    + drops([(18, 84), (30, 76), (100, 80), (110, 70)], "#BFF3FF")
    + f'<ellipse cx="22" cy="92" rx="14" ry="4" fill="none" stroke="#fff" stroke-width="2.4"/>'
    + f'<ellipse cx="106" cy="92" rx="14" ry="4" fill="none" stroke="#fff" stroke-width="2.4"/>',
    "бело-красный карп кои с усиками",
    "выпрыгивает высокой дугой из воды бассейна, роняя капли с хвоста")

# 6. «Спутник»: зелёный пришелец в шапочке плавает в своей летающей тарелке, как в круге
add("kitenok-sputnik", "night",
    water(84, "#3A7FD0", amp=3, n=4, edge="#2A5AA0")
    + "".join(sparkle(x, y, r, "#FFF6C4") for x, y, r in [(20, 30, 5), (106, 24, 4), (90, 44, 3), (30, 52, 3)])
    + f'<ellipse cx="64" cy="86" rx="46" ry="13" fill="#B9C3D6" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="88" r="3" fill="{GOLD}" {W(1.4)}/>' for x in (32, 48, 64, 80, 96))
    + f'<path d="M40 82 Q40 52 64 50 Q88 52 88 82Z" fill="#CFF3FF" opacity=".75" {W(2.6)}/>'
    + f'<ellipse cx="64" cy="68" rx="15" ry="14" fill="#8EE07A" {W(2.8)}/>'
    + f'<path d="M50 64 Q50 50 64 50 Q78 50 78 64 Q64 58 50 64Z" fill="{RED}" {W(2.4)}/>'
    + f'<path d="M56 52 L50 38 M72 52 L78 38" {W(2.4)}/>'
    + f'<circle cx="50" cy="36" r="3.6" fill="{GOLD}" {W(1.8)}/><circle cx="78" cy="36" r="3.6" fill="{GOLD}" {W(1.8)}/>'
    + face(64, 70, d=6, k=0.6)
    + f'<path d="M20 100 q8 -5 16 0 M92 102 q8 -5 16 0" fill="none" stroke="#fff" stroke-width="3"/>',
    "зелёный малыш-инопланетянин с антенками в красной плавательной шапочке",
    "плавает по ночному бассейну внутри своей летающей тарелки, как в надувном круге")

# 7. Долгопрудный: спасательный круг шлёпнулся в воду, малыш за него схватился
add("kitenok-dolgoprudny", "lemon",
    water(64, "#3EA6E6", amp=4, n=4)
    + f'<path d="M64 6 Q74 30 70 52" fill="none" stroke="#C9A06A" stroke-width="4" stroke-dasharray="6 3"/>'
    + G(64, 84, f'<circle r="34" fill="#FFFFFF" {W(3.2)}/>'
        + "".join(f'<path d="M0 0 L{34*math.cos(a):.1f} {34*math.sin(a):.1f} A34 34 0 0 1 {34*math.cos(a+0.785):.1f} {34*math.sin(a+0.785):.1f}Z" fill="#FF6A3D"/>'
                  for a in [i * 1.5708 - 0.39 for i in range(4)])
        + f'<circle r="34" fill="none" {W(3.2)}/>'
        + f'<circle r="15" fill="#3EA6E6" {W(3)}/>'
        + face(0, -24, d=8, k=0.6))
    + capkid(64, 82, "#FFC93C", sc=0.85)
    + f'<path d="M40 70 Q36 62 44 58 M88 70 Q92 62 84 58" fill="none" stroke="{SKIN}" stroke-width="6" stroke-linecap="round"/>'
    + f'<path d="M14 58 l-6 -8 M114 58 l6 -8 M22 52 l-2 -10 M106 52 l2 -10" stroke="#fff" stroke-width="3" stroke-linecap="round"/>',
    "оранжево-белый спасательный круг с верёвкой и улыбкой",
    "шлёпнулся в воду бассейна, а малыш в жёлтой шапочке радостно ухватился за него изнутри")

# 8. Селятино: коала в полосатом купальнике дремлет, обняв бортик, ножки в воде
add("kitenok-selyatino", "mint",
    f'<rect x="-6" y="62" width="140" height="72" fill="#5DC6EC"/>'
    + edge(52, "#EDE7DC")
    + f'<path d="M30 78 Q22 98 30 112 M98 78 Q106 98 98 112" fill="none" stroke="#9AA3AE" stroke-width="12" stroke-linecap="round"/>'
    + f'<path d="M30 78 Q22 98 30 112 M98 78 Q106 98 98 112" fill="none" {W(1.4)}/>'
    + f'<path d="M32 58 Q30 86 64 88 Q98 86 96 58Z" fill="#FFFFFF" {W(3)}/>'
    + "".join(f'<path d="M{34+i} {62+i*0} H{94}" stroke="#4FA8E0" stroke-width="4"/>' for i in (0,))
    + f'<path d="M33 64 H95 M34 72 H94 M38 80 H90" stroke="#4FA8E0" stroke-width="4"/>'
    + f'<path d="M32 58 Q30 86 64 88 Q98 86 96 58" fill="none" {W(3)}/>'
    + f'<ellipse cx="64" cy="38" rx="28" ry="24" fill="#A7AFBA" {W(3)}/>'
    + f'<circle cx="34" cy="24" r="13" fill="#A7AFBA" {W(3)}/><circle cx="34" cy="24" r="7" fill="#F2D3DC"/>'
    + f'<circle cx="94" cy="24" r="13" fill="#A7AFBA" {W(3)}/><circle cx="94" cy="24" r="7" fill="#F2D3DC"/>'
    + f'<ellipse cx="64" cy="42" rx="7" ry="9" fill="#3A3550"/>'
    + f'<path d="M46 34 q4 3 8 0 M74 34 q4 3 8 0" fill="none" {W(2.4)}/>'
    + f'<path d="M40 56 Q30 56 26 60 M88 56 Q98 56 102 60" fill="none" stroke="#A7AFBA" stroke-width="9" stroke-linecap="round"/>'
    + f'<text x="104" y="22" font-family="Arial" font-weight="bold" font-size="12" fill="#3B3355">z</text>'
    + f'<text x="112" y="12" font-family="Arial" font-weight="bold" font-size="9" fill="#3B3355">z</text>',
    "серая коала в бело-голубом полосатом купальнике",
    "сладко дремлет, облокотившись на бортик бассейна и опустив задние лапы в воду")

# 9. Дрожжино: оранжевобрюхий тритон плывёт под водой над разметкой дна
add("kitenok-drozhzhino", "aqua",
    f'<rect x="-6" y="-6" width="140" height="140" fill="#7FD6EE" opacity=".5"/>'
    + f'<path d="M-6 110 H134" stroke="#2F6FB0" stroke-width="7"/>'
    + f'<path d="M100 104 V116 M100 110 H112" stroke="#2F6FB0" stroke-width="7"/>'
    + G(60, 64, f'<path d="M-36 4 Q-10 -14 22 -8 Q40 -4 44 4 Q40 12 22 14 Q-6 18 -36 4Z" fill="#6B8F5A" {W(3)}/>'
        + f'<path d="M-30 8 Q-6 16 22 12 Q34 10 40 6" fill="none" stroke="#FF8A2B" stroke-width="5"/>'
        + f'<path d="M-36 4 Q-56 -8 -64 6 Q-54 0 -40 10Z" fill="#6B8F5A" {W(2.6)}/>'
        + f'<path d="M-40 -2 Q-54 -14 -62 -4" fill="none" stroke="#FF8A2B" stroke-width="3"/>'
        + "".join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="#2E3A28"/>' for x, y in [(-20, -2), (-6, -6), (8, -6), (20, -4), (-12, 2)])
        + f'<path d="M-14 12 L-22 26 M12 14 L18 28 M-10 -8 L-18 -20 M16 -8 L22 -20" stroke="#6B8F5A" stroke-width="5" stroke-linecap="round"/>'
        + eye(34, -2, 0.75) + f'<path d="M36 6 Q40 8 44 6" fill="none" {W(1.8)}/>', rot=-6)
    + bubbles([(104, 50, 4), (112, 38, 3), (108, 26, 2.4)])
    + f'<path d="M-6 14 Q30 6 64 14 T134 14" fill="none" stroke="#fff" stroke-width="3" opacity=".8"/>',
    "пятнистый тритон с ярко-оранжевым брюшком и хвостом-веслом",
    "плывёт под водой, извиваясь, над синей разметкой на дне бассейна")

# 10. Котельники, Парковый: надувной единорог катает малыша
add("kitenok-kotelniki-parkovy", "rose",
    water(88, "#56BDEB", amp=3, n=5)
    + f'<path d="M20 94 Q18 72 46 70 H82 Q100 72 98 94 Q60 104 20 94Z" fill="#FFFFFF" {W(3)}/>'
    + f'<path d="M86 76 Q86 48 96 34 Q104 24 114 30 Q120 38 112 44 Q102 48 100 76Z" fill="#FFFFFF" {W(3)}/>'
    + f'<path d="M104 26 L110 6 L114 28Z" fill="{GOLD}" {W(2.2)}/>'
    + f'<path d="M96 36 Q84 44 88 58 M94 46 Q82 56 88 68" fill="none" stroke="#FF8FB8" stroke-width="6" stroke-linecap="round"/>'
    + f'<path d="M98 32 Q88 34 86 46" fill="none" stroke="#9C7BF0" stroke-width="6" stroke-linecap="round"/>'
    + eye(108, 36, 0.65) + f'<ellipse cx="114" cy="42" rx="3" ry="1.8" fill="{PINK}" opacity=".7"/>'
    + f'<path d="M20 90 Q8 78 14 68" fill="none" stroke="#FF8FB8" stroke-width="7" stroke-linecap="round"/>'
    + capkid(54, 58, "#9C7BF0", sc=0.95)
    + f'<path d="M48 70 Q44 80 52 82 M60 70 Q66 78 74 74" fill="none" stroke="{SKIN}" stroke-width="6" stroke-linecap="round"/>'
    + f'<path d="M24 108 q10 -5 20 0 M80 110 q10 -5 20 0" fill="none" stroke="#fff" stroke-width="3"/>',
    "белый надувной единорог с золотым рогом и радужной гривой",
    "качает на спине малыша в фиолетовой шапочке посреди бассейна")

# 11. Новые Котельники: стрекоза присела на палец малыша, который лежит на спине
add("kitenok-kotelniki-novye", "lemon",
    water(70, "#3FB4DF", amp=3, n=5, edge="#2C8DB5")
    + G(56, 92, f'<ellipse cx="0" cy="0" rx="34" ry="11" fill="#FF6A3D" {W(3)}/>'
        + f'<circle cx="-40" cy="-4" r="14" fill="{SKIN}" {W(3)}/>'
        + f'<path d="M-54 -6 Q-54 -18 -40 -18 Q-28 -18 -26 -8 Q-40 -12 -54 -6Z" fill="#FFFFFF" {W(2.4)}/>'
        + face(-40, -2, d=5, k=0.5))
    + f'<path d="M30 88 Q58 70 74 44" fill="none" stroke="{SKIN}" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M30 88 Q58 70 74 44" fill="none" {W(1.4)}/>'
    + G(80, 34, f'<ellipse cx="-14" cy="-8" rx="16" ry="6" fill="#DDF6FF" opacity=".85" {W(1.8)} transform="rotate(-20 -14 -8)"/>'
        + f'<ellipse cx="14" cy="-8" rx="16" ry="6" fill="#DDF6FF" opacity=".85" {W(1.8)} transform="rotate(20 14 -8)"/>'
        + f'<ellipse cx="-12" cy="2" rx="12" ry="4.6" fill="#DDF6FF" opacity=".85" {W(1.6)} transform="rotate(15 -12 2)"/>'
        + f'<ellipse cx="12" cy="2" rx="12" ry="4.6" fill="#DDF6FF" opacity=".85" {W(1.6)} transform="rotate(-15 12 2)"/>'
        + f'<path d="M0 -6 V30" stroke="#2BA36B" stroke-width="5" stroke-linecap="round"/>'
        + f'<path d="M0 -6 V30" fill="none" {W(1.2)}/>'
        + f'<circle cx="0" cy="-12" r="7" fill="#2BA36B" {W(2.4)}/>' + eye(-3, -13, 0.5) + eye(3, -13, 0.5))
    + f'<ellipse cx="96" cy="108" rx="12" ry="3" fill="none" stroke="#fff" stroke-width="2.4"/>',
    "изумрудная стрекоза с прозрачными крыльями",
    "присела на поднятый палец малыша, который лежит на спине в оранжевом купальнике")

# 12. Мытищи: кудрявая овечка вылезла из бассейна и распушилась облаком
add("kitenok-mytishchi", "berry",
    f'<rect x="-6" y="100" width="140" height="34" fill="#4FB6E8"/>'
    + edge(92, "#F6F0E4")
    + "".join(f'<circle cx="{64+30*math.cos(a):.1f}" cy="{58+26*math.sin(a):.1f}" r="15" fill="#FFFFFF" {W(2.8)}/>'
              for a in [i * 0.628 for i in range(10)])
    + f'<circle cx="64" cy="58" r="30" fill="#FFFFFF"/>'
    + f'<ellipse cx="64" cy="60" rx="15" ry="17" fill="#4A4054" {W(2.8)}/>'
    + f'<ellipse cx="46" cy="52" rx="8" ry="4" fill="#4A4054" {W(2.2)} transform="rotate(-25 46 52)"/>'
    + f'<ellipse cx="82" cy="52" rx="8" ry="4" fill="#4A4054" {W(2.2)} transform="rotate(25 82 52)"/>'
    + f'<circle cx="58" cy="57" r="4" fill="#fff"/><circle cx="70" cy="57" r="4" fill="#fff"/>'
    + eye(58, 57, 0.6) + eye(70, 57, 0.6)
    + f'<path d="M60 68 Q64 71 68 68" fill="none" stroke="#fff" stroke-width="2"/>'
    + f'<path d="M54 86 V96 M74 86 V96" stroke="#4A4054" stroke-width="6" stroke-linecap="round"/>'
    + f'<path d="M14 40 l-8 -4 M16 54 l-10 0 M112 40 l8 -4 M112 54 l10 0" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    + drops([(20, 66), (108, 66), (26, 26), (100, 24)], "#BFEFFF"),
    "белая кудрявая овечка с чёрной мордочкой",
    "вылезла из бассейна на бортик и, отряхиваясь, распушилась огромным облаком шерсти")

# 13. Люберцы, Красная горка: жёлтая подводная лодка всплыла, из люка машет малыш
add("kitenok-lyubertsy-krasnaya-gorka", "teal",
    water(78, "#2E8ED0", amp=3, n=4, edge="#1F6AA6")
    + f'<path d="M14 84 Q14 64 40 62 H92 Q114 64 114 84 Q114 98 92 100 H40 Q14 98 14 84Z" fill="#FFD233" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="82" r="7" fill="#BFF0FF" {W(2.6)}/>' for x in (36, 60, 84))
    + f'<rect x="58" y="44" width="24" height="20" rx="4" fill="#FFD233" {W(3)}/>'
    + f'<path d="M84 46 V30 H94" fill="none" {W(3.2)}/>'
    + f'<path d="M114 84 L124 76 V92Z" fill="#FFB02E" {W(2.4)}/>'
    + capkid(70, 34, RED, sc=0.8)
    + f'<path d="M58 40 Q48 30 50 20" fill="none" stroke="{SKIN}" stroke-width="6" stroke-linecap="round"/>'
    + f'<circle cx="50" cy="18" r="4" fill="{SKIN}" {W(1.8)}/>'
    + face(60, 82, d=24, k=0.7, mouth=False, blush=False)
    + water(96, "#2E8ED0", amp=3, n=5, edge="#1F6AA6")
    + bubbles([(20, 64, 3), (110, 60, 3.4), (118, 48, 2.4)]),
    "жёлтая подводная лодка с тремя иллюминаторами",
    "всплыла посреди бассейна, а из открытого люка машет малыш в красной шапочке")

# 14. Люберцы, Ухтомская: капля-мама прыгает с бортика, держа за руку капельку
add("kitenok-lyubertsy-ukhtomskaya", "ice",
    water(96, "#3E9EE0", amp=3, n=5)
    + f'<path d="M-6 64 H40 V74 H-6Z" fill="#F4F1EA" {W(2.4)}/>'
    + G(66, 50, f'<path d="M0 -36 Q30 0 22 18 Q14 32 0 32 Q-14 32 -22 18 Q-30 0 0 -36Z" fill="#6EC8FF" {W(3)}/>'
        + f'<path d="M-12 -4 Q-14 8 -8 14" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>'
        + face(2, 8, d=7, k=0.65), rot=12)
    + G(100, 72, f'<path d="M0 -18 Q15 0 11 9 Q7 16 0 16 Q-7 16 -11 9 Q-15 0 0 -18Z" fill="#A6E1FF" {W(2.6)}/>'
        + face(0, 4, d=4, k=0.4), rot=18)
    + f'<path d="M86 60 Q92 58 94 64" fill="none" stroke="#6EC8FF" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M86 60 Q92 58 94 64" fill="none" {W(1.2)}/>'
    + f'<path d="M44 42 l-10 -6 M44 54 l-12 2" stroke="#9FD4F5" stroke-width="3" stroke-linecap="round"/>',
    "голубая капля воды с мордочкой",
    "прыгает с бортика в бассейн, держа за ручку маленькую капельку")

# 15. Краснознаменск: верблюжонок впервые в бассейне, горбы торчат как два островка
add("kitenok-krasnoznamensk", "sand",
    f'<path d="M30 70 Q30 50 42 50 Q52 50 54 66 Q60 46 72 46 Q86 46 88 70Z" fill="#D9A465" {W(3)}/>'
    + f'<path d="M86 66 Q96 54 98 38" fill="none" stroke="#D9A465" stroke-width="12" stroke-linecap="round"/>'
    + f'<path d="M86 66 Q96 54 98 38" fill="none" {W(1.4)}/>'
    + f'<ellipse cx="104" cy="34" rx="15" ry="11" fill="#D9A465" {W(3)}/>'
    + f'<path d="M94 24 l-4 -8 l8 4Z" fill="#C08A4E" {W(1.8)}/>'
    + eye(100, 31, 0.7) + f'<path d="M110 40 Q114 42 117 39" fill="none" {W(2)}/>'
    + f'<ellipse cx="112" cy="33" rx="1.4" ry="2.4" fill="{O}"/>'
    + f'<path d="M92 24 Q100 18 108 24" fill="none" {W(2.2)}/>'
    + water(68, "#4FB6E8", amp=4, n=4)
    + f'<path d="M24 72 q8 -6 16 0 M48 72 q8 -6 16 0 M70 72 q8 -6 16 0" fill="none" stroke="#fff" stroke-width="3"/>'
    + f'<path d="M22 96 q10 -5 20 0 M70 104 q10 -5 20 0" fill="none" stroke="#fff" stroke-width="3" opacity=".7"/>'
    + sparkle(22, 40, 5) + sparkle(64, 22, 4),
    "песочный верблюжонок с двумя горбами",
    "впервые зашёл в бассейн по шею и удивлённо улыбается, а горбы торчат из воды как два островка")

# 16. Реутов: серый ослик в надувном круге хлопает ушами по воде
add("kitenok-reutov", "coral",
    water(76, "#55B9EA", amp=3, n=4)
    + f'<ellipse cx="64" cy="86" rx="40" ry="14" fill="#7BD957" {W(3)}/>'
    + "".join(f'<path d="M{x} 74 Q{x+4} 86 {x} 98" fill="none" stroke="#fff" stroke-width="4"/>' for x in (36, 64, 92))
    + f'<ellipse cx="64" cy="82" rx="24" ry="7" fill="#55B9EA" {W(2.4)}/>'
    + f'<path d="M48 82 Q46 54 64 52 Q82 54 80 82Z" fill="#9AA0AA" {W(3)}/>'
    + f'<ellipse cx="64" cy="48" rx="18" ry="16" fill="#9AA0AA" {W(3)}/>'
    + f'<ellipse cx="64" cy="56" rx="11" ry="8" fill="#E6E2DA" {W(2.4)}/>'
    + f'<path d="M50 38 Q22 26 14 40 Q30 44 50 44Z" fill="#9AA0AA" {W(2.8)}/>'
    + f'<path d="M78 38 Q106 26 114 40 Q98 44 78 44Z" fill="#9AA0AA" {W(2.8)}/>'
    + f'<path d="M56 32 Q64 22 72 32" fill="#3A3550"/>'
    + eye(57, 45, 0.65) + eye(71, 45, 0.65)
    + f'<circle cx="61" cy="56" r="1.4" fill="{O}"/><circle cx="67" cy="56" r="1.4" fill="{O}"/>'
    + f'<path d="M60 60 Q64 63 68 60" fill="none" {W(1.8)}/>'
    + f'<path d="M10 46 l-6 6 M14 52 l-8 2 M118 46 l6 6 M114 52 l8 2" stroke="#fff" stroke-width="3" stroke-linecap="round"/>',
    "серый длинноухий ослик в зелёном надувном круге",
    "сидит в бассейне и хлопает длинными ушами по воде, поднимая брызги")

# 17. Балашиха, Железнодорожный: львёнок под душем — грива намокла и обвисла
add("kitenok-balashikha-zheleznodorozhny", "peach",
    f'<rect x="-6" y="100" width="140" height="34" fill="#5DC6EC"/>'
    + f'<path d="M-6 100 H134" stroke="#3E8FD8" stroke-width="2.6"/>'
    + f'<path d="M104 -6 V18 Q104 22 98 22 H82" fill="none" stroke="#A8B3C2" stroke-width="5"/>'
    + f'<path d="M66 18 H90 L86 26 H70Z" fill="#C9D3E0" {W(2.6)}/>'
    + "".join(f'<path d="M{x} 30 l{dx} 12" stroke="#7FD0F5" stroke-width="2.6" stroke-linecap="round"/>' for x, dx in [(70, -3), (76, -1), (82, 1), (88, 3)])
    + f'<path d="M30 52 Q30 36 50 36 Q66 32 80 36 Q100 38 98 56 L100 96 Q84 100 78 92 Q64 100 50 92 Q42 100 28 96Z" fill="#C46A2A" {W(3)}/>'
    + "".join(f'<path d="M{x} 70 Q{x+2} 84 {x} 96" fill="none" stroke="#A85520" stroke-width="2.4"/>' for x in (36, 46, 82, 92))
    + f'<ellipse cx="64" cy="66" rx="22" ry="20" fill="#F2B04A" {W(3)}/>'
    + f'<ellipse cx="64" cy="76" rx="9" ry="6" fill="#FFE2B0" {W(2)}/>'
    + f'<path d="M60 72 L68 72 L64 76Z" fill="#5A3A2A"/>'
    + eye(56, 62, 0.7) + eye(72, 62, 0.7)
    + f'<path d="M60 80 Q64 84 68 80" fill="none" {W(2)}/>'
    + drops([(40, 46), (90, 46), (52, 100), (78, 104)], "#9FDFFF"),
    "рыжий львёнок с пышной гривой",
    "стоит под душем у бассейна, а грива намокла и смешно обвисла сосульками")

# 18. Балашиха, Павлино: двойняшки в одинаковых шапочках сидят на бортике и болтают ногами
add("kitenok-balashikha-pavlino", "dusk",
    f'<rect x="-6" y="84" width="140" height="50" fill="#4FB0E6"/>'
    + edge(74, "#F4EEE6")
    + "".join(G(x, 50, kid(shirt=c, hair="#E0B060"), sc=0.85)
              + f'<path d="M{x-6} 82 L{x-10} 102 M{x+6} 82 L{x+10} 102" stroke="{SKIN}" stroke-width="7" stroke-linecap="round"/>'
              + f'<path d="M{x-6} 82 L{x-10} 102 M{x+6} 82 L{x+10} 102" fill="none" {W(1.2)}/>'
              + f'<path d="M{x-15} 36 Q{x-15} 18 {x} 18 Q{x+15} 18 {x+15} 36 Q{x} 28 {x-15} 36Z" fill="#FFD233" {W(2.6)}/>'
              for x, c in [(44, "#FF6FA0"), (84, "#FF6FA0")])
    + f'<path d="M56 64 Q64 70 72 64" fill="none" stroke="{SKIN}" stroke-width="6" stroke-linecap="round"/>'
    + f'<path d="M24 106 q8 -6 16 0 M88 108 q8 -6 16 0" fill="none" stroke="#fff" stroke-width="3"/>'
    + drops([(30, 112), (98, 114)], "#CFF3FF"),
    "двойняшки-близнецы в одинаковых жёлтых шапочках и розовых купальниках",
    "сидят рядышком на бортике, держатся за руки и болтают ногами в воде")

# 19. Химки, Новокуркино: ньюфаундленд везёт малыша на спине через бассейн
add("kitenok-khimki-novokurkino", "steel",
    water(74, "#4AA8E2", amp=3, n=4)
    + f'<path d="M14 86 Q20 70 52 70 Q80 70 88 80 Q70 94 40 94 Q20 94 14 86Z" fill="#2E2A30" {W(3)}/>'
    + f'<ellipse cx="94" cy="66" rx="18" ry="16" fill="#2E2A30" {W(3)}/>'
    + f'<path d="M80 56 Q72 70 80 80 Q86 72 84 58Z" fill="#1E1A20" {W(2.2)}/>'
    + f'<ellipse cx="104" cy="72" rx="9" ry="6" fill="#3E3A40" {W(2)}/>'
    + f'<circle cx="110" cy="70" r="3" fill="#111"/>'
    + f'<circle cx="92" cy="62" r="4.4" fill="#fff"/>' + eye(92, 62, 0.55)
    + f'<path d="M104 78 Q108 84 104 88" fill="#FF7FA8" {W(1.6)}/>'
    + capkid(46, 56, "#FF8A2B", sc=0.85)
    + f'<path d="M38 66 Q30 72 36 78 M54 66 Q64 70 70 66" fill="none" stroke="{SKIN}" stroke-width="6" stroke-linecap="round"/>'
    + water(88, "#4AA8E2", amp=3, n=5)
    + f'<path d="M8 100 q8 -5 16 0 M110 96 q8 -5 16 0" fill="none" stroke="#fff" stroke-width="3"/>',
    "лохматый чёрный ньюфаундленд-спасатель",
    "плывёт через бассейн, а на его широкой спине едет малыш в оранжевой шапочке")

# 20. Химки, Юбилейный: раскрытый гребешок на дне, внутри жемчужина-мячик
add("kitenok-khimki-yubileyny", "aqua",
    f'<rect x="-6" y="96" width="140" height="40" fill="#CFF5F7"/>'
    + "".join(f'<path d="M{x} 96 V134" stroke="#9FDCE4" stroke-width="1.6"/>' for x in range(4, 130, 14))
    + f'<path d="M-6 96 H134" stroke="#9FDCE4" stroke-width="2"/>'
    + f'<path d="M22 92 Q30 38 64 34 Q98 38 106 92Z" fill="#FFB8A0" {W(3)}/>'
    + "".join(f'<path d="M64 92 L{64+44*math.cos(a):.1f} {92-56*math.sin(a):.1f}" stroke="#E8846A" stroke-width="2.4"/>'
              for a in [0.35 + i * 0.41 for i in range(6)])
    + f'<path d="M22 92 Q64 106 106 92 Q100 110 64 112 Q28 110 22 92Z" fill="#FFCDB8" {W(3)}/>'
    + f'<circle cx="64" cy="84" r="16" fill="#FFFFFF" {W(3)}/>'
    + f'<circle cx="58" cy="78" r="5" fill="#E8F4FF"/>'
    + face(64, 86, d=6, k=0.6)
    + bubbles([(24, 30, 4), (34, 18, 3), (104, 26, 3.4), (112, 40, 2.4)]),
    "розовый морской гребешок с белой жемчужиной",
    "раскрыл створки на кафельном дне бассейна, а жемчужина улыбается, как мячик")

# 21. Лыткарино: дедушка в полосатом купальнике учит внучку держаться на воде
add("kitenok-lytkarino", "ice",
    water(66, "#46A7E5", amp=3, n=4)
    + G(0, 12, ''
    + f'<path d="M66 40 Q66 26 80 26 Q96 26 96 40 V62 H66Z" fill="#FFFFFF" {W(3)}/>'
    + f'<path d="M67 36 H95 M66 46 H96 M66 56 H96" stroke="{RED}" stroke-width="4"/>'
    + f'<path d="M66 40 Q66 26 80 26 Q96 26 96 40 V62 H66Z" fill="none" {W(3)}/>'
    + f'<circle cx="82" cy="12" r="14" fill="{SKIN}" {W(3)}/>'
    + f'<path d="M68 8 Q70 -4 82 -4 Q94 -4 96 8" fill="none" {W(2.2)}/>'
    + f'<path d="M72 18 Q82 13 92 18 Q88 22 82 19 Q76 22 72 18Z" fill="#FFFFFF" {W(1.8)}/>'
    + eye(77, 9, 0.55) + eye(87, 9, 0.55)
    + f'<path d="M68 48 Q52 70 40 74" fill="none" stroke="{SKIN}" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M94 46 Q104 60 96 72" fill="none" stroke="{SKIN}" stroke-width="7" stroke-linecap="round"/>'
    )
    + G(46, 80, f'<ellipse cx="0" cy="0" rx="22" ry="8" fill="#FFC93C" {W(2.8)}/>'
        + f'<circle cx="-26" cy="-4" r="11" fill="{SKIN}" {W(2.8)}/>'
        + f'<circle cx="-34" cy="-10" r="4.6" fill="#7A4A2E" {W(1.8)}/><circle cx="-20" cy="-14" r="4.6" fill="#7A4A2E" {W(1.8)}/>'
        + face(-26, -3, d=4, k=0.42)
        + f'<path d="M20 -2 L34 -6 M20 4 L34 6" stroke="{SKIN}" stroke-width="5" stroke-linecap="round"/>')
    + water(84, "#46A7E5", amp=2.4, n=5)
    + f'<path d="M14 100 q8 -5 16 0 M98 102 q8 -5 16 0" fill="none" stroke="#fff" stroke-width="3"/>',
    "лысый дедушка с седыми усами в полосатом ретро-купальнике",
    "стоит по пояс в воде и поддерживает под животик внучку, которая учится лежать на воде")

# 22. Одинцово: рыба-меч несётся стрелой по дорожке, обгоняя пузыри
add("kitenok-odintsovo", "blue",
    f'<rect x="-6" y="-6" width="140" height="140" fill="#3F8FD6" opacity=".35"/>'
    + f'<path d="M-6 96 H134" stroke="{O}" stroke-width="1.6"/>'
    + "".join(f'<ellipse cx="{x}" cy="96" rx="4.4" ry="3.6" fill="{GOLD if i % 2 else "#FFFFFF"}" {W(1.6)}/>' for i, x in enumerate(range(-2, 134, 10)))
    + G(58, 60, f'<path d="M-40 0 Q-18 -18 18 -14 Q36 -10 40 0 Q36 10 18 14 Q-18 18 -40 0Z" fill="#4E6FB8" {W(3)}/>'
        + f'<path d="M-30 4 Q0 14 34 4" fill="#D8E6FF" {W(2)}/>'
        + f'<path d="M40 -2 L76 -1 L40 3Z" fill="#8FA3C8" {W(2.4)}/>'
        + f'<path d="M-6 -16 L4 -34 L14 -14Z" fill="#3A5598" {W(2.4)}/>'
        + f'<path d="M-40 0 L-56 -16 Q-50 0 -56 16Z" fill="#3A5598" {W(2.6)}/>'
        + f'<circle cx="26" cy="-4" r="6" fill="#fff" {W(2)}/>' + eye(27, -4, 0.7)
        + f'<path d="M24 6 Q28 9 32 6" fill="none" {W(1.8)}/>')
    + f'<path d="M-4 52 H8 M-4 62 H12 M-4 72 H6" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    + bubbles([(18, 40, 4), (10, 80, 3), (30, 84, 2.4)])
    + sparkle(110, 30, 5),
    "синяя рыба-меч с длинным острым носом",
    "несётся стрелой вдоль жёлто-белой дорожки бассейна, оставляя позади пузыри")

# 23. Красногорск, Ильинское ш.: бабочка-махаон плывёт баттерфляем
add("kitenok-krasnogorsk-ilyinskoe", "green",
    water(78, "#47B2E6", amp=3, n=4)
    + f'<path d="M62 70 Q36 30 14 40 Q4 56 26 66 Q12 78 30 86 Q48 88 62 74Z" fill="#FFD233" {W(3)}/>'
    + f'<path d="M66 70 Q92 30 114 40 Q124 56 102 66 Q116 78 98 86 Q80 88 66 74Z" fill="#FFD233" {W(3)}/>'
    + f'<path d="M22 46 Q36 46 48 60 M106 46 Q92 46 80 60" fill="none" stroke="#2E2A36" stroke-width="4"/>'
    + f'<path d="M24 76 Q36 74 50 76 M104 76 Q92 74 78 76" fill="none" stroke="#2E2A36" stroke-width="3.4"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3.4" fill="#5CB7F2" {W(1.2)}/>' for x, y in [(28, 82), (100, 82), (20, 56), (108, 56)])
    + f'<circle cx="34" cy="84" r="3" fill="{RED}"/><circle cx="94" cy="84" r="3" fill="{RED}"/>'
    + f'<ellipse cx="64" cy="70" rx="6" ry="20" fill="#2E2A36" {W(2.4)}/>'
    + f'<circle cx="64" cy="46" r="9" fill="#2E2A36" {W(2.4)}/>'
    + f'<circle cx="60.5" cy="45" r="3" fill="#fff"/><circle cx="67.5" cy="45" r="3" fill="#fff"/>'
    + eye(60.5, 45, 0.45) + eye(67.5, 45, 0.45)
    + f'<path d="M60 38 Q54 24 50 22 M68 38 Q74 24 78 22" fill="none" {W(2)}/>'
    + f'<circle cx="50" cy="22" r="2.6" fill="#2E2A36"/><circle cx="78" cy="22" r="2.6" fill="#2E2A36"/>'
    + water(92, "#47B2E6", amp=3, n=5)
    + f'<path d="M6 82 l-4 -10 M122 82 l4 -10 M14 92 l-8 -4 M114 92 l8 -4" stroke="#fff" stroke-width="3" stroke-linecap="round"/>',
    "жёлтая бабочка-махаон с чёрными жилками",
    "плывёт баттерфляем — обоими крыльями разом загребает воду бассейна")

# 24. Ильинские Луга: малыш вынырнул в центре плавательного круга-ромашки
add("kitenok-ilyinskie-luga", "mint",
    water(60, "#5BC0EA", amp=3, n=4, edge="#3C9AD0")
    + "".join(f'<ellipse cx="{64+30*math.cos(a):.1f}" cy="{84+16*math.sin(a):.1f}" rx="13" ry="8" fill="#FFFFFF" {W(2.6)} transform="rotate({math.degrees(a):.0f} {64+30*math.cos(a):.1f} {84+16*math.sin(a):.1f})"/>'
              for a in [i * 0.785 for i in range(8)])
    + f'<ellipse cx="64" cy="84" rx="26" ry="13" fill="#FFC93C" {W(3)}/>'
    + f'<ellipse cx="64" cy="84" rx="14" ry="6" fill="#5BC0EA" {W(2.2)}/>'
    + capkid(64, 70, "#4FBF6B", sc=0.95)
    + f'<path d="M50 78 Q40 70 44 62 M78 78 Q88 70 84 62" fill="none" stroke="{SKIN}" stroke-width="6" stroke-linecap="round"/>'
    + f'<circle cx="44" cy="60" r="3.6" fill="{SKIN}" {W(1.6)}/><circle cx="84" cy="60" r="3.6" fill="{SKIN}" {W(1.6)}/>'
    + f'<path d="M20 44 Q24 30 36 28 M100 40 Q108 30 116 34" fill="none" stroke="#4E9A44" stroke-width="3"/>'
    + sparkle(22, 26, 5) + sparkle(104, 22, 4),
    "надувной плавательный круг-ромашка с белыми лепестками и жёлтой серединкой",
    "малыш в зелёной шапочке вынырнул прямо в его серединке и поднял руки от радости")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for pid, code in ICONS.items():
        open(os.path.join(OUT, pid + ".svg"), "w").write(code)
    reg = os.path.join(OUT, "subjects.txt")
    lines = [l for l in open(reg, encoding="utf-8") if l.split(" — ", 1)[0] not in SUBJ]
    lines += [line + "\n" for line in SUBJ.values()]
    open(reg, "w", encoding="utf-8").writelines(lines)
    print(len(ICONS), "иконок:", " ".join(ICONS))
