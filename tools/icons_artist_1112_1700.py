"""Робот «художник», 12.11 ~17:00 UTC.
check_unique.py: 0 повторов по точному тексту и картинке. Но в реестре остались серии одного героя у мест, которые
сейчас НА КАРТЕ (проверка их не ловит — разные шапки на том же предмете): «белый/чёрный шахматный конь/слон/ферзь…»,
«треугольный кусок пиццы…», «круглая пицца…», «баскетбольный мяч-…». Из каждой серии оставлен один
(chess-hod-konem-chernogolovka, cafe-ilpatio-gorod-lefortovo, cafe-dodo-khoroshevsky-3a, pbk-cska-solntsevo),
остальные 30 придуманы и нарисованы заново, каждая отдельно — свой герой, своя сцена, своя палитра.
Запуск из корня: python3 tools/icons_artist_1112_1700.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT
from icons_artist_1112_1400 import limb, basketball


def knight(tx, ty, k, fill, mane=None, extra=""):
    """силуэт шахматного коня (смотрит влево), точка (tx,ty) — середина, высота ≈ 46·k"""
    d = ("M-11 22 L13 22 L11 13 Q9 6 9 2 Q15 -6 11 -15 Q6 -22 -2 -21 L-4 -26 L-8 -19 "
         "Q-15 -14 -18 -3 Q-19 1 -15 3 L-11 2 Q-6 0 -4 2 Q-4 6 -8 10 Q-12 15 -11 22 Z")
    out = f'<path d="{d}" transform="translate({tx} {ty}) scale({k})" fill="{fill}" stroke="{O}" stroke-width="{3/k:.2f}" stroke-linejoin="round" {extra}/>'
    if mane:
        out += (f'<path d="M-2 -21 Q8 -18 10 -10 Q12 -4 8 2" transform="translate({tx} {ty}) scale({k})" fill="none" '
                f'stroke="{mane}" stroke-width="{5/k:.2f}" stroke-linecap="round"/>')
    return out


def pawn(cx, by, k, fill):
    """пешка: низ в (cx, by), высота ≈ 30·k"""
    return (f'<path d="M{cx-10*k:.1f} {by} H{cx+10*k:.1f} Q{cx+10*k:.1f} {by-5*k:.1f} {cx+5*k:.1f} {by-7*k:.1f} '
            f'Q{cx+3*k:.1f} {by-14*k:.1f} {cx+5*k:.1f} {by-18*k:.1f} H{cx-5*k:.1f} Q{cx-3*k:.1f} {by-14*k:.1f} {cx-5*k:.1f} {by-7*k:.1f} '
            f'Q{cx-10*k:.1f} {by-5*k:.1f} {cx-10*k:.1f} {by} Z" fill="{fill}" {W(2.6)}/>'
            f'<circle cx="{cx}" cy="{by-23*k:.1f}" r="{6.5*k:.1f}" fill="{fill}" {W(2.6)}/>')


def checker(x, y, n, m, c, a="#FFFFFF", b="#3B3355"):
    out = ""
    for i in range(n):
        for j in range(m):
            out += f'<rect x="{x+i*c}" y="{y+j*c}" width="{c}" height="{c}" fill="{a if (i+j)%2==0 else b}"/>'
    return out + f'<rect x="{x}" y="{y}" width="{n*c}" height="{m*c}" fill="none" {W(2.6)}/>'


def slice_tri(x1, y1, x2, y2, x3, y3, crust="#E8A54B", cheese="#FFD25C"):
    return (f'<path d="M{x1} {y1} L{x2} {y2} L{x3} {y3} Z" fill="{cheese}" {W(3)}/>'
            f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="{crust}" stroke-width="7" stroke-linecap="round"/>'
            f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" {W(2)}/>')


I = {}

# ---------- ШАХМАТЫ ----------

# «Чемпионы», Реутов (малыши с 3 лет, игровая форма): конь-качалка
I["champions-chess-oktyabrya"] = (
    "деревянная лошадка-качалка в форме шахматного коня с красным седлом",
    "раскачивается на клетчатом детском коврике, от полозьев разлетаются дуги движения",
    ("#FFF1DE", "#EFA35C"), f'''
<path d="M10 112 L118 112 L104 124 L24 124 Z" fill="#FFFFFF" {W(2)}/>
<path d="M24 112 h12 l-3 12 h-12z M48 112 h12 l-1 12 h-12z M72 112 h12 l1 12 h-12z M96 112 h12 l3 12 h-12z" fill="#3B3355"/>
<path d="M18 98 Q64 122 110 98" fill="none" stroke="{O}" stroke-width="11" stroke-linecap="round"/>
<path d="M18 98 Q64 122 110 98" fill="none" stroke="#B5652B" stroke-width="7" stroke-linecap="round"/>
<path d="M44 106 L48 92 M84 106 L80 92" fill="none" stroke="{O}" stroke-width="6" stroke-linecap="round"/>
<path d="M44 106 L48 92 M84 106 L80 92" fill="none" stroke="#B5652B" stroke-width="3" stroke-linecap="round"/>
{knight(64, 56, 1.75, "#F1C27D", mane="#8A4A1E")}
<path d="M74 66 Q86 62 88 74 Q80 78 72 76 Z" fill="#E2423C" {W(2.4)}/>
{eye(48, 42, .75)}{blush(42, 52, .9)}
<path d="M38 56 Q34 60 38 62" fill="none" {W(2.2)}/>
<path d="M8 70 Q4 80 8 90 M120 70 Q124 80 120 90" fill="none" stroke="#FFFFFF" stroke-width="3.4" stroke-linecap="round"/>''')

# «Шахматное королевство» в Царицыне: дворец, у которого башни — ладьи
I["chess-korolevstvo-tsaritsyno"] = (
    "красно-белый царицынский дворец с двумя башнями-ладьями и шахматным флагом",
    "отражается в пруду, над средней аркой развевается клетчатое знамя королевства",
    ("#EAF6FF", "#7FB6E6"), f'''
<rect x="0" y="100" width="128" height="28" fill="#5FA8D9"/>
<path d="M14 108 Q30 104 46 108 M70 112 Q90 108 108 112" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"/>
<rect x="40" y="58" width="48" height="42" fill="#C8463C" {W(3)}/>
<path d="M58 100 V82 Q64 74 70 82 V100 Z" fill="#FFFFFF" {W(2.4)}/>
<path d="M46 66 h6 v8 h-6z M76 66 h6 v8 h-6z" fill="#FFFFFF" {W(2)}/>
<path d="M18 100 V54 H42 V100 Z" fill="#D9564A" {W(3)}/>
<path d="M14 54 V42 H20 V48 H26 V42 H34 V48 H40 V42 H46 V54 Z" fill="#FFFFFF" {W(2.8)}/>
<path d="M86 100 V54 H110 V100 Z" fill="#D9564A" {W(3)}/>
<path d="M82 54 V42 H88 V48 H94 V42 H102 V48 H108 V42 H114 V54 Z" fill="#FFFFFF" {W(2.8)}/>
<path d="M24 70 h12 M24 82 h12 M92 70 h12 M92 82 h12" fill="none" stroke="#FFFFFF" stroke-width="3"/>
<path d="M64 58 V22" fill="none" {W(3)}/>
{checker(64, 22, 4, 3, 6, "#FFFFFF", "#3B3355")}
{eye(26, 62, .5)}{eye(36, 62, .5)}{eye(94, 62, .5)}{eye(104, 62, .5)}
{smile(31, 89, 3, .6)}{smile(98, 89, 3, .6)}''')

# Шахматная школа №1 в Апрелевке (город пластинок, ФОК «Мелодия»)
I["chess1-aprelevka-melodiya"] = (
    "чёрная виниловая пластинка, у которой вместо наклейки — шахматная доска",
    "кружится на проигрывателе, а из-под иглы вылетают ноты и маленькие белые пешки",
    ("#F3E6FF", "#9C6FD8"), f'''
<rect x="12" y="66" width="104" height="52" rx="8" fill="#C98A52" {W(3)}/>
<circle cx="58" cy="72" r="40" fill="#24202E" {W(3)}/>
<circle cx="58" cy="72" r="31" fill="none" stroke="#4A4458" stroke-width="2"/>
<circle cx="58" cy="72" r="23" fill="none" stroke="#4A4458" stroke-width="2"/>
{checker(46, 60, 4, 4, 6, "#FFFFFF", "#E2423C")}
<path d="M110 54 L104 92 L84 100" fill="none" stroke="{O}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M110 54 L104 92 L84 100" fill="none" stroke="#D8DCE6" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="110" cy="54" r="6" fill="#D8DCE6" {W(2.6)}/>
{pawn(96, 40, .7, "#FFFFFF")}
<path d="M70 26 V12 L80 9 V22" fill="none" {W(3)}/><ellipse cx="66" cy="26" rx="5" ry="4" fill="#3B3355"/><ellipse cx="76" cy="23" rx="5" ry="4" fill="#3B3355"/>
<path d="M30 22 V10" fill="none" {W(3)}/><ellipse cx="26" cy="22" rx="5" ry="4" fill="#3B3355"/>
{sparkle(46, 18, 4)}''')

# СДЦ «Люблино» — шахматы: уличные гигантские шахматы у пруда
I["sdts-lyublino-chess"] = (
    "мальчик в оранжевой толстовке рядом с напольным шахматным ферзём ростом с него",
    "двумя руками переставляет огромную фигуру по уличной доске у пруда",
    ("#E3FFE9", "#59B97A"), f'''
<ellipse cx="22" cy="80" rx="30" ry="8" fill="#8FD0F0" {W(2)}/><path d="M0 92 L128 84 V128 H0 Z" fill="#78C46A"/>
<path d="M20 120 L36 92 H104 L116 120 Z" fill="#FFFFFF" {W(2.6)}/>
<path d="M36 92 h17 l-4 9 h-17z M70 92 h17 l2 9 h-17z M28 101 h17 l-4 10 h-17z M62 101 h18 l1 10 h-18z M96 101 h17 l3 10 h-17z M41 111 h18 l-2 9 h-18z M77 111 h18 l1 9 h-18z" fill="#3B3355"/>
<path d="M30 92 h66" fill="none" stroke="#3B3355" stroke-width="0"/>
<path d="M76 100 H104 Q104 92 98 90 Q92 74 96 60 H84 Q88 74 82 90 Q76 92 76 100 Z" fill="#F7F3EA" {W(3)}/>
<rect x="82" y="54" width="16" height="7" rx="2" fill="#F7F3EA" {W(2.6)}/>
<path d="M82 54 L80 40 L86 46 L90 36 L94 46 L100 40 L98 54 Z" fill="#F7F3EA" {W(2.6)}/>
<circle cx="90" cy="32" r="4" fill="#F7F3EA" {W(2.4)}/>
{limb("M42 96 L40 112", "#2F5FB3", 7)}{limb("M52 96 L56 112", "#2F5FB3", 7)}
<path d="M34 112 h10 v4 h-12z M52 112 h10 v4 h-12z" fill="#3B3355"/>
<path d="M36 70 H58 L56 98 H38 Z" fill="#F08A2E" {W(3)}/>
{limb("M56 74 Q70 68 82 66", "#F6D2B0", 5)}{limb("M56 84 Q70 82 80 80", "#F6D2B0", 5)}
<circle cx="47" cy="56" r="12" fill="#F6D2B0" {W(2.8)}/>
<path d="M35 54 Q36 42 47 42 Q58 42 59 54 Q54 47 47 48 Q40 47 35 54 Z" fill="#7A4A26" {W(2)}/>
{eye(43, 57, .5)}{eye(52, 57, .5)}{blush(40, 62, .6)}{smile(47.5, 62, 3, .6)}
''')

# «Чемпионы», Носовихинское шоссе: медаль чемпиона
I["champions-chess-nosovikhinskoe"] = (
    "большая золотая медаль с выбитым профилем шахматного коня",
    "висит на красно-синей ленте и сияет, медаль подмигивает",
    ("#FFFCE8", "#E9C85A"), f'''
<path d="M38 4 L58 58 H72 L52 4 Z" fill="#2F6FD0" {W(2.8)}/>
<path d="M90 4 L70 58 H56 L76 4 Z" fill="#E2423C" {W(2.8)}/>
<circle cx="64" cy="84" r="34" fill="#F5C342" {W(3.2)}/>
<circle cx="64" cy="84" r="26" fill="#FFD85E" stroke="#D49A1E" stroke-width="3"/>
{knight(66, 85, .82, "#D49A1E")}
<path d="M54 74 Q56 72 58 74" fill="none" {W(2)}/>
{sparkle(104, 66, 6)}{sparkle(24, 100, 5)}{sparkle(98, 112, 4)}''')

# СК «Ориента» — шахматы: флюгер-конь на крыше
I["ms-orienta-chess"] = (
    "жестяной флюгер в виде чёрного шахматного коня со стрелкой",
    "крутится на шпиле крыши спорткомплекса под ветром, рядом буквы сторон света",
    ("#E8F3FF", "#6E8FD6"), f'''
<path d="M10 128 L64 92 L118 128 Z" fill="#B54A3A" {W(3)}/>
<path d="M64 92 V30" fill="none" stroke="{O}" stroke-width="6"/><path d="M64 92 V30" fill="none" stroke="#9AA0AA" stroke-width="3"/>
<path d="M28 60 H100" fill="none" stroke="{O}" stroke-width="6" stroke-linecap="round"/>
<path d="M28 60 H100" fill="none" stroke="#9AA0AA" stroke-width="3" stroke-linecap="round"/>
<path d="M18 60 L30 52 V68 Z" fill="#E2423C" {W(2.4)}/>
<path d="M110 54 L100 60 L110 66 L106 60 Z" fill="#9AA0AA" {W(2.2)}/>
<text x="16" y="88" font-family="Arial" font-weight="bold" font-size="12" fill="#FFFFFF" stroke="{O}" stroke-width=".8">З</text>
<text x="104" y="88" font-family="Arial" font-weight="bold" font-size="12" fill="#FFFFFF" stroke="{O}" stroke-width=".8">В</text>
{knight(64, 34, 1.0, "#2A2638")}
<circle cx="59" cy="27" r="2.4" fill="#FFFFFF"/>
<path d="M90 20 Q102 16 112 22 M86 32 Q100 28 116 34" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>''')

# Kurchatov Chess в «Бихайве» (улей): шмель в шахматную клетку
I["kurchatov-chess-pavshinsky"] = (
    "пухлый шмель, у которого вместо полосок — чёрно-белая шахматная клетка",
    "несёт в лапках маленькую золотую корону над медовыми сотами",
    ("#FFF6D6", "#F2B53A"), f'''
<path d="M0 96 l12 -7 14 7 v16 l-14 7 -14 -7z M26 96 l14 -7 14 7 v16 l-14 7 -14 -7z M52 96 l14 -7 14 7 v16 l-14 7 -14 -7z M78 96 l14 -7 14 7 v16 l-14 7 -14 -7z M104 96 l14 -7 14 7 v16 l-14 7 -14 -7z" fill="#F7B92E" {W(2.4)}/>
<ellipse cx="44" cy="40" rx="15" ry="20" transform="rotate(-25 44 40)" fill="#DDF3FF" fill-opacity=".9" {W(2.6)}/>
<ellipse cx="80" cy="36" rx="15" ry="20" transform="rotate(20 80 36)" fill="#DDF3FF" fill-opacity=".9" {W(2.6)}/>
<clipPath id="bee"><ellipse cx="64" cy="64" rx="30" ry="24"/></clipPath>
<ellipse cx="64" cy="64" rx="30" ry="24" fill="#FFFFFF"/>
<g clip-path="url(#bee)">{checker(30, 40, 7, 5, 10, "#FFFFFF", "#2A2638").replace(f'<rect x="30" y="40" width="70" height="50" fill="none" {W(2.6)}/>', "")}</g>
<ellipse cx="64" cy="64" rx="30" ry="24" fill="none" {W(3)}/>
<path d="M94 64 L102 66 L94 70" fill="#2A2638" {W(2)}/>
<circle cx="38" cy="62" r="15" fill="#F7B92E" {W(3)}/>
{eye(33, 60, .6)}{eye(42, 60, .6)}{smile(37, 67, 3, .6)}
<path d="M32 48 Q28 38 22 36 M42 48 Q44 38 50 34" fill="none" {W(2.4)}/><circle cx="22" cy="36" r="2.6" fill="#3B3355"/><circle cx="50" cy="34" r="2.6" fill="#3B3355"/>
<path d="M50 88 L50 80 L56 84 L60 77 L64 84 L70 80 L70 88 Z" fill="#FFD23F" {W(2.4)}/>
{limb("M48 78 L52 86", "#2A2638", 3)}{limb("M66 82 L66 86", "#2A2638", 3)}''')

# Дворец спорта «Некрасовка»: шахматы + настольный теннис
I["ms-nekrasovka-sections"] = (
    "зелёный теннисный стол, расчерченный шахматной клеткой",
    "над сеткой летят оранжевый шарик и маленькая пешка, две ракетки ждут по краям",
    ("#E6FFF8", "#3FA88E"), f'''
<path d="M10 78 L34 58 H94 L118 78 Z" fill="#2E8B57" {W(3)}/>
<path d="M22 68 h10 l-3 4 h-10z M42 63 h10 l-2 5 h-10z M66 63 h10 l1 5 h-10z M90 68 h10 l4 4 h-10z M34 74 h10 l-3 4 h-11z M56 68 h11 v4 h-11z M80 74 h11 l2 4 h-11z" fill="#1E5E3A"/>
<path d="M10 78 V84 H118 V78" fill="#256E46" {W(2.6)}/>
<path d="M22 84 V112 M106 84 V112 M40 84 V104 M88 84 V104" fill="none" {W(3)}/>
<path d="M64 52 V80" fill="none" {W(3)}/><path d="M60 54 H68 V78 H60 Z" fill="#FFFFFF" fill-opacity=".7" {W(1.6)}/>
<circle cx="82" cy="30" r="7" fill="#FF8A2E" {W(2.6)}/>
{pawn(44, 46, .62, "#FFFFFF")}
<path d="M90 30 Q100 28 104 34" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-dasharray="3 4"/>
<ellipse cx="14" cy="50" rx="9" ry="10" fill="#E2423C" {W(2.6)}/><path d="M14 60 V70" fill="none" stroke="{O}" stroke-width="6" stroke-linecap="round"/><path d="M14 60 V70" fill="none" stroke="#C98A52" stroke-width="3" stroke-linecap="round"/>
<ellipse cx="114" cy="50" rx="9" ry="10" fill="#2A2638" {W(2.6)}/><path d="M114 60 V70" fill="none" stroke="{O}" stroke-width="6" stroke-linecap="round"/><path d="M114 60 V70" fill="none" stroke="#C98A52" stroke-width="3" stroke-linecap="round"/>
{eye(78, 30, .4)}{eye(85, 30, .4)}''')

# Шахматный клуб «Прорыв»: росток-пешка пробивает асфальт
I["chess-proryv-yasenevo"] = (
    "зелёный росток с бутоном в форме шахматной пешки",
    "пробился сквозь трещину в сером асфальте и тянется к солнцу",
    ("#FFF8E8", "#F6C08A"), f'''
<circle cx="104" cy="24" r="13" fill="#FFD23F" {W(2.6)}/>
<path d="M0 92 H50 L56 100 L62 90 L68 102 L74 92 H128 V128 H0 Z" fill="#8E929C" {W(3)}/>
<path d="M14 106 l6 3 M96 110 l8 -2 M34 118 h6 M108 120 l4 3" fill="none" stroke="#6E727C" stroke-width="2.4" stroke-linecap="round"/>
<path d="M50 92 L60 84 L66 92 L72 86 L78 92" fill="#6E727C" {W(2.2)}/>
<path d="M63 96 Q60 80 64 62" fill="none" stroke="{O}" stroke-width="8" stroke-linecap="round"/>
<path d="M63 96 Q60 80 64 62" fill="none" stroke="#4CAF50" stroke-width="5" stroke-linecap="round"/>
<path d="M62 82 Q44 80 38 66 Q54 64 62 78 Z" fill="#6BCB5A" {W(2.6)}/>
<path d="M64 76 Q82 74 90 60 Q72 58 64 72 Z" fill="#6BCB5A" {W(2.6)}/>
{pawn(64, 64, 1.05, "#FFFFFF")}
{eye(60, 39, .5)}{eye(68, 39, .5)}{smile(64, 44, 3, .6)}
<path d="M50 32 L44 28 M78 32 L84 28 M64 20 V14" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>''')

# «Шахматное королевство» у Нагатинской набережной (Коломенская): речной трамвайчик
I["chess-korolevstvo-kolomenskaya"] = (
    "речной трамвайчик с бортом в чёрно-белую шахматную клетку и короной на рубке",
    "плывёт по Москве-реке мимо зелёного берега, за кормой пенный след",
    ("#E6F7FF", "#4A9FD6"), f'''
<path d="M0 46 Q30 40 60 46 L60 56 H0 Z" fill="#6BBF5A" {W(2)}/>
<rect x="0" y="82" width="128" height="46" fill="#3E8CC8"/>
<path d="M14 84 L114 84 L104 104 H26 Z" fill="#FFFFFF" {W(3)}/>
<g>{"".join(f'<rect x="{26+i*8}" y="{88 + (i%2)*6}" width="8" height="6" fill="#2A2638"/>' for i in range(10))}</g>
<path d="M14 84 L114 84 L104 104 H26 Z" fill="none" {W(3)}/>
<rect x="38" y="62" width="50" height="22" rx="4" fill="#F4F1E6" {W(3)}/>
<rect x="44" y="67" width="10" height="9" rx="2" fill="#9AD3F0" {W(2)}/><rect x="58" y="67" width="10" height="9" rx="2" fill="#9AD3F0" {W(2)}/><rect x="72" y="67" width="10" height="9" rx="2" fill="#9AD3F0" {W(2)}/>
<path d="M50 62 L48 48 L56 54 L63 42 L70 54 L78 48 L76 62 Z" fill="#FFD23F" {W(2.6)}/>
<path d="M2 106 Q12 100 22 106 M108 110 Q118 104 126 110 M40 116 Q52 112 64 116" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>
{eye(98, 92, .45)}{eye(106, 92, .45)}''')

# ---------- ПИЦЦЕРИИ И КАФЕ ----------

# Додо Пицца, Наро-Фоминск: детский мастер-класс — тесто как парашют
I["cafe-dodo-naro-fominsk"] = (
    "малышка в бумажном поварском колпачке",
    "подбрасывает над головой большой круг пиццы-теста, и он раздувается, как парашют",
    ("#FFEDE6", "#F07A5A"), f'''
<path d="M18 50 Q64 4 110 50 Q64 40 18 50 Z" fill="#F6DFA8" {W(3)}/>
<circle cx="40" cy="38" r="3" fill="#E2423C"/><circle cx="64" cy="26" r="3.4" fill="#E2423C"/><circle cx="88" cy="38" r="3" fill="#E2423C"/>
<path d="M30 46 L52 76 M98 46 L76 76" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="3 3"/>
{limb("M52 92 Q46 80 52 74", "#F6D2B0", 5)}{limb("M76 92 Q82 80 76 74", "#F6D2B0", 5)}
<path d="M48 90 H80 L84 124 H44 Z" fill="#FFFFFF" {W(3)}/>
<path d="M56 108 h16" fill="none" stroke="#F07A5A" stroke-width="3" stroke-linecap="round"/>
<circle cx="64" cy="82" r="12" fill="#F6D2B0" {W(2.8)}/>
<path d="M53 72 Q50 60 58 60 Q60 54 66 56 Q74 54 76 62 Q80 66 75 72 Z" fill="#FFFFFF" {W(2.6)}/>
<path d="M53 72 H75" fill="none" {W(2.4)}/>
<path d="M51 80 Q48 86 52 90 M77 80 Q80 86 76 90" fill="none" stroke="#E0A040" stroke-width="4" stroke-linecap="round"/>
{eye(59, 82, .5)}{eye(69, 82, .5)}{blush(56, 88, .5)}{blush(72, 88, .5)}
<ellipse cx="64" cy="89" rx="3" ry="2.4" fill="#C2405A"/>
{sparkle(108, 80, 5)}{sparkle(20, 84, 4)}''')

# Додо Пицца, Голицыно: додстер съезжает с горки в детской
I["cafe-dodo-golitsyno"] = (
    "румяный додстер — свёрнутая трубочкой лепёшка с начинкой и мордашкой",
    "с восторгом съезжает с жёлтой детской горки прямо в сухой бассейн с шариками",
    ("#E9F5FF", "#5DA9E9"), f'''
<rect x="62" y="96" width="62" height="30" rx="6" fill="#FFFFFF" {W(3)}/>
<circle cx="72" cy="98" r="6" fill="#FF6B6B" {W(2)}/><circle cx="85" cy="96" r="6" fill="#FFD23F" {W(2)}/><circle cx="98" cy="98" r="6" fill="#5DCB6A" {W(2)}/>
<circle cx="111" cy="96" r="6" fill="#7B6BEA" {W(2)}/><circle cx="78" cy="88" r="5" fill="#5DA9E9" {W(2)}/>
<path d="M8 40 H26 L74 92 H56 Z" fill="#FFC93C" {W(3)}/>
<path d="M14 40 V120 M26 40 V120" fill="none" stroke="{O}" stroke-width="7"/><path d="M14 40 V120 M26 40 V120" fill="none" stroke="#FF8A3D" stroke-width="4"/>
<path d="M14 60 H26 M14 80 H26 M14 100 H26" fill="none" {W(3)}/>
<g transform="rotate(42 46 62)">
<rect x="20" y="50" width="52" height="24" rx="12" fill="#E8B062" {W(3)}/>
<ellipse cx="72" cy="62" rx="6" ry="12" fill="#F7D79A" {W(2.6)}/>
<path d="M70 56 q4 3 0 6 q4 3 0 6" fill="none" stroke="#5DCB6A" stroke-width="2.4"/>
<path d="M30 52 L34 72 M44 52 L48 72 M58 52 L62 72" fill="none" stroke="#C98A3E" stroke-width="2.4"/>
</g>
{eye(36, 56, .55)}{eye(45, 64, .55)}
<ellipse cx="36" cy="68" rx="3" ry="3.6" fill="#C2405A"/>
<path d="M90 30 L96 24 M100 40 L108 36 M94 48 L104 50" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>''')

# Yug на Большой Новодмитровской: пицца, рыба — рыбка с гриля ныряет в южное море
I["cafe-yug-novodmitrovskaya"] = (
    "запечённая рыбка с полосками гриля и долькой лимона на боку",
    "радостно ныряет с белой тарелки в бирюзовую южную волну под жарким солнцем",
    ("#FFF3C4", "#FF9F45"), f'''
<circle cx="100" cy="28" r="14" fill="#FFE14D" {W(2.6)}/>
<path d="M100 8 V2 M118 18 l5 -3 M120 34 l6 2" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>
<path d="M0 94 Q16 84 32 94 T64 94 T96 94 T128 94 V128 H0 Z" fill="#2EC4B6" {W(3)}/>
<path d="M10 108 Q20 104 30 108 M70 112 Q82 108 94 112" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>
<ellipse cx="34" cy="76" rx="26" ry="7" fill="#FFFFFF" {W(3)}/><ellipse cx="34" cy="75" rx="18" ry="4" fill="#EEF2F6"/>
<g transform="rotate(38 74 62)">
<path d="M44 62 Q60 42 86 54 Q96 58 100 62 Q96 66 86 70 Q60 82 44 62 Z" fill="#E9A05A" {W(3)}/>
<path d="M100 62 L112 52 L110 62 L112 72 Z" fill="#E9A05A" {W(2.8)}/>
<path d="M58 54 L54 70 M68 52 L64 72 M78 54 L74 70" fill="none" stroke="#8A4A1E" stroke-width="3" stroke-linecap="round"/>
<path d="M84 58 A6 6 0 0 1 84 70 Z" fill="#FFE14D" {W(2)}/>
</g>
{eye(58, 44, .55)}{smile(58, 51, 3, .6)}
<path d="M88 90 Q92 84 96 90 M100 92 Q104 86 108 92" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>''')

# Додо Пицца, Боровское ш.: небольшая игровая — мальчик нырнул в шарики
I["cafe-dodo-borovskoe-30a"] = (
    "мальчик в полосатой красно-белой футболке, нырнувший в сухой бассейн вниз головой",
    "из разноцветных шариков торчат только его ноги в синих носках, шарики разлетаются",
    ("#F1FFE8", "#8FD16A"), f'''
<path d="M10 78 H118 V122 H10 Z" fill="#FFFFFF" fill-opacity=".55" {W(3)}/>
<circle cx="22" cy="84" r="8" fill="#FF6B6B" {W(2.2)}/><circle cx="38" cy="82" r="8" fill="#5DA9E9" {W(2.2)}/><circle cx="90" cy="82" r="8" fill="#FFD23F" {W(2.2)}/>
<circle cx="106" cy="84" r="8" fill="#B07BEA" {W(2.2)}/><circle cx="30" cy="96" r="8" fill="#FFD23F" {W(2.2)}/><circle cx="98" cy="96" r="8" fill="#FF6B6B" {W(2.2)}/>
<circle cx="20" cy="108" r="8" fill="#5DCB6A" {W(2.2)}/><circle cx="108" cy="108" r="8" fill="#5DA9E9" {W(2.2)}/><circle cx="44" cy="110" r="8" fill="#B07BEA" {W(2.2)}/>
<circle cx="84" cy="110" r="8" fill="#5DCB6A" {W(2.2)}/><circle cx="64" cy="114" r="8" fill="#FF6B6B" {W(2.2)}/>
<path d="M50 84 Q50 70 64 70 Q78 70 78 84 Z" fill="#FFFFFF" {W(3)}/>
<path d="M51 78 H77 M53 73 H75" fill="none" stroke="#E2423C" stroke-width="3"/>
{limb("M58 72 Q54 50 46 30", "#2F5FB3", 9)}{limb("M70 72 Q76 50 86 32", "#2F5FB3", 9)}
<path d="M38 30 Q40 20 50 24 L52 32 Z" fill="#3E7BE0" {W(2.4)}/>
<path d="M80 34 Q80 22 90 24 L94 32 Z" fill="#3E7BE0" {W(2.4)}/>
<circle cx="30" cy="54" r="6" fill="#FF6B6B" {W(2)}/><circle cx="100" cy="56" r="6" fill="#FFD23F" {W(2)}/><circle cx="20" cy="70" r="5" fill="#5DA9E9" {W(2)}/>
<path d="M24 46 l-4 -4 M106 46 l4 -4" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>''')

# IL Патио в ТЦ «Щука»: щука ловит макаронину
I["cafe-ilpatio-shchuka"] = (
    "зелёная пятнистая щука с зубастой, но доброй улыбкой",
    "выпрыгивает из воды и ловит ртом длинную макаронину, свисающую с вилки над рекой",
    ("#EFFFF6", "#64C2B0"), f'''
<rect x="0" y="96" width="128" height="32" fill="#3E9BD1"/>
<path d="M6 100 Q18 94 30 100 M96 104 Q108 98 120 104" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>
<path d="M96 6 L88 34" fill="none" stroke="{O}" stroke-width="7" stroke-linecap="round"/><path d="M96 6 L88 34" fill="none" stroke="#C8CDD6" stroke-width="4" stroke-linecap="round"/>
<path d="M82 34 L86 44 M88 34 L90 44 M94 34 L94 44 M80 34 H96" fill="none" {W(2.4)}/>
<path d="M88 44 Q86 58 74 60 Q62 62 56 50" fill="none" stroke="{O}" stroke-width="6" stroke-linecap="round"/>
<path d="M88 44 Q86 58 74 60 Q62 62 56 50" fill="none" stroke="#F7D46A" stroke-width="3.4" stroke-linecap="round"/>
<g transform="rotate(-40 52 80)">
<path d="M14 80 Q30 64 64 68 Q80 70 88 80 Q80 90 64 92 Q30 96 14 80 Z" fill="#7E9F5A" {W(3)}/><path d="M22 84 Q40 92 64 90 Q78 88 86 82 Q70 86 60 86 Q40 86 22 84 Z" fill="#F2F0D8"/><path d="M50 90 Q46 100 38 100 Q42 92 46 88 Z" fill="#6F8F4C" {W(2)}/>
<path d="M14 80 L2 70 L4 80 L2 90 Z" fill="#5FA65A" {W(2.8)}/>
<path d="M36 72 l3 2 M46 70 l3 2 M40 86 l3 2 M52 88 l3 2" fill="none" stroke="#2E6B3A" stroke-width="2.6" stroke-linecap="round"/>
<path d="M88 80 L72 78" fill="none" {W(2.4)}/>
<path d="M74 78 l2 3 l2 -3 l2 3 l2 -3" fill="#FFFFFF" {W(1.4)}/>
<path d="M44 68 L52 60 L58 69" fill="#4E8F4A" {W(2.4)}/>
</g>
{eye(56, 66, .75)}''')

# Додо Пицца, Щёлково: картошка из печи
I["cafe-dodo-shchelkovo-lenina"] = (
    "красный бумажный стаканчик с румяными картофельными дольками",
    "одна долька с мордашкой прыгает из стаканчика бомбочкой в лужицу кетчупа",
    ("#FFF9E6", "#E8C27A"), f'''
<ellipse cx="90" cy="108" rx="24" ry="8" fill="#E2423C" {W(3)}/>
<path d="M84 102 Q88 96 92 102 M98 100 l2 -5" fill="none" stroke="#E2423C" stroke-width="3" stroke-linecap="round"/>
<path d="M22 54 L30 114 H62 L70 54 Z" fill="#E2423C" {W(3)}/>
<path d="M28 64 H64" fill="none" stroke="#FFFFFF" stroke-width="3"/>
<path d="M28 56 Q26 36 34 30 Q38 42 36 56 Z" fill="#F2B758" {W(2.6)}/>
<path d="M38 56 Q38 28 46 24 Q50 40 46 56 Z" fill="#E9A443" {W(2.6)}/>
<path d="M48 56 Q52 32 60 30 Q62 44 58 56 Z" fill="#F2B758" {W(2.6)}/>
<path d="M58 56 Q64 40 70 40 Q70 50 66 56 Z" fill="#E9A443" {W(2.6)}/>
<g transform="rotate(30 88 62)"><path d="M76 72 Q76 48 90 44 Q100 56 92 76 Z" fill="#F2B758" {W(3)}/></g>
{eye(84, 60, .5)}{eye(92, 62, .5)}{smile(86, 68, 3, .6)}
<path d="M70 40 Q78 30 86 44" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-dasharray="3 4"/>
{sparkle(108, 30, 5)}''')

# Додо Пицца в Чехове (город «Чайки»): чайка уносит кусок пиццы
I["cafe-dodo-chekhov"] = (
    "белая чайка с распахнутыми крыльями",
    "уносит в клюве горячий треугольник пиццы с тянущимся сыром над красными крышами",
    ("#E9F4FF", "#86B8EC"), f'''
<path d="M0 108 L14 94 L28 108 L42 92 L56 108 L72 96 L88 108 L102 94 L116 108 L128 100 V128 H0 Z" fill="#D9564A" {W(2.8)}/>
<rect x="0" y="108" width="128" height="20" fill="#F2E6D0" {W(2)}/>
<path d="M18 112 h6 v6 h-6z M48 112 h6 v6 h-6z M80 112 h6 v6 h-6z M108 112 h6 v6 h-6z" fill="#9AD3F0" {W(1.6)}/>
<path d="M10 40 Q30 22 56 48 Q80 20 118 34 Q90 40 74 62 Q64 70 54 62 Q38 44 10 40 Z" fill="#FFFFFF" {W(3)}/>
<path d="M10 40 Q20 36 28 38 M118 34 Q108 36 100 38" fill="none" stroke="#9AA0AA" stroke-width="4" stroke-linecap="round"/>
<ellipse cx="64" cy="60" rx="14" ry="10" fill="#FFFFFF" {W(3)}/>
<path d="M74 60 L86 62 L74 66 Z" fill="#FFB020" {W(2.2)}/>
{eye(68, 56, .5)}
{slice_tri(84, 56, 100, 74, 80, 86)}
<circle cx="88" cy="70" r="2.6" fill="#E2423C"/><circle cx="84" cy="78" r="2.4" fill="#E2423C"/>
<path d="M82 86 Q80 94 82 100" fill="none" stroke="#FFD25C" stroke-width="3" stroke-linecap="round"/>''')

# Пипони (римская пепперони): кружок пепперони катится по куску пиццы-горке
I["cafe-piponi-svyatoozerskaya"] = (
    "кружок колбаски пепперони с мордашкой и кружочками жира",
    "катится колесом вниз по прямоугольному куску римской пиццы, как по горке",
    ("#FFEFF2", "#E86A7A"), f'''
<path d="M6 112 L104 52 L118 60 L20 120 Z" fill="#F6D27A" {W(3)}/>
<path d="M104 52 L118 60" fill="none" stroke="#D9934A" stroke-width="8" stroke-linecap="round"/>
<path d="M104 52 L118 60" fill="none" {W(2)}/>
<path d="M30 104 l8 -5 M52 92 l8 -5 M74 78 l8 -5" fill="none" stroke="#5DCB6A" stroke-width="3.4" stroke-linecap="round"/>
<circle cx="88" cy="68" r="6" fill="#C8342C" {W(2)}/>
<circle cx="56" cy="64" r="24" fill="#D8423A" {W(3.2)}/>
<circle cx="56" cy="64" r="19" fill="none" stroke="#B5302A" stroke-width="2"/>
<circle cx="44" cy="54" r="3" fill="#F5A3A0"/><circle cx="68" cy="74" r="3.4" fill="#F5A3A0"/><circle cx="64" cy="50" r="2.4" fill="#F5A3A0"/><circle cx="46" cy="76" r="2.4" fill="#F5A3A0"/>
{eye(50, 62, .6)}{eye(62, 62, .6)}{smile(56, 69, 4, .7)}
<path d="M96 26 Q104 34 100 44 M84 24 Q92 30 90 38" fill="none" stroke="#FFFFFF" stroke-width="3.4" stroke-linecap="round"/>
<path d="M22 50 Q28 44 36 46" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>''')

# IL Патио, Чехов (паста, 4 этаж): фрикаделька съезжает по горе спагетти
I["cafe-ilpatio-chekhov"] = (
    "фрикаделька-глазастик в томатном соусе",
    "съезжает с вершины горы спагетти на тарелке, как с горки, растопырив ручки",
    ("#FFF7DF", "#F5B544"), f'''
<ellipse cx="64" cy="112" rx="56" ry="12" fill="#FFFFFF" {W(3)}/>
<ellipse cx="64" cy="110" rx="40" ry="6" fill="#EEF2F6"/>
<path d="M18 108 Q30 60 64 48 Q98 60 110 108 Z" fill="#F7D46A" {W(3)}/>
<path d="M26 100 Q44 70 64 62 M34 106 Q52 80 74 66 M50 108 Q68 84 90 72 M70 108 Q86 92 102 92 M40 88 Q62 92 86 82" fill="none" stroke="#E0A93A" stroke-width="2.6" stroke-linecap="round"/>
<path d="M60 52 Q66 44 70 52" fill="#E2423C" {W(2)}/>
<path d="M54 50 Q64 40 74 50" fill="none" stroke="#5DCB6A" stroke-width="0"/>
<circle cx="86" cy="76" r="15" fill="#9A4A2A" {W(3)}/>
<path d="M74 70 Q86 62 98 70 Q94 74 86 72 Q78 74 74 70 Z" fill="#E2423C" {W(2)}/>
{eye(81, 78, .5)}{eye(91, 78, .5)}<ellipse cx="86" cy="85" rx="3" ry="2.4" fill="#5A1E14"/>
{limb("M72 78 L64 72", "#9A4A2A", 4)}{limb("M100 78 L108 72", "#9A4A2A", 4)}
<path d="M58 56 L50 62 M60 46 V40" fill="none" stroke="#FFFFFF" stroke-width="0"/>
<path d="M60 40 Q62 30 70 28 Q68 36 62 40 Z" fill="#5DCB6A" {W(2.2)}/>
<path d="M104 58 L112 52 M108 66 L118 64" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>''')

# Додо Пицца у Речного вокзала: коробка пиццы-кораблик
I["cafe-dodo-petrozavodskaya-19"] = (
    "открытая картонная коробка с пиццей, превращённая в кораблик с парусом-салфеткой",
    "плывёт по реке мимо шпиля Речного вокзала, за ней бегут волны",
    ("#E8FAFF", "#48B3C9"), f'''
<path d="M84 64 V36 L90 14 L96 36 V64 Z" fill="#F4F1E6" {W(2.6)}/>
<path d="M78 64 H102 V74 H78 Z" fill="#F4F1E6" {W(2.6)}/>
<path d="M90 14 V6" fill="none" {W(2.4)}/><path d="M90 6 l-3 3 h6 z" fill="#FFD23F" {W(1.6)}/>
<rect x="0" y="84" width="128" height="44" fill="#2D8FC4"/>
<path d="M18 78 L104 78 L94 100 H28 Z" fill="#D9A35A" {W(3)}/>
<ellipse cx="60" cy="80" rx="34" ry="5" fill="#F6CF62" {W(2.4)}/>
<circle cx="46" cy="79" r="2.6" fill="#E2423C"/><circle cx="62" cy="81" r="2.6" fill="#E2423C"/><circle cx="76" cy="79" r="2.6" fill="#E2423C"/>
<path d="M18 78 L10 50 L18 52 Z" fill="#D9A35A" {W(2.6)}/>
<path d="M60 76 V26" fill="none" {W(3)}/>
<path d="M60 28 L60 68 L30 68 Q40 46 60 28 Z" fill="#FFFFFF" {W(2.8)}/>
<path d="M48 48 l6 6 M42 58 l6 6" fill="none" stroke="#E2423C" stroke-width="2.4" stroke-linecap="round"/>
<path d="M60 26 L72 30 L60 34 Z" fill="#E2423C" {W(2)}/>
{eye(32, 88, .45)}{eye(40, 88, .45)}
<path d="M2 104 Q14 98 26 104 M98 108 Q110 102 122 108 M50 114 Q62 110 74 114" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>''')

# Osteria Mario у Ботанического сада: тирамису, из которого растёт мята
I["cafe-osteria-botanica-pika"] = (
    "тирамису в стеклянном стаканчике, слоями",
    "из какао-шапки вырос листик мяты-деревце, стаканчик греется под стеклянным куполом оранжереи",
    ("#F0FFF0", "#7CC79A"), f'''
<path d="M10 126 V70 Q64 0 118 70 V126" fill="#E8FFF6" fill-opacity=".55" {W(3)}/>
<path d="M64 14 V126 M30 40 Q22 80 26 126 M98 40 Q106 80 102 126 M10 82 H118" fill="none" stroke="{O}" stroke-width="2" opacity=".5"/>
<rect x="18" y="112" width="92" height="10" rx="3" fill="#B5845A" {W(2.6)}/>
<path d="M40 64 L46 112 H82 L88 64 Z" fill="#FFFFFF" fill-opacity=".6" {W(3)}/>
<path d="M42 78 L44 92 H84 L86 78 Z" fill="#F7EBD0"/>
<path d="M44 92 L45 100 H83 L84 92 Z" fill="#8A5A3A"/>
<path d="M45 100 L46 110 H82 L83 100 Z" fill="#F7EBD0"/>
<path d="M41 70 L42 78 H86 L87 70 Z" fill="#6A3E22"/>
<path d="M40 64 L46 112 H82 L88 64 Z" fill="none" {W(3)}/>
<path d="M64 66 Q62 52 64 42" fill="none" stroke="#3E8E4A" stroke-width="3.4" stroke-linecap="round"/>
<path d="M64 52 Q48 50 44 38 Q58 36 64 48 Z M64 46 Q78 42 82 30 Q68 30 64 42 Z" fill="#5DCB6A" {W(2.4)}/>
<path d="M50 42 L58 46 M76 36 L68 42" fill="none" stroke="#3E8E4A" stroke-width="1.6"/>
{eye(56, 86, .5)}{eye(72, 86, .5)}<path d="M60 92 Q64 95 68 92" fill="none" stroke="#FFFFFF" stroke-width="0"/>
{blush(52, 90, .5)}{blush(76, 90, .5)}''')

# ---------- БАСКЕТБОЛ ----------

def hoop(x, y, w, board=True, bc="#FFFFFF"):
    """кольцо с сеткой: (x,y) — левый край обода"""
    out = ""
    if board:
        out += f'<rect x="{x - w*.1:.1f}" y="{y - w*.95:.1f}" width="{w*1.2:.1f}" height="{w*.9:.1f}" rx="3" fill="{bc}" {W(2.8)}/>'
        out += f'<rect x="{x + w*.25:.1f}" y="{y - w*.55:.1f}" width="{w*.5:.1f}" height="{w*.45:.1f}" fill="none" stroke="#E2423C" stroke-width="2.4"/>'
    out += (f'<path d="M{x} {y} L{x + w*.15:.1f} {y + w*.6:.1f} H{x + w*.85:.1f} L{x + w} {y} '
            f'M{x + w*.33:.1f} {y} L{x + w*.38:.1f} {y + w*.6:.1f} M{x + w*.66:.1f} {y} L{x + w*.62:.1f} {y + w*.6:.1f} '
            f'M{x + w*.07:.1f} {y + w*.3:.1f} H{x + w*.93:.1f}" fill="none" stroke="#FFFFFF" stroke-width="2"/>'
            f'<ellipse cx="{x + w/2:.1f}" cy="{y}" rx="{w/2:.1f}" ry="{w*.1:.1f}" fill="none" stroke="{O}" stroke-width="5"/>'
            f'<ellipse cx="{x + w/2:.1f}" cy="{y}" rx="{w/2:.1f}" ry="{w*.1:.1f}" fill="none" stroke="#F0662E" stroke-width="2.6"/>')
    return out


# IBASKET в Королёве (город космонавтики): бросок на Луне
I["ibasket-korolev"] = (
    "девочка-космонавт в белом скафандре со стеклянным шлемом",
    "в медленном лунном прыжке бросает мяч в кольцо, воткнутое в серую Луну, а вдали — голубая Земля",
    ("#4B4F9E", "#1C1F4A"), f'''
<circle cx="102" cy="26" r="11" fill="#5DA9E9" {W(2.4)}/><path d="M96 22 q4 -4 8 0 q2 6 -4 8" fill="#5DCB6A"/>
<circle cx="20" cy="30" r="1.8" fill="#fff"/><circle cx="60" cy="14" r="1.6" fill="#fff"/><circle cx="80" cy="44" r="1.4" fill="#fff"/>
<path d="M0 104 Q64 90 128 104 V128 H0 Z" fill="#B9BCC8" {W(3)}/>
<ellipse cx="30" cy="112" rx="8" ry="3" fill="#9497A6"/><ellipse cx="96" cy="116" rx="10" ry="3.4" fill="#9497A6"/>
<path d="M106 102 V52" fill="none" {W(4)}/>
{hoop(84, 56, 22, board=False)}
<rect x="100" y="34" width="20" height="20" rx="3" fill="#FFFFFF" {W(2.6)}/>
{limb("M44 88 L36 100", "#F2F2F6", 9)}{limb("M54 88 L64 98", "#F2F2F6", 9)}
<path d="M38 64 H60 L58 90 H40 Z" fill="#F2F2F6" {W(3)}/>
<rect x="44" y="72" width="10" height="7" rx="1.5" fill="#E2423C" {W(1.6)}/>
{limb("M58 68 L72 50", "#F2F2F6", 7)}{limb("M40 68 L30 78", "#F2F2F6", 7)}
<circle cx="49" cy="52" r="15" fill="#BFE6FF" fill-opacity=".85" {W(3)}/>
<circle cx="49" cy="54" r="9" fill="#F6D2B0" {W(2)}/>
<path d="M40 52 Q40 44 49 44 Q58 44 58 52 Q54 48 49 49 Q44 48 40 52 Z" fill="#7A4A26"/>
{eye(46, 55, .4)}{eye(53, 55, .4)}{smile(49.5, 59, 2.4, .5)}
<path d="M42 44 Q46 40 52 41" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"/>
{basketball(80, 36, 9)}
<path d="M72 46 Q68 52 64 50" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="2 3"/>''')

# МБА — СШОР «Гольяново»: щит-обжора
I["mba-golyanovo"] = (
    "баскетбольный щит с мордашкой, у которого кольцо — широко открытый рот",
    "с аппетитом ловит ртом-кольцом летящий мяч, сетка болтается, как борода",
    ("#FFF0F5", "#EB7FA6"), f'''
<path d="M64 128 V96" fill="none" stroke="{O}" stroke-width="10"/><path d="M64 128 V96" fill="none" stroke="#7A8090" stroke-width="6"/>
<rect x="18" y="18" width="92" height="66" rx="8" fill="#FFFFFF" {W(3.4)}/>
<rect x="44" y="40" width="40" height="30" fill="none" stroke="#E2423C" stroke-width="3"/>
{eye(44, 34, 1.0)}{eye(84, 34, 1.0)}
<path d="M36 22 Q44 18 52 22 M76 22 Q84 18 92 22" fill="none" {W(2.6)}/>
{blush(30, 48, 1.1)}{blush(98, 48, 1.1)}
<path d="M44 74 L50 108 H78 L84 74 M54 74 L57 108 M74 74 L71 108 M46 88 H82 M48 100 H80" fill="none" stroke="#FFFFFF" stroke-width="2.6"/>
<path d="M44 74 L50 108 H78 L84 74" fill="none" {W(1.4)}/>
<ellipse cx="64" cy="74" rx="22" ry="7" fill="#7A2030" stroke="{O}" stroke-width="6"/>
<ellipse cx="64" cy="74" rx="22" ry="7" fill="none" stroke="#F0662E" stroke-width="3.4"/>
{basketball(104, 98, 11)}
<path d="M92 92 Q86 86 84 82" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-dasharray="3 4" stroke-linecap="round"/>''')

# «Стремление», Каланчёвская (группы с 3 лет, мяч дадут): малыш в огромной майке
I["stremlenie-basket-kalanchevskaya"] = (
    "трёхлетний малыш в огромной жёлтой баскетбольной майке до колен",
    "тащит двумя руками мяч больше своей головы к низенькому детскому кольцу",
    ("#E8FBFF", "#6FCBE0"), f'''
<path d="M0 108 H128 V128 H0 Z" fill="#E7B07A" {W(2.4)}/>
<path d="M98 108 V58" fill="none" stroke="{O}" stroke-width="8"/><path d="M98 108 V58" fill="none" stroke="#2F5FB3" stroke-width="5"/>
<rect x="88" y="40" width="34" height="24" rx="3" fill="#FFFFFF" {W(2.6)}/>
{hoop(78, 64, 24, board=False)}
{limb("M38 98 L36 110", "#F6D2B0", 6)}{limb("M50 98 L52 110", "#F6D2B0", 6)}
<path d="M30 110 h10 v4 h-12z M48 110 h10 v4 h-12z" fill="#E2423C" {W(1.6)}/>
<path d="M28 58 Q24 64 26 72 L30 70 L28 100 H60 L58 70 L62 72 Q64 64 60 58 Z" fill="#FFD23F" {W(3)}/>
<text x="38" y="92" font-family="Arial" font-weight="bold" font-size="16" fill="#2F5FB3">3</text>
<circle cx="44" cy="44" r="13" fill="#F6D2B0" {W(2.8)}/>
<path d="M33 40 Q36 30 44 31 Q52 30 55 40 Q50 36 44 37 Q38 36 33 40 Z" fill="#E8B34A" {W(2)}/>
{eye(40, 45, .5)}{eye(49, 45, .5)}{blush(36, 51, .6)}{blush(53, 51, .6)}
<ellipse cx="44.5" cy="51" rx="2.4" ry="2" fill="#C2405A"/>
{basketball(64, 78, 15)}
{limb("M32 66 Q42 78 52 80", "#F6D2B0", 4)}{limb("M58 64 Q66 68 70 72", "#F6D2B0", 4)}
<path d="M28 30 l-4 -4 M60 28 l4 -4" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>''')

# IBASKET у Ломоносовского проспекта: на шпиле МГУ крутится мяч
I["ibasket-lomonosovsky"] = (
    "главное здание МГУ со ступенчатыми крыльями и высоким шпилем",
    "на самом верху шпиля вместо звезды крутится баскетбольный мяч, как на пальце у игрока",
    ("#FFF4E0", "#E6A56B"), f'''
<path d="M6 128 V96 H30 V86 H44 V128 Z M122 128 V96 H98 V86 H84 V128 Z" fill="#F1E3C8" {W(2.8)}/>
<path d="M44 128 V70 H52 V58 H76 V70 H84 V128 Z" fill="#F7EBD3" {W(3)}/>
<path d="M54 58 V46 H74 V58 Z" fill="#F7EBD3" {W(2.8)}/>
<path d="M58 46 L64 28 L70 46 Z" fill="#E8C878" {W(2.6)}/>
<path d="M64 28 V22" fill="none" {W(3)}/>
<path d="M56 80 v6 M64 80 v6 M72 80 v6 M56 96 v6 M64 96 v6 M72 96 v6 M14 104 v6 M22 104 v6 M106 104 v6 M114 104 v6 M36 96 v6 M92 96 v6" fill="none" stroke="#8A6E4A" stroke-width="3" stroke-linecap="round"/>
<rect x="60" y="114" width="8" height="14" fill="#8A6E4A" {W(2)}/>
{basketball(64, 13, 9)}
<path d="M50 10 Q46 14 50 18 M78 10 Q82 14 78 18" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>
{eye(60, 64, .5)}{eye(68, 64, .5)}{smile(64, 70, 3, .6)}
{sparkle(24, 48, 5)}{sparkle(104, 58, 4)}''')

# IBASKET у Водного стадиона: баскетбол на воде
I["ibasket-konakovsky"] = (
    "девочка с косичками в оранжевом спасательном жилете",
    "стоит по пояс в воде и бросает мяч в плавучее кольцо на надувном круге",
    ("#E6FFFB", "#38B5B0"), f'''
<rect x="0" y="80" width="128" height="48" fill="#3AA0D8"/>
<ellipse cx="96" cy="94" rx="22" ry="7" fill="#FF6B6B" {W(2.8)}/>
<path d="M78 92 l6 -4 M100 88 l6 2 M110 96 l-6 3" fill="none" stroke="#FFFFFF" stroke-width="3.4"/>
<path d="M96 92 V54" fill="none" {W(3.4)}/>
<rect x="84" y="36" width="26" height="20" rx="3" fill="#FFFFFF" {W(2.6)}/>
{hoop(80, 56, 20, board=False)}
<path d="M24 86 Q24 66 40 64 Q56 66 56 86 Z" fill="#FF8A2E" {W(3)}/>
<path d="M34 68 V86 M46 68 V86" fill="none" stroke="#FFFFFF" stroke-width="2.4"/>
{limb("M50 70 Q62 56 64 44", "#F6D2B0", 5)}{limb("M30 70 Q22 66 20 58", "#F6D2B0", 5)}
<circle cx="40" cy="52" r="12" fill="#F6D2B0" {W(2.8)}/>
<path d="M28 50 Q30 38 40 39 Q50 38 52 50 Q46 44 40 45 Q34 44 28 50 Z" fill="#B5652B" {W(2)}/>
<path d="M28 50 Q22 58 24 64 M52 50 Q58 58 56 64" fill="none" stroke="#B5652B" stroke-width="4" stroke-linecap="round"/>
{eye(36, 53, .5)}{eye(45, 53, .5)}{smile(40.5, 58, 3, .6)}
{basketball(66, 30, 9)}
<path d="M0 86 Q14 80 28 86 T56 86 T84 86 T112 86 T140 86" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>
<path d="M10 104 Q22 100 34 104 M70 112 Q84 108 96 112" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"/>''')

# IBASKET, Красноказарменная (часовые тренировки): песочные часы из мячиков
I["ibasket-krasnokazarmennaya-11"] = (
    "песочные часы в деревянной рамке, в которых вместо песка пересыпаются оранжевые мячики",
    "последний мячик проскакивает в узкое горлышко — час тренировки пролетел",
    ("#F4F0FF", "#8C7BD8"), f'''
<rect x="26" y="10" width="76" height="12" rx="4" fill="#B5784A" {W(3)}/>
<rect x="26" y="106" width="76" height="12" rx="4" fill="#B5784A" {W(3)}/>
<path d="M34 22 V106 M94 22 V106" fill="none" stroke="{O}" stroke-width="7"/><path d="M34 22 V106 M94 22 V106" fill="none" stroke="#B5784A" stroke-width="4"/>
<path d="M40 22 H88 Q88 50 68 62 Q64 64 68 66 Q88 78 88 106 H40 Q40 78 60 66 Q64 64 60 62 Q40 50 40 22 Z" fill="#E8F6FF" fill-opacity=".85" {W(3)}/>
{basketball(64, 44, 8)}
{basketball(64, 64, 4.5)}
{basketball(52, 97, 8)}{basketball(76, 97, 8)}{basketball(64, 84, 8)}
{eye(61, 44, .35)}{eye(67, 44, .35)}
<path d="M104 40 Q112 50 104 60 M24 70 Q16 80 24 90" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>''')

# IBASKET, Измайловский пр-т: кольцо на башенке Измайловского кремля
I["ibasket-izmaylovsky-115"] = (
    "пёстрая деревянная шатровая башенка Измайловского кремля",
    "на её резном балкончике висит баскетбольное кольцо, и мяч влетает точно в сетку",
    ("#FFF8E0", "#F0B95A"), f'''
<path d="M30 128 V70 H98 V128 Z" fill="#FFFFFF" {W(3)}/>
<path d="M30 84 H98 M30 100 H98" fill="none" stroke="#E2423C" stroke-width="3"/>
<path d="M52 128 V108 Q64 98 76 108 V128 Z" fill="#2F6FD0" {W(2.6)}/>
<path d="M24 70 H104 L96 60 H32 Z" fill="#5DCB6A" {W(2.8)}/>
<path d="M36 60 L64 10 L92 60 Z" fill="#E2423C" {W(3)}/>
<path d="M50 60 L64 20 M78 60 L64 20 M44 46 H84 M54 32 H74" fill="none" stroke="#FFD23F" stroke-width="2.4"/>
<path d="M64 10 V2" fill="none" {W(2.4)}/><circle cx="64" cy="4" r="3" fill="#FFD23F" {W(1.6)}/>
<path d="M36 76 h8 v6 h-8z M84 76 h8 v6 h-8z" fill="#9AD3F0" {W(1.8)}/>
{hoop(72, 92, 22, board=False)}
<path d="M98 92 H106" fill="none" {W(3)}/>
{basketball(82, 80, 8)}
<path d="M98 66 Q104 72 96 76" fill="none" stroke="#FFFFFF" stroke-width="0"/>
{eye(46, 92, .45)}{eye(56, 92, .45)}{smile(51, 96, 2.6, .5)}''')

# IBASKET в Черёмушках: черёмуха, на которой растут мячи
I["ibasket-novocheryomushkinskaya-48"] = (
    "раскидистое дерево, на котором вместо ягод черёмухи висят оранжевые мячики",
    "спелый мяч падает с ветки прямо в кольцо с сеткой, приделанное к стволу",
    ("#F2FFF0", "#7DC56C"), f'''
<path d="M0 116 H128 V128 H0 Z" fill="#6AB55A"/>
<path d="M58 118 Q60 84 54 64 H74 Q68 84 72 118 Z" fill="#9A6A42" {W(3)}/>
<path d="M64 26 Q90 10 108 32 Q124 52 106 68 Q90 80 64 72 Q38 80 22 68 Q4 52 20 32 Q38 10 64 26 Z" fill="#FFFFFF" {W(3)}/>
<circle cx="34" cy="38" r="3" fill="#E8F6E4"/><circle cx="90" cy="30" r="3" fill="#E8F6E4"/>
<path d="M30 48 Q34 52 32 58 M96 46 Q92 52 96 58" fill="none" stroke="#5DCB6A" stroke-width="2.6"/>
{basketball(36, 54, 7)}{basketball(62, 42, 7)}{basketball(88, 54, 7)}{basketball(78, 28, 6)}{basketball(48, 28, 6)}
{hoop(74, 92, 22, board=False)}
<path d="M70 92 H74" fill="none" {W(3)}/>
{basketball(98, 78, 7)}
<path d="M98 66 V60" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="2 2"/>
{eye(59, 90, .45)}{eye(68, 90, .45)}''')

# Баскетбольная школа «Хаски»: мальчик в шапке с ушками хаски на зимней площадке
I["husky-basket-voykovskaya"] = (
    "мальчик в серо-белой вязаной шапке с острыми ушками хаски и голубыми глазками-пуговками",
    "в прыжке забрасывает мяч сверху в кольцо на заснеженной уличной площадке, вокруг падает снег",
    ("#EEF4FF", "#7E9BC8"), f'''
<path d="M0 108 Q64 98 128 108 V128 H0 Z" fill="#FFFFFF" {W(2.6)}/>
<path d="M92 108 V46" fill="none" stroke="{O}" stroke-width="7"/><path d="M92 108 V46" fill="none" stroke="#9AA0AA" stroke-width="4"/>
<rect x="80" y="20" width="36" height="28" rx="3" fill="#FFFFFF" {W(2.6)}/>
<rect x="90" y="30" width="16" height="12" fill="none" stroke="#E2423C" stroke-width="2.4"/>
<path d="M80 20 h36 v4 h-36z" fill="#FFFFFF" stroke="#FFFFFF"/>
{hoop(70, 48, 24, board=False)}
{limb("M46 90 L38 106", "#2F5FB3", 7)}{limb("M54 90 L60 104", "#2F5FB3", 7)}
<path d="M38 64 H60 L58 92 H40 Z" fill="#E2423C" {W(3)}/>
{limb("M58 66 Q70 52 76 42", "#E2423C", 6)}{limb("M40 68 L30 78", "#E2423C", 6)}
{basketball(80, 36, 8)}
<circle cx="49" cy="52" r="12" fill="#F6D2B0" {W(2.8)}/>
<path d="M36 50 Q36 34 49 34 Q62 34 62 50 Z" fill="#8E96A6" {W(2.6)}/>
<path d="M42 44 Q49 38 56 44 L56 50 H42 Z" fill="#FFFFFF"/>
<path d="M37 40 L36 24 L46 35 Z M61 40 L62 24 L52 35 Z" fill="#8E96A6" {W(2.4)}/>
<path d="M39 36 L38 29 L43 34 Z M59 36 L60 29 L55 34 Z" fill="#FFB0C4"/>
<circle cx="45" cy="42" r="1.8" fill="#5DA9E9"/><circle cx="53" cy="42" r="1.8" fill="#5DA9E9"/>
{eye(45, 54, .45)}{eye(53, 54, .45)}{smile(49, 59, 2.6, .5)}
<circle cx="20" cy="30" r="2.4" fill="#fff"/><circle cx="30" cy="80" r="2" fill="#fff"/><circle cx="110" cy="76" r="2.4" fill="#fff"/><circle cx="66" cy="16" r="2" fill="#fff"/><circle cx="14" cy="60" r="2" fill="#fff"/>''')

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
    print(" ".join(I))
