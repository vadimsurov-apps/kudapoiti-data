"""Иконки робота pools, 2026-11-13 (17 UTC). Каждая придумана и нарисована отдельно (правило абсолютной
уникальности): свой герой, своя сцена, своя компоновка и палитра. Герои проверены по реестру icons-src/subjects.txt,
картинки — tools/check_unique.py. Иконки «Аквазаврика» и «Аква Smart» нарисованы в прошлый запуск (tools/icons_pools_1113n.py).
Запуск: python3 tools/icons_pools_1113u.py [id …]  → python3 tools/render_icons.py <id…> → python3 tools/check_unique.py <id…>."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, sparkle, O
from icons_pools_1112b import W, bub, T2

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
BL = '<ellipse cx="{}" cy="{}" rx="4.4" ry="2.6" fill="#FF7FA8" opacity=".8"/>'

# 1. Школа плавания № 1, «Алтайский» (25 м, 7 дорожек) — касатка-малыш выпрыгивает свечкой
ICONS["ss1-altaysky"] = W("#FFF3DE", "#FF9A5A", f'''
<path d="M-6 90 Q28 82 62 90 T134 88 V134 H-6Z" fill="#2E7BD6" {s()}/>
<path d="M42 58 Q22 60 16 78 Q32 76 44 70Z" fill="#2B2B3F" {s()}/>
<path d="M86 58 Q106 60 112 78 Q96 76 84 70Z" fill="#2B2B3F" {s()}/>
<path d="M64 12 Q90 22 90 58 Q90 86 78 104 H50 Q38 86 38 58 Q38 22 64 12Z" fill="#2B2B3F" {s()}/>
<path d="M64 36 Q82 42 82 64 Q82 88 74 104 H54 Q46 88 46 64 Q46 42 64 36Z" fill="#fff"/>
<ellipse cx="50" cy="32" rx="6.5" ry="3.6" fill="#fff" transform="rotate(-28 50 32)"/>
<ellipse cx="78" cy="32" rx="6.5" ry="3.6" fill="#fff" transform="rotate(28 78 32)"/>
{eye(56, 50, .9)}{eye(72, 50, .9)}
<path d="M59 59 Q64 64 69 59" fill="none" {s(T2)}/>
{BL.format(51, 59)}{BL.format(77, 59)}
<path d="M-6 100 Q28 92 62 100 T134 98 V134 H-6Z" fill="#4A9BEE"/>
<path d="M-6 116 H134" stroke="{O}" stroke-width="11" stroke-linecap="round"/>
<path d="M-6 116 H134" stroke="#FFD23F" stroke-width="7" stroke-dasharray="11 9"/>
<path d="M30 96 l-9 -12 M42 92 l-3 -13 M86 92 l3 -13 M98 96 l9 -12" stroke="#fff" stroke-width="3.8" stroke-linecap="round"/>
{bub(20, 60, 4)}{bub(108, 52, 3)}
''', 64, 18)
SUBJ["ss1-altaysky"] = ("касатка-малыш с белыми пятнышками над глазами и белым животиком",
                        "выпрыгивает из воды свечкой, расставив грудные плавники, над жёлтым разделителем дорожек на оранжевом закате")

# 2. Школа плавания № 1, «Буревестник» — моржонок отдыхает на спине после заплыва
ICONS["ss1-burevestnik-plyushchikha"] = W("#EEF0FF", "#8D8FE0", f'''
<path d="M-6 70 Q28 62 62 70 T134 68 V134 H-6Z" fill="#35B8C9" {s()}/>
<path d="M22 86 Q20 70 40 68 H84 Q100 68 100 84 Q100 98 84 98 H40 Q24 98 22 86Z" fill="#B9825A" {s()}/>
<ellipse cx="62" cy="80" rx="22" ry="10" fill="#E4BE9A"/>
<path d="M50 78 Q40 70 46 62 Q56 66 58 76Z M74 78 Q84 70 78 62 Q68 66 66 76Z" fill="#9C6A45" {s(T2)}/>
<path d="M16 84 Q4 76 6 92 Q14 96 22 90Z" fill="#9C6A45" {s()}/>
<circle cx="98" cy="72" r="19" fill="#B9825A" {s()}/>
<ellipse cx="102" cy="80" rx="12" ry="8" fill="#E4BE9A" {s(T2)}/>
<path d="M97 85 v11 M107 85 v11" stroke="{O}" stroke-width="6.4" stroke-linecap="round"/>
<path d="M97 85 v11 M107 85 v11" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
<circle cx="102" cy="76" r="2.6" fill="{O}"/>
<path d="M90 66 q3 -4 6 0 M104 66 q3 -4 6 0" fill="none" {s(T2)}/>
{BL.format(88, 76)}{BL.format(115, 74)}
<path d="M60 58 Q54 40 60 30 M60 58 Q66 42 74 34 M60 58 Q52 46 44 40" fill="none" stroke="#fff" stroke-width="3.6" stroke-linecap="round"/>
<circle cx="60" cy="27" r="3" fill="#fff"/><circle cx="76" cy="31" r="2.6" fill="#fff"/><circle cx="42" cy="37" r="2.6" fill="#fff"/>
<path d="M-6 96 Q28 90 62 96 T134 94 V134 H-6Z" fill="#59CFDD"/>
<path d="M20 110 q9 -5 18 0 M64 114 q9 -5 18 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 30, 22)
SUBJ["ss1-burevestnik-plyushchikha"] = ("коричневый моржонок с двумя короткими белыми бивнями",
                                        "лежит на спине на воде, сложив ласты на светлом пузе, и пускает вверх фонтанчик на сиреневом фоне")

# 3. Школа плавания № 1, «Лужники» (50 м) — ужонок плывёт змейкой мимо таблички «50 м»
ICONS["ss1-luzhniki"] = W("#F6FFD6", "#A4DB46", f'''
<rect x="14" y="16" width="52" height="27" rx="7" fill="#fff" {s()}/>
<text x="40" y="36" font-family="Arial, sans-serif" font-size="18" font-weight="bold" text-anchor="middle" fill="{O}">50 м</text>
<path d="M-6 64 Q28 56 62 64 T134 62 V134 H-6Z" fill="#17B6C4" {s()}/>
<path d="M8 96 Q24 70 42 92 T74 92 T100 74" fill="none" stroke="{O}" stroke-width="17" stroke-linecap="round"/>
<path d="M8 96 Q24 70 42 92 T74 92 T100 74" fill="none" stroke="#3FA34D" stroke-width="10.6" stroke-linecap="round"/>
<path d="M8 96 Q24 70 42 92 T74 92 T100 74" fill="none" stroke="#2B7D3A" stroke-width="3" stroke-dasharray="2 9" stroke-linecap="round"/>
<ellipse cx="104" cy="68" rx="15" ry="12" fill="#3FA34D" {s()}/>
<ellipse cx="92" cy="61" rx="4.6" ry="3.4" fill="#FFD83D" {s(T2)}/><ellipse cx="93" cy="76" rx="4.6" ry="3.4" fill="#FFD83D" {s(T2)}/>
{eye(107, 65, .9)}
<path d="M110 74 Q114 76 117 72" fill="none" {s(T2)}/>
{BL.format(103, 74)}
<path d="M119 68 h7 l3 -3 M126 68 l3 3" fill="none" stroke="#FF5A6E" stroke-width="2.2" stroke-linecap="round"/>
<path d="M16 112 q9 -5 18 0 M56 116 q9 -5 18 0 M94 110 q9 -5 18 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M70 58 l4 -8 M82 54 l1 -9" stroke="#fff" stroke-width="3.2" stroke-linecap="round"/>
''', 70, 16)
SUBJ["ss1-luzhniki"] = ("зелёный ужонок с жёлтыми пятнышками-«ушками» на затылке",
                        "плывёт волнистой змейкой по бирюзовой воде, держа голову над водой, мимо белой таблички «50 м»")

# 4. Школа плавания № 1, МЭИ — сарган рвёт финишную ленточку
ICONS["ss1-mei"] = W("#F1E6FF", "#7B58DE", f'''
<path d="M-6 58 Q28 50 62 58 T134 56 V134 H-6Z" fill="#32C6E6" {s()}/>
<path d="M110 30 Q118 44 110 60" fill="none" stroke="{O}" stroke-width="10" stroke-linecap="round"/>
<path d="M110 30 Q118 44 110 60" fill="none" stroke="#FF4F5E" stroke-width="5.6" stroke-linecap="round"/>
<path d="M112 92 Q104 106 112 122" fill="none" stroke="{O}" stroke-width="10" stroke-linecap="round"/>
<path d="M112 92 Q104 106 112 122" fill="none" stroke="#FF4F5E" stroke-width="5.6" stroke-linecap="round"/>
<path d="M22 78 L4 64 Q10 78 4 92Z" fill="#2E9E78" {s()}/>
<path d="M44 68 Q54 56 64 67Z M48 88 Q56 98 64 89Z" fill="#2E9E78" {s()}/>
<path d="M18 78 Q50 62 90 72 L124 77 L90 84 Q50 94 18 78Z" fill="#CFEFE0" {s()}/>
<path d="M22 76 Q52 64 90 73 L118 77" fill="none" stroke="#2E9E78" stroke-width="5.4" stroke-linecap="round"/>
{eye(82, 77, .8)}
<path d="M88 82 Q92 84 95 81" fill="none" {s(T2)}/>
{BL.format(76, 84)}
<path d="M-2 70 h12 M-4 84 h10 M2 96 h12" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
{bub(34, 104, 4)}{bub(60, 112, 3)}{sparkle(98, 44, 5)}
''', 30, 16)
SUBJ["ss1-mei"] = ("серебристо-зелёный сарган с длинным клювом-иглой",
                   "стрелой пролетает под водой финиш и клювом разрывает красную ленточку на две половинки, фон фиолетовый")

# 5. Школа плавания № 1, «Динамо» — пара синих ласт шлёпает к воде
def _flip(x, y, a, side):
    return f'''<g transform="translate({x} {y}) rotate({a})">
<path d="M-11 30 Q-14 0 -24 -26 Q0 -40 24 -26 Q14 0 11 30 Q0 37 -11 30Z" fill="#2F6FE0" {s()}/>
<path d="M-10 -20 Q-6 -2 -6 14 M10 -20 Q6 -2 6 14 M0 -30 V-8" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round" opacity=".85"/>
<ellipse cx="0" cy="22" rx="8" ry="5" fill="#1C4BA8" {s(T2)}/>
{eye(0, 2, .95)}<path d="M{-5 * side} 10 Q0 14 {5 * side} 10" fill="none" {s(T2)}/>
</g>'''
ICONS["ss1-dinamo-leningradskoe"] = W("#FFFBD6", "#FFC531", f'''
<path d="M70 134 Q84 100 134 92 V134Z" fill="#35B5EA" {s()}/>
<path d="M96 118 q8 -5 16 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M12 112 q4 -9 9 0 q-4 6 -9 0Z M30 122 q4 -9 9 0 q-4 6 -9 0Z" fill="#9AD9F5" opacity=".9"/>
{_flip(46, 66, -16, 1)}{_flip(86, 54, 14, -1)}
<path d="M20 44 l-6 -8 M30 36 l-1 -10 M108 20 l5 -8" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
''', 40, 20)
SUBJ["ss1-dinamo-leningradskoe"] = ("пара синих ласт с белыми рёбрышками и глазками — близнецы",
                                    "шлёпают вразвалку по жёлтому бортику к уголку голубой воды, оставляя за собой мокрые следы")

# 6. «Аквабулько» (Реутов) — пузырёк «бульк» всплывает со дна
ICONS["akvabulko-reutov"] = W("#DDFFF5", "#17A396", f'''
<path d="M-6 26 Q28 18 62 26 T134 24" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".9"/>
<ellipse cx="64" cy="16" rx="18" ry="4" fill="none" stroke="#fff" stroke-width="2.6" opacity=".8"/>
<path d="M-6 112 Q30 104 64 112 T134 110 V134 H-6Z" fill="#F6D98C" {s()}/>
<ellipse cx="64" cy="114" rx="9" ry="3.4" fill="#C9A552"/>
<circle cx="64" cy="66" r="31" fill="#F2FFFF" opacity=".88" {s()}/>
<path d="M42 56 Q46 42 60 39" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<path d="M84 80 Q80 90 70 93" fill="none" stroke="#9FE3E0" stroke-width="4" stroke-linecap="round"/>
{eye(54, 66, 1.05)}{eye(74, 66, 1.05)}
<ellipse cx="64" cy="78" rx="4.6" ry="5.4" fill="{O}"/>
{BL.format(45, 75)}{BL.format(83, 75)}
{bub(22, 54, 6)}{bub(104, 46, 7)}{bub(30, 88, 4)}{bub(100, 86, 5)}{bub(64, 102, 3.4)}{bub(16, 74, 3)}{bub(112, 68, 3)}
''', 64, 22)
SUBJ["akvabulko-reutov"] = ("большой прозрачный пузырёк воздуха «бульк» с круглым ртом буквой «о»",
                            "всплывает с песчаного дна к поверхности под водой цвета морской волны в хороводе маленьких пузырьков")

# 7. World Swim (Реутов) — черепаха с картой мира на панцире
ICONS["world-swim-reutov"] = W("#FFE9E2", "#FF7C6B", f'''
<path d="M-6 52 Q28 44 62 52 T134 50 V134 H-6Z" fill="#8FE3EA" {s()}/>
<path d="M78 62 Q92 42 104 50 Q98 62 86 70Z M78 96 Q92 116 104 108 Q98 96 86 88Z" fill="#7CC95A" {s()}/>
<path d="M36 66 Q22 54 16 62 Q24 70 34 74Z M36 92 Q22 104 16 96 Q24 88 34 84Z" fill="#7CC95A" {s()}/>
<circle cx="104" cy="78" r="13" fill="#8ED36B" {s()}/>
<ellipse cx="60" cy="79" rx="32" ry="24" fill="#2C63D6" {s()}/>
<path d="M40 70 q6 -8 14 -4 q4 6 -2 10 q-2 8 -8 6 q-6 -4 -4 -12Z" fill="#59C766"/>
<path d="M60 64 q10 -4 18 2 q4 8 -4 12 q-8 2 -10 -4 q-6 -4 -4 -10Z" fill="#59C766"/>
<path d="M56 86 q6 -2 8 4 q0 8 -6 8 q-6 -4 -2 -12Z M76 88 q6 0 6 5 q-4 5 -8 1Z" fill="#59C766"/>
<path d="M30 79 H90 M60 56 V102" fill="none" stroke="#fff" stroke-width="1.6" opacity=".55"/>
<ellipse cx="60" cy="79" rx="32" ry="24" fill="none" {s()}/>
{eye(108, 75, .85)}
<path d="M106 84 Q110 87 114 83" fill="none" {s(T2)}/>
{BL.format(100, 83)}
<path d="M4 72 q6 -5 12 0 M0 88 q6 -5 12 0 M6 104 q6 -5 12 0" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round"/>
{sparkle(24, 28, 6)}{sparkle(98, 26, 4)}
''', 50, 14)
SUBJ["world-swim-reutov"] = ("морская черепаха с синим панцирем, на котором зелёными материками нарисована карта мира",
                             "плывёт вправо по светлой бирюзовой воде, широко загребая четырьмя ластами, под коралловым небом")

# 8. «АкваДарина» (Реутов) — мама качает малыша на воде
ICONS["akvadarina-reutov"] = W("#FFF3FA", "#E88BC2", f'''
<path d="M36 62 Q34 52 48 54 H58 Q70 54 68 66 V104 H36Z" fill="#7A5BE0" {s()}/>
<path d="M30 40 Q28 18 50 18 Q72 18 70 40 Q70 30 50 28 Q32 30 30 40Z" fill="#7B4A2E" {s()}/>
<circle cx="70" cy="22" r="8" fill="#7B4A2E" {s()}/>
<circle cx="50" cy="40" r="16" fill="#FFD9B8" {s()}/>
<path d="M34 36 Q40 24 54 26 Q64 26 66 36 Q58 28 50 30 Q40 30 34 36Z" fill="#7B4A2E"/>
<path d="M42 40 q3 -4 6 0 M54 40 q3 -4 6 0" fill="none" {s(T2)}/>
<path d="M46 47 Q51 52 56 47" fill="none" {s(T2)}/>
{BL.format(40, 46)}{BL.format(62, 46)}
<path d="M62 66 Q76 74 92 84" fill="none" stroke="{O}" stroke-width="12" stroke-linecap="round"/>
<path d="M62 66 Q76 74 92 84" fill="none" stroke="#FFD9B8" stroke-width="6.6" stroke-linecap="round"/>
<ellipse cx="92" cy="82" rx="16" ry="9" fill="#FFD9B8" {s()}/>
<path d="M82 78 Q92 70 102 78 L100 86 Q92 90 84 86Z" fill="#fff" {s(T2)}/>
<circle cx="96" cy="62" r="12" fill="#FFD9B8" {s()}/>
<path d="M84 62 Q84 48 98 49 Q108 51 108 62 Q100 54 92 56 Q86 58 84 62Z" fill="#6FC3FF" {s(T2)}/>
{eye(92, 64, .7)}{eye(101, 64, .7)}
<path d="M93 70 Q97 73 100 70" fill="none" {s(T2)}/>
<path d="M106 80 L118 74" stroke="{O}" stroke-width="9" stroke-linecap="round"/><path d="M106 80 L118 74" stroke="#FFD9B8" stroke-width="4.6" stroke-linecap="round"/>
<path d="M-6 92 Q28 84 62 92 T134 90 V134 H-6Z" fill="#57D2E2" {s()}/>
<path d="M112 70 l4 -9 M120 72 l8 -6 M122 80 l9 0" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
<path d="M18 108 q9 -5 18 0 M60 112 q9 -5 18 0 M96 106 q9 -5 18 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 30, 18)
SUBJ["akvadarina-reutov"] = ("мама с каштановым пучком в фиолетовом купальнике и малыш в голубом чепчике",
                             "мама стоит по пояс в тёплой воде и качает малыша на руках, а он хлопает ладошкой по воде, фон розовый")

# 9. Школа плавания «Торпеда» (Ивантеевка) — рыба-парусник мчится торпедой
ICONS["torpeda-ivanteevka"] = W("#D4EEFF", "#1C4FB2", f'''
<g transform="rotate(-12 64 70)">
<path d="M-8 70 H24" stroke="#fff" stroke-width="3.6" stroke-dasharray="3 8" stroke-linecap="round"/>
<path d="M34 70 L12 52 Q20 70 12 88Z" fill="#23357A" {s()}/>
<path d="M44 58 Q46 22 70 20 Q92 22 92 60Z" fill="#E83E8C" {s()}/>
<path d="M56 56 V34 M68 56 V26 M80 56 V32" fill="none" stroke="#A81F5E" stroke-width="2.4" stroke-linecap="round"/>
<circle cx="62" cy="42" r="2.4" fill="#FFD23F"/><circle cx="74" cy="38" r="2.4" fill="#FFD23F"/><circle cx="86" cy="46" r="2.4" fill="#FFD23F"/>
<path d="M58 82 Q64 96 76 84Z" fill="#23357A" {s()}/>
<path d="M30 70 Q60 50 96 62 L126 68 L96 78 Q60 90 30 70Z" fill="#E6EEF8" {s()}/>
<path d="M32 68 Q60 52 96 63 L122 68 Q92 66 60 64 Q44 64 32 68Z" fill="#2B49A8"/>
{eye(90, 70, .8)}
<path d="M95 76 Q99 78 102 75" fill="none" {s(T2)}/>
{BL.format(84, 77)}
</g>
{bub(14, 96, 5)}{bub(28, 108, 3.4)}{bub(8, 112, 3)}
<path d="M104 104 q8 -5 16 0 M84 114 q8 -5 16 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".7"/>
''', 70, 20)
SUBJ["torpeda-ivanteevka"] = ("рыба-парусник с серебристым брюшком, синей спинкой и высоким малиновым плавником-парусом в жёлтый горошек",
                              "мчится торпедой наискосок вверх в тёмно-синей глубине, выставив вперёд нос-копьё, за хвостом — пунктир пузырьков")

if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for i in ids:
        open(os.path.join(OUT, i + ".svg"), "w", encoding="utf-8").write(ICONS[i])
    print("svg:", len(ids))
    for i in ids:
        print(f"{i} — герой: {SUBJ[i][0]} | сцена: {SUBJ[i][1]}")
