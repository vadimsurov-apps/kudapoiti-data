"""Иконки робота sections (2026-11-06, обед): 23 новых сюжета — бассейн, единоборства, футбол, регби, лёд, лёгкая
атлетика, танцы. Сюжеты сверены со всеми листами icons-catalog/sheet-01..19.png и icons-src/subjects.txt
(заняты очки, шапочка, ласты, лесенка, байдарка, шайба, бутса, самбовка, борцовки, мяч, нунчаки, эспандер, диск — их не брали)."""
import os, sys
from draw_icons import svg, s, eye, face, sparkle, O
W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=9, k=0.75, **kw: face(cx, cy, d=d, k=k, **kw)
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
R, OR, Y, G, B, P, V, BR, WH, GR, DK = ("#E8654F", "#FF9A3D", "#FFD25E", "#7CD26E", "#5CB7F2", "#FF8FB8", "#A98BF0",
                                        "#C0732E", "#FFFFFF", "#B8BCCB", "#2B2A44")
GOLD, WOOD, SKIN, LB, TQ = "#F2C14E", "#E8B06E", "#FFD9B8", "#BFE9FF", "#5CCDBA"
WAVE = f'<path d="M0 100 Q16 92 32 100 T64 100 T96 100 T128 100 V128 H0Z" fill="#7FD3F7" {W(2.6)}/>'
FLOOR = f'<path d="M0 104 Q64 96 128 104 V128 H0Z" fill="#E8C9A0" {W(2.6)}/>'
GRASS = f'<path d="M0 100 Q64 90 128 100 V128 H0Z" fill="#8FDB7A" {W(2.6)}/>'
sp = lambda *pts: "".join(sparkle(x, y, r) for x, y, r in pts)
rect = lambda x, y, w, h, c, rx=4, sw=None: f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{c}" {W(sw) if sw else s()}/>'
circ = lambda x, y, r, c, sw=None: f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" {W(sw) if sw else s()}/>'
ell = lambda x, y, rx, ry, c, sw=None: f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{c}" {W(sw) if sw else s()}/>'
path = lambda d, c="none", sw=None: f'<path d="{d}" fill="{c}" {W(sw) if sw else s()}/>'
line = lambda d, c, w: f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
txt = lambda x, y, t, size=12, c=O: f'<text x="{x}" y="{y}" font-family="Arial" font-weight="bold" font-size="{size}" text-anchor="middle" fill="{c}">{t}</text>'


def thick(d, c, w):
    return line(d, O, w + 3.2) + line(d, c, w)


I = {}
# ===================== Бассейны =====================
I["orbita-pool-zelenograd"] = ("sky", "сушилка-центрифуга для купальников",
    ell(64, 108, 34, 8, "#9AA7BF", 2.4) + path("M30 44 V104 Q64 116 98 104 V44Z", "#E9EEF7") +
    ell(64, 44, 34, 10, "#C9D2E3") + path("M44 34 Q64 20 84 34", sw=3) + rect(56, 26, 16, 6, R, 3, 2) +
    path("M48 46 Q50 70 58 74 Q64 76 70 74 Q78 70 80 46", "#FF8FB8", 2.4) + path("M56 46 Q64 54 72 46", sw=2) +
    f(64, 90, d=8, k=0.5) + "".join(line(d, "#7FD3F7", 2.6) for d in ["M14 70 Q20 64 14 58", "M114 70 Q108 64 114 58"]) +
    "".join(circ(x, y, 3, LB, 1.4) for x, y in [(110, 40), (18, 90)]) + sp((106, 22, 6)))
I["altufevsky-sk-pool"] = ("teal", "номерок гардероба",
    thick("M64 14 V30", GR, 3) + circ(64, 14, 5, GR, 2.2) +
    path("M64 30 L96 42 Q104 46 104 56 V96 Q104 112 88 112 H40 Q24 112 24 96 V56 Q24 46 32 42Z", "#C98A4B") +
    circ(64, 44, 6, "#9C6630", 2.2) + txt(64, 88, "125", 22, "#fff") + f(64, 66, d=8, k=0.55) + sp((22, 26, 6), (108, 24, 5)))
I["zhemchuzhina-pool-mitino"] = ("blue", "тест-набор для воды с пробиркой",
    rect(18, 70, 46, 40, "#FFFFFF", 6) + "".join(rect(24, 76 + i * 10, 34, 7, c, 2, 1.6)
                                                 for i, c in enumerate(["#FFE16B", "#FFB36B", "#FF7F7F"])) +
    path("M80 16 H100 V94 Q100 108 90 108 Q80 108 80 94Z", "#F2FBFF") + path("M80 60 H100 V94 Q100 108 90 108 Q80 108 80 94Z", "#FFB36B", 2.4) +
    rect(76, 12, 28, 8, B, 3, 2.4) + f(90, 82, d=4, k=0.32) + "".join(circ(x, y, 2.6, "#fff", 1.2) for x, y in [(88, 70), (94, 62)]) +
    sp((30, 30, 7), (60, 40, 5)))
I["grebnoy-kanal-pool"] = ("sky", "поворотный буй с флажком",
    WAVE + thick("M64 18 V64", GR, 3) + path("M66 18 L96 28 L66 38Z", R) +
    path("M38 70 Q38 52 64 52 Q90 52 90 70 Q90 98 64 100 Q38 98 38 70Z", OR) + path("M40 76 H88", sw=2.4) +
    path("M42 84 Q64 90 86 84", sw=2.4) + f(64, 66, d=8, k=0.55) +
    "".join(circ(x, y, 3, WH, 1.4) for x, y in [(22, 82), (108, 84)]) + sp((24, 30, 6)))
I["beskudnikovo-sk-pool"] = ("teal", "мокрые следы ног на кафеле",
    "".join(rect(x, y, 30, 30, c, 2, 1.4) for x in range(4, 128, 32) for y, c in [(4, "#E6FAF6"), (36, "#D2F3EC"), (68, "#E6FAF6"), (100, "#D2F3EC")]) +
    "".join(ell(x, y, 9, 14, "#7FD3F7", 2.4) + "".join(circ(x + dx, y - 18 + dy, 3, "#7FD3F7", 1.6)
            for dx, dy in [(-7, 2), (-2, -1), (3, -1), (7, 1), (10, 5)]) for x, y in [(44, 96), (82, 54)]) +
    f(44, 96, d=4, k=0.3) + f(82, 54, d=4, k=0.3) + "".join(circ(x, y, 3, WH, 1.4) for x, y in [(100, 96), (24, 40)]))
I["businovo-sk-pool"] = ("blue", "робот-пылесос для дна бассейна",
    WAVE.replace("100 Q", "40 Q").replace("V128", "V140") +
    path("M24 92 Q24 70 44 66 H84 Q104 70 104 92Z", "#FFD25E") + rect(18, 92, 92, 12, "#5A6278", 5) +
    "".join(circ(x, 106, 7, DK, 2) for x in (34, 64, 94)) + rect(46, 56, 36, 12, B, 5, 2.2) +
    thick("M64 56 Q66 30 92 20", "#4A90C8", 3) + f(64, 82, d=9, k=0.55) +
    "".join(circ(x, y, 3, WH, 1.4) for x, y in [(30, 54), (100, 52), (108, 40)]))
I["delfin-sk-nekrasovka"] = ("sky", "носовой зажим для плавания",
    WAVE + circ(64, 64, 38, SKIN) + path("M30 52 Q34 24 64 24 Q94 24 98 52 Q80 40 64 42 Q48 40 30 52Z", "#8A5A3C", 2.4) +
    eye(50, 60, 0.75) + eye(78, 60, 0.75) + path("M64 62 Q58 76 64 80 Q70 76 64 62", "#FFC4A0", 2.2) +
    rect(52, 70, 8, 10, "#3E8FD0", 3, 2) + rect(68, 70, 8, 10, "#3E8FD0", 3, 2) + path("M56 70 Q64 58 72 70", sw=2.4) +
    path("M58 88 Q64 92 70 88", sw=2.4) + ell(44, 76, 4.5, 2.6, "#FF7FA8", 0.1).replace(O, "none") + ell(84, 76, 4.5, 2.6, "#FF7FA8", 0.1).replace(O, "none") +
    "".join(circ(x, y, 3, WH, 1.4) for x, y in [(18, 34), (110, 36), (114, 50)]))
I["kuryanovo-fok-pool"] = ("teal", "перекидной счётчик кругов",
    WAVE + thick("M40 84 V108 M88 84 V108", GR, 3) + rect(24, 30, 80, 58, "#2E3A5C", 8) +
    rect(32, 38, 30, 42, "#fff", 4, 2.4) + rect(66, 38, 30, 42, "#fff", 4, 2.4) + line("M32 59 H62 M66 59 H96", O, 2) +
    txt(47, 72, "1", 30) + txt(81, 72, "4", 30) + f(64, 20, d=8, k=0.5, blush=False) + sp((112, 26, 6), (16, 30, 5)))
I["raduzhny-fok-pool"] = ("green", "медицинская справка в бассейн",
    path("M30 14 H86 L100 28 V112 H30Z", "#fff") + path("M86 14 V28 H100", "#E9EEF7", 2.4) +
    "".join(line(f"M40 {y} H{x}", GR, 3) for y, x in [(36, 76), (48, 90), (60, 84)]) +
    circ(78, 92, 13, "none", 2.4) + rect(74, 84, 8, 16, R, 1, 1.4) + rect(70, 88, 16, 8, R, 1, 1.4) +
    f(52, 84, d=7, k=0.48) + "".join(circ(x, y, 3, "#7FD3F7", 1.4) for x, y in [(112, 46), (18, 70)]) + sp((110, 24, 6)))

# ===================== Единоборства =====================
GI = lambda cx, c: (path(f"M{cx-12} 50 Q{cx} 44 {cx+12} 50 L{cx+16} 84 H{cx-16}Z", c) + circ(cx, 36, 12, SKIN) +
                    line(f"M{cx-14} 70 H{cx+14}", DK, 4))
I["rekord-zelenograd"] = ("orange", "японские сандалии гэта",
    FLOOR + "".join(path(f"M{x} 56 Q{x} 40 {x+18} 40 Q{x+36} 40 {x+36} 56 V96 Q{x+36} 104 {x+18} 104 Q{x} 104 {x} 96Z", WOOD) +
                    rect(x + 4, 104, 8, 10, "#B07A40", 2, 2) + rect(x + 24, 104, 8, 10, "#B07A40", 2, 2) +
                    thick(f"M{x+4} 70 Q{x+18} 52 {x+32} 70 M{x+18} 58 V48", R, 3) for x in (16, 76)) +
    f(34, 84, d=6, k=0.4) + f(94, 84, d=6, k=0.4) + sp((64, 24, 7), (112, 26, 5)))
I["beskudnikovo-borba"] = ("yellow", "борцовский ковёр с кругом",
    path("M10 70 L64 40 L118 70 L64 100Z", "#5CB7F2") + path("M28 70 L64 50 L100 70 L64 90Z", "#FFD25E", 2.4) +
    ell(64, 70, 22, 12, R, 2.4) + ell(64, 70, 6, 3.4, "#fff", 1.8) + path("M10 70 V78 L64 108 L118 78 V70 L64 100Z", "#3E8FD0") +
    f(64, 66, d=8, k=0.42).replace(O, "#fff") + sp((24, 30, 6), (106, 28, 5)))
I["fok-sash-korneychuka"] = ("pink", "двойная лапа-хлопушка тхэквондо",
    thick("M64 112 V80", "#2B2A44", 7) + path("M50 80 H78 L74 70 H54Z", "#2B2A44") +
    path("M54 70 Q30 64 28 36 Q28 18 46 18 Q60 18 62 34 L64 70Z", R) +
    path("M74 70 Q98 64 100 36 Q100 18 82 18 Q68 18 66 34 L64 70Z", "#FF8A73") + f(46, 40, d=5, k=0.38) +
    "".join(line(d, O, 2.4) for d in ["M20 26 L12 20", "M108 26 L116 20", "M18 44 H8", "M110 44 H120"]) + sp((106, 96, 6)))

# ===================== Футбол =====================
I["mfa-krasnoselskaya"] = ("green", "альбом с футбольными наклейками",
    path("M64 30 Q42 20 16 24 V104 Q42 100 64 110Z", "#fff") + path("M64 30 Q86 20 112 24 V104 Q86 100 64 110Z", "#fff") +
    "".join(rect(x, y, 16, 20, c, 2, 2) for x, y, c in [(24, 36, R), (42, 34, B), (24, 64, "#E9EEF7"), (42, 62, Y),
                                                         (72, 34, G), (90, 36, "#E9EEF7"), (72, 62, OR), (90, 64, P)]) +
    "".join(circ(x + 8, y + 8, 4, SKIN, 1.4) for x, y in [(24, 36), (42, 34), (42, 62), (72, 34), (72, 62), (90, 64)]) +
    path("M100 82 L112 72 L118 92 Z", "#FFE16B", 2) + f(64, 96, d=6, k=0.38, blush=False) + sp((112, 18, 5)))
I["mfa-entuziastov"] = ("blue", "мяч на резинке-привязи (тренажёр для ударов)",
    FLOOR + rect(14, 94, 30, 10, "#2B2A44", 5) + path("M30 94 Q50 30 82 52", sw=2.4) + line("M30 94 Q50 30 82 52", "#FFD25E", 1.6) +
    circ(90, 62, 22, "#fff") + path("M90 52 L99 58 L96 69 H84 L81 58Z", DK, 2) +
    "".join(line(d, O, 2) for d in ["M90 52 V42", "M99 58 L110 54", "M96 69 L102 80", "M84 69 L78 80", "M81 58 L70 54"]) +
    f(90, 62, d=0.1, k=0.01, mouth=False, blush=False) + eye(84, 72, 0.5) + eye(96, 72, 0.5) +
    "".join(line(d, WH, 3) for d in ["M58 72 L48 76", "M62 82 L52 90"]) + sp((24, 28, 6)))
I["smena-kapotnya"] = ("green", "дождеватель-спринклер для газона",
    GRASS + rect(54, 86, 20, 16, "#5A6278", 4) + thick("M64 86 V60", GR, 4) + rect(50, 52, 28, 10, "#FFD25E", 4, 2.4) +
    "".join(line(d, "#7FD3F7", 3.4) for d in ["M50 56 Q30 30 12 40", "M78 56 Q98 30 116 40", "M60 52 Q56 26 40 14", "M68 52 Q72 26 88 14"]) +
    "".join(circ(x, y, 3, "#7FD3F7", 1.4) for x, y in [(14, 54), (114, 54), (34, 22), (96, 22), (24, 70), (104, 70)]) +
    f(64, 94, d=5, k=0.34).replace(O, "#fff"))

# ===================== Регби =====================
I["rugby-petushkova"] = ("orange", "подставка-ти для удара по мячу",
    GRASS + path("M34 98 Q36 80 50 74 H78 Q92 80 94 98Z", "#FF8A3D") + path("M50 74 Q64 64 78 74", sw=2.4) +
    ell(64, 74, 14, 6, "#FFB36B", 2.4) + rect(56, 82, 16, 10, "#FFE16B", 3, 1.6) + f(64, 88, d=7, k=0.42) +
    path("M64 20 L68 32 L80 32 L70 40 L74 52 L64 44 L54 52 L58 40 L48 32 L60 32Z", Y, 2) + sp((22, 30, 6), (108, 34, 5)))
I["rugby-zelenograd"] = ("sky", "регбийные ворота в форме буквы Н",
    GRASS + thick("M40 104 V14 M88 104 V14", "#fff", 6) + thick("M40 60 H88", "#fff", 6) +
    rect(36, 80, 8, 24, R, 2, 2) + rect(84, 80, 8, 24, R, 2, 2) + f(64, 74, d=7, k=0.46) +
    path("M60 40 Q64 34 68 40", sw=2) + sp((106, 24, 6), (20, 30, 5)))

# ===================== Лёд и лёгкая атлетика =====================
I["spartak-hockey-sokolniki"] = ("blue", "круг вбрасывания на льду",
    path("M0 40 H128 V128 H0Z", "#EAF8FF", 2) + ell(64, 82, 46, 26, "none", 3) + f'<ellipse cx="64" cy="82" rx="46" ry="26" fill="none" stroke="#E8454F" stroke-width="3"/>' +
    circ(64, 82, 6, "#E8454F", 2) + "".join(line(d, "#E8454F", 3) for d in ["M50 70 V64 M78 70 V64", "M50 94 V100 M78 94 V100"]) +
    line("M0 46 H128", "#5CB7F2", 4) + f(64, 58, d=8, k=0.5) + sp((20, 22, 6), (108, 26, 5)))
I["znamenskie-manezh"] = ("purple", "планка для прыжков в высоту на стойках",
    FLOOR + rect(22, 26, 8, 80, GR, 2, 2.4) + rect(98, 26, 8, 80, GR, 2, 2.4) + rect(16, 102, 20, 6, DK, 2, 2) + rect(92, 102, 20, 6, DK, 2, 2) +
    "".join(line(f"M22 {y} H30 M98 {y} H106", O, 1.6) for y in range(36, 100, 10)) +
    rect(28, 48, 72, 8, "#fff", 3) + "".join(rect(x, 48, 8, 8, R, 1, 1.4) for x in (36, 52, 68, 84)) + f(64, 72, d=8, k=0.5) +
    path("M52 34 Q64 16 76 34", sw=2.4) + sp((112, 18, 6)))

# ===================== Танцы =====================
I["matsarr-ns-center"] = ("pink", "фрак на вешалке",
    thick("M64 12 Q72 12 72 20 Q72 26 64 28", GR, 2.4) + path("M30 40 L64 28 L98 40", sw=3) +
    path("M38 40 L64 30 L90 40 L96 72 L86 112 L74 74 H54 L42 112 L32 72Z", DK) +
    path("M54 34 L64 70 L74 34", "#fff", 2.4) + path("M58 40 L64 36 L70 40 L64 46Z", R, 1.8) + circ(64, 56, 2.4, "#fff", 1) +
    f(64, 92, d=7, k=0.4).replace(O, "#fff") + sp((18, 24, 6), (108, 30, 5), (110, 100, 4)))
I["matsarr-activity-hall"] = ("purple", "музыкальный автомат-джукбокс",
    path("M28 112 V52 Q28 18 64 18 Q100 18 100 52 V112Z", R) + path("M38 112 V54 Q38 28 64 28 Q90 28 90 54 V112Z", "#FFE16B", 2.4) +
    rect(44, 44, 40, 24, "#9DD6F5", 6, 2.4) + "".join(line(f"M{x} 74 V98", R, 4) for x in (50, 58, 66, 74)) +
    rect(46, 100, 36, 8, DK, 3, 2) + f(64, 56, d=8, k=0.5) +
    path("M108 30 V16 L118 14 V28", sw=2.2) + circ(106, 30, 3, O, 1) + circ(116, 28, 3, O, 1) + sp((16, 30, 6)))
I["matsarr-professional"] = ("night", "светящийся танцпол",
    "".join(path(f"M{64 + (i - j) * 15} {58 + (i + j) * 8} l15 8 l-15 8 l-15 -8Z", c, 2)
            for (i, j), c in zip([(a, b) for a in range(4) for b in range(4)],
                                 [P, Y, B, G, V, OR, TQ, P, G, R, Y, B, Y, B, P, TQ])) +
    f(64, 84, d=7, k=0.45) + "".join(line(d, "#FFF6C4", 2.4) for d in ["M30 20 L40 34", "M98 20 L88 34", "M64 12 V28"]) +
    sp((18, 46, 6), (110, 48, 5)))
I["zhavoronki-msk"] = ("yellow", "пучок-гулька с сеткой и шпильками",
    path("M30 116 Q30 92 64 90 Q98 92 98 116Z", P) + circ(64, 74, 26, SKIN) +
    path("M38 72 Q38 46 64 46 Q90 46 90 72 Q78 58 64 58 Q50 58 38 72Z", "#8A5A3C", 2.6) +
    circ(64, 34, 18, "#A06A44") + "".join(line(d, "#E9D7C5", 1.4) for d in ["M48 28 Q64 40 80 28", "M47 38 Q64 50 81 38", "M58 17 Q54 34 58 51", "M70 17 Q74 34 70 51"]) +
    circ(64, 34, 18, "none", 3) + thick("M40 22 L52 30", "#2B2A44", 2.2) + thick("M88 22 L76 30", "#2B2A44", 2.2) +
    circ(40, 22, 3, R, 1.4) + circ(88, 22, 3, R, 1.4) + f(64, 78, d=9, k=0.55) + sp((110, 70, 6), (18, 70, 5)))

if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        bg, subj, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(bg, body))
    print("svg:", len(ids))
