"""Иконки робота creative, 12.11 (запуск 1112p). Каждая придумана и нарисована отдельно: свой герой, своя сцена,
своя компоновка и свой фон (правило абсолютной уникальности). python3 tools/icons_creative_1112p.py → icons-src/<id>.svg"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_creative_1112k import bg, ln, limb, note, head, SKIN

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
I = {}


def hand(x, y, r=5):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{SKIN}" {s("stroke-width=\"2.2\"")}/>'


# 1 Der Вальс (бальные): ботинок и туфелька кружатся вальсом по паркету
I["der-valts-chertanovo"] = ("чёрный лакированный бальный ботинок и серебряная туфелька на каблучке",
    "кружатся парой в вальсе по золотому паркету, оставляя след-завиток «раз-два-три»", bg("#FFF1D6", "#B7782E", f'''
<path d="M0 98 L128 88 V128 H0Z" fill="#D9A55A"/><path d="M0 108 L128 98 M0 118 L128 108 M30 96 L32 128 M70 92 L72 128 M106 90 L108 128" stroke="#B8823F" stroke-width="2"/>
<path d="M14 92 Q24 70 44 84 Q64 98 84 80 Q100 66 116 76" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="2 6" stroke-linecap="round"/>
<g transform="rotate(-8 40 70)">
<path d="M12 80 Q10 60 26 56 L38 54 Q44 66 58 68 Q70 70 68 82 Z" fill="#1D1B24" {s()}/>
<path d="M12 82 H68" {ln(O, 5)}/><path d="M26 58 L34 64 M30 56 L38 62" stroke="#fff" stroke-width="1.6"/>
<path d="M18 62 Q24 58 30 60" stroke="#fff" stroke-width="2.4" fill="none" opacity=".7"/>
{eye(48, 74, 0.55)}{eye(58, 74, 0.55)}</g>
<g transform="rotate(10 90 60)">
<path d="M66 64 Q72 58 82 60 Q92 64 100 54 Q106 46 114 48 Q118 52 116 58 L112 60 L110 76 L106 76 L106 62 Q94 70 82 70 Q68 72 66 64Z" fill="#DCE3EA" {s()}/>
<path d="M84 60 Q90 52 98 54" fill="none" {ln(O, 2)}/>
{eye(78, 65, 0.5)}{eye(87, 65, 0.5)}<ellipse cx="73" cy="68" rx="3" ry="1.8" fill="#FF7FA8" opacity=".7"/></g>
<text x="64" y="30" text-anchor="middle" font-family="Arial Black,Arial" font-weight="900" font-size="13" fill="#7A3E1A">раз·два·три</text>
{sparkle(110, 92, 4)}{sparkle(16, 44, 3.5)}
'''))

# 2 Wings: кроссовки с крылышками взлетают в прыжке
I["wings-tolbukhina"] = ("пара белых танцевальных кроссовок с ангельскими крылышками на пятках",
    "взлетают в прыжке хип-хопа над тёмной сценой, внизу лёгкие тени", bg("#B9F1FF", "#2B6CB0", f'''
<ellipse cx="44" cy="114" rx="18" ry="4" fill="#000" opacity=".25"/><ellipse cx="86" cy="118" rx="18" ry="4" fill="#000" opacity=".25"/>
<g transform="rotate(-14 44 62)">
<path d="M18 70 Q18 52 34 50 L44 50 Q48 60 60 62 Q72 64 70 74 L20 76Z" fill="#fff" {s()}/>
<path d="M18 72 H70" stroke="#FF5A7A" stroke-width="4"/><path d="M34 54 L40 60 M38 52 L44 58" {ln(O, 2)}/>
<path d="M18 58 Q4 50 2 36 Q12 44 18 44 Q8 34 12 24 Q20 36 26 48Z" fill="#FFF8E1" {s('stroke-width="2.4"')}/>
{eye(50, 66, 0.55)}{eye(60, 67, 0.55)}</g>
<g transform="rotate(10 88 86)">
<path d="M62 94 Q62 76 78 74 L88 74 Q92 84 104 86 Q116 88 114 98 L64 100Z" fill="#fff" {s()}/>
<path d="M62 96 H114" stroke="#FF5A7A" stroke-width="4"/><path d="M78 78 L84 84 M82 76 L88 82" {ln(O, 2)}/>
<path d="M62 82 Q48 74 46 60 Q56 68 62 68 Q52 58 56 48 Q64 60 70 72Z" fill="#FFF8E1" {s('stroke-width="2.4"')}/>
{eye(94, 90, 0.55)}{eye(104, 91, 0.55)}</g>
{sparkle(104, 30, 5)}{sparkle(24, 96, 3.5)}{sparkle(70, 22, 3)}
'''))

# 3 Go! Drums: малый барабан и палочки выбивают дробь
I["go-drums-syromyatnichesky"] = ("красный малый барабан с мордашкой на боку",
    "две деревянные палочки выбивают на нём дробь, сверху летят жёлтые искры-звёздочки", bg("#FFF3C4", "#E08A1E", f'''
<path d="M40 104 L30 124 M88 104 L98 124 M64 106 V124" {ln(O, 4)}/>
<ellipse cx="64" cy="64" rx="38" ry="12" fill="#F3F0E8" {s()}/>
<path d="M26 64 V94 Q64 112 102 94 V64 Q64 82 26 64Z" fill="#E33B3B" {s()}/>
<path d="M26 70 Q64 88 102 70 M26 90 Q64 108 102 90" fill="none" stroke="#C9CED6" stroke-width="5"/>
<path d="M34 72 L42 96 M54 78 L58 102 M74 78 L70 102 M94 72 L86 96" {ln("#C9CED6", 2.4)}/>
{face(64, 88, 10, 0.8)}
<path d="M20 22 L56 58" {ln(O, 8)}/><path d="M20 22 L56 58" {ln("#E8B66A", 5)}/><circle cx="57" cy="59" r="3.5" fill="#E8B66A" {s('stroke-width="2"')}/>
<path d="M108 20 L74 56" {ln(O, 8)}/><path d="M108 20 L74 56" {ln("#E8B66A", 5)}/><circle cx="73" cy="57" r="3.5" fill="#E8B66A" {s('stroke-width="2"')}/>
{sparkle(64, 34, 6, "#FFE14A")}{sparkle(44, 40, 4, "#FFE14A")}{sparkle(86, 40, 4, "#FFE14A")}
'''))

# 4 My Vocal Space: девочка поёт в куполе НЛО над звёздами
I["my-vocal-space-shchipok"] = ("серебристое НЛО со стеклянным куполом и поющей девочкой внутри",
    "летит по ночному небу, из купола вылетают светящиеся ноты к звёздам", bg("#5B4BB7", "#120E3A", f'''
<g fill="#fff">{''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in ((18,30,1.6),(30,96,1.3),(104,24,1.8),(112,100,1.4),(20,70,1.2),(96,112,1.2)))}</g>
<path d="M44 96 L30 120 H98 L84 96Z" fill="#FFF59D" opacity=".28"/>
<path d="M40 70 Q40 40 64 40 Q88 40 88 70Z" fill="#BFE9FF" fill-opacity=".75" {s()}/>
{head(64, 60, 11, "#8E4A1E")}
<path d="M72 66 L80 58" {ln(O, 4)}/><circle cx="82" cy="56" r="4" fill="#555" {s('stroke-width="2"')}/>
<ellipse cx="64" cy="78" rx="46" ry="13" fill="#D5DCE6" {s()}/>
<ellipse cx="64" cy="76" rx="30" ry="5" fill="#AEB8C6"/>
<g fill="#FFD23A" {s('stroke-width="2"')}>{''.join(f'<circle cx="{x}" cy="84" r="3.4"/>' for x in (34, 50, 64, 78, 94))}</g>
{note(96, 34, 0.9, "#FFE14A")}{note(26, 46, 0.75, "#9BF0FF")}{note(110, 54, 0.6, "#FF9CC8")}
'''))

# 5 Julia Vocal: рыжая девочка поёт в микрофон на стойке
I["julia-vocal-zatsepa"] = ("девочка с рыжими кудряшками в жёлтом платье",
    "зажмурившись, поёт в микрофон на высокой стойке, вокруг порхают розовые сердечки", bg("#FFE6EF", "#E0567E", f'''
<path d="M88 50 V116 M76 118 H100" {ln(O, 5)}/><path d="M88 50 V116 M76 118 H100" {ln("#7A7F8C", 3)}/>
<path d="M88 50 L76 54" {ln(O, 4)}/><rect x="66" y="48" width="12" height="16" rx="6" fill="#333" {s('stroke-width="2.4"')} transform="rotate(-20 72 56)"/>
<path d="M42 78 H62 L72 116 H32Z" fill="#FFD23A" {s()}/>
{limb(58, 82, 66, 64, SKIN, 5)}{hand(67, 62, 4.5)}{limb(44, 82, 34, 98, SKIN, 5)}
<g fill="#E86A2A" {s('stroke-width="2.2"')}>{''.join(f'<circle cx="{x}" cy="{y}" r="7"/>' for x, y in ((36,44),(40,34),(52,28),(64,34),(66,46),(34,56)))}</g>
<circle cx="50" cy="52" r="14" fill="{SKIN}" {s()}/>
<path d="M42 50 q3 3 6 0 M52 50 q3 3 6 0" fill="none" {ln(O, 2.2)}/>
<ellipse cx="55" cy="58" rx="3.5" ry="4" fill="#B3263E" {s('stroke-width="1.8"')}/>
<ellipse cx="42" cy="56" rx="3.5" ry="2" fill="#FF7FA8" opacity=".7"/>
<path d="M100 26 c-4 -6 -12 0 0 8 c12 -8 4 -14 0 -8Z M22 92 c-3 -4 -9 0 0 6 c9 -6 3 -10 0 -6Z M110 74 c-3 -4 -9 0 0 6 c9 -6 3 -10 0 -6Z" fill="#FF4F86" {s('stroke-width="1.8"')}/>
'''))

# 6 Просвет Мьюзик: раскрытый песенник выпускает ноты в луче света
I["prosvet-music-valovaya"] = ("раскрытый песенник в зелёной обложке с мордашкой на корешке",
    "из его страниц веером вылетают разноцветные ноты в косом луче света", bg("#E9FFF1", "#3E9E6E", f'''
<path d="M64 70 L10 0 H70Z" fill="#FFFDE0" opacity=".55"/>
<path d="M20 74 Q42 64 64 74 Q86 64 108 74 V112 Q86 102 64 112 Q42 102 20 112Z" fill="#2E8B57" {s()}/>
<path d="M24 70 Q44 60 64 70 V106 Q44 96 24 104Z" fill="#fff" {s()}/>
<path d="M104 70 Q84 60 64 70 V106 Q84 96 104 104Z" fill="#fff" {s()}/>
<path d="M30 76 Q44 70 58 76 M30 84 Q44 78 58 84 M70 76 Q84 70 98 76 M70 84 Q84 78 98 84" fill="none" stroke="#B9C4CC" stroke-width="2"/>
{eye(56, 94, 0.6)}{eye(72, 94, 0.6)}<path d="M60 100 Q64 104 68 100" fill="none" {ln(O, 2)}/>
{note(36, 46, 1.0, "#E8344A")}{note(58, 30, 0.9, "#2F7DE1")}{note(82, 40, 1.0, "#F2A400")}{note(100, 22, 0.75, "#9B4DE0")}
'''))

# 7 Талантино (киношкола): мальчик-актёр кланяется камере «REC»
I["talantino-tatarskaya"] = ("мальчик-актёр в синем пиджаке с красной бабочкой",
    "раскланивается перед кинокамерой на треноге, у камеры горит красная лампочка REC", bg("#E0ECFF", "#30406E", f'''
<rect x="0" y="108" width="128" height="20" fill="#1B2440"/>
<path d="M92 76 L80 112 M100 76 V112 M108 76 L120 112" {ln(O, 3.5)}/>
<rect x="84" y="56" width="32" height="22" rx="4" fill="#3A3F4B" {s()}/>
<path d="M84 62 L70 56 V78 L84 72Z" fill="#555B68" {s('stroke-width="2.4"')}/>
<circle cx="108" cy="62" r="3.5" fill="#FF2E3E"/><text x="98" y="74" font-family="Arial" font-weight="700" font-size="7" fill="#fff">REC</text>
<g transform="rotate(-22 40 90)">
<path d="M28 70 H52 L56 104 H24Z" fill="#2F5FD1" {s()}/>
{limb(30, 104, 30, 118, "#26304A", 6)}{limb(48, 104, 50, 118, "#26304A", 6)}
<path d="M34 70 L40 64 L46 70Z" fill="#fff"/><path d="M34 66 L40 70 L34 74Z M46 66 L40 70 L46 74Z" fill="#E8344A" {s('stroke-width="1.6"')}/>
{head(40, 52, 11, "#3A2418")}</g>
{limb(26, 78, 12, 92, "#2F5FD1", 5)}{limb(52, 66, 62, 52, "#2F5FD1", 5)}{hand(64, 50, 4.5)}
{sparkle(20, 30, 4)}{sparkle(64, 22, 3)}
'''))

# 8 Asnova (Гиляровского): красный аккордеон растягивает меха
I["asnova-gilyarovskogo"] = ("красный аккордеон с перламутровыми клавишами и мордашкой",
    "широко растягивает меха-гармошку, из складок вылетают ноты", bg("#FFF8E8", "#C9473B", f'''
<path d="M20 36 H40 V100 H20Z" fill="#C8232F" {s()}/>
<g fill="#fff" {s('stroke-width="1.8"')}>{''.join(f'<rect x="24" y="{y}" width="12" height="6" rx="1.5"/>' for y in range(42, 96, 9))}</g>
<path d="M40 40 L48 34 L56 40 L64 34 L72 40 L80 34 L88 40 V96 L80 102 L72 96 L64 102 L56 96 L48 102 L40 96Z" fill="#F0E2C8" {s()}/>
<path d="M48 34 V102 M56 40 V96 M64 34 V102 M72 40 V96 M80 34 V102" stroke="#C9A97A" stroke-width="2.4"/>
<path d="M88 36 H108 V100 H88Z" fill="#C8232F" {s()}/>
<g fill="#F5F5F5" {s('stroke-width="1.6"')}>{''.join(f'<circle cx="{x}" cy="{y}" r="2.6"/>' for x in (94, 102) for y in (48, 60, 72, 84))}</g>
{face(64, 66, 8, 0.75)}
{note(30, 18, 0.8, "#2F5FD1")}{note(98, 16, 0.8, "#F2A400")}{note(64, 120, 0.6, "#7A1E2A")}
'''))

# 9 Asnova (Страстной): золотой саксофон выдувает пузыри-ноты
I["asnova-strastnoy"] = ("золотой саксофон с мордашкой на раструбе",
    "играет джаз, выдувая из раструба круглые пузыри с нотками внутри", bg("#3C2A5E", "#130B24", f'''
<path d="M44 14 Q50 12 52 18 L54 26 Q56 32 54 40 L50 88 Q50 108 70 108 Q92 108 94 88 L94 76" fill="none" stroke="{O}" stroke-width="20" stroke-linecap="round"/>
<path d="M44 14 Q50 12 52 18 L54 26 Q56 32 54 40 L50 88 Q50 108 70 108 Q92 108 94 88 L94 76" fill="none" stroke="#F4B940" stroke-width="14" stroke-linecap="round"/>
<path d="M82 78 Q84 58 104 56 L110 74 Q96 76 94 88Z" fill="#F4B940" {s()}/>
<ellipse cx="107" cy="65" rx="5" ry="10" fill="#B07A16" {s('stroke-width="2.2"')} transform="rotate(-20 107 65)"/>
<g fill="#FFF3C0" {s('stroke-width="1.6"')}>{''.join(f'<circle cx="54" cy="{y}" r="2.4"/>' for y in (50, 62, 74))}</g>
{eye(66, 98, 0.6)}{eye(78, 98, 0.6)}<path d="M69 103 Q72 106 75 103" fill="none" {ln(O, 2)}/>
<circle cx="112" cy="36" r="10" fill="#9BE7FF" fill-opacity=".35" {s('stroke-width="2"')}/>{note(110, 40, 0.5, "#fff")}
<circle cx="96" cy="20" r="7" fill="#FF9CC8" fill-opacity=".35" {s('stroke-width="2"')}/>
<circle cx="26" cy="60" r="8" fill="#B6FFB0" fill-opacity=".3" {s('stroke-width="2"')}/>{note(24, 64, 0.4, "#fff")}
'''))

# 10 Guitardo: акустическая гитара-девочка с бантом сама перебирает струны
I["guitardo-samotechnaya"] = ("медовая акустическая гитара-девочка с красным бантом на колках",
    "сидит на табурете и сама перебирает свои струны, притопывая ножкой", bg("#E8F7FF", "#4D9BD0", f'''
<path d="M40 104 L36 124 M88 104 L92 124 M38 114 H90" {ln(O, 4)}/><rect x="32" y="98" width="64" height="8" rx="3" fill="#8A5A2B" {s('stroke-width="2.4"')}/>
<rect x="58" y="10" width="12" height="44" rx="3" fill="#6B3E1E" {s()}/>
<path d="M60 18 H68 M60 26 H68 M60 34 H68" stroke="#E7D6B8" stroke-width="1.6"/>
<path d="M54 12 L46 6 L46 20Z M74 12 L82 6 L82 20Z" fill="#E8344A" {s('stroke-width="2"')}/><circle cx="64" cy="12" r="4" fill="#E8344A" {s('stroke-width="2"')}/>
<path d="M64 46 Q44 46 44 62 Q44 70 50 74 Q36 80 38 92 Q42 104 64 104 Q86 104 90 92 Q92 80 78 74 Q84 70 84 62 Q84 46 64 46Z" fill="#F0B65A" {s()}/>
<circle cx="64" cy="76" r="7" fill="#3A2418"/>
<path d="M61 48 V98 M64 48 V98 M67 48 V98" stroke="#fff" stroke-width="1" opacity=".9"/>
{eye(54, 64, 0.6)}{eye(74, 64, 0.6)}<path d="M58 90 Q64 95 70 90" fill="none" {ln(O, 2.2)}/>
<ellipse cx="48" cy="70" rx="3.5" ry="2" fill="#FF7FA8" opacity=".7"/><ellipse cx="80" cy="70" rx="3.5" ry="2" fill="#FF7FA8" opacity=".7"/>
{limb(88, 84, 104, 74, "#F0B65A", 5)}{limb(40, 86, 24, 96, "#F0B65A", 5)}
{note(108, 50, 0.7, "#2F5FD1")}{note(18, 46, 0.6, "#E8344A")}
'''))

# 11 Студия Горшковой: девочка-подсолнух читает стихи на сцене
I["gorshkova-strastnoy"] = ("девочка-актриса в костюме подсолнуха с лепестками вокруг лица",
    "читает стихи на сцене между вишнёвыми кулисами, широко раскинув руки", bg("#FFF0D0", "#8E2E3F", f'''
<path d="M0 0 H30 Q24 60 34 128 H0Z" fill="#9C1F35" {s()}/><path d="M128 0 H98 Q104 60 94 128 H128Z" fill="#9C1F35" {s()}/>
<rect x="0" y="108" width="128" height="20" fill="#6B3A1C"/>
<path d="M50 74 H78 L84 110 H44Z" fill="#4CAF50" {s()}/>
{limb(52, 80, 30, 66, SKIN, 5)}{limb(76, 80, 98, 66, SKIN, 5)}{hand(28, 64)}{hand(100, 64)}
<g fill="#FFC928" {s('stroke-width="2.2"')}>{''.join(f'<ellipse cx="64" cy="31" rx="6" ry="11" transform="rotate({a} 64 50)"/>' for a in range(0, 360, 30))}</g>
<circle cx="64" cy="50" r="14" fill="{SKIN}" {s()}/>
{face(64, 49, 6, 0.6)}
{sparkle(46, 16, 3.5)}{sparkle(84, 14, 3)}
'''))

# 12 Том Сойер: мальчик в соломенной шляпе красит забор-декорацию
I["tom-soyer-sovarmii"] = ("веснушчатый мальчик в соломенной шляпе с малярной кистью",
    "на сцене красит белой краской деревянный забор-декорацию, половина досок уже белая", bg("#E3F5D8", "#5E8E3A", f'''
<rect x="0" y="110" width="128" height="18" fill="#7A4A22"/>
<g {s('stroke-width="2.4"')}>{''.join(f'<path d="M{x} 112 V50 L{x+6} 42 L{x+12} 50 V112Z" fill="{"#FFFFFF" if x < 60 else "#B9824A"}"/>' for x in range(4, 124, 14))}</g>
<path d="M0 64 H128 M0 96 H128" stroke="{O}" stroke-width="2.4"/>
<path d="M82 76 H104 L108 112 H78Z" fill="#3E7CC9" {s()}/>
{limb(84, 82, 66, 70, SKIN, 5)}<path d="M64 70 L52 62" {ln(O, 7)}/><path d="M64 70 L52 62" {ln("#B07A3A", 4)}/>
<rect x="44" y="52" width="12" height="12" rx="2" fill="#fff" {s('stroke-width="2.2"')} transform="rotate(-34 50 58)"/>
<circle cx="94" cy="60" r="13" fill="{SKIN}" {s()}/>{eye(89, 60, 0.6)}{eye(99, 60, 0.6)}
<g fill="#D98A4A">{''.join(f'<circle cx="{x}" cy="66" r="1.2"/>' for x in (86, 89, 99, 102))}</g>
<path d="M90 68 Q94 71 98 68" fill="none" {ln(O, 2)}/>
<ellipse cx="94" cy="49" rx="22" ry="5" fill="#F3D27A" {s()}/><path d="M82 48 Q84 34 94 34 Q104 34 106 48Z" fill="#F3D27A" {s()}/>
<path d="M83 45 H105" stroke="#C0392B" stroke-width="3"/>
'''))

# 13 Сагалова (showtime): девочка в мятном костюме прыгает в шпагате под конфетти
I["sagalova-sharikopodshipnikovskaya"] = ("девочка с высоким пучком в мятно-зелёном спортивном костюме",
    "прыгает в шпагате над полом танцкласса, сверху сыплется цветное конфетти", bg("#F3E9FF", "#7A4FC4", f'''
<rect x="0" y="112" width="128" height="16" fill="#3D2A6E"/>
<g>{''.join(f'<rect x="{x}" y="{y}" width="5" height="3" rx="1" fill="{c}" transform="rotate({r} {x} {y})"/>' for x, y, c, r in ((14,20,"#FFD23A",20),(30,40,"#FF5A7A",-30),(100,18,"#5CE1E6",40),(112,44,"#FFD23A",-10),(20,70,"#5CE1E6",60),(108,80,"#FF5A7A",15),(60,10,"#B6FF5C",-40),(80,30,"#FF9CC8",30)))}</g>
{limb(58, 76, 18, 84, "#4FD1A5", 6)}{limb(70, 76, 110, 84, "#4FD1A5", 6)}
<path d="M12 80 h8 v8 h-10Z M108 80 h8 v8 h-10Z" fill="#fff" {s('stroke-width="2"')}/>
<path d="M52 48 H76 L78 80 H50Z" fill="#4FD1A5" {s()}/>
{limb(54, 52, 36, 30, "#4FD1A5", 5)}{limb(74, 52, 92, 30, "#4FD1A5", 5)}{hand(34, 28, 4.5)}{hand(94, 28, 4.5)}
{head(64, 36, 11, "#6B3A1C")}<circle cx="64" cy="21" r="6" fill="#6B3A1C" {s('stroke-width="2.2"')}/>
'''))

# 14 Fot Baza (хип-хоп): подросток делает «волну» руками у кирпичной стены
I["fot-baza-sharikopodshipnikovskaya"] = ("подросток в широких штанах-карго и синей бандане",
    "делает руками «волну» поппинга у кирпичной стены, волна бежит по рукам пунктиром", bg("#FFD9C2", "#B5502E", f'''
<g stroke="#9A3E22" stroke-width="2" fill="none">{''.join(f'<path d="M0 {y} H128"/>' for y in range(14, 104, 14))}{''.join(f'<path d="M{x + (7 if (y // 14) % 2 else 0)} {y} V{y+14}"/>' for y in range(0, 104, 14) for x in range(0, 128, 22))}</g>
<rect x="0" y="104" width="128" height="24" fill="#4A4A55"/>
<path d="M50 84 L44 116 H58 L64 92 L70 116 H84 L78 84Z" fill="#8A8F5A" {s()}/>
<rect x="48" y="112" width="12" height="6" rx="2" fill="#fff" {s('stroke-width="2"')}/><rect x="70" y="112" width="12" height="6" rx="2" fill="#fff" {s('stroke-width="2"')}/>
<path d="M50 52 H78 L80 86 H48Z" fill="#F2F2F2" {s()}/>
<path d="M52 56 Q40 50 32 58 Q24 66 14 58" fill="none" {ln(O, 9)}/><path d="M52 56 Q40 50 32 58 Q24 66 14 58" fill="none" {ln(SKIN, 6)}/>
<path d="M76 56 Q88 64 96 56 Q104 48 114 56" fill="none" {ln(O, 9)}/><path d="M76 56 Q88 64 96 56 Q104 48 114 56" fill="none" {ln(SKIN, 6)}/>
<path d="M18 46 Q34 38 50 44 M78 44 Q96 38 112 46" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 5" stroke-linecap="round"/>
{head(64, 38, 12, "#2F5FD1")}<path d="M76 32 L86 28 L82 38Z" fill="#2F5FD1" {s('stroke-width="2"')}/>
'''))

# 15 Dance Rhythm (ТРЦ «Миля»): колонка-сабвуфер качает басом
I["dance-rhythm-zhulebino"] = ("чёрная колонка-сабвуфер с мордашкой над динамиком",
    "качает басом так, что от динамика расходятся бирюзовые кольца-волны и прыгают нотки", bg("#D5FFF7", "#14918A", f'''
<g fill="none" stroke="#fff" stroke-width="3" opacity=".8"><circle cx="64" cy="80" r="44"/><circle cx="64" cy="80" r="54"/></g>
<rect x="34" y="30" width="60" height="86" rx="10" fill="#26262E" {s()}/>
<circle cx="64" cy="86" r="20" fill="#3D3D48" {s()}/><circle cx="64" cy="86" r="12" fill="#5A5A68" {s('stroke-width="2.4"')}/><circle cx="64" cy="86" r="4" fill="#26262E"/>
<circle cx="64" cy="50" r="8" fill="#3D3D48" {s('stroke-width="2.4"')}/>
{eye(50, 48, 0.6)}{eye(78, 48, 0.6)}
<path d="M40 112 L36 120 M88 112 L92 120" {ln(O, 4)}/>
{note(18, 40, 0.8, "#FFE14A")}{note(106, 30, 0.8, "#FF5A7A")}{note(110, 98, 0.6, "#fff")}
'''))

# 16 Ровесник (детский ансамбль танца): девочка кружится в народном танце
I["rovesnik-kuusinena"] = ("девочка в расшитой алой юбке и белой блузе с цветными лентами в волосах",
    "кружится в народном танце, юбка раскрылась колоколом, ленты летят по кругу", bg("#FFF9E3", "#D99A1A", f'''
<path d="M64 74 L18 112 Q64 126 110 112Z" fill="#D9262F" {s()}/>
<path d="M26 108 Q64 120 102 108" fill="none" stroke="#FFD23A" stroke-width="4"/>
<g fill="#FFD23A">{''.join(f'<circle cx="{x}" cy="{y}" r="2.6"/>' for x, y in ((40,98),(52,104),(64,106),(76,104),(88,98)))}</g>
<path d="M54 52 H74 L76 76 H52Z" fill="#fff" {s()}/>
<path d="M56 60 H72" stroke="#D9262F" stroke-width="2.4"/>
{limb(54, 56, 32, 46, "#fff", 5)}{limb(74, 56, 96, 46, "#fff", 5)}{hand(30, 44, 4.5)}{hand(98, 44, 4.5)}
{head(64, 38, 12, "#C77B3A")}
<path d="M54 28 Q30 14 18 28 M74 28 Q98 14 110 28 M60 26 Q52 6 34 8" fill="none" stroke-width="3.5" stroke-linecap="round" stroke="#2F7DE1"/>
<path d="M68 26 Q80 6 98 10" fill="none" stroke="#4CAF50" stroke-width="3.5" stroke-linecap="round"/>
<circle cx="64" cy="26" r="4" fill="#FF5A7A" {s('stroke-width="1.8"')}/>
'''))

# 17 Молодой Балет Столицы: Спасская башня в пачке на брусчатке
I["molodoy-balet-opolcheniya"] = ("Спасская башня в белой балетной пачке",
    "стоит на одной ножке в арабеске на брусчатке Красной площади, звезда на шпиле сияет", bg("#E5ECFF", "#5E6FB8", f'''
<rect x="0" y="110" width="128" height="18" fill="#7D7F8C"/><g stroke="#5F616C" stroke-width="2">{''.join(f'<path d="M{x} 110 l-4 18"/>' for x in range(8, 128, 14))}</g>
<path d="M56 18 L64 4 L72 18Z" fill="#2E7D4F" {s('stroke-width="2.4"')}/>
<path d="M64 0 l2 4 4 1 -3 3 1 4 -4 -2 -4 2 1 -4 -3 -3 4 -1Z" fill="#E8344A" stroke="#8A1020" stroke-width="1"/>
<rect x="54" y="18" width="20" height="14" fill="#C23B2E" {s()}/>
<rect x="50" y="32" width="28" height="44" fill="#C23B2E" {s()}/>
<circle cx="64" cy="42" r="7" fill="#fff" {s('stroke-width="2.2"')}/><path d="M64 37 V42 L67 44" {ln(O, 1.8)}/>
{eye(58, 56, 0.6)}{eye(70, 56, 0.6)}<path d="M60 64 Q64 68 68 64" fill="none" {ln(O, 2)}/>
<path d="M26 76 Q64 64 102 76 Q106 84 98 86 Q64 78 30 86 Q22 84 26 76Z" fill="#fff" {s()}/>
<path d="M58 84 V112" {ln(O, 7)}/><path d="M58 84 V112" {ln("#C23B2E", 4)}/>
<path d="M70 84 L100 66" {ln(O, 7)}/><path d="M70 84 L100 66" {ln("#C23B2E", 4)}/>
<path d="M54 110 h8 v4 h-10Z" fill="#FFC1D9" {s('stroke-width="2"')}/>
{sparkle(84, 14, 4)}{sparkle(30, 30, 3)}
'''))

# 18 Ля Позитив: нота «ля» съезжает по нотному стану, как по горке
I["la-pozitiv-khoroshevskaya"] = ("весёлая оранжевая нота-восьмушка с мордашкой на головке",
    "съезжает по пяти линейкам нотного стана, как с горки, раскинув флажок", bg("#FFFCE0", "#F5B700", f'''
<g fill="none" stroke="#7A5A00" stroke-width="2.6">{''.join(f'<path d="M0 {40+i*9} Q64 {60+i*9} 128 {104+i*9}"/>' for i in range(5))}</g>
<g transform="rotate(28 60 70)">
<ellipse cx="54" cy="78" rx="18" ry="13" fill="#FF7A1A" {s()} transform="rotate(-20 54 78)"/>
<path d="M70 74 V30 Q86 36 90 50" fill="none" stroke="{O}" stroke-width="8" stroke-linecap="round"/>
<path d="M70 74 V30 Q86 36 90 50" fill="none" stroke="#FF7A1A" stroke-width="4.5" stroke-linecap="round"/>
{face(52, 76, 6, 0.6)}</g>
<path d="M14 98 q6 -4 12 0 M8 88 q6 -4 12 0" fill="none" {ln("#fff", 3)}/>
<text x="100" y="30" text-anchor="middle" font-family="Arial Black,Arial" font-weight="900" font-size="16" fill="#FF7A1A" stroke="{O}" stroke-width="1.4">ЛЯ!</text>
'''))

# 19 Реальное Рисование: мальчик в берете рисует дерево на холсте
I["realnoe-risovanie-azovskaya"] = ("мальчик в синем берете и фартуке в разноцветных пятнах",
    "длинной кистью дорисовывает на большом холсте зелёное дерево с красными яблоками", bg("#F0FBFF", "#68B7D8", f'''
<rect x="58" y="16" width="56" height="70" rx="2" fill="#fff" {s()}/>
<path d="M86 86 V60" {ln("#7A4A22", 6)}/><circle cx="86" cy="46" r="18" fill="#5CC15C" {s('stroke-width="2.4"')}/>
<g fill="#E8344A">{''.join(f'<circle cx="{x}" cy="{y}" r="3"/>' for x, y in ((78,40),(92,38),(86,52),(96,50),(76,52)))}</g>
<path d="M66 86 L60 120 M106 86 L112 120" {ln(O, 4)}/>
<path d="M22 72 H46 L50 116 H18Z" fill="#F5E6C8" {s()}/>
<g>{''.join(f'<circle cx="{x}" cy="{y}" r="3" fill="{c}"/>' for x, y, c in ((28,86,"#E8344A"),(40,94,"#2F7DE1"),(32,104,"#FFD23A"),(44,108,"#4CAF50")))}</g>
{limb(44, 78, 60, 62, SKIN, 5)}<path d="M60 62 L74 44" {ln(O, 5)}/><path d="M60 62 L74 44" {ln("#C98E52", 3)}/><circle cx="75" cy="43" r="2.6" fill="#5CC15C" {s('stroke-width="1.6"')}/>
{head(34, 56, 12, "#3A2418")}
<ellipse cx="32" cy="44" rx="15" ry="6" fill="#2F5FD1" {s()}/><circle cx="32" cy="38" r="2.5" fill="#2F5FD1" {s('stroke-width="1.8"')}/>
'''))

# 20 Sreda (танцы с 3 лет): девочка с длинным хвостом в контемпорари-изгибе
I["sreda-dance-zadonsky"] = ("девочка с длинным тёмным хвостом в бирюзовом топе и чёрных лосинах",
    "танцует контемпорари: глубоко прогнулась в сторону, одна рука тянется к луне-светильнику", bg("#2A2F5E", "#0D1030", f'''
<circle cx="104" cy="22" r="12" fill="#FFF3B0" {s('stroke-width="2.4"')}/>
<ellipse cx="64" cy="116" rx="40" ry="8" fill="#6B7BD8" opacity=".5"/>
{limb(60, 82, 48, 114, "#1A1A22", 6)}{limb(68, 82, 82, 114, "#1A1A22", 6)}
<path d="M54 56 Q62 50 72 54 L72 84 H56Z" fill="#26C6B4" {s()} transform="rotate(-16 64 70)"/>
{limb(66, 58, 94, 30, SKIN, 5)}{hand(96, 28, 4.5)}{limb(56, 62, 36, 76, SKIN, 5)}
{head(50, 44, 11, "#1E1A2E")}
<path d="M40 40 Q22 44 18 66 Q16 80 24 90" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M40 40 Q22 44 18 66 Q16 80 24 90" fill="none" stroke="#1E1A2E" stroke-width="5.5" stroke-linecap="round"/>
{sparkle(24, 22, 3)}{sparkle(112, 70, 3.5)}
'''))

# 21 Театр-студия Ато (актёрское и театр на английском): рыцарь в картонных доспехах декламирует
I["ato-teatr-6-parkovaya"] = ("маленький рыцарь-актёр в картонных серебряных доспехах",
    "декламирует на сцене с деревянным мечом, над ним облачко с надписью «Hello!»", bg("#E4FFE8", "#2E8F5A", f'''
<rect x="0" y="108" width="128" height="20" fill="#5B3A1E"/>
<path d="M22 0 V108 M106 0 V108" stroke="#C0392B" stroke-width="10"/>
<path d="M58 22 Q58 8 84 8 Q110 8 110 22 Q110 34 86 34 L80 42 L78 34 Q58 34 58 22Z" fill="#fff" {s('stroke-width="2.4"')}/>
<text x="84" y="26" text-anchor="middle" font-family="Arial Black,Arial" font-weight="900" font-size="12" fill="#2E8F5A">Hello!</text>
<path d="M44 70 H68 L70 104 H42Z" fill="#C9D2DC" {s()}/><path d="M44 80 H68 M44 90 H68" stroke="#8D98A6" stroke-width="2"/>
{limb(46, 104, 46, 114, "#5A4A3A", 5)}{limb(64, 104, 66, 114, "#5A4A3A", 5)}
{limb(66, 74, 84, 62, "#C9D2DC", 5)}<path d="M86 60 L104 42" {ln(O, 6)}/><path d="M86 60 L104 42" {ln("#C98E52", 3.5)}/><path d="M82 56 L90 64" {ln(O, 4)}/>
{limb(46, 74, 32, 86, "#C9D2DC", 5)}
<circle cx="56" cy="56" r="13" fill="#C9D2DC" {s()}/><rect x="47" y="52" width="18" height="10" rx="3" fill="{SKIN}" {s('stroke-width="2"')}/>
{eye(52, 57, 0.5)}{eye(60, 57, 0.5)}<path d="M56 43 Q62 34 70 38" fill="none" {ln("#E8344A", 4)}/>
'''))

# 22 Центр лёгкого рисунка: кисточка летит на воздушном шарике и оставляет радугу
I["legkiy-risunok-pervomayskaya"] = ("тонкая кисточка-малышка, привязанная к голубому воздушному шарику",
    "летит над листом бумаги и оставляет за собой лёгкий радужный мазок", bg("#FFF5FB", "#E8A3C7", f'''
<path d="M10 118 L118 96 L124 122 L16 128Z" fill="#fff" {s()}/>
<path d="M18 112 Q44 80 66 92 Q84 102 92 84" fill="none" stroke="#FF5A7A" stroke-width="5" stroke-linecap="round"/>
<path d="M20 118 Q46 86 68 98 Q86 108 94 90" fill="none" stroke="#FFD23A" stroke-width="5" stroke-linecap="round"/>
<path d="M22 124 Q48 92 70 104 Q88 114 96 96" fill="none" stroke="#4FC3F7" stroke-width="5" stroke-linecap="round"/>
<ellipse cx="80" cy="30" rx="18" ry="21" fill="#6EC6FF" {s()}/><path d="M78 51 l2 4 2 -4Z" fill="#6EC6FF" {s('stroke-width="1.6"')}/>
<path d="M72 20 Q76 14 82 16" stroke="#fff" stroke-width="3" fill="none" opacity=".8"/>
<path d="M80 55 Q76 66 86 70" fill="none" {ln(O, 1.8)}/>
<path d="M96 68 L84 80" {ln(O, 7)}/><path d="M96 68 L84 80" {ln("#D9A441", 4)}/>
<path d="M84 80 L88 84 L78 94 Q74 92 76 88Z" fill="#5B3A1E" {s('stroke-width="2"')}/>
{eye(91, 72, 0.45)}{eye(97, 67, 0.45)}
{sparkle(28, 30, 4)}{sparkle(112, 56, 3)}
'''))

# 23 Plastilinstars (балет 3–14): пластилиновая балерина в арабеске на дощечке для лепки
I["plastilinstars-butlerova"] = ("розовая пластилиновая балерина с синим пучком и пачкой из пластилиновых лепестков",
    "держит арабеск на зелёной дощечке для лепки, рядом лежит пластмассовый стек", bg("#FFF0E0", "#F08A5D", f'''
<rect x="10" y="100" width="108" height="16" rx="4" fill="#59B36A" {s()}/>
<path d="M88 106 L114 96" {ln(O, 6)}/><path d="M88 106 L114 96" {ln("#FFD23A", 3)}/>
<path d="M56 74 V100" {ln(O, 9)}/><path d="M56 74 V100" {ln("#FF9EB5", 6)}/>
<path d="M62 74 L98 62" {ln(O, 9)}/><path d="M62 74 L98 62" {ln("#FF9EB5", 6)}/>
<g {s('stroke-width="2"')}>{''.join(f'<ellipse cx="{x}" cy="{y}" rx="8" ry="4.5" fill="{c}" transform="rotate({r} {x} {y})"/>' for x, y, c, r in ((44,72,"#FFD23A",-20),(52,76,"#7FD3FF",-8),(62,77,"#B892FF",6),(72,74,"#FFD23A",18),(48,68,"#B892FF",-30),(70,69,"#7FD3FF",28)))}</g>
<path d="M52 46 Q60 42 66 46 L66 70 H52Z" fill="#FF9EB5" {s()}/>
{limb(54, 50, 34, 34, "#FF9EB5", 5)}{limb(64, 50, 82, 34, "#FF9EB5", 5)}
<circle cx="59" cy="34" r="11" fill="#FFC6D3" {s()}/><circle cx="59" cy="20" r="6" fill="#3F6FD8" {s('stroke-width="2.2"')}/>
{eye(55, 35, 0.55)}{eye(63, 35, 0.55)}<path d="M57 40 Q59 42 61 40" fill="none" {ln(O, 1.8)}/>
<path d="M50 30 q2 1 1 3 M66 28 q-2 2 0 3" fill="none" stroke="#E07090" stroke-width="1.4"/>
{sparkle(100, 26, 4.5)}{sparkle(22, 52, 3.5)}
'''))

# 24 Just a music studio (флейта, фортепиано, вокал с 3 лет): блок-флейта насвистывает
I["just-music-profsoyuznaya"] = ("голубая блок-флейта с мордашкой у мундштука",
    "стоит столбиком и насвистывает, из каждой дырочки выпрыгивает цветная нотка", bg("#EEF3FF", "#3E63C9", f'''
<path d="M54 10 Q64 4 74 10 L72 26 H56Z" fill="#9FD3FF" {s()}/>
<rect x="56" y="24" width="16" height="92" rx="7" fill="#6EB8FF" {s()}/>
<path d="M56 46 H72 M56 104 H72" stroke="{O}" stroke-width="2.2"/>
<g fill="#24305E">{''.join(f'<circle cx="64" cy="{y}" r="3"/>' for y in (58, 68, 78, 88, 98))}</g>
<rect x="60" y="14" width="8" height="4" rx="1.5" fill="#24305E"/>
{eye(60, 34, 0.55)}{eye(68, 34, 0.55)}<path d="M61 40 Q64 42 67 40" fill="none" {ln(O, 1.8)}/>
{note(86, 56, 0.6, "#FF5A7A")}{note(34, 66, 0.6, "#FFD23A")}{note(92, 80, 0.6, "#5CE18A")}{note(30, 90, 0.6, "#B892FF")}{note(88, 100, 0.55, "#FF9A3C")}
{limb(56, 70, 44, 80, "#6EB8FF", 4)}{limb(72, 70, 82, 62, "#6EB8FF", 4)}
'''))


if __name__ == "__main__":
    for pid, (hero, scene, svg_) in I.items():
        open(os.path.join(ROOT, "icons-src", pid + ".svg"), "w").write(svg_)
    if "--subjects" in sys.argv:
        p = os.path.join(ROOT, "icons-src", "subjects.txt")
        have = open(p, encoding="utf-8").read()
        with open(p, "a", encoding="utf-8") as f:
            for pid, (hero, scene, _) in I.items():
                if not any(l.startswith(pid + " — ") for l in have.splitlines()):
                    f.write(f"{pid} — герой: {hero} | сцена: {scene}\n")
    print(len(I))
