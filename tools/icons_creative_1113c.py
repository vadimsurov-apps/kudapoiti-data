"""Иконки робота creative, 13.11 (запуск 1113c). Каждая придумана и нарисована отдельно: свой герой, своя сцена,
своя компоновка и свой фон (правило абсолютной уникальности). python3 tools/icons_creative_1113c.py [--subjects]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_creative_1112k import bg, ln, limb, note, head, SKIN

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
I = {}
BL = '<ellipse cx="{x}" cy="{y}" rx="2.6" ry="1.5" fill="#FF7FA8" opacity=".6"/>'


def blush(x, y):
    return BL.format(x=x, y=y)


# 1 VocalMT (вокал, студия звукозаписи): табло «ON AIR» горит над микрофоном в пенной вокальной кабинке
I["vocalmt-polyanka"] = ("круглое красное табло «ON AIR» с мордашкой",
    "загорелось над детским микрофоном на стойке в вокальной кабинке со стенами из серых пенных пирамидок", bg("#5E6B7A", "#2E3742", f'''
<g fill="#7D8A99" {s('stroke-width="1.6"')}>
<path d="M4 70 l8 -8 8 8Z M20 70 l8 -8 8 8Z M92 70 l8 -8 8 8Z M108 70 l8 -8 8 8Z"/>
<path d="M4 88 l8 -8 8 8Z M20 88 l8 -8 8 8Z M92 88 l8 -8 8 8Z M108 88 l8 -8 8 8Z"/>
<path d="M4 106 l8 -8 8 8Z M20 106 l8 -8 8 8Z M92 106 l8 -8 8 8Z M108 106 l8 -8 8 8Z"/>
</g>
<path d="M64 120 V84" {ln(O, 7)}/><path d="M64 120 V84" {ln("#C9D1DA", 3.5)}/>
<path d="M50 122 H78" {ln(O, 7)}/><path d="M50 122 H78" {ln("#C9D1DA", 3.5)}/>
<rect x="55" y="58" width="18" height="30" rx="9" fill="#D8DEE6" {s()}/>
<path d="M57 66 H71 M57 72 H71 M57 78 H71" stroke="#8C96A3" stroke-width="2"/>
<circle cx="64" cy="34" r="25" fill="#FF4A4A" {s('stroke-width="3.4"')}/>
<circle cx="64" cy="34" r="19" fill="#FF7070" opacity=".6"/>
<text x="64" y="30" font-family="Arial" font-weight="bold" font-size="11" text-anchor="middle" fill="#fff">ON AIR</text>
{eye(57, 40, 0.5)}{eye(71, 40, 0.5)}<path d="M60 45 Q64 48 68 45" fill="none" {ln(O, 1.8)}/>
<path d="M30 22 L22 16 M98 22 L106 16 M28 36 H18 M100 36 H110" {ln("#FFB3B3", 3)}/>
'''))

# 2 «Дети Эволюции» (современный танец): росток в пачке встаёт из горшка на цыпочки
I["deti-evolyutsii-rossoshansky"] = ("зелёный росток в маленькой розовой балетной пачке",
    "вытягивается из глиняного горшка на цыпочки, раскинув два листика-руки в танцевальном па", bg("#F1E6FF", "#B49BE6", f'''
<path d="M40 92 H88 L82 122 H46Z" fill="#D9824E" {s()}/>
<path d="M36 86 H92 V96 H36Z" fill="#E89A66" {s()}/>
<path d="M64 86 Q60 70 64 54" fill="none" {ln(O, 8)}/><path d="M64 86 Q60 70 64 54" fill="none" {ln("#5CC46A", 4.5)}/>
<ellipse cx="64" cy="64" rx="22" ry="6" fill="#FFB3CF" {s()}/>
<path d="M44 64 Q64 72 84 64" fill="none" stroke="#FF8FB5" stroke-width="2"/>
<path d="M60 56 Q40 40 22 44 Q36 58 60 58Z" fill="#6FD47C" {s()}/>
<path d="M68 56 Q88 38 106 40 Q92 56 68 58Z" fill="#6FD47C" {s()}/>
<circle cx="64" cy="40" r="15" fill="#7EDB8A" {s()}/>
{face(64, 42, 7, 0.6)}
<path d="M60 26 Q64 16 70 22" fill="none" {ln(O, 5)}/><path d="M60 26 Q64 16 70 22" fill="none" {ln("#5CC46A", 2.5)}/>
{sparkle(104, 74, 4)}{sparkle(22, 76, 3.5)}{sparkle(98, 20, 3)}
'''))

# 3 «Аллегро» (эстрадный танец для малышей и школьников): девочка в шпагате в прыжке под конфетти
I["allegro-chertanovskaya"] = ("девочка в блестящем малиновом эстрадном костюме с золотой бахромой",
    "взлетела в прыжке-шпагате над сценой, а сверху на неё сыплется серебряное конфетти", bg("#8E1F3A", "#4A0C1E", f'''
<path d="M0 0 H22 Q18 50 26 128 H0Z M128 0 H106 Q110 50 102 128 H128Z" fill="#C2304F" {s()}/>
<path d="M8 0 Q6 60 12 128 M116 0 Q122 60 116 128" stroke="#9E2240" stroke-width="2.4" fill="none"/>
<ellipse cx="64" cy="116" rx="44" ry="10" fill="#E8B04A" {s()}/>
{limb(58, 76, 26, 84, SKIN, 4.5)}{limb(70, 76, 102, 70, SKIN, 4.5)}
<path d="M22 84 L28 81 L28 88Z" fill="#FFD43B" {s('stroke-width="1.6"')}/><path d="M104 66 L104 74 L98 70Z" fill="#FFD43B" {s('stroke-width="1.6"')}/>
{limb(58, 56, 40, 40, SKIN, 4)}{limb(70, 56, 88, 40, SKIN, 4)}
<path d="M54 52 L74 52 L76 78 L52 78Z" fill="#FF3D7F" {s()}/>
<path d="M52 78 L54 86 M57 78 L58 86 M62 78 L62 87 M66 78 L66 87 M71 78 L70 86 M76 78 L74 86" {ln("#FFD43B", 2.4)}/>
<path d="M54 60 L74 60" stroke="#FFD43B" stroke-width="2.4"/>
{head(64, 38, 11, "#5A3420")}
<g fill="#E6EEF7" {s('stroke-width="1.2"')}>
<rect x="34" y="12" width="5" height="3" transform="rotate(30 36 13)"/><rect x="88" y="16" width="5" height="3" transform="rotate(-25 90 17)"/>
<rect x="50" y="8" width="4" height="3" transform="rotate(60 52 9)"/><rect x="74" y="6" width="5" height="3" transform="rotate(10 76 7)"/>
<rect x="100" y="34" width="4" height="3" transform="rotate(45 102 35)"/><rect x="24" y="30" width="4" height="3" transform="rotate(-40 26 31)"/>
</g>
'''))

# 4 «Артель» (балет и брейк-данс от 3 до 15 лет): дуэт балерины на пуанте и брейкера в стойке на руке
I["artel-cherkizovskaya"] = ("дуэт: девочка-балерина в мятной пачке и мальчик-брейкер в красной бандане",
    "она стоит на пуанте с поднятыми руками, а он рядом замер вверх ногами в стойке на одной руке на светлом деревянном полу клуба", bg("#FFF3C4", "#F0B84A", f'''
<path d="M0 108 H128 V128 H0Z" fill="#E2B57A" {s()}/>
<path d="M0 116 H128" stroke="#C8965A" stroke-width="2"/>
{limb(40, 84, 40, 106, SKIN, 4)}<path d="M37 106 L43 106 L40 111Z" fill="#FFB3CF" {s('stroke-width="1.8"')}/>
{limb(42, 84, 52, 98, SKIN, 4)}
<path d="M33 62 L47 62 L46 82 L34 82Z" fill="#7FDCC0" {s()}/>
<ellipse cx="40" cy="82" rx="18" ry="5" fill="#B5F0DE" {s()}/>
{limb(36, 64, 28, 38, SKIN, 3.5)}{limb(44, 64, 50, 38, SKIN, 3.5)}
{head(40, 50, 9, "#3B2A20")}
<circle cx="40" cy="38" r="4" fill="#3B2A20" {s('stroke-width="2"')}/>
{limb(88, 106, 88, 88, SKIN, 4.5)}
<path d="M80 108 H96" {ln(O, 5)}/>
<rect x="80" y="54" width="18" height="28" rx="4" fill="#3E8DE0" {s()}/>
{limb(84, 54, 74, 32, "#2D3A55", 6)}{limb(94, 54, 108, 36, "#2D3A55", 6)}
<path d="M70 30 h8 v-4 h-8Z M104 34 l8 -3 1 4 -8 3Z" fill="#fff" {s('stroke-width="2"')}/>
<circle cx="89" cy="92" r="10" fill="{SKIN}" {s()}/>
<path d="M79 94 Q89 104 99 94 L99 98 Q89 106 79 98Z" fill="#F03E3E" {s('stroke-width="2"')}/>
<path d="M85 89 Q86.5 91 88 89 M90 89 Q91.5 91 93 89" fill="none" {ln(O, 1.8)}/>
<path d="M86 84 Q89 82 92 84" fill="none" {ln(O, 1.8)}/>
{sparkle(64, 24, 4)}
'''))

# 5 BabyDance (танцы для малышей 2,5–7 лет): кудрявый малыш кружится с платочками
I["babydance-sevilsky"] = ("кудрявый малыш в голубом комбинезончике",
    "кружится на месте, подбросив над головой два разноцветных шифоновых платочка — жёлтый и розовый", bg("#E3FFF4", "#7BD8B5", f'''
<path d="M14 26 Q30 8 46 22 Q40 36 26 38 Q16 36 14 26Z" fill="#FFE066" {s()} opacity=".95"/>
<path d="M82 22 Q100 6 114 24 Q108 38 96 38 Q84 34 82 22Z" fill="#FF9EC4" {s()} opacity=".95"/>
{limb(54, 70, 38, 38, SKIN, 5)}{limb(74, 70, 92, 38, SKIN, 5)}
<path d="M48 72 Q64 64 80 72 L84 104 L44 104Z" fill="#74C0FC" {s()}/>
<path d="M56 72 V84 M72 72 V84" stroke="#4A9BE0" stroke-width="2.4"/>
<circle cx="58" cy="86" r="2" fill="#fff" {s('stroke-width="1.2"')}/><circle cx="70" cy="86" r="2" fill="#fff" {s('stroke-width="1.2"')}/>
{limb(54, 104, 50, 118, SKIN, 5)}{limb(74, 104, 78, 118, SKIN, 5)}
<circle cx="64" cy="54" r="15" fill="{SKIN}" {s()}/>
<g fill="#C77B3A" {s('stroke-width="2"')}><circle cx="52" cy="42" r="5"/><circle cx="60" cy="38" r="5"/><circle cx="68" cy="38" r="5"/><circle cx="76" cy="42" r="5"/></g>
{eye(58, 55, 0.55)}{eye(70, 55, 0.55)}<ellipse cx="64" cy="62" rx="3.5" ry="3" fill="#E8590C" {s('stroke-width="1.6"')}/>
{blush(54, 60)}{blush(74, 60)}
<path d="M34 96 Q28 90 34 84 M94 96 Q100 90 94 84" fill="none" {ln("#2F9E79", 3)}/>
'''))

# 6 Lil Ballerine (балет «балет и сказка» с 2 лет): из раскрытой книги сказок выпрыгивает балерина
I["lil-ballerine-prokshino"] = ("раскрытая книга сказок с мордашкой на корешке",
    "из её страниц, как со сцены, выпрыгивает маленькая балерина в голубой пачке и короне", bg("#FFE9DC", "#F4A37E", f'''
<path d="M14 92 Q38 84 64 94 Q90 84 114 92 L114 116 Q90 108 64 118 Q38 108 14 116Z" fill="#8E5BD8" {s()}/>
<path d="M18 88 Q40 80 64 90 V112 Q40 102 18 108Z" fill="#FFFDF5" {s()}/>
<path d="M110 88 Q88 80 64 90 V112 Q88 102 110 108Z" fill="#FFFDF5" {s()}/>
<path d="M26 92 Q40 88 54 94 M26 98 Q40 94 54 100 M74 94 Q88 88 102 92 M74 100 Q88 94 102 98" stroke="#D9CBB5" stroke-width="2" fill="none"/>
{eye(58, 108, 0.45)}{eye(70, 108, 0.45)}<path d="M61 113 Q64 115 67 113" fill="none" {ln(O, 1.6)}/>
{limb(62, 66, 54, 84, SKIN, 3.5)}{limb(66, 66, 82, 74, SKIN, 3.5)}
<path d="M51 84 L57 84 L54 89Z" fill="#74C0FC" {s('stroke-width="1.6"')}/>
<path d="M57 46 L71 46 L70 64 L58 64Z" fill="#74C0FC" {s()}/>
<ellipse cx="64" cy="64" rx="17" ry="5" fill="#BDE3FF" {s()}/>
{limb(59, 50, 46, 34, SKIN, 3)}{limb(69, 50, 82, 34, SKIN, 3)}
{head(64, 34, 8, "#E8A33A", 0.5)}
<path d="M58 26 L59 20 L62 24 L64 18 L66 24 L69 20 L70 26Z" fill="#FFD43B" {s('stroke-width="1.6"')}/>
{sparkle(30, 60, 4)}{sparkle(100, 52, 4)}{sparkle(40, 30, 3)}{sparkle(94, 22, 3)}
'''))

# 7 «Мьюзик Стар» (вокал, гитара, барабаны, саксофон): ударная установка со звездой на бочке
I["music-star-moskovsky"] = ("детская ударная установка: большая бочка с жёлтой звездой и мордашкой",
    "палочки сами выстукивают ритм по малому барабану, а с тарелки разлетаются звёздочки на тёмно-синем фоне", bg("#2B3A7A", "#121A3F", f'''
<path d="M96 40 L96 104" {ln(O, 5)}/><path d="M96 40 L96 104" {ln("#C9D1DA", 2.5)}/>
<ellipse cx="96" cy="38" rx="20" ry="5" fill="#FFD43B" {s()}/>
<circle cx="64" cy="82" r="30" fill="#E03131" {s()}/>
<circle cx="64" cy="82" r="24" fill="#FFF4E0" {s()}/>
<path d="M64 62 L69 74 L82 75 L72 83 L75 96 L64 89 L53 96 L56 83 L46 75 L59 74Z" fill="#FFD43B" {s('stroke-width="2"')}/>
{eye(60, 80, 0.45)}{eye(68, 80, 0.45)}<path d="M61 85 Q64 87 67 85" fill="none" {ln(O, 1.6)}/>
<path d="M18 62 H44 V76 H18Z" fill="#E03131" {s()}/><ellipse cx="31" cy="62" rx="13" ry="4" fill="#FFF4E0" {s()}/>
<path d="M22 76 L18 104 M40 76 L44 104" {ln(O, 3)}/>
<path d="M22 44 L34 60 M44 40 L36 59" {ln(O, 6)}/><path d="M22 44 L34 60 M44 40 L36 59" {ln("#F2C48D", 3)}/>
<path d="M30 52 Q24 46 28 40" fill="none" {ln("#FFE066", 2)}/>
{sparkle(84, 22, 4, "#FFE066")}{sparkle(110, 26, 3.5, "#FFE066")}{sparkle(104, 12, 3, "#fff")}{sparkle(20, 22, 3, "#fff")}
'''))

# 8 Школа фортепиано Юлии Туйбовой: белая клавиша выпрыгнула из клавиатуры и пританцовывает
I["tuybova-piano-vorontsovskaya"] = ("белая клавиша фортепиано-девочка с голубым бантиком",
    "выпрыгнула из ряда клавиш и пританцовывает над клавиатурой, а соседние чёрные клавиши хлопают ей", bg("#E4F1FF", "#8DB6E8", f'''
<path d="M0 88 H128 V128 H0Z" fill="#2B2B35" {s()}/>
<g fill="#FFFFFF" {s('stroke-width="2"')}>
<rect x="4" y="92" width="16" height="34" rx="2"/><rect x="22" y="92" width="16" height="34" rx="2"/><rect x="40" y="92" width="16" height="34" rx="2"/>
<rect x="74" y="92" width="16" height="34" rx="2"/><rect x="92" y="92" width="16" height="34" rx="2"/><rect x="110" y="92" width="16" height="34" rx="2"/>
</g>
<path d="M57 94 H71 V126 H57Z" fill="#3A4A66" opacity=".35"/>
<g fill="#26232E" {s('stroke-width="2"')}><rect x="15" y="90" width="10" height="20" rx="2"/><rect x="33" y="90" width="10" height="20" rx="2"/>
<rect x="85" y="90" width="10" height="20" rx="2"/><rect x="103" y="90" width="10" height="20" rx="2"/></g>
<path d="M28 84 L30 88 M38 84 L36 88 M90 84 L92 88 M100 84 L98 88" {ln("#FFE066", 2.4)}/>
{limb(58, 76, 52, 86, "#fff", 3.5)}{limb(70, 76, 78, 84, "#fff", 3.5)}
<rect x="52" y="22" width="24" height="56" rx="4" fill="#FFFFFF" {s()} transform="rotate(8 64 50)"/>
{limb(54, 42, 40, 30, "#fff", 3.5)}{limb(74, 46, 88, 34, "#fff", 3.5)}
<path d="M58 22 L52 14 L62 18Z M70 22 L78 14 L68 18Z" fill="#74C0FC" {s('stroke-width="1.8"')}/>
<circle cx="65" cy="20" r="3" fill="#4A9BE0" {s('stroke-width="1.6"')}/>
{face(64, 44, 7, 0.55)}
{note(104, 34, 0.9)}{note(22, 48, 0.8)}
'''))

# 9 «Имена Продакшн» (актёрское мастерство 3–18 лет): девочка репетирует роль деда у зеркала гримёрки
I["imena-production-marksistskaya"] = ("девочка в накладной седой бороде и соломенной шляпе",
    "репетирует роль деда перед зеркалом гримёрки в рамке из круглых лампочек, опираясь на палочку", bg("#FFE3C2", "#E8893A", f'''
<rect x="62" y="14" width="56" height="72" rx="4" fill="#FFFFFF" {s()}/>
<rect x="70" y="22" width="40" height="56" fill="#BFE3F2" {s('stroke-width="2"')}/>
<g fill="#FFE066" {s('stroke-width="1.6"')}><circle cx="66" cy="24" r="3.5"/><circle cx="66" cy="44" r="3.5"/><circle cx="66" cy="64" r="3.5"/>
<circle cx="114" cy="24" r="3.5"/><circle cx="114" cy="44" r="3.5"/><circle cx="114" cy="64" r="3.5"/><circle cx="90" cy="18" r="3.5"/></g>
<path d="M80 70 Q90 60 100 70" fill="#E9F6FB" opacity=".9"/>
<path d="M54 100 L62 122" {ln(O, 5)}/><path d="M54 100 L62 122" {ln("#8B5A2B", 2.5)}/>
<path d="M22 84 Q36 76 50 84 L54 122 L18 122Z" fill="#7048C8" {s()}/>
{limb(46, 88, 54, 100, SKIN, 4)}
<circle cx="36" cy="62" r="13" fill="{SKIN}" {s()}/>
<path d="M24 64 Q24 88 36 92 Q48 88 48 64 Q42 72 36 70 Q30 72 24 64Z" fill="#F1F3F5" {s()}/>
<path d="M30 70 Q36 66 42 70" fill="none" {ln("#CED4DA", 2)}/>
<path d="M30 59 Q31.5 57 33 59 M39 59 Q40.5 57 42 59" fill="none" {ln(O, 1.8)}/>
<ellipse cx="36" cy="50" rx="22" ry="5" fill="#F2C94C" {s()}/>
<path d="M24 50 Q24 34 36 34 Q48 34 48 50Z" fill="#F2C94C" {s()}/>
<path d="M25 46 H47" stroke="#C0392B" stroke-width="3"/>
'''))

# 10 «Танцевальная лаборатория» (бальные танцы с 3 лет): колба в оборчатой юбке танцует ча-ча-ча
I["dance-lab-vernadskogo"] = ("стеклянная лабораторная колба с мордашкой в пышной оборчатой оранжевой юбке",
    "танцует ча-ча-ча на белом лабораторном столе, а из горлышка вылетают розовые пузырьки", bg("#DFFBFF", "#5CC6D9", f'''
<path d="M0 100 H128 V128 H0Z" fill="#F8F9FA" {s()}/>
<path d="M0 108 H128" stroke="#DEE2E6" stroke-width="2"/>
<path d="M56 18 H72 V42 L94 82 Q96 90 88 90 H40 Q32 90 34 82 L56 42Z" fill="#E9FBFF" {s()} opacity=".95"/>
<path d="M44 68 H84 L92 84 Q92 88 88 88 H40 Q36 88 36 84Z" fill="#B197FC" opacity=".8"/>
<path d="M54 16 H74" {ln(O, 5)}/>
<path d="M28 82 Q40 72 52 82 Q64 72 76 82 Q88 72 100 82 L104 92 Q90 100 64 96 Q38 100 24 92Z" fill="#FF922B" {s()}/>
<path d="M26 90 Q40 84 52 90 Q64 84 76 90 Q88 84 102 90" fill="none" stroke="#FFC078" stroke-width="2.2"/>
{limb(52, 96, 46, 112, "#E9FBFF", 3.5)}{limb(76, 96, 86, 108, "#E9FBFF", 3.5)}
{limb(48, 56, 30, 46, "#E9FBFF", 3.5)}{limb(80, 56, 98, 64, "#E9FBFF", 3.5)}
{face(64, 56, 7, 0.55)}
<g fill="#FF8FB5" {s('stroke-width="1.6"')}><circle cx="62" cy="8" r="3.5"/><circle cx="72" cy="4" r="2.5"/><circle cx="80" cy="12" r="3"/></g>
<text x="90" y="36" font-family="Arial" font-weight="bold" font-size="10" fill="#1C7C8C">ча-ча</text>
'''))

# 11 Testa Dance Show (брейк, хип-хоп, афро): красный кроссовок-хайтоп в брейк-фризе у стены с граффити
I["testa-dance-domodedovo"] = ("красный кроссовок-хайтоп с мордашкой и развязанными белыми шнурками",
    "застыл в брейк-фризе на одном носке на асфальте перед бетонной стеной, разрисованной разноцветным граффити", bg("#C9CED6", "#7C8594", f'''
<path d="M0 0 H128 V104 H0Z" fill="#B4BAC4"/>
<path d="M8 34 Q22 16 38 32" fill="none" {ln("#7048E8", 7)}/>
<path d="M92 22 Q106 8 120 26" fill="none" {ln("#20C997", 7)}/>
<path d="M98 70 l8 -10 l6 12 l8 -8" fill="none" {ln("#F06595", 5)}/>
<path d="M0 104 H128 V128 H0Z" fill="#5C636E" {s()}/>
<g transform="rotate(-38 64 70)">
<path d="M28 70 L54 70 L56 36 L82 36 L86 70 Q104 72 106 86 L106 90 H28Z" fill="#F03E3E" {s()}/>
<path d="M28 88 H106 V98 Q66 102 28 98Z" fill="#FFFFFF" {s()}/>
<path d="M58 44 L80 44 M58 52 L82 52 M58 60 L84 60" {ln("#fff", 2.6)}/>
<circle cx="70" cy="80" r="7" fill="#fff" {s('stroke-width="1.8"')}/><path d="M66 80 L70 76 L74 80" fill="none" {ln("#F03E3E", 2)}/>
{eye(88, 78, 0.55)}{eye(97, 78, 0.55)}<path d="M89 84 Q92.5 87 96 84" fill="none" {ln(O, 1.8)}/>
</g>
<path d="M50 50 Q34 46 30 58 M54 44 Q46 30 34 34" fill="none" {ln("#fff", 2.6)}/>
<path d="M40 112 L46 106 M88 112 L82 106" {ln("#FFE066", 3)}/>
'''))

# 12 ValeriBallet (балет 7–15 лет): девочка у станка в батмане перед зеркалом
I["valeriballet-domodedovo"] = ("девочка-балерина в бордовом купальнике и белой шифоновой юбочке",
    "держится за деревянный станок у зеркальной стены и высоко поднимает ногу в батмане вперёд", bg("#FCE8EC", "#D98A9C", f'''
<rect x="78" y="8" width="46" height="96" fill="#E7F5FB" {s()}/>
<path d="M86 14 L96 30 M100 14 L114 36" stroke="#fff" stroke-width="3"/>
<path d="M0 104 H128 V128 H0Z" fill="#C59A6D" {s()}/>
<path d="M8 66 H120" {ln(O, 7)}/><path d="M8 66 H120" {ln("#D9A066", 3.5)}/>
<path d="M14 66 V104 M114 66 V104" {ln(O, 3)}/>
{limb(52, 84, 50, 106, SKIN, 4.5)}<path d="M46 106 H54 L52 110Z" fill="#FFD8E0" {s('stroke-width="1.8"')}/>
{limb(56, 82, 88, 52, SKIN, 4.5)}<path d="M88 46 L94 50 L88 54Z" fill="#FFD8E0" {s('stroke-width="1.8"')}/>
<path d="M46 52 L62 52 L60 80 L48 80Z" fill="#A61E4D" {s()}/>
<path d="M40 78 Q54 72 68 78 L70 88 Q54 84 38 88Z" fill="#FFFFFF" {s()} opacity=".95"/>
{limb(48, 56, 30, 66, SKIN, 3.5)}{limb(60, 56, 70, 30, SKIN, 3.5)}
{head(54, 40, 10, "#3B2A20")}
<circle cx="54" cy="28" r="4.5" fill="#3B2A20" {s('stroke-width="2"')}/>
{sparkle(24, 24, 4)}
'''))

# 13 «Подвал» (брейк и танцы в цокольном зале): мальчик крутится на спине под кирпичным сводом
I["podval-dance-shchyolkovo"] = ("мальчик в оранжевой толстовке и синей шапке-бини",
    "крутится на спине на расплющенной картонке под кирпичным сводом подвала, а над ним качается лампочка на проводе", bg("#5A3A2E", "#2C1A14", f'''
<g fill="#8C4A32" stroke="#4A2418" stroke-width="2">
<rect x="0" y="10" width="26" height="12"/><rect x="26" y="10" width="26" height="12"/><rect x="76" y="10" width="26" height="12"/><rect x="102" y="10" width="26" height="12"/>
<rect x="-13" y="22" width="26" height="12"/><rect x="13" y="22" width="26" height="12"/><rect x="89" y="22" width="26" height="12"/><rect x="115" y="22" width="26" height="12"/>
<rect x="0" y="34" width="26" height="12"/><rect x="102" y="34" width="26" height="12"/>
</g>
<path d="M64 0 V24" {ln(O, 2.4)}/>
<path d="M58 24 H70 L68 30 H60Z" fill="#555" {s('stroke-width="1.8"')}/>
<circle cx="64" cy="36" r="7" fill="#FFE066" {s('stroke-width="2"')}/>
<path d="M64 44 L36 100 H92Z" fill="#FFE066" opacity=".18"/>
<path d="M18 106 L110 100 L112 114 L20 120Z" fill="#C9A26B" {s()}/>
<path d="M50 90 Q64 80 80 88 L78 104 L50 104Z" fill="#FF8C2B" {s()}/>
{limb(78, 92, 100, 64, "#2D3A55", 6)}{limb(74, 90, 86, 58, "#2D3A55", 6)}
<path d="M96 58 h10 v6 h-10Z M82 52 h10 v6 h-10Z" fill="#fff" {s('stroke-width="2"')}/>
{limb(52, 92, 40, 80, "#FF8C2B", 5)}{limb(54, 100, 70, 112, "#FF8C2B", 5)}
<circle cx="40" cy="98" r="11" fill="{SKIN}" {s()}/>
<path d="M30 94 Q34 82 46 86 L50 92 Q40 88 30 94Z" fill="#3B5BDB" {s('stroke-width="2"')}/>
<path d="M35 100 Q36.5 102 38 100 M42 100 Q43.5 102 45 100" fill="none" {ln(O, 1.8)}/>
<path d="M36 106 Q40 108 44 106" fill="none" {ln(O, 1.6)}/>
<path d="M22 84 Q16 92 22 100 M110 82 Q118 88 114 96" fill="none" {ln("#FFE066", 2.4)}/>
'''))

# 14 «Катри» (танцы для детей 4–17 лет в фитнес-клубе): светящаяся плитка танцпола под прыжком девочки
I["katri-dance-shchyolkovo"] = ("светящаяся квадратная плитка танцпола с мордашкой",
    "загорается розовым под приземлением девочки с двумя пучками, которая прыгает по разноцветному полу, как по классикам", bg("#2E1F4F", "#140C2A", f'''
<g transform="translate(0 4)">
<path d="M4 92 L40 80 L64 90 L28 104Z" fill="#4DABF7" {s()}/>
<path d="M40 80 L76 70 L100 80 L64 90Z" fill="#9775FA" {s()}/>
<path d="M28 104 L64 90 L88 102 L52 118Z" fill="#FF6BB5" {s()}/>
<path d="M64 90 L100 80 L124 92 L88 102Z" fill="#51CF66" {s()}/>
<path d="M52 118 L88 102 L112 116 L76 132Z" fill="#FAB005" {s()}/>
{eye(52, 102, 0.5)}{eye(62, 104, 0.5)}<path d="M54 109 Q58 111 62 109" fill="none" {ln(O, 1.8)}/>
<path d="M58 84 L56 76 M74 88 L80 82 M40 98 L32 94" {ln("#FFC2E2", 2.6)}/>
</g>
{limb(58, 64, 58, 82, SKIN, 4.5)}{limb(68, 62, 80, 72, SKIN, 4.5)}
<path d="M54 82 H62 M78 74 L84 70" {ln(O, 5)}/>
<path d="M54 40 L72 40 L72 62 L54 64Z" fill="#20C997" {s()}/>
{limb(56, 44, 40, 28, SKIN, 3.5)}{limb(70, 44, 86, 30, SKIN, 3.5)}
{head(63, 28, 9, "#2B1D16", 0.5)}
<circle cx="55" cy="18" r="4.5" fill="#2B1D16" {s('stroke-width="2"')}/><circle cx="71" cy="18" r="4.5" fill="#2B1D16" {s('stroke-width="2"')}/>
{sparkle(104, 30, 4)}{sparkle(22, 44, 3.5)}
'''))

# 15 «Дети в Балете» (балет с 2 до 12 лет): плюшевый мишка в пачке делает реверанс перед малышкой
I["deti-v-balete-starovolynskaya"] = ("коричневый плюшевый мишка в розовой балетной пачке",
    "делает реверанс перед маленькой девочкой в белом купальнике на мягком сиреневом коврике, а она повторяет за ним", bg("#FFF0F6", "#F3A6C8", f'''
<path d="M0 100 H128 V128 H0Z" fill="#C5B3F0" {s()}/>
<circle cx="40" cy="72" r="20" fill="#B5793F" {s()}/>
<circle cx="24" cy="48" r="7" fill="#B5793F" {s()}/><circle cx="52" cy="46" r="7" fill="#B5793F" {s()}/>
<circle cx="38" cy="54" r="15" fill="#C88A4C" {s()}/>
<ellipse cx="38" cy="59" rx="6" ry="4.5" fill="#F2D3A8" {s('stroke-width="1.6"')}/>
<circle cx="38" cy="57" r="2" fill="{O}"/>
{eye(32, 51, 0.5)}{eye(44, 51, 0.5)}
<ellipse cx="40" cy="84" rx="26" ry="8" fill="#FF8FB5" {s()}/>
<path d="M16 84 Q40 94 64 84" fill="none" stroke="#FFC9DE" stroke-width="2"/>
<ellipse cx="28" cy="100" rx="7" ry="5" fill="#B5793F" {s()}/><ellipse cx="52" cy="102" rx="7" ry="5" fill="#B5793F" {s()}/>
{limb(24, 70, 14, 80, "#B5793F", 6)}{limb(56, 70, 66, 80, "#B5793F", 6)}
{limb(90, 86, 84, 104, SKIN, 3.5)}{limb(94, 86, 102, 102, SKIN, 3.5)}
<path d="M86 64 L100 64 L98 86 L88 86Z" fill="#FFFFFF" {s()}/>
<ellipse cx="93" cy="86" rx="13" ry="4" fill="#F8F0FF" {s()}/>
{limb(88, 68, 78, 82, SKIN, 3)}{limb(98, 68, 108, 82, SKIN, 3)}
{head(93, 52, 9, "#E8A33A", 0.5)}
{sparkle(70, 26, 4)}{sparkle(108, 22, 3)}
'''))

# 16 Гитарная школа № 1 (Чертаново, гитара для детей 8–16 лет): рыжий мальчик на высоком табурете с огромной гитарой
I["guitar-school-1-chertanovskaya"] = ("рыжий мальчик в больших зелёных наушниках",
    "сидит на высоком барном табурете и играет на огромной для него синей акустической гитаре, болтая ногами", bg("#FFF8E1", "#F7C948", f'''
<path d="M50 90 H82" {ln(O, 6)}/><path d="M50 90 H82" {ln("#8B5A2B", 3)}/>
<path d="M54 92 L48 124 M78 92 L84 124 M52 110 H80" {ln(O, 3.4)}/>
{limb(58, 88, 48, 108, "#3B5BDB", 5)}{limb(70, 88, 66, 110, "#3B5BDB", 5)}
<path d="M42 110 h8 M62 112 h8" {ln(O, 6)}/>
<path d="M54 56 L74 56 L76 88 L52 88Z" fill="#E03131" {s()}/>
<g transform="rotate(-28 64 78)">
<path d="M64 78 m-22 0 a14 12 0 1 0 22 10 a10 9 0 1 0 22 -10 a10 9 0 1 0 -22 -10 a14 12 0 1 0 -22 10Z" fill="#4DABF7" {s()}/>
<circle cx="64" cy="78" r="5" fill="#1C3D6E" {s('stroke-width="1.6"')}/>
<path d="M76 78 H118" {ln(O, 7)}/><path d="M76 78 H118" {ln("#8B5A2B", 4)}/>
<rect x="114" y="73" width="10" height="10" rx="2" fill="#8B5A2B" {s('stroke-width="2"')}/>
</g>
{limb(56, 62, 52, 80, SKIN, 3.5)}{limb(72, 62, 82, 66, SKIN, 3.5)}
{head(64, 40, 12, "#E8590C")}
<path d="M50 40 Q50 22 64 22 Q78 22 78 40" fill="none" {ln(O, 5)}/><path d="M50 40 Q50 22 64 22 Q78 22 78 40" fill="none" {ln("#40C057", 2.5)}/>
<rect x="46" y="36" width="7" height="11" rx="3" fill="#40C057" {s('stroke-width="2"')}/><rect x="75" y="36" width="7" height="11" rx="3" fill="#40C057" {s('stroke-width="2"')}/>
{note(22, 40, 0.9)}{note(104, 24, 0.8)}
'''))

if __name__ == "__main__":
    if "--subjects" in sys.argv:
        for k, (h, sc, _) in I.items():
            print(f"{k} — герой: {h} | сцена: {sc}")
        sys.exit()
    for k, (_, _, svg) in I.items():
        open(os.path.join(ROOT, "icons-src", k + ".svg"), "w").write(svg)
    print(len(I))
