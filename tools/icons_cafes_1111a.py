"""Иконки робота cafes, 2026-11-11 (02 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая придумана и нарисована отдельно.
Сверено с icons-src/subjects.txt: заняты пицца-подсолнух/рыбак/юла/светофор/фрисби/жвачка, ролл на качелях/батуте/плоту,
хинкали-альпинист, чурчхела, лобио, гондола, дирижёр, канатоходец — не берём. Новые: пицца-садовник с ростком пепперони,
пицца-сёрфер, булочка-птичка в корзинке, хинкали-клоун с шариком-собачкой, пицца-трамвай, селфи пиццы и ролла,
шашлык-турист с рюкзаком, пицца-супергерой над ночным городом, маргарита позирует фотоаппарату, пицца ныряет в листья.
Запуск: python3 tools/icons_cafes_1111a.py [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "k20_mint": ("#EEFCE8", "#8CCB6A"),
    "k20_surf": ("#E3F8FF", "#2F8FD0"),
    "k20_lilac": ("#F6EEFF", "#B49AE8"),
    "k20_circus": ("#FFF6D8", "#F2A93B"),
    "k20_rail": ("#FDEFF0", "#E07C86"),
    "k20_berry": ("#E9FFF7", "#3DB59A"),
    "k20_alp": ("#EAF2FF", "#7E9FD8"),
    "k20_city": ("#B7C0F0", "#3B4596"),
    "k20_studio": ("#FFF4E2", "#D49A55"),
    "k20_autumn": ("#FFFBE6", "#B7B04A"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


def slice_(x0, y0, x1, y1, x2, y2, crust_w=7, fill="#F7C64A", crust="#C9792E"):
    """Кусок пиццы: (x0,y0)-(x1,y1) — корочка, (x2,y2) — острый кончик."""
    return (f'<path d="M{x0} {y0} L{x1} {y1} L{x2} {y2}Z" fill="{fill}" {s()}/>'
            f'<path d="M{x0} {y0} L{x1} {y1}" stroke="{crust}" stroke-width="{crust_w}" stroke-linecap="round"/>'
            f'<path d="M{x0} {y0} L{x1} {y1}" fill="none" {W(2)}/>')


def pep(x, y, r=4.5):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#D9452E" {W(2)}/>'


# 1. Додо (Тимирязевская) — рядом Тимирязевская академия: пицца-садовник сажает «росток пепперони» в горшок
add("cafe-dodo-timiryazevskaya-11",
    "кусок пиццы-садовник в соломенной шляпе",
    "сажает в глиняный горшок кружок пепперони, а из горшка уже проклюнулся росток с пепперони-цветком", "k20_mint", f'''
{slice_(14, 40, 62, 36, 40, 108)}
<path d="M10 40 Q38 22 66 36 Q40 30 10 40Z" fill="#F3D27A" {W(2.4)}/>
<path d="M22 34 Q38 14 54 32" fill="#F3D27A" {W(2.4)}/>
<path d="M24 32 Q38 26 52 31" fill="none" stroke="#E5533D" stroke-width="3"/>
{pep(30, 72, 4)}{pep(48, 60, 4)}
{face(39, 54, d=7, k=0.8)}
<path d="M56 66 Q66 70 74 76" fill="none" {W(3)}/>
<path d="M78 84 L112 84 L106 114 L84 114Z" fill="#D9784A" {s()}/>
<rect x="74" y="78" width="42" height="9" rx="3" fill="#E68A5A" {W(2.6)}/>
<ellipse cx="95" cy="80" rx="17" ry="3" fill="#6B4A36"/>
<path d="M95 79 Q94 62 96 50" fill="none" stroke="#4E9A3A" stroke-width="3.4" stroke-linecap="round"/>
<path d="M95 66 Q84 60 82 52 Q92 52 95 64" fill="#7CCB4E" {W(2.2)}/>
<path d="M96 60 Q108 56 110 48 Q100 46 96 58" fill="#7CCB4E" {W(2.2)}/>
{pep(96, 44, 7)}
<circle cx="93" cy="42" r="1.5" fill="#fff" opacity=".7"/>
''')

# 2. Додо (Головинское ш., у Водного стадиона): кусок пиццы-сёрфер на доске из корочки ловит волну
add("cafe-dodo-golovinskoe-1a",
    "кусок пиццы-сёрфер с раскинутыми ручками",
    "мчится на длинной доске из хлебной корочки по гребню синей волны с белой пеной", "k20_surf", f'''
<path d="M0 88 Q24 56 58 66 Q40 74 46 88 Q60 100 128 86 L128 128 L0 128Z" fill="#1E78C2" {W(2.6)}/>
<path d="M0 88 Q24 56 58 66" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/>
<path d="M50 70 Q44 80 52 88" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
<path d="M18 112 Q26 108 34 112 M74 116 Q82 112 90 116" fill="none" stroke="#9FD6F5" stroke-width="2.6" stroke-linecap="round"/>
<path d="M30 92 Q70 74 112 78 Q118 80 112 84 Q72 92 32 98 Q24 98 30 92Z" fill="#C9792E" {s()}/>
<path d="M40 92 Q72 82 104 82" fill="none" stroke="#E5A867" stroke-width="2.4" stroke-linecap="round"/>
{slice_(54, 26, 96, 34, 72, 84)}
{pep(66, 44)}{pep(84, 46)}{pep(74, 64, 3.6)}
{face(74, 52, d=7, k=0.8)}
<path d="M58 46 L40 36" fill="none" {W(3)}/><path d="M92 50 L110 42" fill="none" {W(3)}/>
<circle cx="39" cy="35" r="3.2" fill="#F7C64A" {W(2)}/><circle cx="111" cy="41" r="3.2" fill="#F7C64A" {W(2)}/>
{sparkle(28, 30, 5)}
''')

# 3. Птица (Отрадное): сдобная булочка-птичка с изюмными глазками высиживает печенье в корзинке
add("cafe-ptitsa-otradnoe",
    "сдобная булочка-птичка с изюминками-глазками и румяным хохолком",
    "уселась в плетёную корзинку и высиживает три круглых печенья, как птенцов", "k20_lilac", f'''
<path d="M16 76 L112 76 L100 114 Q64 122 28 114Z" fill="#C98B4E" {s()}/>
<g stroke="#8E5A2C" stroke-width="2.2" fill="none" stroke-linecap="round">
<path d="M22 88 L106 88"/><path d="M26 100 L102 100"/>
<path d="M36 78 L40 114"/><path d="M56 78 L58 117"/><path d="M76 78 L74 117"/><path d="M94 78 L90 114"/></g>
<circle cx="34" cy="74" r="9" fill="#E9B872" {W(2.4)}/><circle cx="94" cy="74" r="9" fill="#E9B872" {W(2.4)}/>
<circle cx="31" cy="72" r="1.4" fill="#8E5A2C"/><circle cx="37" cy="76" r="1.4" fill="#8E5A2C"/>
<circle cx="91" cy="72" r="1.4" fill="#8E5A2C"/><circle cx="97" cy="76" r="1.4" fill="#8E5A2C"/>
<path d="M34 72 Q40 44 70 42 Q98 42 102 68 Q86 78 64 78 Q44 78 34 72Z" fill="#F2C46E" {s()}/>
<path d="M92 50 Q104 30 116 38 Q106 42 100 54Z" fill="#F2C46E" {s()}/>
<path d="M54 60 Q66 68 80 62" fill="none" stroke="#D9A04E" stroke-width="3" stroke-linecap="round"/>
<path d="M60 52 Q70 48 78 54" fill="none" stroke="#D9A04E" stroke-width="2.4" stroke-linecap="round"/>
<circle cx="40" cy="44" r="16" fill="#F5CC7A" {s()}/>
<path d="M38 28 Q34 18 42 14 Q42 22 46 26" fill="#E3954A" {W(2.4)}/>
<path d="M25 44 L12 48 L25 52Z" fill="#F08A3E" {W(2.4)}/>
<ellipse cx="36" cy="42" rx="3.4" ry="4.2" fill="#3B2333"/><circle cx="35" cy="40.4" r="1.3" fill="#fff"/>
<ellipse cx="44" cy="51" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/>
<path d="M38 54 Q41 56 44 54" fill="none" stroke="#3B2333" stroke-width="1.6" stroke-linecap="round" opacity="0"/>
<circle cx="70" cy="70" r="1.6" fill="#7A4A2E"/><circle cx="86" cy="58" r="1.6" fill="#7A4A2E"/>
''')

# 4. Швили (пр-т Вернадского) — с детьми играют аниматоры: хинкали-клоун скручивает собачку из шарика
add("cafe-shvili-vernadskogo-41",
    "пухлый хинкали-клоун в полосатом колпаке с красным носом-помпоном",
    "скручивает из длинного розового шарика собачку и протягивает её зрителям", "k20_circus", f'''
<path d="M26 104 Q22 68 50 62 L60 62 Q88 66 84 104 Q56 116 26 104Z" fill="#FBF3E2" {s()}/>
<g fill="none" stroke="#D8C9AE" stroke-width="2.4" stroke-linecap="round">
<path d="M34 72 Q44 64 52 58"/><path d="M44 66 Q50 60 54 54"/><path d="M76 72 Q66 64 58 58"/><path d="M66 66 Q60 60 56 54"/></g>
<path d="M48 60 Q55 50 62 60" fill="#FBF3E2" {W(2.6)}/>
<path d="M44 58 L56 22 L68 58Z" fill="#5BB8F0" {s()}/>
<path d="M48 46 L64 46 M51 36 L61 36" stroke="#FFFFFF" stroke-width="4"/>
<path d="M44 58 L56 22 L68 58Z" fill="none" {W(2.6)}/>
<circle cx="56" cy="20" r="5" fill="#FFD13B" {W(2.4)}/>
{face(55, 84, d=9, k=0.85)}
<circle cx="55" cy="90" r="5.5" fill="#E5304A" {W(2.4)}/>
<circle cx="53.5" cy="88.5" r="1.6" fill="#fff" opacity=".8"/>
<path d="M82 88 L92 80" fill="none" {W(3)}/>
<g fill="#FF8FC0" {W(2.4)}>
<ellipse cx="102" cy="58" rx="9" ry="6"/><ellipse cx="96" cy="72" rx="4.5" ry="9"/><ellipse cx="110" cy="72" rx="4.5" ry="9"/>
<ellipse cx="114" cy="48" rx="6" ry="6.5"/><ellipse cx="119" cy="40" rx="3" ry="6"/><ellipse cx="90" cy="54" rx="6" ry="3"/></g>
<circle cx="116" cy="47" r="1.4" fill="{O}"/>
<path d="M98 54 Q102 52 106 55" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
''')

# 5. Додо (Коломна, Советская пл.) — по старой Коломне ходят трамваи: вагончик трамвая из куска пиццы
add("cafe-dodo-kolomna-sovetskaya",
    "трамвайный вагончик из пиццы: томатные бока, сырная крыша, окошки-пепперони",
    "едет по рельсам, токоприёмник-соломинка тянется к проводу, из-под колёс летят искорки", "k20_rail", f'''
<path d="M0 26 L128 18" stroke="{O}" stroke-width="2.4"/>
<path d="M60 52 L74 24 L84 22" fill="none" stroke="#7A6A80" stroke-width="3" stroke-linecap="round"/>
<path d="M20 52 Q20 44 30 44 L100 44 Q110 44 112 54 L114 92 L18 92Z" fill="#E8553E" {s()}/>
<path d="M20 52 Q20 44 30 44 L100 44 Q110 44 112 54" fill="none" stroke="#F7D35A" stroke-width="7" stroke-linecap="round"/>
<path d="M22 50 Q30 58 34 50 Q40 60 46 50 Q54 58 60 50 Q66 60 74 50 Q80 58 86 50 Q92 60 98 50 Q104 58 110 52" fill="#F7D35A" {W(2)}/>
<rect x="16" y="86" width="100" height="8" rx="4" fill="#C9792E" {W(2.6)}/>
<circle cx="34" cy="68" r="8" fill="#B8322A" {W(2.4)}/><circle cx="34" cy="68" r="5" fill="#CDEBFA"/>
<circle cx="56" cy="68" r="8" fill="#B8322A" {W(2.4)}/><circle cx="56" cy="68" r="5" fill="#CDEBFA"/>
{face(92, 68, d=7, k=0.8)}
<circle cx="36" cy="98" r="7" fill="#5B4A63" {W(2.4)}/><circle cx="96" cy="98" r="7" fill="#5B4A63" {W(2.4)}/>
<path d="M0 106 L128 106 M0 112 L128 112" stroke="#8A6E5C" stroke-width="3"/>
<g stroke="#8A6E5C" stroke-width="3"><path d="M14 104 L14 114"/><path d="M48 104 L48 114"/><path d="M82 104 L82 114"/><path d="M116 104 L116 114"/></g>
{sparkle(24, 112, 4, "#FFE36B")}{sparkle(108, 114, 4, "#FFE36B")}
''')

# 6. Мельница (Подольск) — пицца и суши под одной крышей: кусок пиццы и ролл-маки делают селфи
add("cafe-melnitsa-podolsk-sverdlova",
    "кусок пиццы и ролл-маки с лососем — неразлучные друзья",
    "обнялись и делают селфи на телефон на палке, улыбаясь в камеру", "k20_berry", f'''
<path d="M96 44 L114 18" fill="none" stroke="#5B4A63" stroke-width="3.4" stroke-linecap="round"/>
<rect x="104" y="6" width="20" height="30" rx="4" fill="#3B3355" {W(2)} transform="rotate(30 114 21)"/>
<rect x="107" y="10" width="14" height="20" rx="2" fill="#9FE3FF" transform="rotate(30 114 21)"/>
{slice_(10, 44, 56, 40, 34, 110)}
{pep(26, 56)}{pep(44, 54)}{pep(36, 86, 3.8)}
{face(33, 68, d=7, k=0.8)}
<ellipse cx="82" cy="94" rx="24" ry="8" fill="#2E3A2E" {s()}/>
<rect x="58" y="58" width="48" height="36" fill="#2E3A2E"/>
<path d="M58 58 L58 94 M106 58 L106 94" {s()}/>
<ellipse cx="82" cy="58" rx="24" ry="9" fill="#2E3A2E" {s()}/>
<ellipse cx="82" cy="58" rx="19" ry="6.5" fill="#FFFFFF"/>
<ellipse cx="82" cy="58" rx="8" ry="3.2" fill="#FF8A65" {W(1.6)}/>
{face(82, 74, d=8, k=0.8)}
<path d="M54 70 Q60 64 62 70" fill="none" {W(3)}/>
<path d="M100 66 L96 46" fill="none" {W(3)}/>
''')

# 7. Грузинские каникулы (Подольск): шашлык-турист с рюкзаком идёт на каникулы в горы
add("cafe-gruzinskie-kanikuly-podolsk",
    "шампур с тремя румяными кусочками шашлыка в панамке и с зелёным рюкзаком",
    "бодро шагает по горной тропинке к снежным вершинам Кавказа", "k20_alp", f'''
<path d="M0 84 L30 46 L52 70 L80 32 L128 84 L128 128 L0 128Z" fill="#8E9FC8" {W(2.4)}/>
<path d="M22 56 L30 46 L38 56 L32 54 L28 58Z" fill="#fff"/><path d="M70 46 L80 32 L90 46 L84 44 L78 48Z" fill="#fff"/>
<path d="M0 98 Q40 86 128 96 L128 128 L0 128Z" fill="#7CC36A" {W(2.4)}/>
<path d="M22 128 Q52 104 96 98" fill="none" stroke="#E8D3A8" stroke-width="8" stroke-linecap="round"/>
<path d="M64 112 L64 18" stroke="#A7A9B8" stroke-width="3.4" stroke-linecap="round"/>
<circle cx="64" cy="14" r="5" fill="none" stroke="#A7A9B8" stroke-width="3"/>
<rect x="70" y="40" width="18" height="30" rx="6" fill="#4E9A3A" {s()}/>
<path d="M74 48 L84 48" stroke="#2F6B25" stroke-width="2.4"/>
<rect x="48" y="30" width="32" height="20" rx="9" fill="#9A5530" {s()}/>
<rect x="46" y="52" width="36" height="24" rx="10" fill="#8A4A28" {s()}/>
<rect x="48" y="78" width="32" height="20" rx="9" fill="#9A5530" {s()}/>
<path d="M54 36 Q60 34 64 38 M54 84 Q62 82 70 86" fill="none" stroke="#C47A4A" stroke-width="2.4" stroke-linecap="round"/>
{face(62, 62, d=7, k=0.75)}
<path d="M44 30 Q48 18 62 18 Q78 18 82 30Z" fill="#FFE07A" {W(2.4)}/>
<path d="M40 30 L86 30" {W(3)}/>
<path d="M48 98 L42 110 M78 98 L84 110" fill="none" {W(3)}/>
''')

# 8. Додо (Климовск): кусок пиццы-супергерой в маске и плаще-салфетке летит над ночным городом
add("cafe-dodo-klimovsk-zavodskaya",
    "кусок пиццы-супергерой в синей маске и красном плаще-салфетке",
    "летит горизонтально, вытянув кулачок вперёд, над ночными домами с горящими окошками", "k20_city", f'''
<path d="M0 98 L14 98 L14 80 L30 80 L30 92 L44 92 L44 72 L60 72 L60 96 L76 96 L76 84 L92 84 L92 100 L106 100 L106 76 L128 76 L128 128 L0 128Z" fill="#2A2F6B" {W(2.2)}/>
<g fill="#FFE36B"><rect x="18" y="86" width="4" height="5"/><rect x="48" y="78" width="4" height="5"/><rect x="52" y="86" width="4" height="5"/><rect x="80" y="90" width="4" height="5"/><rect x="110" y="82" width="4" height="5"/><rect x="118" y="90" width="4" height="5"/></g>
<path d="M30 40 Q14 30 4 44 Q14 46 10 58 Q22 52 30 62Z" fill="#E5304A" {s()}/>
{slice_(30, 36, 30, 72, 100, 52)}
{pep(46, 46)}{pep(48, 62)}{pep(70, 54, 3.8)}
<path d="M38 46 Q52 40 66 46 L64 54 Q52 50 40 54Z" fill="#2E5BD8" {W(2)}/>
<circle cx="47" cy="49" r="2.6" fill="#fff"/><circle cx="59" cy="49" r="2.6" fill="#fff"/>
<circle cx="47.5" cy="49.5" r="1.3" fill="{O}"/><circle cx="59.5" cy="49.5" r="1.3" fill="{O}"/>
<path d="M48 60 Q53 64 58 60" fill="none" {W(2.4)}/>
<path d="M90 50 L108 44" fill="none" {W(3)}/><circle cx="110" cy="43" r="4" fill="#F7C64A" {W(2)}/>
{sparkle(100, 20, 5, "#FFF6B0")}{sparkle(22, 18, 3.5, "#FFF6B0")}{sparkle(70, 26, 3, "#FFF6B0")}
''')

# 9. Il Патио (Серпухов) — итальянская пицца из печи: маргарита позирует перед фотоаппаратом на треноге
add("cafe-ilpatio-serpukhov",
    "целая круглая пицца маргарита с кружками моцареллы и листиками базилика",
    "позирует, улыбаясь, перед старинным фотоаппаратом на треноге, а вспышка сверкает звёздочкой", "k20_studio", f'''
<circle cx="46" cy="70" r="34" fill="#E9A54E" {s()}/>
<circle cx="46" cy="70" r="27" fill="#E4472F" {W(2.4)}/>
<g fill="#FFF8EC" {W(2)}><circle cx="34" cy="58" r="6"/><circle cx="60" cy="60" r="5.5"/><circle cx="56" cy="84" r="6"/><circle cx="32" cy="82" r="5"/></g>
<path d="M44 48 Q50 44 52 50 Q46 54 44 48Z" fill="#4E9A3A" {W(1.8)}/>
<path d="M66 74 Q72 72 72 78 Q66 80 66 74Z" fill="#4E9A3A" {W(1.8)}/>
{face(46, 68, d=8, k=0.85)}
<g stroke="#6B4A36" stroke-width="3.4" stroke-linecap="round"><path d="M100 76 L88 114"/><path d="M100 76 L112 114"/><path d="M100 76 L100 116"/></g>
<rect x="86" y="52" width="30" height="24" rx="4" fill="#4A4060" {s()}/>
<rect x="92" y="46" width="12" height="7" rx="2" fill="#4A4060" {W(2.4)}/>
<circle cx="96" cy="64" r="8" fill="#A9D8F5" {W(2.6)}/><circle cx="94" cy="62" r="2.4" fill="#fff"/>
<rect x="108" y="42" width="9" height="6" rx="1.5" fill="#E8E8F0" {W(2)}/>
{sparkle(114, 30, 8, "#FFFFFF")}
''')

# 10. Додо (Серпухов, ул. Ворошилова): кусок пиццы с разбегу ныряет в кучу осенних листьев
add("cafe-dodo-serpukhov-voroshilova",
    "кусок пиццы-озорник с поднятыми ручками",
    "в прыжке ныряет кончиком вниз в пушистую кучу оранжевых, красных и жёлтых осенних листьев", "k20_autumn", f'''
<path d="M10 116 Q20 84 44 86 Q58 72 78 82 Q100 76 116 104 L118 128 L8 128Z" fill="#E98A2E" {W(2.6)}/>
<g {W(2)}>
<path d="M22 100 Q30 92 38 100 Q30 108 22 100Z" fill="#F7C23C"/>
<path d="M88 96 Q98 88 106 98 Q96 104 88 96Z" fill="#D9452E"/>
<path d="M56 106 Q64 98 72 106 Q64 114 56 106Z" fill="#B85A24"/>
<path d="M38 116 Q46 108 54 116 Q46 122 38 116Z" fill="#D9452E"/>
<path d="M80 114 Q88 106 96 114 Q88 120 80 114Z" fill="#F7C23C"/></g>
{slice_(40, 22, 84, 30, 60, 84)}
{pep(52, 38)}{pep(72, 40)}{pep(62, 58, 3.8)}
{face(61, 48, d=7, k=0.8)}
<path d="M44 30 L32 14" fill="none" {W(3)}/><path d="M80 36 L94 20" fill="none" {W(3)}/>
<circle cx="31" cy="12" r="3.2" fill="#F7C64A" {W(2)}/><circle cx="95" cy="18" r="3.2" fill="#F7C64A" {W(2)}/>
<g {W(1.8)}><path d="M16 60 Q22 52 28 60 Q22 66 16 60Z" fill="#F7C23C"/>
<path d="M100 54 Q106 46 112 54 Q106 60 100 54Z" fill="#D9452E"/>
<path d="M22 36 Q28 30 32 38 Q26 42 22 36Z" fill="#E98A2E"/></g>
''')


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
