"""Робот «художник», 06.11 ~21:30 UTC (второй запуск, по просьбе Вадима — сначала бассейны и кафе).
40 иконок из auto/icon-repeats.json, каждая придумана и нарисована отдельно, вручную:
свой герой, своя сцена, своя палитра фона. Запуск из корня: python3 tools/icons_artist_1106_2130.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT

I = {}

# ---------- КАФЕ ----------

I["cafe-prokhinkali-botanika"] = ("хинкали с листочком на хвостике", "растёт в цветочном горшке на подоконнике, как кактус", ("#EFFFF0", "#58B878"), f'''
<rect x="8" y="104" width="112" height="10" rx="3" fill="#fff" {W(2.6)}/>
<path d="M36 80 H92 L86 106 H42Z" fill="#D9733A" {W(3)}/><rect x="32" y="74" width="64" height="10" rx="3" fill="#E88A4A" {W(2.6)}/>
<path d="M30 76 Q30 40 64 36 Q98 40 98 76Z" fill="#FFF6E6" {W(3)}/>
<path d="M40 50 Q52 44 56 38 M88 50 Q76 44 72 38 M64 36 V44" fill="none" stroke="#D8C8A8" stroke-width="2.4"/>
<path d="M58 36 Q64 24 70 36" fill="#FFF6E6" {W(2.6)}/>
<path d="M64 26 Q66 14 78 12 Q76 24 64 26Z" fill="#6CC24A" {W(2.2)}/>
{eye(54, 60, .6)}{eye(74, 60, .6)}{smile(64, 66, 4, .7)}{blush(48, 67, .6)}{blush(80, 67, .6)}''')

I["cafe-largo-leninsky"] = ("квадратик тирамису с какао-шапочкой", "прыгает по классикам, расчерченным мелом", ("#F5EDE4", "#A88468"), f'''
<path d="M14 120 L30 84 H98 L114 120Z" fill="#8C8C9C"/>
<path d="M30 84 L22 102 H52 L56 84 M56 84 L52 102 H76 L72 84 M72 84 L76 102 H106 L98 84 M22 102 L14 120 H50 L52 102 M76 102 L78 120 H114 L106 102" fill="none" stroke="#fff" stroke-width="2.4"/>
<text x="34" y="98" font-family="Arial" font-size="11" font-weight="bold" fill="#fff">1</text><text x="84" y="98" font-family="Arial" font-size="11" font-weight="bold" fill="#fff">2</text>
<path d="M60 70 L56 84 M72 70 L80 80" {W(3.4)}/>
<rect x="40" y="26" width="48" height="46" rx="5" fill="#FFF4DC" {W(3)}/>
<path d="M40 42 H88 M40 56 H88" stroke="#8A5A36" stroke-width="5"/>
<rect x="40" y="26" width="48" height="10" rx="5" fill="#6A3E22" {W(2.6)}/>
<g fill="#4A2A14"><circle cx="48" cy="30" r="1.4"/><circle cx="60" cy="32" r="1.4"/><circle cx="74" cy="30" r="1.4"/><circle cx="82" cy="33" r="1.4"/></g>
{eye(56, 48, .5)}{eye(72, 48, .5)}<path d="M60 62 Q64 66 68 62" fill="#E8554A" {W(1.8)}/>
<path d="M40 48 L26 36 M88 48 L102 36" {W(3)}/>''')

I["cafe-tapchan-leningradskoe"] = ("нават — сахарные кристаллы на палочке", "стоит вместо ложки в пиале чая и сверкает", ("#E8F7FF", "#4CA0C8"), f'''
<path d="M24 82 Q24 118 64 118 Q104 118 104 82Z" fill="#fff" {W(3)}/>
<path d="M28 92 H100" stroke="#2E5BC8" stroke-width="4"/><path d="M34 104 l6 -4 l6 4 M58 106 l6 -4 l6 4 M82 104 l6 -4 l6 4" fill="none" stroke="#2E5BC8" stroke-width="2.4"/>
<ellipse cx="64" cy="82" rx="40" ry="8" fill="#D88A3A" {W(3)}/>
<path d="M64 84 V20" stroke="#B9773F" stroke-width="4"/>
<path d="M50 30 L60 22 L72 26 L78 38 L74 52 L80 62 L70 72 L58 70 L48 60 L52 46 L46 38Z" fill="#FFE9A8" {W(2.8)}/>
<path d="M60 22 L64 40 L78 38 M52 46 L64 40 L74 52 M48 60 L64 56 L70 72" fill="none" stroke="#F0C060" stroke-width="2"/>
{eye(58, 46, .5)}{eye(70, 46, .5)}{smile(64, 52, 3, .6)}
{sparkle(36, 30, 5)}{sparkle(94, 22, 4)}{sparkle(98, 56, 3, "#FFE27A")}''')

I["cafe-yan-primus-yugo-zapadnaya"] = ("трдельник — чешская трубочка-спираль в сахаре", "крутится на вертеле над угольками", ("#FFF0E0", "#C86A2A"), f'''
<path d="M8 74 H120" stroke="#6A6A7A" stroke-width="4" stroke-linecap="round"/>
<path d="M16 74 V112 M112 74 V112" {W(4)}/>
<path d="M30 54 Q30 46 40 46 H88 Q98 46 98 54 V94 Q98 102 88 102 H40 Q30 102 30 94Z" fill="#D88A3A" {W(3)}/>
<path d="M30 58 L98 50 M30 72 L98 64 M30 86 L98 78 M30 100 L98 92" stroke="#A85A1E" stroke-width="3"/>
<g fill="#fff"><circle cx="40" cy="64" r="1.4"/><circle cx="56" cy="58" r="1.4"/><circle cx="84" cy="70" r="1.4"/><circle cx="46" cy="90" r="1.4"/><circle cx="76" cy="88" r="1.4"/><circle cx="90" cy="58" r="1.4"/></g>
{eye(54, 72, .6)}{eye(74, 72, .6)}{smile(64, 80, 4, .7)}{blush(48, 82, .6)}{blush(80, 82, .6)}
<path d="M30 118 Q40 108 50 118 Q60 106 70 118 Q80 108 90 118Z" fill="#FF6A2A" {W(2.2)}/>
<path d="M60 30 Q56 22 60 16 M70 30 Q66 22 70 16" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

I["cafe-acha-chacha"] = ("глиняный горшочек лобио", "пыхтит паром, крышка весело подпрыгивает", ("#FBEFFF", "#B866B0"), f'''
<path d="M30 64 Q22 106 64 112 Q106 106 98 64Z" fill="#C8643A" {W(3)}/>
<path d="M36 80 Q64 88 92 80" fill="none" stroke="#E8945A" stroke-width="3"/>
<rect x="26" y="58" width="76" height="10" rx="5" fill="#B4542E" {W(2.6)}/>
<g transform="rotate(-12 64 40)"><path d="M34 46 Q64 30 94 46Z" fill="#B4542E" {W(2.8)}/><circle cx="64" cy="34" r="5" fill="#E8945A" {W(2.2)}/></g>
<g fill="#7A2A2A"><ellipse cx="44" cy="60" rx="4" ry="3"/><ellipse cx="56" cy="58" rx="4" ry="3"/><ellipse cx="72" cy="58" rx="4" ry="3"/><ellipse cx="84" cy="60" rx="4" ry="3"/></g>
{eye(54, 88, .6)}{eye(74, 88, .6)}<ellipse cx="64" cy="98" rx="4" ry="3.4" fill="#E8304A" {W(1.8)}/>
<path d="M24 34 Q18 24 26 16 M104 30 Q110 20 102 12" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M44 22 l-4 -6 M86 20 l4 -6" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

I["cafe-shato-manavi"] = ("фиолетовый пеламуши с орешками", "в короне из грецких орехов на праздничной подставке", ("#F6F0FF", "#7A5AB8"), f'''
<path d="M30 104 H98 L88 112 H40Z" fill="#fff" {W(2.6)}/><path d="M60 112 V122 H68 V112" fill="#fff" {W(2.4)}/>
<path d="M36 102 Q30 60 64 56 Q98 60 92 102Z" fill="#8A3AA8" {W(3)}/>
<path d="M40 72 Q64 80 88 72" fill="none" stroke="#B060D0" stroke-width="3"/>
<path d="M42 58 L44 40 Q50 36 52 44 L56 52 L60 36 Q64 30 68 36 L72 52 L76 44 Q78 36 84 40 L86 58Z" fill="#C89A5A" {W(2.6)}/>
<path d="M48 44 Q50 48 46 50 M62 38 Q66 42 62 46 M80 44 Q78 48 82 50" fill="none" stroke="#8F5A2C" stroke-width="1.8"/>
{eye(54, 82, .6)}{eye(74, 82, .6)}{smile(64, 89, 4, .7)}{blush(46, 90, .6)}{blush(82, 90, .6)}
{sparkle(22, 40, 5)}{sparkle(108, 54, 4)}''')

I["cafe-thali-fusion"] = ("индийский поднос-тхали с мисочками", "мисочки-персонажи сидят по кругу вокруг лепёшки", ("#FFF7E0", "#E89A2A"), f'''
<circle cx="64" cy="66" r="50" fill="#D8DCE6" {W(3)}/><circle cx="64" cy="66" r="44" fill="none" stroke="#fff" stroke-width="2"/>
<circle cx="64" cy="66" r="15" fill="#F2D08A" {W(2.4)}/><g fill="#C88A3A"><circle cx="60" cy="62" r="1.8"/><circle cx="68" cy="66" r="1.8"/><circle cx="62" cy="72" r="1.8"/></g>
<circle cx="64" cy="32" r="12" fill="#F2A22A" {W(2.4)}/>{eye(60, 32, .35)}{eye(68, 32, .35)}
<circle cx="96" cy="54" r="12" fill="#7CC24A" {W(2.4)}/>{eye(92, 54, .35)}{eye(100, 54, .35)}
<circle cx="88" cy="92" r="12" fill="#E8443A" {W(2.4)}/>{eye(84, 92, .35)}{eye(92, 92, .35)}
<circle cx="40" cy="92" r="12" fill="#FFF4E0" {W(2.4)}/>{eye(36, 92, .35)}{eye(44, 92, .35)}
<circle cx="32" cy="54" r="12" fill="#B87A3A" {W(2.4)}/>{eye(28, 54, .35)}{eye(36, 54, .35)}
<path d="M60 37 Q64 40 68 37 M92 59 Q96 62 100 59 M84 97 Q88 100 92 97 M36 97 Q40 100 44 97 M28 59 Q32 62 36 59" fill="none" {W(1.6)}/>''')

I["cafe-uryuk-vdnh"] = ("румяная самса-треугольник с кунжутом", "катается в кабинке колеса обозрения «Солнце Москвы»", ("#E2F2FF", "#5A8AD8"), f'''
<circle cx="64" cy="64" r="58" fill="none" stroke="#fff" stroke-width="3"/>
<path d="M64 64 L64 6 M64 64 L114 36 M64 64 L114 92 M64 64 L14 36 M64 64 L14 92" stroke="#fff" stroke-width="2"/>
<circle cx="64" cy="64" r="6" fill="#FFC93C" {W(2)}/>
<path d="M64 64 L64 74" {W(3)}/>
<rect x="36" y="72" width="56" height="44" rx="10" fill="#E8304A" {W(3)}/><rect x="42" y="78" width="44" height="22" rx="4" fill="#BFE6FF" {W(2)}/>
<path d="M46 98 L64 74 L82 98Z" fill="#E8A040" {W(2.6)}/>
<g fill="#FFF4D6"><circle cx="60" cy="84" r="1.2"/><circle cx="66" cy="88" r="1.2"/><circle cx="58" cy="92" r="1.2"/></g>
{eye(60, 90, .4)}{eye(68, 90, .4)}
<path d="M58 98 L52 90 M70 98 L76 90" {W(2.4)}/>
<circle cx="14" cy="36" r="5" fill="#FFC93C" {W(1.8)}/><circle cx="114" cy="36" r="5" fill="#7CD26E" {W(1.8)}/>''')

I["cafe-ilpatio-zelenopark"] = ("фокачча с веточкой розмарина", "качается в гамаке между двумя деревьями", ("#E8FFE8", "#3E9A4E"), f'''
<path d="M14 120 V40 M114 120 V40" stroke="#8F5A2C" stroke-width="7"/>
<circle cx="14" cy="34" r="16" fill="#4CAF50" {W(2.4)}/><circle cx="114" cy="34" r="16" fill="#4CAF50" {W(2.4)}/>
<path d="M18 62 Q64 104 110 62" fill="none" stroke="#FFF" stroke-width="3"/>
<path d="M18 62 Q64 112 110 62 L104 66 Q64 100 24 66Z" fill="#FF8FA8" {W(2.6)}/>
<path d="M34 68 Q34 54 46 54 H84 Q96 54 96 68 Q96 82 84 82 H46 Q34 82 34 68Z" fill="#F2C86A" {W(3)}/>
<g fill="#D89A3A"><circle cx="44" cy="62" r="2"/><circle cx="56" cy="60" r="2"/><circle cx="84" cy="62" r="2"/><circle cx="90" cy="72" r="2"/></g>
<path d="M60 58 L76 52 M64 56 l2 -4 M70 54 l2 -4 M68 56 l4 2" stroke="#3E8A2E" stroke-width="2.2" stroke-linecap="round"/>
<path d="M50 68 Q53 65 56 68 M70 68 Q73 65 76 68" fill="none" {W(2)}/>{smile(63, 74, 3, .6)}''')

I["cafe-ilpatio-fashion-house"] = ("макаронина-бантик фарфалле", "прихорашивается перед большим зеркалом в бутике", ("#FFEFF8", "#D85A9A"), f'''
<rect x="66" y="16" width="46" height="96" rx="20" fill="#C8ECFF" {W(3)}/>
<path d="M76 30 L96 52 M82 26 L104 50" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M64 112 H112" {W(4)}/>
<path d="M16 50 Q16 36 28 42 L42 56 L56 42 Q68 36 68 50 V82 Q68 96 56 90 L42 76 L28 90 Q16 96 16 82Z" fill="#F6D27A" {W(3)}/>
<path d="M22 50 L26 82 M60 50 L56 82" stroke="#E0A840" stroke-width="2.4"/>
<rect x="36" y="56" width="12" height="20" rx="5" fill="#F0BE5A" {W(2.4)}/>
{eye(38, 64, .4)}{eye(46, 64, .4)}<path d="M38 70 Q42 73 46 70" fill="none" {W(1.6)}/>
<path d="M88 60 Q88 52 94 56 L98 60 L102 56 Q108 52 108 60 V70 Q108 78 102 74 L98 70 L94 74 Q88 78 88 70Z" fill="#F6D27A" opacity=".7" {W(1.8)}/>
{sparkle(24, 24, 4, "#fff")}{sparkle(56, 108, 3)}''')

I["cafe-korchma-krasnokazarmennaya"] = ("пышные пампушки", "стоят друг на друге пирамидкой, как цирковые акробаты", ("#FFF6E0", "#D8A030"), f'''
<path d="M10 118 H118" stroke="#8F5A2C" stroke-width="5"/>
<circle cx="42" cy="98" r="18" fill="#E8B060" {W(3)}/>{eye(36, 96, .45)}{eye(48, 96, .45)}{smile(42, 103, 3, .6)}
<circle cx="86" cy="98" r="18" fill="#E8B060" {W(3)}/>{eye(80, 96, .45)}{eye(92, 96, .45)}{smile(86, 103, 3, .6)}
<circle cx="64" cy="64" r="18" fill="#F0C070" {W(3)}/>{eye(58, 62, .45)}{eye(70, 62, .45)}{smile(64, 69, 3, .6)}
<circle cx="64" cy="30" r="14" fill="#F6CC86" {W(3)}/>{eye(59, 29, .4)}{eye(69, 29, .4)}<path d="M60 35 Q64 38 68 35" fill="#E8554A" {W(1.6)}/>
<path d="M50 30 L36 20 M78 30 L92 20" {W(3)}/>
<g fill="#3E8A2E"><circle cx="38" cy="84" r="1.6"/><circle cx="90" cy="84" r="1.6"/><circle cx="60" cy="50" r="1.6"/><circle cx="66" cy="20" r="1.4"/></g>
{sparkle(22, 30, 5)}{sparkle(108, 36, 4)}''')

I["cafe-yakitoriya-donskogo"] = ("жёлтый омлет-тамагояки с полоской нори", "поднимает штангу из двух роллов", ("#E8FFFB", "#2EA898"), f'''
<path d="M10 114 H118" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
<path d="M18 46 H110" stroke="#5A5A6A" stroke-width="5" stroke-linecap="round"/>
<circle cx="20" cy="46" r="14" fill="#fff" {W(2.8)}/><circle cx="20" cy="46" r="10" fill="#2B3A2A"/><circle cx="20" cy="46" r="5" fill="#FF7A5A"/>
<circle cx="108" cy="46" r="14" fill="#fff" {W(2.8)}/><circle cx="108" cy="46" r="10" fill="#2B3A2A"/><circle cx="108" cy="46" r="5" fill="#7CD26E"/>
<path d="M44 74 L36 48 M84 74 L92 48" {W(4)}/>
<rect x="38" y="64" width="52" height="40" rx="8" fill="#FFD84A" {W(3)}/>
<path d="M38 76 H90 M38 88 H90" stroke="#F0B020" stroke-width="2"/>
<rect x="58" y="64" width="12" height="40" fill="#1F3A2A"/>
{eye(48, 80, .5)}{eye(80, 80, .5)}<path d="M46 92 Q50 88 54 92 M74 92 Q78 88 82 92" fill="none" {W(1.8)}/>
<path d="M50 104 V114 M78 104 V114" {W(4)}/>''')

I["cafe-mimi-vidnoe"] = ("панна-котта с ягодным соусом", "съезжает на санках-ложечке с горки взбитых сливок", ("#FFF0F4", "#E8708A"), f'''
<path d="M0 112 Q20 50 60 40 Q100 34 128 60 V128 H0Z" fill="#fff" {W(2.6)}/>
<path d="M30 70 Q40 60 50 66 M80 50 Q90 44 100 52" fill="none" stroke="#F0E0E8" stroke-width="3"/>
<g transform="rotate(-24 64 80)">
<path d="M36 100 Q30 108 40 108 H92 Q100 108 96 100" fill="none" stroke="#B8C0D0" stroke-width="4" stroke-linecap="round"/>
<path d="M42 100 L48 64 H84 L90 100Z" fill="#FFF8EC" {W(3)}/>
<path d="M48 64 H84 L82 76 Q74 70 66 78 Q58 70 50 76Z" fill="#D8304A" {W(2.4)}/>
<circle cx="66" cy="60" r="5" fill="#B8203A" {W(1.8)}/>
{eye(58, 86, .5)}{eye(74, 86, .5)}<path d="M62 93 Q66 96 70 93" fill="#E8554A" {W(1.6)}/>
</g>
<path d="M20 30 l8 4 M14 44 l8 0" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

I["cafe-semeynoe-korolev"] = ("котлетка-космонавт в шлеме", "парит в невесомости рядом с облачком пюре", ("#283068", "#0E1236"), f'''
<circle cx="64" cy="62" r="30" fill="#BFE6FF" fill-opacity=".35" {W(3)}/>
<path d="M38 66 Q38 46 64 46 Q90 46 90 66 Q90 84 64 84 Q38 84 38 66Z" fill="#9A5A2E" {W(3)}/>
<g fill="#6A3A1A"><circle cx="50" cy="56" r="1.8"/><circle cx="76" cy="58" r="1.8"/><circle cx="58" cy="78" r="1.8"/></g>
{eye(56, 66, .55)}{eye(72, 66, .55)}{smile(64, 73, 3.5, .65)}
<path d="M44 40 Q52 34 60 38" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<rect x="50" y="90" width="28" height="10" rx="4" fill="#fff" {W(2.4)}/>
<path d="M92 96 Q90 84 100 86 Q104 76 114 82 Q124 84 120 94 Q122 104 110 102 Q100 106 96 100 Q88 102 92 96Z" fill="#FFF4C8" {W(2.4)}/>
{sparkle(20, 24, 4, "#FFE27A")}{sparkle(108, 28, 3)}{sparkle(20, 96, 3)}<circle cx="100" cy="50" r="2" fill="#fff"/><circle cx="28" cy="60" r="1.6" fill="#fff"/>''')

I["cafe-kitchen-krylatskoe"] = ("блинчик-гребец", "гребёт веслом в байдарке по гребному каналу", ("#E0F6FF", "#3A8EC8"), f'''
<path d="M0 86 Q32 80 64 86 T128 86 V128 H0Z" fill="#3A9AE0"/>
<path d="M10 100 Q30 96 50 100 M74 108 Q94 104 114 108" fill="none" stroke="#fff" stroke-width="2.6"/>
<path d="M8 84 Q64 98 120 84 Q110 94 64 96 Q18 94 8 84Z" fill="#FFC93C" {W(3)}/>
<path d="M30 30 L100 104" stroke="#8F5A2C" stroke-width="4" stroke-linecap="round"/>
<path d="M22 22 L36 30 L30 40 L18 34Z" fill="#E8304A" {W(2)}/><path d="M96 98 L108 108 L102 116 L92 106Z" fill="#E8304A" {W(2)}/>
<circle cx="62" cy="60" r="22" fill="#F2C266" {W(3)}/><circle cx="62" cy="60" r="14" fill="none" stroke="#E0A040" stroke-width="2"/>
{eye(55, 58, .55)}{eye(69, 58, .55)}{smile(62, 66, 3.5, .65)}
<path d="M44 66 L52 74 M80 66 L74 74" {W(3)}/>
<path d="M44 40 Q62 30 80 40" fill="none" stroke="#FFF" stroke-width="5"/>''')

I["cafe-botanika-zheleznodorozhny"] = ("баночка зелёного смузи с трубочкой", "поливает из лейки росток на грядке", ("#F2FFE6", "#88C040"), f'''
<path d="M0 104 Q64 96 128 104 V128 H0Z" fill="#8F5A2C"/>
<path d="M98 104 V86" stroke="#3E8A2E" stroke-width="3"/><path d="M98 92 Q90 82 84 88 Q90 96 98 92Z M98 88 Q106 78 112 84 Q106 92 98 88Z" fill="#6CC24A" {W(1.8)}/>
<path d="M30 44 H70 L66 104 H34Z" fill="#7CC24A" fill-opacity=".9" {W(3)}/>
<rect x="28" y="38" width="44" height="8" rx="3" fill="#fff" {W(2.4)}/>
<path d="M56 38 L66 14" stroke="#FF6F91" stroke-width="5" stroke-linecap="round"/>
<path d="M36 60 Q50 54 64 60" fill="none" stroke="#B8E890" stroke-width="3"/>
{eye(43, 72, .55)}{eye(57, 72, .55)}{smile(50, 79, 3.5, .65)}
<path d="M66 72 L80 66 L94 58 L100 64 L88 76 L74 82Z" fill="#5CB7F2" {W(2.4)}/>
<path d="M100 64 L106 70 M96 68 L100 76 M102 62 L110 66" stroke="#9AD6FF" stroke-width="2" stroke-linecap="round"/>''')

I["cafe-hatimaki-shcherbinka"] = ("пухлая булочка бао", "выглядывает из бамбуковой корзинки-пароварки, пар облачками", ("#FFF8EE", "#D0A070"), f'''
<rect x="18" y="74" width="92" height="38" rx="6" fill="#E0B870" {W(3)}/>
<path d="M18 86 H110 M18 100 H110" stroke="#B88A40" stroke-width="2.6"/>
<path d="M30 76 Q28 46 64 44 Q100 46 98 76Z" fill="#FFFDF6" {W(3)}/>
<path d="M54 46 Q64 38 74 46 M60 44 Q64 40 68 44" fill="none" stroke="#E8D8C0" stroke-width="2.2"/>
{eye(54, 62, .55)}{eye(74, 62, .55)}{smile(64, 69, 3.5, .65)}{blush(46, 69, .6)}{blush(82, 69, .6)}
<path d="M18 74 Q14 60 22 52 Q16 40 28 36 M110 74 Q114 60 106 52 Q112 40 100 36" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M58 30 Q54 20 60 14 M70 30 Q66 20 72 14" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>''')

I["cafe-dyushes-butovo"] = ("грушевый тарт с дольками веером", "стоит под снегопадом сахарной пудры из ситечка", ("#F6FFE0", "#A8C83A"), f'''
<ellipse cx="64" cy="104" rx="50" ry="10" fill="#fff" {W(2.6)}/>
<path d="M18 86 Q18 102 64 102 Q110 102 110 86 V80 H18Z" fill="#D89A4A" {W(3)}/>
<ellipse cx="64" cy="80" rx="46" ry="14" fill="#F2DC8A" {W(3)}/>
<path d="M64 80 Q40 70 28 78 M64 80 Q46 66 40 70 M64 80 Q58 66 54 68 M64 80 Q72 66 76 68 M64 80 Q84 66 90 70 M64 80 Q92 72 100 78" fill="none" stroke="#C8B040" stroke-width="2.6"/>
<circle cx="64" cy="80" r="5" fill="#B8203A" {W(1.6)}/>
{eye(52, 92, .45)}{eye(76, 92, .45)}<path d="M60 96 Q64 99 68 96" fill="none" {W(1.8)}/>
<path d="M88 14 Q74 14 74 28 Q74 40 88 40 Q102 40 102 28 Q102 14 88 14Z" fill="#E8E8F0" {W(2.4)}/>
<path d="M100 22 L118 10" stroke="#8F5A2C" stroke-width="4" stroke-linecap="round"/>
<path d="M78 24 H98 M80 32 H96 M84 18 V38 M92 18 V38" stroke="#B8B8C8" stroke-width="1.4"/>
<g fill="#fff"><circle cx="80" cy="48" r="2"/><circle cx="90" cy="52" r="2"/><circle cx="84" cy="60" r="2"/><circle cx="74" cy="56" r="1.6"/><circle cx="96" cy="62" r="1.6"/></g>''')

I["cafe-shore-house-village"] = ("рыбные палочки-тройняшки", "плывут на плоту из тоста по озеру", ("#E0FFFA", "#3AB8B0"), f'''
<path d="M0 82 Q32 76 64 82 T128 82 V128 H0Z" fill="#4AB0E0"/>
<path d="M14 100 Q30 96 46 100 M80 110 Q96 106 112 110" fill="none" stroke="#fff" stroke-width="2.6"/>
<path d="M18 84 H110 L104 96 H24Z" fill="#E8B060" {W(3)}/><path d="M22 88 H106" stroke="#F6D49A" stroke-width="3"/>
<rect x="28" y="52" width="16" height="34" rx="5" fill="#E8902A" {W(2.6)}/>{eye(33, 64, .35)}{eye(39, 64, .35)}
<rect x="56" y="44" width="16" height="42" rx="5" fill="#F0A030" {W(2.6)}/>{eye(61, 58, .4)}{eye(67, 58, .4)}<path d="M61 66 Q64 69 67 66" fill="none" {W(1.6)}/>
<rect x="84" y="56" width="16" height="30" rx="5" fill="#E8902A" {W(2.6)}/>{eye(89, 66, .35)}{eye(95, 66, .35)}
<g fill="#B8601E"><circle cx="32" cy="76" r="1.2"/><circle cx="40" cy="80" r="1.2"/><circle cx="60" cy="76" r="1.2"/><circle cx="68" cy="80" r="1.2"/><circle cx="90" cy="78" r="1.2"/></g>
<path d="M64 44 V22" {W(2.6)}/><path d="M64 22 L84 28 L64 34Z" fill="#E8304A" {W(2)}/>''')

I["cafe-niyama-mytishchi"] = ("нигири с лососем верхом на красном ките", "кит пускает фонтанчик, нигири держится за него ручками", ("#EAF4FF", "#2E6AB8"), f'''
<path d="M0 100 Q32 94 64 100 T128 100 V128 H0Z" fill="#3A80D0"/>
<path d="M14 92 Q14 66 52 64 Q92 62 100 80 L116 66 Q120 84 112 92 Q104 104 56 104 Q14 104 14 92Z" fill="#E8443A" {W(3)}/>
<path d="M20 94 Q56 102 98 92" fill="none" stroke="#FFB0A8" stroke-width="3"/>
{eye(28, 84, .55)}<path d="M18 92 Q24 96 30 94" fill="none" {W(2)}/>
<path d="M40 60 Q36 46 40 36 M40 46 Q32 38 26 40 M40 46 Q48 38 54 40" fill="none" stroke="#9AD6FF" stroke-width="3" stroke-linecap="round"/>
<rect x="50" y="48" width="38" height="18" rx="8" fill="#fff" {W(2.6)}/>
<path d="M50 52 Q50 38 70 38 Q90 38 88 52Z" fill="#FF8A5A" {W(2.6)}/><path d="M58 42 L62 50 M68 40 L72 50 M78 42 L80 50" stroke="#FFC8B0" stroke-width="2"/>
{eye(64, 58, .4)}{eye(74, 58, .4)}''')

I["cafe-caramelle-village"] = ("крем-брюле в маленькой формочке", "ложечка стучит по хрустящей карамельной корочке — трещинки и искры", ("#FFF6E8", "#C88A4A"), f'''
<ellipse cx="64" cy="104" rx="46" ry="10" fill="#fff" {W(2.6)}/>
<path d="M24 70 V96 Q24 106 64 106 Q104 106 104 96 V70Z" fill="#fff" {W(3)}/>
<path d="M28 76 V98 M38 78 V102 M50 80 V104 M64 80 V106 M78 80 V104 M90 78 V102 M100 76 V98" stroke="#E0E4EE" stroke-width="2"/>
<ellipse cx="64" cy="70" rx="40" ry="12" fill="#D8862A" {W(3)}/>
<path d="M52 66 L60 70 L56 76 M60 70 L70 66 M60 70 L68 76" fill="none" stroke="#FFE0A0" stroke-width="2"/>
<path d="M78 18 L64 62" stroke="#B8C0D0" stroke-width="5" stroke-linecap="round"/><ellipse cx="62" cy="64" rx="6" ry="3.4" fill="#B8C0D0" {W(1.6)}/>
{eye(52, 90, .5)}{eye(76, 90, .5)}<path d="M60 94 Q64 98 68 94" fill="#E8554A" {W(1.6)}/>
{sparkle(40, 50, 5, "#FFE27A")}{sparkle(90, 48, 4, "#FFE27A")}''')

I["cafe-ilya-muromets-leningradsky"] = ("курник в форме богатырского шлема", "стоит на круглом щите-блюде", ("#FFF2E6", "#B85A3A"), f'''
<ellipse cx="64" cy="102" rx="54" ry="16" fill="#C83A2A" {W(3)}/><ellipse cx="64" cy="100" rx="42" ry="10" fill="#E8A040" {W(2)}/>
<path d="M28 98 Q24 52 64 40 Q104 52 100 98Z" fill="#E8A040" {W(3)}/>
<path d="M64 40 V14" {W(3)}/><circle cx="64" cy="14" r="4" fill="#FFC93C" {W(2)}/>
<path d="M40 70 Q64 60 88 70 M34 84 Q64 74 94 84" fill="none" stroke="#C07A22" stroke-width="2.6"/>
<path d="M60 52 Q64 46 68 52 M54 60 l4 -4 M74 60 l-4 -4" fill="none" stroke="#C07A22" stroke-width="2"/>
<path d="M58 72 V96" stroke="#C07A22" stroke-width="4"/>
{eye(48, 84, .5)}{eye(80, 84, .5)}<path d="M60 96 Q64 99 68 96" fill="none" {W(1.6)}/>''')

I["cafe-osteria-paveletskaya"] = ("кальцоне-полумесяц", "выглядывает из чемодана на вокзале, рядом билетик", ("#F0F4FF", "#5A70C8"), f'''
<rect x="18" y="62" width="92" height="52" rx="8" fill="#B87A3A" {W(3)}/>
<path d="M18 80 H110" stroke="#8F5A2C" stroke-width="3"/>
<path d="M50 62 V54 Q50 48 56 48 H72 Q78 48 78 54 V62" fill="none" {W(3)}/>
<rect x="28" y="92" width="18" height="12" fill="#FFE27A" {W(2)}/><rect x="86" y="90" width="14" height="14" rx="7" fill="#7CD26E" {W(2)}/>
<path d="M28 70 Q28 30 64 28 Q100 30 100 70Z" fill="#F2BE6A" {W(3)}/>
<path d="M30 68 Q34 62 38 68 Q42 62 46 68 Q50 62 54 68 Q58 62 62 68 Q66 62 70 68 Q74 62 78 68 Q82 62 86 68 Q90 62 94 68 Q98 62 100 68" fill="none" stroke="#C88A3A" stroke-width="2.4"/>
{eye(54, 48, .55)}{eye(74, 48, .55)}{smile(64, 55, 3.5, .65)}
<rect x="96" y="14" width="26" height="14" rx="2" fill="#fff" transform="rotate(14 109 21)" {W(2)}/>''')

I["cafe-vinovicino"] = ("квадратик лазаньи со слоями", "стоит на руках вверх тормашками на тарелке", ("#FFF1EC", "#D8603A"), f'''
<ellipse cx="64" cy="110" rx="52" ry="10" fill="#fff" {W(2.6)}/>
<path d="M50 104 L46 92 M78 104 L82 92" {W(3.4)}/>
<rect x="34" y="34" width="60" height="58" rx="5" fill="#F6D27A" {W(3)}/>
<path d="M34 46 H94" stroke="#D84A2A" stroke-width="6"/><path d="M34 60 H94" stroke="#FFF8E0" stroke-width="5"/>
<path d="M34 74 H94" stroke="#D84A2A" stroke-width="6"/>
<path d="M34 86 Q44 92 54 86 Q64 92 74 86 Q84 92 94 86 V92 H34Z" fill="#E8A040" {W(2)}/>
{eye(54, 66, .55)}{eye(74, 66, .55)}<path d="M58 56 Q64 52 70 56" fill="none" {W(2)}/>
<path d="M50 34 L44 16 M78 34 L84 16" {W(3.4)}/><ellipse cx="44" cy="14" rx="5" ry="3" fill="#FF6F91" {W(1.6)}/><ellipse cx="84" cy="14" rx="5" ry="3" fill="#FF6F91" {W(1.6)}/>
{sparkle(18, 50, 4)}{sparkle(110, 40, 4)}''')

I["cafe-anderson-medvedkovo"] = ("печенье-медвежонок", "ныряет в большой стакан молока, брызги", ("#EEF6FF", "#7898D0"), f'''
<path d="M30 52 H98 L92 120 H36Z" fill="#fff" fill-opacity=".9" {W(3)}/>
<path d="M32 66 H96 L92 120 H36Z" fill="#FFFDF6"/>
<path d="M32 66 Q48 60 64 66 T96 66" fill="none" {W(2)}/>
<path d="M44 66 L38 50 M84 66 L92 48" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
<g transform="rotate(170 64 50)">
<circle cx="64" cy="44" r="16" fill="#C8843A" {W(2.8)}/><circle cx="52" cy="30" r="6" fill="#C8843A" {W(2.4)}/><circle cx="76" cy="30" r="6" fill="#C8843A" {W(2.4)}/>
<ellipse cx="64" cy="50" rx="6" ry="4" fill="#E8B070" {W(1.6)}/>
</g>
<path d="M58 54 Q61 52 64 55 M66 55 Q69 52 72 54" fill="none" {W(2)}/>
<path d="M54 28 L46 18 M74 28 L82 18" {W(3)}/>
<circle cx="24" cy="44" r="3" fill="#fff" {W(1.4)}/><circle cx="104" cy="40" r="3" fill="#fff" {W(1.4)}/>''')

I["cafe-chaihona1-vernadskogo"] = ("хворост-бантик в сахарной пудре", "кружится, танцуя под снегопадом пудры", ("#FFF0F0", "#C86A6A"), f'''
<path d="M24 46 Q14 30 30 28 Q44 28 60 54 Q44 80 30 80 Q14 78 24 62 Q30 54 24 46Z" fill="#F0C06A" {W(3)}/>
<path d="M104 46 Q114 30 98 28 Q84 28 68 54 Q84 80 98 80 Q114 78 104 62 Q98 54 104 46Z" fill="#F0C06A" {W(3)}/>
<path d="M30 40 Q42 44 50 54 M98 40 Q86 44 78 54" fill="none" stroke="#D89A3A" stroke-width="2.4"/>
<rect x="52" y="40" width="24" height="28" rx="8" fill="#E8B050" {W(3)}/>
{eye(59, 52, .4)}{eye(69, 52, .4)}<path d="M60 59 Q64 62 68 59" fill="none" {W(1.6)}/>
<path d="M56 68 L48 96 M72 68 L82 94" {W(3)}/>
<g fill="#fff"><circle cx="20" cy="96" r="2.4"/><circle cx="36" cy="108" r="2"/><circle cx="96" cy="104" r="2.4"/><circle cx="110" cy="92" r="2"/><circle cx="64" cy="18" r="2.2"/><circle cx="40" cy="14" r="1.8"/><circle cx="90" cy="16" r="1.8"/></g>
<path d="M22 112 Q64 100 106 112" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="4 6" stroke-linecap="round"/>''')

I["cafe-chaihona-avenue"] = ("горка медового чак-чака", "с неё на санках скатывается изюминка", ("#FFF8DC", "#E0A82A"), f'''
<ellipse cx="64" cy="108" rx="54" ry="10" fill="#fff" {W(2.6)}/>
<path d="M18 104 Q30 40 64 30 Q98 40 110 104Z" fill="#F2B640" {W(3)}/>
<g fill="#D88A1E" stroke="{O}" stroke-width="1.2"><rect x="40" y="70" width="8" height="5" rx="2"/><rect x="58" y="56" width="8" height="5" rx="2"/><rect x="76" y="72" width="8" height="5" rx="2"/><rect x="50" y="88" width="8" height="5" rx="2"/><rect x="70" y="92" width="8" height="5" rx="2"/><rect x="86" y="88" width="8" height="5" rx="2"/><rect x="32" y="92" width="8" height="5" rx="2"/></g>
<path d="M44 46 Q50 40 52 48 M78 46 Q82 40 86 48" fill="none" stroke="#FFF0A0" stroke-width="3" stroke-linecap="round"/>
{eye(54, 76, .55)}{eye(72, 76, .55)}{smile(63, 83, 3.5, .65)}
<g transform="rotate(30 96 54)"><path d="M84 60 H106 Q110 60 110 56" fill="none" stroke="#E8304A" stroke-width="3" stroke-linecap="round"/>
<ellipse cx="96" cy="52" rx="7" ry="6" fill="#5A2A4A" {W(2)}/><circle cx="94" cy="50" r="1.4" fill="#fff"/><circle cx="99" cy="50" r="1.4" fill="#fff"/></g>
<path d="M104 30 Q110 26 114 30" fill="none" stroke="#fff" stroke-width="2.4"/>''')

I["cafe-chaihona-crocus"] = ("стакан чая в подстаканнике с долькой лимона", "сам себя размешивает ложечкой — в чае вихрь", ("#EAF0FF", "#5A6AA8"), f'''
<path d="M40 30 H88 L84 100 H44Z" fill="#C86A2A" fill-opacity=".85" {W(3)}/>
<path d="M44 40 Q64 52 84 40 M46 56 Q64 66 82 56" fill="none" stroke="#F0A060" stroke-width="2.6"/>
<circle cx="56" cy="34" r="8" fill="#FFE860" {W(2)}/><path d="M56 26 V42 M48 34 H64 M50 28 L62 40 M62 28 L50 40" stroke="#F0C020" stroke-width="1.4"/>
<path d="M78 14 L70 70" stroke="#C8CCD8" stroke-width="4" stroke-linecap="round"/>
<path d="M36 64 H92 L88 108 H40Z" fill="#C8A040" {W(3)}/>
<path d="M42 72 H86 M44 96 H84" stroke="#E8C870" stroke-width="2.6"/>
<path d="M92 70 Q106 72 104 86 Q102 98 88 96" fill="none" stroke="#C8A040" stroke-width="5"/>
<path d="M92 70 Q106 72 104 86 Q102 98 88 96" fill="none" {W(1.4)} opacity=".5"/>
<rect x="34" y="106" width="60" height="8" rx="3" fill="#B08830" {W(2.4)}/>
{eye(56, 84, .5)}{eye(72, 84, .5)}{smile(64, 90, 3, .6)}''')

I["cafe-chaihona-salaris"] = ("ролл в лаваше с начинкой", "делает «колесо» на восточном ковре", ("#FFEFE8", "#C8503A"), f'''
<path d="M6 104 L122 104 L118 122 H10Z" fill="#B8203A" {W(2.6)}/>
<path d="M18 108 h10 M36 108 h10 M56 108 h10 M76 108 h10 M96 108 h10" stroke="#FFC93C" stroke-width="3"/>
<path d="M16 116 h96" stroke="#2E5BC8" stroke-width="2.4"/>
<path d="M18 40 Q64 30 98 64" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="4 6" stroke-linecap="round"/>
<g transform="rotate(-50 64 66)">
<rect x="48" y="30" width="32" height="64" rx="14" fill="#F6E2B0" {W(3)}/>
<ellipse cx="64" cy="32" rx="14" ry="6" fill="#7CC24A" {W(2.2)}/><circle cx="58" cy="31" r="2.4" fill="#E8304A"/><circle cx="70" cy="32" r="2.4" fill="#C88A3A"/>
<path d="M50 50 L78 58 M50 66 L78 74" stroke="#E0C080" stroke-width="2"/>
{eye(58, 62, .45)}{eye(70, 62, .45)}<path d="M60 70 Q64 73 68 70" fill="none" {W(1.6)}/>
<path d="M48 54 L32 50 M80 54 L96 50 M54 94 L50 108 M74 94 L78 108" {W(3)}/>
</g>''')

I["cafe-chaihona-metropolis"] = ("плитка кунжутного козинака", "карабкается по лесенке из других плиток козинака", ("#F8F4E8", "#A8986A"), f'''
<rect x="10" y="96" width="34" height="16" rx="3" fill="#E8C060" {W(2.6)}/>
<rect x="34" y="80" width="34" height="16" rx="3" fill="#E8C060" {W(2.6)}/>
<rect x="58" y="64" width="34" height="16" rx="3" fill="#E8C060" {W(2.6)}/>
<g fill="#fff"><circle cx="18" cy="102" r="1.4"/><circle cx="28" cy="106" r="1.4"/><circle cx="38" cy="102" r="1.4"/><circle cx="42" cy="86" r="1.4"/><circle cx="54" cy="90" r="1.4"/><circle cx="64" cy="86" r="1.4"/><circle cx="66" cy="70" r="1.4"/><circle cx="78" cy="74" r="1.4"/><circle cx="88" cy="70" r="1.4"/></g>
<rect x="80" y="24" width="30" height="40" rx="5" fill="#F2D070" {W(3)}/>
<g fill="#fff"><circle cx="86" cy="30" r="1.6"/><circle cx="104" cy="32" r="1.6"/><circle cx="96" cy="58" r="1.6"/><circle cx="86" cy="54" r="1.6"/></g>
{eye(89, 40, .45)}{eye(101, 40, .45)}<path d="M92 48 Q95 51 98 48" fill="none" {W(1.6)}/>
<path d="M80 40 L70 30 M110 40 L118 30 M86 64 L84 72 M104 64 L108 70" {W(3)}/>
<path d="M14 40 l8 -8 l4 8" fill="none" stroke="#fff" stroke-width="2.4"/>
{sparkle(30, 24, 4)}''')

I["cafe-uryuk-shchelkovsky"] = ("торт с шапочкой-тюбетейкой с узором", "на праздничном блюде между двумя бенгальскими огнями", ("#F0FFF4", "#2E9A6A"), f'''
<ellipse cx="64" cy="106" rx="50" ry="10" fill="#fff" {W(2.6)}/>
<path d="M24 100 V74 Q24 60 64 60 Q104 60 104 74 V100 Q104 108 64 108 Q24 108 24 100Z" fill="#FFF4E0" {W(3)}/>
<path d="M24 84 Q30 92 36 84 Q42 92 48 84 Q54 92 60 84 Q66 92 72 84 Q78 92 84 84 Q90 92 96 84 Q100 90 104 84" fill="none" stroke="#F0C080" stroke-width="2.4"/>
{eye(52, 96, .45)}{eye(76, 96, .45)}<path d="M60 100 Q64 103 68 100" fill="none" {W(1.6)}/>
<path d="M34 66 V46 Q34 34 64 34 Q94 34 94 46 V66 Q64 74 34 66Z" fill="#1F7A4A" {W(3)}/>
<path d="M36 52 Q64 58 92 52" fill="none" stroke="#fff" stroke-width="2.4"/>
<path d="M44 62 Q48 56 52 62 Q48 68 44 62Z M60 64 Q64 58 68 64 Q64 70 60 64Z M76 62 Q80 56 84 62 Q80 68 76 62Z M52 44 Q56 40 60 44 Q56 48 52 44Z M68 44 Q72 40 76 44 Q72 48 68 44Z" fill="#fff"/>
<path d="M22 46 L14 26 M106 46 L114 26" stroke="#9AA0B8" stroke-width="2.4"/>
<path d="M14 26 l-6 -6 M14 26 l6 -6 M14 26 l-8 2 M14 26 l8 2 M14 26 V16 M114 26 l-6 -6 M114 26 l6 -6 M114 26 l-8 2 M114 26 l8 2 M114 26 V16" stroke="#FFE27A" stroke-width="2.2" stroke-linecap="round"/>''')

I["cafe-uryuk-prime-park"] = ("вулкан из картофельного пюре", "извергает подливку-лаву, рядом греется котлетка", ("#FFF4EC", "#D87A4A"), f'''
<ellipse cx="64" cy="106" rx="56" ry="14" fill="#fff" {W(3)}/>
<path d="M22 102 Q40 50 54 40 H74 Q88 50 104 102Z" fill="#FFF0B8" {W(3)}/>
<path d="M54 40 Q48 56 56 62 Q60 50 64 64 Q70 52 72 62 Q80 54 74 40Z" fill="#9A4A1E" {W(2.4)}/>
<path d="M58 34 Q54 24 60 18 M70 34 Q74 24 68 16" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<circle cx="64" cy="40" r="3" fill="#7CC24A"/>
{eye(52, 82, .55)}{eye(72, 82, .55)}<ellipse cx="62" cy="91" rx="4" ry="3" fill="#E8554A" {W(1.6)}/>
<ellipse cx="102" cy="96" rx="14" ry="9" fill="#9A5A2E" {W(2.6)}/>{eye(98, 95, .35)}{eye(106, 95, .35)}<path d="M99 100 Q102 102 105 100" fill="none" {W(1.4)}/>''')

# ---------- БАССЕЙНЫ ----------

I["kitenok-molodezhnaya"] = ("доска для плавания с мордочкой", "малыш держится за неё и болтает ногами в воде", ("#E0F8FF", "#2AA0D8"), f'''
<path d="M0 66 Q32 60 64 66 T128 66 V128 H0Z" fill="#4AB8F0"/>
<path d="M0 66 Q32 60 64 66 T128 66" fill="none" stroke="#fff" stroke-width="3"/>
<path d="M26 48 Q26 32 40 32 H88 Q102 32 102 48 V80 Q102 92 88 92 H40 Q26 92 26 80Z" fill="#FFC93C" {W(3)}/>
<rect x="44" y="40" width="40" height="8" rx="4" fill="#FF8A3D"/>
{eye(52, 62, .6)}{eye(76, 62, .6)}{smile(64, 70, 4, .7)}{blush(44, 70, .6)}{blush(84, 70, .6)}
<circle cx="64" cy="104" r="11" fill="#FFD9B8" {W(2.6)}/><path d="M53 100 Q53 90 64 90 Q75 90 75 100Z" fill="#7C5CE0" {W(2.2)}/>
<path d="M54 92 L48 86 M74 92 L80 86" stroke="#FFD9B8" stroke-width="5" stroke-linecap="round"/>
<path d="M30 112 Q36 104 42 112 M86 112 Q92 104 98 112" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<circle cx="24" cy="102" r="3" fill="#fff"/><circle cx="104" cy="100" r="3" fill="#fff"/>''')

I["kitenok-nakhimovsky"] = ("пара синих ласт с глазками", "шлёпают по бортику к воде, оставляя мокрые следы", ("#E8EEFF", "#4A5AC8"), f'''
<path d="M0 100 H128 V128 H0Z" fill="#3AA8E8"/><path d="M0 100 H128" stroke="#fff" stroke-width="4"/>
<rect x="0" y="90" width="128" height="10" fill="#E8F0F8" {W(2)}/>
<path d="M32 22 Q40 16 48 22 L50 44 Q66 70 62 92 Q46 98 30 94 Q14 90 14 84 Q20 64 30 44Z" fill="#2E6AE0" {W(3)}/>
<path d="M33 24 Q40 20 47 24 L48 38 Q40 42 32 38Z" fill="#1A3A90"/>
<path d="M24 84 L36 52 M38 90 L42 54 M52 90 L46 54" stroke="#6A9AF0" stroke-width="2"/>
{eye(35, 48, .45)}{eye(45, 48, .45)}
<path d="M82 14 Q90 8 98 14 L100 36 Q116 62 112 86 Q96 92 80 88 Q64 84 64 78 Q70 56 80 36Z" fill="#2E6AE0" {W(3)}/>
<path d="M83 16 Q90 12 97 16 L98 30 Q90 34 82 30Z" fill="#1A3A90"/>
<path d="M74 78 L86 46 M88 84 L92 48 M102 84 L96 48" stroke="#6A9AF0" stroke-width="2"/>
{eye(85, 40, .45)}{eye(95, 40, .45)}<path d="M87 46 Q90 49 93 46" fill="none" {W(1.6)}/>
<ellipse cx="66" cy="114" rx="5" ry="3" fill="#fff" opacity=".7"/><ellipse cx="22" cy="116" rx="4" ry="2.4" fill="#fff" opacity=".7"/>''')

I["ms-pool-shipilovsky"] = ("стартовая тумба с номером 4", "стоит над дорожкой, с неё только что прыгнули — брызги", ("#E8FFF0", "#2EB06A"), f'''
<path d="M0 78 H128 V128 H0Z" fill="#3AA0E0"/>
<path d="M0 96 H128 M0 114 H128" stroke="#FFF" stroke-width="3" stroke-dasharray="6 6"/>
<path d="M38 40 H90 L84 62 H44Z" fill="#fff" {W(3)}/><rect x="44" y="62" width="40" height="16" fill="#D8DCE6" {W(2.6)}/>
<text x="56" y="58" font-family="Arial" font-weight="bold" font-size="16" fill="#2E5BC8">4</text>
<path d="M40 42 L34 34 M88 42 L94 34" {W(2.4)}/>
{eye(52, 70, .4)}{eye(76, 70, .4)}
<path d="M100 78 L96 56 M108 80 L112 58 M116 80 L124 66 M92 80 L84 64" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
<circle cx="102" cy="48" r="3" fill="#fff"/><circle cx="118" cy="56" r="2.4" fill="#fff"/>''')

I["ms-pool-yuzhny"] = ("мальчик-пловец в зелёной шапочке", "плывёт баттерфляем — обе руки взлетают над водой", ("#FFF6E0", "#E8A030"), f'''
<path d="M0 74 Q32 68 64 74 T128 74 V128 H0Z" fill="#3A9AE0"/>
<path d="M30 74 Q20 40 40 30 M98 74 Q108 40 88 30" fill="none" stroke="#FFD9B8" stroke-width="9" stroke-linecap="round"/>
<path d="M30 74 Q20 40 40 30 M98 74 Q108 40 88 30" fill="none" {W(1.4)} opacity=".5"/>
<circle cx="64" cy="70" r="16" fill="#FFD9B8" {W(3)}/>
<path d="M48 66 Q48 50 64 50 Q80 50 80 66Z" fill="#3EB84A" {W(2.6)}/>
<rect x="50" y="64" width="11" height="8" rx="4" fill="#9AD6FF" {W(2)}/><rect x="67" y="64" width="11" height="8" rx="4" fill="#9AD6FF" {W(2)}/>
<ellipse cx="64" cy="79" rx="3.4" ry="2.6" fill="#E8554A" {W(1.6)}/>
<path d="M0 80 Q32 74 64 80 T128 80" fill="none" stroke="#fff" stroke-width="3"/>
<circle cx="36" cy="24" r="3" fill="#fff"/><circle cx="94" cy="22" r="3" fill="#fff"/><circle cx="20" cy="56" r="2.4" fill="#fff"/><circle cx="110" cy="54" r="2.4" fill="#fff"/>''')

I["murena-izumrudny"] = ("очки для плавания с глазками", "висят на бортике изумрудного бассейна, в стёклах отражается вода", ("#E0FFF4", "#1A9A74"), f'''
<path d="M0 74 H128 V128 H0Z" fill="#1ABC9C"/><path d="M0 92 Q32 86 64 92 T128 92 M0 110 Q32 104 64 110 T128 110" fill="none" stroke="#7AF0D0" stroke-width="2.6"/>
<rect x="0" y="64" width="128" height="12" fill="#fff" {W(2.4)}/>
<path d="M14 50 Q14 34 36 36 M114 50 Q114 34 92 36" fill="none" stroke="#FF5A8A" stroke-width="5"/>
<path d="M62 50 H66" {W(3)}/>
<rect x="18" y="34" width="44" height="34" rx="16" fill="#9AE8FF" {W(3)}/><rect x="66" y="34" width="44" height="34" rx="16" fill="#9AE8FF" {W(3)}/>
<path d="M24 44 Q30 38 36 42 M72 44 Q78 38 84 42" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
{eye(42, 52, .7)}{eye(88, 52, .7)}
<path d="M54 82 Q64 88 74 82" fill="none" {W(2.4)}/>''')

I["kidway-rodionovskaya"] = ("гибкая аквапалка-нудл", "выгнулась аркой, под ней проныривает малыш", ("#FFF0FA", "#C85AB8"), f'''
<path d="M0 84 Q32 78 64 84 T128 84 V128 H0Z" fill="#5AB8F0"/>
<path d="M18 92 Q18 24 64 24 Q110 24 110 92" fill="none" stroke="{O}" stroke-width="20" stroke-linecap="round"/>
<path d="M18 92 Q18 24 64 24 Q110 24 110 92" fill="none" stroke="#7CE04A" stroke-width="14" stroke-linecap="round"/>
<path d="M28 60 Q34 36 54 30" fill="none" stroke="#B8F090" stroke-width="3" stroke-linecap="round"/>
{eye(56, 24, .45)}{eye(72, 24, .45)}
<circle cx="64" cy="84" r="13" fill="#FFD9B8" {W(2.8)}/><path d="M51 80 Q51 68 64 68 Q77 68 77 80Z" fill="#FFC93C" {W(2.2)}/>
<path d="M58 84 Q60 82 62 84 M66 84 Q68 82 70 84" fill="none" {W(1.8)}/><circle cx="64" cy="90" r="2" fill="#E8554A"/>
<path d="M0 92 Q32 86 64 92 T128 92" fill="none" stroke="#fff" stroke-width="3"/>
<circle cx="88" cy="70" r="3" fill="#fff" {W(1.2)}/><circle cx="94" cy="60" r="2" fill="#fff" {W(1.2)}/>''')

I["aqua-class-alekseevskaya"] = ("розовая плавательная шапочка с пупырышками", "выныривает из воды, пуская пузыри", ("#F0F8FF", "#4A88E0"), f'''
<path d="M0 82 Q32 76 64 82 T128 82 V128 H0Z" fill="#3A9AE8"/>
<path d="M22 84 Q22 30 64 28 Q106 30 106 84Z" fill="#FF7FB0" {W(3)}/>
<g fill="#FFB8D4" stroke="{O}" stroke-width="1.2"><circle cx="44" cy="44" r="3"/><circle cx="58" cy="38" r="3"/><circle cx="74" cy="38" r="3"/><circle cx="88" cy="46" r="3"/><circle cx="36" cy="60" r="3"/><circle cx="92" cy="62" r="3"/></g>
{eye(52, 64, .6)}{eye(76, 64, .6)}<ellipse cx="64" cy="75" rx="4" ry="3.4" fill="#fff" {W(1.8)}/>
<path d="M0 84 Q32 78 64 84 T128 84" fill="none" stroke="#fff" stroke-width="3"/>
<circle cx="64" cy="16" r="4" fill="#fff" fill-opacity=".6" {W(1.6)}/><circle cx="74" cy="8" r="2.6" fill="#fff" fill-opacity=".6" {W(1.4)}/>
<path d="M30 100 Q40 96 50 100 M80 108 Q90 104 100 108" fill="none" stroke="#fff" stroke-width="2.4"/>''')

I["aquapups"] = ("пупсик с соской в жёлтой шапочке", "лежит на спинке звёздочкой и плывёт среди пузырей", ("#FFFBE8", "#40C0E0"), f'''
<path d="M0 60 Q32 54 64 60 T128 60 V128 H0Z" fill="#62CCF0"/>
<path d="M42 80 L18 70 M86 80 L110 70 M52 100 L38 118 M76 100 L90 118" stroke="#FFD9B8" stroke-width="10" stroke-linecap="round"/>
<path d="M42 80 L18 70 M86 80 L110 70 M52 100 L38 118 M76 100 L90 118" fill="none" {W(1.4)} opacity=".4"/>
<ellipse cx="64" cy="90" rx="20" ry="16" fill="#FF9AC0" {W(2.8)}/>
<circle cx="64" cy="62" r="18" fill="#FFD9B8" {W(3)}/>
<path d="M46 58 Q46 42 64 42 Q82 42 82 58Z" fill="#FFD84A" {W(2.6)}/>
<path d="M56 62 Q58 60 60 62 M68 62 Q70 60 72 62" fill="none" {W(2)}/>
<circle cx="64" cy="72" r="5" fill="#5CB7F2" {W(2)}/><circle cx="64" cy="72" r="2" fill="#fff"/>
{blush(52, 70, .6)}{blush(76, 70, .6)}
<circle cx="20" cy="96" r="5" fill="#fff" fill-opacity=".6" {W(1.6)}/><circle cx="104" cy="100" r="4" fill="#fff" fill-opacity=".6" {W(1.6)}/><circle cx="112" cy="86" r="2.6" fill="#fff" fill-opacity=".6" {W(1.4)}/>''')


if __name__ == "__main__":
    for pid, (hero, scene, (a, b), body) in I.items():
        open(os.path.join(ROOT, "icons-src", f"{pid}.svg"), "w").write(bgsvg(a, b, body))
    reg = os.path.join(ROOT, "icons-src", "subjects.txt"); txt = open(reg, encoding="utf-8").read()
    for pid in I:
        txt = re.sub(rf"^{re.escape(pid)} — .*\n", "", txt, flags=re.M)
    if not txt.endswith("\n"):
        txt += "\n"
    txt += "".join(f"{pid} — герой: {h} | сцена: {sc}\n" for pid, (h, sc, _, _) in I.items())
    open(reg, "w", encoding="utf-8").write(txt)
    print("нарисовано:", len(I))
