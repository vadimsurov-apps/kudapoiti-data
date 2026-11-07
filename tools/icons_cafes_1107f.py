"""Робот cafes, 2026-11-07 (10 UTC): иконки 36 новых кафе. Каждая придумана и нарисована отдельно
(правило абсолютной уникальности: свой герой, своя сцена, своя компоновка и палитра фона).
Запуск из корня: python3 tools/icons_cafes_1107f.py  → icons-src/<id>.svg + строки в icons-src/subjects.txt"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def W(w):
    return s(f'stroke-width="{w}"')


def svg2(a, b, body, cx="38%", cy="28%"):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
<defs>
 <radialGradient id="g" cx="{cx}" cy="{cy}" r="85%"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></radialGradient>
 <clipPath id="c"><circle cx="64" cy="64" r="61"/></clipPath>
</defs>
<circle cx="64" cy="64" r="61" fill="url(#g)"/>
<g clip-path="url(#c)">{body}</g>
<ellipse cx="44" cy="22" rx="20" ry="7" fill="#fff" opacity=".3"/>
</svg>'''


STEAM = 'fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round"'
I = {}

# 1 Барин и Бараш — кудрявый барашек-официант несёт поднос с дымящимся пловом
I["cafe-barin-barash-kolomna"] = (svg2("#F3FFF0", "#3E8F6A", f'''
<path d="M0 112 H128 V128 H0Z" fill="#2E6E50" opacity=".5"/>
<ellipse cx="54" cy="84" rx="30" ry="26" fill="#FFFFFF" {s()}/>
<g fill="#FFFFFF" {W(2.6)}><circle cx="30" cy="74" r="9"/><circle cx="34" cy="96" r="9"/><circle cx="54" cy="106" r="9"/><circle cx="74" cy="98" r="9"/><circle cx="44" cy="60" r="9"/><circle cx="62" cy="58" r="9"/></g>
<path d="M40 104 V120 M66 104 V120" {W(5)}/>
<ellipse cx="56" cy="80" rx="15" ry="17" fill="#3B3355"/>
<ellipse cx="56" cy="82" rx="12" ry="13" fill="#5A4A6E"/>
<path d="M42 70 Q34 66 32 72 Q36 76 42 74Z M70 70 Q78 66 80 72 Q76 76 70 74Z" fill="#5A4A6E" {W(2)}/>
{eye(51, 79, 0.7)}{eye(61, 79, 0.7)}
<path d="M52 89 Q56 92 60 89" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
<path d="M80 74 Q92 66 100 56" fill="none" {W(5)}/>
<ellipse cx="102" cy="52" rx="22" ry="5" fill="#E8E8F0" {s()}/>
<path d="M86 50 Q86 34 102 32 Q118 34 118 50Z" fill="#F2B544" {W(2.6)}/>
<g fill="#E8642E"><rect x="94" y="40" width="4" height="3" rx="1"/><rect x="104" y="36" width="4" height="3" rx="1"/><rect x="108" y="44" width="4" height="3" rx="1"/></g>
<path d="M96 28 Q92 22 96 16 M106 28 Q102 20 108 12" {STEAM}/>
'''), "герой: кудрявый белый барашек-официант с чёрной мордочкой | сцена: на задних ножках несёт на вытянутом копытце поднос с дымящимся пловом")

# 2 Хорошее кафе — котлетка в пюре-гнёздышке показывает «класс»
I["cafe-khoroshee-kolomna"] = (svg2("#FFF6D8", "#F29A3A", f'''
<ellipse cx="62" cy="96" rx="52" ry="16" fill="#FFFFFF" {s()}/>
<path d="M18 92 Q22 74 40 78 Q46 64 62 70 Q78 62 86 76 Q104 72 106 92 Q62 104 18 92Z" fill="#FFF3C4" {s()}/>
<path d="M30 86 Q36 82 42 86 M74 84 Q80 80 86 84" fill="none" stroke="#E8C870" stroke-width="2"/>
<ellipse cx="60" cy="68" rx="28" ry="20" fill="#B5652E" {s()}/>
<g fill="#7A3E18"><circle cx="44" cy="62" r="1.8"/><circle cx="72" cy="58" r="1.8"/><circle cx="78" cy="70" r="1.8"/><circle cx="50" cy="76" r="1.6"/></g>
{face(60, 66, d=9, k=0.85)}
<path d="M86 66 Q96 64 98 54" fill="none" {W(4)}/>
<rect x="92" y="34" width="14" height="22" rx="6" fill="#FFE27A" {s()}/>
<path d="M96 42 H104 M96 48 H104" stroke="#D9B040" stroke-width="2"/>
<path d="M30 76 L26 86" fill="none" stroke="#3FA34D" stroke-width="4" stroke-linecap="round"/>
{sparkle(112, 26, 7)}
'''), "герой: круглая котлетка в гнёздышке из картофельного пюре | сцена: показывает «класс» большим пальцем-брусочком сливочного масла")

# 3 Житная площадь — каравай-колос на рыночном прилавке
I["cafe-zhitnaya-kolomna"] = (svg2("#FFFBE8", "#C9A04A", f'''
<path d="M6 46 H122 L116 62 H12Z" fill="#E84B3C" {s()}/>
<path d="M30 46 L26 62 M54 46 L52 62 M78 46 L78 62 M102 46 L104 62" stroke="#fff" stroke-width="6"/>
<path d="M14 62 V20 M114 62 V20" {W(4)}/>
<rect x="6" y="100" width="116" height="30" fill="#9A6234" {s()}/>
<path d="M24 102 Q20 70 64 66 Q108 70 104 102Z" fill="#C88A3E" {s()}/>
<path d="M40 82 l6 -6 M56 78 l6 -6 M72 78 l6 -6 M88 82 l6 -6" stroke="#8A5420" stroke-width="3" stroke-linecap="round"/>
<path d="M64 66 V34" stroke="#D8A93A" stroke-width="3"/>
<g fill="#F2C94C" {W(1.6)}><ellipse cx="60" cy="40" rx="3" ry="5" transform="rotate(-25 60 40)"/><ellipse cx="68" cy="40" rx="3" ry="5" transform="rotate(25 68 40)"/><ellipse cx="60" cy="50" rx="3" ry="5" transform="rotate(-25 60 50)"/><ellipse cx="68" cy="50" rx="3" ry="5" transform="rotate(25 68 50)"/><ellipse cx="64" cy="32" rx="3" ry="5"/></g>
{face(64, 90, d=11, k=0.8)}
'''), "герой: ржаной каравай с колоском, воткнутым в макушку | сцена: стоит на прилавке под красно-белым полосатым рыночным навесом")

# 4 ВкусДетства — карамельное яблоко на палочке у Оки
I["cafe-vkus-detstva-korobcheevo"] = (svg2("#E6F7FF", "#7FB8E8", f'''
<path d="M0 96 Q32 88 64 96 Q96 104 128 96 V128 H0Z" fill="#4A8FD0" {s()}/>
<path d="M10 108 Q20 104 30 108 M70 112 Q80 108 90 112" fill="none" stroke="#BFE4FF" stroke-width="2.4" stroke-linecap="round"/>
<path d="M0 84 Q30 74 64 82 L64 96 Q32 88 0 96Z" fill="#7CC46A"/>
<path d="M64 100 L64 66" stroke="#E8C9A0" stroke-width="5" stroke-linecap="round"/>
<path d="M64 100 L64 66" {W(1.6)}/>
<path d="M64 26 Q36 20 34 48 Q34 74 64 74 Q94 74 94 48 Q92 20 64 26Z" fill="#E8302E" {s()}/>
<path d="M36 50 Q64 58 92 50 Q94 64 80 72 Q64 78 48 72 Q34 64 36 50Z" fill="#B8781E" opacity=".9"/>
<path d="M40 58 L38 66 M54 62 L53 72 M76 62 L77 72 M88 56 L90 64" stroke="#B8781E" stroke-width="3" stroke-linecap="round"/>
<path d="M64 26 Q66 16 72 12" fill="none" {W(3)}/>
<path d="M68 18 Q80 10 86 18 Q76 24 68 18Z" fill="#4CB050" {W(2)}/>
<ellipse cx="48" cy="36" rx="6" ry="9" fill="#fff" opacity=".45"/>
{face(64, 44, d=10, k=0.75)}
'''), "герой: красное яблоко в карамельной глазури на палочке | сцена: воткнуто в зелёный берег над синей рекой Окой, карамель стекает каплями")

# 5 Русский дворик — расписная ложка-хохлома черпает мёд из бочонка
I["cafe-russky-dvorik-sergiev"] = (svg2("#FFF4D6", "#B8322A", f'''
<path d="M22 76 Q20 112 30 120 H86 Q96 112 94 76Z" fill="#C88A48" {s()}/>
<path d="M22 86 H94 M24 108 H92" stroke="#7A4A20" stroke-width="4"/>
<ellipse cx="58" cy="76" rx="36" ry="9" fill="#F6B82A" {s()}/>
<path d="M44 78 Q40 90 46 92 Q50 90 46 78" fill="#F6B82A" {W(2)}/>
<path d="M78 72 L104 22" stroke="#1F1A2E" stroke-width="10" stroke-linecap="round"/>
<path d="M78 72 L104 22" stroke="#D8282E" stroke-width="6" stroke-linecap="round"/>
<ellipse cx="72" cy="74" rx="11" ry="7" transform="rotate(-30 72 74)" fill="#D8282E" {s()}/>
<path d="M90 44 q4 -2 6 2 M96 34 q4 -2 6 2" fill="none" stroke="#F6C64A" stroke-width="2"/>
<circle cx="70" cy="74" r="3" fill="#F6C64A"/>
{eye(96, 30, 0.55)}{eye(102, 33, 0.55)}
<path d="M95 38 Q98 41 101 39" fill="none" {W(1.6)}/>
{face(58, 98, d=11, k=0.75)}
'''), "герой: красно-золотая хохломская ложка с глазками на ручке | сцена: черпает густой мёд из деревянного бочонка, мёд капает обратно")

# 6 Печки & Лавочки — пирожок сидит на деревянной лавочке
I["cafe-pechki-lavochki-sergiev"] = (svg2("#F0FFF4", "#6FBF8A", f'''
<rect x="14" y="86" width="100" height="10" rx="3" fill="#B07A44" {s()}/>
<rect x="14" y="62" width="100" height="10" rx="3" fill="#B07A44" {s()}/>
<path d="M24 96 V118 M104 96 V118 M24 72 V86 M104 72 V86" {W(5)}/>
<path d="M30 88 Q30 52 64 50 Q98 52 98 88Z" fill="#E8A54E" {s()}/>
<path d="M38 60 Q50 54 52 64 Q58 52 64 62 Q72 52 76 64 Q82 54 90 60" fill="none" stroke="#B9702C" stroke-width="3" stroke-linecap="round"/>
{face(64, 74, d=10, k=0.8)}
<path d="M48 88 Q44 100 50 108 M80 88 Q86 100 80 108" fill="none" {W(3.4)}/>
<ellipse cx="50" cy="109" rx="5" ry="3" fill="#E8A54E" {W(2)}/><ellipse cx="80" cy="109" rx="5" ry="3" fill="#E8A54E" {W(2)}/>
<path d="M58 44 Q54 36 60 28 M70 44 Q66 34 72 26" {STEAM}/>
'''), "герой: румяный пирожок с защипами на спинке | сцена: сидит на зелёной садовой лавочке и болтает ножками")

# 7 Валентино — карамельный флан и купидонова стрела-шпажка
I["cafe-valentino-sergiev"] = (svg2("#FFEFF5", "#E05A86", f'''
<ellipse cx="62" cy="100" rx="48" ry="11" fill="#FFFFFF" {s()}/>
<path d="M30 98 L38 56 Q62 48 86 56 L94 98 Q62 106 30 98Z" fill="#FFE29A" {s()}/>
<path d="M38 56 Q62 48 86 56 Q84 66 62 64 Q40 66 38 56Z" fill="#B8641E" {s()}/>
<path d="M44 62 Q42 74 46 76 Q50 72 48 62 M76 62 Q76 70 80 72 Q82 66 80 60" fill="#B8641E"/>
{face(62, 80, d=10, k=0.8)}
<path d="M18 30 L104 70" {W(3)}/>
<path d="M96 60 L108 72 L94 74Z" fill="#9A9AA8" {W(2)}/>
<path d="M18 30 L10 24 M18 30 L12 34 M24 33 L16 27 M24 33 L18 37" stroke="#E05A86" stroke-width="3" stroke-linecap="round"/>
<path d="M100 18 C96 10 86 14 92 24 L100 30 L108 24 C114 14 104 10 100 18Z" fill="#FF5A7E" {W(2)}/>
'''), "герой: карамельный флан с глянцевой шапкой карамели | сцена: на блюдце, и его насквозь пронзила купидонова стрела-шпажка, рядом летит сердечко")

# 8 Байкал — бурятская пельмешка-позы на плоту среди волн
I["cafe-baikal-sergiev"] = (svg2("#E2F6FF", "#2C6FB0", f'''
<path d="M0 50 L22 30 L40 44 L58 22 L80 46 L100 32 L128 52 V60 H0Z" fill="#A8C4E0" {W(2)}/>
<path d="M0 86 Q20 78 40 86 Q60 94 80 86 Q100 78 128 86 V128 H0Z" fill="#1E8FC8" {s()}/>
<path d="M0 104 Q16 98 32 104 Q48 110 64 104 Q80 98 96 104 Q112 110 128 104" fill="none" stroke="#BFE8FF" stroke-width="2.6"/>
<path d="M22 86 H106 L100 96 H28Z" fill="#B88A54" {s()}/>
<path d="M40 86 V96 M64 86 V96 M88 86 V96" stroke="#7A5428" stroke-width="2"/>
<path d="M30 86 Q26 54 64 46 Q102 54 98 86Z" fill="#FFF6E6" {s()}/>
<path d="M44 58 L56 50 M84 58 L72 50 M38 70 L52 56 M90 70 L76 56" stroke="#E2D2B8" stroke-width="2.4" stroke-linecap="round"/>
<ellipse cx="64" cy="49" rx="9" ry="4" fill="#C8783A" {W(2)}/>
<path d="M60 42 Q56 34 62 26 Q58 18 64 12 M70 42 Q74 32 68 24" {STEAM}/>
{face(64, 72, d=11, k=0.8)}
'''), "герой: бурятская позы с дырочкой на макушке | сцена: плывёт на деревянном плотике по синим волнам Байкала, из дырочки валит пар")

# 9 Счастье есть — круассан обнимает чашку какао
I["cafe-schastye-est-sergiev"] = (svg2("#FFF9E8", "#F7C548", f'''
<g fill="#FF8AB0"><circle cx="20" cy="30" r="3"/><circle cx="108" cy="24" r="3"/><rect x="96" y="44" width="5" height="5" transform="rotate(30 98 46)"/></g>
<g fill="#6CC4FF"><circle cx="30" cy="50" r="2.6"/><rect x="18" y="74" width="5" height="5" transform="rotate(20 20 76)"/><circle cx="112" cy="70" r="2.6"/></g>
<path d="M48 70 H82 L78 108 Q76 114 70 114 H60 Q54 114 52 108Z" fill="#7BD3C4" {s()}/>
<ellipse cx="65" cy="70" rx="17" ry="4" fill="#7A4A2E" {W(2)}/>
<path d="M58 62 Q54 56 60 50 M70 62 Q66 54 72 48" {STEAM}/>
<path d="M14 82 Q12 50 40 46 Q46 70 34 92Z" fill="#E8A040" {s()}/>
<path d="M114 82 Q116 50 88 46 Q82 70 94 92Z" fill="#E8A040" {s()}/>
<path d="M34 92 Q24 96 22 88 M94 92 Q104 96 106 88" fill="#E8A040" {W(2.4)}/>
<path d="M22 60 L32 68 M20 72 L30 78 M106 60 L96 68 M108 72 L98 78" stroke="#B8701E" stroke-width="2.4" stroke-linecap="round"/>
<path d="M40 46 Q64 30 88 46 Q76 56 64 54 Q52 56 40 46Z" fill="#F2B656" {s()}/>
{face(64, 44, d=9, k=0.65)}
<path d="M58 92 C54 86 46 88 50 96 L58 102 L66 96 C70 88 62 86 58 92Z" fill="#FF6A8E" {W(1.6)}/>
'''), "герой: золотистый круассан-обнимашка | сцена: крепко обнимает рожками бирюзовую чашку какао с сердечком, вокруг летит конфетти")

# 10 Лесные истории — сковорода с картошкой и лисичками на пеньке
I["cafe-lesnye-istorii-tashirovo"] = (svg2("#EAF7DF", "#2F6B3A", f'''
<path d="M2 70 L16 30 L30 70Z M98 66 L112 20 L126 66Z" fill="#1F5A30" {W(2)}/>
<path d="M30 92 H98 V126 H30Z" fill="#9A6234" {s()}/>
<ellipse cx="64" cy="92" rx="34" ry="9" fill="#E8C48A" {s()}/>
<path d="M50 92 Q64 86 78 92 M56 92 Q64 89 72 92" fill="none" stroke="#B88A50" stroke-width="2"/>
<path d="M100 70 L122 60" stroke="#2A2A36" stroke-width="7" stroke-linecap="round"/>
<ellipse cx="62" cy="74" rx="40" ry="14" fill="#3A3A48" {s()}/>
<ellipse cx="62" cy="70" rx="34" ry="10" fill="#F2C24A"/>
<g fill="#FFD86A" {W(1.6)}><rect x="34" y="64" width="12" height="7" rx="2"/><rect x="72" y="62" width="12" height="7" rx="2"/><rect x="56" y="70" width="12" height="7" rx="2"/></g>
<g fill="#F59A1E" {W(1.8)}><path d="M44 60 Q50 50 56 60 Q52 62 50 70 Q48 62 44 60Z"/><path d="M80 66 Q86 56 92 66 Q88 68 86 74 Q84 68 80 66Z"/><path d="M60 58 Q66 46 72 58 Q68 60 66 68 Q64 60 60 58Z"/></g>
{eye(62, 56, 0.45)}{eye(70, 56, 0.45)}
{face(62, 106, d=11, k=0.75)}
'''), "герой: чугунная сковорода с жареной картошкой и грибами-лисичками | сцена: стоит на широком пеньке среди тёмных елей, лисички выглядывают из картошки")

# 11 Русь — калач качается на верёвке, как на качелях
I["cafe-rus-naro-fominsk"] = (svg2("#FFF0E0", "#C2552E", f'''
<path d="M14 0 L34 64 M114 0 L94 64" stroke="#E8D2A6" stroke-width="3"/>
<path d="M14 0 L34 64 M114 0 L94 64" {W(1.2)}/>
<path d="M34 64 Q64 120 94 64" fill="none" stroke="#E8D2A6" stroke-width="4"/>
<path d="M38 56 C36 6 92 6 90 56" fill="none" stroke="#3B3355" stroke-width="12"/>
<path d="M38 56 C36 6 92 6 90 56" fill="none" stroke="#E3A24A" stroke-width="6.5"/>
<path d="M20 76 Q22 50 64 48 Q106 50 108 76 Q106 98 64 100 Q22 98 20 76Z" fill="#E3A24A" {s()}/>

<path d="M30 86 Q64 96 98 86" fill="none" stroke="#C07A2E" stroke-width="3" stroke-linecap="round"/>
<g fill="#FFF"><circle cx="40" cy="70" r="1.6"/><circle cx="88" cy="70" r="1.6"/><circle cx="50" cy="88" r="1.6"/></g>
{face(64, 70, d=12, k=0.85)}
<path d="M8 110 Q20 100 30 112 M98 112 Q110 100 122 110" fill="none" stroke="#FFF" stroke-width="3" opacity=".7"/>
'''), "герой: русский калач с дужкой-ручкой | сцена: раскачивается на верёвочных качелях, как на ярмарке, дужка смотрит вверх")

# 12 Паприка — гуляш в хлебной миске, перечница сыплет паприку
I["cafe-paprika-naro-fominsk"] = (svg2("#FFF0E8", "#D9432E", f'''
<path d="M22 70 Q18 112 64 114 Q110 112 106 70Z" fill="#D7964A" {s()}/>
<path d="M30 92 l6 6 M48 100 l4 6 M80 100 l-4 6 M98 92 l-6 6" stroke="#9A5A20" stroke-width="2.4" stroke-linecap="round"/>
<ellipse cx="64" cy="70" rx="42" ry="12" fill="#B83A1E" {s()}/>
<g fill="#7A2410" {W(1.6)}><rect x="40" y="64" width="10" height="7" rx="2"/><rect x="70" y="62" width="10" height="7" rx="2"/><rect x="56" y="70" width="9" height="6" rx="2"/></g>
<g fill="#FFE07A"><circle cx="86" cy="70" r="2.4"/><circle cx="36" cy="72" r="2"/></g>
<path d="M88 14 L104 30 Q108 34 104 38 L96 46 Q92 50 88 46 L72 30Z" fill="#F4F4F8" {s()}/>
<path d="M72 30 L88 14 L82 10 L66 26Z" fill="#9A9AAA" {W(2)}/>
<g fill="#E8301E"><circle cx="70" cy="44" r="2"/><circle cx="64" cy="50" r="2"/><circle cx="72" cy="54" r="1.8"/><circle cx="60" cy="58" r="1.8"/></g>
{eye(92, 30, 0.5)}{eye(99, 34, 0.5)}
{face(64, 94, d=11, k=0.75)}
'''), "герой: венгерский гуляш в круглой хлебной миске | сцена: перечница с глазками наклонилась и посыпает его сверху красной паприкой")

# 13 Provance — рататуй спиралью в сковороде на фоне лавандового поля
I["cafe-provance-shchekutino"] = (svg2("#F6F0FF", "#8A6CC8", f'''
<path d="M0 74 H128 V128 H0Z" fill="#A98ADF"/>
<g stroke="#6A4CB0" stroke-width="3" stroke-linecap="round"><path d="M6 74 L-2 128 M22 74 L18 128 M110 74 L114 128 M124 74 L130 128"/></g>
<g fill="#C9B3F2"><ellipse cx="8" cy="72" rx="3" ry="6"/><ellipse cx="22" cy="72" rx="3" ry="6"/><ellipse cx="108" cy="72" rx="3" ry="6"/><ellipse cx="122" cy="72" rx="3" ry="6"/></g>
<circle cx="102" cy="28" r="10" fill="#FFD24A"/>
<path d="M104 86 L124 100" stroke="#2A2A36" stroke-width="7" stroke-linecap="round"/>
<ellipse cx="62" cy="80" rx="46" ry="26" fill="#3A3A48" {s()}/>
<ellipse cx="62" cy="77" rx="40" ry="21" fill="#D9472E"/>
<g {W(1.6)}>
<ellipse cx="30" cy="76" rx="5" ry="9" fill="#F2C94C"/><ellipse cx="38" cy="66" rx="5" ry="9" fill="#5FAE4A" transform="rotate(40 38 66)"/>
<ellipse cx="52" cy="60" rx="5" ry="9" fill="#9A4CA8" transform="rotate(70 52 60)"/><ellipse cx="68" cy="58" rx="5" ry="9" fill="#F2C94C" transform="rotate(95 68 58)"/>
<ellipse cx="84" cy="62" rx="5" ry="9" fill="#5FAE4A" transform="rotate(125 84 62)"/><ellipse cx="94" cy="74" rx="5" ry="9" fill="#9A4CA8"/>
<ellipse cx="88" cy="88" rx="5" ry="9" fill="#F2C94C" transform="rotate(45 88 88)"/><ellipse cx="36" cy="88" rx="5" ry="9" fill="#5FAE4A" transform="rotate(-45 36 88)"/>
</g>
{face(62, 80, d=10, k=0.8)}
<path d="M58 54 Q60 44 66 40 Q64 50 58 54Z" fill="#3FA34D" {W(1.6)}/>
'''), "герой: рататуй, уложенный спиралью из кружочков овощей | сцена: в чёрной сковороде посреди лавандового поля Прованса под жёлтым солнцем")

# 14 Лоботрясы — ленивые вареники развалились в сметане, как в джакузи
I["cafe-lobotryasy-elektrostal"] = (svg2("#E8FFFB", "#2FA89A", f'''
<path d="M10 66 Q14 116 64 116 Q114 116 118 66Z" fill="#F4F4F8" {s()}/>
<path d="M16 80 Q64 90 112 80" fill="none" stroke="#5AB0E8" stroke-width="5"/>
<ellipse cx="64" cy="66" rx="54" ry="14" fill="#FFFDF4" {s()}/>
<g fill="#FFFFFF" opacity=".9"><circle cx="24" cy="60" r="4"/><circle cx="104" cy="58" r="5"/><circle cx="96" cy="48" r="3"/><circle cx="30" cy="48" r="3"/></g>
<path d="M22 66 Q22 48 42 50 Q50 58 46 70Z" fill="#FFF0C8" {s()}/>
<path d="M56 70 Q52 46 72 46 Q86 50 82 70Z" fill="#FFF0C8" {s()}/>
<path d="M88 70 Q90 50 108 54 Q110 66 102 72Z" fill="#FFF0C8" {s()}/>
<path d="M30 58 Q34 56 38 58" fill="none" {W(2)}/><path d="M64 56 Q68 54 72 56 M64 60 Q68 58 72 60" fill="none" {W(2)}/>
<path d="M96 62 Q100 60 104 62" fill="none" {W(2)}/>
<path d="M62 64 Q68 68 74 64" fill="none" {W(2)}/>
<text x="84" y="36" font-family="Arial" font-weight="bold" font-size="13" fill="#fff">z</text><text x="94" y="26" font-family="Arial" font-weight="bold" font-size="10" fill="#fff">z</text>
<ellipse cx="22" cy="56" rx="3.4" ry="2" fill="#FF7FA8" opacity=".7"/><ellipse cx="76" cy="62" rx="3.4" ry="2" fill="#FF7FA8" opacity=".7"/>
'''), "герой: три ленивых вареника | сцена: развалились с закрытыми глазами в миске сметаны, как в джакузи, и похрапывают")

# 15 Печка — русская печка с глазками открыла заслонку, внутри пирожки
I["cafe-pechka-elektrostal"] = (svg2("#FFF3E8", "#5A6E9A", f'''
<path d="M16 120 V52 Q16 40 28 40 H100 Q112 40 112 52 V120Z" fill="#FFFFFF" {s()}/>
<path d="M76 40 V14 H96 V40" fill="#F2F2F6" {s()}/>
<path d="M80 10 Q74 2 80 -4 M90 10 Q96 2 90 -4" {STEAM}/>
<path d="M30 104 V86 Q30 70 52 70 H76 Q98 70 98 86 V104Z" fill="#3A2A2A" {s()}/>
<path d="M36 104 Q50 92 64 104 Q78 92 92 104Z" fill="#F57A1E"/>
<g fill="#E8A54E" {W(2)}><path d="M40 92 Q40 80 52 80 Q62 80 62 92Z"/><path d="M66 92 Q66 80 78 80 Q88 80 88 92Z"/></g>
<rect x="100" y="76" width="20" height="30" rx="3" fill="#7A7A8A" {s()} transform="rotate(14 110 90)"/>
<path d="M16 64 H112" stroke="#E04A3A" stroke-width="3"/><path d="M16 112 H112" stroke="#E04A3A" stroke-width="3"/>
{face(64, 52, d=14, k=0.8)}
'''), "герой: белёная русская печка с красной каймой | сцена: распахнула заслонку-ротик, а внутри над огоньком румянятся два пирожка")

# 16 Джузеппе — макаронина карбонары тянется вверх, по ней лезет кусочек бекона
I["cafe-dzhuzeppe-elektrostal"] = (svg2("#FFFCEB", "#3C9A5A", f'''
<ellipse cx="64" cy="106" rx="52" ry="14" fill="#FFFFFF" {s()}/>
<path d="M22 102 Q20 82 40 80 Q46 68 64 72 Q84 66 90 80 Q108 82 106 102Z" fill="#F7DC8A" {s()}/>
<path d="M30 96 Q40 86 50 96 Q60 86 70 96 Q80 86 90 96 M36 88 Q46 80 56 88 M68 86 Q78 78 88 86" fill="none" stroke="#D9B04A" stroke-width="2.4"/>
<circle cx="64" cy="84" r="7" fill="#FFB020" {W(2)}/>
<path d="M76 80 Q90 54 74 40 Q60 26 76 8" fill="none" stroke="#3B3355" stroke-width="7" stroke-linecap="round"/>
<path d="M76 80 Q90 54 74 40 Q60 26 76 8" fill="none" stroke="#F7DC8A" stroke-width="4" stroke-linecap="round"/>
<rect x="74" y="36" width="20" height="10" rx="3" fill="#E86A6A" {W(2)} transform="rotate(-30 84 41)"/>
<path d="M76 42 L90 34" stroke="#FFD0D0" stroke-width="2"/>
{eye(80, 37, 0.4)}{eye(86, 34, 0.4)}
<g fill="#3B3355"><circle cx="44" cy="90" r="1.4"/><circle cx="80" cy="94" r="1.4"/><circle cx="54" cy="98" r="1.4"/></g>
{face(46, 108, d=0.1, k=0) if False else ''}
{face(64, 98, d=12, k=0.7)}
'''), "герой: тарелка спагетти карбонара с желтком посередине | сцена: одна макаронина тянется вверх, как лиана, и по ней карабкается кусочек бекона")

# 17 Хи-Хи — мармеладный червячок хохочет от щекотки пёрышком
I["cafe-hi-hi-elektrostal"] = (svg2("#FFF2FB", "#F07AC0", f'''
<path d="M16 96 Q26 70 44 86 Q58 100 70 80 Q82 60 100 74 Q112 84 112 70" fill="none" stroke="#3B3355" stroke-width="22" stroke-linecap="round"/>
<path d="M16 96 Q26 70 44 86" fill="none" stroke="#FF5A5A" stroke-width="16" stroke-linecap="round"/>
<path d="M44 86 Q58 100 70 80" fill="none" stroke="#FFC83A" stroke-width="16" stroke-linecap="round"/>
<path d="M70 80 Q82 60 100 74" fill="none" stroke="#6AD06A" stroke-width="16" stroke-linecap="round"/>
<path d="M100 74 Q112 84 112 70" fill="none" stroke="#5AB0FF" stroke-width="16" stroke-linecap="round"/>
<g fill="#fff" opacity=".7"><circle cx="30" cy="86" r="1.4"/><circle cx="56" cy="90" r="1.4"/><circle cx="84" cy="70" r="1.4"/></g>
<path d="M104 64 Q106 60 110 64 M114 64 Q116 60 120 64" fill="none" {W(2.2)}/>
<path d="M106 72 Q112 80 118 72Z" fill="#3B3355"/>
<path d="M30 26 Q62 30 72 62" fill="none" {W(2)}/>
<path d="M30 26 Q50 10 70 24 Q76 40 72 62 Q56 46 30 26Z" fill="#FFFFFF" {W(2.4)}/>
<path d="M40 26 L56 34 M48 22 L62 38 M58 24 L66 44" stroke="#E0D6F0" stroke-width="2"/>
<path d="M92 44 L96 36 M104 46 L110 40 M84 50 L80 42" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
'''), "герой: разноцветный мармеладный червячок | сцена: извивается и хохочет до слёз, потому что его щекочет белое гусиное пёрышко")

# 18 Корчма Диканька — галушка сама прыгает из миски в ночном небе с месяцем
I["cafe-korchma-dikanka-zelenograd"] = (svg2("#5A5AA8", "#1C1A44", f'''
<g fill="#FFF6C8"><circle cx="20" cy="30" r="1.6"/><circle cx="40" cy="16" r="1.4"/><circle cx="110" cy="50" r="1.6"/><circle cx="30" cy="60" r="1.2"/></g>
<path d="M98 14 Q84 26 92 42 Q104 54 118 46 Q102 46 98 32 Q96 22 98 14Z" fill="#FFE27A" {W(2)}/>
<path d="M18 92 Q20 120 64 120 Q108 120 110 92Z" fill="#F2F2F8" {s()}/>
<path d="M24 102 Q64 112 104 102" fill="none" stroke="#3A6AD0" stroke-width="4"/>
<path d="M30 108 l4 -4 4 4 M58 112 l4 -4 4 4 M86 108 l4 -4 4 4" fill="none" stroke="#D8282E" stroke-width="2"/>
<ellipse cx="64" cy="92" rx="46" ry="9" fill="#FFFBEA" {s()}/>
<g fill="#FFF3D0" {W(2)}><ellipse cx="40" cy="88" rx="9" ry="6"/><ellipse cx="86" cy="88" rx="9" ry="6"/></g>
<path d="M64 84 Q60 74 66 66" fill="none" stroke="#FFFBEA" stroke-width="4" stroke-linecap="round" stroke-dasharray="2 6"/>
<ellipse cx="62" cy="48" rx="20" ry="16" fill="#FFF3D0" {s()}/>
<path d="M50 62 Q56 70 64 64" fill="#FFFFFF" {W(1.8)}/>
{face(62, 46, d=8, k=0.7)}
<path d="M40 40 L32 32 M84 40 L92 32" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
'''), "герой: пухлая галушка, обмакнутая в сметану | сцена: сама выпрыгивает из расписной миски вверх, к жёлтому месяцу в ночном небе Диканьки")

# 19 Зефир — зефир-силач держит гантельку из двух клубничек
I["cafe-zefir-zelenograd"] = (svg2("#EFFAFF", "#8FC7F0", f'''
<ellipse cx="64" cy="112" rx="36" ry="7" fill="#5A8FC0" opacity=".35"/>
<path d="M36 108 Q30 88 44 80 Q38 64 54 60 Q60 50 72 56 Q86 54 88 68 Q100 74 94 90 Q100 104 88 110Z" fill="#FFC6DA" {s()}/>
<path d="M44 82 Q56 76 64 84 M74 70 Q82 68 86 76 M50 98 Q60 92 70 100" fill="none" stroke="#F49AB8" stroke-width="2.4" stroke-linecap="round"/>
{face(64, 86, d=10, k=0.8)}
<path d="M42 78 Q30 60 34 44 M88 74 Q100 58 94 44" fill="none" {W(4.4)}/>
<path d="M28 42 H100" stroke="#9A9AAA" stroke-width="5" stroke-linecap="round"/>
<path d="M28 42 H100" {W(1.4)}/>
<path d="M14 32 Q16 24 24 26 Q32 28 30 40 Q28 52 20 54 Q10 50 14 32Z" fill="#E8303E" {s()}/>
<path d="M114 32 Q112 24 104 26 Q96 28 98 40 Q100 52 108 54 Q118 50 114 32Z" fill="#E8303E" {s()}/>
<path d="M16 26 L22 20 L26 28 M112 26 L106 20 L102 28" fill="#4CB050" {W(1.8)}/>
<g fill="#FFE07A"><circle cx="20" cy="38" r="1.2"/><circle cx="24" cy="46" r="1.2"/><circle cx="108" cy="38" r="1.2"/><circle cx="104" cy="46" r="1.2"/></g>
'''), "герой: розовый зефир-силач | сцена: поднимает над головой штангу-гантельку, у которой вместо блинов две клубнички")

# 20 Фазенда — медный таз с вареньем варится на дачной плитке
I["cafe-fazenda-zelenograd"] = (svg2("#FFF7E6", "#7CB342", f'''
<path d="M0 34 H128" stroke="#fff" stroke-width="2" opacity=".6"/>
<rect x="22" y="94" width="84" height="26" rx="4" fill="#F2F2F6" {s()}/>
<circle cx="40" cy="107" r="4" fill="#7A7A8A"/><circle cx="88" cy="107" r="4" fill="#7A7A8A"/>
<path d="M50 94 Q56 86 62 94 Q68 86 74 94" fill="#4A8FE8" opacity=".9"/>
<path d="M10 58 Q12 92 64 92 Q116 92 118 58Z" fill="#D9853A" {s()}/>
<path d="M10 58 L0 52 M118 58 L128 52" {W(5)}/>
<ellipse cx="64" cy="58" rx="54" ry="11" fill="#C0283A" {s()}/>
<ellipse cx="64" cy="57" rx="44" ry="7" fill="#F27AA0" opacity=".8"/>
<g fill="#E8303E" {W(1.6)}><circle cx="40" cy="56" r="5"/><circle cx="86" cy="54" r="5"/><circle cx="64" cy="60" r="4"/></g>
<g fill="#FFD0DE"><circle cx="54" cy="52" r="2.4"/><circle cx="76" cy="58" r="2"/><circle cx="96" cy="58" r="2"/></g>
<path d="M54 40 Q50 32 56 24 M72 40 Q68 30 74 22" {STEAM}/>
<path d="M100 54 L118 18" stroke="#B88A54" stroke-width="5" stroke-linecap="round"/>
{face(64, 76, d=12, k=0.8)}
'''), "герой: медный таз с клубничным вареньем и деревянной ложкой | сцена: пыхтит на дачной газовой плитке, по поверхности бегает розовая пенка")

# 21 Мимино — пропеллер из шампуров с шашлыком крутится на вертолётике над горами
I["cafe-mimino-rzhavki"] = (svg2("#E8F6FF", "#5AA0D8", f'''
<path d="M0 112 L24 78 L40 94 L66 62 L92 96 L108 80 L128 104 V128 H0Z" fill="#7A8AA8" {W(2)}/>
<path d="M60 70 L66 62 L72 70 L68 72 L64 68Z" fill="#fff"/>
<path d="M34 64 Q34 44 60 44 H82 Q100 44 100 62 Q100 78 80 78 H50 Q34 78 34 64Z" fill="#F7C23A" {s()}/>
<path d="M34 62 L12 54 L8 64 L12 70 L34 68" fill="#F7C23A" {s()}/>
<path d="M72 48 Q90 48 94 62 H72Z" fill="#BFE6FF" {W(2.4)}/>
<path d="M50 78 L46 88 M84 78 L88 88 M38 88 H96" {W(3.4)}/>
{face(54, 62, d=7, k=0.65)}
<path d="M66 44 V34" {W(3.6)}/>
<g>
<path d="M66 34 L22 26" stroke="#9A9AAA" stroke-width="3"/><path d="M66 34 L112 24" stroke="#9A9AAA" stroke-width="3"/>
<g {W(1.6)}><rect x="28" y="22" width="9" height="9" rx="2" fill="#9A4A24" transform="rotate(-10 32 27)"/><rect x="42" y="25" width="9" height="9" rx="2" fill="#C86A2E" transform="rotate(-10 46 29)"/>
<rect x="80" y="24" width="9" height="9" rx="2" fill="#C86A2E" transform="rotate(10 84 28)"/><rect x="95" y="21" width="9" height="9" rx="2" fill="#9A4A24" transform="rotate(10 99 25)"/></g>
<circle cx="56" cy="31" r="3.4" fill="#E8303E" {W(1.4)}/><circle cx="74" cy="29" r="3.4" fill="#3FA34D" {W(1.4)}/>
<circle cx="66" cy="34" r="4" fill="#7A7A8A" {W(2)}/>
</g>
<path d="M14 22 Q22 16 28 20 M106 16 Q114 14 118 20" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
'''), "герой: два длинных шампура с шашлыком и помидоркой, сложенные крест-накрест в пропеллер | сцена: крутятся на крыше жёлтого вертолётика, летящего над снежными горами")

# 22 Мятный гусь — пряник-гусь с мятной глазурью шагает по противню с гусятами
I["cafe-myatny-gus-zelenograd"] = (svg2("#EFFFF6", "#3FBF9A", f'''
<rect x="-4" y="96" width="136" height="20" rx="4" fill="#B8BCC8" {s()}/>
<path d="M4 106 H124" stroke="#9A9EAA" stroke-width="2" stroke-dasharray="6 6"/>
<path d="M34 96 Q16 92 20 72 Q24 58 44 62 Q56 64 60 54 L60 32 Q60 18 72 18 Q86 18 86 30 L94 34 L86 38 Q84 48 78 56 Q100 64 100 82 Q98 96 80 96Z" fill="#C8843A" {s()}/>
<path d="M34 90 Q24 84 28 74 M48 86 Q60 92 76 86 M70 30 Q66 40 68 52" fill="none" stroke="#9AF2D8" stroke-width="4" stroke-linecap="round"/>
<path d="M86 30 L96 34 L86 38" fill="#F2A23A" {W(2)}/>
{eye(76, 28, 0.6)}
<ellipse cx="80" cy="36" rx="3" ry="1.8" fill="#FF7FA8" opacity=".7"/>
<path d="M52 72 Q60 66 70 72" fill="none" stroke="#9AF2D8" stroke-width="3" stroke-linecap="round"/>
<path d="M50 96 V104 M70 96 V104" {W(3)}/>
<g>
<path d="M104 96 Q100 86 108 82 Q110 76 116 78 Q120 82 116 86 Q124 90 120 96Z" fill="#C8843A" {W(2.2)}/>
<circle cx="114" cy="81" r="1.2" fill="{O}"/><path d="M118 80 L122 81 L118 83" fill="#F2A23A"/>
<path d="M6 96 Q2 86 10 82 Q12 76 18 78 Q22 82 18 86 Q26 90 22 96Z" fill="#C8843A" {W(2.2)}/>
<circle cx="16" cy="81" r="1.2" fill="{O}"/><path d="M20 80 L24 81 L20 83" fill="#F2A23A"/>
</g>
'''), "герой: имбирный пряник в форме гуся с мятной глазурью | сцена: важно шагает по противню, а впереди и позади — два маленьких пряника-гусёнка")

# 23 Игрушечная — кукла-пупс кормит плюшевого слоника кашей с ложечки
I["cafe-igrushechnaya-zelenograd"] = (svg2("#FFF6FF", "#B98AE8", f'''
<rect x="0" y="100" width="128" height="28" fill="#F7E2A6"/>
<path d="M0 100 H128" {W(2)}/>
<ellipse cx="88" cy="74" rx="24" ry="22" fill="#A8B8D8" {s()}/>
<path d="M66 66 Q54 64 56 80 Q58 88 64 84" fill="#B8C6E2" {s()}/>
<ellipse cx="108" cy="66" rx="12" ry="16" fill="#B8C6E2" {s()}/>
<path d="M74 82 Q64 90 56 86 Q52 82 56 80" fill="none" {W(3)}/>
{eye(82, 68, 0.6)}{eye(94, 68, 0.6)}
<ellipse cx="78" cy="76" rx="3" ry="2" fill="#FF7FA8" opacity=".7"/><ellipse cx="98" cy="76" rx="3" ry="2" fill="#FF7FA8" opacity=".7"/>
<path d="M76 96 V104 M100 96 V104" {W(6)}/>
<ellipse cx="34" cy="86" rx="16" ry="14" fill="#FFB6C8" {s()}/>
<circle cx="34" cy="58" r="16" fill="#FFE0C8" {s()}/>
<path d="M18 56 Q18 38 34 38 Q50 38 50 56 Q44 46 34 46 Q24 46 18 56Z" fill="#FFFFFF" {W(2.4)}/>
<circle cx="34" cy="36" r="4" fill="#FF8AB0" {W(1.6)}/>
{eye(28, 58, 0.55)}{eye(40, 58, 0.55)}
<path d="M30 66 Q34 69 38 66" fill="none" {W(1.8)}/>
<path d="M46 80 L58 72" {W(3)}/>
<ellipse cx="60" cy="71" rx="5" ry="3" fill="#C9C9D6" {W(1.6)}/>
<ellipse cx="60" cy="70" rx="3" ry="1.6" fill="#FFF4C8"/>
<path d="M20 104 Q20 96 30 96 H42 Q50 96 50 104Z" fill="#6CC4FF" {W(2)}/>
<ellipse cx="35" cy="97" rx="13" ry="3" fill="#FFF4C8" {W(1.6)}/>
'''), "герой: кукла-пупс в белом чепчике с розовым помпоном | сцена: сидит на полу игровой и кормит с ложечки кашей плюшевого голубого слоника")

# 24 Бисквит — бисквитный рулет раскатывается красной дорожкой из варенья
I["cafe-biskvit-dmitrov"] = (svg2("#FFF7EE", "#E0A040", f'''
<path d="M58 96 L128 96 L128 112 L52 112Z" fill="#E8303E" {s()}/>
<g fill="#FFE07A"><circle cx="74" cy="104" r="1.6"/><circle cx="96" cy="104" r="1.6"/><circle cx="116" cy="104" r="1.6"/></g>
<path d="M30 44 H86 Q100 44 100 70 Q100 96 86 96 H30Z" fill="#F7D99A" {s()}/>
<path d="M44 46 Q50 70 44 94 M62 46 Q68 70 62 94 M80 46 Q86 70 80 94" fill="none" stroke="#E8C080" stroke-width="2.4"/>
<g fill="#fff"><circle cx="50" cy="52" r="1.6"/><circle cx="70" cy="58" r="1.6"/><circle cx="88" cy="50" r="1.6"/><circle cx="56" cy="88" r="1.6"/></g>
<ellipse cx="30" cy="70" rx="18" ry="26" fill="#FBE6B4" {s()}/>
<path d="M30 70 Q36 70 35 62 Q32 52 24 58 Q16 68 24 82 Q32 92 40 82 Q46 70 40 54" fill="none" stroke="#E8303E" stroke-width="4" stroke-linecap="round"/>
{face(68, 72, d=11, k=0.8)}
{sparkle(108, 30, 9, "#FFF")}{sparkle(20, 24, 6, "#FFF")}
'''), "герой: бисквитный рулет с завитком малинового варенья | сцена: раскатывается, и его край ложится красной ковровой дорожкой, как на премьере")

# 25 Терраса — фруктовый лёд загорает в шезлонге под гирляндой лампочек
I["cafe-terrasa-dmitrov"] = (svg2("#FFFBEA", "#F28A6A", f'''
<path d="M-4 18 Q64 44 132 18" fill="none" {W(2)}/>
<g {W(1.6)}><circle cx="18" cy="30" r="5" fill="#FFE07A"/><circle cx="44" cy="37" r="5" fill="#FF8AB0"/><circle cx="70" cy="38" r="5" fill="#8AE0FF"/><circle cx="96" cy="34" r="5" fill="#B6F27A"/><circle cx="118" cy="26" r="5" fill="#FFE07A"/></g>
<rect x="0" y="110" width="128" height="20" fill="#C8956A"/><path d="M0 110 H128 M32 110 V128 M64 110 V128 M96 110 V128" {W(2)}/>
<path d="M30 110 L40 92 M98 110 L90 92 M30 110 L98 110" fill="none" {W(4)}/>
<path d="M22 94 L36 54 L92 54 L106 94Z" fill="#4AA0E8" {s()}/>
<path d="M30 74 H98 M26 84 H102" stroke="#FFFFFF" stroke-width="5"/>
<path d="M50 96 V108" stroke="#E8C9A0" stroke-width="6" stroke-linecap="round"/>
<path d="M50 96 V108" {W(1.4)}/>
<path d="M38 96 V58 Q38 44 50 44 Q62 44 62 58 V96Z" fill="#FF6A4A" {s()}/>
<path d="M38 70 H62 M38 82 H62" stroke="#FFC83A" stroke-width="5"/>
<path d="M38 58 Q50 54 62 58 L62 63 Q56 66 52 62 L48 62 Q44 66 38 63Z" fill="#2A2A36" {W(1.4)}/>
<path d="M44 66 Q50 70 56 66" fill="none" {W(2)}/>
<path d="M62 64 Q74 62 80 70" fill="none" {W(3)}/>
<path d="M74 62 L92 30" stroke="#7A5A3A" stroke-width="2.4"/>
<path d="M74 62 Q78 52 86 54" fill="none" {W(1.6)}/>
<path d="M70 40 L76 62 L88 60Z" fill="#7BD07A" {W(1.6)}/>
<circle cx="80" cy="66" r="6" fill="#FFF3C4" {W(2)}/>
<path d="M78 58 L84 50" stroke="#FF8AB0" stroke-width="2"/>
'''), "герой: апельсиново-клубничный фруктовый лёд на палочке в тёмных очках | сцена: загорает, развалившись в полосатом шезлонге на деревянной террасе под гирляндой лампочек")

# 26 Зензеро — ризотто с белыми грибами в сотейнике, деревянная ложка мешает
I["cafe-zenzero-noginsk"] = (svg2("#F7F7EC", "#7A8A4A", f'''
<path d="M14 76 Q14 112 64 112 Q114 112 114 76Z" fill="#B8C0C8" {s()}/>
<path d="M114 80 L126 80" {W(6)}/>
<path d="M2 80 L14 80" {W(6)}/>
<ellipse cx="64" cy="76" rx="50" ry="13" fill="#F4E6B8" {s()}/>
<g fill="#FFFBEA"><circle cx="34" cy="74" r="2"/><circle cx="44" cy="80" r="2"/><circle cx="58" cy="72" r="2"/><circle cx="84" cy="80" r="2"/><circle cx="96" cy="72" r="2"/><circle cx="70" cy="82" r="2"/></g>
<g {W(1.8)}><path d="M40 70 Q38 62 46 62 Q54 62 52 70Z" fill="#9A6A3A"/><rect x="43" y="69" width="6" height="7" rx="2" fill="#F4E6C8"/>
<path d="M78 72 Q76 64 84 64 Q92 64 90 72Z" fill="#9A6A3A"/><rect x="81" y="71" width="6" height="6" rx="2" fill="#F4E6C8"/></g>
<path d="M60 74 L84 22" stroke="#C8955A" stroke-width="7" stroke-linecap="round"/>
<path d="M60 74 L84 22" {W(1.4)}/>
<path d="M44 54 Q40 44 46 36 M100 58 Q104 48 98 40" {STEAM}/>
<path d="M20 60 q4 -6 8 0 M108 52 q4 -6 8 0" fill="none" stroke="#fff" stroke-width="2"/>
{face(64, 94, d=12, k=0.8)}
'''), "герой: сливочное ризотто с белыми грибами в стальном сотейнике | сцена: деревянная ложка помешивает его, вокруг поднимается пар")

# 27 Family House — три кружки какао-семья сидят на диване под пледом
I["cafe-family-house-noginsk"] = (svg2("#FFF3E0", "#D07A4A", f'''
<path d="M6 76 Q6 62 20 62 H108 Q122 62 122 76 V112 H6Z" fill="#7A5AA8" {s()}/>
<rect x="0" y="86" width="128" height="30" rx="8" fill="#9A7AC8" {s()}/>
<g {W(2.4)}>
<rect x="18" y="44" width="28" height="36" rx="6" fill="#FF8A5A"/><path d="M46 52 Q56 52 54 64 Q52 72 46 70" fill="none"/>
<rect x="72" y="40" width="30" height="40" rx="6" fill="#5AB0E8"/><path d="M102 50 Q112 50 110 62 Q108 72 102 70" fill="none"/>
<rect x="52" y="60" width="18" height="22" rx="5" fill="#FFD24A"/>
</g>
<g fill="#7A4A2E"><ellipse cx="32" cy="45" rx="12" ry="2.6"/><ellipse cx="87" cy="41" rx="13" ry="2.6"/><ellipse cx="61" cy="61" rx="7" ry="2"/></g>
{eye(27, 58, 0.5)}{eye(37, 58, 0.5)}{eye(82, 56, 0.55)}{eye(93, 56, 0.55)}{eye(58, 70, 0.4)}{eye(64, 70, 0.4)}
<path d="M28 64 Q32 67 36 64 M84 63 Q88 66 92 63 M59 75 Q61 77 63 75" fill="none" {W(1.6)}/>
<path d="M4 80 Q30 72 64 82 Q98 72 124 80 L124 100 Q64 108 4 100Z" fill="#FFB8CC" {s()}/>
<path d="M20 86 L28 96 M44 88 L52 98 M76 88 L84 98 M100 86 L108 96" stroke="#FF8AB0" stroke-width="3"/>
'''), "герой: семья из трёх кружек какао — папа, мама и малыш | сцена: сидят рядышком на фиолетовом диване, укрывшись одним розовым пледом")

# 28 Парло Руссо — блин с красной икрой говорит «Привет!»
I["cafe-parlo-russo-noginsk"] = (svg2("#FFF6EA", "#3A7AC8", f'''
<ellipse cx="54" cy="104" rx="44" ry="10" fill="#FFFFFF" {s()}/>
<path d="M14 98 Q14 52 54 52 Q94 52 94 98Z" fill="#F5C66A" {s()}/>
<path d="M14 98 Q54 84 94 98" fill="#E8A84A" {s()}/>
<g fill="#E8401E" {W(1)}><circle cx="30" cy="62" r="3"/><circle cx="38" cy="58" r="3"/><circle cx="46" cy="56" r="3"/><circle cx="54" cy="55" r="3"/><circle cx="62" cy="56" r="3"/><circle cx="70" cy="58" r="3"/><circle cx="78" cy="62" r="3"/><circle cx="42" cy="62" r="3"/><circle cx="66" cy="62" r="3"/></g>
<g fill="#C88A3A"><circle cx="28" cy="80" r="1.6"/><circle cx="80" cy="78" r="1.6"/><circle cx="70" cy="88" r="1.6"/></g>
{face(54, 76, d=11, k=0.8)}
<path d="M80 40 Q74 14 100 12 Q124 12 124 30 Q124 46 104 46 L94 46 L84 54 L86 44 Q80 44 80 40Z" fill="#FFFFFF" {s()}/>
<path d="M108 20 V31" stroke="#3A7AC8" stroke-width="4" stroke-linecap="round"/><circle cx="108" cy="37" r="2.4" fill="#3A7AC8"/><path d="M96 26 C94 22 89 24 91 28 L96 33 L101 28 C103 24 98 22 96 26Z" fill="#FF5A7E"/>
'''), "герой: румяный блин-полумесяц с красной икрой на макушке | сцена: здоровается, а над ним белое облачко-реплика, как в комиксе")

# 29 Галерея — капкейк позирует для портрета в золотой раме
I["cafe-galereya-sokolniki-istra"] = (svg2("#FDF6EE", "#8A5A3A", f'''
<rect x="18" y="14" width="92" height="96" rx="4" fill="#E8B83A" {s()}/>
<rect x="28" y="24" width="72" height="76" fill="#CDE8F7" {W(2.4)}/>
<path d="M18 14 L28 24 M110 14 L100 24 M18 110 L28 100 M110 110 L100 100" {W(2)}/>
<g fill="#F7D46A"><circle cx="23" cy="62" r="2.4"/><circle cx="105" cy="62" r="2.4"/><circle cx="64" cy="19" r="2.4"/><circle cx="64" cy="105" r="2.4"/></g>
<path d="M44 74 L50 98 H78 L84 74Z" fill="#7BC6E8" {s()}/>
<path d="M52 76 L54 96 M64 76 V96 M76 76 L74 96" stroke="#4A9AC8" stroke-width="2"/>
<path d="M40 76 Q36 62 50 60 Q52 46 64 48 Q76 46 78 60 Q92 62 88 76Z" fill="#FFB6D0" {s()}/>
<circle cx="64" cy="42" r="6" fill="#E8303E" {W(2)}/>
<path d="M64 36 Q66 30 70 28" fill="none" {W(2)}/>
<g fill="#6CC4FF"><rect x="48" y="62" width="4" height="2" rx="1"/><rect x="72" y="58" width="4" height="2" rx="1"/></g><g fill="#FFE07A"><rect x="60" y="56" width="4" height="2" rx="1"/><rect x="80" y="68" width="4" height="2" rx="1"/></g>
{face(64, 86, d=8, k=0.65)}
<path d="M100 120 L122 92" stroke="#B8854A" stroke-width="4" stroke-linecap="round"/>
<path d="M120 94 L126 86" stroke="#E8303E" stroke-width="5" stroke-linecap="round"/>
'''), "герой: розовый капкейк с вишенкой и посыпкой | сцена: чинно позирует внутри золотой рамы, как на портрете, а снизу к раме тянется кисточка художника")

# 30 Стрекоза — вафельная трубочка с крылышками-листиками мяты летит над прудом
I["cafe-strekoza-kryuchkovo"] = (svg2("#E6FBF4", "#3A9AB8", f'''
<path d="M0 98 Q32 92 64 98 Q96 104 128 98 V128 H0Z" fill="#2E86B0"/>
<path d="M14 98 V64 M22 98 V72 M110 98 V60 M118 98 V70" stroke="#3E7A3A" stroke-width="3" stroke-linecap="round"/>
<g fill="#8A5A3A"><rect x="11" y="58" width="6" height="14" rx="3"/><rect x="107" y="54" width="6" height="14" rx="3"/></g>
<ellipse cx="62" cy="110" rx="14" ry="4" fill="#7ACB6A" {W(2)}/>
<g {W(2)}>
<path d="M58 50 Q40 26 22 34 Q22 50 56 56Z" fill="#9AF2C8"/>
<path d="M58 58 Q36 64 28 80 Q44 84 58 62Z" fill="#9AF2C8"/>
<path d="M70 50 Q88 26 106 34 Q106 50 72 56Z" fill="#9AF2C8"/>
<path d="M70 58 Q92 64 100 80 Q84 84 70 62Z" fill="#9AF2C8"/>
</g>
<path d="M40 38 L56 52 M88 38 L72 52 M38 74 L56 62 M90 74 L72 62" stroke="#3FBF8A" stroke-width="1.6"/>
<rect x="56" y="30" width="16" height="62" rx="8" fill="#E8B060" {s()}/>
<path d="M56 44 L72 38 M56 56 L72 50 M56 68 L72 62 M56 80 L72 74" stroke="#B8803A" stroke-width="2"/>
<ellipse cx="64" cy="31" rx="7" ry="3" fill="#FFF6E6" {W(1.6)}/>
{eye(60, 40, 0.55)}{eye(68, 40, 0.55)}
<path d="M61 46 Q64 48 67 46" fill="none" {W(1.6)}/>
<path d="M60 26 Q56 18 50 16 M68 26 Q72 18 78 16" fill="none" {W(1.8)}/>
'''), "герой: вафельная трубочка с кремом и крылышками из листиков мяты | сцена: порхает, как стрекоза, над прудом между камышами")

# 31 Василёк — открытый черничный пирог, синий василёк заглядывает с края
I["cafe-vasilek-oktyabrskoy-fabriki"] = (svg2("#F2F6FF", "#5A6EC8", f'''
<rect x="0" y="96" width="128" height="32" fill="#EDE2C8"/>
<path d="M0 104 H128 M0 116 H128" stroke="#D8C8A6" stroke-width="2"/>
<ellipse cx="56" cy="92" rx="48" ry="14" fill="#FFFFFF" {s()}/>
<path d="M14 82 Q14 98 56 100 Q98 98 98 82Z" fill="#D8A050" {s()}/>
<ellipse cx="56" cy="80" rx="42" ry="12" fill="#3A3A8A" {s()}/>
<g fill="#5A5AC8"><circle cx="34" cy="78" r="3.4"/><circle cx="46" cy="74" r="3.4"/><circle cx="62" cy="76" r="3.4"/><circle cx="76" cy="80" r="3.4"/><circle cx="50" cy="84" r="3.4"/><circle cx="70" cy="72" r="3"/></g>
<path d="M22 78 L90 82 M30 72 L36 88 M50 70 L54 90 M70 70 L72 90" stroke="#E8B060" stroke-width="3.4" stroke-linecap="round"/>
{face(56, 92, d=12, k=0.6)}
<path d="M104 96 Q106 74 98 60" fill="none" stroke="#3E8A3A" stroke-width="3"/>
<g fill="#4A6AE8" {W(1.6)}>
<path d="M98 50 L92 38 L100 42Z"/><path d="M98 50 L104 36 L106 46Z"/><path d="M98 50 L114 44 L108 54Z"/><path d="M98 50 L112 60 L102 58Z"/>
<path d="M98 50 L96 66 L92 56Z"/><path d="M98 50 L82 58 L86 48Z"/><path d="M98 50 L84 40 L94 42Z"/>
</g>
<circle cx="98" cy="50" r="5" fill="#2A2A8A" {W(1.6)}/>
{eye(96, 49, 0.35)}{eye(100, 49, 0.35)}
'''), "герой: открытый черничный пирог с решёткой из теста | сцена: лежит на льняной скатерти, а с края стола заглядывает синий цветок василёк с глазками")

# 32 Рум Брум — мотоцикл с колёсами-пончиками мчится, из трубки-соломинки пар
I["cafe-rum-brum-domodedovo"] = (svg2("#FFF6E0", "#E05A3A", f'''
<path d="M0 104 H128 V128 H0Z" fill="#5A5A6A"/>
<path d="M8 116 H28 M48 116 H68 M88 116 H108" stroke="#FFE07A" stroke-width="3"/>
<g {W(2.6)}><circle cx="30" cy="86" r="18" fill="#E8A050"/><circle cx="98" cy="86" r="18" fill="#E8A050"/></g>
<g fill="#FF8AB0"><path d="M14 80 Q30 64 46 80 Q42 74 30 72 Q18 74 14 80Z"/><path d="M82 80 Q98 64 114 80 Q110 74 98 72 Q86 74 82 80Z"/></g>
<g fill="url(#g)" {W(2)}><circle cx="30" cy="86" r="6"/><circle cx="98" cy="86" r="6"/></g>
<path d="M30 86 L52 62 H84 L98 86" fill="none" {W(4)}/>
<path d="M46 66 Q50 50 66 50 H86 Q94 50 92 62 H50Z" fill="#E8303E" {s()}/>
<path d="M88 50 L96 34 L104 34" fill="none" {W(4)}/>
<path d="M12 62 L34 66" stroke="#7BD07A" stroke-width="4" stroke-linecap="round"/>
<path d="M12 62 L34 66" {W(1.2)}/>
<g fill="#FFFFFF" opacity=".9"><circle cx="6" cy="58" r="5"/><circle cx="-2" cy="52" r="4"/></g>
{face(70, 57, d=7, k=0.55)}
<path d="M110 40 H124 M108 52 H122" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
'''), "герой: красный мотоцикл с колёсами из двух глазированных пончиков | сцена: с рёвом мчится по дороге, из выхлопной трубки-соломинки вылетают облачка")

# 33 Царский дворик — осётр на серебряном блюде с лимоном во рту
I["cafe-tsarsky-dvorik-yam"] = (svg2("#FFF8E0", "#A8322A", f'''
<path d="M0 30 H128" stroke="#F2C94C" stroke-width="3"/><path d="M0 36 H128" stroke="#F2C94C" stroke-width="1.6"/>
<ellipse cx="64" cy="92" rx="60" ry="20" fill="#D8DCE8" {s()}/>
<ellipse cx="64" cy="89" rx="50" ry="14" fill="#EEF0F6"/>
<path d="M14 82 Q40 58 84 64 Q100 66 108 76 Q100 88 84 90 Q40 96 14 82Z" fill="#8A9AAE" {s()}/>
<path d="M14 82 L4 70 L6 88Z" fill="#8A9AAE" {W(2.4)}/>
<path d="M30 78 L36 74 L42 78 L48 74 L54 78 L60 74 L66 78 L72 74 L78 78" fill="none" stroke="#F4F6FA" stroke-width="2.4"/>
<path d="M98 72 Q104 66 112 70 Q118 76 112 82 Q104 86 98 80Z" fill="#FFE04A" {W(2)}/>
<path d="M104 70 V82" stroke="#F2C020" stroke-width="1.6"/>
{eye(90, 74, 0.6)}
<ellipse cx="88" cy="82" rx="3.4" ry="2" fill="#FF7FA8" opacity=".7"/>
<g fill="#3FA34D" {W(1.4)}><path d="M30 96 Q34 88 40 96Z"/><path d="M70 98 Q74 90 80 98Z"/></g>
<path d="M54 40 L58 26 L64 34 L70 26 L74 40Z" fill="#F2C94C" {W(2)}/>
<g fill="#E8303E"><circle cx="58" cy="26" r="2"/><circle cx="70" cy="26" r="2"/></g>
<path d="M50 50 Q64 42 78 50" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".7"/>
'''), "герой: серебристый осётр с лимоном во рту | сцена: лежит во главе царского пира на огромном серебряном блюде, над ним парит маленькая золотая корона-гирлянда")

# 34 Грин Парк — матча-латте гуляет по парковой дорожке с собачкой-печеньем
I["cafe-green-park-domodedovo"] = (svg2("#F0FFE8", "#4CAF50", f'''
<path d="M0 98 Q64 82 128 98 V128 H0Z" fill="#E8D8B0" {s()}/>
<circle cx="14" cy="44" r="16" fill="#3E8E3A" {W(2)}/><path d="M14 60 V88" stroke="#7A5A3A" stroke-width="5"/>
<circle cx="112" cy="36" r="14" fill="#5AAE4A" {W(2)}/><path d="M112 50 V80" stroke="#7A5A3A" stroke-width="5"/>
<path d="M36 50 L40 102 Q41 108 48 108 H62 Q69 108 70 102 L74 50Z" fill="#FFFFFF" {s()}/>
<path d="M38 70 L72 70 L70 92 L40 92Z" fill="#8ACB5A"/>
<path d="M34 44 H76 L74 52 H36Z" fill="#7A9A4A" {s()}/>
<path d="M54 44 V30" stroke="#3FA34D" stroke-width="4" stroke-linecap="round"/>
{face(55, 80, d=7, k=0.6)}
<path d="M70 86 Q82 82 92 96" fill="none" stroke="#E8303E" stroke-width="2"/>
<ellipse cx="96" cy="100" rx="13" ry="9" fill="#D9A55A" {s()}/>
<circle cx="108" cy="92" r="7" fill="#D9A55A" {s()}/>
<path d="M104 86 Q100 80 104 80" fill="#B8803A" {W(1.6)}/>
<g fill="#7A4A2E"><circle cx="92" cy="98" r="1.6"/><circle cx="98" cy="104" r="1.6"/><circle cx="100" cy="96" r="1.4"/></g>
<circle cx="110" cy="91" r="1.4" fill="{O}"/><circle cx="114" cy="93" r="1.6" fill="{O}"/>
<path d="M84 98 Q78 92 80 88" fill="none" {W(2.4)}/>
<path d="M88 108 V114 M102 108 V114" {W(3)}/>
'''), "герой: стаканчик матча-латте с собой | сцена: гуляет по парковой дорожке между деревьями и ведёт на красном поводке собачку из печенья")

# 35 Здрасте — булочка с маком высунулась из окошка и машет прихваткой
I["cafe-zdraste-domodedovo"] = (svg2("#FFF2F6", "#F2A23A", f'''
<rect x="8" y="22" width="112" height="106" fill="#F7E2C8" {s()}/>
<path d="M8 22 L64 2 L120 22" fill="#E8603A" {s()}/>
<rect x="24" y="40" width="80" height="66" rx="6" fill="#7AC8F0" {s()}/>
<path d="M18 40 Q22 64 30 64 Q40 56 40 40Z M110 40 Q106 64 98 64 Q88 56 88 40Z" fill="#FF8AB0" {W(2.4)}/>
<rect x="16" y="102" width="96" height="10" rx="3" fill="#FFFFFF" {s()}/>
<path d="M30 102 Q28 66 64 64 Q100 66 98 102Z" fill="#F2C27A" {s()}/>
<g fill="#3B3355"><circle cx="46" cy="74" r="1.4"/><circle cx="54" cy="70" r="1.4"/><circle cx="74" cy="70" r="1.4"/><circle cx="84" cy="76" r="1.4"/><circle cx="64" cy="68" r="1.4"/><circle cx="40" cy="84" r="1.4"/><circle cx="90" cy="86" r="1.4"/></g>
{face(64, 86, d=11, k=0.8)}
<path d="M94 86 Q104 70 104 56" fill="none" {W(4)}/>
<path d="M94 56 Q92 42 104 40 Q116 42 114 56 Q112 62 104 62 Q96 62 94 56Z" fill="#6AD06A" {s()}/>
<path d="M98 50 L110 50" stroke="#fff" stroke-width="2"/>
<path d="M116 40 Q120 36 122 40 M114 32 Q118 26 122 30" fill="none" stroke="#3B3355" stroke-width="2" stroke-linecap="round"/>
'''), "герой: пышная булочка с маком | сцена: высунулась из окошка с розовыми занавесками и машет зелёной кухонной прихваткой — «Здрасте!»")

# 36 Дом блинов — стопка блинов-домик с крышей из сметаны и трубой
I["cafe-dom-blinov-ivanteevka"] = (svg2("#F4F8FF", "#7A9AE0", f'''
<path d="M0 110 H128 V128 H0Z" fill="#8ACB6A"/>
<g {W(2.4)}>
<ellipse cx="64" cy="104" rx="46" ry="8" fill="#E8A84A"/>
<ellipse cx="64" cy="94" rx="44" ry="8" fill="#F2BC5A"/>
<ellipse cx="64" cy="84" rx="44" ry="8" fill="#E8A84A"/>
<ellipse cx="64" cy="74" rx="42" ry="8" fill="#F2BC5A"/>
<ellipse cx="64" cy="64" rx="42" ry="8" fill="#E8A84A"/>
</g>
<path d="M18 62 L64 22 L110 62 Q64 70 18 62Z" fill="#FFFBF0" {s()}/>
<path d="M30 60 Q32 68 36 62 M88 62 Q90 70 94 62" fill="#FFFBF0" {W(1.6)}/>
<rect x="84" y="24" width="12" height="22" fill="#C88A3A" {s()}/>
<path d="M88 20 Q84 12 90 6 M94 20 Q98 12 94 4" {STEAM}/>
<rect x="56" y="80" width="16" height="22" rx="6" fill="#B8702A" {W(2)}/>
<rect x="30" y="72" width="14" height="12" rx="2" fill="#FFE07A" {W(2)}/><rect x="84" y="72" width="14" height="12" rx="2" fill="#FFE07A" {W(2)}/>
<path d="M37 72 V84 M30 78 H44 M91 72 V84 M84 78 H98" stroke="#3B3355" stroke-width="1.6"/>
{face(64, 46, d=9, k=0.7)}
'''), "герой: высокая стопка блинов в виде домика с окошками и дверцей | сцена: крыша из сметаны, а из печной трубы-сосиски вьётся пар")


if __name__ == "__main__":
    reg = os.path.join(ROOT, "icons-src", "subjects.txt")
    lines = open(reg, encoding="utf-8").read().splitlines()
    lines = [l for l in lines if l.split(" — ", 1)[0] not in I]
    for pid, (svg_, subj) in I.items():
        open(os.path.join(ROOT, "icons-src", pid + ".svg"), "w").write(svg_)
        lines.append(f"{pid} — {subj}")
    open(reg, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("иконок:", len(I))
