"""Иконки робота pools, 2026-11-14 (05 UTC). Каждая придумана и нарисована отдельно (правило абсолютной
уникальности): свой герой, своя сцена, своя компоновка и палитра. Герои сверены с реестром icons-src/subjects.txt
(таких героев в реестре нет), картинки — tools/check_unique.py.
Запуск: python3 tools/icons_pools_1114e.py [id …]  → python3 tools/render_icons.py <id…> → python3 tools/check_unique.py <id…>."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, sparkle, O
from icons_pools_1112b import W, bub, T2

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
T18 = 'stroke-width="1.8"'
BL = '<ellipse cx="{}" cy="{}" rx="4.4" ry="2.6" fill="#FF7FA8" opacity=".8"/>'


def rope(pts, c1, c2, r=4.2):
    """Разделительная дорожка: поплавки по заданным точкам (цвета чередуются)."""
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c1 if i % 2 == 0 else c2}" {s("stroke-width=\"2\"")}/>'
                   for i, (x, y) in enumerate(pts))


# 1. Школа плавания № 1, бассейн «Нептун» (лягушатник 60 см, с 3 лет) — утка-гоголь ныряет: над водой только хвост и лапки
ICONS["ss1-neptun-federativny"] = W("#FFF6CF", "#FFC25E", f'''
<path d="M-6 56 Q28 50 64 56 T134 56 V134 H-6Z" fill="#19B3C6" {s()}/>
<path d="M-6 134 V104 Q40 96 64 104 T134 100 V134Z" fill="#0E8FA8" opacity=".55"/>
<path d="M46 50 Q38 30 30 34 Q30 44 40 54Z M82 50 Q90 30 98 34 Q98 44 88 54Z" fill="#FF8A1F" {s(T2)}/>
<path d="M56 56 L64 34 L72 56Z" fill="#2A3350" {s()}/>
<ellipse cx="64" cy="74" rx="24" ry="22" fill="#2A3350" {s()}/>
<ellipse cx="64" cy="80" rx="15" ry="14" fill="#fff" {s(T2)}/>
<circle cx="64" cy="104" r="16" fill="#1F3B4D" {s()}/>
<ellipse cx="52" cy="108" rx="5" ry="6.5" fill="#fff" {s(T2)}/>
<circle cx="70" cy="102" r="5.4" fill="#FFD23F" {s(T2)}/><circle cx="70" cy="103" r="2.4" fill="{O}"/>
<path d="M56 116 Q64 128 72 116 Q64 120 56 116Z" fill="#8792A8" {s(T2)}/>
{bub(96, 84, 5)}{bub(104, 70, 3.4)}{bub(28, 92, 4)}{bub(22, 76, 2.6)}
<path d="M20 58 q8 -5 16 0 M92 58 q8 -5 16 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 50, 20)
SUBJ["ss1-neptun-federativny"] = ("чёрно-белая утка-гоголь с жёлтым глазом и белым пятнышком на щеке",
                                  "ныряет вниз головой в бирюзовую воду — над водой торчат только хвост и оранжевые лапки, под водой пузыри, небо тёплое жёлтое")

# 2. Школа плавания № 1, бассейн «Живописный» — жёлтая рыба-кузовок в чёрный горошек, будто нарисованная
ICONS["ss1-zhivopisny"] = W("#8B6BF0", "#2A1A6E", f'''
{rope([(6, 22), (20, 20), (34, 19), (48, 18), (62, 18), (76, 18), (90, 19), (104, 20), (118, 22)], "#FF7FB4", "#fff")}
<ellipse cx="66" cy="112" rx="30" ry="5" fill="#160C45" opacity=".45"/>
<path d="M96 70 l16 -10 q4 12 0 24Z" fill="#FFB02E" {s(T2)}/>
<path d="M62 40 q6 -12 14 0Z M60 96 q6 10 14 0Z" fill="#FFB02E" {s(T2)}/>
<rect x="30" y="40" width="68" height="56" rx="17" fill="#FFD83A" {s()}/>
<circle cx="78" cy="52" r="3.4" fill="{O}"/><circle cx="88" cy="66" r="3.2" fill="{O}"/><circle cx="74" cy="72" r="3.4" fill="{O}"/>
<circle cx="86" cy="84" r="3" fill="{O}"/><circle cx="62" cy="86" r="3.2" fill="{O}"/><circle cx="64" cy="50" r="2.8" fill="{O}"/>
<circle cx="42" cy="86" r="2.8" fill="{O}"/>
{eye(44, 58, 1.25)}{eye(60, 62, 1.1)}
<ellipse cx="33" cy="74" rx="6.5" ry="5" fill="#FF8FA8" {s(T2)}/>
<path d="M30 74 h6" fill="none" {s(T2)}/>
{BL.format(50, 72)}
{bub(18, 60, 4.4)}{bub(12, 46, 2.8)}
''', 30, 24)
SUBJ["ss1-zhivopisny"] = ("жёлтая рыба-кузовок — кубик в чёрный горошек с губками бантиком",
                          "важно плывёт над самым дном под розово-белой разделительной дорожкой в тёмно-фиолетовой глубине, внизу её квадратная тень")

# 3. Школа плавания № 1, бассейн «Коломенский» (берут с 3 лет) — чибис с хохолком замер на стартовой тумбе № 3
ICONS["ss1-kolomensky"] = W("#E2FFEC", "#3CCB8A", f'''
<path d="M70 96 Q100 88 134 96 V134 H70Z" fill="#2E8BE6" {s()}/>
<path d="M84 110 q8 -5 16 0 M106 104 q7 -4 14 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M14 134 L22 92 L76 84 L82 134Z" fill="#3757C9" {s()}/>
<path d="M18 92 L78 82 L80 90 L20 100Z" fill="#fff" {s(T2)}/>
<text x="48" y="124" font-family="Arial" font-weight="700" font-size="24" fill="#fff" text-anchor="middle">3</text>
<path d="M50 84 l-4 -10 M62 82 l2 -10" fill="none" stroke="{O}" stroke-width="6" stroke-linecap="round"/>
<path d="M50 84 l-4 -10 M62 82 l2 -10" fill="none" stroke="#E8566B" stroke-width="2.6" stroke-linecap="round"/>
<path d="M28 60 Q30 38 56 40 Q84 44 92 62 Q78 78 52 76 Q34 74 28 60Z" fill="#fff" {s()}/>
<path d="M28 60 Q30 38 56 40 Q74 42 86 54 Q62 52 44 60 Q34 64 28 60Z" fill="#1E6B55" {s(T2)}/>
<path d="M30 58 Q14 54 8 62 Q20 66 32 64Z" fill="#17483B" {s(T2)}/>
<circle cx="96" cy="50" r="14" fill="#fff" {s()}/>
<path d="M84 44 Q96 30 108 44 Q96 40 84 44Z" fill="#17483B" {s(T2)}/>
<path d="M92 36 Q86 14 70 12 M96 36 Q94 18 82 10" fill="none" stroke="{O}" stroke-width="3" stroke-linecap="round"/>
{eye(100, 50, 1)}
<path d="M108 52 l12 3 l-12 4Z" fill="#3B3355" {s(T2)}/>
{BL.format(92, 58)}
''', 30, 22)
SUBJ["ss1-kolomensky"] = ("чибис с длинным хохолком, зелёной спинкой и белым животом",
                          "пригнулся в стартовой стойке на синей тумбе с цифрой 3, готовится прыгнуть в бассейн, фон мятно-зелёный")

# 4. Школа плавания № 1, бассейн «Есенинский» — плоский палтус у дна смотрит вверх двумя глазами
ICONS["ss1-eseninsky"] = W("#C9F2FF", "#3A97E0", f'''
{rope([(4, 30), (17, 27), (30, 25), (43, 24), (56, 24), (69, 24), (82, 25), (95, 27), (108, 30), (121, 33)], "#E8443A", "#fff")}
<path d="M-6 100 Q30 92 64 98 T134 96 V134 H-6Z" fill="#FFE2A6" {s()}/>
<circle cx="22" cy="112" r="2" fill="#D9B36A"/><circle cx="96" cy="114" r="2" fill="#D9B36A"/><circle cx="58" cy="118" r="2" fill="#D9B36A"/>
<path d="M100 78 l18 -12 q4 14 -2 26Z" fill="#8A7A3C" {s(T2)}/>
<ellipse cx="62" cy="78" rx="42" ry="21" fill="#B7A552" {s()} stroke-dasharray="1 7"/>
<ellipse cx="62" cy="78" rx="40" ry="19" fill="#A8963F" {s()}/>
<circle cx="74" cy="72" r="3" fill="#8A7A3C"/><circle cx="84" cy="84" r="2.6" fill="#8A7A3C"/><circle cx="62" cy="88" r="2.6" fill="#8A7A3C"/><circle cx="90" cy="74" r="2.2" fill="#8A7A3C"/>
<circle cx="36" cy="70" r="8" fill="#fff" {s(T2)}/><circle cx="52" cy="66" r="8" fill="#fff" {s(T2)}/>
<circle cx="37" cy="68" r="3.6" fill="{O}"/><circle cx="53" cy="64" r="3.6" fill="{O}"/>
<path d="M30 84 Q38 90 46 84" fill="none" {s(T2)}/>
{BL.format(26, 80)}
{bub(40, 50, 4.6)}{bub(48, 40, 3)}{bub(34, 40, 2.4)}
''', 60, 16)
SUBJ["ss1-eseninsky"] = ("плоский оливковый палтус с двумя глазами на одном боку",
                         "лежит у песчаного дна голубого бассейна и смотрит вверх на красно-белую разделительную дорожку, пуская пузыри")

# 5. Школа плавания № 1, бассейн «Качаловский» — рыба-усач в роли усатого тренера со свистком на бортике
ICONS["ss1-kachalovsky"] = W("#FFE6DC", "#FF7652", f'''
<path d="M-6 100 H134 V134 H-6Z" fill="#fff" {s()}/>
<path d="M10 100 v34 M34 100 v34 M58 100 v34 M82 100 v34 M106 100 v34 M-6 116 H134" fill="none" stroke="#7FC8F0" stroke-width="2.4"/>
<path d="M52 100 Q40 110 30 106 Q40 96 50 92Z M76 100 Q88 110 98 106 Q88 96 78 92Z" fill="#B77A1E" {s(T2)}/>
<path d="M40 60 Q38 22 64 20 Q90 22 88 60 Q88 98 64 100 Q40 98 40 60Z" fill="#E0A63A" {s()}/>
<path d="M52 84 q12 8 24 0 M50 74 q14 8 28 0" fill="none" stroke="#B77A1E" stroke-width="2.4" stroke-linecap="round"/>
<path d="M40 56 Q22 54 20 68 Q30 72 42 68Z M88 56 Q106 54 108 68 Q98 72 86 68Z" fill="#B77A1E" {s(T2)}/>
<path d="M56 22 Q64 6 72 22Z" fill="#B77A1E" {s(T2)}/>
{eye(54, 42, 1.15)}{eye(74, 42, 1.15)}
<path d="M56 54 Q64 60 72 54" fill="none" {s(T2)}/>
<path d="M54 52 Q36 50 26 40 M54 55 Q38 60 30 72 M74 52 Q92 50 102 40 M74 55 Q90 60 98 72" fill="none" {s(T2)}/>
<path d="M50 62 Q64 80 78 62" fill="none" stroke="#3A6BE0" stroke-width="2.6"/>
<rect x="58" y="72" width="14" height="9" rx="3" fill="#E8443A" {s(T2)}/><circle cx="72" cy="76" r="4.6" fill="#E8443A" {s(T2)}/>
{BL.format(46, 50)}{BL.format(82, 50)}
''', 64, 20)
SUBJ["ss1-kachalovsky"] = ("золотистая рыба-усач с четырьмя длинными усами",
                           "стоит на хвосте на бело-голубом кафельном бортике как усатый тренер с красным свистком на шее, фон кораллово-оранжевый")

# 6. Школа плавания № 1, бассейн «Большой Одинцовский» — утка-крохаль с рыжим «ирокезом» плывёт кролем
ICONS["ss1-odintsovo-mozhayskoe"] = W("#EEF4FF", "#7C9DFF", f'''
<path d="M-6 78 Q30 70 64 78 T134 76 V134 H-6Z" fill="#3B66DB" {s()}/>
<path d="M22 66 Q30 44 60 46 Q84 48 90 70 Q70 86 44 84 Q26 82 22 66Z" fill="#E9EEF5" {s()}/>
<path d="M22 66 Q10 60 6 70 Q14 76 26 74Z" fill="#9AA6BA" {s(T2)}/>
<path d="M48 52 Q56 24 76 16 Q78 34 70 56Z" fill="#9AA6BA" {s()}/>
<path d="M74 18 l8 -8 M78 26 l10 -6 M70 14 l2 -9" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<circle cx="96" cy="56" r="15" fill="#C4552B" {s()}/>
<path d="M86 46 L72 36 L84 42 L74 28 L88 38 L84 24 L94 40Z" fill="#C4552B" {s(T2)}/>
<path d="M108 56 L128 60 L108 64Z" fill="#E8443A" {s(T2)}/>
<rect x="92" y="48" width="16" height="9" rx="4.5" fill="#7FE0FF" {s(T2)}/><circle cx="101" cy="52.5" r="2" fill="{O}"/>
<path d="M84 50 h8" fill="none" {s(T2)}/>
{BL.format(94, 64)}
<path d="M8 96 q9 -5 18 0 M50 104 q9 -5 18 0 M92 98 q9 -5 18 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 30, 20)
SUBJ["ss1-odintsovo-mozhayskoe"] = ("утка-крохаль с рыжей головой, лохматым хохолком-ирокезом и тонким красным клювом",
                                    "плывёт кролем в голубых очках — серое крыло взлетает над синей водой, с него летят брызги, фон сиренево-голубой")

# 7. «Академия воды» (Фрязевская) — гагарка-профессор в академической шапочке объясняет у доски, как плыть
ICONS["akademiya-vody-fryazevskaya"] = W("#FFF8D6", "#F0AE35", f'''
<rect x="52" y="22" width="68" height="52" rx="5" fill="#2F7D5B" {s()}/>
<path d="M60 58 q7 -6 14 0 t14 0 t14 0 t10 0" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<circle cx="82" cy="42" r="4" fill="none" stroke="#fff" stroke-width="2.6"/>
<path d="M86 46 l14 4 M90 47 l8 -8 M100 50 l10 -2" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<path d="M50 60 L74 34" fill="none" stroke="{O}" stroke-width="5.5" stroke-linecap="round"/>
<path d="M50 60 L74 34" fill="none" stroke="#C98B4A" stroke-width="2.4" stroke-linecap="round"/>
<path d="M14 80 Q10 44 36 42 Q60 44 56 82 Q54 112 36 112 Q16 112 14 80Z" fill="#232A3D" {s()}/>
<path d="M24 84 Q22 62 36 62 Q50 62 48 86 Q46 106 36 106 Q26 106 24 84Z" fill="#fff" {s(T2)}/>
<path d="M54 70 Q62 62 58 54" fill="none" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M26 112 q-6 6 2 6 h8 M44 112 q6 6 -2 6 h-8" fill="#232A3D" {s(T2)}/>
{eye(30, 54, 1)}{eye(44, 54, 1)}
<path d="M30 60 Q37 58 46 62 Q40 70 30 66Z" fill="#232A3D" {s(T2)}/><path d="M36 60 v7" stroke="#fff" stroke-width="2"/>
<path d="M14 38 L36 28 L58 38 L36 48Z" fill="#3757C9" {s()}/>
<path d="M56 38 v12" fill="none" {s(T2)}/><circle cx="56" cy="52" r="3" fill="#FFD23F" {s(T2)}/>
''', 26, 20)
SUBJ["akademiya-vody-fryazevskaya"] = ("чёрно-белая птица гагарка в синей академической шапочке с кисточкой",
                                       "стоит с указкой у зелёной школьной доски, на которой мелом нарисованы пловец и волны, фон янтарно-жёлтый")

# 8. «Акваторика» (Фрязевская) — рыба-брызгун из-под воды сбивает струйкой мячик
ICONS["akvatorika-fryazevskaya"] = W("#D9FFF6", "#119F97", f'''
<path d="M-6 34 Q30 28 64 34 T134 32 V-6 H-6Z" fill="#FFF3B8" {s()}/>
<circle cx="92" cy="22" r="13" fill="#fff" {s()}/>
<path d="M80 18 Q92 26 104 18 M84 30 Q92 22 100 30" fill="none" stroke="#E8443A" stroke-width="4"/>
<circle cx="92" cy="22" r="13" fill="none" {s()}/>
<path d="M88 2 l-3 -6 M98 4 l4 -6 M106 12 l7 -3" fill="none" stroke="#E8443A" stroke-width="2.6" stroke-linecap="round"/>
<circle cx="64" cy="64" r="3" fill="#fff"/><circle cx="72" cy="52" r="3.4" fill="#fff"/><circle cx="80" cy="42" r="3.8" fill="#fff"/><circle cx="86" cy="36" r="3" fill="#fff"/>
<g transform="rotate(-32 48 88)">
<path d="M10 88 l-14 -12 q-4 12 0 24Z" fill="#F2C14E" {s(T2)}/>
<path d="M8 88 Q20 62 52 64 Q78 68 88 88 Q76 108 50 110 Q20 112 8 88Z" fill="#E6EDF2" {s()}/>
<path d="M30 68 Q36 88 30 108 Q24 100 24 78Z M48 64 Q56 88 48 110 Q42 100 42 72Z" fill="#2A3350"/>
<path d="M40 64 Q50 52 62 66Z" fill="#F2C14E" {s(T2)}/>
{eye(70, 82, 1.3)}
<ellipse cx="88" cy="88" rx="4" ry="3" fill="#FF8FA8" {s(T2)}/>
{BL.format(62, 94)}
</g>
{bub(104, 86, 4.6)}{bub(112, 70, 3)}{bub(20, 60, 3.4)}
''', 30, 60)
SUBJ["akvatorika-fryazevskaya"] = ("серебристая рыба-брызгун с чёрными поперечными полосками",
                                   "из-под зелёной воды пускает вверх струйку-пунктир и сбивает с поверхности бело-красный мячик")

# 9. SwimClub (Фрязевская, «Олимпия») — илистый прыгун перепрыгивает разделительную дорожку
ICONS["swimclub-fryazevskaya"] = W("#F7F1FF", "#B7A0FF", f'''
<path d="M-6 92 Q30 84 64 92 T134 90 V134 H-6Z" fill="#35BDEB" {s()}/>
{rope([(8, 100), (22, 98), (36, 97), (50, 97), (64, 98), (78, 97), (92, 97), (106, 98), (120, 100)], "#FFD23F", "#fff", 5)}
<path d="M14 88 Q24 30 64 22" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="2 8" stroke-linecap="round"/>
<g transform="rotate(-18 68 50)">
<path d="M28 58 l-16 -8 q-2 12 4 20Z" fill="#7A6A4F" {s(T2)}/>
<path d="M48 40 Q56 18 74 24 Q70 34 66 42Z" fill="#5FB8E8" {s(T2)}/><circle cx="60" cy="32" r="1.8" fill="#fff"/><circle cx="67" cy="30" r="1.8" fill="#fff"/>
<path d="M26 58 Q34 40 62 40 Q92 40 102 54 Q100 70 76 72 Q40 74 26 58Z" fill="#9C8763" {s()}/>
<circle cx="44" cy="54" r="2" fill="#5FB8E8"/><circle cx="56" cy="62" r="2" fill="#5FB8E8"/><circle cx="68" cy="52" r="2" fill="#5FB8E8"/><circle cx="52" cy="48" r="1.8" fill="#5FB8E8"/>
<path d="M70 66 Q64 84 52 82 Q58 72 62 64Z" fill="#C7B38A" {s(T2)}/>
<circle cx="84" cy="38" r="8" fill="#fff" {s(T2)}/><circle cx="98" cy="40" r="8" fill="#fff" {s(T2)}/>
<circle cx="86" cy="38" r="3.4" fill="{O}"/><circle cx="100" cy="40" r="3.4" fill="{O}"/>
<path d="M84 58 Q92 64 100 58" fill="none" {s(T2)}/>
{BL.format(78, 56)}
</g>
<circle cx="18" cy="76" r="3" fill="#fff"/><circle cx="26" cy="66" r="2.4" fill="#fff"/><circle cx="10" cy="64" r="2.2" fill="#fff"/>
''', 70, 18)
SUBJ["swimclub-fryazevskaya"] = ("коричневая рыбка илистый прыгун с глазами навыкате и голубым плавником-парусом",
                                 "выпрыгнула из голубой воды и по дуге перелетает через жёлто-белую разделительную дорожку, фон светло-сиреневый")

# 10. SwimClub (Земляной Вал, «Университетский») — команда: три мойвы в разных шапочках плывут клином по трём дорожкам
def _moyva(x, y, cap):
    return f'''<path d="M{x - 9} {y + 30} l-4 14 q13 6 26 0 l-4 -14Z" fill="#9FB4C8" {s(T2)}/>
<path d="M{x - 13} {y} Q{x - 14} {y + 26} {x} {y + 36} Q{x + 14} {y + 26} {x + 13} {y} Q{x} {y - 16} {x - 13} {y}Z" fill="#DCE6EE" {s()}/>
<path d="M{x - 13} {y + 2} Q{x} {y - 22} {x + 13} {y + 2} Q{x} {y - 4} {x - 13} {y + 2}Z" fill="{cap}" {s(T2)}/>
<circle cx="{x - 6}" cy="{y + 7}" r="2.6" fill="{O}"/><circle cx="{x + 6}" cy="{y + 7}" r="2.6" fill="{O}"/>
<path d="M{x - 3} {y + 13} q3 3 6 0" fill="none" {s(T2)}/>'''


ICONS["swimclub-zemlyanoy-val"] = W("#9BE8FF", "#1A78D2", f'''
{rope([(43, 6), (43, 20), (43, 34), (43, 48), (43, 62), (43, 76), (43, 90), (43, 104), (43, 118)], "#fff", "#FF6FA0", 3.6)}
{rope([(85, 6), (85, 20), (85, 34), (85, 48), (85, 62), (85, 76), (85, 90), (85, 104), (85, 118)], "#fff", "#FF6FA0", 3.6)}
<path d="M16 112 q6 8 12 0 M58 96 q6 8 12 0 M100 114 q6 8 12 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
{_moyva(22, 62, "#E8443A")}{_moyva(64, 36, "#FFD23F")}{_moyva(106, 64, "#3DBE7A")}
''', 50, 10)
SUBJ["swimclub-zemlyanoy-val"] = ("три серебристые рыбки-мойвы в красной, жёлтой и зелёной плавательных шапочках",
                                  "плывут клином по трём дорожкам бассейна, вид сверху: средняя вырвалась вперёд, между ними бело-розовые разделители")

# 11. SwimClub (ул. Юности, бассейн МосГУ) — малыш-кракен держится щупальцами за дорожку и учится работать «ногами»
ICONS["swimclub-yunosti"] = W("#4257C4", "#131A52", f'''
{sparkle(20, 22, 3)}{sparkle(108, 30, 4)}
<path d="M40 70 Q20 84 14 104 M52 74 Q44 96 34 114 M76 74 Q84 96 94 114 M88 70 Q108 84 114 104" fill="none" stroke="{O}" stroke-width="12" stroke-linecap="round"/>
<path d="M40 70 Q20 84 14 104 M52 74 Q44 96 34 114 M76 74 Q84 96 94 114 M88 70 Q108 84 114 104" fill="none" stroke="#FF6B6B" stroke-width="6.6" stroke-linecap="round"/>
<path d="M64 6 Q92 30 90 58 Q88 80 64 80 Q40 80 38 58 Q36 30 64 6Z" fill="#FF6B6B" {s()}/>
<path d="M50 20 Q40 10 34 16 Q40 24 46 28Z M78 20 Q88 10 94 16 Q88 24 82 28Z" fill="#E04A5A" {s(T2)}/>
{eye(54, 52, 1.5)}{eye(74, 52, 1.5)}
<path d="M58 66 Q64 72 70 66" fill="none" {s(T2)}/>
{BL.format(44, 62)}{BL.format(84, 62)}
<path d="M30 90 Q8 84 4 94 M98 90 Q120 84 124 94" fill="none" stroke="{O}" stroke-width="12" stroke-linecap="round"/>
<path d="M30 90 Q8 84 4 94 M98 90 Q120 84 124 94" fill="none" stroke="#FF8A8A" stroke-width="6.6" stroke-linecap="round"/>
{rope([(8, 94), (22, 93), (36, 92), (50, 92), (64, 92), (78, 92), (92, 92), (106, 93), (120, 94)], "#fff", "#FFD23F", 5.4)}
{bub(100, 54, 4)}{bub(24, 50, 3)}
''', 50, 20)
SUBJ["swimclub-yunosti"] = ("красный малыш-кракен с острой мантией-колпачком и огромными глазами",
                            "в тёмно-синей глубине обнял двумя щупальцами бело-жёлтую разделительную дорожку и болтает остальными, как ногами")

# 12. Swimming Moscow (ул. Щорса, бассейн «Восход») — хариус с плавником-веером выпрыгивает на фоне восходящего солнца
ICONS["swimming-moscow-shchorsa"] = W("#FFEFB0", "#FF6A45", f'''
<circle cx="64" cy="84" r="34" fill="#FFF3B8" opacity=".95"/>
<path d="M64 40 v-12 M34 54 l-9 -9 M94 54 l9 -9 M20 80 h-12 M108 80 h12" fill="none" stroke="#FFF3B8" stroke-width="4" stroke-linecap="round"/>
<path d="M-6 88 Q30 80 64 88 T134 86 V134 H-6Z" fill="#2C63D4" {s()}/>
<g transform="rotate(-24 64 64)">
<path d="M30 66 l-18 -12 q-4 14 2 26Z" fill="#7C6BC4" {s(T2)}/>
<path d="M40 52 Q46 14 78 20 Q92 30 90 54Z" fill="#B48AF0" {s()}/>
<circle cx="56" cy="38" r="3" fill="#FF8A3D"/><circle cx="68" cy="30" r="3" fill="#FF8A3D"/><circle cx="78" cy="40" r="3" fill="#FF8A3D"/><circle cx="64" cy="44" r="2.4" fill="#FFD23F"/>
<path d="M28 66 Q40 46 70 48 Q98 50 108 66 Q96 82 68 84 Q40 84 28 66Z" fill="#D3DBEA" {s()}/>
<path d="M60 80 Q58 94 48 92 Q52 84 54 78Z" fill="#7C6BC4" {s(T2)}/>
{eye(90, 62, 1.25)}
<path d="M98 72 Q102 74 106 70" fill="none" {s(T2)}/>
{BL.format(82, 72)}
</g>
<path d="M30 100 q-8 -12 -2 -18 M40 104 q-2 -12 6 -16" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M76 110 q9 -5 18 0 M98 102 q8 -4 16 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 50, 62)
SUBJ["swimming-moscow-shchorsa"] = ("серебристый хариус с высоким сиреневым спинным плавником-веером в оранжевых пятнышках",
                                    "выпрыгивает из синей воды на фоне большого восходящего солнца, небо оранжево-красное")

# 13. Swimming Moscow (ул. Саморы Машела, ФОК «Гармония») — келпи, водяная лошадка с гривой-волной
ICONS["swimming-moscow-samory-mashela"] = W("#FFE6EE", "#FF8CAE", f'''
<path d="M44 124 Q30 80 50 52 Q58 34 78 32 Q100 34 106 54 Q110 72 96 78 Q84 80 80 70 Q74 84 78 124Z" fill="#7FD0FF" {s()}/>
<path d="M56 30 Q58 14 68 12 Q70 22 68 34Z" fill="#7FD0FF" {s(T2)}/>
<path d="M46 124 Q14 104 26 76 Q20 58 38 52 Q30 38 50 34 Q46 22 60 24 Q52 40 50 56 Q40 84 54 124Z" fill="#E9FBFF" {s()}/>
<path d="M30 78 q8 -2 10 6 M40 54 q8 0 8 8 M52 36 q6 2 4 8" fill="none" stroke="#35BDEB" stroke-width="2.6" stroke-linecap="round"/>
{eye(82, 52, 1.3)}
<ellipse cx="100" cy="66" rx="3" ry="2.2" fill="{O}"/>
<path d="M90 74 Q96 78 102 74" fill="none" {s(T2)}/>
{BL.format(74, 62)}
<path d="M58 40 Q74 28 92 36" fill="none" stroke="{O}" stroke-width="6" stroke-linecap="round"/>
<path d="M58 40 Q74 28 92 36" fill="none" stroke="#FFD23F" stroke-width="2.6" stroke-linecap="round"/>
<rect x="64" y="24" width="12" height="10" rx="5" fill="#FF5E9A" {s(T2)}/><rect x="80" y="26" width="12" height="10" rx="5" fill="#FF5E9A" {s(T2)}/>
<path d="M-6 100 Q30 92 64 100 T134 98 V134 H-6Z" fill="#12B3B0" {s()}/>
<path d="M12 114 q9 -5 18 0 M84 116 q9 -5 18 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
{bub(112, 84, 3.6)}{bub(118, 72, 2.4)}
''', 70, 20)
SUBJ["swimming-moscow-samory-mashela"] = ("голубая водяная лошадка-келпи с белой гривой, закрученной как морская волна",
                                          "вынырнула по шею из бирюзовой воды, на лбу розовые плавательные очки на жёлтой резинке, фон розовый")

# 14. Swimming Moscow (ул. Коштоянца, бассейн «Заряд») — заряженный аллигаторёнок в шапочке с молнией молотит хвостом
ICONS["swimming-moscow-koshtoyantsa"] = W("#F7FFC9", "#A2D82A", f'''
<path d="M-6 80 Q30 72 64 80 T134 78 V134 H-6Z" fill="#1E9BF5" {s()}/>
<path d="M30 72 Q10 60 6 38 Q20 44 34 62Z" fill="#3FA34D" {s()}/>
<circle cx="8" cy="30" r="3" fill="#fff"/><circle cx="18" cy="24" r="2.4" fill="#fff"/><circle cx="2" cy="44" r="2.4" fill="#fff"/><circle cx="24" cy="34" r="2" fill="#fff"/>
<path d="M26 74 Q30 56 56 56 Q76 56 84 70 Q70 90 44 88 Q28 86 26 74Z" fill="#4CB85C" {s()}/>
<path d="M40 58 l4 -7 l4 7 M52 56 l4 -7 l4 7" fill="#3FA34D" {s(T2)}/>
<path d="M58 60 Q70 30 92 34 Q84 46 74 64Z" fill="#4CB85C" {s()}/>
<path d="M74 60 Q78 46 96 48 L124 60 Q126 70 118 74 L84 78 Q72 74 74 60Z" fill="#4CB85C" {s()}/>
<path d="M88 72 l4 5 l4 -5 l4 5 l4 -5 l4 5 l4 -5" fill="#fff" {s(T18)}/>
<path d="M72 60 Q76 40 96 46 Q88 52 84 62Z" fill="#E8443A" {s()}/>
<path d="M84 46 l-4 7 h5 l-3 7" fill="none" stroke="#FFD23F" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
{eye(98, 58, 1.1)}
<circle cx="120" cy="60" r="1.6" fill="{O}"/>
{BL.format(90, 66)}
<path d="M10 100 q9 -5 18 0 M52 106 q9 -5 18 0 M94 98 q9 -5 18 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 60, 20)
SUBJ["swimming-moscow-koshtoyantsa"] = ("зелёный аллигаторёнок в красной плавательной шапочке с жёлтой молнией",
                                        "плывёт кролем по ярко-синей воде и взбивает хвостом фонтан брызг, фон салатовый")

# 15. Swimming Moscow (бул. Дмитрия Донского, «Качаловский») — мозазаврик высунулся из воды и держит на носу доску для плавания
ICONS["swimming-moscow-donskogo"] = W("#FFFFFF", "#BFE4F3", f'''
<path d="M-6 84 Q30 76 64 84 T134 82 V134 H-6Z" fill="#0E8CA6" {s()}/>
<path d="M96 96 Q110 84 122 92 Q112 100 100 102Z" fill="#2F7D5B" {s(T2)}/>
<path d="M30 124 Q24 84 44 62 Q54 50 70 50 L98 44 Q110 46 108 56 Q104 66 88 68 Q74 72 70 88 Q68 104 72 124Z" fill="#3FA37A" {s()}/>
<path d="M40 96 Q46 76 56 68 Q52 90 54 124 H42Z" fill="#CFF2DC" {s(T2)}/>
<path d="M44 62 l-6 -8 l10 2 M52 54 l-4 -9 l10 4" fill="#2F7D5B" {s(T2)}/>
<path d="M84 60 l3 5 l3 -5 l3 5 l3 -5 l3 5" fill="#fff" {s(T18)}/>
{eye(74, 54, 1.15)}
{BL.format(66, 64)}
<g transform="rotate(-10 96 30)">
<rect x="74" y="20" width="46" height="22" rx="9" fill="#E8443A" {s()}/>
<path d="M84 26 h26 M84 34 h26" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
</g>
<path d="M10 100 q9 -5 18 0 M84 110 q9 -5 18 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
{bub(18, 66, 4)}{bub(26, 54, 2.6)}
''', 40, 24)
SUBJ["swimming-moscow-donskogo"] = ("зелёный морской ящер мозазаврик со светлым животиком и гребешком на макушке",
                                    "высунул длинную шею из тёмно-бирюзовой воды и удерживает на носу красную доску для плавания, фон светлый, почти белый")

# 16. Swimming Moscow (Остафьевская ул., бассейн «Максимум») — выпь вытянулась во весь рост и меряет глубину
ICONS["swimming-moscow-ostafyevskaya"] = W("#49D3CB", "#0A5C70", f'''
<rect x="88" y="10" width="14" height="112" rx="4" fill="#fff" {s()}/>
<path d="M88 26 h8 M88 42 h8 M88 58 h8 M88 74 h8 M88 90 h8 M88 106 h8" fill="none" stroke="#E8443A" stroke-width="3"/>
<path d="M22 124 Q16 86 40 78 Q48 74 46 60 L46 44 H62 L62 60 Q60 74 68 78 Q86 86 80 124Z" fill="#E6BE74" {s()}/>
<path d="M24 100 Q10 96 8 108 Q18 114 28 110Z" fill="#C79A4E" {s(T2)}/>
<path d="M50 52 v8 M58 56 v10 M40 88 v8 M52 84 v12 M64 88 v10 M32 98 v6 M72 98 v6" fill="none" stroke="#8A5A2B" stroke-width="2.6" stroke-linecap="round"/>
<path d="M48 26 L54 0 L60 26Z" fill="#F2B632" {s(T2)}/>
<circle cx="54" cy="36" r="15" fill="#E6BE74" {s()}/>
<path d="M41 30 Q54 18 67 30 Q54 26 41 30Z" fill="#5A3A1C" {s(T2)}/>
{eye(48, 38, 1)}{eye(60, 38, 1)}
{BL.format(41, 45)}{BL.format(67, 45)}
<path d="M-6 96 Q30 88 64 96 T134 94 V134 H-6Z" fill="#1FA9E0" opacity=".9" {s()}/>
<path d="M8 112 q9 -5 18 0 M100 114 q9 -5 18 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
{bub(22, 70, 4)}{bub(114, 60, 3)}
''', 30, 20)
SUBJ["swimming-moscow-ostafyevskaya"] = ("песочно-рыжая болотная птица выпь в тёмных пестринах",
                                         "стоит по грудь в воде, вытянув шею и клюв строго вверх рядом с белой рейкой-глубиномером с красными делениями, фон тёмно-бирюзовый")

# 17. Swimming Moscow (Внуково, бассейн «Пегас» у аэропорта) — морская птица глупыш в лётном шлеме заходит на посадку на дорожку
ICONS["swimming-moscow-vnukovo"] = W("#FFFFFF", "#86CCFF", f'''
<path d="M84 22 q4 -10 14 -6 q8 -8 16 2 q10 0 8 10 H84Z" fill="#fff" opacity=".95"/>
<path d="M-6 102 Q30 94 64 102 T134 100 V134 H-6Z" fill="#2B7DE0" {s()}/>
{rope([(40, 116), (54, 113), (68, 111), (82, 110), (96, 110), (110, 111), (124, 113)], "#FFD23F", "#fff", 4.4)}
<g transform="rotate(22 56 56)">
<path d="M40 50 Q20 20 -4 22 Q10 40 30 62Z" fill="#AEB9C9" {s()}/>
<path d="M62 46 Q72 14 98 8 Q94 32 76 56Z" fill="#AEB9C9" {s()}/>
<path d="M26 60 Q30 40 56 42 Q84 44 90 62 Q78 80 52 78 Q30 76 26 60Z" fill="#fff" {s()}/>
<path d="M26 60 Q14 58 10 68 Q20 72 30 68Z" fill="#AEB9C9" {s(T2)}/>
<path d="M72 44 Q84 34 96 46 Q100 56 94 62 Q82 54 72 52Z" fill="#8A5A2B" {s()}/>
<path d="M90 60 L108 66 L92 70Z" fill="#FFD23F" {s(T2)}/>
<rect x="80" y="50" width="14" height="9" rx="4.5" fill="#7FE0FF" {s(T2)}/><circle cx="88" cy="54.5" r="2" fill="{O}"/>
<path d="M52 78 l-2 16 m-6 0 h12 M64 78 l2 16 m-6 0 h12" fill="none" stroke="{O}" stroke-width="5" stroke-linecap="round"/>
<path d="M52 78 l-2 16 m-6 0 h12 M64 78 l2 16 m-6 0 h12" fill="none" stroke="#FF8FA8" stroke-width="2.2" stroke-linecap="round"/>
</g>
<path d="M22 100 q-6 -10 0 -14 M12 104 q-8 -6 -6 -12" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 30, 30)
SUBJ["swimming-moscow-vnukovo"] = ("бело-серая морская птица глупыш в коричневом лётном шлеме и голубых очках",
                                   "заходит на посадку на синюю воду, выставив розовые лапки как шасси, внизу жёлто-белая дорожка-«полоса», в небе облако")

# 18. Семейный аквацентр «ФламинGo!» (Селятино, с 1,5 месяцев) — мама-ходулочник на длинных розовых ногах и птенец в нарукавниках
ICONS["flamingo-selyatino"] = W("#F0FFFB", "#74DCCB", f'''
<g transform="translate(-8 12)">
<path d="M52 62 V112 M66 62 V112" fill="none" stroke="{O}" stroke-width="6.4" stroke-linecap="round"/>
<path d="M52 62 V112 M66 62 V112" fill="none" stroke="#FF6FA0" stroke-width="3" stroke-linecap="round"/>
<path d="M30 48 Q32 26 58 28 Q84 30 88 50 Q76 66 54 64 Q34 62 30 48Z" fill="#fff" {s()}/>
<path d="M30 48 Q32 26 58 28 Q70 30 80 38 Q58 40 44 50 Q36 54 30 48Z" fill="#2A3350" {s(T2)}/>
<path d="M30 48 Q18 46 12 54 Q22 58 34 54Z" fill="#2A3350" {s(T2)}/>
<path d="M82 46 Q86 24 96 18" fill="none" stroke="{O}" stroke-width="12" stroke-linecap="round"/>
<path d="M82 46 Q86 24 96 18" fill="none" stroke="#fff" stroke-width="6.4" stroke-linecap="round"/>
<circle cx="98" cy="16" r="10" fill="#fff" {s()}/>
<path d="M90 12 Q98 2 106 12 Q98 9 90 12Z" fill="#2A3350" {s(T2)}/>
{eye(100, 16, .9)}
<path d="M106 18 L126 24" fill="none" stroke="{O}" stroke-width="3" stroke-linecap="round"/>
</g>
<path d="M-6 96 Q30 88 64 96 T134 94 V134 H-6Z" fill="#2FA8E8" {s()}/>
<circle cx="96" cy="90" r="13" fill="#EDE3CF" {s()}/>
<path d="M90 80 l2 -7 l4 6 l4 -7 l2 8" fill="none" {s(T2)}/>
{eye(92, 90, .85)}{eye(101, 90, .85)}
<path d="M94 97 l3 3 l3 -3" fill="#FF8A1F" {s(T18)}/>
<ellipse cx="80" cy="98" rx="6" ry="7" fill="#FF8A1F" {s(T2)}/><ellipse cx="112" cy="98" rx="6" ry="7" fill="#FF8A1F" {s(T2)}/>
<path d="M14 112 q9 -5 18 0 M52 118 q9 -5 18 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 30, 20)
SUBJ["flamingo-selyatino"] = ("чёрно-белая птица ходулочник на длинных розовых ногах с пушистым птенцом",
                              "мама стоит в голубой воде и смотрит, как птенец в оранжевых нарукавниках плавает у её ног, фон светло-бирюзовый")

# 19. Школа плавания Григория Фалько (Заречье) — пятнистый тюленёнок-ларга с золотой медалью
ICONS["falko-zarechye"] = W("#EEF2F8", "#8C9FBD", f'''
<path d="M-6 88 Q30 80 64 88 T134 86 V134 H-6Z" fill="#2E86DE" {s()}/>
<path d="M30 124 Q24 70 40 48 Q50 30 64 30 Q78 30 88 48 Q104 70 98 124Z" fill="#C9CED8" {s()}/>
<circle cx="44" cy="84" r="3" fill="#7C8598"/><circle cx="86" cy="80" r="3.4" fill="#7C8598"/><circle cx="50" cy="100" r="2.6" fill="#7C8598"/><circle cx="82" cy="100" r="2.6" fill="#7C8598"/><circle cx="40" cy="66" r="2.4" fill="#7C8598"/><circle cx="90" cy="64" r="2.4" fill="#7C8598"/>
<path d="M40 46 Q64 14 88 46 Q64 36 40 46Z" fill="#E8443A" {s()}/>
{eye(54, 54, 1.3)}{eye(74, 54, 1.3)}
<ellipse cx="64" cy="66" rx="10" ry="7" fill="#EEF0F4" {s(T2)}/>
<path d="M60 62 h8 l-4 5Z" fill="{O}"/>
<path d="M56 66 h-16 M56 69 l-14 5 M72 66 h16 M72 69 l14 5" fill="none" stroke="{O}" stroke-width="1.8" stroke-linecap="round"/>
{BL.format(44, 62)}{BL.format(84, 62)}
<path d="M50 74 L64 96 L78 74" fill="none" stroke="#3757C9" stroke-width="5"/>
<circle cx="64" cy="100" r="11" fill="#FFD23F" {s()}/>
<text x="64" y="105" font-family="Arial" font-weight="700" font-size="14" fill="#B77A1E" text-anchor="middle">1</text>
<path d="M28 96 Q14 92 10 102 Q20 108 32 104Z M100 96 Q114 92 118 102 Q108 108 96 104Z" fill="#AEB5C2" {s(T2)}/>
<path d="M6 116 q9 -5 18 0 M104 118 q9 -5 18 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 50, 18)
SUBJ["falko-zarechye"] = ("серый пятнистый тюленёнок-ларга в красной плавательной шапочке",
                          "вынырнул столбиком из синей воды с золотой медалью «1» на синей ленте, фон серо-голубой")

# 20. «Барракуда» (Звенигород) — школа плавания и синхронного плавания: синхронистка с зажимом на носу
ICONS["barrakuda-zvenigorod"] = W("#FFDDF5", "#BE3AB6", f'''
{sparkle(22, 28, 5)}{sparkle(106, 22, 4)}{sparkle(112, 58, 3)}
<path d="M84 70 Q100 44 96 14" fill="none" stroke="{O}" stroke-width="15" stroke-linecap="round"/>
<path d="M84 70 Q100 44 96 14" fill="none" stroke="#FFD2B0" stroke-width="9" stroke-linecap="round"/>
<path d="M38 124 Q38 86 64 84 Q90 86 90 124Z" fill="#19C2B4" {s()}/>
<path d="M52 88 l12 12 l12 -12" fill="none" stroke="#FFD23F" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="64" cy="58" r="25" fill="#FFD2B0" {s()}/>
<path d="M39 56 Q40 30 64 30 Q88 30 89 56 Q76 40 64 42 Q52 40 39 56Z" fill="#5A3A1C" {s()}/>
<circle cx="64" cy="24" r="11" fill="#5A3A1C" {s()}/>
<path d="M54 22 q10 -8 20 0" fill="none" stroke="#FFD23F" stroke-width="3" stroke-linecap="round"/>
<path d="M48 58 q5 -5 10 0 M70 58 q5 -5 10 0" fill="none" {s(T2)}/>
<path d="M60 70 V62 Q64 57 68 62 V70" fill="none" stroke="{O}" stroke-width="6.4" stroke-linecap="round"/>
<path d="M60 70 V62 Q64 57 68 62 V70" fill="none" stroke="#FF5E9A" stroke-width="3" stroke-linecap="round"/>
<path d="M54 76 Q64 84 74 76" fill="none" {s(T2)}/>
{BL.format(46, 68)}{BL.format(82, 68)}
<path d="M-6 104 Q30 96 64 104 T134 102 V134 H-6Z" fill="#2FB8E8" {s()}/>
<path d="M10 118 q9 -5 18 0 M96 120 q9 -5 18 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 40, 20)
SUBJ["barrakuda-zvenigorod"] = ("девочка-синхронистка с тугим пучком, розовым зажимом на носу и в бирюзовом купальнике",
                                "вынырнула из воды с закрытыми глазами и улыбкой, вскинув руку вверх, вокруг блёстки, фон малиново-розовый")

# 21. Школа плавания «Акварель» (Звенигород) — рыбка-мандаринка оставляет за собой акварельные мазки
ICONS["akvarel-zvenigorod"] = W("#FFFEF7", "#F1E0BD", f'''
<path d="M2 38 Q30 26 62 40" fill="none" stroke="#7FD0FF" stroke-width="13" stroke-linecap="round" opacity=".75"/>
<path d="M-2 62 Q22 54 44 64" fill="none" stroke="#FF9EC0" stroke-width="13" stroke-linecap="round" opacity=".75"/>
<path d="M4 88 Q26 78 50 88" fill="none" stroke="#FFD86B" stroke-width="13" stroke-linecap="round" opacity=".8"/>
<path d="M50 64 l-18 -16 q-6 16 0 32Z" fill="#2FB86E" {s(T2)}/>
<path d="M62 44 Q74 20 94 30 Q90 42 84 50Z" fill="#2FB86E" {s(T2)}/>
<path d="M70 84 Q72 102 88 98 Q86 88 82 80Z" fill="#2FB86E" {s(T2)}/>
<path d="M46 64 Q54 40 84 42 Q112 46 118 66 Q108 88 80 88 Q54 88 46 64Z" fill="#FF8A1F" {s()}/>
<path d="M58 60 q8 -10 16 0 t16 0 M56 74 q8 -8 16 0 t14 0" fill="none" stroke="#2456D6" stroke-width="4.4" stroke-linecap="round"/>
<path d="M66 50 q6 -4 12 0 M64 82 q8 4 16 0" fill="none" stroke="#19B3C6" stroke-width="3.4" stroke-linecap="round"/>
<circle cx="100" cy="60" r="8.4" fill="#fff" {s(T2)}/><circle cx="102" cy="60" r="4" fill="{O}"/><circle cx="100.6" cy="58.4" r="1.4" fill="#fff"/>
<path d="M106 74 Q111 77 115 72" fill="none" {s(T2)}/>
{BL.format(96, 74)}
<path d="M-6 112 Q30 104 64 112 T134 110 V134 H-6Z" fill="#5FC3F2" opacity=".85"/>
{bub(112, 34, 4.4)}{bub(120, 22, 2.8)}
''', 60, 30)
SUBJ["akvarel-zvenigorod"] = ("оранжевая рыбка-мандаринка в синих волнистых узорах с зелёными плавниками",
                              "плывёт по белой акварельной бумаге и оставляет за хвостом три прозрачных мазка — голубой, розовый и жёлтый")

if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for i in ids:
        open(os.path.join(OUT, i + ".svg"), "w", encoding="utf-8").write(ICONS[i])
    print("svg:", len(ids))
    for i in ids:
        print(f"{i} — герой: {SUBJ[i][0]} | сцена: {SUBJ[i][1]}")
