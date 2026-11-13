"""Иконки робота pools, 2026-11-13 (02 UTC). Каждая придумана и нарисована отдельно (правило абсолютной
уникальности): свой герой, своя сцена, своя компоновка и палитра. Герои проверены по реестру icons-src/subjects.txt
(ни одного такого героя раньше не было), картинки — tools/check_unique.py.
Запуск: python3 tools/icons_pools_1113c.py [id …]  → python3 tools/render_icons.py <id…> → python3 tools/check_unique.py <id…>."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, sparkle, O
from icons_pools_1112b import W, bub, T2

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
T3 = 'stroke-width="2"'


def rope(x0, y0, x1, y1, n, r=5.2, c1="#F0483E", c2="#FFFFFF"):
    """Разделительная дорожка: поплавки двух цветов по прямой."""
    out = f'<path d="M{x0} {y0} L{x1} {y1}" stroke="{O}" stroke-width="2.4"/>'
    for i in range(n):
        t = i / (n - 1)
        out += (f'<circle cx="{x0 + (x1 - x0) * t:.1f}" cy="{y0 + (y1 - y0) * t:.1f}" r="{r}" '
                f'fill="{c1 if i % 2 == 0 else c2}" {s(T3)}/>')
    return out


# 1. «Территория Фитнеса», Братиславская — большой бассейн с морской водой: морская рыба-хирург на дорожке
ICONS["tswim-bratislavskaya"] = W("#DDF8FF", "#2C9FDB", f'''
{rope(-4, 30, 132, 14, 12)}{rope(-4, 116, 132, 100, 12)}
<path d="M30 64 L6 44 Q14 64 6 86Z" fill="#FFD23F" {s()}/>
<ellipse cx="68" cy="65" rx="40" ry="26" fill="#2E63E6" {s()}/>
<path d="M44 50 Q70 36 92 52 Q76 56 70 66 Q62 80 40 78 Q58 70 56 60 Q52 52 44 50Z" fill="#231F3D"/>
<path d="M60 40 Q72 30 86 42" fill="#FFD23F" {s(T2)}/>
<path d="M62 76 Q54 92 70 88 Q74 82 72 76Z" fill="#FFD23F" {s(T2)}/>
<path d="M78 46 Q96 34 108 56 Q98 50 80 54Z" fill="#FFE46B" {s(T2)}/>
{eye(92, 62, 1.15)}
<path d="M98 72 Q103 76 107 70" fill="none" {s('stroke-width="2.6"')}/>
<ellipse cx="88" cy="74" rx="4.6" ry="2.8" fill="#FF7FA8" opacity=".8"/>
{bub(116, 40, 5)}{bub(120, 28, 3)}
''', 30, 20)
SUBJ["tswim-bratislavskaya"] = ("синяя рыба-хирург с чёрным узором и жёлтым хвостом, в жёлтой плавательной шапочке",
                                "плывёт по своей дорожке морского бассейна между двумя канатами из красно-белых поплавков")

# 2. «ГрудничОк», Коммунарка — персональные занятия «инструктор плюс малыш» с 2 месяцев
ICONS["grudnichok-kommunarka"] = W("#FFF1E0", "#FFB38A", f'''
<path d="M-6 70 Q14 62 30 70 T62 70 T94 70 T134 70 V134 H-6Z" fill="#7FD8F2" {s('stroke-width="2.6"')}/>
<path d="M12 96 Q22 91 32 96 M84 108 Q94 103 104 108 M40 114 Q50 109 60 114" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
<path d="M134 4 L96 -6 Q70 18 62 46 Q58 58 68 60 Q78 60 84 48 Q96 28 134 34Z" fill="#FFD9BC" {s()}/>
<path d="M64 50 Q68 44 74 46" fill="none" {s(T2)}/>
<path d="M58 62 Q34 60 30 82 Q28 102 48 106 Q66 108 68 92" fill="none" stroke="{O}" stroke-width="21" stroke-linecap="round"/>
<path d="M58 62 Q34 60 30 82 Q28 102 48 106 Q66 108 68 92" fill="none" stroke="#FF9FB2" stroke-width="15" stroke-linecap="round"/>
<path d="M30 76 H44 M29 88 H43 M36 100 L46 92 M52 106 L56 94" fill="none" stroke="#F0708C" stroke-width="2.4" stroke-linecap="round"/>
<path d="M70 98 L82 106 L72 110 L84 116" fill="none" {s(T2)}/>
<circle cx="56" cy="60" r="16" fill="#FFB3C1" {s()}/>
<path d="M40 60 Q38 40 58 42 Q74 44 72 60 Q64 50 54 52 Q46 54 40 60Z" fill="#FFFFFF" {s(T2)}/>
<path d="M40 62 Q36 70 42 74" fill="none" {s(T2)}/>
<circle cx="58" cy="41" r="3.6" fill="#7FD8F2" {s(T3)}/>
<path d="M62 46 Q72 30 66 22 M68 48 Q82 38 84 30" fill="none" {s(T3)}/>
{eye(52, 62, .9)}{eye(63, 61, .9)}
<path d="M54 69 Q58 73 62 68" fill="none" {s('stroke-width="2.2"')}/>
<ellipse cx="46" cy="68" rx="3.2" ry="2" fill="#FF5E86" opacity=".7"/>
{bub(100, 84, 5)}{bub(110, 96, 3.4)}{bub(18, 110, 4)}
''', 30, 24)
SUBJ["grudnichok-kommunarka"] = ("крошечный розовый рачок-криль в белом чепчике",
                                 "учится плавать в тёплой неглубокой чаше и держится усиками за большой палец инструктора")

# 3. «Китёнок», Производственная ул. (Солнцево) — солнце пришло поплавать
ICONS["kitenok-proizvodstvennaya"] = W("#FFEAF2", "#FF8FB0", f'''
<g {s(T2)} fill="#FFB52E">
<path d="M64 4 L72 22 H56Z"/><path d="M26 16 L42 28 L32 38Z"/><path d="M102 16 L86 28 L96 38Z"/>
<path d="M6 50 L26 48 L24 62Z"/><path d="M122 50 L102 48 L104 62Z"/>
</g>
<circle cx="64" cy="62" r="34" fill="#FFD83D" {s()}/>
<path d="M30 54 H98" {s('stroke-width="5"')}/>
<rect x="38" y="44" width="22" height="18" rx="8" fill="#3BC3F2" {s()}/><rect x="68" y="44" width="22" height="18" rx="8" fill="#3BC3F2" {s()}/>
<path d="M43 50 Q47 46 52 48 M73 50 Q77 46 82 48" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<path d="M52 72 Q64 84 76 72" fill="#fff" {s('stroke-width="2.6"')}/>
<ellipse cx="40" cy="72" rx="5" ry="3" fill="#FF7FA8" opacity=".8"/><ellipse cx="88" cy="72" rx="5" ry="3" fill="#FF7FA8" opacity=".8"/>
<path d="M-6 84 Q10 76 26 84 T58 84 T90 84 T134 84 V134 H-6Z" fill="#22B8C9" {s('stroke-width="2.6"')}/>
<path d="M14 104 Q24 99 34 104 M82 110 Q92 105 102 110 M48 118 Q58 113 68 118" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".75"/>
<path d="M18 78 Q10 66 18 62 M108 78 Q118 66 110 62 M8 82 Q0 76 4 70 M120 82 Q128 76 124 70" fill="none" stroke="#fff" stroke-width="4.4" stroke-linecap="round"/>
''', 50, 14)
SUBJ["kitenok-proizvodstvennaya"] = ("жёлтое солнце в голубых плавательных очках",
                                     "по пояс сидит в бирюзовой воде детского бассейна и плещется так, что летят брызги")

# 4. «Буду плыть», бассейн МГПУ — детская малая чаша глубиной 0,7 м
ICONS["budu-plyt-mgpu"] = W("#F3EAFF", "#8F73E6", f'''
<path d="M-6 44 Q12 37 28 44 T60 44 T92 44 T134 44 V134 H-6Z" fill="#9BE7F5" opacity=".9" {s('stroke-width="2.6"')}/>
<rect x="96" y="20" width="26" height="58" rx="4" fill="#fff" {s(T2)}/>
<path d="M96 36 H108 M96 52 H104 M96 66 H108" {s(T2)}/>
<text x="110" y="34" font-family="Arial" font-weight="700" font-size="9" fill="{O}" text-anchor="middle">0,7</text>
<g fill="#F2B880" {s(T2)}>
<path d="M30 92 q-4 12 -10 12"/><path d="M46 98 q-2 12 -8 14"/><path d="M62 98 q2 12 8 14"/><path d="M78 92 q6 10 12 10"/>
</g>
<path d="M22 78 Q20 56 44 54 Q70 50 88 60 Q100 68 96 82 Q90 100 60 100 Q26 102 22 78Z" fill="#FFD3A1" {s()}/>
<path d="M42 55 Q40 78 44 100 M58 53 Q58 78 60 100 M74 55 Q76 78 76 98" fill="none" stroke="#E9A56B" stroke-width="2.4" stroke-linecap="round"/>
<g fill="#F2B880" {s(T2)}>
<path d="M34 98 q-6 12 -12 14 q-4 2 -2 6 q8 2 14 -4 q6 -8 8 -14Z"/><path d="M50 100 q-2 14 -6 18 q-2 4 2 6 q8 -2 10 -10 q2 -8 2 -14Z"/>
<path d="M66 100 q2 14 6 18 q2 4 6 2 q4 -6 0 -12 q-4 -6 -6 -10Z"/><path d="M82 96 q6 10 12 12 q4 2 6 -2 q0 -8 -8 -12 q-4 -2 -6 -4Z"/>
</g>
<path d="M74 68 H98" {s('stroke-width="4.4"')}/>
<rect x="70" y="62" width="13" height="12" rx="5.5" fill="#FF6B5E" {s(T2)}/><rect x="86" y="64" width="12" height="11" rx="5" fill="#FF6B5E" {s(T2)}/>
<path d="M84 84 Q90 90 96 84" fill="none" {s('stroke-width="2.4"')}/>
<ellipse cx="76" cy="84" rx="4" ry="2.4" fill="#FF7FA8" opacity=".8"/>
{bub(16, 60, 4.4)}{bub(10, 74, 3)}{bub(112, 94, 4)}
''', 34, 16)
SUBJ["budu-plyt-mgpu"] = ("пухлая тихоходка — «водяной медвежонок» на восьми лапках, в красных плавательных очках",
                          "гребёт всеми лапками по мелкой детской чаше мимо отметки глубины «0,7» на белой рейке")

# 5. «Триумф», бассейн МГПУ — победное касание финишной панели
ICONS["triumf-mgpu"] = W("#D2FFF6", "#11A39B", f'''
<path d="M-6 96 Q10 88 26 96 T58 96 T90 96 T134 96 V134 H-6Z" fill="#0C7F86" opacity=".55"/>
<g transform="rotate(8 78 60)">
<rect x="46" y="22" width="66" height="78" rx="6" fill="#FFD21F" {s()}/>
<rect x="46" y="22" width="66" height="12" rx="6" fill="#2B2745" {s(T2)}/>
<path d="M56 46 H102 M56 88 H102" stroke="#E0A800" stroke-width="3" stroke-linecap="round" stroke-dasharray="1 7"/>
<text x="80" y="82" font-family="Arial" font-weight="700" font-size="38" fill="#2B2745" text-anchor="middle">1</text>
</g>
<path d="M-8 92 Q14 74 34 66" fill="none" stroke="{O}" stroke-width="22" stroke-linecap="round"/>
<path d="M-8 92 Q14 74 34 66" fill="none" stroke="#FFD2B0" stroke-width="16" stroke-linecap="round"/>
<path d="M30 54 Q34 44 44 48 L60 54 Q66 58 62 64 L50 78 Q40 84 32 76Z" fill="#FFD2B0" {s()}/>
<path d="M44 48 L52 38 M52 51 L64 44 M58 56 L70 54 M40 50 L40 40" fill="none" stroke="{O}" stroke-width="10" stroke-linecap="round"/>
<path d="M44 48 L52 38 M52 51 L64 44 M58 56 L70 54 M40 50 L40 40" fill="none" stroke="#FFD2B0" stroke-width="5" stroke-linecap="round"/>
<path d="M62 30 L58 18 M72 34 L78 22 M40 30 L34 20 M28 44 L16 40 M70 70 L82 74" fill="none" stroke="#fff" stroke-width="4.4" stroke-linecap="round"/>
{sparkle(22, 26, 7)}{sparkle(112, 110, 6)}
<circle cx="50" cy="20" r="3" fill="#fff"/><circle cx="20" cy="56" r="2.6" fill="#fff"/>
''', 24, 18)
SUBJ["triumf-mgpu"] = ("жёлтая финишная панель-сенсор на стенке бассейна с большой цифрой «1»",
                       "мокрая ладошка пловца шлёпает по ней первой — во все стороны летят брызги")

# 6. Brain Sport, «Косино» — два часа: сначала зал, потом бассейн
ICONS["brain-sport-kosino"] = W("#FFF6D8", "#F29A2E", f'''
<path d="M-6 30 Q10 23 26 30 T58 30 T90 30 T134 30 V134 H-6Z" fill="#3FA9E8" {s('stroke-width="2.6"')}/>
<path d="M-6 108 H134 V134 H-6Z" fill="#E8D9A6" {s(T2)}/>
<path d="M20 108 V134 M48 108 V134 M78 108 V134 M106 108 V134" stroke="#C9B77A" stroke-width="2"/>
<path d="M36 58 L18 44 Q22 62 16 80Z" fill="#8FA63A" {s()}/>
<path d="M50 44 L56 28 L64 40 L72 26 L78 42 L88 32 L90 48Z" fill="#B7C94E" {s(T2)}/>
<path d="M30 64 Q44 40 78 44 Q108 48 114 66 Q106 86 76 88 Q44 90 30 64Z" fill="#C8D65A" {s()}/>
<path d="M50 48 Q46 62 52 82 M64 45 Q60 62 66 86 M78 45 Q74 62 80 87" fill="none" stroke="#5E7A22" stroke-width="5" stroke-linecap="round" opacity=".8"/>
<path d="M88 46 Q84 54 86 62" fill="none" stroke="#E5332B" stroke-width="6.4" stroke-linecap="round"/>
<path d="M84 44 L76 36 M86 42 L82 32" stroke="#E5332B" stroke-width="3.4" stroke-linecap="round"/>
{eye(98, 60, 1.05)}
<path d="M102 72 Q107 76 111 70" fill="none" {s('stroke-width="2.6"')}/>
<ellipse cx="92" cy="72" rx="4.4" ry="2.6" fill="#FF7FA8" opacity=".8"/>
<path d="M68 80 Q72 96 86 96" fill="none" stroke="{O}" stroke-width="11" stroke-linecap="round"/>
<path d="M68 80 Q72 96 86 96" fill="none" stroke="#B7C94E" stroke-width="5.6" stroke-linecap="round"/>
<path d="M74 98 H104" {s('stroke-width="4.6"')}/>
<rect x="66" y="88" width="10" height="20" rx="3.4" fill="#4A4763" {s(T2)}/><rect x="102" y="88" width="10" height="20" rx="3.4" fill="#4A4763" {s(T2)}/>
{bub(118, 46, 4.4)}{bub(110, 36, 3)}{bub(24, 94, 3.6)}
''', 60, 10)
SUBJ["brain-sport-kosino"] = ("полосатый зелёный судак в красной налобной повязке",
                              "на дне бассейна поднимает плавником чёрную гантель — разминка перед заплывом")

# 7. «Территория Фитнеса», Жулебино — стартовая тумба ждёт пловца
ICONS["tswim-zhulebino"] = W("#FFF3C7", "#FFA94D", f'''
<path d="M-6 92 Q10 84 26 92 T58 92 T90 92 T134 92 V134 H-6Z" fill="#2EC4D6" {s('stroke-width="2.6"')}/>
<path d="M84 112 Q94 107 104 112 M12 116 Q22 111 32 116" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
<path d="M22 100 V62 L26 40 L84 28 L86 100Z" fill="#FFFFFF" {s()}/>
<path d="M24 44 L84 30 L92 22 L30 34Z" fill="#3A66E0" {s()}/>
<path d="M22 100 H86 V112 H22Z" fill="#B9C3D9" {s(T2)}/>
<rect x="56" y="64" width="24" height="26" rx="4" fill="#3A66E0" {s(T2)}/>
<text x="68" y="85" font-family="Arial" font-weight="700" font-size="22" fill="#fff" text-anchor="middle">1</text>
{eye(36, 58, 1.05)}{eye(54, 54, 1.05)}
<path d="M40 70 Q46 76 52 68" fill="none" {s('stroke-width="2.6"')}/>
<ellipse cx="30" cy="68" rx="4" ry="2.6" fill="#FF7FA8" opacity=".8"/>
<path d="M86 52 Q98 48 104 58" fill="none" {s()}/>
<path d="M98 54 H122 V84 Q110 80 98 84Z" fill="#FF6FA3" {s(T2)}/>
<path d="M98 62 H122 M98 72 H122" stroke="#fff" stroke-width="3"/>
<circle cx="106" cy="100" r="11" fill="#FFD2B0" {s()}/>
<path d="M95 98 Q96 86 106 87 Q116 86 117 98 Q106 92 95 98Z" fill="#8E5BD9" {s(T2)}/>
{eye(102, 102, .7)}{eye(110, 102, .7)}
<path d="M103 107 Q106 110 109 107" fill="none" {s(T3)}/>
''', 26, 16)
SUBJ["tswim-zhulebino"] = ("белая стартовая тумба с синей площадкой, номером «1» и мордашкой",
                           "стоит у кромки воды и протягивает розовое полотенце малышу, который доплыл до бортика")

# 8. «Территория Фитнеса», Кожухово — учимся нырять
ICONS["tswim-kozhukhovo"] = W("#FFE3EC", "#F06C9B", f'''
<path d="M-6 50 H134 V134 H-6Z" fill="#0F7F8C"/>
<path d="M-6 50 Q10 43 26 50 T58 50 T90 50 T134 50 V60 H-6Z" fill="#35B7C4" {s('stroke-width="2.6"')}/>
<path d="M40 50 Q44 20 62 26 Q66 38 62 50Z" fill="#6B4A36" {s()}/>
<path d="M66 50 L70 26 M76 50 L84 30" fill="none" {s()}/>
<path d="M70 26 L62 18 M70 26 L72 14 M70 26 L80 20" stroke="#FF9A2E" stroke-width="5" stroke-linecap="round"/>
<path d="M84 30 L78 20 M84 30 L88 18 M84 30 L96 26" stroke="#FF9A2E" stroke-width="5" stroke-linecap="round"/>
<path d="M40 54 Q30 70 46 82 Q64 90 72 74 Q76 60 66 54Z" fill="#F4EDE2" {s()}/>
<path d="M56 80 Q54 98 66 104" fill="none" stroke="{O}" stroke-width="15" stroke-linecap="round"/>
<path d="M56 80 Q54 98 66 104" fill="none" stroke="#F4EDE2" stroke-width="9" stroke-linecap="round"/>
<path d="M58 96 L44 92 L50 104 L40 110 L56 114 L60 124 L70 112Z" fill="#C8552B" {s(T2)}/>
<circle cx="72" cy="106" r="13" fill="#F4EDE2" {s()}/>
<path d="M60 100 Q62 88 72 90 L68 80 L78 88 L84 80 L84 96 Q78 92 60 100Z" fill="#3D3350" {s(T2)}/>
<path d="M84 106 L102 110 L84 114Z" fill="#FFB52E" {s(T2)}/>
<circle cx="76" cy="104" r="4.4" fill="#E5332B" {s(T3)}/><circle cx="76" cy="104" r="1.6" fill="{O}"/>
{bub(100, 88, 5)}{bub(108, 74, 3.6)}{bub(96, 68, 2.6)}{bub(22, 96, 4)}
''', 50, 8)
SUBJ["tswim-kozhukhovo"] = ("птица чомга с рыжим воротником и тёмным хохолком",
                            "ныряет вниз головой: над водой торчат только хвостик и оранжевые лапки, а под водой — голова в пузырях")

# 9. «Территория Фитнеса», Куркино — бассейн в стеклянном шаре
ICONS["tswim-kurkino"] = W("#6F7BD9", "#2A2F78", f'''
{sparkle(18, 30, 6)}{sparkle(110, 22, 5)}{sparkle(112, 84, 4)}
<path d="M30 96 H98 L106 118 H22Z" fill="#B5743C" {s()}/>
<path d="M28 106 H100" stroke="#8B5425" stroke-width="3"/>
<circle cx="64" cy="56" r="44" fill="#E9FBFF" {s()}/>
<path d="M21.5 64 Q32 56 44 64 T68 64 T92 64 T106.5 64 A44 44 0 0 1 21.5 64Z" fill="#35C3E8" {s('stroke-width="2.6"')}/>
<path d="M30 78 L98 78 M34 86 L94 86" stroke="#fff" stroke-width="2.4" stroke-dasharray="5 5" opacity=".8"/>
<circle cx="74" cy="62" r="9" fill="#FFD2B0" {s(T2)}/>
<path d="M65 60 Q66 51 74 52 Q82 51 83 60 Q74 55 65 60Z" fill="#FF5E86" {s(T3)}/>
<path d="M44 66 Q54 60 64 66" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M44 66 Q54 60 64 66" fill="none" stroke="#FFD2B0" stroke-width="4.6" stroke-linecap="round"/>
<path d="M82 58 Q90 46 96 52" fill="none" stroke="{O}" stroke-width="8" stroke-linecap="round"/>
<path d="M82 58 Q90 46 96 52" fill="none" stroke="#FFD2B0" stroke-width="4" stroke-linecap="round"/>
<circle cx="72" cy="63" r="1.8" fill="{O}"/><circle cx="78" cy="63" r="1.8" fill="{O}"/>
<circle cx="40" cy="36" r="3.4" fill="#fff"/><circle cx="56" cy="24" r="2.6" fill="#fff"/><circle cx="84" cy="30" r="3.6" fill="#fff"/>
<circle cx="50" cy="48" r="2.4" fill="#fff"/><circle cx="92" cy="42" r="2.4" fill="#fff"/><circle cx="68" cy="38" r="2" fill="#fff"/>
<path d="M36 30 Q44 18 56 16" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".9"/>
''', 40, 20)
SUBJ["tswim-kurkino"] = ("стеклянный снежный шар-сувенир на деревянной подставке, а внутри — маленький бассейн",
                         "вместо снежинок в шаре кружатся пузырьки, и крошечный пловец в розовой шапочке плывёт кролем")

# 10. «Территория Фитнеса», Люберцы (ул. Побратимов) — группа плывёт вместе
def sprat(x, y, cap, k=1.0):
    return f'''<g transform="translate({x} {y}) scale({k})">
<path d="M-26 0 L-40 -11 Q-36 0 -40 11Z" fill="#9FB4C9" {s(T2)}/>
<path d="M-28 0 Q-8 -15 16 -9 Q28 -4 30 2 Q24 12 6 13 Q-14 14 -28 0Z" fill="#DCE8F2" {s()}/>
<path d="M-22 -2 Q-4 -12 18 -6" fill="none" stroke="#5F86B5" stroke-width="5" stroke-linecap="round"/>
<path d="M4 -12 Q16 -22 28 -4 Q18 -8 6 -6Z" fill="{cap}" {s(T2)}/>
{eye(18, 1, .8)}<path d="M22 7 Q25 9 28 6" fill="none" {s(T3)}/></g>'''


ICONS["tswim-lyubertsy"] = W("#EAFFE9", "#2FBF98", f'''
<path d="M-6 20 H134" stroke="#fff" stroke-width="5" stroke-dasharray="10 8" opacity=".85"/>
<path d="M-6 112 H134" stroke="#fff" stroke-width="5" stroke-dasharray="10 8" opacity=".85"/>
{sprat(52, 38, "#FF5E5E", .9)}{sprat(72, 66, "#FFD23F", 1.0)}{sprat(52, 94, "#8E5BD9", .9)}
{bub(110, 40, 4.4)}{bub(116, 86, 3.6)}{bub(104, 100, 2.6)}
<path d="M8 60 H20 M6 72 H16" stroke="#fff" stroke-width="3.4" stroke-linecap="round" opacity=".9"/>
''', 70, 20)
SUBJ["tswim-lyubertsy"] = ("три серебристые кильки в красной, жёлтой и фиолетовой шапочках",
                           "плывут дружным клином по одной дорожке, как группа на тренировке")

# 11. «Территория Фитнеса», Королёв — город ракет: самый быстрый пловец
ICONS["tswim-korolev"] = W("#3C4FB8", "#0E1A52", f'''
{sparkle(104, 100, 5)}{sparkle(20, 22, 4)}
<g transform="rotate(-32 64 64)">
<path d="M22 64 L2 46 Q10 64 2 82Z" fill="#F4C21F" {s()}/>
<path d="M20 64 Q46 38 84 44 Q112 50 122 64 Q112 78 84 84 Q46 90 20 64Z" fill="#B9C7D9" {s()}/>
<path d="M22 63 Q48 42 84 46 Q110 51 120 63 Q84 56 22 63Z" fill="#274C9E"/>
<path d="M58 42 L70 24 Q76 36 76 44Z" fill="#274C9E" {s(T2)}/>
<path d="M62 84 L72 100 Q78 90 76 84Z" fill="#F4C21F" {s(T2)}/>
<path d="M36 52 l4 -7 l4 7 M44 50 l4 -7 l4 7 M36 76 l4 7 l4 -7 M44 78 l4 7 l4 -7" fill="#F4C21F" {s(T3)}/>
{eye(102, 60, 1.05)}
<path d="M106 72 Q111 75 115 70" fill="none" {s('stroke-width="2.6"')}/>
<ellipse cx="94" cy="72" rx="4.4" ry="2.6" fill="#FF7FA8" opacity=".85"/>
</g>
{bub(22, 104, 8)}{bub(10, 88, 5)}{bub(36, 116, 5)}{bub(6, 112, 3.4)}
<path d="M30 84 L22 92 M40 92 L34 100" stroke="#fff" stroke-width="3.4" stroke-linecap="round" opacity=".9"/>
''', 70, 20)
SUBJ["tswim-korolev"] = ("серебристо-синий тунец с жёлтыми плавничками, вытянутый, как ракета",
                         "взлетает наискосок из тёмно-синей глубины, оставляя за хвостом ракетный след из пузырей")

# 12. «Территория Фитнеса», Зеленоград — морской ангел у отметки глубины
ICONS["tswim-zelenograd"] = W("#EAFFD6", "#3FAE63", f'''
<path d="M-6 -6 H134 V20 Q112 28 90 20 T46 20 T-6 20Z" fill="#BFF3FF" opacity=".9"/>
<path d="M84 90 H118 V114 H84Z" fill="#fff" {s(T2)}/>
<text x="101" y="107" font-family="Arial" font-weight="700" font-size="13" fill="#2B7A45" text-anchor="middle">1,2</text>
<path d="M46 50 Q14 26 10 52 Q10 70 44 62Z" fill="#F6FBFF" opacity=".92" {s()}/>
<path d="M82 50 Q114 26 118 52 Q118 70 84 62Z" fill="#F6FBFF" opacity=".92" {s()}/>
<path d="M44 46 Q44 22 64 22 Q84 22 84 46 Q86 76 76 96 Q70 112 64 116 Q58 112 52 96 Q42 76 44 46Z" fill="#F6FBFF" opacity=".95" {s()}/>
<path d="M52 24 L46 10 M76 24 L82 10" fill="none" {s()}/>
<circle cx="46" cy="10" r="3.4" fill="#FF8A3D" {s(T3)}/><circle cx="82" cy="10" r="3.4" fill="#FF8A3D" {s(T3)}/>
<path d="M56 60 Q64 52 72 60 Q76 76 64 100 Q52 76 56 60Z" fill="#FF8A3D" opacity=".9"/>
<path d="M60 26 Q64 34 68 26 Q66 22 60 26Z" fill="#FF8A3D"/>
{eye(56, 42, 1.05)}{eye(72, 42, 1.05)}
<path d="M59 50 Q64 55 69 50" fill="none" {s('stroke-width="2.6"')}/>
<ellipse cx="49" cy="50" rx="4" ry="2.6" fill="#FF7FA8" opacity=".8"/><ellipse cx="79" cy="50" rx="4" ry="2.6" fill="#FF7FA8" opacity=".8"/>
{bub(24, 92, 5)}{bub(32, 106, 3.4)}{bub(104, 80, 4)}
''', 50, 16)
SUBJ["tswim-zelenograd"] = ("морской ангел — прозрачный белый моллюск с оранжевым сердечком внутри и крылышками-плавниками",
                            "порхает под водой у самого дна рядом с табличкой глубины «1,2»")

if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for i in ids:
        open(os.path.join(OUT, i + ".svg"), "w", encoding="utf-8").write(ICONS[i])
    print("svg:", len(ids))
    for i in ids:
        print(f"{i} — герой: {SUBJ[i][0]} | сцена: {SUBJ[i][1]}")
