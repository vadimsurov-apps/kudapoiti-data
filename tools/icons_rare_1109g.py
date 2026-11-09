"""Иконки робота rare, 2026-11-09 (вечер) — места из tools/add_rare_1109g.py.
АБСОЛЮТНАЯ уникальность: просмотрены все 54 листа icons-catalog (уменьшенными сводками по 6) и реестр subjects.txt
(падел: короны, очки, шапки, береты, звери; теннис: мяч-мама, мальчики/девочки в выпаде, лодка-ракетка; скалодромы:
зверьки на стене, туфли, мел, карабин). Каждая иконка придумана отдельно: свой герой, сцена, ракурс и палитра фона.
Запуск: python3 tools/icons_rare_1109g.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, eye, face, sparkle, O
from icons_sections_1107c import G
from icons_sections_1108g import rect, circ, ell, path, SKIN

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
draw_icons.BG.update({
    "rg_platform": ("#FFF4F0", "#F08A7A"), "rg_wall": ("#F0FBFF", "#4E9BD6"), "rg_pines": ("#F4FFF0", "#5FAF6A"),
    "rg_family": ("#FFFBEA", "#F2C14E"), "rg_smash": ("#F5F0FF", "#9C7BE8"), "rg_cannon": ("#EFFFFA", "#3FBFA0"),
    "rg_diplo": ("#F2F6FF", "#7E9BD8"),
})
LIME = "#D7F25A"
YEL = "#E8E04A"


def add(pid, bg, body, hero, scene):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def wpath(d, c, sw):
    return path(d, "none", sw).replace(O, c, 1)


# 1. Padl Hub «Селигерская» — у академии «станции»: ракетка-дежурная по станции в красной фуражке, флажок отправления
holes = "".join(circ(x, y, 2.6, "#FFF4EC", 1.4) for x, y in
                [(-12, -18), (0, -20), (12, -18), (-16, -6), (16, -6), (-12, 6), (12, 6), (0, 10)])
paddle1 = (rect(-6, 30, 12, 30, "#3B3355", 4, 2.6) + wpath("M0 60 Q-10 70 -2 76", "#FFC93C", 3)
           + ell(0, -4, 30, 36, "#FF6F61", 3) + ell(0, -4, 22, 28, "#FF8F7E", 0) + holes
           + face(0, -2, d=9, k=1.0)
           + path("M-24 -34 Q0 -50 24 -34 L22 -28 H-22Z", "#D62E3A", 2.6)
           + rect(-26, -30, 52, 6, "#2B2F4A", 2, 2.2) + circ(0, -38, 3.2, "#FFC93C", 1.6))
flag = (wpath("M0 0 V-34", "#6B4A2E", 3) + path("M0 -34 L22 -28 L0 -20Z", "#2FB36A", 2.2))
platform = rect(-10, 104, 148, 30, "#C7C2D6", 0, 2.4) + wpath("M-6 106 H134", "#FFD34D", 4)
add("padlhub-seligerskaya", "rg_platform",
    platform + G(60, 62, paddle1, -6, 1.05) + G(100, 100, flag, 0, 1) + circ(28, 92, 8, LIME, 2.2)
    + wpath("M23 88 Q28 92 23 96 M33 88 Q28 92 33 96", "#FFFFFF", 1.6) + sparkle(110, 26, 5),
    "коралловая падел-ракетка с дырочками в красной фуражке дежурной по станции",
    "стоит на перроне с жёлтой линией у края, рядом зелёный флажок отправления и лаймовый мяч")

# 2. GoClimb МГТУ им. Баумана — высокая стена с зацепами, наверху мешочек с магнезией подтягивается и пускает облачко мела
wall = (path("M18 -4 L110 -4 L118 132 L10 132Z", "#2E6FB3", 2.8)
        + path("M18 -4 L64 -4 L60 132 L10 132Z", "#3A82C9", 0))
holds = "".join(circ(x, y, r, c, 2) for x, y, r, c in
                [(34, 102, 6, "#FF7A59"), (82, 96, 5, "#FFD34D"), (48, 78, 5, "#7CD26E"), (92, 70, 6, "#FF8FC7"),
                 (36, 52, 5, "#FFD34D"), (70, 56, 4.5, "#FF7A59"), (98, 40, 5, "#7CD26E"), (42, 24, 5, "#FF8FC7")])
rope = wpath("M84 -4 Q86 40 72 70 Q60 96 66 132", "#FF5A5A", 2.4)
bag = (ell(0, 8, 15, 16, "#FF9A3C", 2.8) + rect(-16, -10, 32, 8, "#E07A20", 3, 2.4)
       + face(0, 10, d=6, k=0.75)
       + wpath("M-13 -6 Q-22 -14 -18 -22", O, 3) + wpath("M13 -6 Q22 -14 18 -22", O, 3)
       + circ(-18, -24, 3.4, "#FFD8B8", 1.8) + circ(18, -24, 3.4, "#FFD8B8", 1.8))
cloud = (circ(0, 0, 7, "#FFFFFF", 1.6) + circ(9, -3, 6, "#FFFFFF", 1.6) + circ(-8, -4, 5, "#FFFFFF", 1.6))
add("goclimb-bauman", "rg_wall",
    wall + holds + rope + path("M4 120 Q64 112 124 120 L124 134 L4 134Z", "#5560A8", 2.4)
    + G(64, 44, bag, 0, 1.45) + G(100, 16, cloud, 0, 1.1) + sparkle(22, 40, 4),
    "оранжевый мешочек для магнезии с ручками и глазками",
    "подтягивается у самого верха высокой синей стены с разноцветными зацепами, рядом красная верёвка и облачко мела")

# 3. Падел в Сокольниках — корт в лесу: большая падел-ракетка стоит между соснами, из-за неё выглядывает шишка-болельщица
def pine(x, y, k):
    return G(x, y, rect(-4, 30, 8, 26, "#8A5530", 2, 2.2)
             + path("M0 -40 L18 -10 H10 L24 14 H14 L28 36 H-28 L-14 14 H-24 L-10 -10 H-18Z", "#2E8B57", 2.6), 0, k)
paddle3 = (rect(-6, 28, 12, 28, "#3B3355", 4, 2.6) + ell(0, -6, 27, 33, "#FF9A3C", 3)
           + "".join(circ(x, y, 2.4, "#FFF0DE", 1.4) for x, y in
                     [(-10, -22), (0, -26), (10, -22), (-14, -10), (14, -10), (-10, 4), (10, 4), (0, 8)])
           + face(0, -8, d=8, k=0.95))
cone = (ell(0, 0, 9, 12, "#A0652F", 2.4)
        + wpath("M-8 -4 Q0 0 8 -4 M-8 4 Q0 8 8 4", "#6E3F17", 1.6)
        + eye(-3, -2, .45) + eye(3, -2, .45) + wpath("M-11 -2 L-17 -10 M11 -2 L17 -10", O, 2.4))
add("padel-sokolniki-les", "rg_pines",
    pine(18, 74, 1.0) + pine(112, 70, 1.05) + path("M-4 112 Q64 102 132 112 V134 H-4Z", "#8FCB6E", 2.4)
    + G(64, 64, paddle3, 8, 1.08) + G(96, 98, cone, 10, 1.0) + circ(36, 30, 7, LIME, 2.2) + sparkle(62, 14, 4),
    "сосновая шишка-болельщица с поднятыми ручками",
    "выглядывает из-за большой оранжевой падел-ракетки, что стоит на поляне между двумя соснами")

# 4. Tennis Family (Писцовая) — ракетка-папа катает на макушке обода маленький мячик-сынишку
strings = "".join(wpath(f"M{x} -30 V22", "#FFFFFF", 1.6) for x in (-15, -9, -3, 3, 9, 15)) + \
          "".join(wpath(f"M-20 {y} H20", "#FFFFFF", 1.6) for y in (-22, -14, -6, 2, 10, 18))
racket4 = (rect(-5, 30, 10, 34, "#2B5FA8", 4, 2.6) + rect(-6, 50, 12, 14, "#F5F5F5", 3, 2.2)
           + ell(0, -4, 26, 32, "none", 6).replace('fill="none"', 'fill="#BFE6FF" fill-opacity=".55"') + strings
           + ell(0, -4, 26, 32, "none", 5).replace(O, "#2B7BD6", 1) + face(0, -2, d=9, k=0.95)
           + wpath("M-24 4 Q-36 -2 -34 -16", O, 3.2) + wpath("M24 4 Q34 -4 30 -18", O, 3.2))
kid = (circ(0, 0, 11, YEL, 2.6) + wpath("M-9 -5 Q0 1 9 -5", "#FFFFFF", 1.8) + eye(-4, 1, .5) + eye(4, 1, .5)
       + wpath("M-2 6 Q0 8 2 6", O, 1.4) + wpath("M8 -6 Q14 -16 18 -12", O, 2.6))
add("tennis-family-pistsovaya", "rg_family",
    G(64, 72, racket4, -4, 1.12) + G(60, 24, kid, 0, 1.0)
    + circ(104, 98, 6, YEL, 2) + sparkle(22, 30, 5) + sparkle(106, 44, 3.5),
    "голубая теннисная ракетка-папа со струнами",
    "катает на макушке обода маленький жёлтый мячик-сынишку, тот машет ручкой")

# 5. «Держава» Крылатское — мальчик в оранжевой кепке в прыжке бьёт смэш над головой, мяч сверху
boy = (wpath("M0 10 L-12 30 M0 10 L12 28", "#2B2F4A", 5) + rect(-10, -12, 20, 24, "#FFFFFF", 6, 2.6)
       + wpath("M-9 -6 L-22 -26", SKIN, 5) + wpath("M9 -6 L18 6", SKIN, 5)
       + circ(0, -22, 10, SKIN, 2.6) + path("M-10 -24 Q0 -38 10 -24 Z", "#FF8A1F", 2.4) + wpath("M8 -26 L18 -24", "#FF8A1F", 4)
       + eye(-3, -20, .45) + eye(4, -20, .45) + wpath("M-2 -15 Q1 -12 4 -15", O, 1.6)
       + G(-26, -32, rect(-2, 0, 4, 18, "#3B3355", 2, 2) + ell(0, -12, 11, 14, "#FFFFFF", 3)
           + "".join(wpath(f"M{x} -24 V0", "#9C7BE8", 1.2) for x in (-5, 0, 5))
           + "".join(wpath(f"M-9 {y} H9", "#9C7BE8", 1.2) for y in (-18, -12, -6)), 20, 1.0))
add("tennis-derzhava-krylatskoe", "rg_smash",
    path("M-4 112 Q40 92 80 104 Q110 112 132 100 V134 H-4Z", "#7CC26A", 2.4)
    + G(70, 74, boy, 0, 1.55) + circ(30, 20, 8, YEL, 2.2) + wpath("M24 16 Q30 22 24 26", "#FFFFFF", 1.6)
    + wpath("M40 30 Q48 38 54 34", "#FFFFFF", 2) + sparkle(108, 28, 5),
    "мальчик в оранжевой кепке и белой футболке с теннисной ракеткой",
    "в высоком прыжке над зелёным холмом бьёт смэш по мячу над головой")

# 6. «Держава» Фили — машина-мячемёт с глазками выстреливает веер жёлтых мячей, у колеса — ракетка
machine = (rect(-30, -6, 60, 34, "#2FA37E", 8, 3) + G(0, -6, rect(-9, -34, 18, 34, "#2FA37E", 4, 3) + ell(0, -34, 9, 4, "#1F7A5C", 2.4), -35, 1.0) + face(0, 10, d=10, k=1.0)
           + circ(-20, 30, 8, "#3B3355", 2.4) + circ(20, 30, 8, "#3B3355", 2.4)
           + circ(-20, 30, 3, "#BDBDBD", 1.4) + circ(20, 30, 3, "#BDBDBD", 1.4))
balls = "".join(circ(x, y, 7, YEL, 2.2) + wpath(f"M{x-5} {y-3} Q{x} {y+2} {x+5} {y-3}", "#FFFFFF", 1.4)
                for x, y in [(96, 18), (78, 10), (112, 36), (100, 52)])
racket6 = G(22, 96, rect(-3, 10, 6, 20, "#3B3355", 2, 2) + ell(0, -6, 10, 13, "#FFFFFF", 2.6)
            + "".join(wpath(f"M{x} -18 V6", "#E8554A", 1.1) for x in (-4, 0, 4)), -30, 1.0)
add("tennis-derzhava-fili", "rg_cannon",
    path("M-4 106 H132 V134 H-4Z", "#E58A4E", 2.4) + wpath("M-4 112 H132", "#FFFFFF", 2.4)
    + balls + G(60, 74, machine, 0, 1.2) + racket6 + sparkle(20, 48, 4),
    "зелёная машина-мячемёт на колёсиках с глазками",
    "выстреливает веер жёлтых теннисных мячей над грунтовым кортом, рядом лежит ракетка")

# 7. «Держава» МГИМО — дипломатия: синяя и красная ракетки жмут друг другу ручки над сеткой
def rk(c, rot, x, mood):
    return G(x, 54, ell(0, -10, 18, 22, c, 3)
             + "".join(wpath(f"M{dx} -30 V10", "#FFFFFF", 1.3) for dx in (-8, -3, 2, 7))
             + "".join(wpath(f"M-15 {dy} H15", "#FFFFFF", 1.3) for dy in (-22, -14, -6, 2))
             + face(0, -10, d=6, k=0.7) + rect(-4, 12, 8, 20, "#3B3355", 3, 2.4), rot, 1.15)
net = (rect(4, 92, 120, 18, "#FFFFFF", 2, 2.4)
       + "".join(wpath(f"M{x} 92 V110", "#9AA6C8", 1.2) for x in range(12, 124, 8))
       + wpath("M4 101 H124", "#9AA6C8", 1.2) + rect(2, 88, 124, 5, "#2B2F4A", 2, 2))
add("tennis-derzhava-mgimo", "rg_diplo",
    net + rk("#2B5FA8", -22, 44, 1) + rk("#D94A4A", 22, 84, 1)
    + circ(64, 88, 7, SKIN, 2.2) + circ(64, 26, 7, YEL, 2.2)
    + sparkle(20, 24, 4) + sparkle(110, 22, 4),
    "синяя и красная теннисные ракетки со струнами",
    "жмут друг другу ручки над теннисной сеткой, как дипломаты на переговорах, над ними жёлтый мяч")

if __name__ == "__main__":
    only = set(sys.argv[1:])
    for pid, s_ in ICONS.items():
        if not only or pid in only:
            open(os.path.join(OUT, pid + ".svg"), "w").write(s_)
    reg = os.path.join(OUT, "subjects.txt")
    keep = [l for l in open(reg).read().splitlines() if l.split(" — ")[0] not in SUBJ]
    open(reg, "w").write("\n".join(keep + [SUBJ[p] for p in SUBJ]) + "\n")
    print("icons", len(ICONS))
