"""Иконки робота sections, 2026-11-08 (03 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно,
свой герой, своя сцена, своя палитра фона.
Шахматы: ферзь-балерина, конь-рыбак у пруда, король-почтальон, девочка с конём-кубком, ладья-терем Коломенского,
пешка-факелоносец «Олимпа», пешка прорывает бумажный обруч («Прорыв»), конь лепит снежную пешку.
Мячи: рост у стойки кольца («Росток»), крылатая Ника на подаче, пеликан-либеро.
Прочий спорт: робот-пушка для пинг-понга, тигрёнок у теннисного стола, малыш на скамеечке у стола, лучница на холме,
рыцарь с арбалетом («Айвенго»), яблоко со стрелой (Shooting Academy), каноистка, маска фехтовальщика в сальто,
теннисный мяч ныряет в бассейн, мяч-эстафетчик, форвард с номером 9, малыш бросает плюшевого медведя, носорожек-борец.
Сверено со всеми листами icons-catalog/sheet-01…36 и icons-src/subjects.txt.
Запуск: python3 tools/icons_sections_1108b.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O
from icons_sections_1107h import G, king, queen, rook, bishop, knight, pawn, checks, WHITE, BLACK
from icons_sections_1107c import ball, hoop

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
PINK, GOLD, RED, ORG = "#FF7FA8", "#FFC93C", "#E8554A", "#F28C38"
SKIN = "#FFD8B8"
draw_icons.BG.update({
    "b_rosewater": ("#FFF0F5", "#F4A7C6"), "b_pond": ("#E3F7FF", "#5FB3D9"), "b_letter": ("#FFF6E5", "#E9B872"),
    "b_cup": ("#F4FFE6", "#9FD86B"), "b_terem": ("#FFF3E0", "#D98E5C"), "b_torch": ("#FFF4D6", "#F2A93B"),
    "b_hoop": ("#FCE9FF", "#B27BE0"), "b_snow": ("#F5FAFF", "#A8C7EE"), "b_grow": ("#EAFBF4", "#62C99A"),
    "b_nike": ("#FFFBEA", "#E7C65A"), "b_pelican": ("#E6FAFF", "#47B5C9"), "b_robot": ("#EEF0FF", "#7C86E8"),
    "b_tiger": ("#FFF1E3", "#F49B5A"), "b_bench": ("#F2FFF0", "#7BC47F"), "b_hill": ("#FFFDE8", "#B9D45A"),
    "b_knight": ("#F0EAFF", "#8E73C9"), "b_apple": ("#FFF3EE", "#E9776A"), "b_canoe": ("#E8FFFB", "#2FA8A0"),
    "b_flip": ("#FFF0FA", "#D06BB5"), "b_dive": ("#E9F9FF", "#3E9FE0"), "b_relay": ("#FFF6F0", "#E58A56"),
    "b_nine": ("#EFFFF0", "#4DB86A"), "b_teddy": ("#FFF8E8", "#D9B36A"), "b_rhino": ("#EEF3F8", "#8AA1BC"),
})


def add(pid, bg, body, hero, scene):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def limb(d, c=SKIN, w=6):
    return (f'<path d="{d}" fill="none" stroke="{O}" stroke-width="{w+3}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')


def head(x, y, hair="#7A4A2E", r=13, k=0.5, style="short"):
    g = f'<circle cx="0" cy="0" r="{r}" fill="{SKIN}" {W(2.8)}/>'
    if style == "short":
        g += f'<path d="M{-r} -1 Q{-r} {-r-4} 0 {-r-3} Q{r} {-r-4} {r} -1 Q{r*0.4} {-r*0.55} 0 {-r*0.6} Q{-r*0.5} {-r*0.55} {-r} -1Z" fill="{hair}" {W(2.4)}/>'
    elif style == "tail":
        g += (f'<path d="M{r-2} -6 Q{r+14} -8 {r+10} 10 Q{r+4} 2 {r-1} 2Z" fill="{hair}" {W(2.4)}/>'
              f'<path d="M{-r} -1 Q{-r} {-r-4} 0 {-r-3} Q{r} {-r-4} {r} -1 Q{r*0.4} {-r*0.55} 0 {-r*0.6} Q{-r*0.5} {-r*0.55} {-r} -1Z" fill="{hair}" {W(2.4)}/>')
    g += face(0, 2, d=r * 0.38, k=k)
    return G(x, y, g)


def ttball(x, y, r=5, c="#FF9A3C"):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" {W(2.2)}/>'


def paddle(x, y, rot=0, c=RED, sc=1.0):
    g = (f'<rect x="-3.5" y="10" width="7" height="18" rx="3" fill="#C98B4E" {W(2.6)}/>'
         f'<circle cx="0" cy="0" r="14" fill="{c}" {W(3)}/>')
    return G(x, y, g, rot=rot, sc=sc)


def soccer(cx, cy, r, fc=True, k=None):
    k = k or r / 30
    pent = lambda x, y, a: f'<polygon points="' + " ".join(
        f"{x + a*math.cos(math.radians(-90+72*i)):.1f},{y + a*math.sin(math.radians(-90+72*i)):.1f}" for i in range(5)) + f'" fill="{O}"/>'
    out = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#FFFFFF" {W(3)}/>'
    out += pent(cx, cy - r * 0.62, r * 0.22) + pent(cx - r * 0.7, cy + r * 0.1, r * 0.18) + pent(cx + r * 0.7, cy + r * 0.1, r * 0.18)
    if fc:
        out += face(cx, cy + r * 0.1, d=r * 0.26, k=k)
    return out


def volley(cx, cy, r, c1="#FFD24A", c2="#4A8FE0", fc=True, k=None):
    k = k or r / 30
    out = (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#FFFFFF" {W(3)}/>'
           f'<path d="M{cx} {cy-r} Q{cx+r*0.2} {cy-r*0.2} {cx+r*0.9} {cy-r*0.35} Q{cx+r*0.6} {cy-r*0.9} {cx} {cy-r}Z" fill="{c1}" {W(2)}/>'
           f'<path d="M{cx-r*0.95} {cy+r*0.15} Q{cx-r*0.2} {cy+r*0.05} {cx-r*0.3} {cy+r*0.92} Q{cx-r*0.85} {cy+r*0.65} {cx-r*0.95} {cy+r*0.15}Z" fill="{c2}" {W(2)}/>')
    if fc:
        out += face(cx + r * 0.1, cy + r * 0.05, d=r * 0.26, k=k)
    return out


# ============================== ШАХМАТЫ ==============================
# 1. Донской: белый ферзь в розовой пачке делает пируэт на одной клетке
_q = queen(WHITE, sc=0.78)
add("chess-korolevstvo-donskoy", "b_rosewater",
    checks(24, 104, 5, 1, 16, "#FFF4E8", "#9C6B8E")
    + f'<rect x="24" y="104" width="80" height="16" fill="none" {W(2.4)}/>'
    + G(64, 100, _q)
    + f'<path d="M34 88 Q64 70 94 88 Q90 96 64 94 Q38 96 34 88Z" fill="#FFB3D1" {W(2.8)}/>'
    + f'<path d="M40 88 l4 6 M52 90 l2 5 M64 91 v5 M76 90 l-2 5 M88 88 l-4 6" fill="none" {W(1.6)}/>'
    + f'<path d="M22 46 Q14 60 22 70" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>'
    + f'<path d="M106 46 Q114 60 106 70" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>'
    + sparkle(100, 30, 6) + sparkle(28, 32, 4),
    "белый шахматный ферзь в розовой балетной пачке",
    "кружится в пируэте на одной клетке шахматной полоски, вокруг — дуги вращения")

# 2. Борисово: белый конь-рыбак с удочкой на берегу пруда, клюёт чёрная пешка
add("chess-korolevstvo-borisovo", "b_pond",
    f'<path d="M-6 84 Q40 78 70 84 Q100 90 134 84 V140 H-6Z" fill="#4FA6DA" {W(2.6)}/>'
    + f'<path d="M-6 92 L46 92 Q50 100 46 140 H-6Z" fill="#8FCF6A" {W(2.6)}/>'
    + G(32, 96, knight(WHITE, sc=0.78, flip=True))
    + f'<path d="M44 56 L104 26" stroke="#9A6A3E" stroke-width="5" stroke-linecap="round"/><path d="M44 56 L104 26" {W(1.4)}/>'
    + f'<path d="M104 26 Q108 60 98 92" fill="none" stroke="{O}" stroke-width="1.6"/>'
    + G(98, 112, pawn(BLACK, sc=0.42))
    + f'<path d="M84 94 q6 -4 12 0 M100 94 q6 -4 12 0" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>'
    + f'<circle cx="98" cy="90" r="3" fill="{RED}" {W(1.6)}/>',
    "белый шахматный конь-рыбак",
    "сидит на берегу пруда с удочкой, а на крючок клюёт маленькая чёрная пешка")

# 3. Серпуховская: чёрный король-почтальон с сумкой и конвертом
add("chess-korolevstvo-serpukhovskaya", "b_letter",
    G(58, 114, king(BLACK, sc=0.9))
    + f'<path d="M42 50 L84 96" stroke="#7A4A2E" stroke-width="5" stroke-linecap="round"/>'
    + f'<rect x="70" y="80" width="34" height="26" rx="5" fill="#B5763F" {W(3)}/>'
    + f'<path d="M70 88 H104" fill="none" {W(2.2)}/><circle cx="87" cy="93" r="2.6" fill="{GOLD}" {W(1.4)}/>'
    + G(98, 48, f'<rect x="-15" y="-10" width="30" height="20" rx="2" fill="#FFFFFF" {W(2.6)}/>'
                f'<path d="M-15 -10 L0 2 L15 -10" fill="none" {W(2.2)}/><circle cx="0" cy="3" r="3" fill="{RED}"/>', rot=-14)
    + f'<path d="M86 64 Q80 70 74 70" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>',
    "чёрный шахматный король-почтальон с кожаной сумкой через плечо",
    "разносит письма: в поднятой руке белый конверт с красной печатью")

# 4. Беляево: девочка поднимает над головой белого коня, как кубок
add("chess-korolevstvo-belyaevo", "b_cup",
    f'<path d="M24 128 Q30 96 64 92 Q98 96 104 128Z" fill="#FFCF4A" {W(3)}/>'
    + limb("M46 104 Q36 80 44 58", SKIN, 6) + limb("M82 104 Q92 80 84 58", SKIN, 6)
    + head(64, 82, "#5A3A2A", r=14, style="tail")
    + G(64, 60, knight(WHITE, sc=0.62))
    + sparkle(26, 40, 6, GOLD) + sparkle(104, 34, 5, GOLD) + sparkle(98, 62, 3.5),
    "девочка с хвостиком в жёлтой футболке",
    "победно поднимает над головой белого шахматного коня, как кубок, вокруг искры")

# 5. Коломенская: чёрная ладья-терем с шатровой крышей и флюгером
add("chess-korolevstvo-kolomenskaya", "b_terem",
    f'<path d="M-6 112 Q64 100 134 112 V140 H-6Z" fill="#7CC36A" {W(2.6)}/>'
    + G(64, 118, rook(BLACK, sc=0.95, fy=-34))
    + f'<path d="M42 48 L64 14 L86 48Z" fill="#C2402F" {W(3)}/>'
    + f'<path d="M50 48 L64 26 L78 48" fill="none" {W(1.6)}/>'
    + f'<path d="M64 14 V4" {W(2.4)}/><path d="M64 5 L76 9 L64 13Z" fill="{GOLD}" {W(1.8)}/>'
    + f'<rect x="56" y="92" width="16" height="18" rx="8" fill="#F2C46B" {W(2.4)}/>',
    "чёрная шахматная ладья-терем с красной шатровой крышей",
    "стоит на зелёном холме, как деревянный терем Коломенского, на шпиле — золотой флажок-флюгер")

# 6. «Олимп» (Кожуховская): белая пешка бежит с олимпийским факелом
add("chess-olimp-kozhukhovo", "b_torch",
    f'<path d="M14 112 H114" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round" opacity=".8"/>'
    + G(54, 112, pawn(WHITE, sc=1.0), rot=8)
    + limb("M70 70 Q82 62 88 50", "#FFF8EE", 6)
    + f'<path d="M84 52 L96 52 L92 70 L88 70Z" fill="#B0B5C8" {W(2.6)}/>'
    + f'<path d="M90 50 Q80 36 90 20 Q92 32 98 30 Q104 40 94 50Z" fill="#FF8A3C" {W(2.6)}/>'
    + f'<path d="M91 48 Q88 40 92 34 Q94 42 96 44Z" fill="{GOLD}"/>'
    + f'<path d="M16 64 H32 M10 76 H28 M18 88 H30" stroke="#FFFFFF" stroke-width="3.4" stroke-linecap="round"/>',
    "белая шахматная пешка-факелоносец",
    "бежит по дорожке, высоко подняв горящий олимпийский факел")

# 7. «Прорыв» (Ясенево): пешка прорывает бумажный обруч
add("chess-proryv-yasenevo", "b_hoop",
    f'<ellipse cx="74" cy="62" rx="24" ry="40" fill="#FFF3C4" {W(3)}/>'
    + f'<ellipse cx="74" cy="62" rx="24" ry="40" fill="none" stroke="{RED}" stroke-width="5"/>'
    + f'<path d="M66 40 L56 30 M80 36 L90 26 M64 86 L54 96 M84 88 L96 96 M60 60 L46 56" fill="none" {W(2.4)}/>'
    + f'<path d="M58 44 L70 54 L60 62 L72 70 L60 80" fill="none" {W(2.2)}/>'
    + G(58, 98, pawn(WHITE, sc=0.85), rot=-10)
    + f'<path d="M14 52 H34 M10 66 H30 M14 80 H34" stroke="#FFFFFF" stroke-width="3.4" stroke-linecap="round"/>'
    + "".join(f'<rect x="{x}" y="{y}" width="7" height="5" fill="#FFF3C4" {W(1.6)} transform="rotate({r} {x} {y})"/>'
              for x, y, r in [(96, 36, 20), (102, 76, -30), (92, 100, 40)]),
    "белая шахматная пешка",
    "с разбега прорывается сквозь бумажный круг-обруч, во все стороны летят клочки")

# 8. Шахматная школа ЗАО: белый конь в шарфе лепит снежную пешку
add("chess-school-zao-ochakovo", "b_snow",
    f'<path d="M-6 100 Q64 90 134 100 V140 H-6Z" fill="#FFFFFF" {W(2.6)}/>'
    + G(42, 106, knight(WHITE, sc=0.78))
    + f'<path d="M30 70 Q42 76 54 70 L54 78 Q42 84 30 78Z" fill="{RED}" {W(2.4)}/>'
    + f'<path d="M50 76 L56 92 L62 90 L56 76Z" fill="{RED}" {W(2.2)}/>'
    + G(90, 106, pawn("#FFFFFF", sc=0.72))
    + f'<path d="M90 64 L104 60 L90 68Z" fill="{ORG}" {W(1.8)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#FFFFFF" {W(1.2)}/>' for x, y in [(24, 24), (60, 18), (104, 26), (78, 40), (20, 50)]),
    "белый шахматный конь в красном шарфе",
    "лепит во дворе снеговика в форме пешки с морковкой, идёт снег")

# ============================== МЯЧИ ==============================
# 9. «Росток»: мальчик меряет рост у стойки кольца
add("rostok-basket-strogino", "b_grow",
    f'<rect x="84" y="20" width="10" height="110" fill="#8A8FA8" {W(2.6)}/>'
    + "".join(f'<path d="M84 {y} H{78 if i % 2 else 74}" {W(2.4)}/>' for i, y in enumerate(range(40, 120, 10)))
    + hoop(62, 30, w=30, board=False)
    + f'<path d="M77 30 H84" {W(3)}/>'
    + f'<path d="M30 130 Q30 96 50 92 Q70 96 70 130Z" fill="#2F9E6E" {W(3)}/>'
    + head(50, 78, "#3A2A20", r=13)
    + f'<path d="M50 62 H82" stroke="{RED}" stroke-width="3" stroke-dasharray="4 3"/>'
    + ball(38, 110, 11, fc=False)
    + f'<path d="M30 54 q4 -10 10 -14 M28 44 q2 -6 6 -8" fill="none" stroke="#2F9E6E" stroke-width="3" stroke-linecap="round"/>',
    "мальчик-подросток в зелёной майке с мячом под мышкой",
    "встал к стойке баскетбольного кольца с делениями и меряет, насколько вырос")

# 10. «Ника»: крылатая девочка в тунике подаёт волейбольный мяч
add("nika-volley-kuzminki", "b_nike",
    f'<path d="M50 70 Q20 54 14 30 Q30 40 40 38 Q30 52 52 62Z" fill="#FFFFFF" {W(2.8)}/>'
    + f'<path d="M78 70 Q108 54 114 30 Q98 40 88 38 Q98 52 76 62Z" fill="#FFFFFF" {W(2.8)}/>'
    + f'<path d="M46 126 L54 70 H74 L82 126Z" fill="#FFFFFF" {W(3)}/>'
    + f'<path d="M54 82 H74" stroke="{GOLD}" stroke-width="4"/>'
    + limb("M72 74 Q84 60 88 46", SKIN, 6) + limb("M56 76 Q48 86 50 96", SKIN, 6)
    + head(64, 58, "#C98B4E", r=13)
    + f'<path d="M52 50 Q64 40 76 50" fill="none" stroke="#7CC36A" stroke-width="4"/>'
    + volley(92, 30, 13),
    "крылатая девочка-Ника в белой тунике с лавровым венком",
    "в прыжке подаёт волейбольный мяч, раскрыв белые крылья")

# 11. ЦСО «Олимп»: пеликан-либеро ловит мяч в клюв
add("olimp-volley-udaltsova", "b_pelican",
    f'<path d="M-6 116 H134" stroke="#F3D79B" stroke-width="20"/>'
    + f'<path d="M40 112 Q30 84 48 70 Q66 62 76 78 Q80 98 64 112Z" fill="#FFFFFF" {W(3)}/>'
    + f'<path d="M50 112 V122 M62 112 V122" stroke="#F2A93B" stroke-width="4" stroke-linecap="round"/>'
    + f'<path d="M60 76 Q62 54 58 44" fill="none" stroke="{O}" stroke-width="11" stroke-linecap="round"/>'
    + f'<path d="M60 76 Q62 54 58 44" fill="none" stroke="#FFFFFF" stroke-width="7" stroke-linecap="round"/>'
    + f'<circle cx="56" cy="38" r="12" fill="#FFFFFF" {W(3)}/>'
    + f'<path d="M64 36 L108 42 L98 48 Q84 66 70 52 L64 44Z" fill="#FFB347" {W(2.8)}/>'
    + eye(53, 35, 0.75)
    + volley(88, 50, 10, k=0.3)
    + f'<path d="M40 82 Q30 90 34 100" fill="none" {W(2.4)}/>',
    "белый пеликан-либеро на песке",
    "ловит волейбольный мяч в свой огромный оранжевый клюв-мешок")

# ============================== НАСТОЛЬНЫЙ ТЕННИС ==============================
# 12. РусТТ: робот-пушка стреляет оранжевыми шариками
add("rustt-voykovskaya", "b_robot",
    f'<path d="M-6 104 H134 V140 H-6Z" fill="#2F7DBF" {W(2.6)}/><path d="M64 104 V140" stroke="#FFFFFF" stroke-width="3"/>'
    + f'<path d="M30 60 Q30 40 50 40 Q70 40 70 60 L66 92 H34Z" fill="#DADFF0" {W(3)}/>'
    + f'<rect x="28" y="92" width="44" height="12" rx="4" fill="#9AA3C2" {W(2.6)}/>'
    + f'<path d="M66 56 L92 48 L94 62 L68 68Z" fill="#9AA3C2" {W(2.6)}/>'
    + f'<rect x="40" y="52" width="20" height="14" rx="5" fill="#2F2A44" {W(2)}/>'
    + f'<circle cx="46" cy="59" r="2.6" fill="#7DF0FF"/><circle cx="55" cy="59" r="2.6" fill="#7DF0FF"/>'
    + f'<path d="M50 40 V30" {W(2.4)}/><circle cx="50" cy="28" r="3.6" fill="{RED}" {W(1.8)}/>'
    + f'<path d="M36 46 Q50 40 64 46" fill="#FFD24A" opacity=".0"/>'
    + ttball(100, 50) + ttball(110, 64, 4.5) + ttball(104, 80, 4)
    + f'<path d="M94 55 q4 -2 6 -5" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"/>'
    + f'<ellipse cx="40" cy="76" rx="4" ry="2.4" fill="{PINK}" opacity=".7"/><ellipse cx="60" cy="76" rx="4" ry="2.4" fill="{PINK}" opacity=".7"/>'
    + f'<path d="M44 80 Q50 84 56 80" fill="none" {W(2.2)}/>',
    "серебристый робот-пушка для настольного тенниса",
    "стоит у края синего стола и очередью выстреливает оранжевые шарики")

# 13. Ховрино: тигрёнок отбивает шарик через сетку стола
add("tt-khovrino-festivalnaya", "b_tiger",
    f'<path d="M-6 96 H134 L124 110 H4Z" fill="#2E9E62" {W(2.6)}/>'
    + f'<path d="M64 80 V96" {W(2.6)}/><rect x="60" y="80" width="8" height="16" fill="#FFFFFF" fill-opacity=".7" {W(1.6)}/>'
    + f'<path d="M16 110 V128 M112 110 V128" {W(4)}/>'
    + f'<circle cx="34" cy="62" r="20" fill="#F7A440" {W(3)}/>'
    + f'<path d="M18 50 L16 38 L28 44Z M50 50 L52 38 L40 44Z" fill="#F7A440" {W(2.4)}/>'
    + f'<path d="M24 48 l4 6 M34 44 v7 M44 48 l-4 6" fill="none" {W(2.4)}/>'
    + f'<ellipse cx="34" cy="70" rx="10" ry="7" fill="#FFF3E0" {W(2)}/>'
    + face(34, 63, d=7, k=0.6)
    + paddle(64, 50, rot=40, c=RED, sc=0.9)
    + limb("M50 66 Q56 62 58 58", "#F7A440", 6)
    + ttball(96, 60) + f'<path d="M74 56 Q86 50 92 58" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-dasharray="3 3"/>',
    "полосатый тигрёнок",
    "выглядывает из-за зелёного теннисного стола и отбивает шарик через сетку ракеткой")

# 14. «Интеграл»: малыш встал на скамеечку, чтобы достать до стола
add("tt-integral-barklaya", "b_bench",
    f'<path d="M50 84 H134 V94 H50Z" fill="#3A73C8" {W(2.6)}/>'
    + f'<path d="M120 94 V128" {W(4)}/>'
    + f'<rect x="20" y="108" width="40" height="8" rx="2" fill="#E8A65A" {W(2.4)}/><path d="M26 116 V128 M54 116 V128" {W(3.6)}/>'
    + f'<path d="M30 108 Q30 84 40 80 Q50 84 50 108Z" fill="#FF8FB5" {W(3)}/>'
    + head(40, 68, "#E0B04A", r=12)
    + limb("M48 88 Q56 84 60 76", SKIN, 5)
    + paddle(64, 70, rot=30, c="#2D2D3A", sc=0.7)
    + ttball(96, 70, 5, "#FFFFFF")
    + f'<path d="M74 70 Q84 62 90 68" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-dasharray="3 3"/>'
    + sparkle(100, 32, 6),
    "малышка лет четырёх в розовой футболке",
    "встала на деревянную скамеечку, чтобы дотянуться до стола, и отбивает белый шарик")

# ============================== СТРЕЛЬБА ИЗ ЛУКА ==============================
# 15. Крылатское: девочка-лучница на зелёном холме
add("archery-school-krylatskoe", "b_hill",
    f'<path d="M-6 104 Q40 84 80 98 Q110 108 134 96 V140 H-6Z" fill="#6DBB55" {W(2.6)}/>'
    + f'<path d="M30 128 L36 92 H56 L62 128Z" fill="#3F7FD0" {W(3)}/>'
    + head(46, 78, "#2A2A2A", r=12, style="tail")
    + limb("M54 96 Q70 92 82 90", SKIN, 5) + limb("M40 96 Q48 92 60 90", SKIN, 5)
    + f'<path d="M84 54 Q100 90 84 126" fill="none" stroke="#9A5B2E" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M84 54 L62 90 L84 126" fill="none" stroke="{O}" stroke-width="1.6"/>'
    + f'<path d="M60 90 H118" {W(2.4)}/><path d="M112 85 L122 90 L112 95Z" fill="#B0B5C8" {W(1.8)}/>'
    + f'<path d="M60 90 l-6 -5 M60 90 l-6 5" stroke="{RED}" stroke-width="3" stroke-linecap="round"/>'
    + f'<circle cx="108" cy="30" r="9" fill="#FFE27A" {W(2.2)}/>',
    "девочка-лучница с чёрным хвостиком в синем",
    "натягивает деревянный лук на вершине зелёного холма, стрела нацелена вдаль")

# 16. «Айвенго»: рыцарь-малыш с арбалетом
add("aivengo-crossbow-lublino", "b_knight",
    f'<path d="M34 128 Q36 92 60 88 Q84 92 86 128Z" fill="#5A6BC8" {W(3)}/>'
    + f'<path d="M50 96 L60 110 L70 96" fill="none" stroke="{GOLD}" stroke-width="3"/>'
    + f'<path d="M40 72 Q40 40 60 40 Q80 40 80 72 Q80 84 60 84 Q40 84 40 72Z" fill="#C9CEDF" {W(3)}/>'
    + f'<path d="M44 64 H76" stroke="{O}" stroke-width="4"/>'
    + f'<path d="M50 64 V70 M58 64 V72 M66 64 V72 M72 64 V70" {W(1.8)}/>'
    + f'<circle cx="52" cy="57" r="2.6" fill="{O}"/><circle cx="68" cy="57" r="2.6" fill="{O}"/>'
    + f'<path d="M60 40 Q66 22 82 20 Q72 30 74 40" fill="{RED}" {W(2.4)}/>'
    + f'<path d="M66 96 H112" stroke="#8A5A32" stroke-width="7" stroke-linecap="round"/><path d="M66 96 H112" {W(1.4)}/>'
    + f'<path d="M100 78 Q90 96 100 114" fill="none" stroke="#5B4A3A" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M100 78 L112 96 L100 114" fill="none" stroke="{O}" stroke-width="1.4"/>'
    + limb("M74 104 Q80 100 86 98", "#C9CEDF", 6),
    "маленький рыцарь в стальном шлеме с забралом и красным плюмажем",
    "держит наготове деревянный арбалет, словно в турнире Айвенго")

# 17. Shooting Academy: довольное яблоко со стрелой на пеньке
add("shooting-academy-solntsevo", "b_apple",
    f'<path d="M34 128 L40 96 H88 L94 128Z" fill="#B07A4A" {W(3)}/>'
    + f'<ellipse cx="64" cy="96" rx="24" ry="6" fill="#D9A574" {W(2.6)}/>'
    + f'<path d="M64 52 Q40 40 34 62 Q30 88 64 92 Q98 88 94 62 Q88 40 64 52Z" fill="#E8453C" {W(3)}/>'
    + f'<path d="M64 52 Q62 40 66 34" fill="none" {W(3)}/><path d="M66 40 Q78 32 84 40 Q74 46 66 40Z" fill="#7CC36A" {W(2.2)}/>'
    + face(64, 70, d=10, k=0.7)
    + f'<path d="M6 54 L58 62" {W(2.6)}/><path d="M90 66 L112 70" {W(2.6)}/>'
    + f'<path d="M108 64 L120 71 L106 76Z" fill="#B0B5C8" {W(1.8)}/>'
    + f'<path d="M8 54 l-6 -6 M8 54 l-6 6 M14 55 l-6 -6 M14 55 l-6 6" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>'
    + sparkle(100, 28, 6),
    "румяное красное яблоко на пеньке",
    "довольно улыбается: точно в него, насквозь, попала стрела — меткий выстрел")

# ============================== ПРОЧИЙ СПОРТ ==============================
# 18. СК «Борисово»: девочка-каноистка гребёт однолопастным веслом
add("sk-borisovo-rowing", "b_canoe",
    f'<path d="M-6 92 Q30 86 64 92 Q98 98 134 92 V140 H-6Z" fill="#3FA6D0" {W(2.6)}/>'
    + f'<path d="M12 86 Q64 102 116 84 Q110 98 64 104 Q22 100 12 86Z" fill="#F25C3C" {W(3)}/>'
    + f'<path d="M50 88 Q48 66 60 62 Q72 66 70 90Z" fill="#FFD24A" {W(3)}/>'
    + head(60, 50, "#6A3A1E", r=12)
    + f'<path d="M90 36 L72 112" stroke="#9A6A3E" stroke-width="4.5" stroke-linecap="round"/>'
    + f'<path d="M66 104 Q70 122 76 122 Q80 116 78 108Z" fill="#9A6A3E" {W(2.4)}/>'
    + f'<path d="M88 34 h6" stroke="{O}" stroke-width="6" stroke-linecap="round"/>'
    + limb("M68 72 Q80 60 88 50", SKIN, 5) + limb("M56 74 Q66 84 78 82", SKIN, 5)
    + f'<path d="M84 116 q6 -4 12 0 M96 112 q6 -4 12 0" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>',
    "девочка-каноистка в жёлтом жилете",
    "стоя на колене в красном каноэ, гребёт однолопастным веслом по пруду")

# 19. In Motion: маска фехтовальщика делает сальто с рапирой
add("inmotion-fencing-nagorny", "b_flip",
    f'<path d="M24 98 Q20 50 64 34 Q108 50 104 98" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-dasharray="5 5"/>'
    + G(64, 64, f'<path d="M-24 -10 Q-24 -30 0 -30 Q24 -30 24 -10 V14 Q24 30 0 30 Q-24 30 -24 14Z" fill="#E9ECF5" {W(3)}/>'
                f'<rect x="-17" y="-20" width="34" height="32" rx="9" fill="#3A3550" {W(2.4)}/>'
                + "".join(f'<path d="M{x} -18 V10" stroke="#6E6A88" stroke-width="1.4"/>' for x in range(-12, 14, 5))
                + "".join(f'<path d="M-15 {y} H15" stroke="#6E6A88" stroke-width="1.4"/>' for y in range(-14, 12, 5))
                + f'<circle cx="-7" cy="-4" r="3.4" fill="#FFFFFF"/><circle cx="7" cy="-4" r="3.4" fill="#FFFFFF"/>'
                f'<path d="M-6 6 Q0 10 6 6" fill="none" stroke="#FFFFFF" stroke-width="2.2"/>'
                f'<path d="M-24 22 Q0 38 24 22 L24 30 Q0 44 -24 30Z" fill="#FFFFFF" {W(2.4)}/>', rot=150)
    + f'<path d="M84 40 L118 14" stroke="#C9CEDF" stroke-width="3" stroke-linecap="round"/><path d="M84 40 L118 14" {W(1)}/>'
    + f'<ellipse cx="82" cy="42" rx="6" ry="4" fill="{GOLD}" {W(2)} transform="rotate(-36 82 42)"/>'
    + f'<path d="M14 112 H114" stroke="#7A4FA0" stroke-width="8" stroke-linecap="round"/>'
    + sparkle(22, 30, 5) + sparkle(108, 96, 4),
    "белая сетчатая маска фехтовальщика",
    "крутит сальто вверх ногами над гимнастической дорожкой, не выпуская рапиру")

# 20. СК «Чертаново»: теннисный мяч в шапочке прыгает в бассейн
add("sk-chertanovo-806", "b_dive",
    f'<path d="M-6 96 Q32 90 64 96 Q96 102 134 96 V140 H-6Z" fill="#4BB8EE" {W(2.6)}/>'
    + f'<path d="M-6 56 H40 V66 H-6Z" fill="#F4F1EA" {W(2.6)}/><path d="M8 66 V96 M30 66 V96" {W(3.4)}/>'
    + f'<circle cx="74" cy="56" r="18" fill="#D7F25A" {W(3)}/>'
    + f'<path d="M58 48 Q74 58 90 48 M58 66 Q74 56 90 66" fill="none" stroke="#FFFFFF" stroke-width="2.6"/>'
    + f'<path d="M57 50 Q58 34 74 34 Q90 34 91 50 Q74 44 57 50Z" fill="{RED}" {W(2.6)}/>'
    + face(74, 58, d=6, k=0.55)
    + f'<path d="M42 50 Q52 36 58 42" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" stroke-dasharray="4 4"/>'
    + f'<path d="M86 104 Q96 92 104 104 M96 98 v-8" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>',
    "жёлтый теннисный мяч в красной плавательной шапочке",
    "соскочил с бортика и летит рыбкой в бассейн — спорткомплекс, где и теннис, и плавание")

# 21. МФЛ «Братеево»: футбольный мяч бежит эстафету с палочкой
add("mfl-brateevo-football", "b_relay",
    f'<path d="M-6 104 H134 V140 H-6Z" fill="#D9603C" {W(2.6)}/>'
    + f'<path d="M-6 118 H134" stroke="#FFFFFF" stroke-width="2.6"/>'
    + soccer(62, 66, 26)
    + limb("M52 90 Q44 98 36 104", "#FFFFFF", 6) + limb("M72 90 Q82 96 88 104", "#FFFFFF", 6)
    + f'<path d="M30 104 h10 M84 104 h10" stroke="{RED}" stroke-width="7" stroke-linecap="round"/>'
    + limb("M86 62 Q96 56 102 48", "#FFFFFF", 5)
    + f'<rect x="98" y="30" width="8" height="24" rx="3" fill="{GOLD}" {W(2.2)}/>'
    + f'<path d="M10 56 H28 M6 70 H26 M12 84 H28" stroke="#FFFFFF" stroke-width="3.4" stroke-linecap="round"/>',
    "футбольный мяч на тонких ножках в красных бутсах",
    "бежит эстафету по красной беговой дорожке с жёлтой палочкой в руке")

# 22. «Форвард»: мальчик-нападающий с номером 9 ведёт мяч вперёд
add("forvard-football-poryadkovy", "b_nine",
    f'<path d="M-6 108 Q64 100 134 108 V140 H-6Z" fill="#3E9E4E" {W(2.6)}/>'
    + f'<path d="M44 100 Q44 70 60 66 Q78 70 78 100Z" fill="#2E5FBF" {W(3)}/>'
    + f'<text x="61" y="92" font-family="Arial Black, Arial" font-weight="900" font-size="20" text-anchor="middle" fill="#FFFFFF" stroke="{O}" stroke-width="1.2">9</text>'
    + head(62, 52, "#E3B23C", r=13)
    + limb("M54 100 Q48 112 40 116", SKIN, 6) + limb("M70 100 Q80 106 88 104", SKIN, 6)
    + f'<path d="M34 116 h10 M86 104 h8" stroke="#FFFFFF" stroke-width="7" stroke-linecap="round"/>'
    + limb("M46 74 Q34 80 30 72", SKIN, 5) + limb("M78 74 Q88 70 92 62", SKIN, 5)
    + soccer(104, 112, 10, fc=False)
    + f'<path d="M12 70 H28 M8 84 H26 M14 98 H28" stroke="#FFFFFF" stroke-width="3.4" stroke-linecap="round"/>'
    + f'<path d="M96 34 L116 34 M108 26 L116 34 L108 42" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>',
    "мальчик-форвард в синей футболке с номером 9",
    "мчится к воротам, ведя мяч, над ним белая стрелка «вперёд»")

# 23. «Фрунзенский»: малыш-дзюдоист бросает через бедро огромного плюшевого медведя
add("sk-frunzensky-judo", "b_teddy",
    f'<path d="M-6 112 H134 V140 H-6Z" fill="#7FBF6A" {W(2.6)}/><path d="M-6 112 H134" stroke="{RED}" stroke-width="4"/>'
    + G(82, 52, f'<circle cx="0" cy="0" r="22" fill="#B07A4A" {W(3)}/>'
                f'<circle cx="-18" cy="-16" r="8" fill="#B07A4A" {W(2.6)}/><circle cx="18" cy="-16" r="8" fill="#B07A4A" {W(2.6)}/>'
                f'<ellipse cx="0" cy="7" rx="9" ry="7" fill="#E8C9A0" {W(2)}/><circle cx="0" cy="4" r="2.4" fill="{O}"/>'
                f'<circle cx="-8" cy="-4" r="2.6" fill="{O}"/><circle cx="8" cy="-4" r="2.6" fill="{O}"/>'
                f'<path d="M-24 18 Q-40 30 -34 40 M24 18 Q40 26 36 38" fill="none" stroke="#B07A4A" stroke-width="9" stroke-linecap="round"/>', rot=-60)
    + f'<path d="M32 112 L36 80 H58 L62 112Z" fill="#FFFFFF" {W(3)}/>'
    + f'<path d="M36 92 H58" stroke="#F2C230" stroke-width="5"/>'
    + f'<path d="M40 80 L47 92 L54 80" fill="none" {W(2)}/>'
    + head(47, 66, "#3A2A20", r=12)
    + limb("M56 84 Q66 78 72 70", "#FFFFFF", 7) + limb("M38 86 Q30 80 30 72", "#FFFFFF", 7)
    + f'<path d="M100 92 q8 6 4 14" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>',
    "малыш-дзюдоист в белом кимоно с жёлтым поясом",
    "на зелёном татами бросает через бедро огромного плюшевого медведя")

# 24. «Свиблово»: носорожек-борец в синем трико в стойке на ковре
add("sk-sviblovo-borba", "b_rhino",
    f'<ellipse cx="64" cy="114" rx="56" ry="12" fill="#E8453C" {W(2.6)}/><ellipse cx="64" cy="114" rx="30" ry="6" fill="none" stroke="#FFFFFF" stroke-width="2.6"/>'
    + f'<path d="M36 112 Q30 80 44 72 H84 Q98 80 92 112Z" fill="#9AA5B8" {W(3)}/>'
    + f'<path d="M44 74 L48 112 H80 L84 74 Q64 84 44 74Z" fill="#2E5FBF" {W(2.6)}/>'
    + limb("M44 82 Q28 88 26 100", "#9AA5B8", 9) + limb("M84 82 Q100 88 102 100", "#9AA5B8", 9)
    + f'<ellipse cx="64" cy="54" rx="26" ry="20" fill="#9AA5B8" {W(3)}/>'
    + f'<path d="M40 40 L36 30 L46 36Z M88 40 L92 30 L82 36Z" fill="#9AA5B8" {W(2.4)}/>'
    + face(64, 48, d=13, k=0.6, mouth=False)
    + f'<ellipse cx="64" cy="64" rx="15" ry="9" fill="#B6C0D0" {W(2.6)}/>'
    + f'<circle cx="58" cy="64" r="1.8" fill="{O}"/><circle cx="70" cy="64" r="1.8" fill="{O}"/>'
    + f'<path d="M57 58 Q62 30 72 40 Q70 50 70 58Z" fill="#F4F1EA" {W(2.6)}/>'
    + f'<path d="M58 70 Q64 74 70 70" fill="none" {W(2.2)}/>',
    "серый носорожек-борец в синем борцовском трико",
    "встал в борцовскую стойку на красном ковре, широко расставив лапы")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for pid, code in ICONS.items():
        open(os.path.join(OUT, pid + ".svg"), "w").write(code)
    reg = os.path.join(OUT, "subjects.txt")
    lines = [l for l in open(reg, encoding="utf-8") if l.split(" — ", 1)[0] not in SUBJ]
    lines += [line + "\n" for line in SUBJ.values()]
    open(reg, "w", encoding="utf-8").writelines(lines)
    print(len(ICONS), "иконок:", " ".join(ICONS))
