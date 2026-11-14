"""Иконки робота fun (2026-11-14, проход 1114q): места из tools/add_fun_1114q.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя компоновка и палитра фона.
Запуск: python3 tools/icons_fun_1114q.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
O = "#3B3355"
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}

# 1. Музей хлеба (Серпухов): румяная плетёная хала с глазками держит на руках маленький бублик, как младшего брата
I["fun-muzey-khleba-serpukhov"] = ("#FFF4DC", "#E8B866",
    "румяная плетёная хала с глазками и румянцем",
    "бережно держит на руках маленький бублик с маком, сверху сыплется мука звёздочками",
    f'<path d="M14 96 Q64 120 114 96 L114 104 Q64 128 14 104Z" fill="#B5793F" {W(2.6)}/>'
    + f'<path d="M18 92 Q20 62 44 58 Q64 46 84 58 Q108 62 110 92 Q64 112 18 92Z" fill="#E7A24E" {W(3)}/>'
    + f'<path d="M34 66 Q46 84 40 98 M58 56 Q66 78 60 104 M82 58 Q90 80 86 100" fill="none" stroke="#B5793F" stroke-width="3" stroke-linecap="round"/>'
    + f'<path d="M30 74 Q38 70 46 76 M52 66 Q62 62 70 68 M76 70 Q86 66 94 74" fill="none" stroke="#F6D49A" stroke-width="2.4" stroke-linecap="round"/>'
    + face(64, 82, d=11, k=.8)
    + f'<circle cx="64" cy="40" r="15" fill="#D98E3E" {W(2.8)}/><circle cx="64" cy="40" r="5.5" fill="#FFF4DC" {W(2.2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1.2" fill="{O}"/>' for x, y in ((56, 32), (70, 31), (74, 42), (55, 46), (66, 50), (58, 38)))
    + f'<path d="M40 70 Q46 52 52 44 M88 70 Q82 52 76 44" fill="none" stroke="#B5793F" stroke-width="5" stroke-linecap="round"/>'
    + sparkle(24, 30, 6) + sparkle(104, 24, 5) + sparkle(98, 44, 3.5))

# 2. Музей РВСН (Власиха): стратегическая ракета на зелёном многоосном тягаче смотрит в небо, а над ней — генеральская звезда
I["fun-muzey-rvsn-vlasikha"] = ("#E4EEF8", "#7E9BB8",
    "белая стратегическая ракета с глазками на зелёном восьмиколёсном тягаче",
    "приподнялась на тягаче и гордо смотрит в небо, где сияет красная звезда",
    f'<rect x="-4" y="108" width="136" height="24" fill="#8DB36C"/>'
    + f'<rect x="10" y="84" width="104" height="18" rx="5" fill="#5B7B3A" {W(2.8)}/>'
    + f'<path d="M96 84 L96 70 L116 70 L118 84Z" fill="#6E8F45" {W(2.6)}/><rect x="101" y="73" width="11" height="7" fill="#BFE3F5" {W(1.8)}/>'
    + "".join(f'<circle cx="{x}" cy="104" r="7" fill="#3B3B3B" {W(2.2)}/><circle cx="{x}" cy="104" r="2.4" fill="#9A9A9A"/>' for x in (20, 36, 52, 68, 84, 104))
    + f'<g transform="rotate(32 52 84)"><rect x="42" y="20" width="20" height="66" rx="3" fill="#F4F4F0" {W(3)}/>'
    + f'<path d="M42 20 Q52 -2 62 20Z" fill="#E8483A" {W(2.8)}/><path d="M42 78 L34 90 L42 86Z M62 78 L70 90 L62 86Z" fill="#7D8A99" {W(2.2)}/>'
    + f'<rect x="42" y="58" width="20" height="5" fill="#5B7B3A"/>' + face(52, 40, d=5, k=.55) + '</g>'
    + f'<path d="M30 18 l4 9 l10 1 l-7.5 6.5 l2.5 10 l-9 -5.5 l-9 5.5 l2.5 -10 l-7.5 -6.5 l10 -1Z" fill="#E8483A" {W(2.2)}/>')

# 3. Коломенский навигатор: медная подзорная труба-путешественница на стопке старых карт, рядом коломенская пастила-флажок
I["fun-kolomenskiy-navigator"] = ("#FBEFE0", "#C98E62",
    "медная подзорная труба-путешественница в треуголке",
    "лежит на свёрнутой старинной карте Коломны и разглядывает кремлёвскую башню вдали",
    f'<path d="M-4 104 L132 98 L132 132 L-4 132Z" fill="#E9D3A6" {W(2.4)}/>'
    + f'<path d="M84 32 L84 70 L110 70 L110 32 L104 22 L97 32 L90 22Z" fill="#C2483C" {W(2.6)}/>'
    + f'<path d="M84 32 L110 32" stroke="{O}" stroke-width="2.4"/><rect x="93" y="54" width="8" height="16" rx="4" fill="#5A2E25"/>'
    + f'<path d="M97 22 L97 12 L106 15 L97 18" fill="#F7C02F" {W(1.8)}/>'
    + f'<rect x="10" y="84" width="74" height="20" rx="10" fill="#F4E3B8" {W(2.6)}/><circle cx="12" cy="94" r="10" fill="#E2C98F" {W(2.4)}/>'
    + f'<path d="M30 88 Q44 96 54 88 Q64 82 72 94" fill="none" stroke="#B5793F" stroke-width="2" stroke-dasharray="3 3"/>'
    + f'<g transform="rotate(-18 50 66)"><rect x="18" y="56" width="26" height="20" rx="4" fill="#C9782F" {W(2.8)}/>'
    + f'<rect x="42" y="59" width="22" height="14" rx="3" fill="#E39A43" {W(2.6)}/><rect x="62" y="61" width="14" height="10" rx="2" fill="#F2B95C" {W(2.4)}/>'
    + f'<ellipse cx="78" cy="66" rx="3.5" ry="6" fill="#BFE3F5" {W(2.2)}/>' + face(31, 64, d=5.5, k=.55) + '</g>'
    + f'<path d="M14 50 L40 38 L44 52Z" fill="#2F3A56" {W(2.4)}/><circle cx="34" cy="44" r="2.4" fill="#F7C02F"/>')

# 4. Железное царство: железный дракончик... нет — сварной ёж из гаек и шестерёнок, на спине искры сварки
I["fun-zheleznoe-tsarstvo"] = ("#EEF0F2", "#8C97A3",
    "сварной железный ёж из гаек, шестерёнок и подков",
    "сидит на наковальне, а на его колючках вспыхивают оранжевые искры сварки",
    f'<path d="M30 100 L98 100 L90 112 L102 122 L26 122 L38 112Z" fill="#4A4F57" {W(3)}/>'
    + f'<path d="M24 100 Q20 86 34 86 L104 86 Q116 90 104 100Z" fill="#646B75" {W(2.8)}/>'
    + "".join(f'<path d="M{x} {y} l{dx} {dy} l6 4Z" fill="#9AA3AD" {W(2)}/>' for x, y, dx, dy in
              ((36, 62, -12, -8), (44, 50, -8, -14), (56, 42, -2, -16), (70, 40, 6, -15), (82, 46, 12, -10), (90, 58, 14, -4)))
    + f'<ellipse cx="62" cy="68" rx="32" ry="20" fill="#7E8892" {W(3)}/>'
    + f'<circle cx="52" cy="62" r="7" fill="#B9C1C9" {W(2.2)}/><circle cx="52" cy="62" r="2.6" fill="#4A4F57"/>'
    + f'<path d="M66 54 l3 -4 l3 4 l5 0 l-1 5 l4 3 l-4 3 l1 5 l-5 0 l-3 4 l-3 -4 l-5 0 l1 -5 l-4 -3 l4 -3 l-1 -5Z" fill="#C9A44A" {W(1.8)}/>'
    + f'<path d="M38 74 Q30 64 40 60" fill="none" stroke="#C8CDD2" stroke-width="4" stroke-linecap="round"/>'
    + f'<path d="M86 64 Q104 66 104 74 Q96 80 86 78Z" fill="#B9C1C9" {W(2.6)}/><circle cx="105" cy="73" r="3" fill="{O}"/>'
    + eye(92, 68, .6)
    + f'<path d="M50 86 L48 94 M76 86 L78 94" stroke="{O}" stroke-width="3.4" stroke-linecap="round"/>'
    + sparkle(30, 30, 7, "#FF9A2E") + sparkle(98, 26, 5, "#FFD23F") + sparkle(108, 44, 3.5, "#FF9A2E"))

# 5. Наро-Фоминский историко-краеведческий музей: древний глиняный горшок с узором-ёлочкой, из него выглядывает наконечник стрелы-находки и монетка
I["fun-naro-fominsk-museum"] = ("#F3EEE6", "#A9B98E",
    "древний глиняный горшок с узором-ёлочкой и глазками",
    "стоит на витринной подставке под стеклянным колпаком, а рядом лупа разглядывает старинную монетку",
    f'<path d="M14 108 L114 108 L106 120 L22 120Z" fill="#8A5A36" {W(2.6)}/>'
    + f'<path d="M22 108 L22 30 Q64 10 106 30 L106 108" fill="#DDEEF3" opacity=".55" {W(2.6)}/>'
    + f'<path d="M30 34 Q64 20 98 34" fill="none" stroke="#fff" stroke-width="3" opacity=".8"/>'
    + f'<path d="M44 52 Q40 46 46 42 L82 42 Q88 46 84 52 Q100 66 94 86 Q88 106 64 106 Q40 106 34 86 Q28 66 44 52Z" fill="#B9673A" {W(3)}/>'
    + f'<path d="M46 42 L82 42" stroke="{O}" stroke-width="2.6"/>'
    + "".join(f'<path d="M{x} 60 l5 6 l5 -6 M{x} 92 l5 -6 l5 6" fill="none" stroke="#6E3A1E" stroke-width="2.2"/>' for x in (40, 52, 64, 76))
    + face(64, 74, d=10, k=.7)
    + f'<circle cx="104" cy="92" r="6" fill="#E9C46A" {W(2)}/><circle cx="96" cy="82" r="9" fill="#BFE3F5" opacity=".7" {W(2.4)}/>'
    + f'<path d="M89 75 L80 66" stroke="#5A3A22" stroke-width="5" stroke-linecap="round"/>')

# 6. Музей микроэлектроники (Зеленоград): микросхема-жучок на ножках-выводах шагает по печатной плате, на спине горит светодиод
I["fun-muzey-mikroelektroniki"] = ("#E6F6EE", "#3E9A73",
    "чёрная микросхема-жучок на серебряных ножках-выводах",
    "бодро шагает по зелёной печатной плате с медными дорожками, на макушке у неё мигает красный светодиод",
    f'<path d="M-4 96 L132 96 L132 132 L-4 132Z" fill="#2E7D55"/>'
    + f'<path d="M6 108 L30 108 L38 116 L70 116 M90 104 L110 104 L118 112 M50 124 L80 124" fill="none" stroke="#E0A23A" stroke-width="3"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#F2C35E" {W(1.6)}/>' for x, y in ((6, 108), (70, 116), (118, 112), (50, 124)))
    + "".join(f'<path d="M{x} 82 L{x+(x-64)*.2:.0f} 98" stroke="#C8CDD2" stroke-width="3.6" stroke-linecap="round"/>' for x in (36, 48, 60, 72, 84, 94))
    + f'<rect x="28" y="40" width="72" height="44" rx="5" fill="#26262E" {W(3)}/>'
    + f'<circle cx="38" cy="50" r="3" fill="#55556A"/>'
    + face(64, 60, d=11, k=.75)
    + '<text x="46" y="80" font-family="Arial" font-weight="700" font-size="7" fill="#8E8EA6">K1810</text>'
    + f'<path d="M64 40 L64 28" stroke="#C8CDD2" stroke-width="3"/><path d="M57 28 Q57 14 64 14 Q71 14 71 28Z" fill="#FF4A3D" {W(2.4)}/>'
    + f'<path d="M50 14 L44 8 M78 14 L84 8 M64 8 L64 2" stroke="#FF4A3D" stroke-width="2.4" stroke-linecap="round"/>')

# 7. Экодеревушка (Парфентьево): енот-полоскун в соломенной шляпке полощет морковку в деревянной кадке
I["fun-ekoderevushka-parfentyevo"] = ("#F2F7E4", "#9CC07A",
    "енот-полоскун в соломенной шляпке",
    "по-деревенски полощет морковку в деревянной кадке с водой у плетня",
    f'<path d="M-4 52 L132 52" stroke="#A47B4E" stroke-width="3"/><path d="M-4 66 L132 66" stroke="#A47B4E" stroke-width="3"/>'
    + "".join(f'<rect x="{x}" y="40" width="7" height="40" rx="3" fill="#C49A63" {W(1.8)}/>' for x in (2, 22, 102, 120))
    + f'<path d="M38 92 L90 92 L86 122 L42 122Z" fill="#B07A45" {W(3)}/><path d="M40 102 L88 102 M41 114 L87 114" stroke="#6E4A2A" stroke-width="3"/>'
    + f'<ellipse cx="64" cy="92" rx="26" ry="6" fill="#7EC8EA" {W(2.6)}/>'
    + f'<path d="M58 88 L74 96" stroke="#F08A2E" stroke-width="6" stroke-linecap="round"/><path d="M74 96 l6 -2 l-3 5Z" fill="#4FB35A"/>'
    + f'<ellipse cx="64" cy="58" rx="24" ry="20" fill="#9A9AA2" {W(3)}/>'
    + f'<path d="M44 56 Q64 46 84 56 Q80 66 64 64 Q48 66 44 56Z" fill="#3B3B44"/>'
    + face(64, 58, d=10, k=.7, blush=False)
    + f'<ellipse cx="64" cy="70" rx="9" ry="6" fill="#E7E7EC" {W(2)}/><ellipse cx="64" cy="67" rx="3" ry="2.2" fill="{O}"/>'
    + f'<path d="M44 82 Q52 92 58 88 M84 82 Q76 92 70 92" fill="none" stroke="#9A9AA2" stroke-width="7" stroke-linecap="round"/>'
    + f'<ellipse cx="64" cy="38" rx="30" ry="6" fill="#F2D27A" {W(2.6)}/><path d="M48 38 Q50 20 64 20 Q78 20 80 38Z" fill="#EAC35E" {W(2.6)}/>'
    + f'<path d="M50 32 L78 32" stroke="#E8483A" stroke-width="3.4"/>')

# 9. Курский вокзал: паровозик-малыш в слюнявчике пыхтит по рельсам, из трубы — мыльные пузыри вместо дыма
I["chg-kursky-vokzal"] = ("#EAF2FF", "#7FA6DC",
    "синий паровозик-малыш в слюнявчике с вишенкой",
    "пыхтит по рельсам, а из трубы вместо дыма вылетают радужные мыльные пузыри",
    f'<path d="M-4 108 L132 108" stroke="#8A6A4A" stroke-width="4"/>'
    + "".join(f'<rect x="{x}" y="108" width="6" height="10" fill="#8A6A4A"/>' for x in (6, 30, 54, 78, 102, 122))
    + f'<rect x="20" y="62" width="62" height="32" rx="8" fill="#2F6FD0" {W(3)}/>'
    + f'<rect x="72" y="44" width="34" height="50" rx="6" fill="#3E86E8" {W(3)}/><rect x="78" y="50" width="22" height="16" rx="3" fill="#FFF6D6" {W(2.2)}/>'
    + f'<rect x="30" y="42" width="12" height="20" fill="#2A2F45" {W(2.6)}/><rect x="26" y="38" width="20" height="6" rx="2" fill="#2A2F45" {W(2.2)}/>'
    + "".join(f'<circle cx="{x}" cy="100" r="{r}" fill="#E8483A" {W(2.6)}/><circle cx="{x}" cy="100" r="2.4" fill="#fff"/>' for x, r in ((34, 9), (58, 9), (90, 11)))
    + face(48, 76, d=8, k=.6)
    + f'<path d="M38 84 Q48 96 58 84Z" fill="#fff" {W(2)}/><circle cx="48" cy="88" r="2.4" fill="#E8483A"/>'
    + f'<circle cx="38" cy="24" r="8" fill="#DDF3FF" opacity=".8" {W(2)}/><circle cx="56" cy="14" r="6" fill="#FFE3F2" opacity=".8" {W(2)}/><circle cx="20" cy="12" r="5" fill="#E9FFD9" opacity=".8" {W(2)}/>'
    + sparkle(36, 21, 2.5) + sparkle(54, 12, 2))

# 10. Казанский вокзал: вокзальные часы-кругляш с пустышкой во рту дремлют на башенке со шпилем
I["chg-kazansky-vokzal"] = ("#F4ECFF", "#9C86C9",
    "круглые вокзальные часы со стрелками-ресничками и пустышкой во рту",
    "дремлют на зелёной башенке со шпилем, вокруг ночные звёздочки",
    f'<path d="M34 128 L34 70 L94 70 L94 128Z" fill="#E9DCC4" {W(3)}/><path d="M28 70 L64 50 L100 70Z" fill="#3E8E5E" {W(3)}/>'
    + f'<path d="M64 50 L64 20" stroke="{O}" stroke-width="3"/><path d="M58 30 L64 14 L70 30Z" fill="#F7C02F" {W(2.2)}/>'
    + f'<rect x="54" y="104" width="20" height="24" rx="10" fill="#7A4A2A" {W(2.4)}/>'
    + f'<circle cx="64" cy="82" r="22" fill="#FFFDF5" {W(3.2)}/>'
    + "".join(f'<circle cx="{64+18*c:.1f}" cy="{82+18*s_:.1f}" r="1.6" fill="{O}"/>' for c, s_ in ((1, 0), (-1, 0), (0, 1), (0, -1)))
    + f'<path d="M54 78 Q58 82 62 78 M66 78 Q70 82 74 78" fill="none" stroke="{O}" stroke-width="2.4" stroke-linecap="round"/>'
    + f'<ellipse cx="64" cy="92" rx="9" ry="5" fill="#7FC8F0" {W(2.2)}/><circle cx="64" cy="92" r="3" fill="#F28AB8" {W(1.8)}/>'
    + sparkle(18, 36, 6, "#FFE88A") + sparkle(108, 30, 5, "#FFE88A") + sparkle(102, 54, 3, "#FFE88A")
    + '<text x="90" y="46" font-family="Arial" font-weight="700" font-size="12" fill="#fff">z</text>')

# 11. Ярославский вокзал: медвежонок в чепчике лежит на пеленальном столике и болтает лапами
I["chg-yaroslavsky-vokzal"] = ("#FFF1E4", "#E39A6A",
    "бурый медвежонок в кружевном чепчике",
    "лежит на спинке на пеленальном столике и весело болтает лапками в воздухе",
    f'<rect x="12" y="84" width="104" height="14" rx="4" fill="#F7F1E6" {W(3)}/>'
    + f'<rect x="18" y="98" width="8" height="30" fill="#C49A63" {W(2.4)}/><rect x="102" y="98" width="8" height="30" fill="#C49A63" {W(2.4)}/>'
    + f'<rect x="16" y="76" width="96" height="10" rx="5" fill="#A8DDF5" {W(2.4)}/>'
    + f'<ellipse cx="70" cy="66" rx="30" ry="15" fill="#9A6A42" {W(3)}/>'
    + f'<path d="M84 56 L94 36 M92 60 L106 44 M56 56 L50 36 M48 62 L36 48" stroke="#9A6A42" stroke-width="9" stroke-linecap="round"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="#6E4A2E" {W(2)}/>' for x, y in ((94, 36), (106, 44), (50, 36), (36, 48)))
    + f'<circle cx="34" cy="64" r="18" fill="#A87448" {W(3)}/>'
    + f'<path d="M14 62 Q18 40 36 42 Q52 44 52 60 Q44 50 34 50 Q22 52 14 62Z" fill="#fff" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="#fff" {W(1.2)}/>' for x, y in ((16, 58), (22, 47), (32, 43), (43, 45), (50, 53)))
    + face(34, 66, d=6, k=.55)
    + f'<ellipse cx="34" cy="74" rx="5" ry="3.4" fill="#E8C9A8" {W(1.6)}/>')

# 12. Ленинградский вокзал: разводной мостик бережно качает в пролёте колыбельку над синей Невой
I["chg-leningradsky-vokzal"] = ("#E6EEFA", "#5E79B8",
    "чугунный разводной мостик с фонариками",
    "приподнял обе половинки и качает на цепочках колыбельку над синей рекой под белой ночью",
    f'<rect x="-4" y="96" width="136" height="36" fill="#3A6FC2"/>'
    + f'<path d="M6 104 Q20 100 34 104 M60 112 Q76 108 92 112 M100 102 Q112 98 124 102" fill="none" stroke="#A8D4FF" stroke-width="2.4"/>'
    + f'<path d="M-4 86 L30 86 L30 96 L-4 96Z M98 86 L132 86 L132 96 L98 96Z" fill="#7A869A" {W(2.6)}/>'
    + f'<path d="M30 88 L58 52 L62 56 L34 92Z" fill="#4A5266" {W(2.6)}/><path d="M98 88 L70 52 L66 56 L94 92Z" fill="#4A5266" {W(2.6)}/>'
    + f'<path d="M14 86 L14 64 M114 86 L114 64" stroke="{O}" stroke-width="3"/><circle cx="14" cy="60" r="5" fill="#FFD95A" {W(2)}/><circle cx="114" cy="60" r="5" fill="#FFD95A" {W(2)}/>'
    + f'<path d="M56 56 L54 70 M72 56 L74 70" stroke="{O}" stroke-width="1.8"/>'
    + f'<path d="M46 70 Q64 92 82 70Z" fill="#F7E2B6" {W(2.6)}/><path d="M48 70 L80 70" stroke="#E8A0B8" stroke-width="4"/>'
    + f'<circle cx="64" cy="72" r="6" fill="#F6D2B5" {W(1.8)}/><path d="M61 72 q1.5 1.5 3 0 M65 72 q1.5 1.5 3 0" fill="none" stroke="{O}" stroke-width="1.2"/>'
    + f'<circle cx="98" cy="22" r="10" fill="#FFF7D6" {W(2)}/>'
    + face(46, 70, d=0.01, k=.01, mouth=False, blush=False) * 0)

# 13. Белорусский вокзал: аист в фуражке проводника несёт в клюве свёрток с малышом над рельсами
I["chg-belorussky-vokzal"] = ("#F2FAF2", "#8CC59A",
    "белый аист в фуражке проводника",
    "летит над рельсами и несёт в клюве голубой свёрток с улыбающимся малышом",
    f'<path d="M-4 118 L132 118 M-4 124 L132 124" stroke="#8A6A4A" stroke-width="3"/>'
    + '<g transform="translate(14 8)">' + f'<path d="M18 62 Q40 40 70 54 Q90 30 116 36 Q96 44 92 58 Q80 78 52 76 Q30 76 18 62Z" fill="#fff" {W(3)}/>'
    + f'<path d="M92 58 Q104 46 116 36 Q110 54 96 62Z" fill="#2E2E36"/>'
    + f'<path d="M44 76 L40 94 M54 76 L54 96" stroke="#E8483A" stroke-width="3"/>'
    + f'<circle cx="22" cy="54" r="11" fill="#fff" {W(3)}/>'
    + f'<path d="M12 54 L-2 64 L12 60Z" fill="#E8483A" {W(2.2)}/>' + eye(20, 51, .55)
    + f'<path d="M12 44 Q22 36 32 44 L30 48 L14 48Z" fill="#2F4A7A" {W(2)}/><rect x="10" y="47" width="22" height="3" fill="#F7C02F"/>'
    + f'<path d="M4 64 L4 72" stroke="{O}" stroke-width="2"/>'
    + f'<path d="M-6 72 Q4 66 14 72 Q16 92 4 96 Q-8 92 -6 72Z" fill="#8FC8F5" {W(2.6)}/>'
    + f'<circle cx="4" cy="78" r="5.5" fill="#F6D2B5" {W(1.8)}/>' + '</g>')

# 14. Савёловский вокзал: зелёная электричка-гусеница с погремушкой на токоприёмнике
I["chg-savelovsky-vokzal"] = ("#F7F9E2", "#BFD06A",
    "зелёная электричка-гусеница из трёх вагончиков-сегментов",
    "ползёт по дуге путей, а на её токоприёмнике звенит жёлтая погремушка",
    f'<path d="M-4 112 Q64 92 132 112" fill="none" stroke="#8A6A4A" stroke-width="4"/>'
    + f'<rect x="8" y="80" width="34" height="26" rx="10" fill="#4FB35A" {W(2.8)}/>'
    + f'<rect x="44" y="74" width="34" height="28" rx="10" fill="#5CC466" {W(2.8)}/>'
    + f'<rect x="80" y="66" width="38" height="32" rx="12" fill="#6BD574" {W(2.8)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="10" height="8" rx="2" fill="#E6F7FF" {W(1.6)}/>' for x, y in ((14, 86), (28, 86), (50, 80), (64, 80)))
    + f'<rect x="80" y="84" width="38" height="5" fill="#E8483A"/>' + face(100, 76, d=7, k=.6)
    + f'<path d="M92 66 L100 50 L108 66 M100 50 L100 40" fill="none" stroke="{O}" stroke-width="2.4"/>'
    + f'<circle cx="100" cy="32" r="8" fill="#F7C02F" {W(2.4)}/><path d="M100 40 L100 46" stroke="{O}" stroke-width="3"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1.6" fill="#E8483A"/>' for x, y in ((97, 30), (103, 34), (100, 28)))
    + f'<path d="M86 24 L82 20 M114 24 L118 20 M88 36 L82 38 M112 36 L118 38" stroke="#F0A030" stroke-width="2" stroke-linecap="round"/>')

# 15. Восточный вокзал: сонное утреннее солнышко в ночном колпаке выглядывает из-за навеса перрона с бутылочкой молока
I["chg-vostochny-vokzal"] = ("#FFF3D9", "#F5A65B",
    "сонное утреннее солнышко в полосатом ночном колпаке",
    "выглядывает из-за навеса перрона и держит бутылочку с тёплым молоком",
    f'<rect x="-4" y="100" width="136" height="32" fill="#9AA6B8" {W(2.4)}/>'
    + "".join(f'<path d="M{x} {64+i*0} L{x+10} 52" stroke="#F7C02F" stroke-width="4" stroke-linecap="round"/>' for i, x in enumerate((28, 46, 64, 82)))
    + f'<circle cx="62" cy="76" r="26" fill="#FFC93C" {W(3)}/>'
    + f'<path d="M36 66 Q50 30 86 60 Q70 50 52 58Z" fill="#5E8FE0" {W(2.6)}/><path d="M48 50 L60 58 M62 44 L70 54 M74 48 L80 58" stroke="#fff" stroke-width="3"/>'
    + f'<circle cx="92" cy="58" r="5" fill="#fff" {W(2)}/>'
    + f'<path d="M52 76 Q56 80 60 76 M66 76 Q70 80 74 76" fill="none" stroke="{O}" stroke-width="2.4" stroke-linecap="round"/>'
    + f'<path d="M58 88 Q62 91 66 88" fill="none" stroke="{O}" stroke-width="2"/>'
    + f'<rect x="-4" y="92" width="136" height="12" fill="#5B6B85" {W(2.6)}/>'
    + f'<rect x="86" y="72" width="12" height="24" rx="4" fill="#FFFDF5" {W(2.4)}/><path d="M88 72 Q92 62 96 72Z" fill="#F28AB8" {W(2)}/>'
    + f'<rect x="86" y="82" width="12" height="10" fill="#EAF6FF"/>')

# 16. Киевский вокзал: дорожный чемоданчик-кроха с наклейками, из приоткрытой крышки выглядывает плюшевый зайчик с соской
I["chg-kievsky-vokzal"] = ("#E8F7F6", "#5DB7B0",
    "оранжевый дорожный чемоданчик-кроха на колёсиках с наклейками",
    "приоткрыл крышку, а оттуда выглядывает плюшевый зайчик с соской",
    f'<rect x="-4" y="112" width="136" height="20" fill="#C9D6D8"/>'
    + f'<rect x="28" y="56" width="72" height="54" rx="8" fill="#F08A2E" {W(3)}/>'
    + f'<path d="M28 56 L36 40 L108 40 L100 56Z" fill="#F7A54F" {W(3)}/>'
    + f'<rect x="54" y="30" width="24" height="10" rx="4" fill="none" {W(3)}/>'
    + f'<circle cx="40" cy="114" r="6" fill="#3B3B44" {W(2)}/><circle cx="88" cy="114" r="6" fill="#3B3B44" {W(2)}/>'
    + f'<rect x="36" y="88" width="16" height="12" rx="3" fill="#4FB3E8" {W(1.8)}/><circle cx="84" cy="94" r="7" fill="#F7C02F" {W(1.8)}/>'
    + face(64, 80, d=10, k=.6)
    + f'<path d="M46 42 Q42 14 52 12 Q58 18 54 42Z M66 42 Q70 14 80 14 Q84 22 72 42Z" fill="#F4F0F6" {W(2.4)}/>'
    + f'<path d="M50 38 Q48 22 52 18 M74 38 Q76 24 80 20" stroke="#F4B6CE" stroke-width="3"/>'
    + f'<ellipse cx="62" cy="44" rx="16" ry="9" fill="#F4F0F6" {W(2.4)}/>' + eye(56, 43, .45) + eye(68, 43, .45)
    + f'<circle cx="62" cy="50" r="3" fill="#7FC8F0" {W(1.4)}/>')

# 17. Павелецкий вокзал: семафор, у которого вместо огней — три пустышки (красная, жёлтая, зелёная)
I["chg-paveletsky-vokzal"] = ("#F1F1F6", "#9AA0B8",
    "железнодорожный семафор с тремя пустышками вместо огней",
    "стоит у края перрона и подмигивает зелёной пустышкой, разрешая ехать дальше",
    f'<path d="M-4 116 L132 116" stroke="#8A6A4A" stroke-width="4"/><rect x="-4" y="100" width="56" height="16" fill="#B8C0CC" {W(2.4)}/>'
    + f'<rect x="60" y="76" width="8" height="40" fill="#5A5F70" {W(2.4)}/><rect x="46" y="112" width="36" height="8" rx="2" fill="#5A5F70" {W(2)}/>'
    + f'<rect x="42" y="8" width="44" height="72" rx="14" fill="#2E3245" {W(3)}/>'
    + "".join(f'<circle cx="64" cy="{y}" r="9" fill="{c}" {W(2.2)}/><path d="M57 {y+9} Q64 {y+13} 71 {y+9}" fill="none" stroke="{c}" stroke-width="3"/>'
              for y, c in ((22, "#F0453A"), (42, "#F7C02F"), (62, "#4FD05A")))
    + f'<circle cx="64" cy="62" r="4" fill="#fff" opacity=".7"/>'
    + eye(98, 50, .6) + eye(108, 50, .6) + f'<path d="M98 58 Q103 62 108 58" fill="none" stroke="{O}" stroke-width="2"/>'
    + f'<path d="M90 44 Q103 34 116 44" fill="none" stroke="{O}" stroke-width="0"/>')

# 19. Семёновский (2 этаж): пинетки-близнецы взбираются по ступенькам к цифре «2»
I["chg-semenovsky"] = ("#FDF0EA", "#E8A08A",
    "вязаные пинетки-близнецы с помпонами",
    "держась за шнурки друг друга, взбираются по трём ступенькам к большой цифре «2»",
    f'<path d="M-4 120 L40 120 L40 100 L72 100 L72 80 L104 80 L104 60 L132 60 L132 132 L-4 132Z" fill="#D9C3A8" {W(2.6)}/>'
    + '<text x="100" y="50" font-family="Arial" font-weight="700" font-size="34" fill="#C2483C" stroke="#3B3355" stroke-width="2">2</text>'
    + f'<path d="M18 116 Q16 92 30 90 Q40 90 40 102 L48 108 Q52 118 40 118Z" fill="#7FC8A0" {W(2.6)}/>'
    + f'<path d="M50 96 Q48 72 62 70 Q72 70 72 82 L80 88 Q84 98 72 98Z" fill="#F0B6CF" {W(2.6)}/>'
    + f'<path d="M18 98 Q30 92 40 98 M50 78 Q62 72 72 78" fill="none" stroke="#fff" stroke-width="3"/>'
    + f'<circle cx="28" cy="86" r="5" fill="#fff" {W(1.8)}/><circle cx="60" cy="66" r="5" fill="#fff" {W(1.8)}/>'
    + eye(30, 104, .5) + eye(38, 104, .5) + eye(62, 84, .5) + eye(70, 84, .5)
    + f'<path d="M42 110 Q48 100 54 92" fill="none" stroke="#C2483C" stroke-width="2" stroke-dasharray="3 2"/>')

# 20. Витте Молл: ванночка-кораблик с мачтой-полотенцем плывёт по мыльной пене, рядом губка-морская звезда
I["chg-vitte-mall"] = ("#E4F8FF", "#62B8E0",
    "голубая детская ванночка-кораблик с мачтой из полотенца",
    "плывёт по мыльной пене, а за ней машет лучами розовая губка-морская звезда",
    f'<path d="M-4 96 Q16 86 36 96 Q56 106 76 96 Q96 86 116 96 Q126 100 132 96 L132 132 L-4 132Z" fill="#9ED8F2" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" {W(1.6)}/>' for x, y, r in ((14, 90, 6), (24, 84, 4), (104, 88, 5), (114, 82, 3.5), (58, 108, 4)))
    + f'<path d="M24 70 L98 70 Q96 96 62 96 Q28 96 24 70Z" fill="#4FA8E0" {W(3)}/><path d="M26 76 L96 76" stroke="#fff" stroke-width="3"/>'
    + face(60, 84, d=9, k=.6)
    + f'<path d="M62 70 L62 22" stroke="{O}" stroke-width="3"/><path d="M62 24 L90 32 L88 58 L62 54Z" fill="#FFE37A" {W(2.4)}/>'
    + f'<path d="M64 32 L88 38 M64 46 L88 50" stroke="#F08A2E" stroke-width="2.4"/>'
    + f'<path d="M106 50 l4 9 l10 1 l-7 7 l2 10 l-9 -5 l-9 5 l2 -10 l-7 -7 l10 -1Z" fill="#F38BB6" {W(2.2)}/>' + eye(103, 60, .35) + eye(109, 60, .35))

# 21. Капитолий (Марьина Роща): плюшевый слонёнок хоботом подаёт малышу подгузник на пеленальном столике
I["chg-kapitoliy-marina-roshcha"] = ("#F0EEFA", "#A49AD0",
    "серый плюшевый слонёнок в розовом фартучке",
    "хоботом подаёт свёрнутый подгузник к пеленальному столику, где лежит малыш",
    f'<rect x="56" y="80" width="68" height="10" rx="4" fill="#FFFDF5" {W(2.6)}/><rect x="62" y="90" width="6" height="40" fill="#C49A63" {W(2)}/><rect x="112" y="90" width="6" height="40" fill="#C49A63" {W(2)}/>'
    + f'<ellipse cx="96" cy="74" rx="20" ry="8" fill="#BFE6FA" {W(2.4)}/><circle cx="80" cy="72" r="8" fill="#F6D2B5" {W(2)}/>' + eye(78, 71, .4) + eye(83, 71, .4)
    + f'<ellipse cx="34" cy="96" rx="24" ry="22" fill="#A7AEBB" {W(3)}/><path d="M20 100 L44 100 L40 118 L24 118Z" fill="#F7A8C6" {W(2.2)}/>'
    + f'<circle cx="34" cy="60" r="20" fill="#B5BCC8" {W(3)}/>'
    + f'<path d="M14 56 Q2 50 4 70 Q8 82 20 72Z M54 56 Q66 50 64 70 Q60 82 48 72Z" fill="#C9CFD9" {W(2.6)}/>'
    + face(34, 58, d=7, k=.55)
    + f'<path d="M40 70 Q52 70 60 60 Q64 54 70 58" fill="none" stroke="#B5BCC8" stroke-width="8" stroke-linecap="round"/>'
    + f'<path d="M40 70 Q52 70 60 60 Q64 54 70 58" fill="none" stroke="{O}" stroke-width="1.6" stroke-dasharray="1 0" opacity=".0"/>'
    + f'<path d="M66 48 L80 46 L82 58 L68 60Z" fill="#FFFFFF" {W(2.2)}/><path d="M68 52 L80 50" stroke="#7FC8F0" stroke-width="2"/>')

# 22. Выходной (Люберцы): бутылочка-термос в вязаном шарфике греет тарелочку каши с ложкой-самолётиком
I["chg-vykhodnoy-lyubertsy"] = ("#FFF7E6", "#F0B860",
    "детская бутылочка в полосатом вязаном шарфике",
    "сидит у тарелочки с кашей, к которой подлетает ложка-самолётик",
    f'<ellipse cx="80" cy="104" rx="36" ry="10" fill="#fff" {W(2.6)}/><path d="M50 100 Q80 120 110 100" fill="#E8F1FA" {W(2.4)}/>'
    + f'<ellipse cx="80" cy="100" rx="26" ry="6" fill="#F6E1A6" {W(2)}/><circle cx="74" cy="98" r="3" fill="#E8483A"/>'
    + f'<rect x="20" y="46" width="34" height="64" rx="12" fill="#F4FBFF" {W(3)}/><path d="M24 70 L50 70 M24 82 L50 82 M24 94 L50 94" stroke="#BFD6E8" stroke-width="2"/>'
    + f'<rect x="22" y="38" width="30" height="10" rx="3" fill="#7FC8F0" {W(2.4)}/><path d="M28 38 Q37 16 46 38Z" fill="#F7C9A0" {W(2.4)}/>'
    + f'<path d="M16 56 L58 56 L58 64 L16 64Z" fill="#E8483A" {W(2.2)}/><path d="M24 56 L24 64 M34 56 L34 64 M44 56 L44 64" stroke="#fff" stroke-width="3"/>'
    + f'<path d="M50 62 L56 80 L48 80Z" fill="#E8483A" {W(2)}/>'
    + face(37, 80, d=7, k=.55)
    + f'<path d="M78 40 L112 40" stroke="#9AA6B8" stroke-width="5" stroke-linecap="round"/><ellipse cx="72" cy="40" rx="8" ry="5" fill="#C8D0DA" {W(2)}/>'
    + f'<path d="M96 30 L100 50 M92 40 L104 40" stroke="#2F6FD0" stroke-width="4" stroke-linecap="round"/>'
    + f'<path d="M112 40 L120 34 L120 46Z" fill="#2F6FD0" {W(1.6)}/>'
    + f'<path d="M62 36 Q56 34 52 38 M64 46 Q58 48 54 46" fill="none" stroke="#fff" stroke-width="2.4"/>')

# 23. Акварель (Пушкино): кисточка с глазками рисует радугу на пелёнке малыша
I["chg-akvarel-pushkino"] = ("#F6F2FF", "#B3A0E6",
    "акварельная кисточка с пушистым хвостиком и глазками",
    "рисует радугу прямо на белой пелёнке, в которую завёрнут спящий малыш",
    f'<path d="M10 92 Q40 74 70 86 Q96 96 118 82 L120 112 Q90 124 60 116 Q30 110 10 118Z" fill="#fff" {W(3)}/>'
    + f'<path d="M24 104 Q60 80 100 98" fill="none" stroke="#F0453A" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M28 110 Q60 88 98 104" fill="none" stroke="#F7C02F" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M32 116 Q60 96 96 110" fill="none" stroke="#4FB35A" stroke-width="5" stroke-linecap="round"/>'
    + f'<circle cx="14" cy="98" r="10" fill="#F6D2B5" {W(2.4)}/><path d="M9 98 q2 2 4 0 M15 98 q2 2 4 0" fill="none" stroke="{O}" stroke-width="1.4"/>'
    + f'<g transform="rotate(35 86 48)"><rect x="80" y="10" width="12" height="54" rx="5" fill="#E05A3A" {W(2.6)}/>'
    + f'<rect x="79" y="60" width="14" height="10" fill="#C8CDD2" {W(2.2)}/><path d="M79 70 Q86 92 93 70Z" fill="#6B4A32" {W(2.2)}/>'
    + f'<path d="M82 78 Q86 92 90 78Z" fill="#4F7FE0"/>' + eye(83, 30, .45) + eye(89, 30, .45) + '</g>'
    + sparkle(30, 30, 6, "#FFE88A") + sparkle(50, 18, 4, "#9FE3FF"))

# 24. Галерея Тушино: золотая рама-картина на мольберте с нарисованным пароходиком
I["fun-galereya-tushino"] = ("#F3F7FB", "#9DB2C6",
    "золочёная рама-картина с глазками на деревянном мольберте",
    "показывает нарисованный пароходик на канале, а палитра с красками стоит у её ножек",
    f'<path d="M40 128 L56 40 M88 128 L72 40 M64 120 L64 50" stroke="#A5713F" stroke-width="5" stroke-linecap="round"/>'
    + f'<rect x="26" y="26" width="76" height="62" rx="4" fill="#E8B83C" {W(3)}/>'
    + f'<rect x="34" y="34" width="60" height="46" fill="#BFE6FA" {W(2)}/><path d="M34 66 Q64 58 94 66 L94 80 L34 80Z" fill="#3A80C9"/>'
    + f'<path d="M50 64 L78 64 L74 70 L54 70Z" fill="#fff" {W(1.6)}/><rect x="60" y="54" width="6" height="10" fill="#E8483A" {W(1.4)}/>'
    + f'<path d="M58 50 q4 -3 8 0" fill="none" stroke="#9AA6B8" stroke-width="2"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#F6D06A" {W(1.4)}/>' for x, y in ((26, 26), (102, 26), (26, 88), (102, 88)))
    + face(64, 96, d=9, k=.55, mouth=True) * 0
    + eye(46, 44, .5) + eye(56, 44, .5)
    + f'<path d="M86 110 Q100 96 116 106 Q122 118 104 122 Q88 124 86 110Z" fill="#F4E0BE" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="{c}"/>' for x, y, c in ((98, 106, "#F0453A"), (106, 104, "#4FB35A"), (112, 110, "#2F6FD0"))))

# 25. Музей Русской Истории: богатырский шлем-шишак с глазками на княжеском пиру, рядом расписной ковш
I["fun-muzey-russkoy-istorii"] = ("#FFF2E2", "#D88C5A",
    "богатырский шлем-шишак с кольчужной бармицей и глазками",
    "сидит во главе княжеского стола, рядом поднимает расписной ковш с квасом",
    f'<rect x="-4" y="96" width="136" height="36" fill="#9A5A2E" {W(2.6)}/><path d="M-4 104 L132 104" stroke="#C98A4E" stroke-width="3"/>'
    + f'<path d="M30 70 Q30 30 56 22 L60 6 L64 22 Q90 30 90 70Z" fill="#C8CDD2" {W(3)}/>'
    + f'<path d="M60 6 L60 0" stroke="{O}" stroke-width="3"/><path d="M30 70 L90 70" stroke="#E8B83C" stroke-width="5"/>'
    + f'<path d="M30 70 Q34 96 46 98 L74 98 Q86 96 90 70Z" fill="#9AA3AD" {W(2.6)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="#6E7782"/>' for x in range(38, 84, 8) for y in (78, 86, 94))
    + f'<rect x="50" y="52" width="20" height="18" rx="4" fill="#F6D2B5" {W(2)}/>' + eye(55, 60, .45) + eye(65, 60, .45)
    + f'<path d="M60 42 L60 70" stroke="#9AA3AD" stroke-width="4"/>'
    + f'<path d="M92 82 Q96 70 114 72 Q120 74 118 80 L112 92 Q100 96 94 92Z" fill="#E8483A" {W(2.4)}/>'
    + f'<path d="M98 82 Q104 78 110 82" fill="none" stroke="#F7C02F" stroke-width="2.4"/><path d="M118 76 Q126 70 124 62" fill="none" stroke="{O}" stroke-width="3"/>')


if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
