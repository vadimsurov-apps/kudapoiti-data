"""Иконки робота fun (2026-11-08, вечер, поиск по районам): 21 место. Каждая придумана и нарисована отдельно
(правило абсолютной уникальности). Сверено со всеми листами icons-catalog (01–40) и icons-src/subjects.txt.
Заняты и НЕ брать: попкорн, бобина, киноплёнка, хлопушка, 3D-очки, неон «КИНО», кинокресло как герой, экран как
герой, проектор, кинокамера, билет, касса, афишная тумба, начос, газировка; виниловая пластинка, граммофон, патефон,
печатный пресс; микроскоп, роботы, ракеты, печатная плата; ткацкий челнок, шелкопряд, ворота усадьбы; горн, галстук,
скворечник; паутинка-пирамида, попугаи, туканы, обезьяны, хамелеон.
Запуск: python3 tools/icons_fun_1108f.py [id ...]  (печатает строки для subjects.txt)"""
import math, os, sys
from draw_icons import s, eye, face, sparkle, O

W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=9, k=0.75, **kw: face(cx, cy, d=d, k=k, **kw)
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")


def svg(a, b, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
<defs>
 <radialGradient id="g" cx="38%" cy="28%" r="85%"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></radialGradient>
 <clipPath id="c"><circle cx="64" cy="64" r="61"/></clipPath>
</defs>
<circle cx="64" cy="64" r="61" fill="url(#g)"/>
<g clip-path="url(#c)">{body}</g>
<ellipse cx="44" cy="22" rx="20" ry="7" fill="#fff" opacity=".3"/>
</svg>'''


def kid(cx, cy, k=1.0, hair="#6B3F23", skin="#FFD9B8"):
    """круглая голова малыша с чёлкой"""
    r = 13 * k
    return (f'<circle cx="{cx}" cy="{cy}" r="{r:.1f}" fill="{skin}" {W(2.8)}/>'
            f'<path d="M{cx-r:.1f} {cy-2*k:.1f} Q{cx-r:.1f} {cy-r-3*k:.1f} {cx:.1f} {cy-r-2*k:.1f} '
            f'Q{cx+r:.1f} {cy-r-3*k:.1f} {cx+r:.1f} {cy-2*k:.1f} Q{cx+4*k:.1f} {cy-9*k:.1f} {cx-r:.1f} {cy-2*k:.1f}Z" '
            f'fill="{hair}" {W(2.4)}/>'
            + face(cx, cy + 2 * k, d=5 * k, k=0.5 * k))


I = {}

# 1. Москино Сатурн — картонный ростовой стенд-ракета с окошком для лица
I["cin-moskino-saturn"] = ("#FFE3BF", "#E2793A",
    "картонный ростовой стенд-ракета с круглым окошком для лица",
    "малыш просунул лицо в окошко стенда в фойе кинотеатра перед сеансом",
    f'<rect x="0" y="104" width="128" height="30" fill="#B5502A" opacity=".55"/>'
    + f'<path d="M86 60 L104 112" stroke="#A8865A" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M64 10 Q90 34 90 74 V100 H38 V74 Q38 34 64 10Z" fill="#E6C08A" {W(3.2)}/>'
    + f'<path d="M64 10 Q78 22 84 36 H44 Q50 22 64 10Z" fill="#E8483F" {W(2.8)}/>'
    + f'<path d="M38 80 L22 104 H40Z M90 80 L106 104 H88Z" fill="#E8483F" {W(2.8)}/>'
    + f'<path d="M50 100 L56 116 H72 L78 100" fill="#FFB33E" {W(2.6)}/>'
    + f'<circle cx="64" cy="62" r="17" fill="#6E5638" {W(3)}/>'
    + kid(64, 63, k=1.05)
    + f'<path d="M44 88 H84" stroke="#C9A06A" stroke-width="2" stroke-dasharray="4 4"/>'
    + sparkle(22, 36, 4, "#fff") + sparkle(108, 28, 3, "#FFF3D6") + sparkle(110, 70, 2.4, "#fff"))

# 2. Москино Молодёжный — билетный терминал
I["cin-moskino-molodezhny"] = ("#DAF7D2", "#3E9E57",
    "билетный терминал с сенсорным экраном и щелью для билетов",
    "малыш на цыпочках жмёт кнопку на экране, а из щели терминала выползает билетик-язычок",
    f'<rect x="54" y="18" width="50" height="98" rx="8" fill="#F4F6FA" {W(3.2)}/>'
    + f'<rect x="60" y="26" width="38" height="34" rx="4" fill="#2C3A66" {W(2.6)}/>'
    + f'<path d="M74 36 L86 43 L74 50Z" fill="#7CE0A0"/>'
    + f(79, 70, d=8, k=0.62)
    + f'<rect x="64" y="86" width="30" height="5" rx="2.5" fill="#3B3355"/>'
    + f'<path d="M68 89 H90 V108 L86 105 L82 108 L78 105 L74 108 L70 105 L68 108Z" fill="#FFD95A" {W(2.4)}/>'
    + f'<path d="M73 96 H85" stroke="#C99A1E" stroke-width="2"/>'
    + f'<path d="M30 118 V92 Q30 82 38 82 Q46 82 46 92 V118" fill="#3E7BD6" {W(3)}/>'
    + f'<path d="M42 86 Q52 66 62 48" fill="none" stroke="#FFD9B8" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M42 86 Q52 66 62 48" fill="none" {W(2.6)} stroke-opacity=".0"/>'
    + f'<circle cx="62" cy="47" r="4.5" fill="#FFD9B8" {W(2.4)}/>'
    + kid(36, 70, k=0.95, hair="#2E2A2A")
    + f'<path d="M30 122 h-6 M46 122 h6" {W(3)}/>'
    + sparkle(66, 42, 3, "#fff") + sparkle(18, 40, 3, "#fff"))

# 3. Москино Тула — световой короб с афишей мультфильма
bulbs = "".join(f'<circle cx="{x}" cy="{y}" r="3.4" fill="#FFE780" {W(1.6)}/>'
                for x, y in [(22, 22), (40, 22), (58, 22), (76, 22), (94, 22), (106, 22), (106, 42), (106, 62),
                             (106, 82), (106, 100), (88, 100), (70, 100), (52, 100), (34, 100), (22, 100), (22, 80),
                             (22, 60), (22, 40)])
I["cin-moskino-tula"] = ("#ECE3FF", "#6B4FC8",
    "световой короб с афишей мультфильма в рамке из лампочек",
    "лампочки по краю мигают, а нарисованный на афише кит выпускает фонтан прямо из рамки",
    f'<rect x="22" y="22" width="84" height="78" rx="6" fill="#B44A7C" {W(3.2)}/>'
    + f'<rect x="32" y="32" width="64" height="58" rx="3" fill="#BFE9FF" {W(2.6)}/>'
    + f'<path d="M32 74 Q48 68 64 74 T96 74 V90 H32Z" fill="#4BA3E3"/>'
    + f'<path d="M40 74 Q42 56 62 56 Q84 56 86 70 Q90 64 94 62 Q92 72 88 76 Q76 84 56 82 Q42 82 40 74Z" '
      f'fill="#5E7BE0" {W(2.6)}/>'
    + eye(52, 66, 0.6) + f'<path d="M46 74 Q52 78 60 74" fill="none" {W(2)}/>'
    + f'<path d="M58 54 Q56 34 50 12 M58 54 Q62 30 70 12 M58 54 Q58 30 60 8" fill="none" stroke="#9FDCFF" '
      f'stroke-width="3.4" stroke-linecap="round"/>'
    + bulbs
    + f'<rect x="56" y="100" width="16" height="22" fill="#7C5AA6" {W(2.6)}/>'
    + sparkle(14, 60, 3, "#fff") + sparkle(116, 40, 2.6, "#FFE780"))

# 4. Киномакс-Титан — малыш задрал голову перед огромным экраном
I["cin-kinomax-titan"] = ("#2B3B7A", "#0E1636",
    "малыш-зритель в полосатой кофточке, задравший голову",
    "сидит в первом ряду перед огромным, во весь круг, экраном, с которого улыбается гигантский динозаврик",
    f'<path d="M4 8 Q64 -2 124 8 V82 Q64 74 4 82Z" fill="#CDEBFF" {W(3)}/>'
    + f'<path d="M4 60 Q34 50 64 58 T124 56 V82 Q64 74 4 82Z" fill="#7FC6F2"/>'
    + f'<path d="M30 80 V40 Q30 16 60 16 Q92 16 96 38 L112 40 Q118 50 108 56 L96 58 V80Z" fill="#6CCB5F" {W(2.8)}/>'
    + "".join(f'<path d="M{x} 17 l5 -9 l5 9" fill="#FFB33E" {W(2)}/>' for x in (40, 52, 64))
    + f(62, 38, d=10, k=0.9)
    + f'<path d="M0 90 Q64 82 128 90 V128 H0Z" fill="#3A2E6E"/>'
    + f'<path d="M48 128 V108 Q48 94 64 94 Q80 94 80 108 V128" fill="#FF7A59" {W(3)}/>'
    + f'<path d="M50 106 H78 M49 116 H79" stroke="#FFE1A8" stroke-width="3"/>'
    + f'<circle cx="64" cy="84" r="13" fill="#FFD9B8" {W(2.8)}/>'
    + f'<path d="M51 82 Q52 68 64 68 Q76 68 77 82 Q70 74 64 76 Q58 74 51 82Z" fill="#E8B84A" {W(2.4)}/>'
    + eye(59, 84, 0.5) + eye(69, 84, 0.5)
    + f'<ellipse cx="64" cy="92" rx="3" ry="3.6" fill="#3B3355"/>'
    + sparkle(104, 18, 3, "#fff"))

# 5. Каро 5 Иридиум — фонарик капельдинера светит на свободное место
I["cin-karo-iridium"] = ("#F2B8D6", "#6A2458",
    "карманный фонарик капельдинера с глазками",
    "светит жёлтым лучом в тёмном зале и показывает свободное место с номерком «7»",
    f'<path d="M58 64 L6 112 L44 128 Z" fill="#FFF1A6" opacity=".55"/>'
    + f'<path d="M14 104 H58 V128 H14Z" fill="#9C2B4E" {W(2.8)}/>'
    + f'<rect x="18" y="96" width="36" height="12" rx="5" fill="#C9406A" {W(2.6)}/>'
    + f'<rect x="28" y="110" width="16" height="9" rx="2" fill="#FFE780" {W(2)}/>'
    + f'<text x="36" y="118" font-family="Arial" font-weight="bold" font-size="8.5" text-anchor="middle" fill="#3B3355">7</text>'
    + f'<g transform="rotate(-40 82 50)">'
    + f'<rect x="66" y="30" width="32" height="56" rx="10" fill="#4A6FE0" {W(3.2)}/>'
    + f'<path d="M62 30 H102 L96 18 H68Z" fill="#C7D3F5" {W(3)}/>'
    + f'<ellipse cx="82" cy="18" rx="14" ry="3" fill="#FFF7B0" {W(2.2)}/>'
    + f'<circle cx="82" cy="72" r="5" fill="#FFD25A" {W(2.2)}/>'
    + face(82, 48, d=7, k=0.62) + '</g>'
    + sparkle(104, 100, 3, "#FFE2F0") + sparkle(98, 20, 2.4, "#fff") + sparkle(20, 40, 2.4, "#fff"))

# 6. Каро 4 Высота — малыш на подушке-бустере выше всех
I["cin-karo-vysota"] = ("#FFF5C8", "#EFA92A",
    "толстая детская подушка-бустер для кинозала",
    "малыш сидит на высокой стопке подушек-бустеров выше всех в ряду и машет ручкой",
    f'<path d="M10 4 Q64 -4 118 4 V30 Q64 24 10 30Z" fill="#FFFDF0" opacity=".85" {W(2.6)}/>'
    + f'<path d="M36 128 V92 Q36 84 44 84 H84 Q92 84 92 92 V128Z" fill="#2E58B8" {W(3)}/>'
    + f'<path d="M28 100 H40 V128 H28Z M88 100 H100 V128 H88Z" fill="#24449A" {W(2.6)}/>'
    + f'<rect x="34" y="66" width="60" height="24" rx="10" fill="#FF8A5B" {W(3)}/>'
    + f'<path d="M50 68 V88 M64 68 V88 M78 68 V88" stroke="#E2663A" stroke-width="2"/>'
    + f(64, 80, d=11, k=0.55)
    + f'<path d="M48 68 V54 Q48 46 56 46 H72 Q80 46 80 54 V68Z" fill="#B565D8" {W(3)}/>'
    + f'<path d="M78 54 Q92 44 96 30" fill="none" stroke="#FFD9B8" stroke-width="7" stroke-linecap="round"/>'
    + f'<circle cx="96" cy="28" r="5" fill="#FFD9B8" {W(2.4)}/>'
    + kid(64, 36, k=0.95, hair="#C0542A")
    + f'<circle cx="12" cy="104" r="12" fill="#5A3A2A" {W(2.8)}/><circle cx="116" cy="104" r="12" fill="#E8B84A" {W(2.8)}/>'
    + f'<path d="M0 118 Q12 112 24 118 V128 H0Z M104 118 Q116 112 128 118 V128 H104Z" fill="#4FB0A5" {W(2.4)}/>'
    + sparkle(106, 52, 3, "#fff") + sparkle(22, 52, 2.6, "#fff"))

# 7. Юбилейный (Раменское) — круг обратного отсчёта перед фильмом
I["cin-yubileyny-ramenskoe"] = ("#D4F4F0", "#24877C",
    "круг обратного отсчёта перед фильмом с большой цифрой «3» и перекрестьем",
    "стрелка-луч обегает круг, а цифра «3» подпрыгивает и считает вслух",
    f'<circle cx="64" cy="62" r="46" fill="#F7F3E6" {W(3.4)}/>'
    + f'<path d="M64 62 L64 16 A46 46 0 0 1 108 50Z" fill="#B7E3DC"/>'
    + f'<circle cx="64" cy="62" r="34" fill="none" {W(2.6)}/>'
    + f'<path d="M64 12 V112 M14 62 H114" {W(2)} stroke-dasharray="5 4"/>'
    + f'<path d="M64 62 L108 50" {W(3.2)}/>'
    + f'<path d="M50 40 Q52 30 64 30 Q78 30 78 41 Q78 52 66 54 Q80 56 80 68 Q80 82 64 82 Q50 82 48 72" '
      f'fill="none" stroke="#E2563C" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>'
    + f(64, 98, d=7, k=0.55)
    + f'<path d="M22 22 l-6 -6 M106 22 l6 -6 M22 104 l-6 6 M106 104 l6 6" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    + sparkle(20, 66, 2.6, "#fff"))

# 8. Планета (Дмитров) — красная ковровая дорожка
I["cin-planeta-dmitrov"] = ("#E7F1D6", "#6F8E44",
    "красная ковровая дорожка со столбиками-ограждениями",
    "по дорожке к дверям кинотеатра шагает малыш-звезда в тёмных очках, вокруг вспышки",
    f'<path d="M50 50 H78 L112 128 H16Z" fill="#D9343F" {W(3)}/>'
    + f'<path d="M58 50 L44 128 M70 50 L84 128" stroke="#B5212C" stroke-width="2"/>'
    + f'<rect x="44" y="20" width="40" height="32" rx="3" fill="#7A4A2A" {W(3)}/>'
    + f'<path d="M64 20 V52" {W(2.4)}/>'
    + f'<circle cx="60" cy="38" r="2" fill="#FFD25A"/><circle cx="68" cy="38" r="2" fill="#FFD25A"/>'
    + "".join(f'<path d="M{x} {y} V{y-22}" {W(3)}/><circle cx="{x}" cy="{y-24}" r="4" fill="#FFD25A" {W(2.2)}/>'
              f'<rect x="{x-6}" y="{y-2}" width="12" height="4" rx="2" fill="#3B3355"/>'
              for x, y in [(18, 112), (110, 112)])
    + f'<path d="M18 92 Q40 104 52 92 M110 92 Q88 104 76 92" fill="none" stroke="#B5212C" stroke-width="4"/>'
    + f'<path d="M56 116 V96 Q56 88 64 88 Q72 88 72 96 V116" fill="#FFD25A" {W(2.8)}/>'
    + f'<path d="M56 116 L54 124 M72 116 L76 122" {W(3.4)}/>'
    + kid(64, 76, k=0.95, hair="#3B2A20")
    + f'<path d="M53 76 H75" {W(2.4)}/><rect x="53" y="73" width="9" height="6" rx="2" fill="#1E1E2E"/>'
      f'<rect x="66" y="73" width="9" height="6" rx="2" fill="#1E1E2E"/>'
    + sparkle(22, 34, 6, "#fff") + sparkle(106, 30, 5, "#fff") + sparkle(98, 62, 3, "#FFF3B0"))

# 9. Юность (Ступино) — световое табло «ТИХО»
I["cin-yunost-stupino"] = ("#FCE3CB", "#B95A30",
    "световое табло «ТИХО» над дверью кинозала",
    "табло горит красным, а малыш у двери прикладывает пальчик к губам",
    f'<rect x="30" y="54" width="68" height="80" rx="4" fill="#6E3B2A" {W(3.2)}/>'
    + f'<rect x="38" y="62" width="52" height="66" rx="3" fill="#8E5137" {W(2.4)}/>'
    + f'<circle cx="82" cy="96" r="3" fill="#FFD25A" {W(1.6)}/>'
    + f'<rect x="20" y="14" width="88" height="32" rx="7" fill="#3B2233" {W(3.2)}/>'
    + f'<rect x="26" y="20" width="76" height="20" rx="4" fill="#FF4A55"/>'
    + f'<text x="64" y="36" font-family="Arial" font-weight="bold" font-size="17" text-anchor="middle" fill="#FFF3E0">ТИХО</text>'
    + f'<path d="M16 10 l-6 -4 M112 10 l6 -4 M64 6 v-6" stroke="#FFB0A6" stroke-width="3" stroke-linecap="round"/>'
    + f'<path d="M50 128 V108 Q50 98 62 98 Q74 98 74 108 V128" fill="#4FB0A5" {W(3)}/>'
    + kid(62, 84, k=1.05, hair="#E2B33E")
    + f'<path d="M63 94 V82" stroke="#FFD9B8" stroke-width="5" stroke-linecap="round"/>'
    + f'<circle cx="63" cy="92" r="3" fill="#FFD9B8"/>'
    + sparkle(112, 70, 3, "#fff"))

# 10. Кванториум Королёв — штангенциркуль измеряет шестерёнку
import math
teeth = []
for i in range(10):
    a0 = i * math.pi / 5
    for da, r in [(-0.16, 15), (-0.1, 20), (0.1, 20), (0.16, 15)]:
        teeth.append((86 + r * math.cos(a0 + da), 88 + r * math.sin(a0 + da)))
gear_d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in teeth) + "Z"
I["kvantorium-korolev"] = ("#DCE6FF", "#4A5FC4",
    "серебристый штангенциркуль с глазками на подвижной рамке",
    "измеряет оранжевую шестерёнку, только что напечатанную на 3D-принтере юного инженера",
    f'<rect x="12" y="24" width="104" height="16" rx="3" fill="#D7DDE8" {W(3)}/>'
    + "".join(f'<path d="M{x} 24 V{30 if x % 10 else 33}" stroke="#3B3355" stroke-width="1.4"/>'
              for x in range(18, 112, 5))
    + f'<path d="M18 40 V96 L30 92 V40Z" fill="#C3CAD8" {W(3)}/>'
    + f'<path d="M58 18 H82 V60 H72 V96 L60 92 V60 H58Z" fill="#AEB8CC" {W(3)}/>'
    + f(70, 48, d=6, k=0.55)
    + f'<path d="{gear_d}" fill="#FF8A3D" {W(2.6)}/>'
    + f'<circle cx="86" cy="88" r="6" fill="#DCE6FF" {W(2.4)}/>'
    + f'<path d="M30 88 H60" stroke="#FF5A6E" stroke-width="2" stroke-dasharray="3 3"/>'
    + sparkle(104, 112, 3, "#fff") + sparkle(20, 112, 2.6, "#fff"))

# 11. Апрелевка — иголка-паровозик едет по канавке пластинки
I["aprelevka-records-museum"] = ("#C8D2F4", "#2D3878",
    "иголка звукоснимателя в образе маленького паровозика с трубой-нотой",
    "катится по огромной спиральной канавке, как по рельсам, а из трубы вылетают нотки",
    f'<path d="M-10 128 A120 120 0 0 1 150 128 V140 H-10Z" fill="#1E1C30" {W(3)}/>'
    + "".join(f'<path d="M{64-r} 136 A{r} {r} 0 0 1 {64+r} 136" fill="none" stroke="#4A4670" stroke-width="2"/>'
              for r in range(40, 118, 10))
    + f'<path d="M{64-80} 136 A80 80 0 0 1 {64+80} 136" fill="none" stroke="#9AA4E8" stroke-width="2.4"/>'
    + f'<g transform="rotate(-12 52 62)">'
    + f'<rect x="30" y="50" width="44" height="22" rx="5" fill="#E8483F" {W(3)}/>'
    + f'<rect x="58" y="38" width="18" height="20" rx="3" fill="#FFD25A" {W(2.8)}/>'
    + f'<rect x="36" y="40" width="8" height="12" fill="#3B3355" {W(2)}/>'
    + f'<circle cx="40" cy="76" r="6" fill="#3B3355"/><circle cx="64" cy="76" r="6" fill="#3B3355"/>'
    + f'<path d="M64 82 L68 92" stroke="#D7DDE8" stroke-width="3" stroke-linecap="round"/>'
    + face(50, 61, d=6, k=0.55) + '</g>'
    + f'<path d="M40 30 V14 l8 -3 v14" fill="none" stroke="#FFE780" stroke-width="2.6" stroke-linecap="round"/>'
    + f'<circle cx="37" cy="30" r="3.4" fill="#FFE780"/><circle cx="45" cy="26" r="3.4" fill="#FFE780"/>'
    + f'<path d="M70 22 V8" stroke="#A8F0D6" stroke-width="2.6" stroke-linecap="round"/><circle cx="67" cy="22" r="3.4" fill="#A8F0D6"/>'
    + f'<path d="M94 34 V20 l7 -2 v12" fill="none" stroke="#FFB0D0" stroke-width="2.6" stroke-linecap="round"/>'
    + f'<circle cx="91" cy="34" r="3.2" fill="#FFB0D0"/><circle cx="98" cy="30" r="3.2" fill="#FFB0D0"/>'
    + sparkle(110, 60, 3, "#fff") + sparkle(16, 50, 2.4, "#fff"))

# 12. Усадьба Фряново — кружевной зонтик барышни гуляет у пруда
lace = "".join(f'<circle cx="{64 + 44*math.cos(a):.1f}" cy="{50 + 18*math.sin(a) + 2:.1f}" r="4" fill="#fff" {W(1.6)}/>'
               for a in [math.pi + i * math.pi / 8 for i in range(9)])
I["fryanovo-estate"] = ("#FFE9D6", "#8DBF7A",
    "белый кружевной зонтик барышни с бантом на ручке",
    "сам прогуливается по аллее у пруда старинной усадьбы, за ним жёлтый дом с колоннами",
    f'<rect x="76" y="58" width="44" height="30" fill="#F6D36B" {W(2.6)}/>'
    + f'<path d="M72 58 L98 44 L124 58Z" fill="#E9F2F7" {W(2.6)}/>'
    + "".join(f'<path d="M{x} 62 V88" stroke="#fff" stroke-width="3"/>' for x in (84, 92, 100, 108))
    + f'<path d="M0 96 Q64 84 128 96 V128 H0Z" fill="#7CC36A"/>'
    + f'<ellipse cx="30" cy="108" rx="26" ry="8" fill="#7FC6F2" {W(2.4)}/>'
    + f'<path d="M64 52 Q64 30 64 30" {W(3)}/>'
    + f'<path d="M20 54 Q24 22 64 20 Q104 22 108 54 Q98 46 86 54 Q76 46 64 54 Q52 46 42 54 Q30 46 20 54Z" '
      f'fill="#FFFFFF" {W(3)}/>'
    + lace
    + f'<path d="M36 50 Q40 32 64 28 M64 28 Q88 32 92 50 M64 28 V54" fill="none" stroke="#E6D4E8" stroke-width="2"/>'
    + f'<path d="M64 54 V104 Q64 112 56 112" fill="none" stroke="#8C5A3C" stroke-width="4" stroke-linecap="round"/>'
    + f'<path d="M64 70 l-10 -6 v12Z M64 70 l10 -6 v12Z" fill="#F08AB8" {W(2)}/>'
    + f(64, 38, d=8, k=0.62)
    + f'<path d="M58 118 q4 -4 8 0 M72 116 q4 -4 8 0" fill="none" stroke="#5E9E52" stroke-width="2.4" stroke-linecap="round"/>'
    + sparkle(22, 30, 3, "#fff"))

# 13. Пушкинский краеведческий — резной наличник старой дачи
I["pushkino-kraeved"] = ("#D9EEFF", "#5D8FC7",
    "резной деревянный наличник с кокошником-гребешком",
    "в окошке старинной пушкинской дачи горит тёплый свет, а с подоконника выглядывает рыжий кот",
    f'<rect x="0" y="0" width="128" height="128" fill="#8FB26A" opacity=".0"/>'
    + "".join(f'<rect x="0" y="{y}" width="128" height="12" fill="{c}" stroke="#7A4A2A" stroke-width="1.6"/>'
              for y, c in zip(range(0, 128, 12), ["#C98A4E", "#B97A42"] * 6))
    + f'<path d="M24 34 Q64 0 104 34 L96 40 Q64 14 32 40Z" fill="#F7F3E6" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#7BC0E8" {W(1.4)}/>' for x, y in [(44, 26), (64, 18), (84, 26)])
    + f'<rect x="34" y="40" width="60" height="58" fill="#FFE07A" {W(3)}/>'
    + f'<path d="M64 40 V98 M34 66 H94" {W(3)}/>'
    + f'<rect x="28" y="38" width="8" height="64" fill="#F7F3E6" {W(2.6)}/>'
    + f'<rect x="92" y="38" width="8" height="64" fill="#F7F3E6" {W(2.6)}/>'
    + f'<path d="M24 98 H104 L98 112 H30Z" fill="#F7F3E6" {W(3)}/>'
    + "".join(f'<path d="M{x} 112 l4 6 l4 -6" fill="#F7F3E6" {W(1.8)}/>' for x in range(34, 96, 10))
    + f'<path d="M66 98 Q66 78 80 78 Q94 78 94 98Z" fill="#F08C3A" {W(2.6)}/>'
    + f'<path d="M70 82 L72 70 L78 78 M90 82 L88 70 L82 78" fill="#F08C3A" {W(2.2)}/>'
    + face(80, 88, d=5, k=0.45)
    + f'<path d="M94 92 Q104 86 100 74" fill="none" stroke="#F08C3A" stroke-width="5" stroke-linecap="round"/>'
    + sparkle(48, 52, 3, "#fff"))

# 14. ДТДиМ «Восточный» — напёрсток бежит по пяльцам
I["dtdim-vostochny"] = ("#FFE4EC", "#E0678F",
    "серебряный напёрсток с ямочками",
    "бежит по натянутой ткани в деревянных пяльцах, а за ним тянется стежок, вышивающий цветок",
    f'<circle cx="64" cy="70" r="46" fill="#C98A4E" {W(3.2)}/>'
    + f'<circle cx="64" cy="70" r="40" fill="#FFF8EE" {W(2.6)}/>'
    + f'<rect x="58" y="18" width="12" height="10" rx="2" fill="#B97A42" {W(2.4)}/>'
    + f'<path d="M30 92 Q40 70 52 84 Q60 94 66 80" fill="none" stroke="#3E9E57" stroke-width="3" stroke-dasharray="5 3"/>'
    + "".join(f'<ellipse cx="{36 + 8*math.cos(a):.1f}" cy="{66 + 8*math.sin(a):.1f}" rx="5" ry="3.4" '
              f'transform="rotate({math.degrees(a):.0f} {36 + 8*math.cos(a):.1f} {66 + 8*math.sin(a):.1f})" fill="#FF7FA8" {W(1.6)}/>'
              for a in [i * math.pi / 3 for i in range(6)])
    + f'<circle cx="36" cy="66" r="4" fill="#FFD25A" {W(1.6)}/>'
    + f'<path d="M66 82 Q74 92 70 98" fill="none" stroke="#3E9E57" stroke-width="2.4"/>'
    + f'<path d="M64 80 L68 46 Q70 34 82 34 Q94 34 96 46 L100 80Z" fill="#C9D1DE" {W(3)}/>'
    + f'<ellipse cx="82" cy="36" rx="13" ry="4" fill="#E6EBF3" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1.5" fill="#8A93A6"/>' for x, y in
              [(74, 46), (82, 44), (90, 46), (72, 54), (92, 54)])
    + face(82, 64, d=6, k=0.55)
    + f'<path d="M98 92 l8 4 M96 100 l8 6" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>'
    + sparkle(104, 30, 3, "#fff"))

# 15. ЦДТ «Замоскворечье» — баночка-непроливайка с радужной водой
I["cdt-zamoskvorechye"] = ("#E0F7FF", "#3FA6C9",
    "пластмассовая баночка-непроливайка с глазками",
    "в неё макнули кисточку, и вода внутри закружилась радугой, а капли разлетелись по столу",
    f'<path d="M0 100 H128 V128 H0Z" fill="#F4E3C3" {W(3)}/>'
    + f'<path d="M30 54 Q30 42 64 42 Q98 42 98 54 V102 Q98 112 64 112 Q30 112 30 102Z" fill="#B9E8FF" '
      f'fill-opacity=".85" {W(3.2)}/>'
    + f'<path d="M32 70 Q48 62 64 70 T96 70 V102 Q96 110 64 110 Q32 110 32 102Z" fill="#FF8AB0"/>'
    + f'<path d="M32 82 Q48 74 64 82 T96 82 V102 Q96 110 64 110 Q32 110 32 102Z" fill="#FFD25A"/>'
    + f'<path d="M32 94 Q48 88 64 94 T96 94 V102 Q96 110 64 110 Q32 110 32 102Z" fill="#7CD6A0"/>'
    + f'<ellipse cx="64" cy="46" rx="30" ry="8" fill="#5FB8E8" {W(3)}/>'
    + f'<ellipse cx="64" cy="46" rx="12" ry="3.5" fill="#2C6E9A"/>'
    + f(64, 84, d=10, k=0.7)
    + f'<path d="M84 4 L66 44" stroke="#C98A4E" stroke-width="6" stroke-linecap="round"/>'
    + f'<path d="M68 38 L64 48 L72 44Z" fill="#3B3355"/>'
    + f'<circle cx="16" cy="96" r="4" fill="#FF8AB0"/><circle cx="110" cy="92" r="4.4" fill="#7CD6A0"/>'
      f'<circle cx="114" cy="72" r="3" fill="#FFD25A"/><circle cx="20" cy="74" r="3" fill="#A88BF0"/>'
    + sparkle(104, 30, 3.4, "#fff"))

# 16. ЦРТДЮ «Сокол» — бумажная гирлянда человечков из ножниц
def paperman(x, y, c):
    return (f'<path d="M{x} {y} m-4 0 a4 4 0 1 1 8 0 a4 4 0 1 1 -8 0 M{x-9} {y+8} H{x+9} L{x+5} {y+12} V{y+24} '
            f'L{x+2} {y+24} L{x} {y+16} L{x-2} {y+24} L{x-5} {y+24} V{y+12}Z" fill="{c}" {W(1.8)}/>')
I["crtdu-sokol"] = ("#FFF0C9", "#E5A13A",
    "бумажная гирлянда из человечков, держащихся за руки",
    "растягивается дугой через весь круг прямо из раскрытых красных ножниц",
    "".join(paperman(x, 52 + 0.012 * (x - 64) ** 2 - 4, c) for x, c in
            zip(range(14, 116, 17), ["#FF8AB0", "#7CD6A0", "#7FC6F2", "#FFE780", "#C9A3F5", "#FF9F6B", "#9FE0D0"]))
    + f(64, 64, d=4, k=0.36)
    + f'<g transform="rotate(25 92 98)">'
    + f'<circle cx="78" cy="110" r="8" fill="none" stroke="#E8483F" stroke-width="5"/>'
    + f'<circle cx="98" cy="114" r="8" fill="none" stroke="#E8483F" stroke-width="5"/>'
    + f'<path d="M82 102 L104 70 M94 106 L92 68" stroke="#AEB8CC" stroke-width="5" stroke-linecap="round"/>'
    + f'<circle cx="90" cy="96" r="2.4" fill="#3B3355"/>' + '</g>'
    + sparkle(22, 26, 3.4, "#fff") + sparkle(106, 24, 2.6, "#fff") + sparkle(20, 104, 2.4, "#fff"))

# 17. «На Стопани» — лобзик выпиливает кораблик из фанеры
I["dtdim-na-stopani"] = ("#E7F6E9", "#4E9B6E",
    "лобзик с синей ручкой и тонкой пилкой",
    "выпиливает из светлой фанеры кораблик, а вокруг летят опилки-звёздочки",
    f'<path d="M44 30 H100 V92 H44" fill="none" stroke="#3B3355" stroke-width="21" stroke-linejoin="round"/>'
    + f'<path d="M44 30 H100 V92 H44" fill="none" stroke="#E8483F" stroke-width="15" stroke-linejoin="round"/>'
    + f'<path d="M100 92 L106 122" stroke="#3B3355" stroke-width="16" stroke-linecap="round"/>'
    + f'<path d="M100 92 L106 122" stroke="#3E7BD6" stroke-width="10" stroke-linecap="round"/>'
    + f'<rect x="-4" y="66" width="86" height="40" rx="3" fill="#F2D3A0" {W(3)}/>'
    + "".join(f'<path d="M{x} {y} q12 4 24 0" fill="none" stroke="#D9B07A" stroke-width="1.8"/>'
              for x, y in [(2, 76), (34, 86), (6, 96), (52, 74)])
    + f'<path d="M10 88 H36 L32 96 H14Z M22 88 V72 L34 86Z" fill="none" stroke="#8C5A3C" stroke-width="2.2" stroke-dasharray="4 3"/>'
    + f'<path d="M44 38 V66" stroke="#3B3355" stroke-width="2.6"/>'
    + f'<path d="M44 66 V80" stroke="#3B3355" stroke-width="2.4" stroke-dasharray="2 2"/>'
    + face(74, 28, d=6, k=0.42)
    + sparkle(30, 58, 3, "#FFE7B0") + sparkle(56, 60, 2.6, "#FFE7B0") + sparkle(40, 112, 2.4, "#FFE7B0")
    + sparkle(18, 28, 3.4, "#fff"))

# 18. ЦДЮТ «Бибирево» — бусины-смайлики на шнурке
beads = [(28, 34, "#FF6F91"), (40, 46, "#FFD25A"), (50, 58, "#7CD6A0"), (58, 71, "#7FC6F2"), (64, 85, "#C9A3F5")]
I["cdyut-bibirevo"] = ("#F4E6FF", "#9B6BD6",
    "разноцветные деревянные бусины-смайлики",
    "малышка нанизывает их на розовый шнурок, и каждая бусина на нитке улыбается",
    f'<path d="M18 22 Q40 50 64 92 Q70 104 70 118" fill="none" stroke="#FF8AB0" stroke-width="3"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="9" fill="{c}" {W(2.6)}/>' + face(x, y - 1, d=3.4, k=0.32, blush=False)
              for x, y, c in beads)
    + f'<path d="M70 118 L72 128" stroke="#FF8AB0" stroke-width="3"/>'
    + f'<path d="M84 128 V112 Q84 100 96 100 Q108 100 108 112 V128" fill="#FF9F6B" {W(3)}/>'
    + f'<path d="M86 108 Q76 104 72 112" fill="none" stroke="#FFD9B8" stroke-width="6" stroke-linecap="round"/>'
    + kid(98, 86, k=1.0, hair="#7A3B1E")
    + f'<circle cx="86" cy="72" r="5" fill="#7A3B1E" {W(2)}/><circle cx="110" cy="72" r="5" fill="#7A3B1E" {W(2)}/>'
    + f'<circle cx="104" cy="40" r="8" fill="#FFB33E" {W(2.4)}/><circle cx="116" cy="54" r="6" fill="#5FD0A3" {W(2.2)}/>'
    + sparkle(30, 100, 3, "#fff") + sparkle(84, 22, 3.4, "#fff"))

# 19. «Остров» (Маркос Молл) — закрученная горка-труба
I["ostrov-markos-mall"] = ("#D6F6FF", "#2FA3C8",
    "закрученная спиралью жёлтая горка-труба",
    "малыш с визгом вылетает из её конца прямо в сухой бассейн с разноцветными шариками",
    f'<path d="M24 14 V112" stroke="#E8483F" stroke-width="6"/>'
    + f'<path d="M24 14 V112" {W(2.4)}/>'
    + f'<path d="M30 24 Q98 18 96 40 Q94 58 36 52 Q20 50 22 66 Q24 82 88 78" fill="none" stroke="#3B3355" '
      f'stroke-width="23" stroke-linecap="round"/>'
    + f'<path d="M30 24 Q98 18 96 40 Q94 58 36 52 Q20 50 22 66 Q24 82 88 78" fill="none" stroke="#FFD25A" '
      f'stroke-width="17" stroke-linecap="round"/>'
    + f'<path d="M30 24 Q98 18 96 40" fill="none" stroke="#FFF1A8" stroke-width="4" stroke-linecap="round"/>'
    + "".join(f'<path d="M{x} {y-10} L{x+dx} {y+10}" stroke="#E0A92E" stroke-width="2.4"/>' for x, y, dx in
              [(48, 22, 0), (70, 22, -2), (90, 30, -10), (70, 52, 2), (46, 52, 2), (30, 70, 10), (52, 76, 0), (72, 78, -2)])
    + f'<path d="M0 104 Q64 92 128 104 V128 H0Z" fill="#fff" opacity=".5"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="6.5" fill="{c}" {W(2)}/>' for x, y, c in
            [(10, 110, "#FF6F91"), (24, 118, "#FFD25A"), (40, 110, "#7CD6A0"), (56, 120, "#7FC6F2"),
             (72, 112, "#C9A3F5"), (90, 120, "#FF6F91"), (108, 110, "#FFD25A"), (122, 120, "#7CD6A0")])
    + kid(104, 86, k=0.95, hair="#3B2A20")
    + f'<path d="M92 76 l-8 -8 M116 76 l8 -8" stroke="#FFD9B8" stroke-width="5" stroke-linecap="round"/>'
    + sparkle(112, 30, 3.4, "#fff") + sparkle(60, 96, 2.4, "#fff"))

# 20. «Зов джунглей» — малыш-исследователь в пробковом шлеме
I["zov-dzhungley-balashikha"] = ("#D8F7B6", "#2E7D3E",
    "малыш-исследователь в пробковом шлеме",
    "раздвигает ладошками огромные листья джунглей и с восторгом выглядывает из зарослей",
    f'<path d="M-6 40 Q20 30 30 56 Q16 70 -6 64Z" fill="#3E9E57" {W(2.6)}/>'
    + f'<path d="M134 34 Q106 26 98 52 Q112 68 134 62Z" fill="#3E9E57" {W(2.6)}/>'
    + f'<path d="M64 130 V98" stroke="#5B3A1E" stroke-width="0"/>'
    + kid(64, 68, k=1.55, hair="#6B3F23")
    + f'<path d="M30 54 Q32 22 64 20 Q96 22 98 54Z" fill="#E9D3A0" {W(3.2)}/>'
    + f'<ellipse cx="64" cy="54" rx="42" ry="7" fill="#D9BE84" {W(3)}/>'
    + f'<path d="M34 46 H94" stroke="#7A4A2A" stroke-width="4"/>'
    + f'<path d="M-4 86 Q24 70 44 92 Q30 112 -4 112Z" fill="#5CC06A" {W(2.8)}/>'
    + f'<path d="M132 84 Q104 70 84 92 Q98 112 132 112Z" fill="#5CC06A" {W(2.8)}/>'
    + f'<path d="M4 98 Q22 94 40 92 M124 98 Q106 94 88 92" fill="none" stroke="#2E7D3E" stroke-width="2"/>'
    + f'<circle cx="40" cy="92" r="6" fill="#FFD9B8" {W(2.4)}/><circle cx="88" cy="92" r="6" fill="#FFD9B8" {W(2.4)}/>'
    + f'<path d="M22 8 Q28 30 18 46 M110 4 Q102 26 114 40" fill="none" stroke="#7A5A2A" stroke-width="3"/>'
    + f'<path d="M-4 120 Q30 108 64 122 Q98 108 132 120 V132 H-4Z" fill="#2E7D3E"/>'
    + sparkle(64, 10, 3, "#fff"))

# 21. Quest Runners — каменная маска-идол майя
I["questrunners-podolsk"] = ("#F4D58A", "#9A5A22",
    "каменная маска-идол майя с бирюзовыми глазами и головным убором из перьев",
    "охраняет вход в тайник: глаза-самоцветы светятся, а из-под подбородка выглядывает золотой ключ",
    "".join(f'<rect x="{x}" y="{y}" width="30" height="14" fill="#C9944E" stroke="#8A5A2A" stroke-width="1.6"/>'
            for y in range(0, 128, 14) for x in range(-15 if (y // 14) % 2 else 0, 128, 30))
    + "".join(f'<path d="M{64 + dx} 34 Q{64 + dx*1.6} 10 {64 + dx*1.2} -2" fill="none" stroke="{c}" '
              f'stroke-width="9" stroke-linecap="round"/>' for dx, c in
              [(-24, "#2FB5A3"), (-12, "#E8483F"), (0, "#FFD25A"), (12, "#E8483F"), (24, "#2FB5A3")])
    + f'<path d="M30 36 H98 L92 100 Q64 112 36 100Z" fill="#9AA3A8" {W(3.2)}/>'
    + f'<path d="M30 36 H98 V46 H30Z" fill="#7E878C" {W(2.6)}/>'
    + f'<path d="M36 52 H58 V64 H36Z M70 52 H92 V64 H70Z" fill="#5E676C" {W(2.4)}/>'
    + f'<ellipse cx="47" cy="58" rx="7" ry="4.6" fill="#4FF0D8" {W(2)}/><ellipse cx="81" cy="58" rx="7" ry="4.6" fill="#4FF0D8" {W(2)}/>'
    + f'<circle cx="47" cy="58" r="2" fill="#1E3B3A"/><circle cx="81" cy="58" r="2" fill="#1E3B3A"/>'
    + f'<path d="M60 64 V78 H68 V64" fill="#AEB6BA" {W(2.4)}/>'
    + f'<path d="M46 86 Q64 96 82 86" fill="none" {W(3)}/>'
    + f'<ellipse cx="40" cy="78" rx="5" ry="3" fill="#FF7FA8" opacity=".55"/><ellipse cx="88" cy="78" rx="5" ry="3" fill="#FF7FA8" opacity=".55"/>'
    + f'<circle cx="76" cy="114" r="7" fill="none" stroke="#FFD25A" stroke-width="4"/>'
    + f'<path d="M83 114 H104 M98 114 V120 M103 114 V119" stroke="#FFD25A" stroke-width="4" stroke-linecap="round"/>'
    + f'<path d="M83 114 H104" fill="none" stroke="#3B3355" stroke-width="0"/>'
    + sparkle(47, 54, 2, "#fff") + sparkle(81, 54, 2, "#fff") + sparkle(112, 96, 3, "#FFF3B0"))


if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        a, b, hero, scene, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
