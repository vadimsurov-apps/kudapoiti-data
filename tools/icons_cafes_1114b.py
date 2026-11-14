"""Иконки робота cafes, 2026-11-14 (02 UTC). Каждая придумана и нарисована отдельно (правило АБСОЛЮТНОЙ уникальности):
герои и сцены сверены поиском по icons-src/subjects.txt; палитры фона — свои.
Запуск: python3 tools/icons_cafes_1114b.py [id…]  (без аргументов — все + строки реестра в subjects.txt)"""
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
    "kb_mintsun": ("#E8FFF4", "#3FB89A"),
    "kb_wineplum": ("#FFEFE6", "#B5475C"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Додо Пицца (пр-т Вернадского, 29, детская комната): малинка в шоколаде из меню съезжает с горки детской
add("cafe-dodo-vernadskogo-29",
    "ягодка малины в шоколадной глазури — наполовину белой, наполовину молочной — с зелёным хвостиком и мордашкой",
    "с поднятыми лапками съезжает с жёлтой изогнутой горки детской комнаты прямо в кучку разноцветных шариков",
    "kb_mintsun", f'''
<path d="M14 40 Q20 34 26 40 L26 112 L14 112Z" fill="#FFFFFF" {W(3)}/>
<path d="M20 44 L20 108" stroke="#D8E4EE" stroke-width="3"/>
<path d="M22 40 Q52 44 66 74 Q78 98 106 104 L106 116 Q72 114 58 88 Q46 60 22 54Z" fill="#FFD23F" {W(3.2)}/>
<path d="M28 47 Q54 52 64 80 Q76 104 104 110" fill="none" stroke="#FFF1A6" stroke-width="3" stroke-linecap="round"/>
<circle cx="86" cy="116" r="8" fill="#FF6B8A" {W(2.6)}/>
<circle cx="102" cy="118" r="8" fill="#4FA3FF" {W(2.6)}/>
<circle cx="70" cy="120" r="7" fill="#9BE15D" {W(2.6)}/>
<g transform="rotate(28 52 54)">
<path d="M52 30 Q72 30 72 54 Q72 76 52 78 Q32 76 32 54 Q32 30 52 30Z" fill="#8A4B2C" {W(3.2)}/>
<path d="M52 30 Q32 30 32 54 Q32 76 52 78Z" fill="#FFF4E2" {W(3.2)}/>
<g fill="#E23D63" opacity=".55"><circle cx="40" cy="44" r="2.4"/><circle cx="44" cy="66" r="2.4"/><circle cx="62" cy="42" r="2.4"/><circle cx="64" cy="64" r="2.4"/></g>
<path d="M46 30 Q52 20 58 30 M52 30 L52 22 M44 26 Q52 28 60 26" fill="#5CC14D" {W(2.6)}/>
{eye(45, 52, .9)}{eye(59, 52, .9)}
<path d="M46 62 Q52 70 58 62Z" fill="#E23D63" {W(2.4)}/>
{BL(39, 59)}{BL(65, 59)}
<path d="M32 50 Q22 40 24 30" fill="none" {W(3)}/><path d="M72 50 Q82 38 80 28" fill="none" {W(3)}/>
</g>
<path d="M88 30 L98 24 M92 40 L104 38 M84 20 L90 12" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>
{sparkle(108, 54, 5)}
''')

# 2. Ваш Гогис (Коммунарка, грузинская кухня, живая музыка, детский уголок): хинкали в папахе играет на барабане доли
add("cafe-vash-gogis-potapovskaya",
    "пухлый хинкали со складочками в маленькой чёрной кавказской папахе",
    "сидит, зажав коленками грузинский барабан доли, и отбивает ритм ладошками, а над ним прыгают две ноты",
    "kb_wineplum", f'''
<ellipse cx="64" cy="116" rx="42" ry="6" fill="#7A2236" opacity=".3"/>
<path d="M40 30 Q64 20 88 30 L86 44 Q64 38 42 44Z" fill="#2E2A33" {W(3)}/>
<path d="M44 32 L46 42 M52 28 L53 39 M60 26 L61 38 M68 26 L67 38 M76 28 L75 39 M84 32 L82 42" stroke="#57505F" stroke-width="2"/>
<path d="M64 40 Q50 44 36 62 Q26 80 40 88 Q64 96 88 88 Q102 80 92 62 Q78 44 64 40Z" fill="#FFF8EC" {W(3.2)}/>
<path d="M64 42 Q56 58 50 86 M64 42 Q64 60 64 90 M64 42 Q72 58 78 86 M64 42 Q46 54 40 74 M64 42 Q82 54 88 74" fill="none" stroke="#E9D9BE" stroke-width="2.4"/>
{eye(55, 64, 1.0)}{eye(73, 64, 1.0)}
<path d="M58 74 Q64 80 70 74" fill="none" {W(2.6)}/>
{BL(48, 72)}{BL(80, 72)}
<path d="M42 96 L44 116 Q64 122 84 116 L86 96Z" fill="#C2373F" {W(3)}/>
<path d="M44 102 L84 102 M45 110 L83 110" stroke="#F2C14E" stroke-width="2.4"/>
<path d="M50 99 L56 113 L62 99 L68 113 L74 99 L80 113" fill="none" stroke="#2E2A33" stroke-width="1.6"/>
<ellipse cx="64" cy="96" rx="22" ry="5" fill="#F7E7C6" {W(3)}/>
<path d="M40 82 Q34 90 46 94" fill="#FFF8EC" {W(3)}/>
<path d="M88 82 Q96 86 84 92" fill="#FFF8EC" {W(3)}/>
<path d="M96 70 L96 50 L106 46 L106 64" fill="none" stroke="#FFFFFF" stroke-width="3"/>
<ellipse cx="93" cy="71" rx="4" ry="3" fill="#FFFFFF"/><ellipse cx="103" cy="65" rx="4" ry="3" fill="#FFFFFF"/>
<path d="M22 44 L22 30 L28 28" fill="none" stroke="#FFFFFF" stroke-width="3"/>
<ellipse cx="19" cy="45" rx="4" ry="3" fill="#FFFFFF"/>
''')


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
