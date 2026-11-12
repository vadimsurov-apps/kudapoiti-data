"""Иконки робота creative, 12.11 (запуск 1112s). Каждая придумана и нарисована отдельно: свой герой, своя сцена,
своя компоновка и свой фон (правило абсолютной уникальности). python3 tools/icons_creative_1112s.py [--subjects]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_creative_1112k import bg, ln, limb, note, head, SKIN

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
I = {}
SW2 = s('stroke-width="2"')

# 1 Элайнз (танцы и акробатика 3–16): девочка в стойке на руках с ногами в шпагат у зеркальной стены
I["elainz-kantemirovskaya"] = ("девочка с косичкой в красном топе и чёрных джоггерах",
    "стоит на руках у зеркальной стены танцзала, ноги раскрыты в шпагат буквой Т", bg("#FFE7F1", "#C2185B", f'''
<rect x="78" y="0" width="60" height="128" fill="#BFE6F5" opacity=".75"/><path d="M84 10 L96 40 M100 8 L110 30" stroke="#fff" stroke-width="3" opacity=".8"/>
<path d="M0 108 H128 V128 H0Z" fill="#C98B4E"/><path d="M0 114 H128" stroke="#A86E37" stroke-width="2"/>
{limb(52, 104, 54, 80, SKIN, 5)}{limb(74, 104, 72, 80, SKIN, 5)}
<path d="M50 82 Q63 70 76 82 L72 60 Q63 56 54 60Z" fill="#E53935" {s()}/>
<path d="M54 60 L60 38 L66 38 L72 60Z" fill="#26232E" {s()}/>
{limb(60, 40, 24, 30, "#26232E", 7)}{limb(66, 40, 102, 30, "#26232E", 7)}
<circle cx="22" cy="30" r="5" fill="#fff" {s('stroke-width="2.4"')}/><circle cx="104" cy="30" r="5" fill="#fff" {s('stroke-width="2.4"')}/>
<circle cx="63" cy="94" r="12" fill="{SKIN}" {s()}/>
<path d="M51 96 Q52 108 63 108 Q74 108 75 96 Q63 102 51 96Z" fill="#5A3A22" {s('stroke-width="2.4"')}/>
<path d="M63 108 Q66 116 62 122" fill="none" {ln("#5A3A22", 4)}/>
{eye(58, 92, 0.5)}{eye(68, 92, 0.5)}<path d="M60 86 Q63 84 66 86" fill="none" {ln(O, 1.8)}/>
{sparkle(30, 66, 4)}{sparkle(110, 70, 3.5)}
'''))

# 2 ТанцПол (хип-хоп для детей от 8): кепка-снэпбек сама танцует
I["tancpol-elektrolitny"] = ("алая кепка-снэпбек с прямым жёлтым козырьком и мордашкой на лбу",
    "крутится на козырьке, как брейкер, на сером полу студии, вокруг расходятся звуковые волны", bg("#E8F6E0", "#2E7D32", f'''
<ellipse cx="64" cy="112" rx="40" ry="8" fill="#000" opacity=".2"/>
<path d="M20 70 Q12 56 20 42 M108 70 Q116 56 108 42 M10 76 Q-2 56 10 36 M118 76 Q130 56 118 36" fill="none" {ln("#fff", 3.5)}/>
<g transform="rotate(-18 64 70)">
<path d="M34 72 Q34 36 64 34 Q94 36 94 72Z" fill="#E53935" {s()}/>
<path d="M64 34 V72 M48 38 Q44 56 46 72 M80 38 Q84 56 82 72" stroke="#B71C1C" stroke-width="2"/>
<circle cx="64" cy="34" r="4" fill="#B71C1C" {s('stroke-width="2"')}/>
<path d="M30 72 H98 L104 82 H24Z" fill="#FFD23A" {s()}/>
{face(64, 58, 9, 0.75)}
</g>
<path d="M60 98 Q64 108 68 98" fill="none" {ln(O, 3)}/>
{note(104, 24, 0.7, "#fff")}{note(20, 22, 0.6, "#FFD23A")}
'''))

# 3 Белая гончарная (детский курс 8–12): белое кашпо на полке сушки
I["belaya-goncharnaya-nagatinskaya"] = ("белое керамическое кашпо с мордашкой, расписанное синими точками",
    "сидит на деревянной полке сушки, из него выглядывает маленький зелёный росток, рядом синяя капля ангоба", bg("#EAF2FF", "#1E4E9C", f'''
<path d="M0 96 H128 V104 H0Z" fill="#B98A5A" {s('stroke-width="2.4"')}/><path d="M14 104 V128 M114 104 V128" {ln("#8C6239", 6)}/>
<path d="M36 58 H92 L86 96 H42Z" fill="#FBFBF8" {s()}/>
<path d="M32 50 H96 V60 H32Z" fill="#fff" {s()}/>
<g fill="#2B5DC9">{''.join(f'<circle cx="{x}" cy="{y}" r="2.6"/>' for x, y in ((44, 66), (54, 70), (74, 70), (84, 66), (48, 86), (64, 90), (80, 86)))}</g>
{face(64, 74, 8, 0.7)}
<path d="M64 50 Q62 36 64 28" fill="none" {ln("#3E8E3E", 4)}/>
<path d="M64 36 Q52 26 46 32 Q54 40 64 36Z M64 30 Q74 18 82 24 Q74 34 64 30Z" fill="#6CCB5F" {s('stroke-width="2.4"')}/>
<path d="M108 76 Q102 86 108 90 Q114 86 108 76Z" fill="#2B5DC9" {s('stroke-width="2.2"')}/>
{sparkle(20, 36, 4)}
'''))

# 4 Арт-студия «Пушкин» (рисунок и живопись 4–16): кудрявый мальчик с бакенбардами у мольберта
I["art-pushkin-starosadsky"] = ("кудрявый мальчик с бакенбардами в чёрной крылатке",
    "рисует кистью жёлтое солнце на холсте мольберта посреди осеннего бульвара", bg("#FFF3D9", "#C77A1E", f'''
<path d="M84 30 L80 112 M112 30 L116 112 M98 28 V116" {ln("#8C5A2B", 4)}/>
<rect x="74" y="24" width="46" height="46" rx="3" fill="#fff" {s()}/>
<circle cx="97" cy="46" r="10" fill="#FFC928" {s('stroke-width="2.2"')}/>
<path d="M97 30 V33 M97 59 V62 M81 46 H84 M110 46 H113" {ln("#FFC928", 3)}/>
<path d="M22 118 Q24 84 44 80 Q64 84 66 118Z" fill="#26232E" {s()}/>
<path d="M30 84 L22 100 L40 96Z" fill="#26232E" {s('stroke-width="2.4"')}/>
{limb(58, 92, 74, 62, "#26232E", 6)}
<path d="M74 62 L84 50" {ln(O, 5)}/><path d="M74 62 L84 50" {ln("#C8823A", 3)}/><circle cx="85" cy="49" r="3" fill="#E53935"/>
<circle cx="44" cy="62" r="17" fill="{SKIN}" {s()}/>
<g fill="#3A2416" {s('stroke-width="2.2"')}>{''.join(f'<circle cx="{x}" cy="{y}" r="6"/>' for x, y in ((30, 52), (36, 44), (45, 41), (54, 44), (59, 52), (28, 61)))}</g>
<path d="M28 64 Q28 76 34 78 L34 66Z M60 64 Q60 76 54 78 L54 66Z" fill="#3A2416" {s('stroke-width="2"')}/>
{eye(39, 63, 0.55)}{eye(49, 63, 0.55)}<path d="M41 71 Q44 74 47 71" fill="none" {ln(O, 1.8)}/>
<path d="M10 20 Q16 14 22 20 Q16 26 10 20Z" fill="#E8862B"/><path d="M20 108 Q26 102 30 108 Q26 114 20 108Z" fill="#D9552B"/>
'''))

# 5 Колибри (балет и танцевальный спорт с 4 лет): девочка с крылышками колибри кружится над цветком
I["kolibri-andropova"] = ("девочка в изумрудном купальнике с прозрачными крылышками колибри за спиной",
    "кружится на носочке на раскрытом розовом цветке гибискуса, вокруг мелкие нектарные капли", bg("#E4FFF6", "#00897B", f'''
<path d="M64 112 Q30 96 26 120 Q50 124 64 116 Q78 124 102 120 Q98 96 64 112Z" fill="#FF6FA5" {s()}/>
<path d="M64 112 Q56 92 64 84 Q72 92 64 112Z" fill="#FF9FC4" {s('stroke-width="2.2"')}/>
<path d="M56 54 Q30 30 22 46 Q32 60 56 62Z M72 54 Q98 30 106 46 Q96 60 72 62Z" fill="#C8F4FF" opacity=".85" {s('stroke-width="2.2"')}/>
{limb(64, 82, 64, 104, SKIN, 5)}{limb(64, 82, 82, 92, SKIN, 5)}
<path d="M54 58 Q64 52 74 58 L72 84 Q64 88 56 84Z" fill="#12B886" {s()}/>
{limb(56, 62, 46, 40, SKIN, 4)}{limb(72, 62, 82, 40, SKIN, 4)}
<path d="M44 38 Q64 26 84 38" fill="none" {ln("#12B886", 2.5)}/>
{head(64, 44, 11, "#2C1B12", 0.5)}
<circle cx="64" cy="31" r="4.5" fill="#2C1B12" {s('stroke-width="2"')}/>
<g fill="#FFE08A">{''.join(f'<circle cx="{x}" cy="{y}" r="2.4"/>' for x, y in ((24, 76), (100, 74), (36, 92), (94, 94), (18, 60)))}</g>
'''))

# 6 The Step Family (уличные танцы с 5 лет): прыжок-кик над ступеньками крыльца
I["step-family-kommunarka"] = ("девочка в жёлтом оверсайз-худи с хвостиками-антеннами",
    "делает высокий прыжок-кик над тремя бетонными ступеньками уличного крыльца", bg("#F1ECFF", "#5E35B1", f'''
<path d="M40 128 V112 H70 V98 H100 V84 H140 V128Z" fill="#B0AEB8" {s()}/>
<path d="M40 112 H70 M70 98 H100" stroke="#8E8C96" stroke-width="2"/>
<path d="M14 92 Q24 86 30 94" fill="none" {ln("#fff", 3)}/><path d="M10 102 Q22 96 30 104" fill="none" {ln("#fff", 3)}/>
{limb(52, 70, 30, 76, "#3949AB", 7)}{limb(60, 72, 74, 92, "#3949AB", 7)}
<path d="M24 72 L32 82 L22 84Z" fill="#fff" {s('stroke-width="2.2"')}/><path d="M70 92 L80 96 L72 100Z" fill="#fff" {s('stroke-width="2.2"')}/>
<path d="M42 44 Q56 36 70 44 L74 72 Q56 78 40 72Z" fill="#FFD23A" {s()}/>
{limb(44, 50, 26, 34, "#FFD23A", 7)}{limb(70, 50, 92, 40, "#FFD23A", 7)}
{head(57, 30, 12, "#8B4A1F", 0.5)}
<path d="M47 20 L40 8 M67 20 L74 8" {ln("#8B4A1F", 4)}/><circle cx="40" cy="8" r="3.5" fill="#FF5A7A"/><circle cx="74" cy="8" r="3.5" fill="#FF5A7A"/>
{sparkle(104, 20, 5)}{sparkle(110, 62, 3.5)}
'''))

# 7 Студия балета Софии Романовой (балет с 2 лет): балетный пучок-гулька делает плие
I["ballet-romanova-kommunarka"] = ("балетный пучок-гулька в розовой сеточке с мордашкой и ножками-шпильками",
    "делает плие на маленькой розовой атласной подушечке с кисточками", bg("#FFF0F5", "#AD1457", f'''
<path d="M18 104 Q64 86 110 104 Q64 122 18 104Z" fill="#F48FB1" {s()}/>
<path d="M18 104 L10 112 M110 104 L118 112" {ln("#FFD23A", 4)}/>
<path d="M50 92 Q44 84 48 76 M78 92 Q84 84 80 76" fill="none" {ln("#5D4037", 3.5)}/>
<path d="M42 96 Q48 90 56 94 Q50 100 42 96Z M72 94 Q80 90 86 96 Q78 100 72 94Z" fill="#F8BBD0" {s('stroke-width="2.2"')}/>
<circle cx="64" cy="58" r="26" fill="#A1887F" {s()}/>
<path d="M40 50 Q64 36 88 50 M38 62 Q64 76 90 62 M50 36 Q46 58 52 80 M78 36 Q82 58 76 80" fill="none" stroke="#F8BBD0" stroke-width="1.4" opacity=".7"/>
<path d="M44 40 Q54 32 62 36" fill="none" stroke="#8D6E63" stroke-width="3"/>
{face(64, 60, 9, 0.75)}
<path d="M36 46 L26 40 M92 46 L102 40" {ln("#5D4037", 3)}/>
<path d="M64 34 Q52 22 46 32 Q54 40 64 34Z M64 34 Q76 22 82 32 Q74 40 64 34Z" fill="#F06292" {s('stroke-width="2.2"')}/><circle cx="64" cy="34" r="3.5" fill="#F06292" {s('stroke-width="2"')}/>
{sparkle(22, 30, 4)}{sparkle(108, 70, 3.5)}
'''))

# 8 Music Star (раннее музыкальное развитие с 3 лет, инструменты, вокал): треугольник звенит звёздочками
I["music-star-kommunarka"] = ("серебряный оркестровый треугольник с мордашкой, подвешенный на красном шнурке",
    "по нему стучит металлическая палочка, и во все стороны разлетаются золотые звёздочки", bg("#FFF9E0", "#6A1B9A", f'''
<path d="M64 6 V26" {ln("#E53935", 3)}/>
<path d="M64 26 L104 100 H24Z" fill="none" {ln(O, 12)}/>
<path d="M64 26 L104 100 H24Z" fill="none" {ln("#D7DDE6", 7)}/>
<path d="M60 34 L30 94" stroke="#fff" stroke-width="2" opacity=".8"/>
{face(64, 74, 9, 0.8)}
<path d="M102 52 L72 82" {ln(O, 6)}/><path d="M102 52 L72 82" {ln("#B0BEC5", 3)}/>
{''.join(sparkle(x, y, r, "#FFC928") for x, y, r in ((18, 40, 6), (110, 30, 5), (16, 112, 4.5), (112, 112, 5), (34, 18, 3.5), (96, 72, 3)))}
'''))

# 9 «Полёт» (театральная студия 5–17): мальчик-актёр «летит» на сцене перед облаками-декорациями
I["polet-kommunarka"] = ("мальчик-актёр в очках-авиаторах и длинном белом шарфе",
    "раскинул руки самолётом на краю детской сцены, за ним фанерные облака-декорации на палках", bg("#E3F2FD", "#1565C0", f'''
<path d="M14 50 Q14 36 28 38 Q34 26 48 34 Q60 32 58 50Z" fill="#fff" {s()}/><path d="M36 50 V96" {ln("#8C6239", 3)}/>
<path d="M78 40 Q78 28 90 30 Q98 20 110 28 Q120 30 118 42Z" fill="#fff" {s()}/><path d="M98 42 V96" {ln("#8C6239", 3)}/>
<path d="M0 100 H128 V128 H0Z" fill="#8D5524" {s()}/><path d="M0 106 H128" stroke="#6D3F18" stroke-width="2"/>
{limb(58, 82, 52, 100, "#455A64", 6)}{limb(70, 82, 76, 100, "#455A64", 6)}
<path d="M54 60 Q64 54 74 60 L72 84 H56Z" fill="#90A4AE" {s()}/>
{limb(56, 64, 22, 60, "#90A4AE", 6)}{limb(72, 64, 106, 60, "#90A4AE", 6)}
<path d="M58 60 Q48 66 34 80 Q42 82 60 66" fill="#fff" {s('stroke-width="2.2"')}/>
{head(64, 46, 12, "#C77A1E", 0.5)}
<rect x="54" y="42" width="9" height="7" rx="3" fill="#4FC3F7" {s('stroke-width="2"')}/><rect x="65" y="42" width="9" height="7" rx="3" fill="#4FC3F7" {s('stroke-width="2"')}/>
'''))

# 10 La Prima (балет 4–12, хореография 3–5): прима в гранд-жете над рампой
I["la-prima-davydkovskaya"] = ("девочка-прима в бордовом трико и белых гетрах",
    "застыла в высоком гранд-жете над краем сцены с тремя круглыми огнями рампы", bg("#2B1B3A", "#120A1C", f'''
<path d="M0 104 H128 V128 H0Z" fill="#5D2E1A" {s()}/>
{''.join(f'<ellipse cx="{x}" cy="104" rx="9" ry="4" fill="#FFE082" {SW2}/><path d="M{x-10} 102 L{x-24} 70 L{x+24} 70 L{x+10} 102Z" fill="#FFE082" opacity=".18"/>' for x in (24, 64, 104))}
{limb(56, 66, 20, 56, "#FFF8E1", 6)}{limb(70, 66, 106, 70, "#FFF8E1", 6)}
<path d="M18 52 L12 58 M108 70 L118 72" {ln("#F8BBD0", 4)}/>
<path d="M54 46 Q64 40 72 46 L72 68 Q62 72 54 68Z" fill="#8E1B3C" {s()}/>
{limb(56, 50, 34, 30, SKIN, 4)}{limb(70, 50, 92, 28, SKIN, 4)}
{head(63, 34, 10, "#3E2723", 0.45)}<circle cx="63" cy="22" r="4" fill="#3E2723" {s('stroke-width="2"')}/>
{sparkle(20, 24, 4)}{sparkle(108, 18, 3)}{sparkle(98, 46, 2.5)}
'''))

# 11 ДМШ № 98 (подготовительный класс, вокал, «Музыка с мамой»): валторна трубит с пюпитра
I["dmsh-98-kronshtadtsky"] = ("медная валторна с мордашкой в раструбе",
    "сидит на чёрном нотном пюпитре и трубит, из раструба вылетают три цветные ноты", bg("#FFF4E5", "#8D4A12", f'''
<path d="M64 96 V124 M50 124 H78" {ln(O, 5)}/>
<path d="M30 92 H98 L92 104 H36Z" fill="#26232E" {s()}/>
<circle cx="52" cy="62" r="24" fill="none" {ln(O, 12)}/><circle cx="52" cy="62" r="24" fill="none" {ln("#E0A43A", 7)}/>
<circle cx="52" cy="62" r="13" fill="none" {ln(O, 9)}/><circle cx="52" cy="62" r="13" fill="none" {ln("#F2C14E", 4.5)}/>
<path d="M70 48 Q90 40 98 26" fill="none" {ln(O, 11)}/><path d="M70 48 Q90 40 98 26" fill="none" {ln("#E0A43A", 6)}/>
<ellipse cx="102" cy="20" rx="16" ry="10" transform="rotate(-30 102 20)" fill="#F2C14E" {s()}/>
<ellipse cx="102" cy="20" rx="9" ry="5" transform="rotate(-30 102 20)" fill="#8D4A12"/>
{eye(98, 20, 0.4)}{eye(106, 16, 0.4)}
<circle cx="40" cy="44" r="3.5" fill="#B0BEC5" {s('stroke-width="2"')}/><circle cx="34" cy="54" r="3.5" fill="#B0BEC5" {s('stroke-width="2"')}/>
{note(18, 22, 0.7, "#E53935")}{note(70, 12, 0.6, "#43A047")}{note(116, 52, 0.6, "#1E88E5")}
'''))

# 12 Art Kids Community, Коммунарка (актёрская школа 4–16): девочка-звездочёт на детской сцене
I["artkids-kommunarka-skandinavsky"] = ("девочка-актриса в костюме звездочёта — синий колпак и плащ в звёздах",
    "читает роль, подняв руку к картонной луне, на маленькой сцене в пятне софита", bg("#0D1B3E", "#050A1A", f'''
<path d="M64 0 L22 108 H106Z" fill="#FFF59D" opacity=".18"/>
<ellipse cx="64" cy="110" rx="44" ry="8" fill="#FFF59D" opacity=".35"/>
<path d="M0 112 H128 V128 H0Z" fill="#6D3F18" {s()}/>
<path d="M98 18 Q84 30 98 44 Q86 42 84 30 Q86 20 98 18Z" fill="#FFD54F" {s('stroke-width="2.4"')}/>
<path d="M40 110 Q42 70 64 64 Q86 70 88 110Z" fill="#283593" {s()}/>
<g fill="#FFD54F">{''.join(sparkle(x, y, 3.2, "#FFD54F") for x, y in ((52, 86), (72, 94), (62, 104), (78, 78)))}</g>
{limb(78, 74, 92, 46, "#283593", 6)}<circle cx="93" cy="44" r="4" fill="{SKIN}" {s('stroke-width="2"')}/>
<circle cx="64" cy="56" r="13" fill="{SKIN}" {s()}/>
{eye(59, 56, 0.5)}{eye(69, 56, 0.5)}<ellipse cx="64" cy="63" rx="3" ry="2.4" fill="{O}"/>
<path d="M48 48 L64 6 L80 48Z" fill="#3949AB" {s()}/>
{sparkle(62, 26, 3.5, "#FFD54F")}{sparkle(68, 38, 2.6, "#FFD54F")}
{sparkle(20, 30, 3)}{sparkle(30, 70, 2.4)}{sparkle(112, 76, 2.6)}
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
