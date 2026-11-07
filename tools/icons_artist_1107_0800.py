"""Робот «художник», 07.11 ~08:00 UTC: 40 иконок из самых похожих пар auto/icon-repeats.json
(старые генераторы «блюдо × сцена», серии баскетбола/волейбола/бассейнов). Из каждой пары одну оставили,
вторую придумали и нарисовали заново, вручную: свой герой по теме места, своя сцена, ракурс и палитра.
Запуск из корня: python3 tools/icons_artist_1107_0800.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT

I = {}


def note(x, y, c="#fff"):
    return (f'<ellipse cx="{x}" cy="{y}" rx="4" ry="3" fill="{c}" {W(1.8)}/>'
            f'<path d="M{x+4} {y} V{y-13} Q{x+8} {y-10} {x+10} {y-6}" fill="none" {W(2)}/>')


# 0. Селёдочная (ВДНХ, рыбный) — селёдка под шубой укрылась салатом как одеялом
I["cafe-selyodochnaya-vdnh"] = ("селёдка под свекольной «шубой»", "выглядывает из-под слоёного салата на блюде, натянув шубу как одеяло", ("#FDE8F1", "#A4305E"), f'''
<ellipse cx="64" cy="98" rx="54" ry="16" fill="#fff" {W(3)}/><ellipse cx="64" cy="96" rx="44" ry="10" fill="#EAF2F8"/>
<path d="M22 92 Q22 62 64 60 Q106 62 106 92 Q64 102 22 92Z" fill="#B0285A" {W(3)}/>
<path d="M26 84 Q64 94 102 84" fill="none" stroke="#FFE07A" stroke-width="4"/>
<path d="M24 76 Q64 86 104 76" fill="none" stroke="#F5F0E0" stroke-width="3.4"/>
<path d="M40 66 Q44 62 48 66 M60 62 Q64 58 68 62 M80 66 Q84 62 88 66" fill="none" stroke="#7CCB5A" stroke-width="2.6" stroke-linecap="round"/>
<path d="M18 58 Q30 40 50 50 Q44 60 30 64Z" fill="#B8C8D8" {W(3)}/>
<path d="M18 58 Q10 54 6 60 Q10 64 18 62" fill="#B8C8D8" {W(2.4)}/>
<path d="M30 54 Q34 50 40 52" fill="none" stroke="#8090A8" stroke-width="2"/>
{eye(42, 54, .5)}<path d="M46 60 Q48 62 50 60" fill="none" {W(1.8)}/>{blush(38, 60, .4)}
<path d="M98 50 Q110 46 112 58 Q104 58 100 62Z" fill="#B8C8D8" {W(2.6)}/>
{sparkle(92, 30, 5)}''')

# 1. Хачапури (Московский) — мегрельский хачапури: кусочек убегает, тянет сыр
I["cafe-khachapuri-moskovsky"] = ("мегрельский хачапури, нарезанный на кусочки", "один кусочек убегает в сторону, растягивая длинную сырную ниточку", ("#FFF5D8", "#E0962A"), f'''
<ellipse cx="54" cy="104" rx="46" ry="9" fill="#fff" {W(3)}/>
<path d="M54 66 L92 76 A40 34 0 1 1 82 46Z" fill="#D88A3A" {W(3)}/>
<path d="M54 66 L84 74 A31 26 0 1 1 76 50Z" fill="#FFE89A"/>
<path d="M54 66 L22 58 M54 66 L44 96" stroke="#C8782A" stroke-width="2"/>
<ellipse cx="38" cy="70" rx="5" ry="3" fill="#E8A040"/><ellipse cx="62" cy="86" rx="6" ry="3" fill="#E8A040"/><ellipse cx="44" cy="50" rx="4" ry="2.4" fill="#E8A040"/><ellipse cx="74" cy="84" rx="3" ry="2" fill="#E8A040"/>
{eye(36, 80, .5)}{eye(50, 82, .5)}{smile(43, 89, 3.5, .7)}{blush(30, 86, .4)}
<path d="M80 60 Q94 62 98 54" fill="none" stroke="#FFE27A" stroke-width="5" stroke-linecap="round"/>
<path d="M80 60 Q94 62 98 54" fill="none" {W(1.4)}/>
<path d="M90 56 L112 22 A40 34 0 0 1 120 56Z" fill="#D88A3A" {W(3)}/><path d="M96 52 L110 30 A32 28 0 0 1 114 52Z" fill="#FFE89A"/>
{eye(104, 44, .4)}{eye(112, 44, .4)}<ellipse cx="108" cy="50" rx="2.2" ry="1.8" fill="{O}"/>
<path d="M118 66 L124 72 M110 66 L112 74" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 3. Причал (Ильинское) — форель загорает в шезлонге на причале
I["cafe-prichal-ilinskoe"] = ("запечённая форель с долькой лимона", "загорает в шезлонге на деревянном причале у воды", ("#E6FBFF", "#2F9FC0"), f'''
<circle cx="100" cy="26" r="11" fill="#FFE066" {W(2.4)}/>
<path d="M0 100 Q16 96 32 100 T64 100 T96 100 T128 100 V128 H0Z" fill="#3FA6D8" {W(2.4)}/>
<path d="M4 86 H124 V96 H4Z" fill="#C98A50" {W(3)}/><path d="M28 86 V96 M54 86 V96 M80 86 V96 M106 86 V96" stroke="#9A5E2E" stroke-width="2"/>
<path d="M20 96 V118 M108 96 V118" {W(5)}/>
<path d="M30 86 L44 54 L92 54 L104 86" fill="none" {W(3.4)}/>
<path d="M40 60 L86 60 L96 84 L48 84Z" fill="#F0607A" {W(2.8)}/><path d="M54 60 L58 84 M70 60 L74 84" stroke="#fff" stroke-width="3"/>
<path d="M36 70 Q60 52 92 66 Q60 84 36 70Z" fill="#D8A060" {W(3)}/>
<path d="M92 66 L106 56 L104 76Z" fill="#D8A060" {W(2.6)}/>
<path d="M52 66 L58 72 M64 64 L70 70 M76 64 L82 70" stroke="#A86A30" stroke-width="2"/>
<rect x="34" y="62" width="14" height="6" rx="3" fill="#2A2F4A"/><path d="M40 64 H42" stroke="#fff" stroke-width="1.4"/>
<path d="M42 74 Q46 76 50 74" fill="none" {W(1.8)}/>
<path d="M72 50 A9 9 0 0 1 90 50Z" fill="#FFE45A" {W(2.2)}/><path d="M81 50 V42 M75 48 L79 44 M87 48 L83 44" stroke="#E8C020" stroke-width="1.4"/>''')

# 4. Нияма (ТРЦ «Columbus») — онигири-мореплаватель на плоту из палочек
I["cafe-niyama-columbus"] = ("онигири-мореплаватель", "плывёт открывать новые земли на плотике из палочек для еды с парусом-нори", ("#EAF7FF", "#2E6FB8"), f'''
<path d="M0 98 Q16 92 32 98 T64 98 T96 98 T128 98 V128 H0Z" fill="#2E86D0" {W(2.4)}/>
<path d="M16 110 Q22 106 28 110 M90 114 Q96 110 102 114" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>
<path d="M18 92 H110 M20 98 H108" stroke="#C88A3A" stroke-width="5" stroke-linecap="round"/><path d="M18 92 H110 M20 98 H108" {W(1.6)}/>
<path d="M88 92 V22" {W(3.2)}/><path d="M90 26 Q114 40 90 70Z" fill="#2E4A3A" {W(2.8)}/>
<path d="M60 30 L92 22" fill="none" stroke="#E8384A" stroke-width="0"/>
<path d="M88 22 L100 18 L88 14Z" fill="#E8384A" {W(2)}/>
<path d="M50 32 Q56 26 62 32 L84 82 Q86 92 76 92 H36 Q26 92 28 82Z" fill="#fff" {W(3)}/>
<path d="M36 70 H76 L80 82 Q82 92 74 92 H38 Q30 92 32 82Z" fill="#2E4A3A" {W(2.4)}/>
{eye(48, 56, .5)}{eye(62, 56, .5)}{smile(55, 63, 3.5, .7)}{blush(44, 62, .45)}{blush(66, 62, .45)}
<circle cx="45" cy="44" r="1.6" fill="#333"/><circle cx="64" cy="44" r="1.6" fill="#333"/>''')

# 5. Милана (Жуковский) — лазанья машет самолётику авиасалона
I["cafe-milana-zhukovsky"] = ("кусок лазаньи слоями с сырной корочкой", "задрав голову, машет пролетающему в небе самолётику авиасалона", ("#F0F6FF", "#5E86C8"), f'''
<path d="M70 26 Q86 18 104 24 M18 46 Q30 40 44 44" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="4 5" stroke-linecap="round"/>
<path d="M98 22 L120 18 L118 24 L100 28Z" fill="#E8384A" {W(2.2)}/><path d="M106 22 L110 12 L114 22 M106 26 L112 34" fill="#fff" {W(2)}/>
<ellipse cx="64" cy="112" rx="50" ry="10" fill="#fff" {W(3)}/>
<path d="M28 60 L94 54 L100 108 L32 112Z" fill="#F5D7A0" {W(3)}/>
<path d="M30 74 L96 68 M31 88 L98 82 M32 100 L99 94" stroke="#D8402A" stroke-width="5"/>
<path d="M30 74 L96 68 M31 88 L98 82 M32 100 L99 94" stroke="#FFE9B8" stroke-width="1.4"/>
<path d="M26 60 Q40 50 56 58 Q70 48 84 56 Q94 50 96 56 L94 62 L28 66Z" fill="#E89A3A" {W(2.6)}/>
<circle cx="44" cy="58" r="2" fill="#B8601A"/><circle cx="76" cy="56" r="2" fill="#B8601A"/>
{eye(52, 78, .5)}{eye(70, 76, .5)}<ellipse cx="62" cy="86" rx="3" ry="2.4" fill="{O}"/>
<path d="M98 76 Q110 64 108 52" fill="none" {W(3.4)}/><circle cx="108" cy="50" r="4" fill="#F5D7A0" {W(2.2)}/>
<path d="M114 44 L118 40 M116 52 H121" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>''')

# 6. Рапсодия (Зеленоград) — торт-пианино, малинка играет мелодию
I["cafe-rapsodiya-zelenograd"] = ("торт-пианино с клавишами из шоколада и крема", "по клавишам прыгает малинка и играет мелодию, вылетают ноты", ("#FFEFF4", "#D0567E"), f'''
<ellipse cx="64" cy="108" rx="52" ry="9" fill="#fff" {W(3)}/>
<path d="M16 66 H112 V104 H16Z" fill="#6A3A2A" {W(3)}/>
<path d="M18 74 H110 V102 H18Z" fill="#fff" {W(2)}/>
<path d="M31 74 V102 M44 74 V102 M57 74 V102 M70 74 V102 M83 74 V102 M96 74 V102" stroke="{O}" stroke-width="1.8"/>
<path d="M27 74 H35 V90 H27Z M40 74 H48 V90 H40Z M66 74 H74 V90 H66Z M79 74 H87 V90 H79Z M92 74 H100 V90 H92Z" fill="#3A2420"/>
<path d="M14 66 Q24 58 34 66 Q44 58 54 66 Q64 58 74 66 Q84 58 94 66 Q104 58 114 66" fill="#FFF4F8" {W(2.6)}/>
{eye(52, 52, .55)}{eye(76, 52, .55)}{smile(64, 58, 4, .8)}
<circle cx="58" cy="70" r="0" fill="none"/>
<circle cx="60" cy="38" r="9" fill="#E8304A" {W(2.4)}/><circle cx="56" cy="35" r="1.4" fill="#FFB0C0"/><circle cx="62" cy="40" r="1.4" fill="#FFB0C0"/><circle cx="64" cy="34" r="1.4" fill="#FFB0C0"/>
<path d="M58 29 L60 24 L64 28" fill="#5AB04A" {W(1.8)}/>
<path d="M56 50 Q58 46 60 48" fill="none" stroke="#fff" stroke-width="0"/>
{note(28, 34)}{note(92, 26, "#FFE07A")}{note(104, 48)}''')

# 8. MiMi (Пироговская, грузинская, доски для рисования) — чурчхела-гусеница рисует мелом
I["cafe-mimi-pirogovskaya"] = ("чурчхела-гусеница из бусин-орешков", "ползёт по школьной грифельной доске, оставляя меловой рисунок-солнышко", ("#EAF5EC", "#3B6E55"), f'''
<rect x="10" y="18" width="108" height="78" rx="6" fill="#2E4A3E" {W(3)}/><rect x="10" y="18" width="108" height="78" rx="6" fill="none" stroke="#C8904A" stroke-width="5"/>
<circle cx="34" cy="42" r="8" fill="none" stroke="#fff" stroke-width="2.4"/><path d="M34 28 V31 M34 53 V56 M20 42 H23 M45 42 H48 M24 32 L26 34 M42 32 L44 34" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>
<path d="M50 54 Q60 44 70 54" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 4" stroke-linecap="round"/>
<path d="M20 70 Q30 60 40 70 Q50 80 60 70" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<circle cx="64" cy="80" r="10" fill="#8A2A3A" {W(2.6)}/><circle cx="78" cy="74" r="10" fill="#9A3242" {W(2.6)}/><circle cx="92" cy="70" r="10" fill="#8A2A3A" {W(2.6)}/>
<circle cx="106" cy="66" r="11" fill="#A63A4A" {W(2.8)}/>
<path d="M104 55 Q102 46 98 44 M110 55 Q112 46 116 44" fill="none" {W(2)}/><circle cx="98" cy="44" r="2" fill="{O}"/><circle cx="116" cy="44" r="2" fill="{O}"/>
{eye(102, 64, .4)}{eye(111, 64, .4)}<path d="M103 71 Q106 73 109 71" fill="none" stroke="#fff" stroke-width="1.8"/>
<path d="M54 82 L44 88" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
<path d="M30 108 H98" {W(4)}/>''')

# 9. Miraclub (Мытищи) — бургер-башня с оливкой-флажком
I["cafe-miraclub-mytishchi"] = ("бургер-башня в пять этажей", "шатается, а на вершине оливка на шпажке развевается как флажок", ("#FFF0F0", "#E05050"), f'''
<path d="M66 4 V30" {W(2.6)}/><path d="M66 6 L82 11 L66 16Z" fill="#FFE07A" {W(2)}/><circle cx="66" cy="24" r="5" fill="#4A6A2A" {W(2)}/>
<path d="M40 40 Q64 22 90 40Z" fill="#E8A44A" {W(3)}/>
<circle cx="56" cy="34" r="1.4" fill="#fff"/><circle cx="68" cy="31" r="1.4" fill="#fff"/><circle cx="78" cy="35" r="1.4" fill="#fff"/>
<path d="M38 40 Q62 46 92 40 L92 48 Q62 52 38 48Z" fill="#6AC04A" {W(2.4)}/>
<rect x="36" y="48" width="58" height="10" rx="5" fill="#7A3E22" {W(2.4)}/>
<path d="M34 58 H96 L90 64 L82 58 L74 64 L66 58 L58 64 L50 58 L42 64Z" fill="#FFD23A" {W(2.2)}/>
<rect x="34" y="64" width="60" height="10" rx="5" fill="#7A3E22" {W(2.4)}/>
<path d="M36 74 Q64 70 94 74 L94 80 H36Z" fill="#E8384A" {W(2.2)}/>
<rect x="32" y="80" width="62" height="11" rx="5" fill="#7A3E22" {W(2.4)}/>
<path d="M30 92 H96 Q98 108 64 108 Q30 108 30 92Z" fill="#E8A44A" {W(3)}/>
{eye(54, 98, .45)}{eye(72, 98, .45)}<path d="M59 103 Q63 106 67 103" fill="none" {W(1.8)}/>
<path d="M22 50 Q16 60 22 70 M106 50 Q112 60 106 70" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<ellipse cx="64" cy="118" rx="40" ry="5" fill="#B03A3A" opacity=".3"/>''')

# 10. IL Патио (Мичуринский) — пицца-маргарита в патио под гирляндой
I["cafe-ilpatio-michurinsky"] = ("пицца-маргарита целиком с листиками базилика", "лежит на столике в вечернем патио под гирляндой лампочек и жмурится от удовольствия", ("#FFE9C8", "#C2562A"), f'''
<path d="M-4 22 Q32 40 64 26 Q96 40 132 22" fill="none" {W(2)}/>
<circle cx="14" cy="30" r="5" fill="#FFE45A" {W(1.8)}/><circle cx="40" cy="34" r="5" fill="#FF8A5A" {W(1.8)}/><circle cx="64" cy="27" r="5" fill="#FFE45A" {W(1.8)}/><circle cx="88" cy="34" r="5" fill="#8AD0FF" {W(1.8)}/><circle cx="114" cy="30" r="5" fill="#FFE45A" {W(1.8)}/>
<path d="M0 104 H128 V128 H0Z" fill="#8A4A2A" {W(2.4)}/>
<ellipse cx="64" cy="82" rx="50" ry="26" fill="#E8A44A" {W(3)}/>
<ellipse cx="64" cy="80" rx="42" ry="20" fill="#E8402A"/>
<path d="M34 76 Q40 70 48 76 Q56 82 50 88 Q40 90 34 76Z M76 70 Q86 66 92 74 Q94 84 84 84 Q74 80 76 70Z M58 88 Q66 84 72 90 Q66 96 58 88Z" fill="#FFF4D8"/>
<path d="M44 70 Q48 64 54 68 Q50 72 44 70Z M84 88 Q88 82 94 86 Q90 90 84 88Z" fill="#3AA048" {W(1.4)}/>
<path d="M56 74 Q60 71 64 74 M70 74 Q74 71 78 74" fill="none" {W(2.2)}/>{smile(67, 80, 4, .7)}
{blush(54, 80, .5)}{blush(82, 80, .5)}''')

# 11. Сирень (парк Сокольники) — сиреневый зефир-цветок в ветке сирени
I["cafe-siren-sokolniki"] = ("сиреневый зефир-цветок", "прячется в цветущей ветке сирени в парке и подставляет щёчки солнцу", ("#F7F0FF", "#9A70D8"), f'''
<circle cx="104" cy="22" r="10" fill="#FFE45A" {W(2.2)}/>
<path d="M10 120 Q30 90 40 70 M40 70 Q50 60 46 44" fill="none" stroke="#6A4A2A" stroke-width="4" stroke-linecap="round"/>
<path d="M20 96 Q4 92 6 80 Q18 80 20 96Z M36 74 Q22 64 30 54 Q40 62 36 74Z" fill="#6AB84A" {W(2)}/>
<g fill="#B58AE8" {W(1.6)}><circle cx="30" cy="40" r="6"/><circle cx="40" cy="30" r="6"/><circle cx="52" cy="38" r="6"/><circle cx="36" cy="50" r="6"/><circle cx="48" cy="50" r="6"/><circle cx="44" cy="20" r="5"/><circle cx="56" cy="26" r="5"/></g>
<g fill="#C9A6F2" {W(1.6)}><circle cx="92" cy="96" r="5"/><circle cx="104" cy="88" r="5"/><circle cx="112" cy="100" r="5"/><circle cx="100" cy="108" r="5"/></g>
<path d="M78 46 Q88 36 98 46 Q110 50 104 62 Q112 74 98 78 Q90 90 78 80 Q64 84 62 70 Q52 60 64 52 Q66 40 78 46Z" fill="#E6D2FF" {W(3)}/>
<path d="M70 56 Q80 50 92 58 M66 70 Q80 76 96 68" fill="none" stroke="#C8A8F0" stroke-width="2"/>
{eye(74, 62, .5)}{eye(88, 62, .5)}{smile(81, 69, 3.5, .7)}{blush(68, 68, .5)}{blush(94, 68, .5)}''')

# 14. Местные (Фили, азиатская) — сяолунбао пьёт бульон через соломинку
I["cafe-mestnye-fili"] = ("пельмешек-сяолунбао с хохолком-защипом", "пьёт свой бульон через соломинку, сидя в бамбуковой корзинке", ("#FFF8E6", "#C9A04A"), f'''
<path d="M18 86 H110 L104 114 Q64 122 24 114Z" fill="#E8C070" {W(3)}/>
<path d="M22 96 H106 M24 106 H104" stroke="#B88A3A" stroke-width="2.2"/>
<ellipse cx="64" cy="86" rx="46" ry="8" fill="#D8AA5A" {W(3)}/>
<path d="M28 84 Q26 52 64 46 Q102 52 100 84Z" fill="#FFF8EE" {W(3)}/>
<path d="M64 46 Q58 34 64 26 Q70 34 64 46" fill="#FFF8EE" {W(2.4)}/>
<path d="M64 46 L44 60 M64 46 L54 62 M64 46 L74 62 M64 46 L84 60" stroke="#E6D8C0" stroke-width="2"/>
{eye(52, 70, .55)}{eye(74, 70, .55)}{blush(44, 77, .5)}{blush(82, 77, .5)}
<circle cx="63" cy="78" r="2.6" fill="{O}"/>
<path d="M63 78 L96 30" stroke="#FF6A8A" stroke-width="4" stroke-linecap="round"/><path d="M96 30 L104 28" stroke="#FF6A8A" stroke-width="4" stroke-linecap="round"/>
<circle cx="108" cy="44" r="3" fill="#fff" opacity=".8"/><circle cx="114" cy="34" r="2" fill="#fff" opacity=".8"/>''')

# 15. Клёвый (Ромашково, рыбный у пруда) — карасик в салфетке, над ним клюёт поплавок
I["cafe-klevyi-romashkovo"] = ("карасик в салфетке на шее", "сидит на тарелке у пруда с камышами, а рядом подпрыгивает поплавок удочки", ("#E8FFF0", "#4FA060"), f'''
<path d="M84 0 Q100 30 104 56" fill="none" stroke="#fff" stroke-width="1.6"/>
<path d="M0 84 H128 V128 H0Z" fill="#4AA0C8" {W(2.4)}/>
<path d="M14 84 V40 M22 84 V50 M116 84 V44" stroke="#4A7A3A" stroke-width="3"/>
<ellipse cx="14" cy="38" rx="3" ry="8" fill="#8A5A2A"/><ellipse cx="116" cy="42" rx="3" ry="8" fill="#8A5A2A"/>
<ellipse cx="104" cy="66" rx="5" ry="8" fill="#fff" {W(2)}/><path d="M99 62 Q104 54 109 62Z" fill="#E8384A" {W(2)}/>
<path d="M94 76 Q104 72 114 76" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
<ellipse cx="58" cy="102" rx="46" ry="12" fill="#fff" {W(3)}/>
<path d="M22 72 Q50 40 82 66 Q50 98 22 72Z" fill="#F2B83A" {W(3)}/>
<path d="M82 66 L98 52 L98 82Z" fill="#F2B83A" {W(2.6)}/>
<path d="M50 52 Q60 44 66 54" fill="#E8A030" {W(2)}/>
<path d="M54 60 L60 70 M62 60 L68 70 M70 62 L74 70" stroke="#D8962A" stroke-width="1.8"/>
{eye(36, 66, .5)}<path d="M26 74 Q30 77 34 74" fill="none" {W(1.8)}/>
<path d="M38 76 L52 70 L46 88Z" fill="#fff" {W(2.2)}/><path d="M42 76 L48 80" stroke="#E8384A" stroke-width="1.6"/>''')

# 16. Князь Багратион (Плющиха) — торт «Наполеон» в треуголке отдаёт честь
I["cafe-knyaz-bagration"] = ("кусок торта «Наполеон» в треуголке", "стоит на тарелке навытяжку и отдаёт честь", ("#FFF1DC", "#B07A40"), f'''
<ellipse cx="64" cy="110" rx="48" ry="9" fill="#fff" {W(3)}/>
<path d="M30 56 H98 V106 H30Z" fill="#FFF2D6" {W(3)}/>
<path d="M30 64 H98 M30 74 H98 M30 84 H98 M30 94 H98" stroke="#D8A060" stroke-width="3"/>
<path d="M30 56 H98" stroke="#F2E0B8" stroke-width="4"/>
<circle cx="40" cy="58" r="1.6" fill="#D8A060"/><circle cx="58" cy="57" r="1.6" fill="#D8A060"/><circle cx="76" cy="58" r="1.6" fill="#D8A060"/><circle cx="90" cy="57" r="1.6" fill="#D8A060"/>
<path d="M24 52 Q64 20 104 52 Q64 42 24 52Z" fill="#2A2F4A" {W(3)}/>
<circle cx="64" cy="38" r="5" fill="#E8384A" {W(1.8)}/><circle cx="64" cy="38" r="2" fill="#fff"/>
{eye(52, 76, .55)}{eye(76, 76, .55)}<path d="M58 88 H70" {W(2.6)}/>
<path d="M98 76 Q112 66 104 50" fill="none" {W(3.4)}/><path d="M98 50 L108 46 L106 56Z" fill="#FFF2D6" {W(2)}/>''')

# 17. Чайхона №1 (Бутлерова) — пиала зелёного чая, пар закручивается в тюбетейку
I["cafe-chaihona1-butlerova"] = ("пиала зелёного чая с узором-хлопком", "над ней пар закручивается в узбекскую тюбетейку", ("#E9FFF8", "#2E9E8E"), f'''
<path d="M48 54 Q40 42 50 34 Q58 28 54 18 M74 54 Q82 42 74 32 Q68 24 76 14" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M44 22 Q64 6 86 22 L84 34 Q64 28 46 34Z" fill="#2A2F4A" {W(2.6)}/>
<path d="M54 20 Q56 26 52 30 M64 14 V28 M74 20 Q72 26 76 30" fill="none" stroke="#fff" stroke-width="1.6"/>
<path d="M14 62 H114 Q110 104 64 108 Q18 104 14 62Z" fill="#2A6AD8" {W(3)}/>
<ellipse cx="64" cy="62" rx="50" ry="9" fill="#B8E070" {W(3)}/>
<path d="M28 80 Q34 72 40 80 Q34 88 28 80Z M88 80 Q94 72 100 80 Q94 88 88 80Z" fill="#fff" {W(1.6)}/>
<path d="M18 92 Q64 104 110 92" fill="none" stroke="#fff" stroke-width="2"/>
<path d="M40 108 H88 L84 116 H44Z" fill="#2A6AD8" {W(2.6)}/>
{eye(54, 84, .5)}{eye(74, 84, .5)}{smile(64, 91, 3.5, .7)}{blush(46, 90, .45)}{blush(82, 90, .45)}''')

# 18. Chester (Варшавка, паб с семейным залом) — английский завтрак-рожица
I["cafe-chester-varshavka"] = ("яичница-глазунья с беконом-улыбкой", "английский завтрак на тарелке: желтки-глазки подмигивают, сосиска-нос", ("#FFF9E0", "#C8A030"), f'''
<circle cx="64" cy="66" r="50" fill="#fff" {W(3)}/><circle cx="64" cy="66" r="40" fill="none" stroke="#E0E8F0" stroke-width="3"/>
<path d="M28 48 Q26 30 44 30 Q58 28 58 44 Q60 58 44 58 Q28 62 28 48Z" fill="#FFFDF4" {W(2.6)}/>
<path d="M70 44 Q72 28 88 30 Q104 32 100 48 Q100 62 84 60 Q70 60 70 44Z" fill="#FFFDF4" {W(2.6)}/>
<circle cx="44" cy="45" r="9" fill="#FFB52A" {W(2.4)}/><circle cx="41" cy="42" r="2.4" fill="#fff"/>
<path d="M78 46 Q86 40 94 46" fill="none" stroke="#FFB52A" stroke-width="6" stroke-linecap="round"/><path d="M78 46 Q86 40 94 46" fill="none" {W(2)}/>
<rect x="56" y="54" width="14" height="22" rx="7" fill="#C8603A" {W(2.4)}/>
<path d="M30 84 Q64 112 98 84 L94 78 Q64 102 34 78Z" fill="#E8706A" {W(2.6)}/><path d="M36 84 Q64 102 92 84" fill="none" stroke="#FFD0C0" stroke-width="2"/>
{blush(30, 66, .7)}{blush(98, 66, .7)}''')

# 19. Гранд Фэмили — семья маффинов: папа, мама и малыш
I["cafe-grand-family"] = ("семья маффинов — папа, мама и малыш", "стоят по росту на блюде и обнимаются", ("#FFF0E8", "#D47A5A"), f'''
<ellipse cx="64" cy="112" rx="56" ry="9" fill="#fff" {W(3)}/>
<path d="M14 72 L20 110 H48 L54 72Z" fill="#7AC0F0" {W(2.6)}/><path d="M22 72 L26 110 M34 72 V110 M46 72 L42 110" stroke="#4A90C8" stroke-width="1.8"/>
<path d="M10 74 Q8 40 34 38 Q60 40 58 74Z" fill="#8A4A2A" {W(3)}/>
<circle cx="24" cy="52" r="2" fill="#3A1E10"/><circle cx="44" cy="48" r="2" fill="#3A1E10"/>
{eye(26, 60, .5)}{eye(42, 60, .5)}{smile(34, 67, 3.5, .7)}
<path d="M58 80 L62 110 H86 L90 80Z" fill="#FF9AC0" {W(2.6)}/><path d="M66 80 L69 110 M74 80 V110 M82 80 L79 110" stroke="#E070A0" stroke-width="1.8"/>
<path d="M54 82 Q54 54 74 52 Q94 54 94 82Z" fill="#E8B060" {W(3)}/>
<circle cx="64" cy="64" r="2" fill="#E84A6A"/><circle cx="82" cy="62" r="2" fill="#4A8AE8"/><circle cx="74" cy="58" r="2" fill="#3AB04A"/>
{eye(68, 70, .45)}{eye(82, 70, .45)}{smile(75, 76, 3, .6)}{blush(62, 76, .4)}{blush(88, 76, .4)}
<path d="M96 92 L98 110 H114 L116 92Z" fill="#B8F07A" {W(2.4)}/>
<path d="M92 94 Q92 76 106 76 Q120 76 120 94Z" fill="#FFE0E8" {W(2.6)}/><circle cx="106" cy="72" r="4" fill="#E8304A" {W(2)}/>
{eye(101, 86, .38)}{eye(111, 86, .38)}<path d="M104 91 Q106 93 108 91" fill="none" {W(1.6)}/>
<path d="M54 74 Q58 70 60 74 M90 86 Q94 82 96 86" fill="none" {W(2.6)}/>''')

# 20. ХинКалибрия — хинкали-кит пускает фонтанчик бульона
I["cafe-hinkalibriya"] = ("хинкали с хвостиком-макушкой", "как кит, пускает из макушки фонтанчик бульона, стоя на доске", ("#E2F4FF", "#3A86C8"), f'''
<path d="M64 38 Q50 18 40 22 M64 38 Q78 18 88 22 M64 38 V14" fill="none" stroke="#FFD86A" stroke-width="4" stroke-linecap="round"/>
<circle cx="38" cy="22" r="4" fill="#FFD86A"/><circle cx="90" cy="22" r="4" fill="#FFD86A"/><circle cx="64" cy="12" r="4" fill="#FFD86A"/>
<rect x="12" y="98" width="104" height="14" rx="6" fill="#C88A4A" {W(3)}/>
<path d="M22 98 Q14 66 40 54 Q52 48 58 44 L70 44 Q76 48 88 54 Q114 66 106 98Z" fill="#FFF6E6" {W(3)}/>
<path d="M58 44 L60 34 H68 L70 44" fill="#FFF6E6" {W(2.6)}/>
<path d="M60 46 L34 72 M62 46 L50 76 M66 46 L78 76 M68 46 L94 72" stroke="#E8D6B8" stroke-width="2.2"/>
{eye(50, 80, .55)}{eye(78, 80, .55)}{smile(64, 88, 4, .8)}{blush(40, 88, .55)}{blush(88, 88, .55)}''')

# 21. Atlantica seafood (Кутузовский) — лобстер в салфетке с вилкой и ножом
I["cafe-atlantica-kutuzovsky"] = ("красный лобстер в салфетке", "сидит за столиком и торжественно держит в клешнях вилку и нож", ("#DCE8FF", "#24407E"), f'''
<path d="M0 104 H128 V128 H0Z" fill="#fff" {W(2.4)}/><path d="M0 112 H128" stroke="#7AA8E0" stroke-width="3"/>
<path d="M50 104 Q46 118 40 124 M64 104 V126 M78 104 Q82 118 88 124" fill="none" stroke="#C8302A" stroke-width="5" stroke-linecap="round"/>
<ellipse cx="64" cy="76" rx="26" ry="30" fill="#E8402A" {W(3)}/>
<path d="M40 86 Q64 94 88 86 M42 96 Q64 104 86 96" fill="none" stroke="#B8281E" stroke-width="2.4"/>
<path d="M54 48 Q44 26 30 22 M74 48 Q84 26 98 22" fill="none" {W(2.2)}/>
<path d="M42 70 Q24 64 20 44" fill="none" stroke="#E8402A" stroke-width="6" stroke-linecap="round"/>
<path d="M86 70 Q104 64 108 44" fill="none" stroke="#E8402A" stroke-width="6" stroke-linecap="round"/>
<path d="M12 40 Q14 26 24 30 L22 40 L30 36 Q30 48 18 48Z" fill="#E8402A" {W(2.4)}/>
<path d="M116 40 Q114 26 104 30 L106 40 L98 36 Q98 48 110 48Z" fill="#E8402A" {W(2.4)}/>
<path d="M18 30 V10 M14 10 V18 M18 10 V18 M22 10 V18" stroke="#C8D0E0" stroke-width="2.6" stroke-linecap="round"/>
<path d="M110 30 L110 8 Q118 14 114 30Z" fill="#C8D0E0" {W(1.8)}/>
<path d="M50 72 L64 84 L78 72 L64 66Z" fill="#fff" {W(2.2)}/>
{eye(56, 58, .5)}{eye(72, 58, .5)}{smile(64, 64, 3, .6)}''')

# 23. Моремания (Братиславская) — креветка катается на волне на доске-лимоне
I["cafe-moremania-bratislavskaya"] = ("розовая креветка", "катается на гребне волны на доске из лимонной дольки", ("#E4FFFB", "#14A6A0"), f'''
<path d="M0 92 Q20 70 44 78 Q30 58 54 52 Q86 48 100 72 Q112 92 128 86 V128 H0Z" fill="#2AA8D8" {W(2.6)}/>
<path d="M54 52 Q40 60 44 78 Q52 66 62 64" fill="#fff" {W(2)}/>
<path d="M10 108 Q20 102 30 108 M80 112 Q90 106 100 112" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M40 76 Q70 92 104 74 L102 70 Q70 82 42 70Z" fill="#FFE45A" {W(2.6)}/>
<path d="M50 76 L54 80 M64 79 L66 84 M78 80 L78 84 M92 76 L90 80" stroke="#E8C020" stroke-width="1.6"/>
<path d="M74 20 A26 26 0 1 0 92 64" fill="none" stroke="{O}" stroke-width="25" stroke-linecap="round"/>
<path d="M74 20 A26 26 0 1 0 92 64" fill="none" stroke="#FF8A7A" stroke-width="19" stroke-linecap="round"/>
<path d="M54 26 L60 34 M46 40 L54 44 M46 56 L54 56 M54 70 L60 64 M68 76 L70 68" stroke="#E0604E" stroke-width="2.2"/>
<path d="M92 64 L104 56 L106 72Z" fill="#FF8A7A" {W(2.4)}/>
<path d="M78 16 Q90 0 108 2 M80 20 Q96 10 112 14" fill="none" {W(1.8)}/>
{eye(76, 26, .45)}{eye(84, 30, .45)}
<path d="M58 48 L46 44 M58 56 L48 58" {W(2.4)}/>''')

# 24. Панчетта (Народного Ополчения, мастер-классы пиццы) — пицца выглядывает из коробки
I["cafe-panchetta-opolchenie"] = ("пицца в картонной коробке", "приоткрыла крышку изнутри и выглядывает с улыбкой", ("#FDEDE2", "#B85A3A"), f'''
<path d="M14 82 L64 70 L114 82 L64 96Z" fill="#E8C48A" {W(3)}/>
<path d="M14 82 V100 L64 116 V96Z" fill="#D8A86A" {W(3)}/><path d="M114 82 V100 L64 116 V96Z" fill="#C8965A" {W(3)}/>
<path d="M20 78 Q64 56 108 78 L64 92Z" fill="#E8A44A" {W(2.6)}/>
<path d="M30 78 Q64 62 98 78 L64 88Z" fill="#E8402A"/>
<circle cx="50" cy="76" r="4" fill="#B8281E"/><circle cx="76" cy="74" r="4" fill="#B8281E"/><circle cx="64" cy="82" r="3" fill="#FFF4D8"/>
<path d="M14 82 L4 30 L56 18 L64 70Z" fill="#F2D49A" {W(3)}/>
<path d="M22 40 L48 34 M24 50 L46 45" stroke="#C8965A" stroke-width="2.4" stroke-linecap="round"/>
{eye(56, 74, .45)}{eye(72, 72, .45)}
<path d="M62 70 Q70 60 82 64" fill="none" stroke="#fff" stroke-width="0"/>
<path d="M90 56 Q96 44 92 34 M102 60 Q110 46 104 36" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

# 27. Нияма (Кунцево Плаза) — три шарика данго болтают на палочке
I["cafe-niyama-kuntsevo-plaza"] = ("три шарика данго на палочке — розовый, белый и зелёный", "сидят рядком на палочке, как на скамейке, и болтают", ("#F2FFE8", "#78B848"), f'''
<path d="M10 104 L118 34" stroke="#D8B070" stroke-width="6" stroke-linecap="round"/><path d="M10 104 L118 34" {W(1.6)}/>
<circle cx="38" cy="84" r="18" fill="#FFB0C8" {W(3)}/>
<circle cx="64" cy="66" r="18" fill="#FFFBF0" {W(3)}/>
<circle cx="90" cy="48" r="18" fill="#9AD870" {W(3)}/>
{eye(32, 82, .45)}{eye(43, 80, .45)}{smile(38, 89, 3, .6)}
{eye(58, 64, .45)}{eye(69, 62, .45)}<ellipse cx="64" cy="72" rx="2.6" ry="3" fill="{O}"/>
{eye(84, 46, .45)}{eye(95, 44, .45)}{smile(90, 52, 3, .6)}
{blush(28, 90, .4)}{blush(98, 54, .4)}
<path d="M48 40 Q52 34 58 36 M104 24 Q110 20 114 24" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 28. ЖARkA (Бабушкинская) — кутаб обмахивается веером от жары
I["cafe-zharka-babushkinskaya"] = ("кутаб-полумесяц с зеленью", "обмахивается веером от жары под палящим солнцем", ("#FFEFD0", "#E06A1A"), f'''
<circle cx="24" cy="24" r="14" fill="#FFD23A" {W(2.4)}/>
<path d="M24 2 V6 M2 24 H6 M42 24 H46 M8 8 L11 11 M38 38 L41 41 M38 8 L35 11" stroke="#FFD23A" stroke-width="3" stroke-linecap="round"/>
<ellipse cx="62" cy="110" rx="48" ry="8" fill="#fff" {W(3)}/>
<path d="M16 100 Q20 52 64 50 Q108 52 112 100Z" fill="#F2D49A" {W(3)}/>
<path d="M18 100 Q64 106 110 100" fill="none" stroke="#E0A858" stroke-width="5"/>
<path d="M30 70 Q34 64 40 68 M82 64 Q88 60 92 66 M58 60 Q62 56 66 60" fill="none" stroke="#4AA040" stroke-width="2.6" stroke-linecap="round"/>
<ellipse cx="42" cy="80" rx="5" ry="3" fill="#D8964A"/><ellipse cx="88" cy="82" rx="4" ry="2.6" fill="#D8964A"/>
<path d="M50 80 Q54 76 58 80 M68 80 Q72 76 76 80" fill="none" {W(2.4)}/>
<ellipse cx="63" cy="90" rx="4" ry="3" fill="{O}"/>
<path d="M84 34 L106 18 A26 26 0 0 1 116 46Z" fill="#E8384A" {W(2.4)}/>
<path d="M84 34 L110 24 M84 34 L114 34" stroke="#fff" stroke-width="1.6"/>
<path d="M84 34 L96 58" {W(3)}/>
<path d="M30 46 Q28 40 32 36" fill="none" stroke="#8AD0FF" stroke-width="3" stroke-linecap="round"/>''')

# 29. Листок (Новозаводская) — чайный пакетик-листик ныряет в чашку
I["cafe-listok-fili"] = ("чайный пакетик с ярлычком-листиком", "ныряет в чашку, как с трамплина", ("#FFFBEA", "#8CAA2E"), f'''
<path d="M20 104 Q20 72 20 66 H88 Q88 100 70 110 H38 Q20 108 20 104Z" fill="#fff" {W(3)}/>
<path d="M88 74 Q106 72 104 88 Q102 100 84 98" fill="none" {W(3.4)}/>
<ellipse cx="54" cy="66" rx="34" ry="7" fill="#C8782A" {W(3)}/>
<path d="M30 86 Q36 80 42 86 M60 92 Q66 86 72 92" fill="none" stroke="#E8F2C8" stroke-width="2.4"/>
<ellipse cx="54" cy="116" rx="40" ry="5" fill="#fff" {W(2.4)}/>
<path d="M60 64 Q70 46 86 40" fill="none" {W(1.6)} stroke-dasharray="3 3"/>
<path d="M78 18 L98 14 L104 36 L84 40Z" fill="#F2E6C8" {W(2.8)}/>
{eye(88, 26, .4)}{eye(97, 24, .4)}<ellipse cx="93" cy="32" rx="2.2" ry="2" fill="{O}"/>
<path d="M104 14 Q114 4 122 8 Q118 20 104 14Z" fill="#7AC040" {W(2)}/><path d="M104 14 Q112 10 118 10" fill="none" stroke="#4A8A2A" stroke-width="1.4"/>
<path d="M60 56 Q58 50 62 46 M50 58 Q48 52 52 48" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 30. Некрасов (Химки) — булочка-зайчик в лодке деда Мазая
I["cafe-nekrasov-khimki"] = ("булочка-зайчик с длинными ушками", "плывёт в деревянной лодочке по весеннему разливу, как у деда Мазая", ("#E8F2FF", "#5A7EC0"), f'''
<path d="M0 90 Q16 84 32 90 T64 90 T96 90 T128 90 V128 H0Z" fill="#5AA0E0" {W(2.4)}/>
<path d="M12 106 Q20 100 28 106 M96 110 Q104 104 112 110" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>
<path d="M14 80 H114 Q104 104 64 104 Q24 104 14 80Z" fill="#A8683A" {W(3)}/><path d="M20 88 H108" stroke="#7A4A22" stroke-width="2"/>
<path d="M40 48 Q30 14 42 12 Q52 14 52 46Z M70 46 Q72 10 84 12 Q94 16 80 50Z" fill="#E8B060" {W(2.8)}/>
<path d="M42 44 Q38 22 43 18 M74 44 Q78 22 83 18" fill="none" stroke="#FFD8E0" stroke-width="3" stroke-linecap="round"/>
<ellipse cx="62" cy="64" rx="30" ry="22" fill="#E8B060" {W(3)}/>
<path d="M44 52 Q52 46 60 50" fill="none" stroke="#FFE2A8" stroke-width="3" stroke-linecap="round"/>
<circle cx="50" cy="66" r="2.4" fill="#5A2A1A"/><circle cx="74" cy="66" r="2.4" fill="#5A2A1A"/>
<ellipse cx="62" cy="72" rx="2.6" ry="2" fill="#E8607A"/><path d="M58 76 Q62 79 66 76" fill="none" {W(1.8)}/>
{blush(44, 74, .5)}{blush(80, 74, .5)}''')

# 31. Florentini (Сосенки) — тающее фисташковое джелато в тени сосенки
I["cafe-florentini-sosenki"] = ("фисташковое джелато в вафельном рожке", "тает от жары и прячется в тени маленькой сосенки", ("#EFFFF0", "#2E7A4A"), f'''
<path d="M94 18 L120 70 H68Z" fill="#2E8A4A" {W(2.6)}/><path d="M94 40 L124 92 H64Z" fill="#3AA058" {W(2.6)}/>
<rect x="89" y="92" width="10" height="20" fill="#8A5A2A" {W(2.4)}/>
<path d="M64 92 Q80 104 110 96" fill="none" stroke="#1E5A34" stroke-width="0"/>
<path d="M30 70 L48 120 L66 70Z" fill="#E8B060" {W(3)}/>
<path d="M36 78 L60 102 M44 74 L62 88 M58 74 L40 96 M64 78 L46 110" stroke="#C8904A" stroke-width="1.8"/>
<path d="M24 70 Q20 40 48 36 Q76 40 72 70 Q66 78 60 72 Q56 82 50 74 Q44 84 38 74 Q30 80 24 70Z" fill="#B8E890" {W(3)}/>
<path d="M66 74 Q68 86 64 88 Q60 86 62 76" fill="#B8E890" {W(2)}/>
<circle cx="38" cy="50" r="2" fill="#6A9A3A"/><circle cx="58" cy="46" r="2" fill="#6A9A3A"/>
{eye(40, 58, .45)}{eye(54, 58, .45)}<path d="M43 65 Q47 62 51 65" fill="none" {W(1.8)}/>
<path d="M28 34 Q24 28 28 24" fill="none" stroke="#8AD0FF" stroke-width="3" stroke-linecap="round"/>''')

# 33. River Club Moscow (яхт-клуб) — бублик-спасательный круг на борту яхты
I["cafe-river-club-moscow"] = ("бублик в красно-белой глазури, похожий на спасательный круг", "висит на борту белой яхты у причала и машет", ("#E6F6FF", "#2C6EA8"), f'''
<path d="M0 100 Q16 94 32 100 T64 100 T96 100 T128 100 V128 H0Z" fill="#2A78C0" {W(2.4)}/>
<path d="M70 8 V70" {W(3)}/><path d="M72 12 L108 66 H72Z" fill="#fff" {W(2.8)}/><path d="M68 16 L40 62 H68Z" fill="#FFE8A0" {W(2.6)}/>
<path d="M8 70 H120 L106 100 H20Z" fill="#fff" {W(3)}/><path d="M14 80 H116" stroke="#2C6EA8" stroke-width="3"/>
<circle cx="88" cy="88" r="3" fill="#8AC8F0" {W(1.6)}/><circle cx="102" cy="88" r="3" fill="#8AC8F0" {W(1.6)}/>
<circle cx="40" cy="86" r="22" fill="#E8B060" {W(3)}/>
<path d="M40 64 A22 22 0 0 1 62 86 L52 86 A12 12 0 0 0 40 74Z M40 108 A22 22 0 0 1 18 86 L28 86 A12 12 0 0 0 40 98Z" fill="#E8384A"/>
<path d="M62 86 A22 22 0 0 1 40 108 L40 98 A12 12 0 0 0 52 86Z M18 86 A22 22 0 0 1 40 64 L40 74 A12 12 0 0 0 28 86Z" fill="#fff"/>
<circle cx="40" cy="86" r="22" fill="none" {W(3)}/><circle cx="40" cy="86" r="10" fill="#2A78C0" {W(2.6)}/>
{eye(30, 72, .4)}{eye(50, 72, .4)}<path d="M36 78 Q40 81 44 78" fill="none" {W(1.6)}/>''')

# 36. Satrapezo (Олимпийская деревня, мини-горка) — круглый хлеб деда-пури катится с мини-горки
I["cafe-satrapezo"] = ("круглый грузинский хлеб «деда-пури» с узором", "с хохотом скатывается с маленькой детской горки", ("#FFF6EC", "#C8783A"), f'''
<path d="M10 40 H38 V112" fill="none" {W(4)}/><path d="M10 40 V112" {W(4)}/><path d="M10 56 H38 M10 72 H38 M10 88 H38" {W(3)}/>
<path d="M38 40 Q60 44 78 86 Q86 104 118 108 V118 Q80 116 70 92 Q56 56 38 52Z" fill="#5AC0E8" {W(3)}/>
<circle cx="84" cy="68" r="26" fill="#E8A44A" {W(3)}/>
<circle cx="84" cy="68" r="20" fill="#F5C878"/>
<g fill="#B8682A"><circle cx="84" cy="50" r="1.6"/><circle cx="98" cy="56" r="1.6"/><circle cx="102" cy="70" r="1.6"/><circle cx="96" cy="82" r="1.6"/><circle cx="70" cy="82" r="1.6"/><circle cx="66" cy="70" r="1.6"/><circle cx="70" cy="56" r="1.6"/></g>
<path d="M90 36 Q86 30 90 26 M78 38 Q74 32 78 28" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M76 62 Q79 58 82 62 M88 62 Q91 58 94 62" fill="none" {W(2.2)}/>
<path d="M78 72 Q85 82 92 72Z" fill="#fff" {W(2)}/>
<path d="M104 46 L110 40 M110 56 L118 54 M58 92 L52 96" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

# 37. Catch (Академика Пилюгина) — эскимо-ракета стартует с тарелки
I["cafe-catch-pilyugina"] = ("эскимо в шоколаде, похожее на ракету", "стартует с тарелки, оставляя облачко из сливок, как с космодрома", ("#1E2A6A", "#0A0F2A"), f'''
{sparkle(20, 30, 4)}{sparkle(104, 22, 3.5)}{sparkle(112, 70, 3)}{sparkle(24, 76, 3)}
<ellipse cx="64" cy="114" rx="50" ry="8" fill="#fff" {W(3)}/>
<path d="M38 104 Q30 92 42 88 Q46 78 58 84 Q66 76 74 84 Q86 78 88 90 Q98 92 90 104Z" fill="#FFF8F0" {W(2.6)}/>
<rect x="60" y="76" width="8" height="18" rx="3" fill="#E8C890" {W(2.4)}/>
<path d="M44 76 L36 88 L46 84Z M84 76 L92 88 L82 84Z" fill="#E8384A" {W(2.4)}/>
<path d="M44 78 V40 Q44 14 64 8 Q84 14 84 40 V78Z" fill="#6A3A22" {W(3)}/>
<path d="M44 36 Q64 30 84 36" fill="none" stroke="#FFC8D8" stroke-width="4"/>
<circle cx="64" cy="44" r="7" fill="#8AD0FF" {W(2.4)}/>
{eye(57, 60, .45)}{eye(71, 60, .45)}{smile(64, 66, 3, .6)}
<path d="M50 20 Q54 14 58 14" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>''')

# 38. Гулиани (Мичуринский, туннель) — стакан тархуна выглядывает из детского туннеля
I["cafe-guliani-michurinsky"] = ("стакан изумрудного тархуна с пузырьками", "выглядывает из полосатого детского туннеля-лаза", ("#FFF4FB", "#C04890"), f'''
<ellipse cx="34" cy="74" rx="26" ry="36" fill="#FFD23A" {W(3)}/>
<path d="M34 38 Q100 30 124 40 V108 Q100 116 34 110" fill="#FFD23A" {W(3)}/>
<path d="M60 36 V112 M84 34 V114 M108 36 V112" stroke="#E8384A" stroke-width="7"/>
<ellipse cx="34" cy="74" rx="18" ry="28" fill="#5A2A4A" {W(2.4)}/>
<path d="M18 50 L22 98 Q34 102 46 98 L50 50Z" fill="#7AE07A" {W(3)}/>
<path d="M18 50 H50" {W(3)}/><path d="M20 58 H48" stroke="#B8F8A0" stroke-width="2"/>
<circle cx="26" cy="86" r="2" fill="#fff"/><circle cx="40" cy="90" r="1.6" fill="#fff"/><circle cx="34" cy="94" r="1.4" fill="#fff"/>
<path d="M40 50 L52 22" stroke="#FF8AC0" stroke-width="4" stroke-linecap="round"/>
{eye(28, 70, .45)}{eye(40, 70, .45)}{smile(34, 77, 3, .6)}''')

# ---------- СПОРТ И БАССЕЙНЫ ----------

# 2. «Стремление» (Дубининская) — мальчик повис на кольце после слэм-данка
I["stremlenie-basket-tulskaya"] = ("мальчик-баскетболист в синей форме с номером 23", "повис на кольце после слэм-данка, а мяч отскакивает от пола внизу", ("#E8ECFF", "#4655C8"), f'''
<rect x="26" y="2" width="76" height="32" rx="3" fill="#fff" {W(3)}/><rect x="50" y="12" width="28" height="20" fill="none" stroke="#E8384A" stroke-width="2.6"/>
<path d="M46 40 L52 52 H76 L82 40" fill="none" stroke="#fff" stroke-width="2.2"/><path d="M52 40 L58 52 M64 40 V52 M76 40 L70 52" stroke="#fff" stroke-width="1.8"/>
<path d="M44 40 L40 78 M84 40 L88 78" fill="none" {W(6)}/><path d="M44 40 L40 78 M84 40 L88 78" fill="none" stroke="#C8865A" stroke-width="2.6"/>
<ellipse cx="64" cy="40" rx="22" ry="5" fill="none" stroke="{O}" stroke-width="7"/><ellipse cx="64" cy="40" rx="22" ry="5" fill="none" stroke="#F25A2A" stroke-width="3.6"/>
<circle cx="44" cy="40" r="4" fill="#C8865A" {W(2)}/><circle cx="84" cy="40" r="4" fill="#C8865A" {W(2)}/>
<path d="M40 76 Q64 70 88 76 L86 104 Q64 108 42 104Z" fill="#2A4AD8" {W(3)}/>
<text x="64" y="98" font-family="Arial" font-weight="bold" font-size="13" fill="#fff" text-anchor="middle">23</text>
<circle cx="64" cy="64" r="12" fill="#C8865A" {W(3)}/><path d="M52 60 Q54 50 64 50 Q74 50 76 60 Q70 54 64 56 Q58 54 52 60Z" fill="#2A1A10" {W(2)}/>
{eye(59, 64, .4)}{eye(69, 64, .4)}<path d="M59 70 Q64 74 69 70" fill="#fff" {W(1.8)}/>
<path d="M48 104 L46 124 M80 104 L82 124" fill="none" {W(6)}/><path d="M48 104 L46 124 M80 104 L82 124" fill="none" stroke="#C8865A" stroke-width="2.4"/>
<circle cx="106" cy="104" r="11" fill="#F2892A" {W(2.8)}/><path d="M95 104 H117 M106 93 V115 M99 96 Q104 104 99 112 M113 96 Q108 104 113 112" fill="none" stroke="{O}" stroke-width="1.5"/>
<path d="M100 120 H112" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M18 30 L24 36 M16 44 H24 M110 30 L104 36 M112 44 H104" stroke="#FFE45A" stroke-width="2.6" stroke-linecap="round"/>''')

# 7. «Про.Плыть» (СК «Лазурный») — девочка у бортика работает ножками
I["proplyt-lazurny"] = ("девочка в лазурной шапочке и розовых очках", "держится за бортик бассейна и работает ножками, взбивая фонтан брызг", ("#E0FCFF", "#1EA7C8"), f'''
<path d="M0 28 H128 V46 H0Z" fill="#fff" {W(3)}/><path d="M0 46 H128" stroke="#1E7AA8" stroke-width="4"/>
<path d="M0 50 H128 V128 H0Z" fill="#3CC4E8"/>
<path d="M0 90 H128" stroke="#fff" stroke-width="5" stroke-dasharray="8 6"/><path d="M0 90 H128" stroke="#E8384A" stroke-width="5" stroke-dasharray="8 6" stroke-dashoffset="7"/>
<path d="M48 64 Q70 70 96 64" fill="none" stroke="#FFD0B0" stroke-width="10" stroke-linecap="round"/>
<path d="M88 52 L108 48 M90 72 L112 78" fill="none" {W(6)}/><path d="M88 52 L108 48 M90 72 L112 78" fill="none" stroke="#FFD0B0" stroke-width="2.6"/>
<path d="M104 40 Q112 28 120 36 M100 30 Q104 18 114 22 M112 82 Q124 76 126 86 M106 88 Q114 96 122 94" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<circle cx="112" cy="44" r="3" fill="#fff"/><circle cx="118" cy="86" r="3" fill="#fff"/>
<path d="M24 44 L30 56 M44 44 L40 56" fill="none" {W(6)}/><path d="M24 44 L30 56 M44 44 L40 56" fill="none" stroke="#FFD0B0" stroke-width="2.6"/>
<circle cx="34" cy="64" r="16" fill="#FFD0B0" {W(3)}/>
<path d="M18 62 Q18 44 34 44 Q50 44 50 62 Q34 56 18 62Z" fill="#2AA8E8" {W(2.6)}/>
<circle cx="28" cy="66" r="5" fill="#FF9AC8" {W(2)}/><circle cx="40" cy="66" r="5" fill="#FF9AC8" {W(2)}/><path d="M33 66 H35" {W(2)}/>
<circle cx="28" cy="66" r="2" fill="{O}"/><circle cx="40" cy="66" r="2" fill="{O}"/>
<path d="M30 74 Q34 77 38 74" fill="none" {W(1.8)}/>''')

# 12. «Стремление» (Шипиловская) — мяч-силач подтягивается на кольце
I["stremlenie-basket-shipilovskaya"] = ("баскетбольный мяч-силач с напульсниками", "подтягивается на кольце, как на турнике, пыхтя от усердия", ("#E9FFF4", "#38A878"), f'''
<rect x="22" y="4" width="84" height="22" rx="3" fill="#fff" {W(3)}/><path d="M50 26 V14 H78 V26" fill="none" stroke="#E8384A" stroke-width="2.6"/>
<path d="M30 46 Q36 34 44 34 M98 46 Q92 34 84 34" fill="none" {W(5)}/>
<path d="M30 46 Q36 34 44 34 M98 46 Q92 34 84 34" fill="none" stroke="#F2892A" stroke-width="2"/>
<ellipse cx="64" cy="32" rx="28" ry="5" fill="none" stroke="{O}" stroke-width="7"/><ellipse cx="64" cy="32" rx="28" ry="5" fill="none" stroke="#F25A2A" stroke-width="3.6"/>
<circle cx="42" cy="32" r="5" fill="#F2892A" {W(2.2)}/><circle cx="86" cy="32" r="5" fill="#F2892A" {W(2.2)}/>
<rect x="38" y="38" width="9" height="6" rx="2" fill="#E8384A" {W(1.8)}/><rect x="81" y="38" width="9" height="6" rx="2" fill="#E8384A" {W(1.8)}/>
<circle cx="64" cy="76" r="30" fill="#F2892A" {W(3)}/>
<path d="M34 76 H94 M64 46 V106 M44 54 Q56 76 44 98 M84 54 Q72 76 84 98" fill="none" stroke="{O}" stroke-width="2"/>
<path d="M50 70 L58 72 M78 70 L70 72" {W(2.6)}/>
<rect x="56" y="82" width="16" height="8" rx="3" fill="#fff" {W(2)}/><path d="M60 82 V90 M64 82 V90 M68 82 V90" stroke="{O}" stroke-width="1.2"/>
<path d="M98 66 Q104 62 102 56 M100 80 Q108 80 108 74" fill="none" stroke="#8AD0FF" stroke-width="3" stroke-linecap="round"/>
<path d="M50 110 Q64 118 78 110" fill="none" stroke="#fff" stroke-width="0"/>''')

# 13. «Хаски» (Зелёный пр-т) — сетка-мешок с тремя мячами на крючке в школьном зале
I["husky-basket-novogireevo"] = ("сетка-мешок с тремя баскетбольными мячами", "висит на крючке на стене школьного спортзала, мячи-тройняшки выглядывают из ячеек", ("#F2F2F8", "#7A82A8"), f'''
<path d="M0 98 H128 V128 H0Z" fill="#E8B57A" {W(2.4)}/><path d="M0 98 H128" stroke="#C98E52" stroke-width="3"/>
<path d="M0 30 H128" stroke="#B8BCD8" stroke-width="10"/>
<path d="M58 12 Q64 4 70 12 V22" fill="none" {W(3.4)}/><rect x="56" y="18" width="16" height="6" rx="2" fill="#9AA0C0" {W(2)}/>
<path d="M64 24 L36 50 M64 24 L92 50" {W(2.4)}/>
<circle cx="48" cy="62" r="17" fill="#F2892A" {W(3)}/><circle cx="80" cy="62" r="17" fill="#F28A3A" {W(3)}/><circle cx="64" cy="90" r="18" fill="#F2892A" {W(3)}/>
<path d="M31 62 H65 M48 45 V79 M97 62 H63 M80 45 V79 M46 90 H82 M64 72 V108" stroke="{O}" stroke-width="1.6"/>
{eye(43, 58, .4)}{eye(53, 58, .4)}{eye(75, 58, .4)}{eye(85, 58, .4)}{eye(58, 88, .45)}{eye(70, 88, .45)}
{smile(48, 66, 2.6, .5)}{smile(80, 66, 2.6, .5)}{smile(64, 96, 3, .6)}
<path d="M30 48 Q24 82 42 106 Q64 116 86 106 Q104 82 98 48 Z" fill="none" stroke="#fff" stroke-width="2.4"/>
<path d="M30 60 L98 84 M28 78 L94 100 M98 60 L30 84 M100 78 L34 100 M40 50 L52 112 M88 50 L76 112" stroke="#fff" stroke-width="1.6" opacity=".9"/>''')

# 22. Nevsky Bears (Светлый пр-д) — девочка-либеро принимает мяч в падении
I["nevsky-bears-streshnevo"] = ("девочка-либеро в наколенниках и жёлтой майке", "в падении принимает волейбольный мяч снизу у самого пола", ("#FFF0F6", "#D04A80"), f'''
<path d="M0 104 H128 V128 H0Z" fill="#F2A65A" {W(2.4)}/><path d="M0 112 H128" stroke="#fff" stroke-width="3"/>
<circle cx="92" cy="32" r="16" fill="#fff" {W(3)}/>
<path d="M78 26 Q92 34 106 28 M84 18 Q90 32 84 46 M100 18 Q96 32 102 44" fill="none" stroke="#2A5AD8" stroke-width="2.4"/>
<path d="M98 50 L104 58 M86 52 L84 60" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M50 74 L82 56" fill="none" {W(7)}/><path d="M50 74 L82 56" fill="none" stroke="#FFD8B8" stroke-width="3.4"/>
<path d="M30 82 Q46 66 66 76 L60 96 Q44 98 30 92Z" fill="#FFD23A" {W(3)}/>
<text x="48" y="90" font-family="Arial" font-weight="bold" font-size="11" fill="#2A2F5A" text-anchor="middle">L</text>
<path d="M62 92 L88 98 L104 104" fill="none" {W(7)}/><path d="M62 92 L88 98 L104 104" fill="none" stroke="#FFD8B8" stroke-width="3.4"/>
<path d="M60 96 L66 86 L76 96 L66 100Z" fill="#2A2F5A" {W(2.4)}/>
<rect x="82" y="92" width="12" height="10" rx="4" fill="#2A2F5A" {W(2)}/>
<circle cx="22" cy="76" r="13" fill="#FFD8B8" {W(3)}/><path d="M10 72 Q12 60 24 62 Q34 64 34 72 Q22 66 10 72Z" fill="#6A3A1A" {W(2)}/>
<path d="M10 70 Q2 72 4 82" fill="none" stroke="#6A3A1A" stroke-width="4" stroke-linecap="round"/>
{eye(20, 78, .38)}{eye(29, 77, .38)}<ellipse cx="25" cy="84" rx="2" ry="1.6" fill="{O}"/>''')

# 25. RusVolley (Нагатинская) — мяч взлетел «свечкой» высоко над сеткой
I["rusvolley-nagatinskaya"] = ("волейбольный мяч в сине-жёлто-белую полоску с весёлым ветром в глазах", "взлетел «свечкой» высоко-высоко над волейбольной сеткой, внизу его тень", ("#FFFBE0", "#E8B820"), f'''
<path d="M6 76 V120 M122 76 V120" {W(4)}/>
<rect x="6" y="76" width="116" height="20" fill="none" stroke="#fff" stroke-width="2.6"/>
<path d="M6 76 H122" {W(3.4)}/>
<path d="M14 76 V96 M22 76 V96 M30 76 V96 M38 76 V96 M46 76 V96 M54 76 V96 M62 76 V96 M70 76 V96 M78 76 V96 M86 76 V96 M94 76 V96 M102 76 V96 M110 76 V96 M6 86 H122" stroke="{O}" stroke-width="1"/>
<ellipse cx="64" cy="118" rx="12" ry="3" fill="#8A6A10" opacity=".35"/>
<path d="M64 62 V70" stroke="#fff" stroke-width="2.4" stroke-dasharray="2 3"/>
<circle cx="64" cy="36" r="24" fill="#fff" {W(3)}/>
<path d="M42 30 Q64 44 86 32 Q78 20 64 14 Q50 18 42 30Z" fill="#FFD23A" {W(2)}/>
<path d="M44 46 Q64 54 84 44 Q86 54 74 58 Q60 60 50 56Z" fill="#2A5AD8" {W(2)}/>
<path d="M56 36 Q58 32 60 36 M68 36 Q70 32 72 36" fill="none" {W(2.2)}/><path d="M60 42 Q64 46 68 42" fill="#fff" {W(1.8)}/>
<path d="M32 22 L36 26 M96 22 L92 26 M30 40 H35 M98 40 H93" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

# 26. «Мама, я плыву» (Динамо, грудничковое) — малыш ныряет к маминым ладоням
I["mama-ya-plyvu-dinamo"] = ("грудничок в полосатых плавках-подгузнике", "ныряет под водой с открытыми глазками к маминым ладоням", ("#D8F6FF", "#1A7EB0"), f'''
<path d="M0 0 H128 V20 Q96 26 64 20 Q32 14 0 20Z" fill="#9AE0FF" opacity=".6"/>
<path d="M104 30 Q120 40 118 56 Q112 62 104 56 L98 40Z M104 96 Q120 88 118 72 Q112 66 104 72 L98 88Z" fill="#FFD0B0" {W(2.6)}/>
<path d="M124 46 L108 48 M124 82 L108 80" {W(4)}/>
<path d="M30 52 Q24 40 14 42 M30 76 Q22 86 12 84" fill="none" {W(6)}/><path d="M30 52 Q24 40 14 42 M30 76 Q22 86 12 84" fill="none" stroke="#FFD8C0" stroke-width="2.6"/>
<ellipse cx="44" cy="64" rx="22" ry="17" fill="#FFD8C0" {W(3)}/>
<path d="M22 56 Q30 46 40 52 Q34 62 24 70 Q18 64 22 56Z" fill="#7ADCFF" {W(2.4)}/><path d="M24 58 L30 54 M22 64 L34 60 M26 68 L36 62" stroke="#fff" stroke-width="1.8"/>
<path d="M66 60 Q86 52 96 50 M66 70 Q86 76 96 80" fill="none" {W(6)}/><path d="M66 60 Q86 52 96 50 M66 70 Q86 76 96 80" fill="none" stroke="#FFD8C0" stroke-width="2.6"/>
<circle cx="78" cy="64" r="15" fill="#FFD8C0" {W(3)}/><path d="M74 49 Q80 44 84 50" fill="none" {W(2)}/>
{eye(76, 60, .45)}{eye(86, 62, .45)}<ellipse cx="82" cy="70" rx="2.6" ry="2.2" fill="{O}"/>{blush(72, 68, .45)}
<circle cx="88" cy="36" r="4" fill="none" stroke="#fff" stroke-width="2"/><circle cx="96" cy="24" r="3" fill="none" stroke="#fff" stroke-width="2"/><circle cx="82" cy="22" r="2.4" fill="none" stroke="#fff" stroke-width="2"/>
<path d="M10 104 Q20 96 30 104 M40 112 Q50 104 60 112" fill="none" stroke="#8AE0F8" stroke-width="3" stroke-linecap="round"/>''')

# 32. «МБА-Динамика» (Крылатское) — девочка бросает мяч в прыжке, вид со спины
I["mba-dinamika-krylatskoe"] = ("девочка с косичкой в фиолетовой форме, вид со спины", "бросает мяч в прыжке, мяч летит прямо в кольцо на фоне холмов Крылатского", ("#FFF6E8", "#E09040"), f'''
<path d="M0 92 Q30 74 60 88 Q94 70 128 86 V128 H0Z" fill="#8AC860" {W(2.4)}/>
<rect x="74" y="6" width="44" height="30" rx="3" fill="#fff" {W(3)}/><rect x="88" y="16" width="16" height="14" fill="none" stroke="#E8384A" stroke-width="2.4"/>
<path d="M86 40 L90 54 H102 L106 40" fill="none" stroke="#fff" stroke-width="2"/>
<ellipse cx="96" cy="40" rx="11" ry="3" fill="none" stroke="#F25A2A" stroke-width="3.4"/>
<circle cx="74" cy="22" r="9" fill="#F2892A" {W(2.4)}/><path d="M65 22 H83 M74 13 V31" stroke="{O}" stroke-width="1.4"/>
<path d="M50 30 Q60 22 70 28" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="3 3"/>
<path d="M40 60 L46 32 M60 60 L58 34" fill="none" {W(5.4)}/><path d="M40 60 L46 32 M60 60 L58 34" fill="none" stroke="#E8B890" stroke-width="2.4"/>
<path d="M36 60 Q50 54 64 60 L62 90 Q50 94 38 90Z" fill="#8A4AE0" {W(3)}/>
<text x="50" y="84" font-family="Arial" font-weight="bold" font-size="14" fill="#fff" text-anchor="middle">8</text>
<circle cx="50" cy="50" r="11" fill="#5A3020" {W(3)}/>
<path d="M50 61 Q44 72 50 78 Q56 72 50 61" fill="#5A3020" {W(2)}/>
<path d="M40 90 L34 112 M60 90 L66 110" fill="none" {W(6)}/><path d="M40 90 L34 112 M60 90 L66 110" fill="none" stroke="#E8B890" stroke-width="2.4"/>
<path d="M28 112 H40 M62 110 H74" {W(5)}/>
<path d="M30 118 Q50 124 70 118" fill="none" stroke="#fff" stroke-width="0"/>''')

# 34. «Шторм» (Красный Октябрь, водное поло) — мяч поло выпрыгивает из волн в ворота
I["shtorm-krasny-oktyabr"] = ("жёлто-синий мяч водного поло", "выпрыгивает из штормовой волны прямо в сетку плавающих ворот", ("#C8D8E8", "#34506E"), f'''
<path d="M70 20 H122 V70 H70Z" fill="none" stroke="#fff" stroke-width="2"/>
<path d="M78 20 V70 M86 20 V70 M94 20 V70 M102 20 V70 M110 20 V70 M70 30 H122 M70 40 H122 M70 50 H122 M70 60 H122" stroke="#fff" stroke-width="1.2" opacity=".8"/>
<path d="M66 70 V18 H124" fill="none" stroke="#E8384A" stroke-width="5" stroke-linecap="round"/><path d="M66 70 V18 H124" fill="none" {W(1.4)}/>
<path d="M0 78 Q14 60 30 70 Q40 52 56 66 Q72 54 84 70 Q100 60 112 72 Q120 66 128 70 V128 H0Z" fill="#2A7AB8" {W(2.6)}/>
<path d="M30 70 Q34 62 40 64 M56 66 Q62 58 68 62" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M10 96 Q22 88 34 96 M70 104 Q82 96 94 104" fill="none" stroke="#8AC8F0" stroke-width="2.6" stroke-linecap="round"/>
<circle cx="42" cy="46" r="20" fill="#FFD23A" {W(3)}/>
<path d="M24 38 Q42 50 60 38 M30 62 Q38 44 34 28 M54 62 Q46 44 50 28" fill="none" stroke="#2A5AD8" stroke-width="4"/>
<path d="M24 38 Q42 50 60 38 M30 62 Q38 44 34 28 M54 62 Q46 44 50 28" fill="none" {W(1.2)}/>
{eye(37, 44, .42)}{eye(48, 44, .42)}<path d="M38 52 Q43 56 47 52" fill="#fff" {W(1.6)}/>
<circle cx="18" cy="60" r="3" fill="#fff"/><circle cx="64" cy="76" r="2.4" fill="#fff"/>''')

# 35. «Территория мяча» (Дубровка) — мяч водружает флажок в центральный круг площадки
I["terball-dubrovka"] = ("баскетбольный мяч-покоритель", "водружает флажок с мячиком в центр площадки — «моя территория!»", ("#FFF4F0", "#C85A6A"), f'''
<path d="M0 86 H128 V128 H0Z" fill="#E8A86A" {W(2.4)}/>
<ellipse cx="64" cy="104" rx="44" ry="12" fill="none" stroke="#fff" stroke-width="3"/><path d="M0 104 H20 M108 104 H128" stroke="#fff" stroke-width="3"/>
<path d="M90 104 V22" {W(3.4)}/><path d="M92 24 L122 34 L92 46Z" fill="#2A8AE8" {W(2.6)}/>
<circle cx="104" cy="35" r="5" fill="#F2892A" {W(1.6)}/>
<circle cx="56" cy="70" r="28" fill="#F2892A" {W(3)}/>
<path d="M28 70 H84 M56 42 V98 M38 50 Q50 70 38 90 M74 50 Q62 70 74 90" fill="none" stroke="{O}" stroke-width="2"/>
<path d="M78 66 Q86 58 90 52" fill="none" {W(5)}/><path d="M78 66 Q86 58 90 52" fill="none" stroke="#F2892A" stroke-width="2"/>
<path d="M44 64 Q48 60 52 64 M60 64 Q64 60 68 64" fill="none" {W(2.4)}/>
<path d="M48 76 Q56 84 64 76Z" fill="#fff" {W(2)}/>
{sparkle(24, 32, 5)}{sparkle(52, 24, 3.5)}''')

# 39. EXTREME KIDS (Раменское) — девочка на роликах тормозит пяткой
I["extremekids-roller-ramenskoe"] = ("девочка на роликах в зелёном шлеме и наколенниках", "тормозит пяточным стопором, за роликом тянется полоска пыли", ("#FFFDE8", "#C0B020"), f'''
<path d="M0 104 H128 V128 H0Z" fill="#B8BCC8" {W(2.4)}/>
<path d="M4 98 Q20 92 36 100 M10 90 Q22 84 34 90" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M60 70 L70 90 L56 100 M66 70 L84 86 L98 94" fill="none" {W(6)}/><path d="M60 70 L70 90 L56 100 M66 70 L84 86 L98 94" fill="none" stroke="#FFD8B8" stroke-width="2.6"/>
<circle cx="70" cy="88" r="5" fill="#2A2F5A" {W(1.8)}/><circle cx="84" cy="86" r="5" fill="#2A2F5A" {W(1.8)}/>
<path d="M40 96 L56 90 L60 100 L42 106Z" fill="#FF6A9A" {W(2.4)}/><circle cx="44" cy="108" r="3.4" fill="#FFE45A" {W(1.6)}/><circle cx="54" cy="106" r="3.4" fill="#FFE45A" {W(1.6)}/>
<path d="M38 102 L32 106" stroke="#E8384A" stroke-width="5" stroke-linecap="round"/>
<path d="M94 90 L112 88 L112 98 L94 100Z" fill="#FF6A9A" {W(2.4)}/><circle cx="98" cy="104" r="3.4" fill="#FFE45A" {W(1.6)}/><circle cx="108" cy="104" r="3.4" fill="#FFE45A" {W(1.6)}/>
<path d="M50 44 Q64 38 76 44 L72 72 Q62 76 54 72Z" fill="#FF8A3A" {W(3)}/>
<path d="M52 50 L34 58 M74 50 L92 40" fill="none" {W(5.4)}/><path d="M52 50 L34 58 M74 50 L92 40" fill="none" stroke="#FFD8B8" stroke-width="2.4"/>
<circle cx="62" cy="28" r="13" fill="#FFD8B8" {W(3)}/>
<path d="M47 28 Q46 10 62 10 Q78 10 77 28 Q62 20 47 28Z" fill="#4AC060" {W(2.6)}/>
{eye(57, 31, .4)}{eye(67, 31, .4)}<path d="M58 37 Q62 40 66 37" fill="none" {W(1.8)}/>''')


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
