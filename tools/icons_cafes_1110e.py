"""Иконки робота cafes, 2026-11-10 (16:50 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая придумана и нарисована
отдельно. Сверено с icons-src/subjects.txt: летающая тарелка (НЛО), бургер с черешней на плетне — в реестре нет.
Запуск: python3 tools/icons_cafes_1110e.py [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "k17_village": ("#FFF9DD", "#9FD36B"),
    "k17_cosmos": ("#5B3F9E", "#1C1846"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Village House (Ступино) — «деревенский дом», фирменный вишнёвый бургер: бургер с черешней сидит на плетне
add("cafe-village-house-stupino",
    "пышный бургер с черешенкой на хвостике, воткнутой в верхнюю булку",
    "сидит на деревенском плетне из прутьев и болтает ножками в красных башмачках", "k17_village", f'''
<path d="M0 98 L128 98 L128 128 L0 128Z" fill="#8CC85A"/>
<g stroke="#7A4E2A" stroke-width="5" stroke-linecap="round">
<path d="M14 112 L14 74"/><path d="M40 112 L40 72"/><path d="M88 112 L88 72"/><path d="M114 112 L114 74"/>
</g>
<path d="M4 86 Q34 80 64 86 T124 86" fill="none" stroke="#B07A45" stroke-width="5" stroke-linecap="round"/>
<path d="M4 96 Q34 102 64 96 T124 96" fill="none" stroke="#9A6535" stroke-width="5" stroke-linecap="round"/>
<path d="M52 84 L48 104" stroke="#3B3355" stroke-width="3.2" stroke-linecap="round"/>
<path d="M76 84 L82 102" stroke="#3B3355" stroke-width="3.2" stroke-linecap="round"/>
<ellipse cx="46" cy="107" rx="7" ry="4.5" fill="#E8453C" {W(2.4)}/>
<ellipse cx="85" cy="105" rx="7" ry="4.5" fill="#E8453C" {W(2.4)}/>
<path d="M30 82 Q30 76 36 76 L92 76 Q98 76 98 82 Q98 88 92 88 L36 88 Q30 88 30 82Z" fill="#F2B35C" {s()}/>
<path d="M30 72 L98 72 L98 78 L30 78Z" fill="#7A3E26" {W(2.6)}/>
<path d="M28 70 Q34 64 40 70 Q46 64 52 70 Q58 64 64 70 Q70 64 76 70 Q82 64 88 70 Q94 64 100 70" fill="#7CCB4E" {W(2.4)}/>
<path d="M30 66 Q30 34 64 32 Q98 34 98 66Z" fill="#F4A949" {s()}/>
<g fill="#FFF3D6"><ellipse cx="48" cy="44" rx="2.2" ry="1.3"/><ellipse cx="60" cy="40" rx="2.2" ry="1.3"/><ellipse cx="74" cy="42" rx="2.2" ry="1.3"/><ellipse cx="84" cy="50" rx="2.2" ry="1.3"/></g>
{face(64, 54, d=10, k=0.95)}
<path d="M64 33 Q66 22 74 14" fill="none" stroke="#4E7A2A" stroke-width="2.6" stroke-linecap="round"/>
<path d="M70 18 Q80 12 84 20 Q76 24 70 18Z" fill="#6DBE45" {W(2)}/>
<circle cx="62" cy="28" r="7" fill="#C8102E" {W(2.4)}/>
<circle cx="59.5" cy="25.5" r="2" fill="#fff" opacity=".8"/>
''' + sparkle(108, 30, 4) + sparkle(20, 40, 3))


# 2. Пипони (Святоозёрская) — пиццерия, работающая круглосуточно: пицца-НЛО ночью опускается на луче
add("cafe-piponi-svyatoozerskaya",
    "круглая пицца пепперони — летающая тарелка с прозрачным куполом-кабиной",
    "ночью парит над спящими домами и светит вниз жёлтым конусом луча", "k17_cosmos", f'''
<g fill="#FFFFFF"><circle cx="18" cy="24" r="1.6"/><circle cx="104" cy="18" r="1.8"/><circle cx="112" cy="46" r="1.3"/><circle cx="22" cy="58" r="1.2"/></g>
<path d="M44 66 L84 66 L106 118 L22 118Z" fill="#FFE37A" opacity=".45"/>
<path d="M0 104 L18 104 L18 92 L34 92 L34 108 L94 108 L94 90 L112 90 L112 100 L128 100 L128 128 L0 128Z" fill="#2A2560" {W(2.4)}/>
<g fill="#FFD45E"><rect x="22" y="97" width="4" height="5"/><rect x="99" y="95" width="4" height="5"/><rect x="104" y="95" width="4" height="5" opacity=".5"/></g>
<path d="M44 46 Q44 24 64 24 Q84 24 84 46Z" fill="#BFE8FF" opacity=".85" {s()}/>
<path d="M50 34 Q54 28 60 28" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<g fill="#3B3355">{face(64, 38, d=6.5, k=0.7)}</g>
<ellipse cx="64" cy="54" rx="48" ry="16" fill="#E8A13C" {s()}/>
<ellipse cx="64" cy="51" rx="40" ry="11" fill="#FFD25A" {W(2.4)}/>
<g fill="#D9473A" stroke="#3B3355" stroke-width="2">
<circle cx="38" cy="51" r="4.6"/><circle cx="54" cy="56" r="4.6"/><circle cx="74" cy="56" r="4.6"/><circle cx="90" cy="51" r="4.6"/><circle cx="64" cy="46" r="3.6"/>
</g>
<g fill="#FFF7B0" stroke="#3B3355" stroke-width="1.8"><circle cx="24" cy="60" r="2.6"/><circle cx="104" cy="60" r="2.6"/><circle cx="64" cy="70" r="2.6"/></g>
''' + sparkle(98, 30, 4, "#FFE37A") + sparkle(28, 36, 3, "#FFFFFF"))

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
