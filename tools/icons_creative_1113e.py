"""Иконки робота creative, 13.11 (запуск 1113e). Каждая придумана и нарисована отдельно: свой герой, своя сцена,
своя компоновка и свой фон (правило абсолютной уникальности). python3 tools/icons_creative_1113e.py [--subjects]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_creative_1112k import bg, ln, limb, note, head, SKIN

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
I = {}

# 1 «Пой под гитару» (гитара и вокал с 6 лет, Коммунарка): каподастр-прищепка обнимает гриф гитары
I["poy-pod-gitaru-salarevskaya"] = ("чёрный гитарный каподастр-прищепка с мордашкой",
    "крепко обнял гриф большой рыжей акустической гитары, а из её круглой розетки вылетают нотки песни", bg("#FFF4D6", "#F7B267", f'''
<path d="M30 120 C8 118 6 92 22 84 C14 70 26 56 42 62 C52 56 66 62 66 74 C80 78 82 100 70 110 C62 122 44 122 30 120Z" fill="#E8833A" {s()}/>
<circle cx="44" cy="92" r="10" fill="#4A2A14" {s('stroke-width="2.4"')}/>
<path d="M50 72 L104 18" {ln(O, 13)}/><path d="M50 72 L104 18" {ln("#6B3E1E", 9)}/>
<path d="M100 14 l14 -6 6 6 -6 14Z" fill="#6B3E1E" {s('stroke-width="2.4"')}/>
<path d="M36 104 L106 16 M40 106 L108 20" stroke="#FFF1C9" stroke-width="1"/>
<g transform="rotate(-45 80 44)">
<rect x="56" y="30" width="48" height="26" rx="12" fill="#38D9A9" {s()}/>
<rect x="60" y="50" width="40" height="6" rx="3" fill="#0CA678" {s('stroke-width="2"')}/>
{face(80, 40, 8, 0.65)}
</g>
<path d="M74 60 l6 6 M86 48 l6 6" {ln(O, 2.4)}/>
{note(20, 52, 0.9, "#7048E8")}{note(34, 34, 1.0, "#E64980")}{note(10, 74, 0.7, "#1C7ED6")}
'''))

# 2 АртБалетФлай (балет с 2 лет, «Карапузы», Чертаново): малыш спускается на парашюте-пачке
I["artballetfly-azovskaya"] = ("двухлетняя малышка-карапуз в розовом купальнике",
    "плавно спускается с неба на парашюте, купол которого — пышная белая балетная пачка, и тянет носочек к облаку", bg("#E7F5FF", "#8EC5FC", f'''
<ellipse cx="34" cy="108" rx="22" ry="9" fill="#fff"/><ellipse cx="50" cy="104" rx="16" ry="10" fill="#fff"/>
<ellipse cx="104" cy="30" rx="12" ry="5" fill="#fff" opacity=".8"/>
<path d="M18 46 Q64 -6 110 46 Q100 40 92 46 Q84 38 76 46 Q68 38 60 46 Q52 38 44 46 Q36 38 28 46 Q22 40 18 46Z" fill="#fff" {s()}/>
<path d="M26 40 Q64 4 102 40" fill="none" stroke="#FFC9DE" stroke-width="3"/>
<path d="M20 46 L58 80 M108 46 L70 80 M44 46 L60 78 M84 46 L68 78" stroke="{O}" stroke-width="1.6"/>
{limb(58, 82, 52, 70, SKIN, 3.5)}{limb(70, 82, 76, 70, SKIN, 3.5)}
<path d="M54 80 H74 L72 98 H56Z" fill="#F783AC" {s()}/>
<path d="M50 94 Q64 88 78 94 L74 100 Q64 96 54 100Z" fill="#FFD8E8" {s('stroke-width="2"')}/>
{limb(60, 100, 56, 114, SKIN, 3.5)}{limb(68, 100, 76, 110, SKIN, 3.5)}
<ellipse cx="56" cy="116" rx="4" ry="2.4" fill="#F783AC" {s('stroke-width="1.6"')}/>
{head(64, 74, 9, "#E8B04A", 0.55)}
<circle cx="64" cy="63" r="3.5" fill="#E8B04A" {s('stroke-width="1.8"')}/>
'''))

# 3 FenixDance (бальные танцы детям с 3 лет, Семёновская): конкурсный номер «21» сам танцует ча-ча-ча
I["fenixdance-semenovskaya"] = ("белый турнирный номер «21» бальника с мордашкой, приколотый английскими булавками",
    "сам отплясывает ча-ча-ча на ножках в чёрных бальных туфлях посреди блестящего паркета, вскинув уголок, как руку", bg("#B3123B", "#4A0516", f'''
<path d="M0 100 H128 V128 H0Z" fill="#C98B4F"/>
<path d="M0 100 H128 M20 100 L10 128 M48 100 L44 128 M80 100 L84 128 M108 100 L118 128" stroke="#8A5A2B" stroke-width="2"/>
<rect x="30" y="24" width="64" height="54" rx="4" fill="#fff" {s()} transform="rotate(-6 62 51)"/>
<g transform="rotate(-6 62 51)">
<text x="62" y="52" font-family="Arial Black, Arial" font-weight="900" font-size="30" text-anchor="middle" fill="#1B1B2F">21</text>
{face(62, 64, 9, 0.55)}
<path d="M34 30 h12 M80 28 h10" {ln("#ADB5BD", 2.4)}/>
<circle cx="34" cy="30" r="2.6" fill="none" stroke="#868E96" stroke-width="1.6"/><circle cx="90" cy="28" r="2.6" fill="none" stroke="#868E96" stroke-width="1.6"/>
</g>
{limb(30, 34, 14, 18, "#fff", 4)}
{limb(52, 78, 44, 98, "#1B1B2F", 4.5)}{limb(72, 78, 86, 94, "#1B1B2F", 4.5)}
<path d="M36 96 h12 l2 4 h-16Z" fill="#1B1B2F" {s('stroke-width="2"')}/><path d="M84 92 l12 2 0 4 -14 -2Z" fill="#1B1B2F" {s('stroke-width="2"')}/>
{sparkle(108, 26, 5, "#FFD43B")}{sparkle(18, 64, 4, "#FFD43B")}{sparkle(110, 70, 3, "#fff")}
'''))

# 4 Active Style (хип-хоп для детей 7–11 лет, Семёновская): граффити-буквы «HIP HOP» пляшут на стене
I["active-style-shcherbakovskaya"] = ("пузатые граффити-буквы «HIP HOP» с мордашкой на букве O",
    "пляшут на кирпичной стене, подпрыгивая каждая в свой такт, а под ними на асфальте отбивает бит красная стрелка-зигзаг", bg("#F4A261", "#9C4A1A", f'''
<g stroke="#7A3A12" stroke-width="1.6" opacity=".55">
<path d="M0 30 H128 M0 50 H128 M0 70 H128 M0 90 H128"/>
<path d="M20 30 V50 M60 30 V50 M100 30 V50 M40 50 V70 M80 50 V70 M120 50 V70 M20 70 V90 M60 70 V90 M100 70 V90"/>
</g>
<path d="M0 98 H128 V128 H0Z" fill="#495057"/>
<path d="M16 112 L40 104 L60 116 L84 104 L110 114" fill="none" {ln("#FA5252", 5)}/>
<g font-family="Arial Black, Arial" font-weight="900" text-anchor="middle" stroke="{O}" stroke-width="2.6" paint-order="stroke">
<text x="26" y="58" font-size="30" fill="#FFE066" transform="rotate(-12 26 48)">H</text>
<text x="48" y="52" font-size="30" fill="#69DB7C" transform="rotate(8 48 42)">I</text>
<text x="70" y="60" font-size="30" fill="#4DABF7" transform="rotate(-6 70 50)">P</text>
<text x="34" y="92" font-size="28" fill="#DA77F2" transform="rotate(10 34 82)">H</text>
<text x="84" y="92" font-size="28" fill="#FFE066" transform="rotate(8 84 82)">P</text>
</g>
<circle cx="60" cy="80" r="13" fill="#FF8787" {s()}/><circle cx="60" cy="80" r="5" fill="#9C4A1A" {s('stroke-width="2"')}/>
{eye(55, 74, 0.45)}{eye(65, 74, 0.45)}
<path d="M98 30 l6 -6 M104 40 h8 M20 26 l-4 -6" {ln("#fff", 2.6)}/>
'''))

# 6 «Картина. Арт» (рисование 5–14 лет, Солнцево): золотая рама обнимает детский рисунок, с которого капает краска
I["kartina-art-solntsevo"] = ("золотая резная багетная рама с мордашкой на верхней планке",
    "обнимает ручками только что нарисованную детскую картину — синего кота под радугой, с которой ещё капает свежая краска", bg("#E3FAFC", "#66D9E8", f'''
<rect x="18" y="20" width="92" height="82" rx="4" fill="#E9B949" {s()}/>
<rect x="26" y="28" width="76" height="66" fill="#FFF9DB" {s('stroke-width="2.4"')}/>
<g fill="#C9962B"><circle cx="22" cy="24" r="2.4"/><circle cx="106" cy="24" r="2.4"/><circle cx="22" cy="98" r="2.4"/><circle cx="106" cy="98" r="2.4"/></g>
<path d="M36 70 A28 28 0 0 1 92 70" fill="none" stroke="#FF6B6B" stroke-width="5"/>
<path d="M42 70 A22 22 0 0 1 86 70" fill="none" stroke="#FFD43B" stroke-width="5"/>
<path d="M48 70 A16 16 0 0 1 80 70" fill="none" stroke="#51CF66" stroke-width="5"/>
<path d="M54 92 Q52 76 64 76 Q76 76 74 92Z" fill="#4C6EF5" {s('stroke-width="2.2"')}/>
<path d="M56 78 l-2 -7 6 4 M72 78 l2 -7 -6 4" fill="#4C6EF5" {s('stroke-width="2"')}/>
<circle cx="61" cy="82" r="1.3" fill="#fff"/><circle cx="67" cy="82" r="1.3" fill="#fff"/>
<path d="M40 70 v10 M84 70 v6" {ln("#FF6B6B", 3)}/><circle cx="40" cy="84" r="2.6" fill="#FF6B6B"/><circle cx="84" cy="80" r="2.4" fill="#FF6B6B"/>
{face(64, 12, 8, 0.5, mouth=True, blush=False)}
{limb(18, 60, 6, 80, "#E9B949", 4)}{limb(110, 60, 122, 80, "#E9B949", 4)}
<path d="M44 102 v12 M84 102 v12" {ln(O, 3)}/><path d="M38 114 h12 M78 114 h12" {ln(O, 3)}/>
'''))

# 7 Театр танца «Зеркальный мир» (дети 3–16 лет, Солнцево): трёхстворчатое трюмо с тремя разными танцами одной девочки
I["zerkalny-mir-bogdanova"] = ("трёхстворчатое зеркало-трюмо на гнутых ножках с мордашкой на верхушке",
    "в каждой створке отражается одна и та же девочка в своём танце: в средней — классика на носочке, в левой — эстрадный прыжок, в правой — мостик-акробатика", bg("#EDE7FF", "#9775FA", f'''
<path d="M4 40 L36 34 V96 L4 102Z" fill="#C5F6FA" {s()}/>
<path d="M124 40 L92 34 V96 L124 102Z" fill="#C5F6FA" {s()}/>
<path d="M36 34 Q64 10 92 34 V96 H36Z" fill="#E3FAFC" {s()}/>
<path d="M44 44 l8 -6 M100 48 l6 -4 M12 52 l6 -4" {ln("#fff", 2.4)}/>
<path d="M36 96 H92 V102 H36Z" fill="#B08968" {s('stroke-width="2.4"')}/>
<path d="M46 102 L42 120 M82 102 L86 120" {ln(O, 3.5)}/>
{face(64, 24, 6, 0.42, blush=False)}
<g>
<circle cx="64" cy="46" r="5" fill="{SKIN}" {s('stroke-width="1.8"')}/>
<path d="M60 52 H68 L72 64 H56Z" fill="#F783AC" {s('stroke-width="1.8"')}/>
<path d="M58 62 Q64 58 70 62" fill="none" {ln("#fff", 2)}/>
<path d="M62 64 V84 M66 64 L74 72" {ln(O, 2.6)}/>
<path d="M60 52 L52 42 M68 52 L76 42" {ln(O, 2.4)}/>
</g>
<g>
<circle cx="18" cy="54" r="4" fill="{SKIN}" {s('stroke-width="1.6"')}/>
<path d="M16 58 L20 72" {ln(O, 2.6)}/><path d="M18 62 L8 56 M18 62 L28 58 M20 72 L10 80 M20 72 L30 80" {ln(O, 2.2)}/>
</g>
<g>
<path d="M98 86 Q108 62 118 86" fill="none" {ln("#F783AC", 4)}/>
<circle cx="117" cy="82" r="3.5" fill="{SKIN}" {s('stroke-width="1.4"')}/>
</g>
{sparkle(64, 6, 3, "#fff")}
'''))

# 8 «Народный стиль» (хореография детям 3–5, 7–10, 11+, Новокосино): венок с лентами пляшет сам по себе
I["narodny-stil-lukhmanovskaya"] = ("венок из ромашек, васильков и колосков с длинными разноцветными лентами и мордашкой",
    "сам кружится в народной пляске над деревянной сценой, а ленты развеваются вокруг него широким колесом", bg("#FFF9DB", "#FFC078", f'''
<path d="M0 106 H128 V128 H0Z" fill="#B5733A"/><path d="M0 106 H128" {ln(O, 2.6)}/>
<path d="M30 116 h20 M70 120 h26" {ln("#8A5226", 2)}/>
<path d="M64 62 C30 70 14 92 22 104" fill="none" {ln("#FA5252", 5)}/>
<path d="M64 62 C98 70 114 92 106 104" fill="none" {ln("#4DABF7", 5)}/>
<path d="M64 62 C40 80 40 100 50 110" fill="none" {ln("#FFD43B", 5)}/>
<path d="M64 62 C88 80 88 100 78 110" fill="none" {ln("#51CF66", 5)}/>
<path d="M64 62 C34 50 18 34 22 20" fill="none" {ln("#DA77F2", 4)}/>
<ellipse cx="64" cy="48" rx="32" ry="20" fill="none" {ln(O, 13)}/>
<ellipse cx="64" cy="48" rx="32" ry="20" fill="none" {ln("#5C940D", 9)}/>
<g {s('stroke-width="1.6"')}>
<circle cx="34" cy="44" r="5" fill="#fff"/><circle cx="34" cy="44" r="2" fill="#FCC419"/>
<circle cx="50" cy="30" r="5" fill="#4C6EF5"/><circle cx="78" cy="30" r="5" fill="#fff"/><circle cx="78" cy="30" r="2" fill="#FCC419"/>
<circle cx="94" cy="44" r="5" fill="#4C6EF5"/><circle cx="88" cy="62" r="5" fill="#fff"/><circle cx="88" cy="62" r="2" fill="#FCC419"/>
<circle cx="40" cy="62" r="5" fill="#4C6EF5"/>
<path d="M64 26 l-3 -8 M64 26 l3 -8" fill="none"/><ellipse cx="64" cy="20" rx="3" ry="6" fill="#F2C94C"/>
</g>
{face(64, 46, 8, 0.6)}
{sparkle(108, 22, 4, "#fff")}{sparkle(16, 72, 3, "#fff")}
'''))

# 9 Underground dance studio (брейк-данс 5+, Пушкино, цоколь): девочка-брейкер замерла во фризе под лампочкой в подвале
I["underground-dance-pushkino"] = ("девочка-брейкер с двумя пушистыми пучками-гульками в мятной толстовке",
    "замерла во «фризе» на одной руке, задрав ноги в огромных красных кроссовках, под голой лампочкой на шнуре в бетонном подвальном зале", bg("#5C677D", "#1D2433", f'''
<path d="M64 0 V20" {ln("#ADB5BD", 2)}/><path d="M58 20 h12 v6 h-12Z" fill="#495057"/>
<circle cx="64" cy="32" r="7" fill="#FFE066" {s('stroke-width="2"')}/>
<path d="M64 32 L22 112 H106Z" fill="#FFE066" opacity=".16"/>
<path d="M0 110 H128 V128 H0Z" fill="#868E96"/><path d="M0 110 H128" {ln(O, 2.4)}/>
<path d="M14 118 l8 4 M96 118 l10 -3" stroke="#5C677D" stroke-width="2"/>
<g transform="translate(-14 -30) scale(1.25)">{limb(60, 110, 62, 88, SKIN, 4)}
<path d="M56 74 Q66 70 74 76 L72 94 Q62 98 54 92Z" fill="#63E6BE" {s()}/>
{limb(70, 78, 84, 58, "#495057", 5)}{limb(74, 84, 96, 70, "#495057", 5)}
<path d="M80 52 l10 -4 4 8 -10 4Z" fill="#FA5252" {s('stroke-width="2.2"')}/>
<path d="M94 64 l10 -4 4 8 -10 4Z" fill="#FA5252" {s('stroke-width="2.2"')}/>
<path d="M82 52 l4 6 M96 64 l4 6" stroke="#fff" stroke-width="1.6"/>
<circle cx="48" cy="92" r="10" fill="{SKIN}" {s()}/>
<circle cx="40" cy="100" r="5" fill="#5F3DC4" {s('stroke-width="2"')}/><circle cx="56" cy="102" r="5" fill="#5F3DC4" {s('stroke-width="2"')}/>
{eye(45, 90, 0.45)}{eye(52, 89, 0.45)}<path d="M46 96 q3 2 6 0" fill="none" {s('stroke-width="1.6"')}/>
</g>
<path d="M30 70 l-6 -4 M28 80 h-8 M104 96 l8 -2" {ln("#FFE066", 2.4)}/>
'''))

# 10 MyClub (бальные танцы, Baby Dance с 2,5 лет, Соколиная Гора): мальчиковый лакированный бальный ботинок ведёт в вальсе туфельку
I["myclub-volnaya"] = ("маленький чёрный лакированный мальчиковый бальный ботинок с мордашкой и бантиком-шнурком",
    "галантно ведёт в медленном вальсе крошечную розовую девичью туфельку по сияющему паркету, оставляя за собой след-«восьмёрку»", bg("#FFE8CC", "#E8590C", f'''
<path d="M0 84 H128 V128 H0Z" fill="#D9A066"/>
<path d="M0 84 H128 M14 84 L4 128 M40 84 L34 128 M70 84 L70 128 M100 84 L106 128" stroke="#A86B32" stroke-width="1.6"/>
<path d="M20 110 C40 92 60 124 80 106 C96 92 112 110 100 118 C88 126 76 100 60 112 C44 124 24 120 20 110Z" fill="none" stroke="#FFF3BF" stroke-width="2.4" stroke-dasharray="4 4"/>
<path d="M16 84 C16 64 30 56 46 58 L62 60 C72 62 78 72 76 82 L74 88 H22 C18 88 16 86 16 84Z" fill="#1F1F2E" {s()}/>
<path d="M22 88 H74" {ln("#555", 4)}/><path d="M60 88 V96 H70 V88" fill="#1F1F2E" {s('stroke-width="2.4"')}/>
<path d="M28 62 Q36 58 44 62" fill="none" {ln("#fff", 2.4)}/>
<path d="M44 58 l-6 -6 M44 58 l6 -6" {ln("#fff", 2.4)}/>
{face(36, 74, 7, 0.55)}
<path d="M72 70 Q84 54 92 62" fill="none" {ln(O, 3)}/>
<path d="M84 74 C84 62 94 58 104 60 L114 62 C120 64 120 74 116 78 L112 80 H88 C86 80 84 78 84 74Z" fill="#F783AC" {s()}/>
<path d="M108 80 L112 94" {ln(O, 3.5)}/>
{eye(96, 70, 0.4)}{eye(103, 70, 0.4)}
{sparkle(64, 30, 5, "#fff")}{sparkle(100, 30, 3.5, "#FFF3BF")}{sparkle(26, 34, 3, "#FFF3BF")}
'''))

# 11 Мастерская музыки Вероники Мавриц (вокал для малышей 3,5–5 лет, мюзикл, Пушкино): малыш поёт в деревянную ложку на табуретке
I["mavrits-music-pushkino"] = ("четырёхлетний малыш с рыжим хохолком в полосатой красно-белой футболке",
    "стоит на маленькой деревянной табуретке и звонко поёт в деревянную ложку, как в микрофон, а за ним на стене вырастает тень настоящей оперной звезды", bg("#E6FCF5", "#38D9A9", f'''
<path d="M78 20 C96 20 104 34 100 48 L110 74 L104 112 H72 L76 74 L70 48 C66 34 66 20 78 20Z" fill="#0B7285" opacity=".35"/>
<path d="M92 50 L118 30" stroke="#0B7285" stroke-width="7" stroke-linecap="round" opacity=".35"/>
<path d="M36 112 H76 V104 H36Z" fill="#C08552" {s()}/><path d="M40 112 V124 M72 112 V124" {ln(O, 4)}/>
{limb(50, 92, 48, 104, SKIN, 4)}{limb(60, 92, 62, 104, SKIN, 4)}
<path d="M42 62 H68 L66 94 H44Z" fill="#fff" {s()}/>
<path d="M43 70 H67 M43 78 H67 M44 86 H66" {ln("#FA5252", 4)}/>
{limb(66, 66, 76, 52, SKIN, 4)}
<path d="M76 52 L88 32" {ln(O, 5)}/><path d="M76 52 L88 32" {ln("#E9B949", 3)}/>
<ellipse cx="90" cy="28" rx="6" ry="8" fill="#E9B949" {s('stroke-width="2.4"')} transform="rotate(30 90 28)"/>
{limb(44, 66, 34, 56, SKIN, 4)}
<circle cx="55" cy="48" r="13" fill="{SKIN}" {s()}/>
<path d="M48 36 Q52 28 56 34 Q58 26 62 34" fill="#F08C00" {s('stroke-width="2"')}/>
{eye(50, 46, 0.5)}{eye(59, 46, 0.5)}
<ellipse cx="55" cy="54" rx="3.5" ry="4.5" fill="#C2255C" {s('stroke-width="1.8"')}/>
{note(20, 36, 0.9, "#7048E8")}{note(28, 18, 0.7, "#E64980")}{note(112, 92, 0.6, "#fff")}
'''))

# 12 K&k (танцевальный спорт с 3 лет): белые бальные перчатки танцуют в паре «рука в руке»
I["kk-dance-pokrovskaya-nab"] = ("пара белых детских бальных перчаток — одна с чёрной манжетой, другая с розовой оборкой",
    "сами по себе танцуют в паре «рука в руке», сцепившись пальчиками, на фоне бархатного синего занавеса с золотой бахромой", bg("#4263EB", "#1B2A7A", f"""
<path d="M0 0 Q16 40 8 128 H0Z M128 0 Q112 40 120 128 H128Z" fill="#2B3A99"/>
<path d="M0 8 H128" {ln("#FCC419", 6)}/>
<path d="M0 104 H128 V128 H0Z" fill="#C98B4F"/>
<g transform="rotate(-18 44 66)">
<path d="M34 104 V70 l-2 -18 a3.5 3.5 0 0 1 7 0 l1 12 V46 a3.5 3.5 0 0 1 7 0 V62 V44 a3.5 3.5 0 0 1 7 0 V64 l2 -10 a3.5 3.5 0 0 1 7 1 L58 78 V104Z" fill="#fff" {s()}/>
<rect x="32" y="96" width="28" height="12" rx="3" fill="#1B1B2F" {s('stroke-width="2.4"')}/>
{eye(42, 82, 0.5)}{eye(50, 82, 0.5)}<path d="M43 88 q3 3 6 0" fill="none" {s('stroke-width="1.8"')}/>
</g>
<g transform="rotate(18 84 66)">
<path d="M70 104 V70 l-2 -18 a3.5 3.5 0 0 1 7 0 l1 12 V46 a3.5 3.5 0 0 1 7 0 V62 V44 a3.5 3.5 0 0 1 7 0 V64 l2 -10 a3.5 3.5 0 0 1 7 1 L94 78 V104Z" fill="#fff" {s()}/>
<path d="M66 98 Q82 92 98 98 L96 110 Q82 104 68 110Z" fill="#F783AC" {s('stroke-width="2.2"')}/>
{eye(78, 82, 0.5)}{eye(86, 82, 0.5)}<path d="M79 88 q3 3 6 0" fill="none" {s('stroke-width="1.8"')}/>
</g>
<circle cx="64" cy="36" r="6" fill="#FFD43B" {s('stroke-width="2"')}/>
{sparkle(36, 26, 4, "#FFF3BF")}{sparkle(96, 24, 4, "#FFF3BF")}{sparkle(64, 18, 3, "#fff")}
"""))

# 13 «Виларт» (рисование 4–12 лет, скетчинг маркерами, Сокол): пенал-кит пускает фонтан из маркеров
I["vilart-volokolamsky"] = ("толстый синий пенал-кит на молнии с мордашкой",
    "выпускает из «дыхала» фонтан разноцветных маркеров и кисточек, а они на лету раскрашивают лист бумаги под ним цветными закорючками", bg("#FFF9DB", "#FFD43B", f"""
<rect x="10" y="96" width="108" height="26" rx="3" fill="#fff" {s()} transform="rotate(-3 64 108)"/>
<path d="M20 108 q8 -8 16 0 t16 0 M62 112 l8 -8 8 8 8 -8 M94 106 a5 5 0 1 0 10 0" fill="none" {ln("#E64980", 2.6)}/>
<path d="M22 70 C22 50 42 44 64 46 C88 48 106 56 108 70 C110 88 90 94 64 94 C40 94 22 88 22 70Z" fill="#4C6EF5" {s()}/>
<path d="M28 70 H104" {ln("#ADB5BD", 3)}/><path d="M28 70 H104" stroke="{O}" stroke-width="1" stroke-dasharray="2 2"/>
<path d="M104 64 l14 -10 v26Z" fill="#4C6EF5" {s()}/>
{face(50, 78, 8, 0.6)}
<g transform="rotate(-24 50 30)"><rect x="46" y="10" width="8" height="30" rx="3" fill="#FA5252" {s('stroke-width="2"')}/></g>
<g transform="rotate(4 64 26)"><rect x="60" y="4" width="8" height="34" rx="3" fill="#40C057" {s('stroke-width="2"')}/></g>
<g transform="rotate(28 78 30)"><rect x="74" y="10" width="8" height="30" rx="3" fill="#FAB005" {s('stroke-width="2"')}/></g>
<path d="M64 46 V38" {ln("#74C0FC", 4)}/>
<circle cx="40" cy="14" r="3" fill="#BE4BDB"/><circle cx="92" cy="14" r="3" fill="#15AABF"/>
"""))

# 14 «Постскриптум» (актёрское мастерство 7–10 лет, Тверская): буквы «P.S.» кланяются после спектакля
I["postskriptum-tverskaya"] = ("две пузатые буквы «P» и «S» с точками-носиками и мордашками",
    "низко кланяются на краю сцены после детского спектакля, а из-за кулис им летят розы и звучат аплодисменты", bg("#FFE3E3", "#C92A2A", f"""
<path d="M0 0 H128 V20 Q96 30 64 20 Q32 30 0 20Z" fill="#A61E4D" {s()}/>
<path d="M0 0 Q14 50 4 120 H0Z M128 0 Q114 50 124 120 H128Z" fill="#A61E4D"/>
<path d="M0 100 H128 V128 H0Z" fill="#5C3A21"/><path d="M0 100 H128" {ln(O, 3)}/>
<g transform="rotate(-14 44 70)">
<path d="M30 100 V40 H48 C64 40 64 68 48 68 H42 V100Z" fill="#FFD43B" {s()}/>
<path d="M42 50 H47 C52 50 52 58 47 58 H42Z" fill="#C92A2A" {s('stroke-width="2"')}/>
{eye(34, 78, 0.45)}{eye(40, 78, 0.45)}
</g>
<circle cx="58" cy="96" r="4" fill="#FFD43B" {s('stroke-width="2"')}/>
<g transform="rotate(14 84 70)">
<path d="M98 46 C92 38 72 38 72 52 C72 66 98 62 98 78 C98 94 74 96 70 86" fill="none" {ln(O, 15)}/>
<path d="M98 46 C92 38 72 38 72 52 C72 66 98 62 98 78 C98 94 74 96 70 86" fill="none" {ln("#74C0FC", 10)}/>
{eye(80, 52, 0.45)}{eye(87, 52, 0.45)}
</g>
<circle cx="104" cy="96" r="4" fill="#74C0FC" {s('stroke-width="2"')}/>
<g><circle cx="20" cy="40" r="4" fill="#FA5252" {s('stroke-width="1.6"')}/><path d="M20 44 l6 10" {ln("#2F9E44", 2)}/></g>
<g><circle cx="110" cy="36" r="4" fill="#FA5252" {s('stroke-width="1.6"')}/><path d="M110 40 l-6 10" {ln("#2F9E44", 2)}/></g>
"""))

# 15 «Балет СП» (Сергиев Посад, хореография с 3 лет): бумажная балеринка-оригами танцует на кончике карандаша
I["balet-sp-sergiev-posad"] = ("бумажная балеринка-оригами из нотного листа со складчатой юбкой-гармошкой",
    "стоит на носочке на кончике жёлтого карандаша, воткнутого в ластик-сцену, и вскинула руки над головой", bg("#E3FAFC", "#99E9F2", f"""
<rect x="40" y="108" width="48" height="16" rx="4" fill="#F783AC" {s()}/>
<path d="M60 108 L62 72 L66 72 L68 108Z" fill="#FFD43B" {s()}/>
<path d="M62 72 L64 64 L66 72Z" fill="#F8D9A0" {s('stroke-width="2"')}/>
<path d="M64 64 V54" {ln(O, 2.6)}/>
<path d="M36 54 L46 44 L54 54 L64 44 L74 54 L82 44 L92 54 L64 58Z" fill="#fff" {s()}/>
<path d="M46 44 L52 56 M64 44 V58 M82 44 L76 56" stroke="{O}" stroke-width="1.4"/>
<path d="M44 50 H86 M42 52 H88" stroke="#ADB5BD" stroke-width="0.8"/>
<path d="M56 44 L60 26 H68 L72 44Z" fill="#fff" {s()}/>
<path d="M60 30 L44 10 M68 30 L84 10" {ln(O, 3)}/>
<path d="M58 24 L64 8 L70 24Z" fill="#fff" {s()}/>
{eye(61, 18, 0.4)}{eye(67, 18, 0.4)}
{sparkle(20, 40, 4, "#fff")}{sparkle(106, 66, 4, "#fff")}{sparkle(98, 22, 3, "#3BC9DB")}
"""))

# 16 «Ориджинал дэнс» (Видное, танцы детям 4–11 лет): танцевальный коврик со стрелками
I["original-dance-vidnoe"] = ("квадратный танцевальный коврик со светящимися стрелками ↑ ↓ ← → и мордашкой в центре",
    "малышка в зелёных кроссовках прыгает по стрелкам, и каждая стрелка под её ногой вспыхивает своим цветом", bg("#F3F0FF", "#7950F2", f"""
<path d="M14 82 L64 62 L114 82 L64 106Z" fill="#212529" {s()}/>
<path d="M64 66 l-6 4 h4 v6 h4 v-6 h4Z" fill="#FF6B6B"/>
<path d="M64 102 l-6 -4 h4 v-6 h4 v6 h4Z" fill="#51CF66"/>
<path d="M28 84 l6 -5 v3 h7 v4 h-7 v3Z" fill="#4DABF7"/>
<path d="M100 84 l-6 -5 v3 h-7 v4 h7 v3Z" fill="#FFD43B"/>
{face(64, 82, 6, 0.45, blush=False)}
<path d="M94 84 l-8 -8 M100 90 l8 -6 M86 92 l-2 10" {ln("#FFD43B", 2.4)}/>
{limb(60, 52, 54, 66, SKIN, 3.5)}{limb(66, 52, 92, 74, SKIN, 3.5)}
<path d="M48 64 h10 q1 5 -4 5 h-8Z" fill="#40C057" {s('stroke-width="2"')}/>
<path d="M88 76 h10 q1 5 -4 5 h-8Z" fill="#40C057" {s('stroke-width="2"')}/>
<path d="M54 32 H72 L74 54 H52Z" fill="#FF922B" {s()}/>
{limb(54, 36, 40, 26, SKIN, 3.5)}{limb(72, 36, 86, 22, SKIN, 3.5)}
{head(63, 22, 9, "#5C3A21", 0.5)}
<circle cx="54" cy="14" r="4" fill="#5C3A21" {s('stroke-width="1.8"')}/><circle cx="72" cy="14" r="4" fill="#5C3A21" {s('stroke-width="1.8"')}/>
"""))

# 17 Школа русского балета (Южное Бутово, балет с 4 лет): Жар-птица в огненной пачке
I["russian-ballet-school-izyumskaya"] = ("Жар-птица с огненным хохолком в балетной пачке из алых и золотых перьев",
    "делает высокий батман на тёмной сцене русского балета, а её длинный хвост рассыпает над сценой золотые искры", bg("#3B1F5C", "#140A26", f"""
<path d="M0 108 H128 V128 H0Z" fill="#5C3A21"/><path d="M0 108 H128" {ln("#FCC419", 2)}/>
<path d="M58 66 C40 74 20 70 6 56 C22 62 36 60 44 54 C30 56 18 48 12 38 C28 48 44 50 52 46Z" fill="#FF922B" {s('stroke-width="2.4"')}/>
<path d="M14 40 l4 6 M8 56 l6 2" {ln("#FFE066", 2)}/>
{limb(66, 80, 64, 106, "#E8590C", 3.5)}{limb(70, 78, 98, 46, "#E8590C", 3.5)}
<path d="M48 76 Q70 62 92 76 Q70 88 48 76Z" fill="#FA5252" {s()}/>
<path d="M52 76 l-6 -6 M60 72 l-4 -8 M80 72 l4 -8 M88 76 l6 -6" {ln("#FFD43B", 3)}/>
<ellipse cx="70" cy="62" rx="10" ry="14" fill="#FF6B6B" {s()}/>
<circle cx="74" cy="42" r="10" fill="#FF922B" {s()}/>
<path d="M82 42 l8 3 -8 3Z" fill="#FFD43B" {s('stroke-width="2"')}/>
{eye(76, 40, 0.5)}
<path d="M70 32 Q66 18 74 14 M74 32 Q76 20 84 18 M78 34 Q86 26 92 28" fill="none" {ln("#FFD43B", 3)}/>
{limb(64, 56, 48, 40, "#FF922B", 3)}{limb(76, 56, 98, 70, "#FF922B", 3)}
{sparkle(22, 24, 4, "#FFD43B")}{sparkle(40, 16, 3, "#FFE066")}{sparkle(110, 26, 4, "#FFD43B")}{sparkle(108, 92, 3, "#FFE066")}
"""))

# 18 «ФаСольКа» (вокал детям 3–17 лет, фортепиано, Строгино): красная фасолинка-солистка поёт на нотном стане из фасолинок
I["fasolka-katukova"] = ("красная фасолинка-солистка с бантиком на макушке",
    "поёт в серебряный микрофончик, стоя на пяти линейках нотного стана, где вместо нот — её маленькие сестрички-фасолинки «фа» и «соль»", bg("#FFF5F5", "#FFA8A8", f"""
<g stroke="{O}" stroke-width="2"><path d="M4 92 H124 M4 100 H124 M4 108 H124 M4 116 H124 M4 124 H124"/></g>
<ellipse cx="22" cy="104" rx="7" ry="5" fill="#C92A2A" {s('stroke-width="2"')} transform="rotate(-20 22 104)"/>
<ellipse cx="104" cy="96" rx="7" ry="5" fill="#C92A2A" {s('stroke-width="2"')} transform="rotate(-20 104 96)"/>
{eye(20, 103, 0.3)}{eye(25, 101, 0.3)}{eye(102, 95, 0.3)}{eye(107, 93, 0.3)}
<text x="22" y="88" font-family="Arial Black, Arial" font-size="10" text-anchor="middle" fill="{O}">фа</text>
<text x="104" y="82" font-family="Arial Black, Arial" font-size="10" text-anchor="middle" fill="{O}">соль</text>
<path d="M44 86 C30 70 34 36 56 28 C78 20 96 36 92 58 C90 72 78 76 76 86 C74 96 54 98 44 86Z" fill="#E03131" {s()}/>
<path d="M58 34 Q64 30 70 34" fill="none" {ln("#fff", 3)}/>
<path d="M60 22 l-10 -8 0 14Z M60 22 l10 -8 0 14Z" fill="#FCC419" {s('stroke-width="2"')}/>
{face(62, 54, 8, 0.6, mouth=False)}
<ellipse cx="62" cy="66" rx="4" ry="5" fill="#5C0A0A"/>
{limb(82, 64, 96, 50, "#E03131", 3.5)}
<path d="M98 48 L104 30" {ln(O, 3)}/><circle cx="105" cy="26" r="6" fill="#CED4DA" {s('stroke-width="2.2"')}/>
{note(28, 40, 0.8, "#7048E8")}{note(112, 64, 0.6, "#E64980")}
"""))

if __name__ == "__main__":
    if "--subjects" in sys.argv:
        for k, (h, sc, _) in I.items():
            print(f"{k} — герой: {h} | сцена: {sc}")
        sys.exit()
    ids = [a for a in sys.argv[1:] if not a.startswith("-")] or list(I)
    for k in ids:
        open(os.path.join(ROOT, "icons-src", k + ".svg"), "w").write(I[k][2])
    print(len(ids))
