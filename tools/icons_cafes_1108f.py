"""Иконки робота cafes, 2026-11-08 (16–17 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая придумана и нарисована
отдельно (свой герой по кухне/названию, своя сцена, своя компоновка и палитра фона). Сверено с листами icons-catalog
и icons-src/subjects.txt. Запуск: python3 tools/icons_cafes_1108f.py [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "f_riviera": ("#FFF3D6", "#F2B880"),
    "f_pkhali": ("#F3FFE8", "#9BCB7A"),
    "f_runway": ("#EAF0FF", "#8EA2E6"),
    "f_cabin": ("#FDF0E4", "#D9A88A"),
    "f_jonj": ("#FFF0F4", "#E79AB2"),
    "f_tkemali": ("#FFFBE0", "#E3C94E"),
    "f_adjika": ("#FFE9E0", "#F08C6E"),
    "f_forest": ("#EFF8E2", "#86B88A"),
    "f_ukha": ("#E2FAFF", "#5FB7D8"),
    "f_hayloft": ("#FFF6E2", "#C99A5A"),
    "f_dream": ("#EDE4FF", "#7B6CD9"),
    "f_tarkhun": ("#E6FFF4", "#4DBF95"),
    "f_baggage": ("#F4F4F8", "#A7A9C4"),
    "f_party": ("#FFF0E0", "#F5A25B"),
    "f_maze": ("#E8FBFF", "#46B4C9"),
    "f_aubergine": ("#F6EDFF", "#B48AD8"),
    "f_terrace": ("#FFFBEA", "#9CCB5C"),
})

# 1. Osteria Mario (ТРЦ «Ривьера») — граните на пляже Ривьеры
ICONS["cafe-osteria-riviera"] = svg("f_riviera", f'''
<rect x="0" y="92" width="128" height="40" fill="#F7DFA6"/>
<path d="M0 84 Q32 78 64 84 T128 84 V96 Q96 90 64 96 T0 96Z" fill="#4FB3D9" {W(2.2)}/>
<circle cx="104" cy="26" r="10" fill="#FFD84A" {W(2.4)}/>
<path d="M36 52 H92 L84 110 Q64 116 44 110Z" fill="#E9F6FF" opacity=".95" {s()}/>
<path d="M40 70 H88 L86 84 H42Z" fill="#F7D046"/><path d="M42 84 H86 L84 98 H44Z" fill="#7BC96F"/>
<path d="M38 56 H90 L88 70 H40Z" fill="#F2506A"/>
<path d="M34 54 Q40 30 64 30 Q88 30 94 54Z" fill="#F2506A" {s()}/>
<path d="M44 44 l4 -3 M58 38 l4 -2 M74 40 l4 2 M82 48 l3 -3" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M76 34 L96 10" stroke="{O}" stroke-width="5" stroke-linecap="round"/><path d="M76 34 L96 10" stroke="#FFC23A" stroke-width="2.4" stroke-linecap="round"/>
{face(64, 84, d=9, k=0.85)}
{sparkle(18, 30, 5)}
''')
SUBJ["cafe-osteria-riviera"] = ("граните — итальянский фруктовый лёд слоями в прозрачном стаканчике с ложечкой",
                                "стоит на песке пляжа Ривьеры у самой кромки моря под жарким солнцем")

# 2. Швили (ТРЦ «Ривьера») — чкмерули в глиняной кеци
ICONS["cafe-shvili-riviera"] = svg("f_pkhali", f'''
<path d="M30 104 L22 120 M98 104 L106 120 M64 108 V122" stroke="#5A3A22" stroke-width="5" stroke-linecap="round"/>
<ellipse cx="64" cy="100" rx="46" ry="10" fill="#6E4A2E" {s()}/>
<path d="M14 66 Q16 100 64 102 Q112 100 114 66Z" fill="#B5582E" {s()}/>
<ellipse cx="64" cy="66" rx="50" ry="14" fill="#F6EED6" {s()}/>
<path d="M30 62 Q64 76 98 62" fill="none" stroke="#E2D7B4" stroke-width="2.4"/>
<path d="M44 60 Q42 30 66 28 Q90 30 88 56 Q80 66 64 66 Q50 66 44 60Z" fill="#E59A3C" {s()}/>
<path d="M84 40 Q100 30 104 18" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M84 40 Q100 30 104 18" fill="none" stroke="#E59A3C" stroke-width="5" stroke-linecap="round"/>
<circle cx="104" cy="16" r="5" fill="#fff" {W(2.2)}/>
{face(64, 46, d=8, k=0.75)}
<circle cx="32" cy="64" r="2.4" fill="#7FBF5A"/><circle cx="96" cy="68" r="2.4" fill="#7FBF5A"/><circle cx="54" cy="72" r="2.2" fill="#fff" {W(1.4)}/>
''')
SUBJ["cafe-shvili-riviera"] = ("чкмерули — румяный цыплёнок в белом чесночно-сливочном соусе",
                               "сидит в глиняной сковородке-кеци на деревянной подставке и машет крылышком")

# 3. Джой Хаус (Внуково) — картофельная крокета-пилот на бумажном самолётике
ICONS["cafe-joy-house-vnukovo"] = svg("f_runway", f'''
<path d="M0 108 L128 96 V128 H0Z" fill="#6B7180"/>
<path d="M10 110 h14 M40 107 h14 M70 104 h14 M100 101 h14" stroke="#fff" stroke-width="3"/>
<path d="M14 72 L114 46 L60 94 L52 76Z" fill="#fff" {s()}/>
<path d="M52 76 L114 46 L66 72Z" fill="#DDE3F7" {W(2.2)}/>
<rect x="40" y="38" width="44" height="34" rx="16" fill="#E8B04E" {s()}/>
<circle cx="50" cy="62" r="1.8" fill="#B5762A"/><circle cx="76" cy="50" r="1.8" fill="#B5762A"/><circle cx="72" cy="66" r="1.8" fill="#B5762A"/>
<path d="M40 50 Q44 24 62 24 Q80 24 84 50 Q74 42 62 42 Q50 42 40 50Z" fill="#2E6FD0" {W(2.4)}/>
<rect x="47" y="30" width="11" height="8" rx="3" fill="#9FE3FF" {W(1.8)}/><rect x="66" y="30" width="11" height="8" rx="3" fill="#9FE3FF" {W(1.8)}/>
{face(62, 56, d=7, k=0.65)}
<path d="M86 46 Q104 40 112 28" fill="none" stroke="#E2483A" stroke-width="4" stroke-linecap="round"/>
{sparkle(22, 28, 5)}{sparkle(100, 78, 4)}
''')
SUBJ["cafe-joy-house-vnukovo"] = ("картофельная крокета в синем шлеме лётчика с очками",
                                  "летит на бумажном самолётике над взлётной полосой Внукова, шарф развевается")

# 4. Рассольников (Внуково) — сбитень в деревянной кружке у иллюминатора
ICONS["cafe-rassolnikov-vnukovo"] = svg("f_cabin", f'''
<rect x="70" y="16" width="42" height="56" rx="21" fill="#B9E4FF" {s()}/>
<path d="M78 50 Q90 44 104 48" fill="none" stroke="#fff" stroke-width="4"/>
<ellipse cx="100" cy="30" rx="7" ry="4" fill="#fff"/>
<rect x="6" y="102" width="116" height="30" fill="#8C5A3C" {s()}/>
<path d="M28 50 H80 V98 Q80 104 74 104 H34 Q28 104 28 98Z" fill="#C98A4A" {s()}/>
<path d="M40 50 V104 M54 50 V104 M68 50 V104" stroke="#9E6532" stroke-width="2.2"/>
<path d="M26 62 H82 M26 90 H82" stroke="#5A6378" stroke-width="4"/>
<path d="M80 60 Q98 60 96 76 Q94 90 80 88" fill="none" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M80 60 Q98 60 96 76 Q94 90 80 88" fill="none" stroke="#C98A4A" stroke-width="3.4" stroke-linecap="round"/>
<ellipse cx="54" cy="50" rx="26" ry="6" fill="#B5542C" {s()}/>
<path d="M44 40 q-4 -8 2 -14 M58 40 q-4 -8 2 -14" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<path d="M60 48 l6 -10 l3 4" fill="#5DAE47" {W(1.6)}/>
{face(54, 76, d=9, k=0.75)}
''')
SUBJ["cafe-rassolnikov-vnukovo"] = ("горячий медовый сбитень в деревянной кружке с обручами",
                                    "дымится на откидном столике у иллюминатора самолёта")

# 5. Джонджоли (пр. Мира, 99) — пиала джонджоли-причёска
ICONS["cafe-dzhondzholi-mira"] = svg("f_jonj", f'''
<path d="M40 54 Q30 24 36 14 M48 52 Q46 22 54 10 M60 50 Q62 22 72 12 M72 52 Q80 26 92 20 M82 56 Q96 38 104 36"
 fill="none" stroke="#3F7D2A" stroke-width="7" stroke-linecap="round"/>
<path d="M40 54 Q30 24 36 14 M48 52 Q46 22 54 10 M60 50 Q62 22 72 12 M72 52 Q80 26 92 20 M82 56 Q96 38 104 36"
 fill="none" stroke="#86C25A" stroke-width="3.6" stroke-linecap="round"/>
<circle cx="36" cy="14" r="3.4" fill="#F5F0D8" {W(1.8)}/><circle cx="92" cy="20" r="3.4" fill="#F5F0D8" {W(1.8)}/>
<path d="M18 56 H110 Q108 104 64 106 Q20 104 18 56Z" fill="#FFFFFF" {s()}/>
<path d="M24 70 H104" stroke="#3A7FC9" stroke-width="3"/>
<path d="M30 80 l6 -5 l6 5 l6 -5 l6 5 l6 -5 l6 5 l6 -5 l6 5 l6 -5 l6 5" fill="none" stroke="#3A7FC9" stroke-width="2"/>
{face(64, 90, d=11, k=0.85)}
''')
SUBJ["cafe-dzhondzholi-mira"] = ("джонджоли — пучок маринованных зелёных стебельков с бутонами",
                                 "торчат вихрастой причёской из белой пиалы с синим узором, а пиала улыбается")

# 6. Джонджоли (Алтуфьевское ш.) — ткемали прыгает через скакалку из лаваша
ICONS["cafe-dzhondzholi-altufevo"] = svg("f_tkemali", f'''
<ellipse cx="64" cy="116" rx="36" ry="6" fill="#B89A2E" opacity=".35"/>
<path d="M22 70 Q14 120 64 122 Q114 120 106 70" fill="none" stroke="{O}" stroke-width="13" stroke-linecap="round"/>
<path d="M22 70 Q14 120 64 122 Q114 120 106 70" fill="none" stroke="#F3DDA0" stroke-width="8" stroke-linecap="round"/>
<path d="M22 70 Q14 120 64 122 Q114 120 106 70" fill="none" stroke="#D9A85A" stroke-width="2" stroke-dasharray="1 6"/>
<rect x="54" y="18" width="20" height="16" rx="3" fill="#2F7D3B" {s()}/>
<path d="M50 34 H78 L86 52 Q90 100 64 100 Q38 100 42 52Z" fill="#E1572A" {s()}/>
<rect x="46" y="58" width="36" height="20" rx="4" fill="#FFF3D0" {W(2.2)}/>
<path d="M52 68 h24" stroke="#2F7D3B" stroke-width="2.4"/>
{face(64, 86, d=8, k=0.7)}
<path d="M42 60 Q30 62 24 68 M86 60 Q98 62 104 68" fill="none" stroke="{O}" stroke-width="3.4" stroke-linecap="round"/>
''')
SUBJ["cafe-dzhondzholi-altufevo"] = ("бутылочка красного соуса ткемали с зелёной крышечкой",
                                     "прыгает через скакалку из длинного лаваша")

# 7. Хинкали-Гали (Абрамцевская) — перчик-аджика на горке из лаваша
ICONS["cafe-hinkali-gali-abramtsevskaya"] = svg("f_adjika", f'''
<path d="M14 36 H34 V112" fill="none" stroke="#7A5BC7" stroke-width="5" stroke-linecap="round"/>
<path d="M24 50 h10 M24 64 h10 M24 78 h10 M24 92 h10" stroke="#7A5BC7" stroke-width="4"/>
<path d="M34 38 Q60 40 74 72 Q86 100 118 104 V116 Q80 114 66 84 Q54 56 34 52Z" fill="#F6E0A6" {s()}/>
<circle cx="50" cy="48" r="1.6" fill="#C9963E"/><circle cx="66" cy="64" r="1.6" fill="#C9963E"/><circle cx="90" cy="100" r="1.6" fill="#C9963E"/>
<path d="M52 56 Q66 46 80 56 Q96 70 106 98 Q96 92 82 84 Q60 76 52 56Z" fill="#E3222F" {s()}/>
<path d="M56 54 Q52 42 58 36" fill="none" stroke="#2F7D3B" stroke-width="5" stroke-linecap="round"/>
<ellipse cx="70" cy="58" rx="6" ry="2.5" fill="#fff" opacity=".45"/>
{face(72, 66, d=6, k=0.6)}
<path d="M98 50 l6 -6 M104 60 l8 -2" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''')
SUBJ["cafe-hinkali-gali-abramtsevskaya"] = ("красный перчик аджики с зелёным хвостиком",
                                            "съезжает с горки из лаваша в детской игровой")

# 8. Хинкали-Гали (ул. Пришвина) — гоми читает книжку на пеньке
ICONS["cafe-hinkali-gali-prishvina"] = svg("f_forest", f'''
<path d="M10 92 L24 52 L38 92Z M92 90 L108 46 L122 90Z" fill="#4F8F55" {W(2.2)}/>
<ellipse cx="64" cy="110" rx="30" ry="9" fill="#A97142" {s()}/>
<rect x="34" y="92" width="60" height="18" fill="#B9804C" {s()}/>
<ellipse cx="64" cy="92" rx="30" ry="8" fill="#E8C58E" {s()}/>
<path d="M56 92 Q64 86 72 92" fill="none" stroke="#B9804C" stroke-width="1.6"/>
<path d="M38 86 Q36 46 64 30 Q92 46 90 86Z" fill="#F7D35A" {s()}/>
<rect x="52" y="22" width="24" height="14" rx="3" fill="#FFFBEF" transform="rotate(-10 64 29)" {W(2.2)}/>
<circle cx="46" cy="60" r="1.8" fill="#D9A92E"/><circle cx="82" cy="58" r="1.8" fill="#D9A92E"/>
{face(64, 52, d=7, k=0.65)}
<path d="M40 70 L64 78 L88 70 L88 88 L64 94 L40 88Z" fill="#3D86C6" {s()}/>
<path d="M64 78 V94" stroke="{O}" stroke-width="2"/>
<path d="M46 76 l12 4 M70 80 l12 -4" stroke="#fff" stroke-width="1.8"/>
''')
SUBJ["cafe-hinkali-gali-prishvina"] = ("гоми — жёлтая горка кукурузной каши с ломтиком сыра на макушке",
                                       "сидит на лесном пеньке и читает раскрытую синюю книжку про лес")

# 9. Ёрш (ул. Пришвина) — судачок выпрыгивает из кастрюли с ухой
ICONS["cafe-ersh-prishvina"] = svg("f_ukha", f'''
<path d="M20 74 H108 L102 116 Q64 124 26 116Z" fill="#D2D8E4" {s()}/>
<rect x="10" y="78" width="12" height="7" rx="3" fill="#8E96AC" {W(2.4)}/><rect x="106" y="78" width="12" height="7" rx="3" fill="#8E96AC" {W(2.4)}/>
<ellipse cx="64" cy="74" rx="44" ry="9" fill="#F2C35A" {s()}/>
<circle cx="44" cy="74" r="3" fill="#F08A3A"/><circle cx="84" cy="73" r="3" fill="#F08A3A"/>
<g transform="rotate(-24 64 46)">
<path d="M26 46 Q48 24 84 38 L102 26 Q100 46 102 62 L84 52 Q48 68 26 46Z" fill="#B7C4A8" {s()}/>
<path d="M44 34 L50 22 L56 32 L62 22 L68 33" fill="#8E9F7A" {W(2.2)}/>
<path d="M50 36 V54 M62 34 V54 M74 37 V51" stroke="#6E7F5E" stroke-width="3" opacity=".55"/>
{eye(38, 42, 0.8)}
<path d="M26 48 Q30 52 34 50" fill="none" {W(2.2)}/>
</g>
<path d="M30 66 q4 -6 8 0 M90 64 q4 -6 8 0" fill="none" stroke="#fff" stroke-width="2.4"/>
''')
SUBJ["cafe-ersh-prishvina"] = ("судачок — серебристая речная рыбка с полосками на боках",
                               "выпрыгивает из кастрюли с жёлтой ухой, разбрызгивая капли")

# 10. Сеновал (Очаково) — гороховый суп спит на сеновале
ICONS["cafe-senoval-ochakovo"] = svg("f_hayloft", f'''
<path d="M6 46 L64 12 L122 46" fill="none" stroke="#7B4A2A" stroke-width="7" stroke-linecap="round"/>
<path d="M18 52 V120 M110 52 V120" stroke="#7B4A2A" stroke-width="6"/>
<path d="M14 120 Q20 92 40 94 Q64 84 88 94 Q108 92 114 120Z" fill="#F2CF6B" {s()}/>
<path d="M28 106 l6 -10 M44 102 l2 -10 M80 100 l4 -10 M96 104 l6 -8" stroke="#C99A3A" stroke-width="2.2"/>
<path d="M34 70 Q36 96 64 96 Q92 96 94 70Z" fill="#fff" {s()}/>
<ellipse cx="64" cy="70" rx="30" ry="8" fill="#E8C04A" {s()}/>
<circle cx="54" cy="69" r="2.4" fill="#C9962E"/><circle cx="72" cy="71" r="2.4" fill="#C9962E"/><rect x="62" y="64" width="6" height="4" rx="1" fill="#B5542C"/>
<path d="M50 82 q4 3 8 0 M70 82 q4 3 8 0" fill="none" {W(2.4)}/>
<text x="86" y="50" font-family="Arial" font-weight="bold" font-size="14" fill="#fff" stroke="{O}" stroke-width="1">z</text>
<text x="98" y="38" font-family="Arial" font-weight="bold" font-size="10" fill="#fff" stroke="{O}" stroke-width="1">z</text>
''')
SUBJ["cafe-senoval-ochakovo"] = ("гороховый суп с копчёностями в белой глубокой тарелке",
                                 "сладко спит на копне сена под деревянной крышей сеновала")

# 11. Dream Kids (Гжатская) — мягкая подушка-месяц в ночном колпаке
ICONS["cafe-dream-kids-gzhatskaya"] = svg("f_dream", f'''
<circle cx="24" cy="26" r="2" fill="#fff"/><circle cx="104" cy="22" r="2.4" fill="#fff"/><circle cx="112" cy="58" r="1.8" fill="#fff"/>
{sparkle(28, 50, 5)}{sparkle(100, 40, 4)}
<path d="M14 108 Q10 90 28 90 Q30 74 50 78 Q60 64 78 74 Q98 68 102 86 Q120 88 114 108Z" fill="#FFFFFF" {s()}/>
<path d="M44 84 Q24 60 40 34 Q48 22 62 20 Q46 36 50 56 Q56 74 80 80 Q64 92 44 84Z" fill="#FFE27A" {s()}/>
<path d="M40 34 Q50 14 70 16 Q84 18 88 30" fill="#4C7BE0" {s()}/>
<circle cx="90" cy="34" r="6" fill="#fff" {W(2.2)}/>
<path d="M44 58 q4 3 8 0" fill="none" {W(2.4)}/>
<ellipse cx="46" cy="66" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/>
<path d="M50 70 q3 2 6 0" fill="none" {W(2)}/>
''')
SUBJ["cafe-dream-kids-gzhatskaya"] = ("мягкая игрушка-подушка в виде месяца в синем ночном колпаке с помпоном",
                                      "спит на белом облаке среди звёзд в детской игровой")

# 12. Старик Хинкалыч (Волхонка) — соусник сацебели с седыми усами
ICONS["cafe-starik-hinkalych-volkhonka"] = svg("f_tarkhun", f'''
<rect x="96" y="30" width="16" height="84" fill="#F2EEE4" {W(2.4)}/><rect x="92" y="24" width="24" height="8" fill="#E2DCCB" {W(2.2)}/>
<rect x="14" y="38" width="12" height="76" fill="#F2EEE4" {W(2.4)}/><rect x="10" y="32" width="20" height="8" fill="#E2DCCB" {W(2.2)}/>
<path d="M36 58 Q36 104 62 104 Q88 104 88 58Z" fill="#FFFFFF" {s()}/>
<path d="M88 64 Q102 64 98 78 Q94 88 86 86" fill="none" stroke="{O}" stroke-width="6" stroke-linecap="round"/>
<path d="M88 64 Q102 64 98 78 Q94 88 86 86" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<path d="M30 58 Q24 52 36 54 H88 Q92 54 88 60 H36Z" fill="#fff" {W(2.4)}/>
<ellipse cx="62" cy="57" rx="24" ry="5" fill="#D8342A" {W(2.2)}/>
<circle cx="56" cy="56" r="1.6" fill="#7FBF5A"/><circle cx="68" cy="58" r="1.6" fill="#7FBF5A"/>
{eye(54, 74, 0.75)}{eye(70, 74, 0.75)}
<path d="M46 84 Q54 78 62 83 Q70 78 78 84 Q72 89 62 86 Q52 89 46 84Z" fill="#F4F4F4" {W(2)}/>
<path d="M58 116 L36 70 Q32 62 26 66" fill="none" stroke="#7B4A2A" stroke-width="4.5" stroke-linecap="round"/>
<path d="M40 104 L36 116 M84 104 L88 116" stroke="{O}" stroke-width="4" stroke-linecap="round"/>
''')
SUBJ["cafe-starik-hinkalych-volkhonka"] = ("белый соусник с красным соусом сацебели и пышными седыми усами",
                                           "гуляет с тростью между белых колонн старой Волхонки")

# 13. Ачарули (Внуково) — оджахури в глиняной сковородке на багажной тележке
ICONS["cafe-acharuli-vnukovo"] = svg("f_baggage", f'''
<path d="M14 98 H104 L112 72" fill="none" stroke="#5A6378" stroke-width="5" stroke-linecap="round"/>
<path d="M16 98 V86" stroke="#5A6378" stroke-width="5" stroke-linecap="round"/>
<circle cx="28" cy="108" r="8" fill="#3B3355"/><circle cx="92" cy="108" r="8" fill="#3B3355"/>
<circle cx="28" cy="108" r="3" fill="#C9CBD6"/><circle cx="92" cy="108" r="3" fill="#C9CBD6"/>
<rect x="74" y="50" width="30" height="46" rx="5" fill="#2FA3A0" {s()}/>
<path d="M82 50 V42 H96 V50" fill="none" stroke="{O}" stroke-width="3"/>
<path d="M74 66 H104" stroke="#1F7C79" stroke-width="2.4"/>
<path d="M14 70 Q16 96 44 96 Q72 96 74 70Z" fill="#B5582E" {s()}/>
<path d="M74 72 L90 66" stroke="{O}" stroke-width="5" stroke-linecap="round"/>
<ellipse cx="44" cy="70" rx="30" ry="8" fill="#F2C35A" {s()}/>
<rect x="26" y="62" width="9" height="8" rx="2" fill="#F5D77A" {W(1.8)}/><rect x="40" y="60" width="9" height="8" rx="2" fill="#F5D77A" {W(1.8)}/>
<rect x="54" y="63" width="9" height="8" rx="2" fill="#A35A2E" {W(1.8)}/><circle cx="34" cy="72" r="2.4" fill="#5DAE47"/><circle cx="62" cy="70" r="2" fill="#E2483A"/>
{face(44, 84, d=8, k=0.65)}
''')
SUBJ["cafe-acharuli-vnukovo"] = ("оджахури — жареная картошка с мясом в глиняной сковородке",
                                 "едет на багажной тележке аэропорта рядом с бирюзовым чемоданом")

# 14. Н'джой (Окская) — кусок торта Наполеон в праздничном колпаке дудит в дудочку-язычок
ICONS["cafe-ndzhoy-okskaya"] = svg("f_party", f'''
<path d="M22 104 H106" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".7"/>
<path d="M26 98 L64 54 L104 98Z" fill="#F7E3B5" {s()}/>
<path d="M30 92 H100 M38 82 H92 M46 72 H82" stroke="#C88A3E" stroke-width="3"/>
<path d="M26 98 H104 V104 H26Z" fill="#E7C27A" {W(2.4)}/>
<path d="M50 56 L64 22 L78 56Z" fill="#7B6CD9" {s()}/>
<circle cx="56" cy="44" r="2.4" fill="#FFE27A"/><circle cx="70" cy="40" r="2.4" fill="#FFE27A"/><circle cx="64" cy="20" r="5" fill="#F2506A" {W(2.2)}/>
<circle cx="56" cy="64" r="1.5" fill="#fff"/><circle cx="72" cy="66" r="1.5" fill="#fff"/><circle cx="64" cy="60" r="1.5" fill="#fff"/>
{eye(56, 80, 0.7)}{eye(72, 80, 0.7)}
<path d="M64 88 L84 82" stroke="#F2506A" stroke-width="5" stroke-linecap="round"/>
<path d="M84 82 Q102 74 110 82 Q102 86 98 94 Q92 88 84 82Z" fill="#4FB3D9" {W(2.2)}/>
{sparkle(20, 40, 5)}{sparkle(108, 46, 4)}
''')
SUBJ["cafe-ndzhoy-okskaya"] = ("кусок торта Наполеон с хрустящими слоями крема",
                               "в фиолетовом праздничном колпаке дудит в дудочку-язычок на детском празднике")

# 15. Игрёнок (Одинцово) — сырная гренка лезет по канатной сетке игрового лабиринта
ICONS["cafe-igrenok-odintsovo"] = svg("f_maze", f'''
<path d="M18 14 V120 M110 14 V120" stroke="#E2483A" stroke-width="7" stroke-linecap="round"/>
<path d="M18 14 H110" stroke="#FFC23A" stroke-width="7" stroke-linecap="round"/>
<path d="M24 34 H104 M24 58 H104 M24 82 H104 M24 106 H104 M38 20 V118 M58 20 V118 M78 20 V118 M96 20 V118"
 stroke="#FFFFFF" stroke-width="3" opacity=".9"/>
<path d="M24 34 H104 M24 58 H104 M24 82 H104 M24 106 H104 M38 20 V118 M58 20 V118 M78 20 V118 M96 20 V118"
 stroke="#2F7FA0" stroke-width="1.2" opacity=".6"/>
<rect x="44" y="50" width="40" height="40" rx="8" fill="#F2BE5C" {s()}/>
<path d="M44 58 Q56 54 64 60 Q74 54 84 60" fill="none" stroke="#FFE38A" stroke-width="5" stroke-linecap="round"/>
<rect x="48" y="62" width="32" height="24" rx="5" fill="#F7D98C" opacity=".6"/>
{face(64, 72, d=7, k=0.7)}
<path d="M44 60 L36 50 M84 60 L94 48 M50 90 L44 102 M78 90 L84 102" stroke="{O}" stroke-width="3.6" stroke-linecap="round"/>
''')
SUBJ["cafe-igrenok-odintsovo"] = ("квадратная сырная гренка с тянущимся сыром",
                                  "карабкается по канатной сетке детского игрового лабиринта")

# 16. Хачапури (Рязанский пр-т) — бадриджани делает стойку на руках на тарелке
ICONS["cafe-khachapuri-ryazansky"] = svg("f_aubergine", f'''
<ellipse cx="64" cy="108" rx="46" ry="10" fill="#fff" {s()}/>
<ellipse cx="64" cy="106" rx="32" ry="5" fill="#EFE9F7"/>
<g transform="rotate(-12 64 64)">
<path d="M48 26 Q40 64 52 100 H76 Q88 64 80 26 Q64 16 48 26Z" fill="#7A3E9D" {s()}/>
<path d="M54 34 Q48 64 56 94 H72 Q80 64 74 34Z" fill="#F5EFD8" {W(2.2)}/>
<path d="M58 44 Q64 50 70 44 M57 58 Q64 64 71 58" fill="none" stroke="#C9B37A" stroke-width="2.4"/>
<circle cx="62" cy="50" r="2.2" fill="#E2483A"/><circle cx="68" cy="62" r="2.2" fill="#E2483A"/><circle cx="60" cy="68" r="1.8" fill="#7FBF5A"/>
<path d="M50 26 Q56 14 64 18 Q72 14 78 26" fill="none" stroke="#2F7D3B" stroke-width="5" stroke-linecap="round"/>
</g>
{face(66, 80, d=6, k=0.6)}
<path d="M50 98 L44 104 M80 96 L86 104" stroke="{O}" stroke-width="4" stroke-linecap="round"/>
{sparkle(24, 32, 5)}{sparkle(104, 28, 4)}
''')
SUBJ["cafe-khachapuri-ryazansky"] = ("бадриджани — фиолетовый рулетик баклажана с ореховой начинкой и гранатом",
                                     "делает стойку на руках на белой тарелке, хвостик-зелень сверху")

# 17. Терраса (Россошанская) — ромбик пахлавы загорает на летней террасе
ICONS["cafe-terrasa-rossoshanskaya"] = svg("f_terrace", f'''
<path d="M8 22 H120 L112 42 H16Z" fill="#fff" {s()}/>
<path d="M22 22 L20 42 M42 22 V42 M64 22 V42 M86 22 V42 M106 22 L108 42" stroke="#3FA36B" stroke-width="7"/>
<path d="M16 42 Q22 50 28 42 Q34 50 40 42 Q46 50 52 42 Q58 50 64 42 Q70 50 76 42 Q82 50 88 42 Q94 50 100 42 Q106 50 112 42" fill="#fff" {W(2.2)}/>
<rect x="0" y="104" width="128" height="30" fill="#C99A5A"/>
<path d="M0 104 H128 M30 104 V128 M70 104 V128 M106 104 V128" stroke="#A97A3E" stroke-width="2.4"/>
<path d="M64 52 L98 80 L64 108 L30 80Z" fill="#E7A646" {s()}/>
<path d="M40 80 L64 60 L88 80 M44 86 L64 70 L84 86" fill="none" stroke="#C7832A" stroke-width="2"/>
<circle cx="64" cy="64" r="5" fill="#8BC34A" {W(2)}/>
<path d="M50 74 h10 v4 h-10z M68 74 h10 v4 h-10z" fill="{O}"/><path d="M60 76 h8" stroke="{O}" stroke-width="2"/>
<path d="M58 90 Q64 95 70 90" fill="none" {W(2.4)}/>
''')
SUBJ["cafe-terrasa-rossoshanskaya"] = ("ромбик медовой пахлавы с фисташкой на макушке",
                                       "загорает в тёмных очках на летней террасе под зелёно-белым тентом")

if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for pid in ids:
        open(os.path.join(OUT, f"{pid}.svg"), "w").write(ICONS[pid])
    path = os.path.join(OUT, "subjects.txt")
    lines = [l for l in open(path, encoding="utf-8").read().splitlines() if l.split(" — ")[0] not in ICONS]
    lines += [f"{pid} — герой: {h} | сцена: {sc}" for pid, (h, sc) in SUBJ.items()]
    open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("svg:", len(ids))
