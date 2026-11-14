"""Иконки робота creative, 14.11 (запуск 1114a). Каждая придумана и нарисована отдельно: свой герой, своя сцена,
своя компоновка и свой фон (правило абсолютной уникальности). python3 tools/icons_creative_1114a.py [--subjects] [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_creative_1112k import bg, ln, limb, note, head, SKIN

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
I = {}

# ---------- Art Kids Community: актёрская школа (6 филиалов — 6 разных идей театра) ----------

# Народного Ополчения: венецианская маска на палочке выглядывает из-за занавеса
I["artkids-narodnogo-opolcheniya"] = ("бирюзовая венецианская маска на тонкой палочке с золотыми узорами и двумя перьями",
    "подмигивает, выглянув из щели между тяжёлыми вишнёвыми половинками занавеса, а сверху падает алый лепесток розы",
    bg("#FFF0F6", "#C2255C", f'''
<path d="M-4 -4 H58 Q50 40 56 132 H-4Z" fill="#A61E4D" {s()}/>
<path d="M132 -4 H70 Q78 40 72 132 H132Z" fill="#A61E4D" {s()}/>
<path d="M14 0 Q10 60 16 128 M34 0 Q30 60 38 128 M114 0 Q118 60 112 128 M94 0 Q98 60 90 128" fill="none" {ln("#7A1237", 3)}/>
<path d="M76 40 L104 14" {ln(O, 8)}/><path d="M76 40 L104 14" {ln("#E8C07A", 4.5)}/>
<path d="M104 14 Q112 2 122 6 Q112 8 108 18Z" fill="#FFD43B" {s('stroke-width="2"')}/>
<path d="M100 18 Q100 4 112 -2 Q106 10 106 20Z" fill="#74C0FC" {s('stroke-width="2"')}/>
<path d="M30 56 Q30 40 50 42 Q64 48 78 42 Q98 40 98 56 Q98 76 80 76 Q70 76 64 66 Q58 76 48 76 Q30 76 30 56Z" fill="#12B886" {s()}/>
<path d="M36 50 Q44 46 50 50 M78 50 Q84 46 92 50" fill="none" {ln("#FCC419", 2.4)}/>
<path d="M40 58 Q48 52 56 58 Q48 64 40 58Z" fill="#fff" {s('stroke-width="2"')}/>{eye(48, 58, 0.55)}
<path d="M72 60 Q80 56 88 60" fill="none" {s('stroke-width="2.6"')}/>
<circle cx="64" cy="70" r="3" fill="#FCC419" {s('stroke-width="1.6"')}/>
<path d="M56 90 Q64 96 72 90" fill="none" {ln("#FFDEEB", 3)}/>
<path d="M60 104 q8 -10 14 0 q-6 8 -14 0Z" fill="#F03E3E" {s('stroke-width="2"')}/>
'''))

# Лазоревый: картонная луна-декорация спускается на верёвках на сцену
I["artkids-lazorevy-7"] = ("жёлтый картонный полумесяц-декорация со спящей мордашкой и ночным колпаком",
    "спускается на двух верёвочках на деревянную сцену, а вокруг на ниточках качаются три картонные звёздочки",
    bg("#364FC7", "#1B1F5E", f'''
<path d="M44 -4 V30 M88 -4 V42" {ln("#CED4DA", 2)}/>
<path d="M60 20 Q30 34 34 66 Q40 96 74 98 Q50 84 50 58 Q50 34 60 20Z" fill="#FFD43B" {s()}/>
<path d="M60 20 Q72 6 88 10 Q80 16 76 26" fill="#E03131" {s('stroke-width="2.4"')}/><circle cx="90" cy="10" r="4" fill="#fff" {s('stroke-width="2"')}/>
<path d="M40 56 q4 3 8 0 M42 72 q4 3 8 0" fill="none" {s('stroke-width="2.2"')}/>
<ellipse cx="44" cy="80" rx="4" ry="2.4" fill="#FF8787" opacity=".8"/>
<path d="M50 88 Q56 92 60 88" fill="none" {s('stroke-width="2"')}/>
<path d="M98 -4 V58 M110 -4 V32 M22 -4 V24" {ln("#CED4DA", 1.6)}/>
<path d="M98 58 l3 7 7 1 -5 5 1 7 -6 -4 -6 4 1 -7 -5 -5 7 -1Z" fill="#FFE066" {s('stroke-width="2"')}/>
<path d="M110 32 l2 5 5 .5 -4 3.5 1 5 -4 -3 -4 3 1 -5 -4 -3.5 5 -.5Z" fill="#FFE066" {s('stroke-width="1.8"')}/>
<path d="M22 24 l2 5 5 .5 -4 3.5 1 5 -4 -3 -4 3 1 -5 -4 -3.5 5 -.5Z" fill="#FFE066" {s('stroke-width="1.8"')}/>
<path d="M76 102 h4 M84 92 h4" {ln("#FFE066", 2)}/>
<rect x="-4" y="104" width="136" height="28" fill="#B07A4A" {s()}/>
<path d="M-4 112 H132 M30 104 V132 M70 104 V132 M106 104 V132" {ln("#8A5A33", 2)}/>
<text x="74" y="78" font-family="Arial" font-weight="bold" font-size="14" fill="#FFE066">z</text>
'''))

# Можайское шоссе: маленький актёр в плаще кланяется, к ногам летят розы
I["artkids-mozhayskoe-38"] = ("мальчик-актёр в фиолетовом бархатном плаще и картонной короне",
    "низко кланяется на краю сцены, прижав руку к груди, а к его ногам из зала летят три красные розы",
    bg("#FFF4E6", "#F59F00", f'''
<rect x="-4" y="100" width="136" height="32" fill="#5C3D2E" {s()}/>
<path d="M-4 108 H132" {ln("#8D6E63", 2)}/>
<path d="M52 98 L40 60 Q56 48 76 54 L88 98Z" fill="#7048E8" {s()}/>
<path d="M56 98 V80 M72 98 V80" {ln(O, 8)}/><path d="M56 98 V80 M72 98 V80" {ln("#343A40", 5)}/>
<path d="M50 100 h10 M68 100 h10" {ln(O, 6)}/>
<path d="M62 62 Q74 72 68 84" fill="none" {ln(O, 8)}/><path d="M62 62 Q74 72 68 84" fill="none" {ln(SKIN, 5)}/>
<g transform="rotate(38 52 50)">{head(52, 50, 12, "#8B5A2B", 0.55)}
<path d="M40 38 L42 26 L47 33 L52 24 L57 33 L62 26 L64 38Z" fill="#FFD43B" {s('stroke-width="2.4"')}/></g>
<path d="M44 58 Q36 62 34 72" fill="none" {ln(O, 8)}/><path d="M44 58 Q36 62 34 72" fill="none" {ln("#7048E8", 5)}/>
<g>
<path d="M98 54 L112 40" {ln("#2F9E44", 3)}/><circle cx="96" cy="56" r="6" fill="#E03131" {s('stroke-width="2"')}/>
<path d="M108 80 L122 72" {ln("#2F9E44", 3)}/><circle cx="104" cy="82" r="6" fill="#E03131" {s('stroke-width="2"')}/>
<path d="M88 30 L100 18" {ln("#2F9E44", 3)}/><circle cx="86" cy="32" r="6" fill="#E03131" {s('stroke-width="2"')}/>
</g>
{sparkle(20, 30, 5)}{sparkle(28, 86, 4)}
'''))

# Шаболовка: сценарий со своей ролью, выделенной маркером
I["artkids-shabolovka-56"] = ("раскрытый сценарий с жёлтой лентой-закладкой и мордашкой на обложке",
    "громко читает свою роль, выделенную на странице жёлтым маркером, а над ним облачко-реплика с восклицательным знаком",
    bg("#E6FCF5", "#20C997", f'''
<path d="M18 60 L60 52 V112 L18 118Z" fill="#fff" {s()}/>
<path d="M110 60 L68 52 V112 L110 118Z" fill="#fff" {s()}/>
<path d="M60 52 Q64 48 68 52 V112 Q64 116 60 112Z" fill="#CED4DA" {s('stroke-width="2"')}/>
<path d="M24 70 L54 65 M24 80 L54 75 M24 90 L46 87 M24 100 L54 95" {ln("#ADB5BD", 2.4)}/>
<path d="M74 66 L104 71" {ln("#FFE066", 7)}/>
<path d="M74 66 L104 71 M74 78 L104 83 M74 90 L96 93 M74 102 L104 107" {ln("#868E96", 2.4)}/>
<path d="M66 112 V126 l-4 -4 -4 4 V112" fill="#F08C00" {s('stroke-width="2"')}/>
{eye(36, 108, 0.6)}{eye(48, 106, 0.6)}<path d="M38 114 Q43 118 48 113" fill="none" {s('stroke-width="2"')}/>
<path d="M58 10 H112 Q120 10 120 18 V36 Q120 44 112 44 H84 L74 54 L76 44 H58 Q50 44 50 36 V18 Q50 10 58 10Z" fill="#fff" {s()}/>
<path d="M85 17 V31" {ln("#E8590C", 6)}/><circle cx="85" cy="38" r="3" fill="#E8590C"/>
'''))

# Щусева (у школы есть актёрское агентство): звёздочка в тёмных очках идёт по красной дорожке
I["artkids-shchuseva-5"] = ("золотая звёздочка в круглых тёмных очках",
    "шагает по красной ковровой дорожке к киноплёнке, свернувшейся аркой, и машет лапкой вспышкам фотоаппаратов",
    bg("#F8F0FC", "#862E9C", f'''
<path d="M40 132 L56 70 H72 L88 132Z" fill="#E03131" {s()}/>
<path d="M50 132 L60 72 M78 132 L68 72" {ln("#C92A2A", 2)}/>
<path d="M14 92 Q14 20 64 18 Q114 20 114 92" fill="none" {ln(O, 18)}/><path d="M14 92 Q14 20 64 18 Q114 20 114 92" fill="none" {ln("#343A40", 14)}/>
<path d="M14 80 Q14 24 64 22 Q114 24 114 80" fill="none" stroke="#F8F9FA" stroke-width="5" stroke-dasharray="5 6"/>
<path d="M64 46 l8 15 17 2 -12 12 3 17 -16 -8 -16 8 3 -17 -12 -12 17 -2Z" fill="#FCC419" {s()}/>
<path d="M50 70 h10 v6 a5 5 0 0 1 -10 0Z M68 70 h10 v6 a5 5 0 0 1 -10 0Z" fill="#212529" {s('stroke-width="2"')}/>
<path d="M60 72 h8" {ln(O, 2.4)}/>
<path d="M58 84 Q64 88 70 84" fill="none" {s('stroke-width="2"')}/>
<path d="M88 64 L100 52" {ln(O, 7)}/><path d="M88 64 L100 52" {ln("#FCC419", 4)}/>
{sparkle(26, 104, 7, "#FFF3BF")}{sparkle(104, 108, 7, "#FFF3BF")}{sparkle(110, 92, 4, "#fff")}
'''))

# Люберцы, Весенняя: картонный кораблик-декорация плывёт по сцене между волнами-кулисами
I["artkids-lyubertsy-vesennyaya"] = ("картонный кораблик-декорация с алым парусом и мордашкой на борту",
    "плывёт по деревянной сцене между тремя рядами качающихся картонных волн, а сверху на него светит круглый луч",
    bg("#FFF9DB", "#E8590C", f'''
<path d="M40 -4 L20 120 H108 L88 -4Z" fill="#FFF3BF" opacity=".6"/>
<path d="M62 22 V74" {ln(O, 5)}/><path d="M62 22 V74" {ln("#8D6E63", 3)}/>
<path d="M66 24 Q94 40 90 70 H66Z" fill="#F03E3E" {s()}/>
<path d="M58 30 L38 66 H58Z" fill="#fff" {s('stroke-width="2.4"')}/>
<path d="M28 74 H104 L94 94 H38Z" fill="#C08552" {s()}/>
{eye(56, 84, 0.6)}{eye(70, 84, 0.6)}<path d="M59 89 Q63 92 67 89" fill="none" {s('stroke-width="1.8"')}/>
<path d="M-4 96 Q8 84 20 96 Q32 84 44 96 Q56 84 68 96 Q80 84 92 96 Q104 84 116 96 Q124 88 132 96 V104 H-4Z" fill="#339AF0" {s()}/>
<path d="M-4 108 Q10 98 24 108 Q38 98 52 108 Q66 98 80 108 Q94 98 108 108 Q120 98 132 108 V114 H-4Z" fill="#1C7ED6" {s()}/>
<rect x="-4" y="114" width="136" height="18" fill="#8D6E63" {s()}/>
'''))

# ---------- Monstarz Dance: хип-хоп, брейк, K-pop (8 филиалов — 8 разных героев) ----------

# Константинова: девочка-айдол показывает руками большое сердце над головой (K-pop)
I["monstarz-konstantinova"] = ("девочка с двумя высокими хвостиками в розовом укороченном топе и клетчатой юбке",
    "складывает руки над головой в огромное K-pop-сердце, а сбоку из-за неё вылетают маленькие розовые сердечки",
    bg("#FFDEEB", "#F06595", f'''
<path d="M54 118 L52 100 M74 118 L76 100" {ln(O, 9)}/><path d="M54 118 L52 100 M74 118 L76 100" {ln(SKIN, 6)}/>
<path d="M44 122 h14 v-5 h-12Z M70 122 h14 v-5 h-12Z" fill="#fff" {s('stroke-width="2"')}/>
<path d="M46 100 L52 80 H76 L82 100Z" fill="#5F3DC4" {s()}/>
<path d="M50 92 H78 M54 82 L50 100 M64 80 V100 M74 82 L78 100" {ln("#9775FA", 1.6)}/>
<rect x="50" y="64" width="28" height="18" rx="5" fill="#F783AC" {s()}/>
<path d="M50 68 Q30 54 40 32 Q48 18 64 34" fill="none" {ln(O, 9)}/><path d="M50 68 Q30 54 40 32 Q48 18 64 34" fill="none" {ln(SKIN, 6)}/>
<path d="M78 68 Q98 54 88 32 Q80 18 64 34" fill="none" {ln(O, 9)}/><path d="M78 68 Q98 54 88 32 Q80 18 64 34" fill="none" {ln(SKIN, 6)}/>
<path d="M50 44 Q40 34 44 22 M78 44 Q88 34 84 22" fill="none" {ln(O, 5)}/>
<path d="M50 44 Q40 34 44 22 M78 44 Q88 34 84 22" fill="none" {ln("#212529", 3)}/>
{head(64, 50, 13, "#212529", 0.55)}
<ellipse cx="55" cy="56" rx="3" ry="2" fill="#FF8787" opacity=".8"/><ellipse cx="73" cy="56" rx="3" ry="2" fill="#FF8787" opacity=".8"/>
<path d="M98 76 q4 -6 8 0 q4 -6 8 0 q0 6 -8 12 q-8 -6 -8 -12Z" fill="#F783AC" {s('stroke-width="2"')}/>
<path d="M14 84 q3 -4 6 0 q3 -4 6 0 q0 4 -6 8 q-6 -4 -6 -8Z" fill="#FCC2D7" {s('stroke-width="1.8"')}/>
<path d="M104 104 q3 -4 6 0 q3 -4 6 0 q0 4 -6 8 q-6 -4 -6 -8Z" fill="#FCC2D7" {s('stroke-width="1.8"')}/>
'''))

# Северодвинская (брейк 4–10): мальчик-брейкер в фризе на одной руке
I["monstarz-severodvinskaya"] = ("мальчик-брейкер в красной бандане и зелёных штанах",
    "стоит в фризе на одной руке вверх ногами на круглом чёрном танцполе, а вокруг него — дуги-стрелки вращения",
    bg("#FFF9DB", "#FAB005", f'''
<ellipse cx="64" cy="112" rx="50" ry="12" fill="#212529" {s()}/>
<path d="M30 112 a34 9 0 0 0 68 0" fill="none" {ln("#FFE066", 2)}/>
<path d="M58 108 L54 86" {ln(O, 9)}/><path d="M58 108 L54 86" {ln(SKIN, 6)}/>
<circle cx="56" cy="76" r="11" fill="{SKIN}" {s()}/>
<path d="M45 74 Q56 90 67 74 Q60 84 56 84 Q50 84 45 74Z" fill="#E03131" {s('stroke-width="2.2"')}/>
{eye(52, 72, 0.5)}{eye(60, 72, 0.5)}<path d="M52 66 Q56 63 60 66" fill="none" {s('stroke-width="1.8"')}/>
<path d="M48 60 Q46 46 58 36 L76 42 Q68 54 66 64Z" fill="#FFA94D" {s()}/>
<path d="M60 38 L58 14 M74 42 L94 26" {ln(O, 11)}/><path d="M60 38 L58 14 M74 42 L94 26" {ln("#2F9E44", 8)}/>
<path d="M52 12 h12 v-6 h-10Z M90 22 l10 -8 4 4 -8 8Z" fill="#fff" {s('stroke-width="2"')}/>
<path d="M50 64 Q38 66 34 58" fill="none" {ln(O, 8)}/><path d="M50 64 Q38 66 34 58" fill="none" {ln(SKIN, 5)}/>
<path d="M18 40 a40 40 0 0 1 20 -24 M110 70 a40 40 0 0 1 -14 26" fill="none" {ln(O, 3)}/>
<path d="M38 16 l-8 -1 4 7Z M96 96 l9 0 -4 -7Z" fill="{O}"/>
'''))

# Бескудниковский (хип-хоп 4–12): жёлтая панамка-бакет прыгает в ритм
I["monstarz-beskudnikovsky"] = ("жёлтая панамка-бакет с мордашкой и наклейкой-молнией",
    "подпрыгивает в ритм на синей пружинке, а вокруг пляшут зигзаги звука и две фиолетовые нотки",
    bg("#E5DBFF", "#7048E8", f'''
<path d="M64 120 l-14 -6 28 -6 -28 -6 28 -6 -28 -6 14 -4" fill="none" {ln(O, 7)}/>
<path d="M64 120 l-14 -6 28 -6 -28 -6 28 -6 -28 -6 14 -4" fill="none" {ln("#4DABF7", 4)}/>
<path d="M20 76 Q22 60 36 58 L42 30 Q64 18 86 30 L92 58 Q106 60 108 76 Q64 92 20 76Z" fill="#FCC419" {s()}/>
<path d="M36 58 Q64 68 92 58" fill="none" {s()}/>
<path d="M60 30 l-6 12 h8 l-6 12 14 -16 h-8 l6 -8Z" fill="#E8590C" {s('stroke-width="1.8"')}/>
{eye(52, 72, 0.7)}{eye(76, 72, 0.7)}<path d="M58 80 Q64 85 70 80" fill="none" {s('stroke-width="2.2"')}/>
<ellipse cx="44" cy="78" rx="4" ry="2.4" fill="#FF8787" opacity=".8"/><ellipse cx="84" cy="78" rx="4" ry="2.4" fill="#FF8787" opacity=".8"/>
<path d="M10 40 l6 6 -6 6 6 6 M118 40 l-6 6 6 6 -6 6" fill="none" {ln("#fff", 3)}/>
{note(22, 22, 0.75, "#5F3DC4")}{note(100, 104, 0.7, "#5F3DC4")}
'''))

# Алтуфьевское шоссе: медвежонок в бандане делает «волну» (хип-хоп)
I["monstarz-altufyevskoe"] = ("бурый медвежонок в синей бандане и белых кроссовках",
    "пускает по вытянутым лапам волну — движение хип-хопа «вэйв», над лапами бежит пунктирная волна",
    bg("#D3F9D8", "#37B24D", f'''
<path d="M52 118 L50 98 M76 118 L78 98" {ln(O, 13)}/><path d="M52 118 L50 98 M76 118 L78 98" {ln("#A0522D", 10)}/>
<path d="M40 120 h18 v-6 h-16Z M70 120 h18 v-6 h-16Z" fill="#fff" {s('stroke-width="2"')}/>
<ellipse cx="64" cy="82" rx="22" ry="22" fill="#A0522D" {s()}/>
<ellipse cx="64" cy="88" rx="12" ry="12" fill="#DEB887" {s('stroke-width="2"')}/>
<path d="M44 70 Q32 58 22 64 Q12 70 4 60" fill="none" {ln(O, 12)}/><path d="M44 70 Q32 58 22 64 Q12 70 4 60" fill="none" {ln("#A0522D", 9)}/>
<path d="M84 70 Q96 82 106 74 Q116 66 124 76" fill="none" {ln(O, 12)}/><path d="M84 70 Q96 82 106 74 Q116 66 124 76" fill="none" {ln("#A0522D", 9)}/>
<circle cx="46" cy="30" r="8" fill="#A0522D" {s()}/><circle cx="82" cy="30" r="8" fill="#A0522D" {s()}/>
<circle cx="64" cy="46" r="20" fill="#A0522D" {s()}/>
<path d="M44 40 Q64 22 84 40 Q64 34 44 40Z" fill="#1C7ED6" {s('stroke-width="2.4"')}/>
<circle cx="54" cy="34" r="1.6" fill="#fff"/><circle cx="64" cy="31" r="1.6" fill="#fff"/><circle cx="74" cy="34" r="1.6" fill="#fff"/>
<path d="M84 40 l10 4 -4 4Z" fill="#1C7ED6" {s('stroke-width="2"')}/>
<ellipse cx="64" cy="54" rx="9" ry="7" fill="#DEB887" {s('stroke-width="2"')}/><ellipse cx="64" cy="51" rx="3.5" ry="2.5" fill="{O}"/>
{eye(56, 44, 0.6)}{eye(72, 44, 0.6)}<path d="M60 57 Q64 60 68 57" fill="none" {s('stroke-width="1.8"')}/>
<path d="M2 46 Q12 36 22 46 Q32 56 42 46" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="3 4" stroke-linecap="round"/>
<path d="M86 58 Q96 48 106 58 Q116 68 126 58" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="3 4" stroke-linecap="round"/>
'''))

# Братиславская (хип-хоп для 4–10): кубок баттла в форме кроссовка
I["monstarz-bratislavskaya"] = ("золотой кубок в форме высокого кроссовка на мраморной подставке",
    "стоит после детского баттла на подиуме с цифрой 1, а сверху на него сыплется разноцветное конфетти",
    bg("#E3FAFC", "#15AABF", f'''
<rect x="28" y="96" width="72" height="30" rx="3" fill="#F1F3F5" {s()}/>
<text x="58" y="120" font-family="Arial" font-weight="bold" font-size="20" fill="#1098AD">1</text>
<rect x="40" y="86" width="48" height="10" rx="2" fill="#868E96" {s()}/>
<path d="M44 86 L46 36 Q48 26 62 26 L66 50 Q80 54 86 66 L86 86Z" fill="#FCC419" {s()}/>
<path d="M44 76 H86" {ln(O, 3)}/>
<path d="M50 40 l8 4 M50 48 l8 4 M50 56 l8 4" {ln(O, 2.4)}/>
<path d="M48 24 Q44 14 52 12" fill="none" {ln(O, 3)}/>
{eye(68, 64, 0.6)}{eye(78, 66, 0.6)}<path d="M70 72 Q74 75 78 72" fill="none" {s('stroke-width="1.8"')}/>
<rect x="18" y="14" width="6" height="4" fill="#F03E3E" transform="rotate(30 21 16)"/>
<rect x="96" y="22" width="6" height="4" fill="#7950F2" transform="rotate(-20 99 24)"/>
<rect x="106" y="50" width="6" height="4" fill="#FAB005" transform="rotate(40 109 52)"/>
<rect x="16" y="56" width="6" height="4" fill="#40C057" transform="rotate(-35 19 58)"/>
<rect x="80" y="8" width="6" height="4" fill="#E64980" transform="rotate(15 83 10)"/>
<circle cx="34" cy="36" r="2.5" fill="#fff"/><circle cx="100" cy="76" r="2.5" fill="#fff"/>
'''))

# Дмитровское шоссе: буква «М» из граффити танцует хип-хоп на кирпичной стене
I["monstarz-dmitrovskoe"] = ("пухлая граффити-буква «М» оранжево-фиолетовая с мордашкой",
    "танцует хип-хоп на фоне кирпичной стены: вскинула одну ножку и показывает «козу», вокруг брызги краски",
    bg("#FFE8CC", "#D9480F", f'''
<g opacity=".55">
<path d="M-4 20 H132 M-4 44 H132 M-4 68 H132 M-4 92 H132 M-4 116 H132" {ln("#C2410C", 2)}/>
<path d="M20 20 V44 M60 20 V44 M100 20 V44 M40 44 V68 M80 44 V68 M120 44 V68 M20 68 V92 M60 68 V92 M100 68 V92 M40 92 V116 M80 92 V116" {ln("#C2410C", 2)}/>
</g>
<path d="M26 92 L32 30 Q36 22 44 28 L64 54 L84 28 Q92 22 96 30 L102 92 Q96 98 88 92 L86 58 L68 80 Q64 84 60 80 L42 58 L40 92 Q32 98 26 92Z" fill="#FF922B" {s()}/>
<path d="M32 36 L36 30 M90 30 L94 36" {ln("#9C36B5", 4)}/>
<path d="M30 92 Q36 98 40 92 M88 92 Q94 98 100 92" fill="none" {ln("#9C36B5", 4)}/>
{eye(52, 66, 0.6)}{eye(76, 66, 0.6)}<path d="M58 74 Q64 78 70 74" fill="none" {s('stroke-width="2"')}/>
<path d="M100 40 L116 26" {ln(O, 8)}/><path d="M100 40 L116 26" {ln("#FF922B", 5)}/>
<path d="M112 22 v-8 M118 26 l6 -6" {ln(O, 4)}/>
<path d="M40 98 L34 116" {ln(O, 8)}/><path d="M40 98 L34 116" {ln("#FF922B", 5)}/>
<path d="M102 98 L118 104" {ln(O, 8)}/><path d="M102 98 L118 104" {ln("#FF922B", 5)}/>
<circle cx="16" cy="40" r="4" fill="#9C36B5"/><circle cx="10" cy="52" r="2" fill="#9C36B5"/><circle cx="112" cy="70" r="3" fill="#9C36B5"/><circle cx="20" cy="110" r="3" fill="#FF922B"/>
'''))

# ---------- Остальные ----------

# Чурочкина (Фрязино, рисование с 4 лет): детский рисунок-кот сохнет на прищепках
I["churochkina-fryazino"] = ("детский рисунок рыжего кота акрилом на листе с мордашкой-подписью",
    "сохнет на верёвке на двух деревянных прищепках рядом с рисунком солнца, а снизу капает свежая оранжевая краска",
    bg("#FFF5F5", "#FA5252", f'''
<path d="M-4 22 Q64 40 132 22" fill="none" {ln(O, 3)}/>
<rect x="18" y="30" width="58" height="72" rx="2" fill="#fff" {s()} transform="rotate(-4 47 66)"/>
<g transform="rotate(-4 47 66)">
<path d="M30 92 Q28 66 40 62 L36 48 L46 58 Q52 56 58 58 L66 48 L64 62 Q74 70 70 92Z" fill="#FF922B" {s('stroke-width="2.4"')}/>
<path d="M36 76 h-8 M36 80 h-8 M66 76 h8 M66 80 h8" {ln(O, 1.6)}/>
{eye(44, 72, 0.5)}{eye(56, 72, 0.5)}<path d="M48 80 Q50 82 52 80" fill="none" {s('stroke-width="1.6"')}/>
<path d="M44 102 v8" {ln("#FF922B", 4)}/><circle cx="44" cy="114" r="3" fill="#FF922B"/>
</g>
<rect x="28" y="20" width="8" height="18" rx="2" fill="#C08552" {s('stroke-width="2"')}/><rect x="60" y="22" width="8" height="18" rx="2" fill="#C08552" {s('stroke-width="2"')}/>
<rect x="84" y="30" width="38" height="44" rx="2" fill="#fff" {s()} transform="rotate(5 103 52)"/>
<circle cx="104" cy="52" r="9" fill="#FCC419" {s('stroke-width="2"')}/>
<path d="M104 36 v5 M104 63 v5 M88 52 h5 M115 52 h5 M93 41 l3 3 M112 60 l3 3 M93 63 l3 -3 M112 44 l3 -3" {ln("#FAB005", 2.4)}/>
<rect x="98" y="24" width="8" height="16" rx="2" fill="#C08552" {s('stroke-width="2"')}/>
'''))

# Арт-Балет (Царицыно, балет 2–14): балетная пачка-юбочка делает батман у станка
I["art-balet-radialnaya"] = ("розовая балетная пачка-юбочка с мордашкой на поясе и ножками в белых колготках",
    "держится лентой за деревянный балетный станок и высоко поднимает ножку в розовой балетке — батман",
    bg("#F3F0FF", "#B197FC", f'''
<path d="M-4 52 H132" {ln(O, 9)}/><path d="M-4 52 H132" {ln("#D9A066", 6)}/>
<path d="M20 52 V132 M108 52 V132" {ln(O, 6)}/><path d="M20 52 V132 M108 52 V132" {ln("#B07A4A", 3)}/>
<path d="M40 74 Q64 58 88 74 L106 82 Q64 98 22 82Z" fill="#FCC2D7" {s()}/>
<path d="M30 82 Q64 94 98 82 M40 74 L34 84 M52 70 L48 86 M64 68 V88 M76 70 L80 86 M88 74 L94 84" fill="none" {ln("#F783AC", 2)}/>
<rect x="46" y="60" width="36" height="14" rx="6" fill="#F06595" {s()}/>
{eye(58, 66, 0.55)}{eye(70, 66, 0.55)}<path d="M61 71 Q64 73 67 71" fill="none" {s('stroke-width="1.6"')}/>
<path d="M58 90 L56 122" {ln(O, 10)}/><path d="M58 90 L56 122" {ln("#fff", 7)}/>
<path d="M70 90 L104 28" {ln(O, 10)}/><path d="M70 90 L104 28" {ln("#fff", 7)}/>
<path d="M48 124 Q56 116 62 124Z" fill="#F783AC" {s('stroke-width="2"')}/>
<path d="M100 26 Q106 14 112 22 Q110 30 104 32Z" fill="#F783AC" {s('stroke-width="2"')}/>
<path d="M48 62 Q36 56 28 52" fill="none" {ln(O, 5)}/><path d="M48 62 Q36 56 28 52" fill="none" {ln("#F06595", 3)}/>
{sparkle(30, 22, 5)}{sparkle(116, 100, 5)}
'''))

# Монтото (Дзержинский, ИЗО с 3 лет): стаканчик-непроливайка с кисточками
I["montoto-dzerzhinsky"] = ("синий пластиковый стаканчик-непроливайка с мордашкой и мутной цветной водой",
    "в него ныряют и плещутся три кисточки — с красной, жёлтой и зелёной краской, а брызги разлетаются радужными каплями",
    bg("#E9FAC8", "#74B816", f'''
<path d="M36 64 H92 L86 116 Q64 124 42 116Z" fill="#339AF0" {s()}/>
<path d="M30 58 Q64 50 98 58 Q98 68 64 70 Q30 68 30 58Z" fill="#74C0FC" {s()}/>
<ellipse cx="64" cy="60" rx="20" ry="5" fill="#A9B4A0" {s('stroke-width="2"')}/>
<path d="M52 60 L36 18 M64 60 L66 12 M76 60 L96 20" {ln(O, 7)}/>
<path d="M52 60 L36 18 M64 60 L66 12 M76 60 L96 20" {ln("#E8C07A", 4)}/>
<path d="M34 14 Q30 4 36 2 Q40 6 38 14Z" fill="#F03E3E" {s('stroke-width="2"')}/>
<path d="M64 8 Q62 -2 68 -2 Q71 2 68 9Z" fill="#FAB005" {s('stroke-width="2"')}/>
<path d="M96 16 Q98 6 104 8 Q104 14 99 18Z" fill="#37B24D" {s('stroke-width="2"')}/>
{eye(54, 90, 0.75)}{eye(74, 90, 0.75)}<path d="M58 100 Q64 106 70 100" fill="none" {s('stroke-width="2.4"')}/>
<ellipse cx="46" cy="98" rx="4" ry="2.4" fill="#FF8787" opacity=".8"/><ellipse cx="82" cy="98" rx="4" ry="2.4" fill="#FF8787" opacity=".8"/>
<circle cx="20" cy="50" r="4" fill="#F03E3E" {s('stroke-width="1.6"')}/><circle cx="110" cy="46" r="4" fill="#37B24D" {s('stroke-width="1.6"')}/>
<circle cx="14" cy="70" r="2.5" fill="#FAB005"/><circle cx="116" cy="66" r="2.5" fill="#7950F2"/>
'''))

# «Мечта» (Дзержинский: ИЗО и бальные танцы с 4 лет): облачко-мечта рисует радугу и танцует вальс
I["mechta-dzerzhinsky-lesnaya"] = ("пушистое белое облачко-мечтатель с мордашкой на ножках в золотых бальных туфельках",
    "одной рукой рисует кисточкой радугу над собой, а ножками делает шаг вальса по сиреневому паркету",
    bg("#EDF2FF", "#748FFC", f'''
<path d="M10 70 A54 54 0 0 1 118 70" fill="none" {ln("#FF6B6B", 7)}/>
<path d="M18 70 A46 46 0 0 1 110 70" fill="none" {ln("#FFD43B", 7)}/>
<path d="M26 70 A38 38 0 0 1 102 70" fill="none" {ln("#51CF66", 7)}/>
<rect x="-4" y="112" width="136" height="20" fill="#B197FC" {s()}/>
<path d="M20 112 V132 M50 112 V132 M80 112 V132 M110 112 V132" {ln("#9775FA", 2)}/>
<path d="M54 96 L46 110 M74 96 L84 106" {ln(O, 7)}/><path d="M54 96 L46 110 M74 96 L84 106" {ln("#fff", 4)}/>
<path d="M38 112 h12 l-2 -4 h-8Z M80 110 l10 2 0 -4 -8 -2Z" fill="#FCC419" {s('stroke-width="2"')}/>
<path d="M34 82 Q26 70 36 62 Q36 48 52 50 Q58 38 72 44 Q86 40 90 54 Q104 58 98 72 Q104 84 90 90 Q84 100 70 96 Q60 102 50 96 Q36 96 34 82Z" fill="#fff" {s()}/>
{eye(56, 72, 0.7)}{eye(74, 72, 0.7)}<path d="M60 81 Q65 86 70 81" fill="none" {s('stroke-width="2.2"')}/>
<ellipse cx="48" cy="80" rx="4" ry="2.4" fill="#FF8787" opacity=".8"/><ellipse cx="82" cy="80" rx="4" ry="2.4" fill="#FF8787" opacity=".8"/>
<path d="M94 66 L110 50" {ln(O, 6)}/><path d="M94 66 L110 50" {ln("#E8C07A", 3)}/>
<path d="M110 50 Q114 42 120 44 Q118 50 112 52Z" fill="#7950F2" {s('stroke-width="1.8"')}/>
'''))

# «Гитарус» (Солнечногорск: гитара, барабаны, фортепиано с 6 лет): медиатор-персонаж играет на гитаре
I["gitarus-solnechnogorsk"] = ("оранжевый гитарный медиатор-треугольник с мордашкой и в кедах",
    "стоит на огромном грифе акустической гитары, как на мостике, и бьёт ножкой по струнам — из розетки вылетают нотки",
    bg("#FFF3BF", "#F08C00", f'''
<path d="M-4 104 L72 64" {ln(O, 20)}/><path d="M-4 104 L72 64" {ln("#8D6E63", 16)}/>
<path d="M2 98 L70 62 M4 104 L72 68" {ln("#DEE2E6", 1.4)}/>
<path d="M20 92 l4 6 M36 84 l4 6 M52 76 l4 6" {ln("#FCC419", 2)}/>
<circle cx="100" cy="88" r="34" fill="#D9A066" {s()}/>
<circle cx="92" cy="58" r="20" fill="#D9A066" {s()}/>
<circle cx="96" cy="80" r="10" fill="#5C3D2E" {s('stroke-width="2.4"')}/>
<path d="M72 64 L118 104" {ln("#DEE2E6", 1.4)}/>
<path d="M36 44 Q34 26 48 22 Q62 22 60 40 Q56 56 48 64 Q38 56 36 44Z" fill="#FF922B" {s()}/>
{eye(43, 38, 0.6)}{eye(54, 38, 0.6)}<path d="M45 46 Q48 49 52 46" fill="none" {s('stroke-width="1.8"')}/>
<path d="M44 62 L40 76 M52 62 L58 74" {ln(O, 3)}/>
<path d="M34 76 h10 v4 h-11Z M54 74 h10 v4 h-10Z" fill="#E03131" {s('stroke-width="1.8"')}/>
{note(100, 44, 0.8, "#5C3D2E")}{note(116, 30, 0.6, "#5C3D2E")}{note(80, 24, 0.6, "#5C3D2E")}
'''))

if __name__ == "__main__":
    if "--subjects" in sys.argv:
        for k, (h, sc, _) in I.items():
            print(f"{k} — герой: {h} | сцена: {sc}")
        sys.exit()
    ids = [a for a in sys.argv[1:] if not a.startswith("-")] or list(I)
    for k in ids:
        open(os.path.join(ROOT, "icons-src", k + ".svg"), "w").write(I[k][2])
    print(len(ids))
