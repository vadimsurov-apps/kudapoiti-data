"""Иконки робота sections, 2026-11-08 (18 UTC) — места из поиска по районам (tools/add_sections_1108f.py).
Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно — свой герой, своя сцена, компоновка и палитра.
Сверено с листами icons-catalog и subjects.txt (уже заняты: лента, булавы, обруч с ребёнком, чешки, помпоны черлидинга,
черкеска, папаха, щелкунчик, орех-балерина, малыш бросает медведя, кимоно с поясами, борцовские куртки, мяч-луна и др.).
Запуск: python3 tools/icons_sections_1108f.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O
from icons_sections_1107c import G
from icons_sections_1108b import limb, head

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
SKIN = "#FFD8B8"
draw_icons.BG.update({
    "f_jet": ("#EAF8FF", "#4FA9E6"), "f_fuchsia": ("#FFF0F8", "#E86FB0"), "f_hoopgold": ("#FFF9E6", "#E9A23B"),
    "f_swallow": ("#E9FFFA", "#3DBFA6"), "f_leo": ("#F8EEFF", "#B07AE6"), "f_roll": ("#F0FFE9", "#8CCB5A"),
    "f_rings": ("#EEF2FF", "#6E83D9"), "f_hand": ("#FFF0EC", "#EF7E66"), "f_pomp": ("#FFF5FB", "#F08DC6"),
    "f_shoes": ("#FFF1EF", "#D9675E"), "f_pad": ("#FFF8E0", "#D8B24A"), "f_belt": ("#FFF6EC", "#F0A257"),
    "f_sensei": ("#F2F5EA", "#9DB077"), "f_bow": ("#EAF6FF", "#7FB1DE"), "f_fall": ("#EDFFF2", "#55B97A"),
    "f_ushanka": ("#E9F1FF", "#5D7FD0"), "f_cross": ("#FFF3E4", "#E59244"), "f_palm": ("#FFFBE3", "#5CC6C0"),
    "f_cape": ("#FFEFEF", "#E35D6A"), "f_wings": ("#F6F0FF", "#9C8BE8"), "f_mouse": ("#FFF2F6", "#D99AB6"),
    "f_waltz": ("#F9F3E8", "#B8956A"), "f_lez": ("#EEF8F0", "#4E9A6E"), "f_mirror": ("#FFFDEB", "#E6CF4E"),
    "f_gum": ("#FFEFFA", "#C46FD8"), "f_star": ("#2E2A5A", "#6A4FB0"), "f_cal": ("#F1FBFF", "#56B2D3"),
    "f_skirt": ("#FFF4E8", "#E77B4E"), "f_steps": ("#F2FFF6", "#79C99B"), "f_abc": ("#FFF7F0", "#E3A27A"),
    "f_leap": ("#EDEBFF", "#4D4FA8"), "f_graf": ("#F3FFE9", "#A1C93B"),
})


def add(pid, bg, body, hero, scene):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def rect(x, y, w, h, c, rx=4, sw=2.8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{c}" {W(sw)}/>'


def circ(x, y, r, c, sw=2.8):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" {W(sw)}/>'


def path(d, c="none", sw=2.8):
    return f'<path d="{d}" fill="{c}" {W(sw)}/>'


def notes(x, y, c=O):
    return (f'<path d="M{x} {y} v-12 l8 -3 v12" fill="none" {W(2.2)}/><ellipse cx="{x-2}" cy="{y}" rx="3" ry="2.4" fill="{c}"/>'
            f'<ellipse cx="{x+6}" cy="{y-3}" rx="3" ry="2.4" fill="{c}"/>')


# ============================== БАССЕЙН ==============================
add("aqua-vnukovo", "f_jet",
    f'<path d="M4 30 Q50 44 124 18" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" opacity=".85"/>'
    + G(108, 20, path("M-12 0 L10 -3 L14 0 L10 3Z", "#fff", 2.2) + path("M0 -1 L-4 -10 L2 -1Z M0 1 L-4 10 L2 1Z", "#fff", 2), -14)
    + path("M-6 70 Q20 62 40 70 T84 70 T134 70 V140 H-6Z", "#3E9FE0", 2.6)
    + rect(30, 76, 52, 12, "#FFD23F", 6)
    + limb("M60 82 L92 90", "#FFD8B8", 6) + limb("M58 84 L96 98", "#FFD8B8", 6)
    + path("M100 88 q8 -2 12 4 M102 98 q8 0 10 6", "none", 2.2)
    + limb("M44 82 L30 74", SKIN, 5)
    + G(48, 68, circ(0, 0, 13, SKIN) + path("M-13 -1 Q-13 -16 0 -16 Q13 -16 13 -1Z", "#FF8A3D", 2.4) + face(0, 3, 5, 0.5)),
    "малыш в оранжевой шапочке на жёлтой плавательной доске",
    "плывёт по бассейну, болтая ногами, а над ним в небе тянется белый след самолёта")

# ============================== ГИМНАСТИКА ==============================
add("chg1-novinsky", "f_fuchsia",
    limb("M10 112 Q40 92 70 74", SKIN, 11)
    + path("M64 70 q10 -6 14 2 q-2 8 -10 8", SKIN, 2.6)
    + circ(52, 56, 26, "#E0287D") + f'<ellipse cx="44" cy="46" rx="9" ry="5" fill="#fff" opacity=".5"/>'
    + face(52, 58, 8, 0.8)
    + sparkle(92, 30, 8) + sparkle(104, 54, 5) + sparkle(22, 30, 5),
    "блестящий мяч цвета фуксии для художественной гимнастики",
    "катится по вытянутой руке гимнастки от плеча к ладони и сверкает")

add("chg1-volzhsky", "f_hoopgold",
    path("M-6 104 H134 V140 H-6Z", "#5B7BD5", 2.4)
    + f'<circle cx="62" cy="64" r="34" fill="none" stroke="{O}" stroke-width="13"/>'
    + f'<circle cx="62" cy="64" r="34" fill="none" stroke="#FFC93C" stroke-width="8"/>'
    + f'<circle cx="62" cy="64" r="34" fill="none" stroke="#FF6FA0" stroke-width="3" stroke-dasharray="6 10"/>'
    + face(62, 64, 8, 0.85)
    + path("M14 92 q-6 0 -8 4 M12 80 q-8 0 -10 4", "none", 2.4)
    + notes(104, 32) + notes(18, 40),
    "золотой гимнастический обруч с розовой обмоткой",
    "катится колесом по синему ковру, а за ним скачут нотки музыки выступления")

add("chg1-profsoyuznaya", "f_swallow",
    path("M-6 100 H134 V140 H-6Z", "#F7E3A6", 2.4)
    + limb("M60 98 L62 72", SKIN, 6)
    + path("M50 54 Q64 46 76 56 L68 74 L54 72Z", "#24B5A6", 2.6)
    + limb("M72 60 L112 42", SKIN, 6)
    + limb("M54 58 L22 52", SKIN, 5)
    + limb("M58 70 L20 76", SKIN, 6)
    + path("M20 52 q-8 -14 4 -22 q10 -6 14 6", "none", 3)
    + head(46, 44, "#3A2A22", r=11, k=0.42) + circ(40, 32, 5, "#3A2A22", 2.2),
    "девочка в бирюзовом купальнике с пучком на макушке",
    "застыла в «ласточке» на одной ноге посреди жёлтого ковра, руки в стороны")

add("chg1-maslova", "f_leo",
    path("M64 14 V26", "none", 3) + path("M40 34 Q64 20 88 34", "none", 3.2)
    + path("M44 34 L52 44 Q64 50 76 44 L84 34 L86 66 Q90 88 80 100 L48 100 Q38 88 42 66Z", "#7B3FC4", 2.8)
    + path("M48 100 L80 100 L76 110 L52 110Z", "#7B3FC4", 2.6)
    + sparkle(56, 62, 4, "#FFE36B") + sparkle(72, 74, 4, "#FFE36B") + sparkle(60, 86, 3.5, "#FFE36B") + sparkle(76, 56, 3, "#FFE36B")
    + face(64, 70, 7, 0.6)
    + sparkle(102, 40, 7) + sparkle(24, 80, 6),
    "фиолетовый гимнастический купальник со стразами на плечиках",
    "висит на вешалке и сияет перед первым выступлением")

add("egc-zum", "f_roll",
    path("M-6 98 H134 V140 H-6Z", "#3D74C9", 2.4)
    + f'<path d="M26 92 Q30 40 64 36 Q98 40 102 92" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="5 7"/>'
    + G(64, 80, circ(0, 0, 16, "#4CBF62") + limb("M-8 -10 Q-18 -24 -6 -26", SKIN, 5) + limb("M8 -10 Q18 -24 6 -26", SKIN, 5)
        + G(0, 10, circ(0, 0, 10, SKIN) + face(0, 1, 4, 0.4)) , 180)
    + path("M14 96 q4 -6 8 0 M106 96 q4 -6 8 0", "none", 2.2),
    "малыш в зелёной футболке, свернувшийся клубочком",
    "делает кувырок вперёд по синему мату, по дуге над ним — пунктир траектории")

add("egc-patriot", "f_rings",
    path("M-6 10 H134", "none", 6) + path("M40 10 L44 66 M88 10 L84 66", "none", 2.6)
    + f'<circle cx="44" cy="80" r="15" fill="none" stroke="{O}" stroke-width="9"/><circle cx="44" cy="80" r="15" fill="none" stroke="#C98A4B" stroke-width="5"/>'
    + f'<circle cx="84" cy="80" r="15" fill="none" stroke="{O}" stroke-width="9"/><circle cx="84" cy="80" r="15" fill="none" stroke="#C98A4B" stroke-width="5"/>'
    + face(44, 80, 5, 0.5) + face(84, 80, 5, 0.5)
    + path("M20 62 q-6 6 0 12 M108 62 q6 6 0 12", "none", 2.4),
    "пара деревянных гимнастических колец с мордочками",
    "раскачиваются на тросах под потолком зала, улыбаясь друг другу")

add("akrobatika-klyuchevaya", "f_hand",
    path("M-6 102 H134 V140 H-6Z", "#F6C84C", 2.4)
    + limb("M54 100 L56 80", SKIN, 6) + limb("M74 100 L72 80", SKIN, 6)
    + rect(52, 52, 24, 30, "#E23B3B", 8)
    + limb("M58 52 L52 22", "#E23B3B", 7) + limb("M70 52 L82 26", "#E23B3B", 7)
    + G(64, 92, circ(0, 0, 11, SKIN) + path("M-11 1 Q-11 12 0 12 Q11 12 11 1 Q4 6 0 6 Q-5 6 -11 1Z", "#5A3A26", 2.2)
        + face(0, -1, 4, 0.4), 180)
    + sparkle(30, 36, 6) + sparkle(100, 40, 5),
    "мальчик в красном трико",
    "стоит на руках на жёлтом мате, ноги разведены «рогаткой» к потолку")

add("cheer-sport-kozikhinsky", "f_pomp",
    "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" {W(2.2)}/>' for x, y, r, c in [
        (38, 58, 24, "#FF5FA2"), (90, 58, 24, "#FFC93C")])
    + "".join(path(f"M{x} {y} l{dx} {dy}", "none", 2) for x, y, dx, dy in [
        (30, 46, -10, -8), (46, 44, 6, -10), (24, 62, -12, 2), (32, 74, -8, 10), (50, 70, 8, 8),
        (84, 44, -6, -10), (100, 46, 10, -8), (106, 60, 12, 0), (98, 74, 8, 10), (80, 72, -8, 8)])
    + face(38, 58, 7, 0.65) + face(90, 58, 7, 0.65)
    + rect(34, 80, 8, 18, "#fff", 3, 2.2) + rect(86, 80, 8, 18, "#fff", 3, 2.2)
    + sparkle(64, 26, 7, "#FFF6B0") + sparkle(64, 100, 6, "#fff") + sparkle(18, 30, 4) + sparkle(112, 98, 4),
    "розовый и золотой пушистые помпоны черлидеров с глазками",
    "трясутся в такт речёвке и сыплют вокруг себя блёстки")

# ============================== ЕДИНОБОРСТВА ==============================
add("sambo-kharlampiev-energetichesky", "f_shoes",
    path("M-6 98 H134 V140 H-6Z", "#3C6BC7", 2.4) + path("M-6 108 H134", "none", 2)
    + path("M18 96 L22 54 Q34 46 46 54 L48 78 Q66 84 64 96Z", "#D8322F", 2.8)
    + path("M64 96 L68 50 Q80 42 92 50 L94 74 Q112 80 110 96Z", "#D8322F", 2.8)
    + path("M24 62 h20 M70 58 h20", "none", 2.2)
    + face(33, 74, 5, 0.55) + face(80, 70, 5, 0.55)
    + path("M30 40 q4 -8 8 0 M76 36 q4 -8 8 0", "none", 2.2),
    "пара красных мягких борцовок-самбовок",
    "подпрыгивают на синем ковре перед схваткой, как будто разминаются")

add("mshbi-aviamotornaya", "f_pad",
    path("M74 20 Q112 18 114 64 Q112 104 74 104 Q60 64 74 20Z", "#E8B44A", 2.8)
    + path("M84 34 Q100 64 84 92", "none", 2.2) + face(94, 60, 6, 0.6)
    + limb("M2 76 L40 66", "#F0C8A8", 12)
    + circ(46, 64, 12, "#2A64C8") + path("M40 56 h10", "none", 2)
    + sparkle(62, 36, 7, "#FFF1A0") + sparkle(60, 92, 6, "#FFF1A0") + sparkle(30, 40, 4),
    "соломенно-жёлтая тренерская лапа для отработки ударов с глазками",
    "принимает удар детского кулачка в синей перчатке, и вокруг вспыхивают звёздочки")

add("karate-club1-arbat", "f_belt",
    path("M10 64 Q64 50 118 64", "none", 1)
    + path("M14 58 Q64 44 114 58 L114 70 Q64 56 14 70Z", "#F28C1E", 2.8)
    + rect(52, 50, 24, 24, "#F28C1E", 6)
    + path("M56 72 L40 108 L52 110 L62 76Z M72 72 L88 108 L76 110 L66 76Z", "#F28C1E", 2.6)
    + path("M82 100 h8 v-6", "none", 2)
    + f'<text x="83" y="106" font-family="Arial" font-weight="bold" font-size="9" fill="{O}">1</text>'
    + face(64, 60, 6, 0.6) + sparkle(28, 32, 6) + sparkle(102, 30, 5),
    "оранжевый пояс каратэ, завязанный тугим узлом",
    "парит в воздухе, свесив два кончика вниз, на одном вышита цифра 1")

add("nastavnik-yankovskogo", "f_sensei",
    path("M-6 104 H134 V140 H-6Z", "#C9B27A", 2.4)
    + path("M22 104 L28 62 Q42 52 56 62 L62 104Z", "#fff", 2.8) + path("M30 82 H54", "none", 4)
    + f'<path d="M30 82 H54" stroke="#222" stroke-width="3"/>'
    + G(42, 44, circ(0, 0, 14, SKIN) + path("M-10 4 Q-14 14 -4 12 M10 4 Q14 14 4 12", "#eee", 2) + path("M-12 -6 Q0 -18 12 -6", "#EDEDED", 2.2)
        + eye(-5, -1, 0.5) + eye(5, -1, 0.5))
    + limb("M56 70 L70 50", SKIN, 5) + path("M70 48 v-8", "none", 3)
    + path("M82 104 L86 82 Q94 76 102 82 L106 104Z", "#fff", 2.6) + f'<path d="M86 94 H102" stroke="#2F6FD0" stroke-width="3"/>'
    + head(94, 70, "#3A2A22", r=9, k=0.34),
    "седой сенсей с белыми усами и бородкой",
    "поднял указательный палец, объясняя приём маленькому ученику на татами")

add("alfa-budo-lyublinskaya", "f_bow",
    path("M-6 96 H134 V140 H-6Z", "#8CC56A", 2.4) + path("M30 96 H98", "none", 2) + path("M64 96 V140", "none", 2)
    + limb("M50 94 L52 70", "#fff", 9) + limb("M68 94 L66 70", "#fff", 9)
    + path("M44 72 L78 72 L92 40 L66 30Z", "#fff", 2.8)
    + f'<path d="M48 72 L82 62" stroke="#2F6FD0" stroke-width="4"/>'
    + G(98, 44, circ(0, 0, 12, SKIN) + path("M-12 -2 Q-12 -14 0 -14 Q12 -14 12 -2Z", "#4A3020", 2.2) + path("M-5 3 q2 2 4 0 M3 3 q2 2 4 0", "none", 1.8))
    + sparkle(24, 40, 6) + sparkle(110, 18, 4),
    "ученик в белом кимоно с синим поясом",
    "склонился в поклоне-рэй у края зелёного татами, закрыв глаза")

add("ippon-vnukovo", "f_fall",
    path("M-6 94 H134 V140 H-6Z", "#2E9E58", 2.4)
    + path("M30 92 Q64 84 98 92", "none", 2)
    + G(64, 76, path("M-30 6 Q-28 -10 -8 -12 L22 -8 Q34 -4 32 8Z", "#2F5FD0", 2.8)
        + limb("M-24 2 L-42 -14", SKIN, 5) + limb("M-30 8 L-46 10", "#2F5FD0", 7)
        + limb("M26 2 L44 -12", "#2F5FD0", 7) + limb("M30 6 L50 4", "#2F5FD0", 7)
        + G(-2, -24, circ(0, 0, 12, SKIN) + path("M-12 -2 Q-10 -14 2 -14 Q12 -12 12 -2Z", "#7A4A2E", 2.2)
            + path("M10 -6 q12 -2 14 8", "none", 4) + face(0, 1, 4, 0.4)), -8)
    + "".join(circ(x, y, r, "#E8F6EA", 1.8) for x, y, r in [(18, 88, 5), (26, 82, 3), (108, 86, 5), (100, 80, 3)]),
    "девочка-дзюдоистка в синем кимоно с рыжей косичкой",
    "мягко падает на бок на зелёное татами, страхуясь рукой, и поднимает облачко")

# ============================== ИГРОВЫЕ ВИДЫ И ОБЩИЙ СПОРТ ==============================
add("nevsky-bears-mira", "f_ushanka",
    path("M-6 60 H134", "none", 3)
    + "".join(path(f"M{x} 60 V84", "none", 1.6) for x in range(4, 128, 12)) + path("M-6 84 H134", "none", 3)
    + circ(64, 46, 22, "#FFD23F")
    + path("M44 40 Q64 26 84 40 M48 58 Q64 48 80 58", "none", 2.4)
    + f'<path d="M50 30 Q60 46 52 64" fill="none" stroke="#2F5FD0" stroke-width="5"/>'
    + path("M40 34 Q42 10 64 10 Q86 10 88 34 Q64 26 40 34Z", "#7A5232", 2.6)
    + path("M40 34 Q30 40 34 54 Q40 52 44 40Z M88 34 Q98 40 94 54 Q88 52 84 40Z", "#7A5232", 2.4)
    + face(64, 50, 7, 0.6) + path("M36 98 q4 -8 8 0 M84 98 q4 -8 8 0", "none", 2.2),
    "сине-жёлтый волейбольный мяч в меховой шапке-ушанке",
    "сидит верхом на натянутой волейбольной сетке, как на заборе")

add("husky-basket-novgorodskaya", "f_cross",
    path("M-6 104 H134 V140 H-6Z", "#E0A462", 2.4) + path("M-6 118 H134", "none", 1.6)
    + limb("M58 74 L44 102", "#2F5FD0", 7) + limb("M70 74 L88 100", "#2F5FD0", 7)
    + rect(50, 46, 28, 32, "#30A64A", 6)
    + f'<text x="58" y="70" font-family="Arial" font-weight="bold" font-size="14" fill="#fff">5</text>'
    + limb("M54 52 L40 84", SKIN, 5) + limb("M76 52 L88 76", SKIN, 5)
    + circ(64, 98, 9, "#F28C38", 2.4) + path("M55 98 H73 M64 89 V107", "none", 1.6)
    + head(64, 34, "#2B1A12", r=11, k=0.42)
    + path("M40 86 q8 10 18 10 M70 98 q10 0 18 -12", "none", 1.8),
    "мальчик в зелёной майке с номером 5",
    "ведёт баскетбольный мяч между ног низко над деревянным паркетом")

add("fiji-kids-foriver", "f_palm",
    path("M-6 98 Q64 80 134 98 V140 H-6Z", "#F7DE8A", 2.4) + path("M-6 112 Q64 100 134 112 V140 H-6Z", "#5CC6E0", 2.2)
    + path("M92 92 Q96 60 88 34", "none", 6) + f'<path d="M92 92 Q96 60 88 34" fill="none" stroke="#B57A3E" stroke-width="3"/>'
    + path("M88 34 Q70 22 58 34 Q74 30 88 34 Q100 18 116 26 Q100 28 88 34 Q106 36 112 50 Q98 40 88 34Z", "#3DAA5A", 2.4)
    + G(42, 72, rect(-20, -9, 8, 18, "#8E7CE0", 3, 2.4) + rect(12, -9, 8, 18, "#8E7CE0", 3, 2.4) + rect(-12, -4, 24, 8, "#BFB4F2", 3, 2.4)
        + face(0, 0, 5, 0.45, blush=False)
        + limb("M-16 9 L-14 21", SKIN, 4) + limb("M16 9 L14 21", SKIN, 4)
        + path("M-16 -9 L-24 -21 M16 -9 L24 -21", "none", 3), sc=1.6)
    + sparkle(18, 30, 5),
    "сиреневая детская гантелька с глазками",
    "делает зарядку на песчаном островке под пальмой, поднимая ручки вверх")

add("obekt-geroi-nikitsky", "f_cape",
    path("M-6 100 H134 V140 H-6Z", "#9FD07A", 2.4)
    + rect(86, 74, 30, 8, "#FFC93C", 3) + rect(92, 82, 4, 18, "#FFC93C", 2, 2) + rect(106, 82, 4, 18, "#FFC93C", 2, 2)
    + path("M40 52 Q10 50 4 74 Q20 70 26 80 Q30 64 44 64Z", "#E23B3B", 2.6)
    + rect(40, 50, 22, 26, "#2F6FD0", 7)
    + f'<path d="M51 57 l3 5 l5 1 l-4 3 l1 5 l-5 -3 l-5 3 l1 -5 l-4 -3 l5 -1Z" fill="#FFC93C"/>'
    + limb("M44 76 L34 98", SKIN, 6) + limb("M58 76 L74 92", SKIN, 6)
    + limb("M60 56 L80 44", SKIN, 5) + limb("M42 58 L30 68", SKIN, 5)
    + head(52, 38, "#E2B65A", r=11, k=0.42)
    + path("M8 90 h10 M2 82 h8", "none", 2.2),
    "малыш в синей футболке со звездой и красном плаще",
    "мчится к полосе препятствий, плащ развевается за спиной")

# ============================== ТАНЦЫ И БАЛЕТ ==============================
add("wings-dance-kabelnaya", "f_wings",
    f'<path d="M64 -6 L30 120 H98Z" fill="#fff" opacity=".35"/>'
    + path("M56 56 Q20 26 18 60 Q24 80 56 66Z", "#9CD6FF", 2.4) + path("M72 56 Q108 26 110 60 Q104 80 72 66Z", "#9CD6FF", 2.4)
    + path("M56 70 Q34 84 40 96 Q54 92 58 74Z", "#C7B6FF", 2.2) + path("M72 70 Q94 84 88 96 Q74 92 70 74Z", "#C7B6FF", 2.2)
    + rect(56, 52, 16, 24, "#FFB3D1", 6)
    + limb("M60 76 L58 108", SKIN, 5) + limb("M68 76 L74 104", SKIN, 5)
    + limb("M58 56 L46 30", SKIN, 4) + limb("M70 56 L80 30", SKIN, 4)
    + head(64, 40, "#B5652E", r=10, k=0.38) + sparkle(28, 22, 5) + sparkle(102, 100, 5),
    "девочка-танцовщица с прозрачными крыльями бабочки",
    "кружится на цыпочках в луче прожектора, подняв руки над головой")

add("nutcracker-ballet-serp-molot", "f_mouse",
    rect(-6, 50, 140, 6, "#C98A4B", 3) + rect(14, 56, 6, 60, "#C98A4B", 2) + rect(108, 56, 6, 60, "#C98A4B", 2)
    + path("M-6 108 H134 V140 H-6Z", "#B98ACB", 2.2)
    + path("M44 80 Q64 64 84 80 Q64 90 44 80Z", "#FF9CC6", 2.6)
    + circ(64, 66, 14, "#A9A9B8") + circ(52, 50, 7, "#A9A9B8", 2.4) + circ(76, 50, 7, "#A9A9B8", 2.4)
    + circ(52, 50, 3.5, "#FFB3CC", 0) + circ(76, 50, 3.5, "#FFB3CC", 0)
    + face(64, 66, 5, 0.5) + circ(64, 72, 2, "#FF7FA8", 1.4)
    + limb("M56 84 L48 104", "#A9A9B8", 4) + limb("M72 84 L80 104", "#A9A9B8", 4)
    + limb("M54 62 L36 54", "#A9A9B8", 4) + path("M84 88 Q104 92 100 74", "none", 2),
    "серая мышка-балерина в розовой пачке",
    "делает плие у деревянного балетного станка, держась лапкой за перекладину")

add("tanc-masterskaya-masterkova", "f_waltz",
    path("M-6 96 H134 V140 H-6Z", "#D6A36A", 2.2) + path("M20 96 L4 140 M52 96 L44 140 M84 96 L88 140 M114 96 L128 140", "none", 1.6)
    + G(44, 76, path("M-20 8 Q-22 -6 -8 -8 L14 -8 Q20 -4 18 8Z", "#2E2E3A", 2.6) + path("M14 -8 L18 -16 L22 -8Z", "#2E2E3A", 2) + face(0, -1, 6, 0.5, mouth=False), -12)
    + G(86, 70, path("M-18 8 Q-20 -6 -6 -10 L10 -8 Q16 -4 16 8Z", "#F2C14E", 2.6) + path("M14 0 L20 22 L24 22 L20 -2Z", "#F2C14E", 2.2) + face(-2, -1, 6, 0.5, mouth=False), 14)
    + notes(26, 40) + notes(98, 30) + path("M30 92 q6 -4 12 0 M76 90 q6 -4 12 0", "none", 1.8),
    "чёрная лакированная туфля партнёра и золотая туфелька партнёрши",
    "кружатся в вальсе по паркету, оставляя за собой следы-нотки")

add("lezginka-allon-masterkova", "f_lez",
    path("M-6 106 H134 V140 H-6Z", "#C9D9A0", 2.2)
    + limb("M56 86 L54 106", "#2E2E3A", 6) + limb("M70 86 L74 106", "#2E2E3A", 6)
    + path("M50 50 L78 50 L84 96 L44 96Z", "#3A3A4A", 2.8)
    + "".join(rect(x, 56, 3, 9, "#F2E4B0", 1, 1.4) for x in (52, 56, 70, 74))
    + limb("M52 54 L18 46", "#3A3A4A", 7) + limb("M76 54 L110 40", "#3A3A4A", 7)
    + head(64, 38, "#2B1A12", r=10, k=0.38)
    + path("M52 34 Q50 18 64 18 Q78 18 76 34 Q64 30 52 34Z", "#4A4A4A", 2.4)
    + path("M44 112 l6 -6 M84 112 l-6 -6", "none", 2) + sparkle(22, 24, 5) + sparkle(108, 92, 5),
    "мальчик в тёмной национальной рубахе с газырями",
    "танцует лезгинку на носочках, раскинув руки — одну выше другой")

add("duos-dance-kedrova", "f_mirror",
    rect(70, 14, 50, 96, "#DDF3FF", 4, 2.8) + f'<path d="M80 24 L100 22 M84 36 L108 30" stroke="#fff" stroke-width="3"/>'
    + G(40, 0, limb("M0 66 L-6 94", SKIN, 5) + limb("M6 66 L18 90", SKIN, 5)
        + rect(-8, 44, 18, 24, "#FF6F61", 6) + limb("M-6 48 L-18 30", SKIN, 4) + limb("M8 48 L18 60", SKIN, 4)
        + head(0, 32, "#5A3A26", r=10, k=0.38) + circ(-12, 24, 4, "#5A3A26", 2) + circ(12, 24, 4, "#5A3A26", 2)
        + rect(-12, 92, 10, 6, "#FFD23F", 3, 2) + rect(14, 88, 10, 6, "#FFD23F", 3, 2))
    + G(96, 0, '<g opacity=".55">' + limb("M0 66 L6 94", SKIN, 5) + limb("M-6 66 L-18 90", SKIN, 5)
        + rect(-10, 44, 18, 24, "#FF6F61", 6) + limb("M6 48 L18 30", SKIN, 4) + head(0, 32, "#5A3A26", r=10, k=0.38) + '</g>'),
    "девочка с двумя хвостиками в жёлтых кроссовках",
    "танцует денс-микс перед большим зеркалом зала, и отражение повторяет движения")

add("gumbeat-dance-kedrova", "f_gum",
    path("M-6 108 H134 V140 H-6Z", "#9D5BC8", 2.2)
    + limb("M58 84 L50 108", "#3A66C8", 6) + limb("M70 84 L80 106", "#3A66C8", 6)
    + rect(52, 62, 24, 26, "#FFD23F", 7)
    + limb("M54 66 L36 78", SKIN, 4) + limb("M74 66 L92 56", SKIN, 4)
    + head(64, 50, "#E2B65A", r=11, k=0.4)
    + path("M50 48 Q50 30 64 30 Q78 30 78 48", "none", 3) + rect(46, 44, 8, 12, "#FF5FA2", 4, 2.2) + rect(74, 44, 8, 12, "#FF5FA2", 4, 2.2)
    + circ(72, 60, 9, "#FF9CD6", 2.2)
    + notes(24, 34, "#fff") + notes(100, 30, "#fff"),
    "малыш в огромных розовых наушниках",
    "пританцовывает под бит и надувает пузырь из жвачки")

add("goldstar-malomoskovskaya", "f_star",
    sparkle(20, 24, 4) + sparkle(110, 20, 5) + sparkle(104, 108, 4) + sparkle(16, 100, 3)
    + G(62, 54, path("M0 -30 L9 -10 L30 -8 L14 6 L19 28 L0 16 L-19 28 L-14 6 L-30 -8 L-9 -10Z", "#FFC93C", 2.8) + face(0, 0, 6, 0.6), -10)
    + path("M48 74 Q30 92 22 110 Q50 100 64 112 Q78 98 104 106 Q92 88 76 74Z", "#E8406A", 2.6)
    + path("M30 104 q6 -6 10 2 M56 106 q6 -6 10 2 M80 102 q6 -6 10 2", "none", 1.8),
    "золотая звезда в пышной алой бальной юбке",
    "кружится в латиноамериканском танце на ночной сцене, юбка взлетает волной")

add("sreda-dance-klyuchevaya", "f_cal",
    rect(36, 22, 56, 66, "#fff", 6) + rect(36, 22, 56, 16, "#E8554A", 6)
    + "".join(circ(x, 22, 3, "#ccc", 2) for x in (50, 78))
    + f'<text x="49" y="72" font-family="Arial" font-weight="bold" font-size="22" fill="{O}">СР</text>'
    + face(64, 48, 8, 0.55, mouth=False) + path("M60 54 q4 3 8 0", "none", 2)
    + limb("M54 88 L44 108", "#3A3A55", 4) + limb("M74 88 L88 104", "#3A3A55", 4)
    + path("M38 110 h12 l2 -4 M84 104 l10 2 l1 -5", "#2E2E3A", 2.4)
    + limb("M36 50 L18 40", "#3A3A55", 3.5) + limb("M92 50 L110 62", "#3A3A55", 3.5)
    + path("M26 116 l-4 4 M100 112 l4 4", "none", 2) + notes(110, 34),
    "листок календаря «СР» на тонких ножках",
    "отбивает чечётку каблучками, раскинув ручки, — день танцев")

add("tam-dance-nezhinskaya", "f_skirt",
    f'<ellipse cx="64" cy="82" rx="48" ry="14" fill="#E23B3B" {W(2.8)}/>'
    + f'<ellipse cx="64" cy="82" rx="36" ry="9" fill="#FF6464" stroke="none"/>'
    + path("M24 80 l-6 -4 M104 80 l6 -4 M40 94 l-4 4 M90 94 l4 4", "none", 2)
    + rect(56, 54, 16, 26, "#fff", 6)
    + limb("M58 58 L36 46", SKIN, 4) + limb("M70 58 L92 46", SKIN, 4)
    + limb("M60 92 L60 114", SKIN, 5) + limb("M68 92 L68 114", SKIN, 5)
    + head(64, 42, "#2B1A12", r=11, k=0.4) + circ(64, 28, 5, "#2B1A12", 2),
    "девочка в алой юбке-солнце",
    "кружится так быстро, что юбка раскрылась ровным красным кругом")

add("labirint-dance-rossoshanskaya", "f_steps",
    path("M-6 92 H134 V140 H-6Z", "#E9F7EE", 2.2)
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="6" ry="4" fill="{c}" {W(1.8)}/>' for x, y, c in [
        (14, 124, "#FF6F61"), (30, 114, "#FFC93C"), (46, 124, "#4FB0E8"), (88, 112, "#B07AE6"), (106, 122, "#FF6F61")])
    + limb("M58 92 L54 108", SKIN, 6) + limb("M70 92 L78 104", SKIN, 6)
    + rect(50, 62, 28, 32, "#4CBF62", 10)
    + limb("M52 68 L38 54", SKIN, 5) + limb("M76 68 L92 56", SKIN, 5)
    + head(64, 48, "#E2B65A", r=13, k=0.48)
    + path("M70 34 l8 -8 l4 8 l-8 2Z", "#FF5FA2", 2) + path("M76 32 l8 2 l-4 6Z", "#FF5FA2", 2)
    + sparkle(20, 40, 5) + sparkle(108, 40, 5),
    "малышка-трёхлетка в зелёном комбинезоне с розовым бантом",
    "прыгает по цветным следам-подсказкам на полу танцевального зала")

add("azbuka-tanca-vnukovo", "f_abc",
    path("M-6 104 H134 V140 H-6Z", "#C98A5A", 2.2)
    + G(44, 64, path("M-18 34 L0 -30 L18 34 L8 34 L4 18 H-4 L-8 34Z M-2 6 H2 L0 -6Z", "#2E2E3A", 2.6)
        + path("M-6 -10 l6 4 l6 -4 l-2 6 l2 6 l-6 -4 l-6 4 l2 -6Z", "#fff", 1.6) + face(0, 0, 5, 0.45, mouth=False), -10)
    + G(88, 66, path("M-14 32 V-28 H4 Q20 -28 18 -12 Q16 -2 6 0 Q22 4 20 18 Q18 32 2 32Z", "#FF7FA8", 2.6)
        + path("M-4 -18 H2 Q8 -18 8 -12 Q8 -6 2 -6 H-4Z M-4 6 H4 Q10 6 10 14 Q10 22 4 22 H-4Z", "#FFD3E2", 2)
        + face(4, -12, 4, 0.4, mouth=False), 10)
    + limb("M52 50 Q66 40 76 50", "#2E2E3A", 3) + notes(110, 30),
    "буква «А» в чёрном бальном фраке с бабочкой",
    "ведёт в медленном вальсе розовую букву «Б»")

add("sinergiya-akhmatovoy", "f_leap",
    f'<path d="M64 -10 L22 112 H106Z" fill="#fff" opacity=".22"/>'
    + path("M-6 108 H134 V140 H-6Z", "#8A5A3A", 2.2)
    + limb("M58 66 L18 74", "#fff", 7) + limb("M70 66 L108 58", "#fff", 7)
    + path("M52 46 L76 46 L74 70 L54 70Z", "#fff", 2.8)
    + limb("M54 50 L30 32", SKIN, 4) + limb("M74 50 L96 30", SKIN, 4)
    + head(64, 34, "#2B1A12", r=10, k=0.38)
    + sparkle(22, 24, 5) + sparkle(110, 90, 4) + path("M30 100 q34 -14 68 0", "none", 1.6),
    "мальчик-танцовщик в белой рубашке и белом трико",
    "взлетел над сценой в большом прыжке-шпагате под лучом софита")

add("zamet-stil-lukinskaya", "f_graf",
    rect(-6, 10, 140, 84, "#B9A79A", 0, 2.2)
    + path("M8 40 Q20 24 34 40 T60 40 M14 66 L30 52 L42 70 L56 50", "none", 5)
    + f'<path d="M8 40 Q20 24 34 40 T60 40" fill="none" stroke="#FF5FA2" stroke-width="3"/><path d="M14 66 L30 52 L42 70 L56 50" fill="none" stroke="#3FD0C0" stroke-width="3"/>'
    + path("M-6 94 H134 V140 H-6Z", "#8C8C96", 2.2)
    + limb("M80 92 L74 116", "#3A3A55", 7) + limb("M92 92 L100 114", "#3A3A55", 7)
    + rect(74, 60, 26, 34, "#FFC93C", 8)
    + limb("M76 66 L66 84", SKIN, 5) + limb("M98 66 L108 50", SKIN, 5) + path("M104 46 l4 -6 l2 6", "none", 2.4)
    + head(86, 48, "#5A3A26", r=11, k=0.42)
    + path("M74 42 Q74 30 86 30 Q98 30 98 42Z", "#FF4F8B", 2.4) + rect(64, 38, 14, 5, "#FF4F8B", 2, 2),
    "девочка в розовой кепке козырьком назад и жёлтом худи",
    "показывает «викторию» на фоне стены с яркими граффити")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for pid, code in ICONS.items():
        open(os.path.join(OUT, pid + ".svg"), "w").write(code)
    reg = os.path.join(OUT, "subjects.txt")
    lines = [l for l in open(reg, encoding="utf-8") if l.split(" — ", 1)[0] not in SUBJ]
    lines += [line + "\n" for line in SUBJ.values()]
    open(reg, "w", encoding="utf-8").writelines(lines)
    print(len(ICONS), "иконок:", " ".join(ICONS))
