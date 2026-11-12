"""Иконки робота cafes, 2026-11-12 (09 UTC), вторая партия. Каждая придумана отдельно (правило АБСОЛЮТНОЙ
уникальности): герои и сцены сверены поиском по icons-src/subjects.txt; палитры фона — свои.
Запуск: python3 tools/icons_cafes_1112i.py [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "zi_smoke": ("#FFF0E6", "#D98B5F"),
    "zi_pond": ("#E3F7FF", "#4FA3C7"),
    "zi_spin": ("#FFF0FA", "#C779C9"),
    "zi_study": ("#F7F1E6", "#A68A64"),
    "zi_bath": ("#EAFBF7", "#4FB8A3"),
    "zi_sunrise": ("#FFF8E0", "#F2B63D"),
    "zi_stage": ("#FBE8FF", "#8A5BC2"),
    "zi_parade": ("#FFEFEA", "#E26D5A"),
    "zi_roll": ("#EFF7E4", "#8DBA54"),
    "zi_fire": ("#FFF1E8", "#F07F4F"),
    "zi_nut": ("#F8F3EA", "#B79A6E"),
    "zi_duel": ("#EEF0FF", "#6672C9"),
    "zi_family": ("#FFF6EF", "#E4A07D"),
    "zi_race": ("#ECFFF0", "#58B36F"),
    "zi_syrup": ("#FFF5E0", "#D49A3A"),
    "zi_attic": ("#F0EEFF", "#9A8FD8"),
    "zi_lamp": ("#E8EEF8", "#5C6E9E"),
    "zi_snow": ("#F2FAFF", "#79B8E0"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. ГрильГрад (г. Московский): ресторан с шашлыком — мангал сам раздувает угли веером
add("cafe-grill-grad-moskovsky",
    "чёрный мангал на тонких ножках с мордашкой на боку и красными угольками",
    "сам раздувает свои угли круглым бумажным веером, а над ним вьётся дымок колечками",
    "zi_smoke", f'''
<path d="M40 86 L34 116 M88 86 L94 116 M64 88 L64 116" {W(3.4)}/>
<path d="M24 60 L104 60 L96 90 L32 90Z" fill="#4A4458" {W(3)}/>
<path d="M30 60 Q40 50 50 60 Q60 48 70 60 Q80 50 90 60 Q96 54 100 60" fill="#FF6B3D" {W(2.4)}/>
<circle cx="44" cy="56" r="3" fill="#FFD23F"/><circle cx="66" cy="54" r="3" fill="#FFD23F"/><circle cx="86" cy="56" r="2.6" fill="#FFD23F"/>
{eye(54, 74, 0.85)}{eye(74, 74, 0.85)}
<path d="M58 81 Q64 86 70 81" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"/>
<ellipse cx="44" cy="80" rx="4" ry="2.2" fill="#FF7FA8" opacity=".8"/><ellipse cx="84" cy="80" rx="4" ry="2.2" fill="#FF7FA8" opacity=".8"/>
<path d="M104 70 L114 60" {W(3)}/>
<circle cx="114" cy="50" r="12" fill="#FFE07A" {W(2.6)}/>
<path d="M114 38 L114 62 M102 50 L126 50 M106 42 L122 58 M106 58 L122 42" stroke="#E0A84A" stroke-width="1.6"/>
<circle cx="50" cy="38" r="7" fill="none" stroke="#FFFFFF" stroke-width="3"/>
<circle cx="64" cy="24" r="9" fill="none" stroke="#FFFFFF" stroke-width="3"/>
<circle cx="80" cy="36" r="5" fill="none" stroke="#FFFFFF" stroke-width="3"/>
''')

# 2. Здрасте (Борисовские Пруды): песочное колечко с орешками пускает кораблик по пруду
add("cafe-zdraste-borisovskie-prudy-26",
    "песочное колечко с дроблёными орешками на глазури",
    "сидит на деревянных мостках у пруда и пускает по воде бумажный кораблик",
    "zi_pond", f'''
<rect x="0" y="84" width="128" height="46" fill="#5DB7DE"/>
<path d="M0 92 q10 -4 20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0" fill="none" stroke="#FFFFFF" stroke-width="2.4" opacity=".7"/>
<rect x="4" y="76" width="66" height="10" rx="2" fill="#C98B52" {W(2.6)}/>
<path d="M14 86 L14 112 M58 86 L58 112" stroke="#8A5A33" stroke-width="5"/>
<circle cx="38" cy="54" r="24" fill="#E7B66E" {W(3)}/>
<circle cx="38" cy="54" r="9" fill="#9FD3EC" {W(2.6)}/>
<path d="M16 46 Q38 26 60 46 Q56 34 38 30 Q20 34 16 46Z" fill="#FFF3DE" {W(2)}/>
<g fill="#A0612F"><circle cx="26" cy="40" r="1.8"/><circle cx="34" cy="34" r="1.6"/><circle cx="46" cy="36" r="1.8"/><circle cx="52" cy="42" r="1.5"/></g>
{eye(28, 60, 0.7)}{eye(48, 60, 0.7)}
<path d="M33 69 Q38 72 43 69" fill="none" {W(2)}/>
<path d="M30 76 L28 84 M46 76 L48 84" {W(2.6)}/>
<path d="M58 62 L78 80" {W(2.4)}/>
<path d="M76 98 L112 98 L104 108 L84 108Z" fill="#FFFFFF" {W(2.4)}/>
<path d="M94 98 L94 76 L106 96Z" fill="#FFFFFF" {W(2.2)}/>
{sparkle(104, 30, 5)}{sparkle(82, 50, 3.5)}
''')

# 3. Тануки (Борисовские Пруды): ролл «Калифорния» крутится на карусели-чашке
add("cafe-tanuki-borisovskie-prudy-10",
    "ролл «Калифорния» в оранжевой шубке из икры масаго",
    "крутится на детской карусели-чашке с горошками и кричит «ура»",
    "zi_spin", f'''
<ellipse cx="64" cy="108" rx="44" ry="9" fill="#E7C7F2" {W(2.6)}/>
<path d="M30 76 Q30 104 64 104 Q98 104 98 76Z" fill="#5DB7DE" {W(3)}/>
<ellipse cx="64" cy="76" rx="34" ry="8" fill="#BDE7F7" {W(2.6)}/>
<g fill="#FFFFFF"><circle cx="42" cy="90" r="3"/><circle cx="58" cy="96" r="3"/><circle cx="76" cy="94" r="3"/><circle cx="90" cy="86" r="2.6"/></g>
<path d="M98 82 q12 0 10 10 q-2 8 -12 6" fill="none" {W(3)}/>
<rect x="44" y="36" width="40" height="40" rx="12" fill="#FF9A3C" {W(3)}/>
<g fill="#FFC27A"><circle cx="50" cy="42" r="2"/><circle cx="60" cy="40" r="2"/><circle cx="72" cy="42" r="2"/><circle cx="80" cy="46" r="2"/><circle cx="48" cy="54" r="2"/><circle cx="80" cy="60" r="2"/><circle cx="48" cy="68" r="2"/><circle cx="78" cy="70" r="2"/></g>
<circle cx="64" cy="56" r="13" fill="#FFFFFF" {W(2.4)}/>
<circle cx="60" cy="54" r="4" fill="#9CCB5A"/><circle cx="69" cy="58" r="3.6" fill="#F59BAF"/>
{eye(57, 49, 0.55)}{eye(71, 49, 0.55)}
<ellipse cx="64" cy="64" rx="3.4" ry="3" fill="#8A2E3A"/>
<path d="M44 46 L32 30 M84 46 L96 30" {W(3)}/>
<path d="M20 60 q-6 -8 0 -16 M108 60 q6 -8 0 -16" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>
{sparkle(24, 28, 4)}{sparkle(108, 22, 5)}
''')

# 4. Додо Пицца (Боровское ш., рядом Переделкино — посёлок писателей): кусок пиццы-писатель с пером
add("cafe-dodo-borovskoe-30a",
    "треугольный кусок пиццы-писатель в круглых очках",
    "пишет гусиным пером толстую книгу за деревянной конторкой с чернильницей",
    "zi_study", f'''
<path d="M24 82 L104 70 L104 80 L24 92Z" fill="#B88350" {W(2.8)}/>
<path d="M34 90 L34 120 M96 80 L96 118" stroke="#8A5A33" stroke-width="5"/>
<path d="M44 76 L92 70 L92 62 L44 68Z" fill="#FFFFFF" {W(2.4)}/>
<path d="M50 70 L86 65 M50 74 L80 70" stroke="#C9D6EA" stroke-width="1.8"/>
<g transform="rotate(10 50 50)">
<path d="M30 20 L70 20 L50 70Z" fill="#F7C548" {W(3)}/>
<path d="M27 15 Q50 6 73 15 L70 22 Q50 14 30 22Z" fill="#D9893A" {W(2.6)}/>
<circle cx="40" cy="30" r="3.4" fill="#D9363E"/><circle cx="58" cy="44" r="3" fill="#D9363E"/>
<circle cx="44" cy="34" r="6" fill="#FFFFFF" fill-opacity=".5" {W(2.2)}/><circle cx="58" cy="34" r="6" fill="#FFFFFF" fill-opacity=".5" {W(2.2)}/>
<path d="M50 34 L52 34" {W(2)}/>
{eye(44, 34, 0.5)}{eye(58, 34, 0.5)}
<path d="M47 46 Q51 49 55 46" fill="none" {W(1.8)}/>
</g>
<path d="M70 66 Q86 34 106 20 Q96 44 74 66Z" fill="#FFFFFF" {W(2.4)}/>
<path d="M74 64 Q90 40 104 24" fill="none" {W(1.6)}/>
<path d="M98 72 L112 70 L112 62 Q106 56 100 62Z" fill="#3E3A8C" {W(2.2)}/>
{sparkle(20, 34, 4)}{sparkle(116, 40, 4)}
''')

# 5. Тануки (Боровское ш., 31): нигири с креветкой принимает ванну в соуснице
add("cafe-tanuki-borovskoe-31",
    "нигири с розово-белой креветкой поверх рисового брусочка",
    "принимает ванну в маленькой соуснице с соевым соусом и трёт спинку щёточкой",
    "zi_bath", f'''
<path d="M18 74 L110 74 Q106 108 64 110 Q22 108 18 74Z" fill="#FFFFFF" {W(3)}/>
<path d="M24 78 L104 78 Q100 96 64 98 Q28 96 24 78Z" fill="#6B3A22"/>
<path d="M30 98 L26 112 M98 98 L102 112" {W(3)}/>
<rect x="38" y="52" width="52" height="28" rx="10" fill="#FFFDF5" {W(3)}/>
<path d="M34 54 Q46 30 64 34 Q82 30 96 52 Q82 46 64 48 Q46 46 34 54Z" fill="#FF9F80" {W(3)}/>
<path d="M46 44 L50 50 M60 38 L62 46 M74 40 L72 47 M86 46 L82 51" stroke="#FFFFFF" stroke-width="2.6"/>
<path d="M96 52 L108 40 L110 52Z" fill="#FF6B4A" {W(2.4)}/>
{eye(54, 62, 0.75)}{eye(72, 62, 0.75)}
<path d="M58 70 Q63 74 68 70" fill="none" {W(2.2)}/>
<path d="M30 66 L18 44" stroke="#C98B52" stroke-width="3.4" stroke-linecap="round"/>
<rect x="10" y="34" width="14" height="10" rx="3" fill="#F2C84B" {W(2.2)} transform="rotate(-30 17 39)"/>
<circle cx="40" cy="22" r="5" fill="#FFFFFF" fill-opacity=".8" {W(1.8)}/><circle cx="54" cy="16" r="3.4" fill="#FFFFFF" fill-opacity=".8" {W(1.6)}/><circle cx="104" cy="24" r="4" fill="#FFFFFF" fill-opacity=".8" {W(1.6)}/>
''')

# 6. Здрасте (Солнцево): тост «яйцо в корзинке» восходит над горизонтом, как солнце
add("cafe-zdraste-proizvodstvennaya-8",
    "тост «яйцо в корзинке» — ломтик хлеба с глазуньей в круглом окошке",
    "поднимается над горизонтом, как утреннее солнце, раскинув лучи из картошки-соломки",
    "zi_sunrise", f'''
<g stroke="{O}" stroke-width="2" fill="#FFD36B">
<rect x="61" y="6" width="6" height="18" rx="2"/>
<rect x="61" y="6" width="6" height="18" rx="2" transform="rotate(35 64 62)"/>
<rect x="61" y="6" width="6" height="18" rx="2" transform="rotate(-35 64 62)"/>
<rect x="61" y="6" width="6" height="18" rx="2" transform="rotate(70 64 62)"/>
<rect x="61" y="6" width="6" height="18" rx="2" transform="rotate(-70 64 62)"/>
</g>
<path d="M32 96 L32 50 Q32 32 48 34 Q56 24 64 30 Q72 24 80 34 Q96 32 96 50 L96 96Z" fill="#D99A4A" {W(3)}/>
<path d="M38 96 L38 52 Q38 40 50 41 Q57 33 64 37 Q71 33 78 41 Q90 40 90 52 L90 96Z" fill="#FFE7B8"/>
<circle cx="64" cy="66" r="18" fill="#FFFFFF" {W(2.4)}/>
<circle cx="64" cy="66" r="9" fill="#FFB020" {W(2.2)}/>
{eye(52, 50, 0.7)}{eye(76, 50, 0.7)}
<rect x="0" y="94" width="128" height="34" fill="#6DBF73"/>
<path d="M0 94 Q64 86 128 94" fill="none" {W(2.8)}/>
<ellipse cx="44" cy="58" rx="3.6" ry="2" fill="#FF7FA8" opacity=".7"/><ellipse cx="84" cy="58" rx="3.6" ry="2" fill="#FF7FA8" opacity=".7"/>
''')

# 7. Здрасте (Сельскохозяйственная ул.): безе «Павлова» танцует на сцене в пачке
add("cafe-zdraste-selskokhozyaystvennaya-38",
    "пышное безе «Павлова» с белыми сливками и ягодами на макушке",
    "танцует на маленькой сцене в розовой балетной пачке под лучом прожектора",
    "zi_stage", f'''
<path d="M44 0 L84 0 L110 112 L18 112Z" fill="#FFF6C4" opacity=".55"/>
<rect x="0" y="108" width="128" height="22" fill="#9B5C2E"/>
<path d="M0 108 L128 108" {W(2.8)}/>
<path d="M64 104 L60 88 M64 104 L72 90" {W(3)}/>
<path d="M30 80 Q64 66 98 80 Q90 92 64 90 Q38 92 30 80Z" fill="#FF9EC4" {W(2.8)}/>
<path d="M36 82 L32 88 M48 86 L46 92 M64 88 L64 94 M80 86 L82 92 M92 82 L96 88" {W(2)}/>
<path d="M40 76 Q36 46 64 40 Q92 46 88 76Z" fill="#FFFDF5" {W(3)}/>
<path d="M46 46 Q50 36 58 40 Q64 30 72 40 Q80 36 82 46" fill="#FFFFFF" {W(2.4)}/>
<circle cx="56" cy="36" r="4.4" fill="#D9264E" {W(1.8)}/><circle cx="68" cy="32" r="4" fill="#5A3C8C" {W(1.8)}/><circle cx="76" cy="38" r="3.6" fill="#D9264E" {W(1.8)}/>
{eye(56, 60, 0.75)}{eye(72, 60, 0.75)}
<path d="M60 68 Q64 71 68 68" fill="none" {W(2)}/>
<path d="M40 60 Q24 48 22 34 M88 60 Q104 48 106 34" fill="none" {W(3)}/>
{sparkle(20, 24, 5)}{sparkle(110, 22, 5)}
''')

# 8. PizzAmore: маленький барабанщик стучит гриссини по пицце, как по барабану
add("cafe-pizzamore-selskokhozyaystvennaya-35",
    "маленький барабанщик в красном мундире с золотыми пуговицами и высоком кивере",
    "стучит хлебными палочками-гриссини по круглой пицце, висящей на ремне, как по барабану",
    "zi_parade", f'''
<rect x="50" y="10" width="28" height="26" rx="4" fill="#2F3C7E" {W(2.8)}/>
<path d="M50 34 L78 34" stroke="#FFD23F" stroke-width="3"/>
<circle cx="64" cy="8" r="4" fill="#FFFFFF" {W(2)}/>
<circle cx="64" cy="48" r="14" fill="#FFD9B8" {W(3)}/>
{eye(58, 47, 0.6)}{eye(70, 47, 0.6)}
<path d="M60 54 Q64 57 68 54" fill="none" {W(1.8)}/>
<path d="M44 62 L84 62 L88 98 L40 98Z" fill="#D9363E" {W(3)}/>
<g fill="#FFD23F"><circle cx="64" cy="70" r="2"/><circle cx="64" cy="80" r="2"/><circle cx="64" cy="90" r="2"/></g>
<path d="M46 64 L82 96" stroke="#FFFFFF" stroke-width="3"/>
<path d="M54 98 L52 116 M74 98 L76 116" {W(4)}/>
<ellipse cx="64" cy="98" rx="30" ry="11" fill="#E9A84C" {W(3)}/>
<ellipse cx="64" cy="96" rx="24" ry="7.5" fill="#E2463A"/>
<g fill="#FFF6DD"><circle cx="54" cy="96" r="3"/><circle cx="70" cy="94" r="2.6"/><circle cx="76" cy="99" r="2.4"/></g>
<path d="M30 70 L50 92" stroke="#F2D29A" stroke-width="5" stroke-linecap="round"/><path d="M30 70 L50 92" stroke="{O}" stroke-width="1" stroke-dasharray="2 4"/>
<path d="M98 66 L80 92" stroke="#F2D29A" stroke-width="5" stroke-linecap="round"/><path d="M98 66 L80 92" stroke="{O}" stroke-width="1" stroke-dasharray="2 4"/>
<path d="M20 86 l-8 -4 M22 96 l-10 2 M108 86 l8 -4 M106 96 l10 2" {W(2.4)}/>
''')

# 9. Алло! Пицца (Марьино): кусок мясной пиццы катается на роликах
add("cafe-allo-pizza-novomaryinskaya",
    "треугольный кусок мясной пиццы с кружками колбасок и ветчиной",
    "мчится на роликовых коньках с синими колёсиками, развевая сырной ниточкой",
    "zi_roll", f'''
<path d="M0 112 L128 104" stroke="#FFFFFF" stroke-width="3" opacity=".7"/>
<g transform="rotate(-18 64 60)">
<path d="M28 28 L100 28 L64 92Z" fill="#F2C35A" {W(3)}/>
<path d="M24 22 Q64 10 104 22 L100 30 Q64 20 28 30Z" fill="#C97A34" {W(2.8)}/>
<circle cx="48" cy="38" r="5" fill="#B83A3A" {W(1.8)}/><circle cx="78" cy="40" r="5" fill="#B83A3A" {W(1.8)}/><circle cx="64" cy="64" r="4.4" fill="#B83A3A" {W(1.8)}/>
<rect x="58" y="34" width="10" height="7" rx="2" fill="#F59BAF" {W(1.6)}/>
{eye(56, 50, 0.7)}{eye(72, 50, 0.7)}
<path d="M60 57 Q64 61 68 57" fill="none" {W(2)}/>
</g>
<path d="M56 86 L46 100 M72 84 L80 98" {W(3)}/>
<path d="M36 98 L56 98 L56 104 L36 104Z" fill="#E85D75" {W(2.4)}/><circle cx="40" cy="108" r="3.4" fill="#4D7FD6" {W(1.8)}/><circle cx="52" cy="108" r="3.4" fill="#4D7FD6" {W(1.8)}/>
<path d="M72 96 L92 96 L92 102 L72 102Z" fill="#E85D75" {W(2.4)}/><circle cx="76" cy="106" r="3.4" fill="#4D7FD6" {W(1.8)}/><circle cx="88" cy="106" r="3.4" fill="#4D7FD6" {W(1.8)}/>
<path d="M104 40 q10 4 16 -2" fill="none" stroke="#FFE7A0" stroke-width="3" stroke-linecap="round"/>
<path d="M14 54 l-10 0 M16 66 l-12 2 M20 78 l-10 4" {W(2.4)}/>
''')

# 10. Додо Пицца (Южнобутовская): кусок пиццы-пожарный тушит свечку на торте струёй кетчупа
add("cafe-dodo-yuzhnobutovskaya-42",
    "кусок пиццы-пожарный в красной каске",
    "тушит струйкой кетчупа из шланга огонёк свечки на праздничном торте",
    "zi_fire", f'''
<path d="M16 26 L56 26 L36 84Z" fill="#F7C548" {W(3)}/>
<path d="M13 22 Q36 14 59 22 L56 28 Q36 22 16 28Z" fill="#D9893A" {W(2.6)}/>
<circle cx="28" cy="36" r="3" fill="#D9363E"/><circle cx="44" cy="40" r="3" fill="#D9363E"/>
<path d="M16 22 Q16 4 36 4 Q56 4 56 22Z" fill="#E23B2E" {W(2.8)}/>
<rect x="31" y="8" width="10" height="9" rx="2" fill="#FFD23F" {W(1.8)}/>
{eye(30, 46, 0.6)}{eye(42, 46, 0.6)}
<path d="M33 54 Q36 57 39 54" fill="none" {W(1.8)}/>
<path d="M50 54 Q60 60 66 54" fill="none" stroke="#3B3355" stroke-width="5" stroke-linecap="round"/>
<path d="M50 54 Q60 60 66 54" fill="none" stroke="#E2463A" stroke-width="2.6" stroke-linecap="round"/>
<path d="M68 52 Q84 40 94 56" fill="none" stroke="#D9263E" stroke-width="4" stroke-linecap="round"/>
<circle cx="96" cy="60" r="2.6" fill="#D9263E"/><circle cx="92" cy="64" r="2" fill="#D9263E"/>
<path d="M52 96 L120 96 L120 120 L52 120Z" fill="#FFFFFF" {W(3)}/>
<path d="M52 96 Q60 104 68 96 Q76 104 86 96 Q94 104 102 96 Q110 104 120 96" fill="#FF9EC4" {W(2.4)}/>
<rect x="84" y="74" width="7" height="22" rx="2" fill="#7FD3F5" {W(2)}/>
<path d="M87.5 74 Q80 66 87.5 58 Q95 66 87.5 74Z" fill="#FFB020" {W(2)}/>
<circle cx="66" cy="110" r="3" fill="#D9264E"/><circle cx="106" cy="110" r="3" fill="#D9264E"/>
''')

# 11. Макадамия (Южное Бутово): орех макадамия выглядывает из треснувшей скорлупы
add("cafe-makadamiya-venevskaya",
    "круглый орех макадамия кремового цвета",
    "выглядывает из треснувшей коричневой скорлупки, как из окошка, и машет ладошкой",
    "zi_nut", f'''
<ellipse cx="64" cy="112" rx="40" ry="6" fill="#8F7A55" opacity=".35"/>
<path d="M22 70 Q22 110 64 110 Q106 110 106 70 L96 64 L88 74 L78 62 L68 74 L58 62 L48 74 L38 62 L30 72Z" fill="#8A5A33" {W(3)}/>
<path d="M34 92 Q40 100 50 102 M80 102 Q92 98 96 88" fill="none" stroke="#B58A5C" stroke-width="2.6"/>
<circle cx="64" cy="58" r="26" fill="#F6E4C2" {W(3)}/>
<ellipse cx="56" cy="48" rx="8" ry="5" fill="#FFFFFF" opacity=".6"/>
{eye(55, 58, 0.85)}{eye(73, 58, 0.85)}
<path d="M58 68 Q64 73 70 68" fill="none" {W(2.3)}/>
<ellipse cx="46" cy="66" rx="4" ry="2.3" fill="#FF7FA8" opacity=".7"/><ellipse cx="82" cy="66" rx="4" ry="2.3" fill="#FF7FA8" opacity=".7"/>
<path d="M92 50 Q102 36 104 26" fill="none" {W(3)}/>
<circle cx="104" cy="24" r="5" fill="#F6E4C2" {W(2.4)}/>
<path d="M112 16 l5 -4 M114 26 l6 0" {W(2.2)}/>
<path d="M22 40 Q30 30 40 34" fill="none" {W(2.4)}/>
<path d="M40 34 L34 28 L44 28Z" fill="#7BC6A4" {W(1.8)}/>
''')

# 12. Алло! Пицца (Бибирево): две сырные палочки фехтуют
add("cafe-allo-pizza-kostromskaya",
    "золотистая сырная палочка из моцареллы в хрустящей панировке",
    "фехтует со своей сестричкой-палочкой, а между ними тянется сырная нитка",
    "zi_duel", f'''
<rect x="0" y="108" width="128" height="22" fill="#4C5AA8"/>
<g transform="rotate(-20 36 72)">
<rect x="22" y="44" width="28" height="62" rx="12" fill="#E8A43C" {W(3)}/>
<g fill="#C27A22"><circle cx="30" cy="56" r="1.8"/><circle cx="42" cy="66" r="1.8"/><circle cx="32" cy="88" r="1.8"/><circle cx="44" cy="96" r="1.6"/></g>
{eye(31, 72, 0.65)}{eye(42, 72, 0.65)}
<path d="M33 80 Q36.5 83 40 80" fill="none" {W(1.8)}/>
</g>
<g transform="rotate(20 92 72)">
<rect x="78" y="44" width="28" height="62" rx="12" fill="#F2BF5C" {W(3)}/>
<g fill="#C27A22"><circle cx="86" cy="58" r="1.8"/><circle cx="98" cy="64" r="1.8"/><circle cx="88" cy="94" r="1.8"/></g>
{eye(87, 72, 0.65)}{eye(98, 72, 0.65)}
<ellipse cx="92.5" cy="81" rx="2.6" ry="2.4" fill="#8A2E3A"/>
</g>
<path d="M50 52 L84 22" stroke="#C9D6EA" stroke-width="3.4" stroke-linecap="round"/><path d="M50 52 L84 22" {W(1)}/>
<path d="M78 52 L44 22" stroke="#C9D6EA" stroke-width="3.4" stroke-linecap="round"/><path d="M78 52 L44 22" {W(1)}/>
<circle cx="64" cy="37" r="4" fill="#FFFFFF" {W(1.6)}/>
<path d="M52 92 Q64 102 76 92" fill="none" stroke="#FFF2C2" stroke-width="3.4" stroke-linecap="round"/>
{sparkle(64, 16, 5)}
''')

# 13. Семейное кафе (Щербинка): семья пельменей отдыхает в тарелке со сметаной, как в ванне
add("cafe-semeynoe-shcherbinka-chechersky",
    "семья из трёх пельменей — папа, мама и пельмешек-малыш",
    "сидят рядком в глубокой тарелке со сметанным озерцом и укропными веточками",
    "zi_family", f'''
<ellipse cx="64" cy="94" rx="52" ry="18" fill="#FFFFFF" {W(3)}/>
<ellipse cx="64" cy="90" rx="40" ry="11" fill="#FFF8E8"/>
<path d="M28 60 Q28 34 44 34 Q60 34 60 60 Q52 68 44 66 Q36 68 28 60Z" fill="#FFF1D6" {W(3)}/>
<path d="M30 52 Q44 44 58 52" fill="none" stroke="#E5CFA6" stroke-width="2"/>
{eye(39, 52, 0.6)}{eye(50, 52, 0.6)}
<path d="M41 58 Q44.5 61 48 58" fill="none" {W(1.8)}/>
<path d="M68 60 Q68 36 83 36 Q98 36 98 60 Q90 68 83 66 Q76 68 68 60Z" fill="#FFF1D6" {W(3)}/>
<path d="M74 34 Q83 26 92 34" fill="none" stroke="#E85D75" stroke-width="3.4" stroke-linecap="round"/>
{eye(78, 52, 0.6)}{eye(88, 52, 0.6)}
<path d="M80 58 Q83 61 86 58" fill="none" {W(1.8)}/>
<path d="M54 82 Q54 64 64 64 Q74 64 74 82 Q69 86 64 85 Q59 86 54 82Z" fill="#FFF1D6" {W(2.6)}/>
{eye(60, 74, 0.45)}{eye(68, 74, 0.45)}
<path d="M30 92 q6 -8 12 0 M84 94 q6 -8 12 0" fill="none" stroke="#5FAE4E" stroke-width="2.6" stroke-linecap="round"/>
{sparkle(18, 26, 4)}{sparkle(110, 26, 5)}
''')

# 14. Crazy Brothers (Богородское): два брата-бургера скачут наперегонки в мешках
add("cafe-crazy-brothers-khimushina",
    "два брата-бургера в кепках козырьком назад",
    "скачут наперегонки в холщовых мешках по зелёной лужайке",
    "zi_race", f'''
<rect x="0" y="104" width="128" height="26" fill="#7CC36B"/>
<path d="M0 104 Q64 98 128 104" fill="none" {W(2.4)}/>
<g transform="translate(-4 4)">
<path d="M18 70 L56 70 L60 104 L14 104Z" fill="#D9B98A" {W(2.8)}/>
<path d="M16 66 Q16 42 37 42 Q58 42 58 66Z" fill="#E7A24A" {W(2.8)}/>
<rect x="15" y="64" width="44" height="7" rx="3" fill="#6B3A22" {W(2.2)}/>
<path d="M18 36 Q37 26 56 36 L56 44 L18 44Z" fill="#4D7FD6" {W(2.4)}/><path d="M18 40 L8 42" stroke="#4D7FD6" stroke-width="5" stroke-linecap="round"/>
{eye(30, 54, 0.6)}{eye(44, 54, 0.6)}
<path d="M33 60 Q37 63 41 60" fill="none" {W(1.8)}/>
</g>
<g transform="translate(58 -6)">
<path d="M18 70 L56 70 L60 104 L14 104Z" fill="#CFAE7C" {W(2.8)}/>
<path d="M16 66 Q16 42 37 42 Q58 42 58 66Z" fill="#E7A24A" {W(2.8)}/>
<rect x="15" y="64" width="44" height="7" rx="3" fill="#6B3A22" {W(2.2)}/>
<path d="M14 62 L60 62" stroke="#7FC96A" stroke-width="3.4"/>
<path d="M18 36 Q37 26 56 36 L56 44 L18 44Z" fill="#E85D75" {W(2.4)}/><path d="M18 40 L8 42" stroke="#E85D75" stroke-width="5" stroke-linecap="round"/>
{eye(30, 54, 0.6)}{eye(44, 54, 0.6)}
<ellipse cx="37" cy="61" rx="2.6" ry="2.4" fill="#8A2E3A"/>
</g>
<path d="M60 110 q4 -6 8 0 M114 98 q4 -6 8 0" fill="none" {W(2)}/>
<path d="M4 50 l-6 0 M6 60 l-8 2" {W(2.2)}/>
''')

# 15. Тануки (Южнобутовская, 74): стопка японских суфле-панкейков дрожит под сиропом
add("cafe-tanuki-yuzhnobutovskaya-74",
    "три высоких японских суфле-панкейка стопкой с кубиком сливочного масла",
    "покачиваются, как желе, и хихикают под струйкой кленового сиропа из кувшинчика",
    "zi_syrup", f'''
<ellipse cx="60" cy="110" rx="44" ry="8" fill="#FFFFFF" {W(3)}/>
<rect x="30" y="86" width="60" height="22" rx="10" fill="#F6D08A" {W(3)}/>
<rect x="32" y="64" width="56" height="24" rx="10" fill="#F9DA9C" {W(3)}/>
<rect x="34" y="42" width="52" height="24" rx="10" fill="#FCE3AE" {W(3)}/>
<path d="M36 44 Q60 36 84 44" fill="none" stroke="#C98B3A" stroke-width="3"/>
<rect x="52" y="32" width="14" height="10" rx="2" fill="#FFF3A6" {W(2)}/>
{eye(52, 56, 0.6)}{eye(68, 56, 0.6)}<path d="M56 60 Q60 63 64 60" fill="none" {W(1.8)}/>
{eye(50, 76, 0.55)}{eye(70, 76, 0.55)}<path d="M55 81 Q60 84 65 81" fill="none" {W(1.8)}/>
{eye(48, 98, 0.55)}{eye(72, 98, 0.55)}<path d="M54 102 Q60 105 66 102" fill="none" {W(1.8)}/>
<path d="M84 46 Q92 56 88 70 Q90 80 92 88" fill="none" stroke="#B5651D" stroke-width="3.4" stroke-linecap="round"/>
<path d="M92 14 L112 14 L114 28 Q104 34 94 28Z" fill="#FFFFFF" {W(2.6)}/>
<path d="M92 20 L80 34" stroke="#B5651D" stroke-width="3.4" stroke-linecap="round"/>
<path d="M20 50 l-6 -2 M22 68 l-8 0 M22 86 l-6 2" {W(2.2)}/>
''')

# 16. Здрасте (Добролюбова): игровая с лесенкой на антресоль — малыш лезет наверх к мягким матам
add("cafe-zdraste-dobrolyubova-8",
    "малыш в полосатом жёлто-зелёном комбинезоне",
    "лезет по деревянной лесенке на антресоль игровой комнаты, где лежат мягкие маты",
    "zi_attic", f'''
<rect x="60" y="34" width="66" height="10" fill="#C98B52" {W(2.8)}/>
<rect x="64" y="22" width="26" height="12" rx="4" fill="#7BC6A4" {W(2.4)}/>
<rect x="92" y="22" width="26" height="12" rx="4" fill="#F59BAF" {W(2.4)}/>
<path d="M66 44 L66 120 M120 44 L120 120" stroke="#A9744A" stroke-width="5"/>
<path d="M30 120 L52 34 M50 120 L72 34" stroke="#B88350" stroke-width="4.4" stroke-linecap="round"/>
<path d="M33 108 L53 108 M36 94 L56 94 M40 80 L60 80 M44 66 L64 66 M47 52 L67 52" stroke="#B88350" stroke-width="3.6" stroke-linecap="round"/>
<circle cx="46" cy="40" r="12" fill="#FFD9B8" {W(2.8)}/>
<path d="M36 34 Q46 24 56 34" fill="#7A4A2A" {W(2)}/>
{eye(42, 41, 0.55)}{eye(51, 41, 0.55)}
<path d="M44 47 Q46.5 49 49 47" fill="none" {W(1.6)}/>
<path d="M36 52 L58 52 L60 80 L34 80Z" fill="#F6D44A" {W(2.8)}/>
<path d="M35 60 L59 60 M35 70 L60 70" stroke="#7BC6A4" stroke-width="4"/>
<path d="M58 54 L66 48 M36 56 L30 64" {W(3)}/>
<path d="M40 80 L38 92 M54 80 L58 92" {W(3.4)}/>
{sparkle(20, 24, 5)}{sparkle(98, 66, 4)}
''')

# 17. Тануки (ул. Паустовского): мисо-суп читает книжку на скамейке под фонарём
add("cafe-tanuki-paustovskogo-8",
    "чёрная лакированная миска мисо-супа с кубиками тофу и ленточкой водоросли",
    "читает раскрытую книжку, сидя на парковой скамейке под вечерним фонарём",
    "zi_lamp", f'''
<path d="M104 120 L104 30" stroke="#2F3550" stroke-width="4"/>
<path d="M94 30 L114 30 L110 18 L98 18Z" fill="#FFE27A" {W(2.4)}/>
<path d="M88 34 L120 34 L130 120 L80 120Z" fill="#FFF3B0" opacity=".25"/>
<rect x="8" y="94" width="84" height="7" rx="2" fill="#C98B52" {W(2.6)}/>
<rect x="8" y="82" width="84" height="6" rx="2" fill="#C98B52" {W(2.4)}/>
<path d="M16 101 L16 118 M84 101 L84 118" stroke="#3B3355" stroke-width="4"/>
<path d="M22 62 Q22 92 50 92 Q78 92 78 62Z" fill="#2B2B33" {W(3)}/>
<ellipse cx="50" cy="62" rx="28" ry="7" fill="#C98B52" {W(2.4)}/>
<rect x="38" y="56" width="7" height="7" fill="#FFFDF5" {W(1.4)}/><rect x="52" y="58" width="7" height="7" fill="#FFFDF5" {W(1.4)}/>
<path d="M60 56 q4 4 10 2" fill="none" stroke="#3E8A4E" stroke-width="2.6"/>
<path d="M30 74 q4 4 8 0" fill="none" stroke="#D44A5A" stroke-width="2.4" opacity="0"/>
{eye(40, 76, 0.6)}{eye(58, 76, 0.6)}
<path d="M46 82 Q49 84 52 82" fill="none" stroke="#FFFFFF" stroke-width="1.8" stroke-linecap="round"/>
<path d="M30 42 L50 46 L70 42 L70 60 L50 64 L30 60Z" fill="#FFFFFF" {W(2.4)}/>
<path d="M50 46 L50 64" {W(2)}/>
<path d="M36 50 L46 52 M54 52 L64 50" stroke="#C9D6EA" stroke-width="1.8"/>
<path d="M22 68 L30 58 M78 68 L70 58" {W(2.6)}/>
<circle cx="18" cy="20" r="2" fill="#FFFFFF"/><circle cx="40" cy="12" r="1.6" fill="#FFFFFF"/><circle cx="70" cy="22" r="1.8" fill="#FFFFFF"/>
''')

# 18. Алло! Пицца (Литовский б-р): десертная пицца с шоколадом и маршмеллоу съезжает с горки на ледянке
add("cafe-allo-pizza-litovsky-22",
    "круглая десертная пицца с шоколадом и белыми кубиками маршмеллоу",
    "съезжает со снежной горки на красной круглой ледянке, раскинув ручки",
    "zi_snow", f'''
<path d="M0 60 Q40 64 80 96 Q100 110 128 112 L128 130 L0 130Z" fill="#FFFFFF" {W(2.8)}/>
<ellipse cx="62" cy="86" rx="30" ry="9" fill="#E23B2E" {W(2.8)} transform="rotate(28 62 86)"/>
<circle cx="60" cy="68" r="24" fill="#D9A15A" {W(3)}/>
<circle cx="60" cy="68" r="18" fill="#6B3A22"/>
<g fill="#FFFFFF" stroke="{O}" stroke-width="1.6"><rect x="48" y="58" width="6" height="6" rx="1.5"/><rect x="64" y="56" width="6" height="6" rx="1.5"/><rect x="66" y="72" width="6" height="6" rx="1.5"/><rect x="50" y="76" width="6" height="6" rx="1.5"/></g>
{eye(54, 68, 0.6)}{eye(66, 66, 0.6)}
<path d="M38 56 L24 44 M82 58 L96 46" {W(3)}/>
<path d="M14 40 l4 4 M100 40 l4 -4" {W(2.2)}/>
<circle cx="22" cy="20" r="2.6" fill="#FFFFFF"/><circle cx="100" cy="18" r="3" fill="#FFFFFF"/><circle cx="114" cy="54" r="2.4" fill="#FFFFFF"/><circle cx="36" cy="30" r="2" fill="#FFFFFF"/>
<path d="M92 100 q6 -2 10 2 M100 108 q6 -2 10 2" fill="none" stroke="#9DC6E8" stroke-width="2.4" stroke-linecap="round"/>
''')


if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for pid in ids:
        open(os.path.join(OUT, pid + ".svg"), "w").write(ICONS[pid])
    print("svg:", len(ids))
