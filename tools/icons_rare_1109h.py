"""Иконки робота rare, 2026-11-09 (22 UTC) — места из tools/add_rare_1109h.py.
Просмотрены все 56 листов icons-catalog (сводками по 6) и реестр subjects.txt: у картингов уже заняты карт-персонажи
с аксессуарами, звери за рулём, малыш с «пончиком», вид сверху со змейкой; у цирка — силач, пудель, акробат в стойке,
клоунский башмак и гудок. Каждая иконка ниже придумана отдельно: свой герой, сцена, ракурс и палитра.
Запуск: python3 tools/icons_rare_1109h.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, eye, face, sparkle, O
from icons_sections_1107c import G
from icons_sections_1108g import rect, circ, ell, path, SKIN

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
draw_icons.BG.update({
    "rh_rose": ("#FFF0F6", "#E879A8"), "rh_lime": ("#FBFFE8", "#B6D94C"), "rh_cobalt": ("#EAF3FF", "#3E7BD6"),
    "rh_lagoon": ("#E6FFFB", "#22A6A0"), "rh_peach": ("#FFF3EA", "#F2995E"), "rh_violet": ("#F6EEFF", "#8A5CD6"),
    "rh_stage": ("#5B4B9E", "#1F1B4A"),
})


def add(pid, bg, body, hero, scene):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def line(d, c, sw):
    return path(d, "none", sw).replace(O, c, 1)


def tyre(x, y, r=11):
    return circ(x, y, r, "#2E2A3E", 2.6) + circ(x, y, r * 0.42, "#B9B4C8", 2)


# 1. ЕвроПарк — малышка в розовом шлеме с хвостиками в мятном круглом карте анфас, за ней след из сердечек по спирали
hearts = "".join(
    path(f"M{x} {y+3} q-6 -5 -3 -8 q3 -2 3 2 q0 -4 3 -2 q3 3 -3 8Z", c, 1.6)
    for x, y, c in [(20, 30, "#FF6F9C"), (34, 18, "#FF8FB4"), (52, 12, "#FFB0CA"), (100, 26, "#FF6F9C"), (110, 44, "#FF8FB4")])
k1 = (tyre(28, 100, 12) + tyre(100, 100, 12)
      + path("M26 78 Q64 60 102 78 L108 104 Q64 116 20 104Z", "#5FD6B4", 3)
      + rect(46, 92, 36, 8, "#2B8F76", 4, 2.2) + circ(64, 84, 9, "#3B3355", 2.4) + circ(64, 84, 3, "#FFD34D", 1.4)
      + ell(64, 56, 22, 21, "#FF7FB0", 3) + path("M44 54 Q64 40 84 54 L84 62 H44Z", "#FF9CC4", 0)
      + ell(64, 62, 15, 11, SKIN, 2.4) + face(64, 60, d=6, k=0.75)
      + path("M41 52 Q30 50 30 62 Q34 58 40 60Z", "#8A5A3C", 2.2) + path("M87 52 Q98 50 98 62 Q94 58 88 60Z", "#8A5A3C", 2.2))
add("crazy-cart-europark", "rh_rose", hearts + k1,
    "малышка в розовом шлеме с торчащими каштановыми хвостиками в мятном круглом дрифт-карте (анфас)",
    "едет прямо на зрителя, а за спиной по спирали тянется след из розовых сердечек")

# 2. «Весна» — девочка в жёлтом шлеме с ромашкой развернулась на сиденье назад и машет рукой; лимонный карт сбоку
daisy = "".join(ell(0, -5, 2.6, 5, "#FFFFFF", 1.2).replace('cx="0"', 'cx="0"') for _ in range(1))
petals = "".join(G(0, 0, ell(0, -6, 2.6, 5, "#FFFFFF", 1.2), a, 1) for a in range(0, 360, 60)) + circ(0, 0, 3, "#FFC93C", 1.2)
k2 = (tyre(30, 102, 12) + tyre(96, 102, 12)
      + path("M14 92 Q16 78 34 78 L96 78 Q114 80 116 94 L112 100 H16Z", "#F2E046", 3)
      + rect(18, 90, 92, 6, "#C9B520", 3, 0)
      + path("M60 80 L56 60 Q58 54 66 54 L72 80Z", "#3B3355", 2.4)
      + path("M48 62 Q40 50 34 40", "none", 3) + circ(33, 37, 5, SKIN, 2.2)
      + ell(64, 46, 17, 16, "#FFD23C", 3) + ell(64, 51, 11, 8, SKIN, 2.2) + face(64, 50, d=5, k=0.65)
      + G(74, 34, petals, 0, 1))
add("crazy-cart-vesna", "rh_lime", k2 + sparkle(102, 30, 5),
    "девочка в жёлтом шлеме с наклейкой-ромашкой на лимонном дрифт-карте (вид сбоку)",
    "развернулась на сиденье задом наперёд и машет рукой тем, кто едет сзади")

# 3. «Город Косино» — красный шлем-персонаж с глазами в визоре выглядывает из-за руля, крупный план кокпита
k3 = (path("M6 128 L14 96 Q64 82 114 96 L122 128Z", "#2F6FD0", 3)
      + ell(64, 52, 32, 30, "#E8353B", 3.2) + path("M38 46 Q64 30 90 46 L90 60 Q64 66 38 60Z", "#2B2F4A", 2.6)
      + eye(54, 52, 1.0) + eye(74, 52, 1.0)
      + line("M44 40 Q52 34 60 33", "#FFFFFF", 2.6)
      + path("M60 22 h8 v8 h-8z", "#FFFFFF", 1.6)
      + circ(64, 100, 24, "none", 7).replace(O, "#3B3355", 1) + rect(40, 96, 48, 8, "#3B3355", 4, 2)
      + circ(64, 100, 6, "#FFD34D", 2) + path("M18 106 h6 M104 106 h6", "none", 3))
add("crazy-cart-kosino", "rh_cobalt", k3,
    "красный гоночный шлем-персонаж с глазами за тёмным визором",
    "осторожно выглядывает поверх руля синего карта, крупный план кокпита")

# 4. «РИО» с океанариумом — мальчик в маске для ныряния с трубкой вместо шлема, голубой карт, вокруг пузыри
bubbles = "".join(circ(x, y, r, "#E9FBFF", 1.8) + circ(x - r * .35, y - r * .35, r * .25, "#FFFFFF", 0)
                  for x, y, r in [(16, 70, 5), (22, 52, 7), (36, 34, 5), (100, 34, 6), (112, 54, 4), (110, 74, 7)])
k4 = (tyre(34, 104, 12) + tyre(96, 104, 12)
      + path("M14 96 Q18 82 38 82 L92 82 Q112 84 114 98 L110 104 H18Z", "#3FB5F0", 3)
      + ell(64, 58, 19, 19, SKIN, 3) + path("M45 52 Q64 42 83 52 L82 66 Q64 72 46 66Z", "#FFB23C", 2.6)
      + ell(64, 58, 15, 8, "#BFF3FF", 2.2) + eye(58, 58, 0.7) + eye(70, 58, 0.7)
      + line("M84 52 Q92 44 90 30", "#FF6F3C", 4) + path("M60 70 Q64 74 68 70", "none", 2.4)
      + path("M46 44 Q64 30 82 44", "#5A3A26", 2.4))
add("crazy-cart-rio-dmitrovka", "rh_lagoon", bubbles + k4,
    "мальчик в оранжевой маске для ныряния с трубкой вместо шлема на голубом дрифт-карте",
    "кружится, а вместо дыма из-под колёс поднимаются пузыри, как в аквариуме")

# 5. «Кузьминки Молл» — двое ребят на оранжевом и фиолетовом мини-картах кружат друг за другом по пунктирной петле
loop = path("M20 64 Q20 26 64 26 Q108 26 108 64 Q108 102 64 102 Q20 102 20 64Z", "none", 2).replace(
    'stroke-width', 'stroke-dasharray="6 6" stroke-width', 1)


def mini(c, helm):
    return (circ(-12, 10, 6, "#2E2A3E", 2) + circ(12, 10, 6, "#2E2A3E", 2)
            + path("M-20 6 Q-18 -4 -6 -4 L14 -4 Q22 -2 22 8 H-20Z", c, 2.6)
            + ell(0, -14, 9, 9, helm, 2.4) + ell(1, -11, 6, 4, SKIN, 1.6) + face(1, -12, d=3, k=0.42, blush=False))


k5 = (loop + G(42, 34, mini("#FF8A2B", "#2FB36A"), 12, 1.3)
      + f'<g transform="translate(86 96) rotate(-12) scale(-1.3 1.3)">{mini("#8E5BE0", "#FFC93C")}</g>')
add("crazy-cart-kuzminki-mall", "rh_peach", k5 + sparkle(64, 64, 7),
    "двое ребят — в зелёном и жёлтом шлемах — на оранжевом и фиолетовом мини-картах",
    "гоняются друг за другом по пунктирной петле, не догоняя, как стрелки часов")

# 6. Цирковая студия «Радуга» — девочка-жонглёр в фиолетовом трико, над головой дуга из семи колец цветов радуги
rings = "".join(circ(x, y, 7.5, "none", 3.2).replace(O, c, 1)
                for (x, y), c in zip([(26, 58), (32, 38), (46, 24), (64, 18), (82, 24), (96, 38), (102, 58)],
                                     ["#E8353B", "#FF8A2B", "#FFD23C", "#3CC46A", "#3FB5F0", "#3E5BD6", "#9C5BE0"]))
girl = (path("M52 118 L56 92 H72 L76 118", "#7E4BD0", 3) + path("M50 92 Q64 70 78 92Z", "#9C6BE8", 3)
        + line("M54 80 Q40 72 30 62", "#FFD8B8", 4.5) + line("M74 80 Q88 72 98 62", "#FFD8B8", 4.5)
        + circ(64, 66, 12, SKIN, 3) + face(64, 66, d=5, k=0.65)
        + path("M52 62 Q54 50 64 50 Q74 50 76 62 Q70 56 64 56 Q58 56 52 62Z", "#C0392B", 2.4)
        + ell(64, 120, 28, 6, "#FFE36B", 2.4))
add("circus-raduga-dshi-centr", "rh_violet", rings + girl,
    "девочка-жонглёр в фиолетовом трико с рыжей чёлкой",
    "подбросила семь колец, и они встали над её головой дугой-радугой")

# 7. Школа цирка им. Никулина — мальчик балансирует на доске-ролла-болла на цилиндре посреди красного манежа под софитами
beams = (path("M24 -4 L48 96 L70 96Z", "#FFF6C4", 0).replace('fill="#FFF6C4"', 'fill="#FFF6C4" opacity=".35"')
         + path("M104 -4 L58 96 L82 96Z", "#FFF6C4", 0).replace('fill="#FFF6C4"', 'fill="#FFF6C4" opacity=".35"'))
arena = (ell(64, 108, 54, 16, "#D62E3A", 3) + ell(64, 106, 44, 11, "#F3D9A4", 2.4)
         + "".join(circ(x, 108 + (0 if abs(x - 64) < 30 else -4), 2, "#FFD34D", 0) for x in range(20, 112, 12)))
boy = (ell(64, 92, 9, 9, "#8B5A2B", 2.8) + rect(40, 80, 48, 6, "#3B88D6", 2, 2.6)
       + line("M58 80 L56 64 M70 80 L72 64", "#2B2F4A", 4.5)
       + path("M54 64 L54 46 Q64 40 74 46 L74 64Z", "#FFC93C", 2.8)
       + line("M54 50 Q42 46 34 40", "#FFD8B8", 4) + line("M74 50 Q86 46 94 40", "#FFD8B8", 4)
       + circ(64, 32, 11, SKIN, 3) + face(64, 32, d=5, k=0.6) + path("M53 28 Q56 18 64 18 Q74 18 76 28 Q68 24 53 28Z", "#2B2F4A", 2.2))
add("circus-school-nikulin", "rh_stage", beams + arena + boy + sparkle(22, 30, 5) + sparkle(108, 22, 4),
    "мальчик-эквилибрист в жёлтой рубашке, руки в стороны",
    "балансирует на доске, лежащей на катушке-цилиндре (ролла-болла), посреди красного манежа под двумя софитами")


if __name__ == "__main__":
    for pid, body in ICONS.items():
        open(os.path.join(OUT, f"{pid}.svg"), "w").write(body)
    reg = os.path.join(OUT, "subjects.txt")
    lines = open(reg).read().splitlines()
    keep = [l for l in lines if l.split(" — ")[0] not in SUBJ]
    open(reg, "w").write("\n".join(keep + list(SUBJ.values())) + "\n")
    print(len(ICONS), "иконок")
