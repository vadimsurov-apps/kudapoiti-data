"""Иконки робота pools, 2026-11-12 (23 UTC). Каждая придумана и нарисована отдельно (правило абсолютной
уникальности): свой герой, своя сцена, своя компоновка и палитра. Иконки «Лотоса» и Magic Swim нарисованы прошлым
запуском (tools/icons_pools_1112b.py). Запуск: python3 tools/icons_pools_1113.py [id …]
затем python3 tools/render_icons.py <id…> и python3 tools/check_unique.py <id…>."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, sparkle, O
from icons_pools_1112b import W, bub, T2

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}

# 2. «Плыви с Алисой» (Большая Почтовая ул.) — почтовая открытка вместо плавательной доски
ICONS["plyvi-s-alisoy-pochtovaya"] = W("#FFF3D6", "#F2A23A", f'''
<path d="M-6 74 Q10 66 24 74 T54 74 T84 74 T114 74 T140 74 V134 H-6Z" fill="#37B6E8" {s('stroke-width="2.6"')}/>
<path d="M6 104 Q16 99 26 104 M92 112 Q102 107 112 112 M44 118 Q54 113 64 118" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".7"/>
<g transform="rotate(-8 44 70)">
<rect x="8" y="46" width="72" height="48" rx="5" fill="#FFFDF6" {s()}/>
<path d="M44 52 V88" stroke="#C9BFAE" stroke-width="2"/>
<path d="M50 66 H72 M50 74 H72 M50 82 H66" stroke="#9BB4D6" stroke-width="2.6" stroke-linecap="round"/>
<rect x="13" y="51" width="19" height="15" rx="1.5" fill="#E8463C" {s('stroke-width="2"')}/>
<path d="M17 61 Q20 55 23 60 T29 58" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
<circle cx="34" cy="64" r="9" fill="none" stroke="#3E63D8" stroke-width="2.2" opacity=".8"/>
<path d="M26 61 Q30 58 34 61 T42 61 M26 67 Q30 64 34 67 T42 67" fill="none" stroke="#3E63D8" stroke-width="1.8" opacity=".8"/>
<path d="M14 80 H38 M14 87 H32" stroke="#9BB4D6" stroke-width="2.6" stroke-linecap="round"/>
</g>
<path d="M70 62 Q86 54 96 60 Q108 66 118 62" fill="none" stroke="{O}" stroke-width="15" stroke-linecap="round"/>
<path d="M70 62 Q86 54 96 60 Q108 66 118 62" fill="none" stroke="#FFD2B0" stroke-width="9.4" stroke-linecap="round"/>
<path d="M96 54 Q104 52 110 58 L108 68 Q100 70 94 64Z" fill="#FF7A1A" {s(T2)}/>
<path d="M62 60 Q50 60 40 52 M64 68 Q52 70 44 64" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M62 60 Q50 60 40 52 M64 68 Q52 70 44 64" fill="none" stroke="#FFD2B0" stroke-width="4.6" stroke-linecap="round"/>
<circle cx="72" cy="46" r="14" fill="#FFD2B0" {s()}/>
<path d="M58 44 Q60 30 72 30 Q84 30 86 42 Q72 36 58 44Z" fill="#7A4A2A" {s(T2)}/>
{eye(66, 48, .85)}{eye(77, 47, .85)}
<path d="M68 54 Q72 58 77 53" fill="none" {s('stroke-width="2.2"')}/>
<ellipse cx="62" cy="53" rx="3.4" ry="2" fill="#FF7FA8" opacity=".7"/>
<path d="M112 50 Q116 40 122 44 M118 56 Q126 50 130 56 M108 44 Q108 34 114 32" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
<path d="M112 50 Q116 40 122 44 M118 56 Q126 50 130 56 M108 44 Q108 34 114 32" fill="none" stroke="#37B6E8" stroke-width="1.6" stroke-linecap="round"/>
''', 60, 18)
SUBJ["plyvi-s-alisoy-pochtovaya"] = ("большая почтовая открытка с красной маркой и волнистым штемпелем",
                                     "служит плавательной доской: малыш в оранжевых плавках держится за неё и бьёт ногами, поднимая брызги")

# 3. My Swim Team (фитнес-клуб «Охана») — ключ от шкафчика на запястье пловца
ICONS["my-swim-team-buninskaya"] = W("#E9F7FF", "#57A8E8", f'''
<path d="M-6 96 Q12 88 28 96 T60 96 T92 96 T124 96 T150 96 V134 H-6Z" fill="#1E7FD0" {s('stroke-width="2.6"')}/>
<path d="M10 114 Q22 109 34 114 M74 118 Q86 113 98 118" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".7"/>
<path d="M22 100 Q30 60 56 40 Q76 26 100 22" fill="none" stroke="{O}" stroke-width="27" stroke-linecap="round"/>
<path d="M22 100 Q30 60 56 40 Q76 26 100 22" fill="none" stroke="#FFD2B0" stroke-width="20.6" stroke-linecap="round"/>
<path d="M98 10 Q112 8 118 16 Q122 24 114 28 L120 34 Q112 38 106 34 Q96 36 92 28Z" fill="#FFD2B0" {s()}/>
<path d="M104 14 L108 26 M110 12 L114 24" fill="none" {s('stroke-width="2"')}/>
<path d="M58 28 Q70 34 74 48" fill="none" stroke="{O}" stroke-width="10" stroke-linecap="round"/>
<path d="M58 28 Q70 34 74 48" fill="none" stroke="#FF4F7B" stroke-width="5.6" stroke-linecap="round" stroke-dasharray="3.4 3"/>
<path d="M66 48 Q70 58 64 66" fill="none" {s('stroke-width="2.6"')}/>
<circle cx="62" cy="76" r="12" fill="#FFD23F" {s()}/>
<circle cx="62" cy="72" r="3.4" fill="#E9F7FF" {s('stroke-width="2"')}/>
<path d="M57 80 H67" stroke="{O}" stroke-width="2.4" stroke-linecap="round"/>
<path d="M70 82 L96 104 L90 108 L92 112 L86 112 L84 106 L80 104 L64 88Z" fill="#C9D3E2" {s()}/>
<rect x="86" y="58" width="26" height="18" rx="4" fill="#FF4F7B" {s()}/>
<path d="M92 65 L95 62 V71 M101 63 H106 L102 71" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M76 74 Q82 70 86 68" fill="none" {s('stroke-width="2.2"')}/>
<path d="M16 90 Q10 80 18 76 M34 92 Q36 82 44 84 M6 98 Q0 92 4 86" fill="none" stroke="#fff" stroke-width="4.4" stroke-linecap="round"/>
{bub(112, 46, 4.4)}{bub(18, 44, 5)}
''', 70, 20)
SUBJ["my-swim-team-buninskaya"] = ("жёлтый ключ от шкафчика раздевалки с розовым номерком 17 на спиральном браслете-пружинке",
                                   "болтается на запястье пловца, пока рука делает широкий гребок кролем над синей водой")

# 4. My Swim Team (ФОК «Изумрудный») — изумруд ныряет «бомбочкой»
ICONS["my-swim-team-izumrudny"] = W("#F2FFE9", "#19A974", f'''
<path d="M-6 88 H134 V134 H-6Z" fill="#0E7F6B"/>
<ellipse cx="64" cy="100" rx="52" ry="13" fill="none" stroke="#fff" stroke-width="3" opacity=".5"/>
<ellipse cx="64" cy="100" rx="34" ry="8" fill="none" stroke="#fff" stroke-width="3.4" opacity=".8"/>
<path d="M-6 88 H134" stroke="{O}" stroke-width="2.6"/>
<path d="M36 22 H92 L112 46 L64 96 L16 46Z" fill="#2EDB8F" {s()}/>
<path d="M36 22 L48 46 L64 22 L80 46 L92 22" fill="#7BF2BE" {s(T2)}/>
<path d="M16 46 H112" fill="none" {s(T2)}/>
<path d="M48 46 L64 96 L80 46" fill="#19B873" {s(T2)}/>
<path d="M48 46 H80 L64 96Z" fill="#19B873" opacity=".0"/>
<rect x="34" y="50" width="26" height="15" rx="7.5" fill="#DFF8FF" {s()}/><rect x="68" y="50" width="26" height="15" rx="7.5" fill="#DFF8FF" {s()}/>
<path d="M60 57 H68 M34 56 L18 50 M94 56 L110 50" fill="none" {s()}/>
{eye(47, 58, .95)}{eye(81, 58, .95)}
<path d="M56 72 Q64 80 72 72" fill="#fff" {s('stroke-width="2.6"')}/>
<ellipse cx="38" cy="72" rx="4.4" ry="2.6" fill="#FF7FA8" opacity=".75"/><ellipse cx="90" cy="72" rx="4.4" ry="2.6" fill="#FF7FA8" opacity=".75"/>
<path d="M30 90 Q22 76 30 72 M98 90 Q106 76 98 72 M46 94 Q42 84 46 80 M82 94 Q86 84 82 80" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
{sparkle(104, 24, 8)}{sparkle(22, 26, 5)}
<circle cx="14" cy="80" r="3.6" fill="#fff"/><circle cx="114" cy="80" r="3.6" fill="#fff"/><circle cx="120" cy="68" r="2.4" fill="#fff"/>
''', 50, 16)
SUBJ["my-swim-team-izumrudny"] = ("огранённый зелёный изумруд в плавательных очках",
                                  "ныряет остриём вниз в зелёную воду — во все стороны летят брызги и расходятся круги")

if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for i in ids:
        open(os.path.join(OUT, i + ".svg"), "w", encoding="utf-8").write(ICONS[i])
    print("svg:", len(ids))
