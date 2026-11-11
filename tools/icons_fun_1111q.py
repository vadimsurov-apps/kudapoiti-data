"""Иконки робота fun (2026-11-11, проход q): пеленальные комнаты и места из tools/add_fun_1111q.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя палитра фона.
Запуск: python3 tools/icons_fun_1111q.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye, O
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}


def stars(pts, r=3, c="#fff"):
    return "".join(sparkle(x, y, r, c) for x, y in pts)


# 1. Ривьера — подгузник-кораблик на реке
I["chg-trc-riviera"] = ("#D8F1FF", "#5BB4E8",
    "белый подгузник, сложенный бумажным корабликом, с голубыми липучками-бортами",
    "плывёт по речным волнам с флажком-сердечком на мачте",
    f'<path d="M0 92 Q16 84 32 92 T64 92 T96 92 T128 92 V128 H0Z" fill="#2E86C9" {W(2.6)}/>'
    f'<path d="M24 70 H104 L90 98 H38Z" fill="#FFFFFF" {W(3.2)}/>'
    f'<path d="M24 70 L38 80 H90 L104 70" fill="none" {W(2.4)}/>'
    f'<rect x="28" y="72" width="10" height="7" rx="2" fill="#7FD0FF" {W(1.8)}/><rect x="90" y="72" width="10" height="7" rx="2" fill="#7FD0FF" {W(1.8)}/>'
    + face(64, 86, d=9, k=0.85) +
    f'<path d="M64 70 V34" {W(3)}/><path d="M64 34 L86 42 L64 50Z" fill="#FF6F91" {W(2.4)}/>'
    f'<path d="M73 40 q2 -3 4 0 q2 -3 4 0 q0 3 -4 5 q-4 -2 -4 -5Z" fill="#fff"/>'
    f'<path d="M14 108 q6 -4 12 0 M96 112 q6 -4 12 0" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'
    + stars(((22, 30), (106, 26), (100, 56)), 3.4))

# 2. Outlet Village Белая Дача — бодик на бельевой верёвке между берёзками
I["chg-outlet-belaya-dacha"] = ("#E6F8E0", "#7CC57A",
    "белоснежный детский бодик с короткими рукавчиками и мордашкой на груди",
    "сушится на бельевой верёвке на двух прищепках между двумя берёзками у дачного штакетника",
    f'<path d="M0 100 H128 V128 H0Z" fill="#5DA84E" {W(2.4)}/>'
    + "".join(f'<path d="M{x} 100 V84 l4 -5 l4 5 V100" fill="#F5E6C8" {W(2)}/>' for x in (6, 18, 30, 86, 98, 110)) +
    f'<rect x="12" y="26" width="9" height="78" fill="#FFFFFF" {W(2.4)}/><rect x="107" y="26" width="9" height="78" fill="#FFFFFF" {W(2.4)}/>'
    f'<path d="M12 44 h5 M16 62 h5 M12 80 h4 M107 50 h5 M111 70 h5 M107 88 h4" {W(2.4)}/>'
    f'<circle cx="16" cy="22" r="11" fill="#A6DB73" {W(2.4)}/><circle cx="112" cy="22" r="11" fill="#A6DB73" {W(2.4)}/>'
    f'<path d="M20 36 Q64 46 108 36" fill="none" {W(2.4)}/>'
    f'<path d="M44 40 L36 50 L44 56 V92 Q44 100 52 100 H76 Q84 100 84 92 V56 L92 50 L84 40 Q76 46 64 46 Q52 46 44 40Z" fill="#FFFFFF" {W(3)}/>'
    f'<path d="M58 92 Q64 97 70 92" fill="none" {W(2.2)}/><circle cx="58" cy="94" r="1.6" fill="{O}"/><circle cx="70" cy="94" r="1.6" fill="{O}"/>'
    f'<rect x="47" y="35" width="5" height="12" rx="1.5" fill="#F2A541" {W(1.8)}/><rect x="76" y="35" width="5" height="12" rx="1.5" fill="#F2A541" {W(1.8)}/>'
    + face(64, 66, d=8, k=0.85))

# 3. МЕГА Химки — бутылочка с молоком в магазинной тележке
I["chg-mega-khimki"] = ("#FFF6C9", "#F2C230",
    "детская бутылочка с молоком, розовой соской и шкалой делений",
    "едет, улыбаясь, в магазинной тележке по торговому центру",
    f'<path d="M60 12 Q64 4 68 12 L70 22 H58Z" fill="#FF9EB5" {W(2.4)}/>'
    f'<rect x="54" y="22" width="20" height="9" rx="3" fill="#7FC8F8" {W(2.4)}/>'
    f'<rect x="50" y="31" width="28" height="52" rx="10" fill="#FFFFFF" {W(3)}/>'
    f'<path d="M52 50 H76 V73 Q76 81 68 81 H60 Q52 81 52 73Z" fill="#FFFBEF"/>'
    f'<path d="M70 38 h5 M70 46 h5 M70 54 h5" {W(1.8)}/>'
    + face(62, 60, d=6, k=0.7) +
    f'<path d="M22 58 H34 L44 98 H100 L108 66 H38" fill="none" {W(3.4)}/>'
    f'<path d="M38 66 H108 L102 90 H44Z" fill="#E8434A" opacity=".85" {W(3)}/>'
    + "".join(f'<path d="M{x} 66 L{x-2} 90" stroke="#fff" stroke-width="2"/>' for x in (54, 68, 82, 96)) +
    f'<circle cx="52" cy="108" r="7" fill="#4A4A5A" {W(2.6)}/><circle cx="94" cy="108" r="7" fill="#4A4A5A" {W(2.6)}/>'
    + stars(((24, 32), (102, 28), (110, 48)), 3.4))

# 4. Галеон — люлька-галеон с парусом и спящим малышом
I["chg-trc-galeon"] = ("#4A4F9A", "#1E2150",
    "деревянная детская люлька в форме старинного галеона с полосатым парусом",
    "в ней сладко спит малыш в чепчике, люлька тихо качается на ночных волнах под луной",
    f'<circle cx="96" cy="28" r="10" fill="#FFE9A8"/><circle cx="101" cy="25" r="9" fill="#33387A"/>'
    f'<path d="M0 100 Q20 92 40 100 T80 100 T128 100 V128 H0Z" fill="#2B6CB0" {W(2.4)}/>'
    f'<path d="M18 72 H110 Q104 98 84 100 H44 Q24 98 18 72Z" fill="#B5703A" {W(3.2)}/>'
    f'<path d="M24 82 H104" stroke="#8A4F24" stroke-width="2.4"/><circle cx="40" cy="90" r="2.6" fill="#FFE07A"/><circle cx="64" cy="91" r="2.6" fill="#FFE07A"/><circle cx="88" cy="90" r="2.6" fill="#FFE07A"/>'
    f'<path d="M64 72 V18" {W(3)}/><path d="M64 22 Q90 34 64 58Z" fill="#FFFFFF" {W(2.6)}/>'
    f'<path d="M66 32 Q78 36 70 42 M66 46 Q74 48 68 52" stroke="#E8434A" stroke-width="3" fill="none"/>'
    f'<circle cx="44" cy="66" r="10" fill="#FFD9B8" {W(2.4)}/>'
    f'<path d="M34 64 Q44 50 54 64" fill="#FFFFFF" {W(2.2)}/>'
    f'<path d="M39 68 q2 2 4 0 M46 68 q2 2 4 0" fill="none" {W(1.8)}/>'
    f'<path d="M30 72 Q44 62 60 72" fill="#9AD0FF" {W(2.2)}/>'
    f'<text x="22" y="52" font-family="Arial" font-weight="bold" font-size="11" fill="#FFF7C2">z</text><text x="14" y="42" font-family="Arial" font-weight="bold" font-size="8" fill="#FFF7C2">z</text>'
    + stars(((112, 54), (24, 22), (84, 12)), 2.8, "#FFF7C2"))

# 5. Европолис — пеленальный столик с малышом
I["chg-trk-evropolis"] = ("#FFE3D3", "#F49A7A",
    "белый пеленальный столик с бортиками, мягким матрасиком и полочкой внизу",
    "на нём лежит малыш и весело болтает ножками, а сверху на ниточке висит жёлтая звёздочка",
    f'<path d="M64 6 V24" {W(2)}/>' + sparkle(64, 30, 8, "#FFD23F") +
    f'<rect x="20" y="66" width="88" height="10" rx="4" fill="#FFFFFF" {W(3)}/>'
    f'<path d="M20 70 V52 M108 70 V52" {W(4)}/>'
    f'<rect x="24" y="58" width="80" height="9" rx="4" fill="#9FD8F0" {W(2.4)}/>'
    f'<path d="M26 76 V112 M102 76 V112" {W(4)}/><rect x="26" y="94" width="76" height="6" rx="2" fill="#FFFFFF" {W(2.4)}/>'
    f'<rect x="38" y="86" width="10" height="8" rx="2" fill="#FF8FB1" {W(1.8)}/><rect x="52" y="84" width="12" height="10" rx="2" fill="#FFFFFF" {W(1.8)}/>'
    f'<circle cx="46" cy="52" r="11" fill="#FFD9B8" {W(2.6)}/>' + eye(42, 51, 0.5) + eye(50, 51, 0.5) +
    f'<path d="M43 56 Q46 59 49 56" fill="none" {W(1.8)}/>'
    f'<path d="M57 50 Q70 44 80 52 Q80 60 68 60 H57Z" fill="#FFFFFF" {W(2.4)}/>'
    f'<path d="M80 50 L90 38 M78 54 L94 48" {W(5)}/><path d="M80 50 L90 38 M78 54 L94 48" stroke="#FFD9B8" stroke-width="2.6" stroke-linecap="round"/>'
    f'<path d="M86 30 q3 -2 4 2 M96 42 q3 -1 3 3" fill="none" {W(1.6)}/>')

# 6. ЦДМ — пеленашка в подарочной коробке
I["chg-cdm-lubyanka"] = ("#EFE3FF", "#A98BE6",
    "малыш-пеленашка, туго завёрнутый в синее одеяльце с белой лентой-бантом",
    "лежит в раскрытой подарочной коробке, а крышка с бантом съехала набок",
    f'<path d="M18 26 L56 16 L60 30 L22 40Z" fill="#FF6F91" {W(2.6)}/><path d="M38 20 L42 34" stroke="#FFE07A" stroke-width="4"/>'
    f'<path d="M34 18 q-6 -10 4 -8 q4 2 0 9 q8 -6 10 0 q0 5 -10 0" fill="#FFE07A" {W(2)}/>'
    f'<path d="M22 64 H106 V108 Q106 112 102 112 H26 Q22 112 22 108Z" fill="#FF6F91" {W(3)}/>'
    f'<rect x="58" y="64" width="12" height="48" fill="#FFE07A" {W(2)}/>'
    f'<ellipse cx="64" cy="58" rx="34" ry="20" fill="#3F6FD8" {W(3)}/>'
    f'<path d="M34 64 Q64 50 94 64" fill="none" stroke="#fff" stroke-width="4"/><path d="M34 64 Q64 50 94 64" fill="none" {W(1.2)}/>'
    f'<circle cx="64" cy="44" r="14" fill="#FFD9B8" {W(2.6)}/>'
    f'<path d="M50 40 Q64 22 78 40" fill="#3F6FD8" {W(2.6)}/>'
    + eye(59, 46, 0.55) + eye(69, 46, 0.55) +
    f'<path d="M61 51 Q64 54 67 51" fill="none" {W(1.8)}/>'
    + stars(((100, 30), (110, 50), (14, 60)), 3.4))

# 7. Станция Мытищи — пачка влажных салфеток на платформе
I["chg-mytishchi-station"] = ("#E0F7F4", "#4FBFB0",
    "мягкая пачка влажных салфеток с откидным клапаном и мордашкой",
    "стоит на краю железнодорожной платформы под станционным фонарём и машет вытянутой салфеткой, как флажком",
    f'<path d="M0 98 H128 V128 H0Z" fill="#9AA3B5" {W(2.4)}/><path d="M0 98 H128" stroke="#FFD23F" stroke-width="4"/>'
    f'<path d="M100 98 V30" {W(3.2)}/><path d="M92 30 H108 L104 20 H96Z" fill="#3B3355"/><circle cx="100" cy="34" r="5" fill="#FFF3B0" {W(2)}/>'
    f'<rect x="22" y="52" width="64" height="44" rx="14" fill="#7BD3EA" {W(3)}/>'
    f'<path d="M36 52 Q54 42 72 52 V60 Q54 54 36 60Z" fill="#2F9FC2" {W(2.4)}/>'
    f'<path d="M50 52 Q46 34 56 22 Q60 18 66 22 Q70 32 60 52" fill="#FFFFFF" {W(2.4)}/>'
    + face(54, 76, d=9, k=0.85) +
    f'<path d="M86 70 L94 62" {W(3)}/>'
    + stars(((18, 30), (36, 16), (116, 56)), 3.2))

# 8. Лианозовский парк — чепчик едет в вагончике детского паровозика
I["chg-park-lianozovsky"] = ("#FFE8F0", "#F27BA8",
    "вязаный белый детский чепчик с розовым помпоном и завязками",
    "катается в открытом вагончике детского паровозика по кругу в парке аттракционов",
    f'<path d="M0 104 H128 V128 H0Z" fill="#8DD18A" {W(2.4)}/><path d="M6 104 H122" {W(3)}/>'
    + "".join(f'<path d="M{x} 101 V107" {W(2.4)}/>' for x in range(12, 122, 14)) +
    f'<rect x="24" y="72" width="80" height="24" rx="6" fill="#FFD23F" {W(3)}/>'
    f'<path d="M30 80 H98" stroke="#E8434A" stroke-width="4"/>'
    f'<circle cx="40" cy="98" r="7" fill="#E8434A" {W(2.6)}/><circle cx="88" cy="98" r="7" fill="#E8434A" {W(2.6)}/>'
    f'<path d="M34 72 Q34 36 64 34 Q94 36 94 72Z" fill="#FFFFFF" {W(3)}/>'
    f'<path d="M40 70 Q40 46 64 44 Q88 46 88 70" fill="none" stroke="#F2C6D6" stroke-width="3"/>'
    f'<circle cx="64" cy="30" r="8" fill="#FF7FA8" {W(2.4)}/>'
    f'<path d="M36 72 Q30 84 36 90 M92 72 Q98 84 92 90" fill="none" stroke="#FF7FA8" stroke-width="3" stroke-linecap="round"/>'
    + face(64, 58, d=9, k=0.8) +
    stars(((16, 34), (112, 30), (110, 60)), 3.2))

# 9. Сокольники — конверт для новорождённого на скамейке под листопадом
I["chg-park-sokolniki"] = ("#FFE9CC", "#F0A04B",
    "голубой конверт для новорождённого с кружевной оборкой и большим бантом, из него выглядывает личико малыша",
    "лежит на деревянной парковой скамейке, а вокруг кружатся кленовые листья",
    f'<rect x="12" y="84" width="104" height="9" rx="3" fill="#B5703A" {W(2.6)}/>'
    f'<path d="M22 93 V114 M106 93 V114" {W(4)}/><rect x="14" y="68" width="100" height="8" rx="3" fill="#B5703A" {W(2.4)}/>'
    f'<path d="M30 84 Q24 60 44 44 Q64 34 84 44 Q104 60 98 84Z" fill="#8EC5FF" {W(3)}/>'
    f'<path d="M30 84 Q64 74 98 84" fill="none" stroke="#fff" stroke-width="3"/>'
    f'<circle cx="64" cy="56" r="13" fill="#FFD9B8" {W(2.6)}/>'
    f'<path d="M50 54 Q64 34 78 54" fill="#FFFFFF" {W(2.4)}/>'
    + eye(59, 58, 0.55) + eye(69, 58, 0.55) +
    f'<path d="M61 63 Q64 66 67 63" fill="none" {W(1.8)}/>'
    f'<path d="M64 72 q-14 -8 -12 4 q2 6 12 -4 q14 -8 12 4 q-2 6 -12 -4Z" fill="#FFFFFF" {W(2.2)}/>'
    f'<path d="M18 24 l4 6 l6 -2 l-2 6 l6 4 l-8 2 l0 6 l-6 -4 l-6 4 l0 -6 l-8 -2 l6 -4 l-2 -6 l6 2Z" fill="#E8434A" {W(1.8)}/>'
    f'<path d="M100 18 l3 5 l5 -2 l-2 5 l5 3 l-6 2 l0 5 l-5 -3 l-5 3 l0 -5 l-6 -2 l5 -3 l-2 -5 l5 2Z" fill="#FFB020" {W(1.8)}/>'
    f'<path d="M108 54 l2 4 l4 -1 l-1 4 l4 2 l-5 1 l0 4 l-4 -2 l-4 2 l0 -4 l-5 -1 l4 -2 l-1 -4 l4 1Z" fill="#E86A2E" {W(1.6)}/>')

# 10. ВДНХ — баночка присыпки и золотой колос
I["chg-vdnh-north"] = ("#FFF1D6", "#D9A441",
    "круглая баночка детской присыпки с дырчатой крышечкой и мордашкой",
    "подпрыгивает и выпускает из крышечки облачко со звёздочками, рядом качается золотой колос",
    f'<path d="M0 108 H128 V128 H0Z" fill="#E7B95A" {W(2.4)}/>'
    f'<path d="M100 108 V40" {W(3)}/>' + "".join(f'<ellipse cx="{100 + (5 if i % 2 else -5)}" cy="{44 + i*8}" rx="5" ry="8" fill="#F5C842" {W(1.8)} transform="rotate({20 if i % 2 else -20} {100 + (5 if i % 2 else -5)} {44 + i*8})"/>' for i in range(6)) +
    f'<rect x="34" y="52" width="46" height="52" rx="12" fill="#FFFFFF" {W(3)}/>'
    f'<rect x="36" y="42" width="42" height="12" rx="5" fill="#FF9EB5" {W(2.6)}/>'
    + "".join(f'<circle cx="{x}" cy="48" r="1.6" fill="{O}"/>' for x in (46, 54, 62, 70)) +
    f'<path d="M36 90 H78" stroke="#9FD8F0" stroke-width="5"/>'
    + face(57, 72, d=8, k=0.8) +
    f'<path d="M40 30 Q34 20 44 16 Q48 6 58 12 Q68 8 70 18 Q80 22 72 30Z" fill="#FFFFFF" {W(2.4)}/>'
    + stars(((52, 22), (62, 20), (18, 46), (22, 80)), 3.2, "#FFD23F"))

# 11. Воронцовский парк — упаковка подгузников на мостике над прудом
I["chg-park-vorontsovsky"] = ("#DDEBFF", "#6E8FD8",
    "мягкая упаковка подгузников в голубую полоску с ручкой-петлёй сверху",
    "стоит на горбатом деревянном мостике над прудом и разглядывает своё отражение в воде",
    f'<path d="M0 96 H128 V128 H0Z" fill="#4F9AD6" {W(2.4)}/>'
    f'<path d="M30 112 q8 -4 16 0 M70 118 q8 -4 16 0" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>'
    f'<path d="M4 96 Q64 60 124 96" fill="none" stroke="#9A5A2E" stroke-width="8"/><path d="M4 96 Q64 60 124 96" fill="none" {W(2)}/>'
    + "".join(f'<path d="M{x} {96 - (36 - abs(64 - x) * 36 / 60) * 0.95:.0f} V{102 - (36 - abs(64 - x) * 36 / 60) * 0.95 - 12:.0f}" {W(2.4)}/>' for x in (14, 30, 98, 114)) +
    f'<rect x="40" y="28" width="48" height="50" rx="10" fill="#FFFFFF" {W(3)}/>'
    + "".join(f'<path d="M42 {36 + i*10} H86" stroke="#8EC5FF" stroke-width="3"/>' for i in range(4)) +
    f'<path d="M54 28 Q54 16 64 16 Q74 16 74 28" fill="none" {W(3)}/>'
    + face(64, 52, d=9, k=0.85) +
    f'<rect x="44" y="102" width="40" height="14" rx="6" fill="#FFFFFF" opacity=".35"/>'
    + stars(((18, 24), (108, 20), (114, 52)), 3.2))

# 12. Митино — баночка детского крема в лодочке
I["chg-park-mitino"] = ("#E7FBEF", "#3FAF7A",
    "низкая баночка детского крема с открытой крышкой-шляпкой и кремом-сердечком",
    "плывёт в маленькой вёсельной лодочке по пруду и гребёт двумя вёслами",
    f'<path d="M0 94 Q32 88 64 94 T128 94 V128 H0Z" fill="#53A8D8" {W(2.4)}/>'
    f'<path d="M18 86 H110 Q102 108 82 108 H46 Q26 108 18 86Z" fill="#E86A2E" {W(3)}/>'
    f'<path d="M24 92 H104" stroke="#fff" stroke-width="3"/>'
    f'<path d="M14 70 L40 104 M114 70 L88 104" {W(3)}/><ellipse cx="38" cy="102" rx="4" ry="8" fill="#F2C14E" {W(2)} transform="rotate(-38 38 102)"/><ellipse cx="90" cy="102" rx="4" ry="8" fill="#F2C14E" {W(2)} transform="rotate(38 90 102)"/>'
    f'<rect x="38" y="56" width="52" height="32" rx="10" fill="#FFFFFF" {W(3)}/>'
    f'<path d="M40 70 H88" stroke="#FFB3C7" stroke-width="5"/>'
    + face(64, 76, d=9, k=0.75) +
    f'<ellipse cx="64" cy="54" rx="24" ry="5" fill="#FFF7EA" {W(2.4)}/>'
    f'<path d="M64 52 q-8 -10 -2 -12 q2 0 2 3 q0 -3 2 -3 q6 2 -2 12Z" fill="#FFFFFF" {W(2)}/>'
    f'<ellipse cx="82" cy="30" rx="18" ry="5" fill="#3FC0A0" {W(2.6)} transform="rotate(-18 82 30)"/>'
    + stars(((22, 28), (40, 14), (112, 52)), 3.2))

# 13. Парк Останкино — прорезыватель-кольцо катится по липовой аллее
I["chg-park-ostankino"] = ("#F4F0D8", "#B9B060",
    "деревянное кольцо-прорезыватель для зубок с силиконовыми бусинами и мордашкой",
    "катится колесом по аллее между двумя круглыми липами, оставляя пыльный след",
    f'<path d="M0 100 H128 V128 H0Z" fill="#D8C79A" {W(2.4)}/>'
    f'<rect x="14" y="58" width="7" height="44" fill="#8A5A34" {W(2.2)}/><circle cx="17" cy="46" r="17" fill="#7DB04A" {W(2.4)}/>'
    f'<rect x="107" y="58" width="7" height="44" fill="#8A5A34" {W(2.2)}/><circle cx="110" cy="46" r="17" fill="#7DB04A" {W(2.4)}/>'
    f'<circle cx="64" cy="70" r="28" fill="none" stroke="{O}" stroke-width="16"/><circle cx="64" cy="70" r="28" fill="none" stroke="#E6B97A" stroke-width="11"/>'
    + "".join(f'<circle cx="{64 + 28*c:.1f}" cy="{70 + 28*s_:.1f}" r="6" fill="{col}" {W(2)}/>' for c, s_, col in
              ((-0.7, -0.7, "#7FD0FF"), (0.7, -0.7, "#FF9EB5"), (1, 0, "#9BE36A"), (-1, 0, "#FFD23F"))) +
    face(64, 66, d=8, k=0.8) +
    f'<path d="M30 104 q-8 -2 -12 2 M36 110 q-8 0 -12 4" fill="none" stroke="#B49A6A" stroke-width="2.6" stroke-linecap="round"/>'
    + stars(((48, 22), (82, 18)), 3.2))

# 14. Коломенское — расписная зыбка на ветке дуба
I["chg-kolomenskoe-dyakovo"] = ("#FCE9D8", "#C77A4A",
    "расписная деревянная колыбель-зыбка с красными цветами на бортике",
    "подвешена на четырёх верёвках к толстой ветке старого дуба и плавно качается",
    f'<path d="M0 24 Q40 14 128 22 L128 34 Q60 28 0 36Z" fill="#7A4A2A" {W(2.6)}/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="10" ry="6" fill="#6FA845" {W(2)}/>' for x, y in ((20, 16), (52, 12), (90, 14), (116, 20))) +
    f'<path d="M64 30 L36 70 M64 30 L92 70 M64 30 L48 72 M64 30 L80 72" {W(2)}/>'
    f'<path d="M28 70 H100 Q98 100 64 102 Q30 100 28 70Z" fill="#F2C14E" {W(3)}/>'
    f'<path d="M30 78 H98" stroke="#B5703A" stroke-width="2"/>'
    + "".join(f'<circle cx="{x}" cy="88" r="5" fill="#E8434A" {W(1.6)}/><circle cx="{x}" cy="88" r="1.8" fill="#FFE07A"/>' for x in (44, 64, 84)) +
    f'<path d="M52 92 q4 -6 8 0 M72 92 q4 -6 8 0" fill="none" stroke="#3D8B3D" stroke-width="2"/>'
    f'<circle cx="64" cy="64" r="9" fill="#FFD9B8" {W(2.4)}/>'
    f'<path d="M60 64 q2 2 3 0 M65 64 q2 2 3 0" fill="none" {W(1.6)}/>'
    f'<path d="M50 72 Q64 60 78 72" fill="#FFFFFF" {W(2.2)}/>'
    f'<path d="M14 72 q-4 6 0 10 M114 72 q4 6 0 10" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'
    + stars(((16, 52), (112, 50)), 3))

# 15. Парк Горького — мамина сумка для прогулок на скамейке у площадки
I["chg-gorky-park-garage"] = ("#E9F0F7", "#8AA3BD",
    "большая мамина сумка для прогулок с карманами и мордашкой на клапане",
    "стоит на скамейке у детской площадки, а из карманов торчат свёрнутый подгузник, погремушка и бутылочка",
    f'<path d="M0 104 H128 V128 H0Z" fill="#7FBF6A" {W(2.4)}/>'
    f'<path d="M100 104 V60 M120 104 V60 M100 64 H120" {W(3)}/><path d="M104 64 L108 92 M116 64 L112 92" {W(1.8)}/><rect x="104" y="90" width="12" height="4" rx="1" fill="#FF6F91" {W(1.6)}/>'
    f'<rect x="8" y="94" width="88" height="8" rx="3" fill="#B5703A" {W(2.4)}/><path d="M16 102 V116 M88 102 V116" {W(3.4)}/>'
    f'<path d="M30 52 Q52 30 74 52" fill="none" {W(4)}/>'
    f'<rect x="20" y="50" width="64" height="44" rx="10" fill="#E86A8E" {W(3)}/>'
    f'<path d="M20 62 Q52 74 84 62 V58 Q52 68 20 58Z" fill="#C24E72" {W(2)}/>'
    f'<rect x="76" y="58" width="16" height="30" rx="5" fill="#C24E72" {W(2.4)}/>'
    f'<rect x="80" y="40" width="9" height="20" rx="3" fill="#FFFFFF" {W(2)}/><path d="M82 40 q2 -6 5 0" fill="#FFB3C7" {W(1.6)}/>'
    f'<path d="M30 52 L26 36 Q32 30 40 36 L42 52" fill="#FFFFFF" {W(2.2)}/>'
    f'<path d="M48 50 L52 32" {W(2.4)}/><circle cx="53" cy="28" r="6" fill="#FFD23F" {W(2)}/>'
    + face(48, 80, d=9, k=0.8) +
    stars(((14, 24), (64, 14), (112, 30)), 3))

# 16. Детский парк им. Прямикова — мягкая расчёска причёсывает одуванчик
I["chg-pryamikov-park"] = ("#FFF3E8", "#E8B98A",
    "мягкая детская щётка-расчёска с деревянной ручкой и белой пушистой щетинкой",
    "бережно причёсывает пушистую головку большого одуванчика на газоне детского парка",
    f'<path d="M0 104 Q64 96 128 104 V128 H0Z" fill="#7FBF6A" {W(2.4)}/>'
    f'<path d="M44 104 Q40 80 46 62" fill="none" stroke="#4E9A3C" stroke-width="4"/>'
    f'<path d="M36 96 q-8 -10 2 -12 q6 4 4 12" fill="#5FB04A" {W(1.8)}/>'
    f'<circle cx="46" cy="50" r="20" fill="#FFFFFF" {W(2.4)}/>'
    + "".join(f'<path d="M46 50 L{46 + 17*c:.1f} {50 + 17*s_:.1f}" stroke="#D9D2C6" stroke-width="1.4"/>' for c, s_ in
              ((1, 0), (0.7, 0.7), (0, 1), (-0.7, 0.7), (-1, 0), (-0.7, -0.7), (0, -1), (0.7, -0.7))) +
    f'<circle cx="46" cy="50" r="5" fill="#E8D9B0"/>'
    f'<rect x="64" y="22" width="40" height="18" rx="8" fill="#C98A52" {W(3)} transform="rotate(30 84 31)"/>'
    f'<path d="M68 34 L60 50 M74 38 L66 54 M80 41 L72 57 M86 45 L78 61 M92 48 L84 64" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" transform="translate(0 -2)"/>'
    f'<path d="M98 54 L118 96" {W(9)}/><path d="M98 54 L118 96" stroke="#C98A52" stroke-width="5" stroke-linecap="round"/>'
    + face(84, 30, d=7, k=0.6, mouth=False) +
    f'<path d="M80 36 Q84 39 88 36" fill="none" {W(1.6)} transform="rotate(30 84 31)"/>'
    f'<circle cx="22" cy="26" r="2" fill="#fff" {W(1)}/><circle cx="28" cy="18" r="1.6" fill="#fff" {W(1)}/>'
    + stars(((112, 20), (16, 70)), 3))

# 17. Юник — баночки пальчиковых красок и отпечатки ладошек
I["fun-yunik-gzhatskaya"] = ("#F3EAFD", "#D17FE0",
    "четыре баночки пальчиковых красок — красная, жёлтая, синяя и зелёная, средняя с мордашкой",
    "стоят у листа бумаги, на котором малыш оставил разноцветные отпечатки ладошек",
    f'<rect x="14" y="16" width="80" height="58" rx="4" fill="#FFFFFF" {W(2.6)} transform="rotate(-6 54 45)"/>'
    + "".join(f'<g transform="translate({x} {y}) rotate({r})"><ellipse cx="0" cy="0" rx="8" ry="9" fill="{c}"/>'
              + "".join(f'<ellipse cx="{dx}" cy="{dy}" rx="2.4" ry="5" fill="{c}" transform="rotate({rr} {dx} {dy})"/>' for dx, dy, rr in ((-8, -9, -25), (-3, -12, -8), (3, -12, 8), (8, -9, 25), (11, 1, 70)))
              + '</g>' for x, y, r, c in ((34, 42, -10, "#FF6F91"), (60, 36, 6, "#3FA9F5"), (80, 52, 18, "#FFC72C"))) +
    "".join(f'<rect x="{x}" y="84" width="22" height="26" rx="5" fill="#FFFFFF" {W(2.6)}/><rect x="{x-1}" y="78" width="24" height="9" rx="3" fill="{c}" {W(2.4)}/><rect x="{x+2}" y="92" width="18" height="15" rx="3" fill="{c}"/>'
            for x, c in ((14, "#E8434A"), (40, "#FFC72C"), (66, "#3F6FD8"), (92, "#4CB050"))) +
    face(51, 99, d=5, k=0.55, mouth=False))

# 18. Монтессори «Волшебная страна» — блок с цилиндрами-вкладышами
I["fun-montessori-volshebnaya-strana"] = ("#FDF2DC", "#E0B66C",
    "деревянный брусок Монтессори с пятью цилиндрами-вкладышами разной толщины на кнопочках-ручках",
    "самый толстый цилиндр с мордашкой выпрыгнул из своего гнезда и радостно подпрыгивает над бруском",
    f'<rect x="10" y="78" width="108" height="26" rx="5" fill="#D9A25E" {W(3)}/>'
    f'<path d="M12 84 H116" stroke="#E9BE80" stroke-width="2"/>'
    + "".join(f'<ellipse cx="{x}" cy="80" rx="{r}" ry="{r*0.35:.1f}" fill="#7A4A24" {W(1.8)}/>' for x, r in ((24, 5), (44, 7), (66, 9))) +
    "".join(f'<rect x="{x - r}" y="70" width="{2*r}" height="10" fill="#E9BE80" {W(2)}/><ellipse cx="{x}" cy="70" rx="{r}" ry="{r*0.35:.1f}" fill="#F2CE94" {W(1.8)}/><path d="M{x} 70 V62" {W(2.4)}/><circle cx="{x}" cy="60" r="3" fill="#B5703A" {W(1.6)}/>' for x, r in ((24, 5), (44, 7))) +
    f'<ellipse cx="94" cy="80" rx="13" ry="4.5" fill="#7A4A24" {W(1.8)}/>'
    f'<rect x="78" y="34" width="32" height="24" fill="#F2CE94" {W(2.6)}/><ellipse cx="94" cy="58" rx="16" ry="5.5" fill="#F2CE94" {W(2.6)}/>'
    f'<ellipse cx="94" cy="34" rx="16" ry="5.5" fill="#F7DDB0" {W(2.6)}/><path d="M94 34 V22" {W(3)}/><circle cx="94" cy="19" r="4.5" fill="#B5703A" {W(2)}/>'
    + face(94, 44, d=6, k=0.6) +
    f'<path d="M80 66 q-4 4 -8 2 M108 66 q4 4 8 2" fill="none" {W(2)}/>'
    + stars(((22, 30), (50, 20), (118, 46)), 3.2))

# 19. Кампус ЗИЛ — оранжевая рука-манипулятор ставит шестерёнку
I["fun-kampus-zil"] = ("#E3E8F0", "#55657F",
    "оранжевая учебная роботизированная рука-манипулятор с тремя суставами и клешнёй",
    "аккуратно ставит голубую шестерёнку на стопку деталей на верстаке",
    f'<rect x="0" y="100" width="128" height="28" fill="#8C6A4A" {W(2.4)}/>'
    f'<rect x="14" y="88" width="30" height="12" rx="3" fill="#3B3F4F" {W(2.4)}/>'
    f'<path d="M29 88 L36 56 L82 40" fill="none" stroke="{O}" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>'
    f'<path d="M29 88 L36 56 L82 40" fill="none" stroke="#FF8A2B" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/>'
    f'<circle cx="36" cy="56" r="7" fill="#FFD23F" {W(2.2)}/><circle cx="82" cy="40" r="6" fill="#FFD23F" {W(2.2)}/>'
    f'<path d="M82 40 L90 58" {W(5)}/><path d="M82 46 L90 58" stroke="#FF8A2B" stroke-width="2"/>'
    f'<path d="M84 58 L80 68 M96 58 L100 68 M84 58 H96" {W(3)}/>'
    + eye(32, 72, 0.45) + eye(40, 72, 0.45) +
    f'<g transform="translate(90 76)">' + "".join(f'<rect x="-3" y="-12" width="6" height="6" fill="#4FB3E8" {W(1.6)} transform="rotate({a})"/>' for a in range(0, 360, 45)) +
    f'<circle r="9" fill="#4FB3E8" {W(2.2)}/><circle r="3" fill="#E3E8F0" {W(1.6)}/></g>'
    f'<rect x="76" y="90" width="28" height="10" rx="2" fill="#9BE36A" {W(2)}/><rect x="80" y="86" width="20" height="5" rx="2" fill="#FF6F91" {W(1.8)}/>'
    + stars(((106, 22), (20, 30), (118, 50)), 3.2))

# 20. Ерошка — плюшевый гвардеец у красной телефонной будки
I["fun-eroshka-voronezhskaya"] = ("#FFE0E0", "#E04848",
    "плюшевый игрушечный британский гвардеец в высокой чёрной меховой шапке и красном мундире",
    "стоит у красной телефонной будки и машет рукой, а над ним облачко «Hello!»",
    f'<path d="M0 108 H128 V128 H0Z" fill="#9AA3B5" {W(2.4)}/>'
    f'<rect x="80" y="34" width="34" height="74" rx="4" fill="#D62828" {W(3)}/><path d="M80 34 Q97 24 114 34" fill="#D62828" {W(3)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="9" height="9" fill="#FFF3B0" {W(1.6)}/>' for x in (86, 98) for y in (46, 58, 70)) +
    f'<path d="M38 22 Q38 6 54 6 Q70 6 70 22 V44 H38Z" fill="#2B2B3A" {W(3)}/>'
    f'<circle cx="54" cy="52" r="13" fill="#FFD9B8" {W(2.6)}/>' + face(54, 52, d=5, k=0.55) +
    f'<path d="M40 44 Q40 56 46 62 M68 44 Q68 56 62 62" fill="none" stroke="#FFD23F" stroke-width="2"/>'
    f'<rect x="38" y="64" width="32" height="30" rx="8" fill="#E8434A" {W(3)}/><path d="M38 72 H70" stroke="#fff" stroke-width="2.4"/>'
    + "".join(f'<circle cx="54" cy="{y}" r="1.8" fill="#FFD23F"/>' for y in (78, 84, 90)) +
    f'<path d="M38 68 L26 52" {W(6)}/><path d="M38 68 L26 52" stroke="#E8434A" stroke-width="3" stroke-linecap="round"/><circle cx="25" cy="50" r="4" fill="#FFFFFF" {W(2)}/>'
    f'<rect x="42" y="94" width="10" height="14" fill="#2B2B3A" {W(2)}/><rect x="56" y="94" width="10" height="14" fill="#2B2B3A" {W(2)}/>'
    f'<rect x="8" y="78" width="30" height="15" rx="7" fill="#FFFFFF" {W(2)}/>'
    f'<text x="11" y="89" font-family="Arial" font-weight="bold" font-size="8.5" fill="{O}">Hello!</text>')

# 21. Домнеон — неоновые очки-звёзды на тёмном танцполе
I["fun-domneon-domodedovo"] = ("#3A1F5C", "#0E0820",
    "праздничные очки в виде двух звёзд с ярко-розовой светящейся неоновой оправой",
    "пляшут на тёмном танцполе из светящихся квадратов под разноцветными лучами прожекторов",
    f'<path d="M20 0 L54 100 L40 100Z" fill="#3FE0FF" opacity=".25"/><path d="M108 0 L74 100 L88 100Z" fill="#FFE03F" opacity=".25"/>'
    + "".join(f'<rect x="{x}" y="{y}" width="20" height="10" fill="{c}" opacity=".85" {W(1.4)}/>' for (x, y, c) in
              ((14, 102, "#FF4FD8"), (34, 102, "#3FE0FF"), (54, 102, "#9BFF4F"), (74, 102, "#FFE03F"), (94, 102, "#FF4FD8"),
               (4, 112, "#9BFF4F"), (24, 112, "#FFE03F"), (44, 112, "#FF4FD8"), (64, 112, "#3FE0FF"), (84, 112, "#9BFF4F"), (104, 112, "#3FE0FF"))) +
    "".join(f'<path d="M{cx} {cy-20} L{cx+6} {cy-7} L{cx+20} {cy-6} L{cx+9} {cy+3} L{cx+13} {cy+18} L{cx} {cy+10} L{cx-13} {cy+18} L{cx-9} {cy+3} L{cx-20} {cy-6} L{cx-6} {cy-7}Z" fill="#2A1640" stroke="#FF4FD8" stroke-width="5" stroke-linejoin="round"/>'
            f'<path d="M{cx} {cy-20} L{cx+6} {cy-7} L{cx+20} {cy-6} L{cx+9} {cy+3} L{cx+13} {cy+18} L{cx} {cy+10} L{cx-13} {cy+18} L{cx-9} {cy+3} L{cx-20} {cy-6} L{cx-6} {cy-7}Z" fill="none" stroke="#FFD1F5" stroke-width="1.6" stroke-linejoin="round"/>'
            for cx, cy in ((40, 60), (88, 60))) +
    f'<path d="M58 58 Q64 52 70 58" fill="none" stroke="#FF4FD8" stroke-width="5" stroke-linecap="round"/>'
    + eye(40, 60, 0.75) + eye(88, 60, 0.75) +
    f'<path d="M56 82 Q64 90 72 82" fill="none" stroke="#3FE0FF" stroke-width="4" stroke-linecap="round"/>'
    + stars(((18, 24), (110, 30), (64, 22)), 3.4, "#FFE03F"))

if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
