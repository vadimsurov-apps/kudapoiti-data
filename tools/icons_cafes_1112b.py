"""Иконки робота cafes, 2026-11-12 (02 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая придумана отдельно,
герои и сцены сверены с subjects.txt и листами каталога кафе 07–21 (медовик-певец с пчелой-дирижёром,
тосты-доминошки, мегрельский хачапури с аккордеоном — таких нет).
Запуск: python3 tools/icons_cafes_1112b.py [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "zb_pine": ("#DDF5E6", "#3E9A6A"),
    "zb_lilac": ("#F1E8FF", "#9C7FD9"),
    "zb_ember": ("#FFE6D6", "#C8553D"),
    "zb_cocoa": ("#FFF1E0", "#B98A62"),
    "zb_ice": ("#F0FBFF", "#57A6D9"),
    "zb_cherry": ("#FFE9EC", "#E0566C"),
    "zb_lime": ("#F6FFD9", "#9CC63F"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Джонджоли (Новогиреево): грузинский ресторан с живой музыкой, в меню медовик — медовик поёт, пчела дирижирует
add("cafe-dzhondzholi-novogireevo",
    "треугольный кусок медовика с медовыми коржами и кремовыми прослойками",
    "поёт с открытым ртом, а маленькая пчёлка над ним дирижирует палочкой",
    "zb_pine", f'''<g transform="translate(5 0)">
<ellipse cx="62" cy="108" rx="44" ry="8" fill="#FFFFFF" {W(3)}/>
<path d="M22 102 L102 102 L102 62 L22 86Z" fill="#D9893A" {W(3)}/>
<path d="M22 86 L102 62 L102 54 L22 78Z" fill="#F4C87A" {W(3)}/>
<path d="M22 93 L102 70 M22 98 L102 78 M22 102 L102 86 M22 102 L102 94" stroke="#FFF1CF" stroke-width="3.4"/>
<path d="M22 102 L102 102 L102 62 L22 86Z" fill="none" {W(3)}/>
<path d="M22 78 L102 54" fill="none" {W(3)}/>
<circle cx="90" cy="52" r="2.2" fill="#B5651D"/><circle cx="72" cy="58" r="2" fill="#B5651D"/><circle cx="50" cy="65" r="2.2" fill="#B5651D"/>
{eye(52, 89, 0.85)}{eye(74, 82, 0.85)}
<ellipse cx="64" cy="94" rx="5" ry="5.5" fill="#8A2E3A" {W(2.4)}/>
<ellipse cx="44" cy="96" rx="4" ry="2.3" fill="#FF7FA8" opacity=".7"/><ellipse cx="84" cy="88" rx="4" ry="2.3" fill="#FF7FA8" opacity=".7"/>
</g>
<path d="M50 46 q-6 -6 0 -12 M46 52 l-4 -3" fill="none" {W(2.4)}/>
<g transform="translate(78 26)">
<ellipse cx="-6" cy="-8" rx="6" ry="4.5" fill="#E8F6FF" {W(2)} transform="rotate(-25 -6 -8)"/>
<ellipse cx="4" cy="-9" rx="6" ry="4.5" fill="#E8F6FF" {W(2)} transform="rotate(25 4 -9)"/>
<ellipse cx="0" cy="0" rx="10" ry="7.5" fill="#FFD23F" {W(2.6)}/>
<path d="M-3 -7 L-3 7 M3 -7 L3 7" stroke="{O}" stroke-width="2.6"/>
<circle cx="-6" cy="-1" r="1.6" fill="{O}"/>
<path d="M-12 2 L-26 14" stroke="{O}" stroke-width="2.4" stroke-linecap="round"/>
</g>
<path d="M30 30 l0 -10 l7 -2 l0 9" fill="none" {W(2.2)}/><circle cx="28" cy="30" r="2.6" fill="{O}"/><circle cx="35" cy="28" r="2.6" fill="{O}"/>
{sparkle(108, 36, 5)}{sparkle(18, 56, 4)}
''')

# 2. Eat&Play (Марфино): кафе с детской игровой, завтраки — тосты-доминошки с черничными точками падают цепочкой
add("cafe-eat-play-marfino",
    "четыре поджаристых тоста-доминошки с точками из черники",
    "падают цепочкой друг на друга, первый удивлённо оглядывается",
    "zb_lilac", f'''
<rect x="8" y="104" width="112" height="6" rx="3" fill="#7A5BC0" opacity=".45"/>
<g transform="rotate(-62 30 104)"><path d="M18 104 L18 72.8 Q14 62 30.0 62 Q46 62 42 72.8 L42 104Z" fill="#D99A4A" {W(2.8)}/><path d="M22 100 L22 74.8 Q19 67 30.0 67 Q41 67 38 74.8 L38 100Z" fill="#FFF0CF"/><path d="M22 83 L38 83" {W(2)}/><circle cx="30" cy="74" r="2.6" fill="#3E3A8C"/><circle cx="30" cy="92" r="2.6" fill="#3E3A8C"/></g>
<g transform="rotate(-38 52 104)"><path d="M40 104 L40 68.8 Q36 58 52.0 58 Q68 58 64 68.8 L64 104Z" fill="#D99A4A" {W(2.8)}/><path d="M44 100 L44 70.8 Q41 63 52.0 63 Q63 63 60 70.8 L60 100Z" fill="#FFF0CF"/><path d="M44 81 L60 81" {W(2)}/><circle cx="48" cy="70" r="2.4" fill="#3E3A8C"/><circle cx="56" cy="76" r="2.4" fill="#3E3A8C"/><circle cx="52" cy="90" r="2.4" fill="#3E3A8C"/></g>
<g transform="rotate(-16 74 104)"><path d="M62 104 L62 65.7 Q58 54 75.0 54 Q92 54 88 65.7 L88 104Z" fill="#D99A4A" {W(2.8)}/><path d="M66 100 L66 67.7 Q63 59 75.0 59 Q87 59 84 67.7 L84 100Z" fill="#FFF0CF"/><path d="M66 79 L84 79" {W(2)}/><circle cx="70" cy="64" r="2.4" fill="#3E3A8C"/><circle cx="80" cy="64" r="2.4" fill="#3E3A8C"/><circle cx="70" cy="74" r="2.4" fill="#3E3A8C"/><circle cx="80" cy="74" r="2.4" fill="#3E3A8C"/><circle cx="75" cy="92" r="2.4" fill="#3E3A8C"/></g>
<path d="M88 104 L88 58.6 Q84 46 102.0 46 Q120 46 116 58.6 L116 104Z" fill="#D99A4A" {W(2.8)}/><path d="M92 100 L92 60.6 Q89 51 102.0 51 Q115 51 112 60.6 L112 100Z" fill="#FFF0CF"/>
<path d="M92 76 L112 76" {W(2.2)}/>
{eye(97, 63, 0.75)}{eye(107, 63, 0.75)}
<ellipse cx="102" cy="70" rx="2.6" ry="3" fill="#8A2E3A"/>
<circle cx="96" cy="86" r="2.6" fill="#3E3A8C"/><circle cx="108" cy="86" r="2.6" fill="#3E3A8C"/><circle cx="102" cy="93" r="2.6" fill="#3E3A8C"/>
<path d="M84 36 q4 -6 8 0 M98 30 l0 -8 M110 34 l5 -5" fill="none" {W(2.4)}/>
{sparkle(24, 30, 6)}{sparkle(56, 22, 4)}
''')

# 3. Семейный Очаг (Печатники): кавказская кухня, живая музыка, хачапури по-мегрельски — лепёшка играет на аккордеоне
add("cafe-semeyny-ochag-pechatniki",
    "круглый хачапури по-мегрельски с румяной сырной корочкой в пузырях",
    "растягивает меха красного аккордеона на маленькой сцене под гирляндой лампочек",
    "zb_ember", f'''
<path d="M6 22 Q64 40 122 22" fill="none" stroke="{O}" stroke-width="2"/>
<circle cx="22" cy="27" r="4" fill="#FFE066" {W(2)}/><circle cx="43" cy="32" r="4" fill="#7FE0C8" {W(2)}/><circle cx="64" cy="33" r="4" fill="#FF9EC4" {W(2)}/><circle cx="85" cy="32" r="4" fill="#FFE066" {W(2)}/><circle cx="106" cy="27" r="4" fill="#7FE0C8" {W(2)}/>
<rect x="10" y="108" width="108" height="14" rx="4" fill="#7A3B22" {W(3)}/>
<circle cx="64" cy="66" r="34" fill="#E6A04A" {W(3.2)}/>
<circle cx="64" cy="66" r="27" fill="#FFD866" {W(2.4)}/>
<circle cx="50" cy="52" r="5" fill="#F0A83A" opacity=".8"/><circle cx="80" cy="50" r="4" fill="#F0A83A" opacity=".8"/><circle cx="78" cy="78" r="3.5" fill="#F0A83A" opacity=".8"/><circle cx="46" cy="76" r="3" fill="#F0A83A" opacity=".8"/>
{face(64, 60, 9, 0.9)}
<rect x="22" y="80" width="18" height="26" rx="3" fill="#E23B3B" {W(2.6)}/>
<rect x="88" y="80" width="18" height="26" rx="3" fill="#E23B3B" {W(2.6)}/>
<path d="M40 82 L46 106 L52 82 L58 106 L64 82 L70 106 L76 82 L82 106 L88 82" fill="#FFF3E0" {W(2.4)}/>
<path d="M40 82 L88 82 M40 106 L88 106" {W(2.4)}/>
<circle cx="28" cy="88" r="2" fill="#FFF"/><circle cx="34" cy="88" r="2" fill="#FFF"/><circle cx="28" cy="96" r="2" fill="#FFF"/><circle cx="34" cy="96" r="2" fill="#FFF"/>
<path d="M92 86 L102 86 M92 92 L102 92 M92 98 L102 98" stroke="#FFF" stroke-width="2.4" stroke-linecap="round"/>
<path d="M112 56 l0 -10 l7 -2 l0 9" fill="none" {W(2.2)}/><circle cx="110" cy="56" r="2.6" fill="{O}"/><circle cx="117" cy="54" r="2.6" fill="{O}"/>
{sparkle(16, 60, 4)}
''')

# 4. Додо Пицца (Малая Филёвская): десерт «бруслетики» — рулетик с брусничной спиралью съезжает в какао
add("cafe-dodo-malaya-filevskaya",
    "сладкий рулетик-бруслетик с розовой брусничной спиралью на срезе",
    "съезжает по горке из пломбирного крема прямо в чашку горячего какао",
    "zb_cocoa", f'''
<path d="M-4 41 Q38 45 61 70 Q72 82 84 86" fill="none" stroke="#FFF6D2" stroke-width="18" stroke-linecap="round"/>
<path d="M-4 41 Q38 45 61 70 Q72 82 84 86" fill="none" stroke="#FFE7A6" stroke-width="4" stroke-dasharray="3 9" stroke-linecap="round"/>
<path d="M2 32 Q40 36 64 62 Q74 74 86 78" fill="none" {W(2.6)}/>
<path d="M4 50 Q36 54 58 78 Q68 90 82 94" fill="none" {W(2.6)}/>
<path d="M70 92 L118 92 L112 120 L76 120Z" fill="#5BB7E8" {W(3)}/>
<path d="M118 98 q10 2 8 10 q-2 8 -12 6" fill="none" {W(3)}/>
<ellipse cx="94" cy="92" rx="24" ry="5" fill="#7B4A2A" {W(2.6)}/>
<path d="M84 80 q-3 -6 0 -10 M100 80 q3 -6 0 -10" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>
<g transform="rotate(32 46 52)">
<rect x="22" y="36" width="40" height="30" rx="8" fill="#F2C27A" {W(3)}/>
<ellipse cx="62" cy="51" rx="11" ry="15" fill="#FFF3DD" {W(3)}/>
<path d="M62 51 m-2 0 a2 2 0 1 1 4 0 a4.5 4.5 0 1 1 -9 0 a7 7 0 1 1 14 0 a9.5 9.5 0 1 1 -19 0" fill="none" stroke="#D6336C" stroke-width="2.6" stroke-linecap="round"/>
{eye(32, 48, 0.75)}{eye(44, 48, 0.75)}
<path d="M34 56 Q38 60 42 56" fill="none" {W(2.2)}/>
<circle cx="28" cy="40" r="1.8" fill="#FFFFFF"/><circle cx="40" cy="39" r="1.8" fill="#FFFFFF"/><circle cx="50" cy="41" r="1.8" fill="#FFFFFF"/>
</g>
<circle cx="30" cy="96" r="4" fill="#D6336C" {W(2)}/><circle cx="38" cy="102" r="4" fill="#D6336C" {W(2)}/><path d="M30 92 q4 -6 10 -4" fill="none" stroke="#3E8E41" stroke-width="2.4"/>
{sparkle(104, 30, 6)}{sparkle(22, 76, 4)}
''')

# 5. Truecost (Орджоникидзе): ресторан, морепродукты на льду — клешня камчатского краба показывает «класс» с горки льда
add("cafe-truecost-ordzhonikidze",
    "красная клешня камчатского краба с белыми шипиками",
    "торчит из горки колотого льда и щёлкает пальцами-клешнями, рядом долька лимона",
    "zb_ice", f'''
<path d="M8 116 L22 92 L36 102 L50 84 L64 98 L78 82 L92 100 L106 88 L122 116Z" fill="#FFFFFF" {W(3)}/>
<path d="M22 92 L28 108 M50 84 L54 104 M78 82 L76 102 M106 88 L100 106" stroke="#BFE3F5" stroke-width="2.4"/>
<path d="M56 100 L54 80 L74 80 L72 100Z" fill="#E8412F" {W(3)}/>
<ellipse cx="64" cy="66" rx="24" ry="20" fill="#E8412F" {W(3)}/>
<path d="M46 54 Q26 34 40 18 Q50 8 60 12 L58 18 Q46 20 46 32 Q48 42 58 48Z" fill="#E8412F" {W(3)}/>
<path d="M82 54 Q102 34 90 20 Q82 12 70 14 L72 20 Q82 22 82 32 Q80 42 70 48Z" fill="#E8412F" {W(3)}/>
<g fill="#FFFFFF" {W(1.4)}><path d="M42 28 l-5 -1 l4 -3Z"/><path d="M86 28 l5 -1 l-4 -3Z"/><path d="M42 74 l-5 1 l3 3Z"/><path d="M86 74 l5 1 l-3 3Z"/></g>
{eye(56, 64, 0.85)}{eye(72, 64, 0.85)}
<path d="M60 74 Q64 78 68 74" fill="none" {W(2.4)}/>
<ellipse cx="49" cy="72" rx="3.6" ry="2.2" fill="#FFB0B8" opacity=".9"/><ellipse cx="79" cy="72" rx="3.6" ry="2.2" fill="#FFB0B8" opacity=".9"/>
<path d="M92 112 a13 13 0 0 1 26 0Z" fill="#FFE14D" {W(2.6)}/><path d="M105 112 L105 102 M105 112 L97 104 M105 112 L113 104" stroke="#F2B705" stroke-width="2"/>
{sparkle(22, 34, 6)}{sparkle(112, 56, 4)}{sparkle(30, 70, 3)}
''')

# 6. TGI Fridays (ТРЦ Columbus): американская кухня — крылышко баффало «машет» косточкой на тарелке в красно-белую полоску
add("cafe-tgi-fridays-columbus",
    "куриное крылышко баффало в красно-оранжевом остром соусе с белой косточкой",
    "машет косточкой, как крылом, и пытается взлететь с тарелки в красно-белую полоску",
    "zb_cherry", f'''
<ellipse cx="64" cy="104" rx="48" ry="12" fill="#FFFFFF" {W(3)}/>
<path d="M24 100 L32 112 M40 96 L48 114 M60 94 L64 116 M80 94 L80 116 M98 96 L94 114" stroke="#E23B4E" stroke-width="5"/>
<ellipse cx="64" cy="104" rx="48" ry="12" fill="none" {W(3)}/>
<path d="M30 90 q-8 -4 -6 -10 M98 90 q8 -4 6 -10" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>
<path d="M36 74 Q30 50 52 42 Q74 36 86 50 Q96 62 90 78 Q82 92 60 92 Q42 92 36 74Z" fill="#E8572A" {W(3.2)}/>
<circle cx="50" cy="52" r="2" fill="#FFB38A"/><circle cx="76" cy="48" r="2.2" fill="#FFB38A"/><circle cx="84" cy="70" r="1.8" fill="#FFB38A"/><circle cx="44" cy="78" r="1.8" fill="#FFB38A"/>
{face(63, 64, 9, 0.9)}
<g transform="rotate(-35 92 52)">
<rect x="88" y="34" width="8" height="28" rx="4" fill="#FFF8EC" {W(2.6)}/>
<circle cx="88" cy="32" r="5" fill="#FFF8EC" {W(2.4)}/><circle cx="96" cy="32" r="5" fill="#FFF8EC" {W(2.4)}/>
</g>
<path d="M110 24 q6 4 2 10 M116 40 q6 0 6 6" fill="none" {W(2.4)}/>
<path d="M20 36 l4 -6 l4 6 l-4 6Z" fill="#FFFFFF" {W(2)}/>
{sparkle(30, 22, 5)}
''')

# 7. Варим Жарим (Коммунарка): хинкали — близнецы, варёный и жареный, меряются ростом
add("cafe-varim-zharim-kommunarka",
    "два хинкали-близнеца — белый варёный и золотистый жареный",
    "меряются ростом у дверного косяка с карандашными отметками",
    "zb_lime", f'''
<rect x="96" y="10" width="16" height="112" fill="#C98B52" {W(3)}/>
<path d="M96 44 L104 44 M96 58 L102 58 M96 72 L104 72 M96 86 L102 86" stroke="#3B3355" stroke-width="2.4" stroke-linecap="round"/>
<rect x="6" y="110" width="116" height="10" rx="3" fill="#8BB548" {W(2.6)}/>
<path d="M14 110 Q10 82 32 76 L36 64 Q38 58 40 64 L44 76 Q66 82 62 110Z" fill="#FFFDF4" {W(3)}/>
<path d="M36 64 L38 50" {W(3)}/><circle cx="38" cy="48" r="3.5" fill="#FFFDF4" {W(2.4)}/>
<path d="M22 84 Q30 90 30 104 M54 84 Q46 90 46 104 M38 80 L38 104" fill="none" stroke="#D9D2C0" stroke-width="2.2"/>
{eye(31, 94, 0.75)}{eye(45, 94, 0.75)}
<path d="M35 101 Q38 104 41 101" fill="none" {W(2)}/>
<path d="M64 110 Q60 80 74 74 L78 60 Q80 54 82 60 L86 74 Q100 80 96 110Z" fill="#E9A23B" {W(3)}/>
<path d="M78 60 L80 44" {W(3)}/><circle cx="80" cy="42" r="3.5" fill="#E9A23B" {W(2.4)}/>
<path d="M70 86 Q76 92 76 104 M90 86 Q84 92 84 104" fill="none" stroke="#C47A1E" stroke-width="2.2"/>
{eye(74, 92, 0.75)}{eye(86, 92, 0.75)}
<path d="M77 99 Q80 102 83 99" fill="none" {W(2)}/>
<rect x="66" y="40" width="34" height="4" rx="2" fill="#5B8DEF" {W(1.8)} transform="rotate(-4 83 42)"/>
<path d="M18 38 q4 -8 0 -14 M28 40 q4 -8 0 -14" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>
{sparkle(58, 22, 5)}
''')


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
