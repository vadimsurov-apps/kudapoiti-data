"""Иконки робота cafes, 2026-11-13 (18 UTC). Каждая придумана и нарисована отдельно (правило АБСОЛЮТНОЙ уникальности):
герои и сцены сверены поиском по icons-src/subjects.txt; палитры фона — свои.
Запуск: python3 tools/icons_cafes_1113q.py [id…]  (без аргументов — все + строки реестра в subjects.txt)"""
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
    "kq_lavendersky": ("#EEE6FF", "#7E6BC4"),
    "kq_sauceyellow": ("#FFF6CF", "#E0A21E"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Алло! Пицца (Боровское ш., 50): пицца «Четыре сезона» — в каждой четвертинке своё время года
add("cafe-allo-pizza-borovskoe-50",
    "круглая пицца «Четыре сезона» с мордашкой, где каждая четвертинка — своё время года: снежинка, тюльпан, солнышко и кленовый лист",
    "стоит на ребре, как большое колесо, и весело подмигивает, а вокруг неё по кругу летают снежок, лепесток, лучик и жёлтый листик",
    "kq_lavendersky", f'''
<circle cx="64" cy="66" r="44" fill="#E9A44A" {W(3.4)}/>
<path d="M64 66 L64 28 A38 38 0 0 1 102 66Z" fill="#DDEBFF"/>
<path d="M64 66 L102 66 A38 38 0 0 1 64 104Z" fill="#FFE27A"/>
<path d="M64 66 L64 104 A38 38 0 0 1 26 66Z" fill="#FFB36B"/>
<path d="M64 66 L26 66 A38 38 0 0 1 64 28Z" fill="#B8EC8E"/>
<circle cx="64" cy="66" r="38" fill="none" stroke="#C9772C" stroke-width="2.4"/>
<path d="M64 28 L64 104 M26 66 L102 66" stroke="#C9772C" stroke-width="2.4"/>
<g stroke="#5B8FD6" stroke-width="2.6" stroke-linecap="round"><path d="M84 36 L84 52 M77 40 L91 48 M77 48 L91 40"/></g>
<g><circle cx="87" cy="82" r="6" fill="#FF9F1C" {W(2)}/><g stroke="#FF9F1C" stroke-width="2.4" stroke-linecap="round"><path d="M87 70 L87 73 M99 82 L96 82 M87 94 L87 91 M78 82 L75 82"/></g></g>
<path d="M40 76 L44 86 L48 78 L46 92 L42 92Z" fill="#D9541F" {W(1.8)}/>
<path d="M44 92 L44 98" stroke="{O}" stroke-width="1.8"/>
<path d="M38 52 Q38 40 44 46 Q46 38 50 46 Q54 40 52 52 Q46 58 38 52Z" fill="#FF6F9A" {W(1.8)}/>
<path d="M45 54 L45 60" stroke="#3E8E3A" stroke-width="2.2" stroke-linecap="round"/>
<circle cx="64" cy="66" r="13" fill="#FFF4D6" {W(2.4)}/>
{eye(59, 64, 0.7)}
<path d="M66 63 Q69 61 72 63" fill="none" {W(2.2)}/>
<path d="M58 70 Q64 75 70 70" fill="none" {W(2.2)}/>
{BL(56, 70)}{BL(72, 70)}
<circle cx="18" cy="30" r="5" fill="#FFFFFF" {W(1.8)}/>
<path d="M110 24 Q116 28 112 34 Q106 30 110 24Z" fill="#FF8FB1" {W(1.6)}/>
<path d="M114 104 L120 98 M116 110 L124 110 M110 114 L114 122" stroke="#FFD23F" stroke-width="3" stroke-linecap="round"/>
<path d="M12 98 Q18 92 22 98 Q18 104 12 98Z" fill="#FFC23A" {W(1.6)}/>
{sparkle(30, 16, 4)}{sparkle(100, 116, 3.5)}
''')

# 2. Ёрш (ул. Перерва, 58): рыбная палочка зажала нос и ныряет с бортика тарелки в соус тартар
add("cafe-ersh-pererva-58",
    "золотистая рыбная палочка в хрустящей панировке с маленьким рыбьим хвостиком и мордашкой",
    "зажав нос плавником, ныряет солдатиком с бортика белой тарелки в лужицу соуса тартар, разбрызгивая капли",
    "kq_sauceyellow", f'''
<ellipse cx="64" cy="104" rx="60" ry="18" fill="#FFFFFF" {W(3.2)}/>
<ellipse cx="64" cy="104" rx="46" ry="11" fill="#F1F4F7"/>
<ellipse cx="74" cy="106" rx="24" ry="7" fill="#F7F3DA" {W(2.6)}/>
<g fill="#7FB547"><circle cx="66" cy="105" r="1.6"/><circle cx="78" cy="107" r="1.4"/><circle cx="84" cy="104" r="1.3"/><circle cx="71" cy="108" r="1.2"/></g>
<g fill="#F7F3DA" stroke="{O}" stroke-width="1.8"><circle cx="54" cy="92" r="3.4"/><circle cx="92" cy="94" r="2.8"/><circle cx="60" cy="84" r="2.2"/><circle cx="88" cy="84" r="2.4"/></g>
<g transform="rotate(8 72 56)">
<rect x="58" y="22" width="28" height="68" rx="9" fill="#F0A93A" {W(3.4)}/>
<g fill="#C9771E"><circle cx="65" cy="32" r="1.6"/><circle cx="78" cy="38" r="1.4"/><circle cx="70" cy="60" r="1.5"/><circle cx="80" cy="74" r="1.6"/><circle cx="64" cy="80" r="1.3"/><circle cx="76" cy="52" r="1.2"/></g>
<path d="M64 22 L58 8 L72 16 L86 8 L80 22" fill="#F0A93A" {W(3)}/>
{eye(66, 44, 0.85)}{eye(79, 44, 0.85)}
<path d="M68 56 Q72 59 76 56" fill="none" {W(2.4)}/>
{BL(63, 52)}{BL(82, 52)}
<path d="M58 54 Q48 52 50 44 Q56 42 64 48" fill="#E8902A" {W(2.6)}/>
<circle cx="72" cy="50" r="3" fill="#E8902A" {W(2)}/>
</g>
<path d="M30 20 Q34 26 30 30 M100 30 Q96 36 102 40" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>
{sparkle(24, 52, 5)}{sparkle(108, 60, 4)}{sparkle(98, 14, 3)}
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
