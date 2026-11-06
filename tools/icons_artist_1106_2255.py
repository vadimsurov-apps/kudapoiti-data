"""Робот «художник», 06.11 ~22:55 UTC: 40 иконок из auto/icon-repeats.json (больше всего похожих пар —
баскетбол, волейбол, ролики, бассейны). Каждая придумана и нарисована отдельно, вручную:
свой герой, своя сцена, свой ракурс и своя палитра фона. Запуск из корня: python3 tools/icons_artist_1106_2255.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT


def bseams(cx, cy, r, sw=2.6):
    """швы баскетбольного мяча (примитив рисования, не сюжет)"""
    k = r * .55
    return (f'<path d="M{cx} {cy-r} V{cy+r} M{cx-r} {cy} H{cx+r} '
            f'M{cx-r*.72} {cy-r*.7} Q{cx-k*.2} {cy} {cx-r*.72} {cy+r*.7} '
            f'M{cx+r*.72} {cy-r*.7} Q{cx+k*.2} {cy} {cx+r*.72} {cy+r*.7}" fill="none" {W(sw)}/>')


I = {}

# ---------- ВОЛЕЙБОЛ (Nevsky Bears) ----------

I["nevsky-bears-prazhskaya"] = ("медвежонок-волейболист", "ставит блок двумя лапами над сеткой, мяч отскакивает", ("#D8FFF6", "#1F8A84"), f'''
<rect x="0" y="78" width="128" height="16" fill="#fff" {W(2.4)}/>
<path d="M8 78 V94 M24 78 V94 M40 78 V94 M56 78 V94 M72 78 V94 M88 78 V94 M104 78 V94 M120 78 V94 M0 86 H128" stroke="#7A8AA0" stroke-width="1.6"/>
<path d="M40 128 Q40 92 64 90 Q88 92 88 128Z" fill="#9A6234" {W(3)}/>
<path d="M44 84 L34 40 M84 84 L94 40" stroke="{O}" stroke-width="15" stroke-linecap="round"/>
<path d="M44 84 L34 40 M84 84 L94 40" stroke="#9A6234" stroke-width="10" stroke-linecap="round"/>
<circle cx="34" cy="36" r="9" fill="#9A6234" {W(2.6)}/><circle cx="94" cy="36" r="9" fill="#9A6234" {W(2.6)}/>
<ellipse cx="34" cy="38" rx="4" ry="3" fill="#E8B88A"/><ellipse cx="94" cy="38" rx="4" ry="3" fill="#E8B88A"/>
<circle cx="64" cy="70" r="20" fill="#A86C3C" {W(3)}/><circle cx="48" cy="54" r="7" fill="#A86C3C" {W(2.6)}/><circle cx="80" cy="54" r="7" fill="#A86C3C" {W(2.6)}/>
<ellipse cx="64" cy="78" rx="9" ry="7" fill="#E8C49A" {W(2)}/><ellipse cx="64" cy="75" rx="3" ry="2.2" fill="{O}"/>
{eye(56, 66, .5)}{eye(72, 66, .5)}
<circle cx="64" cy="18" r="13" fill="#fff" {W(2.6)}/>
<path d="M51 18 Q60 12 64 5 M64 31 Q66 20 77 16 M52 24 Q64 22 72 29" fill="none" stroke="#2E6BD8" stroke-width="2.4"/>
<path d="M44 10 l-6 -4 M84 10 l6 -4" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

I["nevsky-bears-vodny"] = ("волейбольный мяч-парусник", "плывёт под белым парусом по водохранилищу у Водного стадиона", ("#E6F0FF", "#2848A8"), f'''
<path d="M0 92 Q32 86 64 92 T128 92 V128 H0Z" fill="#2E7FD8"/>
<path d="M8 106 Q24 102 40 106 M80 112 Q96 108 112 112" fill="none" stroke="#9AD0FF" stroke-width="2.6"/>
<path d="M66 20 V60" {W(3)}/>
<path d="M68 22 Q96 40 104 62 H68Z" fill="#fff" {W(2.8)}/><path d="M64 26 Q44 44 40 62 H64Z" fill="#FFE27A" {W(2.6)}/>
<circle cx="64" cy="84" r="24" fill="#fff" {W(3)}/>
<path d="M40 84 Q54 74 58 61 M88 84 Q74 78 70 61 M44 98 Q64 92 84 98" fill="none" stroke="#2E6BD8" stroke-width="2.8"/>
<path d="M58 61 Q50 80 44 98" fill="none" stroke="#FFC530" stroke-width="2.8"/>
{eye(56, 82, .55)}{eye(72, 82, .55)}{smile(64, 89, 3.5, .65)}
<path d="M40 96 Q64 104 88 96" fill="none" stroke="#fff" stroke-width="3"/>''')

I["nevsky-bears-semenovskaya"] = ("волейбольный мяч с иголкой и ниткой", "сам себе подшивает шов, как в ткацкой мастерской", ("#FFF0FA", "#C04A9A"), f'''
<circle cx="58" cy="70" r="40" fill="#fff" {W(3.2)}/>
<path d="M18 70 Q40 56 46 32 M98 70 Q76 62 70 32 M24 92 Q58 82 92 92" fill="none" stroke="#E8304A" stroke-width="3"/>
<path d="M46 32 Q34 66 24 92" fill="none" stroke="#2E6BD8" stroke-width="3"/>
<path d="M70 34 l-4 6 M74 42 l-5 5 M78 50 l-6 4" stroke="{O}" stroke-width="2"/>
{eye(48, 70, .7)}{eye(70, 70, .7)}{smile(59, 80, 4.5, .8)}{blush(38, 80, .8)}{blush(80, 80, .8)}
<path d="M80 54 Q100 46 110 24" fill="none" stroke="#FFC530" stroke-width="2.4" stroke-dasharray="4 3"/>
<path d="M104 30 L118 6" stroke="#8C8CA0" stroke-width="4" stroke-linecap="round"/><circle cx="116" cy="10" r="1.6" fill="#fff"/>''')

I["nevsky-bears-kolomenskaya"] = ("волейбольный мяч-тыква с ботвой", "созрел на грядке в огороде у Садовников", ("#FFF8DC", "#7A9A3A"), f'''
<path d="M0 98 Q64 88 128 98 V128 H0Z" fill="#8A5A2C"/>
<path d="M10 112 Q30 108 50 112 M78 116 Q98 112 118 116" fill="none" stroke="#6A4020" stroke-width="2.6"/>
<path d="M64 36 Q60 22 66 12" fill="none" stroke="#3E8A2E" stroke-width="4" stroke-linecap="round"/>
<path d="M64 24 Q44 10 30 22 Q44 32 64 24Z" fill="#6CC24A" {W(2.4)}/><path d="M66 20 Q86 4 100 16 Q86 28 66 20Z" fill="#7CD25A" {W(2.4)}/>
<path d="M30 30 Q20 40 26 50" fill="none" stroke="#3E8A2E" stroke-width="2.4"/>
<circle cx="64" cy="70" r="32" fill="#fff" {W(3.2)}/>
<path d="M32 70 Q50 60 54 40 M96 70 Q78 64 74 40 M38 88 Q64 80 90 88" fill="none" stroke="#FF8A1E" stroke-width="3"/>
<path d="M54 40 Q44 66 38 88" fill="none" stroke="#2E6BD8" stroke-width="3"/>
{eye(54, 70, .6)}{eye(74, 70, .6)}{smile(64, 78, 4, .7)}{blush(44, 78, .7)}{blush(84, 78, .7)}''')

# ---------- БАСКЕТБОЛ ----------

I["pbk-cska-solntsevo"] = ("баскетбольный мяч-солнышко с лучами", "встаёт из-за щита с кольцом, как утреннее солнце", ("#FFF6D0", "#F06A8A"), f'''
<g stroke="#FFD24A" stroke-width="6" stroke-linecap="round">
<path d="M64 6 V16 M24 22 L32 30 M104 22 L96 30 M10 58 H20 M108 58 H118"/></g>
<circle cx="64" cy="56" r="30" fill="#F2892A" {W(3.2)}/>{bseams(64, 56, 30, 2.6)}
{eye(54, 54, .6)}{eye(74, 54, .6)}{blush(46, 64, .7)}{blush(82, 64, .7)}
<rect x="22" y="78" width="84" height="44" rx="4" fill="#fff" {W(3)}/><rect x="48" y="88" width="32" height="22" fill="none" stroke="#E8304A" stroke-width="3"/>
<path d="M44 110 H84" stroke="#E8304A" stroke-width="5" stroke-linecap="round"/>''')

I["pbk-cska-kronshtadtsky"] = ("баскетбольное кольцо на мачте парусника", "мяч-юнга с палубы забрасывает мяч в кольцо на мачте", ("#E0F0FF", "#1E3E78"), f'''
<path d="M0 104 Q32 98 64 104 T128 104 V128 H0Z" fill="#2E6FB8"/>
<path d="M14 96 H114 L102 116 H26Z" fill="#B8642E" {W(3)}/>
<path d="M88 96 V22" {W(4)}/>
<rect x="74" y="20" width="30" height="22" rx="2" fill="#fff" {W(2.6)}/><path d="M80 42 H96" stroke="#E8304A" stroke-width="3"/>
<path d="M80 44 L84 58 H92 L96 44" fill="none" stroke="#fff" stroke-width="2"/><path d="M82 48 H94 M83 53 H93" stroke="#fff" stroke-width="1.4"/>
<path d="M90 70 L72 60 L90 52" fill="#E8304A" {W(2)}/>
<circle cx="42" cy="68" r="22" fill="#F2892A" {W(3)}/>{bseams(42, 68, 22, 2.2)}
{eye(35, 68, .5)}{eye(49, 68, .5)}{smile(42, 75, 3, .6)}
<path d="M52 40 Q62 26 72 32" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 3"/>''')

I["ibasket-begovaya"] = ("баскетбольный мяч-бегун с номером «1» на груди", "рвёт финишную ленточку на беговой дорожке", ("#F2FAFF", "#68B8E8"), f'''
<path d="M0 96 H128 V128 H0Z" fill="#D8503A"/>
<path d="M0 106 H128 M0 118 H128" stroke="#fff" stroke-width="2"/>
<path d="M4 58 Q64 66 124 52" fill="none" stroke="#FFD24A" stroke-width="4"/>
<path d="M30 92 L22 106 M64 92 L78 104" stroke="{O}" stroke-width="6" stroke-linecap="round"/>
<circle cx="48" cy="60" r="32" fill="#F2892A" {W(3.2)}/>{bseams(48, 60, 32, 2.6)}
<rect x="36" y="64" width="24" height="18" rx="3" fill="#fff" {W(2.4)}/>
<text x="44" y="79" font-family="Arial" font-size="15" font-weight="bold" fill="{O}">1</text>
{eye(40, 48, .6)}{eye(58, 48, .6)}<path d="M44 56 Q49 61 54 56" fill="#E8554A" {W(2)}/>
<path d="M94 40 H116 M98 52 H122 M94 64 H112" stroke="#fff" stroke-width="3" stroke-linecap="round"/>''')

I["ibasket-korolev"] = ("баскетбольный мяч-планета с кольцом корзины вместо кольца Сатурна", "летит по орбите в фиолетовом космосе над Королёвом", ("#C88AF0", "#3A1468"), f'''
{sparkle(18, 30, 5)}{sparkle(106, 22, 4)}{sparkle(20, 100, 3)}{sparkle(110, 104, 4, "#FFE27A")}
<circle cx="88" cy="110" r="1.8" fill="#fff"/><circle cx="34" cy="14" r="1.6" fill="#fff"/>
<path d="M14 74 Q64 96 114 74" fill="none" stroke="#E8304A" stroke-width="7" stroke-linecap="round"/>
<circle cx="64" cy="64" r="30" fill="#F2892A" {W(3.2)}/>{bseams(64, 64, 30, 2.6)}
<path d="M36 74 Q64 90 92 74" fill="none" stroke="#E8304A" stroke-width="7" stroke-linecap="round"/>
<path d="M50 84 L54 100 M64 86 V104 M78 84 L74 100 M52 94 H76" stroke="#fff" stroke-width="2"/>
{eye(54, 58, .6)}{eye(74, 58, .6)}{smile(64, 66, 3.5, .65)}''')

I["ibasket-orshanskaya"] = ("баскетбольный мяч, застрявший в сетке кольца", "смущённо выглядывает снизу из сетки под щитом", ("#E8FFF2", "#38B888"), f'''
<rect x="18" y="6" width="92" height="34" rx="4" fill="#fff" {W(3)}/><rect x="46" y="16" width="36" height="20" fill="none" stroke="#E8304A" stroke-width="3"/>
<ellipse cx="64" cy="42" rx="30" ry="6" fill="none" stroke="#E8304A" stroke-width="5"/>
<circle cx="64" cy="76" r="30" fill="#F2892A" {W(3.2)}/>{bseams(64, 76, 30, 2.4)}
<path d="M34 42 L42 100 M46 44 L50 104 M58 46 L60 106 M70 46 L68 106 M82 44 L78 104 M94 42 L86 100 M36 58 Q64 66 92 58 M40 78 Q64 86 88 78 M44 96 Q64 102 84 96" fill="none" stroke="#fff" stroke-width="2.2"/>
{eye(54, 82, .55)}{eye(74, 82, .55)}<path d="M60 92 Q64 89 68 92" fill="none" {W(2)}/>
<path d="M98 80 q4 6 0 10" fill="none" stroke="#5CB7F2" stroke-width="3" stroke-linecap="round"/>{blush(46, 90, .6)}{blush(82, 90, .6)}''')

I["ibasket-talalikhina"] = ("большой и маленький баскетбольные мячи", "малыш-мячик сидит на макушке большого и тянется к кольцу", ("#FFF0E6", "#E89070"), f'''
<rect x="78" y="6" width="44" height="26" rx="3" fill="#fff" {W(2.6)}/><ellipse cx="96" cy="36" rx="14" ry="3.5" fill="none" stroke="#E8304A" stroke-width="4"/>
<path d="M84 38 L88 50 H104 L108 38" fill="none" stroke="#fff" stroke-width="2"/>
<circle cx="56" cy="90" r="32" fill="#E8781E" {W(3.2)}/>{bseams(56, 90, 32, 2.6)}
{eye(46, 88, .6)}{eye(66, 88, .6)}{smile(56, 97, 4, .7)}{blush(38, 98, .7)}{blush(74, 98, .7)}
<circle cx="58" cy="44" r="14" fill="#F8A040" {W(2.8)}/>{bseams(58, 44, 14, 1.8)}
{eye(54, 44, .38)}{eye(63, 44, .38)}
<path d="M70 38 L80 30" {W(3.4)}/>''')

I["cska-basket-aeroport"] = ("баскетбольный мяч в полёте трёхочкового броска", "летит по пунктирной дуге через всю площадку в кольцо, табло «+3»", ("#E6ECFF", "#B02840"), f'''
<path d="M16 108 Q40 20 96 44" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="5 5"/>
<rect x="98" y="30" width="26" height="40" rx="3" fill="#fff" {W(2.6)}/><ellipse cx="98" cy="58" rx="12" ry="3.5" fill="none" stroke="#E8304A" stroke-width="4"/>
<path d="M88 60 L92 74 H104 L106 60" fill="none" stroke="#fff" stroke-width="2"/>
<rect x="8" y="12" width="40" height="22" rx="4" fill="#1A1A3A" {W(2.4)}/>
<text x="14" y="29" font-family="Arial" font-size="15" font-weight="bold" fill="#FFD24A">+3</text>
<circle cx="56" cy="70" r="26" fill="#F2892A" {W(3.2)}/>{bseams(56, 70, 26, 2.4)}
{eye(48, 68, .55)}{eye(64, 68, .55)}<ellipse cx="56" cy="78" rx="3.4" ry="3" fill="#E8554A" {W(1.8)}/>
<path d="M22 96 l-8 6 M30 102 l-6 8" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

I["husky-basket-kantemirovskaya"] = ("щенок хаски за огромным баскетбольным мячом", "выглядывает из-за мяча, положив на него лапы", ("#F4FCFF", "#7AB4D8"), f'''
<path d="M28 44 L22 14 L44 30Z M100 44 L106 14 L84 30Z" fill="#6A7A90" {W(2.8)}/><path d="M28 36 L26 22 L36 30Z M100 36 L102 22 L92 30Z" fill="#FFC8D8"/>
<ellipse cx="64" cy="46" rx="38" ry="26" fill="#6A7A90" {W(3)}/>
<path d="M44 52 Q50 30 64 40 Q78 30 84 52 Q64 64 44 52Z" fill="#fff"/>
{eye(52, 44, .55)}{eye(76, 44, .55)}<ellipse cx="64" cy="54" rx="4" ry="3" fill="{O}"/>
<circle cx="64" cy="94" r="34" fill="#F2892A" {W(3.2)}/>{bseams(64, 94, 34, 2.6)}
<ellipse cx="40" cy="64" rx="9" ry="6" fill="#fff" {W(2.4)}/><ellipse cx="88" cy="64" rx="9" ry="6" fill="#fff" {W(2.4)}/>''')

I["husky-basket-sokol"] = ("скачущий баскетбольный мяч-дриблёр", "спрыгивает по ступенькам лестницы, оставляя дуги отскоков", ("#FFFBE0", "#B8B060"), f'''
<path d="M0 50 H34 V74 H66 V98 H98 V122 H128 V128 H0Z" fill="#9A9AB0" {W(3)}/>
<path d="M8 40 Q20 10 36 34 M48 64 Q58 36 72 60" fill="none" stroke="#fff" stroke-width="2.6" stroke-dasharray="4 4"/>
<circle cx="88" cy="70" r="24" fill="#F2892A" {W(3.2)}/>{bseams(88, 70, 24, 2.4)}
{eye(80, 66, .55)}{eye(96, 66, .55)}<path d="M82 76 Q88 82 94 76" fill="#E8554A" {W(2)}/>
<path d="M76 98 Q88 102 100 98" fill="none" stroke="{O}" stroke-width="2.4" opacity=".5"/>''')

I["ibasket-prazhskaya"] = ("баскетбольный мяч в гамаке из сетки кольца", "отдыхает после тренировки и посапывает, вечер", ("#EAE0FF", "#5A4AA0"), f'''
<path d="M8 40 V128 M120 40 V128" stroke="#FFF" stroke-width="5"/>
<ellipse cx="14" cy="36" rx="10" ry="4" fill="none" stroke="#E8304A" stroke-width="4"/><ellipse cx="114" cy="36" rx="10" ry="4" fill="none" stroke="#E8304A" stroke-width="4"/>
<path d="M14 40 Q64 120 114 40" fill="none" stroke="#fff" stroke-width="2.4"/>
<circle cx="64" cy="70" r="26" fill="#F2892A" {W(3.2)}/>{bseams(64, 70, 26, 2.4)}
<path d="M54 68 Q57 71 60 68 M68 68 Q71 71 74 68" fill="none" {W(2.2)}/><ellipse cx="64" cy="78" rx="2.6" ry="2" fill="{O}"/>
<path d="M14 40 Q30 104 64 98 Q98 104 114 40 M24 58 Q64 100 104 58 M20 50 L40 96 M44 92 L52 98 M84 92 L76 98 M108 50 L88 96" fill="none" stroke="#fff" stroke-width="2.2"/>
<text x="88" y="38" font-family="Arial" font-size="13" font-weight="bold" fill="#fff">z</text><text x="98" y="26" font-family="Arial" font-size="10" font-weight="bold" fill="#fff">z</text>
<circle cx="30" cy="20" r="8" fill="#FFF4B0"/><circle cx="34" cy="17" r="7" fill="#6A5AB0"/>''')

# ---------- ТЕННИС ----------

I["tennis-capital-yuzhnaya"] = ("жёлтый теннисный мяч, подброшенный на подаче", "зависает в воздухе над поднятой ракеткой, корт грунтовый", ("#FFE8D8", "#D86A3A"), f'''
<circle cx="64" cy="30" r="20" fill="#D7F25A" {W(3)}/>
<path d="M46 22 Q58 30 50 46 M82 22 Q70 30 78 46" fill="none" stroke="#fff" stroke-width="2.6"/>
{eye(58, 30, .5)}{eye(70, 30, .5)}<ellipse cx="64" cy="38" rx="2.6" ry="2.4" fill="#E8554A"/>
<g transform="rotate(30 64 90)">
<ellipse cx="64" cy="80" rx="22" ry="28" fill="#fff" fill-opacity=".5" stroke="#2E6BD8" stroke-width="5"/>
<path d="M50 62 V98 M57 56 V104 M64 54 V106 M71 56 V104 M78 62 V98 M44 70 H84 M42 80 H86 M44 90 H84" stroke="#8A9AB0" stroke-width="1.4"/>
<rect x="60" y="108" width="8" height="24" rx="3" fill="{O}"/></g>
<path d="M22 22 l-6 -6 M106 22 l6 -6 M28 44 h-8" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

# ---------- РОЛИКИ ----------

I["extremekids-roller-novoperedelkino"] = ("малыш на роликах в шлеме и наколенниках", "едет «ласточкой» на одной ноге, вторая вытянута назад", ("#DFFFFA", "#1AA8A0"), f'''
<path d="M0 108 H128 V128 H0Z" fill="#8C8CA0"/><path d="M8 118 H30 M50 118 H76 M96 118 H120" stroke="#fff" stroke-width="3"/>
<path d="M60 74 L60 98" stroke="#FF8A5A" stroke-width="10" stroke-linecap="round"/>
<path d="M60 74 L104 56" stroke="#FF8A5A" stroke-width="10" stroke-linecap="round"/>
<rect x="48" y="94" width="26" height="12" rx="4" fill="#FFD24A" {W(2.4)}/><g fill="#fff" {W(1.8)}><circle cx="52" cy="108" r="3"/><circle cx="60" cy="108" r="3"/><circle cx="68" cy="108" r="3"/></g>
<g transform="rotate(-22 108 54)"><rect x="100" y="46" width="22" height="12" rx="4" fill="#FFD24A" {W(2.4)}/></g>
<path d="M40 50 L80 70" stroke="#4A9AE8" stroke-width="16" stroke-linecap="round"/>
<path d="M40 50 L16 46 M52 56 L36 72" stroke="#FFD9B8" stroke-width="6" stroke-linecap="round"/>
<circle cx="36" cy="36" r="13" fill="#FFD9B8" {W(2.8)}/>
<path d="M22 34 Q22 18 38 20 Q52 22 50 34Z" fill="#E8304A" {W(2.6)}/>
{eye(32, 38, .4)}{eye(41, 38, .4)}<path d="M34 44 Q37 46 40 44" fill="none" {W(1.6)}/>
<circle cx="62" cy="90" r="5" fill="#2E2E4A"/>
<path d="M14 92 h14 M8 82 h12" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

I["extremekids-roller-fryazino"] = ("салатовый роликовый конёк-слаломист", "объезжает змейкой оранжевые конусы", ("#F8F0FF", "#9A6AD8"), f'''
<path d="M0 104 H128 V128 H0Z" fill="#6A6A86"/>
<path d="M14 104 L20 84 L26 104Z M100 104 L106 84 L112 104Z" fill="#FF8A1E" {W(2.2)}/><path d="M17 96 H23 M103 96 H109" stroke="#fff" stroke-width="2"/>
<path d="M10 116 Q36 96 64 114 T118 112" fill="none" stroke="#fff" stroke-width="2.2" stroke-dasharray="4 4"/>
<g transform="rotate(-8 64 64)">
<path d="M40 24 H70 V60 H92 Q100 60 100 70 V80 H36 V30 Q36 24 40 24Z" fill="#9AE04A" {W(3)}/>
<path d="M36 34 H70 M54 40 l10 0 M54 48 l10 0" stroke="#fff" stroke-width="2.6"/>
<rect x="32" y="80" width="72" height="8" rx="3" fill="#3B3355"/>
<g fill="#FFD24A" {W(2.4)}><circle cx="42" cy="94" r="7"/><circle cx="58" cy="94" r="7"/><circle cx="74" cy="94" r="7"/><circle cx="90" cy="94" r="7"/></g>
{eye(48, 58, .5)}{eye(62, 58, .5)}{smile(55, 66, 3, .6)}</g>''')

I["schoolrollers-universitet"] = ("пара роликов, держащихся за шнурки как за руки", "катятся с горки на закате, вдали шпиль МГУ", ("#FFE8C8", "#E05A6A"), f'''
<path d="M54 60 V30 M50 40 H58" stroke="#B05060" stroke-width="3"/><path d="M42 60 V44 H66 V60" fill="#C86070" opacity=".6"/>
<path d="M0 80 L128 112 V128 H0Z" fill="#6ACF7A" {W(2.6)}/>
<g transform="rotate(14 64 80)">
<path d="M22 60 H40 V78 H50 Q56 78 56 84 V88 H20 V64 Q20 60 22 60Z" fill="#5AB8F0" {W(2.6)}/>
<g fill="#fff" {W(2)}><circle cx="26" cy="94" r="4"/><circle cx="36" cy="94" r="4"/><circle cx="46" cy="94" r="4"/></g>
{eye(28, 72, .38)}{eye(36, 72, .38)}
<path d="M72 54 H92 V74 H102 Q108 74 108 80 V86 H70 V58 Q70 54 72 54Z" fill="#FF7FB0" {W(2.6)}/>
<g fill="#fff" {W(2)}><circle cx="76" cy="92" r="4"/><circle cx="88" cy="92" r="4"/><circle cx="100" cy="92" r="4"/></g>
{eye(78, 66, .38)}{eye(86, 66, .38)}
<path d="M40 64 Q56 50 72 60" fill="none" stroke="#FFD24A" stroke-width="3"/></g>''')

# ---------- ТАНЦЫ ----------

I["todes-skladochnaya"] = ("красная бальная туфелька на шпильке", "делает пируэт на паркете, вокруг летают нотки", ("#FFE0E8", "#8A2040"), f'''
<path d="M0 104 H128 V128 H0Z" fill="#C88A4A"/><path d="M0 116 H128 M30 104 V116 M70 104 V116 M100 116 V128 M50 116 V128" stroke="#A86A30" stroke-width="2"/>
<path d="M14 92 Q12 82 26 80 Q48 78 62 70 Q80 58 96 34 Q108 26 112 38 Q114 58 104 74 L100 76 L104 102 H96 L92 80 Q74 92 46 94 Z" fill="#E8304A" {W(3.2)}/>
<path d="M26 80 Q44 72 58 72 Q70 70 78 62" fill="none" stroke="{O}" stroke-width="2.6"/>
<path d="M30 84 Q48 82 62 76" fill="none" stroke="#FF8AA0" stroke-width="2.6" stroke-linecap="round"/>
<path d="M96 34 Q104 32 108 40" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
{eye(40, 86, .45)}{eye(52, 84, .45)}
<path d="M16 34 V54 M16 34 L28 31" {W(2.4)}/><ellipse cx="13" cy="54" rx="4" ry="3" fill="{O}"/>
<path d="M50 18 V36 M62 16 V34 M50 18 L62 16" {W(2.4)}/><ellipse cx="47" cy="36" rx="4" ry="3" fill="{O}"/><ellipse cx="59" cy="34" rx="4" ry="3" fill="{O}"/>
<path d="M24 112 Q64 96 112 108" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 4"/>
{sparkle(110, 14, 5)}''')

# ---------- МУЗЕИ, ПАРКИ, РАЗВЛЕЧЕНИЯ ----------

I["ogni-moskvy"] = ("старинная керосиновая лампа с язычком пламени", "светит тёплым светом, к ней прилетел мотылёк", ("#FFF2C8", "#C87A1E"), f'''
<circle cx="64" cy="52" r="36" fill="#FFE27A" opacity=".55"/>
<rect x="36" y="100" width="56" height="14" rx="5" fill="#B8862E" {W(3)}/>
<path d="M44 100 Q36 82 50 76 H78 Q92 82 84 100Z" fill="#D8A040" {W(3)}/>
<path d="M50 76 Q40 54 54 30 H74 Q88 54 78 76Z" fill="#E8F6FF" fill-opacity=".8" {W(3)}/>
<rect x="50" y="22" width="28" height="10" rx="3" fill="#B8862E" {W(2.6)}/>
<path d="M64 70 Q54 60 60 50 Q62 44 64 38 Q68 48 70 52 Q74 62 64 70Z" fill="#FF8A1E" {W(2.2)}/><path d="M64 66 Q60 60 63 54 Q66 58 66 62Z" fill="#FFE27A"/>
{eye(56, 88, .5)}{eye(72, 88, .5)}{smile(64, 94, 3, .6)}
<path d="M98 34 Q92 26 98 22 Q104 26 98 34 Q104 40 110 36 Q106 30 98 34Z" fill="#fff" {W(1.8)}/>''')

I["ostankino-tower"] = ("Останкинская телебашня-великан", "выглядывает над облаками ночью, шпиль подсвечен", ("#6A5AC8", "#1A1440"), f'''
{sparkle(20, 24, 4)}{sparkle(104, 40, 3, "#FFE27A")}<circle cx="30" cy="54" r="1.8" fill="#fff"/><circle cx="96" cy="18" r="1.6" fill="#fff"/>
<path d="M64 4 V24" stroke="#E8304A" stroke-width="3"/><circle cx="64" cy="4" r="3" fill="#FF5A5A"/>
<path d="M58 24 H70 L74 116 H54Z" fill="#E8ECF4" {W(3)}/>
<rect x="50" y="40" width="28" height="14" rx="4" fill="#FFE27A" {W(2.6)}/>
<path d="M58 70 H70 M57 86 H71" stroke="#B8C0D0" stroke-width="2"/>
{eye(60, 62, .4)}{eye(68, 62, .4)}<path d="M61 69 Q64 71 67 69" fill="none" {W(1.6)}/>
<path d="M0 104 Q14 88 30 98 Q40 84 56 96 Q66 84 80 96 Q94 86 104 98 Q118 90 128 100 V128 H0Z" fill="#fff" {W(2.6)}/>''')

I["troparyovo"] = ("деревянный лесной указатель-стрелка", "стоит на развилке тропинки между ёлками", ("#E4FFE0", "#2E7A3E"), f'''
<path d="M18 92 L4 92 L18 40 L32 92Z M114 96 L100 96 L114 48 L128 96Z" fill="#2E8A4A" {W(2.4)}/>
<path d="M44 128 Q56 100 64 96 Q72 100 84 128 M64 96 Q80 90 120 104" fill="#E8D0A0"/>
<path d="M64 112 V40" stroke="#8F5A2C" stroke-width="8"/><path d="M64 112 V40" {W(2)} fill="none" opacity=".4"/>
<path d="M30 30 H82 L94 42 L82 54 H30Z" fill="#C8884A" {W(3)}/>
<path d="M98 62 H46 L36 72 L46 82 H98Z" fill="#B87838" {W(3)}/>
{eye(52, 42, .5)}{eye(66, 42, .5)}{smile(59, 48, 3, .55)}
<path d="M54 72 H88" stroke="#8F5A2C" stroke-width="2.4" stroke-dasharray="6 4"/>''')

I["doaflip-zhukova"] = ("малыш, крутящий сальто", "летит вверх ногами над батутом по дуге", ("#FFE6F6", "#E04AA0"), f'''
<ellipse cx="64" cy="108" rx="48" ry="10" fill="#2E2E4A" {W(3)}/><ellipse cx="64" cy="106" rx="40" ry="6" fill="#4A4A70"/>
<path d="M20 110 L24 124 M108 110 L104 124 M64 118 V126" {W(3)}/>
<path d="M18 92 Q20 30 64 22 Q104 28 110 78" fill="none" stroke="#fff" stroke-width="2.6" stroke-dasharray="5 5"/>
<path d="M104 70 l6 10 l6 -8" fill="none" stroke="#fff" stroke-width="2.6"/>
<circle cx="64" cy="76" r="12" fill="#FFD9B8" {W(2.8)}/>
<path d="M52 78 Q52 90 64 90 Q76 90 76 78" fill="#7A4A2A" {W(2.4)}/>
<path d="M58 72 Q60 70 62 72 M66 72 Q68 70 70 72" fill="none" {W(1.8)}/><path d="M60 66 Q64 63 68 66" fill="none" {W(1.8)}/>
<rect x="52" y="40" width="24" height="26" rx="8" fill="#4AC8F0" {W(2.8)}/>
<path d="M56 40 L48 18 M72 40 L82 20" stroke="#FF8A5A" stroke-width="8" stroke-linecap="round"/>
<path d="M52 56 L36 66 M76 56 L92 64" stroke="#FFD9B8" stroke-width="6" stroke-linecap="round"/>''')

I["archaeology-museum"] = ("старинная серебряная монета-персонаж", "выглядывает из раскопа под землёй, кисточка счищает с неё пыль", ("#F6E8D0", "#8A5A30"), f'''
<path d="M0 52 H128 V128 H0Z" fill="#A87444"/>
<path d="M0 74 H128 M0 98 H128" stroke="#8A5A30" stroke-width="3"/>
<g fill="#C89A6A"><circle cx="16" cy="64" r="3"/><circle cx="110" cy="86" r="4"/><circle cx="24" cy="110" r="3"/><circle cx="100" cy="116" r="2.6"/></g>
<circle cx="56" cy="78" r="28" fill="#D8DCE6" {W(3.2)}/><circle cx="56" cy="78" r="21" fill="none" stroke="#A8B0C0" stroke-width="2.4"/>
<g fill="#A8B0C0"><circle cx="56" cy="56" r="1.6"/><circle cx="76" cy="70" r="1.6"/><circle cx="36" cy="70" r="1.6"/><circle cx="46" cy="98" r="1.6"/></g>
{eye(48, 76, .55)}{eye(64, 76, .55)}{smile(56, 84, 3.5, .65)}
<path d="M84 20 L104 50" stroke="#C8884A" stroke-width="6" stroke-linecap="round"/>
<path d="M76 46 Q80 40 84 44 L96 58 Q92 66 84 64Z" fill="#3B3355"/><path d="M80 50 L74 60 M86 56 L80 66 M90 60 L86 70" stroke="#E8C080" stroke-width="2.4" stroke-linecap="round"/>
{sparkle(30, 46, 4)}{sparkle(86, 92, 3)}''')

I["warpoint-davydkovo"] = ("малыш в VR-шлеме", "тянет руки к виртуальной звезде среди светящихся пикселей", ("#4AF0E0", "#3A1AA0"), f'''
<g fill="#7AF0FF" opacity=".8"><rect x="14" y="26" width="8" height="8"/><rect x="104" y="80" width="8" height="8"/><rect x="22" y="88" width="6" height="6"/><rect x="100" y="20" width="6" height="6"/></g>
{sparkle(84, 22, 12, "#FFE27A")}
<path d="M44 128 Q44 92 64 90 Q84 92 84 128Z" fill="#FF8A5A" {W(3)}/>
<path d="M50 96 L70 36 M78 96 L84 40" stroke="#FFD9B8" stroke-width="7" stroke-linecap="round"/>
<circle cx="64" cy="76" r="18" fill="#FFD9B8" {W(3)}/>
<path d="M46 66 Q46 50 64 50 Q82 50 82 66Z" fill="#6A3A1A" {W(2.4)}/>
<rect x="44" y="64" width="40" height="16" rx="6" fill="#2E2E4A" {W(2.6)}/><rect x="48" y="68" width="32" height="6" rx="3" fill="#4AF0E0"/>
<path d="M58 86 Q64 91 70 86" fill="#E8554A" {W(1.8)}/>''')

I["golf-mcc-kids"] = ("малыш-гольфист в клетчатой кепке", "замахивается клюшкой на зелёном холме, мячик на подставке", ("#E8FFF0", "#1E8A5A"), f'''
<path d="M0 98 Q64 80 128 98 V128 H0Z" fill="#5ACF6A" {W(2.4)}/>
<path d="M104 92 V52" {W(2.6)}/><path d="M104 52 L122 58 L104 64Z" fill="#E8304A" {W(2)}/><ellipse cx="104" cy="94" rx="6" ry="2" fill="#1A3A2A"/>
<path d="M38 96 V104" {W(2.4)}/><circle cx="38" cy="92" r="4" fill="#fff" {W(2)}/>
<path d="M30 20 L54 54" stroke="#8C8CA0" stroke-width="4" stroke-linecap="round"/><path d="M24 14 L34 18 L30 26 L22 22Z" fill="#5A5A70" {W(1.8)}/>
<path d="M56 96 L52 108 M70 96 L74 108" stroke="#2E4A8A" stroke-width="7" stroke-linecap="round"/>
<rect x="50" y="64" width="26" height="32" rx="8" fill="#FFD24A" {W(2.8)}/>
<path d="M52 72 L54 54 M74 72 L56 56" stroke="#FFD9B8" stroke-width="6" stroke-linecap="round"/>
<circle cx="66" cy="48" r="13" fill="#FFD9B8" {W(2.8)}/>
<path d="M52 44 Q52 30 66 32 Q80 32 80 44 Z" fill="#E8304A" {W(2.4)}/><path d="M60 34 V44 M70 33 V44 M53 39 H79" stroke="#fff" stroke-width="1.6"/>
<path d="M78 44 H88" {W(3)}/>{eye(62, 50, .38)}{eye(71, 50, .38)}<path d="M63 55 Q66 57 69 55" fill="none" {W(1.6)}/>''')

I["cin-yerevan-plaza"] = ("окошко киноаппаратной с лучом проектора", "луч летит в тёмный зал, в нём пылинки и улыбающаяся звёздочка", ("#7A2040", "#200818"), f'''
<path d="M30 40 L128 10 V100 L30 56Z" fill="#FFF6C8" opacity=".55"/>
<rect x="8" y="30" width="32" height="34" rx="6" fill="#4A4A62" {W(3)}/>
<circle cx="32" cy="48" r="9" fill="#BFE6FF" {W(2.6)}/><circle cx="32" cy="48" r="4" fill="#fff"/>
<circle cx="16" cy="22" r="10" fill="#4A4A62" {W(2.6)}/><circle cx="34" cy="20" r="10" fill="#4A4A62" {W(2.6)}/>
<circle cx="16" cy="22" r="3" fill="#8A8AA0"/><circle cx="34" cy="20" r="3" fill="#8A8AA0"/>
{sparkle(88, 48, 16, "#FFE27A")}{eye(84, 48, .38)}{eye(92, 48, .38)}
<g fill="#fff"><circle cx="58" cy="44" r="1.6"/><circle cx="70" cy="34" r="1.4"/><circle cx="110" cy="30" r="1.6"/><circle cx="112" cy="70" r="1.4"/></g>
<path d="M0 98 Q16 84 32 98 Q48 84 64 98 Q80 84 96 98 Q112 84 128 98 V128 H0Z" fill="#C8304A" {W(2.4)}/>
<g fill="#2A0A18"><circle cx="20" cy="92" r="8"/><circle cx="52" cy="92" r="8"/><circle cx="84" cy="92" r="8"/><circle cx="114" cy="92" r="8"/></g>''')

# ---------- БАССЕЙНЫ ----------

I["chaika-pool"] = ("чайка на стартовой тумбе", "раскинула крылья перед прыжком в бассейн на закате", ("#FFE6C8", "#F08A5A"), f'''
<path d="M0 90 H128 V128 H0Z" fill="#3AA8E0"/><path d="M0 104 H128" stroke="#FFD24A" stroke-width="3" stroke-dasharray="8 6"/>
<path d="M0 118 Q32 112 64 118 T128 118" fill="none" stroke="#9AD8FF" stroke-width="2.4"/>
<path d="M44 66 H84 L88 90 H40Z" fill="#fff" {W(3)}/><text x="58" y="85" font-family="Arial" font-size="14" font-weight="bold" fill="#2E6BD8">3</text>
<path d="M58 66 V60 M70 66 V60" stroke="#FFA030" stroke-width="3"/>
<ellipse cx="64" cy="48" rx="16" ry="13" fill="#fff" {W(3)}/>
<path d="M50 46 Q26 24 6 34 Q26 44 50 52Z M78 46 Q102 24 122 34 Q102 44 78 52Z" fill="#fff" {W(2.8)}/>
<path d="M14 32 Q20 34 24 38 M114 32 Q108 34 104 38" fill="none" stroke="#7A8AA0" stroke-width="3"/>
<circle cx="64" cy="30" r="11" fill="#fff" {W(2.8)}/>{eye(60, 28, .4)}{eye(69, 28, .4)}
<path d="M64 33 L74 36 L64 39Z" fill="#FFA030" {W(1.8)}/>''')

I["aquababy-khimki-michurina"] = ("малыш в надувных нарукавниках с плавательной доской", "держится за досочку и бултыхает ножками, брызги", ("#F4FFE0", "#58C0B0"), f'''
<path d="M0 66 Q32 60 64 66 T128 66 V128 H0Z" fill="#4AC0E8"/>
<path d="M0 68 Q32 62 64 68 T128 68" fill="none" stroke="#fff" stroke-width="3"/>
<rect x="38" y="52" width="52" height="22" rx="10" fill="#FFD24A" {W(3)}/>
<circle cx="64" cy="40" r="15" fill="#FFD9B8" {W(3)}/><path d="M50 36 Q50 22 64 22 Q78 22 78 36Z" fill="#7AD04A" {W(2.4)}/>
{eye(58, 42, .45)}{eye(70, 42, .45)}<ellipse cx="64" cy="49" rx="3" ry="2.6" fill="#E8554A"/>{blush(53, 47, .5)}{blush(75, 47, .5)}
<ellipse cx="36" cy="62" rx="9" ry="7" fill="#FF5A7A" {W(2.4)}/><ellipse cx="92" cy="62" rx="9" ry="7" fill="#FF5A7A" {W(2.4)}/>
<path d="M54 84 Q50 98 56 110 M74 84 Q80 98 74 110" stroke="#FFD9B8" stroke-width="8" stroke-linecap="round" fill="none" opacity=".75"/>
<g fill="#fff" {W(1.4)}><circle cx="44" cy="110" r="4"/><circle cx="86" cy="112" r="4"/><circle cx="52" cy="120" r="2.6"/><circle cx="80" cy="102" r="2.6"/></g>''')

I["pool-volna-chertanovo"] = ("большая морская волна-персонаж", "катит гребнем над дорожкой бассейна с поплавками-разделителями", ("#E0E8FF", "#3A3AA8"), f'''
<path d="M0 100 H128 V128 H0Z" fill="#2E88D8"/>
<g fill="#FF5A5A" {W(1.6)}><circle cx="8" cy="100" r="4"/><circle cx="24" cy="100" r="4"/><circle cx="104" cy="100" r="4"/><circle cx="120" cy="100" r="4"/></g>
<g fill="#fff" {W(1.6)}><circle cx="16" cy="100" r="4"/><circle cx="112" cy="100" r="4"/></g>
<path d="M14 100 Q14 40 60 26 Q100 18 112 46 Q100 38 88 44 Q100 50 96 62 Q84 54 72 64 Q70 84 90 100Z" fill="#3AB0F0" {W(3.2)}/>
<path d="M60 26 Q100 18 112 46 Q100 38 88 44" fill="#fff" {W(2.6)}/>
<path d="M30 70 Q40 56 54 52" fill="none" stroke="#9AE0FF" stroke-width="3" stroke-linecap="round"/>
{eye(40, 76, .6)}{eye(58, 76, .6)}{smile(49, 84, 4, .7)}{blush(32, 86, .6)}{blush(66, 86, .6)}
<circle cx="114" cy="30" r="3" fill="#fff"/><circle cx="120" cy="40" r="2" fill="#fff"/>''')

I["kitenok-skhodnenskaya"] = ("голубой китёнок-прыгун «бомбочкой»", "летит с вышки, обхватив хвост ластами, внизу всплеск", ("#FFF0E0", "#F0A060"), f'''
<path d="M88 0 V30 H128" fill="none" stroke="#fff" stroke-width="5"/><rect x="84" y="26" width="44" height="7" fill="#fff" {W(2.2)}/>
<path d="M0 100 H128 V128 H0Z" fill="#3AA8E8"/>
<path d="M24 100 Q20 84 30 80 Q34 92 40 96 Q42 78 54 76 Q54 92 58 98 Q66 82 76 84 Q70 94 74 100Z" fill="#fff" {W(2.4)}/>
<circle cx="56" cy="54" r="26" fill="#5AA8F0" {W(3.2)}/>
<path d="M36 64 Q56 82 76 64 Q70 76 56 78 Q42 76 36 64Z" fill="#DFF2FF"/>
<path d="M74 40 Q90 30 92 18 Q84 24 80 18 Q78 28 74 40Z" fill="#5AA8F0" {W(2.6)}/>
<path d="M36 58 Q30 44 42 40 M78 60 Q84 48 76 42" fill="none" {W(3)}/>
{eye(48, 54, .55)}{eye(64, 54, .55)}<ellipse cx="56" cy="64" rx="3" ry="2.6" fill="{O}"/>
<path d="M56 28 Q54 18 58 12 M56 28 Q62 20 66 18" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

I["mama-ya-plyvu-otradnoe"] = ("мама-выдра с выдрёнком на животе", "плывут на спинке по бассейну, держась за лапки", ("#FFEAF2", "#D85A8A"), f'''
<path d="M0 74 Q32 68 64 74 T128 74 V128 H0Z" fill="#4AB0E8"/>
<path d="M8 96 Q30 90 52 96 M76 112 Q98 106 120 112" fill="none" stroke="#9AD8FF" stroke-width="2.6"/>
<path d="M10 78 Q30 62 64 66 Q100 62 116 78 Q100 90 64 88 Q30 90 10 78Z" fill="#9A6234" {W(3)}/>
<path d="M110 76 Q122 70 124 60" fill="none" stroke="#9A6234" stroke-width="7" stroke-linecap="round"/>
<circle cx="22" cy="66" r="14" fill="#9A6234" {W(3)}/><ellipse cx="16" cy="72" rx="6" ry="4" fill="#E8C49A"/>
{eye(20, 62, .4)}{eye(28, 64, .4)}<ellipse cx="14" cy="70" rx="2" ry="1.6" fill="{O}"/>
<ellipse cx="66" cy="60" rx="18" ry="11" fill="#B47A48" {W(2.6)}/>
<circle cx="52" cy="50" r="10" fill="#B47A48" {W(2.6)}/>{eye(50, 48, .35)}{eye(56, 49, .35)}<ellipse cx="47" cy="54" rx="1.8" ry="1.4" fill="{O}"/>
<path d="M60 62 Q64 70 70 66" fill="none" {W(2)}/>
{sparkle(94, 32, 5)}''')

# ---------- ЕДИНОБОРСТВА ----------

I["ms-sambo70-shabolovka"] = ("двое малышей в красной и синей куртках самбо", "борются в захвате на ковре, позади Шуховская башня", ("#E8F4FF", "#5A7AC8"), f'''
<path d="M96 70 L104 14 L112 70Z" fill="none" stroke="#8090B0" stroke-width="2"/><path d="M98 54 H110 M100 38 H108 M102 24 H106" stroke="#8090B0" stroke-width="2"/>
<path d="M0 98 H128 V128 H0Z" fill="#E8C040" {W(2.4)}/><path d="M0 98 Q64 104 128 98" fill="none" stroke="#C83040" stroke-width="4"/>
<path d="M30 96 L26 112 M50 96 L54 112 M78 96 L74 112 M98 96 L102 112" stroke="#FFD9B8" stroke-width="7" stroke-linecap="round"/>
<path d="M22 60 Q22 50 34 50 H52 L58 66 L54 96 H24Z" fill="#E8304A" {W(2.8)}/>
<path d="M106 60 Q106 50 94 50 H76 L70 66 L74 96 H104Z" fill="#2E5BC8" {W(2.8)}/>
<path d="M24 80 H56 M104 80 H72" stroke="#fff" stroke-width="4"/>
<path d="M50 62 L76 56 M78 64 L52 58" stroke="#FFD9B8" stroke-width="7" stroke-linecap="round"/>
<circle cx="38" cy="38" r="12" fill="#FFD9B8" {W(2.8)}/><circle cx="90" cy="38" r="12" fill="#FFD9B8" {W(2.8)}/>
<path d="M27 34 Q28 24 40 26 Q50 28 50 34Z M101 34 Q100 24 88 26 Q78 28 78 34Z" fill="#5A3A1A" {W(2)}/>
{eye(36, 40, .35)}{eye(44, 40, .35)}{eye(84, 40, .35)}{eye(92, 40, .35)}
<path d="M37 45 Q40 47 43 45 M85 45 Q88 47 91 45" fill="none" {W(1.6)}/>''')

I["school-champions-skandinavia"] = ("белое кимоно дзюдо с жёлтым поясом", "кланяется на татами под северным сиянием", ("#3A6A8A", "#0E1E3A"), f'''
<path d="M0 30 Q30 10 60 28 T128 20" fill="none" stroke="#5AF0A0" stroke-width="7" opacity=".7" stroke-linecap="round"/>
<path d="M0 44 Q36 26 70 40 T128 34" fill="none" stroke="#7AC8FF" stroke-width="5" opacity=".6" stroke-linecap="round"/>
{sparkle(20, 60, 3)}{sparkle(110, 56, 3)}
<path d="M0 104 H128 V128 H0Z" fill="#6AB86A" {W(2.4)}/><path d="M64 104 V128" stroke="#4A984A" stroke-width="2"/>
<g transform="rotate(-10 64 70)">
<path d="M40 52 L54 44 H74 L88 52 L98 74 L86 80 L82 70 V102 H46 V70 L42 80 L30 74Z" fill="#fff" {W(3)}/>
<path d="M54 44 L64 64 L74 44" fill="none" {W(2.6)}/><path d="M64 64 V102" stroke="#D8DCE6" stroke-width="2.4"/>
<rect x="44" y="76" width="40" height="8" fill="#FFD24A" {W(2.4)}/><path d="M60 84 L54 98 M68 84 L74 98" stroke="#FFD24A" stroke-width="5"/>
{eye(56, 58, .45)}{eye(72, 58, .45)}<path d="M60 66 Q64 68 68 66" fill="none" {W(1.8)}/></g>''')

# ---------- КАФЕ ----------

I["cafe-florentini-olimp"] = ("кусочек лазаньи слоями", "несёт олимпийский факел по Олимпийской деревне", ("#FFFAE0", "#A8A030"), f'''
<path d="M0 108 H128 V128 H0Z" fill="#E86040"/><path d="M0 116 H128" stroke="#fff" stroke-width="2"/>
<path d="M92 58 L82 40 H100 Z" fill="#C8A040" {W(2.4)}/><path d="M91 40 Q82 28 90 18 Q92 26 98 24 Q100 34 91 40Z" fill="#FF8A1E" {W(2)}/>
<path d="M90 58 L80 68" {W(3.4)}/>
<rect x="28" y="50" width="56" height="50" rx="6" fill="#F6D27A" {W(3)}/>
<path d="M28 62 H84" stroke="#D83A2A" stroke-width="5"/><path d="M28 76 H84" stroke="#FFF4DC" stroke-width="5"/><path d="M28 90 H84" stroke="#D83A2A" stroke-width="5"/>
<path d="M28 54 Q40 46 50 54 Q62 46 72 54 Q80 48 84 54" fill="#FFC830" {W(2.4)}/>
{eye(46, 70, .5)}{eye(66, 70, .5)}
<path d="M36 100 L32 110 M74 100 L78 110" {W(4)}/>
<path d="M28 74 L18 66" {W(3.4)}/>''')

I["cafe-racha-mytishchi"] = ("круглый имеретинский хачапури", "катится колесом по склону, позади снежная гора", ("#E8F6FF", "#4A8AD0"), f'''
<path d="M10 70 L50 18 L90 70Z" fill="#8AA0C8" {W(2.6)}/><path d="M38 34 L50 18 L62 34 L56 30 L50 36 L44 30Z" fill="#fff" {W(1.8)}/>
<path d="M0 74 L128 100 V128 H0Z" fill="#7AC85A" {W(2.4)}/>
<circle cx="76" cy="72" r="32" fill="#E8A850" {W(3.2)}/><circle cx="76" cy="72" r="23" fill="#FFF0B0"/>
<g fill="#F2C84A"><circle cx="66" cy="62" r="4"/><circle cx="88" cy="66" r="3.4"/><circle cx="72" cy="88" r="3.6"/></g>
{eye(68, 72, .55)}{eye(84, 72, .55)}{smile(76, 80, 3.5, .65)}
<path d="M30 60 l-10 -2 M28 74 l-12 2 M34 88 l-10 6" stroke="#fff" stroke-width="3" stroke-linecap="round"/>''')

I["cafe-buonamici"] = ("брускетта с помидорками черри", "загорает на шезлонге под солнцем Италии", ("#E6FFFA", "#E8C060"), f'''
<circle cx="104" cy="22" r="12" fill="#FFD24A" {W(2.2)}/>
<path d="M0 104 H128 V128 H0Z" fill="#F2DCA0"/>
<path d="M16 104 L30 70 H96 L110 104" fill="none" stroke="#B8642E" stroke-width="4"/>
<path d="M22 84 L40 58 H104 L94 84Z" fill="#3AB0E0" {W(2.6)}/><path d="M28 80 L44 60 M50 84 L62 58 M72 84 L84 58" stroke="#fff" stroke-width="3"/>
<g transform="rotate(-14 66 66)">
<rect x="36" y="58" width="60" height="20" rx="9" fill="#D89A4A" {W(3)}/>
<circle cx="50" cy="58" r="7" fill="#E8304A" {W(2.2)}/><circle cx="66" cy="56" r="7" fill="#E8304A" {W(2.2)}/><circle cx="82" cy="58" r="7" fill="#E8304A" {W(2.2)}/>
<path d="M58 50 q4 -4 8 0 M74 50 q4 -4 8 0" stroke="#3E9A3E" stroke-width="2.4" fill="none"/>
<rect x="52" y="64" width="26" height="7" rx="3" fill="{O}"/><path d="M52 67 L44 64 M78 67 L86 64" {W(2)}/>
{smile(65, 74, 3, .55)}</g>''')

I["cafe-bb-grill-semenovskaya"] = ("две сосиски-гриль с полосками от решётки", "качаются на детских качелях-балансире", ("#FFEEDD", "#B8502A"), f'''
<path d="M0 108 H128 V128 H0Z" fill="#6ACF7A"/>
<path d="M54 108 L64 84 L74 108Z" fill="#FFD24A" {W(2.6)}/>
<g transform="rotate(-12 64 80)"><rect x="6" y="78" width="116" height="9" rx="4" fill="#E8304A" {W(2.6)}/>
<rect x="8" y="56" width="50" height="20" rx="10" fill="#D86A3A" {W(3)}/>
<path d="M18 60 L24 72 M30 60 L36 72 M42 60 L48 72" stroke="#8A3A1A" stroke-width="3" stroke-linecap="round"/>
{eye(26, 66, .4)}{eye(38, 66, .4)}
<rect x="70" y="56" width="50" height="20" rx="10" fill="#E07A42" {W(3)}/>
<path d="M80 60 L86 72 M92 60 L98 72 M104 60 L110 72" stroke="#8A3A1A" stroke-width="3" stroke-linecap="round"/>
{eye(88, 66, .4)}{eye(100, 66, .4)}</g>
<path d="M30 36 Q36 28 32 20 M46 40 Q52 32 48 24 M86 30 Q92 22 88 14" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

I["cafe-viet-nametkina"] = ("свежий спринг-ролл с креветкой в рисовой бумаге", "прячется от дождя под вьетнамской конической шляпой", ("#E4FFF0", "#2E8A6A"), f'''
<path d="M18 20 l-4 8 M40 12 l-4 8 M98 14 l-4 8 M114 30 l-4 8 M28 44 l-4 8 M106 50 l-4 8" stroke="#9AD0E8" stroke-width="2.6" stroke-linecap="round"/>
<path d="M12 60 L64 24 L116 60 Q64 70 12 60Z" fill="#F2D88A" {W(3)}/>
<path d="M30 56 L64 30 M48 60 L64 30 M80 60 L64 30 M98 56 L64 30" stroke="#C8A850" stroke-width="1.8"/>
<rect x="30" y="66" width="68" height="40" rx="20" fill="#F4FAF0" fill-opacity=".9" {W(3)}/>
<path d="M38 74 Q48 70 54 78 Q48 86 38 82Z" fill="#FF8A6A" {W(1.8)}/><path d="M80 72 Q90 76 88 88" fill="none" stroke="#6CC24A" stroke-width="4" stroke-linecap="round"/>
{eye(58, 84, .5)}{eye(72, 84, .5)}{smile(65, 91, 3, .55)}
<path d="M24 110 Q64 120 104 110" fill="none" stroke="#2E8A6A" stroke-width="2.4"/>''')

I["cafe-ptitsy-i-pchely"] = ("медовик-торт слоями", "к нему подлетает пчёлка и садится, как на цветок", ("#ECFFF6", "#6AC8A0"), f'''
<ellipse cx="60" cy="108" rx="48" ry="8" fill="#fff" {W(2.6)}/>
<path d="M18 62 H102 V102 H18Z" fill="#E8B060" {W(3)}/>
<path d="M18 74 H102 M18 88 H102" stroke="#FFF2D0" stroke-width="5"/>
<path d="M18 62 Q30 54 42 60 Q54 52 66 60 Q78 52 90 60 Q98 56 102 62Z" fill="#FFF2D0" {W(2.6)}/>
{eye(48, 80, .55)}{eye(72, 80, .55)}{smile(60, 87, 3.5, .65)}{blush(38, 88, .6)}{blush(82, 88, .6)}
<g transform="rotate(10 96 34)">
<ellipse cx="96" cy="36" rx="12" ry="9" fill="#FFD24A" {W(2.6)}/><path d="M92 28 V44 M100 28 V44" stroke="{O}" stroke-width="3"/>
<ellipse cx="92" cy="24" rx="7" ry="5" fill="#fff" fill-opacity=".85" {W(1.8)}/><ellipse cx="102" cy="24" rx="7" ry="5" fill="#fff" fill-opacity=".85" {W(1.8)}/>
<circle cx="87" cy="36" r="1.6" fill="{O}"/></g>
<path d="M84 48 Q72 56 66 52" fill="none" stroke="#fff" stroke-width="2.2" stroke-dasharray="3 3"/>''')


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
