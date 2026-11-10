"""Иконки робота cafes, 2026-11-10 (20:40 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая придумана и нарисована
отдельно. Сверено с icons-src/subjects.txt: капкейк-тюльпан с Дюймовочкой, тарталетка-балерина у станка — в реестре нет
(«Наполеон», сырники, сухой бассейн, взлётная полоса, пение в микрофон — заняты, не берём).
Запуск: python3 tools/icons_cafes_1110f.py [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "k18_mint": ("#E9FFF4", "#7FD9B0"),
    "k18_lilac": ("#FBEFFF", "#C79BE8"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. АндерСон (Таганская) — «АндерСон» звучит как сказочник Андерсен: в кремовом тюльпане на капкейке сидит Дюймовочка
add("cafe-anderson-taganskaya",
    "капкейк в рифлёной голубой формочке с большим розовым тюльпаном из крема",
    "в раскрытых лепестках крем-тюльпана сидит крошечная Дюймовочка с золотыми косичками и машет ручкой", "k18_mint", f'''
<path d="M30 78 L98 78 L90 118 L38 118Z" fill="#6FB7E8" {s()}/>
<g stroke="#3B3355" stroke-width="2.2" stroke-linecap="round"><path d="M44 80 L48 116"/><path d="M58 80 L59 116"/><path d="M70 80 L69 116"/><path d="M84 80 L80 116"/></g>
<path d="M26 80 Q22 64 38 62 Q44 52 56 58 Q64 50 72 58 Q84 52 90 62 Q106 64 102 80Z" fill="#FFF3E2" {s()}/>
{face(64, 94, d=11, k=0.95)}
<path d="M64 60 L64 50" stroke="#4E9A3A" stroke-width="4" stroke-linecap="round"/>
<path d="M64 58 Q50 56 46 46 Q58 46 64 56Z" fill="#7CCB4E" {W(2.2)}/>
<path d="M40 30 Q42 50 64 52 Q86 50 88 30 Q80 36 76 26 Q70 34 64 20 Q58 34 52 26 Q48 36 40 30Z" fill="#FF8FB8" {s()}/>
<circle cx="64" cy="32" r="6.5" fill="#FFE0C8" {W(2.2)}/>
<path d="M57.5 30 Q58 24 64 24 Q70 24 70.5 30" fill="#F5C242" {W(2)}/>
<path d="M58 31 Q53 36 55 40" fill="none" stroke="#F5C242" stroke-width="2.6" stroke-linecap="round"/>
<path d="M70 31 Q75 36 73 40" fill="none" stroke="#F5C242" stroke-width="2.6" stroke-linecap="round"/>
<circle cx="62" cy="32" r="1.1" fill="#3B3355"/><circle cx="66" cy="32" r="1.1" fill="#3B3355"/>
<path d="M62 35 Q64 36.5 66 35" fill="none" stroke="#3B3355" stroke-width="1.2" stroke-linecap="round"/>
<path d="M70 38 Q76 34 78 28" fill="none" stroke="#FFE0C8" stroke-width="3" stroke-linecap="round"/>
<path d="M70 38 Q76 34 78 28" fill="none" stroke="#3B3355" stroke-width="0.9" stroke-linecap="round" opacity=".6"/>
''' + sparkle(100, 30, 4.5) + sparkle(26, 46, 3.2, "#FFF6C4"))


# 2. Синергия Кафе (Внуково) — в доме Академии хореографии «Синергия»: клубничная тарталетка-балерина у балетного станка
add("cafe-sinergiya-vnukovo",
    "песочная тарталетка с клубникой в пышной пачке из взбитых сливок",
    "держится за деревянный балетный станок перед высоким зеркалом и тянет тонкую ножку назад", "k18_lilac", f'''
<rect x="78" y="20" width="36" height="84" rx="4" fill="#DDF3FF" {s()}/>
<path d="M84 30 L96 24 M84 44 L108 30" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".9"/>
<path d="M0 104 L128 104 L128 128 L0 128Z" fill="#E2B27A" {W(2.4)}/>
<path d="M8 66 L120 66" stroke="#9A6535" stroke-width="5" stroke-linecap="round"/>
<path d="M16 66 L16 104 M112 66 L112 104" stroke="#9A6535" stroke-width="3.4" stroke-linecap="round"/>
<path d="M50 84 L46 102" stroke="#3B3355" stroke-width="3.2" stroke-linecap="round"/>
<ellipse cx="45" cy="103" rx="5.5" ry="3.2" fill="#FF8FB8" {W(2)}/>
<path d="M62 82 Q78 80 92 70" stroke="#3B3355" stroke-width="3.2" stroke-linecap="round" fill="none"/>
<ellipse cx="94" cy="69" rx="5" ry="3" fill="#FF8FB8" transform="rotate(-30 94 69)" {W(2)}/>
<path d="M22 74 Q30 64 40 72 Q50 64 60 72 Q70 64 80 74 Q70 86 52 86 Q32 86 22 74Z" fill="#FFFFFF" {s()}/>
<path d="M26 72 L32 46 L72 46 L78 72Z" fill="#E9B26A" {s()}/>
<g stroke="#B9813E" stroke-width="2" stroke-linecap="round"><path d="M38 50 L36 70"/><path d="M52 50 L52 70"/><path d="M66 50 L68 70"/></g>
{face(52, 58, d=8.5, k=0.82)}
<path d="M30 46 Q30 38 38 38 L66 38 Q74 38 74 46Z" fill="#FFF7F0" {W(2.4)}/>
<path d="M40 38 Q36 24 46 22 Q56 22 52 38Z" fill="#E8453C" {W(2.4)}/>
<path d="M54 38 Q56 26 66 28 Q72 32 64 40Z" fill="#E8453C" {W(2.4)}/>
<g fill="#FFE37A"><circle cx="45" cy="28" r="1"/><circle cx="48" cy="33" r="1"/><circle cx="62" cy="32" r="1"/></g>
<path d="M44 22 Q46 16 50 18 M64 28 Q68 22 70 26" stroke="#4E9A3A" stroke-width="2.4" fill="none" stroke-linecap="round"/>
<path d="M28 60 Q20 62 16 66" stroke="#3B3355" stroke-width="3" stroke-linecap="round" fill="none"/>
''' + sparkle(104, 14, 4) + sparkle(20, 30, 3.4))


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
