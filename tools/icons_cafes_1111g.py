"""Иконки робота cafes, 2026-11-11 (07 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая придумана и нарисована отдельно.
Сверено с subjects.txt: у «Тануки» заняты тануки-официант, дораяки, гёдза, удон, футомаки, омурайсу, бенто-автобус,
калифорния, тофу, наруто, гункан, маття; данго, тайяки, чизкейк, том ям — у других. Новые: фруто-сандо играют в ладушки;
пицца-барабан, по которой стучат гриссини.
Запуск: python3 tools/icons_cafes_1111g.py [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "k22_sando": ("#F3F0FF", "#9C8FD9"),
    "k22_drum": ("#E8FFF4", "#2FA36B"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


def sando(cx, flip):
    sx = -1 if flip else 1
    return f'''<g transform="translate({cx} 0) scale({sx} 1)">
<path d="M-26 96 L26 96 L0 34Z" fill="#FFF9EC" {W(2.8)}/>
<path d="M-20 86 L20 86 L0 46Z" fill="#FFFFFF"/>
<path d="M-12 78 Q-12 66 0 66 Q12 66 12 78 Q0 88 -12 78Z" fill="#F0384F" {W(2)}/>
<path d="M-5 66 l5 -6 l5 6" fill="#5DBB46" {W(1.6)}/>
<g fill="#FFE27A"><circle cx="-6" cy="74" r="1.1"/><circle cx="4" cy="72" r="1.1"/><circle cx="0" cy="79" r="1.1"/></g>
<path d="M-26 96 L26 96 L0 34Z" fill="none" stroke="#E9C88E" stroke-width="5" opacity=".9"/>
<path d="M-26 96 L26 96 L0 34Z" fill="none" {W(2.6)}/>
</g>'''


# 1. Тануки (Профсоюзная, 126, Коньково): две половинки японского фруто-сандо с клубникой играют в ладушки
add("cafe-tanuki-profsoyuznaya-126",
    "японский фруто-сандо — треугольный сэндвич из белого хлеба со сливками и клубникой в разрезе",
    "две половинки стоят друг напротив друга и играют в ладушки, хлопая ладошками, а между ними разлетаются сердечки",
    "k22_sando", f'''
<ellipse cx="64" cy="104" rx="50" ry="8" fill="#6E60B8" opacity=".3"/>
{sando(36, False)}
{sando(92, True)}
{face(30, 56, d=4.2, k=0.5)}{face(98, 56, d=4.2, k=0.5)}
<path d="M48 70 Q56 62 60 56" fill="none" {W(3)}/><path d="M80 70 Q72 62 68 56" fill="none" {W(3)}/>
<circle cx="60" cy="54" r="4.2" fill="#FFF9EC" {W(2)}/><circle cx="68" cy="54" r="4.2" fill="#FFF9EC" {W(2)}/>
<path d="M58 44 l-3 -5 M64 42 v-6 M70 44 l3 -5" stroke="{O}" stroke-width="2.2" stroke-linecap="round"/>
<path d="M64 30 c-3 -4 -8 0 -4 4 l4 4 l4 -4 c4 -4 -1 -8 -4 -4Z" fill="#FF5C7A" {W(1.6)}/>
<path d="M44 22 c-2 -3 -6 0 -3 3 l3 3 l3 -3 c3 -3 -1 -6 -3 -3Z" fill="#FF8FA6" {W(1.4)}/>
<path d="M86 24 c-2 -3 -6 0 -3 3 l3 3 l3 -3 c3 -3 -1 -6 -3 -3Z" fill="#FF8FA6" {W(1.4)}/>
''')

# 2. Ла Пиола (Профсоюзная, 109): толстая пицца на бортике, как барабан; палочки гриссини отбивают ритм
add("cafe-la-piola-profsoyuznaya-109",
    "толстая круглая пицца на высоком золотистом бортике, похожая на барабан",
    "висит на ремешке, как пионерский барабан, две хрустящие палочки гриссини сами отбивают по ней ритм, а кружки салями подпрыгивают",
    "k22_drum", f'''
<path d="M30 30 Q64 52 98 30" fill="none" stroke="#C0392B" stroke-width="5" stroke-linecap="round"/>
<path d="M22 64 V92 Q64 110 106 92 V64Z" fill="#E7A84B" {W(2.8)}/>
<path d="M22 70 L36 98 M50 72 L42 104 M50 72 L64 106 M78 72 L64 106 M78 72 L86 104 M106 70 L92 98" fill="none" stroke="#C47F27" stroke-width="2.4"/>
<ellipse cx="64" cy="64" rx="42" ry="14" fill="#F2C063" {W(2.8)}/>
<ellipse cx="64" cy="63" rx="35" ry="10.5" fill="#E8432F" {W(2)}/>
<path d="M36 62 Q44 56 52 62 Q60 68 70 60 Q80 56 90 63" fill="none" stroke="#FFE9A8" stroke-width="5" stroke-linecap="round"/>
<ellipse cx="46" cy="66" rx="5" ry="2.4" fill="#A3192C" {W(1.6)}/>
<ellipse cx="80" cy="66" rx="5" ry="2.4" fill="#A3192C" {W(1.6)}/>
<g transform="translate(58 38)"><ellipse rx="6" ry="3" fill="#A3192C" {W(1.6)}/></g>
<g transform="translate(74 30)"><ellipse rx="5" ry="2.6" fill="#A3192C" {W(1.6)}/></g>
<path d="M56 46 v-3 M74 37 v-3" stroke="{O}" stroke-width="1.8" stroke-linecap="round"/>
{face(64, 84, d=8, k=0.85)}
<g transform="rotate(-38 30 40)"><rect x="26" y="8" width="8" height="46" rx="4" fill="#F5DDA0" {W(2.2)}/>
<path d="M28 16 l4 3 M28 26 l4 3 M28 36 l4 3" stroke="#D5B064" stroke-width="1.6"/></g>
<g transform="rotate(34 98 38)"><rect x="94" y="6" width="8" height="46" rx="4" fill="#F5DDA0" {W(2.2)}/>
<path d="M96 14 l4 3 M96 24 l4 3 M96 34 l4 3" stroke="#D5B064" stroke-width="1.6"/></g>
<path d="M16 52 l-6 -2 M14 60 l-7 1 M112 52 l6 -2 M114 60 l7 1" stroke="{O}" stroke-width="2.2" stroke-linecap="round"/>
{sparkle(64, 18, 4)}
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
