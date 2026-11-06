"""Робот «художник», 06.11 21:20 UTC: перерисовка 40 иконок с повторами (auto/icon-repeats.json).
Каждая иконка придумана и нарисована отдельно, вручную: свой герой, своя сцена, своя палитра фона.
Запуск из корня: python3 tools/icons_artist_1106_2120.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def W(w):
    return s(f'stroke-width="{w}"')


def bgsvg(a, b, body):
    """свой фон для каждой иконки (палитра не из общего набора)"""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
<defs>
 <radialGradient id="g" cx="38%" cy="28%" r="85%"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></radialGradient>
 <clipPath id="c"><circle cx="64" cy="64" r="61"/></clipPath>
</defs>
<circle cx="64" cy="64" r="61" fill="url(#g)"/>
<g clip-path="url(#c)">{body}</g>
<ellipse cx="44" cy="22" rx="20" ry="7" fill="#fff" opacity=".3"/>
</svg>'''


def blush(x, y, k=1.0):
    return f'<ellipse cx="{x}" cy="{y}" rx="{4*k:.1f}" ry="{2.4*k:.1f}" fill="#FF7FA8" opacity=".6"/>'


def smile(x, y, w=4, k=1.0):
    return f'<path d="M{x-w} {y} Q{x} {y+4.5*k:.1f} {x+w} {y}" fill="none" {W(2.4*k)}/>'


I = {}

# 1. Каток в саду «Эрмитаж» — пара коньков вальсирует под садовым фонарём
I["rink-ermitazh"] = ("пара фигурных коньков-танцоров", "вальсируют на льду под садовым фонарём", ("#2E6F78", "#123A48"), f'''
<path d="M0 104 Q64 94 128 104 V128 H0Z" fill="#DDF4FA" {W(2)}/>
<path d="M22 114 Q40 108 58 114 M70 112 Q88 106 106 112" fill="none" stroke="#A8D8E6" stroke-width="2.5"/>
<path d="M108 30 V100" {W(4)}/><path d="M100 30 H116 L112 18 H104Z" fill="#FFE27A" {W(2.4)}/>
<circle cx="108" cy="24" r="16" fill="#FFE27A" opacity=".25"/>
<path d="M20 30 H40 V62 Q40 66 46 68 L58 72 Q64 74 62 82 H18 Q14 82 16 74Z" fill="#fff" {W(3)}/>
<path d="M24 36 L36 40 M24 44 L36 48 M24 52 L36 56" stroke="#E8554A" stroke-width="2.2"/>
<path d="M14 92 H66 Q70 92 70 88" fill="none" stroke="#B8C0D0" stroke-width="4" stroke-linecap="round"/><path d="M22 82 V92 M54 82 V92" {W(2.6)}/>
{eye(28, 70, .55)}{eye(38, 70, .55)}{smile(33, 75, 3, .7)}
<path d="M100 40 H80 V70 Q80 74 74 76 L66 79 Q60 81 62 88 H100 Q104 88 102 80Z" fill="#FFB8D0" {W(3)}/>
<path d="M96 46 L84 50 M96 54 L84 58 M96 62 L84 66" stroke="#fff" stroke-width="2.2"/>
<path d="M106 98 H62 Q58 98 58 94" fill="none" stroke="#B8C0D0" stroke-width="4" stroke-linecap="round"/><path d="M68 88 V98 M96 88 V98" {W(2.6)}/>
{eye(84, 78, .5)}{eye(93, 78, .5)}{smile(88, 83, 3, .6)}
<path d="M59 50 C40 38 50 24 59 34 C68 24 78 38 59 50Z" fill="#FF5A7A" {W(2)}/>
{sparkle(64, 18, 4)}{sparkle(20, 18, 3)}''')

# 2. Сыроварня (Новая Рига) — мышонок выглядывает из дырки в головке сыра
I["cafe-syrovarnya-novaya-riga-outlet"] = ("головка сыра с мышонком в дырке", "мышонок выглядывает из сырной дырки на деревянной доске", ("#FFF1D6", "#E9A86B"), f'''
<rect x="10" y="98" width="108" height="14" rx="6" fill="#B9773F" {W(2.6)}/>
<path d="M18 104 H44 M60 106 H100" stroke="#8F5A2C" stroke-width="2"/>
<path d="M16 66 Q16 44 64 44 Q112 44 112 66 V90 Q112 100 64 100 Q16 100 16 90Z" fill="#FFD24D" {W(3)}/>
<ellipse cx="64" cy="66" rx="48" ry="16" fill="#FFE27A" {W(3)}/>
<circle cx="40" cy="64" r="5" fill="#E8B830"/><circle cx="84" cy="70" r="4" fill="#E8B830"/><circle cx="96" cy="62" r="3" fill="#E8B830"/>
<ellipse cx="64" cy="86" rx="13" ry="10" fill="#7A4E22" {W(2.6)}/>
<circle cx="52" cy="76" r="7" fill="#C9CCD8" {W(2.4)}/><circle cx="76" cy="76" r="7" fill="#C9CCD8" {W(2.4)}/>
<circle cx="52" cy="76" r="3.5" fill="#FFB8C8"/><circle cx="76" cy="76" r="3.5" fill="#FFB8C8"/>
<ellipse cx="64" cy="86" rx="11" ry="8" fill="#C9CCD8" {W(2.4)}/>
{eye(59, 85, .55)}{eye(69, 85, .55)}<circle cx="64" cy="90" r="2" fill="#FF7FA8"/>
<path d="M52 92 L44 94 M52 94 L45 98 M76 92 L84 94 M76 94 L83 98" stroke="{O}" stroke-width="1.4"/>
{eye(36, 82, .7)}{eye(48, 84, .5)}''')

# 3. Якитория (Новогиреево) — онигири прыгает через скакалку
I["cafe-yakitoriya-novogireevo"] = ("онигири с полоской нори", "прыгает через скакалку на детской площадке", ("#DFF7E8", "#6FBF8F"), f'''
<path d="M0 108 H128 V128 H0Z" fill="#F4D9A6" {W(2)}/>
<path d="M24 46 Q14 100 64 112 Q114 100 104 46" fill="none" stroke="#FF6F91" stroke-width="3.5" stroke-linecap="round"/>
<rect x="18" y="36" width="9" height="16" rx="3" fill="#FFC93C" {W(2.2)}/><rect x="101" y="36" width="9" height="16" rx="3" fill="#FFC93C" {W(2.2)}/>
<path d="M64 22 Q72 22 92 62 Q98 76 86 80 H42 Q30 76 36 62 Q56 22 64 22Z" fill="#fff" {W(3)}/>
<rect x="50" y="64" width="28" height="18" rx="2" fill="#2F4A3A" {W(2.4)}/>
{face(64, 50, d=8, k=.75)}
<path d="M42 70 L28 50 M86 70 L100 50" {W(3)}/>
<path d="M54 82 V94 L48 96 M74 82 V94 L80 96" fill="none" {W(3)}/>
<path d="M40 100 Q44 96 48 100 M80 100 Q84 96 88 100" fill="none" stroke="#fff" stroke-width="2"/>''')

# 4. Osteria Mario (ЦДМ) — фрикаделька в гнезде спагетти
I["cafe-osteria-cdm"] = ("фрикаделька-персонаж", "сидит в гнезде из спагетти на тарелке и выглядывает", ("#FFE9E0", "#E6735C"), f'''
<ellipse cx="64" cy="92" rx="54" ry="20" fill="#fff" {W(3)}/><ellipse cx="64" cy="90" rx="40" ry="12" fill="#F2F2F2"/>
<path d="M28 88 Q30 66 64 66 Q98 66 100 88 Q90 96 64 96 Q38 96 28 88Z" fill="#F7D47A" {W(2.8)}/>
<path d="M32 86 Q44 72 58 86 Q70 74 84 86 Q92 78 98 86 M36 80 Q48 70 64 80 Q78 70 92 80" fill="none" stroke="#E0B040" stroke-width="2.4"/>
<circle cx="64" cy="58" r="22" fill="#9A4A2A" {W(3)}/>
<path d="M50 52 Q52 46 58 46 M70 44 l2 2" fill="none" stroke="#C26A44" stroke-width="2.4" stroke-linecap="round"/>
{face(64, 58, d=8, k=.8)}
<path d="M46 40 Q54 30 62 38 Q70 30 78 40" fill="#E8554A" {W(2.4)}/><circle cx="64" cy="36" r="3" fill="#7CD26E" {W(1.6)}/>
<path d="M96 30 l4 8 M104 28 l-2 10" stroke="#5DBB4D" stroke-width="4" stroke-linecap="round"/>''')

# 5. Moomi kids — сырник-мама и сырник-малыш
I["cafe-moomi-kids"] = ("сырник-мама и сырник-малыш", "держатся за руки на блюдце со сметаной", ("#FFF4E8", "#F2A97A"), f'''
<ellipse cx="64" cy="100" rx="52" ry="14" fill="#7FC8F0" {W(3)}/><ellipse cx="64" cy="98" rx="40" ry="8" fill="#B8E2F8"/>
<path d="M18 74 Q18 60 46 60 Q74 60 74 74 V88 Q74 96 46 96 Q18 96 18 88Z" fill="#F0B562" {W(3)}/>
<ellipse cx="46" cy="72" rx="28" ry="10" fill="#F6CC86" {W(2.6)}/>
<path d="M30 70 Q46 52 62 70 Q46 76 30 70Z" fill="#fff" {W(2.4)}/>
{eye(38, 84, .7)}{eye(54, 84, .7)}{smile(46, 89, 4, .8)}{blush(32, 90, .8)}{blush(60, 90, .8)}
<path d="M80 84 Q80 76 96 76 Q112 76 112 84 V92 Q112 98 96 98 Q80 98 80 92Z" fill="#F0B562" {W(2.8)}/>
<ellipse cx="96" cy="83" rx="16" ry="6" fill="#F6CC86" {W(2.4)}/>
<circle cx="96" cy="76" r="4" fill="#E8304A" {W(1.8)}/>
{eye(91, 91, .5)}{eye(101, 91, .5)}
<path d="M74 82 Q78 86 82 88" fill="none" {W(3)}/>
<path d="M58 40 q6 -8 12 0 q-6 8 -12 0Z" fill="#FF7FA8"/>''')

# 6. Альма (Раменки) — сосиска в тесте спит под одеялом
I["cafe-alma-ramenki"] = ("сосиска в тесте", "спит под тестяным одеялом на подушке, Zzz", ("#E4E6FF", "#7C83D6"), f'''
<rect x="6" y="58" width="36" height="28" rx="12" fill="#fff" {W(2.8)}/>
<ellipse cx="34" cy="68" rx="18" ry="14" fill="#E8604A" {W(3)}/>
<path d="M24 66 Q27 63 30 66 M36 66 Q39 63 42 66" fill="none" {W(2.2)}/>
{blush(24, 74, .6)}{blush(42, 74, .6)}<path d="M31 76 Q33 78 35 76" fill="none" {W(2)}/>
<path d="M50 54 H108 Q118 62 116 80 Q112 94 96 94 H52 Q42 94 42 82 V64 Q42 54 50 54Z" fill="#F2B865" {W(3)}/>
<path d="M58 62 L64 86 M78 60 L84 88 M98 60 L104 86" stroke="#D99640" stroke-width="2.4" stroke-linecap="round"/>
<text x="62" y="40" font-family="Arial" font-weight="bold" font-size="14" fill="#fff">z</text>
<text x="74" y="30" font-family="Arial" font-weight="bold" font-size="18" fill="#fff">Z</text>
{sparkle(104, 28, 5, "#FFE27A")}{sparkle(22, 36, 3)}''')

# 7. Пронто (Реутов) — мармеладный мишка машет из креманки
I["cafe-pronto-reutov"] = ("мармеладный мишка", "машет лапкой из стеклянной креманки с мармеладками", ("#E8FFF0", "#5CC59A"), f'''
<path d="M54 100 H74 L70 112 H58Z" fill="#DDF3FF" {W(2.6)}/><rect x="44" y="110" width="40" height="7" rx="3" fill="#DDF3FF" {W(2.4)}/>
<path d="M50 52 Q46 30 64 30 Q82 30 78 52Z" fill="#FF5A6A" fill-opacity=".9" {W(3)}/>
<circle cx="52" cy="32" r="7" fill="#FF5A6A" {W(2.6)}/><circle cx="76" cy="32" r="7" fill="#FF5A6A" {W(2.6)}/>
{eye(58, 42, .6)}{eye(70, 42, .6)}{smile(64, 47, 3, .7)}
<path d="M78 44 Q90 36 92 26" fill="none" stroke="#FF5A6A" stroke-width="8" stroke-linecap="round"/>
<path d="M78 44 Q90 36 92 26" fill="none" {W(1.6)} opacity=".6"/>
<path d="M22 58 Q22 102 64 102 Q106 102 106 58Z" fill="#DDF3FF" fill-opacity=".85" {W(3)}/>
<circle cx="40" cy="68" r="7" fill="#FFC93C" {W(2)}/><circle cx="56" cy="76" r="7" fill="#7CD26E" {W(2)}/>
<circle cx="74" cy="72" r="7" fill="#FF8A3D" {W(2)}/><circle cx="88" cy="66" r="6" fill="#A98BF0" {W(2)}/><circle cx="64" cy="90" r="6" fill="#FF5A6A" {W(2)}/>
<path d="M30 62 Q34 84 46 94" fill="none" stroke="#fff" stroke-width="3" opacity=".8"/>''')

# 8. Каратэ «Мицудэн» — малыш-каратист разбивает дощечку
I["mitsuden-glinisty"] = ("малыш-каратист в белом кимоно с жёлтым поясом", "разбивает дощечку ребром ладони, летят щепки", ("#FFF0D0", "#F28C38"), f'''
<path d="M84 72 L104 64 L108 74 L90 82Z" fill="#D9A15A" {W(2.6)}/><path d="M92 86 L110 82 L112 92 L94 96Z" fill="#D9A15A" {W(2.6)}/>
<path d="M100 60 l6 -8 M112 70 l8 -2 M114 90 l8 4" stroke="{O}" stroke-width="2.4" stroke-linecap="round"/>
<path d="M44 64 L30 92 H76 L66 64Z" fill="#fff" {W(3)}/>
<path d="M52 64 L56 80 L62 64" fill="none" {W(2.4)}/>
<rect x="34" y="80" width="40" height="7" fill="#FFC93C" {W(2.2)}/><path d="M56 87 L50 100 M58 87 L64 100" stroke="#FFC93C" stroke-width="4" stroke-linecap="round"/>
<path d="M34 92 L30 116 H44 L48 96 M66 96 L72 116 H86 L76 92" fill="#fff" {W(3)}/>
<path d="M64 68 Q78 70 90 78" fill="none" stroke="#fff" stroke-width="10" stroke-linecap="round"/>
<path d="M64 68 Q78 70 90 78" fill="none" {W(1.8)}/>
<path d="M88 74 L98 79" stroke="#FFD9B8" stroke-width="7" stroke-linecap="round"/>
<path d="M44 66 Q32 72 26 62" fill="none" stroke="#fff" stroke-width="10" stroke-linecap="round"/><circle cx="24" cy="60" r="5" fill="#FFD9B8" {W(2)}/>
<circle cx="56" cy="44" r="18" fill="#FFD9B8" {W(3)}/>
<path d="M38 40 Q40 24 56 24 Q72 24 74 40 Q66 32 56 34 Q44 32 38 40Z" fill="#3B3355"/>
<rect x="38" y="34" width="36" height="6" fill="#E8304A"/><path d="M38 37 L28 32 M38 37 L30 42" stroke="#E8304A" stroke-width="3" stroke-linecap="round"/>
<path d="M47 46 L53 48 M65 46 L59 48" {W(2.4)}/><path d="M50 54 Q56 58 62 54" fill="none" {W(2.4)}/>{blush(44, 53, .7)}{blush(68, 53, .7)}''')

# 9. ПБК ЦСКА (Смольная) — малыш в форме ЦСКА делает данк
I["pbk-cska-smolnaya"] = ("малыш-баскетболист в красно-синей форме", "в прыжке заколачивает мяч в кольцо сверху (данк)", ("#E3ECFF", "#4A68C9"), f'''
<rect x="78" y="14" width="44" height="30" rx="3" fill="#fff" {W(3)}/><rect x="92" y="26" width="16" height="12" fill="none" stroke="#E8554A" stroke-width="2.6"/>
<path d="M84 46 H112" stroke="#FF6A2A" stroke-width="5" stroke-linecap="round"/>
<path d="M86 48 L90 66 H106 L110 48 M92 48 L98 66 M104 48 L98 66" fill="none" stroke="#fff" stroke-width="2.2"/>
<path d="M44 66 L40 98 H62 L60 66Z" fill="#E8304A" {W(3)}/><path d="M46 70 H58" stroke="#3456C8" stroke-width="4"/>
<path d="M40 98 L32 112 M58 98 L70 108" {W(6)}/>
<path d="M38 94 V106 H62 V94Z" fill="#3456C8" {W(2.6)}/>
<path d="M58 70 L82 42" stroke="#FFD9B8" stroke-width="7" stroke-linecap="round"/><path d="M58 70 L82 42" fill="none" {W(1.4)} opacity=".5"/>
<path d="M44 72 L26 60" stroke="#FFD9B8" stroke-width="7" stroke-linecap="round"/>
<circle cx="88" cy="36" r="11" fill="#F28A2E" {W(2.6)}/><path d="M77 36 H99 M88 25 V47 M80 28 Q88 36 80 44 M96 28 Q88 36 96 44" fill="none" {W(1.8)}/>
<circle cx="50" cy="52" r="14" fill="#FFD9B8" {W(3)}/><path d="M36 48 Q38 36 50 36 Q62 36 64 48 Q56 42 50 44 Q42 42 36 48Z" fill="#6B4226"/>
<rect x="36" y="44" width="28" height="4" fill="#3456C8"/>
{eye(45, 54, .55)}{eye(55, 54, .55)}<path d="M46 60 Q50 64 54 60" fill="#E8554A" {W(2)}/>
{sparkle(20, 30, 5)}{sparkle(34, 18, 3)}''')

# 10. IBASKET (Садовническая) — рука крутит мяч на пальце
I["ibasket-sadovnicheskaya"] = ("ладошка ребёнка", "крутит баскетбольный мяч на указательном пальце", ("#FFF8D6", "#9FD45A"), f'''
<path d="M24 34 Q64 14 104 34 M28 40 Q64 22 100 40" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-dasharray="6 6"/>
<circle cx="64" cy="44" r="27" fill="#F28A2E" {W(3)}/>
<path d="M37 44 H91 M64 17 V71 M44 26 Q58 44 44 62 M84 26 Q70 44 84 62" fill="none" {W(2.2)}/>
{eye(56, 48, .7)}{eye(72, 48, .7)}{smile(64, 54, 4, .8)}{blush(50, 56, .7)}{blush(78, 56, .7)}
<path d="M58 124 L56 96 Q56 86 62 84 L62 74 Q62 70 66 70 Q70 70 70 74 L70 88 Q78 86 80 92 Q88 90 88 98 L88 124Z" fill="#FFD9B8" {W(3)}/>
<path d="M70 92 V100 M80 94 V102" {W(2)}/>
<rect x="54" y="112" width="36" height="10" fill="#5CB7F2" {W(2.4)}/>''')

# 11. Тапчан — лепёшка-нон отдыхает на топчане
I["cafe-tapchan-radonezhskogo"] = ("узбекская лепёшка-нон с узором-печатью", "отдыхает на топчане с подушками и курпачой", ("#FFEFE0", "#C9693A"), f'''
<path d="M14 92 H114 V100 H14Z" fill="#8F5A2C" {W(2.6)}/><path d="M20 100 V116 M108 100 V116 M64 100 V116" {W(4)}/>
<rect x="14" y="84" width="100" height="10" rx="3" fill="#2E7DD1" {W(2.4)}/>
<path d="M22 89 h8 M38 89 h8 M54 89 h8 M70 89 h8 M86 89 h8 M102 89 h6" stroke="#FFC93C" stroke-width="3"/>
<rect x="16" y="64" width="22" height="20" rx="8" fill="#E8304A" {W(2.4)}/><circle cx="27" cy="74" r="4" fill="#FFC93C"/>
<rect x="92" y="66" width="20" height="18" rx="7" fill="#7CD26E" {W(2.4)}/>
<circle cx="64" cy="58" r="30" fill="#E8A94A" {W(3)}/><circle cx="64" cy="58" r="17" fill="#F6D08A" {W(2.4)}/>
<g fill="#B8742A"><circle cx="58" cy="52" r="1.8"/><circle cx="64" cy="50" r="1.8"/><circle cx="70" cy="52" r="1.8"/><circle cx="56" cy="60" r="1.8"/><circle cx="72" cy="60" r="1.8"/><circle cx="64" cy="66" r="1.8"/></g>
<path d="M44 46 Q46 44 50 46 M78 46 Q82 44 84 46" fill="none" {W(2)}/>
{eye(52, 74, .55)}{eye(76, 74, .55)}<path d="M60 78 Q64 81 68 78" fill="none" {W(2)}/>
<path d="M100 30 Q96 22 100 16 M108 32 Q104 24 108 18" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 12. В окошках — пирожок выглядывает из окошка со ставнями
I["cafe-v-okoshkakh"] = ("румяный пирожок с глазками", "выглядывает из деревянного окошка со ставнями и цветком на подоконнике", ("#E8F6FF", "#8FB8E8"), f'''
<rect x="30" y="26" width="68" height="68" fill="#4C3A6B" {W(3)}/>
<path d="M30 26 L22 30 V90 L30 94Z M98 26 L106 30 V90 L98 94Z" fill="#3FA06A" {W(2.6)}/>
<path d="M24 46 L28 50 M24 70 L28 74 M104 46 L100 50 M104 70 L100 74" stroke="#fff" stroke-width="2"/>
<path d="M30 26 Q64 10 98 26" fill="#E8554A" {W(3)}/>
<path d="M36 82 Q36 56 64 56 Q92 56 92 82Z" fill="#E8A040" {W(3)}/>
<path d="M44 62 Q48 58 52 62 M58 58 Q62 54 66 58 M72 60 Q76 56 80 60" fill="none" stroke="#B86A20" stroke-width="2.2"/>
{face(64, 72, d=9, k=.75)}
<rect x="22" y="92" width="84" height="8" rx="2" fill="#fff" {W(2.6)}/>
<path d="M84 92 V80" stroke="#3FA06A" stroke-width="3"/><circle cx="84" cy="76" r="6" fill="#FF6F91" {W(2)}/><circle cx="84" cy="76" r="2" fill="#FFE27A"/>
<rect x="78" y="86" width="12" height="6" fill="#C9693A" {W(1.8)}/>''')

# 13. «Прятки в темноте» — глазки из приоткрытого шкафа
I["hide-dark-kostromskaya"] = ("старый платяной шкаф", "в темноте из приоткрытой дверцы выглядывают глазки ребёнка", ("#3A3058", "#110C22"), f'''
<rect x="28" y="16" width="72" height="100" rx="4" fill="#7A5236" {W(3)}/>
<rect x="34" y="22" width="28" height="88" fill="#8F6242" {W(2.4)}/>
<path d="M66 22 H94 V110 H66" fill="#140F24" {W(2.4)}/>
<path d="M66 22 L84 26 V106 L66 110Z" fill="#9C6E4A" {W(2.4)}/>
<circle cx="58" cy="66" r="2.6" fill="#FFC93C"/><circle cx="72" cy="66" r="2.6" fill="#FFC93C"/>
<ellipse cx="88" cy="56" rx="3.4" ry="4.4" fill="#fff"/><ellipse cx="88" cy="56" rx="1.6" ry="2.6" fill="{O}"/>
<path d="M85 50 Q88 48 91 50" fill="none" stroke="#fff" stroke-width="1.4"/>
<ellipse cx="88" cy="68" rx="2.4" ry="1.4" fill="#FF7FA8" opacity=".7"/>
<path d="M86 96 H92 M85 100 H93" stroke="#FFD9B8" stroke-width="2"/>
<path d="M28 116 V122 M100 116 V122" {W(4)}/>
{sparkle(16, 40, 4, "#FFE27A")}{sparkle(112, 30, 3, "#FFE27A")}{sparkle(110, 92, 2.5, "#fff")}''')

# 14. IBASKET (Бабушкинская) — мяч-бабушка вяжет шарф
I["ibasket-babushkinskaya"] = ("баскетбольный мяч-бабушка в платочке и очках", "вяжет спицами полосатый шарф в кресле", ("#F3E6FF", "#B07CC6"), f'''
<path d="M20 120 V70 Q20 58 34 58 H94 Q108 58 108 70 V120Z" fill="#5A9E6F" {W(3)}/>
<circle cx="64" cy="70" r="28" fill="#F28A2E" {W(3)}/>
<path d="M36 70 H92 M48 46 Q60 70 48 94 M80 46 Q68 70 80 94" fill="none" {W(2)}/>
<path d="M36 64 Q34 38 64 36 Q94 38 92 64 Q86 48 64 48 Q42 48 36 64Z" fill="#E8304A" {W(2.8)}/>
<g fill="#fff"><circle cx="50" cy="44" r="2"/><circle cx="64" cy="41" r="2"/><circle cx="78" cy="44" r="2"/></g>
<circle cx="55" cy="68" r="7" fill="#fff" fill-opacity=".5" {W(2.2)}/><circle cx="73" cy="68" r="7" fill="#fff" fill-opacity=".5" {W(2.2)}/><path d="M62 68 H66" {W(2)}/>
{eye(55, 68, .5)}{eye(73, 68, .5)}{smile(64, 78, 4, .8)}
<path d="M40 98 L62 86 M88 98 L66 86" stroke="#C9CCD8" stroke-width="3" stroke-linecap="round"/>
<path d="M44 96 H86 V108 H44Z" fill="#5CB7F2" {W(2.4)}/><path d="M52 96 V108 M62 96 V108 M72 96 V108 M80 96 V108" stroke="#fff" stroke-width="3"/>
<path d="M86 102 Q98 108 98 120" fill="none" stroke="#5CB7F2" stroke-width="4"/>''')

# 15. «Стремление» (Преображенка) — мяч-комета летит по дуге в кольцо
I["stremlenie-basket-preobrazhenka"] = ("мяч-комета с огненным хвостом", "летит по пунктирной дуге прямо в кольцо", ("#1F2A5E", "#0C1230"), f'''
<path d="M14 110 Q40 20 96 48" fill="none" stroke="#fff" stroke-width="2.6" stroke-dasharray="4 7" stroke-linecap="round"/>
<rect x="96" y="30" width="30" height="24" fill="#fff" {W(2.6)}/>
<path d="M88 58 H112" stroke="#FF6A2A" stroke-width="5" stroke-linecap="round"/>
<path d="M90 60 L94 80 H106 L110 60 M96 60 L100 80 M104 60 L100 80" fill="none" stroke="#fff" stroke-width="2"/>
<path d="M20 74 Q24 54 44 46 Q36 60 50 64 Q34 66 40 82 Q26 82 20 74Z" fill="#FFC93C" {W(2.4)}/>
<path d="M30 70 Q34 60 44 56 Q40 64 48 66" fill="#FF6A2A"/>
<circle cx="58" cy="46" r="16" fill="#F28A2E" {W(2.8)}/><path d="M42 46 H74 M58 30 V62 M48 34 Q56 46 48 58 M68 34 Q60 46 68 58" fill="none" {W(1.8)}/>
{eye(53, 47, .5)}{eye(63, 47, .5)}<path d="M54 53 Q58 56 62 53" fill="none" {W(2)}/>
{sparkle(30, 26, 4, "#FFE27A")}{sparkle(108, 98, 4)}{sparkle(84, 18, 2.5)}''')

# 16. Якитория (Московский) — бенто-коробочка на пикнике
I["cafe-yakitoriya-moskovsky"] = ("бенто-коробочка с отделениями", "открыта на клетчатом пикниковом пледе", ("#E6FFF6", "#7FD6C0"), f'''
<path d="M0 88 L128 76 V128 H0Z" fill="#FF8FA8" {W(2)}/>
<path d="M20 86 L24 128 M52 83 L54 128 M84 80 L84 128 M112 77 L110 128 M0 104 L128 94 M0 118 L128 110" stroke="#fff" stroke-width="4" opacity=".7"/>
<rect x="22" y="40" width="84" height="58" rx="8" fill="#2B2B3A" {W(3)}/>
<rect x="28" y="46" width="34" height="46" rx="4" fill="#fff" {W(2)}/>
<rect x="66" y="46" width="34" height="20" rx="4" fill="#FFE27A" {W(2)}/>
<rect x="66" y="70" width="34" height="22" rx="4" fill="#9BD86A" {W(2)}/>
<g fill="#E8E8E8"><circle cx="36" cy="56" r="2"/><circle cx="46" cy="62" r="2"/><circle cx="52" cy="54" r="2"/></g>
{eye(38, 72, .6)}{eye(52, 72, .6)}{smile(45, 78, 4, .7)}{blush(33, 79, .6)}{blush(57, 79, .6)}
<path d="M72 56 Q83 50 94 56 Q83 62 72 56Z" fill="#FFB020" {W(1.8)}/>
<circle cx="76" cy="81" r="5" fill="#FF6F91" {W(1.8)}/><circle cx="90" cy="81" r="5" fill="#FF6F91" {W(1.8)}/>
<path d="M22 38 L40 20 H120 L106 38" fill="#E8304A" {W(3)}/>''')

# 17. Вареничная №1 (Семёновский) — вареник ныряет в сметану
I["cafe-varenichnaya-semenovskaya"] = ("вареник с вишенкой на макушке", "ныряет с бортика в миску сметаны, как в бассейн", ("#FFE6EC", "#D9607E"), f'''
<path d="M14 82 Q14 120 64 120 Q114 120 114 82Z" fill="#3E8FD8" {W(3)}/>
<ellipse cx="64" cy="82" rx="50" ry="12" fill="#FFFDF4" {W(3)}/>
<path d="M30 80 Q34 72 40 78 M86 78 Q92 70 98 78" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<g transform="rotate(-38 70 46)">
<path d="M42 54 Q42 26 70 26 Q98 26 98 54Z" fill="#FFF3D6" {W(3)}/>
<path d="M44 54 Q48 50 52 54 Q56 50 60 54 Q64 50 68 54 Q72 50 76 54 Q80 50 84 54 Q88 50 92 54 Q96 50 98 54" fill="none" {W(2)}/>
{eye(62, 42, .6)}{eye(76, 42, .6)}<ellipse cx="69" cy="48" rx="3" ry="2.6" fill="#E8554A" {W(1.6)}/>
</g>
<circle cx="88" cy="18" r="6" fill="#B8203A" {W(2)}/><path d="M88 12 Q92 6 98 6" fill="none" stroke="#3FA06A" stroke-width="2.4"/>
<circle cx="40" cy="64" r="3" fill="#fff"/><circle cx="96" cy="60" r="2.5" fill="#fff"/>''')

# 18. La Trattoria (Остров Мечты) — кусочек пиццы мчится по американской горке
I["cafe-la-trattoria-ostrov"] = ("кусочек пиццы в вагончике", "мчится вниз по американской горке, руки вверх", ("#FFF7CF", "#F2B23A"), f'''
<path d="M0 54 Q30 40 50 70 Q70 104 128 96" fill="none" stroke="#E8304A" stroke-width="6"/>
<path d="M0 62 Q30 48 50 78 Q70 112 128 104" fill="none" stroke="#E8304A" stroke-width="4"/>
<path d="M14 54 V128 M38 62 V128 M100 98 V128 M120 98 V128" stroke="#fff" stroke-width="3.5"/>
<g transform="rotate(38 56 64)">
<rect x="36" y="64" width="40" height="18" rx="5" fill="#3E8FD8" {W(2.8)}/>
<circle cx="44" cy="84" r="4" fill="#fff" {W(2)}/><circle cx="68" cy="84" r="4" fill="#fff" {W(2)}/>
<path d="M40 64 L56 24 L72 64Z" fill="#FFD24D" {W(2.8)}/><path d="M42 58 Q56 52 70 58" fill="none" stroke="#E8A040" stroke-width="5"/>
<circle cx="56" cy="40" r="3.5" fill="#E8304A"/><circle cx="62" cy="52" r="3" fill="#E8304A"/>
{eye(51, 50, .45)}{eye(60, 49, .45)}<path d="M52 56 Q56 60 60 56" fill="#E8554A" {W(1.6)}/>
<path d="M44 52 L32 36 M68 52 L80 36" {W(3)}/>
</g>
{sparkle(104, 30, 5)}{sparkle(88, 18, 3)}''')

# 19. Toronto (Истра) — панкейк во вратарской маске
I["cafe-toronto-istra"] = ("панкейк в вратарской маске", "стоит в маленьких хоккейных воротах, кленовый сироп стекает", ("#FFE9E6", "#C8423A"), f'''
<path d="M10 116 H118" stroke="#fff" stroke-width="4"/>
<path d="M20 116 V52 H108 V116" fill="none" stroke="#E8304A" stroke-width="5"/>
<path d="M20 52 L32 64 H96 L108 52" fill="none" stroke="#fff" stroke-width="2"/>
<path d="M32 64 V116 M96 64 V116" stroke="#fff" stroke-width="1.6" opacity=".7"/>
<g stroke="#fff" stroke-width="1.4" opacity=".6"><path d="M44 64 V116 M56 64 V116 M72 64 V116 M84 64 V116 M32 80 H96 M32 96 H96"/></g>
<ellipse cx="64" cy="100" rx="30" ry="9" fill="#E8A040" {W(2.6)}/>
<ellipse cx="64" cy="88" rx="30" ry="9" fill="#F2BE6A" {W(2.6)}/>
<ellipse cx="64" cy="76" rx="30" ry="9" fill="#F6CC86" {W(2.6)}/>
<path d="M40 74 Q46 86 50 78 Q56 92 62 80 Q70 94 76 80 Q82 88 88 74 Z" fill="#B8601E" opacity=".9"/>
<path d="M44 56 Q44 40 64 40 Q84 40 84 56 Q84 72 64 72 Q44 72 44 56Z" fill="#fff" {W(2.8)}/>
<path d="M50 54 H78 M50 62 H78 M58 46 V70 M70 46 V70" stroke="{O}" stroke-width="2"/>
{eye(56, 50, .45)}{eye(72, 50, .45)}
<path d="M98 30 l6 -6 l2 6 l6 0 l-4 5 l3 6 l-7 -2 l-6 4 l1 -7 l-6 -4Z" fill="#E8304A" {W(1.6)}/>''')

# 20. Грузинские каникулы (Мытищи) — косичка сулугуни загорает
I["cafe-gruzinskie-kanikuly-mytishchi"] = ("косичка сулугуни", "загорает в шезлонге под пляжным зонтиком в тёмных очках", ("#DDF6FF", "#3FB0D8"), f'''
<path d="M0 100 Q64 90 128 100 V128 H0Z" fill="#FFE3A3" {W(2)}/>
<path d="M30 20 V100" {W(3.4)}/>
<path d="M2 40 Q30 6 58 40Z" fill="#FF6F91" {W(2.8)}/><path d="M16 40 Q30 14 30 40 M44 40 Q30 14 30 40" fill="#fff" {W(2)}/>
<path d="M50 104 L64 70 H104 L112 104" fill="none" {W(3)}/>
<path d="M58 92 L72 66 L106 70 L100 96Z" fill="#7CD26E" {W(2.6)}/>
<path d="M62 86 L74 64 L104 66 L96 88" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="6 6"/>
<g transform="rotate(-20 84 70)">
<path d="M58 70 Q64 60 72 70 Q80 60 88 70 Q96 60 104 70 Q108 80 104 84 Q96 76 88 84 Q80 76 72 84 Q64 76 58 84 Q54 78 58 70Z" fill="#FFF8E0" {W(2.6)}/>
<rect x="70" y="66" width="10" height="5" rx="2" fill="{O}"/><rect x="84" y="66" width="10" height="5" rx="2" fill="{O}"/><path d="M80 68 H84" {W(1.6)}/>
<path d="M76 76 Q81 80 86 76" fill="none" {W(2)}/>
</g>
<circle cx="108" cy="22" r="10" fill="#FFC93C" {W(2.4)}/>''')

# 21. TODES (Докукина) — мальчик-брейкдансер крутится на голове
I["todes-dokukina"] = ("мальчик-брейкдансер в кепке козырьком назад", "крутится на голове на картонке, линии вращения", ("#FFE0F0", "#E0559A"), f'''
<path d="M14 104 L114 100 L118 114 L10 118Z" fill="#C8955A" {W(2.6)}/><path d="M30 108 H60 M74 106 H100" stroke="#A87440" stroke-width="2"/>
<path d="M30 92 Q64 80 98 92" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="5 6" stroke-linecap="round"/>
<circle cx="64" cy="88" r="13" fill="#FFD9B8" {W(2.8)}/>
<path d="M51 92 Q52 104 64 104 Q76 104 77 92Z" fill="#FFC93C" {W(2.4)}/>
<path d="M74 98 L90 100" stroke="#FFC93C" stroke-width="5" stroke-linecap="round"/>
{eye(59, 84, .5)}{eye(69, 84, .5)}<path d="M60 78 Q64 74 68 78" fill="#E8554A" {W(1.8)}/>
<path d="M54 74 L50 48 H78 L74 74Z" fill="#7C5CE0" {W(2.8)}/>
<path d="M54 52 L36 22 M74 52 L96 26" fill="none" stroke="#3E8FD8" stroke-width="9" stroke-linecap="round"/>
<path d="M54 52 L36 22 M74 52 L96 26" fill="none" {W(1.6)} opacity=".5"/>
<rect x="28" y="12" width="16" height="9" rx="4" fill="#fff" {W(2.2)}/><rect x="90" y="16" width="16" height="9" rx="4" transform="rotate(30 98 20)" fill="#fff" {W(2.2)}/>
<path d="M54 68 L34 76 M74 68 L94 74" stroke="#FFD9B8" stroke-width="6" stroke-linecap="round"/>
<path d="M20 60 Q14 52 20 44 M108 56 Q114 48 108 40" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

# 22. IBASKET (Братиславская) — «дай пять» над мячом
I["ibasket-bratislavskaya"] = ("две ладошки «дай пять»", "хлопают над баскетбольным мячом после победы, искры", ("#E0FFF4", "#2FAF9A"), f'''
<circle cx="64" cy="102" r="22" fill="#F28A2E" {W(3)}/><path d="M42 102 H86 M64 80 V124 M50 86 Q60 102 50 118 M78 86 Q68 102 78 118" fill="none" {W(2)}/>
{eye(57, 100, .5)}{eye(71, 100, .5)}<path d="M59 106 Q64 110 69 106" fill="#E8554A" {W(1.8)}/>
<path d="M16 74 L36 56 Q38 52 42 54 L54 42 Q58 38 61 42 Q63 46 58 50 L62 46 Q66 42 68 46 L60 60 Q54 70 44 72 L26 86Z" fill="#FFD9B8" {W(2.8)}/>
<path d="M112 74 L92 56 Q90 52 86 54 L74 42 Q70 38 67 42 Q65 46 70 50 L66 46 Q62 42 60 46 L68 60 Q74 70 84 72 L102 86Z" fill="#C68B5E" {W(2.8)}/>
<path d="M64 28 V18 M52 30 L46 22 M76 30 L82 22" stroke="#FFE27A" stroke-width="3.4" stroke-linecap="round"/>
{sparkle(30, 30, 5, "#FFE27A")}{sparkle(100, 26, 4, "#fff")}''')

# 23. Москино Салют — стаканчик газировки смотрит мультик
I["cin-salyut"] = ("стаканчик газировки с трубочкой", "сидит в тёмном зале и смотрит на экране мультик-салют", ("#2B2350", "#120E26"), f'''
<rect x="10" y="12" width="108" height="46" rx="4" fill="#BFE6FF" {W(2.6)}/>
<g stroke-linecap="round" stroke-width="2.6"><path d="M40 34 l-8 -8 M40 34 l0 -12 M40 34 l8 -8 M40 34 l-10 2 M40 34 l10 2" stroke="#FF5A8A"/>
<path d="M84 30 l-6 -8 M84 30 l0 -11 M84 30 l7 -7 M84 30 l-9 3 M84 30 l9 3" stroke="#FFB020"/>
<path d="M62 46 l-5 -5 M62 46 l0 -7 M62 46 l5 -5" stroke="#7C5CE0"/></g>
<path d="M44 66 H84 L80 116 H48Z" fill="#E8304A" {W(3)}/>
<path d="M46 80 H82" stroke="#fff" stroke-width="5"/>
<ellipse cx="64" cy="66" rx="22" ry="5" fill="#fff" {W(2.6)}/>
<path d="M70 66 L80 40" stroke="#fff" stroke-width="5" stroke-linecap="round"/><path d="M70 66 L80 40" stroke="#5CB7F2" stroke-width="2" stroke-dasharray="3 3"/>
{face(64, 94, d=7, k=.7)}
<path d="M0 118 Q20 104 40 118 M88 118 Q108 104 128 118" fill="#5A3A8A" {W(2.4)}/>''')

# 24. Чайхона №1 (Алтуфьево) — манты-тройняшки водят хоровод
I["cafe-chaihona1-altufevo"] = ("манты-тройняшки", "водят хоровод на расписном ляганe", ("#EAF2FF", "#4F7BD6"), f'''
<ellipse cx="64" cy="98" rx="56" ry="18" fill="#fff" {W(3)}/><ellipse cx="64" cy="98" rx="46" ry="12" fill="none" stroke="#2E5BC8" stroke-width="3"/>
<path d="M24 98 l6 -4 l6 4 l-6 4Z M92 98 l6 -4 l6 4 l-6 4Z" fill="#2E5BC8"/>
<path d="M18 88 Q18 62 34 58 Q42 54 46 60 Q52 66 50 88Z" fill="#FFF8E6" {W(2.6)}/>
<path d="M28 60 Q34 50 40 58 M34 54 V48" fill="none" {W(2.2)}/>
{eye(28, 74, .45)}{eye(38, 74, .45)}{smile(33, 80, 3, .6)}
<path d="M78 88 Q78 62 94 58 Q102 54 106 60 Q112 66 110 88Z" fill="#FFF8E6" {W(2.6)}/>
<path d="M88 60 Q94 50 100 58 M94 54 V48" fill="none" {W(2.2)}/>
{eye(88, 74, .45)}{eye(98, 74, .45)}{smile(93, 80, 3, .6)}
<path d="M46 92 Q46 58 64 52 Q82 58 82 92Z" fill="#FFF8E6" {W(2.8)}/>
<path d="M54 56 Q64 42 74 56 M64 48 V38" fill="none" {W(2.4)}/><circle cx="64" cy="36" r="3" fill="#7CD26E" {W(1.6)}/>
{eye(58, 72, .55)}{eye(70, 72, .55)}{smile(64, 79, 3.5, .7)}{blush(54, 80, .6)}{blush(74, 80, .6)}
<path d="M48 76 L42 74 M80 76 L86 74" {W(3)}/>''')

# 25. Якитория (Волгоградский) — японский чизкейк дрожит
I["cafe-yakitoriya-volgogradsky"] = ("пышный японский чизкейк", "дрожит и подпрыгивает на тарелке, волны движения", ("#FFFBEA", "#E7C64A"), f'''
<ellipse cx="64" cy="104" rx="50" ry="10" fill="#fff" {W(3)}/>
<path d="M26 98 V56 Q26 44 64 44 Q102 44 102 56 V98 Q102 106 64 106 Q26 106 26 98Z" fill="#FFE9A8" {W(3)}/>
<ellipse cx="64" cy="54" rx="38" ry="10" fill="#E8A640" {W(3)}/>
<path d="M30 64 Q64 74 98 64" fill="none" stroke="#F5D27A" stroke-width="3"/>
{face(64, 80, d=11, k=.85)}
<path d="M14 60 Q8 70 14 80 M8 56 Q0 70 8 84 M114 60 Q120 70 114 80 M120 56 Q128 70 120 84" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<path d="M58 30 Q62 24 66 30 Q70 24 74 30" fill="none" stroke="#fff" stroke-width="2.4"/>
<circle cx="54" cy="52" r="3" fill="#fff" opacity=".6"/>''')

# 26. MiMi (Первомайская) — эклер-лодочка плывёт
I["cafe-mimi-pervomayskaya"] = ("эклер-лодочка с парусом-салфеткой", "плывёт по шоколадной речке", ("#E6F0FF", "#86A6E8"), f'''
<path d="M0 88 Q16 82 32 88 T64 88 T96 88 T128 88 V128 H0Z" fill="#7A4022" {W(2.4)}/>
<path d="M10 104 Q22 100 34 104 M80 110 Q92 106 104 110" fill="none" stroke="#A8643A" stroke-width="3"/>
<path d="M66 18 V68" {W(3)}/><path d="M68 20 L100 60 H68Z" fill="#fff" {W(2.6)}/>
<path d="M76 40 L84 46 M74 50 L90 54" stroke="#FF8FB0" stroke-width="2"/>
<path d="M22 72 Q22 62 34 62 H96 Q108 62 108 72 Q108 86 94 86 H36 Q22 86 22 72Z" fill="#E8B060" {W(3)}/>
<path d="M24 68 Q26 60 36 60 H94 Q106 60 106 68 Q100 72 90 70 Q80 74 70 70 Q60 74 50 70 Q40 74 30 70Z" fill="#5A2E16" {W(2.4)}/>
<path d="M40 64 h10 M60 63 h8" stroke="#fff" stroke-width="2" opacity=".5"/>
{eye(52, 77, .55)}{eye(64, 77, .55)}{smile(58, 82, 3, .6)}{blush(46, 82, .6)}''')

# 27. Батоно Джонни (Видное) — две половинки хачапури перетягивают сырный канат
I["cafe-batono-jonny-vidnoe"] = ("две половинки имеретинского хачапури", "перетягивают тянущуюся сырную нитку, как канат", ("#F0FFE0", "#8CC63E"), f'''
<path d="M0 110 H128 V128 H0Z" fill="#5E9E2E"/>
<path d="M44 64 Q64 74 84 64" fill="none" stroke="#FFF3B0" stroke-width="7" stroke-linecap="round"/>
<path d="M44 64 Q64 74 84 64" fill="none" stroke="{O}" stroke-width="1.4" opacity=".4"/>
<path d="M44 38 A30 30 0 0 0 44 98Z" fill="#E8A040" transform="translate(-6 0)" {W(3)}/>
<path d="M38 46 A22 22 0 0 0 38 90Z" fill="#FFE68A"/>
{eye(22, 62, .5)}{eye(30, 62, .5)}<path d="M22 70 Q26 74 30 70" fill="#E8554A" {W(1.6)}/>
<path d="M84 38 A30 30 0 0 1 84 98Z" fill="#E8A040" transform="translate(6 0)" {W(3)}/>
<path d="M90 46 A22 22 0 0 1 90 90Z" fill="#FFE68A"/>
<path d="M100 60 l-4 2 l4 2 M108 60 l4 2 l-4 2" fill="none" {W(2)}/><path d="M100 70 Q104 74 108 70" fill="#E8554A" {W(1.6)}/>
<path d="M12 104 H32 M96 104 H116" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
{sparkle(64, 34, 5)}''')

# 28. Айва (Одинцово) — запечённая айва, мороженое скатывается
I["cafe-ayva-odintsovo"] = ("запечённая половинка айвы с медовой серединкой", "шарик мороженого съезжает с неё, как с горки", ("#FFEFD8", "#D98A3A"), f'''
<ellipse cx="64" cy="102" rx="52" ry="12" fill="#B8E2F8" {W(3)}/>
<path d="M20 96 Q18 52 60 48 Q102 46 106 92 Q100 100 64 100 Q26 100 20 96Z" fill="#F0B030" {W(3)}/>
<ellipse cx="64" cy="66" rx="16" ry="11" fill="#C8601E" {W(2.4)}/><ellipse cx="62" cy="64" rx="7" ry="4" fill="#E88A3A"/>
{eye(46, 84, .55)}{eye(58, 84, .55)}{smile(52, 90, 3.5, .65)}{blush(40, 90, .6)}
<circle cx="94" cy="58" r="13" fill="#FFF8F0" {W(2.6)}/><path d="M84 66 Q90 72 96 66 Q100 72 104 64" fill="none" {W(2)}/>
{eye(90, 56, .4)}{eye(98, 56, .4)}<path d="M90 62 Q94 66 98 62" fill="#E8554A" {W(1.4)}/>
<path d="M104 46 l6 -6 M108 54 l8 -2" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M56 46 Q54 36 62 30" fill="none" stroke="#8F5A2C" stroke-width="3"/><path d="M62 32 Q72 26 76 34 Q68 38 62 32Z" fill="#7CD26E" {W(1.8)}/>''')

# 29. Чайхона For You (Щука) — щука в короне с пиалой чая
I["cafe-chaihona-for-you-shchuka"] = ("щука в золотой короне", "высовывается из проруби и подаёт пиалу чая («по щучьему велению»)", ("#EAF8FF", "#5C9EC8"), f'''
<path d="M0 92 H128 V128 H0Z" fill="#F2FAFF"/><ellipse cx="56" cy="100" rx="40" ry="10" fill="#1E5A8A" {W(3)}/>
<path d="M36 100 Q30 62 48 40 Q60 26 72 40 Q80 54 76 100Z" fill="#7CB342" {W(3)}/>
<path d="M42 70 Q56 66 70 70 M40 84 Q56 80 72 84" fill="none" stroke="#5A8A2A" stroke-width="2.4"/>
<path d="M44 46 Q56 36 70 46 L74 30 Q56 22 40 30Z" fill="#9CCB5A" {W(2.4)}/>
<path d="M44 30 L46 16 L52 24 L58 12 L64 24 L70 16 L72 30Z" fill="#FFC93C" {W(2.4)}/>
{eye(50, 46, .55)}{eye(64, 46, .55)}<path d="M50 56 L56 58 L62 56 L68 58" fill="none" {W(2)}/>
<path d="M74 62 L92 58" {W(3.4)}/>
<path d="M86 52 Q86 66 100 66 Q114 66 114 52Z" fill="#fff" {W(2.6)}/><path d="M88 56 H112" stroke="#2E5BC8" stroke-width="2.4"/>
<path d="M96 46 Q94 40 98 36 M104 46 Q102 40 106 36" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>''')

# 30. IBASKET (Бутово) — мяч в центральном круге площадки, вид сверху
I["ibasket-butovo"] = ("баскетбольная площадка, вид сверху", "мячик-малыш стоит в центральном круге на разметке", ("#FFE8D0", "#E0904A"), f'''
<rect x="18" y="18" width="92" height="92" fill="#E8A65A" {W(3)}/>
<path d="M18 64 H110" stroke="#fff" stroke-width="3"/><circle cx="64" cy="64" r="16" fill="none" stroke="#fff" stroke-width="3"/>
<path d="M44 18 V34 H84 V18 M44 110 V94 H84 V110" fill="#D06A3A" stroke="#fff" stroke-width="3"/>
<path d="M36 18 Q36 50 64 50 Q92 50 92 18 M36 110 Q36 78 64 78 Q92 78 92 110" fill="none" stroke="#fff" stroke-width="2.4"/>
<circle cx="64" cy="64" r="11" fill="#F28A2E" {W(2.4)}/><path d="M53 64 H75 M64 53 V75" {W(1.6)}/>
{eye(60, 64, .38)}{eye(68, 64, .38)}
<circle cx="64" cy="24" r="4" fill="none" stroke="#E8304A" stroke-width="2.4"/><circle cx="64" cy="104" r="4" fill="none" stroke="#E8304A" stroke-width="2.4"/>''')

# 31. IBASKET (Батайский) — кубок с мячом на крышке под конфетти
I["ibasket-bataysky"] = ("золотой кубок с баскетбольным мячом на крышке", "стоит на пьедестале под конфетти", ("#F2E8FF", "#8C5CD6"), f'''
<rect x="34" y="100" width="60" height="22" fill="#fff" {W(3)}/><text x="58" y="117" font-family="Arial" font-weight="bold" font-size="16" fill="{O}">1</text>
<rect x="48" y="90" width="32" height="10" fill="#C98A20" {W(2.6)}/><path d="M58 76 H70 L72 90 H56Z" fill="#FFC93C" {W(2.6)}/>
<path d="M38 46 H90 Q90 78 64 78 Q38 78 38 46Z" fill="#FFC93C" {W(3)}/>
<path d="M38 52 Q24 52 26 62 Q28 70 42 68 M90 52 Q104 52 102 62 Q100 70 86 68" fill="none" {W(3)}/>
{eye(56, 60, .55)}{eye(72, 60, .55)}{smile(64, 66, 4, .7)}
<circle cx="64" cy="34" r="12" fill="#F28A2E" {W(2.6)}/><path d="M52 34 H76 M64 22 V46 M56 26 Q62 34 56 42 M72 26 Q66 34 72 42" fill="none" {W(1.6)}/>
<rect x="18" y="20" width="6" height="3" fill="#FF5A8A" transform="rotate(30 21 21)"/><rect x="100" y="30" width="6" height="3" fill="#7CD26E" transform="rotate(-20 103 31)"/>
<rect x="104" y="80" width="6" height="3" fill="#FFE27A" transform="rotate(40 107 81)"/><rect x="16" y="76" width="6" height="3" fill="#5CB7F2" transform="rotate(-40 19 77)"/>
<circle cx="30" cy="40" r="2.4" fill="#FFE27A"/><circle cx="96" cy="16" r="2.4" fill="#5CB7F2"/>''')

# 32. EXTREME KIDS (Отрадное) — девочка на роликах едет змейкой между фишками
I["extremekids-roller-otradnoe"] = ("девочка на роликах в шлеме", "едет змейкой между оранжевыми фишками-конусами", ("#E8FFF8", "#43C2A8"), f'''
<path d="M0 98 H128 V128 H0Z" fill="#9AA6B8"/><path d="M10 112 Q40 100 64 112 T118 112" fill="none" stroke="#fff" stroke-width="2.6" stroke-dasharray="5 6"/>
<path d="M16 116 L22 100 L28 116Z M100 118 L106 102 L112 118Z" fill="#FF8A3D" {W(2.2)}/>
<path d="M58 60 L52 82 H72 L70 60Z" fill="#FF6F91" {W(2.8)}/>
<path d="M56 82 L46 96 M68 82 L80 92" {W(6)}/>
<path d="M38 94 H54 V100 H38Z M76 88 L90 92 L88 98 L74 94Z" fill="#7C5CE0" {W(2)}/>
<path d="M38 104 h16 M74 102 l14 4" stroke="{O}" stroke-width="2.4" stroke-dasharray="1 5" stroke-linecap="round"/>
<path d="M58 64 L40 56 M70 64 L88 58" stroke="#FFD9B8" stroke-width="6" stroke-linecap="round"/>
<circle cx="64" cy="44" r="14" fill="#FFD9B8" {W(2.8)}/>
<path d="M48 42 Q48 26 64 26 Q80 26 80 42Z" fill="#FFC93C" {W(2.6)}/><path d="M56 30 V38 M64 28 V38 M72 30 V38" stroke="#fff" stroke-width="2"/>
<path d="M78 42 Q90 44 92 54" fill="none" stroke="#A86F3E" stroke-width="5" stroke-linecap="round"/>
{eye(59, 47, .5)}{eye(69, 47, .5)}{smile(64, 52, 3, .6)}''')

# 33. Школа плавания «Чайка» — малыш в нарукавниках прыгает бомбочкой
I["chaika-swim-school"] = ("малыш в оранжевых нарукавниках", "прыгает «бомбочкой» в бассейн, брызги во все стороны", ("#E0F4FF", "#2C8ED8"), f'''
<path d="M0 92 H128 V128 H0Z" fill="#3FA9F0"/><path d="M0 92 H128" stroke="#fff" stroke-width="3"/>
<path d="M0 108 H128" stroke="#FFC93C" stroke-width="3" stroke-dasharray="8 6"/>
<path d="M26 92 L18 72 M40 90 L36 66 M88 90 L92 66 M102 92 L112 72" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
<circle cx="20" cy="64" r="3" fill="#fff"/><circle cx="110" cy="64" r="3" fill="#fff"/>
<circle cx="64" cy="66" r="22" fill="#FFD9B8" {W(3)}/>
<path d="M44 56 Q44 40 64 40 Q84 40 84 56Z" fill="#E8304A" {W(2.6)}/>
<path d="M46 76 Q40 66 50 62 M82 76 Q88 66 78 62" fill="none" stroke="#FFD9B8" stroke-width="8" stroke-linecap="round"/>
<rect x="34" y="58" width="16" height="14" rx="6" fill="#FF8A3D" {W(2.4)}/><rect x="78" y="58" width="16" height="14" rx="6" fill="#FF8A3D" {W(2.4)}/>
<path d="M54 62 Q57 59 60 62 M68 62 Q71 59 74 62" fill="none" {W(2.2)}/>
<ellipse cx="64" cy="72" rx="4" ry="3" fill="#E8554A" {W(1.8)}/>{blush(52, 70, .6)}{blush(76, 70, .6)}
<path d="M54 84 Q64 92 74 84" fill="none" stroke="#FFD9B8" stroke-width="8" stroke-linecap="round"/>''')

# 34. АндерСон (Воронцовский парк) — маршмеллоу на палочке над костерком
I["cafe-anderson-vorontsovsky"] = ("маршмеллоу на палочке", "поджаривается над маленьким костерком в парке", ("#E8F4DA", "#4F8A3A"), f'''
<path d="M8 40 L20 14 L32 40Z M100 46 L112 18 L124 46Z" fill="#2F6A2A" {W(2)}/>
<path d="M30 112 L98 98 M34 98 L94 112" stroke="#8F5A2C" stroke-width="7" stroke-linecap="round"/>
<path d="M46 102 Q40 84 54 72 Q54 84 62 82 Q60 68 70 60 Q72 76 80 78 Q90 90 80 104Z" fill="#FF8A3D" {W(2.6)}/>
<path d="M56 100 Q54 90 62 84 Q64 92 70 92 Q76 96 72 102Z" fill="#FFE27A"/>
<path d="M106 76 L68 40" stroke="#B9773F" stroke-width="4" stroke-linecap="round"/>
<rect x="52" y="20" width="26" height="26" rx="10" fill="#FFF6FA" transform="rotate(-42 65 33)" {W(2.8)}/>
<path d="M52 36 Q60 48 72 44" fill="none" stroke="#E8A040" stroke-width="3"/>
{eye(60, 30, .5)}{eye(70, 28, .5)}<path d="M62 37 Q66 39 70 35" fill="none" {W(1.8)}/>
{sparkle(36, 70, 3, "#FFE27A")}{sparkle(96, 60, 2.5, "#FFE27A")}''')

# 35. АндерСон (Пушкино) — трубочка с кремом трубит, как горн
I["cafe-anderson-pushkino"] = ("трубочка со взбитыми сливками", "трубит, как горн, — из неё вылетают нотки-кремовые завитки", ("#FFF0F6", "#E88AB0"), f'''
<path d="M18 104 L70 44 Q86 44 92 58 L30 112 Q18 114 18 104Z" fill="#E8A040" {W(3)}/>
<path d="M30 96 L40 104 M42 82 L54 92 M54 68 L68 80 M66 54 L80 66" stroke="#C07A22" stroke-width="2.6"/>
<path d="M66 46 Q66 30 80 32 Q86 20 98 26 Q112 24 110 38 Q120 46 110 56 Q108 66 96 62 Q88 70 82 60 Q70 62 66 46Z" fill="#fff" {W(2.8)}/>
{eye(46, 86, .6)}{eye(58, 76, .6)}<path d="M50 94 Q58 92 62 84" fill="none" {W(2.2)}/>{blush(42, 96, .6)}
<path d="M104 12 v-8 l8 -2 v8" fill="none" {W(2.2)}/><circle cx="102" cy="12" r="3" fill="{O}"/><circle cx="110" cy="10" r="3" fill="{O}"/>
<path d="M120 26 v-8" {W(2.2)}/><circle cx="118" cy="26" r="2.6" fill="{O}"/>
<circle cx="94" cy="30" r="4" fill="#E8304A" {W(1.6)}/>''')

# 36. Урюк (Европейский) — урюк сушится на верёвочке
I["cafe-uryuk-evropeisky"] = ("урючинки-абрикоски", "сушатся рядком на верёвочке под ярким солнцем", ("#FFF6CC", "#F0A020"), f'''
<circle cx="102" cy="26" r="14" fill="#FFE27A" {W(2.4)}/>
<path d="M102 6 v-6 M120 26 h6 M116 12 l4 -4" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M4 52 Q64 76 124 52" fill="none" {W(2.6)}/>
<path d="M28 60 V64 M64 66 V70 M100 60 V64" {W(2)}/>
<ellipse cx="28" cy="74" rx="14" ry="11" fill="#F28A2E" {W(2.6)}/><path d="M28 64 Q24 74 28 84" fill="none" stroke="#C8601E" stroke-width="2"/>
{eye(23, 74, .4)}{eye(33, 74, .4)}<path d="M25 79 Q28 81 31 79" fill="none" {W(1.6)}/>
<ellipse cx="64" cy="82" rx="18" ry="14" fill="#FF9A3C" {W(2.8)}/><path d="M64 68 Q58 82 64 96" fill="none" stroke="#C8601E" stroke-width="2.2"/>
{eye(57, 81, .55)}{eye(71, 81, .55)}{smile(64, 88, 3.5, .7)}{blush(52, 89, .6)}{blush(76, 89, .6)}
<ellipse cx="100" cy="74" rx="14" ry="11" fill="#E87A1E" {W(2.6)}/><path d="M100 64 Q96 74 100 84" fill="none" stroke="#B8501A" stroke-width="2"/>
{eye(95, 74, .4)}{eye(105, 74, .4)}<path d="M97 79 Q100 81 103 79" fill="none" {W(1.6)}/>
<path d="M0 110 Q64 100 128 110 V128 H0Z" fill="#C8E07A" {W(2)}/>''')

# 37. Сыроварня (Митино Парк) — шарик моцареллы плавает в шапочке
I["cafe-syrovarnya-mitino-park"] = ("белый шарик моцареллы", "плавает в мисочке с сывороткой в полосатой шапочке для плавания", ("#F2EEFF", "#6A5AC8"), f'''
<path d="M10 70 Q10 118 64 118 Q118 118 118 70Z" fill="#E8F4FF" {W(3)}/>
<path d="M10 70 Q10 118 64 118 Q118 118 118 70Z" fill="none" stroke="#5CB7F2" stroke-width="0"/>
<ellipse cx="64" cy="70" rx="54" ry="12" fill="#D8EEFF" {W(3)}/>
<path d="M24 74 Q34 68 44 74 M84 74 Q94 68 104 74" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<circle cx="64" cy="58" r="22" fill="#fff" {W(3)}/>
<path d="M42 54 Q42 34 64 34 Q86 34 86 54Z" fill="#FF6F91" {W(2.6)}/><path d="M48 40 Q64 34 80 40 M44 48 Q64 42 84 48" fill="none" stroke="#fff" stroke-width="3"/>
{eye(57, 62, .55)}{eye(71, 62, .55)}{smile(64, 68, 3.5, .7)}{blush(52, 69, .6)}{blush(76, 69, .6)}
<path d="M36 66 Q30 58 34 52 M92 66 Q98 58 94 52" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<path d="M36 66 Q30 58 34 52 M92 66 Q98 58 94 52" fill="none" {W(1.4)} opacity=".5"/>
<path d="M98 30 l6 -6 M106 34 l8 -2" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 38. Якитория (Долгопрудный) — ролл-ракета взлетает
I["cafe-yakitoriya-dolgoprudny"] = ("ролл-ракета с нори-обшивкой", "взлетает к звёздам, из сопла клубится рисовый дымок", ("#1D2B5A", "#070C24"), f'''
<path d="M50 96 Q40 112 52 120 Q58 108 64 122 Q70 108 76 120 Q88 112 78 96Z" fill="#FF8A3D" {W(2.4)}/>
<path d="M58 98 Q56 108 64 114 Q72 108 70 98Z" fill="#FFE27A"/>
<path d="M44 70 L30 96 H48Z M84 70 L98 96 H80Z" fill="#E8304A" {W(2.6)}/>
<path d="M44 96 V44 Q44 20 64 10 Q84 20 84 44 V96Z" fill="#1F3A2A" {W(3)}/>
<rect x="48" y="38" width="32" height="50" rx="6" fill="#fff" {W(2.4)}/>
<circle cx="64" cy="54" r="7" fill="#FF7A5A" {W(2)}/><rect x="60" y="51" width="8" height="6" fill="#7CD26E"/>
{eye(58, 72, .5)}{eye(70, 72, .5)}{smile(64, 78, 3, .6)}
{sparkle(18, 24, 5, "#FFE27A")}{sparkle(108, 36, 4)}{sparkle(22, 70, 3)}{sparkle(110, 80, 3, "#FFE27A")}''')

# 39. Кот да Винчи (Щёлково) — кот-художник с пиццей вместо палитры
I["cafe-kot-da-vinchi"] = ("рыжий кот-художник в берете", "держит пиццу, как палитру, и кисточку", ("#FFE8E0", "#F07858"), f'''
<path d="M30 124 Q28 84 64 82 Q100 84 98 124Z" fill="#FF9A3C" {W(3)}/>
<path d="M36 52 L32 22 L52 38Z M92 52 L96 22 L76 38Z" fill="#FF9A3C" {W(2.8)}/>
<circle cx="64" cy="60" r="28" fill="#FF9A3C" {W(3)}/>
<path d="M38 36 Q46 20 70 22 Q88 24 84 34 Q66 38 38 36Z" fill="#3B3355"/><circle cx="62" cy="20" r="3" fill="#3B3355"/>
<path d="M50 50 l6 4 M78 50 l-6 4" stroke="#C8601E" stroke-width="2.4"/>
{eye(54, 60, .65)}{eye(74, 60, .65)}<path d="M60 70 L64 74 L68 70" fill="none" {W(2)}/><path d="M64 74 Q60 78 56 76 M64 74 Q68 78 72 76" fill="none" {W(2)}/>
<path d="M40 70 H24 M40 74 L26 78 M88 70 H104 M88 74 L102 78" stroke="{O}" stroke-width="1.6"/>
<path d="M14 92 L46 84 L34 118Z" fill="#FFD24D" {W(2.6)}/><path d="M16 94 L46 86" stroke="#E8A040" stroke-width="5"/>
<circle cx="32" cy="98" r="3.5" fill="#E8304A"/><circle cx="38" cy="106" r="3" fill="#7CD26E"/><circle cx="28" cy="104" r="2.6" fill="#E8304A"/>
<path d="M98 116 L112 82" stroke="#B9773F" stroke-width="4" stroke-linecap="round"/><path d="M110 84 L114 74 L118 80Z" fill="#5CB7F2" {W(2)}/>''')

# 40. Kitchen (ЖК Alia) — наггетсы-динозаврики идут к кетчупу
I["cafe-kitchen-alia"] = ("наггетс-динозаврик с длинной шеей", "шагает по тарелке к лужице кетчупа", ("#EFFFE0", "#6CB83A"), f'''
<ellipse cx="64" cy="100" rx="58" ry="18" fill="#fff" {W(3)}/><ellipse cx="64" cy="100" rx="46" ry="12" fill="#F4F4F4"/>
<ellipse cx="102" cy="102" rx="14" ry="6" fill="#E8304A" {W(2.4)}/>
<path d="M30 80 Q14 84 6 98 Q22 94 34 92Z" fill="#F0BE6A" {W(2.6)}/>
<path d="M66 76 Q80 62 80 40" fill="none" stroke="{O}" stroke-width="17" stroke-linecap="round"/>
<path d="M66 76 Q80 62 80 40" fill="none" stroke="#F0BE6A" stroke-width="11" stroke-linecap="round"/>
<path d="M36 88 V102 M48 90 V104 M62 88 V102 M72 86 V100" {W(6)}/>
<path d="M36 88 V102 M48 90 V104 M62 88 V102 M72 86 V100" stroke="#E8B060" stroke-width="3"/>
<ellipse cx="54" cy="80" rx="26" ry="15" fill="#F0BE6A" {W(3)}/>
<ellipse cx="86" cy="36" rx="12" ry="9" fill="#F0BE6A" {W(2.8)}/>
<g fill="#C88A3A"><circle cx="44" cy="76" r="2"/><circle cx="56" cy="72" r="2"/><circle cx="62" cy="84" r="2"/><circle cx="48" cy="86" r="1.6"/></g>
{eye(88, 33, .5)}<path d="M88 40 Q92 42 96 39" fill="none" {W(1.8)}/>{blush(82, 40, .5)}
{sparkle(108, 22, 5)}{sparkle(22, 36, 3)}''')


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
