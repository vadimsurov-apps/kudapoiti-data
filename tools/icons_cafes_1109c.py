"""Иконки робота cafes, 2026-11-09 (третья партия, 10–12 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая придумана
и нарисована отдельно (свой герой по кухне/названию, своя сцена, своя компоновка и палитра фона). Сверено с
icons-src/subjects.txt (поиск по ключевым словам) и всеми листами icons-catalog.
Запуск: python3 tools/icons_cafes_1109c.py [id…]"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=8, k=0.7, **kw: face(cx, cy, d=d, k=k, **kw)
draw_icons.BG.update({
    "k9_clay": ("#FFF1E4", "#C9784A"),
    "k9_fair": ("#F0FFF6", "#5FC79A"),
    "k9_ember": ("#3A2A2A", "#17100F"),
    "k9_fir": ("#F2FFF0", "#3E8A55"),
    "k9_slide": ("#FFF5FB", "#E46FA8"),
    "k9_tokyo": ("#2B2F5C", "#121433"),
    "k9_berry": ("#F4ECFF", "#6E4FA6"),
    "k9_brick": ("#FFF3EA", "#B4533A"),
    "k9_disco": ("#3B1F55", "#1B0D2B"),
    "k9_station": ("#EEF6F9", "#6E8FA3"),
    "k9_aurora": ("#1D3A4F", "#0B1726"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Восток № 1 (чайхана) — тандыр, из которого вылетают самсы
add("cafe-vostok1-yasnogorskaya",
    "глиняный тандыр-печка с огоньком внутри",
    "из его жерла, как птенцы из гнезда, выпрыгивают три румяные самсы", "k9_clay", f'''
<path d="M30 122 Q24 76 40 60 L88 60 Q104 76 98 122Z" fill="#D9895A" {s()}/>
<path d="M36 92 Q64 98 92 92 M33 108 Q64 114 95 108" fill="none" stroke="#B5663E" stroke-width="3"/>
<ellipse cx="64" cy="60" rx="25" ry="8" fill="#5A2E1E" {s()}/>
<path d="M54 62 Q58 52 64 58 Q70 50 74 62Z" fill="#FFB02E"/>
<path d="M18 46 L30 24 L42 46Z" fill="#F2B75E" {s()} transform="rotate(-18 30 38)"/>
<path d="M52 34 L64 10 L76 34Z" fill="#F2B75E" {s()}/>
<path d="M86 46 L98 24 L110 46Z" fill="#F2B75E" {s()} transform="rotate(18 98 38)"/>
<circle cx="61" cy="28" r="1.3" fill="#fff"/><circle cx="67" cy="27" r="1.3" fill="#fff"/><circle cx="64" cy="20" r="1.3" fill="#fff"/>
''' + f(64, 84, d=10, k=0.8) + f(64, 28, d=4, k=0.4, blush=False))

# 2. Барашек (Лыткарино) — барашек из сладкой ваты на палочке
add("cafe-barashek-lytkarino",
    "облако сладкой ваты в виде кудрявого барашка с рожками-завитками",
    "стоит на палочке, воткнутой в бумажный стаканчик на ярмарочном прилавке под полосатым навесом", "k9_fair", f'''
<path d="M0 0 H128 V26 H0Z" fill="#fff"/>
''' + "".join(f'<path d="M{x} 0 H{x+16} V26 Q{x+8} 34 {x} 26Z" fill="#FF6F8E"/>' for x in range(0, 128, 32)) + f'''
<path d="M0 26 H128" {s()}/>
<rect x="10" y="104" width="108" height="24" fill="#C7894F" {s()}/>
<path d="M50 104 L56 122 H72 L78 104Z" fill="#fff" {s()}/>
<path d="M53 112 H75" stroke="#FF6F8E" stroke-width="4"/>
<path d="M64 104 V80" stroke="#F5E6C8" stroke-width="5" stroke-linecap="round"/>
''' + "".join(f'<circle cx="{64+24*math.cos(math.radians(a)):.1f}" cy="{62+16*math.sin(math.radians(a)):.1f}" r="12" fill="#FFC2DA" {W(2.2)}/>'
              for a in range(0, 360, 45)) + f'''
<ellipse cx="64" cy="62" rx="26" ry="18" fill="#FFC2DA"/>
<path d="M44 48 Q34 40 40 32 Q48 30 46 40" fill="none" stroke="#9C6B4A" stroke-width="4" stroke-linecap="round"/>
<path d="M84 48 Q94 40 88 32 Q80 30 82 40" fill="none" stroke="#9C6B4A" stroke-width="4" stroke-linecap="round"/>
''' + f(64, 64, d=9, k=0.8))

# 3. Miragrill — шампиньон греется над углями
add("cafe-miragrill-prospekt-mira",
    "пухлый шампиньон-гриль с тёмными полосками подпалин на шляпке",
    "греет ладошки, сидя на решётке над тлеющими красными углями", "k9_ember", f'''
<path d="M10 124 Q64 100 118 124Z" fill="#3A2622"/>
''' + "".join(f'<circle cx="{x}" cy="{y}" r="7" fill="#FF6A2A"/>' for x, y in [(26, 118), (44, 113), (64, 116), (84, 112), (102, 118)]) + f'''
<path d="M6 104 H122" stroke="#9AA3AD" stroke-width="5" stroke-linecap="round"/>
<path d="M50 104 Q46 82 52 70 H76 Q82 82 78 104Z" fill="#F6EAD6" {s()}/>
<path d="M20 72 Q20 22 64 22 Q108 22 108 72 Q64 82 20 72Z" fill="#E2C49A" {s()}/>
<path d="M36 44 L70 32 M30 58 L92 38 M44 70 L102 52" stroke="#5B3524" stroke-width="4" stroke-linecap="round"/>
<path d="M50 84 L36 94 M78 84 L92 94" {W(3.5)}/>
''' + f(64, 90, d=7, k=0.6) + sparkle(22, 20, 5, "#FFB35C") + sparkle(108, 92, 4, "#FF7A2E"))

# 4. Мёд (Домодедово, парк «Ёлочки») — кусок сотового мёда на пеньке
add("cafe-med-domodedovo",
    "квадратный кусок сотового мёда с шестиугольными ячейками",
    "сидит на пеньке между двумя ёлочками, из нижней ячейки капает мёд на пенёк", "k9_fir", f'''
<path d="M6 110 L22 64 L38 110Z M90 110 L106 60 L122 110Z" fill="#2F7A46" {s()}/>
<path d="M12 94 L22 70 L32 94Z M96 92 L106 66 L116 92Z" fill="#3C9457"/>
<path d="M36 128 V104 Q64 96 92 104 V128Z" fill="#A86E3E" {s()}/>
<ellipse cx="64" cy="104" rx="28" ry="7" fill="#E2B57C" {s()}/>
<ellipse cx="64" cy="104" rx="16" ry="3.5" fill="none" stroke="#B8844C" stroke-width="2"/>
<rect x="34" y="40" width="60" height="58" rx="8" fill="#F7B320" {s()}/>
''' + "".join(f'<path d="M{x} {y-6} l5.2 3 v6 l-5.2 3 l-5.2 -3 v-6Z" fill="#FFD465" stroke="#D88E10" stroke-width="1.6"/>'
              for x in (44, 56, 68, 80) for y in (50, 88)) + f'''
<path d="M60 98 Q62 108 64 112 Q66 108 68 98" fill="#F7B320" {W(2)}/>
''' + f(64, 70, d=10, k=0.85) + sparkle(64, 24, 6, "#FFE27A"))

# 5. Дэди (грузинский ресторан) — хачапури катается с горки
add("cafe-dedi-ulyanova",
    "аджарский хачапури-лодочка с двумя желтками",
    "съезжает с розовой детской горки в игровой комнате, подняв руки от восторга", "k9_slide", f'''
<path d="M10 20 V128 M28 20 V128" stroke="#7C5CC4" stroke-width="5"/>
<path d="M10 36 H28 M10 52 H28 M10 68 H28" stroke="#7C5CC4" stroke-width="4"/>
<path d="M26 20 Q56 26 72 70 Q86 108 128 112 L128 128 Q78 126 60 80 Q48 42 26 38Z" fill="#FF9AC6" {s()}/>
<g transform="rotate(15 72 76)">
<path d="M18 76 Q72 30 126 76 Q72 120 18 76Z" fill="#E9A34A" {s()}/>
<path d="M32 76 Q72 46 112 76 Q72 104 32 76Z" fill="#FFE7A3" {W(2)}/>
<circle cx="88" cy="70" r="8" fill="#FFB31A" {W(2)}/><circle cx="104" cy="78" r="6" fill="#FFB31A" {W(2)}/>
<circle cx="86" cy="68" r="2.4" fill="#fff"/>
</g>
''' + f(58, 74, d=9, k=0.8) + f'''
<path d="M30 70 L16 52 M112 96 L124 78" {W(4)}/>
''' + sparkle(100, 26, 7, "#FFD3E8"))

# 6. Токио-City — ролл-телебашня над ночным городом
add("cafe-tokio-city-miklukho",
    "башенка из трёх роллов-филадельфия, увенчанная икринкой-огоньком",
    "возвышается над ночными крышами города, как токийская телебашня", "k9_tokyo", f'''
<path d="M0 128 V98 H18 V86 H30 V104 H40 V92 H50 V128Z M78 128 V94 H90 V84 H100 V100 H112 V90 H128 V128Z" fill="#3B4280"/>
''' + "".join(f'<rect x="{x}" y="{y}" width="4" height="4" fill="#FFD66B"/>' for x, y in [(6, 104), (22, 92), (44, 98), (84, 100), (94, 90), (116, 96), (34, 110), (104, 108)]) + f'''
''' + "".join(f'''
<rect x="{64-w}" y="{y}" width="{2*w}" height="22" rx="7" fill="#22252E" {s()}/>
<ellipse cx="64" cy="{y+3}" rx="{w-3}" ry="5" fill="#F7F5EE" {W(2)}/>
<ellipse cx="64" cy="{y+3}" rx="{w-10}" ry="3" fill="#FF8C5A"/>
''' for w, y in [(26, 98), (21, 74), (16, 50)]) + f'''
<circle cx="64" cy="40" r="7" fill="#FF5A36" {s()}/><circle cx="62" cy="38" r="2" fill="#fff"/>
<path d="M64 33 V24" {W(2.5)}/>
''' + f(64, 110, d=8, k=0.7) + sparkle(30, 30, 5, "#fff") + sparkle(100, 40, 4, "#FFD66B"))

# 7. Белая Ворона (Звенигород) — пряничная белая ворона на ветке смородины
add("cafe-belaya-vorona-zvenigorod",
    "белая ворона из сахарной глазури — пряник",
    "сидит на ветке среди гроздей чёрной смородины и держит в клюве красную вишенку", "k9_berry", f'''
<path d="M0 98 Q60 88 128 104" fill="none" stroke="#6B4A2E" stroke-width="7" stroke-linecap="round"/>
''' + "".join(f'<circle cx="{x}" cy="{y}" r="5.5" fill="#262039" {W(2)}/>' for x, y in [(12, 108), (20, 112), (14, 117), (104, 114), (112, 118), (98, 119), (118, 110)]) + f'''
<path d="M40 92 Q30 56 56 44 Q84 34 92 62 Q96 86 80 94Z" fill="#FFFFFF" {s()}/>
<path d="M52 66 Q66 58 78 72 Q66 82 52 66Z" fill="#F0ECF8" {W(2)}/>
<path d="M58 70 l4 -3 M64 72 l4 -3 M70 74 l4 -3" stroke="#C9BCE3" stroke-width="2"/>
<path d="M40 88 L22 96 L38 98Z" fill="#fff" {s()}/>
<path d="M86 52 L108 58 L88 64Z" fill="#E8C873" {s()}/>
<path d="M104 60 Q108 70 104 76" fill="none" stroke="#3E7B3A" stroke-width="2.4"/>
<circle cx="104" cy="80" r="6" fill="#E3263E" {W(2)}/>
<path d="M58 94 V100 M70 94 V100" stroke="#E8A13A" stroke-width="4" stroke-linecap="round"/>
''' + f(74, 52, d=0, k=0.8, mouth=False) + sparkle(30, 30, 6, "#fff"))

# 8. Традиции вкуса (пиццерия, Щёлково) — пепперони с веснушками выезжает из печи
add("cafe-traditsii-vkusa-shchelkovo",
    "толстый кусок пиццы пепперони, у которого колбаски-кружочки как веснушки",
    "выезжает из кирпичной дровяной печи на деревянной лопате, щурясь от жара", "k9_brick", f'''
<path d="M0 0 H128 V128 H0Z" fill="#C2583F"/>
''' + "".join(f'<path d="M{x} {y} h20" stroke="#9E4230" stroke-width="2"/>' for x in range(0, 128, 24) for y in (12, 28)) + f'''
<path d="M34 50 V30 Q64 6 94 30 V50Z" fill="#2B1A16" {s()}/>
<path d="M46 50 Q52 34 60 44 Q66 28 74 42 Q80 34 84 50Z" fill="#FF9A2E"/>
<path d="M0 50 H128 V128 H0Z" fill="#EBD8BE"/><path d="M0 50 H128" {s()}/>
<rect x="104" y="112" width="30" height="10" rx="5" fill="#B98552" {s()}/>
<path d="M20 56 H104 Q110 86 104 122 H20 Q14 88 20 56Z" fill="#D6A16A" {s()}/>
<path d="M30 62 Q64 54 98 62 L64 120Z" fill="#FFD36B" {s()}/>
<path d="M30 62 Q64 54 98 62" fill="none" stroke="#D4893C" stroke-width="9" stroke-linecap="round"/>
''' + "".join(f'<circle cx="{x}" cy="{y}" r="5.5" fill="#D93A2A" {W(1.5)}/>' for x, y in [(44, 72), (84, 72), (52, 92), (76, 92), (64, 106)]) + f'''
''' + f(64, 80, d=8, k=0.65, blush=False) + sparkle(112, 34, 5, "#FFD25C"))

# 9. РуКоста (кафе-караоке, Лобня) — макарон-пирожное танцует под диско-шаром
add("cafe-rukosta-lobnya",
    "малиновое печенье-макарон с белой кремовой прослойкой",
    "танцует на маленьком подиуме под зеркальным диско-шаром, разбрасывающим зайчики", "k9_disco", f'''
<path d="M64 0 V18" stroke="#C9C9D6" stroke-width="2"/>
<circle cx="64" cy="26" r="11" fill="#C9D3E6" {s()}/>
<path d="M52 28 H76 M64 16 V40 M55 20 Q64 28 55 36 M73 20 Q64 28 73 36" stroke="#8E9AB8" stroke-width="1.6" fill="none"/>
''' + "".join(f'<rect x="{x}" y="{y}" width="5" height="5" fill="{c}" transform="rotate(45 {x} {y})"/>' for x, y, c in [(22, 52, "#7FE3FF"), (106, 50, "#FF8AD8"), (14, 84, "#FFE27A"), (114, 84, "#9BFFB0")]) + f'''
<ellipse cx="64" cy="116" rx="44" ry="10" fill="#7A3FA8" {s()}/>
<g transform="rotate(-10 64 82)">
<ellipse cx="64" cy="70" rx="32" ry="13" fill="#F05A8E" {s()}/>
<rect x="34" y="78" width="60" height="10" rx="5" fill="#FFF7EC" {W(2)}/>
<ellipse cx="64" cy="95" rx="32" ry="13" fill="#F05A8E" {s()}/>
</g>
<path d="M48 104 L40 114 M80 104 L90 114" {W(3.5)}/>
<path d="M32 82 L16 70 M96 78 L110 64" {W(3.5)}/>
''' + f(64, 70, d=7, k=0.65))

# 10. Анна Варенина — вареник-дама с вуалью на перроне
add("cafe-anna-varenina-korabelnaya",
    "вареник-дама в маленькой шляпке с вуалью",
    "ждёт поезда на перроне с крошечным чемоданчиком под круглыми вокзальными часами", "k9_station", f'''
<rect x="0" y="104" width="128" height="24" fill="#A7B4BE" {s()}/>
<path d="M0 112 H128" stroke="#fff" stroke-width="3" stroke-dasharray="10 8"/>
<path d="M100 104 V30" stroke="#4E5F6E" stroke-width="5"/>
<circle cx="100" cy="28" r="13" fill="#fff" {s()}/>
<path d="M100 28 V20 M100 28 L106 31" {W(2.4)}/>
<path d="M22 100 Q18 64 52 52 Q86 64 82 100Z" fill="#FFF4DD" {s()}/>
<path d="M24 98 Q32 92 40 98 Q48 92 56 98 Q64 92 72 98 Q78 94 82 98" fill="none" stroke="#E9D2A8" stroke-width="3"/>
<ellipse cx="52" cy="50" rx="18" ry="5" fill="#3E2F55" {s()}/>
<path d="M42 50 Q42 36 52 36 Q62 36 62 50Z" fill="#3E2F55" {s()}/>
<path d="M60 40 Q72 30 70 22" fill="none" stroke="#FF8AA8" stroke-width="3"/>
<path d="M36 52 Q52 70 68 52" fill="#D9D6E8" opacity=".55" stroke="#9A93B8" stroke-width="1.4"/>
<rect x="74" y="88" width="18" height="14" rx="3" fill="#C0653A" {s()}/>
<path d="M79 88 Q83 82 87 88" fill="none" {W(2.2)}/>
''' + f(52, 74, d=9, k=0.75))

# 11. Экспедиция. Северная кухня — пельмень-вертолёт над тундрой (в зале ресторана висит вертолёт)
add("cafe-ekspeditsiya-pevchesky",
    "пельмень-вертолёт с лопастями из веточек укропа",
    "летит над заснеженной тундрой под зелёным северным сиянием", "k9_aurora", f'''
<path d="M-4 40 Q30 18 64 34 Q98 50 132 26 L132 44 Q98 66 64 50 Q30 34 -4 58Z" fill="#5BE3A1" opacity=".45"/>
<path d="M-4 56 Q36 40 70 54 Q100 66 132 50 L132 60 Q100 76 70 64 Q36 50 -4 66Z" fill="#7FD1FF" opacity=".3"/>
<path d="M0 110 Q30 98 64 106 Q96 112 128 100 V128 H0Z" fill="#F2F8FF" {s()}/>
<path d="M18 112 L24 100 L30 112Z M100 106 L106 94 L112 106Z" fill="#2E6B57"/>
<path d="M64 46 V36" {W(3)}/>
<path d="M24 34 Q44 28 64 34 Q84 40 104 34" fill="none" stroke="#3E9B48" stroke-width="5" stroke-linecap="round"/>
<path d="M30 33 l-4 -5 M40 31 l-3 -6 M88 37 l3 -6 M98 35 l4 -5" stroke="#3E9B48" stroke-width="2.4" stroke-linecap="round"/>
<path d="M28 76 Q30 46 64 46 Q98 46 100 76 Q64 88 28 76Z" fill="#FBF3E2" {s()}/>
<path d="M30 76 Q38 82 46 78 Q54 84 62 79 Q70 84 78 79 Q86 84 94 78 Q98 80 100 76" fill="none" stroke="#E2D2B2" stroke-width="3"/>
<path d="M100 66 Q116 62 118 52" fill="none" stroke="#FBF3E2" stroke-width="7" stroke-linecap="round"/>
<path d="M100 66 Q116 62 118 52" fill="none" {W(2)}/>
<path d="M112 44 L124 58 M124 46 L112 56" stroke="#3E9B48" stroke-width="3" stroke-linecap="round"/>
<path d="M44 84 V92 M80 84 V92 M36 92 H90" {W(3)}/>
''' + f(60, 64, d=9, k=0.8) + sparkle(100, 16, 4, "#fff") + sparkle(20, 18, 3, "#fff"))


if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for i in ids:
        open(os.path.join(OUT, i + ".svg"), "w").write(ICONS[i])
    reg = os.path.join(OUT, "subjects.txt")
    lines = open(reg).read().splitlines()
    have = {l.split(" — ")[0] for l in lines}
    for i in ids:
        h, sc = SUBJ[i]
        line = f"{i} — герой: {h} | сцена: {sc}"
        if i in have:
            lines = [line if l.split(" — ")[0] == i else l for l in lines]
        else:
            lines.append(line)
    open(reg, "w").write("\n".join(lines) + "\n")
    print("svg", len(ids))
