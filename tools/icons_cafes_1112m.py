"""Иконки робота cafes, 2026-11-12 (11 UTC). Каждая придумана отдельно (правило АБСОЛЮТНОЙ уникальности):
герои и сцены сверены поиском по icons-src/subjects.txt; палитры фона — свои.
Запуск: python3 tools/icons_cafes_1112m.py [id…]  (без аргументов — все + строки реестра в subjects.txt)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
BL = lambda x, y: f'<ellipse cx="{x}" cy="{y}" rx="3.8" ry="2.2" fill="#FF7FA8" opacity=".7"/>'
draw_icons.BG.update({
    "zm_mono": ("#EAF4FF", "#7FA7E0"),
    "zm_hoop": ("#FFF3E2", "#E59A55"),
    "zm_metro": ("#F3EEFF", "#8C7BD1"),
    "zm_pudding": ("#FFF9E8", "#E8B95A"),
    "zm_sugar": ("#FFEFF4", "#E58AA6"),
    "zm_rope": ("#EAFBEF", "#5DB57B"),
    "zm_fez": ("#FFF2E0", "#E07B54"),
    "zm_run": ("#EFFFF4", "#62B88A"),
    "zm_frost": ("#E8F3FF", "#6E9BD6"),
    "zm_peach": ("#FFF0E8", "#F49A6B"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Додо Пицца (ул. Павла Корчагина, у ВДНХ): кусок пиццы едет в вагончике монорельса
add("cafe-dodo-pavla-korchagina-3",
    "кусок пиццы пепперони, высунувшийся из окна вагончика монорельса",
    "едет по высокой бетонной эстакаде монорельса над крышами домов",
    "zm_mono", f'''
<rect x="8" y="92" width="22" height="36" fill="#C9D3E8" {W(2.4)}/>
<rect x="98" y="88" width="24" height="40" fill="#D7DDEC" {W(2.4)}/>
<rect x="56" y="84" width="14" height="44" fill="#B8BFCC" {W(2.6)}/>
<rect x="0" y="76" width="128" height="10" fill="#9EA7B8" {W(2.6)}/>
<path d="M14 40 Q14 30 26 30 L108 30 Q118 30 120 44 L120 70 L14 70Z" fill="#FFFFFF" {W(3)}/>
<path d="M14 58 L120 58" stroke="#E2362F" stroke-width="5"/>
<rect x="24" y="38" width="16" height="14" rx="3" fill="#BFE3FF" {W(2.2)}/>
<rect x="90" y="38" width="16" height="14" rx="3" fill="#BFE3FF" {W(2.2)}/>
<rect x="46" y="36" width="38" height="18" rx="3" fill="#BFE3FF" {W(2.4)}/>
<path d="M50 52 L64 10 L80 52Z" fill="#FFC94A" {W(3)}/>
<path d="M60 22 Q64 16 68 22" fill="#E9A23B" {W(2)}/>
<circle cx="66" cy="40" r="3.6" fill="#D9363E" {W(1.6)}/><circle cx="58" cy="46" r="3" fill="#D9363E" {W(1.6)}/>
{eye(60, 32, 0.6)}{eye(70, 32, 0.6)}
<path d="M62 37 Q65 39 68 37" fill="none" {W(1.6)}/>
<circle cx="30" cy="72" r="4" fill="#555" {W(2)}/><circle cx="104" cy="72" r="4" fill="#555" {W(2)}/>
{sparkle(108, 16, 5)}
''')

# 2. Meat Hook (Мытищи): котлета для бургера крутит хулахуп из колечка жареного лука
add("cafe-meat-hook-mytishchi",
    "толстая котлета для бургера с полосками от гриля",
    "крутит на поясе хулахуп из большого золотого колечка жареного лука",
    "zm_hoop", f'''
<ellipse cx="64" cy="118" rx="30" ry="5" fill="#000" opacity=".12"/>
<path d="M54 92 L50 114 M74 92 L78 114" {W(3.4)}/>
<path d="M44 116 L52 116 M76 116 L84 116" {W(3.4)}/>
<ellipse cx="64" cy="64" rx="34" ry="30" fill="#8A4B2A" {W(3.2)}/>
<path d="M40 46 L56 40 M38 60 L70 46 M44 76 L86 54 M62 84 L92 68" stroke="#4A2614" stroke-width="3.4" stroke-linecap="round"/>
{eye(54, 62, 0.85)}{eye(74, 62, 0.85)}
<path d="M58 72 Q64 78 70 72" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"/>
{BL(46, 70)}{BL(82, 70)}
<path d="M30 60 L14 44 M98 60 L114 44" {W(3.2)}/>
<ellipse cx="64" cy="82" rx="50" ry="11" fill="none" stroke="{O}" stroke-width="11"/>
<ellipse cx="64" cy="82" rx="50" ry="11" fill="none" stroke="#E9A93E" stroke-width="7"/>
<path d="M30 76 Q34 74 38 76 M86 90 Q90 92 94 90 M60 92 Q64 94 68 92" stroke="#C47A22" stroke-width="2" fill="none"/>
<path d="M8 70 Q4 82 10 94 M120 70 Q124 82 118 94" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>
''')

# 3. Здрасте (Мытищи, пр-т Астрахова): пряничный вагон метро (Мытищи — город, где делают вагоны метро)
add("cafe-zdraste-mytishchi-astrakhova",
    "имбирный пряничный вагончик метро с окошками из белой глазури",
    "весело выкатывается на рельсах из тоннеля, сделанного из шоколадного рулета",
    "zm_metro", f'''
<rect x="0" y="100" width="128" height="28" fill="#7A6A9E"/>
<path d="M0 104 L128 104 M0 112 L128 112" stroke="#C9C2D9" stroke-width="2.4"/>
<path d="M76 104 L76 40 Q76 20 100 20 Q124 20 124 40 L124 104" fill="#5B341E" {W(3)}/>
<path d="M88 104 L88 48 Q88 36 100 36 Q112 36 112 48 L112 104Z" fill="#2B1A12"/>
<path d="M80 34 Q100 26 120 34 M78 52 Q100 44 122 52" stroke="#F3E2C8" stroke-width="2.6" fill="none"/>
<path d="M8 44 Q8 36 16 36 L82 36 Q94 36 96 50 L96 96 L8 96Z" fill="#C98545" {W(3)}/>
<path d="M12 86 Q20 82 28 86 Q36 90 44 86 Q52 82 60 86 Q68 90 76 86 Q84 82 92 86" fill="none" stroke="#FFFFFF" stroke-width="2.6"/>
<rect x="16" y="46" width="18" height="16" rx="4" fill="#FFF4E6" {W(2.2)}/>
<rect x="40" y="46" width="18" height="16" rx="4" fill="#FFF4E6" {W(2.2)}/>
<path d="M64 44 L64 82 M78 44 L78 82" {W(2)}/>
<circle cx="20" cy="96" r="5" fill="#4A4458" {W(2)}/><circle cx="84" cy="96" r="5" fill="#4A4458" {W(2)}/>
{eye(46, 72, 0.7)}{eye(60, 72, 0.7)}
<path d="M48 78 Q53 82 58 78" fill="none" {W(2)}/>
<circle cx="90" cy="60" r="3" fill="#FFE07A" {W(1.6)}/>
{sparkle(30, 22, 5)}{sparkle(54, 16, 3.5)}
''')

# 4. Тануки (Одинцово, Можайское ш.): японский пудинг пурин гребёт палочками в пиале-лодочке
add("cafe-tanuki-odintsovo-mozhayskoe-122",
    "японский пудинг пурин с блестящей карамельной шапкой",
    "плывёт в синей фарфоровой пиале, как в лодочке, и гребёт двумя палочками для еды",
    "zm_pudding", f'''
<path d="M0 98 Q16 92 32 98 Q48 104 64 98 Q80 92 96 98 Q112 104 128 98 L128 128 L0 128Z" fill="#8FD0EE" {W(2.4)}/>
<path d="M30 54 L40 26 Q44 22 64 22 Q84 22 88 26 L98 54Z" fill="#FFE29A" {W(3)}/>
<path d="M40 26 Q64 34 88 26 Q84 22 64 22 Q44 22 40 26Z" fill="#9A4B1A" {W(2.4)}/>
<path d="M44 30 Q46 40 44 44 M80 30 Q82 38 80 42" stroke="#9A4B1A" stroke-width="3" stroke-linecap="round" fill="none"/>
{eye(56, 42, 0.75)}{eye(72, 42, 0.75)}
<path d="M60 49 Q64 52 68 49" fill="none" {W(2)}/>
{BL(48, 48)}{BL(80, 48)}
<path d="M16 56 L112 56 Q108 92 64 94 Q20 92 16 56Z" fill="#FFFFFF" {W(3)}/>
<path d="M24 66 Q34 60 44 66 Q54 72 64 66 Q74 60 84 66 Q94 72 104 66" fill="none" stroke="#2F5FB3" stroke-width="3"/>
<circle cx="40" cy="80" r="3" fill="#2F5FB3"/><circle cx="64" cy="82" r="3" fill="#2F5FB3"/><circle cx="88" cy="80" r="3" fill="#2F5FB3"/>
<path d="M34 58 L8 104 M94 58 L120 104" stroke="#C98B4A" stroke-width="5" stroke-linecap="round"/>
<path d="M34 58 L8 104 M94 58 L120 104" fill="none" {W(1.6)}/>
''')

# 5. Osteria Mario (Чонгарский бул.): пончик бомболони под снегопадом сахарной пудры из сита
add("cafe-osteria-chongarsky",
    "пухлый итальянский пончик бомболони, из бочка выглядывает заварной крем",
    "жмурится от удовольствия под «снегопадом» сахарной пудры из металлического сита",
    "zm_sugar", f'''
<path d="M30 16 L98 16 L84 36 L44 36Z" fill="#D9DDE6" {W(3)}/>
<path d="M40 22 L88 22 M44 28 L84 28" stroke="#9AA1B0" stroke-width="1.6"/>
<path d="M98 16 L120 6" {W(4)}/>
<g fill="#FFFFFF"><circle cx="50" cy="44" r="2"/><circle cx="60" cy="50" r="1.8"/><circle cx="70" cy="42" r="2"/><circle cx="78" cy="52" r="1.8"/><circle cx="56" cy="58" r="1.6"/><circle cx="74" cy="60" r="1.6"/><circle cx="46" cy="54" r="1.5"/><circle cx="84" cy="44" r="1.6"/></g>
<ellipse cx="64" cy="118" rx="40" ry="6" fill="#FFFFFF" {W(2.6)}/>
<ellipse cx="64" cy="90" rx="40" ry="26" fill="#E9A85A" {W(3.2)}/>
<path d="M30 80 Q64 62 98 80" fill="none" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round"/>
<path d="M100 92 Q114 90 112 100 Q110 108 98 102Z" fill="#FFE07A" {W(2.4)}/>
<path d="M50 90 Q54 86 58 90 M70 90 Q74 86 78 90" fill="none" {W(2.4)}/>
<path d="M58 100 Q64 106 70 100" fill="none" {W(2.4)}/>
{BL(44, 98)}{BL(84, 98)}
{sparkle(20, 60, 4)}{sparkle(108, 58, 4)}
''')

# 6. Стейк-хаус Muu (ЗИЛАРТ): филе-миньон, перевязанный бечёвкой, идёт по канату с вилкой-шестом
add("cafe-muu-shchuseva",
    "круглый стейк филе-миньон, перевязанный поварской бечёвкой",
    "идёт по натянутому канату, балансируя длинной вилкой для мяса, как шестом",
    "zm_rope", f'''
<rect x="4" y="66" width="10" height="62" fill="#B07A45" {W(2.6)}/>
<rect x="114" y="66" width="10" height="62" fill="#B07A45" {W(2.6)}/>
<path d="M10 70 Q64 84 118 70" fill="none" stroke="{O}" stroke-width="4"/>
<path d="M10 70 Q64 84 118 70" fill="none" stroke="#E8D3A8" stroke-width="2"/>
<path d="M56 64 L54 78 M72 64 L74 78" {W(3)}/>
<rect x="38" y="24" width="52" height="42" rx="20" fill="#A8462F" {W(3.2)}/>
<path d="M40 38 Q64 44 88 38 M40 52 Q64 58 88 52" stroke="#F3E6CC" stroke-width="3.2" fill="none"/>
<path d="M46 30 Q52 28 54 32 M74 30 Q80 28 84 34" stroke="#E07A5F" stroke-width="2" fill="none"/>
{eye(56, 44, 0.75)}{eye(72, 44, 0.75)}
<path d="M60 58 Q64 61 68 58" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
<path d="M8 34 L120 30" stroke="#9AA1B0" stroke-width="4" stroke-linecap="round"/>
<path d="M8 34 L120 30" fill="none" {W(1.4)}/>
<path d="M112 22 L124 26 M112 38 L124 34" {W(2.4)}/>
<path d="M40 40 L30 34 M88 40 L98 32" {W(3)}/>
{sparkle(22, 16, 4)}{sparkle(100, 108, 5)}
''')

# 7. Taksim (Кутузовский пр-т, «Океания»): турецкий мороженщик дразнит рожком дондурмы
add("cafe-taksim-okeania",
    "турецкий мороженщик в красной феске с кисточкой и красном жилете",
    "с хитрой улыбкой протягивает на длинной металлической лопатке вафельный рожок с тягучей дондурмой",
    "zm_fez", f'''
<rect x="0" y="96" width="128" height="32" fill="#2E7D8C" {W(2.4)}/>
<path d="M0 104 L128 104" stroke="#F2C14E" stroke-width="3"/>
<path d="M28 96 Q30 70 46 66 L66 66 Q82 70 84 96Z" fill="#D9363E" {W(3)}/>
<path d="M46 66 L56 96 L66 66" fill="#FFFFFF" {W(2.4)}/>
<circle cx="56" cy="48" r="16" fill="#F2C9A0" {W(3)}/>
<path d="M44 34 L46 18 L66 18 L68 34Z" fill="#C8102E" {W(2.8)}/>
<path d="M56 18 Q50 16 46 26" fill="none" stroke="#1F1F1F" stroke-width="2.4"/>
<circle cx="45" cy="27" r="2.6" fill="#1F1F1F"/>
<path d="M48 46 Q51 43 54 46 M60 46 Q63 43 66 46" fill="none" {W(2.2)}/>
<path d="M46 52 Q56 50 66 52" fill="none" stroke="#3B3355" stroke-width="3"/>
<path d="M50 57 Q56 61 62 57" fill="none" {W(2)}/>
<path d="M80 76 L118 40" stroke="#B9BFCB" stroke-width="5" stroke-linecap="round"/>
<path d="M80 76 L118 40" fill="none" {W(1.4)}/>
<path d="M104 34 L116 58 L124 36Z" fill="#E7B36A" {W(2.4)}/>
<path d="M102 34 Q106 18 114 22 Q124 16 126 34Z" fill="#FFF6E4" {W(2.6)}/>
<path d="M112 24 Q110 12 116 8" fill="none" stroke="#FFF6E4" stroke-width="4" stroke-linecap="round"/>
<path d="M112 24 Q110 12 116 8" fill="none" {W(1.4)}/>
{sparkle(20, 24, 5)}{sparkle(96, 14, 3.5)}
''')

# 8. Тануки (ш. Энтузиастов): суши-нигири бежит марафон по шоссе с номером на поясе из нори
add("cafe-tanuki-entuziastov-50",
    "суши-нигири с оранжевым ломтиком лосося и поясом из нори с номером «50»",
    "бежит марафон по шоссе на тонких ножках, высунув язычок от усердия, а над дорогой — табличка «старт»",
    "zm_run", f'''
<path d="M0 94 L128 94 L128 128 L0 128Z" fill="#6F7586"/>
<path d="M6 110 L26 110 M46 110 L66 110 M86 110 L106 110" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round"/>
<path d="M8 30 L8 10 M120 30 L120 10" {W(3)}/>
<rect x="4" y="8" width="120" height="14" rx="3" fill="#FFD23F" {W(2.6)}/>
<path d="M20 15 L108 15" stroke="#E2362F" stroke-width="3" stroke-dasharray="6 5"/>
<path d="M52 84 L40 100 L32 100 M76 84 L86 98 L96 92" fill="none" {W(3.4)}/>
<path d="M30 62 Q30 44 64 44 Q98 44 98 62 Q98 84 64 86 Q30 84 30 62Z" fill="#FFFFFF" {W(3)}/>
<path d="M26 54 Q30 34 64 34 Q100 34 104 52 Q96 48 64 48 Q36 48 26 54Z" fill="#FF8A4C" {W(3)}/>
<path d="M44 40 Q52 38 58 42 M70 38 Q78 38 86 42" stroke="#FFD2B8" stroke-width="2.4" fill="none"/>
<rect x="54" y="48" width="20" height="38" fill="#244236" {W(2.4)}/>
<rect x="56" y="62" width="16" height="12" fill="#FFFFFF"/>
<text x="64" y="72" font-family="Arial" font-weight="bold" font-size="10" text-anchor="middle" fill="#3B3355">50</text>
{eye(42, 62, 0.7)}{eye(86, 62, 0.7)}
<path d="M40 72 Q46 76 50 72" fill="none" {W(2)}/>
<path d="M45 74 Q46 79 48 75" fill="#FF7FA8" {W(1.4)}/>
<path d="M30 66 L16 56 M98 66 L112 76" {W(3)}/>
<path d="M118 50 Q124 54 120 58 M114 44 Q122 44 122 48" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"/>
''')

# 9. Noba (Коммунарка, Скандинавский бул.): шведская булочка с кардамоном лепит снежок
add("cafe-noba-kommunarka",
    "шведская булочка-узелок с кардамоном и крупным жемчужным сахаром, в вязаной шапочке с узором-оленем",
    "лепит в варежках снежок посреди заснеженного двора с маленькими ёлочками",
    "zm_frost", f'''
<path d="M0 98 Q32 90 64 96 Q96 102 128 94 L128 128 L0 128Z" fill="#FFFFFF" {W(2.4)}/>
<path d="M14 92 L22 70 L30 92Z" fill="#3E8F64" {W(2.2)}/><path d="M100 90 L110 64 L120 90Z" fill="#3E8F64" {W(2.2)}/>
<path d="M18 80 L26 80 M104 78 L116 78" stroke="#FFFFFF" stroke-width="2.4"/>
<path d="M34 72 Q30 48 50 46 Q60 40 72 46 Q96 46 94 70 Q96 94 64 96 Q32 94 34 72Z" fill="#D99A4E" {W(3)}/>
<path d="M46 60 Q58 70 70 58 Q82 50 86 66 M44 78 Q56 70 70 82" fill="none" stroke="#A8692C" stroke-width="3"/>
<g fill="#FFFFFF" stroke="#3B3355" stroke-width="1"><circle cx="52" cy="54" r="2.4"/><circle cx="76" cy="50" r="2.4"/><circle cx="84" cy="74" r="2.2"/><circle cx="44" cy="86" r="2.2"/><circle cx="62" cy="88" r="2"/></g>
<path d="M38 50 Q40 20 64 18 Q88 20 90 50Z" fill="#2F5FB3" {W(3)}/>
<path d="M40 42 L88 42" stroke="#FFFFFF" stroke-width="4"/>
<path d="M58 30 L60 26 L62 30 L66 26 L68 30 M60 30 L60 36 L68 36 L68 30" fill="none" stroke="#FFFFFF" stroke-width="1.8"/>
<circle cx="64" cy="14" r="6" fill="#E2362F" {W(2.4)}/>
{eye(56, 66, 0.7)}{eye(74, 66, 0.7)}
<path d="M60 74 Q65 78 70 74" fill="none" {W(2)}/>
{BL(50, 74)}{BL(80, 74)}
<circle cx="104" cy="104" r="9" fill="#F4FAFF" {W(2.4)}/>
<path d="M90 84 L98 100" {W(3)}/>
<ellipse cx="96" cy="98" rx="6" ry="5" fill="#E2362F" {W(2.2)}/>
{sparkle(20, 30, 3.5, "#FFFFFF")}{sparkle(108, 24, 4.5, "#FFFFFF")}{sparkle(98, 44, 3, "#FFFFFF")}
''')

# 10. «Пили-ели чё хотэли» (Сосенки): бутылочка персикового лимонада взлетает на пузырьках
add("cafe-pili-eli-sosenki",
    "стеклянная бутылочка персикового лимонада с оранжевой этикеткой-персиком",
    "взлетает над столом, как ракета, на струе собственных пузырьков",
    "zm_peach", f'''
<rect x="0" y="108" width="128" height="20" fill="#C98B5A" {W(2.4)}/>
<g fill="#FFFFFF" stroke="#3B3355" stroke-width="1.6"><circle cx="58" cy="104" r="4"/><circle cx="70" cy="98" r="5"/><circle cx="62" cy="92" r="3"/><circle cx="48" cy="98" r="3.4"/><circle cx="78" cy="106" r="3"/></g>
<path d="M52 88 L52 46 Q52 36 58 32 L58 14 L70 14 L70 32 Q76 36 76 46 L76 88 Q76 92 64 92 Q52 92 52 88Z" fill="#FFD9A8" {W(3)}/>
<rect x="56" y="8" width="16" height="8" rx="2" fill="#E2362F" {W(2.4)}/>
<rect x="52" y="54" width="24" height="22" fill="#FF9F5A" {W(2.4)}/>
<circle cx="64" cy="65" r="7" fill="#FFB27A" {W(1.8)}/>
<path d="M64 58 Q68 54 70 56" fill="none" stroke="#5C9E3E" stroke-width="2.2"/>
{eye(59, 44, 0.6)}{eye(69, 44, 0.6)}
<path d="M60 50 Q64 53 68 50" fill="none" {W(1.8)}/>
<path d="M44 30 L36 22 M84 30 L92 22 M40 44 L30 44 M88 44 L98 44" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>
{sparkle(22, 70, 4.5)}{sparkle(106, 76, 5)}
''')


if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for pid in ids:
        open(os.path.join(OUT, pid + ".svg"), "w").write(ICONS[pid])
    if not sys.argv[1:]:
        reg = os.path.join(OUT, "subjects.txt")
        have = {l.split(" — ", 1)[0] for l in open(reg, encoding="utf-8")}
        with open(reg, "a", encoding="utf-8") as f:
            for pid in ICONS:
                if pid not in have:
                    f.write(f"{pid} — герой: {SUBJ[pid][0]} | сцена: {SUBJ[pid][1]}\n")
    print("svg:", len(ids))
