"""Робот «художник», 08.11 ~17:00 UTC. check_unique.py повторов не нашёл (0), но в реестре осталась серия
кафе от старого генератора «блюдо × сцена» (кусок сыра / кружка какао / нигири / бургер + горка, вигвам, качели,
слюнявчик, лошадка, мыльные пузыри…) — 36 иконок со строками реестра старого формата. Все 36 придуманы заново
и нарисованы вручную по одной: свой герой по кухне или детской комнате заведения, своя сцена, ракурс и палитра фона.
Запуск из корня: python3 tools/icons_artist_1108_1700.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT
from icons_artist_1108_0800 import limb, SK
from icons_artist_1108_1400 import head

I = {}

# 1. АндерСон, Афанасьевский — кусочек «Наполеона» в треуголке марширует
I["cafe-anderson-afanasyevsky"] = ("кусочек торта «Наполеон» в чёрной треуголке с кокардой", "важно марширует по праздничной скатерти и отдаёт честь", ("#FFF4D6", "#E8B04A"), f'''
<path d="M0 108 H128 V128 H0Z" fill="#F58CA8" {W(2.4)}/><path d="M12 108 V128 M36 108 V128 M60 108 V128 M84 108 V128 M108 108 V128" stroke="#fff" stroke-width="5" opacity=".7"/>
{limb("M52 96 L46 112", "#F7DFA8", 8)}{limb("M76 96 L84 110", "#F7DFA8", 8)}
<ellipse cx="44" cy="114" rx="7" ry="4" fill="{O}"/><ellipse cx="87" cy="112" rx="7" ry="4" fill="{O}"/>
<rect x="34" y="52" width="60" height="46" rx="6" fill="#F7DFA8" {W(3)}/>
<path d="M35 67 H93 M35 82 H93" stroke="#FFFBF0" stroke-width="6"/><path d="M35 64 H93 M35 70 H93 M35 79 H93 M35 85 H93" stroke="#D8A860" stroke-width="1.4"/>
<rect x="32" y="46" width="64" height="12" rx="6" fill="#E9B86A" {W(2.6)}/>
<circle cx="42" cy="51" r="1.6" fill="#B87A30"/><circle cx="56" cy="50" r="1.6" fill="#B87A30"/><circle cx="72" cy="52" r="1.6" fill="#B87A30"/><circle cx="86" cy="50" r="1.6" fill="#B87A30"/>
<path d="M30 48 Q64 6 98 48 Q64 38 30 48Z" fill="#2B2B3A" {W(2.8)}/>
<circle cx="64" cy="32" r="6" fill="#2F6FDB" {W(2)}/><circle cx="64" cy="32" r="3.6" fill="#fff"/><circle cx="64" cy="32" r="1.8" fill="#E8403A"/>
{face(60, 74, d=10, k=.8)}
{limb("M93 64 Q108 56 98 42", "#F7DFA8", 8)}
{sparkle(18, 30, 5)}''')

# 2. Чайхона №1, Жуковка — игрушечная юрта детского зала
I["cafe-chaihona1-zhukovka"] = ("игрушечная юрта-домик с красной крышей и узорным войлоком", "стоит в детском зале, из круглой двери выглядывает малыш, над дымником вьётся флажок", ("#E3F6FF", "#4FA8D8"), f'''
<path d="M0 104 Q64 96 128 104 V128 H0Z" fill="#9FD873" {W(2.4)}/>
<path d="M24 70 H104 V106 H24Z" fill="#FFF2D8" {W(3)}/>
<path d="M24 80 l8 -6 l8 6 l8 -6 l8 6 l8 -6 l8 6 l8 -6 l8 6 l8 -6 l8 6" fill="none" stroke="#E8503A" stroke-width="3" stroke-linejoin="round"/>
<path d="M18 74 Q64 16 110 74Z" fill="#E8503A" {W(3)}/>
<path d="M34 64 Q64 32 94 64" fill="none" stroke="#FFD23A" stroke-width="3.4"/>
{eye(50, 58, .6)}{eye(78, 58, .6)}{smile(64, 64, 4, .8)}{blush(42, 64, .5)}{blush(86, 64, .5)}
<rect x="56" y="30" width="16" height="8" rx="3" fill="#FFD23A" {W(2.4)}/>
<path d="M64 30 V10" {W(2.6)}/><path d="M64 10 L82 15 L64 21Z" fill="#3FBF8F" {W(2.2)}/>
<path d="M50 106 V90 Q64 78 78 90 V106Z" fill="#5A3A8A" {W(2.8)}/>
{head(64, 96, 9, "#3A2A20", .38)}''')

# 3. Чайхона №1, Новокосино — сухой бассейн: из шариков торчат ножки ныряльщика
I["cafe-chaihona1-novokosino"] = ("сухой бассейн с разноцветными шариками", "малыш нырнул в шарики с головой — наружу торчат только ножки в полосатых носках", ("#F0E6FF", "#8A6AD8"), f'''
{limb("M58 74 L50 36", SK, 10)}{limb("M72 74 L82 38", SK, 10)}
<path d="M46 40 L54 40 L53 46 L46 46Z M78 42 L86 42 L86 48 L79 48Z" fill="#fff"/>
<ellipse cx="49" cy="32" rx="7" ry="5" fill="#E8403A" {W(2.4)}/><ellipse cx="84" cy="34" rx="7" ry="5" fill="#E8403A" {W(2.4)}/>
<circle cx="28" cy="72" r="10" fill="#FF5A5A" {W(2.4)}/><circle cx="46" cy="70" r="10" fill="#FFD23A" {W(2.4)}/><circle cx="64" cy="76" r="10" fill="#4AB8F0" {W(2.4)}/>
<circle cx="82" cy="70" r="10" fill="#6CD06C" {W(2.4)}/><circle cx="100" cy="72" r="10" fill="#FF8FD0" {W(2.4)}/>
<circle cx="38" cy="80" r="9" fill="#4AB8F0" {W(2.4)}/><circle cx="90" cy="80" r="9" fill="#FFD23A" {W(2.4)}/>
<circle cx="24" cy="44" r="6" fill="#FFD23A" {W(2.2)}/><circle cx="104" cy="40" r="6" fill="#6CD06C" {W(2.2)}/><circle cx="96" cy="20" r="5" fill="#FF5A5A" {W(2.2)}/>
<path d="M18 36 l-5 -4 M110 32 l5 -4 M30 54 l-6 -2" {W(2.2)}/>
<rect x="12" y="82" width="104" height="34" rx="12" fill="#2F8AE0" {W(3)}/>
{eye(50, 96, .7)}{eye(78, 96, .7)}{smile(64, 102, 5, .9)}{blush(40, 103, .6)}{blush(88, 103, .6)}''')

# 4. Чайхона №1, Тушино — аниматор-тигрёнок крутит собачку из шарика
I["cafe-chaihona1-tushino"] = ("девушка-аниматор в костюме тигрёнка с ушками на капюшоне", "крутит из длинного голубого шарика собачку для детского праздника", ("#DDF8EE", "#3FBF8F"), f'''
<path d="M18 128 Q18 92 50 88 Q82 92 82 128Z" fill="#FF9A3C" {W(3)}/>
<path d="M30 104 l8 4 M28 116 l10 2 M70 104 l-8 4 M72 116 l-10 2" stroke="{O}" stroke-width="3" stroke-linecap="round"/>
<ellipse cx="50" cy="108" rx="11" ry="14" fill="#FFF2D8" {W(2.4)}/>
<path d="M24 66 Q22 34 50 32 Q78 34 76 66 Q76 86 50 88 Q24 86 24 66Z" fill="#FF9A3C" {W(3)}/>
<circle cx="28" cy="36" r="8" fill="#FF9A3C" {W(2.6)}/><circle cx="72" cy="36" r="8" fill="#FF9A3C" {W(2.6)}/>
<circle cx="28" cy="36" r="3.6" fill="#FFC7A0"/><circle cx="72" cy="36" r="3.6" fill="#FFC7A0"/>
<path d="M44 34 l2 6 M56 34 l-2 6 M50 33 v6" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>
<circle cx="50" cy="64" r="16" fill="{SK}" {W(2.6)}/>
<path d="M34 60 Q36 48 50 48 Q64 48 66 60 Q58 54 50 56 Q42 54 34 60Z" fill="#5A3A20"/>
{eye(44, 64, .5)}{eye(56, 64, .5)}<path d="M46 71 Q50 74 54 71" fill="none" {W(2)}/>{blush(39, 70, .45)}{blush(61, 70, .45)}
<path d="M86 70 Q100 62 112 70 Q114 76 100 78 Q86 78 86 70Z" fill="#4AA8F0" {W(2.4)}/>
<ellipse cx="88" cy="86" rx="4" ry="9" fill="#4AA8F0" {W(2.2)}/><ellipse cx="110" cy="86" rx="4" ry="9" fill="#4AA8F0" {W(2.2)}/>
<ellipse cx="112" cy="54" rx="9" ry="7" fill="#4AA8F0" {W(2.4)}/><ellipse cx="104" cy="44" rx="3.4" ry="8" fill="#4AA8F0" {W(2.2)}/>
<path d="M110 62 L112 70" {W(4)}/><path d="M110 62 L112 70" stroke="#4AA8F0" stroke-width="1.6"/>
<circle cx="115" cy="52" r="1.6" fill="{O}"/>
{limb("M72 96 Q80 84 88 76", "#FF9A3C", 9)}''')

# 5. Чайхона, Железнодорожный — пирамидка, малыш надевает верхушку
I["cafe-chaihona-zheleznodorozhny"] = ("детская пирамидка из цветных колец", "малыш сверху надевает на неё последнее синее колечко-верхушку, пирамидка улыбается", ("#FFE9DA", "#F2A27A"), f'''
<rect x="26" y="100" width="76" height="13" rx="6" fill="#C98547" {W(2.8)}/>
<rect x="60" y="34" width="8" height="68" rx="3" fill="#E7B877" {W(2.2)}/>
<rect x="30" y="82" width="68" height="20" rx="10" fill="#E8403A" {W(3)}/>
<rect x="36" y="65" width="56" height="18" rx="9" fill="#FF9A3C" {W(3)}/>
<rect x="42" y="49" width="44" height="17" rx="8.5" fill="#FFD23A" {W(3)}/>
<rect x="48" y="35" width="32" height="15" rx="7.5" fill="#6CD06C" {W(3)}/>
{eye(54, 91, .6)}{eye(74, 91, .6)}{smile(64, 96, 4, .8)}{blush(45, 96, .5)}{blush(83, 96, .5)}
<ellipse cx="64" cy="20" rx="12" ry="8" fill="#3A7AE8" {W(2.8)}/><circle cx="64" cy="11" r="4" fill="#3A7AE8" {W(2.2)}/>
{limb("M118 2 L78 18", SK, 9)}
<path d="M44 22 l-6 -4 M84 30 l6 2" {W(2)}/>{sparkle(22, 50, 5)}''')

# 6. Чайхона, Остров Мечты — сахарная вата на фоне петли американских горок
I["cafe-chaihona-ostrov-mechty"] = ("розовое облако сахарной ваты на палочке", "довольно улыбается после аттракционов, позади светится петля американских горок", ("#5A6AD8", "#232A70"), f'''
<circle cx="96" cy="66" r="26" fill="none" stroke="#FFD23A" stroke-width="5"/><circle cx="96" cy="66" r="26" fill="none" stroke="{O}" stroke-width="1.4"/>
<path d="M60 112 Q78 112 82 90 M112 90 Q116 112 130 112" fill="none" stroke="#FFD23A" stroke-width="5"/>
<path d="M88 112 V92 M104 112 V92" {W(2.4)}/>
<circle cx="78" cy="44" r="2" fill="#FFF3A0"/><circle cx="114" cy="48" r="2" fill="#FFF3A0"/><circle cx="118" cy="80" r="2" fill="#FFF3A0"/>
<path d="M46 126 L54 74" stroke="#fff" stroke-width="5" stroke-linecap="round"/><path d="M46 126 L54 74" fill="none" {W(1.4)}/>
<path d="M30 62 Q20 54 28 44 Q26 30 40 28 Q46 16 60 22 Q74 18 76 32 Q88 36 82 50 Q88 62 74 66 Q66 76 52 72 Q38 76 30 62Z" fill="#FFA5D0" {W(3)}/>
<path d="M38 40 Q44 34 50 38 M62 30 Q68 28 70 34" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".8"/>
{face(54, 50, d=8, k=.8)}
{sparkle(18, 92, 5, "#FFF3A0")}{sparkle(30, 20, 4, "#FFF3A0")}''')

# 7. Чайхона, Европолис — кегли разлетаются от «страйка»
I["cafe-chaihona-europolis"] = ("три детские кегли с глазками в красных поясках", "мяч влетает в них «страйком», кегли со смехом разлетаются в стороны", ("#E6FAD6", "#5CB85C"), f'''
<path d="M0 104 H128 V128 H0Z" fill="#F2C98A" {W(2.4)}/><path d="M0 116 H128" stroke="#D9A866" stroke-width="2"/>
<g transform="rotate(-28 46 98)"><path d="M37 100 Q31 76 41 66 Q38 52 46 44 Q54 52 51 66 Q61 76 55 100Z" fill="#fff" {W(2.8)}/><path d="M40 60 H52" stroke="#E8403A" stroke-width="4"/>{eye(43, 78, .45)}{eye(50, 78, .45)}</g>
<path d="M70 104 Q62 76 74 64 Q70 46 80 38 Q90 46 86 64 Q98 76 90 104Z" fill="#fff" {W(3)}/>
<path d="M73 56 H87" stroke="#E8403A" stroke-width="5"/>
{eye(75, 80, .55)}{eye(85, 80, .55)}<path d="M76 88 Q80 93 84 88Z" fill="{O}"/>
<g transform="rotate(32 106 96)"><path d="M98 100 Q92 78 101 69 Q98 56 106 49 Q114 56 111 69 Q120 78 114 100Z" fill="#fff" {W(2.8)}/><path d="M100 63 H112" stroke="#E8403A" stroke-width="4"/>{eye(103, 80, .45)}{eye(110, 80, .45)}</g>
<circle cx="30" cy="100" r="13" fill="#7A3AC8" {W(3)}/><circle cx="26" cy="96" r="2" fill="{O}"/><circle cx="33" cy="94" r="2" fill="{O}"/><circle cx="30" cy="101" r="2" fill="{O}"/>
<path d="M6 92 H14 M4 102 H12" {W(2.4)}/>
<path d="M60 30 l-4 -6 M100 30 l4 -6 M80 24 v-6" {W(2.4)}/>''')

# 8. IL Патио, Калита — детская пицца-мордашка
I["cafe-ilpatio-kalita"] = ("детская пицца-мордашка с глазками из маслин и улыбкой из колбасок", "хохочет на подносе детского меню «Бамбини», рядом стаканчик сока с трубочкой", ("#FFE3C8", "#E8603A"), f'''
<rect x="8" y="98" width="112" height="14" rx="6" fill="#7AD8E8" {W(2.6)}/>
<rect x="96" y="66" width="16" height="32" rx="4" fill="#FFB84A" {W(2.6)}/><path d="M104 66 L110 46 L116 44" fill="none" stroke="#E8403A" stroke-width="3" stroke-linecap="round"/>
<circle cx="56" cy="64" r="40" fill="#E9A44A" {W(3)}/>
<circle cx="56" cy="64" r="32" fill="#E8503A"/>
<path d="M30 60 Q34 46 46 50 Q56 40 66 50 Q80 44 82 62 Q90 76 74 82 Q62 94 48 86 Q30 86 32 74 Q24 68 30 60Z" fill="#FFE07A"/>
<circle cx="56" cy="64" r="32" fill="none" {W(1.6)}/>
<circle cx="44" cy="56" r="8" fill="#2B2B3A" {W(1.8)}/><circle cx="44" cy="56" r="3" fill="#FFE07A"/><circle cx="41" cy="53" r="1.6" fill="#fff"/>
<circle cx="68" cy="56" r="8" fill="#2B2B3A" {W(1.8)}/><circle cx="68" cy="56" r="3" fill="#FFE07A"/><circle cx="65" cy="53" r="1.6" fill="#fff"/>
<circle cx="40" cy="74" r="5" fill="#C8302A" {W(1.8)}/><circle cx="48" cy="80" r="5" fill="#C8302A" {W(1.8)}/><circle cx="56" cy="82" r="5" fill="#C8302A" {W(1.8)}/>
<circle cx="64" cy="80" r="5" fill="#C8302A" {W(1.8)}/><circle cx="72" cy="74" r="5" fill="#C8302A" {W(1.8)}/>
<path d="M60 40 Q64 34 68 40" fill="#5CB85C" {W(1.6)}/>''')

# 9. IL Патио, Балашиха — малыш в высоком детском стульчике
I["cafe-ilpatio-balashikha"] = ("высокий детский стульчик для кормления", "в нём сидит малыш в слюнявчике и радостно машет ручками, на столике — кусочек пиццы", ("#F2F2F2", "#A0A8B8"), f'''
{limb("M40 126 L54 86", "#fff", 9)}{limb("M88 126 L74 86", "#fff", 9)}
<path d="M44 108 H84" {W(3)}/>
<rect x="44" y="34" width="40" height="58" rx="12" fill="#FFB84A" {W(3)}/>
<path d="M52 66 Q64 60 76 66 L76 88 H52Z" fill="#fff" {W(2.6)}/><path d="M56 72 Q64 76 72 72" fill="none" stroke="#F58CB8" stroke-width="2.6"/>
{limb("M54 68 L34 50", SK, 8)}{limb("M74 68 L94 50", SK, 8)}
{head(64, 50, 13, "#E0A030", .5)}
<rect x="30" y="86" width="68" height="11" rx="5.5" fill="#FF7A59" {W(2.8)}/>
<path d="M58 86 L70 86 L64 74Z" fill="#FFD23A" {W(2.2)}/><circle cx="64" cy="81" r="1.8" fill="#E8403A"/>
<path d="M26 44 l-6 -4 M102 44 l6 -4 M28 54 h-7 M100 54 h7" {W(2.2)}/>''')

# 10. Якитория, Алексеевская — огромный мыльный пузырь, внутри смеётся малыш
I["cafe-yakitoriya-alekseevskaya"] = ("огромный мыльный пузырь с радужными разводами", "аниматор выдувает его с рамки, а внутри пузыря оказался и смеётся малыш", ("#B9A0F5", "#5A38B8"), f'''
<circle cx="70" cy="56" r="36" fill="#fff" opacity=".22"/>
<path d="M40 42 Q52 22 76 22" fill="none" stroke="#FF8FD0" stroke-width="3" stroke-linecap="round" opacity=".9"/>
<path d="M44 48 Q56 28 80 28" fill="none" stroke="#8FE0FF" stroke-width="3" stroke-linecap="round" opacity=".9"/>
<path d="M100 72 Q94 86 80 90" fill="none" stroke="#FFF3A0" stroke-width="3" stroke-linecap="round" opacity=".9"/>
{head(70, 62, 15, "#C8642A", .55, mouth=False)}
<path d="M64 69 Q70 76 76 69Z" fill="{O}"/>
<circle cx="70" cy="56" r="36" fill="none" stroke="#fff" stroke-width="3"/>
<ellipse cx="54" cy="34" rx="7" ry="4" fill="#fff" transform="rotate(-35 54 34)" opacity=".85"/>
<circle cx="24" cy="102" r="11" fill="none" stroke="#FFD23A" stroke-width="5"/><circle cx="24" cy="102" r="11" fill="none" {W(1.4)}/>
<path d="M16 110 L0 128" stroke="#FFD23A" stroke-width="6" stroke-linecap="round"/>
<circle cx="18" cy="70" r="5" fill="#fff" opacity=".3" stroke="#fff" stroke-width="1.6"/><circle cx="108" cy="104" r="7" fill="#fff" opacity=".3" stroke="#fff" stroke-width="1.6"/>
<circle cx="112" cy="24" r="4" fill="#fff" opacity=".3" stroke="#fff" stroke-width="1.6"/>''')

# 11. Якитория, Багратионовская — фломастеры-человечки рисуют радугу
I["cafe-yakitoriya-bagrationovskaya"] = ("три фломастера-человечка в цветных колпачках", "вместе рисуют большую радугу на стене-раскраске детской комнаты", ("#FFFBEF", "#F2D9A8"), f'''
<path d="M10 92 A54 54 0 0 1 118 92" fill="none" stroke="#E8403A" stroke-width="8"/>
<path d="M20 92 A44 44 0 0 1 108 92" fill="none" stroke="#FFD23A" stroke-width="8"/>
<path d="M30 92 A34 34 0 0 1 98 92" fill="none" stroke="#3A9AE8" stroke-width="8"/>
<path d="M0 108 H128 V128 H0Z" fill="#B8E0A0" {W(2.4)}/>
<rect x="18" y="62" width="18" height="46" rx="5" fill="#fff" {W(2.6)}/><rect x="18" y="52" width="18" height="16" rx="6" fill="#E8403A" {W(2.6)}/>
{eye(24, 80, .42)}{eye(31, 80, .42)}<path d="M25 87 Q27.5 89 30 87" fill="none" {W(1.6)}/>
<rect x="50" y="58" width="18" height="50" rx="5" fill="#fff" {W(2.6)}/><rect x="50" y="48" width="18" height="16" rx="6" fill="#FFD23A" {W(2.6)}/>
{eye(56, 78, .42)}{eye(63, 78, .42)}<path d="M57 85 Q59.5 87 62 85" fill="none" {W(1.6)}/>
<g transform="rotate(35 92 82)"><rect x="83" y="62" width="18" height="44" rx="5" fill="#fff" {W(2.6)}/><path d="M86 62 L92 50 L98 62Z" fill="#3A9AE8" {W(2.2)}/>{eye(89, 80, .42)}{eye(96, 80, .42)}</g>
<path d="M108 100 l6 2" {W(2)}/>''')

# 12. Якитория, Электросталь (ТЦ «Апельсин») — мозаика, фишки сложились в апельсин
I["cafe-yakitoriya-elektrostal"] = ("доска детской мозаики с фишками-грибочками", "оранжевые фишки сложились в большой улыбающийся апельсин с листиком", ("#3A4A8A", "#1A2050"), f'''
<rect x="20" y="20" width="88" height="88" rx="12" fill="#F4F4FA" {W(3)}/>
{''.join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="#C0C4D8"/>' for x in range(28, 104, 12) for y in range(28, 104, 12))}
<circle cx="64" cy="70" r="30" fill="#FF8A1E" {W(3)}/>
{''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="#FFA545" {W(1.4)}/>' for x in range(28, 104, 12) for y in range(28, 104, 12) if (x-64)**2 + (y-70)**2 <= 24**2)}
<circle cx="52" cy="64" r="5.4" fill="{O}"/><circle cx="76" cy="64" r="5.4" fill="{O}"/><circle cx="50.5" cy="62" r="1.8" fill="#fff"/><circle cx="74.5" cy="62" r="1.8" fill="#fff"/>
<path d="M54 80 Q64 90 74 80" fill="none" stroke="{O}" stroke-width="3.6" stroke-linecap="round"/>
<path d="M64 40 Q70 28 84 30 Q78 42 64 40Z" fill="#3FBF5A" {W(2.4)}/>
<circle cx="112" cy="114" r="5" fill="#3A9AE8" {W(1.8)}/><circle cx="14" cy="112" r="5" fill="#FFD23A" {W(1.8)}/>''')

# 13. Bocconcino, Метрополис — кисточка аквагрима рисует бабочку на щеке
I["cafe-bocconcino-metropolis"] = ("кисточка аквагрима с глазками на ручке", "рисует малышу на щёчке голубую бабочку на детском празднике", ("#F5E0FF", "#B04AD8"), f'''
<path d="M10 128 Q12 104 50 100 Q88 104 90 128Z" fill="#3FBF8F" {W(3)}/>
<circle cx="50" cy="70" r="30" fill="{SK}" {W(3)}/>
<path d="M20 66 Q18 36 50 36 Q82 36 80 66 Q74 50 62 48 Q50 56 36 50 Q26 54 20 66Z" fill="#8A5A34" {W(2.6)}/>
{eye(40, 70, .7)}{eye(58, 70, .7)}<path d="M42 84 Q49 90 56 84" fill="none" {W(2.4)}/>
<path d="M66 82 Q60 72 66 70 Q70 72 70 80Z M72 80 Q78 70 82 74 Q82 80 72 82Z" fill="#4AB8F0" {W(1.8)}/>
<path d="M67 84 Q64 90 68 92 Q71 90 70 84Z M72 84 Q78 88 76 92 Q72 92 71 85Z" fill="#FF8FD0" {W(1.8)}/>
<path d="M70 78 V88" {W(2)}/>
<path d="M118 14 L80 74" stroke="#FFD23A" stroke-width="12" stroke-linecap="round"/><path d="M118 14 L80 74" fill="none" {W(1.6)}/>
<path d="M86 64 L78 77 L82 80 L90 68Z" fill="#C0C8D8" {W(2)}/>
<path d="M78 77 Q72 84 74 86 Q78 86 82 80Z" fill="#4AB8F0" {W(2)}/>
{eye(104, 36, .42)}{eye(110, 40, .42)}
{sparkle(104, 74, 5)}{sparkle(18, 28, 4)}''')

# 14. Osteria Mario, Метрополис — девочка на мастер-классе растягивает тесто
I["cafe-osteria-metropolis"] = ("девочка на мастер-классе в огромном белом фартуке до пят", "растягивает тесто для пиццы над головой, вокруг облачком летит мука", ("#FFDCCB", "#C8582E"), f'''
<path d="M38 128 L46 74 Q64 66 82 74 L90 128Z" fill="#fff" {W(3)}/>
<path d="M48 74 L44 62 M80 74 L84 62" {W(2.4)}/>
<rect x="56" y="98" width="16" height="12" rx="3" fill="#FFB8A0" {W(2)}/>
{limb("M50 78 L36 36", SK, 8)}{limb("M78 78 L92 36", SK, 8)}
{head(64, 56, 14, "#5A3A20", .5)}
<circle cx="50" cy="48" r="5" fill="#5A3A20" {W(2)}/><circle cx="78" cy="48" r="5" fill="#5A3A20" {W(2)}/>
<ellipse cx="64" cy="26" rx="36" ry="10" fill="#FFE9B8" {W(3)}/>
<ellipse cx="64" cy="24" rx="24" ry="5" fill="none" stroke="#E8C67A" stroke-width="2"/>
<circle cx="18" cy="40" r="6" fill="#fff" opacity=".9"/><circle cx="26" cy="30" r="4" fill="#fff" opacity=".9"/><circle cx="108" cy="46" r="6" fill="#fff" opacity=".9"/>
<circle cx="102" cy="58" r="3.5" fill="#fff" opacity=".9"/><circle cx="22" cy="56" r="3" fill="#fff" opacity=".9"/>''')

# 15. Osteria Mario, Кунцево Плаза — пуф-груша сплющился под малышом
I["cafe-osteria-kuntsevo-plaza"] = ("мягкий розовый пуф-груша", "малыш с разбегу плюхнулся в него, пуф сплющился и хохочет, ножки малыша торчат вверх", ("#D2FBF3", "#2E9A8A"), f'''
<path d="M0 112 H128 V128 H0Z" fill="#F2D3A0" {W(2.4)}/>
<path d="M14 112 Q8 78 40 68 Q56 58 64 68 Q76 58 90 66 Q120 76 114 112Z" fill="#FF7A9A" {W(3)}/>
<path d="M40 70 Q44 90 36 110 M90 68 Q86 90 94 110" fill="none" stroke="#E0507A" stroke-width="2.4"/>
{limb("M70 70 L92 44", SK, 8)}{limb("M76 72 L104 56", SK, 8)}
<ellipse cx="94" cy="40" rx="6" ry="5" fill="#3A7AE8" {W(2.2)}/><ellipse cx="108" cy="54" rx="6" ry="5" fill="#3A7AE8" {W(2.2)}/>
{limb("M56 70 L34 58", SK, 7)}
{head(60, 58, 12, "#2A2A3A", .45)}
{eye(46, 92, .7)}{eye(80, 92, .7)}<path d="M54 98 Q63 110 72 98Z" fill="{O}"/>{blush(36, 99, .6)}{blush(90, 99, .6)}
<path d="M10 66 l-6 -4 M116 70 l6 -4 M30 44 l-4 -6" {W(2.4)}/>''')

# 16. Osteria Mario, Крокус Сити — кукольная ширма с Пульчинеллой
I["cafe-osteria-crocus"] = ("Пульчинелла в белом колпаке и чёрной полумаске", "машет детям из окошка кукольной ширмы с полосатым занавесом", ("#F7D7C8", "#8A2030"), f'''
<rect x="20" y="40" width="88" height="92" fill="#E8403A" {W(3)}/>
<path d="M28 96 V128 M40 96 V128 M52 96 V128 M64 96 V128 M76 96 V128 M88 96 V128 M100 96 V128" stroke="#fff" stroke-width="5"/>
<path d="M16 40 H112 L112 46 Q106 54 100 46 Q94 54 88 46 Q82 54 76 46 Q70 54 64 46 Q58 54 52 46 Q46 54 40 46 Q34 54 28 46 Q22 54 16 46Z" fill="#FFD23A" {W(2.6)}/>
<rect x="34" y="54" width="60" height="38" rx="4" fill="#2A2E5A" {W(2.6)}/>
<path d="M50 92 Q64 74 78 92Z" fill="#fff" {W(2.6)}/>
<path d="M54 60 L64 14 L74 60Z" fill="#fff" {W(2.8)}/>
<circle cx="64" cy="68" r="12" fill="{SK}" {W(2.6)}/>
<path d="M52 66 Q64 58 76 66 L76 70 Q64 66 52 70Z" fill="#1A1A2A"/>
<circle cx="59" cy="67" r="2.4" fill="#fff"/><circle cx="69" cy="67" r="2.4" fill="#fff"/><circle cx="59" cy="67.4" r="1.2" fill="{O}"/><circle cx="69" cy="67.4" r="1.2" fill="{O}"/>
<path d="M59 74 Q64 78 69 74" fill="none" {W(2)}/>
{limb("M76 86 L92 62", "#fff", 8)}
<rect x="30" y="90" width="68" height="7" rx="3" fill="#FFD23A" {W(2.4)}/>''')

# 17. KLICH, ЗИЛАРТ — палитра художника в творческой зоне
I["cafe-klich-zilart"] = ("деревянная палитра художника с кляксами красок", "кисточка рисует на ней жёлтое солнышко в детской творческой зоне", ("#FFF1D8", "#D9A066"), f'''
<path d="M18 70 Q14 32 60 28 Q110 24 112 64 Q114 98 80 102 Q66 102 66 92 Q66 80 54 86 Q42 102 28 94 Q18 88 18 70Z" fill="#F2D3A0" {W(3)}/>
<ellipse cx="40" cy="74" rx="7" ry="6" fill="#D9A066" {W(2.4)}/>
<path d="M30 48 Q34 38 44 42 Q48 50 40 54 Q30 56 30 48Z" fill="#E8403A" {W(2.2)}/>
<path d="M52 38 Q58 30 66 36 Q68 44 58 46 Q50 44 52 38Z" fill="#3A7AE8" {W(2.2)}/>
<path d="M76 38 Q86 32 90 42 Q88 50 80 48 Q72 46 76 38Z" fill="#6CD06C" {W(2.2)}/>
<path d="M96 56 Q104 54 104 64 Q100 70 94 66 Q90 60 96 56Z" fill="#FF8FD0" {W(2.2)}/>
{eye(62, 64, .6)}{eye(78, 64, .6)}{smile(70, 71, 4, .8)}{blush(54, 71, .5)}{blush(86, 71, .5)}
<circle cx="88" cy="86" r="6" fill="#FFD23A" {W(2)}/><path d="M88 76 v-3 M98 86 h3 M88 96 v3 M78 86 h-3" stroke="#FFB800" stroke-width="2.4" stroke-linecap="round"/>
<path d="M124 126 L100 98" stroke="#C98547" stroke-width="7" stroke-linecap="round"/><path d="M124 126 L100 98" fill="none" {W(1.4)}/>
<path d="M102 100 L96 92 L100 89 L105 97Z" fill="#C0C8D8" {W(1.8)}/><path d="M96 92 Q92 86 94 84 Q98 85 100 89Z" fill="#FFD23A" {W(1.8)}/>''')

# 18. Hatimaki, Видное — малыш скачет на мяче-прыгуне с рожками
I["cafe-hatimaki-vidnoe"] = ("красный мяч-прыгун с рожками-ручками", "малыш верхом скачет на нём по детскому уголку, мяч подпрыгивает и улыбается", ("#EEFFC8", "#8CCB2E"), f'''
<ellipse cx="64" cy="118" rx="26" ry="4" fill="#000" opacity=".15"/>
<path d="M30 116 Q34 112 38 116 M90 116 Q94 112 98 116" fill="none" {W(2)}/>
{limb("M50 62 Q44 50 50 40", "#E8304A", 8)}{limb("M78 62 Q84 50 78 40", "#E8304A", 8)}
<circle cx="64" cy="82" r="28" fill="#FF5A7A" {W(3)}/>
<path d="M44 70 Q50 60 60 58" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
{eye(54, 86, .6)}{eye(74, 86, .6)}{smile(64, 93, 5, .9)}{blush(46, 93, .5)}{blush(82, 93, .5)}
<path d="M54 56 Q64 50 74 56 L72 40 H56Z" fill="#FFD23A" {W(2.6)}/>
{limb("M58 58 L40 72", SK, 7)}{limb("M70 58 L88 72", SK, 7)}
{limb("M56 44 L50 40", SK, 6)}{limb("M72 44 L78 40", SK, 6)}
{head(64, 28, 11, "#3A2A20", .42)}
<path d="M30 30 l-6 -4 M98 30 l6 -4" {W(2.2)}/>''')

# 19. Hatimaki, Кузнечики — половинки кацу-сэндо дают «пять»
I["cafe-hatimaki-podolsk-kuznechiki"] = ("японский сэндвич кацу-сэндо, разрезанный на две половинки", "половинки встают на ножки и весело дают друг другу «пять»", ("#FFE8E0", "#D88A7A"), f'''
<ellipse cx="64" cy="110" rx="50" ry="6" fill="#fff" {W(2.4)}/>
<rect x="14" y="50" width="42" height="56" rx="7" fill="#FFF8EA" {W(3)}/>
<rect x="14" y="68" width="42" height="18" fill="#D88A3A" {W(2.6)}/><path d="M14 68 H56" stroke="#7CD26E" stroke-width="3"/>
<circle cx="22" cy="76" r="1.4" fill="#A85A20"/><circle cx="34" cy="80" r="1.4" fill="#A85A20"/><circle cx="46" cy="75" r="1.4" fill="#A85A20"/>
{eye(28, 58, .5)}{eye(42, 58, .5)}<path d="M32 63 Q35 66 38 63" fill="none" {W(1.8)}/>
<rect x="72" y="50" width="42" height="56" rx="7" fill="#FFF8EA" {W(3)}/>
<rect x="72" y="68" width="42" height="18" fill="#D88A3A" {W(2.6)}/><path d="M72 68 H114" stroke="#7CD26E" stroke-width="3"/>
<circle cx="80" cy="76" r="1.4" fill="#A85A20"/><circle cx="92" cy="80" r="1.4" fill="#A85A20"/><circle cx="104" cy="75" r="1.4" fill="#A85A20"/>
{eye(86, 58, .5)}{eye(100, 58, .5)}<path d="M90 63 Q93 66 96 63" fill="none" {W(1.8)}/>
{limb("M54 58 Q60 42 62 32", "#FFF8EA", 7)}{limb("M74 58 Q68 42 66 32", "#FFF8EA", 7)}
{sparkle(64, 22, 7, "#FFF3A0")}<path d="M52 22 l-6 -2 M76 22 l6 -2 M64 10 v-5" {W(2)}/>''')

# 20. Hatimaki, Коммунарка — малыш качается на доске-балансире
I["cafe-hatimaki-kommunarka"] = ("деревянная доска-балансир дугой", "малыш раскинул руки и раскачивается на ней, как на волне", ("#F0EAFF", "#9A8AD0"), f'''
<path d="M6 106 Q20 100 34 106 T62 106 T90 106 T118 106" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
<path d="M12 70 Q64 120 116 70 L116 80 Q64 130 12 80Z" fill="#E7A85A" {W(3)}/>
<path d="M28 88 Q64 112 100 88" fill="none" stroke="#C98547" stroke-width="2"/>
{eye(36, 91, .45)}{eye(92, 91, .45)}<path d="M58 103 Q64 106 70 103" fill="none" {W(1.8)}/>
{limb("M58 96 L60 74", SK, 8)}{limb("M70 96 L68 74", SK, 8)}
<path d="M50 50 Q64 46 78 50 L76 78 H52Z" fill="#3FBF8F" {W(2.8)}/>
{limb("M54 56 L26 46", SK, 7)}{limb("M74 56 L102 50", SK, 7)}
{head(64, 38, 12, "#E8C24A", .45)}
<path d="M18 40 l-6 -3 M110 42 l6 -3" {W(2.2)}/>''')

# 21. La Riva — магнитная рыбка на детской удочке
I["cafe-la-riva"] = ("красная магнитная рыбка-игрушка на детской удочке", "малыш вылавливает её из игрушечного пруда в ресторане у реки, рыбка улыбается", ("#D8FBF8", "#2FA8B8"), f'''
<ellipse cx="72" cy="102" rx="48" ry="16" fill="#4AB8F0" {W(3)}/>
<ellipse cx="72" cy="102" rx="38" ry="10" fill="none" stroke="#fff" stroke-width="2" opacity=".8"/>
<path d="M56 98 l8 -3 l0 6Z" fill="#FFD23A" {W(1.6)}/><path d="M86 104 l-8 -3 l0 6Z" fill="#6CD06C" {W(1.6)}/>
{limb("M26 78 L28 104", SK, 7)}<path d="M18 64 Q28 58 38 64 L38 88 H18Z" fill="#FFD23A" {W(2.6)}/>
{head(28, 50, 11, "#8A5A34", .42)}
{limb("M34 70 L48 60", SK, 7)}
<path d="M46 62 L84 18" stroke="#3A7AE8" stroke-width="4" stroke-linecap="round"/>
<path d="M84 18 Q96 26 94 48" fill="none" stroke="{O}" stroke-width="1.6"/>
<path d="M78 62 Q94 46 110 62 Q94 78 78 62Z" fill="#E8403A" {W(2.8)}/>
<path d="M110 62 L120 54 L120 70Z" fill="#E8403A" {W(2.4)}/>
<circle cx="94" cy="52" r="3.4" fill="#C0C8D8" {W(1.8)}/>
{eye(88, 60, .45)}<path d="M82 66 Q85 68 87 66" fill="none" {W(1.6)}/>
<path d="M98 82 Q100 76 104 80" fill="none" stroke="#fff" stroke-width="2"/>''')

# 22. Трамплин / Амбассадори — сушка в лыжных очках летит с трамплина
I["cafe-tramplin-ambassadori"] = ("румяная сушка с маком в лыжных очках", "летит на маленьких лыжах с трамплина на Воробьёвых горах", ("#E8F6FF", "#5AA0E0"), f'''
<path d="M-4 66 L50 108 L50 128 L-4 128Z" fill="#fff" {W(2.6)}/>
<path d="M-4 74 L44 112" stroke="#9DD6F5" stroke-width="2"/>
<path d="M18 30 h-12 M22 42 h-16 M28 54 h-10" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M54 92 L112 76 Q118 74 118 70" fill="none" stroke="#E8403A" stroke-width="5" stroke-linecap="round"/>
<path d="M56 100 L114 84 Q120 82 120 78" fill="none" stroke="#E8403A" stroke-width="5" stroke-linecap="round"/>
<circle cx="82" cy="54" r="28" fill="#E8A24A" {W(3)}/>
<circle cx="82" cy="50" r="9" fill="#C3E2FA" {W(2.6)}/>
<circle cx="64" cy="44" r="1.2" fill="{O}"/><circle cx="70" cy="34" r="1.2" fill="{O}"/><circle cx="92" cy="32" r="1.2" fill="{O}"/><circle cx="102" cy="44" r="1.2" fill="{O}"/><circle cx="104" cy="58" r="1.2" fill="{O}"/>
<path d="M58 66 Q82 74 106 66" fill="none" stroke="#3A3A5A" stroke-width="3"/>
<rect x="64" y="60" width="16" height="11" rx="5" fill="#FF9A3C" {W(2.2)}/><rect x="84" y="60" width="16" height="11" rx="5" fill="#FF9A3C" {W(2.2)}/>
{eye(72, 65.5, .4)}{eye(92, 65.5, .4)}
<path d="M76 76 Q82 80 88 76" fill="none" {W(2)}/>
{sparkle(30, 92, 4)}''')

# 23. Shagal, Таганка — ретро-телевизор с мультиком
I["cafe-shagal-taganka"] = ("пузатый ретро-телевизор на ножках с усами-антенной", "показывает мультик про прыгающего зайчика, у экрана на коврике сидит малыш", ("#FFE6C2", "#E8873A"), f'''
<path d="M60 30 L42 10 M68 30 L86 10" {W(2.6)}/><circle cx="42" cy="10" r="3" fill="{O}"/><circle cx="86" cy="10" r="3" fill="{O}"/>
<path d="M36 92 L32 104 M92 92 L96 104" {W(3.4)}/>
<rect x="20" y="28" width="88" height="66" rx="14" fill="#C98547" {W(3)}/>
<rect x="28" y="36" width="58" height="50" rx="10" fill="#8FE0FF" {W(2.6)}/>
<circle cx="98" cy="50" r="4.5" fill="#FFD23A" {W(2)}/><circle cx="98" cy="68" r="4.5" fill="#FFD23A" {W(2)}/>
<path d="M30 80 Q46 54 60 72" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="2 3"/>
<ellipse cx="62" cy="62" rx="10" ry="9" fill="#fff" {W(2.2)}/><ellipse cx="57" cy="47" rx="3" ry="8" fill="#fff" {W(2)}/><ellipse cx="66" cy="47" rx="3" ry="8" fill="#fff" {W(2)}/>
{eye(58, 61, .35)}{eye(66, 61, .35)}<circle cx="62" cy="66" r="1.4" fill="#FF7FA8"/>
<ellipse cx="64" cy="122" rx="50" ry="10" fill="#3FBF8F" {W(2.4)}/>
<circle cx="64" cy="110" r="14" fill="#5A3A20" {W(2.8)}/><circle cx="50" cy="112" r="3.4" fill="{SK}" {W(2)}/><circle cx="78" cy="112" r="3.4" fill="{SK}" {W(2)}/>''')

# 24. Шу-Шу, ТЦ «Азовский» — книжка-раскраска с рыбкой
I["cafe-shu-shu-azovsky"] = ("раскрытая детская книжка-раскраска с морской рыбкой", "синий карандаш докрашивает рыбке полоски, рыбка наполовину уже цветная и улыбается", ("#F4FBD8", "#B8D85A"), f'''
<path d="M10 46 Q38 38 64 48 V108 Q38 98 10 106Z" fill="#fff" {W(3)}/>
<path d="M118 46 Q90 38 64 48 V108 Q90 98 118 106Z" fill="#fff" {W(3)}/>
<path d="M30 76 L16 64 L16 90Z" fill="#fff" {W(2.4)}/>
<path d="M30 76 Q50 54 74 58 V96 Q50 98 30 76Z" fill="#fff" {W(2.6)}/>
<path d="M74 58 Q96 60 104 76 Q96 94 74 96Z" fill="#3A9AE8" {W(2.6)}/>
<path d="M82 60 V95 M92 64 V90" stroke="#FFD23A" stroke-width="3"/>
<path d="M50 62 V92 M60 58 V96" fill="none" {W(1.6)}/>
{eye(92, 72, .55)}<path d="M96 82 Q99 84 102 81" fill="none" {W(1.8)}/>
<g transform="rotate(35 92 30)"><rect x="86" y="-4" width="12" height="40" fill="#3A7AE8" {W(2.4)}/><rect x="86" y="-10" width="12" height="8" rx="2" fill="#FF8FB0" {W(2.2)}/><path d="M86 36 L92 48 L98 36Z" fill="#FFE2B8" {W(2.2)}/><path d="M90 44 L92 48 L94 44Z" fill="#3A7AE8"/></g>''')

# 25. Casa di famiglia — итальянская бабушка-нонна с миской макарон
I["cafe-casa-famiglia-pervomayskaya"] = ("итальянская бабушка-нонна с седым пучком и в круглых очках", "с улыбкой несёт малышам огромную миску макарон, от неё идёт пар", ("#FFE0E6", "#E0607A"), f'''
<path d="M18 128 Q20 94 64 90 Q108 94 110 128Z" fill="#7A4AA8" {W(3)}/>
<path d="M40 92 L64 112 L88 92" fill="none" stroke="#FFD23A" stroke-width="3"/>
<circle cx="64" cy="54" r="21" fill="{SK}" {W(3)}/>
<path d="M42 52 Q42 30 64 30 Q86 30 86 52 Q80 38 64 40 Q48 38 42 52Z" fill="#D8D8E0" {W(2.6)}/>
<circle cx="64" cy="24" r="9" fill="#D8D8E0" {W(2.6)}/>
<circle cx="56" cy="56" r="6.5" fill="#fff" fill-opacity=".5" {W(2)}/><circle cx="72" cy="56" r="6.5" fill="#fff" fill-opacity=".5" {W(2)}/><path d="M62.5 56 H65.5" {W(2)}/>
{eye(56, 56, .45)}{eye(72, 56, .45)}
<path d="M58 66 Q64 71 70 66" fill="none" {W(2.2)}/>{blush(48, 65, .55)}{blush(80, 65, .55)}
<path d="M30 92 Q64 84 98 92 L92 114 Q64 122 36 114Z" fill="#fff" {W(3)}/>
<path d="M34 92 Q40 78 52 84 Q58 74 68 82 Q78 74 86 84 Q96 80 96 92Z" fill="#FFD25E" {W(2.4)}/>
<path d="M44 88 Q50 82 56 88 M62 86 Q68 80 74 86 M78 88 Q84 82 90 88" fill="none" stroke="#E0A030" stroke-width="2"/>
<circle cx="64" cy="82" r="3.6" fill="#E8403A" {W(1.6)}/>
<path d="M50 74 Q46 68 50 62 M78 74 Q82 68 78 62" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 26. Нияма, ТЦ «Водный» — ролл-мишка на надувном круге
I["cafe-niyama-vodny"] = ("круглый кавай-ролл с мордочкой мишки в обёртке из нори", "плавает в бассейне на розовом надувном круге", ("#D8F0FF", "#3A88D8"), f'''
<path d="M0 86 Q32 80 64 86 T128 86 V128 H0Z" fill="#7FD0F8" {W(2.4)}/>
<ellipse cx="64" cy="94" rx="44" ry="15" fill="#FF8FB0" {W(3)}/>
<path d="M28 88 L36 104 M64 79 V109 M100 88 L92 104" stroke="#fff" stroke-width="7"/>
<ellipse cx="64" cy="94" rx="44" ry="15" fill="none" {W(3)}/>
<circle cx="64" cy="56" r="30" fill="#2A3A2A" {W(3)}/>
<circle cx="64" cy="56" r="24" fill="#fff"/>
<circle cx="50" cy="44" r="7" fill="#B8783A" {W(2)}/><circle cx="78" cy="44" r="7" fill="#B8783A" {W(2)}/>
<circle cx="64" cy="58" r="15" fill="#B8783A" {W(2.4)}/>
<ellipse cx="64" cy="64" rx="7" ry="5" fill="#F2D3A0"/>
{eye(58, 55, .45)}{eye(70, 55, .45)}<ellipse cx="64" cy="62" rx="2.4" ry="1.8" fill="{O}"/>
<path d="M14 108 Q18 104 22 108 M104 112 Q108 108 112 112" fill="none" stroke="#fff" stroke-width="2"/>''')

# 27. Кавказский дворик — нарды, выпало «шеш-беш»
I["cafe-kavkazsky-dvorik"] = ("раскрытая доска для нард с шашками", "на зарики выпало «шеш-беш», и доска довольно улыбается", ("#FFEED8", "#B8783A"), f'''
<rect x="12" y="26" width="104" height="76" rx="7" fill="#A8642A" {W(3)}/>
<rect x="18" y="32" width="42" height="54" rx="2" fill="#F2D3A0" {W(2)}/><rect x="68" y="32" width="42" height="54" rx="2" fill="#F2D3A0" {W(2)}/>
<path d="M18 32 l3.5 20 l3.5 -20Z M32 32 l3.5 20 l3.5 -20Z M46 32 l3.5 20 l3.5 -20Z M68 32 l3.5 20 l3.5 -20Z M82 32 l3.5 20 l3.5 -20Z M96 32 l3.5 20 l3.5 -20Z" fill="#C8302A"/>
<path d="M25 32 l3.5 20 l3.5 -20Z M39 32 l3.5 20 l3.5 -20Z M53 32 l3.5 20 l3.5 -20Z M75 32 l3.5 20 l3.5 -20Z M89 32 l3.5 20 l3.5 -20Z M103 32 l3.5 20 l3.5 -20Z" fill="#5A3A20"/>
<path d="M18 86 l3.5 -20 l3.5 20Z M32 86 l3.5 -20 l3.5 20Z M46 86 l3.5 -20 l3.5 20Z M68 86 l3.5 -20 l3.5 20Z M82 86 l3.5 -20 l3.5 20Z M96 86 l3.5 -20 l3.5 20Z" fill="#5A3A20"/>
<path d="M25 86 l3.5 -20 l3.5 20Z M39 86 l3.5 -20 l3.5 20Z M53 86 l3.5 -20 l3.5 20Z M75 86 l3.5 -20 l3.5 20Z M89 86 l3.5 -20 l3.5 20Z M103 86 l3.5 -20 l3.5 20Z" fill="#C8302A"/>
<circle cx="28" cy="38" r="5" fill="#fff" {W(1.8)}/><circle cx="28" cy="48" r="5" fill="#fff" {W(1.8)}/><circle cx="100" cy="80" r="5" fill="#2A2A3A" {W(1.8)}/><circle cx="100" cy="70" r="5" fill="#2A2A3A" {W(1.8)}/>
{eye(52, 94, .5)}{eye(76, 94, .5)}<path d="M60 96 Q64 99 68 96" fill="none" {W(1.8)}/>
<rect x="34" y="102" width="20" height="20" rx="4" fill="#fff" transform="rotate(-12 44 112)" {W(2.4)}/>
<g transform="rotate(-12 44 112)"><circle cx="39" cy="106" r="1.8" fill="{O}"/><circle cx="39" cy="112" r="1.8" fill="{O}"/><circle cx="39" cy="118" r="1.8" fill="{O}"/><circle cx="49" cy="106" r="1.8" fill="{O}"/><circle cx="49" cy="112" r="1.8" fill="{O}"/><circle cx="49" cy="118" r="1.8" fill="{O}"/></g>
<rect x="72" y="100" width="20" height="20" rx="4" fill="#fff" transform="rotate(14 82 110)" {W(2.4)}/>
<g transform="rotate(14 82 110)"><circle cx="77" cy="105" r="1.8" fill="{O}"/><circle cx="87" cy="105" r="1.8" fill="{O}"/><circle cx="82" cy="110" r="1.8" fill="{O}"/><circle cx="77" cy="115" r="1.8" fill="{O}"/><circle cx="87" cy="115" r="1.8" fill="{O}"/></g>''')

# 28. Fun Fam, Стромынка — песочница с замком
I["cafe-fun-fam-stromynka"] = ("деревянная песочница в детской комнате ресторана", "в ней стоит песочный замок с флажком, малыш прихлопывает его ладошкой", ("#FFF2F8", "#E07AB0"), f'''
<path d="M14 92 Q64 80 114 92 L114 100 H14Z" fill="#F7D774" {W(2.4)}/>
<rect x="28" y="62" width="14" height="30" fill="#E8C25A" {W(2.6)}/><path d="M28 62 v-5 h4 v5 M36 62 v-5 h4 v5" fill="#E8C25A" {W(2)}/>
<rect x="42" y="46" width="30" height="46" fill="#F0CE66" {W(2.8)}/>
<path d="M42 46 v-6 h6 v6 h6 v-6 h6 v6 h6 v-6 h6 v6" fill="#F0CE66" {W(2.4)}/>
<path d="M52 92 V80 Q57 74 62 80 V92Z" fill="#C98547" {W(2.2)}/>
{eye(51, 60, .45)}{eye(63, 60, .45)}<path d="M54 67 Q57 70 60 67" fill="none" {W(1.8)}/>
<path d="M57 40 V20" {W(2.4)}/><path d="M57 20 L72 25 L57 30Z" fill="#E8403A" {W(2)}/>
<rect x="10" y="98" width="108" height="16" rx="4" fill="#C98547" {W(3)}/><path d="M38 98 V114 M64 98 V114 M90 98 V114" stroke="#A8642A" stroke-width="2"/>
{limb("M90 74 L76 64", SK, 7)}<path d="M84 72 Q96 66 106 72 L106 98 H86Z" fill="#3A9AE8" {W(2.6)}/>
{head(96, 56, 11, "#E0A030", .42)}''')

# 29. Нияма, Севастопольский — магнитная доска с буквами «МАМА»
I["cafe-niyama-sevastopolsky"] = ("магнитная доска на ножках с глазками", "цветные буквы-магниты сложились на ней в слово «МАМА»", ("#E0E8F2", "#6A80A8"), f'''
<path d="M30 92 L22 124 M98 92 L106 124" {W(4)}/>
<rect x="14" y="26" width="100" height="68" rx="8" fill="#F8FAFF" stroke="#3A6AD8" stroke-width="7"/>
<rect x="14" y="26" width="100" height="68" rx="8" fill="none" {W(2.4)}/>
{eye(52, 42, .55)}{eye(76, 42, .55)}{smile(64, 49, 4, .8)}{blush(44, 49, .5)}{blush(84, 49, .5)}
<path d="M22 84 V62 L28 72 L34 62 V84" fill="none" stroke="#E8403A" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
<path d="M42 84 L48 62 L54 84 M44.5 77 H51.5" fill="none" stroke="#FFB800" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
<path d="M62 84 V62 L68 72 L74 62 V84" fill="none" stroke="#3FBF5A" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
<path d="M82 84 L88 62 L94 84 M84.5 77 H91.5" fill="none" stroke="#3A7AE8" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
<path d="M100 66 l6 -4 M102 76 h7" {W(2)}/>{sparkle(108, 16, 5)}''')

# 30. Терраса, Лианозово — гренка загорает на шезлонге
I["cafe-terrasa-lianozovo"] = ("французская гренка с сахарной пудрой и ягодкой", "загорает в панамке на полосатом шезлонге летней террасы", ("#FFF8D0", "#FFB03A"), f'''
<circle cx="104" cy="24" r="12" fill="#FFE04A" {W(2.4)}/>
<path d="M0 72 H128" {W(3)}/><path d="M8 72 V104 M24 72 V104 M104 72 V104 M120 72 V104" {W(2.4)}/>
<path d="M0 104 H128 V128 H0Z" fill="#C98547" {W(2.4)}/>
<path d="M30 120 L46 50 M98 120 L84 76 M40 96 H92" {W(4)}/>
<path d="M44 40 L70 34 L102 104 L76 110Z" fill="#fff" {W(2.8)}/>
<path d="M51 38.5 L83 107 M63 36 L95 105" stroke="#3AA8E8" stroke-width="5"/>
<path d="M44 40 L70 34 L102 104 L76 110Z" fill="none" {W(2.8)}/>
<g transform="rotate(-14 62 80)">
<path d="M40 112 V70 Q28 66 32 52 Q38 38 64 38 Q90 38 96 52 Q100 66 88 70 V112Z" fill="#E8B04A" {W(3)}/>
<path d="M45 108 V68 Q36 64 38 54 Q44 44 64 44 Q84 44 90 54 Q92 64 83 68 V108Z" fill="#F7D98A"/>
<circle cx="50" cy="60" r="1.6" fill="#fff"/><circle cx="62" cy="54" r="1.6" fill="#fff"/><circle cx="76" cy="58" r="1.6" fill="#fff"/><circle cx="56" cy="96" r="1.6" fill="#fff"/><circle cx="74" cy="98" r="1.6" fill="#fff"/>
{eye(56, 74, .6)}{eye(72, 74, .6)}{smile(64, 82, 4, .8)}{blush(48, 82, .5)}{blush(80, 82, .5)}
<circle cx="86" cy="96" r="6" fill="#E8304A" {W(2.2)}/>
<path d="M30 44 Q34 34 64 32 Q94 34 98 44 Q64 50 30 44Z" fill="#fff" {W(2.6)}/>
<path d="M44 40 Q46 22 64 22 Q82 22 84 40Z" fill="#fff" {W(2.6)}/><path d="M45 36 Q64 40 83 36" fill="none" stroke="#F58CB8" stroke-width="3.4"/>
</g>''')

# 31. Хуан Хэ, Сокол — красный китайский фонарь
I["cafe-huan-he-sokol"] = ("красный китайский бумажный фонарь с золотой кисточкой", "светится над детской комнатой, малыш тянется к его кисточке", ("#6A3A9A", "#2A1050"), f'''
<circle cx="64" cy="52" r="44" fill="#FFD23A" opacity=".18"/>
<path d="M64 0 V20" {W(2.4)}/>
<rect x="50" y="18" width="28" height="8" rx="3" fill="#FFD23A" {W(2.4)}/>
<ellipse cx="64" cy="52" rx="34" ry="28" fill="#E8302A" {W(3)}/>
<ellipse cx="64" cy="52" rx="20" ry="28" fill="none" stroke="#B81E1A" stroke-width="2"/><path d="M64 24 V80" stroke="#B81E1A" stroke-width="2"/>
<rect x="50" y="78" width="28" height="8" rx="3" fill="#FFD23A" {W(2.4)}/>
<path d="M60 86 L58 110 M64 86 V112 M68 86 L70 110" stroke="#FFB800" stroke-width="3" stroke-linecap="round"/>
{eye(52, 50, .6)}{eye(76, 50, .6)}{smile(64, 58, 4, .8)}{blush(44, 58, .5)}{blush(84, 58, .5)}
{limb("M30 112 L52 104", SK, 7)}
<path d="M10 128 Q12 108 28 106 Q40 108 42 128Z" fill="#3FBF8F" {W(2.6)}/>
{head(24, 96, 10, "#2A2A3A", .4)}
{sparkle(108, 20, 4, "#FFF3A0")}{sparkle(18, 30, 3, "#FFF3A0")}''')

# 32. Нияма, Гренада — японский креп-рожок как букет
I["cafe-niyama-grenada-lyubertsy"] = ("японский креп-рожок со взбитыми сливками и клубникой в бумажном кульке", "малыш держит его как букет за столиком детской зоны", ("#FFF0F5", "#C83A6A"), f'''
<path d="M64 120 L28 56 Q64 44 100 56Z" fill="#FFD9E6" {W(3)}/>
<path d="M40 76 L88 76 M48 92 L80 92 M56 106 L72 106" stroke="#F58CB8" stroke-width="3"/>
<path d="M28 56 Q30 46 38 50 Q44 42 52 48 Q60 40 68 46 Q76 40 82 48 Q92 44 94 52 Q100 50 100 56" fill="#F7D07A" {W(2.6)}/>
<circle cx="44" cy="40" r="10" fill="#fff" {W(2.4)}/><circle cx="62" cy="34" r="12" fill="#fff" {W(2.4)}/><circle cx="82" cy="40" r="10" fill="#fff" {W(2.4)}/>
<path d="M44 30 Q50 18 56 30 Q50 36 44 30Z" fill="#E8304A" {W(2)}/><path d="M72 30 Q78 18 84 30 Q78 36 72 30Z" fill="#E8304A" {W(2)}/>
<path d="M64 26 L80 6" stroke="#6A3A20" stroke-width="5" stroke-linecap="round"/>
{eye(56, 66, .55)}{eye(72, 66, .55)}{smile(64, 72, 3.5, .8)}{blush(48, 72, .45)}{blush(80, 72, .45)}
{limb("M22 128 L56 104", SK, 9)}<circle cx="58" cy="104" r="7" fill="{SK}" {W(2.4)}/>''')

# 33. Пекорино, Косино — головка сыра-овечка пасётся у озера
I["cafe-pekorino-kosino"] = ("головка овечьего сыра пекорино с овечьими ушками и кудряшками", "пасётся на зелёном лугу у Косинского озера с травинкой во рту", ("#E9F8FF", "#7EC6E8"), f'''
<ellipse cx="96" cy="74" rx="34" ry="8" fill="#4AA8E8" {W(2.4)}/>
<path d="M0 80 Q64 72 128 80 V128 H0Z" fill="#7CD26E" {W(2.4)}/>
<path d="M44 96 V112 M56 98 V114 M74 98 V114 M86 96 V112" {W(5)}/>
<path d="M26 58 V86 Q64 100 102 86 V58Z" fill="#F2D27A" {W(3)}/>
<ellipse cx="64" cy="58" rx="38" ry="12" fill="#FFF0B0" {W(3)}/>
<circle cx="50" cy="52" r="5" fill="#fff" {W(2)}/><circle cx="60" cy="48" r="5.5" fill="#fff" {W(2)}/><circle cx="72" cy="49" r="5" fill="#fff" {W(2)}/>
<ellipse cx="20" cy="64" rx="10" ry="5" fill="#E8C29A" transform="rotate(25 20 64)" {W(2.4)}/>
<ellipse cx="108" cy="64" rx="10" ry="5" fill="#E8C29A" transform="rotate(-25 108 64)" {W(2.4)}/>
{eye(52, 74, .6)}{eye(76, 74, .6)}<path d="M60 84 Q64 87 68 84" fill="none" {W(2)}/>{blush(42, 82, .5)}{blush(86, 82, .5)}
<path d="M68 85 L80 80" stroke="#3FA03A" stroke-width="2.6" stroke-linecap="round"/>
<path d="M12 104 l3 -8 l3 8 M110 108 l3 -8 l3 8" fill="none" stroke="#3FA03A" stroke-width="2.4"/>''')

# 34. Ганс и Марта, Новокосино — бизиборд, загорается лампочка
I["cafe-gans-i-marta-novokosino"] = ("деревянный бизиборд с шестерёнками, выключателем и лампочкой", "малыш щёлкает выключателем — лампочка зажигается, бизиборд радуется", ("#DDF4EC", "#4A8A6A"), f'''
<rect x="16" y="20" width="92" height="90" rx="10" fill="#F5C877" {W(3)}/>
<path d="M16 50 H108 M16 80 H108" stroke="#E0A860" stroke-width="1.6"/>
{eye(40, 38, .6)}{eye(60, 38, .6)}{smile(50, 45, 4, .8)}
<circle cx="88" cy="40" r="15" fill="#FFF3A0" opacity=".7"/>
<circle cx="88" cy="38" r="9" fill="#FFE04A" {W(2.4)}/><rect x="84" y="46" width="8" height="6" rx="1.5" fill="#C0C8D8" {W(2)}/>
<path d="M88 22 v-4 M100 30 l3 -3 M76 30 l-3 -3" stroke="#FFB800" stroke-width="2.4" stroke-linecap="round"/>
<path d="M28 82 l3 -6 l5 2 l2 -6 l6 3 l4 -5 l4 5 l6 -3 l2 6 l5 -2 l3 6 l-3 6 l3 6 l-3 6 l-5 -2 l-2 6 l-6 -3 l-4 5 l-4 -5 l-6 3 l-2 -6 l-5 2 l-3 -6 l3 -6Z" fill="#E8403A" {W(2.2)}/>
<circle cx="43" cy="88" r="5" fill="#F5C877" {W(2)}/>
<circle cx="64" cy="98" r="9" fill="#3A7AE8" {W(2.2)}/><circle cx="64" cy="98" r="3" fill="#F5C877" {W(1.6)}/>
<rect x="80" y="62" width="18" height="28" rx="4" fill="#fff" {W(2.4)}/><rect x="85" y="66" width="8" height="10" rx="2" fill="#3FBF5A" {W(1.8)}/>
{limb("M124 104 L96 76", SK, 8)}''')

# 35. Нияма, ТЦ «Шоколад» — шоколадный заяц в золотой фольге
I["cafe-niyama-shokolad-reutov"] = ("шоколадный заяц в золотой фольге с красным бантиком", "стоит на задних лапках и машет, фольга блестит", ("#7A4A30", "#3A2010"), f'''
<ellipse cx="64" cy="118" rx="30" ry="5" fill="#000" opacity=".25"/>
<ellipse cx="52" cy="26" rx="7" ry="20" fill="#E8B83A" transform="rotate(-10 52 26)" {W(2.8)}/>
<ellipse cx="76" cy="26" rx="7" ry="20" fill="#E8B83A" transform="rotate(10 76 26)" {W(2.8)}/>
<ellipse cx="64" cy="92" rx="26" ry="26" fill="#E8B83A" {W(3)}/>
<circle cx="64" cy="54" r="19" fill="#E8B83A" {W(3)}/>
<path d="M50 84 L58 92 L52 100 M74 80 L80 92" fill="none" stroke="#FFF3A0" stroke-width="2" stroke-linecap="round"/>
<path d="M54 44 L58 40 M74 46 L78 50" stroke="#FFF3A0" stroke-width="2" stroke-linecap="round"/>
{eye(57, 54, .55)}{eye(71, 54, .55)}<path d="M60 63 Q64 66 68 63" fill="none" {W(2)}/>{blush(50, 62, .45)}{blush(78, 62, .45)}
<path d="M64 74 L52 68 L52 80Z M64 74 L76 68 L76 80Z" fill="#E8304A" {W(2.2)}/><circle cx="64" cy="74" r="3" fill="#E8304A" {W(2)}/>
{limb("M86 84 L104 64", "#E8B83A", 9)}
{sparkle(104, 42, 5, "#FFE07A")}{sparkle(26, 70, 4, "#FFE07A")}''')

# 36. Эль Гаучито, «Времена года» — эмпанада в шляпе гаучо на палочке-лошадке
I["cafe-el-gauchito-vremena-goda"] = ("аргентинская эмпанада с косичкой-защипом в шляпе гаучо", "скачет по залу на палочке-лошадке", ("#FFF0C8", "#C8A23A"), f'''
<path d="M0 112 H128 V128 H0Z" fill="#B87A3A" {W(2.4)}/>
<path d="M18 124 L94 40" stroke="#C98547" stroke-width="6" stroke-linecap="round"/><path d="M18 124 L94 40" fill="none" {W(1.4)}/>
<path d="M88 46 Q86 28 100 22 Q112 20 118 30 L114 36 Q106 32 104 42 Z" fill="#8A5A34" {W(2.6)}/>
<path d="M90 30 Q92 18 100 18" fill="none" stroke="#3A2A20" stroke-width="5" stroke-linecap="round"/>
<circle cx="104" cy="28" r="1.8" fill="{O}"/>
{limb("M44 96 L38 112", "#E8A84A", 7)}{limb("M66 96 L74 112", "#E8A84A", 7)}
<path d="M18 92 Q54 34 92 92Z" fill="#E8A84A" {W(3)}/>
<path d="M24 86 Q54 40 86 86" fill="none" stroke="#C8782A" stroke-width="2.2" stroke-dasharray="4 3"/>
{eye(46, 76, .55)}{eye(62, 76, .55)}{smile(54, 83, 3.5, .8)}{blush(38, 82, .45)}{blush(70, 82, .45)}
<ellipse cx="54" cy="52" rx="26" ry="5" fill="#2B2B3A" {W(2.4)}/>
<path d="M42 51 V40 H66 V51Z" fill="#2B2B3A" {W(2.4)}/><path d="M42 47 H66" stroke="#E8403A" stroke-width="2.6"/>
{limb("M70 74 L80 60", "#E8A84A", 7)}''')


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
