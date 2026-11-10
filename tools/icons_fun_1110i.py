"""Иконки робота fun (2026-11-10, вечерний проход): места из tools/add_fun_1110i.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя палитра фона.
Запуск: python3 tools/icons_fun_1110i.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye, O
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}

# Дом Пастернака — «Свеча горела на столе»
I["pasternak-house-peredelkino"] = ("#E9EEFF", "#3E4C8F",
    "восковая свеча в латунном подсвечнике с мордашкой на воске",
    "горит на деревянном столе у заиндевевшего окна, за которым кружат снежинки",
    f'<rect x="14" y="8" width="100" height="74" rx="4" fill="#26336E" {W(3)}/>'
    f'<path d="M64 8 V82 M14 44 H114" stroke="{O}" stroke-width="3"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.4" fill="#fff"/>' for x, y in ((26, 20), (44, 30), (88, 18), (102, 34), (24, 60), (98, 62), (80, 72), (40, 70)))
    + f'<path d="M14 82 Q30 72 44 80 Q58 70 70 80 Q86 70 114 80 V84 H14Z" fill="#fff" opacity=".9"/>'
    f'<path d="M-2 92 H130 V130 H-2Z" fill="#A86E3C" {W(3)}/><path d="M-2 104 H130" stroke="#8A5428" stroke-width="2.4"/>'
    f'<ellipse cx="64" cy="98" rx="24" ry="6" fill="#E3B23C" {W(2.8)}/>'
    f'<rect x="56" y="90" width="16" height="8" fill="#E3B23C" {W(2.4)}/>'
    f'<rect x="50" y="46" width="28" height="46" rx="6" fill="#FFF6DC" {W(3)}/>'
    f'<path d="M56 46 Q55 54 58 58" fill="none" stroke="#EADBB0" stroke-width="3"/>'
    + face(64, 66, d=6, k=0.6) +
    f'<path d="M64 46 V40" stroke="{O}" stroke-width="2"/>'
    f'<path d="M64 14 Q74 28 68 38 Q64 42 60 38 Q54 28 64 14Z" fill="#FFB43A" {W(2.4)}/>'
    f'<path d="M64 24 Q68 31 65 36 Q62 34 62 30Z" fill="#FFF2A6"/>'
    f'<circle cx="64" cy="30" r="22" fill="#FFE27A" opacity=".18"/>')

# Музей Окуджавы — «Последний троллейбус»
I["okudzhava-museum-peredelkino"] = ("#E4F3FF", "#2E5E9E",
    "синий ночной троллейбус с мордашкой-фарами и двумя усами-штангами",
    "едет по пустой ночной улице под жёлтой луной, в окошках горит тёплый свет",
    f'<circle cx="100" cy="24" r="12" fill="#FFE27A" {W(2.4)}/><circle cx="105" cy="20" r="10" fill="#2E5E9E" opacity=".0"/>'
    f'<path d="M-2 14 H130" stroke="{O}" stroke-width="1.8"/><path d="M-2 20 H130" stroke="{O}" stroke-width="1.8"/>'
    f'<path d="M52 50 L70 16 M64 50 L84 22" stroke="{O}" stroke-width="3"/>'
    f'<path d="M-2 104 H130 V130 H-2Z" fill="#4A5570" {W(2.6)}/>'
    f'<path d="M8 114 H26 M50 114 H68 M92 114 H110" stroke="#FFE27A" stroke-width="3"/>'
    f'<rect x="12" y="48" width="104" height="52" rx="12" fill="#3F7FD8" {W(3.2)}/>'
    f'<rect x="12" y="80" width="104" height="8" fill="#2E5E9E"/>'
    + "".join(f'<rect x="{x}" y="56" width="16" height="16" rx="3" fill="#FFE9A6" {W(2.2)}/>' for x in (20, 42, 64))
    + f'<rect x="88" y="56" width="22" height="22" rx="4" fill="#BFE3FF" {W(2.4)}/>'
    + face(99, 66, d=4.5, k=0.45, mouth=True) +
    f'<circle cx="110" cy="90" r="4" fill="#FFF2A6" {W(1.8)}/>'
    f'<circle cx="32" cy="100" r="9" fill="#2F2F3F" {W(2.6)}/><circle cx="32" cy="100" r="3.6" fill="#C9D2DE"/>'
    f'<circle cx="92" cy="100" r="9" fill="#2F2F3F" {W(2.6)}/><circle cx="92" cy="100" r="3.6" fill="#C9D2DE"/>'
    + sparkle(26, 30, 4) + sparkle(46, 36, 3))

# Музей Жуковского — модель вертолёта под потолком
I["zhukovsky-memorial-museum"] = ("#EFFFF4", "#3E9E77",
    "модель старинного вертолёта с двумя большими винтами и мордашкой на кабине",
    "висит на тонких лесках под потолком музейного зала над стеклянной витриной с крошечной ракетой",
    f'<path d="M44 0 V30 M84 0 V30" stroke="#5A6A80" stroke-width="1.4"/>'
    f'<path d="M14 26 H62 M66 26 H104" stroke="{O}" stroke-width="4" stroke-linecap="round"/>'
    f'<circle cx="58" cy="26" r="3" fill="{O}"/>'
    f'<path d="M58 26 V36" stroke="{O}" stroke-width="3"/>'
    f'<path d="M74 50 L118 44 L120 36 L126 36 L124 56 L74 60Z" fill="#E89A2A" {W(2.8)}/>'
    f'<ellipse cx="58" cy="52" rx="34" ry="18" fill="#F2B33A" {W(3.2)}/>'
    f'<path d="M28 48 Q30 36 46 36 L48 52 Q36 54 28 48Z" fill="#BFE3FF" {W(2.4)}/>'
    + face(62, 54, d=7, k=0.6) +
    f'<path d="M74 68 L80 76 M42 68 L36 76 M28 78 H96" stroke="{O}" stroke-width="3"/>'
    f'<rect x="30" y="88" width="68" height="34" rx="3" fill="#D8F2FF" opacity=".75" {W(2.6)}/>'
    f'<path d="M64 112 V98 Q64 92 68 92 Q72 92 72 98 V112Z" fill="#fff" {W(2)}/>'
    f'<path d="M64 106 L60 112 M72 106 L76 112" stroke="{O}" stroke-width="2"/><circle cx="68" cy="99" r="1.8" fill="#E8434A"/>'
    f'<path d="M26 122 H102" stroke="#7A5A3A" stroke-width="6"/>' + sparkle(104, 92, 4) + sparkle(18, 84, 3))

# Бахрушинский музей — театральный камзол на манекене
I["bakhrushin-theatre-museum"] = ("#FFF0EC", "#A63A4A",
    "бордовый бархатный театральный камзол с золотыми пуговицами и мордашкой на воротнике",
    "надет на деревянный портновский манекен в музейном зале, а сверху парит шляпа с белым пером",
    f'<path d="M64 112 V124 M48 124 H80" stroke="#7A4E2C" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M40 44 Q64 34 88 44 L96 70 Q94 96 84 110 H44 Q34 96 32 70Z" fill="#9E2F45" {W(3.2)}/>'
    f'<path d="M64 42 V110" stroke="{O}" stroke-width="2.4"/>'
    + "".join(f'<circle cx="69" cy="{y}" r="2.6" fill="#F2C85A" {W(1.4)}/>' for y in (66, 78, 90, 102)) +
    f'<path d="M40 44 L26 78 L36 82 L44 60 M88 44 L102 78 L92 82 L84 60" fill="#9E2F45" {W(2.8)}/>'
    f'<path d="M48 40 L64 56 L80 40 L72 36 L64 44 L56 36Z" fill="#FFFDF2" {W(2.4)}/>'
    + face(64, 72, d=8, k=0.65) +
    f'<path d="M30 92 Q36 98 40 96 M98 92 Q92 98 88 96" fill="none" stroke="#F2C85A" stroke-width="3"/>'
    f'<path d="M40 26 Q64 14 88 26 Q64 32 40 26Z" fill="#2F2F3F" {W(2.6)}/>'
    f'<path d="M52 24 Q64 4 76 24Z" fill="#2F2F3F" {W(2.6)}/>'
    f'<path d="M74 18 Q98 0 112 12 Q96 14 80 22Z" fill="#FFFFFF" {W(2.2)}/>'
    + sparkle(22, 34, 5) + sparkle(110, 48, 4))

# Музей хоккея — свитер на плечиках в витрине
I["hockey-museum-avtozavodskaya"] = ("#EAF4FF", "#C2343E",
    "красный хоккейный свитер с белыми полосами и номером 7 на плечиках",
    "висит в музейной витрине под лампой, а под ним на бархатной подушке лежит золотая медаль",
    f'<rect x="10" y="10" width="108" height="112" rx="6" fill="#F4FAFF" opacity=".55" {W(2.6)}/>'
    f'<path d="M64 14 V22 M52 28 Q64 20 76 28" fill="none" stroke="{O}" stroke-width="3"/>'
    f'<path d="M44 30 L22 46 L32 64 L40 58 V94 H88 V58 L96 64 L106 46 L84 30 Q64 40 44 30Z" fill="#D8343E" {W(3.2)}/>'
    f'<path d="M40 82 H88 M40 88 H88" stroke="#fff" stroke-width="4"/>'
    f'<path d="M24 50 L30 60 M104 50 L98 60" stroke="#fff" stroke-width="4"/>'
    f'<path d="M56 30 Q64 38 72 30" fill="none" stroke="#fff" stroke-width="3"/>'
    f'<text x="64" y="60" font-family="Arial" font-weight="bold" font-size="18" fill="#fff" text-anchor="middle">7</text>'
    + face(64, 70, d=8, k=0.55) +
    f'<ellipse cx="64" cy="112" rx="24" ry="6" fill="#4A3A8A" {W(2.4)}/>'
    f'<path d="M58 98 L64 106 L70 98" fill="none" stroke="#3F7FD8" stroke-width="3"/>'
    f'<circle cx="64" cy="108" r="6" fill="#F2C85A" {W(2)}/>' + sparkle(100, 100, 4) + sparkle(24, 100, 3))

# Кукольный театр «Скоморох» — медвежонок-перчатка с гармошкой
I["skomorokh-puppets-kolomna"] = ("#FFF6D9", "#D98A2B",
    "плюшевый медвежонок — кукла-перчатка в пёстрой рубахе",
    "высунулся из-за синей расписной ширмы кукольного театра и растягивает маленькую гармошку",
    f'<path d="M48 84 Q46 60 64 56 Q82 60 80 84Z" fill="#E8434A" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="#FFE27A"/>' for x, y in ((56, 68), (70, 66), (62, 76), (74, 78)))
    + f'<circle cx="64" cy="40" r="20" fill="#B9773E" {W(3.2)}/>'
    f'<circle cx="48" cy="24" r="7" fill="#B9773E" {W(2.8)}/><circle cx="80" cy="24" r="7" fill="#B9773E" {W(2.8)}/>'
    f'<ellipse cx="64" cy="48" rx="9" ry="7" fill="#E9C08A" {W(2)}/><circle cx="64" cy="45" r="2.4" fill="{O}"/>'
    + eye(57, 36, 0.6) + eye(71, 36, 0.6) +
    f'<rect x="26" y="58" width="18" height="24" rx="3" fill="#3F7FD8" {W(2.6)}/><rect x="84" y="58" width="18" height="24" rx="3" fill="#3F7FD8" {W(2.6)}/>'
    f'<path d="M44 60 H84 V80 H44Z" fill="#F7E3B0" {W(2.4)}/>'
    + "".join(f'<path d="M{48+i*6} 60 V80" stroke="#C0603A" stroke-width="2"/>' for i in range(6)) +
    "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="#fff"/>' for x in (31, 39, 89, 97) for y in (64, 70, 76)) +
    f'<path d="M-2 84 H130 V130 H-2Z" fill="#2E5FB0" {W(3.2)}/>'
    + "".join(f'<path d="M{x} 104 q8 -10 16 0 q-8 10 -16 0Z" fill="#FFD25E" {W(1.6)}/>' for x in (8, 40, 72, 104)) +
    f'<path d="M-2 92 H130" stroke="#FFD25E" stroke-width="3"/>' + sparkle(24, 30, 5) + sparkle(104, 40, 4))

# ДДТ «Созвездие» — бумажная звёздочка-аппликация
I["ddt-sozvezdie-khimki"] = ("#F0EAFF", "#4B3E9E",
    "жёлтая бумажная звёздочка-аппликация с мордашкой",
    "детские ножницы с зелёными ручками дорезают её последний лучик из листа, а рядом на синем картоне наклеено созвездие",
    f'<rect x="8" y="12" width="64" height="50" rx="4" fill="#24307A" {W(2.6)}/>'
    + "".join(f'<path d="M{x} {y-5} L{x+1.5} {y-1.5} L{x+5} {y} L{x+1.5} {y+1.5} L{x} {y+5} L{x-1.5} {y+1.5} L{x-5} {y} L{x-1.5} {y-1.5}Z" fill="#FFE27A"/>' for x, y in ((20, 24), (36, 34), (52, 26), (60, 46), (28, 50)))
    + f'<path d="M20 24 L36 34 L52 26 M36 34 L60 46 M36 34 L28 50" stroke="#FFE27A" stroke-width="1.2" stroke-dasharray="2 2"/>'
    f'<rect x="40" y="56" width="80" height="62" rx="3" fill="#FFF8E0" {W(2.4)} transform="rotate(6 80 87)"/>'
    f'<path d="M78 52 L86 70 L106 72 L91 85 L96 105 L78 94 L60 105 L65 85 L50 72 L70 70Z" fill="#FFCC33" {W(3)}/>'
    + face(78, 82, d=6, k=0.6) +
    f'<path d="M20 116 L50 96 M20 96 L50 116" stroke="#9AA6B8" stroke-width="5" stroke-linecap="round"/>'
    f'<circle cx="16" cy="94" r="7" fill="none" stroke="#3FAE5A" stroke-width="5"/><circle cx="16" cy="118" r="7" fill="none" stroke="#3FAE5A" stroke-width="5"/>'
    f'<circle cx="35" cy="106" r="2.4" fill="{O}"/>' + sparkle(110, 30, 6) + sparkle(96, 16, 3.5))

# ЦДТ «Марьина Роща» — роща из цветных карандашей
I["cdt-maryina-roshcha"] = ("#F2FFE6", "#5DAE4A",
    "маленький розовый карандаш с мордашкой",
    "растёт в роще из высоких цветных карандашей-деревьев и рисует на зелёной траве жёлтое солнышко",
    f'<path d="M-2 98 H130 V130 H-2Z" fill="#8CCB6A" {W(3)}/>'
    + "".join(f'<path d="M{x} 98 V{t+12} L{x+6} {t} L{x+12} {t+12} V98Z" fill="{c}" {W(2.6)}/>'
              f'<path d="M{x+3} {t+6} L{x+6} {t} L{x+9} {t+6}Z" fill="#F6D7A8"/><path d="M{x+5} {t+2} L{x+6} {t} L{x+7} {t+2}Z" fill="{O}"/>'
              for x, t, c in ((6, 20, "#3F7FD8"), (24, 8, "#E8434A"), (96, 14, "#9B59D0"), (112, 30, "#F2B33A"), (42, 34, "#2FA36B")))
    + f'<g transform="rotate(-24 76 82)"><path d="M62 104 V64 L76 44 L90 64 V104Z" fill="#FF8FB8" {W(3)}/>'
    f'<path d="M69 54 L76 44 L83 54Z" fill="#F6D7A8" {W(1.6)}/><path d="M74 47 L76 44 L78 47Z" fill="{O}"/>'
    f'<rect x="62" y="96" width="28" height="8" fill="#C9D2DE" {W(2)}/>' + face(76, 76, d=6, k=0.55) + '</g>'
    f'<circle cx="44" cy="112" r="7" fill="#FFE27A" {W(1.8)}/>'
    + "".join(f'<path d="M{44+10*c:.1f} {112+10*s_:.1f} L{44+14*c:.1f} {112+14*s_:.1f}" stroke="#F2B33A" stroke-width="2.4"/>'
              for c, s_ in ((1, 0), (-1, 0), (0, -1), (0.7, -0.7), (-0.7, -0.7))))

# Эколого-биологический центр — кролик у грядки
I["eco-bio-center-pavposad"] = ("#FFF8EC", "#7FB04A",
    "серый пушистый кролик с длинными ушами",
    "сидит у деревянной грядки и бережно поливает из маленькой синей лейки зелёные всходы",
    f'<path d="M-2 100 H130 V130 H-2Z" fill="#9C6A3A" {W(3)}/>'
    + "".join(f'<path d="M{x} 100 Q{x-4} 88 {x-8} 86 M{x} 100 Q{x+4} 88 {x+8} 86" fill="none" stroke="#3FAE5A" stroke-width="3.2"/>' for x in (82, 100, 116))
    + f'<rect x="70" y="100" width="58" height="10" fill="#B88A50" {W(2.4)}/>'
    f'<ellipse cx="44" cy="84" rx="26" ry="22" fill="#B8BDC8" {W(3.2)}/>'
    f'<circle cx="44" cy="54" r="18" fill="#C9CED8" {W(3.2)}/>'
    f'<path d="M34 40 Q26 8 34 6 Q42 8 40 40Z" fill="#C9CED8" {W(2.8)}/><path d="M34 34 Q30 14 34 12 Q38 14 38 34Z" fill="#FFB3C8"/>'
    f'<path d="M50 40 Q56 8 64 10 Q68 14 56 42Z" fill="#C9CED8" {W(2.8)}/><path d="M53 36 Q58 16 62 15 Q63 18 56 38Z" fill="#FFB3C8"/>'
    + face(44, 56, d=7, k=0.6, mouth=False) +
    f'<path d="M41 62 Q44 65 47 62" fill="none" stroke="{O}" stroke-width="2"/><circle cx="44" cy="60" r="2" fill="#FF7FA8"/>'
    f'<path d="M62 70 H80 L86 64" fill="none" stroke="{O}" stroke-width="2"/>'
    f'<path d="M60 74 H82 V90 H60Z" fill="#3F7FD8" {W(2.6)}/><path d="M82 78 L96 70" stroke="#3F7FD8" stroke-width="5" stroke-linecap="round"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="#6CC0F2"/>' for x, y in ((98, 76), (101, 82), (96, 84)))
    + f'<ellipse cx="60" cy="80" rx="6" ry="5" fill="#C9CED8" {W(2.2)}/>' + sparkle(108, 30, 5) + sparkle(86, 18, 3))

# ---------- детские библиотеки ----------
# Коломна №3 — ночник-полумесяц над книжкой сказок
I["lib3-kolomna-devichye-pole"] = ("#FFF4E8", "#6A5AA8",
    "фонарик-ночник в форме жёлтого полумесяца с мордашкой",
    "склонился над раскрытой книжкой сказок, лежащей на пухлой подушке, и светит на страницы",
    f'<path d="M14 92 Q14 78 30 78 H98 Q114 78 114 92 Q114 112 98 112 H30 Q14 112 14 92Z" fill="#F7F2FF" {W(3)}/>'
    f'<path d="M30 82 Q64 92 98 82" fill="none" stroke="#D9CCF2" stroke-width="3"/>'
    f'<path d="M64 98 L36 90 L36 72 L64 80Z" fill="#FFFDF5" {W(2.6)}/><path d="M64 98 L92 90 L92 72 L64 80Z" fill="#FFFDF5" {W(2.6)}/>'
    f'<path d="M42 78 L58 82 M42 84 L58 88 M70 82 L86 78 M70 88 L86 84" stroke="#B9AFA0" stroke-width="1.8"/>'
    f'<path d="M64 26 L92 76 L36 76Z" fill="#FFE9A6" opacity=".45"/>'
    f'<path d="M84 8 A26 26 0 1 0 84 52 A20 20 0 1 1 84 8Z" fill="#FFD84A" {W(3)} transform="translate(-14 0)"/>'
    + eye(52, 26, 0.55) + f'<path d="M48 36 Q52 40 56 36" fill="none" stroke="{O}" stroke-width="2"/>'
    f'<ellipse cx="46" cy="34" rx="3.4" ry="2" fill="#FF7FA8" opacity=".6"/>'
    + sparkle(98, 22, 5, "#FFE9A6") + sparkle(108, 46, 3.5, "#FFE9A6") + sparkle(22, 50, 3.5, "#FFE9A6"))

# Троицк — мальчик читает под одеялом с фонариком
I["lib-kids-troitsk-sirenevy"] = ("#E8F6FF", "#2B4C8C",
    "мальчик в полосатой пижаме с фонариком",
    "лежит под одеялом-палаткой и читает толстую книжку, а луч фонарика освещает страницу",
    f'<path d="M4 110 Q64 18 124 110Z" fill="#5AA0E0" {W(3.2)}/>'
    + "".join(f'<path d="M{x} 110 Q{64+(x-64)*0.4:.0f} 40 64 30" fill="none" stroke="#4A88C8" stroke-width="2.4"/>' for x in (26, 46, 82, 102))
    + f'<circle cx="46" cy="70" r="14" fill="#F6C9A0" {W(3)}/>'
    f'<path d="M32 66 Q36 52 48 54 Q60 56 58 66 Q50 60 40 64Z" fill="#7A4A2A" {W(2.2)}/>'
    + eye(42, 70, 0.5) + eye(52, 70, 0.5) +
    f'<path d="M30 110 V88 Q46 80 62 88 V110Z" fill="#fff" {W(2.8)}/>'
    + "".join(f'<path d="M30 {y} H62" stroke="#3F7FD8" stroke-width="3"/>' for y in (94, 102)) +
    f'<path d="M66 96 L74 80 L92 84 L86 100Z" fill="#E8434A" {W(2.6)}/><path d="M70 94 L76 82 L88 85" fill="#FFFDF5"/>'
    f'<rect x="96" y="92" width="16" height="8" rx="2" fill="#4A4A5A" {W(2.2)} transform="rotate(-20 104 96)"/>'
    f'<path d="M96 90 L80 84 L84 98Z" fill="#FFF2A6" opacity=".8"/>' + sparkle(64, 16, 4))

# Королёв — книжка-ракета
I["lib-kids-korolev-kirova"] = ("#ECEBFF", "#2A2A6E",
    "толстая синяя книжка-ракета с круглым иллюминатором на обложке и мордашкой в нём",
    "взлетает со стола к звёздам, а вместо огненного хвоста из неё веером вылетают белые страницы",
    "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="#fff"/>' for x, y in ((18, 22), (34, 44), (108, 18), (112, 52), (90, 30), (20, 70)))
    + f'<g transform="rotate(30 64 60)">'
    f'<path d="M44 34 Q64 0 84 34 V86 H44Z" fill="#3F6FD8" {W(3.2)}/>'
    f'<path d="M80 34 V86" stroke="#FFFDF5" stroke-width="5"/><path d="M80 34 V86" stroke="{O}" stroke-width="1.4"/>'
    f'<circle cx="62" cy="52" r="12" fill="#BFE3FF" {W(2.6)}/>' + face(62, 52, d=4.5, k=0.45) +
    f'<path d="M44 72 L32 88 L44 86 M84 72 L96 88 L84 86" fill="#E8434A" {W(2.6)}/>'
    f'<path d="M48 86 L44 104 L56 92 L64 110 L72 92 L84 104 L80 86Z" fill="#FFFDF5" {W(2.4)}/>'
    f'<path d="M52 94 L58 92 M70 92 L76 94" stroke="#B9AFA0" stroke-width="1.6"/></g>'
    + sparkle(104, 84, 5) + sparkle(30, 100, 4))

# Красногорск №22 — библиотечный штамп
I["lib22-krasnogorsk-komsomolskaya"] = ("#FBEFFF", "#8A4AB8",
    "деревянный библиотечный штамп с круглой ручкой и мордашкой",
    "шлёпает фиолетовую звёздочку на бумажный кармашек раскрытой книги, а рядом подпрыгивает штемпельная подушечка",
    f'<path d="M8 112 L64 96 L120 112 L120 118 L64 104 L8 118Z" fill="#E8434A" {W(2.6)}/>'
    f'<path d="M12 110 L64 94 L64 70 L12 82Z" fill="#FFFDF5" {W(2.6)}/><path d="M116 110 L64 94 L64 70 L116 82Z" fill="#FFFDF5" {W(2.6)}/>'
    f'<path d="M78 88 L104 94 L104 106 L78 100Z" fill="#F2D9A8" {W(2)}/>'
    f'<path d="M90 92 l2 4 l4 0 l-3 3 l1 4 l-4 -2 l-4 2 l1 -4 l-3 -3 l4 0Z" fill="#8A4AB8"/>'
    f'<circle cx="64" cy="18" r="12" fill="#C98B4A" {W(3)}/>'
    f'<path d="M58 30 H70 V40 H58Z" fill="#B87A3A" {W(2.6)}/>'
    f'<path d="M40 40 H88 V64 H40Z" fill="#D9A060" {W(3.2)}/><path d="M40 64 H88 V70 H40Z" fill="#6A3A8A" {W(2.4)}/>'
    + face(64, 50, d=8, k=0.6) +
    f'<path d="M34 50 L26 46 M34 58 L24 60 M94 50 L102 46 M94 58 L104 60" stroke="{O}" stroke-width="2.4"/>'
    f'<rect x="14" y="54" width="20" height="10" rx="3" fill="#6A3A8A" {W(2.2)} transform="rotate(-12 24 59)"/>' + sparkle(108, 24, 5))

# Кашира — книжный шкаф
I["lib3-kashira-metallistov"] = ("#EFFAF0", "#3E8E5E",
    "книжный шкаф со стеклянными дверцами и мордашкой на карнизе",
    "распахнул дверцы, а книжки внутри выстроились по росту, как ребята на линейке",
    f'<path d="M28 18 H100 V118 H28Z" fill="#A86E3C" {W(3.2)}/>'
    f'<path d="M24 14 H104 V26 H24Z" fill="#8A5428" {W(3)}/>' + face(64, 20, d=10, k=0.5, mouth=False) +
    f'<path d="M60 22 Q64 25 68 22" fill="none" stroke="{O}" stroke-width="1.8"/>'
    f'<path d="M34 60 H94 M34 92 H94" stroke="{O}" stroke-width="3"/>'
    + "".join(f'<rect x="{36+i*8}" y="{60-h}" width="7" height="{h}" fill="{c}" {W(1.6)}/>'
              for i, (h, c) in enumerate(((30, "#E8434A"), (27, "#3F7FD8"), (24, "#F2B33A"), (21, "#2FA36B"), (18, "#9B59D0"), (15, "#FF8FB8"), (12, "#5CCDBA"))))
    + "".join(f'<rect x="{36+i*8}" y="{92-h}" width="7" height="{h}" fill="{c}" {W(1.6)}/>'
              for i, (h, c) in enumerate(((28, "#F2B33A"), (25, "#E8434A"), (22, "#3F7FD8"), (19, "#9B59D0"), (16, "#2FA36B"))))
    + f'<path d="M28 30 L8 24 V108 L28 114Z" fill="#D8F2FF" opacity=".85" {W(2.6)}/>'
    f'<path d="M100 30 L120 24 V108 L100 114Z" fill="#D8F2FF" opacity=".85" {W(2.6)}/>'
    f'<circle cx="23" cy="70" r="2.6" fill="#F2C85A" {W(1.2)}/><circle cx="105" cy="70" r="2.6" fill="#F2C85A" {W(1.2)}/>'
    + sparkle(16, 14, 4) + sparkle(114, 12, 4))

# Климовск — круглые очки на раскрытой книге
I["cdb-klimovsk-pervomayskaya"] = ("#FFF6E0", "#C98A2E",
    "очки в круглой красной оправе с глазками за стёклами",
    "лежат на раскрытой книге и с интересом разглядывают через линзы крупную букву «А»",
    f'<path d="M64 112 L10 98 L10 56 L64 70Z" fill="#FFFDF5" {W(3)}/><path d="M64 112 L118 98 L118 56 L64 70Z" fill="#FFFDF5" {W(3)}/>'
    f'<path d="M64 116 L8 102 M64 116 L120 102" stroke="#3F7FD8" stroke-width="5"/>'
    + "".join(f'<path d="M18 {y} L56 {y+10}" stroke="#B9AFA0" stroke-width="2"/>' for y in (66, 76, 86))
    + f'<text x="92" y="96" font-family="Arial" font-weight="bold" font-size="28" fill="#E8434A" text-anchor="middle">А</text>'
    f'<circle cx="44" cy="44" r="18" fill="#E9F6FF" fill-opacity=".8" stroke="#D8343E" stroke-width="5"/>'
    f'<circle cx="84" cy="44" r="18" fill="#E9F6FF" fill-opacity=".8" stroke="#D8343E" stroke-width="5"/>'
    f'<path d="M62 42 Q64 36 66 42" fill="none" stroke="#D8343E" stroke-width="4"/>'
    f'<path d="M26 40 L10 34 M102 40 L118 34" stroke="#D8343E" stroke-width="4" stroke-linecap="round"/>'
    + eye(46, 46, 0.8) + eye(86, 46, 0.8) + sparkle(110, 16, 5) + sparkle(18, 14, 4))

# Жуковский — бумажный самолётик из книжной страницы
I["cdb-zhukovsky-mayakovskogo"] = ("#E6F7FF", "#3C8FD0",
    "бумажный самолётик, сложенный из книжной страницы со строчками",
    "вылетает из раскрытой книги в голубое небо, оставляя пунктирный след-петлю",
    f'<path d="M64 120 L14 108 L14 88 L64 100Z" fill="#FFFDF5" {W(2.8)}/><path d="M64 120 L114 108 L114 88 L64 100Z" fill="#FFFDF5" {W(2.8)}/>'
    f'<path d="M64 124 L10 112 M64 124 L118 112" stroke="#2FA36B" stroke-width="5"/>'
    f'<path d="M50 96 Q30 70 46 58 Q62 50 58 66 Q54 80 70 70" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="4 4"/>'
    f'<path d="M58 54 L118 22 L84 70 L74 58Z" fill="#FFFFFF" {W(3)}/>'
    f'<path d="M58 54 L118 22 L74 58Z" fill="#F4F0E4" {W(2.4)}/>'
    f'<path d="M74 58 L80 76 L84 70" fill="#E3DCCB" {W(2.4)}/>'
    + "".join(f'<path d="M{70+i*8} {48-i*4} L{90+i*6} {38-i*3}" stroke="#B9AFA0" stroke-width="1.6"/>' for i in range(3))
    + eye(80, 48, 0.55) + eye(90, 43, 0.55) + f'<path d="M82 54 Q87 56 91 51" fill="none" stroke="{O}" stroke-width="1.8"/>'
    + sparkle(30, 26, 5) + sparkle(104, 84, 4))

# Красногорск ЦДБ №20 — кресло-мешок
I["cdb20-krasnogorsk-pionerskaya"] = ("#FFF0E2", "#E07A2E",
    "оранжевое кресло-мешок с мордашкой",
    "уютно обнимает раскрытую книжку с картинками, а рядом на полу стоит кружка какао",
    f'<path d="M-2 108 H130 V130 H-2Z" fill="#C9A27A" {W(3)}/>'
    f'<path d="M20 108 Q8 70 34 46 Q64 24 94 46 Q120 70 108 108Z" fill="#FF9A3C" {W(3.2)}/>'
    f'<path d="M40 50 Q64 38 88 50" fill="none" stroke="#FFC37A" stroke-width="4"/>'
    + face(64, 60, d=10, k=0.7) +
    f'<path d="M64 102 L38 94 L38 74 L64 82Z" fill="#FFFDF5" {W(2.6)}/><path d="M64 102 L90 94 L90 74 L64 82Z" fill="#FFFDF5" {W(2.6)}/>'
    f'<circle cx="50" cy="86" r="5" fill="#FFD84A"/><path d="M70 92 L78 82 L86 90Z" fill="#2FA36B"/>'
    f'<path d="M30 88 Q24 92 32 96 M98 88 Q104 92 96 96" fill="none" stroke="{O}" stroke-width="3"/>'
    f'<rect x="104" y="96" width="14" height="14" rx="3" fill="#E8434A" {W(2.2)}/><path d="M118 100 Q124 103 118 106" fill="none" stroke="{O}" stroke-width="2"/>'
    f'<path d="M108 92 Q110 86 108 82 M114 92 Q116 86 114 82" fill="none" stroke="#fff" stroke-width="2"/>' + sparkle(22, 26, 5))

# Балашиха — лесенка из книг
I["lib-kids-balashikha-sportivnaya"] = ("#F2FFF2", "#4FA37A",
    "лесенка из разноцветных книжек, сложенных ступеньками",
    "на самой верхней книжке сидит маленькое солнышко с мордашкой и болтает лучиками",
    "".join(f'<rect x="{10+i*18}" y="{100-i*14}" width="{108-i*18}" height="14" rx="2" fill="{c}" {W(2.6)}/>'
             f'<path d="M{14+i*18} {104-i*14} H{110} " stroke="#fff" stroke-width="1.6" opacity=".6"/>'
             for i, c in enumerate(("#E8434A", "#3F7FD8", "#F2B33A", "#9B59D0", "#2FA36B")))
    + f'<path d="M-2 114 H130" stroke="{O}" stroke-width="3"/>'
    f'<circle cx="104" cy="30" r="12" fill="#FFD84A" {W(2.8)}/>' + face(104, 30, d=4.5, k=0.45)
    + "".join(f'<path d="M{104+17*c:.1f} {30+17*s_:.1f} L{104+23*c:.1f} {30+23*s_:.1f}" stroke="#F2B33A" stroke-width="3"/>' for c, s_ in ((1, 0), (-1, 0), (0, -1), (0.7, -0.7), (-0.7, -0.7), (0.7, 0.7))) + sparkle(24, 30, 6) + sparkle(46, 18, 4))

# Ступино — книжка-парусник
I["lib-kids-stupino-timiryazeva"] = ("#E8F7FF", "#2E8FB8",
    "раскрытая книжка, поставленная парусом на бумажный кораблик, с мордашкой на корпусе",
    "плывёт по синим волнам, нарисованным строчками, к острову с одной пальмой",
    f'<path d="M-2 92 Q16 84 32 92 Q48 100 64 92 Q80 84 96 92 Q112 100 130 92 V130 H-2Z" fill="#3F8FD8" {W(3)}/>'
    + "".join(f'<path d="M{x} {y} H{x+18}" stroke="#BFE3FF" stroke-width="2.4"/>' for x, y in ((10, 104), (40, 112), (78, 106), (96, 118)))
    + f'<path d="M24 80 H104 L92 98 H36Z" fill="#FFFDF5" {W(3)}/>' + face(64, 88, d=8, k=0.5) +
    f'<path d="M64 80 V18" stroke="{O}" stroke-width="3"/>'
    f'<path d="M64 22 Q46 30 36 72 L64 76Z" fill="#FFFDF5" {W(2.8)}/><path d="M64 22 Q82 30 92 72 L64 76Z" fill="#FFFDF5" {W(2.8)}/>'
    + "".join(f'<path d="M{48+i*2} {40+i*10} L60 {42+i*10} M68 {42+i*10} L{80-i*2} {40+i*10}" stroke="#B9AFA0" stroke-width="1.6"/>' for i in range(3))
    + f'<path d="M64 18 L76 22 L64 26Z" fill="#E8434A" {W(1.8)}/>' + sparkle(104, 30, 5) + sparkle(18, 40, 4))


if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
