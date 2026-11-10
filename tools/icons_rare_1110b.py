"""Иконки робота rare, 2026-11-10 (04 UTC) — места из tools/add_rare_1110b.py (детский теннис и бадминтон).
Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно — свой герой, своя сцена, своя компоновка и палитра.
Якорь — теннисная ракетка со струнами и/или жёлтый теннисный мяч (у бадминтона — волан).
Перед рисованием реестр subjects.txt проверен grep'ом; заняты и заменены: вулкан, катушка/ткацкий станок, колосок,
пугало, волшебник/колпак, воздушный шар, светофор, лось, тюлень, ушанка, панамка, наковальня, стетоскоп.
Запуск: python3 tools/icons_rare_1110b.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O
from icons_sections_1107c import G
from icons_sections_1108g import rect, circ, ell, path

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
BALL = "#E4F04A"


def add(pid, pal, body, hero, scene):
    k = f"r_{pid}"
    draw_icons.BG[k] = pal
    ICONS[pid] = svg(k, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def ball(x, y, r=9, rot=0):
    """Теннисный мяч с белым швом."""
    return G(x, y, circ(0, 0, r, BALL, 2.4)
             + f'<path d="M{-r*.75:.1f} {-r*.6:.1f} Q0 0 {-r*.75:.1f} {r*.6:.1f} M{r*.75:.1f} {-r*.6:.1f} Q0 0 {r*.75:.1f} {r*.6:.1f}" '
               f'fill="none" stroke="#fff" stroke-width="{max(1.4, r/6):.1f}" stroke-linecap="round"/>', rot)


def racket(x, y, rot=0, sc=1.0, rim="#E8414F", grip="#3B3355", strings="#8E9BB3", head=None):
    """Теннисная ракетка: овальный обод со струнами, горло и ручка. Центр головы в (0,0) до поворота."""
    st = "".join(f'<path d="M{i} -19 V19" stroke="{strings}" stroke-width="1.7"/>' for i in range(-10, 11, 5))
    st += "".join(f'<path d="M-15 {j} H15" stroke="{strings}" stroke-width="1.7"/>' for j in range(-12, 13, 6))
    clip = f'<clipPath id="rk{abs(hash((x, y, rot))) % 99999}"><ellipse cx="0" cy="0" rx="15" ry="20"/></clipPath>'
    cid = clip.split('id="')[1].split('"')[0]
    body = (clip + f'<path d="M-5 18 L-3 32 H3 L5 18" fill="{rim}" {s("stroke-width=\"2.4\"")}/>'
            + rect(-3.5, 31, 7, 20, grip, 3, 2.4)
            + ell(0, 0, 15, 20, head or "#FFFFFF", 0)
            + f'<g clip-path="url(#{cid})">{st}</g>'
            + f'<ellipse cx="0" cy="0" rx="15" ry="20" fill="none" stroke="{rim}" stroke-width="5"/>'
            + f'<ellipse cx="0" cy="0" rx="17.5" ry="22.5" fill="none" {s("stroke-width=\"2.2\"")}/>'
            + f'<ellipse cx="0" cy="0" rx="12.5" ry="17.5" fill="none" {s("stroke-width=\"1.6\"")}/>')
    return G(x, y, body, rot, sc)


def ground(y, c, sw=2.6):
    return path(f"M-6 {y} Q64 {y-6} 134 {y} V140 H-6Z", c, sw)


# 1. RacketBall — хомяк в мяче-колесе
add("racketball-strelbishchensky", ("#FFE3F0", "#F27AAE"),
    ground(104, "#6FB7E8")
    + path("M20 112 H108", "none", 2).replace(O, "#FFFFFF")
    + circ(64, 64, 38, BALL, 3)
    + f'<path d="M30 46 Q64 64 30 84 M98 46 Q64 64 98 84" fill="none" stroke="#fff" stroke-width="4.5" stroke-linecap="round" opacity=".9"/>'
    + ell(64, 72, 17, 14, "#F2B36B", 2.6) + ell(64, 77, 10, 8, "#FFE7C2", 0)
    + circ(52, 58, 5, "#F2B36B", 2.4) + circ(76, 58, 5, "#F2B36B", 2.4)
    + circ(52, 58, 2.4, "#FF9BB8", 0) + circ(76, 58, 2.4, "#FF9BB8", 0)
    + eye(58, 68, 0.6) + eye(70, 68, 0.6) + circ(64, 73, 1.6, "#FF6F91", 0)
    + path("M61 76 Q64 79 67 76", "none", 1.8)
    + ell(55, 85, 3.5, 2.4, "#F2B36B", 2) + ell(73, 85, 3.5, 2.4, "#F2B36B", 2)
    + path("M14 70 h8 M10 80 h10 M16 90 h6", "none", 2.4).replace(O, "#FFFFFF"),
    "хомячок с розовыми ушками",
    "бежит внутри огромного жёлтого теннисного мяча, как в колесе, и катит его по синему корту")

# 2. TFL — зимородок на ручке ракетки
add("tfl-tennis-lyublinskaya", ("#FFF4C9", "#FFB84D"),
    racket(70, 56, -28, 1.55, "#2E9E6B", "#3B3355")
    + G(30, 100, ell(0, 0, 14, 10, "#FF8A3D", 2.6)
        + path("M-6 -8 Q-2 -24 12 -22 Q22 -18 16 -6 Q8 2 -6 -2Z", "#1E88E5", 2.6)
        + path("M-14 2 Q-26 8 -24 16 L-10 8Z", "#1565C0", 2.4)
        + path("M15 -16 L34 -13 L16 -10Z", "#3B3355", 2)
        + eye(8, -16, 0.55) + circ(6, -8, 3, "#FFFFFF", 0)
        + path("M-4 9 V15 M4 9 V15", "none", 2.2), -8)
    + ball(64, 86, 7.5)
    + sparkle(104, 100, 5),
    "зимородок с синей спинкой и рыжей грудкой",
    "сидит у ручки зелёной теннисной ракетки и держит в длинном клюве жёлтый мяч, как пойманную рыбку")

# 3. Турсунов — ирбис в прыжке
add("tursunov-tennis-profsoyuznaya", ("#EAF6FF", "#7FB3E0"),
    ground(108, "#4A78C2")
    + G(58, 70, ell(0, 0, 26, 13, "#EDEDE6", 2.8)
        + circ(-12, -4, 2.6, "#7A7A7A", 0) + circ(2, 4, 2.4, "#7A7A7A", 0) + circ(12, -3, 2.6, "#7A7A7A", 0)
        + path("M24 -2 Q44 -16 40 -30", "none", 8).replace(O, "#3B3355")
        + path("M24 -2 Q44 -16 40 -30", "none", 5).replace(O, "#EDEDE6")
        + path("M-22 6 L-34 22 M-14 9 L-20 26 M14 9 L22 24 M22 4 L34 18", "none", 3.2), -14)
    + G(32, 54, circ(0, 0, 13, "#EDEDE6", 2.8) + path("M-10 -10 L-8 -18 L-2 -12 M10 -10 L8 -18 L2 -12", "#EDEDE6", 2.4)
        + face(0, 0, d=5, k=0.55) + circ(-6, -6, 1.6, "#7A7A7A", 0) + circ(7, 7, 1.4, "#7A7A7A", 0))
    + racket(92, 34, 40, 1.05, "#7E57C2")
    + ball(110, 66, 7) + path("M100 78 q-4 6 -10 8", "none", 1.8).replace(O, "#FFFFFF"),
    "снежный барс ирбис в пятнышках",
    "в длинном прыжке над синим хардом тянется фиолетовой ракеткой к улетающему мячу")

# 4. Мегаспорт — ракетка-пожарный
add("megasport-tennis-samory-mashela", ("#FFE9D4", "#FF8F5A"),
    racket(46, 58, 8, 1.6, "#FFC107", "#3B3355")
    + face(46, 62, d=8, k=0.75)
    + G(46, 22, path("M-22 6 Q-20 -14 0 -16 Q20 -14 22 6 Z", "#E53935", 2.6) + rect(-26, 4, 52, 6, "#E53935", 3, 2.4)
        + rect(-6, -12, 12, 10, "#FFD54F", 2, 2))
    + path("M64 92 Q84 96 92 82", "none", 5).replace(O, "#3B3355")
    + path("M64 92 Q84 96 92 82", "none", 3).replace(O, "#90A4AE")
    + G(98, 74, ball(0, 0, 9) + path("M-6 -12 q-4 -8 2 -14 M4 -12 q4 -8 -2 -14", "none", 2).replace(O, "#B0BEC5"))
    + path("M92 82 Q104 56 116 62", "none", 3).replace(O, "#4FC3F7")
    + circ(106, 60, 2.4, "#4FC3F7", 0) + circ(114, 70, 2, "#4FC3F7", 0),
    "жёлтая теннисная ракетка-пожарный в красной каске",
    "заливает из шланга дымящийся после смэша теннисный мяч")

# 5. Потапово — казуар на крытом корте
add("tennis-potapovo-semenova", ("#E2FAD9", "#58B368"),
    ground(102, "#3E9B4F")
    + path("M10 112 H118 M64 100 V128", "none", 2.2).replace(O, "#FFFFFF")
    + G(50, 76, ell(0, 0, 22, 18, "#263238", 2.8)
        + path("M8 -10 Q10 -36 16 -44", "none", 9).replace(O, "#3B3355")
        + path("M8 -10 Q10 -36 16 -44", "none", 6).replace(O, "#29B6F6")
        + circ(17, -48, 9, "#29B6F6", 2.6) + path("M12 -56 Q16 -70 24 -58Z", "#C98A3E", 2.2)
        + path("M24 -48 L34 -44 L24 -42Z", "#3B3355", 1.8) + eye(19, -50, 0.5)
        + path("M10 -24 q-4 8 0 12", "#E53935", 2) + path("M-6 16 V30 M6 16 V30", "none", 3.4))
    + racket(96, 60, 22, 1.25, "#FF7043")
    + ball(70, 26, 7),
    "казуар с синей шеей и рогом-шлемом",
    "стоит на зелёном искусственном газоне крытого корта и следит за мячом над красной ракеткой")

# 6. Русланов — скворец в скворечнике на ракетке
add("ruslanov-tennis-leninsky", ("#E6F4FF", "#5C9BE6"),
    racket(64, 42, 0, 1.45, "#3949AB", "#5D4037")
    + G(64, 100, rect(-17, -14, 34, 28, "#A1887F", 3, 2.6) + path("M-21 -12 L0 -28 L21 -12Z", "#6D4C41", 2.6)
        + circ(0, -1, 7, "#3B3355", 0)
        + circ(0, -2, 6.5, "#37474F", 0) + eye(-2, -4, 0.38) + eye(2.5, -4, 0.38)
        + path("M3 0 L10 1 L3 3Z", "#FFC107", 1.4)
        + circ(-4, 2, 1, "#FFFFFF", 0) + circ(1, 4, 1, "#FFFFFF", 0))
    + ball(98, 98, 7) + sparkle(28, 92, 4),
    "скворец в чёрном пёрышке с белыми крапинками",
    "выглядывает из скворечника, прибитого к ручке синей теннисной ракетки, и косится на мяч рядом")

# 7. Tennis Group (Тимирязевская академия) — цесарка клюёт мячи-зёрна
add("tennis-group-mskha", ("#F6FFD6", "#B5D43D"),
    ground(98, "#C49A5A")
    + racket(98, 54, 18, 1.2, "#43A047")
    + G(44, 74, ell(0, 0, 20, 15, "#455A64", 2.8)
        + "".join(circ(x, y, 1.6, "#FFFFFF", 0) for x, y in [(-10, -4), (-2, -8), (6, -4), (-6, 4), (4, 4), (12, 2), (-12, 6)])
        + path("M14 -6 Q22 -20 26 -26", "none", 6).replace(O, "#455A64")
        + circ(28, -28, 6, "#ECEFF1", 2.4) + path("M26 -34 Q28 -40 32 -34", "#E53935", 1.8)
        + eye(29, -29, 0.4) + path("M33 -27 L38 -24 L33 -23Z", "#FFB300", 1.4)
        + path("M-4 14 V24 M4 14 V24", "none", 2.6))
    + ball(76, 104, 5.5) + ball(92, 110, 5) + ball(60, 112, 4.5),
    "пятнистая серая цесарка с белым хохолком",
    "на агрополе клюёт рассыпанные теннисные мячи, как зёрна, у зелёной ракетки")

# 8. ТеннисЁнок — буква Ё с мячами-точками
add("tennisyonok-petrovsko-razumovsky", ("#EFE3FF", "#9C6BE8"),
    G(56, 72, path("M-20 -30 H18 V-18 H-6 V-6 H14 V6 H-6 V18 H18 V30 H-20Z", "#FF8A65", 3))
    + ball(44, 30, 8) + ball(66, 30, 8)
    + face(54, 80, d=6, k=0.6)
    + racket(96, 76, 24, 1.05, "#26A69A"),
    "оранжевая буква «Ё» с двумя теннисными мячами вместо точек",
    "радостно держит рядом маленькую бирюзовую ракетку — получается «ТеннисЁнок»")

# 9. Малышковый теннис — перепелёнок под ракеткой-зонтиком
add("malyshkovy-tennis-mira-81", ("#E0FFF4", "#4FCFA6"),
    ground(106, "#FFB3C7")
    + racket(64, 40, 180, 1.5, "#FF5C8A", "#7E57C2")
    + G(62, 88, ell(0, 0, 18, 15, "#FFE082", 2.8) + path("M-6 -14 Q-2 -22 2 -14", "#FFE082", 2)
        + face(0, -2, d=6, k=0.6) + path("M-2 4 L2 4 L0 8Z", "#FF9800", 1.4)
        + path("M-16 2 Q-24 -2 -20 8Z", "#FFD54F", 2) + path("M-5 14 V19 M5 14 V19", "none", 2.2))
    + ball(88, 96, 5),
    "пушистый жёлтый перепелёнок",
    "прячется под перевёрнутой розовой ракеткой, как под зонтиком, рядом крошечный мячик")

# 10. Tennis77 (Сигнальный пр-д) — мяч-сигнальщик с флажками
add("tennis77-signalny", ("#DDF2FF", "#3E8EDB"),
    rect(-6, 92, 140, 4, "#FFFFFF", 0, 2) + path("M-6 96 H134", "none", 2)
    + "".join(path(f"M{x} 96 V122", "none", 1.4) for x in range(4, 130, 10))
    + path("M-6 108 H134 M-6 120 H134", "none", 1.2)
    + ball(64, 58, 22)
    + face(64, 60, d=8, k=0.75)
    + path("M44 56 L26 34", "none", 3) + path("M26 34 V14 L44 20 L26 26", "#E53935", 2.4)
    + path("M84 56 L104 70", "none", 3) + path("M104 70 L120 60 L118 80 Z", "#FFEB3B", 2.4)
    + racket(28, 92, -30, 0.8, "#1E88E5"),
    "теннисный мяч-сигнальщик с красным и жёлтым флажками",
    "стоит над сеткой и машет флажками семафорной азбуки, подавая знак к началу игры")

# 11. Magic Ball — клёст натягивает струны
add("magic-ball-tennis-tallinskaya", ("#FFE6E1", "#F06A5C"),
    racket(60, 64, -12, 1.7, "#5E35B1", "#3B3355", strings="#FFF59D")
    + G(98, 30, ell(0, 0, 13, 10, "#E53935", 2.6) + circ(-10, -4, 8, "#E53935", 2.4)
        + path("M-17 -6 Q-24 -2 -20 4 M-17 -2 Q-24 -10 -16 -12", "none", 2.2)
        + eye(-11, -6, 0.45) + path("M10 -2 L22 4 L10 6Z", "#8D3B32", 2) + path("M-2 9 V14 M4 9 V14", "none", 2))
    + path("M78 30 Q70 42 66 46", "none", 1.6).replace(O, "#FFF59D")
    + ball(98, 98, 8) + sparkle(24, 24, 5) + sparkle(110, 70, 3.5),
    "красный клёст со скрещённым клювом",
    "сидит на ободе фиолетовой ракетки и клювом подтягивает золотую струну, как настройщик")

# 12. Вулкан — ракетка с лавой
add("vulkan-tennis-izmaylovsky", ("#FFE0C2", "#E2523B"),
    ell(30, 28, 14, 8, "#B0A39B", 0) + ell(98, 22, 12, 7, "#B0A39B", 0) + ell(108, 34, 9, 6, "#C9BDB5", 0)
    + racket(58, 66, -18, 1.7, "#D84315", "#4E342E", strings="#FFCC80")
    + path("M40 36 q-2 10 3 14 q4 4 0 10 M72 30 q2 8 -2 12", "#FF7043", 2.2)
    + face(58, 66, d=8, k=0.7)
    + ball(100, 56, 8) + path("M92 64 q-6 6 -6 12 M98 66 q-2 6 0 10", "none", 2).replace(O, "#FFB74D"),
    "огненно-оранжевая ракетка с подтёками лавы на ободе",
    "дымится после мощной подачи, а мяч улетает, оставляя жаркий след")

# 13. МССУОР №3 — трясогузка на линии корта
add("mssuor3-tennis-tkatskaya", ("#D8FBF6", "#2BB3A3"),
    ground(84, "#2F7D6D")
    + path("M-6 98 H134", "none", 4).replace(O, "#FFFFFF")
    + racket(98, 46, 30, 1.2, "#FF7043")
    + G(46, 84, ell(0, 0, 14, 8, "#9E9E9E", 2.6) + ell(0, 3, 9, 4, "#FFFFFF", 0)
        + circ(12, -8, 7, "#FFFFFF", 2.4) + path("M8 -14 Q14 -18 18 -12", "#212121", 2)
        + eye(13, -9, 0.4) + path("M18 -8 L24 -7 L18 -5Z", "#212121", 1.4)
        + path("M-12 -2 L-34 -16 L-30 -10 L-36 -8Z", "#212121", 2.2) + path("M-2 7 V14 M4 7 V14", "none", 2), -6)
    + ball(76, 92, 6),
    "серая трясогузка с длинным покачивающимся хвостом",
    "семенит по белой линии корта вслед за катящимся мячом")

# 14. Олимпиец — ракетка-дискобол в хитоне
add("olimpiets-tennis-udaltsova", ("#FFF8E1", "#E0B74C"),
    rect(36, 104, 56, 14, "#ECE3D0", 2, 2.6) + rect(30, 116, 68, 12, "#DDD2BC", 2, 2.6)
    + racket(58, 54, -35, 1.5, "#1565C0")
    + face(56, 56, d=7, k=0.65)
    + path("M40 74 L36 100 H80 L74 72 Q58 82 40 74Z", "#FFFFFF", 2.6)
    + path("M44 78 L70 96", "none", 1.6)
    + path("M38 86 Q20 74 18 60", "none", 3)
    + ball(18, 52, 8)
    + path("M42 30 q-6 -4 -4 -10 M50 26 q-2 -6 2 -10 M62 26 q4 -6 8 -4", "#7CB342", 2),
    "синяя ракетка в белом хитоне и лавровой веточке",
    "застыла на мраморном постаменте в позе античного дискобола, только вместо диска — теннисный мяч")

# 15. ФОК «Гелиос» — волан-солнце над сеткой
add("fok-gelios-badminton", ("#FFF1D6", "#FF8A50"),
    "".join(path(f"M64 74 L{64+60*__import__('math').cos(a):.0f} {74-60*__import__('math').sin(a):.0f}", "none", 4)
            .replace(O, "#FFE082") for a in [0.25, 0.75, 1.25, 1.57, 1.9, 2.4, 2.9])
    + G(64, 66, path("M-24 -26 L-8 10 H8 L24 -26 Q0 -34 -24 -26Z", "#FFFFFF", 2.6)
        + path("M-12 -29 L-4 10 M0 -31 V10 M12 -29 L4 10", "none", 1.6)
        + path("M-24 -26 Q0 -34 24 -26", "none", 3).replace(O, "#FFB300")
        + rect(-11, 8, 22, 6, "#FFB300", 2, 2.2)
        + path("M-11 14 Q0 30 11 14Z", "#FFCA28", 2.6)
        + face(0, -8, d=6, k=0.6))
    + path("M-6 100 H134", "none", 3)
    + "".join(path(f"M{x} 100 V128", "none", 1.2) for x in range(2, 130, 9))
    + path("M-6 112 H134", "none", 1.2),
    "белый волан с золотым ободком и лучами за спиной",
    "восходит над бадминтонной сеткой, как утреннее солнце Гелиос")

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for pid, b in ICONS.items():
        open(os.path.join(OUT, f"{pid}.svg"), "w").write(b)
    if "--svg-only" in sys.argv:
        sys.exit(print(len(ICONS), "svg"))
    reg = os.path.join(OUT, "subjects.txt")
    have = {l.split(" — ")[0] for l in open(reg, encoding="utf-8")}
    with open(reg, "a", encoding="utf-8") as f:
        for pid, line in SUBJ.items():
            if pid not in have:
                f.write(line + "\n")
    print(len(ICONS), "icons")
