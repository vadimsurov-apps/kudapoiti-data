"""Иконки робота cafes, 2026-11-13 (08 UTC). Каждая придумана и нарисована отдельно (правило АБСОЛЮТНОЙ уникальности):
герои и сцены сверены поиском по icons-src/subjects.txt; палитры фона — свои.
Запуск: python3 tools/icons_cafes_1113e.py [id…]  (без аргументов — все + строки реестра в subjects.txt)"""
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
    "ze_pubgreen": ("#CFE8C4", "#3F6B47"),
    "ze_seashore": ("#DDF3FF", "#6FB3E0"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Гуд Стори (Люблино, ресторан-паб): английский мясной пирог пускает пар колечками
add("cafe-gud-stori-lyublinskaya",
    "английский мясной стейк-пай в овальной голубой эмалированной форме с пухлым куполом слоёного теста и косичкой по краю",
    "стоит на деревянной разделочной доске и, довольно зажмурившись, пускает из дырочки в макушке пар колечками",
    "ze_pubgreen", f'''
<path d="M10 100 L118 100 L114 118 L14 118Z" fill="#C98B4E" {W(3)}/>
<path d="M24 106 L58 106 M70 111 L104 111" stroke="#9C6331" stroke-width="2" stroke-linecap="round"/>
<circle cx="112" cy="96" r="4" fill="#C98B4E" {W(2.4)}/>
<path d="M22 72 Q22 100 64 100 Q106 100 106 72Z" fill="#5BA7D9" {W(3.2)}/>
<path d="M26 84 Q64 92 102 84" fill="none" stroke="#FFFFFF" stroke-width="2.4" opacity=".7"/>
<path d="M18 72 Q20 38 64 36 Q108 38 110 72 Q64 80 18 72Z" fill="#F2B45C" {W(3.2)}/>
<path d="M20 72 Q64 82 108 72" fill="none" stroke="#D98A2E" stroke-width="5" stroke-dasharray="6 4"/>
<path d="M36 52 Q44 46 52 50 M76 50 Q84 46 92 52" fill="none" stroke="#D98A2E" stroke-width="2.2" stroke-linecap="round"/>
<path d="M46 62 Q50 58 54 62 M74 62 Q78 58 82 62" fill="none" {W(2.4)}/>
<path d="M58 68 Q64 73 70 68" fill="none" {W(2.2)}/>
{BL(42, 67)}{BL(86, 67)}
<ellipse cx="64" cy="39" rx="4" ry="2.4" fill="#8A4E1E" {W(1.8)}/>
<circle cx="66" cy="26" r="5" fill="none" stroke="#FFFFFF" stroke-width="3" opacity=".9"/>
<circle cx="58" cy="14" r="6.5" fill="none" stroke="#FFFFFF" stroke-width="3" opacity=".75"/>
<circle cx="70" cy="2" r="8" fill="none" stroke="#FFFFFF" stroke-width="3" opacity=".55"/>
''')

# 2. Чайка (Люберцы): стаканчик чая навынос у моря, на крышке сидит чайка
add("cafe-chayka-lyubertsy-vesennyaya",
    "высокий бумажный стаканчик чая навынос в бело-оранжевую полоску с красной крышкой и ярлычком чайного пакетика",
    "стоит на жёлтом песке у моря и улыбается, а на его крышке, как на капитанском мостике, сидит белая чайка",
    "ze_seashore", f'''
<path d="M-4 86 Q30 80 64 86 Q98 92 132 84 L132 100 L-4 100Z" fill="#3E8FCB" {W(3)}/>
<path d="M12 90 Q20 86 28 90 M96 92 Q104 88 112 92" fill="none" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round"/>
<path d="M-4 98 Q64 92 132 98 L132 132 L-4 132Z" fill="#F6D27A" {W(3)}/>
<g fill="#D9A84A"><circle cx="20" cy="112" r="1.6"/><circle cx="104" cy="116" r="1.6"/><circle cx="96" cy="108" r="1.4"/></g>
<path d="M42 50 L86 50 L80 112 L48 112Z" fill="#FFFFFF" {W(3.2)}/>
<path d="M43.5 62 L84.5 62 L83.7 70 L44.3 70Z M45 82 L83 82 L82.2 90 L45.8 90Z" fill="#FF9A4A"/>
<path d="M42 50 L86 50 L80 112 L48 112Z" fill="none" {W(3.2)}/>
<rect x="38" y="42" width="52" height="10" rx="4" fill="#E8474C" {W(3)}/>
<path d="M86 52 Q96 60 94 74" fill="none" stroke="#FFFFFF" stroke-width="1.8"/>
<rect x="88" y="72" width="11" height="12" rx="2" fill="#FFE37A" {W(2.2)}/>
{eye(56, 76, 0.85)}{eye(72, 76, 0.85)}
<path d="M58 86 Q64 91 70 86" fill="none" {W(2)}/>
{BL(51, 84)}{BL(77, 84)}
<path d="M54 42 Q52 32 60 28 Q68 26 74 32 L74 42Z" fill="#FFFFFF" {W(2.6)}/>
<path d="M60 30 Q70 18 84 22 Q74 26 70 34Z" fill="#E6EEF5" {W(2.4)}/>
<circle cx="57" cy="31" r="1.8" fill="{O}"/>
<path d="M52 33 L44 34 L52 36Z" fill="#FFB52E" {W(1.6)}/>
<path d="M60 42 L60 46 M68 42 L68 46" stroke="#FFB52E" stroke-width="2.4"/>
{sparkle(108, 30, 5)}{sparkle(22, 44, 3.5)}
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
