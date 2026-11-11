"""Иконки робота rare, 2026-11-11 (10 UTC) — места из tools/add_rare_1111e.py.
Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно. Перед рисованием просмотрены все листы icons-catalog
и реестр subjects.txt (grep: карт, дрифт, скейт, самокат, BMX, памп-трек, радуга, корона, борода). Свободны: двухместный
карт «папа + малыш», мальчик-король на дрифт-карте, девочка на самокате по радуге-рампе, бородатый скейтборд в чаше.
Запуск: python3 tools/icons_rare_1111e.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, face, sparkle, eye, O, s
from icons_sections_1108g import rect, circ, ell, path

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}


def add(pid, pal, body, hero, scene):
    k = f"r11e_{pid}"
    draw_icons.BG[k] = pal
    ICONS[pid] = svg(k, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def mouth(x, y, w=4, sw=2.2):
    return f'<path d="M{x-w} {y} Q{x} {y+w*0.9} {x+w} {y}" fill="none" stroke="{O}" stroke-width="{sw}" stroke-linecap="round"/>'


def blush(x, y, rx=2.8, ry=1.7):
    return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#FF7FA8" opacity=".7"/>'


# 1. GS Racing (Лесной) — открытая трасса, двухместный карт «взрослый + ребёнок»:
#    папа в синем шлеме ведёт широкий карт, рядом малыш-пассажир в жёлтом шлеме машет рукой; позади сосны и фонарь трассы
pines = (path("M8 84 L18 56 L28 84Z", "#2F8F5B", 2.4) + path("M22 84 L30 62 L38 84Z", "#3BA56A", 2.4)
         + path("M96 84 L106 52 L116 84Z", "#2F8F5B", 2.4))
lamp = (path("M86 84 V30", "none", 2.6) + path("M86 30 H96", "none", 2.6)
        + path("M92 30 L100 30 L98 36 L94 36Z", "#FFE680", 2.0)
        + '<path d="M96 38 L90 54 L104 54Z" fill="#FFF6B0" opacity=".55"/>')
track = ('<rect x="-4" y="84" width="136" height="48" fill="#5A6170"/>'
         '<path d="M-4 122 H132" stroke="#E23B3B" stroke-width="4" stroke-dasharray="9 9"/>'
         '<path d="M-4 122 H132" stroke="#fff" stroke-width="4" stroke-dasharray="9 9" stroke-dashoffset="9"/>')
twin = (
    circ(26, 104, 12, "#2B2B3A", 3.0) + circ(26, 104, 4.5, "#BFC6D1", 2.0)
    + path("M8 100 L14 88 H40 L46 92 H92 L104 86 H118 L124 96 L120 102 H10Z", "#2C5BD8", 3.0)   # широкое шасси
    + path("M14 88 L18 80 H96 L104 86", "#4A7BF0", 2.6)                                           # борт на двоих
    + circ(106, 105, 11, "#2B2B3A", 3.0) + circ(106, 105, 4.2, "#BFC6D1", 2.0)
)
dad = (
    rect(30, 60, 24, 24, "#F2F2F2", 8, 2.8)                                                       # куртка
    + circ(42, 46, 14, "#2C5BD8", 3.0)                                                            # шлем
    + path("M30 44 Q42 36 55 44 V50 H30Z", "#1E2A44", 0)                                          # визор поднят: тёмная полоса
    + ell(44, 52, 9, 7, "#FFD7B5", 2.2)                                                           # лицо в проёме
    + eye(40, 51, 0.45) + eye(48, 51, 0.45) + mouth(44, 55, 2.6, 1.8)
    + path("M52 70 Q60 72 66 66", "none", 3.0)                                                    # рука к рулю
    + path("M66 60 L70 74", "none", 3.2) + ell(68, 59, 3.5, 7, "#2B2B3A", 2.2)                    # руль
)
kid = (
    rect(72, 68, 18, 16, "#FF8A3D", 7, 2.6)                                                       # курточка
    + circ(81, 58, 10.5, "#FFD23F", 2.8)                                                          # жёлтый шлем
    + path("M72 57 Q81 51 90 57 V61 H72Z", "#1E2A44", 0)
    + ell(82, 63, 7, 5.6, "#FFD7B5", 2.0)
    + eye(79, 62, 0.38) + eye(85, 62, 0.38) + mouth(82, 65.5, 2.0, 1.6) + blush(76.5, 65, 1.8, 1.1) + blush(87.5, 65, 1.8, 1.1)
    + path("M89 72 Q98 64 100 52", "none", 3.0) + circ(100, 50, 3.2, "#FFD7B5", 2.0)              # машет рукой
)
add("karting-gs-racing-lesnoy", ("#EAF8FF", "#5BA7D9"),
    pines + lamp + track + twin + dad + kid
    + '<path d="M0 66 H10 M-2 74 H6" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".9"/>'
    + sparkle(22, 26, 4.5) + sparkle(60, 18, 3),
    "широкий синий двухместный карт: папа в синем шлеме за рулём и малыш в жёлтом шлеме на соседнем сиденье",
    "едут по открытой вечерней трассе среди сосен под фонарём освещения, малыш машет рукой")

# 2. «Король Дрифта» (Коломна) — мальчик-король: золотая корона поверх красного шлема, красная мантия с горностаем
#    развевается; ведёт жёлтый дрифт-карт боком по дуге, за ним — полукольцо белого дыма
smoke = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFFFFF" opacity=".85" stroke="{O}" stroke-width="1.8"/>'
                for x, y, r in ((18, 96, 9), (14, 80, 7), (20, 66, 6), (30, 56, 5), (28, 108, 7)))
floor = ('<ellipse cx="66" cy="104" rx="58" ry="16" fill="#5B3F8C" opacity=".45"/>'
         '<path d="M14 106 Q30 118 66 118 Q104 118 120 104" fill="none" stroke="#2B2B3A" stroke-width="4" opacity=".55"/>')
cart = (
    '<g transform="rotate(-8 66 96)">'
    + circ(32, 102, 13, "#2B2B3A", 3.0) + circ(32, 102, 5, "#BFC6D1", 2.0)                       # заднее колесо
    + path("M14 98 L20 86 H48 L54 92 H86 L98 84 H114 L120 94 L116 102 H18Z", "#FFC93C", 3.0)       # низкое шасси карта
    + path("M98 84 L106 76 H116 L114 84", "#F0A22A", 2.6)                                          # обтекатель носа
    + path("M20 90 H44", "none", 2.0)                                                              # бампер-полоса
    + circ(104, 104, 11, "#2B2B3A", 3.0) + circ(104, 104, 4.5, "#BFC6D1", 2.0)                     # переднее колесо
    + path("M80 88 L86 70", "none", 3.0)                                                           # рулевая колонка
    + '</g>'
)
cape = path("M48 60 Q30 66 22 84 Q36 80 46 84 Z", "#D9314A", 2.8) + \
    ''.join(f'<circle cx="{x}" cy="{y}" r="1.6" fill="{O}"/>' for x, y in ((30, 79), (37, 76), (43, 79)))
cape = path("M50 60 Q30 62 20 80 Q26 84 34 80 Q38 84 46 82 L54 70Z", "#D9314A", 2.8) + \
    path("M20 80 Q26 84 34 80 Q38 84 46 82", "#FFFFFF", 2.4) + \
    ''.join(f'<circle cx="{x}" cy="{y}" r="1.4" fill="{O}"/>' for x, y in ((26, 82), (34, 81), (42, 82)))
king = (
    cape
    + rect(52, 58, 22, 22, "#D9314A", 8, 2.8)                                                     # кафтан
    + path("M52 64 H74", "#FFFFFF", 2.0)
    + circ(63, 42, 14, "#E23B3B", 3.0)                                                            # красный шлем
    + ell(65, 46, 9.5, 8, "#FFD7B5", 2.2)
    + eye(61, 45, 0.48) + eye(69, 45, 0.48) + mouth(65, 50, 3.0, 1.9) + blush(57.5, 49) + blush(72.5, 49)
    + path("M51 30 L54 18 L59 26 L63 14 L67 26 L72 18 L75 30Z", "#FFD23F", 2.6)                   # корона поверх шлема
    + circ(63, 14, 2.2, "#E23B3B", 1.4) + circ(54, 18, 1.8, "#4FB3E8", 1.2) + circ(72, 18, 1.8, "#4FB3E8", 1.2)
    + path("M74 70 Q80 72 84 70", "none", 3.0) + ell(86, 68, 3.5, 7, "#2B2B3A", 2.2)               # руки на руле
)
add("karting-drift-king-kolomna", ("#F3E9FF", "#8A5CD1"),
    floor + smoke + '<g transform="translate(0 12)">' + king + '</g>' + cart + sparkle(104, 28, 5) + sparkle(92, 46, 3) + sparkle(24, 30, 3.5),
    "мальчик-король в маленькой золотой короне поверх красного шлема и в красной мантии с горностаевой опушкой",
    "ведёт жёлтый дрифт-карт боком по дуге, мантия развевается, позади клубится полукольцо белого дыма")

# 3. «Движ» (Раменское, ТЦ «Радуга») — радуга, изогнутая как рампа-полутруба; по её внутренней дуге
#    катится девочка на трюковом самокате в бирюзовом шлеме
bands = (("#E84A5F", 0), ("#FF9A3C", 7), ("#FFD23F", 14), ("#5CCB6F", 21), ("#4FA3E8", 28), ("#8A6CE0", 35))
rainbow = ''.join(
    f'<path d="M{6+o} 34 Q{6+o} {118-o} 64 {118-o} Q{122-o} {118-o} {122-o} 34" fill="none" stroke="{c}" stroke-width="7.5"/>'
    for c, o in bands)
rainbow += ('<path d="M2.5 34 Q2.5 121.5 64 121.5 Q125.5 121.5 125.5 34" fill="none" stroke="#3B3355" stroke-width="2.4"/>'
            '<path d="M44.5 34 Q44.5 79.5 64 79.5 Q83.5 79.5 83.5 34" fill="none" stroke="#3B3355" stroke-width="2.4"/>')
scooter = (
    '<g transform="rotate(28 82 92)">'
    + path("M60 98 H96", "none", 4.0)                                                             # дека
    + path("M94 98 L92 66", "none", 3.2) + path("M86 66 H98", "none", 3.2)                        # стойка и руль
    + circ(62, 103, 4.5, "#FFFFFF", 2.4) + circ(94, 103, 4.5, "#FFFFFF", 2.4)
    + '</g>'
)
girl = (
    '<g transform="rotate(28 82 92)">'
    + path("M70 96 L72 84 M80 96 L78 84", "none", 3.2)                                            # ноги
    + rect(66, 66, 18, 20, "#FF6FA8", 7, 2.6)                                                     # кофта
    + path("M82 72 Q88 70 92 67", "none", 3.0)                                                    # рука на руле
    + path("M66 54 Q58 58 56 66 Q60 64 64 62Z", "#7A4A2A", 2.0)                                   # хвостик развевается
    + circ(75, 54, 10, "#FFD7B5", 2.6)
    + path("M64 52 Q66 40 76 40 Q86 40 86 52 Q76 47 64 52Z", "#2CC1B0", 2.6)                      # бирюзовый шлем
    + eye(72, 55, 0.42) + eye(79, 55, 0.42) + mouth(76, 59, 2.4, 1.8) + blush(69, 58.5, 1.9, 1.2) + blush(82.5, 58.5, 1.9, 1.2)
    + '</g>'
)
add("skate-dvij-ramenskoe", ("#EFFBFF", "#7CC7EE"),
    rainbow + '<ellipse cx="78" cy="113" rx="13" ry="2.6" fill="#000" opacity=".15"/>' + scooter + girl
    + '<path d="M36 70 Q40 84 50 92" fill="none" stroke="#fff" stroke-width="2.6" stroke-dasharray="3 5" stroke-linecap="round"/>'
    + sparkle(64, 22, 6) + sparkle(98, 20, 3.5) + sparkle(30, 18, 3),
    "девочка в бирюзовом шлеме и розовой кофте на трюковом самокате",
    "скатывается по внутренней дуге радуги, изогнутой как рампа-полутруба, за ней пунктирный след")

# 4. «Борода» (Каширское ш.) — сам скейтборд с пышной рыжей бородой и усами под мордашкой катится вниз
#    по бортику серой бетонной чаши крытого скейт-парка
bowl = (path("M-4 40 Q8 104 64 108 Q120 104 132 40 V132 H-4Z", "#9AA3B2", 3.0)
        + path("M-4 40 Q8 104 64 108 Q120 104 132 40", "none", 4.2)
        + '<path d="M10 70 Q30 98 64 101" fill="none" stroke="#C8CED8" stroke-width="2.4"/>'
        + '<path d="M-4 38 H18 M110 38 H132" stroke="#E8ECF2" stroke-width="5"/>')
board = (
    '<g transform="rotate(24 64 92)">'
    + path("M22 92 Q16 92 14 86 M106 86 Q104 92 98 92", "none", 3.6)                             # загнутые носы деки
    + path("M18 88 Q20 94 28 94 H100 Q108 94 110 88 L106 86 Q104 90 98 90 H30 Q22 90 22 86Z", "#2E9E6A", 3.0)
    + path("M34 96 H46 M82 96 H94", "none", 3.0)                                                 # подвески
    + circ(40, 103, 7, "#FFE66B", 2.8) + circ(88, 103, 7, "#FFE66B", 2.8)                        # колёса
    + path("M50 88 L54 70 M74 88 L70 70", "none", 3.4)                                           # ноги
    + path("M48 88 H58 M66 88 H78", "none", 4.2)                                                 # кеды
    + rect(50, 46, 24, 26, "#4FA3E8", 8, 2.8)                                                    # голубая футболка
    + path("M50 54 Q38 50 32 40 M74 54 Q86 52 94 44", "none", 3.2)                               # руки для баланса
    + circ(62, 30, 12, "#FFD7B5", 2.8)
    + path("M50 28 Q50 14 62 14 Q74 14 74 28 Q62 22 50 28Z", "#E23B3B", 2.6)                     # красный шлем
    + eye(57, 29, 0.5) + eye(67, 29, 0.5)
    + path("M51 34 Q50 52 62 56 Q74 52 73 34 Q68 38 62 37 Q56 38 51 34Z", "#E8893A", 2.4)        # накладная рыжая борода
    + path("M56 40 Q57 48 60 52 M68 40 Q67 48 64 52", "none", 1.4)
    + path("M55 35 Q62 31 69 35", "none", 2.0)                                                   # усы
    + path("M50 33 L46 26 M74 33 L78 26", "none", 1.4)                                           # резинка бороды
    + '</g>'
)
add("skate-boroda-kashirskoe", ("#FFF7E0", "#F2B84B"),
    bowl + '<path d="M104 30 Q112 40 110 52" fill="none" stroke="#fff" stroke-width="2.6" stroke-dasharray="3 5" stroke-linecap="round"/>'
    + board + sparkle(22, 24, 5) + sparkle(100, 16, 3.5),
    "малыш в красном шлеме с накладной рыжей бородой на резинке",
    "скатывается на зелёном скейтборде по бортику серой бетонной чаши крытого скейт-парка, раскинув руки для баланса")

if __name__ == "__main__":
    reg = os.path.join(OUT, "subjects.txt")
    have = open(reg, encoding="utf-8").read()
    lines = []
    for pid, code in ICONS.items():
        open(os.path.join(OUT, f"{pid}.svg"), "w").write(code)
        if f"\n{pid} — " not in "\n" + have:
            lines.append(SUBJ[pid])
    if lines:
        with open(reg, "a", encoding="utf-8") as f:
            f.write(("" if have.endswith("\n") else "\n") + "\n".join(lines) + "\n")
    print(len(ICONS), "icons;", len(lines), "registry lines")
