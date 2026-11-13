"""Иконки робота pools, 2026-11-13 (05 UTC). Каждая придумана и нарисована отдельно (правило абсолютной
уникальности): свой герой, своя сцена, своя компоновка и палитра. Герои проверены по реестру icons-src/subjects.txt
(ни одного такого героя раньше не было), картинки — tools/check_unique.py.
Запуск: python3 tools/icons_pools_1113e.py [id …]  → python3 tools/render_icons.py <id…> → python3 tools/check_unique.py <id…>."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, sparkle, O
from icons_pools_1112b import W, bub, T2

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
T3 = 'stroke-width="2"'

# 1. OctoSkills, Староволынская — раннее плавание: круглая рыбка-дискус проплывает сквозь обруч для ныряния
ICONS["octoskills-starovolynskaya"] = W("#F6ECFF", "#7A55D8", f'''
<path d="M92 18 Q78 18 78 64 Q78 110 92 110" fill="none" stroke="{O}" stroke-width="11" stroke-linecap="round"/>
<path d="M92 18 Q78 18 78 64 Q78 110 92 110" fill="none" stroke="#FFD23F" stroke-width="6" stroke-linecap="round"/>
<path d="M30 64 L8 46 Q14 64 8 84Z" fill="#35C9C0" {s()}/>
<path d="M40 38 Q62 14 88 40Z" fill="#35C9C0" {s()}/>
<path d="M40 90 Q62 114 88 88Z" fill="#35C9C0" {s()}/>
<circle cx="62" cy="64" r="33" fill="#FF8A3D" {s()}/>
<path d="M46 38 Q52 64 44 90 M60 32 Q68 64 58 96 M76 36 Q82 62 74 92" fill="none" stroke="#35C9C0" stroke-width="5" stroke-linecap="round"/>
<path d="M56 66 Q46 74 54 82" fill="#FFB36B" {s(T2)}/>
{eye(80, 56, 1.3)}
<path d="M86 70 Q90 74 94 68" fill="none" {s('stroke-width="2.6"')}/>
<ellipse cx="76" cy="70" rx="4.6" ry="2.8" fill="#FF5E86" opacity=".8"/>
<path d="M92 18 Q106 18 106 64 Q106 110 92 110" fill="none" stroke="{O}" stroke-width="11" stroke-linecap="round"/>
<path d="M92 18 Q106 18 106 64 Q106 110 92 110" fill="none" stroke="#FFD23F" stroke-width="6" stroke-linecap="round"/>
<path d="M99 30 L103 40 M103 88 L99 98" stroke="#F0483E" stroke-width="6"/>
{bub(20, 28, 5)}{bub(30, 16, 3.2)}{bub(116, 60, 4)}
''', 30, 22)
SUBJ["octoskills-starovolynskaya"] = ("круглая оранжевая рыбка-дискус в бирюзовую полоску",
                                      "проплывает сквозь жёлтый обруч для ныряния, стоящий на дне детского бассейна")

# 2. «Акулята», Красногорск — индивидуальные занятия от 2 месяцев до 7 лет: плавки с акульим плавником прыгают в воду
ICONS["akulyata-krasnogorsk"] = W("#FFF9D6", "#FFB52E", f'''
<path d="M-6 94 Q10 86 26 94 T58 94 T90 94 T134 94 V134 H-6Z" fill="#3DB8EE" {s('stroke-width="2.6"')}/>
<path d="M16 110 Q26 105 36 110 M84 114 Q94 109 104 114" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
<path d="M38 10 V22 M64 4 V18 M90 10 V22" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".9"/>
<path d="M82 34 L96 10 Q104 26 100 40Z" fill="#8FA3B8" {s()}/>
<path d="M30 34 H98 L106 80 Q88 86 72 80 L64 60 L56 80 Q40 86 22 80Z" fill="#F0483E" {s()}/>
<path d="M30 34 H98 L99.500 43 H28.500Z" fill="#FFFFFF" {s(T2)}/>
<path d="M58 38.500 Q64 46 70 38.500" fill="none" {s(T3)}/>
<path d="M26 72 Q40 77 54 73 M74 73 Q88 77 102 72" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
{eye(50, 56, 1.25)}{eye(78, 56, 1.25)}
<path d="M58 64 Q64 70 70 64" fill="#fff" {s('stroke-width="2.4"')}/>
<ellipse cx="40" cy="64" rx="4.6" ry="2.8" fill="#FFD0C8" opacity=".9"/><ellipse cx="88" cy="64" rx="4.6" ry="2.8" fill="#FFD0C8" opacity=".9"/>
<path d="M14 84 Q10 74 16 68 Q22 76 14 84Z M114 84 Q118 74 112 68 Q106 76 114 84Z M64 92 Q60 84 64 78 Q68 84 64 92Z" fill="#BDEBFF" {s(T3)}/>
''', 50, 14)
SUBJ["akulyata-krasnogorsk"] = ("красные детские плавки с белой резинкой и серым акульим плавничком на боку",
                                "весело прыгают «бомбочкой» в тёплую воду, во все стороны летят капли")

# 3. Mighty Sharks, Митино — спортивное плавание в бассейне 25 м: осётр касается бортика на финише
ICONS["mighty-sharks-mitino"] = W("#DCEBFF", "#1E3C8C", f'''
<path d="M108 -6 H134 V134 H108Z" fill="#F4FAFF" {s(T2)}/>
<path d="M108 24 H134 M108 54 H134 M108 84 H134 M108 114 H134 M121 -6 V134" stroke="#B9D3EA" stroke-width="2"/>
<path d="M114 50 H128 M121 50 V82" stroke="#1E3C8C" stroke-width="6" stroke-linecap="round"/>
<path d="M22 62 L2 34 Q12 58 6 70 Q2 82 12 84Z" fill="#5E7F99" {s()}/>
<path d="M16 66 Q40 44 74 48 Q92 50 108 44 Q100 58 92 70 Q70 86 40 82 Q24 80 16 66Z" fill="#7C9DB5" {s()}/>
<path d="M22 70 Q48 82 84 72 Q70 86 40 82 Q28 80 22 70Z" fill="#EAF3FA"/>
<path d="M30 62 l6 -5 l6 5 l-6 5Z M44 60 l6 -5 l6 5 l-6 5Z M58 59 l6 -5 l6 5 l-6 5Z" fill="#FFE46B" {s(T3)}/>
<path d="M44 48 Q52 34 62 46Z" fill="#5E7F99" {s(T2)}/>
<path d="M52 82 Q54 94 64 82Z" fill="#5E7F99" {s(T2)}/>
<path d="M88 66 Q88 76 84 80 M94 62 Q96 72 92 78" fill="none" {s(T2)}/>
<path d="M70 50 Q84 44 94 52" fill="none" stroke="{O}" stroke-width="3"/>
<circle cx="82" cy="56" r="8" fill="#FF5E3A" {s(T2)}/><circle cx="82" cy="56" r="4.2" fill="#fff"/><circle cx="83" cy="56" r="2.2" fill="{O}"/>
<path d="M8 100 H96 M8 22 H96" stroke="#fff" stroke-width="3" stroke-dasharray="2 9" stroke-linecap="round" opacity=".55"/>
{sparkle(104, 32, 7, "#FFE46B")}{bub(30, 36, 4)}{bub(20, 106, 3.4)}
''', 24, 22)
SUBJ["mighty-sharks-mitino"] = ("серо-голубой осётр с жёлтыми ромбами-жучками на боку, в красных плавательных очках",
                                "на финише касается острым носом кафельного бортика с тёмной разметкой 25-метровой дорожки")

# 4. Mighty Sharks, Новогорск — лещ делает кувырок-разворот
ICONS["mighty-sharks-novogorsk"] = W("#DAFFF6", "#0F9E8E", f'''
<path d="M64 14 A50 50 0 1 1 20 40" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-dasharray="3 11" opacity=".8"/>
<path d="M20 40 L18 22 M20 40 L36 34" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".9"/>
<g transform="rotate(-58 64 66)">
<path d="M30 66 L8 46 Q16 66 8 88Z" fill="#B5762A" {s()}/>
<path d="M28 66 Q52 22 88 44 Q108 56 104 68 Q98 92 70 96 Q44 98 28 66Z" fill="#E2AE4A" {s()}/>
<path d="M50 44 Q62 22 84 40Z" fill="#B5762A" {s(T2)}/>
<path d="M56 94 Q62 110 76 94Z" fill="#B5762A" {s(T2)}/>
<path d="M48 62 q6 -6 12 0 M60 74 q6 -6 12 0 M46 78 q6 -6 12 0 M62 56 q6 -6 12 0" fill="none" stroke="#B5762A" stroke-width="2.4" stroke-linecap="round"/>
<path d="M70 70 Q62 80 72 86" fill="#F7D48A" {s(T2)}/>
{eye(90, 60, 1.25)}
<path d="M96 74 Q101 76 104 71" fill="none" {s('stroke-width="2.6"')}/>
<ellipse cx="86" cy="72" rx="4.4" ry="2.6" fill="#FF7FA8" opacity=".8"/>
</g>
{bub(104, 24, 5)}{bub(112, 38, 3.2)}{bub(22, 100, 4.4)}
''', 60, 20)
SUBJ["mighty-sharks-novogorsk"] = ("бронзово-золотистый лещ с высокой спинкой",
                                   "делает под водой кувырок-разворот — вокруг него закручена белая пунктирная стрелка")

# 5. Mighty Sharks, Северный — плотва плывёт на спине под флажками
ICONS["mighty-sharks-severny"] = W("#FFEAF1", "#EF6A9A", f'''
<path d="M-4 20 Q64 36 132 20" fill="none" stroke="{O}" stroke-width="2.4"/>
<path d="M8 22 L20 25 L12 40Z" fill="#FFD23F" {s(T3)}/><path d="M32 27 L44 29 L37 44Z" fill="#3DB8EE" {s(T3)}/>
<path d="M57 30 L70 30 L64 46Z" fill="#FFFFFF" {s(T3)}/><path d="M83 29 L95 27 L91 43Z" fill="#7BD957" {s(T3)}/>
<path d="M107 25 L119 22 L116 39Z" fill="#FFD23F" {s(T3)}/>
<path d="M-6 84 Q10 78 26 84 T58 84 T90 84 T134 84 V134 H-6Z" fill="#5CC8F2" {s('stroke-width="2.6"')}/>
<g transform="rotate(180 64 82)">
<path d="M30 82 L10 66 Q16 82 10 98Z" fill="#F0483E" {s()}/>
<path d="M28 82 Q52 60 86 66 Q106 72 108 82 Q100 98 76 100 Q46 102 28 82Z" fill="#CBD8E6" {s()}/>
<path d="M32 80 Q58 66 100 74 Q86 64 62 66 Q44 68 32 80Z" fill="#7F96AE"/>
<path d="M52 66 Q62 52 74 66Z" fill="#F0483E" {s(T2)}/>
<path d="M54 99 Q58 110 68 99Z M76 98 Q82 108 88 96Z" fill="#F0483E" {s(T2)}/>
<circle cx="92" cy="80" r="7" fill="#FF7A2E" {s(T2)}/><circle cx="92" cy="80" r="3.6" fill="{O}"/><circle cx="90.800" cy="78.800" r="1.300" fill="#fff"/>
<path d="M98 90 Q103 91 105 86" fill="none" {s('stroke-width="2.4"')}/>
</g>
<path d="M44 60 Q50 54 56 60 M70 58 Q76 52 82 58" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".9"/>
<path d="M12 108 Q22 103 32 108 M92 114 Q102 109 112 114" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
''', 70, 70)
SUBJ["mighty-sharks-severny"] = ("серебристая плотва с красными плавниками и оранжевым глазом",
                                 "плывёт на спине, животом кверху, под гирляндой разноцветных флажков для разворота")

# 6. «Второе рождение», Косинская — грудничковое плавание вместе с мамой: вьюн-мама обнимает малыша сердечком
ICONS["vtoroe-rozhdenie-kosinskaya"] = W("#E9F1FF", "#4F74F2", f'''
<path d="M64 50 C60 30 30 26 26 52 C22 80 52 96 64 110 C76 96 106 80 102 52 C98 30 76 30 70 44" fill="none" stroke="{O}" stroke-width="19" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M64 50 C60 30 30 26 26 52 C22 80 52 96 64 110 C76 96 106 80 102 52 C98 30 76 30 70 44" fill="none" stroke="#E9B44C" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M30 48 h.1 M30 66 h.1 M42 84 h.1 M86 84 h.1 M98 66 h.1 M96 48 h.1 M52 36 h.1 M84 36 h.1 M56 98 h.1 M72 98 h.1" stroke="#8A5A1E" stroke-width="5" stroke-linecap="round"/>
<path d="M74 40 L84 14 Q88 26 100 24 Q90 34 80 44Z" fill="#C98A2B" {s(T2)}/>
<path d="M30 10 Q40 4 50 10 M94 112 Q104 106 114 112 M8 70 Q13 66 18 70" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".85"/>
<circle cx="64" cy="50" r="13" fill="#F3C768" {s()}/>
<path d="M57 59 Q55 65 52 64 M61 61 Q60 67 57 68 M67 61 Q68 67 71 68 M71 59 Q73 65 76 64" fill="none" {s(T3)}/>
{eye(59, 48, .85)}{eye(69, 48, .85)}
<path d="M61 55 Q64 58 67 55" fill="none" {s('stroke-width="2"')}/>
<path d="M76 78 L88 68 Q86 78 90 86Z" fill="#C98A2B" {s(T3)}/>
<path d="M50 80 Q56 72 64 78 Q72 84 78 76" fill="none" stroke="{O}" stroke-width="12" stroke-linecap="round"/>
<path d="M50 80 Q56 72 64 78 Q72 84 78 76" fill="none" stroke="#FFD98A" stroke-width="7.500" stroke-linecap="round"/>
<circle cx="50" cy="80" r="7.500" fill="#FFD98A" {s(T2)}/>
<circle cx="48" cy="79" r="1.700" fill="{O}"/><circle cx="52.500" cy="78" r="1.700" fill="{O}"/>
<path d="M48 83 Q50 85 52.500 83" fill="none" {s('stroke-width="1.6"')}/>
{bub(16, 22, 5)}{bub(112, 26, 4)}{bub(110, 102, 3.4)}{bub(18, 100, 3.6)}
''', 50, 30)
SUBJ["vtoroe-rozhdenie-kosinskaya"] = ("длинная песочная рыбка-вьюн в тёмную крапинку, с усиками",
                                       "мама-вьюн свернулась сердечком вокруг своего малыша-вьюнка, который плывёт внутри волной")

# 7. «Фитнес Холл», Щербинка — групповое обучение плаванию: три сардины плывут паровозиком
def sardine(x, y, cap):
    return f'''<g transform="translate({x} {y}) rotate(-24) scale(.86)">
<path d="M-22 0 L-36 -10 Q-32 0 -36 10Z" fill="#3E6DB8" {s(T2)}/>
<path d="M-24 0 Q-6 -15 14 -8 Q24 -3 24 2 Q16 12 -4 11 Q-16 10 -24 0Z" fill="#DCE9F5" {s()}/>
<path d="M-20 -2 Q-4 -13 14 -8 Q4 -5 -4 -3 Q-12 -1 -20 -2Z" fill="#3E6DB8"/>
<path d="M4 -10 Q16 -20 25 -3 Q14 -6 4 -5Z" fill="{cap}" {s(T2)}/>
<circle cx="14" cy="1" r="3.4" fill="{O}"/><circle cx="13" cy="0" r="1.100" fill="#fff"/>
<path d="M17 6.500 Q20 7.500 22 4.500" fill="none" {s('stroke-width="1.8"')}/>
</g>'''


ICONS["fitness-hall-shcherbinka"] = W("#E2FCFF", "#12AFD4", f'''
<path d="M-6 118 L134 58" stroke="#fff" stroke-width="3" stroke-dasharray="10 8" opacity=".7"/>
<path d="M-6 66 L134 6" stroke="#fff" stroke-width="3" stroke-dasharray="10 8" opacity=".7"/>
{sardine(96, 40, "#7BD957")}{sardine(66, 66, "#FFD23F")}{sardine(36, 92, "#F0483E")}
{bub(18, 44, 4.4)}{bub(104, 100, 5)}{bub(114, 86, 3)}
''', 26, 70)
SUBJ["fitness-hall-shcherbinka"] = ("три серебристо-синие сардины в красной, жёлтой и зелёной плавательных шапочках",
                                    "плывут друг за другом паровозиком наискосок между двумя пунктирными разметками дорожек")

# 8. «Пиранья», Заречье — суматранский барбус выпрыгивает из воды
ICONS["piranya-zarechye"] = W("#F1FFE9", "#53C46F", f'''
<path d="M14 96 Q40 8 110 80" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-dasharray="1 10" opacity=".9"/>
<g transform="rotate(-22 64 50)">
<path d="M36 50 L14 34 Q20 50 14 68Z" fill="#F0483E" {s()}/>
<path d="M34 50 Q52 22 84 30 Q102 36 104 50 Q98 70 76 74 Q50 76 34 50Z" fill="#FFD23F" {s()}/>
<path d="M48 34 L46 66 M62 28 L60 73 M76 29 L76 74" stroke="#2B2540" stroke-width="7" stroke-linecap="round"/>
<path d="M56 30 Q66 12 80 30Z" fill="#F0483E" {s(T2)}/>
<path d="M60 74 Q64 88 76 74Z" fill="#F0483E" {s(T2)}/>
{eye(91, 44, 1.2)}
<path d="M88 56 H102 L99 62 L96 57 L93 62 L90 57Z" fill="#fff" {s('stroke-width="2"')}/>
<path d="M100 48 Q108 50 104 56" fill="#F0483E" {s(T3)}/>
</g>
<path d="M-6 100 Q10 92 26 100 T58 100 T90 100 T134 100 V134 H-6Z" fill="#2F8FE0" {s('stroke-width="2.6"')}/>
<path d="M14 92 Q10 82 16 76 Q22 84 14 92Z M30 88 Q28 80 32 76 Q36 82 30 88Z M4 84 Q2 78 6 74 Q9 80 4 84Z" fill="#BDEBFF" {s(T3)}/>
<path d="M70 114 Q80 109 90 114 M24 116 Q34 111 44 116" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
''', 70, 18)
SUBJ["piranya-zarechye"] = ("жёлтый суматранский барбус с тремя чёрными полосками, красными плавниками и зубастой улыбкой",
                            "высокой дугой выпрыгивает из синей воды бассейна, за ним тянется пунктирный след и брызги")

# 9. Child Ocean, ул. Генерала Белова — детский бассейн с морской водой: рыба-игла достаёт со дна кольцо для ныряния
ICONS["child-ocean-belova"] = W("#D3F7F1", "#0C6C78", f'''
<path d="M16 134 Q8 104 18 86 Q20 106 28 134Z M34 134 Q30 112 38 98 Q40 114 44 134Z" fill="#37C28A" {s(T2)}/>
<path d="M-6 120 Q30 110 64 120 T134 116 V134 H-6Z" fill="#F4DFA6" {s('stroke-width="2.6"')}/>
<path d="M14 100 Q40 96 58 74 Q76 52 98 40" fill="none" stroke="{O}" stroke-width="17" stroke-linecap="round"/>
<path d="M14 100 Q40 96 58 74 Q76 52 98 40" fill="none" stroke="#2FD08C" stroke-width="11" stroke-linecap="round"/>
<path d="M26 99 l3 -7 M38 93 l4 -6 M49 84 l5 -5 M60 72 l5 -5 M71 60 l5 -4 M83 49 l5 -3" stroke="#FFE46B" stroke-width="3" stroke-linecap="round"/>
<path d="M54 68 Q52 52 68 56Z" fill="#FFE46B" {s(T2)}/>
<path d="M8 96 L-2 84 Q2 100 -2 112Z" fill="#FFE46B" {s(T2)}/>
<path d="M98 40 L122 24" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M98 40 L122 24" stroke="#2FD08C" stroke-width="4" stroke-linecap="round"/>
<ellipse cx="110" cy="32" rx="7" ry="13" transform="rotate(-34 110 32)" fill="none" stroke="{O}" stroke-width="10"/>
<ellipse cx="110" cy="32" rx="7" ry="13" transform="rotate(-34 110 32)" fill="none" stroke="#FF6B3D" stroke-width="5"/>
{eye(93, 43, .8)}
<ellipse cx="86" cy="50" rx="3.4" ry="2" fill="#FF7FA8" opacity=".9"/>
{bub(40, 36, 6)}{bub(54, 22, 4)}{bub(26, 52, 3.4)}{bub(100, 84, 4.4)}
''', 30, 20)
SUBJ["child-ocean-belova"] = ("длинная тонкая изумрудная рыба-игла с жёлтыми насечками на спине",
                              "вытянулась наискосок от песчаного дна с водорослями и несёт на длинном носу оранжевое кольцо для ныряния")

if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for i in ids:
        open(os.path.join(OUT, i + ".svg"), "w", encoding="utf-8").write(ICONS[i])
    print("svg:", len(ids))
    for i in ids:
        print(f"{i} — герой: {SUBJ[i][0]} | сцена: {SUBJ[i][1]}")
