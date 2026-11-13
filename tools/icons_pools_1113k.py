"""Иконки робота pools, 2026-11-13 (11 UTC). Каждая придумана и нарисована отдельно (правило абсолютной
уникальности): свой герой, своя сцена, своя компоновка и палитра. Герои проверены по реестру icons-src/subjects.txt
(таких героев раньше не было), картинки — tools/check_unique.py.
Запуск: python3 tools/icons_pools_1113k.py [id …]  → python3 tools/render_icons.py <id…> → python3 tools/check_unique.py <id…>."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, sparkle, O
from icons_pools_1112b import W, bub, T2

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
BL = '<ellipse cx="{}" cy="{}" rx="4.6" ry="2.8" fill="#FF7FA8" opacity=".8"/>'

# 1. «Волна», Балашиха (Ольгино) — белый медвежонок отдыхает на гребне большой волны
ICONS["volna-balashikha-olgino"] = W("#EFFFF8", "#2F7FD6", f'''
<path d="M-6 84 Q20 40 62 44 Q98 48 104 74 Q106 88 94 90 Q100 72 84 68 Q60 64 44 92 Q30 116 -6 120Z" fill="#3FA9F0" {s()}/>
<path d="M62 44 Q98 48 104 74 Q106 88 94 90 Q100 72 84 68" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<path d="M-6 112 Q30 96 64 108 T134 104 V134 H-6Z" fill="#1E6FC4" {s()}/>
<ellipse cx="50" cy="42" rx="24" ry="14" fill="#fff" {s()} transform="rotate(-14 50 42)"/>
<circle cx="76" cy="30" r="14" fill="#fff" {s()}/>
<circle cx="66" cy="19" r="5" fill="#fff" {s()}/><circle cx="86" cy="19" r="5" fill="#fff" {s()}/>
{eye(72, 29, .8)}{eye(82, 29, .8)}
<ellipse cx="77" cy="36" rx="3.2" ry="2.4" fill="{O}"/>
{BL.format(66, 36)}{BL.format(88, 36)}
<path d="M30 40 Q22 30 28 24 M40 54 Q36 64 42 68" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M30 40 Q22 30 28 24 M40 54 Q36 64 42 68" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
''', 30, 20)
SUBJ["volna-balashikha-olgino"] = ("белый медвежонок с чёрным носом и круглыми ушками",
                                   "лежит на спине на самом гребне большой синей волны с белым завитком и болтает лапами")

# 2. «Школа раннего плавания», Химки — занятия «мама + малыш» с рождения: малыш катится по маминой шее
ICONS["rannee-plavanie-khimki-yunnatov"] = W("#FFFBD6", "#8FD46A", f'''
<path d="M-6 92 Q26 84 58 92 T134 90 V134 H-6Z" fill="#3CC1C9" {s()}/>
<path d="M40 100 Q30 60 44 34 Q52 20 66 22 Q80 26 78 38 Q76 46 64 44 Q56 44 56 56 Q54 78 70 98Z" fill="#5B8DEF" {s()}/>
<ellipse cx="72" cy="100" rx="40" ry="16" fill="#5B8DEF" {s()}/>
<path d="M-6 100 Q26 92 58 100 T134 98 V134 H-6Z" fill="#3CC1C9"/>
<path d="M-6 100 Q26 92 58 100 T134 98" fill="none" {s()}/>
{eye(68, 32, .85)}
<path d="M72 39 Q76 41 78 38" fill="none" {s(T2)}/>
{BL.format(62, 38)}
<circle cx="50" cy="64" r="3" fill="#BFD4FF"/><circle cx="48" cy="80" r="3.4" fill="#BFD4FF"/><circle cx="90" cy="98" r="3.4" fill="#BFD4FF"/>
<g transform="rotate(24 92 62)">
<ellipse cx="94" cy="66" rx="14" ry="9" fill="#FFB84D" {s()}/>
<path d="M84 62 Q78 46 86 42 Q96 40 96 50 Q94 56 90 58Z" fill="#FFB84D" {s()}/>
{eye(90, 48, .65)}
<path d="M106 66 l10 -5 l-3 9Z" fill="#FFB84D" {s(T2)}/>
</g>
<path d="M104 40 q6 -6 12 0 M96 30 q5 -5 10 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 30, 24)
SUBJ["rannee-plavanie-khimki-yunnatov"] = ("синяя длинношеяя мама-плезиозавр и оранжевый малыш-плезиозаврик",
                                           "мама высунула шею из бирюзовой воды, а малыш съезжает по её спине в воду, как с горки")

# 3. Школа плавания SPN, Химки (25 м, 7 дорожек) — ихтиозавр мчится по своей дорожке
ICONS["spn-khimki-michurina"] = W("#E9F6FF", "#123C8C", f'''
<rect x="-6" y="-6" width="140" height="140" fill="#2A8BE0" opacity=".55"/>
<g transform="rotate(-18 64 64)">
<path d="M-20 30 H150 M-20 98 H150" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M-20 30 H150 M-20 98 H150" stroke="#FF5A4D" stroke-width="5" stroke-linecap="round" stroke-dasharray="12 10"/>
<path d="M-20 30 H150 M-20 98 H150" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-dasharray="12 10" stroke-dashoffset="11"/>
<path d="M26 64 L4 46 Q10 64 4 84Z" fill="#2E9E8F" {s()}/>
<path d="M56 50 L62 34 Q72 40 74 50Z" fill="#2E9E8F" {s()}/>
<path d="M22 64 Q40 44 70 46 Q92 48 100 58 L126 62 Q128 64 126 66 L100 70 Q92 82 70 82 Q40 84 22 64Z" fill="#3CC9B4" {s()}/>
<path d="M34 72 Q62 86 96 72 Q84 82 70 82 Q46 83 34 72Z" fill="#E9FFF8"/>
<path d="M62 80 Q58 94 48 94 Q52 84 52 78Z" fill="#2E9E8F" {s()}/>
<circle cx="90" cy="60" r="7.5" fill="#fff" {s(T2)}/>
{eye(91, 60, .8)}
<path d="M104 68 Q114 69 122 66" fill="none" {s(T2)}/>
</g>
<path d="M8 96 h14 M2 108 h18 M14 84 h10" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".9"/>
''', 70, 24)
SUBJ["spn-khimki-michurina"] = ("бирюзовый ихтиозавр с длинным клювом и большим круглым глазом",
                                "мчится наискосок между двумя красно-белыми разделительными дорожками, за хвостом белые чёрточки скорости")

# 4. Школа плавания SPN, Новогорск — спортивные группы 5–18 лет: баттерфляй («бабочку») плывёт летучий мышонок
ICONS["spn-novogorsk"] = W("#F3E9FF", "#5B3FA8", f'''
<circle cx="100" cy="24" r="12" fill="#FFE98A" opacity=".9"/>
<path d="M64 62 Q40 26 6 40 Q16 46 14 58 Q26 54 30 66 Q42 60 48 72Z" fill="#7A5AC8" {s()}/>
<path d="M64 62 Q88 26 122 40 Q112 46 114 58 Q102 54 98 66 Q86 60 80 72Z" fill="#7A5AC8" {s()}/>
<path d="M64 62 L30 66 M64 62 L14 58 M64 62 L98 66 M64 62 L114 58" stroke="{O}" stroke-width="2" stroke-linecap="round"/>
<ellipse cx="64" cy="74" rx="17" ry="19" fill="#9A7BE0" {s()}/>
<path d="M50 60 L46 42 L58 54Z M78 60 L82 42 L70 54Z" fill="#9A7BE0" {s()}/>
<path d="M50 66 Q64 58 78 66 Q78 72 64 72 Q50 72 50 66Z" fill="#35D0E0" {s(T2)}/>
<path d="M64 62 V72" stroke="{O}" stroke-width="2.4"/>
<circle cx="57" cy="67" r="1.8" fill="{O}"/><circle cx="71" cy="67" r="1.8" fill="{O}"/>
<path d="M58 80 Q64 86 70 80" fill="#fff" {s(T2)}/>
{BL.format(52, 78)}{BL.format(76, 78)}
<path d="M-6 92 Q12 82 30 92 T66 92 T102 92 T134 92 V134 H-6Z" fill="#35B6E6" {s()}/>
<path d="M30 86 q-8 -10 -16 -6 M98 86 q8 -10 16 -6 M44 84 q-2 -8 -8 -10 M84 84 q2 -8 8 -10" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
''', 50, 20)
SUBJ["spn-novogorsk"] = ("фиолетовый летучий мышонок в голубых плавательных очках",
                         "плывёт баттерфляем прямо на зрителя: оба перепончатых крыла взмахнули над водой, летят брызги, сзади луна")

# 5. «Пик Зевса», Химки — Зевс в плавательной шапочке ныряет с облака «ласточкой»
ICONS["pik-zevsa-khimki-michurina"] = W("#FFFFFF", "#F5B82E", f'''
<path d="M-6 100 Q26 90 58 100 T134 98 V134 H-6Z" fill="#2E9BE6" {s()}/>
<path d="M6 34 Q4 20 18 20 Q22 8 36 12 Q48 4 56 16 Q70 16 68 30 Q70 40 56 40 H16 Q4 42 6 34Z" fill="#fff" {s()}/>
<path d="M30 40 L22 56 H32 L26 72 L44 50 H34 L40 40Z" fill="#FFE03A" {s(T2)}/>
<g transform="rotate(38 82 62)">
<path d="M66 50 Q60 30 70 16 M98 50 Q104 30 94 16" fill="none" stroke="{O}" stroke-width="10" stroke-linecap="round"/>
<path d="M66 50 Q60 30 70 16 M98 50 Q104 30 94 16" fill="none" stroke="#F6C9A0" stroke-width="6" stroke-linecap="round"/>
<path d="M66 72 Q64 96 70 112 H94 Q100 96 98 72Z" fill="#fff" {s()}/>
<path d="M68 86 Q82 92 96 84" fill="none" stroke="#F5B82E" stroke-width="4"/>
<circle cx="82" cy="52" r="19" fill="#F6C9A0" {s()}/>
<path d="M64 46 Q66 30 82 30 Q98 30 100 46 Q82 38 64 46Z" fill="#E8483F" {s()}/>
<path d="M64 56 Q62 80 82 84 Q102 80 100 56 Q92 66 82 62 Q72 66 64 56Z" fill="#fff" {s()}/>
{eye(75, 51, .8)}{eye(89, 51, .8)}
<path d="M77 68 Q82 72 87 68" fill="none" {s(T2)}/>
</g>
<path d="M30 96 q-4 -10 4 -14 M44 98 q2 -8 10 -8" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
''', 30, 30)
SUBJ["pik-zevsa-khimki-michurina"] = ("седобородый Зевс в красной плавательной шапочке и белой тоге",
                                      "ныряет «ласточкой» с белого облака в синюю воду, из облака бьёт жёлтая молния")

# 6. «Мой Аква Старт», Подольск — воробышек на стартовой тумбе
ICONS["moy-akva-start-podolsk"] = W("#FFF3E4", "#FF8466", f'''
<path d="M-6 104 Q26 96 58 104 T134 102 V134 H-6Z" fill="#3FC3E8" {s()}/>
<path d="M20 108 L30 76 H78 L84 108Z" fill="#fff" {s()}/>
<path d="M24 76 L82 68 L84 78 H24Z" fill="#3D6BE0" {s()}/>
<circle cx="52" cy="94" r="9" fill="#FFD23F" {s(T2)}/>
<path d="M50 89 h3 v10" fill="none" {s(T2)}/>
<g transform="rotate(20 70 50)">
<path d="M40 52 L22 44 L24 58Z" fill="#8A5A34" {s()}/>
<ellipse cx="60" cy="52" rx="24" ry="18" fill="#B98250" {s()}/>
<path d="M44 48 Q56 36 72 46 Q60 62 44 48Z" fill="#8A5A34" {s()}/>
<circle cx="84" cy="38" r="15" fill="#C99466" {s()}/>
<path d="M70 34 Q84 20 98 34 Q84 28 70 34Z" fill="#7A4A28" {s()}/>
<path d="M74 44 Q84 54 96 44 Q86 50 74 44Z" fill="#F4E4CF"/>
<path d="M98 38 L110 42 L98 46Z" fill="#FFB02E" {s(T2)}/>
<rect x="74" y="33" width="22" height="9" rx="4.5" fill="#35D0E0" {s(T2)}/>
<circle cx="80" cy="37.5" r="1.7" fill="{O}"/><circle cx="90" cy="37.5" r="1.7" fill="{O}"/>
<path d="M56 68 v8 M66 68 v8" stroke="#FFB02E" stroke-width="3.4" stroke-linecap="round"/>
</g>
<path d="M104 70 l10 -4 M106 80 h12 M104 90 l10 4" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
''', 70, 20)
SUBJ["moy-akva-start-podolsk"] = ("коричневый воробышек в голубых плавательных очках",
                                  "наклонился вперёд на бело-синей стартовой тумбе с жёлтой цифрой «1» и готов прыгнуть в воду")

# 7. Aqua Baby Corp, Подольск — малыши с 1 месяца: пчёлка-малышка плавает в надувном круге
ICONS["aqua-baby-corp-podolsk"] = W("#FFFCE0", "#22BFC0", f'''
<path d="M-6 70 Q26 62 58 70 T134 68 V134 H-6Z" fill="#35D4DA" opacity=".55"/>
<ellipse cx="40" cy="38" rx="15" ry="10" fill="#fff" opacity=".9" {s(T2)} transform="rotate(-30 40 38)"/>
<ellipse cx="88" cy="38" rx="15" ry="10" fill="#fff" opacity=".9" {s(T2)} transform="rotate(30 88 38)"/>
<ellipse cx="64" cy="58" rx="24" ry="26" fill="#FFD23F" {s()}/>
<path d="M54 26 Q50 14 44 14 M74 26 Q78 14 84 14" fill="none" {s(T2)}/>
<circle cx="44" cy="14" r="3.4" fill="{O}"/><circle cx="84" cy="14" r="3.4" fill="{O}"/>
{eye(55, 50, 1.05)}{eye(73, 50, 1.05)}
<path d="M58 60 Q64 66 70 60" fill="none" {s(T2)}/>
{BL.format(47, 60)}{BL.format(81, 60)}
<ellipse cx="64" cy="88" rx="44" ry="19" fill="#FF6FA5" {s()}/>
<path d="M24 82 Q30 96 42 104 M104 82 Q98 96 86 104 M64 70 V78" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round"/>
<ellipse cx="64" cy="80" rx="22" ry="8" fill="#FFD23F" {s()}/>
<path d="M46 80 Q64 88 82 80" fill="none" stroke="{O}" stroke-width="5"/>
<path d="M12 112 q8 -5 16 0 M98 114 q8 -5 16 0 M52 118 q8 -5 16 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 50, 16)
SUBJ["aqua-baby-corp-podolsk"] = ("жёлтая пчёлка-малышка с прозрачными крылышками и усиками",
                                  "сидит в розовом надувном круге с белыми полосками посреди бирюзовой воды и улыбается")

# 8. «АкваКидс», Королёв — индивидуальные занятия с 2 месяцев: удавчик свернулся спасательным кругом
ICONS["akvakids-korolev-lesnaya"] = W("#F1FFE3", "#18A06A", f'''
<circle cx="64" cy="64" r="60" fill="#27C4D8" opacity=".5"/>
<circle cx="62" cy="68" r="32" fill="none" stroke="{O}" stroke-width="27"/>
<circle cx="62" cy="68" r="32" fill="none" stroke="#FFC233" stroke-width="21"/>
<circle cx="62" cy="68" r="32" fill="none" stroke="#FF7A2E" stroke-width="21" stroke-dasharray="14 36.3"/>
<path d="M90 50 Q104 40 100 24 Q96 10 82 12 Q68 16 72 30 Q74 40 84 44Z" fill="#FFC233" {s()}/>
{eye(80, 24, .85)}{eye(93, 24, .85)}
<path d="M82 34 Q88 38 94 33" fill="none" {s(T2)}/>
<path d="M88 37 v6 l-3 4 M88 43 l3 4" fill="none" stroke="#E8483F" stroke-width="2.4" stroke-linecap="round"/>
{BL.format(75, 32)}
<path d="M40 44 L26 30 Q24 26 28 26" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M40 44 L26 30 Q24 26 28 26" fill="none" stroke="#FFC233" stroke-width="5" stroke-linecap="round"/>
<circle cx="62" cy="68" r="17" fill="#27C4D8" {s(T2)}/>
<path d="M52 68 q5 -4 10 0 t10 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 40, 30)
SUBJ["akvakids-korolev-lesnaya"] = ("жёлтый удавчик в оранжевую полоску с красным язычком",
                                    "свернулся кольцом, как спасательный круг, и плавает по воде, подняв голову и кончик хвоста")

# 9. «Маленький пловец», Мытищи — крошечная килька в огромных очках плывёт во главе стайки пузырей
ICONS["malenkiy-plovets-mytishchi"] = W("#F4F8FB", "#3F6FA0", f'''
<path d="M-6 20 Q30 34 64 22 T134 26" fill="none" stroke="#fff" stroke-width="4" opacity=".6"/>
<path d="M30 78 L8 60 Q14 78 8 98Z" fill="#8FA8C0" {s()}/>
<path d="M26 78 Q46 56 76 58 Q104 62 114 78 Q104 94 76 98 Q46 100 26 78Z" fill="#C9D8E6" {s()}/>
<path d="M30 80 Q60 70 112 78 Q104 94 76 98 Q46 100 30 80Z" fill="#F4FAFF"/>
<path d="M56 60 Q64 48 76 58Z" fill="#8FA8C0" {s()}/>
<path d="M26 78 Q46 56 76 58 Q104 62 114 78" fill="none" stroke="#4E7FB8" stroke-width="5" stroke-linecap="round" opacity=".7"/>
<path d="M60 66 H118" stroke="{O}" stroke-width="4"/>
<circle cx="84" cy="72" r="13" fill="#FFE03A" {s()}/><circle cx="84" cy="72" r="8.5" fill="#BFF3FF" {s(T2)}/>
{eye(85, 72, .95)}
<path d="M100 86 Q106 88 110 84" fill="none" {s(T2)}/>
{bub(104, 44, 7)}{bub(116, 30, 4.4)}{bub(92, 30, 3.4)}
<path d="M40 108 q6 -4 12 0 M70 114 q6 -4 12 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
''', 30, 26)
SUBJ["malenkiy-plovets-mytishchi"] = ("серебристая рыбка-килька в огромных жёлтых плавательных очках",
                                      "плывёт одна в серо-синей воде, из-под очков смотрит большой глаз, вверх убегают три пузыря")

# 10. «Маленький пловец», Балашиха — Дюймовочка в купальной шапочке плывёт кролем между листьями кувшинок
ICONS["malenkiy-plovets-balashikha"] = W("#F6FFD9", "#1F8F5A", f'''
<rect x="-6" y="-6" width="140" height="140" fill="#2FB7A0" opacity=".45"/>
<path d="M4 34 Q8 10 36 12 Q58 16 56 38 L34 36 L44 54 Q14 60 4 34Z" fill="#6FCB4A" {s()}/>
<path d="M30 34 L12 24 M30 34 L20 48 M30 34 L44 20" stroke="#3E9A32" stroke-width="2.4" stroke-linecap="round"/>
<path d="M72 112 Q70 90 96 88 Q122 90 122 110 L100 108 L110 126 Q78 130 72 112Z" fill="#6FCB4A" {s()}/>
<path d="M98 26 Q90 12 100 6 Q108 12 104 26 Q116 16 122 24 Q116 36 104 34 Q112 44 100 46 Q90 40 96 32 Q84 36 82 26 Q88 18 98 26Z" fill="#FF8FC0" {s()}/>
<circle cx="100" cy="29" r="4.4" fill="#FFE03A" {s(T2)}/>
<path d="M22 96 Q40 84 58 92" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".85"/>
<path d="M14 108 Q30 100 46 106" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".7"/>
<path d="M44 86 Q30 96 20 88" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M44 86 Q30 96 20 88" fill="none" stroke="#FF6FA5" stroke-width="5" stroke-linecap="round"/>
<ellipse cx="50" cy="84" rx="14" ry="9" fill="#FF6FA5" {s()} transform="rotate(-24 50 84)"/>
<path d="M62 70 Q74 44 96 52" fill="none" stroke="{O}" stroke-width="10" stroke-linecap="round"/>
<path d="M62 70 Q74 44 96 52" fill="none" stroke="#FFD9B8" stroke-width="6" stroke-linecap="round"/>
<circle cx="72" cy="72" r="17" fill="#FFD9B8" {s()}/>
<path d="M56 68 Q58 52 74 54 Q88 56 88 70 Q72 60 56 68Z" fill="#FFE03A" {s()}/>
{eye(68, 74, .85)}{eye(81, 75, .85)}
<path d="M71 82 Q75 86 79 82" fill="none" {s(T2)}/>
{BL.format(62, 81)}{BL.format(86, 82)}
<path d="M58 80 Q52 92 58 98" fill="none" stroke="#C9772E" stroke-width="5" stroke-linecap="round"/>
''', 30, 24)
SUBJ["malenkiy-plovets-balashikha"] = ("крошечная Дюймовочка с рыжей косичкой в жёлтой купальной шапочке",
                                       "плывёт кролем по зелёному пруду между двумя листьями кувшинок, рядом розовый цветок кувшинки")

# 11. «Море детям», Мытищи — малыш-Нептун в короне сидит в лодочке и правит трезубцем
ICONS["more-detyam-mytishchi"] = W("#D9FFFA", "#3440A8", f'''
<path d="M-6 84 Q26 76 58 84 T134 82 V134 H-6Z" fill="#2B7BE0" {s()}/>
<path d="M98 16 V92" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M98 16 V92" stroke="#FFD23F" stroke-width="3.4" stroke-linecap="round"/>
<path d="M86 14 V28 Q86 36 98 36 Q110 36 110 28 V14" fill="none" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M86 14 V28 Q86 36 98 36 Q110 36 110 28 V14" fill="none" stroke="#FFD23F" stroke-width="3.4" stroke-linecap="round"/>
<circle cx="56" cy="56" r="24" fill="#FFD9B8" {s()}/>
<path d="M36 40 L38 20 L48 32 L56 16 L64 32 L74 20 L76 40Z" fill="#FFD23F" {s()}/>
<circle cx="56" cy="30" r="3" fill="#E8483F"/>
{eye(47, 54, 1.0)}{eye(65, 54, 1.0)}
<path d="M34 62 Q36 90 56 92 Q76 90 78 62 Q70 72 62 66 Q56 72 50 66 Q42 72 34 62Z" fill="#fff" {s()}/>
<path d="M51 68 Q56 72 61 68" fill="none" {s(T2)}/>
<path d="M78 70 Q88 68 94 62" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M78 70 Q88 68 94 62" fill="none" stroke="#FFD9B8" stroke-width="5" stroke-linecap="round"/>
<path d="M-6 96 Q26 88 58 96 T134 94 V134 H-6Z" fill="#2B7BE0"/>
<path d="M-6 96 Q26 88 58 96 T134 94" fill="none" {s()}/>
<path d="M14 112 q8 -5 16 0 M74 114 q8 -5 16 0" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
''', 40, 20)
SUBJ["more-detyam-mytishchi"] = ("малыш-Нептун в золотой короне с белой бородой из пены",
                                 "выглядывает по плечи из синего моря и держит рядом золотой трезубец")

# 12. «Счастливый дельфин», Юбилейный — морской петух распустил плавники-веер и хохочет
ICONS["schastlivy-delfin-tikhonravova"] = W("#FFEAF3", "#D63C8C", f'''
<path d="M62 66 Q24 20 4 44 Q0 70 30 84 Q48 86 62 66Z" fill="#3D6BE0" {s()}/>
<path d="M62 66 Q100 20 120 44 Q124 70 94 84 Q76 86 62 66Z" fill="#3D6BE0" {s()}/>
<path d="M62 66 L14 46 M62 66 L18 68 M62 66 L32 80 M62 66 L110 46 M62 66 L106 68 M62 66 L92 80" stroke="#8FE3FF" stroke-width="3" stroke-linecap="round"/>
<circle cx="16" cy="54" r="3" fill="#FFE03A"/><circle cx="108" cy="54" r="3" fill="#FFE03A"/><circle cx="28" cy="70" r="3" fill="#FFE03A"/><circle cx="96" cy="70" r="3" fill="#FFE03A"/>
<path d="M50 96 L42 118 Q62 110 82 118 L74 96Z" fill="#FF9E3D" {s()}/>
<path d="M40 60 Q40 34 62 34 Q84 34 84 60 Q84 100 62 102 Q40 100 40 60Z" fill="#FF6A3D" {s()}/>
<path d="M52 36 L56 22 L62 34 L68 22 L72 36Z" fill="#FF9E3D" {s(T2)}/>
{eye(52, 56, 1.1)}{eye(72, 56, 1.1)}
<path d="M50 70 Q62 90 74 70Z" fill="#7A1F3D" {s(T2)}/>
<path d="M56 80 Q62 76 68 80 Q62 86 56 80Z" fill="#FF8FB0"/>
{BL.format(44, 68)}{BL.format(80, 68)}
{bub(104, 100, 5)}{bub(22, 104, 4)}
''', 50, 24)
SUBJ["schastlivy-delfin-tikhonravova"] = ("оранжевая рыба морской петух с синими плавниками-крыльями в жёлтый горошек",
                                          "смотрит прямо на зрителя, распустив плавники веером во весь кадр, и хохочет с открытым ртом")

# 13. «Счастливый дельфин», Октябрьский бульвар — маска с трубкой выглядывает из воды и пускает фонтанчик
ICONS["schastlivy-delfin-oktyabrsky"] = W("#FFFFFF", "#19C3E6", f'''
<path d="M94 74 V26 Q94 14 106 14" fill="none" stroke="{O}" stroke-width="13" stroke-linecap="round"/>
<path d="M94 74 V26 Q94 14 106 14" fill="none" stroke="#FF5A4D" stroke-width="8" stroke-linecap="round"/>
<path d="M94 40 V30" stroke="#fff" stroke-width="8"/>
<path d="M112 10 q8 -6 10 4 M114 20 q10 0 8 10" fill="none" stroke="#19A8D6" stroke-width="3.4" stroke-linecap="round"/>
<circle cx="124" cy="24" r="2.6" fill="#19A8D6"/>
<path d="M14 62 Q14 40 36 40 H84 Q104 40 104 62 Q104 86 84 88 Q70 88 64 78 Q58 88 44 88 Q14 88 14 62Z" fill="#FFD23F" {s()}/>
<path d="M24 62 Q24 50 38 50 H82 Q94 50 94 62 Q94 78 82 78 Q72 78 64 66 Q56 78 46 78 Q24 78 24 62Z" fill="#C8F4FF" {s(T2)}/>
{eye(46, 63, 1.15)}{eye(80, 63, 1.15)}
<path d="M30 56 q6 -4 12 -2" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M14 62 H2 M104 62 H112" stroke="{O}" stroke-width="6" stroke-linecap="round"/>
<path d="M-6 88 Q12 80 30 88 T66 88 T102 88 T134 88 V134 H-6Z" fill="#1E9BE0" {s()}/>
<path d="M20 106 q8 -5 16 0 M60 112 q8 -5 16 0 M94 104 q8 -5 16 0" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
''', 30, 80)
SUBJ["schastlivy-delfin-oktyabrsky"] = ("жёлтая маска для плавания с глазами за стеклом и красной трубкой",
                                        "наполовину выглядывает из синей воды, а из трубки вылетают капли фонтанчиком")

# 14. Школа плавания № 1, Каширское ш. — малыши на малой глубине: щенок ретривера плывёт «по-собачьи» с кольцом в зубах
ICONS["ss1-kashirskoe-65"] = W("#FFF9EC", "#17A6A0", f'''
<path d="M-6 66 Q12 58 30 66 T66 66 T102 66 T134 66 V134 H-6Z" fill="#3FD0CC" {s()}/>
<path d="M22 70 Q30 56 44 62" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M22 70 Q30 56 44 62" fill="none" stroke="#E9B45C" stroke-width="5" stroke-linecap="round"/>
<circle cx="72" cy="50" r="26" fill="#F2C572" {s()}/>
<path d="M50 34 Q36 36 38 60 Q44 66 52 56Z M94 34 Q108 36 106 60 Q100 66 92 56Z" fill="#D99A3F" {s()}/>
<ellipse cx="72" cy="60" rx="14" ry="11" fill="#FFF1D2" {s(T2)}/>
<ellipse cx="72" cy="54" rx="5" ry="3.6" fill="{O}"/>
{eye(61, 44, 1.0)}{eye(83, 44, 1.0)}
<ellipse cx="72" cy="72" rx="15" ry="7" fill="none" stroke="{O}" stroke-width="10"/>
<ellipse cx="72" cy="72" rx="15" ry="7" fill="none" stroke="#FF4F7B" stroke-width="5.5"/>
<path d="M-6 80 Q12 72 30 80 T66 80 T102 80 T134 80 V134 H-6Z" fill="#3FD0CC"/>
<path d="M40 82 Q46 74 52 82 M92 82 Q98 74 104 82" fill="#F2C572" {s()}/>
<path d="M30 84 q-6 -8 -12 -4 M114 84 q6 -8 12 -4" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
<path d="M20 104 q8 -5 16 0 M58 112 q8 -5 16 0 M92 102 q8 -5 16 0" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
''', 50, 20)
SUBJ["ss1-kashirskoe-65"] = ("золотистый щенок ретривера с висячими ушами",
                             "плывёт «по-собачьи» на зрителя, из бирюзовой воды торчат голова, лапки и хвост, в зубах розовое кольцо для ныряния")

# 15. «Морские звёзды», Коммунарка — нутрия лежит на спине в ночной воде и ловит отражение звезды
ICONS["morskie-zvezdy-kommunarka"] = W("#5E6FD8", "#161C54", f'''
{sparkle(22, 24, 7, "#FFE98A")}{sparkle(98, 18, 9, "#FFE98A")}{sparkle(60, 12, 4.4)}{sparkle(116, 46, 4)}{sparkle(40, 44, 3.4)}
<path d="M-6 70 Q26 62 58 70 T134 68 V134 H-6Z" fill="#2A49B8" {s()}/>
<path d="M18 92 Q4 96 -2 86" fill="none" stroke="{O}" stroke-width="8" stroke-linecap="round"/>
<path d="M18 92 Q4 96 -2 86" fill="none" stroke="#C98A6B" stroke-width="4" stroke-linecap="round"/>
<ellipse cx="54" cy="90" rx="38" ry="17" fill="#8A5A3C" {s()}/>
<ellipse cx="54" cy="86" rx="26" ry="10" fill="#C9966E"/>
<circle cx="96" cy="78" r="18" fill="#8A5A3C" {s()}/>
<circle cx="86" cy="62" r="4.6" fill="#8A5A3C" {s(T2)}/><circle cx="106" cy="62" r="4.6" fill="#8A5A3C" {s(T2)}/>
<ellipse cx="97" cy="84" rx="10" ry="7.5" fill="#E8C9A8" {s(T2)}/>
<ellipse cx="97" cy="79" rx="3.4" ry="2.4" fill="{O}"/>
<rect x="93.5" y="84" width="7" height="7" rx="1.5" fill="#FF8A1E" {s('stroke-width="1.8"')}/>
<path d="M97 84 v7" stroke="{O}" stroke-width="1.4"/>
{eye(90, 72, .8)}{eye(104, 72, .8)}
<path d="M40 80 Q44 68 52 72 M66 80 Q64 68 56 72" fill="none" stroke="{O}" stroke-width="8" stroke-linecap="round"/>
<path d="M40 80 Q44 68 52 72 M66 80 Q64 68 56 72" fill="none" stroke="#8A5A3C" stroke-width="4" stroke-linecap="round"/>
{sparkle(54, 64, 8, "#FFE98A")}
<path d="M10 112 q8 -5 16 0 M58 116 q8 -5 16 0 M100 110 q8 -5 16 0" fill="none" stroke="#9FB6FF" stroke-width="3.4" stroke-linecap="round"/>
''', 40, 20)
SUBJ["morskie-zvezdy-kommunarka"] = ("бурая нутрия с оранжевыми зубами и круглыми ушками",
                                     "лежит на спине в тёмно-синей ночной воде и держит в лапках жёлтую звёздочку, в небе звёзды")

if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for i in ids:
        open(os.path.join(OUT, i + ".svg"), "w", encoding="utf-8").write(ICONS[i])
    print("svg:", len(ids))
    for i in ids:
        print(f"{i} — герой: {SUBJ[i][0]} | сцена: {SUBJ[i][1]}")
