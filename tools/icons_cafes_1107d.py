"""Робот cafes, 2026-11-07 (07 UTC): иконки 55 новых кафе. Каждая придумана и нарисована отдельно
(правило абсолютной уникальности: свой герой, своя сцена, своя компоновка и палитра фона).
Запуск из корня: python3 tools/icons_cafes_1107d.py  → icons-src/<id>.svg + строки в icons-src/subjects.txt"""
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

# 1 Встречасто (Доллежаля) — две чашки капучино встретились и чокаются, над ними сердечко из пенки
I["cafe-vstrechasto-dollezhalya"] = (svg2("#E3FFF6", "#3FB8A0", f'''
<ellipse cx="64" cy="110" rx="56" ry="12" fill="#B7794A" {s()}/>
<g transform="rotate(14 40 76)">
<path d="M16 58 H62 L58 96 Q56 102 50 102 H28 Q22 102 20 96Z" fill="#FFFFFF" {s()}/>
<path d="M62 66 Q74 66 72 78 Q70 88 58 86" fill="none" {W(3.4)}/>
<ellipse cx="39" cy="58" rx="23" ry="6" fill="#C98B55" {W(2.6)}/>
<path d="M33 57 Q36 53 39 57 Q42 53 45 57 L39 61Z" fill="#FFF3E0"/>
{face(39, 78, d=8, k=0.75)}</g>
<g transform="rotate(-14 88 76)">
<path d="M66 58 H112 L108 96 Q106 102 100 102 H78 Q72 102 70 96Z" fill="#FFE07A" {s()}/>
<path d="M66 66 Q54 66 56 78 Q58 88 70 86" fill="none" {W(3.4)}/>
<ellipse cx="89" cy="58" rx="23" ry="6" fill="#C98B55" {W(2.6)}/>
<circle cx="89" cy="58" r="3" fill="#FFF3E0"/>
{face(89, 78, d=8, k=0.75)}</g>
<path d="M64 26 Q56 16 50 24 Q46 32 64 42 Q82 32 78 24 Q72 16 64 26Z" fill="#FF6F91" {W(2.4)}/>
<path d="M50 44 L44 38 M78 44 L84 38" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
'''), "герой: две чашки капучино с латте-артом | сцена: встретились за круглым столиком и чокаются, над ними сердечко")

# 2 Встречасто (Рабочая) — голубцы-двойняшки укрылись капустным листом как одеялом
I["cafe-vstrechasto-rabochaya"] = (svg2("#F1FFE0", "#8CCB5A", f'''
<ellipse cx="64" cy="98" rx="54" ry="16" fill="#FFFFFF" {s()}/>
<ellipse cx="64" cy="94" rx="44" ry="10" fill="#F4E9D8"/>
<ellipse cx="46" cy="76" rx="20" ry="16" fill="#E9A06B" {s()}/>
<ellipse cx="82" cy="76" rx="20" ry="16" fill="#E9A06B" {s()}/>
{face(46, 72, d=6, k=0.65)}{face(82, 72, d=6, k=0.65)}
<path d="M18 88 Q22 66 44 78 Q60 62 80 78 Q100 66 110 88 Q108 100 64 102 Q20 100 18 88Z" fill="#B6E07A" {s()}/>
<path d="M30 92 Q46 84 64 90 M64 90 Q82 82 98 92 M64 90 V100 M42 88 L38 96 M86 88 L90 96" fill="none" stroke="#7DB548" stroke-width="2.2"/>
<path d="M30 50 Q34 44 30 38 M96 50 Q100 44 96 38" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" opacity=".8"/>
<path d="M86 30 Q92 22 98 28" fill="none" stroke="#5E9A3A" stroke-width="2"/><text x="100" y="30" font-family="Arial" font-weight="bold" font-size="10" fill="{O}">z</text>
'''), "герой: голубцы-двойняшки | сцена: дремлют на блюде, укрывшись капустным листом, как одеялом")

# 3 Мильфей (Свердлова) — пирожное мильфей слоями с глазурью-ёлочкой делает реверанс на кружевной салфетке
I["cafe-milfey-sverdlova"] = (svg2("#FFF0F6", "#F07FAE", f'''
<circle cx="64" cy="104" r="40" fill="#FFFFFF" {W(2.4)}/>
<circle cx="64" cy="104" r="32" fill="none" stroke="#F5B8D0" stroke-width="2" stroke-dasharray="3 4"/>
<rect x="26" y="40" width="76" height="12" rx="3" fill="#FFFFFF" {s()}/>
<path d="M30 44 L36 48 L42 44 L48 48 L54 44 L60 48 L66 44 L72 48 L78 44 L84 48 L90 44 L96 48" fill="none" stroke="#C07A4A" stroke-width="2"/>
<rect x="26" y="52" width="76" height="9" fill="#E8B060" {W(2.6)}/>
<rect x="26" y="61" width="76" height="10" fill="#FFF3C8" {W(2.6)}/>
<rect x="26" y="71" width="76" height="9" fill="#E8B060" {W(2.6)}/>
<rect x="26" y="80" width="76" height="10" fill="#FFF3C8" {W(2.6)}/>
<rect x="26" y="90" width="76" height="8" rx="2" fill="#D9963E" {W(2.6)}/>
{face(64, 70, d=12, k=0.8)}
<path d="M28 96 Q20 104 24 110 M100 96 Q108 104 104 110" fill="none" {W(3)}/>
<path d="M18 112 Q24 106 30 112 M98 112 Q104 106 110 112" fill="none" {W(3)}/>
'''), "герой: пирожное мильфей слоями с глазурью-ёлочкой | сцена: делает реверанс на кружевной бумажной салфетке")

# 4 Мильфей (Революционный) — печенье макарон читает раскрытую книгу рецептов
I["cafe-milfey-revolyutsionny"] = (svg2("#F3EEFF", "#9C86E8", f'''
<path d="M18 100 L64 92 L110 100 L110 116 L64 108 L18 116Z" fill="#FFFFFF" {s()}/>
<path d="M64 92 V108" {W(2.4)}/>
<path d="M26 102 L56 97 M26 108 L56 103 M72 97 L102 102 M72 103 L102 108" stroke="#C9C0E8" stroke-width="2"/>
<ellipse cx="64" cy="48" rx="38" ry="14" fill="#B6E39A" {s()}/>
<rect x="28" y="54" width="72" height="10" rx="4" fill="#FFF8EE" {s()}/>
<ellipse cx="64" cy="72" rx="38" ry="14" fill="#B6E39A" {s()}/>
<path d="M30 52 Q32 48 36 50 M92 50 Q96 48 98 52 M30 68 Q32 64 36 66" fill="none" stroke="#86C36A" stroke-width="1.8"/>
{face(64, 70, d=11, k=0.8)}
<path d="M30 84 Q28 92 36 96 M98 84 Q100 92 92 96" fill="none" {W(3)}/>
<circle cx="102" cy="34" r="3" fill="#fff"/>{sparkle(108, 22, 6)}
'''), "герой: фисташковое печенье макарон с кремом | сцена: увлечённо читает раскрытую книгу рецептов")

# 5 У Камина — чугунок с картошкой томится в камине, над ним дымок
I["cafe-u-kamina-podolsk"] = (svg2("#FFD9B0", "#8A4B2A", f'''
<rect x="8" y="22" width="112" height="16" fill="#C9C2B8" {s()}/>
<rect x="14" y="38" width="100" height="80" fill="#B05A3A" {s()}/>
<path d="M14 54 H114 M14 70 H30 M98 70 H114 M14 86 H30 M98 86 H114 M14 102 H30 M98 102 H114 M40 38 V54 M74 38 V54" stroke="#8A3F28" stroke-width="2"/>
<path d="M30 118 V70 Q30 58 64 58 Q98 58 98 70 V118Z" fill="#2E2236" {s()}/>
<path d="M40 118 Q38 102 50 96 Q48 106 56 108 Q56 96 66 90 Q68 102 76 104 Q80 96 86 100 Q90 108 88 118Z" fill="#FF9A3C"/>
<path d="M50 118 Q52 108 60 104 Q60 112 66 112 Q70 106 76 110 Q80 114 78 118Z" fill="#FFE07A"/>
<path d="M38 92 Q38 76 64 76 Q90 76 90 92 Q90 108 64 108 Q38 108 38 92Z" fill="#3A3A48" {s()}/>
<ellipse cx="64" cy="78" rx="26" ry="6" fill="#4A4A5A" {W(2.4)}/>
<circle cx="54" cy="76" r="5" fill="#F2C46A" {W(1.8)}/><circle cx="66" cy="74" r="5" fill="#F2C46A" {W(1.8)}/><circle cx="76" cy="77" r="4" fill="#F2C46A" {W(1.8)}/>
<path d="M58 72 L62 68 M72 71 L74 66" stroke="#6CBF4A" stroke-width="2.4" stroke-linecap="round"/>
<g fill="#fff">{eye(56, 92, 0.75)}{eye(72, 92, 0.75)}</g>
<path d="M60 98 Q64 101 68 98" fill="none" {W(2.2)}/>
<path d="M56 64 Q52 56 58 50 M70 62 Q74 54 68 46" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" opacity=".7"/>
'''), "герой: чугунок с картошкой и укропом | сцена: томится в камине на живом огне, над ним вьётся дымок")

# 6 Батон — нарезной батон-дирижёр с палочкой, вокруг ноты
I["cafe-baton-podolsk"] = (svg2("#FFFBE0", "#E3B23C", f'''
<path d="M14 98 Q14 52 64 50 Q114 52 114 98 Q114 108 64 108 Q14 108 14 98Z" fill="#E7A24A" {s()}/>
<path d="M30 70 L40 60 M48 64 L58 54 M66 62 L76 52 M84 64 L94 56 M100 72 L108 64" stroke="#FFE3A8" stroke-width="5" stroke-linecap="round"/>
<path d="M30 70 L40 60 M48 64 L58 54 M66 62 L76 52 M84 64 L94 56 M100 72 L108 64" {W(2)}/>
{face(64, 84, d=12, k=0.9)}
<path d="M104 82 Q114 74 112 60" fill="none" {W(3.4)}/>
<path d="M112 60 L96 24" stroke="#FFFFFF" stroke-width="3.6" stroke-linecap="round"/><path d="M112 60 L96 24" fill="none" {W(1.4)}/>
<circle cx="112" cy="60" r="3.2" fill="#C9302C" {W(1.6)}/>
<path d="M24 36 V20 L36 16 V32" fill="none" {W(2.6)}/><ellipse cx="21" cy="37" rx="4" ry="3" fill="{O}"/><ellipse cx="33" cy="33" rx="4" ry="3" fill="{O}"/>
<path d="M60 32 V18" fill="none" {W(2.6)}/><ellipse cx="57" cy="33" rx="4" ry="3" fill="{O}"/><path d="M60 18 Q68 22 66 28" fill="none" {W(2.4)}/>
'''), "герой: нарезной батон с косыми надрезами | сцена: дирижирует палочкой, а вокруг кружатся ноты")

# 7 Отдых — сырник с изюминками плавает на надувном круге в озере сметаны
I["cafe-otdykh-podolsk"] = (svg2("#E9FAFF", "#5AB4E6", f'''
<path d="M0 74 Q32 66 64 74 Q96 82 128 74 V130 H0Z" fill="#FFFDF4" {s()}/>
<path d="M14 92 Q24 88 34 92 M90 100 Q100 96 110 100" fill="none" stroke="#E8DEC8" stroke-width="2.4"/>
<g transform="translate(-18 -20) scale(1.28)"><ellipse cx="64" cy="86" rx="40" ry="14" fill="#FF6F6F" {s()}/>
<ellipse cx="64" cy="84" rx="22" ry="6" fill="#FFFDF4" {W(2.4)}/>
<path d="M30 82 L36 92 M58 72 L56 82 M92 80 L86 92" stroke="#FFFFFF" stroke-width="6" stroke-linecap="butt"/>
<ellipse cx="64" cy="66" rx="26" ry="18" fill="#F2B56A" {s()}/>
<ellipse cx="64" cy="58" rx="22" ry="8" fill="#F7CC8A"/>
<ellipse cx="48" cy="70" rx="2.4" ry="1.6" fill="#6A3A2A"/><ellipse cx="80" cy="64" rx="2.4" ry="1.6" fill="#6A3A2A"/><ellipse cx="72" cy="76" rx="2.4" ry="1.6" fill="#6A3A2A"/>
<path d="M52 62 Q56 58 60 62 M68 62 Q72 58 76 62" fill="none" {W(2.4)}/>
<path d="M58 70 Q64 75 70 70" fill="none" {W(2.4)}/>
</g><circle cx="102" cy="24" r="11" fill="#FFE066" {W(2.4)}/>
'''), "герой: сырник с изюминками | сцена: отдыхает на надувном круге посреди озера сметаны, зажмурившись от солнца")

# 8 Хмели-Сунели — тарелка харчо, сверху из холщового мешочка сыплются пряности
I["cafe-khmeli-suneli-podolsk"] = (svg2("#FFE3D0", "#D9532F", f'''
<g transform="rotate(-28 86 30)"><path d="M70 12 Q86 8 102 12 L106 46 Q86 54 66 46Z" fill="#E8D7B0" {s()}/>
<path d="M70 18 Q86 22 102 18" fill="none" stroke="#B7A27A" stroke-width="2.4"/><path d="M80 30 L84 36 L90 28" fill="none" stroke="#7DB548" stroke-width="2.4"/></g>
<circle cx="58" cy="44" r="2" fill="#E8A030"/><circle cx="66" cy="50" r="2" fill="#9A4A2A"/><circle cx="52" cy="54" r="2" fill="#6A9A3A"/><circle cx="62" cy="58" r="1.8" fill="#E8A030"/><circle cx="72" cy="42" r="1.8" fill="#6A9A3A"/>
<ellipse cx="64" cy="94" rx="52" ry="18" fill="#FFFFFF" {s()}/>
<path d="M22 86 Q22 112 64 112 Q106 112 106 86Z" fill="#FFFFFF" {s()}/>
<ellipse cx="64" cy="86" rx="40" ry="10" fill="#C9502E" {W(2.6)}/>
<circle cx="46" cy="84" r="3" fill="#FFF6E6"/><circle cx="54" cy="88" r="2.4" fill="#FFF6E6"/><circle cx="80" cy="82" r="3" fill="#FFF6E6"/><circle cx="74" cy="88" r="2.4" fill="#FFF6E6"/>
<path d="M60 82 L64 78 L66 84" fill="none" stroke="#6CBF4A" stroke-width="2.2"/>
{face(64, 100, d=12, k=0.75)}
<circle cx="90" cy="66" r="4" fill="#fff" opacity=".85"/><circle cx="98" cy="60" r="3" fill="#fff" opacity=".85"/><circle cx="104" cy="66" r="2.4" fill="#fff" opacity=".85"/>
'''), "герой: тарелка грузинского супа харчо с рисом | сцена: на неё из холщового мешочка сыплются пряности, и суп чихает")

# 9 Ньокки — тортеллини-колечко плывёт по бульону, как надувной круг, в серединке горошинка
I["cafe-nyokki-podolsk"] = (svg2("#F4F8DC", "#A3B84A", f'''
<ellipse cx="64" cy="82" rx="58" ry="30" fill="#FFFFFF" {s()}/>
<ellipse cx="64" cy="80" rx="46" ry="20" fill="#F6D980" {W(2.4)}/>
<circle cx="30" cy="76" r="3" fill="#FFF1B8"/><circle cx="96" cy="86" r="3" fill="#FFF1B8"/><circle cx="88" cy="70" r="2" fill="#FFF1B8"/>
<path d="M28 88 Q34 84 40 88 M88 94 Q94 90 100 94" fill="none" stroke="#E8BE5A" stroke-width="2"/>
<path d="M34 74 Q34 52 64 52 Q94 52 94 74 Q94 88 64 88 Q34 88 34 74Z M54 72 Q54 66 64 66 Q74 66 74 72 Q74 78 64 78 Q54 78 54 72Z" fill="#FBE3A6" fill-rule="evenodd" {s()}/>
<path d="M38 64 Q44 58 50 62 M78 62 Q84 58 90 64" fill="none" stroke="#E8BE5A" stroke-width="2"/>
<circle cx="64" cy="70" r="5.5" fill="#7CC84A" {W(2)}/>
{face(64, 58, d=14, k=0.7, mouth=False)}
<path d="M44 82 Q64 90 84 82" fill="none" {W(2.4)}/>
<rect x="104" y="14" width="6" height="40" rx="3" fill="#C9C2B8" {W(2)}/>
'''), "герой: тортеллини-колечко | сцена: плывёт по тарелке бульона, как надувной круг, а в серединке катается горошинка")

# 10 Планета Суши (Королёв) — ролл-Сатурн с кольцом из ленточки имбиря в звёздном небе
I["cafe-planeta-sushi-korolev"] = (svg2("#4B3B9A", "#120E33", f'''
<circle cx="18" cy="28" r="1.6" fill="#fff"/><circle cx="104" cy="18" r="1.8" fill="#fff"/><circle cx="112" cy="96" r="1.6" fill="#fff"/><circle cx="20" cy="104" r="1.6" fill="#fff"/><circle cx="40" cy="14" r="1.2" fill="#fff"/>
{sparkle(98, 40, 5, "#FFE68A")}{sparkle(26, 70, 4, "#FFE68A")}
<path d="M14 74 Q64 102 114 74" fill="none" stroke="#FFB0B8" stroke-width="10" stroke-linecap="round"/>
<path d="M14 74 Q64 102 114 74" fill="none" {W(2.4)}/>
<circle cx="64" cy="64" r="32" fill="#2A3A2A" {s()}/>
<circle cx="64" cy="64" r="25" fill="#FFFFFF" {W(2.4)}/>
<circle cx="64" cy="64" r="13" fill="#FF8A5C" {W(2.2)}/><circle cx="58" cy="60" r="4" fill="#FFF6E8"/>
{face(64, 66, d=9, k=0.6)}
<path d="M24 64 Q64 48 104 64" fill="none" stroke="#FFB0B8" stroke-width="10" stroke-linecap="round" opacity="0"/>
<path d="M32 80 Q64 90 96 80" fill="none" stroke="#FFC8CE" stroke-width="8" stroke-linecap="round"/>
<path d="M32 80 Q64 90 96 80" fill="none" {W(2)}/>
'''), "герой: кружок ролла «Филадельфия» — планета с кольцом из ленточки маринованного имбиря | сцена: висит в звёздном космосе, как Сатурн")

# 11 Два зерна — два кофейных зёрнышка-близнеца сидят на краю бумажного стаканчика
I["cafe-dva-zerna-korolev"] = (svg2("#FFEFD8", "#B9763E", f'''
<path d="M30 56 H98 L90 120 H38Z" fill="#FFFFFF" {s()}/>
<rect x="26" y="48" width="76" height="10" rx="3" fill="#7A4A2E" {s()}/>
<path d="M34 80 H94 L91 100 H37Z" fill="#E7B98A" {W(2.4)}/>
<path d="M58 84 Q64 92 70 84 Q64 98 58 84Z" fill="#7A4A2E"/>
<g transform="rotate(-12 46 34)"><ellipse cx="46" cy="34" rx="15" ry="19" fill="#6A3A22" {s()}/>
<path d="M46 16 Q40 34 46 52" fill="none" stroke="#3A1E10" stroke-width="2.6"/></g>
<g transform="rotate(12 82 34)"><ellipse cx="82" cy="34" rx="15" ry="19" fill="#8A4E2C" {s()}/>
<path d="M82 16 Q88 34 82 52" fill="none" stroke="#3A1E10" stroke-width="2.6"/></g>
<g fill="#fff">{eye(40, 32, 0.6)}{eye(50, 32, 0.6)}{eye(78, 32, 0.6)}{eye(88, 32, 0.6)}</g>
<path d="M42 40 Q45 43 48 40 M80 40 Q83 43 86 40" fill="none" stroke="#FFE3C8" stroke-width="2" stroke-linecap="round"/>
<path d="M58 40 Q64 36 70 40" fill="none" stroke="#FFE3C8" stroke-width="2.4" stroke-linecap="round"/>
'''), "герой: два кофейных зёрнышка-близнеца | сцена: сидят на краю бумажного стаканчика и держатся за руки")

# 12 Совёнок — блинчик-совёнок с глазками из бананов и черники сидит на ветке ночью
I["cafe-sovenok-korolev"] = (svg2("#5FA9A8", "#163C4A", f'''
<circle cx="102" cy="26" r="12" fill="#FFF3B0" {W(2)}/><circle cx="106" cy="22" r="10" fill="#2A5560"/>
<circle cx="24" cy="30" r="1.6" fill="#fff"/><circle cx="40" cy="16" r="1.2" fill="#fff"/><circle cx="84" cy="14" r="1.4" fill="#fff"/>
<path d="M0 100 Q40 92 128 104" fill="none" stroke="#6A4128" stroke-width="10" stroke-linecap="round"/>
<path d="M0 100 Q40 92 128 104" fill="none" {W(2.4)}/>
<path d="M100 104 Q108 92 118 92" fill="none" stroke="#6A4128" stroke-width="6" stroke-linecap="round"/><ellipse cx="118" cy="88" rx="6" ry="4" fill="#6CBF4A" {W(1.8)}/>
<circle cx="64" cy="66" r="34" fill="#F0B562" {s()}/>
<path d="M36 46 L40 28 L52 38Z M92 46 L88 28 L76 38Z" fill="#F0B562" {s()}/>
<circle cx="50" cy="60" r="11" fill="#FFF6D8" {W(2.4)}/><circle cx="78" cy="60" r="11" fill="#FFF6D8" {W(2.4)}/>
<circle cx="50" cy="61" r="6" fill="#3A3A7A" {W(1.6)}/><circle cx="78" cy="61" r="6" fill="#3A3A7A" {W(1.6)}/>
<circle cx="48" cy="59" r="2" fill="#fff"/><circle cx="76" cy="59" r="2" fill="#fff"/>
<path d="M60 72 L64 80 L68 72Z" fill="#E86A3A" {W(2)}/>
<path d="M44 84 Q52 90 58 84 M70 84 Q76 90 84 84" fill="none" stroke="#D9963E" stroke-width="2.4"/>
<path d="M54 98 L54 104 M74 98 L74 104" {W(3)}/>
'''), "герой: блинчик-совёнок с глазами из банана и черники | сцена: сидит на ветке под ночной луной")

# 13 Якитория (ТЦ «Корабль») — стручок эдамаме плывёт по волнам, как лодочка, с тремя горошинами-матросами
I["cafe-yakitoriya-korolev"] = (svg2("#DDF7FF", "#2F8FC2", f'''
<path d="M0 84 Q16 76 32 84 Q48 92 64 84 Q80 76 96 84 Q112 92 128 84 V130 H0Z" fill="#3E7FD0" {s()}/>
<path d="M10 100 Q20 96 30 100 M80 106 Q90 102 100 106" fill="none" stroke="#9ED0FF" stroke-width="2.4"/>
<path d="M14 66 Q24 92 64 92 Q104 92 114 66 Q100 76 64 76 Q28 76 14 66Z" fill="#7CC84A" {s()}/>
<circle cx="40" cy="70" r="11" fill="#A6E06A" {W(2.4)}/><circle cx="64" cy="68" r="12" fill="#A6E06A" {W(2.4)}/><circle cx="88" cy="70" r="11" fill="#A6E06A" {W(2.4)}/>
{face(40, 68, d=4, k=0.45)}{face(64, 66, d=4.5, k=0.5)}{face(88, 68, d=4, k=0.45)}
<path d="M64 56 V20" {W(3)}/><path d="M64 22 L92 34 L64 46Z" fill="#FFFFFF" {W(2.4)}/><circle cx="76" cy="34" r="4" fill="#E8453C"/>
'''), "герой: стручок эдамаме с тремя бобами-матросами | сцена: плывёт по волнам, как кораблик под парусом с красным кругом")

# 14 Новые Горки — котлета по-киевски с косточкой катается на санках с заснеженной горки
I["cafe-novye-gorki-korolev"] = (svg2("#F2FAFF", "#9BBCE0", f'''
<path d="M0 54 Q50 58 128 116 V130 H0Z" fill="#FFFFFF" {s()}/>
<circle cx="18" cy="20" r="2" fill="#fff"/><circle cx="58" cy="24" r="2.4" fill="#fff"/><circle cx="96" cy="16" r="2" fill="#fff"/><circle cx="110" cy="44" r="2.2" fill="#fff"/><circle cx="34" cy="38" r="1.8" fill="#fff"/>
<g transform="translate(-6 -8) scale(1.12) rotate(16 64 80)">
<rect x="30" y="86" width="64" height="6" rx="3" fill="#C9302C" {W(2.4)}/>
<path d="M30 92 Q22 92 24 84 M94 92 L36 100 Q26 102 22 96" fill="none" {W(2.6)}/>
<ellipse cx="62" cy="70" rx="28" ry="16" fill="#E39A3A" {s()}/>
<path d="M88 64 L108 56" stroke="#FFFFFF" stroke-width="7" stroke-linecap="round"/><path d="M88 64 L108 56" fill="none" {W(1.6)}/>
<circle cx="110" cy="55" r="5" fill="#FFFFFF" {W(2)}/>
<circle cx="48" cy="64" r="1.6" fill="#B86E22"/><circle cx="72" cy="78" r="1.6" fill="#B86E22"/><circle cx="56" cy="78" r="1.6" fill="#B86E22"/>
{face(62, 68, d=9, k=0.75)}</g>
'''), "герой: котлета по-киевски с белой косточкой | сцена: мчится на красных санках с заснеженной горки")

# 15 Глобус — круглый каравай-глобус с материками из корочки крутится на подставке
I["cafe-globus-korolev"] = (svg2("#E8F7FF", "#5FA6D9", f'''
<path d="M40 118 H88 L82 108 H46Z" fill="#B07A4A" {s()}/>
<path d="M64 108 V96" {W(4)}/>
<path d="M26 64 A40 40 0 0 1 102 40" fill="none" stroke="#C9A04A" stroke-width="5" stroke-linecap="round"/>
<path d="M26 64 A40 40 0 0 1 102 40" fill="none" {W(1.4)}/>
<circle cx="64" cy="62" r="34" fill="#F3C47A" {s()}/>
<path d="M40 44 Q48 38 56 44 Q60 52 52 56 Q44 60 40 54Z M72 36 Q86 38 90 50 Q84 56 76 52 Q70 46 72 36Z M66 78 Q80 74 86 82 Q82 92 70 92 Q62 88 66 78Z M36 70 Q44 68 46 76 Q42 82 36 78Z" fill="#C97F3A" {W(2)}/>
<path d="M32 56 Q64 66 96 56" fill="none" stroke="#FFE8B8" stroke-width="2" stroke-dasharray="3 4"/>
{face(64, 66, d=11, k=0.8)}
<path d="M104 70 Q112 62 108 52" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/><path d="M106 50 L108 52 L112 49" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
'''), "герой: круглый каравай-глобус с материками из румяной корочки | сцена: крутится на деревянной подставке, как школьный глобус")

# 16 Шоколадница (Королёв) — шоколадный фондан удивлённо смотрит, как из него вытекает шоколадная речка
I["cafe-shokoladnitsa-korolev"] = (svg2("#FFE6EE", "#C2607E", f'''
<ellipse cx="64" cy="104" rx="56" ry="16" fill="#FFFFFF" {s()}/>
<path d="M60 96 Q70 110 98 108 Q116 106 112 98 Q100 100 86 96Z" fill="#5A2A18" {W(2.4)}/>
<path d="M34 56 Q34 44 64 44 Q94 44 94 56 L92 92 Q92 100 64 100 Q36 100 36 92Z" fill="#6E3820" {s()}/>
<ellipse cx="64" cy="48" rx="28" ry="7" fill="#8A4A2A" {W(2.4)}/>
<path d="M50 44 Q46 36 54 34 Q60 30 64 38 Q70 30 76 36 Q82 40 76 46" fill="#FFFFFF" {W(2)}/>
<circle cx="64" cy="30" r="4.5" fill="#E8304A" {W(1.8)}/>
<path d="M70 78 Q78 90 74 98 Q70 104 62 98" fill="#4A1E10" {W(2.2)}/>
<circle cx="54" cy="66" r="4.4" fill="#fff"/><circle cx="54" cy="66" r="2.6" fill="{O}"/><circle cx="74" cy="66" r="4.4" fill="#fff"/><circle cx="74" cy="66" r="2.6" fill="{O}"/>
<ellipse cx="64" cy="80" rx="4" ry="5" fill="{O}"/>
<path d="M48 58 L58 60 M80 58 L70 60" {W(2)}/>
'''), "герой: шоколадный фондан с ягодкой на макушке | сцена: удивлённо смотрит, как из его бока вытекает шоколадная речка")

# 17 Лис и барашек — барашек из безе пасётся на лужайке из мятного крема
I["cafe-lis-i-barashek-korolev"] = (svg2("#F3FFF0", "#7DCB8E", f'''
<path d="M0 92 Q20 84 40 92 Q60 84 80 92 Q100 84 128 92 V130 H0Z" fill="#B8F0C8" {s()}/>
<path d="M18 100 L22 92 M30 104 L34 96 M98 102 L102 94 M110 106 L114 98" stroke="#5FB878" stroke-width="2.4" stroke-linecap="round"/>
<path d="M46 92 V106 M58 94 V108 M78 94 V108 M88 92 V106" stroke="{O}" stroke-width="5" stroke-linecap="round"/>
<path d="M30 70 Q24 56 36 50 Q36 38 50 40 Q56 30 68 36 Q80 30 86 40 Q100 40 98 54 Q108 62 100 74 Q104 88 88 90 Q80 100 64 94 Q50 100 42 90 Q26 88 30 70Z" fill="#FFFFFF" {s()}/>
<path d="M44 52 Q50 46 56 52 M70 48 Q76 42 82 48 M58 80 Q64 74 70 80" fill="none" stroke="#E6E2EC" stroke-width="2.4"/>
<ellipse cx="100" cy="62" rx="15" ry="13" fill="#F2D6B8" {s()}/>
<path d="M90 52 Q84 46 88 42 M110 52 Q116 46 112 42" fill="none" {W(2.6)}/>
{face(100, 62, d=5, k=0.55)}
<circle cx="100" cy="46" r="5" fill="#FFFFFF" {W(2)}/>
'''), "герой: барашек из воздушного безе | сцена: пасётся на лужайке из мятного крема")

# 18 Роял (Королёв) — шоколадный торт-рояль сам играет мелодию
I["cafe-royal-korolev"] = (svg2("#EEE4FF", "#7A5BC8", f'''
<path d="M22 70 Q22 44 54 42 L96 42 Q110 42 110 56 L110 70Z" fill="#4A2A1E" {s()}/>
<path d="M28 66 Q30 50 54 48 L94 48" fill="none" stroke="#7A4A32" stroke-width="2.4"/>
<rect x="18" y="70" width="96" height="16" fill="#FFFFFF" {s()}/>
<path d="M30 70 V86 M42 70 V86 M54 70 V86 M66 70 V86 M78 70 V86 M90 70 V86 M102 70 V86" stroke="{O}" stroke-width="1.8"/>
<rect x="27" y="70" width="6" height="9" fill="#3A2216"/><rect x="39" y="70" width="6" height="9" fill="#3A2216"/><rect x="63" y="70" width="6" height="9" fill="#3A2216"/><rect x="75" y="70" width="6" height="9" fill="#3A2216"/><rect x="87" y="70" width="6" height="9" fill="#3A2216"/>
<rect x="22" y="86" width="88" height="8" fill="#4A2A1E" {W(2.6)}/>
<path d="M32 94 V116 M100 94 V116" stroke="{O}" stroke-width="5" stroke-linecap="round"/>
{face(66, 58, d=11, k=0.8)}
<circle cx="88" cy="40" r="5" fill="#E8304A" {W(1.8)}/>
<path d="M30 30 V14 L42 10 V26" fill="none" stroke="#FFFFFF" stroke-width="2.6"/><ellipse cx="27" cy="31" rx="4" ry="3" fill="#FFFFFF"/><ellipse cx="39" cy="27" rx="4" ry="3" fill="#FFFFFF"/>
<path d="M104 30 V16 Q110 18 110 24" fill="none" stroke="#FFFFFF" stroke-width="2.6"/><ellipse cx="101" cy="31" rx="4" ry="3" fill="#FFFFFF"/>
'''), "герой: шоколадный торт в форме рояля с клавишами из белого шоколада | сцена: сам играет мелодию, и над крышкой взлетают ноты")

# 19 Сэр Кролик — морковный торт-джентльмен в цилиндре с моноклем раскланивается
I["cafe-sir-krolik-korolev"] = (svg2("#FFF1DE", "#F08A3C", f'''
<path d="M28 110 L36 62 L92 62 L100 110Z" fill="#F0A85A" {s()}/>
<path d="M32 86 H96 M30 98 H98" stroke="#FFF6E6" stroke-width="5"/>
<path d="M32 86 H96 M30 98 H98" stroke="#E0C9A8" stroke-width="1.4"/>
<path d="M34 64 Q64 54 94 64 Q98 70 92 72 Q64 66 36 72 Q30 70 34 64Z" fill="#FFF6E6" {W(2.4)}/>
<g transform="rotate(-18 66 40)"><rect x="50" y="18" width="30" height="34" rx="3" fill="#2E2A3C" {s()}/>
<rect x="40" y="48" width="50" height="7" rx="3" fill="#2E2A3C" {s()}/><rect x="50" y="40" width="30" height="5" fill="#E85A4A"/></g>
<path d="M98 72 Q110 58 104 44" fill="none" {W(3.4)}/>
<circle cx="52" cy="80" r="3.4" fill="{O}"/><circle cx="51" cy="78.6" r="1.2" fill="#fff"/>
<circle cx="76" cy="80" r="7" fill="none" {W(2.2)}/><circle cx="76" cy="80" r="3.4" fill="{O}"/><circle cx="75" cy="78.6" r="1.2" fill="#fff"/>
<path d="M82 86 Q86 96 84 104" fill="none" stroke="#C9A04A" stroke-width="1.6"/>
<path d="M58 90 Q64 94 70 90" fill="none" {W(2.4)}/>
<ellipse cx="44" cy="88" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/>
<path d="M60 58 L56 50 M68 58 L70 50" stroke="#6CBF4A" stroke-width="3" stroke-linecap="round"/>
'''), "герой: кусок морковного торта-джентльмена с моноклем | сцена: вежливо раскланивается, приподнимая цилиндр")

# 20 Роял (Боровское ш.) — пирог «Наполеон» в треуголке командует, указывая ложкой-шпагой вперёд
I["cafe-royal-borovskoe"] = (svg2("#E0ECFF", "#3E5FB8", f'''
<rect x="0" y="104" width="128" height="26" fill="#C9D8F0" {W(2.4)}/>
<rect x="30" y="58" width="58" height="46" fill="#FFF3D6" {s()}/>
<path d="M30 70 H88 M30 82 H88 M30 94 H88" stroke="#E8B060" stroke-width="4"/>
<path d="M30 70 H88 M30 82 H88 M30 94 H88" stroke="{O}" stroke-width="1.2"/>
<path d="M30 58 H88" stroke="#F3DDB0" stroke-width="6"/><circle cx="40" cy="57" r="1.8" fill="#C9A04A"/><circle cx="58" cy="56" r="1.8" fill="#C9A04A"/><circle cx="76" cy="57" r="1.8" fill="#C9A04A"/>
<path d="M22 54 Q58 22 96 54 Q58 46 22 54Z" fill="#2E2A3C" {s()}/>
<circle cx="58" cy="42" r="4.4" fill="#E8453C" {W(1.6)}/><circle cx="58" cy="42" r="1.8" fill="#fff"/>
{face(58, 76, d=9, k=0.7)}
<path d="M88 76 Q98 70 104 62" fill="none" {W(3.4)}/>
<path d="M102 64 L120 34" stroke="#C9CDD8" stroke-width="4" stroke-linecap="round"/><path d="M102 64 L120 34" fill="none" {W(1.2)}/>
<ellipse cx="121" cy="31" rx="5" ry="7" fill="#C9CDD8" transform="rotate(30 121 31)" {W(2)}/>
'''), "герой: пирог «Наполеон» в треуголке | сцена: командует парадом, указывая вперёд десертной ложкой, как шпагой")

# 21 Тануки (Коштоянца) — енотовидная собака тануки в фартуке несёт поднос с роллами
I["cafe-tanuki-koshtoyantsa"] = (svg2("#FFF0DA", "#E9A04A", f'''
<path d="M40 128 Q36 92 64 90 Q92 92 88 128Z" fill="#9A7458" {s()}/>
<path d="M50 100 H78 L76 126 H52Z" fill="#FFFFFF" {W(2.4)}/><circle cx="64" cy="112" r="4" fill="#E8453C"/>
<path d="M36 40 L30 22 L50 32Z M92 40 L98 22 L78 32Z" fill="#7A5A44" {s()}/>
<ellipse cx="64" cy="56" rx="32" ry="28" fill="#B8926E" {s()}/>
<path d="M36 56 Q44 44 56 54 Q60 64 50 68 Q40 68 36 56Z M92 56 Q84 44 72 54 Q68 64 78 68 Q88 68 92 56Z" fill="#4A3628"/>
<ellipse cx="64" cy="72" rx="12" ry="9" fill="#F3E2CC"/>
<circle cx="50" cy="58" r="4" fill="#fff"/><circle cx="50" cy="58" r="2.4" fill="{O}"/><circle cx="78" cy="58" r="4" fill="#fff"/><circle cx="78" cy="58" r="2.4" fill="{O}"/>
<ellipse cx="64" cy="68" rx="3.6" ry="2.6" fill="{O}"/><path d="M60 74 Q64 78 68 74" fill="none" {W(2)}/>
<rect x="84" y="90" width="38" height="6" rx="2" fill="#C9302C" {W(2.4)}/>
<circle cx="94" cy="84" r="6" fill="#2A3A2A" {W(2)}/><circle cx="94" cy="84" r="3" fill="#FF8A5C"/>
<circle cx="110" cy="84" r="6" fill="#2A3A2A" {W(2)}/><circle cx="110" cy="84" r="3" fill="#FFE07A"/>
<path d="M84 102 Q90 98 92 94" fill="none" {W(3.2)}/>
'''), "герой: енотовидная собачка тануки в белом фартуке | сцена: бережно несёт на красном подносе два ролла")

# 22 СоветЪ в Филях — тефтелька-ёжик с рисовыми иголками бежит по сугробу пюре
I["cafe-sovet-v-filyakh"] = (svg2("#FFE2DC", "#C8382E", f'''
<ellipse cx="64" cy="108" rx="58" ry="14" fill="#FFFFFF" {s()}/>
<path d="M10 104 Q24 84 40 96 Q54 82 70 96 Q86 84 100 98 Q112 90 120 104Z" fill="#FFF3B8" {s()}/>
<circle cx="40" cy="90" r="2.6" fill="#F7C948"/>
<g>
<path d="M38 66 L30 58 M42 56 L36 46 M52 50 L50 38 M62 46 L64 34 M72 48 L78 38 M82 54 L90 46 M88 64 L98 60 M86 74 L96 74" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round"/>
<path d="M38 66 L30 58 M42 56 L36 46 M52 50 L50 38 M62 46 L64 34 M72 48 L78 38 M82 54 L90 46 M88 64 L98 60 M86 74 L96 74" stroke="{O}" stroke-width="1.4" stroke-linecap="round"/>
<ellipse cx="62" cy="72" rx="28" ry="22" fill="#A0603A" {s()}/>
<ellipse cx="36" cy="78" rx="10" ry="8" fill="#C8845A" {W(2.4)}/><circle cx="27" cy="78" r="3" fill="{O}"/>
<g fill="#fff">{eye(42, 72, 0.6)}</g>
<path d="M38 84 Q42 86 46 84" fill="none" {W(2)}/>
<path d="M52 94 L48 102 M74 94 L80 100" {W(3.4)}/>
</g>
<path d="M98 30 L110 30 M100 38 L114 38" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
'''), "герой: тефтелька-ёжик с рисовыми иголками | сцена: бежит по сугробу картофельного пюре в советской столовой")

# 23 Му-Му (Осенний бульвар) — пятнистая коровка-раздатчица в колпаке с половником, вокруг осенние листья
I["cafe-mumu-osenny"] = (svg2("#FFF4D6", "#E07A2A", f'''
<path d="M18 30 Q22 22 30 26 Q26 34 18 30Z" fill="#E8453C" {W(1.8)}/><path d="M100 18 Q108 12 112 20 Q104 26 100 18Z" fill="#F7B43A" {W(1.8)}/><path d="M108 96 Q116 92 118 100 Q110 104 108 96Z" fill="#C9502E" {W(1.8)}/>
<path d="M30 128 Q28 96 64 94 Q100 96 98 128Z" fill="#FFFFFF" {s()}/>
<path d="M40 104 Q48 100 50 110 Q44 116 40 104Z M80 110 Q88 104 90 114Z" fill="#2E2A3C"/>
<path d="M30 52 L16 44 Q14 56 30 60Z M98 52 L112 44 Q114 56 98 60Z" fill="#FFFFFF" {s()}/>
<ellipse cx="64" cy="62" rx="34" ry="30" fill="#FFFFFF" {s()}/>
<path d="M36 50 Q46 40 54 50 Q50 60 40 58Z M80 70 Q92 66 94 76 Q86 84 80 70Z" fill="#2E2A3C"/>
<ellipse cx="64" cy="80" rx="20" ry="12" fill="#FFC2D2" {s()}/>
<ellipse cx="57" cy="80" rx="2.6" ry="3.4" fill="{O}"/><ellipse cx="71" cy="80" rx="2.6" ry="3.4" fill="{O}"/>
{eye(52, 62, 0.75)}{eye(76, 62, 0.75)}
<path d="M40 34 Q36 18 52 20 Q56 10 66 16 Q78 10 82 22 Q94 22 88 34Z" fill="#FFFFFF" {s()}/>
<path d="M98 100 L116 66" stroke="#C9CDD8" stroke-width="4" stroke-linecap="round"/><path d="M110 64 Q112 54 122 58 Q126 66 116 70Z" fill="#C9CDD8" {W(2.2)}/>
'''), "герой: пятнистая коровка-раздатчица в поварском колпаке | сцена: стоит на раздаче с половником, вокруг кружат осенние листья")

# 24 Supremo — шарик пломбира ныряет в чашку эспрессо (аффогато)
I["cafe-supremo-vernadskogo"] = (svg2("#F6EFE6", "#8C6A54", f'''
<circle cx="96" cy="44" r="3" fill="#fff"/><circle cx="104" cy="56" r="2.4" fill="#fff"/><circle cx="26" cy="50" r="2.6" fill="#fff"/>
<ellipse cx="62" cy="112" rx="40" ry="8" fill="#FFFFFF" {s()}/>
<path d="M30 76 H94 L88 104 Q86 110 78 110 H46 Q38 110 36 104Z" fill="#FFFFFF" {s()}/>
<path d="M94 82 Q108 82 106 92 Q104 100 90 98" fill="none" {W(3.2)}/>
<ellipse cx="62" cy="76" rx="32" ry="7" fill="#4A2A18" {W(2.6)}/>
<path d="M42 72 L38 64 M82 72 L88 64 M50 70 L50 62" stroke="#4A2A18" stroke-width="3" stroke-linecap="round"/>
<g transform="rotate(-20 62 52)">
<circle cx="62" cy="52" r="18" fill="#FFF8E6" {s()}/>
<path d="M46 60 Q50 66 56 62 Q62 68 68 62 Q74 66 78 60" fill="#FFF8E6" {W(2.2)}/>
{face(62, 50, d=7, k=0.6)}
<path d="M44 44 Q38 36 42 30 M80 44 Q86 36 82 30" fill="none" {W(2.6)}/></g>
'''), "герой: шарик сливочного пломбира | сцена: ныряет «солдатиком» в чашку горячего эспрессо, поднимая брызги (аффогато)")

# 25 Le Meilleur — печенье-мадлен в беретике на фоне Эйфелевой башни
I["cafe-le-meilleur-novozavodskaya"] = (svg2("#FFEAF2", "#E59AB8", f'''
<path d="M92 120 L100 40 L104 18 L108 40 L116 120 M96 84 H112 M98 62 H110" fill="none" stroke="#9A8AA8" stroke-width="3"/>
<path d="M92 120 Q104 100 116 120" fill="none" stroke="#9A8AA8" stroke-width="3"/>
<path d="M14 110 Q14 66 52 58 Q90 66 90 110Z" fill="#F2C060" {s()}/>
<path d="M22 108 Q26 80 52 68 M34 110 Q36 86 52 74 M52 110 V80 M70 110 Q68 86 52 74 M82 108 Q78 80 52 68" fill="none" stroke="#D9963E" stroke-width="2.2"/>
<path d="M30 60 Q34 44 52 44 Q72 44 74 58 Q52 52 30 60Z" fill="#2E2A3C" {s()}/><path d="M52 44 L54 38" {W(2.6)}/>
{face(52, 86, d=10, k=0.8)}
'''), "герой: печенье-мадлен в форме ракушки в чёрном беретике | сцена: позирует на фоне Эйфелевой башни")

# 26 Цинандали — квадрат ачмы раскрывает слои, как книжку, внутри тянется сыр
I["cafe-tsinandali-pokryshkina"] = (svg2("#F0F5DC", "#7F9A3E", f'''
<path d="M24 96 L64 104 L104 96 L104 106 L64 114 L24 106Z" fill="#E7B060" {s()}/>
<path d="M24 96 L64 104 L104 96 L104 62 L64 70 L24 62Z" fill="#F7DFA0" {s()}/>
<path d="M64 70 L28 40 Q22 36 24 44 L24 62Z" fill="#F2C878" {s()}/>
<path d="M64 70 L100 40 Q106 36 104 44 L104 62Z" fill="#F2C878" {s()}/>
<path d="M40 64 Q44 76 40 86 M56 70 Q60 82 54 92 M78 68 Q74 80 80 90 M90 64 Q86 74 92 84" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round"/>
<path d="M30 52 L56 66 M98 52 L72 66" stroke="#D9963E" stroke-width="2"/>
{face(64, 86, d=12, k=0.8)}
<path d="M14 24 Q20 16 26 22 M108 22 Q114 16 120 22" fill="none" stroke="#5E8A2A" stroke-width="2.4"/>
<circle cx="18" cy="32" r="4" fill="#8A3A6A" {W(1.6)}/><circle cx="24" cy="36" r="4" fill="#8A3A6A" {W(1.6)}/><circle cx="20" cy="40" r="4" fill="#8A3A6A" {W(1.6)}/>
'''), "герой: квадрат ачмы — слоёного сырного пирога | сцена: раскрывает слои, как книжку, а внутри тянется сыр")

# 27 Окно (Петровка) — пирожное «корзиночка» с кремовыми грибочками выглядывает из окна
I["cafe-okno-petrovka"] = (svg2("#FFEADF", "#E8876A", f'''
<rect x="10" y="10" width="108" height="118" fill="#F2D2B8"/>
<rect x="22" y="22" width="84" height="80" rx="4" fill="#9ED6FF" {s()}/>
<path d="M22 22 Q30 50 22 70 L22 22Z M106 22 Q98 50 106 70Z" fill="#F07A8A" {W(2.4)}/>
<rect x="14" y="100" width="100" height="10" rx="3" fill="#FFFFFF" {s()}/>
<path d="M34 100 L40 76 H88 L94 100Z" fill="#D99A4A" {s()}/>
<path d="M44 80 L46 98 M56 78 L56 98 M72 78 L72 98 M84 80 L82 98" stroke="#B87A32" stroke-width="2"/>
<ellipse cx="64" cy="74" rx="28" ry="9" fill="#FFF3E6" {W(2.4)}/>
<path d="M48 70 Q48 60 56 60 Q64 60 64 70Z" fill="#F6A6B8" {W(2)}/><rect x="54" y="68" width="4" height="6" fill="#FFF3E6"/>
<path d="M66 68 Q66 58 74 58 Q82 58 82 68Z" fill="#B48ADE" {W(2)}/><rect x="72" y="66" width="4" height="7" fill="#FFF3E6"/>
<path d="M36 90 Q30 84 34 78 M92 90 Q98 84 94 78" fill="none" {W(2.8)}/>
{face(64, 88, d=10, k=0.65)}
'''), "герой: пирожное «корзиночка» с кремовыми грибочками | сцена: выглядывает из окна, облокотившись на подоконник")

# 28 Smoothie & Coffee — боул с гранолой и ягодами на фоне небоскрёбов Москва-Сити
I["cafe-smoothie-coffee-mantulinskaya"] = (svg2("#E6F2FF", "#4A7FD0", f'''
<rect x="14" y="24" width="18" height="80" fill="#9FC6E8" {W(2.4)}/><path d="M42 104 V14 L58 6 V104Z" fill="#7AA8D8" {W(2.4)}/><rect x="70" y="30" width="16" height="74" fill="#B8D8F0" {W(2.4)}/><path d="M94 104 V20 Q104 12 112 20 V104Z" fill="#8AB4E0" {W(2.4)}/>
<path d="M18 40 H28 M18 56 H28 M46 30 H54 M46 48 H54 M74 46 H82 M98 36 H108 M98 54 H108" stroke="#E6F2FF" stroke-width="2"/>
<path d="M16 82 Q16 118 64 118 Q112 118 112 82Z" fill="#FFFFFF" {s()}/>
<ellipse cx="64" cy="82" rx="48" ry="12" fill="#E87FB0" {W(2.6)}/>
<path d="M24 82 Q40 74 54 80" fill="#E8B060" {W(2)}/><circle cx="32" cy="78" r="2" fill="#B87A32"/><circle cx="44" cy="78" r="2" fill="#B87A32"/>
<circle cx="72" cy="78" r="4.4" fill="#4A4AA8" {W(1.6)}/><circle cx="82" cy="82" r="4.4" fill="#4A4AA8" {W(1.6)}/><circle cx="94" cy="78" r="4.6" fill="#E8304A" {W(1.6)}/>
<path d="M60 76 Q66 70 70 76" fill="#FFF07A" {W(1.6)}/>
{face(64, 98, d=12, k=0.85)}
'''), "герой: розовый смузи-боул с гранолой и ягодами | сцена: стоит на фоне небоскрёбов Москва-Сити")

# 29 Villa Pasta (круглосуточно) — паста-ракушка конкилье спит под луной, но один глаз открыт
I["cafe-villa-pasta-pyatnitskaya"] = (svg2("#3A4C8A", "#141B3E", f'''
<circle cx="100" cy="28" r="14" fill="#FFF3B0" {W(2)}/><circle cx="106" cy="23" r="12" fill="#26315E"/>
<circle cx="22" cy="24" r="1.6" fill="#fff"/><circle cx="50" cy="14" r="1.4" fill="#fff"/><circle cx="76" cy="20" r="1.2" fill="#fff"/>{sparkle(30, 44, 4, "#FFE68A")}
<rect x="10" y="96" width="108" height="20" rx="6" fill="#B85A4A" {s()}/>
<path d="M18 74 Q14 104 64 104 Q114 104 110 74 Q108 54 90 50 Q76 44 64 52 Q52 44 38 50 Q20 54 18 74Z" fill="#F7D27A" {s()}/>
<path d="M30 60 Q36 80 34 98 M46 54 Q50 78 48 100 M64 54 V102 M82 54 Q78 78 80 100 M98 60 Q92 80 94 98" fill="none" stroke="#E0A84A" stroke-width="2.4"/>
<path d="M42 78 Q48 74 54 78" fill="none" {W(2.6)}/>
<circle cx="78" cy="77" r="5" fill="#fff" {W(1.6)}/><circle cx="79" cy="78" r="2.8" fill="{O}"/>
<path d="M58 90 Q64 94 70 90" fill="none" {W(2.4)}/>
'''), "герой: паста-ракушка конкилье | сцена: дремлет ночью под луной, но один глаз держит открытым — работает круглосуточно")

# 30 ЛандринЪ — жестяная баночка монпансье, крышка открыта, леденцы выпрыгивают
I["cafe-landrin-sushchevskaya"] = (svg2("#FFF7E0", "#D9A23A", f'''
<ellipse cx="64" cy="104" rx="42" ry="12" fill="#B8323A" {s()}/>
<path d="M22 80 V104 Q64 124 106 104 V80Z" fill="#C8404A" {s()}/>
<ellipse cx="64" cy="80" rx="42" ry="12" fill="#FFF3D6" {s()}/>
<path d="M28 96 Q64 110 100 96" fill="none" stroke="#F2C060" stroke-width="3"/>
<circle cx="44" cy="80" r="6" fill="#7CC84A" {W(2)}/><circle cx="60" cy="84" r="6" fill="#FFD045" {W(2)}/><circle cx="80" cy="80" r="6" fill="#5AB4E6" {W(2)}/><circle cx="72" cy="76" r="5" fill="#F07AA8" {W(2)}/>
<g transform="rotate(-24 88 40)"><ellipse cx="88" cy="40" rx="30" ry="9" fill="#C8404A" {s()}/><ellipse cx="88" cy="38" rx="20" ry="5" fill="none" stroke="#F2C060" stroke-width="2.4"/></g>
<circle cx="40" cy="42" r="9" fill="#F04A6A" {W(2.2)}/><path d="M36 38 Q38 36 40 38" stroke="#fff" stroke-width="2" fill="none"/>
<circle cx="58" cy="28" r="8" fill="#B07AE0" {W(2.2)}/><circle cx="26" cy="60" r="7" fill="#FFB23A" {W(2.2)}/>
{face(64, 98, d=12, k=0.75)}
'''), "герой: жестяная баночка монпансье с разноцветными леденцами | сцена: крышка отскочила, и леденцы выпрыгивают наружу")

# 31 Городское кафе «317» — яйцо пашот на тосте просыпается и потягивается под будильником
I["cafe-317-glubokiy"] = (svg2("#FFFCE4", "#F2C84A", f'''
<circle cx="98" cy="28" r="14" fill="#FFFFFF" {s()}/><path d="M98 20 V28 L104 32" fill="none" {W(2.4)}/>
<path d="M86 16 L82 12 M110 16 L114 12" {W(3)}/><path d="M84 40 L80 44 M112 40 L116 44" {W(2.4)}/>
<path d="M118 22 L124 20 M118 30 L126 30" stroke="#E8453C" stroke-width="2.2" stroke-linecap="round"/>
<path d="M18 112 L22 66 Q22 56 32 56 Q40 46 52 54 L86 54 Q96 54 96 66 L100 112Z" fill="#E8A85A" {s()}/>
<path d="M28 108 L30 68 Q30 62 36 62 L84 62 Q90 62 90 68 L92 108Z" fill="#FFE3B0"/>
<path d="M30 80 Q28 62 58 62 Q90 62 88 82 Q88 100 58 100 Q30 100 30 80Z" fill="#FFFFFF" {s()}/>
<circle cx="58" cy="80" r="12" fill="#FFC23A" {W(2.4)}/>
<path d="M51 78 Q54 75 57 78 M60 78 Q63 75 66 78" fill="none" {W(2)}/><path d="M56 84 Q58 86 60 84" fill="none" {W(1.8)}/>
<path d="M28 76 Q16 66 18 54 M88 76 Q100 66 98 54" fill="none" {W(3)}/>
'''), "герой: яйцо пашот на тосте | сцена: просыпается и сладко потягивается под звенящим будильником")

# 32 Steak it easy (Мясницкая) — стейк загорает под гриль-лампой в тёмных очках
I["cafe-steak-it-easy-myasnitskaya"] = (svg2("#FFE8D0", "#E0552E", f'''
<path d="M44 10 H84 L94 26 H34Z" fill="#5A5A6A" {s()}/><path d="M40 26 H88" stroke="#FFB23A" stroke-width="4"/>
<path d="M44 34 L38 44 M64 32 V44 M84 34 L90 44" stroke="#FFD045" stroke-width="3" stroke-linecap="round"/>
<rect x="8" y="98" width="112" height="10" rx="4" fill="#3A3A48" {s()}/>
<path d="M20 98 V108 M40 98 V108 M60 98 V108 M80 98 V108 M100 98 V108" stroke="#6A6A7A" stroke-width="2"/>
<path d="M18 82 Q16 56 52 54 Q76 50 96 58 Q114 66 108 84 Q100 100 64 98 Q24 100 18 82Z" fill="#A0402E" {s()}/>
<path d="M34 64 Q50 70 60 62 M70 84 Q84 78 94 86" fill="none" stroke="#F2D6C8" stroke-width="3" stroke-linecap="round"/>
<path d="M30 76 L50 60 M48 88 L76 64 M72 90 L96 70" stroke="#5A1E14" stroke-width="3"/>
<path d="M40 70 H58 Q60 80 50 80 Q40 80 40 70Z M66 70 H84 Q86 80 76 80 Q66 80 66 70Z" fill="#2E2A3C"/><path d="M58 72 H66" {W(2.4)}/>
<path d="M56 88 Q62 92 68 88" fill="none" stroke="#FFE3D6" stroke-width="2.4" stroke-linecap="round"/>
'''), "герой: стейк с полосками гриля в тёмных очках | сцена: загорает под горячей гриль-лампой, как на пляже")

# 33 Steak it easy (Москва-Сити) — луковые кольца в кляре сложены в башню-небоскрёб
I["cafe-steak-it-easy-presnenskaya"] = (svg2("#E8EEFF", "#6A7FC8", f'''
<rect x="8" y="50" width="16" height="70" fill="#B8C6EC" {W(2)}/><rect x="104" y="36" width="18" height="84" fill="#B8C6EC" {W(2)}/>
<rect x="26" y="108" width="76" height="10" rx="4" fill="#FFFFFF" {s()}/>
<ellipse cx="64" cy="98" rx="30" ry="10" fill="#E8A040" {s()}/><ellipse cx="64" cy="97" rx="15" ry="4" fill="#E8EEFF" {W(2)}/>
<ellipse cx="64" cy="80" rx="25" ry="9" fill="#F0B04A" {s()}/><ellipse cx="64" cy="79" rx="12" ry="3.4" fill="#E8EEFF" {W(2)}/>
<ellipse cx="64" cy="63" rx="20" ry="8" fill="#F5BE5A" {s()}/><ellipse cx="64" cy="62" rx="9" ry="3" fill="#E8EEFF" {W(2)}/>
<ellipse cx="64" cy="47" rx="15" ry="7" fill="#F8CA6A" {s()}/><ellipse cx="64" cy="46" rx="6" ry="2.4" fill="#E8EEFF" {W(2)}/>
<path d="M64 40 V22" {W(2.6)}/><path d="M64 22 L78 27 L64 32Z" fill="#E8453C" {W(1.8)}/>
<circle cx="44" cy="96" r="1.4" fill="#B86E22"/><circle cx="84" cy="96" r="1.4" fill="#B86E22"/><circle cx="50" cy="78" r="1.4" fill="#B86E22"/><circle cx="78" cy="80" r="1.4" fill="#B86E22"/>
{face(64, 96, d=19, k=0.6, mouth=False)}<path d="M60 102 Q64 105 68 102" fill="none" {W(2)}/>
'''), "герой: луковые кольца в хрустящем кляре | сцена: сложены высокой башней-небоскрёбом с флажком среди башен Москва-Сити")

# 34 Bistrot — крок-месье сидит за столиком бистро под полосатой маркизой
I["cafe-bistrot-savvinsky"] = (svg2("#FFF6EC", "#D88A6A", f'''
<path d="M6 8 H122 V30 H6Z" fill="#FFFFFF" {s()}/>
<path d="M6 8 H22 V30 H6Z M38 8 H54 V30 H38Z M70 8 H86 V30 H70Z M102 8 H118 V30 H102Z" fill="#2E8A5A"/>
<path d="M6 30 Q14 38 22 30 Q30 38 38 30 Q46 38 54 30 Q62 38 70 30 Q78 38 86 30 Q94 38 102 30 Q110 38 118 30" fill="#FFFFFF" {s()}/>
<ellipse cx="64" cy="98" rx="40" ry="8" fill="#FFFFFF" {s()}/>
<path d="M64 106 V124 M50 124 H78" {W(4)}/>
<path d="M30 92 L34 54 Q36 48 42 50 L86 50 Q92 48 94 54 L98 92Z" fill="#F0C070" {s()}/>
<path d="M30 70 L98 70" stroke="#F7E7B0" stroke-width="7"/>
<path d="M32 54 Q46 46 64 52 Q82 46 96 54 Q92 62 64 60 Q36 62 32 54Z" fill="#FFD84A" {W(2.4)}/>
<path d="M44 60 Q46 68 42 72 M78 60 Q80 68 84 74" fill="none" stroke="#FFD84A" stroke-width="4" stroke-linecap="round"/>
{face(64, 80, d=11, k=0.75)}
'''), "герой: горячий бутерброд крок-месье с тянущимся сыром | сцена: сидит за круглым столиком бистро под полосатой маркизой")

# 35 Генацвале (Пироговская) — рулетик из баклажана с орехами сидит на скамейке у пруда с лебедем
I["cafe-genatsvale-pirogovskaya"] = (svg2("#E4F6F2", "#5DB0A0", f'''
<path d="M0 86 Q64 76 128 86 V130 H0Z" fill="#6CB4E0" {s()}/>
<path d="M90 96 Q96 92 102 96" fill="none" stroke="#C6E8FF" stroke-width="2.4"/>
<path d="M96 88 Q90 70 98 66 Q106 64 104 72 Q102 78 106 82 Q116 82 114 90 Q104 94 96 88Z" fill="#FFFFFF" {W(2.4)}/><path d="M104 70 L110 70" stroke="#F0A040" stroke-width="2.6"/><circle cx="101" cy="68" r="1.2" fill="{O}"/>
<rect x="8" y="76" width="70" height="7" rx="2" fill="#B07A4A" {W(2.4)}/><path d="M16 83 V100 M70 83 V100" {W(3.4)}/>
<rect x="10" y="58" width="66" height="6" rx="2" fill="#B07A4A" {W(2.4)}/>
<g transform="rotate(-8 42 60)">
<path d="M18 52 Q18 30 42 30 Q66 30 66 52 Q66 76 42 76 Q18 76 18 52Z" fill="#6A3A7A" {s()}/>
<path d="M26 52 Q26 38 42 38 Q58 38 58 52 Q58 68 42 68 Q26 68 26 52Z" fill="#F3E6C8" {W(2.4)}/>
<circle cx="36" cy="46" r="2" fill="#C9A06A"/><circle cx="48" cy="44" r="2" fill="#C9A06A"/><circle cx="50" cy="58" r="2" fill="#C9A06A"/>
<circle cx="42" cy="34" r="2.4" fill="#E8304A"/><circle cx="50" cy="32" r="2.4" fill="#E8304A"/>
{face(42, 52, d=7, k=0.6)}</g>
'''), "герой: рулетик из баклажана с ореховой начинкой и зёрнами граната | сцена: сидит на скамейке у пруда и любуется белым лебедем")

# 36 Тополино.Rus — серый мышонок-пиццайоло в колпаке раскатывает тесто скалкой
I["cafe-topolino-krymsky"] = (svg2("#FFF4E8", "#E77A4E", f'''
<ellipse cx="64" cy="112" rx="56" ry="10" fill="#E8C9A0" {s()}/>
<ellipse cx="64" cy="104" rx="38" ry="8" fill="#FFF0D0" {s()}/>
<path d="M18 92 L110 92" stroke="#C98A4A" stroke-width="9" stroke-linecap="round"/><path d="M18 92 L110 92" fill="none" {W(1.6)}/>
<path d="M14 92 H8 M114 92 H120" stroke="#8A5A2A" stroke-width="6" stroke-linecap="round"/>
<path d="M44 90 Q40 64 64 62 Q88 64 84 90Z" fill="#B8B8C8" {s()}/>
<circle cx="40" cy="44" r="12" fill="#B8B8C8" {s()}/><circle cx="40" cy="44" r="6" fill="#FFC2D2"/>
<circle cx="88" cy="44" r="12" fill="#B8B8C8" {s()}/><circle cx="88" cy="44" r="6" fill="#FFC2D2"/>
<path d="M44 58 Q44 38 64 38 Q84 38 84 58 Q84 70 64 74 Q44 70 44 58Z" fill="#C8C8D6" {s()}/>
<path d="M50 34 Q46 20 58 22 Q62 12 72 18 Q84 16 80 32 Q64 28 50 34Z" fill="#FFFFFF" {s()}/>
{eye(56, 54, 0.6)}{eye(72, 54, 0.6)}
<circle cx="64" cy="64" r="3" fill="#FF6F91" {W(1.4)}/>
<path d="M50 62 L40 60 M50 66 L40 68 M78 62 L88 60 M78 66 L88 68" stroke="{O}" stroke-width="1.4"/>
<path d="M46 84 Q38 88 36 92 M82 84 Q90 88 92 92" fill="none" {W(3)}/>
'''), "герой: серый мышонок-пиццайоло в белом колпаке | сцена: раскатывает тесто для пиццы большой скалкой")

# 37 Тануки (Люберцы) — дораяки высовывается из красного японского фонарика
I["cafe-tanuki-lyubertsy"] = (svg2("#FFE9E4", "#D8484A", f'''
<path d="M64 4 V18" {W(3)}/>
<rect x="44" y="16" width="40" height="8" rx="3" fill="#2E2A3C" {s()}/>
<path d="M30 60 Q30 24 64 24 Q98 24 98 60 Q98 96 64 96 Q30 96 30 60Z" fill="#F04A3A" {s()}/>
<path d="M34 44 H94 M31 60 H97 M34 76 H94" stroke="#B8302A" stroke-width="2.4"/>
<rect x="44" y="94" width="40" height="8" rx="3" fill="#2E2A3C" {s()}/>
<path d="M58 102 L56 116 M64 102 V118 M70 102 L72 116" stroke="#FFD045" stroke-width="2.6" stroke-linecap="round"/>
<g transform="translate(0 4)">
<ellipse cx="64" cy="58" rx="24" ry="9" fill="#C9772E" {s()}/>
<rect x="40" y="58" width="48" height="6" fill="#6A2A2A" {W(2)}/>
<ellipse cx="64" cy="66" rx="24" ry="9" fill="#D98A3A" {s()}/>
{face(64, 66, d=9, k=0.6)}</g>
<path d="M22 30 Q16 24 20 18 M108 30 Q114 24 110 18" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".8"/>
'''), "герой: дораяки — два панкейка с бобовой пастой | сцена: выглядывает из красного японского бумажного фонарика")

# 38 Урюк (Люберцы) — нишалда облачком поднимается над пиалой
I["cafe-uryuk-lyubertsy"] = (svg2("#E6F0FF", "#2F6FB8", f'''
<path d="M22 80 Q22 112 64 112 Q106 112 106 80Z" fill="#FFFFFF" {s()}/>
<path d="M28 90 Q64 100 100 90" fill="none" stroke="#2F6FB8" stroke-width="4"/>
<path d="M38 98 L42 92 L46 98 M58 102 L62 96 L66 102 M82 98 L86 92 L90 98" fill="none" stroke="#2F6FB8" stroke-width="2"/>
<ellipse cx="64" cy="80" rx="42" ry="8" fill="#F4E9D6" {W(2.4)}/>
<path d="M32 78 Q24 62 38 56 Q36 38 54 40 Q60 26 76 34 Q94 30 94 48 Q108 54 98 70 Q100 80 90 80Z" fill="#FFFFFF" {s()}/>
<path d="M46 54 Q52 50 58 54 M72 46 Q78 42 84 46" fill="none" stroke="#E6E8F0" stroke-width="2.4"/>
{face(64, 62, d=11, k=0.8)}
<path d="M104 30 Q110 24 116 30" fill="none" stroke="#fff" stroke-width="2.4"/><circle cx="20" cy="40" r="3" fill="#fff" opacity=".8"/>
'''), "герой: белоснежная нишалда — взбитая восточная сладость | сцена: поднимается пышным облачком над синей узбекской пиалой")

# 39 Василий Алибабаевич — пашмак (сахарные нити) пушится в открытом сундуке с сокровищами
I["cafe-alibabaevich-lyubertsy"] = (svg2("#2E2F6A", "#16163A", f'''
<circle cx="18" cy="24" r="1.6" fill="#fff"/><circle cx="108" cy="18" r="1.6" fill="#fff"/>{sparkle(98, 42, 5, "#FFE68A")}{sparkle(24, 52, 4, "#FFE68A")}
<path d="M24 64 Q24 36 64 36 Q104 36 104 64Z" fill="#9A5A2E" {s()}/>
<path d="M24 64 H104 V112 H24Z" fill="#B06A34" {s()}/>
<path d="M24 76 H104 M44 64 V112 M84 64 V112" stroke="#E8B040" stroke-width="4"/>
<rect x="58" y="70" width="12" height="14" rx="2" fill="#E8B040" {W(2)}/>
<path d="M30 64 Q26 46 42 46 Q48 32 62 40 Q74 30 84 42 Q100 40 98 64Z" fill="#FFF4C8" {s()}/>
<path d="M38 56 Q50 48 60 56 Q70 46 82 54 M44 62 Q56 54 66 62" fill="none" stroke="#F2D88A" stroke-width="2"/>
{face(64, 54, d=10, k=0.7)}
<circle cx="34" cy="96" r="4" fill="#FFD045" {W(1.6)}/><circle cx="94" cy="94" r="4" fill="#FFD045" {W(1.6)}/>
'''), "герой: пушистый пашмак — восточная сахарная сладость-нити | сцена: распушился в открытом сундуке с сокровищами под звёздами")

# 40 Шоколадница (Люберцы) — глазированный сырок выглядывает из полосатой обёртки, как из спального мешка
I["cafe-shokoladnitsa-lyubertsy"] = (svg2("#FFF3E0", "#B0623A", f'''
<g transform="translate(-14 8) rotate(-6 64 70)">
<path d="M14 54 L96 54 L104 92 L22 92Z" fill="#4FA8E0" {s()}/>
<path d="M30 54 L38 92 M50 54 L58 92 M70 54 L78 92 M90 54 L98 92" stroke="#FFFFFF" stroke-width="5"/>
<path d="M14 54 L96 54 L104 92 L22 92Z" fill="none" {s()}/>
<rect x="56" y="38" width="56" height="26" rx="10" fill="#5A2A18" {s()}/>
<path d="M60 48 Q84 40 108 48" fill="none" stroke="#8A4A2A" stroke-width="2.4"/>
{face(84, 54, d=8, k=0.6)}
</g>
<path d="M18 30 Q24 22 30 28 M100 108 Q106 100 112 106" fill="none" stroke="#fff" stroke-width="2.4" opacity=".8"/>
<text x="20" y="22" font-family="Arial" font-weight="bold" font-size="11" fill="{O}">z</text><text x="28" y="14" font-family="Arial" font-weight="bold" font-size="8" fill="{O}">z</text>
'''), "герой: глазированный творожный сырок в шоколаде | сцена: высунулся из полосатой обёртки, как из спального мешка")

# 41 Мамас & Папас — булочка-курочка-наседка ведёт гуськом цыплят-профитролей
I["cafe-mamas-papas-lyubertsy"] = (svg2("#FFFBE6", "#9CCB4A", f'''
<path d="M0 100 Q64 92 128 100 V130 H0Z" fill="#7CC04A" {s()}/>
<path d="M22 54 Q22 30 46 30 Q60 30 62 44 Q78 40 86 54 Q92 76 72 88 Q48 96 30 86 Q18 76 22 54Z" fill="#F2B860" {s()}/>
<path d="M44 26 Q42 16 48 18 Q50 10 56 16 Q60 12 60 24" fill="#E8453C" {W(2)}/>
<path d="M18 50 L8 54 L18 58Z" fill="#F7A23A" {W(2)}/>
<circle cx="30" cy="46" r="3" fill="{O}"/><circle cx="29" cy="45" r="1" fill="#fff"/>
<path d="M50 62 Q62 56 70 66 Q62 72 50 62Z" fill="#E09A3E" {W(2)}/>
<circle cx="44" cy="60" r="1.4" fill="#FFF3D6"/><circle cx="36" cy="70" r="1.4" fill="#FFF3D6"/><circle cx="56" cy="78" r="1.4" fill="#FFF3D6"/>
<path d="M44 92 V100 M60 92 V100" stroke="#F7A23A" stroke-width="3"/>
<circle cx="92" cy="88" r="10" fill="#F7D07A" {W(2.4)}/><path d="M84 84 L80 86 L84 88Z" fill="#F7A23A"/>{eye(90, 86, 0.45)}
<circle cx="114" cy="92" r="9" fill="#F7D07A" {W(2.4)}/><path d="M106 88 L102 90 L106 92Z" fill="#F7A23A"/>{eye(112, 90, 0.42)}
<path d="M88 78 Q92 74 96 78 M110 83 Q114 79 118 83" fill="none" stroke="#E8B040" stroke-width="2"/>
'''), "герой: сдобная булочка-бриошь в форме курочки-наседки | сцена: ведёт гуськом по травке цыплят-профитролей")

# 42 Якитория (Люберцы) — кубики тофу ныряют с ложки-трамплина в мисо-суп
I["cafe-yakitoriya-lyubertsy"] = (svg2("#F8F0E0", "#C89A5A", f'''
<path d="M14 80 Q14 114 58 114 Q102 114 102 80Z" fill="#2E2A3C" {s()}/>
<path d="M18 86 Q58 98 98 86" fill="none" stroke="#C8302C" stroke-width="3"/>
<ellipse cx="58" cy="80" rx="44" ry="10" fill="#D9A660" {W(2.6)}/>
<path d="M30 78 Q36 74 42 78 M64 82 Q70 78 76 82" fill="none" stroke="#5E8A3A" stroke-width="3" stroke-linecap="round"/>
<rect x="46" y="74" width="9" height="9" fill="#FFFFFF" {W(2)}/>
<path d="M86 60 L120 40" stroke="#E8E2D6" stroke-width="5" stroke-linecap="round"/><path d="M86 60 L120 40" fill="none" {W(1.4)}/>
<ellipse cx="80" cy="64" rx="10" ry="6" fill="#E8E2D6" transform="rotate(-30 80 64)" {W(2)}/>
<g transform="rotate(20 66 38)"><rect x="54" y="26" width="24" height="24" rx="3" fill="#FFFFFF" {s()}/>{face(66, 37, d=5, k=0.5)}</g>
<path d="M38 50 Q44 42 52 46" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<circle cx="40" cy="62" r="2.4" fill="#fff"/><circle cx="34" cy="56" r="1.8" fill="#fff"/>
'''), "герой: белый кубик тофу | сцена: прыгает с ложки, как с трамплина, в чашку мисо-супа")

# 43 Здрасте (Камова) — булочка-улитка с корицей машет рукой у двери кофейни с колокольчиком
I["cafe-zdraste-kamova"] = (svg2("#EAF8FF", "#7FB8D8", f'''
<rect x="70" y="14" width="46" height="110" fill="#5A8AC0" {s()}/><rect x="78" y="24" width="30" height="40" rx="3" fill="#CDEBFF" {W(2.4)}/>
<circle cx="100" cy="82" r="3" fill="#FFD045" {W(1.6)}/>
<path d="M66 18 V28" {W(2)}/><path d="M60 38 Q60 28 66 28 Q72 28 72 38Z" fill="#FFD045" {W(2)}/><circle cx="66" cy="40" r="2" fill="{O}"/>
<path d="M56 30 Q52 34 54 40 M76 30 Q80 34 78 40" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
<ellipse cx="44" cy="112" rx="36" ry="7" fill="#FFFFFF" {s()}/>
<circle cx="44" cy="82" r="28" fill="#E4A65A" {s()}/>
<path d="M44 82 m0 -6 a6 6 0 1 1 -6 6 a12 12 0 1 1 12 12 a18 18 0 1 1 -18 -18" fill="none" stroke="#9A5A2A" stroke-width="3"/>
<path d="M22 70 Q34 62 44 66 Q58 62 66 72" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round"/>
<path d="M68 76 Q78 66 74 54" fill="none" {W(3.2)}/><circle cx="74" cy="52" r="4" fill="#E4A65A" {W(2)}/>
{face(44, 86, d=9, k=0.7)}
'''), "герой: булочка-улитка с корицей и глазурью | сцена: машет рукой и здоровается у двери кофейни с колокольчиком")

# 44 Арчибальд — трёхъярусное желе-пудинг дрожит на блюде, увенчанное вишенкой
I["cafe-archibald-lyubertsy"] = (svg2("#F0FFF4", "#4FB88A", f'''
<ellipse cx="64" cy="110" rx="48" ry="9" fill="#FFFFFF" {s()}/>
<path d="M28 108 Q26 86 34 82 H94 Q102 86 100 108Z" fill="#F06A8A" {s()}/>
<path d="M38 84 Q38 66 44 62 H84 Q90 66 90 84Z" fill="#FFC23A" {s()}/>
<path d="M48 64 Q48 48 54 44 H74 Q80 48 80 64Z" fill="#7CC8F0" {s()}/>
<path d="M36 90 Q40 86 44 90 M86 92 Q90 88 94 92 M46 70 Q50 66 54 70" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".7"/>
<circle cx="64" cy="38" r="7" fill="#C8102E" {W(2)}/><path d="M64 31 Q66 22 74 20" fill="none" {W(2)}/>
{face(64, 94, d=12, k=0.75)}
<path d="M16 76 Q12 82 16 88 M112 76 Q116 82 112 88 M20 60 Q16 66 20 72 M108 60 Q112 66 108 72" fill="none" {W(2.4)}/>
'''), "герой: трёхъярусное желе-пудинг — розовое, жёлтое и голубое | сцена: весело дрожит на блюде, увенчанное вишенкой")

# 45 Я на Бали — айс-латте со льдом в высоком стакане сёрфит на доске по волне
I["cafe-ya-na-bali-lyubertsy"] = (svg2("#FFF6D8", "#3EC0C8", f'''
<circle cx="100" cy="26" r="12" fill="#FFD045" {W(2.2)}/>
<path d="M0 92 Q24 60 56 74 Q76 84 70 98 Q96 80 128 94 V130 H0Z" fill="#2FA8D8" {s()}/>
<path d="M56 74 Q64 70 68 76 M14 80 Q20 76 26 80" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>
<g transform="rotate(-14 64 88)"><ellipse cx="64" cy="94" rx="40" ry="7" fill="#FF8A4A" {s()}/><path d="M28 94 H100" stroke="#FFFFFF" stroke-width="2"/></g>
<path d="M46 40 H82 L78 86 Q78 90 74 90 H54 Q50 90 50 86Z" fill="#E6F6FF" opacity=".95" {s()}/>
<path d="M48 58 H80 L78 86 Q78 90 74 90 H54 Q50 90 50 86Z" fill="#C8955E"/>
<path d="M48 52 H80 L79.5 60 H48.5Z" fill="#FFF6E6"/>
<rect x="54" y="62" width="9" height="8" rx="2" fill="#FFFFFF" opacity=".8" {W(1.4)}/><rect x="66" y="68" width="9" height="8" rx="2" fill="#FFFFFF" opacity=".8" {W(1.4)}/>
<path d="M46 40 H82 L78 86 Q78 90 74 90 H54 Q50 90 50 86Z" fill="none" {s()}/>
<path d="M70 40 L80 14" stroke="#F04A8A" stroke-width="4" stroke-linecap="round"/>
{face(64, 76, d=8, k=0.6)}
<path d="M48 60 Q36 54 34 44 M80 60 Q92 54 96 46" fill="none" {W(3)}/>
'''), "герой: айс-латте со льдом в высоком стакане с трубочкой | сцена: катается на доске для сёрфинга по тёплой волне")

# 46 Deluxe pizza — квадратная римская пицца на противне в золотой цепи и тёмных очках
I["cafe-deluxe-pizza-lyubertsy"] = (svg2("#2A2A2E", "#4A3A2A", f'''
{sparkle(20, 30, 6, "#FFD045")}{sparkle(108, 22, 5, "#FFD045")}{sparkle(110, 104, 4, "#FFD045")}
<rect x="14" y="40" width="100" height="72" rx="6" fill="#8A8A9A" {s()}/>
<rect x="20" y="46" width="88" height="60" rx="4" fill="#E9A24A" {s()}/>
<rect x="26" y="52" width="76" height="48" rx="3" fill="#E8483A"/>
<path d="M30 58 Q42 54 52 62 Q62 56 72 64 Q84 56 98 62 V94 Q84 100 64 96 Q44 100 30 94Z" fill="#FFE07A"/>
<circle cx="40" cy="88" r="5" fill="#C8302C" {W(1.6)}/><circle cx="90" cy="88" r="5" fill="#C8302C" {W(1.6)}/>
<path d="M88 60 L94 54 M36 66 L42 60" stroke="#4E9A3A" stroke-width="3" stroke-linecap="round"/>
<path d="M42 70 H60 Q62 82 51 82 Q40 82 42 70Z M68 70 H86 Q88 82 77 82 Q66 82 68 70Z" fill="#1E1E28"/><path d="M60 72 H68" {W(2.4)}/>
<path d="M56 90 Q64 94 72 90" fill="none" {W(2.4)}/>
<path d="M30 112 Q64 130 98 112" fill="none" stroke="#FFD045" stroke-width="4" stroke-dasharray="5 3"/>
<circle cx="64" cy="122" r="6" fill="#FFD045" {W(2)}/>
'''), "герой: квадратная римская пицца на противне | сцена: красуется в золотой цепи и тёмных очках, как звезда «делюкс»")

# 47 Град Южный — пряничный город-терем стоит на холме
I["cafe-grad-yuzhny-krasnogorsk"] = (svg2("#FFF0E0", "#C88A5A", f'''
<path d="M0 104 Q64 86 128 104 V130 H0Z" fill="#9AD06A" {s()}/>
<rect x="28" y="62" width="72" height="44" fill="#C8783A" {s()}/>
<path d="M22 64 L64 30 L106 64Z" fill="#9A4E22" {s()}/>
<path d="M28 64 Q34 70 40 64 Q46 70 52 64 Q58 70 64 64 Q70 70 76 64 Q82 70 88 64 Q94 70 100 64" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>
<path d="M40 44 Q46 50 52 44 M76 44 Q82 50 88 44 M56 36 Q64 42 72 36" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"/>
<rect x="10" y="74" width="18" height="32" fill="#D88A4A" {W(2.4)}/><path d="M8 76 L19 60 L30 76Z" fill="#9A4E22" {W(2.4)}/>
<rect x="100" y="74" width="18" height="32" fill="#D88A4A" {W(2.4)}/><path d="M98 76 L109 60 L120 76Z" fill="#9A4E22" {W(2.4)}/>
<path d="M54 106 V90 Q54 82 64 82 Q74 82 74 90 V106Z" fill="#7A3E1A" {W(2.4)}/>
<circle cx="64" cy="24" r="4" fill="#FFD045" {W(1.6)}/>
<circle cx="18" cy="88" r="1.8" fill="#fff"/><circle cx="110" cy="88" r="1.8" fill="#fff"/>
{face(64, 72, d=11, k=0.7)}
'''), "герой: медовый пряничный терем с глазурью-кружевами | сцена: стоит сказочным городом на зелёном холме между двумя башенками")

# 48 Сироп — карамельный леденец-петушок на палочке кукарекает на заборе на рассвете
I["cafe-sirop-gavrilkovo"] = (svg2("#FFE6C8", "#F07A5A", f'''
<circle cx="96" cy="96" r="22" fill="#FFD045" {W(2.2)}/>
<path d="M0 92 H128" {W(0)}/>
<rect x="0" y="94" width="128" height="10" fill="#B07A4A" {W(2.4)}/>
<path d="M10 128 V86 L16 80 L22 86 V128 M36 128 V86 L42 80 L48 86 V128 M84 128 V86 L90 80 L96 86 V128 M110 128 V86 L116 80 L122 86 V128" fill="#C8905A" {W(2.4)}/>
<path d="M62 120 V84" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round"/><path d="M62 120 V84" fill="none" {W(1.4)}/>
<path d="M36 70 Q34 46 56 44 Q58 28 70 32 Q82 28 80 42 Q92 52 86 66 Q96 64 100 54 Q106 72 92 80 Q74 90 54 86 Q38 82 36 70Z" fill="#E8302A" opacity=".92" {s()}/>
<path d="M58 34 Q60 22 66 28 Q70 20 74 30" fill="#FF7A3A" {W(2)}/>
<path d="M50 50 L40 54 L50 58Z" fill="#FFB23A" {W(2)}/>
<circle cx="58" cy="50" r="3" fill="{O}"/><circle cx="57" cy="49" r="1" fill="#fff"/>
<path d="M60 66 Q70 60 80 68" fill="none" stroke="#FFB0A0" stroke-width="2.4"/>
<path d="M30 46 Q24 44 22 38 M28 54 Q20 54 16 50" fill="none" {W(2.2)}/>
<path d="M44 40 Q42 38 46 36" fill="none" stroke="#fff" stroke-width="2" opacity=".8"/>
'''), "герой: карамельный леденец-петушок на палочке | сцена: громко кукарекает с деревенского забора на рассвете")

# 49 Сикварули (любовь) — мацони в глиняном горшочке держит воздушный шарик-сердечко
I["cafe-sikvaruli-otradnoe"] = (svg2("#FFEFF4", "#E86A8E", f'''
<path d="M84 24 Q72 10 64 20 Q58 30 84 52 Q110 30 104 20 Q96 10 84 24Z" fill="#F0304A" {s()}/>
<path d="M74 22 Q72 26 74 30" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".8"/>
<path d="M84 52 Q80 62 84 70 Q88 76 82 84" fill="none" {W(1.8)}/>
<ellipse cx="54" cy="112" rx="36" ry="7" fill="#FFFFFF" {W(2.4)}/>
<path d="M24 74 Q20 112 54 112 Q88 112 84 74Z" fill="#C8683A" {s()}/>
<rect x="20" y="66" width="68" height="10" rx="4" fill="#D8784A" {s()}/>
<path d="M28 66 Q30 54 54 54 Q78 54 80 66Z" fill="#FFFFFF" {s()}/>
<path d="M30 92 Q54 100 78 92" fill="none" stroke="#9A4A22" stroke-width="2.4"/>
<path d="M84 86 Q90 84 86 80" fill="none" {W(3)}/>
{face(54, 86, d=10, k=0.75)}
'''), "герой: грузинский мацони в глиняном горшочке | сцена: держит за ниточку воздушный шарик-сердечко")

# 50 Izym — кекс с изюмом, изюминки выглядывают из него, как из окошек
I["cafe-izym-otradnoe"] = (svg2("#F2EEFF", "#6A5AB8", f'''
<ellipse cx="64" cy="112" rx="44" ry="8" fill="#FFFFFF" {s()}/>
<path d="M22 104 V58 Q22 34 64 34 Q106 34 106 58 V104Z" fill="#F2C470" {s()}/>
<path d="M22 58 Q30 44 46 46 Q52 36 64 42 Q76 36 82 46 Q98 44 106 58" fill="none" stroke="#C88A3A" stroke-width="3"/>
<path d="M22 70 Q64 76 106 70" fill="none" stroke="#FFF3D0" stroke-width="2"/>
<circle cx="40" cy="64" r="6" fill="#5A2A4A" {W(2)}/>{eye(38, 63, 0.35)}{eye(42, 63, 0.35)}
<circle cx="86" cy="60" r="6" fill="#5A2A4A" {W(2)}/>{eye(84, 59, 0.35)}{eye(88, 59, 0.35)}
<circle cx="36" cy="92" r="6" fill="#5A2A4A" {W(2)}/>{eye(34, 91, 0.35)}{eye(38, 91, 0.35)}
<circle cx="92" cy="92" r="6" fill="#5A2A4A" {W(2)}/>{eye(90, 91, 0.35)}{eye(94, 91, 0.35)}
<path d="M50 24 Q56 30 64 26 Q72 30 78 24" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
{face(64, 82, d=11, k=0.8)}
'''), "герой: пышный кекс с изюмом | сцена: изюминки-малыши выглядывают из него, как из окошек")

# 51 Швили (Крокус Сити) — люля-кебаб в лаваше-лодочке плывёт по озеру с фонтанами
I["cafe-shvili-crocus"] = (svg2("#E8F4FF", "#5A8AE0", f'''
<path d="M24 46 Q22 26 26 18 M24 46 Q28 28 34 22 M104 44 Q106 24 102 16 M104 44 Q100 26 94 20" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>
<circle cx="26" cy="16" r="3" fill="#fff"/><circle cx="102" cy="14" r="3" fill="#fff"/>
<path d="M0 72 Q32 64 64 72 Q96 80 128 72 V130 H0Z" fill="#3E7FD0" {s()}/>
<path d="M12 92 Q22 88 32 92 M94 98 Q104 94 114 98" fill="none" stroke="#9ED0FF" stroke-width="2.4"/>
<path d="M18 70 Q24 98 64 98 Q104 98 110 70 Q90 80 64 80 Q38 80 18 70Z" fill="#F4E2B8" {s()}/>
<circle cx="40" cy="86" r="1.6" fill="#D9B070"/><circle cx="84" cy="88" r="1.6" fill="#D9B070"/>
<rect x="30" y="58" width="68" height="20" rx="10" fill="#A8502E" {s()}/>
<path d="M42 60 V76 M56 60 V76 M70 60 V76 M84 60 V76" stroke="#7A3418" stroke-width="2"/>
<path d="M34 56 L40 50 L46 56 M76 54 L82 48 L88 54" fill="none" stroke="#6CBF4A" stroke-width="3" stroke-linecap="round"/>
{face(64, 66, d=10, k=0.6)}
'''), "герой: люля-кебаб в лаваше-лодочке с кинзой | сцена: плывёт по озеру между двумя фонтанами")

# 52 Кайфын — коробочка вок в наушниках кайфует под музыку
I["cafe-kayfyn-olgino"] = (svg2("#F6E6FF", "#B04ACB", f'''
<path d="M30 52 L38 112 H90 L98 52Z" fill="#FFFFFF" {s()}/>
<path d="M30 52 L22 40 H106 L98 52" fill="#F4F4F8" {s()}/>
<path d="M44 72 L84 72" stroke="#E8302A" stroke-width="5"/><circle cx="64" cy="94" r="8" fill="#E8302A"/>
<path d="M36 40 Q44 22 54 38 Q60 20 70 36 Q78 22 88 38" fill="none" stroke="#F2C060" stroke-width="5" stroke-linecap="round"/>
<path d="M36 40 Q44 22 54 38 Q60 20 70 36 Q78 22 88 38" fill="none" {W(1.4)}/>
<path d="M78 34 L98 8 M84 36 L106 12" stroke="#C88A4A" stroke-width="4" stroke-linecap="round"/>
<path d="M26 78 Q26 54 64 54 Q102 54 102 78" fill="none" {W(4)}/>
<rect x="18" y="72" width="14" height="22" rx="6" fill="#4A4AE0" {s()}/><rect x="96" y="72" width="14" height="22" rx="6" fill="#4A4AE0" {s()}/>
<path d="M52 80 Q56 76 60 80 M68 80 Q72 76 76 80" fill="none" {W(2.4)}/><path d="M58 88 Q64 94 70 88" fill="none" {W(2.4)}/>
<path d="M112 46 V34 L120 32 V42" fill="none" stroke="#FFFFFF" stroke-width="2.4"/><ellipse cx="110" cy="47" rx="3" ry="2.4" fill="#fff"/><ellipse cx="118" cy="43" rx="3" ry="2.4" fill="#fff"/>
'''), "герой: коробочка вок с лапшой и палочками | сцена: зажмурившись, кайфует под музыку в больших наушниках")

# 53 Тануки (Балашиха) — гёдза залезает в детскую трубу-лабиринт
I["cafe-tanuki-balashikha"] = (svg2("#E8FFF0", "#3AB87A", f'''
<path d="M0 104 H128 V130 H0Z" fill="#FFD045" {s()}/>
<path d="M-10 64 Q-10 40 14 40 H70 Q94 40 94 64 Q94 88 70 88 H14 Q-10 88 -10 64Z" fill="#F05A7A" {s()}/>
<ellipse cx="94" cy="64" rx="14" ry="24" fill="#FFB0C0" {s()}/>
<ellipse cx="94" cy="64" rx="9" ry="18" fill="#5A2A3A"/>
<path d="M20 40 V88 M44 40 V88" stroke="#C8304A" stroke-width="2.4"/>
<path d="M78 76 Q78 54 100 52 Q122 54 122 76 Q110 84 100 82 Q90 84 78 76Z" fill="#F7E7C8" {s()}/>
<path d="M84 64 L88 58 M94 58 L96 52 M104 58 L106 52 M114 64 L116 58" stroke="#D9B070" stroke-width="2.4"/>
<path d="M80 78 Q100 86 120 78" fill="#E8A040" {W(2)}/>
{face(100, 68, d=7, k=0.55)}
<path d="M120 70 Q126 64 124 58" fill="none" {W(2.8)}/>
'''), "герой: японский пельмешек гёдза с поджаристым донцем | сцена: выбирается из розовой трубы детского лабиринта")

# 54 Чайка (Ольгино) — пирожок-чайка с крылышками из теста летит над волнами
I["cafe-chayka-olgino"] = (svg2("#E4F6FF", "#4A9AD8", f'''
<path d="M0 96 Q16 88 32 96 Q48 104 64 96 Q80 88 96 96 Q112 104 128 96 V130 H0Z" fill="#2F7FC8" {s()}/>
<path d="M14 110 Q24 106 34 110 M84 114 Q94 110 104 114" fill="none" stroke="#9ED0FF" stroke-width="2.4"/>
<circle cx="104" cy="24" r="10" fill="#FFF3B0" {W(2)}/>
<path d="M40 60 Q24 34 6 40 Q18 50 22 64 Q32 70 40 66Z" fill="#F7D08A" {s()}/>
<path d="M88 60 Q104 34 122 40 Q110 50 106 64 Q96 70 88 66Z" fill="#F7D08A" {s()}/>
<path d="M14 44 Q22 48 26 56 M114 44 Q106 48 102 56" fill="none" stroke="#D9A04A" stroke-width="2"/>
<path d="M32 70 Q32 50 64 50 Q96 50 96 70 Q96 84 64 84 Q32 84 32 70Z" fill="#E8A850" {s()}/>
<path d="M40 56 Q50 64 58 54 Q66 64 74 54 Q82 64 90 58" fill="none" stroke="#B8742A" stroke-width="2.4"/>
<path d="M60 74 L64 80 L68 74Z" fill="#FFB23A" {W(1.6)}/>
{face(64, 66, d=10, k=0.7, mouth=False)}
'''), "герой: румяный пирожок-чайка с крылышками из теста | сцена: парит над морскими волнами под бледной луной")

# 55 D&D Дарим Добро — дагестанский чуду, перевязанный лентой с бантом, как подарок
I["cafe-darim-dobro-balashikha"] = (svg2("#E6FFF8", "#2E9A8A", f'''
{sparkle(20, 28, 6)}{sparkle(108, 30, 5)}{sparkle(110, 100, 4)}
<path d="M14 82 Q14 54 64 50 Q114 54 114 82 Q114 104 64 106 Q14 104 14 82Z" fill="#F0C36A" {s()}/>
<path d="M22 80 Q22 62 64 58 Q106 62 106 80 Q106 96 64 98 Q22 96 22 80Z" fill="none" stroke="#D9963E" stroke-width="2.4" stroke-dasharray="4 4"/>
<path d="M64 50 V106" stroke="#E8304A" stroke-width="8"/>
<path d="M14 78 Q64 86 114 78" fill="none" stroke="#E8304A" stroke-width="8"/>
<path d="M64 50 V106 M14 78 Q64 86 114 78" fill="none" stroke="#9A1A2A" stroke-width="1.2"/>
<path d="M64 50 Q46 32 42 44 Q42 54 64 50 Q82 32 86 44 Q86 54 64 50Z" fill="#F04A5A" {s()}/>
<circle cx="64" cy="50" r="5" fill="#C8203A" {W(2)}/>
{face(40, 92, d=7, k=0.55)}
'''), "герой: дагестанский пирог чуду | сцена: перевязан красной лентой с пышным бантом, как подарок от души")


if __name__ == "__main__":
    reg = os.path.join(ROOT, "icons-src", "subjects.txt")
    lines = open(reg, encoding="utf-8").read().splitlines()
    lines = [l for l in lines if l.split(" — ", 1)[0] not in I]
    for pid, (svg_, subj) in I.items():
        open(os.path.join(ROOT, "icons-src", pid + ".svg"), "w").write(svg_)
        lines.append(f"{pid} — {subj}")
    open(reg, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("иконок:", len(I))
