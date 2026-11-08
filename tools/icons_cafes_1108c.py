"""Иконки робота cafes, 2026-11-08 (07 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно —
свой герой (блюдо/сладость по кухне и названию), своя сцена, своя компоновка и палитра. Сверено с листами
icons-catalog и icons-src/subjects.txt.
Запуск: python3 tools/icons_cafes_1108c.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "k_prairie": ("#FFE3A6", "#D9603B"), "k_spring": ("#F3FFE8", "#8FD3A0"), "k_silver": ("#FFF6E8", "#B98AD9"),
    "k_brunch": ("#FFFFF0", "#B7D86A"), "k_river": ("#E9FBFF", "#3AA7C9"), "k_army": ("#F1F5E4", "#7E9455"),
    "k_marble": ("#FFF4E4", "#C99A6B"), "k_desert": ("#FFF1D6", "#E7A44A"), "k_pool": ("#E3FFFB", "#21BFC4"),
    "k_stage": ("#5A2F7A", "#1E0F33"), "k_yauza": ("#FFEFF5", "#D96C93"),
})


def note(x, y, c="#fff"):
    return (f'<ellipse cx="{x}" cy="{y}" rx="4" ry="3" fill="{c}" transform="rotate(-20 {x} {y})"/>'
            f'<path d="M{x+3.5} {y-1} V{y-13} Q{x+8} {y-11} {x+9} {y-6}" fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round"/>')


# 1. Прерия — вафля-банджо играет кантри у костра
ICONS["cafe-preriya-pershino"] = svg("k_prairie", f'''
<path d="M0 104 Q40 96 64 100 Q96 104 128 98 V128 H0Z" fill="#A8572E" opacity=".55"/>
<path d="M84 40 L108 12" {W(7)}/><path d="M84 40 L108 12" stroke="#C98A4B" stroke-width="4" stroke-linecap="round"/>
<rect x="102" y="6" width="14" height="10" rx="3" fill="#8A5A2B" {W(2.4)} transform="rotate(40 109 11)"/>
<path d="M95 26 L74 52 M99 29 L78 55 M103 32 L82 58" stroke="#fff" stroke-width="1.2" opacity=".8"/>
<circle cx="54" cy="70" r="34" fill="#F2B54E" {s()}/>
<circle cx="54" cy="70" r="26" fill="#FFD47A" {W(2.4)}/>
<path d="M34 56 H74 M30 66 H78 M30 76 H78 M34 86 H74 M40 48 V92 M50 45 V95 M60 45 V95 M70 48 V92" stroke="#E39B37" stroke-width="2.2"/>
{face(54, 68, d=10, k=1.05)}
<path d="M44 96 Q54 102 64 96" fill="none" stroke="#8A5A2B" stroke-width="3"/>
<path d="M14 116 Q20 104 24 112 Q28 100 32 114 Z" fill="#FF8A3C" {W(2)}/>
<path d="M10 120 H38" stroke="#6B3F1F" stroke-width="4" stroke-linecap="round"/>
{note(18, 38)}{note(100, 66)}{note(28, 22, "#FFF3C4")}
''')
SUBJ["cafe-preriya-pershino"] = ("вафля-банджо с круглым корпусом и деревянным грифом",
                                  "играет кантри на закате в прерии у маленького костра, вокруг разлетаются ноты")

# 2. Апрель — башенка из луковых колец, на верхнем кольце пробился подснежник
rings = ""
for i, (y, rx) in enumerate([(104, 34), (88, 31), (72, 28)]):
    rings += (f'<ellipse cx="64" cy="{y}" rx="{rx}" ry="12" fill="#E9A83E" {s()}/>'
              f'<ellipse cx="64" cy="{y-1}" rx="{rx-12}" ry="5" fill="#B8E0B0" {W(2.4)}/>'
              f'<path d="M{64-rx+6} {y+3} q4 3 8 1 M{64+rx-14} {y+4} q4 -2 8 0" stroke="#FFD27A" stroke-width="2" fill="none"/>')
ICONS["cafe-aprel-ivanovskoe"] = svg("k_spring", f'''
<path d="M0 112 Q64 104 128 112 V128 H0Z" fill="#7CC27A"/>
{rings}
<path d="M64 70 V40" stroke="#4BA35A" stroke-width="4" stroke-linecap="round"/>
<path d="M64 56 Q50 50 46 38 Q60 40 64 52" fill="#6CC46A" {W(2.4)}/>
<path d="M64 40 Q56 30 60 18 Q66 24 64 40 Q72 28 70 18 Q60 24 64 40" fill="#FFFFFF" {W(2.6)}/>
<path d="M62 22 Q64 30 66 22" fill="none" stroke="#9AD49C" stroke-width="2"/>
{face(64, 84, d=10, k=1.0)}
{sparkle(24, 40, 6)}{sparkle(104, 30, 5)}
<circle cx="98" cy="54" r="4" fill="#fff" opacity=".8"/><circle cx="30" cy="64" r="3" fill="#fff" opacity=".8"/>
''')
SUBJ["cafe-aprel-ivanovskoe"] = ("башенка из трёх хрустящих луковых колец",
                                  "сквозь верхнее кольцо пробился первый весенний подснежник на апрельской лужайке")

# 3. Голицын — серебряный клош приподнимается, под ним румяная курочка
ICONS["cafe-golitsyn-m1"] = svg("k_silver", f'''
<ellipse cx="64" cy="104" rx="52" ry="12" fill="#FFFFFF" {s()}/>
<ellipse cx="64" cy="102" rx="38" ry="7" fill="#EDE6F7"/>
<path d="M30 100 Q28 70 56 66 Q86 62 96 82 Q102 96 94 100Z" fill="#E08A3A" {s()}/>
<path d="M88 76 Q100 62 108 70 Q104 78 96 82" fill="#E08A3A" {s()}/>
<circle cx="108" cy="68" r="5" fill="#FFF6E8" {W(2.4)}/>
<path d="M40 84 Q50 78 60 86" fill="none" stroke="#B9652A" stroke-width="2.4"/>
{face(58, 84, d=9, k=0.95)}
<g transform="rotate(-24 22 60)">
<path d="M10 60 Q10 18 54 18 Q98 18 98 60Z" fill="#D9DEE8" {s()}/>
<path d="M22 54 Q24 30 46 26" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".8"/>
<path d="M6 60 H102" {W(4)}/>
<circle cx="54" cy="13" r="6" fill="#C2C8D6" {s()}/>
</g>
{sparkle(104, 30, 6)}{sparkle(114, 50, 3.5)}
''')
SUBJ["cafe-golitsyn-m1"] = ("румяная жареная курочка на блюде под серебряным клошем",
                             "крышка-клош сама приподнимается наискосок, курочка выглядывает и улыбается")

# 4. Целеево — яйцо Бенедикт на английском маффине, соус стекает
ICONS["cafe-tseleevo"] = svg("k_brunch", f'''
<ellipse cx="64" cy="110" rx="50" ry="9" fill="#fff" {W(2.6)}/>
<path d="M22 92 Q22 80 64 80 Q106 80 106 92 V100 Q106 108 64 108 Q22 108 22 100Z" fill="#E7B46A" {s()}/>
<circle cx="40" cy="96" r="1.6" fill="#B97E3A"/><circle cx="60" cy="102" r="1.6" fill="#B97E3A"/><circle cx="86" cy="97" r="1.6" fill="#B97E3A"/>
<path d="M26 82 Q64 72 102 82 L100 88 Q64 80 28 88Z" fill="#F08AA0" {W(2.4)}/>
<ellipse cx="64" cy="62" rx="36" ry="24" fill="#FFFFFF" {s()}/>
<path d="M30 56 Q36 36 64 36 Q92 36 98 56 Q98 64 94 64 Q92 74 88 64 Q84 60 78 66 Q76 80 72 66 Q64 60 56 66 Q54 78 50 66 Q44 60 38 66 Q34 72 32 64 Q28 62 30 56Z" fill="#FFC93C" {s()}/>
<path d="M44 44 Q52 40 60 42" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
{face(64, 52, d=10, k=1.0)}
<path d="M74 34 Q78 26 76 20" fill="none" stroke="#5BAA4A" stroke-width="3" stroke-linecap="round"/>
<circle cx="76" cy="20" r="3" fill="#6CC46A"/>
{sparkle(20, 36, 6)}{sparkle(110, 40, 4)}
''')
SUBJ["cafe-tseleevo"] = ("яйцо Бенедикт на английском маффине с ломтиком ветчины",
                          "голландский соус стекает с макушки фестонами, как скатерть на воскресном бранче")

# 5. Веретьево — пломбир в вафельном стаканчике отдыхает в шезлонге у реки
ICONS["cafe-veretevo-taldom"] = svg("k_river", f'''
<path d="M0 86 Q32 80 64 86 Q96 92 128 86 V128 H0Z" fill="#2E8FB8"/>
<path d="M10 96 q8 -4 16 0 M60 104 q8 -4 16 0 M96 94 q8 -4 16 0" stroke="#BFEFFF" stroke-width="2.4" fill="none" stroke-linecap="round"/>
<rect x="0" y="108" width="128" height="20" fill="#C98A4B"/>
<path d="M0 116 H128" stroke="#A86E35" stroke-width="2"/>
<path d="M22 112 L44 66 M106 112 L84 70 M30 96 L98 96" {W(4)}/>
<path d="M40 62 L92 66 L100 104 L28 100Z" fill="#fff" {s()}/>
<path d="M44 63 L38 101 M56 64 L52 102 M68 65 L66 103 M80 66 L80 103" stroke="#3FB0E0" stroke-width="6"/>
<path d="M40 62 L92 66 L100 104 L28 100Z" fill="none" {s()}/>
<path d="M50 90 L54 60 H82 L86 90Z" fill="#E7B46A" {s()}/>
<path d="M56 68 H80 M55 76 H82 M54 84 H84" stroke="#C98A4B" stroke-width="2"/>
<path d="M50 60 Q48 36 68 34 Q90 36 86 60Z" fill="#FFF8E8" {s()}/>
{face(68, 48, d=8, k=0.9)}
<path d="M58 34 Q64 24 74 28 Q80 22 84 30" fill="none" stroke="#FFF8E8" stroke-width="0"/>
<circle cx="108" cy="24" r="12" fill="#FFD84A" {W(2.4)}/>
{sparkle(20, 30, 5)}
''')
SUBJ["cafe-veretevo-taldom"] = ("пломбир в вафельном стаканчике",
                                 "отдыхает в полосатом шезлонге на деревянном причале у реки под летним солнцем")

# 6. Гвардеец — гречневая каша в солдатском котелке марширует, ложка на плече как ружьё
ICONS["cafe-gvardeets-kubinka"] = svg("k_army", f'''
<path d="M0 110 H128 V128 H0Z" fill="#A9B77A"/>
<path d="M14 110 V100 M34 110 V100 M94 110 V100 M114 110 V100" stroke="#8A9A5B" stroke-width="3"/>
<path d="M48 104 L42 120 M80 104 L88 118" {W(6)}/>
<ellipse cx="40" cy="121" rx="8" ry="4" fill="#3B3355"/><ellipse cx="90" cy="119" rx="8" ry="4" fill="#3B3355"/>
<path d="M28 50 Q64 14 100 50" fill="none" {W(3)}/>
<path d="M26 54 H102 L98 98 Q96 108 64 108 Q32 108 30 98Z" fill="#6E8B4E" {s()}/>
<path d="M34 60 Q38 84 36 100" fill="none" stroke="#9DB57A" stroke-width="4" stroke-linecap="round"/>
<ellipse cx="64" cy="54" rx="38" ry="10" fill="#9A6A3A" {s()}/>
<circle cx="50" cy="52" r="2" fill="#6B4523"/><circle cx="62" cy="50" r="2" fill="#6B4523"/><circle cx="76" cy="53" r="2" fill="#6B4523"/><circle cx="56" cy="56" r="2" fill="#6B4523"/><circle cx="70" cy="56" r="2" fill="#6B4523"/>
<path d="M96 60 L118 14" {W(6)}/><path d="M96 60 L118 14" stroke="#D9DEE8" stroke-width="3.4" stroke-linecap="round"/>
<ellipse cx="119" cy="10" rx="6" ry="9" fill="#D9DEE8" {W(2.6)} transform="rotate(26 119 10)"/>
{face(62, 80, d=11, k=1.05)}
<path d="M44 66 L52 70 M80 70 L88 66" {W(2.6)}/>
''')
SUBJ["cafe-gvardeets-kubinka"] = ("гречневая каша в зелёном солдатском котелке",
                                   "марширует по плацу строевым шагом, на плече вместо ружья — алюминиевая ложка")

# 7. Ренессанс — фруктовый лёд-трёхцветка в лавровом венке на мраморной колонне
ICONS["cafe-renessans-smena"] = svg("k_marble", f'''
<path d="M40 128 V96 H88 V128" fill="#F7F1EA" {s()}/>
<path d="M50 98 V128 M64 98 V128 M78 98 V128" stroke="#D9CFC2" stroke-width="3"/>
<rect x="32" y="88" width="64" height="10" rx="3" fill="#FFFFFF" {s()}/>
<path d="M62 92 V76" {W(6)}/><path d="M62 92 V74" stroke="#E7C79A" stroke-width="3.4" stroke-linecap="round"/>
<path d="M40 30 Q40 16 62 16 Q84 16 84 30 V72 Q84 78 78 78 H46 Q40 78 40 72Z" fill="#FF6B6B" {s()}/>
<path d="M41 44 H83 V58 H41Z" fill="#FFE066"/><path d="M41 58 H83 V72 Q83 77 78 77 H46 Q41 77 41 72Z" fill="#7BD88F"/>
<path d="M40 30 Q40 16 62 16 Q84 16 84 30 V72 Q84 78 78 78 H46 Q40 78 40 72Z" fill="none" {s()}/>
<path d="M48 26 V40" stroke="#fff" stroke-width="3.4" stroke-linecap="round" opacity=".8"/>
{face(62, 48, d=9, k=0.95)}
<path d="M38 22 Q62 6 86 22" fill="none" stroke="#4E8F3A" stroke-width="3"/>
<g fill="#6CB84F" {W(1.8)}>
<ellipse cx="42" cy="18" rx="6" ry="3" transform="rotate(-50 42 18)"/><ellipse cx="50" cy="12" rx="6" ry="3" transform="rotate(-25 50 12)"/>
<ellipse cx="74" cy="12" rx="6" ry="3" transform="rotate(25 74 12)"/><ellipse cx="82" cy="18" rx="6" ry="3" transform="rotate(50 82 18)"/>
</g>
{sparkle(104, 40, 6, "#FFF6C4")}{sparkle(22, 56, 4, "#FFF6C4")}
''')
SUBJ["cafe-renessans-smena"] = ("фруктовый лёд-трёхцветка на палочке",
                                 "стоит на мраморной колонне, как античная статуя, на макушке — лавровый венок")

# 8. Шёлковый путь — слоёная катлама-розочка, по шёлковой ленте идёт караван
ICONS["cafe-shelkovy-put-yakhroma"] = svg("k_desert", f'''
<path d="M0 98 Q30 86 60 96 Q92 106 128 92 V128 H0Z" fill="#F2C27A"/>
<path d="M-4 116 Q40 100 70 112 Q100 122 132 104" fill="none" stroke="#C9497A" stroke-width="7" stroke-linecap="round"/>
<path d="M-4 116 Q40 100 70 112 Q100 122 132 104" fill="none" stroke="#FF8FB8" stroke-width="2.4" stroke-linecap="round"/>
<g fill="#8A5A2B">
<path d="M88 92 q2 -8 6 -4 q3 -6 6 0 l3 -2 l2 3 l-3 2 v6 h-2 v-4 h-8 v4 h-2Z"/>
<path d="M104 86 q2 -6 5 -3 q2 -5 5 0 l2 -2 l2 2 l-2 2 v5 h-2 v-3 h-6 v3 h-2Z"/>
</g>
<circle cx="56" cy="58" r="40" fill="#E9A85A" {s()}/>
<circle cx="56" cy="58" r="30" fill="#F4C27A" {W(2.4)}/>
<path d="M56 28 Q74 30 82 44 Q86 62 74 78 Q58 90 40 80 Q28 70 30 54 Q34 40 48 36 Q64 34 70 46 Q74 60 64 70 Q52 76 44 66 Q40 54 50 48 Q60 46 62 56" fill="none" stroke="#C97A2E" stroke-width="3" stroke-linecap="round"/>
<circle cx="42" cy="40" r="1.6" fill="#3B3355"/><circle cx="72" cy="36" r="1.6" fill="#3B3355"/><circle cx="80" cy="70" r="1.6" fill="#3B3355"/><circle cx="36" cy="72" r="1.6" fill="#3B3355"/>
{face(56, 58, d=11, k=1.05)}
<circle cx="104" cy="22" r="10" fill="#FFF3C4" {W(2.2)}/>
''')
SUBJ["cafe-shelkovy-put-yakhroma"] = ("слоёная узбекская катлама, свёрнутая розочкой",
                                       "встаёт солнцем над барханами, по шёлковой розовой ленте-дороге идёт караван верблюдов")

# 9. Манго — кусок мангового чизкейка катается на надувном круге в бассейне
ICONS["cafe-mango-egorevsk"] = svg("k_pool", f'''
<path d="M0 74 Q32 68 64 74 Q96 80 128 74 V128 H0Z" fill="#5AD4E6"/>
<path d="M14 92 q8 -4 16 0 M92 100 q8 -4 16 0 M50 116 q8 -4 16 0" stroke="#fff" stroke-width="2.4" fill="none" stroke-linecap="round"/>
<ellipse cx="64" cy="88" rx="50" ry="18" fill="#FF6FA0" {s()}/>
<path d="M22 84 L30 98 M58 70 L58 76 M98 80 L104 96" stroke="#fff" stroke-width="7"/>
<ellipse cx="64" cy="86" rx="28" ry="8" fill="#5AD4E6" {W(2.6)}/>
<path d="M34 80 L62 22 L96 80Z" fill="#FFF3D6" {s()}/>
<path d="M50 46 L62 22 L74 48 Q62 52 50 46Z" fill="#FFB52E" {s()}/>
<path d="M34 80 H96 V86 H34Z" fill="#E0A45A" {W(2.6)}/>
<path d="M58 30 L56 40" stroke="#fff" stroke-width="2.6" stroke-linecap="round" opacity=".8"/>
{face(66, 64, d=8, k=0.9)}
<circle cx="106" cy="24" r="11" fill="#FFD84A" {W(2.4)}/>
{sparkle(22, 30, 6)}
''')
SUBJ["cafe-mango-egorevsk"] = ("треугольный кусок чизкейка с оранжевым манговым желе",
                                "катается на розовом надувном круге по бирюзовому бассейну")

# 10. Burgerock — бургер с ирокезом из салата поёт в микрофон на сцене под софитами
ICONS["cafe-burgerock-ramenskoe"] = svg("k_stage", f'''
<path d="M20 0 L44 120 H84 L108 0" fill="#FFF3A6" opacity=".18"/>
<rect x="0" y="108" width="128" height="20" fill="#3A2550"/>
<path d="M0 108 H128" stroke="#FF5CA8" stroke-width="3"/>
<path d="M26 92 Q26 64 64 64 Q102 64 102 92Z" fill="#F2B04E" {s()}/>
<ellipse cx="50" cy="74" rx="2" ry="1.2" fill="#fff"/><ellipse cx="66" cy="70" rx="2" ry="1.2" fill="#fff"/><ellipse cx="82" cy="75" rx="2" ry="1.2" fill="#fff"/>
<path d="M40 66 L36 44 L46 60 L48 38 L56 60 L60 34 L66 60 L72 36 L76 60 L84 40 L86 64" fill="#6CD45A" {s()}/>
<path d="M22 94 H106 Q104 100 64 100 Q24 100 22 94Z" fill="#8A4A2A" {s()}/>
<path d="M24 92 Q40 98 54 92 Q68 98 82 92 Q94 98 104 92" fill="#FFD23C" {W(2.2)}/>
<path d="M26 102 H102 Q102 112 64 112 Q26 112 26 102Z" fill="#F2B04E" {s()}/>
{face(64, 80, d=9, k=0.9, mouth=False)}
<ellipse cx="64" cy="89" rx="4" ry="3.2" fill="#3B3355"/>
<path d="M88 86 L104 70" {W(5)}/>
<circle cx="108" cy="64" r="8" fill="#5A5A6A" {s()}/>
<path d="M104 60 L112 68 M104 66 L110 60" stroke="#8C8CA0" stroke-width="1.6"/>
{sparkle(20, 24, 6, "#FFF3A6")}{sparkle(108, 24, 5, "#FFB3D9")}
<path d="M14 54 l4 8 M18 48 l8 4" stroke="#FFF3A6" stroke-width="2.4" stroke-linecap="round"/>
''')
SUBJ["cafe-burgerock-ramenskoe"] = ("бургер-рокер с ирокезом из листьев салата",
                                     "поёт в микрофон на тёмной сцене под лучом прожектора")

# 11. АндерСон «Каскад» — трёхъярусный торт, с ярусов каскадом льётся шоколад
ICONS["cafe-anderson-kaskad"] = svg("k_yauza", f'''
<path d="M0 112 Q64 104 128 112 V128 H0Z" fill="#E7C6D4"/>
<ellipse cx="64" cy="112" rx="50" ry="8" fill="#fff" {s()}/>
<rect x="22" y="80" width="84" height="30" rx="6" fill="#FFE2EC" {s()}/>
<rect x="34" y="54" width="60" height="28" rx="6" fill="#FFF6E8" {s()}/>
<rect x="46" y="30" width="36" height="26" rx="6" fill="#FFE2EC" {s()}/>
<path d="M46 34 Q46 30 52 30 H76 Q82 30 82 34 V38 Q78 44 76 38 Q72 46 68 38 Q64 50 60 38 Q56 44 52 38 Q48 42 46 38Z" fill="#7A4326" {W(2.4)}/>
<path d="M34 58 Q34 54 40 54 H88 Q94 54 94 58 V62 Q90 70 86 62 Q80 74 76 62 Q70 70 64 62 Q58 76 52 62 Q46 70 42 62 Q38 68 34 62Z" fill="#7A4326" {W(2.4)}/>
<path d="M22 84 Q22 80 28 80 H100 Q106 80 106 84 V88 Q102 96 98 88 Q92 100 86 88 Q78 96 72 88 Q64 102 58 88 Q50 96 44 88 Q36 98 30 88 Q26 94 22 88Z" fill="#7A4326" {W(2.4)}/>
<circle cx="64" cy="24" r="6" fill="#E8304A" {W(2.4)}/><path d="M64 18 Q66 12 70 12" fill="none" stroke="#4BA35A" stroke-width="2.4" stroke-linecap="round"/>
{face(64, 98, d=11, k=1.05)}
<circle cx="50" cy="70" r="2" fill="#FF7FA8"/><circle cx="78" cy="72" r="2" fill="#7BD88F"/><circle cx="64" cy="74" r="2" fill="#FFC93C"/>
{sparkle(20, 40, 6)}{sparkle(108, 46, 5)}
''')
SUBJ["cafe-anderson-kaskad"] = ("трёхъярусный бисквитный торт с клубникой на макушке",
                                 "шоколадная глазурь льётся каскадом с яруса на ярус, как вода в фонтане")


if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for pid in ids:
        open(os.path.join(OUT, f"{pid}.svg"), "w").write(ICONS[pid])
    path = os.path.join(OUT, "subjects.txt")
    lines = [l for l in open(path, encoding="utf-8").read().splitlines() if l.split(" — ")[0] not in ICONS]
    lines += [f"{pid} — герой: {h} | сцена: {sc}" for pid, (h, sc) in SUBJ.items()]
    open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("svg:", len(ids))
