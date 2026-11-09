"""Иконки робота cafes, 2026-11-09 (22:35 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая придумана и нарисована
отдельно (свой герой по кухне/названию, своя сцена, компоновка и палитра). Сверено с icons-src/subjects.txt
(гедза, наруто, молочный коктейль, кумган, куриное крылышко, дорадо, «Наполеон», печенье-звёздочка, вишнёвый пирог,
бисквитный рулет, пралине-ракушка, пирожок на метле, рисовая гора — свободны).
Запуск: python3 tools/icons_cafes_1110.py [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "k13_soy": ("#F4FFF0", "#8FCB7A"),
    "k13_naruto": ("#FFF8EE", "#E9B98A"),
    "k13_lilac": ("#FBF0FF", "#C79BE6"),
    "k13_tochka": ("#5B4C8C", "#231A44"),
    "k13_party": ("#FFF1E0", "#FF9B6A"),
    "k13_sea": ("#E8FBFF", "#3FB4D8"),
    "k13_mint": ("#EFFFF8", "#7FD9B5"),
    "k13_lemon": ("#FFFDE6", "#F2D24B"),
    "k13_peach": ("#FFF3EC", "#F5A88A"),
    "k13_carpet": ("#EEF4FF", "#8EA6E8"),
    "k13_gold": ("#FFF6D6", "#D9A93A"),
    "k13_dikanka": ("#3C5AA8", "#14204F"),
    "k13_ice": ("#F7FBFF", "#A9C8E8"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Тануки (Нахимовский) — гедза пробует ножкой соевый соус, как лужу
add("cafe-tanuki-nakhimovsky-67",
    "японская гедза-полумесяц с защипами-гребешком и поджаристым донцем",
    "осторожно макает ножку в круглую мисочку соевого соуса, как в лужу, проверяя, не холодно ли", "k13_soy", f'''
<ellipse cx="88" cy="104" rx="30" ry="10" fill="#FFFFFF" {s()}/>
<ellipse cx="88" cy="103" rx="23" ry="6" fill="#5A3418" {W(2)}/>
<path d="M76 102 Q82 99 88 102 Q94 105 100 102" fill="none" stroke="#8A5A33" stroke-width="2"/>
<path d="M18 86 Q14 40 60 34 Q104 40 98 86 Q60 96 18 86Z" fill="#FFF1D6" {s()}/>
<path d="M22 82 Q60 92 96 82 L96 88 Q60 98 22 88Z" fill="#E0A55A" {W(2.4)}/>
<path d="M26 52 q6 -8 12 0 q6 -8 12 0 q6 -8 12 0 q6 -8 12 0 q6 -8 12 0" fill="none" {W(2.6)}/>
<path d="M84 88 Q88 96 86 100" fill="none" {W(3)}/>
<path d="M40 88 Q38 98 42 104" fill="none" {W(3)}/>
<ellipse cx="43" cy="105" rx="5" ry="2.6" fill="#FFF1D6" {W(2)}/>
{face(58, 68, d=12, k=1.0)}
<path d="M98 92 l4 -4 M104 96 l5 -2" {W(2)}/>
''' + sparkle(108, 30, 4) + sparkle(20, 24, 3))

# 2. Тануки (Митинская) — рыбный кружок наруто катится колесом по палочкам-мостику
add("cafe-tanuki-mitinskaya-50",
    "японский рыбный кружок наруто — белый, с розовой спиралью и волнистым краем",
    "катится колесом по двум палочкам для еды, перекинутым мостиком над миской с лапшой", "k13_naruto", f'''
<path d="M10 104 Q64 126 118 104 L112 120 Q64 134 16 120Z" fill="#E85D4A" {s()}/>
<ellipse cx="64" cy="104" rx="54" ry="10" fill="#FFE4A8" {s()}/>
<path d="M24 102 q8 4 16 0 q8 -4 16 0 q8 4 16 0 q8 -4 16 0 q8 4 16 0" fill="none" stroke="#E9B44C" stroke-width="2.4"/>
<path d="M6 92 L122 80" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M6 92 L122 80" stroke="#C98A4B" stroke-width="5" stroke-linecap="round"/>
<path d="M6 98 L122 86" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M6 98 L122 86" stroke="#D9A066" stroke-width="5" stroke-linecap="round"/>
<path d="M64 14 q6 0 8 4 q6 -2 10 2 q2 5 6 6 q4 4 2 9 q4 4 2 9 q2 5 -2 9 q0 6 -5 7 q-3 5 -9 4 q-4 4 -9 2 q-6 2 -9 -2 q-6 0 -8 -5 q-5 -2 -5 -8 q-4 -4 -2 -9 q-3 -5 0 -9 q0 -6 5 -8 q2 -5 8 -5 q4 -4 8 -2Z" fill="#FFFFFF" {s()}/>
<path d="M64 48 q-6 0 -6 -6 q0 -10 10 -10 q14 0 14 14 q0 18 -18 18 q-22 0 -22 -22" fill="none" stroke="#FF6FA5" stroke-width="5" stroke-linecap="round"/>
{face(64, 50, d=10, k=0.85, mouth=False)}
<path d="M58 60 Q64 65 70 60" fill="none" {W(2.4)}/>
<path d="M26 40 l-8 -2 M28 50 l-10 2 M30 30 l-6 -6" {W(2.2)}/>
''' + sparkle(108, 26, 4))

# 3. Dizengof/99 — молочный коктейль надувает через трубочку воздушный шарик (анимация по выходным)
add("cafe-dizengof99-nakhimovsky",
    "высокий стакан клубничного молочного коктейля со взбитыми сливками и вишенкой",
    "через полосатую трубочку надувает голубой воздушный шарик, щёки надуты от усердия", "k13_lilac", f'''
<path d="M40 52 L46 118 H82 L88 52Z" fill="#FFB3CF" {s()}/>
<path d="M44 70 H84" stroke="#FF8AB5" stroke-width="3"/>
<path d="M36 52 Q38 34 50 36 Q56 24 66 32 Q78 26 82 38 Q94 38 92 52Z" fill="#FFFFFF" {s()}/>
<circle cx="64" cy="26" r="7" fill="#E8203A" {W(2.4)}/><path d="M64 19 Q68 10 74 8" fill="none" {W(2.2)}/>
<path d="M80 40 L100 20" stroke="{O}" stroke-width="8" stroke-linecap="round"/>
<path d="M80 40 L100 20" stroke="#FFFFFF" stroke-width="4.4" stroke-linecap="round"/>
<path d="M84 36 l3 -3 M90 30 l3 -3 M96 24 l3 -3" stroke="#FF4D6D" stroke-width="3"/>
<ellipse cx="108" cy="14" rx="13" ry="15" fill="#7CC8FF" {s()}/>
<path d="M102 8 Q104 4 108 4" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
{face(64, 88, d=11, k=0.95, mouth=False)}
<circle cx="64" cy="98" r="4" fill="{O}"/>
<circle cx="50" cy="96" r="5" fill="#FF7FA8" opacity=".75"/><circle cx="78" cy="96" r="5" fill="#FF7FA8" opacity=".75"/>
''' + sparkle(22, 30, 4) + sparkle(106, 60, 3))

# 4. Чайхана Точка (круглосуточно) — медный кумган дежурит ночью под полумесяцем
add("cafe-chaikhana-tochka-festivalnaya",
    "медный кумган — восточный кувшин с длинным изогнутым носиком и крышкой-куполом",
    "не спит ночью под полумесяцем и звёздами: из носика идёт пар, рядом горит маленький фонарик — чайхана открыта круглосуточно", "k13_tochka", f'''
<path d="M88 22 A14 14 0 1 0 100 40 A11 11 0 1 1 88 22Z" fill="#FFE68A"/>
<circle cx="24" cy="26" r="2" fill="#fff"/><circle cx="40" cy="14" r="1.6" fill="#fff"/><circle cx="112" cy="62" r="1.8" fill="#fff"/>
<path d="M80 62 Q100 58 104 40" fill="none" stroke="{O}" stroke-width="8" stroke-linecap="round"/>
<path d="M80 62 Q100 58 104 40" fill="none" stroke="#E08A3C" stroke-width="4.4" stroke-linecap="round"/>
<path d="M104 34 Q100 26 106 20 M110 34 Q108 28 112 24" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".85"/>
<path d="M40 66 Q30 66 30 80 Q30 92 42 92" fill="none" {W(5)}/>
<path d="M46 52 Q34 70 38 92 Q42 112 64 114 Q86 112 90 92 Q94 70 82 52Z" fill="#E59443" {s()}/>
<path d="M40 82 H88" stroke="#B9662A" stroke-width="3"/>
<path d="M52 52 Q50 38 64 32 Q78 38 76 52Z" fill="#F2B15C" {s()}/>
<circle cx="64" cy="29" r="4" fill="#F2B15C" {W(2.2)}/>
<path d="M50 100 l6 -6 l6 6 l6 -6 l6 6" fill="none" stroke="#FFD27A" stroke-width="2.4"/>
{face(64, 70, d=11, k=0.9)}
<rect x="12" y="96" width="14" height="18" rx="3" fill="#FFCF5C" {W(2.4)}/>
<path d="M14 96 Q19 88 24 96" fill="none" {W(2.4)}/><circle cx="19" cy="105" r="3" fill="#FF8A3D"/>
''')

# 5. Мясо & Рыба (Европолис) — куриное крылышко-гриль пытается взлететь с решётки
add("cafe-myaso-ryba-evropolis",
    "румяное куриное крылышко-гриль с золотыми полосками от решётки",
    "машет собой, как настоящим крылом, и подпрыгивает над решёткой гриля, пытаясь взлететь", "k13_party", f'''
<path d="M14 108 H114" stroke="{O}" stroke-width="6" stroke-linecap="round"/>
<path d="M20 100 V116 M40 100 V116 M60 100 V116 M80 100 V116 M100 100 V116" stroke="{O}" stroke-width="4" stroke-linecap="round"/>
<path d="M26 96 Q24 88 28 84 M54 96 Q52 88 56 84 M84 96 Q82 88 86 84" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".8"/>
<path d="M30 66 Q22 32 56 26 Q84 22 98 40 Q110 58 96 74 Q80 88 56 84 Q36 82 30 66Z" fill="#E8913C" {s()}/>
<path d="M44 40 L58 66 M58 34 L72 62 M74 34 L86 58" stroke="#9C4F1C" stroke-width="3.4" stroke-linecap="round"/>
<path d="M98 40 Q116 28 120 12 Q108 22 96 26" fill="#E8913C" {s()}/>
<path d="M104 30 Q112 24 116 16" fill="none" stroke="#9C4F1C" stroke-width="2"/>
{face(62, 60, d=12, k=1.0)}
<path d="M16 52 l-8 -4 M18 62 l-10 0 M20 72 l-8 4" {W(2.2)}/>
''' + sparkle(26, 18, 4) + sparkle(112, 86, 3))

# 6. Мясо & Рыба (Румянцево) — дорадо делает сальто над решёткой гриля
add("cafe-myaso-ryba-rumyantsevo",
    "серебристая рыба дорадо с золотой полоской на лбу и долькой лимона во рту",
    "делает сальто дугой над решёткой гриля, как гимнаст, оставляя в воздухе брызги", "k13_sea", f'''
<rect x="18" y="104" width="92" height="12" rx="3" fill="#4B4B5A" {s()}/>
<path d="M30 104 V116 M46 104 V116 M62 104 V116 M78 104 V116 M94 104 V116" stroke="#9A9AAA" stroke-width="2.4"/>
<path d="M24 88 Q20 40 64 26 Q108 40 104 88" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="4 7" stroke-linecap="round"/>
<g transform="rotate(-25 64 54)">
<path d="M98 54 L118 38 L114 54 L118 70Z" fill="#B8C4D6" {s()}/>
<ellipse cx="62" cy="54" rx="38" ry="22" fill="#D3DCE8" {s()}/>
<path d="M44 33 Q58 22 76 33" fill="#B8C4D6" {W(2.4)}/>
<path d="M34 46 Q40 40 48 42" fill="none" stroke="#E8B830" stroke-width="4" stroke-linecap="round"/>
<path d="M54 64 Q70 72 86 62" fill="none" stroke="#AEB9CB" stroke-width="2.4"/>
<path d="M24 58 L14 54 L14 64Z" fill="#FFE45E" {W(2.2)}/>
<circle cx="40" cy="52" r="6" fill="#fff" {W(2)}/>{eye(40, 52, 0.9)}
<ellipse cx="46" cy="62" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/>
</g>
<circle cx="18" cy="30" r="3" fill="#fff" {W(1.6)}/><circle cx="110" cy="92" r="2.6" fill="#fff" {W(1.4)}/>
''' + sparkle(100, 18, 4))

# 7. Здрасте (Родниковая) — кусок торта «Наполеон» выглядывает из-за детской горки
add("cafe-zdraste-rodnikovaya",
    "кусок слоёного торта «Наполеон» в крошке, с кремовыми прослойками",
    "играет в прятки: выглядывает из-за жёлтой детской горки в игровой зоне кофейни", "k13_mint", f'''
<path d="M70 30 H96 V40 H70Z" fill="#7FB8FF" {s()}/>
<path d="M90 40 Q100 76 120 112 H104 Q86 80 76 40Z" fill="#FFD84A" {s()}/>
<path d="M70 40 V116 M96 40 V116" stroke="{O}" stroke-width="4"/>
<path d="M70 56 H96 M70 72 H96 M70 88 H96" stroke="{O}" stroke-width="3"/>
<path d="M14 116 V60 L66 44 V116Z" fill="#F7E2B5" {s()}/>
<path d="M14 60 L66 44" stroke="#C99A55" stroke-width="5"/>
<path d="M16 76 L64 64 M16 92 L64 82 M16 106 L64 98" stroke="#FFFFFF" stroke-width="4"/>
<path d="M16 76 L64 64 M16 92 L64 82" stroke="#E8C88A" stroke-width="1.6"/>
<circle cx="24" cy="58" r="2" fill="#B07A3A"/><circle cx="36" cy="54" r="2" fill="#B07A3A"/><circle cx="50" cy="50" r="2" fill="#B07A3A"/>
<circle cx="56" cy="74" r="7" fill="#fff" {W(2)}/>{eye(57, 74, 0.9)}
<circle cx="40" cy="78" r="7" fill="#fff" {W(2)}/>{eye(41, 78, 0.9)}
<path d="M42 92 Q50 98 58 90" fill="none" {W(2.6)}/>
<path d="M58 48 l4 -8 M64 50 l8 -6" {W(2.2)}/>
''' + sparkle(110, 20, 4) + sparkle(24, 30, 3))

# 8. Здрасте (Саларьевская) — печенье-звёздочка едет на самокате
add("cafe-zdraste-salarevskaya",
    "песочное печенье-звёздочка с белой глазурью по краю",
    "мчится на красном двухколёсном самокате, за ней вьются три крошечные крошки-пылинки", "k13_lemon", f'''
<circle cx="34" cy="108" r="9" fill="#555" {s()}/><circle cx="34" cy="108" r="3" fill="#ccc"/>
<circle cx="96" cy="108" r="9" fill="#555" {s()}/><circle cx="96" cy="108" r="3" fill="#ccc"/>
<path d="M30 100 H96" stroke="{O}" stroke-width="8" stroke-linecap="round"/>
<path d="M30 100 H96" stroke="#E8323A" stroke-width="4.4" stroke-linecap="round"/>
<path d="M96 100 L86 36" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M96 100 L86 36" stroke="#E8323A" stroke-width="3.6" stroke-linecap="round"/>
<path d="M76 34 H96" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M58 18 L66 38 L88 40 L71 54 L77 76 L58 64 L39 76 L45 54 L28 40 L50 38Z" fill="#F0B65A" {s()}/>
<path d="M58 24 L64 40 L82 42 L68 53 L73 71 L58 61 L43 71 L48 53 L34 42 L52 40Z" fill="none" stroke="#fff" stroke-width="2.4"/>
{face(58, 52, d=9, k=0.8)}
<path d="M48 70 L44 94 M66 70 L70 94" {W(3)}/>
<circle cx="14" cy="70" r="2.4" fill="#E0A04A"/><circle cx="18" cy="82" r="2" fill="#E0A04A"/><circle cx="10" cy="88" r="1.6" fill="#E0A04A"/>
''' + sparkle(110, 22, 4))

# 9. Здрасте (Прокшинский, два этажа) — кусочек вишнёвого пирога поднимается по лестнице
add("cafe-zdraste-prokshinsky",
    "треугольный кусочек вишнёвого пирога с решёткой из теста и вишенками",
    "бодро шагает вверх по лестнице с перилами на второй этаж кофейни", "k13_peach", f'''
<path d="M6 120 V104 H30 V88 H54 V72 H78 V56 H102 V40 H130 V130 H6Z" fill="#C98F5E" {s()}/>
<path d="M6 104 H30 M30 88 H54 M54 72 H78 M78 56 H102 M102 40 H130" stroke="#8E5A30" stroke-width="2"/>
<path d="M14 82 L120 14" stroke="{O}" stroke-width="6" stroke-linecap="round"/>
<path d="M14 82 L120 14" stroke="#F4D3A8" stroke-width="2.6" stroke-linecap="round"/>
<path d="M30 72 V96 M60 52 V80 M90 34 V62" stroke="{O}" stroke-width="3"/>
<path d="M38 82 L80 36 L92 70Z" fill="#F2C27A" {s()}/>
<path d="M44 78 L84 48 L92 70Z" fill="#B3123A" {W(2.4)}/>
<path d="M52 72 L70 50 M62 76 L80 54 M58 62 L86 64" stroke="#F2C27A" stroke-width="3.6" stroke-linecap="round"/>
<circle cx="82" cy="40" r="5" fill="#D81E4A" {W(2)}/><path d="M82 35 Q84 28 90 26" fill="none" {W(2)}/>
{face(62, 60, d=8, k=0.7, mouth=True)}
<path d="M56 78 L54 88 M72 76 L76 86" {W(3)}/>
''' + sparkle(22, 22, 4) + sparkle(112, 70, 3))

# 10. Здрасте (Монаховой) — бисквитный рулет крутит юлу на ковре
add("cafe-zdraste-monakhovoy-87",
    "бисквитный рулет с малиновым вареньем — спираль видна на срезе",
    "сидит на круглом ковре детского уголка и запускает разноцветную юлу, та весело жужжит", "k13_carpet", f'''
<ellipse cx="64" cy="108" rx="56" ry="14" fill="#FFB9D1" {s()}/>
<ellipse cx="64" cy="108" rx="40" ry="9" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="5 5"/>
<rect x="20" y="40" width="50" height="50" rx="6" fill="#F2C778" {s()}/>
<ellipse cx="70" cy="65" rx="22" ry="26" fill="#FFF0D4" {s()}/>
<path d="M70 65 q4 0 4 -4 q0 -7 -8 -7 q-12 0 -12 12 q0 16 16 16 q20 0 20 -20" fill="none" stroke="#9E1036" stroke-width="5" stroke-linecap="round"/>
<circle cx="30" cy="46" r="1.8" fill="#fff"/><circle cx="46" cy="44" r="1.8" fill="#fff"/><circle cx="58" cy="48" r="1.6" fill="#fff"/><circle cx="26" cy="84" r="1.6" fill="#fff"/>
{face(40, 62, d=9, k=0.8)}
<path d="M98 108 L88 92 L108 92Z" fill="#7C5CFF" {s()}/>
<ellipse cx="98" cy="90" rx="18" ry="8" fill="#FFD84A" {s()}/>
<path d="M82 90 H114" stroke="#FF5A5A" stroke-width="4"/>
<path d="M98 82 V72" {W(4)}/>
<path d="M76 84 Q80 78 84 84 M112 76 Q118 72 120 78" fill="none" {W(2)}/>
''' + sparkle(108, 26, 4) + sparkle(22, 24, 3))

# 11. Ян Примус — бельгийская пралине-ракушка в короне на троне-коробке конфет
add("cafe-yan-primus-snezhnaya",
    "бельгийская шоколадная конфета-пралине в форме ракушки, мраморная",
    "в маленькой золотой короне восседает на троне из открытой коробки конфет, как король", "k13_gold", f'''
<path d="M16 120 V78 H112 V120Z" fill="#7A2E3A" {s()}/>
<path d="M16 78 L28 60 H100 L112 78" fill="#A23B4C" {s()}/>
<circle cx="32" cy="98" r="8" fill="#5A3020" {W(2)}/><circle cx="96" cy="98" r="8" fill="#5A3020" {W(2)}/>
<path d="M30 80 Q28 40 64 34 Q100 40 98 80 Q64 90 30 80Z" fill="#8B5A3C" {s()}/>
<path d="M64 80 L64 40 M48 80 L54 42 M80 80 L74 42 M36 76 L44 48 M92 76 L84 48" stroke="#5E3520" stroke-width="2.6"/>
<path d="M40 60 Q52 56 58 66 M72 52 Q84 50 88 62" fill="none" stroke="#E8D2B0" stroke-width="2.4" stroke-linecap="round"/>
<path d="M48 34 L50 18 L58 28 L64 14 L70 28 L78 18 L80 34Z" fill="#FFD23F" {s()}/>
<circle cx="64" cy="14" r="2.6" fill="#E8323A"/>
{face(64, 64, d=11, k=0.9)}
''' + sparkle(112, 26, 4) + sparkle(16, 40, 3))

# 12. Вечера на хуторе — пирожок с вишней летит на метле мимо месяца
add("cafe-vechera-na-khutore-ryazansky",
    "румяный пирожок с вишнёвой начинкой, выглядывающей из надреза",
    "летит верхом на метле по ночному зимнему небу мимо большого месяца, внизу мерцают огоньки", "k13_dikanka", f'''
<path d="M30 20 A20 20 0 1 0 50 52 A16 16 0 1 1 30 20Z" fill="#FFE68A"/>
<circle cx="70" cy="14" r="2" fill="#fff"/><circle cx="104" cy="26" r="1.6" fill="#fff"/><circle cx="16" cy="70" r="1.8" fill="#fff"/><circle cx="96" cy="50" r="1.4" fill="#fff"/>
<path d="M0 116 Q40 104 70 112 Q100 120 128 108 V128 H0Z" fill="#E8F0FF" {W(2)}/>
<circle cx="30" cy="114" r="2.4" fill="#FFD25E"/><circle cx="92" cy="114" r="2.4" fill="#FFD25E"/>
<path d="M12 98 L104 64" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M12 98 L104 64" stroke="#B07A3A" stroke-width="3.6" stroke-linecap="round"/>
<path d="M104 64 L124 50 L122 66 L126 76Z" fill="#E8C060" {s()}/>
<path d="M108 64 L122 56 M108 68 L122 66" stroke="#B88A2A" stroke-width="2"/>
<path d="M36 84 Q34 56 62 52 Q90 52 90 74 Q90 88 62 90 Q40 92 36 84Z" fill="#E8A055" {s()}/>
<path d="M52 58 Q64 54 76 58" fill="none" stroke="#B3123A" stroke-width="5" stroke-linecap="round"/>
<path d="M52 58 Q64 54 76 58" fill="none" {W(1.6)}/>
{face(62, 74, d=10, k=0.85)}
<path d="M26 90 l-8 4 M24 80 l-10 0" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
''')

# 13. Ris cafe (ЖК «Скандинавия») — рисовая гора со снежной шапкой, зёрнышко на санках
add("cafe-ris-cafe-skandinaviya",
    "белая горка варёного риса в синей скандинавской миске, вершина как снежная шапка",
    "по склону рисовой горы на маленьких деревянных санках съезжает рисовое зёрнышко в полосатом шарфике", "k13_ice", f'''
<path d="M10 82 Q64 96 118 82 Q114 120 64 120 Q14 120 10 82Z" fill="#2F5FB3" {s()}/>
<path d="M22 100 l8 -6 l8 6 l8 -6 l8 6 l8 -6 l8 6 l8 -6 l8 6 l8 -6 l8 6" fill="none" stroke="#fff" stroke-width="2.4"/>
<path d="M16 84 Q40 34 64 22 Q88 34 112 84 Q64 94 16 84Z" fill="#FFFFFF" {s()}/>
<path d="M40 50 l3 1 M54 40 l3 -1 M72 44 l3 1 M84 58 l3 1 M30 70 l3 -1 M96 72 l3 1 M60 60 l3 1" stroke="#C9D3E0" stroke-width="2.4" stroke-linecap="round"/>
{face(64, 66, d=11, k=0.9)}
<path d="M88 48 L104 66" stroke="{O}" stroke-width="3"/>
<path d="M84 54 Q92 58 102 68" fill="none" stroke="#B07A3A" stroke-width="3.4" stroke-linecap="round"/>
<ellipse cx="92" cy="50" rx="5" ry="7" fill="#FFF8E8" transform="rotate(-40 92 50)" {W(2)}/>
<path d="M88 54 L94 46" stroke="#E8323A" stroke-width="3"/><path d="M90 56 l-6 4" stroke="#E8323A" stroke-width="2.6"/>
<circle cx="93" cy="48" r="1.2" fill="{O}"/>
''' + sparkle(22, 26, 4) + sparkle(108, 20, 3) + sparkle(116, 44, 2.4))


def main(ids):
    ids = ids or list(ICONS)
    for pid in ids:
        open(os.path.join(OUT, pid + ".svg"), "w").write(ICONS[pid])
    reg = os.path.join(OUT, "subjects.txt")
    lines = open(reg, encoding="utf-8").read().splitlines()
    have = {l.split(" — ", 1)[0] for l in lines if " — " in l}
    with open(reg, "a", encoding="utf-8") as f:
        for pid in ids:
            if pid not in have:
                h, sc = SUBJ[pid]
                f.write(f"{pid} — герой: {h} | сцена: {sc}\n")
    print("svg", len(ids))


if __name__ == "__main__":
    main(sys.argv[1:])
