"""Иконки робота cafes, 2026-11-13 (20 UTC). Каждая придумана и нарисована отдельно (правило АБСОЛЮТНОЙ уникальности):
герои и сцены сверены поиском по icons-src/subjects.txt; палитры фона — свои.
Запуск: python3 tools/icons_cafes_1113x.py [id…]  (без аргументов — все + строки реестра в subjects.txt)"""
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
    "kx_mintdusk": ("#E2FAF2", "#2F9C8A"),
    "kx_coralnight": ("#FFE4DA", "#C2453B"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Тануки (Петрозаводская, 11А): японский хлопковый чизкейк пружинит от смеха и сыплет сахарную пудру, как конфетти
add("cafe-tanuki-petrozavodskaya-11a",
    "высокий пышный японский хлопковый чизкейк с золотистой корочкой и мордашкой",
    "весело трясётся-пружинит на синем блюдце, расставив волнистые бока, а вокруг облачком летят снежинки сахарной пудры",
    "kx_mintdusk", f'''
<ellipse cx="64" cy="104" rx="50" ry="12" fill="#3F6FD1" {W(3)}/>
<ellipse cx="64" cy="102" rx="38" ry="7" fill="#7FA6F0"/>
<path d="M24 96 Q20 74 26 52 Q30 40 64 38 Q98 40 102 52 Q108 74 104 96 Q64 108 24 96Z" fill="#FFF3C8" {W(3.4)}/>
<path d="M26 52 Q30 40 64 38 Q98 40 102 52 Q98 62 64 62 Q30 62 26 52Z" fill="#E8A13E" {W(3)}/>
<path d="M40 46 Q50 42 58 46" fill="none" stroke="#F7C979" stroke-width="2.4" stroke-linecap="round"/>
<path d="M14 64 Q10 72 14 80 M114 64 Q118 72 114 80 M8 58 Q2 72 8 86 M120 58 Q126 72 120 86" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>
{eye(50, 74, 1.0)}{eye(78, 74, 1.0)}
<path d="M54 84 Q64 94 74 84 Q64 88 54 84Z" fill="#E2566B" {W(2.4)}/>
{BL(42, 84)}{BL(86, 84)}
<g fill="#FFFFFF" stroke="#BFD9D2" stroke-width="1"><circle cx="36" cy="24" r="3"/><circle cx="52" cy="16" r="2.2"/><circle cx="74" cy="20" r="2.8"/><circle cx="92" cy="26" r="2.2"/><circle cx="104" cy="38" r="2.6"/><circle cx="22" cy="40" r="2.2"/></g>
{sparkle(64, 26, 4.5)}{sparkle(112, 98, 3.5)}{sparkle(16, 104, 3)}
''')

# 2. Тануки (Волгоградский, 17): кудрявая лапша якисоба в бумажной коробочке, палочки вытянули лапшинку-сердечко
add("cafe-tanuki-volgogradsky-17",
    "кудрявая жареная лапша якисоба с зелёным луком и морковкой в белой бумажной коробочке с мордашкой на боку",
    "пара красных палочек вытягивает из коробочки длинную лапшинку, и та завивается в воздухе сердечком",
    "kx_coralnight", f'''
<path d="M30 70 L98 70 L90 116 L38 116Z" fill="#FFFFFF" {W(3.4)}/>
<path d="M30 70 L22 56 L42 64Z M98 70 L106 56 L86 64Z" fill="#F2F2F2" {W(2.6)}/>
<g fill="none" stroke="#C9822E" stroke-width="5" stroke-linecap="round">
<path d="M34 70 Q38 58 46 66 Q52 54 58 66 Q64 54 70 66 Q76 54 82 66 Q90 56 94 70"/>
</g>
<g fill="none" stroke="#E9A94E" stroke-width="3.4" stroke-linecap="round">
<path d="M40 70 Q44 62 50 68 M60 68 Q66 60 72 68 M80 68 Q86 62 90 70"/>
</g>
<g stroke="#4FA34A" stroke-width="3" stroke-linecap="round"><path d="M48 60 L52 56 M76 58 L80 55"/></g>
<rect x="62" y="56" width="6" height="4" rx="1.5" fill="#FF8C2B" {W(1.4)}/>
<path d="M66 64 Q66 46 62 38 Q56 26 50 32 Q44 40 62 54 Q80 40 74 32 Q68 26 62 38" fill="none" stroke="#C9822E" stroke-width="4.4" stroke-linecap="round" stroke-linejoin="round"/>
<g stroke-linecap="round"><path d="M92 6 L64 34" stroke="{O}" stroke-width="6.4"/><path d="M92 6 L64 34" stroke="#D93A3A" stroke-width="4"/>
<path d="M104 12 L70 38" stroke="{O}" stroke-width="6.4"/><path d="M104 12 L70 38" stroke="#D93A3A" stroke-width="4"/></g>
{eye(54, 90, 0.9)}{eye(74, 90, 0.9)}
<path d="M58 100 Q64 106 70 100" fill="none" {W(2.4)}/>
{BL(48, 99)}{BL(80, 99)}
{sparkle(22, 32, 4.5)}{sparkle(110, 74, 4)}{sparkle(30, 100, 3)}
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
