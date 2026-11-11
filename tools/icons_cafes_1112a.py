"""Иконки робота cafes, 2026-11-11 (23 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая придумана отдельно,
герои и сцены сверены с subjects.txt и листами каталога кафе (рыбка-русалка с вилкой-гребнем, лимонный тарт-гитарист,
кусок пиццы-клоун с моцареллой, сэндвич с пепперони-веснушками на подушках, чёрная равиоли с обручем — таких нет).
Запуск: python3 tools/icons_cafes_1112a.py [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "z_lagoon": ("#D9FBF4", "#2AA69A"),
    "z_stage": ("#FFE8F0", "#B0457A"),
    "z_circus": ("#E8F9D9", "#5FA83A"),
    "z_peach": ("#FFF0E2", "#E08A55"),
    "z_violet": ("#ECE6FF", "#5B4BB0"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Rusalka (Новинки): морепродукты и рыба + название — рыбка-русалка причёсывается вилкой
add("cafe-rusalka-novinki",
    "серебристо-бирюзовая рыбка-русалка с длинными волосами из зелёных водорослей",
    "сидит на камне посреди волн и расчёсывает водоросли вилкой, как гребнем",
    "z_lagoon", f'''
<path d="M0 98 Q16 90 32 98 Q48 106 64 98 Q80 90 96 98 Q112 106 128 98 L128 128 L0 128Z" fill="#5CC8E8" {W(3)}/>
<path d="M30 104 Q38 84 64 84 Q90 84 98 104Z" fill="#9AA5B4" {W(3)}/>
<path d="M40 92 l6 -3 M74 90 l7 2" stroke="#6E7887" stroke-width="2.4" stroke-linecap="round"/>
<path d="M44 86 Q30 70 44 52 Q56 38 74 44 Q92 52 88 72 Q84 84 70 88Z" fill="#BFE6EE" {W(3)}/>
<path d="M70 88 Q84 92 92 84 Q100 92 98 102 Q90 98 84 96 Q78 98 70 96Z" fill="#3FB6A8" {W(3)}/>
<path d="M52 60 q6 4 12 0 M50 70 q6 4 12 0 M60 80 q6 4 12 0" fill="none" stroke="#7FB9C6" stroke-width="2.2" stroke-linecap="round"/>
<path d="M50 46 Q40 30 30 44 Q26 58 32 70 Q36 56 42 52 Q38 66 44 74 Q46 60 52 52Z" fill="#4CB050" {W(2.8)}/>
<path d="M74 44 Q86 28 98 38 Q104 50 96 60 Q94 50 86 48Z" fill="#4CB050" {W(2.8)}/>
{eye(60, 58, 0.85)}{eye(76, 58, 0.85)}
<path d="M64 66 Q68 70 72 66" fill="none" {W(2.4)}/>
<ellipse cx="55" cy="65" rx="4" ry="2.2" fill="#FF7FA8" opacity=".6"/><ellipse cx="81" cy="65" rx="4" ry="2.2" fill="#FF7FA8" opacity=".6"/>
<g transform="rotate(-30 100 50)">
<rect x="97" y="46" width="6" height="34" rx="3" fill="#D9DEE6" {W(2.4)}/>
<path d="M94 46 L94 30 M98.5 46 L98.5 28 M103 46 L103 28 M107 46 L107 30" {W(2.6)}/>
<path d="M93 44 L108 44 L106 50 L95 50Z" fill="#D9DEE6" {W(2.4)}/>
</g>
<circle cx="22" cy="80" r="3" fill="#FFFFFF" {W(1.8)}/><circle cx="16" cy="68" r="2" fill="#FFFFFF" {W(1.6)}/>
{sparkle(108, 22, 5)}
''')

# 2. Солнечный (г. Московский): живая музыка и десерты — лимонный тарт-солнышко играет на гитаре
add("cafe-solnechny-moskovsky",
    "круглый лимонный тарт с золотой корочкой и лучами из завитков безе",
    "играет на маленькой гитаре на сцене под розовым софитом и подпевает",
    "z_stage", f'''
<path d="M40 8 L88 8 L104 120 L24 120Z" fill="#FFF3B8" opacity=".45"/>
<rect x="14" y="106" width="100" height="14" rx="4" fill="#8A4B2E" {W(3)}/>
<g fill="#FFFFFF" {W(2.4)}>
<path d="M64 18 q5 6 0 12 q-5 -6 0 -12Z"/><path d="M98 34 q2 8 -6 10 q0 -8 6 -10Z"/><path d="M30 34 q-2 8 6 10 q0 -8 -6 -10Z"/>
<path d="M108 62 q-6 4 -12 0 q6 -5 12 0Z"/><path d="M20 62 q6 4 12 0 q-6 -5 -12 0Z"/>
<path d="M84 22 q4 7 -3 11 q-2 -7 3 -11Z"/><path d="M44 22 q-4 7 3 11 q2 -7 -3 -11Z"/>
</g>
<circle cx="64" cy="64" r="32" fill="#E8B04E" {W(3)}/>
<circle cx="64" cy="64" r="25" fill="#FFE14D" {W(2.6)}/>
{eye(56, 58, 0.9)}{eye(72, 58, 0.9)}
<ellipse cx="64" cy="70" rx="4.5" ry="5" fill="#C2410C" {W(2.2)}/>
<ellipse cx="49" cy="66" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/><ellipse cx="79" cy="66" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/>
<g transform="rotate(-28 70 92)">
<rect x="78" y="86" width="34" height="6" rx="2" fill="#8A5A2B" {W(2.4)}/>
<path d="M54 80 Q46 80 46 89 Q46 98 54 98 Q60 98 62 94 Q66 100 74 99 Q82 97 82 89 Q82 81 74 79 Q66 78 62 84 Q60 80 54 80Z" fill="#F08A3C" {W(2.8)}/>
<circle cx="66" cy="89" r="4" fill="#6B3A1E" {W(2)}/>
<rect x="110" y="84" width="7" height="10" rx="2" fill="#6B3A1E" {W(2)}/>
</g>
<path d="M22 30 l0 -12 l8 -2 l0 10" fill="none" {W(2.4)}/><circle cx="19" cy="30" r="3" fill="{O}"/><circle cx="27" cy="27" r="3" fill="{O}"/>
{sparkle(108, 18, 5)}
''')

# 3. Полианто (Троицк): пиццерия с детской анимацией — кусок пиццы-клоун жонглирует моцареллой
add("cafe-polianto-troitsk",
    "треугольный кусок пиццы «Деревенская» с носом-помидоркой черри и рыжими кудрями из сыра",
    "жонглирует тремя белыми шариками моцареллы, как клоун-аниматор на детском празднике",
    "z_circus", f'''
<path d="M64 112 L30 46 Q64 30 98 46Z" fill="#FFD36B" {W(3)}/>
<path d="M30 46 Q64 30 98 46 L94 38 Q64 22 34 38Z" fill="#E09A3E" {W(3)}/>
<circle cx="48" cy="62" r="5" fill="#C8A26B" {W(2)}/><circle cx="82" cy="60" r="5" fill="#C8A26B" {W(2)}/>
<path d="M58 92 q4 -4 8 0 M70 80 q3 -3 6 0" fill="none" stroke="#B5742A" stroke-width="2.2" stroke-linecap="round"/>
<g fill="#FFB347" {W(2.2)}><circle cx="30" cy="40" r="6"/><circle cx="24" cy="48" r="5"/><circle cx="98" cy="40" r="6"/><circle cx="104" cy="48" r="5"/></g>
{eye(56, 56, 0.85)}{eye(72, 56, 0.85)}
<circle cx="64" cy="66" r="6" fill="#E8382F" {W(2.4)}/><circle cx="62" cy="64" r="1.6" fill="#fff"/>
<path d="M56 76 Q64 84 72 76" fill="#fff" {W(2.4)}/>
<path d="M40 70 Q30 64 26 54" fill="none" {W(3)}/><path d="M88 70 Q98 64 102 54" fill="none" {W(3)}/>
<g fill="#FFFFFF" {W(2.4)}><circle cx="28" cy="22" r="7"/><circle cx="64" cy="12" r="7"/><circle cx="100" cy="22" r="7"/></g>
<path d="M36 18 Q48 8 56 10 M72 10 Q82 8 92 18" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="3 4" stroke-linecap="round"/>
''')

# 4. Соул (Окская): кофейня с детским уголком и сэндвичами — сэндвич с пепперони-веснушками на подушках
add("cafe-soul-okskaya",
    "пышный ремесленный сэндвич с кружками пепперони, торчащими, как веснушки",
    "валяется на горке мягких разноцветных подушек в детском уголке и хохочет, болтая ножками",
    "z_peach", f'''
<ellipse cx="40" cy="102" rx="30" ry="14" fill="#7ED6C8" {W(3)}/>
<ellipse cx="88" cy="104" rx="30" ry="13" fill="#B79CF0" {W(3)}/>
<ellipse cx="64" cy="94" rx="30" ry="13" fill="#FFB0C8" {W(3)}/>
<path d="M30 74 Q30 50 64 48 Q98 50 98 74Z" fill="#D9984A" {W(3)}/>
<path d="M28 74 L100 74 L98 80 L30 80Z" fill="#6FC24A" {W(2.4)}/>
<g fill="#D9483B" {W(2.4)}><circle cx="38" cy="80" r="6"/><circle cx="56" cy="82" r="6"/><circle cx="74" cy="82" r="6"/><circle cx="92" cy="80" r="6"/></g>
<rect x="30" y="80" width="68" height="8" rx="3" fill="#FFE07A" {W(2.4)}/>
<path d="M30 88 Q64 96 98 88 L98 92 Q64 102 30 92Z" fill="#E3A957" {W(2.8)}/>
<path d="M42 58 l4 -2 M60 54 l4 0 M78 56 l4 2" stroke="#A86A26" stroke-width="2.2" stroke-linecap="round"/>
<path d="M50 66 q4 -4 8 0 M70 66 q4 -4 8 0" fill="none" {W(2.6)}/>
<path d="M56 70 Q64 78 72 70" fill="#fff" {W(2.4)}/>
<ellipse cx="45" cy="70" rx="4" ry="2.2" fill="#FF7FA8" opacity=".7"/><ellipse cx="83" cy="70" rx="4" ry="2.2" fill="#FF7FA8" opacity=".7"/>
<path d="M98 86 Q108 74 116 80" fill="none" {W(3)}/><path d="M30 86 Q20 74 12 80" fill="none" {W(3)}/>
<path d="M18 40 l4 -6 M24 44 l7 -3 M104 38 l-4 -6 M110 44 l-7 -3" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>
{sparkle(64, 26, 6)}
''')

# 5. La Provincia (Октябрьская): итальянский ресторан с детской анимацией — чёрная равиоли крутит обруч
add("cafe-la-provincia-oktyabrskaya",
    "чёрная равиоли с сибасом — квадратная подушечка с зубчатым краем цвета каракатицы",
    "крутит на талии ярко-оранжевый обруч, а вокруг сыплется праздничное конфетти",
    "z_violet", f'''
<rect x="38" y="36" width="52" height="52" rx="8" fill="#2E2E3A" {W(3)}/>
<path d="M38 44 l-4 4 l4 4 l-4 4 l4 4 l-4 4 l4 4 l-4 4 l4 4 M90 44 l4 4 l-4 4 l4 4 l-4 4 l4 4 l-4 4 l4 4 l-4 4" fill="none" {W(2.4)}/>
<path d="M42 36 l4 -4 l4 4 l4 -4 l4 4 l4 -4 l4 4 l4 -4 l4 4 l4 -4 l4 4 l4 -4 l4 4" fill="#2E2E3A" {W(2.4)}/>
<path d="M42 88 l4 4 l4 -4 l4 4 l4 -4 l4 4 l4 -4 l4 4 l4 -4 l4 4 l4 -4 l4 4 l4 -4" fill="#2E2E3A" {W(2.4)}/>
<circle cx="64" cy="62" r="20" fill="#454558" stroke="#6A6A80" stroke-width="2"/>
<path d="M52 50 Q58 44 66 45" fill="none" stroke="#8C8CA6" stroke-width="2.4" stroke-linecap="round"/>
<circle cx="56" cy="58" r="5.2" fill="#fff"/><circle cx="72" cy="58" r="5.2" fill="#fff"/>
{eye(56, 58, 0.8)}{eye(72, 58, 0.8)}
<path d="M58 68 Q64 74 70 68" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<ellipse cx="50" cy="67" rx="3.6" ry="2" fill="#FF7FA8" opacity=".8"/><ellipse cx="78" cy="67" rx="3.6" ry="2" fill="#FF7FA8" opacity=".8"/>
<path d="M28 30 L42 40 M100 30 L86 40" fill="none" {W(3)}/>
<path d="M50 88 L46 104 M78 88 L82 104" fill="none" {W(3)}/>
<path d="M40 104 L50 104 M76 104 L88 104" fill="none" {W(3.4)}/>
<ellipse cx="64" cy="80" rx="44" ry="9" fill="none" stroke="{O}" stroke-width="7"/>
<ellipse cx="64" cy="80" rx="44" ry="9" fill="none" stroke="#FF8A1F" stroke-width="4"/>
<rect x="38" y="70" width="52" height="8" fill="#2E2E3A"/>
<g {W(1.6)}>
<rect x="18" y="16" width="6" height="4" fill="#FFD23F" transform="rotate(20 21 18)"/><rect x="104" y="20" width="6" height="4" fill="#4CD6C0" transform="rotate(-25 107 22)"/>
<rect x="60" y="14" width="6" height="4" fill="#FF6FA8" transform="rotate(35 63 16)"/><rect x="16" y="64" width="6" height="4" fill="#4CD6C0"/>
<rect x="106" y="60" width="6" height="4" fill="#FFD23F" transform="rotate(-15 109 62)"/><rect x="84" y="12" width="6" height="4" fill="#FF6FA8" transform="rotate(-30 87 14)"/>
</g>
{sparkle(30, 112, 4)}{sparkle(100, 112, 4)}
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
