"""Иконки робота cafes, 2026-11-10 (23 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая придумана и нарисована отдельно.
Сверено с icons-src/subjects.txt: заняты шезлонги, качели, детский стульчик, мыльные пузыри, пицца-подсолнух, троллейбус,
молочный коктейль, желе-пудинг, сырники — не берём. Новые: котлетка-гоночная машинка на трассе из пюре; трёхшариковое
мороженое с горкой-спиралью и вишенкой; кусок пиццы во главе птичьего клина, летящего на юг.
Запуск: python3 tools/icons_cafes_1110g.py [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "k19_peach": ("#FFF1E6", "#F6A97A"),
    "k19_aqua": ("#E8FBFF", "#63C6E0"),
    "k19_dusk": ("#FFE9C9", "#F08A6A"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Тролли Кидс — детский ресторан: классика детского меню — котлетка с пюре, только котлетка — гоночная машинка
add("cafe-trolli-kids-krasnobogatyrskaya",
    "румяная котлетка в форме гоночной машинки с колёсами-горошинами",
    "мчится по извилистой трассе из картофельного пюре на большой белой тарелке, за ней облачко пара", "k19_peach", f'''
<ellipse cx="64" cy="80" rx="56" ry="34" fill="#FFFFFF" {s()}/>
<ellipse cx="64" cy="80" rx="44" ry="25" fill="none" stroke="#D9D2E6" stroke-width="2.4"/>
<path d="M14 92 Q34 70 58 84 Q82 98 112 72" fill="none" stroke="#FFE6A0" stroke-width="15" stroke-linecap="round"/>
<path d="M14 92 Q34 70 58 84 Q82 98 112 72" fill="none" stroke="#3B3355" stroke-width="1.6" stroke-dasharray="4 5" opacity=".5"/>
<path d="M30 70 Q30 46 56 44 L80 44 Q100 46 104 62 L106 74 Q106 80 98 80 L34 80 Q28 80 30 70Z" fill="#B8622E" {s()}/>
<path d="M38 50 Q50 46 60 50" fill="none" stroke="#E39A5E" stroke-width="3" stroke-linecap="round"/>
<path d="M78 44 L82 34 L94 34" fill="none" {W(3)}/>
<circle cx="44" cy="82" r="9" fill="#7CCB4E" {s()}/><circle cx="92" cy="82" r="9" fill="#7CCB4E" {s()}/>
<circle cx="42" cy="79" r="2.5" fill="#fff" opacity=".8"/><circle cx="90" cy="79" r="2.5" fill="#fff" opacity=".8"/>
{face(70, 60, d=10, k=0.95)}
<path d="M20 58 Q12 56 14 50 Q10 44 18 42 Q22 36 28 42" fill="#fff" {W(2.2)} opacity=".95"/>
''')

# 2. МаксЛевел — ресторан с трёхэтажной детской с горками: мороженое из трёх «уровней» с горкой-спиралью
add("cafe-maxlevel-novodanilovskaya",
    "мороженое из трёх шариков — фисташкового, клубничного и шоколадного — в вафельном рожке",
    "вокруг шариков вьётся детская горка-спираль, и по ней с визгом съезжает вишенка с хвостиком", "k19_aqua", f'''
<path d="M44 70 L84 70 L64 120Z" fill="#E7B46A" {s()}/>
<g stroke="#B9813E" stroke-width="2" stroke-linecap="round"><path d="M50 76 L70 112"/><path d="M62 74 L76 100"/><path d="M78 76 L58 112"/><path d="M66 74 L52 98"/></g>
<circle cx="64" cy="62" r="20" fill="#C9A27A" {s()}/>
<circle cx="64" cy="62" r="20" fill="#7A4A2E" {s()}/>
<circle cx="64" cy="40" r="18" fill="#FF9EBE" {s()}/>
<circle cx="64" cy="21" r="14" fill="#B6E08A" {s()}/>
{face(64, 60, d=8, k=0.85)}
<path d="M86 30 Q100 38 84 46 L44 52 Q28 58 44 64 L84 70 Q100 76 86 86" fill="none" stroke="#FFD13B" stroke-width="7" stroke-linecap="round"/>
<path d="M86 30 Q100 38 84 46 L44 52 Q28 58 44 64 L84 70 Q100 76 86 86" fill="none" {W(2)} opacity=".6"/>
<circle cx="38" cy="58" r="7" fill="#E5304A" {W(2.4)}/>
<path d="M38 51 Q40 42 48 40" fill="none" stroke="#4E9A3A" stroke-width="2.6" stroke-linecap="round"/>
<circle cx="36" cy="57" r="1.2" fill="#3B3355"/><circle cx="40.5" cy="57" r="1.2" fill="#3B3355"/>
<ellipse cx="38.2" cy="61" rx="2" ry="1.6" fill="#3B3355"/>
{sparkle(104, 20, 6)}
''')

# 3. Yug — «Юг»: кусок пиццы летит на юг во главе клина перелётных птиц
add("cafe-yug-novodmitrovskaya",
    "треугольный кусок пиццы с кружками колбаски и тянущимся сыром",
    "летит впереди клина перелётных птиц к южному закатному солнцу над морем", "k19_dusk", f'''
<circle cx="30" cy="96" r="20" fill="#FFD25E" {W(2.4)}/>
<path d="M0 104 L128 104 L128 128 L0 128Z" fill="#4FA7D8" {W(2.4)}/>
<path d="M8 112 Q16 108 24 112 M40 116 Q48 112 56 116 M82 112 Q90 108 98 112" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M30 26 L100 30 L56 86Z" fill="#F7C64A" {s()}/>
<path d="M30 26 L100 30" stroke="#C9792E" stroke-width="7" stroke-linecap="round"/>
<path d="M30 26 L100 30" fill="none" {W(2)}/>
<circle cx="50" cy="40" r="5" fill="#D9452E" {W(2)}/><circle cx="80" cy="40" r="5" fill="#D9452E" {W(2)}/><circle cx="62" cy="62" r="4.5" fill="#D9452E" {W(2)}/>
<path d="M60 82 Q58 92 62 96" fill="none" stroke="#F7C64A" stroke-width="3" stroke-linecap="round"/>
{face(64, 48, d=8, k=0.85)}
<g fill="none" stroke="#3B3355" stroke-width="2.6" stroke-linecap="round">
<path d="M90 56 Q95 52 100 56 Q105 52 110 56"/><path d="M98 70 Q103 66 108 70 Q113 66 118 70"/>
<path d="M20 50 Q25 46 30 50 Q35 46 40 50"/><path d="M12 64 Q17 60 22 64 Q27 60 32 64"/></g>
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
