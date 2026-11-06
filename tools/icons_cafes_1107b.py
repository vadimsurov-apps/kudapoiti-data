"""Робот cafes, 2026-11-07 (ночь): 17 иконок кафе, каждая придумана и нарисована отдельно
(правило абсолютной уникальности: свой герой, своя сцена, своя палитра фона).
Запуск из корня: python3 tools/icons_cafes_1107b.py  → icons-src/<id>.svg + строки в icons-src/subjects.txt"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def W(w):
    return s(f'stroke-width="{w}"')


def svg2(a, b, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
<defs>
 <radialGradient id="g" cx="38%" cy="28%" r="85%"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></radialGradient>
 <clipPath id="c"><circle cx="64" cy="64" r="61"/></clipPath>
</defs>
<circle cx="64" cy="64" r="61" fill="url(#g)"/>
<g clip-path="url(#c)">{body}</g>
<ellipse cx="44" cy="22" rx="20" ry="7" fill="#fff" opacity=".3"/>
</svg>'''


I = {}

# 1 Шахин-Шах — азербайджанский шах-плов: золотой купол из лаваша, отрезан кусочек с рисом и курагой; позади восточная арка
I["cafe-shakhin-shakh"] = (svg2("#FFE9B0", "#E8893A", f'''
<path d="M22 128 V58 Q22 30 64 14 Q106 30 106 58 V128" fill="#3FA9A0" opacity=".55" {W(2.6)}/>
<path d="M30 128 V60 Q30 38 64 24 Q98 38 98 60 V128" fill="#FFF1D6" opacity=".7"/>
<ellipse cx="64" cy="104" rx="46" ry="10" fill="#fff" {s()}/>
<path d="M24 100 Q24 46 64 42 Q104 46 104 100Z" fill="#E9A445" {s()}/>
<path d="M34 64 Q64 54 94 64 M28 82 Q64 72 100 82" fill="none" stroke="#C47A25" stroke-width="2.4" stroke-dasharray="4 4"/>
<path d="M78 100 L104 100 Q104 70 92 56 Z" fill="#FFF6D8" {s()}/>
<circle cx="90" cy="84" r="2.4" fill="#F5C23E"/><circle cx="96" cy="92" r="2.4" fill="#F5C23E"/><circle cx="86" cy="94" r="2" fill="#B5503A"/>
<circle cx="95" cy="76" r="2.2" fill="#FF9E3D"/><circle cx="84" cy="86" r="1.8" fill="#F5C23E"/>
{face(54, 76, d=10, k=0.95)}
<path d="M64 42 V34" {W(3)}/><circle cx="64" cy="31" r="4" fill="#F5C23E" {W(2.4)}/>
'''), "герой: шах-плов — золотой купол из хрустящего лаваша с отрезанным кусочком риса и кураги | сцена: стоит под бирюзовой восточной аркой")

# 2 Матам — брускетта с черри подбрасывает листик базилика
I["cafe-matam"] = (svg2("#DDF7EC", "#45AE92", f'''
<path d="M30 30 Q40 18 52 26" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
<path d="M78 22 Q92 10 100 26 Q90 34 78 22Z" fill="#3E9C3A" {W(2.4)}/><path d="M80 23 Q90 20 98 25" fill="none" stroke="#9BE08A" stroke-width="1.6"/>
<path d="M18 86 Q20 60 44 56 L96 50 Q114 50 112 74 Q110 98 86 100 L36 104 Q16 106 18 86Z" fill="#E7B467" {s()}/>
<path d="M26 84 Q28 66 46 63 L94 58 Q104 60 104 74 Q102 90 84 92 L38 96 Q26 96 26 84Z" fill="#F6D497"/>
<circle cx="44" cy="70" r="9" fill="#E8394A" {W(2.4)}/><circle cx="44" cy="70" r="4" fill="#FF8C8C"/>
<circle cx="88" cy="66" r="9" fill="#E8394A" {W(2.4)}/><circle cx="88" cy="66" r="4" fill="#FF8C8C"/>
<path d="M60 64 Q66 56 72 64 Q66 70 60 64Z" fill="#3E9C3A" {W(2)}/>
{face(66, 82, d=10, k=0.85)}
<path d="M54 50 Q50 40 60 34 M74 46 Q78 36 72 30" fill="none" {W(2.2)} stroke-dasharray="3 4"/>
'''), "герой: брускетта с половинками черри | сцена: подбрасывает вверх листик базилика")

# 3 Меркалето (парк «Садовники») — панини с полосками гриля сидит на садовой скамейке между тюльпанами
I["cafe-merkaleto-sadovniki"] = (svg2("#F3FFE3", "#9FD3E8", f'''
<rect x="0" y="100" width="128" height="30" fill="#7CCB5E" {W(2.4)}/>
<path d="M14 100 V80 M14 80 Q8 74 10 66 Q14 70 14 72 Q16 66 20 66 Q22 74 14 80Z" fill="#F0507A" {W(2)}/>
<path d="M114 100 V82 M114 82 Q108 76 110 68 Q114 72 114 74 Q116 68 120 68 Q122 76 114 82Z" fill="#FFC53D" {W(2)}/>
<path d="M14 92 Q8 88 6 92 M114 94 Q120 90 122 94" fill="none" stroke="#3E9C3A" stroke-width="3"/>
<rect x="26" y="84" width="76" height="8" rx="3" fill="#B77A45" {W(2.4)}/>
<path d="M32 92 V108 M96 92 V108" {W(3)}/>
<rect x="30" y="52" width="68" height="34" rx="12" fill="#EAB15E" {s()}/>
<path d="M40 54 L52 84 M54 54 L66 84 M68 54 L80 84 M82 54 L92 78" stroke="#9C5B26" stroke-width="3.4" stroke-linecap="round" opacity=".75"/>
<path d="M34 84 Q40 92 46 86 Q52 94 58 86" fill="#FFE07A" {W(2)}/>
{face(64, 68, d=11, k=0.95)}
'''), "герой: панини с тёмными полосками гриля и капелькой сыра | сцена: отдыхает на садовой скамейке между тюльпанами")

# 4 Сытый лось — круглая булочка-лось с рогами из кренделей
I["cafe-sytyy-los-tekstilshchiki"] = (svg2("#EEF7D8", "#86B24A", f'''
<path d="M42 44 Q22 40 20 24 Q30 18 36 28 Q36 14 46 16 Q52 26 46 36 Q50 40 48 46Z" fill="#C9874A" {s()}/>
<path d="M86 44 Q106 40 108 24 Q98 18 92 28 Q92 14 82 16 Q76 26 82 36 Q78 40 80 46Z" fill="#C9874A" {s()}/>
<circle cx="30" cy="27" r="1.5" fill="#fff"/><circle cx="98" cy="27" r="1.5" fill="#fff"/><circle cx="44" cy="24" r="1.5" fill="#fff"/><circle cx="84" cy="24" r="1.5" fill="#fff"/>
<ellipse cx="64" cy="76" rx="40" ry="36" fill="#E3A45F" {s()}/>
<ellipse cx="64" cy="94" rx="20" ry="13" fill="#F3C98E" {W(2.6)}/>
<ellipse cx="57" cy="93" rx="2.6" ry="3.4" fill="{O}"/><ellipse cx="71" cy="93" rx="2.6" ry="3.4" fill="{O}"/>
<path d="M58 101 Q64 105 70 101" fill="none" {W(2.4)}/>
{face(64, 68, d=13, k=1.0, mouth=False)}
<ellipse cx="48" cy="54" rx="2" ry="1.2" fill="#FFF3D6" transform="rotate(-30 48 54)"/><ellipse cx="78" cy="52" rx="2" ry="1.2" fill="#FFF3D6" transform="rotate(30 78 52)"/><ellipse cx="64" cy="48" rx="2" ry="1.2" fill="#FFF3D6"/>
'''), "герой: круглая булочка-лосёнок с рогами из кренделей и мягким носом | сцена: сытно улыбается крупным планом")

# 5 Вилладжио — квадратный равиоли с зубчатым краем на тосканском холме с кипарисами
I["cafe-villaggio"] = (svg2("#EEF1FF", "#8EA2E6", f'''
<path d="M-4 96 Q30 70 70 88 Q100 72 132 86 V130 H-4Z" fill="#8FCB6B" {W(2.4)}/>
<path d="M-4 110 Q40 96 132 108 V130 H-4Z" fill="#6DB356"/>
<ellipse cx="18" cy="70" rx="6" ry="20" fill="#2F7A46" {W(2.2)}/><ellipse cx="108" cy="66" rx="6" ry="22" fill="#2F7A46" {W(2.2)}/><ellipse cx="96" cy="72" rx="4.5" ry="15" fill="#3A8B52" {W(2)}/>
<rect x="34" y="40" width="60" height="60" rx="6" fill="#F7D98C" {s()} transform="rotate(-6 64 70)"/>
<rect x="44" y="50" width="40" height="40" rx="10" fill="#FBE7B0" transform="rotate(-6 64 70)"/>
<g transform="rotate(-6 64 70)" fill="none" stroke="#D9A847" stroke-width="2">
<path d="M38 44 h52 M38 96 h52 M38 44 v52 M90 44 v52" stroke-dasharray="2 4"/></g>
{face(64, 70, d=10, k=0.95)}
<path d="M66 40 Q70 30 78 30" fill="none" stroke="#3E9C3A" stroke-width="3" stroke-linecap="round"/><path d="M76 30 Q84 24 88 32 Q80 36 76 30Z" fill="#4DB34A" {W(1.8)}/>
'''), "герой: квадратный равиоли с зубчатым краем и листиком базилика | сцена: стоит на тосканском холме между кипарисами")

# 6 Qartuli (Грузинский Вал) — хлеб шоти выпрыгивает из горячей печи-тоне
I["cafe-qartuli-gruzinsky-val"] = (svg2("#FFE3D2", "#C6603F", f'''
<ellipse cx="64" cy="112" rx="48" ry="16" fill="#9A5A3A" {s()}/>
<ellipse cx="64" cy="108" rx="34" ry="9" fill="#3A2232"/>
<ellipse cx="64" cy="110" rx="26" ry="5" fill="#FF8A2A" opacity=".9"/>
<path d="M30 96 Q34 88 30 80 M98 96 Q94 88 98 80" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" opacity=".8"/>
<path d="M14 64 Q40 30 64 30 Q88 30 114 64 Q88 80 64 80 Q40 80 14 64Z" fill="#E8B060" {s()} transform="rotate(-12 64 56)"/>
<path d="M30 60 Q50 44 64 44 Q80 44 98 58" fill="none" stroke="#C47B30" stroke-width="2.6" stroke-linecap="round" transform="rotate(-12 64 56)"/>
{face(64, 60, d=11, k=0.95)}
<path d="M58 92 V84 M70 92 V84" fill="none" {W(2.2)} stroke-dasharray="2 3"/>
{sparkle(108, 30, 6)}
'''), "герой: грузинский хлеб шоти в форме лодочки | сцена: выпрыгивает из раскалённой печи-тоне")

# 7 Бора Бора — половинка кокоса с трубочкой и цветочным ожерельем на закате
I["cafe-bora-bora"] = (svg2("#FFE0CC", "#A967D2", f'''
<circle cx="98" cy="38" r="12" fill="#FFD36B" opacity=".9"/>
<path d="M82 22 L92 6" stroke="#fff" stroke-width="5" stroke-linecap="round"/><path d="M82 22 L92 6" {W(2)} fill="none"/>
<path d="M76 40 L86 18" stroke="#FF6FA3" stroke-width="5" stroke-linecap="round"/>
<path d="M22 58 H106 Q104 106 64 108 Q24 106 22 58Z" fill="#8A5636" {s()}/>
<ellipse cx="64" cy="58" rx="42" ry="10" fill="#FFFDF5" {s()}/>
<ellipse cx="64" cy="58" rx="32" ry="6" fill="#F4EEDC"/>
<circle cx="46" cy="88" r="1.6" fill="#5E3A24"/><circle cx="84" cy="96" r="1.6" fill="#5E3A24"/><circle cx="78" cy="80" r="1.4" fill="#5E3A24"/>
{face(64, 80, d=11, k=0.95)}
''' + "".join(f'<circle cx="{x}" cy="{y}" r="5.2" fill="{c}" {W(1.8)}/><circle cx="{x}" cy="{y}" r="1.6" fill="#FFF3A0"/>'
              for n, (x, y) in enumerate([(26, 70), (30, 82), (36, 93), (46, 101), (58, 106), (70, 106), (82, 101), (92, 93), (98, 82), (102, 70)])
              for c in [["#FF6FA3", "#FFD23F", "#FF8C42", "#FFFFFF"][n % 4]])
), "герой: половинка кокоса с полосатой трубочкой | сцена: в цветочном ожерелье-лее на фоне закатного солнца")

# 8 SOHO Country Club — печёная картошка в фольге с тающим маслом у сосны на загородной лужайке
I["cafe-soho-country-club"] = (svg2("#F6FAD6", "#A3C452", f'''
<path d="M10 94 L22 44 L34 94Z" fill="#2E7D4F" {W(2.4)}/><path d="M14 78 L22 54 L30 78Z" fill="#3E9A60"/><rect x="19" y="94" width="6" height="10" fill="#8A5636" {W(2)}/>
<path d="M0 104 Q64 94 128 104 V130 H0Z" fill="#7DBA4E" {W(2.4)}/>
<ellipse cx="68" cy="68" rx="36" ry="32" fill="#B8814A" {s()}/>
<circle cx="48" cy="56" r="1.8" fill="#8A5A2E"/><circle cx="92" cy="74" r="1.8" fill="#8A5A2E"/><circle cx="84" cy="48" r="1.6" fill="#8A5A2E"/>
<path d="M54 44 L82 52 M70 38 L66 58" stroke="#FFF3C4" stroke-width="6" stroke-linecap="round"/>
<path d="M60 46 Q68 50 74 46 Q74 54 70 58 Q66 54 60 46Z" fill="#FFE066" {W(1.8)}/>
<path d="M32 80 Q30 112 68 112 Q106 112 104 80 Q96 90 86 84 Q78 94 68 86 Q58 94 50 84 Q40 90 32 80Z" fill="#CBD5E0" {s()}/>
<path d="M42 92 L48 98 M90 92 L84 100 M64 100 L70 106" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M60 28 Q56 20 60 14 M74 28 Q78 20 74 12" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
{face(68, 68, d=11, k=0.9)}
'''), "герой: печёная картошка в мятой фольге с тающим кубиком масла | сцена: дымится на загородной лужайке у сосны")


# 9 Tulum (детское кафе, Мытищи) — пиньята-звезда с кисточками, из неё сыплются конфеты
I["cafe-tulum-mytishchi"] = (svg2("#D3F6FB", "#2FB0C4", f'''
<path d="M64 0 V14" {W(2.4)}/>
''' + "".join(f'<path d="M{a} {b} L{x} {y} L{c} {d}Z" fill="{col}" {W(2.4)}/>' for a, b, x, y, c, d, col in [
    (54, 32, 64, 4, 74, 32, "#FF5E8A"), (84, 40, 112, 38, 88, 60, "#FFC93C"), (86, 70, 98, 96, 70, 82, "#7BD66B"),
    (58, 82, 30, 96, 42, 70, "#9B7BFF"), (40, 60, 16, 38, 44, 40, "#FF8C42")]) + f'''
<circle cx="64" cy="56" r="27" fill="#FFE07A" {s()}/>
<path d="M40 46 H88 M38 66 H90" stroke="#FF5E8A" stroke-width="3.4" opacity=".8"/>
{face(64, 56, d=10, k=0.95)}
<path d="M50 82 V96 M58 84 V100 M70 84 V100 M78 82 V96" stroke="#FF5E8A" stroke-width="3" stroke-linecap="round"/>
<path d="M54 83 V98 M74 83 V98" stroke="#5CC8FF" stroke-width="3" stroke-linecap="round"/>
<rect x="30" y="104" width="10" height="7" rx="3" fill="#FF6FA3" {W(1.8)} transform="rotate(20 35 107)"/>
<rect x="60" y="112" width="10" height="7" rx="3" fill="#7BD66B" {W(1.8)}/>
<rect x="88" y="104" width="10" height="7" rx="3" fill="#FFC93C" {W(1.8)} transform="rotate(-25 93 107)"/>
'''), "герой: разноцветная пиньята-звезда с бумажными кисточками | сцена: висит на верёвочке, а из неё сыплются конфеты")


# 10 Insight cafe (Подольск) — ягодная тарталетка мечтает на облачке под звездой-идеей
I["cafe-insight-podolsk"] = (svg2("#B9C3F7", "#4B43A6", f'''
<circle cx="22" cy="40" r="1.6" fill="#fff"/><circle cx="104" cy="58" r="1.4" fill="#fff"/><circle cx="30" cy="70" r="1.2" fill="#fff"/>
<path d="M64 6 L69 18 L82 19 L72 27 L75 40 L64 33 L53 40 L56 27 L46 19 L59 18Z" fill="#FFE066" {W(2.4)}/>
<path d="M44 30 L38 26 M84 30 L90 26 M64 44 V48" stroke="#FFE066" stroke-width="2.6" stroke-linecap="round"/>
<path d="M14 108 Q8 92 24 90 Q26 76 42 80 Q52 68 66 78 Q80 70 88 82 Q106 80 106 94 Q120 96 114 110Z" fill="#fff" {s()}/>
<path d="M34 72 L40 96 H88 L94 72Z" fill="#E7B36A" {s()}/>
<path d="M40 74 L44 92 M52 74 L54 94 M64 74 V94 M76 74 L74 94 M88 74 L84 92" stroke="#C88A3C" stroke-width="2" opacity=".7"/>
<ellipse cx="64" cy="70" rx="32" ry="8" fill="#FFF0D0" {W(2.4)}/>
<circle cx="48" cy="66" r="5" fill="#E8394A" {W(1.8)}/><circle cx="60" cy="62" r="5" fill="#4A5BD6" {W(1.8)}/><circle cx="72" cy="64" r="5" fill="#E8394A" {W(1.8)}/><circle cx="82" cy="68" r="4.5" fill="#4A5BD6" {W(1.8)}/>
{face(64, 82, d=10, k=0.8)}
'''), "герой: тарталетка с малиной и черникой | сцена: мечтает на облачке, над ней загорается звезда-идея")

# 11 Dachniki — ватрушка в кресле-качалке на дачной веранде с пледом
I["cafe-dachniki"] = (svg2("#FFF4E2", "#EDB27E", f'''
<rect x="0" y="104" width="128" height="26" fill="#C98A55" {W(2.4)}/>
<path d="M0 112 H128 M0 120 H128" stroke="#A86C3E" stroke-width="2"/>
<path d="M26 112 Q64 124 102 112" fill="none" stroke="#8A5636" stroke-width="4" stroke-linecap="round"/>
<path d="M26 112 Q64 124 102 112" fill="none" stroke="#B77A45" stroke-width="2.4"/>
<path d="M36 112 V36 Q36 24 48 24 H80 Q92 24 92 36 V112" fill="none" stroke="#8A5636" stroke-width="5" stroke-linejoin="round"/>
<path d="M44 30 V80 M54 28 V80 M64 28 V80 M74 28 V80 M84 30 V80" stroke="#B77A45" stroke-width="3"/>
<circle cx="64" cy="76" r="30" fill="#E2A44F" {s()}/>
<circle cx="64" cy="76" r="19" fill="#FFF8E8" {W(2.6)}/>
{face(64, 74, d=8, k=0.8)}
<path d="M30 96 H98 L94 112 H34Z" fill="#7FB8E8" {W(2.4)}/>
<path d="M40 96 V112 M52 96 V112 M64 96 V112 M76 96 V112 M88 96 V112" stroke="#fff" stroke-width="2" opacity=".7"/>
'''), "герой: ватрушка с творожной серединкой | сцена: качается в кресле-качалке на дачной веранде, укрытая пледом")

# 12 Food Park (ВДНХ) — палочки чуррос в сахаре ныряют в стаканчик горячего шоколада
I["cafe-food-park-vdnh"] = (svg2("#FCEADF", "#C2856A", f'''
<g transform="rotate(-24 60 60)">
<rect x="40" y="10" width="20" height="86" rx="9" fill="#E3A14E" {s()}/>
<path d="M45 16 V90 M50 14 V92 M55 16 V90" stroke="#B9732E" stroke-width="2"/>
<circle cx="44" cy="30" r="1.5" fill="#fff"/><circle cx="56" cy="44" r="1.5" fill="#fff"/><circle cx="46" cy="60" r="1.5" fill="#fff"/><circle cx="54" cy="24" r="1.5" fill="#fff"/>
</g>
<g transform="rotate(14 82 60)">
<rect x="72" y="22" width="18" height="74" rx="8" fill="#EAAE5C" {s()}/>
<path d="M77 28 V90 M81 26 V92 M85 28 V90" stroke="#B9732E" stroke-width="2"/>
<circle cx="76" cy="40" r="1.5" fill="#fff"/><circle cx="86" cy="54" r="1.5" fill="#fff"/>
</g>
<path d="M34 86 H96 L90 118 Q64 126 40 118Z" fill="#FFFFFF" {s()}/>
<ellipse cx="65" cy="86" rx="31" ry="7" fill="#6B3A22" {W(2.6)}/>
<path d="M40 100 H92" stroke="#E8604C" stroke-width="4"/>
{face(46, 52, d=7, k=0.7)}
'''), "герой: палочки чуррос в сахарной пудре | сцена: ныряют в стаканчик с горячим шоколадом")

# 13 Чайхона №1 (Б. Полянка) — кубик халвы с фисташками идёт по канату, балансируя
I["cafe-chaihona1-polyanka"] = (svg2("#DCEEFF", "#4677C8", f'''
<path d="M-4 96 Q64 108 132 96" fill="none" {W(3)}/>
<path d="M12 70 L116 56" stroke="#8A5636" stroke-width="4" stroke-linecap="round"/>
<circle cx="12" cy="70" r="5" fill="#FF6FA3" {W(2)}/><circle cx="116" cy="56" r="5" fill="#FF6FA3" {W(2)}/>
<path d="M36 64 Q30 58 34 52 M92 60 Q98 54 94 48" fill="none" {W(3)}/>
<rect x="38" y="44" width="52" height="50" rx="7" fill="#EBD3A6" {s()}/>
<path d="M40 60 H88 M40 76 H88" stroke="#CDAE76" stroke-width="2.4"/>
''' + "".join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="#7CC36A"/>' for x, y in [(46, 52), (80, 50), (50, 86), (84, 84), (64, 88), (74, 54)]) + f'''
{face(64, 66, d=9, k=0.85)}
<path d="M54 94 L52 102 M74 94 L76 102" {W(3)}/>
{sparkle(110, 28, 6)}{sparkle(20, 30, 4)}
'''), "герой: кубик халвы с фисташками | сцена: балансирует на натянутом канате, раскинув руки")

# 14 Чайхона №1 (Б. Грузинская) — лагман: лапша тянется из пиалы вверх пружинкой
I["cafe-chaihona1-gruzinskaya"] = (svg2("#FFE3D3", "#DF5B42", f'''
<path d="M60 74 C40 64 86 56 64 46 C42 36 88 28 66 18 C52 12 60 4 70 6" fill="none" stroke="#F7E3A5" stroke-width="7" stroke-linecap="round"/>
<path d="M60 74 C40 64 86 56 64 46 C42 36 88 28 66 18 C52 12 60 4 70 6" fill="none" {W(2)} opacity=".5"/>
<path d="M18 72 H110 Q108 112 64 114 Q20 112 18 72Z" fill="#2E6FC2" {s()}/>
<path d="M30 92 Q36 86 42 92 Q48 98 54 92 Q60 86 66 92 Q72 98 78 92 Q84 86 90 92 Q96 98 100 92" fill="none" stroke="#fff" stroke-width="2.4"/>
<ellipse cx="64" cy="72" rx="46" ry="9" fill="#D9542E" {s()}/>
<circle cx="44" cy="70" r="4" fill="#7CC36A"/><circle cx="82" cy="72" r="4" fill="#F5C23E"/><rect x="58" y="66" width="8" height="6" rx="2" fill="#8A4A2E"/>
{face(64, 98, d=12, k=0.85, blush=False)}
'''), "герой: лагман в синей узбекской пиале | сцена: лапша тянется из пиалы высоко вверх пружинкой")

# 15 Лодка — суп в хлебном горшочке плывёт как лодка, гребёт вёслами-гренками
I["cafe-lodka"] = (svg2("#DEEBF7", "#6B8CC6", f'''
<path d="M-4 96 Q16 88 32 96 Q48 104 64 96 Q80 88 96 96 Q112 104 132 96 V130 H-4Z" fill="#5AA7E0" {W(2.4)}/>
<path d="M8 110 Q20 104 32 110 M76 112 Q88 106 100 112" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M30 64 L10 98" stroke="#8A5636" stroke-width="3.4" stroke-linecap="round"/><rect x="4" y="94" width="14" height="10" rx="2" fill="#E3A14E" {W(2)} transform="rotate(30 11 99)"/>
<path d="M98 64 L118 98" stroke="#8A5636" stroke-width="3.4" stroke-linecap="round"/><rect x="110" y="94" width="14" height="10" rx="2" fill="#E3A14E" {W(2)} transform="rotate(-30 117 99)"/>
<path d="M24 58 Q24 100 64 100 Q104 100 104 58Z" fill="#C98340" {s()}/>
<ellipse cx="64" cy="58" rx="40" ry="10" fill="#F08A3C" {s()}/>
<circle cx="52" cy="56" r="3" fill="#fff"/><circle cx="74" cy="58" r="2.4" fill="#7CC36A"/>
<path d="M36 44 Q50 22 82 30 Q96 36 92 48" fill="#E0A458" {s()}/>
<path d="M48 40 L52 34 M64 34 L66 28 M78 38 L82 32" stroke="#9C5B26" stroke-width="2.2" stroke-linecap="round"/>
{face(64, 80, d=11, k=0.9)}
'''), "герой: суп в круглом хлебном горшочке с хлебной крышкой | сцена: плывёт по реке как лодка, гребёт вёслами-гренками")

# 16 Osteria della Piazza Bianca — буррата с листиком базилика сидит на белой мраморной площади у колонны
I["cafe-piazza-bianca"] = (svg2("#F7F4FB", "#B3A8CF", f'''
<path d="M-4 96 L132 96 L132 130 L-4 130Z" fill="#FFFFFF" {W(2.4)}/>
<path d="M-4 108 H132 M20 96 L4 130 M48 96 L40 130 M80 96 L88 130 M108 96 L124 130" stroke="#D9D2E8" stroke-width="2"/>
<rect x="96" y="30" width="16" height="66" fill="#F3EFF9" {W(2.4)}/><rect x="92" y="24" width="24" height="8" rx="2" fill="#fff" {W(2.4)}/>
<path d="M100 36 V92 M104 36 V92 M108 36 V92" stroke="#D9D2E8" stroke-width="1.6"/>
<path d="M58 40 Q50 30 56 24 Q64 30 64 38 Q64 30 72 24 Q78 30 70 40Z" fill="#FFFFFF" {W(2.4)}/>
<path d="M60 40 Q64 44 68 40" fill="none" {W(2.4)}/>
<path d="M30 74 Q30 42 64 40 Q94 42 94 74 Q94 102 64 102 Q30 102 30 74Z" fill="#FFFFFF" {s()}/>
<path d="M38 66 Q44 52 58 48" fill="none" stroke="#EDE6F6" stroke-width="4" stroke-linecap="round"/>
<path d="M70 50 Q84 40 92 52 Q82 60 70 50Z" fill="#46A748" {W(2)}/>
<ellipse cx="50" cy="94" rx="8" ry="3" fill="#E8C64A" opacity=".8"/>
{face(62, 74, d=10, k=0.95)}
'''), "герой: шарик бурраты с узелком и листиком базилика | сцена: сидит на белой мраморной площади у колонны")

# 17 Jesstaurant (Лапино) — блинчик-конвертик с печатью-ягодкой летит как письмо
I["cafe-jesstaurant"] = (svg2("#FFE6EA", "#E25F79", f'''
<path d="M10 40 H28 M6 56 H24 M12 72 H26" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
<path d="M34 36 H104 V96 H34Z" fill="#F2C474" {s()} transform="rotate(-8 69 66)"/>
<g transform="rotate(-8 69 66)">
<path d="M34 36 L69 70 L104 36" fill="#EBB05A" {s()}/>
<path d="M34 96 L60 66 M104 96 L78 66" fill="none" {W(2.4)}/>
<circle cx="46" cy="86" r="1.6" fill="#B9732E"/><circle cx="92" cy="84" r="1.6" fill="#B9732E"/><circle cx="70" cy="90" r="1.6" fill="#B9732E"/>
</g>
<circle cx="70" cy="64" r="8" fill="#D8233F" {W(2.4)}/><path d="M70 56 Q72 50 78 50" fill="none" stroke="#3E9C3A" stroke-width="2.6" stroke-linecap="round"/>
{face(70, 82, d=12, k=0.85)}
<path d="M104 26 Q108 20 112 26 Q116 20 120 26 Q120 32 112 38 Q104 32 104 26Z" fill="#FF6F8E" {W(2)}/>
'''), "герой: блинчик-конвертик с печатью из ягодки | сцена: летит по небу как письмо, за ним сердечко")


if __name__ == "__main__":
    reg = os.path.join(ROOT, "icons-src", "subjects.txt")
    have = {l.split(" — ", 1)[0] for l in open(reg, encoding="utf-8") if " — " in l}
    add = []
    for pid, (svg_, subj) in I.items():
        open(os.path.join(ROOT, "icons-src", pid + ".svg"), "w").write(svg_)
        if pid not in have:
            add.append(f"{pid} — {subj}\n")
    if add:
        txt = open(reg, encoding="utf-8").read()
        if not txt.endswith("\n"):
            txt += "\n"
        open(reg, "w", encoding="utf-8").write(txt + "".join(add))
    print("иконок:", len(I), "новых строк реестра:", len(add))
