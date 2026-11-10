"""Иконки робота cafes, 2026-11-10 (05:30 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая придумана и нарисована
отдельно. Сверено с icons-src/subjects.txt и листами icons-catalog: копчёный брискет (коптил* — 0 в реестре) и шар
дрожжевого теста в квашне — свободны.
Запуск: python3 tools/icons_cafes_1110c.py [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "k15_smoke": ("#FFF1E6", "#B5654A"),
    "k15_lavender": ("#F6F0FF", "#9C86D6"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. ГОВЯDИНА (Columbus) — у ресторана своя коптильня: брискет на доске, над ним дымок
add("cafe-govyadina-columbus",
    "толстый кусок копчёной говяжьей грудинки-брискета с тёмной перечной корочкой и розовым срезом",
    "довольно лежит на деревянной разделочной доске, а над ним поднимаются три завитка ароматного дымка", "k15_smoke", f'''
<rect x="16" y="88" width="96" height="20" rx="8" fill="#C98B52" {s()}/>
<circle cx="104" cy="98" r="3.2" fill="#8A5A30"/>
<path d="M24 88 Q22 58 44 52 L92 50 Q108 54 106 88Z" fill="#5A2E1E" {s()}/>
<path d="M92 50 Q108 54 106 88 L92 88 Q90 66 92 50Z" fill="#F08A86" {W(2.4)}/>
<path d="M95 60 Q100 64 98 72 M96 76 Q101 80 99 86" fill="none" stroke="#C2565A" stroke-width="2"/>
<circle cx="36" cy="64" r="1.6" fill="#2A140C"/><circle cx="50" cy="58" r="1.5" fill="#2A140C"/><circle cx="66" cy="60" r="1.6" fill="#2A140C"/>
<circle cx="80" cy="56" r="1.4" fill="#2A140C"/><circle cx="44" cy="80" r="1.4" fill="#2A140C"/><circle cx="76" cy="82" r="1.5" fill="#2A140C"/>
<g fill="#FFFFFF">{face(60, 72, d=12, k=1.0)}</g>
<path d="M40 44 Q32 36 40 28 Q48 20 40 12" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" opacity="0.9"/>
<path d="M62 42 Q54 34 62 26 Q70 18 62 10" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" opacity="0.9"/>
<path d="M84 42 Q76 34 84 26 Q92 18 84 10" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" opacity="0.9"/>
''')

# 2. Тесто (Вешки) — ресторан назван «Тесто», интерьер в стиле прованс: шар теста поднимается в квашне
add("cafe-testo-veshki",
    "пухлый шар дрожжевого теста с ямочками от пальцев, присыпанный мукой",
    "поднимается из деревянной квашни, сладко потягиваясь, а вокруг кружатся облачка муки на фоне лавандового неба", "k15_lavender", f'''
<path d="M20 78 L28 112 Q64 122 100 112 L108 78Z" fill="#B07A45" {s()}/>
<path d="M26 90 Q64 98 102 90 M30 104 Q64 112 98 104" fill="none" stroke="#7E5128" stroke-width="2.4"/>
<path d="M28 80 Q20 34 64 26 Q108 34 100 80 Q64 90 28 80Z" fill="#FFF3DC" {s()}/>
<circle cx="46" cy="50" r="2.4" fill="#EAD3A8"/><circle cx="84" cy="48" r="2.4" fill="#EAD3A8"/><circle cx="70" cy="38" r="2" fill="#EAD3A8"/>
{face(64, 62, d=12, k=1.0)}
<path d="M28 70 Q14 60 18 46" fill="none" stroke="#2B2B3A" stroke-width="4" stroke-linecap="round"/>
<path d="M100 70 Q114 60 110 46" fill="none" stroke="#2B2B3A" stroke-width="4" stroke-linecap="round"/>
<circle cx="18" cy="44" r="5" fill="#FFF3DC" {W(2.4)}/><circle cx="110" cy="44" r="5" fill="#FFF3DC" {W(2.4)}/>
<circle cx="30" cy="22" r="4" fill="#FFFFFF" opacity="0.9"/><circle cx="38" cy="16" r="2.6" fill="#FFFFFF" opacity="0.9"/>
<circle cx="98" cy="18" r="3.4" fill="#FFFFFF" opacity="0.9"/><circle cx="106" cy="26" r="2.4" fill="#FFFFFF" opacity="0.9"/>
''' + sparkle(64, 14, 3.5))


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
