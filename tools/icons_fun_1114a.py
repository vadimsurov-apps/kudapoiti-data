"""Иконки робота fun (2026-11-14, проход 1114a): места из tools/add_fun_1114a.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя компоновка и палитра фона.
Запуск: python3 tools/icons_fun_1114a.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
O = "#3B3355"
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}
BL = lambda x, y, k=1: f'<ellipse cx="{x}" cy="{y}" rx="{4*k}" ry="{2.4*k}" fill="#FF7FA8" opacity=".6"/>'
SM = lambda x, y, w=4: f'<path d="M{x-w} {y} Q{x} {y+w} {x+w} {y}" fill="none" stroke="{O}" stroke-width="2.2" stroke-linecap="round"/>'

# 1. Аннинский лесопарк — тихий лес: сосновая шишка-путешественница с рюкзачком шагает по тропинке
I["fun-annino-lesopark"] = ("#E4F2DC", "#6FAF6A",
    "сосновая шишка-путешественница с маленьким красным рюкзачком и посохом",
    "шагает по извилистой песочной тропинке между двумя тонкими стволами сосен",
    '<path d="M40 132 Q56 104 70 96 Q86 88 80 70" fill="none" stroke="#E8D29A" stroke-width="16" stroke-linecap="round"/>'
    f'<rect x="10" y="4" width="10" height="110" fill="#B5683F" {W(2.4)}/><rect x="104" y="0" width="9" height="104" fill="#B5683F" {W(2.4)}/>'
    f'<path d="M0 26 L15 6 L30 26Z M-4 46 L15 20 L34 46Z" fill="#2F7D4A" {W(2.4)}/><path d="M94 22 L108 2 L122 22Z M90 42 L108 16 L126 42Z" fill="#2F7D4A" {W(2.4)}/>'
    # шишка-тело
    f'<ellipse cx="62" cy="72" rx="20" ry="28" fill="#A86B3A" {W(3)}/>'
    + "".join(f'<path d="M{48+dx} {54+dy} q6 6 12 0" fill="none" stroke="#7A4A26" stroke-width="2.2"/>' for dx, dy in ((0,0),(14,0),(6,12),(-4,24),(10,24),(4,36)))
    + f'<rect x="76" y="58" width="14" height="22" rx="4" fill="#E8483A" {W(2.4)}/>'
    + face(60, 70, d=7, k=.75)
    + f'<path d="M50 98 L46 112 M70 98 L76 110" stroke="{O}" stroke-width="3" stroke-linecap="round"/>'
    + f'<path d="M38 66 L30 112" stroke="#6E4A2E" stroke-width="3.4" stroke-linecap="round"/><path d="M42 72 L38 70" stroke="{O}" stroke-width="3" stroke-linecap="round"/>')

# 2. Аршиновский парк — детская площадка: горка-жираф, по шее которой съезжает малыш
I["fun-arshinovsky-park"] = ("#FFF4D6", "#F2B33D",
    "горка в виде пятнистого жирафа с длинной шеей-скатом",
    "малыш в синей шапочке съезжает с макушки по шее вниз, раскинув руки, на солнечном жёлтом фоне",
    f'<rect x="-4" y="108" width="136" height="24" fill="#7FC66A"/>'
    f'<path d="M26 108 L26 80 L46 80 L46 108" fill="#F6C24A" {W(3)}/>'
    f'<path d="M30 80 Q36 50 60 34 Q72 26 80 28 L84 36 Q76 40 70 46 Q54 62 52 80Z" fill="#F6C24A" {W(3)}/>'
    f'<path d="M52 80 Q62 96 104 106 L106 112 Q60 104 46 84Z" fill="#F6C24A" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3.4" fill="#B5683F"/>' for x, y in ((34,92),(40,100),(42,70),(54,52),(64,42),(70,92),(86,100)))
    + f'<ellipse cx="82" cy="30" rx="12" ry="9" fill="#F6C24A" {W(3)}/><path d="M78 20 L76 12 M86 20 L88 12" stroke="{O}" stroke-width="3" stroke-linecap="round"/>'
    + '<circle cx="76" cy="12" r="3" fill="#B5683F"/><circle cx="88" cy="12" r="3" fill="#B5683F"/>'
    + eye(84, 28, .7) + f'<path d="M90 34 q3 2 4 -1" fill="none" stroke="{O}" stroke-width="2"/>'
    # малыш
    + f'<circle cx="64" cy="58" r="9" fill="#FFD9B8" {W(2.4)}/><path d="M55 56 Q64 44 73 56Z" fill="#3E7BE0" {W(2)}/>'
    + eye(61, 60, .45) + eye(67, 60, .45) + SM(64, 63, 3)
    + f'<path d="M56 66 L46 60 M72 66 L82 58" stroke="#3E7BE0" stroke-width="4" stroke-linecap="round"/>'
    + sparkle(108, 22, 6, "#fff"))

# 3. Дюссельдорфский парк — BMX-велодром: велосипед-BMX сам в прыжке над земляным бугром
I["fun-dusseldorf-park"] = ("#DFF1FF", "#4C9BE0",
    "оранжевый BMX-велосипед с глазками на руле и высунутым языком",
    "взлетел над коричневым земляным бугром-трамплином BMX-трассы, за колёсами пыльный след",
    f'<path d="M-4 120 Q30 86 64 120 Q96 92 132 120 L132 132 L-4 132Z" fill="#B07A4A" {W(3)}/>'
    f'<g transform="rotate(-14 64 60)">'
    f'<circle cx="38" cy="70" r="16" fill="none" {W(4)}/><circle cx="90" cy="70" r="16" fill="none" {W(4)}/>'
    f'<circle cx="38" cy="70" r="3" fill="{O}"/><circle cx="90" cy="70" r="3" fill="{O}"/>'
    f'<path d="M38 70 L58 70 L82 46 L52 46 Z M58 70 L50 46 M82 46 L90 70" fill="none" stroke="#F5822A" stroke-width="5" stroke-linejoin="round"/>'
    f'<path d="M48 42 L58 42" stroke="{O}" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M82 46 L84 32 M76 30 L94 30" stroke="{O}" stroke-width="4" stroke-linecap="round"/>'
    + eye(80, 22, .7) + eye(90, 22, .7) + f'<path d="M84 34 q3 6 6 0" fill="#FF6F8A" {W(1.6)}/>'
    + '</g>'
    + f'<path d="M12 100 q8 -6 14 0 M4 90 q8 -6 14 0" fill="none" stroke="#E8D2B0" stroke-width="4" stroke-linecap="round"/>'
    + sparkle(110, 18, 5, "#fff"))

# 4. Ивановский лесопарк — три детские площадки в лесу: жёлудь в шапочке катается на качелях, подвешенных к дубовой ветке
I["fun-ivanovsky-lesopark"] = ("#F3EBDA", "#C69A5A",
    "пузатый жёлудь в зелёной шапочке-плюске с хвостиком",
    "качается на верёвочных качелях-дощечке, подвешенных к толстой дубовой ветке, и болтает ножками",
    f'<path d="M-4 22 Q40 14 80 22 Q110 26 132 18 L132 32 Q100 36 80 34 Q40 28 -4 36Z" fill="#7A5236" {W(3)}/>'
    + "".join(f'<path d="M{x} {y} q-8 -10 0 -16 q8 6 0 16Z" fill="#5DAA48" {W(2)}/>' for x, y in ((20, 22), (100, 22), (116, 18)))
    + f'<path d="M42 34 L44 96 M84 34 L82 96" stroke="#5B3A22" stroke-width="2.6"/>'
    + f'<rect x="34" y="94" width="58" height="8" rx="3" fill="#C88A55" {W(2.6)}/>'
    + f'<ellipse cx="63" cy="74" rx="17" ry="21" fill="#D29A4E" {W(3)}/>'
    + f'<path d="M44 66 Q46 46 63 44 Q80 46 82 66 Q63 72 44 66Z" fill="#6E9A3A" {W(3)}/>'
    + "".join(f'<path d="M{x} 54 l3 4 l3 -4" fill="none" stroke="#4E7426" stroke-width="2"/>' for x in (52, 60, 68))
    + f'<path d="M63 44 L64 36" stroke="{O}" stroke-width="3" stroke-linecap="round"/>'
    + face(63, 78, d=7, k=.75)
    + f'<path d="M56 96 L52 110 M70 96 L76 108" stroke="{O}" stroke-width="3" stroke-linecap="round"/>')

# 5. Парк «Отрада» — родник и дерево желаний: дерево с разноцветными ленточками-желаниями
I["fun-park-otrada"] = ("#F7E8F2", "#C77BB5",
    "низенькое кудрявое дерево желаний с улыбкой, увешанное разноцветными ленточками",
    "у его корней из камней бьёт родничок голубой струйкой, на сиреневом фоне",
    f'<path d="M54 120 Q58 96 56 80 L72 80 Q70 96 76 120Z" fill="#8A5A3A" {W(3)}/>'
    f'<path d="M22 70 Q14 44 36 36 Q42 14 66 18 Q90 12 98 36 Q118 44 108 70 Q96 86 66 82 Q34 88 22 70Z" fill="#69B85A" {W(3)}/>'
    + "".join(f'<path d="M{x} {y} q3 10 -2 16" fill="none" stroke="{c}" stroke-width="4" stroke-linecap="round"/>'
              for x, y, c in ((34, 64, "#FF5A6E"), (48, 76, "#FFD23F"), (82, 76, "#3E7BE0"), (98, 62, "#FF8A2A"), (64, 80, "#B05AE0")))
    + face(64, 52, d=9, k=.85)
    + f'<path d="M78 120 Q86 110 96 112 Q106 110 110 120Z" fill="#9AA3B0" {W(2.6)}/>'
    + f'<path d="M94 112 Q96 96 104 92 M98 112 Q104 98 112 98" fill="none" stroke="#6CC8F0" stroke-width="3.4" stroke-linecap="round"/>'
    + '<circle cx="104" cy="90" r="2.5" fill="#BFEAFF"/><circle cx="113" cy="96" r="2" fill="#BFEAFF"/>')

# 6. Парк «Пальмира» (Куркино) — шутка по названию: пальма в шапке-ушанке и шарфе среди подмосковного снега
I["fun-park-palmira"] = ("#EAF4FB", "#8FB8D8",
    "пальма-модница в шапке-ушанке и полосатом шарфе",
    "стоит в сугробе посреди куркинского парка, а сверху падают снежинки",
    f'<path d="M-4 108 Q40 98 64 104 Q96 98 132 106 L132 132 L-4 132Z" fill="#FFFFFF" {W(3)}/>'
    f'<path d="M56 106 Q54 80 60 58 L70 58 Q66 82 70 106Z" fill="#C8955A" {W(3)}/>'
    + "".join(f'<path d="M57 {y} h12" stroke="#9A6A3A" stroke-width="2"/>' for y in (70, 80, 90, 100))
    + f'<path d="M64 52 Q40 40 18 56 Q40 46 62 58Z M64 52 Q86 38 110 54 Q88 46 66 58Z M64 50 Q50 28 30 26 Q50 36 62 54Z M64 50 Q78 26 100 24 Q80 36 66 54Z" fill="#3FA65A" {W(2.4)}/>'
    + f'<path d="M48 40 Q64 22 80 40Z" fill="#8A5A3A" {W(2.6)}/><path d="M48 40 L44 54 L52 52 Z M80 40 L84 54 L76 52Z" fill="#8A5A3A" {W(2)}/>'
    + eye(59, 50, .6) + eye(69, 50, .6) + SM(64, 55, 3)
    + f'<path d="M56 62 Q64 68 72 62 L72 68 Q64 74 56 68Z" fill="#E8483A" {W(2)}/><path d="M70 66 L76 82" stroke="#E8483A" stroke-width="5"/>'
    + "".join(sparkle(x, y, 4, "#fff") for x, y in ((24, 20), (104, 14), (112, 80), (16, 84))))

# 7. Парк имени Герцена (Загорье) — усадьба Загорье в парке: беседка-ротонда с колоннами, на куполе сидит голубь
I["fun-park-gertsena-zagorye"] = ("#FFF0E0", "#E39A6A",
    "белая усадебная беседка-ротонда с колоннами и улыбкой на фронтоне",
    "на её зелёном куполе устроился сизый голубь, вокруг липы старого парка на персиковом фоне",
    f'<path d="M-4 110 Q60 100 132 110 L132 132 L-4 132Z" fill="#8CCB6A"/>'
    f'<ellipse cx="18" cy="74" rx="16" ry="30" fill="#5FA04A" {W(2.6)}/><ellipse cx="110" cy="74" rx="16" ry="30" fill="#5FA04A" {W(2.6)}/>'
    f'<rect x="30" y="102" width="68" height="8" fill="#F4EEE4" {W(2.6)}/>'
    + "".join(f'<rect x="{x}" y="62" width="7" height="40" fill="#FFFFFF" {W(2.4)}/>' for x in (36, 52, 68, 84))
    + f'<rect x="30" y="54" width="68" height="10" fill="#F4EEE4" {W(2.6)}/>'
    + f'<path d="M30 54 Q64 18 98 54Z" fill="#5FB7A0" {W(3)}/>'
    + eye(57, 59, .5) + eye(71, 59, .5)
    + f'<ellipse cx="66" cy="28" rx="10" ry="7" fill="#8E9BB4" {W(2.4)}/><circle cx="74" cy="22" r="5" fill="#8E9BB4" {W(2.2)}/>'
    + f'<path d="M78 22 l5 1 l-5 2Z" fill="#F2A33A"/>' + eye(75, 21, .35))

# 8. Парк имени Воровского — арт-объект «кот-пират»
I["fun-park-vorovskogo"] = ("#E0ECFF", "#5468C8",
    "рыжий кот-пират с чёрной повязкой на глазу и в треуголке",
    "сидит на парковой скамейке и смотрит в подзорную трубу на грибы-мухоморы у дорожки",
    f'<rect x="-4" y="108" width="136" height="24" fill="#7FC66A"/>'
    f'<rect x="14" y="84" width="74" height="8" rx="2" fill="#B5783E" {W(2.4)}/><path d="M20 92 L20 110 M82 92 L82 110" stroke="{O}" stroke-width="4"/>'
    f'<ellipse cx="50" cy="70" rx="20" ry="18" fill="#F59A3E" {W(3)}/>'
    f'<circle cx="50" cy="46" r="16" fill="#F59A3E" {W(3)}/><path d="M38 36 L36 24 L46 32Z M62 36 L64 24 L54 32Z" fill="#F59A3E" {W(2.4)}/>'
    f'<path d="M30 34 Q50 14 70 34 Q50 28 30 34Z" fill="#2A2A3A" {W(2.4)}/><circle cx="50" cy="26" r="3" fill="#fff"/>'
    f'<circle cx="44" cy="46" r="5" fill="#2A2A3A"/><path d="M36 40 L62 50" stroke="#2A2A3A" stroke-width="2"/>' + eye(56, 46, .6)
    + f'<path d="M46 54 q4 3 8 0" fill="none" stroke="{O}" stroke-width="2"/>'
    + f'<path d="M64 48 L90 40" stroke="#C8A040" stroke-width="7" stroke-linecap="round"/><path d="M88 41 L94 39" stroke="{O}" stroke-width="9" stroke-linecap="round"/>'
    + f'<path d="M100 104 L100 96" stroke="#fff" stroke-width="5"/><path d="M90 98 Q100 82 112 98Z" fill="#E8343A" {W(2.4)}/>'
    + '<circle cx="96" cy="92" r="2" fill="#fff"/><circle cx="104" cy="90" r="2" fill="#fff"/>'
    + f'<path d="M116 106 L116 100" stroke="#fff" stroke-width="4"/><path d="M110 102 Q116 92 123 102Z" fill="#E8343A" {W(2)}/>')

# 9. Парк им. Лужкова — набережная в затоне: чайка в тельняшке на парапете над рекой
I["fun-park-luzhkova"] = ("#E2F6F7", "#3FA7B5",
    "белая чайка в тельняшке с биноклем на шее",
    "стоит на гранитном парапете набережной над рекой, а по воде плывёт маленький речной трамвайчик",
    f'<rect x="-4" y="80" width="136" height="52" fill="#2E86B8"/>'
    + "".join(f'<path d="M{x} {y} q6 -4 12 0" fill="none" stroke="#9FD6F0" stroke-width="2.4"/>' for x, y in ((10, 96), (60, 112), (96, 100)))
    + f'<rect x="-4" y="70" width="80" height="16" fill="#A8A2A0" {W(2.6)}/>'
    + f'<path d="M84 92 L118 92 L114 102 L88 102Z" fill="#FFFFFF" {W(2.4)}/><rect x="92" y="84" width="18" height="8" fill="#F2C94C" {W(2)}/>'
    + f'<ellipse cx="38" cy="50" rx="16" ry="18" fill="#FFFFFF" {W(3)}/>'
    + "".join(f'<path d="M24 {y} Q38 {y+3} 52 {y}" fill="none" stroke="#2E5EA8" stroke-width="2.6"/>' for y in (48, 56, 64))
    + f'<circle cx="40" cy="26" r="11" fill="#FFFFFF" {W(3)}/><path d="M50 26 L62 29 L50 31Z" fill="#F2A33A" {W(2)}/>'
    + eye(42, 24, .55)
    + f'<path d="M22 46 Q12 54 22 62" fill="#D8DEE6" {W(2.4)}/>'
    + f'<path d="M34 70 L32 76 M42 70 L44 76" stroke="#F2A33A" stroke-width="3"/>'
    + f'<rect x="30" y="38" width="6" height="6" fill="{O}"/><rect x="38" y="38" width="6" height="6" fill="{O}"/>')

# 10. Щукинский парк — детские площадки прямо у метро: песочница-черепашка с ведёрком на панцире
I["fun-shchukinsky-park"] = ("#FCEFD8", "#E0A84A",
    "песочница в виде большой зелёной черепахи с песком в панцире",
    "в песке на её спине торчит синяя лопатка и стоит красная формочка-звёздочка, черепаха довольно жмурится",
    f'<rect x="-4" y="104" width="136" height="28" fill="#9ED17A"/>'
    f'<ellipse cx="62" cy="88" rx="44" ry="22" fill="#3FA65A" {W(3)}/>'
    f'<ellipse cx="62" cy="80" rx="36" ry="12" fill="#F2D58A" {W(2.6)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1.6" fill="#D2B060"/>' for x, y in ((44, 80), (56, 76), (70, 82), (80, 78), (52, 84)))
    + f'<circle cx="112" cy="84" r="12" fill="#6CC070" {W(3)}/>'
    + f'<path d="M106 82 q3 -3 6 0 M114 82 q3 -3 6 0" fill="none" stroke="{O}" stroke-width="2.4" stroke-linecap="round"/>' + SM(113, 88, 3)
    + f'<path d="M30 104 L26 112 M50 108 L48 116 M78 108 L80 116 M96 104 L100 112" stroke="#3FA65A" stroke-width="8" stroke-linecap="round"/>'
    + f'<path d="M50 78 L44 54" stroke="#3E7BE0" stroke-width="4" stroke-linecap="round"/><path d="M40 46 L48 46 L48 56 L40 56Z" fill="#3E7BE0" {W(2)}/>'
    + f'<path d="M76 66 l4 8 l9 1 l-7 6 l2 9 l-8 -5 l-8 5 l2 -9 l-7 -6 l9 -1Z" fill="#E8483A" {W(2.2)}/>')

# 11. Парк «Вагоноремонт» — по имени района: старый вагончик-клумба с цветами
I["fun-park-vagonoremont"] = ("#FFF1E6", "#E06A4A",
    "красный железнодорожный вагончик-клумба с окошками-глазками",
    "стоит на коротком отрезке рельсов в парке, из крыши вместо груза растут тюльпаны и ромашки",
    f'<rect x="-4" y="104" width="136" height="28" fill="#8CCB6A"/>'
    f'<path d="M8 110 H120" stroke="#6E5A4A" stroke-width="4"/>' + "".join(f'<rect x="{x}" y="108" width="8" height="10" fill="#9A7A5A"/>' for x in (14, 34, 54, 74, 94, 112))
    + f'<rect x="20" y="56" width="88" height="42" rx="6" fill="#D8423A" {W(3)}/>'
    + f'<rect x="30" y="64" width="22" height="18" rx="4" fill="#BFE6FF" {W(2.4)}/><rect x="76" y="64" width="22" height="18" rx="4" fill="#BFE6FF" {W(2.4)}/>'
    + eye(41, 73, .7) + eye(87, 73, .7) + f'<path d="M56 88 Q64 94 72 88" fill="none" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>'
    + f'<circle cx="38" cy="100" r="8" fill="#555" {W(2.6)}/><circle cx="90" cy="100" r="8" fill="#555" {W(2.6)}/>'
    + f'<rect x="20" y="48" width="88" height="10" fill="#7A4A2E" {W(2.4)}/>'
    + "".join(f'<path d="M{x} 48 L{x} 30" stroke="#3E8E2E" stroke-width="2.6"/>' for x in (34, 52, 70, 90))
    + f'<path d="M28 30 Q34 18 40 30 L37 34 L31 34Z" fill="#FF5A8A" {W(2)}/><path d="M64 30 Q70 18 76 30 L73 34 L67 34Z" fill="#FFD23F" {W(2)}/>'
    + "".join(f'<circle cx="{x}" cy="28" r="6" fill="#fff" {W(1.8)}/><circle cx="{x}" cy="28" r="2.4" fill="#F2B33D"/>' for x in (52, 90)))

# 12. Парк Школьников — школьный ранец с лицом отдыхает на скамейке под деревом
I["fun-park-shkolnikov"] = ("#E9F0FF", "#7F8FE0",
    "синий школьный ранец с застёжками-глазами и свисающими лямками",
    "отдыхает на парковой скамейке под кроной дерева, рядом на земле лежит жёлтый кленовый лист",
    f'<rect x="-4" y="104" width="136" height="28" fill="#8CCB6A"/>'
    f'<path d="M96 104 L96 40" stroke="#8A5A3A" stroke-width="8"/><circle cx="96" cy="30" r="26" fill="#5FB548" {W(3)}/>'
    f'<rect x="10" y="84" width="84" height="8" rx="2" fill="#C88A55" {W(2.4)}/><rect x="10" y="70" width="84" height="6" rx="2" fill="#C88A55" {W(2.2)}/>'
    f'<path d="M16 92 L16 108 M88 92 L88 108" stroke="{O}" stroke-width="4"/>'
    f'<rect x="30" y="40" width="40" height="46" rx="10" fill="#3E6BE0" {W(3)}/>'
    f'<path d="M30 52 Q50 36 70 52 L70 58 Q50 48 30 58Z" fill="#2A4FB0" {W(2.4)}/>'
    f'<rect x="38" y="56" width="8" height="10" rx="2" fill="#F2C94C" {W(2)}/><rect x="54" y="56" width="8" height="10" rx="2" fill="#F2C94C" {W(2)}/>'
    + eye(42, 61, .45) + eye(58, 61, .45) + SM(50, 74, 4)
    + f'<path d="M34 86 Q30 98 36 104 M66 86 Q70 98 64 104" fill="none" stroke="#2A4FB0" stroke-width="3.4"/>'
    + f'<path d="M104 118 l6 -6 l2 4 l6 -2 l-2 6 l4 2 l-8 4 l0 4 l-4 -4 l-6 2Z" fill="#F2B33D" {W(1.8)}/>')

# 13. Парк «Никулино» — кленовый лист-парашютист планирует над аллеей
I["fun-park-nikulino"] = ("#FFE9D6", "#F08A4A",
    "огненно-красный кленовый лист-парашютист в маленьких лётных очках",
    "плавно планирует вниз над парковой аллеей с фонарём, держась за черешок как за стропу",
    f'<path d="M30 132 L56 92 L72 92 L98 132Z" fill="#E8D2A0" {W(2.6)}/>'
    f'<rect x="-4" y="92" width="136" height="6" fill="#8CCB6A"/>'
    f'<path d="M104 92 L104 54" stroke="{O}" stroke-width="4"/><path d="M96 54 L112 54 L108 44 L100 44Z" fill="#FFE07A" {W(2.4)}/>'
    f'<path d="M58 14 L64 30 L76 20 L74 36 L92 34 L80 46 L94 54 L74 56 L76 70 L60 60 L44 70 L46 56 L26 54 L40 46 L28 34 L46 36 L44 20 L56 30Z" fill="#E8483A" {W(3)}/>'
    + f'<path d="M60 60 L58 84" stroke="#8A3A2A" stroke-width="3" stroke-linecap="round"/>'
    + f'<rect x="48" y="34" width="10" height="7" rx="3" fill="#BFE6FF" {W(1.8)}/><rect x="62" y="34" width="10" height="7" rx="3" fill="#BFE6FF" {W(1.8)}/>'
    + eye(53, 38, .4) + eye(67, 38, .4) + SM(60, 46, 4)
    + "".join(f'<path d="M{x} {y} q4 2 6 6" fill="none" stroke="#fff" stroke-width="2" opacity=".8"/>' for x, y in ((24, 20), (98, 24))))

# 14. Юго-Западный лесопарк — тихие прогулки: дятел-барабанщик в лесу
I["fun-yugo-zapadny-lesopark"] = ("#E6F3E8", "#4F9A6A",
    "пёстрый дятел в красной шапочке с крошечными барабанными палочками в лапках",
    "сидит на берёзовом стволе и отбивает ритм, от ствола разлетаются нотки-щепочки",
    f'<rect x="44" y="-4" width="26" height="136" fill="#F7F7F2" {W(3)}/>'
    + "".join(f'<path d="M{x} {y} h10" stroke="{O}" stroke-width="3" stroke-linecap="round"/>' for x, y in ((48, 14), (56, 40), (46, 96), (54, 116)))
    + f'<ellipse cx="82" cy="66" rx="14" ry="20" fill="#2A2A3A" {W(3)}/><ellipse cx="84" cy="70" rx="8" ry="13" fill="#FFFFFF"/>'
    + f'<circle cx="84" cy="42" r="12" fill="#FFFFFF" {W(3)}/><path d="M74 36 Q84 26 94 36 L90 38 Q84 32 78 38Z" fill="#E8343A" {W(2)}/>'
    + f'<path d="M73 44 L62 46 L73 49Z" fill="#6E6A6A" {W(2)}/>' + eye(82, 42, .55)
    + f'<path d="M80 84 Q76 96 70 100" fill="#2A2A3A" {W(2.4)}/>'
    + f'<path d="M92 60 L104 50 M94 70 L106 66" stroke="#C88A55" stroke-width="3" stroke-linecap="round"/>'
    + '<circle cx="105" cy="49" r="2.6" fill="#E8343A"/><circle cx="107" cy="66" r="2.6" fill="#E8343A"/>'
    + f'<path d="M20 40 v-12 l8 -2 v12" fill="none" stroke="{O}" stroke-width="2.4"/><circle cx="18" cy="40" r="3" fill="{O}"/><circle cx="26" cy="38" r="3" fill="{O}"/>'
    + f'<path d="M22 76 v-10" stroke="{O}" stroke-width="2.4"/><circle cx="20" cy="76" r="3" fill="{O}"/>')

# 15. Дом бабочек ВДНХ — хамелеон ловит взглядом голубую бабочку
I["fun-dom-babochek-vdnh"] = ("#E8FFF0", "#3FBF8A",
    "ярко-зелёный хамелеон со скрученным в спираль хвостом",
    "сидит на ветке в тропической оранжерее и восхищённо скосил глаз на огромную голубую бабочку-морфо у себя на носу",
    f'<path d="M-4 96 Q40 86 80 92 Q110 96 132 88" fill="none" stroke="#7A5236" stroke-width="8" stroke-linecap="round"/>'
    + "".join(f'<path d="M{x} {y} q-12 -8 -4 -20 q10 6 4 20Z" fill="#2FA060" {W(2)}/>' for x, y in ((14, 92), (112, 90), (98, 96)))
    + f'<path d="M30 84 Q30 58 56 54 Q84 52 90 74 Q92 88 74 90 L40 90 Q30 90 30 84Z" fill="#7FD04A" {W(3)}/>'
    + f'<path d="M34 86 Q14 90 16 106 Q18 118 30 114 Q38 108 30 102 Q24 100 26 106" fill="none" stroke="#7FD04A" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M34 86 Q14 90 16 106 Q18 118 30 114 Q38 108 30 102 Q24 100 26 106" fill="none" stroke="{O}" stroke-width="1.6" stroke-linecap="round" opacity=".5"/>'
    + f'<circle cx="80" cy="66" r="9" fill="#5DB83A" {W(2.4)}/><circle cx="83" cy="64" r="4" fill="{O}"/><circle cx="82" cy="63" r="1.4" fill="#fff"/>'
    + f'<path d="M58 92 L56 100 M74 92 L76 100" stroke="{O}" stroke-width="3" stroke-linecap="round"/>'
    + f'<path d="M86 76 Q90 80 94 78" fill="none" stroke="{O}" stroke-width="2"/>'
    + f'<path d="M96 56 Q84 36 96 32 Q104 40 100 54Z M100 56 Q116 40 120 48 Q116 60 102 58Z" fill="#3E7BF0" {W(2.4)}/>'
    + f'<path d="M98 58 L96 66" stroke="{O}" stroke-width="2.4"/>' + sparkle(18, 24, 5, "#fff"))

# 16. Зооландия (Истра) — козлёнок жуёт морковку из бумажного стаканчика с овощами
I["fun-zoolandia-istra"] = ("#FFF6DA", "#E9C24A",
    "белый козлёнок с розовыми ушками и маленькой бородкой",
    "встал передними копытцами на деревянную изгородь и тянется к бумажному стаканчику с морковкой и капустой",
    f'<rect x="-4" y="108" width="136" height="24" fill="#8CCB6A"/>'
    f'<path d="M6 76 H122 M6 94 H122" stroke="#A8743E" stroke-width="7"/>' + "".join(f'<rect x="{x}" y="66" width="8" height="46" fill="#C88A55" {W(2.2)}/>' for x in (10, 60, 110))
    + f'<ellipse cx="48" cy="62" rx="22" ry="18" fill="#FFFFFF" {W(3)}/>'
    + f'<path d="M36 76 L34 92 M58 76 L62 92" stroke="{O}" stroke-width="5" stroke-linecap="round"/>'
    + f'<circle cx="64" cy="40" r="14" fill="#FFFFFF" {W(3)}/>'
    + f'<path d="M52 34 Q42 30 44 40 Q50 40 54 38Z M76 34 Q86 30 84 40 Q78 40 74 38Z" fill="#FFB6C8" {W(2)}/>'
    + f'<path d="M58 28 L56 20 M70 28 L72 20" stroke="#B5A07A" stroke-width="3.4" stroke-linecap="round"/>'
    + eye(59, 40, .55) + eye(69, 40, .55) + f'<path d="M64 52 L62 60 L66 60Z" fill="#E8E8E0" {W(1.6)}/>' + SM(64, 47, 3)
    + f'<path d="M86 50 L104 50 L100 72 L90 72Z" fill="#F4EEE4" {W(2.6)}/>'
    + f'<path d="M92 50 L88 34" stroke="#F5822A" stroke-width="5" stroke-linecap="round"/><path d="M88 34 l-3 -6 M88 34 l2 -7" stroke="#3E8E2E" stroke-width="2.4"/>'
    + f'<circle cx="100" cy="46" r="6" fill="#A8DC7A" {W(2)}/>')

# 17. Аттра-Град (Люберцы) — цепочная карусель-ромашка, на сиденьях кружатся дети
I["fun-attra-grad-lyubertsy"] = ("#FDE8FF", "#B65CE0",
    "цепочная карусель с крышей-ромашкой и улыбкой на жёлтой серединке",
    "кружит на цепочках три сиденья с разлетающимися косичками, над прудом Наташинского парка",
    f'<rect x="-4" y="112" width="136" height="20" fill="#5EB3E6"/>'
    f'<rect x="60" y="44" width="8" height="70" fill="#E8E8F2" {W(2.6)}/>'
    + "".join(f'<ellipse cx="{64+28*__import__("math").cos(a)}" cy="{30+8*__import__("math").sin(a)}" rx="11" ry="6" fill="#FFFFFF" {W(2.2)}/>'
              for a in [i * 0.785 for i in range(8)])
    + f'<ellipse cx="64" cy="30" rx="14" ry="10" fill="#FFD23F" {W(2.6)}/>' + eye(59, 29, .5) + eye(69, 29, .5) + SM(64, 33, 3)
    + f'<path d="M40 40 L18 76 M88 40 L110 76 M64 42 L64 82" stroke="{O}" stroke-width="1.8"/>'
    + f'<rect x="10" y="76" width="16" height="6" rx="2" fill="#E8483A" {W(2)}/><rect x="102" y="76" width="16" height="6" rx="2" fill="#3E7BE0" {W(2)}/>'
    + f'<rect x="56" y="82" width="16" height="6" rx="2" fill="#2FB070" {W(2)}/>'
    + f'<circle cx="18" cy="70" r="5" fill="#FFD9B8" {W(1.8)}/><path d="M12 68 L4 64 M24 68 L28 62" stroke="#8A5A3A" stroke-width="2.4"/>'
    + f'<circle cx="110" cy="70" r="5" fill="#FFD9B8" {W(1.8)}/><circle cx="64" cy="76" r="5" fill="#FFD9B8" {W(1.8)}/>')

# 18. МиниЛандия — бегемотик выныривает из сухого бассейна с шариками
I["fun-minilandia-crocus"] = ("#E6F0FF", "#6A8CF0",
    "сиреневый бегемотик с круглыми ноздрями",
    "выныривает по плечи из сухого бассейна, полного разноцветных шариков, и подбрасывает один шарик носом",
    f'<rect x="10" y="74" width="108" height="50" rx="14" fill="#FFFFFF" {W(3)}/>'
    + f'<ellipse cx="64" cy="54" rx="26" ry="22" fill="#B48FE0" {W(3)}/>'
    + f'<ellipse cx="64" cy="66" rx="20" ry="12" fill="#C9AAF0" {W(2.6)}/>'
    + f'<circle cx="57" cy="64" r="2.4" fill="{O}"/><circle cx="71" cy="64" r="2.4" fill="{O}"/>'
    + eye(54, 46, .6) + eye(74, 46, .6) + f'<circle cx="46" cy="34" r="6" fill="#B48FE0" {W(2.4)}/><circle cx="82" cy="34" r="6" fill="#B48FE0" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="7" fill="{c}" {W(2)}/>' for x, y, c in (
        (20, 82, "#FF5A6E"), (34, 80, "#FFD23F"), (48, 84, "#3EC0F0"), (80, 84, "#5FD06A"), (94, 80, "#FF8A2A"), (108, 82, "#FF5A6E"),
        (24, 96, "#5FD06A"), (40, 98, "#B05AE0"), (56, 96, "#FF8A2A"), (72, 98, "#FFD23F"), (88, 96, "#3EC0F0"), (104, 98, "#B05AE0"),
        (30, 112, "#FFD23F"), (48, 112, "#FF5A6E"), (66, 112, "#3EC0F0"), (84, 112, "#5FD06A"), (100, 112, "#FF8A2A")))
    + f'<circle cx="64" cy="18" r="8" fill="#FF5A6E" {W(2.4)}/><path d="M60 26 l-2 4 M68 26 l2 4" stroke="{O}" stroke-width="1.6"/>')

# 19. Пушкинский музей — античная гипсовая голова в лавровом венке разглядывает в лупу египетского котика-статуэтку
I["fun-gmii-pushkin-main"] = ("#F4EEE2", "#BFA27A",
    "белая гипсовая античная голова-бюст в зелёном лавровом венке",
    "стоит на постаменте с колоннами и через лупу с любопытством разглядывает маленькую чёрную египетскую кошку-статуэтку",
    f'<rect x="14" y="88" width="56" height="34" fill="#E6DCCB" {W(3)}/>'
    + "".join(f'<rect x="{x}" y="92" width="6" height="26" fill="#F7F2EA" {W(1.8)}/>' for x in (22, 39, 56))
    + f'<path d="M24 88 Q20 70 30 64 L54 64 Q64 70 60 88Z" fill="#FAF8F4" {W(3)}/>'
    + f'<path d="M26 44 Q24 18 42 16 Q60 18 58 44 Q58 62 42 66 Q26 62 26 44Z" fill="#FAF8F4" {W(3)}/>'
    + "".join(f'<path d="M{x} {y} q-6 -4 -2 -10 q6 2 2 10Z" fill="#5FA04A" {W(1.6)}/>' for x, y in ((28, 28), (34, 20), (44, 16), (54, 22), (58, 30)))
    + f'<path d="M32 40 q4 -3 8 0 M46 40 q4 -3 8 0" fill="none" stroke="#9A9088" stroke-width="2"/>' + eye(36, 44, .5) + eye(50, 44, .5)
    + f'<path d="M43 46 L41 54 L45 54" fill="none" stroke="#9A9088" stroke-width="1.8"/>' + SM(43, 58, 3)
    + f'<circle cx="80" cy="56" r="12" fill="#DDF3FF" fill-opacity=".7" {W(3)}/><path d="M71 64 L60 74" stroke="#7A5236" stroke-width="5" stroke-linecap="round"/>'
    + f'<rect x="84" y="104" width="30" height="8" fill="#C9A86A" {W(2.2)}/>'
    + f'<path d="M92 104 Q88 84 96 76 L94 66 L100 72 L106 66 L104 76 Q112 84 108 104Z" fill="#2A2A3A" {W(2.4)}/>'
    + '<circle cx="100" cy="76" r="1.8" fill="#F2C94C"/><path d="M96 90 h8" stroke="#F2C94C" stroke-width="2"/>')

# 20. Lazertag Zone — дымовая арена: инфракрасный бластер-робот с красным лучом
I["fun-lazertag-zone-solntsevo"] = ("#1E2440", "#3A2A6A",
    "футуристичный светящийся лазертаг-шлем с антенной и зелёным визором-глазами",
    "парит в тёмном неоновом лабиринте арены, а мимо него проносится тонкий красный луч и отражается от бочки",
    f'<rect x="-4" y="96" width="136" height="36" fill="#2A3058"/>'
    + f'<rect x="8" y="58" width="22" height="40" fill="#3A4078" {W(2.4)}/><rect x="98" y="50" width="24" height="48" fill="#3A4078" {W(2.4)}/>'
    + f'<path d="M8 58 h22 M98 50 h24" stroke="#39F0FF" stroke-width="2.4"/>'
    + f'<ellipse cx="18" cy="104" rx="10" ry="6" fill="#F2A33A" {W(2)}/>'
    + f'<path d="M36 64 Q34 30 64 28 Q94 30 92 64 Q92 74 64 74 Q36 74 36 64Z" fill="#E8E8F2" {W(3)}/>'
    + f'<path d="M42 50 Q64 42 86 50 L84 62 Q64 58 44 62Z" fill="#3BFF8A" {W(2.4)}/>'
    + eye(56, 54, .55) + eye(72, 54, .55)
    + f'<path d="M64 28 L64 14" stroke="{O}" stroke-width="3"/><circle cx="64" cy="12" r="4" fill="#FF3A5A" {W(2)}/>'
    + f'<path d="M-4 86 L60 92 L124 82" fill="none" stroke="#FF2A4A" stroke-width="2.6"/>'
    + f'<path d="M-4 86 L60 92 L124 82" fill="none" stroke="#FF9AAA" stroke-width="1" />'
    + sparkle(110, 20, 4, "#39F0FF") + sparkle(20, 24, 3, "#FF5AE0"))

# 21. Форт Боярд (Подольск) — старинный ключ-подсказка выпрыгивает из сундука у каменной башни
I["fun-fort-boyard-podolsk"] = ("#FFF1D0", "#D9893A",
    "золотой старинный ключ с узорной головкой-лицом",
    "выпрыгнул из приоткрытого деревянного сундука с испытаниями у подножия круглой каменной башни с флажком",
    f'<rect x="72" y="28" width="40" height="92" fill="#B8AE9E" {W(3)}/>'
    + "".join(f'<rect x="{x}" y="18" width="8" height="12" fill="#B8AE9E" {W(2.2)}/>' for x in (72, 88, 104))
    + "".join(f'<path d="M72 {y} H112" stroke="#8E8676" stroke-width="2"/>' for y in (50, 72, 94))
    + f'<rect x="86" y="58" width="12" height="18" rx="6" fill="#3A3048" {W(2)}/>'
    + f'<path d="M92 18 L92 4 L106 8 L92 12" fill="#E8343A" {W(2)}/>'
    + f'<rect x="10" y="88" width="56" height="30" rx="4" fill="#9A5E2E" {W(3)}/>'
    + f'<path d="M10 88 L14 70 L70 74 L66 88Z" fill="#B87440" {W(3)}/>'
    + f'<path d="M10 100 H66" stroke="#F2C94C" stroke-width="3"/><rect x="34" y="96" width="8" height="10" fill="#F2C94C" {W(1.8)}/>'
    + f'<circle cx="38" cy="38" r="14" fill="#F6C83A" {W(3)}/><circle cx="38" cy="38" r="6" fill="#FFF1D0" {W(2)}/>'
    + eye(33, 34, .4) + eye(43, 34, .4)
    + f'<rect x="35" y="52" width="6" height="26" fill="#F6C83A" {W(2.4)}/><path d="M41 66 h7 v5 h-7 M41 72 h5" fill="#F6C83A" {W(2)}/>'
    + sparkle(18, 20, 5, "#fff") + sparkle(60, 50, 4, "#fff"))

# 22. Мини-зоопарк в Невском парке — фазан с пышным хвостом гуляет по вольеру
I["fun-minizoo-nevsky-park"] = ("#F1F7E6", "#9CC45A",
    "золотисто-рыжий фазан с длинным полосатым хвостом и красными щёчками",
    "важно шагает по вольеру с сеточкой, а рядом из домика-курятника выглядывает пёстрая курочка",
    f'<rect x="-4" y="104" width="136" height="28" fill="#C8B07A"/>'
    + "".join(f'<path d="M{x} 30 V104" stroke="#9A9AA6" stroke-width="1.6"/>' for x in range(6, 128, 14))
    + f'<path d="M-4 30 H132" stroke="#7A7A86" stroke-width="3"/>'
    + f'<rect x="84" y="62" width="40" height="42" fill="#B5783E" {W(3)}/><path d="M80 64 L104 44 L128 64Z" fill="#D8423A" {W(3)}/>'
    + f'<circle cx="104" cy="82" r="10" fill="#3A2A20" {W(2)}/><circle cx="104" cy="82" r="7" fill="#F4EEE4" {W(1.8)}/>'
    + eye(102, 81, .35) + f'<path d="M100 74 l2 -4 l2 4" fill="#E8343A"/>'
    + f'<path d="M30 78 Q4 70 -4 58 Q12 66 34 70Z" fill="#C8783A" {W(2.4)}/>'
    + "".join(f'<path d="M{6+i*7} {64+i*2} l3 4" stroke="{O}" stroke-width="1.6"/>' for i in range(4))
    + f'<ellipse cx="46" cy="76" rx="20" ry="14" fill="#E8913A" {W(3)}/>'
    + f'<path d="M58 70 Q62 50 60 40" fill="none" stroke="#2E7D5A" stroke-width="10" stroke-linecap="round"/>'
    + f'<circle cx="60" cy="38" r="9" fill="#2E7D5A" {W(2.6)}/><ellipse cx="62" cy="38" rx="5" ry="6" fill="#E8343A"/>'
    + eye(63, 37, .45) + f'<path d="M68 39 l6 2 l-6 2Z" fill="#E8D27A" {W(1.4)}/>'
    + f'<path d="M58 50 H64" stroke="#fff" stroke-width="3"/>'
    + f'<path d="M42 90 L40 104 M52 90 L54 104" stroke="#A8743E" stroke-width="3" stroke-linecap="round"/>')

# 23. Пеленальная — ТРЦ «Авеню Юго-Запад»: подгузник с крылышками-ангелочек
I["chg-avenue-sw"] = ("#EAF6FF", "#7CC4F0",
    "белоснежный подгузник с крылышками и ямочками на щёчках",
    "порхает над пеленальным столиком с голубым матрасиком, рассыпая пузырьки свежести",
    f'<rect x="16" y="92" width="96" height="12" rx="4" fill="#9AD0F5" {W(3)}/><rect x="22" y="104" width="84" height="22" fill="#F4EEE4" {W(2.6)}/>'
    + f'<path d="M64 104 V126" stroke="{O}" stroke-width="2"/><circle cx="56" cy="115" r="2" fill="{O}"/><circle cx="72" cy="115" r="2" fill="{O}"/>'
    + f'<path d="M34 44 Q14 30 10 46 Q20 54 38 54Z M94 44 Q114 30 118 46 Q108 54 90 54Z" fill="#FFFFFF" {W(2.6)}/>'
    + f'<path d="M36 36 H92 Q90 62 76 72 Q64 78 52 72 Q38 62 36 36Z" fill="#FFFFFF" {W(3)}/>'
    + f'<rect x="36" y="34" width="56" height="8" rx="3" fill="#7CC4F0" {W(2.2)}/>'
    + face(64, 54, d=9, k=.75)
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFFFFF" fill-opacity=".8" {W(1.4)}/>' for x, y, r in ((24, 76, 4), (100, 70, 5), (108, 84, 3), (30, 18, 3)))
    + sparkle(64, 14, 6, "#FFF6A8"))

# 24. Пеленальная — ТРЦ «Весна»: бутон-подснежник, укутанный в листья, как в пелёнку
I["chg-trc-vesna"] = ("#EFFFF0", "#7FD6A0",
    "белый подснежник-малыш с сонными глазками",
    "укутан в два зелёных листа, как в пелёнку, и сладко спит на мягкой розовой подушке с бантиком",
    f'<ellipse cx="64" cy="98" rx="46" ry="16" fill="#FFC2D6" {W(3)}/><path d="M20 92 Q40 86 64 88" fill="none" stroke="#FF9AB8" stroke-width="2"/>'
    + f'<path d="M104 92 l10 -6 l2 10Z M104 92 l12 4 l-6 8Z" fill="#FF7FA8" {W(1.8)}/>'
    + f'<path d="M64 92 Q34 86 38 56 Q48 68 64 74Z" fill="#4FB070" {W(3)}/><path d="M64 92 Q94 86 90 56 Q80 68 64 74Z" fill="#5FC27E" {W(3)}/>'
    + f'<path d="M64 74 Q48 64 50 42 Q56 26 64 22 Q72 26 78 42 Q80 64 64 74Z" fill="#FFFFFF" {W(3)}/>'
    + f'<path d="M64 22 Q66 12 74 10" fill="none" stroke="#3E8E2E" stroke-width="3" stroke-linecap="round"/>'
    + f'<path d="M55 50 q4 3 8 0 M66 50 q4 3 8 0" fill="none" stroke="{O}" stroke-width="2.2" stroke-linecap="round"/>' + BL(52, 58, .8) + BL(76, 58, .8)
    + f'<text x="92" y="38" font-family="Arial" font-weight="bold" font-size="12" fill="{O}">z</text><text x="100" y="28" font-family="Arial" font-weight="bold" font-size="9" fill="{O}">z</text>')

# 25. Пеленальная — ТРЦ «Перловский»: жемчужинка-малыш в чепчике в раскрытой ракушке-колыбели (Перловский — «перл», жемчуг)
I["chg-trc-perlovsky"] = ("#F2EEFF", "#A38AE8",
    "розовая жемчужинка-малыш в кружевном чепчике",
    "лежит в раскрытой ракушке-колыбели, как в люльке, и держит в ручке погремушку",
    f'<path d="M14 88 Q64 128 114 88 Q100 104 64 106 Q28 104 14 88Z" fill="#F7D9E8" {W(3)}/>'
    + f'<path d="M14 88 Q20 30 64 24 Q108 30 114 88 Q64 70 14 88Z" fill="#FFE8F2" {W(3)}/>'
    + "".join(f'<path d="M64 26 L{x} 84" stroke="#E8B8CC" stroke-width="2"/>' for x in (24, 40, 56, 72, 88, 104))
    + f'<circle cx="64" cy="82" r="18" fill="#FFD3E0" {W(3)}/><circle cx="58" cy="76" r="5" fill="#fff" opacity=".7"/>'
    + f'<path d="M46 80 Q46 60 64 60 Q82 60 82 80 Q74 70 64 70 Q54 70 46 80Z" fill="#FFFFFF" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="#E8D8F0"/>' for x, y in ((50, 70), (58, 64), (70, 64), (78, 70)))
    + face(64, 84, d=6, k=.6)
    + f'<path d="M80 92 L92 100" stroke="#F2B33D" stroke-width="3"/><circle cx="95" cy="102" r="5" fill="#F2B33D" {W(2)}/>')

# 26. Пеленальная — ТЦ «Варшавский»: бутылочка с молоком в чепчике на пеленальном столике
I["chg-varshavsky"] = ("#FFF8E6", "#F2C46A",
    "детская бутылочка с молоком в вязаном чепчике с помпоном",
    "сидит на пеленальном столике рядом со стопкой сложенных полотенец и машет ручкой",
    f'<rect x="10" y="98" width="108" height="10" rx="3" fill="#C88A55" {W(3)}/><path d="M18 108 V128 M110 108 V128" stroke="{O}" stroke-width="5"/>'
    + f'<rect x="76" y="86" width="34" height="12" rx="3" fill="#8FD0F0" {W(2.4)}/><rect x="78" y="74" width="30" height="12" rx="3" fill="#FFB6C8" {W(2.4)}/><rect x="80" y="62" width="26" height="12" rx="3" fill="#B6E8A0" {W(2.4)}/>'
    + f'<rect x="32" y="50" width="34" height="48" rx="10" fill="#FFFFFF" {W(3)}/><rect x="34" y="64" width="30" height="32" rx="8" fill="#FFF4D0"/>'
    + "".join(f'<path d="M32 {y} h8" stroke="{O}" stroke-width="2"/>' for y in (60, 70, 80))
    + f'<path d="M30 52 Q49 22 68 52Z" fill="#7FB8F0" {W(3)}/><circle cx="49" cy="26" r="6" fill="#FF7FA8" {W(2.2)}/>'
    + f'<path d="M30 52 Q49 46 68 52" fill="none" stroke="#4A88D0" stroke-width="3"/>'
    + face(49, 76, d=7, k=.65)
    + f'<path d="M66 70 Q76 60 74 50" fill="none" stroke="{O}" stroke-width="3" stroke-linecap="round"/>')

# 27. Пеленальная — аутлет «Новая Рига»: мамина сумка с ручками-ушками
I["chg-newriga-outlet"] = ("#F0F4FF", "#8E9EE0",
    "мамина сумка-переноска с ручками-ушками и мордашкой на кармашке",
    "стоит на газоне у пряничных домиков аутлета, а из неё выглядывают погремушка и свёрнутый подгузник",
    f'<rect x="-4" y="104" width="136" height="28" fill="#8CCB6A"/>'
    + f'<rect x="4" y="52" width="26" height="40" fill="#FFF2DA" {W(2.4)}/><path d="M0 54 L17 38 L34 54Z" fill="#C8423A" {W(2.4)}/>'
    + f'<rect x="98" y="48" width="28" height="44" fill="#FFF2DA" {W(2.4)}/><path d="M94 50 L112 32 L130 50Z" fill="#3A6AB0" {W(2.4)}/>'
    + f'<rect x="12" y="66" width="10" height="10" fill="#BFE6FF" {W(1.8)}/><rect x="106" y="62" width="12" height="10" fill="#BFE6FF" {W(1.8)}/>'
    + f'<path d="M34 64 L94 64 L88 112 L40 112Z" fill="#E87AA8" {W(3)}/>'
    + f'<path d="M44 66 Q44 40 56 40 Q64 42 62 66 M66 66 Q64 42 72 40 Q84 40 84 66" fill="none" stroke="{O}" stroke-width="4"/>'
    + f'<rect x="50" y="80" width="28" height="22" rx="6" fill="#F7B6D0" {W(2.4)}/>' + face(64, 88, d=6, k=.6)
    + f'<path d="M46 64 L40 48" stroke="#F2B33D" stroke-width="3"/><circle cx="38" cy="44" r="6" fill="#F2B33D" {W(2)}/>'
    + f'<rect x="72" y="50" width="16" height="16" rx="5" fill="#FFFFFF" {W(2.2)}/>')

# 28. Пеленальная — ТРЦ «Вэйпарк»: соска-пустышка с глазками на детских весах
I["chg-waypark"] = ("#E6FFF8", "#5CCFB0",
    "оранжевая соска-пустышка с колечком и глазками на щитке",
    "лежит на белых детских весах-люльке и с гордостью смотрит на стрелку циферблата",
    f'<path d="M14 84 Q64 112 114 84 L108 98 Q64 118 20 98Z" fill="#FFFFFF" {W(3)}/>'
    + f'<rect x="40" y="100" width="48" height="20" rx="4" fill="#E8F2F0" {W(2.6)}/>'
    + f'<circle cx="64" cy="110" r="7" fill="#FFFFFF" {W(2)}/><path d="M64 110 L68 106" stroke="#E8343A" stroke-width="2"/>'
    + f'<ellipse cx="64" cy="66" rx="30" ry="18" fill="#FF9A3A" {W(3)}/>'
    + f'<ellipse cx="64" cy="66" rx="10" ry="8" fill="#FFD6A8" {W(2.4)}/>'
    + f'<circle cx="64" cy="36" r="14" fill="none" stroke="#FF9A3A" stroke-width="6"/><circle cx="64" cy="36" r="14" fill="none" {W(1.6)}/>'
    + eye(46, 64, .6) + eye(82, 64, .6) + BL(42, 72, .7) + BL(86, 72, .7)
    + sparkle(104, 30, 5, "#fff"))

# 29. Пеленальная — ТРЦ «Мари»: ванночка с пеной, в которой плещется резиновый кит
I["chg-trc-mari"] = ("#E3F4FF", "#6FB6F2",
    "голубой резиновый китёнок с фонтанчиком-сердечком",
    "плещется в детской ванночке на ножках, полной мыльной пены и пузырей",
    f'<path d="M24 104 L18 122 M104 104 L110 122" stroke="{O}" stroke-width="4"/>'
    + f'<path d="M14 68 L114 68 Q112 104 64 106 Q16 104 14 68Z" fill="#FFFFFF" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFFFFF" {W(1.8)}/>' for x, y, r in ((22, 66, 8), (36, 62, 9), (92, 62, 9), (106, 66, 8), (50, 66, 6)))
    + f'<path d="M50 70 Q50 44 74 44 Q94 46 94 64 Q90 72 70 72Z" fill="#7EC8F8" {W(3)}/>'
    + f'<path d="M50 62 Q38 52 36 42 Q46 48 52 52Z" fill="#7EC8F8" {W(2.4)}/>'
    + eye(80, 56, .6) + SM(84, 63, 3)
    + f'<path d="M72 44 Q70 30 64 26 M72 44 Q76 30 82 26" fill="none" stroke="#9AD8FF" stroke-width="3" stroke-linecap="round"/>'
    + f'<path d="M73 22 q-4 -6 -8 -2 q-2 4 8 10 q10 -6 8 -10 q-4 -4 -8 2Z" fill="#FF6F9A" {W(1.6)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="#fff" stroke-width="2"/>' for x, y, r in ((24, 40, 5), (104, 36, 6), (112, 50, 3))))

# 30. Пеленальная — ТРЦ «Люблю Молл»: подушка-сердце обнимает спящего малыша
I["chg-lyublyu-moll"] = ("#FFEAF0", "#F27C9C",
    "мягкая красная подушка-сердечко с ручками",
    "нежно обнимает спящего малыша в жёлтом комбинезоне с капюшоном-ушками",
    f'<path d="M64 112 Q16 82 18 50 Q22 26 44 28 Q58 30 64 44 Q70 30 84 28 Q106 26 110 50 Q112 82 64 112Z" fill="#E8344E" {W(3)}/>'
    + f'<path d="M30 46 q4 -10 14 -10" fill="none" stroke="#FF8A9A" stroke-width="4" stroke-linecap="round"/>'
    + f'<ellipse cx="64" cy="70" rx="20" ry="24" fill="#FFD84A" {W(3)}/>'
    + f'<circle cx="64" cy="58" r="14" fill="#FFE2C6" {W(2.6)}/>'
    + f'<path d="M48 54 Q48 38 64 38 Q80 38 80 54 Q74 46 64 46 Q54 46 48 54Z" fill="#FFD84A" {W(2.4)}/>'
    + f'<circle cx="52" cy="40" r="5" fill="#FFD84A" {W(2)}/><circle cx="76" cy="40" r="5" fill="#FFD84A" {W(2)}/>'
    + f'<path d="M57 58 q3 2 6 0 M65 58 q3 2 6 0" fill="none" stroke="{O}" stroke-width="2" stroke-linecap="round"/>' + SM(64, 64, 2)
    + f'<path d="M30 64 Q44 74 50 70 M98 64 Q84 74 78 70" fill="none" stroke="{O}" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M30 64 Q44 74 50 70 M98 64 Q84 74 78 70" fill="none" stroke="#E8344E" stroke-width="3" stroke-linecap="round"/>'
    + face(64, 96, d=8, k=.55, mouth=False) + SM(64, 101, 3))

if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
