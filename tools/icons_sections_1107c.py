"""Иконки робота sections, 2026-11-07 (03 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно —
свой герой, своя сцена, своя компоновка и палитра. Якорь вида спорта читается сразу (бадминтон — волан и ракетка со
струнами, баскетбол — оранжевый мяч с чёрными швами и кольцо с сеткой, шахматы — фигуры и клетчатая доска).
Сверено с листами icons-catalog/sheet-01..28 и icons-src/subjects.txt (заняты: волан-персонаж в шапках, мяч-персонаж
с аксессуарами, кольцо-персонаж, кони/пешки/короли-персонажи, жираф/слонёнок/осьминожка/робот/бельчонок с мячом и др.).
Запуск: python3 tools/icons_sections_1107c.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
W = lambda w: s(f'stroke-width="{w}"')
PINK, GOLD, RED, ORG, LIGHT = "#FF7FA8", "#FFC93C", "#E8554A", "#F28C38", "#FFF7EC"
ICONS, SUBJ = {}, {}


def add(pid, bg, body, hero, scene):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def ball(cx, cy, r, fc=True, k=None, c=ORG):
    """баскетбольный мяч"""
    k = k or r / 34
    q = r * 0.62
    out = (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}" {W(3)}/>'
           f'<path d="M{cx-r} {cy} H{cx+r} M{cx} {cy-r} V{cy+r}" fill="none" {W(2.2)}/>'
           f'<path d="M{cx-q} {cy-r*0.78} Q{cx-r*0.2} {cy} {cx-q} {cy+r*0.78} M{cx+q} {cy-r*0.78} Q{cx+r*0.2} {cy} {cx+q} {cy+r*0.78}" fill="none" {W(2.2)}/>')
    if fc:
        out += face(cx, cy + r * 0.15, d=r * 0.26, k=k)
    return out


def hoop(x, y, w=36, board=True, bw=None):
    """кольцо с сеткой; x,y — центр кольца"""
    out = ""
    if board:
        bw = bw or w + 20
        out += (f'<rect x="{x-bw/2}" y="{y-34}" width="{bw}" height="36" rx="4" fill="#fff" {W(3)}/>'
                f'<rect x="{x-w/3}" y="{y-24}" width="{w*2/3}" height="18" fill="none" stroke="{RED}" stroke-width="2.6"/>')
    h = w / 2
    out += (f'<path d="M{x-h} {y} L{x-h*0.7} {y+26} L{x+h*0.7} {y+26} L{x+h} {y}" fill="#fff" fill-opacity=".85" {W(2.4)}/>'
            f'<path d="M{x-h*0.5} {y} L{x-h*0.35} {y+26} M{x} {y} V{y+26} M{x+h*0.5} {y} L{x+h*0.35} {y+26} '
            f'M{x-h*0.85} {y+9} H{x+h*0.85} M{x-h*0.78} {y+18} H{x+h*0.78}" fill="none" {W(1.6)}/>'
            f'<ellipse cx="{x}" cy="{y}" rx="{h+2}" ry="4.5" fill="none" stroke="{RED}" stroke-width="4"/>')
    return out


def shuttle(sc=1.0, fc=True, cork="#FFFFFF", band=RED, feather="#FFFFFF"):
    """волан вокруг (0,0): пробка внизу, юбка из перьев вверх; высота ~80*sc"""
    g = (f'<path d="M-30 -40 L-14 12 H14 L30 -40 Q0 -48 -30 -40Z" fill="{feather}" {W(3)}/>'
         f'<path d="M-15 -43 L-6 12 M0 -45 V12 M15 -43 L6 12" fill="none" {W(1.8)}/>'
         f'<path d="M-24 -20 Q0 -25 24 -20 M-19 -2 Q0 -6 19 -2" fill="none" {W(1.8)}/>'
         f'<rect x="-16" y="10" width="32" height="7" rx="2" fill="{band}" {W(2.6)}/>'
         f'<path d="M-16 17 H16 Q16 38 0 38 Q-16 38 -16 17Z" fill="{cork}" {W(3)}/>')
    if fc:
        g += face(0, 25, d=6.5, k=0.62)
    return f'<g transform="scale({sc})">{g}</g>'


def racket(c="#5CB7F2", grip="#4A4466", sc=1.0, strings=True):
    """ракетка для бадминтона вокруг (0,0): голова вверху (центр 0,-30), ручка вниз до y=+46"""
    out = (f'<rect x="-2.2" y="-6" width="4.4" height="30" fill="#C9CED8" {W(2.2)}/>'
           f'<rect x="-5" y="22" width="10" height="26" rx="4" fill="{grip}" {W(2.4)}/>'
           f'<ellipse cx="0" cy="-30" rx="19" ry="25" fill="#fff" fill-opacity=".55" stroke="{c}" stroke-width="7"/>'
           f'<ellipse cx="0" cy="-30" rx="19" ry="25" fill="none" {W(2.4)}/>'
           f'<ellipse cx="0" cy="-30" rx="22.5" ry="28.5" fill="none" {W(2.4)}/>')
    if strings:
        st = ""
        for i in range(-12, 13, 6):
            hh = 22 * math.sqrt(max(0, 1 - (i / 18) ** 2))
            st += f'M{i} {-30-hh} V{-30+hh} '
        for j in range(-18, 19, 6):
            ww = 16 * math.sqrt(max(0, 1 - (j / 23) ** 2))
            st += f'M{-ww:.1f} {-30+j} H{ww:.1f} '
        out += f'<path d="{st}" fill="none" stroke="{O}" stroke-width="1.1" opacity=".55"/>'
    return f'<g transform="scale({sc})">{out}</g>'


def G(x, y, body, rot=0, sc=1.0):
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({sc})">{body}</g>'


def pawn(c=LIGHT, c2="#E9DCC8", fc=True, k=1.0):
    g = (f'<rect x="-24" y="34" width="48" height="11" rx="4" fill="{c}" {W(3)}/>'
         f'<path d="M-19 36 Q-14 12 -8 2 H8 Q14 12 19 36Z" fill="{c}" {W(3)}/>'
         f'<rect x="-14" y="-4" width="28" height="8" rx="4" fill="{c2}" {W(3)}/>'
         f'<circle cx="0" cy="-21" r="18" fill="{c}" {W(3)}/>')
    if fc:
        g += face(0, -21, d=6.5, k=0.62)
    return f'<g transform="scale({k})">{g}</g>'


def board(x, y, n, c, a="#FFF7EC", b="#8A6A55", w=3):
    out = f'<rect x="{x}" y="{y}" width="{n*c}" height="{n*c}" fill="{a}"/>'
    for i in range(n):
        for j in range(n):
            if (i + j) % 2:
                out += f'<rect x="{x+i*c}" y="{y+j*c}" width="{c}" height="{c}" fill="{b}"/>'
    return out + f'<rect x="{x}" y="{y}" width="{n*c}" height="{n*c}" fill="none" {W(w)}/>'


def cloud(x, y, k=1.0, c="#fff"):
    return (f'<g transform="translate({x} {y}) scale({k})"><path d="M-22 8 Q-30 8 -28 0 Q-28 -10 -16 -9 Q-12 -20 0 -18 '
            f'Q12 -22 16 -10 Q28 -10 27 0 Q28 8 20 8Z" fill="{c}" {W(2.6)}/></g>')


# ============================== БАДМИНТОН ==============================
# «НаТен» (пр-т Вернадского): волан-парашютист — пробка-голова, перья-купол, спускается среди облаков
add("naten-badminton-vernadskogo", "sky",
    cloud(24, 96, 0.9) + cloud(106, 104, 0.7) + cloud(104, 30, 0.6) + cloud(22, 34, 0.5)
    + G(64, 68, shuttle(0.92), rot=0)
    + f'<path d="M47 96 L34 86 M81 96 L94 86" fill="none" {W(3)}/>'
    + f'<path d="M40 22 q2 -6 6 -8 M88 22 q-2 -6 -6 -8" fill="none" stroke="#fff" stroke-width="2.4"/>',
    "волан-парашютист с пробковой головой",
    "плавно опускается пробкой вниз среди облаков, раскинув ручки, перья раскрыты, как купол")

# «НаТен» (Щипковский): ракетка-сачок ловит летящий волан, как бабочку, на цветочной поляне
add("naten-badminton-shchipkovsky", "green",
    f'<path d="M0 104 Q64 88 128 104 V128 H0Z" fill="#9BE07F" {W(2.6)}/>'
    + ''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="{c}" {W(1.8)}/><circle cx="{x}" cy="{y}" r="1.5" fill="{GOLD}"/>'
              for x, y, c in [(22, 104, PINK), (40, 110, "#fff"), (100, 106, "#B79CF2")])
    + G(52, 74, racket("#FF8A3C", sc=1.0) + face(0, -28, d=7, k=0.7), rot=-32)
    + G(92, 40, shuttle(0.42, fc=False), rot=-50)
    + f'<path d="M110 26 q4 -3 8 0 M106 34 q4 -3 8 0" fill="none" {W(2)}/>',
    "ракетка-сачок с оранжевым ободом",
    "размахнулась на цветочной поляне и ловит летящий волан, как бабочку")

# «Высшая лига»: волан-альпинист водрузил флажок на снежной вершине
add("vysshaya-liga-badminton", "purple",
    f'<path d="M-4 128 L40 82 L56 96 L74 70 L132 128Z" fill="#8C7BC9" {W(3)}/>'
    + f'<path d="M64 84 L74 70 L84 84 L79 81 L74 86 L69 81Z" fill="#fff" {W(2.4)}/>'
    + G(72, 34, shuttle(0.72), rot=0)
    + f'<path d="M100 44 V8" {W(3)}/><path d="M100 10 L120 16 L100 22Z" fill="{GOLD}" {W(2.4)}/>'
    + f'<path d="M86 52 L100 44" fill="none" {W(2.6)}/>',
    "волан-альпинист",
    "стоит на самой высокой снежной вершине и держит золотой флажок")

# «Развитие»: росток с листьями-ракетками в горшке, на макушке распускается волан
add("razvitie-badminton-kozhukhovo", "yellow",
    f'<path d="M40 96 H88 L82 122 H46Z" fill="#E07A4F" {W(3)}/><rect x="36" y="88" width="56" height="12" rx="4" fill="#F09A6C" {W(3)}/>'
    + face(64, 106, d=8, k=0.6)
    + f'<path d="M64 88 V44" fill="none" stroke="#5DA84E" stroke-width="5" stroke-linecap="round"/><path d="M64 88 V44" fill="none" {W(1.5)}/>'
    + G(46, 66, racket("#7CD26E", sc=0.5, strings=True), rot=-58)
    + G(82, 70, racket("#7CD26E", sc=0.5, strings=True), rot=58)
    + G(64, 30, shuttle(0.38, fc=False), rot=180)
    + sparkle(96, 26, 5) + sparkle(30, 36, 4),
    "росток в горшке с двумя листьями-ракетками",
    "тянется вверх, а на макушке у него распускается волан вместо бутона")

# «Мастер+»: ракетка-жонглёр подбрасывает три волана по дуге
add("master-plus-badminton", "orange",
    G(64, 76, racket("#4AA3E8", sc=1.05) + face(0, -32, d=7, k=0.72), rot=0)
    + f'<path d="M38 50 Q36 22 64 14 Q92 22 90 50" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="4 5"/>'
    + G(34, 44, shuttle(0.24, fc=False), rot=-150) + G(64, 12, shuttle(0.24, fc=False), rot=180)
    + G(94, 44, shuttle(0.24, fc=False), rot=150)
    + f'<path d="M36 90 L44 78 M92 90 L84 78" fill="none" {W(2.6)}/>',
    "ракетка-жонглёр в синем ободе",
    "подбрасывает по дуге над собой сразу три волана и ловит их по очереди")

# NLBC на Турчаниновом: волан-лебедь плывёт по тихой реке
add("nlbc-badminton-turchaninov", "teal",
    f'<path d="M0 86 Q32 80 64 86 T128 86 V128 H0Z" fill="#7FD3F0" {W(2.6)}/>'
    + f'<path d="M14 100 q8 -4 16 0 M92 110 q8 -4 16 0 M50 116 q8 -4 16 0" fill="none" stroke="#fff" stroke-width="2.4"/>'
    + G(70, 64, shuttle(0.62, fc=False), rot=-90)
    + f'<path d="M44 66 Q36 46 44 34 Q52 26 58 34" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M44 66 Q36 46 44 34 Q52 26 58 34" fill="none" {W(1.8)}/>'
    + f'<circle cx="52" cy="32" r="8" fill="#fff" {W(2.6)}/><path d="M59 31 L68 33 L59 36Z" fill="{ORG}" {W(2)}/>'
    + eye(53, 30, 0.6),
    "волан-лебедь — пробка-туловище, перья-хвост, белая шея",
    "плывёт по тихой реке, оставляя за собой лёгкую рябь")

# Badminton club Сколково: волан-спутник с антеннами на орбите вокруг Земли
add("badminton-club-skolkovo", "night",
    f'<circle cx="26" cy="102" r="22" fill="#5CB7F2" {W(3)}/>'
    + f'<path d="M12 94 Q22 88 26 98 Q30 106 22 114 Q14 112 10 104Z" fill="#7CD26E" {W(2)}/>'
    + f'<ellipse cx="64" cy="64" rx="58" ry="20" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="3 5" transform="rotate(-24 64 64)"/>'
    + G(72, 62, shuttle(0.82), rot=-35)
    + f'<path d="M84 22 L94 10 M70 18 L68 6" fill="none" {W(2.2)}/><circle cx="94" cy="10" r="3" fill="{GOLD}" {W(1.6)}/><circle cx="68" cy="6" r="3" fill="{GOLD}" {W(1.6)}/>'
    + sparkle(110, 92, 4) + sparkle(104, 28, 3) + sparkle(22, 26, 3),
    "волан-спутник с двумя антеннами",
    "облетает голубую Землю по пунктирной орбите в звёздном небе")

# «Мир бадминтона»: белый голубь мира несёт в клюве волан
add("mir-badmintona-leningradka", "pink",
    f'<path d="M14 50 Q20 30 42 34 Q54 36 58 44 L70 40 L64 50 Q56 62 36 60 Q20 60 14 50Z" fill="#fff" {W(3)}/>'
    + f'<path d="M30 44 Q34 20 52 14 Q50 32 44 44" fill="#F3F0FF" {W(3)}/>'
    + eye(54, 44, 0.5) + f'<path d="M60 47 L68 49 L61 51Z" fill="{GOLD}" {W(1.8)}/>'
    + f'<path d="M64 50 L74 62" {W(2)}/>'
    + G(80, 88, shuttle(0.62), rot=-20)
    + f'<path d="M16 50 L4 44 L10 54 L4 62 L18 58" fill="#fff" {W(2.6)}/>',
    "белый голубь мира",
    "летит, расправив крылья, и бережно несёт в клюве волан")

# Сквош-клуб «Москва»: ракетка для бадминтона и ракетка для сквоша меряются ростом спина к спине
add("squash-moskva-badminton", "blue",
    G(48, 72, racket("#7CD26E", sc=0.92) + face(0, -30, d=6.5, k=0.62), rot=0)
    + G(82, 74, f'<rect x="-3" y="-8" width="6" height="26" fill="#C9CED8" {W(2.2)}/><rect x="-6" y="16" width="12" height="22" rx="4" fill="#4A4466" {W(2.4)}/>'
              f'<ellipse cx="0" cy="-26" rx="20" ry="22" fill="#FFE2B8" stroke="#E8554A" stroke-width="7"/><ellipse cx="0" cy="-26" rx="20" ry="22" fill="none" {W(2.4)}/>'
              f'<ellipse cx="0" cy="-26" rx="23.5" ry="25.5" fill="none" {W(2.4)}/>' + face(0, -26, d=6.5, k=0.62), rot=0)
    + f'<path d="M30 18 H100" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="5 4"/>'
    + f'<circle cx="104" cy="104" r="6" fill="#3B3355" {W(2)}/><circle cx="102" cy="102" r="1.5" fill="{GOLD}"/>'
    + G(24, 106, shuttle(0.2, fc=False), rot=-30),
    "две ракетки — длинная бадминтонная и круглая для сквоша",
    "стоят спина к спине и меряются ростом под пунктирной линейкой")

# «Градиор»: из тучки сыплется «град» воланов, ракетка-зонтик укрывает от него
add("gradior-pokryshkina", "sky",
    cloud(64, 28, 1.3, "#DDE6F5")
    + ''.join(G(x, y, shuttle(0.17, fc=False), rot=180) for x, y in [(38, 46), (58, 52), (80, 46), (96, 56), (28, 62)])
    + G(64, 110, racket("#B79CF2", sc=1.0) + face(0, -30, d=7, k=0.7), rot=0)
    + f'<path d="M30 104 q-6 -4 -2 -10 M98 104 q6 -4 2 -10" fill="none" {W(2)}/>',
    "ракетка-зонтик с сиреневым ободом",
    "держит голову над собой и укрывает всех от «града» из воланов, сыплющегося из тучки")

# ============================== БАСКЕТБОЛ ==============================
# «Хаски» (Зелёный пр-т, 10Б): снеговик из трёх баскетбольных мячей
add("husky-basket-zeleny-10", "sky",
    f'<path d="M0 110 Q64 98 128 110 V128 H0Z" fill="#fff" {W(2.6)}/>'
    + ball(64, 96, 22, fc=False) + ball(64, 62, 17, fc=False) + ball(64, 32, 14, fc=False)
    + eye(59, 30, 0.6) + eye(69, 30, 0.6) + f'<path d="M64 34 L76 37 L64 39Z" fill="#FF8A3C" {W(1.8)}/>'
    + f'<path d="M50 46 Q64 52 78 46 L80 54 Q64 58 48 54Z" fill="{RED}" {W(2.4)}/><path d="M74 54 L78 70 L84 68 L80 52" fill="{RED}" {W(2.4)}/>'
    + f'<path d="M47 60 L28 48 M81 60 L100 48" fill="none" stroke="#8A6A55" stroke-width="3.4" stroke-linecap="round"/>'
    + ''.join(f'<circle cx="{x}" cy="{y}" r="2.4" fill="#fff"/>' for x, y in [(20, 20), (104, 26), (30, 80), (108, 70), (92, 14)]),
    "снеговик из трёх баскетбольных мячей",
    "стоит в снежном дворе в красном шарфе, с носом-морковкой и руками-веточками")

# «Хаски» (Авиамоторная): кенгуру-баскетболист прыгает к кольцу, в сумке — запасной мяч
add("husky-basket-aviamotornaya", "orange",
    hoop(98, 40, 26, bw=40)
    + f'<path d="M30 112 Q20 116 12 108" fill="none" stroke="#C98A55" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M30 112 Q20 116 12 108" fill="none" {W(1.6)}/>'
    + f'<path d="M32 112 Q24 80 42 62 Q52 54 60 60 Q72 74 64 104 Q56 118 32 112Z" fill="#D9A06A" {W(3)}/>'
    + f'<path d="M42 92 Q52 98 62 92 Q62 104 52 106 Q42 104 42 92Z" fill="#EBC08E" {W(2.4)}/>'
    + ball(52, 92, 8, fc=False)
    + f'<path d="M54 62 Q50 40 60 30 Q72 24 76 34 Q78 46 66 56Z" fill="#D9A06A" {W(3)}/>'
    + f'<path d="M58 34 L52 14 L62 26 M66 30 L68 10 L72 28" fill="#D9A06A" {W(2.4)}/>'
    + eye(68, 38, 0.6) + f'<circle cx="76" cy="44" r="2" fill="{O}"/>'
    + f'<path d="M64 60 L82 46" fill="none" stroke="#D9A06A" stroke-width="6" stroke-linecap="round"/>'
    + ball(86, 34, 9, fc=False),
    "кенгуру-баскетболист с карманом",
    "в прыжке тянется к кольцу с мячом, а из сумки выглядывает запасной мячик")

# «Хаски» (Рязанский пр-т): плетёная корзинка с мячиками-цыплятами
add("husky-basket-ryazansky", "yellow",
    ball(40, 56, 15, k=0.45) + ball(64, 48, 16, k=0.48) + ball(88, 56, 15, k=0.45)
    + f'<path d="M22 70 H106 L96 112 H32Z" fill="#D7A15F" {W(3)}/>'
    + ''.join(f'<path d="M{x} 70 L{x+(64-x)*0.12:.0f} 112" fill="none" {W(1.6)}/>' for x in range(34, 100, 12))
    + f'<path d="M26 84 H102 M29 98 H99" fill="none" {W(1.6)}/>'
    + sparkle(108, 26, 5),
    "плетёная корзинка с ручкой",
    "из неё, как цыплята из гнезда, выглядывают три маленьких баскетбольных мяча")

# «Хаски» (Правобережная): мяч — воздушный шар с плетёной корзиной над рекой
add("husky-basket-pravoberezhnaya", "teal",
    f'<path d="M0 104 Q32 98 64 104 T128 104 V128 H0Z" fill="#7FD3F0" {W(2.6)}/>'
    + f'<path d="M0 98 Q20 86 40 98Z" fill="#7CD26E" {W(2.4)}/>'
    + ball(64, 44, 30, k=0.85)
    + f'<path d="M44 66 L56 88 M84 66 L72 88" fill="none" {W(2)}/>'
    + f'<path d="M54 86 H74 L72 100 H56Z" fill="#C98A55" {W(2.6)}/><path d="M58 86 V100 M64 86 V100 M70 86 V100" fill="none" {W(1.4)}/>'
    + cloud(22, 30, 0.6) + cloud(108, 72, 0.5),
    "баскетбольный мяч — воздушный шар",
    "поднимается над рекой, под ним на верёвочках плетёная корзина")

# «Хаски» (Новодмитровская): рыжий котёнок свернулся в кольце с сеткой, как в корзинке
add("husky-basket-novodmitrovskaya", "purple",
    f'<rect x="20" y="16" width="88" height="44" rx="5" fill="#fff" {W(3)}/><rect x="44" y="26" width="40" height="24" fill="none" stroke="{RED}" stroke-width="2.6"/>'
    + f'<path d="M40 64 L46 98 H82 L88 64" fill="#fff" fill-opacity=".9" {W(2.4)}/>'
    + f'<path d="M52 64 L56 98 M64 64 V98 M76 64 L72 98 M42 76 H86 M44 88 H84" fill="none" {W(1.5)}/>'
    + f'<path d="M44 66 Q50 44 64 46 Q80 44 84 66Z" fill="#F7A55A" {W(3)}/>'
    + f'<path d="M50 52 L48 38 L58 47 M72 47 L80 38 L80 52" fill="#F7A55A" {W(2.4)}/>'
    + f'<path d="M60 58 q2 2 4 0 M66 58 q2 2 4 0" fill="none" {W(2)}/><path d="M64 61 l-2 2 h4Z" fill="{PINK}"/>'
    + f'<path d="M84 64 Q100 60 98 76" fill="none" stroke="#F7A55A" stroke-width="5" stroke-linecap="round"/>'
    + f'<ellipse cx="64" cy="64" rx="26" ry="5" fill="none" stroke="{RED}" stroke-width="4"/>'
    + ball(30, 104, 11, fc=False) + f'<text x="94" y="40" font-size="12" font-family="Arial" fill="{O}">z</text>',
    "рыжий котёнок",
    "свернулся и дремлет в баскетбольном кольце с сеткой, как в корзинке, а мяч лежит внизу")

# «Хаски» (Химки, Машкинское ш.): малыш на стремянке кладёт мяч в высокое кольцо
add("husky-basket-khimki-mashkinskoe", "green",
    hoop(92, 34, 28, bw=44)
    + f'<path d="M24 122 L42 56 L60 122" fill="none" stroke="#B9844A" stroke-width="5"/><path d="M24 122 L42 56 L60 122" fill="none" {W(1.6)}/>'
    + ''.join(f'<path d="M{42-(y-56)*0.27:.1f} {y} H{42+(y-56)*0.27:.1f}" {W(3)}/>' for y in (72, 88, 104))
    + f'<rect x="34" y="40" width="16" height="18" rx="4" fill="#5CB7F2" {W(2.6)}/>'
    + f'<circle cx="42" cy="30" r="11" fill="#FFD9B8" {W(2.6)}/>' + face(42, 31, d=4, k=0.45)
    + f'<path d="M38 20 Q42 14 48 20" fill="none" stroke="#8A5A3C" stroke-width="3"/>'
    + f'<path d="M48 44 L70 30" fill="none" {W(3)}/>' + ball(76, 26, 9, fc=False),
    "малыш на деревянной стремянке",
    "забрался повыше и аккуратно опускает мяч в высокое кольцо")

# «Хаски» (Смольная): мяч с надутыми щеками накачивают ручным насосом
add("husky-basket-smolnaya", "pink",
    ball(50, 66, 32, fc=False)
    + eye(42, 62, 0.75) + eye(58, 62, 0.75)
    + f'<ellipse cx="34" cy="72" rx="6" ry="4" fill="{PINK}" opacity=".8"/><ellipse cx="66" cy="72" rx="6" ry="4" fill="{PINK}" opacity=".8"/>'
    + f'<circle cx="50" cy="76" r="4" fill="{O}"/>'
    + f'<path d="M82 66 Q92 68 94 80" fill="none" stroke="#3B3355" stroke-width="3"/>'
    + f'<rect x="88" y="80" width="14" height="34" rx="3" fill="#5CB7F2" {W(2.6)}/><path d="M95 80 V56" {W(3)}/>'
    + f'<rect x="84" y="50" width="22" height="7" rx="3" fill="{GOLD}" {W(2.4)}/><rect x="84" y="112" width="22" height="6" rx="2" fill="#4A4466" {W(2)}/>'
    + f'<path d="M24 30 l-4 -6 M32 26 l-1 -7 M18 38 l-7 -2" fill="none" {W(2)}/>',
    "баскетбольный мяч с надутыми щеками",
    "держит воздух, пока его накачивают синим ручным насосом перед тренировкой")

# «Хаски» (Ярославское ш.): мяч и щит с кольцом крепко обнимаются
add("husky-basket-yaroslavskoe", "blue",
    f'<rect x="56" y="18" width="56" height="40" rx="5" fill="#fff" {W(3)}/><rect x="72" y="28" width="24" height="18" fill="none" stroke="{RED}" stroke-width="2.6"/>'
    + eye(76, 36, 0.55) + eye(92, 36, 0.55)
    + f'<path d="M80 44 Q84 48 88 44" fill="none" {W(2)}/>'
    + f'<rect x="80" y="58" width="8" height="64" fill="#9AA3B5" {W(2.6)}/>'
    + ball(48, 80, 26, k=0.75)
    + f'<path d="M62 64 Q76 58 82 70" fill="none" stroke="#F28C38" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M86 62 Q74 70 70 84" fill="none" stroke="#9AA3B5" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M30 22 q4 -6 8 0 q4 -6 8 0 q0 6 -8 12 q-8 -6 -8 -12Z" fill="{RED}" {W(2)}/>',
    "баскетбольный мяч и стойка со щитом",
    "крепко обнимаются после удачного броска, над ними сердечко")

# «Хаски» (Новоясеневский пр-т): лягушонок-баскетболист прыгает с кувшинки и забрасывает мяч
add("husky-basket-novoyasenevsky", "teal",
    f'<path d="M0 100 Q64 92 128 100 V128 H0Z" fill="#6FC5E8" {W(2.6)}/>'
    + f'<ellipse cx="34" cy="106" rx="24" ry="7" fill="#5DBB63" {W(2.6)}/><path d="M34 106 L52 102" {W(2)}/>'
    + hoop(98, 36, 26, bw=40)
    + f'<path d="M44 88 Q40 66 56 58 Q72 54 74 70 Q76 86 60 92Z" fill="#7CD26E" {W(3)}/>'
    + f'<path d="M48 88 L34 98 M60 92 L56 104" fill="none" stroke="#7CD26E" stroke-width="5" stroke-linecap="round"/>'
    + f'<circle cx="54" cy="54" r="7" fill="#7CD26E" {W(2.6)}/><circle cx="68" cy="54" r="7" fill="#7CD26E" {W(2.6)}/>'
    + eye(54, 54, 0.55) + eye(68, 54, 0.55) + f'<path d="M56 66 Q61 70 66 66" fill="none" {W(2)}/>'
    + f'<path d="M70 64 L82 48" fill="none" stroke="#7CD26E" stroke-width="5" stroke-linecap="round"/>'
    + ball(86, 34, 8, fc=False),
    "зелёный лягушонок-баскетболист",
    "оттолкнулся от кувшинки на пруду и в прыжке забрасывает мяч в кольцо")

# «Хаски» (Профсоюзная, 96Б): пирамида из шести мячей, верхний балансирует и машет
add("husky-basket-profsoyuznaya-96", "orange",
    f'<rect x="10" y="112" width="108" height="16" fill="#E8B27A" {W(2.4)}/>'
    + ''.join(ball(x, 98, 13, fc=False) for x in (37, 64, 91))
    + ''.join(ball(x, 74, 13, fc=False) for x in (50, 78))
    + ball(64, 46, 15, k=0.45)
    + f'<path d="M50 44 L40 34 M78 44 L90 30" fill="none" {W(2.6)}/>'
    + sparkle(100, 22, 5) + sparkle(24, 34, 4),
    "пирамида из шести баскетбольных мячей",
    "стоит на паркете, а самый верхний мячик балансирует на вершине и машет руками")

# «Стремление» (Новые Сады): яблоня с мячами вместо яблок, мяч падает в кольцо-корзину
add("stremlenie-basket-novye-sady", "green",
    f'<rect x="38" y="66" width="12" height="52" fill="#9A6B45" {W(2.6)}/>'
    + f'<path d="M10 64 Q4 30 34 20 Q50 2 72 18 Q92 18 88 46 Q90 72 60 72 Q30 80 10 64Z" fill="#5DBB63" {W(3)}/>'
    + ball(24, 46, 7, fc=False) + ball(48, 30, 7, fc=False) + ball(70, 48, 7, fc=False) + ball(40, 58, 7, fc=False)
    + hoop(100, 86, 24, board=False)
    + f'<rect x="114" y="66" width="6" height="58" fill="#9AA3B5" {W(2.2)}/><path d="M112 86 H117" {W(2.4)}/>'
    + ball(98, 64, 9, k=0.28)
    + f'<path d="M86 52 q4 4 6 2" fill="none" stroke="#fff" stroke-width="2"/>',
    "садовая яблоня с баскетбольными мячами вместо яблок",
    "созревший мяч срывается с ветки и падает прямо в кольцо под деревом")

# «Стремление» (Молодёжная): мяч упорно лезет вверх по стойке к кольцу
add("stremlenie-basket-molodezhnaya", "yellow",
    f'<rect x="58" y="34" width="12" height="94" fill="#9AA3B5" {W(2.6)}/>'
    + f'<rect x="34" y="6" width="60" height="32" rx="4" fill="#fff" {W(3)}/><rect x="52" y="14" width="24" height="16" fill="none" stroke="{RED}" stroke-width="2.4"/>'
    + f'<ellipse cx="64" cy="40" rx="16" ry="4" fill="none" stroke="{RED}" stroke-width="4"/>'
    + ball(64, 86, 22, fc=False)
    + eye(58, 80, 0.62) + eye(72, 80, 0.62) + f'<path d="M60 94 H70" {W(2.6)}/>'
    + f'<path d="M44 78 Q50 64 58 62 M84 78 Q78 64 70 62 M48 102 Q54 108 58 104 M80 102 Q74 108 70 104" fill="none" stroke="{ORG}" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M30 92 l-6 2 M28 82 l-7 -1 M98 92 l6 2" fill="none" {W(2)}/>'
    + f'<path d="M92 56 q6 -10 0 -16" fill="none" stroke="#66C2F0" stroke-width="3" stroke-linecap="round"/>',
    "упорный баскетбольный мяч с ручками и ножками",
    "изо всех сил карабкается вверх по стойке к кольцу, капелька пота летит в сторону")

# «Стремление» (Кутузовская): сова-судья со свистком подбрасывает мяч в спорном броске
add("stremlenie-basket-kutuzovskaya", "night",
    f'<path d="M30 122 Q26 70 64 64 Q102 70 98 122Z" fill="#9C7A5A" {W(3)}/>'
    + f'<path d="M40 122 V82 M52 122 V74 M64 122 V72 M76 122 V74 M88 122 V82" stroke="#fff" stroke-width="5"/>'
    + f'<path d="M40 122 V82 M52 122 V74 M64 122 V72 M76 122 V74 M88 122 V82" stroke="{O}" stroke-width="1.2"/>'
    + f'<circle cx="64" cy="58" r="22" fill="#B48A64" {W(3)}/><path d="M46 42 L44 28 L56 38 M82 42 L84 28 L72 38" fill="#B48A64" {W(2.6)}/>'
    + f'<circle cx="55" cy="56" r="8" fill="#fff" {W(2)}/><circle cx="73" cy="56" r="8" fill="#fff" {W(2)}/>' + eye(55, 56, 0.6) + eye(73, 56, 0.6)
    + f'<path d="M64 62 L60 68 H68Z" fill="{GOLD}" {W(2)}/>'
    + f'<rect x="66" y="66" width="14" height="7" rx="3" fill="#C9CED8" {W(2)}/><path d="M64 68 Q58 74 60 84" fill="none" stroke="#C9CED8" stroke-width="1.6"/>'
    + f'<path d="M94 84 Q108 70 106 46" fill="none" stroke="#9C7A5A" stroke-width="7" stroke-linecap="round"/>'
    + ball(104, 30, 11, fc=False) + sparkle(22, 24, 4) + sparkle(30, 50, 3),
    "сова-судья в полосатой форме со свистком",
    "подбрасывает мяч крылом для спорного броска в начале матча")

# IBASKET (Никулинская): черепаха несёт мяч на панцире к кольцу
add("ibasket-troparevo", "teal",
    hoop(104, 44, 22, bw=34)
    + f'<path d="M0 108 H128 V128 H0Z" fill="#E8B27A" {W(2.4)}/>'
    + f'<path d="M22 104 Q24 72 54 70 Q84 72 86 104Z" fill="#6DBE6A" {W(3)}/>'
    + f'<path d="M36 102 L42 84 L56 80 L68 84 L74 102 M42 84 L36 76 M68 84 L76 78" fill="none" {W(2)}/>'
    + f'<path d="M86 100 Q98 98 100 86 Q100 76 92 76 Q84 78 84 90" fill="#9BD98C" {W(3)}/>'
    + eye(93, 84, 0.55) + f'<path d="M90 92 Q94 94 97 91" fill="none" {W(1.8)}/>'
    + f'<path d="M30 104 V112 M46 104 V112 M66 104 V112 M78 104 V112" stroke="#9BD98C" stroke-width="6" stroke-linecap="round"/>'
    + ball(54, 56, 15, fc=False),
    "неторопливая черепаха",
    "везёт баскетбольный мяч на панцире через весь паркет к кольцу")

# ОЦ «Протон»: мяч — ядро атома, вокруг по орбитам летают мячики-электроны
add("proton-basket-fili", "purple",
    ''.join(f'<ellipse cx="64" cy="64" rx="50" ry="17" fill="none" stroke="#fff" stroke-width="2.6" transform="rotate({a} 64 64)"/>'
            for a in (0, 60, 120))
    + ball(64, 64, 22, k=0.65)
    + ball(114, 64, 7, fc=False) + ball(39, 21, 7, fc=False) + ball(39, 107, 7, fc=False)
    + sparkle(104, 22, 4) + sparkle(20, 70, 3),
    "баскетбольный мяч — ядро атома",
    "в центре, а вокруг по трём орбитам носятся маленькие мячики-электроны")

# СК «Восход»: мяч в ночном колпаке потягивается у окна на рассвете
add("voskhod-basket-fili", "pink",
    f'<rect x="74" y="14" width="44" height="48" rx="4" fill="#FFE7A8" {W(3)}/>'
    + f'<circle cx="96" cy="56" r="13" fill="#FF8A3C" {W(2.4)}/>'
    + f'<path d="M96 14 V62 M74 38 H118" fill="none" {W(2.6)}/><rect x="74" y="14" width="44" height="48" rx="4" fill="none" {W(3)}/>'
    + ball(52, 80, 30, fc=False)
    + f'<path d="M40 76 q4 4 8 0 M56 76 q4 4 8 0" fill="none" {W(2.4)}/><ellipse cx="52" cy="92" rx="5" ry="6" fill="{O}"/>'
    + f'<path d="M30 56 Q40 30 64 44 Q50 46 44 54Z" fill="#5CB7F2" {W(2.6)}/><circle cx="66" cy="44" r="5" fill="#fff" {W(2)}/>'
    + f'<path d="M24 74 L10 52 M80 74 L92 70" fill="none" stroke="{ORG}" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M14 40 l-4 -4 M20 34 l0 -6" fill="none" {W(2)}/>',
    "сонный баскетбольный мяч в ночном колпаке",
    "просыпается и сладко потягивается у окна, за которым встаёт солнце")

# ============================== ШАХМАТЫ ==============================
# Chess First (Ландышевая): ландыш, у которого вместо колокольчиков — белые пешки
add("chessfirst-landyshevaya", "green",
    f'<path d="M64 124 V40 Q64 22 84 18" fill="none" stroke="#4E9A44" stroke-width="4" stroke-linecap="round"/>'
    + f'<path d="M64 124 Q30 100 34 50 Q52 80 64 110Z" fill="#7CD26E" {W(3)}/><path d="M64 124 Q96 104 96 66 Q80 90 66 112Z" fill="#6CC45F" {W(3)}/>'
    + ''.join(f'<path d="M{x} {y-10} Q{x} {y-14} {x+2} {y-16}" fill="none" stroke="#4E9A44" stroke-width="2.4"/>' + G(x, y, pawn(k=0.36, fc=False))
              for x, y in [(70, 36), (84, 30), (98, 34)])
    + face(84, 22, d=3.6, k=0.4, mouth=False)
    + G(38, 30, pawn(k=0.44), rot=0),
    "ландыш с белыми пешками вместо колокольчиков",
    "раскачивает на стебле пешки-бутоны, а самая смелая пешка уже «расцвела» рядом")

# Chess First (Лобачевского, детский сад): пешка-малыш спит в шахматной коробке-кроватке
add("chessfirst-lobachevskogo", "sky",
    f'<path d="M14 80 H114 V112 H14Z" fill="#B9844A" {W(3)}/>'
    + board(18, 84, 6, 4.6, a="#F3D9B1", b="#8A5A3C", w=0)
    + f'<rect x="46" y="84" width="66" height="26" fill="#C9965A"/><path d="M14 80 H114 V112 H14Z" fill="none" {W(3)}/>'
    + f'<path d="M30 80 Q30 58 48 58 Q60 58 62 70" fill="#fff" {W(2.6)}/>'
    + f'<circle cx="46" cy="66" r="13" fill="{LIGHT}" {W(3)}/>'
    + f'<path d="M40 66 q3 3 6 0 M48 66 q3 3 6 0" fill="none" {W(2)}/><ellipse cx="38" cy="72" rx="3.6" ry="2.2" fill="{PINK}" opacity=".7"/>'
    + f'<path d="M54 72 Q80 64 112 74 V82 H54Z" fill="#B79CF2" {W(2.6)}/><path d="M62 72 V82 M76 70 V82 M90 70 V82 M104 72 V82" fill="none" stroke="#fff" stroke-width="1.6"/>'
    + f'<text x="72" y="44" font-size="14" font-family="Arial" fill="{O}">z</text><text x="86" y="32" font-size="18" font-family="Arial" fill="{O}">Z</text>'
    + f'<path d="M14 80 L6 60 L22 60 Z" fill="#C9965A" {W(2.4)}/>',
    "пешка-малыш",
    "сладко спит в деревянной шахматной коробке, как в кроватке, укрывшись сиреневым одеялом")

# EduChess (Мосфильмовская): чёрный слон-режиссёр в берете командует в рупор пешками
add("educhess-mosfilmovskaya", "orange",
    board(8, 98, 10, 12, a="#FFF2DC", b="#C98A55", w=0) + f'<path d="M0 98 H128" {W(2.6)}/>'
    + G(36, 72, f'<rect x="-20" y="18" width="40" height="10" rx="4" fill="#E9DCC8" {W(3)}/>'
                f'<path d="M-15 20 Q-12 -4 -14 -12 Q-14 -34 0 -42 Q14 -34 14 -12 Q12 -4 15 20Z" fill="{LIGHT}" {W(3)}/>'
                f'<path d="M6 -34 L-4 -20" fill="none" {W(2.6)}/><circle cx="0" cy="-46" r="4" fill="{LIGHT}" {W(2.4)}/>'
                f'<path d="M-16 -36 Q-10 -46 2 -40 Q-6 -34 -16 -36Z" fill="{RED}" {W(2.2)}/>'
                + face(0, -22, d=5.5, k=0.55))
    + f'<path d="M50 60 L76 46 L80 70 L52 66Z" fill="{GOLD}" {W(2.6)}/>'
    + f'<path d="M86 50 q6 6 0 14 M92 44 q10 12 0 26" fill="none" {W(2.2)}/>'
    + G(98, 96, pawn(k=0.32, fc=False)) + G(114, 98, pawn(k=0.26, fc=False))
    + face(98, 89, d=2.4, k=0.32, mouth=False) + face(114, 92, d=2, k=0.28, mouth=False),
    "белый шахматный слон-режиссёр в красном берете",
    "кричит «Мотор!» в жёлтый рупор маленьким пешкам-актёрам на съёмочной площадке-доске")

# EduChess (Крылатская): шахматный конь-Пегас с крыльями летит над холмами Крылатского
add("educhess-krylatskaya", "blue",
    f'<path d="M0 110 Q34 88 70 104 Q100 92 128 104 V128 H0Z" fill="#7CD26E" {W(2.6)}/>'
    + f'<path d="M58 60 Q34 34 20 44 Q30 50 26 58 Q40 56 40 66 Q50 62 58 68Z" fill="#fff" {W(3)}/>'
    + G(70, 64, f'<rect x="-22" y="26" width="44" height="9" rx="3" fill="#E9DCC8" {W(3)}/>'
                f'<path d="M-15 26 C-20 8 -16 -10 -8 -20 L-11 -34 L0 -26 C16 -28 26 -16 25 -2 L15 0 C9 0 6 3 9 9 C12 14 15 18 16 26Z" fill="{LIGHT}" {W(3)}/>'
                + eye(8, -15, 0.6) + f'<ellipse cx="14" cy="-7" rx="4" ry="2.4" fill="{PINK}" opacity=".7"/>', sc=1.05)
    + f'<path d="M64 52 Q82 22 106 26 Q98 34 102 40 Q88 40 86 50 Q78 46 70 56Z" fill="#fff" {W(3)}/>'
    + cloud(102, 70, 0.55) + sparkle(30, 22, 4),
    "белый шахматный конь-Пегас с крыльями",
    "летит над зелёными холмами Крылатского, раскинув белые крылья")

# EduChess (Инициативная): детская ладошка делает первый ход ферзём
add("educhess-initsiativnaya", "yellow",
    board(14, 76, 8, 12.5, a="#FFF7EC", b="#7FB6E8", w=3)
    + G(78, 62, f'<rect x="-16" y="14" width="32" height="8" rx="3" fill="#F3F0FF" {W(2.6)}/>'
                f'<path d="M-12 14 Q-8 -6 -12 -18 L-6 -12 L-4 -24 L0 -14 L4 -24 L6 -12 L12 -18 Q8 -6 12 14Z" fill="#F3F0FF" {W(2.6)}/>'
                f'<circle cx="0" cy="-27" r="3.6" fill="{GOLD}" {W(2)}/>' + face(0, -2, d=4.5, k=0.45))
    + f'<path d="M96 22 Q112 30 108 50 L100 66 Q94 72 86 66 L80 56 Q76 50 82 48 L88 52 L84 36 Q82 30 88 30 L92 40 L92 26 Q94 20 96 22Z" fill="#FFD9B8" {W(3)}/>'
    + f'<path d="M30 70 L44 64" fill="none" stroke="{RED}" stroke-width="3" stroke-dasharray="3 3"/>'
    + sparkle(30, 30, 6) + sparkle(48, 18, 3),
    "детская ладошка",
    "держит белого ферзя двумя пальцами и делает свой первый ход на голубой доске")

# EduChess (Удальцова): клетчатый ковёр-самолёт с пешкой летит среди облаков
add("educhess-udaltsova", "purple",
    cloud(26, 34, 0.8) + cloud(104, 96, 0.7)
    + f'<path d="M14 84 L92 70 L118 92 L38 108Z" fill="#E8554A" {W(3)}/>'
    + ''.join(f'<path d="M{14+(92-14)*t:.1f} {84+(70-84)*t:.1f} L{38+(118-38)*t:.1f} {108+(92-108)*t:.1f}" stroke="#FFC93C" stroke-width="1.6"/>' for t in (0.25, 0.5, 0.75))
    + ''.join(f'<path d="M{14+(38-14)*t:.1f} {84+(108-84)*t:.1f} L{92+(118-92)*t:.1f} {70+(92-70)*t:.1f}" stroke="#FFC93C" stroke-width="1.6"/>' for t in (0.33, 0.66))
    + f'<path d="M14 84 L8 90 M38 108 L32 116 M118 92 L124 96" fill="none" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>'
    + G(66, 58, pawn(k=0.7))
    + f'<path d="M50 44 L40 36 M82 44 L92 34" fill="none" {W(2.6)}/>',
    "белая пешка на клетчатом ковре-самолёте",
    "летит на красном ковре в клеточку среди облаков, радостно раскинув руки")

# Шахматная школа №1 (библиотека на Озёрной): пешка в очках читает книгу на берегу озера
add("chess1-ozernaya", "teal",
    f'<path d="M0 92 Q40 84 80 92 Q104 96 128 90 V128 H0Z" fill="#6FC5E8" {W(2.6)}/>'
    + f'<path d="M66 128 Q70 96 128 96 V128Z" fill="#E8D08A" {W(2.6)}/>'
    + f'<path d="M84 96 V74 M84 74 q-8 -10 -2 -18 M84 74 q8 -10 2 -18" fill="none" stroke="#4E9A44" stroke-width="3"/>'
    + f'<ellipse cx="84" cy="54" rx="4" ry="9" fill="#8A5A3C" {W(2)}/>'
    + G(42, 70, pawn(c="#3B3355", c2="#5A5378", fc=False, k=0.85))
    + f'<circle cx="37" cy="52" r="5" fill="none" stroke="#fff" stroke-width="2.4"/><circle cx="49" cy="52" r="5" fill="none" stroke="#fff" stroke-width="2.4"/><path d="M42 52 H44" stroke="#fff" stroke-width="2.4"/>'
    + f'<circle cx="37" cy="52" r="1.8" fill="#fff"/><circle cx="49" cy="52" r="1.8" fill="#fff"/>'
    + f'<path d="M26 70 L42 66 L58 70 L58 84 L42 80 L26 84Z" fill="#fff" {W(2.6)}/><path d="M42 66 V80" {W(1.8)}/>'
    + f'<path d="M30 74 H38 M46 74 H54" stroke="{O}" stroke-width="1.2"/>'
    + f'<path d="M14 104 q8 -4 16 0 M96 112 q8 -4 16 0" fill="none" stroke="#fff" stroke-width="2.2"/>',
    "чёрная пешка-книгочей в круглых очках",
    "читает раскрытую книгу на берегу озера у камышей")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for pid, code in ICONS.items():
        open(os.path.join(OUT, pid + ".svg"), "w").write(code)
    reg = os.path.join(OUT, "subjects.txt")
    lines = [l for l in open(reg, encoding="utf-8") if l.split(" — ", 1)[0] not in SUBJ]
    lines += [line + "\n" for line in SUBJ.values()]
    open(reg, "w", encoding="utf-8").writelines(lines)
    print(len(ICONS), "иконок:", " ".join(ICONS))
