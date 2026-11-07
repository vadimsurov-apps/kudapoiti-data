"""Иконки робота sections, 2026-11-07 (12 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно —
свой герой, своя сцена, своя компоновка и палитра. Бассейны «Китёнка» — НЕ серия: у каждого филиала свой герой
(гагара, бобрёнок-спасатель, рыба-луна, поросёнок, водолаз, машинка-амфибия…), общая только вода. Спорткомплексы
спортшкол Москомспорта — у каждого свой вид спорта из списка школы и свой герой.
Сверено с листами icons-catalog/sheet-01..32 и icons-src/subjects.txt (повторов героев нет).
Запуск: python3 tools/icons_sections_1107f.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import svg, s, eye, face, sparkle, O
from icons_sections_1107d import kid, G, W, PINK, GOLD, RED, ORG, LIGHT

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
SKIN = "#FFD8B8"


def add(pid, bg, body, hero, scene):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def water(y, c="#5CB7F2", amp=4, n=4, edge="#3E8FD8"):
    """вода от y до низа с волнистой кромкой"""
    step = 140 / n
    d = f"M-6 {y}" + "".join(f" q{step/4:.1f} {-amp} {step/2:.1f} 0 t{step/2:.1f} 0" for _ in range(n)) + " V134 H-6Z"
    return f'<path d="{d}" fill="{c}" stroke="{edge}" stroke-width="2.6"/>'


def bubbles(pts, c="#fff"):
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{c}" stroke-width="2"/>' for x, y, r in pts)


def lane(y, x0=-6, x1=134, a=RED, b="#FFFFFF", r=4.2):
    n = int((x1 - x0) / (2 * r + 1))
    return (f'<path d="M{x0} {y} H{x1}" stroke="{O}" stroke-width="1.6"/>'
            + "".join(f'<ellipse cx="{x0 + r + i*(2*r+1):.1f}" cy="{y}" rx="{r}" ry="{r*0.8:.1f}" fill="{a if i % 2 else b}" {W(1.6)}/>'
                      for i in range(n)))


def tiles(y0, c="#BFEFF5", line="#7FCFE0", step=14):
    out = f'<rect x="-6" y="{y0}" width="140" height="{134-y0}" fill="{c}"/>'
    out += "".join(f'<path d="M{x} {y0} V134" stroke="{line}" stroke-width="1.6"/>' for x in range(0, 130, step))
    out += "".join(f'<path d="M-6 {y} H134" stroke="{line}" stroke-width="1.6"/>' for y in range(y0, 134, step))
    return out


# ============================== БАССЕЙНЫ «КИТЁНОК» ==============================
# Котляковский: гагара с пушистыми птенцами на спине плывёт по бассейну
add("kitenok-kotlyakovsky", "teal",
    water(76, "#4FB3E8")
    + f'<path d="M24 84 Q30 60 66 62 Q90 62 96 72 L104 82 Q72 98 36 94 Q24 92 24 84Z" fill="#3A4048" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="#fff"/>' for x, y in [(40, 78), (48, 74), (56, 80), (64, 74), (72, 80), (46, 86), (60, 86), (80, 78)])
    + f'<path d="M92 76 Q90 52 100 40" fill="none" stroke="#3A4048" stroke-width="11" stroke-linecap="round"/>'
    + f'<path d="M92 76 Q90 52 100 40" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="2 4"/>'
    + f'<circle cx="102" cy="36" r="12" fill="#2A2E36" {W(3)}/>'
    + f'<path d="M112 34 L126 38 L112 41Z" fill="#9AA3AE" {W(2.2)}/>'
    + f'<circle cx="104" cy="33" r="3.4" fill="{RED}"/><circle cx="103.4" cy="32" r="1.2" fill="#fff"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="10" fill="#8C8A86" {W(2.6)}/>' + face(x, y - 1, d=4, k=0.45)
              + f'<path d="M{x+8} {y-2} l5 1.5 l-5 1.5Z" fill="{GOLD}" {W(1.4)}/>'
              for x, y in [(46, 60), (66, 56)])
    + f'<path d="M14 100 q8 -4 16 0 M96 104 q8 -4 16 0" fill="none" stroke="#fff" stroke-width="2.6" opacity=".8"/>',
    "черношейная гагара в белую крапинку с двумя пушистыми птенцами",
    "плывёт по бассейну, катая серых птенцов на спине")

# Берёзовая аллея: бобрёнок-спасатель на высоком стуле у бассейна, на коленях — спасательный круг
add("kitenok-berezovaya-alleya", "yellow",
    tiles(92, "#9FE3F0", "#6CC8DE")
    + f'<path d="M70 92 Q84 86 98 92 T128 92 V134 H70Z" fill="#5CB7F2" opacity=".85"/>'
    + f'<path d="M22 128 L32 70 M58 128 L48 70 M26 104 H54 M28 88 H52" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M22 128 L32 70 M58 128 L48 70" fill="none" {W(1.6)}/>'
    + f'<rect x="26" y="62" width="30" height="9" rx="3" fill="{RED}" {W(2.6)}/>'
    + f'<path d="M30 62 Q26 34 41 30 Q56 34 52 62Z" fill="#9A6A44" {W(3)}/>'
    + f'<ellipse cx="41" cy="50" rx="8" ry="10" fill="#D9B48E"/>'
    + f'<circle cx="41" cy="24" r="14" fill="#9A6A44" {W(3)}/>'
    + f'<circle cx="29" cy="14" r="4.5" fill="#9A6A44" {W(2.2)}/><circle cx="53" cy="14" r="4.5" fill="#9A6A44" {W(2.2)}/>'
    + f'<path d="M27 16 Q41 2 55 16 Q41 12 27 16Z" fill="{RED}" {W(2.2)}/>'
    + face(41, 24, d=5, k=0.55)
    + f'<rect x="37" y="33" width="4" height="4" fill="#fff" {W(1)}/><rect x="41" y="33" width="4" height="4" fill="#fff" {W(1)}/>'
    + f'<path d="M58 66 Q74 70 74 56 Q72 50 64 54" fill="#6B4A30" {W(2.6)}/>'
    + f'<circle cx="86" cy="56" r="15" fill="none" stroke="{RED}" stroke-width="9"/>'
    + f'<circle cx="86" cy="56" r="15" fill="none" stroke="#fff" stroke-width="9" stroke-dasharray="6 6"/>'
    + f'<circle cx="86" cy="56" r="19.5" fill="none" {W(2)}/><circle cx="86" cy="56" r="10.5" fill="none" {W(2)}/>'
    + f'<path d="M50 44 L74 50" stroke="#9A6A44" stroke-width="6" stroke-linecap="round"/>',
    "бобрёнок-спасатель в красной кепке",
    "дежурит на высоком белом стуле у края бассейна и протягивает красно-белый спасательный круг")

# Академика Павлова: огромная серебристая рыба-луна, малыш в жёлтой шапочке держится за её плавник
add("kitenok-akademika-pavlova", "blue",
    "".join(f'<path d="M{x} -4 L{x+16} 134" stroke="#fff" stroke-width="8" opacity=".12"/>' for x in (20, 60, 100))
    + f'<path d="M58 22 Q66 2 76 8 Q74 22 70 30Z" fill="#AFC0D2" {W(2.6)}/>'
    + f'<path d="M58 102 Q66 124 78 118 Q74 104 70 96Z" fill="#AFC0D2" {W(2.6)}/>'
    + f'<circle cx="60" cy="62" r="38" fill="#C9D6E4" {W(3.2)}/>'
    + f'<path d="M96 46 Q108 62 96 78" fill="#AFC0D2" {W(2.6)}/>'
    + f'<path d="M40 50 Q58 44 78 52 M36 68 Q58 62 82 70" fill="none" stroke="#AFC0D2" stroke-width="3"/>'
    + face(42, 56, d=8, k=0.8)
    + f'<ellipse cx="24" cy="62" rx="3" ry="2" fill="{O}"/>'
    + f'<circle cx="104" cy="104" r="12" fill="{SKIN}" {W(2.6)}/>'
    + f'<path d="M92 102 Q94 88 104 88 Q114 88 116 102 Q104 96 92 102Z" fill="{GOLD}" {W(2.2)}/>'
    + face(104, 106, d=4, k=0.45)
    + f'<path d="M96 112 Q84 116 76 116" fill="none" stroke="{SKIN}" stroke-width="5" stroke-linecap="round"/>'
    + bubbles([(110, 80, 3), (116, 70, 2.2), (24, 26, 3)]),
    "огромная серебристая рыба-луна с круглым боком",
    "плавно плывёт под водой, а малыш в жёлтой шапочке держится за её нижний плавник")

# Коломенский проезд: тонущие кольца-игрушки на дне, малыш ныряет за ними головой вниз
add("kitenok-kolomensky-proezd", "sky",
    water(30, "#7FD0F5", amp=3)
    + tiles(104, "#5CB7F2", "#3E8FD8", 16)
    + "".join(f'<ellipse cx="{x}" cy="104" rx="11" ry="5" fill="none" stroke="{c}" stroke-width="5"/>'
              f'<ellipse cx="{x}" cy="104" rx="13.5" ry="7.5" fill="none" {W(1.4)}/>' for x, c in [(34, RED), (64, GOLD), (94, "#4FBF6B")])
    + G(64, 58, f'<path d="M-6 -30 L-12 -48 M6 -30 L12 -48" stroke="{SKIN}" stroke-width="7" stroke-linecap="round"/>'
        f'<path d="M-10 -30 Q-14 -6 0 -4 Q14 -6 10 -30Z" fill="#E8554A" {W(2.6)}/>'
        f'<circle cx="0" cy="8" r="13" fill="{SKIN}" {W(2.6)}/>'
        f'<path d="M-13 6 Q-12 -6 0 -5 Q12 -6 13 6Z" fill="#4A4466" {W(2)}/>'
        + face(0, 12, d=4.6, k=0.5, mouth=False) + f'<circle cx="0" cy="18" r="2.2" fill="{O}"/>'
        f'<path d="M-8 4 Q-20 18 -18 30 M8 4 Q20 18 18 30" fill="none" stroke="{SKIN}" stroke-width="5" stroke-linecap="round"/>')
    + bubbles([(76, 36, 3), (82, 44, 2.2), (72, 50, 1.8)]),
    "разноцветные тонущие кольца-игрушки",
    "лежат на кафельном дне бассейна, а малыш в красном купальнике ныряет за ними головой вниз")

# Комсомольский: надувной круг-пончик с розовой глазурью, в дырке сидит малыш и машет
add("kitenok-komsomolsky", "pink",
    water(78, "#6CC8F0")
    + f'<ellipse cx="64" cy="86" rx="44" ry="18" fill="#E9B27A" {W(3)}/>'
    + f'<path d="M22 82 Q26 66 64 66 Q102 66 106 82 Q96 92 86 84 Q76 94 64 86 Q52 94 42 84 Q32 92 22 82Z" fill="#FF9EC4" {W(2.6)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="6" height="2.6" rx="1.3" fill="{c}" transform="rotate({r} {x} {y})"/>'
              for x, y, c, r in [(32, 76, "#fff", 20), (46, 70, GOLD, -30), (78, 70, "#5CB7F2", 40), (92, 76, "#fff", -20), (62, 72, "#4FBF6B", 10)])
    + f'<ellipse cx="64" cy="80" rx="16" ry="6" fill="#4FA8DC" {W(2.2)}/>'
    + G(64, 60, kid(shirt="#5CB7F2", hair="#3B3355"), sc=0.85)
    + f'<path d="M50 62 L36 42 M78 62 L92 42" stroke="{SKIN}" stroke-width="6" stroke-linecap="round"/>'
    + face(64, 98, d=12, k=0.6),
    "надувной круг-пончик с розовой глазурью и посыпкой",
    "качается на воде бассейна, а в дырке сидит малыш и радостно машет обеими руками")

# Люблинский парк: надувной мяч-арбуз качается на воде
add("kitenok-lyublinsky-park", "green",
    water(84, "#5CC4EE")
    + f'<circle cx="64" cy="64" r="34" fill="#4FBF6B" {W(3.2)}/>'
    + "".join(f'<path d="M{64+dx} 31 Q{64+dx*1.9} 64 {64+dx} 97" fill="none" stroke="#2E8B47" stroke-width="5"/>' for dx in (-20, -7, 7, 20))
    + f'<circle cx="64" cy="64" r="34" fill="none" {W(3.2)}/>'
    + f'<circle cx="64" cy="31" r="4" fill="{RED}" {W(2)}/>'
    + f'<ellipse cx="50" cy="48" rx="8" ry="5" fill="#fff" opacity=".45"/>'
    + face(64, 66, d=9, k=0.8)
    + f'<path d="M26 92 q6 -10 12 -2 M90 92 q6 -10 12 -2" fill="none" stroke="#fff" stroke-width="3"/>'
    + water(92, "#5CC4EE", amp=3, n=5),
    "надувной мяч-арбуз в зелёную полоску",
    "покачивается на волнах бассейна и улыбается, наполовину в воде")

# Веласкеса: рак-отшельник в закрученной ракушке ползёт по кафельному дну бассейна
add("kitenok-velaskesa", "orange",
    tiles(36, "#7FD8EE", "#4FB8D8", 15)
    + f'<path d="M-6 36 H134" stroke="#3E8FD8" stroke-width="3"/>'
    + f'<path d="M40 100 Q30 66 60 52 Q92 44 100 76 Q102 98 80 104Z" fill="#FFE2C4" {W(3)}/>'
    + f'<path d="M60 52 Q84 60 80 80 Q70 92 62 82 Q58 72 68 70" fill="none" stroke="#E8955A" stroke-width="5"/>'
    + f'<path d="M48 96 L28 108 M56 102 L40 116 M74 104 L70 118" stroke="{RED}" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M36 86 Q22 82 18 92 Q24 100 34 96" fill="{RED}" {W(2.4)}/>'
    + f'<path d="M34 84 L30 66 M42 84 L44 64" stroke="{RED}" stroke-width="3"/>'
    + eye(30, 64, 0.8) + eye(44, 62, 0.8)
    + f'<path d="M30 96 Q34 100 38 96" fill="none" {W(2)}/>'
    + bubbles([(96, 40, 3.2), (104, 30, 2.4), (90, 22, 1.8)]),
    "рак-отшельник в закрученной бежевой ракушке",
    "деловито ползёт по голубому кафельному дну бассейна, выглядывая глазками на стебельках")

# Вернадского: усатый сом лежит на дне бассейна и пускает пузыри
add("kitenok-vernadskogo", "purple",
    f'<rect x="-6" y="24" width="140" height="110" fill="#6FC3E8" opacity=".9"/>'
    + f'<path d="M-6 24 H134" stroke="#3E8FD8" stroke-width="3"/>'
    + f'<rect x="-6" y="104" width="140" height="30" fill="#4FA0C8"/>'
    + f'<path d="M108 76 L126 60 L124 96Z" fill="#5E7A62" {W(2.6)}/>'
    + f'<path d="M20 82 Q24 58 60 58 Q100 60 110 78 Q100 96 60 98 Q24 98 20 82Z" fill="#6E8C70" {W(3)}/>'
    + f'<path d="M40 60 Q60 46 80 60" fill="#5E7A62" {W(2.4)}/>'
    + f'<path d="M30 92 Q60 102 96 90" fill="none" stroke="#B9CDB4" stroke-width="5"/>'
    + face(40, 76, d=7, k=0.7, blush=False)
    + f'<path d="M24 82 Q6 84 2 100 M26 86 Q14 96 14 110 M26 78 Q8 70 4 60" fill="none" {W(2.6)}/>'
    + bubbles([(30, 50, 4), (36, 38, 3), (28, 30, 2.2)]),
    "большой усатый сом с длинными усами",
    "лежит на дне бассейна, шевелит усами и пускает пузыри вверх")

# Свинорье: поросёнок плывёт по-собачьи, пятачок над водой
add("kitenok-svinorye", "sky",
    lane(40)
    + water(70, "#5CB7F2")
    + f'<ellipse cx="64" cy="64" rx="26" ry="23" fill="#FFB3C8" {W(3)}/>'
    + f'<path d="M42 48 L36 30 L54 42Z M86 48 L92 30 L74 42Z" fill="#FF9AB6" {W(2.6)}/>'
    + face(64, 58, d=10, k=0.75, mouth=False)
    + f'<ellipse cx="64" cy="72" rx="10" ry="7" fill="#FF8FB0" {W(2.4)}/>'
    + f'<circle cx="60" cy="72" r="1.8" fill="{O}"/><circle cx="68" cy="72" r="1.8" fill="{O}"/>'
    + water(78, "#5CB7F2", amp=3, n=5)
    + f'<path d="M32 86 Q26 80 30 74 M96 86 Q102 80 98 74" fill="none" stroke="#FFB3C8" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M22 72 l-6 -6 M26 66 l-2 -8 M104 72 l6 -6 M100 66 l2 -8" stroke="#fff" stroke-width="3" stroke-linecap="round"/>',
    "розовый поросёнок с пятачком",
    "плывёт по-собачьи вдоль разделительной дорожки, держа пятачок над водой и брызгаясь копытцами")

# Бромлей: рыба-удильщик светит фонариком на ночном дне бассейна
add("kitenok-bromley", "night",
    tiles(100, "#2E3C86", "#4A58A8", 14)
    + f'<circle cx="92" cy="30" r="20" fill="#FFF3A0" opacity=".25"/>'
    + f'<path d="M58 54 Q66 26 92 28" fill="none" {W(2.6)}/>'
    + f'<circle cx="92" cy="30" r="7" fill="#FFF3A0" {W(2.4)}/>' + sparkle(92, 30, 4, "#fff")
    + f'<path d="M24 74 L6 58 L8 92Z" fill="#6A5A9A" {W(2.6)}/>'
    + f'<path d="M22 74 Q24 48 56 46 Q90 46 96 74 Q92 98 58 100 Q26 100 22 74Z" fill="#8A78C8" {W(3)}/>'
    + f'<path d="M60 82 Q80 92 96 78 Q86 102 64 98Z" fill="#fff" {W(2.2)}/>'
    + "".join(f'<path d="M{x} {y1} L{x+3} {y2} L{x+6} {y1}" fill="#fff" {W(1.4)}/>' for x, y1, y2 in [(66, 84, 90), (76, 86, 92), (86, 84, 90)])
    + face(66, 64, d=8, k=0.75, mouth=False)
    + f'<path d="M40 56 L46 46 L52 56" fill="#6A5A9A" {W(2)}/>',
    "фиолетовая рыба-удильщик с фонариком на удочке",
    "светит фонариком в тёмной воде над ночным кафельным дном бассейна")

# Ютаново: жук-плавунец гребёт лапками-вёслами и тащит пузырь воздуха
add("kitenok-yutanovo", "green",
    f'<rect x="-6" y="-6" width="140" height="140" fill="#7FD0EE" opacity=".55"/>'
    + water(18, "#7FD0EE", amp=3)
    + f'<circle cx="100" cy="88" r="12" fill="#E8F8FF" opacity=".8" {W(2)}/>' + sparkle(96, 84, 3, "#fff")
    + f'<path d="M40 70 L14 52 M40 84 L12 96 M76 64 L104 46" stroke="#2E4A2A" stroke-width="4" stroke-linecap="round"/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="9" ry="3.6" fill="#4C6B3A" transform="rotate({r} {x} {y})" {W(1.6)}/>' for x, y, r in [(16, 52, 35), (14, 96, -25)])
    + f'<ellipse cx="62" cy="76" rx="32" ry="24" fill="#2F5A34" {W(3)}/>'
    + f'<ellipse cx="62" cy="76" rx="27" ry="19" fill="none" stroke="{GOLD}" stroke-width="4"/>'
    + f'<path d="M62 58 V96" stroke="#1E3A22" stroke-width="2.4"/>'
    + f'<path d="M32 70 Q24 76 32 82" fill="#2F5A34" {W(2.4)}/>'
    + eye(30, 72, 0.6) + f'<path d="M26 80 q3 2 6 0" fill="none" {W(1.6)}/>'
    + bubbles([(110, 64, 3), (116, 50, 2.2), (108, 38, 1.8)]),
    "тёмно-зелёный жук-плавунец с жёлтой каймой",
    "гребёт под водой длинными лапками-вёслами и несёт на хвосте серебристый пузырь воздуха")

# Коммунарка: розовый лосось перепрыгивает через поплавковую дорожку, как через барьер
add("kitenok-kommunarka", "purple",
    water(84, "#6CC4F0")
    + lane(90, r=5)
    + f'<path d="M24 92 Q40 36 92 40 Q100 42 104 48" fill="none" stroke="#fff" stroke-width="2.6" stroke-dasharray="4 6"/>'
    + G(70, 46, f'<path d="M-32 6 Q-10 -18 22 -8 Q34 -2 34 6 Q22 18 -6 16 Q-24 16 -32 6Z" fill="#FF9A8A" {W(3)}/>'
        f'<path d="M-30 6 L-46 -8 L-44 20Z" fill="#F07A6A" {W(2.6)}/>'
        f'<path d="M-20 8 Q4 16 30 6" fill="none" stroke="#FFD6CC" stroke-width="4"/>'
        f'<path d="M-6 -10 L0 -20 L8 -9" fill="#F07A6A" {W(2)}/>'
        + "".join(f'<circle cx="{x}" cy="{y}" r="1.4" fill="#C0504A"/>' for x, y in [(-14, -2), (-6, 0), (2, -4), (-10, 6)])
        + eye(20, -1, 0.6) + f'<path d="M26 8 q3 2 6 -1" fill="none" {W(1.6)}/>', rot=-12)
    + f'<path d="M14 80 q4 -12 10 -2 M30 84 q2 -10 8 -4" fill="none" stroke="#fff" stroke-width="2.6"/>',
    "розовый лосось в крапинку",
    "в прыжке перелетает через красно-белую поплавковую дорожку, как через барьер")

# Матвеевская: водолаз в медном шлеме машет со дна бассейна
add("kitenok-matveevskaya", "blue",
    tiles(108, "#7FD8EE", "#4FB8D8", 16)
    + f'<path d="M64 20 V-6" stroke="#E0D2A6" stroke-width="4"/>'
    + bubbles([(70, 16, 3), (76, 6, 2.2)])
    + f'<path d="M38 112 Q36 80 64 78 Q92 80 90 112Z" fill="#9AA6B8" {W(3)}/>'
    + f'<path d="M42 112 V122 H56 V112 M72 112 V122 H86 V112" fill="#5A6478" {W(2.6)}/>'
    + f'<path d="M88 88 Q104 76 108 58" fill="none" stroke="#9AA6B8" stroke-width="9" stroke-linecap="round"/>'
    + f'<path d="M88 88 Q104 76 108 58" fill="none" {W(1.6)}/>'
    + f'<circle cx="108" cy="54" r="7" fill="#C9A06A" {W(2.4)}/>'
    + f'<circle cx="64" cy="54" r="27" fill="#D9934A" {W(3.2)}/>'
    + f'<circle cx="64" cy="56" r="15" fill="#BFE8F8" {W(3)}/>'
    + "".join(f'<circle cx="{64+22*math.cos(a)}" cy="{54+22*math.sin(a)}" r="2.2" fill="#8A5A2E"/>' for a in [i * math.pi / 4 for i in range(8)])
    + f'<rect x="38" y="76" width="52" height="7" rx="3" fill="#B87A3A" {W(2.4)}/>'
    + face(64, 54, d=5, k=0.55),
    "водолаз в медном шлеме с круглым окошком",
    "стоит на кафельном дне бассейна в тяжёлых ботинках и машет рукой, а вверх бегут пузыри")

# Мнёвники: баклан сушит раскрытые крылья на стартовой тумбе
add("kitenok-mnevniki", "orange",
    water(92, "#5CB7F2")
    + f'<path d="M44 92 L48 72 H80 L84 92Z" fill="#fff" {W(3)}/>'
    + f'<rect x="44" y="66" width="40" height="8" rx="2" fill="#5CB7F2" {W(2.6)}/>'
    + f'<path d="M58 66 Q56 44 64 34 Q72 44 70 66Z" fill="#2E2A36" {W(3)}/>'
    + f'<path d="M58 50 Q30 30 12 46 Q24 50 26 58 Q40 52 58 58Z" fill="#3A3644" {W(2.6)}/>'
    + f'<path d="M70 50 Q98 30 116 46 Q104 50 102 58 Q88 52 70 58Z" fill="#3A3644" {W(2.6)}/>'
    + "".join(f'<path d="M{x} {y} l{dx} 6" stroke="#5A5666" stroke-width="2"/>' for x, y, dx in [(22, 46, 2), (32, 42, 2), (42, 44, 2), (106, 46, -2), (96, 42, -2), (86, 44, -2)])
    + f'<circle cx="64" cy="28" r="11" fill="#2E2A36" {W(3)}/>'
    + f'<path d="M72 28 L88 32 L72 34Z" fill="{GOLD}" {W(2.2)}/>'
    + f'<circle cx="67" cy="26" r="3" fill="#6FD38A"/><circle cx="66" cy="25" r="1.2" fill="#fff"/>'
    + f'<path d="M60 32 Q62 34 66 32" fill="none" stroke="#fff" stroke-width="1.6"/>'
    + f'<path d="M58 66 L54 74 M70 66 L74 74" stroke="#2E2A36" stroke-width="3"/>',
    "чёрный баклан с зелёными глазами",
    "стоит на белой стартовой тумбе бассейна и сушит широко раскрытые крылья")

# Раменки: наутилус в полосатой раковине плывёт по дорожке
add("kitenok-ramenki", "pink",
    f'<rect x="-6" y="34" width="140" height="100" fill="#7FD0F0"/>'
    + f'<path d="M-6 34 H134" stroke="#3E8FD8" stroke-width="3"/>'
    + f'<path d="M-6 110 H134" stroke="#3E8FD8" stroke-width="4" stroke-dasharray="10 8"/>'
    + f'<circle cx="74" cy="70" r="30" fill="#FFF3E6" {W(3.2)}/>'
    + "".join(f'<path d="M{74+30*math.cos(a)} {70+30*math.sin(a)} Q{74+16*math.cos(a+0.5)} {70+16*math.sin(a+0.5)} 80 70" fill="none" stroke="#D9774A" stroke-width="4.6"/>'
              for a in [math.pi * (1.2 + i * 0.28) for i in range(6)])
    + f'<path d="M80 70 m-8 0 a8 8 0 1 0 16 0 a12 12 0 1 0 -20 4" fill="none" {W(2.4)}/>'
    + f'<path d="M46 70 Q34 60 40 82 Q46 96 56 90" fill="#F2D4C0" {W(2.6)}/>'
    + "".join(f'<path d="M{x} {y} q-10 {dy} -18 {dy+6}" fill="none" stroke="#F2B8A0" stroke-width="3.4" stroke-linecap="round"/>' for x, y, dy in [(42, 84, 4), (44, 90, 10), (48, 94, 16)])
    + eye(48, 76, 0.65)
    + bubbles([(22, 50, 3), (14, 60, 2)]),
    "наутилус в бело-рыжей полосатой раковине",
    "плывёт вдоль дорожки бассейна, перебирая щупальцами")

# ЗИЛ: красная машинка-амфибия плывёт по бассейну, гребной винт сзади
add("kitenok-zil", "yellow",
    water(78, "#5CB7F2")
    + f'<path d="M24 82 L30 60 Q34 52 46 52 H76 Q86 52 92 62 L104 66 Q112 68 110 82 Q66 92 24 82Z" fill="{RED}" {W(3)}/>'
    + f'<path d="M48 56 H72 L76 66 H44Z" fill="#BFE8F8" {W(2.4)}/>'
    + f'<circle cx="104" cy="72" r="4" fill="#FFF3A0" {W(2)}/>'
    + face(60, 74, d=10, k=0.7)
    + f'<path d="M18 84 L10 78 L12 92Z" fill="#9AA6B8" {W(2)}/>'
    + water(84, "#5CB7F2", amp=3, n=5)
    + f'<path d="M4 90 Q14 84 22 92 M2 100 Q12 94 20 100" fill="none" stroke="#fff" stroke-width="3"/>'
    + f'<path d="M108 84 q10 -8 18 -2" fill="none" stroke="#fff" stroke-width="3"/>',
    "красная машинка-амфибия с гребным винтом",
    "плывёт по бассейну как катер, оставляя за собой пенную волну")

# Бутлерова: розовые шлёпанцы ждут на бортике, а хозяин уже плывёт — только пятки и брызги
add("kitenok-butlerova", "green",
    f'<rect x="-6" y="70" width="140" height="64" fill="#5CB7F2"/>'
    + f'<path d="M-6 70 H134" stroke="#3E8FD8" stroke-width="3"/>'
    + f'<rect x="-6" y="60" width="140" height="12" fill="#EAF6FA" {W(2.4)}/>'
    + "".join(f'<path d="M{x} 60 V72" stroke="#B8DDE8" stroke-width="1.6"/>' for x in range(4, 130, 12))
    + "".join(G(x, 50, f'<ellipse cx="0" cy="0" rx="10" ry="15" fill="#FF8FB8" {W(2.6)}/>'
                f'<path d="M-9 -2 Q0 -12 9 -2" fill="none" stroke="#fff" stroke-width="4"/>'
                f'<path d="M-9 -2 Q0 -12 9 -2" fill="none" {W(1.4)}/>' + face(0, 5, d=4, k=0.4), rot=r) for x, r in [(30, -8), (54, 8)])
    + f'<path d="M84 98 L92 80 M100 98 L104 82" stroke="{SKIN}" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M84 98 L92 80 M100 98 L104 82" fill="none" {W(1.4)}/>'
    + f'<path d="M78 82 l-6 -10 M88 74 l-2 -12 M100 74 l2 -12 M110 80 l8 -8" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    + f'<ellipse cx="94" cy="100" rx="18" ry="5" fill="#fff" opacity=".6"/>',
    "пара розовых резиновых шлёпанцев",
    "ждут на бортике бассейна, а их хозяин уже плавает — видны только пятки и брызги")

# Лефортово: ящерица-василиск бежит по воде на задних лапках
add("kitenok-lefortovo", "teal",
    water(92, "#5CB7F2")
    + f'<path d="M30 70 Q10 74 4 92" fill="none" stroke="#5FB04A" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M34 76 Q40 50 64 46 Q78 46 80 56 Q74 76 52 82Z" fill="#7CCB5A" {W(3)}/>'
    + f'<path d="M44 52 L48 40 L54 50 L60 38 L64 48 L70 40 L72 50" fill="#4E9A3E" {W(2.2)}/>'
    + f'<ellipse cx="86" cy="42" rx="14" ry="11" fill="#7CCB5A" {W(3)}/>'
    + f'<path d="M80 32 L86 18 L92 32" fill="#4E9A3E" {W(2.2)}/>'
    + eye(90, 40, 0.65) + f'<path d="M92 48 q4 2 8 -1" fill="none" {W(1.8)}/>'
    + f'<path d="M72 60 L90 62 M68 64 L82 72" stroke="#7CCB5A" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M46 80 L36 94 L28 92 M58 80 L66 94 L74 92" fill="none" stroke="#5FB04A" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
    + f'<path d="M22 96 q6 -8 12 0 M60 96 q6 -8 12 0" fill="none" stroke="#fff" stroke-width="3"/>'
    + f'<path d="M16 88 l-4 -6 M80 88 l4 -6" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>',
    "зелёная ящерица-василиск с гребнем",
    "бежит по воде бассейна на задних лапках, поднимая брызги")

# Щербинка: синий пенопластовый пояс-поплавок обнимает малыша, который впервые плывёт сам
add("kitenok-shcherbinka", "purple",
    water(70, "#6CC8F0")
    + G(64, 56, kid(shirt="#FFC93C", hair="#C9783C", girl=True), sc=0.95)
    + f'<path d="M50 60 L28 52 M78 60 L100 52" stroke="{SKIN}" stroke-width="6" stroke-linecap="round"/>'
    + "".join(f'<rect x="{x}" y="70" width="15" height="18" rx="4" fill="#3E7FD8" {W(2.4)}/>' for x in (34, 49, 64, 79))
    + f'<path d="M30 79 H98" stroke="#FFC93C" stroke-width="2.4"/>'
    + face(64, 77, d=8, k=0.5)
    + water(86, "#6CC8F0", amp=3, n=5)
    + f'<path d="M14 92 q6 -6 12 0 M102 92 q6 -6 12 0" fill="none" stroke="#fff" stroke-width="2.6"/>',
    "синий пенопластовый пояс-поплавок из брусочков",
    "обнимает за талию девочку с хвостиками, которая впервые плывёт сама и раскинула руки")

# Троицк: ёршик с колючим плавником плывёт наперегонки с малышом по соседней дорожке
add("kitenok-troitsk", "orange",
    f'<rect x="-6" y="30" width="140" height="104" fill="#6CC4F0"/>'
    + f'<path d="M-6 30 H134" stroke="#3E8FD8" stroke-width="3"/>'
    + lane(76, r=3.6)
    + G(66, 52, f'<path d="M-34 0 Q-10 -18 22 -8 Q32 -2 32 4 Q20 14 -8 12 Q-26 12 -34 0Z" fill="#B7B26A" {W(3)}/>'
        f'<path d="M-14 -10 L-10 -24 L-4 -12 L0 -26 L6 -12 L10 -22 L14 -8" fill="#8E8A48" {W(2)}/>'
        f'<path d="M-32 0 L-46 -10 L-44 12Z" fill="#8E8A48" {W(2.4)}/>'
        + "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="#6E6A38"/>' for x, y in [(-18, 0), (-8, 4), (2, -2), (-12, -6)])
        + eye(20, -1, 0.65) + f'<path d="M26 6 q3 2 6 -1" fill="none" {W(1.6)}/>')
    + G(56, 104, f'<circle cx="0" cy="0" r="10" fill="{SKIN}" {W(2.4)}/>'
        f'<path d="M-10 -2 Q-10 -12 0 -12 Q10 -12 10 -2Z" fill="{RED}" {W(2)}/>' + face(0, 2, d=4, k=0.4)
        + f'<path d="M-10 6 Q-24 -4 -30 6 M10 6 Q24 -4 30 6" fill="none" stroke="{SKIN}" stroke-width="5" stroke-linecap="round"/>')
    + f'<path d="M80 104 q6 -4 12 0 q6 4 12 0" fill="none" stroke="#fff" stroke-width="2.6"/>',
    "колючий ёршик в пятнышках",
    "плывёт наперегонки с малышом в красной шапочке по соседней дорожке бассейна")

# Медынский: под сигнальными флажками на спине плывёт малыш, 50-метровые дорожки уходят вдаль
add("medynsky-pool", "sky",
    f'<path d="M-6 50 H134 V134 H-6Z" fill="#5CB7F2"/>'
    + "".join(f'<path d="M{64+dx*0.25} 50 L{64+dx} 134" stroke="#fff" stroke-width="2.4" opacity=".7"/>' for dx in (-120, -60, 0, 60, 120))
    + f'<path d="M-6 26 Q64 40 134 26" fill="none" {W(2)}/>'
    + "".join(f'<path d="M{x} {28+ (1-((x-64)/70)**2)*7:.1f} l6 12 l6 -12Z" fill="{c}" {W(1.6)}/>'
              for x, c in [(2, RED), (18, GOLD), (34, "#4FBF6B"), (50, RED), (66, GOLD), (82, "#4FBF6B"), (98, RED), (114, GOLD)])
    + f'<circle cx="64" cy="92" r="12" fill="{SKIN}" {W(2.6)}/>'
    + f'<path d="M52 90 Q52 78 64 78 Q76 78 76 90 Q64 84 52 90Z" fill="#4FBF6B" {W(2.2)}/>'
    + face(64, 94, d=4.6, k=0.5)
    + f'<path d="M52 98 Q40 92 36 74 M76 98 Q88 104 96 116" fill="none" stroke="{SKIN}" stroke-width="6" stroke-linecap="round"/>'
    + f'<path d="M50 106 q14 8 28 0" fill="none" stroke="#fff" stroke-width="3"/>',
    "гирлянда сигнальных флажков над 50-метровым бассейном",
    "малыш в зелёной шапочке плывёт на спине под флажками, дорожки уходят вдаль")


# ============================== СПОРТКОМПЛЕКСЫ МОСКОМСПОРТА ==============================
# «Кантемировский» (батут): тушканчик взлетает над синим батутом
add("ms-yug-kantemirovsky", "purple",
    f'<ellipse cx="64" cy="104" rx="46" ry="11" fill="#2E3C86" {W(3)}/>'
    + f'<ellipse cx="64" cy="102" rx="38" ry="7" fill="#4A6AD8"/>'
    + "".join(f'<path d="M{x} 110 L{x+dx} 126" stroke="{O}" stroke-width="4" stroke-linecap="round"/>' for x, dx in [(28, -4), (100, 4), (64, 0)])
    + f'<path d="M50 92 q14 -6 28 0" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 4"/>'
    + f'<path d="M78 56 Q104 60 112 40 Q114 30 118 28" fill="none" stroke="#E0B07A" stroke-width="4" stroke-linecap="round"/>'
    + f'<path d="M114 22 Q124 22 122 32 Q116 34 114 22Z" fill="#fff" {W(2)}/>'
    + f'<ellipse cx="64" cy="54" rx="18" ry="16" fill="#E9C08A" {W(3)}/>'
    + f'<path d="M56 66 L50 84 L40 86 M72 66 L78 84 L88 86" fill="none" stroke="#E9C08A" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
    + f'<path d="M56 66 L50 84 L40 86 M72 66 L78 84 L88 86" fill="none" {W(1.4)}/>'
    + f'<circle cx="64" cy="32" r="13" fill="#E9C08A" {W(3)}/>'
    + f'<path d="M54 24 Q46 2 54 0 Q62 4 60 22Z M74 24 Q82 2 74 0 Q66 4 68 22Z" fill="#F5D6B0" {W(2.4)}/>'
    + face(64, 33, d=5, k=0.55)
    + f'<path d="M52 46 L40 36 M76 46 L88 36" stroke="#E9C08A" stroke-width="4" stroke-linecap="round"/>'
    + sparkle(24, 40, 5) + sparkle(104, 74, 4),
    "песочный тушканчик с длинными ушами и хвостом с кисточкой",
    "взлетает высоко над синим батутом, раскинув лапки")

# «На Донбасской» (бейсбол): бейсбольный мячик въезжает в базу в облаке пыли
add("ms-yug-donbasskaya", "green",
    f'<path d="M-6 84 Q64 70 134 84 V134 H-6Z" fill="#D9A46A" {W(2.6)}/>'
    + f'<path d="M70 92 L96 86 L104 100 L78 106Z" fill="#fff" {W(2.6)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#EED2A8" {W(2)}/>' for x, y, r in [(14, 94, 8), (26, 86, 10), (8, 80, 6), (34, 98, 7)])
    + f'<path d="M30 74 H6 M34 64 H14" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    + f'<circle cx="62" cy="72" r="24" fill="#FFFDF6" {W(3)}/>'
    + f'<path d="M46 54 Q56 72 46 90 M78 54 Q68 72 78 90" fill="none" stroke="{RED}" stroke-width="2.6"/>'
    + "".join(f'<path d="M{x-3} {y} l6 -2 M{x-3} {y+2} l6 2" stroke="{RED}" stroke-width="1.6"/>' for x, y in [(50, 62), (52, 72), (50, 82), (74, 62), (72, 72), (74, 82)])
    + face(62, 70, d=6, k=0.6)
    + f'<path d="M84 72 Q100 60 104 44" fill="none" stroke="#fff" stroke-width="3"/>',
    "бейсбольный мячик с красными швами",
    "въезжает в белую базу на поле, поднимая облако пыли")

# «Россошанский» (бокс): цыплёнок в огромных красных перчатках в углу ринга
add("ms-yug-rossoshansky", "yellow",
    "".join(f'<path d="M-6 {y} H134" stroke="{c}" stroke-width="5"/>' for y, c in [(52, RED), (72, "#fff"), (92, "#3E7FD8")])
    + f'<rect x="106" y="38" width="12" height="96" fill="#C9CED8" {W(2.6)}/>'
    + f'<rect x="-6" y="104" width="140" height="30" fill="#5CB7F2" {W(2.6)}/>'
    + f'<ellipse cx="62" cy="80" rx="26" ry="28" fill="#FFE066" {W(3)}/>'
    + f'<path d="M50 104 L46 116 M74 104 L78 116" stroke="#F28C38" stroke-width="4" stroke-linecap="round"/>'
    + f'<path d="M58 54 Q60 44 66 50" fill="none" {W(2.4)}/>'
    + face(62, 72, d=8, k=0.7, mouth=False)
    + f'<path d="M58 80 L66 80 L62 86Z" fill="#F28C38" {W(2)}/>'
    + "".join(f'<circle cx="{x}" cy="88" r="15" fill="{RED}" {W(3)}/><path d="M{x-8} 80 Q{x} 74 {x+8} 80" fill="none" stroke="#fff" stroke-width="2.4" opacity=".6"/>'
              + f'<rect x="{x-9}" y="100" width="18" height="8" rx="2" fill="#fff" {W(2)}/>' for x in (30, 94)),
    "жёлтый цыплёнок в огромных красных боксёрских перчатках",
    "стоит в стойке в углу ринга у трёх канатов, перчатки больше него самого")

# «Люсиновский» (акробатика): девочка в звёздном купальнике стоит на руках на синем мате
add("ms-yug-lyusinovsky", "pink",
    f'<rect x="10" y="100" width="108" height="16" rx="5" fill="#3E7FD8" {W(3)}/>'
    + f'<path d="M36 100 V116 M64 100 V116 M92 100 V116" stroke="#2E5FB0" stroke-width="2"/>'
    + G(64, 66, f'<path d="M-9 -2 L-24 -36 M9 -2 L24 -36" stroke="{SKIN}" stroke-width="8" stroke-linecap="round"/>'
        f'<path d="M-9 -2 L-24 -36 M9 -2 L24 -36" fill="none" {W(1.4)}/>'
        f'<ellipse cx="-25" cy="-38" rx="6" ry="3" fill="{SKIN}" {W(1.6)}/><ellipse cx="25" cy="-38" rx="6" ry="3" fill="{SKIN}" {W(1.6)}/>'
        f'<path d="M-12 -4 Q-14 18 0 20 Q14 18 12 -4Z" fill="#8A5AD8" {W(2.6)}/>'
        + sparkle(-4, 4, 4, GOLD) + sparkle(6, 12, 3, GOLD)
        + f'<path d="M-12 18 L-18 32 M12 18 L18 32" stroke="{SKIN}" stroke-width="6" stroke-linecap="round"/>'
        f'<circle cx="0" cy="30" r="0" />', rot=180)
    + f'<circle cx="64" cy="86" r="11" fill="{SKIN}" {W(2.6)}/>'
    + f'<path d="M54 92 Q52 104 58 108 M74 92 Q76 104 70 108" fill="none" stroke="#7A4A2E" stroke-width="4"/>'
    + G(64, 86, face(0, 0, d=4, k=0.45), rot=180)
    + sparkle(22, 34, 6) + sparkle(106, 30, 5),
    "девочка-акробатка в фиолетовом купальнике со звёздами",
    "стоит на руках на синем гимнастическом мате, вытянув ноги к потолку")

# «Бутырский» (лёгкая атлетика): эстафетная палочка переходит из руки в руку над беговой дорожкой
add("ms-sever-butyrsky", "orange",
    f'<path d="M-6 90 Q64 78 134 90 V134 H-6Z" fill="#D9603C" {W(2.6)}/>'
    + "".join(f'<path d="M-6 {y} Q64 {y-12} 134 {y}" fill="none" stroke="#fff" stroke-width="2.4"/>' for y in (104, 118))
    + f'<path d="M-6 66 Q16 60 34 62" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>'
    + f'<path d="M134 54 Q112 50 96 54" stroke="#C98A5A" stroke-width="12" stroke-linecap="round"/>'
    + f'<path d="M-6 66 Q16 60 34 62 M134 54 Q112 50 96 54" fill="none" {W(1.6)}/>'
    + G(64, 58, f'<rect x="-30" y="-9" width="60" height="18" rx="9" fill="{RED}" {W(3)}/>'
        f'<path d="M-30 -2 H30" stroke="#fff" stroke-width="2" opacity=".5"/>' + face(0, -1, d=7, k=0.6), rot=-8)
    + f'<circle cx="34" cy="62" r="8" fill="{SKIN}" {W(2.4)}/><circle cx="96" cy="54" r="8" fill="#C98A5A" {W(2.4)}/>'
    + f'<path d="M14 40 H34 M8 48 H24" stroke="#fff" stroke-width="3" stroke-linecap="round"/>',
    "красная эстафетная палочка с улыбкой",
    "переходит из одной руки в другую над красной беговой дорожкой стадиона")

# «Фестивальный» (чир спорт): девочка-чирлидерша в прыжке «звезда» с помпонами
add("ms-sever-festivalny", "blue",
    f'<ellipse cx="64" cy="118" rx="34" ry="6" fill="#2E5FB0" opacity=".35"/>'
    + G(64, 62, kid(shirt="#FFFFFF", hair="#F2B64A", girl=True), sc=0.9)
    + f'<path d="M50 70 L24 38 M78 70 L104 38" stroke="{SKIN}" stroke-width="6" stroke-linecap="round"/>'
    + f'<path d="M54 90 L36 112 M74 90 L92 112" stroke="{SKIN}" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M50 76 H78 L82 92 H46Z" fill="{RED}" {W(2.4)}/>'
    + f'<path d="M52 66 L64 74 L76 66" fill="none" stroke="{RED}" stroke-width="3"/>'
    + "".join(f'<g>' + "".join(f'<path d="M{x} {y} l{8*math.cos(a):.1f} {8*math.sin(a):.1f}" stroke="{c}" stroke-width="4" stroke-linecap="round"/>'
                               for a in [i * math.pi / 6 for i in range(12)]) + f'<circle cx="{x}" cy="{y}" r="5" fill="{c}"/></g>'
              for x, y, c in [(22, 34, GOLD), (106, 34, GOLD)])
    + sparkle(64, 18, 5) + sparkle(16, 80, 4) + sparkle(112, 82, 4),
    "девочка-чирлидерша в бело-красной форме с золотыми помпонами",
    "подпрыгнула в прыжке «звезда», раскинув руки и ноги")

# «Коптево» (самбо): медоед в красной куртке самбо бросает плюшевого мишку через бедро
add("ms-sever-koptevo", "teal",
    f'<rect x="-6" y="100" width="140" height="34" fill="#E8554A"/>'
    + f'<path d="M-6 100 H134" {W(2.6)}/>'
    + f'<circle cx="64" cy="122" r="40" fill="none" stroke="#fff" stroke-width="3" opacity=".6"/>'
    + f'<path d="M30 100 V84 M48 100 V84" stroke="#2A2A30" stroke-width="10" stroke-linecap="round"/>'
    + f'<path d="M24 86 Q22 54 40 52 Q58 54 56 86Z" fill="{RED}" {W(3)}/>'
    + f'<path d="M24 74 H56" stroke="#2A2A30" stroke-width="4"/>'
    + f'<path d="M30 52 Q40 46 50 52" fill="#C9CED8" {W(2)}/>'
    + f'<circle cx="40" cy="40" r="14" fill="#2A2A30" {W(3)}/>'
    + f'<path d="M27 36 Q40 22 53 36 Q40 30 27 36Z" fill="#E6E6EA" {W(2)}/>'
    + eye(35, 42, 0.6) + eye(45, 42, 0.6) + f'<ellipse cx="40" cy="48" rx="3" ry="2" fill="#FF7FA8"/>'
    + f'<path d="M54 60 Q66 52 74 46" stroke="{RED}" stroke-width="8" stroke-linecap="round"/>'
    + G(88, 46, f'<ellipse cx="0" cy="0" rx="16" ry="12" fill="#C98A52" {W(2.6)}/>'
        f'<circle cx="-18" cy="-2" r="10" fill="#C98A52" {W(2.6)}/>'
        f'<circle cx="-24" cy="-10" r="4" fill="#C98A52" {W(2)}/><circle cx="-12" cy="-11" r="4" fill="#C98A52" {W(2)}/>'
        + face(-18, -1, d=3.6, k=0.4)
        + f'<path d="M10 8 L18 18 M2 10 L4 22 M14 -6 L24 -12" stroke="#C98A52" stroke-width="6" stroke-linecap="round"/>', rot=-30)
    + f'<path d="M96 76 q8 -2 14 4 M100 86 q6 0 10 6" fill="none" stroke="#fff" stroke-width="2.6"/>',
    "медоед в красной куртке самбо с серой спинкой",
    "бросает через бедро плюшевого мишку на красном борцовском ковре")

# «Луч» (тяжёлая атлетика): жук-носорог поднимает штангу над головой
add("ms-sever-luch", "night",
    f'<rect x="20" y="104" width="88" height="14" rx="3" fill="#8A6A55" {W(2.6)}/>'
    + f'<path d="M20 34 H108" stroke="#C9CED8" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M20 34 H108" fill="none" {W(1.4)}/>'
    + "".join(f'<rect x="{x}" y="18" width="10" height="32" rx="3" fill="{c}" {W(2.4)}/>' for x, c in [(10, RED), (22, "#3E7FD8"), (96, "#3E7FD8"), (108, RED)])
    + f'<path d="M46 66 L36 40 M82 66 L92 40" stroke="#5A3A2A" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M52 98 L44 106 M76 98 L84 106 M48 86 L34 92 M80 86 L94 92" stroke="#5A3A2A" stroke-width="4" stroke-linecap="round"/>'
    + f'<ellipse cx="64" cy="84" rx="22" ry="18" fill="#7A4A2E" {W(3)}/>'
    + f'<path d="M64 66 V102" stroke="#4A2A1A" stroke-width="2.4"/>'
    + f'<ellipse cx="56" cy="78" rx="5" ry="3" fill="#fff" opacity=".3"/>'
    + f'<ellipse cx="64" cy="64" rx="14" ry="11" fill="#6A3E26" {W(3)}/>'
    + f'<path d="M64 56 Q62 42 72 36 Q70 46 70 56Z" fill="#6A3E26" {W(2.4)}/>'
    + face(64, 66, d=5, k=0.5)
    + sparkle(110, 74, 4) + sparkle(16, 72, 3),
    "коричневый жук-носорог с рогом",
    "на помосте поднимает над головой штангу с красными и синими блинами")

# «Трудовые резервы» (стрельба из лука): кожаный колчан со стрелами, одна стрела улетает
add("ms-vostok-trudovye-rezervy", "sky",
    f'<path d="M-6 104 Q64 92 134 104 V134 H-6Z" fill="#7CD26E" {W(2.6)}/>'
    + "".join(f'<path d="M{x} 50 L{x+dx} 18" stroke="#8A5A3C" stroke-width="3"/>'
              f'<path d="M{x+dx} 18 l-5 -8 l3 10 M{x+dx} 18 l5 -8 l-3 10" fill="{c}" {W(1.6)}/>' for x, dx, c in [(52, -6, RED), (62, 0, GOLD), (72, 6, "#3E7FD8")])
    + f'<path d="M44 46 Q42 104 50 112 H78 Q86 104 84 46Z" fill="#B0703C" {W(3)}/>'
    + f'<path d="M42 46 H86" stroke="#8A4A2A" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M50 70 Q64 76 78 70" fill="none" stroke="#8A4A2A" stroke-width="3" stroke-dasharray="3 3"/>'
    + face(64, 86, d=8, k=0.7)
    + f'<path d="M88 40 L120 22" stroke="#8A5A3C" stroke-width="3"/><path d="M120 22 l-10 0 l6 6Z" fill="#C9CED8" {W(1.6)}/>'
    + f'<path d="M88 40 l-2 -8 l6 4Z M88 40 l8 2 l-6 4Z" fill="#4FBF6B" {W(1.4)}/>'
    + f'<path d="M100 44 H110 M96 50 H104" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>',
    "кожаный колчан со стрелами в цветном оперении",
    "стоит на траве лучного поля, а одна стрела со свистом вылетает из него вверх")

# «Есенинский» (хоккей на траве): деревянная клюшка с загнутым крюком гонит белый мячик по газону
add("ms-vostok-eseninsky", "yellow",
    f'<path d="M-6 92 Q64 80 134 92 V134 H-6Z" fill="#4FBF6B" {W(2.6)}/>'
    + f'<path d="M-6 108 Q64 98 134 108" fill="none" stroke="#fff" stroke-width="3"/>'
    + G(60, 62, f'<path d="M-4 -52 L4 -52 L6 24 Q8 40 -6 42 Q-22 42 -22 32 Q-22 26 -14 26 Q-6 28 -6 22Z" fill="#C9884A" {W(3)}/>'
        f'<rect x="-6" y="-52" width="12" height="20" rx="3" fill="#3B3355"/>'
        + face(0, -4, d=5, k=0.5), rot=-24)
    + f'<circle cx="92" cy="96" r="9" fill="#fff" {W(2.6)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1.4" fill="#C9CED8"/>' for x, y in [(89, 93), (95, 94), (92, 99)])
    + f'<path d="M106 96 H122 M104 88 H116" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>',
    "деревянная клюшка для хоккея на траве с загнутым крюком",
    "ведёт белый мячик по зелёному газону к воротам")

# «Восточный» (настольный теннис): оранжевый шарик балансирует на краю сетки стола
add("ms-vostok-vostochny", "blue",
    f'<path d="M4 92 L28 70 H100 L124 92Z" fill="#2E7A5A" {W(3)}/>'
    + f'<path d="M64 70 V92 M16 81 H112" stroke="#fff" stroke-width="2"/>'
    + f'<path d="M4 92 H124" {W(3)}/>'
    + f'<path d="M22 92 V122 M106 92 V122" stroke="{O}" stroke-width="5"/>'
    + f'<rect x="14" y="62" width="100" height="16" fill="#fff" fill-opacity=".35" {W(2.2)}/>'
    + "".join(f'<path d="M{x} 62 V78" stroke="#fff" stroke-width="1"/>' for x in range(20, 114, 6))
    + f'<path d="M14 62 H114" stroke="#fff" stroke-width="3"/>'
    + f'<circle cx="64" cy="44" r="17" fill="#FF9A3C" {W(3)}/>'
    + face(64, 42, d=6, k=0.6)
    + f'<path d="M44 34 L36 30 M84 34 L92 30" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'
    + f'<path d="M40 50 Q30 52 26 46 M88 50 Q98 52 102 46" fill="none" {W(2)}/>',
    "оранжевый шарик для пинг-понга",
    "балансирует, раскинув ручки, на самом краю сетки зелёного теннисного стола")

# «Москвич» (дзюдо): мангуст в белом кимоно с жёлтым поясом кланяется на татами
add("ms-vostok-moskvich", "pink",
    f'<rect x="-6" y="100" width="140" height="34" fill="#9FD86A"/>'
    + f'<path d="M-6 100 H134 M40 100 V134 M88 100 V134" {W(2.4)}/>'
    + f'<path d="M88 98 Q114 94 118 76 Q120 70 116 66" fill="none" stroke="#B88A5A" stroke-width="8" stroke-linecap="round"/>'
    + f'<path d="M48 100 V86 M70 100 V86" stroke="#B88A5A" stroke-width="9" stroke-linecap="round"/>'
    + G(58, 74, f'<path d="M-20 14 Q-24 -16 0 -20 Q24 -16 22 14Z" fill="#fff" {W(3)}/>'
        f'<path d="M-6 -18 L0 -4 L6 -18" fill="none" {W(2)}/>'
        f'<path d="M-21 2 H23" stroke="{GOLD}" stroke-width="5"/>'
        f'<path d="M0 2 l-6 12 M0 2 l6 12" stroke="{GOLD}" stroke-width="4"/>', rot=28)
    + G(78, 52, f'<ellipse cx="0" cy="0" rx="16" ry="12" fill="#C99A68" {W(3)}/>'
        f'<path d="M12 4 Q24 8 26 2 Q22 -4 12 -4" fill="#C99A68" {W(2.4)}/>'
        f'<circle cx="25" cy="2" r="2" fill="{O}"/>'
        f'<circle cx="-10" cy="-10" r="4" fill="#C99A68" {W(2)}/>'
        + f'<path d="M0 -2 q3 3 6 0 M10 -4 q3 3 6 0" fill="none" {W(2)}/>', rot=36)
    + f'<path d="M30 70 Q36 82 50 88" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round"/>'
    + sparkle(24, 30, 5),
    "мангуст в белом кимоно с жёлтым поясом",
    "почтительно кланяется на зелёном татами перед схваткой")

# «Крылатские Холмы» (сумо): малыш-сумоист в синем маваси топает ногой на круглом дохё
add("ms-zapad-krylatskie-kholmy", "purple",
    f'<ellipse cx="64" cy="114" rx="54" ry="14" fill="#E0C08A" {W(3)}/>'
    + f'<ellipse cx="64" cy="112" rx="40" ry="8" fill="none" stroke="#fff" stroke-width="3"/>'
    + f'<path d="M46 108 L52 86 M82 92 L100 74" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>'
    + f'<ellipse cx="44" cy="110" rx="9" ry="4" fill="{SKIN}" {W(2)}/>'
    + f'<ellipse cx="64" cy="72" rx="30" ry="26" fill="{SKIN}" {W(3)}/>'
    + f'<path d="M36 80 Q64 96 92 80 L90 92 Q64 104 38 92Z" fill="#3E5FC8" {W(2.6)}/>'
    + f'<path d="M64 90 V104" stroke="#3E5FC8" stroke-width="7"/>'
    + f'<path d="M36 64 L18 54 M92 64 L108 50" stroke="{SKIN}" stroke-width="9" stroke-linecap="round"/>'
    + f'<circle cx="64" cy="40" r="15" fill="{SKIN}" {W(3)}/>'
    + f'<path d="M50 34 Q64 20 78 34 Q64 30 50 34Z" fill="#2A2A30" {W(2)}/>'
    + f'<ellipse cx="64" cy="22" rx="6" ry="4" fill="#2A2A30" {W(1.6)}/>'
    + face(64, 42, d=5.5, k=0.55)
    + f'<path d="M94 72 q8 -4 12 -10 M98 80 q8 0 14 -4" fill="none" stroke="#fff" stroke-width="2.4"/>',
    "малыш-сумоист в синем маваси с пучком на макушке",
    "высоко поднял ногу и топает на круглом песочном дохё")

# «На Можайке» (тхэквондо): девочка в добоке бьёт ногой высоко по лапе тренера
add("ms-zapad-na-mozhayke", "teal",
    f'<rect x="-6" y="108" width="140" height="26" fill="#3E7FD8"/>'
    + f'<path d="M-6 108 H134" {W(2.4)}/>'
    + G(44, 64, kid(shirt="#FFFFFF", hair="#3B3355", girl=True))
    + f'<path d="M36 94 L32 110" stroke="#fff" stroke-width="9" stroke-linecap="round"/>'
    + f'<path d="M36 94 L32 110" fill="none" {W(1.4)}/>'
    + f'<path d="M50 88 L92 44" stroke="#fff" stroke-width="10" stroke-linecap="round"/>'
    + f'<path d="M50 88 L92 44" fill="none" {W(1.4)}/>'
    + f'<ellipse cx="94" cy="42" rx="5" ry="4" fill="{SKIN}" {W(2)}/>'
    + f'<path d="M30 80 H58" stroke="#2A2A30" stroke-width="4"/>'
    + f'<path d="M34 70 L20 60 M54 70 L62 58" stroke="{SKIN}" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M104 18 Q120 22 118 40 Q114 52 104 46 Q96 38 104 18Z" fill="{RED}" {W(2.6)}/>'
    + f'<path d="M116 40 L132 50" stroke="#C98A5A" stroke-width="8" stroke-linecap="round"/>'
    + f'<path d="M84 30 l-6 -6 M86 22 l-2 -8 M96 28 l2 -8" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>',
    "девочка в белом добоке с чёрным поясом",
    "бьёт ногой высоко по красной лапе тренера на синем татами")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for pid, code in ICONS.items():
        open(os.path.join(OUT, pid + ".svg"), "w").write(code)
    reg = os.path.join(OUT, "subjects.txt")
    lines = [l for l in open(reg, encoding="utf-8") if l.split(" — ", 1)[0] not in SUBJ]
    lines += [line + "\n" for line in SUBJ.values()]
    open(reg, "w", encoding="utf-8").writelines(lines)
    print(len(ICONS), "иконок:", " ".join(ICONS))
