"""Иконки робота pools, 2026-11-12 (20–22 UTC). Каждая придумана и нарисована отдельно (правило абсолютной
уникальности): свой герой, своя сцена, своя компоновка и палитра. Запуск: python3 tools/icons_pools_1112b.py [id …]
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


def bub(x, y, r, op=.6):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity="{op}" {s("stroke-width=\"2\"")}/>'
            f'<circle cx="{x - r * .3:.1f}" cy="{y - r * .3:.1f}" r="{r * .25:.1f}" fill="#fff"/>')


T2 = 'stroke-width="2.4"'
ICONS, SUBJ = {}, {}

# 1. Грудничковое плавание М98 (ул. Удальцова) — аксолотль: вечный малыш, который живёт в воде
ICONS["m98-udaltsova"] = W("#F4EBFF", "#8E6BE0", f'''
<path d="M78 84 Q104 86 116 108 Q96 112 80 100Z" fill="#FF9EC0" {s()}/>
<path d="M92 92 Q104 96 110 106" fill="none" {s(T2)}/>
<ellipse cx="70" cy="90" rx="24" ry="15" fill="#FFB7D2" {s()}/>
<path d="M52 98 Q46 108 40 106 M84 102 Q86 112 80 114" fill="none" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M52 98 Q46 108 40 106 M84 102 Q86 112 80 114" fill="none" stroke="#FFB7D2" stroke-width="3.4" stroke-linecap="round"/>
<path d="M28 44 Q8 34 6 22 M24 54 Q4 54 -2 44 M26 64 Q8 72 2 68" fill="none" stroke="{O}" stroke-width="10" stroke-linecap="round"/>
<path d="M28 44 Q8 34 6 22 M24 54 Q4 54 -2 44 M26 64 Q8 72 2 68" fill="none" stroke="#E0457F" stroke-width="5" stroke-linecap="round"/>
<path d="M92 44 Q112 34 114 22 M96 54 Q116 54 122 44 M94 64 Q112 72 118 68" fill="none" stroke="{O}" stroke-width="10" stroke-linecap="round"/>
<path d="M92 44 Q112 34 114 22 M96 54 Q116 54 122 44 M94 64 Q112 72 118 68" fill="none" stroke="#E0457F" stroke-width="5" stroke-linecap="round"/>
<ellipse cx="60" cy="54" rx="37" ry="28" fill="#FFC6DC" {s()}/>
{eye(42, 52, 1.15)}{eye(78, 52, 1.15)}
<ellipse cx="34" cy="63" rx="5" ry="3" fill="#FF6FA0" opacity=".6"/><ellipse cx="86" cy="63" rx="5" ry="3" fill="#FF6FA0" opacity=".6"/>
<path d="M48 62 Q60 74 72 62" fill="none" {s()}/>
{bub(104, 84, 5)}{bub(20, 96, 4)}
''', 60, 20)
SUBJ["m98-udaltsova"] = ("розовый аксолотль с малиновыми веточками-жабрами и улыбкой до ушей",
                         "гребёт короткими лапками в сиреневой воде — вечный малыш, которому в воде как дома")

# 2. «Аквапузики» (Одинцово) — бобрёнок шлёпает хвостом
ICONS["akvapuziki-odintsovo"] = W("#F3FFE0", "#8FD45A", f'''
<path d="M84 70 Q112 40 122 52 Q124 74 96 88Z" fill="#6B4A2E" {s()}/>
<path d="M96 62 L112 72 M104 54 L118 64 M92 72 L104 82" fill="none" stroke="#4A321E" stroke-width="2.2" stroke-linecap="round"/>
<circle cx="30" cy="30" r="9" fill="#8A5A34" {s()}/><circle cx="74" cy="26" r="9" fill="#8A5A34" {s()}/>
<path d="M18 92 Q14 30 52 26 Q90 30 88 92Z" fill="#A9713F" {s()}/>
<ellipse cx="52" cy="80" rx="22" ry="20" fill="#F0CF9C"/>
{eye(40, 48, 1.1)}{eye(64, 48, 1.1)}
<ellipse cx="52" cy="58" rx="6.5" ry="4.5" fill="{O}"/>
<path d="M46 64 H58 V74 H46Z" fill="#fff" {s(T2)}/><path d="M52 64 V74" stroke="{O}" stroke-width="1.8"/>
<ellipse cx="32" cy="60" rx="4.5" ry="2.8" fill="#FF7FA8" opacity=".6"/><ellipse cx="72" cy="60" rx="4.5" ry="2.8" fill="#FF7FA8" opacity=".6"/>
<path d="M-6 92 Q10 84 24 92 T54 92 T84 92 T114 92 T140 92 V134 H-6Z" fill="#3D9BE0" {s('stroke-width="2.6"')}/>
<path d="M10 106 Q20 101 30 106 M60 112 Q70 107 80 112" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".7"/>
<path d="M106 28 Q110 36 106 40 Q102 36 106 28Z M118 34 Q121 40 118 43 Q115 40 118 34Z M94 34 Q97 40 94 43 Q91 40 94 34Z" fill="#3D9BE0" {s('stroke-width="2"')}/>
''', 30, 22)
SUBJ["akvapuziki-odintsovo"] = ("бобрёнок с двумя белыми зубами и светлым круглым пузиком",
                                "стоит по пояс в чаше и шлёпает плоским клетчатым хвостом — брызги летят выше ушей")

# 3. Bubbles Team Oz (Орехово-Зуево) — сомик выдувает пузыри
ICONS["bubbles-team-orekhovo-zuevo"] = W("#7FA8F5", "#1F2F86", f'''
<path d="M-10 140 Q-12 60 34 52 Q84 50 86 140Z" fill="#5E7A8C" {s()}/>
<path d="M-4 112 Q2 96 14 92" fill="none" stroke="#3F5868" stroke-width="3" stroke-linecap="round"/>
<ellipse cx="44" cy="84" rx="38" ry="31" fill="#7C9CB0" {s()}/>
<ellipse cx="44" cy="100" rx="22" ry="11" fill="#DDEAF0"/>
{eye(28, 74, 1.25)}{eye(56, 72, 1.25)}
<ellipse cx="74" cy="88" rx="7" ry="8.5" fill="#2A3B66" {s(T2)}/>
<path d="M68 100 Q92 112 106 102 M64 106 Q82 126 98 122 M20 96 Q4 108 -4 100 M24 102 Q12 120 2 118" fill="none" {s('stroke-width="3"')}/>
{bub(90, 70, 7, .8)}{bub(100, 48, 10, .8)}{bub(98, 22, 14, .85)}
{sparkle(30, 26, 6, "#FFE27A")}{sparkle(58, 38, 4, "#FFE27A")}
''', 70, 20)
SUBJ["bubbles-team-orekhovo-zuevo"] = ("серо-голубой сомик с длинными усами и круглым ртом",
                                       "со дна ночного омута выдувает три пузыря один больше другого — команда «пузыри!» перед нырком")

# 4. KidWay (Пятницкое ш.) — жёлтая субмарина держит курс
ICONS["kidway-pyatnitskoe"] = W("#DDF9FF", "#18A7B5", f'''
<path d="M-6 30 Q10 22 26 30 T58 30 T90 30 T122 30 T140 30 V-6 H-6Z" fill="#FFF6D8"/>
<path d="M-6 30 Q10 22 26 30 T58 30 T90 30 T122 30 T140 30" fill="none" {s('stroke-width="2.6"')}/>
<path d="M70 50 V16 H88" fill="none" stroke="{O}" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M70 50 V16 H88" fill="none" stroke="#F0483E" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M100 66 L118 52 V96 L100 82Z" fill="#F0483E" {s()}/>
<rect x="18" y="46" width="88" height="46" rx="23" fill="#FFD23F" {s()}/>
<path d="M30 56 Q44 49 62 50" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".75"/>
<circle cx="44" cy="68" r="13" fill="#DFF7FF" {s()}/>{eye(44, 68, 1.25)}
<circle cx="74" cy="70" r="6" fill="#DFF7FF" {s(T2)}/><circle cx="90" cy="70" r="6" fill="#DFF7FF" {s(T2)}/>
<path d="M26 80 Q32 86 40 84" fill="none" {s(T2)}/>
<path d="M8 110 H20 M32 110 H44 M56 110 H68 M80 110 H92 M104 110 H116" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".85"/>
{bub(12, 62, 4)}{bub(6, 78, 3)}
''', 40, 70)
SUBJ["kidway-pyatnitskoe"] = ("жёлтая подводная лодочка с глазом-иллюминатором и красным перископом",
                              "идёт под водой ровно над белой пунктирной линией — держит свой путь, перископ выглядывает над волной")

# 5. Sweet Baby Swim (Одинцово) — жемчужина в раковине
ICONS["sweet-baby-swim-odintsovo"] = W("#FFF4E6", "#FF9C7A", f'''
<path d="M64 70 L18 30 Q30 8 64 6 Q98 8 110 30Z" fill="#C7A6F7" {s()}/>
<path d="M64 68 L40 16 M64 68 L64 8 M64 68 L88 16" fill="none" stroke="#9A73DE" stroke-width="2.6" stroke-linecap="round"/>
<path d="M10 78 Q64 60 118 78 Q112 118 64 122 Q16 118 10 78Z" fill="#B48EF0" {s()}/>
<path d="M22 86 Q64 72 106 86" fill="none" stroke="#E9DBFF" stroke-width="3.4" stroke-linecap="round"/>
<path d="M40 112 L46 92 M64 118 V96 M88 112 L82 92" fill="none" stroke="#9A73DE" stroke-width="2.6" stroke-linecap="round"/>
<circle cx="64" cy="68" r="23" fill="#fff" {s()}/>
<path d="M48 58 Q54 48 64 48" fill="none" stroke="#FFD9E6" stroke-width="5" stroke-linecap="round"/>
{face(64, 68, d=8, k=.95)}
''', 50, 80)
SUBJ["sweet-baby-swim-odintsovo"] = ("белая жемчужина с румяной мордашкой в распахнутой сиреневой раковине-гребешке",
                                     "сладко устроилась между створками на персиковом дне — самое тёплое и бережное место для малыша")

# 6. «АкваКрабсКлуб» (Дмитровское ш.) — надувной круг с клешнями
ICONS["akvakrabsklub-dmitrovskoe"] = W("#FFFBE0", "#FFC83D", f'''
<path d="M30 58 Q10 46 12 26" fill="none" stroke="{O}" stroke-width="10" stroke-linecap="round"/>
<path d="M30 58 Q10 46 12 26" fill="none" stroke="#F0563C" stroke-width="5" stroke-linecap="round"/>
<path d="M98 58 Q118 46 116 26" fill="none" stroke="{O}" stroke-width="10" stroke-linecap="round"/>
<path d="M98 58 Q118 46 116 26" fill="none" stroke="#F0563C" stroke-width="5" stroke-linecap="round"/>
<path d="M12 28 Q-2 20 4 6 Q10 14 14 14 Q14 4 24 4 Q28 20 12 28Z" fill="#F0563C" {s()}/>
<path d="M116 28 Q130 20 124 6 Q118 14 114 14 Q114 4 104 4 Q100 20 116 28Z" fill="#F0563C" {s()}/>
<path d="M52 44 V26 M76 44 V26" stroke="{O}" stroke-width="3.2" stroke-linecap="round"/>
<circle cx="52" cy="22" r="8" fill="#fff" {s()}/>{eye(52, 22, .9)}<circle cx="76" cy="22" r="8" fill="#fff" {s()}/>{eye(76, 22, .9)}
<ellipse cx="64" cy="76" rx="44" ry="34" fill="#F0563C" {s()}/>
<path d="M30 56 Q38 46 50 44 M98 96 Q90 106 78 108 M30 96 Q38 106 50 108 M98 56 Q90 46 78 44" fill="none" stroke="#fff" stroke-width="9" stroke-linecap="butt"/>
<ellipse cx="64" cy="76" rx="44" ry="34" fill="none" {s()}/>
<ellipse cx="64" cy="76" rx="19" ry="13" fill="#3DB7E4" {s()}/>
<path d="M54 76 Q59 72 64 76 T74 76" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<path d="M46 62 Q64 54 82 62" fill="none" {s(T2)}/>
''', 50, 20)
SUBJ["akvakrabsklub-dmitrovskoe"] = ("красный надувной круг в белую полоску с двумя клешнями и глазками на стебельках",
                                     "поднял клешни вверх как на зарядке, в серединке плещется голубая вода — заходи и держись")

# 7. «Каури» (Коммунарка) — ракушка каури на волне-ладошке
ICONS["kauri-kommunarka"] = W("#E2FFF6", "#149C8E", f'''
<path d="M-8 96 Q6 70 26 78 Q30 60 44 68 Q50 54 62 64 Q72 54 80 68 Q96 62 100 80 Q120 76 136 100 V136 H-8Z" fill="#8FE3F2" {s()}/>
<path d="M-8 110 Q30 96 64 108 T136 106 V136 H-8Z" fill="#4CC3DE"/>
<path d="M10 104 Q30 96 48 104 M78 110 Q96 102 116 108" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
<ellipse cx="64" cy="46" rx="40" ry="28" fill="#FBEBCB" {s()}/>
<path d="M30 48 Q64 62 98 48" fill="none" {s('stroke-width="2.8"')}/>
<path d="M38 50 V56 M46 53 V59 M55 55 V61 M64 56 V62 M73 55 V61 M82 53 V59 M90 50 V56" stroke="{O}" stroke-width="2.2" stroke-linecap="round"/>
<circle cx="40" cy="30" r="4.5" fill="#B9753A"/><circle cx="58" cy="24" r="3.5" fill="#B9753A"/><circle cx="78" cy="26" r="4.5" fill="#B9753A"/>
<circle cx="92" cy="36" r="3.2" fill="#B9753A"/><circle cx="30" cy="40" r="3" fill="#B9753A"/><circle cx="68" cy="34" r="2.6" fill="#B9753A"/>
{eye(52, 40, .95)}{eye(76, 40, .95)}
<ellipse cx="44" cy="47" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/><ellipse cx="84" cy="47" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/>
''', 30, 30)
SUBJ["kauri-kommunarka"] = ("кремовая ракушка каури в карамельную крапинку с зубчатой улыбкой",
                            "лежит на гребне голубой волны, а волна держит её пятью пенными пальцами, как заботливая ладонь")

# 8. «Море рядом» (Новороссийская ул.) — море за дверью
ICONS["more-ryadom-novorossiyskaya"] = W("#FFE9F1", "#E86A9A", f'''
<rect x="14" y="12" width="58" height="104" fill="#2E86C9" {s()}/>
<circle cx="56" cy="30" r="8" fill="#FFE27A" {s(T2)}/>
<path d="M14 58 Q28 50 42 58 T72 58 V116 H14Z" fill="#38B5E6"/>
<path d="M14 12 L46 24 V128 L14 116Z" fill="#fff" {s()}/>
<path d="M22 30 L38 36 V62 L22 58Z M22 72 L38 76 V108 L22 104Z" fill="#E8EEF7" {s(T2)}/>
<circle cx="40" cy="70" r="3.6" fill="#FFB02E" {s('stroke-width="2"')}/>
<path d="M46 70 Q64 56 80 72 Q92 60 106 74 Q118 66 134 80 V134 H46Z" fill="#38B5E6" {s()}/>
<path d="M56 86 Q66 80 76 86 M92 96 Q102 90 112 96" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".85"/>
<path d="M96 104 L108 96 V118Z" fill="#FF8A3C" {s(T2)}/>
<ellipse cx="82" cy="107" rx="16" ry="11" fill="#FFA24D" {s()}/>
{eye(74, 104, .9)}<path d="M68 111 Q72 114 76 111" fill="none" {s('stroke-width="2.2"')}/>
''', 80, 20)
SUBJ["more-ryadom-novorossiyskaya"] = ("белая приоткрытая дверь с золотой ручкой, а за ней — синее море и солнце",
                                       "из дверного проёма в розовую комнату выкатывается волна и выносит оранжевую рыбку — море совсем рядом")

# 10. «Утка БОСС» (ул. Лескова) — тритон-босс на матрасе (уточка в каталоге занята)
ICONS["utka-boss-leskova"] = W("#DCFCFF", "#27AEDD", f'''
<path d="M-6 30 H134 M-6 64 H134 M-6 98 H134 M30 -6 V134 M64 -6 V134 M98 -6 V134" stroke="#fff" stroke-width="2" opacity=".35"/>
<g transform="rotate(-18 64 70)">
<rect x="12" y="46" width="104" height="50" rx="12" fill="#fff" {s()}/>
<path d="M36 46 V96 M60 46 V96 M84 46 V96" stroke="#F0483E" stroke-width="12"/>
<rect x="12" y="46" width="104" height="50" rx="12" fill="none" {s()}/>
<path d="M84 74 Q112 78 122 62" fill="none" stroke="{O}" stroke-width="11" stroke-linecap="round"/>
<path d="M84 74 Q112 78 122 62" fill="none" stroke="#FF9A3C" stroke-width="6" stroke-linecap="round"/>
<path d="M52 60 L46 48 M78 60 L84 48 M52 82 L46 94 M78 82 L84 94" stroke="{O}" stroke-width="8" stroke-linecap="round"/>
<path d="M52 60 L46 48 M78 60 L84 48 M52 82 L46 94 M78 82 L84 94" stroke="#FF9A3C" stroke-width="4" stroke-linecap="round"/>
<ellipse cx="66" cy="71" rx="26" ry="14" fill="#FF9A3C" {s()}/>
<path d="M50 64 L54 58 L58 64 L62 58 L66 64 L70 58 L74 64 L78 58 L82 64" fill="none" {s(T2)}/>
<ellipse cx="34" cy="71" rx="17" ry="15" fill="#FFAE5C" {s()}/>
<rect x="20" y="62" width="13" height="9" rx="3" fill="{O}"/><rect x="36" y="62" width="13" height="9" rx="3" fill="{O}"/><path d="M33 65 H36" stroke="{O}" stroke-width="2.4"/>
<path d="M28 79 Q34 84 41 79" fill="none" {s(T2)}/>
</g>
''', 40, 30)
SUBJ["utka-boss-leskova"] = ("оранжевый гребенчатый тритон в чёрных очках",
                             "развалился на красно-белом надувном матрасе посреди бассейна, вид сверху — сразу видно, кто тут босс")

# 11. «Лотос» (Ставропольская ул.) — родители в воде вместе с ребёнком
ICONS["lotos-stavropolskaya"] = W("#D4F5DC", "#23805A", f'''
<ellipse cx="64" cy="104" rx="56" ry="13" fill="#7BD3E8" {s()}/>
<path d="M30 104 Q40 99 50 104 M80 108 Q90 103 100 108" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<path d="M64 98 Q20 96 10 56 Q40 56 64 98Z" fill="#FF8FB5" {s()}/>
<path d="M64 98 Q108 96 118 56 Q88 56 64 98Z" fill="#FF8FB5" {s()}/>
<path d="M64 100 Q30 78 36 34 Q62 50 64 100Z" fill="#FFB3CC" {s()}/>
<path d="M64 100 Q98 78 92 34 Q66 50 64 100Z" fill="#FFB3CC" {s()}/>
<path d="M50 40 Q58 66 54 70 Q40 62 50 40Z" fill="#fff" opacity=".0"/>
<path d="M54 22 Q76 52 54 66 Q32 52 54 22Z" fill="#49B4F0" {s()}/>
{eye(48, 48, .9)}{eye(60, 48, .9)}<path d="M50 56 Q54 60 58 56" fill="none" {s('stroke-width="2.2"')}/>
<path d="M82 46 Q95 64 82 72 Q69 64 82 46Z" fill="#8FD6FF" {s()}/>
{eye(78, 62, .7)}{eye(86, 62, .7)}
<path d="M64 102 Q44 92 44 74 Q64 80 64 102Z M64 102 Q84 92 84 74 Q64 80 64 102Z" fill="#FFD0DF" {s()}/>
''', 50, 15)
SUBJ["lotos-stavropolskaya"] = ("розовый цветок лотоса на зелёном пруду",
                                "в его лепестках, как в тёплой чаше, сидят рядышком большая капля-мама и маленькая капля-малыш")

# 12. «Плыви с Алисой» (Гончарная наб.) — Белый Кролик с часами
ICONS["plyvi-s-alisoy-goncharnaya"] = W("#EEF1FF", "#6F7FEA", f'''
<path d="M40 44 Q26 4 40 2 Q52 6 52 42Z" fill="#fff" {s()}/><path d="M42 36 Q36 14 41 10 Q46 16 46 36Z" fill="#FFB3CC"/>
<path d="M62 42 Q70 2 84 6 Q92 14 74 46Z" fill="#fff" {s()}/><path d="M68 38 Q74 16 81 13 Q82 22 73 40Z" fill="#FFB3CC"/>
<ellipse cx="56" cy="62" rx="30" ry="25" fill="#fff" {s()}/>
{eye(44, 58, 1.05)}{eye(66, 58, 1.05)}
<path d="M52 66 L58 66 L55 70Z" fill="#FF7FA8" {s('stroke-width="1.8"')}/>
<path d="M50 74 Q55 78 60 74" fill="none" {s(T2)}/>
<ellipse cx="36" cy="68" rx="4.5" ry="2.8" fill="#FF7FA8" opacity=".6"/><ellipse cx="74" cy="68" rx="4.5" ry="2.8" fill="#FF7FA8" opacity=".6"/>
<path d="M80 78 Q92 70 98 54" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M80 78 Q92 70 98 54" fill="none" stroke="#fff" stroke-width="4.4" stroke-linecap="round"/>
<path d="M98 30 V40" stroke="{O}" stroke-width="3"/><circle cx="98" cy="26" r="4" fill="none" {s(T2)}/>
<circle cx="100" cy="50" r="15" fill="#FFD23F" {s()}/><circle cx="100" cy="50" r="10" fill="#fff" {s(T2)}/>
<path d="M100 44 V50 L105 53" fill="none" {s(T2)}/>
<path d="M-6 84 Q8 76 22 84 T50 84 T78 84 T106 84 T134 84 V134 H-6Z" fill="#35C6D6" {s('stroke-width="2.6"')}/>
<path d="M14 102 Q26 97 38 102 M72 110 Q84 105 96 110" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
''', 30, 20)
SUBJ["plyvi-s-alisoy-goncharnaya"] = ("Белый Кролик с розовыми ушами и золотыми карманными часами",
                                      "плывёт по шею в воде и держит часы высоко над волной — боится опоздать на свой заплыв")

# 13. «Плыви с Алисой» (ул. Столетова) — Чеширский кот в круге
ICONS["plyvi-s-alisoy-stoletova"] = W("#C3A8FA", "#3F2386", f'''
{sparkle(22, 24, 5, "#FFE27A")}{sparkle(108, 36, 4, "#FFE27A")}{sparkle(92, 14, 3, "#FFE27A")}
<path d="M30 40 L26 12 L50 28Z M98 40 L102 12 L78 28Z" fill="#D65BD0" {s()}/>
<ellipse cx="64" cy="54" rx="38" ry="30" fill="#E77FE0" {s()}/>
<path d="M46 26 L50 38 M64 23 V36 M82 26 L78 38" stroke="#9A2FA0" stroke-width="5" stroke-linecap="round"/>
<ellipse cx="48" cy="48" rx="8" ry="9" fill="#F7F48B" {s(T2)}/><ellipse cx="80" cy="48" rx="8" ry="9" fill="#F7F48B" {s(T2)}/>
<ellipse cx="48" cy="48" rx="2.6" ry="7" fill="{O}"/><ellipse cx="80" cy="48" rx="2.6" ry="7" fill="{O}"/>
<path d="M34 60 Q64 92 94 60 Q64 72 34 60Z" fill="#fff" {s()}/>
<path d="M46 65 V72 M55 68 V77 M64 69 V79 M73 68 V77 M82 65 V72" stroke="{O}" stroke-width="2"/>
<path d="M-6 96 H134 V134 H-6Z" fill="#2CB7C9"/>
<ellipse cx="64" cy="98" rx="50" ry="17" fill="#FF8FB5" {s()}/>
<path d="M22 92 Q30 86 40 84 M88 84 Q98 86 106 92" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round"/>
<path d="M30 97 Q64 82 98 97" fill="none" {s('stroke-width="2.8"')}/>
<path d="M-6 108 Q8 102 22 108 T50 108 T78 108 T106 108 T134 108 V134 H-6Z" fill="#2CB7C9" {s('stroke-width="2.6"')}/>
''', 50, 15)
SUBJ["plyvi-s-alisoy-stoletova"] = ("сиреневый Чеширский кот в полоску с улыбкой во всю морду",
                                    "сидит ночью в розовом надувном круге, и кажется, что над водой плывёт одна довольная улыбка")

# 14. Magic Swim (Тушинская ул.) — пловец из шляпы фокусника
ICONS["magic-swim-tushinskaya"] = W("#FFE1DC", "#D8433C", f'''
<path d="M26 70 L34 122 Q64 132 94 122 L102 70Z" fill="#2B2540" {s()}/>
<path d="M30 96 Q64 106 98 96 L96 108 Q64 118 32 108Z" fill="#8E5BE8"/>
<ellipse cx="64" cy="70" rx="56" ry="13" fill="#2B2540" {s()}/>
<ellipse cx="64" cy="68" rx="37" ry="8" fill="#4CC3F0" {s(T2)}/>
<path d="M22 44 Q14 34 20 26 M106 44 Q114 34 108 26" fill="none" stroke="#4CC3F0" stroke-width="6" stroke-linecap="round"/>
<path d="M36 68 Q28 40 22 44 M92 68 Q100 40 106 44" fill="none" stroke="{O}" stroke-width="12" stroke-linecap="round"/>
<path d="M36 68 Q28 40 22 44 M92 68 Q100 40 106 44" fill="none" stroke="#FFD2B0" stroke-width="6.5" stroke-linecap="round"/>
<circle cx="64" cy="44" r="24" fill="#FFD2B0" {s()}/>
<path d="M40 42 Q42 16 64 16 Q86 16 88 42 Q64 30 40 42Z" fill="#FFD23F" {s()}/>
<rect x="44" y="38" width="17" height="12" rx="5" fill="#BEEBFF" {s(T2)}/><rect x="67" y="38" width="17" height="12" rx="5" fill="#BEEBFF" {s(T2)}/>
<path d="M61 43 H67" stroke="{O}" stroke-width="2.6"/><circle cx="52" cy="44" r="2.4" fill="{O}"/><circle cx="76" cy="44" r="2.4" fill="{O}"/>
<path d="M56 56 Q64 63 72 56" fill="none" {s(T2)}/>
{sparkle(108, 14, 7, "#FFE27A")}{sparkle(16, 12, 5, "#FFE27A")}{sparkle(116, 60, 4, "#fff")}
''', 50, 10)
SUBJ["magic-swim-tushinskaya"] = ("чёрный цилиндр фокусника, до краёв налитый водой",
                                  "вместо кролика из шляпы выныривает пловец в жёлтой шапочке и очках и вскидывает руки — фокус удался")

# 16. «Ква-Ква-Пузики» (Пушкино) — нырок вниз головой
ICONS["kva-kva-puziki-pushkino"] = W("#D5F7F2", "#177787", f'''
<ellipse cx="64" cy="92" rx="58" ry="22" fill="none" stroke="#fff" stroke-width="3" opacity=".55"/>
<ellipse cx="64" cy="92" rx="40" ry="14" fill="none" stroke="#fff" stroke-width="3.4" opacity=".8"/>
<path d="M52 92 Q46 60 34 50" fill="none" stroke="{O}" stroke-width="17" stroke-linecap="round"/>
<path d="M52 92 Q46 60 34 50" fill="none" stroke="#6CCB3F" stroke-width="11" stroke-linecap="round"/>
<path d="M76 92 Q82 60 94 50" fill="none" stroke="{O}" stroke-width="17" stroke-linecap="round"/>
<path d="M76 92 Q82 60 94 50" fill="none" stroke="#6CCB3F" stroke-width="11" stroke-linecap="round"/>
<path d="M36 52 L6 44 L16 30 L26 38 L24 16 L40 22 L40 36 L54 22 L60 36Z" fill="#8BDB55" {s()}/>
<path d="M92 52 L122 44 L112 30 L102 38 L104 16 L88 22 L88 36 L74 22 L68 36Z" fill="#8BDB55" {s()}/>
<ellipse cx="64" cy="92" rx="22" ry="7" fill="#BFF3FF" {s(T2)}/>
<path d="M30 78 Q28 70 32 66 M98 78 Q100 70 96 66 M64 72 V62" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
{bub(22, 106, 4)}{bub(104, 110, 5)}
''', 50, 20)
SUBJ["kva-kva-puziki-pushkino"] = ("две зелёные перепончатые лапки, торчащие из воды вверх тормашками",
                                   "лягушонок только что нырнул с головой — над водой остались растопыренные пятки и расходятся круги")

# 17. «Аквапупс» (ЗИЛ, б-р Братьев Весниных) — грузовичок с бассейном в кузове
ICONS["akvapups-zil"] = W("#F6F7FB", "#9DABC6", f'''
<path d="M-6 104 H134 V134 H-6Z" fill="#6E7A93"/>
<path d="M4 116 H22 M40 116 H58 M76 116 H94 M112 116 H130" stroke="#fff" stroke-width="3.4" stroke-linecap="round" opacity=".8"/>
<circle cx="64" cy="38" r="13" fill="#FFD2B0" {s()}/>
<path d="M51 36 Q52 22 64 22 Q76 22 77 36 Q64 30 51 36Z" fill="#FFD23F" {s(T2)}/>
{eye(59, 40, .75)}{eye(69, 40, .75)}<path d="M60 46 Q64 49 68 46" fill="none" {s('stroke-width="2"')}/>
<path d="M46 56 Q40 44 44 40 M82 56 Q88 44 84 40" fill="none" stroke="{O}" stroke-width="8" stroke-linecap="round"/>
<path d="M46 56 Q40 44 44 40 M82 56 Q88 44 84 40" fill="none" stroke="#FFD2B0" stroke-width="4" stroke-linecap="round"/>
<path d="M30 52 Q40 46 50 52 T70 52 T90 52 V70 H30Z" fill="#4CC3F0" {s(T2)}/>
<path d="M26 56 H94 V94 H26Z" fill="#3E63D8" {s()}/>
<path d="M36 64 V88 M50 64 V88 M64 64 V88 M78 64 V88" stroke="#2A479E" stroke-width="3" stroke-linecap="round"/>
<path d="M94 62 H112 Q124 64 126 80 V94 H94Z" fill="#5C82F2" {s()}/>
<path d="M100 68 H110 Q118 70 119 80 H100Z" fill="#DFF3FF" {s(T2)}/>
<rect x="18" y="90" width="110" height="9" rx="4" fill="#2B2540" {s(T2)}/>
<circle cx="44" cy="102" r="12" fill="#2B2540" {s()}/><circle cx="44" cy="102" r="4.5" fill="#DDE3EE"/>
<circle cx="104" cy="102" r="12" fill="#2B2540" {s()}/><circle cx="104" cy="102" r="4.5" fill="#DDE3EE"/>
<path d="M16 48 Q19 54 16 57 Q13 54 16 48Z M104 40 Q107 46 104 49 Q101 46 104 40Z" fill="#4CC3F0" {s('stroke-width="1.8"')}/>
''', 30, 20)
SUBJ["akvapups-zil"] = ("синий грузовичок с кузовом, до бортов налитым морской водой",
                        "едет по улице у бывшего автозавода, а в кузове, как в бассейне, плещется пупс в жёлтой шапочке")

if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for i in ids:
        open(os.path.join(OUT, i + ".svg"), "w", encoding="utf-8").write(ICONS[i])
    print("svg:", len(ids))
