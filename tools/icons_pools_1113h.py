"""Иконки робота pools, 2026-11-13 (08 UTC). Каждая придумана и нарисована отдельно (правило абсолютной
уникальности): свой герой, своя сцена, своя компоновка и палитра. Герои проверены по реестру icons-src/subjects.txt
(таких героев раньше не было), картинки — tools/check_unique.py.
Запуск: python3 tools/icons_pools_1113h.py [id …]  → python3 tools/render_icons.py <id…> → python3 tools/check_unique.py <id…>."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, sparkle, O
from icons_pools_1112b import W, bub, T2

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
T3 = 'stroke-width="2"'

# 1. «Мама, я плыву», Нагатинская — мама и малыш в воде: сивучиха везёт детёныша на спине
ICONS["mama-ya-plyvu-nagatinskaya"] = W("#FFF1DC", "#FF9E7A", f'''
<circle cx="24" cy="28" r="11" fill="#FFE46B" opacity=".9"/>
<path d="M14 92 Q-2 100 4 116 Q16 108 28 100Z" fill="#B87A3F" {s()}/>
<ellipse cx="56" cy="92" rx="46" ry="21" fill="#C98A4B" {s()}/>
<path d="M40 70 Q30 56 44 50 Q62 46 66 62 Q64 72 52 74Z" fill="#EBC08A" {s()}/>
<circle cx="62" cy="50" r="11" fill="#EBC08A" {s()}/>
{eye(65, 48, .75)}
<circle cx="72" cy="52" r="2.2" fill="{O}"/>
<path d="M80 86 Q84 60 100 54 Q120 52 120 70 Q118 86 100 92Z" fill="#C98A4B" {s()}/>
<ellipse cx="112" cy="72" rx="9" ry="7" fill="#E2A868" {s(T2)}/>
<ellipse cx="116" cy="68" rx="3" ry="2.2" fill="{O}"/>
{eye(100, 64, 1.05)}
<path d="M108 76 Q112 80 116 76" fill="none" {s(T2)}/>
<path d="M106 72 l-9 -2 M106 75 l-9 3" stroke="{O}" stroke-width="1.6" stroke-linecap="round"/>
<ellipse cx="94" cy="74" rx="4.4" ry="2.6" fill="#FF7FA8" opacity=".8"/>
<path d="M-6 96 Q10 88 26 96 T58 96 T90 96 T134 96 V134 H-6Z" fill="#35B6E6" {s('stroke-width="2.6"')}/>
<path d="M14 112 Q24 107 34 112 M82 114 Q92 109 102 114" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
''', 24, 22)
SUBJ["mama-ya-plyvu-nagatinskaya"] = ("рыжая мама-сивучиха с усатой мордой и светлый детёныш-сивучонок",
                                      "мама плывёт по голубой воде на закате, а малыш лежит у неё на спине и смотрит вперёд")

# 2. «Китик», Вешняковская — детский бассейн 0–7: китовая акула в белый горошек улыбается во весь широкий рот
ICONS["kitik-veshnyakovskaya"] = W("#E3FBF4", "#19A3A0", f'''
<path d="M22 66 L2 44 Q10 66 0 90Z" fill="#3E5F9C" {s()}/>
<path d="M56 40 L68 16 Q82 26 82 40Z" fill="#3E5F9C" {s()}/>
<path d="M14 68 Q22 38 68 36 Q112 36 122 62 Q124 72 118 80 Q100 98 64 98 Q26 98 14 68Z" fill="#4F74B8" {s()}/>
<path d="M30 84 Q62 104 112 84 Q98 98 64 98 Q40 98 30 84Z" fill="#EAF4FF"/>
<path d="M60 92 Q52 112 38 112 Q44 100 44 90Z" fill="#3E5F9C" {s()}/>
<path d="M94 80 Q108 84 121 70" fill="none" {s('stroke-width="3.4"')}/>
<circle cx="34" cy="60" r="3.4" fill="#fff"/><circle cx="46" cy="50" r="3" fill="#fff"/><circle cx="50" cy="66" r="3.6" fill="#fff"/>
<circle cx="62" cy="54" r="3" fill="#fff"/><circle cx="66" cy="72" r="3.4" fill="#fff"/><circle cx="78" cy="48" r="3.2" fill="#fff"/>
<circle cx="82" cy="64" r="3" fill="#fff"/><circle cx="36" cy="74" r="2.6" fill="#fff"/><circle cx="94" cy="50" r="2.6" fill="#fff"/>
{eye(104, 58, 1.1)}
<ellipse cx="98" cy="70" rx="4.6" ry="2.8" fill="#FF7FA8" opacity=".85"/>
{bub(108, 30, 6)}{bub(118, 18, 3.6)}{bub(20, 106, 4.4)}
''', 60, 20)
SUBJ["kitik-veshnyakovskaya"] = ("синяя китовая акула в белый горошек с широкой улыбкой",
                                 "плывёт во весь кадр в бирюзовой воде и пускает пузыри к поверхности")

# 3. «Акваладушки», ЖК «Шагал» — две рыбки-клоуна играют плавниками в «ладушки»
def _clown(flip):
    t = 'transform="translate(128 0) scale(-1 1)"' if flip else ""
    return f'''<g {t}>
<path d="M12 64 L-4 48 Q4 64 -4 82Z" fill="#FF7A1A" {s()}/>
<path d="M22 44 Q34 28 46 44Z" fill="#FF7A1A" {s()}/>
<ellipse cx="34" cy="66" rx="25" ry="20" fill="#FF8C2B" {s()}/>
<path d="M22 49 Q16 66 22 83 L30 85 Q24 66 30 47Z" fill="#fff" {s(T2)}/>
<path d="M42 47 Q38 66 42 85 L48 82 Q45 66 48 50Z" fill="#fff" {s(T2)}/>
<path d="M50 70 Q64 62 62 50 Q52 54 48 62Z" fill="#FFB36B" {s()}/>
{eye(51, 58, .9)}
<path d="M53 74 Q56 77 58 73" fill="none" {s(T3)}/>
</g>'''
ICONS["akvaladushki-shagala"] = W("#F3E4FF", "#B66BE8", f'''
<path d="M40 134 Q36 108 44 98 Q50 110 50 134Z M58 134 Q58 104 64 94 Q72 106 70 134Z M80 134 Q80 110 88 100 Q94 112 90 134Z" fill="#FF8FC2" {s(T2)}/>
{_clown(False)}{_clown(True)}
<path d="M64 40 V30 M54 44 L48 36 M74 44 L80 36" stroke="#FFE46B" stroke-width="4" stroke-linecap="round"/>
{bub(64, 16, 5)}{bub(20, 24, 3.4)}{bub(108, 22, 4)}
''', 50, 24)
SUBJ["akvaladushki-shagala"] = ("две оранжевые рыбки-клоуна с белыми полосками",
                                "плывут друг к другу и хлопают плавниками в «ладушки» над розовыми щупальцами актинии")

# 4. AQVILLE, Миклухо-Маклая — синхронное плавание и водное поло: сардины синхронно кружат вокруг мяча
def _sard(a):
    return f'''<g transform="rotate({a} 64 64)">
<path d="M64 14 Q82 16 92 24 Q80 34 64 32 Q52 30 46 23 Q54 15 64 14Z" fill="#C9D6E6" {s(T2)}/>
<path d="M50 23 L38 15 Q42 23 38 31Z" fill="#8FA3BD" {s(T2)}/>
<path d="M56 17 Q70 17 86 23" fill="none" stroke="#5B78A8" stroke-width="3" stroke-linecap="round"/>
{eye(83, 24, .6)}</g>'''
ICONS["aqville-miklukho"] = W("#2B5FC4", "#0B1F5C", f'''
<circle cx="64" cy="64" r="30" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 7" opacity=".55"/>
{_sard(0)}{_sard(90)}{_sard(180)}{_sard(270)}
<circle cx="64" cy="64" r="19" fill="#FFD23F" {s()}/>
<path d="M47 58 Q64 68 81 58 M52 78 Q64 64 60 46 M76 78 Q66 66 70 46" fill="none" {s(T3)}/>
<circle cx="57" cy="57" r="4" fill="#fff" opacity=".7"/>
''', 50, 50)
SUBJ["aqville-miklukho"] = ("четыре серебристые сардины с синей полоской на спине",
                            "синхронно плывут по кругу вокруг жёлтого мяча для водного поло, вид сверху на тёмно-синюю воду")

# 5. «Волна Успеха», Косинская — синхронное плавание для девочек: вуалехвост в короне на гребне волны
ICONS["volna-uspekha-kosinskaya"] = W("#FFFBE0", "#FFC94D", f'''
<path d="M-6 96 Q14 60 44 62 Q70 64 76 84 Q80 98 68 100 Q84 108 104 96 Q120 86 134 92 V134 H-6Z" fill="#2E9BE6" {s()}/>
<path d="M2 96 Q18 72 44 72 Q62 73 66 86" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".85"/>
<path d="M58 44 Q30 18 18 34 Q26 40 22 52 Q34 44 40 58 Q46 50 58 52Z" fill="#FF9EC0" {s()}/>
<path d="M54 46 Q38 34 26 38 M54 50 Q42 46 34 50" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".9"/>
<path d="M70 30 Q78 16 90 28Z" fill="#FF9EC0" {s()}/>
<ellipse cx="80" cy="46" rx="25" ry="18" fill="#FF6B5E" {s()}/>
<path d="M72 58 Q70 72 82 70 Q84 62 80 58Z" fill="#FF9EC0" {s()}/>
{eye(92, 42, 1.05)}
<path d="M98 52 Q102 55 104 50" fill="none" {s(T2)}/>
<ellipse cx="88" cy="52" rx="4.4" ry="2.6" fill="#FFD0DC" opacity=".9"/>
<path d="M84 26 L86 14 L92 22 L98 12 L102 22 L108 16 L106 30Z" fill="#FFE46B" {s(T2)}/>
{sparkle(114, 44, 6)}{sparkle(14, 16, 5)}
''', 30, 20)
SUBJ["volna-uspekha-kosinskaya"] = ("красная рыбка-вуалехвост с пышным розовым хвостом и золотой короной",
                                    "красуется на самом гребне высокой синей волны, хвост развевается как шлейф")

# 6. Strong Swim, Косинская — сильное плавание: лабрадор в очках для плавания гребёт лапами
ICONS["strong-swim-kosinskaya"] = W("#DDF9FF", "#1E88D9", f'''
<path d="M30 40 Q14 44 16 72 Q26 76 34 62Z" fill="#B8862F" {s()}/>
<path d="M98 40 Q114 44 112 72 Q102 76 94 62Z" fill="#B8862F" {s()}/>
<path d="M30 52 Q30 22 64 22 Q98 22 98 52 Q98 86 64 88 Q30 86 30 52Z" fill="#F2C766" {s()}/>
<ellipse cx="64" cy="68" rx="19" ry="15" fill="#FFE9B0" {s()}/>
<ellipse cx="64" cy="60" rx="7" ry="5" fill="{O}"/>
<path d="M64 65 V72 M56 74 Q64 80 72 74" fill="none" {s(T2)}/>
<path d="M60 76 Q64 86 68 76Z" fill="#FF6B8A" {s(T3)}/>
<path d="M30 44 H98" stroke="{O}" stroke-width="7"/>
<path d="M30 44 H98" stroke="#F0483E" stroke-width="3.4"/>
<ellipse cx="48" cy="44" rx="12" ry="9" fill="#9BE3FF" {s()}/>
<ellipse cx="80" cy="44" rx="12" ry="9" fill="#9BE3FF" {s()}/>
{eye(49, 45, .85)}{eye(79, 45, .85)}
<path d="M-6 92 Q10 84 26 92 T58 92 T90 92 T134 92 V134 H-6Z" fill="#1565C0" {s('stroke-width="2.6"')}/>
<ellipse cx="26" cy="92" rx="13" ry="9" fill="#F2C766" {s()}/>
<ellipse cx="102" cy="92" rx="13" ry="9" fill="#F2C766" {s()}/>
<path d="M20 88 v6 M26 87 v7 M32 88 v6 M96 88 v6 M102 87 v7 M108 88 v6" stroke="{O}" stroke-width="1.8" stroke-linecap="round"/>
<path d="M8 80 l-6 -8 M14 76 l-2 -10 M120 80 l6 -8 M114 76 l2 -10" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
''', 50, 16)
SUBJ["strong-swim-kosinskaya"] = ("палевый лабрадор в красных очках для плавания с голубыми стёклами",
                                  "смотрит прямо на нас из синей воды и изо всех сил гребёт передними лапами, летят брызги")

# 7. Школа плавания № 1, «Лихоборы» — группы 7–13 лет: меченосец финиширует, касаясь бортика «мечом»
ICONS["ss1-lihobory"] = W("#F4FBFF", "#8CCBF2", f'''
<rect x="100" y="-4" width="34" height="136" fill="#E9EEF5" {s()}/>
<rect x="100" y="40" width="12" height="48" fill="#FFD23F" {s(T2)}/>
<path d="M-6 26 H100" stroke="{O}" stroke-width="9"/>
<path d="M-6 26 H100" stroke="#F0483E" stroke-width="5" stroke-dasharray="12 8"/>
<path d="M30 60 L8 44 Q14 58 10 66 L-4 96 Q10 92 20 80 Q26 74 34 72Z" fill="#E03A2B" {s()}/>
<path d="M44 48 Q56 34 70 46Z" fill="#E03A2B" {s()}/>
<path d="M28 66 Q44 44 72 50 Q92 56 100 64 Q88 78 66 80 Q42 82 28 66Z" fill="#FF6A3D" {s()}/>
<path d="M34 66 Q60 62 92 64" fill="none" stroke="{O}" stroke-width="2.2" stroke-linecap="round" opacity=".6"/>
<path d="M56 78 Q58 90 68 86 Q68 80 64 78Z" fill="#E03A2B" {s(T2)}/>
{eye(84, 60, .95)}
<path d="M90 70 Q94 72 96 68" fill="none" {s(T3)}/>
<path d="M108 30 l8 -6 M112 100 l8 6 M116 64 h8" stroke="#F0483E" stroke-width="3.4" stroke-linecap="round"/>
{bub(20, 108, 5)}{bub(40, 100, 3.4)}
''', 30, 30)
SUBJ["ss1-lihobory"] = ("красно-оранжевый меченосец с длинным хвостом-«мечом»",
                        "под красно-белой разделительной дорожкой доплывает до бортика и касается носом жёлтого финишного щита")

# 8. Школа плавания № 1, Дворец водного спорта «Фили» — 50 м и прыжковая зона 6 м: Несси в шапочке
ICONS["ss1-fili-dvs"] = W("#FFE9C9", "#FF8A5B", f'''
<path d="M-6 84 Q10 76 26 84 T58 84 T90 84 T134 84 V134 H-6Z" fill="#17A3A8" {s('stroke-width="2.6"')}/>
<path d="M14 84 Q26 58 40 84Z" fill="#5CC46A" {s()}/>
<path d="M40 84 Q54 52 68 84Z" fill="#5CC46A" {s()}/>
<path d="M72 86 Q72 40 84 26 Q92 16 104 22 Q116 30 110 44 Q104 54 96 50 Q94 66 96 86Z" fill="#5CC46A" {s()}/>
<path d="M80 30 Q88 10 106 18 Q116 24 114 36 Q98 22 80 30Z" fill="#F0483E" {s()}/>
{eye(100, 36, 1.05)}
<path d="M102 46 Q107 48 109 43" fill="none" {s(T2)}/>
<ellipse cx="94" cy="44" rx="4" ry="2.4" fill="#FF7FA8" opacity=".85"/>
<circle cx="22" cy="80" r="3" fill="#FFE46B"/><circle cx="54" cy="74" r="3" fill="#FFE46B"/><circle cx="84" cy="62" r="3" fill="#FFE46B"/>
<path d="M-6 104 H134" stroke="{O}" stroke-width="8"/>
<path d="M-6 104 H134" stroke="#FFD23F" stroke-width="4.4" stroke-dasharray="10 7"/>
<path d="M-6 122 H134" stroke="#fff" stroke-width="3" stroke-dasharray="10 7" opacity=".7"/>
''', 30, 22)
SUBJ["ss1-fili-dvs"] = ("зелёное длинношеее чудище Несси в красной плавательной шапочке",
                        "высунуло шею и два горба из глубокого бассейна за жёлтой разделительной дорожкой, вечернее оранжевое небо")

# 9. Школа плавания № 1, МГСУ — группы 7–13 лет: скумбрия плывёт на спине под флажками
ICONS["ss1-mgsu"] = W("#EFFFF4", "#7ADDB0", f'''
<path d="M-6 20 Q64 34 134 20" fill="none" {s(T2)}/>
<path d="M10 23 L18 40 L26 25Z" fill="#F0483E" {s(T2)}/><path d="M36 27 L44 44 L52 28Z" fill="#FFD23F" {s(T2)}/>
<path d="M62 29 L70 46 L78 29Z" fill="#3D7BE0" {s(T2)}/><path d="M88 28 L96 44 L104 26Z" fill="#F0483E" {s(T2)}/>
<path d="M-6 76 Q10 68 26 76 T58 76 T90 76 T134 76 V134 H-6Z" fill="#2FB6C9" {s('stroke-width="2.6"')}/>
<path d="M22 76 L4 62 Q10 78 2 92Z" fill="#2C6FB3" {s()}/>
<path d="M20 78 Q42 96 76 92 Q104 88 114 76 Q100 62 72 62 Q40 62 20 78Z" fill="#EAF4FF" {s()}/>
<path d="M22 79 Q44 96 76 92 Q102 89 113 77 Q90 84 66 84 Q40 84 22 79Z" fill="#2C8FB3"/>
<path d="M36 84 l5 6 M48 85 l5 6 M60 85 l5 6 M72 84 l5 6 M84 82 l5 5" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>
<path d="M60 64 Q56 44 72 48 Q74 56 70 63Z" fill="#9BD3F2" {s()}/>
{eye(98, 72, .95)}
<path d="M104 80 Q108 79 108 75" fill="none" {s(T3)}/>
<path d="M54 54 l-6 -6 M64 50 l-2 -8" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
''', 60, 16)
SUBJ["ss1-mgsu"] = ("скумбрия с синей полосатой спинкой и белым брюшком",
                    "плывёт на спине брюшком вверх и машет плавником под гирляндой цветных флажков для пловцов-спинистов")

# 10. Школа плавания № 1, МЭИ — 25 м × 4 дорожки: хариус с плавником-парусом летит над водой баттерфляем
ICONS["ss1-mei"] = W("#EDE4FF", "#6A4FD0", f'''
<path d="M10 100 Q40 20 110 78" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="2 8" stroke-linecap="round" opacity=".8"/>
<path d="M40 56 L20 50 Q28 62 22 76Z" fill="#35C9C0" {s()}/>
<path d="M50 44 Q54 12 84 22 Q88 36 80 46Z" fill="#FF5E86" {s()}/>
<path d="M58 40 Q62 26 74 26 M66 42 Q70 32 80 32" fill="none" stroke="#FFD23F" stroke-width="3" stroke-linecap="round"/>
<path d="M36 60 Q52 38 82 44 Q102 50 106 62 Q94 76 70 74 Q46 74 36 60Z" fill="#9FB4C8" {s()}/>
<path d="M44 60 Q70 54 100 60" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".7"/>
<path d="M64 72 Q62 84 74 82 Q76 76 72 73Z" fill="#35C9C0" {s(T2)}/>
{eye(92, 56, .95)}
<path d="M98 66 Q102 67 103 63" fill="none" {s(T3)}/>
<path d="M-6 104 Q10 96 26 104 T58 104 T90 104 T134 104 V134 H-6Z" fill="#3D9BF2" {s('stroke-width="2.6"')}/>
<path d="M16 100 l-4 -10 M26 98 l2 -10 M104 98 l4 -10 M114 100 l8 -6" stroke="#fff" stroke-width="3.6" stroke-linecap="round"/>
''', 70, 20)
SUBJ["ss1-mei"] = ("серебристый хариус с огромным розовым спинным плавником-парусом",
                   "дугой перелетает над водой, как пловец баттерфляем, на сиреневом фоне, внизу всплески")

# 11. Школа плавания № 1, МГТУ им. Баумана — 50 м × 10 дорожек: латимерия готовится к старту с тумбы
ICONS["ss1-bauman"] = W("#FFFBD0", "#FFD23F", f'''
<path d="M70 96 L122 86 V134 H62Z" fill="#DDE5F0" {s()}/>
<path d="M66 88 L120 76 L124 86 L70 98Z" fill="#3D7BE0" {s()}/>
<path d="M86 108 h18 M95 100 v22" stroke="{O}" stroke-width="3.4" stroke-linecap="round"/>
<path d="M-6 116 Q10 110 26 116 T64 116 V134 H-6Z" fill="#2FB6E9" {s('stroke-width="2.6"')}/>
<path d="M108 58 L126 44 Q122 60 126 76 Q116 70 108 68Z" fill="#14605C" {s()}/>
<path d="M84 44 Q92 30 100 46Z M64 44 Q70 32 78 44Z" fill="#14605C" {s()}/>
<path d="M30 70 Q40 44 74 44 Q102 46 112 62 Q100 82 70 84 Q44 84 30 70Z" fill="#1F8F86" {s()}/>
<path d="M58 54 q5 4 0 8 M70 52 q5 4 0 8 M82 54 q5 4 0 8 M64 66 q5 4 0 8 M76 66 q5 4 0 8 M90 66 q5 4 0 8 M94 56 q4 3 0 7" fill="none" stroke="#FFE46B" stroke-width="2.6" stroke-linecap="round"/>
<path d="M62 82 Q56 92 64 94 L72 94 Q74 88 70 84Z M88 80 Q86 88 92 90 L98 88 Q98 82 94 78Z" fill="#14605C" {s(T2)}/>
<path d="M40 78 Q30 86 22 82 Q24 92 34 92 Q44 90 48 82Z" fill="#14605C" {s(T2)}/>
{eye(42, 62, 1.05)}
<path d="M32 72 Q36 76 40 72" fill="none" {s(T2)}/>
<ellipse cx="50" cy="70" rx="4" ry="2.4" fill="#FF7FA8" opacity=".85"/>
''', 30, 20)
SUBJ["ss1-bauman"] = ("тёмно-бирюзовая латимерия в жёлтых чешуйках-скобках с плавниками-лапками",
                      "стоит на синей стартовой тумбе, наклонилась к воде и готовится нырнуть по свистку, жёлтый фон")

# 12. Школа плавания № 1, бассейн «Серебряный» — серебряная сельдь с серебряной медалью
ICONS["ss1-serebryany"] = W("#3C4F8F", "#141B45", f'''
<path d="M52 108 L40 124 Q64 116 88 124 L76 108Z" fill="#7F93B5" {s()}/>
<path d="M44 40 Q28 46 26 60 Q36 60 44 54Z M84 40 Q100 46 102 60 Q92 60 84 54Z" fill="#7F93B5" {s()}/>
<path d="M64 10 Q90 26 88 66 Q86 96 64 112 Q42 96 40 66 Q38 26 64 10Z" fill="#D8E1EE" {s()}/>
<path d="M64 12 Q84 28 84 52 Q74 40 64 40 Q54 40 44 52 Q44 28 64 12Z" fill="#8FA6C8"/>
{eye(54, 36, 1.05)}{eye(74, 36, 1.05)}
<path d="M58 46 Q64 51 70 46" fill="none" {s(T2)}/>
<ellipse cx="46" cy="44" rx="4" ry="2.4" fill="#FF7FA8" opacity=".8"/><ellipse cx="82" cy="44" rx="4" ry="2.4" fill="#FF7FA8" opacity=".8"/>
<path d="M46 56 L64 78 L82 56" fill="none" stroke="{O}" stroke-width="8" stroke-linejoin="round"/>
<path d="M46 56 L64 78 L82 56" fill="none" stroke="#35C9C0" stroke-width="4.4" stroke-linejoin="round"/>
<circle cx="64" cy="86" r="12" fill="#EEF2F7" {s()}/>
<circle cx="64" cy="86" r="7.4" fill="none" stroke="#9AA8BD" stroke-width="2"/>
{sparkle(104, 28, 7)}{sparkle(20, 84, 5)}{sparkle(108, 96, 4)}
''', 50, 30)
SUBJ["ss1-serebryany"] = ("серебряная сельдь, стоящая столбиком на хвосте",
                          "гордо смотрит на нас с серебряной медалью на бирюзовой ленте, вокруг блёстки на тёмно-синем фоне")

# 13. Школа плавания № 1, «Фитнес Практика» (Толбухина) — рыба-губан толкает перед собой плавательную доску
ICONS["ss1-fitnes-praktika"] = W("#FFF0DC", "#FF9A3D", f'''
<path d="M-6 58 Q10 50 26 58 T58 58 T90 58 T134 58 V134 H-6Z" fill="#2BA8D9" {s('stroke-width="2.6"')}/>
<path d="M30 84 L8 66 Q14 86 6 106Z" fill="#7B4FD0" {s()}/>
<path d="M40 66 Q54 50 70 64Z" fill="#7B4FD0" {s()}/>
<path d="M24 86 Q36 62 64 64 Q86 66 92 84 Q84 104 60 106 Q36 106 24 86Z" fill="#2FCB9A" {s()}/>
<path d="M36 78 Q44 96 40 100 M50 70 Q58 92 54 104" fill="none" stroke="#7B4FD0" stroke-width="4" stroke-linecap="round"/>
<ellipse cx="92" cy="88" rx="8" ry="6.4" fill="#FF6B8A" {s(T2)}/>
<path d="M86 88 H98" {s(T3)}/>
{eye(78, 78, 1)}
<path d="M70 92 Q84 94 96 78" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M70 92 Q84 94 96 78" fill="none" stroke="#2FCB9A" stroke-width="4.6" stroke-linecap="round"/>
<path d="M92 52 Q92 44 100 44 H118 Q126 44 126 52 V84 Q126 88 122 88 H96 Q92 88 92 84Z" fill="#F0483E" {s()} transform="rotate(14 108 66)"/>
<path d="M100 54 h16" stroke="#fff" stroke-width="3.4" stroke-linecap="round" transform="rotate(14 108 66)"/>
<path d="M12 50 l-4 -10 M22 48 l2 -10 M34 50 l6 -8" stroke="#fff" stroke-width="3.6" stroke-linecap="round"/>
''', 40, 14)
SUBJ["ss1-fitnes-praktika"] = ("зелёная рыба-губан с фиолетовыми полосками и пухлыми розовыми губами",
                               "держится плавником за красную плавательную доску и работает хвостом, за хвостом брызги")

# 14. Школа плавания № 1, Одинцово — группы с 5 лет: полосатая рыбка данио учится выдыхать в воду
ICONS["ss1-odintsovo"] = W("#FFE6F0", "#F06AA5", f'''
<circle cx="92" cy="34" r="24" fill="#fff" opacity=".35" {s()}/>
<circle cx="84" cy="26" r="6" fill="#fff" opacity=".9"/>
<circle cx="62" cy="62" r="15" fill="#fff" opacity=".35" {s()}/>
<circle cx="57" cy="57" r="3.8" fill="#fff" opacity=".9"/>
<circle cx="46" cy="82" r="9" fill="#fff" opacity=".35" {s(T2)}/>
<circle cx="43" cy="79" r="2.2" fill="#fff" opacity=".9"/>
<path d="M12 100 L-2 88 Q2 102 -4 116Z" fill="#FFD23F" {s()}/>
<path d="M8 102 Q14 88 30 88 Q44 90 48 100 Q42 112 28 114 Q14 114 8 102Z" fill="#FFE46B" {s()}/>
<path d="M12 98 Q28 92 44 98 M12 104 Q28 100 46 104 M16 110 Q28 106 40 110" fill="none" stroke="#3D5BD9" stroke-width="3" stroke-linecap="round"/>
{eye(39, 98, .8)}
<circle cx="50" cy="102" r="3" fill="none" {s(T2)}/>
<path d="M70 134 Q66 116 74 108 Q80 118 78 134Z M88 134 Q88 112 96 106 Q102 116 98 134Z" fill="#37C28A" {s(T2)}/>
''', 70, 24)
SUBJ["ss1-odintsovo"] = ("маленькая жёлтая рыбка данио в синюю продольную полоску",
                         "сидит в нижнем углу и выдувает ртом цепочку пузырей — от крошечного до огромного во весь верх картинки")

# 15. Школа плавания № 1, «Жаворонки» — 25 м × 6 дорожек: стерлядь скользит «стрелочкой»
ICONS["ss1-zhavoronki"] = W("#F2FFD9", "#4BBF73", f'''
<path d="M-6 -6 H134 V40 Q100 30 64 40 T-6 40Z" fill="#fff" opacity=".35"/>
<g transform="rotate(-38 64 64)">
<path d="M22 64 L2 48 Q8 64 -2 84Z" fill="#6B7C5A" {s()}/>
<path d="M18 64 Q40 48 78 52 Q104 56 128 64 Q104 72 78 76 Q40 80 18 64Z" fill="#9BAA7E" {s()}/>
<path d="M28 68 Q60 76 100 68 Q80 74 60 76 Q40 76 28 68Z" fill="#F4F1D8"/>
<path d="M36 56 l4 -6 l4 6 M52 54 l4 -6 l4 6 M68 54 l4 -6 l4 6 M84 56 l3 -5 l4 6" fill="#FFD23F" {s(T3)}/>
<path d="M54 76 Q52 88 64 84 Q64 78 60 76Z" fill="#6B7C5A" {s(T2)}/>
{eye(98, 62, .85)}
<ellipse cx="92" cy="68" rx="3.6" ry="2.2" fill="#FF7FA8" opacity=".85"/>
</g>
<path d="M12 112 l14 -11 M30 122 l12 -9 M6 92 l10 -8" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
{bub(104, 100, 5)}{bub(116, 86, 3.2)}
''', 70, 70)
SUBJ["ss1-zhavoronki"] = ("оливковая остроносая стерлядь с жёлтыми шипами-«жучками» на спине",
                          "вытянулась в струнку и скользит «стрелочкой» по диагонали вверх, оставляя за собой белые чёрточки")

# 16. Школа плавания № 1, бассейн МИСИС — группы 7–12 лет: спинорог делает кувырок-поворот у бортика
ICONS["ss1-misis"] = W("#E8F1F7", "#6E8CA8", f'''
<rect x="-6" y="-4" width="26" height="136" fill="#C7D3DF" {s()}/>
<path d="M6 30 h8 M6 64 h8 M6 98 h8" stroke="{O}" stroke-width="3" stroke-linecap="round"/>
<path d="M104 64 A40 40 0 1 1 86 31" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-dasharray="1 10"/>
<path d="M82 22 L96 30 L82 40Z" fill="#fff"/>
<g transform="rotate(150 62 66)">
<path d="M88 66 L106 52 Q102 66 106 82Z" fill="#FFD23F" {s()}/>
<path d="M52 44 Q62 26 78 46Z M56 88 Q64 104 78 86Z" fill="#17B5C9" {s()}/>
<path d="M22 68 Q40 40 66 42 Q86 46 94 66 Q86 88 66 90 Q40 92 22 68Z" fill="#FF8A3D" {s()}/>
<path d="M50 46 Q44 66 52 88 M66 43 Q60 66 68 90" fill="none" stroke="#23408E" stroke-width="5" stroke-linecap="round"/>
<path d="M22 68 Q30 62 36 66 Q30 72 22 68Z" fill="#FFE46B" {s(T2)}/>
{eye(40, 58, .95)}
</g>
{bub(104, 104, 5)}{bub(116, 90, 3.2)}
''', 70, 30)
SUBJ["ss1-misis"] = ("оранжевая рыба-спинорог с синими полосами и бирюзовыми плавниками",
                     "перевернулась вверх брюхом у серого бортика и делает кувырок-поворот, белая пунктирная стрелка показывает круг")

if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for i in ids:
        open(os.path.join(OUT, i + ".svg"), "w", encoding="utf-8").write(ICONS[i])
    print("svg:", len(ids))
    for i in ids:
        print(f"{i} — герой: {SUBJ[i][0]} | сцена: {SUBJ[i][1]}")
