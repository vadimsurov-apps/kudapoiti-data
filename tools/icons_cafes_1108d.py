"""Иконки робота cafes, 2026-11-08 (10 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно —
свой герой (блюдо/сладость по кухне и названию), своя сцена, своя компоновка и палитра. Сверено с листами
icons-catalog и icons-src/subjects.txt (герои: икра, пиде, «Наполеон», мак-энд-чиз, пармезан, рулька, утка конфи,
блинчик-конвертик, масло, пастила, щи, бочонок мёда, пицца-колесо, оливка — в реестре их не было).
Запуск: python3 tools/icons_cafes_1108d.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "d_deep": ("#BFF3FF", "#1C7FB8"), "d_bosph": ("#FFE6C9", "#E0706B"), "d_lilac": ("#FBEFFF", "#C77DDB"),
    "d_rodeo": ("#FFF3D6", "#D9813B"), "d_tusc": ("#F6FFDF", "#9CC25A"), "d_ember": ("#FFE9D2", "#B3472E"),
    "d_orange": ("#FFF8EE", "#F29A3A"), "d_tv": ("#E9E6FF", "#6A6FC8"), "d_ice": ("#F5FFFF", "#8ED8E8"),
    "d_willow": ("#FFFBEA", "#C9B27A"), "d_tsar": ("#FFE4E4", "#9E2C3C"), "d_honey": ("#FFF9D9", "#E8B23A"),
    "d_wheel": ("#E7FFF6", "#38B58A"), "d_olive": ("#F8F4FF", "#8C7FC9"),
})


def bub(x, y, r):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" fill-opacity=".55" {W(1.8)}/>'


# 1. Моремания (Каширское) — бутерброд с красной икрой ныряет с маской под воду
ICONS["cafe-moremania-kashirskoe"] = svg("d_deep", f'''
<path d="M0 34 Q16 28 32 34 T64 34 T96 34 T128 34 V128 H0Z" fill="#3FA9D6" opacity=".45"/>
<path d="M8 118 Q20 104 28 118 M100 120 Q108 102 118 118" fill="none" stroke="#2E9E6A" stroke-width="5" stroke-linecap="round"/>
<g transform="rotate(-18 62 76)">
<path d="M22 66 Q22 52 40 54 Q62 44 84 54 Q104 52 102 68 L100 98 Q62 106 26 98Z" fill="#E9B26A" {s()}/>
<path d="M30 70 Q62 60 94 70 L92 92 Q62 98 32 92Z" fill="#FFF3D9" {W(2.4)}/>
{"".join(f'<circle cx="{x}" cy="{y}" r="4.2" fill="#F0502E" {W(1.6)}/><circle cx="{x-1.3}" cy="{y-1.3}" r="1.2" fill="#fff"/>' for x, y in [(38,72),(48,68),(58,66),(68,66),(78,68),(88,72),(44,80),(84,80)])}
{face(64, 82, d=10, k=0.95)}
<rect x="44" y="70" width="40" height="15" rx="7" fill="#9BE3FF" fill-opacity=".5" {W(2.4)}/>
<path d="M44 76 Q36 74 30 70" fill="none" {W(2.4)}/>
</g>
{bub(96, 40, 5)}{bub(104, 26, 3.5)}{bub(88, 22, 2.5)}{bub(22, 46, 3)}
''')
SUBJ["cafe-moremania-kashirskoe"] = ("бутерброд с красной икрой в маске для плавания",
                                      "ныряет наискосок под воду среди пузырьков и водорослей")

# 2. Taksim — пиде-лодочка плывёт по Босфору к силуэту мечети
ICONS["cafe-taksim-columbus"] = svg("d_bosph", f'''
<circle cx="94" cy="40" r="12" fill="#FFE07A" opacity=".9"/>
<path d="M12 74 H40 V62 Q48 48 56 62 V74 H70 V56 H72 V74 H86 V60 Q92 52 98 60 V74 H116" fill="#8E4A6B" opacity=".55"/>
<path d="M58 54 V40 M71 52 V38" stroke="#8E4A6B" stroke-width="2.4" opacity=".55"/>
<path d="M0 82 Q32 76 64 82 T128 82 V128 H0Z" fill="#2F7FC1"/>
<path d="M8 96 Q20 92 32 96 M90 108 Q102 104 114 108" fill="none" stroke="#9AD3FF" stroke-width="3" stroke-linecap="round"/>
<path d="M14 82 Q16 102 40 104 H88 Q112 102 114 82 Q100 90 88 88 H40 Q28 90 14 82Z" fill="#D88A3A" {s()}/>
<path d="M30 86 Q64 76 98 86 Q86 92 64 92 Q42 92 30 86Z" fill="#FFE59A" {W(2.4)}/>
<ellipse cx="64" cy="85" rx="9" ry="5" fill="#FFB020" {W(2)}/>
{face(64, 96, d=13, k=0.9)}
''')
SUBJ["cafe-taksim-columbus"] = ("турецкое пиде — лепёшка-лодочка с сыром и желтком",
                                 "плывёт по синему Босфору на закате к силуэту мечети с минаретами")

# 3. Анненфельд — кусок торта «Наполеон» поёт в микрофон под живую музыку
layers = "".join(f'<rect x="30" y="{y}" width="56" height="9" fill="{c}" {W(2)}/>'
                 for y, c in [(52, "#F3C27A"), (61, "#FFF5DC"), (70, "#F3C27A"), (79, "#FFF5DC"), (88, "#F3C27A"), (97, "#FFF5DC")])
ICONS["cafe-annenfeld-uralskaya"] = svg("d_lilac", f'''
<path d="M10 118 H118" stroke="#8C4FA6" stroke-width="6" stroke-linecap="round" opacity=".5"/>
<rect x="28" y="50" width="60" height="58" rx="4" fill="#F3C27A" {s()}/>
{layers}
<path d="M28 50 Q30 40 40 44 Q48 36 58 44 Q68 36 76 44 Q86 38 88 50Z" fill="#FFF8EC" {W(2.6)}/>
<circle cx="40" cy="44" r="1.6" fill="#E3A65A"/><circle cx="58" cy="42" r="1.6" fill="#E3A65A"/><circle cx="76" cy="44" r="1.6" fill="#E3A65A"/>
{eye(48, 70, 0.9)}{eye(66, 70, 0.9)}
<ellipse cx="57" cy="82" rx="5" ry="6" fill="#B33A5B" {W(2.2)}/>
<path d="M96 96 L88 76" stroke="{O}" stroke-width="5" stroke-linecap="round"/>
<circle cx="86" cy="70" r="8" fill="#7A7F99" {W(2.6)}/>
<path d="M98 34 v14 M98 34 l8 -3 v14" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<circle cx="96" cy="48" r="3" fill="#fff"/><circle cx="104" cy="45" r="3" fill="#fff"/>
<path d="M18 30 v12" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/><circle cx="16" cy="42" r="3" fill="#fff"/>
''')
SUBJ["cafe-annenfeld-uralskaya"] = ("кусок слоёного торта «Наполеон» с кремовой шапкой-крошкой",
                                     "поёт в микрофон на маленькой сцене кафе, вокруг летят ноты")

# 4. TGI Fridays — мак-энд-чиз в полосатой миске закидывает сырное лассо
ICONS["cafe-tgi-fridays-kashirskoe"] = svg("d_rodeo", f'''
<path d="M0 110 Q64 100 128 110 V128 H0Z" fill="#C9874A" opacity=".5"/>
<path d="M60 58 Q70 22 92 20 Q116 20 114 36 Q110 52 90 46 Q74 42 84 30" fill="none" stroke="#FFD23F" stroke-width="5" stroke-linecap="round"/>
<path d="M60 58 Q70 22 92 20 Q116 20 114 36 Q110 52 90 46 Q74 42 84 30" fill="none" stroke="{O}" stroke-width="1.4" stroke-dasharray="1 5" opacity=".4"/>
<path d="M40 52 Q34 40 44 36 M56 46 Q52 32 62 30 M74 48 Q76 34 86 36" fill="none" stroke="#FFCA3A" stroke-width="6" stroke-linecap="round"/>
<path d="M14 66 Q16 104 64 106 Q112 104 114 66Z" fill="#3E8FD6" {s()}/>
<path d="M22 80 Q64 90 106 80" fill="none" stroke="#9FD0FF" stroke-width="3"/>
<path d="M14 66 Q20 46 38 52 Q46 40 58 48 Q68 38 78 48 Q92 42 96 52 Q110 48 114 66Z" fill="#FFCA3A" {W(2.6)}/>
{"".join(f'<path d="M{x} {y} a5 5 0 0 1 9 0" fill="none" stroke="#E8A21A" stroke-width="3.2" stroke-linecap="round"/>' for x, y in [(26,62),(40,56),(54,60),(68,54),(82,58),(96,60),(46,64),(74,64)])}
<rect x="40" y="76" width="48" height="22" rx="10" fill="#fff" opacity=".0"/>
{face(64, 86, d=13, k=1.0)}
''')
SUBJ["cafe-tgi-fridays-kashirskoe"] = ("синяя миска макарон-рожков мак-энд-чиз с тянущимся сыром",
                                        "закидывает тянущуюся сырную нитку, как ковбойское лассо, на фоне прерии")

# 5. Перчини — головка пармезана катится колесом по тосканским холмам с кипарисами
ICONS["cafe-perchini-prime-plaza"] = svg("d_tusc", f'''
<path d="M0 92 Q30 70 64 86 Q96 70 128 84 V128 H0Z" fill="#8DBA4E"/>
<path d="M0 108 Q40 94 80 104 Q104 98 128 104 V128 H0Z" fill="#6E9E3A"/>
{"".join(f'<path d="M{x} {y} Q{x-6} {y-18} {x} {y-34} Q{x+6} {y-18} {x} {y}Z" fill="#2E6B3A" {W(2)}/>' for x, y in [(16,86),(26,80),(110,82)])}
<circle cx="64" cy="70" r="34" fill="#F5D57C" {s()}/>
<circle cx="64" cy="70" r="26" fill="#FBE4A2" {W(2.2)}/>
<path d="M64 70 L98 64 A34 34 0 0 1 96 84Z" fill="#FFF2C8" {W(2.4)}/>
{"".join(f'<circle cx="{x}" cy="{y}" r="1.6" fill="#E3B54E"/>' for x, y in [(44,58),(52,92),(78,96),(40,80),(70,48)])}
{face(58, 68, d=10, k=1.0)}
<path d="M20 112 q6 -4 12 0 M36 116 q4 -3 8 0" fill="none" stroke="#FFF2C8" stroke-width="2.4" stroke-linecap="round"/>
<path d="M104 64 l8 -2 M104 72 l10 0 M104 80 l8 2" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
''')
SUBJ["cafe-perchini-prime-plaza"] = ("головка сыра пармезан с вырезанным клинышком",
                                      "катится колесом по зелёным тосканским холмам мимо кипарисов")

# 6. Жаровня — свиная рулька загорает на решётке над угольками
ICONS["cafe-zharovnya-ostrov"] = svg("d_ember", f'''
<circle cx="100" cy="28" r="12" fill="#FFE07A" {W(2.4)}/>
{"".join(f'<path d="M100 28 L{100+20*__import__("math").cos(a/57.3):.1f} {28+20*__import__("math").sin(a/57.3):.1f}" stroke="#FFE07A" stroke-width="3" stroke-linecap="round"/>' for a in range(0, 360, 45))}
<path d="M14 108 Q64 120 114 108 L106 120 H22Z" fill="#3B3355"/>
{"".join(f'<ellipse cx="{x}" cy="110" rx="7" ry="4" fill="#FF6A2B"/>' for x in (34, 52, 70, 88))}
<path d="M14 98 H114" stroke="#7A7F99" stroke-width="4" stroke-linecap="round"/>
{"".join(f'<path d="M{x} 92 V104" stroke="#7A7F99" stroke-width="3"/>' for x in range(22, 112, 12))}
<path d="M24 82 Q22 56 46 52 Q70 46 88 60 Q100 70 96 88 Q60 100 24 82Z" fill="#B85E2E" {s()}/>
<path d="M36 64 L46 86 M52 58 L62 90 M70 58 L78 90" stroke="#7E3A1A" stroke-width="3" stroke-linecap="round"/>
<path d="M92 72 L112 66" stroke="{O}" stroke-width="10" stroke-linecap="round"/><path d="M92 72 L112 66" stroke="#FFF6E2" stroke-width="5.5" stroke-linecap="round"/>
<circle cx="114" cy="62" r="5" fill="#FFF6E2" {W(2.2)}/><circle cx="116" cy="70" r="5" fill="#FFF6E2" {W(2.2)}/>
<path d="M44 70 q4 -3 8 0 M62 70 q4 -3 8 0" fill="none" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>
<path d="M50 78 Q57 84 64 78" fill="none" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>
<ellipse cx="42" cy="78" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/><ellipse cx="72" cy="78" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/>
''')
SUBJ["cafe-zharovnya-ostrov"] = ("запечённая свиная рулька на косточке",
                                  "блаженно загорает с закрытыми глазами на решётке гриля над угольками, светит солнце")

# 7. Сытая Утка (пр-т Мира) — утиная ножка конфи болтает косточкой над апельсиновым соусом
ICONS["cafe-sytaya-utka-mira"] = svg("d_orange", f'''
<ellipse cx="64" cy="102" rx="50" ry="16" fill="#fff" {s()}/>
<ellipse cx="64" cy="102" rx="36" ry="10" fill="#F7F1E6" {W(2)}/>
<ellipse cx="78" cy="104" rx="18" ry="6" fill="#FF9A2E" {W(2)}/>
<circle cx="72" cy="102" r="1.8" fill="#fff" opacity=".8"/>
<path d="M30 92 Q20 64 40 46 Q62 30 74 52 Q82 72 62 90 Q46 98 30 92Z" fill="#C9772F" {s()}/>
<path d="M40 56 Q48 50 56 54" fill="none" stroke="#F2B266" stroke-width="3" stroke-linecap="round"/>
<path d="M66 82 L90 96" stroke="{O}" stroke-width="10" stroke-linecap="round"/><path d="M66 82 L90 96" stroke="#FFF6E2" stroke-width="5.5" stroke-linecap="round"/>
<circle cx="92" cy="94" r="5" fill="#FFF6E2" {W(2.2)}/><circle cx="90" cy="101" r="5" fill="#FFF6E2" {W(2.2)}/>
{face(50, 68, d=9, k=0.95)}
<path d="M98 30 q6 -6 12 0 q-6 6 -12 0Z" fill="#7CC27A" {W(2)}/>
{sparkle(24, 30, 6)}{sparkle(110, 60, 4)}
''')
SUBJ["cafe-sytaya-utka-mira"] = ("румяная утиная ножка конфи с белой косточкой",
                                  "сидит на краю тарелки и болтает косточкой над лужицей апельсинового соуса")

# 8. Сытая Утка (Куркино) — блинчик-конвертик смотрит мультики по телевизору, укрывшись пледом
ICONS["cafe-sytaya-utka-kurkino"] = svg("d_tv", f'''
<rect x="62" y="20" width="56" height="40" rx="6" fill="#4A4F7A" {s()}/>
<rect x="68" y="25" width="44" height="30" rx="3" fill="#9FE6FF"/>
<circle cx="90" cy="40" r="7" fill="#FFD84A"/><path d="M68 55 Q80 44 90 50 Q100 44 112 55Z" fill="#7BD88F"/>
<path d="M80 60 L74 68 M100 60 L106 68" {W(3)}/>
<path d="M8 100 Q12 66 48 64 Q84 66 88 100 Z" fill="#F2C878" {s()}/>
<path d="M14 92 L48 70 L82 92" fill="none" stroke="#D99A45" stroke-width="3" stroke-linecap="round"/>
{face(48, 82, d=10, k=0.95)}
<path d="M4 98 Q48 86 94 98 L98 124 H0Z" fill="#E25C7A" {s()}/>
<path d="M14 100 L10 124 M30 96 L28 124 M48 94 V124 M66 96 L68 124 M82 98 L86 124" stroke="#fff" stroke-width="3" opacity=".7"/>
<path d="M60 100 Q46 104 40 100" fill="none" {W(2.4)}/>
''')
SUBJ["cafe-sytaya-utka-kurkino"] = ("блинчик-конвертик с утиным рагу",
                                     "смотрит мультики по телевизору в детской комнате, укрывшись полосатым пледом")

# 9. Ферма (ВДНХ) — кубик сливочного масла катается по горячему тосту, как по катку
ICONS["cafe-ferma-vdnh"] = svg("d_ice", f'''
<path d="M20 70 Q16 50 34 48 Q40 34 60 38 Q80 30 92 42 Q112 42 108 64 L104 112 H24Z" fill="#E7B467" {s()}/>
<path d="M30 70 Q28 56 40 56 Q48 46 62 50 Q78 44 86 54 Q100 54 98 70 L94 104 H34Z" fill="#FCE2A6" {W(2.4)}/>
<path d="M40 92 Q56 86 70 92 Q82 98 92 90" fill="none" stroke="#FFF6C9" stroke-width="5" stroke-linecap="round"/>
<path d="M42 96 Q60 90 88 96" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="4 4"/>
<g transform="rotate(-10 64 66)">
<path d="M46 56 L72 50 L88 60 L62 66Z" fill="#FFF7B8" {W(2.6)}/>
<path d="M46 56 L62 66 L62 86 L46 76Z" fill="#FFE97A" {W(2.6)}/>
<path d="M62 66 L88 60 L88 80 L62 86Z" fill="#FFF09A" {W(2.6)}/>
{eye(70, 70, 0.75)}{eye(81, 68, 0.75)}
<path d="M71 77 Q76 80 81 75" fill="none" {W(2.2)}/>
<path d="M52 80 L48 92 M58 84 L60 96" {W(3)}/>
<path d="M44 92 h10 M56 96 h10" stroke="#9AA6C9" stroke-width="3.4" stroke-linecap="round"/>
</g>
<path d="M30 40 q-6 -10 0 -16 M44 34 q-6 -10 0 -16" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
{sparkle(104, 30, 6)}{sparkle(112, 86, 4)}
''')
SUBJ["cafe-ferma-vdnh"] = ("кубик сливочного масла на коньках",
                            "скользит, как фигурист, по горячему румяному тосту, оставляя тающий след")

# 10. Верба (Коломенское) — пастила-брусочек под веточкой вербы с пушистыми почками
ICONS["cafe-verba-kolomenskoe"] = svg("d_willow", f'''
<path d="M14 20 Q60 26 108 10" fill="none" stroke="#7A4F2A" stroke-width="4" stroke-linecap="round"/>
<path d="M44 24 Q50 36 46 46 M76 20 Q84 32 82 44" fill="none" stroke="#7A4F2A" stroke-width="3" stroke-linecap="round"/>
{"".join(f'<ellipse cx="{x}" cy="{y}" rx="4.5" ry="6" fill="#F4F2EE" {W(1.8)} transform="rotate({r} {x} {y})"/>' for x, y, r in [(24,20,-10),(36,23,10),(60,24,-5),(92,16,15),(47,34,-20),(46,46,0),(80,30,20),(82,44,0),(102,12,-10)])}
<path d="M10 112 H118" stroke="#B08A50" stroke-width="5" stroke-linecap="round"/>
<path d="M18 104 L110 104" stroke="#8C6A38" stroke-width="7" stroke-linecap="round"/>
<path d="M24 104 V116 M104 104 V116" stroke="#8C6A38" stroke-width="5" stroke-linecap="round"/>
<path d="M26 66 L86 56 L102 66 L42 76Z" fill="#FFE3EC" {W(2.6)}/>
<path d="M26 66 L42 76 L42 100 L26 90Z" fill="#F7BFD2" {W(2.6)}/>
<path d="M42 76 L102 66 L102 90 L42 100Z" fill="#FBD3E0" {W(2.6)}/>
<path d="M46 84 L98 76 M46 92 L98 84" stroke="#F0A6C0" stroke-width="2"/>
{face(72, 82, d=10, k=0.9)}
''')
SUBJ["cafe-verba-kolomenskoe"] = ("розовая пастила-брусочек, посыпанная сахарной пудрой",
                                   "отдыхает на деревянной скамейке парка под веточкой вербы с пушистыми почками")

# 11. Борис Годунов — горшочек щей восседает на царском троне
ICONS["cafe-boris-godunov-kiselny"] = svg("d_tsar", f'''
<path d="M24 120 V40 Q24 22 44 26 Q64 10 84 26 Q104 22 104 40 V120Z" fill="#D4A23A" {s()}/>
<path d="M34 112 V44 Q34 34 46 36 Q64 24 82 36 Q94 34 94 44 V112Z" fill="#A82B3E" {W(2.6)}/>
<circle cx="64" cy="22" r="5" fill="#FFE07A" {W(2.2)}/>
<rect x="18" y="96" width="92" height="12" rx="5" fill="#D4A23A" {s()}/>
<path d="M36 64 Q34 98 64 98 Q94 98 92 64Z" fill="#B5643A" {s()}/>
<path d="M32 64 H96" stroke="{O}" stroke-width="8" stroke-linecap="round"/><path d="M32 64 H96" stroke="#C8784A" stroke-width="4" stroke-linecap="round"/>
<path d="M40 60 Q52 52 64 58 Q76 50 88 60" fill="#E7F0C8" {W(2.2)}/>
<path d="M52 56 Q56 50 62 54" fill="none" stroke="#9CC25A" stroke-width="2.4"/>
<path d="M48 48 q-4 -8 0 -14 M80 48 q-4 -8 0 -14" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
{face(64, 78, d=11, k=0.95)}
<path d="M40 90 Q64 96 88 90" fill="none" stroke="#F2D07A" stroke-width="2.4"/>
''')
SUBJ["cafe-boris-godunov-kiselny"] = ("глиняный горшочек дымящихся щей с капустным листиком",
                                       "важно восседает на золотом царском троне с красной бархатной спинкой")

# 12. Русское подворье — бочонок мёда у резных деревянных ворот подворья
ICONS["cafe-russkoe-podvorye-zyuzino"] = svg("d_honey", f'''
<path d="M6 120 V48 L22 34 L38 48 V120" fill="#9C6A36" {s()}/>
<path d="M90 120 V48 L106 34 L122 48 V120" fill="#9C6A36" {s()}/>
<path d="M22 34 Q64 4 106 34" fill="none" stroke="#9C6A36" stroke-width="8" stroke-linecap="round"/>
<path d="M22 34 Q64 4 106 34" fill="none" {W(2)}/>
{"".join(f'<circle cx="{x}" cy="{y}" r="2.4" fill="#F6D9A0"/>' for x, y in [(36,26),(50,18),(64,15),(78,18),(92,26)])}
<path d="M38 112 Q34 84 38 58 H90 Q94 84 90 112Z" fill="#C98A45" {s()}/>
<path d="M36 72 H92 M36 98 H92" stroke="#6B4523" stroke-width="5"/>
<path d="M42 58 Q40 50 50 52 Q58 44 66 52 Q76 46 84 52 Q90 50 86 58Z" fill="#FFC21E" {W(2.4)}/>
<path d="M52 58 Q50 66 54 70 Q58 66 56 58" fill="#FFC21E" {W(2)}/>
<path d="M78 50 L96 30" stroke="#8C5A2B" stroke-width="5" stroke-linecap="round"/>
<ellipse cx="74" cy="54" rx="6" ry="4" fill="#8C5A2B" {W(2)}/>
{face(64, 84, d=11, k=0.95)}
''')
SUBJ["cafe-russkoe-podvorye-zyuzino"] = ("деревянный бочонок мёда с золотой шапкой и ложкой",
                                          "встречает гостей в проёме резных деревянных ворот русского подворья")

# 13. IL Патио (Митинская) — пицца-колесо обозрения с кабинками
import math
cab = ""
for i in range(6):
    a = math.radians(i * 60 + 30)
    x, y = 64 + 38 * math.cos(a), 56 + 38 * math.sin(a)
    cab += (f'<path d="M{x:.1f} {y:.1f} v4" {W(2)}/>'
            f'<rect x="{x-7:.1f}" y="{y+4:.1f}" width="14" height="10" rx="3" fill="{["#FF8A65","#7BD88F","#FFD84A"][i % 3]}" {W(2)}/>')
ICONS["cafe-ilpatio-mitinskaya"] = svg("d_wheel", f'''
<path d="M64 56 L40 118 M64 56 L88 118" stroke="#6B7A99" stroke-width="5" stroke-linecap="round"/>
<path d="M20 118 H108" stroke="#2F8A63" stroke-width="6" stroke-linecap="round"/>
<circle cx="64" cy="56" r="36" fill="#E9A84E" {s()}/>
<circle cx="64" cy="56" r="29" fill="#E2483A" {W(2.4)}/>
{"".join(f'<path d="M64 56 L{64+29*math.cos(math.radians(a)):.1f} {56+29*math.sin(math.radians(a)):.1f}" stroke="#F3C27A" stroke-width="1.8"/>' for a in range(0, 360, 45))}
{"".join(f'<circle cx="{x}" cy="{y}" r="5" fill="#FFF8E8" {W(1.6)}/>' for x, y in [(48,40),(80,42),(46,70),(82,72)])}
<path d="M56 32 q3 -4 6 0 M78 60 q3 -4 6 0" fill="none" stroke="#3E9A4E" stroke-width="2.6" stroke-linecap="round"/>
{face(64, 54, d=9, k=0.9)}
{cab}
''')
SUBJ["cafe-ilpatio-mitinskaya"] = ("круглая пицца-маргарита — колесо обозрения",
                                    "крутится на высокой опоре, а по краю висят разноцветные кабинки")

# 14. Вино и Еда by Первый Нос — оливка с большим носом нюхает аромат из тарелки пасты
ICONS["cafe-vino-i-eda-gzhatskaya"] = svg("d_olive", f'''
<ellipse cx="64" cy="106" rx="48" ry="12" fill="#fff" {s()}/>
<path d="M34 104 Q40 88 64 90 Q88 88 94 104Z" fill="#F4D27A" {W(2.4)}/>
<path d="M40 100 Q52 92 60 100 Q70 92 80 100 Q86 96 90 102" fill="none" stroke="#E0A93A" stroke-width="2.4"/>
<circle cx="70" cy="94" r="3.4" fill="#E2483A" {W(1.6)}/>
<path d="M50 86 Q44 76 52 68 Q60 60 54 50 M64 84 Q58 72 66 64" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".9"/>
<ellipse cx="78" cy="48" rx="26" ry="32" fill="#8DB33A" {s()} transform="rotate(18 78 48)"/>
<ellipse cx="84" cy="30" rx="6" ry="4" fill="#C94A5A" {W(2)} transform="rotate(18 84 30)"/>
<path d="M78 36 q-6 0 -8 4 M94 40 q-6 0 -8 4" fill="none" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>
<path d="M76 48 Q62 54 60 62 Q64 68 74 62" fill="#B5CF63" {W(2.6)}/>
<path d="M76 70 Q82 74 88 70" fill="none" {W(2.4)}/>
<ellipse cx="94" cy="62" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/>
{sparkle(30, 40, 6)}{sparkle(22, 62, 4)}
''')
SUBJ["cafe-vino-i-eda-gzhatskaya"] = ("зелёная оливка с большим смешным носом",
                                       "зажмурившись, вдыхает аромат над тарелкой пасты с помидоркой")


if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for pid in ids:
        open(os.path.join(OUT, f"{pid}.svg"), "w").write(ICONS[pid])
    path = os.path.join(OUT, "subjects.txt")
    lines = [l for l in open(path, encoding="utf-8").read().splitlines() if l.split(" — ")[0] not in ICONS]
    lines += [f"{pid} — герой: {h} | сцена: {sc}" for pid, (h, sc) in SUBJ.items()]
    open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("svg:", len(ids))
