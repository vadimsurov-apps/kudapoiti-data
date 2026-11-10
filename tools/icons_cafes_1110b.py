"""Иконки робота cafes, 2026-11-10 (01:30 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая придумана и нарисована
отдельно (свой герой по кухне/названию, своя сцена, компоновка и палитра). Сверено с icons-src/subjects.txt и листами
icons-catalog (сфольятелла, кустик базилика в горшке, чакапули с тархуном, перемяч, малина-саксофонист, сырная
пирамида-акробат — свободны).
Запуск: python3 tools/icons_cafes_1110b.py [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "k14_sky": ("#EAF6FF", "#6FA8E0"),
    "k14_terra": ("#FFF4E8", "#E08A5A"),
    "k14_city": ("#E9F0FF", "#5A6FB8"),
    "k14_mint": ("#F2FFF4", "#5FBF84"),
    "k14_jazz": ("#3A2E5C", "#1A1433"),
    "k14_sun": ("#FFFBE0", "#F5B83D"),
    "k14_dusk": ("#FFEFE0", "#F07E6A"),
    "k14_lamp": ("#4A3A2E", "#22180F"),
    "k14_disco": ("#FFE9F6", "#D96BB5"),
    "k14_book": ("#FFF8EC", "#B6D98A"),
    "k14_pond": ("#E6FAFF", "#59B7C9"),
    "k14_wave": ("#E3F1FF", "#2F6FBF"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Остерия Марио (Внуково) — сфольятелла летит у иллюминатора самолёта (рядом аэропорт Внуково)
add("cafe-osteria-vnukovo-chukovskogo",
    "неаполитанская слоёная сфольятелла — ракушка из тонких золотистых слоёв, присыпанная сахарной пудрой",
    "сидит в иллюминаторе самолёта и с восторгом смотрит на пушистые облака внизу", "k14_sky", f'''
<rect x="14" y="10" width="100" height="108" rx="46" fill="#F4F6FA" {s()}/>
<rect x="24" y="22" width="80" height="84" rx="38" fill="#BFE3FF" {W(3)}/>
<path d="M24 82 Q34 70 46 78 Q54 66 68 74 Q80 64 92 76 Q100 72 104 78 L104 90 Q64 112 24 90Z" fill="#FFFFFF" {W(2.4)}/>
<path d="M36 94 Q38 54 66 46 Q94 54 94 94 Q64 104 36 94Z" fill="#F2B45A" {s()}/>
<path d="M44 92 Q46 62 66 54" fill="none" stroke="#C9792B" stroke-width="2.4"/>
<path d="M54 95 Q56 68 70 58" fill="none" stroke="#C9792B" stroke-width="2.4"/>
<path d="M66 96 Q70 72 80 62" fill="none" stroke="#C9792B" stroke-width="2.4"/>
<path d="M78 95 Q84 78 88 70" fill="none" stroke="#C9792B" stroke-width="2.4"/>
<circle cx="58" cy="50" r="1.6" fill="#fff"/><circle cx="72" cy="48" r="1.6" fill="#fff"/><circle cx="64" cy="44" r="1.4" fill="#fff"/><circle cx="82" cy="54" r="1.4" fill="#fff"/>
{face(64, 76, d=10, k=0.95, mouth=False)}
<ellipse cx="64" cy="86" rx="4" ry="4.6" fill="#7A2E3A" {W(2)}/>
''' + sparkle(98, 30, 4) + sparkle(30, 36, 3))

# 2. La Basilico (Внуково) — кустик базилика в горшке сам себя поливает
add("cafe-labasilico-vnukovo",
    "кустик свежего базилика из пяти крупных листьев в терракотовом горшочке",
    "поливает себя из крошечной лейки-листика, и на нём сверкают капли", "k14_terra", f'''
<path d="M38 84 L44 120 H84 L90 84Z" fill="#D9744A" {s()}/>
<rect x="34" y="78" width="60" height="12" rx="4" fill="#E88A5E" {s()}/>
<path d="M64 80 L64 46" stroke="#3E8E41" stroke-width="5" stroke-linecap="round"/>
<path d="M64 60 Q40 62 30 44 Q50 34 64 60Z" fill="#58B65B" {s()}/>
<path d="M64 60 Q88 62 98 44 Q78 34 64 60Z" fill="#58B65B" {s()}/>
<path d="M64 48 Q44 40 46 18 Q66 22 64 48Z" fill="#6ACB6A" {s()}/>
<path d="M64 48 Q84 40 82 18 Q62 22 64 48Z" fill="#6ACB6A" {s()}/>
<path d="M64 78 Q50 74 48 66 Q60 64 64 78Z" fill="#4FA853" {W(2.4)}/>
<path d="M36 44 Q48 46 60 58 M92 44 Q80 46 68 58 M50 22 Q56 32 62 46 M78 22 Q72 32 66 46" fill="none" stroke="#2F7A33" stroke-width="1.8"/>
{face(64, 98, d=11, k=1.0)}
<path d="M98 40 L112 30 L116 38 L102 46Z" fill="#7BD3E8" {W(2.4)}/>
<path d="M112 30 Q118 24 122 28" fill="none" {W(2.2)}/>
<path d="M100 48 l-3 6 M95 50 l-4 5 M104 52 l-2 6" stroke="#4AB3E0" stroke-width="2.4" stroke-linecap="round"/>
<circle cx="40" cy="38" r="2.2" fill="#BFF0FF" {W(1.4)}/><circle cx="88" cy="26" r="2.2" fill="#BFF0FF" {W(1.4)}/>
''' + sparkle(20, 76, 3))

# 3. Чакапули (ТЦ «Океания», 4 этаж с панорамой) — рагу чакапули смотрит на Сити
add("cafe-chakapuli-okeania",
    "глиняная мисочка грузинского рагу чакапули, из которой торчат веточки тархуна",
    "сидит у панорамного окна и разглядывает в бинокль высотки Москва-Сити вдали", "k14_city", f'''
<rect x="70" y="30" width="12" height="56" fill="#9FB4E8" {W(2.4)}/>
<path d="M86 86 V20 L94 12 L100 20 V86Z" fill="#B9C9F2" {W(2.4)}/>
<rect x="104" y="40" width="12" height="46" fill="#8AA2E0" {W(2.4)}/>
<path d="M60 86 H124" stroke="{O}" stroke-width="3"/>
<path d="M14 82 Q14 118 50 118 Q86 118 86 82Z" fill="#B5623B" {s()}/>
<ellipse cx="50" cy="82" rx="36" ry="9" fill="#9BBF5A" {s()}/>
<path d="M30 80 Q24 56 34 44 M42 78 Q40 58 48 50 M62 78 Q66 60 58 46" fill="none" stroke="#2F7A33" stroke-width="3.2" stroke-linecap="round"/>
<path d="M34 44 q-6 -2 -8 4 q6 2 8 -4Z M34 52 q6 -4 10 0 q-6 4 -10 0Z M48 50 q4 -6 10 -4 q-4 6 -10 4Z M58 46 q-6 -4 -10 0 q6 4 10 0Z M44 62 q-6 0 -8 5 q6 1 8 -5Z" fill="#5FB45F" {W(1.6)}/>
<circle cx="38" cy="82" r="3" fill="#E8EFD0" {W(1.4)}/><circle cx="58" cy="84" r="3" fill="#E8EFD0" {W(1.4)}/>
{face(50, 100, d=11, k=0.95)}
<rect x="54" y="62" width="12" height="16" rx="5" fill="#4B4B6A" {W(2.4)}/>
<rect x="68" y="62" width="12" height="16" rx="5" fill="#4B4B6A" {W(2.4)}/>
<rect x="64" y="66" width="6" height="6" fill="#4B4B6A" {W(2)}/>
<circle cx="60" cy="64" r="3.4" fill="#BFE3FF" {W(1.6)}/><circle cx="74" cy="64" r="3.4" fill="#BFE3FF" {W(1.6)}/>
''' + sparkle(112, 24, 4))

# 4. Мирадж (татарская кухня) — перемяч пускает из дырочки мыльные пузыри
add("cafe-miradj-budennogo",
    "круглый татарский пирожок перемяч с открытой дырочкой-окошком на макушке",
    "пускает из своей дырочки радужные мыльные пузыри, как из трубочки, и радуется", "k14_mint", f'''
<ellipse cx="62" cy="112" rx="40" ry="7" fill="#3E9A62" opacity=".35"/>
<ellipse cx="62" cy="84" rx="44" ry="30" fill="#E8A350" {s()}/>
<ellipse cx="62" cy="76" rx="38" ry="20" fill="#F2BD6A" stroke="none"/>
<path d="M30 70 q4 -6 8 0 q4 -6 8 0 q4 -6 8 0 q4 -6 8 0 q4 -6 8 0 q4 -6 8 0 q4 -6 8 0" fill="none" stroke="#C9792B" stroke-width="2.4"/>
<ellipse cx="62" cy="64" rx="12" ry="6" fill="#8A4A1E" {W(2.6)}/>
<ellipse cx="62" cy="63" rx="7" ry="3" fill="#C46A2A"/>
{face(62, 88, d=13, k=1.0)}
<circle cx="70" cy="40" r="9" fill="#E9F8FF" opacity=".85" {W(2.2)}/>
<circle cx="88" cy="22" r="12" fill="#F3E9FF" opacity=".85" {W(2.2)}/>
<circle cx="48" cy="28" r="6" fill="#FFF3D6" opacity=".85" {W(2)}/>
<path d="M66 36 q3 -2 5 0 M83 17 q4 -3 8 0 M46 25 q2 -2 4 0" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
<path d="M82 28 q4 2 6 -2" fill="none" stroke="#FF8AC0" stroke-width="2"/>
''' + sparkle(108, 46, 4) + sparkle(24, 46, 3))

# 5. Малиновка (парк «Сокольники», джаз) — малина играет на саксофоне
add("cafe-malinovka-sokolniki",
    "крупная ягода малины из пупырышек с зелёной шапочкой-чашелистиком",
    "играет джаз на золотом саксофоне под лучом прожектора, вокруг летят ноты", "k14_jazz", f'''
<path d="M40 0 L88 0 L118 128 L10 128Z" fill="#FFF6C8" opacity=".18"/>
<ellipse cx="62" cy="118" rx="38" ry="6" fill="#000" opacity=".25"/>
<g fill="#E8325A" {W(2.2)}>
<circle cx="50" cy="56" r="10"/><circle cx="68" cy="54" r="10"/><circle cx="40" cy="72" r="10"/><circle cx="58" cy="72" r="10"/>
<circle cx="76" cy="70" r="10"/><circle cx="46" cy="90" r="10"/><circle cx="64" cy="90" r="10"/><circle cx="56" cy="106" r="10"/><circle cx="74" cy="104" r="9"/>
</g>
<g fill="#FF8FA8" opacity=".9"><circle cx="47" cy="53" r="2.4"/><circle cx="65" cy="51" r="2.4"/><circle cx="55" cy="69" r="2.4"/><circle cx="43" cy="87" r="2.4"/></g>
<path d="M44 46 L36 36 L52 42 L58 30 L64 42 L80 36 L72 48Z" fill="#4FB357" {W(2.4)}/>
{face(56, 76, d=9, k=0.9, mouth=False)}
<path d="M66 82 L84 70" stroke="{O}" stroke-width="3"/>
<path d="M84 70 Q92 66 94 76 L98 100 Q100 112 90 112 Q80 112 84 102 L88 96" fill="#F5C443" {W(2.6)}/>
<path d="M84 102 Q76 110 74 116 Q90 120 96 108" fill="#F5C443" {W(2.6)}/>
<circle cx="92" cy="84" r="1.8" fill="{O}"/><circle cx="94" cy="92" r="1.8" fill="{O}"/>
<path d="M100 42 v-12 l8 -2 v12" fill="none" stroke="#FFE27A" stroke-width="2.4" stroke-linecap="round"/>
<ellipse cx="98" cy="42" rx="3.4" ry="2.6" fill="#FFE27A"/><ellipse cx="106" cy="40" rx="3.4" ry="2.6" fill="#FFE27A"/>
<path d="M22 50 v-10" stroke="#FFE27A" stroke-width="2.4"/><ellipse cx="20" cy="50" rx="3.2" ry="2.4" fill="#FFE27A"/>
''' + sparkle(112, 70, 3, "#FFE27A"))

# 6. Четыре сыра (Чертаново, игротека) — пирамида из четырёх сыров держит равновесие на мяче
add("cafe-chetyre-syra-dnepropetrovskaya",
    "пирамида-акробат из четырёх разных сыров: белый кубик моцареллы, жёлтый треугольник, голубой ломтик с прожилками и оранжевый брусок",
    "держит равновесие на красно-синем прыгающем мяче, как в цирке, и все четыре сыра улыбаются", "k14_sun", f'''
<circle cx="64" cy="104" r="18" fill="#E8424E" {s()}/>
<path d="M46 104 Q64 92 82 104 Q64 116 46 104Z" fill="#3E7BE0" {W(2.4)}/>
<rect x="36" y="70" width="56" height="16" rx="4" fill="#F59A3C" {s()}/>
{face(64, 77, d=9, k=0.6)}
<path d="M42 52 L86 52 L86 70 L42 70Z" fill="#CFE4F2" {s()}/>
<path d="M48 56 q8 6 4 12 M66 54 q-4 8 6 14 M80 56 q-6 4 -2 10" fill="none" stroke="#5B86B8" stroke-width="2"/>
{face(64, 59, d=8, k=0.55)}
<path d="M50 52 L64 28 L78 52Z" fill="#FFD84A" {s()}/>
<circle cx="58" cy="46" r="2.6" fill="#E9B42A"/><circle cx="70" cy="44" r="2" fill="#E9B42A"/>
{face(64, 42, d=6, k=0.5, mouth=False)}
<rect x="54" y="8" width="20" height="20" rx="4" fill="#FFFFFF" {s()}/>
{face(64, 16, d=5, k=0.45)}
<path d="M30 70 l-10 -6 M98 70 l10 -6" {W(2.4)}/>
''' + sparkle(20, 30, 4) + sparkle(108, 34, 3))

# 7. Тюрки Diner (узбекская и турецкая кухня, летняя веранда) — гёзлеме запускает самолётик
add("cafe-turki-diner-nebesny",
    "турецкая лепёшка гёзлеме, сложенная пополам, с зеленью и сыром, выглядывающими из шва",
    "запускает с перил летней веранды бумажный самолётик, сложенный из салфетки", "k14_dusk", f'''
<circle cx="100" cy="30" r="12" fill="#FFD36A" opacity=".8"/>
<path d="M0 104 H128 V128 H0Z" fill="#B97A4C" {s()}/>
<path d="M0 92 H128" stroke="{O}" stroke-width="3"/><path d="M12 92 V104 M36 92 V104 M92 92 V104 M116 92 V104" {W(3)}/>
<path d="M18 92 Q20 48 62 44 Q100 48 98 92Z" fill="#F0C27A" {s()}/>
<path d="M22 90 Q40 80 60 86 Q80 80 96 90" fill="none" stroke="#3E9A47" stroke-width="4" stroke-linecap="round"/>
<path d="M30 86 q4 -4 8 0 M66 84 q4 -4 8 0" fill="none" stroke="#FFF7DA" stroke-width="3" stroke-linecap="round"/>
<circle cx="42" cy="58" r="2.4" fill="#C98A3B"/><circle cx="76" cy="56" r="2.4" fill="#C98A3B"/><circle cx="58" cy="52" r="2" fill="#C98A3B"/><circle cx="86" cy="70" r="2" fill="#C98A3B"/>
{face(58, 68, d=11, k=0.95)}
<path d="M90 64 L102 54" {W(3)}/>
<path d="M100 54 L124 40 L108 60 Z" fill="#FFFFFF" {W(2.4)}/>
<path d="M100 54 L112 52 L108 60" fill="#E6EEF7" {W(2)}/>
<path d="M84 36 q6 -6 12 -2 M76 44 q4 -4 8 -2" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-dasharray="3 4"/>
''' + sparkle(24, 30, 3))

# 8. Торшер — десерт «Павлова» читает книжку под торшером
add("cafe-torsher-vasiltsovsky",
    "воздушный десерт «Павлова»: круглое гнездо из безе со сливками, клубникой и голубикой",
    "уютно читает толстую книжку при свете старинного торшера с жёлтым абажуром и бахромой", "k14_lamp", f'''
<path d="M96 14 L120 14 L126 42 L90 42Z" fill="#FFD66B" {W(2.6)}/>
<path d="M90 42 l2 6 M96 42 l1 6 M102 42 l0 6 M108 42 l0 6 M114 42 l-1 6 M120 42 l-1 6 M126 42 l-2 6" {W(2)}/>
<path d="M108 48 V118 M98 120 H118" {W(3.2)}/>
<path d="M88 42 L30 120 L128 120 L128 42Z" fill="#FFE9A0" opacity=".16"/>
<ellipse cx="54" cy="110" rx="40" ry="6" fill="#000" opacity=".25"/>
<path d="M14 88 Q14 104 54 106 Q94 104 94 88 Q90 76 54 74 Q18 76 14 88Z" fill="#FFF6EA" {s()}/>
<path d="M20 80 q6 -10 12 -2 q6 -12 14 -2 q6 -12 14 -2 q6 -12 14 0 q6 -8 12 4" fill="#FFFFFF" {W(2.6)}/>
<circle cx="34" cy="70" r="6" fill="#E8344E" {W(2.2)}/><circle cx="52" cy="66" r="6.5" fill="#E8344E" {W(2.2)}/><circle cx="70" cy="70" r="6" fill="#E8344E" {W(2.2)}/>
<circle cx="44" cy="74" r="3.6" fill="#4C6FD8" {W(1.8)}/><circle cx="62" cy="75" r="3.6" fill="#4C6FD8" {W(1.8)}/><circle cx="80" cy="76" r="3.4" fill="#4C6FD8" {W(1.8)}/>
<path d="M50 60 q3 -4 6 -1" fill="none" stroke="#3E9A47" stroke-width="2.4"/>
{face(54, 92, d=10, k=0.85, mouth=False)}
<path d="M30 104 L54 98 L78 104 L78 118 L54 112 L30 118Z" fill="#4E8BD6" {W(2.4)}/>
<path d="M54 98 V112" {W(2)}/><path d="M36 106 L50 103 M58 103 L72 106" stroke="#fff" stroke-width="1.6"/>
''')

# 9. Кусочки (тематическое кафе, праздники) — пирожное «Буше» катается на пластинке
add("cafe-kusochki-shabolovka",
    "советское пирожное «Буше» — два круглых бисквита с кремом, облитые шоколадом, с вишенкой",
    "катается, как на карусели, на крутящейся виниловой пластинке, а вокруг разлетается конфетти", "k14_disco", f'''
<ellipse cx="64" cy="100" rx="56" ry="18" fill="#2B2340" {s()}/>
<ellipse cx="64" cy="100" rx="42" ry="13" fill="none" stroke="#5B4C7E" stroke-width="1.6"/>
<ellipse cx="64" cy="100" rx="30" ry="9" fill="none" stroke="#5B4C7E" stroke-width="1.6"/>
<ellipse cx="64" cy="100" rx="13" ry="4.5" fill="#FF6FA5" {W(2)}/>
<path d="M16 92 q-6 -4 -2 -10 M112 92 q6 -4 2 -10" fill="none" {W(2.4)}/>
<ellipse cx="64" cy="88" rx="30" ry="9" fill="#5A3420" {s()}/>
<path d="M34 72 V88 Q64 98 94 88 V72Z" fill="#5A3420" {s()}/>
<path d="M36 74 Q64 82 92 74" fill="none" stroke="#FFF2DA" stroke-width="5"/>
<ellipse cx="64" cy="58" rx="30" ry="14" fill="#6B3E24" {s()}/>
<path d="M34 58 V72 Q64 82 94 72 V58" fill="#6B3E24" {s()}/>
<path d="M44 52 q10 -6 20 -2" fill="none" stroke="#8A5534" stroke-width="2.4"/>
<circle cx="64" cy="40" r="7" fill="#D81F3C" {W(2.4)}/><path d="M64 33 Q68 24 76 22" fill="none" {W(2.2)}/>
{face(64, 64, d=11, k=0.85)}
<rect x="18" y="26" width="6" height="6" fill="#FFD84A" transform="rotate(20 21 29)"/>
<rect x="100" y="20" width="6" height="6" fill="#5FD0E8" transform="rotate(-25 103 23)"/>
<rect x="30" y="12" width="5" height="5" fill="#7FE07A" transform="rotate(40 32 14)"/>
<rect x="88" y="44" width="5" height="5" fill="#FF8A3C" transform="rotate(15 90 46)"/>
<circle cx="106" cy="56" r="3" fill="#FFF"/><circle cx="16" cy="54" r="3" fill="#FFD84A"/>
''')

# 10. Хинкали-Gали! (Тушино, детский уголок с книжками) — мацони читает книжку на пуфе
add("cafe-hinkali-gali-vishnevaya",
    "грузинский йогурт мацони в глиняной чашечке с золотой капелькой мёда на макушке",
    "сидит на мягком розовом пуфе в детском уголке и читает раскрытую книжку с картинками", "k14_book", f'''
<ellipse cx="64" cy="108" rx="44" ry="14" fill="#FF9EC2" {s()}/>
<path d="M20 108 Q20 96 64 94 Q108 96 108 108" fill="#FFB8D2" {W(2.6)}/>
<path d="M36 58 Q36 96 64 96 Q92 96 92 58Z" fill="#C9763E" {s()}/>
<ellipse cx="64" cy="58" rx="28" ry="8" fill="#FFFDF5" {s()}/>
<path d="M60 56 q4 -12 8 0" fill="#F2B530" {W(2)}/>
<path d="M40 66 Q64 74 88 66" fill="none" stroke="#A85D2C" stroke-width="2.4"/>
{face(64, 72, d=10, k=0.9)}
<path d="M28 94 L52 88 L52 106 L28 112Z" fill="#FFFFFF" {W(2.4)}/>
<path d="M100 94 L76 88 L76 106 L100 112Z" fill="#FFFFFF" {W(2.4)}/>
<path d="M52 88 Q64 84 76 88 L76 106 Q64 102 52 106Z" fill="#FFE27A" {W(2.4)}/>
<circle cx="40" cy="100" r="4.5" fill="#FFB547"/><path d="M84 104 l6 -8 l6 8Z" fill="#6AC07A"/>

''' + sparkle(108, 30, 4) + sparkle(22, 40, 3))

# 11. Pizzamento (у парка «Царицыно») — ломтик пиццы плывёт на лодке перед дворцом
add("cafe-pizzamento-tsaritsyno",
    "треугольный ломтик пиццы с чёрными оливками и тянущимся сыром",
    "плывёт на деревянной лодочке с вёслами по пруду перед красным дворцом с белыми башенками", "k14_pond", f'''
<path d="M10 64 V40 L18 30 L26 40 V64Z M102 64 V40 L110 30 L118 40 V64Z" fill="#C8443A" {W(2.4)}/>
<path d="M26 64 V46 H102 V64Z" fill="#D9564A" {W(2.4)}/>
<path d="M18 30 V24 M110 30 V24" {W(2.4)}/>
<path d="M36 52 v6 M50 52 v6 M64 52 v6 M78 52 v6 M92 52 v6" stroke="#fff" stroke-width="3"/>
<path d="M14 44 h8 M106 44 h8" stroke="#fff" stroke-width="2.4"/>
<path d="M0 66 H128 V128 H0Z" fill="#7CCFE0" {s()}/>
<path d="M8 78 q8 -4 16 0 M100 76 q8 -4 16 0" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M22 98 Q64 124 106 98 L98 112 Q64 126 30 112Z" fill="#B5733F" {s()}/>
<path d="M26 102 Q64 120 102 102" fill="none" stroke="#8A5228" stroke-width="2"/>
<path d="M14 108 L36 96 M114 108 L92 96" stroke="{O}" stroke-width="4" stroke-linecap="round"/>
<path d="M44 102 L64 50 L84 102Z" fill="#FFD25A" {s()}/>
<path d="M44 102 Q64 108 84 102 L86 96 Q64 102 42 96Z" fill="#E59A3C" {W(2.4)}/>
<ellipse cx="62" cy="68" rx="3.4" ry="2.6" fill="#2E2A3A"/><ellipse cx="72" cy="88" rx="3.4" ry="2.6" fill="#2E2A3A"/><ellipse cx="54" cy="90" rx="3.4" ry="2.6" fill="#2E2A3A"/>
<path d="M58 58 Q56 64 60 66" fill="none" stroke="#FFF2B0" stroke-width="2.4"/>
{face(64, 80, d=7, k=0.75)}
''')

# 12. Строгинская гавань — шашлычок из сёмги у штурвала катера
add("cafe-strogino-gavan",
    "шашлычок из розовой сёмги на деревянной шпажке с дольками лимона между кусочками",
    "стоит у штурвала маленького белого катера и ведёт его по заливу, за кормой пенится след", "k14_wave", f'''
<path d="M0 92 Q16 86 32 92 T64 92 T96 92 T128 92 V128 H0Z" fill="#3E86D6" {s()}/>
<path d="M4 108 q10 -4 20 0 M88 112 q10 -4 20 0" fill="none" stroke="#BFE3FF" stroke-width="2.4" stroke-linecap="round"/>
<path d="M14 84 L110 84 L100 100 L24 100Z" fill="#FFFFFF" {s()}/>
<path d="M24 92 H102" stroke="#E8344E" stroke-width="3"/>
<path d="M110 90 q8 0 14 6 M106 98 q8 2 14 8" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>
<path d="M60 84 V20" stroke="#B5733F" stroke-width="4" stroke-linecap="round"/>
<rect x="46" y="26" width="28" height="14" rx="5" fill="#FF8E7A" {W(2.4)}/>
<path d="M52 28 v10 M60 28 v10 M68 28 v10" stroke="#FFC2B6" stroke-width="2"/>
<path d="M48 44 Q60 38 72 44 Q60 50 48 44Z" fill="#FFE45A" {W(2.2)}/>
<rect x="44" y="50" width="32" height="18" rx="6" fill="#FF8E7A" {W(2.4)}/>
<path d="M50 52 v14 M70 52 v14" stroke="#FFC2B6" stroke-width="2"/>
{face(60, 58, d=7, k=0.7)}
<path d="M48 72 Q60 66 72 72 Q60 78 48 72Z" fill="#FFE45A" {W(2.2)}/>
<circle cx="94" cy="68" r="10" fill="none" {W(3)}/>
<path d="M94 56 V80 M82 68 H106 M86 60 L102 76 M102 60 L86 76" {W(2)}/>
<path d="M76 62 L86 66" {W(3)}/>
''' + sparkle(20, 30, 4) + sparkle(104, 26, 3))


def main(ids):
    ids = ids or list(ICONS)
    for pid in ids:
        open(os.path.join(OUT, pid + ".svg"), "w").write(ICONS[pid])
    reg = os.path.join(OUT, "subjects.txt")
    lines = open(reg, encoding="utf-8").read().splitlines()
    have = {l.split(" — ", 1)[0] for l in lines if " — " in l}
    with open(reg, "a", encoding="utf-8") as f:
        for pid in ids:
            if pid not in have:
                h, sc = SUBJ[pid]
                f.write(f"{pid} — герой: {h} | сцена: {sc}\n")
    print("svg", len(ids))


if __name__ == "__main__":
    main(sys.argv[1:])
