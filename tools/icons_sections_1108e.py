"""Иконки робота sections, 2026-11-08 (15 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно —
свой герой, своя сцена, своя компоновка и палитра. Сверено со всеми листами icons-catalog/sheet-01…38 и subjects.txt
(в футболе уже заняты: мяч-персонаж на сцене/в воротах/с медалью/в луче прожектора, сетка ворот, бутсы, гетры, шорты,
фишка, свисток, флажок, табло, прожектор, тактическая доска, карточки, насос, капитанская повязка, вратарь-девочка в
прыжке, мальчик в «ножницах», бегущий мальчик с номером 9). Новые футбольные сюжеты — ниже, каждый свой.
Запуск: python3 tools/icons_sections_1108e.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O
from icons_sections_1107c import G
from icons_sections_1108b import limb, head, soccer

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
SKIN = "#FFD8B8"
draw_icons.BG.update({
    "e_hug": ("#FFFBE0", "#F2C94C"), "e_pen": ("#F1FFE9", "#6FCF6A"), "e_glove": ("#F6ECFF", "#9B6FD6"),
    "e_dome": ("#EAF4FF", "#5C8FD6"), "e_jug": ("#FFF1E8", "#F0956A"), "e_slal": ("#E9FFF8", "#3FBFA0"),
    "e_corgi": ("#EFFAFF", "#7EC8E8"), "e_boots": ("#FBF0FF", "#C58BE0"), "e_rain": ("#F2F7EE", "#93B57A"),
    "e_pass": ("#FFF8EC", "#E3B25C"), "e_head": ("#F3FFF2", "#8FD18A"), "e_wall": ("#FFF3EA", "#EE9F6E"),
    "e_corner": ("#F5FFEF", "#5DAE52"), "e_throw": ("#FFF0F0", "#E77F7F"), "e_slide": ("#FFEFF7", "#E07AB3"),
    "e_dad": ("#E8FBF9", "#4DB6AC"), "e_dalm": ("#FFFDF4", "#D8C27A"),
    "e_step": ("#E8FFFE", "#33B8C4"), "e_lift": ("#EEF1FF", "#6F7FD6"), "e_bridge": ("#FFF0F4", "#E86A8E"),
    "e_jump": ("#FFF9E5", "#E8B547"), "e_bow": ("#FFFBEF", "#C9A15A"), "e_bat": ("#F0F6FF", "#4F7BC4"),
    "e_catch": ("#F7F2EA", "#B08A5E"), "e_acro": ("#FFF6FB", "#C772C9"), "e_ski": ("#F4FBFF", "#9CC6EA"),
    "e_board": ("#FFF4E6", "#F08C3A"), "e_tbar": ("#EAF7F0", "#6BA884"),
})


def add(pid, bg, body, hero, scene):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def grass(y=104, c="#7CC66A"):
    return f'<rect x="-6" y="{y}" width="140" height="40" fill="{c}" {W(2.6)}/>'


def shirt(x, y, w, h, c, rx=5):
    return f'<rect x="{x - w/2}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{c}" {W(2.8)}/>'


def cone(x, y, c="#FF8A3D"):
    return f'<path d="M{x-6} {y} L{x} {y-12} L{x+6} {y}Z" fill="{c}" {W(2.2)}/>'


# ============================== ФУТБОЛ «ЧЕМПИОНИКА» ==============================
add("championika-butovo-park", "e_hug",
    grass(106)
    + soccer(72, 70, 34)
    + shirt(26, 64, 20, 26, "#7FC8F8", 7)
    + limb("M20 90 L18 104", "#7FC8F8", 6) + limb("M32 90 L34 104", "#7FC8F8", 6)
    + head(26, 52, "#E0A25A", r=11, k=0.42)
    + limb("M34 70 Q52 66 58 78", SKIN, 5) + limb("M32 80 Q50 94 62 92", SKIN, 5)
    + f'<path d="M100 30 l4 -6 M108 36 l6 -3" {W(2.4)}/>',
    "малыш-трёхлетка в голубом комбинезоне",
    "обнимает обеими руками футбольный мяч больше себя, стоя на траве")

add("championika-kulikovskaya", "e_pen",
    grass(100)
    + f'<path d="M14 100 V34 H114 V100" fill="none" stroke="#fff" stroke-width="7" stroke-linejoin="round"/>'
    + f'<path d="M14 100 V34 H114 V100" fill="none" {W(1.6)}/>'
    + G(36, 76, shirt(0, -8, 30, 16, "#FFD23F", 6) + limb("M-14 0 L-26 -10", SKIN, 5) + limb("M14 0 L24 8", "#3B5BA8", 5)
        + limb("M14 -4 L26 -2", "#3B5BA8", 5), rot=-20)
    + head(18, 64, "#5A3A2A", r=10, k=0.38)
    + soccer(96, 48, 12, fc=False)
    + f'<path d="M84 60 l-8 6 M80 52 l-9 1" {W(2.2)}/>',
    "вратарь-малыш в жёлтой кофте",
    "прыгнул в левый угол ворот, а мяч влетает в правый")

add("championika-butovo-mall", "e_glove",
    soccer(64, 66, 22, fc=False)
    + G(32, 66, f'<path d="M-14 -26 Q-2 -34 10 -22 L12 22 Q0 32 -14 24Z" fill="#43C26A" {W(3)}/>'
        + f'<path d="M-10 -16 L6 -16 M-10 -4 L8 -4 M-10 8 L8 8" {W(2)}/>' + face(-3, 14, d=4.5, k=0.42), rot=-8)
    + G(96, 66, f'<path d="M14 -26 Q2 -34 -10 -22 L-12 22 Q0 32 14 24Z" fill="#43C26A" {W(3)}/>'
        + f'<path d="M10 -16 L-6 -16 M10 -4 L-8 -4 M10 8 L-8 8" {W(2)}/>' + face(3, 14, d=4.5, k=0.42), rot=8)
    + f'<rect x="20" y="92" width="22" height="12" rx="3" fill="#2F2A44" {W(2.4)}/>'
    + f'<rect x="86" y="92" width="22" height="12" rx="3" fill="#2F2A44" {W(2.4)}/>'
    + sparkle(64, 28, 7) + sparkle(30, 26, 4) + sparkle(100, 24, 5),
    "пара зелёных вратарских перчаток с мордочками",
    "крепко сжали пойманный мяч с двух сторон, над ними искорки")

add("championika-shchipok", "e_dome",
    f'<rect x="-6" y="98" width="140" height="40" fill="#DDE8F5" {W(2.6)}/>'
    + f'<path d="M10 100 Q64 8 118 100Z" fill="#FFFFFF" {W(3.2)}/>'
    + f'<path d="M40 100 Q52 40 64 30 M88 100 Q76 40 64 30" fill="none" {W(2)}/>'
    + f'<path d="M26 100 L102 100 L94 82 L34 82Z" fill="#6CC46A" {W(2.4)}/>'
    + f'<path d="M64 82 V100" stroke="#fff" stroke-width="2"/>'
    + soccer(76, 88, 5, fc=False) + head(52, 80, "#333", r=5, k=0.2)
    + face(64, 54, d=8, k=0.6)
    + f'<path d="M100 22 l0 8 M96 26 l8 0 M20 30 l0 6 M17 33 l6 0" stroke="#fff" stroke-width="2.4"/>',
    "белый купол крытого футбольного манежа с мордочкой",
    "укрывает маленькое зелёное поле, где малыш бьёт по мячу, а снаружи падает снег")

add("championika-taymyrskaya", "e_jug",
    grass(108, "#9AD47F")
    + shirt(56, 54, 22, 26, "#FF8A3D")
    + limb("M50 80 L48 106", SKIN, 6) + limb("M62 80 Q78 80 74 92", SKIN, 6)
    + limb("M46 60 L30 70", SKIN, 5) + limb("M66 60 L84 58", SKIN, 5)
    + head(56, 40, "#2E2E2E", r=12, k=0.45)
    + soccer(82, 30, 11, fc=False)
    + f'<path d="M76 70 Q72 54 78 44" fill="none" stroke-dasharray="3 4" {W(2)}/>',
    "мальчик в оранжевой футболке",
    "чеканит мяч коленкой, стоя на одной ноге и раскинув руки для равновесия")

add("championika-tayninskaya", "e_slal",
    grass(96, "#8ED6A0")
    + cone(26, 112) + cone(64, 104) + cone(102, 114)
    + f'<path d="M18 120 Q44 92 64 116 Q84 128 110 100" fill="none" stroke="#fff" stroke-dasharray="4 5" stroke-width="2.4"/>'
    + shirt(64, 48, 22, 24, "#FF7FA8")
    + limb("M58 72 L50 92", SKIN, 6) + limb("M70 72 L80 90", SKIN, 6)
    + limb("M54 54 L42 64", SKIN, 5) + limb("M74 54 L86 62", SKIN, 5)
    + f'<path d="M50 28 Q38 32 40 46 M78 28 Q90 32 88 46" fill="none" stroke="#8B4A2B" stroke-width="5" stroke-linecap="round"/>'
    + head(64, 34, "#8B4A2B", r=12, k=0.45)
    + soccer(88, 94, 8, fc=False),
    "девочка с двумя косичками в розовой форме",
    "ведёт мяч змейкой между тремя оранжевыми фишками по пунктирной дорожке")

add("championika-polyany", "e_corgi",
    grass(100)
    + f'<ellipse cx="54" cy="72" rx="28" ry="16" fill="#F2A65A" {W(3)}/>'
    + f'<ellipse cx="54" cy="78" rx="18" ry="8" fill="#FFF3E2"/>'
    + limb("M36 84 L32 96", "#F2A65A", 6) + limb("M70 84 L76 96", "#F2A65A", 6)
    + f'<path d="M26 66 Q14 58 16 50" fill="none" stroke="#F2A65A" stroke-width="7" stroke-linecap="round"/>'
    + f'<circle cx="84" cy="56" r="15" fill="#F2A65A" {W(3)}/>'
    + f'<path d="M74 46 L70 28 L84 42Z M90 42 L100 28 L98 48Z" fill="#F2A65A" {W(2.4)}/>'
    + f'<ellipse cx="92" cy="62" rx="7" ry="5" fill="#FFF3E2" {W(2)}/><circle cx="97" cy="60" r="2.4" fill="{O}"/>'
    + eye(82, 52, 0.6) + eye(90, 51, 0.6)
    + soccer(112, 90, 10, fc=False)
    + f'<path d="M8 80 l-6 0 M10 90 l-7 2" {W(2.2)}/>',
    "рыжий корги с короткими лапками",
    "несётся по полю за катящимся мячом, уши торчат по ветру")

add("championika-lobnya", "e_boots",
    f'<rect x="-6" y="104" width="140" height="40" fill="#B9DE8C" {W(2.6)}/>'
    + shirt(52, 52, 22, 24, "#FFD54A")
    + limb("M46 76 L42 94", SKIN, 5) + limb("M58 76 L64 92", SKIN, 5)
    + f'<path d="M18 92 Q18 84 30 86 L42 86 Q54 92 52 104 L16 104 Q12 98 18 92Z" fill="#2B2B3A" {W(2.8)}/>'
    + f'<path d="M54 88 Q54 80 66 82 L76 82 Q90 88 88 100 L52 100 Q48 94 54 88Z" fill="#2B2B3A" {W(2.8)}/>'
    + f'<path d="M26 90 l6 0 M28 95 l6 0 M62 86 l6 0 M64 91 l6 0" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>'
    + f'<path d="M16 104 H52 M52 100 H88" stroke="#E8E8E8" stroke-width="3"/>'
    + limb("M44 58 L32 70", SKIN, 5) + limb("M62 58 L74 66", SKIN, 5)
    + head(52, 38, "#C8873E", r=12, k=0.45)
    + soccer(104, 90, 12, fc=False),
    "малыш в огромных папиных бутсах",
    "важно шагает к мячу, а бутсы больше его самого")

add("championika-ruzino", "e_rain",
    grass(100, "#A6D27E")
    + f'<ellipse cx="54" cy="110" rx="34" ry="8" fill="#7CB9E8" {W(2.4)}/>'
    + f'<path d="M30 98 l-6 -8 M40 96 l-2 -10 M70 96 l4 -10 M80 98 l8 -8" {W(2.2)}/>'
    + f'<path d="M40 44 Q54 34 68 44 L72 82 L36 82Z" fill="#FFD83A" {W(3)}/>'
    + limb("M46 82 L44 100", SKIN, 5) + limb("M62 82 Q74 88 80 82", SKIN, 5)
    + f'<rect x="38" y="96" width="12" height="12" rx="3" fill="#E84B4B" {W(2.4)}/>'
    + f'<path d="M76 76 L88 76 L88 88 L78 88Z" fill="#E84B4B" {W(2.4)}/>'
    + head(54, 32, "#E0C080", r=12, k=0.45)
    + f'<path d="M40 30 Q54 12 68 30" fill="#FFD83A" {W(2.6)}/>'
    + soccer(104, 66, 11, fc=False)
    + f'<circle cx="14" cy="92" r="4" fill="#fff" {W(1.6)}/><circle cx="14" cy="92" r="1.6" fill="#FFC93C"/>'
    + f'<circle cx="118" cy="98" r="4" fill="#fff" {W(1.6)}/><circle cx="118" cy="98" r="1.6" fill="#FFC93C"/>',
    "девочка в жёлтом дождевике и красных резиновых сапогах",
    "бьёт по мячу прямо из лужи на деревенском лугу, брызги во все стороны")

add("championika-zelenograd-rekord", "e_pass",
    grass(102, "#86C96E")
    + shirt(22, 64, 16, 20, "#3E7BE0") + limb("M18 84 L14 100", SKIN, 4) + limb("M26 84 L34 98", SKIN, 4)
    + head(22, 52, "#3A2A20", r=9, k=0.35)
    + shirt(106, 64, 16, 20, "#E84B4B") + limb("M102 84 L98 100", SKIN, 4) + limb("M110 84 L114 100", SKIN, 4)
    + limb("M98 70 L90 62", SKIN, 4) + limb("M114 70 L122 62", SKIN, 4)
    + head(106, 52, "#E0B060", r=9, k=0.35)
    + f'<path d="M36 96 Q64 20 94 92" fill="none" stroke="#fff" stroke-dasharray="4 6" stroke-width="2.6"/>'
    + soccer(64, 42, 13, fc=True, k=0.4),
    "два малыша в синей и красной форме",
    "пасуют мяч друг другу через всё поле по высокой пунктирной дуге")

add("championika-zelenograd-1514", "e_head",
    f'<rect x="-6" y="110" width="140" height="30" fill="#6FBE62" {W(2.6)}/>'
    + G(60, 74, shirt(0, -14, 22, 26, "#3FBF6A") + f'<path d="M-11 -6 H11 M-11 2 H11" stroke="#fff" stroke-width="3"/>', rot=-10)
    + limb("M52 86 L42 104", SKIN, 6) + limb("M66 86 L78 100", SKIN, 6)
    + limb("M50 64 L34 56", SKIN, 5) + limb("M70 62 L84 70", SKIN, 5)
    + head(56, 46, "#6A4028", r=12, k=0.45)
    + soccer(62, 18, 11, fc=False)
    + sparkle(42, 18, 5, "#FFE066") + sparkle(84, 20, 6, "#FFE066") + sparkle(76, 6, 4, "#FFE066"),
    "мальчик в полосатой зелёной футболке",
    "в прыжке отбивает мяч головой, вокруг вспыхивают звёздочки")

add("championika-zelenograd-430a", "e_wall",
    f'<rect x="-6" y="96" width="140" height="40" fill="#9FD67E" {W(2.6)}/>'
    + "".join(shirt(x, 54, 22, 34, "#2F6FD0") + limb(f"M{x-5} 88 L{x-6} 100", SKIN, 5) + limb(f"M{x+5} 88 L{x+6} 100", SKIN, 5)
              + G(x, 40, f'<circle r="11" fill="{SKIN}" {W(2.6)}/>'
                  + f'<path d="M-11 -2 Q-10 -14 0 -13 Q10 -14 11 -2 Q2 -8 -11 -2Z" fill="{h}" {W(2)}/>'
                  + f'<path d="M-6 2 q2 2 4 0 M2 2 q2 2 4 0" fill="none" {W(1.8)}/>'
                  + f'<path d="M-3 7 q3 -2 6 0" fill="none" {W(1.8)}/>')
              + limb(f"M{x-8} 60 L{x-2} 70", SKIN, 4) + limb(f"M{x+8} 60 L{x+2} 70", SKIN, 4)
              for x, h in ((34, "#3A2A20"), (64, "#E2B65A"), (94, "#9A4A2A")))
    + soccer(64, 112, 12, fc=False)
    + f'<path d="M56 98 l-4 -6 M72 98 l4 -6" {W(2)}/>',
    "три малыша-«стенка» в одинаковых синих футболках",
    "зажмурились и прикрылись руками перед штрафным ударом, мяч летит на них")

add("championika-shchelkovo-biokombinat", "e_corner",
    f'<rect x="-6" y="70" width="140" height="70" fill="#7CCB6C" {W(2.6)}/>'
    + f'<path d="M-6 72 H134" stroke="#fff" stroke-width="3"/>'
    + f'<path d="M18 72 L18 30" {W(3)}/><path d="M18 30 L40 36 L18 44Z" fill="#FFD23F" {W(2.4)}/>'
    + f'<path d="M18 92 Q34 92 36 72" fill="none" stroke="#fff" stroke-width="3"/>'
    + soccer(28, 82, 7, fc=False)
    + shirt(78, 50, 22, 26, "#8E5BD8")
    + limb("M72 76 L68 96", SKIN, 6) + limb("M84 76 L88 96", SKIN, 6)
    + limb("M70 58 L46 76", SKIN, 5) + limb("M86 58 L98 70", SKIN, 5)
    + head(80, 36, "#D2843C", r=12, k=0.45, style="tail"),
    "девочка в фиолетовой форме с хвостиком",
    "ставит мяч в угловую дугу у жёлтого флажка, готовясь подать угловой")

add("championika-shchelkovo-goldtennis", "e_throw",
    grass(98, "#8BCF73")
    + f'<path d="M-6 112 H134" stroke="#fff" stroke-width="4"/>'
    + shirt(64, 50, 24, 28, "#E5484D")
    + limb("M58 78 L54 108", SKIN, 6) + limb("M70 78 L76 108", SKIN, 6)
    + f'<rect x="49" y="94" width="10" height="12" fill="#E5484D" {W(2)}/><rect x="71" y="94" width="10" height="12" fill="#E5484D" {W(2)}/>'
    + limb("M54 56 Q46 40 56 24", SKIN, 5) + limb("M74 56 Q82 40 72 24", SKIN, 5)
    + head(64, 40, "#3A3030", r=12, k=0.45)
    + soccer(64, 16, 11, fc=False),
    "мальчик в красной форме и красных гетрах",
    "вбрасывает мяч из-за головы двумя руками, стоя у белой боковой линии")

add("championika-balashikha-trubetskaya", "e_slide",
    grass(96, "#86CF78")
    + f'<path d="M4 108 H40 M10 116 H46 M2 100 H30" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'
    + shirt(70, 52, 24, 28, "#FFFFFF")
    + f'<path d="M58 60 H82" stroke="#5AA9E6" stroke-width="5"/>'
    + limb("M62 80 L44 98", "#5AA9E6", 6) + limb("M76 80 L60 102", "#5AA9E6", 6)
    + limb("M60 56 L50 30", SKIN, 5) + limb("M80 56 L92 30", SKIN, 5)
    + head(70, 40, "#2F2F2F", r=12, k=0.45)
    + f'<path d="M64 46 q6 6 12 0" fill="{O}"/>'
    + soccer(108, 92, 9, fc=False)
    + f'<rect x="14" y="20" width="5" height="9" fill="#FFD23F" transform="rotate(20 16 24)"/>'
    + f'<rect x="104" y="18" width="5" height="9" fill="#FF6FA8" transform="rotate(-25 106 22)"/>'
    + f'<rect x="30" y="40" width="5" height="9" fill="#5AA9E6" transform="rotate(40 32 44)"/>',
    "мальчик в бело-голубой форме",
    "празднует гол, скользя на коленях по траве с поднятыми руками, вокруг конфетти")

add("championika-balashikha-mayakovskogo", "e_dad",
    grass(100, "#7FCB8A")
    + f'<path d="M64 100 V36 H124 V100" fill="none" stroke="#fff" stroke-width="5"/>'
    + shirt(94, 50, 30, 30, "#F28C38")
    + limb("M86 80 L80 100", "#3A3A55", 7) + limb("M102 80 L108 100", "#3A3A55", 7)
    + limb("M80 58 L70 46", SKIN, 6) + limb("M108 58 L118 46", SKIN, 6)
    + f'<circle cx="68" cy="43" r="7" fill="#43C26A" {W(2.4)}/><circle cx="120" cy="43" r="7" fill="#43C26A" {W(2.4)}/>'
    + head(94, 34, "#5A3A28", r=13, k=0.5)
    + shirt(26, 76, 16, 16, "#FFD23F")
    + limb("M22 92 L20 104", SKIN, 4) + limb("M30 92 L40 98", SKIN, 4)
    + head(26, 66, "#E2B65A", r=9, k=0.35)
    + soccer(50, 98, 8, fc=False),
    "папа во вратарских перчатках и малыш в жёлтой футболке",
    "папа стоит в воротах, а малыш бьёт ему пенальти")

add("championika-ramenskoe", "e_dalm",
    grass(104, "#A9D97E")
    + f'<path d="M44 104 Q38 70 52 56 L76 56 Q90 70 84 104Z" fill="#FFFFFF" {W(3)}/>'
    + f'<circle cx="54" cy="76" r="4" fill="{O}"/><circle cx="72" cy="88" r="3.4" fill="{O}"/><circle cx="60" cy="96" r="3" fill="{O}"/>'
    + f'<path d="M84 96 Q102 94 104 80" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/>'
    + f'<path d="M84 96 Q102 94 104 80" fill="none" {W(1.6)}/>'
    + f'<circle cx="64" cy="40" r="20" fill="#FFFFFF" {W(3)}/>'
    + f'<path d="M46 30 Q34 36 40 54 Q48 48 48 34Z M82 30 Q94 36 88 54 Q80 48 80 34Z" fill="#2E2E3A" {W(2.4)}/>'
    + f'<circle cx="72" cy="28" r="3" fill="{O}"/>'
    + eye(57, 38, 0.6) + eye(71, 38, 0.6)
    + soccer(64, 60, 12, fc=False),
    "пятнистый далматинец",
    "сидит на траве с футбольным мячом в зубах и виляет хвостом")

# ============================== СПОРТШКОЛЫ МОСКОМСПОРТА ==============================
add("ms-sever-sokol", "e_step",
    f'<rect x="-6" y="108" width="140" height="30" fill="#9BD9DE" {W(2.6)}/>'
    + f'<path d="M26 108 L34 94 L94 94 L102 108Z" fill="#5A5F7A" {W(2.8)}/><rect x="34" y="88" width="60" height="7" rx="3" fill="#B6E36A" {W(2.4)}/>'
    + f'<path d="M54 46 L74 46 L76 72 L52 72Z" fill="#26C6C6" {W(2.8)}/>'
    + limb("M58 72 L56 88", SKIN, 6) + limb("M70 72 L84 84 L86 96", SKIN, 6)
    + limb("M56 50 L42 28", SKIN, 5) + limb("M72 50 L86 28", SKIN, 5)
    + head(64, 34, "#9B4A2A", r=12, k=0.45, style="tail")
    + f'<path d="M52 28 Q64 22 76 28" fill="none" stroke="#FF5A8A" stroke-width="4"/>',
    "девочка-аэробистка в бирюзовом купальнике с розовой повязкой",
    "делает шаг на степ-платформу, подняв руки вверх")

add("ms-sever-dinamika", "e_lift",
    f'<rect x="-6" y="106" width="140" height="30" fill="#C9B48E" {W(2.6)}/>'
    + f'<path d="M16 24 H112" stroke="#9AA0B5" stroke-width="5" stroke-linecap="round"/><path d="M16 24 H112" {W(1.4)}/>'
    + f'<rect x="10" y="10" width="12" height="28" rx="3" fill="#E8554A" {W(2.6)}/><rect x="106" y="10" width="12" height="28" rx="3" fill="#E8554A" {W(2.6)}/>'
    + f'<rect x="22" y="14" width="7" height="20" rx="2" fill="#FFC93C" {W(2.2)}/><rect x="99" y="14" width="7" height="20" rx="2" fill="#FFC93C" {W(2.2)}/>'
    + limb("M54 62 L44 26", SKIN, 6) + limb("M74 62 L84 26", SKIN, 6)
    + f'<path d="M50 56 L78 56 L80 88 L48 88Z" fill="#3B66C8" {W(2.8)}/>'
    + limb("M54 88 L44 104", SKIN, 7) + limb("M74 88 L84 104", SKIN, 7)
    + head(64, 52, "#2E2A26", r=12, k=0.45)
    + f'<circle cx="53" cy="56" r="4" fill="#FF9AB8" opacity=".8"/><circle cx="75" cy="56" r="4" fill="#FF9AB8" opacity=".8"/>',
    "малыш-тяжелоатлет в синем трико",
    "поднимает над головой лёгкую штангу с красными и жёлтыми блинами, надув щёки")

add("ms-sever-izmaylovo", "e_bridge",
    f'<rect x="-6" y="96" width="140" height="40" fill="#F7C9D6" {W(2.6)}/>'
    + f'<rect x="14" y="90" width="100" height="12" rx="5" fill="#6FA8F0" {W(2.6)}/>'
    + f'<path d="M30 90 Q36 46 64 42 Q92 46 98 90" fill="none" stroke="{O}" stroke-width="15" stroke-linecap="round"/>'
    + f'<path d="M30 90 Q36 46 64 42 Q92 46 98 90" fill="none" stroke="#D93A6B" stroke-width="11" stroke-linecap="round"/>'
    + limb("M30 88 L22 90", SKIN, 5) + limb("M98 88 L108 90", SKIN, 5)
    + head(26, 76, "#3A2A20", r=10, k=0.38, style="tail")
    + sparkle(64, 22, 7) + sparkle(100, 30, 4),
    "гимнастка в малиновом купальнике",
    "стоит «мостиком» на голубом мате, выгнув спину дугой")

add("ms-sever-ikshinsky", "e_jump",
    f'<rect x="-6" y="100" width="70" height="40" fill="#E6795A" {W(2.6)}/>'
    + f'<rect x="64" y="100" width="70" height="40" fill="#F6DE9A" {W(2.6)}/>'
    + f'<rect x="56" y="100" width="8" height="6" fill="#fff" {W(2)}/>'
    + f'<path d="M80 112 q2 -3 4 0 M92 118 q2 -3 4 0" fill="none" {W(1.6)}/>'
    + G(70, 54, shirt(0, -12, 22, 24, "#2EA3E0"), rot=20)
    + limb("M74 64 L96 66 L104 74", SKIN, 6) + limb("M68 66 L92 76", SKIN, 6)
    + limb("M62 46 L84 30", SKIN, 5) + limb("M66 50 L92 42", SKIN, 5)
    + head(54, 38, "#6A3A20", r=12, k=0.45)
    + f'<path d="M8 50 H30 M12 62 H32 M16 74 H34" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>',
    "мальчик-прыгун в длину в голубой майке",
    "летит в прыжке над песочной ямой, оттолкнувшись от белой доски")

add("ms-sever-kronshtadtsky", "e_bow",
    f'<rect x="-6" y="92" width="140" height="44" fill="#E8D27A" {W(2.6)}/>'
    + f'<path d="M-6 92 H134 M30 92 L22 136 M64 92 V136 M98 92 L106 136" fill="none" {W(1.8)}/>'
    + G(36, 70, f'<path d="M-12 -14 L12 -14 L14 22 L-14 22Z" fill="#fff" {W(2.8)}/>'
        + f'<rect x="-14" y="4" width="28" height="5" fill="#FFD23F" {W(1.8)}/>', rot=25)
    + limb("M30 92 L26 104", "#fff", 6) + limb("M44 90 L44 104", "#fff", 6)
    + head(52, 52, "#2E2A26", r=10, k=0.38)
    + G(92, 70, f'<path d="M-12 -14 L12 -14 L14 22 L-14 22Z" fill="#fff" {W(2.8)}/>'
        + f'<rect x="-14" y="4" width="28" height="5" fill="#fff" {W(1.8)}/>', rot=-25)
    + limb("M98 92 L102 104", "#fff", 6) + limb("M84 90 L84 104", "#fff", 6)
    + head(76, 52, "#C8873E", r=10, k=0.38)
    + f'<path d="M58 30 q6 -6 12 0" fill="none" stroke="#E8554A" stroke-width="3"/>',
    "два малыша-дзюдоиста в белых кимоно с жёлтым и белым поясом",
    "кланяются друг другу на татами перед схваткой")

add("ms-sever-dmitrovsky", "e_bat",
    f'<rect x="-6" y="102" width="140" height="40" fill="#C99A68" {W(2.6)}/>'
    + f'<path d="M56 110 L64 104 L72 110 L68 118 L60 118Z" fill="#fff" {W(2)}/>'
    + shirt(52, 52, 22, 28, "#FFFFFF") + f'<path d="M41 62 H63" stroke="#E8554A" stroke-width="4"/>'
    + limb("M46 80 L40 102", "#5A6B8A", 6) + limb("M58 80 L66 102", "#5A6B8A", 6)
    + limb("M44 58 L62 44", SKIN, 5) + limb("M60 58 L66 46", SKIN, 5)
    + f'<path d="M64 46 L104 12" stroke="#C98B4E" stroke-width="8" stroke-linecap="round"/><path d="M64 46 L104 12" {W(1.2)}/>'
    + head(48, 38, "#E2B65A", r=12, k=0.45, style="tail")
    + f'<path d="M34 36 Q34 20 48 20 Q64 20 62 36 L66 38 L34 38Z" fill="#E8554A" {W(2.6)}/>'
    + f'<circle cx="104" cy="52" r="9" fill="#F4E04A" {W(2.4)}/><path d="M98 46 q6 6 0 12 M110 46 q-6 6 0 12" fill="none" stroke="#E8554A" stroke-width="1.6"/>',
    "девочка-бэттер в красном шлеме",
    "замахивается битой на летящий жёлтый софтбольный мяч у домашней базы")

add("ms-yug-annino", "e_catch",
    f'<rect x="-6" y="100" width="140" height="40" fill="#C8A57A" {W(2.6)}/>'
    + f'<ellipse cx="56" cy="86" rx="24" ry="18" fill="#3E6FB8" {W(2.8)}/>'
    + limb("M40 96 L34 106", "#3E6FB8", 7) + limb("M72 96 L78 106", "#3E6FB8", 7)
    + head(56, 56, "#4A3326", r=14, k=0.5)
    + f'<path d="M44 50 H68 M44 58 H68 M50 46 V66 M62 46 V66" stroke="#555" stroke-width="2.4"/>'
    + f'<path d="M42 44 Q56 34 70 44" fill="none" {W(2.4)}/>'
    + f'<path d="M78 70 Q96 54 108 68 Q112 88 92 92 Q78 90 78 70Z" fill="#A0622E" {W(3)}/>'
    + f'<path d="M86 72 L100 72 M88 80 L100 80" {W(1.8)}/>'
    + f'<circle cx="94" cy="76" r="7" fill="#fff" {W(2.2)}/><path d="M90 71 q3 5 0 10 M98 71 q-3 5 0 10" fill="none" stroke="#E8554A" stroke-width="1.4"/>'
    + f'<path d="M110 50 l8 -8 M112 60 l10 -2" {W(2)}/>',
    "мальчик-кэтчер в защитной маске и большой коричневой ловушке",
    "сидит на корточках за домашней базой и ловит бейсбольный мяч")

add("ms-yug-orekhovo", "e_acro",
    f'<rect x="-6" y="112" width="140" height="30" fill="#E7B7E8" {W(2.6)}/>'
    + shirt(64, 70, 26, 26, "#3E8FE0")
    + limb("M56 96 L52 112", SKIN, 7) + limb("M72 96 L76 112", SKIN, 7)
    + limb("M54 76 L46 60", SKIN, 6) + limb("M74 76 L82 60", SKIN, 6)
    + head(64, 58, "#3A2A20", r=11, k=0.4)
    + limb("M58 46 L52 58", SKIN, 5) + limb("M70 46 L78 58", SKIN, 5)
    + f'<path d="M56 22 L72 22 L74 46 L54 46Z" fill="#FF6FA8" {W(2.6)}/>'
    + limb("M58 26 L32 18", SKIN, 4) + limb("M70 26 L96 18", SKIN, 4)
    + head(64, 12, "#E2B65A", r=9, k=0.34, style="tail")
    + sparkle(22, 40, 5) + sparkle(106, 40, 5),
    "пара юных акробатов: мальчик и девочка",
    "девочка стоит на плечах у мальчика и раскинула руки, как звёздочка")

add("mazvs-kurkino", "e_ski",
    f'<path d="M-6 50 L134 120 L134 140 L-6 140Z" fill="#FFFFFF" {W(2.6)}/>'
    + f'<path d="M24 54 L24 76" {W(2.4)}/><path d="M24 54 L38 60 L24 66Z" fill="#E8554A" {W(2)}/>'
    + f'<path d="M100 92 L100 112" {W(2.4)}/><path d="M100 92 L114 98 L100 104Z" fill="#3E7BE0" {W(2)}/>'
    + f'<path d="M30 100 L86 120" stroke="#3E7BE0" stroke-width="4" stroke-linecap="round"/><path d="M30 100 L86 120" {W(1.2)}/>'
    + shirt(58, 76, 20, 22, "#FF8A3D")
    + limb("M52 98 L48 108", "#5A5F7A", 6) + limb("M64 98 L68 112", "#5A5F7A", 6)
    + limb("M50 82 L36 94", SKIN, 4) + limb("M68 82 L80 98", SKIN, 4)
    + f'<path d="M36 94 L28 114 M80 98 L84 118" {W(2.2)}/>'
    + head(58, 60, "#E2B65A", r=11, k=0.42)
    + f'<path d="M42 62 Q42 38 58 38 Q76 38 76 62 L70 58 Q58 50 46 58Z" fill="#7C4DD6" {W(2.8)}/>'
    + f'<rect x="48" y="48" width="20" height="7" rx="3" fill="#9DE0FF" {W(2)}/>',
    "малыш-горнолыжник в огромном фиолетовом шлеме",
    "спускается по белому склону змейкой между красным и синим флажками слалома")

add("mazvs-novoperedelkino", "e_board",
    f'<path d="M-6 108 Q30 96 64 112 L64 140 L-6 140Z" fill="#FFFFFF" {W(2.6)}/>'
    + f'<path d="M64 112 Q70 96 80 94" fill="none" {W(2.4)}/>'
    + G(70, 66, f'<rect x="-34" y="16" width="68" height="12" rx="6" fill="#39C27A" {W(2.8)}/>'
        + f'<path d="M-20 22 h6 M14 22 h6" {W(2)}/>'
        + shirt(0, -22, 26, 28, "#FF8A3D", 7)
        + limb("M-8 6 L-14 18", "#3A3A55", 7) + limb("M8 6 L14 18", "#3A3A55", 7)
        + limb("M10 -16 L22 18", SKIN, 5) + limb("M-12 -16 L-30 -30", SKIN, 5), rot=-18)
    + head(64, 28, "#3A2A20", r=12, k=0.45)
    + f'<path d="M52 24 Q64 10 76 24 Z" fill="#2F6FD0" {W(2.4)}/>'
    + f'<rect x="52" y="24" width="24" height="7" rx="3" fill="#FFC93C" {W(2)}/>'
    + sparkle(104, 30, 6) + sparkle(22, 44, 4),
    "подросток-сноубордист в оранжевой куртке и жёлтой маске",
    "в прыжке над снежным трамплином хватается рукой за зелёную доску")

add("mazvs-sevastopolsky", "e_tbar",
    f'<path d="M-6 120 L134 50 L134 140 L-6 140Z" fill="#FFFFFF" {W(2.6)}/>'
    + f'<path d="M-6 50 L134 -20" stroke="#4A4466" stroke-width="2.6"/>'
    + f'<path d="M16 40 L16 64 M6 64 H26" fill="none" {W(3)}/>'
    + f'<path d="M86 4 L86 30 M76 30 H96" fill="none" {W(3)}/>'
    + f'<path d="M110 50 L118 30 L126 50Z M100 70 L108 50 L116 70Z" fill="#3E9A62" {W(2.2)}/>'
    + shirt(76, 46, 20, 22, "#E8554A")
    + limb("M70 68 L74 82", "#3A3A55", 6) + limb("M82 68 L90 78", "#3A3A55", 6)
    + f'<path d="M58 86 L104 70 M64 90 L110 74" stroke="#2F6FD0" stroke-width="3.4" stroke-linecap="round"/>'
    + limb("M70 50 L86 34", SKIN, 4) + limb("M82 50 L90 32", SKIN, 4)
    + head(72, 34, "#E2B65A", r=10, k=0.38)
    + f'<path d="M62 32 Q62 18 72 18 Q82 18 82 32Z" fill="#FFD23F" {W(2.4)}/><circle cx="72" cy="16" r="3.4" fill="#fff" {W(1.6)}/>',
    "бугельный подъёмник с малышом в жёлтой шапке",
    "тянет малыша на лыжах вверх по склону мимо ёлочек")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for pid, code in ICONS.items():
        open(os.path.join(OUT, pid + ".svg"), "w").write(code)
    reg = os.path.join(OUT, "subjects.txt")
    lines = [l for l in open(reg, encoding="utf-8") if l.split(" — ", 1)[0] not in SUBJ]
    lines += [line + "\n" for line in SUBJ.values()]
    open(reg, "w", encoding="utf-8").writelines(lines)
    print(len(ICONS), "иконок:", " ".join(ICONS))
