"""Иконки робота fun (2026-11-10, поздний проход z): места из tools/add_fun_1110z.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя палитра фона.
Запуск: python3 tools/icons_fun_1110z.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye, O
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}


def stars(pts, r=3, c="#fff"):
    return "".join(sparkle(x, y, r, c) for x, y in pts)


def kid(x, y, shirt, hair="#6B3E1F", k=1.0):
    """голова и туловище малыша (центр головы x, y)"""
    return (f'<path d="M{x-11*k} {y+30*k} Q{x-12*k} {y+12*k} {x} {y+11*k} Q{x+12*k} {y+12*k} {x+11*k} {y+30*k}Z" fill="{shirt}" {W(2.6)}/>'
            f'<circle cx="{x}" cy="{y}" r="{11*k}" fill="#FFD9B8" {W(2.6)}/>'
            f'<path d="M{x-11*k} {y-1*k} Q{x-9*k} {y-13*k} {x} {y-12*k} Q{x+10*k} {y-13*k} {x+11*k} {y-2*k} Q{x+4*k} {y-7*k} {x-11*k} {y-1*k}Z" fill="{hair}" {W(2.2)}/>'
            + face(x, y + 1 * k, d=4.5 * k, k=0.42 * k))


# 1. Ну, погоди-ка! (Зарайск): игровая с батутами и кафе
I["fun-nupogodika-zaraysk"] = ("#FFF3D6", "#F08A3C",
    "круглый батут с синей сеткой-ограждением на дугах",
    "внутри высоко подпрыгивает малыш в полосатой футболке и держит румяный пирожок",
    f'<ellipse cx="64" cy="104" rx="46" ry="12" fill="#2F6FD0" {W(3)}/>'
    f'<ellipse cx="64" cy="101" rx="38" ry="8" fill="#1E2F55"/>'
    + "".join(f'<path d="M{x} 104 V122" {W(3)}/>' for x in (26, 50, 78, 102)) +
    "".join(f'<path d="M{x} 102 Q{x+(64-x)*0.15} 50 {x+(64-x)*0.3} 40" fill="none" stroke="#2F6FD0" stroke-width="4"/>' for x in (20, 108)) +
    f'<path d="M20 102 Q22 56 38 40 H90 Q106 56 108 102" fill="#8FC8FF" fill-opacity=".25" stroke="#2F6FD0" stroke-width="2" stroke-dasharray="3 4"/>'
    + kid(64, 46, "#FFFFFF") +
    "".join(f'<path d="M54 {y} H74" stroke="#E8434A" stroke-width="2.6"/>' for x, y in ((0, 64), (0, 70))) +
    f'<path d="M53 76 L46 90 M75 76 L82 90" {W(4)}/>'
    f'<path d="M53 60 L40 50" {W(4)}/><ellipse cx="36" cy="46" rx="9" ry="6" fill="#E59A3A" {W(2.4)} transform="rotate(-25 36 46)"/>'
    f'<path d="M30 46 Q36 43 42 46" stroke="#B5651D" stroke-width="1.6" fill="none"/>'
    f'<path d="M75 60 L88 50" {W(4)}/>'
    f'<path d="M50 92 Q64 98 78 92" stroke="#fff" stroke-width="2.4" fill="none" opacity=".8"/>'
    + stars(((20, 26), (108, 24)), 4, "#FFF"))

# 2. Детский технопарк «Альтаир» РТУ МИРЭА
I["fun-altair-vernadskogo"] = ("#2B3E7A", "#0E1636",
    "кубсат — маленький кубический спутник с синими солнечными крыльями и мордашкой",
    "летит над голубой планетой к яркой белой звезде Альтаир",
    f'<circle cx="18" cy="128" r="46" fill="#3FA8E8" {W(3)}/>'
    f'<path d="M-6 104 Q14 96 30 108 Q40 118 54 112" fill="none" stroke="#4CC27A" stroke-width="6"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1.6" fill="#fff"/>' for x, y in ((30, 24), (54, 16), (88, 96), (110, 80), (20, 60), (76, 22)))
    + sparkle(104, 26, 13, "#FFFFFF") + f'<circle cx="104" cy="26" r="4" fill="#BFE6FF"/>'
    f'<g transform="rotate(-18 62 70)">'
    f'<rect x="10" y="62" width="30" height="18" fill="#2A5BD7" {W(2.6)}/><path d="M20 62 V80 M30 62 V80 M10 71 H40" stroke="#9FC2FF" stroke-width="1.6"/>'
    f'<rect x="84" y="62" width="30" height="18" fill="#2A5BD7" {W(2.6)}/><path d="M94 62 V80 M104 62 V80 M84 71 H114" stroke="#9FC2FF" stroke-width="1.6"/>'
    f'<path d="M40 71 H46 M78 71 H84" {W(3)}/>'
    f'<rect x="46" y="54" width="32" height="34" rx="3" fill="#C9D2DE" {W(3)}/>'
    f'<rect x="50" y="58" width="24" height="26" rx="2" fill="#E9EEF5"/>'
    + face(62, 70, d=6, k=0.6) +
    f'<path d="M62 54 V44" {W(2.4)}/><circle cx="62" cy="42" r="3" fill="#E8434A" {W(1.8)}/></g>')

# 3. Лига роботов (Чертаново)
I["fun-liga-robotov-yuzhnaya"] = ("#E9FFF2", "#3BAF6E",
    "гусеничный робот-тележка из деталей конструктора с антенной",
    "въезжает на пьедестал и поднимает манипулятором золотой кубок лиги",
    f'<rect x="8" y="106" width="112" height="22" fill="#2D7A4E" {W(3)}/>'
    f'<rect x="20" y="88" width="72" height="20" rx="10" fill="#3A3A48" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="98" r="5" fill="#8A8FA0" {W(2)}/>' for x in (32, 48, 64, 80)) +
    f'<rect x="26" y="52" width="60" height="38" rx="4" fill="#F6C624" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="#B88A00"/>' for x, y in ((32, 58), (80, 58), (32, 84), (80, 84))) +
    f'<rect x="36" y="60" width="40" height="22" rx="3" fill="#1E2A3A" {W(2.4)}/>'
    + eye(48, 70, 0.6).replace(f'fill="{O}"', 'fill="#5CF2FF"') + eye(64, 70, 0.6).replace(f'fill="{O}"', 'fill="#5CF2FF"') +
    f'<path d="M50 77 Q56 80 62 77" stroke="#5CF2FF" stroke-width="2" fill="none"/>'
    f'<path d="M44 52 V40" {W(2.4)}/><circle cx="44" cy="38" r="3" fill="#E8434A" {W(1.8)}/>'
    f'<path d="M86 64 L96 54 L98 44" fill="none" stroke="#E8434A" stroke-width="6"/><path d="M86 64 L96 54 L98 44" fill="none" {W(1.6)}/>'
    f'<path d="M92 42 L94 38 M104 42 L102 38" {W(3)}/>'
    f'<path d="M86 20 H110 V26 Q110 40 98 40 Q86 40 86 26Z" fill="#FFD23F" {W(2.6)}/>'
    f'<path d="M86 24 Q78 24 80 32 Q82 36 87 34 M110 24 Q118 24 116 32 Q114 36 109 34" fill="none" {W(2)}/>'
    + stars(((78, 16), (118, 18)), 3.5, "#FFF7A8"))

# 4. Клуб «Первое хобби» (Ясенево): вязание, шитьё, мягкая игрушка
I["fun-pervoe-hobbi-yasenevo"] = ("#FFF0F5", "#E77FA6",
    "белая швейная машинка с мордашкой на корпусе",
    "строчит крошечное голубое платьице, из-под лапки бежит пунктир стежков",
    f'<rect x="10" y="98" width="108" height="14" rx="3" fill="#B97A4A" {W(3)}/>'
    f'<path d="M22 98 V54 Q22 40 36 40 H96 Q108 40 108 52 V66 H90 V58 H44 V98Z" fill="#FFFFFF" {W(3.2)}/>'
    f'<rect x="90" y="58" width="12" height="8" fill="#FFFFFF"/>'
    f'<path d="M84 66 V84" {W(3)}/><path d="M78 84 H92" {W(3)}/>'
    f'<circle cx="104" cy="50" r="8" fill="#E77FA6" {W(2.4)}/>'
    + face(42, 56, d=7, k=0.6) +
    f'<path d="M60 86 L66 76 H82 L88 86 L94 96 H54Z" fill="#7FC8F2" {W(2.6)}/>'
    f'<path d="M66 76 Q74 82 82 76" fill="none" {W(2)}/>'
    f'<path d="M86 92 H120" stroke="#E8434A" stroke-width="2.4" stroke-dasharray="4 3"/>'
    f'<path d="M50 26 Q60 16 72 24" stroke="#E8434A" stroke-width="2.4" fill="none"/><circle cx="72" cy="24" r="4" fill="#E8434A" {W(1.6)}/>'
    + stars(((24, 26), (110, 22)), 3.5, "#FFFFFF"))

# 5. Клуб юных инженеров «Тесла»
I["fun-tesla-beskudnikovsky"] = ("#F2EAFF", "#7B4FD0",
    "катушка Теслы с серебряным шаром-головой и мордашкой",
    "от шара к лампочке на подставке проскакивает фиолетовая молния, и лампочка загорается",
    f'<rect x="20" y="104" width="44" height="12" rx="3" fill="#5A3A1E" {W(3)}/>'
    f'<rect x="32" y="56" width="20" height="48" fill="#C8783A" {W(3)}/>'
    + "".join(f'<path d="M32 {y} H52" stroke="#8A4A1A" stroke-width="1.6"/>' for y in range(60, 104, 5)) +
    f'<ellipse cx="42" cy="54" rx="10" ry="4" fill="#9AA3B2" {W(2.4)}/>'
    f'<circle cx="42" cy="34" r="20" fill="#DDE3EC" {W(3.2)}/>'
    f'<ellipse cx="34" cy="26" rx="6" ry="4" fill="#fff" opacity=".8"/>'
    + face(42, 36, d=7, k=0.62) +
    f'<path d="M62 34 L72 42 L68 46 L80 56 L76 60 L90 72" fill="none" stroke="#C04BFF" stroke-width="4"/>'
    f'<path d="M62 34 L72 42 L68 46 L80 56 L76 60 L90 72" fill="none" stroke="#fff" stroke-width="1.6"/>'
    f'<circle cx="96" cy="78" r="15" fill="#FFF07A" {W(3)}/>'
    f'<path d="M90 80 Q96 72 102 80" stroke="#E0A400" stroke-width="2" fill="none"/>'
    f'<rect x="89" y="92" width="14" height="10" fill="#9AA3B2" {W(2.4)}/>'
    f'<rect x="80" y="104" width="32" height="10" rx="3" fill="#5A3A1E" {W(2.6)}/>'
    + "".join(f'<path d="M{96+22*dx} {78+22*dy} L{96+30*dx} {78+30*dy}" stroke="#FFE14A" stroke-width="3" stroke-linecap="round"/>'
              for dx, dy in ((0, -1), (0.7, -0.7), (1, 0), (-0.7, -0.7))))

# 6. Мастерская «Лепка из глины и гончарное мастерство» (Шипиловская)
I["fun-lepka-shipilovskaya"] = ("#EAF7F6", "#4C9FA0",
    "голубой гончарный круг с мордашкой на станине",
    "крутится, а на нём из рыжей глины вырастает пузатый горшочек и летят капли глиняной воды",
    f'<path d="M30 118 L40 82 H88 L98 118Z" fill="#7FB8E6" {W(3.2)}/>'
    + face(64, 98, d=9, k=0.75) +
    f'<ellipse cx="64" cy="80" rx="40" ry="10" fill="#B9C2CE" {W(3)}/>'
    f'<ellipse cx="64" cy="78" rx="34" ry="7" fill="#DDE3EC"/>'
    f'<path d="M48 76 Q40 56 50 44 Q54 38 56 30 H72 Q74 38 78 44 Q88 56 80 76Z" fill="#D9793A" {W(3)}/>'
    f'<ellipse cx="64" cy="30" rx="8" ry="3" fill="#A65424" {W(2)}/>'
    f'<path d="M52 58 Q64 62 76 58" stroke="#F2A86A" stroke-width="2.4" fill="none"/>'
    f'<path d="M14 72 Q18 64 24 70 M104 70 Q110 64 114 72" stroke="{O}" stroke-width="2" fill="none"/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="2.6" ry="3.4" fill="#D9793A" {W(1.2)}/>' for x, y in ((24, 52), (104, 50), (32, 38), (98, 34))))

# 7. Квесты «Квест Хантер» (Электрозаводская)
I["fun-quest-hunter-semenovskaya"] = ("#FFF8E6", "#C79A3C",
    "огромный отпечаток пальца с мордашкой",
    "под лупой юного сыщика улыбается сквозь стекло, рядом лежит улика — ключ",
    f'<circle cx="54" cy="58" r="40" fill="#E8F4FF" fill-opacity=".85" {W(4)}/>'
    + "".join(f'<ellipse cx="54" cy="60" rx="{r}" ry="{r*1.25}" fill="none" stroke="#6B4A8C" stroke-width="2.6"/>' for r in (8, 14, 20, 26))
    + f'<rect x="44" y="48" width="20" height="18" rx="6" fill="#E8F4FF" fill-opacity=".9"/>'
    + face(54, 56, d=5, k=0.55) +
    f'<path d="M84 88 L112 116" stroke="#5A3A1E" stroke-width="10" stroke-linecap="round"/>'
    f'<path d="M84 88 L112 116" {W(2)}/>'
    f'<circle cx="54" cy="58" r="40" fill="none" stroke="#C79A3C" stroke-width="5"/>'
    f'<ellipse cx="38" cy="38" rx="10" ry="5" fill="#fff" opacity=".7" transform="rotate(-30 38 38)"/>'
    f'<circle cx="22" cy="110" r="6" fill="none" stroke="#FFC530" stroke-width="3"/>'
    f'<path d="M28 110 H48 M42 110 V116 M46 110 V114" stroke="#FFC530" stroke-width="3"/>'
    f'<path d="M28 110 H48" {W(1)}/>')

# 8. Актёрская школа Art Kids Community (Шелепиха)
I["fun-artkids-shelepiha"] = ("#FFF4E8", "#D0573F",
    "складной режиссёрский стул с красной парусиновой спинкой и мордашкой",
    "стоит в круге света на сцене, а на сиденье ждёт маленькая золотая звёздочка-роль",
    f'<path d="M40 0 L10 128 H118 L88 0Z" fill="#FFF6C8" opacity=".55"/>'
    f'<ellipse cx="64" cy="114" rx="46" ry="9" fill="#FFE9A0" opacity=".9"/>'
    f'<path d="M34 112 L94 70 M94 112 L34 70" stroke="#8B5A2B" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M34 112 L94 70 M94 112 L34 70" {W(1.6)}/>'
    f'<rect x="28" y="64" width="72" height="9" rx="2" fill="#D93A3A" {W(2.6)}/>'
    f'<path d="M34 64 V20 M94 64 V20" stroke="#8B5A2B" stroke-width="6" stroke-linecap="round"/>'
    f'<rect x="30" y="22" width="68" height="28" rx="2" fill="#D93A3A" {W(3)}/>'
    + face(64, 34, d=9, k=0.65) +
    sparkle(64, 56, 9, "#FFC21A") + f'<circle cx="61" cy="56" r="1.2" fill="{O}"/><circle cx="67" cy="56" r="1.2" fill="{O}"/>')

# 9. Театральная студия «Отражение» (Пражская)
I["fun-otrazhenie-kirovogradskaya"] = ("#EEF0FF", "#5E5BB8",
    "мальчик в бумажной короне и пижаме перед ростовым зеркалом в деревянной раме",
    "в зеркале он уже настоящий король в алой мантии и машет сам себе рукой",
    f'<rect x="58" y="10" width="56" height="108" rx="6" fill="#A0703F" {W(3.2)}/>'
    f'<rect x="65" y="17" width="42" height="94" rx="3" fill="#CFE7FF" {W(2)}/>'
    f'<path d="M70 104 Q86 64 102 104Z" fill="#C0283A" {W(2.4)}/>'
    f'<path d="M70 104 Q86 98 102 104" stroke="#fff" stroke-width="3" fill="none"/>'
    f'<circle cx="86" cy="58" r="10" fill="#FFD9B8" {W(2.4)}/>' + face(86, 59, d=4, k=0.38) +
    f'<path d="M76 48 L78 38 L82 44 L86 36 L90 44 L94 38 L96 48Z" fill="#FFC21A" {W(2)}/>'
    f'<path d="M98 74 L104 62" {W(3)}/>'
    f'<path d="M72 30 L82 22" stroke="#fff" stroke-width="3" opacity=".7"/>'
    f'<path d="M24 120 Q22 92 38 88 Q54 92 52 120Z" fill="#7FB8E6" {W(2.6)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="#fff"/>' for x, y in ((32, 100), (44, 106), (36, 114)))
    + f'<circle cx="38" cy="72" r="13" fill="#FFD9B8" {W(2.6)}/>' + face(38, 73, d=5, k=0.45) +
    f'<path d="M26 62 L28 50 L33 57 L38 48 L43 57 L48 50 L50 62Z" fill="#FFF2B0" {W(2.2)}/>'
    f'<path d="M52 98 L60 86" {W(3)}/>')

# 10. Студия творчества «Крылатая долина» (Лобачевского): театр по воскресеньям
I["fun-krylataya-dolina-lobachevskogo"] = ("#E8FFF0", "#5CBF7A",
    "кукольная ширма-домик в синюю полоску с белыми крыльями по бокам",
    "летит над зелёной долиной, а из окошка машет кукла-ворона в соломенной шляпке",
    f'<path d="M-4 112 Q30 92 64 108 Q96 120 132 100 V132 H-4Z" fill="#4CB07A" {W(3)}/>'
    f'<path d="M-4 120 Q40 106 72 118 Q100 126 132 114 V132 H-4Z" fill="#2E8A55"/>'
    f'<path d="M36 50 Q8 30 4 52 Q14 50 10 62 Q22 58 22 70 Q32 62 36 70Z" fill="#FFFFFF" {W(2.6)}/>'
    f'<path d="M92 50 Q120 30 124 52 Q114 50 118 62 Q106 58 106 70 Q96 62 92 70Z" fill="#FFFFFF" {W(2.6)}/>'
    f'<path d="M34 36 L64 18 L94 36Z" fill="#E8434A" {W(3)}/>'
    f'<rect x="36" y="36" width="56" height="52" fill="#FFFFFF" {W(3)}/>'
    + "".join(f'<rect x="{x}" y="36" width="7" height="52" fill="#4E7FD8"/>' for x in (36, 50, 64, 78)) +
    f'<rect x="36" y="36" width="56" height="52" fill="none" {W(3)}/>'
    f'<rect x="46" y="44" width="36" height="22" rx="2" fill="#2B2B3A" {W(2.4)}/>'
    f'<ellipse cx="64" cy="66" rx="10" ry="9" fill="#3A3A48" {W(2)}/>'
    f'<path d="M64 62 L74 66 L64 68Z" fill="#FFB020" {W(1.4)}/>'
    + eye(60, 60, 0.45).replace(f'fill="{O}"', 'fill="#fff"') +
    f'<ellipse cx="62" cy="52" rx="10" ry="3" fill="#F2D27A" {W(1.6)}/><path d="M57 52 Q62 44 67 52" fill="#F2D27A" {W(1.6)}/>'
    f'<path d="M74 62 Q80 54 78 48" {W(2.4)}/>'
    + face(64, 77, d=7, k=0.5))

# 11. Творческий центр «Джельсомино» (Шелепиха)
I["fun-dzhelsomino-shelepiha"] = ("#FFFBEA", "#F2B83A",
    "фиолетовый клей-карандаш с мордашкой и открытым колпачком",
    "приклеивает к листу последнюю цветную полоску бумажной радуги",
    f'<rect x="8" y="58" width="96" height="66" rx="3" fill="#FFFFFF" {W(3)}/>'
    + "".join(f'<path d="M{20+i*7} 118 Q{20+i*7} {74+i*7} 56 {74+i*7} Q{92-i*7} {74+i*7} {92-i*7} 118" fill="none" stroke="{c}" stroke-width="6"/>'
              for i, c in enumerate(("#E8434A", "#F59A23", "#FFD23F", "#4CB07A", "#3F7FD8")) if i < 4)
    + f'<path d="M48 118 Q48 108 56 108 Q64 108 64 118" fill="none" stroke="#8A5CD8" stroke-width="6" stroke-dasharray="3 0"/>'
    f'<g transform="rotate(28 92 56)">'
    f'<rect x="80" y="18" width="26" height="58" rx="5" fill="#8A5CD8" {W(3)}/>'
    f'<rect x="80" y="58" width="26" height="18" rx="3" fill="#FFFFFF" {W(2.6)}/>'
    f'<rect x="84" y="76" width="18" height="8" fill="#F2F0FF" {W(2.2)}/></g>'
    + face(88, 44, d=6, k=0.6) +
    f'<g transform="rotate(-20 112 20)"><rect x="100" y="8" width="24" height="18" rx="4" fill="#8A5CD8" {W(2.6)}/></g>'
    + stars(((22, 30), (50, 18)), 4, "#FFFFFF"))


if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
