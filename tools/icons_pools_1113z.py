"""Иконки робота pools, 2026-11-13 (23 UTC). Каждая придумана и нарисована отдельно (правило абсолютной
уникальности): свой герой, своя сцена, своя компоновка и палитра. Герои проверены по реестру icons-src/subjects.txt
(рыба-клоун, черепашонок, малёк, выдрёнок, лебедёнок, нерпёнок, сазан — в реестре героями не встречались), картинки —
tools/check_unique.py. Иконка ustinov-beregovaya нарисована впрок: место не добавлено (нет точки), svg и строка
реестра не записаны — при добавлении проверить уникальность заново.
Запуск: python3 tools/icons_pools_1113z.py [id …]  → python3 tools/render_icons.py <id…> → python3 tools/check_unique.py <id…>."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, sparkle, O
from icons_pools_1112b import W, bub, T2

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
BL = '<ellipse cx="{}" cy="{}" rx="4.4" ry="2.6" fill="#FF7FA8" opacity=".8"/>'

# 1. «Город волн» (Очаково, 0–14 лет) — рыба-клоун плывёт по улице города, где дома — волны с окошками
ICONS["gorod-voln-ochakovo"] = W("#7C6BD6", "#2A2468", f'''
<path d="M-4 128 V70 Q4 44 22 50 Q34 54 30 68 Q40 60 44 76 V128Z" fill="#2FB7C9" {s()}/>
<path d="M84 128 V60 Q92 30 112 38 Q126 44 120 60 Q132 54 134 70 V128Z" fill="#35A0E8" {s()}/>
<path d="M40 128 V92 Q50 74 64 80 Q74 84 70 94 Q80 90 86 100 V128Z" fill="#59D3C0" {s()}/>
<rect x="6" y="80" width="9" height="10" rx="2" fill="#FFE46B" {s(T2)}/><rect x="22" y="80" width="9" height="10" rx="2" fill="#FFE46B" {s(T2)}/>
<rect x="6" y="100" width="9" height="10" rx="2" fill="#FFE46B" {s(T2)}/><rect x="22" y="100" width="9" height="10" rx="2" fill="#FFF7C9" {s(T2)}/>
<rect x="96" y="70" width="9" height="10" rx="2" fill="#FFE46B" {s(T2)}/><rect x="112" y="70" width="9" height="10" rx="2" fill="#FFF7C9" {s(T2)}/>
<rect x="96" y="92" width="9" height="10" rx="2" fill="#FFE46B" {s(T2)}/><rect x="112" y="92" width="9" height="10" rx="2" fill="#FFE46B" {s(T2)}/>
<rect x="52" y="102" width="8" height="9" rx="2" fill="#FFE46B" {s(T2)}/><rect x="66" y="102" width="8" height="9" rx="2" fill="#FFE46B" {s(T2)}/>
<path d="M92 44 l16 -12 v26Z" fill="#FF8A1F" {s()}/>
<path d="M62 20 q8 -10 18 -2 l-6 10Z M60 68 q10 10 20 2 l-8 -8Z" fill="#FF8A1F" {s(T2)}/>
<ellipse cx="62" cy="45" rx="34" ry="23" fill="#FF8A1F" {s()}/>
<path d="M50 24 Q42 45 50 66 L60 68 Q52 45 60 22Z" fill="#fff" {s(T2)}/>
<path d="M78 26 Q72 45 78 64 L86 60 Q81 45 86 30Z" fill="#fff" {s(T2)}/>
{eye(36, 40, 1.25)}
<path d="M30 52 Q36 58 42 53" fill="none" {s(T2)}/>
{BL.format(42, 49)}
{bub(18, 30, 5)}{bub(10, 18, 3.5)}
{sparkle(108, 16, 4, "#FFE46B")}
''', 50, 30)
SUBJ["gorod-voln-ochakovo"] = ("рыба-клоун в оранжево-белую полоску",
                               "плывёт по вечерней улице города, где вместо домов стоят три волны с горящими жёлтыми окошками, на сине-фиолетовом фоне")

# 2. «БараБулька» (Дзержинский, 0–8 лет, круглая чаша диаметром 4 м) — черепашонок плывёт по кругу, вид сверху
ICONS["barabulka-dzerzhinsky"] = W("#FFE3D2", "#FF8F70", f'''
<circle cx="64" cy="66" r="50" fill="#fff" {s()}/>
<circle cx="64" cy="66" r="42" fill="#3FC8D8" {s(T2)}/>
<path d="M64 36 A30 30 0 1 0 94 66" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-dasharray="1 9" opacity=".95"/>
<circle cx="64" cy="66" r="9" fill="#8FE6EE" opacity=".8"/>
<g transform="rotate(-18 84 50)">
<path d="M70 38 q-10 -8 -14 2 q6 6 14 4Z M98 38 q10 -8 14 2 q-6 6 -14 4Z M72 64 q-8 8 -4 14 q8 -2 10 -10Z M96 64 q8 8 4 14 q-8 -2 -10 -10Z" fill="#7BCB52" {s(T2)}/>
<path d="M84 70 l-4 10 h8Z" fill="#7BCB52" {s(T2)}/>
<circle cx="84" cy="28" r="11" fill="#8FDB62" {s()}/>
{eye(80, 26, .75)}{eye(88, 26, .75)}
<ellipse cx="84" cy="52" rx="17" ry="20" fill="#FFD23F" {s()}/>
<path d="M84 38 l9 7 v12 l-9 7 l-9 -7 v-12Z" fill="#FFB31F" {s(T2)}/>
</g>
{bub(40, 92, 4.5, .85)}{bub(52, 100, 3, .85)}
''', 30, 22)
SUBJ["barabulka-dzerzhinsky"] = ("зелёный черепашонок с жёлтым панцирем, вид сверху",
                                 "плывёт по кругу в маленькой круглой бирюзовой чаше с белым бортиком, оставляя за собой пунктирный след, на кораллово-персиковом фоне")

# 3. Mini Swimmer (Октябрьский, с 2 месяцев до 7 лет) — крошечный малёк рядом с огромной плавательной доской
ICONS["mini-swimmer-oktyabrsky"] = W("#F3E9FF", "#B58CF2", f'''
<path d="M-6 84 Q28 74 62 84 T134 82 V134 H-6Z" fill="#6FD0F2" {s()}/>
<g transform="rotate(-14 70 48)">
<path d="M26 28 H104 Q116 28 116 44 V58 Q116 70 104 70 H26 Q14 70 14 58 V44 Q14 28 26 28Z" fill="#FFD23F" {s()}/>
<ellipse cx="38" cy="49" rx="9" ry="6" fill="#F5A81C" {s(T2)}/><ellipse cx="92" cy="49" rx="9" ry="6" fill="#F5A81C" {s(T2)}/>
<path d="M54 40 h22 M54 58 h22" stroke="#F5A81C" stroke-width="3.4" stroke-linecap="round"/>
</g>
<path d="M82 100 l14 -9 v18Z" fill="#8AA6FF" {s(T2)}/>
<ellipse cx="64" cy="100" rx="20" ry="13" fill="#DCE6FF" {s()}/>
<path d="M56 89 q8 -7 14 0Z" fill="#8AA6FF" {s(T2)}/>
{eye(53, 98, 1.3)}
<path d="M47 106 q4 3 8 0" fill="none" {s(T2)}/>
{BL.format(60, 106)}
{bub(34, 92, 4)}{bub(26, 80, 2.8)}
<path d="M10 116 q9 -5 18 0 M98 118 q9 -5 18 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 70, 20)
SUBJ["mini-swimmer-oktyabrsky"] = ("крошечный серебристо-голубой малёк с огромным глазом",
                                   "плывёт под большущей жёлтой плавательной доской, которая в три раза больше него, на сиреневом фоне")

# 4. Школа плавания Евгения Устинова («Зоркий», Красногорск, 6–17 лет) — зоркий выдрёнок плывёт на спине
ICONS["ustinov-zorky-krasnogorsk"] = W("#DFFBE9", "#27B07A", f'''
<path d="M-6 58 H134 V134 H-6Z" fill="#35B9E6" {s()}/>
<path d="M-4 108 H132" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-dasharray="12 12"/>
<path d="M-4 108 H132" stroke="#FF5A5A" stroke-width="7" stroke-linecap="butt" stroke-dasharray="12 12" stroke-dashoffset="12"/>
<path d="M100 70 Q122 60 126 78 Q116 86 100 84Z" fill="#8A5A3A" {s()}/>
<ellipse cx="66" cy="76" rx="42" ry="15" fill="#A87248" {s()}/>
<ellipse cx="68" cy="74" rx="26" ry="8" fill="#F1D7B5" {s(T2)}/>
<path d="M58 66 q4 -12 12 -4 M84 66 q4 -12 12 -4" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M58 66 q4 -12 12 -4 M84 66 q4 -12 12 -4" fill="none" stroke="#A87248" stroke-width="4.6" stroke-linecap="round"/>
<circle cx="28" cy="62" r="20" fill="#A87248" {s()}/>
<circle cx="14" cy="46" r="5.5" fill="#8A5A3A" {s(T2)}/><circle cx="42" cy="46" r="5.5" fill="#8A5A3A" {s(T2)}/>
<ellipse cx="28" cy="70" rx="10" ry="7" fill="#F1D7B5" {s(T2)}/>
<circle cx="28" cy="66" r="2.6" fill="{O}"/>
<path d="M8 58 H48" stroke="{O}" stroke-width="5" stroke-linecap="round"/>
<circle cx="19" cy="58" r="8.5" fill="#BFF3FF" {s()}/><circle cx="37" cy="58" r="8.5" fill="#BFF3FF" {s()}/>
<circle cx="19" cy="58" r="3.2" fill="{O}"/><circle cx="37" cy="58" r="3.2" fill="{O}"/>
<circle cx="17.6" cy="56.4" r="1.2" fill="#fff"/><circle cx="35.6" cy="56.4" r="1.2" fill="#fff"/>
<path d="M24 73 q4 3 8 0" fill="none" {s(T2)}/>
{sparkle(104, 30, 5)}{sparkle(84, 18, 3)}
''', 60, 14)
SUBJ["ustinov-zorky-krasnogorsk"] = ("коричневый выдрёнок в больших голубых плавательных очках",
                                     "плывёт на спине вдоль красно-белой разделительной дорожки, сложив лапки на животе, на изумрудном фоне")

# 5. Школа плавания Евгения Устинова («Аквастудия на Береговой», от 7 лет) — лебедёнок скользит «стрелочкой» от берега
ICONS["ustinov-beregovaya"] = W("#FFF4C9", "#F2B84B", f'''
<circle cx="24" cy="28" r="13" fill="#FFF7D6" opacity=".9"/>
<path d="M-6 86 Q30 78 64 86 T134 84 V134 H-6Z" fill="#2C9FD9" {s()}/>
<path d="M-6 134 V96 Q12 90 20 106 Q26 122 14 134Z" fill="#F6DFA4" {s()}/>
<path d="M2 110 h8 M4 121 h7" stroke="#D9B96A" stroke-width="3" stroke-linecap="round"/>
<path d="M66 70 Q62 44 76 34" fill="none" stroke="{O}" stroke-width="20" stroke-linecap="round"/>
<path d="M66 70 Q62 44 76 34" fill="none" stroke="#C9CED6" stroke-width="13.6" stroke-linecap="round"/>
<path d="M22 74 Q14 60 26 58 Q40 50 64 58 Q84 66 80 86 Q70 102 46 100 Q24 98 22 74Z" fill="#C9CED6" {s()}/>
<path d="M34 72 Q50 62 64 76 Q52 90 34 84Z" fill="#AEB5C0" {s(T2)}/>
<circle cx="80" cy="32" r="14" fill="#DADFE6" {s()}/>
<path d="M92 28 l15 5 l-15 7Z" fill="#4A4458" {s(T2)}/>
{eye(82, 29, .95)}
{BL.format(78, 38)}
<path d="M72 19 q4 -8 9 -2 q5 -5 7 3" fill="none" {s(T2)}/>
<g transform="rotate(-8 106 80)"><rect x="90" y="72" width="34" height="17" rx="8.5" fill="#FF5A5A" {s()}/><path d="M100 80.5 h14" stroke="#fff" stroke-width="3" stroke-linecap="round"/></g>
<path d="M30 108 q9 -5 18 0 M70 114 q9 -5 18 0 M100 104 q8 -4 16 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 76, 22)
SUBJ["ustinov-beregovaya"] = ("серый пуховый лебедёнок с тёмным клювом и хохолком",
                              "отплывает от песчаного берега и толкает перед собой клювом красную плавательную доску на медово-жёлтом фоне")

# 6. Высшая школа плавания (Гребной канал, Островная ул.) — нерпёнок-выпускник с дипломом
ICONS["vshp-ostrovnaya"] = W("#3D6FD1", "#122457", f'''
<path d="M-6 88 Q28 80 62 88 T134 86 V134 H-6Z" fill="#59C7F2" {s()}/>
<path d="M34 96 Q30 50 64 46 Q98 50 94 96Z" fill="#E9EEF5" {s()}/>
<path d="M36 86 Q20 80 18 66 Q30 66 40 74Z" fill="#CBD5E3" {s()}/>
<ellipse cx="64" cy="76" rx="13" ry="9" fill="#fff" {s(T2)}/>
<ellipse cx="64" cy="71" rx="4.2" ry="3" fill="{O}"/>
<path d="M58 78 q6 5 12 0" fill="none" {s(T2)}/>
<path d="M50 76 h-12 M51 80 l-11 4 M78 76 h12 M77 80 l11 4" stroke="{O}" stroke-width="1.8" stroke-linecap="round"/>
{eye(52, 64, 1.1)}{eye(76, 64, 1.1)}
{BL.format(44, 72)}{BL.format(84, 72)}
<path d="M30 38 L64 24 L98 38 L64 52Z" fill="#2B2540" {s()}/>
<path d="M46 45 V54 Q64 62 82 54 V45" fill="#2B2540" {s()}/>
<path d="M64 38 L96 42 V60" fill="none" stroke="#FFD23F" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M92 58 h8 l-2 12 h-4Z" fill="#FFD23F" {s(T2)}/>
<g transform="rotate(-24 104 92)"><rect x="88" y="84" width="34" height="14" rx="7" fill="#FFF7E0" {s()}/><rect x="102" y="82" width="7" height="18" rx="2" fill="#FF5A6E" {s(T2)}/></g>
<path d="M12 112 q9 -5 18 0 M54 116 q9 -5 18 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
{sparkle(20, 30, 4)}{sparkle(112, 22, 3)}
''', 44, 24)
SUBJ["vshp-ostrovnaya"] = ("белый усатый нерпёнок в чёрной шапочке выпускника с золотой кисточкой",
                           "высунулся из воды по грудь и держит под ластом свиток-диплом с красной лентой на тёмно-синем фоне")

# 7. «Дельфин» (СК «Арена Лыткарино», с 6 месяцев) — сазан прыгает сквозь обруч «как дельфин»
ICONS["delfin-lytkarino"] = W("#E4FFF6", "#5FD6B4", f'''
<path d="M-6 98 Q28 90 62 98 T134 96 V134 H-6Z" fill="#2F8FE0" {s()}/>
<ellipse cx="64" cy="58" rx="13" ry="40" fill="none" stroke="{O}" stroke-width="11"/>
<ellipse cx="64" cy="58" rx="13" ry="40" fill="none" stroke="#FF5A5A" stroke-width="5.5"/>
<path d="M56 20 l14 3 M52 40 l8 2 M54 78 l10 2" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<g transform="rotate(-20 64 56)">
<path d="M22 56 L4 42 Q10 56 4 72Z" fill="#E08A1E" {s()}/>
<path d="M22 56 Q40 30 82 36 Q112 42 118 58 Q108 76 80 78 Q40 80 22 56Z" fill="#F2B63A" {s()}/>
<path d="M56 34 Q70 20 88 36Z" fill="#E08A1E" {s(T2)}/>
<path d="M60 78 q6 12 16 2Z" fill="#E08A1E" {s(T2)}/>
<path d="M44 50 q6 6 0 12 M58 46 q7 10 0 20 M72 44 q7 12 0 24" fill="none" stroke="#C97A12" stroke-width="2.6" stroke-linecap="round"/>
{eye(100, 52, 1.15)}
<path d="M108 64 q5 2 8 -2" fill="none" {s(T2)}/>
<path d="M112 66 q4 6 0 10" fill="none" stroke="{O}" stroke-width="2.2" stroke-linecap="round"/>
{BL.format(94, 62)}
</g>
<path d="M22 100 q4 -10 8 0 q0 6 -4 6 q-4 0 -4 -6Z M36 92 q3 -8 6 0 q0 5 -3 5 q-3 0 -3 -5Z" fill="#fff" {s(T2)}/>
<path d="M84 116 q9 -5 18 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 30, 20)
SUBJ["delfin-lytkarino"] = ("золотистый усатый сазан с крупной чешуёй",
                            "выпрыгивает из бассейна дугой и пролетает сквозь красно-белый обруч, как дельфин на представлении, на мятном фоне")

if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for i in ids:
        open(os.path.join(OUT, i + ".svg"), "w", encoding="utf-8").write(ICONS[i])
    print("svg:", len(ids))
    for i in ids:
        print(f"{i} — герой: {SUBJ[i][0]} | сцена: {SUBJ[i][1]}")
