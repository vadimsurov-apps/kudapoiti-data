"""Иконки робота creative, 12.11 (запуск 1112z). Каждая придумана и нарисована отдельно: свой герой, своя сцена,
своя компоновка и свой фон (правило абсолютной уникальности). python3 tools/icons_creative_1112z.py [--subjects]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_creative_1112k import bg, ln, limb, note, head, SKIN

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
I = {}

# 1 B-Major (вокал, мюзикл, эстрадный танец, Некрасовка): знак диеза поёт в старинный микрофон
I["b-major-nekrasovka"] = ("золотой знак диеза «♯» с мордашкой в центральном окошке",
    "поёт, наклонившись к серебряному ретро-микрофону на стойке, из микрофона вылетают нотки", bg("#FFD6F0", "#8E1F6E", f'''
<path d="M0 112 H128 V128 H0Z" fill="#5A1446"/>
<g transform="rotate(-10 52 64)">
<path d="M40 22 L36 106 M62 18 L58 102" {ln(O, 13)}/><path d="M40 22 L36 106 M62 18 L58 102" {ln("#FFC93C", 8)}/>
<path d="M22 50 L80 38 M20 80 L78 68" {ln(O, 15)}/><path d="M22 50 L80 38 M20 80 L78 68" {ln("#FFC93C", 10)}/>
<rect x="38" y="47" width="22" height="25" rx="4" fill="#FFE590" {s('stroke-width="2.4"')}/>
{face(49, 57, 5, 0.55)}
</g>
<path d="M98 112 V70" {ln(O, 7)}/><path d="M98 112 V70" {ln("#B0B7C3", 4)}/>
<path d="M86 114 H110" {ln(O, 6)}/>
<path d="M98 70 L88 58" {ln(O, 6)}/><path d="M98 70 L88 58" {ln("#B0B7C3", 3)}/>
<rect x="76" y="40" width="18" height="24" rx="9" fill="#D9DEE6" transform="rotate(-40 85 52)" {s()}/>
<path d="M76 46 L90 58 M79 42 L93 54" stroke="#8A93A3" stroke-width="1.6" transform="rotate(0)"/>
{note(104, 26, 0.75, "#fff")}{note(116, 46, 0.55, "#FFC93C")}
{sparkle(16, 22, 4)}
'''))

# 2 Студия Ксении Белой (хореография с 2 лет, классика, актёрское): малышка с бантом делает реверанс у белого облака-кулисы
I["belaya-studio-komsomolsky"] = ("двухлетняя малышка в голубом купальнике с огромным белым бантом на макушке",
    "делает первый в жизни реверанс на краю сцены, держа юбочку двумя пальчиками, а сверху свисает белое облако-кулиса", bg("#E9F4FF", "#3D78C2", f'''
<path d="M0 100 Q64 92 128 100 V128 H0Z" fill="#E7C08E" {s('stroke-width="2.4"')}/>
<path d="M-4 0 H132 V22 Q120 32 106 24 Q94 34 80 25 Q64 35 48 25 Q34 34 22 24 Q8 32 -4 22Z" fill="#fff" {s()}/>
{limb(56, 84, 52, 104, SKIN, 5)}{limb(70, 84, 76, 104, SKIN, 5)}
<path d="M48 104 H56 M72 104 H80" {ln("#F5B7C9", 5)}/>
<path d="M50 62 Q64 56 78 62 L80 76 H48Z" fill="#7EC3F2" {s()}/>
<path d="M34 86 Q64 66 94 86 Q64 94 34 86Z" fill="#CFE9FF" {s()}/>
<circle cx="37" cy="84" r="3.5" fill="{SKIN}" {s('stroke-width="2"')}/><circle cx="91" cy="84" r="3.5" fill="{SKIN}" {s('stroke-width="2"')}/>
<path d="M50 66 L38 82 M78 66 L90 82" {ln(SKIN, 4)}/>
<circle cx="64" cy="46" r="14" fill="{SKIN}" {s()}/>
<path d="M50 44 Q52 30 64 31 Q76 30 78 44 Q70 36 64 38 Q58 36 50 44Z" fill="#C8894E" {s('stroke-width="2.2"')}/>
{eye(59, 47, 0.5)}{eye(69, 47, 0.5)}<path d="M61 54 Q64 56 67 54" fill="none" {ln(O, 1.8)}/>
<ellipse cx="55" cy="51" rx="3" ry="1.8" fill="#FF8FB0" opacity=".6"/><ellipse cx="73" cy="51" rx="3" ry="1.8" fill="#FF8FB0" opacity=".6"/>
<path d="M64 30 Q48 14 42 26 Q46 34 64 30Z M64 30 Q80 14 86 26 Q82 34 64 30Z" fill="#fff" {s()}/>
<circle cx="64" cy="30" r="4" fill="#fff" {s('stroke-width="2.4"')}/>
{sparkle(18, 70, 4)}{sparkle(110, 64, 3.5)}
'''))

# 3 Студия балета Ксении Малеевой (балет с 2 лет): большой пуант-мама учит маленький пуант стоять на носочке
def _pointe(x, y, k, ang, fill, inner):
    return f'''<g transform="translate({x} {y}) rotate({ang}) scale({k})">
<path d="M-40 -2 Q-42 -14 -28 -16 L18 -16 Q34 -16 38 -6 Q40 4 28 8 L-30 10 Q-40 10 -40 -2Z" fill="{fill}" {s()}/>
<path d="M-30 -14 Q-8 -24 14 -14 Q-8 -8 -30 -14Z" fill="{inner}" {s('stroke-width="2.4"')}/>
<path d="M24 -14 Q30 -4 26 6" fill="none" stroke="#E98E7A" stroke-width="2"/>
<path d="M-36 6 Q0 12 30 6" fill="none" stroke="#E98E7A" stroke-width="2"/>
</g>'''


I["maleeva-ballet-vysotny"] = ("большой персиковый атласный пуант-мама с лентами и крошечный пуант-малыш",
    "мама-пуант стоит на пятачке носка и придерживает лентой малыша, который впервые встаёт на носочек на паркете", bg("#FFF0E6", "#E0706A", f'''
<path d="M0 108 H128 V128 H0Z" fill="#C98E5C"/><path d="M0 116 H128 M30 108 V128 M70 108 V128 M104 108 V128" stroke="#A8703F" stroke-width="2"/>
<path d="M44 36 Q70 20 90 40 Q100 52 96 72" fill="none" {ln(O, 6)}/><path d="M44 36 Q70 20 90 40 Q100 52 96 72" fill="none" {ln("#FF8FB0", 3.5)}/>
<path d="M40 40 Q18 34 14 56 Q14 70 22 76" fill="none" {ln(O, 6)}/><path d="M40 40 Q18 34 14 56 Q14 70 22 76" fill="none" {ln("#FF8FB0", 3.5)}/>
{_pointe(46, 70, 1.0, 72, "#FFC1AE", "#B9564A")}
{eye(42, 74, 0.55)}{eye(54, 74, 0.55)}<path d="M44 81 Q48 84 52 81" fill="none" {ln(O, 2)}/>
<ellipse cx="38" cy="80" rx="3" ry="1.8" fill="#FF7FA8" opacity=".6"/><ellipse cx="58" cy="80" rx="3" ry="1.8" fill="#FF7FA8" opacity=".6"/>
{_pointe(96, 92, 0.42, 78, "#FFD3C6", "#B9564A")}
{eye(94, 92, 0.36)}{eye(99, 92, 0.36)}
{sparkle(110, 24, 4.5)}{sparkle(20, 20, 3)}{sparkle(116, 52, 2.6)}
'''))

# 4 Школа танцев Александра Макарова (хип-хоп, брейк, K-pop с 4 лет): худи танцует «робота»
I["makarov-dance-marksistsky"] = ("неоново-зелёная толстовка-худи с мордашкой в капюшоне",
    "танцует «робота» — руки-рукава согнуты под прямым углом, на тёмном танцполе из светящихся разноцветных квадратов", bg("#4B3F8F", "#16123A", f'''
<g opacity=".9">
<rect x="0" y="100" width="32" height="28" fill="#FF4FA3"/><rect x="32" y="100" width="32" height="28" fill="#2FD4FF"/>
<rect x="64" y="100" width="32" height="28" fill="#FFE14F"/><rect x="96" y="100" width="32" height="28" fill="#7CFF6B"/>
</g>
<path d="M0 100 H128 M32 100 V128 M64 100 V128 M96 100 V128" stroke="#16123A" stroke-width="3"/>
<path d="M50 84 L48 100 M78 84 L82 100" {ln(O, 9)}/><path d="M50 84 L48 100 M78 84 L82 100" {ln("#2A2F45", 6)}/>
<path d="M42 54 Q64 46 86 54 L84 88 H44Z" fill="#7CFF6B" {s()}/>
<path d="M54 74 H74 V84 H54Z" fill="#5BD94C" {s('stroke-width="2.2"')}/>
<path d="M44 58 L22 60 L22 38" fill="none" {ln(O, 13)}/><path d="M44 58 L22 60 L22 38" fill="none" {ln("#7CFF6B", 9)}/>
<path d="M84 58 L106 70 L106 92" fill="none" {ln(O, 13)}/><path d="M84 58 L106 70 L106 92" fill="none" {ln("#7CFF6B", 9)}/>
<rect x="16" y="28" width="12" height="9" rx="3" fill="{SKIN}" {s('stroke-width="2.2"')}/>
<rect x="100" y="92" width="12" height="9" rx="3" fill="{SKIN}" {s('stroke-width="2.2"')}/>
<path d="M44 38 Q44 14 64 14 Q84 14 84 38 Q84 56 64 56 Q44 56 44 38Z" fill="#7CFF6B" {s()}/>
<ellipse cx="64" cy="38" rx="13" ry="13" fill="#2A2F45" {s('stroke-width="2.4"')}/>
<ellipse cx="64" cy="39" rx="10" ry="10" fill="{SKIN}"/>
{eye(60, 38, 0.45)}{eye(68, 38, 0.45)}<path d="M61 44 Q64 46 67 44" fill="none" {ln(O, 1.6)}/>
<path d="M58 56 L56 66 M70 56 L72 66" {ln("#F4F4F4", 2.4)}/>
{sparkle(108, 22, 4, "#FFE14F")}{sparkle(18, 84, 3.5, "#2FD4FF")}
'''))

# 5 «Дети райка» (театральная студия 6–17): мальчик на самой верхней галёрке («раёк») машет программкой
I["deti-rayka-michurinsky"] = ("мальчик в синей бархатной кепке-восьмиклинке на самой верхней галёрке театра",
    "свесился через золочёные перила райка и машет театральной программкой, а далеко внизу открывается красный занавес", bg("#4A1020", "#1B0510", f'''
<path d="M10 128 V96 Q64 70 118 96 V128Z" fill="#D02B3A" {s()}/>
<path d="M30 128 V92 M50 128 V84 M78 128 V84 M98 128 V92" stroke="#9E1726" stroke-width="3"/>
<path d="M44 128 Q64 106 84 128Z" fill="#FFE7A3" opacity=".8"/>
<path d="M0 58 H128 V68 H0Z" fill="#E3B341" {s()}/>
<path d="M8 68 V84 M24 68 V84 M40 68 V84 M88 68 V84 M104 68 V84 M120 68 V84" {ln("#E3B341", 4)}/>
<path d="M0 84 H128" {ln(O, 5)}/><path d="M0 84 H128" {ln("#E3B341", 2.5)}/>
<path d="M48 58 Q48 44 64 42 Q80 44 80 58Z" fill="#2E5FB8" {s()}/>
<circle cx="64" cy="36" r="13" fill="{SKIN}" {s()}/>
<path d="M50 32 Q52 20 66 20 Q80 21 80 32 L86 34 Q78 36 50 32Z" fill="#2E5FB8" {s('stroke-width="2.4"')}/>
<circle cx="66" cy="21" r="2.4" fill="#2E5FB8" {s('stroke-width="1.6"')}/>
{eye(59, 37, 0.5)}{eye(69, 37, 0.5)}<path d="M60 43 Q64 47 68 43" fill="none" {ln(O, 2)}/>
{limb(78, 54, 98, 34, "#2E5FB8", 6)}
<g transform="rotate(18 104 24)"><rect x="96" y="10" width="18" height="24" rx="2" fill="#FFF8E7" {s('stroke-width="2.4"')}/>
<path d="M100 17 H110 M100 22 H110 M100 27 H106" stroke="#C0392B" stroke-width="2"/></g>
{limb(50, 54, 40, 62, "#2E5FB8", 6)}
{sparkle(20, 22, 3.5, "#FFE7A3")}{sparkle(30, 44, 2.4, "#FFE7A3")}
'''))

# 6 «Акт Плэйс» на Ленинском (театральная студия 3–11): софит светит на пустой табурет — сцена ждёт актёра
I["act-place-leninsky"] = ("круглый бирюзовый театральный прожектор-фонарь с мордашкой на крюке",
    "висит под колосниками и направляет конус тёплого света на маленький деревянный табурет посреди пустой сцены", bg("#2B3A55", "#0F1726", f'''
<path d="M70 40 L30 112 H118 L92 40Z" fill="#FFE9A8" opacity=".35"/>
<ellipse cx="74" cy="112" rx="40" ry="8" fill="#FFE9A8" opacity=".6"/>
<path d="M0 116 H128 V128 H0Z" fill="#6B4A2E"/>
<path d="M62 96 H86 M66 96 L62 114 M82 96 L86 114 M64 106 H84" {ln(O, 6)}/>
<path d="M62 96 H86 M66 96 L62 114 M82 96 L86 114 M64 106 H84" {ln("#C88B52", 3.5)}/>
<path d="M0 8 H128" {ln("#8A93A3", 5)}/>
<path d="M44 8 V18" {ln(O, 4)}/><path d="M34 22 Q44 14 54 22" fill="none" {ln(O, 4)}/>
<g transform="rotate(-30 46 40)">
<rect x="28" y="22" width="36" height="34" rx="10" fill="#2BB3B1" {s()}/>
<ellipse cx="46" cy="58" rx="16" ry="5" fill="#FFF3C4" {s('stroke-width="2.6"')}/>
{face(46, 38, 7, 0.6)}
<path d="M30 30 H22 M30 46 H22" {ln(O, 4)}/>
</g>
{sparkle(108, 24, 4, "#FFE9A8")}{sparkle(18, 70, 3, "#FFE9A8")}
'''))

# 7 «Акт Плэйс» на Люблинской (театральная студия 3,5–11): пальчиковый лисёнок выглядывает из-за ширмы
I["act-place-lyublinskaya"] = ("рыжий пальчиковый лисёнок-кукла с белой грудкой на детском пальчике",
    "выглядывает из-за синей ширмы кукольного театра, расшитой жёлтыми звёздами, и кланяется зрителям", bg("#FFF6D6", "#F2A93B", f'''
<path d="M14 72 H114 V128 H14Z" fill="#2747A8" {s()}/>
<path d="M14 72 H114 V82 H14Z" fill="#1B3483" {s('stroke-width="2.6"')}/>
<g fill="#FFD84A">{''.join(sparkle(x, y, r, "#FFD84A") for x, y, r in ((32, 98, 5), (60, 112, 4), (92, 100, 5.5), (104, 120, 3.5), (26, 120, 3)))}</g>
<path d="M54 80 V58 Q54 52 64 52 Q74 52 74 58 V80" fill="{SKIN}" {s()}/>
<path d="M48 60 Q46 36 64 30 Q82 36 80 60 Q72 66 64 66 Q56 66 48 60Z" fill="#F07A22" {s()}/>
<path d="M56 60 Q64 48 72 60 Q64 66 56 60Z" fill="#fff" {s('stroke-width="2.2"')}/>
<path d="M50 38 L46 18 L60 30Z M78 38 L82 18 L68 30Z" fill="#F07A22" {s()}/>
<path d="M50 32 L48 24 L55 30Z M78 32 L80 24 L73 30Z" fill="#3B2A2A"/>
{eye(58, 44, 0.55)}{eye(70, 44, 0.55)}<ellipse cx="64" cy="51" rx="3" ry="2.2" fill="{O}"/>
<ellipse cx="53" cy="50" rx="3" ry="1.8" fill="#FF8FB0" opacity=".6"/><ellipse cx="75" cy="50" rx="3" ry="1.8" fill="#FF8FB0" opacity=".6"/>
<path d="M18 44 Q24 38 30 44 M98 44 Q104 38 110 44" fill="none" {ln("#C0661A", 3)}/>
'''))

# 8 Театральная лаборатория «Зерно» (7–17): пшеничное зёрнышко в жабо кланяется, под ним пробивается росток
I["zerno-lyublinskaya"] = ("золотое пшеничное зёрнышко в белом кружевном театральном жабо",
    "низко кланяется на краю сцены, а из щели между досками под ним пробивается зелёный росток с двумя листиками", bg("#EAF7E1", "#4E8F3A", f'''
<path d="M0 104 H128 V128 H0Z" fill="#9C6B3F"/><path d="M0 104 H128 M40 104 V128 M88 104 V128" stroke="#7A4F2A" stroke-width="2.4"/>
<path d="M64 104 Q60 92 66 84" fill="none" {ln(O, 5)}/><path d="M64 104 Q60 92 66 84" fill="none" {ln("#4CAF50", 3)}/>
<path d="M65 88 Q54 80 48 86 Q56 94 65 88Z M66 86 Q76 76 84 82 Q76 92 66 86Z" fill="#7CD26E" {s('stroke-width="2.2"')}/>
<g transform="rotate(28 64 54)">
<path d="M64 14 Q86 26 86 54 Q84 82 64 88 Q44 82 42 54 Q42 26 64 14Z" fill="#F2B83A" {s()}/>
<path d="M64 20 Q60 50 64 82" fill="none" {ln("#C98A1E", 2.4)}/>
<path d="M44 66 Q50 74 56 66 Q60 76 64 68 Q68 76 72 66 Q78 74 84 66 Q78 82 64 82 Q50 82 44 66Z" fill="#fff" {s('stroke-width="2.4"')}/>
{face(64, 48, 8, 0.65)}
</g>
{limb(40, 70, 26, 84, "#F2B83A", 4)}{limb(88, 78, 104, 68, "#F2B83A", 4)}
{sparkle(108, 26, 4.5)}{sparkle(20, 30, 3.5)}{sparkle(112, 46, 2.5)}
'''))

# 9 «Прорисунок» (рисунок, живопись, скульптура 4–17): деревянный манекен-человечек позирует, рядом его набросок
I["prorisunok-tyumensky"] = ("деревянный художественный манекен-человечек на шарнирах",
    "позирует на круглой подставке, подняв руку как в приветствии, а рядом на приколотом листе — его набросок углём", bg("#F6EEDF", "#B9925C", f'''
<rect x="70" y="18" width="46" height="62" rx="2" fill="#fff" transform="rotate(6 93 49)" {s()}/>
<circle cx="78" cy="22" r="3" fill="#E53935" {s('stroke-width="1.6"')}/>
<g transform="rotate(6 93 49)" fill="none" stroke="#3A3A3A" stroke-width="1.8" stroke-linecap="round">
<circle cx="94" cy="32" r="5"/><path d="M94 37 V56 M94 42 L104 32 M94 42 L86 50 M94 56 L88 70 M94 56 L100 70"/>
<path d="M80 74 Q94 70 108 74" stroke-width="1.2"/></g>
<ellipse cx="42" cy="114" rx="22" ry="6" fill="#8C5A2B" {s()}/>
<path d="M42 108 V96" {ln(O, 6)}/><path d="M42 108 V96" {ln("#C98E5C", 3)}/>
<g fill="#E8B77D" {s('stroke-width="2.6"')}>
<ellipse cx="34" cy="86" rx="5" ry="11" transform="rotate(12 34 86)"/><ellipse cx="50" cy="86" rx="5" ry="11" transform="rotate(-12 50 86)"/>
<ellipse cx="42" cy="58" rx="12" ry="16"/>
<ellipse cx="26" cy="60" rx="4.5" ry="10" transform="rotate(30 26 60)"/>
<ellipse cx="60" cy="36" rx="4.5" ry="10" transform="rotate(30 60 36)"/>
<ellipse cx="42" cy="30" rx="10" ry="11"/>
</g>
<g fill="#C98E5C" {s('stroke-width="2"')}><circle cx="42" cy="74" r="4"/><circle cx="54" cy="46" r="3.5"/><circle cx="30" cy="46" r="3.5"/></g>
{eye(38, 30, 0.45)}{eye(46, 30, 0.45)}<path d="M39 36 Q42 38 45 36" fill="none" {ln(O, 1.6)}/>
<path d="M12 24 L22 14" {ln(O, 6)}/><path d="M12 24 L22 14" {ln("#2B2B2B", 3)}/>
'''))

# 10 Art Libre (русско-французская школа живописи, дети 5–14): матрёшка-художница пишет Эйфелеву башню
I["art-libre-mosfilmovskaya"] = ("матрёшка-художница в красном платке с васильками и синем берете поверх платка",
    "пишет кисточкой Эйфелеву башню на маленьком холсте, стоящем на коротком настольном этюднике", bg("#E8EEFF", "#5A6FD6", f'''
<path d="M0 110 H128 V128 H0Z" fill="#8FA3E8"/>
<path d="M76 108 L80 92 M108 108 L104 92" {ln(O, 5)}/><path d="M76 108 L80 92 M108 108 L104 92" {ln("#B07A43", 3)}/>
<rect x="72" y="40" width="42" height="52" rx="2" fill="#FFFDF6" {s()}/>
<path d="M93 48 L84 86 M93 48 L102 86 M87 74 H99 M89 64 H97 M84 86 Q93 78 102 86" fill="none" stroke="#3A3A5A" stroke-width="2.2" stroke-linecap="round"/>
<path d="M76 88 H110" {ln("#7CC36E", 3)}/>
<path d="M18 112 Q14 80 26 66 Q22 50 40 44 Q58 50 54 66 Q66 80 62 112Z" fill="#E53935" {s()}/>
<ellipse cx="40" cy="92" rx="14" ry="12" fill="#FFF3E0" {s('stroke-width="2.4"')}/>
<g fill="#3F6BD6">{''.join(f'<circle cx="{x}" cy="{y}" r="2.6"/>' for x, y in ((34, 88), (46, 88), (40, 96), (33, 98), (47, 98)))}</g>
<circle cx="40" cy="64" r="11" fill="{SKIN}" {s()}/>
{eye(36, 64, 0.45)}{eye(44, 64, 0.45)}<path d="M37 70 Q40 72 43 70" fill="none" {ln(O, 1.6)}/>
<ellipse cx="33" cy="68" rx="2.6" ry="1.6" fill="#FF6B6B" opacity=".7"/><ellipse cx="47" cy="68" rx="2.6" ry="1.6" fill="#FF6B6B" opacity=".7"/>
<ellipse cx="42" cy="44" rx="15" ry="6" fill="#2E3E9E" {s()}/><path d="M42 38 V34" {ln(O, 3)}/>
<path d="M54 82 L76 66" {ln(O, 6)}/><path d="M54 82 L76 66" {ln("#E8B77D", 3)}/>
<path d="M75 67 L82 62" {ln("#3F6BD6", 5)}/>
{sparkle(108, 22, 4)}{sparkle(16, 30, 3)}
'''))


if __name__ == "__main__":
    for pid, (hero, scene, svg_) in I.items():
        open(os.path.join(ROOT, "icons-src", pid + ".svg"), "w").write(svg_)
    if "--subjects" in sys.argv:
        p = os.path.join(ROOT, "icons-src", "subjects.txt")
        have = open(p, encoding="utf-8").read()
        with open(p, "a", encoding="utf-8") as f:
            for pid, (hero, scene, _) in I.items():
                if not any(l.startswith(pid + " — ") for l in have.splitlines()):
                    f.write(f"{pid} — герой: {hero} | сцена: {scene}\n")
    print(len(I))
