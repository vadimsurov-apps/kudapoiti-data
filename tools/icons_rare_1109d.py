"""Иконки робота rare, 2026-11-09 (10 UTC) — места из tools/add_rare_1109d.py.
Правило АБСОЛЮТНОЙ уникальности: каждая придумана отдельно (свой герой, сцена, компоновка, палитра).
Просмотрены листы icons-catalog 01, 10, 20, 30, 40, 50 (остальные — по реестру subjects.txt: проверены скейт/ролики,
теннис/подача/ракетки, цирк, велосипеды). Заняты и НЕ использованы: скейт-персонаж, ролик-конёк, самокат на
памп-треке, мяч на подаче, ракетка-жонглёр, «две ракетки» сквош+бадминтон, белый кролик.
Запуск: python3 tools/icons_rare_1109d.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, eye, face, sparkle, O
from icons_sections_1107c import G
from icons_sections_1108g import rect, circ, ell, path, SKIN
from icons_rare_1109 import racket, tball

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
draw_icons.BG.update({
    "rd_hall": ("#F3EEFF", "#7B5CD6"), "rd_coach": ("#FFFBE6", "#E9B949"), "rd_volley": ("#FFEFF4", "#E2557B"),
    "rd_twins": ("#E8FFF8", "#27A98A"), "rd_climb": ("#EAF3FF", "#3E6FC4"), "rd_kart": ("#F5F5F0", "#8E9A5B"),
})


def add(pid, bg, body, hero, scene):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def wheel(x, y, r, c="#2B2B2B"):
    sp = "".join(f'<path d="M{x} {y} l{r*0.8*__import__("math").cos(a/57.3):.1f} {r*0.8*__import__("math").sin(a/57.3):.1f}" '
                 f'stroke="#9AA3AD" stroke-width="1.4"/>' for a in range(0, 360, 45))
    return circ(x, y, r, "none", 4.2).replace(O, c, 1) + circ(x, y, r + 2, "none", 2) + sp + circ(x, y, 3, "#9AA3AD", 1.6)


# 1. Bunny Hop — BMX-велосипед делает банни-хоп над фанбоксом
add("bunnyhop-smolnaya", "rd_hall",
    # фанбокс
    path("M18 112 L38 92 L90 92 L110 112Z", "#3FA7E0", 2.8) + rect(18, 112, 92, 14, "#2C86BC", 2, 2.8)
    + path("M40 100 H88", "none", 2).replace(O, "#ffffff", 1)
    # линии прыжка
    + path("M20 70 q8 -10 16 -2 M14 82 q8 -10 16 -2", "none", 2.6).replace(O, "#ffffff", 1)
    + G(64, 46,
        wheel(-26, 14, 15) + wheel(26, 14, 15)
        + path("M-26 14 L-6 -6 L18 -6 L26 14 M-6 -6 L2 14 L18 -6 M2 14 L-26 14", "none", 5).replace(O, "#FF7A1A", 1)
        + path("M-26 14 L-6 -6 L18 -6 L26 14 M-6 -6 L2 14 L18 -6 M2 14 L-26 14", "none", 1.6)
        + path("M18 -6 L14 -22 M6 -24 L22 -20", "none", 4)
        + path("M-6 -6 L-9 -16 M-16 -17 L-2 -17", "none", 4)
        + circ(2, 14, 4, "#FFB74D", 2)
        + face(4, 2, 5, 0.55), -18)
    + sparkle(104, 34, 6) + sparkle(24, 40, 4),
    "оранжевый BMX-велосипед с глазками на раме",
    "делает банни-хоп — подпрыгнул обоими колёсами над синим фанбоксом в крытом зале, задрав переднее колесо")

# 2. Теннис Групп — ракетка-тренер со свистком и три ракетки-ученика
add("tennis-group-akademicheskaya", "rd_coach",
    G(44, 50, racket("#FF7043", rx=21, ry=26, face_k=0.55), -8)
    + path("M30 64 q-4 10 4 14", "none", 1.8) + circ(36, 79, 4, "#C0C7CF", 1.8)
    + "".join(G(x, 92, racket("#5AB0F0", rx=8, ry=10, handle="#5B4636")
                + face(0, -1, 2.6, 0.32, mouth=False), 0) for x in (78, 96, 114))
    + tball(78, 70, 4) + tball(96, 70, 4) + tball(114, 70, 4),
    "большая оранжевая ракетка-тренер со свистком на шнурке",
    "строит на разминке три маленькие голубые ракетки-ученика, у каждой над головой по жёлтому мячу")

# 3. Школа тенниса Куприна — мальчик в красной бандане бьёт с лёта у сетки
add("kuprin-tennis-ostryakova", "rd_volley",
    # сетка
    rect(4, 86, 120, 30, "none", 0, 0)
    + "".join(f'<path d="M{x} 88 V122" stroke="#ffffff" stroke-width="1.3" opacity=".9"/>' for x in range(8, 124, 8))
    + "".join(f'<path d="M4 {y} H124" stroke="#ffffff" stroke-width="1.3" opacity=".9"/>' for y in range(94, 124, 7))
    + rect(4, 84, 120, 6, "#ffffff", 2, 2.4)
    # мальчик в выпаде
    + path("M58 70 L44 98", "none", 9).replace(O, "#2E3A59", 1) + path("M62 70 L80 96", "none", 9).replace(O, "#2E3A59", 1)
    + path("M40 98 h10 M78 96 h10", "none", 5)
    + rect(50, 46, 22, 28, "#FFFFFF", 8, 2.6)
    + path("M70 52 L92 38", "none", 6).replace(O, SKIN, 1)
    + G(98, 30, racket("#2EBD6B", rx=11, ry=13), 50)
    + path("M52 54 L36 62", "none", 6).replace(O, SKIN, 1)
    + circ(60, 32, 12, SKIN, 2.6) + path("M48 30 Q60 14 72 30 L76 26 L78 34 L72 32Z", "#E53935", 2.4)
    + face(60, 35, 4, 0.42)
    + tball(112, 54, 6) + path("M100 62 l6 -4 M98 54 l6 0", "none", 2).replace(O, "#ffffff", 1),
    "мальчик в красной бандане и белой футболке",
    "в длинном выпаде у самой сетки бьёт с лёта жёлтый мяч зелёной ракеткой")

# 4. Две ракетки — две ракетки дают пять, между ними мяч-сердечко
add("dve-raketki-setunsky", "rd_twins",
    G(42, 58, racket("#7C4DFF", rx=19, ry=23, face_k=0.5), 22)
    + G(86, 58, racket("#FFB300", rx=19, ry=23, face_k=0.5), -22)
    + sparkle(64, 26, 7, "#FFF59D")
    + tball(64, 104, 9, fc=True, k=0.4)
    + path("M54 28 l-6 -6 M74 28 l6 -6 M64 18 v-8", "none", 2.4).replace(O, "#ffffff", 1),
    "две ракетки-подружки — фиолетовая и янтарная",
    "наклонились навстречу и звонко дают пять ободами, у их ручек сидит улыбающийся жёлтый мяч")

# 5. Скалодром СК «Дворец детского спорта» — карабин держит верёвку девочки-скалолазки
add("climb-dds-rabochaya", "rd_climb",
    path("M14 8 L114 8 L120 128 L8 128Z", "#F2E6D0", 2.8)
    + "".join(circ(x, y, r, c, 2.2) for x, y, r, c in [(26, 36, 8, "#E53935"), (98, 30, 9, "#43A047"), (28, 82, 9, "#FFB300"),
                                                        (102, 72, 8, "#8E24AA"), (26, 112, 8, "#1E88E5"), (102, 110, 9, "#F4511E"),
                                                        (60, 120, 4, "#26C6DA")])
    + path("M64 30 C66 52 60 60 62 72", "none", 3.4).replace(O, "#E53935", 1)
    + G(64, 24, path("M-9 -14 C-20 -14 -20 14 -9 14 L9 14 C20 14 20 -14 9 -14Z", "#5EC0F5", 3.2)
        + path("M-8 -6 L8 -6", "none", 2.6) + face(0, 3, 4, 0.42), 0)
    + rect(52, 82, 22, 22, "#7E57C2", 7, 2.6)
    + path("M54 86 L42 74 M72 86 L86 78", "none", 5).replace(O, SKIN, 1)
    + circ(42, 72, 4, "#FFB300", 2) + circ(88, 77, 4, "#43A047", 2)
    + path("M57 102 L50 118 M69 102 L78 116", "none", 5).replace(O, "#3E4A6B", 1)
    + circ(63, 72, 10, SKIN, 2.4) + path("M52 70 Q63 54 74 70Z", "#FFD600", 2.4) + face(63, 75, 3.4, 0.36),
    "голубой страховочный карабин с глазками",
    "крепко держит наверху красную верёвку, по которой девочка в жёлтой каске лезет по стене с разноцветными зацепами")

if __name__ == "__main__":
    only = set(sys.argv[1:])
    for pid, s_ in ICONS.items():
        if not only or pid in only:
            open(os.path.join(OUT, pid + ".svg"), "w").write(s_)
    reg = os.path.join(OUT, "subjects.txt")
    keep = [l for l in open(reg).read().splitlines() if l.split(" — ")[0] not in SUBJ]
    open(reg, "w").write("\n".join(keep + [SUBJ[p] for p in SUBJ]) + "\n")
    print("icons", len(ICONS))
