"""Иконки робота fun (2026-11-11, проход t): пеленальные комнаты и места из tools/add_fun_1111t.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя палитра фона.
Запуск: python3 tools/icons_fun_1111t.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye, O
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}


def stars(pts, r=3, c="#fff"):
    return "".join(sparkle(x, y, r, c) for x, y in pts)


# 1. Сад Баумана — вязаные пинетки танцуют на эстраде-ракушке
I["chg-sad-baumana"] = ("#FFF0F5", "#F5A3C0",
    "пара вязаных розовых пинеток с белыми помпончиками",
    "танцуют, подпрыгивая, на круглой эстраде-ракушке городского сада",
    f'<path d="M8 104 Q8 30 64 26 Q120 30 120 104Z" fill="#FFFFFF" {W(3)}/>'
    + "".join(f'<path d="M64 104 L{64 + 54 * __import__("math").cos(a):.0f} {104 - 74 * __import__("math").sin(a):.0f}" stroke="#F7C6D6" stroke-width="2.4"/>' for a in (0.5, 0.95, 1.4, 1.75, 2.2, 2.65)) +
    f'<rect x="0" y="100" width="128" height="28" fill="#C98A5A" {W(2.6)}/>'
    f'<path d="M24 92 Q22 62 38 60 Q50 60 50 74 L50 86 Q62 86 62 94 Q62 100 54 100 H30 Q24 100 24 92Z" fill="#FF8FB1" {W(3)} transform="rotate(-10 40 84)"/>'
    f'<path d="M66 82 Q64 52 80 50 Q92 50 92 64 L92 76 Q104 76 104 84 Q104 90 96 90 H72 Q66 90 66 82Z" fill="#FF8FB1" {W(3)} transform="rotate(12 84 74)"/>'
    f'<circle cx="38" cy="58" r="6" fill="#fff" {W(2.2)}/><circle cx="82" cy="48" r="6" fill="#fff" {W(2.2)}/>'
    + face(42, 82, d=5, k=0.55) + face(84, 72, d=5, k=0.55) +
    f'<path d="M14 64 l6 4 M108 50 l6 -4 M60 40 l0 -6" {W(2.4)}/>'
    + stars(((20, 40), (110, 30)), 3.2))

# 2. Сад «Эрмитаж» — мобиль над кроваткой крутится под садовой гирляндой
I["chg-sad-ermitazh"] = ("#3A3470", "#141235",
    "детский мобиль на деревянном кольце с плюшевыми звёздочкой, месяцем и облачком на ниточках",
    "плавно крутится, подвешенный к ветке под гирляндой жёлтых садовых лампочек ночью",
    f'<path d="M-4 22 Q64 44 132 22" fill="none" stroke="#1E1A40" stroke-width="2"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4.5" fill="#FFE27A" {W(1.6)}/>' for x, y in ((12, 26), (36, 32), (92, 32), (116, 26))) +
    f'<path d="M64 0 V30" stroke="#FFF7E0" stroke-width="2"/>'
    f'<ellipse cx="64" cy="36" rx="40" ry="9" fill="#D9A06A" {W(3)}/>'
    f'<path d="M30 40 V62 M64 45 V82 M98 40 V60" stroke="#FFF7E0" stroke-width="1.8"/>'
    + sparkle(30, 72, 12, "#FFD23F") +
    f'<path d="M92 56 Q110 66 100 84 Q114 80 112 64 Q106 52 92 56Z" fill="#FFF3B0" {W(2.4)}/>'
    f'<path d="M48 92 Q46 80 58 80 Q62 72 72 76 Q84 74 82 86 Q90 90 84 98 H52 Q44 98 48 92Z" fill="#FFFFFF" {W(2.6)}/>'
    + face(66, 88, d=7, k=0.6) +
    stars(((14, 100), (116, 106), (22, 52)), 2.6, "#FFF7C2"))

# 3. Музеон — муслиновая пелёнка-рулон на постаменте как скульптура
I["chg-muzeon"] = ("#F3EEE6", "#BFAF98",
    "голубая муслиновая пелёнка в белый горошек, свёрнутая мягким рулоном",
    "стоит на мраморном постаменте с табличкой посреди парка скульптур, как экспонат",
    f'<rect x="34" y="78" width="60" height="40" fill="#E8E4DC" {W(3)}/><rect x="28" y="72" width="72" height="9" fill="#F7F4EE" {W(2.6)}/>'
    f'<rect x="50" y="92" width="28" height="10" rx="2" fill="#D9B45A" {W(2)}/>'
    f'<path d="M40 72 V44 Q40 30 64 30 Q88 30 88 44 V72Z" fill="#9FD3F5" {W(3)}/>'
    f'<path d="M88 44 Q100 50 96 72" fill="#9FD3F5" {W(2.6)}/>'
    f'<ellipse cx="64" cy="44" rx="24" ry="9" fill="#C7E8FF" {W(2.6)}/><path d="M54 44 Q64 36 74 44 Q64 50 58 44" fill="none" {W(2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="#fff"/>' for x, y in ((48, 58), (60, 66), (74, 56), (82, 66), (52, 70))) +
    face(64, 58, d=8, k=0.65) +
    f'<path d="M8 118 V90 Q8 82 14 82 Q20 82 20 90 V118" fill="#9AA68A" {W(2)}/><path d="M112 118 V96 L120 86 V118" fill="#9AA68A" {W(2)}/>')

# 4. Северное Тушино — нагрудник-флаг на рубке подводной лодки
I["chg-severnoe-tushino"] = ("#CDEBFF", "#3C8CC4",
    "детский нагрудник-слюнявчик в жёлто-белую полоску с кармашком",
    "гордо развевается флагом на флагштоке над рубкой подводной лодки",
    f'<path d="M0 104 Q32 98 64 104 T128 104 V128 H0Z" fill="#2A6FA8" {W(2.4)}/>'
    f'<path d="M6 100 Q14 86 30 86 H104 Q120 86 124 100Z" fill="#4E5A6E" {W(3)}/>'
    f'<path d="M44 86 V66 Q44 60 50 60 H72 Q78 60 78 66 V86Z" fill="#5F6C82" {W(3)}/>'
    f'<circle cx="54" cy="74" r="4" fill="#BFE6FF" {W(1.8)}/><circle cx="68" cy="74" r="4" fill="#BFE6FF" {W(1.8)}/>'
    f'<path d="M60 60 V14" {W(3)}/>'
    f'<path d="M62 16 H104 Q100 30 104 44 H62Z" fill="#FFFFFF" {W(2.8)}/>'
    f'<path d="M62 23 H102 M62 37 H102" stroke="#FFD23F" stroke-width="5"/>'
    f'<path d="M62 16 H104 Q100 30 104 44 H62Z" fill="none" {W(2.8)}/>'
    f'<path d="M74 16 Q83 24 92 16" fill="#FFFFFF" {W(2.2)}/>'
    + face(83, 30, d=6, k=0.55) +
    f'<path d="M14 116 q6 -4 12 0 M90 118 q6 -4 12 0" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>')

# 5. Парк «Яуза» — прогулочная коляска катится по набережной
I["chg-park-yauza-severodvinskaya"] = ("#E9F7D9", "#8CCB6A",
    "зелёная прогулочная коляска с большим козырьком и мордашкой на люльке",
    "катится по набережной вдоль реки, а над ней покачивается ветка ивы",
    f'<path d="M0 98 H128 V128 H0Z" fill="#66B3D9" {W(2.2)}/><path d="M0 98 H128" stroke="#C99A6A" stroke-width="6"/>'
    f'<path d="M18 112 q6 -4 12 0 M80 118 q6 -4 12 0" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>'
    f'<path d="M96 0 Q98 22 92 44 M108 0 Q112 26 106 50 M118 0 Q122 20 120 40" fill="none" stroke="#4E9A3A" stroke-width="3"/>'
    f'<path d="M30 70 Q30 40 60 38 L66 70Z" fill="#2E9E5B" {W(3)}/>'
    f'<path d="M26 70 H90 Q90 88 72 88 H44 Q26 88 26 70Z" fill="#4CC07A" {W(3)}/>'
    f'<path d="M90 70 L100 50 H108" fill="none" {W(3.2)}/>'
    f'<path d="M40 88 L34 96 M76 88 L84 96" {W(2.6)}/>'
    f'<circle cx="34" cy="96" r="6" fill="#4A4A5A" {W(2.4)}/><circle cx="84" cy="96" r="6" fill="#4A4A5A" {W(2.4)}/>'
    + face(58, 78, d=8, k=0.7) +
    f'<path d="M8 60 l8 0 M12 66 l10 0" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>')

# 6. Синичка (Красногорск) — красный слинг-шарф с малышом на мостике
I["chg-park-sinichka-krasnogorsk"] = ("#FFF4D6", "#F2B84B",
    "красный тканевый слинг-шарф, завязанный узлом, из которого выглядывают макушка и ножки малыша",
    "переходит маленький деревянный мостик через речку, а рядом на перила села синичка",
    f'<path d="M0 108 Q30 102 64 108 T128 108 V128 H0Z" fill="#6BB8E0" {W(2)}/>'
    f'<rect x="4" y="90" width="120" height="8" rx="3" fill="#B5703A" {W(2.4)}/>'
    f'<path d="M14 98 V112 M114 98 V112 M14 72 V90 M114 72 V90" {W(3)}/><path d="M10 72 H118" {W(3.4)}/>'
    f'<path d="M30 30 Q64 20 98 30 L86 84 Q64 92 42 84Z" fill="#E8434A" {W(3)}/>'
    f'<path d="M36 46 Q64 38 92 46" fill="none" stroke="#B82A33" stroke-width="3"/>'
    f'<circle cx="64" cy="40" r="13" fill="#FFD9B8" {W(2.6)}/><path d="M52 36 Q64 22 76 36" fill="#8A5A3A" {W(2.2)}/>'
    + eye(59, 42, 0.5) + eye(69, 42, 0.5) +
    f'<path d="M61 47 Q64 50 67 47" fill="none" {W(1.8)}/>'
    f'<path d="M50 84 Q46 92 52 94 M78 84 Q82 92 76 94" fill="#FFD9B8" {W(2.4)}/>'
    f'<path d="M84 26 Q98 16 104 26 Q96 30 92 36Z" fill="#E8434A" {W(2.4)}/>'
    f'<ellipse cx="108" cy="64" rx="9" ry="7" fill="#FFD23F" {W(2)}/><circle cx="112" cy="58" r="5" fill="#2E3A5C" {W(1.8)}/><path d="M116 58 l4 1" {W(2)}/><path d="M100 66 l-6 2" {W(2)}/>')

# 7. Инженерный пруд (Дмитров) — аквашузы сохнут на мостках
I["chg-dmitrov-inzhenerny-prud"] = ("#D6FBF7", "#33BFB2",
    "пара детских бирюзовых аквашузов-тапочек для воды с прорезиненной подошвой",
    "сохнут на деревянных мостках у пруда, с носочков капают капельки",
    f'<path d="M0 92 H128 V128 H0Z" fill="#2E8FC9" {W(2)}/>'
    f'<rect x="0" y="76" width="128" height="12" fill="#D9A46A" {W(2.6)}/>'
    + "".join(f'<path d="M{x} 76 V88" {W(1.6)}/>' for x in (20, 44, 68, 92, 116)) +
    f'<path d="M26 88 V108 M100 88 V108" {W(4)}/>'
    f'<path d="M14 74 Q12 48 30 46 Q44 46 46 58 L56 60 Q62 62 60 70 L58 74Z" fill="#3FD6C8" {W(3)}/>'
    f'<path d="M14 74 H58" stroke="#3B3355" stroke-width="5"/><path d="M26 54 L40 50 M26 62 L44 58" stroke="#fff" stroke-width="2"/>'
    f'<path d="M68 74 Q66 44 84 42 Q98 42 100 54 L110 56 Q116 58 114 66 L112 74Z" fill="#FF9F43" {W(3)}/>'
    f'<path d="M68 74 H112" stroke="#3B3355" stroke-width="5"/><path d="M80 50 L94 46 M80 58 L98 54" stroke="#fff" stroke-width="2"/>'
    + face(34, 64, d=5, k=0.5) + face(88, 62, d=5, k=0.5) +
    f'<path d="M60 80 q-2 6 0 8 q2 -2 0 -8Z M114 80 q-2 6 0 8 q2 -2 0 -8Z" fill="#9FE6FF" {W(1.4)}/>'
    + sparkle(104, 24, 9, "#FFF3B0") + stars(((20, 26),), 3))

# 8. Павелецкая Плаза — эргорюкзак едет на эскалаторе
I["chg-paveletskaya-plaza"] = ("#F0E6FF", "#9A7CE0",
    "фиолетовый эргорюкзак-переноска с мягкими лямками и мордашкой на спинке",
    "едет вверх по эскалатору торгового центра, держась лямкой за поручень",
    f'<path d="M-4 120 L124 20 L132 30 L4 128Z" fill="#B9BED0" {W(2.6)}/>'
    + "".join(f'<path d="M{8 + i*16} {120 - i*12.5:.0f} l12 -2" stroke="#7D8296" stroke-width="2"/>' for i in range(8)) +
    f'<path d="M-4 104 L118 8" stroke="#3B3355" stroke-width="5" stroke-linecap="round"/>'
    f'<rect x="40" y="38" width="44" height="50" rx="14" fill="#8A5CD8" {W(3)} transform="rotate(-38 62 63)"/>'
    f'<rect x="48" y="48" width="28" height="22" rx="8" fill="#B79BF0" {W(2.2)} transform="rotate(-38 62 59)"/>'
    + face(62, 60, d=6, k=0.6) +
    f'<path d="M80 40 Q84 26 74 24" fill="none" stroke="#5B3CA8" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M46 80 Q40 92 50 96" fill="none" stroke="#5B3CA8" stroke-width="5" stroke-linecap="round"/>'
    + stars(((22, 30), (106, 70), (110, 92)), 3.2))

# 9. Станция МЦД Подольск — термосумка для бутылочек ждёт электричку под часами
I["chg-mcd-podolsk"] = ("#FFE7D6", "#F07E4F",
    "мягкая оранжевая термосумка для детских бутылочек на молнии, с ремешком",
    "стоит на платформе под круглыми станционными часами и ждёт электричку",
    f'<path d="M0 100 H128 V128 H0Z" fill="#A9A3B0" {W(2.2)}/><path d="M0 100 H128" stroke="#FFFFFF" stroke-width="4"/>'
    f'<path d="M92 0 V22" {W(3)}/><circle cx="92" cy="34" r="14" fill="#FFFFFF" {W(3)}/>'
    f'<path d="M92 34 V24 M92 34 L99 38" {W(2.4)}/>'
    f'<rect x="22" y="54" width="62" height="44" rx="12" fill="#FF8A3D" {W(3)}/>'
    f'<path d="M26 62 H80" stroke="#FFD23F" stroke-width="3" stroke-dasharray="4 3"/>'
    f'<path d="M34 54 Q53 26 72 54" fill="none" {W(3.4)}/>'
    + face(53, 80, d=9, k=0.8) +
    f'<rect x="64" y="40" width="10" height="20" rx="4" fill="#FFFFFF" {W(2)}/><path d="M66 40 Q69 32 72 40" fill="#FF9EB5" {W(1.6)}/>')

# 10. МЦД Остафьево — поильник на скамейке, подходит красная электричка
I["chg-mcd-ostafyevo"] = ("#E3F0FF", "#7A9CE8",
    "детский поильник-непроливайка с двумя ручками и мягким носиком",
    "сидит на скамейке платформы и машет ручкой подъезжающей красной электричке",
    f'<rect x="-6" y="30" width="80" height="44" rx="10" fill="#E8434A" {W(3)}/>'
    f'<rect x="4" y="38" width="16" height="14" rx="3" fill="#BFE6FF" {W(2)}/><rect x="26" y="38" width="16" height="14" rx="3" fill="#BFE6FF" {W(2)}/><rect x="48" y="38" width="16" height="14" rx="3" fill="#BFE6FF" {W(2)}/>'
    f'<path d="M-6 62 H74" stroke="#fff" stroke-width="3"/>'
    f'<path d="M0 108 H128 V128 H0Z" fill="#A9A3B0" {W(2)}/>'
    f'<rect x="60" y="92" width="64" height="7" rx="2" fill="#C98A5A" {W(2.4)}/><path d="M66 99 V110 M118 99 V110" {W(3)}/>'
    f'<path d="M80 92 V58 Q80 50 88 50 H100 Q108 50 108 58 V92Z" fill="#FFFFFF" {W(3)}/>'
    f'<path d="M82 74 H106 V88 Q106 92 100 92 H88 Q82 92 82 88Z" fill="#FFE07A"/>'
    f'<path d="M86 50 Q94 36 102 50Z" fill="#7FD0FF" {W(2.4)}/><path d="M94 40 L96 28 L100 30 L98 42" fill="#7FD0FF" {W(2)}/>'
    f'<path d="M80 62 Q70 58 70 48 M108 64 Q116 66 116 74" fill="none" stroke="#7FD0FF" stroke-width="5" stroke-linecap="round"/>'
    + face(94, 66, d=6, k=0.6) + stars(((112, 20),), 3.2))

# 11. МЦК Коптево — ползунки на вешалке в вагоне у окна
I["chg-mck-koptevo"] = ("#FFF9E0", "#E8C547",
    "детские ползунки в бело-зелёную клетку с кнопочками, на плечиках-вешалке",
    "висят на поручне вагона городской электрички у большого окна, за которым мелькают дома",
    f'<rect x="8" y="22" width="112" height="70" rx="10" fill="#BFE6FF" {W(3)}/>'
    f'<path d="M18 80 V60 H32 V80 M40 80 V50 H54 V80 M96 80 V56 H110 V80" fill="#9AA8C0" {W(2)}/>'
    f'<path d="M0 14 H128" stroke="#C0C4D0" stroke-width="6"/><path d="M0 14 H128" {W(1.6)}/>'
    f'<path d="M64 14 V24 M50 32 L64 24 L78 32" fill="none" {W(2.6)}/>'
    f'<path d="M44 32 H84 L88 52 L80 54 V108 H68 L64 84 L60 108 H48 V54 L40 52Z" fill="#FFFFFF" {W(3)}/>'
    + "".join(f'<path d="M{x} 34 V106" stroke="#7FD68A" stroke-width="2.4"/>' for x in (54, 64, 74)) +
    "".join(f'<path d="M46 {y} H82" stroke="#7FD68A" stroke-width="2.4"/>' for y in (44, 64, 84)) +
    f'<path d="M44 32 H84 L88 52 L80 54 V108 H68 L64 84 L60 108 H48 V54 L40 52Z" fill="none" {W(3)}/>'
    + face(64, 56, d=7, k=0.65) +
    f'<rect x="0" y="100" width="128" height="28" fill="#6C7A8F" {W(2)}/>')

# 12. Станция Подсолнечная — детский горшок под подсолнухом
I["chg-podsolnechnaya"] = ("#FCEBDD", "#D98C5F",
    "голубой детский горшок с ручкой и крышечкой",
    "стоит на перроне под огромным подсолнухом рядом со станционной табличкой",
    f'<path d="M0 104 H128 V128 H0Z" fill="#B0A69E" {W(2)}/>'
    f'<path d="M96 104 V30" stroke="#4E9A3A" stroke-width="5"/>'
    f'<path d="M96 70 Q110 60 118 68 Q108 76 96 74Z" fill="#6CC04A" {W(2)}/>'
    + "".join(f'<ellipse cx="{96 + 15*__import__("math").cos(a*0.785):.1f}" cy="{30 + 15*__import__("math").sin(a*0.785):.1f}" rx="7" ry="4" fill="#FFD23F" {W(1.6)} transform="rotate({a*45} {96 + 15*__import__("math").cos(a*0.785):.1f} {30 + 15*__import__("math").sin(a*0.785):.1f})"/>' for a in range(8)) +
    f'<circle cx="96" cy="30" r="10" fill="#8A5A2E" {W(2.2)}/>'
    f'<rect x="8" y="22" width="40" height="14" rx="2" fill="#2E6FB8" {W(2.2)}/><path d="M28 36 V60" {W(3)}/>'
    f'<path d="M14 29 H42" stroke="#fff" stroke-width="2.4"/>'
    f'<ellipse cx="50" cy="74" rx="30" ry="8" fill="#9ED8FF" {W(3)}/>'
    f'<path d="M22 76 Q26 104 50 104 Q74 104 78 76" fill="#5BB8F0" {W(3)}/>'
    f'<path d="M78 82 Q92 84 88 94 Q84 98 76 94" fill="none" {W(3)}/>'
    + face(50, 88, d=8, k=0.7))

# 13. Аэропорт Домодедово — детский чемодан-самокат катится по взлётной полосе
I["chg-aeroport-domodedovo"] = ("#E6F0F5", "#7A9AAE",
    "детский жёлтый чемодан-самокат на колёсиках с рулём-ручкой и мордашкой",
    "катится по взлётной полосе, а над ним взлетает маленький самолётик",
    f'<path d="M0 100 H128 V128 H0Z" fill="#5E6670" {W(2)}/>'
    + "".join(f'<rect x="{x}" y="111" width="14" height="4" fill="#fff"/>' for x in (6, 34, 62, 90, 118)) +
    f'<path d="M84 30 L112 22 L116 26 L92 38Z" fill="#FFFFFF" {W(2)}/><path d="M96 26 L92 16 L98 18 L104 25" fill="#E8434A" {W(1.8)}/>'
    f'<path d="M98 34 L104 42 L108 40 L104 31" fill="#E8434A" {W(1.6)}/>'
    f'<path d="M66 32 q8 2 16 0" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 3"/>'
    f'<rect x="26" y="52" width="58" height="42" rx="10" fill="#FFC93C" {W(3)}/>'
    f'<path d="M30 64 H80" stroke="#F29A2E" stroke-width="3"/>'
    f'<path d="M84 60 L96 40 M90 40 H102" {W(3.4)}/>'
    f'<circle cx="36" cy="98" r="6" fill="#3B3355"/><circle cx="74" cy="98" r="6" fill="#3B3355"/>'
    + face(55, 78, d=9, k=0.8) +
    f'<path d="M10 82 h10 M6 90 h12" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>')

# 14. Аэропорт Шереметьево — автолюлька едет по багажной ленте
I["chg-aeroport-sheremetyevo"] = ("#FFE0E6", "#E05A78",
    "малиновая автолюлька-переноска с дугой-ручкой и мягким козырьком",
    "едет по ленте выдачи багажа среди чемоданов, а малыш внутри машет ручкой",
    f'<rect x="-4" y="92" width="136" height="16" rx="8" fill="#5E6670" {W(3)}/>'
    + "".join(f'<path d="M{x} 92 V108" stroke="#8A929C" stroke-width="2"/>' for x in range(8, 128, 14)) +
    f'<rect x="-6" y="62" width="22" height="30" rx="4" fill="#4E8FD6" {W(2.6)}/><rect x="104" y="56" width="26" height="36" rx="4" fill="#5FBF6A" {W(2.6)}/>'
    f'<path d="M30 92 Q26 62 46 56 H86 Q102 60 98 92Z" fill="#E8436A" {W(3)}/>'
    f'<path d="M38 60 Q50 30 82 40 L86 56" fill="#C82E55" {W(2.6)}/>'
    f'<path d="M30 76 Q64 30 98 76" fill="none" stroke="#3B3355" stroke-width="5"/>'
    f'<circle cx="66" cy="70" r="11" fill="#FFD9B8" {W(2.4)}/>' + eye(62, 69, 0.5) + eye(70, 69, 0.5) +
    f'<path d="M63 74 Q66 77 69 74" fill="none" {W(1.8)}/>'
    f'<path d="M80 74 L92 62" stroke="#3B3355" stroke-width="6" stroke-linecap="round"/><path d="M80 74 L92 62" stroke="#FFD9B8" stroke-width="3" stroke-linecap="round"/>'
    + stars(((20, 30), (108, 28)), 3.2))

# 15. Аэропорт Внуково — подушка-подкова в кресле у иллюминатора
I["chg-aeroport-vnukovo"] = ("#FFFFFF", "#C5D6E8",
    "мягкая детская подушка-подкова для путешествий в голубой горошек",
    "сидит в самолётном кресле у иллюминатора, а за окном проплывают облака",
    f'<rect x="64" y="14" width="44" height="58" rx="22" fill="#5E6670" {W(3)}/>'
    f'<rect x="70" y="20" width="32" height="46" rx="16" fill="#9FD8FF" {W(2.2)}/>'
    f'<path d="M74 48 Q78 40 86 44 Q92 38 98 46 Q102 52 96 54 H78 Q72 54 74 48Z" fill="#FFFFFF"/>'
    f'<path d="M18 120 V54 Q18 40 32 40 H50 Q62 40 62 54 V120Z" fill="#2E4E8A" {W(3)}/>'
    f'<rect x="14" y="96" width="56" height="12" rx="5" fill="#25406F" {W(2.6)}/>'
    f'<path d="M22 66 Q22 44 40 44 Q58 44 58 66 Q58 74 52 74 Q48 74 48 66 Q48 58 40 58 Q32 58 32 66 Q32 74 28 74 Q22 74 22 66Z" fill="#8EC5FF" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="#fff"/>' for x, y in ((28, 54), (40, 48), (52, 54), (26, 66), (54, 66))) +
    face(40, 52, d=6, k=0.5) + stars(((112, 90), (98, 110)), 3, "#8EC5FF"))

# 16. «Белый Кролик» (Коломна) — неоновый кот убегает по тёмному коридору
I["fun-belyy-krolik-kolomna"] = ("#301040", "#12061C",
    "светящийся неоновый кот из розовых и голубых линий",
    "крадётся по тёмному коридору квеста, оставляя за собой светящиеся следы лапок",
    f'<path d="M0 100 L40 76 H88 L128 100Z" fill="#1E0A2C"/>'
    f'<rect x="44" y="30" width="40" height="46" rx="4" fill="none" stroke="#3FE0FF" stroke-width="3" opacity=".7"/>'
    f'<path d="M30 70 Q30 50 46 48 L42 36 L54 46 H66 L78 36 L74 48 Q88 50 88 70 Q88 86 70 86 H48 Q30 86 30 70Z" fill="#2A1640" stroke="#FF4FD8" stroke-width="5" stroke-linejoin="round"/>'
    f'<path d="M88 74 Q108 70 104 50" fill="none" stroke="#FF4FD8" stroke-width="5" stroke-linecap="round"/>'
    + eye(50, 64, 0.8) + eye(68, 64, 0.8) +
    f'<path d="M55 74 Q59 78 63 74" fill="none" stroke="#3FE0FF" stroke-width="3" stroke-linecap="round"/>'
    f'<path d="M38 66 H24 M38 72 H26 M80 66 H94" stroke="#3FE0FF" stroke-width="2.4" stroke-linecap="round"/>'
    + "".join(f'<g fill="#9BFF4F"><circle cx="{x}" cy="{y}" r="3"/><circle cx="{x-4}" cy="{y-5}" r="1.6"/><circle cx="{x}" cy="{y-6}" r="1.6"/><circle cx="{x+4}" cy="{y-5}" r="1.6"/></g>' for x, y in ((20, 108), (40, 100), (100, 108), (114, 116))))

# 17. «Квесторий» (Коломна) — свиток-шифровка разворачивается сам
I["fun-kvestoriy-kolomna"] = ("#F3E2C0", "#A9773F",
    "старинный свиток-шифровка с большим вопросительным знаком, перевязанный красной лентой",
    "сам разворачивается на столе сыщика, и из него вылетают цифры кода",
    f'<rect x="0" y="100" width="128" height="28" fill="#7A4A26" {W(2)}/>'
    f'<path d="M30 30 H98 V92 H30Z" fill="#FFF3D6" {W(3)}/>'
    f'<rect x="24" y="22" width="80" height="12" rx="6" fill="#E9C98E" {W(2.8)}/><rect x="24" y="88" width="80" height="12" rx="6" fill="#E9C98E" {W(2.8)}/>'
    f'<path d="M52 50 Q52 38 64 38 Q76 38 76 48 Q76 56 66 60 V68" fill="none" stroke="#C0392B" stroke-width="6" stroke-linecap="round"/>'
    f'<circle cx="66" cy="78" r="3.6" fill="#C0392B"/>'
    f'<path d="M100 94 Q112 100 108 112 M104 96 Q118 98 120 108" fill="none" stroke="#E8434A" stroke-width="4" stroke-linecap="round"/>'
    + eye(44, 62, 0.6) + eye(86, 62, 0.6) +
    f'<text x="10" y="24" font-family="Arial" font-weight="bold" font-size="13" fill="#5A3A1A">7</text>'
    f'<text x="108" y="22" font-family="Arial" font-weight="bold" font-size="12" fill="#5A3A1A">3</text>'
    f'<text x="8" y="70" font-family="Arial" font-weight="bold" font-size="11" fill="#5A3A1A">9</text>')

# 18. «Королевство праздников» (Химки) — торт-замок с башенками
I["fun-korolevstvo-prazdnikov-khimki"] = ("#FFE3F7", "#E77FD0",
    "праздничный торт-замок с тремя башенками из бисквита и розовым кремом-стенами",
    "на башенках горят свечки-факелы и вьются флажки, а над воротами-печеньем висит гирлянда",
    f'<rect x="20" y="64" width="88" height="44" rx="6" fill="#FFB3D9" {W(3)}/>'
    f'<path d="M20 74 Q30 82 40 74 Q50 82 60 74 Q70 82 80 74 Q90 82 100 74 Q104 78 108 74" fill="none" stroke="#fff" stroke-width="4"/>'
    f'<rect x="14" y="40" width="22" height="68" rx="4" fill="#FFD7EC" {W(3)}/><rect x="92" y="40" width="22" height="68" rx="4" fill="#FFD7EC" {W(3)}/>'
    f'<rect x="52" y="30" width="24" height="40" rx="4" fill="#FFD7EC" {W(3)}/>'
    + "".join(f'<path d="M{x} {y} v-6 h4 v6 h4 v-6 h4 v6 h4 v-6 h4 v6" fill="none" {W(2.2)}/>' for x, y in ((15, 40), (93, 40), (53, 30))) +
    f'<path d="M54 108 V92 Q64 80 74 92 V108Z" fill="#C98A5A" {W(2.6)}/>'
    + "".join(f'<path d="M{x} {y} v-12" {W(2.4)}/><path d="M{x} {y-12} l12 4 l-12 4Z" fill="{c}" {W(1.8)}/>' for x, y, c in ((25, 34, "#FFD23F"), (103, 34, "#3FA9F5"), (64, 24, "#E8434A"))) +
    "".join(f'<rect x="{x-2}" y="{y}" width="4" height="10" fill="#FFF3B0" {W(1.4)}/><path d="M{x} {y-6} q3 3 0 6 q-3 -3 0 -6Z" fill="#FF9A3C"/>' for x, y in ((40, 54), (88, 54))) +
    face(64, 52, d=6, k=0.6) + stars(((10, 20), (116, 18)), 3.2))

# 19. Студия Макаровой (Коломна) — батик: шёлковый платок на раме
I["fun-studiya-makarovoy-kolomna"] = ("#E0FFF0", "#4CC38A",
    "шёлковый платок на деревянной раме для батика, натянутый как барабан",
    "кисточка с краской рисует на нём большой ярко-красный цветок, а краска растекается каплями",
    f'<rect x="16" y="20" width="84" height="84" rx="4" fill="#C98A5A" {W(3)}/>'
    f'<rect x="24" y="28" width="68" height="68" fill="#FFFBF2" {W(2.4)}/>'
    + "".join(f'<ellipse cx="{58 + 13*__import__("math").cos(a*1.257):.1f}" cy="{62 + 13*__import__("math").sin(a*1.257):.1f}" rx="10" ry="7" fill="#F2545B" {W(2)} transform="rotate({a*72} {58 + 13*__import__("math").cos(a*1.257):.1f} {62 + 13*__import__("math").sin(a*1.257):.1f})"/>' for a in range(5)) +
    f'<circle cx="58" cy="62" r="8" fill="#FFD23F" {W(2)}/>'
    + face(58, 60, d=4, k=0.4, blush=False) +
    f'<path d="M78 84 q-3 6 0 8 q3 -2 0 -8Z" fill="#3FA9F5"/><path d="M34 40 q-3 6 0 8 q3 -2 0 -8Z" fill="#8E5CE0"/>'
    f'<path d="M84 76 L118 34" stroke="#D9A46A" stroke-width="7" stroke-linecap="round"/><path d="M84 76 L118 34" {W(1.8)}/>'
    f'<path d="M78 84 L84 74 L88 78Z" fill="#F2545B" {W(2)}/>')

# 20. Chalet Studio — первая кривоватая детская мисочка с отпечатком пальчика
I["fun-chalet-studio"] = ("#F4E9DE", "#C49A7A",
    "первая детская глиняная мисочка — кривоватая, с волнистым краем и отпечатком маленького пальчика",
    "гордо стоит на гончарном круге, ещё мокрая и блестящая, а рядом лежит деревянная стека",
    f'<ellipse cx="64" cy="98" rx="52" ry="14" fill="#8C8C96" {W(3)}/><ellipse cx="64" cy="94" rx="46" ry="11" fill="#B9B9C2" {W(2.4)}/>'
    f'<path d="M24 56 Q30 50 40 56 Q50 48 62 56 Q74 48 86 56 Q96 50 104 56 Q100 92 64 92 Q28 92 24 56Z" fill="#D88B5A" {W(3)}/>'
    f'<path d="M26 58 Q64 68 102 58" fill="none" stroke="#B5663A" stroke-width="3"/>'
    f'<ellipse cx="86" cy="76" rx="5" ry="6" fill="#C2723F"/><path d="M83 74 q3 -2 6 0 M83 78 q3 -2 6 0" fill="none" stroke="#9A522A" stroke-width="1.2"/>'
    + face(58, 72, d=8, k=0.75) +
    f'<path d="M14 116 L50 104" stroke="#C99A5A" stroke-width="6" stroke-linecap="round"/><path d="M14 116 L50 104" {W(1.6)}/>'
    f'<path d="M40 40 q4 -4 8 0 M76 38 q4 -4 8 0" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'
    + stars(((18, 30), (110, 34)), 3.2))

# 21. Nukus Games (Котельники) — светящаяся плитка пола загорается под кроссовкой
I["fun-nukus-games-kotelniki"] = ("#0F2238", "#06101C",
    "светящаяся квадратная плитка игрового пола с мордашкой",
    "вспыхивает ярко-зелёным, когда на неё прыгает детская кроссовка, а соседние плитки горят красным",
    "".join(f'<rect x="{x}" y="{y}" width="26" height="26" rx="3" fill="{c}" opacity=".9" stroke="#0A1626" stroke-width="2"/>'
            for x, y, c in ((4, 72, "#E8434A"), (32, 72, "#2B3F5C"), (88, 72, "#2B3F5C"), (4, 100, "#2B3F5C"), (32, 100, "#E8434A"),
                            (60, 100, "#2B3F5C"), (88, 100, "#E8434A"), (116, 72, "#2B3F5C"), (116, 100, "#2B3F5C"))) +
    f'<rect x="56" y="66" width="32" height="32" rx="4" fill="#4CFF7A" {W(3)}/>'
    f'<rect x="50" y="60" width="44" height="44" rx="8" fill="none" stroke="#4CFF7A" stroke-width="2" opacity=".5"/>'
    + face(72, 82, d=6, k=0.6) +
    f'<path d="M56 46 Q54 30 68 28 L84 30 Q94 34 94 44 Q94 52 84 52 H60 Q56 52 56 46Z" fill="#FFFFFF" {W(3)}/>'
    f'<path d="M56 46 H94" stroke="#3FE0FF" stroke-width="5"/><path d="M66 32 L74 40 M72 30 L80 38" {W(2)}/>'
    f'<path d="M60 58 V54 M76 58 V54 M90 58 V54" stroke="#4CFF7A" stroke-width="2.4" stroke-linecap="round"/>'
    + stars(((20, 26), (110, 22), (24, 52)), 3, "#4CFF7A"))

# 22. Арт-студия «Огни» (Коптево) — огонёк-свечка в берете рисует на холсте
I["fun-art-studiya-ogni-koptevo"] = ("#FFF2B8", "#FFC83D",
    "огонёк-язычок пламени в синем берете художника",
    "стоит на маленьком мольберте-подставке и выводит кисточкой на холсте яркое солнышко",
    f'<path d="M14 116 L30 40 M46 116 L30 40" {W(3)}/><rect x="10" y="34" width="44" height="48" rx="3" fill="#FFFFFF" {W(3)}/>'
    f'<circle cx="32" cy="56" r="9" fill="#FF9A3C"/>' + "".join(f'<path d="M{32 + 12*__import__("math").cos(a*0.785):.0f} {56 + 12*__import__("math").sin(a*0.785):.0f} L{32 + 17*__import__("math").cos(a*0.785):.0f} {56 + 17*__import__("math").sin(a*0.785):.0f}" stroke="#FF9A3C" stroke-width="2.4" stroke-linecap="round"/>' for a in range(8)) +
    f'<path d="M84 104 Q62 98 66 72 Q70 54 84 40 Q86 56 96 62 Q108 72 104 88 Q100 104 84 104Z" fill="#FF6F3C" {W(3)}/>'
    f'<path d="M84 98 Q74 92 76 80 Q80 70 86 66 Q90 76 96 80 Q98 92 84 98Z" fill="#FFD23F"/>'
    + face(85, 84, d=6, k=0.6) +
    f'<ellipse cx="86" cy="46" rx="16" ry="6" fill="#2E5FD8" {W(2.6)} transform="rotate(-10 86 46)"/><path d="M88 40 l2 -6" {W(2.4)}/>'
    f'<path d="M66 80 L48 64" stroke="#C98A5A" stroke-width="4" stroke-linecap="round"/><path d="M48 64 l-4 -3" stroke="#FF9A3C" stroke-width="4" stroke-linecap="round"/>'
    f'<rect x="60" y="104" width="50" height="8" rx="3" fill="#B5703A" {W(2.2)}/>')

# 23. «Арт-точка» (Электросталь) — пластилиновая улитка оставляет цветной след
I["fun-art-tochka-elektrostal"] = ("#E5F5FF", "#5EC3F0",
    "пластилиновая улитка с полосатым разноцветным домиком-спиралью",
    "ползёт по белому листу бумаги и оставляет за собой дорожку из цветных точек",
    f'<path d="M-4 84 L132 70 V128 H-4Z" fill="#FFFFFF" {W(2.6)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="{c}"/>' for x, y, c in ((10, 100, "#E8434A"), (24, 98, "#FFD23F"), (38, 96, "#4CC07A"), (52, 94, "#8E5CE0"))) +
    f'<path d="M58 96 Q60 84 74 84 H106 Q118 84 118 74 L112 70 Q112 80 104 80 H74 Q56 80 52 92Z" fill="#9BE07A" {W(3)}/>'
    f'<path d="M108 74 L104 56 M116 72 L120 56" {W(2.6)}/><circle cx="104" cy="54" r="4" fill="#9BE07A" {W(2)}/><circle cx="120" cy="54" r="4" fill="#9BE07A" {W(2)}/>'
    f'<circle cx="84" cy="62" r="24" fill="#FF8FB1" {W(3)}/>'
    f'<path d="M84 62 m0 -6 a6 6 0 1 1 -6 6 a12 12 0 1 1 12 12 a18 18 0 1 1 -18 -18" fill="none" stroke="#FFD23F" stroke-width="4" stroke-linecap="round"/>'
    + eye(102, 76, 0.5) + eye(110, 76, 0.5) +
    f'<path d="M102 80 Q106 83 110 80" fill="none" {W(1.6)}/>'
    + stars(((20, 30), (50, 20)), 3.2))

# 24. «Гончар-Ко» — глиняный поросёнок-копилка ловит монетку
I["fun-gonchar-ko"] = ("#EAF4D3", "#A3C46A",
    "глиняный поросёнок-копилка цвета терракоты с пятачком и щелью на спинке",
    "довольно ловит спинкой золотую монетку, которая падает сверху",
    f'<ellipse cx="62" cy="80" rx="38" ry="28" fill="#D9824F" {W(3)}/>'
    f'<rect x="56" y="52" width="16" height="4" rx="2" fill="#5A2E1A"/>'
    f'<ellipse cx="96" cy="80" rx="10" ry="9" fill="#E8A07A" {W(2.6)}/><circle cx="93" cy="80" r="2" fill="{O}"/><circle cx="99" cy="80" r="2" fill="{O}"/>'
    f'<path d="M40 56 L36 42 L50 52Z M70 54 L76 40 L82 54Z" fill="#D9824F" {W(2.4)}/>'
    f'<path d="M38 104 V114 M54 106 V114 M70 106 V114 M84 104 V114" stroke="#3B3355" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M24 76 q-10 -4 -6 -12 q6 4 0 8" fill="none" {W(2.4)}/>'
    + eye(68, 72, 0.7) + eye(82, 72, 0.7) +
    f'<ellipse cx="62" cy="88" rx="5" ry="3" fill="#FF7FA8" opacity=".6"/>'
    f'<circle cx="64" cy="28" r="11" fill="#FFD23F" {W(2.6)}/><path d="M64 22 V34" stroke="#E0A800" stroke-width="3"/>'
    f'<path d="M58 44 v-4 M70 44 v-4" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'
    + stars(((22, 26), (106, 30)), 3.2))

# 25. Студия Жилиной (Котельники) — тарелочка с отпечатком листа сохнет на подоконнике
I["fun-goncharnaya-zhilinoy-kotelniki"] = ("#DDF4E4", "#5E9E74",
    "круглая глиняная тарелочка с отпечатком кленового листа",
    "сохнет на подоконнике под солнышком, рядом в окне качается ветка клёна",
    f'<rect x="10" y="10" width="108" height="86" rx="6" fill="#BFE6FF" {W(3)}/><path d="M64 10 V96 M10 52 H118" {W(3)}/>'
    + sparkle(96, 30, 10, "#FFE27A") +
    f'<path d="M12 40 Q30 34 40 22" fill="none" stroke="#7A4A26" stroke-width="3"/><path d="M30 30 l6 -8 l2 6 l6 -2 l-4 6 l6 2 l-8 2Z" fill="#F2A23C" {W(1.6)}/>'
    f'<rect x="0" y="96" width="128" height="12" fill="#FFFFFF" {W(3)}/><rect x="0" y="108" width="128" height="20" fill="#E8DCC8" {W(2)}/>'
    f'<ellipse cx="64" cy="82" rx="40" ry="16" fill="#E9B98A" {W(3)}/><ellipse cx="64" cy="80" rx="30" ry="10" fill="#F2CFA6" {W(2)}/>'
    f'<path d="M64 72 l6 4 l6 -2 l-2 6 l6 2 l-8 2 l0 4 l-8 -4 l-8 4 l0 -4 l-8 -2 l6 -2 l-2 -6 l6 2Z" fill="#C88A5A" opacity=".8"/>'
    + face(64, 86, d=12, k=0.55, mouth=False))

# 26. «МариАрт» (Некрасовка) — коробочка аквагрима выпускает звёзды
I["fun-mariart-nekrasovka"] = ("#FFE6EC", "#B23A5A",
    "раскрытая коробочка аквагрима с шестью круглыми красками и зеркальцем в крышке",
    "стоит на сцене между бархатными кулисами, и из красок вылетают разноцветные звёздочки",
    f'<path d="M0 0 H22 Q18 60 26 128 H0Z M128 0 H106 Q110 60 102 128 H128Z" fill="#8A1C3A" {W(2.4)}/>'
    f'<rect x="30" y="20" width="68" height="38" rx="6" fill="#4A4A5A" {W(3)}/><rect x="36" y="26" width="56" height="26" rx="4" fill="#CFE8F5" {W(2)}/>'
    f'<path d="M42 46 L56 30" stroke="#fff" stroke-width="3" opacity=".7"/>'
    f'<rect x="30" y="60" width="68" height="42" rx="6" fill="#4A4A5A" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="8" fill="{c}" {W(2)}/>' for x, y, c in ((44, 72, "#FF5A7A"), (64, 72, "#FFD23F"), (84, 72, "#4CC07A"), (44, 90, "#3FA9F5"), (64, 90, "#9B6BFF"), (84, 90, "#FFFFFF"))) +
    f'<rect x="20" y="104" width="88" height="24" fill="#C98A5A" {W(2.4)}/>'
    + eye(56, 40, 0.6) + eye(72, 40, 0.6) +
    f'<path d="M61 46 Q64 49 67 46" fill="none" {W(1.8)}/>'
    + stars(((48, 12), (80, 10), (112, 50)), 3.6, "#FFD23F"))

# 27. «Рисуют Все!» (Щёлково) — стакан с радужной водой и кисточками
I["fun-risuyut-vse-shchelkovo"] = ("#EEF0FF", "#6C74D8",
    "прозрачный стаканчик для воды, в котором вода разноцветная, как радуга",
    "из него торчат три кисточки, и стаканчик весело брызгает цветными каплями на лист",
    f'<rect x="8" y="96" width="112" height="32" fill="#FFFFFF" {W(2.6)}/>'
    f'<path d="M86 44 L74 14 M64 44 L64 10 M42 44 L52 16" stroke="#D9A46A" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M74 14 l-3 -8 M64 10 v-8 M52 16 l3 -8" stroke="#3B3355" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M38 40 H90 L84 102 H44Z" fill="#FFFFFF" opacity=".6" {W(3)}/>'
    f'<path d="M40 56 H88 L86 70 H42Z" fill="#FF6F6F"/><path d="M42 70 H86 L85 84 H43Z" fill="#FFD23F"/><path d="M43 84 H85 L84 100 H44Z" fill="#4CC07A"/>'
    f'<path d="M38 40 H90 L84 102 H44Z" fill="none" {W(3)}/>'
    + face(64, 76, d=8, k=0.7) +
    f'<circle cx="20" cy="108" r="5" fill="#FF6F6F"/><circle cx="104" cy="112" r="6" fill="#3FA9F5"/><circle cx="112" cy="102" r="3" fill="#9B6BFF"/>'
    f'<path d="M24 64 q-6 4 -4 10 M104 60 q6 4 4 10" fill="none" stroke="#3FA9F5" stroke-width="3" stroke-linecap="round"/>')

if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
