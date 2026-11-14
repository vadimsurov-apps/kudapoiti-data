"""Иконки робота pools, 2026-11-14 (11 UTC). Каждая придумана и нарисована отдельно (правило абсолютной
уникальности): свой герой, своя сцена, своя компоновка и палитра. Герои сверены с реестром icons-src/subjects.txt
(таких героев в реестре нет), картинки — tools/check_unique.py.
Запуск: python3 tools/icons_pools_1114k.py [id …]  → python3 tools/render_icons.py <id…> → python3 tools/check_unique.py <id…>."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, sparkle, O
from icons_pools_1112b import W, bub, T2

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
BL = '<ellipse cx="{}" cy="{}" rx="4.4" ry="2.6" fill="#FF7FA8" opacity=".8"/>'
T3 = 'stroke-width="3"'

# 1. Школа плавания № 1, открытый подогреваемый бассейн «Чайка» — рыжая утка огарь плывёт зимой в парящей воде
ICONS["ss1-chayka-turchaninov"] = W("#DCEBFA", "#8FB4E0", f'''
<circle cx="22" cy="22" r="3" fill="#fff"/><circle cx="52" cy="12" r="2.4" fill="#fff"/><circle cx="96" cy="20" r="3" fill="#fff"/><circle cx="112" cy="44" r="2.4" fill="#fff"/><circle cx="12" cy="52" r="2.2" fill="#fff"/>
<path d="M-6 84 Q30 76 64 84 T134 82 V134 H-6Z" fill="#1F9FB8" {s()}/>
<path d="M30 60 q-8 -10 0 -18 q8 -8 0 -18 M100 62 q8 -10 0 -18 q-8 -8 0 -16" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".75"/>
<path d="M30 86 Q34 62 62 64 Q92 64 104 80 Q96 100 64 100 Q38 100 30 86Z" fill="#E0762B" {s()}/>
<path d="M92 72 L112 62 Q110 82 98 86Z" fill="#2B2B33" {s(T2)}/>
<path d="M58 76 Q76 68 92 80 Q76 88 58 76Z" fill="#fff" {s(T2)}/>
<circle cx="42" cy="56" r="17" fill="#F6D9A6" {s()}/>
<path d="M27 60 L10 64 L27 68Z" fill="#2B2B33" {s(T2)}/>
{eye(40, 54, 1.15)}
{BL.format(48, 63)}
<path d="M12 104 q8 -5 16 0 M52 110 q8 -5 16 0 M92 104 q8 -5 16 0" fill="none" stroke="#BFF0F7" stroke-width="3" stroke-linecap="round"/>
''', 50, 20)
SUBJ["ss1-chayka-turchaninov"] = ("рыжая утка огарь с кремовой головой и чёрным хвостом",
                                  "плывёт зимой по открытому бассейну с подогревом — над бирюзовой водой поднимаются два столбика белого пара, с серо-голубого неба падает снег")

# 2. Школа плавания № 1, «Меридиан» — круглая рыба пинагор в полосках-меридианах катится между дорожками
ICONS["ss1-meridian"] = W("#0E8C8C", "#064E5C", f'''
<path d="M-4 30 H132 M-4 104 H132" stroke="#fff" stroke-width="5" stroke-dasharray="10 8"/>
<path d="M-4 30 H132 M-4 104 H132" stroke="#FF5A4E" stroke-width="5" stroke-dasharray="10 8" stroke-dashoffset="9"/>
<path d="M94 58 L118 44 L112 67 L118 90 L94 76Z" fill="#F2B632" {s()}/>
<circle cx="60" cy="67" r="34" fill="#FFD95C" {s()}/>
<path d="M60 33 Q40 67 60 101 M60 33 Q80 67 60 101 M28 60 Q60 50 92 60 M30 80 Q60 90 90 80" fill="none" stroke="#E08A1E" stroke-width="3" stroke-linecap="round"/>
<path d="M48 34 Q60 20 72 34Z" fill="#F2B632" {s(T2)}/>
{eye(44, 62, 1.25)}{eye(64, 62, 1.25)}
<path d="M46 76 Q54 84 62 76" fill="none" {s(T2)}/>
{BL.format(36, 72)}{BL.format(72, 72)}
{bub(18, 60, 4)}{bub(10, 76, 2.6)}
''', 46, 40)
SUBJ["ss1-meridian"] = ("круглая жёлтая рыба пинагор, расчерченная оранжевыми линиями-меридианами, как глобус",
                        "катится шариком по тёмно-бирюзовой воде между двумя красно-белыми разделительными дорожками")

# 3. Школа плавания № 1, бассейн педагогического университета — утка пеганка ведёт трёх птенцов цепочкой
ICONS["ss1-mgpu"] = W("#FFF6C9", "#FFD46B", f'''
<path d="M-6 72 Q30 64 64 72 T134 70 V134 H-6Z" fill="#3D8DE0" {s()}/>
<circle cx="46" cy="84" r="8" fill="#FFF" {s(T2)}/><path d="M40 79 q6 -6 12 0" fill="#6B4A2E" {s(T2)}/><path d="M53 84 l7 2 l-7 2Z" fill="#E8483F"/>
<circle cx="30" cy="96" r="8" fill="#FFF" {s(T2)}/><path d="M24 91 q6 -6 12 0" fill="#6B4A2E" {s(T2)}/><path d="M37 96 l7 2 l-7 2Z" fill="#E8483F"/>
<circle cx="46" cy="110" r="8" fill="#FFF" {s(T2)}/><path d="M40 105 q6 -6 12 0" fill="#6B4A2E" {s(T2)}/><path d="M53 110 l7 2 l-7 2Z" fill="#E8483F"/>
<circle cx="47" cy="84" r="1.8" fill="{O}"/><circle cx="31" cy="96" r="1.8" fill="{O}"/><circle cx="47" cy="110" r="1.8" fill="{O}"/>
<path d="M62 80 Q64 58 88 60 Q110 62 116 76 Q110 92 88 92 Q68 92 62 80Z" fill="#fff" {s()}/>
<path d="M72 66 Q86 62 98 68 L96 82 Q84 76 72 80Z" fill="#B5562A" {s(T2)}/>
<path d="M102 66 L120 60 Q118 76 110 80Z" fill="#23303F" {s(T2)}/>
<path d="M92 62 Q84 44 94 34" fill="none" stroke="#1F4D3A" stroke-width="12" stroke-linecap="round"/>
<circle cx="96" cy="34" r="13" fill="#1F4D3A" {s()}/>
<path d="M106 30 Q122 28 120 40 Q110 40 106 38Z" fill="#E8483F" {s(T2)}/>
<circle cx="108" cy="25" r="4" fill="#E8483F" {s(T2)}/>
{eye(98, 33, 1.0)}
''', 30, 16)
SUBJ["ss1-mgpu"] = ("белая утка пеганка с тёмно-зелёной головой, красным клювом с шишкой и рыжей перевязью",
                    "как учительница ведёт по синей воде трёх пушистых птенцов — они плывут за ней цепочкой, небо солнечно-жёлтое")

# 4. Школа плавания № 1, бассейн юридической академии — радужный рак-богомол судит заплыв со свистком
ICONS["ss1-mgyua"] = W("#3A2A66", "#1B1238", f'''
<path d="M-6 96 Q30 88 64 96 T134 94 V134 H-6Z" fill="#2CC4C9" {s()}/>
<path d="M40 100 Q30 70 44 48 Q58 30 78 44 Q92 56 86 80 Q84 92 88 100Z" fill="#35C46A" {s()}/>
<path d="M44 86 Q64 78 86 86 M42 72 Q62 64 86 72 M46 58 Q62 50 84 60" fill="none" stroke="#F2D13B" stroke-width="3"/>
<path d="M50 44 Q40 22 30 20 M70 40 Q78 20 90 18" fill="none" {s(T2)}/>
<circle cx="30" cy="18" r="8" fill="#FF5FA2" {s(T2)}/><circle cx="92" cy="16" r="8" fill="#FF5FA2" {s(T2)}/>
<circle cx="30" cy="18" r="3" fill="{O}"/><circle cx="92" cy="16" r="3" fill="{O}"/>
<path d="M44 64 Q22 60 18 76 Q24 90 40 80Z" fill="#FF8A3C" {s(T2)}/>
<path d="M84 62 Q104 54 110 44" fill="none" stroke="#FF8A3C" stroke-width="8" stroke-linecap="round"/>
<rect x="100" y="32" width="18" height="12" rx="5" fill="#F2D13B" {s(T2)}/><rect x="90" y="35" width="12" height="6" rx="2" fill="#F2D13B" {s(T2)}/>
<path d="M56 54 Q64 60 72 54" fill="none" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>
<path d="M118 22 l6 -6 M122 30 l8 -2 M112 18 l2 -8" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<path d="M10 110 q8 -5 16 0 M96 112 q8 -5 16 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
''', 60, 30)
SUBJ["ss1-mgyua"] = ("зелёный рак-богомол в жёлтую полоску с розовыми глазами на стебельках и оранжевой клешнёй",
                     "стоит по пояс в бирюзовой воде и, как судья заплыва, свистит в жёлтый свисток, фон тёмно-фиолетовый")

# 5. Школа плавания № 1, бассейн МосГУ — длинная серебристая рыба арована плывёт на спине
ICONS["ss1-mosgu"] = W("#CFF5E6", "#59C9A5", f'''
<path d="M-6 58 Q30 50 64 58 T134 56 V134 H-6Z" fill="#1B6FA8" {s()}/>
<path d="M12 78 Q10 62 34 60 L96 60 Q116 62 118 74 Q112 88 92 88 L36 90 Q16 92 12 78Z" fill="#DDE7EE" {s()}/>
<path d="M40 62 q6 13 0 26 M54 61 q6 13 0 27 M68 61 q6 13 0 27 M82 61 q6 13 0 27" fill="none" stroke="#9FB3C2" stroke-width="2.6"/>
<path d="M14 74 L-2 60 L2 78 L-4 94Z" fill="#F26D5B" {s(T2)}/>
<path d="M50 60 Q64 42 82 58Z" fill="#F26D5B" {s(T2)}/>
<path d="M88 66 Q100 44 110 34" fill="none" stroke="#DDE7EE" stroke-width="8" stroke-linecap="round"/>
<path d="M88 66 Q100 44 110 34" fill="none" {s(T2)}/>
<path d="M116 70 q8 -2 10 -8 M116 76 q8 2 10 8" fill="none" {s(T2)}/>
{eye(104, 72, 1.1)}
<path d="M96 82 Q102 86 108 82" fill="none" {s(T2)}/>
<path d="M20 106 q8 -5 16 0 M60 112 q8 -5 16 0 M96 104 q8 -5 16 0" fill="none" stroke="#9BD8F5" stroke-width="3" stroke-linecap="round"/>
{sparkle(30, 30, 7)}{sparkle(84, 22, 5)}
''', 30, 20)
SUBJ["ss1-mosgu"] = ("длинная серебристая рыба арована в крупной чешуе с красным хвостом и двумя усиками",
                     "плывёт на спине по синей воде, закинув длинный грудной плавник назад, как рука в гребке, небо мятно-зелёное")

# 6. Школа плавания № 1, «Некрасовка» (чаша из нержавеющей стали) — красная нерка прыгает над стальной чашей
ICONS["ss1-nekrasovka"] = W("#EAF0F5", "#A9B8C6", f'''
<path d="M10 92 H118 Q118 124 64 124 Q10 124 10 92Z" fill="#C9D3DC" {s()}/>
<ellipse cx="64" cy="92" rx="54" ry="13" fill="#39B7E6" {s()}/>
<path d="M24 104 Q30 116 46 120" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".9"/>
<path d="M30 78 Q34 34 74 28 Q98 26 106 40 Q92 62 64 68 Q44 72 40 86Z" fill="#E23B3B" {s()}/>
<path d="M30 78 L18 92 L36 96 L48 86Z" fill="#B32626" {s(T2)}/>
<path d="M62 30 Q66 14 82 20 L78 30Z" fill="#B32626" {s(T2)}/>
<path d="M82 28 Q102 22 108 40 Q100 52 86 50 Q78 40 82 28Z" fill="#4E9A51" {s(T2)}/>
<path d="M104 42 l8 4 l-9 3" fill="none" {s(T2)}/>
{eye(94, 36, 1.1)}
<path d="M52 56 q6 -8 14 -8" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
<circle cx="50" cy="84" r="3" fill="#fff"/><circle cx="76" cy="80" r="2.4" fill="#fff"/><circle cx="64" cy="76" r="2" fill="#fff"/>
''', 40, 24)
SUBJ["ss1-nekrasovka"] = ("ярко-красная рыба нерка с зелёной головой",
                          "выпрыгивает дугой из блестящей стальной чаши с голубой водой, за хвостом летят капли, фон серебристо-серый")

# 7. Школа плавания № 1, «Ника» (богиня победы, крылья) — птица скопа пикирует в воду лапами вперёд
ICONS["ss1-nika-volzhsky"] = W("#FFE3D1", "#FF9E7D", f'''
<path d="M-6 102 Q30 94 64 102 T134 100 V134 H-6Z" fill="#136B8A" {s()}/>
<path d="M58 44 Q20 30 6 6 Q34 12 62 30Z" fill="#6B4A36" {s()}/>
<path d="M70 44 Q108 30 122 6 Q94 12 66 30Z" fill="#6B4A36" {s()}/>
<path d="M48 42 Q64 26 80 42 Q82 68 64 78 Q46 68 48 42Z" fill="#fff" {s()}/>
<circle cx="64" cy="34" r="15" fill="#fff" {s()}/>
<path d="M48 32 Q64 26 80 32 L80 38 Q64 32 48 38Z" fill="#3B2A22"/>
<path d="M60 40 L64 50 L68 40Z" fill="#3B3355" {s(T2)}/>
{eye(57, 34, 0.95)}{eye(71, 34, 0.95)}
<path d="M56 76 L52 94 M72 76 L76 94" fill="none" stroke="#F2B632" stroke-width="6" stroke-linecap="round"/>
<path d="M46 96 l6 -4 l6 4 M70 96 l6 -4 l6 4" fill="none" {s(T2)}/>
<path d="M40 106 q-6 -10 -14 -8 M88 106 q6 -10 14 -8 M64 108 v-8" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
''', 50, 30)
SUBJ["ss1-nika-volzhsky"] = ("птица скопа с белой грудью, коричневыми крыльями и тёмной маской на глазах",
                             "пикирует с раскинутыми вверх крыльями и жёлтыми лапами вперёд в тёмно-синюю воду, уже летят брызги, небо персиковое")

# 8. Школа плавания № 1, «Профсоюзная» (небольшой тёплый бассейн глубиной 1,2 м) — птица якана шагает по кувшинкам
ICONS["ss1-profsoyuznaya"] = W("#B7F0E0", "#3CC2A2", f'''
<rect x="-6" y="70" width="140" height="64" fill="#0E7F8F" {s()}/>
<ellipse cx="30" cy="98" rx="24" ry="9" fill="#7BD657" {s(T2)}/><path d="M30 98 L52 92" stroke="{O}" stroke-width="2.4"/>
<ellipse cx="86" cy="106" rx="26" ry="9" fill="#7BD657" {s(T2)}/><path d="M86 106 L64 100" stroke="{O}" stroke-width="2.4"/>
<ellipse cx="112" cy="84" rx="16" ry="6" fill="#5FC243" {s(T2)}/>
<path d="M52 66 L40 94 M40 94 l-12 2 M40 94 l-4 8 M40 94 l10 4" fill="none" stroke="#7FA6B8" stroke-width="3.4" stroke-linecap="round"/>
<path d="M68 66 L84 100 M84 100 l-12 4 M84 100 l2 9 M84 100 l12 2" fill="none" stroke="#7FA6B8" stroke-width="3.4" stroke-linecap="round"/>
<path d="M36 56 Q40 36 62 38 Q84 40 90 56 Q80 72 60 70 Q42 70 36 56Z" fill="#8A4B2A" {s()}/>
<path d="M36 56 L20 50 L30 64Z" fill="#5E2F18" {s(T2)}/>
<path d="M56 46 Q70 42 82 52 Q70 58 56 46Z" fill="#F2C53B" {s(T2)}/>
<path d="M80 46 Q84 26 96 20" fill="none" stroke="#23303F" stroke-width="10" stroke-linecap="round"/>
<circle cx="98" cy="18" r="11" fill="#23303F" {s()}/>
<path d="M96 6 Q104 2 108 12 Q102 14 96 12Z" fill="#3EA8F0" {s(T2)}/>
<path d="M107 16 L122 20 L107 23Z" fill="#F2C53B" {s(T2)}/>
<circle cx="100" cy="18" r="3.4" fill="#fff"/><circle cx="101" cy="18" r="1.8" fill="{O}"/>
''', 30, 20)
SUBJ["ss1-profsoyuznaya"] = ("каштановая птица якана с чёрной шеей, голубой бляшкой на лбу и длиннющими пальцами",
                             "шагает по мелкой бирюзовой воде с одного листа кувшинки на другой, не проваливаясь, фон светло-мятный")

# 9. Школа плавания № 1, «Союз» — чёрная рыбка лабео с красным хвостом несётся, как ракета
ICONS["ss1-soyuz"] = W("#2E5BD9", "#12205E", f'''
<path d="M10 118 L40 88 M4 96 L30 74 M30 124 L52 100" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".55"/>
<path d="M34 96 L10 106 L20 86 L14 66Z" fill="#FF4A3D" {s()}/>
<path d="M30 92 Q38 52 78 30 Q104 20 112 26 Q112 46 92 68 Q62 96 30 92Z" fill="#2B2B33" {s()}/>
<path d="M58 44 Q62 26 80 22 L76 36Z" fill="#FF4A3D" {s(T2)}/>
<path d="M70 78 Q84 86 90 74 L80 68Z" fill="#FF4A3D" {s(T2)}/>
<circle cx="92" cy="40" r="9" fill="#fff" {s(T2)}/><circle cx="94" cy="39" r="4.6" fill="{O}"/><circle cx="92.6" cy="37.4" r="1.6" fill="#fff"/>
<path d="M100 54 Q106 54 108 48" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<path d="M48 70 q10 -14 22 -20" fill="none" stroke="#6E6E7A" stroke-width="3" stroke-linecap="round"/>
{sparkle(108, 92, 7, "#FFE27A")}{sparkle(20, 30, 6, "#FFE27A")}{sparkle(60, 112, 4, "#FFE27A")}
{bub(46, 108, 4)}{bub(34, 116, 2.6)}
''', 70, 30)
SUBJ["ss1-soyuz"] = ("бархатно-чёрная рыбка лабео с алым хвостом и алыми плавниками",
                     "несётся по диагонали вверх, как ракета, оставляя за хвостом три белые струи, вокруг жёлтые звёздочки, вода густо-синяя")

# 10. Школа плавания № 1, Дворец спорта «Янтарь» — оранжевая рыбка пецилия в капле янтаря-воды
ICONS["ss1-yantar"] = W("#FFF1B8", "#F2A93B", f'''
<path d="M64 8 Q106 58 106 82 A42 42 0 0 1 22 82 Q22 58 64 8Z" fill="#FFC93B" {s()}/>
<path d="M64 22 Q96 62 96 82 A32 32 0 0 1 32 82 Q32 62 64 22Z" fill="#FFDF7A" opacity=".8"/>
<path d="M36 84 L22 72 L26 86 L20 100Z" fill="#E8542A" {s(T2)}/>
<path d="M34 86 Q38 66 60 66 Q82 66 90 82 Q82 100 60 100 Q40 100 34 86Z" fill="#FF7A2E" {s()}/>
<path d="M52 68 Q60 54 74 66Z" fill="#E8542A" {s(T2)}/>
<path d="M56 98 Q62 108 72 98Z" fill="#E8542A" {s(T2)}/>
<circle cx="46" cy="84" r="3" fill="#2B2B33"/><circle cx="54" cy="90" r="2.4" fill="#2B2B33"/>
{eye(74, 80, 1.15)}
<path d="M72 90 Q78 94 84 89" fill="none" {s(T2)}/>
{BL.format(66, 88)}
<path d="M48 36 Q40 48 38 60" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".9"/>
{bub(100, 30, 5)}{bub(112, 46, 3)}
''', 50, 30)
SUBJ["ss1-yantar"] = ("оранжевая рыбка пецилия с двумя чёрными крапинками на боку",
                      "плавает внутри большой прозрачной капли янтарно-жёлтой воды, на капле белый блик, фон медовый")

# 11. Школа плавания № 1, «Парк Победы» — серебристый омуль финиширует, касаясь бортика, в лавровом венке
ICONS["ss1-park-pobedy"] = W("#E9F7D9", "#9AD06A", f'''
<rect x="-6" y="52" width="140" height="82" fill="#2A8FD6" {s()}/>
<rect x="102" y="40" width="32" height="94" fill="#F4F6F8" {s()}/>
<path d="M102 62 H134 M102 84 H134 M102 106 H134 M118 40 V134" stroke="#B9C6D1" stroke-width="2.4"/>
<path d="M22 86 L4 72 L8 88 L2 104Z" fill="#7C8FA0" {s(T2)}/>
<path d="M18 88 Q24 66 54 66 Q84 66 94 84 Q84 104 54 104 Q28 104 18 88Z" fill="#D7E1EA" {s()}/>
<path d="M22 86 Q54 74 92 82" fill="none" stroke="#7C8FA0" stroke-width="3"/>
<path d="M80 84 Q92 70 102 68" fill="none" stroke="#D7E1EA" stroke-width="8" stroke-linecap="round"/>
<path d="M80 84 Q92 70 102 68" fill="none" {s(T2)}/>
{eye(76, 82, 1.15)}
<path d="M72 93 Q79 98 86 92" fill="none" {s(T2)}/>
<path d="M50 64 Q44 46 62 38 M90 62 Q98 46 80 38" fill="none" stroke="#3E8B3A" stroke-width="3" stroke-linecap="round"/>
<path d="M48 58 l-8 -4 M48 50 l-8 -2 M54 42 l-6 -6 M92 56 l8 -4 M92 48 l8 -2 M86 42 l6 -6" stroke="#3E8B3A" stroke-width="4" stroke-linecap="round"/>
<path d="M98 60 l-8 -6 M98 76 l-8 6" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 30, 16)
SUBJ["ss1-park-pobedy"] = ("серебристая рыба омуль с тёмной полоской вдоль спины",
                           "финиширует — касается плавником белого кафельного бортика, над головой зелёный лавровый венок победителя, фон салатовый")

# 12. Школа плавания № 1, бассейн «Стальной» — мечехвост в панцире-шлеме ползёт по дну с пузырьками
ICONS["ss1-stalnoy"] = W("#5FD1E8", "#1C6FA3", f'''
<path d="M-6 108 Q30 100 64 108 T134 106 V134 H-6Z" fill="#E9D49A" {s()}/>
<path d="M64 96 L64 124" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M64 96 L64 122" stroke="#8C99A6" stroke-width="3.6" stroke-linecap="round"/>
<path d="M16 84 Q14 34 64 30 Q114 34 112 84 Q92 98 64 98 Q36 98 16 84Z" fill="#A9B6C2" {s()}/>
<path d="M30 80 Q30 46 64 42 Q98 46 98 80" fill="none" stroke="#7C8A97" stroke-width="3.4"/>
<path d="M64 30 V98" stroke="#7C8A97" stroke-width="3"/>
<path d="M28 50 Q40 38 54 36" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".85"/>
{eye(48, 68, 1.3)}{eye(80, 68, 1.3)}
<path d="M56 82 Q64 88 72 82" fill="none" {s(T2)}/>
{BL.format(38, 78)}{BL.format(90, 78)}
{bub(104, 22, 5)}{bub(116, 38, 3)}{bub(20, 20, 4)}
''', 50, 30)
SUBJ["ss1-stalnoy"] = ("серо-стальной мечехвост в круглом панцире, похожем на рыцарский шлем, с хвостом-шипом",
                       "ползёт по песчаному дну прямо на зрителя и улыбается, вверх бегут пузырьки, вода голубая")

# 13. Школа плавания «Океаника», Текстильщики — лиственный морской дракон с наклейками-звёздами за уровни
ICONS["okeanika-tekstilshchiki"] = W("#FFE1F0", "#F58BB8", f'''
<path d="M70 20 Q96 26 90 52 Q84 70 66 74 Q50 80 54 96 Q58 110 74 108" fill="none" stroke="{O}" stroke-width="19" stroke-linecap="round"/>
<path d="M70 20 Q96 26 90 52 Q84 70 66 74 Q50 80 54 96 Q58 110 74 108" fill="none" stroke="#F2C53B" stroke-width="13" stroke-linecap="round"/>
<path d="M92 40 Q112 34 116 20 Q102 20 92 30Z M84 64 Q104 70 112 62 Q100 54 88 56Z M50 86 Q30 80 22 90 Q34 98 48 94Z M60 104 Q52 122 40 120 Q44 108 54 102Z M58 72 Q40 62 34 70 Q44 78 56 78Z" fill="#6CC04A" {s(T2)}/>
<path d="M56 22 Q36 14 20 22 Q22 30 40 30 Q50 32 58 30Z" fill="#F2C53B" {s()}/>
<circle cx="66" cy="22" r="13" fill="#F2C53B" {s()}/>
<path d="M62 10 Q66 0 74 4 Q72 10 68 12Z" fill="#6CC04A" {s(T2)}/>
{eye(64, 21, 1.1)}
{BL.format(58, 28)}
<path d="M100 92 l3 6 l7 1 l-5 5 l1 7 l-6 -3 l-6 3 l1 -7 l-5 -5 l7 -1Z" fill="#3EA8F0" {s(T2)}/>
<path d="M24 50 l2 4 l5 1 l-4 3 l1 5 l-4 -2 l-4 2 l1 -5 l-4 -3 l5 -1Z" fill="#fff" {s(T2)}/>
''', 40, 30)
SUBJ["okeanika-tekstilshchiki"] = ("жёлтый лиственный морской дракон с зелёными отростками-листиками и длинным рыльцем-трубочкой",
                                   "плывёт стоймя, изогнувшись буквой S, рядом две наклейки-звёздочки за пройденные уровни — голубая и белая, фон розовый")

# 14. Школа плавания «Океаника», Измайлово — сине-жёлтый голожаберник со светящимся браслетом
ICONS["okeanika-izmaylovo"] = W("#1D2A6B", "#0B1030", f'''
<path d="M-6 100 Q20 92 40 100 Q64 110 90 100 Q112 92 134 100 V134 H-6Z" fill="#7A4BC4" {s()}/>
<path d="M14 92 Q10 70 34 66 L84 62 Q112 60 116 80 Q116 98 92 98 L34 100 Q16 102 14 92Z" fill="#2F7BEA" {s()}/>
<path d="M22 86 Q60 74 110 82" fill="none" stroke="#FFE14A" stroke-width="5" stroke-linecap="round"/>
<path d="M30 68 Q24 48 30 40 Q38 50 40 66Z M48 66 Q46 44 54 36 Q60 48 58 64Z M66 64 Q68 44 76 38 Q80 50 76 62Z" fill="#FF8A3C" {s(T2)}/>
<path d="M98 62 Q100 44 96 34 M108 64 Q114 48 114 36" fill="none" {s(T3)}/>
<circle cx="96" cy="32" r="5" fill="#FFE14A" {s(T2)}/><circle cx="114" cy="34" r="5" fill="#FFE14A" {s(T2)}/>
{eye(96, 76, 1.1)}{eye(110, 78, 0.9)}
<path d="M96 88 Q102 92 108 88" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<path d="M62 64 Q60 82 66 100" fill="none" stroke="{O}" stroke-width="9"/>
<path d="M62 64 Q60 82 66 100" fill="none" stroke="#7CFFB2" stroke-width="5"/>
{sparkle(50, 22, 6, "#7CFFB2")}{sparkle(20, 30, 4, "#7CFFB2")}{sparkle(84, 16, 4, "#7CFFB2")}
''', 60, 40)
SUBJ["okeanika-izmaylovo"] = ("синий морской слизень голожаберник с жёлтой полосой, оранжевыми жабрами-язычками на спине и жёлтыми рожками",
                              "ползёт по фиолетовому дну в тёмной глубине, на нём светится зелёный браслет пловца, вокруг зелёные искры")

# 15. Школа спортивно-оздоровительного плавания, Крылатское — белая птица фаэтон плывёт, хвост-лента за ней
ICONS["shsop-krylatskoe"] = W("#D9ECFF", "#6FA8F0", f'''
<path d="M-6 80 Q30 72 64 80 T134 78 V134 H-6Z" fill="#0FA3A3" {s()}/>
<path d="M44 78 Q20 60 8 30 M44 82 Q16 70 0 48" fill="none" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M44 78 Q20 60 8 30 M44 82 Q16 70 0 48" fill="none" stroke="#fff" stroke-width="3.6" stroke-linecap="round"/>
<path d="M36 84 Q40 60 68 60 Q96 60 104 78 Q96 96 68 96 Q44 96 36 84Z" fill="#fff" {s()}/>
<path d="M52 70 Q70 60 90 72 Q72 82 52 70Z" fill="#fff" {s(T2)}/>
<path d="M58 71 Q72 66 84 73" fill="none" stroke="#23303F" stroke-width="4" stroke-linecap="round"/>
<circle cx="96" cy="56" r="15" fill="#fff" {s()}/>
<path d="M86 52 Q96 48 106 56" fill="none" stroke="#23303F" stroke-width="4" stroke-linecap="round"/>
<path d="M108 54 L126 60 L108 64Z" fill="#F2463B" {s(T2)}/>
{eye(98, 57, 1.0)}
{BL.format(92, 64)}
<path d="M14 100 q8 -5 16 0 M56 108 q8 -5 16 0 M98 102 q8 -5 16 0" fill="none" stroke="#BFF5F0" stroke-width="3" stroke-linecap="round"/>
''', 40, 20)
SUBJ["shsop-krylatskoe"] = ("белая морская птица фаэтон с красным клювом, чёрной бровью и двумя длинными перьями-лентами в хвосте",
                            "плывёт по бирюзовой воде, а перья-ленты хвоста развеваются высоко за спиной, небо голубое")

# ---------- места, ждавшие справку OSM ----------
# 16. Школа плавания № 1, бассейн МГУСиТ — розовая рыба-капля в плавательных очках
ICONS["ss1-mgusit"] = W("#C9F2FF", "#4FB6E8", f"""
<path d="M-6 112 Q30 104 64 112 T134 110 V134 H-6Z" fill="#2E7FC4" {s()}/>
<path d="M18 86 Q10 46 44 34 Q78 22 102 44 Q122 64 112 90 Q98 110 62 108 Q26 108 18 86Z" fill="#F7B8C4" {s()}/>
<path d="M52 70 Q62 98 78 72 Q70 62 52 70Z" fill="#F29AAE" {s(T2)}/>
<path d="M44 92 Q64 102 86 92" fill="none" {s(T3)}/>
<rect x="28" y="46" width="30" height="20" rx="9" fill="#3EA8F0" {s()}/><rect x="70" y="46" width="30" height="20" rx="9" fill="#3EA8F0" {s()}/>
<path d="M58 56 H70 M28 54 L16 50 M100 54 L112 50" fill="none" {s(T3)}/>
<circle cx="44" cy="56" r="4" fill="{O}"/><circle cx="84" cy="56" r="4" fill="{O}"/>
<path d="M34 50 q5 -3 10 0 M76 50 q5 -3 10 0" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
{BL.format(32, 78)}{BL.format(98, 78)}
<path d="M112 84 L126 76 L122 96Z" fill="#F29AAE" {s(T2)}/>
{bub(108, 18, 5)}{bub(20, 22, 3.4)}
""", 40, 26)
SUBJ["ss1-mgusit"] = ("розовая рыба-капля с большим носом-картошкой",
                      "смотрит прямо на зрителя сквозь голубые плавательные очки и довольно улыбается, вода светло-голубая")

# 17. Школа плавания № 1, бассейн железнодорожного университета — жёлтая подлодка идёт по дорожке
ICONS["ss1-miit"] = W("#0F5E8C", "#062B47", f"""
<path d="M-4 22 H132" stroke="#FFD23B" stroke-width="5" stroke-dasharray="12 8"/>
<path d="M-4 112 H132" stroke="#FFD23B" stroke-width="5" stroke-dasharray="12 8"/>
<path d="M22 70 L6 56 L8 84Z" fill="#E8542A" {s(T2)}/>
<circle cx="12" cy="70" r="4" fill="#B9C6D1" {s(T2)}/>
<rect x="56" y="30" width="22" height="22" rx="5" fill="#F2B200" {s()}/>
<path d="M70 30 V18 H86" fill="none" {s("stroke-width=\"5\"")}/>
<path d="M70 30 V18 H86" fill="none" stroke="#B9C6D1" stroke-width="2.4"/>
<rect x="20" y="46" width="94" height="48" rx="24" fill="#FFD23B" {s()}/>
<path d="M24 78 H110" stroke="#F2B200" stroke-width="4"/>
<circle cx="46" cy="66" r="9" fill="#BEEBFF" {s(T2)}/><circle cx="70" cy="66" r="9" fill="#BEEBFF" {s(T2)}/>
{eye(46, 66, 0.9)}{eye(70, 66, 0.9)}
<path d="M90 70 Q97 76 104 70" fill="none" {s(T2)}/>
{BL.format(96, 62)}
{bub(116, 40, 4)}{bub(122, 26, 2.6)}{bub(100, 104, 3)}
""", 50, 40)
SUBJ["ss1-miit"] = ("жёлтая подводная лодка с двумя иллюминаторами-глазами, перископом и красным винтом",
                    "идёт строго по своей дорожке между двумя жёлтыми пунктирными разметками, как поезд по расписанию, вода тёмно-синяя")

# 18. Школа плавания № 1, Центр водных видов спорта (50-метровые бассейны) — огромная белуга на всю дорожку
ICONS["ss1-motsvs"] = W("#FFE9B8", "#F7A55C", f"""
<rect x="-6" y="44" width="140" height="90" fill="#1877C9" {s()}/>
<path d="M-4 60 H132 M-4 110 H132" stroke="#fff" stroke-width="4" stroke-dasharray="6 6"/>
<path d="M14 86 L-4 70 L0 88 L-6 104Z" fill="#6B7C8C" {s(T2)}/>
<path d="M10 88 Q30 70 70 70 Q104 70 126 84 Q112 100 70 100 Q30 100 10 88Z" fill="#8FA1B0" {s()}/>
<path d="M16 90 Q60 98 122 86 Q106 100 70 100 Q34 100 16 90Z" fill="#EEF2F5"/>
<path d="M30 74 l4 -8 l4 7 M46 71 l4 -8 l4 8 M62 70 l4 -8 l4 8 M78 70 l4 -8 l4 9" fill="#6B7C8C" {s(T2)}/>
<path d="M106 92 q2 8 -2 12 M114 90 q3 8 0 12" fill="none" {s(T2)}/>
{eye(104, 82, 1.0)}
<text x="64" y="34" font-family="Arial" font-weight="700" font-size="22" text-anchor="middle" fill="{O}">50 м</text>
<path d="M22 28 H40 M88 28 H106 M22 22 V34 M106 22 V34" stroke="{O}" stroke-width="3" stroke-linecap="round"/>
""", 50, 10)
SUBJ["ss1-motsvs"] = ("огромная серая белуга с белым брюхом, шипами-жучками вдоль спины и усиками",
                      "вытянулась во всю длину дорожки между белыми разделителями, над водой размерная стрелка «50 м», небо оранжевое")

# 19. Школа плавания № 1, бассейн «Надежда» — красно-белый буёк с флажком качается на волне
ICONS["ss1-nadezhda-krupskoy"] = W("#E3FBF3", "#7ADCC0", f"""
<path d="M64 40 V10" stroke="{O}" stroke-width="5" stroke-linecap="round"/>
<path d="M64 10 L92 18 L64 28Z" fill="#FFD23B" {s(T2)}/>
<path d="M40 100 Q34 40 64 38 Q94 40 88 100Z" fill="#F23B3B" {s()}/>
<path d="M38 74 Q64 66 90 74 L89 92 Q64 84 39 92Z" fill="#fff" {s(T2)}/>
{eye(54, 58, 1.2)}{eye(74, 58, 1.2)}
<path d="M58 68 Q64 73 70 68" fill="none" {s(T2)}/>
{BL.format(46, 66)}{BL.format(82, 66)}
<path d="M-6 100 Q16 88 38 100 Q64 114 90 100 Q112 88 134 100 V134 H-6Z" fill="#2563C9" {s()}/>
<path d="M14 112 q8 -5 16 0 M56 118 q8 -5 16 0 M98 112 q8 -5 16 0" fill="none" stroke="#9BC4FF" stroke-width="3" stroke-linecap="round"/>
<path d="M22 84 q-8 -4 -10 -12 M106 84 q8 -4 10 -12" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
""", 50, 30)
SUBJ["ss1-nadezhda-krupskoy"] = ("красный буёк-неваляшка с белым пояском и жёлтым флажком на макушке",
                                 "качается на синей волне и улыбается — до него точно можно доплыть, фон мятно-зелёный")

# 20. Школа плавания № 1, «Орехово-Борисово» — птичка зуёк пробует воду лапкой с бортика
ICONS["ss1-orekhovo-borisovo"] = W("#FFF0E0", "#F5B98A", f"""
<path d="M-6 98 H70 V134 H-6Z" fill="#F4F6F8" {s()}/>
<path d="M12 98 V134 M36 98 V134 M60 98 V134 M-6 116 H70" stroke="#B9C6D1" stroke-width="2.4"/>
<path d="M70 104 Q90 98 102 104 T134 102 V134 H70Z" fill="#25A7D9" {s()}/>
<path d="M36 76 L34 98 M34 98 l-8 0 M34 98 l6 2" fill="none" stroke="#F28B2E" stroke-width="4" stroke-linecap="round"/>
<path d="M50 76 L78 104 M78 104 l8 -2" fill="none" stroke="#F28B2E" stroke-width="4" stroke-linecap="round"/>
<path d="M16 62 Q20 40 44 42 Q66 44 68 62 Q62 80 42 80 Q22 80 16 62Z" fill="#C9A77C" {s()}/>
<path d="M22 70 Q42 84 64 70 Q58 80 42 80 Q28 80 22 70Z" fill="#fff"/>
<path d="M16 62 L2 56 L10 70Z" fill="#8A6A45" {s(T2)}/>
<circle cx="66" cy="38" r="16" fill="#fff" {s()}/>
<path d="M50 36 Q66 14 82 36 Q66 28 50 36Z" fill="#C9A77C" {s(T2)}/>
<path d="M54 50 Q66 58 78 50" fill="none" stroke="#2B2B33" stroke-width="6" stroke-linecap="round"/>
<path d="M81 36 L96 40 L81 44Z" fill="#F28B2E" {s(T2)}/>
{eye(70, 38, 1.05)}
<path d="M84 96 q6 -8 2 -14 M96 100 q8 -4 10 -12" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
""", 60, 20)
SUBJ["ss1-orekhovo-borisovo"] = ("маленькая птичка зуёк песочного цвета с чёрным галстуком на шее и оранжевым клювом",
                                 "стоит на белом кафельном бортике на одной ноге, а второй лапкой осторожно пробует голубую воду, фон персиковый")

# 21. Школа плавания № 1, бассейн РЭУ им. Плеханова — сомик-анциструс, присосавшись, начищает кафель до блеска
ICONS["ss1-reu-plekhanova"] = W("#9BE0F2", "#3B9CCB", f"""
<rect x="-6" y="-6" width="140" height="140" fill="#7CCDE8"/>
<path d="M-6 32 H134 M-6 64 H134 M-6 96 H134 M32 -6 V134 M64 -6 V134 M96 -6 V134" stroke="#fff" stroke-width="3" opacity=".8"/>
<path d="M46 96 L26 116 L44 114 L52 126 L60 102Z" fill="#5E4630" {s(T2)}/>
<path d="M40 100 Q30 60 52 36 Q70 20 88 34 Q100 48 92 72 Q82 100 56 106Z" fill="#8A6A45" {s()}/>
<circle cx="56" cy="78" r="4" fill="#5E4630"/><circle cx="72" cy="88" r="3" fill="#5E4630"/><circle cx="50" cy="60" r="3" fill="#5E4630"/><circle cx="80" cy="70" r="3.4" fill="#5E4630"/>
<path d="M44 70 Q26 62 20 74 Q30 82 44 80Z M90 62 Q108 60 110 72 Q100 78 88 74Z" fill="#5E4630" {s(T2)}/>
<ellipse cx="72" cy="28" rx="15" ry="9" fill="#F4C9A0" {s()}/>
<path d="M62 24 l-6 -10 M70 20 l-2 -11 M78 20 l4 -10 M84 24 l8 -8" fill="none" {s(T2)}/>
{eye(60, 46, 1.0)}{eye(82, 44, 1.0)}
{sparkle(104, 22, 9)}{sparkle(22, 30, 6)}{sparkle(110, 104, 5)}
""", 50, 50)
SUBJ["ss1-reu-plekhanova"] = ("коричневый в крапинку сомик-анциструс с ртом-присоской и усиками-щёточкой",
                              "присосался к голубой кафельной стенке бассейна и начищает плитку — вокруг белые искры чистоты")

# 22. Школа плавания № 1, «Раменки» — уточка чирок с зелёной полосой у глаза лежит на воде звёздочкой
ICONS["ss1-ramenki"] = W("#3FC6C0", "#147C86", f"""
<circle cx="64" cy="66" r="50" fill="none" stroke="#fff" stroke-width="3" opacity=".5"/>
<circle cx="64" cy="66" r="38" fill="none" stroke="#fff" stroke-width="3" opacity=".35"/>
<path d="M42 54 Q20 44 12 28 Q32 30 48 44Z M86 54 Q108 44 116 28 Q96 30 80 44Z" fill="#9A7B5B" {s()}/>
<path d="M28 34 Q36 36 42 44 M100 34 Q92 36 86 44" fill="none" stroke="#3FBF6A" stroke-width="5" stroke-linecap="round"/>
<path d="M52 92 L44 114 L56 108 L60 118 Z M76 92 L84 114 L72 108 L68 118Z" fill="#F28B2E" {s(T2)}/>
<ellipse cx="64" cy="72" rx="24" ry="28" fill="#E9DCC8" {s()}/>
<circle cx="56" cy="72" r="2.4" fill="#9A7B5B"/><circle cx="70" cy="80" r="2.4" fill="#9A7B5B"/><circle cx="64" cy="66" r="2.4" fill="#9A7B5B"/><circle cx="58" cy="86" r="2.4" fill="#9A7B5B"/>
<circle cx="64" cy="38" r="17" fill="#A8572E" {s()}/>
<path d="M50 34 Q58 28 64 36 Q58 42 50 40Z M78 34 Q70 28 64 36 Q70 42 78 40Z" fill="#2F9E5B" {s(T2)}/>
<path d="M58 46 Q64 56 70 46Z" fill="#3B3355" {s(T2)}/>
{eye(56, 36, 0.8)}{eye(72, 36, 0.8)}
""", 50, 50)
SUBJ["ss1-ramenki"] = ("уточка чирок с каштановой головой, зелёными полосками у глаз и крапчатым животом",
                       "лежит на спине на воде «звёздочкой», раскинув крылья и оранжевые лапы, от неё расходятся круги, вода бирюзовая, вид сверху")

# 23. Школа плавания № 1, 50-метровый бассейн РГУФК — птица змеешейка: над водой только длинная шея
ICONS["ss1-rgufk"] = W("#FFD8E4", "#F285A8", f"""
<path d="M-6 86 Q30 78 64 86 T134 84 V134 H-6Z" fill="#274B9F" {s()}/>
<path d="M40 96 Q36 60 56 50 Q76 42 70 26 Q66 16 78 12" fill="none" stroke="{O}" stroke-width="17" stroke-linecap="round"/>
<path d="M40 96 Q36 60 56 50 Q76 42 70 26 Q66 16 78 12" fill="none" stroke="#5E4630" stroke-width="11" stroke-linecap="round"/>
<path d="M42 84 Q38 62 54 54" fill="none" stroke="#E9DCC8" stroke-width="4" stroke-linecap="round"/>
<path d="M82 6 L118 14 L84 18Z" fill="#F2C53B" {s(T2)}/>
<circle cx="78" cy="12" r="3.4" fill="#fff"/><circle cx="79" cy="12" r="1.9" fill="{O}"/>
<path d="M-6 100 Q30 92 64 100 T134 98 V134 H-6Z" fill="#3563C4"/>
<ellipse cx="40" cy="98" rx="16" ry="4" fill="none" stroke="#fff" stroke-width="2.6" opacity=".9"/>
<path d="M74 110 q8 -5 16 0 M98 104 q8 -5 16 0 M10 112 q8 -5 16 0" fill="none" stroke="#9BB8FF" stroke-width="3" stroke-linecap="round"/>
<path d="M92 60 l5 2 l-5 2 M104 50 l5 2 l-5 2" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
""", 30, 20)
SUBJ["ss1-rgufk"] = ("тёмно-коричневая птица змеешейка с длинной S-образной шеей и острым жёлтым клювом",
                     "плывёт так, что всё тело под водой, а над синей гладью торчит одна изогнутая шея, как перископ, небо розовое")

# 24. Школа плавания № 1, «Ховрино» (только индивидуальные занятия) — зубастая рыба зубатка и тренерский секундомер
ICONS["ss1-khovrino"] = W("#E5E0FF", "#9C8CF0", f"""
<path d="M-6 54 Q30 46 64 54 T134 52 V134 H-6Z" fill="#0F8FA8" {s()}/>
<path d="M8 96 Q4 70 34 68 L86 66 Q116 64 120 86 Q118 108 88 108 L34 112 Q10 114 8 96Z" fill="#6E7FA3" {s()}/>
<path d="M30 70 q4 20 0 40 M46 69 q4 20 0 40 M62 68 q4 20 0 40" fill="none" stroke="#4E5D80" stroke-width="5"/>
<path d="M22 68 Q50 50 84 66Z" fill="#4E5D80" {s(T2)}/>
<path d="M84 92 H118 Q114 104 98 104 Q88 102 84 92Z" fill="#fff" {s(T2)}/>
<path d="M92 92 v8 M100 92 v10 M108 92 v9" stroke="{O}" stroke-width="2.4"/>
{eye(96, 80, 1.15)}
{BL.format(84, 88)}
<circle cx="98" cy="28" r="17" fill="#FFD23B" {s()}/><circle cx="98" cy="28" r="11" fill="#fff" {s(T2)}/>
<path d="M98 28 V20 M98 28 L104 31 M92 8 H104 M98 8 V11" fill="none" {s(T2)}/>
""", 30, 20)
SUBJ["ss1-khovrino"] = ("серо-синяя полосатая рыба зубатка с широкой улыбкой во все белые зубы",
                        "плывёт одна по бирюзовой дорожке, а над водой висит жёлтый тренерский секундомер — занятие только для неё, небо сиреневое")

# 25. Семейно-оздоровительный центр «Волна» (груднички с 2 месяцев, тёплая вода) — прозрачный морской ангел клион
ICONS["volna-olgino"] = W("#FFF4D6", "#FFC2A1", f"""
<circle cx="64" cy="64" r="46" fill="#7FE0E0" opacity=".9" {s()}/>
<path d="M22 64 Q44 52 64 64 T106 64" fill="none" stroke="#fff" stroke-width="4" opacity=".8" stroke-linecap="round"/>
<path d="M50 50 Q22 30 20 54 Q28 66 50 60Z M78 50 Q106 30 108 54 Q100 66 78 60Z" fill="#DDF6FF" {s()}/>
<path d="M50 44 Q50 26 64 26 Q78 26 78 44 Q80 76 64 100 Q48 76 50 44Z" fill="#EAFBFF" {s()}/>
<path d="M58 56 Q64 48 70 56 Q72 70 64 82 Q56 70 58 56Z" fill="#FF8A5C"/>
<path d="M56 26 Q54 16 60 14 M72 26 Q74 16 68 14" fill="none" {s(T2)}/>
{eye(58, 40, 0.9)}{eye(70, 40, 0.9)}
<path d="M61 47 Q64 50 67 47" fill="none" {s("stroke-width=\"2\"")}/>
{BL.format(53, 46)}{BL.format(75, 46)}
{bub(98, 92, 4)}{bub(30, 90, 3)}
<path d="M100 14 q6 6 0 12 q-6 6 0 12" fill="none" stroke="#FF8A5C" stroke-width="3" stroke-linecap="round" opacity=".7"/>
""", 50, 30)
SUBJ["volna-olgino"] = ("прозрачный морской ангел клион с крылышками и оранжевым сердечком внутри",
                        "парит, расправив крылышки, в круглом пузыре тёплой бирюзовой воды, фон сливочно-персиковый")

# 26. Клуб синхронного плавания «Артистик», «Манхэттен» — пять серебристых корюшек выстроились звездой (вид сверху)
import math as _m
_fish = ""
for _k in range(5):
    _a = -90 + _k * 72
    _fish += (f'<g transform="rotate({_a} 64 64) translate(64 64)">'
              f'<path d="M14 0 Q26 -11 44 -6 Q52 -2 52 0 Q52 2 44 6 Q26 11 14 0Z" fill="#DCE8F2" {s(T2)}/>'
              f'<path d="M14 0 L4 -7 L6 0 L4 7Z" fill="#9FB6CC" {s(T2)}/>'
              f'<path d="M22 -3 Q32 -6 44 -3" fill="none" stroke="#7FD0C2" stroke-width="3" stroke-linecap="round"/>'
              f'<circle cx="46" cy="0" r="2.2" fill="{O}"/></g>')
ICONS["artistic-manhattan"] = W("#7A4BE0", "#2E1A7A", f"""
<circle cx="64" cy="64" r="56" fill="#3A6BE8" opacity=".55"/>
<circle cx="64" cy="64" r="40" fill="none" stroke="#fff" stroke-width="2.6" opacity=".45"/>
{_fish}
{sparkle(64, 64, 9, "#FFE27A")}
{sparkle(20, 22, 5, "#FFE27A")}{sparkle(108, 22, 5, "#FFE27A")}{sparkle(18, 106, 4, "#FFE27A")}{sparkle(110, 104, 4, "#FFE27A")}
""", 50, 50)
SUBJ["artistic-manhattan"] = ("пять серебристых рыбок-корюшек с бирюзовой полоской на спинке",
                              "выстроились в воде звездой хвостами к центру, как синхронистки в фигуре, вид сверху, в середине золотая искра, вода фиолетово-синяя")

# 27. Клуб синхронного плавания «Артистик», «Фитнес Парк» — утка-шилохвость держит «шпагат» лапками над водой
ICONS["artistic-fitnes-park-izmaylovo"] = W("#FFE9F3", "#FF9CC4", f"""
<path d="M64 60 L26 22 M64 60 L102 22" fill="none" stroke="{O}" stroke-width="11" stroke-linecap="round"/>
<path d="M64 60 L26 22 M64 60 L102 22" fill="none" stroke="#8C99A6" stroke-width="6" stroke-linecap="round"/>
<path d="M26 22 L10 16 L18 30 L12 36Z M102 22 L118 16 L110 30 L116 36Z" fill="#F28B2E" {s(T2)}/>
<path d="M64 26 L60 6 L64 -2 L68 6Z" fill="#3A3F4A" {s(T2)}/>
<path d="M44 84 Q44 44 64 26 Q84 44 84 84Z" fill="#fff" {s()}/>
<path d="M50 84 Q52 56 64 40 Q76 56 78 84Z" fill="#C9D1DA"/>
<path d="M-6 84 Q30 76 64 84 T134 82 V134 H-6Z" fill="#12A5B5" {s()}/>
<ellipse cx="64" cy="86" rx="30" ry="6" fill="none" stroke="#fff" stroke-width="3" opacity=".9"/>
<path d="M64 96 Q60 108 64 118" fill="none" stroke="#6B4A36" stroke-width="9" stroke-linecap="round" opacity=".55"/>
<circle cx="64" cy="122" r="8" fill="#6B4A36" opacity=".55"/>
<path d="M14 104 q8 -5 16 0 M98 104 q8 -5 16 0" fill="none" stroke="#BFF5F0" stroke-width="3" stroke-linecap="round"/>
{sparkle(30, 56, 6)}{sparkle(100, 58, 5)}{sparkle(64, 14, 4)}
""", 50, 20)
SUBJ["artistic-fitnes-park-izmaylovo"] = ("серо-белая утка-шилохвость с длинным острым хвостом",
                                          "нырнула вниз головой и держит над бирюзовой водой «шпагат» — две лапки с оранжевыми ластами врозь и хвост-шило свечкой, фон розовый")

if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for i in ids:
        open(os.path.join(OUT, i + ".svg"), "w", encoding="utf-8").write(ICONS[i])
    print("svg:", len(ids))
    for i in ids:
        print(f"{i} — герой: {SUBJ[i][0]} | сцена: {SUBJ[i][1]}")
