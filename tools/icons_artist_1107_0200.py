"""Робот «художник», 07.11 ~02:00 UTC: 40 иконок из auto/icon-repeats.json (больше всего похожих пар —
в основном кафе из старого генератора «блюдо × сцена»). Каждая придумана и нарисована отдельно, вручную:
своё блюдо по кухне заведения, своя сцена по названию/месту, свой ракурс и своя палитра фона.
Запуск из корня: python3 tools/icons_artist_1107_0200.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT

I = {}

# 1. Hatimaki (Люберцы) — ролл в повязке хатимаки рвёт финишную ленточку
I["cafe-hatimaki-lyubertsy"] = ("ролл-маки в повязке хатимаки", "рвёт грудью финишную ленточку на беговой дорожке", ("#FFF4F0", "#D8364A"), f'''
<path d="M0 98 H128 V128 H0Z" fill="#E8875A"/><path d="M0 108 H128 M0 119 H128" stroke="#fff" stroke-width="2.4"/>
<path d="M2 66 Q22 74 36 68" fill="none" stroke="#FFE14A" stroke-width="5" stroke-linecap="round"/>
<path d="M92 68 Q108 76 126 62" fill="none" stroke="#FFE14A" stroke-width="5" stroke-linecap="round"/>
<path d="M54 86 L44 100 L34 100 M74 86 L86 96 L96 90" fill="none" {W(4)}/>
<circle cx="64" cy="62" r="30" fill="#2F4A3A" {W(3)}/><circle cx="64" cy="62" r="23" fill="#fff"/>
<circle cx="64" cy="60" r="8" fill="#FF8A5A" {W(2)}/>
{eye(52, 64, .5)}{eye(76, 64, .5)}{smile(64, 74, 4, .7)}{blush(46, 72, .6)}{blush(82, 72, .6)}
<path d="M36 46 Q64 34 92 46 L91 54 Q64 43 37 54Z" fill="#fff" {W(2.4)}/><circle cx="64" cy="44" r="3.6" fill="#E8304A"/>
<path d="M92 49 L108 40 M92 51 L110 56" stroke="{O}" stroke-width="8" stroke-linecap="round"/>
<path d="M92 49 L108 40 M92 51 L110 56" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
<path d="M16 40 H28 M10 52 H24" stroke="#fff" stroke-width="3" stroke-linecap="round"/>''')

# 2. Бристоль Хаус — английский скон с джемом гуляет под дождём с зонтиком
I["cafe-bristol-house"] = ("английская булочка-скон со сливками и джемом", "гуляет под лондонским дождём под красным зонтиком", ("#EEF2F8", "#6B7FA0"), f'''
<path d="M14 26 l-3 8 M22 62 l-3 8 M108 62 l-3 8 M116 28 l-3 8 M110 96 l-3 8 M16 94 l-3 8" stroke="#D8E6FA" stroke-width="3" stroke-linecap="round"/>
<path d="M64 40 V66" {W(3)}/>
<path d="M28 42 Q64 4 100 42 Q91 36 82 42 Q73 36 64 42 Q55 36 46 42 Q37 36 28 42Z" fill="#E8304A" {W(3)}/>
<path d="M64 12 V7" {W(3)}/>
<path d="M32 80 Q32 68 64 68 Q96 68 96 80 V100 Q96 112 64 112 Q32 112 32 100Z" fill="#E8B060" {W(3)}/>
<path d="M34 78 Q42 64 53 72 Q61 62 72 72 Q82 64 94 78 Q64 86 34 78Z" fill="#FFF8E8" {W(2.4)}/>
<path d="M53 73 Q64 63 75 73 Q64 79 53 73Z" fill="#D8204A"/>
{eye(54, 94, .55)}{eye(74, 94, .55)}{smile(64, 101, 3.5, .65)}{blush(44, 101, .6)}{blush(84, 101, .6)}
<path d="M90 92 Q102 84 100 70 Q98 64 92 66" fill="none" {W(3)}/>''')

# 3. Macadamia — брауни жонглирует орешками макадамии
I["cafe-macadamia-pilyugina"] = ("брауни-кубик с шоколадной крошкой", "жонглирует тремя орешками макадамии", ("#F2FFE8", "#6FB85A"), f'''
<path d="M30 58 Q30 26 64 22 Q98 26 98 58" fill="none" stroke="#fff" stroke-width="2.2" stroke-dasharray="4 4"/>
<circle cx="30" cy="40" r="8" fill="#F3E2B8" {W(2.4)}/><circle cx="64" cy="20" r="8" fill="#F3E2B8" {W(2.4)}/><circle cx="98" cy="40" r="8" fill="#F3E2B8" {W(2.4)}/>
<circle cx="27" cy="37" r="2" fill="#fff"/><circle cx="61" cy="17" r="2" fill="#fff"/><circle cx="95" cy="37" r="2" fill="#fff"/>
<path d="M40 78 L26 58 M88 78 L102 58" {W(4)}/>
<rect x="36" y="58" width="56" height="52" rx="7" fill="#9A5A34" {W(3)}/>
<path d="M38 68 Q50 62 64 68 Q78 62 90 68" fill="none" stroke="#C8844E" stroke-width="3"/>
<rect x="44" y="96" width="6" height="5" fill="#5A2E18"/><rect x="78" y="94" width="6" height="5" fill="#5A2E18"/><rect x="62" y="102" width="5" height="4" fill="#5A2E18"/>
{eye(54, 82, .55)}{eye(74, 82, .55)}{smile(64, 89, 3.5, .65)}{blush(46, 90, .6)}{blush(82, 90, .6)}''')

# 4. Osteria Mario «Капитолий» — спагетти на вилке стоят меж колонн, как статуя
I["cafe-osteria-kapitoliy"] = ("клубок спагетти на вилке с томатным соусом", "стоит на пьедестале между белыми колоннами, как статуя", ("#FFF9EC", "#E8A23A"), f'''
<rect x="8" y="30" width="16" height="74" fill="#fff" {W(2.4)}/><rect x="104" y="30" width="16" height="74" fill="#fff" {W(2.4)}/>
<rect x="4" y="24" width="24" height="8" fill="#fff" {W(2.4)}/><rect x="100" y="24" width="24" height="8" fill="#fff" {W(2.4)}/>
<path d="M13 36 V100 M19 36 V100 M109 36 V100 M115 36 V100" stroke="#D8D8E8" stroke-width="1.6"/>
<rect x="38" y="104" width="52" height="14" rx="3" fill="#F2E6D0" {W(2.6)}/>
<path d="M64 104 V80" stroke="{O}" stroke-width="9" stroke-linecap="round"/><path d="M64 104 V80" stroke="#C8D0DC" stroke-width="4" stroke-linecap="round"/>
<ellipse cx="64" cy="62" rx="30" ry="24" fill="#FFD86A" {W(3)}/>
<path d="M38 56 Q64 46 90 58 M36 66 Q64 56 92 68 M42 76 Q64 68 86 78" fill="none" stroke="#E8B040" stroke-width="2.4"/>
<path d="M48 42 Q64 32 80 42 Q72 50 64 46 Q56 50 48 42Z" fill="#E8402A" {W(2.4)}/>
<path d="M64 36 Q70 28 76 32 Q70 38 64 36Z" fill="#4AB84A" {W(1.8)}/>
<path d="M86 74 Q92 86 86 96" fill="none" stroke="#FFD86A" stroke-width="4" stroke-linecap="round"/>
{eye(54, 64, .55)}{eye(74, 64, .55)}{smile(64, 72, 3.5, .65)}''')

# 5. Ботаника (Павловский Посад) — шарлотка в павлово-посадском платке
I["cafe-botanika-pavposad"] = ("яблочная шарлотка", "повязалась павлово-посадским платком с розами", ("#F4FFF6", "#4AA88A"), f'''
<path d="M18 80 Q18 62 64 62 Q110 62 110 80 V96 Q110 112 64 112 Q18 112 18 96Z" fill="#E8A848" {W(3)}/>
<path d="M30 96 Q38 92 46 96 M58 100 Q66 96 74 100 M86 96 Q94 92 100 96" fill="none" stroke="#C8842E" stroke-width="2.4"/>
<path d="M14 76 Q64 6 114 76 Q64 58 14 76Z" fill="#2A2238" {W(3)}/>
<circle cx="64" cy="40" r="8" fill="#E8304A" {W(2)}/><circle cx="44" cy="56" r="6" fill="#E8304A" {W(2)}/><circle cx="84" cy="56" r="6" fill="#E8304A" {W(2)}/>
<path d="M62 37 Q66 40 64 44 M42 54 Q46 56 44 59 M82 54 Q86 56 84 59" fill="none" stroke="#FF8A9A" stroke-width="1.6"/>
<path d="M52 44 L46 40 M76 44 L82 40 M34 64 L28 62 M94 64 L100 62" stroke="#4AB84A" stroke-width="4" stroke-linecap="round"/>
<path d="M18 74 L14 84 M24 70 L20 80 M110 74 L114 84 M104 70 L108 80" stroke="#E8304A" stroke-width="2"/>
{eye(52, 84, .6)}{eye(76, 84, .6)}{smile(64, 92, 4, .7)}{blush(42, 92, .7)}{blush(86, 92, .7)}''')

# 6. Ян Примус (Крылатское) — чешский кнедлик крутит педали на Крылатских холмах
I["cafe-yan-primus-krylatskoe"] = ("чешский кнедлик-ломтик с дырочками", "крутит педали велосипеда по Крылатским холмам", ("#EAF8FF", "#4A9AD8"), f'''
<path d="M0 104 Q30 84 64 100 Q96 84 128 98 V128 H0Z" fill="#6CC24A"/>
<circle cx="34" cy="100" r="16" fill="none" {W(3)}/><circle cx="96" cy="100" r="16" fill="none" {W(3)}/>
<circle cx="34" cy="100" r="2.6" fill="{O}"/><circle cx="96" cy="100" r="2.6" fill="{O}"/>
<path d="M34 100 L54 82 L84 82 L96 100 M54 82 L64 100 L84 82 M84 82 L88 66 L98 64" fill="none" stroke="#E8304A" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M56 98 L64 100 L58 104" fill="none" {W(2.6)}/>
<ellipse cx="62" cy="54" rx="26" ry="22" fill="#FFF6DE" {W(3)}/>
<circle cx="50" cy="44" r="2.2" fill="#E8D8B0"/><circle cx="74" cy="42" r="2" fill="#E8D8B0"/><circle cx="80" cy="58" r="2.2" fill="#E8D8B0"/><circle cx="46" cy="62" r="1.8" fill="#E8D8B0"/>
{eye(56, 52, .5)}{eye(72, 52, .5)}{smile(64, 60, 3.5, .65)}
<path d="M84 52 L96 64 M56 74 L62 98" fill="none" {W(3)}/>''')

# 7. Contrasto — чёрно-белое печенье: день и ночь
I["cafe-contrasto"] = ("чёрно-белое печенье: половина ваниль, половина шоколад", "ванильная половинка спит в ночи, шоколадная бодрствует днём", ("#FFE9A0", "#2A3270"), f'''
<rect x="0" y="0" width="64" height="128" fill="#2A3270"/><rect x="64" y="0" width="64" height="128" fill="#FFE27A"/>
<path d="M22 22 A12 12 0 1 0 34 36 A9 9 0 1 1 22 22Z" fill="#FFF6C4"/>
{sparkle(40, 22, 3)}{sparkle(16, 100, 3)}
<circle cx="104" cy="24" r="9" fill="#FF9A2A"/><path d="M104 8 V12 M118 24 H114 M90 24 H94 M114 14 L111 17 M94 14 L97 17" stroke="#FF9A2A" stroke-width="3" stroke-linecap="round"/>
<path d="M64 30 A34 34 0 0 0 64 98Z" fill="#FFF4DC"/><path d="M64 30 A34 34 0 0 1 64 98Z" fill="#6B3A22"/>
<circle cx="64" cy="64" r="34" fill="none" {W(3.2)}/><path d="M64 30 V98" {W(2)}/>
<path d="M44 62 Q49 66 54 62" fill="none" {W(2.4)}/>
<ellipse cx="76" cy="62" rx="4" ry="4.8" fill="#fff"/><circle cx="76" cy="63" r="2" fill="{O}"/>
<path d="M56 76 Q64 82 72 76" fill="none" stroke="#C88A5A" stroke-width="2.4" stroke-linecap="round"/>
<text x="38" y="52" font-family="Arial" font-size="9" font-weight="bold" fill="#A8B0E8">z</text>''')

# 8. Трактир «Ипполит Матвеевич» — пельмень в пенсне на венском стуле
I["cafe-ippolit-matveevich"] = ("пельмень в пенсне и с усиками", "чинно сидит на гнутом венском стуле", ("#F6F0FF", "#7A62B8"), f'''
<circle cx="64" cy="40" r="26" fill="none" stroke="#7A4A28" stroke-width="5"/>
<path d="M42 54 Q40 76 44 82 M86 54 Q88 76 84 82" fill="none" stroke="#7A4A28" stroke-width="5" stroke-linecap="round"/>
<path d="M42 92 Q38 108 30 120 M86 92 Q90 108 98 120 M54 94 L52 120 M74 94 L76 120" fill="none" stroke="#7A4A28" stroke-width="5" stroke-linecap="round"/>
<ellipse cx="64" cy="90" rx="30" ry="8" fill="#9A6234" {W(2.6)}/>
<path d="M36 84 Q34 52 64 50 Q94 52 92 84 Q78 90 64 86 Q50 90 36 84Z" fill="#FFF8EC" {W(3)}/>
<path d="M44 84 Q46 80 50 84 Q54 80 58 84 Q62 80 66 84 Q70 80 74 84 Q78 80 82 84" fill="none" stroke="#E8D8C0" stroke-width="2"/>
<circle cx="55" cy="66" r="6" fill="#E8F4FF" fill-opacity=".6" {W(2)}/><circle cx="73" cy="66" r="6" fill="#E8F4FF" fill-opacity=".6" {W(2)}/>
<path d="M61 66 H67 M79 66 Q86 72 84 84" fill="none" {W(1.6)}/>
<circle cx="55" cy="66" r="2.2" fill="{O}"/><circle cx="73" cy="66" r="2.2" fill="{O}"/>
<path d="M64 74 Q56 72 52 78 Q58 76 64 76 Q70 76 76 78 Q72 72 64 74Z" fill="#5A3A22" {W(1.4)}/>''')

# 9. Генацвале (Новый Арбат) — гозинаки играет на гитаре, как уличный музыкант
I["cafe-genatsvale-arbat"] = ("ромбик гозинаки из орехов в мёде", "играет на гитаре, как уличный музыкант на Арбате", ("#FFEFF6", "#C04A80"), f'''
<path d="M14 120 V54 M8 54 H20 L18 42 H10Z" fill="#FFE27A" {W(2.6)}/><circle cx="14" cy="48" r="10" fill="#FFE27A" opacity=".3"/>
<path d="M58 14 L98 56 L58 98 L18 56Z" fill="#D99A3A" {W(3)}/>
<path d="M40 44 l6 -3 l3 5 l-5 3Z M66 30 l6 2 l-1 6 l-6 -2Z M72 72 l5 -3 l4 5 l-5 3Z M34 60 l5 1 l-1 5 l-5 -1Z M58 82 l5 -2 l2 5 l-5 2Z" fill="#8A5224"/>
<path d="M50 28 L56 22 M30 50 L36 44" stroke="#FFE0A0" stroke-width="3" stroke-linecap="round"/>
{eye(50, 54, .55)}{eye(66, 54, .55)}{smile(58, 62, 3.5, .65)}{blush(42, 62, .6)}{blush(74, 62, .6)}
<path d="M70 96 L112 58" stroke="#5A3A22" stroke-width="5" stroke-linecap="round"/>
<path d="M108 54 l8 -6 l4 4 l-6 8Z" fill="#5A3A22" {W(1.6)}/>
<path d="M62 92 Q54 82 64 78 Q72 76 76 84 Q86 82 88 92 Q90 106 76 110 Q62 112 60 102 Q58 96 62 92Z" fill="#E8843A" {W(2.8)}/>
<circle cx="74" cy="94" r="4" fill="#5A3A22"/>
<path d="M98 30 v10 a3 3 0 1 1 -2 -3 M110 22 v8 a3 3 0 1 1 -2 -3" fill="none" stroke="#fff" stroke-width="2.4"/>''')

# 10. Park Baku — шекербура-полумесяц спит в звёздном небе вместо луны
I["cafe-park-baku"] = ("шекербура-полумесяц с узором-ёлочкой", "спит в ночном небе вместо месяца среди звёзд", ("#4A3C8A", "#1A1640"), f'''
{sparkle(98, 30, 6, "#FFE9A0")}{sparkle(108, 72, 4, "#FFE9A0")}{sparkle(86, 104, 5, "#FFE9A0")}{sparkle(30, 18, 3, "#FFE9A0")}
<path d="M58 16 A48 48 0 1 0 108 92 A40 40 0 0 1 58 16Z" fill="#F0B858" {W(3.2)}/>
<path d="M44 34 l-6 4 M40 44 l-7 3 M37 55 l-7 2 M36 66 l-7 0 M38 77 l-7 -2 M42 88 l-6 -3 M50 98 l-5 -5 M60 104 l-3 -6 M72 108 l-2 -7 M84 108 l0 -7" stroke="#B8742A" stroke-width="2.6" stroke-linecap="round"/>
<path d="M30 60 Q34 64 38 60 M44 70 Q48 74 52 70" fill="none" {W(2.4)}/>
<path d="M36 78 Q40 82 44 79" fill="none" {W(2.2)}/>{blush(28, 70, .6)}
<text x="58" y="56" font-family="Arial" font-size="11" font-weight="bold" fill="#C8C8F0">z</text><text x="66" y="44" font-family="Arial" font-size="8" font-weight="bold" fill="#C8C8F0">z</text>''')

# 11. Мясо & Рыба (ЗИЛ) — рыбка-гриль сама ловит удочкой котлету
I["cafe-myaso-ryba-zil"] = ("жареная рыбка с полосками от гриля", "сама сидит с удочкой и ловит из воды котлету", ("#E4FBFF", "#2AA0B8"), f'''
<path d="M0 96 Q32 90 64 96 T128 96 V128 H0Z" fill="#1E7AA0"/>
<path d="M60 52 Q84 16 116 18" fill="none" stroke="#7A4A28" stroke-width="3.4" stroke-linecap="round"/>
<path d="M116 18 V98" stroke="#fff" stroke-width="1.6"/>
<ellipse cx="108" cy="104" rx="12" ry="7" fill="#8A4A2A" {W(2.4)}/><path d="M100 102 l4 3 M108 100 l4 3 M114 104 l3 2" stroke="#B87048" stroke-width="2"/>
<path d="M14 66 L2 52 L4 82Z" fill="#E8A050" {W(3)}/>
<ellipse cx="44" cy="66" rx="34" ry="20" fill="#F0B060" {W(3)}/>
<path d="M30 50 L22 82 M44 46 L36 84 M58 48 L50 84" stroke="#9A5224" stroke-width="3.4" stroke-linecap="round"/>
<circle cx="64" cy="62" r="6" fill="#fff" {W(2)}/>{eye(64, 62, .55)}
<path d="M70 74 Q74 76 76 72" fill="none" {W(2.4)}/>
<path d="M44 82 Q50 92 58 86" fill="#E8A050" {W(2.4)}/>''')

# 12. Меркалето (Царицыно) — кростата в короне царицы у красно-белого дворца
I["cafe-merkaleto-tsaritsyno"] = ("итальянская кростата с решёткой и вареньем", "в короне царицы перед красно-кирпичной стеной Царицынского дворца", ("#FFF4EA", "#E87A5A"), f'''
<rect x="0" y="22" width="128" height="72" fill="#C8443A"/>
<path d="M14 92 V50 Q14 38 24 34 Q34 38 34 50 V92Z M94 92 V50 Q94 38 104 34 Q114 38 114 50 V92Z" fill="#fff" {W(2.2)}/>
<path d="M18 92 V54 Q18 44 24 40 Q30 44 30 54 V92Z M98 92 V54 Q98 44 104 40 Q110 44 110 54 V92Z" fill="#8AC0E8"/>
<path d="M0 26 H128" stroke="#fff" stroke-width="4" stroke-dasharray="6 4"/>
<path d="M18 88 Q18 76 64 76 Q110 76 110 88 V100 Q110 114 64 114 Q18 114 18 100Z" fill="#E8B060" {W(3)}/>
<ellipse cx="64" cy="86" rx="40" ry="10" fill="#C8202A" {W(2.6)}/>
<path d="M38 80 L50 94 M56 77 L70 95 M74 77 L88 94 M90 80 L82 94 M70 77 L58 95 M52 78 L40 92" stroke="#F0C070" stroke-width="3.4" stroke-linecap="round"/>
{eye(52, 103, .55)}{eye(76, 103, .55)}{smile(64, 109, 3, .55)}
<path d="M44 76 L42 56 L54 66 L64 50 L74 66 L86 56 L84 76Z" fill="#FFD24A" {W(2.8)}/>
<circle cx="64" cy="66" r="3.4" fill="#4AA8E8"/><circle cx="64" cy="48" r="3" fill="#FFD24A" {W(1.8)}/>''')

# 13. Илья Муромец (Ленинский) — пирожок-богатырь в шлеме лежит на русской печи
I["cafe-ilya-muromets"] = ("пирожок-богатырь в остроконечном шлеме", "лежит на русской печи, как Илья Муромец 33 года", ("#FFF8E8", "#D8A050"), f'''
<rect x="98" y="18" width="16" height="30" fill="#F4F0E8" {W(2.6)}/>
<path d="M14 60 H114 V120 H14Z" fill="#F4F0E8" {W(3)}/>
<path d="M44 120 V100 Q44 84 64 84 Q84 84 84 100 V120Z" fill="#3A2A30" {W(2.6)}/>
<path d="M52 118 Q50 104 58 100 Q60 108 64 102 Q68 94 72 104 Q78 108 76 118Z" fill="#FF8A2A"/>
<path d="M58 118 Q58 110 64 108 Q70 112 70 118Z" fill="#FFE04A"/>
<path d="M14 72 H40 M88 72 H114 M24 84 V72 M104 84 V72" stroke="#D8D0C0" stroke-width="2"/>
<path d="M22 58 Q22 38 64 36 Q106 38 106 58 Q64 64 22 58Z" fill="#E8A040" {W(3)}/>
<path d="M30 56 Q36 52 42 56 Q48 52 54 56 Q60 52 66 56 Q72 52 78 56 Q84 52 90 56 Q96 52 102 56" fill="none" stroke="#B8742A" stroke-width="2"/>
{eye(76, 46, .5)}{eye(92, 46, .5)}{smile(84, 52, 3, .55)}
<path d="M70 38 Q72 22 84 14 Q96 22 98 38Z" fill="#B8C4D8" {W(2.6)}/><path d="M84 14 V8" {W(2.6)}/>
<path d="M68 38 H100" {W(3)}/>''')

# 14. Хачапури тётушки Марико (Лесной Городок) — хачапури-конвертик на пеньке в лесу
I["cafe-mariko-lesnoy-gorodok"] = ("слоёный хачапури-конвертик пеновани", "отдыхает на пеньке посреди елового леса", ("#EFFFE6", "#3E8A4A"), f'''
<path d="M2 92 L18 30 L34 92Z M96 96 L112 26 L128 96Z" fill="#2E7A3E" {W(2.4)}/>
<path d="M0 104 Q64 94 128 104 V128 H0Z" fill="#7CC24A"/>
<path d="M38 96 V116 Q64 122 90 116 V96Z" fill="#9A6234" {W(2.8)}/>
<ellipse cx="64" cy="96" rx="26" ry="7" fill="#E8C08A" {W(2.6)}/><ellipse cx="64" cy="96" rx="14" ry="3.6" fill="none" stroke="#B88A5A" stroke-width="1.6"/>
<path d="M64 22 L100 56 L64 90 L28 56Z" fill="#F0B050" {W(3)}/>
<path d="M28 56 L64 46 L100 56 M64 22 L64 46 M64 90 L64 70" fill="none" stroke="#C8842E" stroke-width="2.2"/>
<path d="M64 46 L76 56 L64 70 L52 56Z" fill="#FFE97A" {W(2.2)}/>
{eye(52, 72, .5)}{eye(76, 72, .5)}{smile(64, 80, 3, .55)}{blush(46, 78, .5)}{blush(82, 78, .5)}''')

# 15. Корчма «Тарас Бульба» (Бакунинская) — вареник с чубом пляшет гопак
I["cafe-korchma-bakuninskaya"] = ("вареник-казачок с чубом-оселедцем", "пляшет гопак вприсядку, выбрасывая ноги в красных шароварах", ("#FFFBE0", "#4A7AE0"), f'''
<path d="M0 108 H128 V128 H0Z" fill="#F0D060"/>
<path d="M50 88 Q40 100 18 96 M78 88 Q90 100 110 94" fill="none" stroke="{O}" stroke-width="16" stroke-linecap="round"/>
<path d="M50 88 Q40 100 18 96 M78 88 Q90 100 110 94" fill="none" stroke="#E8304A" stroke-width="11" stroke-linecap="round"/>
<path d="M10 92 L20 90 L20 102 L8 102Z M116 88 L108 88 L108 100 L120 100Z" fill="#5A3A22" {W(2.4)}/>
<path d="M30 84 Q30 40 64 38 Q98 40 98 84Z" fill="#FFFAF0" {W(3)}/>
<path d="M32 84 Q36 80 40 84 Q44 80 48 84 Q52 80 56 84 Q60 80 64 84 Q68 80 72 84 Q76 80 80 84 Q84 80 88 84 Q92 80 96 84" fill="none" stroke="#E8DCC4" stroke-width="2.4"/>
<path d="M64 40 Q60 24 70 18 Q80 16 76 26" fill="none" stroke="#3A2A30" stroke-width="5" stroke-linecap="round"/>
<path d="M30 62 L12 48 M98 62 L116 48" {W(4)}/>
{eye(54, 60, .55)}{eye(74, 60, .55)}{smile(64, 68, 4, .7)}{blush(46, 68, .6)}{blush(82, 68, .6)}
<path d="M56 74 Q64 70 72 74" fill="none" stroke="#7A4A28" stroke-width="2.6" stroke-linecap="round"/>''')

# 16. IL Патио (ТЦ «Щука») — круглая пицца-плот, на ней загорает щучка
I["cafe-ilpatio-shchuka"] = ("круглая пицца пепперони", "плывёт по реке, как плот, на ней загорает маленькая щучка", ("#FFFDE8", "#58C8E8"), f'''
<path d="M0 82 Q32 76 64 82 T128 82 V128 H0Z" fill="#2E8AD0"/>
<path d="M8 112 Q24 108 40 112 M88 118 Q104 114 120 118" fill="none" stroke="#9AD0FF" stroke-width="2.6"/>
<ellipse cx="64" cy="86" rx="52" ry="22" fill="#E8A048" {W(3)}/>
<ellipse cx="64" cy="84" rx="44" ry="17" fill="#FFD45A"/>
<ellipse cx="38" cy="82" rx="7" ry="4" fill="#D8343A"/><ellipse cx="90" cy="80" rx="7" ry="4" fill="#D8343A"/><ellipse cx="66" cy="94" rx="7" ry="4" fill="#D8343A"/><ellipse cx="80" cy="92" rx="5" ry="3" fill="#4AB84A"/>
{eye(52, 86, .5)}{eye(76, 86, .5)}<path d="M60 92 Q64 95 68 92" fill="none" {W(2)}/>
<path d="M30 68 Q50 56 76 64 L88 56 L86 70 L76 68 Q50 76 30 68Z" fill="#7AB860" {W(2.4)}/>
<path d="M44 62 l2 8 M54 61 l2 9" stroke="#4A8A3A" stroke-width="2"/>
<path d="M30 64 Q36 62 40 66" fill="none" stroke="{O}" stroke-width="3"/><circle cx="36" cy="65" r="3" fill="{O}"/>
<circle cx="104" cy="26" r="11" fill="#FFD24A"/>''')

# 17. Кухня Полли — крекер, за уголок которого держится попугай Полли
I["cafe-kukhnya-polli"] = ("солёный крекер с дырочками", "попугай Полли сидит на уголке и клюёт его", ("#FFF0E0", "#F08A3A"), f'''
<rect x="22" y="46" width="70" height="66" rx="6" fill="#F0C068" {W(3)}/>
<path d="M28 52 l3 0 M44 52 l3 0" stroke="#fff"/>
<circle cx="36" cy="60" r="2.4" fill="#B8742A"/><circle cx="57" cy="60" r="2.4" fill="#B8742A"/><circle cx="78" cy="60" r="2.4" fill="#B8742A"/>
<circle cx="36" cy="98" r="2.4" fill="#B8742A"/><circle cx="57" cy="100" r="2.4" fill="#B8742A"/><circle cx="78" cy="98" r="2.4" fill="#B8742A"/>
<circle cx="32" cy="70" r="1.6" fill="#fff"/><circle cx="80" cy="74" r="1.6" fill="#fff"/><circle cx="50" cy="104" r="1.6" fill="#fff"/>
{eye(46, 78, .55)}{eye(68, 78, .55)}{smile(57, 86, 4, .7)}{blush(38, 86, .6)}{blush(76, 86, .6)}
<path d="M98 54 Q112 70 118 92 Q106 84 96 66Z" fill="#E8304A" {W(2.4)}/>
<ellipse cx="96" cy="44" rx="13" ry="16" fill="#3AB84A" {W(2.8)}/>
<circle cx="90" cy="26" r="11" fill="#4AD05A" {W(2.8)}/>
<path d="M80 26 Q72 30 78 38 Q82 34 84 30Z" fill="#FFC530" {W(2.2)}/>
<circle cx="90" cy="24" r="3.4" fill="#fff" {W(1.4)}/><circle cx="89" cy="24" r="1.6" fill="{O}"/>
<path d="M104 40 Q108 48 102 54" fill="none" stroke="#2A8A3A" stroke-width="2.4"/>
<path d="M90 60 L88 66 M98 60 L98 66" {W(2.4)}/>''')

# 18. Гамбринус (Большая Спасская) — брецель ловит языком падающую соль
I["cafe-gambrinus-spasskaya"] = ("крендель-брецель", "ловит языком крупинки соли, падающие, как снежинки", ("#E6EEFF", "#3A4AA8"), f'''
<rect x="20" y="10" width="5" height="5" fill="#fff" transform="rotate(20 22 12)"/><rect x="50" y="16" width="4" height="4" fill="#fff" transform="rotate(40 52 18)"/>
<rect x="82" y="8" width="5" height="5" fill="#fff" transform="rotate(15 84 10)"/><rect x="104" y="22" width="4" height="4" fill="#fff"/>
<rect x="14" y="40" width="4" height="4" fill="#fff" transform="rotate(30 16 42)"/><rect x="110" y="48" width="5" height="5" fill="#fff" transform="rotate(25 112 50)"/>
<g fill="none" stroke-linecap="round" stroke-linejoin="round">
<path d="M40 104 C10 92 12 40 44 36 C70 34 72 64 64 74 C56 64 58 34 84 36 C116 40 118 92 88 104 M40 104 L76 68 M88 104 L52 68" stroke="{O}" stroke-width="20"/>
<path d="M40 104 C10 92 12 40 44 36 C70 34 72 64 64 74 C56 64 58 34 84 36 C116 40 118 92 88 104 M40 104 L76 68 M88 104 L52 68" stroke="#B8642A" stroke-width="14"/>
<path d="M22 70 C22 52 30 42 44 41 M106 70 C106 52 98 42 84 41" stroke="#D88A48" stroke-width="4"/></g>
<rect x="30" y="60" width="3" height="3" fill="#fff"/><rect x="96" y="80" width="3" height="3" fill="#fff"/><rect x="58" y="96" width="3" height="3" fill="#fff"/>
<circle cx="64" cy="90" r="14" fill="#C8783A" {W(2.4)}/>
{eye(58, 87, .45)}{eye(70, 87, .45)}
<path d="M60 94 Q64 98 68 94 L67 100 Q64 103 61 100Z" fill="#FF7FA8" {W(1.8)}/>''')

# 19. Алубали (Заречье) — вишнёвый штрудель катает вишенку на плечах
I["cafe-alubali-zareche"] = ("вишнёвый штрудель-рулет в сахарной пудре", "катает вишенку-малыша у себя на плечах", ("#FFE8EE", "#E0507A"), f'''
<rect x="14" y="70" width="100" height="38" rx="19" fill="#F0C070" {W(3)}/>
<path d="M30 74 L38 90 M50 72 L58 90 M70 72 L78 90 M90 74 L98 90" stroke="#C8202A" stroke-width="4" stroke-linecap="round"/>
<circle cx="34" cy="78" r="1.4" fill="#fff"/><circle cx="62" cy="76" r="1.4" fill="#fff"/><circle cx="86" cy="78" r="1.4" fill="#fff"/><circle cx="48" cy="80" r="1.2" fill="#fff"/><circle cx="104" cy="82" r="1.2" fill="#fff"/>
{eye(52, 96, .5)}{eye(76, 96, .5)}{smile(64, 101, 3, .55)}{blush(44, 101, .5)}{blush(84, 101, .5)}
<circle cx="64" cy="54" r="15" fill="#D8203A" {W(2.8)}/><circle cx="58" cy="48" r="4" fill="#fff" opacity=".6"/>
{eye(58, 56, .45)}{eye(70, 56, .45)}{smile(64, 61, 2.6, .5)}
<path d="M64 40 Q66 26 78 18" fill="none" stroke="#3E8A2E" stroke-width="3" stroke-linecap="round"/>
<path d="M76 20 Q88 12 94 22 Q84 28 76 20Z" fill="#6CC24A" {W(2)}/>
<path d="M50 60 L38 72 M78 60 L90 72" {W(3)}/>''')

# 20. Osteria Mario (Vegas Кунцево) — канноли поёт в микрофон под неоновыми звёздами
I["cafe-osteria-vegas-kuntsevo"] = ("сицилийская трубочка канноли с кремом", "поёт в микрофон под неоновыми звёздами, как на сцене Вегаса", ("#3A1E5A", "#120A24"), f'''
<path d="M24 22 l4 9 10 1 -8 6 3 10 -9 -6 -9 6 3 -10 -8 -6 10 -1Z" fill="none" stroke="#FF5AC8" stroke-width="2.6" stroke-linejoin="round"/>
<path d="M102 14 l3 7 8 1 -6 5 2 8 -7 -5 -7 5 2 -8 -6 -5 8 -1Z" fill="none" stroke="#4AE8F0" stroke-width="2.4" stroke-linejoin="round"/>
<path d="M0 112 H128" stroke="#FFD24A" stroke-width="3" stroke-dasharray="2 6"/>
<path d="M30 92 L82 40 L98 56 L46 108Z" fill="#E8A040" {W(3)}/>
<path d="M44 82 L54 92 M56 70 L66 80 M68 58 L78 68" stroke="#B8742A" stroke-width="2.4"/>
<ellipse cx="90" cy="48" rx="13" ry="9" transform="rotate(45 90 48)" fill="#FFF8F0" {W(2.6)}/>
<ellipse cx="38" cy="100" rx="13" ry="9" transform="rotate(45 38 100)" fill="#FFF8F0" {W(2.6)}/>
<circle cx="88" cy="46" r="1.8" fill="#4A2A1A"/><circle cx="94" cy="50" r="1.8" fill="#4A2A1A"/><circle cx="36" cy="98" r="1.8" fill="#7AC84A"/><circle cx="42" cy="102" r="1.8" fill="#7AC84A"/>
{eye(58, 70, .5)}{eye(70, 82, .5)}
<ellipse cx="72" cy="94" rx="4" ry="5" fill="{O}"/>
<path d="M92 98 L104 84" stroke="#8A8AA0" stroke-width="4" stroke-linecap="round"/><circle cx="106" cy="80" r="7" fill="#C8C8D8" {W(2.4)}/>
<path d="M112 66 v8 a3 3 0 1 1 -2 -3" fill="none" stroke="#FF5AC8" stroke-width="2.2"/>''')

# 21. Чайхана «Сезам» — пахлава открывает пещеру с сокровищами
I["cafe-chaykhana-sezam"] = ("ромбик пахлавы с половинкой грецкого ореха", "отодвигает камень пещеры с сокровищами: «Сезам, откройся!»", ("#FFF6D8", "#B88A4A"), f'''
<path d="M60 128 V60 Q60 18 100 16 Q128 18 128 50 V128Z" fill="#8A6A4A" {W(3)}/>
<path d="M76 128 V70 Q76 40 100 38 Q120 40 120 66 V128Z" fill="#2A1E2A"/>
<circle cx="98" cy="96" r="16" fill="#FFD24A" opacity=".35"/>
<circle cx="92" cy="104" r="6" fill="#FFD24A" {W(2)}/><circle cx="104" cy="100" r="6" fill="#FFD24A" {W(2)}/><circle cx="98" cy="92" r="6" fill="#FFD24A" {W(2)}/>
{sparkle(108, 80, 4, "#FFF6C4")}{sparkle(86, 86, 3, "#FFF6C4")}
<ellipse cx="22" cy="104" rx="20" ry="16" fill="#A8947A" {W(3)}/><path d="M12 98 Q18 94 24 98" fill="none" stroke="#7A6A54" stroke-width="2"/>
<path d="M48 26 L78 64 L48 102 L18 64Z" fill="#E8B050" {W(3)}/>
<path d="M28 52 L68 52 M22 64 L74 64 M28 76 L68 76 M34 88 L62 88 M36 40 L60 40" stroke="#B8742A" stroke-width="2"/>
<path d="M40 38 Q48 28 56 38 Q48 44 40 38Z" fill="#8A5224" {W(1.8)}/>
{eye(40, 68, .5)}{eye(56, 68, .5)}{smile(48, 75, 3, .55)}
<path d="M68 80 Q74 70 78 74" fill="none" {W(3)}/><path d="M26 76 L18 88" {W(3)}/>
<path d="M58 98 Q60 106 56 110" fill="none" stroke="#FFC530" stroke-width="3" stroke-linecap="round"/>''')

# 22. Новорижская застава (КП «Ёлочка») — оладушек прячется под заснеженной еловой лапой
I["cafe-novorizhskaya-zastava"] = ("пышный оладушек с мёдом", "прячется от снегопада под заснеженной еловой лапой", ("#EAF4FF", "#7A9AD0"), f'''
<path d="M0 100 Q64 92 128 100 V128 H0Z" fill="#fff"/>
<path d="M-4 20 Q60 18 120 46" fill="none" stroke="#6A4A2A" stroke-width="5" stroke-linecap="round"/>
<path d="M10 20 L4 40 M24 20 L18 42 M38 21 L34 44 M52 22 L50 46 M66 25 L66 48 M80 29 L82 52 M94 34 L98 56 M106 40 L112 58 M10 20 L16 38 M24 20 L30 40 M38 21 L46 42 M52 22 L60 44 M66 25 L74 46 M80 29 L90 50 M94 34 L104 52" stroke="#2E7A4A" stroke-width="5" stroke-linecap="round"/>
<path d="M0 16 Q20 10 40 16 Q60 12 80 22 Q100 26 118 38" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/>
<ellipse cx="64" cy="88" rx="38" ry="18" fill="#E8A048" {W(3)}/>
<ellipse cx="64" cy="80" rx="34" ry="12" fill="#F4C068" {W(2.6)}/>
<path d="M50 78 Q64 70 80 78 Q82 86 76 84 Q74 92 70 86 Q64 90 60 84 Q52 86 50 78Z" fill="#FFB020" {W(2)}/>
{eye(52, 94, .5)}{eye(76, 94, .5)}{smile(64, 99, 3, .55)}{blush(44, 98, .5)}{blush(84, 98, .5)}
{sparkle(20, 64, 4)}{sparkle(108, 76, 3)}{sparkle(30, 86, 2.6)}{sparkle(98, 104, 3)}''')

# 23. MiMi (ТЦ «Сканди», Коммунарка) — скандинавская вафля-сердечко на беговых лыжах
I["cafe-mimi-kommunarka"] = ("скандинавская вафля-сердечко", "бежит на беговых лыжах по снежной лыжне", ("#F0F8FF", "#4A6AA0"), f'''
<path d="M0 96 Q64 84 128 92 V128 H0Z" fill="#F6FAFF"/>
<path d="M0 108 Q64 98 128 104 M0 114 Q64 104 128 110" fill="none" stroke="#C8D8F0" stroke-width="2"/>
<path d="M14 106 L104 92 Q110 90 112 86 M20 112 L110 98 Q116 96 118 92" fill="none" stroke="#E8304A" stroke-width="4" stroke-linecap="round"/>
<path d="M30 72 L22 104 M98 64 L108 98" stroke="#5A5A70" stroke-width="2.6" stroke-linecap="round"/>
<path d="M50 88 L44 104 M76 86 L84 100" {W(3.4)}/>
<path d="M64 92 C20 64 30 18 64 38 C98 18 108 64 64 92Z" fill="#F2B860" {W(3)}/>
<path d="M44 40 L82 80 M56 34 L90 68 M38 54 L70 86 M84 36 L46 80 M94 50 L60 86 M70 34 L38 66" stroke="#D08A38" stroke-width="2"/>
<path d="M44 66 L30 72 M84 62 L98 64" {W(3)}/>
{eye(54, 56, .5)}{eye(74, 56, .5)}{smile(64, 63, 3, .55)}{blush(46, 62, .5)}{blush(82, 62, .5)}
{sparkle(108, 22, 4)}{sparkle(20, 30, 3)}''')

# 24. Marani (Жуковка) — долма выглядывает из бочки винного погреба
I["cafe-marani-zhukovka"] = ("долма-рулетик в виноградном листе", "выглядывает из дубовой бочки в погребе-марани", ("#F6EEFF", "#6A3A7A"), f'''
<path d="M30 70 Q24 96 32 122 H96 Q104 96 98 70Z" fill="#A8683A" {W(3)}/>
<path d="M28 80 H100 M28 112 H100" stroke="{O}" stroke-width="5"/><path d="M28 80 H100 M28 112 H100" stroke="#8A8AA0" stroke-width="2.6"/>
<path d="M48 72 V122 M64 72 V122 M80 72 V122" stroke="#8A4E26" stroke-width="2"/>
<ellipse cx="64" cy="70" rx="34" ry="8" fill="#6A3E22" {W(3)}/>
<path d="M42 70 Q40 34 64 30 Q88 34 86 70Z" fill="#6C9A3A" {W(3)}/>
<path d="M64 32 V68 M64 44 L50 36 M64 44 L78 36 M64 56 L46 48 M64 56 L82 48" stroke="#4A7A2A" stroke-width="2"/>
<path d="M44 52 Q64 46 84 52" fill="none" stroke="#8ABA4A" stroke-width="2"/>
{eye(54, 58, .5)}{eye(74, 58, .5)}{smile(64, 64, 3, .5)}
<path d="M90 28 Q100 14 112 22 Q108 30 116 34 Q104 40 98 34 Q92 40 90 28Z" fill="#7CC24A" {W(2.2)}/>
<circle cx="18" cy="40" r="5" fill="#8A3A9A" {W(1.8)}/><circle cx="26" cy="44" r="5" fill="#8A3A9A" {W(1.8)}/><circle cx="21" cy="50" r="5" fill="#8A3A9A" {W(1.8)}/>''')

# 25. IL Патио (Одинцово) — тесто для пиццы подброшено и крутится в воздухе
I["cafe-ilpatio-odintsovo"] = ("тесто для пиццы с томатной спиралью", "взлетает и крутится над ладонями пиццайоло", ("#FFF2E6", "#E8603A"), f'''
<path d="M8 128 L22 98 Q30 90 40 96 L46 104 L32 128Z" fill="#fff" {W(2.6)}/><path d="M120 128 L106 98 Q98 90 88 96 L82 104 L96 128Z" fill="#fff" {W(2.6)}/>
<path d="M30 96 Q34 84 46 88 Q54 92 50 100 Q44 104 38 100Z" fill="#FFD0A8" {W(2.4)}/>
<path d="M98 96 Q94 84 82 88 Q74 92 78 100 Q84 104 90 100Z" fill="#FFD0A8" {W(2.4)}/>
<path d="M20 76 Q64 90 108 76" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="5 5"/>
<ellipse cx="64" cy="50" rx="48" ry="20" fill="#FFF0D0" {W(3)}/>
<ellipse cx="64" cy="48" rx="38" ry="14" fill="#E8402A"/>
<path d="M64 48 m-6 0 a6 3 0 1 1 12 0 a12 6 0 1 1 -24 0 a18 9 0 1 1 36 0" fill="none" stroke="#FF8A5A" stroke-width="2"/>
<path d="M90 40 Q96 34 100 40 Q96 44 90 40Z" fill="#4AB84A" {W(1.6)}/>
{eye(50, 52, .5)}{eye(78, 52, .5)}<path d="M60 58 Q64 62 68 58" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<circle cx="18" cy="30" r="3" fill="#fff"/><circle cx="110" cy="24" r="2.4" fill="#fff"/><circle cx="24" cy="16" r="2" fill="#fff"/>''')

# 26. Fish Point (Бузланово) — рыбка в кляре выглядывает из бумажного кулька с картошкой
I["cafe-fish-point-buzlanovo"] = ("рыбка в хрустящем кляре", "выглядывает из газетного кулька с картошкой фри", ("#E8F8FF", "#3A7AC8"), f'''
<rect x="34" y="22" width="9" height="40" rx="2" fill="#FFD24A" {W(2.2)} transform="rotate(-14 38 42)"/>
<rect x="84" y="20" width="9" height="42" rx="2" fill="#FFD24A" {W(2.2)} transform="rotate(16 88 42)"/>
<rect x="92" y="34" width="8" height="30" rx="2" fill="#FFC530" {W(2.2)} transform="rotate(26 96 50)"/>
<path d="M60 18 L50 6 L72 8Z" fill="#E8A048" {W(2.6)}/>
<path d="M44 66 Q40 26 62 20 Q84 26 80 66Z" fill="#E8A048" {W(3)}/>
<path d="M50 34 l4 3 M64 30 l3 4 M72 40 l3 3 M52 48 l4 2" stroke="#B8742A" stroke-width="2.4" stroke-linecap="round"/>
{eye(56, 46, .5)}{eye(70, 46, .5)}{smile(63, 53, 3, .5)}
<path d="M22 56 L106 56 L70 122 Q64 126 58 122Z" fill="#F6F2E8" {W(3)}/>
<path d="M32 66 H96 M38 76 H90 M44 86 H84 M50 96 H78" stroke="#A8A8B8" stroke-width="2"/>
<rect x="56" y="64" width="16" height="10" fill="#C8C8D8"/>''')

# 27. Ботаника на песке (Волкушинский карьер) — кекс-куличик лепит из песка своего двойника
I["cafe-botanika-lytkarino"] = ("кекс-куличик с белой глазурью и посыпкой", "на песчаном пляже карьера лепит формочкой своего песочного двойника", ("#E8FBFF", "#4AB0D8"), f'''
<path d="M0 92 Q64 80 128 92 V128 H0Z" fill="#F2D08A"/>
<circle cx="20" cy="104" r="1.6" fill="#D8B060"/><circle cx="40" cy="116" r="1.6" fill="#D8B060"/><circle cx="110" cy="114" r="1.6" fill="#D8B060"/>
<path d="M26 104 V58 Q26 52 32 52 H72 Q78 52 78 58 V104Z" fill="#D8964A" {W(3)}/>
<path d="M22 58 Q22 30 52 28 Q82 30 82 58 Q78 66 72 58 Q66 66 60 58 Q54 66 48 58 Q42 66 36 58 Q30 66 22 58Z" fill="#FFFAF4" {W(3)}/>
<rect x="38" y="38" width="5" height="2" rx="1" fill="#FF5A8A" transform="rotate(30 40 39)"/><rect x="58" y="34" width="5" height="2" rx="1" fill="#4AB8F0"/><rect x="66" y="46" width="5" height="2" rx="1" fill="#FFC530" transform="rotate(-30 68 47)"/><rect x="46" y="48" width="5" height="2" rx="1" fill="#6CC24A"/>
{eye(42, 78, .55)}{eye(62, 78, .55)}{smile(52, 86, 3.5, .65)}{blush(34, 86, .6)}{blush(70, 86, .6)}
<path d="M90 104 L94 82 H112 L116 104Z" fill="#E8C47A" {W(2.6)}/>
<path d="M92 82 Q103 72 114 82" fill="#E8C47A" {W(2.6)}/>
<circle cx="99" cy="92" r="1.6" fill="{O}"/><circle cx="107" cy="92" r="1.6" fill="{O}"/>
<path d="M78 74 L90 66" {W(3)}/>''')

# 28. Джи Джи Гриль (Сокольники) — сосиска-осьминожка машет ножками на решётке гриля
I["cafe-gi-gi-grill"] = ("сосиска-осьминожка с надрезанными ножками", "машет всеми ножками на горячей решётке гриля", ("#FFF0E8", "#C8462A"), f'''
<path d="M0 104 H128 V128 H0Z" fill="#3A3240"/>
<path d="M0 104 H128 M8 104 V128 M28 104 V128 M48 104 V128 M68 104 V128 M88 104 V128 M108 104 V128" stroke="#8A8AA0" stroke-width="3"/>
<path d="M20 116 Q24 108 28 116 M60 118 Q64 110 68 118 M98 116 Q102 108 106 116" fill="none" stroke="#FF8A2A" stroke-width="2.4"/>
<path d="M46 72 Q30 80 22 96 M52 78 Q42 92 40 104 M64 80 V104 M76 78 Q86 92 88 104 M82 72 Q98 80 106 96" fill="none" stroke="{O}" stroke-width="11" stroke-linecap="round"/>
<path d="M46 72 Q30 80 22 96 M52 78 Q42 92 40 104 M64 80 V104 M76 78 Q86 92 88 104 M82 72 Q98 80 106 96" fill="none" stroke="#E8604A" stroke-width="7" stroke-linecap="round"/>
<path d="M40 76 Q38 30 64 28 Q90 30 88 76Z" fill="#E8604A" {W(3)}/>
<path d="M48 40 L80 50 M44 54 L84 64" stroke="#8A2A1A" stroke-width="3.4" stroke-linecap="round"/>
{eye(54, 64, .55)}{eye(74, 64, .55)}{smile(64, 71, 3, .55)}
<path d="M24 50 Q20 40 26 32 M104 46 Q110 36 104 28" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

# 29. Fish Box (Захарово, пушкинские места) — пирог-рыбник в короне золотой рыбки
I["cafe-fishbox-zakharovo"] = ("пирог-рыбник в форме рыбки с узором-чешуёй", "в короне золотой рыбки выныривает из синего моря исполнить желание", ("#E8F6FF", "#2A5AB8"), f'''
<path d="M0 90 Q20 82 40 90 T80 90 T128 90 V128 H0Z" fill="#1E4AA8"/>
<path d="M10 104 Q22 98 34 104 M74 110 Q88 104 100 110" fill="none" stroke="#7AB0F0" stroke-width="2.6"/>
<path d="M98 62 L122 44 L120 84Z" fill="#E8A040" {W(3)}/>
<ellipse cx="60" cy="64" rx="42" ry="26" fill="#F0B050" {W(3)}/>
<path d="M60 44 Q66 52 60 60 Q66 68 60 76 Q66 84 60 88 M76 42 Q82 50 76 58 Q82 66 76 74 Q82 80 76 86 M44 44 Q50 52 44 60 Q50 68 44 76 Q50 82 44 86" fill="none" stroke="#C8842E" stroke-width="2.2"/>
<circle cx="30" cy="58" r="6" fill="#fff" {W(2)}/>{eye(30, 58, .5)}
<path d="M24 74 Q28 78 32 74" fill="none" {W(2.4)}/>{blush(22, 68, .5)}
<path d="M22 40 L20 24 L28 32 L34 20 L40 32 L48 24 L46 40Z" fill="#FFD24A" {W(2.4)}/>
{sparkle(98, 22, 6, "#FFE97A")}{sparkle(84, 12, 3, "#FFE97A")}{sparkle(112, 30, 3, "#FFE97A")}''')

# 30. Central Perk (Краснобогатырская) — черничный маффин на большом оранжевом диване
I["cafe-central-perk"] = ("черничный маффин в бумажной формочке", "уютно сидит на большом оранжевом диване в кофейне", ("#F2FFF0", "#5A9A6A"), f'''
<path d="M10 70 Q10 56 24 56 H104 Q118 56 118 70 V96 H10Z" fill="#E87A2A" {W(3)}/>
<rect x="4" y="76" width="20" height="34" rx="9" fill="#F08A3A" {W(3)}/><rect x="104" y="76" width="20" height="34" rx="9" fill="#F08A3A" {W(3)}/>
<rect x="18" y="92" width="92" height="18" rx="6" fill="#F08A3A" {W(3)}/>
<path d="M16 110 V120 M112 110 V120" {W(4)}/>
<path d="M44 92 L40 62 H88 L84 92Z" fill="#fff" {W(3)}/>
<path d="M48 64 L50 92 M56 64 L57 92 M64 64 V92 M72 64 L71 92 M80 64 L78 92" stroke="#A8C8F0" stroke-width="2"/>
<path d="M36 64 Q32 36 64 32 Q96 36 92 64Z" fill="#E8B068" {W(3)}/>
<circle cx="48" cy="46" r="3.6" fill="#3A3A9A"/><circle cx="70" cy="40" r="3.6" fill="#3A3A9A"/><circle cx="82" cy="54" r="3.6" fill="#3A3A9A"/><circle cx="58" cy="58" r="3" fill="#3A3A9A"/>
{eye(54, 76, .5)}{eye(74, 76, .5)}{smile(64, 83, 3, .55)}''')

# 31. Манана (Генерала Белова) — пирог лобиани катится колесом
I["cafe-manana-belova"] = ("круглый пирог лобиани с фасолью", "катится колесом по лужайке, раскинув руки и ноги", ("#F0FFF8", "#3AAA8A"), f'''
<path d="M0 108 Q64 100 128 108 V128 H0Z" fill="#6CC24A"/>
<path d="M14 64 Q8 56 14 48 M20 80 Q12 74 16 66" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M64 26 L54 6 M64 26 L76 6 M64 98 L50 116 M64 98 L80 116" stroke="{O}" stroke-width="5" stroke-linecap="round"/>
<circle cx="64" cy="62" r="38" fill="#D89A48" {W(3.2)}/>
<circle cx="64" cy="62" r="30" fill="#E8B060"/>
<path d="M50 40 Q64 36 78 40 M44 84 Q64 90 84 84" fill="none" stroke="#B8742A" stroke-width="2.6" stroke-linecap="round"/>
<ellipse cx="88" cy="50" rx="4" ry="2.6" fill="#8A3A2A" transform="rotate(30 88 50)"/><ellipse cx="40" cy="74" rx="4" ry="2.6" fill="#8A3A2A"/>
{eye(54, 60, .55)}{eye(74, 60, .55)}{smile(64, 69, 4, .7)}{blush(46, 68, .6)}{blush(82, 68, .6)}''')

# 32. Casa Bella (Одинцово) — лимонный тарт с меренгой прихорашивается у зеркальца
I["cafe-casa-bella-odintsovo"] = ("лимонный тарт с завитками меренги", "прихорашивается перед зеркальцем и пудрит носик сахарной пудрой", ("#FFF8FF", "#D88AE0"), f'''
<path d="M18 84 L24 108 H84 L90 84Z" fill="#E8B060" {W(3)}/>
<path d="M24 90 V104 M34 90 V106 M44 90 V106 M54 90 V106 M64 90 V106 M74 90 V106 M84 90 V104" stroke="#C8842E" stroke-width="2"/>
<ellipse cx="54" cy="84" rx="36" ry="8" fill="#FFE04A" {W(2.6)}/>
<path d="M22 82 Q24 66 32 70 Q34 52 44 62 Q50 44 58 60 Q66 46 70 62 Q80 54 80 70 Q88 66 86 82Z" fill="#FFF8EE" {W(2.6)}/>
<path d="M44 62 Q48 56 50 54 M58 60 Q60 54 62 52" fill="none" stroke="#E8A860" stroke-width="2.4" stroke-linecap="round"/>
{eye(44, 74, .5)}{eye(62, 74, .5)}{smile(53, 80, 3, .5)}
<ellipse cx="104" cy="56" rx="12" ry="16" fill="#E0F4FF" {W(2.8)}/><path d="M104 72 V96" stroke="{O}" stroke-width="7" stroke-linecap="round"/><path d="M104 72 V96" stroke="#FFC0E0" stroke-width="3.4" stroke-linecap="round"/>
<path d="M98 48 L104 42" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<circle cx="22" cy="40" r="11" fill="#FFB0D0" {W(2.4)}/><path d="M22 29 Q26 22 30 26" fill="none" {W(2)}/>
<circle cx="32" cy="54" r="1.6" fill="#fff"/><circle cx="36" cy="48" r="1.4" fill="#fff"/><circle cx="28" cy="58" r="1.2" fill="#fff"/>''')

# 33. IL Патио (ТЦ «Мегаполис») — кусок пиццы-небоскрёб среди домов мегаполиса
I["cafe-ilpatio-megapolis"] = ("пицца-небоскрёб: высокий кусок, поставленный остриём вверх", "возвышается среди многоэтажек мегаполиса, на шпиле листик базилика", ("#EEF0FF", "#5A62C8"), f'''
<rect x="4" y="60" width="24" height="70" fill="#8A94C8" {W(2.4)}/><rect x="100" y="48" width="26" height="80" fill="#7A84B8" {W(2.4)}/>
<rect x="24" y="78" width="18" height="50" fill="#A8B0D8" {W(2.4)}/><rect x="86" y="74" width="18" height="54" fill="#9AA2D0" {W(2.4)}/>
<path d="M10 68 h5 M18 68 h5 M10 78 h5 M18 78 h5 M10 88 h5 M106 56 h5 M114 56 h5 M106 66 h5 M114 66 h5 M106 76 h5 M114 76 h5" stroke="#FFE97A" stroke-width="4"/>
<path d="M64 12 L92 112 Q64 120 36 112Z" fill="#FFD45A" {W(3)}/>
<path d="M34 108 Q64 118 94 108 L96 116 Q64 128 32 116Z" fill="#E8A048" {W(3)}/>
<circle cx="62" cy="44" r="5" fill="#D8343A"/><circle cx="54" cy="94" r="5" fill="#D8343A"/><circle cx="76" cy="90" r="5" fill="#D8343A"/>
<path d="M64 12 Q60 2 52 4 Q56 12 64 12Z" fill="#4AB84A" {W(1.8)}/>
{eye(56, 66, .5)}{eye(72, 66, .5)}{smile(64, 74, 3, .55)}''')

# 34. Osteria Mario (БЦ «Академик») — макаронина-пенне в очках пишет мелом формулу
I["cafe-osteria-akademik"] = ("макаронина-пенне в круглых очках", "пишет мелом формулу на школьной доске, как академик", ("#FFFAF0", "#C8A050"), f'''
<rect x="6" y="14" width="116" height="62" rx="4" fill="#2E5A44" {W(3)}/>
<path d="M6 76 H122" stroke="#9A6234" stroke-width="5"/>
<text x="14" y="42" font-family="Arial" font-size="17" font-weight="bold" fill="#fff" opacity=".9">2+2=</text>
<path d="M66 34 Q72 26 78 34 Q84 42 90 34" fill="none" stroke="#fff" stroke-width="2.4" opacity=".9"/>
<path d="M14 58 Q30 50 46 58" fill="none" stroke="#fff" stroke-width="2" opacity=".6"/>
<path d="M40 122 L50 54 L82 44 L74 112Z" fill="#F4C25A" {W(3)}/>
<path d="M50 62 L76 54 M48 74 L78 66 M46 86 L78 78 M44 98 L77 90 M42 110 L75 102" stroke="#D89A38" stroke-width="2.2"/>
<circle cx="56" cy="78" r="7" fill="#fff" fill-opacity=".5" {W(2.2)}/><circle cx="72" cy="74" r="7" fill="#fff" fill-opacity=".5" {W(2.2)}/><path d="M63 77 L65 76" {W(2)}/>
<circle cx="56" cy="78" r="2.4" fill="{O}"/><circle cx="72" cy="74" r="2.4" fill="{O}"/>
<path d="M58 92 Q64 96 70 90" fill="none" {W(2.4)}/>
<path d="M78 70 L98 58" {W(3)}/><rect x="96" y="52" width="10" height="5" rx="2" fill="#fff" {W(1.6)} transform="rotate(-30 100 55)"/>''')

# 35. Vasilchuki Chaihona №1 (Каширское) — чебурек в тюбетейке приветствует гостей
I["cafe-chaihona-kashirskoe"] = ("пузатый чебурек-полумесяц с пузырьками", "в тюбетейке встречает гостей, приложив руку к сердцу", ("#FFFCEC", "#8AC83A"), f'''
<path d="M14 92 Q14 40 64 40 Q114 40 114 92Z" fill="#F0B858" {W(3.2)}/>
<path d="M16 92 Q20 86 24 92 Q28 86 32 92 Q36 86 40 92 Q44 86 48 92 Q52 86 56 92 Q60 86 64 92 Q68 86 72 92 Q76 86 80 92 Q84 86 88 92 Q92 86 96 92 Q100 86 104 92 Q108 86 112 92" fill="none" stroke="#C8842E" stroke-width="2.4"/>
<circle cx="34" cy="62" r="3" fill="#FFE0A0"/><circle cx="92" cy="58" r="3.6" fill="#FFE0A0"/><circle cx="80" cy="76" r="2.4" fill="#FFE0A0"/><circle cx="40" cy="80" r="2.4" fill="#FFE0A0"/>
<path d="M44 46 Q44 26 64 24 Q84 26 84 46Z" fill="#2A2238" {W(2.8)}/>
<path d="M52 40 l4 -6 l4 6Z M68 40 l4 -6 l4 6Z" fill="#fff"/><path d="M60 30 l4 -3 l4 3" fill="none" stroke="#fff" stroke-width="2"/>
{eye(52, 62, .55)}{eye(76, 62, .55)}{smile(64, 70, 4, .7)}{blush(44, 70, .6)}{blush(84, 70, .6)}
<path d="M88 96 Q86 108 74 106 Q66 104 70 96" fill="none" {W(3.4)}/>
<path d="M66 108 C62 102 56 104 58 108 C56 104 50 104 52 110 C54 114 62 118 66 108Z" fill="#E8304A" {W(1.6)}/>
<path d="M30 92 L28 112 M98 92 L100 112" {W(3.4)}/>''')

# 36. Чайхана (ТРЦ «Океания») — шашлычок в маске для ныряния плавает в аквариуме
I["cafe-chaykhana-okeaniya"] = ("шашлычок на шампуре с колечками лука", "плавает в аквариуме среди рыбок в маске для ныряния", ("#E0FFFF", "#1A8AB8"), f'''
<path d="M10 128 Q8 108 16 96 M20 128 Q24 112 18 100 M112 128 Q116 104 108 92" fill="none" stroke="#3AB86A" stroke-width="4" stroke-linecap="round"/>
<circle cx="102" cy="20" r="4" fill="none" stroke="#fff" stroke-width="2"/><circle cx="110" cy="34" r="3" fill="none" stroke="#fff" stroke-width="2"/><circle cx="96" cy="40" r="2.4" fill="none" stroke="#fff" stroke-width="2"/>
<path d="M88 100 Q96 92 104 100 Q96 108 88 100Z M104 100 L110 94 V106Z" fill="#FF9A3C" {W(2)}/>
<path d="M20 30 Q26 24 32 30 Q26 36 20 30Z M32 30 L38 25 V35Z" fill="#FFD24A" {W(2)}/>
<path d="M22 104 L106 36" stroke="{O}" stroke-width="6" stroke-linecap="round"/><path d="M22 104 L106 36" stroke="#C8D0DC" stroke-width="2.6" stroke-linecap="round"/>
<rect x="30" y="76" width="22" height="20" rx="7" fill="#9A4E2A" {W(2.6)} transform="rotate(-39 41 86)"/>
<ellipse cx="58" cy="72" rx="5" ry="11" fill="#FFF4FA" {W(2.2)} transform="rotate(-39 58 72)"/>
<rect x="62" y="44" width="28" height="26" rx="8" fill="#A8582E" {W(2.8)} transform="rotate(-39 76 57)"/>
<rect x="62" y="48" width="26" height="12" rx="5" fill="#BFF0FF" fill-opacity=".85" {W(2.2)} transform="rotate(-39 75 54)"/>
<circle cx="70" cy="58" r="2.2" fill="{O}"/><circle cx="80" cy="50" r="2.2" fill="{O}"/>
<path d="M74 66 Q80 66 82 60" fill="none" {W(2.2)}/>
<path d="M88 40 L96 24" {W(3)}/><path d="M96 24 v-8" stroke="#FFC530" stroke-width="4" stroke-linecap="round"/>''')

# 37. Джонджоли (Маршала Жукова) — эларджи прыгает через скакалку из тянущегося сыра
I["cafe-dzhondzholi-zhukova"] = ("горка эларджи — кукурузной каши с тянущимся сыром", "прыгает через скакалку из сырной нитки", ("#F6E8FF", "#9A5AD8"), f'''
<ellipse cx="64" cy="116" rx="30" ry="5" fill="#7A4AB8" opacity=".5"/>
<path d="M40 70 Q14 66 18 30 Q40 4 64 10 Q88 4 110 30 Q114 66 88 70" fill="none" stroke="#FFF2A0" stroke-width="5" stroke-linecap="round"/>
<path d="M30 102 L36 92 M98 102 L92 92" {W(3.4)}/>
<path d="M28 92 Q28 56 64 52 Q100 56 100 92 Q64 100 28 92Z" fill="#FFE04A" {W(3)}/>
<path d="M18 92 Q64 104 110 92 L104 102 Q64 112 24 102Z" fill="#C86A3A" {W(2.8)}/>
<path d="M50 60 Q46 50 40 70 M78 60 Q84 50 88 70" fill="none" stroke="#FFF6C4" stroke-width="3" stroke-linecap="round"/>
<path d="M36 78 L40 70 M92 78 L88 70" {W(3)}/>
{eye(54, 74, .55)}{eye(74, 74, .55)}{smile(64, 82, 3.5, .6)}{blush(46, 82, .6)}{blush(82, 82, .6)}''')

# 38. Vivezza (Мытищи, Лётная ул.) — панеттоне-лётчик в шлеме и очках
I["cafe-vivezza-mytishchi"] = ("купол панеттоне с изюмом в бумажной обёртке", "летит лётчиком в кожаном шлеме и очках, шарф развевается", ("#E8F4FF", "#3A8AE0"), f'''
<path d="M100 96 Q110 88 120 94 Q128 92 128 100 H96 Q94 96 100 96Z M8 40 Q16 32 26 38 Q34 36 34 44 H4 Q2 40 8 40Z" fill="#fff"/>
<path d="M10 70 H26 M4 82 H22 M12 94 H28" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M36 80 Q20 70 4 74 Q18 82 6 92 Q24 92 38 86Z" fill="#E8304A" {W(2.4)}/>
<path d="M34 80 L90 80 L88 112 Q64 118 40 112Z" fill="#C89A5A" {W(3)}/>
<path d="M44 82 V112 M56 82 V114 M68 82 V114 M80 82 V112" stroke="#A87A3A" stroke-width="1.6"/>
<path d="M30 82 Q28 30 64 28 Q100 30 98 82Z" fill="#E8A848" {W(3)}/>
<path d="M36 54 Q34 30 64 28 Q94 30 92 54 Q64 46 36 54Z" fill="#7A4A28" {W(2.8)}/>
<circle cx="50" cy="52" r="8" fill="#BFE8FF" {W(2.4)}/><circle cx="78" cy="52" r="8" fill="#BFE8FF" {W(2.4)}/><path d="M58 52 H70" {W(2.4)}/>
<circle cx="52" cy="54" r="2.4" fill="{O}"/><circle cx="80" cy="54" r="2.4" fill="{O}"/>
<path d="M58 68 Q64 73 70 68" fill="none" {W(2.4)}/>
<circle cx="42" cy="70" r="2" fill="#6A2A3A"/><circle cx="86" cy="66" r="2" fill="#6A2A3A"/><circle cx="64" cy="76" r="2" fill="#6A2A3A"/>
<path d="M98 66 L118 56 M30 66 L14 58" {W(3.4)}/>''')

# 39. СШОР по бадминтону (СК «Красный Октябрь») — волан с шоколадной головкой над кирпичной фабрикой
I["mgfso-badminton-krasny-oktyabr"] = ("волан для бадминтона с шоколадной головкой", "пикирует над красной кирпичной фабрикой с трубой", ("#FFF0E6", "#C84A3A"), f'''
<rect x="96" y="44" width="14" height="60" fill="#B8402E" {W(2.6)}/><path d="M96 52 H110" stroke="#fff" stroke-width="3"/>
<path d="M0 84 H128 V128 H0Z" fill="#B8402E" {W(2.6)}/>
<path d="M0 94 H128 M0 106 H128 M0 118 H128 M14 84 V94 M42 84 V94 M70 84 V94 M28 94 V106 M56 94 V106 M84 94 V106 M112 94 V106 M14 106 V118 M42 106 V118 M98 106 V118" stroke="#8A2A1E" stroke-width="1.6"/>
<rect x="12" y="96" width="14" height="12" fill="#FFE97A" {W(1.8)}/><rect x="56" y="98" width="14" height="12" fill="#FFE97A" {W(1.8)}/>
<path d="M100 34 Q106 26 104 18 M106 38 Q114 32 116 24" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
<g transform="rotate(-40 50 40)">
<path d="M42 54 L30 14 Q54 4 78 14 L66 54Z" fill="#fff" {W(3)}/>
<path d="M48 54 L42 12 M54 54 V8 M60 54 L66 12 M34 28 Q54 22 74 28" fill="none" stroke="#C8C8D8" stroke-width="2"/>
<path d="M40 52 H68 Q70 72 54 74 Q38 72 40 52Z" fill="#6B3A22" {W(3)}/>
</g>
{eye(57, 54, .45)}{eye(67, 58, .45)}
<path d="M8 22 Q20 18 26 28 M14 40 Q24 36 30 44" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

# 40. Баскетбольная школа «Хаски» (Люблино) — высокий баскетбольный кроссовок ведёт мяч
I["husky-basket-lyublino"] = ("высокий баскетбольный кроссовок с оранжевыми шнурками", "ведёт баскетбольный мяч носком, как дриблингом", ("#E8FFF4", "#2A9A7A"), f'''
<path d="M0 108 H128 V128 H0Z" fill="#E8B878"/><path d="M0 116 H128" stroke="#C8985A" stroke-width="2"/>
<path d="M26 98 V36 Q26 26 36 26 H58 Q64 26 64 34 V60 Q66 66 74 70 L96 78 Q108 82 108 92 V98Z" fill="#fff" {W(3)}/>
<path d="M22 98 H112 V106 Q112 110 106 110 H26 Q22 110 22 106Z" fill="#2A3A5A" {W(3)}/>
<path d="M34 76 Q60 62 96 86" fill="none" stroke="#FF8A1E" stroke-width="6" stroke-linecap="round"/>
<path d="M48 40 H62 M48 48 H62 M50 56 H64" stroke="#FF8A1E" stroke-width="3" stroke-linecap="round"/>
<path d="M26 36 Q40 30 46 40" fill="none" stroke="#2A3A5A" stroke-width="3"/>
{eye(36, 56, .5)}{eye(48, 64, .5)}<path d="M36 72 Q42 76 48 74" fill="none" {W(2.4)}/>
<circle cx="104" cy="48" r="15" fill="#F2892A" {W(3)}/>
<path d="M104 33 V63 M89 48 H119 M93 37 Q100 48 93 59 M115 37 Q108 48 115 59" fill="none" stroke="{O}" stroke-width="2"/>
<path d="M92 72 Q100 68 104 66 M86 66 Q94 60 96 58" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')


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
