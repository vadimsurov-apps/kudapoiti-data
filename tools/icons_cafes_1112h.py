"""Иконки робота cafes, 2026-11-12 (08 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая придумана отдельно,
герои и сцены сверены с subjects.txt (поиск по ключевым словам) и листом каталога кафе.
Запуск: python3 tools/icons_cafes_1112h.py [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "zh_fern": ("#E9FBE3", "#5FB86A"),
    "zh_sugar": ("#FFF4FA", "#E79BC0"),
    "zh_book": ("#FFF8E8", "#E3A857"),
    "zh_window": ("#EAF3FF", "#7E9FD8"),
    "zh_dawn": ("#FFF3D6", "#F49A5A"),
    "zh_frost": ("#EEF4FF", "#8C9FE8"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Osteria Mario у Ботанического сада: пицца-садовник поливает клумбу ромашек из шланга
add("cafe-osteria-botanica-pika",
    "круглая пицца «Маргарита» в соломенной шляпе садовника",
    "поливает из зелёного садового шланга клумбу с ромашками в ботаническом саду",
    "zh_fern", f'''
<rect x="0" y="100" width="128" height="30" fill="#7CC36B"/>
<path d="M0 100 Q64 92 128 100" fill="none" {W(2.6)}/>
<circle cx="66" cy="70" r="32" fill="#F0B862" {W(3)}/>
<circle cx="66" cy="70" r="25" fill="#E2463A"/>
<circle cx="56" cy="80" r="6" fill="#FFF6DD" {W(2)}/><circle cx="78" cy="62" r="5.5" fill="#FFF6DD" {W(2)}/><circle cx="80" cy="82" r="4.5" fill="#FFF6DD" {W(2)}/>
<path d="M70 86 q4 -6 8 0 q-4 4 -8 0Z" fill="#3E9A4E" {W(1.6)}/>
{eye(58, 66, 0.9)}{eye(72, 66, 0.9)}
<path d="M60 74 Q65 79 70 74" fill="none" {W(2.4)}/>
<ellipse cx="66" cy="42" rx="34" ry="7" fill="#F4D77A" {W(2.8)}/>
<path d="M50 41 Q52 24 66 24 Q80 24 82 41Z" fill="#F4D77A" {W(2.8)}/>
<path d="M51 36 Q66 40 81 36" fill="none" stroke="#5FB86A" stroke-width="4"/>
<path d="M38 74 Q22 78 22 92 Q22 104 36 108" fill="none" stroke="#3E9A4E" stroke-width="5" stroke-linecap="round"/>
<path d="M38 74 Q22 78 22 92 Q22 104 36 108" fill="none" stroke="{O}" stroke-width="1.4" stroke-dasharray="1 7"/>
<rect x="34" y="70" width="9" height="7" rx="2" fill="#F2C84B" {W(2)} transform="rotate(-20 38 73)"/>
<path d="M30 70 q-8 4 -10 14 M30 70 q-12 0 -16 8 M30 70 q-4 8 -2 16" fill="none" stroke="#7FD3F5" stroke-width="2.4" stroke-linecap="round"/>
<g>
<circle cx="16" cy="104" r="6" fill="#FFFFFF" {W(1.8)}/><circle cx="16" cy="104" r="2.4" fill="#FFD23F"/>
<circle cx="102" cy="108" r="6" fill="#FFFFFF" {W(1.8)}/><circle cx="102" cy="108" r="2.4" fill="#FFD23F"/>
<circle cx="116" cy="100" r="5" fill="#FFFFFF" {W(1.8)}/><circle cx="116" cy="100" r="2" fill="#FFD23F"/>
</g>
{sparkle(104, 30, 5)}{sparkle(20, 40, 4)}
''')

# 2. Здрасте (Очаковское ш.): берлинер плещется в миске сахарной пудры
add("cafe-zdraste-ochakovskoe-5",
    "берлинер — пышный пончик без дырки с малиновым джемом, выглядывающим сбоку",
    "плещется в голубой миске сахарной пудры, как в сугробе, и подбрасывает белое облачко",
    "zh_sugar", f'''
<path d="M18 80 Q64 80 110 80 Q106 112 64 114 Q22 112 18 80Z" fill="#7FC4E8" {W(3)}/>
<path d="M30 92 Q64 98 98 92" fill="none" stroke="#FFFFFF" stroke-width="3" opacity=".7"/>
<ellipse cx="64" cy="66" rx="34" ry="24" fill="#E0A04F" {W(3)}/>
<path d="M32 62 Q64 52 96 62 Q96 52 64 44 Q32 52 32 62Z" fill="#FFFFFF" opacity=".9"/>
<path d="M96 66 q10 -2 10 6 q-2 6 -10 4Z" fill="#D7264E" {W(2.4)}/>
{eye(54, 66, 0.95)}{eye(72, 66, 0.95)}
<ellipse cx="63" cy="76" rx="4" ry="4.5" fill="#8A2E3A" {W(2)}/>
<ellipse cx="44" cy="74" rx="4" ry="2.3" fill="#FF7FA8" opacity=".7"/><ellipse cx="82" cy="74" rx="4" ry="2.3" fill="#FF7FA8" opacity=".7"/>
<path d="M12 82 Q20 70 30 78 Q38 70 48 80 Q56 72 64 80 Q72 72 80 80 Q90 70 98 78 Q108 70 116 82Z" fill="#FFFFFF" {W(2.6)}/>
<path d="M30 40 q-4 -10 6 -14 q4 -10 14 -6 q8 -4 10 6 q8 4 2 12Z" fill="#FFFFFF" {W(2.2)}/>
<circle cx="76" cy="26" r="3" fill="#FFFFFF" {W(1.6)}/><circle cx="88" cy="34" r="2.4" fill="#FFFFFF" {W(1.6)}/><circle cx="96" cy="22" r="2" fill="#FFFFFF" {W(1.4)}/>
{sparkle(108, 44, 5)}
''')

# 3. Здрасте (ул. Михайлова): детский уголок с книжками — книжка-картонка, из неё выпрыгивает кусочек пиццы
add("cafe-zdraste-mikhailova-30a",
    "раскрытая детская книжка-картонка с толстыми страницами и мордашкой на переплёте",
    "с её разворота, как из окошка, выпрыгивает маленький кусочек пиццы и машет ручкой",
    "zh_book", f'''
<path d="M14 96 L64 104 L114 96 L114 58 L64 66 L14 58Z" fill="#4C8ED9" {W(3)}/>
<path d="M18 92 L62 99 L62 64 L18 57Z" fill="#FFFFFF" {W(2.6)}/>
<path d="M66 99 L110 92 L110 57 L66 64Z" fill="#FFFFFF" {W(2.6)}/>
<path d="M24 70 L52 74 M24 78 L52 82 M24 86 L46 89" stroke="#C9D6EA" stroke-width="3" stroke-linecap="round"/>
<circle cx="86" cy="80" r="8" fill="#FFD23F" opacity=".8"/>
<path d="M64 66 L64 104" {W(2.6)}/>
{eye(40, 108, 0.7)}{eye(88, 108, 0.7)}
<path d="M58 112 Q64 116 70 112" fill="none" {W(2.2)}/>
<g transform="rotate(-14 84 44)">
<path d="M70 22 L100 22 L85 64Z" fill="#F7C548" {W(2.8)}/>
<path d="M68 18 Q85 12 102 18 L100 24 Q85 18 70 24Z" fill="#D9893A" {W(2.6)}/>
<circle cx="80" cy="30" r="3.4" fill="#D9363E"/><circle cx="91" cy="34" r="3" fill="#D9363E"/><circle cx="85" cy="46" r="2.6" fill="#D9363E"/>
{eye(80, 38, 0.6)}{eye(89, 38, 0.6)}
<path d="M82 43 Q85 46 88 43" fill="none" {W(1.8)}/>
<path d="M100 26 L110 16" {W(2.6)}/><circle cx="111" cy="15" r="3" fill="#F7C548" {W(2)}/>
</g>
<path d="M58 40 q-6 -2 -8 -8 M56 50 l-8 0" fill="none" {W(2.2)}/>
{sparkle(30, 32, 5)}{sparkle(112, 54, 4)}
''')

# 4. Здрасте (Большая Почтовая): голубь-почтальон приносит пакетик с выпечкой на подоконник
add("cafe-zdraste-bolshaya-pochtovaya-32",
    "сизый голубь-почтальон в синей фуражке с сумкой через плечо",
    "приземляется на подоконник кофейни, держа в клюве бумажный пакетик с выпечкой",
    "zh_window", f'''
<rect x="10" y="20" width="108" height="78" rx="4" fill="#FFF4DD" {W(3)}/>
<path d="M64 20 L64 98 M10 58 L118 58" stroke="#E2C9A0" stroke-width="3"/>
<rect x="4" y="96" width="120" height="12" rx="3" fill="#FFFFFF" {W(3)}/>
<ellipse cx="62" cy="76" rx="26" ry="20" fill="#9AA6C7" {W(3)}/>
<path d="M40 70 Q30 52 46 50 Q52 64 56 72Z" fill="#7F8BB0" {W(2.6)}/>
<circle cx="70" cy="52" r="14" fill="#A9B4D2" {W(3)}/>
<path d="M62 62 Q70 70 80 62" fill="#7BC6A4" opacity=".8"/>
{eye(74, 50, 0.75)}
<path d="M83 52 L94 55 L83 58Z" fill="#F2A541" {W(2.2)}/>
<path d="M58 42 Q70 34 82 42 L80 46 L60 46Z" fill="#2F4F9C" {W(2.4)}/>
<rect x="66" y="45" width="18" height="3" rx="1.5" fill="#1F2F5C"/>
<path d="M50 62 L72 90" stroke="#8A5A33" stroke-width="3"/>
<rect x="62" y="84" width="18" height="12" rx="2" fill="#B9773E" {W(2.4)}/>
<path d="M54 94 L58 102 M66 94 L64 102" {W(2.6)}/>
<path d="M92 50 L110 50 L108 74 L94 74Z" fill="#D9B07A" {W(2.4)}/>
<path d="M92 50 L96 46 L106 46 L110 50" fill="none" {W(2)}/>
<path d="M97 62 q4 -6 9 0" fill="none" stroke="#B5651D" stroke-width="3"/>
{sparkle(28, 34, 5)}{sparkle(108, 30, 4)}
''')

# 5. Додо Пицца (Хорошёвский, у Ходынки): пицца-солнце восходит над крышами, под ней летит самолётик
add("cafe-dodo-khoroshevsky-3a",
    "круглая пицца-солнце с лучами из хрустящих сырных палочек",
    "восходит над крышами домов, а под ней пролетает маленький белый самолёт",
    "zh_dawn", f'''
<g>
<rect x="56" y="12" width="8" height="18" rx="3" fill="#F6D27A" {W(2)} transform="rotate(0 60 54)"/>
<rect x="56" y="12" width="8" height="18" rx="3" fill="#F6D27A" {W(2)} transform="rotate(40 60 54)"/>
<rect x="56" y="12" width="8" height="18" rx="3" fill="#F6D27A" {W(2)} transform="rotate(-40 60 54)"/>
<rect x="56" y="12" width="8" height="18" rx="3" fill="#F6D27A" {W(2)} transform="rotate(80 60 54)"/>
<rect x="56" y="12" width="8" height="18" rx="3" fill="#F6D27A" {W(2)} transform="rotate(-80 60 54)"/>
</g>
<circle cx="60" cy="56" r="24" fill="#E9A84C" {W(3)}/>
<circle cx="60" cy="56" r="18" fill="#FFD65A"/>
<circle cx="52" cy="64" r="3.2" fill="#D9363E"/><circle cx="70" cy="48" r="3" fill="#D9363E"/>
{eye(53, 53, 0.85)}{eye(67, 53, 0.85)}
<path d="M55 61 Q60 66 65 61" fill="none" {W(2.2)}/>
<path d="M0 128 L0 90 L18 90 L18 80 L34 80 L34 94 L48 94 L48 76 L66 76 L66 92 L80 92 L80 84 L98 84 L98 96 L112 96 L112 82 L128 82 L128 128Z" fill="#6E5A9E" {W(2.8)}/>
<g fill="#FFE27A"><rect x="22" y="86" width="4" height="5"/><rect x="54" y="82" width="4" height="5"/><rect x="54" y="94" width="4" height="5"/><rect x="86" y="90" width="4" height="5"/><rect x="116" y="88" width="4" height="5"/></g>
<g transform="translate(94 66) rotate(-12)">
<path d="M-16 0 Q0 -5 16 0 Q0 5 -16 0Z" fill="#FFFFFF" {W(2.2)}/>
<path d="M-2 -1 L-8 -12 L-2 -12 L6 -1Z" fill="#FFFFFF" {W(2)}/>
<path d="M-12 -1 L-16 -7 L-12 -7 L-8 -1Z" fill="#FFFFFF" {W(1.8)}/>
</g>
<path d="M66 72 q8 -2 12 -6" fill="none" stroke="#FFFFFF" stroke-width="2.2" stroke-dasharray="3 4"/>
''')

# 6. Додо Пицца (Балашиха, Южный): малыш в шапке с помпоном греется стаканчиком какао
add("cafe-dodo-balashikha-nekrasova-5",
    "бумажный стаканчик горячего какао с белой крышечкой и мордашкой",
    "малыш в полосатой шапке с помпоном держит его двумя ладошками и греется на снегу",
    "zh_frost", f'''
<rect x="0" y="104" width="128" height="26" fill="#FFFFFF"/>
<path d="M0 104 Q64 98 128 104" fill="none" {W(2.4)}/>
<path d="M30 128 Q30 96 56 92 L72 92 Q98 96 98 128Z" fill="#E85D75" {W(3)}/>
<circle cx="64" cy="58" r="24" fill="#FFD9B8" {W(3)}/>
<path d="M38 52 Q40 22 64 22 Q88 22 90 52Z" fill="#4D7FD6" {W(3)}/>
<path d="M40 44 L88 44 M42 36 L86 36" stroke="#FFFFFF" stroke-width="4"/>
<path d="M38 52 L90 52" {W(3)}/>
<circle cx="64" cy="18" r="8" fill="#FFFFFF" {W(2.6)}/>
{eye(55, 60, 0.8)}{eye(73, 60, 0.8)}
<ellipse cx="48" cy="68" rx="4" ry="2.3" fill="#FF7FA8" opacity=".75"/><ellipse cx="80" cy="68" rx="4" ry="2.3" fill="#FF7FA8" opacity=".75"/>
<path d="M60 70 Q64 73 68 70" fill="none" {W(2)}/>
<path d="M52 82 L76 82 L73 112 L55 112Z" fill="#F4E7D3" {W(2.8)}/>
<path d="M50 78 L78 78 L77 84 L51 84Z" fill="#FFFFFF" {W(2.4)}/>
<path d="M53 92 L75 92 L74 100 L54 100Z" fill="#8B5A3C"/>
{eye(60, 104, 0.55)}{eye(68, 104, 0.55)}
<ellipse cx="44" cy="98" rx="9" ry="8" fill="#E85D75" {W(2.6)}/><ellipse cx="84" cy="98" rx="9" ry="8" fill="#E85D75" {W(2.6)}/>
<path d="M58 72 q-2 -6 2 -10 M66 72 q2 -6 -2 -10" fill="none" stroke="#FFFFFF" stroke-width="2.4" opacity="0"/>
<path d="M62 76 q-3 -5 0 -8" fill="none" stroke="#FFFFFF" stroke-width="2.2" opacity="0"/>
<circle cx="20" cy="30" r="2.6" fill="#FFFFFF"/><circle cx="106" cy="24" r="3" fill="#FFFFFF"/><circle cx="112" cy="60" r="2.4" fill="#FFFFFF"/><circle cx="16" cy="70" r="2.2" fill="#FFFFFF"/><circle cx="100" cy="86" r="2" fill="#FFFFFF"/>
''')


if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for pid in ids:
        open(os.path.join(OUT, pid + ".svg"), "w").write(ICONS[pid])
    print("svg:", len(ids))
