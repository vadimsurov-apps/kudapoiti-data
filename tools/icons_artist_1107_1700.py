"""Робот «художник», 07.11 ~17:00 UTC: 30 иконок из похожих пар auto/icon-repeats.json
(киноэкраны с погодой, звери на надувном матрасе / на сёрфе / в пузыре, мячи с медалью, блюдо на машинке /
на батутике, пиксельные герои) и неверные якоря (рейнстик у бокса, ситар у самбо, диджериду у айкидо,
вувузела у футбола, хэндпан у балета, киви у оленьей фермы, скрипичный ключ у кавказских танцев).
Из каждой пары одну оставили, вторую придумали заново и нарисовали вручную: свой герой, сцена, ракурс, палитра.
Запуск из корня: python3 tools/icons_artist_1107_1700.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT

I = {}
SK = "#FFD8B8"


def limb(d, color=SK, w=6):
    return f'<path d="{d}" fill="none" {W(w)}/><path d="{d}" fill="none" stroke="{color}" stroke-width="{w-3.4:.1f}" stroke-linecap="round"/>'


def kidhead(x, y, r=11, hair="#6A3A1A", k=.42):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{SK}" {W(2.8)}/>'
            f'{eye(x-4, y+1, k)}{eye(x+4, y+1, k)}<path d="M{x-3} {y+5} Q{x} {y+8} {x+3} {y+5}" fill="none" {W(1.8)}/>'
            f'{blush(x-7, y+5, .3)}{blush(x+7, y+5, .3)}')


# 1. Кинотеатр «Октябрь» (Руза) — кинохлопушка щёлкает перед красным занавесом
I["ruza-oktyabr-cinema"] = ("кинохлопушка с чёрно-белыми полосками", "щёлкает «Мотор!» на фоне красного бархатного занавеса, из щели летят звёздочки", ("#FFE0D8", "#B02838"), f'''
<path d="M0 0 H128 V128 H0Z" fill="#C8303C"/>
<path d="M16 0 Q12 64 18 128 M36 0 Q32 64 38 128 M92 0 Q96 64 90 128 M112 0 Q116 64 110 128" stroke="#8E1A28" stroke-width="5" fill="none"/>
<path d="M30 54 H100 V104 Q100 108 96 108 H34 Q30 108 30 104Z" fill="#2E2A3A" {W(3)}/>
<path d="M30 54 H100" stroke="#fff" stroke-width="1.6"/>
<path d="M28 50 L96 30 L100 42 L32 62Z" fill="#fff" {W(3)}/>
<path d="M38 47 L46 59 M52 43 L60 55 M66 39 L74 51 M80 35 L88 47" stroke="#2E2A3A" stroke-width="6"/>
<path d="M28 50 L96 30 L100 42 L32 62Z" fill="none" {W(3)}/>
<circle cx="30" cy="56" r="3" fill="#C0C0C8" {W(1.6)}/>
<path d="M38 66 H92 M38 76 H92" stroke="#fff" stroke-width="1.4" opacity=".5"/>
{eye(54, 86, .6)}{eye(76, 86, .6)}{smile(65, 95, 5, .9)}{blush(46, 94, .5)}{blush(84, 94, .5)}
{sparkle(104, 26, 6, "#FFE070")}{sparkle(112, 44, 4, "#FFE070")}{sparkle(92, 16, 3.5, "#FFE070")}''')

# 2. «Китёнок» (Окская) — малыш в шапочке-китёнке плывёт брассом, из шапочки фонтанчик
I["kitenok-okskaya"] = ("малыш в плавательной шапочке в форме синего китёнка с хвостиком", "плывёт брассом по голубой воде, а из макушки шапочки бьёт фонтанчик", ("#E6FBFF", "#28A0C8"), f'''
<path d="M0 74 Q16 68 32 74 T64 74 T96 74 T128 74 V128 H0Z" fill="#5CC8EC" {W(2.6)}/>
<path d="M58 22 Q52 8 46 14 M64 20 V6 M70 22 Q76 8 82 14" fill="none" stroke="#9AE4FF" stroke-width="4" stroke-linecap="round"/>
<path d="M58 22 Q52 8 46 14 M64 20 V6 M70 22 Q76 8 82 14" fill="none" {W(1.4)}/>
<circle cx="46" cy="14" r="2.4" fill="#fff"/><circle cx="82" cy="14" r="2.4" fill="#fff"/><circle cx="64" cy="5" r="2.4" fill="#fff"/>
{limb("M40 74 Q26 66 18 76", SK, 7)}{limb("M88 74 Q102 66 110 76", SK, 7)}
<circle cx="64" cy="58" r="20" fill="{SK}" {W(3)}/>
<path d="M43 56 Q44 30 64 28 Q84 30 85 56 Q74 48 64 48 Q54 48 43 56Z" fill="#2E6AD8" {W(3)}/>
<path d="M82 40 Q94 30 98 22 Q90 22 86 30 Q84 22 76 24" fill="#2E6AD8" {W(2.6)}/>
<circle cx="56" cy="38" r="2.2" fill="{O}"/><path d="M52 44 Q56 46 60 44" fill="none" stroke="#fff" stroke-width="1.6"/>
{eye(57, 62, .55)}{eye(71, 62, .55)}{smile(64, 70, 4, .8)}{blush(50, 68, .45)}{blush(78, 68, .45)}
<path d="M40 76 Q64 84 88 76" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M14 100 Q22 96 30 100 M92 106 Q100 102 108 106" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 3. Оленья ферма Zoooleni — пятнистый оленёнок тянется к морковке на ладошке
I["zoooleni-ruza"] = ("пятнистый оленёнок с большими ушами", "на зелёной поляне фермы тянется носиком к морковке на детской ладошке", ("#F4FBE0", "#7AB04A"), f'''
<path d="M0 96 Q64 84 128 96 V128 H0Z" fill="#8ACB5A" {W(2.6)}/>
<path d="M44 74 L42 108 M54 76 L54 110 M76 76 L76 110 M86 74 L88 108" {W(6)}/>
<path d="M44 74 L42 108 M54 76 L54 110 M76 76 L76 110 M86 74 L88 108" stroke="#C88A50" stroke-width="3"/>
<ellipse cx="66" cy="72" rx="28" ry="15" fill="#C88A50" {W(3)}/>
<circle cx="54" cy="66" r="2.6" fill="#fff"/><circle cx="64" cy="64" r="2.6" fill="#fff"/><circle cx="74" cy="66" r="2.6" fill="#fff"/><circle cx="82" cy="72" r="2.2" fill="#fff"/>
<path d="M92 66 Q100 60 96 70" fill="#fff" {W(2)}/>
<path d="M46 66 Q40 52 38 44" fill="none" {W(10)}/><path d="M46 66 Q40 52 38 44" fill="none" stroke="#C88A50" stroke-width="6.6" stroke-linecap="round"/>
<path d="M26 30 Q12 22 14 34 Q18 40 28 38Z M44 28 Q56 18 56 30 Q52 38 42 36Z" fill="#C88A50" {W(2.6)}/>
<path d="M22 32 Q18 30 19 34 M46 30 Q52 28 51 32" fill="none" stroke="#F0B8A0" stroke-width="2.4" stroke-linecap="round"/>
<ellipse cx="34" cy="42" rx="12" ry="10" fill="#C88A50" {W(2.8)}/>
<path d="M22 46 Q16 48 18 52 Q24 54 28 50" fill="#E0B080" {W(2.4)}/><circle cx="18" cy="49" r="2.2" fill="{O}"/>
{eye(32, 40, .55)}{eye(41, 40, .55)}{blush(42, 47, .4)}
<path d="M14 58 L2 64" {W(6)}/><path d="M14 58 L2 64" stroke="#FF8A2A" stroke-width="3"/>
<path d="M14 58 L18 50 M14 58 L20 54" stroke="#4AA040" stroke-width="2.4" stroke-linecap="round"/>
<path d="M-4 66 Q6 58 14 64 Q12 74 -4 76Z" fill="{SK}" {W(2.6)}/>''')

# 4. RusVolley (Барболина) — мальчик-нападающий бьёт по мячу над сеткой
I["rusvolley-barbolina"] = ("мальчик-нападающий в синей майке с номером", "выпрыгнул высоко над волейбольной сеткой и в замахе бьёт по мячу", ("#FFF0E0", "#E07830"), f'''
<path d="M70 70 H128 V100 H70Z" fill="none"/>
<path d="M72 70 H128" stroke="#fff" stroke-width="5"/><path d="M72 70 H128" {W(1.6)}/>
<path d="M76 74 H128 M76 80 H128 M76 86 H128 M76 92 H128 M82 70 V98 M92 70 V98 M102 70 V98 M112 70 V98 M122 70 V98" stroke="{O}" stroke-width="1" opacity=".5"/>
<path d="M74 66 V128" {W(4.2)}/>
<circle cx="92" cy="24" r="12" fill="#fff" {W(2.8)}/><path d="M82 20 Q92 26 102 20 M90 12 Q96 24 90 36" fill="none" stroke="#2AA0E0" stroke-width="2.4"/><path d="M84 30 Q94 30 100 32" fill="none" stroke="#FFD23A" stroke-width="2.4"/>
{limb("M50 58 L64 42 L76 30", SK, 7)}{limb("M36 60 L22 48", SK, 7)}
{limb("M40 84 L30 100 L36 112", SK, 7)}{limb("M50 84 L58 98 L52 110", SK, 7)}
<path d="M32 54 Q32 48 44 46 Q56 48 56 56 L54 86 H36Z" fill="#2E5AD8" {W(3)}/>
<text x="45" y="76" font-family="Arial" font-weight="bold" font-size="13" fill="#fff" text-anchor="middle">7</text>
{kidhead(44, 36, 11, "#3A2A1A")}
<path d="M33 34 Q34 22 44 22 Q56 22 55 34 Q48 28 40 30Z" fill="#3A2A1A" {W(2)}/>
<path d="M78 40 L84 34 M74 46 L68 40" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 5. Energy (Красная Сосна) — девочка-хипхоперка в розовой толстовке
I["energy-dance-kompas"] = ("девочка-хипхоперка в мешковатой розовой толстовке и кепке козырьком вбок", "танцует хип-хоп: нога согнута вверх, руки в стороны, косички разлетаются", ("#2A2350", "#120E30"), f'''
<circle cx="24" cy="24" r="3" fill="#FFE04A"/><circle cx="104" cy="30" r="2.4" fill="#5AF0FF"/><circle cx="20" cy="92" r="2.4" fill="#FF6AD0"/>
<path d="M98 50 L106 46 L102 56 L110 54" fill="none" stroke="#FFE04A" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M14 54 L22 50 L18 60 L26 58" fill="none" stroke="#5AF0FF" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<ellipse cx="64" cy="118" rx="30" ry="5" fill="#FF6AD0" opacity=".45"/>
{limb("M54 82 L50 102 L54 116", SK, 7)}{limb("M72 80 L88 86 L82 70", SK, 7)}
<path d="M46 116 H60 Q62 112 56 110 H48Z" fill="#fff" {W(2.4)}/>
<path d="M78 66 L90 64 Q92 70 86 72Z" fill="#fff" {W(2.4)}/>
<path d="M48 82 Q60 90 76 82 L74 74 H50Z" fill="#3A3A5A" {W(2.8)}/>
{limb("M48 52 L32 46 L24 34", SK, 7)}{limb("M80 52 L94 60 L106 54", SK, 7)}
<path d="M44 76 Q40 54 50 48 H78 Q88 54 82 76Z" fill="#FF6AB8" {W(3)}/>
<path d="M58 48 Q64 56 70 48" fill="none" {W(2)}/><path d="M60 54 V64 M68 54 V64" stroke="#fff" stroke-width="2"/>
<path d="M50 30 Q38 32 34 42 Q42 40 48 36Z M78 30 Q90 32 94 42 Q86 40 80 36Z" fill="#6A3A1A" {W(2.2)}/>
<circle cx="64" cy="34" r="13" fill="{SK}" {W(2.8)}/>
<path d="M50 30 Q52 18 64 18 Q78 18 79 28 Z" fill="#5AE0F0" {W(2.4)}/><path d="M76 26 L92 24 Q92 30 78 30Z" fill="#5AE0F0" {W(2.4)}/>
{eye(59, 36, .48)}{eye(69, 36, .48)}<path d="M59 42 Q64 47 69 42" fill="none" {W(2)}/>{blush(54, 41, .35)}{blush(74, 41, .35)}''')

# 6. RusVolley (Ташкентский) — девочка подбросила мяч для верхней подачи
I["rusvolley-tashkentsky"] = ("девочка-волейболистка с высоким хвостиком в бирюзовой форме", "на лицевой линии зала подбросила мяч высоко над головой для верхней подачи", ("#E8FFF6", "#2AAA8A"), f'''
<path d="M0 104 H128 V128 H0Z" fill="#F0C890" {W(2.4)}/><path d="M0 108 H128" stroke="#fff" stroke-width="3"/>
<circle cx="76" cy="18" r="12" fill="#fff" {W(2.8)}/><path d="M66 14 Q76 20 86 14 M74 6 Q80 18 74 30" fill="none" stroke="#2A6AE0" stroke-width="2.4"/><path d="M68 24 Q78 24 84 26" fill="none" stroke="#FFC23A" stroke-width="2.4"/>
<path d="M72 36 Q76 34 80 36 M70 42 Q76 40 82 42" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" opacity=".8"/>
{limb("M58 92 L54 106", SK, 8)}{limb("M68 92 L74 106", SK, 8)}
<path d="M48 106 H58 V100 H52Z M70 106 H82 L78 100 H72Z" fill="#fff" {W(2.2)}/>
<path d="M50 94 H76 V84 H50Z" fill="#1A6A5A" {W(2.6)}/>
{limb("M72 62 L80 44 L78 32", SK, 7)}{limb("M52 62 L40 52 L36 40", SK, 7)}
<path d="M48 86 Q46 60 56 56 H70 Q80 60 78 86Z" fill="#2ACAA0" {W(3)}/>
<text x="63" y="78" font-family="Arial" font-weight="bold" font-size="12" fill="#fff" text-anchor="middle">3</text>
<path d="M70 36 Q86 32 92 44 Q84 46 74 44" fill="#E8B040" {W(2.4)}/>
{kidhead(63, 44, 12)}
<path d="M51 42 Q52 30 63 30 Q76 30 75 42 Q68 36 58 38Z" fill="#E8B040" {W(2.2)}/>''')

# 7. «Шторм» (Озёрная) — белая шапочка ватерполиста с ушными чашками-персонаж на волнах
I["shtorm-ozernaya"] = ("белая шапочка ватерполиста с синими ушными чашками и номером 7", "сама качается на штормовой волне бассейна и подмигивает, рядом подпрыгивает жёлтый мяч", ("#DDEBFF", "#1A3A8A"), f'''
<path d="M0 82 Q12 66 26 80 Q40 92 52 78 Q66 62 80 78 Q94 92 106 78 Q118 66 128 76 V128 H0Z" fill="#2A70D8" {W(2.6)}/>
<path d="M0 98 Q20 92 40 98 T80 98 T120 98" fill="none" stroke="#7AB8FF" stroke-width="3"/>
<path d="M22 80 Q26 72 30 78 M76 76 Q80 68 84 74" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M30 78 Q28 30 64 28 Q100 30 98 78 Q64 70 30 78Z" fill="#fff" {W(3.2)}/>
<path d="M64 28 V74" stroke="#D0D8E8" stroke-width="2"/><path d="M42 36 Q64 50 86 36" fill="none" stroke="#D0D8E8" stroke-width="2"/>
<circle cx="32" cy="66" r="11" fill="#2A5AD8" {W(2.8)}/><circle cx="96" cy="66" r="11" fill="#2A5AD8" {W(2.8)}/>
<path d="M27 62 H37 M27 66 H37 M27 70 H37 M91 62 H101 M91 66 H101 M91 70 H101" stroke="#9AB8FF" stroke-width="1.6"/>
<text x="64" y="50" font-family="Arial" font-weight="bold" font-size="14" fill="#2A5AD8" text-anchor="middle">7</text>
{eye(54, 60, .55)}<path d="M70 60 Q74 56 78 60" fill="none" {W(2.4)}/>{smile(64, 66, 5, .8)}
<circle cx="108" cy="36" r="11" fill="#FFD23A" {W(2.8)}/><path d="M98 34 Q108 40 118 34 M106 26 Q112 36 106 46" fill="none" stroke="#2A5AD8" stroke-width="2.2"/>
<path d="M104 54 Q108 58 112 54" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>''')

# 8. «Винзавод» — опрокинутая банка краски разлила радугу на холст
I["mc-vinzavod"] = ("жестяная банка краски с ручкой-дужкой", "опрокинулась на белом холсте и с хохотом разлила разноцветную радужную лужу", ("#F6F2EC", "#A8A0A0"), f'''
<path d="M10 94 L20 30 H112 L118 94Z" fill="#fff" {W(3)}/>
<path d="M14 94 H120 V100 H14Z" fill="#C8A070" {W(2.4)}/>
<path d="M40 86 Q30 70 46 62 Q58 56 70 66 Q84 60 96 68 Q110 78 98 88Z" fill="#FF5A5A" {W(2.6)}/>
<path d="M50 84 Q42 74 54 68 Q64 66 72 72 Q82 68 90 74 Q98 82 88 86Z" fill="#FFC83A"/>
<path d="M60 82 Q56 76 64 74 Q72 74 76 78 Q84 78 82 84Z" fill="#3AB8F0"/>
<circle cx="102" cy="52" r="4" fill="#9A5AE0" {W(2)}/><circle cx="92" cy="42" r="2.6" fill="#3ACA7A" {W(1.6)}/><circle cx="28" cy="56" r="3.2" fill="#FFC83A" {W(1.8)}/>
<g transform="rotate(-62 40 68)">
<path d="M22 50 H58 V86 Q58 92 40 92 Q22 92 22 86Z" fill="#7ACBE8" {W(3)}/>
<ellipse cx="40" cy="50" rx="18" ry="6" fill="#FF5A5A" {W(3)}/>
<path d="M22 54 Q40 44 58 54" fill="none" {W(2.4)}/>
<path d="M22 60 H58" stroke="#fff" stroke-width="2.4" opacity=".6"/>
</g>
{eye(36, 78, .5)}{eye(46, 72, .5)}<path d="M38 86 Q46 86 50 78" fill="none" {W(2.2)}/>{blush(32, 86, .4)}''')

# 9. Открытый бассейн в Тёплом Стане — надувной зелёный крокодил катает малыша
I["pool-teply-stan"] = ("надувной зелёный крокодил с ручками", "катает малыша в панамке по открытому бассейну под жарким солнцем", ("#FFF8D0", "#F0A830"), f'''
<circle cx="104" cy="22" r="13" fill="#FFE04A" {W(2.6)}/>
<path d="M104 2 V-2 M120 10 L124 6 M124 24 H128" stroke="#FFB020" stroke-width="3" stroke-linecap="round"/>
<path d="M0 78 H128 V128 H0Z" fill="#4AC0E8" {W(2.4)}/>
<path d="M0 82 H128" stroke="#9AE6FF" stroke-width="3"/>
<path d="M10 104 Q18 100 26 104 M98 112 Q106 108 114 112" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M14 86 Q14 70 34 70 H86 Q110 70 116 78 L120 84 Q110 92 86 92 H30 Q14 92 14 86Z" fill="#5AC84A" {W(3)}/>
<path d="M4 90 L14 82 L16 92Z" fill="#5AC84A" {W(2.6)}/>
<path d="M38 70 L42 64 L46 70 M50 70 L54 64 L58 70 M62 70 L66 64 L70 70" fill="#3AA03A" {W(2)}/>
<path d="M92 86 L96 90 L100 86 L104 90 L108 86 L112 88" fill="none" stroke="#fff" stroke-width="2"/>
<circle cx="96" cy="68" r="7" fill="#5AC84A" {W(2.6)}/>{eye(96, 68, .5)}
<path d="M34 92 Q60 98 90 92" fill="none" stroke="#C0F0A0" stroke-width="2.4"/>
{limb("M52 66 L44 74", SK, 6)}{limb("M72 66 L80 74", SK, 6)}
<path d="M52 72 Q50 54 62 52 Q74 54 72 72Z" fill="#FF7A5A" {W(2.8)}/>
<circle cx="62" cy="42" r="11" fill="{SK}" {W(2.8)}/>
<path d="M46 40 Q48 28 62 28 Q76 28 78 40Z" fill="#fff" {W(2.4)}/>
{eye(58, 44, .4)}{eye(66, 44, .4)}<path d="M58 48 Q62 52 66 48" fill="none" {W(1.8)}/>''')

# 10. Школа балета «Гармония» — мальчик-балерун в прыжке-шпагате
I["harmony-ballet-vargi"] = ("мальчик-балерун в белом трико и голубом колете", "парит в прыжке-шпагате высоко над тёмной сценой в луче прожектора", ("#E0E4FF", "#4A4AA8"), f'''
<path d="M40 -4 L88 -4 L120 128 H8Z" fill="#fff" opacity=".22"/>
<path d="M0 108 H128 V128 H0Z" fill="#8A5A3A" {W(2.4)}/><path d="M0 112 H128" stroke="#B07A50" stroke-width="2"/>
<ellipse cx="64" cy="110" rx="24" ry="4" fill="#3A2A50" opacity=".35"/>
<path d="M54 66 L32 74 L12 80" fill="none" {W(8)}/><path d="M54 66 L32 74 L12 80" fill="none" stroke="#fff" stroke-width="4.6" stroke-linecap="round"/>
<path d="M72 66 L96 72 L116 74" fill="none" {W(8)}/><path d="M72 66 L96 72 L116 74" fill="none" stroke="#fff" stroke-width="4.6" stroke-linecap="round"/>
<path d="M6 78 Q10 84 16 82 L14 76Z M114 70 Q122 72 120 78 L114 78Z" fill="#fff" {W(2)}/>
{limb("M52 44 L36 32 L26 22", SK, 6)}{limb("M76 44 L92 32 L102 22", SK, 6)}
<path d="M50 70 Q48 44 56 40 H72 Q80 44 78 70Z" fill="#7AB8FF" {W(3)}/>
<path d="M50 62 H78" stroke="#FFD24A" stroke-width="3"/><path d="M58 44 L64 52 L70 44" fill="none" stroke="#fff" stroke-width="2"/>
{kidhead(64, 28, 11)}
<path d="M53 26 Q54 14 64 14 Q75 14 75 26 Q68 20 58 22Z" fill="#E8B040" {W(2.2)}/>
{sparkle(22, 50, 4)}{sparkle(108, 46, 4)}{sparkle(30, 100, 3)}''')

# 11. «Шторм» («Спутник Арена») — мальчик-ватерполист ведёт мяч кролем
I["shtorm-sputnik-zelenograd"] = ("мальчик-ватерполист в красной шапочке с номером 5", "плывёт кролем по прозрачной зелёной воде и толкает жёлтый мяч носом перед собой", ("#E4FFF0", "#1A8A68"), f'''
<path d="M0 60 Q14 54 28 60 T56 60 T84 60 T112 60 T140 60 V128 H0Z" fill="#3ACAA0" {W(2.6)}/>
<path d="M0 84 Q20 78 40 84 T80 84 T120 84" fill="none" stroke="#A0F0D8" stroke-width="3"/>
<path d="M10 108 Q20 104 30 108 M84 112 Q94 108 104 112" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M34 72 Q20 64 26 50 Q32 40 40 46" fill="none" {W(7)}/><path d="M34 72 Q20 64 26 50 Q32 40 40 46" fill="none" stroke="{SK}" stroke-width="3.6" stroke-linecap="round"/>
<path d="M30 74 Q50 84 70 74 Q50 68 30 74Z" fill="{SK}" {W(2.6)}/>
<circle cx="76" cy="62" r="13" fill="{SK}" {W(2.8)}/>
<path d="M63 60 Q64 46 76 46 Q90 46 90 60 Q78 54 63 60Z" fill="#E8303A" {W(2.6)}/>
<circle cx="66" cy="62" r="4" fill="#E8303A" {W(2)}/>
<text x="78" y="57" font-family="Arial" font-weight="bold" font-size="9" fill="#fff" text-anchor="middle">5</text>
{eye(76, 64, .45)}{eye(84, 64, .45)}<path d="M78 70 Q82 72 86 70" fill="none" {W(1.8)}/>
<circle cx="104" cy="58" r="11" fill="#FFD23A" {W(2.8)}/><path d="M94 56 Q104 62 114 56 M102 48 Q108 58 102 68" fill="none" stroke="#2A5AD8" stroke-width="2.2"/>
<path d="M92 44 Q96 38 100 42 M112 40 Q116 36 118 42" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 12. «Гигант» — огромная напольная груша-великан, малыш бьёт её перчаткой
I["gigant-boxing-kids"] = ("огромная красная напольная боксёрская груша-великан", "добродушно смеётся, пока крошечный малыш в синих перчатках бьёт её изо всех сил", ("#FFF1E0", "#C8602A"), f'''
<path d="M0 112 H128 V128 H0Z" fill="#5A6A8A" {W(2.4)}/>
<path d="M76 0 V10" {W(4)}/><path d="M70 10 H82 V16 H70Z" fill="#9AA0B0" {W(2)}/>
<path d="M58 16 H94 Q104 16 104 30 V96 Q104 112 76 112 Q48 112 48 96 V30 Q48 16 58 16Z" fill="#E03A3A" {W(3.2)}/>
<path d="M50 30 H102 M50 92 H102" stroke="#A01E28" stroke-width="3"/>
<path d="M56 22 V88" stroke="#FF8080" stroke-width="3" stroke-linecap="round" opacity=".6"/>
{eye(68, 52, .65)}{eye(86, 52, .65)}<path d="M66 64 Q77 76 88 64Z" fill="#7A1A28" {W(2.4)}/>{blush(60, 62, .5)}{blush(94, 62, .5)}
<path d="M40 70 L44 66 M40 78 H46" stroke="{O}" stroke-width="2.4" stroke-linecap="round"/>
{limb("M22 96 L18 112", SK, 7)}{limb("M30 96 L34 112", SK, 7)}
<path d="M18 98 Q16 80 26 78 Q36 80 34 98Z" fill="#FFD24A" {W(2.6)}/>
{limb("M30 84 L40 76", SK, 6)}
<circle cx="42" cy="74" r="7" fill="#2E6AE0" {W(2.6)}/>
<circle cx="18" cy="86" r="6" fill="#2E6AE0" {W(2.4)}/>
{kidhead(26, 68, 9)}
<path d="M17 66 Q18 57 26 57 Q35 57 35 66 Q30 61 22 63Z" fill="#6A3A1A" {W(2)}/>''')

# 13. «Три Медведя» (Троицк) — медвежонок-самбист кланяется на ковре
I["tri-medvedya-troitsk"] = ("бурый медвежонок-самбист в красной куртке с поясом и в борцовках", "вежливо кланяется на синем борцовском ковре перед схваткой", ("#E2F0FF", "#3A68B8"), f'''
<ellipse cx="64" cy="112" rx="70" ry="22" fill="#2A5AC8" {W(2.6)}/><ellipse cx="64" cy="112" rx="48" ry="12" fill="none" stroke="#E83A3A" stroke-width="3"/>
<path d="M48 92 L46 110 M74 92 L78 110" {W(9)}/><path d="M48 92 L46 110 M74 92 L78 110" stroke="#8A5A30" stroke-width="5.6" stroke-linecap="round"/>
<path d="M40 112 H52 V106 H42Z M74 106 H86 L84 112 H74Z" fill="#E83A3A" {W(2.2)}/>
<path d="M40 96 Q36 66 54 58 L86 52 Q96 70 84 96Z" fill="#E83A3A" {W(3)}/>
<path d="M56 60 L70 80 L84 54" fill="none" stroke="#fff" stroke-width="2.4"/>
<path d="M40 84 H86" stroke="#fff" stroke-width="5"/><path d="M40 84 H86" stroke="{O}" stroke-width="1.4" opacity=".4"/>
<path d="M58 84 L52 96 M62 84 L64 96" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
<path d="M48 64 L40 82" {W(9)}/><path d="M48 64 L40 82" stroke="#E83A3A" stroke-width="5.6" stroke-linecap="round"/>
<circle cx="40" cy="84" r="5" fill="#8A5A30" {W(2.2)}/>
<g transform="rotate(28 84 42)">
<circle cx="72" cy="26" r="7" fill="#8A5A30" {W(2.6)}/><circle cx="96" cy="26" r="7" fill="#8A5A30" {W(2.6)}/>
<circle cx="72" cy="26" r="3" fill="#D8A070"/><circle cx="96" cy="26" r="3" fill="#D8A070"/>
<circle cx="84" cy="42" r="17" fill="#8A5A30" {W(3)}/>
<ellipse cx="84" cy="50" rx="8" ry="6" fill="#D8A070" {W(2)}/><ellipse cx="84" cy="47" rx="3" ry="2" fill="{O}"/>
<path d="M76 38 Q78 35 80 38 M88 38 Q90 35 92 38" fill="none" {W(2.4)}/>{blush(73, 46, .4)}{blush(95, 46, .4)}
</g>''')

# 14. Перевозников (Юрловский) — мальчик держит «крест» на гимнастических кольцах
I["perevoznikov-gym-yurlovsky"] = ("мальчик-гимнаст в белой майке и синих брючках", "держит «крест» на гимнастических кольцах, раскинув руки на тросах, ноги вместе", ("#FFF4FF", "#A85AC0"), f'''
<path d="M22 -4 V40 M106 -4 V40" stroke="#8A8A9A" stroke-width="3"/>
<circle cx="22" cy="46" r="8" fill="none" stroke="#C88A40" stroke-width="5"/><circle cx="22" cy="46" r="8" fill="none" {W(1.6)}/>
<circle cx="106" cy="46" r="8" fill="none" stroke="#C88A40" stroke-width="5"/><circle cx="106" cy="46" r="8" fill="none" {W(1.6)}/>
{limb("M50 52 L22 46", SK, 8)}{limb("M78 52 L106 46", SK, 8)}
<path d="M50 48 Q64 44 78 48 L76 74 H52Z" fill="#fff" {W(3)}/>
<path d="M52 72 H76 L74 112 Q70 116 66 112 L64 86 L62 112 Q58 116 54 112Z" fill="#2E4AB8" {W(3)}/>
<path d="M54 112 H62 V118 H52Z M66 112 H74 L76 118 H66Z" fill="#fff" {W(2.2)}/>
{kidhead(64, 34, 12)}
<path d="M52 32 Q53 20 64 20 Q76 20 76 32 Q70 26 60 28Z" fill="#2A1A10" {W(2.2)}/>
{sparkle(30, 86, 5)}{sparkle(100, 92, 4)}''')

# 15. Усадьба Трубецких — старая липа-великан с дуплом, из дупла выглядывает птенец
I["trubetskikh"] = ("старая раскидистая липа-великан с добрым лицом на стволе", "стоит посреди тихого усадебного парка, а из её дупла выглядывает пушистый птенец", ("#FAF6E0", "#A0B860"), f'''
<path d="M0 108 Q64 98 128 108 V128 H0Z" fill="#7AB850" {W(2.4)}/>
<path d="M50 112 Q54 84 52 62 H76 Q74 84 80 112Z" fill="#9A6A40" {W(3)}/>
<path d="M50 112 Q40 112 36 116 M80 112 Q90 112 94 116" {W(3)}/>
<path d="M58 70 Q60 84 58 100 M70 74 Q68 88 72 104" stroke="#7A4A28" stroke-width="2" fill="none"/>
<circle cx="64" cy="40" r="36" fill="#6ABA4A" {W(3)}/>
<circle cx="32" cy="54" r="18" fill="#6ABA4A" {W(3)}/><circle cx="96" cy="54" r="18" fill="#6ABA4A" {W(3)}/>
<circle cx="64" cy="40" r="35" fill="#6ABA4A"/><circle cx="33" cy="54" r="17" fill="#6ABA4A"/><circle cx="95" cy="54" r="17" fill="#6ABA4A"/>
<path d="M36 30 Q44 26 50 32 M78 24 Q86 22 92 28 M58 52 Q64 48 70 52" fill="none" stroke="#9AD870" stroke-width="2.6" stroke-linecap="round"/>
<ellipse cx="64" cy="92" rx="7" ry="9" fill="#4A2A18" {W(2.4)}/>
<circle cx="64" cy="90" r="6" fill="#E8D8C0" {W(2)}/>
<circle cx="62" cy="89" r="1.4" fill="{O}"/><circle cx="66" cy="89" r="1.4" fill="{O}"/><path d="M63 92 L64 94 L65 92Z" fill="#F0A030"/>
{eye(58, 74, .5)}{eye(70, 74, .5)}<path d="M60 80 Q64 83 68 80" fill="none" {W(2)}/>''')

# 16. «Про.Плыть» (Новогорск) — девочка в оранжевой шапочке летит в стартовом прыжке
I["proplyt-novogorsk"] = ("девочка-пловчиха в оранжевой шапочке и тёмных очках", "летит горизонтально над водой в стартовом прыжке, руки вытянуты вперёд «стрелочкой»", ("#FFF0E0", "#E06A3A"), f'''
<path d="M0 92 Q16 86 32 92 T64 92 T96 92 T128 92 V128 H0Z" fill="#3A9AE8" {W(2.6)}/>
<path d="M0 108 H128" stroke="#fff" stroke-width="3" stroke-dasharray="8 6"/>
<path d="M8 76 H30 V92 H8Z" fill="#fff" {W(2.6)}/><text x="19" y="88" font-family="Arial" font-weight="bold" font-size="11" fill="#E06A3A" text-anchor="middle">4</text>
<path d="M30 52 L18 46" {W(8)}/><path d="M30 52 L18 46" stroke="{SK}" stroke-width="4.6" stroke-linecap="round"/>
<path d="M30 58 L16 58" {W(8)}/><path d="M30 58 L16 58" stroke="{SK}" stroke-width="4.6" stroke-linecap="round"/>
<path d="M28 48 Q50 42 74 50 Q76 60 72 62 Q50 64 28 58Z" fill="#2A3A8A" {W(3)}/>
<path d="M74 50 L104 46 L118 42 M74 58 L106 56 L120 54" fill="none" {W(7)}/>
<path d="M74 50 L104 46 L118 42 M74 58 L106 56 L120 54" fill="none" stroke="{SK}" stroke-width="3.6" stroke-linecap="round"/>
<circle cx="88" cy="40" r="11" fill="{SK}" {W(2.8)}/>
<path d="M78 34 Q84 26 94 30 Q100 34 98 40 Q88 36 78 34Z" fill="#FF8A2A" {W(2.4)}/>
<path d="M82 40 H96" {W(4)}/><path d="M82 40 H96" stroke="#3A3A4A" stroke-width="2"/><circle cx="92" cy="41" r="3" fill="#3A3A4A" {W(1.4)}/>
<path d="M88 47 Q92 49 95 46" fill="none" {W(1.8)}/>
<path d="M60 100 Q64 94 68 100 M98 98 Q102 92 106 98" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 17. Vesna (Новая Рига) — муссовое пирожное-тюльпан распускается на блюдце
I["cafe-vesna-novaya-riga"] = ("розовое муссовое пирожное в форме тюльпана на зелёном листике", "распускается на белом блюдце, а вокруг кружат весенние лепестки", ("#F0FFF0", "#7ACB9A"), f'''
<ellipse cx="64" cy="104" rx="46" ry="12" fill="#fff" {W(3)}/><ellipse cx="64" cy="102" rx="30" ry="6" fill="none" stroke="#D8E0E8" stroke-width="2"/>
<path d="M64 98 Q40 98 30 84 Q44 80 60 92Z M64 98 Q88 98 98 84 Q84 80 68 92Z" fill="#5AB85A" {W(2.6)}/>
<path d="M36 40 Q34 82 64 96 Q94 82 92 40 Q84 50 78 40 Q72 26 64 22 Q56 26 50 40 Q44 50 36 40Z" fill="#FF8AB8" {W(3.2)}/>
<path d="M50 40 Q56 64 64 70 Q72 64 78 40" fill="none" stroke="#E8609A" stroke-width="2.4"/>
<path d="M42 50 Q46 70 56 82" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".6"/>
{eye(56, 66, .55)}{eye(72, 66, .55)}{smile(64, 74, 4, .8)}{blush(48, 74, .45)}{blush(80, 74, .45)}
<circle cx="64" cy="24" r="4" fill="#FFF0A0" {W(1.8)}/>
<path d="M14 30 Q20 24 24 32 Q18 36 14 30Z" fill="#FFC0D8" {W(1.6)}/>
<path d="M104 20 Q112 16 114 24 Q106 28 104 20Z" fill="#FFC0D8" {W(1.6)}/>
<path d="M108 56 Q116 54 116 62 Q108 64 108 56Z" fill="#FFC0D8" {W(1.6)}/>
<path d="M12 64 Q18 60 20 66 Q14 70 12 64Z" fill="#FFC0D8" {W(1.6)}/>''')

# 18. Ribambelle — картошка фри в красной коробочке съезжает с горки в шарики
I["cafe-ribambelle-serdtse-stolitsy"] = ("картошка фри в красной коробочке", "с визгом съезжает с жёлтой детской горки прямо в сухой бассейн с шариками", ("#FFF8D8", "#E8B020"), f'''
<path d="M14 18 H38 V30 H14Z" fill="#9A6AE0" {W(2.6)}/>
<path d="M18 30 V104 M34 30 V104" {W(3)}/>
<path d="M18 44 H34 M18 58 H34 M18 72 H34 M18 86 H34" {W(2.4)}/>
<path d="M30 28 Q70 40 98 92 L110 86 Q80 26 34 18Z" fill="#FFD23A" {W(3)}/>
<path d="M40 30 Q74 44 98 86" fill="none" stroke="#FFF0A0" stroke-width="3" stroke-linecap="round"/>
<path d="M0 100 Q64 88 128 100 V128 H0Z" fill="#fff" opacity=".4"/>
<circle cx="72" cy="112" r="7" fill="#FF5A5A" {W(2.2)}/><circle cx="88" cy="106" r="7" fill="#3AB0F0" {W(2.2)}/><circle cx="104" cy="112" r="7" fill="#5ACB5A" {W(2.2)}/>
<circle cx="118" cy="102" r="7" fill="#FFC83A" {W(2.2)}/><circle cx="58" cy="118" r="7" fill="#C86AE8" {W(2.2)}/><circle cx="94" cy="122" r="7" fill="#FF8A3A" {W(2.2)}/>
<g transform="rotate(32 62 62)">
<path d="M50 46 L52 28 M56 46 L56 24 M62 46 L62 22 M68 46 L69 26 M74 46 L76 30" {W(7)}/>
<path d="M50 46 L52 28 M56 46 L56 24 M62 46 L62 22 M68 46 L69 26 M74 46 L76 30" stroke="#FFD860" stroke-width="3.8" stroke-linecap="round"/>
<path d="M44 44 H82 L78 76 H48Z" fill="#E8303A" {W(3)}/>
<path d="M44 44 Q63 54 82 44" fill="none" {W(2.4)}/>
{eye(56, 60, .5)}{eye(70, 60, .5)}<ellipse cx="63" cy="68" rx="3.4" ry="3" fill="#7A1A28" {W(1.8)}/>
</g>''')

# 19. Музей русского импрессионизма — золотая рама с маковым полем в мазках
I["rusimp-museum"] = ("резная золотая музейная рама с лицом на нижней планке", "держит картину-пейзаж с маковым полем, написанным крупными мазками, и висит на бордовой стене", ("#F3E2E6", "#7A2A3A"), f'''
<path d="M64 4 L52 18 M64 4 L76 18" stroke="#C8A040" stroke-width="2"/><circle cx="64" cy="4" r="3" fill="#C8A040" {W(1.6)}/>
<path d="M18 18 H110 V104 H18Z" fill="#E8B83A" {W(3.2)}/>
<path d="M26 26 H102 V90 H26Z" fill="#BFE4FF" {W(2.4)}/>
<path d="M26 60 Q50 52 70 58 Q88 62 102 56 V90 H26Z" fill="#9ACB5A"/>
<path d="M30 40 h6 M42 34 h8 M60 38 h6 M80 32 h8 M90 42 h6" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<circle cx="88" cy="36" r="6" fill="#FFE070"/>
<circle cx="36" cy="70" r="4" fill="#E8303A"/><circle cx="50" cy="78" r="5" fill="#E8303A"/><circle cx="62" cy="68" r="3.4" fill="#E8303A"/>
<circle cx="76" cy="80" r="5" fill="#E8303A"/><circle cx="90" cy="70" r="4" fill="#E8303A"/><circle cx="42" cy="86" r="3" fill="#E8303A"/><circle cx="96" cy="84" r="3.4" fill="#E8303A"/>
<path d="M26 26 H102 V90 H26Z" fill="none" {W(2.4)}/>
<circle cx="18" cy="18" r="5" fill="#E8B83A" {W(2.4)}/><circle cx="110" cy="18" r="5" fill="#E8B83A" {W(2.4)}/>
<circle cx="18" cy="104" r="5" fill="#E8B83A" {W(2.4)}/><circle cx="110" cy="104" r="5" fill="#E8B83A" {W(2.4)}/>
{eye(54, 97, .4)}{eye(74, 97, .4)}<path d="M60 100 Q64 103 68 100" fill="none" {W(1.8)}/>
<ellipse cx="64" cy="118" rx="22" ry="4" fill="#5A1A28" opacity=".3"/>''')

# 20. Pixel Quest (Одинцово) — девочка прыгает по светящимся квадратам пола
I["pixel-quest-odintsovo"] = ("девочка в розовых кедах и полосатой футболке", "в прыжке перескакивает с одного светящегося квадрата игрового пола на другой", ("#2A1A40", "#0E0820"), f'''
<path d="M-10 92 L138 92 L150 128 H-22Z" fill="#1A1430"/>
<path d="M4 96 H32 L28 108 H-2Z" fill="#FF4A8A" {W(2)}/><path d="M36 96 H62 V108 H32Z" fill="#3A3460" {W(2)}/>
<path d="M66 96 H92 L96 108 H66Z" fill="#3A3460" {W(2)}/><path d="M96 96 H124 L130 108 H100Z" fill="#4AE0F0" {W(2)}/>
<path d="M-4 112 H28 L24 126 H-10Z" fill="#3A3460" {W(2)}/><path d="M32 112 H62 V126 H28Z" fill="#FFE04A" {W(2)}/>
<path d="M66 112 H96 L100 126 H66Z" fill="#3A3460" {W(2)}/><path d="M100 112 H132 L138 126 H104Z" fill="#7AF05A" {W(2)}/>
<path d="M4 94 L20 82 M120 94 L104 82" stroke="#FF4A8A" stroke-width="0"/>
<ellipse cx="64" cy="100" rx="16" ry="3" fill="#000" opacity=".4"/>
{limb("M58 66 L48 74 L46 84", SK, 7)}{limb("M70 66 L84 70 L92 62", SK, 7)}
<path d="M40 84 H52 Q54 90 48 90 H40Z" fill="#FF6AB0" {W(2.2)}/><path d="M88 58 L98 56 Q100 62 94 64Z" fill="#FF6AB0" {W(2.2)}/>
<path d="M54 68 H74 V60 H54Z" fill="#3A5AD8" {W(2.4)}/>
{limb("M54 44 L40 34 L34 22", SK, 6)}{limb("M74 44 L88 36 L96 26", SK, 6)}
<path d="M52 62 Q50 42 58 40 H70 Q78 42 76 62Z" fill="#fff" {W(3)}/>
<path d="M52 48 H76 M52 55 H76" stroke="#FF4A8A" stroke-width="3"/>
<path d="M52 24 Q44 26 42 36 Q48 32 52 30Z M76 24 Q84 26 86 36 Q80 32 76 30Z" fill="#2A1A10" {W(2)}/>
{kidhead(64, 28, 11)}
<path d="M53 26 Q54 15 64 15 Q75 15 75 26 Q68 20 58 22Z" fill="#2A1A10" {W(2.2)}/>
{sparkle(20, 40, 4, "#4AE0F0")}{sparkle(108, 46, 4, "#FFE04A")}{sparkle(30, 70, 3, "#FF4A8A")}''')

# 21. «Арена-Сокол» — бутса с шипами пинает мяч на газоне стадиона
I["ms-arena-sokol"] = ("оранжевая футбольная бутса-персонаж с белыми шипами", "лихо пинает чёрно-белый мяч на полосатом газоне стадиона", ("#E8FFE0", "#3A9A3A"), f'''
<path d="M0 0 H128 V128 H0Z" fill="none"/>
<path d="M0 88 H128 V128 H0Z" fill="#5AB84A"/><path d="M0 100 H128 V112 H0Z" fill="#6ACB5A"/>
<path d="M0 88 H128" {W(2.4)}/>
<g transform="rotate(-18 50 66)">
<path d="M18 52 Q18 40 30 40 H44 Q50 40 52 46 L58 56 Q80 56 88 64 Q92 72 84 76 H22 Q16 76 16 68Z" fill="#FF8A2A" {W(3.2)}/>
<path d="M16 72 H86" stroke="#fff" stroke-width="4"/><path d="M16 74 Q50 80 88 72" fill="none" {W(2.4)}/>
<path d="M26 78 V84 M38 78 V84 M56 78 V84 M70 78 V84 M80 78 V84" {W(5)}/>
<path d="M26 78 V84 M38 78 V84 M56 78 V84 M70 78 V84 M80 78 V84" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M46 48 L54 44 M50 52 L58 48 M54 56 L62 52" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M24 56 L36 52 L30 62" fill="none" stroke="#FFE04A" stroke-width="3" stroke-linecap="round"/>
{eye(66, 64, .5)}{eye(76, 64, .5)}<path d="M66 70 Q72 74 78 70" fill="none" {W(2)}/>
</g>
<circle cx="102" cy="58" r="15" fill="#fff" {W(3)}/>
<path d="M102 50 L109 55 L106 63 H98 L95 55Z" fill="{O}"/><path d="M89 52 L95 55 M109 55 L115 52 M106 63 L110 70 M98 63 L94 70 M102 50 V44" {W(2)}/>
<path d="M84 46 L90 50 M82 58 H88 M84 70 L90 66" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

# 22. Айкидо Байдера — мальчик в широкой хакаме в стойке, руки вытянуты вперёд
I["bayder-aikido-babushkina"] = ("мальчик-айкидока в белом ги и широкой тёмно-синей хакаме", "стоит в стойке на зелёном татами, мягко вытянув обе руки вперёд-в стороны, хакама развевается", ("#FFF6EA", "#B89A6A"), f'''
<path d="M0 104 H128 V128 H0Z" fill="#7ABA5A" {W(2.4)}/><path d="M42 104 V128 M86 104 V128" stroke="#5A9A3A" stroke-width="2"/>
<path d="M36 112 H50 V106 H38Z M78 106 H92 L90 112 H78Z" fill="{SK}" {W(2)}/>
<path d="M50 66 H78 L100 108 Q84 112 72 106 L64 82 L56 106 Q44 112 28 108Z" fill="#23306A" {W(3.2)}/>
<path d="M58 70 L48 104 M70 70 L82 104 M64 82 V70" stroke="#4A5A9A" stroke-width="2"/>
<path d="M48 70 Q46 46 56 42 H72 Q82 46 80 70Z" fill="#fff" {W(3)}/>
<path d="M58 42 L64 58 L70 42" fill="none" {W(2)}/>
<path d="M48 66 H80" stroke="#23306A" stroke-width="5"/>
<path d="M52 48 L32 56 L16 54" fill="none" {W(9)}/><path d="M52 48 L32 56 L16 54" fill="none" stroke="#fff" stroke-width="5.6" stroke-linecap="round"/>
<path d="M76 48 L96 44 L112 36" fill="none" {W(9)}/><path d="M76 48 L96 44 L112 36" fill="none" stroke="#fff" stroke-width="5.6" stroke-linecap="round"/>
<circle cx="14" cy="54" r="4.6" fill="{SK}" {W(2)}/><circle cx="114" cy="35" r="4.6" fill="{SK}" {W(2)}/>
{kidhead(64, 30, 12)}
<path d="M52 28 Q53 16 64 16 Q76 16 76 28 Q70 22 60 24Z" fill="#1A1010" {W(2.2)}/>
<path d="M20 86 Q14 92 18 98 M108 82 Q114 88 110 94" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

# 23. Warpoint (Раменки) — VR-шлем-персонаж парит среди неоновых планет
I["warpoint-vinnitskaya"] = ("белый VR-шлем-персонаж с синим светящимся визором и ремешком", "парит в невесомости среди неоновых планет виртуального космоса", ("#3A2A8A", "#0A0A2A"), f'''
<circle cx="22" cy="30" r="10" fill="#FF6AD0" {W(2.4)}/><path d="M8 34 Q22 22 36 26" fill="none" stroke="#FFB0F0" stroke-width="2.4"/>
<circle cx="108" cy="98" r="12" fill="#5AF0B0" {W(2.4)}/><path d="M94 96 Q108 108 122 98" fill="none" stroke="#B0FFE0" stroke-width="2.4"/>
<circle cx="104" cy="24" r="2" fill="#fff"/><circle cx="16" cy="96" r="2" fill="#fff"/><circle cx="40" cy="112" r="1.6" fill="#fff"/><circle cx="116" cy="60" r="1.6" fill="#fff"/>
<path d="M30 48 Q30 32 64 32 Q98 32 98 48 Q104 44 104 56 V76 Q104 90 92 90 H36 Q24 90 24 76 V56 Q24 44 30 48Z" fill="none"/>
<path d="M20 60 Q64 20 108 60" fill="none" {W(6)}/><path d="M20 60 Q64 20 108 60" fill="none" stroke="#5A5A7A" stroke-width="2.6"/>
<path d="M26 52 Q26 42 40 42 H88 Q102 42 102 52 V80 Q102 90 90 90 H38 Q26 90 26 80Z" fill="#F4F4FF" {W(3.2)}/>
<path d="M32 54 Q32 50 38 50 H90 Q96 50 96 54 V76 Q96 82 90 82 H72 L64 74 L56 82 H38 Q32 82 32 76Z" fill="#2A3AE0" {W(2.6)}/>
<path d="M36 56 Q48 54 54 60" fill="none" stroke="#9AD8FF" stroke-width="2.6" stroke-linecap="round"/>
<ellipse cx="50" cy="66" rx="5" ry="6" fill="#7AF0FF"/><ellipse cx="78" cy="66" rx="5" ry="6" fill="#7AF0FF"/>
<circle cx="48" cy="64" r="1.8" fill="#fff"/><circle cx="76" cy="64" r="1.8" fill="#fff"/>
<path d="M58 98 Q64 102 70 98" fill="none" {W(2.2)}/>
{sparkle(64, 16, 5, "#FFE04A")}{sparkle(14, 66, 4, "#7AF0FF")}''')

# 24. Warpoint (Авиапарк) — два VR-контроллера дают «пять» в неоновой сетке
I["warpoint-aviapark"] = ("пара VR-контроллеров с подсвеченными кольцами — левый и правый", "дают друг другу «пять» над неоновой сеткой-полом виртуальной арены, искры летят", ("#FFE0F4", "#D02A8A"), f'''
<path d="M-10 128 L40 84 H88 L138 128Z" fill="#3A0A3A"/>
<path d="M40 84 L20 128 M56 84 L48 128 M72 84 L80 128 M88 84 L108 128 M28 96 H100 M14 110 H114" stroke="#FF8AE0" stroke-width="1.6"/>
<g transform="rotate(24 40 60)">
<circle cx="40" cy="34" r="16" fill="none" stroke="#5AF0FF" stroke-width="7"/><circle cx="40" cy="34" r="16" fill="none" {W(2.4)}/>
<path d="M32 46 H48 L46 92 Q40 98 34 92Z" fill="#2E2A3A" {W(3)}/>
<circle cx="40" cy="58" r="4" fill="#5AF0FF" {W(1.6)}/>
{eye(36, 72, .4)}{eye(44, 72, .4)}<path d="M37 78 Q40 80 43 78" fill="none" stroke="#fff" stroke-width="1.6"/>
</g>
<g transform="rotate(-24 88 60)">
<circle cx="88" cy="34" r="16" fill="none" stroke="#FFE04A" stroke-width="7"/><circle cx="88" cy="34" r="16" fill="none" {W(2.4)}/>
<path d="M80 46 H96 L94 92 Q88 98 82 92Z" fill="#2E2A3A" {W(3)}/>
<circle cx="88" cy="58" r="4" fill="#FFE04A" {W(1.6)}/>
{eye(84, 72, .4)}{eye(92, 72, .4)}<path d="M85 78 Q88 80 91 78" fill="none" stroke="#fff" stroke-width="1.6"/>
</g>
{sparkle(64, 18, 8)}{sparkle(52, 8, 3.5)}{sparkle(78, 8, 3.5)}''')

# 25. Покровское-Стрешнево — пёстрый дятел стучит по сосне
I["pokrovskoe-streshnevo"] = ("пёстрый дятел в красной шапочке", "уцепился за толстый ствол сосны в лесопарке и звонко стучит клювом, летят щепочки", ("#EAF6FF", "#6AA8D0"), f'''
<path d="M70 -4 H104 V132 H70Z" fill="#C8783A" {W(3)}/>
<path d="M76 10 Q80 16 76 22 M96 40 Q92 46 96 52 M78 70 Q82 76 78 82 M98 96 Q94 102 98 108" fill="none" stroke="#8A4A1A" stroke-width="2.4"/>
<path d="M104 30 Q120 22 128 26 M104 86 Q118 82 130 88" {W(3)}/>
<path d="M112 14 L118 28 L126 18 M120 76 L124 90 L132 80" fill="none" stroke="#2A7A3A" stroke-width="3" stroke-linecap="round"/>
<path d="M62 54 L70 52" stroke="#E8C080" stroke-width="3" stroke-linecap="round"/>
<path d="M58 44 L62 40 M58 62 L62 66" stroke="#E8C080" stroke-width="3" stroke-linecap="round"/>
<path d="M42 98 L30 118 L44 108 L46 120 L52 100Z" fill="#2A2A3A" {W(2.4)}/>
<path d="M30 64 Q26 90 44 102 Q60 104 64 86 Q66 64 52 54Z" fill="#2A2A3A" {W(3)}/>
<path d="M38 72 h4 M36 82 h4 M42 90 h4 M48 78 h4" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M50 96 Q46 104 52 106 L58 94Z" fill="#E8303A" {W(2)}/>
<circle cx="50" cy="52" r="14" fill="#fff" {W(3)}/>
<path d="M38 46 Q40 36 52 36 Q62 38 62 46 Q52 42 38 46Z" fill="#E8303A" {W(2.4)}/>
<path d="M62 52 L74 54 L62 58Z" fill="#5A5A6A" {W(2.4)}/>
{eye(52, 52, .5)}<path d="M40 58 Q44 62 48 60" fill="none" stroke="#2A2A3A" stroke-width="3" stroke-linecap="round"/>{blush(46, 60, .35)}
<path d="M64 64 L72 62 M66 70 L74 72" stroke="#fff" stroke-width="2" stroke-linecap="round"/>''')

# 26. Гжельский фарфоровый завод — кисточка расписывает белую чашку синим цветком
I["tour-gzhel"] = ("белая фарфоровая чашка с блюдцем", "улыбается, пока тонкая кисточка расписывает её бок синим гжельским цветком", ("#F0F4FF", "#5A7AC8"), f'''
<ellipse cx="58" cy="104" rx="44" ry="10" fill="#fff" {W(3)}/>
<path d="M18 104 Q58 114 98 104" fill="none" stroke="#2A4AB8" stroke-width="2.4"/>
<path d="M92 56 Q110 56 110 70 Q110 84 90 84" fill="none" {W(8)}/><path d="M92 56 Q110 56 110 70 Q110 84 90 84" fill="none" stroke="#fff" stroke-width="4.6"/>
<path d="M22 46 H94 Q94 88 74 98 H42 Q22 88 22 46Z" fill="#fff" {W(3.2)}/>
<ellipse cx="58" cy="46" rx="36" ry="7" fill="#F0F4FF" {W(2.8)}/>
<path d="M24 54 Q58 60 92 54" fill="none" stroke="#2A4AB8" stroke-width="3"/>
<path d="M40 76 Q34 68 40 64 Q44 68 40 76Z M40 76 Q30 78 30 72 Q36 70 40 76Z M40 76 Q46 82 42 86 Q38 82 40 76Z" fill="#2A4AB8"/>
<circle cx="40" cy="76" r="2.4" fill="#2A4AB8"/><path d="M44 80 Q50 84 54 80" fill="none" stroke="#2A4AB8" stroke-width="2"/>
{eye(64, 70, .5)}{eye(78, 70, .5)}{smile(71, 78, 4, .8)}{blush(58, 78, .4)}{blush(86, 78, .4)}
<path d="M48 82 L90 14" {W(6)}/><path d="M48 82 L90 14" stroke="#E8B860" stroke-width="3" stroke-linecap="round"/>
<path d="M90 14 L100 0" {W(6)}/><path d="M90 14 L100 0" stroke="#B8402A" stroke-width="3" stroke-linecap="round"/>
<path d="M50 78 L46 84 L44 88 L48 86Z" fill="#2A4AB8" {W(1.8)}/>
<path d="M54 76 L58 72" stroke="#C0C0C8" stroke-width="3"/>''')

# 27. Пронто (Подольск) — миска макарон-ракушек, одна ракушка выглядывает как рак-отшельник
I["cafe-pronto-podolsk"] = ("белая миска пасты-ракушек конкилье в томатном соусе", "одна весёлая ракушка выглянула из горки пасты и машет листиком базилика, как флажком", ("#FFF2E0", "#C83A2A"), f'''
<path d="M10 70 Q14 110 64 112 Q114 110 118 70Z" fill="#fff" {W(3.2)}/>
<path d="M18 82 Q64 92 110 82" fill="none" stroke="#2A8A4A" stroke-width="3"/><path d="M22 92 Q64 102 106 92" fill="none" stroke="#E8303A" stroke-width="3"/>
<path d="M12 70 Q20 44 44 44 Q54 34 70 38 Q92 34 104 50 Q118 56 116 70Z" fill="#E8503A" {W(3)}/>
<path d="M24 64 Q22 54 32 52 Q40 54 38 62Z" fill="#FFD480" {W(2.2)}/><path d="M28 62 Q27 56 33 55" fill="none" stroke="#E8A040" stroke-width="1.6"/>
<path d="M92 62 Q90 52 100 50 Q108 52 106 60Z" fill="#FFD480" {W(2.2)}/><path d="M96 60 Q95 54 101 53" fill="none" stroke="#E8A040" stroke-width="1.6"/>
<path d="M44 66 Q42 58 50 56 Q56 58 54 64Z" fill="#FFD480" {W(2)}/><path d="M76 66 Q74 58 82 56 Q88 58 86 64Z" fill="#FFD480" {W(2)}/>
<path d="M50 54 Q46 30 64 24 Q84 22 84 40 Q80 54 64 56Z" fill="#FFD480" {W(3)}/>
<path d="M56 30 Q60 44 58 54 M66 26 Q70 40 68 56 M76 28 Q78 40 76 52" fill="none" stroke="#E8A040" stroke-width="2"/>
<ellipse cx="72" cy="46" rx="9" ry="7" fill="#C8582A" {W(2)}/>
{eye(68, 45, .45)}{eye(76, 45, .45)}<path d="M69 50 Q72 52 75 50" fill="none" {W(1.6)}/>
<path d="M86 40 L98 22" {W(3)}/><path d="M98 22 Q108 10 112 20 Q106 30 98 22Z" fill="#4AB04A" {W(2.4)}/><path d="M99 22 L108 16" stroke="#2A7A2A" stroke-width="1.6"/>
<path d="M30 30 Q34 24 30 18 M44 24 Q48 18 44 12" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" opacity=".8"/>''')

# 28. Япоша (Королёв) — креветка темпура играет в приставку
I["cafe-yaposha-korolev"] = ("хрустящая креветка темпура с розовым хвостиком", "сидит на подушке в детской комнате и азартно жмёт кнопки игрового джойстика", ("#E8F0FF", "#5A6AE0"), f'''
<ellipse cx="64" cy="112" rx="44" ry="10" fill="#FFB84A" {W(2.8)}/><path d="M28 110 Q64 118 100 110" fill="none" stroke="#FFE0A0" stroke-width="2.4"/>
<path d="M92 34 L112 20 L118 34 L104 40 L116 50 L98 50Z" fill="#FF7A6A" {W(2.8)}/>
<path d="M100 36 L110 28 M100 46 L112 46" stroke="#FFC0B0" stroke-width="2"/>
<path d="M30 100 Q14 70 34 48 Q56 28 94 36 Q104 44 94 54 Q66 50 54 68 Q46 84 56 104Z" fill="#F0C060" {W(3.2)}/>
<path d="M30 70 l4 -4 M38 56 l4 -4 M52 46 l3 -4 M66 40 l2 -4 M80 38 l2 -4 M26 86 l4 -2 M40 96 l3 -3" stroke="#C88A2A" stroke-width="2.6" stroke-linecap="round"/>
{eye(46, 68, .55)}{eye(60, 62, .55)}<path d="M50 76 Q56 78 60 72" fill="none" {W(2)}/>{blush(42, 78, .45)}
<path d="M58 88 Q58 80 70 80 H96 Q108 80 108 88 V94 Q108 104 98 102 L90 96 H74 L66 102 Q58 104 58 94Z" fill="#3A3A50" {W(3)}/>
<path d="M68 86 V94 M64 90 H72" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<circle cx="94" cy="87" r="2.6" fill="#FF5A5A"/><circle cx="100" cy="92" r="2.6" fill="#5AD0FF"/>
{limb("M48 92 L60 90", "#F0C060", 6)}{limb("M74 74 L84 82", "#F0C060", 6)}
{sparkle(20, 36, 4)}{sparkle(112, 70, 3.5)}''')

# 29. Чайхона №1 (Флотская) — медный казан плывёт по реке, как пароходик
I["cafe-chaihona-flotskaya"] = ("медный казан с крышкой-трубой", "плывёт по реке у Северного речного вокзала, как пароходик, из трубы валит ароматный пар", ("#E0F6FF", "#2A88B8"), f'''
<path d="M0 86 Q16 80 32 86 T64 86 T96 86 T128 86 V128 H0Z" fill="#2A78C8" {W(2.6)}/>
<path d="M10 104 Q20 100 30 104 M92 110 Q102 106 112 110 M50 118 Q58 114 66 118" fill="none" stroke="#9AD0FF" stroke-width="2.6" stroke-linecap="round"/>
<path d="M60 22 Q50 12 58 4 Q68 0 72 8 Q82 4 84 14 Q90 22 80 26" fill="#fff" {W(2.4)}/>
<path d="M18 58 H110 Q110 96 64 98 Q18 96 18 58Z" fill="#C8783A" {W(3.2)}/>
<path d="M24 74 Q64 82 104 74" fill="none" stroke="#E8A060" stroke-width="3"/>
<path d="M12 58 H116 V66 H12Z" fill="#A85A2A" {W(2.8)}/>
<circle cx="12" cy="62" r="6" fill="none" {W(3)}/><circle cx="116" cy="62" r="6" fill="none" {W(3)}/>
<path d="M30 58 Q64 40 98 58Z" fill="#B86A30" {W(2.8)}/>
<path d="M60 48 L62 28 H74 L76 48Z" fill="#E8303A" {W(2.6)}/><path d="M61 34 H75" stroke="#fff" stroke-width="3"/>
<circle cx="44" cy="54" r="3" fill="#E8F4FF" {W(1.6)}/><circle cx="88" cy="54" r="3" fill="#E8F4FF" {W(1.6)}/>
{eye(54, 82, .55)}{eye(74, 82, .55)}{smile(64, 89, 4, .8)}{blush(46, 88, .45)}{blush(82, 88, .45)}
<path d="M0 96 Q10 92 18 96 M110 96 Q118 92 128 96" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

# 30. «Джигит.ру» — мальчик-джигит в черкеске и папахе танцует лезгинку на носочках
I["djigit-davydkovskaya"] = ("мальчик-джигит в чёрной черкеске с газырями и белой папахе", "лихо танцует лезгинку на самых носочках, одна рука вытянута в сторону, другая у груди", ("#FFF6D8", "#C88A20"), f'''
<ellipse cx="62" cy="118" rx="26" ry="4" fill="#8A5A10" opacity=".3"/>
<path d="M54 92 L52 116 M66 92 L70 116" {W(8)}/><path d="M54 92 L52 116 M66 92 L70 116" stroke="#2A2A30" stroke-width="4.6" stroke-linecap="round"/>
<path d="M48 118 L54 112 L56 118Z M66 118 L72 112 L74 118Z" fill="#2A2A30" {W(2)}/>
<path d="M44 96 L50 54 H74 L82 96 Q64 102 44 96Z" fill="#2A2A3A" {W(3)}/>
<path d="M62 54 L56 96 M62 54 L68 96" stroke="#5A5A6A" stroke-width="1.6"/>
<path d="M52 60 V72 M55 60 V72 M58 60 V72 M66 60 V72 M69 60 V72 M72 60 V72" stroke="#E8C860" stroke-width="2" stroke-linecap="round"/>
<path d="M46 80 H80" stroke="#C8A040" stroke-width="3"/><circle cx="63" cy="80" r="2.6" fill="#E8C860" {W(1.4)}/>
<path d="M76 58 L98 50 L118 44" fill="none" {W(8)}/><path d="M76 58 L98 50 L118 44" fill="none" stroke="#2A2A3A" stroke-width="4.6" stroke-linecap="round"/>
<circle cx="120" cy="43" r="4" fill="{SK}" {W(2)}/>
<path d="M50 58 L36 66 L52 72" fill="none" {W(8)}/><path d="M50 58 L36 66 L52 72" fill="none" stroke="#2A2A3A" stroke-width="4.6" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="54" cy="72" r="3.6" fill="{SK}" {W(1.8)}/>
{kidhead(62, 40, 11)}
<path d="M48 34 Q48 18 62 18 Q76 18 76 34 Q62 30 48 34Z" fill="#F4F0E8" {W(2.6)}/>
<path d="M52 24 l3 3 M58 21 l3 3 M64 21 l3 3 M70 24 l3 3 M54 30 l3 2 M66 28 l3 2" stroke="#C8C0B0" stroke-width="1.8" stroke-linecap="round"/>
{sparkle(24, 30, 5, "#fff")}{sparkle(100, 92, 4, "#fff")}<path d="M30 96 Q24 100 26 106 M96 72 Q104 74 106 80" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')


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
