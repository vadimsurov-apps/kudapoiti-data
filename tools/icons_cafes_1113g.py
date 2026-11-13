"""Иконки робота cafes, 2026-11-13 (11 UTC). Каждая придумана и нарисована отдельно (правило АБСОЛЮТНОЙ уникальности):
герои и сцены сверены поиском по icons-src/subjects.txt; палитры фона — свои.
Запуск: python3 tools/icons_cafes_1113g.py [id…]  (без аргументов — все + строки реестра в subjects.txt)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
BL = lambda x, y: f'<ellipse cx="{x}" cy="{y}" rx="3.6" ry="2.1" fill="#FF7FA8" opacity=".7"/>'
draw_icons.BG.update({
    "zg_mintlace": ("#E4F7E9", "#7FC79A"),
    "zg_plumdusk": ("#F3E1F2", "#9B6BA8"),
    "zg_festnight": ("#4A5FA8", "#1C2350"),
    "zg_honeyglow": ("#FFF4C9", "#F2B33D"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Osteria Mario (Зелёный проспект, Новогиреево): римская булочка маритоццо отрастила пышные сливочные усы
add("cafe-osteria-zeleny-81",
    "римская булочка маритоццо, разрезанная сверху и щедро набитая взбитыми сливками, с сахарной пудрой на макушке",
    "лежит на мятно-зелёном блюдце и гордо щеголяет пышными закрученными усами из взбитых сливок",
    "zg_mintlace", f'''
<ellipse cx="64" cy="104" rx="52" ry="13" fill="#FFFFFF" {W(3)}/>
<ellipse cx="64" cy="102" rx="38" ry="7" fill="#BFE8CC"/>
<path d="M18 92 Q14 50 64 40 Q114 50 110 92 Q64 104 18 92Z" fill="#E9A659" {W(3.2)}/>
<path d="M26 56 Q64 34 102 56 Q64 62 26 56Z" fill="#FFFDF6" {W(2.6)}/>
<g fill="#FFFFFF" opacity=".9"><circle cx="52" cy="46" r="1.6"/><circle cx="64" cy="44" r="1.8"/><circle cx="76" cy="47" r="1.5"/><circle cx="58" cy="49" r="1.2"/><circle cx="70" cy="50" r="1.3"/></g>
{eye(50, 64, 1.0)}{eye(78, 64, 1.0)}
{BL(40, 74)}{BL(88, 74)}
<path d="M64 76 Q52 70 40 76 Q30 82 24 74 Q26 88 42 86 Q54 84 64 80 Q74 84 86 86 Q102 88 104 74 Q98 82 88 76 Q76 70 64 76Z" fill="#FFFDF6" {W(2.8)}/>
<path d="M56 90 Q64 95 72 90" fill="none" {W(2.4)}/>
{sparkle(104, 34, 5)}{sparkle(24, 40, 3.5)}
''')

# 2. Osteria Mario (Пятницкая, Замоскворечье): клубок тальятелле вяжет сам себя палочками гриссини
add("cafe-osteria-pyatnitskaya-25a",
    "круглый клубок жёлтой яичной пасты тальятелле с выбившейся длинной лентой",
    "как бабушкина пряжа, вяжет сам себя двумя хлебными палочками гриссини вместо спиц, сидя на фиолетовом пуфике",
    "zg_plumdusk", f'''
<ellipse cx="64" cy="112" rx="40" ry="12" fill="#7A3E8C" {W(3)}/>
<ellipse cx="64" cy="108" rx="34" ry="7" fill="#B477C4"/>
<circle cx="64" cy="70" r="38" fill="#F7D35A" {W(3.2)}/>
<g fill="none" stroke="#D9A92A" stroke-width="3.4" stroke-linecap="round">
<path d="M30 58 Q64 44 98 62"/><path d="M28 74 Q64 60 100 78"/><path d="M34 90 Q64 78 94 94"/><path d="M48 36 Q40 70 52 104"/><path d="M80 36 Q92 70 80 104"/></g>
<path d="M98 82 Q114 94 108 110 Q104 122 120 126" fill="none" stroke="#F7D35A" stroke-width="6" stroke-linecap="round"/>
<path d="M98 82 Q114 94 108 110 Q104 122 120 126" fill="none" stroke="#B88A1C" stroke-width="1.4" stroke-linecap="round" opacity=".6"/>
<circle cx="64" cy="70" r="38" fill="none" {W(3.2)}/>
{eye(52, 60, 1.0)}{eye(76, 60, 1.0)}
{BL(44, 70)}{BL(84, 70)}
<path d="M58 72 Q64 77 70 72" fill="none" {W(2.4)}/>
<path d="M54 100 L74 100 L72 120 L56 120Z" fill="#F7D35A" {W(2.4)}/>
<path d="M56 106 L72 106 M56 112 L72 112" stroke="#D9A92A" stroke-width="2"/>
<line x1="10" y1="114" x2="84" y2="92" stroke="{O}" stroke-width="10" stroke-linecap="round"/>
<line x1="10" y1="114" x2="84" y2="92" stroke="#E2B677" stroke-width="5.4" stroke-linecap="round"/>
<line x1="118" y1="114" x2="44" y2="92" stroke="{O}" stroke-width="10" stroke-linecap="round"/>
<line x1="118" y1="114" x2="44" y2="92" stroke="#E2B677" stroke-width="5.4" stroke-linecap="round"/>
<g fill="#B9813D"><circle cx="24" cy="110" r="1.2"/><circle cx="38" cy="106" r="1.2"/><circle cx="104" cy="110" r="1.2"/><circle cx="90" cy="106" r="1.2"/></g>
{sparkle(64, 18, 4.5)}
''')


# 3. Фестиваль (Фрязино, ресторан-пиццерия): пицца с сырным бортом любуется салютом
add("cafe-festival-fryazino-60-let-sssr",
    "круглая пицца с пухлым сырным бортом из золотистых подушечек и зелёными кружками перца",
    "стоит на ребре ночью и, разинув рот от восторга, любуется разноцветным праздничным салютом в тёмно-синем небе",
    "zg_festnight", f'''
<g stroke-linecap="round" stroke-width="3">
<g stroke="#FF6B8A"><path d="M30 30 L30 18 M30 30 L20 24 M30 30 L40 24 M30 30 L22 36 M30 30 L38 36"/></g>
<g stroke="#7FE0FF"><path d="M98 22 L98 10 M98 22 L88 16 M98 22 L108 16 M98 22 L90 30 M98 22 L106 30"/></g>
<g stroke="#FFE066"><path d="M64 14 L64 4 M64 14 L56 9 M64 14 L72 9"/></g></g>
<circle cx="64" cy="80" r="40" fill="#F0B04A" {W(3.2)}/>
<g fill="#FFD27A" stroke="#C98A2A" stroke-width="1.8">
<circle cx="64" cy="42" r="6"/><circle cx="83" cy="47" r="6"/><circle cx="97" cy="61" r="6"/><circle cx="102" cy="80" r="6"/><circle cx="97" cy="99" r="6"/><circle cx="83" cy="113" r="6"/>
<circle cx="45" cy="47" r="6"/><circle cx="31" cy="61" r="6"/><circle cx="26" cy="80" r="6"/><circle cx="31" cy="99" r="6"/><circle cx="45" cy="113" r="6"/><circle cx="64" cy="118" r="6"/></g>
<circle cx="64" cy="80" r="31" fill="#E8553E"/>
<path d="M40 74 Q46 70 52 74 Q58 70 64 74" fill="none" stroke="#FFE9A8" stroke-width="5" stroke-linecap="round"/>
<g fill="none" stroke="#3FA34D" stroke-width="3"><circle cx="44" cy="96" r="4.5"/><circle cx="86" cy="96" r="4.5"/></g>
{eye(54, 70, 1.0)}{eye(74, 70, 1.0)}
<ellipse cx="64" cy="90" rx="6" ry="7.5" fill="#7A1F2B" {W(2.4)}/>
{BL(46, 82)}{BL(82, 82)}
''')

# 4. Мельница (Павловский Посад, пиццерия): пицца-сердце обнимает свой маленький кусочек
add("cafe-melnitsa-pavlovsky-posad-gertsena",
    "пицца в форме сердца с румяным бортиком, сыром и тремя кружками пепперони",
    "нежно обнимает двумя ручками маленький треугольный кусочек пиццы, будто своего малыша",
    "zg_honeyglow", f'''
<path d="M64 116 Q14 84 14 50 Q14 22 40 22 Q56 22 64 38 Q72 22 88 22 Q114 22 114 50 Q114 84 64 116Z" fill="#D98C3A" {W(3.2)}/>
<path d="M64 106 Q22 80 22 52 Q22 30 41 30 Q55 30 64 46 Q73 30 87 30 Q106 30 106 52 Q106 80 64 106Z" fill="#FFD85E"/>
<g fill="#D8343E" stroke="#8E1E26" stroke-width="1.6"><circle cx="38" cy="50" r="6"/><circle cx="92" cy="48" r="6"/><circle cx="90" cy="80" r="5.5"/></g>
{eye(52, 52, 1.0)}{eye(76, 52, 1.0)}
<path d="M58 62 Q64 67 70 62" fill="none" {W(2.4)}/>
{BL(44, 62)}{BL(84, 62)}
<path d="M48 78 L80 78 L64 104Z" fill="#FFD85E" {W(2.6)}/>
<path d="M46 72 Q64 66 82 72 L80 79 Q64 74 48 79Z" fill="#D98C3A" {W(2.4)}/>
<circle cx="64" cy="88" r="3.6" fill="#D8343E" stroke="#8E1E26" stroke-width="1.2"/>
<circle cx="59" cy="81" r="1.5" fill="{O}"/><circle cx="69" cy="81" r="1.5" fill="{O}"/>
<path d="M32 74 Q42 92 56 92" fill="none" {W(6)}/><path d="M32 74 Q42 92 56 92" fill="none" stroke="#D98C3A" stroke-width="3.4" stroke-linecap="round"/>
<path d="M96 74 Q86 92 72 92" fill="none" {W(6)}/><path d="M96 74 Q86 92 72 92" fill="none" stroke="#D98C3A" stroke-width="3.4" stroke-linecap="round"/>
{sparkle(108, 104, 5)}{sparkle(18, 106, 3.5)}
''')


if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for pid in ids:
        open(os.path.join(OUT, f"{pid}.svg"), "w").write(ICONS[pid])
    if not sys.argv[1:]:
        p = os.path.join(OUT, "subjects.txt")
        have = {l.split(" — ", 1)[0] for l in open(p, encoding="utf-8")}
        with open(p, "a", encoding="utf-8") as f:
            for pid in ids:
                if pid not in have:
                    h, sc = SUBJ[pid]
                    f.write(f"{pid} — герой: {h} | сцена: {sc}\n")
    print("svg", len(ids))
