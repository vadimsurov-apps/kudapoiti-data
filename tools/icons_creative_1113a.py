"""Иконки робота creative, 13.11 (запуск 1113a). Каждая придумана и нарисована отдельно: свой герой, своя сцена,
своя компоновка и свой фон (правило абсолютной уникальности). python3 tools/icons_creative_1113a.py [--subjects]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_creative_1112k import bg, ln, limb, note, head, SKIN

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
I = {}

# 1 Лаборатория Веты Гулливер (вокал с 3,5 лет, инструменты): крошечная певица на клавише рояля-великана
I["veta-gulliver-odintsovo"] = ("крошечная девочка-лилипут в жёлтом платьице с двумя хвостиками",
    "поёт, раскинув руки, стоя на огромных клавишах рояля-великана, которые уходят за край картинки", bg("#E6F7EE", "#2E8C6A", f'''
<path d="M-4 76 H132 V128 H-4Z" fill="#fff" {s()}/>
<path d="M14 76 V128 M42 76 V128 M70 76 V128 M98 76 V128 M126 76 V128" stroke="{O}" stroke-width="2.6"/>
<rect x="6" y="76" width="16" height="30" rx="2" fill="#2B2440"/><rect x="34" y="76" width="16" height="30" rx="2" fill="#2B2440"/>
<rect x="90" y="76" width="16" height="30" rx="2" fill="#2B2440"/><rect x="118" y="76" width="16" height="30" rx="2" fill="#2B2440"/>
{limb(52, 66, 50, 78, SKIN, 4)}{limb(60, 66, 62, 78, SKIN, 4)}
<path d="M44 66 L50 42 H62 L68 66Z" fill="#FFD43B" {s()}/>
{limb(51, 46, 36, 34, SKIN, 3.5)}{limb(61, 46, 76, 34, SKIN, 3.5)}
<circle cx="56" cy="30" r="11" fill="{SKIN}" {s()}/>
<path d="M45 28 Q47 17 56 18 Q65 17 67 28 Q60 22 56 23 Q52 22 45 28Z" fill="#B5652E" {s('stroke-width="2.2"')}/>
<path d="M45 24 L36 18 L40 28Z M67 24 L76 18 L72 28Z" fill="#B5652E" {s('stroke-width="2"')}/>
{eye(52, 30, 0.45)}{eye(60, 30, 0.45)}<ellipse cx="56" cy="36.5" rx="3" ry="3.2" fill="#C2365A" {s('stroke-width="1.6"')}/>
{note(88, 30, 0.9, "#fff")}{note(102, 50, 0.7, "#FFD43B")}{note(20, 48, 0.6, "#fff")}
{sparkle(108, 20, 4)}
'''))

# 2 Первая детская школа телевидения и эстрады (Одинцово): табличка «В ЭФИРЕ» загорелась
I["tv-estrada-school-odintsovo"] = ("красная светящаяся табличка «В ЭФИРЕ» с мордашкой",
    "загорается над студией и подмигивает, от неё во все стороны расходятся жёлтые лучи-вспышки", bg("#3A3F6E", "#14162E", f'''
<path d="M64 40 L64 16 M48 42 L40 20 M80 42 L88 20" {ln("#FFE27A", 4)} opacity=".8"/>
<path d="M22 64 L6 60 M106 64 L122 60 M26 86 L10 94 M102 86 L118 94" {ln("#FFE27A", 4)} opacity=".8"/>
<path d="M46 40 L46 30 M82 40 L82 30" {ln("#9AA0B8", 4)}/>
<rect x="22" y="40" width="84" height="52" rx="12" fill="#E8344E" {s()}/>
<rect x="28" y="46" width="72" height="40" rx="8" fill="#FF5A6E"/>
<text x="64" y="64" font-family="Arial, sans-serif" font-weight="900" font-size="15" fill="#fff" text-anchor="middle">В ЭФИРЕ</text>
{eye(52, 75, 0.55)}<path d="M72 75 Q76 71 80 75" fill="none" {ln("#3B3355", 2.4)}/>
<path d="M60 81 Q64 84 68 81" fill="none" {ln(O, 2)}/>
<rect x="44" y="104" width="40" height="10" rx="5" fill="#5C6496" {s('stroke-width="2.4"')}/>
{sparkle(16, 30, 4, "#FFE27A")}{sparkle(112, 34, 3.5, "#FFE27A")}
'''))

# 3 «Буфф» (Одинцово, «Театр и школа» 4–8 лет): картонное солнышко-реквизит на палочке выглядывает из кулисы
I["buff-odintsovo"] = ("картонное солнышко-реквизит на деревянной палочке, лучи вырезаны зигзагом",
    "выглядывает из-за синей кулисы над краем сцены, как будто наступило утро в детском спектакле", bg("#FFF4D6", "#F2A23A", f'''
<path d="M0 104 H128 V128 H0Z" fill="#B87A44" {s()}/>
<path d="M0 104 H128" stroke="#8E5A2E" stroke-width="3"/>
<path d="M-4 -4 H40 Q34 40 40 106 H-4Z" fill="#3D5DB8" {s()}/>
<path d="M10 0 Q8 50 12 104 M24 0 Q22 50 26 104" fill="none" stroke="#2B4592" stroke-width="2.6"/>
<path d="M76 104 V70" {ln(O, 8)}/><path d="M76 104 V70" {ln("#D9A066", 5)}/>
<path d="M76 18 L82 30 L95 24 L93 38 L107 40 L97 50 L107 60 L93 62 L95 76 L82 70 L76 82 L70 70 L57 76 L59 62 L45 60 L55 50 L45 40 L59 38 L57 24 L70 30Z" fill="#FFC531" {s()}/>
<circle cx="76" cy="50" r="18" fill="#FFE07A" {s('stroke-width="2.6"')}/>
{face(76, 49, 6, 0.6)}
<path d="M54 104 H100" stroke="{O}" stroke-width="2"/>
{sparkle(112, 20, 4)}{sparkle(52, 14, 3)}
'''))

# 4 Академия балета «Сказка»: Дюймовочка-балеринка делает арабеск в половинке грецкого ореха
I["skazka-ballet-nikulinskaya"] = ("крошечная балеринка-Дюймовочка в пачке из лепестков шиповника",
    "делает арабеск в половинке скорлупки грецкого ореха, которая плывёт по пруду между листьями кувшинок", bg("#E4F6FF", "#3B8FC9", f'''
<path d="M-4 86 Q64 76 132 86 V132 H-4Z" fill="#7FC8EE" {s()}/>
<path d="M12 100 Q22 96 32 100 M90 112 Q102 108 112 112" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<ellipse cx="104" cy="96" rx="16" ry="6" fill="#5DBB63" {s('stroke-width="2.4"')}/><path d="M104 96 L116 92" stroke="{O}" stroke-width="2"/>
<path d="M30 86 Q64 116 98 86 Q64 94 30 86Z" fill="#B07A45" {s()}/>
<path d="M38 90 Q64 104 90 90" fill="none" stroke="#8A5A2E" stroke-width="2"/>
{limb(62, 74, 60, 88, SKIN, 3.5)}{limb(66, 72, 86, 62, SKIN, 3.5)}
<path d="M52 72 Q64 62 76 72 Q64 78 52 72Z" fill="#FF9BB8" {s('stroke-width="2.4"')}/>
<path d="M60 56 L58 70 H70 L68 56Z" fill="#FF7FA8" {s('stroke-width="2.4"')}/>
{limb(60, 58, 48, 44, SKIN, 3)}{limb(68, 58, 80, 44, SKIN, 3)}
<circle cx="64" cy="46" r="9" fill="{SKIN}" {s('stroke-width="2.6"')}/>
<path d="M55 44 Q57 35 64 36 Q71 35 73 44 Q67 39 64 40 Q61 39 55 44Z" fill="#E7B85C" {s('stroke-width="2"')}/>
<circle cx="64" cy="35" r="3" fill="#E7B85C" {s('stroke-width="1.8"')}/>
{eye(61, 47, 0.38)}{eye(67, 47, 0.38)}
{sparkle(24, 30, 4.5)}{sparkle(100, 26, 3.5)}{sparkle(40, 16, 2.6)}
'''))

# 5 Ars Musica (вокал, гитара, фортепиано с 7 лет): нотная тетрадь на пружинке пишет ноты карандашом
I["ars-musica-dmitrovskoe"] = ("нотная тетрадь на спиральной пружинке с мордашкой на обложке",
    "сама записывает песню: держит карандаш и выводит ноты на нотном стане, который вылетает из неё лентой", bg("#F1E8FF", "#7046B8", f'''
<path d="M70 30 Q100 20 120 40 Q110 56 124 70" fill="none" {ln(O, 18)}/>
<path d="M70 30 Q100 20 120 40 Q110 56 124 70" fill="none" {ln("#fff", 14)}/>
<path d="M76 26 Q100 17 116 34 M78 30 Q100 22 113 37 M80 34 Q100 26 110 40" fill="none" stroke="#9A86C8" stroke-width="1.2"/>
{note(96, 30, 0.55)}{note(108, 42, 0.55)}
<rect x="22" y="38" width="58" height="72" rx="6" fill="#4FB3A9" {s()} transform="rotate(-8 51 74)"/>
<g transform="rotate(-8 51 74)">
<path d="M28 44 V104" stroke="#2E7F77" stroke-width="2"/>
<circle cx="22" cy="48" r="3.5" fill="none" {s('stroke-width="2.2"')}/><circle cx="22" cy="60" r="3.5" fill="none" {s('stroke-width="2.2"')}/>
<circle cx="22" cy="72" r="3.5" fill="none" {s('stroke-width="2.2"')}/><circle cx="22" cy="84" r="3.5" fill="none" {s('stroke-width="2.2"')}/>
<circle cx="22" cy="96" r="3.5" fill="none" {s('stroke-width="2.2"')}/>
<rect x="36" y="48" width="36" height="12" rx="2" fill="#fff" {s('stroke-width="2"')}/>
<path d="M40 52 H68 M40 55 H68" stroke="#7BA" stroke-width="1"/>
{face(54, 80, 8, 0.65)}
</g>
<path d="M84 72 L100 52" {ln(O, 8)}/><path d="M84 72 L100 52" {ln("#FFC93C", 5)}/>
<path d="M100 52 L104 46 L102 54Z" fill="#F4A6A6" {s('stroke-width="2"')}/>
<path d="M82 76 L84 72 L87 74Z" fill="{O}"/>
{sparkle(108, 96, 4)}{sparkle(16, 22, 3)}
'''))

# 6 «Моне Шагал» (рисование 2,5–13 лет): деревянный шарнирный манекен художника позирует, а рядом его набросок
I["mone-shagal-vershinina"] = ("светлый деревянный шарнирный манекен-человечек для рисования",
    "гордо позирует на подставке, подбоченясь, а рядом на листе — его смешной детский набросок углём", bg("#FFF1E8", "#C9805A", f'''
<rect x="78" y="22" width="40" height="56" rx="3" fill="#fff" {s()} transform="rotate(6 98 50)"/>
<g transform="rotate(6 98 50)" stroke="#555" stroke-width="2" fill="none" stroke-linecap="round">
<circle cx="98" cy="34" r="6"/><path d="M98 40 V58 M98 46 L88 40 M98 46 L108 52 M98 58 L92 70 M98 58 L104 70"/>
<path d="M95 33 h0.1 M101 33 h0.1" stroke-width="2.6"/>
</g>
<path d="M18 112 H66" {ln(O, 6)}/><path d="M42 112 V96" {ln(O, 7)}/><path d="M42 112 V96" {ln("#C69A63", 4)}/>
<g fill="#E8C48E" stroke="{O}" stroke-width="2.6" stroke-linejoin="round">
<ellipse cx="42" cy="78" rx="7" ry="11"/>
<ellipse cx="42" cy="60" rx="9" ry="10"/>
<ellipse cx="34" cy="94" rx="4" ry="9" transform="rotate(15 34 94)"/><ellipse cx="50" cy="94" rx="4" ry="9" transform="rotate(-15 50 94)"/>
<ellipse cx="28" cy="66" rx="3.5" ry="9" transform="rotate(50 28 66)"/><ellipse cx="22" cy="76" rx="3.5" ry="8" transform="rotate(-30 22 76)"/>
<ellipse cx="56" cy="66" rx="3.5" ry="9" transform="rotate(-50 56 66)"/><ellipse cx="62" cy="76" rx="3.5" ry="8" transform="rotate(30 62 76)"/>
<circle cx="42" cy="38" r="11"/>
<circle cx="42" cy="50" r="3"/><circle cx="42" cy="88" r="3"/>
</g>
{eye(38, 38, 0.48)}{eye(46, 38, 0.48)}<path d="M39 44 Q42 46 45 44" fill="none" {ln(O, 1.8)}/>
<ellipse cx="34" cy="42" rx="2.6" ry="1.6" fill="#FF8FB0" opacity=".6"/><ellipse cx="50" cy="42" rx="2.6" ry="1.6" fill="#FF8FB0" opacity=".6"/>
{sparkle(70, 18, 4)}{sparkle(112, 96, 3.5)}
'''))

# 7 «Пантера» (джаз-модерн, мюзикл 4–12 лет): две белые перчатки делают «джазовые ручки» в луче сцены
I["pantera-dance-zarayskaya"] = ("пара белых танцевальных перчаток с растопыренными пальцами",
    "делают «джазовые ручки» — трепещут ладонями в жёлтом круге света на тёмно-бордовой сцене", bg("#6B1E3C", "#22081A", f'''
<path d="M40 0 L88 0 L118 128 L10 128Z" fill="#FFE58A" opacity=".22"/>
<ellipse cx="64" cy="112" rx="50" ry="10" fill="#FFE58A" opacity=".45"/>
<g transform="rotate(-18 40 64)">
<path d="M28 100 L30 78 Q18 70 22 60 L20 36 Q20 30 25 31 Q29 32 29 38 L30 54 L30 28 Q30 22 35 22 Q40 22 40 28 L40 52 L42 26 Q42 20 47 21 Q52 22 51 28 L50 54 L54 36 Q55 31 60 32 Q64 34 62 40 L56 70 Q54 80 48 84 L48 100Z" fill="#fff" {s()}/>
<path d="M26 100 H50" {ln(O, 6)}/><path d="M26 100 H50" {ln("#E8344E", 3)}/>
{face(38, 66, 5, 0.5)}
</g>
<g transform="rotate(18 88 64)">
<path d="M100 100 L98 78 Q110 70 106 60 L108 36 Q108 30 103 31 Q99 32 99 38 L98 54 L98 28 Q98 22 93 22 Q88 22 88 28 L88 52 L86 26 Q86 20 81 21 Q76 22 77 28 L78 54 L74 36 Q73 31 68 32 Q64 34 66 40 L72 70 Q74 80 80 84 L80 100Z" fill="#fff" {s()}/>
<path d="M78 100 H102" {ln(O, 6)}/><path d="M78 100 H102" {ln("#E8344E", 3)}/>
{face(90, 66, 5, 0.5)}
</g>
<path d="M12 46 L4 44 M14 34 L8 28 M116 46 L124 44 M114 34 L120 28" {ln("#FFE58A", 3)}/>
{sparkle(64, 18, 4, "#FFE58A")}{sparkle(20, 96, 3, "#FFE58A")}
'''))

# 8 Danzart (детский и современный танец с 3 лет): радужные вязаные гетры танцуют на кончиках пальцев
I["danzart-rimskogo-korsakova"] = ("пара радужных вязаных танцевальных гетр на тоненьких ножках",
    "кружатся на полупальцах по светлому паркету зала, оставляя за собой разноцветный завиток движения", bg("#E9FBFF", "#45B5C9", f'''
<path d="M0 100 H128 V128 H0Z" fill="#F2D3A6"/><path d="M0 100 H128 M20 100 L10 128 M56 100 L52 128 M92 100 L96 128" stroke="#D9B07A" stroke-width="2"/>
<path d="M14 72 Q30 40 62 46 Q96 52 112 26" fill="none" {ln("#FF6FA8", 5)} opacity=".8"/>
<path d="M14 80 Q34 52 64 56 Q96 60 116 36" fill="none" {ln("#FFC531", 5)} opacity=".8"/>
<g>
<path d="M44 62 L42 98" {ln(O, 9)}/><path d="M44 62 L42 98" {ln(SKIN, 6)}/>
<path d="M30 52 H56 L54 88 H32Z" fill="#FF6FA8" {s()}/>
<path d="M31 60 H55 M31.5 68 H54.5 M32 76 H54 M32.5 84 H53.5" stroke="#3B3355" stroke-width="2"/>
<path d="M31 60 H55 V68 H31Z" fill="#FFC531"/><path d="M32 76 H54 V84 H32Z" fill="#5BC0EB"/>
<path d="M30 52 H56 L54 88 H32Z" fill="none" {s()}/>
<path d="M38 98 Q44 102 48 98 L46 104 H38Z" fill="#F5B7C9" {s('stroke-width="2.4"')}/>
{face(43, 45, 6, 0.5, blush=False)}
</g>
<g transform="rotate(14 86 70)">
<path d="M86 62 L84 98" {ln(O, 9)}/><path d="M86 62 L84 98" {ln(SKIN, 6)}/>
<path d="M72 52 H98 L96 88 H74Z" fill="#8E6CF0" {s()}/>
<path d="M73 60 H97 V68 H73Z" fill="#7CD26E"/><path d="M74 76 H96 V84 H74Z" fill="#FF8A3D"/>
<path d="M73 60 H97 M73.5 68 H96.5 M74 76 H96 M74.5 84 H95.5" stroke="#3B3355" stroke-width="2"/>
<path d="M72 52 H98 L96 88 H74Z" fill="none" {s()}/>
<path d="M80 98 Q86 102 90 98 L88 104 H80Z" fill="#F5B7C9" {s('stroke-width="2.4"')}/>
</g>
{sparkle(108, 92, 4)}{sparkle(20, 22, 3.5)}
'''))

# 9 «Русский балет» (Королёв, балет 3–13 лет): серебристая ракета в розовой пачке стоит на носочке
I["russian-ballet-korolev-pionerskaya"] = ("серебристая ракета с иллюминатором-мордашкой в розовой балетной пачке",
    "стоит на носочке-сопле, как на пуанте, и делает плие над звёздным небом, вместо огня — блёстки", bg("#2B2F6B", "#0E0F2A", f'''
<circle cx="20" cy="24" r="1.6" fill="#fff"/><circle cx="108" cy="40" r="1.4" fill="#fff"/><circle cx="96" cy="14" r="1.2" fill="#fff"/>
<circle cx="18" cy="70" r="1.3" fill="#fff"/><circle cx="114" cy="84" r="1.6" fill="#fff"/>
<path d="M64 12 Q82 30 80 66 L48 66 Q46 30 64 12Z" fill="#DDE3EE" {s()}/>
<path d="M48 54 L34 70 L48 68Z M80 54 L94 70 L80 68Z" fill="#E8344E" {s()}/>
<circle cx="64" cy="40" r="11" fill="#9FD6FF" {s()}/>
{face(64, 40, 4.5, 0.42)}
<path d="M30 70 Q64 54 98 70 Q90 80 64 78 Q38 80 30 70Z" fill="#FF9BC4" {s()}/>
<path d="M36 70 Q64 62 92 70" fill="none" stroke="#fff" stroke-width="2"/>
<path d="M56 78 L60 96 H68 L72 78Z" fill="#B0B7C3" {s()}/>
<path d="M58 98 L64 108 L70 98" fill="#FFC1D8" {s('stroke-width="2.4"')}/>
{sparkle(52, 114, 3.5, "#FFE27A")}{sparkle(76, 118, 3, "#FF9BC4")}{sparkle(64, 124, 2.5, "#FFE27A")}
{sparkle(104, 22, 4)}
'''))

# 10 WestEnd (мюзикл: вокал, танец, актёрское): девочка качается на флажке огромной ноты и поёт
I["westend-mytishchi"] = ("девочка-солистка в малиновом платье с блёстками",
    "качается, как на качелях, на флажке огромной чёрной ноты-восьмушки и поёт, а нота подпевает ей", bg("#FFE9F2", "#D6457C", f'''
<ellipse cx="44" cy="96" rx="26" ry="19" fill="#2B2440" transform="rotate(-20 44 96)" {s()}/>
<path d="M66 86 V22" {ln(O, 10)}/><path d="M66 86 V22" {ln("#2B2440", 6)}/>
<path d="M66 22 Q98 30 104 58 Q92 44 66 42" fill="#2B2440" {s()}/>
{eye(38, 94, 0.55)}{eye(50, 92, 0.55)}<ellipse cx="45" cy="102" rx="3" ry="2.6" fill="#E8344E"/>
<path d="M86 50 L92 78 M100 56 L100 80" {ln("#C9C3D9", 2)}/>
<path d="M84 80 H106" {ln(O, 6)}/><path d="M84 80 H106" {ln("#C08A4E", 3)}/>
{limb(90, 80, 88, 96, SKIN, 3.5)}{limb(98, 80, 102, 96, SKIN, 3.5)}
<path d="M84 80 L88 62 H100 L104 80Z" fill="#E0216E" {s()}/>
<circle cx="91" cy="70" r="1.2" fill="#fff"/><circle cx="97" cy="74" r="1.2" fill="#fff"/><circle cx="94" cy="66" r="1" fill="#fff"/>
{limb(90, 64, 86, 52, SKIN, 3)}{limb(98, 64, 100, 54, SKIN, 3)}
<circle cx="94" cy="50" r="9" fill="{SKIN}" {s('stroke-width="2.6"')}/>
<path d="M85 50 Q86 40 94 40 Q102 40 103 50 Q104 58 100 60 Q100 46 94 45 Q88 46 88 60 Q84 58 85 50Z" fill="#3D2A1E" {s('stroke-width="2"')}/>
{eye(91, 51, 0.35)}{eye(97, 51, 0.35)}<ellipse cx="94" cy="55.5" rx="2" ry="2.2" fill="#C2365A"/>
{note(24, 40, 0.6, "#fff")}{note(116, 100, 0.6, "#fff")}
{sparkle(30, 18, 4)}{sparkle(116, 30, 3.5)}
'''))

# 11 «Акт Плэйс» (Мытищи, 3,5–11 лет): мальчик в бумажных заячьих ушках кланяется, на сцену летят цветы
I["act-place-mytishchi"] = ("мальчик в бумажных заячьих ушках на ободке и белом комбинезоне с хвостиком-помпоном",
    "низко кланяется после детского спектакля у рампы, а из зала на сцену летят три ромашки", bg("#F3FFE6", "#7BB84A", f'''
<path d="M0 98 H128 V128 H0Z" fill="#7A4A2A" {s()}/>
<path d="M8 98 h10 M30 98 h10 M52 98 h10 M74 98 h10 M96 98 h10 M118 98 h10" stroke="#FFE27A" stroke-width="4" stroke-linecap="round"/>
<path d="M-4 -4 H132 V14 Q116 22 100 14 Q84 22 64 14 Q44 22 28 14 Q12 22 -4 14Z" fill="#C2273E" {s()}/>
{limb(56, 76, 52, 96, "#fff", 6)}{limb(66, 76, 70, 96, "#fff", 6)}
<path d="M44 52 Q60 42 74 56 L70 80 H50Z" fill="#fff" {s()}/>
<circle cx="44" cy="70" r="6" fill="#fff" {s('stroke-width="2.6"')}/>
{limb(58, 56, 76, 72, "#fff", 5)}
<g transform="rotate(38 72 54)">
<circle cx="72" cy="54" r="11" fill="{SKIN}" {s()}/>
<path d="M62 50 Q72 38 82 50" fill="none" {ln(O, 5)}/><path d="M62 50 Q72 38 82 50" fill="none" {ln("#FF9BC4", 2.5)}/>
<path d="M66 44 Q60 22 66 18 Q72 22 70 43Z M76 43 Q78 20 86 22 Q88 30 79 45Z" fill="#fff" {s('stroke-width="2.6"')}/>
<path d="M66 40 Q64 28 66 24 M78 40 Q80 30 84 26" stroke="#FF9BC4" stroke-width="2.4" fill="none"/>
<path d="M68 56 Q70 58 72 56 M74 56 Q76 58 78 56" fill="none" {ln(O, 2)}/>
<path d="M70 61 Q73 63 76 61" fill="none" {ln(O, 1.8)}/>
</g>
<g fill="#fff" {s('stroke-width="2"')}>
<circle cx="24" cy="44" r="6"/><circle cx="104" cy="40" r="6"/><circle cx="96" cy="74" r="5"/>
</g>
<circle cx="24" cy="44" r="2.6" fill="#FFC531"/><circle cx="104" cy="40" r="2.6" fill="#FFC531"/><circle cx="96" cy="74" r="2.2" fill="#FFC531"/>
<path d="M24 50 L20 60 M104 46 L108 56 M96 79 L92 88" {ln("#4CAF50", 2.4)}/>
'''))

# 12 «Оранжевый кот» (рисование 3–15 лет): рыжий котёнок в берете рисует хвостом-кисточкой
I["orange-kot-mytishchi"] = ("пушистый оранжевый котёнок в синем берете художника",
    "сидит перед листом и рисует собственным хвостом, обмакнув его кончик в голубую краску, — на листе уже рыбка", bg("#E6F0FF", "#5279C9", f'''
<rect x="68" y="28" width="48" height="60" rx="3" fill="#fff" {s()}/>
<path d="M78 58 Q90 46 102 58 Q90 70 78 58Z M102 58 L110 50 L110 66Z" fill="#7EC3F2" {s('stroke-width="2.2"')}/>
<circle cx="86" cy="56" r="1.8" fill="{O}"/>
<path d="M0 108 H128 V128 H0Z" fill="#C9D8F2"/>
<ellipse cx="42" cy="96" rx="22" ry="18" fill="#FF9A3C" {s()}/>
<path d="M58 100 Q76 112 74 90 Q72 76 80 66" fill="none" {ln(O, 9)}/><path d="M58 100 Q76 112 74 90 Q72 76 80 66" fill="none" {ln("#FF9A3C", 6)}/>
<ellipse cx="81" cy="64" rx="4" ry="5" fill="#5BA8E6" {s('stroke-width="2.2"')}/>
<path d="M32 104 V112 M50 104 V112" {ln(O, 7)}/><path d="M32 104 V112 M50 104 V112" {ln("#FFB466", 4)}/>
<path d="M26 52 L22 34 L36 44Z M58 52 L62 34 L48 44Z" fill="#FF9A3C" {s()}/>
<path d="M27 48 L25 40 L32 45Z M57 48 L59 40 L52 45Z" fill="#FFC9A0"/>
<circle cx="42" cy="60" r="19" fill="#FF9A3C" {s()}/>
<path d="M36 46 L38 52 M42 44 V51 M48 46 L46 52" stroke="#D9701C" stroke-width="2.4" stroke-linecap="round"/>
<ellipse cx="42" cy="40" rx="17" ry="6" fill="#3E5BB8" {s()}/><circle cx="42" cy="33" r="3" fill="#3E5BB8" {s('stroke-width="2"')}/>
{face(42, 62, 7, 0.6, mouth=False)}
<path d="M38 69 Q42 72 46 69 M42 67 V69" fill="none" {ln(O, 1.8)}/>
<path d="M24 64 L14 62 M24 68 L14 70 M60 64 L70 62 M60 68 L70 70" stroke="{O}" stroke-width="1.4"/>
{sparkle(20, 22, 4)}
'''))

# 13 «Лис и Сирин» (художественная школа 4–16 лет): расписная птица Сирин на доске городецкой росписи
I["lis-i-sirin-mytishchi"] = ("сказочная птица Сирин с девичьим личиком, в золотой короне и с пёстрым хвостом",
    "сидит на ветке, нарисованной на деревянной разделочной доске в стиле городецкой росписи, вокруг — алые купавки", bg("#FFF0D6", "#C97A2E", f'''
<path d="M30 6 Q30 -2 38 -2 H90 Q98 -2 98 6 V8 H30Z" fill="#E6B472" {s()}/>
<rect x="12" y="8" width="104" height="116" rx="30" fill="#F2C98A" {s()}/>
<path d="M22 92 Q64 80 106 96" fill="none" {ln("#6B3E1C", 4)}/>
<circle cx="28" cy="100" r="9" fill="#D6283A" {s('stroke-width="2.4"')}/><circle cx="28" cy="100" r="4" fill="#FFB0B0"/>
<circle cx="100" cy="104" r="9" fill="#D6283A" {s('stroke-width="2.4"')}/><circle cx="100" cy="104" r="4" fill="#FFB0B0"/>
<path d="M72 74 Q102 60 110 34 Q96 48 88 46 Q100 36 98 22 Q86 40 76 46Z" fill="#2E7DBE" {s()}/>
<path d="M86 52 Q98 42 104 32 M84 58 Q100 52 108 42" fill="none" stroke="#FFD86B" stroke-width="2"/>
<path d="M40 66 Q42 46 58 44 Q76 46 76 66 Q72 84 54 86 Q40 82 40 66Z" fill="#1E1E2E" {s()}/>
<path d="M48 68 Q58 58 70 66 Q62 76 48 68Z" fill="#E8B23A" {s('stroke-width="2"')}/>
<path d="M52 86 L50 92 M58 86 L60 92" {ln(O, 3)}/>
<circle cx="50" cy="38" r="11" fill="{SKIN}" {s()}/>
<path d="M40 36 Q42 26 50 26 Q58 26 60 36 Q54 30 50 31 Q46 30 40 36Z" fill="#3D2A1E" {s('stroke-width="2"')}/>
<path d="M42 26 L44 16 L48 22 L50 14 L52 22 L56 16 L58 26Z" fill="#FFC531" {s('stroke-width="2.2"')}/>
{eye(46, 39, 0.4)}{eye(54, 39, 0.4)}<path d="M48 44 Q50 45.5 52 44" fill="none" {ln(O, 1.6)}/>
<ellipse cx="44" cy="43" rx="2.4" ry="1.4" fill="#FF7FA8" opacity=".6"/><ellipse cx="56" cy="43" rx="2.4" ry="1.4" fill="#FF7FA8" opacity=".6"/>
'''))

# 14 «Физалис Арт» (художественная студия с 5 лет): оранжевый физалис в бумажном фонарике рисует акварелью
I["fizalis-art-mikhaylova"] = ("оранжевая ягодка физалиса в раскрытом бумажном фонарике-чашечке",
    "выглядывает из фонарика, держит акварельную кисточку и ставит на мокрый лист круглую оранжевую кляксу-солнце", bg("#FFF6E6", "#E07B2E", f'''
<rect x="14" y="70" width="76" height="48" rx="3" fill="#fff" {s()} transform="rotate(-6 52 94)"/>
<circle cx="40" cy="96" r="11" fill="#FFB347" opacity=".75"/><circle cx="64" cy="100" r="7" fill="#7EC3F2" opacity=".75"/>
<path d="M22 112 Q40 104 60 112" fill="none" stroke="#9BD48A" stroke-width="5" opacity=".8" stroke-linecap="round"/>
<path d="M84 18 L80 8" {ln(O, 6)}/><path d="M84 18 L80 8" {ln("#7A5A2E", 3)}/>
<path d="M84 18 Q58 22 56 48 Q60 66 78 74 Q72 54 84 40 Q96 54 90 74 Q108 66 112 48 Q110 22 84 18Z" fill="#F3D9A4" {s()}/>
<path d="M84 18 Q76 40 78 74 M84 18 Q92 40 90 74" fill="none" stroke="#D9B477" stroke-width="2"/>
<circle cx="84" cy="56" r="13" fill="#FF8A1E" {s()}/>
{face(84, 56, 5, 0.5)}
<path d="M72 60 L50 88" {ln(O, 6)}/><path d="M72 60 L50 88" {ln("#C0392B", 3.5)}/>
<path d="M50 88 L46 96 L54 92Z" fill="#FFB347" {s('stroke-width="2"')}/>
{sparkle(112, 92, 4)}{sparkle(22, 24, 3.5)}{sparkle(46, 40, 2.6)}
'''))

if __name__ == "__main__":
    if "--subjects" in sys.argv:
        for k, (h, sc, _) in I.items():
            print(f"{k} — герой: {h} | сцена: {sc}")
        sys.exit()
    for k, (_, _, svg) in I.items():
        open(os.path.join(ROOT, "icons-src", k + ".svg"), "w").write(svg)
    print(len(I))
