"""Иконки робота pools, 2026-11-12 (17 UTC). Каждая придумана и нарисована отдельно (правило абсолютной уникальности):
свой герой, своя сцена, своя компоновка и палитра. Запуск: python3 tools/icons_pools_1112.py [id …]
затем python3 tools/render_icons.py <id…> и python3 tools/check_unique.py <id…>."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")


def W(a, b, body, cx=38, cy=28):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
<defs><radialGradient id="g" cx="{cx}%" cy="{cy}%" r="88%"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></radialGradient>
<clipPath id="c"><circle cx="64" cy="64" r="61"/></clipPath></defs>
<circle cx="64" cy="64" r="61" fill="url(#g)"/>
<g clip-path="url(#c)">{body}</g>
</svg>'''


def drop(x, y, k=1.0, c="#4FB7F0"):
    return (f'<path d="M{x} {y - 9 * k:.1f} Q{x + 7 * k:.1f} {y + 1 * k:.1f} {x} {y + 6 * k:.1f} '
            f'Q{x - 7 * k:.1f} {y + 1 * k:.1f} {x} {y - 9 * k:.1f}Z" fill="{c}" {s("stroke-width=\"2.2\"")}/>')


def bub(x, y, r):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".55" {s("stroke-width=\"2\"")}/>'
            f'<circle cx="{x - r * .3:.1f}" cy="{y - r * .3:.1f}" r="{r * .25:.1f}" fill="#fff"/>')


def star(x, y, r, c="#FFD23F"):
    import math
    pts = []
    for i in range(10):
        rr = r if i % 2 == 0 else r * .45
        a = -math.pi / 2 + i * math.pi / 5
        pts.append(f"{x + rr * math.cos(a):.1f},{y + rr * math.sin(a):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{c}" {s("stroke-width=\"2.6\"")}/>'


ICONS, SUBJ = {}, {}

# 1. «Осьминожки» (Пятницкое ш.) — душевая лейка: тёплый дождик перед бассейном
ICONS["osminozhki-pyatnitskoe"] = W("#F2FFF9", "#74D9BC", f'''
<path d="M100 -4 V26 Q100 40 86 40 H70" fill="none" stroke="{O}" stroke-width="13" stroke-linecap="round"/>
<path d="M100 -4 V26 Q100 40 86 40 H70" fill="none" stroke="#DDE3EE" stroke-width="7" stroke-linecap="round"/>
<path d="M22 66 Q22 30 58 30 Q94 30 94 66Z" fill="#FFD23F" {s()}/>
<path d="M32 50 Q38 36 54 34" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".7"/>
<rect x="16" y="62" width="84" height="11" rx="5.5" fill="#EEF2F8" {s()}/>
{face(58, 50, d=11, k=1.05)}
{drop(28, 90, 1.0)}{drop(48, 100, 1.15)}{drop(68, 88, 1.0)}{drop(88, 100, 1.1)}{drop(38, 118, .9)}{drop(78, 116, .9)}
''', 30, 20)
SUBJ["osminozhki-pyatnitskoe"] = ("жёлтая душевая лейка с мордашкой на блестящей трубе",
                                  "льёт тёплый дождик из крупных капель — так малыши ополаскиваются перед заходом в чашу")

# 2. «Золотой Моржик» (Митино) — калан на спине с золотой звездой
ICONS["zolotoy-morzhik-mitino"] = W("#FFF8D6", "#F2B63C", f'''
<path d="M-6 62 Q8 56 22 62 T50 62 T78 62 T106 62 T134 62 V134 H-6Z" fill="#3FB6C9" {s('stroke-width="2.6"')}/>
<path d="M92 66 Q112 50 118 62 Q112 72 98 76Z" fill="#8A5A2B" {s()}/>
<ellipse cx="66" cy="74" rx="38" ry="17" fill="#A86B34" {s()}/>
<ellipse cx="68" cy="70" rx="27" ry="10" fill="#E3B57A"/>
<path d="M96 60 q4 -12 12 -8 q2 8 -6 13Z" fill="#8A5A2B" {s('stroke-width="2.8"')}/>
<circle cx="30" cy="64" r="19" fill="#B97A3E" {s()}/>
<circle cx="15" cy="52" r="5.5" fill="#8A5A2B" {s('stroke-width="2.6"')}/><circle cx="44" cy="50" r="5.5" fill="#8A5A2B" {s('stroke-width="2.6"')}/>
<ellipse cx="30" cy="70" rx="12" ry="9" fill="#F4E3C5"/>
{eye(23, 61, .9)}{eye(37, 61, .9)}
<ellipse cx="30" cy="67" rx="3.4" ry="2.4" fill="{O}"/>
<path d="M25 72 Q30 77 35 72" fill="none" {s('stroke-width="2.4"')}/>
{star(68, 60, 15)}
<ellipse cx="54" cy="68" rx="6" ry="4.5" fill="#8A5A2B" {s('stroke-width="2.6"')}/><ellipse cx="82" cy="68" rx="6" ry="4.5" fill="#8A5A2B" {s('stroke-width="2.6"')}/>
<path d="M-6 98 Q20 92 46 98 T98 98 T150 98 V134 H-6Z" fill="#2A9DB3" opacity=".6"/>
''', 60, 18)
SUBJ["zolotoy-morzhik-mitino"] = ("золотисто-бурый калан с круглыми ушками",
                                  "лежит на спине на бирюзовой воде и держит лапками на животе золотую звезду")

# 4. Strong Swim (Рязанский пр-т) — угорь-силач с гантелей
ICONS["strong-swim-ryazansky"] = W("#FFF1DC", "#FFA552", f'''
<path d="M-6 108 Q30 100 64 108 T134 108 V134 H-6Z" fill="#E8C98A" {s('stroke-width="2.6"')}/>
<path d="M34 34 Q76 20 82 48 Q86 70 52 70 Q26 72 34 90 Q44 106 86 96" fill="none" stroke="{O}" stroke-width="25" stroke-linecap="round"/>
<path d="M34 34 Q76 20 82 48 Q86 70 52 70 Q26 72 34 90 Q44 106 86 96" fill="none" stroke="#1FA37A" stroke-width="18.5" stroke-linecap="round"/>
<path d="M40 30 Q70 22 78 44" fill="none" stroke="#7BE0B8" stroke-width="5" stroke-linecap="round" opacity=".8"/>
<circle cx="32" cy="36" r="17" fill="#1FA37A" {s()}/>
<ellipse cx="30" cy="42" rx="10" ry="7" fill="#C9F5DF"/>
{face(30, 34, d=7, k=.85)}
<path d="M70 96 H116" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M70 96 H116" stroke="#C9CFDA" stroke-width="3" stroke-linecap="round"/>
<rect x="60" y="80" width="13" height="32" rx="5" fill="#3B4A6B" {s()}/><rect x="108" y="80" width="13" height="32" rx="5" fill="#3B4A6B" {s()}/>
{bub(100, 40, 7)}{bub(110, 24, 4.5)}{bub(92, 22, 3.5)}
''', 70, 25)
SUBJ["strong-swim-ryazansky"] = ("изумрудный угорь-силач с довольной мордочкой",
                                 "обвил хвостом гантель и отрывает её от песчаного дна, пуская пузыри от натуги")

# 5. Свин Свим (Живописная) — спасательный жилет плывёт на спине
ICONS["svin-svim-zhivopisnaya"] = W("#B9C6FF", "#2B3A8C", f'''
{sparkle(24, 26, 5)}{sparkle(104, 20, 6)}{sparkle(92, 40, 3)}
<path d="M30 40 Q30 26 44 26 L54 26 Q64 40 74 26 L84 26 Q98 26 98 40 L102 92 Q64 104 26 92Z" fill="#FF8A2B" {s()}/>
<path d="M54 26 Q64 46 74 26" fill="#2B3A8C" {s()}/>
<path d="M64 44 V98" stroke="{O}" stroke-width="3"/>
<path d="M28 62 H100 M27 80 H101" stroke="{O}" stroke-width="9"/>
<path d="M28 62 H100 M27 80 H101" stroke="#FFE14D" stroke-width="5"/>
<rect x="58" y="57" width="12" height="10" rx="2" fill="#2B2B3A"/><rect x="58" y="75" width="12" height="10" rx="2" fill="#2B2B3A"/>
{eye(46, 46, .9)}{eye(82, 46, .9)}
<path d="M-6 96 Q10 88 26 96 T58 96 T90 96 T122 96 T154 96 V134 H-6Z" fill="#6FD3F2" {s('stroke-width="2.6"')}/>
<path d="M-6 112 Q20 106 46 112 T98 112 T150 112 V134 H-6Z" fill="#3FA9DC"/>
''', 50, 20)
SUBJ["svin-svim-zhivopisnaya"] = ("оранжевый спасательный жилет с жёлтыми стропами и глазками",
                                  "сам качается по пояс в волне вечернего бассейна под звёздами, расправив плечи")

# 6. Mam Balance kids (Мосфильмовская) — рыба-ангел учит малька держать пузырь
ICONS["mam-balance-mosfilmovskaya"] = W("#FFF0F6", "#F285B4", f'''
<path d="M52 44 Q64 4 84 10 Q78 30 74 46Z" fill="#FFE9A8" {s()}/>
<path d="M52 84 Q64 124 84 118 Q78 98 74 82Z" fill="#FFE9A8" {s()}/>
<path d="M94 64 L120 44 Q114 64 120 84Z" fill="#FFE9A8" {s()}/>
<path d="M28 64 Q52 30 82 44 Q100 54 100 64 Q100 74 82 84 Q52 98 28 64Z" fill="#F7F9FF" {s()}/>
<path d="M58 40 Q52 64 58 88 M76 42 Q70 64 76 86" fill="none" stroke="#2B2B3A" stroke-width="6" stroke-linecap="round"/>
{eye(42, 60, 1.0)}
<path d="M32 68 Q37 72 42 69" fill="none" {s('stroke-width="2.4"')}/>
<ellipse cx="46" cy="70" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/>
<path d="M24 104 L34 96 L34 112Z" fill="#FFE9A8" {s('stroke-width="2.4"')}/>
<ellipse cx="16" cy="104" rx="10" ry="7" fill="#F7F9FF" {s('stroke-width="2.6"')}/>
<circle cx="12" cy="102" r="2" fill="{O}"/>
{bub(12, 84, 9)}
''', 30, 75)
SUBJ["mam-balance-mosfilmovskaya"] = ("белая рыба-ангел скалярия с двумя чёрными полосками и высокими плавниками-парусами",
                                      "плывёт рядом с мальком, который учится удерживать на носу большой воздушный пузырь")

# 7. «Дельфин» (Щёлково) — кит-горбач свечкой на закате
ICONS["delfin-shchyolkovo"] = W("#FFF4C4", "#FF8F5A", f'''
<circle cx="100" cy="30" r="14" fill="#FFF7D6" opacity=".9"/>
<path d="M30 112 Q20 60 52 26 Q70 10 84 22 Q92 60 76 112Z" fill="#3E5F9C" {s()}/>
<path d="M42 112 Q34 66 58 34 Q70 24 78 30 Q82 62 70 112Z" fill="#F4F7FF"/>
<path d="M50 104 Q46 70 62 44 M58 106 Q56 74 70 50 M66 106 Q66 80 76 60" fill="none" stroke="#B9C6E6" stroke-width="2.4" stroke-linecap="round"/>
<path d="M36 70 Q6 62 2 34 Q22 44 44 54Z" fill="#F4F7FF" {s()}/>
<circle cx="60" cy="30" r="3.6" fill="{O}"/><circle cx="59" cy="29" r="1.3" fill="#fff"/>
<path d="M68 34 Q76 40 82 34" fill="none" {s('stroke-width="2.6"')}/>
<path d="M-6 104 Q10 94 26 104 T58 104 T90 104 T122 104 T154 104 V134 H-6Z" fill="#3FA9DC" {s('stroke-width="2.6"')}/>
<path d="M22 102 q-8 -16 -16 -6 M84 102 q10 -18 18 -4 M92 96 q12 -6 14 4" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
''', 78, 22)
SUBJ["delfin-shchyolkovo"] = ("синий кит-горбач с бороздчатым белым брюшком и длинным белым плавником",
                              "выпрыгивает из моря свечкой на оранжевом закате и машет плавником солнцу")

# 8. Starfish (Щербинка) — лангуст в надувном круге
ICONS["starfish-shcherbinka"] = W("#DBFFF9", "#2FB7A4", f'''
<path d="M52 40 Q30 10 6 22 M76 40 Q98 10 122 22" fill="none" stroke="{O}" stroke-width="6.5" stroke-linecap="round"/>
<path d="M52 40 Q30 10 6 22 M76 40 Q98 10 122 22" fill="none" stroke="#FF6B5E" stroke-width="3" stroke-linecap="round"/>
<ellipse cx="64" cy="58" rx="24" ry="27" fill="#FF6B5E" {s()}/>
<path d="M44 46 l-6 -8 M84 46 l6 -8 M48 36 l-3 -9 M80 36 l3 -9" stroke="{O}" stroke-width="3" stroke-linecap="round"/>
<path d="M46 66 Q64 74 82 66" fill="none" stroke="#D94A3F" stroke-width="3" stroke-linecap="round"/>
{face(64, 52, d=9, k=1.0)}
<ellipse cx="64" cy="92" rx="50" ry="20" fill="#7CC8FF" {s()}/>
<ellipse cx="64" cy="87" rx="26" ry="8" fill="#2A8E80" {s('stroke-width="2.6"')}/>
<path d="M40 86 Q64 60 88 86 Q64 96 40 86Z" fill="#FF6B5E"/>
<path d="M22 86 Q30 78 44 76 M106 86 Q98 78 84 76" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".75"/>
<path d="M20 100 l8 5 M108 100 l-8 5 M64 111 v-7" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
''', 50, 12)
SUBJ["starfish-shcherbinka"] = ("красный лангуст с длинными усами-антеннами и шипиками на панцире",
                                "сидит в голубом надувном круге с белыми полосками и рулит усами, как вёслами")

# 9. Starfish (пр. Шелихова) — рыба-попугай ведёт стайку от мала до велика
ICONS["starfish-shelikhova"] = W("#FFFCE0", "#FFCB2E", f'''
<path d="M36 52 L10 30 Q16 54 10 78Z" fill="#7B5BE0" {s()}/>
<path d="M52 34 Q72 14 96 30 L88 42Z" fill="#FF7FB0" {s()}/>
<path d="M30 54 Q52 22 92 34 Q118 44 118 58 Q118 72 92 80 Q52 90 30 54Z" fill="#19B8B0" {s()}/>
<path d="M50 44 Q62 56 50 70 M64 40 Q76 56 64 74" fill="none" stroke="#0E8F92" stroke-width="3" stroke-linecap="round"/>
<path d="M84 60 Q96 54 104 62 Q96 74 84 70Z" fill="#FF9F43" {s('stroke-width="2.6"')}/>
<path d="M108 50 L122 54 L122 64 L108 68 Q104 59 108 50Z" fill="#FFF7E0" {s('stroke-width="2.8"')}/>
<path d="M110 59 H122" stroke="{O}" stroke-width="2"/>
{eye(98, 46, 1.0)}
<ellipse cx="92" cy="54" rx="4.5" ry="2.6" fill="#FF7FA8" opacity=".7"/>
<g {s('stroke-width="2.6"')}><path d="M62 104 l-10 -7 v14Z" fill="#7B5BE0"/><ellipse cx="72" cy="104" rx="12" ry="7.5" fill="#FF7FB0"/>
<path d="M32 100 l-8 -6 v12Z" fill="#7B5BE0"/><ellipse cx="40" cy="100" rx="9" ry="5.5" fill="#FF9F43"/>
<path d="M12 108 l-6 -4 v9Z" fill="#7B5BE0"/><ellipse cx="18" cy="108" rx="6" ry="4" fill="#19B8B0"/></g>
<circle cx="78" cy="102" r="1.8" fill="{O}"/><circle cx="44" cy="99" r="1.6" fill="{O}"/><circle cx="20" cy="107" r="1.3" fill="{O}"/>
''', 30, 20)
SUBJ["starfish-shelikhova"] = ("радужная рыба-попугай с белым клювиком, бирюзовым боком и розовым гребнем",
                               "ведёт за собой стайку рыбок разного роста — от крошки до подростка")

# 10. «Как рыбка в воде» (Балашиха) — рыба-бабочка выдувает пузыри
ICONS["kak-rybka-balashikha"] = W("#F3E8FF", "#A77BEA", f'''
<path d="M40 30 Q66 6 96 28 L90 40Z" fill="#FF9F43" {s()}/>
<path d="M92 66 L120 48 Q114 68 122 90Z" fill="#FFE14D" {s()}/>
<path d="M44 100 Q66 118 90 100 L86 90Z" fill="#FF9F43" {s()}/>
<path d="M14 70 L34 56 Q52 26 80 34 Q100 44 100 68 Q100 92 78 100 Q52 106 34 82Z" fill="#FFE14D" {s()}/>
<path d="M46 36 Q36 64 50 98 L62 100 Q48 64 58 32Z" fill="#2B2B3A"/>
<path d="M84 40 Q92 68 82 98" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/>
<circle cx="50" cy="60" r="6" fill="#fff"/><circle cx="50" cy="60" r="3.4" fill="{O}"/><circle cx="48.8" cy="58.6" r="1.2" fill="#fff"/>
<path d="M22 74 Q28 78 34 76" fill="none" {s('stroke-width="2.4"')}/>
<path d="M64 62 Q78 56 80 70 Q72 80 64 74Z" fill="#FFF3A6" {s('stroke-width="2.6"')}/>
{bub(12, 52, 6)}{bub(22, 34, 8)}{bub(10, 22, 4)}
''', 62, 80)
SUBJ["kak-rybka-balashikha"] = ("жёлтая рыба-бабочка с чёрной маской через глаз и вытянутым носиком",
                                "выдувает носиком-трубочкой вереницу пузырей в сиреневой воде")

# 11. «Синхро Старс» (Лухмановская) — две рыбы-иглы буквой V со звездой
ICONS["synchro-stars-lukhmanovskaya"] = W("#D5C8FF", "#4B33B5", f'''
{star(64, 30, 15)}
<g transform="rotate(-20 40 92)">
<path d="M33 96 L36 4 L40 -6 L44 4 L47 96Z" fill="#C9D6EA" {s()}/>
<path d="M40 30 V96" stroke="#3E8FD9" stroke-width="3.4"/>
<circle cx="40" cy="42" r="3" fill="{O}"/>
<path d="M33 66 l-10 6 l10 4 M47 66 l10 6 l-10 4" fill="#8FB3E8" {s('stroke-width="2.4"')}/>
</g>
<g transform="rotate(20 88 92)">
<path d="M81 96 L84 4 L88 -6 L92 4 L95 96Z" fill="#C9D6EA" {s()}/>
<path d="M88 30 V96" stroke="#3E8FD9" stroke-width="3.4"/>
<circle cx="88" cy="42" r="3" fill="{O}"/>
<path d="M81 66 l-10 6 l10 4 M95 66 l10 6 l-10 4" fill="#8FB3E8" {s('stroke-width="2.4"')}/>
</g>
<path d="M-6 92 Q10 84 26 92 T58 92 T90 92 T122 92 T154 92 V134 H-6Z" fill="#59C8F0" {s('stroke-width="2.6"')}/>
<ellipse cx="40" cy="96" rx="15" ry="4" fill="none" stroke="#fff" stroke-width="3"/><ellipse cx="88" cy="96" rx="15" ry="4" fill="none" stroke="#fff" stroke-width="3"/>
<path d="M-6 112 Q20 106 46 112 T98 112 T150 112 V134 H-6Z" fill="#2E9BD6"/>
''', 50, 10)
SUBJ["synchro-stars-lukhmanovskaya"] = ("две серебристые рыбы-иглы с длинными острыми носами и синей полоской",
                                        "синхронно высунулись из воды буквой V и тянутся носами к золотой звезде")

# 12. «Поколение» (пр-т Вернадского) — оляпка в очках учит птенца нырять
ICONS["pokolenie-vernadskogo"] = W("#EDFFE0", "#69C95C", f'''
<path d="M-6 94 Q10 88 26 94 T58 94 T90 94 T122 94 T154 94 V134 H-6Z" fill="#58C4EE" {s('stroke-width="2.6"')}/>
<path d="M-4 96 Q10 66 44 70 Q76 74 82 98Z" fill="#A9B4C6" {s()}/>
<path d="M10 84 Q26 74 44 78" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".6"/>
<path d="M22 38 L4 30 L16 46Z" fill="#6B4A2E" {s('stroke-width="2.8"')}/>
<ellipse cx="42" cy="48" rx="25" ry="22" fill="#7A5535" {s()}/>
<path d="M44 36 Q66 40 62 60 Q52 70 40 64 Q34 48 44 36Z" fill="#fff"/>
<path d="M30 68 v8 M46 69 v8" stroke="{O}" stroke-width="3.2" stroke-linecap="round"/>
<path d="M65 44 L80 48 L65 52Z" fill="#3B3355"/>
<path d="M38 40 H64" stroke="#2B2B3A" stroke-width="3"/>
<circle cx="56" cy="41" r="7" fill="#8FE3FF" {s('stroke-width="2.8"')}/><circle cx="54" cy="39" r="2" fill="#fff"/><circle cx="57" cy="42" r="2.6" fill="{O}"/>
<path d="M82 76 L72 72 L78 82Z" fill="#6B4A2E" {s('stroke-width="2.4"')}/>
<ellipse cx="94" cy="80" rx="15" ry="13" fill="#9A7350" {s()}/>
<path d="M96 72 Q108 76 104 88 Q98 92 92 88 Q90 78 96 72Z" fill="#fff"/>
<path d="M107 78 L117 81 L107 84Z" fill="#3B3355"/>
<circle cx="100" cy="76" r="2.6" fill="{O}"/>
<path d="M88 92 v6 M98 92 v6" stroke="{O}" stroke-width="2.8" stroke-linecap="round"/>
<path d="M70 108 q8 -8 16 0 M96 114 q8 -8 16 0" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
''', 70, 20)
SUBJ["pokolenie-vernadskogo"] = ("бурая птичка-оляпка с белой манишкой в голубых плавательных очках и её птенец",
                                 "стоит на сером камне у воды и показывает птенцу, как нырять с берега")

if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    reg = os.path.join(OUT, "subjects.txt")
    lines = [l for l in open(reg, encoding="utf-8").read().splitlines() if l.split(" — ")[0] not in ids]
    for pid in ids:
        open(os.path.join(OUT, f"{pid}.svg"), "w").write(ICONS[pid])
        lines.append(f"{pid} — герой: {SUBJ[pid][0]} | сцена: {SUBJ[pid][1]}")
    open(reg, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(len(ids))
