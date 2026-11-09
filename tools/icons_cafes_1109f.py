"""Иконки робота cafes, 2026-11-09 (20 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая придумана и нарисована
отдельно (свой герой по названию/кухне, своя сцена, своя компоновка и палитра фона). Сверено с icons-src/subjects.txt
(поиск по ключевым словам: уха, джелато, фо-бо, бочка как герой, торт «Прага» — свободны) и листами icons-catalog.
Запуск: python3 tools/icons_cafes_1109f.py [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "k12_pond": ("#EAF8FF", "#4F9FD1"),
    "k12_alps": ("#F2FAFF", "#86B7E8"),
    "k12_gelato": ("#FFF4F8", "#F2A3C0"),
    "k12_bamboo": ("#F3FFE8", "#6FB35A"),
    "k12_campfire": ("#4B3A6E", "#1B1430"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Клёвое бистро — тарелка ухи, в неё свешена удочка, поплавок дёргается: клюёт!
add("cafe-klevoe-bistro-cheremushkinsky",
    "глубокая тарелка ухи с кусочком рыбы и веточкой укропа",
    "сверху в неё свешена удочка, красно-белый поплавок дёргается в бульоне — клюёт!", "k12_pond", f'''
<path d="M10 14 Q60 6 92 40" fill="none" stroke="#9A6A3A" stroke-width="5" stroke-linecap="round"/>
<path d="M10 14 Q60 6 92 40" fill="none" {W(1.6)}/>
<path d="M92 40 V70" stroke="{O}" stroke-width="1.6"/>
<ellipse cx="64" cy="104" rx="50" ry="10" fill="#2F6F96" opacity=".35"/>
<path d="M14 74 Q18 112 64 112 Q110 112 114 74Z" fill="#FFFFFF" {s()}/>
<path d="M22 84 Q64 92 106 84" fill="none" stroke="#7CC3EA" stroke-width="4" stroke-linecap="round"/>
<ellipse cx="64" cy="74" rx="50" ry="13" fill="#FFFFFF" {s()}/>
<ellipse cx="64" cy="75" rx="42" ry="9" fill="#FFD47A" {W(2)}/>
<path d="M30 74 Q38 70 46 74 Q38 78 30 74Z" fill="#7BC96F" {W(1.6)}/>
<path d="M36 74 L34 69 M40 74 L41 69" stroke="#4E9B44" stroke-width="1.6" stroke-linecap="round"/>
<rect x="44" y="70" width="22" height="11" rx="5" fill="#FFF3E2" {W(2)}/>
<path d="M50 72 V79 M56 72 V79" stroke="#F2C9A0" stroke-width="1.6"/>
<circle cx="80" cy="76" r="3" fill="#FF8A3D" {W(1.4)}/><circle cx="34" cy="80" r="2.4" fill="#FF8A3D" {W(1.2)}/>
<path d="M86 64 Q92 58 98 64" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M84 70 Q92 64 100 70" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" opacity=".8"/>
<ellipse cx="92" cy="66" rx="6" ry="9" fill="#FFFFFF" {W(2.2)}/>
<path d="M86 66 Q86 57 92 57 Q98 57 98 66Z" fill="#FF4D4D" {W(2.2)}/>
<path d="M92 57 V52" {W(2)}/>
<path d="M104 52 l5 -4 M106 58 l6 -1 M80 52 l-5 -4" {W(2)}/>
''' + face(64, 96, d=11, k=0.8) + sparkle(112, 26, 4) + sparkle(24, 40, 3))

# 2. Бочка — пузатая дубовая бочка-стол, на крышке дымится тарелка жаркого, позади снежные Альпы
add("cafe-bochka-1905",
    "пузатая дубовая бочка с медными обручами",
    "служит столом: на её крышке дымится тарелка жареного мяса с картошкой, а позади белеют снежные вершины Альп", "k12_alps", f'''
<path d="M-4 84 L30 44 L48 62 L74 30 L132 84Z" fill="#B9D3EE" {s()}/>
<path d="M22 54 L30 44 L38 52 L32 56 L28 52Z M64 42 L74 30 L86 44 L78 47 L72 42Z" fill="#fff" {W(2)}/>
<path d="M30 62 Q24 92 30 120 H98 Q104 92 98 62Z" fill="#B87842" {s()}/>
<path d="M44 62 Q40 92 44 120 M64 62 V120 M84 62 Q88 92 84 120" stroke="#8E5428" stroke-width="2.4"/>
<path d="M27 74 H101 M26 108 H102" stroke="{O}" stroke-width="8" stroke-linecap="round"/>
<path d="M27 74 H101 M26 108 H102" stroke="#E0A040" stroke-width="4" stroke-linecap="round"/>
<ellipse cx="64" cy="62" rx="34" ry="8" fill="#D39A62" {s()}/>
<ellipse cx="64" cy="56" rx="26" ry="6" fill="#FFFFFF" {s()}/>
<path d="M46 54 Q52 44 62 48 Q70 42 78 50 Q84 52 80 56 Q64 60 46 56Z" fill="#9C4A28" {W(2)}/>
<circle cx="52" cy="55" r="3.4" fill="#FFD25E" {W(1.6)}/><circle cx="76" cy="56" r="3" fill="#FFD25E" {W(1.6)}/>
<path d="M56 40 Q52 34 56 28 M66 38 Q62 30 66 22 M76 40 Q72 34 76 28" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
''' + face(64, 90, d=11, k=0.85) + sparkle(110, 22, 4) + sparkle(16, 24, 3))

# 3. Casa di Famiglia — джелато-семья: три шарика в одном рожке обнимаются
add("cafe-casa-famiglia-perovo",
    "итальянское джелато — три шарика разного размера в одном вафельном рожке",
    "шарики-семья обнимаются: папа-фисташковый снизу, мама-клубничная посередине, а малыш-лимонный сверху машет ручкой", "k12_gelato", f'''
<path d="M44 76 L64 124 L84 76Z" fill="#E8A65A" {s()}/>
<path d="M50 84 L76 108 M58 80 L80 100 M46 90 L66 110 M78 84 L54 108 M70 80 L50 100 M82 90 L62 110" stroke="#C47F35" stroke-width="2"/>
<path d="M44 76 L64 124 L84 76Z" fill="none" {s()}/>
<circle cx="64" cy="72" r="22" fill="#A9D98A" {s()}/>
<path d="M44 80 Q50 88 58 82 Q64 90 70 82 Q78 88 84 80" fill="none" stroke="#86C266" stroke-width="3"/>
<circle cx="64" cy="44" r="17" fill="#FF9EB5" {s()}/>
<circle cx="64" cy="20" r="11" fill="#FFF07A" {s()}/>
<path d="M74 16 Q84 8 86 0" fill="none" {W(3)}/><circle cx="87" cy="-1" r="3" fill="#FFF07A" {W(2)}/>
<path d="M44 66 Q36 56 46 48 M84 66 Q92 56 82 48" fill="none" {W(3)}/>
''' + face(64, 72, d=9, k=0.8) + face(64, 44, d=7, k=0.7) + face(64, 21, d=4.5, k=0.5, blush=False)
    + sparkle(22, 30, 5) + sparkle(106, 52, 4) + sparkle(100, 100, 3))

# 4. Шикари («охотник») — пиала фо-бо в пробковом шлеме смотрит в бинокль из бамбука
add("cafe-shikari-columbus",
    "пиала вьетнамского супа фо-бо с ломтиками говядины и звёздочкой бадьяна",
    "в пробковом шлеме охотника выглядывает из бамбуковых зарослей и смотрит в бинокль", "k12_bamboo", f'''
<path d="M14 128 V20 M26 128 V34 M108 128 V14 M118 128 V40" stroke="#4E9A3E" stroke-width="7" stroke-linecap="round"/>
<path d="M14 56 H20 M26 80 H32 M108 50 H114 M118 84 H124" stroke="#2F6E26" stroke-width="2"/>
<path d="M20 30 Q34 22 40 30 Q30 34 20 30Z M108 26 Q94 18 88 26 Q98 30 108 26Z M26 46 Q40 40 44 48 Q34 50 26 46Z" fill="#8FD46F" {W(1.8)}/>
<path d="M24 74 Q26 110 64 110 Q102 110 104 74Z" fill="#F4F0E6" {s()}/>
<path d="M32 90 Q64 98 96 90" fill="none" stroke="#5DB8A8" stroke-width="4" stroke-linecap="round"/>
<ellipse cx="64" cy="74" rx="40" ry="10" fill="#F4F0E6" {s()}/>
<ellipse cx="64" cy="75" rx="34" ry="7" fill="#E6B26A" {W(2)}/>
<path d="M36 74 Q46 70 56 75 M70 75 Q80 70 92 74" fill="none" stroke="#FFF6DD" stroke-width="3" stroke-linecap="round"/>
<path d="M44 76 L52 73 L58 77Z" fill="#A8574B" {W(1.6)}/><path d="M72 77 L80 73 L86 76Z" fill="#A8574B" {W(1.6)}/>
<path d="M64 68 l2 4 4 0 -3 3 1 4 -4 -2 -4 2 1 -4 -3 -3 4 0Z" fill="#7A3E1E" {W(1.2)}/>
<path d="M36 58 Q36 34 64 34 Q92 34 92 58Z" fill="#E9D7A8" {s()}/>
<path d="M28 60 Q64 52 100 60 Q64 66 28 60Z" fill="#E9D7A8" {s()}/>
<path d="M38 52 Q64 46 90 52" fill="none" stroke="#B8935A" stroke-width="3.5"/>
<circle cx="64" cy="33" r="3" fill="#E9D7A8" {W(2)}/>
<rect x="44" y="78" width="16" height="16" rx="6" fill="#3B3355" {W(2)}/><rect x="68" y="78" width="16" height="16" rx="6" fill="#3B3355" {W(2)}/>
<rect x="58" y="82" width="12" height="7" fill="#3B3355"/>
<circle cx="52" cy="86" r="5" fill="#9ED8FF"/><circle cx="76" cy="86" r="5" fill="#9ED8FF"/>
<circle cx="50.5" cy="84.5" r="1.6" fill="#fff"/><circle cx="74.5" cy="84.5" r="1.6" fill="#fff"/>
<ellipse cx="38" cy="98" rx="4.5" ry="2.6" fill="#FF7FA8" opacity=".6"/><ellipse cx="90" cy="98" rx="4.5" ry="2.6" fill="#FF7FA8" opacity=".6"/>
<path d="M58 101 Q64 105 70 101" fill="none" {W(2.4)}/>
''')

# 5. Легенда — кусок торта «Прага» рассказывает у костра легенду, подсвечивая себя фонариком снизу
add("cafe-legenda-tushino",
    "кусок шоколадного торта «Прага» с глазурью и кремовой розочкой",
    "ночью у костра рассказывает таинственную легенду, подсвечивая себя фонариком снизу", "k12_campfire",
    sparkle(18, 22, 3) + sparkle(42, 12, 2) + sparkle(110, 18, 3) + sparkle(96, 36, 2) + f'''
<path d="M24 26 A10 10 0 1 0 32 14 A8 8 0 1 1 24 26Z" fill="#FFF1A8"/>
<path d="M0 108 Q64 98 128 108 V128 H0Z" fill="#2B2147"/>
<path d="M30 70 L98 70 L98 106 L30 106Z" fill="#6B3B25" {s()}/>
<path d="M30 70 L64 50 L98 70Z" fill="#4A2616" {s()}/>
<path d="M30 82 H98 M30 94 H98" stroke="#C98A55" stroke-width="3"/>
<path d="M30 70 L98 70 L98 106 L30 106Z" fill="none" {s()}/>
<circle cx="64" cy="52" r="6" fill="#FFE4C2" {W(2)}/><path d="M60 52 Q64 46 68 52" fill="none" stroke="#E7B98A" stroke-width="1.6"/>
<path d="M30 70 Q64 64 98 70 L98 74 Q64 68 30 74Z" fill="#3A1B0E" opacity=".5"/>
<path d="M36 70 L64 104 L92 70Z" fill="#FFE27A" opacity=".28"/>
''' + face(64, 86, d=10, k=0.8) + f'''
<path d="M54 104 L60 116 H68 L74 104Z" fill="#9AA3B8" {W(2)}/>
<circle cx="64" cy="104" r="5" fill="#FFF3A0" {W(2)}/>
<path d="M104 116 L112 108 M104 108 L112 116" stroke="#8A5A33" stroke-width="5" stroke-linecap="round"/>
<path d="M108 108 Q100 98 106 88 Q108 96 112 92 Q118 100 108 108Z" fill="#FF8A3D" {W(2)}/>
<path d="M108 106 Q105 100 108 95 Q111 101 108 106Z" fill="#FFE27A"/>
<path d="M16 116 L24 108 M16 108 L24 116" stroke="#8A5A33" stroke-width="5" stroke-linecap="round" opacity="0"/>
''')


def main(ids):
    ids = ids or list(ICONS)
    for pid in ids:
        open(os.path.join(OUT, pid + ".svg"), "w").write(ICONS[pid])
    reg = os.path.join(OUT, "subjects.txt")
    lines = open(reg, encoding="utf-8").read().splitlines()
    have = {l.split(" — ", 1)[0] for l in lines if " — " in l}
    with open(reg, "a", encoding="utf-8") as f:
        for pid in ids:
            if pid not in have:
                h, sc = SUBJ[pid]
                f.write(f"{pid} — герой: {h} | сцена: {sc}\n")
    print("svg", len(ids))


if __name__ == "__main__":
    main(sys.argv[1:])
