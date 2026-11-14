"""Иконки робота rare 14.11 (1114f). Каждая придумана и нарисована отдельно (правило абсолютной уникальности):
свой герой, своя сцена, своя компоновка и палитра.  python3 tools/icons_rare_1114f.py [id ...]"""
import os
from draw_icons import s, eye, face, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def svg(a, b, body, cx="38%", cy="28%"):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
<defs>
 <radialGradient id="g" cx="{cx}" cy="{cy}" r="85%"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></radialGradient>
 <clipPath id="c"><circle cx="64" cy="64" r="61"/></clipPath>
</defs>
<circle cx="64" cy="64" r="61" fill="url(#g)"/>
<g clip-path="url(#c)">{body}</g>
<ellipse cx="44" cy="22" rx="20" ry="7" fill="#fff" opacity=".3"/>
</svg>'''


I = {}

# 1. IceZubrus у ЦСКА (хоккей для малышей 4–11 лет): пухлая белая полярная куропатка в красно-синем свитере и синем шлеме
#    ведёт шайбу крюком большой жёлтой клюшки по льду, из-под крюка летят ледяные искры; фон алый, внизу лёд
I["icezubrus-cska"] = svg("#FF8A80", "#B71C1C", f'''
<path d="M-4 96 Q64 88 132 96 V132 H-4Z" fill="#EAF6FF" {s('stroke-width="2.4"')}/>
<path d="M14 108 H44 M78 116 H112" stroke="#BCDDF2" stroke-width="2.6" stroke-linecap="round"/>
<ellipse cx="46" cy="70" rx="26" ry="22" fill="#FFFFFF" {s()}/>
<path d="M24 66 Q46 54 70 66 L70 80 Q46 92 24 80Z" fill="#D32F2F" {s('stroke-width="2.6"')}/>
<path d="M26 72 Q46 64 68 72" fill="none" stroke="#1E40AF" stroke-width="4"/>
<path d="M28 60 Q14 64 12 76 Q22 74 30 70Z" fill="#FFFFFF" {s('stroke-width="2.4"')}/>
<circle cx="56" cy="42" r="15" fill="#FFFFFF" {s()}/>
<path d="M42 38 Q44 22 58 24 Q72 26 70 40 Q56 34 42 38Z" fill="#1E40AF" {s('stroke-width="2.6"')}/>
<path d="M50 28 Q58 26 64 30" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" opacity=".8"/>
<path d="M70 42 L80 45 L70 48Z" fill="#37474F" {s('stroke-width="2"')}/>
{eye(61, 43, .8)}
<ellipse cx="57" cy="50" rx="3.6" ry="2.2" fill="#FF7FA8" opacity=".7"/>
<path d="M58 22 Q60 14 66 16" fill="none" {s('stroke-width="2.4"')}/>
<path d="M40 90 L38 98 M52 90 L54 98" {s('stroke-width="3"')}/>
<path d="M32 99 H42 M50 99 H60" stroke="#E53935" stroke-width="3" stroke-linecap="round"/>
<path d="M70 62 L96 98 H116" fill="none" stroke="{O}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M70 62 L96 98 H116" fill="none" stroke="#FBC02D" stroke-width="4.4" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M98 100 H114" stroke="#263238" stroke-width="2.4" stroke-linecap="round"/>
<ellipse cx="98" cy="110" rx="10" ry="4" fill="#212121"/>
<rect x="88" y="105" width="20" height="5" fill="#212121"/>
<ellipse cx="98" cy="105" rx="10" ry="4" fill="#424242"/>
{sparkle(118, 88, 3)}{sparkle(110, 80, 2.4)}{sparkle(122, 104, 2)}
''', cx="30%", cy="22%")

# 2. «Невские медведи», Нагатинская (волейбол 9–17 лет): лохматый чёрный медведь-губач со светлой мордой и белой «галочкой»
#    на груди в высоком прыжке ставит блок над белой сеткой обеими лапами — жёлто-синий мяч отскакивает от лап; фон мандариновый
I["nevsky-bears-nagatinskaya"] = svg("#FFE0B2", "#F57C00", f'''
<path d="M42 70 Q30 52 34 34 Q36 26 42 28 Q46 30 46 38 L52 62Z" fill="#2B2B33" {s()}/>
<path d="M78 70 Q92 50 94 30 Q94 22 88 22 Q82 22 82 30 L72 62Z" fill="#2B2B33" {s()}/>
<path d="M36 30 q2 -8 6 -6 M40 30 q4 -6 6 -2 M86 24 q2 -8 6 -4 M90 26 q4 -4 5 0" fill="none" stroke="#E8D5B5" stroke-width="2.4" stroke-linecap="round"/>
<path d="M30 112 Q24 84 38 70 Q50 60 60 60 Q72 60 84 70 Q98 84 90 112Z" fill="#2B2B33" {s()}/>
<circle cx="44" cy="56" r="6" fill="#2B2B33" {s('stroke-width="2.4"')}/><circle cx="76" cy="56" r="6" fill="#2B2B33" {s('stroke-width="2.4"')}/>
<circle cx="60" cy="70" r="16" fill="#2B2B33" {s()}/>
<path d="M50 72 Q60 64 70 72 Q72 82 60 84 Q48 82 50 72Z" fill="#E8D5B5" {s('stroke-width="2.4"')}/>
<ellipse cx="60" cy="73" rx="4.4" ry="3" fill="{O}"/>
<path d="M56 78 Q60 81 64 78" fill="none" {s('stroke-width="2"')}/>
{eye(53, 64, .7)}{eye(67, 64, .7)}
<path d="M46 94 L60 104 L74 94" fill="none" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="-4" y="88" width="136" height="8" fill="#FFFFFF" {s('stroke-width="2.4"')}/>
<path d="M4 96 V132 M20 96 V132 M36 96 V132 M52 96 V132 M68 96 V132 M84 96 V132 M100 96 V132 M116 96 V132 M-4 106 H132 M-4 118 H132"
 stroke="#FFFFFF" stroke-width="1.6" opacity=".85"/>
<circle cx="66" cy="16" r="13" fill="#FFD54F" {s()}/>
<path d="M54 12 Q66 20 78 14 M60 28 Q64 16 62 4 M72 28 Q70 16 76 6" fill="none" stroke="#1E5AC8" stroke-width="2.6"/>
<circle cx="66" cy="16" r="13" fill="none" {s()}/>
<path d="M84 8 l6 -3 M86 14 l7 0 M84 20 l6 3" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
''', cx="60%", cy="25%")

# 3. «Полюс Арена», Горки-2 (массовое катание с «помощником фигуриста»): северный оленёнок с золотыми рожками и красным
#    вязаным шарфом осторожно едет по льду, держась передними копытцами за синюю раму-помощника; фон сумеречный бирюзовый лес
I["rink-polyus-arena-gorki2"] = svg("#B2EBF2", "#00838F", f'''
<path d="M6 70 L16 44 L26 70Z M100 72 L112 40 L124 72Z M86 66 L94 48 L102 66Z" fill="#00695C" opacity=".75"/>
<path d="M-4 86 Q64 78 132 86 V132 H-4Z" fill="#F2FBFF" {s('stroke-width="2.4"')}/>
<path d="M10 100 Q30 96 50 100 M76 112 Q96 108 116 112" stroke="#BFE6F2" stroke-width="3" stroke-linecap="round" fill="none"/>
<path d="M76 58 H112 M80 58 L76 98 M108 58 L112 98 M76 80 H112" fill="none" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M76 58 H112 M80 58 L76 98 M108 58 L112 98 M76 80 H112" fill="none" stroke="#1E88E5" stroke-width="3.6" stroke-linecap="round"/>
<ellipse cx="50" cy="72" rx="24" ry="15" fill="#A1673F" {s()}/>
<ellipse cx="48" cy="78" rx="14" ry="7" fill="#F3E0C8"/>
<path d="M34 84 L32 98 M44 86 L44 98 M58 86 L60 98" {s('stroke-width="5"')}/>
<path d="M34 84 L32 98 M44 86 L44 98 M58 86 L60 98" stroke="#A1673F" stroke-width="2.6"/>
<path d="M26 100 H38 M38 100 H50 M54 100 H66" stroke="#C9D3E0" stroke-width="3" stroke-linecap="round"/>
<path d="M66 66 L82 62" {s('stroke-width="6"')}/><path d="M66 66 L82 62" stroke="#A1673F" stroke-width="3"/>
<circle cx="83" cy="62" r="3" fill="{O}"/>
<path d="M60 64 Q62 44 70 40" fill="none" {s('stroke-width="12"')}/><path d="M60 64 Q62 44 70 40" fill="none" stroke="#A1673F" stroke-width="8"/>
<ellipse cx="70" cy="34" rx="13" ry="11" fill="#A1673F" {s()}/>
<ellipse cx="80" cy="38" rx="6" ry="5" fill="#F3E0C8" {s('stroke-width="2"')}/>
<ellipse cx="84" cy="37" rx="2.6" ry="2" fill="#3E2723"/>
{eye(70, 31, .8)}
<path d="M60 26 Q52 20 54 30Z" fill="#A1673F" {s('stroke-width="2"')}/>
<path d="M64 24 Q58 12 50 10 M58 16 L52 18 M68 23 Q72 10 80 8 M74 14 L80 16" fill="none" stroke="{O}" stroke-width="5" stroke-linecap="round"/>
<path d="M64 24 Q58 12 50 10 M58 16 L52 18 M68 23 Q72 10 80 8 M74 14 L80 16" fill="none" stroke="#FFC107" stroke-width="2.6" stroke-linecap="round"/>
<path d="M58 48 Q68 54 76 46 L78 52 Q68 60 58 54Z" fill="#E53935" {s('stroke-width="2.2"')}/>
<path d="M60 54 L56 66 L62 66Z" fill="#E53935" {s('stroke-width="2"')}/>
{sparkle(30, 26, 3)}{sparkle(98, 22, 2.6)}
''', cx="50%", cy="15%")

# 4. Zavadovskaya.club, Крылатское (горные лыжи с 2,5 лет): чёрная альпийская галка с жёлтым клювом и красными лапками в
#    оранжевой горнолыжной маске съезжает «плугом» на маленьких красных лыжах между двумя флажками-воротами; фон голубое небо с солнцем
I["ski-zavadovskaya-krylatskoe"] = svg("#E1F5FE", "#4FC3F7", f'''
<circle cx="104" cy="24" r="12" fill="#FFEB3B" opacity=".95"/>
<path d="M-4 54 Q40 60 132 112 V132 H-4Z" fill="#FFFFFF" {s('stroke-width="2.4"')}/>
<path d="M10 74 Q30 78 44 86 M70 104 Q86 110 96 118" fill="none" stroke="#D6ECF7" stroke-width="3" stroke-linecap="round"/>
<path d="M20 62 V88" {s('stroke-width="2.6"')}/><path d="M20 63 L34 68 L20 73Z" fill="#E53935" {s('stroke-width="2"')}/>
<path d="M104 92 V118" {s('stroke-width="2.6"')}/><path d="M104 93 L118 98 L104 103Z" fill="#1E88E5" {s('stroke-width="2"')}/>
<path d="M36 112 L66 98 M90 112 L66 98" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M36 112 L66 98 M90 112 L66 98" stroke="#E53935" stroke-width="4" stroke-linecap="round"/>
<path d="M56 98 L54 106 M76 98 L78 106" stroke="#E65100" stroke-width="3" stroke-linecap="round"/>
<path d="M50 104 L58 106 M74 106 L82 104" stroke="#E65100" stroke-width="2.4" stroke-linecap="round"/>
<ellipse cx="66" cy="78" rx="18" ry="20" fill="#1F1F27" {s()}/>
<path d="M50 74 Q38 82 40 94 Q48 88 54 84Z M82 74 Q94 82 92 94 Q84 88 78 84Z" fill="#2D2D38" {s('stroke-width="2.4"')}/>
<circle cx="66" cy="50" r="14" fill="#1F1F27" {s()}/>
<rect x="53" y="42" width="26" height="11" rx="5.5" fill="#FF9800" {s('stroke-width="2.4"')}/>
<path d="M53 46 Q46 46 46 52 M79 46 Q86 46 86 52" fill="none" stroke="#FF9800" stroke-width="2.4"/>
<path d="M58 46 Q62 44 66 46" fill="none" stroke="#FFF3E0" stroke-width="2" stroke-linecap="round"/>
<path d="M62 56 L66 66 L70 56Z" fill="#FFD600" {s('stroke-width="2"')}/>
<ellipse cx="57" cy="58" rx="3" ry="1.8" fill="#FF7FA8" opacity=".6"/><ellipse cx="75" cy="58" rx="3" ry="1.8" fill="#FF7FA8" opacity=".6"/>
''', cx="70%", cy="18%")

# 5. «Диксодром», Измайлово (картинг с 5 лет): маленький жёлтый детский карт с крупной «5» на носу и фарами-глазками, в нём
#    малыш-пилот в синем шлеме; карт входит в поворот у красно-белого поребрика, из-под колёс облачко пыли, сверху клетчатый
#    флажок; фон закатный малиновый
I["karting-dixxodrom-izmailovo"] = svg("#F8BBD0", "#AD1457", f'''
<path d="M-4 92 H132 V132 H-4Z" fill="#5B5B66" {s('stroke-width="2.4"')}/>
<path d="M-4 92 H16 V100 H-4Z M32 92 H48 V100 H32Z M64 92 H80 V100 H64Z M96 92 H112 V100 H96Z" fill="#E53935"/>
<path d="M16 92 H32 V100 H16Z M48 92 H64 V100 H48Z M80 92 H96 V100 H80Z M112 92 H132 V100 H112Z" fill="#FFFFFF"/>
<path d="M-4 100 H132" {s('stroke-width="2"')}/>
<path d="M20 116 H44 M70 122 H96" stroke="#FFFFFF" stroke-width="3" stroke-dasharray="8 6" opacity=".7"/>
<path d="M92 14 V44" {s('stroke-width="2.6"')}/>
<rect x="92" y="14" width="24" height="16" fill="#FFFFFF" {s('stroke-width="2.2"')}/>
<path d="M92 14 h6 v4 h-6Z M104 14 h6 v4 h-6Z M98 18 h6 v4 h-6Z M110 18 h6 v4 h-6Z M92 22 h6 v4 h-6Z M104 22 h6 v4 h-6Z M98 26 h6 v4 h-6Z M110 26 h6 v4 h-6Z" fill="#26232F"/>
<circle cx="20" cy="84" r="8" fill="#ECEFF1" opacity=".9"/><circle cx="10" cy="78" r="6" fill="#ECEFF1" opacity=".8"/><circle cx="8" cy="88" r="5" fill="#ECEFF1" opacity=".7"/>
<path d="M28 82 Q28 70 40 68 H86 Q102 68 108 80 L110 86 H28Z" fill="#FDD835" {s()}/>
<path d="M30 80 H108" stroke="#F9A825" stroke-width="2.4"/>
<circle cx="56" cy="50" r="13" fill="#1E5AC8" {s()}/>
<path d="M46 50 Q56 44 66 50 V56 H46Z" fill="#B3E5FC" {s('stroke-width="2.2"')}/>
{eye(52, 52, .6)}{eye(60, 52, .6)}
<path d="M50 60 Q56 64 62 60 L64 70 H48Z" fill="#E53935" {s('stroke-width="2.2"')}/>
<path d="M64 64 L72 66" {s('stroke-width="3"')}/><circle cx="74" cy="66" r="4" fill="none" {s('stroke-width="2.4"')}/>
<text x="88" y="81" font-family="Arial Black, Arial" font-weight="900" font-size="15" fill="#E53935" stroke="{O}" stroke-width="1">5</text>
<circle cx="104" cy="76" r="3.6" fill="#fff" {s('stroke-width="1.6"')}/><circle cx="104.8" cy="76.4" r="1.6" fill="{O}"/>
<circle cx="40" cy="88" r="10" fill="#26232F" {s()}/><circle cx="40" cy="88" r="4" fill="#9E9E9E"/>
<circle cx="96" cy="88" r="10" fill="#26232F" {s()}/><circle cx="96" cy="88" r="4" fill="#9E9E9E"/>
''', cx="40%", cy="20%")

if __name__ == "__main__":
    import sys
    for pid, body in I.items():
        if len(sys.argv) > 1 and pid not in sys.argv[1:]:
            continue
        open(os.path.join(ROOT, "icons-src", pid + ".svg"), "w").write(body)
    print(len(I))
