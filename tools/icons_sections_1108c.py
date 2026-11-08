"""Иконки робота sections, 2026-11-08 (06 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно —
свой герой, своя сцена, своя палитра фона. Сверено со всеми листами icons-catalog/sheet-01…36 и icons-src/subjects.txt.
Бадминтон: волан-салют в ночном небе, лягушонок с ракеткой на кувшинке, волан на чертеже с циркулем.
Шахматы: слон-космонавт на Луне, король в шезлонге, ферзь за партой тянет руку, конь в кресле с книгой, ладья с кубком,
король-жонглёр (шашка, камень го, пешка), пешка-судья в полосатой рубашке, бородатый гроссмейстер на сеансе,
пешка-первоклассница с ранцем и букетом, конь выпрыгивает из ноутбука, рукопожатие белой и чёрной пешки,
волейбольный мяч в короне на шахматной доске.
Мячи: мальчик-спартанец бросает в кольцо, большой и маленький мяч за руку, мяч на парашюте, малыш на табуретке у низкого
кольца, улитка с мячом-раковиной, мяч на ходулях, мяч-фокусник с цилиндром, кожаный ретро-мяч даёт пять новому,
прыжок над облаками («Взлёт»), волейбольный мяч ведёт мячики-утят, три мяча в обнимку, девушка-подающая в лучах
прожекторов, подросток крутит мяч на пальце, девочка ведёт мяч между конусами.
Настольный теннис: рука подбрасывает мяч на подаче, мячик в солнечных очках загорает на столе, мячик скачет дугами,
мальчик в очках делает топспин, ракетка-паровоз с вагончиками-мячиками. Фехтование: выпад саблей со следом-молнией.
Запуск: python3 tools/icons_sections_1108c.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O
from icons_sections_1107h import G, king, queen, rook, bishop, knight, pawn, checks, WHITE, BLACK
from icons_sections_1107c import ball, hoop, shuttle, racket
from icons_sections_1108b import limb, head, ttball, paddle, soccer, volley

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
PINK, GOLD, RED, ORG, SKIN = "#FF7FA8", "#FFC93C", "#E8554A", "#F28C38", "#FFD8B8"
draw_icons.BG.update({
    "c_salute": ("#5B4BA8", "#231C4E"), "c_lily": ("#E8FFF0", "#3FAE8C"), "c_blueprint": ("#E7F1FF", "#3D6FD1"),
    "c_moon": ("#6F7BD6", "#2A3170"), "c_beach": ("#FFF8DC", "#F2B35E"), "c_class": ("#F2FFEA", "#88C86A"),
    "c_den": ("#FFF0E6", "#C9825A"), "c_podium": ("#FFFBE0", "#E7B932"), "c_juggle": ("#FDEBFF", "#C26BD6"),
    "c_ref": ("#EAFCFF", "#58B9D1"), "c_simul": ("#F5EEE6", "#A58A6C"), "c_school": ("#FFF1F1", "#EE8A8A"),
    "c_laptop": ("#E9FFFB", "#3BBFA8"), "c_hands": ("#F1EEFF", "#7E6FD6"), "c_throne": ("#FFF5E9", "#E0894A"),
    "c_sparta": ("#FFF0E0", "#C85A3A"), "c_family": ("#FFF7EC", "#F0A35A"), "c_chute": ("#E8F7FF", "#6EB6F0"),
    "c_stool": ("#FFF2FA", "#E58BC0"), "c_snail": ("#F4FFE4", "#9CCB4A"), "c_stilts": ("#FFFDE6", "#D9C140"),
    "c_magic": ("#2E2A5E", "#191538"), "c_retro": ("#F7EEDD", "#B98A55"), "c_clouds": ("#DFF3FF", "#4E9BE8"),
    "c_ducks": ("#E6FFF7", "#2DB39A"), "c_trio": ("#EEF7FF", "#7FA6E0"), "c_arena": ("#40306E", "#1B1236"),
    "c_teen": ("#F0FFE9", "#5BBF6E"), "c_cones": ("#FFF4F0", "#F07C5A"), "c_serve": ("#FFEFF4", "#E05A87"),
    "c_sun": ("#FFFBD6", "#F6C83D"), "c_bounce": ("#E8F3FF", "#5A8FD6"), "c_spin": ("#F4F0FF", "#9070D8"),
    "c_train": ("#EFFAF0", "#6FB57A"), "c_flash": ("#FFFDE8", "#E0B021"),
})


def add(pid, bg, body, hero, scene):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def star(x, y, r, c=GOLD, sw=2.2):
    pts = " ".join(f"{x + (r if i % 2 == 0 else r*0.45)*math.cos(math.radians(-90+36*i)):.1f},"
                   f"{y + (r if i % 2 == 0 else r*0.45)*math.sin(math.radians(-90+36*i)):.1f}" for i in range(10))
    return f'<polygon points="{pts}" fill="{c}" {W(sw)}/>'


def table(x, y, w, h=10, c="#2F8F5B", legs=True):
    out = f'<rect x="{x-w/2}" y="{y}" width="{w}" height="{h}" rx="2" fill="{c}" {W(2.8)}/>'
    out += f'<path d="M{x} {y} V{y+h}" stroke="#FFFFFF" stroke-width="2"/>'
    if legs:
        out += f'<path d="M{x-w/2+8} {y+h} V{y+h+22} M{x+w/2-8} {y+h} V{y+h+22}" fill="none" {W(4)}/>'
    return out


# ============================== БАДМИНТОН ==============================
# 1. «Салют»: волан взлетает в ночное небо и рассыпается салютом
_burst = "".join(f'<path d="M{64+18*math.cos(math.radians(a)):.1f} {36+18*math.sin(math.radians(a)):.1f} '
                 f'L{64+30*math.cos(math.radians(a)):.1f} {36+30*math.sin(math.radians(a)):.1f}" stroke="{c}" stroke-width="4" stroke-linecap="round"/>'
                 for a, c in zip(range(0, 360, 30), ["#FFD23F", "#FF6FA8", "#7FE3FF", "#B7FF6A"] * 3))
add("badm-khimki-salyut", "c_salute",
    _burst
    + G(64, 72, shuttle(sc=0.82, feather="#FFFFFF", band="#FF6FA8"), rot=0)
    + f'<path d="M58 106 Q64 118 62 130 M70 106 Q66 118 70 130" fill="none" stroke="#FFD23F" stroke-width="3" stroke-dasharray="4 5" stroke-linecap="round"/>'
    + sparkle(22, 30, 5, "#FFD23F") + sparkle(106, 24, 4, "#7FE3FF") + sparkle(102, 92, 4, "#FF9ED0"),
    "белый волан с розовым ободком",
    "взлетает в ночное небо как ракета салюта, над ним раскрывается разноцветный фейерверк")

# 2. Новогорск: лягушонок на кувшинке отбивает волан ракеткой
add("badm-kurkino-sport-novogorsk", "c_lily",
    f'<path d="M-6 96 Q64 84 134 96 V140 H-6Z" fill="#4CB2C9" {W(2.6)}/>'
    + f'<path d="M22 104 Q64 88 106 104 Q100 118 64 118 Q28 118 22 104Z" fill="#6BCB5A" {W(3)}/>'
    + f'<path d="M64 104 L76 96" {W(2.4)}/>'
    + f'<ellipse cx="54" cy="84" rx="22" ry="16" fill="#7EDB6A" {W(3)}/>'
    + f'<circle cx="42" cy="66" r="9" fill="#7EDB6A" {W(3)}/><circle cx="64" cy="66" r="9" fill="#7EDB6A" {W(3)}/>'
    + f'<circle cx="42" cy="66" r="5.5" fill="#fff"/><circle cx="64" cy="66" r="5.5" fill="#fff"/>' + eye(42, 66, 0.7) + eye(64, 66, 0.7)
    + f'<path d="M46 86 Q54 92 62 86" fill="none" {W(2.4)}/>'
    + f'<ellipse cx="40" cy="84" rx="3.5" ry="2" fill="{PINK}" opacity=".7"/><ellipse cx="68" cy="84" rx="3.5" ry="2" fill="{PINK}" opacity=".7"/>'
    + limb("M72 84 Q82 78 84 70", "#7EDB6A", 6)
    + G(88, 50, racket(c="#FF8A3D", sc=0.62), rot=28)
    + G(104, 22, shuttle(sc=0.32, fc=False), rot=-130),
    "зелёный лягушонок с оранжевой бадминтонной ракеткой",
    "сидит на кувшинке посреди пруда и отбивает волан над водой")

# 3. МГТУ им. Баумана: волан на голубом чертеже, циркуль чертит его траекторию
_grid = "".join(f'<path d="M{x} -6 V140" stroke="#FFFFFF" stroke-opacity=".35" stroke-width="1"/>' for x in range(8, 128, 16)) + \
        "".join(f'<path d="M-6 {y} H140" stroke="#FFFFFF" stroke-opacity=".35" stroke-width="1"/>' for y in range(8, 128, 16))
add("badm-bauman-mytishchi", "c_blueprint",
    _grid
    + f'<path d="M20 98 Q40 26 104 40" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-dasharray="6 6" stroke-linecap="round"/>'
    + G(50, 78, shuttle(sc=0.72, band="#FFC93C"), rot=-20)
    + f'<path d="M100 18 L88 64 M100 18 L114 60" fill="none" stroke="#C9CED8" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M100 18 L88 64 M100 18 L114 60" fill="none" {W(1.6)}/>'
    + f'<circle cx="100" cy="16" r="5" fill="{GOLD}" {W(2.4)}/>'
    + f'<path d="M86 64 L88 72 L90 64" fill="#3B3355"/>'
    + f'<path d="M112 60 l4 8" {W(3)}/>',
    "белый волан с жёлтым ободком",
    "летит по пунктирной траектории на голубом инженерном чертеже, рядом циркуль, который её начертил")

# ============================== ШАХМАТЫ ==============================
# 4. «Дебют» (Королёв): чёрный слон-космонавт в шлеме стоит на Луне
add("chess-debut-korolev", "c_moon",
    f'<path d="M-6 104 Q64 92 134 104 V140 H-6Z" fill="#C7C9D9" {W(2.6)}/>'
    + f'<ellipse cx="30" cy="112" rx="9" ry="3.5" fill="#A8AABD" {W(1.8)}/><ellipse cx="100" cy="118" rx="12" ry="4" fill="#A8AABD" {W(1.8)}/>'
    + f'<circle cx="104" cy="28" r="12" fill="#5DA9F0" {W(2.6)}/><path d="M96 24 q6 -4 10 2 q4 6 -2 10" fill="#7DD36E"/>'
    + G(60, 106, bishop(WHITE, sc=0.82))
    + f'<circle cx="60" cy="56" r="21" fill="#BFE8FF" fill-opacity=".45" {W(3)}/>'
    + f'<path d="M48 44 Q52 38 58 38" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>'
    + f'<path d="M80 86 L96 72" {W(3)}/><rect x="92" y="58" width="16" height="12" fill="#FF6F61" {W(2.2)}/>'
    + sparkle(22, 30, 4) + sparkle(36, 16, 3),
    "белый шахматный слон в прозрачном шлеме космонавта",
    "стоит на Луне и втыкает в грунт красный флажок, над горизонтом висит голубая Земля")

# 5. «Досуг» (Красногорск): белый король отдыхает в полосатом шезлонге с шахматным журналом
add("chess-dosug-krasnogorsk", "c_beach",
    f'<circle cx="104" cy="26" r="11" fill="#FFE066" {W(2.4)}/>'
    + f'<path d="M24 112 L44 70 M92 112 L80 84 M38 84 L100 74" fill="none" stroke="#9A6A3E" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M44 70 L80 84 L94 112 L58 112Z" fill="#3FA7E0" {W(2.8)}/>'
    + f'<path d="M50 74 L64 104 M62 78 L76 108" stroke="#FFFFFF" stroke-width="5"/>'
    + G(66, 100, king(WHITE, sc=0.6), rot=-28)
    + f'<rect x="72" y="64" width="22" height="16" rx="2" fill="#FFFFFF" {W(2.4)}/>'
    + f'<rect x="76" y="68" width="6" height="6" fill="{O}"/><rect x="82" y="74" width="6" height="4" fill="{O}"/>'
    + f'<path d="M80 56 q4 -6 8 0 M90 52 q4 -6 8 0" fill="none" {W(2)}/>',
    "белый шахматный король",
    "развалился в голубом полосатом шезлонге под солнцем и читает шахматный журнал")

# 6. «Знаток» (Нахабино): чёрный ферзь за школьной партой тянет руку
add("chess-znatok-nakhabino", "c_class",
    f'<rect x="10" y="20" width="56" height="34" rx="3" fill="#2F5C46" {W(3)}/>'
    + f'<path d="M18 30 h10 M18 40 h18 M40 30 l6 10 l8 -14" fill="none" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round"/>'
    + G(80, 96, queen(BLACK, sc=0.7))
    + limb("M94 66 Q106 50 104 30", "#3A3550", 7)
    + f'<circle cx="104" cy="28" r="5" fill="#3A3550" {W(2)}/>'
    + f'<rect x="40" y="94" width="84" height="10" rx="2" fill="#D99A5B" {W(2.8)}/>'
    + f'<path d="M50 104 V126 M114 104 V126" {W(4)}/>'
    + f'<rect x="54" y="86" width="20" height="8" fill="#FFFFFF" {W(2)}/>',
    "чёрный шахматный ферзь",
    "сидит за школьной партой у доски с задачей и тянет руку вверх, зная ответ")

# 7. «Знаток» (Красногорск): белый конь в очках сидит в кресле и читает толстую книгу дебютов
add("chess-znatok-krasnogorsk", "c_den",
    f'<path d="M24 120 V62 Q24 46 40 46 H88 Q104 46 104 62 V120Z" fill="#7C3F58" {W(3)}/>'
    + f'<rect x="16" y="78" width="16" height="42" rx="6" fill="#93506E" {W(3)}/><rect x="96" y="78" width="16" height="42" rx="6" fill="#93506E" {W(3)}/>'
    + G(56, 112, knight(WHITE, sc=0.82))
    + f'<circle cx="43" cy="72" r="6" fill="none" {W(2.4)}/><circle cx="30" cy="73" r="6" fill="none" {W(2.4)}/><path d="M36 72 h1" {W(2)}/>'
    + f'<path d="M58 94 L76 86 L94 94 L94 112 L76 104 L58 112Z" fill="#FFFFFF" {W(2.6)}/>'
    + f'<path d="M76 86 V104" {W(2)}/><path d="M62 98 h10 M80 96 h10 M62 104 h8" fill="none" {W(1.4)}/>'
    + f'<path d="M58 94 v-4 h36 v4" fill="none" stroke="#C9473F" stroke-width="3"/>',
    "белый шахматный конь в круглых очках",
    "сидит в бордовом кресле и читает толстую книгу шахматных дебютов")

# 8. «Чемпион»: белая ладья на пьедестале поднимает золотой кубок
add("chess-champion-krasnogorsk", "c_podium",
    f'<rect x="34" y="102" width="60" height="26" fill="#FFFFFF" {W(3)}/><path d="M60 110 h8 v14" fill="none" {W(3)}/>'
    + f'<rect x="4" y="112" width="30" height="16" fill="#E6E6F2" {W(3)}/><rect x="94" y="116" width="30" height="12" fill="#E6E6F2" {W(3)}/>'
    + G(64, 102, rook(WHITE, sc=0.66))
    + limb("M52 68 Q42 54 50 40", WHITE, 6) + limb("M76 68 Q86 54 78 40", WHITE, 6)
    + f'<path d="M48 18 H80 Q80 38 64 42 Q48 38 48 18Z" fill="{GOLD}" {W(2.8)}/>'
    + f'<path d="M48 22 Q40 22 42 30 Q44 34 50 34 M80 22 Q88 22 86 30 Q84 34 78 34" fill="none" {W(2.4)}/>'
    + f'<rect x="60" y="42" width="8" height="4" fill="{GOLD}" {W(2)}/>'
    + sparkle(24, 30, 5) + sparkle(104, 34, 6) + sparkle(98, 66, 3),
    "белая шахматная ладья",
    "стоит на верхней ступени пьедестала и поднимает над головой золотой кубок")

# 9. Royal Gambit: белый король в мантии жонглирует шашкой, камнем го и пешкой
add("chess-royal-gambit-mytishchi", "c_juggle",
    f'<path d="M30 116 Q64 88 98 116Z" fill="#B0263A" {W(3)}/><path d="M34 112 l6 -4 l6 4 M86 112 l6 -4 l6 4" fill="none" stroke="#FFFFFF" stroke-width="2"/>'
    + G(64, 118, king(WHITE, sc=0.68))
    + limb("M54 82 Q38 70 34 56", WHITE, 6) + limb("M74 82 Q90 70 94 56", WHITE, 6)
    + f'<path d="M30 44 Q64 -4 98 44" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-dasharray="4 5"/>'
    + f'<ellipse cx="34" cy="38" rx="9" ry="5" fill="{RED}" {W(2.4)}/><ellipse cx="34" cy="35" rx="9" ry="5" fill="{RED}" {W(2.4)}/>'
    + f'<circle cx="64" cy="18" r="7" fill="#2B2B3A" {W(2.4)}/><circle cx="62" cy="16" r="2" fill="#FFFFFF" opacity=".6"/>'
    + G(96, 44, pawn(BLACK, sc=0.26, faced=False)),
    "белый шахматный король в красной мантии",
    "жонглирует над головой шашкой, чёрным камнем го и маленькой пешкой")

# 10. «Олимпик»: чёрная пешка-судья в полосатой рубашке со свистком
add("chess-olimpik-mytishchi", "c_ref",
    checks(14, 104, 6, 1, 17, "#FFFFFF", "#5A7FB8") + f'<rect x="14" y="104" width="102" height="17" fill="none" {W(2.4)}/>'
    + G(56, 104, pawn(BLACK, sc=0.88, faced=False))
    + f'<path d="M43 92 Q41 74 48 68 H64 Q71 74 69 92Z" fill="#FFFFFF" {W(2.6)}/>'
    + f'<path d="M48 70 V92 M56 68 V92 M64 70 V92" stroke="{O}" stroke-width="3"/>'
    + "".join(f'<circle cx="{56+dx}" cy="55" r="5.2" fill="#fff"/>' for dx in (-6, 6)) + face(56, 55, d=6, k=0.55, mouth=False)
    + f'<rect x="58" y="60" width="12" height="6" rx="2" fill="{GOLD}" {W(2)}/><path d="M70 63 q8 -2 10 -8" fill="none" {W(1.6)}/>'
    + f'<path d="M78 46 q6 -4 10 0 M82 38 q6 -4 10 0" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"/>'
    + f'<rect x="88" y="62" width="18" height="24" rx="2" fill="#FFE44D" {W(2.6)}/><path d="M97 86 v6" {W(2.6)}/>',
    "чёрная пешка-судья в полосатой бело-чёрной рубашке",
    "дует в золотой свисток и показывает жёлтую карточку у края доски")

# 11. «Гроссмейстер»: седой король с длинной бородой играет сеанс одновременной игры на трёх досках
add("chess-grossmeister-borisovka", "c_simul",
    "".join(checks(x, 96, 3, 2, 8, "#FFF4E0", "#6F5A44") + f'<rect x="{x}" y="96" width="24" height="16" fill="none" {W(2)}/>'
            + f'<rect x="{x-2}" y="112" width="28" height="5" fill="#9A6A3E" {W(2)}/>' for x in (8, 52, 96))
    + G(64, 92, king(WHITE, sc=0.6))
    + f'<path d="M56 74 Q64 100 72 74 Q64 80 56 74Z" fill="#FFFFFF" {W(2.4)}/>'
    + f'<path d="M58 66 Q64 63 70 66" fill="none" {W(2.2)}/>'
    + f'<path d="M50 82 L20 94 M78 82 L108 94" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="3 4"/>',
    "седой белый король-гроссмейстер с длинной белой бородой",
    "проводит сеанс одновременной игры, обходя сразу три маленькие шахматные доски")

# 12. Шахматная школа им. Карпова (гимназия): белая пешка-первоклассница с ранцем и букетом
add("chess-karpov-gymn16-mytishchi", "c_school",
    f'<path d="M-6 112 H134 V140 H-6Z" fill="#B5B9C9" {W(2.6)}/>'
    + f'<rect x="78" y="40" width="40" height="72" fill="#F6E1B5" {W(3)}/><path d="M74 42 L98 24 L122 42Z" fill="#D9604F" {W(3)}/>'
    + f'<rect x="90" y="88" width="16" height="24" fill="#8C5A3A" {W(2.6)}/><rect x="84" y="52" width="10" height="10" fill="#9ED8FF" {W(2)}/><rect x="102" y="52" width="10" height="10" fill="#9ED8FF" {W(2)}/>'
    + G(44, 118, pawn(WHITE, sc=0.78))
    + f'<rect x="56" y="70" width="18" height="22" rx="4" fill="{RED}" {W(2.6)}/><path d="M56 76 h18" {W(2)}/>'
    + f'<path d="M30 62 l-8 -18" stroke="#3E9B4F" stroke-width="3" stroke-linecap="round"/>'
    + "".join(f'<circle cx="{22+dx}" cy="{42+dy}" r="5" fill="{c}" {W(2)}/>' for dx, dy, c in [(-4, 0, "#FF7FA8"), (4, -3, "#FFD23F"), (2, 6, "#B07CF0")])
    + f'<path d="M34 30 l4 -6 l4 6 l-4 3Z" fill="#FFFFFF" {W(1.8)}/>',
    "белая пешка-первоклассница с красным ранцем",
    "идёт к школе с букетом цветов и белым бантом на голове")

# 13. «Импульс» (компьютерный класс): чёрный конь выпрыгивает из экрана ноутбука
add("chess-impuls-mytishchi", "c_laptop",
    f'<path d="M14 108 H114 L122 118 H6Z" fill="#C9CED8" {W(3)}/>'
    + f'<rect x="24" y="52" width="80" height="56" rx="4" fill="#2E3350" {W(3)}/>'
    + checks(30, 58, 6, 4, 11.4, "#BFF5E6", "#4FB59E")
    + G(66, 70, knight(BLACK, sc=0.62), rot=-14)
    + f'<path d="M40 52 Q34 40 40 30 M92 52 Q98 40 92 30" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>'
    + sparkle(26, 30, 5) + sparkle(104, 26, 6) + sparkle(110, 46, 3),
    "чёрный шахматный конь",
    "выпрыгивает прямо из экрана ноутбука с шахматной доской, вокруг искры")

# 14. Спортшкола по шахматам (Подольск): белая и чёрная пешки пожимают руки перед партией
add("chess-dyussh-podolsk", "c_hands",
    checks(14, 104, 6, 1, 17, "#FFF2D8", "#6C5A9E") + f'<rect x="14" y="104" width="102" height="17" fill="none" {W(2.4)}/>'
    + G(38, 104, pawn(WHITE, sc=0.82)) + G(90, 104, pawn(BLACK, sc=0.82))
    + limb("M50 78 Q58 72 64 74", WHITE, 7) + limb("M78 78 Q70 72 64 74", BLACK, 7)
    + f'<ellipse cx="64" cy="74" rx="7" ry="5" fill="{WHITE}" {W(2.4)}/>'
    + f'<path d="M58 54 l3 -6 M70 54 l-3 -6 M64 52 v-8" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>',
    "белая и чёрная пешки",
    "пожимают друг другу руки над краем шахматной доски перед партией")

# 15. СДЮСШОР Серпухов (шахматы + волейбол): волейбольный мяч в короне на шахматной доске
add("sdyushor-serpukhov-chess-volley", "c_throne",
    checks(8, 96, 7, 2, 16, "#FFF1DD", "#8A5A3C") + f'<rect x="8" y="96" width="112" height="32" fill="none" {W(2.6)}/>'
    + volley(64, 66, 27, c1="#FFD24A", c2="#3C7BD8", k=0.8)
    + f'<path d="M44 42 L40 22 L52 32 L64 16 L76 32 L88 22 L84 42Z" fill="{GOLD}" {W(2.8)}/>'
    + f'<circle cx="64" cy="16" r="3.4" fill="{RED}" {W(1.8)}/>'
    + G(22, 96, pawn(BLACK, sc=0.32, faced=False)) + G(106, 96, pawn(WHITE, sc=0.32, faced=False)),
    "волейбольный мяч в золотой королевской короне",
    "стоит вместо короля в центре шахматной доски, по краям — маленькие пешки")

# ============================== БАСКЕТБОЛ И ВОЛЕЙБОЛ ==============================
# 16. «Спарта»: мальчик-спартанец в шлеме с гребнем бросает мяч в кольцо
add("sparta-basket-khimki", "c_sparta",
    hoop(98, 44, w=30, bw=40)
    + f'<path d="M30 76 Q20 100 26 122 H54 Q58 100 50 76Z" fill="#C7302C" {W(2.8)}/>'
    + f'<rect x="34" y="80" width="18" height="26" rx="4" fill="#E9C46A" {W(2.6)}/>'
    + limb("M38 108 L34 124", SKIN, 6) + limb("M48 108 L54 124", SKIN, 6)
    + f'<circle cx="43" cy="64" r="13" fill="{SKIN}" {W(2.8)}/>' + face(43, 66, d=5, k=0.5)
    + f'<path d="M29 64 Q29 46 43 46 Q57 46 57 64 L52 64 L52 58 L34 58 L34 64Z" fill="#E0A93A" {W(2.6)}/>'
    + f'<path d="M30 48 Q43 26 58 46 Q44 40 30 48Z" fill="#D0302C" {W(2.4)}/>'
    + limb("M52 84 Q62 70 66 58", SKIN, 6)
    + ball(72, 46, 11, fc=False)
    + f'<path d="M80 40 Q88 34 90 38" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-dasharray="3 4"/>',
    "мальчик-спартанец в бронзовом шлеме с красным гребнем",
    "бросает баскетбольный мяч в кольцо, развевается красный плащ")

# 17. «Спартак Junior»: большой и маленький мячи идут за руку по паркету
add("spartak-junior-lyubertsy", "c_family",
    f'<path d="M-6 108 H134 V140 H-6Z" fill="#E9B26A" {W(2.6)}/>'
    + "".join(f'<path d="M{x} 108 L{x-10} 140" stroke="#C98D4A" stroke-width="2"/>' for x in range(10, 134, 20))
    + ball(48, 72, 30, k=0.85)
    + limb("M76 78 Q84 82 90 84", ORG, 5)
    + ball(98, 92, 14, k=0.45)
    + limb("M34 100 L30 112", ORG, 5) + limb("M60 100 L64 112", ORG, 5)
    + limb("M94 106 L92 112", ORG, 4) + limb("M102 106 L104 112", ORG, 4),
    "большой баскетбольный мяч-мама и маленький мячик-малыш",
    "шагают за руку по паркету спортзала, малыш едва достаёт до маминой руки")

# 18. СШОР «Спартак» (Люберцы): баскетбольный мяч спускается на парашюте прямо в кольцо
add("sshor-spartak-basket-lyubertsy", "c_chute",
    f'<path d="M22 44 Q64 -4 106 44 Q96 38 85 44 Q75 36 64 44 Q53 36 43 44 Q32 38 22 44Z" fill="#FF6F61" {W(3)}/>'
    + f'<path d="M43 44 Q50 14 64 6 M85 44 Q78 14 64 6" fill="none" {W(2)}/>'
    + f'<path d="M22 44 L52 70 M43 44 L56 66 M85 44 L72 66 M106 44 L76 70" fill="none" {W(1.6)}/>'
    + ball(64, 78, 17, k=0.55)
    + hoop(64, 108, w=40, board=False),
    "баскетбольный мяч с улыбкой",
    "спускается на красном парашюте точно в кольцо с сеткой")

# 19. JUNIBASKET (Люберцы): малыш встал на табуретку и опускает мяч в низкое кольцо
add("junibasket-lyubertsy", "c_stool",
    f'<path d="M90 120 V40" stroke="#8C8FA6" stroke-width="6"/><path d="M90 120 V40" {W(1.6)}/>'
    + hoop(72, 52, w=30, board=False)
    + f'<rect x="20" y="96" width="34" height="8" rx="2" fill="#4FB0E8" {W(2.6)}/><path d="M24 104 L22 122 M50 104 L52 122" fill="none" {W(4)}/>'
    + limb("M32 94 V82", SKIN, 6) + limb("M44 94 V82", SKIN, 6)
    + f'<path d="M28 84 Q26 66 38 64 Q50 66 48 84Z" fill="#FFD23F" {W(2.6)}/>'
    + head(38, 52, hair="#C9832E", r=11, style="short")
    + limb("M46 70 Q56 62 62 50", SKIN, 5)
    + ball(68, 42, 10, fc=False),
    "малыш-дошкольник в жёлтой футболке",
    "встал на голубую табуретку и опускает мяч в низкое детское кольцо")

# 20. JUNIBASKET (Долгопрудный): улитка несёт баскетбольный мяч вместо раковины
add("junibasket-dolgoprudny", "c_snail",
    f'<path d="M-6 108 Q64 98 134 108 V140 H-6Z" fill="#A9D96A" {W(2.6)}/>'
    + f'<path d="M14 108 Q20 92 40 92 H98 Q112 92 112 76 Q112 62 104 56" fill="#FFC4A8" {W(3)}/>'
    + f'<path d="M14 108 H100 Q118 106 118 86 Q118 64 104 56 L98 66 Q104 74 102 84 Q100 94 90 96 H30 Q18 98 14 108Z" fill="#FFC4A8" {W(3)}/>'
    + f'<path d="M100 58 L94 40 M108 58 L112 40" {W(2.4)}/><circle cx="94" cy="38" r="3.6" fill="{O}"/><circle cx="112" cy="38" r="3.6" fill="{O}"/>'
    + face(104, 74, d=5, k=0.45, mouth=True)
    + ball(54, 66, 28, fc=False),
    "розовая улитка",
    "медленно ползёт по траве, а вместо раковины у неё на спине баскетбольный мяч")

# 21. «Стремление» (Мытищи): мяч на ходулях тянется к кольцу
add("stremlenie-basket-mytishchi", "c_stilts",
    hoop(96, 34, w=28, bw=38)
    + f'<path d="M40 70 L30 124 M64 70 L74 124" stroke="#9A6A3E" stroke-width="6" stroke-linecap="round"/><path d="M40 70 L30 124 M64 70 L74 124" {W(1.6)}/>'
    + f'<path d="M26 108 h10 M70 108 h10" {W(4)}/>'
    + ball(52, 50, 20, k=0.6)
    + limb("M68 44 Q76 36 80 30", ORG, 5),
    "баскетбольный мяч",
    "встал на высокие деревянные ходули и тянется лапкой к кольцу")

# 22. B-ball: мяч-фокусник достаёт из цилиндра маленький мячик
add("bball-mytishchi", "c_magic",
    ball(46, 66, 24, k=0.7)
    + f'<path d="M66 62 L84 60" {W(3)}/><path d="M84 60 L104 56" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round"/><path d="M84 60 L104 56" {W(1.4)}/>'
    + f'<path d="M64 108 L70 80 H106 L112 108Z" fill="#26243A" {W(3)}/><ellipse cx="88" cy="80" rx="22" ry="6" fill="#3E3B5A" {W(2.6)}/>'
    + f'<rect x="68" y="96" width="40" height="5" fill="{RED}"/>'
    + ball(88, 72, 9, fc=False)
    + sparkle(100, 40, 5, GOLD) + sparkle(76, 36, 3, "#FFFFFF") + sparkle(22, 26, 4, "#FFFFFF"),
    "баскетбольный мяч-фокусник с волшебной палочкой",
    "взмахом палочки достаёт из чёрного цилиндра маленький мячик, вокруг звёздочки")

# 23. СДЮШОР по баскетболу Мытищи (с 1961): старый кожаный мяч со шнуровкой даёт пять новому
add("sdyushor-basket-mytishchi", "c_retro",
    f'<circle cx="38" cy="74" r="24" fill="#9C5A2E" {W(3)}/>'
    + f'<path d="M38 50 V98 M14 74 H62" fill="none" {W(2)}/><path d="M34 58 h8 M34 64 h8 M34 70 h8" fill="none" stroke="#F2E2C4" stroke-width="2"/>'
    + face(38, 80, d=7, k=0.6)
    + ball(92, 74, 24, k=0.7)
    + limb("M58 60 L64 46", "#9C5A2E", 5) + limb("M72 60 L66 46", ORG, 5)
    + f'<path d="M58 38 l-4 -6 M66 34 v-7 M74 38 l4 -6" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>',
    "старый коричневый кожаный мяч со шнуровкой",
    "даёт пять новенькому оранжевому баскетбольному мячу")

# 24. «Взлёт» (Жуковский): мальчик-баскетболист в высоком прыжке над облаками кладёт мяч в кольцо
add("vzlet-basket-zhukovsky", "c_clouds",
    f'<path d="M-6 112 Q14 96 34 108 Q50 92 70 106 Q90 92 108 108 Q124 98 134 108 V140 H-6Z" fill="#FFFFFF" {W(2.6)}/>'
    + hoop(92, 38, w=28, bw=38)
    + limb("M48 82 L36 100", SKIN, 6) + limb("M58 82 L66 98", SKIN, 6)
    + f'<path d="M40 82 Q38 62 52 58 Q66 62 62 82Z" fill="#2E6FD6" {W(2.6)}/><path d="M48 66 h8" stroke="#FFFFFF" stroke-width="3"/>'
    + head(52, 46, hair="#3B2A1E", r=11)
    + limb("M60 62 Q72 48 82 40", SKIN, 5)
    + ball(88, 30, 9, fc=False)
    + f'<path d="M30 70 Q24 60 30 50 M24 84 Q16 74 20 62" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>',
    "мальчик-баскетболист в синей форме",
    "взлетел в прыжке выше облаков и кладёт мяч в кольцо сверху")

# 25. «Авангард» (волейбол): большой волейбольный мяч ведёт за собой три маленьких мячика, как утка утят
add("avangard-volley-mytishchi", "c_ducks",
    f'<path d="M-6 104 Q64 96 134 104 V140 H-6Z" fill="#F2E3B8" {W(2.6)}/>'
    + volley(36, 72, 24, c1="#FFD24A", c2="#2F6FD0", k=0.7)
    + limb("M26 94 L24 104", "#FFFFFF", 5) + limb("M44 94 L46 104", "#FFFFFF", 5)
    + "".join(volley(x, 96, 9, c1="#FFD24A", c2="#2F6FD0", fc=False) + f'<circle cx="{x-2}" cy="95" r="1.6" fill="{O}"/><circle cx="{x+3}" cy="95" r="1.6" fill="{O}"/>'
              for x in (70, 92, 114))
    + f'<path d="M64 86 q4 -4 8 0 M86 86 q4 -4 8 0" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>',
    "большой волейбольный мяч-вожак",
    "шагает по песку впереди, а за ним гуськом спешат три маленьких волейбольных мячика")

# 26. СДЮСШОР «Балашиха»: футбольный, баскетбольный и бейсбольный мячи в обнимку на пьедестале
add("sdyusshor-balashikha", "c_trio",
    f'<rect x="12" y="104" width="104" height="24" fill="#FFFFFF" {W(3)}/>'
    + soccer(36, 82, 20, k=0.55)
    + f'<circle cx="94" cy="86" r="16" fill="#FFFFFF" {W(3)}/>'
    + f'<path d="M84 74 Q90 86 84 98 M104 74 Q98 86 104 98" fill="none" stroke="{RED}" stroke-width="2"/>'
    + face(94, 88, d=5, k=0.45)
    + ball(64, 64, 24, k=0.7)
    + limb("M52 80 Q46 86 44 80", ORG, 4) + limb("M76 80 Q82 86 86 82", ORG, 4),
    "три мяча — футбольный, баскетбольный и бейсбольный",
    "стоят в обнимку на белом пьедестале, баскетбольный — посередине")

# 27. Волейбольный центр (Одинцово): девушка с хвостиком в прыжке подаёт мяч в лучах прожекторов
add("volley-center-odintsovo", "c_arena",
    f'<path d="M10 -6 L36 120 H60Z M118 -6 L92 120 H68Z" fill="#FFF6C8" opacity=".35"/>'
    + f'<circle cx="10" cy="4" r="8" fill="#FFF6C8" {W(2.4)}/><circle cx="118" cy="4" r="8" fill="#FFF6C8" {W(2.4)}/>'
    + f'<path d="M-6 116 H134 V140 H-6Z" fill="#E07A3A" {W(2.6)}/>'
    + limb("M56 92 L48 112", SKIN, 6) + limb("M66 92 L74 110", SKIN, 6)
    + f'<path d="M50 94 Q48 70 62 66 Q76 70 72 94Z" fill="#E63B6F" {W(2.6)}/><text x="56" y="88" font-size="12" font-family="Arial" font-weight="bold" fill="#FFFFFF">5</text>'
    + head(62, 54, hair="#5A3420", r=11, style="tail")
    + limb("M70 70 Q82 56 84 42", SKIN, 5)
    + volley(88, 30, 11, fc=False),
    "девушка-волейболистка с хвостиком в розовой форме № 5",
    "в прыжке подаёт мяч на ночной арене, сверху светят два прожектора")

# 28. «Подросток» (Подольск): подросток в кепке козырьком назад крутит мяч на пальце
add("podrostok-podolsk", "c_teen",
    f'<path d="M30 128 Q30 96 64 92 Q98 96 98 128Z" fill="#7B5CD6" {W(3)}/>'
    + f'<path d="M58 96 L64 106 L70 96" fill="none" {W(2.4)}/>'
    + head(64, 70, hair="#2E2A26", r=17, k=0.6)
    + f'<path d="M47 62 Q48 46 64 46 Q80 46 81 62Z" fill="#2FA86A" {W(2.6)}/><path d="M48 60 Q36 60 32 66 Q44 66 50 64Z" fill="#2FA86A" {W(2.4)}/>'
    + limb("M92 112 Q104 90 102 62", SKIN, 6)
    + ball(102, 40, 15, k=0.45)
    + f'<path d="M84 40 Q86 28 96 24 M120 40 Q118 52 108 56" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>',
    "подросток в зелёной кепке козырьком назад",
    "крутит баскетбольный мяч на одном пальце и довольно улыбается")

# 29. «Звезда» (Серпухов): девочка ведёт мяч между оранжевыми конусами
add("zvezda-dyussh-serpukhov", "c_cones",
    f'<path d="M-6 110 H134 V140 H-6Z" fill="#D9B07A" {W(2.6)}/>'
    + "".join(f'<path d="M{x-8} 112 L{x} 92 L{x+8} 112Z" fill="#FF8A2B" {W(2.4)}/><path d="M{x-5} 104 H{x+5}" stroke="#FFFFFF" stroke-width="2.6"/>'
              for x in (16, 112))
    + f'<path d="M24 118 Q44 100 64 118 Q84 134 104 118" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-dasharray="4 5"/>'
    + limb("M54 88 L46 108", SKIN, 6) + limb("M64 88 L70 108", SKIN, 6)
    + f'<path d="M46 90 Q44 66 58 62 Q72 66 70 90Z" fill="#3BB0E0" {W(2.6)}/>'
    + head(58, 48, hair="#E0A53A", r=11, style="tail")
    + limb("M68 72 Q78 80 82 92", SKIN, 5)
    + ball(84, 104, 10, fc=False),
    "девочка с рыжим хвостиком в голубой майке",
    "ведёт баскетбольный мяч змейкой между оранжевыми конусами")

# ============================== НАСТОЛЬНЫЙ ТЕННИС ==============================
# 30. «Твоя подача» (Красный кит): рука с ракеткой, мячик подброшен высоко над ладонью
add("tvoya-podacha-krasny-kit", "c_serve",
    table(64, 104, 116, h=9, c="#2E7FD0", legs=False)
    + limb("M14 96 Q28 80 34 70", SKIN, 9)
    + f'<ellipse cx="38" cy="66" rx="9" ry="6" fill="{SKIN}" {W(2.6)}/>'
    + f'<path d="M40 62 V24" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-dasharray="3 5" stroke-linecap="round"/>'
    + ttball(40, 18, 7, "#FFFFFF") + face(40, 18, d=2.6, k=0.25, mouth=False, blush=False)
    + paddle(90, 60, rot=30, c=RED, sc=1.05)
    + limb("M118 100 Q110 86 100 76", SKIN, 8),
    "ракетка для настольного тенниса в руке игрока",
    "перед подачей: другая рука подбросила белый мячик высоко вверх над синим столом")

# 31. «Твоя подача» (ТРЦ «Июнь»): оранжевый мячик в солнечных очках загорает на столе
add("tvoya-podacha-iyun", "c_sun",
    f'<circle cx="100" cy="26" r="13" fill="#FFE34D" {W(2.6)}/>'
    + "".join(f'<path d="M{100+18*math.cos(math.radians(a)):.1f} {26+18*math.sin(math.radians(a)):.1f} L{100+25*math.cos(math.radians(a)):.1f} {26+25*math.sin(math.radians(a)):.1f}" {W(2.6)}/>' for a in range(0, 360, 45))
    + table(64, 92, 120, h=10, c="#2F9F6A")
    + f'<path d="M64 92 V74" {W(2)}/><path d="M64 74 H120 V92" fill="none" stroke="#FFFFFF" stroke-width="1.2"/>'
    + f'<circle cx="38" cy="74" r="17" fill="#FF9A3C" {W(3)}/>'
    + f'<path d="M24 68 H52" {W(2.4)}/><rect x="25" y="66" width="11" height="8" rx="3" fill="{O}"/><rect x="40" y="66" width="11" height="8" rx="3" fill="{O}"/>'
    + f'<path d="M32 80 Q38 85 44 80" fill="none" {W(2.4)}/>'
    + paddle(88, 70, rot=-80, c=RED, sc=0.75),
    "оранжевый мячик для настольного тенниса в солнечных очках",
    "загорает на зелёном теннисном столе под летним солнцем, рядом лежит ракетка")

# 32. Tn Club: белый мячик скачет дугами по столу
add("tn-club-mytishchi", "c_bounce",
    f'<path d="M8 96 L120 96 L110 80 L18 80Z" fill="#2E6BC8" {W(2.8)}/>'
    + f'<path d="M64 80 V96" stroke="#FFFFFF" stroke-width="2"/><path d="M14 88 H114" stroke="#FFFFFF" stroke-width="1.4" opacity=".6"/>'
    + f'<path d="M58 70 V96 M70 70 V96" {W(2)}/><rect x="58" y="70" width="12" height="10" fill="#FFFFFF" fill-opacity=".6" {W(1.6)}/>'
    + f'<path d="M8 96 V118 M120 96 V118" {W(4)}/>'
    + f'<path d="M20 82 Q32 40 46 82 Q60 24 82 82" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-dasharray="3 5" stroke-linecap="round"/>'
    + "".join(f'<ellipse cx="{x}" cy="82" rx="5" ry="1.6" fill="#FFFFFF" opacity=".8"/>' for x in (20, 46))
    + f'<circle cx="96" cy="50" r="14" fill="#FFFFFF" {W(3)}/>' + face(96, 50, d=4.5, k=0.42),
    "белый мячик для настольного тенниса",
    "весело скачет по синему столу, оставляя пунктирные дуги-следы")

# 33. V2 (Лефортово): мальчик в очках делает топспин, мячик крутится со следом вращения
add("v2-ttc-lefortovo", "c_spin",
    table(74, 100, 100, h=9, c="#1F7A5A", legs=True)
    + limb("M34 92 L28 120", SKIN, 6) + limb("M44 92 L50 120", SKIN, 6)
    + f'<path d="M26 94 Q24 70 38 66 Q52 70 50 94Z" fill="#F5C33B" {W(2.6)}/>'
    + head(38, 52, hair="#4A3022", r=12)
    + f'<circle cx="33" cy="54" r="4.6" fill="none" {W(1.8)}/><circle cx="43" cy="54" r="4.6" fill="none" {W(1.8)}/>'
    + limb("M48 76 Q60 74 66 62", SKIN, 5)
    + paddle(72, 54, rot=-60, c=RED, sc=0.7)
    + f'<path d="M86 50 a12 12 0 1 1 8 20" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/><path d="M94 70 l-6 1 l3 -6" fill="none" stroke="#FFFFFF" stroke-width="2.4"/>'
    + ttball(96, 58, 5.5, "#FF9A3C"),
    "мальчик в круглых очках с ракеткой для настольного тенниса",
    "закручивает мяч топспином над столом, вокруг мячика — стрелка вращения")

# 34. TTleadeR (Савёловский вокзал): ракетка-паровоз везёт вагончики-мячики
add("ttleader-savelovsky", "c_train",
    f'<path d="M-6 112 H134" {W(3)}/>' + "".join(f'<rect x="{x}" y="112" width="10" height="4" fill="#9A6A3E" {W(1.4)}/>' for x in range(0, 128, 16))
    + G(88, 72, f'<rect x="-3.5" y="10" width="7" height="18" rx="3" fill="#C98B4E" {W(2.6)}/><circle cx="0" cy="0" r="22" fill="{RED}" {W(3)}/>', rot=-90)
    + face(88, 72, d=7, k=0.6)
    + f'<rect x="56" y="58" width="10" height="16" rx="2" fill="#C98B4E" {W(2.4)}/>'
    + f'<path d="M58 54 q-4 -10 4 -14 q-6 -12 6 -16" fill="none" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round"/>'
    + f'<circle cx="78" cy="102" r="7" fill="#3B3355"/><circle cx="100" cy="102" r="7" fill="#3B3355"/>'
    + "".join(f'<rect x="{x-12}" y="86" width="24" height="16" rx="3" fill="#FFD23F" {W(2.4)}/>' + ttball(x, 80, 7, c) + f'<circle cx="{x-6}" cy="106" r="4.5" fill="#3B3355"/><circle cx="{x+6}" cy="106" r="4.5" fill="#3B3355"/>'
              for x, c in ((44, "#FFFFFF"), (16, "#FF9A3C")))
    + f'<path d="M56 96 H66 M28 96 H32" {W(2.4)}/>',
    "красная ракетка для настольного тенниса-паровозик",
    "везёт по рельсам два вагончика, в которых едут белый и оранжевый мячики")

# ============================== ФЕХТОВАНИЕ ==============================
# 35. FC Flash (Куркино): фехтовальщица в белом делает выпад саблей, клинок оставляет след-молнию
add("flash-fencing-kurkino", "c_flash",
    f'<rect x="-6" y="108" width="140" height="10" fill="#8C8FA6" {W(2.4)}/>'
    + limb("M44 84 L22 108", "#FFFFFF", 8) + limb("M50 84 L66 106", "#FFFFFF", 8)
    + f'<path d="M36 86 Q34 62 48 58 Q60 60 58 86Z" fill="#FFFFFF" {W(2.8)}/>'
    + limb("M40 66 Q30 58 24 44", "#FFFFFF", 6)
    + f'<circle cx="52" cy="44" r="12" fill="#3B3355" {W(2.6)}/>'
    + "".join(f'<path d="M{44+i*4} 36 V54" stroke="#8C8FA6" stroke-width="1.2"/>' for i in range(5))
    + f'<path d="M38 50 Q32 44 34 38" fill="none" stroke="#7A4A2E" stroke-width="4" stroke-linecap="round"/>'
    + limb("M56 66 Q66 60 72 58", "#FFFFFF", 6)
    + f'<path d="M72 58 L118 34" stroke="#C9CED8" stroke-width="3.4" stroke-linecap="round"/><path d="M72 58 L118 34" {W(1.2)}/>'
    + f'<path d="M70 52 Q68 62 76 64" fill="none" stroke="{GOLD}" stroke-width="4"/>'
    + f'<path d="M86 30 L98 40 L92 42 L104 54" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>'
    + f'<path d="M86 30 L98 40 L92 42 L104 54" fill="none" stroke="#FFC400" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>',
    "девочка-саблистка в белом фехтовальном костюме и чёрной маске",
    "делает глубокий выпад на дорожке, клинок сабли оставляет в воздухе след-молнию")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for pid, code in ICONS.items():
        open(os.path.join(OUT, pid + ".svg"), "w").write(code)
    reg = os.path.join(OUT, "subjects.txt")
    lines = [l for l in open(reg, encoding="utf-8") if l.split(" — ", 1)[0] not in SUBJ]
    lines += [line + "\n" for line in SUBJ.values()]
    open(reg, "w", encoding="utf-8").writelines(lines)
    print(len(ICONS), "иконок:", " ".join(ICONS))
