"""Иконки робота cafes, 2026-11-09. Правило АБСОЛЮТНОЙ уникальности: каждая придумана и нарисована отдельно
(свой герой по кухне/названию, своя сцена, своя компоновка и палитра фона). Сверено с icons-src/subjects.txt.
Запуск: python3 tools/icons_cafes_1109.py [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "i9_street": ("#FFF8EC", "#E9B98A"),
    "i9_rain": ("#E3EEF7", "#7FA6C9"),
    "i9_retro": ("#FFF1D0", "#E8B54A"),
    "i9_thai": ("#FDFBE0", "#B7CE4E"),
    "i9_mill": ("#F6ECFF", "#9F84CF"),
    "i9_lab": ("#E6FFFB", "#4FBFB3"),
    "i9_field": ("#F2FAFF", "#7CB7E8"),
    "i9_terra": ("#FFEBDD", "#D9774A"),
    "i9_aegean": ("#F3FBFF", "#2F8FD0"),
    "i9_vine": ("#F6F0E2", "#8E9C4A"),
})

# 1. Дом 8а — почтовый ящик «8а», из щели высовывается горячий пирожок
ICONS["cafe-dom-8a-alabyana"] = svg("i9_street", f'''
<rect x="58" y="92" width="12" height="40" fill="#7A8796" {s()}/>
<path d="M26 50 Q26 30 46 30 H82 Q102 30 102 50 V96 H26Z" fill="#3E7FD9" {s()}/>
<path d="M26 50 Q26 30 46 30 Q64 30 64 50 V96" fill="none" {W(2.4)}/>
<rect x="72" y="70" width="22" height="14" rx="3" fill="#FFF7E0" {W(2.2)}/>
<text x="83" y="81" font-family="Arial" font-weight="bold" font-size="11" text-anchor="middle" fill="{O}">8а</text>
<path d="M32 58 H94" {W(2.4)}/>
<path d="M30 60 Q22 36 46 32 Q72 30 86 50 Q74 64 50 64 Q34 64 30 60Z" fill="#E9A24E" {s()}/>
<path d="M44 40 q4 4 8 0 q4 4 8 0 q4 4 8 0" fill="none" stroke="#B86E2A" stroke-width="2.4" stroke-linecap="round"/>
{face(54, 50, d=8, k=0.8)}
<path d="M44 26 q-4 -6 0 -12 M56 24 q-4 -6 0 -12 M68 26 q-4 -6 0 -12" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M104 46 V22 L118 26 L104 32" fill="#E8304A" {W(2.2)}/>
''')
SUBJ["cafe-dom-8a-alabyana"] = ("синий уличный почтовый ящик с табличкой «8а»",
                               "из щели для писем высовывается горячий румяный пирожок с глазками, от него идёт пар")

# 2. Додо Пицца (Воронежская) — пицца-зонтик над оливкой под томатным дождиком
ICONS["cafe-dodo-voronezhskaya"] = svg("i9_rain", f'''
<g fill="#E8443A" {W(1.6)}><path d="M18 20 q-3 6 0 8 q3 -2 0 -8z"/><path d="M104 14 q-3 6 0 8 q3 -2 0 -8z"/><path d="M112 40 q-3 6 0 8 q3 -2 0 -8z"/><path d="M12 48 q-3 6 0 8 q3 -2 0 -8z"/></g>
<path d="M14 64 Q64 2 114 64 Q104 58 94 64 Q84 58 74 64 Q64 58 54 64 Q44 58 34 64 Q24 58 14 64Z" fill="#F9C94A" {s()}/>
<path d="M20 60 Q64 10 108 60" fill="none" stroke="#E07A2E" stroke-width="5" opacity=".6"/>
<g fill="#D8432F" {W(2)}><circle cx="44" cy="40" r="6"/><circle cx="66" cy="28" r="6"/><circle cx="86" cy="42" r="6"/><circle cx="56" cy="52" r="5"/><circle cx="78" cy="56" r="5"/></g>
<path d="M64 62 V104 Q64 112 56 112 Q50 112 50 106" fill="none" stroke="#8A5A34" stroke-width="5" stroke-linecap="round"/>
<path d="M64 62 V104 Q64 112 56 112 Q50 112 50 106" fill="none" {W(1.6)}/>
<ellipse cx="84" cy="96" rx="16" ry="20" fill="#3D4A2E" {s()}/>
<ellipse cx="84" cy="80" rx="5" ry="3" fill="#C9352E" {W(1.8)}/>
{face(84, 96, d=6, k=0.7)}
<path d="M10 120 H118" stroke="#9BC0DE" stroke-width="5" stroke-linecap="round"/>
''')
SUBJ["cafe-dodo-voronezhskaya"] = ("пицца пепперони, раскрытая как зонтик на ручке",
                                  "укрывает маленькую чёрную оливку-малыша от дождика из томатных капель")

# 3. Алло! Пицца — ретро-телефон, у которого диск — пицца
ICONS["cafe-allo-pizza-tkatskaya"] = svg("i9_retro", f'''
<path d="M24 34 Q22 22 36 22 H92 Q106 22 104 34 L98 40 Q92 36 86 40 L82 34 H46 L42 40 Q36 36 30 40Z" fill="#E8304A" {s()}/>
<path d="M30 112 L38 52 Q40 44 50 44 H78 Q88 44 90 52 L98 112Z" fill="#E8304A" {s()}/>
<circle cx="64" cy="82" r="24" fill="#F2B24A" {s()}/>
<circle cx="64" cy="82" r="19" fill="#FFD966" {W(2)}/>
<g fill="#C9352E" {W(1.6)}><circle cx="64" cy="66" r="4"/><circle cx="78" cy="74" r="4"/><circle cx="76" cy="92" r="4"/><circle cx="52" cy="92" r="4"/><circle cx="50" cy="74" r="4"/></g>
{face(64, 80, d=6, k=0.65)}
<path d="M98 30 q12 10 6 26 q-6 14 4 22" fill="none" stroke="#3B3355" stroke-width="2.6" stroke-dasharray="1 5" stroke-linecap="round"/>
<path d="M14 16 l6 4 M10 26 l7 1 M114 14 l-6 5" {W(2.6)}/>
''')
SUBJ["cafe-allo-pizza-tkatskaya"] = ("красный дисковый телефон, у которого вместо номеронабирателя — пицца с глазками",
                                    "трубка подпрыгивает над корпусом — телефон звонит, принимает заказ")

# 4. Лемонграсс — три шпажки куриного сатая с арахисовым соусом
ICONS["cafe-lemongrass-mironovskaya"] = svg("i9_thai", f'''
<ellipse cx="64" cy="104" rx="50" ry="12" fill="#fff" {s()}/>
<ellipse cx="94" cy="100" rx="14" ry="6" fill="#C98A3E" {W(2.4)}/>
<path d="M86 98 q8 -3 16 0" fill="none" stroke="#8A5A2A" stroke-width="2"/>
<g>
<path d="M20 104 L96 24" stroke="#D9B47A" stroke-width="4" stroke-linecap="round"/>
<path d="M30 102 L106 30" stroke="#D9B47A" stroke-width="4" stroke-linecap="round"/>
<path d="M14 96 L84 18" stroke="#D9B47A" stroke-width="4" stroke-linecap="round"/>
</g>
<g fill="#C9762E" {W(2.4)}>
<rect x="30" y="58" width="16" height="16" rx="5" transform="rotate(-45 38 66)"/>
<rect x="44" y="44" width="16" height="16" rx="5" transform="rotate(-45 52 52)"/>
<rect x="58" y="30" width="16" height="16" rx="5" transform="rotate(-45 66 38)"/>
<rect x="54" y="68" width="16" height="16" rx="5" transform="rotate(-45 62 76)"/>
<rect x="68" y="54" width="16" height="16" rx="5" transform="rotate(-45 76 62)"/>
<rect x="82" y="40" width="16" height="16" rx="5" transform="rotate(-45 90 48)"/>
</g>
{face(64, 62, d=7, k=0.75)}
<path d="M18 36 q6 -8 14 -4 M100 82 q8 -4 12 2" fill="none" stroke="#6FA63A" stroke-width="3" stroke-linecap="round"/>
''')
SUBJ["cafe-lemongrass-mironovskaya"] = ("три шпажки тайского куриного сатая крест-накрест",
                                       "лежат на белой тарелке рядом с лужицей арахисового соуса, средний кусочек улыбается")

# 5. Стачка (Орехово-Зуево) — ткацкая катушка, намотанная спагетти
ICONS["cafe-stachka-orekhovo"] = svg("i9_mill", f'''
<rect x="0" y="104" width="128" height="26" fill="#F3E6FF"/>
<path d="M0 104 H128" {W(2.4)}/>
<path d="M0 112 H128 M0 120 H128 M16 104 V130 M48 104 V130 M80 104 V130 M112 104 V130" stroke="#C9A8F0" stroke-width="2"/>
<rect x="34" y="22" width="60" height="12" rx="4" fill="#B97A44" {s()}/>
<rect x="34" y="92" width="60" height="12" rx="4" fill="#B97A44" {s()}/>
<rect x="40" y="34" width="48" height="58" fill="#F6D06A" {s()}/>
<g fill="none" stroke="#E2A93A" stroke-width="2.2"><path d="M40 42 H88 M40 50 H88 M40 58 H88 M40 66 H88 M40 74 H88 M40 82 H88"/></g>
<path d="M54 60 q6 -6 12 0 q4 6 -4 8 q-8 0 -8 -8z" fill="#D8432F" {W(1.8)}/>
{face(64, 70, d=10, k=0.8)}
<path d="M88 84 Q104 86 104 100 Q104 112 92 114 Q82 116 84 124" fill="none" stroke="#F6D06A" stroke-width="4" stroke-linecap="round"/>
<path d="M88 84 Q104 86 104 100 Q104 112 92 114 Q82 116 84 124" fill="none" {W(1.4)}/>
''')
SUBJ["cafe-stachka-orekhovo"] = ("деревянная ткацкая катушка, намотанная спагетти вместо ниток, с капелькой томатного соуса",
                                "стоит на лиловой клетчатой скатерти, а кончик макаронины свисает и вьётся по столу")

# 6. IQ кафе (Долгопрудный) — колба с какао и маршмеллоу-пузырями
ICONS["cafe-iq-dolgoprudny"] = svg("i9_lab", f'''
<path d="M22 112 H106" {W(4)}/>
<path d="M30 112 V104 M98 112 V104" {W(3)}/>
<path d="M52 18 H76 M56 18 V50 L28 100 Q24 110 36 110 H92 Q104 110 100 100 L72 50 V18" fill="#EFFFFC" fill-opacity=".9" {s()}/>
<path d="M44 74 H84 L98 100 Q102 108 92 108 H36 Q26 108 30 100Z" fill="#8A5234" {W(2)}/>
{face(64, 90, d=9, k=0.85)}
<g fill="#fff" {W(2)}><rect x="54" y="64" width="9" height="9" rx="3"/><rect x="66" y="58" width="9" height="9" rx="3"/><rect x="60" y="40" width="8" height="8" rx="3"/><rect x="58" y="22" width="9" height="9" rx="3" fill="#FFD3E2"/></g>
<text x="100" y="40" font-family="Arial" font-weight="bold" font-size="14" text-anchor="middle" fill="{O}">IQ</text>
{sparkle(20, 36, 5)}{sparkle(108, 64, 4)}
''')
SUBJ["cafe-iq-dolgoprudny"] = ("химическая колба, полная горячего какао",
                              "бурлит в лаборатории, из горлышка вылетают пузыри-зефирки, рядом надпись «IQ»")

# 7. Васильки (Жуковский) — торт с синими кремовыми васильками в поле
ICONS["cafe-vasilki-zhukovsky"] = svg("i9_field", f'''
<path d="M0 104 Q64 92 128 104 V130 H0Z" fill="#B9DA7A" {W(2.4)}/>
<g {W(1.6)} fill="#3B6FD8"><circle cx="14" cy="100" r="4"/><circle cx="112" cy="102" r="4"/><circle cx="24" cy="114" r="3.5"/><circle cx="104" cy="116" r="3.5"/></g>
<rect x="28" y="62" width="72" height="42" rx="6" fill="#FFF3E2" {s()}/>
<rect x="34" y="40" width="60" height="26" rx="6" fill="#FFF3E2" {s()}/>
<path d="M28 74 Q36 80 44 74 Q52 80 60 74 Q68 80 76 74 Q84 80 92 74 Q96 78 100 74" fill="none" stroke="#9EC3F2" stroke-width="3"/>
<g {W(1.6)}>
<g fill="#3B6FD8"><circle cx="44" cy="38" r="5"/><circle cx="64" cy="34" r="6"/><circle cx="84" cy="38" r="5"/></g>
<g fill="#fff"><circle cx="44" cy="38" r="1.6"/><circle cx="64" cy="34" r="2"/><circle cx="84" cy="38" r="1.6"/></g>
</g>
<path d="M40 40 l-4 -4 M48 40 l4 -4 M60 30 l-4 -4 M68 30 l4 -4 M80 40 l-4 -4 M88 40 l4 -4" stroke="#3B6FD8" stroke-width="3" stroke-linecap="round"/>
{face(64, 88, d=11, k=0.85)}
''')
SUBJ["cafe-vasilki-zhukovsky"] = ("двухъярусный белый торт, украшенный синими кремовыми васильками",
                                 "стоит прямо в летнем поле среди настоящих васильков под голубым небом")

# 8. Мясорубка (Пушкино) — фаршированный перец в рисовой шапочке
ICONS["cafe-myasorubka-pushkino"] = svg("i9_terra", f'''
<ellipse cx="64" cy="108" rx="44" ry="10" fill="#FFF6EC" {s()}/>
<ellipse cx="64" cy="106" rx="30" ry="5" fill="#E2683E" opacity=".7"/>
<path d="M36 52 Q30 98 50 104 Q64 108 78 104 Q98 98 92 52Z" fill="#E8443A" {s()}/>
<path d="M48 58 Q44 84 52 100" fill="none" stroke="#B82A2A" stroke-width="3"/>
<path d="M80 58 Q84 84 76 100" fill="none" stroke="#B82A2A" stroke-width="3"/>
<path d="M34 54 Q38 34 64 34 Q90 34 94 54 Q64 62 34 54Z" fill="#FFFDF4" {s()}/>
<g fill="#EDE6D4"><ellipse cx="50" cy="44" rx="3" ry="1.6"/><ellipse cx="62" cy="40" rx="3" ry="1.6"/><ellipse cx="76" cy="44" rx="3" ry="1.6"/><ellipse cx="70" cy="50" rx="3" ry="1.6"/></g>
<path d="M64 34 Q62 22 70 16" fill="none" stroke="#3E8A3A" stroke-width="5" stroke-linecap="round"/>
<path d="M64 34 Q62 22 70 16" fill="none" {W(1.6)}/>
<path d="M76 24 q8 -4 12 4 q-8 4 -12 -4z" fill="#7CC36A" {W(1.8)}/>
{face(64, 76, d=10, k=0.9)}
''')
SUBJ["cafe-myasorubka-pushkino"] = ("запечённый красный фаршированный перец с белой рисовой начинкой-шапочкой",
                                   "стоит на тарелке в лужице томатного соуса, хвостик-веточка торчит как перо")

# 9. Пита&Сувлаки — гирос в пите кульком
ICONS["cafe-pita-souvlaki-samotechnaya"] = svg("i9_aegean", f'''
<path d="M0 98 Q32 92 64 98 T128 98 V130 H0Z" fill="#2F8FD0" {W(2.4)}/>
<path d="M0 108 Q32 102 64 108 T128 108" fill="none" stroke="#fff" stroke-width="3" opacity=".6"/>
<rect x="98" y="30" width="14" height="70" fill="#fff" {W(2.4)}/>
<rect x="94" y="24" width="22" height="8" fill="#fff" {W(2.4)}/>
<path d="M102 36 V94 M108 36 V94" stroke="#C8D8E6" stroke-width="2"/>
<path d="M30 40 Q64 26 90 40 L64 116Z" fill="#F4D49A" {s()}/>
<path d="M32 42 Q40 30 50 36 Q56 24 66 32 Q76 24 82 34 Q90 32 88 42" fill="#9A5A32" {W(2.2)}/>
<path d="M36 40 q6 -6 12 0 M60 34 q6 -4 10 2" fill="none" stroke="#5FAE4E" stroke-width="4" stroke-linecap="round"/>
<g fill="#E8443A" {W(1.6)}><circle cx="46" cy="34" r="3.5"/><circle cx="76" cy="34" r="3.5"/></g>
<path d="M34 46 Q62 56 88 46" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
{face(62, 66, d=8, k=0.8)}
<path d="M44 74 L84 74" stroke="#D9B47A" stroke-width="2" opacity=".7"/>
''')
SUBJ["cafe-pita-souvlaki-samotechnaya"] = ("греческий гирос в пите, свёрнутой кульком, с мясом, помидором и соусом дзадзики",
                                         "стоит на берегу синего моря у белой античной колонны")

# 10. Qvevri (Жулебино) — мцвади на шампуре-лозе
ICONS["cafe-qvevri-privolnaya"] = svg("i9_vine", f'''
<path d="M8 96 Q40 76 64 62 Q90 46 120 30" fill="none" stroke="#6E4A2A" stroke-width="6" stroke-linecap="round"/>
<path d="M8 96 Q40 76 64 62 Q90 46 120 30" fill="none" {W(1.6)}/>
<path d="M108 26 q10 -14 20 -6 q-6 12 -20 6z" fill="#7FB05A" {W(2)}/>
<path d="M14 84 q-12 -4 -10 -16 q12 2 10 16z" fill="#7FB05A" {W(2)}/>
<path d="M118 34 q4 8 -2 12" fill="none" stroke="#6E4A2A" stroke-width="2"/>
<g {W(2.4)}>
<ellipse cx="36" cy="80" rx="13" ry="11" fill="#9A4A2A"/>
<ellipse cx="62" cy="64" rx="15" ry="13" fill="#A85430"/>
<ellipse cx="90" cy="48" rx="13" ry="11" fill="#9A4A2A"/>
</g>
<path d="M30 76 l6 2 M86 44 l6 2 M28 84 l5 1" stroke="#5A2618" stroke-width="2.4" stroke-linecap="round"/>
<g fill="#F3F0E0" {W(1.4)}><path d="M48 52 q4 -6 8 0z"/><path d="M76 38 q4 -6 8 0z"/><path d="M22 70 q4 -6 8 0z"/></g>
{face(62, 64, d=7, k=0.75)}
<g fill="#7A3B8E" {W(1.4)}><circle cx="34" cy="106" r="5"/><circle cx="44" cy="106" r="5"/><circle cx="39" cy="114" r="5"/><circle cx="49" cy="114" r="5"/><circle cx="44" cy="122" r="5"/></g>
<path d="M66 108 q8 -10 16 0 q-8 6 -16 0z" fill="none" stroke="#E07A2E" stroke-width="3"/>
''')
SUBJ["cafe-qvevri-privolnaya"] = ("три сочных куска грузинского мцвади на шампуре из виноградной лозы",
                                 "шампур-лоза наискосок с живыми листиками на концах, внизу гроздь тёмного винограда")

draw_icons.BG.update({
    "i9_zaton": ("#E8FAFF", "#3E9FB8"),
    "i9_cream": ("#FFF6EE", "#D9A27A"),
    "i9_runway": ("#EEF3FA", "#8C9DB8"),
    "i9_xmas": ("#E9F6EF", "#3E8A62"),
    "i9_clay": ("#FFF2E2", "#C8935E"),
    "i9_drum": ("#FFF0F6", "#E06A9A"),
    "i9_uzbek": ("#E9F0FF", "#4A6FD0"),
    "i9_tokyo": ("#FFF9E8", "#F0C84A"),
})

# 11. Пронто (Новинки, Нагатинский затон) — пицца-штурвал над волнами
ICONS["cafe-pronto-novinki"] = svg("i9_zaton", f'''
<path d="M0 100 Q16 92 32 100 T64 100 T96 100 T128 100 V130 H0Z" fill="#2F86B8" {W(2.4)}/>
<path d="M0 112 Q16 104 32 112 T64 112 T96 112 T128 112" fill="none" stroke="#fff" stroke-width="3" opacity=".6"/>
<g stroke="#C98A4E" stroke-width="8" stroke-linecap="round">
<path d="M64 14 V28 M64 92 V106 M14 60 H28 M100 60 H114 M29 25 L38 34 M90 86 L99 95 M99 25 L90 34 M38 86 L29 95"/></g>
<g {W(1.6)} fill="none"><path d="M64 14 V28 M64 92 V106 M14 60 H28 M100 60 H114"/></g>
<circle cx="64" cy="60" r="36" fill="#F2B24A" {s()}/>
<circle cx="64" cy="60" r="29" fill="#FFD966" {W(2)}/>
<g fill="#5FAE4E" {W(1.4)}><path d="M48 44 q4 -6 8 0 q-4 4 -8 0z"/><path d="M78 76 q4 -6 8 0 q-4 4 -8 0z"/></g>
<g fill="#C9352E" {W(1.6)}><circle cx="78" cy="44" r="5"/><circle cx="46" cy="74" r="5"/></g>
{face(64, 60, d=9, k=0.85)}
<path d="M104 18 q4 -4 8 0 q4 -4 8 0" fill="none" {W(2.2)}/>
''')
SUBJ["cafe-pronto-novinki"] = ("пицца-штурвал с деревянными рукоятками по кругу",
                               "крутится над волнами Нагатинского затона, а вдалеке летит чайка")

# 12. Котокафе (Лобня) — кошка-калико свернулась в чашке капучино
ICONS["cafe-kotokafe-lobnya"] = svg("i9_cream", f'''
<ellipse cx="62" cy="110" rx="46" ry="9" fill="#fff" {s()}/>
<path d="M22 64 H100 Q100 106 62 106 Q22 106 22 64Z" fill="#7FC6E8" {s()}/>
<path d="M100 72 Q118 72 116 86 Q114 98 98 94" fill="none" stroke="#7FC6E8" stroke-width="7"/>
<path d="M100 72 Q118 72 116 86 Q114 98 98 94" fill="none" {W(2)}/>
<ellipse cx="61" cy="64" rx="39" ry="9" fill="#E9D2B0" {W(2.6)}/>
<path d="M30 64 Q30 40 60 38 Q92 38 92 62Z" fill="#fff" {s()}/>
<path d="M30 60 Q34 44 46 42 Q50 52 40 62Z" fill="#F29A3A"/>
<path d="M72 40 Q90 42 92 58 Q80 56 74 48Z" fill="#3B3355"/>
<path d="M30 64 Q30 40 60 38 Q92 38 92 62" fill="none" {s()}/>
<path d="M40 44 L36 26 L52 38Z" fill="#F29A3A" {W(2.6)}/>
<path d="M68 38 L80 24 L82 42Z" fill="#3B3355" {W(2.6)}/>
<path d="M44 52 q5 -4 10 0 M64 52 q5 -4 10 0" fill="none" {W(2.4)}/>
<path d="M57 58 l2 2 l2 -2" fill="#FF7FA8" {W(1.6)}/>
<path d="M28 56 l-10 -2 M28 60 l-10 2 M92 56 l10 -2 M92 60 l10 2" {W(1.6)}/>
<path d="M88 62 Q104 58 104 44" fill="none" stroke="#F29A3A" stroke-width="7" stroke-linecap="round"/>
<path d="M58 84 q-6 -6 0 -10 q6 4 0 10z M58 84 q6 -6 0 -10" fill="#fff" opacity=".8"/>
''')
SUBJ["cafe-kotokafe-lobnya"] = ("трёхцветная кошка-калико с рыжим и чёрным ушком",
                               "сладко спит, свернувшись в голубой чашке капучино на блюдце")

# 13. Якитория (Лобня, рядом Шереметьево) — мисо-суп под крылом самолёта
ICONS["cafe-yakitoriya-lobnya"] = svg("i9_runway", f'''
<path d="M10 32 L92 22 Q106 20 108 26 Q106 32 92 32 L58 36 L40 50 L32 50 L42 36 L10 36Z" fill="#fff" {W(2.4)}/>
<path d="M14 28 L8 20 L16 20 L22 30" fill="#E8304A" {W(2)}/>
<circle cx="70" cy="28" r="1.6" fill="{O}"/><circle cx="78" cy="27" r="1.6" fill="{O}"/><circle cx="86" cy="26" r="1.6" fill="{O}"/>
<rect x="0" y="112" width="128" height="18" fill="#6B7487"/>
<path d="M8 120 H24 M40 120 H56 M72 120 H88 M104 120 H120" stroke="#fff" stroke-width="3"/>
<path d="M24 66 H104 Q102 110 64 110 Q26 110 24 66Z" fill="#C8243A" {s()}/>
<ellipse cx="64" cy="66" rx="40" ry="9" fill="#E8C27A" {W(2.6)}/>
<g fill="#FFFDF2" {W(1.6)}><rect x="40" y="60" width="9" height="9" rx="2"/><rect x="74" y="62" width="9" height="9" rx="2"/></g>
<path d="M56 62 q4 -4 8 0 M86 66 q4 -3 8 0" fill="none" stroke="#5FAE4E" stroke-width="3" stroke-linecap="round"/>
<path d="M30 80 Q64 90 98 80" fill="none" stroke="#1E1A2E" stroke-width="2" opacity=".5"/>
{face(64, 90, d=10, k=0.85)}
<path d="M50 54 q-4 -8 0 -14 M76 54 q-4 -8 0 -14" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
''')
SUBJ["cafe-yakitoriya-lobnya"] = ("мисо-суп в красной лаковой чашке с кубиками тофу и зелёным луком",
                                 "дымится у взлётной полосы, а над ним пролетает белый пассажирский самолёт")

# 14. Додо Пицца (Клин, город Чайковского) — Щелкунчик с кусочком пиццы
ICONS["cafe-dodo-klin"] = svg("i9_xmas", f'''
<path d="M0 116 Q64 104 128 116 V130 H0Z" fill="#fff" {W(2.4)}/>
{sparkle(18, 30, 4)}{sparkle(110, 24, 5)}{sparkle(108, 84, 3)}
<rect x="44" y="18" width="40" height="20" rx="4" fill="#3B3355" {s()}/>
<rect x="44" y="34" width="40" height="6" fill="#F2C14A" {W(2)}/>
<rect x="46" y="40" width="36" height="28" rx="6" fill="#FFD9BE" {s()}/>
<path d="M46 60 Q64 74 82 60 V70 H46Z" fill="#fff" {W(2.4)}/>
<path d="M54 56 q10 -6 20 0" fill="none" {W(3)}/>
{eye(56, 48, 0.8)}{eye(72, 48, 0.8)}
<path d="M44 70 H84 V106 H44Z" fill="#D8343A" {s()}/>
<path d="M64 70 V106 M52 80 h6 M52 90 h6 M70 80 h6 M70 90 h6" {W(2)}/>
<rect x="44" y="96" width="40" height="6" fill="#3B3355"/>
<path d="M50 106 V116 M78 106 V116" stroke="#3B3355" stroke-width="7"/>
<path d="M60 64 L104 52 L100 80Z" fill="#F9C94A" {s()}/>
<path d="M100 52 Q108 64 100 80" fill="none" stroke="#C98A3E" stroke-width="6" stroke-linecap="round"/>
<g fill="#C9352E" {W(1.4)}><circle cx="86" cy="62" r="3.5"/><circle cx="94" cy="70" r="3"/></g>
''')
SUBJ["cafe-dodo-klin"] = ("деревянный Щелкунчик в красном мундире и чёрном кивере",
                          "держит в зубах кусок пиццы пепперони на заснеженной ёлочной сцене")

# 15. Старик Хинкалыч (Дмитров) — шкмерули в глиняной сковородке-кеци
ICONS["cafe-starik-khinkalych-dmitrov"] = svg("i9_clay", f'''
<rect x="8" y="96" width="112" height="22" rx="6" fill="#B07A48" {s()}/>
<path d="M16 104 H112 M16 110 H112" stroke="#8E5C32" stroke-width="2"/>
<ellipse cx="64" cy="80" rx="48" ry="20" fill="#C8643A" {s()}/>
<ellipse cx="64" cy="76" rx="40" ry="14" fill="#FFF6E0" {W(2.4)}/>
<g {W(2.4)}><path d="M36 76 Q38 60 54 62 Q62 66 58 78 Q46 84 36 76Z" fill="#D9883E"/>
<path d="M70 74 Q72 58 88 60 Q96 64 92 76 Q80 82 70 74Z" fill="#D9883E"/></g>
{face(64, 82, d=9, k=0.7)}
<g fill="#7CC36A"><circle cx="50" cy="70" r="1.8"/><circle cx="84" cy="68" r="1.8"/><circle cx="66" cy="70" r="1.8"/></g>
<path d="M100 44 Q92 30 100 22 Q108 30 100 44Z" fill="#FBF7EE" {W(2.2)}/>
<path d="M100 44 Q90 34 94 26 M100 44 Q110 34 106 26" fill="none" {W(1.6)}/>
<path d="M100 22 V14" {W(2.4)}/>
<path d="M30 44 q-4 -8 0 -14 M44 40 q-4 -8 0 -14" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''')
SUBJ["cafe-starik-khinkalych-dmitrov"] = ("шкмерули — курица в сливочно-чесночном соусе в глиняной сковородке-кеци",
                                         "дымится на деревянной доске, рядом стоит головка чеснока")

# 16. Kucher&Conga (Дмитров) — барабан-конга из бочонка, палочки-гриссини
ICONS["cafe-kucher-conga-dmitrov"] = svg("i9_drum", f'''
<path d="M40 40 Q34 80 44 116 H84 Q94 80 88 40Z" fill="#C97A3E" {s()}/>
<path d="M38 60 H90 M40 96 H88" stroke="#7A4A2A" stroke-width="5"/>
<path d="M38 60 H90 M40 96 H88" fill="none" {W(1.4)}/>
<ellipse cx="64" cy="40" rx="24" ry="8" fill="#F6E2B8" {s()}/>
{face(64, 78, d=10, k=0.9)}
<path d="M14 30 L46 36" stroke="#E8C27A" stroke-width="6" stroke-linecap="round"/>
<path d="M114 24 L82 34" stroke="#E8C27A" stroke-width="6" stroke-linecap="round"/>
<path d="M14 30 L46 36 M114 24 L82 34" {W(1.4)}/>
<g fill="#fff"><circle cx="20" cy="31" r="1"/><circle cx="30" cy="33" r="1"/><circle cx="104" cy="27" r="1"/><circle cx="94" cy="30" r="1"/></g>
<path d="M30 16 l4 6 M64 18 v8 M98 12 l-4 6" {W(2.4)}/>
<path d="M18 70 q-6 8 0 14 M110 70 q6 8 0 14" fill="none" {W(2.2)}/>
''')
SUBJ["cafe-kucher-conga-dmitrov"] = ("деревянный бочонок-барабан конга с весёлой мордочкой",
                                    "по нему отбивают ритм две хлебные палочки-гриссини, вокруг разлетаются звуковые волны")

# 17. Сафо (Пролетарский пр-т, чайхана) — узбекские конфеты-подушечки парварда
ICONS["cafe-safo-proletarsky"] = svg("i9_uzbek", f'''
<ellipse cx="64" cy="100" rx="52" ry="16" fill="#fff" {s()}/>
<path d="M20 100 Q64 112 108 100" fill="none" stroke="#3E63C8" stroke-width="3"/>
<g fill="none" stroke="#3E63C8" stroke-width="2.4"><circle cx="30" cy="98" r="3"/><circle cx="98" cy="98" r="3"/><circle cx="64" cy="108" r="3"/></g>
<g {s()}>
<path d="M30 92 L46 70 L62 92Z" fill="#FFF8F0"/>
<path d="M66 92 L82 70 L98 92Z" fill="#FFF8F0"/>
<path d="M46 72 L64 46 L82 72Z" fill="#FFF8F0"/>
</g>
<g stroke="#F2B9C8" stroke-width="2"><path d="M38 82 l6 6 M74 82 l6 6 M56 58 l6 6"/></g>
<g fill="#F7E6A0"><circle cx="40" cy="86" r="1.2"/><circle cx="88" cy="84" r="1.2"/><circle cx="66" cy="54" r="1.2"/></g>
{face(64, 62, d=6, k=0.6)}
{eye(42, 84, 0.5)}{eye(50, 84, 0.5)}{eye(78, 84, 0.5)}{eye(86, 84, 0.5)}
{sparkle(20, 40, 5, "#FFE89A")}{sparkle(106, 34, 4, "#FFE89A")}
''')
SUBJ["cafe-safo-proletarsky"] = ("три белые узбекские конфеты-подушечки парварда пирамидкой",
                                "лежат горкой на белом лягане с синим узором, поблёскивают сахаром")

# 18. Тануки (Каширское ш., 46) — омурайсу с рожицей из кетчупа
ICONS["cafe-tanuki-kashirskoe-46"] = svg("i9_tokyo", f'''
<ellipse cx="64" cy="94" rx="54" ry="20" fill="#fff" {s()}/>
<path d="M22 92 Q20 50 64 46 Q108 50 106 92 Q64 104 22 92Z" fill="#FFD33A" {s()}/>
<path d="M30 70 Q40 58 52 60" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".7"/>
<g stroke="#D8343A" stroke-width="5" stroke-linecap="round" fill="none">
<path d="M48 68 v4 M80 68 v4"/><path d="M50 82 Q64 92 78 82"/></g>
<ellipse cx="40" cy="80" rx="5" ry="3" fill="#FF7FA8" opacity=".6"/><ellipse cx="88" cy="80" rx="5" ry="3" fill="#FF7FA8" opacity=".6"/>
<path d="M20 98 q8 -6 16 0 M92 98 q8 -6 16 0" fill="#F2F0E6" {W(1.6)}/>
<path d="M98 30 l16 -12 M104 34 l16 -10" stroke="#B5834A" stroke-width="4" stroke-linecap="round"/>
''')
SUBJ["cafe-tanuki-kashirskoe-46"] = ("японский омурайсу — жёлтый омлет-подушка на рисе",
                                    "на омлете кетчупом нарисована улыбающаяся рожица, рядом лежат палочки")


if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for i in ids:
        open(os.path.join(OUT, i + ".svg"), "w").write(ICONS[i])
    reg = os.path.join(OUT, "subjects.txt")
    lines = open(reg).read().splitlines()
    have = {l.split(" — ")[0] for l in lines}
    for i in ids:
        h, sc = SUBJ[i]
        line = f"{i} — герой: {h} | сцена: {sc}"
        if i in have:
            lines = [line if l.split(" — ")[0] == i else l for l in lines]
        else:
            lines.append(line)
    open(reg, "w").write("\n".join(lines) + "\n")
    print("svg", len(ids))
