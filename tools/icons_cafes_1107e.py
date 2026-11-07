"""Робот cafes, 2026-11-07 (08 UTC): иконки 45 новых кафе. Каждая придумана и нарисована отдельно
(правило абсолютной уникальности: свой герой, своя сцена, своя компоновка и палитра фона).
Запуск из корня: python3 tools/icons_cafes_1107e.py  → icons-src/<id>.svg + строки в icons-src/subjects.txt"""
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


I = {}

# 1 Тин — римская пинса парит над крышами, как ковёр-самолёт
I["cafe-tin-novodmitrovskaya"] = (svg2("#FFF1E6", "#7A5BC8", f'''
<path d="M0 112 V96 H18 V86 H34 V100 H50 V90 H70 V104 H88 V84 H106 V98 H128 V128 H0Z" fill="#4B3A86" opacity=".55"/>
<rect x="24" y="92" width="4" height="4" fill="#FFE07A"/><rect x="94" y="90" width="4" height="4" fill="#FFE07A"/>
<path d="M14 62 Q14 40 64 38 Q114 40 114 62 Q114 84 64 86 Q14 84 14 62Z" fill="#F4C27A" {s()}/>
<path d="M22 62 Q22 46 64 45 Q106 46 106 62 Q106 78 64 79 Q22 78 22 62Z" fill="#E8573A" {W(2.2)}/>
<circle cx="40" cy="56" r="6" fill="#FFF8E8" {W(2)}/><circle cx="88" cy="58" r="7" fill="#FFF8E8" {W(2)}/><circle cx="66" cy="70" r="5" fill="#FFF8E8" {W(2)}/>
<path d="M50 52 Q55 46 60 52 Q55 56 50 52Z M78 70 Q83 64 88 70 Q83 74 78 70Z" fill="#3FA34D" {W(1.6)}/>
{face(64, 58, d=8, k=0.7)}
<path d="M14 66 L6 74 M114 66 L122 74 M26 82 L20 92 M102 82 L108 92" stroke="#FFF" stroke-width="3" stroke-linecap="round" opacity=".8"/>
'''), "герой: овальная римская пинса с томатом и моцареллой | сцена: парит над ночными крышами города, как ковёр-самолёт")

# 2 На Руси — кулебяка с косичкой на расписном рушнике
I["cafe-na-rusi-mytishchi"] = (svg2("#FFF8EC", "#D6A04A", f'''
<path d="M6 92 H122 V118 H6Z" fill="#FFFFFF" {s()}/>
<path d="M6 106 H122" stroke="#D8283A" stroke-width="4"/>
<path d="M14 112 l6 -6 6 6 6 -6 6 6 6 -6 6 6 6 -6 6 6 6 -6 6 6 6 -6 6 6 6 -6 6 6 6 -6 6 6" fill="none" stroke="#D8283A" stroke-width="2"/>
<path d="M14 92 Q12 58 64 54 Q116 58 114 92Z" fill="#E7A24E" {s()}/>
<path d="M28 66 Q36 60 44 66 Q52 60 60 66 Q68 60 76 66 Q84 60 92 66 Q100 60 106 68" fill="none" stroke="#B9702C" stroke-width="5" stroke-linecap="round"/>
<path d="M28 66 Q36 60 44 66 Q52 60 60 66 Q68 60 76 66 Q84 60 92 66 Q100 60 106 68" fill="none" stroke="#F6C27A" stroke-width="2" stroke-linecap="round"/>
<ellipse cx="64" cy="58" rx="6" ry="4" fill="#7A4A20"/>
<path d="M58 48 Q54 40 60 34 M66 46 Q62 36 70 28" fill="none" stroke="#FFF" stroke-width="3.4" stroke-linecap="round"/>
{face(64, 80, d=10, k=0.8)}
'''), "герой: кулебяка с косичкой из теста | сцена: лежит на вышитом красном рушнике, из окошка в корочке поднимается пар")

# 3 Оранжевый Экспресс — апельсиновый мусс-полусфера мчится вперёд
I["cafe-oranzhevy-ekspress-odintsovo"] = (svg2("#FFFBE0", "#FF8A1E", f'''
<path d="M6 46 H34 M2 62 H28 M8 78 H32" stroke="#FFF" stroke-width="5" stroke-linecap="round" opacity=".85"/>
<ellipse cx="72" cy="98" rx="46" ry="7" fill="#C25A10" opacity=".35"/>
<path d="M34 94 Q34 40 76 38 Q118 40 116 94Z" fill="#FF9A2E" {s()}/>
<path d="M40 60 Q76 52 112 60" fill="none" stroke="#FFD08A" stroke-width="3"/>
<path d="M30 94 H120" {W(3.4)}/>
<path d="M30 94 H120 V100 Q75 106 30 100Z" fill="#7A3E12" {s()}/>
<path d="M70 38 Q72 26 82 24 Q80 34 70 38Z" fill="#4CB050" {W(2)}/>
<circle cx="76" cy="40" r="4" fill="#FF5A3A" {W(2)}/>
{face(76, 72, d=9, k=0.8)}
<path d="M96 66 Q104 62 108 68" fill="none" {W(2.2)}/>
'''), "герой: апельсиновый мусс-полусфера на шоколадном донышке | сцена: мчится вперёд, оставляя белые линии скорости")

# 4 ТакаТуки — поке-боул-остров плывёт по волнам
I["cafe-takatuki-odintsovo"] = (svg2("#E0FBFF", "#1E9CC8", f'''
<path d="M0 96 Q16 88 32 96 Q48 104 64 96 Q80 88 96 96 Q112 104 128 96 V128 H0Z" fill="#3FC3E8" {s()}/>
<path d="M18 74 Q22 104 64 104 Q106 104 110 74Z" fill="#FFFFFF" {s()}/>
<path d="M18 74 Q64 64 110 74" fill="#FFFFFF" {s()}/>
<path d="M26 74 Q38 62 52 72 Z" fill="#FF8A6A" {W(2)}/>
<path d="M52 72 Q60 60 74 70Z" fill="#7BD07A" {W(2)}/>
<path d="M74 70 Q88 60 102 72Z" fill="#FFF3D0" {W(2)}/>
<circle cx="88" cy="70" r="2" fill="{O}"/><circle cx="92" cy="72" r="2" fill="{O}"/><circle cx="84" cy="73" r="2" fill="{O}"/>
<path d="M60 70 V36" stroke="#8A5A2A" stroke-width="4" stroke-linecap="round"/>
<path d="M60 38 Q46 26 34 34 Q48 34 60 38 Q58 22 46 16 Q60 20 60 38 Q70 20 84 22 Q70 28 60 38 Q76 30 88 40 Q72 38 60 38Z" fill="#3FAE4A" {W(2.2)}/>
{face(64, 88, d=10, k=0.75)}
'''), "герой: поке-боул с лососем и авокадо | сцена: плывёт по волнам, как маленький остров с пальмой посередине")

# 5 Загородный очаг — кружка горячего сбитня греется у очага
I["cafe-zagorodny-ochag-odintsovo"] = (svg2("#FFE8C8", "#8A3A1E", f'''
<path d="M8 128 V40 Q8 26 22 26 H52 Q66 26 66 40 V128Z" fill="#9C5A3A" {s()}/>
<path d="M18 128 V56 Q18 46 37 46 Q56 46 56 56 V128Z" fill="#3A1E1E" {s()}/>
<path d="M24 112 Q28 88 36 98 Q38 80 44 96 Q50 88 50 112Z" fill="#FFB02E" {W(2)}/>
<path d="M30 112 Q34 100 37 104 Q40 96 44 112Z" fill="#FFE27A"/>
<path d="M20 114 H54" stroke="#6A3A1E" stroke-width="6" stroke-linecap="round"/>
<path d="M70 62 H112 V108 Q112 116 104 116 H78 Q70 116 70 108Z" fill="#5BA8E0" {s()}/>
<path d="M112 72 Q124 72 124 86 Q124 98 112 98" fill="none" {W(4)}/>
<ellipse cx="91" cy="62" rx="21" ry="5" fill="#C86A2A" {W(2.4)}/>
<path d="M82 52 Q78 44 84 38 M94 50 Q90 40 98 32" fill="none" stroke="#FFF" stroke-width="3" stroke-linecap="round" opacity=".9"/>
{face(91, 88, d=8, k=0.75)}
'''), "герой: глиняная кружка горячего медового сбитня | сцена: греется у каменного очага, где горят поленья")

# 6 Ковчег — эчпочмак у трапа под радугой после дождя
I["cafe-kovcheg-odintsovo"] = (svg2("#F2F9FF", "#6F8FD8", f'''
<path d="M-4 80 Q64 -6 132 80" fill="none" stroke="#FF6B6B" stroke-width="7"/>
<path d="M4 82 Q64 6 124 82" fill="none" stroke="#FFC23E" stroke-width="7"/>
<path d="M12 84 Q64 18 116 84" fill="none" stroke="#5FCB6A" stroke-width="7"/>
<path d="M20 86 Q64 30 108 86" fill="none" stroke="#5AA8F0" stroke-width="7"/>
<path d="M0 106 H128 V128 H0Z" fill="#8FD07A" {s()}/>
<path d="M34 104 L64 50 L94 104Z" fill="#E9B05A" {s()}/>
<path d="M44 96 L64 60 L84 96" fill="none" stroke="#C4843A" stroke-width="2.4" stroke-dasharray="4 4"/>
<circle cx="64" cy="58" r="4" fill="#B06A2A" {W(2)}/>
{face(64, 86, d=8, k=0.75)}
<path d="M100 26 Q106 20 112 26 Q118 24 118 32 H98 Q94 26 100 26Z" fill="#fff" {W(2)}/>
'''), "герой: татарский эчпочмак-треугольник | сцена: стоит на траве под огромной радугой после дождя")

# 7 Олива — салат оливье горкой, горошина с флажком на вершине
I["cafe-oliva-erino"] = (svg2("#F3FFF0", "#5DB37A", f'''
<path d="M0 74 L14 50 L28 74Z M100 76 L114 48 L128 76Z" fill="#2E8A4E" {W(2.4)}/>
<ellipse cx="64" cy="102" rx="54" ry="14" fill="#FFFFFF" {s()}/>
<ellipse cx="64" cy="100" rx="42" ry="8" fill="#E6F0F4"/>
<path d="M28 100 Q30 58 64 50 Q98 58 100 100Z" fill="#FFF2B8" {s()}/>
<rect x="38" y="76" width="8" height="8" rx="2" fill="#FF9E4A" {W(1.6)}/><rect x="80" y="70" width="8" height="8" rx="2" fill="#FF9E4A" {W(1.6)}/>
<rect x="52" y="88" width="7" height="7" rx="2" fill="#F4D7A0" {W(1.6)}/><rect x="86" y="88" width="7" height="7" rx="2" fill="#E89A9A" {W(1.6)}/>
<circle cx="44" cy="92" r="3.6" fill="#6BCB4A" {W(1.6)}/><circle cx="72" cy="66" r="3.6" fill="#6BCB4A" {W(1.6)}/><circle cx="94" cy="80" r="3.6" fill="#6BCB4A" {W(1.6)}/>
<circle cx="64" cy="46" r="7" fill="#6BCB4A" {W(2.4)}/>
<path d="M64 40 V18" {W(2.4)}/><path d="M64 18 L82 23 L64 28Z" fill="#FF5A5A" {W(2)}/>
{face(64, 74, d=8, k=0.7)}
'''), "герой: горка салата оливье с горошком | сцена: на её вершине горошина водрузила красный флажок, вокруг ёлочки")

# 8 Фишерикс — мидия раскрылась и поёт на камне у моря
I["cafe-fisheriks-troitsk"] = (svg2("#E8F7FF", "#2A6FB8", f'''
<path d="M0 104 Q20 96 40 104 Q60 112 80 104 Q100 96 128 104 V128 H0Z" fill="#4AA3E0" {s()}/>
<path d="M18 110 Q24 94 50 94 Q80 96 96 110Z" fill="#9A9AA8" {s()}/>
<path d="M16 86 Q30 108 70 104 Q104 98 112 78 Q80 92 40 88Z" fill="#2E2A50" {s()}/>
<path d="M16 86 Q12 50 56 40 Q96 34 112 64 Q84 58 48 66 Q26 72 16 86Z" fill="#2E2A50" {s()}/>
<path d="M26 74 Q50 54 98 56" fill="none" stroke="#6A66A8" stroke-width="2.4"/>
<path d="M22 86 Q40 70 70 70 Q98 70 110 76 Q100 92 64 94 Q34 94 22 86Z" fill="#FF9A5A" {s()}/>
{eye(56, 80, 0.75)}{eye(78, 80, 0.75)}
<ellipse cx="67" cy="87" rx="4" ry="2.6" fill="#B03A3A"/>
<path d="M92 30 q4 -8 8 0 v-14 l12 -3 v14 q4 -8 8 0" fill="none" {W(2.4)}/>
<circle cx="96" cy="30" r="3.4" fill="{O}"/><circle cx="116" cy="27" r="3.4" fill="{O}"/>
'''), "герой: чёрная мидия-ракушка | сцена: раскрыла створки и распевает песню на камне у моря, вокруг летят ноты")

# 9 F. kitchen — начос горкой у дорожного указателя «59 км»
I["cafe-f-kitchen-chekhov"] = (svg2("#FFFDE8", "#E0B43A", f'''
<path d="M0 104 H128 V128 H0Z" fill="#6A6A7A" {s()}/>
<path d="M8 116 H28 M48 116 H72 M92 116 H120" stroke="#FFF" stroke-width="4"/>
<path d="M98 104 V40" stroke="#9AA0AA" stroke-width="5"/>
<rect x="84" y="24" width="30" height="20" rx="3" fill="#FFFFFF" {s()}/>
<text x="99" y="39" text-anchor="middle" font-family="Arial" font-weight="bold" font-size="13" fill="{O}">59</text>
<path d="M14 100 L40 54 L58 92Z" fill="#FFC93E" {s()}/>
<path d="M34 102 L62 50 L84 100Z" fill="#FFB52E" {s()}/>
<path d="M52 104 L76 68 L92 104Z" fill="#FFD25A" {s()}/>
<path d="M40 70 Q50 64 62 70 Q58 80 52 74 Q46 82 40 70Z" fill="#FF8A2A" {W(2)}/>
<circle cx="72" cy="88" r="3" fill="#E84A3A"/><circle cx="38" cy="88" r="3" fill="#5BBF4A"/>
{face(60, 82, d=7, k=0.65)}
'''), "герой: горка кукурузных начос с сырным соусом | сцена: ждёт у трассы под дорожным указателем «59»")

# 10 Casa Rosa — розовый зефир распускается как роза на стебле
I["cafe-casa-rosa-pushkino"] = (svg2("#FFF0F6", "#E86AA0", f'''
<path d="M64 128 V76" stroke="#3E9A4E" stroke-width="6"/>
<path d="M64 104 Q40 94 32 106 Q48 116 64 104Z M64 96 Q88 84 98 96 Q82 106 64 96Z" fill="#5BC06A" {W(2.4)}/>
<path d="M30 54 Q26 30 50 26 Q64 14 78 26 Q102 30 98 54 Q102 78 64 82 Q26 78 30 54Z" fill="#FFB6D2" {s()}/>
<path d="M44 46 Q46 32 64 32 Q82 32 84 46 M40 60 Q44 72 64 72 Q84 72 88 60" fill="none" stroke="#F07AA6" stroke-width="3"/>
<path d="M52 44 Q64 36 76 44" fill="none" stroke="#F07AA6" stroke-width="2.6"/>
{face(64, 56, d=9, k=0.8)}
{sparkle(108, 26, 6)}{sparkle(20, 34, 5)}
'''), "герой: розовый зефир с волнистыми лепестками | сцена: распустился на зелёном стебле, как садовая роза")

# 11 Турка — кубики лукума катаются с горки-подноса, пудра облачком
I["cafe-turka-tarasovka"] = (svg2("#FFF6F0", "#C0485A", f'''
<path d="M6 40 L118 96 L118 106 L6 50Z" fill="#E2B04A" {s()}/>
<path d="M14 46 L112 95" stroke="#F8DA8A" stroke-width="2"/>
<rect x="18" y="20" width="26" height="26" rx="5" transform="rotate(26 31 33)" fill="#FF8FB4" {s()}/>
<rect x="56" y="44" width="28" height="28" rx="5" transform="rotate(26 70 58)" fill="#FFFFFF" {s()}/>
<rect x="88" y="66" width="24" height="24" rx="5" transform="rotate(26 100 78)" fill="#B6E06A" {s()}/>
{face(70, 58, d=6, k=0.6)}
<circle cx="31" cy="33" r="1.4" fill="{O}"/><circle cx="37" cy="36" r="1.4" fill="{O}"/>
<circle cx="99" cy="78" r="1.4" fill="{O}"/><circle cx="104" cy="80" r="1.4" fill="{O}"/>
<g fill="#FFF" opacity=".9"><circle cx="48" cy="18" r="6"/><circle cx="56" cy="14" r="5"/><circle cx="60" cy="22" r="4"/><circle cx="16" cy="70" r="3"/><circle cx="24" cy="78" r="2"/><circle cx="84" cy="34" r="2.5"/></g>
'''), "герой: три кубика рахат-лукума в сахарной пудре | сцена: катятся с золотого подноса-горки, пудра взлетает облачком")

# 12 Джанико — три оладушка играют в чехарду
I["cafe-dzhaniko-pushkino"] = (svg2("#FFFDF2", "#9FD06A", f'''
<path d="M0 108 Q64 96 128 108 V128 H0Z" fill="#6BB04A" {s()}/>
<ellipse cx="28" cy="100" rx="22" ry="10" fill="#E8B060" {s()}/>
<ellipse cx="100" cy="100" rx="22" ry="10" fill="#E8B060" {s()}/>
{face(28, 98, d=6, k=0.55)}{face(100, 98, d=6, k=0.55)}
<path d="M30 86 Q44 30 64 28 Q86 30 96 84" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="3 5" stroke-linecap="round"/>
<g transform="rotate(-12 64 54)">
<ellipse cx="64" cy="54" rx="32" ry="16" fill="#F0C070" {s()}/>
<path d="M44 46 Q64 38 84 46" fill="none" stroke="#FFE2A0" stroke-width="3"/>
<path d="M54 42 Q60 54 52 62 Q66 56 72 44" fill="#F6A21E" {W(1.8)}/>
{face(66, 56, d=8, k=0.7)}</g>
'''), "герой: пышные золотистые оладьи | сцена: три оладушка играют в чехарду, средний перелетает через друзей с каплей мёда")

# 13 Urban Kitchen — бейгл катится, как колесо, по тротуару среди многоэтажек
I["cafe-urban-kitchen-kholmogory"] = (svg2("#F4F2FF", "#5A6A8A", f'''
<rect x="4" y="30" width="22" height="70" fill="#8C9AC8" {W(2)}/><rect x="98" y="20" width="26" height="80" fill="#7A88B8" {W(2)}/>
<rect x="28" y="50" width="16" height="50" fill="#A8B4DA" {W(2)}/>
<g fill="#FFE07A"><rect x="9" y="38" width="5" height="5"/><rect x="17" y="52" width="5" height="5"/><rect x="104" y="30" width="5" height="5"/><rect x="113" y="46" width="5" height="5"/><rect x="104" y="62" width="5" height="5"/><rect x="32" y="58" width="4" height="4"/></g>
<path d="M0 100 H128 V128 H0Z" fill="#B8BCC8" {s()}/>
<path d="M0 112 H128" stroke="#9AA0AE" stroke-width="2"/>
<circle cx="66" cy="70" r="30" fill="#D9A25A" {s()}/>
<circle cx="66" cy="70" r="10" fill="#B8BCC8" {s()}/>
<g fill="#FFF6DC"><ellipse cx="50" cy="52" rx="2" ry="1.2"/><ellipse cx="80" cy="50" rx="2" ry="1.2"/><ellipse cx="88" cy="74" rx="2" ry="1.2"/><ellipse cx="46" cy="84" rx="2" ry="1.2"/><ellipse cx="70" cy="94" rx="2" ry="1.2"/><ellipse cx="62" cy="46" rx="2" ry="1.2"/></g>
{eye(54, 64, 0.7)}{eye(78, 64, 0.7)}
<path d="M58 84 Q66 90 74 84" fill="none" {W(2.4)}/>
<path d="M22 106 Q30 100 34 106 M14 92 H28" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
'''), "герой: бейгл с кунжутом | сцена: катится, как колесо, по городскому тротуару между многоэтажками")

# 14 Дело вкуса — синнабон-улитка вытягивается пружинкой и подпрыгивает
I["cafe-delo-vkusa-fryazino"] = (svg2("#FFF8E6", "#C88A4A", f'''
<path d="M10 100 Q8 80 30 78 H98 Q120 80 118 100 Q118 116 98 116 H30 Q10 116 10 100Z" fill="#9AD0F0" {s()}/>
<path d="M22 92 Q64 86 106 92" fill="none" stroke="#C8E8FA" stroke-width="3"/>
<circle cx="64" cy="64" r="36" fill="#E8A860" {s()}/>
<path d="M67.0 64.0 L67.1 64.2 L67.2 64.5 L67.2 64.8 L67.3 65.0 L67.3 65.3 L67.3 65.6 L67.2 65.9 L67.1 66.2 L67.0 66.5 L66.9 66.8 L66.8 67.1 L66.6 67.4 L66.4 67.7 L66.1 68.0 L65.8 68.2 L65.5 68.5 L65.2 68.7 L64.9 68.9 L64.5 69.0 L64.1 69.2 L63.7 69.3 L63.3 69.3 L62.9 69.4 L62.4 69.4 L62.0 69.3 L61.5 69.2 L61.1 69.1 L60.6 69.0 L60.2 68.8 L59.8 68.6 L59.3 68.3 L58.9 68.0 L58.6 67.6 L58.2 67.3 L57.9 66.9 L57.6 66.4 L57.3 65.9 L57.1 65.4 L56.9 64.9 L56.7 64.4 L56.6 63.8 L56.5 63.2 L56.5 62.6 L56.5 62.0 L56.6 61.4 L56.7 60.8 L56.9 60.2 L57.1 59.6 L57.4 59.0 L57.7 58.4 L58.1 57.9 L58.5 57.4 L59.0 56.9 L59.5 56.4 L60.0 56.0 L60.6 55.6 L61.3 55.3 L61.9 55.0 L62.6 54.8 L63.3 54.6 L64.0 54.4 L64.8 54.4 L65.6 54.3 L66.3 54.4 L67.1 54.5 L67.9 54.7 L68.6 54.9 L69.4 55.2 L70.1 55.5 L70.8 55.9 L71.5 56.4 L72.1 56.9 L72.7 57.5 L73.3 58.2 L73.8 58.9 L74.3 59.6 L74.7 60.4 L75.0 61.2 L75.3 62.0 L75.6 62.9 L75.7 63.8 L75.8 64.7 L75.8 65.6 L75.8 66.5 L75.6 67.5 L75.4 68.4 L75.2 69.3 L74.8 70.2 L74.4 71.1 L73.9 71.9 L73.3 72.8 L72.7 73.5 L72.0 74.3 L71.2 74.9 L70.4 75.6 L69.6 76.1 L68.6 76.6 L67.7 77.0 L66.7 77.4 L65.7 77.7 L64.6 77.9 L63.5 78.0 L62.4 78.0 L61.3 77.9 L60.2 77.8 L59.1 77.6 L58.1 77.3 L57.0 76.9 L56.0 76.4 L55.0 75.8 L54.0 75.1 L53.1 74.4 L52.3 73.6 L51.5 72.7 L50.7 71.8 L50.1 70.8 L49.5 69.7 L49.0 68.6 L48.6 67.5 L48.2 66.3 L48.0 65.1 L47.9 63.8 L47.8 62.6 L47.9 61.3 L48.0 60.1 L48.3 58.8 L48.6 57.6 L49.1 56.3 L49.6 55.2 L50.2 54.0 L51.0 52.9 L51.8 51.9 L52.7 50.9 L53.7 49.9 L54.7 49.1 L55.9 48.3 L57.1 47.7 L58.3 47.1 L59.6 46.6 L61.0 46.2 L62.3 45.9 L63.7 45.7 L65.2 45.6 L66.6 45.7 L68.0 45.8 L69.4 46.1 L70.8 46.5 L72.2 46.9 L73.6 47.5 L74.9 48.2 L76.1 49.0 L77.3 49.9 L78.5 50.9 L79.5 52.0 L80.5 53.2 L81.4 54.5 L82.1 55.8 L82.8 57.2 L83.4 58.6 L83.9 60.1 L84.2 61.6 L84.4 63.2 L84.5 64.8 L84.5 66.4 L84.4 68.0 L84.1 69.6 L83.7 71.2 L83.2 72.7 L82.6 74.2 L81.8 75.7 L81.0 77.1 L80.0 78.4 L78.9 79.7 L77.7 80.9 L76.4 82.0 L75.0 83.0 L73.6 83.9 L72.1 84.7 L70.5 85.3 L68.8 85.9 L67.1 86.3 L65.4 86.6 L63.7 86.7 L61.9 86.7 L60.1 86.6 L58.4 86.3 L56.6 85.9 L54.9 85.4 L53.2 84.7 L51.6 83.9 L50.1 83.0 L48.6 81.9 L47.1 80.8 L45.8 79.5 L44.6 78.1 L43.5 76.6 L42.5 75.0 L41.6 73.4 L40.8 71.7 L40.2 69.9 L39.7 68.0 L39.3 66.2 L39.1 64.2 L39.1 62.3 L39.2 60.4 L39.4 58.4 L39.8 56.5 L40.4 54.6 L41.1 52.8 L41.9 51.0 L42.9 49.3 L44.0 47.6 L45.3 46.1 L46.6 44.6 L48.1 43.2 L49.7 42.0 L51.4 40.8 L53.2 39.8 L55.1 39.0 L57.0 38.2 L59.0 37.7 L61.0 37.3 L63.1 37.0 L65.2 36.9 L67.3 37.0 L69.4 37.2 L71.5 37.6 L73.5 38.1 L75.5 38.9 L77.5 39.7 L79.4 40.8 L81.2 41.9 L82.9 43.2 L84.6 44.7 L86.1 46.3 L87.5 48.0 L88.7 49.8 L89.8 51.7 L90.8 53.7 L91.6 55.8 L92.3 57.9 L92.8 60.1 L93.1 62.3 L93.3 64.6 L93.2 66.8 L93.0 69.1 L92.7 71.4 L92.1 73.6 L91.4 75.8 L90.5 77.9 L89.4 80.0 L88.2 81.9 L86.8 83.8 L85.3 85.6 L83.6 87.3 L81.8 88.8 L79.9 90.2 L77.9 91.5 L75.8 92.6" fill="none" stroke="#9A5A22" stroke-width="3.2" stroke-linecap="round"/>
<path d="M36 44 Q50 36 56 48 Q62 38 74 44 Q84 34 92 46" fill="none" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round"/>
<path d="M42 56 Q50 54 50 62 M78 52 Q86 50 88 60" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round"/>
<path d="M50 76 Q54 72 58 76 M70 76 Q74 72 78 76" fill="none" {W(2.6)}/>
<ellipse cx="44" cy="82" rx="4.5" ry="2.6" fill="#FF7FA8" opacity=".6"/><ellipse cx="84" cy="82" rx="4.5" ry="2.6" fill="#FF7FA8" opacity=".6"/>
<path d="M96 30 Q100 26 104 30 M106 20 Q110 16 114 20" fill="none" {W(2)}/>
<text x="110" y="34" font-family="Arial" font-weight="bold" font-size="11" fill="{O}">z</text>
'''), "герой: синнабон-улитка с белой глазурью | сцена: сладко спит, свернувшись клубочком на голубой подушке")

# 15 Жигули — солянка в горшочке на пеньке в сосновом бору
I["cafe-zhiguli-sofrino"] = (svg2("#EFFFF2", "#2F6E4A", f'''
<path d="M14 92 L26 40 L38 92Z M92 88 L106 30 L120 88Z" fill="#1E5A36" {W(2.4)}/>
<path d="M26 92 V100 M106 88 V100" stroke="#6A4A2A" stroke-width="4"/>
<path d="M36 100 H92 V122 H36Z" fill="#A87444" {s()}/>
<ellipse cx="64" cy="100" rx="28" ry="6" fill="#E2B880" {s()}/>
<path d="M66 100 m-4 0 a4 3 0 1 1 4 3" fill="none" stroke="#B88A54" stroke-width="2"/>
<path d="M40 60 Q40 94 64 94 Q88 94 88 60Z" fill="#7A4A2E" {s()}/>
<ellipse cx="64" cy="60" rx="25" ry="7" fill="#D8502A" {s()}/>
<circle cx="72" cy="58" r="6" fill="#FFF27A" {W(2)}/><path d="M72 52 V64 M66 58 H78" stroke="#E0C84A" stroke-width="1.4"/>
<circle cx="54" cy="59" r="3" fill="#2E2E3E"/>
<path d="M60 50 Q56 42 62 36 M70 48 Q68 40 74 34" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
{face(64, 78, d=8, k=0.7)}
'''), "герой: горшочек сборной солянки с долькой лимона и маслиной | сцена: стоит на пеньке в сосновом бору")

# 16 Баку сити — стопка кутабов с зеленью на фоне трёх башен-пламени
I["cafe-baku-siti-ramenskoe"] = (svg2("#FFF0E0", "#3A4FA0", f'''
<path d="M18 74 Q16 36 30 18 Q40 40 38 74Z" fill="#5A8AD8" {W(2.4)}/>
<path d="M48 70 Q46 24 64 6 Q82 24 80 70Z" fill="#6AA0F0" {W(2.4)}/>
<path d="M90 74 Q88 40 98 20 Q112 36 110 74Z" fill="#5A8AD8" {W(2.4)}/>
<path d="M58 30 L70 30 M56 44 L72 44 M54 58 L74 58" stroke="#BFD8FF" stroke-width="2"/>
<path d="M10 108 Q64 120 118 108 L114 118 Q64 128 14 118Z" fill="#E8E2D8" {s()}/>
<path d="M16 102 Q16 86 64 86 Q112 86 112 102 Q64 112 16 102Z" fill="#F2D49A" {s()}/>
<path d="M20 92 Q20 76 64 76 Q108 76 108 92 Q64 102 20 92Z" fill="#F6DCA6" {s()}/>
<path d="M24 82 Q24 64 64 64 Q104 64 104 82 Q64 92 24 82Z" fill="#FAE4B4" {s()}/>
<path d="M30 80 Q34 74 40 80 M84 78 Q90 72 96 78" fill="none" stroke="#4CAF50" stroke-width="3"/>
{face(64, 76, d=8, k=0.65)}
'''), "герой: стопка тонких азербайджанских кутабов с зеленью | сцена: лежит на блюде на фоне трёх синих башен-пламени Баку")

# 17 Happyterria — коржик рисует мелками смайлик на меловой доске
I["cafe-happyterria-ramenskoe"] = (svg2("#F0FFF4", "#F0A030", f'''
<rect x="10" y="20" width="76" height="56" rx="4" fill="#2F4A3A" {s()}/>
<path d="M10 76 H86" stroke="#B07A4A" stroke-width="6"/>
<circle cx="48" cy="46" r="16" fill="none" stroke="#FFF" stroke-width="2.6"/>
<circle cx="42" cy="42" r="2" fill="#FFF"/><circle cx="54" cy="42" r="2" fill="#FFF"/>
<path d="M40 52 Q48 58 56 52" fill="none" stroke="#FFF" stroke-width="2.4"/>
<path d="M18 30 l5 5 M74 64 q4 -6 8 0" stroke="#FFE07A" stroke-width="2.4" fill="none"/>
<circle cx="88" cy="88" r="28" fill="#E8B060" {s()}/>
<circle cx="88" cy="88" r="28" fill="none" stroke="#C88A3A" stroke-width="4" stroke-dasharray="6 5"/>
<g fill="#C88A3A"><circle cx="80" cy="76" r="2"/><circle cx="98" cy="78" r="2"/><circle cx="102" cy="98" r="2"/><circle cx="76" cy="100" r="2"/></g>
{face(88, 90, d=8, k=0.75)}
<path d="M64 84 L72 76" stroke="#FF5A8A" stroke-width="6" stroke-linecap="round"/>
<path d="M64 84 L72 76" {W(1.6)}/>
'''), "герой: круглый песочный коржик с зубчатым краем | сцена: рисует мелком весёлый смайлик на школьной меловой доске")

# 18 Вкус традиций — торт «Наполеон» осыпается крошкой-снежинками
I["cafe-vkus-traditsiy-reutov"] = (svg2("#F2F6FF", "#8A9AD0", f'''
<ellipse cx="64" cy="108" rx="50" ry="10" fill="#FFFFFF" {s()}/>
<path d="M22 56 H106 V100 H22Z" fill="#F8E6BE" {s()}/>
<g stroke="#E0B064" stroke-width="3"><path d="M22 66 H106"/><path d="M22 76 H106"/><path d="M22 86 H106"/></g>
<path d="M22 56 H106" {W(3.2)}/>
<path d="M20 50 Q64 42 108 50 V58 H20Z" fill="#E8C27A" {s()}/>
<g fill="#FFF8E0" stroke="{O}" stroke-width="1.4"><circle cx="34" cy="26" r="3"/><circle cx="54" cy="16" r="2.4"/><circle cx="78" cy="22" r="3"/><circle cx="98" cy="30" r="2.4"/><circle cx="66" cy="34" r="2"/><circle cx="44" cy="38" r="2"/></g>
{face(64, 80, d=11, k=0.8)}
<path d="M58 88 Q64 94 70 88" fill="#FF8A9A"/>
'''), "герой: прямоугольный торт «Наполеон» из тонких коржей | сцена: сверху на него падает крошка, как снежинки, а он ловит её язычком")

# 19 Сенешаль — пирог-крепость с зубцами на холме, флажок на башне
I["cafe-seneshal-solnechnogorsk"] = (svg2("#FFFCE8", "#7AB0E0", f'''
<path d="M0 110 Q64 78 128 110 V128 H0Z" fill="#7CC45A" {s()}/>
<path d="M26 98 V62 H34 V54 H42 V62 H52 V54 H60 V62 H68 V54 H76 V62 H86 V54 H94 V62 H102 V98Z" fill="#E4A85A" {s()}/>
<path d="M30 74 Q64 68 98 74" fill="none" stroke="#C8843A" stroke-width="2.4"/>
<path d="M52 98 V86 Q64 76 76 86 V98Z" fill="#9A5A2A" {W(2.4)}/>
<path d="M40 54 V40 H48 V54" fill="#E4A85A" {s()}/>
<path d="M44 40 V20" {W(2.4)}/><path d="M44 20 L60 25 L44 30Z" fill="#E83A5A" {W(2)}/>
<g fill="#FFFFFF" stroke="{O}" stroke-width="1.6"><circle cx="34" cy="54" r="3"/><circle cx="56" cy="54" r="3"/><circle cx="72" cy="54" r="3"/><circle cx="90" cy="54" r="3"/></g>
{face(64, 76, d=12, k=0.75, mouth=False)}
<path d="M58 82 Q64 76 70 82" fill="none" {W(2.2)}/>
'''), "герой: пирог в форме крепости с зубцами из теста | сцена: стоит на зелёном холме, на угловой башенке развевается флажок")

# 20 РК Русь — шаньга с картофельной шапкой сидит у колодца-журавля
I["cafe-rus-saltykovka"] = (svg2("#FFF8E8", "#B07A3A", f'''
<path d="M0 104 H128 V128 H0Z" fill="#A6C86A" {s()}/>
<path d="M88 104 V40" stroke="#7A5230" stroke-width="5"/>
<path d="M64 30 L124 60" stroke="#7A5230" stroke-width="4"/>
<path d="M70 32 V58" {W(2)}/><rect x="64" y="58" width="12" height="10" rx="2" fill="#9A9AA8" {W(2)}/>
<rect x="98" y="78" width="26" height="26" fill="#9A6A3A" {s()}/>
<path d="M98 86 H124 M98 94 H124" stroke="#6A4A2A" stroke-width="2"/>
<ellipse cx="44" cy="96" rx="34" ry="10" fill="#D8903A" {s()}/>
<path d="M14 92 Q16 64 44 62 Q72 64 74 92Z" fill="#E8A44A" {s()}/>
<path d="M22 76 Q28 58 44 58 Q60 58 66 76 Q44 84 22 76Z" fill="#FFE6A8" {s()}/>
<path d="M30 70 Q36 64 40 70 M48 66 Q54 62 58 68" fill="none" stroke="#E8B860" stroke-width="2.4"/>
{face(44, 84, d=8, k=0.65)}
'''), "герой: круглая шаньга с картофельной шапкой | сцена: отдыхает у деревенского колодца-журавля со срубом")

# 21 Salazkin — карельская калитка едет на деревянных салазках с горки
I["cafe-salazkin-vidnoe"] = (svg2("#F4FAFF", "#88B0DE", f'''
<path d="M0 54 L128 112 V128 H0Z" fill="#FFFFFF" {s()}/>
<g fill="#fff"><circle cx="20" cy="20" r="2.4"/><circle cx="96" cy="16" r="2"/><circle cx="112" cy="40" r="2.4"/><circle cx="60" cy="12" r="1.8"/></g>
<g transform="rotate(24 64 76)">
<path d="M24 92 H108 Q118 92 116 82" fill="none" stroke="#7A4A2A" stroke-width="4" stroke-linecap="round"/>
<path d="M34 92 V84 M60 92 V84 M86 92 V84" stroke="#7A4A2A" stroke-width="3"/>
<rect x="28" y="80" width="68" height="6" rx="2" fill="#B07A4A" {W(2)}/>
<path d="M30 80 Q28 56 62 52 Q96 56 94 80Z" fill="#E6C27A" {s()}/>
<path d="M38 72 Q38 60 62 60 Q86 60 86 72 Z" fill="#FFF1C8" {W(2)}/>
<path d="M30 80 l4 -6 4 6 4 -6 4 6 4 -6 4 6 4 -6 4 6 4 -6 4 6 4 -6 4 6 4 -6 4 6 4 -6 4 6" fill="none" stroke="#B8843A" stroke-width="2"/>
{face(62, 68, d=7, k=0.6)}</g>
<path d="M14 46 L26 50 M10 58 L22 62" stroke="#88B0DE" stroke-width="3" stroke-linecap="round"/>
'''), "герой: карельская калитка с волнистым краем | сцена: лихо съезжает с заснеженной горки на деревянных салазках")

# 22 Южный дворик — хычин сидит за столиком под виноградной лозой
I["cafe-yuzhny-dvorik-meshcherino"] = (svg2("#FFFBE0", "#E8A04A", f'''
<circle cx="104" cy="22" r="14" fill="#FFE04A" {W(2.4)}/>
<path d="M0 24 Q30 34 64 26 Q96 18 128 30" fill="none" stroke="#7A5A2A" stroke-width="4"/>
<path d="M14 30 Q8 40 16 44 Q24 38 14 30Z M44 30 Q38 42 48 44 Q54 36 44 30Z M78 26 Q74 38 84 38 Q88 30 78 26Z" fill="#5CB04A" {W(2)}/>
<g fill="#8A4AB0" stroke="{O}" stroke-width="1.4"><circle cx="30" cy="38" r="3.4"/><circle cx="36" cy="38" r="3.4"/><circle cx="33" cy="44" r="3.4"/><circle cx="64" cy="34" r="3.4"/><circle cx="70" cy="34" r="3.4"/><circle cx="67" cy="40" r="3.4"/></g>
<path d="M18 100 H110 V106 H18Z" fill="#C88A54" {W(2.4)}/>
<path d="M28 106 V124 M100 106 V124" stroke="#9A6A3A" stroke-width="5"/>
<ellipse cx="64" cy="86" rx="38" ry="15" fill="#F1D6A0" {s()}/>
<ellipse cx="64" cy="84" rx="30" ry="9" fill="#E6BE7A"/>
<g fill="#C88A3A"><circle cx="48" cy="80" r="2"/><circle cx="76" cy="88" r="2"/><circle cx="84" cy="78" r="1.6"/></g>
{face(64, 84, d=8, k=0.7)}
'''), "герой: круглый балкарский хычин | сцена: сидит за деревянным столиком во дворике под виноградной лозой и южным солнцем")

# 23 Манка — воздушное суфле поднимается из формочки, как воздушный шар
I["cafe-manka-vidnoe"] = (svg2("#F6F0FF", "#B88AE8", f'''
<g fill="#fff" opacity=".85"><circle cx="20" cy="42" r="7"/><circle cx="28" cy="38" r="6"/><circle cx="104" cy="54" r="6"/><circle cx="112" cy="50" r="5"/></g>
<path d="M30 116 L34 84 H94 L98 116Z" fill="#FFFFFF" {s()}/>
<path d="M38 86 V114 M50 86 V116 M64 86 V116 M78 86 V116 M90 86 V114" stroke="#D8D0EE" stroke-width="2.4"/>
<path d="M32 86 Q22 44 64 32 Q106 44 96 86Z" fill="#F7D48A" {s()}/>
<path d="M34 72 Q24 44 64 32 Q104 44 94 72 Q64 62 34 72Z" fill="#D9963E" {W(2.4)}/>
<g fill="#FFF8E8"><circle cx="50" cy="48" r="2"/><circle cx="70" cy="42" r="2"/><circle cx="82" cy="54" r="2"/><circle cx="58" cy="58" r="1.6"/></g>
{face(64, 76, d=10, k=0.75)}
<path d="M64 32 V18" stroke="#fff" stroke-width="2"/><path d="M58 18 Q64 10 70 18" fill="none" stroke="#fff" stroke-width="2.4"/>
'''), "герой: пышное ванильное суфле в белой формочке | сцена: поднимается высоко над краями и парит, как воздушный шар среди облаков")

# 24 Пронто Видное — тако бежит со всех ног, роняя кусочки
I["cafe-pronto-vidnoe"] = (svg2("#FFFDF0", "#E85A3A", f'''
<path d="M2 50 H24 M0 66 H20 M6 82 H26" stroke="#FFF" stroke-width="5" stroke-linecap="round"/>
<path d="M50 96 L40 114 M84 96 L96 112" {W(4)}/>
<ellipse cx="38" cy="116" rx="7" ry="3.6" fill="#5A4AB0" {W(2)}/><ellipse cx="100" cy="114" rx="7" ry="3.6" fill="#5A4AB0" {W(2)}/>
<path d="M32 90 Q34 40 68 36 Q102 40 104 90Z" fill="#7AD05A" {s()}/>
<path d="M36 70 Q50 58 62 66 Q74 56 90 64 Q98 70 100 80" fill="none" stroke="#E83A3A" stroke-width="5" stroke-linecap="round"/>
<path d="M26 92 Q26 46 68 44 Q110 46 110 92 Z" fill="#F4C25A" {s()}/>
<path d="M30 92 H108" {W(3)}/>
{face(68, 74, d=9, k=0.75)}
<circle cx="22" cy="104" r="3" fill="#E83A3A" {W(1.4)}/><rect x="12" y="94" width="5" height="5" fill="#7AD05A" {W(1.4)}/>
'''), "герой: хрустящий тако с начинкой | сцена: бежит со всех ног, роняя за собой кусочки помидора и салата")

# 25 Мельница — беляш сидит на мешке муки у жерновов
I["cafe-melnitsa-zheleznodorozhny"] = (svg2("#FFFFF2", "#C0B080", f'''
<circle cx="102" cy="88" r="22" fill="#A0A0A8" {s()}/>
<circle cx="102" cy="88" r="6" fill="#6A6A74" {W(2)}/>
<path d="M88 74 L96 82 M116 74 L108 82 M88 102 L96 94" stroke="#7A7A84" stroke-width="2.4"/>
<path d="M14 120 Q10 74 26 66 Q34 58 48 62 Q60 58 66 66 Q80 74 76 120Z" fill="#F4ECD8" {s()}/>
<path d="M32 62 Q40 54 52 60" fill="none" {W(2.4)}/>
<text x="44" y="104" text-anchor="middle" font-family="Arial" font-weight="bold" font-size="12" fill="#B08A4A">МУКА</text>
<ellipse cx="46" cy="52" rx="28" ry="14" fill="#D9963E" {s()}/>
<circle cx="46" cy="44" r="6" fill="#8A4A2A" {W(2)}/>
{face(46, 56, d=8, k=0.65)}
<g fill="#fff"><circle cx="86" cy="40" r="2.4"/><circle cx="92" cy="30" r="1.6"/><circle cx="20" cy="36" r="1.8"/></g>
'''), "герой: румяный беляш с открытой серединкой | сцена: сидит на мешке муки рядом с каменным жерновом мельницы")

# 26 Пицца Паоло (Янтарный) — пицца «Четыре сыра», четвертинки разъехались, как пазл
I["cafe-pizza-paolo-yantarny"] = (svg2("#FFF6DC", "#D88A2A", f'''
<path d="M60 60 L60 18 A42 42 0 0 0 18 60Z" fill="#FFE27A" {s()}/>
<path d="M68 60 L110 60 A42 42 0 0 0 68 18Z" fill="#FFF6D8" {s()}/>
<path d="M60 68 L18 68 A42 42 0 0 0 60 110Z" fill="#F6C24A" {s()}/>
<path d="M68 68 L68 110 A42 42 0 0 0 110 68Z" fill="#FFD9A0" {s()}/>
<g fill="#5A9AD8" opacity=".8"><circle cx="86" cy="36" r="3"/><circle cx="96" cy="48" r="2.4"/><circle cx="80" cy="48" r="2"/></g>
<g fill="#E89A3A"><circle cx="34" cy="86" r="3"/><circle cx="44" cy="96" r="2.4"/></g>
<g fill="#fff" stroke="{O}" stroke-width="1.4"><circle cx="86" cy="92" r="3"/><circle cx="96" cy="82" r="2.4"/></g>
<g fill="#FFFFFF" opacity=".7"><circle cx="38" cy="38" r="3"/><circle cx="48" cy="28" r="2.4"/></g>
{face(42, 46, d=5, k=0.5)}{face(86, 46, d=5, k=0.5)}{face(42, 82, d=5, k=0.5)}{face(86, 82, d=5, k=0.5)}
'''), "герой: пицца «Четыре сыра» из четырёх разноцветных четвертинок | сцена: четвертинки разъехались, как кусочки пазла, и улыбаются друг другу")

# 27 Венеция — фузилли плывут в гондоле под мостиком
I["cafe-venetsiya-kuchino"] = (svg2("#E8FFFA", "#2A8A9A", f'''
<path d="M-4 52 Q64 0 132 52 V62 Q64 14 -4 62Z" fill="#E8C49A" {s()}/>
<path d="M20 50 V60 M44 34 V46 M84 34 V46 M108 50 V60" stroke="#C49A6A" stroke-width="3"/>
<path d="M0 98 Q32 92 64 98 Q96 104 128 98 V128 H0Z" fill="#3AB0B8" {s()}/>
<path d="M10 106 Q32 102 54 106 M74 112 Q96 108 118 112" fill="none" stroke="#B8F0F0" stroke-width="2.4"/>
<path d="M12 86 Q20 100 64 100 Q108 100 118 82 Q110 92 64 92 Q22 92 12 86Z" fill="#2A2A3A" {s()}/>
<path d="M118 82 Q124 74 120 68" fill="none" {W(3)}/>
<g fill="#F6C84A" stroke="{O}" stroke-width="2.4">
<path d="M42 92 Q36 84 44 80 Q36 74 44 70 Q36 64 44 60 Q50 64 46 70 Q52 74 46 80 Q52 84 48 92Z"/>
<path d="M70 92 Q64 84 72 80 Q64 74 72 70 Q64 64 72 60 Q78 64 74 70 Q80 74 74 80 Q80 84 76 92Z"/>
</g>
{eye(41, 70, 0.5)}{eye(48, 70, 0.5)}{eye(69, 70, 0.5)}{eye(76, 70, 0.5)}
<path d="M92 92 L104 40" stroke="#8A5A2A" stroke-width="3"/>
'''), "герой: макароны-спиральки фузилли | сцена: две спиральки плывут в чёрной гондоле по каналу под каменным мостиком")

# 28 LukCafe — окрошка в тарелке, по ней плывёт яйцо-кораблик
I["cafe-lukcafe-balashikha"] = (svg2("#F2FFF8", "#6AB8D8", f'''
<ellipse cx="64" cy="82" rx="54" ry="26" fill="#FFFFFF" {s()}/>
<ellipse cx="64" cy="78" rx="44" ry="18" fill="#EEF6E6" {W(2.4)}/>
<g stroke="{O}" stroke-width="1.4"><rect x="34" y="76" width="7" height="7" fill="#FFC4A8"/><rect x="82" y="80" width="7" height="7" fill="#C8E8A0"/><rect x="58" y="86" width="6" height="6" fill="#FFF2B0"/><rect x="88" y="70" width="6" height="6" fill="#FFC4A8"/></g>
<path d="M28 70 Q32 66 36 70 M98 86 Q102 82 106 86" fill="none" stroke="#4CAF50" stroke-width="2.4"/>
<path d="M46 74 Q46 60 62 58 Q78 60 78 74Z" fill="#FFFFFF" {s()}/>
<ellipse cx="62" cy="66" rx="8" ry="6" fill="#FFC93E" {W(2)}/>
<path d="M62 58 V34" {W(2.4)}/><path d="M62 34 L80 46 L62 52Z" fill="#7ACB5A" {W(2)}/>
{eye(58, 66, 0.45)}{eye(66, 66, 0.45)}
<path d="M20 110 Q28 104 36 110 M90 112 Q98 106 106 112" fill="none" stroke="#fff" stroke-width="3"/>
'''), "герой: тарелка окрошки | сцена: по ней, как кораблик, плывёт половинка яйца с парусом из листика зелени")

# 29 Эйфория — трайфл в высоком стакане, вокруг взрываются конфетти
I["cafe-euforiya-krasnogorsk"] = (svg2("#FFF2FA", "#8A4AD8", f'''
<g stroke="{O}" stroke-width="1.4"><rect x="14" y="20" width="6" height="10" fill="#FFD84A" transform="rotate(20 17 25)"/><rect x="104" y="18" width="6" height="10" fill="#5AD0E8" transform="rotate(-24 107 23)"/><rect x="18" y="88" width="6" height="10" fill="#FF6A9A" transform="rotate(-30 21 93)"/><rect x="106" y="86" width="6" height="10" fill="#7AE07A" transform="rotate(30 109 91)"/><circle cx="30" cy="54" r="3" fill="#FF9A3A"/><circle cx="100" cy="56" r="3" fill="#FFD84A"/></g>
<path d="M40 30 H88 L84 112 Q84 118 78 118 H50 Q44 118 44 112Z" fill="#FFFFFF" opacity=".5" {s()}/>
<path d="M44 98 H84 L84 112 Q84 116 78 116 H50 Q44 116 44 112Z" fill="#8A4A2A"/>
<path d="M43 82 H85 V98 H44Z" fill="#FFF2D0"/>
<path d="M42 66 H86 L85 82 H43Z" fill="#E83A6A"/>
<path d="M41 50 H87 L86 66 H42Z" fill="#FFF8E8"/>
<path d="M40 30 H88 L84 112 Q84 118 78 118 H50 Q44 118 44 112Z" fill="none" {s()}/>
<path d="M38 50 Q46 38 54 46 Q62 34 72 44 Q82 36 90 50Z" fill="#FFFFFF" {s()}/>
<circle cx="64" cy="34" r="6" fill="#E8203A" {W(2)}/>
{face(64, 86, d=9, k=0.7)}
'''), "герой: десерт трайфл слоями в высоком стакане | сцена: празднует, а вокруг взрываются разноцветные конфетти")

# 30 Пицца Паоло (Одинцово) — мини-пиццы на шпажках водят хоровод
I["cafe-pizza-paolo-odintsovo"] = (svg2("#F0FFF0", "#3FA86A", f'''
<ellipse cx="64" cy="70" rx="46" ry="30" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="4 6"/>
<g>
<path d="M30 74 V110" stroke="#C49A6A" stroke-width="3"/><circle cx="30" cy="62" r="14" fill="#E8A44A" {s()}/><circle cx="30" cy="62" r="10" fill="#E8483A"/><circle cx="26" cy="58" r="2.4" fill="#FFF"/><circle cx="34" cy="64" r="2.4" fill="#FFF"/>
<path d="M64 52 V96" stroke="#C49A6A" stroke-width="3"/><circle cx="64" cy="40" r="16" fill="#E8A44A" {s()}/><circle cx="64" cy="40" r="12" fill="#FFD25A"/><circle cx="58" cy="36" r="3" fill="#7ACB5A"/><circle cx="70" cy="44" r="3" fill="#E8483A"/>
<path d="M98 74 V110" stroke="#C49A6A" stroke-width="3"/><circle cx="98" cy="62" r="14" fill="#E8A44A" {s()}/><circle cx="98" cy="62" r="10" fill="#FF8A5A"/><circle cx="94" cy="66" r="2.4" fill="#2E2E3E"/><circle cx="102" cy="58" r="2.4" fill="#2E2E3E"/>
</g>
{face(30, 66, d=4, k=0.4, blush=False)}{face(64, 44, d=5, k=0.5, blush=False)}{face(98, 66, d=4, k=0.4, blush=False)}
<path d="M38 66 Q48 58 52 50 M90 66 Q80 58 76 50" fill="none" {W(2.6)}/>
'''), "герой: три мини-пиццы на деревянных шпажках | сцена: взялись за руки и водят хоровод")

# 31 Золотой улей — торт в форме улья, из летка вылетает пчёлка
I["cafe-zolotoy-uley-trekhgorka"] = (svg2("#FFFBE0", "#E8B21E", f'''
<ellipse cx="64" cy="112" rx="48" ry="8" fill="#FFFFFF" {s()}/>
<path d="M30 110 Q26 96 34 86 Q24 76 36 64 Q30 52 44 42 Q48 26 64 24 Q80 26 84 42 Q98 52 92 64 Q104 76 94 86 Q102 96 98 110Z" fill="#FFC93E" {s()}/>
<path d="M32 86 H96 M34 64 H94 M46 42 H82" stroke="#E09A1E" stroke-width="3"/>
<path d="M54 110 V100 Q64 92 74 100 V110Z" fill="#6A3A1E" {W(2.4)}/>
{face(64, 74, d=10, k=0.8)}
<g transform="translate(98 26)"><ellipse cx="0" cy="0" rx="9" ry="7" fill="#FFD84A" {W(2.2)}/><path d="M-3 -6 V6 M3 -6 V6" stroke="{O}" stroke-width="2.4"/><ellipse cx="-2" cy="-10" rx="5" ry="4" fill="#fff" opacity=".9" {W(1.6)}/><ellipse cx="5" cy="-10" rx="5" ry="4" fill="#fff" opacity=".9" {W(1.6)}/><circle cx="7" cy="0" r="1.4" fill="{O}"/></g>
<path d="M76 98 Q86 76 92 38" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 5"/>
'''), "герой: медовый торт в форме золотого улья | сцена: из круглого летка у основания вылетает пчёлка по пунктирной дорожке")

# 32 Бриошь — кейк-попы букетом в стаканчике
I["cafe-briosh-podolsk"] = (svg2("#F0F8FF", "#5A7AE8", f'''
<path d="M40 82 L46 120 H82 L88 82Z" fill="#FF8AB0" {s()}/>
<path d="M42 92 H86 M44 104 H84" stroke="#fff" stroke-width="3"/>
<path d="M64 82 V46 M46 82 L34 50 M82 82 L96 52" stroke="#FFFFFF" stroke-width="4"/>
<path d="M64 82 V46 M46 82 L34 50 M82 82 L96 52" stroke="{O}" stroke-width="1.2" opacity=".5"/>
<circle cx="64" cy="36" r="16" fill="#7A4A2A" {s()}/>
<path d="M50 30 Q64 18 78 30 Q72 26 64 28 Q56 26 50 30Z" fill="#FFF" opacity=".5"/>
<circle cx="32" cy="44" r="13" fill="#FFB6D2" {s()}/>
<circle cx="98" cy="46" r="13" fill="#FFFFFF" {s()}/>
<g fill="#FFD84A"><rect x="58" y="24" width="4" height="2" transform="rotate(30 60 25)"/><rect x="70" y="40" width="4" height="2"/></g>
<g fill="#5AC8E8"><rect x="26" y="38" width="4" height="2"/><rect x="36" y="48" width="4" height="2" transform="rotate(-30 38 49)"/></g>
<g fill="#FF6A6A"><rect x="94" y="40" width="4" height="2"/><rect x="102" y="50" width="4" height="2" transform="rotate(40 104 51)"/></g>
{face(64, 38, d=6, k=0.55)}
'''), "герой: три кейк-попа в цветной посыпке | сцена: стоят букетом в розовом бумажном стаканчике, как цветы")

# 33 Родник — стакан клюквенного киселя у родника
I["cafe-rodnik-mamontovka"] = (svg2("#ECFFF6", "#3A9A8A", f'''
<path d="M0 82 Q20 70 40 76 Q30 90 0 96Z" fill="#9AA0A8" {s()}/>
<path d="M30 82 Q40 92 34 108 Q52 112 72 120 Q90 126 128 120 V128 H0 V104Z" fill="#7AD0F0" {s()}/>
<path d="M28 84 Q30 92 38 96" fill="none" stroke="#fff" stroke-width="3"/>
<path d="M14 104 Q22 100 30 106 M60 118 Q70 114 80 120" fill="none" stroke="#fff" stroke-width="2.4"/>
<path d="M64 34 H104 L100 102 H68Z" fill="#E8304A" {s()}/>
<path d="M66 44 H102" stroke="#FF8A9A" stroke-width="4"/>
<path d="M64 34 H104" {W(3)}/>
<path d="M72 50 V94 M84 50 V96 M96 50 V94" stroke="#C0203A" stroke-width="1.6" opacity=".5"/>
<circle cx="96" cy="28" r="6" fill="#C0203A" {W(2)}/><path d="M96 22 Q98 14 104 12" fill="none" stroke="#3A8A3A" stroke-width="2"/>
{face(84, 72, d=8, k=0.7)}
'''), "герой: гранёный стакан клюквенного киселя с ягодкой | сцена: стоит у лесного родника, бьющего из-под серого камня")

# 34 Маэстро вкуса — шоколадный мусс в бокале дирижирует, вокруг ноты
I["cafe-maestro-vkusa-serebryanka"] = (svg2("#FFF6EC", "#5A3A8A", f'''
<path d="M64 98 V116" {W(4)}/><ellipse cx="64" cy="118" rx="18" ry="4" fill="#E8E8F4" {W(2.4)}/>
<path d="M34 50 Q34 98 64 98 Q94 98 94 50Z" fill="#E8E8F4" opacity=".6" {s()}/>
<path d="M37 62 Q40 94 64 94 Q88 94 91 62Z" fill="#6A3A22"/>
<path d="M34 50 Q34 98 64 98 Q94 98 94 50Z" fill="none" {s()}/>
<path d="M32 52 Q40 40 50 48 Q58 36 70 46 Q80 38 88 48 Q98 44 96 54 Q64 60 32 52Z" fill="#FFF6E6" {s()}/>
<path d="M90 60 L116 32" stroke="#F4F0E8" stroke-width="3.4" stroke-linecap="round"/>
<path d="M90 60 L116 32" {W(1.2)}/>
<circle cx="114" cy="34" r="2" fill="{O}"/>
<path d="M22 34 v-14 l10 -3 v14" fill="none" {W(2.4)}/><circle cx="20" cy="34" r="3.4" fill="{O}"/><circle cx="30" cy="31" r="3.4" fill="{O}"/>
<path d="M58 24 v-12" {W(2.4)}/><circle cx="55" cy="24" r="3.4" fill="{O}"/><path d="M58 12 q6 2 6 8" fill="none" {W(2)}/>
{face(64, 76, d=9, k=0.75)}
'''), "герой: шоколадный мусс со сливками в бокале на ножке | сцена: взмахивает дирижёрской палочкой, а вокруг разлетаются ноты")

# 35 АрмаВир — кюфта-шарик катится по виноградной лозе
I["cafe-armavir-mamontovka"] = (svg2("#FBF0FF", "#A8508A", f'''
<path d="M-4 100 Q30 70 64 92 Q98 112 132 80" fill="none" stroke="#7A5A2A" stroke-width="6" stroke-linecap="round"/>
<path d="M20 86 Q10 70 24 66 Q32 76 20 86Z M100 98 Q96 112 110 112 Q114 100 100 98Z" fill="#6AC04A" {W(2)}/>
<g fill="#7A3A9A" stroke="{O}" stroke-width="1.4"><circle cx="40" cy="96" r="4"/><circle cx="47" cy="96" r="4"/><circle cx="43" cy="103" r="4"/><circle cx="88" cy="112" r="4"/><circle cx="95" cy="110" r="4"/></g>
<circle cx="66" cy="56" r="28" fill="#C46A3A" {s()}/>
<g fill="#E8945A"><circle cx="52" cy="44" r="3"/><circle cx="80" cy="48" r="2.4"/><circle cx="74" cy="72" r="3"/><circle cx="50" cy="68" r="2"/></g>
<path d="M50 34 Q56 30 62 34 M70 32 Q76 30 80 36" fill="none" stroke="#5ABF4A" stroke-width="3"/>
{face(66, 58, d=9, k=0.8)}
<path d="M30 46 Q24 54 30 62 M26 40 Q16 52 24 66" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
'''), "герой: армянская кюфта-шарик с зеленью | сцена: катится по изогнутой виноградной лозе, мимо гроздей винограда")

# 36 Мелуна — селёдка под шубой укуталась в шубку и машет плавником
I["cafe-meluna-pushkino"] = (svg2("#F0F6FF", "#C83A6A", f'''
<ellipse cx="64" cy="112" rx="50" ry="8" fill="#FFFFFF" {s()}/>
<path d="M22 108 V64 Q22 50 64 50 Q106 50 106 64 V108Z" fill="#B8325A" {s()}/>
<path d="M22 78 H106" stroke="#F4C24A" stroke-width="5"/>
<path d="M22 92 H106" stroke="#FFF2D8" stroke-width="5"/>
<path d="M22 102 H106" stroke="#E8823A" stroke-width="4"/>
<path d="M22 64 Q22 50 64 50 Q106 50 106 64 Q64 72 22 64Z" fill="#FFF8F0" {W(2.4)}/>
<g fill="#FFD84A"><circle cx="40" cy="58" r="2"/><circle cx="58" cy="60" r="2"/><circle cx="84" cy="58" r="2"/></g>
<path d="M98 54 L120 40 L116 56 L124 66 Z" fill="#9AB0C8" {s()}/>
<path d="M30 60 L14 44 L10 58Z" fill="#9AB0C8" {W(2.4)}/>
{face(64, 74, d=10, k=0.8)}
'''), "герой: салат «селёдка под шубой» слоями | сцена: укутался в свекольную шубку, из-под неё торчит хвост, а селёдка машет плавником")

# 37 Бум-Бум — кукурузные палочки взлетают из пачки фонтаном
I["cafe-bum-bum-ramenskoe"] = (svg2("#FFFDE8", "#4A8AE8", f'''
<path d="M38 74 L44 122 H84 L90 74Z" fill="#FF5A3A" {s()}/>
<path d="M40 86 H88" stroke="#FFD84A" stroke-width="6"/>
<path d="M50 100 L56 94 L62 104 L70 92 L76 102" fill="none" stroke="#FFF" stroke-width="3"/>
<g fill="#FFE07A" stroke="{O}" stroke-width="2.2">
<rect x="58" y="20" width="10" height="30" rx="5" transform="rotate(4 63 35)"/>
<rect x="30" y="36" width="10" height="28" rx="5" transform="rotate(-34 35 50)"/>
<rect x="88" y="34" width="10" height="28" rx="5" transform="rotate(34 93 48)"/>
<rect x="46" y="44" width="9" height="24" rx="4.5" transform="rotate(-14 50 56)"/>
<rect x="74" y="44" width="9" height="24" rx="4.5" transform="rotate(16 78 56)"/>
</g>
{face(64, 108, d=9, k=0.65)}
<path d="M18 26 L24 32 M110 22 L104 28 M14 64 H22 M106 66 H114" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
'''), "герой: сладкие кукурузные палочки | сцена: с хлопком вылетают фонтаном из открытой красной пачки")

# 38 Бонкейк — сочник несёт на подносе маленький тортик-подарок
I["cafe-bonkeik-reutov"] = (svg2("#FFF4F0", "#E87A5A", f'''
<path d="M14 92 Q14 54 64 52 Q114 54 114 92 Q64 102 14 92Z" fill="#EBB36A" {s()}/>
<path d="M30 86 Q32 66 64 66 Q96 66 98 86 Q64 92 30 86Z" fill="#FFF6E0" {s()}/>
{face(64, 80, d=9, k=0.7)}
<path d="M28 62 L34 48 M100 62 L94 48" {W(3.4)}/>
<path d="M26 46 H102" stroke="#C8C8D8" stroke-width="6" stroke-linecap="round"/>
<path d="M26 46 H102" {W(1.4)}/>
<path d="M50 43 H78 V22 H50Z" fill="#FFB6D2" {s()}/>
<path d="M48 22 H80" {W(3.2)}/>
<path d="M64 22 V14" {W(2)}/><path d="M64 14 Q60 8 64 4 Q68 8 64 14Z" fill="#FFB02E" {W(1.6)}/>
<path d="M50 32 Q57 36 64 32 Q71 36 78 32" fill="none" stroke="#fff" stroke-width="2.4"/>
'''), "герой: сочник с творожной начинкой | сцена: поднял над головой поднос с маленьким розовым тортиком со свечкой")

# 39 Дедас Пури — ачма-слоёный пирог, слои поднимаются лесенкой
I["cafe-dedas-puri-reutov"] = (svg2("#FFFEF4", "#E09A5A", f'''
<rect x="14" y="98" width="100" height="14" rx="3" fill="#A0663A" {s()}/>
<path d="M22 98 V84 H106 V98Z" fill="#F2D08A" {s()}/>
<path d="M30 84 V70 H98 V84Z" fill="#F6DA9A" {s()}/>
<path d="M38 70 V56 H90 V70Z" fill="#F9E2AA" {s()}/>
<path d="M46 56 V42 Q64 34 82 42 V56Z" fill="#E8B060" {s()}/>
<g fill="#FFFFFF"><rect x="26" y="88" width="8" height="3" rx="1.5"/><rect x="92" y="88" width="8" height="3" rx="1.5"/><rect x="34" y="74" width="8" height="3" rx="1.5"/><rect x="84" y="74" width="8" height="3" rx="1.5"/></g>
{face(64, 62, d=9, k=0.65)}
<path d="M58 34 Q54 26 60 20 M70 32 Q68 24 74 18" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
'''), "герой: грузинская ачма из тонких слоёв теста с сыром | сцена: слои поднимаются вверх ступеньками, как лесенка-пирамида")

# 40 Русские традиции — холодец дрожит на блюде
I["cafe-russkie-traditsii-reutov"] = (svg2("#F8F6FF", "#4A6AB0", f'''
<ellipse cx="64" cy="102" rx="54" ry="14" fill="#FFFFFF" {s()}/>
<path d="M22 96 Q20 54 64 50 Q108 54 106 96 Q64 104 22 96Z" fill="#F6E2B0" opacity=".85" {s()}/>
<g fill="#E8A06A" stroke="#C8784A" stroke-width="1.4"><rect x="36" y="66" width="10" height="8" rx="2"/><rect x="80" y="70" width="10" height="8" rx="2"/><rect x="60" y="82" width="9" height="7" rx="2"/></g>
<circle cx="86" cy="58" r="4" fill="#FF8A3A" {W(1.6)}/><path d="M38 84 Q42 80 46 84" fill="none" stroke="#5AB04A" stroke-width="2.4"/>
<path d="M14 64 Q10 72 14 80 M114 64 Q118 72 114 80 M10 58 Q4 72 10 86 M118 58 Q124 72 118 86" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
{eye(54, 70, 0.75)}{eye(74, 70, 0.75)}
<path d="M56 80 Q60 76 64 80 Q68 84 72 80" fill="none" {W(2.4)}/>
'''), "герой: прозрачный холодец с морковными звёздочками | сцена: дрожит на большом белом блюде, волнистые линии вокруг")

# 41 Basilico — гнездо спагетти песто с базиликом-чубчиком
I["cafe-basilico-vidnoe"] = (svg2("#F2FFF0", "#2F8A3A", f'''
<ellipse cx="64" cy="98" rx="54" ry="18" fill="#FFFFFF" {s()}/>
<path d="M24 92 Q20 62 64 56 Q108 62 104 92 Q64 100 24 92Z" fill="#FFE08A" {s()}/>
<path d="M30 84 Q44 66 60 80 Q72 64 86 80 Q96 70 100 86 M36 76 Q50 62 64 72 Q80 60 94 74" fill="none" stroke="#E8B84A" stroke-width="3"/>
<path d="M44 92 Q58 82 70 90 Q82 82 92 90" fill="none" stroke="#E8B84A" stroke-width="3"/>
<path d="M64 56 Q50 34 62 22 Q72 38 64 56Z" fill="#3FB04A" {W(2.4)}/>
<path d="M66 54 Q84 38 96 46 Q82 58 66 54Z" fill="#5AC85A" {W(2.4)}/>
<path d="M62 56 Q44 44 34 52 Q48 62 62 56Z" fill="#5AC85A" {W(2.4)}/>
<path d="M64 52 Q62 40 62 28" fill="none" stroke="#2A8A3A" stroke-width="1.6"/>
{face(64, 76, d=9, k=0.75)}
'''), "герой: гнездо спагетти песто | сцена: на макушке, как чубчик, торчат три ярко-зелёных листа базилика")

# 42 Пицца №1 — кусок пиццы-альпинист водружает флажок «1» на сырную гору
I["cafe-pizza-1-khimki"] = (svg2("#FFF8E0", "#5AA0E8", f'''
<path d="M-4 116 L40 58 L64 80 L86 46 L132 116Z" fill="#FFD84A" {s()}/>
<g fill="#F2B82A"><circle cx="46" cy="90" r="5"/><circle cx="84" cy="80" r="4"/><circle cx="100" cy="100" r="6"/><circle cx="28" cy="104" r="4"/></g>
<path d="M86 46 V20" {W(2.6)}/><path d="M86 20 L106 26 L86 32Z" fill="#E83A3A" {W(2)}/>
<text x="93" y="30" text-anchor="middle" font-family="Arial" font-weight="bold" font-size="9" fill="#FFF">1</text>
<g transform="rotate(-18 60 54)">
<path d="M46 30 L74 30 L60 76Z" fill="#F6C24A" {s()}/>
<path d="M44 26 Q60 20 76 26 L74 32 Q60 28 46 32Z" fill="#D9963E" {W(2.4)}/>
<circle cx="56" cy="40" r="3.4" fill="#E8483A"/><circle cx="66" cy="48" r="3" fill="#E8483A"/>
{face(60, 46, d=5, k=0.5)}</g>
<path d="M74 54 L84 46" {W(3)}/>
'''), "герой: треугольный кусок пиццы-альпинист | сцена: взобрался на вершину сырной горы и водружает красный флажок «1»")

# 43 Милана (Железнодорожный) — ризотто по-милански, сверху падают сырные снежинки-стружки
I["cafe-milana-zheleznodorozhny"] = (svg2("#F4F0FF", "#3A3A8A", f'''
<ellipse cx="64" cy="96" rx="54" ry="20" fill="#FFFFFF" {s()}/>
<ellipse cx="64" cy="92" rx="40" ry="12" fill="#E8E8F2"/>
<path d="M28 92 Q26 62 64 58 Q102 62 100 92 Q64 100 28 92Z" fill="#FFC62E" {s()}/>
<g fill="#FFE27A" stroke="#E8A41E" stroke-width="1.2"><ellipse cx="44" cy="80" rx="3" ry="2"/><ellipse cx="54" cy="72" rx="3" ry="2"/><ellipse cx="80" cy="74" rx="3" ry="2"/><ellipse cx="88" cy="84" rx="3" ry="2"/><ellipse cx="70" cy="88" rx="3" ry="2"/><ellipse cx="40" cy="90" rx="3" ry="2"/></g>
{face(64, 78, d=10, k=0.75)}
<g fill="#FFFBEA" stroke="{O}" stroke-width="1.4">
<path d="M28 22 q6 -4 10 2 q-6 4 -10 -2Z"/><path d="M58 14 q6 -4 10 2 q-6 4 -10 -2Z"/><path d="M92 24 q6 -4 10 2 q-6 4 -10 -2Z"/><path d="M42 40 q6 -4 10 2 q-6 4 -10 -2Z"/><path d="M78 42 q6 -4 10 2 q-6 4 -10 -2Z"/></g>
'''), "герой: жёлтое шафрановое ризотто по-милански | сцена: на него с неба падают сырные стружки, как снежинки")

# 44 Милана (Чугунова) — шницель держит дольку лимона, как зонтик под дождём из соуса
I["cafe-milana-chugunova"] = (svg2("#FFFFF0", "#7A9A3A", f'''
<g fill="#E8E0B8"><path d="M20 10 l-3 8" stroke="#D8C88A" stroke-width="3"/><path d="M40 4 l-3 8" stroke="#D8C88A" stroke-width="3"/><path d="M96 8 l-3 8" stroke="#D8C88A" stroke-width="3"/><path d="M114 22 l-3 8" stroke="#D8C88A" stroke-width="3"/></g>
<path d="M30 46 Q64 6 98 46 Q90 40 82 46 Q73 38 64 46 Q55 38 46 46 Q38 40 30 46Z" fill="#FFF04A" {s()}/>
<path d="M64 46 L64 18 M64 46 L44 26 M64 46 L84 26" stroke="#E8D020" stroke-width="2"/>
<path d="M64 46 V64" {W(2.6)}/>
<path d="M14 92 Q10 66 40 64 Q64 58 88 64 Q118 66 114 92 Q118 112 88 112 Q64 118 40 112 Q10 112 14 92Z" fill="#D9963E" {s()}/>
<g fill="#B8742A"><circle cx="30" cy="80" r="2"/><circle cx="50" cy="104" r="2"/><circle cx="96" cy="78" r="2"/><circle cx="100" cy="100" r="2"/><circle cx="74" cy="104" r="1.6"/><circle cx="38" cy="96" r="1.6"/></g>
{face(64, 88, d=11, k=0.85)}
<path d="M64 64 Q68 70 66 76" fill="none" {W(2.6)}/>
'''), "герой: огромный шницель в золотистой панировке | сцена: прячется от дождика под долькой лимона, как под зонтиком")

# 45 Милана (Красноармейская) — кантуччи плывут в чашке какао, как лодочки
I["cafe-milana-krasnoarmeyskaya"] = (svg2("#FFF2EA", "#B0603A", f'''
<path d="M18 52 H110 L102 104 Q100 114 90 114 H38 Q28 114 26 104Z" fill="#5AB0E8" {s()}/>
<path d="M108 62 Q126 62 124 80 Q122 94 104 94" fill="none" {W(4.4)}/>
<ellipse cx="64" cy="54" rx="46" ry="10" fill="#7A4A2E" {s()}/>
<path d="M30 54 Q34 40 48 42 L56 54Z" fill="#F0CE8A" {s()}/>
<path d="M58 54 Q62 36 80 38 L90 54Z" fill="#F0CE8A" {s()}/>
<g fill="#FFFFFF" stroke="#C8A06A" stroke-width="1.2"><ellipse cx="42" cy="48" rx="2.4" ry="1.8"/><ellipse cx="72" cy="44" rx="2.6" ry="2"/><ellipse cx="80" cy="50" rx="2.4" ry="1.8"/></g>
{eye(64, 46, 0.45)}{eye(72, 50, 0.45)}
{face(64, 82, d=11, k=0.8)}
<path d="M44 26 Q40 18 46 12 M84 26 Q80 18 86 12" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
'''), "герой: два миндальных печенья кантуччи | сцена: плавают, как лодочки, в голубой чашке горячего какао")


if __name__ == "__main__":
    reg = os.path.join(ROOT, "icons-src", "subjects.txt")
    lines = open(reg, encoding="utf-8").read().splitlines()
    lines = [l for l in lines if l.split(" — ", 1)[0] not in I]
    for pid, (svg_, subj) in I.items():
        open(os.path.join(ROOT, "icons-src", pid + ".svg"), "w").write(svg_)
        lines.append(f"{pid} — {subj}")
    open(reg, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("иконок:", len(I))
