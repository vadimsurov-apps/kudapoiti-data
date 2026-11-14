"""Иконки робота fun (2026-11-14, проход 1114f): места из tools/add_fun_1114f.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя компоновка и палитра фона.
Запуск: python3 tools/icons_fun_1114f.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
O = "#3B3355"
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}
SM = lambda x, y, w=4: f'<path d="M{x-w} {y} Q{x} {y+w} {x+w} {y}" fill="none" stroke="{O}" stroke-width="2.2" stroke-linecap="round"/>'

# 1. Говоровский лес — велодорожки в лесу: ёжик крутит педали, в корзинке шишки
I["fun-govorovsky-les"] = ("#EAF4E0", "#7DB46A",
    "ёжик-велосипедист в зелёном шлеме",
    "едет по лесной велодорожке, в корзинке на руле — шишки и грибок",
    f'<path d="M-4 112 Q64 100 132 112 L132 132 L-4 132Z" fill="#C9A66B" {W(2.6)}/>'
    + f'<path d="M6 30 L18 6 L30 30Z M2 52 L18 22 L34 52Z" fill="#3F8A4E" {W(2.4)}/><rect x="15" y="52" width="6" height="56" fill="#8A5A36" {W(2)}/>'
    + f'<circle cx="38" cy="98" r="16" fill="none" {W(4)}/><circle cx="94" cy="98" r="16" fill="none" {W(4)}/>'
    + f'<path d="M38 98 L58 98 L80 74 L52 74Z M58 98 L52 74 M80 74 L94 98 M80 74 L84 62" fill="none" stroke="#2F6FD0" stroke-width="4.4" stroke-linejoin="round"/>'
    + f'<path d="M78 60 L92 60" stroke="{O}" stroke-width="4" stroke-linecap="round"/>'
    + f'<rect x="86" y="62" width="20" height="12" rx="3" fill="#E9C27A" {W(2.4)}/>'
    + f'<ellipse cx="92" cy="61" rx="4" ry="5" fill="#9A5A2E" {W(1.8)}/><path d="M98 62 Q102 54 106 62Z" fill="#E8483A" {W(1.8)}/>'
    # ёжик
    + "".join(f'<path d="M{x} {y} l-8 -10 l10 4Z" fill="#6B4A32" {W(1.6)}/>' for x, y in ((40, 60), (46, 52), (54, 48), (62, 48), (36, 70)))
    + f'<ellipse cx="54" cy="64" rx="18" ry="14" fill="#8C6446" {W(3)}/>'
    + f'<path d="M64 56 Q78 58 80 66 Q74 72 64 70Z" fill="#F2D3B0" {W(2.4)}/><circle cx="81" cy="66" r="2.6" fill="{O}"/>'
    + eye(70, 61, .6)
    + f'<path d="M44 52 Q54 38 68 48 Z" fill="#4FB35A" {W(2.4)}/>'
    + f'<path d="M58 76 L60 90" stroke="{O}" stroke-width="3.4" stroke-linecap="round"/>')

# 2. Чоботовский лес — хвойный лес с детскими площадками: ёлка-великан качает гамак с бельчонком
I["fun-chobotovsky-les"] = ("#E3EEF7", "#5E8FB8",
    "пушистая ёлка-великан с глазками и румянцем",
    "держит на ветке-лапе верёвочный гамак, в котором дремлет рыжий бельчонок",
    f'<rect x="-4" y="114" width="136" height="18" fill="#9CCB7A"/>'
    + f'<rect x="54" y="98" width="14" height="20" fill="#7A4A2A" {W(2.4)}/>'
    + f'<path d="M61 6 L84 40 L74 40 L96 70 L82 70 L106 100 L16 100 L40 70 L26 70 L48 40 L38 40Z" fill="#2E7D4F" {W(3)}/>'
    + face(61, 56, d=9, k=.8)
    + f'<path d="M100 88 L118 96" stroke="{O}" stroke-width="2"/><path d="M84 78 L80 100" stroke="{O}" stroke-width="2"/>'
    + f'<path d="M80 100 Q98 116 118 96" fill="#F4E3B8" {W(2.6)}/>'
    + f'<path d="M84 102 L90 108 M94 106 L100 110 M104 104 L110 106" stroke="#C9A66B" stroke-width="1.6"/>'
    + f'<path d="M110 98 Q124 86 116 76 Q108 80 108 92Z" fill="#D9762B" {W(2)}/>'
    + f'<circle cx="98" cy="100" r="7" fill="#E08A3A" {W(2)}/><path d="M94 99 q2 2 4 0 M100 99 q2 2 4 0" fill="none" stroke="{O}" stroke-width="1.6"/>'
    + f'<path d="M94 92 l2 -5 l3 4" fill="#E08A3A" {W(1.6)}/>'
    + '<text x="104" y="84" font-family="Arial" font-weight="700" font-size="10" fill="#fff">z</text>'
    + '<text x="112" y="74" font-family="Arial" font-weight="700" font-size="8" fill="#fff">z</text>')

# 3. Парк у прудов «Радуга» — радужный мостик над прудом, девочка на самокате
I["fun-park-raduga-veshnyaki"] = ("#FFF6E8", "#F0A8C8",
    "полукруглый радужный мостик-персонаж с улыбкой",
    "перекинулся через синий пруд, по нему едет девочка на самокате",
    f'<ellipse cx="64" cy="112" rx="70" ry="22" fill="#5BB6E8" {W(2.6)}/>'
    + f'<path d="M14 112 A50 50 0 0 1 114 112 L102 112 A38 38 0 0 0 26 112Z" fill="#F0453A" {W(2.6)}/>'
    + f'<path d="M26 112 A38 38 0 0 1 102 112 L94 112 A30 30 0 0 0 34 112Z" fill="#F7C02F"/>'
    + f'<path d="M34 112 A30 30 0 0 1 94 112 L86 112 A22 22 0 0 0 42 112Z" fill="#53B85A"/>'
    + f'<path d="M42 112 A22 22 0 0 1 86 112" fill="none" {W(2.6)}/>'
    + face(64, 84, d=10, k=.6)
    + f'<path d="M60 52 L72 52 M66 52 L58 34 M58 34 L52 34" stroke="{O}" stroke-width="3" stroke-linecap="round"/>'
    + f'<circle cx="58" cy="54" r="3.4" fill="{O}"/><circle cx="74" cy="54" r="3.4" fill="{O}"/>'
    + f'<path d="M64 46 L60 30 M60 38 L52 36" stroke="#E84393" stroke-width="5" stroke-linecap="round"/>'
    + f'<circle cx="60" cy="22" r="7" fill="#FFD9B8" {W(2.2)}/><path d="M53 20 Q60 10 67 20" fill="#7A4A26" {W(1.8)}/>'
    + sparkle(104, 26, 6, "#fff") + sparkle(20, 34, 4, "#fff"))

# 4. Парк Казачьей славы — фонтан и площадка: каменная чаша-фонтан брызгает, мальчик ловит струйки
I["fun-park-kazachey-slavy"] = ("#E6F6FA", "#4FB1C9",
    "каменная чаша фонтана с мордашкой на боку",
    "брызгает вверх тремя струйками, а мальчик в панамке подставляет ладошки",
    f'<rect x="-4" y="112" width="136" height="20" fill="#D8CFC0"/>'
    + f'<rect x="36" y="88" width="20" height="24" fill="#B9B2A6" {W(2.6)}/>'
    + f'<path d="M10 70 L82 70 Q80 92 46 92 Q12 92 10 70Z" fill="#CFC8BB" {W(3)}/>'
    + f'<ellipse cx="46" cy="70" rx="36" ry="7" fill="#7FD0EC" {W(2.6)}/>'
    + face(46, 80, d=9, k=.6)
    + f'<path d="M46 66 Q44 34 46 18 M38 66 Q28 40 20 30 M54 66 Q64 44 74 36" fill="none" stroke="#3FA7DB" stroke-width="3.4" stroke-linecap="round"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#3FA7DB"/>' for x, y in ((46, 12), (18, 24), (78, 30), (84, 40)))
    # мальчик
    + f'<rect x="92" y="78" width="16" height="22" rx="4" fill="#F28C28" {W(2.4)}/>'
    + f'<path d="M96 100 L94 112 M104 100 L106 112" stroke="{O}" stroke-width="3.4" stroke-linecap="round"/>'
    + f'<circle cx="100" cy="66" r="9" fill="#FFD9B8" {W(2.4)}/>'
    + f'<path d="M88 62 Q100 50 112 62Z" fill="#FFFFFF" {W(2.2)}/>'
    + eye(97, 67, .45) + eye(103, 67, .45)
    + f'<path d="M93 82 L84 56" stroke="{O}" stroke-width="6" stroke-linecap="round"/><path d="M93 82 L84 56" stroke="#FFD9B8" stroke-width="3.6" stroke-linecap="round"/>'
    + f'<path d="M107 82 L112 56" stroke="{O}" stroke-width="6" stroke-linecap="round"/><path d="M107 82 L112 56" stroke="#FFD9B8" stroke-width="3.6" stroke-linecap="round"/>')

# 5. Парк «Зюзино» — уличные тренажёры: маятник-тренажёр шагает с мальчиком
I["fun-park-zyuzino"] = ("#F2F0FF", "#8C7AE0",
    "оранжевый уличный тренажёр-маятник с мордашкой на перекладине",
    "мальчик в кепке шагает на его педалях, будто идёт по воздуху над зелёной травкой",
    f'<rect x="-4" y="110" width="136" height="22" fill="#78C25A"/>'
    + f'<path d="M30 112 L50 30 L78 30 L98 112" fill="none" stroke="#F28C28" stroke-width="8" stroke-linejoin="round"/>'
    + f'<path d="M30 112 L50 30 L78 30 L98 112" fill="none" {W(1.6)}/>'
    + f'<rect x="44" y="22" width="40" height="16" rx="7" fill="#F28C28" {W(2.6)}/>'
    + eye(57, 30, .55) + eye(71, 30, .55) + SM(64, 33, 3)
    + f'<path d="M58 38 L44 92 M70 38 L86 88" stroke="#9A9A9A" stroke-width="4" stroke-linecap="round"/>'
    + f'<rect x="36" y="90" width="18" height="6" rx="2" fill="#5A5A5A" {W(1.8)}/><rect x="80" y="86" width="18" height="6" rx="2" fill="#5A5A5A" {W(1.8)}/>'
    # мальчик
    + f'<rect x="56" y="54" width="18" height="20" rx="5" fill="#3E7BE0" {W(2.4)}/>'
    + f'<path d="M60 74 L46 90 M70 74 L88 86" stroke="#2D3A6E" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M58 58 L50 44 M72 58 L78 44" stroke="#FFD9B8" stroke-width="4" stroke-linecap="round"/>'
    + f'<circle cx="65" cy="48" r="8" fill="#FFD9B8" {W(2.2)}/><path d="M56 46 Q65 36 74 46 L80 46" fill="#E8483A" {W(2)}/>'
    + eye(62, 49, .4) + eye(68, 49, .4))

# 6. Химкинский лесопарк — беседки для пикника у водохранилища: плед для пикника под сосной у воды
I["fun-khimkinsky-lesopark"] = ("#FFF1E0", "#E8A15A",
    "клетчатый красно-белый плед для пикника с мордашкой на загнутом краешке",
    "расстелен у кромки водохранилища под сосной, на нём яблоко и термос",
    f'<rect x="-4" y="40" width="136" height="44" fill="#6CB7E0"/>'
    + f'<path d="M-4 52 q10 -4 20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0" fill="none" stroke="#fff" stroke-width="2" opacity=".7"/>'
    + f'<rect x="-4" y="80" width="136" height="52" fill="#8CC56A"/>'
    + f'<rect x="100" y="20" width="7" height="66" fill="#8A5A36" {W(2)}/><ellipse cx="104" cy="22" rx="20" ry="12" fill="#2F7D4A" {W(2.4)}/>'
    + f'<path d="M14 104 L44 82 L110 90 L84 118Z" fill="#E8483A" {W(3)}/>'
    + "".join(f'<path d="M{14+i*14} {104-i*10} L{40+i*12} {116-i*0}" stroke="#fff" stroke-width="3" opacity=".8"/>' for i in range(1, 3))
    + f'<path d="M30 92 L98 100 M22 98 L92 108" stroke="#fff" stroke-width="3" opacity=".8"/>'
    + f'<path d="M84 118 Q92 112 96 116 L88 122Z" fill="#F5B5AE" {W(2)}/>'
    + eye(36, 104, .5) + eye(46, 106, .5) + SM(42, 110, 3)
    + f'<circle cx="62" cy="94" r="6" fill="#7CC243" {W(2)}/><path d="M62 88 L63 84" stroke="{O}" stroke-width="2"/>'
    + f'<rect x="72" y="80" width="10" height="18" rx="3" fill="#3E7BE0" {W(2)}/><rect x="71" y="77" width="12" height="5" rx="2" fill="#B0B8C8" {W(1.8)}/>')

# 7. Брик Стар Ленд (Остров Мечты) — выставка из кубиков: красный кирпичик балансирует башней
I["fun-brickstar-ostrov"] = ("#FFF7D6", "#F5C431",
    "красный кирпичик-конструктор с четырьмя пупырышками и мордашкой",
    "держит на макушке шаткую башню из жёлтого, синего и зелёного кирпичиков, раскинув ручки для равновесия",
    f'<rect x="30" y="76" width="68" height="36" rx="3" fill="#E33B2E" {W(3)}/>'
    + "".join(f'<rect x="{x}" y="68" width="10" height="9" rx="2" fill="#E33B2E" {W(2.4)}/>' for x in (36, 52, 66, 82))
    + face(64, 92, d=11, k=.8)
    + f'<path d="M30 90 L14 80 M98 90 L114 80" stroke="{O}" stroke-width="3.4" stroke-linecap="round"/>'
    + f'<g transform="rotate(-6 64 50)"><rect x="46" y="52" width="36" height="16" rx="2" fill="#F7C51E" {W(2.6)}/>'
    + f'<rect x="50" y="46" width="8" height="7" rx="2" fill="#F7C51E" {W(2)}/><rect x="70" y="46" width="8" height="7" rx="2" fill="#F7C51E" {W(2)}/></g>'
    + f'<g transform="rotate(8 64 34)"><rect x="50" y="32" width="30" height="14" rx="2" fill="#2F6FD0" {W(2.6)}/>'
    + f'<rect x="54" y="26" width="8" height="7" rx="2" fill="#2F6FD0" {W(2)}/><rect x="68" y="26" width="8" height="7" rx="2" fill="#2F6FD0" {W(2)}/></g>'
    + f'<g transform="rotate(-10 64 18)"><rect x="54" y="14" width="22" height="12" rx="2" fill="#3DAA4A" {W(2.4)}/>'
    + f'<rect x="58" y="8" width="7" height="7" rx="2" fill="#3DAA4A" {W(2)}/></g>'
    + f'<path d="M40 112 L40 120 M88 112 L88 120" stroke="{O}" stroke-width="3.4" stroke-linecap="round"/>')

# 8. Парк альпак «Симба» — угощение животным: стаканчик с морковкой, к нему тянется альпака
I["fun-alpaca-simba"] = ("#FDEFF4", "#D98BB0",
    "бумажный полосатый стаканчик с морковными палочками и мордашкой",
    "его осторожно трогает губами белая пушистая альпака, выглянувшая из-за деревянного заборчика",
    f'<rect x="-4" y="82" width="136" height="8" fill="#B07A4A" {W(2)}/><rect x="-4" y="100" width="136" height="8" fill="#B07A4A" {W(2)}/>'
    + "".join(f'<rect x="{x}" y="72" width="8" height="60" fill="#C88A55" {W(2)}/>' for x in (6, 114))
    + f'<path d="M74 30 Q72 12 90 10 Q112 10 112 32 L112 76 L84 76 Q84 54 74 46Z" fill="#FFFFFF" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="#FFFFFF" {W(1.6)}/>' for x, y in ((86, 10), (96, 6), (106, 10)))
    + f'<path d="M84 12 L80 2 L90 8 M104 10 L110 0 L112 12" fill="#FFFFFF" {W(2)}/>'
    + f'<ellipse cx="74" cy="40" rx="10" ry="8" fill="#F3E3D3" {W(2.4)}/><path d="M68 42 q4 3 8 0" fill="none" stroke="{O}" stroke-width="2"/>'
    + eye(88, 26, .6)
    # стаканчик
    + f'<path d="M30 58 L66 58 L60 112 L36 112Z" fill="#FFFFFF" {W(3)}/>'
    + f'<path d="M33 72 L63 72 M35 88 L61 88" stroke="#E8483A" stroke-width="5"/>'
    + "".join(f'<path d="M{x} 60 L{x+dx} 36" stroke="#F28C28" stroke-width="5" stroke-linecap="round"/>' for x, dx in ((38, -4), (46, 0), (54, 4), (60, 8)))
    + f'<path d="M44 36 l-2 -6 M58 38 l4 -6" stroke="#4FB35A" stroke-width="2.4" stroke-linecap="round"/>'
    + face(48, 98, d=6, k=.55))

# 9. Музей радио и телевидения «Дедушкина чердака» — «говорящий утюг» из экспозиции
I["fun-radio-tv-cherdak"] = ("#EFE8DC", "#A88C68",
    "говорящий старинный утюг с раструбом-громкоговорителем на ручке",
    "стоит на деревянном ламповом радиоприёмнике и выпевает в эфир цветные нотки",
    f'<rect x="18" y="82" width="92" height="40" rx="6" fill="#9B6A3E" {W(3)}/>'
    + f'<rect x="26" y="90" width="44" height="24" rx="4" fill="#E8D7A8" {W(2.4)}/>'
    + "".join(f'<path d="M{x} 92 L{x} 112" stroke="#9B6A3E" stroke-width="1.6"/>' for x in (34, 42, 50, 58))
    + f'<circle cx="86" cy="96" r="6" fill="#E8C27A" {W(2.2)}/><circle cx="98" cy="106" r="5" fill="#E8C27A" {W(2.2)}/>'
    + f'<path d="M20 82 Q24 54 50 52 L104 52 L104 82Z" fill="#4A4F5C" {W(3)}/>'
    + f'<path d="M50 52 Q52 36 62 36 L80 36 Q90 36 90 52" fill="none" stroke="{O}" stroke-width="6" stroke-linecap="round"/>'
    + f'<path d="M80 36 L96 22 L112 8 L114 34 Z" fill="#D9A441" {W(2.6)}/>'
    + face(66, 68, d=10, k=.75)
    + f'<text x="14" y="40" font-family="Arial" font-weight="700" font-size="20" fill="#E8483A">♪</text>'
    + f'<text x="28" y="22" font-family="Arial" font-weight="700" font-size="16" fill="#2F6FD0">♫</text>')

# 10. Ванана Парк — игровая с горками и сухим бассейном: горка-труба выпускает малыша в шарики
I["fun-vanana-park"] = ("#E6F7FF", "#4AA8E0",
    "жёлтая горка-труба спиралью с мордашкой на верхушке",
    "выпускает малыша в полосатой футболке прямо в сухой бассейн с цветными шариками",
    f'<rect x="-4" y="98" width="136" height="34" fill="#FFFFFF" opacity=".5"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="7" fill="{c}" {W(1.6)}/>' for x, y, c in
              ((14, 110, "#E8483A"), (28, 104, "#3DAA4A"), (42, 112, "#2F6FD0"), (56, 104, "#F7C51E"), (70, 112, "#E84393"),
               (84, 106, "#F28C28"), (98, 112, "#3DAA4A"), (112, 106, "#E8483A"), (22, 122, "#F7C51E"), (50, 124, "#2F6FD0"),
               (78, 124, "#E8483A"), (106, 122, "#2F6FD0")))
    + f'<path d="M96 14 Q120 22 108 38 Q94 50 112 62 Q124 76 98 84 L80 96" fill="none" stroke="{O}" stroke-width="20" stroke-linecap="round"/>'
    + f'<path d="M96 14 Q120 22 108 38 Q94 50 112 62 Q124 76 98 84 L80 96" fill="none" stroke="#F7C51E" stroke-width="15" stroke-linecap="round"/>'
    + f'<circle cx="94" cy="16" r="13" fill="#F7C51E" {W(2.6)}/>' + face(94, 16, d=5, k=.5)
    # малыш в полёте
    + f'<circle cx="54" cy="70" r="9" fill="#FFD9B8" {W(2.4)}/>' + eye(51, 70, .45) + eye(57, 70, .45)
    + f'<ellipse cx="54" cy="76" rx="3" ry="2.4" fill="{O}"/>'
    + f'<rect x="58" y="76" width="18" height="12" rx="4" fill="#FFFFFF" {W(2.2)}/><path d="M60 82 L74 82" stroke="#E8483A" stroke-width="3"/>'
    + f'<path d="M48 64 L40 54 M60 64 L66 52" stroke="#FFD9B8" stroke-width="4" stroke-linecap="round"/>'
    + f'<path d="M76 84 L86 90 M74 88 L82 96" stroke="#2D3A6E" stroke-width="4" stroke-linecap="round"/>')

# 11. Музей «Динамо» — спортивная слава клуба: кубок с бело-голубой лентой под стеклянным колпаком
I["fun-dynamo-museum"] = ("#E4ECFA", "#3F67B5",
    "серебряный кубок с бело-голубой лентой и буквой «Д»",
    "гордо улыбается на музейной тумбе под стеклянным колпаком, вокруг искорки",
    f'<rect x="30" y="100" width="68" height="28" fill="#5A3A26" {W(3)}/>'
    + f'<path d="M30 100 L30 34 Q30 12 64 12 Q98 12 98 34 L98 100" fill="#DFF1FF" opacity=".55" {W(2.6)}/>'
    + f'<path d="M38 30 Q40 20 48 18" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    + f'<path d="M44 34 L84 34 Q84 66 64 70 Q44 66 44 34Z" fill="#C9D3E0" {W(3)}/>'
    + f'<path d="M44 40 Q32 40 34 50 Q36 58 46 56 M84 40 Q96 40 94 50 Q92 58 82 56" fill="none" {W(3)}/>'
    + f'<rect x="60" y="70" width="8" height="12" fill="#C9D3E0" {W(2.4)}/><rect x="48" y="82" width="32" height="10" rx="2" fill="#C9D3E0" {W(2.6)}/>'
    + f'<path d="M44 74 L36 96 L44 92 L48 98 L54 76" fill="#2F6FD0" {W(2)}/><path d="M84 74 L92 96 L84 92 L80 98 L74 76" fill="#FFFFFF" {W(2)}/>'
    + f'<text x="58" y="66" font-family="Arial" font-weight="900" font-size="14" fill="#2F6FD0">Д</text>'
    + face(64, 46, d=8, k=.6)
    + sparkle(18, 30, 5, "#fff") + sparkle(110, 60, 6, "#fff"))

# 12. «Поезд Победы» у Белорусского вокзала — вагон-теплушка с красной звездой и голубем на крыше
I["fun-poezd-pobedy"] = ("#F5EEDD", "#B9A27A",
    "зелёный деревянный вагон-теплушка с красной звездой",
    "стоит у перрона под круглыми вокзальными часами, на крыше сидит белый голубь",
    f'<rect x="-4" y="110" width="136" height="6" fill="#6E6E6E"/><rect x="-4" y="118" width="136" height="14" fill="#C9B79A"/>'
    + f'<circle cx="104" cy="22" r="13" fill="#FFFFFF" {W(2.6)}/><path d="M104 14 L104 22 L110 24" fill="none" {W(2.2)}/>'
    + f'<rect x="12" y="48" width="90" height="54" rx="3" fill="#4C7A3E" {W(3)}/>'
    + "".join(f'<path d="M{x} 50 L{x} 100" stroke="#3B6230" stroke-width="2"/>' for x in (24, 36, 78, 90))
    + f'<path d="M8 48 Q57 34 106 48Z" fill="#5E5E5E" {W(2.6)}/>'
    + f'<rect x="44" y="58" width="26" height="40" fill="#3B6230" {W(2.4)}/>'
    + f'<path d="M57 64 l3 7 l7 0 l-6 4 l2 7 l-6 -4 l-6 4 l2 -7 l-6 -4 l7 0Z" fill="#E33B2E" {W(1.4)}/>'
    + face(57, 88, d=7, k=.5)
    + f'<circle cx="30" cy="106" r="6" fill="#3A3A3A" {W(2)}/><circle cx="84" cy="106" r="6" fill="#3A3A3A" {W(2)}/>'
    # голубь
    + f'<ellipse cx="34" cy="36" rx="10" ry="6" fill="#FFFFFF" {W(2)}/><circle cx="42" cy="31" r="4" fill="#FFFFFF" {W(2)}/>'
    + f'<path d="M45 31 l4 1 l-4 1" fill="#F2A23A"/><circle cx="42" cy="30" r="1" fill="{O}"/>'
    + f'<path d="M30 34 Q22 22 34 26" fill="#E8EEF5" {W(1.8)}/>')

# 13. Выставочное пространство Музея транспорта (Южный речной вокзал) — трамвай с вопросом
I["fun-mtm-andropova"] = ("#FFEDE6", "#E2725B",
    "красный трамвайчик с круглыми фарами-глазками и дугой-токоприёмником",
    "катится по рельсам, а над крышей висит большой жёлтый вопросительный знак",
    f'<path d="M-4 30 L132 22" stroke="{O}" stroke-width="2"/>'
    + f'<path d="M58 42 L72 28 L90 27" fill="none" stroke="{O}" stroke-width="3" stroke-linecap="round"/>'
    + f'<rect x="16" y="42" width="96" height="58" rx="12" fill="#E33B2E" {W(3)}/>'
    + f'<rect x="16" y="78" width="96" height="10" fill="#FFF1D6" {W(2)}/>'
    + "".join(f'<rect x="{x}" y="52" width="16" height="18" rx="3" fill="#BFE6F7" {W(2.2)}/>' for x in (24, 46, 68))
    + f'<rect x="90" y="52" width="16" height="30" rx="3" fill="#BFE6F7" {W(2.2)}/>'
    + eye(30, 61, .55) + eye(38, 61, .55)
    + f'<circle cx="104" cy="92" r="4" fill="#FFE27A" {W(1.6)}/>'
    + f'<circle cx="38" cy="104" r="7" fill="#4A4A4A" {W(2)}/><circle cx="90" cy="104" r="7" fill="#4A4A4A" {W(2)}/>'
    + f'<path d="M-4 112 L132 112" stroke="#7A7A7A" stroke-width="4"/>'
    + f'<text x="20" y="38" font-family="Arial" font-weight="900" font-size="30" fill="#F7C51E" stroke="{O}" stroke-width="1.6">?</text>')

# 14. Общественный музей авиации и космонавтики — спускаемый аппарат на парашюте
I["fun-aviacosmos-domodedovskaya"] = ("#E9F0FF", "#6C83D6",
    "обгорелый шарик спускаемого космического аппарата с мордашкой в иллюминаторе",
    "плавно опускается на полосатом красно-белом парашюте над жёлтой степью",
    f'<path d="M-4 116 Q64 104 132 116 L132 132 L-4 132Z" fill="#E8C35A"/>'
    + f'<path d="M20 44 Q64 -6 108 44 Q98 38 86 44 Q76 36 64 44 Q52 36 42 44 Q30 38 20 44Z" fill="#FFFFFF" {W(3)}/>'
    + f'<path d="M42 44 Q48 14 64 8 Q60 26 64 44 Q52 36 42 44Z M86 44 Q80 14 64 8 Q68 26 64 44 Q76 36 86 44Z" fill="#E33B2E" {W(2.2)}/>'
    + f'<path d="M20 44 L54 84 M42 44 L58 82 M86 44 L70 82 M108 44 L74 84" stroke="{O}" stroke-width="1.6"/>'
    + f'<circle cx="64" cy="96" r="20" fill="#8A6A4A" {W(3)}/>'
    + f'<path d="M46 104 Q64 120 82 104" fill="none" stroke="#5A4030" stroke-width="3"/>'
    + f'<circle cx="64" cy="92" r="10" fill="#BFE6F7" {W(2.4)}/>' + face(64, 91, d=4, k=.4)
    + sparkle(110, 72, 5, "#fff"))

# 15. Музей магистрального транспорта газа — синий газовый огонёк в каске бежит по трубе
I["fun-gas-museum"] = ("#E8F6FF", "#3C8FD8",
    "синий газовый огонёк-капелька в оранжевой каске",
    "бодро бежит по огромной жёлтой трубе-магистрали с вентилем-штурвалом и машет рукой",
    f'<rect x="-4" y="76" width="136" height="32" fill="#F2C230" {W(3)}/>'
    + f'<rect x="38" y="70" width="10" height="44" rx="3" fill="#E0A81E" {W(2.4)}/><rect x="96" y="70" width="10" height="44" rx="3" fill="#E0A81E" {W(2.4)}/>'
    + f'<path d="M-4 84 L132 84" stroke="#FFE38A" stroke-width="3"/>'
    + f'<rect x="12" y="58" width="6" height="20" fill="#9A9A9A" {W(2)}/><circle cx="15" cy="54" r="10" fill="none" stroke="#E33B2E" stroke-width="4"/>'
    + f'<path d="M5 54 L25 54 M15 44 L15 64" stroke="#E33B2E" stroke-width="3"/>'
    + f'<path d="M70 72 Q50 50 62 30 Q66 40 72 36 Q74 22 86 14 Q82 34 94 46 Q100 62 86 72Z" fill="#3E86F0" {W(3)}/>'
    + f'<path d="M74 70 Q66 58 74 48 Q78 56 84 52 Q88 62 82 70Z" fill="#9FD3FF"/>'
    + f'<path d="M62 30 Q66 14 84 14 Q98 16 96 30Z" fill="#F28C28" {W(2.6)}/><rect x="58" y="28" width="42" height="5" rx="2" fill="#F28C28" {W(2)}/>'
    + face(78, 46, d=7, k=.6)
    + f'<path d="M94 50 L108 38" stroke="{O}" stroke-width="3.4" stroke-linecap="round"/>'
    + f'<path d="M70 72 L64 76 M86 72 L94 76" stroke="{O}" stroke-width="3" stroke-linecap="round"/>')

# 16. Зоопарк «Горки» (Луховицы) — деревенский зоопарк: ослик в соломенной шляпе жуёт сено
I["fun-zoo-gorki"] = ("#F9F2DC", "#C8A85A",
    "серый ослик с длинными ушами в соломенной шляпе с ромашкой",
    "жуёт пучок сена, облокотившись на деревянную изгородь деревенского зоопарка",
    f'<rect x="-4" y="110" width="136" height="22" fill="#9CCB6A"/>'
    + f'<rect x="-4" y="84" width="136" height="7" fill="#B07A4A" {W(2)}/><rect x="-4" y="100" width="136" height="7" fill="#B07A4A" {W(2)}/>'
    + "".join(f'<rect x="{x}" y="76" width="7" height="44" fill="#C88A55" {W(2)}/>' for x in (8, 112))
    + f'<path d="M44 30 L38 4 L52 22Z M74 26 L84 0 L86 24Z" fill="#9A9AA8" {W(2.6)}/>'
    + f'<ellipse cx="62" cy="54" rx="26" ry="28" fill="#A9A9B6" {W(3)}/>'
    + f'<ellipse cx="62" cy="72" rx="18" ry="13" fill="#E6E2DA" {W(2.6)}/>'
    + f'<circle cx="56" cy="72" r="2" fill="{O}"/><circle cx="68" cy="72" r="2" fill="{O}"/>'
    + eye(52, 50, .7) + eye(72, 50, .7)
    + f'<path d="M30 34 Q62 14 94 34 Q62 40 30 34Z" fill="#EBC56A" {W(2.6)}/><path d="M44 30 Q62 14 80 30" fill="#EBC56A" {W(2.4)}/>'
    + f'<circle cx="80" cy="28" r="4" fill="#FFFFFF" {W(1.4)}/><circle cx="80" cy="28" r="1.6" fill="#F7C51E"/>'
    + "".join(f'<path d="M62 80 L{x} 98" stroke="#E2C04A" stroke-width="2.4"/>' for x in (44, 52, 60, 70, 80))
    + f'<path d="M34 86 L48 80 M90 86 L76 80" stroke="{O}" stroke-width="3.4" stroke-linecap="round"/>')

if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
