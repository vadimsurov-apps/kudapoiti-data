"""Иконки робота pools, 2026-11-13 (15 UTC). Каждая придумана и нарисована отдельно (правило абсолютной
уникальности): свой герой, своя сцена, своя компоновка и палитра. Герои проверены по реестру icons-src/subjects.txt,
картинки — tools/check_unique.py.
Запуск: python3 tools/icons_pools_1113n.py [id …]  → python3 tools/render_icons.py <id…> → python3 tools/check_unique.py <id…>."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, sparkle, O
from icons_pools_1112b import W, bub, T2

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
BL = '<ellipse cx="{}" cy="{}" rx="4.4" ry="2.6" fill="#FF7FA8" opacity=".8"/>'

# 1. Школа плавания № 1, «Коралл» (25 м, 5 дорожек) — плотвичка берёт разделитель дорожек, как барьер
ICONS["ss1-korall-krasnoselsky"] = W("#DDF3FF", "#3E7BE0", f'''
<path d="M-6 84 Q30 76 64 84 T134 82 V134 H-6Z" fill="#1F5FC0" {s()}/>
<path d="M-6 96 H134" stroke="{O}" stroke-width="13" stroke-linecap="round"/>
<path d="M-6 96 H134" stroke="#FF4F4F" stroke-width="9" stroke-dasharray="14 14"/>
<path d="M-6 96 H134" stroke="#fff" stroke-width="9" stroke-dasharray="14 14" stroke-dashoffset="14"/>
<path d="M22 86 Q34 34 70 26 Q98 22 108 44" fill="none" stroke="#fff" stroke-width="3.4" stroke-dasharray="2 9" stroke-linecap="round" opacity=".9"/>
<g transform="rotate(-24 70 46)">
<path d="M40 46 L18 30 Q24 46 18 62Z" fill="#FF5A4D" {s()}/>
<path d="M62 28 Q72 14 86 26Z" fill="#FF5A4D" {s()}/>
<path d="M64 62 Q70 74 80 62Z" fill="#FF5A4D" {s()}/>
<ellipse cx="70" cy="46" rx="34" ry="19" fill="#DCE6F2" {s()}/>
<path d="M44 40 Q70 30 100 42" fill="none" stroke="#9FB4CC" stroke-width="6" stroke-linecap="round" opacity=".7"/>
<path d="M58 44 q5 6 0 12 M68 44 q5 6 0 12 M48 46 q4 5 0 9" fill="none" stroke="#9FB4CC" stroke-width="2.2" stroke-linecap="round"/>
<circle cx="90" cy="42" r="6.4" fill="#fff" {s(T2)}/>{eye(91, 42, .8)}
<path d="M96 52 Q100 55 103 50" fill="none" {s(T2)}/>
{BL.format(86, 53)}
</g>
{bub(26, 70, 4)}{bub(110, 68, 3)}
<path d="M14 78 l-6 -10 M24 74 l0 -11 M34 78 l6 -10" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
''', 34, 20)
SUBJ["ss1-korall-krasnoselsky"] = ("серебристая плотвичка с красными плавниками",
                                   "перепрыгивает дугой через красно-белый разделитель дорожек, как бегун через барьер")

# 2. Школа плавания № 1, «Вешняки» — летучая мышка в очках висит на трамплине перед прыжком
ICONS["ss1-veshnyaki-kosinskaya"] = W("#F1E4FF", "#7A5BD0", f'''
<path d="M-6 100 Q28 92 62 100 T134 98 V134 H-6Z" fill="#39C6D8" {s()}/>
<path d="M20 112 q8 -5 16 0 M70 114 q8 -5 16 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<rect x="-8" y="22" width="92" height="11" rx="5" fill="#FFC94A" {s()}/>
<rect x="-8" y="33" width="26" height="80" fill="#B9A6E8" {s()}/>
<path d="M-8 52 H18 M-8 72 H18 M-8 92 H18" {s(T2)}/>
<path d="M64 33 V40 M76 33 V40" {s()}/>
<path d="M70 52 L36 44 Q40 58 34 66 Q46 62 50 72 Q56 64 64 70Z" fill="#5A4A7A" {s()}/>
<path d="M70 52 L104 44 Q100 58 106 66 Q94 62 90 72 Q84 64 76 70Z" fill="#5A4A7A" {s()}/>
<ellipse cx="70" cy="56" rx="13" ry="17" fill="#7B689E" {s()}/>
<circle cx="70" cy="78" r="15" fill="#7B689E" {s()}/>
<path d="M58 88 L54 100 L66 92Z M82 88 L86 100 L74 92Z" fill="#7B689E" {s()}/>
<rect x="55" y="72" width="30" height="12" rx="6" fill="#FF6FA5" {s(T2)}/>
<circle cx="63" cy="78" r="5" fill="#CFF4FF" {s(T2)}/><circle cx="77" cy="78" r="5" fill="#CFF4FF" {s(T2)}/>
<circle cx="63" cy="78" r="2" fill="{O}"/><circle cx="77" cy="78" r="2" fill="{O}"/>
<path d="M66 68 Q70 65 74 68" fill="none" {s(T2)}/>
{sparkle(104, 24, 6)}{sparkle(112, 84, 4)}
''', 70, 16)
SUBJ["ss1-veshnyaki-kosinskaya"] = ("сиреневая летучая мышка в розовых плавательных очках",
                                    "висит вниз головой на краю жёлтого трамплина над водой и собирается нырнуть")

# 3. Школа плавания № 1, «Зоркий» (Красногорск) — верблюжонок, «корабль пустыни», пробует воду
ICONS["ss1-zorky-krasnogorsk"] = W("#FFF9D9", "#FFC64A", f'''
<path d="M-6 88 Q28 80 62 88 T134 86 V134 H-6Z" fill="#38B7EA" {s()}/>
<path d="M46 90 V64 M60 92 V66 M84 92 V66" stroke="{O}" stroke-width="12" stroke-linecap="round"/>
<path d="M46 90 V64 M60 92 V66 M84 92 V66" stroke="#E9A25A" stroke-width="6.6" stroke-linecap="round"/>
<path d="M96 66 L112 78" stroke="{O}" stroke-width="12" stroke-linecap="round"/>
<path d="M96 66 L112 78" stroke="#E9A25A" stroke-width="6.6" stroke-linecap="round"/>
<path d="M36 68 Q32 46 52 44 Q62 22 76 44 Q98 44 98 62 Q96 76 76 76 H50 Q38 76 36 68Z" fill="#F2B56B" {s()}/>
<path d="M40 60 Q30 40 30 28" fill="none" stroke="{O}" stroke-width="15" stroke-linecap="round"/>
<path d="M40 60 Q30 40 30 28" fill="none" stroke="#F2B56B" stroke-width="9" stroke-linecap="round"/>
<ellipse cx="26" cy="26" rx="14" ry="11" fill="#F2B56B" {s()}/>
<path d="M32 16 l4 -8 l4 9Z" fill="#F2B56B" {s(T2)}/>
{eye(24, 23, .75)}
<path d="M14 30 Q18 34 23 31" fill="none" {s(T2)}/>
{BL.format(30, 31)}
<ellipse cx="64" cy="38" rx="17" ry="8" fill="none" stroke="{O}" stroke-width="11"/>
<ellipse cx="64" cy="38" rx="17" ry="8" fill="none" stroke="#FF5A6E" stroke-width="6"/>
<ellipse cx="64" cy="38" rx="17" ry="8" fill="none" stroke="#fff" stroke-width="6" stroke-dasharray="9 18"/>
<path d="M-6 96 Q28 88 62 96 T134 94 V134 H-6Z" fill="#38B7EA"/>
<path d="M-6 96 Q28 88 62 96 T134 94" fill="none" {s()}/>
<path d="M104 84 q8 -6 16 0 M100 92 q12 -8 24 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M98 62 q8 2 8 10" fill="none" {s(T2)}/>
''', 60, 18)
SUBJ["ss1-zorky-krasnogorsk"] = ("рыжий верблюжонок с красно-белым спасательным кругом на горбу",
                                 "стоит по колено в бассейне и осторожно пробует воду вытянутым копытцем, от копытца идут круги")

# 4. «Крабибу», Раменское (индивидуально, 0–7 лет) — малыш-юнга лежит на воде звёздочкой, вид сверху
ICONS["krabibu-ramenskoe"] = W("#B8F4EA", "#19B5C2", f'''
<circle cx="64" cy="66" r="54" fill="none" stroke="#fff" stroke-width="3" opacity=".55"/>
<circle cx="64" cy="66" r="42" fill="none" stroke="#fff" stroke-width="3" opacity=".75"/>
<path d="M64 70 L30 46 M64 70 L98 46 M60 80 L42 108 M68 80 L86 108" stroke="{O}" stroke-width="15" stroke-linecap="round"/>
<path d="M64 70 L30 46 M64 70 L98 46 M60 80 L42 108 M68 80 L86 108" stroke="#FFD2AE" stroke-width="9" stroke-linecap="round"/>
<rect x="49" y="60" width="30" height="30" rx="13" fill="#fff" {s()}/>
<path d="M50 68 H78 M49 76 H79 M51 84 H77" stroke="#2D6CDF" stroke-width="4"/>
<rect x="49" y="60" width="30" height="30" rx="13" fill="none" {s()}/>
<circle cx="64" cy="44" r="17" fill="#FFD2AE" {s()}/>
<path d="M47 40 Q64 18 81 40 Q64 34 47 40Z" fill="#fff" {s()}/>
<path d="M48 40 Q64 34 80 40" fill="none" stroke="#2D6CDF" stroke-width="4"/>
<path d="M80 38 q10 -2 12 8 M80 38 q12 2 8 14" fill="none" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>
<circle cx="64" cy="27" r="3" fill="#FF5A4D" {s(T2)}/>
{eye(58, 46, .75)}{eye(70, 46, .75)}
<path d="M60 53 Q64 57 68 53" fill="none" {s(T2)}/>
{BL.format(52, 51)}{BL.format(76, 51)}
{sparkle(20, 84, 5)}{sparkle(108, 80, 4)}
''', 50, 50)
SUBJ["krabibu-ramenskoe"] = ("малыш-юнга в тельняшке и белой бескозырке с ленточками",
                             "лежит на спине «звёздочкой» на бирюзовой воде, вид сверху, вокруг него расходятся белые круги")

# 5. «Аквазаврик», Одинцово — спинозаврик плывёт, гребень торчит над водой, как парус
ICONS["akvazavrik-odintsovo"] = W("#F4FFD9", "#58C98A", f'''
<path d="M40 74 Q46 22 70 20 Q92 22 98 74Z" fill="#FFD23F" {s()}/>
<path d="M52 72 Q56 36 70 22 M70 72 V22 M88 72 Q84 36 70 22" fill="none" stroke="#FF7A3D" stroke-width="5" stroke-linecap="round"/>
<path d="M40 74 Q46 22 70 20 Q92 22 98 74" fill="none" {s()}/>
<path d="M98 80 Q118 76 124 60 Q112 62 104 70Z" fill="#FF8A3D" {s()}/>
<ellipse cx="68" cy="84" rx="38" ry="16" fill="#FF8A3D" {s()}/>
<path d="M36 82 Q20 78 14 64 Q10 52 22 48 Q36 46 40 60 Q42 70 48 76Z" fill="#FF8A3D" {s()}/>
<path d="M10 58 Q2 60 4 66 Q10 70 18 66Z" fill="#FF8A3D" {s()}/>
{eye(24, 56, .8)}
<path d="M8 66 Q14 70 20 67" fill="none" {s(T2)}/>
{BL.format(30, 64)}
<path d="M-6 90 Q26 80 60 90 T134 88 V134 H-6Z" fill="#17A6B8" {s()}/>
<path d="M18 104 q10 -6 20 0 M66 108 q10 -6 20 0 M96 100 q8 -5 16 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
{bub(112, 40, 5)}{bub(104, 26, 3)}
''', 28, 24)
SUBJ["akvazavrik-odintsovo"] = ("оранжевый спинозаврик с жёлто-полосатым гребнем на спине",
                                "плывёт по бассейну: над водой только голова и высокий гребень, похожий на парус лодочки")

# 6. Real Swim, Одинцово — девочка ныряет на дно за тонущим кольцом, вид под водой
ICONS["real-swim-odintsovo"] = W("#7FE3F0", "#0E4FA8", f'''
<path d="M30 -6 L50 134 M64 -6 L78 134 M96 -6 L104 134" stroke="#fff" stroke-width="12" opacity=".14"/>
<path d="M-6 118 Q40 108 70 116 T134 112 V134 H-6Z" fill="#F3D9A0" {s()}/>
<ellipse cx="92" cy="110" rx="13" ry="5.5" fill="none" stroke="{O}" stroke-width="9"/>
<ellipse cx="92" cy="110" rx="13" ry="5.5" fill="none" stroke="#FF4F5E" stroke-width="5"/>
<ellipse cx="30" cy="116" rx="9" ry="4" fill="none" stroke="{O}" stroke-width="7"/>
<ellipse cx="30" cy="116" rx="9" ry="4" fill="none" stroke="#FFD23F" stroke-width="3.6"/>
<g transform="rotate(38 60 60)">
<path d="M50 30 L44 8 M70 30 L78 8" stroke="{O}" stroke-width="13" stroke-linecap="round"/>
<path d="M50 30 L44 8 M70 30 L78 8" stroke="#FFD2AE" stroke-width="7.6" stroke-linecap="round"/>
<path d="M54 76 L48 100 M68 76 L74 100" stroke="{O}" stroke-width="12" stroke-linecap="round"/>
<path d="M54 76 L48 100 M68 76 L74 100" stroke="#FFD2AE" stroke-width="7" stroke-linecap="round"/>
<rect x="46" y="26" width="30" height="36" rx="13" fill="#35C46A" {s()}/>
<path d="M48 40 H74" stroke="#fff" stroke-width="3.4"/>
<path d="M46 72 Q30 60 30 44 M76 72 Q92 60 92 44" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M46 72 Q30 60 30 44 M76 72 Q92 60 92 44" fill="none" stroke="#8A4B2A" stroke-width="5" stroke-linecap="round"/>
<circle cx="30" cy="42" r="4" fill="#FF6FA5" {s(T2)}/><circle cx="92" cy="42" r="4" fill="#FF6FA5" {s(T2)}/>
<circle cx="61" cy="76" r="17" fill="#FFD2AE" {s()}/>
<path d="M44 74 Q46 58 61 58 Q76 58 78 74 Q62 66 44 74Z" fill="#8A4B2A" {s()}/>
{eye(55, 80, .75)}{eye(67, 80, .75)}
<ellipse cx="61" cy="88" rx="3" ry="3.6" fill="{O}"/>
</g>
{bub(102, 52, 5)}{bub(110, 36, 3.4)}{bub(98, 70, 2.6)}
''', 40, 10)
SUBJ["real-swim-odintsovo"] = ("девочка с двумя каштановыми косичками в зелёном купальнике",
                               "ныряет под водой вниз головой ко дну бассейна за красным тонущим кольцом, косички тянутся следом")

# 7. «Аква Smart», Электросталь (раннее плавание 2 мес – 5 лет) — умный белёк в шапочке выпускника
ICONS["akva-smart-elektrostal"] = W("#FFEAF4", "#C58BEA", f'''
<path d="M-6 92 Q28 84 62 92 T134 90 V134 H-6Z" fill="#5ED3E6" {s()}/>
<rect x="14" y="80" width="100" height="20" rx="10" fill="#FF6FA5" {s()}/>
<path d="M30 86 H98" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".7"/>
<path d="M92 84 Q112 78 118 62 Q104 62 96 72Z" fill="#fff" {s()}/>
<path d="M30 84 Q30 54 60 52 Q92 52 98 84Z" fill="#fff" {s()}/>
<circle cx="44" cy="58" r="21" fill="#fff" {s()}/>
<path d="M40 82 Q32 92 24 88 M70 84 Q72 94 82 92" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M40 82 Q32 92 24 88 M70 84 Q72 94 82 92" fill="none" stroke="#fff" stroke-width="4.6" stroke-linecap="round"/>
{eye(36, 58, .9)}{eye(52, 58, .9)}
<ellipse cx="44" cy="66" rx="3.4" ry="2.6" fill="{O}"/>
<path d="M44 68 Q40 73 36 70 M44 68 Q48 73 52 70" fill="none" {s(T2)}/>
{BL.format(28, 66)}{BL.format(60, 66)}
<path d="M20 38 L44 28 L68 38 L44 48Z" fill="#3B3F8F" {s()}/>
<path d="M32 43 V50 Q44 56 56 50 V43" fill="#3B3F8F" {s()}/>
<path d="M66 38 V52" {s(T2)}/><circle cx="66" cy="55" r="3.4" fill="#FFD23F" {s(T2)}/>
<circle cx="44" cy="15" r="9" fill="#FFD23F" {s()}/>
<path d="M36 13 Q44 9 52 13" fill="none" stroke="#FF8A3D" stroke-width="3" stroke-linecap="round"/>
<path d="M-6 100 Q28 92 62 100 T134 98 V134 H-6Z" fill="#5ED3E6"/>
<path d="M-6 100 Q28 92 62 100 T134 98" fill="none" {s()}/>
{sparkle(100, 34, 6)}{sparkle(88, 18, 4)}
''', 30, 22)
SUBJ["akva-smart-elektrostal"] = ("пушистый белёк-тюленёнок в синей шапочке выпускника с кисточкой",
                                  "лежит на розовой плавательной доске и держит над головой жёлтый мячик")

# 8. SwimRocket, Лужники (50 м) — пловец стартует с тумбы, как ракета
ICONS["swimrocket-luzhniki"] = W("#3C4FB5", "#141B52", f'''
{sparkle(24, 22, 5)}{sparkle(106, 30, 4)}{sparkle(62, 12, 3)}
<path d="M-6 104 Q28 96 62 104 T134 102 V134 H-6Z" fill="#28B6E8" {s()}/>
<path d="M-8 78 H30 L36 112 H-8Z" fill="#E8EDF7" {s()}/>
<path d="M-8 78 H30" stroke="#FF5A4D" stroke-width="6" stroke-linecap="round"/>
<path d="M-8 78 H30" fill="none" {s()}/>
<g transform="rotate(-20 68 56)">
<path d="M30 56 L2 44 Q12 56 2 70Z" fill="#FFD23F" {s()}/>
<path d="M30 56 L10 50 Q16 56 10 63Z" fill="#FF6A3D"/>
<path d="M30 52 L48 52 M30 62 L48 62" stroke="{O}" stroke-width="12" stroke-linecap="round"/>
<path d="M30 52 L48 52 M30 62 L48 62" stroke="#FFD2AE" stroke-width="7" stroke-linecap="round"/>
<rect x="42" y="44" width="34" height="26" rx="12" fill="#FFD2AE" {s()}/>
<path d="M42 58 Q42 70 54 70 H58 V46 H54 Q42 46 42 58Z" fill="#FF4F5E" {s()}/>
<path d="M78 50 L112 48 M78 64 L112 54" stroke="{O}" stroke-width="11" stroke-linecap="round"/>
<path d="M78 50 L112 48 M78 64 L112 54" stroke="#FFD2AE" stroke-width="6.4" stroke-linecap="round"/>
<circle cx="88" cy="56" r="15" fill="#FFD2AE" {s()}/>
<path d="M82 42 Q100 36 103 56 Q94 50 82 42Z" fill="#DDE3EE" {s()}/>
<path d="M76 46 Q88 36 102 50" fill="#DDE3EE" {s()}/>
{sparkle(90, 45, 3.4, "#FFD23F")}
{eye(93, 59, .7)}
<path d="M90 66 Q95 68 98 64" fill="none" {s(T2)}/>
</g>
<path d="M92 112 q8 -5 16 0 M56 116 q8 -5 16 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 70, 20)
SUBJ["swimrocket-luzhniki"] = ("мальчик-пловец в серебряной шапочке со звездой и красных плавках",
                               "летит «ласточкой» со стартовой тумбы над ночным бассейном, за пятками — огненный хвост, как у ракеты")

# 9. «Пять утят», Малая Филёвская — пять капитошек прыгают в воду друг за другом
_K = [("#FF5A6E", 20, 30), ("#FFB02E", 40, 22), ("#35C46A", 61, 24), ("#3B8CFF", 82, 36), ("#A66BF0", 100, 58)]
ICONS["pyat-utyat-filevskaya"] = W("#FFFDE4", "#FFD98A", f'''
<path d="M-6 96 Q28 88 62 96 T134 94 V134 H-6Z" fill="#35B9E6" {s()}/>
<path d="M-8 62 H50 V134 H-8Z" fill="#E6F4FB" {s()}/>
<path d="M-8 62 H50" stroke="#7CCBEA" stroke-width="7"/>
<path d="M-8 62 H50 V134" fill="none" {s()}/>
<path d="M0 82 H40 M0 100 H40 M20 62 V134" stroke="#BFE3F2" stroke-width="2.4"/>
<path d="M14 50 Q40 2 78 20 Q104 34 106 70" fill="none" stroke="#fff" stroke-width="3.4" stroke-dasharray="2 9" stroke-linecap="round"/>
''' + "".join(
    f'<g transform="rotate({r} {x} {y})"><path d="M{x} {y - 15} Q{x + 14} {y + 2} {x} {y + 11} Q{x - 14} {y + 2} {x} {y - 15}Z" fill="{c}" {s()}/>'
    f'{eye(x - 4, y + 1, .5)}{eye(x + 4, y + 1, .5)}<path d="M{x - 3} {y + 6} Q{x} {y + 8.5} {x + 3} {y + 6}" fill="none" {s(T2)}/></g>'
    for (c, x, y), r in zip(_K, (0, 14, 40, 80, 150))) + f'''
<path d="M92 92 l-8 -12 M106 90 l0 -14 M120 92 l8 -12" stroke="#fff" stroke-width="3.6" stroke-linecap="round"/>
<path d="M88 104 q18 -12 36 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 36, 26)
SUBJ["pyat-utyat-filevskaya"] = ("пять разноцветных капитошек — капелек с глазками (красная, оранжевая, зелёная, синяя, фиолетовая)",
                                 "прыгают цепочкой с кафельного бортика в бассейн, последняя уже ныряет с брызгами")

# 10. «Морской львёнок», Раменское — львёнок в надувном круге гребёт лапами
ICONS["morskoy-lvenok-ramenskoe"] = W("#E3FBFF", "#56B4F0", f'''
<path d="M-6 70 Q28 62 62 70 T134 68 V134 H-6Z" fill="#2D8EE0" {s()}/>
<path d="M64 12 l8 12 l12 -8 l0 14 l14 2 l-8 12 l10 10 l-14 4 l2 14 l-12 -6 l-12 12 l-12 -12 l-12 6 l2 -14 l-14 -4 l10 -10 l-8 -12 l14 -2 l0 -14 l12 8Z" fill="#E8752A" {s()}/>
<circle cx="64" cy="48" r="23" fill="#FFC45A" {s()}/>
<circle cx="46" cy="28" r="6" fill="#FFC45A" {s()}/><circle cx="82" cy="28" r="6" fill="#FFC45A" {s()}/>
{eye(55, 46, .9)}{eye(73, 46, .9)}
<path d="M60 54 h8 l-4 5Z" fill="{O}"/>
<path d="M64 59 Q59 65 54 61 M64 59 Q69 65 74 61" fill="none" {s(T2)}/>
{BL.format(46, 55)}{BL.format(82, 55)}
<ellipse cx="64" cy="88" rx="38" ry="15" fill="none" stroke="{O}" stroke-width="20"/>
<ellipse cx="64" cy="88" rx="38" ry="15" fill="none" stroke="#fff" stroke-width="14"/>
<ellipse cx="64" cy="88" rx="38" ry="15" fill="none" stroke="#19B37A" stroke-width="14" stroke-dasharray="20 20"/>
<path d="M22 82 Q8 76 6 88 M106 82 Q120 76 122 88" fill="none" stroke="{O}" stroke-width="12" stroke-linecap="round"/>
<path d="M22 82 Q8 76 6 88 M106 82 Q120 76 122 88" fill="none" stroke="#FFC45A" stroke-width="7" stroke-linecap="round"/>
<path d="M2 100 l-4 -8 M12 104 l0 -9 M116 104 l0 -9 M126 100 l4 -8" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
<path d="M40 116 q10 -6 20 0 M72 118 q10 -6 20 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 64, 20)
SUBJ["morskoy-lvenok-ramenskoe"] = ("львёнок с рыжей лохматой гривой",
                                    "сидит в зелёно-белом надувном круге посреди синей воды и гребёт обеими лапами, поднимая брызги")

if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for i in ids:
        open(os.path.join(OUT, i + ".svg"), "w", encoding="utf-8").write(ICONS[i])
    print("svg:", len(ids))
    for i in ids:
        print(f"{i} — герой: {SUBJ[i][0]} | сцена: {SUBJ[i][1]}")
