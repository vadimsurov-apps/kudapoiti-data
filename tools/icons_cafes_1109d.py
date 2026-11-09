"""Иконки робота cafes, 2026-11-09 (13 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая придумана и нарисована
отдельно (свой герой по названию/кухне, своя сцена, своя компоновка и палитра фона). Сверено с icons-src/subjects.txt
(поиск по ключевым словам) и всеми листами icons-catalog.
Запуск: python3 tools/icons_cafes_1109d.py [id…]"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=8, k=0.7, **kw: face(cx, cy, d=d, k=k, **kw)
draw_icons.BG.update({
    "k10_cosmos": ("#4B5BA8", "#161C46"),
    "k10_alps": ("#F3FBFF", "#8FB9E0"),
    "k10_thaw": ("#FBFFF4", "#A9D9B8"),
    "k10_ginger": ("#FFF7EC", "#E2A35E"),
    "k10_panel": ("#F7F3FF", "#9C93C9"),
    "k10_luck": ("#F2FFF2", "#3FAE63"),
    "k10_field": ("#EAF8FF", "#62B3E8"),
    "k10_porch": ("#FFF8EE", "#D9A774"),
    "k10_feast": ("#FFF0F3", "#D9577A"),
    "k10_stage": ("#5A2B47", "#22101C"),
    "k10_hearth": ("#FFE9D6", "#A8482C"),
    "k10_arena": ("#FFFBEA", "#C9B27A"),
    "k10_desert": ("#FFF6D8", "#F0A23A"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Небо Руфтоп (Королёв, город космонавтики) — желе-планета смотрит в телескоп с крыши
add("cafe-nebo-rooftop-korolev",
    "мятное желе-планета с кольцом из взбитых сливок",
    "смотрит в телескоп с плоской крыши дома на звёздное небо", "k10_cosmos",
    sparkle(22, 22, 4) + sparkle(104, 18, 5, "#FFE48A") + sparkle(112, 52, 3) + sparkle(40, 40, 2.5) + f'''
<path d="M0 104 H128 V128 H0Z" fill="#2A2F55" {s()}/>
<rect x="14" y="110" width="8" height="8" fill="#FFD45E"/><rect x="40" y="112" width="8" height="8" fill="#FFD45E"/>
<rect x="96" y="110" width="8" height="8" fill="#FFD45E"/>
<path d="M30 104 L36 84 M44 104 L36 84" {W(2.6)} fill="none"/>
<path d="M24 76 L50 66 L54 74 L28 86Z" fill="#B9C2E8" {s()}/>
<rect x="49" y="64" width="9" height="14" rx="2" fill="#7E89C7" {s()} transform="rotate(-22 53 71)"/>
<ellipse cx="78" cy="66" rx="42" ry="10" fill="none" stroke="#fff" stroke-width="9" transform="rotate(-14 78 66)"/>
<circle cx="78" cy="66" r="27" fill="#7FE0B8" {s()}/>
<path d="M58 56 Q66 44 82 42" fill="none" stroke="#C8F7E2" stroke-width="5" stroke-linecap="round"/>
<path d="M37 72 Q78 62 119 58" fill="none" stroke="#fff" stroke-width="9" stroke-linecap="round" transform="rotate(-2 78 66)"/>
<path d="M37 72 Q78 62 119 58" fill="none" {W(2)} transform="rotate(-2 78 66)"/>
''' + eye(68, 62, 0.8) + f'''<path d="M84 60 Q89 57 94 60" fill="none" {W(2.4)}/>
<path d="M74 78 Q80 82 86 78" fill="none" {W(2.4)}/>
<ellipse cx="94" cy="72" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/>''')

# 2. Олимп — печенье «ушки» в лавровом венке на вершине горы над облаками
add("cafe-olimp-uvarovo",
    "печенье «ушки» из слоёного теста с лавровым венком",
    "стоит на снежной вершине горы над облаками и машет рукой", "k10_alps", f'''
<path d="M-4 128 L46 70 L64 84 L84 62 L132 128Z" fill="#9AA7C2" {s()}/>
<path d="M46 70 L56 82 L64 84 L72 74 L84 62 L94 76 L84 80 L74 84 L64 92 L54 86Z" fill="#fff"/>
<ellipse cx="22" cy="104" rx="22" ry="9" fill="#fff" opacity=".95"/><ellipse cx="108" cy="110" rx="24" ry="9" fill="#fff" opacity=".95"/>
<path d="M64 66 C44 66 36 50 44 38 C50 28 62 32 64 42 C66 32 78 28 84 38 C92 50 84 66 64 66Z" fill="#F2B45C" {s()}/>
<path d="M64 62 V44 M52 56 Q46 46 52 40 M76 56 Q82 46 76 40" fill="none" stroke="#C7832F" stroke-width="2.4" stroke-linecap="round"/>
''' + "".join(f'<ellipse cx="{64+22*math.cos(math.radians(a)):.1f}" cy="{36+8*math.sin(math.radians(a)):.1f}" rx="5" ry="2.6" fill="#5DAA4E" {W(1.6)} transform="rotate({a+90} {64+22*math.cos(math.radians(a)):.1f} {36+8*math.sin(math.radians(a)):.1f})"/>'
              for a in range(190, 360, 28)) + f'''
<path d="M86 52 Q98 42 100 30" fill="none" {W(3)}/>
''' + f(64, 50, d=8, k=0.6) + sparkle(104, 24, 4))

# 3. Vesna — подснежник из помадки пробивается из проталины
add("cafe-vesna-rogozinino",
    "подснежник из белой помадки на марципановом стебле",
    "пробивается из проталины в сугробе под весенним солнышком", "k10_thaw", f'''
<circle cx="104" cy="24" r="12" fill="#FFD45E" {W(2.4)}/>
''' + "".join(f'<path d="M{104+16*math.cos(math.radians(a)):.1f} {24+16*math.sin(math.radians(a)):.1f} L{104+22*math.cos(math.radians(a)):.1f} {24+22*math.sin(math.radians(a)):.1f}" {W(2.4)}/>' for a in range(0, 360, 45)) + f'''
<path d="M-4 128 L-4 96 Q20 84 40 94 Q64 104 88 92 Q110 82 132 96 V128Z" fill="#fff" {s()}/>
<ellipse cx="62" cy="104" rx="26" ry="8" fill="#8A6A4A" {s()}/>
<path d="M62 104 Q60 80 64 56" fill="none" stroke="#6CC56A" stroke-width="6" stroke-linecap="round"/>
<path d="M62 104 Q60 80 64 56" fill="none" {W(1.8)}/>
<path d="M62 92 Q44 84 42 70 Q56 74 62 88Z" fill="#7FD27A" {s()}/>
<path d="M64 56 C48 58 44 40 52 30 C56 26 62 26 64 28 C66 26 72 26 76 30 C84 40 80 58 64 56Z" fill="#FFFFFF" {s()}/>
<path d="M58 54 Q64 60 70 54" fill="none" stroke="#9BD6A0" stroke-width="3"/>
''' + f(64, 42, d=6, k=0.55) + sparkle(28, 30, 4, "#BFEFFF") + sparkle(96, 64, 3, "#fff"))

# 4. Лабиринт — пряник с глазурным лабиринтом, к центру катится драже
add("cafe-labirint-zhukovka",
    "круглый пряник с глазурным лабиринтом",
    "по дорожкам лабиринта катится цветное драже к сердечку в центре", "k10_ginger", f'''
<circle cx="64" cy="66" r="48" fill="#C98543" {s()}/>
<circle cx="64" cy="66" r="40" fill="none" stroke="#FFF7EE" stroke-width="4" stroke-dasharray="200 30"/>
<circle cx="64" cy="66" r="30" fill="none" stroke="#FFF7EE" stroke-width="4" stroke-dasharray="40 22 120 20" transform="rotate(70 64 66)"/>
<circle cx="64" cy="66" r="20" fill="none" stroke="#FFF7EE" stroke-width="4" stroke-dasharray="90 26" transform="rotate(200 64 66)"/>
<path d="M64 72 C58 66 58 60 64 62 C70 60 70 66 64 72Z" fill="#FF5C8A" {W(2)}/>
<circle cx="98" cy="40" r="9" fill="#5CC1FF" {s()}/>
''' + eye(95, 39, 0.5) + eye(101, 39, 0.5) + f'''
<path d="M108 30 l6 -4 M110 36 l7 -1" {W(2)}/>
''' + f(64, 98, d=9, k=0.65))

# 5. Соседи — две слойки здороваются из соседних окон панельного дома
add("cafe-sosedi-odintsovo",
    "две румяные слойки-подушечки с сахарной посыпкой",
    "здороваются, высунувшись из соседних окон панельного дома", "k10_panel", f'''
<rect x="10" y="18" width="108" height="118" fill="#E9E4F7" {s()}/>
<path d="M10 52 H118 M10 92 H118 M64 18 V136" stroke="#B9B2D8" stroke-width="2.4"/>
<rect x="18" y="26" width="38" height="20" fill="#9FD3F2" {W(2.4)}/><rect x="72" y="26" width="38" height="20" fill="#9FD3F2" {W(2.4)}/>
<rect x="16" y="60" width="44" height="28" fill="#6E8FB8" {s()}/>
<rect x="68" y="60" width="44" height="28" fill="#6E8FB8" {s()}/>
<rect x="18" y="100" width="38" height="20" fill="#9FD3F2" {W(2.4)}/><rect x="72" y="100" width="38" height="20" fill="#9FD3F2" {W(2.4)}/>
<rect x="22" y="56" width="34" height="28" rx="10" fill="#F2B866" {s()}/>
<rect x="72" y="56" width="34" height="28" rx="10" fill="#E9A752" {s()}/>
<path d="M14 88 H62 M66 88 H114" {W(4)}/>
<path d="M56 64 Q62 56 66 58" fill="none" {W(3)}/><path d="M72 64 Q66 56 62 58" fill="none" {W(3)}/>
''' + "".join(f'<circle cx="{x}" cy="{y}" r="1.5" fill="#fff"/>' for x, y in [(28, 60), (34, 59), (46, 60), (80, 60), (92, 59), (100, 61)]) +
    f(39, 70, d=6, k=0.5) + f(89, 70, d=6, k=0.5))

# 6. Удачи — печенье-клевер держит подкову, сверху сыплются звёздочки
add("cafe-udachi-pominovo",
    "печенье в форме четырёхлистного клевера с зелёной глазурью",
    "держит над головой подкову, а сверху сыплются золотые звёздочки", "k10_luck",
    "".join(f'<circle cx="{64+19*math.cos(math.radians(a)):.1f}" cy="{74+19*math.sin(math.radians(a)):.1f}" r="21" fill="#8EDB7C" {s()}/>' for a in (45, 135, 225, 315)) + f'''
<circle cx="64" cy="74" r="14" fill="#8EDB7C"/>
<path d="M64 98 Q68 112 78 120" fill="none" stroke="#5B9E4C" stroke-width="6" stroke-linecap="round"/>
<g transform="translate(96 30) rotate(28) scale(0.62) translate(-64 -22)"><path d="M48 40 V24 Q48 8 64 8 Q80 8 80 24 V40" fill="none" stroke="#FFC93C" stroke-width="10"/>
<path d="M43 40 V24 Q43 3 64 3 Q85 3 85 24 V40 H75 V24 Q75 13 64 13 Q53 13 53 24 V40Z" fill="none" {W(2)}/>
<circle cx="48" cy="22" r="1.5" fill="{O}"/><circle cx="56" cy="10" r="1.5" fill="{O}"/><circle cx="72" cy="10" r="1.5" fill="{O}"/><circle cx="80" cy="22" r="1.5" fill="{O}"/>
</g>
<path d="M84 60 Q92 52 92 44" fill="none" {W(3)}/>
''' + f(64, 74, d=9, k=0.75) + sparkle(20, 30, 6, "#FFD45E") + sparkle(108, 22, 5, "#FFD45E") + sparkle(104, 52, 3.5, "#FFE9A0") + sparkle(24, 60, 3, "#FFE9A0"))

# 7. Le Café (Скоково) — бургер-слайдер летит на воздушном шаре над полями
add("cafe-le-cafe-skokovo",
    "крошечный бургер-слайдер на шпажке с флажком",
    "летит в корзине воздушного шара над полями и лесом", "k10_field", f'''
<path d="M-4 112 Q30 102 64 110 Q98 118 132 106 V132 H-4Z" fill="#9BD86A" {s()}/>
<path d="M14 112 l6 -14 l6 14Z M100 112 l6 -16 l6 16Z" fill="#3E8A55" {W(2)}/>
<path d="M64 8 C34 8 26 40 46 62 L54 70 H74 L82 62 C102 40 94 8 64 8Z" fill="#FF8E6B" {s()}/>
<path d="M64 8 C54 20 54 50 58 70 M64 8 C74 20 74 50 70 70" fill="none" stroke="#FFD45E" stroke-width="7"/>
<path d="M64 8 C54 20 54 50 58 70 M64 8 C74 20 74 50 70 70" fill="none" {W(1.6)}/>
<path d="M54 70 L50 82 M74 70 L78 82" {W(2.2)}/>
<path d="M44 82 H84 L80 102 H48Z" fill="#B57B45" {s()}/>
<path d="M48 84 Q48 64 64 64 Q80 64 80 84Z" fill="#F2B45C" {W(2.4)}/>
<rect x="47" y="78" width="34" height="6" rx="2" fill="#7A4A2A"/><path d="M47 77 q6 4 12 0 t12 0 t10 0" fill="none" stroke="#7FD27A" stroke-width="3"/>
<path d="M64 64 V52" {W(2)}/><path d="M64 52 L74 56 L64 59Z" fill="#E94C4C" {W(1.6)}/>
''' + eye(58, 72, 0.5) + eye(70, 72, 0.5) + sparkle(18, 34, 4) + sparkle(110, 40, 3))

# 8. Веранда — чайник облепихового чая на столике веранды под флажками
add("cafe-veranda-mytishchi",
    "стеклянный чайник облепихового чая с оранжевыми ягодками",
    "стоит на деревянном столике веранды под гирляндой бумажных флажков", "k10_porch", f'''
<path d="M-4 18 Q64 40 132 18" fill="none" {W(2)}/>
''' + "".join(f'<path d="M{x} {18+22*math.sin(math.pi*(x+4)/136):.1f} l8 0 l-4 10Z" fill="{c}" {W(1.4)}/>' for x, c in [(6, "#FF6F6F"), (26, "#5CC1FF"), (46, "#FFD45E"), (66, "#7FD27A"), (86, "#C79BFF"), (106, "#FF9F5A")]) + f'''
<rect x="-4" y="100" width="136" height="12" fill="#C98A52" {s()}/>
<path d="M14 112 V132 M114 112 V132" {W(6)}/>
<path d="M40 52 Q36 100 48 100 H82 Q94 100 88 52Z" fill="#FFB347" fill-opacity=".9" {s()}/>
<path d="M40 52 Q36 100 48 100 H82 Q94 100 88 52Z" fill="#fff" fill-opacity=".25"/>
<path d="M88 62 Q106 60 104 78 Q102 90 88 90" fill="none" {W(3.5)}/>
<path d="M40 60 L24 48" {W(4)}/>
<rect x="44" y="44" width="40" height="9" rx="4" fill="#E9EEF5" {s()}/>
<circle cx="64" cy="40" r="4" fill="#E9EEF5" {W(2)}/>
''' + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#FF7A1A" {W(1.2)}/>' for x, y in [(50, 88), (58, 92), (74, 90), (80, 84), (48, 80)]) +
    f(64, 70, d=8, k=0.65) + f'<path d="M52 34 q-4 -6 0 -12 M76 34 q4 -6 0 -12" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')

# 9. Даниловский — заливная рыба на банкетном столе под серпантином
add("cafe-danilovsky",
    "заливная рыба на овальном блюде с лимонной долькой",
    "красуется посреди банкетного стола под взлетающими лентами серпантина", "k10_feast", f'''
<path d="M14 30 q8 -14 16 0 t16 0 M84 22 q8 -12 16 0 t14 0" fill="none" stroke="#FFD45E" stroke-width="3.5" stroke-linecap="round"/>
<path d="M40 14 q6 10 0 18 q-6 8 0 16" fill="none" stroke="#5CC1FF" stroke-width="3.5" stroke-linecap="round"/>
<path d="M96 40 q-8 6 -2 14 q6 8 -2 14" fill="none" stroke="#7FD27A" stroke-width="3.5" stroke-linecap="round"/>
<rect x="-4" y="98" width="136" height="34" fill="#FFFFFF" {s()}/>
<path d="M-4 108 Q10 116 24 108 Q38 116 52 108 Q66 116 80 108 Q94 116 108 108 Q122 116 136 108" fill="none" stroke="#F3B3C4" stroke-width="3"/>
<ellipse cx="64" cy="94" rx="56" ry="14" fill="#E6EEF5" {s()}/>
<path d="M20 86 Q24 58 64 56 Q100 56 104 80 L118 66 L116 96 L104 88 Q96 104 64 104 Q26 104 20 86Z" fill="#F5C77E" fill-opacity=".85" {s()}/>
<path d="M30 80 Q60 66 96 78" fill="none" stroke="#E98B5B" stroke-width="4" stroke-dasharray="6 6" stroke-linecap="round"/>
<path d="M76 92 a8 8 0 0 1 16 0Z" fill="#FFE45E" {W(2)}/>
<path d="M44 66 l-4 -8 M52 64 l-2 -9" {W(2)}/>
''' + eye(36, 80, 0.6) + f'''<path d="M30 90 Q36 94 42 90" fill="none" {W(2.4)}/>
<path d="M58 88 l3 4 l3 -4 M64 90 l3 4 l3 -4" fill="none" stroke="#9BD06A" stroke-width="3"/>''')

# 10. MiMi (Аннино, живая музыка) — паппарделле на вилке играет на саксофоне
add("cafe-mimi-annino",
    "широкие ленты пасты-паппарделле, закрученные на вилке",
    "играет на саксофоне на маленькой сцене под лучом софита", "k10_stage", f'''
<path d="M40 -4 L88 -4 L118 132 L10 132Z" fill="#FFF3B0" opacity=".28"/>
<rect x="-4" y="108" width="136" height="24" fill="#8A3B5E" {s()}/>
<path d="M58 108 V78 M52 78 V64 M58 78 V62 M64 78 V64 M70 78 V64" {W(3)}/>
<path d="M50 78 H72" {W(3)}/>
<path d="M36 52 C30 30 50 18 62 24 C74 14 98 26 92 48 C96 62 80 72 64 68 C48 74 30 66 36 52Z" fill="#F7D774" {s()}/>
<path d="M42 50 Q62 34 86 46 M44 60 Q64 46 84 58 M50 34 Q66 28 80 34" fill="none" stroke="#E2B442" stroke-width="3" stroke-linecap="round"/>
<path d="M84 62 Q96 74 94 92 Q92 102 84 100 Q78 98 80 90 L88 68Z" fill="#FFC23A" {s()}/>
<path d="M80 92 Q74 104 84 106 Q94 106 94 94" fill="#FFC23A" {s()}/>
<path d="M78 56 L86 64" {W(4)}/>
<circle cx="88" cy="78" r="2" fill="{O}"/><circle cx="90" cy="86" r="2" fill="{O}"/>
''' + eye(54, 46, 0.6) + eye(70, 44, 0.6) + f'''<path d="M60 58 Q66 54 72 56" fill="none" {W(2.4)}/>
<path d="M102 52 q8 -4 6 -12 l4 -2 M108 66 q10 -2 10 -10 l4 0" fill="none" stroke="#FFD45E" stroke-width="2.6" stroke-linecap="round"/>
<circle cx="102" cy="52" r="3" fill="#FFD45E"/><circle cx="108" cy="66" r="3" fill="#FFD45E"/>''')

# 11. MiMi (Гастровилла Novaya Riga) — ягодная галета греется у камина под пледом
add("cafe-mimi-novaya-riga",
    "ягодная галета с загнутыми краями",
    "греется у камина в кресле, укрывшись клетчатым пледом", "k10_hearth", f'''
<rect x="68" y="34" width="56" height="70" fill="#E0D4C8" {s()}/>
<path d="M78 104 V60 Q96 46 114 60 V104Z" fill="#3A2420" {s()}/>
<path d="M86 102 Q84 84 94 74 Q96 86 100 80 Q108 90 104 102Z" fill="#FF8A2A"/>
<path d="M92 102 Q92 92 97 86 Q100 94 102 102Z" fill="#FFD45E"/>
<rect x="62" y="28" width="68" height="8" fill="#B98D6C" {s()}/>
<path d="M4 120 V62 Q4 48 18 48 H50 Q64 48 64 62 V120Z" fill="#7C4E9E" {s()}/>
<rect x="0" y="86" width="70" height="14" rx="6" fill="#6A3E8C" {s()}/>
<circle cx="34" cy="70" r="24" fill="#E3A65A" {s()}/>
<circle cx="34" cy="70" r="15" fill="#B0274A"/>
''' + "".join(f'<circle cx="{34+9*math.cos(math.radians(a)):.1f}" cy="{70+9*math.sin(math.radians(a)):.1f}" r="3.2" fill="#5A2A8A"/>' for a in range(0, 360, 72)) + f'''
<path d="M2 84 Q34 76 66 84 L64 112 Q34 118 4 112Z" fill="#4FA36B" {s()}/>
<path d="M14 82 V114 M30 79 V116 M46 79 V116 M58 82 V113 M4 94 Q34 88 64 94 M4 104 Q34 100 64 104" stroke="#E94C4C" stroke-width="2.6"/>
''' + f(34, 66, d=7, k=0.55) + sparkle(104, 18, 4, "#FFE9A0"))

# 12. Ивановское (конно-спортивный комплекс) — печенье-лошадка прыгает барьер на манеже
add("cafe-ivanovskoe-konny",
    "печенье-лошадка «козуля» с гривой из глазури",
    "перепрыгивает барьер из шоколадных батончиков на песчаном манеже", "k10_arena", f'''
<path d="M-4 104 H132 V132 H-4Z" fill="#E8CD94" {s()}/>
<path d="M18 104 V80 M110 104 V80" {W(4)}/>
<rect x="14" y="80" width="100" height="9" rx="3" fill="#6B3A22" {s()}/>
<rect x="14" y="92" width="100" height="8" rx="3" fill="#8A4E2C" {s()}/>
<path d="M30 80 V89 M46 80 V89 M62 80 V89 M78 80 V89 M94 80 V89" stroke="#4A2614" stroke-width="2"/>
<g transform="rotate(-14 64 50)">
<path d="M26 56 Q30 40 48 40 L74 40 Q78 22 92 18 Q104 16 106 26 L100 34 Q96 44 92 52 Q90 62 80 64 L50 64 Q36 70 30 76 L22 72 Q30 66 32 62Z" fill="#C98543" {s()}/>
<path d="M50 64 L42 78 M64 64 L60 80 M80 62 L88 76 M86 56 L98 66" {W(6)}/>
<path d="M50 64 L42 78 M64 64 L60 80 M80 62 L88 76 M86 56 L98 66" stroke="#C98543" stroke-width="3" stroke-linecap="round"/>
<path d="M76 38 Q80 24 92 20 M80 42 Q84 30 94 26 M84 46 Q88 36 96 32" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/>
<path d="M40 46 Q50 50 60 46 M42 56 Q52 60 64 56" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 4" stroke-linecap="round"/>
<path d="M26 56 Q14 52 12 62" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
</g>
''' + eye(96, 22, 0.55) + f'<ellipse cx="104" cy="30" rx="3" ry="2" fill="#FF7FA8" opacity=".7"/>' + sparkle(24, 24, 4))

# 13. Сахара — курабье бредёт по барханам под зонтиком
add("cafe-sahara-mkad",
    "песочное печенье-курабье с капелькой варенья",
    "бредёт по барханам пустыни, прикрываясь зонтиком от палящего солнца", "k10_desert", f'''
<circle cx="24" cy="24" r="14" fill="#FFF3A6" {W(2.4)}/>
<path d="M-4 96 Q30 76 60 92 Q92 108 132 86 V132 H-4Z" fill="#F6C66A" {s()}/>
<path d="M-4 114 Q40 100 76 114 Q104 124 132 110 V132 H-4Z" fill="#EBAE4E" {s()}/>
<path d="M98 82 Q104 72 106 60 M106 72 l6 -6 M104 66 l-6 -4" fill="none" stroke="#5B9E4C" stroke-width="3" stroke-linecap="round"/>
<path d="M30 36 Q60 10 92 36Z" fill="#5CC1FF" {s()}/>
<path d="M46 36 Q50 22 61 20 M76 36 Q72 22 61 20" fill="none" {W(2)}/>
<path d="M61 36 V54" {W(3)}/>
''' + "".join(f'<circle cx="{61+20*math.cos(math.radians(a)):.1f}" cy="{74+20*math.sin(math.radians(a)):.1f}" r="9" fill="#F5D7A1" {W(2.4)}/>' for a in range(0, 360, 45)) + f'''
<circle cx="61" cy="74" r="20" fill="#F5D7A1"/>
<circle cx="61" cy="74" r="7" fill="#E9405F" {W(2)}/>
<path d="M44 96 L40 106 M78 96 L84 104" {W(3.5)}/>
''' + eye(52, 66, 0.55) + eye(70, 66, 0.55) + f'''<path d="M56 84 Q61 87 66 84" fill="none" {W(2.2)}/>
<path d="M82 58 q3 5 0 8" fill="#7FD0FF" {W(1.4)}/>''')


if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for pid in ids:
        open(os.path.join(OUT, f"{pid}.svg"), "w").write(ICONS[pid])
    path = os.path.join(OUT, "subjects.txt")
    lines = [l for l in open(path, encoding="utf-8").read().splitlines() if l.split(" — ")[0] not in ids]
    lines += [f"{pid} — герой: {SUBJ[pid][0]} | сцена: {SUBJ[pid][1]}" for pid in ids]
    open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("ok", len(ids))
