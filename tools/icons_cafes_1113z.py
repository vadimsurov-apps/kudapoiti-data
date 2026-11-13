"""Иконки робота cafes, 2026-11-13 (23 UTC). Каждая придумана и нарисована отдельно (правило АБСОЛЮТНОЙ уникальности):
герои и сцены сверены поиском по icons-src/subjects.txt; палитры фона — свои.
Запуск: python3 tools/icons_cafes_1113z.py [id…]  (без аргументов — все + строки реестра в subjects.txt)"""
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
    "kz_limepeach": ("#F4FFD6", "#E58A4A"),
    "kz_icelilac": ("#EEF2FF", "#6E5BC8"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Додо Пицца (Намёткина, 13Б): корочка пиццы ныряет «солдатиком» в баночку сырного соуса, как в бассейн
add("cafe-dodo-nametkina-13b",
    "маленькая круглая баночка сырного соуса с прозрачной откинутой крышечкой и мордашкой на боку",
    "в неё, как в бассейн, вниз головой ныряет рыжая хлебная корочка пиццы, и во все стороны летят жёлтые брызги соуса",
    "kz_limepeach", f'''
<ellipse cx="62" cy="112" rx="40" ry="7" fill="#C9662F" opacity=".35"/>
<path d="M26 72 L32 108 Q62 118 92 108 L98 72Z" fill="#FFFFFF" {W(3.4)}/>
<ellipse cx="62" cy="72" rx="36" ry="10" fill="#FFC93A" {W(3.2)}/>
<ellipse cx="62" cy="71" rx="26" ry="5" fill="#FFE08A"/>
<path d="M96 66 Q110 52 118 60 Q112 70 100 72Z" fill="#E9F4FF" opacity=".9" {W(2.6)}/>
{eye(50, 92, 1.0)}{eye(74, 92, 1.0)}
<path d="M56 100 Q62 106 68 100" fill="none" {W(2.6)}/>
{BL(42, 99)}{BL(82, 99)}
<g transform="rotate(-12 60 40)">
<path d="M48 64 L52 18 Q60 10 70 18 L72 64 Q60 70 48 64Z" fill="#E4943E" {W(3.2)}/>
<path d="M52 24 Q60 18 68 24" fill="none" stroke="#F6C27A" stroke-width="3" stroke-linecap="round"/>
<circle cx="58" cy="38" r="2" fill="#B5652A"/><circle cx="64" cy="50" r="2" fill="#B5652A"/><circle cx="57" cy="56" r="1.8" fill="#B5652A"/>
</g>
<g fill="#FFC93A" stroke="{O}" stroke-width="2">
<circle cx="24" cy="56" r="4.5"/><circle cx="14" cy="70" r="3"/><circle cx="102" cy="44" r="3.6"/><circle cx="34" cy="40" r="2.8"/><circle cx="90" cy="30" r="2.4"/>
</g>
{sparkle(20, 30, 4)}{sparkle(108, 92, 3.5)}
''')

# 2. Yellowfin by Bluefin (ЗИЛАРТ): жёлтый плавник тунца кружит в соуснице, как акулий, а ролл поджал ножки на бортике
add("cafe-yellowfin-zilart",
    "острый жёлтый плавник тунца, торчащий из тёмного соевого соуса",
    "нарезает круги, как акулий, в квадратной чёрной соуснице, а на её бортике испуганно поджал ножки маленький ролл-маки с округлившимися глазами",
    "kz_icelilac", f'''
<path d="M14 70 L114 70 L106 112 L22 112Z" fill="#2B2B3A" {W(3.4)}/>
<path d="M20 74 L108 74 L104 86 Q64 92 24 86Z" fill="#6B3A22"/>
<path d="M30 80 Q44 74 58 80 M70 82 Q84 76 98 82" fill="none" stroke="#9A5A34" stroke-width="2.4" stroke-linecap="round"/>
<path d="M46 82 Q56 44 74 30 Q72 56 82 82Z" fill="#FFD21F" {W(3.2)}/>
<path d="M58 78 Q64 56 72 42" fill="none" stroke="#F0A800" stroke-width="2.4" stroke-linecap="round"/>
<path d="M34 86 Q40 82 46 86 M82 86 Q88 82 94 86" fill="none" stroke="#C78A5E" stroke-width="2" stroke-linecap="round"/>
<g>
<path d="M94 60 L94 50 L118 50 L118 60" fill="none" {W(2.2)}/>
<rect x="92" y="38" width="28" height="22" rx="10" fill="#1E3B2A" {W(3)}/>
<ellipse cx="106" cy="40" rx="12" ry="5" fill="#FFFFFF" {W(2.4)}/>
<circle cx="106" cy="40" r="3" fill="#F06A4A"/>
<path d="M98 60 L96 68 M114 60 L116 68" {W(2.6)}/>
<circle cx="101" cy="50" r="3" fill="#fff" {W(1.6)}/><circle cx="111" cy="50" r="3" fill="#fff" {W(1.6)}/>
<circle cx="101" cy="50" r="1.2" fill="{O}"/><circle cx="111" cy="50" r="1.2" fill="{O}"/>
<ellipse cx="106" cy="56" rx="2" ry="1.6" fill="{O}"/>
</g>
<path d="M40 26 Q46 20 52 26 M30 40 Q34 36 38 40" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"/>
{sparkle(24, 54, 4)}{sparkle(84, 20, 3.5)}
''')

draw_icons.BG.update({
    "kz_papercream": ("#FFF9EC", "#B98A5A"),
    "kz_pinemorning": ("#E9FFF0", "#3E8F5C"),
})

# 3. Эссе (Никитинская, 13): кафе-кофейня «Эссе» — капучино с буквой «Э» на пенке пишет сочинение
add("cafe-esse-nikitinskaya-13",
    "белая чашка капучино с буквой «Э», нарисованной молочной пенкой",
    "стоит на раскрытой тетради в линейку, а рядом гусиное перо выводит строчку кофейными чернилами",
    "kz_papercream", f'''
<path d="M10 92 L64 80 L118 92 L118 118 L64 108 L10 118Z" fill="#FFFFFF" {W(3)}/>
<path d="M64 80 L64 108" {W(2.4)}/>
<g stroke="#9CC3E6" stroke-width="1.6"><path d="M16 98 L58 89 M16 104 L58 95 M16 110 L58 101 M70 89 L112 98 M70 95 L112 104"/></g>
<path d="M72 101 Q78 97 84 101 Q90 105 96 101" fill="none" stroke="#6B3E1F" stroke-width="2.4" stroke-linecap="round"/>
<path d="M98 100 L120 52 Q124 46 122 58 L102 102Z" fill="#FFFFFF" {W(2.6)}/>
<path d="M104 92 L118 60" stroke="#D8D8E8" stroke-width="1.6"/>
<ellipse cx="44" cy="86" rx="32" ry="6" fill="#E8D8C4" {W(2.6)}/>
<path d="M18 46 L22 80 Q44 92 66 80 L70 46Z" fill="#FFFFFF" {W(3.4)}/>
<path d="M68 54 Q84 54 82 66 Q80 76 66 74" fill="none" {W(3.4)}/>
<ellipse cx="44" cy="46" rx="26" ry="8" fill="#C8894E" {W(3)}/>
<ellipse cx="44" cy="46" rx="18" ry="5" fill="#FFF3DF"/>
<path d="M48 43 Q40 41 38 44 M40 46 L47 46 M38 48 Q42 51 48 49" fill="none" stroke="#C8894E" stroke-width="1.8" stroke-linecap="round"/>
{eye(36, 64, 0.9)}{eye(52, 64, 0.9)}
<path d="M40 72 Q44 76 48 72" fill="none" {W(2.4)}/>
{BL(30, 71)}{BL(58, 71)}
<path d="M34 34 Q30 26 36 20 M50 32 Q46 22 54 14" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>
{sparkle(96, 28, 4)}{sparkle(14, 30, 3)}
''')

# 4. Додо Пицца (Туристская, 23): кусок пиццы-путешественник с рюкзаком идёт в поход к флажку на холме
add("cafe-dodo-turistskaya-23",
    "кусок пиццы-путешественник с огромным оранжевым походным рюкзаком и треккинговой палкой",
    "бодро шагает по извилистой тропинке вверх к красному флажку на зелёном холме",
    "kz_pinemorning", f'''
<path d="M-4 112 Q40 84 74 92 Q104 98 132 80 L132 132 L-4 132Z" fill="#7CCB6A" {W(3)}/>
<path d="M20 110 Q46 98 66 102 Q90 106 104 90" fill="none" stroke="#E8D6A8" stroke-width="5" stroke-linecap="round"/>
<path d="M104 90 L104 64" {W(2.4)}/><path d="M104 64 L120 70 L104 76Z" fill="#E23B3B" {W(2)}/>
<path d="M30 30 L40 82 L74 64Z" fill="#FF9F2E" {W(3.2)}/>
<path d="M34 30 Q50 18 62 28 L70 62 L40 78Z" fill="#FFB648" {W(3.2)}/>
<path d="M38 44 L60 40" stroke="{O}" stroke-width="2.4"/>
<path d="M54 46 L94 34 L70 92Z" fill="#FFD866" {W(3.2)}/>
<path d="M50 44 Q72 30 96 32 Q98 40 94 40 Q72 40 56 50Z" fill="#E09A4A" {W(3)}/>
<circle cx="74" cy="56" r="4.5" fill="#D9453A" {W(1.8)}/><circle cx="76" cy="76" r="3.8" fill="#D9453A" {W(1.8)}/>
<path d="M66 66 L70 70" stroke="#4FA34A" stroke-width="3" stroke-linecap="round"/>
{eye(68, 48, 0.85)}{eye(82, 46, 0.85)}
<path d="M70 58 Q76 62 82 56" fill="none" {W(2.2)}/>
<path d="M66 86 L60 100 M74 90 L80 102" {W(3)}/>
<path d="M84 50 L100 46 M100 40 L96 104" {W(2.8)}/>
<circle cx="100" cy="40" r="2.6" fill="#3B6FD1" {W(1.6)}/>
{sparkle(18, 22, 4)}{sparkle(110, 18, 3.5)}
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
