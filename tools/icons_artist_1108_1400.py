"""Робот «художник», 08.11 ~14:00 UTC. check_unique.py повторов не нашёл, но среди волейбольных секций осталась
серия от генератора: 18 иконок «волейбольный мяч-персонаж + аксессуар» (кепка, наушники, корона, кубок, вымпел…),
и 5 старых иконок RusVolley с чужим видом спорта (баскетбольное кольцо, баскетбольный мяч — тот же сюжет, что
у stremlenie-basket-mytishchi, бейсбольная перчатка, бита, теннисный стол). 23 иконки придуманы заново и нарисованы
вручную по одной: свой герой, своя сцена, ракурс и палитра фона. Один простой мяч (ms-volley-leningradka) оставлен.
Запуск из корня: python3 tools/icons_artist_1108_1400.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT
from icons_artist_1108_0800 import limb, SK

I = {}
_n = [0]


def vb(cx, cy, r, c1="#FFD23A", c2="#2F6FDB", sw=2.6):
    """волейбольный мяч: жёлтая и синяя панели, белая — между ними (реквизит, не герой)"""
    _n[0] += 1
    i = f"vb{_n[0]}"
    return (f'<clipPath id="{i}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff"/>'
            f'<g clip-path="url(#{i})">'
            f'<path d="M{cx-r*1.1:.1f} {cy+r*.2:.1f} Q{cx-r*.05:.1f} {cy-r*.3:.1f} {cx+r*.5:.1f} {cy-r*1.1:.1f} L{cx-r*1.1:.1f} {cy-r*1.1:.1f}Z" fill="{c1}"/>'
            f'<path d="M{cx+r*1.1:.1f} {cy-r*.45:.1f} Q{cx+r*.05:.1f} {cy+r*.05:.1f} {cx-r*.2:.1f} {cy+r*1.1:.1f} L{cx+r*1.1:.1f} {cy+r*1.1:.1f}Z" fill="{c2}"/>'
            f'<path d="M{cx-r*1.1:.1f} {cy+r*.2:.1f} Q{cx-r*.05:.1f} {cy-r*.3:.1f} {cx+r*.5:.1f} {cy-r*1.1:.1f} '
            f'M{cx+r*1.1:.1f} {cy-r*.45:.1f} Q{cx+r*.05:.1f} {cy+r*.05:.1f} {cx-r*.2:.1f} {cy+r*1.1:.1f} '
            f'M{cx-r*.7:.1f} {cy+r*.8:.1f} Q{cx-r*.15:.1f} {cy+r*.1:.1f} {cx+r*.85:.1f} {cy-r*.55:.1f}" fill="none" {W(sw*.8)}/>'
            f'</g><circle cx="{cx}" cy="{cy}" r="{r}" fill="none" {W(sw)}/>')


def head(x, y, r, hair, k=.5, mouth=True):
    """круглая голова с причёской-шапочкой сверху"""
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{SK}" {W(2.8)}/>'
            f'<path d="M{x-r-.5} {y} Q{x-r} {y-r-3} {x} {y-r-1} Q{x+r} {y-r-3} {x+r+.5} {y} Q{x} {y-r*.45} {x-r-.5} {y}Z" fill="{hair}" {W(2.4)}/>'
            f'{eye(x-r*.36, y+r*.2, k)}{eye(x+r*.36, y+r*.2, k)}'
            + (f'<path d="M{x-r*.25} {y+r*.55} Q{x} {y+r*.8} {x+r*.25} {y+r*.55}" fill="none" {W(2)}/>' if mouth else '')
            + f'{blush(x-r*.62, y+r*.55, r/36)}{blush(x+r*.62, y+r*.55, r/36)}')


def net(x1, x2, y, h, band="#fff", cell=7):
    """кусок волейбольной сетки: белая лента сверху и клетка"""
    g = "".join(f'M{x} {y} V{y+h} ' for x in range(int(x1) + cell, int(x2), cell))
    g += "".join(f'M{x1} {yy} H{x2} ' for yy in range(int(y) + cell, int(y + h), cell))
    return (f'<path d="{g}" stroke="{O}" stroke-width="1.3" opacity=".75"/>'
            f'<rect x="{x1}" y="{y-3}" width="{x2-x1}" height="6" rx="2" fill="{band}" {W(2.2)}/>')


# 1. Марксистская — первый день в секции: малыш обнимает мяч больше себя
I["rusvolley-marksistskaya"] = ("малыш-новичок в огромных белых наколенниках до самых шорт", "в первый день в секции крепко обнимает волейбольный мяч больше себя и сияет", ("#DDF7EC", "#4FBF97"), f'''
<path d="M0 112 H128 V128 H0Z" fill="#E7B877" {W(2.4)}/>
{limb("M54 96 L52 114", SK, 9)}{limb("M74 96 L76 114", SK, 9)}
<rect x="44" y="96" width="17" height="15" rx="6" fill="#fff" {W(2.6)}/><rect x="67" y="96" width="17" height="15" rx="6" fill="#fff" {W(2.6)}/>
<path d="M44 114 H60 L60 118 H42Z M68 114 H84 L86 118 H68Z" fill="#2F6FDB" {W(2.2)}/>
<path d="M46 60 Q64 52 82 60 L84 96 H44Z" fill="#FF7A59" {W(2.8)}/>
{vb(64, 76, 25)}
{limb("M46 64 Q32 78 46 92 L58 92", SK, 8)}{limb("M82 64 Q96 78 82 92 L70 92", SK, 8)}
{head(64, 38, 17, "#8A5A34", .62)}
{sparkle(22, 30, 6)}{sparkle(106, 40, 4.5)}''')

# 2. Новодмитровская — девочка-линейный судья поднимает флажок «аут»
I["rusvolley-novodmitrovskaya"] = ("девочка — линейный судья с красно-жёлтым флажком", "стоит на углу площадки и поднимает флажок «аут»: мяч упал за белую линию", ("#FFEBDD", "#EC7F62"), f'''
<path d="M0 92 H128 V128 H0Z" fill="#F4A65A" {W(2.4)}/>
<path d="M0 104 H84 L84 128" fill="none" stroke="#fff" stroke-width="5"/>
{limb("M38 92 L36 112", SK, 7)}{limb("M50 92 L52 112", SK, 7)}
<path d="M30 112 h10 v4 h-12Z M48 112 h10 l2 4 h-12Z" fill="#fff" {W(2)}/>
<path d="M32 58 Q44 52 56 58 L58 94 H30Z" fill="#fff" {W(2.8)}/>
<path d="M32 66 H56 M31 76 H57 M30 86 H58" stroke="{O}" stroke-width="2.2"/>
{limb("M34 62 L22 84", SK, 7)}
{limb("M54 60 L66 36", SK, 7)}
<path d="M66 40 L76 8" {W(3)}/>
<path d="M74 10 L104 16 L96 36 L70 30Z" fill="#FFD23A" {W(2.6)}/><path d="M74 10 L104 16 L70 30Z" fill="#E8403A" {W(2.4)}/>
{head(44, 40, 14, "#3A2A20", .5)}
<path d="M32 30 Q24 36 28 46 M56 30 Q64 36 60 46" fill="none" stroke="#3A2A20" stroke-width="4" stroke-linecap="round"/>
{vb(94, 106, 10)}
<path d="M84 90 Q88 86 92 90 M100 88 Q104 84 108 88" fill="none" {W(2)}/>''')

# 3. Гарибальди — антенна сетки следит, чтобы мяч не залетел за неё
I["rusvolley-garibaldi"] = ("красно-белая антенна волейбольной сетки с глазками", "торчит над краем сетки, строго выставила ладошку — мяч не должен пролететь за неё", ("#C8F0F2", "#23808F"), f'''
{net(-4, 92, 66, 30)}
<rect x="90" y="14" width="12" height="96" rx="6" fill="#fff" {W(3)}/>
<path d="M90 26 H102 V40 H90Z M90 54 H102 V68 H90Z M90 82 H102 V96 H90Z" fill="#E8403A"/>
<rect x="90" y="14" width="12" height="96" rx="6" fill="none" {W(3)}/>
<circle cx="96" cy="44" r="13" fill="#fff" {W(2.6)}/>{eye(91, 43, .5)}{eye(101, 43, .5)}
<path d="M92 50 H100" {W(2.2)}/>
{limb("M84 46 L70 40", "#fff", 6)}<circle cx="68" cy="39" r="4" fill="#fff" {W(2.4)}/>
{vb(36, 34, 16)}
<path d="M10 22 L-2 18 M8 36 L-4 36 M12 48 L0 52" {W(2.4)}/>''')

# 4. Орджоникидзе — трое ребят обнялись командным кружком перед игрой
I["rusvolley-ordzhonikidze"] = ("трое ребят в зелёной форме, обнявшихся за плечи", "встали командным кружком перед игрой, у ног — волейбольный мяч", ("#F4FAD0", "#97C43A"), f'''
<path d="M14 70 Q36 62 50 70 L54 128 H10Z" fill="#2FAF6A" {W(2.8)}/>
<path d="M78 70 Q92 62 114 70 L118 128 H74Z" fill="#2FAF6A" {W(2.8)}/>
<path d="M44 64 Q64 56 84 64 L88 128 H40Z" fill="#45C882" {W(2.8)}/>
<path d="M58 66 H70" stroke="#fff" stroke-width="3"/>
{head(32, 52, 14, "#E0A030", .45)}{head(96, 52, 14, "#2A2A3A", .45)}
{head(64, 44, 15, "#B2552A", .5)}
{limb("M22 72 Q44 64 64 70 Q84 64 106 72", "#2FAF6A", 8)}
{vb(64, 104, 17)}''')

# 5. Строгино, пляжный — ананас отбивает мяч хохолком на песке
I["rusvolley-strogino-beach"] = ("ананас-пляжник в тёмных очках", "на горячем песке у пляжной сетки отбивает волейбольный мяч своим зелёным хохолком", ("#FFF6C0", "#FFA234"), f'''
<path d="M0 100 Q64 92 128 100 V128 H0Z" fill="#F6D38A" {W(2.4)}/>
<path d="M104 54 V104 M124 54 V104" {W(2.6)}/>{net(104, 128, 58, 22)}
<path d="M48 44 L42 22 L54 36 L56 14 L64 34 L72 14 L74 36 L86 22 L80 44Z" fill="#4FBF5A" {W(2.6)}/>
<ellipse cx="64" cy="76" rx="24" ry="30" fill="#FFC93A" {W(3)}/>
<path d="M46 60 L74 100 M58 50 L84 86 M44 78 L64 104 M82 60 L54 100 M70 48 L44 84 M86 76 L70 102" stroke="#D99A1A" stroke-width="2"/>
<rect x="46" y="64" width="15" height="9" rx="4" fill="{O}"/><rect x="67" y="64" width="15" height="9" rx="4" fill="{O}"/><path d="M61 67 H67" {W(2.2)}/>
<path d="M58 84 Q64 89 70 84" fill="none" {W(2.4)}/>{blush(48, 80, .6)}{blush(80, 80, .6)}
{limb("M42 80 L28 70", "#FFC93A", 7)}{limb("M86 80 L98 92", "#FFC93A", 7)}
{vb(64, 15, 11)}<path d="M54 30 Q64 33 74 30" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 6. Nevsky Bears, Медведково — папа с сыном перекидывают мяч через верёвку во дворе
I["nevsky-bears-medvedkovo"] = ("папа с сыном в одинаковых синих майках", "во дворе перекидывают волейбольный мяч через натянутую бельевую верёвку", ("#E3E8FF", "#7380E0"), f'''
<path d="M0 112 H128 V128 H0Z" fill="#8ACB6A" {W(2.4)}/>
<path d="M8 50 V114 M120 50 V114" {W(3.4)}/>
<path d="M8 52 Q64 64 120 52" fill="none" {W(2.4)}/>
<path d="M30 58 l4 8 l4 -8Z M90 58 l4 8 l4 -8Z" fill="#FFD23A" {W(1.6)}/>
<path d="M16 86 Q34 78 50 86 L52 128 H14Z" fill="#2F6FDB" {W(2.8)}/>
{limb("M46 88 L62 70", SK, 8)}
{head(33, 66, 15, "#5A3A26", .5)}
<path d="M27 76 Q33 79 39 76" fill="none" stroke="#5A3A26" stroke-width="3"/>
<path d="M84 98 Q96 92 108 98 L110 128 H82Z" fill="#2F6FDB" {W(2.8)}/>
{limb("M86 100 L76 84", SK, 6)}
{head(96, 82, 11, "#5A3A26", .42)}
{vb(64, 26, 12)}
<path d="M50 38 Q52 30 56 28 M74 28 Q80 32 82 40" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 4" stroke-linecap="round"/>''')

# 7. Nevsky Bears, Римская — малыш в шлеме римского легионера бьёт через сетку
I["nevsky-bears-rimskaya"] = ("малыш в золотом шлеме римского легионера с красным гребнем", "в прыжке над волейбольной сеткой бьёт по мячу ладонью", ("#FFE2C8", "#C8603A"), f'''
{net(0, 128, 96, 34)}
{limb("M60 82 L50 100", SK, 7)}{limb("M70 82 L84 96", SK, 7)}
<path d="M54 56 Q66 50 78 56 L78 84 H54Z" fill="#E8403A" {W(2.8)}/>
{limb("M74 58 L94 34", SK, 7)}{limb("M56 60 L44 72", SK, 7)}
{head(64, 40, 14, "#E8B030", .48)}
<path d="M48 36 Q48 22 64 22 Q80 22 80 36 Z" fill="#F2C23A" {W(2.6)}/>
<path d="M48 36 H80" {W(2.6)}/>
<path d="M52 22 Q64 2 76 22 Q64 16 52 22Z" fill="#E8403A" {W(2.4)}/>
<path d="M54 18 L56 12 M60 14 L61 8 M68 14 L67 8 M74 18 L72 12" stroke="#fff" stroke-width="1.6"/>
{vb(100, 24, 12)}
{sparkle(108, 46, 5)}''')

# 8. Nevsky Bears, Лихоборы — мальчик тренирует приём у кирпичной стены
I["nevsky-bears-likhobory"] = ("мальчик в бирюзовой повязке на лбу", "один тренирует приём снизу у кирпичной стены двора: мяч отскакивает от стены к нему", ("#EAF3FF", "#7FA8E8"), f'''
<path d="M0 0 H38 V128 H0Z" fill="#D9774E" {W(2.6)}/>
<path d="M0 14 H38 M0 30 H38 M0 46 H38 M0 62 H38 M0 78 H38 M0 94 H38 M0 110 H38 M18 0 V14 M8 14 V30 M28 14 V30 M18 30 V46 M8 46 V62 M28 46 V62 M18 62 V78 M8 78 V94 M28 78 V94 M18 94 V110" stroke="#FFD8C0" stroke-width="2"/>
<path d="M38 112 H128 V128 H38Z" fill="#9AA3B8" {W(2.4)}/>
{vb(52, 52, 12)}
<path d="M42 40 Q46 30 40 22 M66 60 Q74 66 80 64" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 4" stroke-linecap="round"/>
{limb("M88 96 L80 114", SK, 7)}{limb("M100 96 L104 114", SK, 7)}
<path d="M80 66 Q92 60 106 66 L106 98 H80Z" fill="#2FC4B8" {W(2.8)}/>
{limb("M84 72 L70 82", SK, 7)}{limb("M100 72 L72 86", SK, 7)}
{head(94, 48, 14, "#2A2A3A", .5)}
<path d="M80 42 Q94 36 108 42" fill="none" stroke="#2FC4B8" stroke-width="5" stroke-linecap="round"/>''')

# 9. Nevsky Bears, Реутов — бабушка-болельщица с плакатом
I["nevsky-bears-reutov"] = ("бабушка-болельщица в вязаной шапке с помпоном и в очках", "на трибуне подняла над головой плакат с нарисованным волейбольным мячом и сердечком", ("#F6E2FF", "#A866DE"), f'''
<path d="M0 112 H128 M0 122 H128" stroke="#fff" stroke-width="3" opacity=".6"/>
<path d="M34 98 Q64 84 94 98 L100 128 H28Z" fill="#7A4AC0" {W(2.8)}/>
<path d="M44 92 L64 116 L84 92" fill="none" stroke="#FFC0D8" stroke-width="4"/>
{limb("M40 96 L30 52", "#7A4AC0", 8)}{limb("M88 96 L98 52", "#7A4AC0", 8)}
<rect x="18" y="14" width="92" height="40" rx="5" fill="#fff" {W(3)}/>
{vb(46, 34, 12)}
<path d="M84 44 Q68 32 72 26 Q76 20 84 28 Q92 20 96 26 Q100 32 84 44Z" fill="#FF5A7A" {W(2.4)}/>
<circle cx="64" cy="80" r="16" fill="{SK}" {W(2.8)}/>
<path d="M47 76 Q48 58 64 58 Q80 58 81 76 Q64 70 47 76Z" fill="#E8403A" {W(2.4)}/>
<path d="M52 66 V74 M58 63 V72 M64 62 V71 M70 63 V72 M76 66 V74" stroke="#fff" stroke-width="1.8"/>
<circle cx="64" cy="55" r="5" fill="#fff" {W(2.2)}/>
<circle cx="57" cy="81" r="5" fill="#fff" fill-opacity=".4" {W(2)}/><circle cx="71" cy="81" r="5" fill="#fff" fill-opacity=".4" {W(2)}/><path d="M62 81 H66" {W(2)}/>
{eye(57, 81, .4)}{eye(71, 81, .4)}<path d="M59 89 Q64 93 69 89" fill="none" {W(2)}/>{blush(50, 88, .45)}{blush(78, 88, .45)}''')

# 10. Nevsky Bears, Сходненская — усатый тренер показывает подачу
I["nevsky-bears-skhodnenskaya"] = ("усатый тренер в красном спортивном костюме со свистком на шнурке", "подбросил волейбольный мяч над головой и показывает детям, как правильно подавать", ("#FBF2D8", "#B89A50"), f'''
<path d="M34 72 Q64 62 94 72 L98 128 H30Z" fill="#D8352E" {W(2.8)}/>
<path d="M42 74 L46 128 M86 74 L82 128" stroke="#fff" stroke-width="3"/>
<path d="M54 68 Q64 92 74 68" fill="none" {W(2)}/><rect x="60" y="90" width="9" height="6" rx="2" fill="#C8CCD8" {W(2)}/>
{limb("M38 78 L28 48", "#D8352E", 9)}<circle cx="27" cy="44" r="5" fill="{SK}" {W(2.4)}/>
{limb("M90 78 L104 98", "#D8352E", 9)}
<circle cx="64" cy="50" r="17" fill="{SK}" {W(2.8)}/>
<path d="M47 46 Q46 32 64 32 Q82 32 81 46 Q76 38 64 40 Q52 38 47 46Z" fill="#6A6A72" {W(2.4)}/>
{eye(57, 48, .5)}{eye(71, 48, .5)}
<path d="M52 58 Q58 54 64 58 Q70 54 76 58 Q70 62 64 59 Q58 62 52 58Z" fill="#5A3A26" {W(2)}/>
{blush(50, 56, .45)}{blush(78, 56, .45)}
{vb(38, 24, 11)}
<path d="M30 38 V34 M36 38 V36" {W(2)}/>''')

# 11. Nevsky Bears, Коньково — снежный волейбол: мальчик в ушанке бьёт варежкой
I["nevsky-bears-konkovo"] = ("мальчик в ушанке и красных варежках", "играет в снежный волейбол: на заснеженной площадке подаёт мяч снизу кулаком в варежке", ("#F4FBFF", "#9CC4EA"), f'''
<path d="M0 100 Q64 90 128 100 V128 H0Z" fill="#fff" {W(2.4)}/>
<circle cx="20" cy="22" r="2.4" fill="#fff"/><circle cx="100" cy="16" r="2.4" fill="#fff"/><circle cx="114" cy="80" r="2" fill="#fff"/><circle cx="12" cy="64" r="2" fill="#fff"/>
{limb("M44 94 L38 112", "#3A4A7A", 8)}{limb("M56 94 L62 112", "#3A4A7A", 8)}
<path d="M32 112 h12 v4 h-14Z M58 112 h12 l2 4 h-14Z" fill="#6A4A30" {W(2)}/>
<path d="M32 62 Q48 54 64 62 L64 96 H32Z" fill="#2F6FDB" {W(2.8)}/>
<path d="M48 62 V96" stroke="#fff" stroke-width="2"/>
{limb("M60 70 L80 80", "#2F6FDB", 8)}<circle cx="83" cy="81" r="6" fill="#E8403A" {W(2.4)}/>
{limb("M36 68 L28 84", "#2F6FDB", 8)}<circle cx="27" cy="88" r="5.5" fill="#E8403A" {W(2.4)}/>
{head(48, 44, 14, "#2A2A3A", .48)}
<path d="M32 42 Q30 22 48 22 Q66 22 64 42 Q56 34 48 34 Q40 34 32 42Z" fill="#9A6A44" {W(2.6)}/>
<path d="M32 40 Q26 50 30 60 L36 56 Q34 48 36 42Z M64 40 Q70 50 66 60 L60 56 Q62 48 60 42Z" fill="#9A6A44" {W(2.4)}/>
{vb(98, 66, 14)}
<path d="M84 52 l-4 -4 M88 46 l-1 -6 M110 50 l4 -4" {W(2.2)}/>''')

# 12. RusVolley, Коптево — девочка в очках делает передачу сверху
I["rusvolley-koptevo"] = ("девочка в круглых очках с косичками-баранками", "делает передачу сверху: мяч зависает над растопыренными пальцами", ("#FFE0EC", "#E8609A"), f'''
<path d="M30 92 Q64 80 98 92 L104 128 H24Z" fill="#7A3AD0" {W(2.8)}/>
<path d="M64 88 V128" stroke="#fff" stroke-width="2.4"/>
{limb("M38 94 L42 52", SK, 8)}{limb("M90 94 L86 52", SK, 8)}
<path d="M36 52 l-2 -9 M41 50 l0 -9 M46 52 l2 -8 M92 52 l2 -9 M87 50 l0 -9 M82 52 l-2 -8" {W(4)}/>
<path d="M36 52 l-2 -9 M41 50 l0 -9 M46 52 l2 -8 M92 52 l2 -9 M87 50 l0 -9 M82 52 l-2 -8" stroke="{SK}" stroke-width="1.6" stroke-linecap="round"/>
{vb(64, 26, 15)}
<circle cx="64" cy="76" r="17" fill="{SK}" {W(2.8)}/>
<path d="M46 74 Q46 56 64 56 Q82 56 82 74 Q72 64 64 66 Q56 64 46 74Z" fill="#C8642A" {W(2.4)}/>
<circle cx="44" cy="82" r="7" fill="none" stroke="#C8642A" stroke-width="5"/><circle cx="84" cy="82" r="7" fill="none" stroke="#C8642A" stroke-width="5"/>
<circle cx="57" cy="78" r="6" fill="#fff" fill-opacity=".5" {W(2.2)}/><circle cx="71" cy="78" r="6" fill="#fff" fill-opacity=".5" {W(2.2)}/><path d="M63 78 H65" {W(2.2)}/>
{eye(57, 78, .42)}{eye(71, 78, .42)}<path d="M60 87 Q64 90 68 87" fill="none" {W(2)}/>''')

# 13. Beach Volleyball, Хорошёво — мальчик в кепке козырьком назад бьёт на песке
I["beach-volleyball-school-leto-khoroshevo"] = ("загорелый мальчик в зелёной кепке козырьком назад", "выпрыгнул с песка и бьёт мяч влево, из-под пяток фонтаном летит песок", ("#D6F8FF", "#22B0D0"), f'''
<path d="M0 104 Q64 96 128 104 V128 H0Z" fill="#F6D38A" {W(2.4)}/>
<circle cx="96" cy="104" r="3" fill="#F6D38A" {W(1.6)}/><circle cx="108" cy="96" r="2.4" fill="#F6D38A" {W(1.6)}/><circle cx="86" cy="96" r="2" fill="#F6D38A" {W(1.6)}/><circle cx="114" cy="108" r="2.6" fill="#F6D38A" {W(1.6)}/>
{limb("M82 84 L96 96 L104 90", "#C88A5A", 7)}{limb("M76 86 L84 100", "#C88A5A", 7)}
<path d="M62 62 Q74 56 86 64 L82 88 L68 84Z" fill="#FF9A2A" {W(2.8)}/>
{limb("M66 64 L44 36", "#C88A5A", 7)}{limb("M82 66 L94 76", "#C88A5A", 7)}
<circle cx="76" cy="46" r="13" fill="#C88A5A" {W(2.8)}/>
<path d="M63 44 Q64 32 76 32 Q88 32 89 44 Q76 40 63 44Z" fill="#3CB04A" {W(2.4)}/><path d="M88 40 Q98 40 100 46 L89 46Z" fill="#3CB04A" {W(2.2)}/>
{eye(71, 49, .45)}{eye(80, 49, .45)}<path d="M72 55 Q76 58 80 55" fill="none" {W(2)}/>
{vb(34, 26, 13)}
<path d="M20 40 L10 48 M28 44 L22 54" {W(2.4)}/>''')

# 14. Beach Volleyball, Тропарёво — сёстры-близняшки дают «пять» в прыжке
I["beach-volleyball-school-leto-troparevo"] = ("сёстры-близняшки в красных купальниках", "в прыжке над песком дают друг другу «пять» после выигранного очка, мяч лежит внизу", ("#FFD8A8", "#B85AC0"), f'''
<path d="M0 106 Q64 98 128 106 V128 H0Z" fill="#F6D38A" {W(2.4)}/>
{limb("M34 84 L26 98", SK, 7)}{limb("M42 84 L46 100", SK, 7)}
{limb("M94 84 L102 98", SK, 7)}{limb("M86 84 L82 100", SK, 7)}
<path d="M28 62 Q38 56 48 62 L46 86 H30Z" fill="#E8303A" {W(2.8)}/>
<path d="M80 62 Q90 56 100 62 L98 86 H82Z" fill="#E8303A" {W(2.8)}/>
{limb("M44 64 L60 30", SK, 7)}{limb("M84 64 L68 30", SK, 7)}
{limb("M32 66 L22 78", SK, 7)}{limb("M96 66 L106 78", SK, 7)}
{head(38, 46, 13, "#F2C23A", .45)}{head(90, 46, 13, "#F2C23A", .45)}
<path d="M26 40 Q16 44 20 56 M102 40 Q112 44 108 56" fill="none" stroke="#F2C23A" stroke-width="5" stroke-linecap="round"/>
<path d="M64 8 L67 18 L77 16 L70 23 L75 31 L66 27 L62 36 L60 26 L51 26 L58 20 L54 12 L62 16Z" fill="#FFF3A0" {W(2)}/>
{vb(64, 104, 11)}''')

# 15. Beach Volleyball, Сокол — мальчик-подавальщик бежит с охапкой мячей
I["beach-volleyball-school-sokol"] = ("мальчик-подавальщик мячей в оранжевой панамке", "бежит босиком по песку с охапкой из трёх волейбольных мячей, позади следы", ("#EEFCD8", "#6CBF4A"), f'''
<path d="M0 102 Q64 94 128 102 V128 H0Z" fill="#F6D38A" {W(2.4)}/>
<ellipse cx="14" cy="114" rx="4" ry="2" fill="#D8AE5A"/><ellipse cx="26" cy="120" rx="4" ry="2" fill="#D8AE5A"/><ellipse cx="38" cy="112" rx="4" ry="2" fill="#D8AE5A"/>
{limb("M60 92 L46 104 L40 100", SK, 7)}{limb("M70 92 L80 112", SK, 7)}
<path d="M54 64 Q66 58 78 64 L76 94 H56Z" fill="#fff" {W(2.8)}/>
{vb(84, 50, 11)}{vb(88, 72, 12)}{vb(80, 92, 11)}
{limb("M58 70 L74 86 L80 82", SK, 7)}{limb("M74 66 L94 62", SK, 7)}
{head(62, 44, 14, "#5A3A26", .48)}
<path d="M46 42 Q46 26 62 26 Q78 26 78 42 Z" fill="#FF8A2A" {W(2.6)}/><path d="M42 42 H82" {W(3)}/>''')

# 16. RusVolley, Красноказарменная — подача в прыжке, вид со спины
I["rusvolley-krasnokazarmennaya"] = ("девочка в оранжевой майке с номером 10 (вид со спины)", "подбросила мяч для подачи в прыжке, впереди вдали — сетка вечернего зала", ("#6A7AD8", "#1C2660"), f'''
<path d="M0 74 H128" stroke="#fff" stroke-width="1.6" opacity=".5"/>
<path d="M14 50 V74 M114 50 V74" stroke="#fff" stroke-width="2.4"/>
<path d="M14 52 H114" stroke="#fff" stroke-width="3"/>
<path d="M14 56 H114 M14 62 H114 M14 68 H114 M24 52 V70 M36 52 V70 M48 52 V70 M60 52 V70 M72 52 V70 M84 52 V70 M96 52 V70 M106 52 V70" stroke="#fff" stroke-width="1" opacity=".55"/>
<circle cx="24" cy="10" r="4" fill="#FFF3A0"/><circle cx="104" cy="10" r="4" fill="#FFF3A0"/>
<path d="M36 92 Q64 80 92 92 L96 128 H32Z" fill="#FF8A2A" {W(2.8)}/>
<text x="64" y="120" font-family="Arial, sans-serif" font-weight="bold" font-size="20" fill="#fff" text-anchor="middle">10</text>
{limb("M88 94 L98 50", SK, 9)}{limb("M40 94 L28 108", SK, 9)}
<circle cx="64" cy="76" r="17" fill="#4A2A1A" {W(2.8)}/>
<path d="M56 62 Q64 50 72 62" fill="none" stroke="#4A2A1A" stroke-width="8" stroke-linecap="round"/><circle cx="64" cy="56" r="5" fill="#E8403A" {W(2)}/>
{vb(100, 30, 13)}''')

# 17. RusVolley, Старокачаловская — мальчик на скамейке запасных ждёт выхода
I["rusvolley-starokachalovskaya"] = ("мальчик-запасной в жёлтой форме", "сидит на скамейке у края площадки, болтает ногами и держит мяч на коленях — ждёт выхода", ("#F6E6E6", "#B8848A"), f'''
<path d="M70 18 V60 M70 22 H128" {W(2.6)}/>{net(70, 132, 22, 26)}
<path d="M0 104 H128 V128 H0Z" fill="#E7B877" {W(2.4)}/>
<rect x="10" y="84" width="108" height="9" rx="3" fill="#8A5A34" {W(2.6)}/>
<path d="M20 93 V106 M108 93 V106" {W(3)}/>
{limb("M52 86 L46 104", SK, 7)}{limb("M64 86 L72 102", SK, 7)}
<path d="M40 104 h10 v4 h-12Z M70 100 h10 l2 4 h-12Z" fill="#fff" {W(2)}/>
<path d="M44 56 Q58 50 72 56 L74 86 H42Z" fill="#FFD23A" {W(2.8)}/>
<text x="58" y="78" font-family="Arial, sans-serif" font-weight="bold" font-size="13" fill="{O}" text-anchor="middle">12</text>
{vb(58, 80, 13)}
{limb("M46 60 L46 80", SK, 7)}{limb("M70 60 L70 80", SK, 7)}
{head(58, 38, 14, "#C8642A", .48)}''')

# 18. RusVolley, Новотушинский — силуэт в прыжке на фоне закатного солнца
I["rusvolley-novotushinsky"] = ("тёмный силуэт мальчика в прыжке", "бьёт по мячу на фоне огромного оранжевого закатного солнца над пляжной сеткой", ("#FFE08A", "#E8503A"), f'''
<circle cx="64" cy="70" r="40" fill="#FFF3B0" opacity=".85"/>
<path d="M0 102 Q64 94 128 102 V128 H0Z" fill="#7A2A3A"/>
<path d="M10 70 V104 M118 70 V104" stroke="#4A1A2A" stroke-width="3"/>
<path d="M10 72 H118" stroke="#4A1A2A" stroke-width="3"/>
<path d="M10 78 H118 M10 84 H118 M22 72 V86 M34 72 V86 M46 72 V86 M82 72 V86 M94 72 V86 M106 72 V86" stroke="#4A1A2A" stroke-width="1.2"/>
<g fill="#3A1A3A" stroke="#3A1A3A" stroke-linecap="round" stroke-linejoin="round">
<circle cx="62" cy="40" r="9"/>
<path d="M54 50 Q62 46 70 50 L68 72 H56Z"/>
<path d="M68 52 L84 30" stroke-width="6" fill="none"/><path d="M56 54 L46 62" stroke-width="6" fill="none"/>
<path d="M58 70 L50 86 L56 92" stroke-width="6" fill="none"/><path d="M66 70 L72 88" stroke-width="6" fill="none"/>
<circle cx="88" cy="22" r="9"/>
</g>
<path d="M81 20 Q86 18 90 13 M80 26 Q90 24 96 18" fill="none" stroke="#FFC070" stroke-width="1.6"/>
<path d="M96 30 l6 4 M98 22 h7" stroke="#3A1A3A" stroke-width="2.4" stroke-linecap="round"/>''')

# 19. RusVolley, Обручева — подача точно сквозь обруч над сеткой
I["rusvolley-obrucheva"] = ("подвешенный над сеткой оранжевый гимнастический обруч", "на тренировке точности волейбольный мяч пролетает точно сквозь обруч, девочка внизу радуется", ("#FFE6F8", "#C04AA0"), f'''
{net(0, 128, 64, 22)}
<path d="M74 0 V20" {W(2.4)}/>
<ellipse cx="74" cy="38" rx="14" ry="20" fill="none" {W(9)}/><ellipse cx="74" cy="38" rx="14" ry="20" fill="none" stroke="#FF8A2A" stroke-width="5"/>
<path d="M24 64 Q40 30 66 36" fill="none" stroke="#fff" stroke-width="2.6" stroke-dasharray="3 4" stroke-linecap="round"/>
{vb(76, 38, 10)}
<ellipse cx="74" cy="38" rx="14" ry="20" fill="none" stroke="#FF8A2A" stroke-width="5" stroke-dasharray="20 200" stroke-dashoffset="-40"/>
<path d="M30 108 Q44 100 58 108 L60 128 H28Z" fill="#2FC4B8" {W(2.8)}/>
{limb("M32 110 L22 94", SK, 7)}{limb("M56 110 L66 94", SK, 7)}
{head(44, 94, 12, "#3A2A20", .45)}
<path d="M32 90 Q26 98 30 106" fill="none" stroke="#3A2A20" stroke-width="4" stroke-linecap="round"/>
{sparkle(100, 18, 5)}{sparkle(106, 50, 3.5)}''')

# 20. RusVolley, Брянская — мяч-тренажёр на резинке под потолком зала
I["rusvolley-bryanskaya"] = ("мальчик в серой форме с налокотниками", "в прыжке отрабатывает нападающий удар по мячу, подвешенному на резинке к потолку зала", ("#E8EEF2", "#7A8CA0"), f'''
<path d="M0 0 H128 V12 H0Z" fill="#5A6A80" {W(2.4)}/>
<path d="M20 12 L36 52" {W(2)}/><path d="M20 12 L36 52" stroke="#FFD23A" stroke-width="1.2" stroke-dasharray="3 3"/>
{vb(38, 62, 13)}
<path d="M16 76 l-6 4 M24 80 l-4 6" {W(2.2)}/>
<path d="M0 110 H128 V128 H0Z" fill="#E7B877" {W(2.4)}/>
{limb("M80 86 L72 104", SK, 7)}{limb("M90 86 L100 100", SK, 7)}
<path d="M74 60 Q86 54 98 60 L96 88 H76Z" fill="#8A96A8" {W(2.8)}/>
{limb("M78 64 L56 58", SK, 7)}<rect x="62" y="56" width="8" height="7" rx="2" fill="#fff" {W(1.8)}/>
{limb("M94 64 L108 80", SK, 7)}
{head(88, 42, 14, "#C8642A", .5)}
<path d="M54 54 l-4 -4 M54 62 h-6" {W(2.2)}/>''')

# 21. RusVolley, Люблинская — мальчик гордо идёт домой с медалью и мячом
I["rusvolley-lyublinskaya"] = ("мальчик с медалью на шее и мячом под мышкой", "после первого турнира гордо шагает домой мимо спортзала, выпятив грудь", ("#FFE0E0", "#D84A4A"), f'''
<path d="M0 108 H128 V128 H0Z" fill="#B8C0D0" {W(2.4)}/>
<path d="M90 30 H128 V108 H90Z" fill="#fff" opacity=".55"/>
<path d="M98 62 H120 V108 H98Z" fill="#8A5A34" {W(2.4)}/><circle cx="102" cy="86" r="2" fill="{O}"/>
<path d="M92 38 H126 V52 H92Z" fill="#2F6FDB" {W(2.2)}/>
<text x="109" y="49" font-family="Arial, sans-serif" font-weight="bold" font-size="9" fill="#fff" text-anchor="middle">ЗАЛ</text>
{limb("M48 88 L38 106", SK, 7)}{limb("M58 88 L66 106", SK, 7)}
<path d="M32 106 h10 v4 h-12Z M62 106 h10 l2 4 h-12Z" fill="#fff" {W(2)}/>
<path d="M38 58 Q52 52 66 60 L64 90 H40Z" fill="#2F6FDB" {W(2.8)}/>
<path d="M44 58 L52 74 L60 58" fill="none" stroke="#E8403A" stroke-width="3"/>
<circle cx="52" cy="78" r="7" fill="#FFD23A" {W(2.4)}/><text x="52" y="82" font-family="Arial, sans-serif" font-weight="bold" font-size="9" fill="{O}" text-anchor="middle">1</text>
{vb(72, 76, 12)}
{limb("M64 64 L70 84 L62 86", SK, 7)}{limb("M40 64 L30 80", SK, 7)}
<circle cx="52" cy="40" r="15" fill="{SK}" {W(2.8)}/>
<path d="M37 38 Q38 24 52 24 Q66 24 67 38 Q52 32 37 38Z" fill="#E0A030" {W(2.4)}/>
<path d="M43 42 Q46 39 49 42 M55 42 Q58 39 61 42" fill="none" {W(2.4)}/>
<path d="M47 49 Q52 53 57 49" fill="none" {W(2)}/>{blush(42, 48, .45)}{blush(62, 48, .45)}
{sparkle(24, 30, 5)}''')

# 22. RusVolley, Кржижановского — пушка-автомат для подачи мячей
I["rusvolley-krzhizhanovskogo"] = ("пушка-автомат для подачи мячей на колёсиках с глазками", "выстреливает волейбольный мяч дугой через сетку тренировочного зала", ("#8A6AD8", "#3A2280"), f'''
<path d="M0 108 H128 V128 H0Z" fill="#E7B877" {W(2.4)}/>
<path d="M92 50 V108" {W(3)}/>{net(92, 132, 52, 30)}
<path d="M30 40 Q50 6 86 26" fill="none" stroke="#fff" stroke-width="2.6" stroke-dasharray="3 4" stroke-linecap="round"/>
{vb(96, 30, 12)}
<path d="M18 72 L36 40 L50 48 L34 80Z" fill="#7AD8E8" {W(2.8)}/>
<ellipse cx="43" cy="44" rx="8" ry="4" transform="rotate(30 43 44)" fill="{O}"/>
<rect x="10" y="70" width="52" height="28" rx="8" fill="#FFD23A" {W(3)}/>
{eye(28, 82, .55)}{eye(44, 82, .55)}<path d="M32 90 Q36 93 40 90" fill="none" {W(2)}/>{blush(22, 89, .45)}{blush(50, 89, .45)}
<circle cx="20" cy="102" r="7" fill="#5A5A6A" {W(2.6)}/><circle cx="52" cy="102" r="7" fill="#5A5A6A" {W(2.6)}/>
<path d="M58 66 l4 -6 M62 74 l7 -2" stroke="#FFF3A0" stroke-width="2.4" stroke-linecap="round"/>''')

# 23. RusVolley, Волжский б-р — малыши бегут разминку «паровозиком»
I["rusvolley-volzhsky"] = ("четверо малышей в одинаковых голубых майках", "бегут разминку «паровозиком» друг за другом вокруг площадки, первый несёт мяч над головой", ("#F2E0CC", "#9A6A44"), f'''
<path d="M0 96 Q64 88 128 96 V128 H0Z" fill="#E7B877" {W(2.4)}/>
<path d="M0 108 Q64 100 128 108" fill="none" stroke="#fff" stroke-width="3"/>
{limb("M20 98 L14 108", SK, 5)}{limb("M24 98 L30 106", SK, 5)}<path d="M14 82 Q22 78 30 82 L29 100 H15Z" fill="#6AB8F0" {W(2.4)}/>{head(22, 72, 8, "#3A2A20", .32)}
{limb("M40 94 L33 106", SK, 6)}{limb("M45 94 L52 104", SK, 6)}<path d="M33 76 Q42 71 51 76 L50 96 H34Z" fill="#6AB8F0" {W(2.6)}/>{head(42, 64, 9.5, "#E0A030", .36)}
{limb("M68 90 L60 104", SK, 6.5)}{limb("M74 90 L82 102", SK, 6.5)}<path d="M60 68 Q71 62 82 68 L80 92 H62Z" fill="#6AB8F0" {W(2.6)}/>{head(71, 54, 11, "#C8642A", .4)}
{limb("M98 88 L90 104", SK, 7)}{limb("M105 88 L114 102", SK, 7)}<path d="M90 62 Q102 56 114 62 L112 90 H92Z" fill="#6AB8F0" {W(2.8)}/>
{limb("M94 66 L92 36", SK, 7)}{limb("M110 66 L112 36", SK, 7)}
{head(102, 48, 12, "#2A2A3A", .42)}
{vb(101, 30, 10)}''')


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
