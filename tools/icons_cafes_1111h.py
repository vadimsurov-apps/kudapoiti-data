"""Иконки робота cafes, 2026-11-11 (11 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая придумана и нарисована отдельно,
у каждой свой герой (сверено с subjects.txt — героев с таким предметом в реестре нет), своя сцена, компоновка и фон.
Запуск: python3 tools/icons_cafes_1111h.py [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "h_escal": ("#F1E6FF", "#8E6CD8"),
    "h_jack": ("#E3FFF6", "#2BB59A"),
    "h_canvas": ("#FFF7DE", "#F2A94A"),
    "h_rope": ("#E8F4FF", "#4C8FE0"),
    "h_hello": ("#FFEFE6", "#F08A8A"),
    "h_sugar": ("#FFF0D8", "#C0703A"),
    "h_bag": ("#FFE9EE", "#C83B5A"),
    "h_cloud": ("#E6FBF4", "#3E8E86"),
    "h_scale": ("#F7EEDD", "#A58052"),
    "h_bell": ("#F2F7DC", "#8AA43C"),
    "h_vane": ("#E2FAFF", "#1FA2C2"),
    "h_milk": ("#DCEBFF", "#2F5FB8"),
    "h_stairs": ("#FFE6F6", "#D25CB0"),
    "h_brick": ("#FFE7D9", "#D0643F"),
    "h_canele": ("#FBF1E4", "#B98A5E"),
    "h_fire": ("#E7F5D9", "#3F7A3A"),
    "h_kimchi": ("#FFE3E3", "#E04848"),
    "h_petal": ("#E9F7FF", "#3C8FB0"),
    "h_stew": ("#E9FFE6", "#5DAA3A"),
    "h_party": ("#F3E3FF", "#7B3FB0"),
    "h_phone": ("#FFF3C9", "#F28C28"),
    "h_bundle": ("#E5F3FF", "#6E9BC9"),
    "h_apricot": ("#FFEBD6", "#E06A2A"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Вино и Хинкали (ТЦ «Атриум», 3 этаж): миска чашушули едет вверх по эскалатору
add("cafe-vino-i-hinkali-atrium",
    "глиняная миска грузинского чашушули — тушёной говядины в томатах с кинзой",
    "едет вверх по эскалатору торгового центра, держась ручкой за чёрный поручень, впереди табличка «3 этаж»",
    "h_escal", f'''
<path d="M6 118 L104 30 L124 30 L124 44 L22 128 L6 128Z" fill="#B9B4C8" {W(2.6)}/>
<path d="M18 112 l10 0 l0 -9 l10 0 l0 -9 l10 0 l0 -9 l10 0 l0 -9 l10 0 l0 -9 l10 0 l0 -9 l10 0 l0 -9 l10 0" fill="none" stroke="#7E7896" stroke-width="2.4"/>
<path d="M2 100 L96 16" stroke="{O}" stroke-width="6" stroke-linecap="round"/>
<path d="M2 100 L96 16" stroke="#3F3A55" stroke-width="3" stroke-linecap="round"/>
<g transform="rotate(-8 60 72)">
<path d="M30 66 Q60 64 90 66 Q88 96 60 98 Q32 96 30 66Z" fill="#B5643A" {W(2.8)}/>
<path d="M30 66 Q60 58 90 66 Q60 74 30 66Z" fill="#E0442E" {W(2.4)}/>
<circle cx="46" cy="64" r="4" fill="#9E2E1E" {W(1.6)}/><circle cx="62" cy="62" r="4.5" fill="#9E2E1E" {W(1.6)}/><circle cx="76" cy="65" r="3.6" fill="#9E2E1E" {W(1.6)}/>
<path d="M53 61 l3 -4 l3 4 M68 61 l2 -4 l3 3" fill="#4FB34A" {W(1.4)}/>
{face(60, 80, d=8, k=0.75)}
<path d="M86 70 Q96 56 74 42" fill="none" {W(3)}/>
</g>
<rect x="76" y="20" width="30" height="14" rx="4" fill="#fff" {W(2)}/>
<text x="91" y="31" font-family="Arial" font-weight="bold" font-size="10" text-anchor="middle" fill="{O}">3 эт</text>
''')

# 2. Додо (Варшавское ш., 152А): из коробки на пружинке выскакивает пицца-сердце
add("cafe-dodo-varshavskoe-152a",
    "пицца в форме сердца с кружками салями",
    "выскакивает на пружинке из открытой картонной коробки, как игрушка-чёртик из табакерки, вокруг разлетаются звёздочки",
    "h_jack", f'''
<path d="M24 92 L104 92 L100 116 L28 116Z" fill="#F4D9A8" {W(2.8)}/>
<path d="M24 92 L104 92 L118 74 L38 74Z" fill="#E9C384" {W(2.6)}/>
<path d="M24 92 L10 70 L24 66" fill="#F4D9A8" {W(2.4)}/>
<path d="M60 92 q-10 -6 0 -10 q10 -4 0 -10 q-10 -4 0 -10 q10 -4 0 -8" fill="none" stroke="#8C8C9A" stroke-width="3.4" stroke-linecap="round"/>
<path d="M60 64 C40 54 24 40 32 24 C40 10 56 16 60 26 C64 16 80 10 88 24 C96 40 80 54 60 64Z" fill="#F7B547" {W(2.8)}/>
<path d="M60 58 C44 50 32 40 37 28 C43 18 55 22 60 32 C65 22 77 18 83 28 C88 40 76 50 60 58Z" fill="#F45B3A"/>
<circle cx="46" cy="34" r="4.6" fill="#B32025" {W(1.6)}/><circle cx="75" cy="33" r="4.6" fill="#B32025" {W(1.6)}/><circle cx="60" cy="50" r="3.8" fill="#B32025" {W(1.6)}/>
<path d="M50 44 q3 2 6 0 M66 44 q3 2 6 0" fill="none" stroke="#FFF5C0" stroke-width="2"/>
{face(60, 38, d=6, k=0.6)}
{sparkle(18, 34, 5)}{sparkle(104, 40, 6)}{sparkle(96, 14, 4)}
''')

# 3. Додо (Дубнинская ул., 50): на голом корже детская рука рисует кисточкой соусом улыбку
add("cafe-dodo-dubninskaya-50",
    "круглый румяный корж для пиццы — пока без начинки, как чистый холст",
    "детская ладошка водит по нему кисточкой и рисует томатным соусом улыбку и два глаза",
    "h_canvas", f'''
<ellipse cx="58" cy="72" rx="44" ry="40" fill="#F0B862" {W(3)}/>
<ellipse cx="58" cy="72" rx="35" ry="31" fill="#FBE3A8" {W(2)}/>
<circle cx="45" cy="64" r="5" fill="#E2412E"/><circle cx="70" cy="62" r="5" fill="#E2412E"/>
<path d="M40 80 Q58 96 76 80" fill="none" stroke="#E2412E" stroke-width="5" stroke-linecap="round"/>
<ellipse cx="40" cy="72" rx="4" ry="2.4" fill="#FF7FA8" opacity=".55"/><ellipse cx="78" cy="70" rx="4" ry="2.4" fill="#FF7FA8" opacity=".55"/>
<g transform="rotate(35 92 48)">
<rect x="88" y="10" width="7" height="40" rx="3" fill="#4F8FE0" {W(2.2)}/>
<rect x="88" y="48" width="7" height="6" fill="#C9CCD8" {W(1.8)}/>
<path d="M88 54 Q91.5 66 95 54Z" fill="#E2412E" {W(1.8)}/>
</g>
<path d="M98 22 Q112 18 116 30 Q118 42 106 44 L96 40 Q92 30 98 22Z" fill="#FFD3B5" {W(2.4)}/>
<path d="M100 22 q-4 -6 2 -8 M106 20 q0 -7 5 -6" fill="#FFD3B5" {W(2)}/>
''')

# 4. Додо (Ломоносовский пр-т, 36): кубик чеддера идёт по сырной нитке между двумя кусками пиццы
add("cafe-dodo-lomonosovsky-36",
    "оранжевый кубик сыра чеддер",
    "идёт, как канатоходец, по тянущейся сырной нитке между двумя кусками пиццы и балансирует хлебной палочкой",
    "h_rope", f'''
<path d="M4 76 L30 58 L34 110 Z" fill="#F6C55A" {W(2.6)}/>
<path d="M10 78 L28 66 L31 100Z" fill="#F45B3A"/><circle cx="24" cy="80" r="3.4" fill="#B32025"/>
<path d="M124 76 L98 58 L94 110 Z" fill="#F6C55A" {W(2.6)}/>
<path d="M118 78 L100 66 L97 100Z" fill="#F45B3A"/><circle cx="104" cy="82" r="3.4" fill="#B32025"/>
<path d="M28 66 Q64 86 100 66" fill="none" stroke="#FFF1B0" stroke-width="5" stroke-linecap="round"/>
<path d="M28 66 Q64 86 100 66" fill="none" {W(1.6)}/>
<path d="M58 74 l-4 -8 M70 74 l4 -8" {W(2.6)}/>
<path d="M44 38 L64 30 L84 38 L84 60 L64 68 L44 60Z" fill="#F59A23" {W(2.8)}/>
<path d="M44 38 L64 46 L84 38 M64 46 V68" fill="none" {W(2)}/>
<circle cx="54" cy="56" r="2" fill="#D9771A"/><circle cx="76" cy="52" r="1.6" fill="#D9771A"/>
{face(64, 34, d=5, k=0.55, blush=False)}
<path d="M20 26 L108 18" stroke="#E6B66A" stroke-width="5" stroke-linecap="round"/>
<path d="M20 26 L108 18" fill="none" {W(1.6)}/>
<path d="M48 40 L40 24 M80 40 L88 21" {W(2.6)}/>
''')

# 5. Здрасте (б-р Дмитрия Донского, 1): пирожное-картошка машет и говорит «Здрасте!»
add("cafe-zdraste-donskogo-1",
    "пирожное «картошка» в какао-обсыпке с двумя кремовыми ростками на макушке",
    "приветливо машет ручкой, а над ним облачко-реплика «Здрасте!»",
    "h_hello", f'''
<ellipse cx="60" cy="112" rx="34" ry="6" fill="#B65C5C" opacity=".35"/>
<path d="M30 80 Q26 54 48 48 Q66 42 82 52 Q98 64 90 90 Q84 110 60 110 Q34 110 30 80Z" fill="#7A4A2E" {W(3)}/>
<g fill="#5B341F"><circle cx="44" cy="64" r="1.8"/><circle cx="70" cy="58" r="1.6"/><circle cx="82" cy="78" r="1.8"/><circle cx="40" cy="92" r="1.6"/><circle cx="74" cy="100" r="1.8"/></g>
<path d="M50 48 Q46 38 52 34 Q58 38 54 48Z M64 46 Q64 34 72 32 Q76 40 68 48Z" fill="#FFF6E6" {W(2.2)}/>
{face(60, 74, d=10, k=0.85)}
<path d="M90 76 Q102 68 106 56" fill="none" {W(3)}/>
<circle cx="107" cy="53" r="5" fill="#7A4A2E" {W(2.2)}/>
<path d="M112 46 l4 -3 M114 54 l5 0" stroke="{O}" stroke-width="2" stroke-linecap="round"/>
<path d="M10 14 H66 Q72 14 72 20 V32 Q72 38 66 38 H30 L22 46 L24 38 H16 Q10 38 10 32 V20 Q10 14 16 14Z" fill="#fff" {W(2.2)}/>
<text x="41" y="31" font-family="Arial" font-weight="bold" font-size="11" text-anchor="middle" fill="#C8434E">Здрасте!</text>
''')

# 6. Купец (Лобненская ул.): сахарная голова в синей обёртке раздаёт кусочки сахара
add("cafe-kupets-lobnenskaya",
    "купеческая сахарная голова — высокий белый конус сахара в синей бумажной обёртке",
    "стоит на прилавке лавки и угощает: протягивает ручкой кусочек колотого сахара, рядом горка таких кусочков",
    "h_sugar", f'''
<rect x="6" y="100" width="116" height="30" fill="#8C5530" {W(2.6)}/>
<path d="M6 108 H122" stroke="#6E3F22" stroke-width="2"/>
<path d="M60 14 L88 96 L32 96Z" fill="#FFFFFF" {W(3)}/>
<path d="M44 60 L76 60 L88 96 L32 96Z" fill="#2E5BB8" {W(2.8)}/>
<path d="M40 72 H80 M36 84 H84" stroke="#9FB8F0" stroke-width="2"/>
<path d="M54 22 L58 34 M64 30 L66 40" stroke="#E2E6F2" stroke-width="2"/>
{face(60, 46, d=6.5, k=0.6)}
<path d="M80 74 Q94 72 98 62" fill="none" {W(3)}/>
<path d="M94 56 L104 52 L108 60 L98 64Z" fill="#fff" {W(2)}/>
<path d="M12 98 L18 90 L24 98Z M20 98 L26 88 L32 98Z M14 92 L20 84 L24 92Z" fill="#fff" {W(1.8)}/>
{sparkle(104, 40, 4)}
''')

# 7. Брусника (Мичуринский пр-т, 5): калорийная булочка выглядывает из бумажного пакета, на макушке веточка брусники
add("cafe-brusnika-michurinsky-5",
    "калорийная булочка с изюмом и рубленым орехом сверху",
    "выглядывает из крафтового бумажного пакета, а на макушке у неё веточка брусники с тремя ягодками",
    "h_bag", f'''
<path d="M30 60 L98 60 L104 120 L24 120Z" fill="#D9B07A" {W(3)}/>
<path d="M30 60 l6 -6 l6 6 l6 -6 l6 6 l6 -6 l6 6 l6 -6 l6 6 l6 -6 l6 6 l6 -6 l4 6" fill="#D9B07A" {W(2.4)}/>
<path d="M64 74 v30 M50 88 q14 8 28 0" stroke="#B98A52" stroke-width="2" fill="none"/>
<path d="M34 62 Q30 30 64 26 Q98 30 94 62Z" fill="#8A4E26" {W(3)}/>
<path d="M38 50 Q64 38 90 50" fill="none" stroke="#C88A55" stroke-width="3"/>
<g fill="#4A2412"><ellipse cx="48" cy="40" rx="2.4" ry="1.6"/><ellipse cx="74" cy="36" rx="2.4" ry="1.6"/><ellipse cx="84" cy="46" rx="2" ry="1.4"/></g>
<g fill="#F2D49B" {W(1)}><path d="M56 34 l4 -2 l1 3z"/><path d="M66 32 l4 1 l-2 3z"/><path d="M42 48 l4 -1 l0 3z"/></g>
{face(64, 52, d=9, k=0.7)}
<path d="M58 28 Q62 14 74 10" fill="none" stroke="#3E7D32" stroke-width="2.6" stroke-linecap="round"/>
<path d="M66 18 q-8 -6 -14 0 q8 4 14 0Z M70 14 q6 -8 14 -4 q-6 6 -14 4Z" fill="#4FA344" {W(1.6)}/>
<circle cx="76" cy="12" r="4" fill="#D21F3C" {W(1.6)}/><circle cx="82" cy="18" r="3.6" fill="#D21F3C" {W(1.6)}/><circle cx="74" cy="20" r="3.4" fill="#E2344F" {W(1.6)}/>
''')

# 8. Тетри (Окская ул.): белый сыр-облачко над горами, с него капает гранатовый дождик
add("cafe-tetri-okskaya",
    "пухлый ломоть белого грузинского сыра имерули с дырочками-порами",
    "плывёт облаком над зелёными горами, а из него вместо дождя падают гранатовые зёрнышки",
    "h_cloud", f'''
<path d="M-4 128 L28 82 L50 104 L78 70 L132 128Z" fill="#5BAE6A" {W(2.6)}/>
<path d="M78 70 L70 82 L78 80 L86 84Z" fill="#fff" {W(1.8)}/>
<path d="M20 52 Q14 30 36 28 Q42 12 62 16 Q78 8 88 24 Q110 22 108 42 Q116 58 98 60 L30 60 Q16 62 20 52Z" fill="#FFFCF2" {W(3)}/>
<g fill="#EDE6CF"><circle cx="40" cy="44" r="3"/><circle cx="86" cy="36" r="2.6"/><circle cx="96" cy="50" r="2"/><circle cx="34" cy="34" r="2"/></g>
{face(64, 40, d=9, k=0.75)}
<g fill="#D9233F" {W(1.4)}>
<path d="M40 70 q3 5 0 8 q-3 -3 0 -8Z"/><path d="M58 76 q3 5 0 8 q-3 -3 0 -8Z"/><path d="M76 68 q3 5 0 8 q-3 -3 0 -8Z"/>
<path d="M48 88 q3 5 0 8 q-3 -3 0 -8Z"/><path d="M88 82 q3 5 0 8 q-3 -3 0 -8Z"/><path d="M68 94 q3 5 0 8 q-3 -3 0 -8Z"/>
</g>
''')

# 9. Булошная (Лялин пер.): длинная сайка на старинных чашечных весах перевешивает стопку монет
add("cafe-buloshnaya-lyalin",
    "продолговатая сайка с хрустящей корочкой и надрезом-гребешком",
    "лежит на одной чаше старинных латунных весов и перевешивает стопку медных монеток на другой чаше",
    "h_scale", f'''
<rect x="56" y="104" width="16" height="16" fill="#C99A3C" {W(2.4)}/>
<path d="M40 122 H88" {W(3)}/>
<path d="M64 104 V30" {W(3.2)}/>
<circle cx="64" cy="28" r="4" fill="#E2B54A" {W(2.2)}/>
<path d="M14 40 L114 60" stroke="#C99A3C" stroke-width="5" stroke-linecap="round"/>
<path d="M14 40 L114 60" fill="none" {W(1.6)}/>
<path d="M20 42 L10 70 M20 42 L34 70 M108 58 L96 86 M108 58 L120 86" stroke="{O}" stroke-width="1.8"/>
<path d="M4 70 Q22 82 40 70Z" fill="#E2B54A" {W(2.4)}/>
<path d="M90 86 Q108 98 126 86Z" fill="#E2B54A" {W(2.4)}/>
<ellipse cx="22" cy="60" rx="22" ry="11" fill="#E8A34E" {W(2.8)}/>
<path d="M8 58 Q22 50 36 58" fill="none" stroke="#B66A24" stroke-width="2.4"/>
{face(22, 62, d=5, k=0.5)}
<g fill="#C77A3A" {W(1.8)}><ellipse cx="108" cy="82" rx="8" ry="3"/><ellipse cx="108" cy="78" rx="8" ry="3"/><ellipse cx="108" cy="74" rx="8" ry="3"/></g>
''')

# 10. Кампанелло (Зеленодольская ул.): две трубочки каннеллони звонят в медный колокольчик
add("cafe-campanello-zelenodolskaya",
    "две трубочки каннеллони под томатным соусом и сыром, лежащие рядком",
    "звонят в маленький медный колокольчик на красной ленте (campanello — «колокольчик» по-итальянски), зовут к столу",
    "h_bell", f'''
<ellipse cx="58" cy="100" rx="48" ry="12" fill="#fff" {W(2.6)}/>
<rect x="18" y="66" width="76" height="20" rx="10" fill="#F6E2B0" {W(2.8)}/>
<rect x="18" y="82" width="76" height="20" rx="10" fill="#F6E2B0" {W(2.8)}/>
<ellipse cx="22" cy="76" rx="6" ry="10" fill="#E7B86A" {W(2.2)}/><ellipse cx="22" cy="92" rx="6" ry="10" fill="#E7B86A" {W(2.2)}/>
<path d="M28 68 Q44 60 58 68 Q72 76 92 66 L92 74 Q72 82 58 76 Q42 70 28 76Z" fill="#E2452F" {W(2)}/>
<path d="M40 70 l2 6 M66 74 l1 5 M82 70 l2 5" stroke="#FFF2A8" stroke-width="3" stroke-linecap="round"/>
{face(58, 92, d=8, k=0.6)}
<path d="M94 72 Q104 60 100 46" fill="none" {W(2.8)}/>
<path d="M98 22 Q112 18 114 34" fill="none" stroke="#D2263A" stroke-width="3"/>
<path d="M92 30 Q100 24 108 30 L112 48 Q100 54 88 48Z" fill="#E09A3A" {W(2.6)}/>
<circle cx="100" cy="52" r="3.2" fill="#B5721E" {W(1.8)}/>
<path d="M80 30 l-6 -4 M80 40 l-8 0 M118 40 l6 -2 M116 52 l7 2" stroke="{O}" stroke-width="2" stroke-linecap="round"/>
''')

# 11. Роза ветров (Сторожевая ул.): брусок нуги с флюгером-розой ветров на макушке
add("cafe-roza-vetrov-storozhevaya",
    "брусок белой нуги с орешками и тонкими вафельными пластинками сверху и снизу",
    "держит на макушке флюгер — розу ветров со стрелками и буквами С, Ю, З, В, а ветер раздувает её щёки",
    "h_vane", f'''
<path d="M20 28 q10 -4 18 0 M14 40 q8 -3 14 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".9"/>
<rect x="30" y="72" width="68" height="40" rx="6" fill="#FFFBF2" {W(3)}/>
<rect x="28" y="66" width="72" height="8" rx="3" fill="#F2D38C" {W(2.4)}/>
<rect x="28" y="110" width="72" height="8" rx="3" fill="#F2D38C" {W(2.4)}/>
<path d="M34 68 h64 M34 114 h64" stroke="#D9B05E" stroke-width="1.2"/>
<g fill="#B97A3C" {W(1.4)}><ellipse cx="40" cy="80" rx="3" ry="2"/><ellipse cx="88" cy="84" rx="3" ry="2"/><ellipse cx="46" cy="104" rx="2.6" ry="1.8"/><ellipse cx="86" cy="102" rx="3" ry="2"/></g>
<g fill="#7DC36A" {W(1.2)}><circle cx="58" cy="100" r="2"/><circle cx="74" cy="78" r="2"/></g>
{face(64, 88, d=10, k=0.75)}
<path d="M64 66 V36" {W(2.6)}/>
<path d="M64 10 L69 31 L90 36 L69 41 L64 62 L59 41 L38 36 L59 31Z" fill="#F4C542" {W(2.2)}/>
<path d="M64 18 L67 33 L82 36 L67 39 L64 54 L61 39 L46 36 L61 33Z" fill="#E2463C"/>
<circle cx="64" cy="36" r="3" fill="#fff" {W(1.6)}/>
<g font-family="Arial" font-weight="bold" font-size="8" fill="{O}" text-anchor="middle"><text x="64" y="9">С</text><text x="98" y="39">В</text><text x="30" y="39">З</text></g>
''')

# 12. Водопад (Юных Ленинцев, 71): из банки сгущёнки водопадом льётся молоко в пиалу
add("cafe-vodopad-yunykh-lenintsev",
    "жестяная банка сгущёнки в бело-голубой этикетке",
    "наклонилась с уступа скалы, и из неё водопадом льётся сгущённое молоко в пиалу внизу, разлетаются брызги",
    "h_milk", f'''
<path d="M-4 62 L52 54 L58 128 L-4 128Z" fill="#7A8AA6" {W(2.6)}/>
<path d="M8 70 l14 -2 M20 92 l18 -2" stroke="#5E6C88" stroke-width="2.4"/>
<g transform="rotate(-28 34 38)">
<rect x="14" y="18" width="40" height="40" rx="4" fill="#DCE6F6" {W(2.8)}/>
<rect x="14" y="26" width="40" height="22" fill="#fff" {W(2)}/>
<rect x="14" y="34" width="40" height="8" fill="#5D8FE0"/>
<ellipse cx="34" cy="18" rx="20" ry="5" fill="#C9D3E6" {W(2.4)}/>
{face(34, 30, d=6, k=0.5)}
</g>
<path d="M50 40 Q64 44 66 60 L72 106 L58 106 L56 62 Q54 50 46 48Z" fill="#FFF7E2" {W(2.6)}/>
<path d="M62 60 L64 100" stroke="#F1E3B8" stroke-width="2.4"/>
<path d="M44 104 Q66 126 96 104Z" fill="#F0F6FF" {W(2.8)}/>
<path d="M50 104 Q70 98 92 104" fill="#FFF7E2" {W(2)}/>
<circle cx="84" cy="96" r="3" fill="#fff" {W(1.6)}/><circle cx="92" cy="88" r="2.4" fill="#fff" {W(1.6)}/><circle cx="48" cy="96" r="2.4" fill="#fff" {W(1.6)}/>
{sparkle(100, 30, 6)}{sparkle(110, 60, 4)}
''')

# 13. Страна Хинкалия (Лобня): орешек фундука скатывается по радужной винтовой лестнице
add("cafe-strana-hinkaliya-lobnya",
    "круглый орешек фундука в коричневой скорлупке со светлой шапочкой",
    "съезжает по радужной винтовой лестнице, раскинув ручки от восторга",
    "h_stairs", f'''
<path d="M30 118 Q30 96 64 94 Q98 92 98 74 Q98 58 64 56 Q30 54 30 38 Q30 22 64 20" fill="none" stroke="#E2412E" stroke-width="12" stroke-linecap="round"/>
<path d="M30 118 Q30 96 64 94 Q98 92 98 74 Q98 58 64 56 Q30 54 30 38 Q30 22 64 20" fill="none" stroke="#F7B733" stroke-width="7" stroke-linecap="round"/>
<path d="M30 118 Q30 96 64 94 Q98 92 98 74 Q98 58 64 56 Q30 54 30 38 Q30 22 64 20" fill="none" stroke="#4FB34A" stroke-width="3" stroke-linecap="round"/>
<path d="M30 118 Q30 96 64 94 Q98 92 98 74 Q98 58 64 56 Q30 54 30 38 Q30 22 64 20" fill="none" stroke="#3E6FD8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="3 5"/>
<circle cx="90" cy="62" r="17" fill="#A9652E" {W(3)}/>
<path d="M76 56 Q90 40 104 56 Q90 50 76 56Z" fill="#E9CFA0" {W(2.2)}/>
<path d="M90 41 v-6" {W(2.4)}/>
{face(90, 66, d=6, k=0.55)}
<path d="M74 66 l-10 -6 M106 66 l10 -6" {W(2.8)}/>
{sparkle(30, 70, 5)}{sparkle(108, 28, 4)}
''')

# 14. Лофт (Лобня): листик мяты катается на дольке лимона по стакану лимонада у кирпичной стены
add("cafe-loft-lobnya-lenina-2a",
    "ярко-зелёный листик мяты с прожилками",
    "катается, как сёрфер, на дольке лимона по волне лимонада в высоком стакане на фоне кирпичной стены",
    "h_brick", f'''
<g stroke="#B9502C" stroke-width="1.6" fill="none" opacity=".7">
<path d="M0 30 H128 M0 48 H128 M0 66 H128 M0 84 H128 M0 102 H128"/>
<path d="M20 30 V48 M60 30 V48 M100 30 V48 M40 48 V66 M80 48 V66 M120 48 V66 M20 66 V84 M100 66 V84 M40 84 V102 M80 84 V102"/>
</g>
<path d="M34 40 L94 40 L88 122 L40 122Z" fill="#E8FAFF" fill-opacity=".85" {W(3)}/>
<path d="M37 62 Q50 54 64 62 Q78 70 91 60 L88 120 L40 120Z" fill="#FFE97A" {W(2)}/>
<rect x="46" y="88" width="10" height="10" rx="2" fill="#fff" opacity=".8" {W(1.4)}/><rect x="70" y="96" width="9" height="9" rx="2" fill="#fff" opacity=".8" {W(1.4)}/>
<path d="M44 58 Q64 70 86 56 Q64 50 44 58Z" fill="#FFE04A" {W(2.4)}/>
<path d="M50 58 Q64 64 80 57" fill="none" stroke="#fff" stroke-width="1.6"/>
<path d="M56 54 Q50 30 70 22 Q80 40 64 54Z" fill="#45B649" {W(2.6)}/>
<path d="M60 52 Q62 38 70 26 M62 44 l-5 -3 M65 38 l5 -2" fill="none" stroke="#2D7F33" stroke-width="1.6"/>
{face(64, 40, d=4.5, k=0.45, blush=False)}
''')

# 15. Valya Бистро (Амурская ул.): канеле на блюдце, над ним от кофе поднимается пар-сердечко
add("cafe-valya-bistro-amurskaya",
    "бордосская канеле — маленький рифлёный кексик с тёмной карамельной корочкой",
    "сидит на блюдце у чашки какао и мечтательно смотрит, как пар над чашкой складывается в сердечко",
    "h_canele", f'''
<ellipse cx="50" cy="104" rx="38" ry="9" fill="#fff" {W(2.6)}/>
<path d="M28 98 L30 56 Q50 48 70 56 L72 98 Q50 106 28 98Z" fill="#8B3E1C" {W(3)}/>
<path d="M36 58 L36 98 M44 55 L44 101 M52 54 L52 102 M60 55 L60 101 M66 57 L66 99" stroke="#5E2410" stroke-width="2"/>
<ellipse cx="50" cy="56" rx="20" ry="6" fill="#C96B2C" {W(2.4)}/>
<circle cx="50" cy="56" r="3.4" fill="#7A3416"/>
{face(50, 78, d=8, k=0.7)}
<path d="M86 84 L118 84 L114 110 Q102 116 90 110Z" fill="#7AC5B8" {W(2.6)}/>
<path d="M114 90 q10 2 6 10 q-3 4 -8 2" fill="none" {W(2.4)}/>
<ellipse cx="102" cy="84" rx="16" ry="4" fill="#9A6038" {W(2)}/>
<path d="M98 76 q-6 -8 2 -14 q6 -6 0 -14 M106 74 q6 -8 -2 -14" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<path d="M102 30 c-4 -6 -12 -1 -7 5 l7 7 l7 -7 c5 -6 -3 -11 -7 -5Z" fill="#FF6F8E" {W(1.8)}/>
''')

# 16. Усадьба (Филёвский парк): головка раклета плавится у костра и стекает на хлеб
add("cafe-usadba-filyovsky-park",
    "половинка круглой головки сыра для раклета с золотистым плавленым срезом",
    "греется у костра на летней веранде в парке, и расплавленный сыр стекает с неё на ломтик хлеба",
    "h_fire", f'''
<path d="M0 104 H128 V128 H0Z" fill="#9C6B3E" {W(2.4)}/>
<path d="M0 112 H128" stroke="#7A5230" stroke-width="2"/>
<path d="M10 44 Q16 34 22 44 L22 104 H10Z" fill="#2F6B2E" opacity=".6"/>
<path d="M18 92 A40 40 0 0 1 98 92Z" fill="#E8902E" {W(3)}/>
<path d="M26 92 A32 32 0 0 1 90 92Z" fill="#FFD95A" {W(2.2)}/>
<circle cx="44" cy="76" r="3.4" fill="#F2BE3A"/><circle cx="72" cy="70" r="2.8" fill="#F2BE3A"/>
<path d="M30 92 Q34 100 32 106 Q38 102 40 92 M58 92 Q60 102 58 108 Q66 104 66 92" fill="#FFD447" {W(2)}/>
<rect x="22" y="104" width="54" height="11" rx="5" fill="#E2A65E" {W(2.4)}/>
{face(58, 80, d=8, k=0.7)}
<path d="M98 102 L106 78 L112 92 L118 72 L124 102Z" fill="#FF8A2A" {W(2.2)}/>
<path d="M104 102 L110 88 L116 102Z" fill="#FFE05A"/>
<path d="M98 104 L124 98 M100 98 L124 104" stroke="#6E4422" stroke-width="4" stroke-linecap="round"/>
''')

# 17. Ra'men (4-й Сыромятнический пер.): горшочек кимчи с аниме-глазами
add("cafe-ramen-syromyatnichesky",
    "глиняный корейский горшочек-онгги, полный красного кимчи с торчащими капустными листиками",
    "смотрит огромными сияющими аниме-глазами, вокруг вспыхивают звёздочки-блёстки",
    "h_kimchi", f'''
<path d="M30 58 Q24 112 64 116 Q104 112 98 58Z" fill="#8A5A3C" {W(3)}/>
<path d="M34 70 Q64 78 94 70" fill="none" stroke="#6E432A" stroke-width="2.4"/>
<ellipse cx="64" cy="58" rx="36" ry="10" fill="#6E432A" {W(2.6)}/>
<path d="M36 56 Q40 30 56 40 Q60 22 72 38 Q86 26 92 54" fill="#E8463A" {W(2.6)}/>
<path d="M48 50 Q50 36 58 42 M70 48 Q74 34 82 44" fill="none" stroke="#F7EFC8" stroke-width="2.6" stroke-linecap="round"/>
<path d="M44 30 Q40 14 54 18 Q50 28 44 30Z M78 30 Q86 14 94 24 Q84 28 78 30Z" fill="#B8E07A" {W(2)}/>
<ellipse cx="50" cy="90" rx="8" ry="10" fill="{O}"/><ellipse cx="78" cy="90" rx="8" ry="10" fill="{O}"/>
<circle cx="47" cy="86" r="3.6" fill="#fff"/><circle cx="75" cy="86" r="3.6" fill="#fff"/>
<circle cx="53" cy="94" r="1.8" fill="#fff"/><circle cx="81" cy="94" r="1.8" fill="#fff"/>
<path d="M60 104 Q64 108 68 104" fill="none" {W(2.2)}/>
<ellipse cx="38" cy="100" rx="4.5" ry="2.6" fill="#FF7FA8" opacity=".7"/><ellipse cx="90" cy="100" rx="4.5" ry="2.6" fill="#FF7FA8" opacity=".7"/>
{sparkle(18, 40, 6)}{sparkle(110, 36, 7)}{sparkle(112, 84, 4)}{sparkle(16, 86, 4)}
''')

# 18. Жи Есть (ул. Орджоникидзе): чепалгаш, разрезанный на треугольники, раскрылся ромашкой вокруг кубика масла
add("cafe-zhi-est-ordzhonikidze",
    "чеченский чепалгаш — тонкая лепёшка с творогом, разрезанная на треугольники",
    "треугольнички разошлись вокруг тающего кубика масла, как лепестки ромашки, и каждый улыбается",
    "h_petal", f'''
<g transform="translate(64 66)">
{''.join(f'<g transform="rotate({a}) translate(0 -6)"><path d="M0 -10 L-14 -50 Q0 -55 14 -50Z" fill="#EDB257" {W(2.4)}/><ellipse cx="-3" cy="-36" rx="3.2" ry="2.2" fill="#B9742A"/><ellipse cx="5" cy="-26" rx="2.4" ry="1.8" fill="#B9742A"/><ellipse cx="-2" cy="-46" rx="2" ry="1.4" fill="#B9742A"/></g>' for a in range(0, 360, 45))}
</g>
<rect x="52" y="54" width="24" height="22" rx="4" fill="#FFF3A0" {W(2.6)}/>
<path d="M56 76 Q58 82 54 86 Q62 84 62 76" fill="#FFF3A0" {W(1.8)}/>
{face(64, 64, d=5, k=0.5)}
''')

# 19. Джонджоли (Волгоградский пр-т, 117): большая миска аджапсандала, пар над ней — силуэт гор
add("cafe-dzhondzholi-volgogradsky-117",
    "большая расписная миска грузинского аджапсандала — рагу из баклажанов, перца и помидоров",
    "дымится на праздничном столе, и пар над ней поднимается силуэтом снежных Кавказских гор",
    "h_stew", f'''
<path d="M24 46 L40 22 L52 36 L64 14 L80 34 L92 24 L106 46" fill="none" stroke="#fff" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" opacity=".95"/>
<path d="M58 20 L64 14 L70 22" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" opacity=".8"/>
<rect x="0" y="100" width="128" height="28" fill="#F6EBD2" {W(2.4)}/>
<path d="M0 108 H128" stroke="#E3D3AE" stroke-width="2"/>
<path d="M14 64 Q16 108 64 110 Q112 108 114 64Z" fill="#2E7FC0" {W(3)}/>
<path d="M22 80 Q64 92 106 80" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-dasharray="6 6"/>
<ellipse cx="64" cy="64" rx="50" ry="12" fill="#C2402E" {W(2.6)}/>
<ellipse cx="44" cy="62" rx="10" ry="5" fill="#5B2B6E" {W(1.8)}/><ellipse cx="80" cy="60" rx="9" ry="4.6" fill="#5B2B6E" {W(1.8)}/>
<path d="M58 58 q6 -4 12 0 q-6 6 -12 0Z" fill="#F2C230" {W(1.6)}/>
<path d="M28 62 q4 -4 8 0 M92 66 q4 -4 8 0 M66 68 l3 -4 l3 4" fill="#4FB34A" {W(1.4)}/>
{face(64, 90, d=11, k=0.8)}
''')

# 20. Ковчег (Жулебинский б-р): губадия со свечками на празднике
add("cafe-kovcheg-zhulebinsky-25",
    "высокий круглый татарский пирог губадия с узорчатой решёткой сверху",
    "стоит именинником на праздничном столе с тремя горящими свечками, вокруг сыплется разноцветное конфетти",
    "h_party", f'''
<ellipse cx="64" cy="112" rx="50" ry="10" fill="#fff" {W(2.6)}/>
<path d="M22 70 Q22 60 64 58 Q106 60 106 70 L104 104 Q64 116 24 104Z" fill="#D9893A" {W(3)}/>
<ellipse cx="64" cy="66" rx="42" ry="10" fill="#EBA555" {W(2.6)}/>
<path d="M30 64 L48 72 M44 60 L66 74 M62 58 L84 72 M80 58 L98 68 M98 62 L82 74 M80 58 L60 74 M60 58 L42 73 M42 60 L30 68" stroke="#B9692A" stroke-width="2.4"/>
<path d="M24 86 Q64 96 104 86" fill="none" stroke="#B9692A" stroke-width="2"/>
{face(64, 94, d=11, k=0.8)}
<g {W(2)}>
<rect x="44" y="34" width="6" height="22" fill="#FF6F9C"/><rect x="61" y="30" width="6" height="26" fill="#5EC8F2"/><rect x="78" y="34" width="6" height="22" fill="#9BE07A"/>
</g>
<path d="M47 32 q-4 -6 0 -10 q4 4 0 10Z M64 28 q-4 -6 0 -10 q4 4 0 10Z M81 32 q-4 -6 0 -10 q4 4 0 10Z" fill="#FFC531" {W(1.6)}/>
<g {W(1.2)}><rect x="18" y="20" width="6" height="4" fill="#FFD84A" transform="rotate(20 21 22)"/><rect x="104" y="28" width="6" height="4" fill="#FF6F9C" transform="rotate(-25 107 30)"/>
<rect x="28" y="40" width="5" height="4" fill="#5EC8F2" transform="rotate(-15 30 42)"/><rect x="98" y="46" width="5" height="4" fill="#9BE07A" transform="rotate(30 100 48)"/>
<circle cx="90" cy="16" r="2.4" fill="#FFD84A"/><circle cx="36" cy="14" r="2.4" fill="#9BE07A"/></g>
''')

# 21. Алло! Пицца (Энергетическая ул.): шоколадный смартфон, на экране звонит кусочек пиццы
add("cafe-allo-pizza-energeticheskaya",
    "плитка молочного шоколада в виде смартфона с экраном из белой глазури",
    "вибрирует от входящего звонка: на экране улыбается кусочек пиццы и надпись «Алло!»",
    "h_phone", f'''
<g transform="rotate(-10 64 66)">
<rect x="34" y="14" width="60" height="104" rx="12" fill="#7B4A2A" {W(3)}/>
<rect x="40" y="26" width="48" height="74" rx="5" fill="#FFF8EE" {W(2.2)}/>
<path d="M40 64 H88" stroke="#E9D9C2" stroke-width="1.4"/>
<path d="M64 108 m-5 0 a5 5 0 1 0 10 0 a5 5 0 1 0 -10 0" fill="#9A6038" {W(1.8)}/>
<path d="M50 34 L78 34 L64 62Z" fill="#F6C55A" {W(2)}/>
<path d="M54 38 L74 38 L64 56Z" fill="#F45B3A"/>
<circle cx="64" cy="44" r="2.6" fill="#B32025"/>
{face(64, 74, d=6, k=0.5, blush=False)}
<text x="64" y="94" font-family="Arial" font-weight="bold" font-size="11" text-anchor="middle" fill="#2BA54E">Алло!</text>
</g>
<path d="M18 50 q-6 10 0 20 M10 44 q-9 16 0 32 M110 46 q6 10 0 20 M118 40 q9 16 0 32" fill="none" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>
''')

# 22. Теремок (Авиамоторная ул.): блинный мешочек-кошелёк, завязанный пёрышком лука, на крылечке
add("cafe-teremok-aviamotornaya-41",
    "блинный мешочек-кошелёк с начинкой, завязанный пёрышком зелёного лука",
    "сидит на резном деревянном крылечке сказочного теремка и болтает ножками",
    "h_bundle", f'''
<path d="M10 128 V58 L64 30 L118 58 V128Z" fill="#C98A4A" {W(2.8)}/>
<path d="M4 60 L64 26 L124 60" fill="none" stroke="#D2263A" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M4 60 L64 26 L124 60" fill="none" {W(1.8)}/>
<path d="M24 66 H104 M24 80 H104" stroke="#A86E34" stroke-width="2"/>
<rect x="22" y="94" width="84" height="10" fill="#E9B46E" {W(2.4)}/>
<path d="M26 104 V128 M102 104 V128" {W(2.6)}/>
<path d="M26 94 q6 -6 12 0 q6 -6 12 0 q6 -6 12 0 q6 -6 12 0 q6 -6 12 0 q6 -6 12 0 q6 -6 12 0" fill="none" stroke="#D2263A" stroke-width="2.4"/>
<path d="M42 92 Q36 66 52 56 Q46 46 58 44 Q64 50 70 44 Q82 46 76 56 Q92 66 86 92Z" fill="#F5C36A" {W(3)}/>
<path d="M48 64 q4 4 2 10 M78 66 q-4 4 -2 10" fill="none" stroke="#D99A3E" stroke-width="2"/>
<g fill="#C88430"><circle cx="54" cy="84" r="1.6"/><circle cx="74" cy="82" r="1.4"/><circle cx="66" cy="62" r="1.4"/></g>
<path d="M50 54 Q64 60 78 54" fill="none" stroke="#3E9A3A" stroke-width="4" stroke-linecap="round"/>
<path d="M76 54 Q88 44 92 34" fill="none" stroke="#4FB34A" stroke-width="3.4" stroke-linecap="round"/>
{face(64, 74, d=8, k=0.65)}
<path d="M54 92 l-2 12 M74 92 l2 12" {W(2.8)}/>
''')

# 23. Чайхана Изюм (Энергетическая ул.): курага-подушка, на ней спит изюминка
add("cafe-chaikhana-izyum-energeticheskaya",
    "круглая мягкая долька кураги, похожая на оранжевую подушку",
    "на ней свернулась и сладко спит маленькая тёмная изюминка, а над ними плывут буквы «з-з-з»",
    "h_apricot", f'''
<ellipse cx="64" cy="108" rx="44" ry="8" fill="#B9471A" opacity=".3"/>
<path d="M18 80 Q14 52 44 46 Q64 40 84 46 Q114 52 110 80 Q108 104 64 106 Q20 104 18 80Z" fill="#F7962E" {W(3)}/>
<path d="M30 60 Q64 52 98 60 M28 88 Q64 96 100 88" fill="none" stroke="#E07418" stroke-width="2.2"/>
<path d="M64 46 Q62 76 64 104" fill="none" stroke="#E07418" stroke-width="2"/>
<path d="M50 84 Q52 92 58 90 M70 90 Q76 92 78 84" fill="none" {W(2.2)}/>
<ellipse cx="44" cy="92" rx="5" ry="2.8" fill="#FF6F6F" opacity=".55"/><ellipse cx="86" cy="92" rx="5" ry="2.8" fill="#FF6F6F" opacity=".55"/>
<path d="M58 98 Q64 101 70 98" fill="none" {W(2.2)}/>
<path d="M50 44 Q48 30 62 28 Q78 26 80 40 Q80 48 66 48 Q52 50 50 44Z" fill="#4A2338" {W(2.6)}/>
<path d="M56 36 q4 3 8 0 M68 36 q4 3 8 0" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round"/>
<path d="M58 32 Q66 30 74 34" fill="none" stroke="#7A4562" stroke-width="1.6"/>
<g font-family="Arial" font-weight="bold" fill="#fff" stroke="{O}" stroke-width="0.8"><text x="86" y="26" font-size="12">з</text><text x="96" y="18" font-size="10">з</text><text x="104" y="11" font-size="8">з</text></g>
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
