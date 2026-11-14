"""Иконки робота cafes, 2026-11-14 (10–12 UTC). Каждая придумана и нарисована отдельно (правило АБСОЛЮТНОЙ уникальности).
Запуск: python3 tools/icons_cafes_1114g.py [id…]  (без аргументов — все + строки реестра в subjects.txt)"""
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
    "kg_mint": ("#F2FFF0", "#57B86A"),
    "kg_plum": ("#FBEFFF", "#8E5BC8"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Qalaquri Family в Филях (грузинская кухня + детский уголок): квадратик сладкой гаты прыгает через резиночку
add("cafe-qalaquri-family-beregovoy-5",
    "квадратик грузинской гаты — слоёного сладкого пирога с ромбиками-сеточкой на золотой корочке",
    "прыгает через розовую резиночку, натянутую между ножками двух маленьких детских стульчиков — синего и жёлтого",
    "kg_mint", f"""
<path d="M0 104 L128 104 L128 128 L0 128Z" fill="#E9C58E"/>
<path d="M0 104 L128 104" stroke="#B9884F" stroke-width="2.4"/>
<g {W(2.8)}>
<rect x="6" y="70" width="22" height="6" rx="2" fill="#4F86E0"/>
<path d="M8 76 L8 104 M26 76 L26 104" stroke="{O}" stroke-width="3"/>
<path d="M8 70 L8 52 Q8 48 12 48 L22 48 Q26 48 26 52 L26 70" fill="#4F86E0"/>
<rect x="100" y="70" width="22" height="6" rx="2" fill="#FFC531"/>
<path d="M102 76 L102 104 M120 76 L120 104" stroke="{O}" stroke-width="3"/>
<path d="M102 70 L102 52 Q102 48 106 48 L116 48 Q120 48 120 52 L120 70" fill="#FFC531"/>
</g>
<path d="M26 94 Q64 100 102 94" fill="none" stroke="#FF5C9A" stroke-width="3.6" stroke-linecap="round"/>
<g transform="rotate(-8 64 54)">
<rect x="38" y="30" width="52" height="42" rx="6" fill="#F3B451" {W(3.2)}/>
<rect x="38" y="58" width="52" height="14" rx="4" fill="#FFF0C9" {W(2.6)}/>
<path d="M38 64 Q64 68 90 64" fill="none" stroke="#E2B060" stroke-width="2"/>
<g stroke="#B9752A" stroke-width="2" opacity=".8">
<path d="M44 34 L60 50 M56 32 L74 50 M70 32 L86 48 M44 46 L50 52"/>
<path d="M84 34 L68 50 M72 32 L54 50 M58 32 L44 46 M86 46 L80 52"/>
</g>
<circle cx="52" cy="46" r="7.2" fill="#F3B451"/><circle cx="76" cy="46" r="7.2" fill="#F3B451"/>
{eye(52, 46, .8)}{eye(76, 46, .8)}
<path d="M59 52 Q64 57 69 52" fill="none" {W(2.4)}/>
{BL(46, 53)}{BL(82, 53)}
<path d="M48 72 L42 84 M80 72 L88 80" fill="none" {W(3)}/>
<g fill="#7A4FB8" {W(2)}><ellipse cx="41" cy="86" rx="4.6" ry="2.8"/><ellipse cx="90" cy="81" rx="4.6" ry="2.8"/></g>
<path d="M38 40 L28 30 M90 40 L100 28" fill="none" {W(3)}/>
</g>
<path d="M60 90 Q64 86 68 90" fill="none" stroke="#FFFFFF" stroke-width="2" opacity=".8"/>
{sparkle(24, 26, 5)}{sparkle(108, 22, 4)}
""")

# 2. Up Sushi в Коммунарке («Up», «Хорошее место 2026», детская игровая): «Калифорния» на пирамиде мягких модулей с золотой звездой
add("cafe-up-sushi-maloe-ponizovye-4",
    "кружок ролла «Калифорния» рисом наружу в оранжевой икре тобико, на срезе краб, авокадо и огурец",
    "стоит на верхушке пирамиды из трёх мягких игровых модулей-цилиндров и поднимает над головой золотую звезду-награду",
    "kg_plum", f"""
<g {W(2.8)}>
<rect x="14" y="98" width="44" height="22" rx="8" fill="#FF6B6B"/>
<rect x="70" y="98" width="44" height="22" rx="8" fill="#4FC3F7"/>
<rect x="38" y="76" width="52" height="22" rx="8" fill="#8BD46A"/>
</g>
<path d="M20 104 L52 104 M76 104 L108 104 M44 82 L84 82" stroke="#FFFFFF" stroke-width="2.4" opacity=".55" stroke-linecap="round"/>
<circle cx="64" cy="56" r="21" fill="#FF8A2B" {W(3.2)}/>
<g fill="#FFB36B"><circle cx="50" cy="46" r="1.8"/><circle cx="56" cy="40" r="1.8"/><circle cx="72" cy="38" r="1.8"/><circle cx="80" cy="48" r="1.8"/><circle cx="78" cy="66" r="1.8"/><circle cx="48" cy="66" r="1.8"/><circle cx="64" cy="74" r="1.8"/><circle cx="46" cy="56" r="1.8"/><circle cx="82" cy="58" r="1.8"/></g>
<circle cx="64" cy="56" r="14.5" fill="#FFFFFF" {W(2.2)}/>
<rect x="58" y="47" width="12" height="7" rx="2" fill="#F26D6D" stroke="#C94C4C" stroke-width="1.2"/>
<path d="M56 56 Q60 52 64 56 L60 60Z" fill="#9BCB4A" stroke="#5E8F2A" stroke-width="1.2"/>
<rect x="66" y="56" width="6" height="6" rx="1.5" fill="#4FAE5B" stroke="#2E7D3A" stroke-width="1.2"/>
{eye(58, 64, .62)}{eye(70, 64, .62)}
<path d="M61 68.5 Q64 71 67 68.5" fill="none" {W(1.8)}/>
<path d="M50 70 L46 76 M78 70 L82 76" fill="none" {W(3)}/>
<path d="M46 44 L40 22 M82 44 L88 22" fill="none" {W(3)}/>
<path d="M64 4 L69 15 L81 15 L71.5 22 L75 34 L64 27 L53 34 L56.5 22 L47 15 L59 15Z" fill="#FFD23F" {W(2.8)} transform="translate(0 2)"/>
<path d="M40 22 Q46 22 52 26 M88 22 Q82 22 76 26" fill="none" {W(2.6)}/>
{sparkle(30, 14, 5)}{sparkle(100, 14, 5)}{sparkle(108, 44, 3.5)}
""")

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
