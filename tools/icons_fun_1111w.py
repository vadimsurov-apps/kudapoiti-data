"""Иконки робота fun (2026-11-11, проход w): места из tools/add_fun_1111w.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя палитра фона.
Запуск: python3 tools/icons_fun_1111w.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}


def stars(pts, r=3, c="#fff"):
    return "".join(sparkle(x, y, r, c) for x, y in pts)


# 1. Пиксель Арена (Серпухов) — плитка пиксельного пола подпрыгивает, соседние вспыхивают
I["fun-pixel-arena-serpukhov"] = ("#2B2F4A", "#0E1022",
    "светящаяся бирюзовая квадратная плитка пиксельного пола с мордашкой",
    "выпрыгнула из тёмного пола, а соседние плитки под ней вспыхивают малиновым и жёлтым",
    "".join(f'<rect x="{x}" y="{y}" width="22" height="14" rx="2" fill="{c}" {W(2)}/>'
            for x, y, c in ((8, 96, "#3A3F66"), (32, 96, "#FF4F8B"), (56, 96, "#3A3F66"), (80, 96, "#FFD23F"),
                            (104, 96, "#3A3F66"), (20, 112, "#FFD23F"), (44, 112, "#3A3F66"), (68, 112, "#FF4F8B"),
                            (92, 112, "#3A3F66"))) +
    f'<rect x="56" y="96" width="22" height="14" rx="2" fill="#1B1E36" {W(2)}/>'
    f'<path d="M50 88 Q67 80 84 88" fill="none" stroke="#5FF2E0" stroke-width="2.4" opacity=".7"/>'
    f'<rect x="34" y="26" width="60" height="52" rx="8" fill="#3DE8D2" {W(3.4)}/>'
    f'<rect x="40" y="31" width="48" height="8" rx="4" fill="#B8FFF5" opacity=".8"/>'
    + face(64, 54, d=10, k=0.9) +
    f'<path d="M28 40 l-8 -4 M28 58 l-10 0 M100 40 l8 -4 M100 58 l10 0" stroke="#5FF2E0" stroke-width="3" stroke-linecap="round"/>'
    + stars(((18, 18), (112, 22)), 3, "#FFD23F"))

# 2. Квесты в реальности (Серпухов) — каменный куб с рунами, из скважины сыплются вопросики
I["fun-kvesty-v-realnosti-serpukhov"] = ("#E9E2FF", "#7A5CC8",
    "фиолетовый каменный куб с вырезанными золотыми рунами и светящейся замочной скважиной",
    "парит над каменной подставкой, а из скважины вылетают золотые вопросительные знаки",
    f'<path d="M34 112 H94 L88 100 H40Z" fill="#9C8FB8" {W(3)}/>'
    f'<ellipse cx="64" cy="94" rx="20" ry="4" fill="#3B2A66" opacity=".3"/>'
    f'<path d="M64 22 L98 36 L98 76 L64 90 L30 76 L30 36Z" fill="#5B3FA6" {W(3.4)}/>'
    f'<path d="M64 22 L98 36 L64 50 L30 36Z" fill="#7C5CD6" {W(3)}/>'
    f'<path d="M64 50 V90" {W(3)}/>'
    f'<path d="M38 50 l6 4 -6 4 M42 66 h8 M88 52 l-4 8 h6 M80 70 l6 -4" fill="none" stroke="#FFD23F" stroke-width="2.4"/>'
    f'<circle cx="64" cy="64" r="6" fill="#FFE98A" {W(2.4)}/><path d="M62 68 L60 78 H68 L66 68" fill="#FFE98A" {W(2.4)}/>'
    + eye(52, 42, 0.55) + eye(76, 42, 0.55) +
    f'<text x="18" y="30" font-family="Arial" font-weight="bold" font-size="18" fill="#FFC531" stroke="#3B3355" stroke-width="1.4">?</text>'
    f'<text x="100" y="22" font-family="Arial" font-weight="bold" font-size="14" fill="#FFC531" stroke="#3B3355" stroke-width="1.2">?</text>'
    + stars(((106, 52), (20, 62)), 3, "#FFD23F"))

# 3. ЭкоПати (Жуковский) — рация в тёмном бункере шепчет «приём»
I["fun-ekopati-zhukovsky"] = ("#4E5A47", "#1D2419",
    "жёлтая детская рация с антенной и красной лампочкой",
    "в полутьме бункера шепчет в облачко со знаком вопроса, лампочка мигает",
    f'<rect x="0" y="100" width="128" height="28" fill="#2E3828"/>'
    + "".join(f'<path d="M{x} 100 V128" stroke="#1D2419" stroke-width="2"/>' for x in (20, 52, 84, 116)) +
    f'<path d="M50 34 V10" stroke="#3B3355" stroke-width="5" stroke-linecap="round"/><circle cx="50" cy="9" r="4" fill="#3B3355"/>'
    f'<rect x="38" y="32" width="46" height="70" rx="10" fill="#FFC931" {W(3.4)}/>'
    f'<rect x="46" y="40" width="30" height="18" rx="4" fill="#1F2A1A" {W(2.4)}/>'
    + "".join(f'<path d="M48 {y} H74" stroke="#B88A10" stroke-width="2.4" stroke-linecap="round"/>' for y in (84, 90, 96)) +
    f'<circle cx="76" cy="30" r="5" fill="#FF4040" {W(2)}/><path d="M76 20 v-4 M84 24 l3 -3 M86 31 h4" stroke="#FF8080" stroke-width="2" stroke-linecap="round"/>'
    + face(61, 70, d=8, k=0.7) +
    f'<path d="M48 49 l4 -3 4 4 4 -4 4 4 4 -3 4 2" fill="none" stroke="#6CFF8A" stroke-width="1.8"/>'
    f'<path d="M92 50 Q92 38 106 38 Q120 38 120 50 Q120 62 106 62 L100 70 L100 62 Q92 60 92 50Z" fill="#FFFFFF" {W(2.4)}/>'
    f'<text x="101" y="57" font-family="Arial" font-weight="bold" font-size="16" fill="#3B3355">?</text>')

# 4. «Знак Творчества» (Лобня) — графический планшет со стилусом рисует знак-звезду
I["fun-znak-tvorchestva-lobnya"] = ("#E3F7FF", "#4FB3D9",
    "графический планшет с тонким стилусом на шнурке",
    "стилус сам выводит на светящемся экране яркую розовую звезду, планшет довольно улыбается",
    f'<rect x="14" y="40" width="90" height="64" rx="10" fill="#2E3445" {W(3.4)}/>'
    f'<rect x="24" y="48" width="70" height="48" rx="4" fill="#FFFFFF" {W(2.4)}/>'
    f'<path d="M52 56 L56 66 L67 66 L58 72 L62 83 L52 76 L42 83 L46 72 L37 66 L48 66Z" fill="#FF6FB5" {W(2.4)}/>'
    f'<path d="M108 58 Q118 70 104 80" fill="none" stroke="#3B3355" stroke-width="2"/>'
    f'<path d="M112 22 L76 70" stroke="#3B3355" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M112 22 L76 70" stroke="#9AA4FF" stroke-width="4.5" stroke-linecap="round"/>'
    f'<path d="M78 67 L72 76 L80 72Z" fill="#3B3355"/>'
    + eye(36, 89, 0.45) + eye(80, 89, 0.45) +
    f'<path d="M52 92 Q58 95 64 92" fill="none" {W(2)}/>'
    + stars(((20, 22), (60, 18), (98, 36)), 3, "#FFE14D"))

# 5. «Тайны Чародеев» (Лобня) — кружка-котёнок раскрашивает себе пятнышки
I["fun-tainy-charodeev-lobnya"] = ("#FFF4E3", "#E3A86A",
    "белая керамическая кружка в форме пузатого котёнка с ушками",
    "держит хвостом-ручкой кисточку и раскрашивает себе голубые пятнышки ангобом",
    f'<ellipse cx="60" cy="110" rx="40" ry="7" fill="#B9773B" opacity=".35"/>'
    f'<path d="M30 46 L34 28 L46 40Z" fill="#FFFFFF" {W(3)}/><path d="M90 46 L86 28 L74 40Z" fill="#FFFFFF" {W(3)}/>'
    f'<path d="M28 44 H92 V96 Q92 110 78 110 H42 Q28 110 28 96Z" fill="#FFFFFF" {W(3.4)}/>'
    f'<ellipse cx="60" cy="44" rx="32" ry="6" fill="#F3E3CF" {W(2.6)}/>'
    f'<path d="M92 56 Q112 56 110 76 Q108 90 92 88" fill="none" stroke="#3B3355" stroke-width="8"/>'
    f'<path d="M92 56 Q112 56 110 76 Q108 90 92 88" fill="none" stroke="#FFFFFF" stroke-width="4.5"/>'
    f'<path d="M108 74 L118 50" stroke="#C98A5A" stroke-width="4" stroke-linecap="round"/><path d="M118 50 l2 -7" stroke="#4FA3E8" stroke-width="5" stroke-linecap="round"/>'
    f'<circle cx="42" cy="92" r="6" fill="#7EC4F2"/><circle cx="76" cy="98" r="5" fill="#7EC4F2"/><circle cx="80" cy="60" r="4" fill="#7EC4F2"/>'
    + face(58, 72, d=10, k=0.85) +
    f'<path d="M40 74 H28 M40 79 H30 M76 74 H88 M76 79 H86" stroke="#3B3355" stroke-width="1.6"/>'
    + stars(((18, 22), (104, 22)), 3, "#FFFFFF"))

# 6. Арт-студия «Малевич» (Лобня) — чёрный квадрат, которому дорисовали солнышко
I["fun-malevich-lobnya"] = ("#FFFBEA", "#F0C75A",
    "чёрный квадрат в широкой золотой раме с мордашкой",
    "висит на стене, а детская кисточка с оранжевой краской дорисовала ему круглое солнышко с лучиками",
    f'<rect x="20" y="20" width="76" height="76" rx="3" fill="#E0A93A" {W(3.4)}/>'
    f'<rect x="28" y="28" width="60" height="60" fill="#22202A" {W(2.4)}/>'
    f'<circle cx="74" cy="40" r="8" fill="#FF9A2E" {W(2)}/>'
    + "".join(f'<path d="M{74 + 11 * dx} {40 + 11 * dy} l{4 * dx} {4 * dy}" stroke="#FF9A2E" stroke-width="2.6" stroke-linecap="round"/>'
              for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1), (0.7, 0.7), (-0.7, 0.7), (0.7, -0.7), (-0.7, -0.7))) +
    eye(48, 62, 0.65) + eye(64, 62, 0.65) +
    f'<path d="M50 72 Q56 77 62 72" fill="none" stroke="#FFFFFF" stroke-width="2.2"/>'
    f'<path d="M120 116 L96 54" stroke="#C98A5A" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M98 58 L92 44 Q90 38 94 40 L100 54Z" fill="#FF9A2E" {W(2)}/><rect x="95" y="54" width="8" height="8" transform="rotate(-21 99 58)" fill="#B9B9C8" {W(1.6)}/>'
    f'<circle cx="104" cy="104" r="3" fill="#FF9A2E"/><circle cx="110" cy="96" r="2" fill="#FF9A2E"/>')

# 7. Арт-студия НВ (Лобня) — клячка, вылепленная в зайчика
I["fun-art-studiya-nv-lobnya"] = ("#E8F7EC", "#7CC48E",
    "серый мягкий ластик-клячка, вылепленный в длинноухого зайчика",
    "стирает на листе лишнюю линию с наброска яблока, оставляя чистую дорожку",
    f'<rect x="10" y="66" width="108" height="54" rx="4" fill="#FFFFFF" {W(3)}/>'
    f'<path d="M22 100 Q30 76 50 80 Q66 84 60 104 Q54 114 36 112 Q22 110 22 100Z" fill="none" stroke="#6B6B7A" stroke-width="2.2"/>'
    f'<path d="M42 80 Q44 72 50 70" fill="none" stroke="#6B6B7A" stroke-width="2.2"/>'
    f'<path d="M62 92 L100 84" stroke="#B0B0BC" stroke-width="2" stroke-dasharray="3 4"/>'
    f'<path d="M78 30 Q72 6 80 6 Q88 6 86 32" fill="#A9A9B8" {W(3)}/><path d="M92 32 Q96 8 104 10 Q110 14 98 36" fill="#A9A9B8" {W(3)}/>'
    f'<path d="M80 26 Q78 14 81 12 M98 30 Q102 18 104 16" stroke="#D6D6E0" stroke-width="2.4" fill="none"/>'
    f'<path d="M68 52 Q66 30 90 30 Q112 30 110 52 Q110 76 88 76 Q68 76 68 52Z" fill="#B7B7C6" {W(3.4)}/>'
    + face(89, 54, d=9, k=0.8) +
    f'<circle cx="104" cy="88" r="2.4" fill="#B7B7C6"/><circle cx="110" cy="82" r="1.8" fill="#B7B7C6"/>'
    + stars(((24, 30), (50, 16)), 3.2, "#FFFFFF"))

# 8. «Арт Клин» (Клин) — детский рисунок солнышка, приклеенный скотчем к стене-выставке
I["fun-art-klin"] = ("#EAF0FF", "#8C9BE8",
    "детский рисунок кривого солнышка с домиком на тетрадном листке в клетку",
    "приклеен двумя полосками скотча на стену-выставку и гордо улыбается, рядом красная наклейка-звёздочка «молодец»",
    f'<rect x="0" y="0" width="128" height="128" fill="#D8DEFF" opacity=".5"/>'
    f'<rect x="22" y="26" width="80" height="80" rx="2" fill="#FFFFFF" {W(3)} transform="rotate(-4 62 66)"/>'
    + "".join(f'<path d="M{x} 30 V104" stroke="#C9D7FF" stroke-width="1" transform="rotate(-4 62 66)"/>' for x in range(30, 100, 10)) +
    "".join(f'<path d="M26 {y} H98" stroke="#C9D7FF" stroke-width="1" transform="rotate(-4 62 66)"/>' for y in range(36, 104, 10)) +
    f'<rect x="12" y="20" width="28" height="9" fill="#FFF6C8" opacity=".85" transform="rotate(-38 26 24)" {W(1.4)}/>'
    f'<rect x="84" y="20" width="28" height="9" fill="#FFF6C8" opacity=".85" transform="rotate(32 98 24)" {W(1.4)}/>'
    f'<circle cx="60" cy="54" r="14" fill="#FFD23F" stroke="#F09A00" stroke-width="2.6"/>'
    + "".join(f'<path d="M{60 + 18 * dx} {54 + 18 * dy} l{6 * dx} {6 * dy}" stroke="#F09A00" stroke-width="2.6" stroke-linecap="round"/>'
              for dx, dy in ((1, 0), (-1, 0), (0, -1), (0.7, 0.7), (-0.7, 0.7), (0.7, -0.7), (-0.7, -0.7))) +
    face(60, 56, d=7, k=0.6) +
    f'<path d="M36 100 V84 L46 76 L56 84 V100Z" fill="none" stroke="#4FA3E8" stroke-width="2.6"/>'
    f'<path d="M80 100 Q84 88 90 100" fill="none" stroke="#4CC07A" stroke-width="2.6"/>'
    f'<path d="M104 92 L107 99 L114 99 L108 103 L110 110 L104 106 L98 110 L100 103 L94 99 L101 99Z" fill="#FF4D4D" {W(1.8)}/>')

# 9. «Счастье керамика» (Егорьевск) — тарелочка с отпечатком детской ладошки
I["fun-schastye-keramika-egoryevsk"] = ("#FFEFF2", "#E38AA0",
    "круглая глиняная тарелочка цвета сливок с отпечатком детской ладошки в середине",
    "лежит на гончарном столе, ладошку обвели синей глазурью, тарелочка смущённо улыбается краешком",
    f'<rect x="0" y="94" width="128" height="34" fill="#B98258" {W(2.4)}/>'
    f'<ellipse cx="64" cy="70" rx="50" ry="40" fill="#FFF3DC" {W(3.4)}/>'
    f'<ellipse cx="64" cy="70" rx="38" ry="29" fill="#F7E3C2" {W(2.2)}/>'
    f'<path d="M52 92 Q46 78 48 70 L42 52 Q41 46 46 47 L52 62 L50 42 Q50 36 55 37 L58 58 L60 36 Q61 31 66 33 L66 58 '
    f'L70 40 Q72 35 76 38 L72 62 L80 54 Q85 52 85 57 L72 78 Q70 92 60 94Z" fill="#E7C6A0" stroke="#3E7BD8" stroke-width="2.6"/>'
    + eye(40, 92, 0.45) + eye(88, 92, 0.45) +
    f'<path d="M58 104 Q64 108 70 104" fill="none" {W(2)}/>'
    f'<circle cx="34" cy="98" r="3" fill="#FF9DB4" opacity=".7"/><circle cx="94" cy="98" r="3" fill="#FF9DB4" opacity=".7"/>'
    + stars(((16, 20), (110, 18)), 3.2, "#FFFFFF"))

# 10. Мастерская Дарьи Ивановой (Наро-Фоминск) — угольная палочка штрихует шар с тенью
I["fun-masterskaya-ivanovoy-naro-fominsk"] = ("#F2F1EC", "#A9A49A",
    "чёрная палочка рисовального угля с мордашкой",
    "старательно штрихует на листе бумаги шар с падающей тенью, как на академическом рисунке",
    f'<rect x="12" y="30" width="78" height="84" fill="#FFFDF6" {W(3)}/>'
    f'<circle cx="46" cy="70" r="20" fill="none" stroke="#55525A" stroke-width="2.4"/>'
    + "".join(f'<path d="M{46 + i * 3} {58 + i * 2} l10 -6" stroke="#77737E" stroke-width="1.6"/>' for i in range(5)) +
    f'<path d="M30 92 Q48 100 72 92 Q60 88 46 90Z" fill="#9A96A2" opacity=".7"/>'
    f'<path d="M34 64 Q38 56 46 54" fill="none" stroke="#FFFFFF" stroke-width="3"/>'
    f'<path d="M118 14 L82 84" stroke="#3B3355" stroke-width="17" stroke-linecap="round"/>'
    f'<path d="M118 14 L82 84" stroke="#2A2830" stroke-width="12" stroke-linecap="round"/>'
    f'<path d="M86 76 l-6 10 6 -4Z" fill="#111"/>'
    + f'<circle cx="101" cy="39" r="4.5" fill="#fff"/><circle cx="109" cy="45" r="4.5" fill="#fff"/>'
    + eye(101, 39, 0.5) + eye(109, 45, 0.5) +
    f'<path d="M98 52 Q101 56 105 53" fill="none" stroke="#FFFFFF" stroke-width="1.8"/>'
    f'<circle cx="80" cy="96" r="1.6" fill="#2A2830"/><circle cx="74" cy="102" r="1.2" fill="#2A2830"/>'
    + stars(((22, 18), (60, 14)), 3, "#FFFFFF"))

# --- пеленальные ---
# 11. Филатов луг — плюшевый слоник-комфортер на лугу тянет хобот к бабочке
I["chg-filatov-lug"] = ("#F2FFE6", "#8CCB5E",
    "плюшевый слоник-комфортер — мягкий сиреневый платочек с головой слонёнка",
    "лежит на лугу среди ромашек и тянет хобот к порхающей жёлтой бабочке",
    f'<path d="M0 92 Q64 80 128 92 V128 H0Z" fill="#6DBE45"/>'
    f'<path d="M20 100 Q40 80 64 86 Q92 80 110 100 Q100 116 64 114 Q28 116 20 100Z" fill="#CDB8F5" {W(3)}/>'
    + "".join(f'<path d="M{x} {y} l-6 8 M{x} {y} l6 8" stroke="#3B3355" stroke-width="2"/>' for x, y in ((22, 100), (108, 100))) +
    f'<ellipse cx="38" cy="62" rx="12" ry="16" fill="#B49CF0" {W(3)}/><ellipse cx="86" cy="62" rx="12" ry="16" fill="#B49CF0" {W(3)}/>'
    f'<circle cx="62" cy="64" r="22" fill="#CDB8F5" {W(3.2)}/>'
    f'<path d="M62 74 Q62 88 74 84 Q86 78 84 56 Q88 46 94 42" fill="none" stroke="#3B3355" stroke-width="10" stroke-linecap="round"/>'
    f'<path d="M62 74 Q62 88 74 84 Q86 78 84 56 Q88 46 94 42" fill="none" stroke="#CDB8F5" stroke-width="6" stroke-linecap="round"/>'
    + eye(54, 60, 0.55) + eye(70, 60, 0.55) +
    f'<circle cx="48" cy="70" r="3" fill="#FF9DB4" opacity=".7"/>'
    f'<path d="M98 30 q-8 -10 -12 0 q4 8 12 0 q8 -10 12 0 q-4 8 -12 0Z" fill="#FFD23F" {W(2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#fff" {W(1.4)}/><circle cx="{x}" cy="{y}" r="1.5" fill="#FFC531"/>' for x, y in ((12, 110), (116, 112), (66, 122))))

# 12. Царицыно — варежки-царапки на бархатной подушке под короной
I["chg-tsaritsyno"] = ("#FFE9EE", "#B8405E",
    "пара крошечных белых варежек-царапок для новорождённого с розовыми резиночками",
    "лежат на красной бархатной подушечке с кистями под маленькой золотой короной, как царские регалии",
    f'<path d="M14 92 Q14 78 30 78 H98 Q114 78 114 92 Q114 108 98 108 H30 Q14 108 14 92Z" fill="#C8243E" {W(3)}/>'
    f'<path d="M14 92 l-6 8 M114 92 l6 8" stroke="#FFC531" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M30 82 Q28 56 44 54 Q60 54 58 82Z" fill="#FFFFFF" {W(3)}/><rect x="30" y="80" width="28" height="6" rx="3" fill="#FF9DB4" {W(2)}/>'
    f'<path d="M70 82 Q68 56 84 54 Q100 54 98 82Z" fill="#FFFFFF" {W(3)}/><rect x="70" y="80" width="28" height="6" rx="3" fill="#FF9DB4" {W(2)}/>'
    + face(44, 68, d=6, k=0.55) + face(84, 68, d=6, k=0.55) +
    f'<path d="M48 40 L52 22 L60 32 L64 18 L68 32 L76 22 L80 40Z" fill="#FFC531" {W(2.6)}/>'
    f'<circle cx="64" cy="34" r="3" fill="#FF4F8B"/>'
    + stars(((22, 30), (106, 34)), 3.2, "#FFE98A"))

# 13. Шишкин лес — комбинезон-медвежонок сушится на сосновой ветке
I["chg-shishkin-les-istra"] = ("#E6F4E8", "#3E7D52",
    "детский флисовый комбинезон коричневого цвета с медвежьими ушками на капюшоне",
    "висит на сосновой ветке в лесу и болтает пустыми рукавами и штанишками",
    f'<path d="M0 26 Q60 34 128 22" stroke="#7A4E2A" stroke-width="7" fill="none"/>'
    + "".join(f'<path d="M{x} {y} l-6 -8 M{x} {y} l6 -8 M{x} {y} l0 -10" stroke="#2F7A44" stroke-width="2.4"/>' for x, y in ((14, 28), (104, 26), (120, 22))) +
    f'<path d="M64 28 V40" stroke="#3B3355" stroke-width="2.4"/>'
    f'<circle cx="50" cy="44" r="6" fill="#9B6234" {W(2.6)}/><circle cx="78" cy="44" r="6" fill="#9B6234" {W(2.6)}/>'
    f'<circle cx="64" cy="56" r="16" fill="#B07443" {W(3)}/><circle cx="64" cy="58" r="10" fill="#F3D9B8" {W(2)}/>'
    + face(64, 58, d=6, k=0.55) +
    f'<path d="M48 70 H80 L94 92 L86 96 L78 84 L80 116 H68 L64 100 L60 116 H48 L50 84 L42 96 L34 92Z" fill="#B07443" {W(3)}/>'
    f'<path d="M64 74 V100" stroke="#7A4E2A" stroke-width="2"/>'
    f'<path d="M10 128 L22 96 L34 128Z M100 128 L112 92 L124 128Z" fill="#2F7A44" {W(2)}/>')

# 14. Опалиха — полосатые носочки-первоноски сушатся на верёвочке между берёзками
I["chg-opalikha-krasnogorsk"] = ("#FFFBE8", "#E8D07A",
    "пара крошечных носочков-первоносков в красно-белую полоску",
    "сушатся на верёвочке на деревянных прищепках между двух берёзок",
    f'<rect x="8" y="16" width="10" height="112" fill="#FFFFFF" {W(2.4)}/><rect x="110" y="12" width="10" height="116" fill="#FFFFFF" {W(2.4)}/>'
    + "".join(f'<path d="M{x} {y} h6" stroke="#3B3355" stroke-width="2.4"/>' for x, y in ((9, 40), (11, 70), (111, 36), (113, 80))) +
    f'<path d="M18 40 Q64 58 110 36" fill="none" stroke="#3B3355" stroke-width="2"/>'
    f'<path d="M38 50 V82 Q38 92 48 92 H58 Q62 92 62 86 Q62 80 54 80 V52Z" fill="#FFFFFF" {W(3)}/>'
    + "".join(f'<path d="M38 {y} H54" stroke="#F04848" stroke-width="4"/>' for y in (58, 66, 74)) +
    f'<path d="M72 52 V84 Q72 94 82 94 H92 Q96 94 96 88 Q96 82 88 82 V50Z" fill="#FFFFFF" {W(3)}/>'
    + "".join(f'<path d="M72 {y} H88" stroke="#F04848" stroke-width="4"/>' for y in (60, 68, 76)) +
    f'<rect x="42" y="42" width="6" height="14" rx="2" fill="#D9A06A" {W(1.8)}/><rect x="77" y="42" width="6" height="14" rx="2" fill="#D9A06A" {W(1.8)}/>'
    + face(47, 84, d=5, k=0.45) + face(81, 86, d=5, k=0.45) +
    "".join(f'<ellipse cx="{x}" cy="{y}" rx="5" ry="3" fill="#8BCB4C" {W(1.4)}/>' for x, y in ((24, 20), (30, 28), (104, 18), (98, 26))))

# 15. Олонецкий сквер — контейнер-дозатор для сухой смеси вертится каруселькой
I["chg-olonetsky-skver"] = ("#E8F6FF", "#5CA8E0",
    "прозрачный контейнер-дозатор для детской смеси с тремя отделениями-лепестками и носиком",
    "кружится, как карусель, а из носика сыплется белая смесь прямо в горлышко бутылочки внизу",
    f'<circle cx="64" cy="50" r="36" fill="#FFFFFF" opacity=".75" {W(3.4)}/>'
    f'<path d="M64 50 L64 14 M64 50 L95 68 M64 50 L33 68" stroke="#3B3355" stroke-width="3"/>'
    f'<path d="M64 50 L64 14 A36 36 0 0 1 95 68Z" fill="#FFF1B8" opacity=".9"/>'
    f'<path d="M64 50 L95 68 A36 36 0 0 1 33 68Z" fill="#FFD9E6" opacity=".9"/>'
    f'<path d="M64 50 L33 68 A36 36 0 0 1 64 14Z" fill="#D7F0FF" opacity=".9"/>'
    f'<circle cx="64" cy="50" r="36" fill="none" {W(3.4)}/>'
    f'<rect x="58" y="84" width="12" height="10" fill="#9FD3F5" {W(2.4)}/>'
    + face(64, 46, d=9, k=0.75) +
    f'<path d="M14 40 q-4 -10 6 -14 M114 40 q4 -10 -6 -14" fill="none" stroke="#3B3355" stroke-width="2.4" stroke-linecap="round"/>'
    + "".join(f'<circle cx="{64 + dx}" cy="{y}" r="1.6" fill="#FFFFFF" {W(0.8)}/>' for dx, y in ((-2, 98), (2, 102), (0, 106))) +
    f'<path d="M56 110 H72 V128 H56Z" fill="#FFFFFF" {W(2.6)}/>')

# 16. Томилинский лесопарк — мягкие наколенники для ползунков ползут по тропинке
I["chg-tomilinsky-lesopark"] = ("#F6EEDC", "#9C8452",
    "пара мягких детских наколенников для ползания с противоскользящими кружочками",
    "ползут друг за другом по лесной тропинке между сосновых шишек, оставляя следы-кружочки",
    f'<path d="M-4 96 Q64 70 132 96 V128 H-4Z" fill="#D8B988" {W(2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.4" fill="#A88B58"/>' for x, y in ((14, 104), (22, 100), (30, 98), (38, 96))) +
    f'<rect x="40" y="52" width="34" height="40" rx="14" fill="#FF8C5A" {W(3)}/>'
    f'<rect x="78" y="62" width="34" height="40" rx="14" fill="#5BC0EB" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#FFFFFF" {W(1)}/>' for x, y in ((50, 80), (58, 84), (66, 80), (88, 90), (96, 94), (104, 90))) +
    f'<path d="M40 64 H74 M78 74 H112" stroke="#3B3355" stroke-width="2"/>'
    + face(57, 70, d=6, k=0.55) + face(95, 80, d=6, k=0.55) +
    f'<ellipse cx="18" cy="76" rx="7" ry="10" fill="#8B5A2B" {W(2)}/><path d="M12 72 h12 M12 78 h12 M13 84 h10" stroke="#5E3A1A" stroke-width="1.4"/>'
    f'<path d="M100 20 L112 46 H88Z M100 32 L110 54 H90Z" fill="#3E8A55" {W(2)}/>')

# 17. Подольск, бульвар — зонтик-трость для коляски раскрылся над скамейкой
I["chg-podolsk-bulvar-pobedy"] = ("#EFF0FF", "#7D7FD8",
    "складной детский зонтик для коляски в мятный горошек с гибкой ножкой-прищепкой",
    "раскрылся над бульварной скамейкой и укрывает её от падающих капелек",
    f'<rect x="20" y="96" width="88" height="8" rx="3" fill="#C98A5A" {W(2.4)}/><rect x="20" y="84" width="88" height="7" rx="3" fill="#C98A5A" {W(2.4)}/>'
    f'<path d="M28 104 V120 M100 104 V120" stroke="#3B3355" stroke-width="4"/>'
    f'<path d="M64 46 Q60 66 70 70 Q78 74 74 84" fill="none" stroke="#3B3355" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M64 46 Q60 66 70 70 Q78 74 74 84" fill="none" stroke="#B0B4C8" stroke-width="2.4" stroke-linecap="round"/>'
    f'<rect x="68" y="82" width="12" height="8" rx="2" fill="#FF8FB1" {W(2)}/>'
    f'<path d="M18 46 Q22 12 64 10 Q106 12 110 46 Q100 40 92 46 Q82 38 72 46 Q64 40 56 46 Q46 38 36 46 Q28 40 18 46Z" fill="#7FE0C4" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3.4" fill="#FFFFFF"/>' for x, y in ((40, 26), (64, 20), (88, 26), (52, 36), (76, 36))) +
    face(64, 30, d=7, k=0.6) +
    "".join(f'<path d="M{x} {y} q-3 5 0 7 q3 -2 0 -7Z" fill="#6FA8FF" {W(1.2)}/>' for x, y in ((10, 60), (118, 62), (8, 90), (120, 92))))

# 18. «Лента» (Домодедово) — баночка детского пюре с ложечкой
I["chg-lenta-domodedovo"] = ("#FFF4E0", "#F2A43A",
    "стеклянная баночка детского яблочно-грушевого пюре с синей крышкой и наклейкой-грушей",
    "открыла крышку-шляпу, а маленькая ложечка сама зачерпнула пюре и дует на него",
    f'<rect x="0" y="104" width="128" height="24" fill="#E07A2A" opacity=".5"/>'
    f'<path d="M34 50 H90 V100 Q90 110 80 110 H44 Q34 110 34 100Z" fill="#FFFFFF" opacity=".75" {W(3.2)}/>'
    f'<path d="M36 58 H88 V100 Q88 108 80 108 H44 Q36 108 36 100Z" fill="#F7DE7A"/>'
    f'<path d="M34 50 H90 V100 Q90 110 80 110 H44 Q34 110 34 100Z" fill="none" {W(3.2)}/>'
    f'<rect x="42" y="70" width="40" height="30" rx="6" fill="#FFFFFF" {W(2)}/>'
    f'<path d="M62 76 Q54 82 56 92 Q62 98 68 92 Q70 82 62 76Z" fill="#A6D65C" {W(1.8)}/><path d="M62 76 l2 -4" stroke="#3B3355" stroke-width="1.8"/>'
    f'<path d="M24 40 Q30 20 54 30 L36 52Z" fill="#3F7FE0" {W(3)} transform="rotate(-8 40 40)"/>'
    f'<path d="M104 18 L76 52" stroke="#C0C4D6" stroke-width="5" stroke-linecap="round"/><ellipse cx="74" cy="56" rx="9" ry="6" fill="#C0C4D6" {W(2.2)} transform="rotate(-40 74 56)"/>'
    f'<ellipse cx="74" cy="55" rx="5" ry="3" fill="#F7DE7A" transform="rotate(-40 74 55)"/>'
    + face(62, 62, d=8, k=0.65) +
    f'<path d="M84 44 q6 -4 10 0 M86 38 q6 -4 10 0" fill="none" stroke="#9AA" stroke-width="1.8" stroke-linecap="round"/>')

if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
