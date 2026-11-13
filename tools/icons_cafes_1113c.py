"""Иконки робота cafes, 2026-11-13 (05 UTC). Каждая придумана и нарисована отдельно (правило АБСОЛЮТНОЙ уникальности):
герои и сцены сверены поиском по icons-src/subjects.txt и просмотром всех листов icons-catalog; палитры фона — свои.
Запуск: python3 tools/icons_cafes_1113c.py [id…]  (без аргументов — все + строки реестра в subjects.txt)"""
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
    "zc_lagoon": ("#E6FFF6", "#5FC9B0"),
    "zc_night": ("#3E5FA8", "#162447"),
    "zc_apricot": ("#FFF1DC", "#F0A86A"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Додо (Давыдковская): черепашка несёт пиццу-панцирь
add("cafe-dodo-davydkovskaya-8",
    "зелёная черепашка, у которой панцирь — круглая пицца пепперони с румяным бортиком",
    "неспешно ползёт по красно-белой клетчатой скатерти, за ней тянется пунктир следов",
    "zc_lagoon", f'''
<path d="M-4 92 L132 84 L132 132 L-4 132Z" fill="#FFFFFF" {W(3)}/>
<g fill="#F26B6B" opacity=".85"><path d="M-4 92 L14 91 L16 132 L-4 132Z"/><path d="M34 90 L52 89 L54 132 L36 132Z"/><path d="M72 88 L90 87 L92 132 L74 132Z"/><path d="M110 86 L128 85 L130 132 L112 132Z"/></g>
<path d="M-4 108 L132 102 M-4 122 L132 116" stroke="#F26B6B" stroke-width="7" opacity=".45"/>
<g fill="{O}" opacity=".35"><circle cx="12" cy="86" r="2.2"/><circle cx="20" cy="83" r="2.2"/><circle cx="4" cy="89" r="2.2"/></g>
<path d="M30 92 Q26 102 32 104 Q38 104 38 94Z" fill="#7BCF6A" {W(2.6)}/>
<path d="M84 92 Q82 104 90 104 Q96 102 92 92Z" fill="#7BCF6A" {W(2.6)}/>
<path d="M92 72 Q110 64 112 76 Q112 88 96 84Z" fill="#7BCF6A" {W(3)}/>
{eye(103, 74, 0.8)}
<path d="M104 81 Q108 83 110 80" fill="none" {W(1.8)}/>
{BL(98, 80)}
<path d="M24 82 L16 86" {W(3)}/>
<ellipse cx="60" cy="74" rx="38" ry="24" fill="#E39A4A" {W(3.2)}/>
<ellipse cx="60" cy="72" rx="31" ry="18" fill="#FFD66B" {W(2.2)}/>
<g fill="#D9473C" stroke="{O}" stroke-width="1.8"><circle cx="46" cy="66" r="5.4"/><circle cx="66" cy="62" r="5.4"/><circle cx="74" cy="78" r="5.4"/><circle cx="52" cy="80" r="5.4"/></g>
<g fill="#FFFFFF" opacity=".55"><circle cx="45" cy="64" r="1.4"/><circle cx="65" cy="60" r="1.4"/><circle cx="73" cy="76" r="1.4"/><circle cx="51" cy="78" r="1.4"/></g>
<path d="M60 62 L62 58 M80 68 L84 66" stroke="#6DBF5A" stroke-width="3" stroke-linecap="round"/>
''')

# 2. Osteria Mario (Котельники): панеттоне-маяк светит над лагуной
add("cafe-osteria-mario-kotelniki",
    "высокий панеттоне в бумажной обёртке в красно-белую полоску, превращённый в маяк с окошком-изюминкой",
    "стоит на скалистом островке ночью и светит жёлтым лучом над тёмной водой, рядом мерцают звёзды",
    "zc_night", f'''
<path d="M-4 104 Q30 96 64 104 Q98 112 132 102 L132 132 L-4 132Z" fill="#2C7FB8" {W(3)}/>
<path d="M10 114 Q20 110 30 114 M90 118 Q100 114 110 118" fill="none" stroke="#9BD3F2" stroke-width="2.4" stroke-linecap="round"/>
<path d="M66 40 L132 18 L132 52Z" fill="#FFE37A" opacity=".55"/>
<path d="M36 104 Q40 90 64 90 Q88 90 92 104Z" fill="#8C8A9E" {W(3)}/>
<path d="M44 92 L48 62 L80 62 L84 92Z" fill="#FFFFFF" {W(3)}/>
<path d="M45 84 L83 84 L82 76 L46 76Z M47 68 L81 68 L80.5 64 L47.5 64Z" fill="#E8474C"/>
<path d="M44 92 L48 62 L80 62 L84 92Z" fill="none" {W(3)}/>
<path d="M42 64 Q40 34 64 30 Q88 34 86 64 Q64 70 42 64Z" fill="#E7A24C" {W(3.2)}/>
<path d="M50 40 Q56 36 60 40 M70 38 Q74 34 78 40" fill="none" stroke="#B9702A" stroke-width="2" stroke-linecap="round"/>
<ellipse cx="64" cy="22" rx="6" ry="5" fill="#FFE37A" {W(2.6)}/>
<path d="M64 27 L64 30" {W(2.4)}/>
<rect x="58" y="48" width="12" height="10" rx="5" fill="#6A3A6E" {W(2)}/>
{eye(55, 54, 0.75)}{eye(73, 54, 0.75)}
<path d="M60 61 Q64 64 68 61" fill="none" {W(1.8)}/>
{BL(50, 60)}{BL(78, 60)}
{sparkle(20, 30, 5)}{sparkle(28, 66, 3.5)}{sparkle(104, 74, 4)}
''')

# 3. Батоно Джонни (Люберцы): ослик-качалка катает хинкали
add("cafe-batono-jonny-lyubertsy-8marta",
    "мохнатый серо-голубой плюшевый ослик-качалка на деревянных полозьях",
    "раскачивается в детской комнате и катает на спине маленького хинкали-седока, который машет хвостиком-ручкой",
    "zc_apricot", f'''
<path d="M-4 112 L132 112 L132 132 L-4 132Z" fill="#F7D9A8" {W(3)}/>
<path d="M14 104 Q64 126 114 104" fill="none" stroke="#B9702A" stroke-width="6" stroke-linecap="round"/>
<path d="M14 104 Q64 126 114 104" fill="none" {W(2)}/>
<path d="M38 84 L34 110 M54 88 L52 114 M80 88 L82 114 M94 82 L98 108" {W(5)}/>
<path d="M38 84 L34 110 M54 88 L52 114 M80 88 L82 114 M94 82 L98 108" stroke="#9EB4CC" stroke-width="3"/>
<path d="M30 70 Q30 92 60 92 Q92 92 98 72 Q96 60 64 60 Q34 60 30 70Z" fill="#9EB4CC" {W(3.2)}/>
<path d="M22 66 Q16 70 20 76" fill="none" {W(3)}/>
<path d="M92 66 Q98 40 108 36 Q122 34 122 50 Q122 62 108 64 Q100 66 96 74Z" fill="#9EB4CC" {W(3.2)}/>
<path d="M104 36 L98 18 L108 30 M112 34 L116 16 L118 34" fill="#9EB4CC" {W(2.6)}/>
<ellipse cx="117" cy="56" rx="6" ry="5" fill="#D8E3EE" {W(2.2)}/>
{eye(108, 46, 0.8)}
<path d="M114 59 Q117 61 120 58" fill="none" {W(1.6)}/>
{BL(104, 54)}
<path d="M94 46 Q90 54 92 62" fill="none" stroke="#5B6E86" stroke-width="4" stroke-linecap="round"/>
<path d="M56 62 Q50 48 54 40 Q64 32 74 40 Q78 48 72 62Z" fill="#FFF3DC" {W(3)}/>
<path d="M58 44 L60 56 M64 40 L64 58 M70 44 L68 56" stroke="#E0C49A" stroke-width="2"/>
<path d="M64 36 L64 28" stroke="{O}" stroke-width="3.4" stroke-linecap="round"/>
<path d="M64 30 L70 24" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>
{eye(60, 50, 0.65)}{eye(68, 50, 0.65)}
<path d="M61 55 Q64 58 67 55" fill="none" {W(1.6)}/>
{sparkle(18, 30, 5)}{sparkle(40, 22, 3.5)}
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
