"""Иконка робота cafes, 2026-11-08 (13 UTC). Правило АБСОЛЮТНОЙ уникальности: придумана отдельно.
Таверна Робина — йоркширский пудинг в шапочке Робин Гуда приподнимает её, стоя на деревянной вывеске таверны на цепях.
Сверено с листами icons-catalog и subjects.txt (йоркширского пудинга и вывески таверны в реестре нет).
Запуск: python3 tools/icons_cafes_1108e.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({"d_sherwood": ("#F1FFE0", "#3F8F4A")})

ICONS["cafe-taverna-robina-kommunarka"] = svg("d_sherwood", f'''
<path d="M4 16 Q40 10 80 14" stroke="#6B4126" stroke-width="6" stroke-linecap="round" fill="none"/>
<path d="M22 14 V24 M58 13 V24" stroke="#8A8F9C" stroke-width="2.4" stroke-dasharray="3 2"/>
<rect x="14" y="24" width="52" height="16" rx="4" fill="#B9773F" {s("stroke-width=\"2.6\"")}/>
<path d="M22 32 H58" stroke="#8C5428" stroke-width="2" opacity=".6"/>
<ellipse cx="62" cy="110" rx="50" ry="9" fill="#F4F1E8" {s()}/>
<path d="M22 66 Q16 100 40 108 H86 Q110 100 104 66 Q96 72 90 64 Q82 74 74 64 Q66 74 58 64 Q50 74 42 64 Q34 72 22 66Z" fill="#E7A646" {s()}/>
<path d="M32 74 Q62 84 94 74 Q92 90 62 92 Q34 90 32 74Z" fill="#8A4B22" {s("stroke-width=\"2.2\"")}/>
<ellipse cx="50" cy="79" rx="5" ry="1.8" fill="#fff" opacity=".5"/>
{face(62, 96, d=12, k=0.8)}
<path d="M102 74 Q114 66 108 54" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M102 74 Q114 66 108 54" fill="none" stroke="#E7A646" stroke-width="4.6" stroke-linecap="round"/>
<g transform="rotate(-20 92 52)">
<path d="M66 64 Q80 34 116 46 Q102 52 100 64Z" fill="#2F7D3B" {s()}/>
<path d="M94 46 Q106 26 120 22 Q112 36 102 48Z" fill="#E2483A" {s("stroke-width=\"2.2\"")}/>
</g>
{sparkle(108, 22, 6)}{sparkle(14, 58, 4)}
''')
SUBJ["cafe-taverna-robina-kommunarka"] = ("йоркширский пудинг — румяная корзиночка из теста с подливкой, в зелёной шапочке Робин Гуда с красным пером",
                                          "стоит на тарелке под деревянной вывеской таверны на цепях и приветственно приподнимает шапочку")

if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for pid in ids:
        open(os.path.join(OUT, f"{pid}.svg"), "w").write(ICONS[pid])
    path = os.path.join(OUT, "subjects.txt")
    lines = [l for l in open(path, encoding="utf-8").read().splitlines() if l.split(" — ")[0] not in ICONS]
    lines += [f"{pid} — герой: {h} | сцена: {sc}" for pid, (h, sc) in SUBJ.items()]
    open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("svg:", len(ids))
