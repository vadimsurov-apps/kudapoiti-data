"""Иконки робота sections, 2026-11-07 (09 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно —
свой герой, своя сцена, своя компоновка и палитра; вид спорта читается по якорю (баскетбол — оранжевый мяч/кольцо,
волейбол — бело-жёлто-синий мяч, гандбол — ворота в полоску, бадминтон — волан и ракетка, шахматы — фигуры и доска,
фехтование — шпага/меч). Сверено с листами icons-catalog/sheet-01..31 и icons-src/subjects.txt.
Запуск: python3 tools/icons_sections_1107e.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import svg, s, eye, face, sparkle, O
from icons_sections_1107d import (shuttle, racket, vball, net, pawn, rook, queen, knight_head, cloud, sword, kid, G, W,
                                  PINK, GOLD, RED, ORG, LIGHT)
from icons_sections_1107c import ball, hoop
from icons_sections_1107b import knight

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
DARK = "#3B3355"


def add(pid, bg, body, hero, scene):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def checks(x, y, n, m, c, a="#FFF7EC", b="#8A6A55", w=1.2):
    """клетчатое поле n×m клеток размером c"""
    out = f'<rect x="{x}" y="{y}" width="{n*c}" height="{m*c}" fill="{a}" {W(2.6)}/>'
    out += "".join(f'<rect x="{x+i*c}" y="{y+j*c}" width="{c}" height="{c}" fill="{b}"/>'
                   for i in range(n) for j in range(m) if (i + j) % 2)
    return out + f'<rect x="{x}" y="{y}" width="{n*c}" height="{m*c}" fill="none" {W(2.6)}/>'


# ============================== БАСКЕТБОЛ ==============================
# «Стремление», Калитниковская: кенгурёнок выпрыгивает из маминой сумки... нет — сам кенгуру несёт мяч в сумке и прыгает к кольцу
add("stremlenie-basket-kalitniki", "green",
    hoop(98, 40, w=30, bw=46)
    + f'<path d="M30 118 Q22 96 30 76 Q36 60 52 60 Q66 60 70 76 Q74 96 64 112" fill="#C98A52" {W(3)}/>'
    + f'<path d="M64 112 Q80 122 100 118" fill="none" stroke="#C98A52" stroke-width="9" stroke-linecap="round"/>'
    + f'<path d="M64 112 Q80 122 100 118" fill="none" {W(1.6)}/>'
    + f'<path d="M40 100 Q52 108 64 98 L62 90 Q50 94 40 92Z" fill="#E0B07A" {W(2.4)}/>'
    + ball(52, 88, 10, fc=False)
    + f'<circle cx="50" cy="48" r="17" fill="#C98A52" {W(3)}/>'
    + f'<path d="M38 36 L32 14 L46 32Z M58 34 L62 12 L66 34Z" fill="#C98A52" {W(2.6)}/>'
    + face(50, 48, d=6, k=0.6)
    + f'<path d="M66 64 L82 50" fill="none" stroke="#C98A52" stroke-width="6" stroke-linecap="round"/>'
    + f'<path d="M14 122 h20 M8 116 h12" fill="none" stroke="#fff" stroke-width="3" opacity=".7"/>',
    "кенгуру-баскетболистка с мячом в сумке на животе",
    "прыгает на хвосте к кольцу и тянет лапу, чтобы положить мяч")

# «Стремление», Сокольники: сова-судья со свистком на щите, мяч влетает в кольцо, сосны парка
add("stremlenie-basket-egerskaya", "night",
    "".join(f'<path d="M{x} 128 L{x} 100 M{x-14} 112 L{x} 84 L{x+14} 112Z" fill="#2E6B4A" stroke="#1F4A33" stroke-width="2"/>' for x in (14, 116))
    + hoop(64, 86, w=40, bw=62)
    + f'<ellipse cx="64" cy="30" rx="20" ry="22" fill="#A07A5A" {W(3)}/>'
    + f'<path d="M46 16 L50 4 L56 12 M82 16 L78 4 L72 12" fill="#A07A5A" {W(2.4)}/>'
    + f'<circle cx="56" cy="26" r="8" fill="#FFF3D6" {W(2)}/><circle cx="72" cy="26" r="8" fill="#FFF3D6" {W(2)}/>'
    + eye(56, 26, 0.8) + eye(72, 26, 0.8)
    + f'<path d="M62 33 L64 38 L66 33Z" fill="{GOLD}" {W(1.6)}/>'
    + f'<rect x="64" y="38" width="12" height="6" rx="3" fill="#C9CED8" {W(2)}/>'
    + f'<path d="M80 40 l10 -4 M82 46 l10 0" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'
    + ball(34, 70, 11, fc=False)
    + f'<path d="M22 84 q-6 8 -4 18" fill="none" stroke="#fff" stroke-width="2.2" stroke-dasharray="3 4"/>',
    "сова-судья со свистком в клюве",
    "сидит на верхушке баскетбольного щита среди сосен Сокольников и свистит, когда мяч летит к кольцу")

# «Стремление», Шелепиха: вагон-платформа МЦК, гружённый горкой баскетбольных мячей
add("stremlenie-basket-shelepikha", "sky",
    f'<path d="M-4 108 H132" stroke="#8A6A55" stroke-width="4"/>'
    + "".join(f'<rect x="{x}" y="108" width="4" height="10" fill="#8A6A55"/>' for x in range(2, 128, 14))
    + f'<rect x="10" y="78" width="96" height="20" rx="4" fill="#E8554A" {W(3)}/>'
    + f'<rect x="106" y="84" width="14" height="8" fill="#C9CED8" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="104" r="7" fill="#4A4466" {W(2.4)}/>' for x in (26, 46, 74, 94))
    + ball(30, 66, 12, fc=False) + ball(56, 66, 12, fc=False) + ball(82, 66, 12, fc=False)
    + ball(44, 44, 13, fc=False) + ball(70, 42, 14)
    + face(58, 88, d=8, k=0.7),
    "красная грузовая платформа-вагончик с глазками",
    "везёт по рельсам горку из пяти баскетбольных мячей, верхний мяч улыбается")

# «Спартаковец», Красная Пресня: малыш-гладиатор в шлеме с гребнем забрасывает мяч сверху
add("spartakovets-basket-presnya", "orange",
    hoop(92, 44, w=34, bw=50)
    + G(54, 92, kid(shirt="#E8554A", hair="#7A4A2E"))
    + f'<path d="M36 70 Q54 46 72 70Z" fill="#C9CED8" {W(3)}/>'
    + f'<path d="M40 52 Q54 34 72 50 L70 56 Q54 44 42 58Z" fill="#E8554A" {W(2.4)}/>'
    + f'<path d="M58 54 V72" {W(2)}/>'
    + f'<path d="M66 96 L80 62" fill="none" stroke="#FFD8B8" stroke-width="7" stroke-linecap="round"/>'
    + ball(84, 50, 11, fc=False)
    + f'<rect x="42" y="100" width="24" height="4" fill="#fff"/>',
    "малыш-гладиатор в серебряном шлеме с красным гребнем",
    "в прыжке вколачивает мяч в кольцо сверху, как римский чемпион")

# «Спартаковец», Авиамоторная: самолётик-кукурузник с кольцом на хвосте, мяч пролетает сквозь него
add("spartakovets-basket-aviamotornaya", "blue",
    cloud(28, 98, 0.9) + cloud(104, 24, 0.7)
    + f'<path d="M20 60 Q60 50 96 58 L104 46 L112 48 L108 64 Q60 76 20 66Z" fill="#FFC93C" {W(3)}/>'
    + f'<rect x="40" y="38" width="44" height="7" rx="3" fill="#FFE27A" {W(2.6)}/><rect x="40" y="76" width="44" height="7" rx="3" fill="#FFE27A" {W(2.6)}/>'
    + f'<path d="M50 45 V58 M74 45 V56 M50 66 V76 M74 64 V76" {W(2.2)}/>'
    + f'<ellipse cx="16" cy="63" rx="4" ry="16" fill="#C9CED8" {W(2.2)}/>'
    + face(32, 62, d=5, k=0.5)
    + f'<path d="M106 48 V40" {W(2.4)}/><ellipse cx="106" cy="38" rx="10" ry="3.5" fill="none" stroke="{RED}" stroke-width="3.5"/>'
    + ball(96, 26, 8, fc=False)
    + f'<path d="M84 22 q-8 -6 -16 -2" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="2 3"/>',
    "жёлтый самолётик-биплан с баскетбольным кольцом на хвосте",
    "летит между облаками, а мяч ныряет в кольцо прямо в небе")

# «Прогресс»: грузовой корабль «Прогресс» стыкуется с кольцом-станцией, в люке мяч
add("progress-basket-solntsevo", "night",
    sparkle(18, 22, 4) + sparkle(104, 104, 5, "#FFE27A") + sparkle(22, 96, 3) + sparkle(112, 20, 3, "#FFE27A")
    + f'<rect x="76" y="20" width="44" height="22" fill="#5CB7F2" {W(2.4)}/><path d="M76 31 H120 M90 20 V42 M104 20 V42" {W(1.4)}/>'
    + f'<rect x="8" y="78" width="40" height="22" fill="#5CB7F2" {W(2.4)}/><path d="M8 89 H48 M21 78 V100 M34 78 V100" {W(1.4)}/>'
    + f'<g transform="rotate(-40 64 64)"><path d="M44 50 H84 V96 H44Z" fill="#E7EAF0" {W(3)}/>'
    + f'<path d="M50 50 Q64 22 78 50Z" fill="#E7EAF0" {W(3)}/><rect x="40" y="96" width="48" height="8" rx="3" fill="#A8AFBD" {W(2.6)}/></g>'
    + ball(64, 70, 13)
    + f'<ellipse cx="98" cy="58" rx="10" ry="4" fill="none" stroke="{RED}" stroke-width="3.5"/><path d="M98 54 V42" {W(2.4)}/>',
    "космический грузовик «Прогресс» с баскетбольным мячом в иллюминаторе",
    "стыкуется в звёздном небе, и мяч смотрит на кольцо орбитальной станции")

# «Медведи»: бурый медвежонок висит на кольце после данка
add("medvedi-basket-prospekt-mira", "yellow",
    f'<rect x="20" y="10" width="88" height="44" rx="5" fill="#fff" {W(3)}/><rect x="48" y="22" width="32" height="20" fill="none" stroke="{RED}" stroke-width="2.6"/>'
    + f'<ellipse cx="64" cy="54" rx="20" ry="5" fill="none" stroke="{RED}" stroke-width="4"/>'
    + f'<path d="M44 54 L48 70 H80 L84 54" fill="#fff" fill-opacity=".7" {W(1.6)}/>'
    + f'<ellipse cx="64" cy="98" rx="20" ry="22" fill="#8A5A3C" {W(3)}/>'
    + f'<path d="M48 84 Q40 70 46 56 M80 84 Q88 70 82 56" fill="none" stroke="#8A5A3C" stroke-width="10" stroke-linecap="round"/>'
    + f'<circle cx="64" cy="80" r="16" fill="#8A5A3C" {W(3)}/>'
    + f'<circle cx="51" cy="67" r="6" fill="#8A5A3C" {W(2.4)}/><circle cx="77" cy="67" r="6" fill="#8A5A3C" {W(2.4)}/>'
    + f'<ellipse cx="64" cy="86" rx="7" ry="5" fill="#E0B07A"/>'
    + face(64, 80, d=6, k=0.55)
    + ball(64, 66, 8, fc=False)
    + f'<ellipse cx="64" cy="102" rx="10" ry="12" fill="#E0B07A" opacity=".8"/>',
    "бурый медвежонок-баскетболист",
    "повис на кольце обеими лапами после броска сверху, мяч проскакивает сквозь сетку над его носом")

# «Академия Будущего», Терехово: летающая тарелка с кольцом снизу ловит мяч
add("akademiya-budushchego-terekhovo", "purple",
    sparkle(20, 24, 4) + sparkle(108, 30, 3) + sparkle(98, 108, 4)
    + f'<ellipse cx="64" cy="36" rx="18" ry="14" fill="#B8F0E6" fill-opacity=".8" {W(3)}/>'
    + f'<ellipse cx="64" cy="48" rx="44" ry="12" fill="#C9CED8" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="50" r="3" fill="{GOLD}" {W(1.4)}/>' for x in (34, 50, 64, 78, 94))
    + face(64, 34, d=5, k=0.5)
    + f'<ellipse cx="64" cy="62" rx="14" ry="4" fill="none" stroke="{RED}" stroke-width="3.5"/>'
    + f'<path d="M50 62 L54 76 H74 L78 62" fill="none" {W(1.4)}/>'
    + f'<path d="M48 64 L36 112 H92 L80 64Z" fill="#FFF7A8" opacity=".45"/>'
    + ball(64, 98, 13),
    "летающая тарелка с баскетбольным кольцом на днище",
    "зелёным лучом затягивает улыбающийся мяч снизу вверх прямо в корзину")

# «Академия Будущего», Черёмушки (баскетбол + художественная гимнастика): лента спиралью вокруг летящего мяча
add("akademiya-budushchego-cheryomushki", "pink",
    f'<path d="M14 112 Q30 72 64 84 Q100 96 92 60 Q84 28 50 40 Q24 50 44 22 Q56 6 80 14" fill="none" stroke="#9B6BE8" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M14 112 l-8 6" stroke="#8A5A3C" stroke-width="5" stroke-linecap="round"/>'
    + ball(66, 60, 22)
    + f'<path d="M82 74 Q94 82 90 98" fill="none" stroke="#9B6BE8" stroke-width="7" stroke-linecap="round"/>'
    + sparkle(104, 24, 5) + sparkle(24, 30, 4),
    "сиреневая гимнастическая лента на палочке",
    "закручивается спиралью вокруг летящего баскетбольного мяча")

# TeenBasket, 16-я Парковая: подросток в худи ведёт мяч между ног на уличной площадке
add("teenbasket-shchelkovskaya", "teal",
    f'<path d="M0 104 H128 V128 H0Z" fill="#7A8396"/><path d="M10 116 Q64 100 118 116" fill="none" stroke="#fff" stroke-width="2.4"/>'
    + f'<path d="M48 108 L40 72 H88 L80 108" fill="none" stroke="#2C3E66" stroke-width="10" stroke-linecap="round"/>'
    + f'<path d="M42 78 Q40 46 64 42 Q88 46 86 78Z" fill="#5A5378" {W(3)}/>'
    + f'<path d="M46 46 Q64 22 82 46 Q76 36 64 36 Q52 36 46 46Z" fill="#5A5378" {W(2.6)}/>'
    + f'<circle cx="64" cy="34" r="14" fill="#E9B48C" {W(3)}/>'
    + f'<path d="M50 30 Q64 10 78 30 Q72 22 64 24 Q56 22 50 30Z" fill="#5A5378" {W(2.4)}/>'
    + face(64, 36, d=5, k=0.5)
    + f'<path d="M86 66 L96 92" fill="none" stroke="#5A5378" stroke-width="8" stroke-linecap="round"/>'
    + ball(64, 96, 10, fc=False)
    + f'<path d="M76 96 q8 -6 14 0" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="2 3"/>'
    + f'<path d="M40 112 h14 M76 112 h14" stroke="#fff" stroke-width="7" stroke-linecap="round"/><path d="M40 112 h14 M76 112 h14" {W(1.6)}/>',
    "подросток в сиреневом худи с капюшоном",
    "ведёт баскетбольный мяч между широко расставленных ног на асфальтовой площадке во дворе")

# «Крылья Советов»: голубь-баскетболист на трибуне стадиона подкидывает мяч крыльями
add("krylya-sovetov-basket", "sky",
    f'<path d="M0 98 H128 V128 H0Z" fill="#4FBF6B"/><path d="M0 98 H128" {W(2.4)}/>'
    + "".join(f'<rect x="{x}" y="86" width="10" height="12" fill="#E8554A" {W(1.6)}/>' for x in (4, 18, 100, 114))
    + f'<ellipse cx="60" cy="74" rx="24" ry="20" fill="#A8AFBD" {W(3)}/>'
    + f'<path d="M48 70 Q60 82 74 70" fill="none" stroke="#8C7BD8" stroke-width="5" opacity=".6"/>'
    + f'<circle cx="62" cy="50" r="14" fill="#C9CED8" {W(3)}/>'
    + f'<path d="M74 50 L84 54 L74 56Z" fill="{GOLD}" {W(2)}/>'
    + eye(66, 47, 0.7) + f'<ellipse cx="60" cy="56" rx="3.6" ry="2.2" fill="{PINK}" opacity=".7"/>'
    + f'<path d="M40 70 Q24 48 36 30 Q46 52 50 62Z" fill="#C9CED8" {W(2.6)}/>'
    + f'<path d="M80 70 Q100 50 92 32 Q78 52 72 62Z" fill="#C9CED8" {W(2.6)}/>'
    + ball(64, 20, 12, fc=False)
    + f'<path d="M54 94 v6 M66 94 v6" stroke="#E8554A" stroke-width="3" stroke-linecap="round"/>',
    "сизый голубь-баскетболист",
    "подкидывает мяч двумя крыльями над газоном старого стадиона")

# «Движение вверх»: кабина лифта со стрелкой вверх поднимает мяч к кольцу
add("dvizhenie-vverkh-basket", "orange",
    f'<rect x="38" y="4" width="52" height="124" fill="#FFE7C2" {W(2.6)}/>'
    + f'<path d="M64 4 V30" {W(2.4)}/>'
    + f'<rect x="42" y="30" width="44" height="54" rx="4" fill="#C9CED8" {W(3)}/>'
    + f'<path d="M64 30 V84" {W(2)}/>'
    + f'<path d="M64 38 L72 48 H67 V56 H61 V48 H56Z" fill="#4FBF6B" {W(1.8)}/>'
    + ball(64, 70, 11)
    + hoop(104, 22, w=22, board=False)
    + f'<rect x="96" y="2" width="24" height="18" rx="2" fill="#fff" {W(2.4)}/>'
    + "".join(f'<circle cx="24" cy="{y}" r="5" fill="#fff" {W(2)}/>' for y in (60, 76))
    + f'<path d="M21 61 L24 57 L27 61 M21 75 L24 79 L27 75" fill="none" {W(1.6)}/>',
    "серебристая кабина лифта с зелёной стрелкой «вверх»",
    "поднимает в шахте улыбающийся мяч на верхний этаж, где висит кольцо")

# ============================== ВОЛЕЙБОЛ ==============================
# «Залп», ВДНХ: салют из волейбольных мячей над аркой павильона
add("zalp-volley-vdnkh", "night",
    f'<path d="M20 128 V96 Q64 70 108 96 V128Z" fill="#F3E3C3" {W(3)}/><path d="M40 128 V104 Q64 88 88 104 V128" fill="#8A97E0" {W(2.4)}/>'
    + f'<path d="M64 80 V66" {W(2.4)}/><path d="M58 66 L64 54 L70 66Z" fill="{GOLD}" {W(2)}/>'
    + "".join(f'<path d="M64 46 L{64+30*math.cos(a):.1f} {46+30*math.sin(a):.1f}" stroke="{c}" stroke-width="3" stroke-linecap="round" stroke-dasharray="4 4"/>'
              for a, c in [(-2.6, "#FFD23F"), (-1.9, "#fff"), (-1.2, "#FF7FA8"), (-0.5, "#FFD23F"), (0.3, "#fff"), (2.9, "#FF7FA8")])
    + vball(64, 40, 15)
    + vball(28, 22, 7, fc=False) + vball(100, 20, 8, fc=False) + vball(108, 54, 6, fc=False) + vball(20, 56, 6, fc=False),
    "праздничный салют из волейбольных мячей",
    "взрывается над аркой павильона ВДНХ — в центре залпа большой улыбающийся мяч, вокруг разлетаются маленькие")

# «Зенит-Москва»: девочка подаёт мяч вертикально вверх к солнцу в зените
add("zenit-moskva-volley", "blue",
    f'<circle cx="64" cy="18" r="13" fill="#FFE27A" stroke="#FFC93C" stroke-width="3"/>'
    + "".join(f'<path d="M{64+16*math.cos(a):.1f} {18+16*math.sin(a):.1f} L{64+22*math.cos(a):.1f} {18+22*math.sin(a):.1f}" stroke="#FFE27A" stroke-width="3.4" stroke-linecap="round"/>' for a in [i * math.pi / 5 for i in range(10)])
    + vball(64, 52, 12, fc=False)
    + f'<path d="M64 66 V80" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 4"/>'
    + G(64, 108, kid(shirt="#3E7FD8", hair="#E8A43C", girl=True), sc=0.9)
    + f'<path d="M52 104 L46 84 M76 104 L82 84" fill="none" stroke="#FFD8B8" stroke-width="6" stroke-linecap="round"/>',
    "девочка-волейболистка в синей форме с рыжими хвостиками",
    "подбросила мяч строго вертикально вверх, к солнцу в самой высокой точке неба")

# Globus: школьный глобус с волейбольной раскраской крутится на подставке
add("globus-volley-kuzminki", "green",
    f'<path d="M30 54 A38 38 0 0 0 98 82" fill="none" stroke="#C98A52" stroke-width="6" stroke-linecap="round"/>'
    + f'<path d="M30 54 A38 38 0 0 0 98 82" fill="none" {W(1.6)}/>'
    + f'<path d="M64 92 V108" stroke="#C98A52" stroke-width="7"/><path d="M40 118 Q64 104 88 118Z" fill="#C98A52" {W(3)}/>'
    + vball(64, 54, 30)
    + f'<path d="M14 40 q-4 12 2 22 M114 50 q4 12 -2 22" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    + f'<path d="M12 60 l4 4 l4 -5" fill="none" stroke="#fff" stroke-width="2.4"/>',
    "школьный глобус с волейбольными долями вместо материков",
    "весело вертится на деревянной подставке с дугой-меридианом")

# RusVolley, Павелецкая: матрёшка в наколенниках принимает мяч снизу
add("rusvolley-paveletskaya", "yellow",
    f'<path d="M36 120 Q28 84 44 66 Q36 50 50 38 Q64 28 78 38 Q92 50 84 66 Q100 84 92 120Z" fill="#E8554A" {W(3)}/>'
    + f'<path d="M44 60 Q64 26 84 60 Q78 70 64 70 Q50 70 44 60Z" fill="#FFC93C" {W(2.4)}/>'
    + f'<circle cx="64" cy="52" r="13" fill="#FFE2CC" {W(2.4)}/>'
    + face(64, 52, d=5, k=0.5)
    + f'<path d="M50 74 Q64 94 78 74" fill="#FFF7EC" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#FFC93C" {W(1.6)}/>' for x, y in [(58, 82), (70, 82), (64, 90)])
    + f'<rect x="40" y="104" width="14" height="8" rx="3" fill="#fff" {W(2)}/><rect x="74" y="104" width="14" height="8" rx="3" fill="#fff" {W(2)}/>'
    + f'<path d="M54 96 L64 108 L74 96" fill="none" stroke="#FFE2CC" stroke-width="6" stroke-linecap="round"/>'
    + vball(64, 112, 10, fc=False)
    + f'<path d="M100 40 q10 -10 6 -24" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 4"/>',
    "матрёшка-волейболистка в белых наколенниках",
    "низко присела и принимает мяч снизу сложенными руками")

# «Тактика»: тренерский планшет с площадкой, маркер рисует стрелки комбинации
add("taktika-volley-dvintsev", "teal",
    f'<rect x="18" y="20" width="84" height="94" rx="8" fill="#4A4466" {W(3)}/>'
    + f'<rect x="26" y="30" width="68" height="76" fill="#F28C38" {W(2.4)}/>'
    + f'<path d="M26 68 H94" stroke="#fff" stroke-width="3"/><path d="M26 68 H94" stroke="{O}" stroke-width="1" stroke-dasharray="2 2"/>'
    + f'<path d="M26 54 H94 M26 82 H94" stroke="#fff" stroke-width="1.6"/>'
    + "".join(f'<path d="M{x-4} {y-4} l8 8 m0 -8 l-8 8" stroke="#fff" stroke-width="2.4"/>' for x, y in [(40, 44), (60, 40), (80, 46)])
    + "".join(f'<circle cx="{x}" cy="{y}" r="4.5" fill="none" stroke="#fff" stroke-width="2.4"/>' for x, y in [(40, 92), (60, 96), (80, 90)])
    + f'<path d="M40 88 Q50 72 60 46" fill="none" stroke="#FFE27A" stroke-width="2.6" stroke-dasharray="3 3"/>'
    + vball(60, 60, 8, fc=False)
    + f'<rect x="52" y="14" width="24" height="10" rx="3" fill="#C9CED8" {W(2.4)}/>'
    + G(104, 70, f'<rect x="-5" y="-30" width="10" height="44" rx="3" fill="#E8554A" {W(2.4)}/><path d="M-5 14 L0 24 L5 14Z" fill="#FFE2CC" {W(2)}/>' + face(0, -12, d=2.8, k=0.32, blush=False), rot=28)
    + face(60, 112, d=7, k=0.6),
    "тренерский планшет с оранжевой волейбольной площадкой",
    "красный маркер с глазками рисует на нём пунктирную стрелку атаки между крестиками и ноликами")

# ============================== ГАНДБОЛ ==============================
# СШОР №53: гандбольные ворота в красно-белую полоску с глазками ловят мяч сеткой
add("sshor53-handball-vykhino", "sky",
    f'<path d="M0 100 H128 V128 H0Z" fill="#5CCDBA"/><path d="M0 100 H128" {W(2.4)}/>'
    + f'<path d="M24 100 V44 H104 V100" fill="none" stroke="#fff" stroke-width="10"/>'
    + "".join(f'<path d="M24 {y} V{y+10}" stroke="#E8554A" stroke-width="10"/><path d="M104 {y} V{y+10}" stroke="#E8554A" stroke-width="10"/>' for y in range(44, 100, 20))
    + "".join(f'<path d="M{x} 44 H{x+10}" stroke="#E8554A" stroke-width="10"/>' for x in range(30, 104, 20))
    + f'<path d="M19 100 V39 H109 V100 M29 100 V49 H99 V100" fill="none" {W(2.2)}/>'
    + f'<path d="M29 49 Q64 84 99 49" fill="#fff" fill-opacity=".5" {W(1.4)}/>'
    + "".join(f'<path d="M{x} 49 Q{x+3} 64 {64+(x-64)*0.4:.0f} 70" fill="none" stroke="{O}" stroke-width="1" opacity=".5"/>' for x in range(36, 99, 9))
    + face(64, 30, d=10, k=0.8)
    + f'<circle cx="64" cy="70" r="11" fill="#2F7DE0" {W(2.6)}/><path d="M56 64 Q64 70 72 64 M58 78 Q64 72 70 78" fill="none" stroke="#FFD23F" stroke-width="2.6"/>',
    "гандбольные ворота в красно-белую полоску с глазками на перекладине",
    "поймали сине-жёлтый мячик в сетку, как сачком, и довольно улыбаются")

# «Юность Москвы» — «Кунцево»: мальчик-гандболист в прыжке бросает мяч над вратарём
add("yunost-kuntsevo-handball", "orange",
    f'<path d="M0 110 H128" stroke="#fff" stroke-width="3"/><path d="M8 110 Q64 70 120 110" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="5 4"/>'
    + G(46, 74, kid(shirt="#2F7DE0", hair="#3B2A1E"), rot=-12)
    + f'<path d="M40 100 L28 116 M54 100 L62 118" stroke="#2C3E66" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M58 66 L76 40" fill="none" stroke="#FFD8B8" stroke-width="7" stroke-linecap="round"/>'
    + f'<circle cx="80" cy="34" r="10" fill="#FFD23F" {W(2.6)}/><path d="M72 30 Q80 36 88 30 M74 40 Q80 34 86 40" fill="none" stroke="#2F7DE0" stroke-width="2.4"/>'
    + f'<path d="M92 26 h12 M94 34 h14" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'
    + f'<path d="M30 76 L18 62" fill="none" stroke="#FFD8B8" stroke-width="6" stroke-linecap="round"/>',
    "мальчик-гандболист в синей майке",
    "в высоком прыжке над пунктирной линией шестиметровой зоны замахивается и бросает жёлтый мяч")

# ============================== БАДМИНТОН ==============================
# СК Тимирязевской академии: подсолнух-бадминтонист отбивает волан листом-ракеткой на опытном поле
add("timiryazevka-sk-badminton", "sky",
    f'<path d="M0 108 Q64 98 128 108 V128 H0Z" fill="#8A6A55"/>'
    + "".join(f'<path d="M{x} 108 q2 -8 6 -10" fill="none" stroke="#4FBF6B" stroke-width="3" stroke-linecap="round"/>' for x in range(6, 128, 14))
    + f'<path d="M56 116 Q58 84 56 66" fill="none" stroke="#4E9A44" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M57 92 Q36 92 30 80 Q44 74 57 88Z" fill="#7CD26E" {W(2.4)}/>'
    + "".join(f'<ellipse cx="{56+24*math.cos(a):.1f}" cy="{50+24*math.sin(a):.1f}" rx="10" ry="5" transform="rotate({math.degrees(a):.0f} {56+24*math.cos(a):.1f} {50+24*math.sin(a):.1f})" fill="#FFC93C" {W(2)}/>' for a in [i * math.pi / 6 for i in range(12)])
    + f'<circle cx="56" cy="50" r="17" fill="#8A5A3C" {W(3)}/>' + face(56, 50, d=6, k=0.58)
    + G(84, 78, racket(c="#4FBF6B", grip="#4E9A44"), rot=40, sc=0.5)
    + G(104, 34, shuttle(fc=False), rot=-140, sc=0.32),
    "подсолнух-бадминтонист с ракеткой вместо листа",
    "отбивает волан высоко в небо над вспаханной грядкой опытного поля")

# Конноспортивная база ЦСКА: рыжий пони подбрасывает волан носом, в зубах ракетка
add("cska-horse-base-badminton", "pink",
    f'<path d="M0 104 H128 V128 H0Z" fill="#E0B07A"/><path d="M0 104 H128" {W(2.4)}/>'
    + f'<path d="M8 104 V70 H30 V104 M8 80 H30 M8 92 H30" fill="none" stroke="#fff" stroke-width="4"/>'
    + f'<ellipse cx="70" cy="90" rx="30" ry="16" fill="#E8955A" {W(3)}/>'
    + f'<path d="M48 100 V118 M58 102 V120 M82 102 V120 M92 100 V118" stroke="#E8955A" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M48 100 V118 M58 102 V120 M82 102 V120 M92 100 V118" {W(1.4)}/>'
    + f'<path d="M100 84 Q116 86 112 106" fill="none" stroke="#8A4A2E" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M50 84 Q42 60 46 44 L60 40 Q66 60 66 80Z" fill="#E8955A" {W(3)}/>'
    + f'<ellipse cx="44" cy="44" rx="16" ry="11" transform="rotate(-20 44 44)" fill="#E8955A" {W(3)}/>'
    + f'<path d="M50 34 L54 24 L58 36" fill="#E8955A" {W(2.4)}/>'
    + f'<path d="M56 38 Q66 50 64 70" fill="none" stroke="#8A4A2E" stroke-width="6" stroke-linecap="round"/>'
    + eye(48, 40, 0.7) + f'<circle cx="34" cy="48" r="1.6" fill="{O}"/>'
    + f'<ellipse cx="44" cy="50" rx="3.6" ry="2" fill="{PINK}" opacity=".7"/>'
    + G(30, 22, shuttle(fc=False), rot=200, sc=0.3)
    + G(80, 66, racket(c="#E8554A"), rot=70, sc=0.42),
    "рыжий пони с тёмной гривой",
    "на манеже конной базы подбивает волан носом, а бадминтонная ракетка лежит у него на спине")

# ============================== ШАХМАТЫ ==============================
# «Гранит»: ладья наполовину высечена из гранитной скалы, рядом резец и молоток
add("granit-chess-makarenko", "orange",
    f'<path d="M6 128 L14 84 L30 70 L50 74 L78 66 L104 76 L120 92 L124 128Z" fill="#9AA3B5" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1.6" fill="#6B7280"/>' for x, y in [(24, 100), (36, 116), (96, 104), (110, 118), (86, 120), (20, 118)])
    + G(64, 50, rook(c="#B8C0CC", c2="#9AA3B5", fy=10), sc=0.82)
    + f'<path d="M98 50 L112 28" stroke="#C9CED8" stroke-width="5" stroke-linecap="round"/><path d="M98 50 L112 28" {W(1.4)}/>'
    + f'<rect x="102" y="12" width="20" height="12" rx="3" transform="rotate(30 112 18)" fill="#8A5A3C" {W(2.4)}/>'
    + sparkle(92, 58, 4) + sparkle(86, 46, 3),
    "серая гранитная ладья",
    "наполовину высечена из скалы, стоит по пояс в камне, а рядом стучит резец скульптора")

# «Алисиум»: белый кролик с карманными часами спешит по доске Зазеркалья
add("alisium-chess", "purple",
    checks(-4, 92, 9, 3, 16, a="#FFF7EC", b="#E8554A")
    + f'<ellipse cx="60" cy="72" rx="18" ry="22" fill="#fff" {W(3)}/>'
    + f'<path d="M44 62 Q60 54 76 62 L74 84 Q60 90 46 84Z" fill="#E8554A" {W(2.4)}/>'
    + f'<circle cx="60" cy="42" r="15" fill="#fff" {W(3)}/>'
    + f'<path d="M52 30 Q46 6 54 4 Q60 8 58 30Z M66 30 Q70 4 78 6 Q80 14 68 32Z" fill="#fff" {W(2.6)}/>'
    + f'<path d="M54 26 Q52 12 55 8 M68 28 Q72 14 75 10" stroke="{PINK}" stroke-width="3" fill="none"/>'
    + face(60, 44, d=5, k=0.5)
    + f'<circle cx="90" cy="60" r="11" fill="{GOLD}" {W(2.6)}/><circle cx="90" cy="60" r="7" fill="#fff" {W(1.6)}/>'
    + f'<path d="M90 60 V55 M90 60 L93 62" {W(1.6)}/><path d="M78 66 Q80 62 82 62" fill="none" {W(1.6)}/>'
    + f'<path d="M50 94 L44 106 M70 94 L76 106" stroke="#fff" stroke-width="7" stroke-linecap="round"/><path d="M50 94 L44 106 M70 94 L76 106" {W(1.4)}/>',
    "белый кролик в красной жилетке с золотыми карманными часами",
    "спешит по красно-белой шахматной доске Зазеркалья, глядя на циферблат")

# «Этюд»: мольберт с холстом-доской, кисть дорисовывает ферзя
add("etyud-chess-otradnoe", "green",
    f'<path d="M36 124 L54 30 M92 124 L74 30 M64 30 V124" stroke="#C98A52" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M36 124 L54 30 M92 124 L74 30" fill="none" {W(1.4)}/>'
    + f'<rect x="24" y="22" width="80" height="62" rx="3" fill="#fff" {W(3)}/>'
    + checks(30, 28, 6, 4, 11.4, a="#FFF7EC", b="#B9E6A8", w=1)
    + G(64, 56, queen(c="#fff", c2="#E6E6F0", fc=False), sc=0.42)
    + f'<rect x="26" y="84" width="76" height="6" rx="2" fill="#C98A52" {W(2.4)}/>'
    + G(98, 46, f'<rect x="-3" y="-34" width="6" height="34" rx="2" fill="#E8554A" {W(2)}/><rect x="-4" y="0" width="8" height="6" fill="#C9CED8" {W(1.8)}/><path d="M-4 6 Q0 18 4 6Z" fill="#3E7FD8" {W(1.8)}/>', rot=-35)
    + face(64, 104, d=8, k=0.6),
    "деревянный мольберт с глазками",
    "держит холст, на котором кисть дорисовывает белого ферзя на клетчатой доске")

# «Подкова»: красно-синяя подкова-магнит притягивает пешку и коня
add("podkova-chess-kurkino", "yellow",
    f'<path d="M30 20 V58 A34 34 0 0 0 98 58 V20 H80 V58 A16 16 0 0 1 48 58 V20Z" fill="#E8554A" {W(3)}/>'
    + f'<rect x="30" y="14" width="18" height="14" fill="#C9CED8" {W(2.6)}/><rect x="80" y="14" width="18" height="14" fill="#C9CED8" {W(2.6)}/>'
    + f'<path d="M64 92 V76" stroke="#fff" stroke-width="0"/>'
    + face(64, 80, d=9, k=0.7)
    + f'<path d="M22 10 l-6 -6 M106 10 l6 -6 M18 22 h-8 M110 22 h8" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>'
    + G(34, 104, pawn(c="#3B3355", c2="#5A5378", fc=False), sc=0.32)
    + G(94, 102, knight(c="#fff"), sc=0.34)
    + f'<path d="M40 88 q2 -4 6 -2 M88 86 q-2 -4 -6 -2" fill="none" stroke="#fff" stroke-width="2.4"/>',
    "красная подкова-магнит с серебристыми полюсами",
    "довольно притягивает к себе чёрную пешку и белого коня, а вокруг искрит магнитное поле")

# «Ферзьбери»: ферзь-леди в английской шляпке пьёт чай
add("ferzbury-chess-strogino", "sky",
    G(56, 70, queen(c="#fff", c2="#DCE3F0", fc=False), sc=0.9)
    + f'<ellipse cx="56" cy="30" rx="30" ry="6" fill="#8C7BD8" {W(2.6)}/>'
    + f'<path d="M40 30 Q42 14 56 14 Q70 14 72 30Z" fill="#8C7BD8" {W(2.6)}/><path d="M42 26 H70" stroke="{PINK}" stroke-width="4"/>'
    + f'<circle cx="74" cy="22" r="5" fill="{PINK}" {W(2)}/>'
    + face(56, 74, d=6, k=0.58)
    + f'<path d="M84 92 H104 L102 104 Q94 110 86 104Z" fill="#fff" {W(2.6)}/><path d="M104 96 q8 0 6 6 q-2 4 -6 2" fill="none" {W(2.2)}/>'
    + f'<ellipse cx="94" cy="108" rx="16" ry="4" fill="#fff" {W(2.2)}/>'
    + f'<path d="M90 86 q-4 -6 0 -10 M98 86 q-4 -6 0 -10" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'
    + f'<path d="M72 84 L84 96" stroke="#fff" stroke-width="6" stroke-linecap="round"/><path d="M72 84 L84 96" {W(1.4)}/>',
    "белый ферзь-леди в сиреневой английской шляпке",
    "чинно пьёт горячий чай из фарфоровой чашки с блюдцем, оттопырив мизинчик")

# «Королевская пешка»: пешка дошла до последней горизонтали и примеряет корону у зеркала
add("korolevskaya-peshka-chess", "pink",
    f'<ellipse cx="96" cy="64" rx="22" ry="34" fill="#DFF4FF" stroke="{GOLD}" stroke-width="6"/><ellipse cx="96" cy="64" rx="25" ry="37" fill="none" {W(2.4)}/>'
    + f'<path d="M84 44 L100 36 M86 54 L104 44" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    + G(96, 74, pawn(c="#F4EEE4", fc=False), sc=0.42)
    + G(46, 76, pawn(c="#F4EEE4"), sc=0.9)
    + f'<path d="M30 46 L34 30 L42 40 L46 26 L50 40 L58 30 L62 46Z" fill="{GOLD}" {W(2.6)}/>'
    + f'<circle cx="46" cy="38" r="2.6" fill="#E8554A"/>'
    + f'<path d="M8 122 H120" stroke="#fff" stroke-width="2"/>' + sparkle(20, 24, 4) + sparkle(70, 18, 3),
    "светлая пешка, дошедшая до края доски",
    "впервые надевает золотую корону и любуется собой в зеркале в золотой раме")

# aChess, Шаболовка: Шуховская башня из шахматных клеток, на макушке — конь
add("achess-shabolovka", "blue",
    "".join(f'<path d="M{64-w} {y} H{64+w}" {W(2)}/>' for y, w in [(118, 38), (96, 30), (76, 24), (58, 19), (42, 15)])
    + "".join(f'<path d="M{64-a} {y1} L{64+b} {y2} M{64+a} {y1} L{64-b} {y2}" stroke="{c}" stroke-width="3"/>'
              for y1, y2, a, b, c in [(118, 96, 38, 30, "#3B3355"), (96, 76, 30, 24, "#E8554A"), (76, 58, 24, 19, "#3B3355"), (58, 42, 19, 15, "#E8554A")])
    + f'<path d="M26 118 L34 96 L40 76 L45 58 L49 42 M102 118 L94 96 L88 76 L83 58 L79 42" fill="none" {W(2.6)}/>'
    + G(64, 22, knight(c="#fff"), sc=0.48)
    + f'<path d="M14 40 q6 -4 12 0 M102 30 q6 -4 12 0" fill="none" stroke="#fff" stroke-width="2.4"/>',
    "Шуховская радиобашня в красно-тёмную шахматную решётку",
    "держит на самой макушке белого шахматного коня, как антенну")

# «Феномен», Медведково: слон-фокусник вытаскивает из цилиндра ладью
add("fenomen-chess-chelyuskinskaya", "night",
    f'<path d="M30 92 H74 L70 120 H34Z" fill="#2C2742" {W(3)}/><ellipse cx="52" cy="92" rx="26" ry="6" fill="#3B3355" {W(2.6)}/>'
    + f'<path d="M30 110 H74" stroke="#E8554A" stroke-width="5"/>'
    + G(52, 74, rook(c="#fff", fc=True, fy=10), sc=0.36)
    + sparkle(36, 54, 4, "#FFE27A") + sparkle(70, 50, 5, "#FFE27A") + sparkle(52, 40, 3)
    + G(94, 70, f'<rect x="-20" y="34" width="40" height="10" rx="3" fill="#fff" {W(3)}/>'
        f'<path d="M-15 36 Q-12 6 -6 -6 H6 Q12 6 15 36Z" fill="#fff" {W(3)}/>'
        f'<ellipse cx="0" cy="-22" rx="12" ry="17" fill="#fff" {W(3)}/><path d="M-3 -38 L6 -26" {W(2.6)}/>'
        + face(0, -18, d=4.5, k=0.45), sc=0.95)
    + f'<path d="M78 72 L66 84" stroke="#3B3355" stroke-width="4" stroke-linecap="round"/><path d="M66 84 l-3 3" stroke="#fff" stroke-width="4"/>',
    "белый шахматный слон-фокусник с волшебной палочкой",
    "вытаскивает из чёрного цилиндра изумлённую ладью под золотые искры")

# «Феномен», Аргуновская: Останкинская телебашня транслирует партию на экран телевизора
add("fenomen-chess-argunovskaya", "teal",
    f'<path d="M30 120 L34 96 L38 120Z M30 120 L36 100 L42 120" fill="#E7EAF0" {W(2.2)}/>'
    + f'<path d="M34 98 L36 10 L38 98Z" fill="#E7EAF0" {W(2.4)}/><rect x="31" y="44" width="10" height="7" rx="2" fill="#C9CED8" {W(2)}/>'
    + f'<path d="M36 10 V2" {W(2)}/>'
    + "".join(f'<path d="M{44+i*6} {40-i*2} q6 6 0 12" fill="none" stroke="#fff" stroke-width="2.4"/>' for i in range(3))
    + f'<rect x="58" y="54" width="60" height="46" rx="8" fill="#8A6A55" {W(3)}/>'
    + checks(64, 60, 6, 4, 8, a="#FFF7EC", b="#5CCDBA")
    + G(84, 76, knight(c="#3B3355", c2="#5A5378", ew="#fff"), sc=0.22)
    + f'<path d="M72 100 L66 112 M104 100 L110 112" {W(2.6)}/>'
    + f'<path d="M80 54 L72 42 M96 54 L104 42" {W(2.4)}/>'
    + face(88, 106, d=6, k=0.5, mouth=False),
    "серебристая Останкинская телебашня",
    "посылает радиоволны в пузатый ламповый телевизор, где показывают партию с чёрным конём")

# «Феномен», Лётчика Бабушкина: биплан с клетчатыми крыльями везёт пешку-пассажира
add("fenomen-chess-babushkina", "yellow",
    cloud(24, 100, 0.8) + cloud(106, 108, 0.6)
    + checks(26, 40, 8, 1, 9.5, a="#fff", b="#3B3355") + checks(26, 76, 8, 1, 9.5, a="#fff", b="#3B3355")
    + f'<path d="M40 50 V76 M88 50 V76" {W(2.4)}/>'
    + f'<path d="M14 64 Q60 54 104 60 L116 48 L120 70 Q60 78 14 70Z" fill="#E8554A" {W(3)}/>'
    + f'<ellipse cx="10" cy="67" rx="3.6" ry="14" fill="#C9CED8" {W(2)}/>'
    + G(64, 38, pawn(c="#FFF7EC", fc=True), sc=0.46)
    + f'<path d="M56 50 Q64 44 72 50" fill="none" stroke="#8A5A3C" stroke-width="3"/>'
    + face(28, 66, d=4, k=0.4, mouth=False),
    "красный биплан с крыльями в чёрно-белую клетку",
    "везёт в открытой кабине пешку-пассажира в лётных очках над облаками")

# Шахматная школа №1, Сущёвский Вал (Марьина Роща): белочка на пне-доске двигает пешку-жёлудь
add("chess1-sushchevsky-val", "green",
    "".join(f'<path d="M{x} 128 V60" stroke="#8A6A55" stroke-width="5"/><circle cx="{x}" cy="{y}" r="{r}" fill="#4FBF6B" {W(2.4)}/>' for x, y, r in [(12, 48, 18), (116, 40, 20)])
    + f'<path d="M30 128 V100 H98 V128" fill="#C98A52" {W(3)}/>'
    + f'<ellipse cx="64" cy="100" rx="34" ry="9" fill="#E0B07A" {W(3)}/>'
    + "".join(f'<rect x="{38+i*10}" y="{96+(i%2)*4}" width="10" height="4" fill="#8A5A3C" opacity=".7"/>' for i in range(5))
    + f'<path d="M86 90 Q112 84 106 58 Q100 40 88 50 Q98 62 84 78Z" fill="#E8955A" {W(2.6)}/>'
    + f'<ellipse cx="68" cy="80" rx="13" ry="14" fill="#E8955A" {W(3)}/>'
    + f'<circle cx="64" cy="60" r="12" fill="#E8955A" {W(3)}/><path d="M56 50 L54 40 L62 48 M70 48 L74 40 L74 50" fill="#E8955A" {W(2.2)}/>'
    + face(64, 61, d=4.5, k=0.45)
    + f'<ellipse cx="44" cy="90" rx="6" ry="7" fill="#C98A52" {W(2.4)}/><path d="M38 86 Q44 78 50 86Z" fill="#8A5A3C" {W(2.2)}/>'
    + f'<path d="M56 78 L48 86" stroke="#E8955A" stroke-width="5" stroke-linecap="round"/>',
    "рыжая белочка-шахматистка",
    "в роще на пне с клетками передвигает лапкой пешку-жёлудь")

# Шахматная школа №1, Дубнинская: часы с кукушкой, из дверцы выскакивает конь
add("chess1-dubninskaya", "purple",
    f'<path d="M24 50 L64 18 L104 50Z" fill="#8A5A3C" {W(3)}/>'
    + f'<rect x="32" y="48" width="64" height="58" fill="#C98A52" {W(3)}/>'
    + f'<circle cx="64" cy="84" r="16" fill="#FFF7EC" {W(2.6)}/><path d="M64 84 V74 M64 84 L72 88" {W(2.4)}/>'
    + f'<rect x="54" y="52" width="20" height="16" fill="#3B3355" {W(2.2)}/><path d="M74 52 L84 46 V62 L74 68" fill="#E0B07A" {W(2)}/>'
    + G(62, 46, knight(c="#fff"), sc=0.3)
    + f'<path d="M50 106 V118 M78 106 V112" {W(2.2)}/>'
    + f'<path d="M44 118 L50 126 L56 118Z" fill="{GOLD}" {W(2)}/><path d="M72 112 L78 120 L84 112Z" fill="{GOLD}" {W(2)}/>'
    + f'<path d="M94 30 q6 -4 10 2 M98 22 q8 -6 14 2" fill="none" stroke="#fff" stroke-width="2.4"/>',
    "резные часы с кукушкой",
    "вместо кукушки из дверцы выскакивает белый шахматный конь и объявляет время партии")

# Шахматная школа №1, Братиславская: лодка-ладья (пун) с парусом-доской плывёт по реке
add("chess1-bratislavskaya", "sky",
    f'<path d="M0 96 Q16 90 32 96 T64 96 T96 96 T128 96 V128 H0Z" fill="#5CB7F2" {W(2.4)}/>'
    + f'<path d="M10 112 q8 -4 16 0 M80 116 q8 -4 16 0" fill="none" stroke="#fff" stroke-width="2.4"/>'
    + f'<path d="M24 84 H104 L94 100 H34Z" fill="#8A5A3C" {W(3)}/>'
    + f'<path d="M24 84 V74 H32 V80 H40 V74 H48 V84" fill="#8A5A3C" {W(2.4)}/>'
    + f'<path d="M64 84 V18" {W(3)}/>'
    + f'<path d="M66 20 L100 70 H66Z" fill="#fff" {W(2.6)}/>'
    + "".join(f'<rect x="{66+i*8}" y="{30+j*10}" width="8" height="10" fill="#3B3355" opacity=".85"/>' for i in range(4) for j in range(4) if (i + j) % 2 and 66 + i * 8 < 66 + (30 + j * 10 - 20) * 0.68)
    + f'<path d="M66 20 L100 70 H66Z" fill="none" {W(2.6)}/>'
    + face(74, 92, d=7, k=0.55)
    + f'<path d="M62 22 L44 30 L62 36Z" fill="#E8554A" {W(2)}/>',
    "деревянная лодка-ладья с зубчатой кормой",
    "плывёт по реке под треугольным парусом в шахматную клетку")

# Шахматная школа №1, Кастанаевская (Пионерская): пионерский горн с клетчатым флажком
add("chess1-kastanaevskaya", "orange",
    G(64, 64, f'<path d="M-42 -6 L18 -10 L46 -30 V30 L18 10 L-42 6Z" fill="{GOLD}" {W(3)}/>'
        f'<ellipse cx="46" cy="0" rx="8" ry="30" fill="#FFE27A" {W(3)}/>'
        f'<rect x="-50" y="-8" width="10" height="16" rx="3" fill="#C9A13C" {W(2.4)}/>'
        + face(-6, 0, d=6, k=0.55), rot=-20)
    + f'<path d="M36 82 L40 116" {W(2.4)}/>'
    + checks(40, 90, 4, 3, 7, a="#fff", b="#3B3355")
    + "".join(f'<path d="M{x} {y} q6 -2 8 4" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>' for x, y in [(100, 22), (108, 34), (94, 12)]),
    "блестящий пионерский горн с клетчатым флажком",
    "трубит сбор на шахматный турнир, и из раструба летят звонкие ноты-дуги")

# Шахматная школа №1, «Мореон»: морской конёк-шахматист над клетчатым дном
add("chess1-moreon-golubinskaya", "blue",
    checks(-4, 104, 9, 2, 16, a="#FFF2C9", b="#5CB7F2")
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" fill-opacity=".5" {W(1.6)}/>' for x, y, r in [(96, 20, 5), (104, 34, 3), (90, 40, 4)])
    + f'<path d="M30 104 Q24 86 34 80 Q20 70 28 60" fill="none" stroke="#4FBF6B" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M58 30 Q76 22 82 36 Q86 46 76 50 Q90 60 84 78 Q78 96 62 98 Q52 100 54 110 Q62 116 68 110" fill="none" stroke="#FFC93C" stroke-width="18" stroke-linecap="round" stroke-linejoin="round"/>'
    + f'<path d="M58 30 Q76 22 82 36 Q86 46 76 50 Q90 60 84 78 Q78 96 62 98 Q52 100 54 110 Q62 116 68 110" fill="none" {W(2)}/>'
    + f'<path d="M58 28 L38 30 L40 40 L58 36Z" fill="#FFC93C" {W(2.4)}/>'
    + f'<path d="M60 24 L56 14 L66 20" fill="#FFC93C" {W(2)}/>'
    + eye(68, 32, 0.7) + f'<ellipse cx="66" cy="40" rx="3.4" ry="2" fill="{PINK}" opacity=".7"/>'
    + G(100, 88, knight(c="#fff"), sc=0.3),
    "жёлтый морской конёк",
    "на клетчатом песчаном дне аквапарка разглядывает белого шахматного коня — родственника по профилю")

# ============================== ФЕХТОВАНИЕ ==============================
# «Сталь»: девочка-фехтовальщица без маски салютует шпагой перед боем
add("stal-fencing-khoroshevsky", "teal",
    f'<path d="M0 112 H128" stroke="#fff" stroke-width="10"/><path d="M0 107 H128 M0 117 H128" stroke="{O}" stroke-width="1.4"/>'
    + G(54, 84, kid(shirt="#fff", hair="#3B2A1E", girl=True))
    + f'<path d="M38 112 V100 M70 112 V100" stroke="#fff" stroke-width="8" stroke-linecap="round"/><path d="M38 112 V100 M70 112 V100" {W(1.2)}/>'
    + f'<path d="M66 82 L78 66" stroke="#FFD8B8" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M80 64 L84 10" stroke="#C9CED8" stroke-width="3.2" stroke-linecap="round"/><path d="M80 64 L84 10" {W(1)}/>'
    + f'<ellipse cx="80" cy="64" rx="9" ry="3.6" fill="#C9CED8" {W(2.2)}/>'
    + G(26, 104, f'<path d="M-12 -6 Q-12 -22 0 -22 Q12 -22 12 -6 V6 H-12Z" fill="#3B3355" stroke="#C9CED8" stroke-width="2"/>'
        + "".join(f'<path d="M{x} -18 V4" stroke="#8A97E0" stroke-width="1"/>' for x in range(-8, 10, 4)))
    + sparkle(96, 20, 5) + sparkle(100, 40, 3),
    "девочка-фехтовальщица в белом костюме с тёмной косичкой",
    "сняла маску, поставила её на дорожку и салютует шпагой клинком вверх перед боем")

# ФФМ, Баррикадная: малыш с деревянным мечом штурмует баррикаду из подушек
add("fmech-barrikadnaya", "pink",
    f'<rect x="56" y="88" width="62" height="22" rx="10" fill="#8C7BD8" {W(3)}/><rect x="64" y="66" width="46" height="24" rx="10" fill="#FFC93C" {W(3)}/>'
    + f'<rect x="72" y="44" width="34" height="22" rx="10" fill="#5CCDBA" {W(3)}/>'
    + f'<path d="M89 44 V24" {W(2.4)}/><path d="M89 24 L104 30 L89 36Z" fill="#E8554A" {W(2)}/>'
    + G(36, 86, kid(shirt="#3E7FD8", hair="#E8A43C"))
    + f'<path d="M22 72 Q14 52 26 46" fill="none" stroke="#E8554A" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M48 86 L58 66" stroke="#FFD8B8" stroke-width="7" stroke-linecap="round"/>'
    + G(60, 62, sword(L=40, blade="#E0B07A", guard="#8A5A3C", grip="#8A5A3C", w=5), rot=40)
    + f'<path d="M24 116 V128 M46 116 V128" {W(6)}/>',
    "рыжий малыш в синей футболке с деревянным мечом и красным плащом",
    "штурмует баррикаду из разноцветных диванных подушек с флажком на вершине")

# ФФМ, Тропарёво: ёжик с мечом-иголкой и щитом-листиком на лесной тропинке
add("fmech-troparevo", "green",
    f'<path d="M30 128 Q50 100 64 98 Q82 96 100 128Z" fill="#E0B07A"/>'
    + "".join(f'<path d="M{x} 128 V80" stroke="#8A6A55" stroke-width="6"/><circle cx="{x}" cy="{y}" r="16" fill="#2E8B57" {W(2.4)}/>' for x, y in [(10, 70), (118, 64)])
    + f'<path d="M30 96 Q28 62 58 56 Q86 54 92 82 Q94 98 80 100 H40Z" fill="#8A6A55" {W(3)}/>'
    + "".join(f'<path d="M{40+i*9} {66-(i%2)*4} l-4 -10 l8 6" fill="#6B4E3A" {W(1.8)}/>' for i in range(5))
    + f'<path d="M78 76 Q96 74 100 88 Q92 96 80 94Z" fill="#E9C9A6" {W(2.6)}/><circle cx="101" cy="88" r="2.6" fill="{O}"/>'
    + eye(86, 82, 0.6) + f'<ellipse cx="84" cy="90" rx="3" ry="1.8" fill="{PINK}" opacity=".7"/>'
    + G(98, 64, sword(L=44, blade="#DDE3EC", w=4), rot=20)
    + f'<ellipse cx="46" cy="88" rx="12" ry="15" fill="#7CD26E" {W(2.6)}/><path d="M46 74 V102 M46 84 l-6 -4 M46 92 l6 -4" fill="none" {W(1.6)}/>',
    "ёжик-рыцарь с мечом и щитом-листиком",
    "стоит на страже на лесной тропинке, подняв меч и прикрывшись зелёным листом")
if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for pid, code in ICONS.items():
        open(os.path.join(OUT, pid + ".svg"), "w").write(code)
    reg = os.path.join(OUT, "subjects.txt")
    lines = [l for l in open(reg, encoding="utf-8") if l.split(" — ", 1)[0] not in SUBJ]
    lines += [line + "\n" for line in SUBJ.values()]
    open(reg, "w", encoding="utf-8").writelines(lines)
    print(len(ICONS), "иконок:", " ".join(ICONS))
