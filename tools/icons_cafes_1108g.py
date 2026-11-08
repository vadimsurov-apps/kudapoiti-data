"""Иконки робота cafes, 2026-11-08 (19–21 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая придумана и нарисована
отдельно (свой герой по кухне/названию, своя сцена, своя компоновка и палитра фона). Сверено со всеми листами
icons-catalog и icons-src/subjects.txt. Запуск: python3 tools/icons_cafes_1108g.py [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "g_coffeetree": ("#F1FFE9", "#7FBF7A"),
    "g_stage": ("#3A2A5E", "#1E1636"),
    "g_whitesea": ("#EAF7FF", "#7FB4E0"),
    "g_toybox": ("#F7EEFF", "#B79BE8"),
    "g_broth": ("#E4FFFA", "#59C2B5"),
    "g_welcome": ("#FFF1E6", "#E59466"),
    "g_arbat": ("#FFF6DC", "#D9B36A"),
    "g_playground": ("#FFF0E8", "#FF9F80"),
    "g_figtree": ("#FFFBE5", "#C8D66A"),
    "g_mammamia": ("#FFF3F0", "#F2797A"),
    "g_oatfield": ("#FFFDE8", "#E9C46A"),
    "g_skyhimki": ("#E8F4FF", "#6FA8EA"),
    "g_board": ("#FFF5E1", "#F0A84B"),
    "g_naples": ("#FFE9F2", "#C98BD8"),
    "g_meadow": ("#F2FFF0", "#8FD08C"),
})

# 1. Натура — кофейная ветка с ягодами-вишнями кофе
ICONS["cafe-natura-zvenigorodskaya"] = svg("g_coffeetree", f'''
<path d="M6 30 Q60 40 122 100" fill="none" stroke="#7A5232" stroke-width="7" stroke-linecap="round"/>
<path d="M6 30 Q60 40 122 100" fill="none" {W(2.4)}/>
<path d="M30 34 Q18 8 44 6 Q50 26 30 34Z" fill="#3E9B57" {s()}/><path d="M30 34 Q36 18 44 6" fill="none" stroke="#2F7A44" stroke-width="2"/>
<path d="M92 72 Q118 56 124 78 Q106 90 92 72Z" fill="#3E9B57" {s()}/><path d="M92 72 Q108 70 124 78" fill="none" stroke="#2F7A44" stroke-width="2"/>
<path d="M70 52 Q66 26 88 22 Q94 42 70 52Z" fill="#4FB067" {s()}/>
<circle cx="52" cy="72" r="24" fill="#E0323A" {s()}/>
<ellipse cx="44" cy="62" rx="7" ry="4" fill="#fff" opacity=".45"/>
<path d="M50 48 q2 -6 6 -6" fill="none" {W(2.4)}/>
{face(52, 74, d=8, k=0.9)}
<circle cx="84" cy="88" r="13" fill="#F04A4E" {s()}/>{face(84, 89, d=4.5, k=0.55)}
<circle cx="26" cy="96" r="11" fill="#C8242C" {s()}/>{face(26, 97, d=4, k=0.5, mouth=False)}
{sparkle(104, 30, 5)}
''')
SUBJ["cafe-natura-zvenigorodskaya"] = ("ярко-красная ягода-вишня кофейного дерева с двумя сестричками поменьше",
                                       "висят гроздью на ветке кофейного дерева среди глянцевых листьев")

# 2. Natahtari Grand Cafe — гурийский хачапури кланяется на большой сцене
ICONS["cafe-natahtari-grand-khoroshevskoe"] = svg("g_stage", f'''
<path d="M40 -4 L88 -4 L120 112 L8 112Z" fill="#FFF4B8" opacity=".28"/>
<path d="M0 0 H30 Q24 60 34 128 H0Z" fill="#C8243A" {s()}/><path d="M128 0 H98 Q104 60 94 128 H128Z" fill="#C8243A" {s()}/>
<path d="M10 0 Q8 60 16 128 M118 0 Q120 60 112 128" stroke="#9A1A2C" stroke-width="3" fill="none"/>
<rect x="0" y="104" width="128" height="30" fill="#8A5A34" {s()}/>
<path d="M28 98 Q30 52 64 46 Q98 52 100 98 Q64 108 28 98Z" fill="#E9A84C" {s()}/>
<path d="M38 92 Q42 62 64 58 Q86 62 90 92" fill="#FFE69A" {W(2.2)}/>
<ellipse cx="54" cy="80" rx="7" ry="5" fill="#fff" {W(1.8)}/><circle cx="54" cy="80" r="3" fill="#FFC21A"/>
<ellipse cx="76" cy="84" rx="6" ry="4.5" fill="#fff" {W(1.8)}/><circle cx="76" cy="84" r="2.6" fill="#FFC21A"/>
{face(64, 68, d=8, k=0.8)}
<path d="M30 86 Q18 80 16 92 M98 86 Q110 80 112 92" fill="none" {W(3)}/>
<path d="M18 114 l6 -8 l4 8z M104 114 l6 -8 l4 8z" fill="#FF7FA8" {W(1.6)}/>
{sparkle(46, 24, 4, "#FFF4B8")}{sparkle(84, 18, 3, "#FFF4B8")}
''')
SUBJ["cafe-natahtari-grand-khoroshevskoe"] = ("хачапури по-гурийски — румяный полумесяц с варёным яйцом внутри",
                                              "раскланивается на большой сцене под лучом прожектора между красными кулисами")

# 3. Мольто Белло (Беломорская) — белая пицца на льдине в Белом море
ICONS["cafe-molto-bello-belomorskaya"] = svg("g_whitesea", f'''
<path d="M86 50 L100 22 L116 50Z" fill="#fff" {s()}/><path d="M100 22 L104 50" stroke="#CDE6F7" stroke-width="3"/>
<rect x="0" y="82" width="128" height="50" fill="#3C86C6"/>
<path d="M0 84 Q16 78 32 84 T64 84 T96 84 T128 84" fill="none" stroke="#fff" stroke-width="3"/>
<path d="M14 92 L28 80 H104 L116 94 L100 104 H26Z" fill="#F4FBFF" {s()}/>
<ellipse cx="64" cy="70" rx="40" ry="16" fill="#F2C27A" {s()}/>
<ellipse cx="64" cy="67" rx="33" ry="11.5" fill="#FFF8E8" {W(2)}/>
<circle cx="44" cy="66" r="3.4" fill="#2D2A32"/><circle cx="84" cy="64" r="3.4" fill="#2D2A32"/><circle cx="72" cy="72" r="3" fill="#2D2A32"/>
<path d="M52 60 l5 3 M58 58 l2 5 M78 74 l6 -2" stroke="#4E9B3C" stroke-width="2.4" stroke-linecap="round"/>
{face(64, 64, d=7, k=0.75)}
<path d="M36 76 Q64 90 92 76 L94 84 Q64 96 34 84Z" fill="#E8434E" {W(2.2)}/>
<path d="M88 82 L96 98 L102 94 L94 80" fill="#E8434E" {W(2.2)}/>
{sparkle(24, 30, 5)}{sparkle(60, 22, 3)}
''')
SUBJ["cafe-molto-bello-belomorskaya"] = ("белая пицца «бьянка» со сливочным соусом, маслинами и розмарином, в красном шарфе",
                                         "дрейфует на льдине по холодному Белому морю мимо маленького айсберга")

# 4. Molinari — заводной пончик шагает по столу
ICONS["cafe-molinari-altufevskoe"] = svg("g_toybox", f'''
<rect x="0" y="100" width="128" height="30" fill="#E8D3B0"/><path d="M0 100 H128" {W(2.4)}/>
<path d="M44 92 l-6 10 h10 M78 92 l6 10 h-10" fill="none" {W(3.4)}/>
<circle cx="64" cy="62" r="34" fill="#E3A35A" {s()}/>
<path d="M32 54 Q36 30 64 28 Q94 30 96 56 Q90 62 84 56 Q78 66 70 58 Q62 66 54 58 Q46 66 40 58 Q36 62 32 54Z" fill="#F57FB0" {W(2.2)}/>
<circle cx="64" cy="62" r="9" fill="#C9B3EE" {s()}/>
<path d="M46 40 l3 2 M58 34 l1 4 M76 36 l-2 3 M86 46 l-3 1" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<path d="M50 40 l2 -3 M70 42 l3 1" stroke="#7BD3F7" stroke-width="2.6" stroke-linecap="round"/>
{face(64, 82, d=9, k=0.8)}
<rect x="96" y="58" width="12" height="6" fill="#E9C04A" {W(2)}/>
<path d="M108 50 Q120 50 120 61 Q120 72 108 72 Q114 61 108 50Z" fill="#E9C04A" {W(2)}/>
<path d="M14 70 h12 M10 80 h14 M16 90 h10" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".9"/>
''')
SUBJ["cafe-molinari-altufevskoe"] = ("заводной пончик в розовой глазури с латунным ключиком в боку",
                                     "бодро шагает по столу на игрушечных ножках, ключик крутится")

# 5. Mom&me — пельмешек в ушанке гребёт ложкой в миске бульона
ICONS["cafe-momme-leninsky"] = svg("g_broth", f'''
<path d="M0 104 Q32 96 64 104 T128 104 V130 H0Z" fill="#7FD6E8" opacity=".7"/>
<path d="M14 72 H114 Q110 112 64 114 Q18 112 14 72Z" fill="#fff" {s()}/>
<path d="M22 92 Q64 104 106 92" fill="none" stroke="#5BB5E0" stroke-width="3"/>
<ellipse cx="64" cy="72" rx="50" ry="9" fill="#F7D98A" {s()}/>
<path d="M34 70 Q30 40 64 36 Q98 40 94 70 Q64 78 34 70Z" fill="#FFF6E4" {s()}/>
<path d="M38 64 q4 -6 8 0 q4 -6 8 0 q4 -6 8 0 q4 -6 8 0 q4 -6 8 0 q4 -6 8 0 q4 -6 8 0" fill="none" {W(2)}/>
<path d="M42 38 Q44 18 64 16 Q84 18 86 38Z" fill="#6E4A8E" {s()}/>
<path d="M40 36 H88 V42 H40Z" fill="#B99A7A" {W(2)}/>
<path d="M42 40 Q34 50 38 56 L44 52 Q42 46 46 42Z M86 40 Q94 50 90 56 L84 52 Q86 46 82 42Z" fill="#B99A7A" {W(2)}/>
{face(64, 52, d=8, k=0.8)}
<path d="M92 50 L114 94" stroke="{O}" stroke-width="6" stroke-linecap="round"/><path d="M92 50 L114 94" stroke="#D9DDE6" stroke-width="3" stroke-linecap="round"/>
<ellipse cx="116" cy="98" rx="6" ry="9" transform="rotate(-25 116 98)" fill="#D9DDE6" {W(2.2)}/>
<circle cx="24" cy="26" r="3" fill="#fff" opacity=".8"/><circle cx="104" cy="22" r="2.4" fill="#fff" opacity=".8"/>
''')
SUBJ["cafe-momme-leninsky"] = ("пельмешек-малыш в фиолетовой шапке-ушанке",
                               "гребёт ложкой-веслом, сидя в мисочке с бульоном, как в лодочке")

# 6. Шемоди — рулон пастилы-тклапи раскатывается ковровой дорожкой «заходите!»
ICONS["cafe-shemodi-kulikovskaya"] = svg("g_welcome", f'''
<path d="M0 34 H128 V40 H0Z" fill="#fff" opacity=".35"/>
<path d="M50 84 L128 126 L128 132 L36 132 L26 96Z" fill="#B3263E" {s()}/>
<path d="M46 98 L112 132 M38 108 L84 132" stroke="#E8536B" stroke-width="2.4"/>
<circle cx="38" cy="78" r="26" fill="#C42F48" {s()}/>
<path d="M38 78 m-16 0 a16 16 0 1 0 32 0 a12 12 0 1 0 -24 0 a8 8 0 1 0 16 0" fill="none" stroke="#7E1A2C" stroke-width="2.4"/>
{face(40, 66, d=7, k=0.75)}
<path d="M62 70 Q74 56 80 62" fill="none" {W(3)}/>
<path d="M80 62 l6 -6 M80 62 l8 -1" {W(2.6)}/>
<path d="M96 40 Q104 30 112 40 Q104 52 96 40Z" fill="#FFD166" {W(2)}/>
{sparkle(104, 74, 5)}{sparkle(20, 24, 4)}
''')
SUBJ["cafe-shemodi-kulikovskaya"] = ("рулон грузинской фруктовой пастилы тклапи вишнёвого цвета",
                                     "раскатывается красной ковровой дорожкой и машет рукой: «заходите!»")

# 7. Баба Марта (Арбат) — баница-спираль с мартеницей у арбатского фонаря
ICONS["cafe-baba-marta-arbat"] = svg("g_arbat", f'''
<rect x="0" y="100" width="128" height="30" fill="#B9A58A"/>
<path d="M0 100 H128 M0 112 H128 M20 100 V112 M50 100 V112 M80 100 V112 M110 100 V112 M8 112 V128 M36 112 V128 M66 112 V128 M96 112 V128" stroke="#8E7B62" stroke-width="2"/>
<path d="M102 100 V30" stroke="{O}" stroke-width="6"/><path d="M102 100 V30" stroke="#4A4E5A" stroke-width="3"/>
<path d="M92 30 H112 L108 14 H96Z" fill="#FFE59A" {s()}/><path d="M94 12 H110" {W(3)}/>
<circle cx="52" cy="72" r="32" fill="#E9AE55" {s()}/>
<path d="M52 72 m-6 0 a6 6 0 1 1 12 0 a12 12 0 1 1 -24 0 a18 18 0 1 1 36 0 a24 24 0 1 1 -48 0" fill="none" stroke="#B9782E" stroke-width="2.6"/>
{face(52, 70, d=8, k=0.85)}
<path d="M26 46 Q20 54 22 64" fill="none" stroke="#fff" stroke-width="4"/>
<path d="M26 46 Q20 54 22 64" fill="none" stroke="#E23A3A" stroke-width="4" stroke-dasharray="5 5"/>
<circle cx="22" cy="68" r="5" fill="#E23A3A" {W(1.8)}/><circle cx="31" cy="66" r="5" fill="#fff" {W(1.8)}/>
<path d="M22 73 v8 M31 71 v8" stroke="#E23A3A" stroke-width="2.6"/><path d="M33 71 v8" stroke="#fff" stroke-width="2.6"/>
''')
SUBJ["cafe-baba-marta-arbat"] = ("болгарская баница — золотая слоёная спираль с красно-белой мартеницей",
                                 "стоит на брусчатке Старого Арбата у чугунного фонаря")

# 8. Ути-пути — карапуз в слюнявчике съезжает с горки с ложкой
ICONS["cafe-uti-puti-bakuninskaya"] = svg("g_playground", f'''
<rect x="0" y="108" width="128" height="22" fill="#9ED37A"/>
<path d="M98 26 V110 M118 26 V110" stroke="{O}" stroke-width="5"/><path d="M98 26 V110 M118 26 V110" stroke="#5B9BE0" stroke-width="2.4"/>
<path d="M98 44 H118 M98 62 H118 M98 80 H118" {W(3)}/>
<path d="M98 34 Q60 44 30 104 L46 108 Q70 62 100 52Z" fill="#FFC93C" {s()}/>
<circle cx="66" cy="50" r="17" fill="#FFD9B8" {s()}/>
<path d="M54 40 Q58 30 66 34 Q68 28 74 34" fill="none" {W(2.6)}/>
{face(66, 51, d=6, k=0.7)}
<path d="M54 64 Q66 76 78 64 L76 74 Q66 82 56 74Z" fill="#fff" {W(2)}/>
<circle cx="62" cy="71" r="1.8" fill="#FF7FA8"/><circle cx="70" cy="71" r="1.8" fill="#7BD3F7"/>
<path d="M60 76 Q50 92 44 94 M72 76 Q80 88 76 96" fill="none" stroke="#7BC9F2" stroke-width="9" stroke-linecap="round"/>
<path d="M50 52 L32 30" stroke="{O}" stroke-width="5" stroke-linecap="round"/><path d="M50 52 L32 30" stroke="#E6E9EF" stroke-width="2.4" stroke-linecap="round"/>
<ellipse cx="30" cy="26" rx="6" ry="8" transform="rotate(-40 30 26)" fill="#E6E9EF" {W(2.2)}/>
<circle cx="30" cy="25" r="3" fill="#F3D36B"/>
{sparkle(16, 60, 4)}
''')
SUBJ["cafe-uti-puti-bakuninskaya"] = ("карапуз в белом слюнявчике с ложкой каши в поднятой руке",
                                      "с восторгом съезжает с жёлтой горки на детской площадке кафе")

# 9. Райский сад — раскрытый инжир на ветке смоковницы
ICONS["cafe-raysky-sad-balashikha"] = svg("g_figtree", f'''
<circle cx="104" cy="24" r="11" fill="#FFD84A" {W(2.4)}/>
<path d="M0 18 Q50 24 80 12" fill="none" stroke="#7A5232" stroke-width="6" stroke-linecap="round"/>
<path d="M14 22 Q2 40 14 52 Q18 40 28 46 Q30 32 20 30 Q28 20 14 22Z" fill="#6FB24E" {s()}/>
<path d="M66 16 Q82 30 96 26 Q90 40 76 38 Q78 50 66 46 Q60 30 66 16Z" fill="#6FB24E" {s()}/>
<path d="M50 22 V36" {W(3)}/>
<path d="M50 36 Q16 52 22 88 Q30 116 50 116 Q70 116 78 88 Q84 52 50 36Z" fill="#7B3F8C" {s()}/>
<path d="M50 50 Q28 62 32 88 Q38 106 50 106 Q62 106 68 88 Q72 62 50 50Z" fill="#F27A8C" {W(2.2)}/>
<g fill="#FFE5A8">{"".join(f'<circle cx="{x}" cy="{y}" r="1.6"/>' for x, y in [(40,70),(46,64),(56,66),(60,74),(42,86),(58,90),(50,98),(38,96),(62,98),(48,78)])}</g>
{face(50, 80, d=7, k=0.75)}
{sparkle(104, 80, 5)}{sparkle(96, 104, 3)}
''')
SUBJ["cafe-raysky-sad-balashikha"] = ("спелый раскрытый инжир с розовой серединкой в зёрнышках",
                                      "висит на ветке смоковницы с большими резными листьями под южным солнцем")

# 10. Мама Миа — кусок пиццы «Четыре сыра» восклицает «мамма миа!»
ICONS["cafe-mama-mia-balashikha"] = svg("g_mammamia", f'''
<path d="M64 112 L22 30 Q64 12 106 30Z" fill="#F7C95C" {s()}/>
<path d="M22 30 Q64 12 106 30 L102 40 Q64 24 26 40Z" fill="#D9913E" {W(2.4)}/>
<path d="M64 112 L64 30 M44 72 L84 72" stroke="#E3A93A" stroke-width="2"/>
<path d="M34 46 Q48 40 62 42 L62 70 L46 70Z" fill="#FFF1B3"/>
<path d="M66 42 Q82 40 94 46 L82 70 L66 70Z" fill="#FFE07A"/>
<path d="M46 74 L62 74 L62 102Z" fill="#FFF8DC"/><path d="M66 74 L82 74 L66 102Z" fill="#F2D27A"/>
<circle cx="76" cy="52" r="3" fill="#E7B748"/><circle cx="52" cy="84" r="2.4" fill="#EAD9A8"/>
<path d="M88 40 q0 8 3 12" stroke="#5FA0D8" stroke-width="2.4"/>
{face(64, 58, d=8, k=0.85)}
<path d="M58 66 Q64 74 70 66 Q64 70 58 66Z" fill="#B53B4A"/>
<path d="M16 64 Q8 52 14 44 L20 46 Q16 54 22 62Z" fill="#FFD9B8" {W(2.2)}/>
<path d="M14 44 l1 -6 l4 1 l-1 6z" fill="#FFD9B8" {W(2)}/>
<path d="M112 64 Q120 52 114 44 L108 46 Q112 54 106 62Z" fill="#FFD9B8" {W(2.2)}/>
<path d="M114 44 l-1 -6 l-4 1 l1 6z" fill="#FFD9B8" {W(2)}/>
<path d="M24 64 Q20 64 16 64 M104 64 Q108 64 112 64" fill="none" {W(2.6)}/>
<path d="M100 14 l3 10 M110 18 l-4 8 M90 16 l5 8" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''')
SUBJ["cafe-mama-mia-balashikha"] = ("треугольный кусок пиццы «Четыре сыра» с четырьмя разными сырами",
                                    "в восторге восклицает «мамма миа!», сложив обе руки щепоткой")

# 11. Овсянка — птичка-овсянка на краю миски каши
ICONS["cafe-ovsyanka-balashikha"] = svg("g_oatfield", f'''
<path d="M10 128 Q14 96 8 80 M20 128 Q24 100 22 84 M112 128 Q110 98 118 82" fill="none" stroke="#C99A3A" stroke-width="3"/>
<ellipse cx="8" cy="78" rx="3" ry="6" fill="#E9C46A" {W(1.6)}/><ellipse cx="22" cy="82" rx="3" ry="6" fill="#E9C46A" {W(1.6)}/><ellipse cx="118" cy="80" rx="3" ry="6" fill="#E9C46A" {W(1.6)}/>
<path d="M22 82 H106 Q102 118 64 118 Q26 118 22 82Z" fill="#5FA8D8" {s()}/>
<path d="M30 96 Q64 104 98 96" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="2 6" stroke-linecap="round"/>
<ellipse cx="64" cy="82" rx="42" ry="9" fill="#F5E3C0" {s()}/>
<ellipse cx="50" cy="80" rx="4" ry="2.6" fill="#E8C98E"/><ellipse cx="78" cy="82" rx="4" ry="2.6" fill="#E8C98E"/><circle cx="64" cy="79" r="3" fill="#C2185B"/>
<path d="M58 70 Q48 70 40 60 L52 58Z" fill="#8A6A3A" {W(2.2)}/>
<ellipse cx="72" cy="56" rx="22" ry="17" fill="#F7D33C" {s()}/>
<path d="M60 56 Q72 48 86 60 Q74 68 60 56Z" fill="#B8862E" {W(2)}/>
<circle cx="88" cy="38" r="13" fill="#F7D33C" {s()}/>
<path d="M82 30 Q90 26 96 32" fill="none" stroke="#B8862E" stroke-width="2.4"/>
{eye(91, 38, 0.8)}
<ellipse cx="94" cy="44" rx="3" ry="1.8" fill="#FF7FA8" opacity=".6"/>
<path d="M100 38 L110 41 L100 44Z" fill="#E9963A" {W(2)}/>
<ellipse cx="114" cy="42" rx="4" ry="2.6" fill="#F5E3C0" {W(1.6)}/>
<path d="M66 72 v8 M76 72 v8" {W(2.4)}/>
''')
SUBJ["cafe-ovsyanka-balashikha"] = ("жёлтая птичка-овсянка с коричневыми крылышками",
                                    "сидит на краю синей миски с кашей и держит в клюве овсяную хлопушку")

# 12. Хмели Летели — хачапури-полумесяц летит бумерангом над облаками
ICONS["cafe-khmeli-leteli-khimki"] = svg("g_skyhimki", f'''
<path d="M8 100 Q18 88 32 96 Q42 86 54 98 Q60 110 46 112 H14 Q2 110 8 100Z" fill="#fff" {s()}/>
<path d="M84 116 Q92 106 104 112 Q114 106 120 116 Z" fill="#fff" {s()}/>
<path d="M22 78 Q14 36 52 22 Q90 12 112 40 Q96 38 80 46 Q60 56 52 82 Q36 92 22 78Z" fill="#D98A35" {s()}/>
<path d="M32 72 Q28 44 56 34 Q84 26 100 40 Q84 42 70 50 Q56 60 50 76 Q40 82 32 72Z" fill="#FFF2C6" {W(2.2)}/>
<path d="M40 64 q4 -4 8 0 M52 46 q4 -4 8 0 M70 38 q4 -4 8 0" fill="none" stroke="#E8C77A" stroke-width="2"/>
<circle cx="86" cy="40" r="2" fill="#7A4A1E"/><circle cx="30" cy="56" r="2" fill="#7A4A1E"/><circle cx="96" cy="32" r="2" fill="#7A4A1E"/>
{face(56, 56, d=7, k=0.75)}
<path d="M16 86 Q2 80 4 66 M26 94 Q10 98 2 86" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" opacity=".9"/>
{sparkle(108, 70, 5)}{sparkle(20, 20, 4)}
''')
SUBJ["cafe-khmeli-leteli-khimki"] = ("румяный хачапури-полумесяц с открытой сырной начинкой, изогнутый как бумеранг",
                                     "со свистом пролетает над облаками Химок, оставляя завитки ветра")

# 13. Оджахури — картофельная долька делает колесо на деревянной доске
ICONS["cafe-odzhakhuri-khimki"] = svg("g_board", f'''
<rect x="8" y="98" width="112" height="16" rx="8" fill="#C98B4E" {s()}/>
<path d="M20 104 H60 M70 108 H108" stroke="#A86E36" stroke-width="2"/>
<circle cx="120" cy="106" r="4" fill="#FFF5E1" {W(2)}/>
<g transform="rotate(-28 62 58)">
<path d="M28 66 Q28 30 62 26 Q96 30 96 66 Z" fill="#F4C445" {s()}/>
<path d="M28 66 H96" {W(3)}/>
<path d="M30 64 Q30 34 62 30" fill="none" stroke="#C97F24" stroke-width="5"/>
{face(64, 50, d=8, k=0.8)}
<path d="M54 26 q-2 -10 4 -12 M62 25 q0 -12 6 -12 M70 27 q4 -10 10 -8" fill="none" stroke="#3E9B57" stroke-width="3" stroke-linecap="round"/>
</g>
<path d="M30 84 L22 96 M88 72 L100 66" fill="none" {W(3.4)}/>
<path d="M14 40 Q10 56 18 66 M110 30 Q120 44 116 56" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''')
SUBJ["cafe-odzhakhuri-khimki"] = ("золотистая жареная картофельная долька с чубчиком из укропа",
                                  "делает колесо на деревянной доске для подачи, разбрасывая ручки и ножки")

# 14. Пульчинелла — неаполитанский пончик дзепполе сидит на Везувии
ICONS["cafe-pulcinella-khimki"] = svg("g_naples", f'''
<path d="M70 4 Q60 12 66 20 Q56 24 64 32" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".85"/>
<path d="M0 128 L54 40 H82 L128 128Z" fill="#8C6A8E" {s()}/>
<path d="M54 40 Q68 48 82 40" fill="#6B4C6E" {W(2)}/>
<path d="M0 116 Q30 108 60 118 T128 112 V130 H0Z" fill="#7FC7E8" {W(2)}/>
<ellipse cx="66" cy="62" rx="32" ry="14" fill="#E8A247" {s()}/>
<ellipse cx="66" cy="56" rx="26" ry="10" fill="#F2BC5E" {W(2)}/>
<path d="M48 54 Q52 42 60 50 Q64 38 72 50 Q78 40 84 54 Q66 62 48 54Z" fill="#FFF3D1" {W(2)}/>
<circle cx="66" cy="44" r="5" fill="#B5163A" {W(2)}/><path d="M66 39 q3 -6 8 -6" fill="none" {W(2)}/>
<circle cx="58" cy="52" r="1.4" fill="#fff"/><circle cx="76" cy="54" r="1.4" fill="#fff"/>
{face(66, 66, d=8, k=0.75)}
<path d="M48 72 L42 92 M84 72 L90 92" fill="none" stroke="#E8A247" stroke-width="7" stroke-linecap="round"/>
<path d="M48 72 L42 92 M84 72 L90 92" fill="none" {W(2)}/>
{sparkle(22, 30, 5)}{sparkle(108, 22, 4)}
''')
SUBJ["cafe-pulcinella-khimki"] = ("неаполитанский пончик дзепполе с кремовой розочкой и вишенкой-амареной",
                                  "сидит на краю кратера Везувия, болтая ножками над Неаполитанским заливом")

# 15. Корги — кекс-бундт в высокой траве Морщихинского поля
ICONS["cafe-korgi-skhodnya"] = svg("g_meadow", f'''
<circle cx="104" cy="24" r="10" fill="#FFE27A" {W(2.2)}/>
<path d="M20 92 Q20 36 64 32 Q108 36 108 92 Z" fill="#E08A3A" {s()}/>
<path d="M40 92 V52 M56 92 V40 M72 92 V40 M88 92 V52" stroke="#B8682A" stroke-width="2.4"/>
<ellipse cx="64" cy="38" rx="12" ry="5" fill="#B7E3A8" {W(2.2)}/>
<path d="M24 58 Q30 40 64 36 Q98 40 104 58 Q100 66 96 58 Q94 72 88 60 Q82 70 78 58 Q72 74 66 60 Q60 72 54 58 Q48 70 44 58 Q38 68 34 58 Q28 66 24 58Z" fill="#FFF6E6" {W(2.2)}/>
{face(64, 74, d=9, k=0.85)}
<g fill="#5DB65A" stroke="{O}" stroke-width="2.2" stroke-linejoin="round">
<path d="M0 128 V96 L6 80 L12 96 L18 78 L24 96 L30 84 L36 98 L42 82 L48 98 L54 88 L60 100 L66 86 L72 100 L78 88 L84 98 L90 80 L96 96 L102 82 L108 96 L114 78 L120 94 L128 80 V128Z"/>
</g>
<path d="M10 112 l3 -8 M34 116 l2 -9 M60 118 l2 -8 M92 116 l2 -9 M116 114 l2 -8" stroke="#3F8F3E" stroke-width="2"/>
''')
SUBJ["cafe-korgi-skhodnya"] = ("рыжий кекс-бундт кольцом с потёками белой сахарной глазури",
                               "выглядывает из высокой травы Морщихинского поля по самые щёки")

# ===== вторая партия (районы Боровское шоссе … Верхние Котлы, Королёв, Мытищи, Люберцы) =====
draw_icons.BG.update({
    "h_pumpkin": ("#FFF4E0", "#F4A259"),
    "h_atelier": ("#F3F7FF", "#9DB4E8"),
    "h_coaster": ("#E9F9FF", "#53B9E6"),
    "h_sirocco": ("#FFF3D9", "#E8B25A"),
    "h_diavola": ("#FFECE8", "#E5584F"),
    "h_airship": ("#EEF4FF", "#8FA8F0"),
    "h_suzani": ("#FFF0F6", "#D9739F"),
    "h_bakery": ("#FFF8EC", "#CFA36A"),
    "h_caspian": ("#E6FCFF", "#38B6C8"),
    "h_bath": ("#F4F1FF", "#A99BE0"),
    "h_gym": ("#ECFFF2", "#62C48A"),
    "h_boot": ("#FFF7E6", "#7FBF7F"),
    "h_adriatic": ("#E2F3FF", "#2E7FC2"),
    "h_fountain": ("#FFF9EF", "#E0A2A2"),
    "h_hawaii": ("#E8FFF7", "#3FC2A0"),
    "h_coals": ("#3B2B2B", "#1F1616"),
    "h_street": ("#FFF6E8", "#E7B98A"),
})

# 16. Пьеро (ЗИЛАРТ) — крем-суп в тыкве-горшочке
ICONS["cafe-piero-zilart"] = svg("h_pumpkin", f'''
<path d="M60 30 Q58 16 70 10" fill="none" stroke="#5E8C3A" stroke-width="6" stroke-linecap="round"/>
<path d="M70 14 Q86 8 92 20 Q80 24 70 14Z" fill="#7DBB4A" {s()}/>
<path d="M14 64 Q10 112 42 116 Q64 122 86 116 Q118 112 114 64Z" fill="#F08A24" {s()}/>
<path d="M40 66 Q34 92 42 116 M64 68 V120 M88 66 Q94 92 86 116" fill="none" stroke="#C9661A" stroke-width="2.6"/>
<ellipse cx="64" cy="64" rx="50" ry="14" fill="#F08A24" {s()}/>
<ellipse cx="64" cy="64" rx="42" ry="10" fill="#FFC857" {W(2.2)}/>
<path d="M44 62 Q54 58 60 64 Q68 70 80 62" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<circle cx="74" cy="60" r="2" fill="#7A5232"/><circle cx="80" cy="66" r="2" fill="#7A5232"/><circle cx="50" cy="66" r="2" fill="#7A5232"/>
{face(64, 92, d=10, k=0.9)}
<path d="M50 40 Q46 30 52 22 M64 42 Q60 30 66 22 M78 40 Q74 30 80 22" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
''')
SUBJ["cafe-piero-zilart"] = ("оранжевая тыква-горшочек, полная тыквенного крем-супа с семечками",
                             "дымится паром, гордо подняв зелёный хвостик-черешок")

# 17. Il Pittore — торт-палитра с кремовыми красками
ICONS["cafe-il-pittore-nakhimovsky"] = svg("h_atelier", f'''
<path d="M12 70 Q8 34 52 26 Q104 18 116 52 Q122 76 98 80 Q86 80 88 92 Q90 110 62 110 Q18 108 12 70Z" fill="#F6E2C0" {s()}/>
<path d="M14 80 Q20 108 62 110 Q90 110 88 92" fill="none" stroke="#C9A66E" stroke-width="2.4"/>
<ellipse cx="74" cy="92" rx="9" ry="7" fill="#9DB4E8" {W(2.2)}/>
<circle cx="36" cy="54" r="8" fill="#F25C78" {W(2.2)}/><circle cx="56" cy="40" r="7" fill="#FFD23F" {W(2.2)}/>
<circle cx="82" cy="40" r="7" fill="#5CC27A" {W(2.2)}/><circle cx="102" cy="56" r="6.5" fill="#6C8CF0" {W(2.2)}/>
<circle cx="34" cy="78" r="6" fill="#B07BE0" {W(2.2)}/>
<path d="M36 46 q2 -6 4 0 M56 33 q2 -6 4 0" fill="#fff" opacity=".7"/>
{face(62, 70, d=9, k=0.85)}
<path d="M100 6 L84 50" stroke="{O}" stroke-width="7" stroke-linecap="round"/><path d="M100 6 L84 50" stroke="#C98B4E" stroke-width="3.6" stroke-linecap="round"/>
<path d="M86 44 L80 58 L88 56Z" fill="#F25C78" {W(2)}/>
{sparkle(20, 24, 4)}
''')
SUBJ["cafe-il-pittore-nakhimovsky"] = ("торт в форме палитры художника с кремовыми каплями-красками",
                                       "в него воткнута кисточка, с которой капает розовый крем")

# 18. Батони («Остров Мечты») — торт Наполеон в позе полководца
ICONS["cafe-batoni-ostrov"] = svg("h_coaster", f'''
<path d="M0 104 Q30 60 58 92 Q84 120 128 70" fill="none" stroke="#F25C78" stroke-width="5"/>
<path d="M14 128 V92 M44 128 V82 M98 128 V90 M120 128 V78" stroke="#7B8BA8" stroke-width="3"/>
<rect x="36" y="44" width="56" height="58" rx="4" fill="#FFF3DC" {s()}/>
<path d="M36 58 H92 M36 72 H92 M36 86 H92" stroke="#E7B062" stroke-width="5"/>
<path d="M36 44 H92 V50 H36Z" fill="#F4E2C4" {W(2)}/>
<g fill="#E7B062">{"".join(f'<circle cx="{x}" cy="{y}" r="1.8"/>' for x, y in [(44,47),(54,46),(66,48),(78,46),(86,47)])}</g>
<path d="M30 46 Q64 22 98 46 Q64 36 30 46Z" fill="#2F3A5C" {s()}/>
<circle cx="64" cy="34" r="4" fill="#E23A3A" {W(1.8)}/>
{face(64, 66, d=9, k=0.85)}
<path d="M92 70 Q104 76 100 90" fill="none" {W(3)}/>
{sparkle(108, 22, 5)}{sparkle(18, 34, 4)}
''')
SUBJ["cafe-batoni-ostrov"] = ("кусок торта «Наполеон» с хрустящей крошкой и треуголкой",
                              "стоит, заложив руку за борт, на фоне розовых американских горок «Острова Мечты»")

# 19. Сирокко — хумус, которого обдувает горячий ветер
ICONS["cafe-sirocco-korolev"] = svg("h_sirocco", f'''
<path d="M4 34 Q30 24 52 34 Q70 42 90 30 M0 50 Q24 44 40 50 M84 46 Q104 40 124 48" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".9"/>
<path d="M18 74 H110 Q106 112 64 114 Q22 112 18 74Z" fill="#3E8FB0" {s()}/>
<path d="M26 92 Q64 102 102 92" fill="none" stroke="#9FD8EC" stroke-width="3"/>
<ellipse cx="64" cy="74" rx="46" ry="12" fill="#F2DDB0" {s()}/>
<path d="M30 72 Q64 60 98 72 Q64 82 30 72Z" fill="#EBCB8E" {W(2)}/>
<ellipse cx="64" cy="70" rx="12" ry="4" fill="#C8B428" {W(1.8)}/>
<circle cx="98" cy="54" r="5" fill="#EAC27A" {W(2)}/><circle cx="110" cy="40" r="4.4" fill="#EAC27A" {W(2)}/><circle cx="116" cy="62" r="3.8" fill="#EAC27A" {W(2)}/>
<path d="M72 64 L80 56" stroke="#E2572E" stroke-width="2.4"/>
{face(58, 92, d=9, k=0.85)}
<path d="M16 86 Q4 78 8 64 M112 86 Q118 74 108 66" fill="none" {W(3)}/>
''')
SUBJ["cafe-sirocco-korolev"] = ("мисочка нежного хумуса с лужицей оливкового масла и паприкой",
                                "жаркий ветер сирокко сдувает с неё нут, а хумус ловит горошины руками")

# 20. Малатеста — пицца «Дьявола» с перчиками-рожками
ICONS["cafe-malatesta-korolev"] = svg("h_diavola", f'''
<circle cx="64" cy="72" r="46" fill="#E9A84C" {s()}/>
<circle cx="64" cy="72" r="38" fill="#E2483A" {W(2.2)}/>
<path d="M36 64 Q50 58 62 66 Q78 74 92 64" fill="none" stroke="#FFE7A8" stroke-width="5" stroke-linecap="round"/>
<circle cx="44" cy="88" r="6" fill="#A32626" {W(1.8)}/><circle cx="84" cy="90" r="6" fill="#A32626" {W(1.8)}/><circle cx="64" cy="100" r="5" fill="#A32626" {W(1.8)}/>
<path d="M40 34 Q30 18 40 8 Q46 22 50 30Z" fill="#D7261E" {s()}/><path d="M40 8 l-4 -4" {W(3)}/>
<path d="M88 34 Q98 18 88 8 Q82 22 78 30Z" fill="#D7261E" {s()}/><path d="M88 8 l4 -4" {W(3)}/>
{eye(52, 76, 0.9)}<path d="M70 76 q6 -4 12 0" fill="none" {W(2.8)}/>
<path d="M52 88 Q64 96 78 86" fill="none" {W(2.8)}/>
<path d="M46 66 l10 4 M84 66 l-10 4" {W(2.8)}/>
''')
SUBJ["cafe-malatesta-korolev"] = ("острая пицца «Дьявола» с двумя красными перчиками-рожками",
                                  "хитро подмигивает и ухмыляется, задумав шалость")

# 21. Дирижабль — паровая булочка бао взлетает как дирижабль
ICONS["cafe-dirizhabl-lyubertsy"] = svg("h_airship", f'''
<path d="M10 112 Q22 100 36 108 Q46 98 58 110 Q62 120 50 122 H16 Q2 120 10 112Z" fill="#fff" {s()}/>
<ellipse cx="64" cy="48" rx="46" ry="26" fill="#FBF7EF" {s()}/>
<path d="M30 40 Q64 28 98 40" fill="none" stroke="#E9DFCB" stroke-width="3"/>
<path d="M104 40 L118 30 L118 66 L104 56Z" fill="#F25C78" {s()}/>
{face(56, 50, d=9, k=0.85)}
<path d="M48 72 L54 86 M80 72 L74 86" {W(2.4)}/>
<path d="M50 84 H78 L74 98 H54Z" fill="#C98B4E" {s()}/>
<path d="M54 90 H74" stroke="#9A6634" stroke-width="2"/>
<path d="M22 44 Q12 38 6 44 M22 52 Q12 58 6 52" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
{sparkle(104, 96, 5)}{sparkle(108, 16, 4)}
''')
SUBJ["cafe-dirizhabl-lyubertsy"] = ("пухлая белая паровая булочка бао с розовым хвостовым оперением",
                                    "плывёт по небу, как дирижабль, неся под собой плетёную корзинку-гондолу")

# 22. Чайхана Инжир — рулет ханум дремлет на курпаче под сюзане
ICONS["cafe-chaikhana-inzhir-pererva"] = svg("h_suzani", f'''
<circle cx="30" cy="30" r="14" fill="#FFE07A" {W(2.2)}/><circle cx="30" cy="30" r="7" fill="#E2483A"/>
<circle cx="98" cy="22" r="11" fill="#7BD3C4" {W(2.2)}/><circle cx="98" cy="22" r="5" fill="#2F7A6E"/>
<rect x="6" y="88" width="116" height="26" rx="8" fill="#3A6FC2" {s()}/>
<path d="M14 100 h8 l4 -6 l4 6 h8 l4 -6 l4 6 h8 l4 -6 l4 6 h8 l4 -6 l4 6 h8 l4 -6 l4 6 h8" fill="none" stroke="#FFD166" stroke-width="2.4"/>
<path d="M18 88 Q16 54 64 50 Q112 54 110 88Z" fill="#F7EBD3" {s()}/>
<path d="M30 86 Q28 62 64 60 Q100 62 98 86" fill="none" stroke="#C96B3A" stroke-width="4"/>
<path d="M42 86 Q42 72 64 70 Q86 72 86 86" fill="none" stroke="#C96B3A" stroke-width="4"/>
<path d="M54 86 Q56 80 64 80 Q72 80 74 86" fill="none" stroke="#C96B3A" stroke-width="4"/>
<path d="M50 66 q4 3 8 0 M70 66 q4 3 8 0" fill="none" {W(2.6)}/>
<ellipse cx="44" cy="74" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/><ellipse cx="84" cy="74" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/>
<text x="96" y="52" font-family="Arial" font-weight="bold" font-size="14" fill="#fff" stroke="{O}" stroke-width="1">z</text>
<text x="106" y="40" font-family="Arial" font-weight="bold" font-size="10" fill="#fff" stroke="{O}" stroke-width="1">z</text>
''')
SUBJ["cafe-chaikhana-inzhir-pererva"] = ("узбекский паровой рулет ханум с мясной спиралью внутри",
                                         "сладко дремлет на синей курпаче под расшитыми кругами сюзане")

# 23. Жаворонок — булочка-жаворонок в соломенном гнезде на подоконнике
ICONS["cafe-zhavoronok-pererva"] = svg("h_bakery", f'''
<rect x="8" y="10" width="112" height="72" rx="6" fill="#DFF2FF" {s()}/>
<path d="M64 10 V82 M8 46 H120" {W(3)}/>
<rect x="0" y="82" width="128" height="14" fill="#F2F2F2" {s()}/>
<path d="M22 96 Q20 78 64 76 Q108 78 106 96 Q64 104 22 96Z" fill="#E8C66A" {s()}/>
<path d="M28 90 l10 -6 M44 92 l8 -8 M74 90 l10 -6 M90 92 l8 -6" stroke="#B88E2E" stroke-width="2"/>
<path d="M36 80 Q34 52 62 50 Q76 48 84 56 L100 46 L96 60 Q100 74 86 82Z" fill="#E7A24E" {s()}/>
<path d="M84 56 L100 46 L96 60" fill="#D18A3A" {W(2)}/>
<path d="M44 64 Q54 58 62 66 Q54 72 44 64Z" fill="#D18A3A" {W(2)}/>
<path d="M30 60 L18 54 L28 66Z" fill="#D18A3A" {W(2)}/>
<circle cx="74" cy="58" r="3.4" fill="#4A2E1E"/><circle cx="73" cy="57" r="1.1" fill="#fff"/>
<path d="M82 62 L90 64 L82 67Z" fill="#B87A2A" {W(1.6)}/>
<ellipse cx="72" cy="66" rx="3.6" ry="2" fill="#FF7FA8" opacity=".6"/>
<circle cx="50" cy="74" r="1.8" fill="#6B3A1E"/><circle cx="60" cy="76" r="1.8" fill="#6B3A1E"/>
''')
SUBJ["cafe-zhavoronok-pererva"] = ("весенняя сдобная булочка-жаворонок с изюминкой-глазком",
                                   "сидит в соломенном гнёздышке на белом подоконнике пекарни")

# 24. Бакинские Каникулы — шакер-чурек на надувном матрасе в Каспии
ICONS["cafe-bakinskie-kanikuly-bratislavskaya"] = svg("h_caspian", f'''
<circle cx="102" cy="24" r="12" fill="#FFD84A" {W(2.4)}/>
<path d="M0 60 Q32 54 64 60 T128 60 V130 H0Z" fill="#2E9BC2"/>
<path d="M0 60 Q32 54 64 60 T128 60" fill="none" stroke="#fff" stroke-width="3"/>
<path d="M10 98 Q16 84 30 86 H104 Q120 86 118 100 Q116 110 102 110 H26 Q10 110 10 98Z" fill="#F25C78" {s()}/>
<path d="M36 88 V108 M58 88 V108 M80 88 V108" stroke="#D63A5E" stroke-width="2.4"/>
<circle cx="64" cy="80" r="26" fill="#F7E1B0" {s()}/>
<circle cx="64" cy="80" r="20" fill="none" stroke="#E2BE7A" stroke-width="2"/>
<g fill="#D9A84E">{"".join(f'<circle cx="{64+16*__import__("math").cos(a/8*6.283):.1f}" cy="{80+16*__import__("math").sin(a/8*6.283):.1f}" r="1.6"/>' for a in range(8))}</g>
<path d="M56 70 q-2 -6 2 -8 M64 68 q0 -6 4 -8" fill="none" stroke="#D9A84E" stroke-width="2"/>
{face(64, 82, d=8, k=0.8)}
<path d="M48 74 h8 v4 h-8z M72 74 h8 v4 h-8z" fill="{O}"/><path d="M56 76 h16" {W(1.8)}/>
''')
SUBJ["cafe-bakinskie-kanikuly-bratislavskaya"] = ("круглое азербайджанское песочное печенье шакер-чурек в тёмных очках",
                                                  "загорает на розовом надувном матрасе посреди Каспийского моря")

# 25. Qalaquri Family — сациви принимает ванну в ореховом соусе
ICONS["cafe-qalaquri-family-bratislavskaya"] = svg("h_bath", f'''
<path d="M14 66 H114 V78 Q114 108 64 110 Q14 108 14 78Z" fill="#fff" {s()}/>
<path d="M24 110 L20 122 M104 110 L108 122" {W(4)}/>
<path d="M14 66 H114" {W(3)}/>
<ellipse cx="64" cy="66" rx="50" ry="6" fill="#FFF8E8" {W(2)}/>
<path d="M42 66 Q40 40 62 38 Q84 40 82 64Z" fill="#D9A15C" {s()}/>
<path d="M78 46 Q96 38 98 26 Q102 22 104 28 Q104 40 82 56Z" fill="#D9A15C" {s()}/>
<circle cx="104" cy="24" r="5" fill="#fff" {W(2)}/>
{face(60, 52, d=7, k=0.75)}
<circle cx="30" cy="56" r="6" fill="#fff" {W(2)}/><circle cx="20" cy="44" r="4" fill="#fff" {W(1.8)}/><circle cx="96" cy="58" r="5" fill="#fff" {W(2)}/>
<circle cx="34" cy="30" r="3" fill="#fff" {W(1.6)}/>
<path d="M48 78 Q64 88 80 78" fill="none" stroke="#E7DDC8" stroke-width="3"/>
<circle cx="70" cy="58" r="2" fill="#C2185B"/><circle cx="50" cy="60" r="2" fill="#C2185B"/>
''')
SUBJ["cafe-qalaquri-family-bratislavskaya"] = ("румяная курочка сациви с зёрнышками граната",
                                               "нежится в белой ванне, полной орехового соуса, и пускает мыльные пузыри")

# 26. Бык да Баран — чизбургер-силач подтягивается на турнике
ICONS["cafe-byk-da-baran-ushakova"] = svg("h_gym", f'''
<rect x="0" y="110" width="128" height="20" fill="#8FD08C"/>
<path d="M14 112 V16 M114 112 V16" stroke="{O}" stroke-width="6"/><path d="M14 112 V16 M114 112 V16" stroke="#E07A3A" stroke-width="3"/>
<path d="M10 22 H118" stroke="{O}" stroke-width="6"/><path d="M10 22 H118" stroke="#C9CED8" stroke-width="3"/>
<path d="M40 64 Q34 40 38 22 M88 64 Q94 40 90 22" fill="none" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M40 64 Q34 40 38 22 M88 64 Q94 40 90 22" fill="none" stroke="#E2A35A" stroke-width="3.6" stroke-linecap="round"/>
<path d="M30 66 Q32 44 64 42 Q96 44 98 66Z" fill="#E9A84C" {s()}/>
<g fill="#FFF4D6">{"".join(f'<ellipse cx="{x}" cy="{y}" rx="2" ry="1.2"/>' for x, y in [(48,52),(60,48),(72,50),(84,54),(56,58),(76,58)])}</g>
<path d="M28 66 Q36 72 44 66 Q52 74 60 66 Q68 74 76 66 Q84 74 92 66 Q98 70 100 66 L98 72 H30Z" fill="#7BC24E" {W(2)}/>
<path d="M30 72 H98 L94 76 L96 82 H32 L34 76Z" fill="#FFC21A" {W(2)}/>
<rect x="28" y="80" width="72" height="12" rx="6" fill="#7A4424" {s()}/>
<path d="M30 92 H98 Q98 104 64 104 Q30 104 30 92Z" fill="#E9A84C" {s()}/>
{face(64, 98, d=8, k=0.6, mouth=False)}
<path d="M58 60 h12" fill="none" {W(1)}/>
{eye(54, 58, 0.75)}{eye(74, 58, 0.75)}
<path d="M56 64 Q64 70 72 64" fill="none" {W(2.4)}/>
<path d="M104 52 l6 -4 M106 60 h8" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''')
SUBJ["cafe-byk-da-baran-ushakova"] = ("двойной чизбургер с говяжьей и бараньей котлетами",
                                      "подтягивается на уличном турнике, напрягая руки-силачи")

# 27. Маленькая Италия — крошечная пиццетта в красном сапожке-Италии
ICONS["cafe-malenkaya-italiya-tyumensky"] = svg("h_boot", f'''
<path d="M44 14 H86 V74 Q86 82 96 86 L116 92 Q124 96 120 106 Q116 114 104 112 L58 110 Q40 110 40 94 V20Z" fill="#E23A3A" {s()}/>
<path d="M44 14 H86 V24 H44Z" fill="#fff" {W(2.2)}/>
<path d="M44 24 H86 V30 H44Z" fill="#3E9B57" {W(2)}/>
<path d="M50 102 h4 M60 102 h4 M70 102 h4 M80 102 h4 M90 102 h4 M100 102 h4" stroke="#fff" stroke-width="2.4"/>
<circle cx="64" cy="48" r="20" fill="#E9A84C" {s()}/>
<circle cx="64" cy="48" r="15" fill="#F25C46" {W(2)}/>
<circle cx="58" cy="42" r="3" fill="#FFF6D8"/><circle cx="70" cy="44" r="3" fill="#FFF6D8"/>
<path d="M66 54 l4 -3" stroke="#3E9B57" stroke-width="2.6" stroke-linecap="round"/>
{face(64, 50, d=6, k=0.6)}
<path d="M44 52 Q36 46 34 36 M84 52 Q94 46 96 36" fill="none" {W(3)}/>
{sparkle(20, 40, 5)}{sparkle(108, 24, 4)}
''')
SUBJ["cafe-malenkaya-italiya-tyumensky"] = ("крошечная пиццетта размером с ладошку",
                                            "радостно машет руками, выглядывая из красного сапожка в форме Италии")

# 28. Adria Mare — дорадо выпрыгивает из Адриатики у маяка
ICONS["cafe-adria-mare-preobrazhenka"] = svg("h_adriatic", f'''
<path d="M104 20 L112 20 L114 70 L102 70Z" fill="#fff" {s()}/>
<path d="M103 34 H113 M103 50 H113" stroke="#E23A3A" stroke-width="6"/>
<path d="M100 20 H116 L108 10Z" fill="#E23A3A" {W(2)}/>
<path d="M0 78 Q32 70 64 78 T128 78 V130 H0Z" fill="#1F6FB0"/>
<path d="M0 78 Q32 70 64 78 T128 78" fill="none" stroke="#fff" stroke-width="3"/>
<path d="M20 96 Q30 88 40 96 M78 104 Q88 96 98 104" fill="none" stroke="#7FC3EE" stroke-width="3"/>
<g transform="rotate(-24 56 58)">
<path d="M16 58 Q36 30 70 40 Q86 46 92 58 Q86 70 70 76 Q36 86 16 58Z" fill="#C9D3DC" {s()}/>
<path d="M30 58 Q50 46 76 52" fill="none" stroke="#F2C23A" stroke-width="4"/>
<path d="M92 58 L110 44 L106 58 L110 72Z" fill="#AEB9C4" {s()}/>
<path d="M44 40 Q54 28 66 38" fill="#AEB9C4" {W(2)}/>
<circle cx="30" cy="54" r="5" fill="#fff" {W(2)}/><circle cx="31" cy="54" r="2.4" fill="{O}"/>
<path d="M20 64 Q26 68 32 64" fill="none" {W(2.2)}/>
<ellipse cx="38" cy="62" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/>
</g>
<circle cx="30" cy="94" r="3" fill="#fff" opacity=".8"/><circle cx="40" cy="104" r="2" fill="#fff" opacity=".8"/>
''')
SUBJ["cafe-adria-mare-preobrazhenka"] = ("серебристая дорада с золотой полоской на лбу",
                                         "выпрыгивает дугой из синей Адриатики рядом с красно-белым маяком")

# 29. Италония — полосатое семифредо тает у фонтана
ICONS["cafe-italoniya-yuzhnobutovskaya"] = svg("h_fountain", f'''
<path d="M6 108 H122 V128 H6Z" fill="#E7DCC8"/>
<path d="M60 108 V70 M68 108 V70" {W(3)}/>
<path d="M44 70 H84 L80 78 H48Z" fill="#B8D8E8" {s()}/>
<path d="M64 70 Q50 56 46 66 M64 70 Q78 56 82 66 M64 70 V58" fill="none" stroke="#5FB7E8" stroke-width="3" stroke-linecap="round"/>
<path d="M20 108 Q20 96 64 96 Q108 96 108 108Z" fill="#9FD3EA" {s()}/>
<g transform="translate(-6 0)">
<rect x="14" y="56" width="36" height="34" rx="4" fill="#FFF3DC" {s()}/>
<rect x="14" y="56" width="36" height="10" fill="#F6A6B8" {W(2)}/><rect x="14" y="76" width="36" height="8" fill="#9C6B4A" {W(2)}/>
<path d="M22 90 Q22 98 26 98 Q30 98 30 90 M40 90 Q40 102 44 102 Q48 102 48 90" fill="#FFF3DC" {W(2)}/>
{face(32, 70, d=6, k=0.6)}
</g>
<circle cx="104" cy="28" r="10" fill="#FFD84A" {W(2.4)}/>
<path d="M90 36 l-6 6 M104 44 v8 M118 36 l6 6" stroke="#FFD84A" stroke-width="3" stroke-linecap="round"/>
''')
SUBJ["cafe-italoniya-yuzhnobutovskaya"] = ("полосатый кирпичик итальянского семифредо — клубника, ваниль и шоколад",
                                           "тает на жарком солнце у городского фонтана, капли стекают вниз")

# 30. Ohana — йогурт-боул в венке танцует хулу
ICONS["cafe-ohana-buninskaya"] = svg("h_hawaii", f'''
<path d="M108 128 Q104 70 116 40" fill="none" stroke="#8A5A34" stroke-width="6"/>
<path d="M116 40 Q96 30 90 44 M116 40 Q128 24 140 36 M116 40 Q110 20 124 14" fill="none" stroke="#3E9B57" stroke-width="6" stroke-linecap="round"/>
<path d="M30 90 Q26 120 34 124 M98 90 Q102 120 94 124" fill="none" stroke="#8BC34A" stroke-width="4"/>
<path d="M28 92 Q30 112 64 114 Q98 112 100 92 L92 120 H36Z" fill="#B5DE6C" {W(2.2)}/>
<path d="M34 96 V120 M46 98 V122 M58 98 V122 M70 98 V122 M82 98 V122 M94 96 V120" stroke="#7CB342" stroke-width="2"/>
<path d="M22 54 H106 Q102 94 64 96 Q26 94 22 54Z" fill="#fff" {s()}/>
<ellipse cx="64" cy="54" rx="42" ry="10" fill="#FBF6FF" {s()}/>
<circle cx="46" cy="52" r="5" fill="#F25C78" {W(1.8)}/><circle cx="62" cy="50" r="5" fill="#FFC21A" {W(1.8)}/><circle cx="80" cy="52" r="5" fill="#6C5CE7" {W(1.8)}/>
<path d="M50 46 l6 -8 M84 46 l4 -8" stroke="#3E9B57" stroke-width="2.4"/>
{face(64, 74, d=9, k=0.85)}
<g>{"".join(f'<circle cx="{x}" cy="{y}" r="4.6" fill="{c}" stroke="{O}" stroke-width="1.6"/>' for x, y, c in [(28,60,"#FF7FA8"),(36,84,"#FFD166"),(52,92,"#FF7FA8"),(76,92,"#FFD166"),(92,84,"#FF7FA8"),(100,60,"#FFD166")])}</g>
<path d="M22 60 Q10 50 8 40 M106 60 Q116 70 122 66" fill="none" {W(3)}/>
''')
SUBJ["cafe-ohana-buninskaya"] = ("йогурт-боул с ягодами и цветочным ожерельем-леи",
                                 "танцует хулу в юбочке из травы под пальмой")

# 31. Чайхона Butovo Grill — кюфте на шампуре поют над углями
ICONS["cafe-butovo-grill-bartenevskaya"] = svg("h_coals", f'''
<rect x="10" y="88" width="108" height="26" rx="4" fill="#5A5F6E" {s()}/>
<g fill="#FF7A2E">{"".join(f'<circle cx="{x}" cy="{y}" r="5"/>' for x, y in [(24,90),(38,92),(52,89),(66,92),(80,90),(94,92),(108,90)])}</g>
<path d="M30 84 Q26 74 32 66 M64 84 Q60 72 66 64 M98 84 Q94 74 100 66" fill="none" stroke="#FFB13B" stroke-width="3" stroke-linecap="round"/>
<path d="M4 60 H124" stroke="{O}" stroke-width="5" stroke-linecap="round"/><path d="M4 60 H124" stroke="#D9DDE6" stroke-width="2.4" stroke-linecap="round"/>
<circle cx="120" cy="60" r="5" fill="#D9DDE6" {W(2)}/>
<ellipse cx="34" cy="58" rx="14" ry="13" fill="#9C5A34" {s()}/>{face(34, 58, d=5, k=0.55)}
<ellipse cx="64" cy="58" rx="14" ry="13" fill="#A8643A" {s()}/>{eye(59, 56, 0.55)}{eye(69, 56, 0.55)}<ellipse cx="64" cy="64" rx="3" ry="4" fill="{O}"/>
<ellipse cx="94" cy="58" rx="14" ry="13" fill="#9C5A34" {s()}/>{face(94, 58, d=5, k=0.55)}
<path d="M58 28 q4 -8 8 0 q-4 6 -8 0z M80 22 l2 -10 l8 2 v8" fill="#fff" {W(1.8)}/>
<circle cx="80" cy="24" r="3" fill="#fff" {W(1.8)}/><circle cx="90" cy="22" r="3" fill="#fff" {W(1.8)}/>
''')
SUBJ["cafe-butovo-grill-bartenevskaya"] = ("три пухлых шарика-кюфте на одном шампуре",
                                           "хором поют песню, жарясь над тлеющими углями мангала")

# 32. Mammina — тортеллини катится колесом-обручем по итальянской улочке
ICONS["cafe-mammina-kapitoliy"] = svg("h_street", f'''
<rect x="0" y="14" width="40" height="88" fill="#F2C08F" {s()}/><rect x="88" y="8" width="40" height="94" fill="#E89A74" {s()}/>
<rect x="10" y="26" width="12" height="16" fill="#6FB7D8" {W(2)}/><rect x="10" y="54" width="12" height="16" fill="#6FB7D8" {W(2)}/>
<rect x="100" y="22" width="12" height="16" fill="#6FB7D8" {W(2)}/><rect x="100" y="50" width="12" height="16" fill="#6FB7D8" {W(2)}/>
<path d="M40 30 Q64 40 88 30" fill="none" {W(1.6)}/>
<path d="M50 34 v8 h6 v-6 M66 36 v8 h6 v-8" fill="#fff" {W(1.6)}/>
<rect x="0" y="102" width="128" height="28" fill="#C9B79A"/>
<path d="M0 102 H128 M0 114 H128 M16 102 V114 M44 102 V114 M76 102 V114 M108 102 V114" stroke="#A8957A" stroke-width="2"/>
<circle cx="66" cy="76" r="26" fill="#F7D774" {s()}/>
<circle cx="66" cy="76" r="11" fill="#C9E6F2" {s()}/>
<path d="M44 62 Q40 76 46 90" fill="none" stroke="#E4B847" stroke-width="3"/>
<path d="M86 60 Q94 52 100 58 Q96 66 86 66Z" fill="#F7D774" {W(2)}/>
{face(66, 60, d=6, k=0.6, mouth=False)}
<path d="M62 66 Q66 69 70 66" fill="none" {W(2)}/>
<path d="M22 84 h12 M18 92 h14 M26 76 h8" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''')
SUBJ["cafe-mammina-kapitoliy"] = ("золотое колечко тортеллини с защипом сбоку",
                                  "катится, как обруч, по брусчатке узкой итальянской улочки с бельевой верёвкой")

if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for pid in ids:
        open(os.path.join(OUT, f"{pid}.svg"), "w").write(ICONS[pid])
    path = os.path.join(OUT, "subjects.txt")
    lines = [l for l in open(path, encoding="utf-8").read().splitlines() if l.split(" — ")[0] not in ICONS]
    lines += [f"{pid} — герой: {h} | сцена: {sc}" for pid, (h, sc) in SUBJ.items()]
    open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("svg:", len(ids))
