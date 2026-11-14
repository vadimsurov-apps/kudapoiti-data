"""Иконки робота cafes, 2026-11-14 (05 UTC). Каждая придумана и нарисована отдельно (правило АБСОЛЮТНОЙ уникальности):
герои и сцены сверены поиском по icons-src/subjects.txt; палитры фона — свои.
Запуск: python3 tools/icons_cafes_1114c.py [id…]  (без аргументов — все + строки реестра в subjects.txt)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
BL = lambda x, y: f'<ellipse cx="{x}" cy="{y}" rx="3.4" ry="2" fill="#FF7FA8" opacity=".75"/>'
draw_icons.BG.update({
    "kc_tangerine": ("#FFF6D9", "#F08A24"),
    "kc_heaven": ("#FFF0FA", "#9C8CE8"),
    "kc_river": ("#E6FBFF", "#2C8FB8"),
    "kc_lime": ("#F4FFD9", "#6FB536"),
    "kc_velvet": ("#FFE9EF", "#7E1F45"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Eat Arena (фудмолл, детская комната): пейджер-«пищалка» фудкорта подпрыгивает на подносе — заказ готов!
add("cafe-eat-arena-michurinsky-13a",
    "круглый чёрный пейджер-«пищалка» фудкорта с красными огоньками по ободку и мордашкой",
    "радостно подпрыгивает и жужжит на оранжевом подносе рядом с пышным бургером — заказ готов",
    "kc_tangerine", f"""
<path d="M10 100 L118 100 L110 120 L18 120Z" fill="#FF8A1F" {W(3.2)}/>
<path d="M16 104 L112 104" stroke="#FFC37A" stroke-width="3"/>
<g>
<path d="M66 90 Q66 70 90 70 Q114 70 114 90Z" fill="#F2A541" {W(3)}/>
<g fill="#FFF3D6"><ellipse cx="80" cy="78" rx="2" ry="1.2"/><ellipse cx="92" cy="75" rx="2" ry="1.2"/><ellipse cx="103" cy="80" rx="2" ry="1.2"/></g>
<path d="M64 90 Q74 86 80 92 Q88 86 96 92 Q104 86 116 90 L116 93 L64 93Z" fill="#7CCB4A" {W(2.4)}/>
<rect x="64" y="92" width="52" height="6" rx="3" fill="#8A4B2C" {W(2.4)}/>
<path d="M64 98 L116 98 Q116 102 90 102 Q64 102 64 98Z" fill="#E9A043" {W(2.4)}/>
</g>
<g transform="translate(-2 -6)">
<ellipse cx="40" cy="96" rx="22" ry="5" fill="#000" opacity=".15"/>
<circle cx="40" cy="62" r="27" fill="#2E2A33" {W(3.2)}/>
<circle cx="40" cy="62" r="20" fill="#47414F"/>
<g fill="#FF3B3B" stroke="#fff" stroke-width="1"><circle cx="40" cy="37" r="3.2"/><circle cx="58" cy="44" r="3.2"/><circle cx="65" cy="62" r="3.2"/><circle cx="58" cy="80" r="3.2"/><circle cx="22" cy="44" r="3.2"/><circle cx="15" cy="62" r="3.2"/><circle cx="22" cy="80" r="3.2"/><circle cx="40" cy="87" r="3.2"/></g>
<circle cx="31" cy="58" r="5.2" fill="#fff"/><circle cx="49" cy="58" r="5.2" fill="#fff"/>
{eye(31, 59, .9)}{eye(49, 59, .9)}
<path d="M33 68 Q40 76 47 68Z" fill="#FF6B8A" {W(2.2)}/>
</g>
<path d="M6 46 Q2 54 6 62 M12 42 Q6 54 12 66" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M74 32 Q80 40 74 48 M80 28 Q88 40 80 52" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
{sparkle(100, 30, 6)}
""")

# 2. Ресторай («рай»; паста, детский уголок): тарелка спагетти с нимбом и крылышками парит на облачке
add("cafe-restorai-pasternaka-12",
    "белая тарелка спагетти карбонара с вилкой, на которую накручена паста, — с золотым нимбом и пёстрыми крылышками",
    "блаженно парит на розовом облачке, жмурясь от удовольствия",
    "kc_heaven", f"""
<path d="M14 106 Q12 92 28 92 Q32 80 48 86 Q60 76 74 86 Q90 80 96 92 Q116 92 112 106 Q110 116 96 114 L28 114 Q14 116 14 106Z" fill="#FFD3E8" {W(3)}/>
<path d="M16 72 Q2 60 8 44 Q20 52 26 64Z" fill="#FFFFFF" {W(2.8)}/>
<path d="M112 72 Q126 60 120 44 Q108 52 102 64Z" fill="#FFFFFF" {W(2.8)}/>
<path d="M12 52 L22 60 M10 60 L20 66" stroke="#C9B8FF" stroke-width="2.4"/>
<path d="M116 52 L106 60 M118 60 L108 66" stroke="#C9B8FF" stroke-width="2.4"/>
<ellipse cx="64" cy="80" rx="44" ry="14" fill="#FFFFFF" {W(3.2)}/>
<ellipse cx="64" cy="77" rx="32" ry="8" fill="#F3F0FA"/>
<path d="M36 76 Q44 58 64 58 Q84 58 92 76 Q80 82 64 82 Q46 82 36 76Z" fill="#FFE08A" {W(3)}/>
<path d="M42 72 Q52 62 62 70 Q72 60 84 72 M46 76 Q58 68 68 76 Q76 68 86 76" fill="none" stroke="#E8B64A" stroke-width="2.2"/>
<g fill="#D9785A"><rect x="50" y="64" width="6" height="4" rx="1.5"/><rect x="72" y="66" width="6" height="4" rx="1.5"/></g>
<path d="M60 58 L56 30" stroke="#B9C3CF" stroke-width="3.4" stroke-linecap="round"/>
<path d="M50 30 L50 22 M54 30 L54 21 M58 30 L58 21 M62 30 L62 22" stroke="#B9C3CF" stroke-width="2.4" stroke-linecap="round"/>
<ellipse cx="57" cy="40" rx="9" ry="6" fill="#FFE08A" {W(2.4)}/>
<path d="M50 38 Q57 44 64 38 M50 42 Q57 47 64 42" fill="none" stroke="#E8B64A" stroke-width="1.6"/>
<path d="M54 68 Q57 66 60 68 M68 68 Q71 66 74 68" fill="none" {W(2.6)}/>
<path d="M58 74 Q64 79 70 74" fill="none" {W(2.4)}/>
{BL(50, 73)}{BL(78, 73)}
<ellipse cx="86" cy="22" rx="16" ry="5" fill="none" stroke="#FFC93C" stroke-width="4.5"/>
{sparkle(104, 40, 5)}{sparkle(24, 30, 4)}
""")

# 3. Хинкали-Gали! (Речной вокзал, обжаренные хинкали): румяный жареный хинкали-капитан на речном трамвайчике
add("cafe-hinkali-gali-festivalnaya-39",
    "румяный обжаренный хинкали с золотистой корочкой в белой капитанской фуражке с чёрным козырьком",
    "стоит на носу маленького бело-синего речного трамвайчика с красной трубой и отдаёт честь, под ним волны",
    "kc_river", f"""
<path d="M0 104 Q16 96 32 104 Q48 112 64 104 Q80 96 96 104 Q112 112 128 104 L128 128 L0 128Z" fill="#1E6F9A"/>
<path d="M16 86 L112 86 L102 106 L26 106Z" fill="#FFFFFF" {W(3.2)}/>
<path d="M22 96 L106 96" stroke="#2C5DB8" stroke-width="4"/>
<g fill="#9FD8F2" {W(2)}><circle cx="40" cy="91" r="2.6"/><circle cx="52" cy="91" r="2.6"/><circle cx="76" cy="91" r="2.6"/><circle cx="88" cy="91" r="2.6"/></g>
<rect x="88" y="62" width="12" height="24" rx="2" fill="#E8453C" {W(3)}/>
<rect x="88" y="66" width="12" height="4" fill="#2E2A33"/>
<circle cx="100" cy="52" r="5" fill="#fff" opacity=".85"/><circle cx="108" cy="42" r="3.5" fill="#fff" opacity=".7"/>
<path d="M40 50 Q26 58 24 76 Q28 88 46 88 Q64 88 68 76 Q66 58 52 50Z" fill="#E7A24A" {W(3.2)}/>
<path d="M46 50 Q38 64 34 86 M46 50 Q46 66 46 88 M46 50 Q54 64 58 86" fill="none" stroke="#C47A2A" stroke-width="2.2"/>
<path d="M30 80 Q46 86 64 80" fill="none" stroke="#A65F1C" stroke-width="2.4"/>
<path d="M30 46 Q46 34 62 46 L60 52 Q46 46 32 52Z" fill="#FFFFFF" {W(2.8)}/>
<path d="M30 52 Q46 48 62 52 Q64 56 58 56 L34 56 Q28 56 30 52Z" fill="#2E2A33"/>
<circle cx="46" cy="44" r="2.6" fill="#FFC93C" {W(1.4)}/>
{eye(40, 66, .85)}{eye(52, 66, .85)}
<path d="M42 74 Q46 78 50 74" fill="none" {W(2.4)}/>
{BL(35, 72)}{BL(57, 72)}
<path d="M64 62 Q72 52 66 42" fill="none" {W(3)}/>
""")

# 4. Додо Пицца (Одесская ул.; детская комната): румяный ролл-тортилья в полосатой салфетке качается на пружинной качалке
add("cafe-dodo-odesskaya-16",
    "поджаристый ролл-тортилья с ломтиками томата и курицы на срезе, обёрнутый в сине-белую полосатую салфетку",
    "катается на зелёной пружинной качалке-жучке из детской комнаты, раскинув лапки, рядом пляшут два мячика",
    "kc_lime", f"""
<path d="M56 116 Q58 106 50 100 Q44 96 52 92 Q60 88 64 94 Q70 100 64 108 Q60 114 70 118" fill="none" stroke="#7A7A88" stroke-width="5" stroke-linecap="round"/>
<rect x="36" y="114" width="56" height="8" rx="3" fill="#5E5A6A" {W(2.6)}/>
<path d="M22 86 Q28 70 60 70 Q96 70 104 86 Q98 96 64 96 Q30 96 22 86Z" fill="#43B05C" {W(3.2)}/>
<g fill="#2E2A33"><circle cx="46" cy="80" r="3.4"/><circle cx="64" cy="76" r="3.4"/><circle cx="82" cy="80" r="3.4"/></g>
<circle cx="102" cy="76" r="8" fill="#43B05C" {W(2.8)}/>
<path d="M100 68 Q98 60 92 58 M104 68 Q108 60 114 60" fill="none" {W(2.4)}/>
<g transform="rotate(-14 56 50)">
<rect x="34" y="28" width="40" height="46" rx="18" fill="#F0C27A" {W(3.2)}/>
<ellipse cx="54" cy="31" rx="18" ry="7" fill="#FFE3A8" {W(2.6)}/>
<circle cx="47" cy="31" r="3" fill="#E8453C"/><circle cx="60" cy="30" r="3" fill="#F5F0E6" {W(1.2)}/><circle cx="54" cy="33" r="2.4" fill="#5CC14D"/>
<path d="M34 50 L74 50 L74 74 Q54 80 34 74Z" fill="#FFFFFF" {W(3)}/>
<path d="M34 56 L74 56 M34 63 L74 63 M34 70 L74 70" stroke="#3E6FD8" stroke-width="3"/>
<g fill="#C98A3E" opacity=".6"><circle cx="40" cy="40" r="1.6"/><circle cx="68" cy="42" r="1.6"/></g>
{eye(47, 42, .8)}{eye(61, 42, .8)}
<path d="M50 46 Q54 50 58 46" fill="none" {W(2.2)}/>
<path d="M34 46 Q22 38 22 28 M74 44 Q86 36 88 26" fill="none" {W(3)}/>
</g>
<circle cx="16" cy="104" r="7" fill="#FFC93C" {W(2.6)}/>
<circle cx="112" cy="104" r="7" fill="#FF6B8A" {W(2.6)}/>
{sparkle(20, 40, 5)}
""")

# 5. Velluto («бархат»; кофейня с эклерами, детский уголок): малиново-фисташковый эклер дремлет на бархатной подушке
add("cafe-velluto-chongarsky-9",
    "длинный эклер с малиновой глазурью и посыпкой из рубленой фисташки, с сонной мордашкой",
    "сладко дремлет на бордовой бархатной подушке с золотыми кисточками по углам, над ним плывут буквы «z»",
    "kc_velvet", f"""
<path d="M14 92 Q14 74 30 72 L98 70 Q114 70 114 88 Q114 104 98 106 L30 108 Q14 108 14 92Z" fill="#9E2B55" {W(3.2)}/>
<path d="M22 80 Q64 86 106 78" fill="none" stroke="#C4527D" stroke-width="3" stroke-linecap="round"/>
<g fill="#F2C14E" {W(2)}><path d="M14 72 L8 64 L18 66Z"/><path d="M114 70 L122 62 L120 74Z"/><path d="M14 108 L6 114 L18 116Z"/><path d="M114 106 L122 112 L112 116Z"/></g>
<path d="M24 74 Q24 58 40 56 L92 54 Q106 54 106 68 Q106 80 90 80 L40 82 Q24 82 24 74Z" fill="#E9B46A" {W(3.2)}/>
<path d="M26 66 Q26 54 40 52 L92 50 Q104 50 104 60 Q100 66 92 64 Q84 68 76 64 Q66 70 58 64 Q48 70 40 64 Q30 70 26 66Z" fill="#E64C7C" {W(3)}/>
<g fill="#8DC63F"><rect x="40" y="56" width="3" height="2" rx="1"/><rect x="56" y="54" width="3" height="2" rx="1"/><rect x="72" y="56" width="3" height="2" rx="1"/><rect x="86" y="54" width="3" height="2" rx="1"/><rect x="48" y="60" width="3" height="2" rx="1"/><rect x="80" y="60" width="3" height="2" rx="1"/></g>
<path d="M50 72 Q54 75 58 72 M70 72 Q74 75 78 72" fill="none" {W(2.6)}/>
<ellipse cx="64" cy="77" rx="3" ry="2" fill="#B5475C"/>
{BL(44, 76)}{BL(84, 76)}
<g fill="#FFFFFF" font-family="Arial" font-weight="bold"><text x="88" y="40" font-size="14">z</text><text x="100" y="28" font-size="11">z</text><text x="108" y="18" font-size="8">z</text></g>
{sparkle(26, 34, 5)}
"""
)


if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for pid in ids:
        open(os.path.join(OUT, pid + ".svg"), "w").write(ICONS[pid])
    if not sys.argv[1:]:
        reg = os.path.join(OUT, "subjects.txt")
        have = open(reg).read()
        with open(reg, "a") as f:
            for pid in ids:
                if pid + " —" not in have:
                    f.write(f"{pid} — герой: {SUBJ[pid][0]} | сцена: {SUBJ[pid][1]}\n")
    print("svg:", len(ids))
