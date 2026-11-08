"""Робот «художник», 08.11 ~08:00 UTC. check_unique.py повторов не нашёл, но 57 бассейнов остались от генератора
icons_pools_v2 («зверь × сцена»: пьедестал, кубок, фонтан, аквариум-шар, горка — по кругу, в реестре старые строки
«… плывёт по дорожке бассейна, в шапке»). 40 из них придуманы заново и нарисованы вручную по одной:
свой герой (которого нет в реестре), своя сцена, ракурс и палитра фона.
Запуск из корня: python3 tools/icons_artist_1108_0800.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT

I = {}
SK = "#FFD8B8"


def limb(d, color=SK, w=6):
    return f'<path d="{d}" fill="none" {W(w)}/><path d="{d}" fill="none" stroke="{color}" stroke-width="{w-3.4:.1f}" stroke-linecap="round"/>'


def kidhead(x, y, r=11, cap="#2E6AD8", k=.42):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{SK}" {W(2.8)}/>'
            f'<path d="M{x-r-.5} {y-1} Q{x-r} {y-r-3} {x} {y-r-1} Q{x+r} {y-r-3} {x+r+.5} {y-1} Q{x} {y-5} {x-r-.5} {y-1}Z" fill="{cap}" {W(2.4)}/>'
            f'{eye(x-4, y+2, k)}{eye(x+4, y+2, k)}<path d="M{x-3} {y+6} Q{x} {y+9} {x+3} {y+6}" fill="none" {W(1.8)}/>'
            f'{blush(x-7, y+6, .3)}{blush(x+7, y+6, .3)}')


# 1. «ФламинGo!» — фламинго-малыш на одной ноге пробует воду клювом
I["flamingo-naro-fominsk"] = ("фламинго-малыш в оранжевой плавательной шапочке", "стоит на одной ноге в мелком лягушатнике и пробует воду кончиком клюва, от клюва круги", ("#FFF4C8", "#F08A5A"), f'''
<path d="M0 92 Q64 84 128 92 V128 H0Z" fill="#7FD8F0" {W(2.6)}/>
<ellipse cx="92" cy="96" rx="14" ry="3.5" fill="none" stroke="#fff" stroke-width="2.4"/><ellipse cx="92" cy="96" rx="24" ry="6" fill="none" stroke="#fff" stroke-width="1.6" opacity=".7"/>
<path d="M50 72 L50 116" {W(5)}/><path d="M50 72 L50 116" stroke="#F06A90" stroke-width="2.4"/>
<path d="M54 72 L62 86 L52 92" fill="none" {W(5)}/><path d="M54 72 L62 86 L52 92" fill="none" stroke="#F06A90" stroke-width="2.4" stroke-linejoin="round"/>
<ellipse cx="46" cy="60" rx="24" ry="17" fill="#FF8FB0" {W(3)}/>
<path d="M30 58 Q22 52 22 64 Q30 66 34 62" fill="#FF6F98" {W(2.4)}/>
<path d="M60 50 Q70 30 72 28" fill="none" {W(11)}/><path d="M60 50 Q70 30 72 28" fill="none" stroke="#FF8FB0" stroke-width="7.6" stroke-linecap="round"/>
<circle cx="76" cy="28" r="12" fill="#FF8FB0" {W(2.8)}/>
<path d="M64 25 Q66 12 77 13 Q89 14 88 26 Q77 21 64 25Z" fill="#FF9A2A" {W(2.4)}/>
{eye(79, 29, .55)}{blush(84, 35, .4)}
<path d="M86 32 Q96 40 94 58 Q92 66 90 72" fill="none" {W(6.5)}/><path d="M86 32 Q96 40 94 58 Q92 66 90 72" fill="none" stroke="#FFF2E0" stroke-width="3.2" stroke-linecap="round"/>
<path d="M92 64 L90 74 L88 66Z" fill="{O}"/>''')

# 2. «Морелакс» — рыба-шар надулась и блаженно качается
I["morelax-pool"] = ("пятнистая рыба-шар, надутая, как мячик, с короткими шипиками", "наполовину в воде блаженно зажмурилась и качается на волне бассейна, как поплавок", ("#D8FFF0", "#2FB59A"), f'''
<path d="M104 58 Q120 46 122 60 Q120 72 104 70Z" fill="#B8D890" {W(2.6)}/>
<circle cx="62" cy="64" r="40" fill="#D8E8B0" {W(3.2)}/>
<path d="M24 74 Q62 108 100 74 Q98 104 62 104 Q26 104 24 74Z" fill="#FFF8E0"/>
<circle cx="62" cy="64" r="40" fill="none" {W(3.2)}/>
<path d="M36 34 l-4 -4 M52 26 l-1 -5 M70 26 l1 -5 M86 34 l4 -4 M30 50 l-5 -2 M94 50 l5 -2" {W(3)}/>
<circle cx="46" cy="42" r="3.2" fill="#8AA060"/><circle cx="76" cy="38" r="3.2" fill="#8AA060"/><circle cx="62" cy="34" r="2.6" fill="#8AA060"/><circle cx="90" cy="54" r="2.8" fill="#8AA060"/><circle cx="34" cy="58" r="2.6" fill="#8AA060"/>
<path d="M46 60 Q52 55 58 60 M70 60 Q76 55 82 60" fill="none" {W(2.8)}/>
{blush(42, 70, .9)}{blush(86, 70, .9)}
<ellipse cx="64" cy="76" rx="6" ry="4.5" fill="#E8607A" {W(2.4)}/>
<path d="M28 66 Q16 60 14 70 Q20 76 28 72Z" fill="#B8D890" {W(2.4)}/>
<path d="M0 80 Q16 74 32 80 T64 80 T96 80 T128 80 V128 H0Z" fill="#3AB8E8" opacity=".88"/>
<path d="M0 80 Q16 74 32 80 T64 80 T96 80 T128 80" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M14 100 Q22 96 30 100 M90 108 Q98 104 106 108" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 3. «Китёнок» (Анохина) — хомяк катится по воде в прозрачном шаре
I["kitenok-anokhina"] = ("рыжий хомячок с набитыми щеками", "катится по воде бассейна внутри прозрачного надувного шара, перебирая лапками", ("#FFE8D0", "#E8823A"), f'''
<path d="M0 98 Q32 92 64 98 T128 98 V128 H0Z" fill="#5CC0F0" {W(2.6)}/>
<circle cx="64" cy="62" r="44" fill="#EAF8FF" opacity=".55" {W(3)}/>
<path d="M34 34 Q44 24 56 22" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<ellipse cx="64" cy="78" rx="24" ry="20" fill="#F0A050" {W(3)}/>
<ellipse cx="64" cy="84" rx="14" ry="12" fill="#FFF0DA"/>
<circle cx="64" cy="58" r="18" fill="#F0A050" {W(3)}/>
<circle cx="50" cy="44" r="6" fill="#F0A050" {W(2.6)}/><circle cx="78" cy="44" r="6" fill="#F0A050" {W(2.6)}/>
<circle cx="50" cy="44" r="2.6" fill="#FFB0B8"/><circle cx="78" cy="44" r="2.6" fill="#FFB0B8"/>
<ellipse cx="50" cy="66" rx="10" ry="8" fill="#FFF0DA" {W(2.4)}/><ellipse cx="78" cy="66" rx="10" ry="8" fill="#FFF0DA" {W(2.4)}/>
{eye(57, 56, .55)}{eye(71, 56, .55)}<circle cx="64" cy="63" r="2.2" fill="#E8607A"/>
<path d="M60 68 Q64 71 68 68" fill="none" {W(1.8)}/>
<path d="M50 96 l-4 5 M58 99 l-2 5 M70 99 l2 5 M78 96 l4 5" {W(2.6)}/>
<path d="M14 104 Q22 100 30 104 M98 108 Q106 104 114 108" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 4. «Китёнок» (Некрасовка) — браслет-номерок от шкафчика плывёт по волне
I["kitenok-nekrasovka"] = ("оранжевый браслет-номерок от шкафчика раздевалки с цифрой «7»", "сам плавает на волне у кафельного бортика бассейна и улыбается", ("#E9F4FF", "#4A78C8"), f'''
<path d="M0 0 H128 V40 H0Z" fill="#fff" opacity=".85"/>
<path d="M0 20 H128 M0 40 H128 M20 0 V40 M44 0 V40 M68 0 V40 M92 0 V40 M116 0 V40" stroke="#B8D0E8" stroke-width="2"/>
<path d="M0 40 H128" {W(3)}/>
<path d="M0 48 Q16 42 32 48 T64 48 T96 48 T128 48 V128 H0Z" fill="#3AA8E8" {W(2.6)}/>
<ellipse cx="64" cy="76" rx="40" ry="22" fill="none" {W(13)}/><ellipse cx="64" cy="76" rx="40" ry="22" fill="none" stroke="#FF8A2A" stroke-width="9"/>
<path d="M30 66 Q64 50 98 66" fill="none" stroke="#FFC890" stroke-width="2.4" stroke-linecap="round"/>
<rect x="44" y="64" width="40" height="36" rx="10" fill="#FF8A2A" {W(3)}/>
<rect x="50" y="70" width="28" height="24" rx="7" fill="#FFF4E0" {W(2.2)}/>
<path d="M57 75 H71 L62 90" fill="none" {W(3.4)}/>
{eye(50, 104, .5)}{eye(78, 104, .5)}<path d="M58 108 Q64 112 70 108" fill="none" {W(2)}/>
<path d="M8 110 Q16 106 24 110 M104 116 Q112 112 120 116" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 5. «Китёнок» (Марьино) — альпака по шею в воде, чёлка сухая
I["kitenok-maryino"] = ("бежевая альпака с длинной шеей и ушками-бананами", "стоит по шею в воде бассейна, кудрявый хохолок на макушке остался сухим", ("#F3E6FF", "#9A6FE0"), f'''
<path d="M48 100 Q46 70 52 50 L74 50 Q80 70 78 100Z" fill="#F2DCC0" {W(3)}/>
<path d="M56 60 Q58 66 56 72 M68 64 Q70 70 68 76" fill="none" stroke="#D8B890" stroke-width="2.2" stroke-linecap="round"/>
<path d="M44 26 Q36 10 42 6 Q50 12 50 26Z M84 26 Q92 10 86 6 Q78 12 78 26Z" fill="#F2DCC0" {W(2.6)}/>
<path d="M44 24 Q50 32 64 30 Q78 32 84 24 Q86 52 64 56 Q42 52 44 24Z" fill="#F2DCC0" {W(3)}/>
<path d="M50 24 Q48 14 56 16 Q58 8 64 12 Q70 8 72 16 Q80 14 78 24 Q64 28 50 24Z" fill="#FFF4E4" {W(2.4)}/>
<ellipse cx="64" cy="46" rx="9" ry="6.5" fill="#FFF4E4" {W(2.2)}/>
<path d="M61 44 L64 47 L67 44 M64 47 V50" fill="none" {W(1.8)}/>
{eye(55, 36, .6)}{eye(73, 36, .6)}{blush(50, 44, .5)}{blush(78, 44, .5)}
<path d="M0 84 Q16 78 32 84 T64 84 T96 84 T128 84 V128 H0Z" fill="#6AC8F0" opacity=".92" {W(2.6)}/>
<path d="M40 86 Q64 94 88 86" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M10 102 Q18 98 26 102 M96 106 Q104 102 112 106 M50 114 Q58 110 66 114" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 6. «Китёнок» (Текстильщики) — морской котик хлопает в ласты на бортике
I["kitenok-tekstilshchiki"] = ("бурый морской котик с ушками и усами", "сидит на бортике бассейна, задрав нос, и громко хлопает в ласты", ("#E6F8FF", "#3A8FD8"), f'''
<path d="M0 84 H70 V128 H0Z" fill="#F2F6FA" {W(3)}/>
<path d="M0 98 H70 M0 112 H70 M18 84 V128 M40 84 V128 M62 84 V128" stroke="#C8D8E8" stroke-width="2"/>
<path d="M70 92 Q84 88 98 92 T128 92 V128 H70Z" fill="#3AB0F0" {W(2.6)}/>
<path d="M30 86 Q20 60 36 40 Q46 30 56 34 Q64 40 60 60 Q58 76 64 86Z" fill="#8A5A3A" {W(3)}/>
<path d="M24 86 Q10 84 8 92 Q20 94 30 90Z M64 86 Q78 82 82 90 Q70 94 58 90Z" fill="#6A4028" {W(2.4)}/>
<ellipse cx="50" cy="28" rx="14" ry="12" fill="#8A5A3A" {W(2.8)}/>
<path d="M58 30 Q70 28 70 34 Q64 38 58 36" fill="#A0704A" {W(2.2)}/><circle cx="69" cy="31" r="2" fill="{O}"/>
<path d="M62 36 L76 38 M62 38 L74 42" stroke="{O}" stroke-width="1.4"/>
<path d="M40 20 Q38 16 42 16" fill="none" {W(2.4)}/>
{eye(48, 25, .5)}{eye(57, 24, .45)}{blush(46, 32, .4)}
<path d="M42 54 Q52 42 62 48 L70 40 M44 60 Q56 54 66 56 L76 50" fill="none" {W(7)}/>
<path d="M42 54 Q52 42 62 48 L70 40 M44 60 Q56 54 66 56 L76 50" fill="none" stroke="#6A4028" stroke-width="4" stroke-linecap="round"/>
<path d="M76 34 l4 -6 M82 42 l7 -2 M80 52 l7 2" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M80 108 Q90 104 100 108 M104 118 Q112 114 120 118" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 7. «Китёнок» (Коломенская) — нерпа положила подбородок на бортик
I["kitenok-kolomenskaya"] = ("серебристая нерпа с огромными чёрными глазами", "высунулась из воды и положила подбородок на кафельный бортик бассейна, крупно", ("#FFF7E0", "#C8A050"), f'''
<path d="M0 0 H128 V60 H0Z" fill="#FFF1D0" opacity=".6"/>
<path d="M0 30 H128 M32 0 V60 M64 0 V60 M96 0 V60" stroke="#E8D0A0" stroke-width="2"/>
<path d="M0 60 H128 V70 H0Z" fill="#fff" {W(3)}/>
<path d="M0 70 H128 V128 H0Z" fill="#4AB8E8"/>
<path d="M0 70 H128" {W(3)}/>
<path d="M22 128 Q20 76 64 66 Q108 76 106 128Z" fill="#A8B4C0" {W(3)}/>
<circle cx="48" cy="96" r="3" fill="#7A8898"/><circle cx="86" cy="104" r="3.5" fill="#7A8898"/><circle cx="70" cy="116" r="2.6" fill="#7A8898"/>
<path d="M24 58 Q22 22 64 20 Q106 22 104 58 Q100 70 64 70 Q28 70 24 58Z" fill="#B8C4D0" {W(3)}/>
<ellipse cx="46" cy="42" rx="10" ry="11" fill="{O}"/><ellipse cx="82" cy="42" rx="10" ry="11" fill="{O}"/>
<circle cx="42" cy="37" r="4" fill="#fff"/><circle cx="78" cy="37" r="4" fill="#fff"/><circle cx="49" cy="47" r="2" fill="#fff"/><circle cx="85" cy="47" r="2" fill="#fff"/>
<ellipse cx="64" cy="56" rx="6" ry="4" fill="{O}"/>
<path d="M56 62 Q64 66 72 62" fill="none" {W(2)}/>
<path d="M50 58 L34 56 M50 62 L36 64 M78 58 L94 56 M78 62 L92 64" stroke="{O}" stroke-width="1.4"/>
{blush(34, 52, .7)}{blush(94, 52, .7)}
<path d="M0 74 Q14 80 24 74 M104 74 Q114 80 128 74" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

# 8. «Китёнок» (Ясенево) — кит-полосатик катает малыша на спине
I["kitenok-yasenevo"] = ("большой синий кит-полосатик с полосками на горле", "катает на спине малыша в шапочке через весь бассейн", ("#FFFBD0", "#E8C030"), f'''
<path d="M0 82 Q32 76 64 82 T128 82 V128 H0Z" fill="#58C8F0" {W(2.6)}/>
<path d="M8 72 Q8 44 50 44 Q92 44 104 66 L118 54 Q124 66 116 76 Q122 86 112 92 L102 82 Q90 96 50 96 Q8 96 8 72Z" fill="#3A6AD0" {W(3)}/>
<path d="M14 80 Q40 94 80 88 M18 86 Q40 96 70 92 M24 90 Q40 98 60 95" fill="none" stroke="#9AC0F8" stroke-width="2"/>
{eye(28, 64, .6)}{blush(22, 72, .5)}<path d="M12 74 Q22 78 30 74" fill="none" {W(2.2)}/>
{limb("M58 44 L50 36", SK, 6)}{limb("M66 44 L76 34", SK, 6)}
<path d="M54 46 Q54 34 62 34 Q70 34 70 46Z" fill="#FF6A6A" {W(2.4)}/>
{kidhead(62, 24, 10, "#FF6A6A")}
<path d="M0 90 Q16 86 30 92 M104 102 Q114 98 124 102" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<path d="M0 96 Q32 90 64 96 T128 96 V128 H0Z" fill="#58C8F0" opacity=".85"/>''')

# 9. «Китёнок» (Пролетарская) — мопс пыхтя плывёт по-собачьи
I["kitenok-proletarskaya"] = ("кремовый мопс в голубых плавательных очках на лбу", "пыхтя плывёт по-собачьи, над водой только морщинистая голова и лапки", ("#E8FFE8", "#58B868"), f'''
<path d="M0 74 Q20 68 40 74 T80 74 T128 74 V128 H0Z" fill="#52C0E8" {W(2.6)}/>
<path d="M26 82 Q20 74 28 70 M100 82 Q108 74 100 70" fill="none" {W(7)}/>
<path d="M26 82 Q20 74 28 70 M100 82 Q108 74 100 70" fill="none" stroke="#F0D8A8" stroke-width="3.6" stroke-linecap="round"/>
<path d="M30 30 Q20 30 22 50 Q30 44 34 38Z M98 30 Q108 30 106 50 Q98 44 94 38Z" fill="#3A2E2A" {W(2.6)}/>
<ellipse cx="64" cy="54" rx="34" ry="30" fill="#F0D8A8" {W(3)}/>
<path d="M52 32 Q64 28 76 32 M54 38 Q64 35 74 38" fill="none" {W(2)}/>
<ellipse cx="64" cy="66" rx="18" ry="14" fill="#3A2E2A" {W(2.6)}/>
<ellipse cx="64" cy="60" rx="6" ry="4" fill="#111"/>
<path d="M58 70 Q64 74 70 70" fill="none" stroke="#fff" stroke-width="1.8"/>
<path d="M62 72 Q64 80 68 74" fill="#FF7FA0" {W(1.6)}/>
{eye(48, 50, .65)}{eye(80, 50, .65)}
<circle cx="50" cy="26" r="7" fill="#9AE0FF" {W(2.4)}/><circle cx="78" cy="26" r="7" fill="#9AE0FF" {W(2.4)}/><path d="M57 26 H71" {W(2.4)}/>
<path d="M30 36 Q64 14 98 36" fill="none" stroke="#2A80D0" stroke-width="2.4"/>
<path d="M12 64 Q8 58 12 54 M116 64 Q120 58 116 54" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M30 84 Q64 92 98 84" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>''')

# 10. «Китёнок» (Новогиреево) — ёлочный шар плавает в бассейне, как буёк
I["kitenok-novogireevo"] = ("красный ёлочный шар с золотым колпачком и белыми снежинками", "плавает в бассейне, как буёк, петелькой вверх, вокруг кружатся снежинки", ("#EAF0FF", "#2E4A9A"), f'''
<path d="M0 86 Q32 80 64 86 T128 86 V128 H0Z" fill="#3AB8E8" {W(2.6)}/>
<path d="M58 14 Q64 4 70 14" fill="none" {W(3)}/>
<rect x="54" y="14" width="20" height="12" rx="3" fill="#FFD040" {W(2.6)}/>
<path d="M58 14 V26 M64 14 V26 M70 14 V26" stroke="#C89820" stroke-width="1.6"/>
<circle cx="64" cy="64" r="38" fill="#E83A4A" {W(3.2)}/>
<path d="M34 44 Q44 32 56 30" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".7"/>
<path d="M28 68 Q64 80 100 68" fill="none" stroke="#FFD040" stroke-width="5"/>
{eye(52, 58, .65)}{eye(76, 58, .65)}{smile(64, 66, 5, 1)}{blush(44, 66, .6)}{blush(84, 66, .6)}
<path d="M0 92 Q32 86 64 92 T128 92 V128 H0Z" fill="#3AB8E8" opacity=".85"/>
<path d="M30 94 Q64 102 98 94" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M18 30 v10 M13 35 h10 M14 31 l8 8 M22 31 l-8 8" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
<path d="M108 40 v8 M104 44 h8" stroke="#fff" stroke-width="2" stroke-linecap="round"/>''')

# 11. «Китёнок» (Черёмушки) — морской слон развалился на краю бассейна и зевает
I["kitenok-cheryomushki"] = ("толстый серый морской слон с носом-хоботком", "лежит на краю бассейна, свесив хвостовые ласты в воду, и сладко зевает во весь рот", ("#F6EEE6", "#B08A70"), f'''
<path d="M0 74 H128 V84 H0Z" fill="#fff" {W(3)}/>
<path d="M0 84 H128 V128 H0Z" fill="#40B0E8"/>
<path d="M10 104 Q20 100 30 104 M44 116 Q54 112 64 116" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M92 76 Q112 80 114 98 Q104 94 100 100 Q98 90 90 86Z" fill="#7A7480" {W(2.6)}/>
<path d="M24 76 Q18 40 50 34 Q84 30 100 60 Q104 70 98 78Z" fill="#9A94A0" {W(3)}/>
<path d="M56 46 Q70 44 84 54 M58 56 Q72 54 88 64" fill="none" stroke="#7A7480" stroke-width="2"/>
<path d="M62 76 Q70 64 78 76" fill="#7A7480" {W(2.4)}/>
<path d="M30 46 Q16 44 14 58 Q14 66 22 64 Q20 56 28 54" fill="#B4AEB8" {W(2.8)}/>
<ellipse cx="38" cy="60" rx="9" ry="10" fill="#7A2A3A" {W(2.4)}/><path d="M33 66 Q38 61 43 66" fill="#FF7F98"/>
<path d="M36 40 Q40 36 44 40 M48 38 Q52 34 56 38" fill="none" {W(2.4)}/>
{blush(54, 48, .6)}
<path d="M62 20 q4 -4 8 0 M74 12 q3 -3 6 0" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 12. «Китёнок» (Медведково) — шимпанзе на лесенке пробует воду ногой
I["kitenok-medvedkovo"] = ("малыш-шимпанзе с большими ушами", "висит одной рукой на хромированной лесенке бассейна и осторожно пробует воду пальцами ноги", ("#FFF0F0", "#E86A8A"), f'''
<path d="M0 88 Q32 82 64 88 T128 88 V128 H0Z" fill="#48B8EC" {W(2.6)}/>
<ellipse cx="78" cy="96" rx="10" ry="3" fill="none" stroke="#fff" stroke-width="2.2"/>
<path d="M30 20 Q30 6 44 6 Q56 6 56 20 V110 M30 20 V110" fill="none" stroke="#D8E0EA" stroke-width="7" stroke-linecap="round"/>
<path d="M30 20 Q30 6 44 6 Q56 6 56 20 V110 M30 20 V110" fill="none" {W(1.6)}/>
<path d="M30 60 H56 M30 80 H56" stroke="#D8E0EA" stroke-width="5"/>
{limb("M70 50 Q60 34 56 24", "#6A4A3A", 8)}
{limb("M72 74 Q84 84 80 94", "#6A4A3A", 8)}{limb("M62 74 Q56 84 58 92", "#6A4A3A", 8)}
<ellipse cx="68" cy="62" rx="14" ry="16" fill="#6A4A3A" {W(3)}/><ellipse cx="68" cy="66" rx="8" ry="10" fill="#D8B090"/>
{limb("M78 56 Q92 50 96 40", "#6A4A3A", 8)}
<circle cx="74" cy="36" r="15" fill="#6A4A3A" {W(3)}/>
<circle cx="58" cy="34" r="6" fill="#D8B090" {W(2.4)}/><circle cx="90" cy="34" r="6" fill="#D8B090" {W(2.4)}/>
<path d="M64 34 Q74 26 84 34 Q86 46 74 48 Q62 46 64 34Z" fill="#D8B090" {W(2.2)}/>
{eye(69, 34, .5)}{eye(79, 34, .5)}<path d="M68 42 Q74 46 80 42" fill="none" {W(2)}/>
<path d="M84 98 l3 -5 M88 100 l5 -2" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 13. «Китёнок» (Филатов луг) — скалярия проплывает сквозь подводный обруч
I["kitenok-filatov-lug"] = ("полосатая рыбка-скалярия с высокими плавниками-парусами", "под водой у кафельного дна бассейна разглядывает пузырьки, повернувшись боком", ("#E0FFF8", "#38A8B8"), f'''
<path d="M0 0 H128 V18 Q96 24 64 18 T0 18Z" fill="#fff" opacity=".35"/>
<path d="M0 108 H128 V128 H0Z" fill="#9AE0E0"/><path d="M0 108 H128" {W(2.4)}/>
<path d="M20 108 V128 M48 108 V128 M76 108 V128 M104 108 V128" stroke="#70C8C8" stroke-width="2"/>
<path d="M44 62 L22 46 Q16 62 22 78Z" fill="#FFE070" {W(2.8)}/>
<path d="M58 34 Q66 2 74 14 Q80 36 96 60 Q80 84 74 106 Q66 120 58 90 Q42 76 40 62 Q42 48 58 34Z" fill="#FFF0B0" {W(3)}/>
<path d="M58 36 Q56 62 58 90 M72 18 Q68 62 72 104" fill="none" stroke="#3A3060" stroke-width="6"/>
<path d="M58 34 Q66 2 74 14 Q80 36 96 60 Q80 84 74 106 Q66 120 58 90 Q42 76 40 62 Q42 48 58 34Z" fill="none" {W(3)}/>
{eye(84, 56, .65)}<path d="M88 66 Q92 68 95 64" fill="none" {W(2)}/>{blush(82, 66, .45)}
<circle cx="104" cy="44" r="4" fill="none" stroke="#fff" stroke-width="2"/><circle cx="110" cy="30" r="2.6" fill="none" stroke="#fff" stroke-width="2"/><circle cx="102" cy="20" r="2" fill="none" stroke="#fff" stroke-width="2"/>''')

# 14. «Китёнок» (Потапово) — птичка киви ныряет с бортика клювом вперёд
I["kitenok-potapovo"] = ("круглая коричневая птичка киви с длинным клювом", "ныряет с бортика в бассейн клювом вперёд, как стрела, лапки ещё на бортике", ("#F4FFE0", "#8CC040"), f'''
<path d="M0 50 H50 V60 H0Z" fill="#fff" {W(2.6)}/>
<path d="M0 78 Q40 72 80 78 T128 74 V128 H0Z" fill="#40B8E8" {W(2.6)}/>
<path d="M90 78 L96 66 L100 76 L108 66 L108 80" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M26 50 L22 40 M34 50 L32 40" {W(3.4)}/><path d="M18 50 H26 M28 50 H36" {W(3)}/>
<ellipse cx="44" cy="34" rx="26" ry="22" fill="#8A6038" transform="rotate(20 44 34)" {W(3)}/>
<path d="M30 26 l4 4 M40 20 l3 5 M28 38 l5 2 M44 32 l3 5 M54 22 l2 5" stroke="#5A3A20" stroke-width="2" stroke-linecap="round"/>
<path d="M62 44 Q82 54 96 80" fill="none" {W(7)}/><path d="M62 44 Q82 54 96 80" fill="none" stroke="#E8C8A0" stroke-width="3.6" stroke-linecap="round"/>
{eye(60, 36, .6)}{blush(54, 44, .45)}''')

# 15. «Китёнок» (Жулебино) — альбатрос садится на воду, растопырив лапы
I["kitenok-zhulebino"] = ("белый альбатрос с длинными крыльями", "садится на воду бассейна, растопырив перепончатые лапы, как тормоза, — брызги веером", ("#FFF0D8", "#E8A040"), f'''
<path d="M0 92 Q32 86 64 92 T128 92 V128 H0Z" fill="#4AB0E0" {W(2.6)}/>
<path d="M44 92 Q36 76 30 82 M52 92 Q50 74 44 76 M80 92 Q88 76 94 82 M72 92 Q76 74 82 76" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M60 56 Q30 30 4 38 Q26 44 34 56 Q46 62 60 62Z" fill="#fff" {W(3)}/>
<path d="M4 38 Q14 40 20 44" fill="none" stroke="#3A3A4A" stroke-width="4" stroke-linecap="round"/>
<path d="M68 56 Q98 30 124 38 Q102 44 94 56 Q82 62 68 62Z" fill="#fff" {W(3)}/>
<path d="M124 38 Q114 40 108 44" fill="none" stroke="#3A3A4A" stroke-width="4" stroke-linecap="round"/>
<ellipse cx="64" cy="62" rx="16" ry="12" fill="#fff" {W(3)}/>
<path d="M56 72 L52 86 L46 90 H58 L56 86 M72 72 L76 86 L70 90 H82 L78 86" fill="#FFA0B0" {W(2.4)}/>
<circle cx="64" cy="42" r="11" fill="#fff" {W(2.8)}/>
<path d="M66 46 L82 50 Q84 54 80 54 L66 52Z" fill="#FFC060" {W(2.2)}/>
{eye(60, 40, .5)}{eye(68, 40, .5)}{blush(56, 46, .4)}''')

# 16. «Аквакласс» — каракатица в очках пишет чернилами букву «А» на дне
I["aqua-class-rybalko"] = ("сиреневая каракатица в круглых учительских очках", "выводит чернилами на кафельном дне бассейна большую букву «А»", ("#FFFFF0", "#9AD0A0"), f'''
<path d="M0 0 H128 V128 H0Z" fill="#7ED0E8" opacity=".55"/>
<path d="M0 32 H128 M0 64 H128 M0 96 H128 M32 0 V128 M64 0 V128 M96 0 V128" stroke="#fff" stroke-width="1.6" opacity=".7"/>
<path d="M18 112 L36 72 L54 112 M26 98 H46" fill="none" stroke="#3A3060" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M54 112 Q60 104 66 98" fill="none" stroke="#3A3060" stroke-width="4" stroke-linecap="round" opacity=".7"/>
<path d="M70 92 Q64 104 58 108 M78 96 Q74 110 70 114 M88 96 Q90 110 94 114 M96 92 Q104 102 108 104" fill="none" {W(5)}/>
<path d="M70 92 Q64 104 58 108 M78 96 Q74 110 70 114 M88 96 Q90 110 94 114 M96 92 Q104 102 108 104" fill="none" stroke="#C8A0F0" stroke-width="2.4" stroke-linecap="round"/>
<path d="M62 92 Q56 52 84 26 Q112 52 106 92 Q84 100 62 92Z" fill="#C8A0F0" {W(3)}/>
<path d="M62 92 Q50 70 62 46 M106 92 Q118 70 106 46" fill="none" stroke="#E8D0FF" stroke-width="4" stroke-linecap="round"/>
<circle cx="76" cy="72" r="7" fill="#fff" {W(2.4)}/><circle cx="94" cy="72" r="7" fill="#fff" {W(2.4)}/><path d="M83 72 H87" {W(2.4)}/>
{eye(76, 72, .5)}{eye(94, 72, .5)}<path d="M80 84 Q85 88 90 84" fill="none" {W(2)}/>
<circle cx="70" cy="22" r="3" fill="none" stroke="#fff" stroke-width="2"/><circle cx="62" cy="12" r="2" fill="none" stroke="#fff" stroke-width="2"/>''')

# 17. «Атлант» — малыш-силач держит над головой надувной круг, как штангу
I["pool-atlant"] = ("малыш-силач в полосатом ретро-купальнике с лямкой через плечо", "стоит по пояс в воде и гордо держит над головой надувной круг, как штангу", ("#FFE0E0", "#D04848"), f'''
<ellipse cx="64" cy="22" rx="40" ry="12" fill="none" {W(14)}/><ellipse cx="64" cy="22" rx="40" ry="12" fill="none" stroke="#fff" stroke-width="10"/>
<path d="M30 16 L36 30 M64 10 V34 M98 16 L92 30" stroke="#FF4A5A" stroke-width="9"/>
<ellipse cx="64" cy="22" rx="40" ry="12" fill="none" {W(1.6)}/>
{limb("M48 66 Q32 52 34 30", SK, 9)}{limb("M80 66 Q96 52 94 30", SK, 9)}
<path d="M44 70 Q44 60 64 60 Q84 60 84 70 V104 H44Z" fill="#fff" {W(3)}/>
<path d="M44 74 H84 M44 84 H84 M44 94 H84" stroke="#2A4AA8" stroke-width="5"/>
<path d="M44 70 Q44 60 64 60 Q84 60 84 70 V104 H44Z" fill="none" {W(3)}/>
<path d="M52 60 L58 70 M76 60 L70 70" {W(2.4)}/>
<circle cx="64" cy="48" r="13" fill="{SK}" {W(2.8)}/>
<path d="M52 44 Q54 34 64 35 Q74 34 76 44 Q70 40 64 41 Q58 40 52 44Z" fill="#7A4A2A" {W(2)}/>
<path d="M56 48 Q59 45 62 48 M66 48 Q69 45 72 48" fill="none" {W(2)}/>
<path d="M58 54 Q64 58 70 54" fill="none" {W(2)}/>{blush(54, 54, .35)}{blush(74, 54, .35)}
<path d="M0 90 Q32 84 64 90 T128 90 V128 H0Z" fill="#48B8F0" opacity=".92" {W(2.6)}/>
<path d="M36 92 Q64 100 92 92" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M18 40 l-6 -2 M20 50 l-8 2 M110 40 l6 -2 M108 50 l8 2" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

# 18. СК «Молния» — дюгонь пасётся на дне бассейна
I["molniya-lobnenskaya"] = ("пухлая дюгонь с усатой мордочкой и хвостом-полумесяцем", "под водой «пасётся» у дна бассейна, жуя длинную травинку, вид сбоку", ("#E8F4FF", "#3A5AC0"), f'''
<path d="M0 0 H128 V128 H0Z" fill="#4A9AE0" opacity=".45"/>
<path d="M0 112 H128 V128 H0Z" fill="#E8F0F8"/><path d="M0 112 H128" {W(2.4)}/>
<path d="M30 112 Q24 96 32 84 Q38 74 32 64" fill="none" stroke="#3AA060" stroke-width="5" stroke-linecap="round"/>
<path d="M14 112 Q10 100 16 92" fill="none" stroke="#3AA060" stroke-width="4" stroke-linecap="round"/>
<path d="M98 62 Q112 52 122 40 Q124 54 116 62 Q126 70 122 84 Q112 72 98 68Z" fill="#8A9AA8" {W(2.8)}/>
<path d="M24 76 Q26 50 60 46 Q90 44 102 64 Q96 90 60 92 Q34 92 24 76Z" fill="#A8B8C4" {W(3)}/>
<path d="M60 90 Q66 102 56 104 Q50 98 52 90" fill="#8A9AA8" {W(2.4)}/>
<path d="M24 70 Q14 70 14 82 Q22 90 34 84" fill="#C8D2DA" {W(2.6)}/>
<path d="M14 80 Q8 84 4 92" fill="none" stroke="#3AA060" stroke-width="4" stroke-linecap="round"/>
<circle cx="20" cy="78" r="1.2" fill="{O}"/><circle cx="25" cy="81" r="1.2" fill="{O}"/><circle cx="22" cy="84" r="1.2" fill="{O}"/>
{eye(38, 66, .55)}{blush(44, 74, .5)}
<circle cx="40" cy="30" r="4" fill="none" stroke="#fff" stroke-width="2"/><circle cx="48" cy="18" r="2.6" fill="none" stroke="#fff" stroke-width="2"/>''')

# 19. «Москворечье» — девочка плывёт кролем, рука взлетает над водой
I["ms-pool-moskvorechye"] = ("девочка в фиолетовой шапочке и лимонных очках", "плывёт кролем, рука взлетела над водой, лицо повёрнуто вдохнуть, вид сбоку", ("#F8FFE0", "#A8D040"), f'''
<path d="M0 72 Q16 66 32 72 T64 72 T96 72 T128 72 V128 H0Z" fill="#40B0E8" {W(2.6)}/>
<path d="M0 88 H128" stroke="#fff" stroke-width="5" stroke-dasharray="7 5"/>
{limb("M62 72 Q70 38 98 34", SK, 9)}
<path d="M30 78 Q50 70 80 76" fill="none" {W(14)}/><path d="M30 78 Q50 70 80 76" fill="none" stroke="#E04A8A" stroke-width="10.6" stroke-linecap="round"/>
<circle cx="44" cy="64" r="14" fill="{SK}" {W(2.8)}/>
<path d="M30 62 Q30 46 46 48 Q58 50 58 60 Q44 54 30 62Z" fill="#8A4AD8" {W(2.4)}/>
<path d="M34 64 H54" stroke="#E0F040" stroke-width="5" stroke-linecap="round"/><path d="M34 64 H54" {W(1.4)}/>
<circle cx="38" cy="65" r="3" fill="#fff" {W(1.4)}/>
<ellipse cx="44" cy="72" rx="4" ry="3" fill="#C8406A" {W(1.6)}/>{blush(52, 70, .35)}
<path d="M98 34 l6 -6 M100 38 l8 -2" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M90 70 Q100 60 106 70 Q112 60 118 70" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M14 100 Q22 96 30 100 M90 110 Q98 106 106 110" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 20. «На Ереванской» — рыба-молот плывёт вдоль линии на дне, вид сверху
I["ms-pool-yerevanskaya"] = ("серая рыба-молот с широкой головой-молотком", "плывёт вдоль разметки на дне бассейна, вид сверху", ("#E8E8FF", "#5860C0"), f'''
<path d="M0 0 H128 V128 H0Z" fill="#68C0F0" opacity=".6"/>
<path d="M60 128 V12 H68 V128Z" fill="#2A3050" opacity=".55"/>
<path d="M0 50 Q20 46 40 50 M88 90 Q108 86 128 90 M10 100 Q24 96 38 100" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".8"/>
<path d="M64 36 Q80 56 78 80 Q74 100 64 108 Q54 100 50 80 Q48 56 64 36Z" fill="#9AA8B8" {W(3)}/>
<path d="M64 106 L50 124 L64 116 L78 124Z" fill="#9AA8B8" {W(2.6)}/>
<path d="M54 62 L28 82 L54 76Z M74 62 L100 82 L74 76Z" fill="#8090A0" {W(2.6)}/>
<path d="M14 32 Q14 20 64 20 Q114 20 114 32 Q114 44 64 44 Q14 44 14 32Z" fill="#B0BCC8" {W(3)}/>
{eye(22, 32, .75)}{eye(106, 32, .75)}
<path d="M54 36 Q64 42 74 36" fill="none" {W(2.4)}/>{blush(38, 38, .6)}{blush(90, 38, .6)}''')

# 21. «Детская бухта» (Островитянова) — надувной островок с пальмой посреди бассейна
I["detskaya-bukhta-ostrovityanova"] = ("надувной песочный островок с зелёной пальмой", "плавает посреди бассейна, в тени пальмы отдыхает малыш в панамке", ("#FFF8D0", "#40C0D0"), f'''
<path d="M0 74 Q32 68 64 74 T128 74 V128 H0Z" fill="#3ABCE0" {W(2.6)}/>
<ellipse cx="64" cy="86" rx="46" ry="14" fill="#FFD890" {W(3)}/>
<path d="M24 86 Q64 96 104 86" fill="none" stroke="#FFF0C8" stroke-width="3" stroke-linecap="round"/>
<path d="M76 84 Q72 56 82 30" fill="none" {W(8)}/><path d="M76 84 Q72 56 82 30" fill="none" stroke="#B07A40" stroke-width="4.6" stroke-linecap="round"/>
<path d="M82 30 Q64 16 46 26 Q62 26 72 34Z M82 30 Q100 14 116 26 Q100 26 90 34Z M82 30 Q78 12 90 6 Q88 18 86 30Z M82 30 Q60 34 54 50 Q68 40 80 36Z M82 30 Q104 34 108 50 Q96 40 84 36Z" fill="#4AC060" {W(2.4)}/>
<circle cx="80" cy="34" r="3" fill="#8A5A2A" {W(1.4)}/><circle cx="86" cy="35" r="3" fill="#8A5A2A" {W(1.4)}/>
{limb("M44 82 L32 80", SK, 6)}
<path d="M36 82 Q40 72 56 74 Q60 80 56 84Z" fill="#FF7A5A" {W(2.4)}/>
<circle cx="46" cy="70" r="8" fill="{SK}" {W(2.4)}/>
<path d="M36 68 Q38 58 46 58 Q54 58 56 68 Z" fill="#fff" {W(2.2)}/><path d="M34 68 H58" {W(2.4)}/>
<path d="M42 72 Q44 70 46 72 M48 72 Q50 70 52 72" fill="none" {W(1.6)}/>
<path d="M10 104 Q18 100 26 104 M98 110 Q106 106 114 110" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 22. «Детская бухта» (Измайлово) — якорь на дне, цепь к бую
I["detskaya-bukhta-izmaylovo"] = ("тёмно-синий якорь с мордочкой", "лежит на дне бассейна и держит цепью красно-белый буй на поверхности, вид в разрезе", ("#E0F4FF", "#2060A0"), f'''
<path d="M0 22 Q32 16 64 22 T128 22 V128 H0Z" fill="#3A90D8" opacity=".75"/>
<path d="M0 22 Q32 16 64 22 T128 22" fill="none" stroke="#fff" stroke-width="3"/>
<path d="M0 112 H128 V128 H0Z" fill="#D8E8F4"/><path d="M0 112 H128" {W(2.4)}/>
<path d="M64 30 Q70 46 64 60" fill="none" stroke="#C8C8D0" stroke-width="3.4" stroke-dasharray="4 3"/>
<path d="M50 22 Q50 8 64 8 Q78 8 78 22 Q78 32 64 32 Q50 32 50 22Z" fill="#fff" {W(2.8)}/>
<path d="M51 18 H77 V26 H51Z" fill="#E83A4A"/>
<path d="M50 22 Q50 8 64 8 Q78 8 78 22 Q78 32 64 32 Q50 32 50 22Z" fill="none" {W(2.8)}/>
<circle cx="64" cy="66" r="6" fill="none" {W(9)}/><circle cx="64" cy="66" r="6" fill="none" stroke="#2A3A70" stroke-width="5"/>
<path d="M64 72 V108" {W(12)}/><path d="M64 72 V108" stroke="#2A3A70" stroke-width="8"/>
<path d="M48 82 H80" {W(9)}/><path d="M48 82 H80" stroke="#2A3A70" stroke-width="5" stroke-linecap="round"/>
<path d="M30 92 Q36 112 64 112 Q92 112 98 92" fill="none" {W(12)}/><path d="M30 92 Q36 112 64 112 Q92 112 98 92" fill="none" stroke="#2A3A70" stroke-width="8" stroke-linecap="round"/>
<path d="M24 92 L32 84 L36 94Z M104 92 L96 84 L92 94Z" fill="#2A3A70" {W(2.4)}/>
<circle cx="61" cy="94" r="2.2" fill="#fff"/><circle cx="68" cy="94" r="2.2" fill="#fff"/>
<path d="M60 100 Q64 103 68 100" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round"/>
<circle cx="90" cy="60" r="3" fill="none" stroke="#fff" stroke-width="2"/><circle cx="96" cy="46" r="2" fill="none" stroke="#fff" stroke-width="2"/>''')

# 23. «Немо» (Пражская) — актиния машет щупальцами со дна
I["aqua-nemo-prazhskaya"] = ("розовая актиния с пышными щупальцами", "растёт на кафельном дне бассейна и весело машет всеми щупальцами, как ладошками", ("#FFE4EC", "#F07090"), f'''
<path d="M0 0 H128 V128 H0Z" fill="#60C8E8" opacity=".5"/>
<path d="M0 104 H128 V128 H0Z" fill="#E8F4F8"/><path d="M0 104 H128" {W(2.4)}/>
<path d="M30 104 V128 M64 104 V128 M98 104 V128" stroke="#B8D8E8" stroke-width="2"/>
<path d="M38 66 Q22 40 14 46 M46 60 Q34 28 26 30 M56 56 Q52 22 44 18 M64 56 Q66 20 64 12 M72 56 Q78 22 86 18 M82 60 Q94 28 102 30 M90 66 Q106 40 114 46" fill="none" {W(10)}/>
<path d="M38 66 Q22 40 14 46 M46 60 Q34 28 26 30 M56 56 Q52 22 44 18 M64 56 Q66 20 64 12 M72 56 Q78 22 86 18 M82 60 Q94 28 102 30 M90 66 Q106 40 114 46" fill="none" stroke="#FF8AB0" stroke-width="6.6" stroke-linecap="round"/>
<circle cx="14" cy="46" r="3.4" fill="#FFE0EA"/><circle cx="26" cy="30" r="3.4" fill="#FFE0EA"/><circle cx="44" cy="18" r="3.4" fill="#FFE0EA"/><circle cx="64" cy="12" r="3.4" fill="#FFE0EA"/><circle cx="86" cy="18" r="3.4" fill="#FFE0EA"/><circle cx="102" cy="30" r="3.4" fill="#FFE0EA"/><circle cx="114" cy="46" r="3.4" fill="#FFE0EA"/>
<path d="M36 104 Q32 66 64 58 Q96 66 92 104Z" fill="#F0507A" {W(3)}/>
<path d="M46 98 Q44 76 50 68 M82 98 Q84 76 78 68" fill="none" stroke="#FF8AB0" stroke-width="3" stroke-linecap="round"/>
{eye(56, 80, .65)}{eye(72, 80, .65)}{smile(64, 88, 5, 1)}{blush(48, 88, .5)}{blush(80, 88, .5)}''')

# 24. «Немо» (Академическая) — малыш-Нептун на надувном троне
I["aqua-nemo-akademicheskaya"] = ("малыш-Нептун с бородой из пены, короной и трезубцем", "восседает на зелёном надувном троне посреди бассейна", ("#E8FFF0", "#40B070"), f'''
<path d="M0 86 Q32 80 64 86 T128 86 V128 H0Z" fill="#40B0E0" {W(2.6)}/>
<path d="M30 92 Q28 56 36 50 Q44 46 46 60 H82 Q84 46 92 50 Q100 56 98 92Z" fill="#5AD080" {W(3)}/>
<path d="M30 92 Q64 102 98 92 Q98 104 64 106 Q30 104 30 92Z" fill="#3AB060" {W(3)}/>
<path d="M40 60 Q40 54 36 52 M88 60 Q88 54 92 52" fill="none" stroke="#B0F0C0" stroke-width="2.4" stroke-linecap="round"/>
<path d="M50 90 Q50 70 64 68 Q78 70 78 90Z" fill="#4A80E0" {W(2.6)}/>
<path d="M98 26 V96" {W(5)}/><path d="M98 26 V96" stroke="#FFC830" stroke-width="2.4"/>
<path d="M88 30 V20 M98 28 V14 M108 30 V20 M88 30 H108" fill="none" {W(5)}/><path d="M88 30 V20 M98 28 V14 M108 30 V20 M88 30 H108" fill="none" stroke="#FFC830" stroke-width="2.4" stroke-linecap="round"/>
{limb("M76 76 Q90 72 96 64", SK, 6)}
<circle cx="64" cy="52" r="12" fill="{SK}" {W(2.8)}/>
<path d="M52 56 Q54 72 64 70 Q74 72 76 56 Q70 62 64 60 Q58 62 52 56Z" fill="#fff" {W(2.2)}/>
<path d="M52 42 L50 30 L57 36 L64 26 L71 36 L78 30 L76 42Z" fill="#FFD040" {W(2.4)}/>
{eye(59, 50, .45)}{eye(69, 50, .45)}{blush(54, 56, .3)}{blush(74, 56, .3)}
<path d="M10 108 Q18 104 26 108 M100 112 Q108 108 116 112" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 25. «Немо» (Ховрино) — веточка коралла танцует на дне
I["aqua-nemo-khovrino"] = ("оранжевая ветвистая веточка коралла", "танцует на песчаном дне бассейна, подняв веточки-руки, вокруг поднимаются пузырьки", ("#FFF0E0", "#FF8C50"), f'''
<path d="M0 0 H128 V128 H0Z" fill="#30A8D8" opacity=".55"/>
<path d="M0 108 Q64 98 128 108 V128 H0Z" fill="#FFE6B0" {W(2.4)}/>
<path d="M64 110 V60 M64 84 L44 62 L36 40 M44 62 L28 56 M64 74 L86 52 L92 30 M86 52 L104 48 M64 60 L58 36 M64 60 L72 40" fill="none" {W(12)}/>
<path d="M64 110 V60 M64 84 L44 62 L36 40 M44 62 L28 56 M64 74 L86 52 L92 30 M86 52 L104 48 M64 60 L58 36 M64 60 L72 40" fill="none" stroke="#FF7A4A" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="36" cy="40" r="4" fill="#FFB08A"/><circle cx="92" cy="30" r="4" fill="#FFB08A"/><circle cx="58" cy="36" r="4" fill="#FFB08A"/><circle cx="72" cy="40" r="4" fill="#FFB08A"/><circle cx="28" cy="56" r="3.4" fill="#FFB08A"/><circle cx="104" cy="48" r="3.4" fill="#FFB08A"/>
<ellipse cx="64" cy="92" rx="13" ry="15" fill="#FF7A4A" {W(2.8)}/>
{eye(59, 88, .5)}{eye(69, 88, .5)}{smile(64, 95, 3.5, .8)}{blush(54, 95, .35)}{blush(74, 95, .35)}
<circle cx="20" cy="84" r="3.6" fill="none" stroke="#fff" stroke-width="2"/><circle cx="24" cy="70" r="2.4" fill="none" stroke="#fff" stroke-width="2"/><circle cx="108" cy="80" r="3" fill="none" stroke="#fff" stroke-width="2"/>''')

# 26. «Немо» (Севастопольская) — матросик машет флажками над бассейном
I["aqua-nemo-sevastopolskaya"] = ("матросик в тельняшке и бескозырке с ленточками", "стоит на бортике бассейна и машет над водой двумя сигнальными флажками", ("#FFFFFF", "#3060C0"), f'''
<path d="M0 98 H128 V128 H0Z" fill="#3AB0E8"/>
<path d="M0 90 H128 V98 H0Z" fill="#fff" {W(2.6)}/>
<path d="M14 112 Q22 108 30 112 M96 116 Q104 112 112 116" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M56 90 V76 M72 90 V76" {W(6)}/><path d="M56 90 V76 M72 90 V76" stroke="#2A3A70" stroke-width="3"/>
{limb("M52 58 L34 40", SK, 7)}{limb("M76 58 L94 40", SK, 7)}
<path d="M34 40 L26 16" {W(2.6)}/><path d="M26 16 L10 20 L14 34 L30 30Z" fill="#FFD040" {W(2.4)}/><path d="M26 16 L14 34 M10 20 L30 30" stroke="#E83A4A" stroke-width="3"/>
<path d="M94 40 L102 16" {W(2.6)}/><path d="M102 16 L118 20 L114 34 L98 30Z" fill="#FFD040" {W(2.4)}/><path d="M102 16 L114 34 M118 20 L98 30" stroke="#E83A4A" stroke-width="3"/>
<path d="M50 56 Q64 50 78 56 V80 H50Z" fill="#fff" {W(3)}/>
<path d="M50 62 H78 M50 68 H78 M50 74 H78" stroke="#2A4AA8" stroke-width="3"/>
<path d="M50 56 Q64 50 78 56 V80 H50Z" fill="none" {W(3)}/>
<path d="M56 54 L64 64 L72 54" fill="#2A4AA8" {W(2)}/>
<circle cx="64" cy="40" r="12" fill="{SK}" {W(2.8)}/>
<path d="M50 32 Q64 22 78 32 L78 30 Q64 20 50 30Z" fill="#fff" {W(2.4)}/><path d="M50 32 H78" stroke="#2A3A70" stroke-width="3"/>
<path d="M76 32 Q82 40 80 48 M74 33 Q78 42 74 48" fill="none" stroke="#2A3A70" stroke-width="2.2" stroke-linecap="round"/>
{eye(59, 41, .45)}{eye(69, 41, .45)}<path d="M60 46 Q64 50 68 46" fill="none" {W(1.8)}/>{blush(55, 46, .3)}{blush(73, 46, .3)}''')

# 27. «Немо» (Свиблово) — девочка с хвостиками пускает пузыри, опустив лицо в воду
I["aqua-nemo-sviblovo"] = ("девочка с двумя рыжими хвостиками", "опустила лицо в воду бассейна и пускает пузыри — видны макушка, хвостики и пузырьки, вид сбоку в разрезе", ("#FFF8E8", "#F0B040"), f'''
<path d="M0 60 Q32 54 64 60 T128 60 V128 H0Z" fill="#48B8E8" {W(2.6)}/>
<path d="M38 50 Q22 46 12 56 Q10 66 18 66 Q24 56 38 58Z M90 50 Q106 46 116 56 Q118 66 110 66 Q104 56 90 58Z" fill="#F08A30" {W(2.6)}/>
<circle cx="38" cy="53" r="4.4" fill="#5AD080" {W(2)}/><circle cx="90" cy="53" r="4.4" fill="#5AD080" {W(2)}/>
<path d="M36 64 Q36 34 64 34 Q92 34 92 64 Q92 84 64 86 Q36 84 36 64Z" fill="{SK}" {W(3)}/>
<path d="M36 58 Q38 34 64 34 Q90 34 92 58 Q80 48 64 48 Q48 48 36 58Z" fill="#F08A30" {W(2.6)}/>
<path d="M0 64 Q32 58 64 64 T128 64 V128 H0Z" fill="#48B8E8" opacity=".7"/>
<path d="M50 70 Q54 66 58 70 M70 70 Q74 66 78 70" fill="none" {W(2.4)}/>
<ellipse cx="64" cy="80" rx="4" ry="3.4" fill="#C8406A" {W(1.6)}/>
<circle cx="64" cy="96" r="4.4" fill="#fff" opacity=".85" {W(1.8)}/><circle cx="70" cy="108" r="5.4" fill="#fff" opacity=".85" {W(1.8)}/><circle cx="60" cy="118" r="3.4" fill="#fff" opacity=".85" {W(1.8)}/>
<path d="M0 64 Q32 58 64 64 T128 64" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>''')

# 28. «Немо» (Люберцы) — гуппи с радужным хвостом-веером плывёт за крошкой
I["aqua-nemo-lyubertsy"] = ("крошечная гуппи с огромным радужным хвостом-веером", "под водой плывёт вверх к поверхности за плавающей крошкой корма", ("#F4ECFF", "#7A50D0"), f'''
<path d="M0 0 H128 V20 Q96 26 64 20 T0 20Z" fill="#fff" opacity=".45"/>
<path d="M0 20 Q32 26 64 20 T128 20" fill="none" stroke="#fff" stroke-width="2.6"/>
<rect x="84" y="14" width="8" height="6" rx="2" fill="#E8A050" {W(1.8)}/>
<path d="M58 70 Q30 70 16 110 Q34 120 50 116 Q66 112 70 82Z" fill="#FF6AA0" {W(3)}/>
<path d="M58 72 Q36 82 26 110 M62 76 Q48 92 42 116" fill="none" stroke="#FFD040" stroke-width="5" stroke-linecap="round"/>
<path d="M60 72 Q44 88 34 114" fill="none" stroke="#5AC0F0" stroke-width="4" stroke-linecap="round"/>
<path d="M58 70 Q30 70 16 110 Q34 120 50 116 Q66 112 70 82Z" fill="none" {W(3)}/>
<path d="M58 78 Q60 50 82 34 Q96 30 94 44 Q90 64 70 82Z" fill="#B8E0B0" {W(3)}/>
{eye(86, 42, .55)}<path d="M90 50 Q92 52 94 48" fill="none" {W(1.8)}/>{blush(80, 50, .35)}
<circle cx="40" cy="40" r="3" fill="none" stroke="#fff" stroke-width="2"/><circle cx="48" cy="54" r="2" fill="none" stroke="#fff" stroke-width="2"/>''')

# 29. «Море детям» — устрица-малышка хихикает на дне
I["more-detyam-malygina"] = ("устрица-малышка в волнистой серой раковине", "приоткрылась на дне детского бассейна и хихикает, выпуская вверх цепочку пузырей", ("#E8FFFF", "#2AB0B0"), f'''
<path d="M0 0 H128 V128 H0Z" fill="#78D8F0" opacity=".45"/>
<path d="M0 104 H128 V128 H0Z" fill="#FFF0D0"/><path d="M0 104 H128" {W(2.4)}/>
<path d="M18 102 Q22 70 64 64 Q106 70 110 102 Q64 114 18 102Z" fill="#B8C0C8" {W(3)}/>
<path d="M28 98 Q36 80 50 74 M44 102 Q50 84 60 76 M84 102 Q80 84 72 76 M100 98 Q92 80 78 74" fill="none" stroke="#8A949E" stroke-width="2.2" stroke-linecap="round"/>
<path d="M22 62 Q28 26 64 22 Q100 26 106 62 Q64 72 22 62Z" fill="#C8D0D8" {W(3)}/>
<path d="M34 56 Q40 38 52 32 M94 56 Q88 38 76 32 M64 60 V28" fill="none" stroke="#9AA4AE" stroke-width="2.2" stroke-linecap="round"/>
<path d="M26 64 Q64 76 102 64 Q100 74 64 80 Q28 74 26 64Z" fill="#FFB8C8" {W(2.6)}/>
<path d="M52 66 Q55 62 58 66 M70 66 Q73 62 76 66" fill="none" {W(2.4)}/>
<path d="M58 72 Q64 77 70 72" fill="none" {W(2)}/>{blush(46, 72, .6)}{blush(82, 72, .6)}
<circle cx="80" cy="14" r="3" fill="#fff" opacity=".8" {W(1.6)}/><circle cx="72" cy="6" r="2.2" fill="#fff" opacity=".8" {W(1.4)}/>''')

# 30. «Орбита» — Сатурн плавает в бассейне, кольцо как надувной круг
I["orbita-pool-zelenograd"] = ("планета Сатурн с мордочкой", "плавает в бассейне, а своё кольцо использует как надувной круг, вокруг звёзды", ("#5A60C8", "#1A1E5A"), f'''
{sparkle(20, 26, 5, "#FFF4B0")}{sparkle(104, 18, 4, "#FFF4B0")}{sparkle(112, 44, 3, "#FFF4B0")}{sparkle(30, 52, 3, "#FFF4B0")}
<path d="M0 82 Q32 76 64 82 T128 82 V128 H0Z" fill="#3AB0F0" {W(2.6)}/>
<ellipse cx="64" cy="76" rx="50" ry="14" fill="none" {W(12)}/>
<path d="M14 76 A50 14 0 0 1 114 76" fill="none" stroke="#FFC060" stroke-width="8"/>
<circle cx="64" cy="62" r="30" fill="#F0C080" {W(3)}/>
<path d="M36 52 Q64 46 92 52 M34 64 Q64 58 94 64" fill="none" stroke="#D89A50" stroke-width="3"/>
{eye(54, 60, .6)}{eye(74, 60, .6)}{smile(64, 67, 4, .9)}{blush(46, 68, .5)}{blush(82, 68, .5)}
<path d="M14 76 A50 14 0 0 0 114 76" fill="none" {W(12)}/><path d="M14 76 A50 14 0 0 0 114 76" fill="none" stroke="#FF9A40" stroke-width="8"/>
<path d="M0 92 Q32 86 64 92 T128 92 V128 H0Z" fill="#3AB0F0" opacity=".8"/>
<path d="M10 106 Q18 102 26 106 M98 110 Q106 106 114 110" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 31. «Алтуфьевский» — орангутан плывёт на спине, закинув руки за голову
I["altufevsky-sk-pool"] = ("рыжий лохматый орангутан", "плывёт на спине по бассейну, закинув длинные руки за голову, пальцы ног торчат из воды", ("#FFF6E8", "#D06A30"), f'''
<path d="M0 60 Q32 54 64 60 T128 60 V128 H0Z" fill="#40B0E8" {W(2.6)}/>
<path d="M44 66 Q24 50 30 40 Q40 36 48 50 M84 66 Q104 50 98 40 Q88 36 80 50" fill="none" {W(9)}/>
<path d="M44 66 Q24 50 30 40 Q40 36 48 50 M84 66 Q104 50 98 40 Q88 36 80 50" fill="none" stroke="#D86A28" stroke-width="5.6" stroke-linecap="round"/>
<ellipse cx="64" cy="72" rx="26" ry="12" fill="#D86A28" {W(3)}/>
<path d="M44 70 l-4 6 M52 74 l-2 6 M76 74 l2 6 M84 70 l4 6" stroke="#B04A18" stroke-width="2" stroke-linecap="round"/>
<circle cx="64" cy="52" r="16" fill="#D86A28" {W(3)}/>
<path d="M50 40 Q56 30 64 34 Q72 30 78 40" fill="none" stroke="#B04A18" stroke-width="3" stroke-linecap="round"/>
<path d="M52 52 Q52 42 64 42 Q76 42 76 52 Q76 64 64 64 Q52 64 52 52Z" fill="#F0B890" {W(2.4)}/>
{eye(59, 50, .5)}{eye(69, 50, .5)}<path d="M58 58 Q64 62 70 58" fill="none" {W(2)}/>
<path d="M92 80 Q100 76 104 80 M100 86 Q108 82 112 86" fill="none" {W(5)}/><path d="M92 80 Q100 76 104 80 M100 86 Q108 82 112 86" fill="none" stroke="#F0B890" stroke-width="2.4" stroke-linecap="round"/>
<path d="M0 78 Q32 72 64 78 T128 78 V128 H0Z" fill="#40B0E8" opacity=".75"/>
<path d="M10 96 Q18 92 26 96 M40 110 Q48 106 56 110 M96 104 Q104 100 112 104" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 32. «Жемчужина» (Митино) — перламутровая жемчужина ныряет, рассыпая искорки
I["zhemchuzhina-pool-mitino"] = ("перламутровая жемчужина с мордочкой и сиянием", "ныряет в бассейн по дуге, рассыпая за собой искорки", ("#FFF0FA", "#C870B8"), f'''
<path d="M0 78 Q32 72 64 78 T128 78 V128 H0Z" fill="#48B8E8" {W(2.6)}/>
<path d="M16 30 Q34 14 54 26" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="2 6" stroke-linecap="round"/>
{sparkle(18, 40, 5)}{sparkle(30, 22, 4)}{sparkle(44, 18, 3)}
<circle cx="72" cy="50" r="28" fill="#FFF8FC" {W(3)}/>
<circle cx="72" cy="50" r="28" fill="#F0D8F0" opacity=".45"/>
<path d="M56 34 Q64 28 74 30" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<circle cx="86" cy="40" r="5" fill="#fff" opacity=".9"/>
{eye(64, 52, .6)}{eye(80, 52, .6)}{smile(72, 59, 4, .9)}{blush(58, 60, .5)}{blush(88, 60, .5)}
<path d="M82 84 L90 72 L94 84 L102 74 L104 86" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M14 100 Q22 96 30 100 M44 112 Q52 108 60 112" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 33. Гребной канал — мальчик-викинг гребёт в надувной ладье
I["grebnoy-kanal-pool"] = ("мальчик-викинг в рогатом шлеме", "гребёт двухлопастным веслом в надувной ладье с головой-завитком через бассейн", ("#E8F0FF", "#6A7AC8"), f'''
<path d="M0 84 Q32 78 64 84 T128 84 V128 H0Z" fill="#3AB0E8" {W(2.6)}/>
<path d="M22 20 L106 92" {W(5)}/><path d="M22 20 L106 92" stroke="#C88A50" stroke-width="2.4"/>
<path d="M14 12 Q22 8 28 18 Q22 26 14 22Z M100 86 Q108 82 114 92 Q108 100 100 96Z" fill="#FFD040" {W(2.4)}/>
<path d="M16 76 Q64 96 104 76 Q100 92 64 98 Q26 94 16 76Z" fill="#E86A30" {W(3)}/>
<path d="M104 76 Q110 60 104 52 Q96 50 98 58 Q104 60 100 66" fill="none" {W(7)}/><path d="M104 76 Q110 60 104 52 Q96 50 98 58 Q104 60 100 66" fill="none" stroke="#E86A30" stroke-width="3.6" stroke-linecap="round"/>
<circle cx="34" cy="84" r="4" fill="#FFD040" {W(1.8)}/><circle cx="52" cy="88" r="4" fill="#FFD040" {W(1.8)}/><circle cx="70" cy="88" r="4" fill="#FFD040" {W(1.8)}/>
<path d="M48 78 Q48 62 60 62 Q72 62 72 78Z" fill="#4AA060" {W(2.6)}/>
{limb("M52 68 L44 48", SK, 6)}{limb("M68 68 L74 58", SK, 6)}
<circle cx="60" cy="48" r="11" fill="{SK}" {W(2.8)}/>
<path d="M48 46 Q48 32 60 32 Q72 32 72 46Z" fill="#B8C0C8" {W(2.6)}/>
<path d="M49 40 Q40 36 40 26 Q46 32 50 34 M71 40 Q80 36 80 26 Q74 32 70 34" fill="#FFF4E0" {W(2.2)}/>
{eye(56, 50, .42)}{eye(64, 50, .42)}<path d="M57 55 Q60 58 63 55" fill="none" {W(1.6)}/>
<path d="M50 54 Q52 62 60 62 Q68 62 70 54 Q64 58 60 57 Q56 58 50 54Z" fill="#F0A040" {W(1.8)}/>''')

# 34. «Бескудниково» — какаду отряхивается после купания
I["beskudnikovo-sk-pool"] = ("белый какаду с жёлтым хохолком", "стоит на бортике после купания и отряхивается — перья торчком, брызги летят во все стороны", ("#FFFFE0", "#8FD06A"), f'''
<path d="M0 96 H128 V104 H0Z" fill="#fff" {W(2.6)}/>
<path d="M0 104 H128 V128 H0Z" fill="#3AB0E8"/>
<path d="M30 30 l-8 -6 M24 48 l-10 -2 M28 70 l-10 4 M98 30 l8 -6 M104 48 l10 -2 M100 70 l10 4 M64 8 v-6" stroke="#5AC0F0" stroke-width="3.4" stroke-linecap="round"/>
<circle cx="18" cy="60" r="3" fill="#5AC0F0"/><circle cx="110" cy="60" r="3" fill="#5AC0F0"/><circle cx="40" cy="14" r="2.6" fill="#5AC0F0"/>
<path d="M56 96 V86 M70 96 V86" {W(5)}/><path d="M56 96 V86 M70 96 V86" stroke="#9A9AA8" stroke-width="2.4"/>
<path d="M40 70 Q34 52 44 46 L36 40 L48 42 L42 32 L54 40 Q64 34 74 40 L86 32 L80 42 L92 40 L84 46 Q94 52 88 70 Q92 80 84 88 L92 92 L78 90 Q64 94 50 90 L36 92 L44 88 Q36 80 40 70Z" fill="#fff" {W(3)}/>
<path d="M50 34 Q44 14 52 6 Q56 18 58 30 Q60 12 70 6 Q68 20 66 30 Q74 16 84 14 Q76 26 72 34" fill="#FFE040" {W(2.6)}/>
<path d="M66 56 Q76 56 76 64 Q72 72 66 68Z" fill="#3A3A4A" {W(2)}/>
{eye(58, 54, .6)}{blush(54, 62, .5)}''')

# 35. «Бусиново» — индюк распустил хвост на надувном матрасе
I["businovo-sk-pool"] = ("индюк с красной бородкой и пёстрым хвостом", "распустил хвост веером, лёжа на голубом надувном матрасе посреди бассейна", ("#FFF4E0", "#C88A40"), f'''
<path d="M0 80 Q32 74 64 80 T128 80 V128 H0Z" fill="#3AB0E8" {W(2.6)}/>
<path d="M64 74 L30 30 Q46 20 64 18 Q82 20 98 30Z" fill="#8A5A30" {W(3)}/>
<path d="M64 74 L36 32 M64 74 L50 22 M64 74 L64 18 M64 74 L78 22 M64 74 L92 32" stroke="#E8A040" stroke-width="4"/>
<path d="M30 30 Q46 20 64 18 Q82 20 98 30" fill="none" stroke="#FFE070" stroke-width="5"/>
<path d="M64 74 L30 30 Q46 20 64 18 Q82 20 98 30Z" fill="none" {W(3)}/>
<path d="M20 86 Q20 76 32 76 H96 Q108 76 108 86 Q108 96 96 96 H32 Q20 96 20 86Z" fill="#9AD8FF" {W(3)}/>
<path d="M40 78 V94 M56 78 V94 M72 78 V94 M88 78 V94" stroke="#70B8E8" stroke-width="2.2"/>
<ellipse cx="62" cy="68" rx="18" ry="14" fill="#6A4028" {W(3)}/>
<path d="M50 56 Q52 38 62 38 Q70 38 70 50" fill="none" {W(9)}/><path d="M50 56 Q52 38 62 38 Q70 38 70 50" fill="none" stroke="#5A8AD0" stroke-width="5.6" stroke-linecap="round"/>
<circle cx="62" cy="38" r="8" fill="#5A8AD0" {W(2.6)}/>
<path d="M68 38 L76 40 L68 43Z" fill="#FFC040" {W(1.6)}/>
<path d="M66 44 Q70 54 64 54 Q62 48 64 44Z" fill="#E83A3A" {W(1.8)}/>
{eye(61, 36, .45)}''')

# 36. СК «Дельфин» — мальчик в моноласте плывёт под водой «дельфином»
I["delfin-sk-nekrasovka"] = ("мальчик в синей моноласте и красной шапочке", "плывёт под водой волной, «дельфином», ноги вместе в одной большой ласте, вид сбоку", ("#E8FFFA", "#1A8A9A"), f'''
<path d="M0 0 H128 V128 H0Z" fill="#3AB8E0" opacity=".5"/>
<path d="M0 22 Q32 16 64 22 T128 22" fill="none" stroke="#fff" stroke-width="3"/>
<path d="M0 116 H128 V128 H0Z" fill="#D8F0F4"/><path d="M0 116 H128" {W(2.2)}/>
{limb("M98 62 L116 50", SK, 7)}{limb("M96 68 L116 62", SK, 7)}
<path d="M40 78 Q60 56 92 62 Q96 70 92 74 Q66 70 46 88Z" fill="#20306A" {W(3)}/>
<path d="M44 86 Q34 94 26 96" fill="none" {W(10)}/><path d="M44 86 Q34 94 26 96" fill="none" stroke="#F8C8A8" stroke-width="6.6" stroke-linecap="round"/>
<path d="M28 94 Q10 82 4 92 Q8 106 2 116 Q18 112 30 100Z" fill="#2A60E0" {W(3)}/>
<path d="M10 94 Q14 104 8 112" fill="none" stroke="#7AA8FF" stroke-width="2.4" stroke-linecap="round"/>
<circle cx="100" cy="58" r="11" fill="{SK}" {W(2.8)}/>
<path d="M90 54 Q92 44 102 46 Q112 48 110 58 Q100 50 90 54Z" fill="#E83A3A" {W(2.4)}/>
{eye(104, 60, .45)}<path d="M100 66 Q104 68 107 65" fill="none" {W(1.6)}/>{blush(98, 64, .3)}
<circle cx="112" cy="40" r="3" fill="none" stroke="#fff" stroke-width="2"/><circle cx="116" cy="30" r="2" fill="none" stroke="#fff" stroke-width="2"/>
<path d="M30 60 Q36 54 42 60 M54 40 Q60 34 66 40" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" opacity=".7"/>''')

# 37. «Курьяново» — рябая курочка в шапочке сидит в надувном круге
I["kuryanovo-fok-pool"] = ("рябая курочка с красным гребешком в белой плавательной шапочке", "важно сидит в полосатом надувном круге посреди бассейна, крылышки на круге", ("#FFF2F2", "#E05A6A"), f'''
<path d="M0 78 Q32 72 64 78 T128 78 V128 H0Z" fill="#40B8E8" {W(2.6)}/>
<ellipse cx="64" cy="84" rx="40" ry="14" fill="#fff" {W(3)}/>
<path d="M32 76 L28 90 M64 70 V98 M96 76 L100 90" stroke="#FF5A6A" stroke-width="9"/>
<ellipse cx="64" cy="84" rx="40" ry="14" fill="none" {W(3)}/>
<ellipse cx="64" cy="84" rx="22" ry="6" fill="#40B8E8" {W(2.4)}/>
<path d="M44 82 Q40 50 64 46 Q88 50 84 82Z" fill="#C89060" {W(3)}/>
<path d="M52 60 l3 3 M62 56 l3 3 M72 60 l3 3 M54 72 l3 3 M68 70 l3 3" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M44 74 Q30 70 32 80 Q38 84 46 80Z M84 74 Q98 70 96 80 Q90 84 82 80Z" fill="#A87040" {W(2.4)}/>
<circle cx="64" cy="38" r="15" fill="#C89060" {W(3)}/>
<path d="M50 34 Q50 20 64 20 Q78 20 78 34 Q64 28 50 34Z" fill="#fff" {W(2.4)}/>
<path d="M58 20 Q58 12 62 14 Q64 8 68 14 Q72 12 70 20" fill="#E83A3A" {W(2.2)}/>
<path d="M62 42 L64 48 L67 42Z" fill="#FFB030" {W(1.8)}/><path d="M62 49 Q64 56 66 49" fill="#E83A3A" {W(1.6)}/>
{eye(58, 38, .5)}{eye(70, 38, .5)}{blush(54, 44, .35)}{blush(74, 44, .35)}''')

# 38. «Олимпийская деревня-80» — олимпийский факел плывёт на спине, держа огонь над водой
I["olimp80-pool"] = ("олимпийский факел с мордочкой и живым огоньком", "плывёт на спине по бассейну, бережно держа свой огонь над водой, чтобы не погас", ("#FFF8E0", "#E8A020"), f'''
<path d="M0 70 Q32 64 64 70 T128 70 V128 H0Z" fill="#3AB0E8" {W(2.6)}/>
<path d="M18 74 L80 54 L86 66 L24 88Z" fill="#E8C060" {W(3)}/>
<path d="M30 74 L82 58 M34 82 L84 64" stroke="#C89A30" stroke-width="2"/>
<path d="M80 54 L96 46 L102 60 L86 66Z" fill="#C8C8D8" {W(2.8)}/>
<path d="M98 50 Q92 34 104 20 Q104 32 112 30 Q118 42 112 52 Q106 58 98 50Z" fill="#FF7A2A" {W(2.6)}/>
<path d="M102 50 Q100 40 106 34 Q108 42 110 46 Q108 52 102 50Z" fill="#FFE040"/>
{eye(46, 72, .5)}{eye(58, 68, .5)}<path d="M48 80 Q54 82 60 76" fill="none" {W(2)}/>{blush(40, 80, .4)}
{limb("M40 66 L34 54", "#E8C060", 6)}{limb("M66 60 L74 46", "#E8C060", 6)}
<path d="M0 82 Q32 76 64 82 T128 82 V128 H0Z" fill="#3AB0E8" opacity=".8"/>
<path d="M10 100 Q18 96 26 100 M50 112 Q58 108 66 112 M96 104 Q104 100 112 104" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 39. «Про.Плыть» (Алтайская) — мальчик делает стартовый прыжок с тумбы
I["proplyt-altaysky"] = ("мальчик в жёлтой шапочке и зелёных плавках", "оттолкнулся от стартовой тумбы и летит над водой вытянутой стрелой, руки вперёд", ("#F0FFF0", "#2A9A6A"), f'''
<path d="M0 92 Q32 86 64 92 T128 92 V128 H0Z" fill="#3AB0E8" {W(2.6)}/>
<path d="M0 64 H24 V128 H0Z" fill="#fff" {W(3)}/><path d="M0 64 H26 L22 72 H0Z" fill="#5AD080" {W(2.4)}/>
<path d="M30 58 L8 52" fill="none" {W(8)}/><path d="M30 58 L8 52" fill="none" stroke="{SK}" stroke-width="4.6" stroke-linecap="round"/>
<path d="M28 60 L6 60" fill="none" {W(8)}/><path d="M28 60 L6 60" fill="none" stroke="{SK}" stroke-width="4.6" stroke-linecap="round"/>
<path d="M28 52 Q50 42 80 46 L82 58 Q54 62 30 64Z" fill="{SK}" {W(3)}/>
<path d="M28 52 L40 50 L42 62 L30 64Z" fill="#3AA050" {W(2.4)}/>
<path d="M84 46 L120 40 M84 56 L120 52" fill="none" {W(8)}/><path d="M84 46 L120 40 M84 56 L120 52" fill="none" stroke="{SK}" stroke-width="4.6" stroke-linecap="round"/>
<circle cx="88" cy="48" r="11" fill="{SK}" {W(2.8)}/>
<path d="M78 44 Q80 34 90 36 Q100 38 98 46 Q88 40 78 44Z" fill="#FFD020" {W(2.4)}/>
{eye(90, 50, .45)}<path d="M88 56 Q92 58 95 55" fill="none" {W(1.6)}/>{blush(84, 55, .3)}
<path d="M40 74 Q60 70 80 74" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 6" stroke-linecap="round"/>
<path d="M60 108 Q68 104 76 108 M96 112 Q104 108 112 112" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 40. «Про.Плыть» (Дегунино) — девочка делает кувырок-поворот под водой у стенки
I["proplyt-degunino"] = ("девочка в оранжевой шапочке и синем купальнике", "делает кувырок-поворот под водой у стенки бассейна, свернувшись клубочком, вокруг пузыри", ("#FFF0E8", "#E87A40"), f'''
<path d="M0 0 H128 V128 H0Z" fill="#48B0E0" opacity=".55"/>
<path d="M0 18 Q32 12 64 18 T128 18" fill="none" stroke="#fff" stroke-width="3"/>
<path d="M104 0 H128 V128 H104Z" fill="#fff" {W(3)}/>
<path d="M104 30 H128 M104 60 H128 M104 90 H128" stroke="#C8D8E8" stroke-width="2"/>
<path d="M104 54 H128 V66 H104Z" fill="#2A3050"/>
<path d="M74 52 Q90 46 96 58 Q94 72 80 70" fill="none" {W(8)}/><path d="M74 52 Q90 46 96 58 Q94 72 80 70" fill="none" stroke="{SK}" stroke-width="4.6" stroke-linecap="round"/>
<path d="M76 46 Q92 36 100 48" fill="none" {W(8)}/><path d="M76 46 Q92 36 100 48" fill="none" stroke="{SK}" stroke-width="4.6" stroke-linecap="round"/>
<path d="M44 52 Q50 34 70 40 Q82 48 76 68 Q64 82 50 76 Q40 66 44 52Z" fill="#2A60D0" {W(3)}/>
{limb("M50 74 Q46 86 58 92", SK, 7)}
<circle cx="56" cy="92" r="12" fill="{SK}" {W(2.8)}/>
<path d="M44 92 Q44 104 56 104 Q68 104 68 94 Q56 98 44 92Z" fill="#FF8A2A" {W(2.4)}/>
<path d="M50 88 Q52 86 54 88 M58 88 Q60 86 62 88" fill="none" {W(1.8)}/>
<path d="M53 82 Q56 80 59 82" fill="none" {W(1.6)}/>{blush(48, 86, .3)}{blush(64, 86, .3)}
<circle cx="30" cy="60" r="4" fill="none" stroke="#fff" stroke-width="2"/><circle cx="24" cy="44" r="3" fill="none" stroke="#fff" stroke-width="2"/><circle cx="34" cy="30" r="2.2" fill="none" stroke="#fff" stroke-width="2"/>''')


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
