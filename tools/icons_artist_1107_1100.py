"""Робот «художник», 07.11 ~11:00 UTC: 40 иконок из самых похожих пар auto/icon-repeats.json
(старые серии «блюдо × шляпа фокусника / батутик / карусель / клетчатая скатерть», «зверь плывёт по дорожке»,
«персонаж-инвентарь в короне / шапке выпускника»). Из каждой пары одну оставили, вторую придумали заново
и нарисовали вручную: свой герой по теме места, своя сцена, ракурс и палитра.
Запуск из корня: python3 tools/icons_artist_1107_1100.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT

I = {}


def limb(d, color="#FFD8B8", w=6):
    return f'<path d="{d}" fill="none" {W(w)}/><path d="{d}" fill="none" stroke="{color}" stroke-width="{w-3.4:.1f}" stroke-linecap="round"/>'


# 1. «Лето» (Раменское) — солнышко пьёт морс через длинную трубочку
I["cafe-leto-ramenskoe"] = ("стакан красного ягодного морса со льдом", "летнее солнышко тянет из него морс через длинную полосатую трубочку", ("#FFF6C8", "#F0A030"), f'''
<circle cx="32" cy="34" r="19" fill="#FFD23A" {W(3)}/>
<path d="M32 8 V2 M8 34 H2 M14 16 L9 11 M50 16 L55 11 M14 52 L9 57" stroke="#FFB020" stroke-width="4" stroke-linecap="round"/>
{eye(26, 31, .5)}{eye(38, 31, .5)}{blush(22, 38, .45)}<circle cx="40" cy="40" r="3" fill="{O}"/>
<path d="M40 40 Q62 26 86 50" fill="none" {W(6)}/><path d="M40 40 Q62 26 86 50" fill="none" stroke="#fff" stroke-width="2.8"/>
<path d="M46 35 L50 33 M58 31 L62 31 M70 34 L74 37 M80 42 L83 45" stroke="#E83A5A" stroke-width="2.8"/>
<path d="M56 54 H112 L104 118 H64Z" fill="#EAF8FF" {W(3)}/>
<path d="M59 68 H109 L103 115 H65Z" fill="#D8234A"/>
<rect x="66" y="60" width="14" height="14" rx="3" fill="#fff" opacity=".85" {W(2)}/><rect x="88" y="62" width="13" height="13" rx="3" fill="#fff" opacity=".85" {W(2)}/>
{eye(76, 92, .55)}{eye(92, 92, .55)}{smile(84, 100, 4, .8)}<circle cx="71" cy="101" r="2.4" fill="#FF9AB8"/><circle cx="97" cy="101" r="2.4" fill="#FF9AB8"/>
<path d="M56 54 H112" {W(3)}/>''')

# 2. Osteria Mario (Охотный Ряд) — башенка профитролей, верхний съезжает по шоколаду
I["cafe-osteria-okhotny"] = ("башенка из профитролей в шоколадной глазури", "верхний профитроль с поднятыми ручками съезжает по шоколадному ручейку, как с горки", ("#FFF1E6", "#8A4B2E"), f'''
<ellipse cx="60" cy="112" rx="50" ry="10" fill="#fff" {W(3)}/>
<circle cx="36" cy="96" r="15" fill="#F2C680" {W(3)}/><circle cx="64" cy="98" r="15" fill="#F2C680" {W(3)}/><circle cx="90" cy="96" r="14" fill="#F2C680" {W(3)}/>
<circle cx="50" cy="72" r="15" fill="#F2C680" {W(3)}/><circle cx="78" cy="72" r="15" fill="#F2C680" {W(3)}/>
<path d="M36 64 Q50 56 64 62 Q78 56 92 64 Q90 74 86 70 Q82 80 78 72 Q72 82 66 70 Q58 80 54 70 Q46 80 40 70 Q36 74 36 64Z" fill="#6A3420" {W(2.4)}/>
<path d="M92 66 Q104 76 108 92" fill="none" stroke="#6A3420" stroke-width="8" stroke-linecap="round"/>
{eye(58, 92, .45)}{eye(70, 92, .45)}{smile(64, 100, 3, .6)}
<circle cx="98" cy="50" r="14" fill="#F2C680" {W(3)}/><path d="M85 46 Q98 34 111 46 Q104 42 98 46 Q92 42 85 46Z" fill="#6A3420" {W(2)}/>
{eye(94, 53, .45)}{eye(104, 53, .45)}<ellipse cx="99" cy="59" rx="2.4" ry="2" fill="{O}"/>
<path d="M86 50 L76 38 M110 50 L118 36" fill="none" {W(4.4)}/><path d="M86 50 L76 38 M110 50 L118 36" fill="none" stroke="#F2C680" stroke-width="1.6"/>
<path d="M70 30 Q76 26 80 30 M112 26 Q118 22 122 26" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 3. Гамбринус (Коньково) — чешский жареный сыр растягивает сыр, как гармошку
I["cafe-gambrinus-konkovo"] = ("чешский жареный сыр-кирпичик в золотистой панировке", "разломился пополам и играет польку, растягивая сырные складки, как меха гармошки", ("#EEF8E6", "#4E8A3A"), f'''
<path d="M14 54 L42 50 L44 98 L16 102Z" fill="#E8A040" {W(3)}/><path d="M20 60 L24 58 M30 70 L34 68 M22 84 L26 82 M34 90 L38 88" stroke="#B86A20" stroke-width="2.4" stroke-linecap="round"/>
<path d="M86 50 L114 54 L112 102 L84 98Z" fill="#E8A040" {W(3)}/><path d="M94 60 L98 62 M104 72 L108 74 M92 84 L96 86 M102 92 L106 94" stroke="#B86A20" stroke-width="2.4" stroke-linecap="round"/>
<path d="M42 54 L52 60 L58 52 L64 60 L70 52 L76 60 L86 54 L86 96 L76 90 L70 98 L64 90 L58 98 L52 90 L42 96Z" fill="#FFE27A" {W(2.8)}/>
<path d="M52 60 V90 M58 52 V98 M64 60 V90 M70 52 V98 M76 60 V90" stroke="#E8C040" stroke-width="2"/>
{eye(24, 72, .5)}{eye(35, 71, .5)}{smile(30, 80, 3.5, .7)}{blush(20, 79, .4)}
{eye(94, 71, .5)}{eye(105, 72, .5)}<path d="M96 80 Q100 84 104 80" fill="none" {W(2)}/>{blush(109, 79, .4)}
<ellipse cx="34" cy="20" rx="4" ry="3" fill="#fff" {W(1.8)}/><path d="M38 20 V6 Q44 10 46 14" fill="none" {W(2)}/>
<ellipse cx="90" cy="28" rx="4" ry="3" fill="#fff" {W(1.8)}/><path d="M94 28 V14 L102 12 V24" fill="none" {W(2)}/><ellipse cx="98" cy="24" rx="4" ry="3" fill="#fff" {W(1.8)}/>''')

# 4. Up Sushi (Люберцы) — ролл «Калифорния» в оранжевой икре делает колесо на лужайке
I["cafe-upsushi-lyubertsy"] = ("высокий ролл «Калифорния» в оранжевой икре тобико", "делает утреннюю зарядку на зелёной лужайке — ручки вверх, одна ножка в сторону", ("#E6FFF6", "#1E9C88"), f'''
<path d="M0 106 Q64 98 128 106 V128 H0Z" fill="#7CCB5A" {W(2.4)}/>
{limb("M40 64 L22 40", "#FFF4E0", 6.4)}{limb("M88 64 L106 40", "#FFF4E0", 6.4)}
{limb("M54 98 L50 112", "#FFF4E0", 6.4)}{limb("M76 98 L96 106", "#FFF4E0", 6.4)}
<path d="M36 44 V90 Q36 102 64 102 Q92 102 92 90 V44Z" fill="#FF8A2A" {W(3)}/>
<g fill="#E8600A"><circle cx="42" cy="60" r="1.8"/><circle cx="50" cy="94" r="1.8"/><circle cx="86" cy="62" r="1.8"/><circle cx="80" cy="94" r="1.8"/><circle cx="44" cy="80" r="1.8"/><circle cx="86" cy="82" r="1.8"/><circle cx="64" cy="96" r="1.8"/></g>
<ellipse cx="64" cy="44" rx="28" ry="12" fill="#fff" {W(3)}/>
<ellipse cx="64" cy="44" rx="18" ry="7.4" fill="#2E4A3A"/><ellipse cx="64" cy="44" rx="13" ry="5" fill="#fff"/>
<ellipse cx="59" cy="44" rx="5" ry="3" fill="#9ED36A"/><ellipse cx="69" cy="44" rx="5" ry="3" fill="#FF8AA0"/>
{eye(55, 72, .55)}{eye(73, 72, .55)}{smile(64, 81, 4, .8)}{blush(49, 80, .45)}{blush(79, 80, .45)}
{sparkle(20, 24, 4)}{sparkle(110, 22, 3)}''')

# 5. Пиццаменто — мальчик-пиццайоло подбрасывает тесто над головой
I["cafe-pitstsamento"] = ("мальчик-пиццайоло в высоком белом колпаке", "крутит над головой летящий блин теста, вокруг облачка муки", ("#FFEFEF", "#C8323A"), f'''
<ellipse cx="64" cy="30" rx="34" ry="11" fill="#F8E2B0" {W(3)}/><ellipse cx="64" cy="29" rx="25" ry="6" fill="#FFF0CC"/>
<path d="M26 18 Q22 12 26 8 M102 18 Q106 12 102 8" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
{sparkle(18, 46, 4)}{sparkle(108, 44, 4)}{sparkle(30, 56, 2.6)}
{limb("M50 82 L42 60 L48 40", "#FFD8B8", 6.4)}{limb("M78 82 L86 60 L80 40", "#FFD8B8", 6.4)}
<path d="M44 128 L48 92 Q64 84 80 92 L84 128Z" fill="#fff" {W(3)}/><path d="M56 96 L64 108 L72 96" fill="#E8384A" {W(2)}/>
<circle cx="64" cy="76" r="15" fill="#FFD8B8" {W(3)}/>
<path d="M50 70 Q46 52 56 52 Q58 44 64 46 Q70 44 72 52 Q82 52 78 70Z" fill="#fff" {W(2.6)}/>
{eye(58, 78, .45)}{eye(70, 78, .45)}<path d="M59 85 Q64 90 69 85" fill="none" {W(2)}/>{blush(54, 84, .4)}{blush(74, 84, .4)}''')

# 6. Сытый лось (Коломенский) — гречка горкой, кусочек масла съезжает с вершины
I["cafe-sytyy-los"] = ("рассыпчатая гречневая каша горкой на тарелке", "с вершины каши, растекаясь, съезжает кусочек сливочного масла и радостно машет", ("#EDF0FF", "#5A6AB0"), f'''
<ellipse cx="64" cy="102" rx="58" ry="18" fill="#fff" {W(3)}/><ellipse cx="64" cy="100" rx="46" ry="11" fill="#E4E8F6"/>
<path d="M22 100 Q28 66 64 62 Q100 66 106 100 Q64 108 22 100Z" fill="#B87A40" {W(3)}/>
<ellipse cx="34" cy="92" rx="2.2" ry="1.4" fill="#E8B878" transform="rotate(20 34 92)"/><ellipse cx="44" cy="84" rx="2.2" ry="1.4" fill="#E8B878" transform="rotate(-30 44 84)"/><ellipse cx="54" cy="90" rx="2.2" ry="1.4" fill="#E8B878" transform="rotate(10 54 90)"/><ellipse cx="64" cy="80" rx="2.2" ry="1.4" fill="#E8B878" transform="rotate(40 64 80)"/><ellipse cx="74" cy="88" rx="2.2" ry="1.4" fill="#E8B878" transform="rotate(-20 74 88)"/><ellipse cx="84" cy="82" rx="2.2" ry="1.4" fill="#E8B878" transform="rotate(30 84 82)"/><ellipse cx="94" cy="92" rx="2.2" ry="1.4" fill="#E8B878" transform="rotate(-10 94 92)"/><ellipse cx="48" cy="74" rx="2.2" ry="1.4" fill="#E8B878" transform="rotate(0 48 74)"/><ellipse cx="80" cy="72" rx="2.2" ry="1.4" fill="#E8B878" transform="rotate(-40 80 72)"/><ellipse cx="60" cy="94" rx="2.2" ry="1.4" fill="#E8B878" transform="rotate(25 60 94)"/><ellipse cx="70" cy="70" rx="2.2" ry="1.4" fill="#E8B878" transform="rotate(15 70 70)"/><ellipse cx="40" cy="96" rx="2.2" ry="1.4" fill="#E8B878" transform="rotate(-15 40 96)"/><ellipse cx="88" cy="96" rx="2.2" ry="1.4" fill="#E8B878" transform="rotate(35 88 96)"/><ellipse cx="56" cy="66" rx="2.2" ry="1.4" fill="#E8B878" transform="rotate(-25 56 66)"/>
<path d="M58 64 Q48 70 44 80 Q52 80 56 72Z" fill="#FFE68A" opacity=".95"/>
<rect x="54" y="40" width="26" height="20" rx="4" fill="#FFE27A" {W(3)} transform="rotate(-14 67 50)"/>
<path d="M58 40 L64 36 L84 32" fill="none" stroke="#FFF6C0" stroke-width="2"/>
{eye(62, 50, .5)}{eye(73, 48, .5)}{smile(68, 55, 3, .6)}
{limb("M80 44 L94 32", "#FFE27A", 5)}{limb("M54 52 L42 46", "#FFE27A", 5)}
<path d="M30 52 Q26 44 32 38 M100 56 Q96 48 102 42" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

# 7. Bocconcino (ТРЦ «Рио») — трёхколёсный велосипед с колёсами-пиццами
I["cafe-bocconcino-rio-leninsky"] = ("детский трёхколёсный велосипед с колёсами-пиццами", "весело катится по ресторану, колёса крутятся, позади — пыльные облачка", ("#F7FFE0", "#8AB02A"), f'''
<path d="M6 92 Q12 86 20 90 M2 104 Q10 98 18 102" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<circle cx="36" cy="96" r="20" fill="#E8A040" {W(3)}/><circle cx="36" cy="96" r="15" fill="#E8432A"/><circle cx="30" cy="90" r="3" fill="#FFF4C8"/><circle cx="42" cy="98" r="3" fill="#FFF4C8"/><circle cx="32" cy="104" r="2.4" fill="#5AA040"/>
<circle cx="98" cy="102" r="14" fill="#E8A040" {W(3)}/><circle cx="98" cy="102" r="10" fill="#E8432A"/><circle cx="95" cy="99" r="2.4" fill="#FFF4C8"/><circle cx="102" cy="105" r="2" fill="#5AA040"/>
<path d="M36 96 L60 68 L92 72 L98 102 M60 68 L58 54 M92 72 L88 40" fill="none" {W(5)}/><path d="M36 96 L60 68 L92 72 L98 102 M60 68 L58 54 M92 72 L88 40" fill="none" stroke="#2A8AE8" stroke-width="2"/>
<path d="M48 52 Q58 46 70 52" fill="none" {W(6)}/><path d="M48 52 Q58 46 70 52" fill="none" stroke="#E83A5A" stroke-width="2.6"/>
<path d="M78 40 H98" {W(5)}/><circle cx="76" cy="40" r="4" fill="#E83A5A" {W(2)}/><circle cx="100" cy="40" r="4" fill="#E83A5A" {W(2)}/>
{eye(31, 94, .4)}{eye(41, 94, .4)}<path d="M32 101 Q36 104 40 101" fill="none" {W(1.8)}/>''')

# 8. Колбасофф (Митино) — колбаска-спиралька спускается по ступенькам, как пружинка
I["cafe-kolbasoff-mitino"] = ("связка из четырёх сарделек", "шагает вниз по ступенькам, как пружинка-радуга, перекидываясь со ступеньки на ступеньку", ("#FFE8F4", "#C0307A"), f'''
<path d="M0 90 H40 V104 H80 V116 H128 V128 H0Z" fill="#F6D2E4" {W(3)}/>
<rect x="12" y="87" width="32" height="18" rx="9" fill="#D8703A" {W(3)} transform="rotate(-60 28 96)"/><path d="M20 93 Q28 90 36 93" fill="none" stroke="#F2A070" stroke-width="2.4" stroke-linecap="round" transform="rotate(-60 28 96)"/><rect x="26" y="55" width="32" height="18" rx="9" fill="#D8703A" {W(3)} transform="rotate(-30 42 64)"/><path d="M34 61 Q42 58 50 61" fill="none" stroke="#F2A070" stroke-width="2.4" stroke-linecap="round" transform="rotate(-30 42 64)"/><rect x="50" y="43" width="32" height="18" rx="9" fill="#D8703A" {W(3)} transform="rotate(10 66 52)"/><path d="M58 49 Q66 46 74 49" fill="none" stroke="#F2A070" stroke-width="2.4" stroke-linecap="round" transform="rotate(10 66 52)"/><rect x="72" y="57" width="32" height="18" rx="9" fill="#D8703A" {W(3)} transform="rotate(50 88 66)"/><path d="M80 63 Q88 60 96 63" fill="none" stroke="#F2A070" stroke-width="2.4" stroke-linecap="round" transform="rotate(50 88 66)"/>
<circle cx="34" cy="80" r="3" fill="#fff" {W(1.6)}/><circle cx="54" cy="56" r="3" fill="#fff" {W(1.6)}/><circle cx="78" cy="56" r="3" fill="#fff" {W(1.6)}/>
<g transform="rotate(50 88 66)">{eye(86, 63, .4)}{eye(94, 63, .4)}</g><path d="M86 74 Q89 77 92 74" fill="none" {W(1.8)}/>
<path d="M20 40 Q24 34 30 38 M100 30 Q104 24 110 28" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 9. Шахдаг (Талдомская) — шекер-чурек покоряет снежную вершину Шахдаг
I["cafe-shahdag-taldomskaya"] = ("круглое азербайджанское печенье шекер-чурек", "стоит на снежной вершине горы Шахдаг и втыкает флажок", ("#F2F8FF", "#6A9AD0"), f'''
<path d="M-4 128 L44 52 L64 74 L84 40 L136 128Z" fill="#8A9AB8" {W(3)}/>
<path d="M44 52 L54 68 L48 66 L40 72 L36 64Z" fill="#fff"/><path d="M84 40 L98 62 L90 58 L84 66 L76 58 L72 60Z" fill="#fff"/>
<path d="M102 40 V8" {W(3)}/><path d="M104 10 L124 16 L104 24Z" fill="#E8384A" {W(2.4)}/>
<circle cx="80" cy="30" r="21" fill="#FFF2D8" {W(3)}/><circle cx="80" cy="30" r="14" fill="none" stroke="#E8B870" stroke-width="2.4" stroke-dasharray="4 3"/><circle cx="80" cy="30" r="7" fill="#E8C070"/>
{eye(74, 27, .5)}{eye(86, 27, .5)}<path d="M76 38 Q80 42 84 38" fill="none" {W(2)}/>
{limb("M98 28 L102 22", "#FFF2D8", 5)}
<path d="M10 22 Q16 18 22 22 M30 14 Q34 10 38 14" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 10. Florentini (Ленинский) — печенье-флорентина встаёт солнышком над куполом Дуомо
I["cafe-florentini-leninsky"] = ("печенье-флорентина с миндальными лепестками", "восходит, как солнышко, из-за купола флорентийского собора", ("#FFF0E0", "#D07040"), f'''
<circle cx="64" cy="48" r="30" fill="#E8B050" {W(3)}/>
<path d="M50 34 L58 40 M70 30 L76 38 M44 52 L52 54 M76 56 L84 52 M60 62 L66 64" stroke="#FFF2C8" stroke-width="4" stroke-linecap="round"/>
<path d="M44 66 Q64 76 84 66" fill="none" stroke="#5A3020" stroke-width="5"/>
{eye(56, 46, .55)}{eye(72, 46, .55)}{smile(64, 54, 4, .8)}{blush(50, 54, .45)}{blush(78, 54, .45)}
<path d="M20 128 V100 Q20 72 64 70 Q108 72 108 100 V128Z" fill="#C8502A" {W(3)}/>
<path d="M44 76 Q46 96 44 128 M64 70 V128 M84 76 Q82 96 84 128" stroke="#fff" stroke-width="2.6"/>
<rect x="58" y="62" width="12" height="10" fill="#F4E8D4" {W(2.4)}/>
<path d="M12 22 L16 30 M110 22 L106 30 M20 10 L22 18 M104 10 L102 18" stroke="#FFF6C0" stroke-width="3" stroke-linecap="round"/>''')

# 11. Kitchen (Реутов) — куриная ножка-барабанщица
I["cafe-kitchen-reutov"] = ("запечённая куриная ножка-барабанщица", "лупит палочками по детскому барабану, вокруг разлетаются нотки", ("#F4ECFF", "#7A4AC0"), f'''
<ellipse cx="64" cy="100" rx="34" ry="10" fill="#E8384A" {W(3)}/><path d="M30 100 V114 Q64 128 98 114 V100" fill="#fff" {W(3)}/>
<path d="M32 104 L44 120 L58 104 L72 120 L86 104 L96 116" fill="none" stroke="#E8384A" stroke-width="2.4"/>
<path d="M58 84 Q34 70 40 42 Q48 22 70 30 Q90 40 80 66 Q76 78 70 86Z" fill="#C86A2A" {W(3)}/>
<path d="M66 86 L72 94" {W(7)}/><path d="M66 86 L72 94" stroke="#FFF4E0" stroke-width="3.6" stroke-linecap="round"/><circle cx="70" cy="96" r="4" fill="#FFF4E0" {W(2)}/><circle cx="75" cy="93" r="4" fill="#FFF4E0" {W(2)}/>
<path d="M50 40 Q56 34 62 38" fill="none" stroke="#E89050" stroke-width="3" stroke-linecap="round"/>
{eye(54, 54, .55)}{eye(68, 54, .55)}{smile(61, 62, 4, .8)}{blush(48, 62, .45)}
<path d="M42 62 L26 90" {W(3.4)}/><circle cx="26" cy="90" r="3.4" fill="#F2C680" {W(2)}/>
<path d="M80 58 L100 86" {W(3.4)}/><circle cx="100" cy="88" r="3.4" fill="#F2C680" {W(2)}/>
<ellipse cx="104" cy="34" rx="4" ry="3" fill="#fff" {W(1.8)}/><path d="M108 34 V20" {W(2)}/>
<ellipse cx="20" cy="40" rx="4" ry="3" fill="#FFE45A" {W(1.8)}/><path d="M24 40 V26 Q30 30 32 34" fill="none" {W(2)}/>''')

# 12. Азербайджан (Демьяна Бедного) — стаканчик-армуды кружится в танце с кусочком сахара
I["cafe-azerbaijan-bednogo"] = ("стаканчик-армуды с горячим чаем", "кружится в танце на блюдце, держа за ручку кусочек колотого сахара", ("#FFEDEA", "#A82838"), f'''
<ellipse cx="62" cy="108" rx="40" ry="10" fill="#E8C060" {W(3)}/><ellipse cx="62" cy="106" rx="28" ry="5" fill="#F8E098"/>
<path d="M44 40 H80 Q74 56 80 74 Q86 94 70 104 H54 Q38 94 44 74 Q50 56 44 40Z" fill="#F4FAFF" {W(3)}/>
<path d="M47 56 H77 Q74 64 78 76 Q82 94 68 100 H56 Q42 94 46 76 Q50 64 47 56Z" fill="#B8381A"/>
<path d="M44 40 H80" {W(3.4)}/><path d="M48 36 H76" stroke="#E8C060" stroke-width="3"/>
<path d="M54 30 Q50 22 56 16 M68 30 Q64 22 70 14" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
{eye(56, 78, .5)}{eye(68, 78, .5)}{smile(62, 86, 3.5, .7)}
{limb("M80 70 L94 64", "#F4FAFF", 5)}
<path d="M94 52 L108 50 L112 62 L98 68Z" fill="#fff" {W(2.6)}/>{eye(101, 58, .35)}{eye(107, 57, .35)}
{limb("M98 66 L96 80", "#fff", 4.6)}
<path d="M20 60 Q28 52 24 44 M104 96 Q112 92 116 98" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 13. Колбасофф (Сокольники) — бутерброд-кораблик с колбасным парусом плывёт по луже в парке
I["cafe-kolbasoff-sokolniki"] = ("бутерброд-кораблик с парусом из кружка колбасы на шпажке", "плывёт по луже в парке, рядом кружится осенний листик", ("#E6F4EE", "#4A8A70"), f'''
<path d="M0 92 Q32 82 64 90 Q96 82 128 92 V128 H0Z" fill="#6AB8D8" {W(2.4)}/>
<path d="M18 108 Q24 104 30 108 M96 112 Q102 108 108 112" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>
<path d="M26 82 H102 L94 100 H34Z" fill="#E8B068" {W(3)}/><path d="M28 82 H100 V76 H28Z" fill="#FFE8B8" {W(2.6)}/>
<path d="M64 76 V18" {W(3)}/>
<circle cx="64" cy="46" r="24" fill="#E88090" {W(3)}/><circle cx="56" cy="40" r="2.4" fill="#fff"/><circle cx="72" cy="52" r="2.4" fill="#fff"/><circle cx="68" cy="36" r="2" fill="#fff"/><circle cx="56" cy="56" r="2" fill="#fff"/>
{eye(48, 90, .5)}{eye(60, 90, .5)}{smile(54, 96, 3, .6)}
<path d="M64 18 L76 22 L64 26" fill="#FFE45A" {W(2)}/>
<path d="M100 34 Q110 30 112 40 Q106 46 100 34Z" fill="#E8A030" {W(2.2)}/>''')

# 14. Пронто (Отрадное, пиццерия) — красная итальянская веспа доставки мчится
I["cafe-pronto-otradnoe"] = ("красная итальянская веспа с коробкой пиццы на багажнике", "мчится с подмигиванием по городу, за ней вьётся дымок «пронто!»", ("#FFFBE0", "#E0B020"), f'''
<path d="M0 108 H128 V128 H0Z" fill="#9A9AA8" {W(2.4)}/><path d="M10 116 H30 M50 116 H70 M90 116 H110" stroke="#fff" stroke-width="3"/>
<path d="M6 80 Q14 76 20 80 M2 92 Q10 88 18 92" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<circle cx="40" cy="98" r="11" fill="#2A2F4A" {W(3)}/><circle cx="40" cy="98" r="4" fill="#C8C8D8"/>
<circle cx="96" cy="98" r="11" fill="#2A2F4A" {W(3)}/><circle cx="96" cy="98" r="4" fill="#C8C8D8"/>
<path d="M26 92 Q24 70 46 66 H66 L72 84 H88 Q84 60 94 46 L100 46 Q96 66 108 92Z" fill="#E8302A" {W(3)}/>
<path d="M92 46 L100 30 M94 30 H108" {W(3.4)}/>
<rect x="24" y="46" width="34" height="18" rx="2" fill="#FFF6E0" {W(2.6)}/><path d="M30 55 H52" stroke="#E8302A" stroke-width="3"/>
<circle cx="104" cy="56" r="5" fill="#FFE45A" {W(2)}/>
{eye(80, 76, .45)}<path d="M90 74 Q94 72 96 75" fill="none" {W(2)}/><path d="M80 84 Q86 88 92 84" fill="none" {W(2)}/>''')

# 15. Маска (Филёвский парк) — панцеротти в венецианской маске с пёрышком
I["cafe-maska-fili"] = ("жареный пирожок панцеротти с тянущимся сыром", "на карнавале примеряет венецианскую маску с пёрышком", ("#F0E8FF", "#5A2A8A"), f'''
<path d="M18 90 Q20 46 64 40 Q108 46 110 90Z" fill="#E8A848" {W(3)}/>
<path d="M18 90 Q64 104 110 90" fill="#D89030" {W(3)}/>
<path d="M24 88 L28 94 L34 90 L40 96 L46 92 L52 98 L58 94 L64 100 L70 94 L76 98 L82 92 L88 96 L94 90 L100 94 L104 88" fill="none" stroke="#B87020" stroke-width="2"/>
<path d="M30 60 Q46 50 64 58 Q82 50 98 60 Q96 76 82 76 Q70 76 64 68 Q58 76 46 76 Q32 76 30 60Z" fill="#7A2AC0" {W(2.8)}/>
<ellipse cx="47" cy="65" rx="7" ry="5" fill="#E8A848"/><ellipse cx="81" cy="65" rx="7" ry="5" fill="#E8A848"/>
{eye(47, 65, .45)}{eye(81, 65, .45)}
<circle cx="64" cy="58" r="3" fill="#FFD23A" {W(1.6)}/>
<path d="M96 58 Q112 34 104 16 Q120 30 112 52" fill="#FF6A9A" {W(2.4)}/><path d="M98 56 Q108 38 106 22" fill="none" stroke="#fff" stroke-width="1.6"/>
<path d="M54 86 Q64 92 74 86" fill="none" {W(2.4)}/>
<path d="M104 96 Q112 104 106 114" fill="none" stroke="#FFE27A" stroke-width="5" stroke-linecap="round"/>
{sparkle(24, 30, 4)}{sparkle(40, 18, 3)}''')

# 16. Osteria Mario (Баррикадная, у зоопарка) — кассата, жирафик тянет шею понюхать
I["cafe-osteria-barrikadnaya"] = ("кусок сицилийской кассаты с цукатами и вишенкой", "сверху к нему тянет длинную шею любопытный жирафик из соседнего зоопарка", ("#FFF0F4", "#D86080"), f'''
<ellipse cx="54" cy="110" rx="44" ry="9" fill="#fff" {W(3)}/>
<path d="M18 104 L26 62 L84 62 L90 104Z" fill="#FFF6E8" {W(3)}/>
<path d="M22 84 L88 84" stroke="#F8D0DC" stroke-width="10"/><path d="M20 94 L89 94" stroke="#7ACB7A" stroke-width="3"/>
<rect x="34" y="70" width="7" height="6" rx="2" fill="#E83A5A"/><rect x="60" y="72" width="7" height="6" rx="2" fill="#5AB050"/><rect x="72" y="88" width="6" height="5" rx="2" fill="#FFB020"/>
<circle cx="56" cy="54" r="7" fill="#D8203A" {W(2.4)}/><path d="M56 47 Q58 38 64 34" fill="none" {W(2)}/>
{eye(42, 92, .5)}{eye(58, 92, .5)}{smile(50, 100, 3, .6)}
<path d="M128 6 Q100 4 92 26 L88 40" fill="none" {W(10)}/><path d="M128 6 Q100 4 92 26 L88 40" fill="none" stroke="#F2C040" stroke-width="6"/>
<ellipse cx="82" cy="40" rx="11" ry="8" fill="#F2C040" {W(3)}/>
<circle cx="96" cy="16" r="3" fill="#B87020"/><circle cx="106" cy="8" r="2.4" fill="#B87020"/>
{eye(84, 36, .4)}<ellipse cx="74" cy="42" rx="2" ry="1.6" fill="{O}"/>
<path d="M88 32 L90 26 M94 32 L98 28" {W(2.4)}/>''')

# 17. Mansard (Речной вокзал) — волнистая детская горка, с неё съезжает малыш
I["cafe-mansard-lavochkina"] = ("круглое печенье с шоколадной крошкой", "выглядывает из круглого окошка мансарды под черепичной крышей, рядом голубь на карнизе", ("#E8EEFF", "#2A3A7A"), f'''
<path d="M-4 70 L64 14 L132 70Z" fill="#C8503A" {W(3)}/>
<path d="M14 56 H114 M30 42 H98 M46 28 H82" stroke="#9A3020" stroke-width="2.4"/>
<path d="M8 70 H120 V132 H8Z" fill="#F4E8D4" {W(3)}/>
<circle cx="64" cy="94" r="26" fill="#3A4A8A" {W(3)}/>
<circle cx="64" cy="96" r="20" fill="#E0A860" {W(2.8)}/>
<g fill="#5A3020"><circle cx="54" cy="88" r="3"/><circle cx="74" cy="90" r="2.6"/><circle cx="58" cy="108" r="2.6"/><circle cx="72" cy="106" r="3"/></g>
{eye(59, 96, .45)}{eye(69, 96, .45)}{smile(64, 102, 3, .6)}
<path d="M64 68 V120 M38 94 H90" stroke="#fff" stroke-width="2" opacity=".4"/>
<path d="M96 66 Q100 58 108 60 Q114 62 112 68 Z" fill="#C8C8D8" {W(2.2)}/><circle cx="106" cy="62" r="1.2" fill="{O}"/><path d="M112 62 L116 62" stroke="#E8A030" stroke-width="2"/>
{sparkle(20, 22, 4)}{sparkle(108, 22, 3)}''')

# 18. Ротонда (Москва-река) — торт-шарлотка с бортиком из савоярди, мимо плывёт кораблик
I["cafe-rotonda-aviatsionnaya"] = ("торт-шарлотка с бортиком из бисквитных палочек савоярди и бантиком", "стоит, как беседка-ротонда, на берегу реки, мимо плывёт прогулочный кораблик", ("#EFFFF8", "#3AAA8A"), f'''
<path d="M0 94 Q32 88 64 94 T128 94 V128 H0Z" fill="#4AA8D8" {W(2.4)}/>
<path d="M88 86 H122 L116 96 H92Z" fill="#fff" {W(2.4)}/><rect x="96" y="78" width="16" height="8" fill="#E8384A" {W(2)}/>
<path d="M20 52 Q50 40 78 52 V100 Q50 110 20 100Z" fill="#F2D49A" {W(3)}/>
<path d="M27 50 V103 M34 48 V105 M41 46 V106 M48 46 V107 M55 46 V107 M62 47 V106 M69 49 V104" stroke="#D8A860" stroke-width="2"/>
<ellipse cx="49" cy="50" rx="29" ry="9" fill="#FFF6F8" {W(3)}/>
<circle cx="38" cy="46" r="4" fill="#E8304A" {W(1.6)}/><circle cx="52" cy="44" r="4" fill="#5A3AA0" {W(1.6)}/><circle cx="62" cy="50" r="4" fill="#E8304A" {W(1.6)}/>
<path d="M20 80 Q50 90 78 80" fill="none" stroke="#FF6A9A" stroke-width="5"/>
<path d="M44 84 L36 78 L36 90Z M54 84 L62 78 L62 90Z" fill="#FF6A9A" {W(2)}/><circle cx="49" cy="84" r="3" fill="#FF6A9A" {W(1.6)}/>
{eye(40, 68, .5)}{eye(58, 68, .5)}{smile(49, 74, 3.5, .7)}''')

# 19. Поместье-парк (Серебряный бор) — белочка в фартучке угощает пирожком на пеньке
I["cafe-pomestie-park"] = ("рыжая белочка в клетчатом фартучке с горячим пирожком", "угощает пирожком, сидя на пеньке среди сосен Серебряного бора", ("#EEF6E4", "#3E6E30"), f'''
<path d="M10 70 L22 34 L34 70Z M96 66 L110 22 L124 66Z" fill="#2E7A3A" {W(2.6)}/><path d="M22 70 V90 M110 66 V90" {W(3)}/>
<path d="M34 104 Q34 92 64 92 Q94 92 94 104 V124 H34Z" fill="#B07840" {W(3)}/><ellipse cx="64" cy="98" rx="30" ry="7" fill="#E8C890" {W(2.6)}/>
<ellipse cx="64" cy="98" rx="16" ry="3.4" fill="none" stroke="#C8A060" stroke-width="1.6"/>
<path d="M86 88 Q112 80 104 50 Q98 34 88 42 Q100 56 84 74Z" fill="#E87A2A" {W(3)}/>
<path d="M50 94 Q46 66 64 62 Q82 66 78 94Z" fill="#E87A2A" {W(3)}/>
<path d="M54 92 Q52 72 64 70 Q76 72 74 92Z" fill="#fff" {W(2.2)}/><path d="M54 80 H74 M58 72 V92 M70 72 V92" stroke="#E8384A" stroke-width="1.6"/>
<circle cx="64" cy="48" r="15" fill="#E87A2A" {W(3)}/><path d="M52 38 L50 26 L58 34 M76 38 L78 26 L70 34" fill="#E87A2A" {W(2.4)}/>
{eye(59, 48, .45)}{eye(69, 48, .45)}<ellipse cx="64" cy="54" rx="2.2" ry="1.8" fill="{O}"/>{blush(55, 55, .4)}{blush(73, 55, .4)}
<ellipse cx="40" cy="76" rx="12" ry="7" fill="#E8A040" {W(2.6)}/><path d="M32 74 Q40 70 48 74" fill="none" stroke="#B86A20" stroke-width="1.8"/>
{limb("M52 76 L44 76", "#E87A2A", 5)}
<path d="M36 64 Q34 58 38 54 M44 64 Q42 58 46 54" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>''')

# 20. Соседи (Мичуринский, грузинская кухня) — две лепёшки мчади болтают через заборчик
I["cafe-sosedi-michurinsky"] = ("две круглые золотистые грузинские лепёшки мчади", "болтают через низкий деревянный заборчик, как соседи по даче", ("#FFF4E4", "#E0A060"), f'''
<path d="M0 104 H128 V128 H0Z" fill="#8ACB5A" {W(2.4)}/>
<circle cx="32" cy="78" r="22" fill="#F0B860" {W(3)}/><circle cx="32" cy="78" r="15" fill="none" stroke="#D8903A" stroke-width="2"/>
{eye(26, 76, .5)}{eye(38, 76, .5)}<ellipse cx="34" cy="86" rx="3" ry="2.4" fill="{O}"/>{blush(22, 84, .4)}
<circle cx="98" cy="80" r="20" fill="#E8A850" {W(3)}/><circle cx="98" cy="80" r="13" fill="none" stroke="#C8803A" stroke-width="2"/>
{eye(92, 78, .5)}{eye(104, 78, .5)}{smile(97, 86, 3.5, .7)}{blush(108, 86, .4)}
<path d="M54 112 V76 L58 70 L62 76 V112 M66 112 V76 L70 70 L74 76 V112" fill="#C8905A" {W(2.6)}/>
<path d="M50 86 H78 M50 100 H78" {W(3)}/>
<path d="M44 52 Q50 46 56 50 M74 50 Q80 44 86 48" fill="none" {W(2.2)}/>
<circle cx="50" cy="40" r="2" fill="{O}"/><circle cx="58" cy="36" r="2" fill="{O}"/><circle cx="78" cy="38" r="2" fill="{O}"/>''')

# 21. НОА (Народного Ополчения) — ковчег-игровая под парусом из лаваша
I["cafe-noa-opolchenie"] = ("деревянный Ноев ковчег-игровая с парусом из лаваша", "плывёт по волнам, из окошек выглядывают жирафик и слонёнок, над мачтой голубь с веточкой", ("#E4F4FF", "#2A6AB0"), f'''
<path d="M0 100 Q16 94 32 100 T64 100 T96 100 T128 100 V128 H0Z" fill="#2E86D0" {W(2.4)}/>
<path d="M14 76 H114 Q108 104 64 106 Q20 104 14 76Z" fill="#B87840" {W(3)}/>
<path d="M18 88 H110" stroke="#8A5228" stroke-width="2"/>
<rect x="34" y="56" width="58" height="22" rx="4" fill="#E0A060" {W(2.8)}/>
<circle cx="48" cy="67" r="6" fill="#FFF0C8" {W(2)}/><circle cx="78" cy="67" r="6" fill="#FFF0C8" {W(2)}/>
<path d="M44 60 V40 Q44 34 50 36" fill="none" {W(5)}/><path d="M44 60 V40 Q44 34 50 36" fill="none" stroke="#F2C040" stroke-width="2"/>
<ellipse cx="51" cy="35" rx="5" ry="4" fill="#F2C040" {W(2)}/><circle cx="52" cy="34" r="1.2" fill="{O}"/>
<circle cx="78" cy="64" r="7" fill="#A8B0C8" {W(2.2)}/><path d="M78 70 Q76 78 80 80" fill="none" {W(3.4)}/><path d="M78 70 Q76 78 80 80" fill="none" stroke="#A8B0C8" stroke-width="1.2"/>
<circle cx="76" cy="62" r="1.2" fill="{O}"/><circle cx="81" cy="62" r="1.2" fill="{O}"/>
<path d="M64 56 V12" {W(3)}/><path d="M66 16 Q92 28 90 50 H66Z" fill="#F8E6B8" {W(2.6)}/>
<circle cx="74" cy="30" r="1.6" fill="#C8903A"/><circle cx="82" cy="40" r="1.6" fill="#C8903A"/><circle cx="72" cy="44" r="1.4" fill="#C8903A"/>
<path d="M30 22 Q36 14 44 20 Q38 26 30 22Z" fill="#fff" {W(2)}/><path d="M44 20 L50 22" stroke="#4AA040" stroke-width="2.6" stroke-linecap="round"/>
{eye(22, 92, .4)}{eye(30, 93, .4)}''')

# 22. Завидное (загородный ресторан с завтраками) — творожная запеканка на деревенском окне
I["cafe-zavidnoe-izmaylovo"] = ("квадратик творожной запеканки с изюмом и сметаной", "остывает на подоконнике деревенского окошка с резными наличниками", ("#FFF5EC", "#E08858"), f'''
<rect x="18" y="20" width="92" height="76" fill="#BFE4FF" {W(3)}/>
<path d="M64 20 V96 M18 58 H110" {W(3)}/>
<path d="M10 20 L64 4 L118 20Z" fill="#fff" {W(2.6)}/><path d="M30 16 Q36 10 42 16 M58 10 Q64 4 70 10 M86 16 Q92 10 98 16" fill="none" stroke="#2A6AC0" stroke-width="2"/>
<path d="M10 20 V96 M118 20 V96" stroke="#fff" stroke-width="8"/><path d="M10 20 V96 M118 20 V96" {W(2)}/>
<rect x="4" y="94" width="120" height="10" rx="2" fill="#F4F0E8" {W(3)}/>
<path d="M36 94 L42 64 H90 L86 94Z" fill="#F2C870" {W(3)}/><path d="M42 64 H90 L94 70 H46Z" fill="#E8A040" {W(2.4)}/>
<path d="M60 62 Q66 56 74 62 Q70 66 60 62Z" fill="#fff" {W(2)}/>
<circle cx="50" cy="88" r="2" fill="#6A2A3A"/><circle cx="80" cy="76" r="2" fill="#6A2A3A"/><circle cx="74" cy="90" r="2" fill="#6A2A3A"/>
{eye(56, 78, .5)}{eye(70, 78, .5)}{smile(63, 85, 3.5, .7)}{blush(50, 84, .4)}
<path d="M54 52 Q50 44 56 38 M70 52 Q66 44 72 36" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

# 23. Shore House (яхт-клуб) — рыбка-тайяки выпрыгивает у пирса
I["cafe-shore-house-crocus"] = ("вафля-рыбка тайяки с шоколадной начинкой", "выпрыгивает из воды у пирса яхт-клуба, как настоящая рыба, брызги во все стороны", ("#E8FDFF", "#18A0B8"), f'''
<path d="M0 96 Q16 90 32 96 T64 96 T96 96 T128 96 V128 H0Z" fill="#1E90C0" {W(2.4)}/>
<path d="M96 64 V40" {W(2.6)}/><path d="M98 42 L114 60 H98Z" fill="#fff" {W(2.2)}/><path d="M84 64 H112 L106 72 H90Z" fill="#fff" {W(2.2)}/>
<path d="M0 82 H40 V90 H0Z" fill="#B87840" {W(2.4)}/><path d="M10 90 V112 M30 90 V112" {W(4)}/>
<g transform="rotate(-30 62 58)">
<path d="M28 58 Q34 34 62 34 Q86 34 92 52 L110 40 L106 58 L110 76 L92 64 Q86 82 62 82 Q34 82 28 58Z" fill="#D89040" {W(3)}/>
<path d="M58 44 Q64 50 58 56 M68 44 Q74 50 68 56 M78 48 Q84 54 78 60 M60 64 Q66 70 60 76 M70 62 Q76 68 70 74" fill="none" stroke="#B06A20" stroke-width="2"/>
{eye(42, 52, .55)}<path d="M32 62 Q36 64 40 62" fill="none" {W(2)}/>{blush(44, 62, .45)}
</g>
<path d="M44 94 L36 82 M56 92 L58 80 M76 94 L86 84" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<circle cx="32" cy="76" r="2.4" fill="#fff"/><circle cx="90" cy="80" r="2.4" fill="#fff"/>''')

# 24. «Шторм» (Орехово-Борисово, водное поло) — плавучие ворота ловят мяч сеткой
I["shtorm-orekhovo"] = ("плавучие ворота водного поло с красной рамкой и глазками на перекладине", "растопырили сетку и ловят влетающий жёлто-синий мяч, на воде качаются поплавки", ("#DDF4FF", "#0E4A8A"), f'''
<path d="M0 92 Q16 86 32 92 T64 92 T96 92 T128 92 V128 H0Z" fill="#2A9AE0" {W(2.4)}/>
<path d="M16 96 V44 H112 V96" fill="none" stroke="{O}" stroke-width="9" stroke-linejoin="round"/><path d="M16 96 V44 H112 V96" fill="none" stroke="#E8302A" stroke-width="5"/>
<path d="M22 50 L106 50 L100 88 L28 88Z" fill="#fff" opacity=".5"/>
<path d="M30 50 L34 88 M44 50 L46 88 M58 50 L58 88 M72 50 L70 88 M86 50 L82 88 M100 50 L94 88 M24 62 H104 M26 76 H102" stroke="#fff" stroke-width="1.8"/>
{eye(52, 44, .45)}{eye(76, 44, .45)}<path d="M58 34 Q64 30 70 34" fill="none" {W(2)}/>
<circle cx="64" cy="70" r="13" fill="#FFD23A" {W(2.6)}/><path d="M52 66 Q64 60 76 66 M52 76 Q64 82 76 76" fill="none" stroke="#2A5AC8" stroke-width="3"/>
<path d="M88 26 L96 20 M96 34 L106 32" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<circle cx="10" cy="98" r="5" fill="#FFE45A" {W(2)}/><circle cx="118" cy="98" r="5" fill="#E8302A" {W(2)}/>''')

# 25. «Шторм» (Битца) — девочка-вратарь водного поло ловит мяч в прыжке из воды
I["shtorm-bitsa"] = ("девочка-вратарь водного поло в синей шапочке с ушными защитками", "выпрыгнула по пояс из воды и ловит мяч над головой обеими руками", ("#F0EAFF", "#6A4AD0"), f'''
<path d="M0 90 Q20 84 40 90 T80 90 T128 90 V128 H0Z" fill="#3AA8E0" {W(2.4)}/>
<path d="M36 84 Q30 74 38 70 M92 84 Q100 76 92 70" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<circle cx="64" cy="22" r="13" fill="#FFD23A" {W(2.6)}/><path d="M52 18 Q64 12 76 18 M52 28 Q64 34 76 28" fill="none" stroke="#2A5AC8" stroke-width="3"/>
{limb("M50 74 L42 50 L52 32", "#FFD8B8", 6.6)}{limb("M78 74 L86 50 L76 32", "#FFD8B8", 6.6)}
<path d="M48 96 Q46 76 64 72 Q82 76 80 96Z" fill="#E8384A" {W(3)}/>
<circle cx="64" cy="58" r="14" fill="#FFD8B8" {W(3)}/>
<path d="M49 56 Q48 40 64 40 Q80 40 79 56 Q64 50 49 56Z" fill="#2A5AC8" {W(2.6)}/>
<circle cx="50" cy="60" r="5" fill="#fff" {W(2)}/><circle cx="78" cy="60" r="5" fill="#fff" {W(2)}/>
{eye(59, 59, .45)}{eye(69, 59, .45)}<ellipse cx="64" cy="66" rx="2.6" ry="2" fill="{O}"/>
<path d="M58 44 L62 50 L66 44" fill="none" stroke="#fff" stroke-width="2"/>''')

# 26. «Триумф» (Мытищи, «Бригантина») — надувная бригантина под парусами идёт по бассейну
I["triumf-mytishchi-brigantina"] = ("надувной кораблик-бригантина с двумя мачтами и алыми парусами", "идёт под всеми парусами по дорожке бассейна вдоль поплавков", ("#E6FFF4", "#1C8C6C"), f'''
<rect x="-2" y="78" width="132" height="52" fill="#48C0E8" {W(2.4)}/>
<path d="M0 108 H128" stroke="#fff" stroke-width="7"/><g fill="#E8384A"><circle cx="8" cy="108" r="3.4"/><circle cx="32" cy="108" r="3.4"/><circle cx="56" cy="108" r="3.4"/><circle cx="80" cy="108" r="3.4"/><circle cx="104" cy="108" r="3.4"/><circle cx="124" cy="108" r="3.4"/></g>
<path d="M18 78 Q14 98 64 98 Q114 98 112 74 Q90 82 64 82 Q36 82 18 78Z" fill="#FFD23A" {W(3)}/>
<circle cx="40" cy="88" r="3.4" fill="#fff" {W(1.6)}/><circle cx="64" cy="90" r="3.4" fill="#fff" {W(1.6)}/><circle cx="88" cy="88" r="3.4" fill="#fff" {W(1.6)}/>
<path d="M46 80 V16 M84 80 V22" {W(3)}/>
<path d="M48 22 Q66 34 48 46Z M48 50 Q70 62 48 76Z" fill="#E8304A" {W(2.4)}/>
<path d="M86 26 Q104 38 86 50Z M86 54 Q106 64 86 76Z" fill="#E8304A" {W(2.4)}/>
<path d="M46 16 L36 20 L46 24 M84 22 L74 26 L84 30" fill="#fff" {W(1.8)}/>
{eye(104, 82, .45)}<path d="M108 88 Q111 90 114 87" fill="none" {W(1.8)}/>''')

# 27. «Детская бухта» (индивидуальное плавание) — морж-тренер поддерживает малыша на воде
I["detskaya-bukhta-lefortovo"] = ("усатый морж-тренер со свистком", "в воде бережно держит на ластах малыша, который учится лежать звёздочкой", ("#E8FFFE", "#2AB0B0"), f'''
<path d="M0 84 Q20 78 40 84 T80 84 T128 84 V128 H0Z" fill="#3ABCD8" {W(2.4)}/>
<path d="M30 128 Q20 82 50 70 Q64 64 78 70 Q108 82 98 128Z" fill="#A8806A" {W(3)}/>
{eye(56, 82, .55)}{eye(72, 82, .55)}
<ellipse cx="64" cy="94" rx="12" ry="8" fill="#C8A890" {W(2.4)}/>
<path d="M58 98 L54 114 M70 98 L74 114" stroke="#fff" stroke-width="5" stroke-linecap="round"/><path d="M58 98 L54 114 M70 98 L74 114" {W(1.4)}/>
<path d="M46 92 L38 98 M82 92 L90 98" {W(1.6)}/>
<path d="M76 74 L90 64" {W(2.4)}/><rect x="88" y="58" width="10" height="7" rx="3" fill="#C8C8D8" {W(2)}/>
<path d="M14 66 Q40 74 64 64 Q88 54 112 64" fill="none" stroke="#FFD8B8" stroke-width="0"/>
{limb("M34 58 L18 50", "#FFD8B8", 6)}{limb("M38 62 L28 72", "#FFD8B8", 6)}{limb("M76 56 L94 48", "#FFD8B8", 6)}{limb("M74 60 L92 66", "#FFD8B8", 6)}
<path d="M38 52 Q56 46 76 52 Q78 64 56 66 Q36 64 38 52Z" fill="#FF8A3A" {W(2.8)}/>
<circle cx="30" cy="46" r="11" fill="#FFD8B8" {W(2.8)}/><path d="M20 42 Q22 32 32 34 Q40 36 40 44Z" fill="#FFE45A" {W(2)}/>
{eye(28, 48, .4)}<path d="M24 52 Q27 54 30 52" fill="none" {W(1.8)}/>''')

# 28. Splash (Бакунинская) — водяная корона всплеска, из неё торчат ноги ныряльщика
I["splash-bakuninskaya"] = ("белая корона брызг от прыжка в воду", "из центра всплеска торчат только ножки маленького ныряльщика в полосатых плавках", ("#EAF8FF", "#1A8AE0"), f'''
<rect x="-2" y="76" width="132" height="54" fill="#2E9AE8" {W(2.4)}/>
<path d="M16 82 L24 52 L32 72 L40 38 L50 68 L58 30 L68 66 L78 34 L86 68 L96 44 L102 70 L112 56 L112 84 Q64 96 16 84Z" fill="#fff" {W(3)}/>
<path d="M30 80 Q64 90 98 80" fill="none" stroke="#9AD8FF" stroke-width="3"/>
<circle cx="22" cy="40" r="3.4" fill="#fff" {W(1.6)}/><circle cx="104" cy="30" r="3.4" fill="#fff" {W(1.6)}/><circle cx="46" cy="22" r="2.6" fill="#fff" {W(1.4)}/><circle cx="86" cy="18" r="2.6" fill="#fff" {W(1.4)}/>
<path d="M54 68 Q50 56 52 46 H76 Q78 56 74 68Z" fill="#E8384A" {W(2.8)}/><path d="M53 52 H75 M53 60 H75" stroke="#fff" stroke-width="3"/>
{limb("M58 46 L54 20", "#FFD8B8", 8)}{limb("M70 46 L76 20", "#FFD8B8", 8)}
<path d="M48 22 Q52 12 58 18Z M82 22 Q78 12 72 18Z" fill="#FFD8B8" {W(2.2)}/>''')

# 29. «Архимед» (Дубна) — бородатый Архимед в ванне кричит «Эврика!»
I["pool-arkhimed-dubna"] = ("весёлый бородатый Архимед в лавровом венке", "сидит в переполненной ванне с резиновой уточкой и радостно поднимает палец — «Эврика!»", ("#FFF8E8", "#C8A060"), f'''
<path d="M0 116 H128 V128 H0Z" fill="#8AD0F0" {W(2.4)}/>
<path d="M14 72 H114 Q112 106 92 110 H36 Q16 106 14 72Z" fill="#fff" {W(3)}/><path d="M36 110 L32 120 M92 110 L96 120" {W(4)}/>
<path d="M14 72 Q24 64 34 72 Q44 64 54 72 Q64 64 74 72 Q84 64 94 72 Q104 64 114 72" fill="#9AD8FF" {W(2.4)}/>
<path d="M18 74 Q10 90 12 112 M110 76 Q118 92 116 112" fill="none" stroke="#9AD8FF" stroke-width="4" stroke-linecap="round"/>
<circle cx="56" cy="48" r="17" fill="#FFD8B8" {W(3)}/>
<path d="M42 54 Q44 76 56 78 Q68 76 70 54 Q62 60 56 58 Q50 60 42 54Z" fill="#fff" {W(2.6)}/>
<path d="M40 40 Q42 30 48 34 Q50 26 56 30 Q62 26 64 34 Q70 30 72 40" fill="none" stroke="#4AA040" stroke-width="4" stroke-linecap="round"/>
{eye(50, 46, .45)}{eye(62, 46, .45)}<ellipse cx="56" cy="58" rx="3.4" ry="3" fill="{O}"/>
{limb("M74 60 L88 44 L88 30", "#FFD8B8", 6.4)}
{sparkle(100, 26, 6, "#FFE45A")}
<path d="M92 62 Q92 54 98 54 Q104 54 102 60 L108 58 L104 64 Q98 70 92 62Z" fill="#FFD23A" {W(2.2)}/><circle cx="99" cy="58" r="1.2" fill="{O}"/>''')

# 30. «Китёнок» (Саларьевская) — малыш скатывается с голубой водной горки
I["kitenok-salaryevo"] = ("малыш в розовой шапочке на голубой водной горке", "с визгом скатывается по струе воды прямо в детский бассейн", ("#FFEAF4", "#E06AA0"), f'''
<rect x="-2" y="92" width="132" height="38" fill="#4AC0F0" {W(2.4)}/>
<path d="M104 20 V92 M118 20 V92" {W(4)}/><path d="M104 40 H118 M104 58 H118 M104 76 H118" {W(3)}/>
<path d="M104 20 Q60 26 50 60 Q44 84 14 92 L28 98 Q60 92 66 66 Q74 38 112 32Z" fill="#6AB8FF" {W(3)}/>
<path d="M98 28 Q66 34 58 62 Q52 84 24 94" fill="none" stroke="#fff" stroke-width="2.6" stroke-dasharray="6 5"/>
<path d="M18 96 Q12 84 20 80 M26 94 Q24 84 30 80" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
{limb("M42 64 L30 54", "#FFD8B8", 6)}{limb("M54 62 L62 48", "#FFD8B8", 6)}{limb("M40 78 L24 86", "#FFD8B8", 6)}
<path d="M36 62 Q46 54 56 62 L50 80 Q40 82 36 76Z" fill="#FFD23A" {W(2.6)}/>
<circle cx="46" cy="46" r="12" fill="#FFD8B8" {W(2.8)}/><path d="M35 44 Q34 32 46 32 Q58 32 57 44 Q46 38 35 44Z" fill="#FF6AAA" {W(2.4)}/>
{eye(42, 48, .4)}{eye(51, 48, .4)}<ellipse cx="46" cy="54" rx="2.6" ry="2.2" fill="{O}"/>''')

# 31. «Зоркий» (Красногорск, город фотоаппаратов «Зоркий») — фотоаппарат в подводном боксе снимает рыбку
I["pool-zorky"] = ("старый фотоаппарат «Зоркий» в прозрачном подводном боксе", "на дне бассейна у разметки фотографирует рыбку — сверкает вспышка", ("#EAFFF0", "#2A9A60"), f'''
<rect x="-2" y="-2" width="132" height="132" fill="#5ACCE0" opacity=".55"/>
<path d="M0 112 H128" stroke="#1E5A9A" stroke-width="8"/><path d="M0 112 H128" {W(1.4)}/>
<path d="M10 20 Q14 14 18 20 M110 100 Q114 94 118 100" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
<rect x="24" y="44" width="70" height="50" rx="10" fill="#E8F8FF" opacity=".75" {W(3)}/>
<rect x="30" y="54" width="58" height="34" rx="4" fill="#3A3A48" {W(2.6)}/><rect x="30" y="54" width="58" height="8" fill="#C8C8D0" {W(2)}/>
<rect x="36" y="48" width="12" height="7" rx="2" fill="#C8C8D0" {W(2)}/>
<circle cx="59" cy="74" r="13" fill="#C8C8D0" {W(2.6)}/><circle cx="59" cy="74" r="8" fill="#2A2F5A"/><circle cx="56" cy="71" r="2.6" fill="#fff"/>
<circle cx="80" cy="66" r="3" fill="#FFE45A" {W(1.4)}/>
<path d="M94 56 L104 50 M96 66 L108 66 M94 76 L104 82" stroke="#FFF6A0" stroke-width="3" stroke-linecap="round"/>
<path d="M104 30 Q114 22 122 30 Q114 38 104 30Z" fill="#FF8A3A" {W(2.4)}/><path d="M104 30 L96 24 V36Z" fill="#FF8A3A" {W(2.2)}/>
{eye(114, 29, .35)}
<circle cx="36" cy="30" r="3" fill="#fff" {W(1.4)}/><circle cx="44" cy="20" r="2.2" fill="#fff" {W(1.2)}/>
''')

# 32. Aqua Baby Club (Яхромская) — мама держит малыша над водой, он шлёпает ладошками
I["aquababy-yakhromskaya"] = ("мама в бирюзовом купальнике с малышом в голубом подгузнике для плавания", "держит его на вытянутых руках над водой, малыш шлёпает ладошками и смеётся", ("#F4F0FF", "#8A8AE0"), f'''
<path d="M0 82 Q24 76 48 82 T96 82 T128 82 V128 H0Z" fill="#6AC8F0" {W(2.4)}/>
<path d="M26 128 Q24 100 40 92 Q52 88 64 92 L60 128Z" fill="#20B0A0" {W(3)}/>
<circle cx="40" cy="74" r="14" fill="#F8D0B0" {W(3)}/><path d="M26 72 Q24 56 42 56 Q56 58 54 72 Q50 62 40 64 Q30 62 26 72Z" fill="#6A3A2A" {W(2.4)}/>
{eye(36, 76, .45)}{eye(46, 76, .45)}{smile(41, 83, 3, .6)}
{limb("M54 96 L76 78", "#F8D0B0", 6.4)}{limb("M50 104 L80 92", "#F8D0B0", 6.4)}
<circle cx="88" cy="64" r="13" fill="#FFE0C8" {W(3)}/><path d="M80 56 Q84 50 90 52" fill="none" {W(2)}/>
{eye(84, 64, .45)}{eye(93, 64, .45)}<path d="M84 70 Q88 75 92 70Z" fill="#fff" {W(1.8)}/>
<path d="M76 80 Q88 74 100 80 L98 92 Q88 96 78 92Z" fill="#6AA8FF" {W(2.6)}/>
{limb("M100 72 L110 82", "#FFE0C8", 5.6)}{limb("M78 74 L68 66", "#FFE0C8", 5.6)}
<path d="M106 86 L102 78 M114 86 L118 78 M110 88 V80" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

# 33. Z Fencing Club — мальчик в маске Зорро рисует шпагой букву Z
I["zfencing-altufyevskoe"] = ("мальчик-фехтовальщик в чёрной маске Зорро и белом костюме", "делает выпад и шпагой рисует в воздухе сверкающую букву Z", ("#F4F4F8", "#3A3A4A"), f'''
<path d="M70 18 H110 L74 50 H114" fill="none" stroke="#FFE45A" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
{sparkle(114, 50, 6, "#FFE45A")}
<path d="M58 66 L112 50" {W(3)}/><path d="M58 66 L64 60" stroke="#C8C8D0" stroke-width="6" stroke-linecap="round"/>
{limb("M44 88 L28 112", "#fff", 8)}{limb("M54 90 L76 104 L80 118", "#fff", 8)}
<path d="M38 90 Q34 64 46 58 Q58 56 62 62 L56 92Z" fill="#fff" {W(3)}/><path d="M42 72 H60" stroke="#E8384A" stroke-width="3"/>
{limb("M58 64 L58 66", "#fff", 6)}{limb("M40 66 L22 56 L20 44", "#fff", 6)}
<circle cx="48" cy="42" r="13" fill="#FFD8B8" {W(3)}/><path d="M35 38 Q36 28 48 28 Q60 28 61 38 Q48 34 35 38Z" fill="#3A2A20" {W(2)}/>
<path d="M34 42 H62 V48 H34Z" fill="#1A1A24" {W(1.4)}/><ellipse cx="43" cy="45" rx="3" ry="2.2" fill="#fff"/><ellipse cx="54" cy="45" rx="3" ry="2.2" fill="#fff"/>
<circle cx="43" cy="45" r="1.4" fill="{O}"/><circle cx="54" cy="45" r="1.4" fill="{O}"/>
<path d="M44 51 Q48 54 52 51" fill="none" {W(1.8)}/>''')

# 34. «Игнис» (лёгкая атлетика) — девочка-барьеристка перелетает барьер
I["ignis-athletics-tenisty"] = ("девочка-барьеристка с огненно-рыжим хвостиком", "перелетает через бело-красный барьер на беговой дорожке, вытянув ножку вперёд", ("#FFF0E0", "#E04A20"), f'''
<path d="M0 104 H128 V128 H0Z" fill="#D8503A" {W(2.4)}/><path d="M0 114 H128" stroke="#fff" stroke-width="2.4"/>
<path d="M40 104 V80 M84 104 V80" {W(4)}/><rect x="36" y="74" width="52" height="9" fill="#fff" {W(2.6)}/><path d="M46 74 V83 M58 74 V83 M70 74 V83" stroke="#E8384A" stroke-width="6"/><rect x="36" y="74" width="52" height="9" fill="none" {W(2.6)}/>
{limb("M58 58 L80 54 L98 60", "#FFD8B8", 6.6)}{limb("M54 60 L40 66 L30 56", "#FFD8B8", 6.6)}
<path d="M94 56 L104 58 L102 64 L94 64Z" fill="#2A8AE8" {W(2)}/><path d="M26 52 L32 54 L30 60 L24 58Z" fill="#2A8AE8" {W(2)}/>
<path d="M50 60 Q48 42 60 38 Q70 38 70 48 L64 62Z" fill="#FFD23A" {W(2.8)}/>
{limb("M66 42 L86 34", "#FFD8B8", 5.6)}{limb("M56 42 L40 32", "#FFD8B8", 5.6)}
<circle cx="68" cy="26" r="12" fill="#FFD8B8" {W(2.8)}/>
<path d="M57 22 Q60 12 70 14 Q78 16 80 24 Q70 18 57 22Z" fill="#E86A20" {W(2)}/>
<path d="M58 18 Q44 10 40 18 Q44 22 56 22" fill="#E86A20" {W(2.2)}/>
{eye(68, 28, .4)}{eye(76, 27, .4)}<path d="M70 34 Q74 36 77 33" fill="none" {W(1.8)}/>
<path d="M14 40 H26 M10 48 H22" stroke="#fff" stroke-width="3" stroke-linecap="round"/>''')

# 35. Шахматная школа №1 (в библиотеке Голицына) — раскрытая книга со страницами-доской
I["chess1-golitsyno"] = ("раскрытая книга, страницы которой — шахматная доска", "лежит на библиотечном столе, а на её клетках стоит чёрный конь-читатель и разглядывает строчки", ("#FFF8EC", "#9A6A3A"), f'''
<path d="M0 104 H128 V128 H0Z" fill="#B07840" {W(2.4)}/>
<path d="M10 98 L64 104 L118 98 L112 54 L64 60 L16 54Z" fill="#7A3A2A" {W(3)}/>
<path d="M16 92 L64 98 L112 92 L106 50 Q84 44 64 54 Q44 44 22 50Z" fill="#FFF6E0" {W(3)}/>
<path d="M64 54 V98" {W(2.4)}/>
<path d="M28 58 L38 57 L39 67 L29 68Z M48 56 L58 57 L58 67 L49 66Z M29 78 L39 77 L40 87 L30 88Z M49 76 L58 77 L59 87 L50 86Z M39 67 L49 66 L49 76 L40 77Z" fill="#9A6A3A"/>
<path d="M70 57 L80 56 L80 66 L70 67Z M90 57 L100 58 L100 68 L91 67Z M80 66 L90 67 L91 77 L81 77Z M70 77 L80 77 L81 87 L71 88Z M91 77 L101 78 L101 88 L92 87Z" fill="#9A6A3A"/>
<path d="M78 72 Q72 52 82 36 Q90 26 100 32 L104 42 L96 44 L92 50 Q100 60 96 72Z" fill="#2A2A3A" {W(2.6)}/>
<path d="M74 72 H100 V78 H74Z" fill="#2A2A3A" {W(2.4)}/>
<path d="M86 30 L90 22 L94 30" fill="#2A2A3A" {W(2.2)}/>
<circle cx="92" cy="38" r="2.6" fill="#fff"/><circle cx="92" cy="38" r="1.2" fill="{O}"/>
<path d="M32 40 Q36 30 46 34 M20 30 Q26 22 34 26" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 36. «Варяг» (стрельба из лука) — мальчик-варяг в рогатом шлеме натягивает лук
I["varyag-archery"] = ("мальчик-варяг в рогатом шлеме", "натягивает большой деревянный лук, целясь в мишень у края круга", ("#F6F0E4", "#8A7A5A"), f'''
<circle cx="112" cy="60" r="19" fill="#fff" {W(3)}/><circle cx="112" cy="60" r="13" fill="#E8384A"/><circle cx="112" cy="60" r="8" fill="#2A8AE8"/><circle cx="112" cy="60" r="3.6" fill="#FFD23A"/>
<path d="M52 22 Q80 60 52 98" fill="none" {W(7)}/><path d="M52 22 Q80 60 52 98" fill="none" stroke="#B87840" stroke-width="3.4"/>
<path d="M52 22 L34 60 L52 98" fill="none" stroke="{O}" stroke-width="1.4"/>
<path d="M34 60 H92" {W(2.6)}/><path d="M94 60 L84 55 L86 60 L84 65Z" fill="#C8C8D0" {W(1.8)}/><path d="M34 60 L28 55 M34 60 L28 65" stroke="#E8384A" stroke-width="2.6"/>
<path d="M2 128 Q2 84 22 76 Q40 74 44 92 L42 128Z" fill="#4A7AC0" {W(3)}/><path d="M6 104 H42" stroke="#C88A3A" stroke-width="5"/>
{limb("M30 82 L34 62", "#FFD8B8", 6.4)}{limb("M36 86 L64 62", "#FFD8B8", 6.4)}
<circle cx="22" cy="58" r="13" fill="#FFD8B8" {W(3)}/>
<path d="M8 54 Q8 38 22 38 Q36 38 36 54Z" fill="#B8B8C8" {W(2.6)}/><path d="M8 54 H36" stroke="#C88A3A" stroke-width="4"/>
<path d="M10 46 Q0 40 2 26 Q8 36 14 40Z M34 46 Q44 40 42 26 Q36 36 30 40Z" fill="#FFF4D8" {W(2.4)}/>
<path d="M10 62 Q8 72 12 78 M34 62 Q36 72 32 78" fill="none" stroke="#E8A030" stroke-width="4" stroke-linecap="round"/>
{eye(18, 60, .4)}{eye(27, 60, .4)}<path d="M19 67 Q23 69 27 66" fill="none" {W(1.8)}/>''')

# 37. Khimki Badminton Club (ДС «Динамо») — девочка-бадминтонистка в высоком прыжке
I["khimki-badminton-dinamo"] = ("девочка-бадминтонистка в бело-голубой форме «Динамо» с двумя косичками", "в высоком прыжке тянется ракеткой к волану под самым потолком зала", ("#EAF2FF", "#1E4AA0"), f'''
<path d="M0 116 H128 V128 H0Z" fill="#E0B070" {W(2.4)}/>
<path d="M94 14 L104 26 L96 30 L88 20Z" fill="#fff" {W(2.2)}/><circle cx="100" cy="30" r="5" fill="#FFE45A" {W(2)}/>
<path d="M86 12 L92 18 M98 8 L100 16" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
{limb("M72 50 L82 34", "#FFD8B8", 6)}
<path d="M82 34 L86 26" {W(3)}/><ellipse cx="88" cy="18" rx="8" ry="10" fill="#fff" {W(2.6)} transform="rotate(25 88 18)"/>
<path d="M84 14 L92 22 M86 10 L94 18 M82 18 L90 26" stroke="#9AB0D8" stroke-width="1.2"/>
{limb("M52 52 L36 44", "#FFD8B8", 6)}
<path d="M50 78 Q48 52 62 48 Q74 48 74 62 L70 80Z" fill="#fff" {W(2.8)}/><path d="M52 62 H72" stroke="#2A5AC8" stroke-width="4"/>
{limb("M56 80 L48 98 L40 100", "#FFD8B8", 6.4)}{limb("M66 80 L76 94 L72 104", "#FFD8B8", 6.4)}
<path d="M34 98 L44 98 L44 104 L34 104Z M68 102 L78 102 L78 108 L68 108Z" fill="#2A5AC8" {W(2)}/>
<circle cx="60" cy="34" r="12" fill="#FFD8B8" {W(2.8)}/><path d="M48 32 Q48 20 60 20 Q72 20 72 32 Q60 26 48 32Z" fill="#3A2A20" {W(2)}/>
<path d="M48 30 Q40 34 42 44 M72 30 Q80 34 78 44" fill="none" stroke="#3A2A20" stroke-width="4" stroke-linecap="round"/>
{eye(57, 34, .4)}{eye(65, 33, .4)}<ellipse cx="61" cy="40" rx="2" ry="1.8" fill="{O}"/>''')

# 38. Nevsky Bears (Электролитный) — мальчик-либеро в падении рыбкой спасает мяч
I["nevsky-bears-nagornaya"] = ("мальчик-либеро в красной футболке и наколенниках", "в падении рыбкой вытягивает руку и спасает мяч в сантиметре от паркета", ("#FFEAEA", "#C02A3A"), f'''
<path d="M0 100 H128 V128 H0Z" fill="#E8B878" {W(2.4)}/><path d="M0 112 H128" stroke="#fff" stroke-width="2.4"/>
<circle cx="98" cy="84" r="12" fill="#fff" {W(2.6)}/><path d="M90 76 Q98 84 92 94 M98 72 Q102 84 110 88 M88 84 Q98 86 106 76" fill="none" stroke="#2A5AC8" stroke-width="2.4"/>
<path d="M104 64 L108 58 M112 70 L118 66" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<path d="M30 82 Q36 70 58 70 Q72 72 72 84 Q60 92 36 90Z" fill="#D8303A" {W(3)}/>
{limb("M70 80 L88 90", "#FFD8B8", 6.4)}{limb("M68 76 L82 64", "#FFD8B8", 6)}
{limb("M32 84 L12 76", "#FFD8B8", 7)}{limb("M34 88 L14 96", "#FFD8B8", 7)}
<rect x="18" y="72" width="8" height="8" rx="2" fill="#2A2F4A" {W(1.6)}/><rect x="20" y="90" width="8" height="8" rx="2" fill="#2A2F4A" {W(1.6)}/>
<circle cx="78" cy="58" r="11" fill="#FFD8B8" {W(2.8)}/><path d="M68 52 Q72 44 82 46 Q88 50 88 56 Q78 50 68 52Z" fill="#E8A030" {W(2)}/>
{eye(78, 60, .4)}{eye(85, 61, .4)}<ellipse cx="80" cy="66" rx="2" ry="1.6" fill="{O}"/>
<path d="M36 108 H60" stroke="#fff" stroke-width="3" stroke-linecap="round"/>''')

# 39. «Партия» (настольный теннис) — стол для пинг-понга на ножках, по нему скачет шарик
I["partiya-tabletennis"] = ("зелёный стол для настольного тенниса на четырёх ножках с глазками на сетке", "переминается с ножки на ножку, по нему скачет белый шарик", ("#EFFFEA", "#2E8A3E"), f'''
<path d="M10 70 L40 50 H118 L94 70Z" fill="#2A7AC8" {W(3)}/>
<path d="M10 70 H94 V76 H10Z" fill="#1A5A9A" {W(2.6)}/><path d="M94 70 L118 50 V56 L94 76Z" fill="#1A5A9A" {W(2.4)}/>
<path d="M52 70 L79 50" stroke="#fff" stroke-width="2.4"/><path d="M12 70 L42 50 M92 70 L116 50" stroke="#fff" stroke-width="1.6"/>
<path d="M50 70 L77 50 L77 40 L50 60Z" fill="#fff" opacity=".7" {W(2.4)}/>
<path d="M54 62 L74 48 M54 66 L74 52" stroke="#9AA" stroke-width="1"/>
{eye(58, 58, .4)}{eye(68, 51, .4)}
<path d="M20 76 L14 108 M36 76 L40 106 M84 76 L80 108 M100 66 L108 98" {W(4)}/>
<path d="M8 108 H20 M34 106 H46 M74 108 H86 M102 98 H114" {W(4)}/>
<circle cx="34" cy="30" r="6" fill="#fff" {W(2.2)}/><path d="M38 38 Q44 52 46 58 M24 38 Q22 44 20 46" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="3 4"/>
<path d="M90 28 Q100 20 108 28 Q102 36 90 28Z" fill="#E8384A" {W(2.2)}/><path d="M100 32 L104 42" {W(3)}/>''')

# 40. ДК им. Конина (Егорьевск) — маска комедии выглядывает из-за красного занавеса
I["egoryevsk-dk-konina"] = ("золотая театральная маска комедии", "выглядывает из-за тяжёлого красного занавеса с кистями и подмигивает зрителям", ("#FFF0E8", "#7A1A2A"), f'''
<path d="M0 0 H128 V20 H0Z" fill="#B8203A" {W(2.4)}/>
<path d="M4 20 Q14 30 24 20 Q34 30 44 20 Q54 30 64 20 Q74 30 84 20 Q94 30 104 20 Q114 30 124 20" fill="#B8203A" {W(2.4)}/>
<path d="M-4 20 H52 Q50 70 58 128 H-4Z" fill="#C8283E" {W(3)}/><path d="M10 24 Q14 76 18 128 M28 24 Q30 76 36 128" stroke="#8A1428" stroke-width="2.4" fill="none"/>
<path d="M132 20 H90 Q96 70 92 128 H132Z" fill="#C8283E" {W(3)}/><path d="M118 24 Q114 76 112 128 M104 24 Q104 76 102 128" stroke="#8A1428" stroke-width="2.4" fill="none"/>
<path d="M54 64 Q60 70 56 78" {W(3)}/><circle cx="56" cy="80" r="4" fill="#FFD23A" {W(2)}/>
<path d="M50 48 Q72 40 94 48 Q98 76 72 94 Q46 76 50 48Z" fill="#FFD23A" {W(3)}/>
<path d="M58 58 Q62 54 66 58" fill="none" {W(2.6)}/>
<path d="M76 56 Q82 50 88 56 Q82 62 76 56Z" fill="#7A1A2A" {W(2)}/>
<path d="M60 70 Q72 84 86 70 Q72 76 60 70Z" fill="#7A1A2A" {W(2.4)}/>
<ellipse cx="57" cy="66" rx="3.4" ry="2" fill="#FF7FA8" opacity=".7"/><ellipse cx="88" cy="66" rx="3.4" ry="2" fill="#FF7FA8" opacity=".7"/>
{sparkle(70, 36, 4)}{sparkle(100, 100, 3.4)}''')


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
