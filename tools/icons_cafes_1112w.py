"""Иконки робота cafes, 2026-11-12 (23 UTC). Каждая придумана и нарисована отдельно (правило АБСОЛЮТНОЙ уникальности):
герои и сцены сверены поиском по icons-src/subjects.txt; палитры фона — свои.
Запуск: python3 tools/icons_cafes_1112w.py [id…]  (без аргументов — все + строки реестра в subjects.txt)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
BL = lambda x, y: f'<ellipse cx="{x}" cy="{y}" rx="3.8" ry="2.2" fill="#FF7FA8" opacity=".7"/>'
draw_icons.BG.update({
    "zw_sunrise": ("#FFF1D6", "#F49A6C"),
    "zw_moon": ("#3A3F73", "#171B3D"),
    "zw_wall": ("#E8F7F1", "#7FC7B0"),
    "zw_paper": ("#FBF3E6", "#C9A27A"),
    "zw_skyblue": ("#EAF6FF", "#5FA8E8"),
    "zw_mimosa": ("#FFFBE0", "#E6C640"),
    "zw_lagoon": ("#D8FBFF", "#2BB3C8"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Якитория (Подольск): нигири с угрём потягивается под восходящим солнцем
add("cafe-yakitoriya-podolsk-lenina",
    "нигири с угрём унаги — глянцевый коричневый ломтик угря в соусе с кунжутом на белом рисовом брусочке, перехваченный поясом нори",
    "сладко потягивается, раскинув ручки, на фоне большого красного восходящего солнца — утро начинается",
    "zw_sunrise", f'''
<circle cx="98" cy="36" r="20" fill="#E8453C" opacity=".85"/>
<path d="M0 92 Q32 86 64 92 Q96 98 128 90 L128 128 L0 128Z" fill="#F7C9A0" opacity=".7"/>
<path d="M22 70 Q10 56 14 44 M106 70 Q118 56 114 44" fill="none" {W(3.4)}/>
<circle cx="14" cy="42" r="4" fill="#FFF7EC" {W(2.2)}/><circle cx="114" cy="42" r="4" fill="#FFF7EC" {W(2.2)}/>
<rect x="24" y="66" width="80" height="34" rx="15" fill="#FFFCF5" {W(3.2)}/>
<g fill="#EFE6D6"><ellipse cx="32" cy="94" rx="3" ry="1.8"/><ellipse cx="82" cy="96" rx="3" ry="1.8"/></g>
<path d="M20 70 Q22 54 44 54 Q64 50 86 54 Q108 54 108 70 Q90 78 64 76 Q38 78 20 70Z" fill="#8A4A24" {W(3.2)}/>
<path d="M30 62 Q50 58 70 60 Q88 60 100 64" fill="none" stroke="#C9874E" stroke-width="3" stroke-linecap="round" opacity=".8"/>
<g fill="#FFF3D6"><ellipse cx="40" cy="64" rx="1.6" ry="1"/><ellipse cx="58" cy="62" rx="1.6" ry="1"/><ellipse cx="76" cy="64" rx="1.6" ry="1"/><ellipse cx="90" cy="66" rx="1.6" ry="1"/></g>
<rect x="88" y="54" width="12" height="47" rx="2" fill="#1F3B2E" {W(2.6)}/>
{eye(50, 84, 0.85)}{eye(70, 84, 0.85)}
<ellipse cx="60" cy="93" rx="3.6" ry="3" fill="#E24B5B" {W(1.8)}/>
{BL(42, 91)}{BL(78, 91)}
<path d="M30 28 Q34 24 38 28 M90 22 Q94 18 98 22" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" opacity=".9"/>
''')

# 2. Додо (Домодедово, Лунная ул.): пицца-луноход на колёсиках-оливках едет по Луне
add("cafe-dodo-domodedovo-lunnaya",
    "круглая пицца-луноход с кружками пепперони, на шести чёрных колёсиках-оливках и с антенной-веточкой базилика",
    "едет по серой лунной поверхности с кратерами под звёздным небом, за ней тянутся следы колёс, вдали голубая Земля",
    "zw_moon", f'''
<g fill="#FFFFFF"><circle cx="16" cy="30" r="1.4"/><circle cx="40" cy="14" r="1.2"/><circle cx="74" cy="20" r="1.4"/><circle cx="56" cy="36" r="1"/><circle cx="20" cy="56" r="1.2"/></g>
<circle cx="104" cy="28" r="11" fill="#5BB0F0" {W(2.2)}/><path d="M98 24 Q104 20 108 26 Q104 32 99 30Z" fill="#6CCB6A"/>
<path d="M0 98 Q30 90 64 96 Q98 102 128 92 L128 128 L0 128Z" fill="#B9BCCB" {W(3)}/>
<ellipse cx="26" cy="112" rx="10" ry="3.6" fill="#9497AA"/><ellipse cx="96" cy="114" rx="8" ry="3" fill="#9497AA"/><ellipse cx="62" cy="120" rx="5" ry="2" fill="#9497AA"/>
<path d="M8 104 L18 102 M10 108 L20 106" stroke="#8C8FA2" stroke-width="2.4" stroke-linecap="round"/>
<path d="M88 44 Q86 32 80 26" fill="none" stroke="#2F7A3A" stroke-width="3" stroke-linecap="round"/>
<path d="M80 26 Q72 20 76 30 Q84 34 80 26Z" fill="#4CB050" {W(2)}/>
<ellipse cx="62" cy="68" rx="40" ry="22" fill="#E8A447" {W(3.2)}/>
<ellipse cx="62" cy="66" rx="33" ry="16" fill="#FFD25A"/>
<g fill="#D9473C" stroke="{O}" stroke-width="1.8"><circle cx="42" cy="64" r="5"/><circle cx="84" cy="62" r="5"/><circle cx="62" cy="56" r="4.4"/></g>
{eye(54, 70, 0.85)}{eye(72, 70, 0.85)}
<path d="M58 78 Q63 83 68 78" fill="none" {W(2)}/>
{BL(46, 76)}{BL(80, 76)}
<g fill="#2E2B33" stroke="{O}" stroke-width="2.2">
<ellipse cx="32" cy="92" rx="7" ry="6"/><ellipse cx="52" cy="95" rx="7" ry="6"/><ellipse cx="74" cy="95" rx="7" ry="6"/><ellipse cx="94" cy="92" rx="7" ry="6"/></g>
<g fill="#E8E2D0"><circle cx="32" cy="92" r="2"/><circle cx="52" cy="95" r="2"/><circle cx="74" cy="95" r="2"/><circle cx="94" cy="92" r="2"/></g>
''')

# 3. Додо (Электросталь): пицца-часы со стрелками-гриссини показывает время обеда
add("cafe-dodo-elektrostal-yalagina",
    "круглая пицца-часы: вместо цифр — кусочки пепперони по кругу, две стрелки — хлебные палочки гриссини",
    "висит на мятной стене кафе, стрелки показывают ровно полдень — время обеда, по бокам дрожат весёлые черточки «тик-так»",
    "zw_wall", f'''
<path d="M14 40 L22 44 M12 52 L22 52 M14 64 L22 60 M114 40 L106 44 M116 52 L106 52 M114 64 L106 60" stroke="{O}" stroke-width="2.8" stroke-linecap="round"/>
<circle cx="64" cy="66" r="44" fill="#D88A3A" {W(3.4)}/>
<circle cx="64" cy="66" r="36" fill="#FFCF5A" {W(2)}/>
<path d="M40 56 Q46 52 50 58 M80 86 Q86 82 90 88 M38 84 Q42 80 46 84" fill="none" stroke="#F3A93A" stroke-width="2.4" stroke-linecap="round"/>
<g fill="#D9473C" stroke="{O}" stroke-width="1.8"><circle cx="64" cy="35" r="4.6"/><circle cx="95" cy="66" r="4.6"/><circle cx="64" cy="97" r="4.6"/><circle cx="33" cy="66" r="4.6"/></g>
<g fill="#D9473C" opacity=".85"><circle cx="86" cy="44" r="2.6"/><circle cx="86" cy="88" r="2.6"/><circle cx="42" cy="88" r="2.6"/><circle cx="42" cy="44" r="2.6"/></g>
<rect x="61" y="30" width="6" height="38" rx="3" fill="#F4D7A0" {W(2.2)}/>
<rect x="60" y="40" width="8" height="28" rx="3" fill="#F4D7A0" {W(2.2)} transform="rotate(-8 64 66)"/>
<g stroke="#C79B5A" stroke-width="1.4" stroke-linecap="round"><path d="M62 36 L66 38 M62 44 L66 46 M62 52 L66 54"/></g>
<circle cx="64" cy="66" r="4" fill="#3B3355"/>
{eye(50, 74, 0.8)}{eye(78, 74, 0.8)}
<path d="M58 82 Q64 88 70 82" fill="none" {W(2)}/>
{BL(44, 80)}{BL(84, 80)}
<path d="M64 10 L64 22" stroke="{O}" stroke-width="2.6"/><circle cx="64" cy="9" r="3" fill="#7A6B5A" {W(1.8)}/>
''')

# 4. Здрасте (Дубининская ул.): баскский чизкейк сидит в пергаменте, как в кресле, и читает книжку
add("cafe-zdraste-dubininskaya-59a",
    "баскский чизкейк «Сан-Себастьян» — кремовый кусок с тёмной карамельной верхушкой в мятом коричневом пергаменте",
    "уютно устроился в загнутом пергаменте, как в кресле-мешке, и читает раскрытую детскую книжку с картинками",
    "zw_paper", f'''
<path d="M16 108 Q12 70 30 58 L44 64 L48 50 L62 60 L74 48 L84 62 L98 52 L104 66 L114 62 Q118 92 112 110 Q64 122 16 108Z" fill="#B88A5A" {W(3)}/>
<path d="M30 72 L40 100 M96 70 L88 100 M60 66 L62 104" stroke="#9C7046" stroke-width="2" stroke-linecap="round" opacity=".7"/>
<path d="M24 50 L106 72 L106 94 Q64 100 24 94Z" fill="#FFF0CF" {W(3.2)}/>
<path d="M24 50 Q22 44 30 44 Q70 52 106 66 Q110 70 106 74 L24 54Z" fill="#5A3218" {W(2.6)}/>
<path d="M34 54 Q60 60 96 70" fill="none" stroke="#8A4E26" stroke-width="2.4" stroke-linecap="round"/>
<path d="M28 60 Q32 66 28 72 M36 60 Q38 64 36 68" fill="none" stroke="#E8CC8E" stroke-width="2" stroke-linecap="round"/>
{eye(50, 74, 0.85)}{eye(72, 78, 0.85)}
<path d="M56 84 Q61 88 66 85" fill="none" {W(1.8)}/>
{BL(42, 80)}{BL(82, 86)}
<path d="M44 96 L64 90 L84 96 L84 112 L64 106 L44 112Z" fill="#FFFFFF" {W(2.6)}/>
<path d="M64 90 L64 106" {W(2)}/>
<circle cx="54" cy="100" r="3.2" fill="#FF9B5A"/><path d="M70 102 L78 98 L80 104Z" fill="#6CB7F0"/>
<path d="M40 92 Q36 98 44 100 M88 92 Q92 98 84 100" fill="none" {W(2.6)}/>
{sparkle(22, 30, 5)}{sparkle(104, 28, 4)}
''')

# 5. Здрасте (Люберцы, ул. Лётчика Ларюшина): кружка какао с маршмеллоу-облачками, сквозь пар пролетает самолётик
add("cafe-zdraste-lyubertsy-laryushina",
    "пузатая кружка горячего какао с тремя пухлыми розово-белыми маршмеллоу-облачками на шоколадной глади",
    "из кружки поднимается пар-облака, сквозь которые пролетает маленький красный биплан, а кружка радостно смотрит вверх",
    "zw_skyblue", f'''
<path d="M30 48 Q24 36 34 30 Q38 22 48 28 M76 40 Q78 30 88 30" fill="none" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round" opacity=".9"/>
<g transform="rotate(-12 82 24)">
<path d="M66 24 L98 22 Q102 24 98 28 L66 28Z" fill="#E8453C" {W(2.2)}/>
<rect x="76" y="14" width="6" height="22" rx="2" fill="#F27C5A" {W(2)}/>
<path d="M64 20 L68 32" {W(2.2)}/>
<circle cx="99" cy="25" r="2" fill="#3B3355"/>
</g>
<path d="M96 70 Q116 70 114 86 Q112 100 94 96" fill="none" stroke="#3B3355" stroke-width="3.2"/>
<path d="M96 74 Q110 74 108 86 Q106 94 94 92" fill="none" stroke="#2C8FD8" stroke-width="5"/>
<path d="M26 56 L100 56 L96 108 Q94 116 86 116 L40 116 Q32 116 30 108Z" fill="#2C8FD8" {W(3.2)}/>
<ellipse cx="63" cy="56" rx="37" ry="8" fill="#7A4424" {W(3)}/>
<g {W(2.2)}><rect x="36" y="44" width="16" height="13" rx="6" fill="#FFFFFF"/><rect x="54" y="42" width="16" height="13" rx="6" fill="#FFC6DA"/><rect x="72" y="45" width="15" height="12" rx="6" fill="#FFFFFF"/></g>
{eye(52, 84, 0.9)}{eye(74, 84, 0.9)}
<path d="M57 94 Q63 100 69 94" fill="none" {W(2.2)}/>
{BL(44, 92)}{BL(82, 92)}
''')

# 6. Здрасте (Люберцы, ул. 8 Марта): пирожное «Птичье молоко» поздравляет с веточкой мимозы
add("cafe-zdraste-lyubertsy-8-marta",
    "квадратное пирожное «Птичье молоко» — белое воздушное суфле в тонкой шоколадной глазури с волнистым узором",
    "держит в ручках пушистую веточку жёлтой мимозы и протягивает её, как подарок на праздник, вокруг порхают сердечки",
    "zw_mimosa", f'''
<path d="M28 104 Q64 112 100 104" fill="none" stroke="#C9A830" stroke-width="3" stroke-linecap="round" opacity=".6"/>
<rect x="30" y="46" width="68" height="56" rx="10" fill="#FFFDF4" {W(3.2)}/>
<path d="M30 58 L30 56 Q30 46 40 46 L88 46 Q98 46 98 56 L98 58Z" fill="#4A2A1A"/>
<rect x="30" y="46" width="68" height="14" rx="8" fill="#4A2A1A" {W(3)}/>
<path d="M38 52 Q44 48 50 52 Q56 56 62 52 Q68 48 74 52 Q80 56 86 52 Q90 50 92 52" fill="none" stroke="#8A5A3A" stroke-width="2" stroke-linecap="round"/>
<path d="M30 92 L98 92 L98 94 Q98 102 88 102 L40 102 Q30 102 30 94Z" fill="#4A2A1A" opacity=".9"/>
{eye(52, 72, 0.85)}{eye(76, 72, 0.85)}
<path d="M58 80 Q64 86 70 80" fill="none" {W(2)}/>
{BL(44, 80)}{BL(84, 80)}
<path d="M98 76 Q106 72 108 62" fill="none" {W(3)}/>
<path d="M108 66 Q110 46 104 30" fill="none" stroke="#6A9A3A" stroke-width="2.6" stroke-linecap="round"/>
<path d="M106 50 L116 44 M106 40 L96 34 M108 58 L118 56" stroke="#6A9A3A" stroke-width="2" stroke-linecap="round"/>
<g fill="#FFD21F" stroke="#C9A200" stroke-width="1"><circle cx="104" cy="28" r="4"/><circle cx="110" cy="24" r="3.4"/><circle cx="98" cy="30" r="3.2"/><circle cx="117" cy="42" r="3.6"/><circle cx="114" cy="48" r="3"/><circle cx="94" cy="34" r="3.2"/><circle cx="119" cy="55" r="3"/><circle cx="106" cy="22" r="2.8"/></g>
<path d="M22 30 Q18 24 22 22 Q26 20 26 26 Q26 20 30 22 Q34 24 30 30 L26 34Z" fill="#FF6F91" {W(1.6)}/>
<path d="M40 22 Q38 18 40 17 Q43 16 43 20 Q43 16 46 17 Q48 18 46 22 L43 25Z" fill="#FF8FAB" {W(1.4)}/>
''')

# 7. Эндемик (ул. Берзарина): пицца-остров с пальмой из базилика посреди лагуны
add("cafe-endemik-berzarina",
    "круглая пицца-остров с сырными пляжами, пальмой из листьев базилика и оливкой-кокосом",
    "лежит посреди бирюзовой лагуны, вокруг плещут волны, над островом светит солнце — единственный такой остров на свете",
    "zw_lagoon", f'''
<circle cx="104" cy="24" r="10" fill="#FFE36A" {W(2)}/>
<path d="M0 84 Q20 78 40 84 Q60 90 80 84 Q100 78 128 84 L128 128 L0 128Z" fill="#1E9CB4" opacity=".55"/>
<path d="M8 104 Q16 100 24 104 M100 108 Q108 104 116 108 M50 118 Q58 114 66 118" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>
<ellipse cx="60" cy="88" rx="44" ry="16" fill="#D68B3A" {W(3.2)}/>
<ellipse cx="60" cy="86" rx="37" ry="11" fill="#FFD25A"/>
<g fill="#D9473C" stroke="{O}" stroke-width="1.6"><ellipse cx="34" cy="86" rx="4.4" ry="2.6"/><ellipse cx="88" cy="84" rx="4.4" ry="2.6"/></g>
<path d="M62 84 Q60 60 66 36" fill="none" stroke="#8A5A2A" stroke-width="5" stroke-linecap="round"/>
<path d="M62 84 Q60 60 66 36" fill="none" {W(1.6)} opacity=".6"/>
<g {W(2.2)} fill="#3FA34D">
<path d="M66 36 Q50 26 36 36 Q52 32 66 38Z"/><path d="M66 36 Q82 24 96 34 Q80 32 66 38Z"/>
<path d="M66 36 Q54 40 46 54 Q58 44 66 38Z"/><path d="M66 36 Q80 40 86 54 Q76 44 66 38Z"/></g>
<circle cx="66" cy="40" r="4" fill="#2E2B33" {W(1.6)}/><circle cx="72" cy="38" r="3.4" fill="#2E2B33" {W(1.4)}/>
{eye(46, 92, 0.75)}{eye(76, 92, 0.75)}
<path d="M56 96 Q61 100 66 96" fill="none" {W(1.8)}/>
{BL(38, 97)}{BL(84, 97)}
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
